"""collector 命令行入口：python -m collector {check,bootstrap,clean,sync,backfill,recheck,scan}。"""
from __future__ import annotations

import argparse

from . import state as state_mod
from .audit import format_report, run_audit
from .bootstrap import bootstrap
from .clean import clean_dry_run


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="collector",
        description="PocOrExp_in_Github 采集/清洗管线（P0+P1a）",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("check", help="审计扫描（固定口径，输出漂移对比）")
    parser_boot = sub.add_parser("bootstrap", help="从年份 README 引导历史关系到 state/")
    parser_boot.add_argument("--force", action="store_true",
                             help="已引导过时强制重建（自动快照到 state/bootstrap_backup/）")
    parser_clean = sub.add_parser("clean", help="历史清洗（dry-run 复核清单 / --apply 应用证据完备项）")
    parser_clean.add_argument("--apply", action="store_true",
                              help="应用反证复核结论（evidenced→rejected 墓碑，resolved→accepted）并重渲染")

    parser_sync = sub.add_parser("sync", help="cvelistV5 连续同步（新增/修改/REJECTED）")
    parser_sync.add_argument("--all-releases", action="store_true",
                             help="处理窗口内全部未处理 release（默认首跑只取最新）")

    parser_backfill = sub.add_parser("backfill", help="回补仓库元数据（预算内，可续跑）")
    parser_backfill.add_argument("--limit", type=int, default=100, help="本轮最多拉取的仓库数")
    parser_backfill.add_argument("--priority-conflicts", action="store_true",
                                 help="优先回补冲突候选涉及的仓库（反证复核急需）")
    parser_backfill.add_argument("--budget-minutes", type=float, default=None,
                                 help="本轮时间预算（分钟）")

    sub.add_parser("recheck", help="冲突候选反证复核（纯本地，需先回补元数据）")

    sub.add_parser("render", help="统一渲染年份 README / PocOrExp.md / Today.md（原子写，未变不写）")
    sub.add_parser("verify", help="契约验证：渲染集合 == 活跃关系集合，并用真实下游解析函数复核")
    sub.add_parser("migrate", help="存量迁移：任务差集补齐、游标 schema、权威状态与 auto 标记（幂等）")
    parser_discover = sub.add_parser(
        "discover", help="仓库侧增量发现：最近新建且含 CVE 字样的仓库，反查归属（时效通道）")
    parser_discover.add_argument("--dry-run", action="store_true",
                                 help="只读模式：不写关系/事件/任务/游标")

    parser_daily = sub.add_parser(
        "daily", help="单命令编排一轮：sync→scan→backfill→recheck→apply→render→verify")
    parser_daily.add_argument("--scan-requests", type=int, default=300)
    parser_daily.add_argument("--scan-minutes", type=float, default=12.0)
    parser_daily.add_argument("--backfill-limit", type=int, default=1500)
    parser_daily.add_argument("--backfill-minutes", type=float, default=16.0)
    parser_daily.add_argument("--time-budget-minutes", type=float, default=40.0,
                              help="整轮时间预算（含同步/发现/扫描/回补）")

    parser_scan = sub.add_parser("scan", help="扫描到期 CVE 任务（搜索+三态过滤+合并）")
    parser_scan.add_argument("--limit-tasks", type=int, default=50)
    parser_scan.add_argument("--budget-requests", type=int, default=None)
    parser_scan.add_argument("--budget-minutes", type=float, default=None)

    args = parser.parse_args(argv)
    root = state_mod.project_root()

    if args.command == "check":
        result = run_audit(root)
        print(format_report(result))
        state_mod.write_json(state_mod.state_dir(root) / "audit_report.json", result)
        return 0

    if args.command == "bootstrap":
        report = bootstrap(root, force=args.force)
        print(f"bootstrap 完成: relations={report['relations_total']}, "
              f"unique_repos={report['unique_repos']}, years={len(report['years'])}, "
              f"cves_scheduled={report['cves_scheduled']}")
        return 0

    if args.command == "clean":
        if args.apply:
            from .clean import clean_apply
            from .render import render_all

            report = clean_apply(root)
            print(f"clean --apply 完成: rejected={report['applied_rejected']}, "
                  f"revoked_rejected={report['revoked_rejected']}, "
                  f"revoked_accepted={report['revoked_accepted']}, "
                  f"受影响年份={report['affected_years'] or '无'}, "
                  f"待回补元数据={report['still_pending_meta']}")
            if report["affected_years"]:
                manifest = render_all(root)
                print(f"已重渲染: {len(manifest['changed'])} 个文件变更")
            return 0
        result = clean_dry_run(root)
        stats = result["stats"]
        print(f"clean dry-run 完成: total={stats['total']}, "
              f"conflict_candidate={stats['conflict_candidate']}, "
              f"insufficient_evidence={stats['insufficient_evidence']}")
        print("报告: state/clean_dryrun/summary.md 与 conflicts.jsonl（未修改任何数据）")
        return 0

    if args.command == "sync":
        from .cvesource import sync
        from .ghsearch import GitHubClient

        report = sync(GitHubClient(), root, all_releases=args.all_releases)
        print(f"sync 完成: releases {report['releases_processed']}/{report['releases_seen']} 处理, "
              f"cves_seen={report['cves_seen']}, new_tasks={report['new_tasks']}, "
              f"rejected={report['rejected']}, last_tag={report['last_tag']}")
        return 0

    if args.command == "backfill":
        from .backfill import backfill
        from .ghsearch import GitHubClient

        report = backfill(GitHubClient(), root, limit=args.limit,
                          priority_conflicts=args.priority_conflicts,
                          budget_seconds=(args.budget_minutes * 60)
                          if args.budget_minutes is not None else None)  # G8：显式 0 ≠ 缺省
        print(f"backfill 完成: requested={report['requested']}, fetched={report['fetched']}, "
              f"cached_total={report['cached_total']}"
              + (f", 提前停止: {report['stop_reason']}" if report["stop_reason"] else ""))
        return 0

    if args.command == "recheck":
        from .recheck import recheck

        report = recheck(root)
        print(f"recheck 完成: 冲突候选 {report['conflicts_total']} 条 -> "
              f"证据充分可拒 {report['conflict_evidenced']} / 待复核 {report['needs_review']} / "
              f"仓库消失 {report['gone']} / 待回补元数据 {report['missing_meta']}")
        print("报告: state/recheck/report.json")
        return 0

    if args.command == "migrate":
        from .migrate import migrate

        report = migrate(root)
        print(f"migrate 完成: 缺失任务补齐 {report['tasks_created']}"
              f"（补前缺失 {report['tasks_missing_before']}）, "
              f"游标迁移={report.get('cursor_floor_migrated', False)}, "
              f"权威状态补写={report['cve_states_backfilled']}, "
              f"auto 标记补齐={report['auto_flags_patched']}, "
              f"状态 source_kind 规范化={report.get('state_kind_patched', 0)}, "
              f"新任务优先级规范化={report.get('priorities_normalized', 0)}")
        return 0

    if args.command == "render":
        from .render import render_all

        manifest = render_all(root)
        print(f"render 完成: years={manifest['years']}, sections={manifest['sections']}, "
              f"relations={manifest['relations']}, 变更文件={len(manifest['changed'])}")
        for path in manifest["changed"]:
            print(f"  变更: {path}")
        return 0

    if args.command == "verify":
        from .render import verify_contract

        report = verify_contract(root)
        if report["ok"]:
            kind = report.get("downstream_kind", "none")
            print(f"verify 通过: 真实发布产物与活跃关系一致"
                  + (f"，下游解析复核一致（{kind}）" if report["downstream_checked"] else ""))
        else:
            for problem in report["problems"]:
                print(f"[FAIL] {problem}")
            return 1
        return 0

    if args.command == "discover":
        from .ghsearch import GitHubClient
        from .repo_watch import discover

        stats = discover(GitHubClient(), root, dry_run=args.dry_run)
        print(f"discover 完成{' (dry-run)' if args.dry_run else ''}: "
              f"window={stats['window']}, repos_seen={stats['repos_seen']}, "
              f"cves_hit={stats['cves_hit']}, new_relations={stats['new_relations']}, "
              f"rejected={stats['rejected_at_collection']}, blocked={stats['blocked']}, "
              f"complete={stats['complete']}"
              + ("（不完整，游标未推进，下轮重试）" if not stats["complete"] else ""))
        return 0

    if args.command == "daily":
        from .pipeline import daily

        summary = daily(
            root,
            scan_requests=args.scan_requests,
            scan_minutes=args.scan_minutes,
            backfill_limit=args.backfill_limit,
            backfill_minutes=args.backfill_minutes,
            time_budget_minutes=args.time_budget_minutes,
        )
        steps = summary["steps"]
        print(f"daily 完成 ({summary['ts']}): "
              f"sync new_tasks={steps['sync']['new_tasks']}, "
              f"repo_watch hit={steps['repo_watch']['cves_hit']} new={steps['repo_watch']['new_relations']}, "
              f"scan scanned={steps['scan']['scanned']} new_relations={steps['scan']['new_relations']}, "
              f"backfill fetched={steps['backfill_conflicts']['fetched'] + steps['backfill_queue']['fetched']}, "
              f"apply rejected={steps['clean_apply'].get('applied_rejected', 0)}, "
              f"render changed={steps['render']['changed_files']}, verify ok={summary['ok']}")
        return 0

    if args.command == "scan":
        from .ghsearch import GitHubClient
        from .scan import scan

        stats = scan(GitHubClient(), root, limit_tasks=args.limit_tasks,
                     budget_requests=args.budget_requests,
                     budget_seconds=(args.budget_minutes * 60)
                     if args.budget_minutes is not None else None)  # G8：显式 0 ≠ 缺省
        print(f"scan 完成: scanned={stats['scanned']}/{stats['tasks_due']}, "
              f"new_relations={stats['new_relations']}, "
              f"rejected_at_collection={stats['rejected_at_collection']}, "
              f"needs_review={stats['needs_review']}, incomplete={stats['incomplete']}"
              + (f", 任务异常={stats['task_errors']}" if stats["task_errors"] else "")
              + ("（预算停止，任务保留）" if stats["budget_stopped"] else ""))
        return 0

    return 2


if __name__ == "__main__":
    raise SystemExit(main())
