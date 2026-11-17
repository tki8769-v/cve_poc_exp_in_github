# Update 2026-11-17
## CVE-2021-41773

- [https://github.com/itsDav804/CVE-2021-41773](https://github.com/itsDav804/CVE-2021-41773) : ![starts](https://img.shields.io/github/stars/itsDav804/CVE-2021-41773.svg) ![forks](https://img.shields.io/github/forks/itsDav804/CVE-2021-41773.svg)

## CVE-2023-22515

- [https://github.com/oshaie2/CVE-2023-22515-Incident-Response](https://github.com/oshaie2/CVE-2023-22515-Incident-Response) : ![starts](https://img.shields.io/github/stars/oshaie2/CVE-2023-22515-Incident-Response.svg) ![forks](https://img.shields.io/github/forks/oshaie2/CVE-2023-22515-Incident-Response.svg)

## CVE-2026-112181
> Vulnerability due to inadequate restriction of references to external XML entities in OpenKM Community Edition. The XML processing in FormUtils / LocalEntityResolver does not properly restrict the resolution of external resources. An authenticated remote attacker with the ROLE_USER role can exploit the flaw via a REST request. In the 6.3.x branch, this allows the attacker to trigger HTTP requests under their control (SSRF); in 7.0.3, it allows the attacker to read local files and access internal

- [https://github.com/Lasersinho/cve-2026-112181-cve-2026-112182-openkm-ce](https://github.com/Lasersinho/cve-2026-112181-cve-2026-112182-openkm-ce) : ![starts](https://img.shields.io/github/stars/Lasersinho/cve-2026-112181-cve-2026-112182-openkm-ce.svg) ![forks](https://img.shields.io/github/forks/Lasersinho/cve-2026-112181-cve-2026-112182-openkm-ce.svg)

## CVE-2026-112182
> Unauthorization vulnerability in the management of workflow definitions in OpenKM Community Edition. The REST endpoints `registerProcessDefinition` and `runProcessDefinition` require authentication but do not verify roles in the WorkflowService or in lower layers. An attacker with the `ROLE_USER` role can register and execute a process definition containing BeanShell scripts, allowing them to execute Java code and operating system commands with the service’s privileges. In the official Docker im

- [https://github.com/Lasersinho/cve-2026-112181-cve-2026-112182-openkm-ce](https://github.com/Lasersinho/cve-2026-112181-cve-2026-112182-openkm-ce) : ![starts](https://img.shields.io/github/stars/Lasersinho/cve-2026-112181-cve-2026-112182-openkm-ce.svg) ![forks](https://img.shields.io/github/forks/Lasersinho/cve-2026-112181-cve-2026-112182-openkm-ce.svg)

## CVE-2026-3650

- [https://github.com/Summitvc/cve-2026-3650](https://github.com/Summitvc/cve-2026-3650) : ![starts](https://img.shields.io/github/stars/Summitvc/cve-2026-3650.svg) ![forks](https://img.shields.io/github/forks/Summitvc/cve-2026-3650.svg)

## CVE-2026-59309

- [https://github.com/JHenryArcaneCipher/CVE-2026-59309-PoC](https://github.com/JHenryArcaneCipher/CVE-2026-59309-PoC) : ![starts](https://img.shields.io/github/stars/JHenryArcaneCipher/CVE-2026-59309-PoC.svg) ![forks](https://img.shields.io/github/forks/JHenryArcaneCipher/CVE-2026-59309-PoC.svg)

## CVE-2026-78287
> Improper Control of Generation of Code (&#x27;Code Injection&#x27;) vulnerability in Staggs STAGGS staggs allows Remote Code Inclusion.This issue affects STAGGS: from n/a through 3.3.0.

- [https://github.com/0xTerror/CVE-2026-78287](https://github.com/0xTerror/CVE-2026-78287) : ![starts](https://img.shields.io/github/stars/0xTerror/CVE-2026-78287.svg) ![forks](https://img.shields.io/github/forks/0xTerror/CVE-2026-78287.svg)

## CVE-2026-83548

- [https://github.com/0xTerror/CVE-2026-83548-CVE-2026-83549](https://github.com/0xTerror/CVE-2026-83548-CVE-2026-83549) : ![starts](https://img.shields.io/github/stars/0xTerror/CVE-2026-83548-CVE-2026-83549.svg) ![forks](https://img.shields.io/github/forks/0xTerror/CVE-2026-83548-CVE-2026-83549.svg)

## CVE-2026-83549

- [https://github.com/0xTerror/CVE-2026-83548-CVE-2026-83549](https://github.com/0xTerror/CVE-2026-83548-CVE-2026-83549) : ![starts](https://img.shields.io/github/stars/0xTerror/CVE-2026-83548-CVE-2026-83549.svg) ![forks](https://img.shields.io/github/forks/0xTerror/CVE-2026-83548-CVE-2026-83549.svg)

## CVE-2026-95518
> Time-of-check time-of-use (TOCTOU) race condition vulnerability in TÜBİTAK BİLGEM Yazılım Teknolojileri Araştırma Enstitüsü Pardus Package Installer allows Leveraging Time-of-Check and Time-of-Use (TOCTOU) Race Conditions.

This issue affects Pardus Package Installer: from 0.7.0 before 0.7.1.

- [https://github.com/ozcanpng/CVE-2026-95518](https://github.com/ozcanpng/CVE-2026-95518) : ![starts](https://img.shields.io/github/stars/ozcanpng/CVE-2026-95518.svg) ![forks](https://img.shields.io/github/forks/ozcanpng/CVE-2026-95518.svg)

## CVE-2026-99288
> In the Linux kernel, the following vulnerability has been resolved:

inet: reject unhashed sockets during established lookups

TCP established ehash lookups are lockless. The socket caches involved
use SLAB_TYPESAFE_BY_RCU, so memory can be reused before an RCU reader
that retained its old address has finished.

After a tuple match, __inet_lookup_established() and
__inet6_lookup_established() acquire a reference and repeat the tuple
check. They do not check whether the new object is hashed. If t

- [https://github.com/re4/noisytcp-poc](https://github.com/re4/noisytcp-poc) : ![starts](https://img.shields.io/github/stars/re4/noisytcp-poc.svg) ![forks](https://img.shields.io/github/forks/re4/noisytcp-poc.svg)
- [https://github.com/tal7aouy/NoisyTCP](https://github.com/tal7aouy/NoisyTCP) : ![starts](https://img.shields.io/github/stars/tal7aouy/NoisyTCP.svg) ![forks](https://img.shields.io/github/forks/tal7aouy/NoisyTCP.svg)
