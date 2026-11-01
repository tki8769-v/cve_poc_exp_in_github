# Update 2026-11-01
## CVE-2026-109618
> PHP uses longjmp() for out-of-memory (OOM) errors to exit the current context and abort handling of the request. Some contexts may not properly account for this scenario and leave request memory in an uninitialized state before performing an allocation. The subsequent request cleanup procedure may read or branch on this memory. Multiple OOM strategies can consistently trigger this condition and lead to remote code execution (RCE).

- [https://github.com/catscarlet/php-fpm-docker-PHP-7.4-CVE-2026-109618-109619-patched](https://github.com/catscarlet/php-fpm-docker-PHP-7.4-CVE-2026-109618-109619-patched) : ![starts](https://img.shields.io/github/stars/catscarlet/php-fpm-docker-PHP-7.4-CVE-2026-109618-109619-patched.svg) ![forks](https://img.shields.io/github/forks/catscarlet/php-fpm-docker-PHP-7.4-CVE-2026-109618-109619-patched.svg)

## CVE-2026-118764
> minimatch is a minimal matching utility for converting glob expressions into JavaScript RegExp objects. Prior to 11.0.1, src/index.ts implements firstPhasePreProcess() so that, at optimizationLevel 2 or higher, it repeatedly expands attacker-controlled **/.. pattern segments inside a fixpoint loop, allowing generated globParts entries to be processed and expanded again. secondPhasePreProcess() then compares the expanded entries pairwise, so a short malicious glob can cause excessive CPU and memo

- [https://github.com/b1nv0id/CVE-2026-118764](https://github.com/b1nv0id/CVE-2026-118764) : ![starts](https://img.shields.io/github/stars/b1nv0id/CVE-2026-118764.svg) ![forks](https://img.shields.io/github/forks/b1nv0id/CVE-2026-118764.svg)
