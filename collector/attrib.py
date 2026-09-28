"""三态归属判定（REFACTOR_PLAN.md 3.4 保守规则，按评审 R4 修订）。

判定分级（评审要求区分"编号出现""关联证据""足以排除的证据"）：

  accepted              URL 编号集合包含目标；或 URL 无任何编号而描述/补充
                        文本精确包含目标（采集标准允许的描述证据）
  needs_review          证据不足或相互冲突，一律待复核，不自动处置：
                        - desc_mention_with_url_conflict：URL 指向其他编号、
                          描述又提及目标（"regression of CVE-X" 类上下文
                          引用只是关系线索，不能直接认定对应 PoC）
                        - empty_description_no_evidence：空描述不能作为
                          排除依据
                        - silent_description_insufficient：描述存在但既不
                          提及目标也不确认 URL 所指编号
                        - meta_missing：元数据尚未回补
  conflict_candidate    充分排除证据：URL 含其他编号且不含目标，同时描述
                        非空、不含目标、且明确自述为 URL 所指的外来编号
                        （如 "Mass Checker For CVE-2015-57115"）
  insufficient_evidence URL 与全部证据文本均无任何编号

每条判定记录证据编号集合、原因代码与规则版本。
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from . import RULES_VERSION
from .parse import extract_cve_ids, normalize_cve_id

__all__ = [
    "ACCEPTED",
    "NEEDS_REVIEW",
    "CONFLICT_CANDIDATE",
    "INSUFFICIENT_EVIDENCE",
    "Verdict",
    "classify_relation",
]

ACCEPTED = "accepted"
NEEDS_REVIEW = "needs_review"
CONFLICT_CANDIDATE = "conflict_candidate"
INSUFFICIENT_EVIDENCE = "insufficient_evidence"


@dataclass
class Verdict:
    state: str
    reason: str
    cve_id: str
    url: str
    url_ids: list[str] = field(default_factory=list)
    evidence_ids: list[str] = field(default_factory=list)
    rule_version: str = RULES_VERSION

    def to_record(self) -> dict:
        return {
            "state": self.state,
            "reason": self.reason,
            "cve_id": self.cve_id,
            "url": self.url,
            "url_ids": self.url_ids,
            "evidence_ids": self.evidence_ids,
            "rule_version": self.rule_version,
        }


def classify_relation(
    cve_id: str,
    url: str,
    repo_description: Optional[str] = None,
    extra_text: str = "",
) -> Verdict:
    """对一条 (CVE, URL) 关系做归属判定。

    repo_description 为已回补的仓库描述；None 表示元数据缺失（与空串
    区分：空串是"已确认无描述"，None 是"还没查"）。extra_text 汇集
    topics 等其他证据文本。
    """
    cve_id = normalize_cve_id(cve_id)
    url_ids = sorted(extract_cve_ids(url))
    evidence_ids = extract_cve_ids(repo_description or "", extra_text)
    evidence_sorted = sorted(evidence_ids)

    if cve_id in url_ids:
        state, reason = ACCEPTED, "url_contains_target"
    elif not url_ids:
        if cve_id in evidence_ids:
            if evidence_ids - {cve_id}:
                # F6：描述同时提及多个编号且 URL 无目标证据——无法判定
                # 主体关联与背景引用（regression 类），进复核
                state, reason = NEEDS_REVIEW, "multi_id_mention_unresolved"
            else:
                state, reason = ACCEPTED, "desc_contains_target_only"
        else:
            state, reason = INSUFFICIENT_EVIDENCE, "no_cve_id_in_evidence"
    else:
        # URL 指向其他编号且不含目标：需要充分证据才能排除
        if repo_description is None:
            state, reason = NEEDS_REVIEW, "meta_missing"
        elif cve_id in evidence_ids:
            state, reason = NEEDS_REVIEW, "desc_mention_with_url_conflict"
        elif not repo_description.strip():
            state, reason = NEEDS_REVIEW, "empty_description_no_evidence"
        elif evidence_ids & set(url_ids):
            if any(value.startswith(cve_id) for value in url_ids):
                reason = "prefix_conflict_evidenced"
            else:
                reason = "foreign_id_conflict_evidenced"
            state = CONFLICT_CANDIDATE
        else:
            state, reason = NEEDS_REVIEW, "silent_description_insufficient"

    return Verdict(
        state=state, reason=reason, cve_id=cve_id, url=url,
        url_ids=url_ids, evidence_ids=evidence_sorted,
    )
