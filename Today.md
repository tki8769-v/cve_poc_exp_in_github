# Update 2026-11-06
## CVE-2025-50579

- [https://github.com/davidoberst/CVE-2025-50579-CORS-Misconfiguration-Exploit](https://github.com/davidoberst/CVE-2025-50579-CORS-Misconfiguration-Exploit) : ![starts](https://img.shields.io/github/stars/davidoberst/CVE-2025-50579-CORS-Misconfiguration-Exploit.svg) ![forks](https://img.shields.io/github/forks/davidoberst/CVE-2025-50579-CORS-Misconfiguration-Exploit.svg)

## CVE-2025-55182
> A pre-authentication remote code execution vulnerability exists in React Server Components versions 19.0.0, 19.1.0, 19.1.1, and 19.2.0 including the following packages: react-server-dom-parcel, react-server-dom-turbopack, and react-server-dom-webpack. The vulnerable code unsafely deserializes payloads from HTTP requests to Server Function endpoints.

- [https://github.com/sg-evals/react--v19.2.1](https://github.com/sg-evals/react--v19.2.1) : ![starts](https://img.shields.io/github/stars/sg-evals/react--v19.2.1.svg) ![forks](https://img.shields.io/github/forks/sg-evals/react--v19.2.1.svg)

## CVE-2026-102334
> Nginx Proxy Manager through 2.16.0 lacks rate-limiting on authentication endpoints, allowing unauthenticated attackers to make unlimited password guesses against any account. Attackers can brute-force login credentials via POST /api/tokens and subsequently guess TOTP codes via POST /api/tokens/2fa to gain full session access and administrative control.

- [https://github.com/davidoberst/CVE-2026-102334-exploit](https://github.com/davidoberst/CVE-2026-102334-exploit) : ![starts](https://img.shields.io/github/stars/davidoberst/CVE-2026-102334-exploit.svg) ![forks](https://img.shields.io/github/forks/davidoberst/CVE-2026-102334-exploit.svg)

## CVE-2026-104935
> Authentication bypass by spoofing in ICS before version 25.1.3.0 allows a remote unauthenticated attacker to execute arbitrary commands. This does not impact ICS version 22.7R2.14 or prior.

- [https://github.com/CompleteTech-Security/ivanti-connect-secure-cve-2026-104935-check](https://github.com/CompleteTech-Security/ivanti-connect-secure-cve-2026-104935-check) : ![starts](https://img.shields.io/github/stars/CompleteTech-Security/ivanti-connect-secure-cve-2026-104935-check.svg) ![forks](https://img.shields.io/github/forks/CompleteTech-Security/ivanti-connect-secure-cve-2026-104935-check.svg)

## CVE-2026-109618
> PHP uses longjmp() for out-of-memory (OOM) errors to exit the current context and abort handling of the request. Some contexts may not properly account for this scenario and leave request memory in an uninitialized state before performing an allocation. The subsequent request cleanup procedure may read or branch on this memory. Multiple OOM strategies can consistently trigger this condition and lead to remote code execution (RCE).

- [https://github.com/siedysoes/php2shell-scanner](https://github.com/siedysoes/php2shell-scanner) : ![starts](https://img.shields.io/github/stars/siedysoes/php2shell-scanner.svg) ![forks](https://img.shields.io/github/forks/siedysoes/php2shell-scanner.svg)

## CVE-2026-112688
> A memory corruption issue was addressed with improved memory handling. This issue is fixed in iOS 26.7 and iPadOS 26.7, iOS 27.2 and iPadOS 27.2, macOS Golden Gate 27.2, macOS Sequoia 15.8.2, macOS Tahoe 26.7.2. Parsing a file may lead to an unexpected app termination or arbitrary code execution.

- [https://github.com/xcbjkymz/cve-2026-112688-oobw](https://github.com/xcbjkymz/cve-2026-112688-oobw) : ![starts](https://img.shields.io/github/stars/xcbjkymz/cve-2026-112688-oobw.svg) ![forks](https://img.shields.io/github/forks/xcbjkymz/cve-2026-112688-oobw.svg)

## CVE-2026-121720

- [https://github.com/refiaa/CVE-2026-121720](https://github.com/refiaa/CVE-2026-121720) : ![starts](https://img.shields.io/github/stars/refiaa/CVE-2026-121720.svg) ![forks](https://img.shields.io/github/forks/refiaa/CVE-2026-121720.svg)

## CVE-2026-122158
> A security flaw has been discovered in InvoiceShelf up to 2.4.3/3.0.0-alpha.3. Affected by this issue is the function MemberService::create of the file app/Domains/Accounts/Application/MemberService.php. Performing a manipulation of the argument companies[].id/companies[].role results in improper access controls. The attack is possible to be carried out remotely. The exploit has been released to the public and may be used for attacks. Upgrading to version 2.4.4 and 3.0.0-alpha.4 can resolve this

- [https://github.com/capivara-research/CVE-2026-122158](https://github.com/capivara-research/CVE-2026-122158) : ![starts](https://img.shields.io/github/stars/capivara-research/CVE-2026-122158.svg) ![forks](https://img.shields.io/github/forks/capivara-research/CVE-2026-122158.svg)

## CVE-2026-123158
> sshd in OpenSSH before 10.6p2 on Linux, when musl libc is used without PAM, lacks a workaround for a password authentication bypass (related to misinterpretation of whether a string is intended to be a password hash). For some configurations of accounts, any password between 256 and 1024 characters succeeds. An example of a platform using musl libc without PAM is Alpine Linux.

- [https://github.com/ersinkoc/sshole-check](https://github.com/ersinkoc/sshole-check) : ![starts](https://img.shields.io/github/stars/ersinkoc/sshole-check.svg) ![forks](https://img.shields.io/github/forks/ersinkoc/sshole-check.svg)
- [https://github.com/gabrielunknown/CVE-2026-123158_SSHole](https://github.com/gabrielunknown/CVE-2026-123158_SSHole) : ![starts](https://img.shields.io/github/stars/gabrielunknown/CVE-2026-123158_SSHole.svg) ![forks](https://img.shields.io/github/forks/gabrielunknown/CVE-2026-123158_SSHole.svg)
- [https://github.com/rothoma2/cve-2026-123158-sshole](https://github.com/rothoma2/cve-2026-123158-sshole) : ![starts](https://img.shields.io/github/stars/rothoma2/cve-2026-123158-sshole.svg) ![forks](https://img.shields.io/github/forks/rothoma2/cve-2026-123158-sshole.svg)

## CVE-2026-33439

- [https://github.com/duohnson/CVE-2026-33439-PoC](https://github.com/duohnson/CVE-2026-33439-PoC) : ![starts](https://img.shields.io/github/stars/duohnson/CVE-2026-33439-PoC.svg) ![forks](https://img.shields.io/github/forks/duohnson/CVE-2026-33439-PoC.svg)

## CVE-2026-76142
> Insufficient authentication and access control on the internal-only IPC SOAP endpoint of the Genian NAC/ZTNA policy server allows an unauthenticated attacker to invoke internal functions

- [https://github.com/MalHyuk/CVE-2026-76142](https://github.com/MalHyuk/CVE-2026-76142) : ![starts](https://img.shields.io/github/stars/MalHyuk/CVE-2026-76142.svg) ![forks](https://img.shields.io/github/forks/MalHyuk/CVE-2026-76142.svg)
