"""daily 编排端到端测试（FakeClient，无网络）。"""
from __future__ import annotations

import io
import json
import zipfile
from pathlib import Path

from collector import state as state_mod
from collector.ghsearch import SearchResult
from collector.pipeline import daily


class FakeDailyClient:
    """覆盖 daily 全流程所需接口：releases/资产下载/搜索/仓库元数据。"""

    def __init__(self):
        record = {
            "cveMetadata": {"cveId": "CVE-2026-0500", "state": "PUBLISHED"},
            "containers": {"cna": {"descriptions": [
                {"lang": "en", "value": "test vulnerability CVE-2026-0500"}]}},
        }
        buffer = io.BytesIO()
        with zipfile.ZipFile(buffer, "w") as zf:
            zf.writestr("2026/0xxx/CVE-2026-0500.json", json.dumps(record))
        self.delta = buffer.getvalue()
        self.search_calls = 0
        self.repo_calls = 0

    def list_releases(self, per_page=30, page=1, budget=None):
        return [{
            "tag_name": "cve_2026-09-24_1100Z",
            "assets": [{"id": 99, "name": "2026-09-24_1100Z_delta_CVEs_at_1100Z.zip",
                        "browser_download_url": "https://example/99.zip"}],
        }]

    def download_asset(self, url, budget=None):
        return self.delta

    def search_repositories(self, query, max_pages=3, budget=None, start_page=1):
        self.search_calls += 1
        if query.startswith("CVE in:name,description"):
            # 仓库侧 created 窗口查询不返回既有仓库（模拟真实行为）
            return SearchResult()
        return SearchResult(items=[{
            "html_url": "https://github.com/x/CVE-2026-0500-poc",
            "description": "poc for CVE-2026-0500",
            "stargazers_count": 9,
            "forks_count": 1,
        }])

    def get_repo(self, owner, repo, budget=None):
        self.repo_calls += 1
        return {"id": 1, "description": "poc for CVE-2026-0500",
                "stargazers_count": 9, "forks_count": 1,
                "updated_at": "2026-09-24T00:00:00Z", "pushed_at": "2026-09-24T00:00:00Z",
                "archived": False, "default_branch": "main"}


def _setup(tmp_path: Path) -> Path:
    root = tmp_path
    (root / "2026").mkdir()
    (root / "2026" / "README.md").write_text("", encoding="utf-8")
    # 已有一条 legacy 关系，保持渲染有基础内容
    state_mod.write_jsonl(state_mod.state_dir(root) / "relations" / "2026.jsonl", [{
        "cve_id": "CVE-2026-0100", "url": "https://github.com/a/old",
        "owner": "a", "repo": "old", "source": "legacy_markdown",
        "verification": "pending",
    }])
    return root


def test_daily_end_to_end(tmp_path: Path):
    root = _setup(tmp_path)
    client = FakeDailyClient()

    summary = daily(root, client=client,
                    scan_requests=10, scan_minutes=1.0,
                    backfill_limit=10, backfill_minutes=0.5)

    assert summary["ok"] is True
    steps = summary["steps"]

    # sync：delta 中的 CVE 入队
    assert steps["sync"]["new_tasks"] == 1
    # scan：搜索命中并经三态过滤合并
    assert steps["scan"]["scanned"] == 1
    assert steps["scan"]["new_relations"] == 1
    # backfill：全量队列（meta_backfill_queue 缺省为空），不报错即可
    assert "fetched" in steps["backfill_queue"]
    # recheck 无冲突候选 → 全 0 报告；clean_apply 正常返回零应用
    assert steps["recheck"]["conflicts_total"] == 0
    assert steps["clean_apply"]["applied_rejected"] == 0
    assert steps["clean_apply"]["revoked_rejected"] == 0
    # render 写出年份 README，含新增关系
    readme = (root / "2026" / "README.md").read_text(encoding="utf-8")
    assert "CVE-2026-0500" in readme and "a/old" in readme
    # Today.md 由 new_poc 事件生成
    today = (root / "Today.md").read_text(encoding="utf-8")
    assert "CVE-2026-0500" in today
    # verify 通过 + last_run 落盘
    assert steps["verify"]["ok"] is True
    last_run = state_mod.read_json(state_mod.state_dir(root) / "last_run.json")
    assert last_run["ok"] is True
    # 仓库侧窗口查询 3 次（首跑回看 3 天）+ CVE 定向搜索 1 次
    assert client.search_calls == 4


def test_daily_idempotent_rerun(tmp_path: Path):
    root = _setup(tmp_path)
    client = FakeDailyClient()
    daily(root, client=client, scan_requests=10, scan_minutes=1.0,
          backfill_limit=10, backfill_minutes=0.5)
    events_before = len(state_mod.read_jsonl(state_mod.state_dir(root) / "events.jsonl"))

    summary = daily(root, client=client, scan_requests=10, scan_minutes=1.0,
                    backfill_limit=10, backfill_minutes=0.5)

    # 第二轮：sync 游标命中无新任务；scan 到期任务为 0（重扫在 7 天后）；
    # 关系与事件不重复
    assert summary["steps"]["sync"]["new_tasks"] == 0
    assert summary["steps"]["scan"]["scanned"] == 0
    relations = state_mod.read_jsonl(state_mod.state_dir(root) / "relations_search" / "2026.jsonl")
    assert len(relations) == 1
    events_after = len(state_mod.read_jsonl(state_mod.state_dir(root) / "events.jsonl"))
    assert events_after == events_before
    assert summary["ok"] is True


def test_daily_survives_sync_budget_exhaustion(tmp_path: Path):
    """评审 H3：sync 预算耗尽是受控停止——整轮照常渲染/验证/发布。"""
    from collector.ghsearch import BudgetExhausted

    root = _setup(tmp_path)

    class SyncBudgetOutClient(FakeDailyClient):
        def list_releases(self, per_page=30, page=1, budget=None):
            raise BudgetExhausted("time budget exhausted")

    summary = daily(root, client=SyncBudgetOutClient(),
                    scan_requests=10, scan_minutes=1.0,
                    backfill_limit=10, backfill_minutes=0.5)

    assert summary["ok"] is True                       # 不再弃整轮
    assert summary["steps"]["sync"]["budget_stopped"] is True
    assert summary["steps"]["verify"]["ok"] is True
    # 队列观测字段（评审 4 容量项）——sync 受控停止，本轮无新任务属正常
    assert "queue" in summary["steps"]
    assert "due_by_priority" in summary["steps"]["queue"]
    assert summary["steps"]["queue"]["tasks_total"] == 0
