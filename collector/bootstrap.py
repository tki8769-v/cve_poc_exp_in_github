"""历史数据引导（REFACTOR_PLAN.md 3.3 / 评审 R3/R13）。

仓库不含任何 CVE-*.json（实测 0 个），Markdown 只能恢复 CVE—URL
关系，不能恢复仓库元数据（不编造数值）。按评审修订：
- R3：引导的历史 CVE 全部纳入调度（错峰散布在未来 7 天，避免任务风暴），
  历史关系不再游离于周期对账之外；
- R13：state/relations 已存在时默认拒绝重建（防止丢失墓碑与判定），
  --force 才允许覆盖（覆盖前自动快照到 state/bootstrap_backup/）。
"""
from __future__ import annotations

import random
from datetime import datetime, timedelta, timezone
from pathlib import Path

from . import RULES_VERSION
from . import scheduler
from . import state as state_mod
from .parse import parse_github_repo, parse_readme_file

__all__ = ["bootstrap"]

FOUND_RESCAN_DAYS = 7


def bootstrap(root: Path, force: bool = False) -> dict:
    relations_dir = state_mod.state_dir(root) / "relations"
    existing = list(relations_dir.glob("*.jsonl"))
    if existing and not force:
        raise SystemExit(
            "state/relations 已存在（引导过）。重复 bootstrap 会丢失清洗墓碑与判定；"
            "确需重建请使用 --force（将自动快照到 state/bootstrap_backup/）"
        )

    raw_total = 0
    relations: list[dict] = []
    repos: dict[tuple[str, str], None] = {}

    for readme in sorted(root.glob("[12][0-9][0-9][0-9]/README.md")):
        for rel in parse_readme_file(readme):
            raw_total += 1
            owner, repo = parse_github_repo(rel.url)
            relations.append(
                {
                    "cve_id": rel.cve_id,
                    "url": rel.url,
                    "owner": owner,
                    "repo": repo,
                    "source": "legacy_markdown",
                    "verification": "pending",
                    "rule_version": RULES_VERSION,
                }
            )
            if owner and repo:
                repos.setdefault((owner, repo))

    if existing and force:
        backup = state_mod.state_dir(root) / "bootstrap_backup"
        backup.mkdir(parents=True, exist_ok=True)
        for shard in existing:
            shard.rename(backup / shard.name)

    relations.sort(key=lambda r: (r["cve_id"], r["url"]))

    sdir = state_mod.state_dir(root)
    by_year: dict[str, list[dict]] = {}
    for record in relations:
        year = record["cve_id"].split("-")[1]
        by_year.setdefault(year, []).append(record)
    for year, rows in sorted(by_year.items()):
        state_mod.write_jsonl(sdir / "relations" / f"{year}.jsonl", rows)

    backfill = [
        {
            "owner": owner,
            "repo": repo,
            "missing_metadata": [
                "repo_id", "description", "stars", "forks", "updated_at", "pushed_at",
            ],
        }
        for owner, repo in sorted(repos)
    ]
    state_mod.write_json(sdir / "meta_backfill_queue.json", backfill)

    # R3：历史 CVE 全量纳入调度，due 均匀散布未来 7 天（错峰）
    now = datetime.now(timezone.utc)
    items = []
    for cve_id in sorted({r["cve_id"] for r in relations}):
        due = now + timedelta(seconds=random.uniform(0, FOUND_RESCAN_DAYS * 86400))
        items.append({
            "cve_id": cve_id,
            "reason": "rescan",
            "priority": scheduler.PRIORITY_FOUND,
            "due_at": due.strftime("%Y-%m-%dT%H:%M:%SZ"),
        })
    scheduled = scheduler.enqueue_many(root, items)

    report = {
        "rule_version": RULES_VERSION,
        "relations_raw": raw_total,
        "relations_total": len(relations),
        "relations_with_github_repo": sum(1 for r in relations if r["owner"] and r["repo"]),
        "unique_repos": len(repos),
        "years": sorted(by_year),
        "shard_sizes": {year: len(rows) for year, rows in sorted(by_year.items())},
        "cves_scheduled": scheduled,
    }
    state_mod.write_json(sdir / "bootstrap_report.json", report)
    return report
