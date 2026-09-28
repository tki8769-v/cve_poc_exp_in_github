"""仓库侧增量发现（repo_watch）与黑名单测试。"""
from __future__ import annotations

from pathlib import Path

import pytest

from collector import state as state_mod
from collector.blacklist import is_blocked, load_blacklist
from collector.ghsearch import SearchResult
from collector.repo_watch import discover, CURSOR_FILE


class FakeDiscoverClient:
    def __init__(self, result=None, queries=None):
        self.result = result if result is not None else SearchResult()
        self.queries = queries if queries is not None else []
        self.calls = []

    def search_repositories(self, query, max_pages=10, budget=None, start_page=1):
        self.calls.append(query)
        return self.result


def _repo_item(name, url=None, description="", topics=None):
    return {
        "html_url": url or f"https://github.com/o/{name}",
        "name": name,
        "description": description,
        "topics": topics or [],
        "stargazers_count": 3,
        "forks_count": 0,
    }


def _preset_cursor(tmp_path: Path) -> None:
    """预置游标到今天：首跑回看窗口收敛为单日，断言计数确定。"""
    from datetime import datetime, timezone

    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    state_mod.write_json(tmp_path / "state" / CURSOR_FILE, {"last_date": today})


def test_blacklist_loading_and_match(tmp_path: Path):
    (tmp_path / "blacklist.txt").write_text(
        "https://github.com/bad/actor\n\nhttps://github.com/evil\n", encoding="utf-8")
    entries = load_blacklist(tmp_path)
    assert entries == ["https://github.com/bad/actor", "https://github.com/evil"]
    assert is_blocked("https://github.com/bad/actor/poc", entries)
    assert not is_blocked("https://github.com/good/repo", entries)


def test_discover_finds_poc_for_old_cve(tmp_path: Path):
    """老 CVE（不在任务表、无历史关系）的新 PoC 仓库应被发现并建立关系。"""
    _preset_cursor(tmp_path)
    client = FakeDiscoverClient(result=SearchResult(items=[
        _repo_item("CVE-2015-57115", description="Mass Checker For CVE-2015-57115"),
        _repo_item("mytool-CVE-2014-0160", description="exploit for CVE-2014-0160"),
    ]))
    stats = discover(client, tmp_path)

    assert stats["complete"] is True
    assert stats["cursor_advanced"] is True
    # 两个仓库命中两个不同年份的老 CVE
    assert stats["cves_hit"] == 2
    relations = (state_mod.read_jsonl(tmp_path / "state" / "relations_search" / "2015.jsonl")
                 + state_mod.read_jsonl(tmp_path / "state" / "relations_search" / "2014.jsonl"))
    urls = {r["url"] for r in relations}
    assert any("CVE-2015-57115" in u for u in urls)
    assert any("CVE-2014-0160" in u for u in urls)
    # 事件与调度任务建立（进入 7 天重扫循环）
    events = state_mod.read_jsonl(tmp_path / "state" / "events.jsonl")
    assert {e["cve_id"] for e in events} == {"CVE-2015-57115", "CVE-2014-0160"}
    tasks = {t["cve_id"] for t in state_mod.read_jsonl(tmp_path / "state" / "scan_tasks.jsonl")}
    assert {"CVE-2015-57115", "CVE-2014-0160"} <= tasks


def test_discover_desc_mention_collects_both(tmp_path: Path):
    """URL 编号的直接收录；regression 类描述提及只登记待复核（R4 保守规则）。"""
    _preset_cursor(tmp_path)
    client = FakeDiscoverClient(result=SearchResult(items=[
        _repo_item("CVE-2024-6387", url="https://github.com/x/CVE-2024-6387",
                   description="regression of CVE-2006-5051"),
    ]))
    stats = discover(client, tmp_path)
    # CVE-2024-6387：URL 证据 → 收录；CVE-2006-5051：URL 他指 + 描述提及 → 待复核不收录
    assert stats["new_relations"] == 1
    assert stats["needs_review"] == 1
    assert state_mod.read_jsonl(tmp_path / "state" / "relations_search" / "2024.jsonl")
    assert not (tmp_path / "state" / "relations_search" / "2006.jsonl").exists()


def test_discover_skips_repos_without_cve_ids(tmp_path: Path):
    """无编号线索的仓库跳过（由正向通道兜底），不产生关系。"""
    _preset_cursor(tmp_path)
    client = FakeDiscoverClient(result=SearchResult(items=[
        _repo_item("PrintNightmare-Tool", description="just a scanner"),
    ]))
    stats = discover(client, tmp_path)
    assert stats["repos_seen"] == 1
    assert stats["cves_hit"] == 0
    assert stats["new_relations"] == 0


def test_discover_incomplete_keeps_cursor(tmp_path: Path):
    client = FakeDiscoverClient(
        result=SearchResult(items=[], complete=False, errors=["truncated"]))
    stats = discover(client, tmp_path)
    assert stats["complete"] is False
    assert stats["cursor_advanced"] is False
    assert not (tmp_path / "state" / CURSOR_FILE).exists()


def test_discover_idempotent_rerun(tmp_path: Path):
    result = SearchResult(items=[_repo_item("tool-CVE-2019-0708",
                                            description="bluekeep CVE-2019-0708")])
    first = discover(FakeDiscoverClient(result), tmp_path)
    second = discover(FakeDiscoverClient(result), tmp_path)

    assert first["new_relations"] == 1
    assert second["new_relations"] == 0  # 重复发现不新增关系
    events = state_mod.read_jsonl(tmp_path / "state" / "events.jsonl")
    assert len(events) == 1


def test_discover_does_not_duplicate_legacy_relations(tmp_path: Path):
    """上游已收录的关系不算新发现：不重复建关系、不产生虚假 new_poc 事件。"""
    _preset_cursor(tmp_path)
    state_mod.write_jsonl(tmp_path / "state" / "relations" / "2015.jsonl", [{
        "cve_id": "CVE-2015-57115", "url": "https://github.com/o/CVE-2015-57115",
        "owner": "o", "repo": "CVE-2015-57115",
        "source": "legacy_markdown", "verification": "pending",
    }])
    client = FakeDiscoverClient(result=SearchResult(items=[
        _repo_item("CVE-2015-57115", url="https://github.com/o/CVE-2015-57115",
                   description="Mass Checker For CVE-2015-57115"),
    ]))
    stats = discover(client, tmp_path)

    assert stats["new_relations"] == 0
    assert state_mod.read_jsonl(tmp_path / "state" / "events.jsonl") == []
    # search 分片不写重复记录
    assert not (tmp_path / "state" / "relations_search" / "2015.jsonl").exists()


def test_discover_respects_blacklist(tmp_path: Path):
    _preset_cursor(tmp_path)
    (tmp_path / "blacklist.txt").write_text(
        "https://github.com/o/blocked-tool\n", encoding="utf-8")
    client = FakeDiscoverClient(result=SearchResult(items=[
        _repo_item("blocked-tool", description="poc CVE-2020-1234"),
    ]))
    stats = discover(client, tmp_path)
    assert stats["blocked"] == 1
    assert stats["new_relations"] == 0


def test_discover_multi_day_catchup_queries_per_day(tmp_path: Path):
    """游标落后多天：逐日窗口查询。"""
    # 预置游标在 3 天前（相对今天动态构造）
    from datetime import datetime, timedelta, timezone

    three_days_ago = (datetime.now(timezone.utc) - timedelta(days=3)).strftime("%Y-%m-%d")
    state_mod.write_json(tmp_path / "state" / CURSOR_FILE, {"last_date": three_days_ago})

    client = FakeDiscoverClient(result=SearchResult(items=[]))
    discover(client, tmp_path)

    assert len(client.calls) == 4  # 3 天前..今天 共 4 个单日窗口
    assert all("created:" in q for q in client.calls)


def test_discover_dry_run_writes_nothing(tmp_path: Path):
    """评审 R12：dry-run 是真正的只读模式。"""
    _preset_cursor(tmp_path)
    client = FakeDiscoverClient(result=SearchResult(items=[
        _repo_item("tool-CVE-2019-0708", description="bluekeep CVE-2019-0708"),
    ]))
    stats = discover(client, tmp_path, dry_run=True)

    assert stats["cves_hit"] == 1      # 分析照常
    assert stats["new_relations"] == 0  # 但不写
    assert not (tmp_path / "state" / "relations_search").exists()
    assert not (tmp_path / "state" / "events.jsonl").exists()
    assert not (tmp_path / "state" / "scan_tasks.jsonl").exists()
    assert not (tmp_path / "state" / "repo_watch_cursor.jsonl").exists()


def test_discover_skips_rejected_cves(tmp_path: Path):
    """评审 R9：官方 REJECTED 的编号不被 discovery 重新激活。"""
    from collector import cvestate

    _preset_cursor(tmp_path)
    cvestate.set_state(tmp_path, "CVE-2019-0708", "REJECTED", source_tag="t")
    client = FakeDiscoverClient(result=SearchResult(items=[
        _repo_item("tool-CVE-2019-0708", description="bluekeep CVE-2019-0708"),
    ]))
    stats = discover(client, tmp_path)
    assert stats["new_relations"] == 0
    assert not (tmp_path / "state" / "relations_search").exists()


def test_f1_release_pagination_passes_page():
    """评审 F1：分页必须翻页，且到达检查点即停。"""
    from collector.cvesource import _list_releases_paginated

    class PagedClient:
        def __init__(self):
            self.calls = []

        def list_releases(self, per_page=30, page=1, budget=None):
            self.calls.append(page)
            # 第 1、2 页满 30，第 3 页 5 条；tag 递减
            count = 30 if page < 3 else 5
            return [{"tag_name": f"cve_r{page:02d}_{i:03d}"} for i in range(count)]

    client = PagedClient()
    releases, complete = _list_releases_paginated(client)
    assert client.calls == [1, 2, 3]           # 真翻页
    assert len(releases) == 65 and complete is True

    stop_client = PagedClient()
    releases, complete = _list_releases_paginated(stop_client, stop_tag="cve_r01_000")
    assert complete is True and "cve_r01_000" in {r["tag_name"] for r in releases}


def test_h2_invalid_cve_id_skipped_end_to_end(tmp_path: Path):
    """评审 H2：短编号仓库不入状态；渲染/契约验证不受影响（端到端）。"""
    from collector.render import render_all, verify_contract

    _preset_cursor(tmp_path)
    client = FakeDiscoverClient(result=SearchResult(items=[
        _repo_item("CVE-2026-1", description="bogus CVE-2026-1 tool"),
        _repo_item("CVE-0000-0000-template", description="placeholder CVE-0000-0000"),
        _repo_item("CVE-3026-1234-scanner", description="future CVE-3026-1234"),
        _repo_item("tool-CVE-2026-1234", description="poc for CVE-2026-1234"),
    ]))
    stats = discover(client, tmp_path)

    assert stats["invalid_ids"] == 3  # 短序号 + 不支持的年份（评审 I1）
    assert stats["new_relations"] == 1  # 合法编号正常收录
    records = state_mod.read_jsonl(tmp_path / "state" / "relations_search" / "2026.jsonl")
    assert all(r["cve_id"] != "CVE-2026-1" for r in records)

    # 单条异常数据不阻断发布：渲染 + 真实产物契约验证通过
    (tmp_path / "2026").mkdir(exist_ok=True)
    (tmp_path / "2026" / "README.md").write_text("", encoding="utf-8")
    render_all(tmp_path)
    assert verify_contract(tmp_path)["ok"]


def test_h4_overcap_day_advances_cursor_with_partial_queue(tmp_path: Path):
    """评审 H4：单日超上限不堵后续日期——记录部分覆盖、游标推进、有限重试。"""
    from datetime import datetime, timedelta, timezone

    three_days_ago = (datetime.now(timezone.utc) - timedelta(days=3)).strftime("%Y-%m-%d")
    state_mod.write_json(tmp_path / "state" / CURSOR_FILE, {"last_date": three_days_ago})

    capped = SearchResult(items=[], complete=False, stop_reason="pagination_cap",
                          errors=["pagination_cap_at_page_10 (total_count=1500)"])
    normal = SearchResult(items=[])

    class MixedClient:
        def __init__(self):
            self.calls = []

        def search_repositories(self, query, max_pages=10, budget=None, start_page=1):
            self.calls.append(query)
            return capped if three_days_ago in query else normal

    stats = discover(MixedClient(), tmp_path)
    assert stats["complete"] is True            # 主窗口完成（超量日为部分覆盖）
    assert stats["cursor_advanced"] is True     # 游标推进，不再卡死在超量日
    assert stats["partial_days_pending"] == 1
    cursor = state_mod.read_json(tmp_path / "state" / CURSOR_FILE)
    assert cursor["partial_days"] == [{"date": three_days_ago, "attempts": 1}]
    # 4 个单日窗口全部被查询（超量日 + 后续 3 天），未堵住
    assert stats["repos_seen"] == 0

    # 下轮：重试仍超量 → 次数增长；连续达到上限后放弃并继续
    stats2 = discover(MixedClient(), tmp_path)
    cursor2 = state_mod.read_json(tmp_path / "state" / CURSOR_FILE)
    assert cursor2["partial_days"][0]["attempts"] == 2
    stats3 = discover(MixedClient(), tmp_path)
    assert stats3["partial_days_dropped"] == 1
    assert state_mod.read_json(tmp_path / "state" / CURSOR_FILE)["partial_days"] == []


def test_i3_backfill_retry_never_starves_main_window(tmp_path: Path):
    """评审 I3：历史超量日补扫预算耗尽不阻塞主窗口，真实尝试计数。"""
    from datetime import datetime, timedelta, timezone

    now = datetime.now(timezone.utc)
    three_days_ago = (now - timedelta(days=3)).strftime("%Y-%m-%d")
    two_days_ago = (now - timedelta(days=2)).strftime("%Y-%m-%d")
    today = now.strftime("%Y-%m-%d")
    state_mod.write_json(tmp_path / "state" / CURSOR_FILE, {
        "last_date": two_days_ago,
        "partial_days": [{"date": three_days_ago, "attempts": 1}],
    })

    budget_out = SearchResult(items=[{"html_url": "u"}], complete=False,
                              stop_reason="budget", errors=["exhausted"], pages=5)
    ok = SearchResult(items=[])

    class Client:
        def __init__(self):
            self.calls = []

        def search_repositories(self, query, max_pages=10, budget=None, start_page=1):
            self.calls.append(query)
            return budget_out if three_days_ago in query else ok

    client = Client()
    stats = discover(client, tmp_path)

    assert stats["complete"] is True
    assert stats["cursor_advanced"] is True          # 主窗口未被补扫拖累
    assert any(f"created:{today}..{today}" in q for q in client.calls)
    cursor = state_mod.read_json(tmp_path / "state" / CURSOR_FILE)
    assert cursor["partial_days"] == [{"date": three_days_ago, "attempts": 2}]


def test_i3_overlap_day_queue_deduped(tmp_path):
    """评审 I3：重叠日超量只保留一个队列条目，重试计数统一。"""
    from datetime import datetime, timezone

    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    _preset_cursor(tmp_path)  # last_date = today，窗口与队列重叠
    capped = SearchResult(items=[], complete=False, stop_reason="pagination_cap",
                          errors=["cap"])

    stats = discover(FakeDiscoverClient(capped), tmp_path)
    cursor = state_mod.read_json(tmp_path / "state" / CURSOR_FILE)
    assert cursor["partial_days"] == [{"date": today, "attempts": 1}]

    discover(FakeDiscoverClient(capped), tmp_path)   # 第二轮同日再超量
    cursor2 = state_mod.read_json(tmp_path / "state" / CURSOR_FILE)
    assert cursor2["partial_days"] == [{"date": today, "attempts": 2}]  # 去重

    stats3 = discover(FakeDiscoverClient(capped), tmp_path)
    assert stats3["partial_days_dropped"] == 1        # 达上限放弃
    assert state_mod.read_json(tmp_path / "state" / CURSOR_FILE)["partial_days"] == []


@pytest.fixture
def timed_discovery(monkeypatch):
    """真实分页/预算客户端，模拟旧日超量、每次 HTTP 耗时一秒。"""
    from collector import repo_watch
    from collector.ghsearch import Budget, GitHubClient

    old_day = "2026-09-28"
    clock = [0.0]
    monkeypatch.setattr("collector.ghsearch.time.monotonic", lambda: clock[0])

    class Response:
        status_code = 200
        headers = {}
        url = "https://api.github.com/search/repositories"

        def __init__(self, day, page):
            self.day = day
            self.links = {"next": {"url": "next"}} if day == old_day and page < 10 else {}

        def json(self):
            items = ([_repo_item("CVE-2020-1234-old")] + [{}] * 99
                     if self.day == old_day else [_repo_item("CVE-2020-5678-new")])
            return {"items": items, "total_count": 1001 if self.day == old_day else 1,
                    "incomplete_results": False}

    class Session:
        def __init__(self):
            self.calls = []

        def get(self, url, params=None, **kwargs):
            day = params["q"].split("created:", 1)[1].split("..", 1)[0]
            self.calls.append((day, params["page"]))
            clock[0] += 1
            return Response(day, params["page"])

    def run(root, today, seconds, dry_run=False):
        monkeypatch.setattr(repo_watch, "_today", lambda: today)
        session = Session()
        client = GitHubClient(token="test-discovery-token", session=session, min_interval=0)
        stats = discover(client, root, dry_run=dry_run,
                         budget=Budget(max_seconds=seconds, started_at=clock[0]))
        return stats, session.calls

    return run


def test_j1_capped_overlap_never_blocks_next_day(tmp_path, timed_discovery):
    """当天超量自然入队；跨天零/少量预算和多轮补扫不阻塞新日期。"""
    old_day, today = "2026-09-28", "2026-09-29"
    cursor_path = tmp_path / "state" / CURSOR_FILE
    state_mod.write_json(cursor_path, {"last_date": old_day})
    first, calls = timed_discovery(tmp_path, old_day, 15)
    assert first["complete"] and len(calls) == 10
    initial = state_mod.read_json(cursor_path)
    assert initial["partial_days"] == [{"date": old_day, "attempts": 1}]

    stopped, calls = timed_discovery(tmp_path, today, 0)
    assert not stopped["complete"] and not calls
    assert state_mod.read_json(cursor_path) == initial

    # 只有一页预算也先收今天；未实际查询的旧日不计尝试。
    fresh, calls = timed_discovery(tmp_path, today, 1)
    assert calls == [(today, 1)]
    assert fresh["complete"] and fresh["cursor_advanced"]
    cursor = state_mod.read_json(cursor_path)
    assert cursor["last_date"] == today
    assert cursor["partial_days"] == [{"date": old_day, "attempts": 1}]
    rows = state_mod.read_jsonl(tmp_path / "state" / "relations_search" / "2020.jsonl")
    assert {r["cve_id"] for r in rows} == {"CVE-2020-1234", "CVE-2020-5678"}

    # 真实分页在旧日第 4 页后耗尽预算；两次尝试后按既定上限放弃。
    for attempt in (2, 3):
        stats, calls = timed_discovery(tmp_path, today, 5)
        assert calls == [(today, 1)] + [(old_day, page) for page in range(1, 5)]
        assert stats["complete"] and stats["cursor_advanced"]
        cursor = state_mod.read_json(cursor_path)
        expected = [{"date": old_day, "attempts": attempt}] if attempt < 3 else []
        assert cursor["partial_days"] == expected
        assert stats["partial_days_dropped"] == (1 if attempt == 3 else 0)

    final, calls = timed_discovery(tmp_path, today, 5)
    assert final["complete"] and calls == [(today, 1)]
    assert state_mod.read_json(cursor_path)["partial_days"] == []


def test_j1_dropped_overlap_does_not_restart_after_midnight(tmp_path, timed_discovery):
    """当天已达到放弃上限的超量日，跨天不能重新变成必扫前置项。"""
    old_day, today = "2026-09-28", "2026-09-29"
    cursor_path = tmp_path / "state" / CURSOR_FILE
    state_mod.write_json(cursor_path, {"last_date": old_day})
    for _ in range(3):
        stats, calls = timed_discovery(tmp_path, old_day, 15)
        assert stats["complete"] and len(calls) == 10
    assert stats["partial_days_dropped"] == 1
    assert state_mod.read_json(cursor_path)["partial_days"] == []

    fresh, calls = timed_discovery(tmp_path, today, 1)
    assert calls == [(today, 1)]
    assert fresh["complete"] and fresh["cursor_advanced"]
    assert state_mod.read_json(cursor_path)["last_date"] == today


def test_j1_deferred_overlap_dry_run_preserves_state(tmp_path, timed_discovery):
    """旧格式游标无新标志也能延后补扫；dry-run 不提交关系或重试进度。"""
    cursor_path = tmp_path / "state" / CURSOR_FILE
    state_mod.write_json(cursor_path, {
        "last_date": "2026-09-28",
        "partial_days": [{"date": "2026-09-28", "attempts": 1}],
    })
    before = {p.relative_to(tmp_path): p.read_bytes() for p in tmp_path.rglob("*") if p.is_file()}
    stats, calls = timed_discovery(tmp_path, "2026-09-29", 5, dry_run=True)
    assert calls[0] == ("2026-09-29", 1)
    assert stats["complete"] and not stats["cursor_advanced"]
    after = {p.relative_to(tmp_path): p.read_bytes() for p in tmp_path.rglob("*") if p.is_file()}
    assert after == before
