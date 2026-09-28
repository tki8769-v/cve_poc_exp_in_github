"""CVE 级权威状态（评审 R9 + F5 + G1）：官方状态按源版本单调更新。

- 状态记录区分 source_kind（G1）：release（可按 tag 排序的权威版本）与
  legacy_event（历史迁移线索，不参与版本排序，任何正式版本可覆盖）；
- release 之间按 source_tag 字符串比较，较旧快照不得覆盖较新状态；
  REJECTED 之后出现较新的 PUBLISHED 可恢复（解除入队/发现封锁）；
- set_state 返回是否接受（G7）：只有被接受的更新才允许触发任务、
  事件等副作用；渲染/验证的"有效关系视图"查询同一状态表（F5）。
"""
from __future__ import annotations

from pathlib import Path

from . import state as state_mod

__all__ = ["load_states", "is_rejected", "set_state", "record_kind", "STATES_FILE"]

STATES_FILE = "cve_states.jsonl"

KIND_RELEASE = "release"
KIND_LEGACY = "legacy_event"


def _path(root: Path) -> Path:
    return state_mod.state_dir(root) / STATES_FILE


def load_states(root: Path) -> dict[str, dict]:
    states: dict[str, dict] = {}
    for record in state_mod.read_jsonl(_path(root)):
        states[record["cve_id"]] = record  # 后行覆盖前行
    return states


def record_kind(record: dict) -> str:
    """记录的 source_kind；旧记录缺字段时按 source_tag 推断（G1）。"""
    kind = record.get("source_kind")
    if kind in (KIND_RELEASE, KIND_LEGACY):
        return kind
    return KIND_LEGACY if record.get("source_tag") == "legacy_event" else KIND_RELEASE


def is_rejected(root: Path, cve_id: str) -> bool:
    record = load_states(root).get(cve_id.upper())
    return bool(record and record.get("state") == "REJECTED")


def set_state(root: Path, cve_id: str, state: str, source_tag: str = "",
              source_kind: str | None = None) -> bool:
    """按源版本单调更新（G1）。返回 True=已接受，False=被既有较新版本压下。

    - release vs release：source_tag 字符串比较，较旧不覆盖较新；
    - legacy_event 是待权威对账的历史线索：不覆盖 release，
      且可被任何正式 release（含更早 tag）覆盖。
    """
    cve_id = cve_id.upper()
    kind = source_kind or (KIND_LEGACY if source_tag == "legacy_event" else KIND_RELEASE)
    states = load_states(root)
    existing = states.get(cve_id)
    if existing:
        old_kind = record_kind(existing)
        if old_kind == KIND_RELEASE:
            if kind == KIND_LEGACY:
                return False  # 历史线索不覆盖权威版本
            old_tag = existing.get("source_tag") or ""
            if source_tag and old_tag and source_tag < old_tag:
                return False  # 旧快照不覆盖新状态
        # existing 为 legacy_event：任何更新可覆盖（含正式 release）
    record = existing or {"cve_id": cve_id}
    record.update({"state": state, "since": state_mod.now_iso(),
                   "source_tag": source_tag, "source_kind": kind})
    states[cve_id] = record
    rows = [states[key] for key in sorted(states)]
    state_mod.write_jsonl(_path(root), rows)
    return True
