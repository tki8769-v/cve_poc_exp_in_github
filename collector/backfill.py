"""仓库元数据回补（REFACTOR_PLAN.md 3.3/3.6 / 评审 4.1）。

bootstrap 登记的缺失元数据按预算逐批拉取，不编造数值：
- --priority-conflicts 优先回补冲突候选涉及的仓库（反证复核最急需）；
- 已回补的仓库不再重复请求（幂等续跑）；
- 404/仓库消失记为 error=gone 并缓存，避免反复探测。
"""
from __future__ import annotations

from pathlib import Path

from . import state as state_mod
from .ghsearch import Budget
from .parse import parse_github_repo

__all__ = ["load_meta", "backfill"]

META_FILE = "repo_meta.jsonl"


def _meta_path(root: Path) -> Path:
    return state_mod.state_dir(root) / META_FILE


def load_meta(root: Path) -> dict[tuple[str, str], dict]:
    meta: dict[tuple[str, str], dict] = {}
    for record in state_mod.read_jsonl(_meta_path(root)):
        meta[(record["owner"], record["repo"])] = record  # 后行覆盖前行
    return meta


def _conflict_repos(root: Path) -> list[tuple[str, str]]:
    """优先刷新队列（评审 F10）：待复核候选 + 自动墓碑 + needs_review 关系。

    与"本轮待清洗候选"分开——墓碑必须持续刷新元数据，否则新证据永远
    读不到（TTL 恢复流程的前提）。
    """
    sdir = state_mod.state_dir(root)
    keys: list[tuple[str, str]] = []
    seen: set[tuple[str, str]] = set()

    def add_url(url: str) -> None:
        owner, repo = parse_github_repo(url)
        if owner and repo and (owner, repo) not in seen:
            seen.add((owner, repo))
            keys.append((owner, repo))

    for conflict in state_mod.read_jsonl(sdir / "clean_dryrun" / "conflicts.jsonl"):
        add_url(conflict.get("url", ""))
    for directory in ("relations", "relations_search"):
        for shard in sorted((sdir / directory).glob("*.jsonl")):
            for record in state_mod.read_jsonl(shard):
                needs_refresh = (
                    (record.get("verification") == "rejected" and record.get("auto", True))
                    or record.get("verification") == "needs_review"
                )
                if needs_refresh:
                    add_url(record.get("url", ""))
    return keys


def _queue_repos(root: Path) -> list[tuple[str, str]]:
    queue = state_mod.read_json(state_mod.state_dir(root) / "meta_backfill_queue.json", default=[])
    return [(item["owner"], item["repo"]) for item in queue if item.get("owner") and item.get("repo")]


def backfill(client, root: Path, limit: int = 100, priority_conflicts: bool = False,
             budget_seconds: float | None = None, max_age_days: float | None = None) -> dict:
    """回补仓库元数据。max_age_days：缓存过期重取（墓碑重审需要新描述）。"""
    meta = load_meta(root)
    order = _conflict_repos(root) if priority_conflicts else _queue_repos(root)
    now = state_mod.now_iso()
    if max_age_days is None:
        targets = [(o, r) for o, r in order if (o, r) not in meta][: max(limit, 0)]
    else:
        cutoff = _shift_days(-max_age_days)
        targets = [
            (o, r) for o, r in order
            if (o, r) not in meta or meta[(o, r)].get("fetched_at", "") < cutoff
        ][: max(limit, 0)]

    budget = Budget(max_seconds=budget_seconds) if budget_seconds is not None else None
    fetched: list[dict] = []
    stop_reason = None

    for owner, repo in targets:
        try:
            info = client.get_repo(owner, repo, budget=budget)
        except Exception as exc:  # 预算/网络中断：保留进度，下次续跑
            stop_reason = f"{type(exc).__name__}: {exc}"
            break
        record = {
            "owner": owner,
            "repo": repo,
            "fetched_at": state_mod.now_iso(),
        }
        if info is None:
            record["error"] = "gone"
        else:
            record.update(
                {
                    "repo_id": info.get("id"),
                    "description": info.get("description") or "",
                    "stars": info.get("stargazers_count"),
                    "forks": info.get("forks_count"),
                    "updated_at": info.get("updated_at"),
                    "pushed_at": info.get("pushed_at"),
                    "archived": info.get("archived"),
                    "default_branch": info.get("default_branch"),
                }
            )
        fetched.append(record)

    if fetched:
        state_mod.append_jsonl(_meta_path(root), fetched)

    return {
        "requested": len(targets),
        "fetched": len(fetched),
        "cached_total": len(meta) + len(fetched),
        "stop_reason": stop_reason,
    }


def _shift_days(days: float) -> str:
    from datetime import datetime, timedelta, timezone

    moment = datetime.now(timezone.utc) + timedelta(days=days)
    return moment.strftime("%Y-%m-%dT%H:%M:%SZ")
