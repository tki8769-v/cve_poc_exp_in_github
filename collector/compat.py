"""下游兼容解析器（评审 R16）。

独立仓库的 CI 缺少父项目 service/ 时，用本模块复刻
service.poc_source_pocorexp.parse_poc_markdown_files 的解析行为
（同样的标题/链接正则与链接文字取法），保证发布契约校验在任何
环境都可执行。父项目存在时优先使用真实解析函数。
"""
from __future__ import annotations

import os
import re
from pathlib import Path

__all__ = ["vendored_parse_markdown_files"]

_CVE_PATTERN = re.compile(r"##\s+(CVE-\d{4,}-\d{4,})")
_URL_PATTERN = re.compile(r"-\s+\[(https://github\.com/[^\]]+)\]")


def vendored_parse_markdown_files(base_path: str) -> dict[str, list[str]]:
    """行为对齐父项目解析器：walk 目录找 readme.md，取链接文字中的 URL。"""
    poc_map: dict[str, list[str]] = {}
    for root, _, files in os.walk(base_path):
        readme = next((f for f in files if f.lower() == "readme.md"), None)
        if not readme:
            continue
        current = None
        with open(os.path.join(root, readme), "r", encoding="utf-8") as fh:
            for line in fh:
                cve_match = _CVE_PATTERN.match(line)
                if cve_match:
                    current = cve_match.group(1)
                elif current:
                    url_match = _URL_PATTERN.match(line)
                    if url_match:
                        poc_map.setdefault(current, []).append(url_match.group(1))
    return poc_map
