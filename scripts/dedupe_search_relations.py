"""一次性清理：relations_search 中与 legacy 重复的记录 + 虚假 new_poc 事件。"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from collector import state as state_mod

root = Path(__file__).resolve().parents[1]
sdir = state_mod.state_dir(root)

legacy_keys = {
    (r["cve_id"], r["url"])
    for p in sorted((sdir / "relations").glob("*.jsonl"))
    for r in state_mod.read_jsonl(p)
}

removed_dup = 0
for shard in sorted((sdir / "relations_search").glob("*.jsonl")):
    records = state_mod.read_jsonl(shard)
    kept = []
    for record in records:
        if (record["cve_id"], record["url"]) in legacy_keys:
            removed_dup += 1
        else:
            kept.append(record)
    state_mod.write_jsonl(shard, kept)

events = state_mod.read_jsonl(sdir / "events.jsonl")
kept_events = [
    e for e in events
    if not (e.get("type") == "new_poc" and (e.get("cve_id"), e.get("url")) in legacy_keys)
]
removed_events = len(events) - len(kept_events)
state_mod.write_jsonl(sdir / "events.jsonl", kept_events)

print(f"清理完成: 移除 search 分片重复记录 {removed_dup} 条, 移除虚假 new_poc 事件 {removed_events} 条")
