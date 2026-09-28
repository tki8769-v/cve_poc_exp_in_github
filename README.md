# PocOrExp in Github（collector 版）

聚合 GitHub 上公开的 CVE PoC / EXP 仓库，按年份组织成 Markdown 索引，全自动采集、清洗与发布。

- 数据产出：`<年份>/README.md`、汇总 `PocOrExp.md`、每日新增 `Today.md`
- 采集来源：CVEProject/cvelistV5（CVE 清单）+ GitHub Search API（PoC 发现）
- 运行方式：本地单命令，或 GitHub Actions 免服务器定时运行

## 为什么有这个版本

原方案直接把搜索 `"CVE-2020-1234"` 的结果挂到 CVE-2020-1234 名下，而 GitHub 仓库搜索是**子串匹配**——`CVE-2020-12345`、甚至 description 里顺带提到该编号的无关仓库都会混进来（历史数据实测约 3.6% 的链接归属存疑）。

本版本在采集与清洗两端都做了**精确归属校验**：

- 每条 CVE—仓库 关联按三态判定：`accepted`（URL/描述精确含该编号，多 CVE 仓库保留）、
  `rejected`（URL 与仓库描述证据均不利，落墓碑记录可回滚）、`needs_review`（证据不足待补）；
- 每个判定记录证据、原因代码与规则版本，可追溯、可复核；
- 搜索结果在采集期即拦截冲突仓库，历史脏数据由反证复核流程增量清洗。

## 快速开始（本地）

```bash
pip install -r requirements.txt          # 仅需 requests（pytest 为开发依赖）
export GH_TOKEN=ghp_xxx                  # classic PAT，无需任何 scope

python -m collector bootstrap            # 首次：从年份 README 引导历史关系到 state/
python -m collector clean                # 冲突候选 dry-run 清单（不修改数据）
python -m collector daily                # 一轮完整编排（见下）
```

## 命令一览

| 命令 | 作用 |
|---|---|
| `python -m collector sync` | 拉取 cvelistV5 增量（新增/修改/REJECTED），入扫描队列 |
| `python -m collector discover` | 仓库侧增量发现：最近新建且含 CVE 字样的仓库，反查归属（时效通道） |
| `python -m collector scan --limit-tasks 50 --budget-requests 100` | 预算内扫描到期 CVE：搜索 + 三态过滤 + 合并关系 |
| `python -m collector backfill --priority-conflicts --limit 500` | 回补仓库元数据（冲突候选仓库优先，幂等续跑） |
| `python -m collector recheck` | 用回补的仓库描述对冲突候选做反证复核（纯本地） |
| `python -m collector clean` / `clean --apply` | 冲突清单 dry-run / 应用证据完备项并重渲染 |
| `python -m collector render` | 渲染年份 README、PocOrExp.md、Today.md（原子写，未变不写） |
| `python -m collector verify` | 契约验证：渲染集合 == 活跃关系集合 |
| `python -m collector daily` | 单命令编排：sync→scan→backfill→recheck→apply→render→verify |
| `python -m collector check` / `check_data.py` | 固定口径审计扫描（含基线漂移对比） |

## GitHub Actions 自动运行

`.github/workflows/collect.yml` 每 6 小时（错峰 :17 分）执行一轮 `daily`，变更自动提交：

1. fork/推送本仓库后，在 Actions 页启用，并确认
   Settings → Actions → General → Workflow permissions 为 **Read and write**；
2. 默认使用内置 `GITHUB_TOKEN`（搜索 30 次/分钟）；如需更高吞吐可添加 `GH_TOKEN` secret；
3. `state/` 目录随仓库提交，是跨运行的持久化检查点（任务队列、游标、证据、墓碑）；
4. `state/last_run.json` 记录最后成功执行时间与各步骤统计，用于监控与补跑
   （GitHub 定时任务可能延迟或丢弃；公开仓库 60 天无活动 Actions 会自动停用）；
5. 手动触发可选 `daily / backfill / clean` 三种模式。

## 调度与配额策略

双通道发现：

- **仓库侧增量（时效通道）**：检索最近新建、名称/描述含 CVE 字样的仓库
  （`created:` 日期窗口），反查编号精确归属——任何年份的 CVE 冒出新 PoC
  仓库，下一轮巡检即命中，与 CVE 年龄无关；游标按日推进，处理不完整
  自动重试，窗口重叠幂等；
- **CVE 侧调度（对账通道）**：新发布/被修改的 CVE 即时入队扫描；
  有发现的每 7 天重扫，无发现的 1→2→4→…→90 天指数退避——覆盖
  "发布当天零 PoC、数日后出首个 PoC"的场景并周期对账。

其余保证：

- **可恢复**：搜索不完整（预算耗尽/截断）不清任务、不清数据，短暂延后续跑；
  停机跨日由 cvelistV5 游标自动补洞；
- **预算**：单 token 即可运行（搜索 30 次/分钟、REST 5000 次/小时），
  客户端按限流响应头主动等待，401/403/429/5xx 分类处理。

## 目录结构

```
collector/          # 采集管线（parse/attrib/ghsearch/cvesource/scheduler/backfill/recheck/scan/render/pipeline）
tests/              # 单元与契约测试（pytest）
state/              # 运行状态：关系分片、任务队列、游标、元数据缓存、墓碑与证据
check_data.py       # 审计扫描入口
<年份>/README.md     # 数据产出（1999–今）
```

## 数据质量口径

`python check_data.py` 输出固定口径的审计统计（规则版本化，含与历史基线的漂移对比）：

- 冲突候选：URL 含 CVE 编号但集合不含目标编号（前缀冲突 / 其他编号冲突）；
- 多 CVE 仓库（URL 同时含目标与其他编号）一律保留，不计为冲突；
- URL 无任何编号的关联标记为证据不足，待元数据回补后判定，不丢弃。

## 已知限制

以下为当前明确接受、暂不处理的边界，按需评估影响：

- **同步断档不自动对账**：停机过久导致检查点被挤出 release 列表窗口时，
  会持续报告 `continuity_warning` 并在游标持久化断档标志，但不会自动执行
  完整基线对账补洞（需人工 `sync --all-releases` 或等待权威基线机制）；
- **描述证据边界**：URL 无编号、描述中仅以背景口吻提及目标编号（如
  "regression of CVE-X"）的仓库仍会被接受，此类措辞的误收依赖后续复核；
- **历史数据字段缺口**：早期自动拒绝的部分墓碑缺少裁决证据快照
  （描述文本/获取时间），不可恢复的历史裁决不伪造补齐；新裁决均完整落证据；
- **官方描述不回写**：CVE 官方描述更新不覆盖已发布 Markdown 中的旧描述；
- **零 PoC 历史基线未导入**：调度覆盖来自已收录关系与 cvelistV5 增量，
  历史上从未有 PoC 记录的 CVE 未做全量目录调度（增量通道会逐步纳入）。

## License

MIT License（见 [LICENSE](LICENSE)）。

本仓库基于 [ycdxsb/PocOrExp_in_Github](https://github.com/ycdxsb/PocOrExp_in_Github)
（MIT License © 2021 ycdxsb）的数据与思路重构而来，感谢原作者的聚合工作。
