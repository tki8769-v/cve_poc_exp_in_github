"""仓库侧 pushed 增量通道（主动发现改造阶段 2B，实施方案 §1.5/§4.1）。

覆盖缺口：老仓库（早于监控起点、不在 created 窗口内）出现新推送时，只要
其元数据含 CVE 线索即可被发现——不等待对应 CVE 的周期重扫。

边界（如实记录，不冒充完整覆盖）：本通道只找"元数据已有 CVE 线索"的仓库；
元数据无线索的老仓库新增 PoC 文件，仍需后续 README 取证与重点仓库巡检。

按实施方案的技术共识实现：
- 独立游标（repo_pushed_cursor.json），与 created 通道互不代推；
- 超 1,000 条窗口做**时间拆分**（12h→6h→3h→1h），不照搬 created 通道的
  有限次放弃策略；最小粒度仍超量时记录 unresolved 缺口并暴露计数，绝不
  静默标记完成；
- 待处理子窗口每轮限量先行处理（J1 教训：旧工作不得饿死当前日期）；
- 幂等合并复用 process_repo_items（source=github_pushed）。
"""
from __future__ import annotations

from datetime import datetime, timedelta, timezone
from pathlib import Path

from . import state as state_mod
from .ghsearch import Budget
from .repo_watch import process_repo_items

__all__ = ["discover_pushed"]

CURSOR_FILE = "repo_pushed_cursor.json"
QUERY_TEMPLATE = "CVE in:name,description,topics pushed:{start}..{end}"
FIRST_LOOKBACK_DAYS = 2
MAX_CATCHUP_DAYS = 30
MIN_WINDOW = timedelta(hours=1)          # 拆分下限：仍超量则记 unresolved
MAX_PENDING_WINDOWS_PER_RUN = 6          # 待处理子窗口每轮限量（防饿死新日期）
DEFAULT_MAX_PAGES = 3


def _now() -> datetime:
    return datetime.now(timezone.utc).replace(minute=0, second=0, microsecond=0)


def _fmt(moment: datetime) -> str:
    return moment.strftime("%Y-%m-%dT%H:%M:%SZ")


def _parse(value: str) -> datetime:
    return datetime.strptime(value, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)


def _load_cursor(root: Path) -> dict:
    return state_mod.read_json(state_mod.state_dir(root) / CURSOR_FILE,
                               default={"last_date": None, "windows": [],
                                        "unresolved": []})


def _save_cursor(root: Path, cursor: dict) -> None:
    state_mod.write_json(state_mod.state_dir(root) / CURSOR_FILE, cursor)


def discover_pushed(client, root: Path, max_pages: int = DEFAULT_MAX_PAGES,
                    dry_run: bool = False, budget: Budget | None = None) -> dict:
    cursor = _load_cursor(root)
    now = _now()
    today = now.strftime("%Y-%m-%d")

    stats = {
        "window": None,
        "repos_seen": 0,
        "new_relations": 0,
        "accepted_existing": 0,
        "rejected_at_collection": 0,
        "needs_review": 0,
        "blocked": 0,
        "invalid_ids": 0,
        "windows_done": 0,
        "splits": 0,
        "windows_pending": 0,
        "unresolved_total": 0,
        "unresolved_added": 0,
        "cursor_advanced": False,
        "requests_used": 0,
        "stop_reason": None,
        "warning": None,
    }

    pending: list[dict] = [dict(w) for w in (cursor.get("windows") or [])]
    unresolved: list[dict] = list(cursor.get("unresolved") or [])
    last_date = cursor.get("last_date")
    start_day = last_date or (now - timedelta(days=FIRST_LOOKBACK_DAYS)).strftime("%Y-%m-%d")

    span = (datetime.strptime(today, "%Y-%m-%d") - datetime.strptime(start_day, "%Y-%m-%d")).days
    if span > MAX_CATCHUP_DAYS:
        # 长停机：老区间记录为 unresolved 摘要（不静默丢弃），从近期重启
        unresolved.append({"from": start_day, "to": today, "note": "catchup_cap_reset"})
        stats["unresolved_added"] += 1
        start_day = (now - timedelta(days=FIRST_LOOKBACK_DAYS)).strftime("%Y-%m-%d")
        stats["warning"] = f"游标落后 {span} 天超过上限，老区间转入 unresolved"

    from .blacklist import load_blacklist
    blacklist = load_blacklist(root)

    def _run_window(start: datetime, end: datetime) -> str:
        """处理一个时间窗口，返回 complete / cap / truncated / budget / incomplete。"""
        if end <= start:
            return "complete"  # 零长度窗口（当日刚过零点）：无需查询
        result = client.search_repositories(
            QUERY_TEMPLATE.format(start=_fmt(start), end=_fmt(end)),
            max_pages=max_pages, budget=budget,
        )
        stats["repos_seen"] += len(result.items)
        process_repo_items(root, result.items, stats, dry_run=dry_run,
                           source="github_pushed", blacklist=blacklist)
        stats["windows_done"] += 1
        if result.complete:
            return "complete"
        reason = result.stop_reason or "incomplete"
        return {"pagination_cap": "cap"}.get(reason, reason)

    def _split_or_unresolve(start: datetime, end: datetime, total_hint: str) -> None:
        if end - start > MIN_WINDOW:
            middle = start + (end - start) / 2
            pending.append({"start": _fmt(start), "end": _fmt(middle), "attempts": 1})
            pending.append({"start": _fmt(middle), "end": _fmt(end), "attempts": 1})
            stats["splits"] += 1
        else:
            unresolved.append({"start": _fmt(start), "end": _fmt(end),
                               "note": f"min_window_cap {total_hint}"})
            stats["unresolved_added"] += 1

    stopped = False

    # 1) 待处理子窗口限量先行（J1：旧工作不得饿死当前日期）
    for _ in range(MAX_PENDING_WINDOWS_PER_RUN):
        if not pending:
            break
        entry = pending.pop(0)
        outcome = _run_window(_parse(entry["start"]), _parse(entry["end"]))
        if outcome == "complete":
            continue
        if outcome in ("cap", "truncated"):
            # 超量（1000 上限）与本轮页数截断同治：时间拆分
            _split_or_unresolve(_parse(entry["start"]), _parse(entry["end"]), outcome)
            continue
        # 预算/网络不完整：原窗口放回队首，下轮续跑
        entry["attempts"] = int(entry.get("attempts", 1)) + 1
        pending.insert(0, entry)
        stats["stop_reason"] = "incomplete pending window"
        stopped = True
        break

    # 2) 完整日期窗口（结束于此刻之前）：complete 或已拆分入队即视为该日
    #    已处理（覆盖状态由窗口队列承载，J1 模式），游标推进不被拆分阻塞；
    #    预算/网络不完整停在该日，下轮重扫（幂等合并去重）
    day = start_day
    covered_through = None  # 最后一个已处理（完整覆盖或已拆分）的完整日
    while not stopped:
        day_start = datetime.strptime(day, "%Y-%m-%d").replace(tzinfo=timezone.utc)
        day_end = day_start + timedelta(days=1)
        if day_end > now:
            break  # 剩下的只有"当日"，交给快照处理
        outcome = _run_window(day_start, day_end)
        if outcome in ("complete", "cap", "truncated"):
            if outcome != "complete":
                _split_or_unresolve(day_start, day_end, outcome)
            covered_through = day
            day = (day_start + timedelta(days=1)).strftime("%Y-%m-%d")
            continue
        # budget / 服务端不完整：停住，游标不越过该日
        stats["stop_reason"] = f"{outcome} full day window"
        stopped = True
        break

    # 3) 当日快照（天然部分覆盖：只到此刻）：仅吸收结果，不影响游标语义
    #    ——当日的权威覆盖由次日的完整日查询完成（幂等合并去重）。
    #    修复实测缺陷：此前当日窗口的截断/预算结果会永久阻塞游标推进。
    if not stopped:
        today_start = datetime.strptime(today, "%Y-%m-%d").replace(tzinfo=timezone.utc)
        if now > today_start:
            _run_window(today_start, now)

    stats["window"] = f"{start_day}..{today}"
    stats["windows_pending"] = len(pending)
    stats["unresolved_total"] = len(unresolved)
    stats["requests_used"] = budget.requests_used if budget is not None else None

    if not dry_run:
        # 游标推进：全部完整日处理完毕（无预算停）→ last_date=今天（与
        # created 通道的重叠日语义一致：当日每轮重查）；中途预算停 →
        # 停在前一个已处理日。待处理窗口队列不阻塞日期推进。
        if covered_through is not None and not stopped:
            new_last_date = today
        elif covered_through is not None:
            new_last_date = covered_through
        else:
            new_last_date = last_date
        cursor.update({"last_date": new_last_date,
                       "windows": pending, "unresolved": unresolved})
        if new_last_date != last_date:
            stats["cursor_advanced"] = True
        _save_cursor(root, cursor)
    return stats
