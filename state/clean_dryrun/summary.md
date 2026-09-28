# Clean dry-run（不修改任何数据）

- rule_version: 2
- 关系总数: 27916
- keep（URL 含目标，含多 CVE 仓库）: 20907
- conflict_candidate（URL 含编号但不含目标，待反证复核）: 903
  - prefix_conflict: 547
  - foreign_id_conflict: 356
- insufficient_evidence（URL 无编号，待元数据回补）: 6106

## 处置规则（保守）

- 仅当仓库描述非空、不含目标编号、且明确自述为 URL 所指编号时，
  clean --apply 才自动 rejected；
- 描述提及目标（regression 类上下文）、空描述、沉默描述 → needs_review；
- rejected 墓碑可被新证据重新裁决（auto 标记，revocable）。
