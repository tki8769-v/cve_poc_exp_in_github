"""调度策略与扫描合并测试。"""
from __future__ import annotations

from pathlib import Path

from collector import scheduler
from collector import state as state_mod
from collector.ghsearch import SearchResult
from collector.scan import scan


class FakeScanClient:
    def __init__(self, result: SearchResult):
        self.result = result
        self.calls = []

    def search_repositories(self, query, max_pages=3, budget=None, start_page=1):
        self.calls.append(query)
        return self.result


def test_enqueue_dedupe_and_refresh(tmp_path: Path):
    assert scheduler.enqueue(tmp_path, "CVE-2026-0001", "new", description="d1") == 1
    assert scheduler.enqueue(tmp_path, "cve-2026-0001", "new") == 0  # 大小写归一
    tasks = scheduler.load_tasks(tmp_path)
    assert len(tasks) == 1
    assert tasks[0]["description"] == "d1"


def test_record_result_found_reschedules_weekly(tmp_path: Path):
    scheduler.enqueue(tmp_path, "CVE-2026-0001", "new")
    scheduler.record_result(tmp_path, "CVE-2026-0001", found=True, complete=True)
    tasks = scheduler.load_tasks(tmp_path)
    assert tasks[0]["reason"] == "rescan"
    assert tasks[0]["priority"] == scheduler.PRIORITY_FOUND
    assert tasks[0]["due_at"] > state_mod.now_iso()
    assert scheduler.due_tasks(tmp_path) == []  # 未来到期，不出队


def test_record_result_not_found_backoff_sequence(tmp_path: Path):
    scheduler.enqueue(tmp_path, "CVE-2026-0002", "new")
    prev_due = ""
    for expected_attempts in (1, 2, 3):
        scheduler.record_result(tmp_path, "CVE-2026-0002", found=False, complete=True)
        tasks = {t["cve_id"]: t for t in scheduler.load_tasks(tmp_path)}
        task = tasks["CVE-2026-0002"]
        assert task["attempts"] == expected_attempts
        assert task["due_at"] > prev_due  # 逐次退避拉长
        prev_due = task["due_at"]


def test_record_result_incomplete_keeps_task_retry_soon(tmp_path: Path):
    scheduler.enqueue(tmp_path, "CVE-2026-0003", "new")
    scheduler.record_result(tmp_path, "CVE-2026-0003", found=False, complete=False, note="budget")
    tasks = {t["cve_id"]: t for t in scheduler.load_tasks(tmp_path)}
    task = tasks["CVE-2026-0003"]
    assert task["attempts"] == 1
    assert task["last_outcome"].startswith("incomplete")
    assert task["due_at"] > state_mod.now_iso()


def test_cancel_removes_task(tmp_path: Path):
    scheduler.enqueue(tmp_path, "CVE-2026-0004", "new")
    scheduler.cancel(tmp_path, "CVE-2026-0004")
    assert scheduler.load_tasks(tmp_path) == []


def _result(items, complete=True, errors=None, stop_reason="complete"):
    return SearchResult(items=items, complete=complete, errors=errors or [],
                        stop_reason=stop_reason)


def test_scan_merges_accepted_and_blocks_conflicts(tmp_path: Path):
    scheduler.enqueue(tmp_path, "CVE-2026-0001", "new")
    result = _result(
        [
            {
                "html_url": "https://github.com/a/CVE-2026-0001-poc",
                "description": "poc for CVE-2026-0001",
                "stargazers_count": 10,
                "forks_count": 2,
            },
            {
                "html_url": "https://github.com/b/CVE-2026-00011",
                "description": "another CVE-2026-00011 tool",
                "stargazers_count": 5,
                "forks_count": 0,
            },
            {
                "html_url": "https://github.com/c/some-tool",
                "description": None,
                "stargazers_count": 1,
                "forks_count": 0,
            },
        ]
    )
    stats = scan(FakeScanClient(result), tmp_path, limit_tasks=5)

    assert stats["scanned"] == 1
    assert stats["new_relations"] == 1
    assert stats["rejected_at_collection"] == 1
    assert stats["needs_review"] == 1

    relations = state_mod.read_jsonl(tmp_path / "state" / "relations_search" / "2026.jsonl")
    assert len(relations) == 1
    assert relations[0]["url"].endswith("CVE-2026-0001-poc")
    assert relations[0]["source"] == "github_search"
    assert relations[0]["verification"] == "accepted"

    rejected = state_mod.read_jsonl(tmp_path / "state" / "rejected_at_collection.jsonl")
    assert rejected[0]["reason"] == "prefix_conflict_evidenced"

    events = state_mod.read_jsonl(tmp_path / "state" / "events.jsonl")
    assert events and events[0]["type"] == "new_poc"

    # 扫描完成：任务按 found 重排为周级重扫
    tasks = scheduler.load_tasks(tmp_path)
    assert tasks[0]["last_outcome"] == "found"


def test_scan_incomplete_keeps_task(tmp_path: Path):
    """R7：预算耗尽且无已取得数据时，任务保持原状、立即停止本轮。"""
    scheduler.enqueue(tmp_path, "CVE-2026-0009", "new")
    stats = scan(FakeScanClient(_result([], complete=False, errors=["request budget exhausted (0)"], stop_reason="budget")), tmp_path)
    assert stats["budget_stopped"] is True
    assert stats["incomplete"] == 0
    tasks = {t["cve_id"]: t for t in scheduler.load_tasks(tmp_path)}
    task = tasks["CVE-2026-0009"]
    assert task["attempts"] == 0          # 未尝试的任务不被记成失败
    assert task["last_outcome"] is None
    assert task["due_at"] <= state_mod.now_iso()  # 仍到期可重试


def test_scan_dedupes_relation_on_rerun(tmp_path: Path):
    scheduler.enqueue(tmp_path, "CVE-2026-0002", "new")
    items = [{"html_url": "https://github.com/a/x-CVE-2026-0002",
              "description": "poc CVE-2026-0002", "stargazers_count": 3, "forks_count": 0}]
    scan(FakeScanClient(_result(items)), tmp_path)
    # 模拟到期重扫
    tasks = scheduler.load_tasks(tmp_path)
    tasks[0]["due_at"] = "2000-01-01T00:00:00Z"
    state_mod.write_jsonl(tmp_path / "state" / "scan_tasks.jsonl", tasks)
    scan(FakeScanClient(_result(items)), tmp_path)

    relations = state_mod.read_jsonl(tmp_path / "state" / "relations_search" / "2026.jsonl")
    assert len(relations) == 1  # 不重复
    assert relations[0]["last_seen_at"]  # 统计被刷新
    events = state_mod.read_jsonl(tmp_path / "state" / "events.jsonl")
    assert len(events) == 1  # 不重复产生 new_poc 事件


def test_scan_zero_budget_leaves_unattempted_tasks_untouched(tmp_path: Path):
    """评审 R7：预算为 0 时，所有任务保持原状，attempts 不增长。"""
    for i in range(3):
        scheduler.enqueue(tmp_path, f"CVE-2026-000{i}", "new")
    # 模拟真实客户端在预算 0 下的返回：未取得任何数据、预算错误
    exhausted = _result([], complete=False, errors=["request budget exhausted (0)"], stop_reason="budget")
    stats = scan(FakeScanClient(exhausted), tmp_path, budget_requests=0)
    assert stats["budget_stopped"] is True
    tasks = scheduler.load_tasks(tmp_path)
    assert len(tasks) == 3
    assert all(t["attempts"] == 0 for t in tasks)
    assert all(t["last_outcome"] is None for t in tasks)


def test_g4_enqueue_many_new_task_priority(tmp_path: Path):
    """评审 G4：批量入队的新建任务与单条 enqueue 一致使用最高优先级。"""
    created = scheduler.enqueue_many(tmp_path, [{"cve_id": "CVE-2026-0910", "reason": "new"}])
    assert created == 1
    assert scheduler.load_tasks(tmp_path)[0]["priority"] == scheduler.PRIORITY_NEW

    # rescan 等历史重扫仍是普通优先级
    scheduler.enqueue_many(tmp_path, [{"cve_id": "CVE-2026-0911", "reason": "rescan"}])
    by_id = {t["cve_id"]: t for t in scheduler.load_tasks(tmp_path)}
    assert by_id["CVE-2026-0911"]["priority"] == scheduler.PRIORITY_FOUND


def test_g5_partial_coverage_does_not_grow_empty_streak(tmp_path: Path):
    """评审 G5：pagination_cap 部分覆盖且无命中，不增长 empty_streak。"""
    scheduler.enqueue(tmp_path, "CVE-2026-0911", "new")
    scheduler.apply_results(tmp_path, [(
        "CVE-2026-0911", {"found_any": False, "complete": True, "coverage_partial": True},
    )])
    task = {t["cve_id"]: t for t in scheduler.load_tasks(tmp_path)}["CVE-2026-0911"]
    assert task["last_outcome"] == "partial: pagination_cap"
    assert task["coverage_partial"] is True
    assert task.get("empty_streak", 0) == 0          # 未增长
    assert task["priority"] == scheduler.PRIORITY_FOUND

    # 部分覆盖但有命中：与 found 相同的短周期重扫
    scheduler.enqueue(tmp_path, "CVE-2026-0912", "new")
    scheduler.apply_results(tmp_path, [(
        "CVE-2026-0912", {"found_any": True, "complete": True, "coverage_partial": True},
    )])
    task2 = {t["cve_id"]: t for t in scheduler.load_tasks(tmp_path)}["CVE-2026-0912"]
    assert task2["empty_streak"] == 0
    assert task2["coverage_partial"] is True


def test_g8_zero_request_keeps_resumed_task_untouched(tmp_path: Path):
    """评审 G8：预算耗尽且零请求时，已有断点的任务字段完全不变。"""
    scheduler.enqueue(tmp_path, "CVE-2026-0912", "new")
    tasks = scheduler.load_tasks(tmp_path)
    tasks[0]["resume_page"] = 4
    tasks[0]["scan_found_any"] = True
    state_mod.write_jsonl(tmp_path / "state" / "scan_tasks.jsonl", tasks)
    before = scheduler.load_tasks(tmp_path)[0]

    exhausted = _result([], complete=False, errors=["request budget exhausted (0)"],
                        stop_reason="budget")
    stats = scan(FakeScanClient(exhausted), tmp_path, budget_requests=0)

    assert stats["budget_stopped"] is True
    after = {t["cve_id"]: t for t in scheduler.load_tasks(tmp_path)}["CVE-2026-0912"]
    assert after["attempts"] == 0
    assert after["resume_page"] == 4
    assert after["scan_found_any"] is True
    assert after["due_at"] == before["due_at"]


def test_g3_later_task_error_keeps_earlier_progress(tmp_path: Path):
    """评审 G3：任务 B 异常不得丢掉任务 A 已取得的分页断点，整轮不中止。"""
    scheduler.enqueue(tmp_path, "CVE-2026-0920", "new")
    scheduler.enqueue(tmp_path, "CVE-2026-0921", "new")

    class FlakyClient:
        def __init__(self):
            self.calls = 0

        def search_repositories(self, query, max_pages=3, budget=None, start_page=1):
            self.calls += 1
            if "CVE-2026-0920" in query:
                return SearchResult(items=[], complete=False, stop_reason="truncated",
                                    errors=["truncated at page 3"], pages=3)
            raise RuntimeError("simulated retry exhaustion")

    stats = scan(FlakyClient(), tmp_path, limit_tasks=5)

    assert stats["task_errors"] == 1
    assert stats["scanned"] == 1
    tasks = {t["cve_id"]: t for t in scheduler.load_tasks(tmp_path)}
    a = tasks["CVE-2026-0920"]
    assert a["attempts"] == 1
    assert a["resume_page"] == 4                    # A 的断点已落盘
    assert a["last_outcome"].startswith("incomplete")
    b = tasks["CVE-2026-0921"]
    assert b["attempts"] == 1                        # B 记为可重试失败
    assert "task error" in b["last_outcome"]
