"""parse.py 统一解析规则边界用例（REFACTOR_PLAN.md 验收 2）。"""
from __future__ import annotations

from pathlib import Path

from collector.parse import (
    Relation,
    extract_cve_ids,
    iter_readme_relations,
    parse_github_repo,
    parse_readme_file,
)


class TestExtractCveIds:
    def test_case_insensitive(self):
        assert extract_cve_ids("repo for cve-2020-1234") == {"CVE-2020-1234"}

    def test_prefix_ids_are_distinct(self):
        # 用户报告的核心场景：CVE-2020-1234 与 CVE-2020-12345 是不同编号
        ids = extract_cve_ids("CVE-2020-1234 CVE-2020-12345")
        assert ids == {"CVE-2020-1234", "CVE-2020-12345"}
        assert "CVE-2020-1234" not in extract_cve_ids("only CVE-2020-12345 here")
        assert "CVE-2014-9137" not in extract_cve_ids("CVE-2014-91371-Wordpress-")

    def test_leading_zeros_preserved(self):
        assert extract_cve_ids("CVE-2020-0123") == {"CVE-2020-0123"}
        assert extract_cve_ids("CVE-2020-0123") != {"CVE-2020-123"}

    def test_long_sequence_ids(self):
        assert extract_cve_ids("CVE-2021-41091 CVE-2021-4109123") == {
            "CVE-2021-41091",
            "CVE-2021-4109123",
        }

    def test_multiple_cves_in_one_url(self):
        url = "https://github.com/koozxcv/CVE-2014-7911-CVE-2014-4322_get_root_privilege"
        assert extract_cve_ids(url) == {"CVE-2014-7911", "CVE-2014-4322"}

    def test_no_cve_in_plain_url(self):
        assert extract_cve_ids("https://github.com/z3rox1s/PrintNightmare") == set()

    def test_none_and_empty_texts(self):
        assert extract_cve_ids(None, "", "CVE-2020-1") == {"CVE-2020-1"}
        assert extract_cve_ids(None, "") == set()


class TestParseGithubRepo:
    def test_plain_repo(self):
        assert parse_github_repo("https://github.com/owner/repo") == ("owner", "repo")

    def test_trailing_slash(self):
        assert parse_github_repo("https://github.com/owner/repo/") == ("owner", "repo")

    def test_dot_git_suffix(self):
        assert parse_github_repo("https://github.com/owner/repo.git") == ("owner", "repo")

    def test_subpath_keeps_owner_repo(self):
        assert parse_github_repo("https://github.com/owner/repo/tree/main/src") == ("owner", "repo")

    def test_non_github_host(self):
        assert parse_github_repo("https://gitlab.com/owner/repo") == (None, None)

    def test_profile_url_only(self):
        assert parse_github_repo("https://github.com/owner") == (None, None)

    def test_not_a_url(self):
        assert parse_github_repo("not a url") == (None, None)


README_FIXTURE = """# Title

## CVE-2020-1234
> Some description mentioning CVE-2020-1234

- [https://github.com/a/one](https://github.com/a/one) : ![starts](https://img.shields.io/github/stars/a/one.svg)
- [https://github.com/c/CVE-2020-12345](https://github.com/c/CVE-2020-12345) : ![starts](x)

## Other Heading

- [https://github.com/d/excluded](https://github.com/d/excluded)

## CVE-2021-42
- [https://github.com/e/poc](https://github.com/e/poc)
"""


class TestReadmeParsing:
    def test_relations_and_section_scoping(self, tmp_path: Path):
        readme = tmp_path / "README.md"
        readme.write_text(README_FIXTURE, encoding="utf-8")
        relations = parse_readme_file(readme)
        # 非 CVE 标题之后的链接不属于任何小节，必须被排除
        assert relations == [
            Relation("CVE-2020-1234", "https://github.com/a/one"),
            Relation("CVE-2020-1234", "https://github.com/c/CVE-2020-12345"),
            Relation("CVE-2021-42", "https://github.com/e/poc"),
        ]

    def test_dedup_preserves_first_order(self, tmp_path: Path):
        readme = tmp_path / "README.md"
        readme.write_text(
            "## CVE-2020-1\n- [u](https://github.com/a/b)\n- [u2](https://github.com/a/b)\n",
            encoding="utf-8",
        )
        assert parse_readme_file(readme) == [Relation("CVE-2020-1", "https://github.com/a/b")]

    def test_iterator_matches_parser(self, tmp_path: Path):
        readme = tmp_path / "README.md"
        readme.write_text(README_FIXTURE, encoding="utf-8")
        assert list(iter_readme_relations(readme)) == parse_readme_file(readme)
