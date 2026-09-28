"""待扫队列与降频调度（REFACTOR_PLAN.md 3.6 / 评审 4.3）。

设计要点：
- 所有 CVE（含当前零 PoC 的）都保留 next_due：任务文件兼任调度表；
- 有发现 → 短周期重扫（FOUND_RESCAN_DAYS）；无发现 → 指数退避
  （NOT_FOUND_BACKOFF_DAYS 序列，封顶 90 天），实现“新活跃高频、
  长期无结果降频”；
- 结果不完整（预算耗尽/搜索截断）不清任务：attempts+1、短暂延后重试，
  失败或部分结果不代表“没有 PoC”；
- 全部写入原子落盘，崩溃后重跑按 due_at 自然恢复。
"""
from __future__ import annotations

from datetime import datetime, timedelta, timezone
from pathlib import Path

from . import state as state_mod
from .parse import is_valid_cve_id

__all__ = [
    "TASKS_FILE",
    "FOUND_RESCAN_DAYS",
    "NOT_FOUND_BACKOFF_DAYS",
    "load_tasks",
    "enqueue",
    "cancel",
    "due_tasks",
    "record_result",
]

FOUND_RESCAN_DAYS = 7
NOT_FOUND_BACKOFF_DAYS = [1, 2, 4, 8, 16, 32, 64, 90]
INCOMPLETE_RETRY_MINUTES = 5

# 优先级：数字越小越先扫
PRIORITY_NEW = 0
PRIORITY_FOUND = 5
PRIORITY_NOT_FOUND = 8


def _tasks_path(root: Path) -> Path:
    return state_mod.state_dir(root) / "scan_tasks.jsonl"


def load_tasks(root: Path) -> list[dict]:
    return state_mod.read_jsonl(_tasks_path(root))


def _save(root: Path, tasks: list[dict]) -> None:
    tasks.sort(key=lambda t: (t.get("priority", 9), t.get("due_at", ""), t.get("cve_id", "")))
    state_mod.write_jsonl(_tasks_path(root), tasks)


def _default_priority(reason: str) -> int:
    """新建任务的默认优先级（G4）：新发现/修改 = 最高优先级。"""
    return PRIORITY_NEW if reason in ("new", "modified") else PRIORITY_FOUND


def enqueue(root: Path, cve_id: str, reason: str, description: str = "") -> int:
    """入队/刷新任务。返回 1 表示新建，0 表示已存在（仅刷新）。

    已被官方 REJECTED 的 CVE 不入队（评审 R9）。
    """
    from . import cvestate

    cve_id = cve_id.upper()
    if not is_valid_cve_id(cve_id):
        return 0  # H2：非法编号不入队
    if cvestate.is_rejected(root, cve_id):
        return 0
    tasks = load_tasks(root)
    now = state_mod.now_iso()
    for task in tasks:
        if task["cve_id"] == cve_id:
            if reason in ("new", "modified"):
                task["reason"] = "modified"
                task["priority"] = min(task.get("priority", PRIORITY_NEW), PRIORITY_NEW)
                task["due_at"] = now
                if description:
                    task["description"] = description
            _save(root, tasks)
            return 0
    tasks.append(
        {
            "cve_id": cve_id,
            "reason": reason,
            "priority": _default_priority(reason),
            "due_at": now,
            "enqueued_at": now,
            "attempts": 0,
            "last_outcome": None,
            "description": description,
        }
    )
    _save(root, tasks)
    return 1


def cancel(root: Path, cve_id: str) -> None:
    cancel_many(root, [cve_id])


def cancel_many(root: Path, cve_ids: list[str]) -> None:
    """批量取消任务（单次读写）。"""
    drop = {c.upper() for c in cve_ids}
    tasks = [t for t in load_tasks(root) if t["cve_id"] not in drop]
    _save(root, tasks)


def due_tasks(root: Path, limit: int = 50) -> list[dict]:
    now = state_mod.now_iso()
    return [t for t in load_tasks(root) if t.get("due_at", "") <= now][:limit]


def enqueue_many(root: Path, items: list[dict]) -> int:
    """批量入队（评审 R7：避免逐条全表重写）。items: {cve_id, reason, due_at, priority, description?}。"""
    from . import cvestate

    tasks = load_tasks(root)
    existing = {t["cve_id"]: t for t in tasks}
    now = state_mod.now_iso()
    created = 0
    for item in items:
        cve_id = item["cve_id"].upper()
        if not is_valid_cve_id(cve_id):
            continue  # H2：非法编号不入队
        if cvestate.is_rejected(root, cve_id):
            continue
        task = existing.get(cve_id)
        if task is None:
            task = {
                "cve_id": cve_id,
                "reason": item.get("reason", "rescan"),
                "priority": item.get("priority",
                                     _default_priority(item.get("reason", "rescan"))),
                "due_at": item.get("due_at", now),
                "enqueued_at": now,
                "attempts": 0,
                "last_outcome": None,
                "description": item.get("description", ""),
            }
            tasks.append(task)
            existing[cve_id] = task
            created += 1
        else:
            if item.get("reason") in ("new", "modified"):
                task["reason"] = "modified"
                task["priority"] = min(task.get("priority", PRIORITY_FOUND), PRIORITY_NEW)
                task["due_at"] = now
            due = item.get("due_at", now)
            if due < task.get("due_at", now):  # 只提前不推迟
                task["due_at"] = due
            if item.get("description"):
                task["description"] = item["description"]
    _save(root, tasks)
    return created


def record_result(root: Path, cve_id: str, found: bool, complete: bool, note: str = "",
                  resume_page: int | None = None) -> None:
    apply_results(root, [(cve_id, {"found": found, "complete": complete,
                                   "note": note, "resume_page": resume_page})])


def apply_results(root: Path, results: list[tuple[str, dict]]) -> None:
    """批量记录扫描结果（评审 R7/F12：一次加载一次落盘）。

    逻辑扫描状态机：
    - complete=True：整次扫描结束才判定 found/none；empty_streak 只统计
      "完整扫描且无结果" 的连续次数（预算中断不计入退避）；
    - complete=False：保存 resume_page 与累计 scan_found_any，短暂延后
      从断点续跑（预算耗尽与截断走同一路径，F3）；
    - coverage_partial：达到分页上限被接受的部分覆盖，显式保留。
    """
    if not results:
        return
    tasks = load_tasks(root)
    index = {t["cve_id"]: t for t in tasks}
    for cve_id, outcome in results:
        task = index.get(cve_id.upper())
        if task is None:
            continue
        complete = outcome.get("complete", True)
        task["attempts"] = task.get("attempts", 0) + 1
        if not complete:
            task["last_outcome"] = f"incomplete: {outcome.get('note', '')}"[:200]
            task["due_at"] = _shift(minutes=INCOMPLETE_RETRY_MINUTES)
            task["scan_found_any"] = bool(task.get("scan_found_any")) or bool(outcome.get("found_any"))
            page = outcome.get("resume_page")
            if page:
                task["resume_page"] = max(1, min(page, 10))
            continue
        found = bool(outcome.get("found_any") or outcome.get("found"))
        task.pop("resume_page", None)
        task.pop("scan_found_any", None)
        if outcome.get("coverage_partial"):
            task["coverage_partial"] = True
            task["last_outcome"] = "partial: pagination_cap"
            task["reason"] = "rescan"
            task["priority"] = PRIORITY_FOUND
            if found:
                task["due_at"] = _shift(days=FOUND_RESCAN_DAYS)
                task["empty_streak"] = 0
            else:
                # G5：部分覆盖不构成"完整空结果"——不增长 empty_streak，
                # 以短周期补扫代替退避推进
                task["due_at"] = _shift(days=1)
            continue
        task.pop("coverage_partial", None)
        task["last_outcome"] = "found" if found else "none"
        if found:
            task["reason"] = "rescan"
            task["priority"] = PRIORITY_FOUND
            task["due_at"] = _shift(days=FOUND_RESCAN_DAYS)
            task["empty_streak"] = 0
        else:
            streak = task.get("empty_streak", 0) + 1
            task["empty_streak"] = streak
            task["reason"] = "rescan"
            task["priority"] = PRIORITY_NOT_FOUND
            idx = min(streak - 1, len(NOT_FOUND_BACKOFF_DAYS) - 1)
            task["due_at"] = _shift(days=NOT_FOUND_BACKOFF_DAYS[idx])
    _save(root, tasks)


def normalize_priorities(root: Path) -> int:
    """G4 迁移：reason=new/modified 的既有任务优先级压回 PRIORITY_NEW（幂等）。

    修复批量入队曾把新 CVE 建成 PRIORITY_FOUND 的部署。
    """
    tasks = load_tasks(root)
    patched = 0
    for task in tasks:
        if (task.get("reason") in ("new", "modified")
                and task.get("priority", PRIORITY_NEW) > PRIORITY_NEW):
            task["priority"] = PRIORITY_NEW
            patched += 1
    if patched:
        _save(root, tasks)
    return patched


def _shift(**kwargs) -> str:
    moment = datetime.now(timezone.utc) + timedelta(**kwargs)
    return moment.strftime("%Y-%m-%dT%H:%M:%SZ")
