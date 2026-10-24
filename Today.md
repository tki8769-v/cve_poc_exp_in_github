# Update 2026-10-24
## CVE-2025-32440

- [https://github.com/jstjep00/CVE-2025-32440-netalertx-auth-bypass](https://github.com/jstjep00/CVE-2025-32440-netalertx-auth-bypass) : ![starts](https://img.shields.io/github/stars/jstjep00/CVE-2025-32440-netalertx-auth-bypass.svg) ![forks](https://img.shields.io/github/forks/jstjep00/CVE-2025-32440-netalertx-auth-bypass.svg)

## CVE-2026-102255
> A Pre-authentication SSRF vulnerability exists in the SMA1000 Appliance Work Place interface due to an unintended alternate access path. By abusing this path, a remote unauthenticated attacker could potentially exploit this vulnerability to direct the appliance to issue requests on their behalf and reach internal functionality and perform unauthorized operations.

- [https://github.com/CompleteTech-LLC/sonicwall-sma1000-cve-2026-102255-check](https://github.com/CompleteTech-LLC/sonicwall-sma1000-cve-2026-102255-check) : ![starts](https://img.shields.io/github/stars/CompleteTech-LLC/sonicwall-sma1000-cve-2026-102255-check.svg) ![forks](https://img.shields.io/github/forks/CompleteTech-LLC/sonicwall-sma1000-cve-2026-102255-check.svg)

## CVE-2026-102256
> Post-authentication Improper Neutralization of Special Elements used in an OS Command (&#x27;OS Command Injection&#x27;) vulnerability has been identified in the SMA1000 appliance which in specific conditions could potentially enable a remote authenticated attacker as administrator to execute arbitrary OS commands, resulting in remote code execution.

- [https://github.com/CompleteTech-LLC/sonicwall-sma1000-cve-2026-102256-check](https://github.com/CompleteTech-LLC/sonicwall-sma1000-cve-2026-102256-check) : ![starts](https://img.shields.io/github/stars/CompleteTech-LLC/sonicwall-sma1000-cve-2026-102256-check.svg) ![forks](https://img.shields.io/github/forks/CompleteTech-LLC/sonicwall-sma1000-cve-2026-102256-check.svg)

## CVE-2026-102257
> A Zip Slip vulnerability in the in the SMA1000 Appliance Management Console (AMC) interface allows an attacker to extract files outside the intended destination directory using a specially crafted archive, resulting in remote code execution.

- [https://github.com/CompleteTech-LLC/sonicwall-sma1000-cve-2026-102257-check](https://github.com/CompleteTech-LLC/sonicwall-sma1000-cve-2026-102257-check) : ![starts](https://img.shields.io/github/stars/CompleteTech-LLC/sonicwall-sma1000-cve-2026-102257-check.svg) ![forks](https://img.shields.io/github/forks/CompleteTech-LLC/sonicwall-sma1000-cve-2026-102257-check.svg)

## CVE-2026-102258
> Post-authentication Stored Cross-Site Scripting (XSS) vulnerability has been identified in the SMA1000 Appliance Management Console (AMC) which in specific conditions could potentially enable a remote authenticated attacker as administrator to store and potentially execute arbitrary JavaScript code in the Appliance Management Console (AMC).

- [https://github.com/CompleteTech-LLC/sonicwall-sma1000-cve-2026-102258-check](https://github.com/CompleteTech-LLC/sonicwall-sma1000-cve-2026-102258-check) : ![starts](https://img.shields.io/github/stars/CompleteTech-LLC/sonicwall-sma1000-cve-2026-102258-check.svg) ![forks](https://img.shields.io/github/forks/CompleteTech-LLC/sonicwall-sma1000-cve-2026-102258-check.svg)

## CVE-2026-102764
> The vulnerability exists within internal components of BeyondTrust’s Remote Support product. The components did not adequately validate the origin of the messages it received. Under the right conditions, this could allow an attacker to perform file operations on the appliance.

- [https://github.com/CompleteTech-LLC/beyondtrust-remote-support-cve-2026-102764-check](https://github.com/CompleteTech-LLC/beyondtrust-remote-support-cve-2026-102764-check) : ![starts](https://img.shields.io/github/stars/CompleteTech-LLC/beyondtrust-remote-support-cve-2026-102764-check.svg) ![forks](https://img.shields.io/github/forks/CompleteTech-LLC/beyondtrust-remote-support-cve-2026-102764-check.svg)

## CVE-2026-102826
> simple-git, an interface for running git commands in any node.js application, enables applications to execute Git operations from JavaScript. Prior to 4.0.0, the default blockUnsafeOperationsPlugin does not completely reject configuration includes supplied through customArgs to git.clone(). The missing include.path classification permits Git to load an attacker-controlled configuration file, and the initial remediation does not cover includeIf.&lt;condition&gt;.path, allowing the same file-loading pri

- [https://github.com/CompleteTech-LLC/simplegit-rce-check](https://github.com/CompleteTech-LLC/simplegit-rce-check) : ![starts](https://img.shields.io/github/stars/CompleteTech-LLC/simplegit-rce-check.svg) ![forks](https://img.shields.io/github/forks/CompleteTech-LLC/simplegit-rce-check.svg)

## CVE-2026-104286
> An improper limitation of a pathname to a restricted directory (&#x27;path traversal&#x27;) vulnerability in Fortinet FortiMail 8.0.0 through 8.0.1, FortiMail 7.6.0 through 7.6.6, FortiMail 7.4.0 through 7.4.8, FortiMail 7.2.0 through 7.2.9 may allow an unauthenticated attacker to write arbitrary files on the underlying system via crafted HTTP or HTTPS requests.

- [https://github.com/CompleteTech-LLC/fortimail-cve-2026-104286-check](https://github.com/CompleteTech-LLC/fortimail-cve-2026-104286-check) : ![starts](https://img.shields.io/github/stars/CompleteTech-LLC/fortimail-cve-2026-104286-check.svg) ![forks](https://img.shields.io/github/forks/CompleteTech-LLC/fortimail-cve-2026-104286-check.svg)

## CVE-2026-104849
> Tinypool is a minimal Node.js worker thread pool implementation. Prior to 2.1.2, Tinypool reads filename from a caller-supplied options object in pool.run(task, options) without requiring an own property, so a polluted Object.prototype.filename can replace the intended worker module. Applications are affected only when they pass their own second-argument options object to pool.run(); calls without that argument use the trusted default options object. An attacker who can first pollute the prototy

- [https://github.com/CompleteTech-LLC/tinypool-options-rce-check](https://github.com/CompleteTech-LLC/tinypool-options-rce-check) : ![starts](https://img.shields.io/github/stars/CompleteTech-LLC/tinypool-options-rce-check.svg) ![forks](https://img.shields.io/github/forks/CompleteTech-LLC/tinypool-options-rce-check.svg)

## CVE-2026-104935
> Authentication bypass by spoofing in ICS before version 25.1.3.0 allows a remote unauthenticated attacker to execute arbitrary commands. This does not impact ICS version 22.7R2.14 or prior.

- [https://github.com/CompleteTech-LLC/ivanti-connect-secure-cve-2026-104935-check](https://github.com/CompleteTech-LLC/ivanti-connect-secure-cve-2026-104935-check) : ![starts](https://img.shields.io/github/stars/CompleteTech-LLC/ivanti-connect-secure-cve-2026-104935-check.svg) ![forks](https://img.shields.io/github/forks/CompleteTech-LLC/ivanti-connect-secure-cve-2026-104935-check.svg)

## CVE-2026-105445
> An Incorrect Privilege Assignment vulnerability in Docker Hub&#x27;s account-to-organization conversion feature allowed an authenticated attacker to reassign a personal access token (PAT) they controlled to another Docker Hub user without rotating or revoking the token secret. The unchanged PAT then authenticated to the registry as the recipient and could pull, push, or delete images, within its scopes, in repositories accessible to that user, including organization repositories.

- [https://github.com/CompleteTech-LLC/docker-hub-pat-check](https://github.com/CompleteTech-LLC/docker-hub-pat-check) : ![starts](https://img.shields.io/github/stars/CompleteTech-LLC/docker-hub-pat-check.svg) ![forks](https://img.shields.io/github/forks/CompleteTech-LLC/docker-hub-pat-check.svg)

## CVE-2026-105481
> A flaw in Node.js HTTP Agent connection reuse can cause a client to accept as valid a response that was sent before the client has sent the request. This is an incomplete fix of CVE-2026-48931.

The guard that destroys idle keep-alive sockets when unexpected data arrives only runs when the event loop polls for I/O. If an unsolicited response has already reached the socket but has not been read yet when the socket is handed to a new request, for example because the event loop was busy with synchr

- [https://github.com/CompleteTech-LLC/node-cve-2026-105481-check](https://github.com/CompleteTech-LLC/node-cve-2026-105481-check) : ![starts](https://img.shields.io/github/stars/CompleteTech-LLC/node-cve-2026-105481-check.svg) ![forks](https://img.shields.io/github/forks/CompleteTech-LLC/node-cve-2026-105481-check.svg)

## CVE-2026-105482
> A flaw in Node.js DNS resolution allows hostnames containing a NUL byte to be silently truncated by the dns.resolve*() functions and dns.reverse(). This is an incomplete fix of CVE-2026-48930, which only covered dns.lookup() and the net/tls host options.

Because the name is passed to c-ares as a C string, resolving attacker.example\0.trusted.example queries attacker.example and returns its records without any error. Applications that validate a hostname, for example against a domain allowlist

- [https://github.com/CompleteTech-LLC/node-cve-2026-105482-check](https://github.com/CompleteTech-LLC/node-cve-2026-105482-check) : ![starts](https://img.shields.io/github/stars/CompleteTech-LLC/node-cve-2026-105482-check.svg) ![forks](https://img.shields.io/github/forks/CompleteTech-LLC/node-cve-2026-105482-check.svg)

## CVE-2026-105483
> A flaw in Node.js TLS hostname verification allows a certificate without a matching IP address SAN to authenticate a connection to an IPv4 address when the host is written with non-ASCII characters, such as fullwidth digits (`１２７.0.0.1`).

`tls.checkServerIdentity()` did not recognize such hosts as IP addresses, even though they normalize and resolve to a regular IPv4 address, and matched them against the certificate DNS names and Common Name instead. A certificate containing `DNS:127.0.0.1` or 

- [https://github.com/CompleteTech-LLC/node-cve-2026-105483-check](https://github.com/CompleteTech-LLC/node-cve-2026-105483-check) : ![starts](https://img.shields.io/github/stars/CompleteTech-LLC/node-cve-2026-105483-check.svg) ![forks](https://img.shields.io/github/forks/CompleteTech-LLC/node-cve-2026-105483-check.svg)

## CVE-2026-106069
> A flaw in Node.js TLS hostname verification can cause a server certificate to be validated against a different IP address than the one the client connected to, when the host is a non-canonical IPv4 literal with a leading zero, such as `0127.0.0.1`.

`tls.checkServerIdentity()` normalizes the host following the WHATWG URL rules, which read a leading-zero octet as octal (`0127.0.0.1` becomes `87.0.0.1`), while the connection is made through the operating system resolver, which on some platforms su

- [https://github.com/CompleteTech-LLC/node-cve-2026-106069-check](https://github.com/CompleteTech-LLC/node-cve-2026-106069-check) : ![starts](https://img.shields.io/github/stars/CompleteTech-LLC/node-cve-2026-106069-check.svg) ![forks](https://img.shields.io/github/forks/CompleteTech-LLC/node-cve-2026-106069-check.svg)

## CVE-2026-106070
> A flaw in the Node.js `zlib.ZipFile` API can cause it to return bytes that do not belong to the requested entry after the local and central header validation fails.

When `zipEntry.modified` is read on an archive whose local header does not match its central directory, either directly or while compacting the archive, the validation error is caught but the parsed local header is left cached without a content offset. A later content read then returns attacker-controlled bytes from the start of the

- [https://github.com/CompleteTech-LLC/node-cve-2026-106070-check](https://github.com/CompleteTech-LLC/node-cve-2026-106070-check) : ![starts](https://img.shields.io/github/stars/CompleteTech-LLC/node-cve-2026-106070-check.svg) ![forks](https://img.shields.io/github/forks/CompleteTech-LLC/node-cve-2026-106070-check.svg)

## CVE-2026-106071
> A flaw in Node.js Permission Model filesystem enforcement can grant access to paths that do not match a wildcard `--allow-fs-read` or `--allow-fs-write` rule.

When the requested path is shorter than the prefix of a wildcard grant, the radix tree lookup stops comparing early and treats the path as a match. For example, `--allow-fs-read=/etc/passwd.*` also allows reading `/etc/passwd`. This requires the wildcard grant to sit directly under the root of the permission tree, for example when it is t

- [https://github.com/CompleteTech-LLC/node-cve-2026-106071-check](https://github.com/CompleteTech-LLC/node-cve-2026-106071-check) : ![starts](https://img.shields.io/github/stars/CompleteTech-LLC/node-cve-2026-106071-check.svg) ![forks](https://img.shields.io/github/forks/CompleteTech-LLC/node-cve-2026-106071-check.svg)

## CVE-2026-106072
> A flaw in Node.js TLS hostname verification allows a certificate with only a DNS SAN to authenticate an IP endpoint when the client connects using a non-canonical IPv4 spelling, such as `0177.0.0.1`, `0x7f.0.0.1`, `2130706433` or `127.1`.

`tls.checkServerIdentity()` did not classify these hosts as IP addresses, but normalized them to their canonical form and matched the result against the certificate DNS names. A certificate containing `DNS:127.0.0.1` and no `IP Address:127.0.0.1` SAN was there

- [https://github.com/CompleteTech-LLC/node-cve-2026-106072-check](https://github.com/CompleteTech-LLC/node-cve-2026-106072-check) : ![starts](https://img.shields.io/github/stars/CompleteTech-LLC/node-cve-2026-106072-check.svg) ![forks](https://img.shields.io/github/forks/CompleteTech-LLC/node-cve-2026-106072-check.svg)

## CVE-2026-106073
> A flaw in Node.js Permission Model filesystem enforcement leaves `fs.realpathSync()` without the required read permission checks. This is an incomplete fix of CVE-2026-21715, which only covered `fs.realpathSync.native()`.

As a result, code running under `--permission` with restricted `--allow-fs-read` can still use `fs.realpathSync()` to check file existence, resolve symlink targets, and enumerate filesystem paths outside of permitted directories.

This vulnerability affects Node.js **26.x**, *

- [https://github.com/CompleteTech-LLC/node-cve-2026-106073-check](https://github.com/CompleteTech-LLC/node-cve-2026-106073-check) : ![starts](https://img.shields.io/github/stars/CompleteTech-LLC/node-cve-2026-106073-check.svg) ![forks](https://img.shields.io/github/forks/CompleteTech-LLC/node-cve-2026-106073-check.svg)

## CVE-2026-106074
> A flaw in Node.js `crypto` causes the internal entropy caches used by `crypto.randomUUID()`, `crypto.randomUUIDv7()`, and `crypto.randomInt()` to be saved into user-land startup snapshots (`--build-snapshot`) and single executable applications built with `useSnapshot`.

If any of these functions, or an API that relies on them such as `URL.createObjectURL()`, is called while the snapshot is built, every process started from that snapshot returns the same values until the cache is refilled: up to 

- [https://github.com/CompleteTech-LLC/node-cve-2026-106074-check](https://github.com/CompleteTech-LLC/node-cve-2026-106074-check) : ![starts](https://img.shields.io/github/stars/CompleteTech-LLC/node-cve-2026-106074-check.svg) ![forks](https://img.shields.io/github/forks/CompleteTech-LLC/node-cve-2026-106074-check.svg)

## CVE-2026-109618
> PHP uses longjmp() for out-of-memory (OOM) errors to exit the current context and abort handling of the request. Some contexts may not properly account for this scenario and leave request memory in an uninitialized state before performing an allocation. The subsequent request cleanup procedure may read or branch on this memory. Multiple OOM strategies can consistently trigger this condition and lead to remote code execution (RCE).

- [https://github.com/pagvac/php2shell-detect](https://github.com/pagvac/php2shell-detect) : ![starts](https://img.shields.io/github/stars/pagvac/php2shell-detect.svg) ![forks](https://img.shields.io/github/forks/pagvac/php2shell-detect.svg)
- [https://github.com/pagvac/php2shell-trends](https://github.com/pagvac/php2shell-trends) : ![starts](https://img.shields.io/github/stars/pagvac/php2shell-trends.svg) ![forks](https://img.shields.io/github/forks/pagvac/php2shell-trends.svg)
- [https://github.com/segfaultx01/php2shell-pocJavali](https://github.com/segfaultx01/php2shell-pocJavali) : ![starts](https://img.shields.io/github/stars/segfaultx01/php2shell-pocJavali.svg) ![forks](https://img.shields.io/github/forks/segfaultx01/php2shell-pocJavali.svg)

## CVE-2026-111497
> A buffer overflow vulnerability in the Brotli decoder (c/dec/decode.c) in Google Brotli versions 1.0.3 through 1.2.0 on all platforms allows a remote unauthenticated attacker to corrupt adjacent decoder state memory, disclose sensitive memory contents, cause a denial of service, or potentially execute arbitrary code using a crafted Brotli-compressed stream.





Users need to update any Brotli libraries or binaries between 1.0.3 through 1.2.0 to the latest available version: 1.0.10 or 1.1.1 or 1

- [https://github.com/Ghost-Bx1/Node2Shell-CVE-2026-111497](https://github.com/Ghost-Bx1/Node2Shell-CVE-2026-111497) : ![starts](https://img.shields.io/github/stars/Ghost-Bx1/Node2Shell-CVE-2026-111497.svg) ![forks](https://img.shields.io/github/forks/Ghost-Bx1/Node2Shell-CVE-2026-111497.svg)
- [https://github.com/fuzheado/n2s-buildpack-probe](https://github.com/fuzheado/n2s-buildpack-probe) : ![starts](https://img.shields.io/github/stars/fuzheado/n2s-buildpack-probe.svg) ![forks](https://img.shields.io/github/forks/fuzheado/n2s-buildpack-probe.svg)
- [https://github.com/trailofbits/brotli-checker](https://github.com/trailofbits/brotli-checker) : ![starts](https://img.shields.io/github/stars/trailofbits/brotli-checker.svg) ![forks](https://img.shields.io/github/forks/trailofbits/brotli-checker.svg)

## CVE-2026-112398
> Pillow is a Python imaging library. Prior to 13.0.0, Pillow&#x27;s FlashPix JPEG-tile decoder can write decoded scanlines beyond the allocated tile buffer. FlashPix (FPX) JPEG decoding selects raw mode LA with two bytes per pixel, while an unrecognized JPEG mode can be decoded as JCS_UNKNOWN with four components, causing ImagingJpegDecode to write four-component scanlines into the two-byte tile buffer. An attacker can supply a crafted OLE2 FlashPix file to an application with the optional olefile dep

- [https://github.com/mcpmark-eval-liuhezi/security-advisory-research](https://github.com/mcpmark-eval-liuhezi/security-advisory-research) : ![starts](https://img.shields.io/github/stars/mcpmark-eval-liuhezi/security-advisory-research.svg) ![forks](https://img.shields.io/github/forks/mcpmark-eval-liuhezi/security-advisory-research.svg)

## CVE-2026-115560

- [https://github.com/ivst/CVE-2026-115560](https://github.com/ivst/CVE-2026-115560) : ![starts](https://img.shields.io/github/stars/ivst/CVE-2026-115560.svg) ![forks](https://img.shields.io/github/forks/ivst/CVE-2026-115560.svg)

## CVE-2026-17106

- [https://github.com/CompleteTech-LLC/copyescape-check](https://github.com/CompleteTech-LLC/copyescape-check) : ![starts](https://img.shields.io/github/stars/CompleteTech-LLC/copyescape-check.svg) ![forks](https://img.shields.io/github/forks/CompleteTech-LLC/copyescape-check.svg)

## CVE-2026-19489

- [https://github.com/CompleteTech-LLC/netscaler-cve-2026-19489-check](https://github.com/CompleteTech-LLC/netscaler-cve-2026-19489-check) : ![starts](https://img.shields.io/github/stars/CompleteTech-LLC/netscaler-cve-2026-19489-check.svg) ![forks](https://img.shields.io/github/forks/CompleteTech-LLC/netscaler-cve-2026-19489-check.svg)

## CVE-2026-19490
> Vulnerability in NetScaler ADC and NetScaler Gateway.

This issue affects ADC: from 14.1 through 73.32 and from 13.1 through 63.21; Gateway: from 14.1 through 73.32 and from 13.1 through 63.21.

- [https://github.com/CompleteTech-LLC/netscaler-cve-2026-19490-check](https://github.com/CompleteTech-LLC/netscaler-cve-2026-19490-check) : ![starts](https://img.shields.io/github/stars/CompleteTech-LLC/netscaler-cve-2026-19490-check.svg) ![forks](https://img.shields.io/github/forks/CompleteTech-LLC/netscaler-cve-2026-19490-check.svg)

## CVE-2026-21589
> This is a vulnerability in Bitbucket Data Center, Confluence Data Center, Jira Service Management Data Center, Jira Software Data Center, Bamboo Data Center. Crowd Data Center, Crucible and Fisheye. This Arbitrary File Access vulnerability allows an unauthenticated attacker to access specific files within the web application root directory in affected versions. Exploitation requires prior knowledge of the target file&#x27;s exact name and path; this vulnerability does not allow attackers to enumerate

- [https://github.com/CompleteTech-LLC/atlassian-cve-2026-21589-check](https://github.com/CompleteTech-LLC/atlassian-cve-2026-21589-check) : ![starts](https://img.shields.io/github/stars/CompleteTech-LLC/atlassian-cve-2026-21589-check.svg) ![forks](https://img.shields.io/github/forks/CompleteTech-LLC/atlassian-cve-2026-21589-check.svg)

## CVE-2026-54668
> Kitodo.Production is a workflow management tool for mass digitization and is part of the Kitodo Digital Library Suite. Prior to version 3.9.2, org.kitodo.production.helper.XMLUtils exposes several XML parsing helpers that construct a JAXP parser with the default, non-secure configuration. The methods parseXMLString(String), getNumberOfEADElements(String, String) and checkIfXmlIsWellFormed(String) build a DocumentBuilderFactory / XMLInputFactory / SAXParserFactory via newInstance() and parse the 

- [https://github.com/KernelEditor/CVE-2026-54668](https://github.com/KernelEditor/CVE-2026-54668) : ![starts](https://img.shields.io/github/stars/KernelEditor/CVE-2026-54668.svg) ![forks](https://img.shields.io/github/forks/KernelEditor/CVE-2026-54668.svg)

## CVE-2026-56846

- [https://github.com/CompleteTech-LLC/node-cve-2026-56846-check](https://github.com/CompleteTech-LLC/node-cve-2026-56846-check) : ![starts](https://img.shields.io/github/stars/CompleteTech-LLC/node-cve-2026-56846-check.svg) ![forks](https://img.shields.io/github/forks/CompleteTech-LLC/node-cve-2026-56846-check.svg)

## CVE-2026-56847

- [https://github.com/CompleteTech-LLC/node-cve-2026-56847-check](https://github.com/CompleteTech-LLC/node-cve-2026-56847-check) : ![starts](https://img.shields.io/github/stars/CompleteTech-LLC/node-cve-2026-56847-check.svg) ![forks](https://img.shields.io/github/forks/CompleteTech-LLC/node-cve-2026-56847-check.svg)

## CVE-2026-56848

- [https://github.com/CompleteTech-LLC/node-cve-2026-56848-check](https://github.com/CompleteTech-LLC/node-cve-2026-56848-check) : ![starts](https://img.shields.io/github/stars/CompleteTech-LLC/node-cve-2026-56848-check.svg) ![forks](https://img.shields.io/github/forks/CompleteTech-LLC/node-cve-2026-56848-check.svg)

## CVE-2026-56850

- [https://github.com/CompleteTech-LLC/node-cve-2026-56850-check](https://github.com/CompleteTech-LLC/node-cve-2026-56850-check) : ![starts](https://img.shields.io/github/stars/CompleteTech-LLC/node-cve-2026-56850-check.svg) ![forks](https://img.shields.io/github/forks/CompleteTech-LLC/node-cve-2026-56850-check.svg)

## CVE-2026-58039

- [https://github.com/CompleteTech-LLC/node-cve-2026-58039-check](https://github.com/CompleteTech-LLC/node-cve-2026-58039-check) : ![starts](https://img.shields.io/github/stars/CompleteTech-LLC/node-cve-2026-58039-check.svg) ![forks](https://img.shields.io/github/forks/CompleteTech-LLC/node-cve-2026-58039-check.svg)

## CVE-2026-58040

- [https://github.com/CompleteTech-LLC/node-cve-2026-58040-check](https://github.com/CompleteTech-LLC/node-cve-2026-58040-check) : ![starts](https://img.shields.io/github/stars/CompleteTech-LLC/node-cve-2026-58040-check.svg) ![forks](https://img.shields.io/github/forks/CompleteTech-LLC/node-cve-2026-58040-check.svg)

## CVE-2026-58041

- [https://github.com/CompleteTech-LLC/node-cve-2026-58041-check](https://github.com/CompleteTech-LLC/node-cve-2026-58041-check) : ![starts](https://img.shields.io/github/stars/CompleteTech-LLC/node-cve-2026-58041-check.svg) ![forks](https://img.shields.io/github/forks/CompleteTech-LLC/node-cve-2026-58041-check.svg)

## CVE-2026-58042

- [https://github.com/CompleteTech-LLC/node-cve-2026-58042-check](https://github.com/CompleteTech-LLC/node-cve-2026-58042-check) : ![starts](https://img.shields.io/github/stars/CompleteTech-LLC/node-cve-2026-58042-check.svg) ![forks](https://img.shields.io/github/forks/CompleteTech-LLC/node-cve-2026-58042-check.svg)

## CVE-2026-58043

- [https://github.com/CompleteTech-LLC/node-cve-2026-58043-check](https://github.com/CompleteTech-LLC/node-cve-2026-58043-check) : ![starts](https://img.shields.io/github/stars/CompleteTech-LLC/node-cve-2026-58043-check.svg) ![forks](https://img.shields.io/github/forks/CompleteTech-LLC/node-cve-2026-58043-check.svg)

## CVE-2026-58044

- [https://github.com/CompleteTech-LLC/node-cve-2026-58044-check](https://github.com/CompleteTech-LLC/node-cve-2026-58044-check) : ![starts](https://img.shields.io/github/stars/CompleteTech-LLC/node-cve-2026-58044-check.svg) ![forks](https://img.shields.io/github/forks/CompleteTech-LLC/node-cve-2026-58044-check.svg)

## CVE-2026-58045

- [https://github.com/CompleteTech-LLC/node-cve-2026-58045-check](https://github.com/CompleteTech-LLC/node-cve-2026-58045-check) : ![starts](https://img.shields.io/github/stars/CompleteTech-LLC/node-cve-2026-58045-check.svg) ![forks](https://img.shields.io/github/forks/CompleteTech-LLC/node-cve-2026-58045-check.svg)

## CVE-2026-68136
> In the Linux kernel, the following vulnerability has been resolved:

net: gro: fix double aggregation of flush-marked skbs

Commit 0ab03f353d36 (&quot;net-gro: Fix GRO flush when receiving a GSO
packet.&quot;) added a flush check to skb_gro_receive(), but
skb_gro_receive_list() lacks the same validation.

As a result, packets marked with NAPI_GRO_CB(skb)-&gt;flush may still be
re-aggregated.

This allows already-GRO&#x27;d packets with existing frag_list to be
re-aggregated into a new GRO session, corrupting the 

- [https://github.com/KernelEditor/CVE-2026-68136](https://github.com/KernelEditor/CVE-2026-68136) : ![starts](https://img.shields.io/github/stars/KernelEditor/CVE-2026-68136.svg) ![forks](https://img.shields.io/github/forks/KernelEditor/CVE-2026-68136.svg)

## CVE-2026-69254

- [https://github.com/CompleteTech-LLC/flowise-cve-2026-69254-check](https://github.com/CompleteTech-LLC/flowise-cve-2026-69254-check) : ![starts](https://img.shields.io/github/stars/CompleteTech-LLC/flowise-cve-2026-69254-check.svg) ![forks](https://img.shields.io/github/forks/CompleteTech-LLC/flowise-cve-2026-69254-check.svg)

## CVE-2026-88773
> Inconsistent interpretation of HTTP requests (&#x27;HTTP Request/Response smuggling&#x27;) vulnerability in Citrix NetScaler ADC and Citrix NetScaler Gateway.

This issue affects ADC: before 14.1-73.37, before 13.1-64.23, before 14.1-73.37 FIPS, and before 13.1-37.279 and NDcPP; Gateway: before 14.1-73.37 FIPS and before 13.1-64.23.

- [https://github.com/CompleteTech-LLC/netscaler-cve-2026-88773-check](https://github.com/CompleteTech-LLC/netscaler-cve-2026-88773-check) : ![starts](https://img.shields.io/github/stars/CompleteTech-LLC/netscaler-cve-2026-88773-check.svg) ![forks](https://img.shields.io/github/forks/CompleteTech-LLC/netscaler-cve-2026-88773-check.svg)

## CVE-2026-88774
> Vulnerability in Citrix NetScaler ADC and Citrix NetScaler Gateway.

This issue affects ADC: before 14.1-73.37, before 13.1-64.23, before 14.1-73.37 FIPS, and before 13.1.37.279 FIPS and NDcPP; Gateway: before 14.1-73.37 and before 13.1-64.23 leading to a feature policy bypass due to improper HTTP URL based expression usage.

- [https://github.com/CompleteTech-LLC/netscaler-cve-2026-88774-check](https://github.com/CompleteTech-LLC/netscaler-cve-2026-88774-check) : ![starts](https://img.shields.io/github/stars/CompleteTech-LLC/netscaler-cve-2026-88774-check.svg) ![forks](https://img.shields.io/github/forks/CompleteTech-LLC/netscaler-cve-2026-88774-check.svg)

## CVE-2026-88775
> Memory overflow vulnerability in Citrix NetScaler ADC and Citrix NetScaler Gateway.

This issue affects ADC: before 14.1-73.37, before 13.1-64.23, before 14.1-73.37 FIPS, and before 13.1.37.279 FIPS and NDcPP; Gateway: before 14.1-73.37 and before 13.1-64.23 leading Memory overflow vulnerability leading to unpredictable or erroneous behavior or Denial of Service

- [https://github.com/CompleteTech-LLC/netscaler-cve-2026-88775-check](https://github.com/CompleteTech-LLC/netscaler-cve-2026-88775-check) : ![starts](https://img.shields.io/github/stars/CompleteTech-LLC/netscaler-cve-2026-88775-check.svg) ![forks](https://img.shields.io/github/forks/CompleteTech-LLC/netscaler-cve-2026-88775-check.svg)

## CVE-2026-88776
> Memory overflow vulnerability vulnerability in Citrix NetScaler ADC and Citrix NetScaler Gateway.
This issue affects ADC: before 14.1-73.37, before 13.1-64.23, before 14.1-73.37 FIPS, and before 13.1.37.279 FIPS and NDcPP; Gateway: before 14.1-73.37 and before 13.1-64.23  leading to unpredictable or erroneous behavior or Denial of Service

- [https://github.com/CompleteTech-LLC/netscaler-cve-2026-88776-check](https://github.com/CompleteTech-LLC/netscaler-cve-2026-88776-check) : ![starts](https://img.shields.io/github/stars/CompleteTech-LLC/netscaler-cve-2026-88776-check.svg) ![forks](https://img.shields.io/github/forks/CompleteTech-LLC/netscaler-cve-2026-88776-check.svg)

## CVE-2026-88777
> Memory overflow vulnerability vulnerability in Citrix NetScaler ADC and Citrix NetScaler Gateway.

This issue affects ADC: before 14.1-73.37, before 13.1-64.23, before 14.1-73.37 FIPS, and before 13.1.37.279 FIPS and NDcPP; Gateway: before 14.1-73.37 and before 13.1-64.23  leading to unpredictable or erroneous behavior or Denial of Service

- [https://github.com/CompleteTech-LLC/netscaler-cve-2026-88777-check](https://github.com/CompleteTech-LLC/netscaler-cve-2026-88777-check) : ![starts](https://img.shields.io/github/stars/CompleteTech-LLC/netscaler-cve-2026-88777-check.svg) ![forks](https://img.shields.io/github/forks/CompleteTech-LLC/netscaler-cve-2026-88777-check.svg)

## CVE-2026-88778
> Predictable exact value from previous values vulnerability in Citrix NetScaler ADC and Citrix NetScaler Gateway.

This issue affects ADC: before 14.1-73.37, before 13.1-64.23, before 14.1-73.37 FIPS, and before 13.1.37.279 FIPS and NDcPP; Gateway: before 14.1-73.37 and before 13.1-64.23.

- [https://github.com/CompleteTech-LLC/netscaler-cve-2026-88778-check](https://github.com/CompleteTech-LLC/netscaler-cve-2026-88778-check) : ![starts](https://img.shields.io/github/stars/CompleteTech-LLC/netscaler-cve-2026-88778-check.svg) ![forks](https://img.shields.io/github/forks/CompleteTech-LLC/netscaler-cve-2026-88778-check.svg)

## CVE-2026-92162
> Flatpak is a system for building, distributing, and running sandboxed desktop applications on Linux. Prior to version 1.18.1, on systems where at least one OCI remote is configured (most common on Fedora systems), a malicious local user in an active local session could use a crafted architecture name to trick the `flatpak-system-helper` process into creating a root-owned directory tree with contents determined by the OCI remote, plus a root-owned `lock` file and `icons` directory, outside the in

- [https://github.com/0xSemizzz/CVE-2026-92162](https://github.com/0xSemizzz/CVE-2026-92162) : ![starts](https://img.shields.io/github/stars/0xSemizzz/CVE-2026-92162.svg) ![forks](https://img.shields.io/github/forks/0xSemizzz/CVE-2026-92162.svg)

## CVE-2026-92935

- [https://github.com/CompleteTech-LLC/vm2-nesting-check](https://github.com/CompleteTech-LLC/vm2-nesting-check) : ![starts](https://img.shields.io/github/stars/CompleteTech-LLC/vm2-nesting-check.svg) ![forks](https://img.shields.io/github/forks/CompleteTech-LLC/vm2-nesting-check.svg)

## CVE-2026-94293
> An unauthenticated remote attacker can modify Asset Administration Shell submodel data via PATCH requests and can read all data exposed by the GET endpoints.

- [https://github.com/KernelEditor/CVE-2026-94293](https://github.com/KernelEditor/CVE-2026-94293) : ![starts](https://img.shields.io/github/stars/KernelEditor/CVE-2026-94293.svg) ![forks](https://img.shields.io/github/forks/KernelEditor/CVE-2026-94293.svg)

## CVE-2026-96889
> A flaw was found in librsvg. When processing an SVG document containing nested XML inclusions (Xincludes) with duplicate entity declarations, a use-after-free error can occur. This vulnerability arises because the library incorrectly frees an XML entity that is still in use by the parser. An attacker could potentially exploit this to cause a denial of service or execute arbitrary code.

- [https://github.com/CompleteTech-LLC/sharp-rsvg-rce-check](https://github.com/CompleteTech-LLC/sharp-rsvg-rce-check) : ![starts](https://img.shields.io/github/stars/CompleteTech-LLC/sharp-rsvg-rce-check.svg) ![forks](https://img.shields.io/github/forks/CompleteTech-LLC/sharp-rsvg-rce-check.svg)
