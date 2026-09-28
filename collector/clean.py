"""历史清洗（REFACTOR_PLAN.md 3.5）。保守规则（评审 R4/R5）。

- dry-run：URL 级冲突候选分析（口径与审计一致），不修改任何数据；
- --apply：仅"充分排除证据"（conflict_evidenced）自动 rejected（墓碑，
  auto=true，可被新证据重新裁决）；描述提及/空描述/沉默一律 needs_review；
- 墓碑恢复（R5）：对既有 rejected 关系用当前元数据重审——证据不再充分
  时回退 needs_review（revoked_rejected），新描述到位即可翻案；
- 采集期 desc 接受的历史记录（desc_contains_target_only 证据）重审为
  needs_review（revoked_accepted），URL 证据的 accepted 不动。
"""
from __future__ import annotations

from pathlib import Path

from . import RULES_VERSION
from . import state as state_mod
from .attrib import ACCEPTED, CONFLICT_CANDIDATE, classify_relation
from .backfill import load_meta
from .parse import extract_cve_ids, is_valid_cve_id

__all__ = ["clean_dry_run", "clean_apply"]


def clean_dry_run(root: Path) -> dict:
    """URL 级冲突候选清单（不修改任何数据）。

    口径与审计一致：URL 含编号但集合不含目标 → 冲突候选（前缀/其他）；
    URL 无编号 → 证据不足待元数据；URL 含目标 → 保留。
    """
    rows = [r for r in _load_relations(root) if r.get("verification") != "rejected"]
    conflicts: list[dict] = []
    stats = {"total": len(rows), "keep": 0, "conflict_candidate": 0, "insufficient_evidence": 0}
    reasons: dict[str, int] = {}

    for row in rows:
        cve_id = row["cve_id"]
        ids = extract_cve_ids(row["url"])
        if cve_id in ids:
            stats["keep"] += 1
            continue
        if not ids:
            stats["insufficient_evidence"] += 1
            continue
        stats["conflict_candidate"] += 1
        reason = "prefix_conflict" if any(v.startswith(cve_id) for v in ids) else "foreign_id_conflict"
        reasons[reason] = reasons.get(reason, 0) + 1
        conflicts.append({
            "cve_id": cve_id, "url": row["url"], "reason": reason,
            "url_ids": sorted(ids), "rule_version": RULES_VERSION,
        })

    conflicts.sort(key=lambda r: (r["cve_id"], r["url"]))
    out_dir = state_mod.state_dir(root) / "clean_dryrun"
    state_mod.write_jsonl(out_dir / "conflicts.jsonl", conflicts)

    summary = [
        "# Clean dry-run（不修改任何数据）",
        "",
        f"- rule_version: {RULES_VERSION}",
        f"- 关系总数: {stats['total']}",
        f"- keep（URL 含目标，含多 CVE 仓库）: {stats['keep']}",
        f"- conflict_candidate（URL 含编号但不含目标，待反证复核）: {stats['conflict_candidate']}",
        f"  - prefix_conflict: {reasons.get('prefix_conflict', 0)}",
        f"  - foreign_id_conflict: {reasons.get('foreign_id_conflict', 0)}",
        f"- insufficient_evidence（URL 无编号，待元数据回补）: {stats['insufficient_evidence']}",
        "",
        "## 处置规则（保守）",
        "",
        "- 仅当仓库描述非空、不含目标编号、且明确自述为 URL 所指编号时，",
        "  clean --apply 才自动 rejected；",
        "- 描述提及目标（regression 类上下文）、空描述、沉默描述 → needs_review；",
        "- rejected 墓碑可被新证据重新裁决（auto 标记，revocable）。",
    ]
    state_mod.atomic_write_text(out_dir / "summary.md", "\n".join(summary) + "\n")

    return {
        "rule_version": RULES_VERSION,
        "mode": "dry-run",
        "stats": stats,
        "reasons": reasons,
        "conflicts_written": len(conflicts),
    }


def _load_relations(root: Path) -> list[dict]:
    """legacy 与 search 两来源的全部关系（评审 F6：新增来源同样需复审）。"""
    rows: list[dict] = []
    for directory in ("relations", "relations_search"):
        for path in sorted((state_mod.state_dir(root) / directory).glob("*.jsonl")):
            rows.extend(state_mod.read_jsonl(path))
    if not rows:
        raise SystemExit("state/relations 为空：请先运行 python -m collector bootstrap")
    return rows


def clean_apply(root: Path, strict: bool = True) -> dict:
    """应用复核结论 + 重审既有自动处置（评审 R4/R5）。"""
    recheck_dir = state_mod.state_dir(root) / "recheck"
    if not (recheck_dir / "report.json").exists():
        if strict:
            raise SystemExit("缺少 state/recheck/report.json：先运行 backfill --priority-conflicts 与 recheck")
        return {"skipped": "no-recheck-report"}

    evidenced = {(c["cve_id"], c["url"]): c for c in
                 state_mod.read_jsonl(recheck_dir / "conflict_evidenced.jsonl")}
    meta = load_meta(root)
    now = state_mod.now_iso()

    applied_rejected = 0
    revoked_rejected = 0
    revoked_accepted = 0
    affected_years: set[str] = set()

    for directory in ("relations", "relations_search"):
        relations_dir = state_mod.state_dir(root) / directory
        for shard in sorted(relations_dir.glob("*.jsonl")):
            records = state_mod.read_jsonl(shard)
            changed = False
            for record in records:
                key = (record["cve_id"], record["url"])
                verification = record.get("verification")

                if verification != "rejected" and key in evidenced and record.get("auto", True):
                    evidence = evidenced[key]
                    record.update({
                        "verification": "rejected",
                        "auto": True,
                        "rejected_reason": "evidenced_foreign_id",
                        # F13：持久化裁决证据与元数据快照时间，可追溯可复核
                        "rejected_evidence": (evidence.get("evidence_description") or "")[:500],
                        "rejected_evidence_fetched_at": evidence.get("evidence_fetched_at", ""),
                        "rejected_at": now,
                        "rule_version": RULES_VERSION,
                    })
                    applied_rejected += 1
                    affected_years.add(record["cve_id"].split("-")[1])
                    changed = True
                    continue

                if verification == "rejected":
                    if not is_valid_cve_id(record.get("cve_id", "")):
                        continue  # I4：格式隔离墓碑不参与证据翻案
                    # 墓碑重审（R5/F9）：仅自动决定可被自动撤销；证据不再
                    # 充分 → 回退 needs_review
                    verdict = _verdict_with_meta(root, record, meta)
                    if (verdict is not None and verdict.state != CONFLICT_CANDIDATE
                            and record.get("auto", True)):
                        record.update({
                            "verification": "needs_review",
                            "revoked_from": "rejected",
                            "revoked_at": now,
                            "revoked_reason": verdict.reason,
                            "rule_version": RULES_VERSION,
                        })
                        revoked_rejected += 1
                        affected_years.add(record["cve_id"].split("-")[1])
                        changed = True
                    elif (not record.get("rejected_evidence") and record.get("auto", True)
                          and key in evidenced):
                        # F13 修复：既有墓碑缺失证据 → 从复核结论回补
                        record["rejected_evidence"] = (evidenced[key].get("evidence_description") or "")[:500]
                        changed = True
                    continue

                if verification == "accepted" and not _url_evidence(record) and (
                        record.get("accepted_reason") == "desc_contains_target_only"
                        or not record.get("accepted_reason")):
                    # 采集期 desc 接受重审（R4/F6/H5）：URL 不含目标的记录才需
                    # 重审（URL 证据是结构性的，不会随时间失效）；当前证据仍
                    # 支持接受 → 刷新原因与证据，不降级；元数据缺失时凭 URL
                    # 与空描述保守判定
                    info = meta.get((record.get("owner"), record.get("repo")))
                    description = (info or {}).get("description") or ""
                    verdict = classify_relation(record["cve_id"], record["url"],
                                                repo_description=description)
                    if verdict.state == ACCEPTED:
                        record["accepted_reason"] = verdict.reason
                        record["accepted_url_ids"] = sorted(verdict.url_ids)
                        record["accepted_evidence_ids"] = sorted(verdict.evidence_ids)
                        record["accepted_at"] = now
                        changed = True
                        continue
                    reason = verdict.reason if verdict else "multi_id_mention_unresolved"
                    record.update({
                        "verification": "needs_review",
                        "revoked_from": "accepted",
                        "revoked_at": now,
                        "revoked_reason": reason,
                        "rule_version": RULES_VERSION,
                    })
                    revoked_accepted += 1
                    affected_years.add(record["cve_id"].split("-")[1])
                    changed = True

            if changed:
                state_mod.write_jsonl(shard, records)

    pending = state_mod.read_json(recheck_dir / "report.json", default={}) or {}
    report = {
        "rule_version": RULES_VERSION,
        "applied_at": now,
        "applied_rejected": applied_rejected,
        "revoked_rejected": revoked_rejected,
        "revoked_accepted": revoked_accepted,
        "affected_years": sorted(affected_years),
        "still_pending_meta": int(pending.get("missing_meta", 0)),
    }
    state_mod.write_json(state_mod.state_dir(root) / "clean_apply" / "report.json", report)
    return report


def _verdict_with_meta(root: Path, record: dict, meta: dict):
    """用当前元数据对一条关系重审；元数据缺失返回 None（维持原状）。"""
    owner, repo = record.get("owner"), record.get("repo")
    if not (owner and repo):
        return None
    info = meta.get((owner, repo))
    if info is None or info.get("error"):
        return None
    return classify_relation(record["cve_id"], record["url"],
                             repo_description=info.get("description"))


def _url_evidence(record: dict) -> bool:
    """URL 编号集合包含目标 → 结构性接受证据，不随元数据变化失效（H5）。"""
    return record["cve_id"] in extract_cve_ids(record["url"])
