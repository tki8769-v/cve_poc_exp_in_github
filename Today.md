# Update 2026-10-28
## CVE-2014-6271

- [https://github.com/ItzSteve04/shellshock-linux-host-hardening-lab](https://github.com/ItzSteve04/shellshock-linux-host-hardening-lab) : ![starts](https://img.shields.io/github/stars/ItzSteve04/shellshock-linux-host-hardening-lab.svg) ![forks](https://img.shields.io/github/forks/ItzSteve04/shellshock-linux-host-hardening-lab.svg)

## CVE-2017-1000486

- [https://github.com/keitan339/primefaces-cve-2017-1000486](https://github.com/keitan339/primefaces-cve-2017-1000486) : ![starts](https://img.shields.io/github/stars/keitan339/primefaces-cve-2017-1000486.svg) ![forks](https://img.shields.io/github/forks/keitan339/primefaces-cve-2017-1000486.svg)

## CVE-2018-17246

- [https://github.com/ght657/work1-secure-api](https://github.com/ght657/work1-secure-api) : ![starts](https://img.shields.io/github/stars/ght657/work1-secure-api.svg) ![forks](https://img.shields.io/github/forks/ght657/work1-secure-api.svg)

## CVE-2019-18935

- [https://github.com/piecar21/CVE-2019-18935](https://github.com/piecar21/CVE-2019-18935) : ![starts](https://img.shields.io/github/stars/piecar21/CVE-2019-18935.svg) ![forks](https://img.shields.io/github/forks/piecar21/CVE-2019-18935.svg)

## CVE-2022-30781

- [https://github.com/403ArkhamS3c/cve-gitea](https://github.com/403ArkhamS3c/cve-gitea) : ![starts](https://img.shields.io/github/stars/403ArkhamS3c/cve-gitea.svg) ![forks](https://img.shields.io/github/forks/403ArkhamS3c/cve-gitea.svg)

## CVE-2024-49138

- [https://github.com/Dudasantluiz/Triagem-de-Explora-o-CVE-2024-49138-detectada](https://github.com/Dudasantluiz/Triagem-de-Explora-o-CVE-2024-49138-detectada) : ![starts](https://img.shields.io/github/stars/Dudasantluiz/Triagem-de-Explora-o-CVE-2024-49138-detectada.svg) ![forks](https://img.shields.io/github/forks/Dudasantluiz/Triagem-de-Explora-o-CVE-2024-49138-detectada.svg)

## CVE-2026-105482
> A flaw in Node.js DNS resolution allows hostnames containing a NUL byte to be silently truncated by the dns.resolve*() functions and dns.reverse(). This is an incomplete fix of CVE-2026-48930, which only covered dns.lookup() and the net/tls host options.

Because the name is passed to c-ares as a C string, resolving attacker.example\0.trusted.example queries attacker.example and returns its records without any error. Applications that validate a hostname, for example against a domain allowlist

- [https://github.com/EthanTech-Offical/CVE-2026-105482-Reproduce](https://github.com/EthanTech-Offical/CVE-2026-105482-Reproduce) : ![starts](https://img.shields.io/github/stars/EthanTech-Offical/CVE-2026-105482-Reproduce.svg) ![forks](https://img.shields.io/github/forks/EthanTech-Offical/CVE-2026-105482-Reproduce.svg)

## CVE-2026-109618
> PHP uses longjmp() for out-of-memory (OOM) errors to exit the current context and abort handling of the request. Some contexts may not properly account for this scenario and leave request memory in an uninitialized state before performing an allocation. The subsequent request cleanup procedure may read or branch on this memory. Multiple OOM strategies can consistently trigger this condition and lead to remote code execution (RCE).

- [https://github.com/lflare/php2shell-cve-2026-109618-109619](https://github.com/lflare/php2shell-cve-2026-109618-109619) : ![starts](https://img.shields.io/github/stars/lflare/php2shell-cve-2026-109618-109619.svg) ![forks](https://img.shields.io/github/forks/lflare/php2shell-cve-2026-109618-109619.svg)
- [https://github.com/rayaar/php2shellPoc](https://github.com/rayaar/php2shellPoc) : ![starts](https://img.shields.io/github/stars/rayaar/php2shellPoc.svg) ![forks](https://img.shields.io/github/forks/rayaar/php2shellPoc.svg)

## CVE-2026-111497
> A buffer overflow vulnerability in the Brotli decoder (c/dec/decode.c) in Google Brotli versions 1.0.3 through 1.2.0 on all platforms allows a remote unauthenticated attacker to corrupt adjacent decoder state memory, disclose sensitive memory contents, cause a denial of service, or potentially execute arbitrary code using a crafted Brotli-compressed stream.





Users need to update any Brotli libraries or binaries between 1.0.3 through 1.2.0 to the latest available version: 1.0.10 or 1.1.1 or 1

- [https://github.com/suominen/CVE-2026-111497](https://github.com/suominen/CVE-2026-111497) : ![starts](https://img.shields.io/github/stars/suominen/CVE-2026-111497.svg) ![forks](https://img.shields.io/github/forks/suominen/CVE-2026-111497.svg)
- [https://github.com/thebarel/CVE-2026-111497](https://github.com/thebarel/CVE-2026-111497) : ![starts](https://img.shields.io/github/stars/thebarel/CVE-2026-111497.svg) ![forks](https://img.shields.io/github/forks/thebarel/CVE-2026-111497.svg)

## CVE-2026-115560

- [https://github.com/Pr0fEs0r-X/PHP2SHELL-Checker-v-1.0-CVE-2026-115560-](https://github.com/Pr0fEs0r-X/PHP2SHELL-Checker-v-1.0-CVE-2026-115560-) : ![starts](https://img.shields.io/github/stars/Pr0fEs0r-X/PHP2SHELL-Checker-v-1.0-CVE-2026-115560-.svg) ![forks](https://img.shields.io/github/forks/Pr0fEs0r-X/PHP2SHELL-Checker-v-1.0-CVE-2026-115560-.svg)
- [https://github.com/Pr0fEs0r-X/PHP2SHELL-Checker-v-2.0-CVE-2026-115560-](https://github.com/Pr0fEs0r-X/PHP2SHELL-Checker-v-2.0-CVE-2026-115560-) : ![starts](https://img.shields.io/github/stars/Pr0fEs0r-X/PHP2SHELL-Checker-v-2.0-CVE-2026-115560-.svg) ![forks](https://img.shields.io/github/forks/Pr0fEs0r-X/PHP2SHELL-Checker-v-2.0-CVE-2026-115560-.svg)

## CVE-2026-116692
> MLflow is an open source AI engineering platform for agents, large language models, and machine learning models. From 3.12.0rc0 until 3.17.0, third-party scorer deserialization in mlflow/genai/scorers/base.py accepts request-selected descendants of THIRD_PARTY_SCORER_ALLOWED_MODULES rather than requiring an exact allowed module. A caller can use MLflow artifact endpoints to place a Python module beneath a writable allowed package and submit its module and class through /ajax-api/3.0/mlflow/score

- [https://github.com/foxcornlab/mlflow-scorer-scanner](https://github.com/foxcornlab/mlflow-scorer-scanner) : ![starts](https://img.shields.io/github/stars/foxcornlab/mlflow-scorer-scanner.svg) ![forks](https://img.shields.io/github/forks/foxcornlab/mlflow-scorer-scanner.svg)

## CVE-2026-118238

- [https://github.com/Cushz/CVE-2026-118238](https://github.com/Cushz/CVE-2026-118238) : ![starts](https://img.shields.io/github/stars/Cushz/CVE-2026-118238.svg) ![forks](https://img.shields.io/github/forks/Cushz/CVE-2026-118238.svg)

## CVE-2026-1277

- [https://github.com/piecar21/CVE-2026-1277](https://github.com/piecar21/CVE-2026-1277) : ![starts](https://img.shields.io/github/stars/piecar21/CVE-2026-1277.svg) ![forks](https://img.shields.io/github/forks/piecar21/CVE-2026-1277.svg)

## CVE-2026-38056

- [https://github.com/sudo5Q/CVE-2026-38056-PoC](https://github.com/sudo5Q/CVE-2026-38056-PoC) : ![starts](https://img.shields.io/github/stars/sudo5Q/CVE-2026-38056-PoC.svg) ![forks](https://img.shields.io/github/forks/sudo5Q/CVE-2026-38056-PoC.svg)

## CVE-2026-42530

- [https://github.com/Udyz/CVE-2026-42530](https://github.com/Udyz/CVE-2026-42530) : ![starts](https://img.shields.io/github/stars/Udyz/CVE-2026-42530.svg) ![forks](https://img.shields.io/github/forks/Udyz/CVE-2026-42530.svg)

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

- [https://github.com/Syerain/cve-2026-43499-mt6896-pd2238](https://github.com/Syerain/cve-2026-43499-mt6896-pd2238) : ![starts](https://img.shields.io/github/stars/Syerain/cve-2026-43499-mt6896-pd2238.svg) ![forks](https://img.shields.io/github/forks/Syerain/cve-2026-43499-mt6896-pd2238.svg)
- [https://github.com/tokenbleed/ghostlock-tv](https://github.com/tokenbleed/ghostlock-tv) : ![starts](https://img.shields.io/github/stars/tokenbleed/ghostlock-tv.svg) ![forks](https://img.shields.io/github/forks/tokenbleed/ghostlock-tv.svg)

## CVE-2026-9539

- [https://github.com/quarkslab/slirp_snapshots_stateful](https://github.com/quarkslab/slirp_snapshots_stateful) : ![starts](https://img.shields.io/github/stars/quarkslab/slirp_snapshots_stateful.svg) ![forks](https://img.shields.io/github/forks/quarkslab/slirp_snapshots_stateful.svg)

## CVE-2026-96778
> Pillow is a Python imaging library. From 9.4.0 until 13.0.0, ImagingJpegEncode() in src/libImaging/JpegEncode.c can call jpeg_write_marker() for a JPEG COM comment when an ICC profile has exactly filled the 65536-byte encoder buffer. libjpeg writes one byte before checking the exhausted free_in_buffer counter, which then wraps and permits the attacker-controlled comment and subsequent compressed image data to overwrite adjacent heap memory. Re-saving an untrusted image as JPEG while preserving i

- [https://github.com/paktiko1986/CVE-2026-96778-pillow](https://github.com/paktiko1986/CVE-2026-96778-pillow) : ![starts](https://img.shields.io/github/stars/paktiko1986/CVE-2026-96778-pillow.svg) ![forks](https://img.shields.io/github/forks/paktiko1986/CVE-2026-96778-pillow.svg)

## CVE-2026-98260
> In the Linux kernel, the following vulnerability has been resolved:

exec: Cleanup POSIX timers right after de_thread()

A per-thread CPU timer holds a reference to the PID of the thread it is
attached to and, while it is armed, its node is queued in that thread&#x27;s
posix_cputimers. The task is looked up by that PID.

When a non-leader thread exec()s, de_thread() changes which task owns
that PID. pid_task(timer-&gt;it.cpu.pid, PIDTYPE_PID) then returns NULL,
but the node is still queued on tsk, which

- [https://github.com/4627488/cve-2026-98260-nezha](https://github.com/4627488/cve-2026-98260-nezha) : ![starts](https://img.shields.io/github/stars/4627488/cve-2026-98260-nezha.svg) ![forks](https://img.shields.io/github/forks/4627488/cve-2026-98260-nezha.svg)
- [https://github.com/zjns/CVE-2026-98260](https://github.com/zjns/CVE-2026-98260) : ![starts](https://img.shields.io/github/stars/zjns/CVE-2026-98260.svg) ![forks](https://img.shields.io/github/forks/zjns/CVE-2026-98260.svg)
