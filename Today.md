# Update 2026-10-23
## CVE-2021-44228

- [https://github.com/mcpmark-eval-liuhezi/log4shell-audit-evidence](https://github.com/mcpmark-eval-liuhezi/log4shell-audit-evidence) : ![starts](https://img.shields.io/github/stars/mcpmark-eval-liuhezi/log4shell-audit-evidence.svg) ![forks](https://img.shields.io/github/forks/mcpmark-eval-liuhezi/log4shell-audit-evidence.svg)

## CVE-2025-54309

- [https://github.com/Goodworkid0/CrushFTP-AS2-Bypass-Research-CVE-2025-54309](https://github.com/Goodworkid0/CrushFTP-AS2-Bypass-Research-CVE-2025-54309) : ![starts](https://img.shields.io/github/stars/Goodworkid0/CrushFTP-AS2-Bypass-Research-CVE-2025-54309.svg) ![forks](https://img.shields.io/github/forks/Goodworkid0/CrushFTP-AS2-Bypass-Research-CVE-2025-54309.svg)

## CVE-2026-106991

- [https://github.com/MX-Qulin/CVE-2026-106991](https://github.com/MX-Qulin/CVE-2026-106991) : ![starts](https://img.shields.io/github/stars/MX-Qulin/CVE-2026-106991.svg) ![forks](https://img.shields.io/github/forks/MX-Qulin/CVE-2026-106991.svg)

## CVE-2026-109255
> FreeRDP 3.0.0 before 3.32.0 contains an integer truncation vulnerability in license_check_stream_length that allows a malicious RDP server to trigger a heap buffer overflow on 32-bit clients. Attackers can send a crafted SERVER_LICENSE_REQUEST with a large scopeCount that bypasses length checks, causing out-of-bounds writes leading to denial of service or remote code execution.

- [https://github.com/D7EAD/CVE-2026-109255](https://github.com/D7EAD/CVE-2026-109255) : ![starts](https://img.shields.io/github/stars/D7EAD/CVE-2026-109255.svg) ![forks](https://img.shields.io/github/forks/D7EAD/CVE-2026-109255.svg)

## CVE-2026-109618
> PHP uses longjmp() for out-of-memory (OOM) errors to exit the current context and abort handling of the request. Some contexts may not properly account for this scenario and leave request memory in an uninitialized state before performing an allocation. The subsequent request cleanup procedure may read or branch on this memory. Multiple OOM strategies can consistently trigger this condition and lead to remote code execution (RCE).

- [https://github.com/JoasASantos/php2shell-exploit](https://github.com/JoasASantos/php2shell-exploit) : ![starts](https://img.shields.io/github/stars/JoasASantos/php2shell-exploit.svg) ![forks](https://img.shields.io/github/forks/JoasASantos/php2shell-exploit.svg)
- [https://github.com/JoasASantos/php2shell-lab](https://github.com/JoasASantos/php2shell-lab) : ![starts](https://img.shields.io/github/stars/JoasASantos/php2shell-lab.svg) ![forks](https://img.shields.io/github/forks/JoasASantos/php2shell-lab.svg)
- [https://github.com/mc493/php2shell-enterprise-hardening-cve-2026-109618-109619](https://github.com/mc493/php2shell-enterprise-hardening-cve-2026-109618-109619) : ![starts](https://img.shields.io/github/stars/mc493/php2shell-enterprise-hardening-cve-2026-109618-109619.svg) ![forks](https://img.shields.io/github/forks/mc493/php2shell-enterprise-hardening-cve-2026-109618-109619.svg)
- [https://github.com/memuratozturk/php2shell-poc](https://github.com/memuratozturk/php2shell-poc) : ![starts](https://img.shields.io/github/stars/memuratozturk/php2shell-poc.svg) ![forks](https://img.shields.io/github/forks/memuratozturk/php2shell-poc.svg)

## CVE-2026-110264
> An issue has been discovered in GitLab CE/EE affecting all versions from 7.0 before 18.11.13, 19.0 before 19.0.10, 19.1 before 19.1.9, 19.2 before 19.2.9, 19.3 before 19.3.6, 19.4 before 19.4.3, and 19.5 before 19.5.1 that, under certain conditions, could have allowed an unauthenticated user to execute arbitrary code on the GitLab server due to integer overflow when compiling a specially crafted regular expression.

- [https://github.com/xaviware/go-gitlab-cve-2026-110264-scanner](https://github.com/xaviware/go-gitlab-cve-2026-110264-scanner) : ![starts](https://img.shields.io/github/stars/xaviware/go-gitlab-cve-2026-110264-scanner.svg) ![forks](https://img.shields.io/github/forks/xaviware/go-gitlab-cve-2026-110264-scanner.svg)

## CVE-2026-114101

- [https://github.com/cafaye/nilepatch-coraza-bypass](https://github.com/cafaye/nilepatch-coraza-bypass) : ![starts](https://img.shields.io/github/stars/cafaye/nilepatch-coraza-bypass.svg) ![forks](https://img.shields.io/github/forks/cafaye/nilepatch-coraza-bypass.svg)

## CVE-2026-114102
> adm-zip before 0.6.1 contains a denial of service vulnerability that allows unauthenticated attackers to crash the Node.js process via a malformed ZIP file, because inflateAsync in methods/inflater.js lacks a zlib stream error listener. Attackers can supply a ZIP with corrupted DEFLATE data processed by readFileAsync, readAsTextAsync, extractAllToAsync, or getDataAsync, triggering an uncatchable exception that terminates all in-flight requests.

- [https://github.com/cafaye/nilepatch-admzip-dos](https://github.com/cafaye/nilepatch-admzip-dos) : ![starts](https://img.shields.io/github/stars/cafaye/nilepatch-admzip-dos.svg) ![forks](https://img.shields.io/github/forks/cafaye/nilepatch-admzip-dos.svg)

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

- [https://github.com/wazzuj99-svg/Root-My-Galaxy](https://github.com/wazzuj99-svg/Root-My-Galaxy) : ![starts](https://img.shields.io/github/stars/wazzuj99-svg/Root-My-Galaxy.svg) ![forks](https://img.shields.io/github/forks/wazzuj99-svg/Root-My-Galaxy.svg)
