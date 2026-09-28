"""attrib.py 三态归属判定用例（保守规则，REFACTOR_PLAN.md 3.4 / 评审 R4）。

业务预期来自计划规则，不照实现填写：
- "regression of CVE-X" 类上下文引用 → needs_review（不得自动接受）
- 空描述 / 沉默描述 / 元数据缺失 → needs_review（不得作为排除依据）
- 仅"描述明确自述为 URL 所指编号"构成充分排除证据
"""
from __future__ import annotations

from collector.attrib import (
    ACCEPTED,
    CONFLICT_CANDIDATE,
    INSUFFICIENT_EVIDENCE,
    NEEDS_REVIEW,
    classify_relation,
)


class TestAccepted:
    def test_url_contains_target(self):
        verdict = classify_relation("CVE-2020-1234", "https://github.com/a/CVE-2020-1234-poc")
        assert verdict.state == ACCEPTED
        assert verdict.reason == "url_contains_target"

    def test_multi_cve_repo_is_kept_for_both(self):
        url = "https://github.com/koozxcv/CVE-2014-7911-CVE-2014-4322_get_root_privilege"
        for cve in ("CVE-2014-7911", "CVE-2014-4322"):
            assert classify_relation(cve, url).state == ACCEPTED

    def test_case_insensitive_url(self):
        assert classify_relation("CVE-2020-1234", "https://github.com/a/cve-2020-1234").state == ACCEPTED

    def test_desc_only_when_url_has_no_ids(self):
        # 采集标准允许：URL 无编号、描述精确包含目标（搜索即按描述命中）
        verdict = classify_relation("CVE-2021-44228", "https://github.com/a/log4shell-poc",
                                    repo_description="exploit for CVE-2021-44228")
        assert verdict.state == ACCEPTED
        assert verdict.reason == "desc_contains_target_only"

    def test_topics_extra_text_counts(self):
        verdict = classify_relation("CVE-2021-44228", "https://github.com/a/log4shell-poc",
                                    repo_description="", extra_text="cve-2021-44228 rce")
        assert verdict.state == ACCEPTED


class TestNeedsReview:
    def test_regression_mention_is_not_acceptance(self):
        # 评审 R4 核心场景：URL 指向别的编号，描述写 "regression of 目标"
        verdict = classify_relation(
            "CVE-2006-5051", "https://github.com/s/CVE-2024-6387",
            repo_description="regression of CVE-2006-5051 in OpenSSH",
        )
        assert verdict.state == NEEDS_REVIEW
        assert verdict.reason == "desc_mention_with_url_conflict"

    def test_empty_description_cannot_exclude(self):
        verdict = classify_relation("CVE-2014-9137",
                                    "https://github.com/jamaal001/CVE-2014-91371-Wordpress-",
                                    repo_description="")
        assert verdict.state == NEEDS_REVIEW
        assert verdict.reason == "empty_description_no_evidence"

    def test_missing_meta_is_not_a_verdict(self):
        verdict = classify_relation("CVE-2014-9137",
                                    "https://github.com/jamaal001/CVE-2014-91371-Wordpress-")
        assert verdict.state == NEEDS_REVIEW
        assert verdict.reason == "meta_missing"

    def test_silent_description_is_insufficient(self):
        verdict = classify_relation("CVE-2016-0856",
                                    "https://github.com/404godd/CVE-2026-20841-PoC",
                                    repo_description="A remote code execution demo tool")
        assert verdict.state == NEEDS_REVIEW
        assert verdict.reason == "silent_description_insufficient"

    def test_desc_target_with_foreign_url_conflicting(self):
        verdict = classify_relation(
            "CVE-2020-1234", "https://github.com/x/CVE-2020-12345",
            repo_description="exploit for CVE-2020-1234 (repo name typo)",
        )
        assert verdict.state == NEEDS_REVIEW
        assert verdict.reason == "desc_mention_with_url_conflict"


class TestConflictCandidate:
    def test_evidenced_foreign_id(self):
        verdict = classify_relation("CVE-2015-5711", "https://github.com/TrixSec/CVE-2015-57115",
                                    repo_description="Mass Checker For CVE-2015-57115")
        assert verdict.state == CONFLICT_CANDIDATE
        assert verdict.reason == "prefix_conflict_evidenced"

    def test_evidenced_prefix_real_sample(self):
        verdict = classify_relation(
            "CVE-2014-9137", "https://github.com/jamaal001/CVE-2014-91371-Wordpress-",
            repo_description="Wordpress exploit for CVE-2014-91371",
        )
        assert verdict.state == CONFLICT_CANDIDATE

    def test_evidenced_foreign_without_prefix(self):
        verdict = classify_relation("CVE-2006-5051", "https://github.com/bigb0x/CVE-2024-6387",
                                    repo_description="RegreSSHion CVE-2024-6387 scanner")
        assert verdict.state == CONFLICT_CANDIDATE
        assert verdict.reason == "foreign_id_conflict_evidenced"


class TestInsufficientEvidence:
    def test_no_ids_anywhere(self):
        verdict = classify_relation("CVE-2018-9995", "https://github.com/quocquoc181/dvr",
                                    repo_description="dvr tool")
        assert verdict.state == INSUFFICIENT_EVIDENCE


class TestVerdictRecord:
    def test_record_is_traceable(self):
        verdict = classify_relation("CVE-2015-5711", "https://github.com/TrixSec/CVE-2015-57115",
                                    repo_description="Mass Checker For CVE-2015-57115")
        record = verdict.to_record()
        assert record["rule_version"]
        assert record["url_ids"] == ["CVE-2015-57115"]
        assert record["evidence_ids"] == ["CVE-2015-57115"]
