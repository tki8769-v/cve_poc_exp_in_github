# Update 2026-11-12
## CVE-2023-29017

- [https://github.com/wooung105/Node_CVE-2023-29017](https://github.com/wooung105/Node_CVE-2023-29017) : ![starts](https://img.shields.io/github/stars/wooung105/Node_CVE-2023-29017.svg) ![forks](https://img.shields.io/github/forks/wooung105/Node_CVE-2023-29017.svg)

## CVE-2026-110912
> In DragonFly BSD through 6.4.2 before 4bb22ff, the ARP input handlers arpintr() and in_arpinput() (sys/netinet/if_ether.c) do not validate the hardware address length (ar_hln) and protocol address length (ar_pln) fields of incoming ARP packets. in_arpreply() then uses these attacker-controlled values as memcpy lengths when copying from kernel buffers that are only 6 and 4 bytes long, resulting in an out-of-bounds read of kernel heap and stack memory that is copied into the ARP reply sent back to

- [https://github.com/ashrafzaryouh/CVE-2026-110912](https://github.com/ashrafzaryouh/CVE-2026-110912) : ![starts](https://img.shields.io/github/stars/ashrafzaryouh/CVE-2026-110912.svg) ![forks](https://img.shields.io/github/forks/ashrafzaryouh/CVE-2026-110912.svg)

## CVE-2026-12485

- [https://github.com/ashrafzaryouh/CVE-2026-12485](https://github.com/ashrafzaryouh/CVE-2026-12485) : ![starts](https://img.shields.io/github/stars/ashrafzaryouh/CVE-2026-12485.svg) ![forks](https://img.shields.io/github/forks/ashrafzaryouh/CVE-2026-12485.svg)

## CVE-2026-6471

- [https://github.com/ashrafzaryouh/CVE-2026-6471](https://github.com/ashrafzaryouh/CVE-2026-6471) : ![starts](https://img.shields.io/github/stars/ashrafzaryouh/CVE-2026-6471.svg) ![forks](https://img.shields.io/github/forks/ashrafzaryouh/CVE-2026-6471.svg)

## CVE-2026-76954

- [https://github.com/ansonhsu-ai/synology-dsm-cve-2026-76954-ste](https://github.com/ansonhsu-ai/synology-dsm-cve-2026-76954-ste) : ![starts](https://img.shields.io/github/stars/ansonhsu-ai/synology-dsm-cve-2026-76954-ste.svg) ![forks](https://img.shields.io/github/forks/ansonhsu-ai/synology-dsm-cve-2026-76954-ste.svg)

## CVE-2026-80844
> In the Linux kernel, the following vulnerability has been resolved:

xfrm: ah6: validate routing header segments_left

AH6 rearranges routing-header addresses before computing or verifying the
ICV. ipv6_rearrange_rthdr() assumes that segments_left is not larger than
the number of addresses described by the routing header&#x27;s hdrlen field.

That assumption does not hold for raw IPv6 HDRINCL packets. A packet with
hdrlen equal to 2 describes one address, but can carry an arbitrary
segments_left valu

- [https://github.com/ashrafzaryouh/CVE-2026-80844](https://github.com/ashrafzaryouh/CVE-2026-80844) : ![starts](https://img.shields.io/github/stars/ashrafzaryouh/CVE-2026-80844.svg) ![forks](https://img.shields.io/github/forks/ashrafzaryouh/CVE-2026-80844.svg)
