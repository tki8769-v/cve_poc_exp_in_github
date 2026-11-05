# Update 2026-11-05
## CVE-2017-18349

- [https://github.com/dichen-L/CVE-2017-18349-fastjson1.2.24-vul](https://github.com/dichen-L/CVE-2017-18349-fastjson1.2.24-vul) : ![starts](https://img.shields.io/github/stars/dichen-L/CVE-2017-18349-fastjson1.2.24-vul.svg) ![forks](https://img.shields.io/github/forks/dichen-L/CVE-2017-18349-fastjson1.2.24-vul.svg)

## CVE-2017-7921

- [https://github.com/Mr-Ochobot/Hikvision-CCTV-POC](https://github.com/Mr-Ochobot/Hikvision-CCTV-POC) : ![starts](https://img.shields.io/github/stars/Mr-Ochobot/Hikvision-CCTV-POC.svg) ![forks](https://img.shields.io/github/forks/Mr-Ochobot/Hikvision-CCTV-POC.svg)

## CVE-2018-20062

- [https://github.com/0xRar/ThinkPHP5_RCE](https://github.com/0xRar/ThinkPHP5_RCE) : ![starts](https://img.shields.io/github/stars/0xRar/ThinkPHP5_RCE.svg) ![forks](https://img.shields.io/github/forks/0xRar/ThinkPHP5_RCE.svg)

## CVE-2021-44228

- [https://github.com/Certbn/CVE-2021-44228-Apache-Log4j2-JNDI-Lookup](https://github.com/Certbn/CVE-2021-44228-Apache-Log4j2-JNDI-Lookup) : ![starts](https://img.shields.io/github/stars/Certbn/CVE-2021-44228-Apache-Log4j2-JNDI-Lookup.svg) ![forks](https://img.shields.io/github/forks/Certbn/CVE-2021-44228-Apache-Log4j2-JNDI-Lookup.svg)

## CVE-2024-21626

- [https://github.com/GjerdanKashmiri/leakyvessels_reproduction_mitigation](https://github.com/GjerdanKashmiri/leakyvessels_reproduction_mitigation) : ![starts](https://img.shields.io/github/stars/GjerdanKashmiri/leakyvessels_reproduction_mitigation.svg) ![forks](https://img.shields.io/github/forks/GjerdanKashmiri/leakyvessels_reproduction_mitigation.svg)

## CVE-2024-47066

- [https://github.com/EQSTLab/CVE-2024-47066](https://github.com/EQSTLab/CVE-2024-47066) : ![starts](https://img.shields.io/github/stars/EQSTLab/CVE-2024-47066.svg) ![forks](https://img.shields.io/github/forks/EQSTLab/CVE-2024-47066.svg)

## CVE-2026-107441
> An out-of-bounds write vulnerability in the CGI program of Zyxel GS1900-24E firmware versions through 2.90(AAHK.2)C0 could allow an unauthenticated adjacent attacker  to exploit the flaw and potentially execute OS commands via a crafted HTTP request.

- [https://github.com/foxcornlab/zyxel-gs1900-scanner](https://github.com/foxcornlab/zyxel-gs1900-scanner) : ![starts](https://img.shields.io/github/stars/foxcornlab/zyxel-gs1900-scanner.svg) ![forks](https://img.shields.io/github/forks/foxcornlab/zyxel-gs1900-scanner.svg)

## CVE-2026-109518
> On Debian, Ubuntu, and derivative Linux distributions, an on-path attacker who can manipulate the HTTP traffic (including a malicious mirror or proxy) between an APT client and an archive server triggered by a package install can trick the client into installing an attacker-controlled unverified package and achieve remote code execution with root privileges.



The vulnerability is caused by the reuse of hard links and requires the client to follow redirects and retry the download of package fil

- [https://github.com/Quaerendir/cve-2026-109518-audit](https://github.com/Quaerendir/cve-2026-109518-audit) : ![starts](https://img.shields.io/github/stars/Quaerendir/cve-2026-109518-audit.svg) ![forks](https://img.shields.io/github/forks/Quaerendir/cve-2026-109518-audit.svg)

## CVE-2026-109618
> PHP uses longjmp() for out-of-memory (OOM) errors to exit the current context and abort handling of the request. Some contexts may not properly account for this scenario and leave request memory in an uninitialized state before performing an allocation. The subsequent request cleanup procedure may read or branch on this memory. Multiple OOM strategies can consistently trigger this condition and lead to remote code execution (RCE).

- [https://github.com/D-1P1X/php2shell-web](https://github.com/D-1P1X/php2shell-web) : ![starts](https://img.shields.io/github/stars/D-1P1X/php2shell-web.svg) ![forks](https://img.shields.io/github/forks/D-1P1X/php2shell-web.svg)
- [https://github.com/Nebur692/php-legacy-ubuntu](https://github.com/Nebur692/php-legacy-ubuntu) : ![starts](https://img.shields.io/github/stars/Nebur692/php-legacy-ubuntu.svg) ![forks](https://img.shields.io/github/forks/Nebur692/php-legacy-ubuntu.svg)
- [https://github.com/sam00/CVE-2026-109618-CVE-2026-109619-POC](https://github.com/sam00/CVE-2026-109618-CVE-2026-109619-POC) : ![starts](https://img.shields.io/github/stars/sam00/CVE-2026-109618-CVE-2026-109619-POC.svg) ![forks](https://img.shields.io/github/forks/sam00/CVE-2026-109618-CVE-2026-109619-POC.svg)

## CVE-2026-109619
> PHP has various global state that temporarily points into request memory. In some scenarios, global state may not be correctly reset, or may be repopulated after being reset. The global state may then refer to request memory even after it has been freed. Subsequent requests may read or branch on this stale state before it is fully initialized. Multiple strategies can trigger this condition and produce remote code execution (RCE).

- [https://github.com/blkph0x/CVE-2026-109619-ZendPipelineLab](https://github.com/blkph0x/CVE-2026-109619-ZendPipelineLab) : ![starts](https://img.shields.io/github/stars/blkph0x/CVE-2026-109619-ZendPipelineLab.svg) ![forks](https://img.shields.io/github/forks/blkph0x/CVE-2026-109619-ZendPipelineLab.svg)
- [https://github.com/sam00/CVE-2026-109618-CVE-2026-109619-POC](https://github.com/sam00/CVE-2026-109618-CVE-2026-109619-POC) : ![starts](https://img.shields.io/github/stars/sam00/CVE-2026-109618-CVE-2026-109619-POC.svg) ![forks](https://img.shields.io/github/forks/sam00/CVE-2026-109618-CVE-2026-109619-POC.svg)

## CVE-2026-111497
> A buffer overflow vulnerability in the Brotli decoder (c/dec/decode.c) in Google Brotli versions 1.0.3 through 1.2.0 on all platforms allows a remote unauthenticated attacker to corrupt adjacent decoder state memory, disclose sensitive memory contents, cause a denial of service, or potentially execute arbitrary code using a crafted Brotli-compressed stream.





Users need to update any Brotli libraries or binaries between 1.0.3 through 1.2.0 to the latest available version: 1.0.10 or 1.1.1 or 1

- [https://github.com/aymenkmar/node2shell-check](https://github.com/aymenkmar/node2shell-check) : ![starts](https://img.shields.io/github/stars/aymenkmar/node2shell-check.svg) ![forks](https://img.shields.io/github/forks/aymenkmar/node2shell-check.svg)
- [https://github.com/sam00/Node2Shell-CVE-2026-111497-POC](https://github.com/sam00/Node2Shell-CVE-2026-111497-POC) : ![starts](https://img.shields.io/github/stars/sam00/Node2Shell-CVE-2026-111497-POC.svg) ![forks](https://img.shields.io/github/forks/sam00/Node2Shell-CVE-2026-111497-POC.svg)

## CVE-2026-111943
> On most platforms, Go uses the given system root certificates. However, in some narrower cases, the system trust stores may not be updated without further action. To defend against the narrower set of cases that may remain affected, a denylist was added in crypto/x509 to return an error when calling Verify with any of the known intermediate certificates that are no longer considered to be trustworthy.

- [https://github.com/sam00/CVE-2026-111943-Emudhra-Ca-Compromise-POC](https://github.com/sam00/CVE-2026-111943-Emudhra-Ca-Compromise-POC) : ![starts](https://img.shields.io/github/stars/sam00/CVE-2026-111943-Emudhra-Ca-Compromise-POC.svg) ![forks](https://img.shields.io/github/forks/sam00/CVE-2026-111943-Emudhra-Ca-Compromise-POC.svg)

## CVE-2026-114550
> libwebsockets MQTT Protocol PUBACK Packet Handling Out-Of-Bounds Write Remote Code Execution Vulnerability. This vulnerability allows remote attackers to execute arbitrary code on affected installations of libwebsockets. Authentication is not required to exploit this vulnerability.

The specific flaw exists within the handling of PUBACK packets. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated buffer. An attacker

- [https://github.com/googlesky/CVE-2026-114550](https://github.com/googlesky/CVE-2026-114550) : ![starts](https://img.shields.io/github/stars/googlesky/CVE-2026-114550.svg) ![forks](https://img.shields.io/github/forks/googlesky/CVE-2026-114550.svg)

## CVE-2026-115290
> Uncontrolled Recursion (CWE-674) in Elasticsearch can lead to denial of service via Serialized Data with Nested Payloads (CAPEC-230). An unauthenticated attacker with network access to the remote cluster server interface of a node can send a specially crafted request that causes the node to terminate. No credentials are required. The attacker can repeat the request against each reachable node.

- [https://github.com/googlesky/CVE-2026-115290](https://github.com/googlesky/CVE-2026-115290) : ![starts](https://img.shields.io/github/stars/googlesky/CVE-2026-115290.svg) ![forks](https://img.shields.io/github/forks/googlesky/CVE-2026-115290.svg)

## CVE-2026-116512
> The Project Manager – AI Powered Project Management, Task Management, Kanban Board &amp; Time Tracker plugin for WordPress is vulnerable to Remote Code Execution in all versions up to, and including, 4.1.1 via the &#x27;id&#x27; parameter parameter. This is due to unsanitized &#x27;id&#x27; parameter value concatenated directly into the pipe-delimited validation rule string, which is then split and each token invoked as a dynamic PHP function with no allowlist check. This makes it possible for unauthenticated attackers

- [https://github.com/Mushr00w/CVE-2026-116512](https://github.com/Mushr00w/CVE-2026-116512) : ![starts](https://img.shields.io/github/stars/Mushr00w/CVE-2026-116512.svg) ![forks](https://img.shields.io/github/forks/Mushr00w/CVE-2026-116512.svg)

## CVE-2026-120232
> A vulnerability was identified in Horizon DataSys Reboot Restore Standard up to 13.2. The impacted element is the function sub_23908 in the library shield.sys of the component Kernel Driver. Such manipulation leads to memory corruption. The attack can only be performed from a local environment. The exploit is publicly available and might be used. A fix is planned for the upcoming release.

- [https://github.com/Element2023H/CVE-2026-120232-RUST-POC](https://github.com/Element2023H/CVE-2026-120232-RUST-POC) : ![starts](https://img.shields.io/github/stars/Element2023H/CVE-2026-120232-RUST-POC.svg) ![forks](https://img.shields.io/github/forks/Element2023H/CVE-2026-120232-RUST-POC.svg)

## CVE-2026-122006
> The activestorage gem before 8.1.4.1 for Ruby on Rails, when ImageMagick attachment processing occurs, can allow server read and write operations (e.g., reading secret_key_base) because the ImageMagick analyzer runs when a file is attached, and there is not an ImageMagick security policy to block unintended functionality.

- [https://github.com/charlie-goldenowl/cve-2026-122006-check](https://github.com/charlie-goldenowl/cve-2026-122006-check) : ![starts](https://img.shields.io/github/stars/charlie-goldenowl/cve-2026-122006-check.svg) ![forks](https://img.shields.io/github/forks/charlie-goldenowl/cve-2026-122006-check.svg)

## CVE-2026-122051

- [https://github.com/carterlasalle/CVE-2026-122051](https://github.com/carterlasalle/CVE-2026-122051) : ![starts](https://img.shields.io/github/stars/carterlasalle/CVE-2026-122051.svg) ![forks](https://img.shields.io/github/forks/carterlasalle/CVE-2026-122051.svg)

## CVE-2026-18470

- [https://github.com/0xg33k/CVE-2026-18470](https://github.com/0xg33k/CVE-2026-18470) : ![starts](https://img.shields.io/github/stars/0xg33k/CVE-2026-18470.svg) ![forks](https://img.shields.io/github/forks/0xg33k/CVE-2026-18470.svg)

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

- [https://github.com/thedavidweng/ghostlock-z3q](https://github.com/thedavidweng/ghostlock-z3q) : ![starts](https://img.shields.io/github/stars/thedavidweng/ghostlock-z3q.svg) ![forks](https://img.shields.io/github/forks/thedavidweng/ghostlock-z3q.svg)

## CVE-2026-58868
> In onOutputReceived of FrameDecoder.cpp, there is a possible out-of-bounds write due to a heap buffer overflow. This could lead to remote code execution with no additional execution privileges needed. User interaction is not needed for exploitation.

- [https://github.com/probear0001/CVE-2026-58868](https://github.com/probear0001/CVE-2026-58868) : ![starts](https://img.shields.io/github/stars/probear0001/CVE-2026-58868.svg) ![forks](https://img.shields.io/github/forks/probear0001/CVE-2026-58868.svg)

## CVE-2026-91403

- [https://github.com/bryanHsiao/domino-emudhra-cert-mitigation](https://github.com/bryanHsiao/domino-emudhra-cert-mitigation) : ![starts](https://img.shields.io/github/stars/bryanHsiao/domino-emudhra-cert-mitigation.svg) ![forks](https://img.shields.io/github/forks/bryanHsiao/domino-emudhra-cert-mitigation.svg)

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

## CVE-2026-98260
> In the Linux kernel, the following vulnerability has been resolved:

exec: Cleanup POSIX timers right after de_thread()

A per-thread CPU timer holds a reference to the PID of the thread it is
attached to and, while it is armed, its node is queued in that thread&#x27;s
posix_cputimers. The task is looked up by that PID.

When a non-leader thread exec()s, de_thread() changes which task owns
that PID. pid_task(timer-&gt;it.cpu.pid, PIDTYPE_PID) then returns NULL,
but the node is still queued on tsk, which

- [https://github.com/Yukaneko520/RootMyZ9Turbo](https://github.com/Yukaneko520/RootMyZ9Turbo) : ![starts](https://img.shields.io/github/stars/Yukaneko520/RootMyZ9Turbo.svg) ![forks](https://img.shields.io/github/forks/Yukaneko520/RootMyZ9Turbo.svg)
- [https://github.com/al123xiaaaa/CVE-2026-98260-GT7Pro-RMX5010](https://github.com/al123xiaaaa/CVE-2026-98260-GT7Pro-RMX5010) : ![starts](https://img.shields.io/github/stars/al123xiaaaa/CVE-2026-98260-GT7Pro-RMX5010.svg) ![forks](https://img.shields.io/github/forks/al123xiaaaa/CVE-2026-98260-GT7Pro-RMX5010.svg)
- [https://github.com/starriv/CVE-2026-98260-Xiaomi-17-Pro-Max](https://github.com/starriv/CVE-2026-98260-Xiaomi-17-Pro-Max) : ![starts](https://img.shields.io/github/stars/starriv/CVE-2026-98260-Xiaomi-17-Pro-Max.svg) ![forks](https://img.shields.io/github/forks/starriv/CVE-2026-98260-Xiaomi-17-Pro-Max.svg)
- [https://github.com/whooslizi/infinitycore-x200pro](https://github.com/whooslizi/infinitycore-x200pro) : ![starts](https://img.shields.io/github/stars/whooslizi/infinitycore-x200pro.svg) ![forks](https://img.shields.io/github/forks/whooslizi/infinitycore-x200pro.svg)

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
- [https://github.com/INFOKOM-KI/CVE-2026-98432-Wazuh-](https://github.com/INFOKOM-KI/CVE-2026-98432-Wazuh-) : ![starts](https://img.shields.io/github/stars/INFOKOM-KI/CVE-2026-98432-Wazuh-.svg) ![forks](https://img.shields.io/github/forks/INFOKOM-KI/CVE-2026-98432-Wazuh-.svg)
- [https://github.com/carlosbustillordguez/cve-2026-98432-mitigation](https://github.com/carlosbustillordguez/cve-2026-98432-mitigation) : ![starts](https://img.shields.io/github/stars/carlosbustillordguez/cve-2026-98432-mitigation.svg) ![forks](https://img.shields.io/github/forks/carlosbustillordguez/cve-2026-98432-mitigation.svg)
- [https://github.com/datacenter-metrotel/Mitigating-CVE-2026-98432](https://github.com/datacenter-metrotel/Mitigating-CVE-2026-98432) : ![starts](https://img.shields.io/github/stars/datacenter-metrotel/Mitigating-CVE-2026-98432.svg) ![forks](https://img.shields.io/github/forks/datacenter-metrotel/Mitigating-CVE-2026-98432.svg)
- [https://github.com/dolistblesson/CVE-2026-98432-update](https://github.com/dolistblesson/CVE-2026-98432-update) : ![starts](https://img.shields.io/github/stars/dolistblesson/CVE-2026-98432-update.svg) ![forks](https://img.shields.io/github/forks/dolistblesson/CVE-2026-98432-update.svg)
- [https://github.com/keithel/ubuntu-26.04-kernel-cve-2026-98432-patch-build-docker](https://github.com/keithel/ubuntu-26.04-kernel-cve-2026-98432-patch-build-docker) : ![starts](https://img.shields.io/github/stars/keithel/ubuntu-26.04-kernel-cve-2026-98432-patch-build-docker.svg) ![forks](https://img.shields.io/github/forks/keithel/ubuntu-26.04-kernel-cve-2026-98432-patch-build-docker.svg)
- [https://github.com/moatome/CVE-2026-98432-pen-test-main](https://github.com/moatome/CVE-2026-98432-pen-test-main) : ![starts](https://img.shields.io/github/stars/moatome/CVE-2026-98432-pen-test-main.svg) ![forks](https://img.shields.io/github/forks/moatome/CVE-2026-98432-pen-test-main.svg)
