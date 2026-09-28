"""批量克隆 PocOrExp.md 收录的仓库（独立工具，不属于 collector 管线）。

P0 改造（REFACTOR_PLAN.md 3.2 / REFACTOR_REVIEW §5.7）：
  - git 调用改为 subprocess 列表参数 + cwd + 返回码检查 + URL 校验；
  - 解析器过滤空行（与 today.py 一致），描述不再被空串覆盖；
  - 读取本地 PocOrExp.md，不再自动 clone 上游仓库。
"""
from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import urlparse

try:
    from tqdm import tqdm
except ImportError:  # 进度条可选

    def tqdm(iterable, **kwargs):
        return iterable


BASE_DIR = Path(__file__).resolve().parent
REPO_ROOT = BASE_DIR / "repo"

# GitHub 标识符实际规则（评审 F14：仓库名可连字符开头/结尾，≤100 字符）
_OWNER_RE = re.compile(r"^[A-Za-z0-9](?:[A-Za-z0-9-]{0,38}[A-Za-z0-9])?$")
_REPO_RE = re.compile(r"^[A-Za-z0-9._-]{1,100}$")


def parse_readme(content):
    poc_or_exps = {}
    cve_ids = []
    cve_id = ""
    for line in content:
        line = line.rstrip("\n")
        if not line.strip():
            continue
        if line.startswith("## CVE"):
            cve_id = "CVE" + line.split("CVE")[-1]
            cve_ids.append(cve_id)
            poc_or_exps[cve_id] = {"CVE_ID": cve_id, "CVE_DESCRIPTION": "", "URL": []}
        elif line.startswith("- ["):
            url = line.split("[")[1].split("]")[0]
            poc_or_exps[cve_id]["URL"].append(url)
        elif line.startswith("##"):
            continue
        else:
            poc_or_exps[cve_id]["CVE_DESCRIPTION"] = line
    return poc_or_exps, cve_ids


def _validate_url(url: str) -> bool:
    try:
        parsed = urlparse(url)
    except ValueError:
        return False
    if parsed.scheme != "https" or parsed.netloc != "github.com":
        return False
    parts = [p for p in parsed.path.split("/") if p]
    if len(parts) < 2:
        return False
    owner, repo = parts[0], parts[1]
    if repo in (".", "..") or "/" in repo or "\\" in repo:
        return False
    return bool(_OWNER_RE.match(owner) and _REPO_RE.match(repo))


def _run_git(args, cwd: Path) -> bool:
    proc = subprocess.run(["git", *args], cwd=str(cwd))
    if proc.returncode != 0:
        print(f"[WARN] git {' '.join(args)} 失败 (rc={proc.returncode})", file=sys.stderr)
        return False
    return True


def clone_repos(urls):
    for url in tqdm(sorted(set(urls)), desc="cloning"):
        if not _validate_url(url):
            print(f"[WARN] 跳过非法 URL: {url}", file=sys.stderr)
            continue
        parts = [p for p in urlparse(url).path.split("/") if p]
        author, name = parts[0], parts[1]
        author_path = REPO_ROOT / author
        author_path.mkdir(parents=True, exist_ok=True)
        repo_path = author_path / name
        # 路径包含校验（R15）：目标必须落在 repo/ 之内
        if not repo_path.resolve().is_relative_to(REPO_ROOT.resolve()):
            print(f"[WARN] 路径越界，跳过: {url}", file=sys.stderr)
            continue
        if repo_path.exists():
            _run_git(["pull", "--ff-only"], repo_path)
        else:
            _run_git(["clone", "--", url], author_path)


def main():
    REPO_ROOT.mkdir(parents=True, exist_ok=True)
    source = BASE_DIR / "PocOrExp.md"
    content = source.read_text(encoding="utf-8").split("\n")
    content = [line for line in content if line.strip() != ""]
    poc_or_exps, cve_ids = parse_readme(content)
    urls = []
    for cve_id in cve_ids:
        urls += poc_or_exps[cve_id]["URL"]
    (BASE_DIR / "urls").write_text("\n".join(urls), encoding="utf-8")
    clone_repos(urls)


if __name__ == "__main__":
    main()
