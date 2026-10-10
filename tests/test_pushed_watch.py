"""阶段 2B：pushed 增量通道（独立游标、时间拆分、未解缺口、不饿死新日期）。"""
from __future__ import annotations

from datetime import datetime, timedelta, timezone
from pathlib import Path

from collector import state as state_mod
from collector.ghsearch import SearchResult
from collector.pushed_watch import CURSOR_FILE, discover_pushed


def _item(name="tool-CVE-2020-1234", url=None, desc="poc CVE-2020-1234"):
    return {"html_url": url or f"https://github.com/o/{name}", "name": name,
            "description": desc, "topics": [], "stargazers_count": 1, "forks_count": 0}


class FakeClient:
    def __init__(self, behavior):
        self.behavior = behavior
        self.calls = []

    def search_repositories(self, query, max_pages=3, budget=None, start_page=1):
        self.calls.append(query)
        return self.behavior(query)


def _window_span(query: str) -> timedelta:
    rng = query.split("pushed:")[1]
    start, end = rng.split("..")
    fmt = "%Y-%m-%dT%H:%M:%SZ"
    return datetime.strptime(end, fmt) - datetime.strptime(start, fmt)


def test_p2b_independent_cursor_and_merge(tmp_path: Path):
    """独立游标（created 游标不被触碰）；结果走统一归属合并。"""
    client = FakeClient(lambda q: SearchResult(items=[_item()]) if "pushed:" in q
                        else SearchResult())
    stats = discover_pushed(client, tmp_path)

    assert stats["cursor_advanced"] is True
    assert stats["new_relations"] == 1
    assert not (tmp_path / "state" / "repo_watch_cursor.json").exists()
    cursor = state_mod.read_json(tmp_path / "state" / CURSOR_FILE)
    assert cursor["last_date"]
    relation = state_mod.read_jsonl(tmp_path / "state" / "relations_search" / "2020.jsonl")[0]
    assert relation["source"] == "github_pushed"

    calls_before = len(client.calls)
    stats2 = discover_pushed(client, tmp_path)
    assert stats2["new_relations"] == 0                    # 幂等
    assert len(client.calls) == calls_before + 1           # 只重查当日窗口


def test_p2b_cap_splits_by_time(tmp_path: Path):
    """日窗口超量 → 时间拆分入队（不照搬放弃策略）；游标不越过未覆盖日。"""
    def behavior(query):
        if _window_span(query) >= timedelta(hours=12):
            return SearchResult(items=[], complete=False, stop_reason="pagination_cap",
                                errors=["cap"])
        return SearchResult(items=[])

    stats = discover_pushed(FakeClient(behavior), tmp_path)

    assert stats["splits"] >= 1                 # 拆分而非放弃
    assert stats["windows_pending"] >= 2
    assert stats["cursor_advanced"] is False    # 子窗口未完成，last_date 不推进
    cursor = state_mod.read_json(tmp_path / "state" / CURSOR_FILE)
    assert len(cursor["windows"]) == stats["windows_pending"]
    assert cursor["unresolved"] == []           # 尚未到最小粒度，无未解缺口


def test_p2b_min_window_cap_becomes_unresolved(tmp_path: Path):
    """最小粒度（1h）仍超量 → unresolved 缺口记录，不静默标记完成。"""
    hour_from_now = datetime.now(timezone.utc).replace(minute=0, second=0, microsecond=0)
    start = (hour_from_now - timedelta(hours=2)).strftime("%Y-%m-%dT%H:%M:%SZ")
    end = (hour_from_now - timedelta(hours=1)).strftime("%Y-%m-%dT%H:%M:%SZ")
    state_mod.write_json(tmp_path / "state" / CURSOR_FILE, {
        "last_date": None,
        "windows": [{"start": start, "end": end, "attempts": 1}],
        "unresolved": [],
    })

    def behavior(query):
        return SearchResult(items=[], complete=False, stop_reason="pagination_cap",
                            errors=["cap"])

    stats = discover_pushed(FakeClient(behavior), tmp_path)

    assert stats["unresolved_added"] == 1
    cursor = state_mod.read_json(tmp_path / "state" / CURSOR_FILE)
    assert cursor["unresolved"][0]["start"] == start


def test_p2b_incomplete_keeps_window_queued(tmp_path: Path):
    """预算/网络不完整：子窗口放回队首且计数，last_date 不推进。"""
    hour_from_now = datetime.now(timezone.utc).replace(minute=0, second=0, microsecond=0)
    start = (hour_from_now - timedelta(hours=3)).strftime("%Y-%m-%dT%H:%M:%SZ")
    end = (hour_from_now - timedelta(hours=2)).strftime("%Y-%m-%dT%H:%M:%SZ")
    state_mod.write_json(tmp_path / "state" / CURSOR_FILE, {
        "last_date": None,
        "windows": [{"start": start, "end": end, "attempts": 1}],
        "unresolved": [],
    })

    def behavior(query):
        if _window_span(query) <= timedelta(hours=1):
            return SearchResult(items=[], complete=False, stop_reason="budget",
                                errors=["budget"])
        return SearchResult(items=[])

    stats = discover_pushed(FakeClient(behavior), tmp_path)

    assert stats["stop_reason"]
    cursor = state_mod.read_json(tmp_path / "state" / CURSOR_FILE)
    assert cursor["windows"] and cursor["windows"][0]["attempts"] == 2


def test_p2b_long_downtime_records_unresolved_and_restarts(tmp_path: Path):
    """落后超过追赶上限：老区间记为 unresolved 摘要，从近期重启。"""
    old = (datetime.now(timezone.utc) - timedelta(days=40)).strftime("%Y-%m-%d")
    state_mod.write_json(tmp_path / "state" / CURSOR_FILE, {
        "last_date": old, "windows": [], "unresolved": []})

    stats = discover_pushed(FakeClient(lambda q: SearchResult()), tmp_path)

    assert stats["unresolved_added"] == 1
    cursor = state_mod.read_json(tmp_path / "state" / CURSOR_FILE)
    assert cursor["unresolved"][0]["from"] == old
    assert stats["cursor_advanced"] is True  # 近期窗口正常推进
