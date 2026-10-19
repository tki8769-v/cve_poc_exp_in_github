# Update 2026-10-19
## CVE-2024-23334

- [https://github.com/JohnnyWang108/hdu-is-lab1-secure-api](https://github.com/JohnnyWang108/hdu-is-lab1-secure-api) : ![starts](https://img.shields.io/github/stars/JohnnyWang108/hdu-is-lab1-secure-api.svg) ![forks](https://img.shields.io/github/forks/JohnnyWang108/hdu-is-lab1-secure-api.svg)

## CVE-2024-23897

- [https://github.com/ydkdk12345-bot/CVE-2024-23897-CTF](https://github.com/ydkdk12345-bot/CVE-2024-23897-CTF) : ![starts](https://img.shields.io/github/stars/ydkdk12345-bot/CVE-2024-23897-CTF.svg) ![forks](https://img.shields.io/github/forks/ydkdk12345-bot/CVE-2024-23897-CTF.svg)

## CVE-2024-27198

- [https://github.com/wonnnggge/CVE-2024-27198_CTF](https://github.com/wonnnggge/CVE-2024-27198_CTF) : ![starts](https://img.shields.io/github/stars/wonnnggge/CVE-2024-27198_CTF.svg) ![forks](https://img.shields.io/github/forks/wonnnggge/CVE-2024-27198_CTF.svg)

## CVE-2025-55182
> A pre-authentication remote code execution vulnerability exists in React Server Components versions 19.0.0, 19.1.0, 19.1.1, and 19.2.0 including the following packages: react-server-dom-parcel, react-server-dom-turbopack, and react-server-dom-webpack. The vulnerable code unsafely deserializes payloads from HTTP requests to Server Function endpoints.

- [https://github.com/0xRAM-bit/CVE-2025-55182](https://github.com/0xRAM-bit/CVE-2025-55182) : ![starts](https://img.shields.io/github/stars/0xRAM-bit/CVE-2025-55182.svg) ![forks](https://img.shields.io/github/forks/0xRAM-bit/CVE-2025-55182.svg)

## CVE-2026-27606

- [https://github.com/AaaronP/Seguridad---Proyecto-de-investigaci-n](https://github.com/AaaronP/Seguridad---Proyecto-de-investigaci-n) : ![starts](https://img.shields.io/github/stars/AaaronP/Seguridad---Proyecto-de-investigaci-n.svg) ![forks](https://img.shields.io/github/forks/AaaronP/Seguridad---Proyecto-de-investigaci-n.svg)

## CVE-2026-53582
> OPNsense is a FreeBSD based firewall and routing platform. Prior to version 26.1.10, the Trust module stores attacker-controlled certificate authority and certificate refid values and interpolates them into XPath expressions in src/opnsense/mvc/app/models/OPNsense/Trust/FieldTypes/CAsField.php and src/opnsense/mvc/app/models/OPNsense/Trust/FieldTypes/CertificatesField.php. A user with CA Manager or Certificate Manager privileges can submit a crafted refid and repeatedly retrieve the object to ob

- [https://github.com/eev4n/CVE-2026-53582](https://github.com/eev4n/CVE-2026-53582) : ![starts](https://img.shields.io/github/stars/eev4n/CVE-2026-53582.svg) ![forks](https://img.shields.io/github/forks/eev4n/CVE-2026-53582.svg)

## CVE-2026-64560
> In the Linux kernel, the following vulnerability has been resolved:

posix-cpu-timers: Prevent UAF caused by non-leader exec() race

Wongi and Jungwoo decoded and reported a non-leader exec() related race
which can result in an UAF:

 sys_timer_delete()			exec()
   posix_cpu_timer_del()
   // Observes old leader
   p = pid_task(pid, pid_type);		de_thread()
   					  switch_leader();
					  release_task(old_leader)
					    __exit_signal(old_leader)
					      sighand = lock(old_leader, sighand);

- [https://github.com/Feng1586/CVE-2026-64560-public](https://github.com/Feng1586/CVE-2026-64560-public) : ![starts](https://img.shields.io/github/stars/Feng1586/CVE-2026-64560-public.svg) ![forks](https://img.shields.io/github/forks/Feng1586/CVE-2026-64560-public.svg)
- [https://github.com/Feng1586/CVE-2026-64560-sources](https://github.com/Feng1586/CVE-2026-64560-sources) : ![starts](https://img.shields.io/github/stars/Feng1586/CVE-2026-64560-sources.svg) ![forks](https://img.shields.io/github/forks/Feng1586/CVE-2026-64560-sources.svg)
- [https://github.com/itsmichiya/exploit-CVE-2026-64560](https://github.com/itsmichiya/exploit-CVE-2026-64560) : ![starts](https://img.shields.io/github/stars/itsmichiya/exploit-CVE-2026-64560.svg) ![forks](https://img.shields.io/github/forks/itsmichiya/exploit-CVE-2026-64560.svg)

## CVE-2026-99999
> In the Linux kernel, the following vulnerability has been resolved:

ipv4: validate checksum_start before completing checksum

If a packet with bad checksum metadata gets into the ipv4 stack,
skb_checksum_help can corrupt the network header and cause a bunch of
mischief.

This was discovered and reported by Paulos, and has been reporoduced
by others independently since.

We really shouldn&#x27;t allow such packets in, but as a defence
in depth measure, let&#x27;s also check before we complete the checksum

- [https://github.com/gandli/CVE-2026-99999-pwnescape](https://github.com/gandli/CVE-2026-99999-pwnescape) : ![starts](https://img.shields.io/github/stars/gandli/CVE-2026-99999-pwnescape.svg) ![forks](https://img.shields.io/github/forks/gandli/CVE-2026-99999-pwnescape.svg)
