# Update 2026-10-26
## CVE-2026-39902
> Cacti is an open source performance and fault management framework. Prior to version 1.2.31, the prior blocklist ([;&amp;| `$\\n\r]) omitted single-quote, double-quote, redirect operators, subshell parens and braces. An authenticated admin could save an input_string` containing single-quote, redirect operator, or subshell parens, and pass the check. This issue has been patched in version 1.2.31.

- [https://github.com/kx00007/CVE-2026-39902](https://github.com/kx00007/CVE-2026-39902) : ![starts](https://img.shields.io/github/stars/kx00007/CVE-2026-39902.svg) ![forks](https://img.shields.io/github/forks/kx00007/CVE-2026-39902.svg)

## CVE-2026-53921
> odhcpd is the DHCPv6, DHCPv4, and router-advertisement server used by OpenWrt. Prior to version 25.12, odhcpd&#x27;s DHCPv6 IA response handler writes past the end of a fixed 512-byte stack buffer (pdbuf) when a single DHCPv6 REQUEST carries enough IA options to nearly exhaust the reply space. Two independent overflow sites exist in the same call chain, both reachable from the network via a single unauthenticated UDP packet. odhcpd runs as root on OpenWrt; embedded targets often lack stack canaries a

- [https://github.com/0xBlackash/CVE-2026-53921](https://github.com/0xBlackash/CVE-2026-53921) : ![starts](https://img.shields.io/github/stars/0xBlackash/CVE-2026-53921.svg) ![forks](https://img.shields.io/github/forks/0xBlackash/CVE-2026-53921.svg)
