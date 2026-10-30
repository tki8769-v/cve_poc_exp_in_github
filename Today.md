# Update 2026-10-30
## CVE-2023-23752

- [https://github.com/Charly-bite/SITEUR](https://github.com/Charly-bite/SITEUR) : ![starts](https://img.shields.io/github/stars/Charly-bite/SITEUR.svg) ![forks](https://img.shields.io/github/forks/Charly-bite/SITEUR.svg)

## CVE-2026-104286
> An improper limitation of a pathname to a restricted directory (&#x27;path traversal&#x27;) vulnerability in Fortinet FortiMail 8.0.0 through 8.0.1, FortiMail 7.6.0 through 7.6.6, FortiMail 7.4.0 through 7.4.8, FortiMail 7.2.0 through 7.2.9, FortiMail 7.0 all versions may allow an unauthenticated attacker to write arbitrary files on the underlying system via crafted HTTP or HTTPS requests.

- [https://github.com/CompleteTech-Security/fortimail-cve-2026-104286-check](https://github.com/CompleteTech-Security/fortimail-cve-2026-104286-check) : ![starts](https://img.shields.io/github/stars/CompleteTech-Security/fortimail-cve-2026-104286-check.svg) ![forks](https://img.shields.io/github/forks/CompleteTech-Security/fortimail-cve-2026-104286-check.svg)

## CVE-2026-105014

- [https://github.com/mehmet-emir-eroglu/CVE-2026-105014](https://github.com/mehmet-emir-eroglu/CVE-2026-105014) : ![starts](https://img.shields.io/github/stars/mehmet-emir-eroglu/CVE-2026-105014.svg) ![forks](https://img.shields.io/github/forks/mehmet-emir-eroglu/CVE-2026-105014.svg)

## CVE-2026-109618
> PHP uses longjmp() for out-of-memory (OOM) errors to exit the current context and abort handling of the request. Some contexts may not properly account for this scenario and leave request memory in an uninitialized state before performing an allocation. The subsequent request cleanup procedure may read or branch on this memory. Multiple OOM strategies can consistently trigger this condition and lead to remote code execution (RCE).

- [https://github.com/iliaal/php2shell](https://github.com/iliaal/php2shell) : ![starts](https://img.shields.io/github/stars/iliaal/php2shell.svg) ![forks](https://img.shields.io/github/forks/iliaal/php2shell.svg)

## CVE-2026-119025

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
