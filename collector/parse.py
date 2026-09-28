"""统一、版本化的解析规则（REFACTOR_PLAN.md 3.1）。

审计、bootstrap、clean 与后续生产模块的 CVE 提取、GitHub URL 解析、
年份 README 解析必须全部经由本模块，保证统计口径一致可比。
任何规则变更必须递增 RULES_VERSION。
"""
from __future__ import annotations

import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterator, NamedTuple, Optional
from urllib.parse import urlparse

from . import RULES_VERSION

__all__ = [
    "RULES_VERSION",
    "CVE_RE",
    "Relation",
    "normalize_cve_id",
    "extract_cve_ids",
    "is_valid_cve_id",
    "parse_github_repo",
    "iter_readme_relations",
    "parse_readme_file",
]

# CVE 编号：4 位年份 + 任意长度序号（保留前导零，集合内精确比较）。
CVE_RE = re.compile(r"CVE-\d{4}-\d+", re.IGNORECASE)

# 合法 CVE 编号（下游契约口径，compat 模块同源）：序号至少 4 位。
# 采集边界用它过滤短编号（CVE-2026-1）——此类编号能进状态但不能被
# 下游解析，会令 verify 永久失败、阻断发布（评审 H2）。
# 年份范围另行限制为 1999..次年预留（评审 I1）：render/verify 只枚举
# 1xxx/2xxx 年份目录，CVE-0000-0000/未来年份占位编号同样会阻断发布。
VALID_CVE_RE = re.compile(r"^CVE-(\d{4})-\d{4,}$", re.IGNORECASE)

# CVE 编号自 1999 年启用；次年编号提前预留。
FIRST_CVE_YEAR = 1999

# 年份 README 链接行：'- [text](url) : ![starts](...)'，取链接目标 URL。
README_LINK_RE = re.compile(r"^- \[[^\]]+\]\(([^)]+)\)")

# 年份 README 小节标题：'## CVE-2020-1234'。
README_HEADING_RE = re.compile(r"^## (CVE-\d{4}-\d+)\s*$")

GITHUB_HOSTS = {"github.com"}


def normalize_cve_id(value: str) -> str:
    return value.strip().upper()


def is_valid_cve_id(cve_id: str) -> bool:
    """采集边界合法性校验：年份 4 位且在支持范围内 + 序号至少 4 位。

    年份范围与发布产物一致（render/verify 只枚举 1xxx/2xxx 年份目录，
    且 CVE 编号 1999 年才启用、次年预留），评审 H2/I1。
    """
    match = VALID_CVE_RE.match((cve_id or "").strip())
    if not match:
        return False
    year = int(match.group(1))
    return FIRST_CVE_YEAR <= year <= datetime.now(timezone.utc).year + 1


def extract_cve_ids(*texts: Optional[str]) -> set[str]:
    """从任意多段文本提取 CVE 编号集合（大写、保留前导零）。"""
    ids: set[str] = set()
    for text in texts:
        if text:
            ids.update(normalize_cve_id(match) for match in CVE_RE.findall(text))
    return ids


def parse_github_repo(url: str) -> tuple[Optional[str], Optional[str]]:
    """解析 github.com 仓库 URL，返回 (owner, repo)；非仓库 URL 返回 (None, None)。"""
    try:
        parsed = urlparse(url)
    except ValueError:
        return None, None
    if parsed.scheme not in ("http", "https") or parsed.netloc.lower() not in GITHUB_HOSTS:
        return None, None
    parts = [p for p in parsed.path.split("/") if p]
    if len(parts) < 2 or not parts[1]:
        return None, None
    repo = parts[1]
    if repo.endswith(".git"):
        repo = repo[: -len(".git")]
    return parts[0], repo or None


class Relation(NamedTuple):
    cve_id: str
    url: str


def iter_readme_relations(path: Path) -> Iterator[Relation]:
    """逐条产出年份 README 中的 (CVE, URL) 关系。

    口径与 REFACTOR_REVIEW.md 第 8 节一致：'## CVE-...' 标题切换当前
    小节，其他 '## ' 标题结束小节，链接取 URL（括号目标）。
    """
    current: Optional[str] = None
    with open(path, "r", encoding="utf-8") as fh:
        for line in fh:
            line = line.rstrip("\n")
            heading = README_HEADING_RE.match(line)
            if heading:
                current = normalize_cve_id(heading.group(1))
                continue
            if line.startswith("## "):
                current = None
                continue
            link = README_LINK_RE.match(line)
            if current and link:
                yield Relation(current, link.group(1).strip())


def parse_readme_file(path: Path) -> list[Relation]:
    """解析单个 README 并去重（保持首次出现顺序）。"""
    seen: set[tuple[str, str]] = set()
    relations: list[Relation] = []
    for rel in iter_readme_relations(path):
        key = (rel.cve_id, rel.url)
        if key not in seen:
            seen.add(key)
            relations.append(rel)
    return relations
