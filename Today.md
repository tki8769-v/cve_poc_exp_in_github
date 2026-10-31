# Update 2026-10-31
## CVE-2012-0002

- [https://github.com/engineer-lucasmcmelo/CVE-2012-0002](https://github.com/engineer-lucasmcmelo/CVE-2012-0002) : ![starts](https://img.shields.io/github/stars/engineer-lucasmcmelo/CVE-2012-0002.svg) ![forks](https://img.shields.io/github/forks/engineer-lucasmcmelo/CVE-2012-0002.svg)

## CVE-2021-3493

- [https://github.com/devloperhalaand-ship-it/TryHackMe-OverlayFS---CVE-2021-3493](https://github.com/devloperhalaand-ship-it/TryHackMe-OverlayFS---CVE-2021-3493) : ![starts](https://img.shields.io/github/stars/devloperhalaand-ship-it/TryHackMe-OverlayFS---CVE-2021-3493.svg) ![forks](https://img.shields.io/github/forks/devloperhalaand-ship-it/TryHackMe-OverlayFS---CVE-2021-3493.svg)

## CVE-2024-21626

- [https://github.com/Leven0101/cve-2024-21626-lab](https://github.com/Leven0101/cve-2024-21626-lab) : ![starts](https://img.shields.io/github/stars/Leven0101/cve-2024-21626-lab.svg) ![forks](https://img.shields.io/github/forks/Leven0101/cve-2024-21626-lab.svg)

## CVE-2026-101767

- [https://github.com/shivrajem/ebs-cve-2026-101767-check](https://github.com/shivrajem/ebs-cve-2026-101767-check) : ![starts](https://img.shields.io/github/stars/shivrajem/ebs-cve-2026-101767-check.svg) ![forks](https://img.shields.io/github/forks/shivrajem/ebs-cve-2026-101767-check.svg)

## CVE-2026-109618
> PHP uses longjmp() for out-of-memory (OOM) errors to exit the current context and abort handling of the request. Some contexts may not properly account for this scenario and leave request memory in an uninitialized state before performing an allocation. The subsequent request cleanup procedure may read or branch on this memory. Multiple OOM strategies can consistently trigger this condition and lead to remote code execution (RCE).

- [https://github.com/Lydia-King-K/ddld36-solar-aegis](https://github.com/Lydia-King-K/ddld36-solar-aegis) : ![starts](https://img.shields.io/github/stars/Lydia-King-K/ddld36-solar-aegis.svg) ![forks](https://img.shields.io/github/forks/Lydia-King-K/ddld36-solar-aegis.svg)

## CVE-2026-111497
> A buffer overflow vulnerability in the Brotli decoder (c/dec/decode.c) in Google Brotli versions 1.0.3 through 1.2.0 on all platforms allows a remote unauthenticated attacker to corrupt adjacent decoder state memory, disclose sensitive memory contents, cause a denial of service, or potentially execute arbitrary code using a crafted Brotli-compressed stream.





Users need to update any Brotli libraries or binaries between 1.0.3 through 1.2.0 to the latest available version: 1.0.10 or 1.1.1 or 1

- [https://github.com/adachis/pillow-patched-brotli](https://github.com/adachis/pillow-patched-brotli) : ![starts](https://img.shields.io/github/stars/adachis/pillow-patched-brotli.svg) ![forks](https://img.shields.io/github/forks/adachis/pillow-patched-brotli.svg)
- [https://github.com/dansaurabh/brotli2shell_Hunter](https://github.com/dansaurabh/brotli2shell_Hunter) : ![starts](https://img.shields.io/github/stars/dansaurabh/brotli2shell_Hunter.svg) ![forks](https://img.shields.io/github/forks/dansaurabh/brotli2shell_Hunter.svg)

## CVE-2026-116366

- [https://github.com/googlesky/CVE-2026-116366](https://github.com/googlesky/CVE-2026-116366) : ![starts](https://img.shields.io/github/stars/googlesky/CVE-2026-116366.svg) ![forks](https://img.shields.io/github/forks/googlesky/CVE-2026-116366.svg)

## CVE-2026-119712

- [https://github.com/hyderpwn/CVE-pipeshub](https://github.com/hyderpwn/CVE-pipeshub) : ![starts](https://img.shields.io/github/stars/hyderpwn/CVE-pipeshub.svg) ![forks](https://img.shields.io/github/forks/hyderpwn/CVE-pipeshub.svg)

## CVE-2026-46300
> In the Linux kernel, the following vulnerability has been resolved:

net: skbuff: preserve shared-frag marker during coalescing

skb_try_coalesce() can attach paged frags from @from to @to.  If @from
has SKBFL_SHARED_FRAG set, the resulting @to skb can contain the same
externally-owned or page-cache-backed frags, but the shared-frag marker
is currently lost.

That breaks the invariant relied on by later in-place writers.  In
particular, ESP input checks skb_has_shared_frag() before deciding
whet

- [https://github.com/foxcornlab/fragnesia-scanner](https://github.com/foxcornlab/fragnesia-scanner) : ![starts](https://img.shields.io/github/stars/foxcornlab/fragnesia-scanner.svg) ![forks](https://img.shields.io/github/forks/foxcornlab/fragnesia-scanner.svg)

## CVE-2026-98432
> In the Linux kernel, the following vulnerability has been resolved:

ipv4: free inet_opt and ireq_opt after an RCU grace period

tcp_v4_syn_recv_sock() transfers ownership of ireq-&gt;ireq_opt to the
child socket (newinet-&gt;inet_opt) without copying it.

Another cpu can concurrently process a retransmitted SYN for the same
request socket, and send a SYNACK from tcp_check_req().
tcp_v4_send_synack() and inet_csk_route_req() read ireq-&gt;ireq_opt
under rcu_read_lock() only, and ip_build_and_send_pkt() a

- [https://github.com/alvaroguzmancode/cve-2026-98432](https://github.com/alvaroguzmancode/cve-2026-98432) : ![starts](https://img.shields.io/github/stars/alvaroguzmancode/cve-2026-98432.svg) ![forks](https://img.shields.io/github/forks/alvaroguzmancode/cve-2026-98432.svg)
- [https://github.com/brett6320/fix_CVE-2026-98432](https://github.com/brett6320/fix_CVE-2026-98432) : ![starts](https://img.shields.io/github/stars/brett6320/fix_CVE-2026-98432.svg) ![forks](https://img.shields.io/github/forks/brett6320/fix_CVE-2026-98432.svg)
- [https://github.com/tiendungdev/cve-2026-98432-guard](https://github.com/tiendungdev/cve-2026-98432-guard) : ![starts](https://img.shields.io/github/stars/tiendungdev/cve-2026-98432-guard.svg) ![forks](https://img.shields.io/github/forks/tiendungdev/cve-2026-98432-guard.svg)
