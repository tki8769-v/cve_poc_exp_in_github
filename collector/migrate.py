"""存量部署迁移（评审 F2/F4/F5/F9 + G1/G4）。幂等，可重复执行。

- F4：关系库中的 CVE 与任务表做差集，批量补齐并错峰调度（保留既有判定）；
- F2：旧 schema 游标迁移（floor 继承 last_tag；窗口自愈在 sync 内进行）；
- F5：历史 cve_rejected 事件补写权威状态（缺状态的 CVE）；
- F9：缺少 auto 标记的历史拒绝记录补 auto=True（历史上仅存在自动流程）；
- G1：状态记录补 source_kind（legacy_event 是待对账线索，任何正式
  release 版本可覆盖，不再以字符串比较压制 cve_* tag）；
- G4：reason=new/modified 的既有任务优先级压回最高（时效性）；
- H2：active 关系中的非法编号（序号不足 4 位）确定性隔离为墓碑、
  任务移除——单条外部异常数据不得阻断发布。
"""
from __future__ import annotations

import random
from datetime import datetime, timedelta, timezone
from pathlib import Path

from . import RULES_VERSION
from . import cvestate
from . import scheduler
from . import state as state_mod
from .parse import is_valid_cve_id

__all__ = ["migrate"]

STAGGER_DAYS = 7


def migrate(root: Path) -> dict:
    report: dict = {}
    sdir = state_mod.state_dir(root)

    # 1. 游标 schema 迁移（F2）
    cursor_path = sdir / "cve_cursor.json"
    cursor = state_mod.read_json(cursor_path, default=None)
    if cursor and not cursor.get("floor_tag") and cursor.get("last_tag"):
        cursor["floor_tag"] = cursor["last_tag"]
        state_mod.write_json(cursor_path, cursor)
        report["cursor_floor_migrated"] = True

    # 2. 任务差集补齐（F4）
    relation_cves: set[str] = set()
    for directory in ("relations", "relations_search"):
        for shard in (sdir / directory).glob("*.jsonl"):
            relation_cves.update(r["cve_id"] for r in state_mod.read_jsonl(shard))
    task_cves = {t["cve_id"] for t in scheduler.load_tasks(root)}
    rejected_states = {c for c, r in cvestate.load_states(root).items()
                       if r.get("state") == "REJECTED"}
    missing = sorted(relation_cves - task_cves - rejected_states)
    if missing:
        now = datetime.now(timezone.utc)
        items = []
        for cve_id in missing:
            due = now + timedelta(seconds=random.uniform(0, STAGGER_DAYS * 86400))
            items.append({
                "cve_id": cve_id,
                "reason": "rescan",
                "priority": scheduler.PRIORITY_FOUND,
                "due_at": due.strftime("%Y-%m-%dT%H:%M:%SZ"),
            })
        created = scheduler.enqueue_many(root, items)
        report["tasks_created"] = created
    else:
        report["tasks_created"] = 0
    report["tasks_missing_before"] = len(missing)

    # 3. 历史拒绝事件补权威状态（F5）
    events = [e for e in state_mod.read_jsonl(sdir / "events.jsonl")
              if e.get("type") == "cve_rejected"]
    states = cvestate.load_states(root)
    backfilled = 0
    for event in events:
        cve_id = event.get("cve_id")
        if cve_id and cve_id not in states:
            cvestate.set_state(root, cve_id, "REJECTED", source_tag="legacy_event",
                               source_kind=cvestate.KIND_LEGACY)
            backfilled += 1
    report["cve_states_backfilled"] = backfilled

    # 3b. 状态记录 source_kind 规范化（G1，幂等）：旧记录缺字段时按
    #     source_tag 推断补齐——legacy_event 此后可被任何正式版本覆盖
    states_rows = state_mod.read_jsonl(sdir / cvestate.STATES_FILE)
    kind_patched = 0
    for row in states_rows:
        if not row.get("source_kind"):
            row["source_kind"] = cvestate.record_kind(row)
            kind_patched += 1
    if kind_patched:
        state_mod.write_jsonl(sdir / cvestate.STATES_FILE, states_rows)
    report["state_kind_patched"] = kind_patched

    # 4. auto 标记补齐（F9）
    patched = 0
    for shard in sorted((sdir / "relations").glob("*.jsonl")):
        records = state_mod.read_jsonl(shard)
        changed = False
        for record in records:
            if record.get("verification") == "rejected" and "auto" not in record:
                record["auto"] = True  # 历史拒绝均出自自动流程
                changed = True
                patched += 1
        if changed:
            state_mod.write_jsonl(shard, records)
    report["auto_flags_patched"] = patched

    # 5. 新 CVE 任务优先级规范化（G4，幂等）
    report["priorities_normalized"] = scheduler.normalize_priorities(root)

    # 6. 非法编号隔离（H2，幂等）：active 关系转墓碑、任务移除
    quarantined = 0
    for directory in ("relations", "relations_search"):
        for shard in sorted((sdir / directory).glob("*.jsonl")):
            records = state_mod.read_jsonl(shard)
            changed = False
            for record in records:
                if (record.get("verification") != "rejected"
                        and not is_valid_cve_id(record.get("cve_id", ""))):
                    record.update({
                        "verification": "rejected",
                        "auto": True,
                        "rejected_reason": "invalid_cve_id_format",
                        "rejected_evidence": f"invalid CVE id: {record.get('cve_id')}",
                        "rejected_evidence_fetched_at": state_mod.now_iso(),
                        "rejected_at": state_mod.now_iso(),
                        "rule_version": RULES_VERSION,
                    })
                    quarantined += 1
                    changed = True
            if changed:
                state_mod.write_jsonl(shard, records)
    invalid_tasks = [t["cve_id"] for t in scheduler.load_tasks(root)
                     if not is_valid_cve_id(t["cve_id"])]
    if invalid_tasks:
        scheduler.cancel_many(root, invalid_tasks)
    report["invalid_id_quarantined"] = quarantined
    report["invalid_id_tasks_dropped"] = len(invalid_tasks)

    state_mod.write_json(sdir / "migrate_report.json",
                         {**report, "ts": state_mod.now_iso()})
    return report
