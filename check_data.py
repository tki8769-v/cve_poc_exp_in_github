#!/usr/bin/env python3
"""审计扫描入口（REFACTOR_PLAN.md 3.1）：固定口径 + 规则版本 + 基线漂移对比。"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from collector import state as state_mod
from collector.audit import format_report, run_audit


def main() -> int:
    root = Path(__file__).resolve().parent
    result = run_audit(root)
    print(format_report(result))
    state_mod.write_json(state_mod.state_dir(root) / "audit_report.json", result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
