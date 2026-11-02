# Update 2026-11-02
## CVE-2024-48990

- [https://github.com/nekr0ff/needrestart-sudo-escalate-cve-2024-48990](https://github.com/nekr0ff/needrestart-sudo-escalate-cve-2024-48990) : ![starts](https://img.shields.io/github/stars/nekr0ff/needrestart-sudo-escalate-cve-2024-48990.svg) ![forks](https://img.shields.io/github/forks/nekr0ff/needrestart-sudo-escalate-cve-2024-48990.svg)

## CVE-2024-9264

- [https://github.com/ferralon-demo/grafana-cve-2024-9264-duckdb-rce](https://github.com/ferralon-demo/grafana-cve-2024-9264-duckdb-rce) : ![starts](https://img.shields.io/github/stars/ferralon-demo/grafana-cve-2024-9264-duckdb-rce.svg) ![forks](https://img.shields.io/github/forks/ferralon-demo/grafana-cve-2024-9264-duckdb-rce.svg)

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

- [https://github.com/al4n4n/CVE-2026-98432](https://github.com/al4n4n/CVE-2026-98432) : ![starts](https://img.shields.io/github/stars/al4n4n/CVE-2026-98432.svg) ![forks](https://img.shields.io/github/forks/al4n4n/CVE-2026-98432.svg)
- [https://github.com/illuscapital/CVE-2026-98432](https://github.com/illuscapital/CVE-2026-98432) : ![starts](https://img.shields.io/github/stars/illuscapital/CVE-2026-98432.svg) ![forks](https://img.shields.io/github/forks/illuscapital/CVE-2026-98432.svg)
