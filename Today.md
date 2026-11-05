# Update 2026-11-05
## CVE-2024-21626

- [https://github.com/GjerdanKashmiri/leakyvessels_reproduction_mitigation](https://github.com/GjerdanKashmiri/leakyvessels_reproduction_mitigation) : ![starts](https://img.shields.io/github/stars/GjerdanKashmiri/leakyvessels_reproduction_mitigation.svg) ![forks](https://img.shields.io/github/forks/GjerdanKashmiri/leakyvessels_reproduction_mitigation.svg)

## CVE-2024-47066

- [https://github.com/EQSTLab/CVE-2024-47066](https://github.com/EQSTLab/CVE-2024-47066) : ![starts](https://img.shields.io/github/stars/EQSTLab/CVE-2024-47066.svg) ![forks](https://img.shields.io/github/forks/EQSTLab/CVE-2024-47066.svg)

## CVE-2026-109518

- [https://github.com/Quaerendir/cve-2026-109518-audit](https://github.com/Quaerendir/cve-2026-109518-audit) : ![starts](https://img.shields.io/github/stars/Quaerendir/cve-2026-109518-audit.svg) ![forks](https://img.shields.io/github/forks/Quaerendir/cve-2026-109518-audit.svg)

## CVE-2026-109618
> PHP uses longjmp() for out-of-memory (OOM) errors to exit the current context and abort handling of the request. Some contexts may not properly account for this scenario and leave request memory in an uninitialized state before performing an allocation. The subsequent request cleanup procedure may read or branch on this memory. Multiple OOM strategies can consistently trigger this condition and lead to remote code execution (RCE).

- [https://github.com/sam00/CVE-2026-109618-CVE-2026-109619-POC](https://github.com/sam00/CVE-2026-109618-CVE-2026-109619-POC) : ![starts](https://img.shields.io/github/stars/sam00/CVE-2026-109618-CVE-2026-109619-POC.svg) ![forks](https://img.shields.io/github/forks/sam00/CVE-2026-109618-CVE-2026-109619-POC.svg)

## CVE-2026-109619
> PHP has various global state that temporarily points into request memory. In some scenarios, global state may not be correctly reset, or may be repopulated after being reset. The global state may then refer to request memory even after it has been freed. Subsequent requests may read or branch on this stale state before it is fully initialized. Multiple strategies can trigger this condition and produce remote code execution (RCE).

- [https://github.com/sam00/CVE-2026-109618-CVE-2026-109619-POC](https://github.com/sam00/CVE-2026-109618-CVE-2026-109619-POC) : ![starts](https://img.shields.io/github/stars/sam00/CVE-2026-109618-CVE-2026-109619-POC.svg) ![forks](https://img.shields.io/github/forks/sam00/CVE-2026-109618-CVE-2026-109619-POC.svg)

## CVE-2026-111497
> A buffer overflow vulnerability in the Brotli decoder (c/dec/decode.c) in Google Brotli versions 1.0.3 through 1.2.0 on all platforms allows a remote unauthenticated attacker to corrupt adjacent decoder state memory, disclose sensitive memory contents, cause a denial of service, or potentially execute arbitrary code using a crafted Brotli-compressed stream.





Users need to update any Brotli libraries or binaries between 1.0.3 through 1.2.0 to the latest available version: 1.0.10 or 1.1.1 or 1

- [https://github.com/aymenkmar/node2shell-check](https://github.com/aymenkmar/node2shell-check) : ![starts](https://img.shields.io/github/stars/aymenkmar/node2shell-check.svg) ![forks](https://img.shields.io/github/forks/aymenkmar/node2shell-check.svg)
- [https://github.com/sam00/Node2Shell-CVE-2026-111497-POC](https://github.com/sam00/Node2Shell-CVE-2026-111497-POC) : ![starts](https://img.shields.io/github/stars/sam00/Node2Shell-CVE-2026-111497-POC.svg) ![forks](https://img.shields.io/github/forks/sam00/Node2Shell-CVE-2026-111497-POC.svg)

## CVE-2026-111943
> On most platforms, Go uses the given system root certificates. However, in some narrower cases, the system trust stores may not be updated without further action. To defend against the narrower set of cases that may remain affected, a denylist was added in crypto/x509 to return an error when calling Verify with any of the known intermediate certificates that are no longer considered to be trustworthy.

- [https://github.com/sam00/CVE-2026-111943-Emudhra-Ca-Compromise-POC](https://github.com/sam00/CVE-2026-111943-Emudhra-Ca-Compromise-POC) : ![starts](https://img.shields.io/github/stars/sam00/CVE-2026-111943-Emudhra-Ca-Compromise-POC.svg) ![forks](https://img.shields.io/github/forks/sam00/CVE-2026-111943-Emudhra-Ca-Compromise-POC.svg)

## CVE-2026-97229
> GitLab has remediated an issue in GitLab CE/EE affecting all versions from 19.2 before 19.2.8, 19.3 before 19.3.5, and 19.4 before 19.4.2 that, under certain conditions, could have allowed an unauthenticated user to execute arbitrary code on the GitLab server via a specially crafted regular expression in a CI/CD configuration, due to insufficient regular expression validation.

- [https://github.com/Certbn/CVE-2026-97229-GitLab-CI-CD](https://github.com/Certbn/CVE-2026-97229-GitLab-CI-CD) : ![starts](https://img.shields.io/github/stars/Certbn/CVE-2026-97229-GitLab-CI-CD.svg) ![forks](https://img.shields.io/github/forks/Certbn/CVE-2026-97229-GitLab-CI-CD.svg)

## CVE-2026-98258
> In the Linux kernel, the following vulnerability has been resolved:

posix-cpu-timers: Prevent freeing a timer which is queued on the expiry list

Kijo analyzed another race in the POSIX CPU timer code:

Commit bf635681c906 converted cpu_timer::firing from a tristate value to a
boolean. This lost the distinction between &quot;not owned by the firing list&quot;
and &quot;still owned, but delivery was canceled&quot;. The resulting race is:

    expiry handler              timer_settime()        timer_delete()
    ---

- [https://github.com/imkidz0/Trilemma](https://github.com/imkidz0/Trilemma) : ![starts](https://img.shields.io/github/stars/imkidz0/Trilemma.svg) ![forks](https://img.shields.io/github/forks/imkidz0/Trilemma.svg)

## CVE-2026-98432
> In the Linux kernel, the following vulnerability has been resolved:

ipv4: free inet_opt and ireq_opt after an RCU grace period

tcp_v4_syn_recv_sock() transfers ownership of ireq-&gt;ireq_opt to the
child socket (newinet-&gt;inet_opt) without copying it.

Another cpu can concurrently process a retransmitted SYN for the same
request socket, and send a SYNACK from tcp_check_req().
tcp_v4_send_synack() and inet_csk_route_req() read ireq-&gt;ireq_opt
under rcu_read_lock() only, and ip_build_and_send_pkt() a

- [https://github.com/Certbn/CVE-2026-98432-Linux-IPv4-TCP-IP-Use-After-Free](https://github.com/Certbn/CVE-2026-98432-Linux-IPv4-TCP-IP-Use-After-Free) : ![starts](https://img.shields.io/github/stars/Certbn/CVE-2026-98432-Linux-IPv4-TCP-IP-Use-After-Free.svg) ![forks](https://img.shields.io/github/forks/Certbn/CVE-2026-98432-Linux-IPv4-TCP-IP-Use-After-Free.svg)
- [https://github.com/moatome/CVE-2026-98432-pen-test-main](https://github.com/moatome/CVE-2026-98432-pen-test-main) : ![starts](https://img.shields.io/github/stars/moatome/CVE-2026-98432-pen-test-main.svg) ![forks](https://img.shields.io/github/forks/moatome/CVE-2026-98432-pen-test-main.svg)
