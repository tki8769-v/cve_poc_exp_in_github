"""黑名单过滤（沿用上游 blacklist.txt 的 URL 前缀匹配约定）。"""
from __future__ import annotations

from pathlib import Path

__all__ = ["load_blacklist", "is_blocked"]

BLACKLIST_FILE = "blacklist.txt"


def load_blacklist(root: Path) -> list[str]:
    path = root / BLACKLIST_FILE
    if not path.exists():
        return []
    entries = []
    with open(path, "r", encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if line:
                entries.append(line)
    return entries


def is_blocked(url: str, entries: list[str]) -> bool:
    return any(url.startswith(entry) for entry in entries)
