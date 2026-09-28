"""cvelistV5 连续同步（REFACTOR_PLAN.md 3.6 / 评审 R1/R2/R3/R9 + F1/F2/F5）。

- F1：release 列表真分页（页码参数、去重、检查点即停、末页判定）；
  达到页数上限不算"追溯完整"，触发断档告警；
- F2：旧 schema 游标（有 last_tag 无 floor_tag）迁移为 floor=last_tag
  （保留既有成功边界，不截断历史）；若窗口内存在早于 floor 的未处理
  资产，floor 自动下调自愈（修复曾被错误抬高的边界）；
- F5：CVE 权威状态按源版本单调更新——REJECTED/PUBLISHED 均带 tag，
  较新 PUBLISHED 可恢复被撤回编号，较旧快照不得覆盖较新状态；
- 记录先应用、后提交游标（R1），入队批量化（评审 5.6 性能项）。
"""
from __future__ import annotations

import io
import json
import zipfile
from pathlib import Path

from . import cvestate
from . import scheduler
from . import state as state_mod
from .ghsearch import BudgetExhausted

__all__ = ["parse_cve_record", "extract_records", "delta_assets", "sync"]

CURSOR_FILE = "cve_cursor.json"
RELEASE_PAGE_SIZE = 30
MAX_RELEASE_PAGES = 10


def parse_cve_record(data: dict) -> dict | None:
    meta = data.get("cveMetadata") or {}
    cve_id = meta.get("cveId")
    if not cve_id:
        return None
    state = meta.get("state", "UNKNOWN")
    description = ""
    cna = (data.get("containers") or {}).get("cna") or {}
    for item in cna.get("descriptions") or []:
        if item.get("lang") == "en":
            description = item.get("value", "")
            break
    return {"cve_id": str(cve_id).upper(), "state": state, "description": description}


def extract_records(zip_bytes: bytes) -> dict[str, dict]:
    records: dict[str, dict] = {}
    with zipfile.ZipFile(io.BytesIO(zip_bytes)) as zf:
        for name in zf.namelist():
            if not name.endswith(".json") or "CVE-" not in name:
                continue
            try:
                data = json.loads(zf.read(name).decode("utf-8"))
            except (ValueError, UnicodeDecodeError):
                continue
            record = parse_cve_record(data)
            if record:
                records[record["cve_id"]] = record
    return records


def delta_assets(release: dict) -> list[dict]:
    out = []
    for asset in release.get("assets", []):
        name = str(asset.get("name", ""))
        if "delta" in name.lower():
            url = asset.get("browser_download_url") or ""
            asset_id = asset.get("id") or url
            if url:
                out.append({"id": asset_id, "url": url, "name": name})
    return out


def _load_cursor(root: Path) -> dict:
    cursor = state_mod.read_json(state_mod.state_dir(root) / CURSOR_FILE,
                                 default={"processed_assets": [], "last_tag": None,
                                          "floor_tag": None})
    # F2 迁移：旧 schema（有成功检查点、无 floor）→ floor 继承 last_tag
    if not cursor.get("floor_tag") and cursor.get("last_tag"):
        cursor["floor_tag"] = cursor["last_tag"]
    return cursor


def _save_cursor(root: Path, cursor: dict) -> None:
    state_mod.write_json(state_mod.state_dir(root) / CURSOR_FILE, cursor)


def _list_releases_paginated(client, budget=None, stop_tag: str | None = None):
    """按页追溯 release 列表（F1）。

    返回 (releases 最新在前, traced_complete)。traced_complete 仅在追溯到
    stop_tag（最近已应用检查点）、或无检查点要求（首跑）且列表读尽时为真；
    列表读尽仍未见检查点 = 存在断档，不得宣布连续（G2）。达到页数上限
    不算完整（存在缺口）；非列表响按上游结构异常处理（G2）。
    """
    releases: list[dict] = []
    seen_tags: set[str] = set()
    traced_complete = False
    for page in range(1, MAX_RELEASE_PAGES + 1):
        batch = client.list_releases(per_page=RELEASE_PAGE_SIZE, page=page, budget=budget)
        if not isinstance(batch, list):
            break  # 上游结构异常：按存在缺口处理
        releases.extend(r for r in batch if r.get("tag_name") not in seen_tags)
        seen_tags.update(r.get("tag_name") for r in batch)
        if stop_tag and stop_tag in seen_tags:
            traced_complete = True  # 追溯到最近已应用检查点
            break
        if not batch or len(batch) < RELEASE_PAGE_SIZE:
            traced_complete = stop_tag is None  # 读尽未见检查点 = 断档（G2）
            break
    return releases, traced_complete


def sync(client, root: Path, all_releases: bool = False, max_releases: int = 30,
         budget=None) -> dict:
    cursor = _load_cursor(root)
    processed: set = set(cursor.get("processed_assets") or [])
    floor_tag = cursor.get("floor_tag")
    last_tag = cursor.get("last_tag")

    # H3：预算耗尽是受控阶段停止（非整轮异常）——已应用资产的检查点已在
    # 游标中，由本轮后续渲染/验证/发布提交，避免 Actions 丢弃 runner 进度
    try:
        releases, traced_complete = _list_releases_paginated(client, budget=budget,
                                                             stop_tag=last_tag)
    except BudgetExhausted:
        return {"releases_seen": 0, "releases_processed": 0, "cves_seen": 0,
                "new_tasks": 0, "rejected": 0, "last_tag": last_tag,
                "floor_tag": floor_tag, "continuity_warning": False,
                "budget_stopped": True}

    # F1：连续性 = 能追溯到最近已应用检查点（而非 floor 是否可见）
    continuity_warning = bool(last_tag and not traced_complete)
    if not releases:
        return {"releases_seen": 0, "releases_processed": 0, "cves_seen": 0,
                "new_tasks": 0, "rejected": 0, "last_tag": last_tag,
                "floor_tag": floor_tag, "continuity_warning": continuity_warning,
                "budget_stopped": False}

    # G2/H1：断档持久化——记录断档前的原始检查点；只有该检查点重新可见
    # （断档真正补齐）才清除告警，"最近已见版本"的新进度不构成恢复
    gap_flag = bool(cursor.get("continuity_gap"))
    gap_below = cursor.get("continuity_gap_below")
    if continuity_warning and not gap_flag:
        cursor["continuity_gap"] = True
        cursor["continuity_gap_below"] = last_tag
        gap_flag = True
        _save_cursor(root, cursor)
    elif gap_flag and gap_below and gap_below in {r.get("tag_name") for r in releases}:
        cursor.pop("continuity_gap", None)
        cursor.pop("continuity_gap_below", None)
        gap_flag = False
        _save_cursor(root, cursor)
    report_gap = continuity_warning or gap_flag

    # R2/F2：无任何历史状态才允许确立新边界；默认取最新，历史回补取最旧
    if not floor_tag:
        boundary = releases[-1] if all_releases else releases[0]
        floor_tag = boundary.get("tag_name") or ""
        cursor["floor_tag"] = floor_tag
        _save_cursor(root, cursor)

    # F2 自愈：floor 超过最后成功检查点 = 曾被错误抬高 → 降回检查点重开窗口。
    # （正常状态恒有 floor <= last_tag；不应因"存在未处理的更旧 release"降界，
    #   否则会与 R2 的旧快照回放保护冲突。）
    if last_tag and floor_tag > last_tag:
        floor_tag = last_tag
        cursor["floor_tag"] = floor_tag
        _save_cursor(root, cursor)

    pending = [r for r in releases
               if (r.get("tag_name") or "") >= floor_tag
               and any(a["id"] not in processed for a in delta_assets(r))]
    if not all_releases and not last_tag:
        # 首次运行（非历史回补模式）：以最新 release 为连续性起点
        pending = [releases[0]]
    targets = list(reversed(pending))[:max_releases]  # 时间正序

    cves_seen: set[str] = set()
    rejected = 0
    new_tasks = 0
    processed_releases = 0
    budget_stopped = False
    task_index = {t["cve_id"] for t in scheduler.load_tasks(root)}

    for release in targets:
        tag = release.get("tag_name") or ""
        if tag < floor_tag:
            continue
        todo = [a for a in delta_assets(release) if a["id"] not in processed]
        if not todo:
            continue
        for asset in todo:
            try:
                zip_bytes = client.download_asset(asset["url"], budget=budget)
            except BudgetExhausted:
                # H3：受控停止——已完成资产的检查点已逐个落盘，本轮照常
                # 渲染/验证/发布以提交进度；未完成资产下轮从游标续跑
                budget_stopped = True
                break
            records = extract_records(zip_bytes)
            # R1：先应用记录（按资产批量提交任务），后提交游标——崩溃
            # 重跑最多重复应用（幂等），不会丢任务
            asset_items: list[dict] = []
            for cve_id, record in records.items():
                cves_seen.add(cve_id)
                if record["state"] == "REJECTED":
                    rejected += 1
                    # G7：仅当版本更新被接受才执行任务取消/事件副作用；
                    # 被较新版本压下的旧快照不得产生任何副作用
                    if cvestate.set_state(root, cve_id, "REJECTED", source_tag=tag):
                        scheduler.cancel(root, cve_id)
                        state_mod.append_jsonl(state_mod.state_dir(root) / "events.jsonl", [
                            {"ts": state_mod.now_iso(), "type": "cve_rejected", "cve_id": cve_id}
                        ])
                    continue
                if cvestate.set_state(root, cve_id, record["state"], source_tag=tag):
                    asset_items.append({
                        "cve_id": cve_id,
                        "reason": "modified" if cve_id in task_index else "new",
                        "description": record["description"][:4000],
                    })
            if asset_items:
                new_tasks += scheduler.enqueue_many(root, asset_items)
                task_index.update(item["cve_id"] for item in asset_items)
            processed.add(asset["id"])
            cursor["processed_assets"] = sorted(processed)
            if tag >= (cursor.get("last_tag") or ""):
                cursor["last_tag"] = tag  # R2：单调不减
            _save_cursor(root, cursor)
        if budget_stopped:
            break
        processed_releases += 1

    return {
        "releases_seen": len(releases),
        "releases_processed": processed_releases,
        "cves_seen": len(cves_seen),
        "new_tasks": new_tasks,
        "rejected": rejected,
        "last_tag": cursor.get("last_tag"),
        "floor_tag": floor_tag,
        "continuity_warning": report_gap,
        "budget_stopped": budget_stopped,
    }


def _known(root: Path, cve_id: str, cache: list[dict] | None = None) -> bool:
    tasks = cache if cache is not None else scheduler.load_tasks(root)
    return any(t["cve_id"] == cve_id for t in tasks)
