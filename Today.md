# Update 2026-11-27
## CVE-2021-44228

- [https://github.com/johnyProDev/CVE-2021-44228-Essay](https://github.com/johnyProDev/CVE-2021-44228-Essay) : ![starts](https://img.shields.io/github/stars/johnyProDev/CVE-2021-44228-Essay.svg) ![forks](https://img.shields.io/github/forks/johnyProDev/CVE-2021-44228-Essay.svg)

## CVE-2025-10184

- [https://github.com/LimLLL/coloros-sms-guard](https://github.com/LimLLL/coloros-sms-guard) : ![starts](https://img.shields.io/github/stars/LimLLL/coloros-sms-guard.svg) ![forks](https://img.shields.io/github/forks/LimLLL/coloros-sms-guard.svg)

## CVE-2025-3248
> Langflow versions prior to 1.3.0 are susceptible to code injection in 
the /api/v1/validate/code endpoint. A remote and unauthenticated attacker can send crafted HTTP requests to execute arbitrary
code.

- [https://github.com/Yasinnozbek/langflow-cve-2025-3248-detector](https://github.com/Yasinnozbek/langflow-cve-2025-3248-detector) : ![starts](https://img.shields.io/github/stars/Yasinnozbek/langflow-cve-2025-3248-detector.svg) ![forks](https://img.shields.io/github/forks/Yasinnozbek/langflow-cve-2025-3248-detector.svg)

## CVE-2026-0087

- [https://github.com/helloguy1234/CVE-2026-0087_PoC](https://github.com/helloguy1234/CVE-2026-0087_PoC) : ![starts](https://img.shields.io/github/stars/helloguy1234/CVE-2026-0087_PoC.svg) ![forks](https://img.shields.io/github/forks/helloguy1234/CVE-2026-0087_PoC.svg)

## CVE-2026-111497
> A buffer overflow vulnerability in the Brotli decoder (c/dec/decode.c) in Google Brotli versions 1.0.3 through 1.2.0 on all platforms allows a remote unauthenticated attacker to corrupt adjacent decoder state memory, disclose sensitive memory contents, cause a denial of service, or potentially execute arbitrary code using a crafted Brotli-compressed stream.





Users need to update any Brotli libraries or binaries between 1.0.3 through 1.2.0 to the latest available version: 1.0.10 or 1.1.1 or 1

- [https://github.com/jianghang8421/fix-cve-2026-111497](https://github.com/jianghang8421/fix-cve-2026-111497) : ![starts](https://img.shields.io/github/stars/jianghang8421/fix-cve-2026-111497.svg) ![forks](https://img.shields.io/github/forks/jianghang8421/fix-cve-2026-111497.svg)

## CVE-2026-112477
> A race condition was addressed with improved locking. This issue is fixed in iOS 26.7.2 and iPadOS 26.7.2, iOS 27.2 and iPadOS 27.2, macOS Golden Gate 27.2, macOS Sequoia 15.8.2, macOS Tahoe 26.7.2, tvOS 27.2, visionOS 27.2, watchOS 27.2. An app may be able to cause unexpected system termination or corrupt kernel memory.

- [https://github.com/lixue1228321-cmyk/iOS-Exploitation](https://github.com/lixue1228321-cmyk/iOS-Exploitation) : ![starts](https://img.shields.io/github/stars/lixue1228321-cmyk/iOS-Exploitation.svg) ![forks](https://img.shields.io/github/forks/lixue1228321-cmyk/iOS-Exploitation.svg)

## CVE-2026-125180
> FFmpeg 8.1 through 9.0.2 contains a memory exhaustion vulnerability in the libavcodec/exif.c parser that allows attackers to amplify allocations by pointing many IFD entries at overlapping payloads. Attackers can embed a small crafted EXIF block in TIFF, JPEG, PNG or WebP images to trigger quadratic memory allocation, causing denial of service in decoding applications.

- [https://github.com/XChen446/CVE-2026-125180-demo](https://github.com/XChen446/CVE-2026-125180-demo) : ![starts](https://img.shields.io/github/stars/XChen446/CVE-2026-125180-demo.svg) ![forks](https://img.shields.io/github/forks/XChen446/CVE-2026-125180-demo.svg)

## CVE-2026-32475

- [https://github.com/tenderacer-lgtm/cve-32475-lab](https://github.com/tenderacer-lgtm/cve-32475-lab) : ![starts](https://img.shields.io/github/stars/tenderacer-lgtm/cve-32475-lab.svg) ![forks](https://img.shields.io/github/forks/tenderacer-lgtm/cve-32475-lab.svg)

## CVE-2026-39808

- [https://github.com/joel-correa/Fortinet-Exploits-CVE-2026-39808-106173-107656](https://github.com/joel-correa/Fortinet-Exploits-CVE-2026-39808-106173-107656) : ![starts](https://img.shields.io/github/stars/joel-correa/Fortinet-Exploits-CVE-2026-39808-106173-107656.svg) ![forks](https://img.shields.io/github/forks/joel-correa/Fortinet-Exploits-CVE-2026-39808-106173-107656.svg)

## CVE-2026-61725
> sevenz-rust2 is a Rust-native 7z compressor and `decompress`or. Prior to 0.21.1, extracting an attacker-supplied 7z archive can write or overwrite files outside the destination directory. In `src/util/decompress.rs`, `decompress_impl` computes each destination with `dest.join(entry.name())` without normalizing the archive&#x27;s UTF-16 entry name or verifying containment, and `default_entry_extract_fn` writes to it with `File::create`. Parent-directory components escape the extraction root, and an ab

- [https://github.com/pluto-chou/CVE-2026-61725_sevenz-rust2](https://github.com/pluto-chou/CVE-2026-61725_sevenz-rust2) : ![starts](https://img.shields.io/github/stars/pluto-chou/CVE-2026-61725_sevenz-rust2.svg) ![forks](https://img.shields.io/github/forks/pluto-chou/CVE-2026-61725_sevenz-rust2.svg)

## CVE-2026-93479
> A vulnerability exists in NGINX Plus and NGINX Open Source when a map directive uses regex matching and the root directive or access log format references the map&#x27;s regex capture variables before referencing the map output variable. Alternatively, the same result could be achieved by using a non-cacheable variable in a string expression under certain conditions. An unauthenticated attacker along with conditions beyond their control can exploit this vulnerability by sending crafted HTTP requests.

- [https://github.com/googlesky/CVE-2026-93479](https://github.com/googlesky/CVE-2026-93479) : ![starts](https://img.shields.io/github/stars/googlesky/CVE-2026-93479.svg) ![forks](https://img.shields.io/github/forks/googlesky/CVE-2026-93479.svg)

## CVE-2026-99163
> In the Linux kernel, the following vulnerability has been resolved:

tracing/histograms: Reject non-stacktrace fields for synthetic stacktrace fields

In check_synth_field(), when a synthetic event field is a stacktrace
(field-&gt;is_stack) and the histogram field is not a &quot;long[&quot; stacktrace
array, validation falls through to the generic size and signedness
comparison.

Because parse_synth_field() sets a stacktrace field&#x27;s type to
&quot;__data_loc unsigned long[]&quot;, its size is sizeof(u64) and
synth_fiel

- [https://github.com/Aoki-Shinshi/CVE-2026-99163](https://github.com/Aoki-Shinshi/CVE-2026-99163) : ![starts](https://img.shields.io/github/stars/Aoki-Shinshi/CVE-2026-99163.svg) ![forks](https://img.shields.io/github/forks/Aoki-Shinshi/CVE-2026-99163.svg)

## CVE-2026-99362
> In the Linux kernel, the following vulnerability has been resolved:

nfsd: preflight SEQUENCE replies before accepting a slot

nfsd4_sequence() narrows the reply buffer to the session&#x27;s cached
reply limit before it accepts the slot seqid. A client may negotiate
ca_maxresponsesize_cached down to NFSD_MIN_HDR_SEQ_SZ, and
nfsd4_alloc_slot() then gives every slot a zero-length sl_data[]. A
COMPOUND tag can fill that narrowed buffer until it holds the
SEQUENCE opcode but not the status word that foll

- [https://github.com/suominen/CVE-2026-99362](https://github.com/suominen/CVE-2026-99362) : ![starts](https://img.shields.io/github/stars/suominen/CVE-2026-99362.svg) ![forks](https://img.shields.io/github/forks/suominen/CVE-2026-99362.svg)
