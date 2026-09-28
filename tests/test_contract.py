"""下游契约测试（REFACTOR_PLAN.md 3.7 / 验收 6）。

用真实下游纯解析函数（父项目 service/poc_source_pocorexp.py 的
parse_poc_markdown_files）对比 collector 的解析结果，验证年份 README
的 Markdown 契约不因改造被破坏。父项目不存在或无法导入时跳过。
"""
from __future__ import annotations

import sys
from pathlib import Path

import pytest

from collector.parse import parse_readme_file

PROJECT_ROOT = Path(__file__).resolve().parents[1]
PARENT_ROOT = PROJECT_ROOT.parent

FIXTURE_README = """## CVE-2099-0001
> fixture description

- [https://github.com/a/one](https://github.com/a/one) : ![starts](https://img.shields.io/github/stars/a/one.svg)
- [https://github.com/b/CVE-2099-0002](https://github.com/b/CVE-2099-0002) : ![starts](https://img.shields.io/github/stars/b/CVE-2099-0002.svg)

## CVE-2099-0002
- [https://github.com/b/CVE-2099-0002](https://github.com/b/CVE-2099-0002) : ![starts](x)
"""


def _downstream_parser():
    module_path = PARENT_ROOT / "service" / "poc_source_pocorexp.py"
    if not module_path.exists():
        pytest.skip("下游解析函数不可用（父项目 service/ 缺失）")
    sys.path.insert(0, str(PARENT_ROOT))
    try:
        from service.poc_source_pocorexp import parse_poc_markdown_files
    except Exception as exc:  # 配置缺失等环境原因
        pytest.skip(f"下游模块导入失败: {exc}")
    return parse_poc_markdown_files


def _collector_map(year_dir: Path) -> dict[str, set[str]]:
    readme = year_dir / "README.md"
    mapping: dict[str, set[str]] = {}
    for rel in parse_readme_file(readme):
        mapping.setdefault(rel.cve_id, set()).add(rel.url)
    return mapping


def _downstream_map(year_dir: Path) -> dict[str, set[str]]:
    parser = _downstream_parser()
    raw = parser(str(year_dir))
    return {cve: set(urls) for cve, urls in raw.items()}


def test_contract_on_fixture(tmp_path: Path):
    year_dir = tmp_path / "2099"
    year_dir.mkdir()
    (year_dir / "README.md").write_text(FIXTURE_README, encoding="utf-8")
    assert _collector_map(year_dir) == _downstream_map(year_dir)


def test_contract_on_real_year_2026():
    year_dir = PROJECT_ROOT / "2026"
    if not (year_dir / "README.md").exists():
        pytest.skip("2026/README.md 不存在")
    ours = _collector_map(year_dir)
    theirs = _downstream_map(year_dir)
    assert ours == theirs
    assert ours, "2026 年份目录应解析出非空映射"
