"""日常编排（REFACTOR_PLAN.md 3.6/3.8 / 评审 R7/R11/R16）。

按预算依次：sync → repo_watch(discover) → scan → backfill（冲突优先，
带缓存过期重取）→ recheck → clean --apply → render → verify。

- verify 失败立即非零退出（不发布坏数据）；
- 整轮共享时间预算（R11）：各阶段用剩余时间，等待超预算即退出；
- last_attempt 与 last_success 分离（R16）：前者总是写，后者仅在
  verify 通过后写；
- 全程幂等：重复执行同一输入不产生重复关系/事件。
"""
from __future__ import annotations

import time
from pathlib import Path

from . import cvesource
from . import state as state_mod
from .backfill import backfill
from .clean import clean_apply
from .ghsearch import Budget
from .recheck import recheck
from .render import render_all, verify_contract
from .repo_watch import discover
from .scan import scan

__all__ = ["daily"]

META_REFRESH_DAYS = 30  # 冲突仓库元数据缓存过期（墓碑重审需要新描述，R5/R11）


def daily(
    root: Path,
    client=None,
    scan_requests: int = 300,
    scan_minutes: float = 12.0,
    backfill_limit: int = 1500,
    backfill_minutes: float = 16.0,
    time_budget_minutes: float = 40.0,
) -> dict:
    if client is None:
        from .ghsearch import GitHubClient

        client = GitHubClient()

    started = time.monotonic()
    total_seconds = time_budget_minutes * 60 if time_budget_minutes is not None else None

    def remaining() -> float | None:
        if total_seconds is None:
            return None
        return max(total_seconds - (time.monotonic() - started), 0.0)

    def stage_seconds(stage_minutes: float) -> float | None:
        rem = remaining()
        if rem is None:
            return stage_minutes * 60
        return min(stage_minutes * 60, rem)

    steps: dict = {}

    rem = remaining()
    if rem is not None and rem <= 0:
        steps["skipped"] = "time budget exhausted before sync"
        summary = {"ts": state_mod.now_iso(), "ok": False, "steps": steps}
        state_mod.write_json(state_mod.state_dir(root) / "last_attempt.json", summary)
        raise SystemExit("整轮时间预算已耗尽，未开始任何阶段")

    try:
        steps["sync"] = cvesource.sync(client, root, budget=Budget(max_seconds=remaining()))
        steps["repo_watch"] = discover(client, root, budget=Budget(max_seconds=remaining()))

        scan_time = stage_seconds(scan_minutes)
        steps["scan"] = scan(
            client, root,
            limit_tasks=10000,
            budget_requests=scan_requests,
            budget_seconds=scan_time,
        )

        half = stage_seconds(backfill_minutes)
        steps["backfill_conflicts"] = backfill(
            client, root, limit=100000, priority_conflicts=True,
            budget_seconds=half,
            max_age_days=META_REFRESH_DAYS,
        )
        steps["backfill_queue"] = backfill(
            client, root, limit=backfill_limit,
            budget_seconds=stage_seconds(backfill_minutes),
        )

        steps["recheck"] = recheck(root)
        steps["clean_apply"] = clean_apply(root, strict=False)

        manifest = render_all(root)
        steps["render"] = {"changed_files": len(manifest["changed"])}

        verdict = verify_contract(root)
        steps["verify"] = verdict
    except SystemExit:
        raise
    except Exception as exc:  # 早期异常也要留痕（F8/评审补充）
        return _finish(root, steps, None, error=f"{type(exc).__name__}: {exc}")
    return _finish(root, steps, verdict)


def _finish(root: Path, steps: dict, verdict: dict | None, error: str | None = None) -> dict:
    summary = {
        "ts": state_mod.now_iso(),
        "ok": bool(verdict and verdict.get("ok")),
        "steps": steps,
        **({"error": error} if error else {}),
    }
    # R16/F8：尝试时间总是记录（含早期异常）；成功仅在 verify 通过后写
    state_mod.write_json(state_mod.state_dir(root) / "last_attempt.json", summary)
    if verdict is not None and verdict.get("ok"):
        state_mod.write_json(state_mod.state_dir(root) / "last_run.json", summary)
        return summary
    if verdict is not None:
        raise SystemExit(f"verify 失败，本轮不发布: {verdict['problems']}")
    raise SystemExit(f"daily 异常中断: {error}")

