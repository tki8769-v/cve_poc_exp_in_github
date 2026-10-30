# Update 2026-10-30
## CVE-2023-23752

- [https://github.com/Charly-bite/SITEUR](https://github.com/Charly-bite/SITEUR) : ![starts](https://img.shields.io/github/stars/Charly-bite/SITEUR.svg) ![forks](https://img.shields.io/github/forks/Charly-bite/SITEUR.svg)

## CVE-2024-33224

- [https://github.com/Wacatac600/rtkio-memory-dump-poc](https://github.com/Wacatac600/rtkio-memory-dump-poc) : ![starts](https://img.shields.io/github/stars/Wacatac600/rtkio-memory-dump-poc.svg) ![forks](https://img.shields.io/github/forks/Wacatac600/rtkio-memory-dump-poc.svg)

## CVE-2026-102255
> A Pre-authentication SSRF vulnerability exists in the SMA1000 Appliance Work Place interface due to an unintended alternate access path. By abusing this path, a remote unauthenticated attacker could potentially exploit this vulnerability to direct the appliance to issue requests on their behalf and reach internal functionality and perform unauthorized operations.

- [https://github.com/CompleteTech-Security/sonicwall-sma1000-cve-2026-102255-check](https://github.com/CompleteTech-Security/sonicwall-sma1000-cve-2026-102255-check) : ![starts](https://img.shields.io/github/stars/CompleteTech-Security/sonicwall-sma1000-cve-2026-102255-check.svg) ![forks](https://img.shields.io/github/forks/CompleteTech-Security/sonicwall-sma1000-cve-2026-102255-check.svg)

## CVE-2026-102258
> Post-authentication Stored Cross-Site Scripting (XSS) vulnerability has been identified in the SMA1000 Appliance Management Console (AMC) which in specific conditions could potentially enable a remote authenticated attacker as administrator to store and potentially execute arbitrary JavaScript code in the Appliance Management Console (AMC).

- [https://github.com/CompleteTech-Security/sonicwall-sma1000-cve-2026-102258-check](https://github.com/CompleteTech-Security/sonicwall-sma1000-cve-2026-102258-check) : ![starts](https://img.shields.io/github/stars/CompleteTech-Security/sonicwall-sma1000-cve-2026-102258-check.svg) ![forks](https://img.shields.io/github/forks/CompleteTech-Security/sonicwall-sma1000-cve-2026-102258-check.svg)

## CVE-2026-104286
> An improper limitation of a pathname to a restricted directory (&#x27;path traversal&#x27;) vulnerability in Fortinet FortiMail 8.0.0 through 8.0.1, FortiMail 7.6.0 through 7.6.6, FortiMail 7.4.0 through 7.4.8, FortiMail 7.2.0 through 7.2.9, FortiMail 7.0 all versions may allow an unauthenticated attacker to write arbitrary files on the underlying system via crafted HTTP or HTTPS requests.

- [https://github.com/CompleteTech-Security/fortimail-cve-2026-104286-check](https://github.com/CompleteTech-Security/fortimail-cve-2026-104286-check) : ![starts](https://img.shields.io/github/stars/CompleteTech-Security/fortimail-cve-2026-104286-check.svg) ![forks](https://img.shields.io/github/forks/CompleteTech-Security/fortimail-cve-2026-104286-check.svg)

## CVE-2026-105014

- [https://github.com/mehmet-emir-eroglu/CVE-2026-105014](https://github.com/mehmet-emir-eroglu/CVE-2026-105014) : ![starts](https://img.shields.io/github/stars/mehmet-emir-eroglu/CVE-2026-105014.svg) ![forks](https://img.shields.io/github/forks/mehmet-emir-eroglu/CVE-2026-105014.svg)

## CVE-2026-109618
> PHP uses longjmp() for out-of-memory (OOM) errors to exit the current context and abort handling of the request. Some contexts may not properly account for this scenario and leave request memory in an uninitialized state before performing an allocation. The subsequent request cleanup procedure may read or branch on this memory. Multiple OOM strategies can consistently trigger this condition and lead to remote code execution (RCE).

- [https://github.com/ArchonXDeadLocksecurity/ArchonX-PHP2Shell](https://github.com/ArchonXDeadLocksecurity/ArchonX-PHP2Shell) : ![starts](https://img.shields.io/github/stars/ArchonXDeadLocksecurity/ArchonX-PHP2Shell.svg) ![forks](https://img.shields.io/github/forks/ArchonXDeadLocksecurity/ArchonX-PHP2Shell.svg)
- [https://github.com/iliaal/php2shell](https://github.com/iliaal/php2shell) : ![starts](https://img.shields.io/github/stars/iliaal/php2shell.svg) ![forks](https://img.shields.io/github/forks/iliaal/php2shell.svg)

## CVE-2026-110063

- [https://github.com/mehmet-emir-eroglu/CVE-2026-110063](https://github.com/mehmet-emir-eroglu/CVE-2026-110063) : ![starts](https://img.shields.io/github/stars/mehmet-emir-eroglu/CVE-2026-110063.svg) ![forks](https://img.shields.io/github/forks/mehmet-emir-eroglu/CVE-2026-110063.svg)

## CVE-2026-110912
> In DragonFly BSD through 6.4.2 before 4bb22ff, the ARP input handlers arpintr() and in_arpinput() (sys/netinet/if_ether.c) do not validate the hardware address length (ar_hln) and protocol address length (ar_pln) fields of incoming ARP packets. in_arpreply() then uses these attacker-controlled values as memcpy lengths when copying from kernel buffers that are only 6 and 4 bytes long, resulting in an out-of-bounds read of kernel heap and stack memory that is copied into the ARP reply sent back to

- [https://github.com/0xredash/CVE-2026-110912](https://github.com/0xredash/CVE-2026-110912) : ![starts](https://img.shields.io/github/stars/0xredash/CVE-2026-110912.svg) ![forks](https://img.shields.io/github/forks/0xredash/CVE-2026-110912.svg)

## CVE-2026-111497
> A buffer overflow vulnerability in the Brotli decoder (c/dec/decode.c) in Google Brotli versions 1.0.3 through 1.2.0 on all platforms allows a remote unauthenticated attacker to corrupt adjacent decoder state memory, disclose sensitive memory contents, cause a denial of service, or potentially execute arbitrary code using a crafted Brotli-compressed stream.





Users need to update any Brotli libraries or binaries between 1.0.3 through 1.2.0 to the latest available version: 1.0.10 or 1.1.1 or 1

- [https://github.com/0xredash/CVE-2026-111497](https://github.com/0xredash/CVE-2026-111497) : ![starts](https://img.shields.io/github/stars/0xredash/CVE-2026-111497.svg) ![forks](https://img.shields.io/github/forks/0xredash/CVE-2026-111497.svg)
- [https://github.com/CompleteTech-Security/http2shell-check](https://github.com/CompleteTech-Security/http2shell-check) : ![starts](https://img.shields.io/github/stars/CompleteTech-Security/http2shell-check.svg) ![forks](https://img.shields.io/github/forks/CompleteTech-Security/http2shell-check.svg)
- [https://github.com/CompleteTech-Security/node2shell-check](https://github.com/CompleteTech-Security/node2shell-check) : ![starts](https://img.shields.io/github/stars/CompleteTech-Security/node2shell-check.svg) ![forks](https://img.shields.io/github/forks/CompleteTech-Security/node2shell-check.svg)
- [https://github.com/amier-ge/Node2Shell](https://github.com/amier-ge/Node2Shell) : ![starts](https://img.shields.io/github/stars/amier-ge/Node2Shell.svg) ![forks](https://img.shields.io/github/forks/amier-ge/Node2Shell.svg)
- [https://github.com/mehmet-emir-eroglu/CVE-2026-111497](https://github.com/mehmet-emir-eroglu/CVE-2026-111497) : ![starts](https://img.shields.io/github/stars/mehmet-emir-eroglu/CVE-2026-111497.svg) ![forks](https://img.shields.io/github/forks/mehmet-emir-eroglu/CVE-2026-111497.svg)
- [https://github.com/miracle438/node2shell-two-stage](https://github.com/miracle438/node2shell-two-stage) : ![starts](https://img.shields.io/github/stars/miracle438/node2shell-two-stage.svg) ![forks](https://img.shields.io/github/forks/miracle438/node2shell-two-stage.svg)

## CVE-2026-114509
> Laravel is a web application framework. Prior to 12.68.0 and 13.29.0, TokenGuard configured as a standard token-based API guard does not reject a crafted non-string credential. Under affected MySQL or MariaDB configurations, the authentication lookup can match an unintended existing user, allowing an unauthenticated attacker to bypass authentication and take over an account on routes protected by TokenGuard. This issue is fixed in versions 12.68.0 and 13.29.0.

- [https://github.com/mehmet-emir-eroglu/CVE-2026-114509](https://github.com/mehmet-emir-eroglu/CVE-2026-114509) : ![starts](https://img.shields.io/github/stars/mehmet-emir-eroglu/CVE-2026-114509.svg) ![forks](https://img.shields.io/github/forks/mehmet-emir-eroglu/CVE-2026-114509.svg)

## CVE-2026-119025
> open 7.2.0 before 11.0.0 contains an OS command injection vulnerability that allows attackers to execute PowerShell code by supplying crafted URLs on Windows and WSL. Attackers can embed $(...) subexpressions in URLs, such as OAuth authorization_endpoint values from malicious MCP servers, which execute when index.js passes them unescaped to powershell -EncodedCommand.

- [https://github.com/shouvikkkk/oauth-sink-check](https://github.com/shouvikkkk/oauth-sink-check) : ![starts](https://img.shields.io/github/stars/shouvikkkk/oauth-sink-check.svg) ![forks](https://img.shields.io/github/forks/shouvikkkk/oauth-sink-check.svg)

## CVE-2026-12485

- [https://github.com/0xredash/CVE-2026-12485](https://github.com/0xredash/CVE-2026-12485) : ![starts](https://img.shields.io/github/stars/0xredash/CVE-2026-12485.svg) ![forks](https://img.shields.io/github/forks/0xredash/CVE-2026-12485.svg)

## CVE-2026-6471

- [https://github.com/0xredash/CVE-2026-6471](https://github.com/0xredash/CVE-2026-6471) : ![starts](https://img.shields.io/github/stars/0xredash/CVE-2026-6471.svg) ![forks](https://img.shields.io/github/forks/0xredash/CVE-2026-6471.svg)

## CVE-2026-98432
> In the Linux kernel, the following vulnerability has been resolved:

ipv4: free inet_opt and ireq_opt after an RCU grace period

tcp_v4_syn_recv_sock() transfers ownership of ireq-&gt;ireq_opt to the
child socket (newinet-&gt;inet_opt) without copying it.

Another cpu can concurrently process a retransmitted SYN for the same
request socket, and send a SYNACK from tcp_check_req().
tcp_v4_send_synack() and inet_csk_route_req() read ireq-&gt;ireq_opt
under rcu_read_lock() only, and ip_build_and_send_pkt() a

- [https://github.com/H1z3-br0/CVE-2026-98432](https://github.com/H1z3-br0/CVE-2026-98432) : ![starts](https://img.shields.io/github/stars/H1z3-br0/CVE-2026-98432.svg) ![forks](https://img.shields.io/github/forks/H1z3-br0/CVE-2026-98432.svg)
- [https://github.com/fbuff-tools/cve-2026-98432-checker](https://github.com/fbuff-tools/cve-2026-98432-checker) : ![starts](https://img.shields.io/github/stars/fbuff-tools/cve-2026-98432-checker.svg) ![forks](https://img.shields.io/github/forks/fbuff-tools/cve-2026-98432-checker.svg)
- [https://github.com/mahdi-salmanzade/CVE-2026-98432](https://github.com/mahdi-salmanzade/CVE-2026-98432) : ![starts](https://img.shields.io/github/stars/mahdi-salmanzade/CVE-2026-98432.svg) ![forks](https://img.shields.io/github/forks/mahdi-salmanzade/CVE-2026-98432.svg)
- [https://github.com/maxigentr/netviser-linux-security-auditor](https://github.com/maxigentr/netviser-linux-security-auditor) : ![starts](https://img.shields.io/github/stars/maxigentr/netviser-linux-security-auditor.svg) ![forks](https://img.shields.io/github/forks/maxigentr/netviser-linux-security-auditor.svg)
- [https://github.com/scriptzteam/Paranoid-CVE-2026-98432](https://github.com/scriptzteam/Paranoid-CVE-2026-98432) : ![starts](https://img.shields.io/github/stars/scriptzteam/Paranoid-CVE-2026-98432.svg) ![forks](https://img.shields.io/github/forks/scriptzteam/Paranoid-CVE-2026-98432.svg)
