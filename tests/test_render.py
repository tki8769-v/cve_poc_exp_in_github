"""渲染、发布契约与 clean --apply 测试。"""
from __future__ import annotations

from pathlib import Path

from collector import state as state_mod
from collector.clean import clean_apply
from collector.render import load_active_relations, render_all, verify_contract


def _shard(root: Path, name: str, records: list[dict]) -> None:
    state_mod.write_jsonl(state_mod.state_dir(root) / name, records)


def _legacy(cve_id, url, **extra):
    owner, repo = url.rstrip("/").split("/")[-2:]
    return {"cve_id": cve_id, "url": url, "owner": owner, "repo": repo,
            "source": "legacy_markdown", "verification": "pending", **extra}


def _search(cve_id, url, stars=1):
    owner, repo = url.rstrip("/").split("/")[-2:]
    return {"cve_id": cve_id, "url": url, "owner": owner, "repo": repo,
            "source": "github_search", "verification": "accepted",
            "first_seen_at": "2026-09-23T00:00:00Z", "stars": stars, "forks": 0}


EXISTING_README = """## CVE-2026-0100
> 老描述保留

- [https://github.com/a/old](https://github.com/a/old) : ![starts](https://img.shields.io/github/stars/a/old.svg) ![forks](https://img.shields.io/github/forks/a/old.svg)

## CVE-2026-0002
> 另一个老 CVE

- [https://github.com/b/keep](https://github.com/b/keep) : ![starts](x)
"""


def _setup(tmp_path: Path) -> Path:
    root = tmp_path
    (root / "2026").mkdir()
    (root / "2026" / "README.md").write_text(EXISTING_README, encoding="utf-8")
    _shard(root, "relations/2026.jsonl", [
        _legacy("CVE-2026-0100", "https://github.com/a/old"),
        _legacy("CVE-2026-0002", "https://github.com/b/keep"),
        _legacy("CVE-2026-0002", "https://github.com/b/gone-wrong"),  # 将被 reject
    ])
    _shard(root, "relations_search/2026.jsonl", [
        _search("CVE-2026-0100", "https://github.com/a/new-poc", stars=7),
    ])
    return root


def test_render_preserves_existing_and_appends_new(tmp_path: Path):
    root = _setup(tmp_path)
    render_all(root)

    text = (root / "2026" / "README.md").read_text(encoding="utf-8")
    # 序号降序：0100 在前
    assert text.index("## CVE-2026-0100") < text.index("## CVE-2026-0002")
    # 老描述原样保留
    assert "> 老描述保留" in text
    # 既有链接顺序保留，新链接追加
    section = text.split("## CVE-2026-0100")[1].split("## ")[0]
    assert section.index("a/old") < section.index("a/new-poc")
    # 聚合页含年份标题
    aggregate = (root / "PocOrExp.md").read_text(encoding="utf-8")
    assert aggregate.startswith("## 2026\n")
    # Today.md 未接管且当日无事件 → 不写出
    assert not (root / "Today.md").exists()


def test_render_idempotent(tmp_path: Path):
    root = _setup(tmp_path)
    first = render_all(root)
    second = render_all(root)
    assert first["changed"] and second["changed"] == []


def test_today_md_from_first_seen(tmp_path: Path):
    """F11：Today 从关系 first_seen 权威派生，与事件日志解耦。"""
    root = _setup(tmp_path)
    today = state_mod.now_iso()[:10]
    # 把一条关系的 first_seen 置为今天（模拟今日新发现）
    shard = state_mod.state_dir(root) / "relations_search" / "2026.jsonl"
    records = state_mod.read_jsonl(shard)
    records[0]["first_seen_at"] = f"{today}T10:00:00Z"
    state_mod.write_jsonl(shard, records)
    render_all(root)
    text = (root / "Today.md").read_text(encoding="utf-8")
    assert text.startswith(f"# Update {today}")
    assert text.count("- [https://github.com/a/new-poc](") == 1

    # 该关系被 rejected 后：不再计入 Today（有效关系视图过滤）
    records = state_mod.read_jsonl(shard)
    records[0]["verification"] = "rejected"
    state_mod.write_jsonl(shard, records)
    render_all(root)
    assert "new-poc" not in (root / "Today.md").read_text(encoding="utf-8")


def test_verify_contract_ok(tmp_path: Path):
    root = _setup(tmp_path)
    render_all(root)  # R8：verify 校验真实发布产物，需先渲染
    report = verify_contract(root)
    assert report["ok"], report["problems"]
    # vendored 兼容解析器使独立 CI 也能执行下游契约复核
    assert report["downstream_checked"] is True


def test_verify_detects_corrupted_real_artifacts(tmp_path: Path):
    """R8 回归：真实产物被篡改必须报错。"""
    root = _setup(tmp_path)
    render_all(root)
    readme = root / "2026" / "README.md"
    readme.write_text(
        "## CVE-2026-9999\n- [u](https://github.com/x/y)\n", encoding="utf-8"
    )
    report = verify_contract(root)
    assert not report["ok"]


def test_verify_detects_stale_empty_year(tmp_path: Path):
    """R8 回归：全部关系失活的年份不得残留旧 README。"""
    root = _setup(tmp_path)
    render_all(root)
    # 将 2026 全部关系置为 rejected → render 清理 README → verify 通过；
    # 反之若不清理则报错
    relations_path = state_mod.state_dir(root) / "relations" / "2026.jsonl"
    records = state_mod.read_jsonl(relations_path)
    for record in records:
        record["verification"] = "rejected"
    state_mod.write_jsonl(relations_path, records)
    state_mod.write_jsonl(state_mod.state_dir(root) / "relations_search" / "2026.jsonl", [])
    render_all(root)
    assert not (root / "2026" / "README.md").exists()
    assert verify_contract(root)["ok"]


def test_clean_apply_tombstones_and_renders_exclusion(tmp_path: Path):
    root = _setup(tmp_path)
    recheck_dir = state_mod.state_dir(root) / "recheck"
    state_mod.write_json(recheck_dir / "report.json",
                         {"missing_meta": 3, "conflicts_total": 1})
    # 充分排除证据：描述明确自述为 URL 所指编号
    state_mod.write_jsonl(recheck_dir / "conflict_evidenced.jsonl", [
        {"cve_id": "CVE-2026-0002", "url": "https://github.com/b/gone-wrong",
         "reason": "foreign_id_conflict_evidenced", "evidence_description": "tool for other CVE"},
    ])

    report = clean_apply(root)
    assert report["applied_rejected"] == 1
    assert report["affected_years"] == ["2026"]
    assert report["still_pending_meta"] == 3

    relations = state_mod.read_jsonl(state_mod.state_dir(root) / "relations" / "2026.jsonl")
    by_url = {r["url"]: r for r in relations}
    assert by_url["https://github.com/b/gone-wrong"]["verification"] == "rejected"
    assert by_url["https://github.com/b/gone-wrong"]["auto"] is True

    render_all(root)
    text = (root / "2026" / "README.md").read_text(encoding="utf-8")
    assert "b/gone-wrong" not in text
    assert "b/keep" in text
    assert verify_contract(root)["ok"]


def test_clean_apply_revives_stale_tombstones_on_new_evidence(tmp_path: Path):
    """R5：空描述误拒的墓碑，在新描述证据到位后被重新裁决回 needs_review。"""
    root = _setup(tmp_path)
    relations_path = state_mod.state_dir(root) / "relations" / "2026.jsonl"
    records = state_mod.read_jsonl(relations_path)
    for record in records:
        if record["url"].endswith("gone-wrong"):
            record.update({"verification": "rejected", "auto": True,
                           "rejected_reason": "evidenced_foreign_id",
                           "rejected_evidence": "", "rejected_at": "2026-01-01T00:00:00Z"})
    state_mod.write_jsonl(relations_path, records)

    # 回补的新描述明确提及目标编号
    state_mod.write_jsonl(state_mod.state_dir(root) / "repo_meta.jsonl", [{
        "owner": "b", "repo": "gone-wrong", "fetched_at": state_mod.now_iso(),
        "description": "poc and checker for CVE-2026-0002",
    }])
    recheck_dir = state_mod.state_dir(root) / "recheck"
    state_mod.write_json(recheck_dir / "report.json", {"missing_meta": 0, "conflicts_total": 0})

    report = clean_apply(root)
    assert report["revoked_rejected"] == 1
    records = state_mod.read_jsonl(relations_path)
    by_url = {r["url"]: r for r in records}
    revived = by_url["https://github.com/b/gone-wrong"]
    assert revived["verification"] == "needs_review"
    assert revived["revoked_reason"] in (
        "desc_contains_target_only",       # URL 无编号、描述确认目标
        "desc_mention_with_url_conflict",  # URL 他指、描述提及目标
    )
    # 恢复后重新渲染出现
    render_all(root)
    assert "gone-wrong" in (root / "2026" / "README.md").read_text(encoding="utf-8")


def test_clean_apply_revokes_desc_based_accepted(tmp_path: Path):
    """R4 止损：采集期按描述接受的记录重审为 needs_review。"""
    root = _setup(tmp_path)
    relations_path = state_mod.state_dir(root) / "relations" / "2026.jsonl"
    records = state_mod.read_jsonl(relations_path)
    for record in records:
        if record["url"].endswith("a/old"):
            record.update({"verification": "accepted",
                           "accepted_reason": "desc_contains_target_only",
                           "accepted_evidence": "regression of CVE-2026-0100"})
    state_mod.write_jsonl(relations_path, records)
    state_mod.write_jsonl(state_mod.state_dir(root) / "repo_meta.jsonl", [{
        "owner": "a", "repo": "old", "fetched_at": state_mod.now_iso(),
        "description": "regression of CVE-2026-0100",
    }])
    recheck_dir = state_mod.state_dir(root) / "recheck"
    state_mod.write_json(recheck_dir / "report.json", {"missing_meta": 0, "conflicts_total": 0})

    report = clean_apply(root)
    assert report["revoked_accepted"] == 1
    records = state_mod.read_jsonl(relations_path)
    by_url = {r["url"]: r for r in records}
    assert by_url["https://github.com/a/old"]["verification"] == "needs_review"


def test_clean_apply_requires_recheck(tmp_path: Path):
    root = tmp_path
    root.mkdir(exist_ok=True)
    try:
        clean_apply(root)
        raise AssertionError("应当 SystemExit")
    except SystemExit as exc:
        assert "recheck" in str(exc.code) or "recheck" in str(exc)
    # 编排内（strict=False）宽容跳过
    assert clean_apply(root, strict=False) == {"skipped": "no-recheck-report"}


def test_active_relations_merge_prefers_search_metadata(tmp_path: Path):
    root = _setup(tmp_path)
    merged = load_active_relations(root)
    record = merged["CVE-2026-0100"]["https://github.com/a/new-poc"]
    assert record["source"] == "github_search" and record["stars"] == 7
    legacy = merged["CVE-2026-0100"]["https://github.com/a/old"]
    assert legacy["source"] == "legacy_markdown"


def test_bootstrap_refuses_overwrite_without_force(tmp_path: Path):
    """评审 R13：已引导过的 state 默认拒绝重建，防止丢墓碑。"""
    from collector.bootstrap import bootstrap

    root = _setup(tmp_path)
    try:
        bootstrap(root)
        raise AssertionError("应当 SystemExit")
    except SystemExit as exc:
        assert "force" in str(exc.code) or "force" in str(exc)


def test_f5_rejected_cve_excluded_from_active_view(tmp_path: Path):
    """评审 F5：官方撤回的 CVE 不再进入有效关系视图与渲染。"""
    from collector import cvestate

    root = _setup(tmp_path)
    render_all(root)
    assert "a/old" in (root / "2026" / "README.md").read_text(encoding="utf-8")
    cvestate.set_state(root, "CVE-2026-0100", "REJECTED", source_tag="t")
    render_all(root)
    text = (root / "2026" / "README.md").read_text(encoding="utf-8")
    assert "a/old" not in text and "CVE-2026-0100" not in text
    assert verify_contract(root)["ok"]


def test_f7_missing_required_artifacts_fail_verify(tmp_path: Path):
    """评审 F7：PocOrExp.md / 已接管 Today 被删除必须报错。"""
    root = _setup(tmp_path)
    render_all(root)
    (root / "PocOrExp.md").unlink()
    report = verify_contract(root)
    assert not report["ok"] and any("PocOrExp" in p for p in report["problems"])


def test_f9_manual_rejection_not_revoked_automatically(tmp_path: Path):
    """评审 F9：auto=False 的人工拒绝不被自动重审撤销。"""
    root = _setup(tmp_path)
    relations_path = state_mod.state_dir(root) / "relations" / "2026.jsonl"
    records = state_mod.read_jsonl(relations_path)
    for record in records:
        if record["url"].endswith("gone-wrong"):
            record.update({"verification": "rejected", "auto": False,
                           "rejected_reason": "manual"})
    state_mod.write_jsonl(relations_path, records)
    # 回补的证据明确支持目标（若可自动撤销则会回退）
    state_mod.write_jsonl(state_mod.state_dir(root) / "repo_meta.jsonl", [{
        "owner": "b", "repo": "gone-wrong", "fetched_at": state_mod.now_iso(),
        "description": "poc for CVE-2026-0002",
    }])
    recheck_dir = state_mod.state_dir(root) / "recheck"
    state_mod.write_json(recheck_dir / "report.json", {"missing_meta": 0})
    report = clean_apply(root)
    assert report["revoked_rejected"] == 0
    by_url = {r["url"]: r for r in state_mod.read_jsonl(relations_path)}
    assert by_url["https://github.com/b/gone-wrong"]["verification"] == "rejected"


def test_f10_refresh_queue_includes_tombstones(tmp_path: Path):
    """评审 F10：自动墓碑与 needs_review 进入优先刷新队列。"""
    from collector.backfill import _conflict_repos

    root = _setup(tmp_path)
    relations_path = state_mod.state_dir(root) / "relations" / "2026.jsonl"
    records = state_mod.read_jsonl(relations_path)
    for record in records:
        if record["url"].endswith("gone-wrong"):
            record.update({"verification": "rejected", "auto": True})
        elif record["url"].endswith("a/old"):
            record.update({"verification": "needs_review"})
    state_mod.write_jsonl(relations_path, records)
    keys = _conflict_repos(root)
    assert ("b", "gone-wrong") in keys
    assert ("a", "old") in keys


def test_missing_today_fails_verify_structured(tmp_path: Path):
    """评审 3 次要项：已接管 Today 被删除 → 结构化报错，不抛异常。"""
    root = _setup(tmp_path)
    today = state_mod.now_iso()[:10]
    shard = state_mod.state_dir(root) / "relations_search" / "2026.jsonl"
    records = state_mod.read_jsonl(shard)
    records[0]["first_seen_at"] = f"{today}T10:00:00Z"
    state_mod.write_jsonl(shard, records)
    render_all(root)
    assert (root / "Today.md").exists()

    (root / "Today.md").unlink()
    report = verify_contract(root)  # 不得抛 FileNotFoundError
    assert not report["ok"]
    assert any("Today.md" in p for p in report["problems"])
