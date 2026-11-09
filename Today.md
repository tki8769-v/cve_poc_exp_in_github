# Update 2026-11-09
## CVE-2021-40444

- [https://github.com/m4madturk/CVE-2021-40444](https://github.com/m4madturk/CVE-2021-40444) : ![starts](https://img.shields.io/github/stars/m4madturk/CVE-2021-40444.svg) ![forks](https://img.shields.io/github/forks/m4madturk/CVE-2021-40444.svg)

## CVE-2021-44228

- [https://github.com/sejauhkayuh/Vulnerable-and-Outdated-Components-Insiden-Log4Shell-CVE-2021-44228-](https://github.com/sejauhkayuh/Vulnerable-and-Outdated-Components-Insiden-Log4Shell-CVE-2021-44228-) : ![starts](https://img.shields.io/github/stars/sejauhkayuh/Vulnerable-and-Outdated-Components-Insiden-Log4Shell-CVE-2021-44228-.svg) ![forks](https://img.shields.io/github/forks/sejauhkayuh/Vulnerable-and-Outdated-Components-Insiden-Log4Shell-CVE-2021-44228-.svg)

## CVE-2024-44068

- [https://github.com/privacyportalUK/PP-Root](https://github.com/privacyportalUK/PP-Root) : ![starts](https://img.shields.io/github/stars/privacyportalUK/PP-Root.svg) ![forks](https://img.shields.io/github/forks/privacyportalUK/PP-Root.svg)

## CVE-2025-31161

- [https://github.com/ashrafzaryouh/CVE-2025-31161](https://github.com/ashrafzaryouh/CVE-2025-31161) : ![starts](https://img.shields.io/github/stars/ashrafzaryouh/CVE-2025-31161.svg) ![forks](https://img.shields.io/github/forks/ashrafzaryouh/CVE-2025-31161.svg)

## CVE-2025-48583

- [https://github.com/helloguy1234/CVE-2025-48583-PoC](https://github.com/helloguy1234/CVE-2025-48583-PoC) : ![starts](https://img.shields.io/github/stars/helloguy1234/CVE-2025-48583-PoC.svg) ![forks](https://img.shields.io/github/forks/helloguy1234/CVE-2025-48583-PoC.svg)

## CVE-2026-109618
> PHP uses longjmp() for out-of-memory (OOM) errors to exit the current context and abort handling of the request. Some contexts may not properly account for this scenario and leave request memory in an uninitialized state before performing an allocation. The subsequent request cleanup procedure may read or branch on this memory. Multiple OOM strategies can consistently trigger this condition and lead to remote code execution (RCE).

- [https://github.com/Ghxstsec/PHP2SHELL-POC](https://github.com/Ghxstsec/PHP2SHELL-POC) : ![starts](https://img.shields.io/github/stars/Ghxstsec/PHP2SHELL-POC.svg) ![forks](https://img.shields.io/github/forks/Ghxstsec/PHP2SHELL-POC.svg)
- [https://github.com/ashrafzaryouh/CVE-2026-109618](https://github.com/ashrafzaryouh/CVE-2026-109618) : ![starts](https://img.shields.io/github/stars/ashrafzaryouh/CVE-2026-109618.svg) ![forks](https://img.shields.io/github/forks/ashrafzaryouh/CVE-2026-109618.svg)
- [https://github.com/hosun-hwang/CVE-2026-109618-CVE-2026-109619_PoC](https://github.com/hosun-hwang/CVE-2026-109618-CVE-2026-109619_PoC) : ![starts](https://img.shields.io/github/stars/hosun-hwang/CVE-2026-109618-CVE-2026-109619_PoC.svg) ![forks](https://img.shields.io/github/forks/hosun-hwang/CVE-2026-109618-CVE-2026-109619_PoC.svg)

## CVE-2026-109619
> PHP has various global state that temporarily points into request memory. In some scenarios, global state may not be correctly reset, or may be repopulated after being reset. The global state may then refer to request memory even after it has been freed. Subsequent requests may read or branch on this stale state before it is fully initialized. Multiple strategies can trigger this condition and produce remote code execution (RCE).

- [https://github.com/che3axujnya/cve-2026-109618-cve-2026-109619-poc](https://github.com/che3axujnya/cve-2026-109618-cve-2026-109619-poc) : ![starts](https://img.shields.io/github/stars/che3axujnya/cve-2026-109618-cve-2026-109619-poc.svg) ![forks](https://img.shields.io/github/forks/che3axujnya/cve-2026-109618-cve-2026-109619-poc.svg)
- [https://github.com/hosun-hwang/CVE-2026-109618-CVE-2026-109619_PoC](https://github.com/hosun-hwang/CVE-2026-109618-CVE-2026-109619_PoC) : ![starts](https://img.shields.io/github/stars/hosun-hwang/CVE-2026-109618-CVE-2026-109619_PoC.svg) ![forks](https://img.shields.io/github/forks/hosun-hwang/CVE-2026-109618-CVE-2026-109619_PoC.svg)

## CVE-2026-111497
> A buffer overflow vulnerability in the Brotli decoder (c/dec/decode.c) in Google Brotli versions 1.0.3 through 1.2.0 on all platforms allows a remote unauthenticated attacker to corrupt adjacent decoder state memory, disclose sensitive memory contents, cause a denial of service, or potentially execute arbitrary code using a crafted Brotli-compressed stream.





Users need to update any Brotli libraries or binaries between 1.0.3 through 1.2.0 to the latest available version: 1.0.10 or 1.1.1 or 1

- [https://github.com/hosun-hwang/CVE-2026-111497_PoC](https://github.com/hosun-hwang/CVE-2026-111497_PoC) : ![starts](https://img.shields.io/github/stars/hosun-hwang/CVE-2026-111497_PoC.svg) ![forks](https://img.shields.io/github/forks/hosun-hwang/CVE-2026-111497_PoC.svg)

## CVE-2026-113386
> Roundcube Webmail before 1.6.20 and 1.7.x before 1.7.5 are affected by IMAP command injection. A remote authenticated attacker can exploit this via CRLF sequences injected into the _uid parameter of the mail/headers and mail/viewsource actions to execute arbitrary IMAP commands.

- [https://github.com/Neo-XeD/CVE-2026-113386](https://github.com/Neo-XeD/CVE-2026-113386) : ![starts](https://img.shields.io/github/stars/Neo-XeD/CVE-2026-113386.svg) ![forks](https://img.shields.io/github/forks/Neo-XeD/CVE-2026-113386.svg)

## CVE-2026-11499
> A vulnerability was determined in Tenda HG7, HG9 and HG10 300001138_en_xpon. This affects the function formDOMAINBLK of the file /boaform/formDOMAINBLK. Executing a manipulation of the argument blkDomain can lead to stack-based buffer overflow. The attack may be performed from remote.

- [https://github.com/ashrafzaryouh/CVE-2026-11499](https://github.com/ashrafzaryouh/CVE-2026-11499) : ![starts](https://img.shields.io/github/stars/ashrafzaryouh/CVE-2026-11499.svg) ![forks](https://img.shields.io/github/forks/ashrafzaryouh/CVE-2026-11499.svg)

## CVE-2026-116567
> FreeSWITCH is a Software Defined Telecom Stack enabling the digital transformation from proprietary telecom switches to a software implementation that runs on any commodity hardware. Prior to 1.11.2, rtmp_handle_control() rendered an RTMP user-control message into a 200-byte stack buffer using an unbounded sprintf loop controlled by the wire message length. A body of roughly 70 bytes or more overflowed the stack before any RTMP login, because the handshake authenticates neither side. The flaw af

- [https://github.com/carterlasalle/CVE-2026-116567](https://github.com/carterlasalle/CVE-2026-116567) : ![starts](https://img.shields.io/github/stars/carterlasalle/CVE-2026-116567.svg) ![forks](https://img.shields.io/github/forks/carterlasalle/CVE-2026-116567.svg)

## CVE-2026-117083

- [https://github.com/gabrielunknown/intelbras_1200_bypass](https://github.com/gabrielunknown/intelbras_1200_bypass) : ![starts](https://img.shields.io/github/stars/gabrielunknown/intelbras_1200_bypass.svg) ![forks](https://img.shields.io/github/forks/gabrielunknown/intelbras_1200_bypass.svg)

## CVE-2026-123158
> sshd in OpenSSH before 10.6p2 on Linux, when musl libc is used without PAM, lacks a workaround for a password authentication bypass (related to misinterpretation of whether a string is intended to be a password hash). For some configurations of accounts, any password between 256 and 1024 characters succeeds. An example of a platform using musl libc without PAM is Alpine Linux.

- [https://github.com/D1se0/CVE-2026-123158](https://github.com/D1se0/CVE-2026-123158) : ![starts](https://img.shields.io/github/stars/D1se0/CVE-2026-123158.svg) ![forks](https://img.shields.io/github/forks/D1se0/CVE-2026-123158.svg)

## CVE-2026-14431

- [https://github.com/djayaGit/CVE-2026-14431](https://github.com/djayaGit/CVE-2026-14431) : ![starts](https://img.shields.io/github/stars/djayaGit/CVE-2026-14431.svg) ![forks](https://img.shields.io/github/forks/djayaGit/CVE-2026-14431.svg)

## CVE-2026-24061
> telnetd in GNU Inetutils through 2.7 allows remote authentication bypass via a &quot;-f root&quot; value for the USER environment variable.

- [https://github.com/ashrafzaryouh/CVE-2026-24061](https://github.com/ashrafzaryouh/CVE-2026-24061) : ![starts](https://img.shields.io/github/stars/ashrafzaryouh/CVE-2026-24061.svg) ![forks](https://img.shields.io/github/forks/ashrafzaryouh/CVE-2026-24061.svg)
- [https://github.com/hosun-hwang/CVE-2026-24061_PoC](https://github.com/hosun-hwang/CVE-2026-24061_PoC) : ![starts](https://img.shields.io/github/stars/hosun-hwang/CVE-2026-24061_PoC.svg) ![forks](https://img.shields.io/github/forks/hosun-hwang/CVE-2026-24061_PoC.svg)

## CVE-2026-31431
> In the Linux kernel, the following vulnerability has been resolved:

crypto: algif_aead - Revert to operating out-of-place

This mostly reverts commit 72548b093ee3 except for the copying of
the associated data.

There is no benefit in operating in-place in algif_aead since the
source and destination come from different mappings.  Get rid of
all the complexity added for in-place operation and just copy the
AD directly.

- [https://github.com/hosun-hwang/CVE-2026-31431_PoC](https://github.com/hosun-hwang/CVE-2026-31431_PoC) : ![starts](https://img.shields.io/github/stars/hosun-hwang/CVE-2026-31431_PoC.svg) ![forks](https://img.shields.io/github/forks/hosun-hwang/CVE-2026-31431_PoC.svg)

## CVE-2026-35616

- [https://github.com/ashrafzaryouh/CVE-2026-35616](https://github.com/ashrafzaryouh/CVE-2026-35616) : ![starts](https://img.shields.io/github/stars/ashrafzaryouh/CVE-2026-35616.svg) ![forks](https://img.shields.io/github/forks/ashrafzaryouh/CVE-2026-35616.svg)

## CVE-2026-40175

- [https://github.com/ashrafzaryouh/CVE-2026-40175](https://github.com/ashrafzaryouh/CVE-2026-40175) : ![starts](https://img.shields.io/github/stars/ashrafzaryouh/CVE-2026-40175.svg) ![forks](https://img.shields.io/github/forks/ashrafzaryouh/CVE-2026-40175.svg)

## CVE-2026-41940
> cPanel and WHM versions after 11.40 contain an authentication bypass vulnerability in the login flow that allows unauthenticated remote attackers to gain unauthorized access to the control panel.

- [https://github.com/ashrafzaryouh/CVE-2026-41940](https://github.com/ashrafzaryouh/CVE-2026-41940) : ![starts](https://img.shields.io/github/stars/ashrafzaryouh/CVE-2026-41940.svg) ![forks](https://img.shields.io/github/forks/ashrafzaryouh/CVE-2026-41940.svg)
- [https://github.com/ryhnmhrdka/CVE-2026-41940](https://github.com/ryhnmhrdka/CVE-2026-41940) : ![starts](https://img.shields.io/github/stars/ryhnmhrdka/CVE-2026-41940.svg) ![forks](https://img.shields.io/github/forks/ryhnmhrdka/CVE-2026-41940.svg)
- [https://github.com/ylerpeek/CVE-2026-41940-PoC-3](https://github.com/ylerpeek/CVE-2026-41940-PoC-3) : ![starts](https://img.shields.io/github/stars/ylerpeek/CVE-2026-41940-PoC-3.svg) ![forks](https://img.shields.io/github/forks/ylerpeek/CVE-2026-41940-PoC-3.svg)

## CVE-2026-50656

- [https://github.com/ashrafzaryouh/CVE-2026-50656](https://github.com/ashrafzaryouh/CVE-2026-50656) : ![starts](https://img.shields.io/github/stars/ashrafzaryouh/CVE-2026-50656.svg) ![forks](https://img.shields.io/github/forks/ashrafzaryouh/CVE-2026-50656.svg)

## CVE-2026-56712

- [https://github.com/SaiTeja-Erukude/CVE-2026-56712-cog-ssrf](https://github.com/SaiTeja-Erukude/CVE-2026-56712-cog-ssrf) : ![starts](https://img.shields.io/github/stars/SaiTeja-Erukude/CVE-2026-56712-cog-ssrf.svg) ![forks](https://img.shields.io/github/forks/SaiTeja-Erukude/CVE-2026-56712-cog-ssrf.svg)

## CVE-2026-60004

- [https://github.com/ashrafzaryouh/CVE-2026-60004](https://github.com/ashrafzaryouh/CVE-2026-60004) : ![starts](https://img.shields.io/github/stars/ashrafzaryouh/CVE-2026-60004.svg) ![forks](https://img.shields.io/github/forks/ashrafzaryouh/CVE-2026-60004.svg)

## CVE-2026-63292
> Stack-based buffer overflow in mod_vhost_alias in Apache Software Foundation Apache HTTP Server through 2.4.68 on all platforms allows a remote client to cause a denial of service or potentially execute arbitrary code via an HTTP request with a Host header exceeding 8192 bytes when VirtualDocumentRoot uses a hostname format specifier and LimitRequestFieldSize is raised above the default.

Users are recommended to upgrade to version 2.4.69, which fixes this issue.

- [https://github.com/ashrafzaryouh/CVE-2026-63292](https://github.com/ashrafzaryouh/CVE-2026-63292) : ![starts](https://img.shields.io/github/stars/ashrafzaryouh/CVE-2026-63292.svg) ![forks](https://img.shields.io/github/forks/ashrafzaryouh/CVE-2026-63292.svg)

## CVE-2026-8461

- [https://github.com/ashrafzaryouh/CVE-2026-8461](https://github.com/ashrafzaryouh/CVE-2026-8461) : ![starts](https://img.shields.io/github/stars/ashrafzaryouh/CVE-2026-8461.svg) ![forks](https://img.shields.io/github/forks/ashrafzaryouh/CVE-2026-8461.svg)

## CVE-2026-88771
> Improper input validation vulnerability in Citrix NetScaler ADC and Citrix NetScaler Gateway.

This issue affects ADC: before 14.1-73.37, before 13.1-64.23, before 14.1-73.37 FIPS, and before 13.1.37.279 FIPS and NDcPP; Gateway: before 14.1-73.37 and before 13.1-64.23 leading to an unauthenticated attacker to execute arbitrary commands.

- [https://github.com/CompleteTech-Security/netscaler-pitscaler-cve-2026-88771-check](https://github.com/CompleteTech-Security/netscaler-pitscaler-cve-2026-88771-check) : ![starts](https://img.shields.io/github/stars/CompleteTech-Security/netscaler-pitscaler-cve-2026-88771-check.svg) ![forks](https://img.shields.io/github/forks/CompleteTech-Security/netscaler-pitscaler-cve-2026-88771-check.svg)
- [https://github.com/irfanr-source/Get-NetScalerTimeline](https://github.com/irfanr-source/Get-NetScalerTimeline) : ![starts](https://img.shields.io/github/stars/irfanr-source/Get-NetScalerTimeline.svg) ![forks](https://img.shields.io/github/forks/irfanr-source/Get-NetScalerTimeline.svg)

## CVE-2026-88772
> Vulnerability in Citrix NetScaler ADC and Citrix NetScaler Gateway.

This issue affects ADC: before 14.1-73.37, before 13.1-64.23, before 14.1-73.37 FIPS, and before 13.1.37.279 FIPS and NDcPP; Gateway: before 14.1-73.37 and before 13.1-64.23 leading to Remote Code Execution or Denial of Service

- [https://github.com/CompleteTech-Security/netscaler-pitscaler-cve-2026-88772-check](https://github.com/CompleteTech-Security/netscaler-pitscaler-cve-2026-88772-check) : ![starts](https://img.shields.io/github/stars/CompleteTech-Security/netscaler-pitscaler-cve-2026-88772-check.svg) ![forks](https://img.shields.io/github/forks/CompleteTech-Security/netscaler-pitscaler-cve-2026-88772-check.svg)

## CVE-2026-92080
> Improper Limitation of a Pathname to a Restricted Directory (&#x27;Path Traversal&#x27;) vulnerability in TÜBİTAK BİLGEM Software Technologies Research Institute pardus-boot-repair allows Path Traversal.

This issue affects pardus-boot-repair: from 1.0.8 before 1.1.0.

- [https://github.com/ozcanpng/CVE-2026-92080](https://github.com/ozcanpng/CVE-2026-92080) : ![starts](https://img.shields.io/github/stars/ozcanpng/CVE-2026-92080.svg) ![forks](https://img.shields.io/github/forks/ozcanpng/CVE-2026-92080.svg)

## CVE-2026-96889
> A flaw was found in librsvg. When processing an SVG document containing nested XML inclusions (Xincludes) with duplicate entity declarations, a use-after-free error can occur. This vulnerability arises because the library incorrectly frees an XML entity that is still in use by the parser. An attacker could potentially exploit this to cause a denial of service or execute arbitrary code.

- [https://github.com/anishadhikari02/cve-2026-96889-payload](https://github.com/anishadhikari02/cve-2026-96889-payload) : ![starts](https://img.shields.io/github/stars/anishadhikari02/cve-2026-96889-payload.svg) ![forks](https://img.shields.io/github/forks/anishadhikari02/cve-2026-96889-payload.svg)

## CVE-2026-98260
> In the Linux kernel, the following vulnerability has been resolved:

exec: Cleanup POSIX timers right after de_thread()

A per-thread CPU timer holds a reference to the PID of the thread it is
attached to and, while it is armed, its node is queued in that thread&#x27;s
posix_cputimers. The task is looked up by that PID.

When a non-leader thread exec()s, de_thread() changes which task owns
that PID. pid_task(timer-&gt;it.cpu.pid, PIDTYPE_PID) then returns NULL,
but the node is still queued on tsk, which

- [https://github.com/cuteaplane/opd2051example](https://github.com/cuteaplane/opd2051example) : ![starts](https://img.shields.io/github/stars/cuteaplane/opd2051example.svg) ![forks](https://img.shields.io/github/forks/cuteaplane/opd2051example.svg)

## CVE-2026-98432
> In the Linux kernel, the following vulnerability has been resolved:

ipv4: free inet_opt and ireq_opt after an RCU grace period

tcp_v4_syn_recv_sock() transfers ownership of ireq-&gt;ireq_opt to the
child socket (newinet-&gt;inet_opt) without copying it.

Another cpu can concurrently process a retransmitted SYN for the same
request socket, and send a SYNACK from tcp_check_req().
tcp_v4_send_synack() and inet_csk_route_req() read ireq-&gt;ireq_opt
under rcu_read_lock() only, and ip_build_and_send_pkt() a

- [https://github.com/jackykeung/CVE-2026-98432-Verified-Attack](https://github.com/jackykeung/CVE-2026-98432-Verified-Attack) : ![starts](https://img.shields.io/github/stars/jackykeung/CVE-2026-98432-Verified-Attack.svg) ![forks](https://img.shields.io/github/forks/jackykeung/CVE-2026-98432-Verified-Attack.svg)
