# Update 2026-11-13
## CVE-2021-23337
> Lodash versions prior to 4.17.21 are vulnerable to Command Injection via the template function.

- [https://github.com/mcpmark-eval-liuhezi/ghsa-lodash-ci-7f3c9a](https://github.com/mcpmark-eval-liuhezi/ghsa-lodash-ci-7f3c9a) : ![starts](https://img.shields.io/github/stars/mcpmark-eval-liuhezi/ghsa-lodash-ci-7f3c9a.svg) ![forks](https://img.shields.io/github/forks/mcpmark-eval-liuhezi/ghsa-lodash-ci-7f3c9a.svg)

## CVE-2024-51482

- [https://github.com/ehl0707/CVE-2024-51482-ZoneMinder-CCTV-HTB-Reliable-EXP](https://github.com/ehl0707/CVE-2024-51482-ZoneMinder-CCTV-HTB-Reliable-EXP) : ![starts](https://img.shields.io/github/stars/ehl0707/CVE-2024-51482-ZoneMinder-CCTV-HTB-Reliable-EXP.svg) ![forks](https://img.shields.io/github/forks/ehl0707/CVE-2024-51482-ZoneMinder-CCTV-HTB-Reliable-EXP.svg)

## CVE-2026-109618
> PHP uses longjmp() for out-of-memory (OOM) errors to exit the current context and abort handling of the request. Some contexts may not properly account for this scenario and leave request memory in an uninitialized state before performing an allocation. The subsequent request cleanup procedure may read or branch on this memory. Multiple OOM strategies can consistently trigger this condition and lead to remote code execution (RCE).

- [https://github.com/che3axujnya/cve-2026-109618-cve-2026-109619-poc](https://github.com/che3axujnya/cve-2026-109618-cve-2026-109619-poc) : ![starts](https://img.shields.io/github/stars/che3axujnya/cve-2026-109618-cve-2026-109619-poc.svg) ![forks](https://img.shields.io/github/forks/che3axujnya/cve-2026-109618-cve-2026-109619-poc.svg)
- [https://github.com/mxxnknght/php2shell-CVE-2026-109618-CVE-2026-109619-Dorks](https://github.com/mxxnknght/php2shell-CVE-2026-109618-CVE-2026-109619-Dorks) : ![starts](https://img.shields.io/github/stars/mxxnknght/php2shell-CVE-2026-109618-CVE-2026-109619-Dorks.svg) ![forks](https://img.shields.io/github/forks/mxxnknght/php2shell-CVE-2026-109618-CVE-2026-109619-Dorks.svg)

## CVE-2026-109619
> PHP has various global state that temporarily points into request memory. In some scenarios, global state may not be correctly reset, or may be repopulated after being reset. The global state may then refer to request memory even after it has been freed. Subsequent requests may read or branch on this stale state before it is fully initialized. Multiple strategies can trigger this condition and produce remote code execution (RCE).

- [https://github.com/mxxnknght/php2shell-CVE-2026-109618-CVE-2026-109619-Dorks](https://github.com/mxxnknght/php2shell-CVE-2026-109618-CVE-2026-109619-Dorks) : ![starts](https://img.shields.io/github/stars/mxxnknght/php2shell-CVE-2026-109618-CVE-2026-109619-Dorks.svg) ![forks](https://img.shields.io/github/forks/mxxnknght/php2shell-CVE-2026-109618-CVE-2026-109619-Dorks.svg)

## CVE-2026-119618

- [https://github.com/LLCForge/CVE-2026-119618](https://github.com/LLCForge/CVE-2026-119618) : ![starts](https://img.shields.io/github/stars/LLCForge/CVE-2026-119618.svg) ![forks](https://img.shields.io/github/forks/LLCForge/CVE-2026-119618.svg)
- [https://github.com/jeffschafer/Apache-HTTP2-RCE-HEAP-CORRUPTION-CVE-2026-119618-STAND-ALONE-SCANNER](https://github.com/jeffschafer/Apache-HTTP2-RCE-HEAP-CORRUPTION-CVE-2026-119618-STAND-ALONE-SCANNER) : ![starts](https://img.shields.io/github/stars/jeffschafer/Apache-HTTP2-RCE-HEAP-CORRUPTION-CVE-2026-119618-STAND-ALONE-SCANNER.svg) ![forks](https://img.shields.io/github/forks/jeffschafer/Apache-HTTP2-RCE-HEAP-CORRUPTION-CVE-2026-119618-STAND-ALONE-SCANNER.svg)

## CVE-2026-31431
> In the Linux kernel, the following vulnerability has been resolved:

crypto: algif_aead - Revert to operating out-of-place

This mostly reverts commit 72548b093ee3 except for the copying of
the associated data.

There is no benefit in operating in-place in algif_aead since the
source and destination come from different mappings.  Get rid of
all the complexity added for in-place operation and just copy the
AD directly.

- [https://github.com/CypherMux/CopyFix](https://github.com/CypherMux/CopyFix) : ![starts](https://img.shields.io/github/stars/CypherMux/CopyFix.svg) ![forks](https://img.shields.io/github/forks/CypherMux/CopyFix.svg)

## CVE-2026-56290
> Joomla Extension - joomlack.fr - Unauthenticated file upload in Page Builder CK extension &lt; 3.6.0 - The Joomla extension Page Builder CK is vulnerable to an unauthenticated arbitrary file upload that allows uploading executable files and leads to full RCE.

- [https://github.com/Mushr00w/CVE-2026-56290](https://github.com/Mushr00w/CVE-2026-56290) : ![starts](https://img.shields.io/github/stars/Mushr00w/CVE-2026-56290.svg) ![forks](https://img.shields.io/github/forks/Mushr00w/CVE-2026-56290.svg)

## CVE-2026-97793

- [https://github.com/yo-yo-yo-jbo/intro_to_com](https://github.com/yo-yo-yo-jbo/intro_to_com) : ![starts](https://img.shields.io/github/stars/yo-yo-yo-jbo/intro_to_com.svg) ![forks](https://img.shields.io/github/forks/yo-yo-yo-jbo/intro_to_com.svg)

## CVE-2026-98260
> In the Linux kernel, the following vulnerability has been resolved:

exec: Cleanup POSIX timers right after de_thread()

A per-thread CPU timer holds a reference to the PID of the thread it is
attached to and, while it is armed, its node is queued in that thread&#x27;s
posix_cputimers. The task is looked up by that PID.

When a non-leader thread exec()s, de_thread() changes which task owns
that PID. pid_task(timer-&gt;it.cpu.pid, PIDTYPE_PID) then returns NULL,
but the node is still queued on tsk, which

- [https://github.com/mumaosong/CVE-2026-98260-Drive](https://github.com/mumaosong/CVE-2026-98260-Drive) : ![starts](https://img.shields.io/github/stars/mumaosong/CVE-2026-98260-Drive.svg) ![forks](https://img.shields.io/github/forks/mumaosong/CVE-2026-98260-Drive.svg)
