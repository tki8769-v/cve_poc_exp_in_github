"""仓库侧增量发现（REFACTOR_PLAN.md 3.9 双通道的仓库向通道）。

解决"老 CVE 出现新 PoC"的时效性：检索最近新建、名称/描述含 CVE 字样
的仓库（`created:` 日期窗口），反查 CVE 编号做精确归属——与 CVE 年龄
无关。

按评审修订：
- R6：窗口不完整（预算/截断）时已取得页面照常幂等合并，游标不推进，
  下轮重试；
- R12：dry_run 为真正的只读模式（不写关系/事件/任务/游标，黑名单照常
  生效）；
- R9：官方 REJECTED 的 CVE 不建关系不入队；
- R11：接受预算参数，等待不超预算；
- H2：非法编号（序号不足 4 位）跳过并计数，不进入状态；
- H4/I3：单日结果达搜索上限时按日期去重记录部分覆盖（有限次重试后
  放弃），主窗口先行、补扫后置——超量日与未完成补扫都不阻塞新日期。
"""
from __future__ import annotations

from datetime import datetime, timedelta, timezone
from pathlib import Path

from . import cvestate
from . import scheduler
from . import state as state_mod
from .attrib import ACCEPTED, CONFLICT_CANDIDATE, classify_relation
from .blacklist import is_blocked, load_blacklist
from .ghsearch import Budget
from .parse import extract_cve_ids, is_valid_cve_id
from .scan import merge_accepted

__all__ = ["discover"]

CURSOR_FILE = "repo_watch_cursor.json"
QUERY_TEMPLATE = "CVE in:name,description created:{start}..{end}"
FIRST_LOOKBACK_DAYS = 2
MAX_CATCHUP_DAYS = 30
MAX_PARTIAL_DAY_ATTEMPTS = 3  # H4：超量日重试上限，超过则记为放弃


def _today() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


def _day_offset(base: str, days: int) -> str:
    moment = datetime.strptime(base, "%Y-%m-%d").replace(tzinfo=timezone.utc) + timedelta(days=days)
    return moment.strftime("%Y-%m-%d")


def _load_cursor(root: Path) -> dict:
    return state_mod.read_json(state_mod.state_dir(root) / CURSOR_FILE,
                               default={"last_date": None, "partial_days": []})


def discover(client, root: Path, max_pages: int = 10, dry_run: bool = False,
             budget: Budget | None = None) -> dict:
    cursor = _load_cursor(root)
    today = _today()
    if cursor.get("last_date"):
        start = cursor["last_date"]  # 窗口含上次日期：重叠一天，幂等去重
    else:
        start = _day_offset(today, -FIRST_LOOKBACK_DAYS)

    stats = {
        "window": f"{start}..{today}",
        "repos_seen": 0,
        "cves_hit": 0,
        "new_relations": 0,
        "rejected_at_collection": 0,
        "needs_review": 0,
        "blocked": 0,
        "invalid_ids": 0,
        "partial_days_pending": 0,
        "partial_days_dropped": 0,
        "complete": True,
        "cursor_advanced": False,
        "warning": None,
    }
    blacklist = load_blacklist(root)

    span_days = (datetime.strptime(today, "%Y-%m-%d")
                 - datetime.strptime(start, "%Y-%m-%d")).days
    if span_days > MAX_CATCHUP_DAYS:
        stats["warning"] = (
            f"游标落后 {span_days} 天超过追赶上限 {MAX_CATCHUP_DAYS}，"
            f"从 {today} 前重新开始（历史窗口由周期对账兜底）"
        )
        start = _day_offset(today, -FIRST_LOOKBACK_DAYS)
        stats["window"] = f"{start}..{today}"

    hit_cves: set[str] = set()

    def _search_one(day_str: str):
        return client.search_repositories(
            QUERY_TEMPLATE.format(start=day_str, end=day_str),
            max_pages=max_pages, budget=budget,
        )

    def _absorb(result) -> str:
        """合并一个日窗口的已取得结果。返回 complete / cap / incomplete。"""
        stats["repos_seen"] += len(result.items)
        for item in result.items:
            url = item.get("html_url") or ""
            if not url:
                continue
            if is_blocked(url, blacklist):
                stats["blocked"] += 1
                continue
            description = item.get("description") or ""
            topics = " ".join(item.get("topics") or [])
            ids = extract_cve_ids(item.get("name") or "", description, topics)
            if not ids:
                continue  # 仓库无编号线索（如仅 README 提及），由正向通道兜底
            for cve_id in sorted(ids):
                if not is_valid_cve_id(cve_id):
                    stats["invalid_ids"] += 1  # H2：非法编号不进入状态
                    continue
                if cvestate.is_rejected(root, cve_id):
                    continue  # R9：官方撤回的编号不激活
                verdict = classify_relation(cve_id, url, repo_description=description,
                                            extra_text=topics)
                if verdict.state == ACCEPTED:
                    hit_cves.add(cve_id)
                    if not dry_run and merge_accepted(root, cve_id, url, item,
                                                      verdict=verdict):
                        stats["new_relations"] += 1
                        state_mod.append_jsonl(
                            state_mod.state_dir(root) / "events.jsonl",
                            [{"ts": state_mod.now_iso(), "type": "new_poc",
                              "cve_id": cve_id, "url": url}],
                        )
                elif verdict.state == CONFLICT_CANDIDATE:
                    stats["rejected_at_collection"] += 1
                    if not dry_run:
                        state_mod.append_jsonl(
                            state_mod.state_dir(root) / "rejected_at_collection.jsonl",
                            [{"ts": state_mod.now_iso(), "cve_id": cve_id, "url": url,
                              "reason": verdict.reason, "channel": "repo_watch"}],
                        )
                else:
                    stats["needs_review"] += 1
        if result.complete:
            return "complete"
        if result.stop_reason == "pagination_cap":
            return "cap"
        return "incomplete"

    # I3：主窗口先行（时效优先），历史超量日补扫后置——未完成的补扫
    # 不得阻塞当日新窗口。超量日按日期去重入队，达上限即放弃。
    def _queue_day(date_str: str) -> None:
        for i, entry in enumerate(queue):
            if entry["date"] == date_str:
                entry["attempts"] = int(entry.get("attempts", 0)) + 1
                if entry["attempts"] >= MAX_PARTIAL_DAY_ATTEMPTS:
                    queue.pop(i)
                    stats["partial_days_dropped"] += 1
                return
        queue.append({"date": date_str, "attempts": 1})

    queue: list[dict] = [dict(entry) for entry in (cursor.get("partial_days") or [])]

    day = start
    while stats["complete"]:
        result = _search_one(day)
        outcome = _absorb(result)
        if outcome == "incomplete":
            stats["complete"] = False
            stats["warning"] = "; ".join(result.errors) or "incomplete"
            break
        if outcome == "cap":
            _queue_day(day)
        else:
            # 重叠日补齐即出队（主窗口与补扫共用同一重试计数，I3 去重）
            queue[:] = [e for e in queue if e["date"] != day]
        if day >= today:
            break
        day = _day_offset(day, 1)

    # 历史超量日补扫：仅在主窗口完成后执行；重叠日（>= start）由主窗口
    # 覆盖，不重复查询。零请求零新进展不计尝试（G8 原则），其余真实尝试
    # 无论结果如何都推进重试计数，保证有限次后放弃
    index = 0
    while index < len(queue) and stats["complete"]:
        entry = queue[index]
        if entry["date"] >= start:
            index += 1
            continue
        result = _search_one(entry["date"])
        outcome = _absorb(result)
        if outcome == "complete":
            queue.pop(index)
            continue
        real_attempt = (outcome == "cap" or result.pages > 0
                        or bool(result.items) or result.stop_reason != "budget")
        if real_attempt:
            entry["attempts"] = int(entry.get("attempts", 0)) + 1
        if entry["attempts"] >= MAX_PARTIAL_DAY_ATTEMPTS:
            queue.pop(index)
            stats["partial_days_dropped"] += 1
            continue
        index += 1
        if not real_attempt and result.stop_reason == "budget":
            break  # 预算耗尽：停止补扫，主窗口已完成不受影响

    # 命中但尚无调度任务的 CVE 建立任务进入 7 天重扫循环（R9 守卫在
    # enqueue 内部：REJECTED 编号不入队）；dry_run 不写任何状态
    if not dry_run:
        known = {t["cve_id"] for t in scheduler.load_tasks(root)}
        for cve_id in hit_cves:
            if cve_id not in known:
                scheduler.enqueue(root, cve_id, reason="modified")

    stats["cves_hit"] = len(hit_cves)
    stats["partial_days_pending"] = len(queue)
    if not dry_run:
        if stats["complete"]:
            state_mod.write_json(state_mod.state_dir(root) / CURSOR_FILE,
                                 {"last_date": today, "partial_days": queue})
            stats["cursor_advanced"] = True
        elif queue or cursor.get("last_date"):
            # 不完整：last_date 不推进，但持久化已变化的部分覆盖队列（H4）
            state_mod.write_json(state_mod.state_dir(root) / CURSOR_FILE,
                                 {"last_date": cursor.get("last_date"),
                                  "partial_days": queue})
    return stats
