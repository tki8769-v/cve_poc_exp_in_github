# Update 2026-11-02
## CVE-2023-37474

- [https://github.com/0D00-0721-0/hdu-is-work1-copyparty-cve-2023-37474](https://github.com/0D00-0721-0/hdu-is-work1-copyparty-cve-2023-37474) : ![starts](https://img.shields.io/github/stars/0D00-0721-0/hdu-is-work1-copyparty-cve-2023-37474.svg) ![forks](https://img.shields.io/github/forks/0D00-0721-0/hdu-is-work1-copyparty-cve-2023-37474.svg)

## CVE-2024-48990

- [https://github.com/nekr0ff/needrestart-sudo-escalate-cve-2024-48990](https://github.com/nekr0ff/needrestart-sudo-escalate-cve-2024-48990) : ![starts](https://img.shields.io/github/stars/nekr0ff/needrestart-sudo-escalate-cve-2024-48990.svg) ![forks](https://img.shields.io/github/forks/nekr0ff/needrestart-sudo-escalate-cve-2024-48990.svg)

## CVE-2024-9264

- [https://github.com/ferralon-demo/grafana-cve-2024-9264-duckdb-rce](https://github.com/ferralon-demo/grafana-cve-2024-9264-duckdb-rce) : ![starts](https://img.shields.io/github/stars/ferralon-demo/grafana-cve-2024-9264-duckdb-rce.svg) ![forks](https://img.shields.io/github/forks/ferralon-demo/grafana-cve-2024-9264-duckdb-rce.svg)

## CVE-2025-24799

- [https://github.com/ryhnmhrdka/CVE-2025-24799](https://github.com/ryhnmhrdka/CVE-2025-24799) : ![starts](https://img.shields.io/github/stars/ryhnmhrdka/CVE-2025-24799.svg) ![forks](https://img.shields.io/github/forks/ryhnmhrdka/CVE-2025-24799.svg)

## CVE-2025-8110

- [https://github.com/godylockz/CVE-2025-8110](https://github.com/godylockz/CVE-2025-8110) : ![starts](https://img.shields.io/github/stars/godylockz/CVE-2025-8110.svg) ![forks](https://img.shields.io/github/forks/godylockz/CVE-2025-8110.svg)

## CVE-2026-109618
> PHP uses longjmp() for out-of-memory (OOM) errors to exit the current context and abort handling of the request. Some contexts may not properly account for this scenario and leave request memory in an uninitialized state before performing an allocation. The subsequent request cleanup procedure may read or branch on this memory. Multiple OOM strategies can consistently trigger this condition and lead to remote code execution (RCE).

- [https://github.com/godylockz/CVE-2026-109618-109619](https://github.com/godylockz/CVE-2026-109618-109619) : ![starts](https://img.shields.io/github/stars/godylockz/CVE-2026-109618-109619.svg) ![forks](https://img.shields.io/github/forks/godylockz/CVE-2026-109618-109619.svg)

## CVE-2026-111497
> A buffer overflow vulnerability in the Brotli decoder (c/dec/decode.c) in Google Brotli versions 1.0.3 through 1.2.0 on all platforms allows a remote unauthenticated attacker to corrupt adjacent decoder state memory, disclose sensitive memory contents, cause a denial of service, or potentially execute arbitrary code using a crafted Brotli-compressed stream.





Users need to update any Brotli libraries or binaries between 1.0.3 through 1.2.0 to the latest available version: 1.0.10 or 1.1.1 or 1

- [https://github.com/ChriSec7/CVE-2026-111497-POC](https://github.com/ChriSec7/CVE-2026-111497-POC) : ![starts](https://img.shields.io/github/stars/ChriSec7/CVE-2026-111497-POC.svg) ![forks](https://img.shields.io/github/forks/ChriSec7/CVE-2026-111497-POC.svg)
- [https://github.com/fieldse/http2shell-checker](https://github.com/fieldse/http2shell-checker) : ![starts](https://img.shields.io/github/stars/fieldse/http2shell-checker.svg) ![forks](https://img.shields.io/github/forks/fieldse/http2shell-checker.svg)

## CVE-2026-112816
> Improper certificate validation in the HTTPS listener in Canonical LXD 4.0.14, 5.0.10, 5.21.8, 6.9 before 4.0.15, 5.0.11, 5.21.9, 6.10.1 allows an unauthenticated attacker to authenticate as any trusted client and gain full access to the cluster and managed virtual machines via a crafted certificate chain.

- [https://github.com/foxcornlab/lxd-scanner](https://github.com/foxcornlab/lxd-scanner) : ![starts](https://img.shields.io/github/stars/foxcornlab/lxd-scanner.svg) ![forks](https://img.shields.io/github/forks/foxcornlab/lxd-scanner.svg)

## CVE-2026-14900

- [https://github.com/tenderacer-lgtm/CVE-2026-14900-PoC](https://github.com/tenderacer-lgtm/CVE-2026-14900-PoC) : ![starts](https://img.shields.io/github/stars/tenderacer-lgtm/CVE-2026-14900-PoC.svg) ![forks](https://img.shields.io/github/forks/tenderacer-lgtm/CVE-2026-14900-PoC.svg)

## CVE-2026-33186

- [https://github.com/basesixtythree/B63-POC-CVE-2026-33186](https://github.com/basesixtythree/B63-POC-CVE-2026-33186) : ![starts](https://img.shields.io/github/stars/basesixtythree/B63-POC-CVE-2026-33186.svg) ![forks](https://img.shields.io/github/forks/basesixtythree/B63-POC-CVE-2026-33186.svg)

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

- [https://github.com/tungmv/IONSTACK-S22E](https://github.com/tungmv/IONSTACK-S22E) : ![starts](https://img.shields.io/github/stars/tungmv/IONSTACK-S22E.svg) ![forks](https://img.shields.io/github/forks/tungmv/IONSTACK-S22E.svg)

## CVE-2026-53157

- [https://github.com/santoshkalluri/CVE-2026-53157](https://github.com/santoshkalluri/CVE-2026-53157) : ![starts](https://img.shields.io/github/stars/santoshkalluri/CVE-2026-53157.svg) ![forks](https://img.shields.io/github/forks/santoshkalluri/CVE-2026-53157.svg)

## CVE-2026-74583
> In the Linux kernel, the following vulnerability has been resolved:

net/sched: cls_route: fix fastmap use-after-free on filter

The route4 classifier maintains a 16-slot fastmap cache that stores raw
struct route4_filter pointers indexed by (id, iif). The reader
(route4_classify) populates this cache via route4_set_fastmap() for every
classified packet that hits a filter. The writer (route4_delete,
route4_change) clears the cache via route4_reset_fastmap() before
RCU-deferred kfree of the filte

- [https://github.com/santoshkalluri/CVE-2026-74583](https://github.com/santoshkalluri/CVE-2026-74583) : ![starts](https://img.shields.io/github/stars/santoshkalluri/CVE-2026-74583.svg) ![forks](https://img.shields.io/github/forks/santoshkalluri/CVE-2026-74583.svg)

## CVE-2026-88774
> Vulnerability in Citrix NetScaler ADC and Citrix NetScaler Gateway.

This issue affects ADC: before 14.1-73.37, before 13.1-64.23, before 14.1-73.37 FIPS, and before 13.1.37.279 FIPS and NDcPP; Gateway: before 14.1-73.37 and before 13.1-64.23 leading to a feature policy bypass due to improper HTTP URL based expression usage.

- [https://github.com/CompleteTech-Security/netscaler-cve-2026-88774-check](https://github.com/CompleteTech-Security/netscaler-cve-2026-88774-check) : ![starts](https://img.shields.io/github/stars/CompleteTech-Security/netscaler-cve-2026-88774-check.svg) ![forks](https://img.shields.io/github/forks/CompleteTech-Security/netscaler-cve-2026-88774-check.svg)

## CVE-2026-88775
> Memory overflow vulnerability in Citrix NetScaler ADC and Citrix NetScaler Gateway.

This issue affects ADC: before 14.1-73.37, before 13.1-64.23, before 14.1-73.37 FIPS, and before 13.1.37.279 FIPS and NDcPP; Gateway: before 14.1-73.37 and before 13.1-64.23 leading Memory overflow vulnerability leading to unpredictable or erroneous behavior or Denial of Service

- [https://github.com/CompleteTech-Security/netscaler-cve-2026-88775-check](https://github.com/CompleteTech-Security/netscaler-cve-2026-88775-check) : ![starts](https://img.shields.io/github/stars/CompleteTech-Security/netscaler-cve-2026-88775-check.svg) ![forks](https://img.shields.io/github/forks/CompleteTech-Security/netscaler-cve-2026-88775-check.svg)

## CVE-2026-88777
> Memory overflow vulnerability vulnerability in Citrix NetScaler ADC and Citrix NetScaler Gateway.

This issue affects ADC: before 14.1-73.37, before 13.1-64.23, before 14.1-73.37 FIPS, and before 13.1.37.279 FIPS and NDcPP; Gateway: before 14.1-73.37 and before 13.1-64.23  leading to unpredictable or erroneous behavior or Denial of Service

- [https://github.com/CompleteTech-Security/netscaler-cve-2026-88777-check](https://github.com/CompleteTech-Security/netscaler-cve-2026-88777-check) : ![starts](https://img.shields.io/github/stars/CompleteTech-Security/netscaler-cve-2026-88777-check.svg) ![forks](https://img.shields.io/github/forks/CompleteTech-Security/netscaler-cve-2026-88777-check.svg)

## CVE-2026-88778
> Predictable exact value from previous values vulnerability in Citrix NetScaler ADC and Citrix NetScaler Gateway.

This issue affects ADC: before 14.1-73.37, before 13.1-64.23, before 14.1-73.37 FIPS, and before 13.1.37.279 FIPS and NDcPP; Gateway: before 14.1-73.37 and before 13.1-64.23.

- [https://github.com/CompleteTech-Security/netscaler-cve-2026-88778-check](https://github.com/CompleteTech-Security/netscaler-cve-2026-88778-check) : ![starts](https://img.shields.io/github/stars/CompleteTech-Security/netscaler-cve-2026-88778-check.svg) ![forks](https://img.shields.io/github/forks/CompleteTech-Security/netscaler-cve-2026-88778-check.svg)

## CVE-2026-98260
> In the Linux kernel, the following vulnerability has been resolved:

exec: Cleanup POSIX timers right after de_thread()

A per-thread CPU timer holds a reference to the PID of the thread it is
attached to and, while it is armed, its node is queued in that thread&#x27;s
posix_cputimers. The task is looked up by that PID.

When a non-leader thread exec()s, de_thread() changes which task owns
that PID. pid_task(timer-&gt;it.cpu.pid, PIDTYPE_PID) then returns NULL,
but the node is still queued on tsk, which

- [https://github.com/yoro1836/SamTimer](https://github.com/yoro1836/SamTimer) : ![starts](https://img.shields.io/github/stars/yoro1836/SamTimer.svg) ![forks](https://img.shields.io/github/forks/yoro1836/SamTimer.svg)

## CVE-2026-98432
> In the Linux kernel, the following vulnerability has been resolved:

ipv4: free inet_opt and ireq_opt after an RCU grace period

tcp_v4_syn_recv_sock() transfers ownership of ireq-&gt;ireq_opt to the
child socket (newinet-&gt;inet_opt) without copying it.

Another cpu can concurrently process a retransmitted SYN for the same
request socket, and send a SYNACK from tcp_check_req().
tcp_v4_send_synack() and inet_csk_route_req() read ireq-&gt;ireq_opt
under rcu_read_lock() only, and ip_build_and_send_pkt() a

- [https://github.com/0xSpuddy/cve-2026-98432-check](https://github.com/0xSpuddy/cve-2026-98432-check) : ![starts](https://img.shields.io/github/stars/0xSpuddy/cve-2026-98432-check.svg) ![forks](https://img.shields.io/github/forks/0xSpuddy/cve-2026-98432-check.svg)
- [https://github.com/al4n4n/CVE-2026-98432](https://github.com/al4n4n/CVE-2026-98432) : ![starts](https://img.shields.io/github/stars/al4n4n/CVE-2026-98432.svg) ![forks](https://img.shields.io/github/forks/al4n4n/CVE-2026-98432.svg)
- [https://github.com/illuscapital/CVE-2026-98432](https://github.com/illuscapital/CVE-2026-98432) : ![starts](https://img.shields.io/github/stars/illuscapital/CVE-2026-98432.svg) ![forks](https://img.shields.io/github/forks/illuscapital/CVE-2026-98432.svg)
- [https://github.com/johnhsb/linux-tcp-uaf-cve-2026-98432](https://github.com/johnhsb/linux-tcp-uaf-cve-2026-98432) : ![starts](https://img.shields.io/github/stars/johnhsb/linux-tcp-uaf-cve-2026-98432.svg) ![forks](https://img.shields.io/github/forks/johnhsb/linux-tcp-uaf-cve-2026-98432.svg)
- [https://github.com/xxhjkl/cve-2026-98432-check](https://github.com/xxhjkl/cve-2026-98432-check) : ![starts](https://img.shields.io/github/stars/xxhjkl/cve-2026-98432-check.svg) ![forks](https://img.shields.io/github/forks/xxhjkl/cve-2026-98432-check.svg)
