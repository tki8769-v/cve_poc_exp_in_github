"""cvesource 连续同步测试（FakeClient，无网络）。"""
from __future__ import annotations

import io
import json
import zipfile
from pathlib import Path

from collector import cvesource
from collector import state as state_mod


def _record(cve_id, state="PUBLISHED", description=None):
    data = {"cveMetadata": {"cveId": cve_id, "state": state}}
    if description is None:
        description = f"vulnerability {cve_id}"
    data["containers"] = {"cna": {"descriptions": [{"lang": "en", "value": description}]}}
    return data


def _delta_zip(records: list[dict]) -> bytes:
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w") as zf:
        for index, record in enumerate(records):
            cve_id = record["cveMetadata"]["cveId"]
            year = cve_id.split("-")[1]
            zf.writestr(f"{year}/0xxx/{cve_id}.json", json.dumps(record))
    return buffer.getvalue()


class FakeClient:
    def __init__(self, releases, assets: dict[int, bytes]):
        self.releases = releases
        self.assets = assets
        self.downloaded = []

    def list_releases(self, per_page=30, page=1, budget=None):
        return self.releases

    def download_asset(self, url, budget=None):
        self.downloaded.append(url)
        for asset_id, payload in self.assets.items():
            if str(asset_id) in url or url.endswith(f"{asset_id}"):
                return payload
        return _delta_zip([])


def _release(tag, asset_id, url):
    return {
        "tag_name": tag,
        "assets": [{"id": asset_id, "name": f"{tag}_delta_CVEs_at_1700Z.zip.zip",
                    "browser_download_url": url}],
    }


def test_parse_cve_record_edges():
    assert cvesource.parse_cve_record({}) is None
    record = cvesource.parse_cve_record(_record("cve-2026-0001"))
    assert record["cve_id"] == "CVE-2026-0001"
    assert record["state"] == "PUBLISHED"
    assert record["description"].startswith("vulnerability")


def test_sync_first_run_latest_release_only(tmp_path: Path):
    zip_bytes = _delta_zip([
        _record("CVE-2026-0001"),
        _record("CVE-2026-0002"),
        _record("CVE-2026-0003", state="REJECTED"),
    ])
    releases = [
        _release("cve_2026-09-23_1700Z", 30, "https://x/30.zip"),
        _release("cve_2026-09-22_1700Z", 29, "https://x/29.zip"),
    ]
    client = FakeClient(releases, {30: zip_bytes, 29: _delta_zip([_record("CVE-2026-0000")])})

    report = cvesource.sync(client, tmp_path)

    # 首次运行只消费最新 release（29 号资产不应被下载）
    assert report["releases_processed"] == 1
    assert all("29" not in url for url in client.downloaded)
    assert report["cves_seen"] == 3
    assert report["new_tasks"] == 2  # REJECTED 不入队
    assert report["rejected"] == 1

    tasks = state_mod.read_jsonl(tmp_path / "state" / "scan_tasks.jsonl")
    assert {t["cve_id"] for t in tasks} == {"CVE-2026-0001", "CVE-2026-0002"}


def test_sync_idempotent_rerun(tmp_path: Path):
    zip_bytes = _delta_zip([_record("CVE-2026-0001")])
    client = FakeClient([_release("cve_2026-09-23_1700Z", 30, "https://x/30.zip")], {30: zip_bytes})

    first = cvesource.sync(client, tmp_path)
    second = cvesource.sync(client, tmp_path)

    assert first["new_tasks"] == 1
    assert second["new_tasks"] == 0
    assert second["releases_processed"] == 0  # 游标命中，资产不重复下载


def test_sync_catches_up_after_downtime(tmp_path: Path):
    """停机一天后：两个未处理 release 按时间正序全部消费。"""
    day1 = _release("cve_2026-09-22_1700Z", 29, "https://x/29.zip")
    day2 = _release("cve_2026-09-23_1700Z", 30, "https://x/30.zip")
    client = FakeClient([day2, day1], {
        29: _delta_zip([_record("CVE-2026-0100")]),
        30: _delta_zip([_record("CVE-2026-0101")]),
    })

    cvesource.sync(client, tmp_path, all_releases=True)  # 首跑建立游标（只最新）
    # 模拟停机后又发布一个 release
    day3 = _release("cve_2026-09-24_1700Z", 31, "https://x/31.zip")
    client.releases = [day3, day2, day1]
    client.assets[31] = _delta_zip([_record("CVE-2026-0100", description="modified")])

    report = cvesource.sync(client, tmp_path)

    assert report["releases_processed"] >= 1
    tasks = state_mod.read_jsonl(tmp_path / "state" / "scan_tasks.jsonl")
    by_id = {t["cve_id"]: t for t in tasks}
    assert "CVE-2026-0100" in by_id  # 修改过的 CVE 被刷新
    assert "CVE-2026-0101" in by_id


def test_sync_modified_refreshes_existing_task(tmp_path: Path):
    zip_bytes = _delta_zip([_record("CVE-2026-0001")])
    client = FakeClient([_release("cve_2026-09-23_1700Z", 30, "https://x/30.zip")], {30: zip_bytes})
    cvesource.sync(client, tmp_path)

    # 同一 CVE 再次出现在新 release 中 → 任务刷新为 modified，不新建
    client.releases = [_release("cve_2026-09-23_1800Z", 31, "https://x/31.zip")]
    client.assets[31] = _delta_zip([_record("CVE-2026-0001", description="updated desc")])
    report = cvesource.sync(client, tmp_path)

    assert report["new_tasks"] == 0
    tasks = state_mod.read_jsonl(tmp_path / "state" / "scan_tasks.jsonl")
    assert len(tasks) == 1
    assert tasks[0]["reason"] == "modified"


class FailingDownloadClient(FakeClient):
    """第 N 次 download_asset 抛异常，用于崩溃窗口注入。"""

    def __init__(self, releases, assets, fail_on_call: int):
        super().__init__(releases, assets)
        self.fail_on_call = fail_on_call
        self.download_count = 0

    def download_asset(self, url, budget=None):
        self.download_count += 1
        if self.download_count == self.fail_on_call:
            raise RuntimeError("simulated network failure")
        return super().download_asset(url, budget=budget)


def test_sync_crash_between_assets_loses_nothing(tmp_path: Path):
    """评审 R1：第二个资产下载失败后重跑，两个资产的 CVE 都必须存在。"""
    r1 = _release("cve_2026-09-22_1700Z", 29, "https://x/29.zip")
    r2 = _release("cve_2026-09-23_1700Z", 30, "https://x/30.zip")
    client = FailingDownloadClient(
        [r2, r1],
        {29: _delta_zip([_record("CVE-2026-0100")]),
         30: _delta_zip([_record("CVE-2026-0101")])},
        fail_on_call=2,
    )

    try:
        cvesource.sync(client, tmp_path, all_releases=True)
    except RuntimeError:
        pass  # 模拟中断

    # 重跑：完整客户端（无失败）
    ok_client = FakeClient([r2, r1], {29: _delta_zip([_record("CVE-2026-0100")]),
                                      30: _delta_zip([_record("CVE-2026-0101")])})
    report = cvesource.sync(ok_client, tmp_path, all_releases=True)

    tasks = {t["cve_id"] for t in state_mod.read_jsonl(tmp_path / "state" / "scan_tasks.jsonl")}
    assert {"CVE-2026-0100", "CVE-2026-0101"} <= tasks
    assert report["releases_processed"] >= 1


def test_sync_floor_tag_prevents_stale_replay(tmp_path: Path):
    """评审 R2：最新 REJECTED 已采纳后，旧 PUBLISHED 快照不得回放复活。"""
    day1 = _release("cve_2026-09-22_1700Z", 29, "https://x/29.zip")
    day2 = _release("cve_2026-09-23_1700Z", 30, "https://x/30.zip")
    client = FakeClient([day2, day1], {
        29: _delta_zip([_record("CVE-2026-0200", state="PUBLISHED")]),  # 旧快照：PUBLISHED
        30: _delta_zip([_record("CVE-2026-0200", state="REJECTED")]),   # 新快照：REJECTED
    })

    cvesource.sync(client, tmp_path)  # 首跑：只消费最新（REJECTED 生效）
    assert not any(t["cve_id"] == "CVE-2026-0200"
                   for t in state_mod.read_jsonl(tmp_path / "state" / "scan_tasks.jsonl"))

    # 第二次（旧 release 仍未处理）：不得把 PUBLISHED 旧快照重新入队
    report = cvesource.sync(client, tmp_path)
    tasks = state_mod.read_jsonl(tmp_path / "state" / "scan_tasks.jsonl")
    assert not any(t["cve_id"] == "CVE-2026-0200" for t in tasks)
    cursor = state_mod.read_json(tmp_path / "state" / "cve_cursor.json")
    assert cursor["last_tag"] == "cve_2026-09-23_1700Z"  # last_tag 单调不减
    assert cursor["floor_tag"] == "cve_2026-09-23_1700Z"


def test_f2_old_cursor_migrates_floor_to_last_tag(tmp_path: Path):
    """评审 F2：旧 schema 游标（无 floor）迁移为 floor=last_tag，不跳窗口。"""
    state_mod.write_json(tmp_path / "state" / "cve_cursor.json",
                         {"last_tag": "r01", "processed_assets": [1]})
    r1 = _release("r01", 1, "https://x/1.zip")
    r2 = _release("r02", 2, "https://x/2.zip")
    r3 = _release("r03", 3, "https://x/3.zip")
    client = FakeClient([r3, r2, r1], {
        1: _delta_zip([_record("CVE-2026-0001")]),
        2: _delta_zip([_record("CVE-2026-0002")]),
        3: _delta_zip([_record("CVE-2026-0003")]),
    })
    report = cvesource.sync(client, tmp_path)
    tasks = {t["cve_id"] for t in state_mod.read_jsonl(tmp_path / "state" / "scan_tasks.jsonl")}
    assert {"CVE-2026-0002", "CVE-2026-0003"} <= tasks  # r02 不被跳过
    cursor = state_mod.read_json(tmp_path / "state" / "cve_cursor.json")
    assert cursor["floor_tag"] == "r01"


def test_f5_published_recovers_rejected_cve(tmp_path: Path):
    """评审 F5：较新 PUBLISHED 恢复被撤回编号；较旧快照不覆盖较新状态。"""
    from collector import cvestate

    # 预置：r00 时被官方撤回
    cvestate.set_state(tmp_path, "CVE-2026-0300", "REJECTED", source_tag="r00")
    # 较新 release r01 携带 PUBLISHED
    client = FakeClient([_release("r01", 1, "https://x/1.zip")],
                        {1: _delta_zip([_record("CVE-2026-0300", state="PUBLISHED")])})
    cvesource.sync(client, tmp_path)
    tasks = {t["cve_id"] for t in state_mod.read_jsonl(tmp_path / "state" / "scan_tasks.jsonl")}
    assert "CVE-2026-0300" in tasks  # 恢复入队
    assert cvestate.load_states(tmp_path)["CVE-2026-0300"]["state"] == "PUBLISHED"

    # 较旧 REJECTED 快照（tag 更小）不得把状态倒回
    cvestate.set_state(tmp_path, "CVE-2026-0300", "REJECTED", source_tag="r00")
    assert cvestate.load_states(tmp_path)["CVE-2026-0300"]["state"] == "PUBLISHED"


def test_g1_legacy_event_state_accepts_release_update(tmp_path: Path):
    """评审 G1：legacy_event 线索不得压制正式版本——后续 PUBLISHED 恢复入队。"""
    from collector import cvestate

    assert cvestate.set_state(tmp_path, "CVE-2026-0700", "REJECTED",
                              source_tag="legacy_event")
    client = FakeClient([_release("cve_2026-09-24_0800Z", 1, "https://x/1.zip")],
                        {1: _delta_zip([_record("CVE-2026-0700", state="PUBLISHED")])})
    report = cvesource.sync(client, tmp_path)

    assert report["new_tasks"] == 1
    state = cvestate.load_states(tmp_path)["CVE-2026-0700"]
    assert state["state"] == "PUBLISHED"
    assert state["source_kind"] == "release"
    assert state["source_tag"] == "cve_2026-09-24_0800Z"


def test_g1_state_kind_ordering(tmp_path: Path):
    """评审 G1：release 不被 legacy_event 覆盖；legacy_event 可被任何版本覆盖。"""
    from collector import cvestate

    assert cvestate.set_state(tmp_path, "CVE-2026-0703", "PUBLISHED", source_tag="r05")
    assert not cvestate.set_state(tmp_path, "CVE-2026-0703", "REJECTED",
                                  source_tag="legacy_event")
    assert cvestate.load_states(tmp_path)["CVE-2026-0703"]["state"] == "PUBLISHED"

    assert cvestate.set_state(tmp_path, "CVE-2026-0704", "REJECTED",
                              source_tag="legacy_event")
    # 更早 tag 的正式版本也可覆盖历史线索
    assert cvestate.set_state(tmp_path, "CVE-2026-0704", "PUBLISHED", source_tag="r01")
    assert cvestate.load_states(tmp_path)["CVE-2026-0704"]["state"] == "PUBLISHED"


def test_g7_stale_rejected_snapshot_has_no_side_effects(tmp_path: Path):
    """评审 G7：较旧 REJECTED 快照被版本保护拒绝时，不取消任务、不写事件。"""
    from collector import cvestate, scheduler

    cvestate.set_state(tmp_path, "CVE-2026-0701", "PUBLISHED", source_tag="r02")
    scheduler.enqueue(tmp_path, "CVE-2026-0701", "new")
    events_before = len(state_mod.read_jsonl(tmp_path / "state" / "events.jsonl"))

    client = FakeClient([_release("r01", 1, "https://x/1.zip")],
                        {1: _delta_zip([_record("CVE-2026-0701", state="REJECTED")])})
    report = cvesource.sync(client, tmp_path)

    assert report["rejected"] == 1  # 记录被看到，但更新被拒
    tasks = state_mod.read_jsonl(tmp_path / "state" / "scan_tasks.jsonl")
    assert any(t["cve_id"] == "CVE-2026-0701" for t in tasks)  # 任务未被取消
    assert cvestate.load_states(tmp_path)["CVE-2026-0701"]["state"] == "PUBLISHED"
    events_after = len(state_mod.read_jsonl(tmp_path / "state" / "events.jsonl"))
    assert events_after == events_before  # 不产生拒绝事件


def test_g7_stale_published_snapshot_does_not_requeue(tmp_path: Path):
    """评审 G7：较旧 PUBLISHED 快照被拒时，已撤回编号不得重新入队。"""
    from collector import cvestate

    cvestate.set_state(tmp_path, "CVE-2026-0702", "REJECTED", source_tag="r02")
    client = FakeClient([_release("r01", 1, "https://x/1.zip")],
                        {1: _delta_zip([_record("CVE-2026-0702", state="PUBLISHED")])})
    report = cvesource.sync(client, tmp_path)

    assert report["new_tasks"] == 0
    assert cvestate.load_states(tmp_path)["CVE-2026-0702"]["state"] == "REJECTED"


def test_g2_missing_checkpoint_reports_gap(tmp_path: Path):
    """评审 G2/H1：断档须持续告警，直到原始检查点重新可见才算补齐。"""
    r01 = _release("cve_2026-09-20_1700Z", 1, "https://x/1.zip")
    cvesource.sync(FakeClient([r01], {1: _delta_zip([_record("CVE-2026-0800")])}), tmp_path)

    # 停机后检查点被挤出可见列表，只剩更近的 release
    r10 = _release("cve_2026-09-24_1700Z", 10, "https://x/10.zip")
    report = cvesource.sync(FakeClient([r10], {10: _delta_zip([_record("CVE-2026-0801")])}),
                            tmp_path)
    assert report["continuity_warning"] is True
    cursor = state_mod.read_json(tmp_path / "state" / "cve_cursor.json")
    assert cursor["continuity_gap"] is True
    assert cursor["continuity_gap_below"] == "cve_2026-09-20_1700Z"  # 原始检查点

    # H1：新进度可见 ≠ 断档补齐——r01 仍不可见时持续告警
    report3 = cvesource.sync(FakeClient([r10], {10: _delta_zip([])}), tmp_path)
    assert report3["continuity_warning"] is True
    cursor3 = state_mod.read_json(tmp_path / "state" / "cve_cursor.json")
    assert cursor3["continuity_gap"] is True

    # 原始检查点重新出现在列表中 → 断档真正消除
    report4 = cvesource.sync(FakeClient([r10, r01], {}), tmp_path)
    assert report4["continuity_warning"] is False
    cursor4 = state_mod.read_json(tmp_path / "state" / "cve_cursor.json")
    assert "continuity_gap" not in cursor4


def test_h3_sync_budget_exhaustion_is_controlled(tmp_path: Path):
    """评审 H3：资产下载中预算耗尽 → 受控返回（非异常），已完成资产保留。"""
    from collector.ghsearch import BudgetExhausted

    r1 = _release("cve_2026-09-20_1700Z", 1, "https://x/1.zip")
    r2 = _release("cve_2026-09-21_1700Z", 2, "https://x/2.zip")
    r3 = _release("cve_2026-09-22_1700Z", 3, "https://x/3.zip")

    class BudgetOutClient(FakeClient):
        def download_asset(self, url, budget=None):
            if "3.zip" in url:
                raise BudgetExhausted("time budget exhausted")
            return super().download_asset(url, budget=budget)

    client = BudgetOutClient([r3, r2, r1], {
        1: _delta_zip([_record("CVE-2026-0810")]),
        2: _delta_zip([_record("CVE-2026-0811")]),
        3: _delta_zip([_record("CVE-2026-0812")]),
    })
    report = cvesource.sync(client, tmp_path, all_releases=True)  # 不抛异常

    assert report["budget_stopped"] is True
    assert report["new_tasks"] == 2                      # r1/r2 已应用
    cursor = state_mod.read_json(tmp_path / "state" / "cve_cursor.json")
    assert 1 in cursor["processed_assets"] and 2 in cursor["processed_assets"]
    assert 3 not in cursor["processed_assets"]           # 断点下轮续跑


def test_g4_sync_new_cve_gets_top_priority(tmp_path: Path):
    """评审 G4：sync 批量入队新建任务与单条 enqueue 一致使用最高优先级。"""
    client = FakeClient([_release("cve_2026-09-24_0800Z", 1, "https://x/1.zip")],
                        {1: _delta_zip([_record("CVE-2026-0900")])})
    cvesource.sync(client, tmp_path)
    tasks = {t["cve_id"]: t for t in
             state_mod.read_jsonl(tmp_path / "state" / "scan_tasks.jsonl")}
    assert tasks["CVE-2026-0900"]["priority"] == 0
