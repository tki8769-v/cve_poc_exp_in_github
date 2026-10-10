"""官方 CVE 引用通道（主动发现改造阶段 2A，实施方案 §1.1/§1.2）。

CNA/ADP references 是**发现线索**，不是判定结论：
- 引用大量指向修复 commit、补丁 PR、产品源码、公告——保存时按证据分级
  （poc > reference > patch/advisory），patch/advisory 不做元数据级自动确认；
- 判定只用仓库自身元数据（名称/描述/topics），官方"引用了这个仓库"这一
  事实只触发查看、绝不充当归属证据——杜绝循环证明；
- 候选先持久化（state/candidates/official_refs.jsonl），来源游标不越过
  未保存结果；patch 类候选保留待内容取证（后续阶段）。
"""
from __future__ import annotations

from pathlib import Path

from . import cvestate
from . import state as state_mod
from .attrib import ACCEPTED, CONFLICT_CANDIDATE, classify_relation
from .ghsearch import Budget
from .parse import is_valid_cve_id, parse_github_repo

__all__ = ["ref_kind", "extract_references", "record_candidates",
           "process_official_refs", "CANDIDATES_FILE"]

CANDIDATES_FILE = "candidates/official_refs.jsonl"

# 元数据级自动确认只处理这两类；patch/advisory 需内容取证（后续阶段）
PROCESSABLE_KINDS = ("poc", "reference")


def ref_kind(url: str, tags: list) -> str:
    """引用证据分级（保存时标注，实施方案 §4.3）。标签按子串匹配
    （cvelistV5 使用 "Vendor Advisory" 等组合标签）。"""
    lowered_tags = {str(t).lower() for t in (tags or [])}

    def has(keyword: str) -> bool:
        return any(keyword in t for t in lowered_tags)

    if has("exploit"):
        return "poc"
    lowered_url = (url or "").lower()
    if has("patch") or "/commit/" in lowered_url or "/pull/" in lowered_url:
        return "patch"
    if has("advisory"):
        return "advisory"
    return "reference"


def extract_references(data: dict) -> list[dict]:
    """从一条 cvelistV5 记录提取 GitHub 引用（CNA 与 ADP 容器）。"""
    out: list[dict] = []
    containers = (data.get("containers") or {})
    sources = [("cna", containers.get("cna") or {})]
    for adp in containers.get("adp") or []:
        if isinstance(adp, dict):
            sources.append(("adp", adp))
    for container, payload in sources:
        for ref in payload.get("references") or []:
            url = str(ref.get("url") or "")
            owner_repo = parse_github_repo(url)
            if not (owner_repo and owner_repo[0] and owner_repo[1]):
                continue  # 非 GitHub 仓库链接：本通道不处理
            out.append({
                "url": url,
                "repo_owner": owner_repo[0],
                "repo_name": owner_repo[1],
                "kind": ref_kind(url, ref.get("tags") or []),
                "tags": [str(t) for t in (ref.get("tags") or [])],
                "container": container,
            })
    return out


def _candidates_path(root: Path) -> Path:
    return state_mod.state_dir(root) / CANDIDATES_FILE


def record_candidates(root: Path, cve_id: str, references: list[dict],
                      source_tag: str) -> int:
    """持久化引用候选（按 (cve_id, url) 去重）。返回新增数。

    必须在来源游标推进前调用（候选不落盘，游标不得越过）。
    """
    if not is_valid_cve_id(cve_id):
        return 0
    path = _candidates_path(root)
    rows = state_mod.read_jsonl(path)
    known = {(r["cve_id"], r["url"]) for r in rows}
    added = 0
    now = state_mod.now_iso()
    for ref in references:
        key = (cve_id, ref["url"])
        if key in known:
            continue
        known.add(key)
        rows.append({
            "cve_id": cve_id,
            "url": ref["url"],
            "repo_owner": ref["repo_owner"],
            "repo_name": ref["repo_name"],
            "kind": ref["kind"],
            "tags": ref["tags"],
            "container": ref["container"],
            "source_tag": source_tag,
            "first_seen": now,
            "status": "pending",
        })
        added += 1
    if added:
        state_mod.write_jsonl(path, rows)
    return added


def process_official_refs(client, root: Path, limit: int = 30,
                          budget: Budget | None = None) -> dict:
    """小预算取证处理候选：仅用仓库自身元数据判定（反循环证明）。

    - kind=poc/reference 且仓库元数据独立支持归属 → 合并关系
      （source=official_reference，引用证据随关系保存）；
    - 元数据不足 → 候选保留（kept_for_review），不建关系不误收；
    - 元数据指向其他编号 → 标记 rejected_lead；
    - patch/advisory → 跳过（需内容取证）；官方 REJECTED/非法编号 → 标记。
    """
    from .scan import merge_accepted

    path = _candidates_path(root)
    rows = state_mod.read_jsonl(path)
    stats = {
        "candidates_total": len(rows),
        "pending_before": sum(1 for r in rows if r.get("status") == "pending"),
        "processed": 0,
        "accepted": 0,
        "kept_for_review": 0,
        "rejected_lead": 0,
        "patchlike_skipped": 0,
        "meta_fetched": 0,
        "requests_used": 0,
        "stop_reason": None,
    }

    changed = False
    for record in rows:
        if stats["processed"] >= limit:
            break
        if record.get("status") != "pending":
            continue
        cve_id = record["cve_id"]
        if not is_valid_cve_id(cve_id):
            record["status"] = "invalid_id"
            changed = True
            continue
        if cvestate.is_rejected(root, cve_id):
            record["status"] = "cve_rejected"
            changed = True
            continue
        if record.get("kind") not in PROCESSABLE_KINDS:
            record["status"] = "deferred_content_verification"
            stats["patchlike_skipped"] += 1
            changed = True
            continue

        owner, repo = record["repo_owner"], record["repo_name"]
        repo_url = f"https://github.com/{owner}/{repo}"
        try:
            info = client.get_repo(owner, repo, budget=budget)
        except Exception as exc:  # 预算/网络中断：候选保留，下轮续跑
            stats["stop_reason"] = f"{type(exc).__name__}: {exc}"
            break
        stats["meta_fetched"] += 1
        stats["processed"] += 1
        if info is None:
            record["status"] = "gone"
            changed = True
            continue

        topics = " ".join(info.get("topics") or [])
        # 反循环证明：仅以仓库自身元数据判定；引用事实不进证据
        verdict = classify_relation(cve_id, repo_url,
                                    repo_description=info.get("description") or "",
                                    extra_text=topics)
        if verdict.state == ACCEPTED:
            created = merge_accepted(
                root, cve_id, repo_url,
                {"stargazers_count": info.get("stargazers_count"),
                 "forks_count": info.get("forks_count")},
                verdict=verdict, source="official_reference",
                extra={"official_reference": {
                    "url": record["url"], "kind": record["kind"],
                    "tags": record["tags"], "source_tag": record["source_tag"],
                }},
            )
            stats["accepted"] += 1
            record["status"] = "accepted"
            record["processed_at"] = state_mod.now_iso()
        elif verdict.state == CONFLICT_CANDIDATE:
            stats["rejected_lead"] += 1
            record["status"] = "rejected_lead"
            record["processed_at"] = state_mod.now_iso()
        else:
            stats["kept_for_review"] += 1
            record["status"] = "kept_for_review"
            record["processed_at"] = state_mod.now_iso()
        changed = True

    stats["requests_used"] = budget.requests_used if budget is not None else None
    stats["pending_after"] = sum(1 for r in rows if r.get("status") == "pending")
    if changed:
        state_mod.write_jsonl(path, rows)
    return stats
