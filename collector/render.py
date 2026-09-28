"""统一渲染与一致发布（REFACTOR_PLAN.md 3.7 / 评审 4.7）。

兼容承诺对象是年份 README 的 Markdown 契约（真实下游只解析
'## CVE-...' 标题与 '- [github-url](github-url)' 链接行）：
- 段落按 CVE 序号降序、链接行带 shields 徽章，沿用原格式；
- 既有段落的描述与链接顺序原样保留（首次渲染对未变更年份零扰动），
  新关系按 stars 降序追加；rejected 关系不再渲染（墓碑保留在 state）；
- Today.md 由事件派生（当天 UTC 的 new_poc 去重汇总），重跑幂等；
  未接管前（无当日事件且从未由本管线写出）不覆盖上游遗留内容；
- 全部产物走原子写（同目录 tmp + os.replace、显式 UTF-8），内容未变
  不重写；发布清单记录本次产物与统计（内部状态不嵌入公开产物）。
"""
from __future__ import annotations

import html
import re
from pathlib import Path

from . import RULES_VERSION
from . import scheduler
from . import state as state_mod
from .parse import README_HEADING_RE, README_LINK_RE, parse_github_repo

__all__ = ["load_active_relations", "render_all", "verify_contract"]

YEAR_DIR_RE = re.compile(r"^[12]\d{3}$")
MANIFEST_FILE = "publish_manifest.json"


# ---------------------------------------------------------------- 读取现状

def _read_sections(readme: Path) -> dict:
    """解析现有年份 README：{cve: {"description": [行], "urls": [保序]}}。"""
    sections: dict[str, dict] = {}
    if not readme.exists():
        return sections
    current: str | None = None
    with open(readme, "r", encoding="utf-8") as fh:
        for raw in fh:
            line = raw.rstrip("\n")
            heading = README_HEADING_RE.match(line)
            if heading:
                current = heading.group(1).upper()
                sections.setdefault(current, {"description": [], "urls": [], "gap": 1})
                continue
            if line.startswith("## "):
                current = None
                continue
            link = README_LINK_RE.match(line)
            if current is None:
                continue
            section = sections[current]
            if link:
                url = link.group(1).strip()
                if not section["urls"]:
                    # 首个链接前：截断描述尾部空行并记录原始间隔（逐字节保真）
                    desc = section["description"]
                    gap = 0
                    while desc and not desc[-1].strip():
                        desc.pop()
                        gap += 1
                    section["gap"] = gap
                if url not in section["urls"]:
                    section["urls"].append(url)
            elif not section["urls"]:
                # 链接开始前的行（含空行）都属于描述块
                section["description"].append(line)
    return sections


def load_active_relations(root: Path) -> dict[str, dict[str, dict]]:
    """{cve_id: {url: 关系记录}}：legacy 与 search 分片合并，剔除 rejected。

    同键时 search 记录后读覆盖（元数据更全）；来源字段保留各自值，
    支持按来源回滚（评审 4.6）。CVE 级官方 REJECTED 的编号整体不计入
    有效视图（评审 F5：渲染/验证/Today 使用同一视图）。
    """
    from . import cvestate

    merged: dict[str, dict[str, dict]] = {}
    rejected_cves = {c for c, r in cvestate.load_states(root).items()
                     if r.get("state") == "REJECTED"}

    def absorb(directory: str) -> None:
        for shard in sorted((state_mod.state_dir(root) / directory).glob("*.jsonl")):
            for record in state_mod.read_jsonl(shard):
                if record.get("verification") == "rejected":
                    continue
                if record["cve_id"] in rejected_cves:
                    continue
                merged.setdefault(record["cve_id"], {})[record["url"]] = record

    absorb("relations")         # legacy 先读
    absorb("relations_search")  # search 覆盖同键
    return merged


def _task_descriptions(root: Path) -> dict[str, str]:
    return {t["cve_id"]: t.get("description", "") for t in scheduler.load_tasks(root)}


# ---------------------------------------------------------------- 构建内容

def _link_line(url: str, record: dict) -> str:
    owner = record.get("owner")
    repo = record.get("repo")
    if not (owner and repo):
        owner, repo = parse_github_repo(url)
    if owner and repo:
        stars = f"![starts](https://img.shields.io/github/stars/{owner}/{repo}.svg)"
        forks = f"![forks](https://img.shields.io/github/forks/{owner}/{repo}.svg)"
        return f"- [{url}]({url}) : {stars} {forks}"
    return f"- [{url}]({url})"


def _ordered_urls(cve_id: str, sections: dict, rel_map: dict[str, dict]) -> list[str]:
    """既有链接保持文件原顺序，新链接按 stars 降序追加。"""
    old_order = sections.get(cve_id, {}).get("urls", [])
    active = [u for u in old_order if u in rel_map]
    seen = set(active)
    fresh = sorted(
        (u for u in rel_map if u not in seen),
        key=lambda u: (-(rel_map[u].get("stars") or 0), u),
    )
    return active + fresh


def _description_lines(cve_id: str, sections: dict, task_desc: str) -> list[str]:
    existing = sections.get(cve_id, {}).get("description", [])
    if existing:
        return existing
    text = (task_desc or "").strip()[:500]  # 展示摘要（全文存任务，R16）
    return [f"> {html.escape(text)}"] if text else []


def build_year_lines(year_cves: list[str], merged: dict, sections: dict, tasks: dict) -> list[str]:
    lines: list[str] = []
    ordered = sorted(
        year_cves,
        key=lambda c: (-int(c.split("-")[2]), c),
    )
    for cve_id in ordered:
        rel_map = merged[cve_id]
        urls = _ordered_urls(cve_id, sections, rel_map)
        if not urls:
            continue
        lines.append(f"## {cve_id}")
        lines.extend(_description_lines(cve_id, sections, tasks.get(cve_id, "")))
        existing_gap = sections.get(cve_id, {}).get("gap", 1)
        lines.extend([""] * existing_gap)
        for index, url in enumerate(urls):
            lines.append(_link_line(url, rel_map[url]))
            if index != len(urls) - 1:
                lines.append("")  # 与原格式一致：链接之间保留空行
        lines.append("")
    while lines and lines[-1] == "":
        lines.pop()
    return lines


def _today_event_sections(root: Path, merged: dict[str, dict[str, dict]]) -> dict[str, list[str]]:
    """当日新增（F11）：从关系的 first_seen_at 权威派生，而非事件日志。

    事件日志仅作审计流水；有效关系视图（剔除 rejected/官方撤回）保证
    Today 不会展示已失活的链接，且关系与"事件"不可能再分叉。
    """
    today = state_mod.now_iso()[:10]
    per_cve: dict[str, list[str]] = {}
    for cve_id, rel_map in merged.items():
        for url, record in rel_map.items():
            if str(record.get("first_seen_at", "")).startswith(today):
                per_cve.setdefault(cve_id, []).append(url)
    return {cve: sorted(set(urls)) for cve, urls in sorted(per_cve.items())}


def _build_today(root: Path, merged: dict, tasks: dict) -> str:
    today = state_mod.now_iso()[:10]
    events = _today_event_sections(root, merged)
    if not events:
        return f"# Update {today}\nNo Update Today!\n"
    lines = [f"# Update {today}"]
    for cve_id, urls in events.items():
        lines.append(f"## {cve_id}")
        desc = _description_lines(cve_id, {}, tasks.get(cve_id, ""))
        lines.extend(desc)
        lines.append("")
        for url in urls:
            record = merged.get(cve_id, {}).get(url, {})
            lines.append(_link_line(url, record))
        lines.append("")
    while lines and lines[-1] == "":
        lines.pop()
    return "\n".join(lines) + "\n"


# ---------------------------------------------------------------- 发布

def _write_if_changed(path: Path, text: str, changed: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and path.read_text(encoding="utf-8") == text:
        return
    state_mod.atomic_write_text(path, text)
    changed.append(str(path))


def render_all(root: Path, write: bool = True) -> dict:
    merged = load_active_relations(root)
    tasks = _task_descriptions(root)
    years = sorted({cve.split("-")[1] for cve in merged}, reverse=True)
    changed: list[str] = []
    stats = {"years": len(years), "sections": 0, "relations": 0}

    year_texts: dict[str, str] = {}
    for year in years:
        year_cves = [c for c in merged if c.split("-")[1] == year]
        sections = _read_sections(root / year / "README.md")
        lines = build_year_lines(year_cves, merged, sections, tasks)
        stats["sections"] += sum(1 for line in lines if line.startswith("## CVE-"))
        stats["relations"] += sum(1 for c in year_cves for _ in merged[c])
        year_texts[year] = "\n".join(lines) + "\n"
        if write:
            _write_if_changed(root / year / "README.md", year_texts[year], changed)

    if write:
        # R8：活跃关系清零的年份清理遗留 README（防止已拒绝关联继续暴露）
        active_years = set(years)
        for year_dir in _existing_year_dirs(root):
            if year_dir.name in active_years:
                continue
            readme = year_dir / "README.md"
            if readme.exists():
                readme.unlink()
                changed.append(str(readme))
            try:
                year_dir.rmdir()
            except OSError:
                pass
        aggregate = "\n".join(f"## {year}\n{year_texts[year]}" for year in years)
        _write_if_changed(root / "PocOrExp.md", aggregate, changed)

    # Today.md：仅当日有事件，或清单表明已由本管线接管时写出
    manifest_path = state_mod.state_dir(root) / MANIFEST_FILE
    manifest = state_mod.read_json(manifest_path, default={}) or {}
    today_owned = bool(manifest.get("today_owned"))
    events = _today_event_sections(root, merged)
    if write and (events or today_owned):
        _write_if_changed(root / "Today.md", _build_today(root, merged, tasks), changed)
        today_owned = True

    manifest_out = {
        "ts": state_mod.now_iso(),
        "rule_version": RULES_VERSION,
        **stats,
        "today_owned": today_owned,
        "changed": changed,
    }
    if write:
        state_mod.write_json(manifest_path, manifest_out)
    return manifest_out


# ---------------------------------------------------------------- 契约验证

def _try_downstream(root: Path):
    """真实下游解析函数优先（评审 R16）；缺失时退回 vendored 兼容实现。"""
    service = root.parent / "service" / "poc_source_pocorexp.py"
    if service.exists():
        import sys

        sys.path.insert(0, str(root.parent))
        try:
            from service.poc_source_pocorexp import parse_poc_markdown_files

            return parse_poc_markdown_files, "real"
        except Exception:
            pass
    from .compat import vendored_parse_markdown_files

    return vendored_parse_markdown_files, "vendored"


def _existing_year_dirs(root: Path) -> list[Path]:
    return sorted(
        (p for p in root.iterdir() if p.is_dir() and YEAR_DIR_RE.match(p.name)),
        key=lambda p: p.name,
    )


def verify_contract(root: Path) -> dict:
    """校验**真实发布产物**（评审 R8）：磁盘上的年份 README、PocOrExp.md、Today.md。

    - 每个磁盘上年份 README 表达的关系集合必须等于该年份的活跃关系集合；
      活跃关系为空的年份不允许残留旧 README；
    - PocOrExp.md 的解析集合必须等于全部活跃关系；
    - 已接管的 Today.md 必须精确反映当日 new_poc 事件（去重）；
    - 用真实（或 vendored）下游解析函数复核同一批文件。
    """
    from .parse import parse_readme_file

    merged = load_active_relations(root)
    expected = {cve: set(urls) for cve, urls in merged.items() if urls}
    problems: list[str] = []

    active_years = {c.split("-")[1] for c in expected}
    rendered: dict[str, set[str]] = {}

    for year_dir in _existing_year_dirs(root):
        readme = year_dir / "README.md"
        if not readme.exists():
            continue
        year = year_dir.name
        parsed: dict[str, set[str]] = {}
        for rel in parse_readme_file(readme):
            parsed.setdefault(rel.cve_id, set()).add(rel.url)
        if not parsed and year not in active_years:
            problems.append(f"{year}: 存在无活跃关系的遗留 README，应清理")
            continue
        rendered.update(parsed)

    missing_years = active_years - {d.name for d in _existing_year_dirs(root) if (d / "README.md").exists()}
    if missing_years:
        problems.append(f"活跃年份缺少年份 README: {sorted(missing_years)}")

    if rendered != expected:
        only_rendered = {c: rendered[c] for c in rendered if rendered[c] != expected.get(c)}
        only_expected = {c: expected[c] for c in expected if rendered.get(c) != expected[c]}
        problems.append(f"年份 README 集合与活跃关系不一致: "
                        f"多出/不符 {len(only_rendered)}, 缺失/不符 {len(only_expected)}")

    aggregate_path = root / "PocOrExp.md"
    if expected and not aggregate_path.exists():
        problems.append("PocOrExp.md 缺失（存在活跃关系时为必需产物）")
    if aggregate_path.exists():
        aggregate_map: dict[str, set[str]] = {}
        current = None
        for line in aggregate_path.read_text(encoding="utf-8").split("\n"):
            heading = README_HEADING_RE.match(line)
            if heading:
                current = heading.group(1).upper()
                continue
            if line.startswith("## "):
                current = None
                continue
            link = README_LINK_RE.match(line)
            if current and link:
                aggregate_map.setdefault(current, set()).add(link.group(1).strip())
        if aggregate_map != expected:
            problems.append("PocOrExp.md 解析集合与活跃关系不一致")

    manifest = state_mod.read_json(state_mod.state_dir(root) / MANIFEST_FILE, default={}) or {}
    if manifest.get("today_owned") or _today_event_sections(root, merged):
        today_path = root / "Today.md"
        if not today_path.exists():
            # 缺文件记入结构化问题并继续校验其余产物，不抛异常（评审 3 次要项）
            problems.append("已接管/应发布的 Today.md 缺失")
        else:
            today_events = _today_event_sections(root, merged)
            today_map = {c: set(urls) for c, urls in today_events.items()}
            today_parsed: dict[str, set[str]] = {}
            current = None
            for line in today_path.read_text(encoding="utf-8").split("\n"):
                heading = README_HEADING_RE.match(line)
                if heading:
                    current = heading.group(1).upper()
                    continue
                if line.startswith("## "):
                    current = None
                    continue
                link = README_LINK_RE.match(line)
                if current and link:
                    today_parsed.setdefault(current, set()).add(link.group(1).strip())
            if today_parsed != today_map:
                problems.append("Today.md 与当日 new_poc 事件不一致")

    downstream, downstream_kind = _try_downstream(root)
    downstream_checked = False
    if downstream is not None:
        try:
            raw = downstream(str(root))
            parsed_downstream = {cve: set(urls) for cve, urls in raw.items()}
            # 下游遍历根目录会命中项目 README（无 CVE 段落，不产生条目）
            if parsed_downstream != expected:
                problems.append(f"下游解析（{downstream_kind}）结果与活跃关系不一致")
            downstream_checked = True
        except Exception as exc:
            problems.append(f"下游解析函数执行失败: {exc}")

    return {
        "ok": not problems,
        "problems": problems,
        "downstream_checked": downstream_checked,
        "downstream_kind": downstream_kind,
    }
