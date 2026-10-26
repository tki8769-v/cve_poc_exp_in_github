# Update 2026-10-26
## CVE-2017-1000028

- [https://github.com/skl233/hdu-is-work1](https://github.com/skl233/hdu-is-work1) : ![starts](https://img.shields.io/github/stars/skl233/hdu-is-work1.svg) ![forks](https://img.shields.io/github/forks/skl233/hdu-is-work1.svg)

## CVE-2025-5548

- [https://github.com/FreemanHack/CVE-2025-5548](https://github.com/FreemanHack/CVE-2025-5548) : ![starts](https://img.shields.io/github/stars/FreemanHack/CVE-2025-5548.svg) ![forks](https://img.shields.io/github/forks/FreemanHack/CVE-2025-5548.svg)

## CVE-2026-109618
> PHP uses longjmp() for out-of-memory (OOM) errors to exit the current context and abort handling of the request. Some contexts may not properly account for this scenario and leave request memory in an uninitialized state before performing an allocation. The subsequent request cleanup procedure may read or branch on this memory. Multiple OOM strategies can consistently trigger this condition and lead to remote code execution (RCE).

- [https://github.com/franckferman/CVE-2026-109618](https://github.com/franckferman/CVE-2026-109618) : ![starts](https://img.shields.io/github/stars/franckferman/CVE-2026-109618.svg) ![forks](https://img.shields.io/github/forks/franckferman/CVE-2026-109618.svg)
- [https://github.com/gagaltotal/CVE-2026-109618-109619-php2shell](https://github.com/gagaltotal/CVE-2026-109618-109619-php2shell) : ![starts](https://img.shields.io/github/stars/gagaltotal/CVE-2026-109618-109619-php2shell.svg) ![forks](https://img.shields.io/github/forks/gagaltotal/CVE-2026-109618-109619-php2shell.svg)
- [https://github.com/lynolz163/php2shell-research-public](https://github.com/lynolz163/php2shell-research-public) : ![starts](https://img.shields.io/github/stars/lynolz163/php2shell-research-public.svg) ![forks](https://img.shields.io/github/forks/lynolz163/php2shell-research-public.svg)
- [https://github.com/turovskiy/php2shell-fixer](https://github.com/turovskiy/php2shell-fixer) : ![starts](https://img.shields.io/github/stars/turovskiy/php2shell-fixer.svg) ![forks](https://img.shields.io/github/forks/turovskiy/php2shell-fixer.svg)
- [https://github.com/yildirimserkan/stackprint](https://github.com/yildirimserkan/stackprint) : ![starts](https://img.shields.io/github/stars/yildirimserkan/stackprint.svg) ![forks](https://img.shields.io/github/forks/yildirimserkan/stackprint.svg)

## CVE-2026-109619
> PHP has various global state that temporarily points into request memory. In some scenarios, global state may not be correctly reset, or may be repopulated after being reset. The global state may then refer to request memory even after it has been freed. Subsequent requests may read or branch on this stale state before it is fully initialized. Multiple strategies can trigger this condition and produce remote code execution (RCE).

- [https://github.com/franckferman/CVE-2026-109619](https://github.com/franckferman/CVE-2026-109619) : ![starts](https://img.shields.io/github/stars/franckferman/CVE-2026-109619.svg) ![forks](https://img.shields.io/github/forks/franckferman/CVE-2026-109619.svg)

## CVE-2026-111497
> A buffer overflow vulnerability in the Brotli decoder (c/dec/decode.c) in Google Brotli versions 1.0.3 through 1.2.0 on all platforms allows a remote unauthenticated attacker to corrupt adjacent decoder state memory, disclose sensitive memory contents, cause a denial of service, or potentially execute arbitrary code using a crafted Brotli-compressed stream.





Users need to update any Brotli libraries or binaries between 1.0.3 through 1.2.0 to the latest available version: 1.0.10 or 1.1.1 or 1

- [https://github.com/CompleTetech-Security/http2shell-check](https://github.com/CompleTetech-Security/http2shell-check) : ![starts](https://img.shields.io/github/stars/CompleTetech-Security/http2shell-check.svg) ![forks](https://img.shields.io/github/forks/CompleTetech-Security/http2shell-check.svg)
- [https://github.com/datmt/vulcheck](https://github.com/datmt/vulcheck) : ![starts](https://img.shields.io/github/stars/datmt/vulcheck.svg) ![forks](https://img.shields.io/github/forks/datmt/vulcheck.svg)
- [https://github.com/ionsec/node2shell-detector](https://github.com/ionsec/node2shell-detector) : ![starts](https://img.shields.io/github/stars/ionsec/node2shell-detector.svg) ![forks](https://img.shields.io/github/forks/ionsec/node2shell-detector.svg)

## CVE-2026-115560

- [https://github.com/Pr0fEs0r-X/PHP-CVE-2026-115560-Cheker-v-1.0](https://github.com/Pr0fEs0r-X/PHP-CVE-2026-115560-Cheker-v-1.0) : ![starts](https://img.shields.io/github/stars/Pr0fEs0r-X/PHP-CVE-2026-115560-Cheker-v-1.0.svg) ![forks](https://img.shields.io/github/forks/Pr0fEs0r-X/PHP-CVE-2026-115560-Cheker-v-1.0.svg)

## CVE-2026-18107

- [https://github.com/robalb/criu-exploit](https://github.com/robalb/criu-exploit) : ![starts](https://img.shields.io/github/stars/robalb/criu-exploit.svg) ![forks](https://img.shields.io/github/forks/robalb/criu-exploit.svg)

## CVE-2026-20131

- [https://github.com/basesixtythree/B63-POC-CVE-2026-20131](https://github.com/basesixtythree/B63-POC-CVE-2026-20131) : ![starts](https://img.shields.io/github/stars/basesixtythree/B63-POC-CVE-2026-20131.svg) ![forks](https://img.shields.io/github/forks/basesixtythree/B63-POC-CVE-2026-20131.svg)

## CVE-2026-39902
> Cacti is an open source performance and fault management framework. Prior to version 1.2.31, the prior blocklist ([;&amp;| `$\\n\r]) omitted single-quote, double-quote, redirect operators, subshell parens and braces. An authenticated admin could save an input_string` containing single-quote, redirect operator, or subshell parens, and pass the check. This issue has been patched in version 1.2.31.

- [https://github.com/kx00007/CVE-2026-39902](https://github.com/kx00007/CVE-2026-39902) : ![starts](https://img.shields.io/github/stars/kx00007/CVE-2026-39902.svg) ![forks](https://img.shields.io/github/forks/kx00007/CVE-2026-39902.svg)

## CVE-2026-42945

- [https://github.com/x0xr00t/sl0ppy-riftscan-CVE-2026-42945](https://github.com/x0xr00t/sl0ppy-riftscan-CVE-2026-42945) : ![starts](https://img.shields.io/github/stars/x0xr00t/sl0ppy-riftscan-CVE-2026-42945.svg) ![forks](https://img.shields.io/github/forks/x0xr00t/sl0ppy-riftscan-CVE-2026-42945.svg)

## CVE-2026-53921
> odhcpd is the DHCPv6, DHCPv4, and router-advertisement server used by OpenWrt. Prior to version 25.12, odhcpd&#x27;s DHCPv6 IA response handler writes past the end of a fixed 512-byte stack buffer (pdbuf) when a single DHCPv6 REQUEST carries enough IA options to nearly exhaust the reply space. Two independent overflow sites exist in the same call chain, both reachable from the network via a single unauthenticated UDP packet. odhcpd runs as root on OpenWrt; embedded targets often lack stack canaries a

- [https://github.com/0xBlackash/CVE-2026-53921](https://github.com/0xBlackash/CVE-2026-53921) : ![starts](https://img.shields.io/github/stars/0xBlackash/CVE-2026-53921.svg) ![forks](https://img.shields.io/github/forks/0xBlackash/CVE-2026-53921.svg)

## CVE-2026-75650

- [https://github.com/basesixtythree/B63-POC-CVE-2026-75650](https://github.com/basesixtythree/B63-POC-CVE-2026-75650) : ![starts](https://img.shields.io/github/stars/basesixtythree/B63-POC-CVE-2026-75650.svg) ![forks](https://img.shields.io/github/forks/basesixtythree/B63-POC-CVE-2026-75650.svg)

## CVE-2026-84589

- [https://github.com/isaiahehlert/CVE-2026-84589-macOS-TCC-Bypass](https://github.com/isaiahehlert/CVE-2026-84589-macOS-TCC-Bypass) : ![starts](https://img.shields.io/github/stars/isaiahehlert/CVE-2026-84589-macOS-TCC-Bypass.svg) ![forks](https://img.shields.io/github/forks/isaiahehlert/CVE-2026-84589-macOS-TCC-Bypass.svg)

## CVE-2026-98260
> In the Linux kernel, the following vulnerability has been resolved:

exec: Cleanup POSIX timers right after de_thread()

A per-thread CPU timer holds a reference to the PID of the thread it is
attached to and, while it is armed, its node is queued in that thread&#x27;s
posix_cputimers. The task is looked up by that PID.

When a non-leader thread exec()s, de_thread() changes which task owns
that PID. pid_task(timer-&gt;it.cpu.pid, PIDTYPE_PID) then returns NULL,
but the node is still queued on tsk, which

- [https://github.com/AzirX1337/CVE-2026-98260-OnePlus16-PYB110-Jailbreak](https://github.com/AzirX1337/CVE-2026-98260-OnePlus16-PYB110-Jailbreak) : ![starts](https://img.shields.io/github/stars/AzirX1337/CVE-2026-98260-OnePlus16-PYB110-Jailbreak.svg) ![forks](https://img.shields.io/github/forks/AzirX1337/CVE-2026-98260-OnePlus16-PYB110-Jailbreak.svg)
- [https://github.com/addxemmm/CVE-2026-98260-pudding-android](https://github.com/addxemmm/CVE-2026-98260-pudding-android) : ![starts](https://img.shields.io/github/stars/addxemmm/CVE-2026-98260-pudding-android.svg) ![forks](https://img.shields.io/github/forks/addxemmm/CVE-2026-98260-pudding-android.svg)
