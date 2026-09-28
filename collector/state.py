"""内部状态持久化（REFACTOR_PLAN.md §2 / 3.7）。

state/ 目录存放来源游标、引导关系、回补清单、审计与清洗报告等内部
状态：按年份分片的 JSONL、稳定排序、原子写（同目录 tmp + os.replace、
显式 UTF-8）。内部状态不嵌入公开产物（README / PocOrExp.md）。
"""
from __future__ import annotations

import json
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Union

from . import RULES_VERSION

__all__ = [
    "project_root",
    "state_dir",
    "atomic_write_text",
    "write_jsonl",
    "read_jsonl",
    "append_jsonl",
    "write_json",
    "read_json",
    "now_iso",
]


def now_iso() -> str:
    """统一 UTC 时间戳（固定格式，字符串比较即时间比较）。"""
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def project_root() -> Path:
    return Path(__file__).resolve().parents[1]


def state_dir(root: Union[Path, None] = None) -> Path:
    directory = (root or project_root()) / "state"
    directory.mkdir(parents=True, exist_ok=True)
    return directory


def atomic_write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name + ".tmp")
    with open(tmp, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    os.replace(tmp, path)


def write_jsonl(path: Path, records: list[dict]) -> None:
    lines = [json.dumps(record, ensure_ascii=False, sort_keys=True) for record in records]
    atomic_write_text(path, "\n".join(lines) + ("\n" if lines else ""))


def read_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    records = []
    with open(path, "r", encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if line:
                records.append(json.loads(line))
    return records


def write_json(path: Path, payload) -> None:
    atomic_write_text(path, json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n")


def read_json(path: Path, default=None):
    if not path.exists():
        return default
    with open(path, "r", encoding="utf-8") as fh:
        return json.load(fh)


def append_jsonl(path: Path, records: list[dict]) -> None:
    """以读改写方式追加（整文件原子替换），保持崩溃安全与去重由调用方负责。"""
    existing = read_jsonl(path)
    write_jsonl(path, existing + records)
