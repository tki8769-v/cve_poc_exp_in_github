# Update 2026-10-07
## CVE-2022-0185

- [https://github.com/secjuhl/CVE-2022-0185](https://github.com/secjuhl/CVE-2022-0185) : ![starts](https://img.shields.io/github/stars/secjuhl/CVE-2022-0185.svg) ![forks](https://img.shields.io/github/forks/secjuhl/CVE-2022-0185.svg)

## CVE-2025-21479

- [https://github.com/Shiho-Patch/linux-tools-vivo_iqoo_neo_9_root_research_on_CVE-2025-21479](https://github.com/Shiho-Patch/linux-tools-vivo_iqoo_neo_9_root_research_on_CVE-2025-21479) : ![starts](https://img.shields.io/github/stars/Shiho-Patch/linux-tools-vivo_iqoo_neo_9_root_research_on_CVE-2025-21479.svg) ![forks](https://img.shields.io/github/forks/Shiho-Patch/linux-tools-vivo_iqoo_neo_9_root_research_on_CVE-2025-21479.svg)

## CVE-2025-55182

- [https://github.com/Frizzardsecurity/CVE-2025-55182](https://github.com/Frizzardsecurity/CVE-2025-55182) : ![starts](https://img.shields.io/github/stars/Frizzardsecurity/CVE-2025-55182.svg) ![forks](https://img.shields.io/github/forks/Frizzardsecurity/CVE-2025-55182.svg)

## CVE-2026-102422
> shell-quote&#x27;s `quote()` function emits a `{ comment }` token as `#` followed by its text, which comments out the rest of the shell line, including the opening quote of any later string token. A line terminator (\n, \r, U+2028, U+2029) in that later string therefore ends the comment, and the rest of the string is parsed as shell input: `quote([&#x27;echo&#x27;, &#x27;ok&#x27;, { comment: &#x27;x&#x27; }, &#x27;a\nid;#&#x27;])` runs `id` in sh, bash, dash, ksh and zsh. `parse()` emits a comment token for a `#` in the middle of a word (f

- [https://github.com/DevVaibhav07/CVE-2026-102422](https://github.com/DevVaibhav07/CVE-2026-102422) : ![starts](https://img.shields.io/github/stars/DevVaibhav07/CVE-2026-102422.svg) ![forks](https://img.shields.io/github/forks/DevVaibhav07/CVE-2026-102422.svg)

## CVE-2026-33439

- [https://github.com/amis13/openam-clean](https://github.com/amis13/openam-clean) : ![starts](https://img.shields.io/github/stars/amis13/openam-clean.svg) ![forks](https://img.shields.io/github/forks/amis13/openam-clean.svg)

## CVE-2026-57967

- [https://github.com/c0dem4sters/CVE-2026-57967](https://github.com/c0dem4sters/CVE-2026-57967) : ![starts](https://img.shields.io/github/stars/c0dem4sters/CVE-2026-57967.svg) ![forks](https://img.shields.io/github/forks/c0dem4sters/CVE-2026-57967.svg)

## CVE-2026-59346
> VMware Workstation and Fusion contain an integer-overflow vulnerability. A malicious actor with local administrative privileges on a virtual machine with VMXNET3 virtual network adapter may exploit this issue to execute code on the host.

Affected versions:
- VMware Workstation: 25H2, 26H1 (fixed in 26H1u1)
- VMware Fusion: 25H2, 26H1 (fixed in 26H1u1)

- [https://github.com/0xCyberstan/CVE-2026-59346-POC](https://github.com/0xCyberstan/CVE-2026-59346-POC) : ![starts](https://img.shields.io/github/stars/0xCyberstan/CVE-2026-59346-POC.svg) ![forks](https://img.shields.io/github/forks/0xCyberstan/CVE-2026-59346-POC.svg)

## CVE-2026-59358
> Improper authentication (CWE-287) in the OAuth token endpoint in Cloud Foundry UAA allows a remote, authenticated attacker holding a valid user access token to obtain a fully-privileged client_credentials token for the OAuth client that issued it, by presenting the user token as an OAuth 2.0 Bearer credential on a client_credentials grant request in place of the client’s configured secret.



UAA’s client_credentials handling does not verify that the Bearer credential supplied for client authent

- [https://github.com/abraxas/CVE-2026-59358](https://github.com/abraxas/CVE-2026-59358) : ![starts](https://img.shields.io/github/stars/abraxas/CVE-2026-59358.svg) ![forks](https://img.shields.io/github/forks/abraxas/CVE-2026-59358.svg)

## CVE-2026-82531
> Smarty before 4.5.8 and 5.x before 5.8.5 contains a code injection vulnerability where the top-level nocache_hash is never restored during extends:/multi-component template inheritance, leaving it null. Attackers can supply assigned data containing a forged SmartyNocache marker that is copied verbatim into the regenerated PHP cache file, executing arbitrary PHP on include for remote code execution.

- [https://github.com/murrez/CVE-2026-82531](https://github.com/murrez/CVE-2026-82531) : ![starts](https://img.shields.io/github/stars/murrez/CVE-2026-82531.svg) ![forks](https://img.shields.io/github/forks/murrez/CVE-2026-82531.svg)
