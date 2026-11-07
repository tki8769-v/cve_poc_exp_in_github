# Update 2026-11-07
## CVE-2023-4622

- [https://github.com/android-cve-exploits/0range1337--CVE-CVE-2023-4622](https://github.com/android-cve-exploits/0range1337--CVE-CVE-2023-4622) : ![starts](https://img.shields.io/github/stars/android-cve-exploits/0range1337--CVE-CVE-2023-4622.svg) ![forks](https://img.shields.io/github/forks/android-cve-exploits/0range1337--CVE-CVE-2023-4622.svg)

## CVE-2024-21762
> A out-of-bounds write vulnerability in Fortinet FortiOS 7.4.0 through 7.4.2, FortiOS 7.2.0 through 7.2.6, FortiOS 7.0.0 through 7.0.13, FortiOS 6.4.0 through 6.4.14, FortiOS 6.2.0 through 6.2.15, FortiOS 6.0 all versions, FortiProxy 7.4.0 through 7.4.2, FortiProxy 7.2.0 through 7.2.8, FortiProxy 7.0.0 through 7.0.14, FortiProxy 2.0.0 through 2.0.13, FortiProxy 01.02 all versions, FortiProxy 1.2 all versions, FortiProxy 01.01 all versions, FortiProxy 1.1 all versions, FortiProxy 01.00 all version

- [https://github.com/IzanInPublic/CVE-2024-21762-Safe-Check](https://github.com/IzanInPublic/CVE-2024-21762-Safe-Check) : ![starts](https://img.shields.io/github/stars/IzanInPublic/CVE-2024-21762-Safe-Check.svg) ![forks](https://img.shields.io/github/forks/IzanInPublic/CVE-2024-21762-Safe-Check.svg)

## CVE-2026-10795

- [https://github.com/NilsZimmermann/wordpress-ushort-redirect-cleaner](https://github.com/NilsZimmermann/wordpress-ushort-redirect-cleaner) : ![starts](https://img.shields.io/github/stars/NilsZimmermann/wordpress-ushort-redirect-cleaner.svg) ![forks](https://img.shields.io/github/forks/NilsZimmermann/wordpress-ushort-redirect-cleaner.svg)

## CVE-2026-109618
> PHP uses longjmp() for out-of-memory (OOM) errors to exit the current context and abort handling of the request. Some contexts may not properly account for this scenario and leave request memory in an uninitialized state before performing an allocation. The subsequent request cleanup procedure may read or branch on this memory. Multiple OOM strategies can consistently trigger this condition and lead to remote code execution (RCE).

- [https://github.com/LiliNothere/CVE-2026-109618](https://github.com/LiliNothere/CVE-2026-109618) : ![starts](https://img.shields.io/github/stars/LiliNothere/CVE-2026-109618.svg) ![forks](https://img.shields.io/github/forks/LiliNothere/CVE-2026-109618.svg)
- [https://github.com/psikoma/php2shell-CVE-2026-109618-109619](https://github.com/psikoma/php2shell-CVE-2026-109618-109619) : ![starts](https://img.shields.io/github/stars/psikoma/php2shell-CVE-2026-109618-109619.svg) ![forks](https://img.shields.io/github/forks/psikoma/php2shell-CVE-2026-109618-109619.svg)

## CVE-2026-111560
> Improper neutralization of shell metacharacters in the timezone configuration field in certain Barracuda appliance products using common Barracuda code allows an authenticated administrator to inject OS commands that execute with root privileges when the crafted timezone value is subsequently processed.

- [https://github.com/watchtowrlabs/watchTowr-vs-Barracuda-RCE-CVE-2026-116606-CVE-2026-111560](https://github.com/watchtowrlabs/watchTowr-vs-Barracuda-RCE-CVE-2026-116606-CVE-2026-111560) : ![starts](https://img.shields.io/github/stars/watchtowrlabs/watchTowr-vs-Barracuda-RCE-CVE-2026-116606-CVE-2026-111560.svg) ![forks](https://img.shields.io/github/forks/watchtowrlabs/watchTowr-vs-Barracuda-RCE-CVE-2026-116606-CVE-2026-111560.svg)

## CVE-2026-116606
> An authentication bypass in Barracuda Email Security Gateway versions earlier than 9.4.0.030 allows an unauthenticated remote attacker to invoke a configuration-import function and restore a crafted, compatible backup archive, resulting in unauthorized modification of the appliance’s global configuration.

- [https://github.com/watchtowrlabs/watchTowr-vs-Barracuda-RCE-CVE-2026-116606-CVE-2026-111560](https://github.com/watchtowrlabs/watchTowr-vs-Barracuda-RCE-CVE-2026-116606-CVE-2026-111560) : ![starts](https://img.shields.io/github/stars/watchtowrlabs/watchTowr-vs-Barracuda-RCE-CVE-2026-116606-CVE-2026-111560.svg) ![forks](https://img.shields.io/github/forks/watchtowrlabs/watchTowr-vs-Barracuda-RCE-CVE-2026-116606-CVE-2026-111560.svg)

## CVE-2026-117691
> A flaw was found in the SAML HTTP-Redirect binding implementation of Keycloak. The issue occurs because the server processes percent-encoded parameter names (like %53AMLResponse) while the signature verification logic only checks literal parameter names. An attacker can use this discrepancy to provide a crafted, unsigned SAML message that the server processes instead of a legitimately signed one, leading to full account takeover of federated users.

- [https://github.com/foxcornlab/keycloak-saml-scanner](https://github.com/foxcornlab/keycloak-saml-scanner) : ![starts](https://img.shields.io/github/stars/foxcornlab/keycloak-saml-scanner.svg) ![forks](https://img.shields.io/github/forks/foxcornlab/keycloak-saml-scanner.svg)

## CVE-2026-119977
> WordPress Core is vulnerable to Remote Code Execution in versions 4.7 through 7.1.3. This is due to predictable, web-accessible staging paths used during full-package core upgrades. This makes it possible for unauthenticated attackers to execute code on the server during the upgrade window.

- [https://github.com/riabinov/CVE-2026-119977](https://github.com/riabinov/CVE-2026-119977) : ![starts](https://img.shields.io/github/stars/riabinov/CVE-2026-119977.svg) ![forks](https://img.shields.io/github/forks/riabinov/CVE-2026-119977.svg)

## CVE-2026-123014
> iTerm2 before 3.7.7beta2 has an argument injection vulnerability in the x-man-page: URL handler, allowing an attacker to execute arbitrary commands with the privileges of the logged-in user by inducing the user to open a crafted URL in iTerm2. Percent-encoded NUL characters survive input sanitization and are subsequently converted to whitespace during command-line parsing, allowing injection of additional arguments to /usr/bin/man. An attacker can inject the -P option to select an attacker-contr

- [https://github.com/giki-shergill/CVE-2026-123014---iTerm2-Terminal](https://github.com/giki-shergill/CVE-2026-123014---iTerm2-Terminal) : ![starts](https://img.shields.io/github/stars/giki-shergill/CVE-2026-123014---iTerm2-Terminal.svg) ![forks](https://img.shields.io/github/forks/giki-shergill/CVE-2026-123014---iTerm2-Terminal.svg)

## CVE-2026-123158
> sshd in OpenSSH before 10.6p2 on Linux, when musl libc is used without PAM, lacks a workaround for a password authentication bypass (related to misinterpretation of whether a string is intended to be a password hash). For some configurations of accounts, any password between 256 and 1024 characters succeeds. An example of a platform using musl libc without PAM is Alpine Linux.

- [https://github.com/Funcan/sshole](https://github.com/Funcan/sshole) : ![starts](https://img.shields.io/github/stars/Funcan/sshole.svg) ![forks](https://img.shields.io/github/forks/Funcan/sshole.svg)

## CVE-2026-33017

- [https://github.com/NSK-394/kavach-loop](https://github.com/NSK-394/kavach-loop) : ![starts](https://img.shields.io/github/stars/NSK-394/kavach-loop.svg) ![forks](https://img.shields.io/github/forks/NSK-394/kavach-loop.svg)

## CVE-2026-42945

- [https://github.com/richard-rodriguez26/CVE-2026-42945](https://github.com/richard-rodriguez26/CVE-2026-42945) : ![starts](https://img.shields.io/github/stars/richard-rodriguez26/CVE-2026-42945.svg) ![forks](https://img.shields.io/github/forks/richard-rodriguez26/CVE-2026-42945.svg)

## CVE-2026-43284
> In the Linux kernel, the following vulnerability has been resolved:

xfrm: esp: avoid in-place decrypt on shared skb frags

MSG_SPLICE_PAGES can attach pages from a pipe directly to an skb. TCP
marks such skbs with SKBFL_SHARED_FRAG after skb_splice_from_iter(),
so later paths that may modify packet data can first make a private
copy. The IPv4/IPv6 datagram append paths did not set this flag when
splicing pages into UDP skbs.

That leaves an ESP-in-UDP packet made from shared pipe pages looking


- [https://github.com/noctide/redmi-k50-temp-root](https://github.com/noctide/redmi-k50-temp-root) : ![starts](https://img.shields.io/github/stars/noctide/redmi-k50-temp-root.svg) ![forks](https://img.shields.io/github/forks/noctide/redmi-k50-temp-root.svg)

## CVE-2026-83844

- [https://github.com/Cobrastrike62/CVE-2026-83844-Detection](https://github.com/Cobrastrike62/CVE-2026-83844-Detection) : ![starts](https://img.shields.io/github/stars/Cobrastrike62/CVE-2026-83844-Detection.svg) ![forks](https://img.shields.io/github/forks/Cobrastrike62/CVE-2026-83844-Detection.svg)

## CVE-2026-88773
> Inconsistent interpretation of HTTP requests (&#x27;HTTP Request/Response smuggling&#x27;) vulnerability in Citrix NetScaler ADC and Citrix NetScaler Gateway.

This issue affects ADC: before 14.1-73.37, before 13.1-64.23, before 14.1-73.37 FIPS, and before 13.1-37.279 and NDcPP; Gateway: before 14.1-73.37 FIPS and before 13.1-64.23.

- [https://github.com/CompleteTech-Security/netscaler-cve-2026-88773-check](https://github.com/CompleteTech-Security/netscaler-cve-2026-88773-check) : ![starts](https://img.shields.io/github/stars/CompleteTech-Security/netscaler-cve-2026-88773-check.svg) ![forks](https://img.shields.io/github/forks/CompleteTech-Security/netscaler-cve-2026-88773-check.svg)

## CVE-2026-88776
> Memory overflow vulnerability vulnerability in Citrix NetScaler ADC and Citrix NetScaler Gateway.
This issue affects ADC: before 14.1-73.37, before 13.1-64.23, before 14.1-73.37 FIPS, and before 13.1.37.279 FIPS and NDcPP; Gateway: before 14.1-73.37 and before 13.1-64.23  leading to unpredictable or erroneous behavior or Denial of Service

- [https://github.com/CompleteTech-Security/netscaler-cve-2026-88776-check](https://github.com/CompleteTech-Security/netscaler-cve-2026-88776-check) : ![starts](https://img.shields.io/github/stars/CompleteTech-Security/netscaler-cve-2026-88776-check.svg) ![forks](https://img.shields.io/github/forks/CompleteTech-Security/netscaler-cve-2026-88776-check.svg)

## CVE-2026-98499
> In the Linux kernel, the following vulnerability has been resolved:

HID: wacom: fix OOB read in wacom_wac_pen_serial_enforce()

The &#x27;wacom_wac_pen_serial_enforce()&#x27; function may calculate and pass an
invalid offset to hid_field_extract(), resulting in memory reads at
incorrect addresses -- possibly beyond the end of the report.  If a
field in the HID descriptor lists more usages than its Report Count
actually reserves space for, the function&#x27;s inner &#x27;j&#x27; will walk past
the end of the field:

	fo

- [https://github.com/woshigenm/CVE-2026-98499](https://github.com/woshigenm/CVE-2026-98499) : ![starts](https://img.shields.io/github/stars/woshigenm/CVE-2026-98499.svg) ![forks](https://img.shields.io/github/forks/woshigenm/CVE-2026-98499.svg)
