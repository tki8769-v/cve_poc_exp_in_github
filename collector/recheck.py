"""冲突候选反证复核（REFACTOR_PLAN.md 3.4/3.5）。纯本地，零 API。

按保守规则分桶（评审 R4/R5）：
  conflict_evidenced   描述提供充分排除证据 → clean --apply 可自动 rejected
  needs_review         描述提及目标（regression 类）、描述为空、描述沉默、
                       仓库消失 → 一律待复核，不自动处置
  missing_meta         元数据未回补
"""
from __future__ import annotations

from pathlib import Path

from . import RULES_VERSION
from . import state as state_mod
from .attrib import CONFLICT_CANDIDATE, NEEDS_REVIEW, classify_relation
from .backfill import load_meta
from .parse import parse_github_repo

__all__ = ["recheck"]


def recheck(root: Path) -> dict:
    conflicts_path = state_mod.state_dir(root) / "clean_dryrun" / "conflicts.jsonl"
    conflicts = state_mod.read_jsonl(conflicts_path)
    meta = load_meta(root)

    conflict_evidenced: list[dict] = []
    needs_review: list[dict] = []
    gone: list[dict] = []
    missing_meta: list[dict] = []

    for conflict in conflicts:
        cve_id = conflict["cve_id"]
        url = conflict["url"]
        owner, repo = parse_github_repo(url)
        record = {"cve_id": cve_id, "url": url, "rule_version": RULES_VERSION}
        if not owner or not repo:
            record["reason"] = "not_a_repo_url"
            missing_meta.append(record)
            continue
        info = meta.get((owner, repo))
        if info is None:
            record["reason"] = "meta_not_fetched"
            missing_meta.append(record)
            continue
        if info.get("error"):
            record["reason"] = f"repo_{info['error']}"
            gone.append(record)
            continue
        verdict = classify_relation(cve_id, url, repo_description=info.get("description") or "")
        record["evidence_description"] = info.get("description") or ""
        record["evidence_fetched_at"] = info.get("fetched_at", "")
        record["reason"] = verdict.reason
        if verdict.state == CONFLICT_CANDIDATE:
            conflict_evidenced.append(record)
        else:  # needs_review / insufficient 等均待复核
            needs_review.append(record)

    out_dir = state_mod.state_dir(root) / "recheck"
    state_mod.write_jsonl(out_dir / "conflict_evidenced.jsonl", conflict_evidenced)
    state_mod.write_jsonl(out_dir / "needs_review.jsonl", needs_review)
    state_mod.write_jsonl(out_dir / "gone.jsonl", gone)
    state_mod.write_jsonl(out_dir / "missing_meta.jsonl", missing_meta)

    report = {
        "rule_version": RULES_VERSION,
        "conflicts_total": len(conflicts),
        "conflict_evidenced": len(conflict_evidenced),
        "needs_review": len(needs_review),
        "gone": len(gone),
        "missing_meta": len(missing_meta),
    }
    state_mod.write_json(out_dir / "report.json", report)
    return report
