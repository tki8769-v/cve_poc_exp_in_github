"""扫描执行（REFACTOR_PLAN.md 3.6）：消费到期任务 → 搜索 → 三态过滤 → 合并。

按评审 R6/R7/G3 修订：
- 预算耗尽立即停止本轮：未尝试的任务**保持原状**（不改 attempts/due），
  正在处理的任务若已取得部分页则先幂等合并再登记未完成；零请求零新
  进展时任务字段完全不动（G8，含已有断点的任务）；
- 搜索不完整（截断/预算）时已取得页面照常合并，并持久化 resume_page
  供下次从断点续跑；分页达到 GitHub 1000 条上限时接受部分覆盖并标注；
- 单任务异常（重试耗尽/HTTP/写盘）不中止整轮：异常任务登记为可重试
  失败，已取得进度按有限批次提交落盘，后续任务继续（G3）；
- 任务结果批量落盘（一次读写），失败或部分结果不代表"没有 PoC"。
"""
from __future__ import annotations

from pathlib import Path

from . import RULES_VERSION
from . import scheduler
from . import state as state_mod
from .attrib import (
    ACCEPTED,
    CONFLICT_CANDIDATE,
    INSUFFICIENT_EVIDENCE,
    NEEDS_REVIEW,
    classify_relation,
)
from .blacklist import is_blocked, load_blacklist
from .ghsearch import Budget
from .parse import is_valid_cve_id, parse_github_repo

__all__ = ["scan", "merge_accepted"]

RELATIONS_SEARCH_DIR = "relations_search"
PAGINATION_CAP = "pagination_cap_at_page_"
TASK_BATCH_COMMIT = 5  # G3：outcomes 有限批次提交边界


def _shard_path(root: Path, year: str) -> Path:
    return state_mod.state_dir(root) / RELATIONS_SEARCH_DIR / f"{year}.jsonl"


def merge_accepted(root: Path, cve_id: str, url: str, item: dict,
                   verdict=None) -> bool:
    """合并一条 accepted 关系。返回 True 表示新增（首次发现）。

    - 跨通道去重：legacy 分片已有同键时不重复建关系/事件；
    - 墓碑恢复（评审 R5）：legacy 同键已被自动 rejected 而本轮取到
      accepted 证据（新描述等）→ 回退 needs_review 等待复核，不让
      同键去重吞掉新证据；
    - H5：verdict 提供时持久化接受原因与证据编号/时间，可追溯可重审。
    """
    year = cve_id.split("-")[1]
    legacy_path = state_mod.state_dir(root) / "relations" / f"{year}.jsonl"
    for record in state_mod.read_jsonl(legacy_path):
        if record["cve_id"] == cve_id and record["url"] == url:
            if (record.get("verification") == "rejected" and record.get("auto", True)
                    and is_valid_cve_id(record["cve_id"])):
                # I4：格式隔离墓碑（非法编号）不被新证据复活
                record.update({
                    "verification": "needs_review",
                    "revoked_from": "rejected",
                    "revoked_at": state_mod.now_iso(),
                    "revoked_reason": "fresh_scan_evidence",
                    "rule_version": RULES_VERSION,
                })
                _rewrite_record(legacy_path, record)
            return False

    path = _shard_path(root, year)
    existing = state_mod.read_jsonl(path)
    for record in existing:
        if record["cve_id"] == cve_id and record["url"] == url:
            record["stars"] = item.get("stargazers_count")
            record["forks"] = item.get("forks_count")
            record["last_seen_at"] = state_mod.now_iso()
            if verdict is not None and record.get("verification") == "accepted":
                record["accepted_reason"] = verdict.reason
                record["accepted_at"] = state_mod.now_iso()
            state_mod.write_jsonl(path, existing)
            return False

    owner, repo = parse_github_repo(url)
    accepted = {
        "cve_id": cve_id,
        "url": url,
        "owner": owner,
        "repo": repo,
        "source": "github_search",
        "verification": ACCEPTED,
        "first_seen_at": state_mod.now_iso(),
        "stars": item.get("stargazers_count"),
        "forks": item.get("forks_count"),
        "rule_version": RULES_VERSION,
    }
    if verdict is not None:
        accepted.update({
            "accepted_reason": verdict.reason,
            "accepted_url_ids": sorted(verdict.url_ids),
            "accepted_evidence_ids": sorted(verdict.evidence_ids),
            "accepted_at": state_mod.now_iso(),
        })
    existing.append(accepted)
    existing.sort(key=lambda r: (r["cve_id"], r["url"]))
    state_mod.write_jsonl(path, existing)
    return True


def _rewrite_record(path: Path, record: dict) -> None:
    rows = state_mod.read_jsonl(path)
    for index, row in enumerate(rows):
        if row["cve_id"] == record["cve_id"] and row["url"] == record["url"]:
            rows[index] = record
            break
    state_mod.write_jsonl(path, rows)


def _log_jsonl(root: Path, name: str, records: list[dict]) -> None:
    if not records:
        return
    stamped = [{**r, "ts": state_mod.now_iso()} for r in records]
    state_mod.append_jsonl(state_mod.state_dir(root) / name, stamped)


def scan(client, root: Path, limit_tasks: int = 50, budget_requests: int | None = None,
         budget_seconds: float | None = None, max_pages: int = 3) -> dict:
    budget = Budget(max_requests=budget_requests, max_seconds=budget_seconds)
    tasks = scheduler.due_tasks(root, limit=limit_tasks)
    stats = {
        "tasks_due": len(tasks),
        "scanned": 0,
        "scanned_by_priority": {},  # P1.4：分类服务数（验证防饿死轮转）
        "new_relations": 0,
        "rejected_at_collection": 0,
        "needs_review": 0,
        "blocked": 0,
        "incomplete": 0,
        "task_errors": 0,
        "invalid_id_skipped": 0,
        "budget_stopped": False,
    }
    blacklist = load_blacklist(root)
    outcomes: list[tuple[str, dict]] = []

    for task in tasks:
        cve_id = task["cve_id"]
        if not is_valid_cve_id(cve_id):
            # H2：非法编号任务确定性移除，不扫描（其关系由迁移隔离）
            scheduler.cancel(root, cve_id)
            stats["invalid_id_skipped"] += 1
            continue
        resume_page = max(1, int(task.get("resume_page", 1) or 1))
        found_any = bool(task.get("scan_found_any"))
        stop = False
        try:
            result = client.search_repositories(
                f'"{cve_id}"', max_pages=max_pages, budget=budget,
                start_page=resume_page,
            )

            found = False
            rejected: list[dict] = []
            review: list[dict] = []
            new_events: list[dict] = []
            for item in result.items:  # 部分页照常合并（R6）
                url = item.get("html_url") or ""
                if not url:
                    continue
                if is_blocked(url, blacklist):
                    stats["blocked"] += 1
                    continue
                topics = " ".join(item.get("topics") or [])
                verdict = classify_relation(
                    cve_id, url,
                    repo_description=item.get("description") or "",
                    extra_text=topics,
                )
                if verdict.state == ACCEPTED:
                    found = True
                    if merge_accepted(root, cve_id, url, item, verdict=verdict):
                        stats["new_relations"] += 1
                        new_events.append(
                            {"ts": state_mod.now_iso(), "type": "new_poc", "cve_id": cve_id, "url": url}
                        )
                elif verdict.state == CONFLICT_CANDIDATE:
                    rejected.append({"cve_id": cve_id, "url": url, "reason": verdict.reason,
                                     "url_ids": verdict.url_ids})
                elif verdict.state in (NEEDS_REVIEW, INSUFFICIENT_EVIDENCE):
                    review.append({"cve_id": cve_id, "url": url, "reason": verdict.reason,
                                   "description": (item.get("description") or "")[:200]})
            found_any = found_any or found

            stats["rejected_at_collection"] += len(rejected)
            stats["needs_review"] += len(review)
            _log_jsonl(root, "rejected_at_collection.jsonl", rejected)
            _log_jsonl(root, "needs_review.jsonl", review)
            if new_events:
                state_mod.append_jsonl(state_mod.state_dir(root) / "events.jsonl", new_events)

            stats["scanned"] += 1
            prio_key = str(task.get("priority", 9))
            stats["scanned_by_priority"][prio_key] = stats["scanned_by_priority"].get(prio_key, 0) + 1

            if result.stop_reason == "budget":
                # F3/F12：预算耗尽与截断走同一"提交已完成页 + 保存断点"路径
                if result.pages == 0:
                    # G8：零请求零新进展——任务保持原状（含已有断点与
                    # 调度字段），后续未尝试任务同样不动（R7）
                    stats["budget_stopped"] = True
                    stats["scanned"] -= 1  # 本任务未实际尝试
                    stop = True
                else:
                    outcomes.append((cve_id, {
                        "found_any": found_any, "complete": False,
                        "note": "; ".join(result.errors),
                        "resume_page": result.pages + 1,
                    }))
                    stats["budget_stopped"] = True
                    stop = True  # 后续任务未尝试，不再遍历（R7）
            elif result.complete:
                outcomes.append((cve_id, {"found_any": found_any, "complete": True}))
            elif result.stop_reason == "pagination_cap":
                # F12：覆盖上限被接受为"调度完成"，但显式保留部分覆盖状态
                outcomes.append((cve_id, {"found_any": found_any, "complete": True,
                                          "coverage_partial": True}))
                stats["incomplete"] += 1
            elif result.stop_reason == "incomplete_results":
                # 服务端声明当前页不完整：本页不可视为已完成，原起点重试
                stats["incomplete"] += 1
                outcomes.append((cve_id, {"found_any": found_any, "complete": False,
                                          "note": "; ".join(result.errors),
                                          "resume_page": resume_page}))
            else:  # truncated：合并过部分页后从断点续跑（R6）
                stats["incomplete"] += 1
                outcomes.append((cve_id, {"found_any": found_any, "complete": False,
                                          "note": "; ".join(result.errors),
                                          "resume_page": result.pages + 1 if result.pages else resume_page}))
        except Exception as exc:  # G3：单任务异常不中止整轮、不丢前面任务的进度
            stats["task_errors"] += 1
            outcomes.append((cve_id, {
                "found_any": found_any, "complete": False,
                "note": f"task error: {exc}"[:200],
                "resume_page": resume_page,  # 本轮无新进展，保留既有断点
            }))

        # G3：有限批次提交——预算退出/单任务异常前，已取得进度已落盘
        if stop or len(outcomes) >= TASK_BATCH_COMMIT:
            scheduler.apply_results(root, outcomes)
            outcomes = []
        if stop:
            break

    scheduler.apply_results(root, outcomes)
    return stats
