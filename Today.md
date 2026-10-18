# Update 2026-10-18
## CVE-2015-2291
> (1) IQVW32.sys before 1.3.1.0 and (2) IQVW64.sys before 1.3.1.0 in the Intel Ethernet diagnostics driver for Windows allows local users to cause a denial of service or possibly execute arbitrary code with kernel privileges via a crafted (a) 0x80862013, (b) 0x8086200B, (c) 0x8086200F, or (d) 0x80862007 IOCTL call.

- [https://github.com/antoniorauso/NalCaller](https://github.com/antoniorauso/NalCaller) : ![starts](https://img.shields.io/github/stars/antoniorauso/NalCaller.svg) ![forks](https://img.shields.io/github/forks/antoniorauso/NalCaller.svg)

## CVE-2026-31431
> In the Linux kernel, the following vulnerability has been resolved:

crypto: algif_aead - Revert to operating out-of-place

This mostly reverts commit 72548b093ee3 except for the copying of
the associated data.

There is no benefit in operating in-place in algif_aead since the
source and destination come from different mappings.  Get rid of
all the complexity added for in-place operation and just copy the
AD directly.

- [https://github.com/DroPZsec/SplicePrivillegeEscalationFIX](https://github.com/DroPZsec/SplicePrivillegeEscalationFIX) : ![starts](https://img.shields.io/github/stars/DroPZsec/SplicePrivillegeEscalationFIX.svg) ![forks](https://img.shields.io/github/forks/DroPZsec/SplicePrivillegeEscalationFIX.svg)
- [https://github.com/Hunt-Benito/copy-fail-cve-2026-31431-linux-kernel-page-cache-lpe](https://github.com/Hunt-Benito/copy-fail-cve-2026-31431-linux-kernel-page-cache-lpe) : ![starts](https://img.shields.io/github/stars/Hunt-Benito/copy-fail-cve-2026-31431-linux-kernel-page-cache-lpe.svg) ![forks](https://img.shields.io/github/forks/Hunt-Benito/copy-fail-cve-2026-31431-linux-kernel-page-cache-lpe.svg)
- [https://github.com/Maxime288/CVE-2026-31431-Copy-Fail-R-pertoire-de-Pr-vention](https://github.com/Maxime288/CVE-2026-31431-Copy-Fail-R-pertoire-de-Pr-vention) : ![starts](https://img.shields.io/github/stars/Maxime288/CVE-2026-31431-Copy-Fail-R-pertoire-de-Pr-vention.svg) ![forks](https://img.shields.io/github/forks/Maxime288/CVE-2026-31431-Copy-Fail-R-pertoire-de-Pr-vention.svg)
- [https://github.com/Mr-bv/Copy-fail-CVE-2026-31431-Exploit-in-C](https://github.com/Mr-bv/Copy-fail-CVE-2026-31431-Exploit-in-C) : ![starts](https://img.shields.io/github/stars/Mr-bv/Copy-fail-CVE-2026-31431-Exploit-in-C.svg) ![forks](https://img.shields.io/github/forks/Mr-bv/Copy-fail-CVE-2026-31431-Exploit-in-C.svg)
- [https://github.com/ROSNLR5/MitigationToolkit-ROSN-LR5-Full](https://github.com/ROSNLR5/MitigationToolkit-ROSN-LR5-Full) : ![starts](https://img.shields.io/github/stars/ROSNLR5/MitigationToolkit-ROSN-LR5-Full.svg) ![forks](https://img.shields.io/github/forks/ROSNLR5/MitigationToolkit-ROSN-LR5-Full.svg)
- [https://github.com/Rat5ak/CVE-2026-31431-CopyFail-static-ELF--POC](https://github.com/Rat5ak/CVE-2026-31431-CopyFail-static-ELF--POC) : ![starts](https://img.shields.io/github/stars/Rat5ak/CVE-2026-31431-CopyFail-static-ELF--POC.svg) ![forks](https://img.shields.io/github/forks/Rat5ak/CVE-2026-31431-CopyFail-static-ELF--POC.svg)
- [https://github.com/RazvanDuda/GhostShell](https://github.com/RazvanDuda/GhostShell) : ![starts](https://img.shields.io/github/stars/RazvanDuda/GhostShell.svg) ![forks](https://img.shields.io/github/forks/RazvanDuda/GhostShell.svg)
- [https://github.com/YuCc777/Copy-Fail-CVE-2026-31431-Linux-exp-tools-C-EXP](https://github.com/YuCc777/Copy-Fail-CVE-2026-31431-Linux-exp-tools-C-EXP) : ![starts](https://img.shields.io/github/stars/YuCc777/Copy-Fail-CVE-2026-31431-Linux-exp-tools-C-EXP.svg) ![forks](https://img.shields.io/github/forks/YuCc777/Copy-Fail-CVE-2026-31431-Linux-exp-tools-C-EXP.svg)
- [https://github.com/chavezvic/CopyFail-Penguin](https://github.com/chavezvic/CopyFail-Penguin) : ![starts](https://img.shields.io/github/stars/chavezvic/CopyFail-Penguin.svg) ![forks](https://img.shields.io/github/forks/chavezvic/CopyFail-Penguin.svg)
- [https://github.com/cleozi/Copy_Grail](https://github.com/cleozi/Copy_Grail) : ![starts](https://img.shields.io/github/stars/cleozi/Copy_Grail.svg) ![forks](https://img.shields.io/github/forks/cleozi/Copy_Grail.svg)
- [https://github.com/deadRabbit92/mitigate-copy-fail.yml](https://github.com/deadRabbit92/mitigate-copy-fail.yml) : ![starts](https://img.shields.io/github/stars/deadRabbit92/mitigate-copy-fail.yml.svg) ![forks](https://img.shields.io/github/forks/deadRabbit92/mitigate-copy-fail.yml.svg)
- [https://github.com/dicatalin/Copy_Fail_CVE-2026-31431_test_and_fix](https://github.com/dicatalin/Copy_Fail_CVE-2026-31431_test_and_fix) : ![starts](https://img.shields.io/github/stars/dicatalin/Copy_Fail_CVE-2026-31431_test_and_fix.svg) ![forks](https://img.shields.io/github/forks/dicatalin/Copy_Fail_CVE-2026-31431_test_and_fix.svg)
- [https://github.com/dotPY-hax/CopyFail](https://github.com/dotPY-hax/CopyFail) : ![starts](https://img.shields.io/github/stars/dotPY-hax/CopyFail.svg) ![forks](https://img.shields.io/github/forks/dotPY-hax/CopyFail.svg)
- [https://github.com/iblamenear/CVE-2026-31431-Copy-Fail---Advanced-LPE-Proof-of-Concept---C-Rewrite](https://github.com/iblamenear/CVE-2026-31431-Copy-Fail---Advanced-LPE-Proof-of-Concept---C-Rewrite) : ![starts](https://img.shields.io/github/stars/iblamenear/CVE-2026-31431-Copy-Fail---Advanced-LPE-Proof-of-Concept---C-Rewrite.svg) ![forks](https://img.shields.io/github/forks/iblamenear/CVE-2026-31431-Copy-Fail---Advanced-LPE-Proof-of-Concept---C-Rewrite.svg)
- [https://github.com/imkk000/play-go-copy-fail-cve-2026-31431](https://github.com/imkk000/play-go-copy-fail-cve-2026-31431) : ![starts](https://img.shields.io/github/stars/imkk000/play-go-copy-fail-cve-2026-31431.svg) ![forks](https://img.shields.io/github/forks/imkk000/play-go-copy-fail-cve-2026-31431.svg)
- [https://github.com/jbiniek/copy.fail-mitigation-MLM](https://github.com/jbiniek/copy.fail-mitigation-MLM) : ![starts](https://img.shields.io/github/stars/jbiniek/copy.fail-mitigation-MLM.svg) ![forks](https://img.shields.io/github/forks/jbiniek/copy.fail-mitigation-MLM.svg)
- [https://github.com/jiangban046-spec/CVE-2026-31431-exploit_py2_py3](https://github.com/jiangban046-spec/CVE-2026-31431-exploit_py2_py3) : ![starts](https://img.shields.io/github/stars/jiangban046-spec/CVE-2026-31431-exploit_py2_py3.svg) ![forks](https://img.shields.io/github/forks/jiangban046-spec/CVE-2026-31431-exploit_py2_py3.svg)
- [https://github.com/jihwan77/Linux-Kernel-Copy-Fail-CVE-2026-31431-](https://github.com/jihwan77/Linux-Kernel-Copy-Fail-CVE-2026-31431-) : ![starts](https://img.shields.io/github/stars/jihwan77/Linux-Kernel-Copy-Fail-CVE-2026-31431-.svg) ![forks](https://img.shields.io/github/forks/jihwan77/Linux-Kernel-Copy-Fail-CVE-2026-31431-.svg)
- [https://github.com/joaocalciolari07/copyfail-guard](https://github.com/joaocalciolari07/copyfail-guard) : ![starts](https://img.shields.io/github/stars/joaocalciolari07/copyfail-guard.svg) ![forks](https://img.shields.io/github/forks/joaocalciolari07/copyfail-guard.svg)
- [https://github.com/jodonnel/copyfail-briefing](https://github.com/jodonnel/copyfail-briefing) : ![starts](https://img.shields.io/github/stars/jodonnel/copyfail-briefing.svg) ![forks](https://img.shields.io/github/forks/jodonnel/copyfail-briefing.svg)
- [https://github.com/kvendler/BigFix-CopyFail-AlmaLinux-Content](https://github.com/kvendler/BigFix-CopyFail-AlmaLinux-Content) : ![starts](https://img.shields.io/github/stars/kvendler/BigFix-CopyFail-AlmaLinux-Content.svg) ![forks](https://img.shields.io/github/forks/kvendler/BigFix-CopyFail-AlmaLinux-Content.svg)
- [https://github.com/luoqianlin/copyfail-c](https://github.com/luoqianlin/copyfail-c) : ![starts](https://img.shields.io/github/stars/luoqianlin/copyfail-c.svg) ![forks](https://img.shields.io/github/forks/luoqianlin/copyfail-c.svg)
- [https://github.com/mlazzarotto/copy-fail-CVE-2026-31431-mitigation-ansible-playbook](https://github.com/mlazzarotto/copy-fail-CVE-2026-31431-mitigation-ansible-playbook) : ![starts](https://img.shields.io/github/stars/mlazzarotto/copy-fail-CVE-2026-31431-mitigation-ansible-playbook.svg) ![forks](https://img.shields.io/github/forks/mlazzarotto/copy-fail-CVE-2026-31431-mitigation-ansible-playbook.svg)
- [https://github.com/monobrau/copyfailscan](https://github.com/monobrau/copyfailscan) : ![starts](https://img.shields.io/github/stars/monobrau/copyfailscan.svg) ![forks](https://img.shields.io/github/forks/monobrau/copyfailscan.svg)
- [https://github.com/mrowkoob/copy-fail-mitigate-no-reboot](https://github.com/mrowkoob/copy-fail-mitigate-no-reboot) : ![starts](https://img.shields.io/github/stars/mrowkoob/copy-fail-mitigate-no-reboot.svg) ![forks](https://img.shields.io/github/forks/mrowkoob/copy-fail-mitigate-no-reboot.svg)
- [https://github.com/nrnw/CVE-2026-31431-Linux-Kernel-Copy-Fail-Detector](https://github.com/nrnw/CVE-2026-31431-Linux-Kernel-Copy-Fail-Detector) : ![starts](https://img.shields.io/github/stars/nrnw/CVE-2026-31431-Linux-Kernel-Copy-Fail-Detector.svg) ![forks](https://img.shields.io/github/forks/nrnw/CVE-2026-31431-Linux-Kernel-Copy-Fail-Detector.svg)
- [https://github.com/p401a-ops/Copy-Fail](https://github.com/p401a-ops/Copy-Fail) : ![starts](https://img.shields.io/github/stars/p401a-ops/Copy-Fail.svg) ![forks](https://img.shields.io/github/forks/p401a-ops/Copy-Fail.svg)
- [https://github.com/paulorlima9/copyfail-fix](https://github.com/paulorlima9/copyfail-fix) : ![starts](https://img.shields.io/github/stars/paulorlima9/copyfail-fix.svg) ![forks](https://img.shields.io/github/forks/paulorlima9/copyfail-fix.svg)
- [https://github.com/pedro-lucas-melo/Estudo-de-Caso-CVE-2026-31431-CopyFail](https://github.com/pedro-lucas-melo/Estudo-de-Caso-CVE-2026-31431-CopyFail) : ![starts](https://img.shields.io/github/stars/pedro-lucas-melo/Estudo-de-Caso-CVE-2026-31431-CopyFail.svg) ![forks](https://img.shields.io/github/forks/pedro-lucas-melo/Estudo-de-Caso-CVE-2026-31431-CopyFail.svg)
- [https://github.com/ridhinva/linux-kernel-algif-aead-checker](https://github.com/ridhinva/linux-kernel-algif-aead-checker) : ![starts](https://img.shields.io/github/stars/ridhinva/linux-kernel-algif-aead-checker.svg) ![forks](https://img.shields.io/github/forks/ridhinva/linux-kernel-algif-aead-checker.svg)
- [https://github.com/selectel/mks-copy-fail-mitigation](https://github.com/selectel/mks-copy-fail-mitigation) : ![starts](https://img.shields.io/github/stars/selectel/mks-copy-fail-mitigation.svg) ![forks](https://img.shields.io/github/forks/selectel/mks-copy-fail-mitigation.svg)
- [https://github.com/starscow/Copy-Fail-CVE-2026-31431-Kubernetes-PoC](https://github.com/starscow/Copy-Fail-CVE-2026-31431-Kubernetes-PoC) : ![starts](https://img.shields.io/github/stars/starscow/Copy-Fail-CVE-2026-31431-Kubernetes-PoC.svg) ![forks](https://img.shields.io/github/forks/starscow/Copy-Fail-CVE-2026-31431-Kubernetes-PoC.svg)
- [https://github.com/tang-yikai/copy-fail-mitigation-with-bpftrace](https://github.com/tang-yikai/copy-fail-mitigation-with-bpftrace) : ![starts](https://img.shields.io/github/stars/tang-yikai/copy-fail-mitigation-with-bpftrace.svg) ![forks](https://img.shields.io/github/forks/tang-yikai/copy-fail-mitigation-with-bpftrace.svg)
- [https://github.com/vishvacyber/Detection-Tool-Kit-for-CVE-2026-31431](https://github.com/vishvacyber/Detection-Tool-Kit-for-CVE-2026-31431) : ![starts](https://img.shields.io/github/stars/vishvacyber/Detection-Tool-Kit-for-CVE-2026-31431.svg) ![forks](https://img.shields.io/github/forks/vishvacyber/Detection-Tool-Kit-for-CVE-2026-31431.svg)
- [https://github.com/vorkampfer/copy_fail_mitigation](https://github.com/vorkampfer/copy_fail_mitigation) : ![starts](https://img.shields.io/github/stars/vorkampfer/copy_fail_mitigation.svg) ![forks](https://img.shields.io/github/forks/vorkampfer/copy_fail_mitigation.svg)
- [https://github.com/vorkampfer/copyfail2_electric_boogaloo_fix](https://github.com/vorkampfer/copyfail2_electric_boogaloo_fix) : ![starts](https://img.shields.io/github/stars/vorkampfer/copyfail2_electric_boogaloo_fix.svg) ![forks](https://img.shields.io/github/forks/vorkampfer/copyfail2_electric_boogaloo_fix.svg)
- [https://github.com/voxcia-io/copy-fail](https://github.com/voxcia-io/copy-fail) : ![starts](https://img.shields.io/github/stars/voxcia-io/copy-fail.svg) ![forks](https://img.shields.io/github/forks/voxcia-io/copy-fail.svg)

## CVE-2026-43499
> In the Linux kernel, the following vulnerability has been resolved:

rtmutex: Use waiter::task instead of current in remove_waiter()

remove_waiter() is used by the slowlock paths, but it is also used for
proxy-lock rollback in rt_mutex_start_proxy_lock() when invoked from
futex_requeue().

In the latter case waiter::task is not current, but remove_waiter()
operates on current for the dequeue operation. That results in several
problems:

  1) the rbtree dequeue happens without waiter::task::pi_l

- [https://github.com/AuroraMythweaver/iqoo-neo9-ghostlock-pc](https://github.com/AuroraMythweaver/iqoo-neo9-ghostlock-pc) : ![starts](https://img.shields.io/github/stars/AuroraMythweaver/iqoo-neo9-ghostlock-pc.svg) ![forks](https://img.shields.io/github/forks/AuroraMythweaver/iqoo-neo9-ghostlock-pc.svg)

## CVE-2026-50229

- [https://github.com/flvzx/CVE-2026-50229](https://github.com/flvzx/CVE-2026-50229) : ![starts](https://img.shields.io/github/stars/flvzx/CVE-2026-50229.svg) ![forks](https://img.shields.io/github/forks/flvzx/CVE-2026-50229.svg)

## CVE-2026-71557

- [https://github.com/Saku0512/reprokit-go-git-cve-2026-71557-lab](https://github.com/Saku0512/reprokit-go-git-cve-2026-71557-lab) : ![starts](https://img.shields.io/github/stars/Saku0512/reprokit-go-git-cve-2026-71557-lab.svg) ![forks](https://img.shields.io/github/forks/Saku0512/reprokit-go-git-cve-2026-71557-lab.svg)
