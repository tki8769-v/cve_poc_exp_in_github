# Update 2026-11-08
## CVE-2019-6693

- [https://github.com/lureprey/fortidecrypter-CVE-2019-6693](https://github.com/lureprey/fortidecrypter-CVE-2019-6693) : ![starts](https://img.shields.io/github/stars/lureprey/fortidecrypter-CVE-2019-6693.svg) ![forks](https://img.shields.io/github/forks/lureprey/fortidecrypter-CVE-2019-6693.svg)

## CVE-2026-123158
> sshd in OpenSSH before 10.6p2 on Linux, when musl libc is used without PAM, lacks a workaround for a password authentication bypass (related to misinterpretation of whether a string is intended to be a password hash). For some configurations of accounts, any password between 256 and 1024 characters succeeds. An example of a platform using musl libc without PAM is Alpine Linux.

- [https://github.com/liamromanis101/MaSSHole](https://github.com/liamromanis101/MaSSHole) : ![starts](https://img.shields.io/github/stars/liamromanis101/MaSSHole.svg) ![forks](https://img.shields.io/github/forks/liamromanis101/MaSSHole.svg)

## CVE-2026-42016

- [https://github.com/dylvie/CVE-2026-42016_CVE-2026-42018](https://github.com/dylvie/CVE-2026-42016_CVE-2026-42018) : ![starts](https://img.shields.io/github/stars/dylvie/CVE-2026-42016_CVE-2026-42018.svg) ![forks](https://img.shields.io/github/forks/dylvie/CVE-2026-42016_CVE-2026-42018.svg)

## CVE-2026-42018
> JFrog Artifactory could return an internal anonymous-user token to an unauthenticated caller when anonymous access is disabled, potentially exposing sensitive resources.

- [https://github.com/dylvie/CVE-2026-42016_CVE-2026-42018](https://github.com/dylvie/CVE-2026-42016_CVE-2026-42018) : ![starts](https://img.shields.io/github/stars/dylvie/CVE-2026-42016_CVE-2026-42018.svg) ![forks](https://img.shields.io/github/forks/dylvie/CVE-2026-42016_CVE-2026-42018.svg)

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

- [https://github.com/AksiSpirit/ghostlock-cve-2026-43499-4.19-k40](https://github.com/AksiSpirit/ghostlock-cve-2026-43499-4.19-k40) : ![starts](https://img.shields.io/github/stars/AksiSpirit/ghostlock-cve-2026-43499-4.19-k40.svg) ![forks](https://img.shields.io/github/forks/AksiSpirit/ghostlock-cve-2026-43499-4.19-k40.svg)
