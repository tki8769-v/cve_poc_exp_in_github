# Update 2026-11-07
## CVE-2026-10795

- [https://github.com/NilsZimmermann/wordpress-ushort-redirect-cleaner](https://github.com/NilsZimmermann/wordpress-ushort-redirect-cleaner) : ![starts](https://img.shields.io/github/stars/NilsZimmermann/wordpress-ushort-redirect-cleaner.svg) ![forks](https://img.shields.io/github/forks/NilsZimmermann/wordpress-ushort-redirect-cleaner.svg)

## CVE-2026-109618
> PHP uses longjmp() for out-of-memory (OOM) errors to exit the current context and abort handling of the request. Some contexts may not properly account for this scenario and leave request memory in an uninitialized state before performing an allocation. The subsequent request cleanup procedure may read or branch on this memory. Multiple OOM strategies can consistently trigger this condition and lead to remote code execution (RCE).

- [https://github.com/psikoma/php2shell-CVE-2026-109618-109619](https://github.com/psikoma/php2shell-CVE-2026-109618-109619) : ![starts](https://img.shields.io/github/stars/psikoma/php2shell-CVE-2026-109618-109619.svg) ![forks](https://img.shields.io/github/forks/psikoma/php2shell-CVE-2026-109618-109619.svg)

## CVE-2026-111560
> Improper neutralization of shell metacharacters in the timezone configuration field in certain Barracuda appliance products using common Barracuda code allows an authenticated administrator to inject OS commands that execute with root privileges when the crafted timezone value is subsequently processed.

- [https://github.com/watchtowrlabs/watchTowr-vs-Barracuda-RCE-CVE-2026-116606-CVE-2026-111560](https://github.com/watchtowrlabs/watchTowr-vs-Barracuda-RCE-CVE-2026-116606-CVE-2026-111560) : ![starts](https://img.shields.io/github/stars/watchtowrlabs/watchTowr-vs-Barracuda-RCE-CVE-2026-116606-CVE-2026-111560.svg) ![forks](https://img.shields.io/github/forks/watchtowrlabs/watchTowr-vs-Barracuda-RCE-CVE-2026-116606-CVE-2026-111560.svg)

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

## CVE-2026-83844

- [https://github.com/Cobrastrike62/CVE-2026-83844-Detection](https://github.com/Cobrastrike62/CVE-2026-83844-Detection) : ![starts](https://img.shields.io/github/stars/Cobrastrike62/CVE-2026-83844-Detection.svg) ![forks](https://img.shields.io/github/forks/Cobrastrike62/CVE-2026-83844-Detection.svg)
