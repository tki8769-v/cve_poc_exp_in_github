"""阶段 2A：官方 CNA/ADP 引用通道（refs）。

核心契约（实施方案 §1.1）：引用是发现线索不是判定结论——判定只用仓库
自身元数据，杜绝循环证明；候选先持久化，游标不越过未保存结果。
"""
from __future__ import annotations

import io
import json
import zipfile
from pathlib import Path

from collector import state as state_mod
from collector.refs import (
    extract_references,
    process_official_refs,
    record_candidates,
    ref_kind,
)


def test_ref_kind_grading():
    """证据分级：Exploit 标签 > commit/PR/Patch > Advisory > 普通引用。"""
    assert ref_kind("https://github.com/a/poc", ["Exploit"]) == "poc"
    assert ref_kind("https://github.com/a/fix/commit/abc", []) == "patch"
    assert ref_kind("https://github.com/a/fix", ["Patch"]) == "patch"
    assert ref_kind("https://github.com/a/x", ["Vendor Advisory"]) == "advisory"
    assert ref_kind("https://github.com/a/tool", []) == "reference"


def test_extract_references_cna_adp_and_non_github():
    data = {
        "cveMetadata": {"cveId": "CVE-2026-0101", "state": "PUBLISHED"},
        "containers": {
            "cna": {"references": [
                {"url": "https://github.com/a/poc-CVE-2026-0101", "tags": ["Exploit"]},
                {"url": "https://example.com/advisory", "tags": []},
            ]},
            "adp": [{"references": [
                {"url": "https://github.com/b/deep-CVE-2026-0101/blob/main/x.py",
                 "tags": []},
            ]}],
        },
    }
    extracted = extract_references(data)
    assert len(extracted) == 2  # 非 GitHub 链接不进入本通道
    by_url = {r["url"]: r for r in extracted}
    assert by_url["https://github.com/a/poc-CVE-2026-0101"]["kind"] == "poc"
    assert by_url["https://github.com/a/poc-CVE-2026-0101"]["container"] == "cna"
    deep = by_url["https://github.com/b/deep-CVE-2026-0101/blob/main/x.py"]
    assert deep["container"] == "adp"
    assert deep["repo_owner"] == "b" and deep["repo_name"] == "deep-CVE-2026-0101"


def test_record_candidates_dedup_and_persistence(tmp_path: Path):
    ref = {"url": "https://github.com/a/poc", "repo_owner": "a", "repo_name": "poc",
           "kind": "poc", "tags": ["Exploit"], "container": "cna"}
    assert record_candidates(tmp_path, "CVE-2026-0102", [ref], "t1") == 1
    assert record_candidates(tmp_path, "CVE-2026-0102", [ref], "t2") == 0  # 去重
    rows = state_mod.read_jsonl(tmp_path / "state" / "candidates" / "official_refs.jsonl")
    assert len(rows) == 1 and rows[0]["source_tag"] == "t1" and rows[0]["status"] == "pending"


class FakeRepoClient:
    def __init__(self, repos: dict):
        self.repos = repos
        self.calls = []

    def get_repo(self, owner, repo, budget=None):
        self.calls.append((owner, repo))
        info = self.repos.get((owner, repo), {"id": 9, "description": "",
                                              "topics": [], "stargazers_count": 0,
                                              "forks_count": 0})
        return info


def test_p2a_anti_circular_no_repo_evidence_no_accept(tmp_path: Path):
    """反循环证明：官方引用只触发查看；仓库元数据不含目标编号 → 不接受。"""
    record_candidates(tmp_path, "CVE-2026-0103", [
        {"url": "https://github.com/a/some-tool", "repo_owner": "a",
         "repo_name": "some-tool", "kind": "reference", "tags": [], "container": "cna"},
    ], "t1")
    client = FakeRepoClient({("a", "some-tool"): {
        "id": 1, "description": "a generic tool", "topics": [],
        "stargazers_count": 5, "forks_count": 0}})

    stats = process_official_refs(client, tmp_path)

    assert stats["accepted"] == 0
    assert stats["kept_for_review"] == 1
    assert not (tmp_path / "state" / "relations_search").exists() or \
        state_mod.read_jsonl(tmp_path / "state" / "relations_search" / "2026.jsonl") == []


def test_p2a_accepted_with_evidence_and_idempotent(tmp_path: Path):
    record_candidates(tmp_path, "CVE-2026-0104", [
        {"url": "https://github.com/a/CVE-2026-0104-poc", "repo_owner": "a",
         "repo_name": "CVE-2026-0104-poc", "kind": "poc", "tags": ["Exploit"],
         "container": "cna"},
    ], "cve_2026-10-09_0800Z")
    client = FakeRepoClient({("a", "CVE-2026-0104-poc"): {
        "id": 2, "description": "poc for CVE-2026-0104", "topics": [],
        "stargazers_count": 5, "forks_count": 0}})

    stats = process_official_refs(client, tmp_path)

    assert stats["accepted"] == 1
    record = state_mod.read_jsonl(tmp_path / "state" / "relations_search" / "2026.jsonl")[0]
    assert record["source"] == "official_reference"
    assert record["official_reference"]["kind"] == "poc"
    assert record["official_reference"]["source_tag"] == "cve_2026-10-09_0800Z"
    assert record["accepted_reason"] == "url_contains_target"

    stats2 = process_official_refs(client, tmp_path)  # 候选已处理，不重复
    assert stats2["processed"] == 0 and stats2["accepted"] == 0


def test_p2a_patch_refs_deferred_no_meta_fetch(tmp_path: Path):
    """patch/公告类不做元数据级自动确认（需内容取证，后续阶段）。"""
    record_candidates(tmp_path, "CVE-2026-0105", [
        {"url": "https://github.com/a/fix/commit/abc", "repo_owner": "a",
         "repo_name": "fix", "kind": "patch", "tags": ["Patch"], "container": "cna"},
    ], "t1")
    client = FakeRepoClient({})

    stats = process_official_refs(client, tmp_path)

    assert stats["patchlike_skipped"] == 1
    assert client.calls == []  # 未消耗取证请求
    rows = state_mod.read_jsonl(tmp_path / "state" / "candidates" / "official_refs.jsonl")
    assert rows[0]["status"] == "deferred_content_verification"


def test_p2a_sync_persists_candidates_before_cursor(tmp_path: Path):
    """sync 资产内先存候选（游标不越过未保存结果）。"""
    from collector import cvesource

    data = {
        "cveMetadata": {"cveId": "CVE-2026-0600", "state": "PUBLISHED"},
        "containers": {"cna": {
            "descriptions": [{"lang": "en", "value": "d"}],
            "references": [{"url": "https://github.com/z/poc-CVE-2026-0600",
                            "tags": ["Exploit"]}],
        }},
    }
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w") as zf:
        zf.writestr("2026/0xxx/CVE-2026-0600.json", json.dumps(data))
    release = {"tag_name": "t1", "assets": [
        {"id": 1, "name": "t1_delta.zip", "browser_download_url": "https://x/1.zip"}]}

    class Client:
        def list_releases(self, per_page=30, page=1, budget=None):
            return [release]

        def download_asset(self, url, budget=None):
            return buffer.getvalue()

    report = cvesource.sync(Client(), tmp_path)

    assert report["ref_candidates_added"] == 1
    rows = state_mod.read_jsonl(tmp_path / "state" / "candidates" / "official_refs.jsonl")
    assert rows[0]["cve_id"] == "CVE-2026-0600"
    assert rows[0]["source_tag"] == "t1"
