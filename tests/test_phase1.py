"""主动发现改造第一阶段：topics 证据一致、阶段预算、防饿死轮转、基础指标。"""
from __future__ import annotations

from collections import Counter
from pathlib import Path

from collector import scheduler
from collector import state as state_mod
from collector.backfill import backfill, load_meta
from collector.clean import clean_apply
from collector.ghsearch import Budget, SearchResult
from collector.pipeline import daily
from collector.scan import scan


class FakeMetaClient:
    def get_repo(self, owner, repo, budget=None):
        return {
            "id": 101, "description": "poc for CVE-2020-0796",
            "topics": ["cve-2020-0796", "poc"],
            "stargazers_count": 3, "forks_count": 0,
            "updated_at": "t", "pushed_at": "t",
            "archived": False, "default_branch": "main",
        }


def test_p11_backfill_persists_topics(tmp_path: Path):
    """P1.1：元数据回补保存 topics，采集与重审证据同源。"""
    state_mod.write_json(state_mod.state_dir(tmp_path) / "meta_backfill_queue.json",
                         [{"owner": "a", "repo": "poc"}])
    report = backfill(FakeMetaClient(), tmp_path, limit=5)
    assert report["fetched"] == 1
    meta = load_meta(tmp_path)
    assert meta[("a", "poc")]["topics"] == ["cve-2020-0796", "poc"]


def _legacy(cve_id, url, verification, **extra):
    owner, repo = url.rstrip("/").split("/")[-2:]
    return {"cve_id": cve_id, "url": url, "owner": owner, "repo": repo,
            "source": "legacy_markdown", "verification": verification, **extra}


def _recheck_ready(root: Path):
    recheck_dir = state_mod.state_dir(root) / "recheck"
    state_mod.write_json(recheck_dir / "report.json", {"missing_meta": 0, "conflicts_total": 0})


def test_p11_topics_supported_accept_not_downgraded(tmp_path: Path):
    """P1.1：topics 命中接受的记录，描述不含编号不得降级（证据完整时刷新保留）。"""
    root = tmp_path
    (root / "2026").mkdir()
    (root / "2026" / "README.md").write_text("", encoding="utf-8")
    relations_path = state_mod.state_dir(root) / "relations" / "2026.jsonl"
    # URL 无编号、无 accepted_reason（旧格式），采集时靠 topics 接受
    state_mod.write_jsonl(relations_path, [
        _legacy("CVE-2026-0300", "https://github.com/a/silent-repo", "accepted"),
    ])
    _recheck_ready(root)
    # 完整证据：描述沉默，但 topics 明确提及目标
    state_mod.write_jsonl(state_mod.state_dir(root) / "repo_meta.jsonl", [{
        "owner": "a", "repo": "silent-repo", "fetched_at": state_mod.now_iso(),
        "description": "just some tool", "topics": ["cve-2026-0300"],
    }])
    report = clean_apply(root)
    assert report["revoked_accepted"] == 0
    record = state_mod.read_jsonl(relations_path)[0]
    assert record["verification"] == "accepted"
    assert record["accepted_reason"] == "desc_contains_target_only"  # 刷新保留
    assert record["accepted_evidence_ids"] == ["CVE-2026-0300"]


def test_p11_missing_topics_field_is_not_counter_evidence(tmp_path: Path):
    """P1.1：旧缓存无 topics 字段 = 证据不完整——不降级 accepted，也不复活墓碑。"""
    root = tmp_path
    (root / "2026").mkdir()
    (root / "2026" / "README.md").write_text("", encoding="utf-8")
    relations_path = state_mod.state_dir(root) / "relations" / "2026.jsonl"
    state_mod.write_jsonl(relations_path, [
        # 描述矛盾（提及另一编号），但缓存无 topics——按不完整证据维持原状
        _legacy("CVE-2026-0400", "https://github.com/a/old-cache", "accepted"),
        # 自动墓碑，缓存无 topics——不据此复活
        _legacy("CVE-2026-0401", "https://github.com/b/tomb", "rejected",
                auto=True, rejected_reason="evidenced_foreign_id",
                rejected_evidence="x", rejected_evidence_fetched_at="t"),
    ])
    _recheck_ready(root)
    state_mod.write_jsonl(state_mod.state_dir(root) / "repo_meta.jsonl", [
        {"owner": "a", "repo": "old-cache", "fetched_at": state_mod.now_iso(),
         "description": "regression of CVE-2026-0400, related to CVE-2026-0002"},  # 无 topics 键
        {"owner": "b", "repo": "tomb", "fetched_at": state_mod.now_iso(),
         "description": "poc for CVE-2026-0401"},  # 无 topics 键
    ])
    report = clean_apply(root)
    assert report["revoked_accepted"] == 0   # 不降级
    assert report["revoked_rejected"] == 0   # 不复活
    by_url = {r["url"]: r for r in state_mod.read_jsonl(relations_path)}
    assert by_url["https://github.com/a/old-cache"]["verification"] == "accepted"
    assert by_url["https://github.com/b/tomb"]["verification"] == "rejected"


def test_p13_due_tasks_weighted_round_robin(tmp_path: Path):
    """P1.3：大量 P0 到期时，P5/P8 周期重扫每轮仍获得确定份额。"""
    tasks = []
    for i in range(60):
        tasks.append({"cve_id": f"CVE-2026-{i:04d}", "priority": scheduler.PRIORITY_NEW,
                      "due_at": "2020-01-01T00:00:00Z"})
    for i in range(30):
        tasks.append({"cve_id": f"CVE-2019-{i:04d}", "priority": scheduler.PRIORITY_FOUND,
                      "due_at": "2020-01-02T00:00:00Z"})
    for i in range(20):
        tasks.append({"cve_id": f"CVE-2015-{i:04d}", "priority": scheduler.PRIORITY_NOT_FOUND,
                      "due_at": "2020-01-03T00:00:00Z"})
    state_mod.write_jsonl(tmp_path / "state" / "scan_tasks.jsonl", tasks)

    selected = scheduler.due_tasks(tmp_path, limit=30)
    counts = Counter(t["priority"] for t in selected)
    assert len(selected) == 30
    # 5:3:2 加权轮转：三类都有确定份额，且 P0 仍占多数
    assert counts[scheduler.PRIORITY_NEW] >= 15
    assert counts[scheduler.PRIORITY_FOUND] >= 8
    assert counts[scheduler.PRIORITY_NOT_FOUND] >= 5

    # 到期数不超过 limit 时全量返回（原语义保留）
    assert len(scheduler.due_tasks(tmp_path, limit=200)) == 110


class _DailyClient:
    """覆盖 daily 各阶段接口的最小客户端。"""

    def list_releases(self, per_page=30, page=1, budget=None):
        return []

    def download_asset(self, url, budget=None):
        return b""

    def search_repositories(self, query, max_pages=3, budget=None, start_page=1):
        if "created:" in query:
            return SearchResult()
        return SearchResult(items=[{
            "html_url": "https://github.com/x/CVE-2026-0500-poc",
            "description": "poc for CVE-2026-0500",
            "stargazers_count": 1, "forks_count": 0,
        }])

    def get_repo(self, owner, repo, budget=None):
        return {"id": 1, "description": "poc", "topics": [],
                "stargazers_count": 1, "forks_count": 0, "updated_at": "t",
                "pushed_at": "t", "archived": False, "default_branch": "main"}


def test_p12_stage_budgets_and_timing_metrics(tmp_path: Path, monkeypatch):
    """P1.2/P1.4：前置阶段预算封顶；last_run 含阶段耗时与分类观测。"""
    from collector import cvesource
    from collector import pipeline

    root = tmp_path
    (root / "2026").mkdir()
    (root / "2026" / "README.md").write_text("", encoding="utf-8")
    state_mod.write_jsonl(state_mod.state_dir(root) / "relations" / "2026.jsonl", [
        _legacy("CVE-2026-0500", "https://github.com/x/CVE-2026-0500-poc", "accepted",
                owner="x", repo="CVE-2026-0500-poc"),
    ])

    captured = {}

    def fake_sync(client, root_, all_releases=False, max_releases=30, budget=None):
        captured["sync_budget"] = budget.max_seconds if budget else None
        return {"releases_seen": 0, "releases_processed": 0, "cves_seen": 0,
                "new_tasks": 0, "rejected": 0, "last_tag": None, "floor_tag": None,
                "continuity_warning": False, "budget_stopped": False}

    monkeypatch.setattr(pipeline.cvesource, "sync", fake_sync)
    scheduler.enqueue(root, "CVE-2026-0500", "new")  # 让 scan 本轮实际服务一个任务

    summary = daily(root, client=_DailyClient(), scan_requests=5, scan_minutes=1,
                    backfill_limit=2, backfill_minutes=0.5, time_budget_minutes=10)

    # P1.2：sync 只拿整轮预算的 30% 封顶，scan 必有执行机会
    assert captured["sync_budget"] is not None
    assert captured["sync_budget"] <= 10 * 60 * pipeline.SYNC_STAGE_SHARE
    # P1.4：阶段耗时与分类观测入 last_run
    assert summary["ok"] is True
    timing = summary["steps"]["timing"]
    assert {"sync", "repo_watch", "scan", "verify"} <= set(timing)
    queue = summary["steps"]["queue"]
    assert "oldest_due_by_priority" in queue
    # scan 分类服务数
    assert summary["steps"]["scan"]["scanned_by_priority"]
    # repo_watch 渠道成本骨架
    assert "requests_used" in summary["steps"]["repo_watch"]


def test_p11_backfill_refreshes_cache_missing_topics(tmp_path: Path):
    """P1.1：缓存刚抓取但缺 topics 键（旧缓存）也进入刷新——证据补齐不被 30 天 TTL 卡住。"""
    state_mod.write_jsonl(tmp_path / "state" / "repo_meta.jsonl", [{
        "owner": "a", "repo": "poc", "fetched_at": state_mod.now_iso(),
        "description": "old",  # 无 topics 键：证据不完整
    }])
    state_mod.write_json(state_mod.state_dir(tmp_path) / "meta_backfill_queue.json",
                         [{"owner": "a", "repo": "poc"}])
    report = backfill(FakeMetaClient(), tmp_path, limit=5, max_age_days=30)
    assert report["fetched"] == 1
    assert load_meta(tmp_path)[("a", "poc")]["topics"] == ["cve-2020-0796", "poc"]
