# Update 2026-10-25
## CVE-2023-41991

- [https://github.com/lambertse/CoreTrust-bypass](https://github.com/lambertse/CoreTrust-bypass) : ![starts](https://img.shields.io/github/stars/lambertse/CoreTrust-bypass.svg) ![forks](https://img.shields.io/github/forks/lambertse/CoreTrust-bypass.svg)

## CVE-2024-10441

- [https://github.com/Ntn10/cve-2024-10441-synology-rce](https://github.com/Ntn10/cve-2024-10441-synology-rce) : ![starts](https://img.shields.io/github/stars/Ntn10/cve-2024-10441-synology-rce.svg) ![forks](https://img.shields.io/github/forks/Ntn10/cve-2024-10441-synology-rce.svg)

## CVE-2026-106072
> A flaw in Node.js TLS hostname verification allows a certificate with only a DNS SAN to authenticate an IP endpoint when the client connects using a non-canonical IPv4 spelling, such as `0177.0.0.1`, `0x7f.0.0.1`, `2130706433` or `127.1`.

`tls.checkServerIdentity()` did not classify these hosts as IP addresses, but normalized them to their canonical form and matched the result against the certificate DNS names. A certificate containing `DNS:127.0.0.1` and no `IP Address:127.0.0.1` SAN was there

- [https://github.com/CompleTetech-Security/node-cve-2026-106072-check](https://github.com/CompleTetech-Security/node-cve-2026-106072-check) : ![starts](https://img.shields.io/github/stars/CompleTetech-Security/node-cve-2026-106072-check.svg) ![forks](https://img.shields.io/github/forks/CompleTetech-Security/node-cve-2026-106072-check.svg)

## CVE-2026-109618
> PHP uses longjmp() for out-of-memory (OOM) errors to exit the current context and abort handling of the request. Some contexts may not properly account for this scenario and leave request memory in an uninitialized state before performing an allocation. The subsequent request cleanup procedure may read or branch on this memory. Multiple OOM strategies can consistently trigger this condition and lead to remote code execution (RCE).

- [https://github.com/AbacusNin/php-radar](https://github.com/AbacusNin/php-radar) : ![starts](https://img.shields.io/github/stars/AbacusNin/php-radar.svg) ![forks](https://img.shields.io/github/forks/AbacusNin/php-radar.svg)
- [https://github.com/GOLF2546/PHP2Shell-CVE-2026-109618-CVE-2026-109619](https://github.com/GOLF2546/PHP2Shell-CVE-2026-109618-CVE-2026-109619) : ![starts](https://img.shields.io/github/stars/GOLF2546/PHP2Shell-CVE-2026-109618-CVE-2026-109619.svg) ![forks](https://img.shields.io/github/forks/GOLF2546/PHP2Shell-CVE-2026-109618-CVE-2026-109619.svg)
- [https://github.com/StiJans/php8-cve-109618-109619-fix](https://github.com/StiJans/php8-cve-109618-109619-fix) : ![starts](https://img.shields.io/github/stars/StiJans/php8-cve-109618-109619-fix.svg) ![forks](https://img.shields.io/github/forks/StiJans/php8-cve-109618-109619-fix.svg)
- [https://github.com/darkLabz001/php2shell-audit](https://github.com/darkLabz001/php2shell-audit) : ![starts](https://img.shields.io/github/stars/darkLabz001/php2shell-audit.svg) ![forks](https://img.shields.io/github/forks/darkLabz001/php2shell-audit.svg)
- [https://github.com/mostofajr7-sudo/CVE-2026-109618-CVE-2026-109619-php2shell-](https://github.com/mostofajr7-sudo/CVE-2026-109618-CVE-2026-109619-php2shell-) : ![starts](https://img.shields.io/github/stars/mostofajr7-sudo/CVE-2026-109618-CVE-2026-109619-php2shell-.svg) ![forks](https://img.shields.io/github/forks/mostofajr7-sudo/CVE-2026-109618-CVE-2026-109619-php2shell-.svg)

## CVE-2026-109619
> PHP has various global state that temporarily points into request memory. In some scenarios, global state may not be correctly reset, or may be repopulated after being reset. The global state may then refer to request memory even after it has been freed. Subsequent requests may read or branch on this stale state before it is fully initialized. Multiple strategies can trigger this condition and produce remote code execution (RCE).

- [https://github.com/GOLF2546/PHP2Shell-CVE-2026-109618-CVE-2026-109619](https://github.com/GOLF2546/PHP2Shell-CVE-2026-109618-CVE-2026-109619) : ![starts](https://img.shields.io/github/stars/GOLF2546/PHP2Shell-CVE-2026-109618-CVE-2026-109619.svg) ![forks](https://img.shields.io/github/forks/GOLF2546/PHP2Shell-CVE-2026-109618-CVE-2026-109619.svg)
- [https://github.com/mostofajr7-sudo/CVE-2026-109618-CVE-2026-109619-php2shell-](https://github.com/mostofajr7-sudo/CVE-2026-109618-CVE-2026-109619-php2shell-) : ![starts](https://img.shields.io/github/stars/mostofajr7-sudo/CVE-2026-109618-CVE-2026-109619-php2shell-.svg) ![forks](https://img.shields.io/github/forks/mostofajr7-sudo/CVE-2026-109618-CVE-2026-109619-php2shell-.svg)

## CVE-2026-111497
> A buffer overflow vulnerability in the Brotli decoder (c/dec/decode.c) in Google Brotli versions 1.0.3 through 1.2.0 on all platforms allows a remote unauthenticated attacker to corrupt adjacent decoder state memory, disclose sensitive memory contents, cause a denial of service, or potentially execute arbitrary code using a crafted Brotli-compressed stream.





Users need to update any Brotli libraries or binaries between 1.0.3 through 1.2.0 to the latest available version: 1.0.10 or 1.1.1 or 1

- [https://github.com/GlobularOne/HTTP2Shell-PoC](https://github.com/GlobularOne/HTTP2Shell-PoC) : ![starts](https://img.shields.io/github/stars/GlobularOne/HTTP2Shell-PoC.svg) ![forks](https://img.shields.io/github/forks/GlobularOne/HTTP2Shell-PoC.svg)
- [https://github.com/assetnote/node2shell-scanner](https://github.com/assetnote/node2shell-scanner) : ![starts](https://img.shields.io/github/stars/assetnote/node2shell-scanner.svg) ![forks](https://img.shields.io/github/forks/assetnote/node2shell-scanner.svg)
- [https://github.com/yavuzsemih/brotli-secfix](https://github.com/yavuzsemih/brotli-secfix) : ![starts](https://img.shields.io/github/stars/yavuzsemih/brotli-secfix.svg) ![forks](https://img.shields.io/github/forks/yavuzsemih/brotli-secfix.svg)

## CVE-2026-112900
> Pillow is a Python imaging library. From 2.6.0 until 13.0.0, Pillow is vulnerable to argument injection when invoking Ghostscript for EPS input. EpsImagePlugin.Ghostscript passes a caller-controlled input filename after -f without converting it to a safe absolute path, so a name beginning with a hyphen can be interpreted as a Ghostscript option. An attacker who controls the filename can inject Ghostscript arguments. Arbitrary command execution specifically requires a leading @ argument-file file

- [https://github.com/moprius/CVE-2026-112900-Pillow-PoC](https://github.com/moprius/CVE-2026-112900-Pillow-PoC) : ![starts](https://img.shields.io/github/stars/moprius/CVE-2026-112900-Pillow-PoC.svg) ![forks](https://img.shields.io/github/forks/moprius/CVE-2026-112900-Pillow-PoC.svg)

## CVE-2026-43284
> In the Linux kernel, the following vulnerability has been resolved:

xfrm: esp: avoid in-place decrypt on shared skb frags

MSG_SPLICE_PAGES can attach pages from a pipe directly to an skb. TCP
marks such skbs with SKBFL_SHARED_FRAG after skb_splice_from_iter(),
so later paths that may modify packet data can first make a private
copy. The IPv4/IPv6 datagram append paths did not set this flag when
splicing pages into UDP skbs.

That leaves an ESP-in-UDP packet made from shared pipe pages looking


- [https://github.com/yameteeee-kudasaiiiiiii90/DFRoot](https://github.com/yameteeee-kudasaiiiiiii90/DFRoot) : ![starts](https://img.shields.io/github/stars/yameteeee-kudasaiiiiiii90/DFRoot.svg) ![forks](https://img.shields.io/github/forks/yameteeee-kudasaiiiiiii90/DFRoot.svg)

## CVE-2026-85168

- [https://github.com/Boreas37/CVE-2026-85168-PoC](https://github.com/Boreas37/CVE-2026-85168-PoC) : ![starts](https://img.shields.io/github/stars/Boreas37/CVE-2026-85168-PoC.svg) ![forks](https://img.shields.io/github/forks/Boreas37/CVE-2026-85168-PoC.svg)

## CVE-2026-85595
> Traefik versions before v2.11.55 and versions v3.0.0 through v3.7.10 contain an authentication bypass vulnerability in the digestAuth middleware where unknown usernames receive an empty secret instead of rejection. Attackers can compute a valid digest response using the empty secret and arbitrary credentials to bypass authentication on any digestAuth-protected route without a valid username or password.

- [https://github.com/Boreas37/CVE-2026-85595-PoC](https://github.com/Boreas37/CVE-2026-85595-PoC) : ![starts](https://img.shields.io/github/stars/Boreas37/CVE-2026-85595-PoC.svg) ![forks](https://img.shields.io/github/forks/Boreas37/CVE-2026-85595-PoC.svg)

## CVE-2026-86076

- [https://github.com/Boreas37/CVE-2026-86076-PoC](https://github.com/Boreas37/CVE-2026-86076-PoC) : ![starts](https://img.shields.io/github/stars/Boreas37/CVE-2026-86076-PoC.svg) ![forks](https://img.shields.io/github/forks/Boreas37/CVE-2026-86076-PoC.svg)

## CVE-2026-86426

- [https://github.com/Guila95/CVE-2026-86426](https://github.com/Guila95/CVE-2026-86426) : ![starts](https://img.shields.io/github/stars/Guila95/CVE-2026-86426.svg) ![forks](https://img.shields.io/github/forks/Guila95/CVE-2026-86426.svg)

## CVE-2026-88009

- [https://github.com/Boreas37/CVE-2026-88009-PoC](https://github.com/Boreas37/CVE-2026-88009-PoC) : ![starts](https://img.shields.io/github/stars/Boreas37/CVE-2026-88009-PoC.svg) ![forks](https://img.shields.io/github/forks/Boreas37/CVE-2026-88009-PoC.svg)

## CVE-2026-88776
> Memory overflow vulnerability vulnerability in Citrix NetScaler ADC and Citrix NetScaler Gateway.
This issue affects ADC: before 14.1-73.37, before 13.1-64.23, before 14.1-73.37 FIPS, and before 13.1.37.279 FIPS and NDcPP; Gateway: before 14.1-73.37 and before 13.1-64.23  leading to unpredictable or erroneous behavior or Denial of Service

- [https://github.com/CompleTetech-Security/netscaler-cve-2026-88776-check](https://github.com/CompleTetech-Security/netscaler-cve-2026-88776-check) : ![starts](https://img.shields.io/github/stars/CompleTetech-Security/netscaler-cve-2026-88776-check.svg) ![forks](https://img.shields.io/github/forks/CompleTetech-Security/netscaler-cve-2026-88776-check.svg)
