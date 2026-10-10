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

    def _run_window(start: datetime, end: datetime, attempts: int) -> str:
        """处理一个时间窗口，返回 complete / cap / incomplete。"""
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
        if result.stop_reason == "pagination_cap":
            return "cap"
        return "incomplete"

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
        outcome = _run_window(_parse(entry["start"]), _parse(entry["end"]),
                              int(entry.get("attempts", 1)))
        if outcome == "complete":
            continue
        if outcome == "cap":
            _split_or_unresolve(_parse(entry["start"]), _parse(entry["end"]), "cap")
            continue
        # 预算/网络不完整：原窗口放回队首，下轮续跑
        entry["attempts"] = int(entry.get("attempts", 1)) + 1
        pending.insert(0, entry)
        stats["stop_reason"] = "incomplete pending window"
        stopped = True
        break

    # 2) 日期窗口推进：超量拆分入队后继续下一日，不阻塞
    day = start_day
    while not stopped:
        day_start = datetime.strptime(day, "%Y-%m-%d").replace(tzinfo=timezone.utc)
        day_end = day_start + timedelta(days=1)
        if day_start > now:
            break
        end = min(day_end, now)
        outcome = _run_window(day_start, end, 1)
        if outcome == "incomplete":
            stopped = True
            stats["stop_reason"] = "incomplete current window"
            break  # last_date 不推进，该日下轮重扫（幂等合并去重）
        if outcome == "cap":
            _split_or_unresolve(day_start, end, "cap")
        if day >= today:
            break
        day = (day_start + timedelta(days=1)).strftime("%Y-%m-%d")

    stats["window"] = f"{start_day}..{today}"
    stats["windows_pending"] = len(pending)
    stats["unresolved_total"] = len(unresolved)
    stats["requests_used"] = budget.requests_used if budget is not None else None

    if not dry_run:
        advanced = (not stopped) and day >= today and not pending
        cursor.update({"last_date": today if advanced else last_date,
                       "windows": pending, "unresolved": unresolved})
        if advanced:
            stats["cursor_advanced"] = True
        _save_cursor(root, cursor)
    return stats
