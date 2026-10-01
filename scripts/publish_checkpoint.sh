#!/bin/bash
# 提交并推送采集检查点（供采集周期之间与最终发布共用）。
# 注意：提交消息不得携带 [skip ci] 等跳过标记——GitHub 会对默认分支
# HEAD 应用跳过标记并连带压制 schedule 触发（2026-09-28 事故）。
set -e

git config user.name "collector-bot"
git config user.email "collector-bot@users.noreply.github.com"

# 显式发布清单（评审 R16）：数据产物 + 状态 + 代码/测试变更
git add -A -- state PocOrExp.md Today.md '*/README.md' \
  collector tests scripts check_data.py requirements.txt README.md \
  TOKENS.example .gitignore download.py conftest.py .github

if git diff --cached --quiet; then
  echo "No changes to publish."
  exit 0
fi

git commit -m "Auto collect $(date -u +%Y-%m-%dT%H:%M:%SZ)"
for attempt in 1 2 3; do
  if git push; then exit 0; fi
  echo "push 失败（第 ${attempt} 次），rebase 后重验再推送..."
  git pull --rebase origin "${GITHUB_REF_NAME}" || { echo "rebase 冲突，人工介入"; exit 1; }
  python -m collector verify || { echo "rebase 后快照验证失败，人工介入"; exit 1; }
done
echo "push 重试耗尽"; exit 1
