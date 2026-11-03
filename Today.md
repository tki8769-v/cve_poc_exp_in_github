# Update 2026-11-03
## CVE-2019-15107

- [https://github.com/r3vpwnx/Webmin-1.910-Exploit-Script](https://github.com/r3vpwnx/Webmin-1.910-Exploit-Script) : ![starts](https://img.shields.io/github/stars/r3vpwnx/Webmin-1.910-Exploit-Script.svg) ![forks](https://img.shields.io/github/forks/r3vpwnx/Webmin-1.910-Exploit-Script.svg)

## CVE-2024-38998

- [https://github.com/c4bsec/PP_CVE-2024-38998](https://github.com/c4bsec/PP_CVE-2024-38998) : ![starts](https://img.shields.io/github/stars/c4bsec/PP_CVE-2024-38998.svg) ![forks](https://img.shields.io/github/forks/c4bsec/PP_CVE-2024-38998.svg)

## CVE-2025-32433

- [https://github.com/Avinash37402/CVE-2025-32433](https://github.com/Avinash37402/CVE-2025-32433) : ![starts](https://img.shields.io/github/stars/Avinash37402/CVE-2025-32433.svg) ![forks](https://img.shields.io/github/forks/Avinash37402/CVE-2025-32433.svg)
- [https://github.com/Avinash37402/CVE-2025-32433-Erlang-OTP-SSH](https://github.com/Avinash37402/CVE-2025-32433-Erlang-OTP-SSH) : ![starts](https://img.shields.io/github/stars/Avinash37402/CVE-2025-32433-Erlang-OTP-SSH.svg) ![forks](https://img.shields.io/github/forks/Avinash37402/CVE-2025-32433-Erlang-OTP-SSH.svg)

## CVE-2025-41450
> Improper Authentication vulnerability in Danfoss AKSM8xxA Series.This issue affects Danfoss AK-SM 8xxA Series prior to version 4.2

- [https://github.com/GabrieleDattile/CVE-2025-41450-Fromagegate](https://github.com/GabrieleDattile/CVE-2025-41450-Fromagegate) : ![starts](https://img.shields.io/github/stars/GabrieleDattile/CVE-2025-41450-Fromagegate.svg) ![forks](https://img.shields.io/github/forks/GabrieleDattile/CVE-2025-41450-Fromagegate.svg)

## CVE-2026-33439

- [https://github.com/stapat1245/CVE-2026-33439_poc](https://github.com/stapat1245/CVE-2026-33439_poc) : ![starts](https://img.shields.io/github/stars/stapat1245/CVE-2026-33439_poc.svg) ![forks](https://img.shields.io/github/forks/stapat1245/CVE-2026-33439_poc.svg)

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

- [https://github.com/Delta-Water/phq110-root](https://github.com/Delta-Water/phq110-root) : ![starts](https://img.shields.io/github/stars/Delta-Water/phq110-root.svg) ![forks](https://img.shields.io/github/forks/Delta-Water/phq110-root.svg)

## CVE-2026-62911

- [https://github.com/c5z54/cve-2026-62911-poc](https://github.com/c5z54/cve-2026-62911-poc) : ![starts](https://img.shields.io/github/stars/c5z54/cve-2026-62911-poc.svg) ![forks](https://img.shields.io/github/forks/c5z54/cve-2026-62911-poc.svg)

## CVE-2026-86596

- [https://github.com/thiscitze/cve-2026-86596-poc](https://github.com/thiscitze/cve-2026-86596-poc) : ![starts](https://img.shields.io/github/stars/thiscitze/cve-2026-86596-poc.svg) ![forks](https://img.shields.io/github/forks/thiscitze/cve-2026-86596-poc.svg)

## CVE-2026-98260
> In the Linux kernel, the following vulnerability has been resolved:

exec: Cleanup POSIX timers right after de_thread()

A per-thread CPU timer holds a reference to the PID of the thread it is
attached to and, while it is armed, its node is queued in that thread&#x27;s
posix_cputimers. The task is looked up by that PID.

When a non-leader thread exec()s, de_thread() changes which task owns
that PID. pid_task(timer-&gt;it.cpu.pid, PIDTYPE_PID) then returns NULL,
but the node is still queued on tsk, which

- [https://github.com/YodonTan/cve-2026-98260-harmonyos-applicability](https://github.com/YodonTan/cve-2026-98260-harmonyos-applicability) : ![starts](https://img.shields.io/github/stars/YodonTan/cve-2026-98260-harmonyos-applicability.svg) ![forks](https://img.shields.io/github/forks/YodonTan/cve-2026-98260-harmonyos-applicability.svg)

## CVE-2026-98432
> In the Linux kernel, the following vulnerability has been resolved:

ipv4: free inet_opt and ireq_opt after an RCU grace period

tcp_v4_syn_recv_sock() transfers ownership of ireq-&gt;ireq_opt to the
child socket (newinet-&gt;inet_opt) without copying it.

Another cpu can concurrently process a retransmitted SYN for the same
request socket, and send a SYNACK from tcp_check_req().
tcp_v4_send_synack() and inet_csk_route_req() read ireq-&gt;ireq_opt
under rcu_read_lock() only, and ip_build_and_send_pkt() a

- [https://github.com/GarphenGate/cve-2026-98432-defender-toolkit](https://github.com/GarphenGate/cve-2026-98432-defender-toolkit) : ![starts](https://img.shields.io/github/stars/GarphenGate/cve-2026-98432-defender-toolkit.svg) ![forks](https://img.shields.io/github/forks/GarphenGate/cve-2026-98432-defender-toolkit.svg)
- [https://github.com/IgrekLg/cve-2026-98432-mitigation](https://github.com/IgrekLg/cve-2026-98432-mitigation) : ![starts](https://img.shields.io/github/stars/IgrekLg/cve-2026-98432-mitigation.svg) ![forks](https://img.shields.io/github/forks/IgrekLg/cve-2026-98432-mitigation.svg)
- [https://github.com/lowerpower/cve-2026-98432-mitigation](https://github.com/lowerpower/cve-2026-98432-mitigation) : ![starts](https://img.shields.io/github/stars/lowerpower/cve-2026-98432-mitigation.svg) ![forks](https://img.shields.io/github/forks/lowerpower/cve-2026-98432-mitigation.svg)
