"""GitHub API 客户端（REFACTOR_PLAN.md 3.6 / 评审 4.5）。

同步 requests.Session + 预算队列，不依赖多 token 轮换：
- 搜索返回 items + complete + errors（而非裸列表），达预算/页数上限/
  incomplete_results 时 complete=False，调用方应保留任务而非丢弃；
- 401 标记凭证不可用（TokenInvalid）；403 先区分限流（x-ratelimit-
  remaining=0 → 等待 reset）与其他（退避）；429 按 Retry-After；
- 5xx/网络错误有限次带抖动退避（MAX_RETRIES）；
- 主动读限流头，超限等待（单次封顶 MAX_SINGLE_WAIT）；
- 日志与异常只出现凭证别名（末 4 位）。
"""
from __future__ import annotations

import os
import random
import time
from dataclasses import dataclass, field
from typing import Optional

import requests

__all__ = [
    "Budget",
    "BudgetExhausted",
    "TokenInvalid",
    "SearchResult",
    "GitHubClient",
]

API_BASE = "https://api.github.com"
MAX_RETRIES = 5
MAX_SINGLE_WAIT = 120.0  # 退避封顶（可多次进入）
MAX_ABSOLUTE_WAIT = 3600.0  # 单次限流等待绝对上限（评审 F8：不截短限流）
DEFAULT_MIN_INTERVAL = 0.25


class TokenInvalid(Exception):
    """凭证缺失、无效或过期。"""


class BudgetExhausted(Exception):
    """运行预算（请求数或时间）耗尽。"""


@dataclass
class Budget:
    max_requests: Optional[int] = None
    max_seconds: Optional[float] = None
    requests_used: int = 0
    started_at: float = field(default_factory=time.monotonic)

    def check(self) -> None:
        if self.max_requests is not None and self.requests_used >= self.max_requests:
            raise BudgetExhausted(f"request budget exhausted ({self.max_requests})")
        if self.max_seconds is not None and time.monotonic() - self.started_at >= self.max_seconds:
            raise BudgetExhausted(f"time budget exhausted ({self.max_seconds}s)")

    def spend(self) -> None:
        self.requests_used += 1

    def remaining_seconds(self) -> float | None:
        if self.max_seconds is None:
            return None
        return self.max_seconds - (time.monotonic() - self.started_at)


@dataclass
class SearchResult:
    items: list = field(default_factory=list)
    total_count: int = 0
    complete: bool = True
    errors: list = field(default_factory=list)
    pages: int = 0
    stop_reason: str = "complete"  # complete|budget|truncated|pagination_cap|incomplete_results


def _sleep(seconds: float) -> None:
    if seconds > 0:
        time.sleep(seconds)


class GitHubClient:
    def __init__(
        self,
        token: Optional[str] = None,
        session: Optional[requests.Session] = None,
        per_page: int = 100,
        min_interval: float = DEFAULT_MIN_INTERVAL,
    ):
        token = (token or "").strip() or os.environ.get("GH_TOKEN", "").strip()
        if not token:
            raise TokenInvalid("GH_TOKEN 未配置（export GH_TOKEN=... 或传 token 参数）")
        self._token = token
        self.token_alias = "****" + token[-4:]
        self.session = session if session is not None else requests.Session()
        self.per_page = per_page
        self._min_interval = min_interval
        self._last_request_at = 0.0
        self._reset_at: dict[str, float] = {}

    def _headers(self) -> dict:
        return {
            "Authorization": f"Bearer {self._token}",
            "Accept": "application/vnd.github+json",
            "User-Agent": "pocorexp-collector/0.1",
            "X-GitHub-Api-Version": "2022-11-28",
        }

    @staticmethod
    def _bucket(url: str) -> str:
        return "search" if "/search/" in url else "core"

    def _respect_rate(self, bucket: str, budget: Optional[Budget] = None) -> None:
        reset = self._reset_at.get(bucket)
        if not reset:
            return
        wait = reset - time.time()
        if wait <= 0:
            return
        # 等待不得截短以迁就限流（评审 F8）：有预算且等待超余量 → 耗尽退出；
        # 无预算则完整等待（仅保留 1 小时绝对上限防病态休眠）
        remaining = budget.remaining_seconds() if budget else None
        if remaining is not None and wait > remaining:
            raise BudgetExhausted(f"rate-limit wait {wait:.0f}s exceeds remaining budget {remaining:.0f}s")
        _sleep(min(wait, MAX_ABSOLUTE_WAIT))

    def _update_rate(self, resp) -> None:
        try:
            remaining = int(resp.headers.get("x-ratelimit-remaining", "1"))
            reset = int(resp.headers.get("x-ratelimit-reset", "0"))
        except (TypeError, ValueError):
            return
        if remaining == 0 and reset:
            bucket = resp.headers.get("x-ratelimit-resource", self._bucket(resp.url or ""))
            self._reset_at[bucket] = float(reset) + 1.0

    def _get(self, url: str, params: Optional[dict] = None, budget: Optional[Budget] = None):
        bucket = self._bucket(url)
        last_error = ""
        for attempt in range(MAX_RETRIES):
            if budget is not None:
                budget.check()
                budget.spend()  # 按实际请求尝试计数（评审 R11），失败重试同样消耗
            self._respect_rate(bucket, budget)
            pacing = self._min_interval - (time.monotonic() - self._last_request_at)
            if pacing > 0:
                _sleep(pacing)
            try:
                resp = self.session.get(url, params=params, headers=self._headers(), timeout=30)
            except requests.RequestException as exc:
                last_error = f"network error: {exc}"
                _sleep((2 ** attempt) + random.uniform(0, 0.5))
                continue
            self._last_request_at = time.monotonic()
            self._update_rate(resp)

            if resp.status_code == 200:
                return resp
            if resp.status_code == 404:
                return resp
            if resp.status_code == 401:
                raise TokenInvalid(f"凭证无效或已过期 ({self.token_alias})")
            if resp.status_code in (403, 429):
                retry_after = resp.headers.get("retry-after")
                if retry_after:
                    try:
                        wait = float(retry_after)
                        remaining = budget.remaining_seconds() if budget else None
                        if remaining is not None and wait > remaining:
                            raise BudgetExhausted(
                                f"retry-after {wait:.0f}s exceeds remaining budget {remaining:.0f}s"
                            )
                        _sleep(min(wait, MAX_ABSOLUTE_WAIT))
                    except (TypeError, ValueError):
                        pass
                    last_error = f"{resp.status_code} retry-after={retry_after}"
                    continue
                remaining = resp.headers.get("x-ratelimit-remaining")
                if remaining == "0":
                    last_error = f"{resp.status_code} rate limited"
                    continue  # _respect_rate 在下一轮等待 reset
                last_error = f"{resp.status_code}: {(resp.text or '')[:120]}"
                _sleep((2 ** attempt) + random.uniform(0, 0.5))
                continue
            if 500 <= resp.status_code < 600:
                last_error = f"{resp.status_code} server error"
                _sleep((2 ** attempt) + random.uniform(0, 0.5))
                continue
            resp.raise_for_status()
        raise RuntimeError(f"重试耗尽 ({url}): {last_error}")

    def search_repositories(
        self,
        query: str,
        max_pages: int = 3,
        budget: Optional[Budget] = None,
        start_page: int = 1,
    ) -> SearchResult:
        """start_page 支持截断续跑（评审 R6）：从上次已取得页之后继续。"""
        result = SearchResult()
        try:
            for page in range(start_page, start_page + max_pages):
                resp = self._get(
                    f"{API_BASE}/search/repositories",
                    params={"q": query, "per_page": self.per_page, "page": page, "sort": "stars"},
                    budget=budget,
                )
                data = resp.json()
                result.total_count = int(data.get("total_count", 0))
                result.pages = page
                items = data.get("items", [])
                result.items.extend(items)
                if data.get("incomplete_results"):
                    # 服务端声明当前页结果本身不完整：本页不可视为已完成
                    result.complete = False
                    result.stop_reason = "incomplete_results"
                    result.errors.append("incomplete_results=true")
                    break
                if len(items) < self.per_page or "next" not in (resp.links or {}):
                    # G5：自然结束也可能停在 API 覆盖上限——第 10 页无 next
                    # 而 total_count 显示仍有未覆盖结果时，不得判为完整
                    if page >= 10 and result.total_count > len(result.items):
                        result.complete = False
                        result.stop_reason = "pagination_cap"
                        result.errors.append(
                            f"pagination_cap_at_page_{page} "
                            f"(total_count={result.total_count}, fetched={len(result.items)})"
                        )
                    break  # 自然结束（末页）
                if page >= 10:
                    # GitHub 单查询上限 1000 条（10×100）：覆盖不全，显式标注
                    result.complete = False
                    result.stop_reason = "pagination_cap"
                    result.errors.append(f"pagination_cap_at_page_{page}")
                    break
                if page == start_page + max_pages - 1:
                    # 本轮页数预算用尽且仍有下一页：截断（断点续跑）
                    result.complete = False
                    result.stop_reason = "truncated"
                    result.errors.append(
                        f"truncated at page {page} (total_count={result.total_count})"
                    )
        except BudgetExhausted as exc:
            result.complete = False
            result.stop_reason = "budget"
            result.errors.append(str(exc))
        return result

    def get_repo(self, owner: str, repo: str, budget: Optional[Budget] = None) -> Optional[dict]:
        resp = self._get(f"{API_BASE}/repos/{owner}/{repo}", budget=budget)
        if resp.status_code == 404:
            return None
        return resp.json()

    def list_releases(
        self,
        repo: str = "CVEProject/cvelistV5",
        per_page: int = 30,
        page: int = 1,
        budget: Optional[Budget] = None,
    ) -> list:
        resp = self._get(f"{API_BASE}/repos/{repo}/releases",
                         params={"per_page": per_page, "page": page}, budget=budget)
        return resp.json()

    def download_asset(self, url: str, budget: Optional[Budget] = None) -> bytes:
        resp = self._get(url, budget=budget)
        if resp.status_code != 200:
            raise RuntimeError(f"资产下载失败 HTTP {resp.status_code}: {url}")
        return resp.content
