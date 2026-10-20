# Update 2026-10-20
## CVE-2017-0143

- [https://github.com/BlessingOlaniyan/cve-2017-0143-smbv1-analysis](https://github.com/BlessingOlaniyan/cve-2017-0143-smbv1-analysis) : ![starts](https://img.shields.io/github/stars/BlessingOlaniyan/cve-2017-0143-smbv1-analysis.svg) ![forks](https://img.shields.io/github/forks/BlessingOlaniyan/cve-2017-0143-smbv1-analysis.svg)

## CVE-2017-7494

- [https://github.com/JA-Cyber365/home-network-security-assessment](https://github.com/JA-Cyber365/home-network-security-assessment) : ![starts](https://img.shields.io/github/stars/JA-Cyber365/home-network-security-assessment.svg) ![forks](https://img.shields.io/github/forks/JA-Cyber365/home-network-security-assessment.svg)

## CVE-2021-41773

- [https://github.com/twq0316/work1-secure-rest-api](https://github.com/twq0316/work1-secure-rest-api) : ![starts](https://img.shields.io/github/stars/twq0316/work1-secure-rest-api.svg) ![forks](https://img.shields.io/github/forks/twq0316/work1-secure-rest-api.svg)

## CVE-2024-21762

- [https://github.com/Deekshitha2203/security-triage-agent-cybersec590](https://github.com/Deekshitha2203/security-triage-agent-cybersec590) : ![starts](https://img.shields.io/github/stars/Deekshitha2203/security-triage-agent-cybersec590.svg) ![forks](https://img.shields.io/github/forks/Deekshitha2203/security-triage-agent-cybersec590.svg)

## CVE-2026-111057
> Mercury is a Python framework for sharing Jupyter notebooks as web applications and dashboards. From 3.0.0 until 3.2.4, a missing comma in BLOCKED_PATTERNS concatenates the /lab and /api/terminals regular-expression literals. Requests to /api/terminals therefore bypass the anonymous endpoint blocklist and reach Jupyter Server&#x27;s terminal API. An unauthenticated attacker can use the resulting interactive operating-system shell to execute commands and access data available to the Mercury process. T

- [https://github.com/ExDev994/CVE-2026-111058-CVE-2026-111057-mercury-rce](https://github.com/ExDev994/CVE-2026-111058-CVE-2026-111057-mercury-rce) : ![starts](https://img.shields.io/github/stars/ExDev994/CVE-2026-111058-CVE-2026-111057-mercury-rce.svg) ![forks](https://img.shields.io/github/forks/ExDev994/CVE-2026-111058-CVE-2026-111057-mercury-rce.svg)

## CVE-2026-111058
> Mercury is a Python framework for sharing Jupyter notebooks as web applications and dashboards. Prior to 3.2.6, default tokenless deployments allow anonymous clients to create Jupyter kernels and send execute_request messages containing arbitrary Python. The endpoint blocklist does not cover /api/kernels, and the websocket wrapper previously tracked idle activity without authorizing executable messages. This issue is fixed in version 3.2.6.

- [https://github.com/ExDev994/CVE-2026-111058-CVE-2026-111057-mercury-rce](https://github.com/ExDev994/CVE-2026-111058-CVE-2026-111057-mercury-rce) : ![starts](https://img.shields.io/github/stars/ExDev994/CVE-2026-111058-CVE-2026-111057-mercury-rce.svg) ![forks](https://img.shields.io/github/forks/ExDev994/CVE-2026-111058-CVE-2026-111057-mercury-rce.svg)

## CVE-2026-35273

- [https://github.com/rayo0009/CVE-2026-35273-Oracle-PeopleSoft-PeopleTools-Zero-Day-](https://github.com/rayo0009/CVE-2026-35273-Oracle-PeopleSoft-PeopleTools-Zero-Day-) : ![starts](https://img.shields.io/github/stars/rayo0009/CVE-2026-35273-Oracle-PeopleSoft-PeopleTools-Zero-Day-.svg) ![forks](https://img.shields.io/github/forks/rayo0009/CVE-2026-35273-Oracle-PeopleSoft-PeopleTools-Zero-Day-.svg)

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

- [https://github.com/Escosis/V2463A-LPE](https://github.com/Escosis/V2463A-LPE) : ![starts](https://img.shields.io/github/stars/Escosis/V2463A-LPE.svg) ![forks](https://img.shields.io/github/forks/Escosis/V2463A-LPE.svg)

## CVE-2026-96652
> Plex Media Server before 1.43.3.10861 allows SSRF via &#x27;/player/timeline&#x27;. An attacker using any X-Plex-Token value can include a full URL in the &#x27;protocol&#x27; parameter and force the Plex server to POST to the attacker&#x27;s chosen destination.

- [https://github.com/ChrisLPJones/plex2shell-check](https://github.com/ChrisLPJones/plex2shell-check) : ![starts](https://img.shields.io/github/stars/ChrisLPJones/plex2shell-check.svg) ![forks](https://img.shields.io/github/forks/ChrisLPJones/plex2shell-check.svg)

## CVE-2026-99999
> In the Linux kernel, the following vulnerability has been resolved:

ipv4: validate checksum_start before completing checksum

If a packet with bad checksum metadata gets into the ipv4 stack,
skb_checksum_help can corrupt the network header and cause a bunch of
mischief.

This was discovered and reported by Paulos, and has been reporoduced
by others independently since.

We really shouldn&#x27;t allow such packets in, but as a defence
in depth measure, let&#x27;s also check before we complete the checksum

- [https://github.com/nsrg-fmlorg/kpatch-alma-cve-2026-99999](https://github.com/nsrg-fmlorg/kpatch-alma-cve-2026-99999) : ![starts](https://img.shields.io/github/stars/nsrg-fmlorg/kpatch-alma-cve-2026-99999.svg) ![forks](https://img.shields.io/github/forks/nsrg-fmlorg/kpatch-alma-cve-2026-99999.svg)
