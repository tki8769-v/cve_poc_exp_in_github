# Update 2026-11-28
## CVE-2021-44228

- [https://github.com/johnyProDev/CVE-2021-44228-Study](https://github.com/johnyProDev/CVE-2021-44228-Study) : ![starts](https://img.shields.io/github/stars/johnyProDev/CVE-2021-44228-Study.svg) ![forks](https://img.shields.io/github/forks/johnyProDev/CVE-2021-44228-Study.svg)

## CVE-2026-111497
> A buffer overflow vulnerability in the Brotli decoder (c/dec/decode.c) in Google Brotli versions 1.0.3 through 1.2.0 on all platforms allows a remote unauthenticated attacker to corrupt adjacent decoder state memory, disclose sensitive memory contents, cause a denial of service, or potentially execute arbitrary code using a crafted Brotli-compressed stream.





Users need to update any Brotli libraries or binaries between 1.0.3 through 1.2.0 to the latest available version: 1.0.10 or 1.1.1 or 1

- [https://github.com/Tenrion618/brscan](https://github.com/Tenrion618/brscan) : ![starts](https://img.shields.io/github/stars/Tenrion618/brscan.svg) ![forks](https://img.shields.io/github/forks/Tenrion618/brscan.svg)

## CVE-2026-129863
> GitBucket through 4.48.0 contains an incorrect authorization vulnerability that allows authenticated users to edit and merge other users&#x27; pull requests because the PATCH pulls and PUT pulls merge REST API endpoints only check read access. Attackers can close, reopen, retitle, retarget, or merge pull requests into the base branch without write permission on public repositories or as private-repository guest collaborators.

- [https://github.com/n4n45h1/CVE-2026-129863](https://github.com/n4n45h1/CVE-2026-129863) : ![starts](https://img.shields.io/github/stars/n4n45h1/CVE-2026-129863.svg) ![forks](https://img.shields.io/github/forks/n4n45h1/CVE-2026-129863.svg)

## CVE-2026-133250
> @fastify/middie is the middleware engine for the Fastify web framework. In versions up to and including 9.3.7, middie matches path-scoped middleware against its own reading of the request path, which can differ from the path Fastify&#x27;s router uses to dispatch the request. When the two disagree, the router can route a request to a handler covered by a middleware mount while middie skips that middleware, so an unauthenticated client reaches a handler that an authentication, authorization, or rate-l

- [https://github.com/googlesky/CVE-2026-133250](https://github.com/googlesky/CVE-2026-133250) : ![starts](https://img.shields.io/github/stars/googlesky/CVE-2026-133250.svg) ![forks](https://img.shields.io/github/forks/googlesky/CVE-2026-133250.svg)

## CVE-2026-133742

- [https://github.com/tryformy/CVE-2026-133742](https://github.com/tryformy/CVE-2026-133742) : ![starts](https://img.shields.io/github/stars/tryformy/CVE-2026-133742.svg) ![forks](https://img.shields.io/github/forks/tryformy/CVE-2026-133742.svg)

## CVE-2026-34990

- [https://github.com/deboravazx/cups-2.4.16-lpe](https://github.com/deboravazx/cups-2.4.16-lpe) : ![starts](https://img.shields.io/github/stars/deboravazx/cups-2.4.16-lpe.svg) ![forks](https://img.shields.io/github/forks/deboravazx/cups-2.4.16-lpe.svg)

## CVE-2026-43284
> In the Linux kernel, the following vulnerability has been resolved:

xfrm: esp: avoid in-place decrypt on shared skb frags

MSG_SPLICE_PAGES can attach pages from a pipe directly to an skb. TCP
marks such skbs with SKBFL_SHARED_FRAG after skb_splice_from_iter(),
so later paths that may modify packet data can first make a private
copy. The IPv4/IPv6 datagram append paths did not set this flag when
splicing pages into UDP skbs.

That leaves an ESP-in-UDP packet made from shared pipe pages looking


- [https://github.com/username-enzo/Fold7-Canada-TempRoot-Lock](https://github.com/username-enzo/Fold7-Canada-TempRoot-Lock) : ![starts](https://img.shields.io/github/stars/username-enzo/Fold7-Canada-TempRoot-Lock.svg) ![forks](https://img.shields.io/github/forks/username-enzo/Fold7-Canada-TempRoot-Lock.svg)

## CVE-2026-53361
> In the Linux kernel, the following vulnerability has been resolved:

af_unix: Set gc_in_progress to true in unix_gc().

Igor Ushakov reported that unix_gc() could run with gc_in_progress
being false if the work is scheduled while running:

  Thread 1         Thread 2                     Thread 3
  --------         --------                     --------
                   unix_schedule_gc()           unix_schedule_gc()
                   `- if (!gc_in_progress)      `- if (!gc_in_progress)
       

- [https://github.com/Subtle-profound/ExtractKit-53361](https://github.com/Subtle-profound/ExtractKit-53361) : ![starts](https://img.shields.io/github/stars/Subtle-profound/ExtractKit-53361.svg) ![forks](https://img.shields.io/github/forks/Subtle-profound/ExtractKit-53361.svg)

## CVE-2026-98260
> In the Linux kernel, the following vulnerability has been resolved:

exec: Cleanup POSIX timers right after de_thread()

A per-thread CPU timer holds a reference to the PID of the thread it is
attached to and, while it is armed, its node is queued in that thread&#x27;s
posix_cputimers. The task is looked up by that PID.

When a non-leader thread exec()s, de_thread() changes which task owns
that PID. pid_task(timer-&gt;it.cpu.pid, PIDTYPE_PID) then returns NULL,
but the node is still queued on tsk, which

- [https://github.com/laobinggunzhao-lab/TimerRoot-Next](https://github.com/laobinggunzhao-lab/TimerRoot-Next) : ![starts](https://img.shields.io/github/stars/laobinggunzhao-lab/TimerRoot-Next.svg) ![forks](https://img.shields.io/github/forks/laobinggunzhao-lab/TimerRoot-Next.svg)

## CVE-2026-99233
> In the Linux kernel, the following vulnerability has been resolved:

tracing/histograms: Verify event_call identity when updating synth_event refcount

In event_hist_trigger_parse() and hist_unreg_all(), the histogram
registration and unregistration paths look up find_synth_event() using
trace_event_name(file-&gt;event_call) and adjust se-&gt;ref if a match is
found.

Because find_synth_event() only compares the event basename, registering
or removing a histogram on a non-synthetic trace event whose b

- [https://github.com/gsymasd/CVE-2026-99233](https://github.com/gsymasd/CVE-2026-99233) : ![starts](https://img.shields.io/github/stars/gsymasd/CVE-2026-99233.svg) ![forks](https://img.shields.io/github/forks/gsymasd/CVE-2026-99233.svg)

## CVE-2026-99362
> In the Linux kernel, the following vulnerability has been resolved:

nfsd: preflight SEQUENCE replies before accepting a slot

nfsd4_sequence() narrows the reply buffer to the session&#x27;s cached
reply limit before it accepts the slot seqid. A client may negotiate
ca_maxresponsesize_cached down to NFSD_MIN_HDR_SEQ_SZ, and
nfsd4_alloc_slot() then gives every slot a zero-length sl_data[]. A
COMPOUND tag can fill that narrowed buffer until it holds the
SEQUENCE opcode but not the status word that foll

- [https://github.com/al00000000al/nfs2root_demo](https://github.com/al00000000al/nfs2root_demo) : ![starts](https://img.shields.io/github/stars/al00000000al/nfs2root_demo.svg) ![forks](https://img.shields.io/github/forks/al00000000al/nfs2root_demo.svg)

## CVE-2026-99489
> In the Linux kernel, the following vulnerability has been resolved:

HID: wacom: Redesign shared sibling data lifecycle

The Wacom driver coordinates state between sibling interfaces of
the same physical device using a shared structure &#x27;wacom_shared&#x27;
inside &#x27;wacom_hdev_data&#x27;.  The driver kept a volatile representative
pointer &#x27;data-&gt;dev&#x27; pointing to a sibling &#x27;hid_device&#x27; for physical
path comparisons during sibling matching.

This pointer management is fragile.  When the representative device
i

- [https://github.com/Aoki-Shinshi/CVE-2026-99489](https://github.com/Aoki-Shinshi/CVE-2026-99489) : ![starts](https://img.shields.io/github/stars/Aoki-Shinshi/CVE-2026-99489.svg) ![forks](https://img.shields.io/github/forks/Aoki-Shinshi/CVE-2026-99489.svg)
