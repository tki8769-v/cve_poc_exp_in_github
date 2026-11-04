# Update 2026-11-04
## CVE-2009-4496

- [https://github.com/enriquenegri-cyberlaw/boa-webserver-log-escape-injection-cve-2009-4496](https://github.com/enriquenegri-cyberlaw/boa-webserver-log-escape-injection-cve-2009-4496) : ![starts](https://img.shields.io/github/stars/enriquenegri-cyberlaw/boa-webserver-log-escape-injection-cve-2009-4496.svg) ![forks](https://img.shields.io/github/forks/enriquenegri-cyberlaw/boa-webserver-log-escape-injection-cve-2009-4496.svg)

## CVE-2021-4034

- [https://github.com/eshkoreee/CVE-2021-4034](https://github.com/eshkoreee/CVE-2021-4034) : ![starts](https://img.shields.io/github/stars/eshkoreee/CVE-2021-4034.svg) ![forks](https://img.shields.io/github/forks/eshkoreee/CVE-2021-4034.svg)

## CVE-2024-23334

- [https://github.com/frogb1t/CVE-2024-23334](https://github.com/frogb1t/CVE-2024-23334) : ![starts](https://img.shields.io/github/stars/frogb1t/CVE-2024-23334.svg) ![forks](https://img.shields.io/github/forks/frogb1t/CVE-2024-23334.svg)

## CVE-2025-55182
> A pre-authentication remote code execution vulnerability exists in React Server Components versions 19.0.0, 19.1.0, 19.1.1, and 19.2.0 including the following packages: react-server-dom-parcel, react-server-dom-turbopack, and react-server-dom-webpack. The vulnerable code unsafely deserializes payloads from HTTP requests to Server Function endpoints.

- [https://github.com/Certbn/CVE-2025-55182-React-Server-Components-Flight-React2Shell-](https://github.com/Certbn/CVE-2025-55182-React-Server-Components-Flight-React2Shell-) : ![starts](https://img.shields.io/github/stars/Certbn/CVE-2025-55182-React-Server-Components-Flight-React2Shell-.svg) ![forks](https://img.shields.io/github/forks/Certbn/CVE-2025-55182-React-Server-Components-Flight-React2Shell-.svg)

## CVE-2026-109618
> PHP uses longjmp() for out-of-memory (OOM) errors to exit the current context and abort handling of the request. Some contexts may not properly account for this scenario and leave request memory in an uninitialized state before performing an allocation. The subsequent request cleanup procedure may read or branch on this memory. Multiple OOM strategies can consistently trigger this condition and lead to remote code execution (RCE).

- [https://github.com/Danyw24/the-php2shell-recipe](https://github.com/Danyw24/the-php2shell-recipe) : ![starts](https://img.shields.io/github/stars/Danyw24/the-php2shell-recipe.svg) ![forks](https://img.shields.io/github/forks/Danyw24/the-php2shell-recipe.svg)

## CVE-2026-112689
> An out-of-bounds write issue was addressed with improved input validation. This issue is fixed in iOS 26.7.2 and iPadOS 26.7.2, iOS 27.2 and iPadOS 27.2, macOS Golden Gate 27.2, macOS Sequoia 15.8.2, macOS Tahoe 26.7.2, tvOS 27.2. An app may be able to cause unexpected system termination or corrupt kernel memory.

- [https://github.com/Lak453/CVE-2026-112689-poc](https://github.com/Lak453/CVE-2026-112689-poc) : ![starts](https://img.shields.io/github/stars/Lak453/CVE-2026-112689-poc.svg) ![forks](https://img.shields.io/github/forks/Lak453/CVE-2026-112689-poc.svg)

## CVE-2026-20687
> A use after free issue was addressed with improved memory management. This issue is fixed in iOS 18.7.7 and iPadOS 18.7.7, iOS 26.4 and iPadOS 26.4, macOS Sequoia 15.7.5, macOS Tahoe 26.4, tvOS 26.4, watchOS 26.4. An app may be able to cause unexpected system termination or write kernel memory.

- [https://github.com/hidra0x/hidra](https://github.com/hidra0x/hidra) : ![starts](https://img.shields.io/github/stars/hidra0x/hidra.svg) ![forks](https://img.shields.io/github/forks/hidra0x/hidra.svg)

## CVE-2026-59795

- [https://github.com/JoakimBulow/CVE-2026-59795](https://github.com/JoakimBulow/CVE-2026-59795) : ![starts](https://img.shields.io/github/stars/JoakimBulow/CVE-2026-59795.svg) ![forks](https://img.shields.io/github/forks/JoakimBulow/CVE-2026-59795.svg)

## CVE-2026-80587
> In the Linux kernel, the following vulnerability has been resolved:

mptcp: avoid combining some incoming suboptions

Some MPTCP suboptions are mutually exclusive according to the RFC8684,
but also because in different places, the code doesn&#x27;t expect some
combinations to be present. That&#x27;s specially true for suboptions that
would be present twice, but with different attributes.

The new restrictions are the same as the ones applied on the output
side, with mptcp_write_options. The same rules can

- [https://github.com/9technologygroup/cve-2026-80587-check](https://github.com/9technologygroup/cve-2026-80587-check) : ![starts](https://img.shields.io/github/stars/9technologygroup/cve-2026-80587-check.svg) ![forks](https://img.shields.io/github/forks/9technologygroup/cve-2026-80587-check.svg)

## CVE-2026-92183
> GIMP APNG File Parsing Stack-based Buffer Overflow Remote Code Execution Vulnerability. This vulnerability allows remote attackers to execute arbitrary code on affected installations of GIMP. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file.

The specific flaw exists within the parsing of APNG files. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a st

- [https://github.com/CXu0630/CVE-2026-92183_GIMP_RCE_Proof-of-Concept](https://github.com/CXu0630/CVE-2026-92183_GIMP_RCE_Proof-of-Concept) : ![starts](https://img.shields.io/github/stars/CXu0630/CVE-2026-92183_GIMP_RCE_Proof-of-Concept.svg) ![forks](https://img.shields.io/github/forks/CXu0630/CVE-2026-92183_GIMP_RCE_Proof-of-Concept.svg)

## CVE-2026-98432
> In the Linux kernel, the following vulnerability has been resolved:

ipv4: free inet_opt and ireq_opt after an RCU grace period

tcp_v4_syn_recv_sock() transfers ownership of ireq-&gt;ireq_opt to the
child socket (newinet-&gt;inet_opt) without copying it.

Another cpu can concurrently process a retransmitted SYN for the same
request socket, and send a SYNACK from tcp_check_req().
tcp_v4_send_synack() and inet_csk_route_req() read ireq-&gt;ireq_opt
under rcu_read_lock() only, and ip_build_and_send_pkt() a

- [https://github.com/hdp1972be-svg/cve_2026_98432_guard](https://github.com/hdp1972be-svg/cve_2026_98432_guard) : ![starts](https://img.shields.io/github/stars/hdp1972be-svg/cve_2026_98432_guard.svg) ![forks](https://img.shields.io/github/forks/hdp1972be-svg/cve_2026_98432_guard.svg)
- [https://github.com/zenjabba/cve-2026-98432-mitigation](https://github.com/zenjabba/cve-2026-98432-mitigation) : ![starts](https://img.shields.io/github/stars/zenjabba/cve-2026-98432-mitigation.svg) ![forks](https://img.shields.io/github/forks/zenjabba/cve-2026-98432-mitigation.svg)
