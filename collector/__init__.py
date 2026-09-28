"""PocOrExp_in_Github collector (REFACTOR_PLAN.md v2, P0 scope).

P0 提供统一解析规则（parse）、审计扫描（audit）、历史关系引导
（bootstrap）与清洗 dry-run（clean）。P1/P2 模块（cvesource /
ghsearch / scheduler / 渲染发布）按计划后续补充。
"""

RULES_VERSION = "2"  # v2：归属规则修订（背景引用进复核、空描述不排除，评审 R4/F6）
