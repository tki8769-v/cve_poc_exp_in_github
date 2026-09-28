"""审计扫描（固定口径），产品化自 REFACTOR_REVIEW.md 第 8 节。

口径定义（与评审一致，规则版本 collector.RULES_VERSION）：
  contains_other_id    URL 至少含一个非当前 CVE（=1,408 基线）
  also_contains_target 上述关联中 URL 同时含当前 CVE（=401，多 CVE 仓库，应保留）
  target_absent        URL 含 CVE 但集合不含当前 CVE（=1,007，冲突候选）
  prefix               target_absent 中存在数字前缀冲突（=627）
  other_conflict       target_absent 中其他编号冲突（=380）
  no_cve_in_url        URL 未匹配到任何 CVE（=6,100）
  target_present       URL 集合包含当前 CVE（=20,875）
"""
from __future__ import annotations

from collections import Counter
from pathlib import Path

from . import RULES_VERSION
from .parse import extract_cve_ids, iter_readme_relations

__all__ = ["year_readme_files", "run_audit", "format_report", "BASELINE_2026_09_23"]

# 2026-09-23 快照基线，供漂移对比（数据合法变化时允许不一致，但必须显式呈现）。
BASELINE_2026_09_23 = {
    "counts": {
        "links": 27982,
        "target_present": 20875,
        "contains_other_id": 1408,
        "also_contains_target": 401,
        "target_absent": 1007,
        "prefix": 627,
        "other_conflict": 380,
        "no_cve_in_url": 6100,
    },
    "populated_cves": 12153,
    "contains_other_id_cves": 907,
    "target_absent_cves": 629,
}


def year_readme_files(root: Path) -> list[Path]:
    return sorted(root.glob("[12][0-9][0-9][0-9]/README.md"))


def run_audit(root: Path) -> dict:
    counts: Counter = Counter()
    foreign_cves: set[str] = set()
    conflict_cves: set[str] = set()
    populated_cves: set[str] = set()

    for path in year_readme_files(root):
        for rel in iter_readme_relations(path):
            populated_cves.add(rel.cve_id)
            counts["links"] += 1
            ids = extract_cve_ids(rel.url)
            if ids - {rel.cve_id}:
                counts["contains_other_id"] += 1
                foreign_cves.add(rel.cve_id)
                if rel.cve_id in ids:
                    counts["also_contains_target"] += 1
            if not ids:
                counts["no_cve_in_url"] += 1
            elif rel.cve_id not in ids:
                counts["target_absent"] += 1
                conflict_cves.add(rel.cve_id)
                if any(value.startswith(rel.cve_id) for value in ids):
                    counts["prefix"] += 1
                else:
                    counts["other_conflict"] += 1
            else:
                counts["target_present"] += 1

    return {
        "rule_version": RULES_VERSION,
        "counts": dict(counts),
        "populated_cves": len(populated_cves),
        "contains_other_id_cves": len(foreign_cves),
        "target_absent_cves": len(conflict_cves),
    }


_ORDER = [
    "links",
    "target_present",
    "contains_other_id",
    "also_contains_target",
    "target_absent",
    "prefix",
    "other_conflict",
    "no_cve_in_url",
]


def format_report(result: dict) -> str:
    lines = [
        f"Audit (rule_version={result['rule_version']})",
        "-" * 46,
    ]
    baseline_counts = BASELINE_2026_09_23["counts"]
    for key in _ORDER:
        value = result["counts"].get(key, 0)
        expected = baseline_counts.get(key)
        drift = "" if expected == value else f"  (baseline {expected}, DRIFT)"
        lines.append(f"{key:24}{value:>8}{drift}")
    for key in ("populated_cves", "contains_other_id_cves", "target_absent_cves"):
        expected = BASELINE_2026_09_23[key]
        drift = "" if expected == result[key] else f"  (baseline {expected}, DRIFT)"
        lines.append(f"{key:24}{result[key]:>8}{drift}")
    return "\n".join(lines)
