"""仓库侧增量发现（repo_watch）与黑名单测试。"""
from __future__ import annotations

from pathlib import Path

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
