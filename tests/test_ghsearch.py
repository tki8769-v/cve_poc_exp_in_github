"""ghsearch 客户端测试（mock session，无网络）。"""
from __future__ import annotations

import pytest
import requests

from collector import ghsearch
from collector.ghsearch import Budget, BudgetExhausted, GitHubClient, TokenInvalid

TOKEN = "ghp_test_token_1234"


class FakeResponse:
    def __init__(self, status_code=200, json_data=None, headers=None, links=None, text="", url=""):
        self.status_code = status_code
        self._json = json_data or {}
        self.headers = headers or {}
        self.links = links or {}
        self.text = text
        self.url = url

    def json(self):
        return self._json

    def raise_for_status(self):
        if self.status_code >= 400:
            raise requests.HTTPError(f"HTTP {self.status_code}")


class FakeSession:
    """按调用顺序返回预设响应；记录请求供断言。"""

    def __init__(self, responses):
        self.responses = list(responses)
        self.calls = []

    def get(self, url, params=None, headers=None, timeout=None):
        self.calls.append({"url": url, "params": params, "headers": headers})
        if self.responses:
            item = self.responses.pop(0)
            response = item if isinstance(item, FakeResponse) else item(params)
        else:
            response = FakeResponse(status_code=200, json_data={"items": []})
        if not response.url:
            response.url = url
        return response


@pytest.fixture(autouse=True)
def _no_sleep(monkeypatch):
    monkeypatch.setattr(ghsearch.time, "sleep", lambda *_a, **_k: None)


def _client(session):
    return GitHubClient(token=TOKEN, session=session, min_interval=0)


def test_token_required(monkeypatch):
    monkeypatch.delenv("GH_TOKEN", raising=False)
    with pytest.raises(TokenInvalid):
        GitHubClient(session=FakeSession([]))


def test_token_alias_not_leaked():
    client = GitHubClient(token=TOKEN, session=FakeSession([]), min_interval=0)
    assert TOKEN not in client.token_alias
    assert client.token_alias.endswith("1234")


def _search_response(items, total_count=None, incomplete=False, links=None):
    return FakeResponse(
        json_data={
            "total_count": total_count if total_count is not None else len(items),
            "incomplete_results": incomplete,
            "items": items,
        },
        links=links or {},
    )


def test_search_single_page_complete():
    session = FakeSession([_search_response([{"html_url": "https://github.com/a/b"}])])
    result = _client(session).search_repositories('"CVE-2020-1234"')
    assert result.complete and len(result.items) == 1 and result.pages == 1


def test_search_pagination_follows_link_header():
    big = [{"html_url": f"https://github.com/a/b{i}"} for i in range(100)]
    small = [{"html_url": "https://github.com/a/tail"}]
    session = FakeSession(
        [
            _search_response(big, total_count=101, links={"next": {"url": "x"}}),
            _search_response(small, total_count=101),
        ]
    )
    result = _client(session).search_repositories('"CVE-2019-0708"')
    assert len(result.items) == 101 and result.pages == 2 and result.complete


def test_search_truncation_marks_incomplete():
    big = [{"html_url": "u"} for _ in range(100)]
    session = FakeSession(
        [
            _search_response(big, total_count=500, links={"next": {"url": "x"}}),
            _search_response(big, total_count=500, links={"next": {"url": "x"}}),
            _search_response(big, total_count=500, links={"next": {"url": "x"}}),
        ]
    )
    result = _client(session).search_repositories("q", max_pages=3)
    assert not result.complete
    assert any("truncated" in e for e in result.errors)


def test_search_incomplete_results_flag():
    session = FakeSession([_search_response([{"html_url": "u"}], incomplete=True)])
    result = _client(session).search_repositories("q")
    assert not result.complete and any("incomplete_results" in e for e in result.errors)


def test_401_raises_token_invalid():
    session = FakeSession([FakeResponse(status_code=401, text="Bad credentials")])
    with pytest.raises(TokenInvalid):
        _client(session).search_repositories("q")


def test_429_then_success_retries():
    session = FakeSession(
        [
            FakeResponse(status_code=429, headers={"retry-after": "1"}),
            _search_response([{"html_url": "u"}]),
        ]
    )
    result = _client(session).search_repositories("q")
    assert result.complete and len(result.items) == 1
    assert len(session.calls) == 2


def test_rate_limited_403_waits_for_reset():
    session = FakeSession(
        [
            FakeResponse(
                status_code=403,
                headers={
                    "x-ratelimit-remaining": "0",
                    "x-ratelimit-reset": str(int(ghsearch.time.time()) + 5),
                    "x-ratelimit-resource": "search",
                },
            ),
            _search_response([{"html_url": "u"}]),
        ]
    )
    result = _client(session).search_repositories("q")
    assert result.complete
    assert len(session.calls) == 2


def test_budget_exhaustion_returns_partial():
    big = [{"html_url": "u"} for _ in range(100)]

    def page_two(_):
        raise AssertionError("不应发起第二页请求")

    session = FakeSession(
        [
            _search_response(big, total_count=500, links={"next": {"url": "x"}}),
        ]
    )
    budget = Budget(max_requests=1)
    result = _client(session).search_repositories("q", max_pages=3, budget=budget)
    assert not result.complete and budget.requests_used == 1
    assert result.stop_reason == "budget"


def test_get_repo_404_returns_none():
    session = FakeSession([FakeResponse(status_code=404)])
    assert _client(session).get_repo("owner", "gone") is None


def test_get_repo_ok():
    session = FakeSession([FakeResponse(json_data={"id": 1, "description": "poc"})])
    info = _client(session).get_repo("owner", "repo")
    assert info["id"] == 1


def test_f14_download_name_validation_accepts_cache_examples():
    """评审 F14：缓存中的边界仓库名不再被误拒。"""
    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
    from download import _validate_url

    assert _validate_url("https://github.com/jamaal001/CVE-2014-91371-Wordpress-")
    assert _validate_url("https://github.com/0x00-0x00/-CVE-2017-9805")
    assert _validate_url(
        "https://github.com/santokum/CVE-2020-25478--ASUS-RT-AC87U-TFTP-is-"
        "vulnerable-to-Denial-of-Service-DoS-attack")
    assert not _validate_url("https://github.com/a/..")
    assert not _validate_url("https://github.com/a/../b")
    assert not _validate_url("https://github.com/../x")


def test_g5_pagination_cap_without_next_link():
    """评审 G5：第 10 页无 next 而 total_count 更大 → 覆盖不全，不判完整。"""
    big = [{"html_url": f"u{i}"} for i in range(100)]
    pages = [_search_response(big, total_count=1200, links={"next": {"url": "x"}})
             for _ in range(9)]
    pages.append(_search_response(big, total_count=1200))  # 第 10 页：无 next
    session = FakeSession(pages)
    result = _client(session).search_repositories("q", max_pages=10)
    assert not result.complete
    assert result.stop_reason == "pagination_cap"
    assert any("pagination_cap" in e for e in result.errors)
    assert len(result.items) == 1000
