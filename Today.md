# Update 2026-11-07
## CVE-2026-123014
> iTerm2 before 3.7.7beta2 has an argument injection vulnerability in the x-man-page: URL handler, allowing an attacker to execute arbitrary commands with the privileges of the logged-in user by inducing the user to open a crafted URL in iTerm2. Percent-encoded NUL characters survive input sanitization and are subsequently converted to whitespace during command-line parsing, allowing injection of additional arguments to /usr/bin/man. An attacker can inject the -P option to select an attacker-contr

- [https://github.com/giki-shergill/CVE-2026-123014---iTerm2-Terminal](https://github.com/giki-shergill/CVE-2026-123014---iTerm2-Terminal) : ![starts](https://img.shields.io/github/stars/giki-shergill/CVE-2026-123014---iTerm2-Terminal.svg) ![forks](https://img.shields.io/github/forks/giki-shergill/CVE-2026-123014---iTerm2-Terminal.svg)

## CVE-2026-123158
> sshd in OpenSSH before 10.6p2 on Linux, when musl libc is used without PAM, lacks a workaround for a password authentication bypass (related to misinterpretation of whether a string is intended to be a password hash). For some configurations of accounts, any password between 256 and 1024 characters succeeds. An example of a platform using musl libc without PAM is Alpine Linux.

- [https://github.com/Funcan/sshole](https://github.com/Funcan/sshole) : ![starts](https://img.shields.io/github/stars/Funcan/sshole.svg) ![forks](https://img.shields.io/github/forks/Funcan/sshole.svg)

## CVE-2026-83844

- [https://github.com/Cobrastrike62/CVE-2026-83844-Detection](https://github.com/Cobrastrike62/CVE-2026-83844-Detection) : ![starts](https://img.shields.io/github/stars/Cobrastrike62/CVE-2026-83844-Detection.svg) ![forks](https://img.shields.io/github/forks/Cobrastrike62/CVE-2026-83844-Detection.svg)
