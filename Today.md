# Update 2026-11-08
## CVE-2019-2215

- [https://github.com/RxinnotRstar/CVE-2019-2215-ForMIpad4](https://github.com/RxinnotRstar/CVE-2019-2215-ForMIpad4) : ![starts](https://img.shields.io/github/stars/RxinnotRstar/CVE-2019-2215-ForMIpad4.svg) ![forks](https://img.shields.io/github/forks/RxinnotRstar/CVE-2019-2215-ForMIpad4.svg)

## CVE-2019-6693

- [https://github.com/lureprey/fortidecrypter-CVE-2019-6693](https://github.com/lureprey/fortidecrypter-CVE-2019-6693) : ![starts](https://img.shields.io/github/stars/lureprey/fortidecrypter-CVE-2019-6693.svg) ![forks](https://img.shields.io/github/forks/lureprey/fortidecrypter-CVE-2019-6693.svg)

## CVE-2020-13405

- [https://github.com/nobleordu/CVE-2020-13405-MicroWeber-PoC](https://github.com/nobleordu/CVE-2020-13405-MicroWeber-PoC) : ![starts](https://img.shields.io/github/stars/nobleordu/CVE-2020-13405-MicroWeber-PoC.svg) ![forks](https://img.shields.io/github/forks/nobleordu/CVE-2020-13405-MicroWeber-PoC.svg)

## CVE-2023-41974

- [https://github.com/kienhho/Solarium](https://github.com/kienhho/Solarium) : ![starts](https://img.shields.io/github/stars/kienhho/Solarium.svg) ![forks](https://img.shields.io/github/forks/kienhho/Solarium.svg)

## CVE-2023-6931
> A heap out-of-bounds write vulnerability in the Linux kernel&#x27;s Performance Events system component can be exploited to achieve local privilege escalation.



A perf_event&#x27;s read_size can overflow, leading to an heap out-of-bounds increment or write in perf_read_group().



We recommend upgrading past commit 382c27f4ed28f803b1f1473ac2d8db0afc795a1b.

- [https://github.com/koast18/cve-2023-6931-hitv205n](https://github.com/koast18/cve-2023-6931-hitv205n) : ![starts](https://img.shields.io/github/stars/koast18/cve-2023-6931-hitv205n.svg) ![forks](https://img.shields.io/github/forks/koast18/cve-2023-6931-hitv205n.svg)

## CVE-2024-23222

- [https://github.com/xxsioo/coruna-lab](https://github.com/xxsioo/coruna-lab) : ![starts](https://img.shields.io/github/stars/xxsioo/coruna-lab.svg) ![forks](https://img.shields.io/github/forks/xxsioo/coruna-lab.svg)

## CVE-2025-59845

- [https://github.com/C3viche/cve-2025-59845](https://github.com/C3viche/cve-2025-59845) : ![starts](https://img.shields.io/github/stars/C3viche/cve-2025-59845.svg) ![forks](https://img.shields.io/github/forks/C3viche/cve-2025-59845.svg)

## CVE-2026-109618
> PHP uses longjmp() for out-of-memory (OOM) errors to exit the current context and abort handling of the request. Some contexts may not properly account for this scenario and leave request memory in an uninitialized state before performing an allocation. The subsequent request cleanup procedure may read or branch on this memory. Multiple OOM strategies can consistently trigger this condition and lead to remote code execution (RCE).

- [https://github.com/ameeshaheshan/ShellSpectre](https://github.com/ameeshaheshan/ShellSpectre) : ![starts](https://img.shields.io/github/stars/ameeshaheshan/ShellSpectre.svg) ![forks](https://img.shields.io/github/forks/ameeshaheshan/ShellSpectre.svg)
- [https://github.com/catscarlet/php-fpm-docker-PHP-8.1-CVE-2026-109618-109619-patched](https://github.com/catscarlet/php-fpm-docker-PHP-8.1-CVE-2026-109618-109619-patched) : ![starts](https://img.shields.io/github/stars/catscarlet/php-fpm-docker-PHP-8.1-CVE-2026-109618-109619-patched.svg) ![forks](https://img.shields.io/github/forks/catscarlet/php-fpm-docker-PHP-8.1-CVE-2026-109618-109619-patched.svg)

## CVE-2026-109619
> PHP has various global state that temporarily points into request memory. In some scenarios, global state may not be correctly reset, or may be repopulated after being reset. The global state may then refer to request memory even after it has been freed. Subsequent requests may read or branch on this stale state before it is fully initialized. Multiple strategies can trigger this condition and produce remote code execution (RCE).

- [https://github.com/MarceloAstudillo13/Tryhackme-PHP2Shell](https://github.com/MarceloAstudillo13/Tryhackme-PHP2Shell) : ![starts](https://img.shields.io/github/stars/MarceloAstudillo13/Tryhackme-PHP2Shell.svg) ![forks](https://img.shields.io/github/forks/MarceloAstudillo13/Tryhackme-PHP2Shell.svg)

## CVE-2026-111967
> The MP3 Audio Player  WordPress plugin before 5.16 does not escape one of its audio player shortcode attributes before outputting it into an HTML attribute, allowing users with Contributor-level access and above to inject arbitrary JavaScript that executes when another user, such as an administrator previewing a pending post, views the content.

- [https://github.com/HexxedBitHeadz/cve-2026-111967](https://github.com/HexxedBitHeadz/cve-2026-111967) : ![starts](https://img.shields.io/github/stars/HexxedBitHeadz/cve-2026-111967.svg) ![forks](https://img.shields.io/github/forks/HexxedBitHeadz/cve-2026-111967.svg)

## CVE-2026-112611
> An out-of-bounds write issue was addressed with improved bounds checking. This issue is fixed in iOS 26.7.2 and iPadOS 26.7.2, iOS 27.2 and iPadOS 27.2, macOS Sequoia 15.8.2, macOS Tahoe 26.7.2. Processing a maliciously crafted PDF file may lead to memory corruption.

- [https://github.com/Rust505/CVE-2026-112611](https://github.com/Rust505/CVE-2026-112611) : ![starts](https://img.shields.io/github/stars/Rust505/CVE-2026-112611.svg) ![forks](https://img.shields.io/github/forks/Rust505/CVE-2026-112611.svg)

## CVE-2026-114595
> In EPICS Base release 7.0.10 and prior, an integer overflow in network request processing can cause memory to be allocated with an incorrect size. Subsequent handling of attacker supplied data may result in memory corruption, denial of service, or potential remote code execution.

- [https://github.com/ashrafzaryouh/CVE-2026-114595](https://github.com/ashrafzaryouh/CVE-2026-114595) : ![starts](https://img.shields.io/github/stars/ashrafzaryouh/CVE-2026-114595.svg) ![forks](https://img.shields.io/github/forks/ashrafzaryouh/CVE-2026-114595.svg)

## CVE-2026-11645

- [https://github.com/ashrafzaryouh/CVE-2026-11645](https://github.com/ashrafzaryouh/CVE-2026-11645) : ![starts](https://img.shields.io/github/stars/ashrafzaryouh/CVE-2026-11645.svg) ![forks](https://img.shields.io/github/forks/ashrafzaryouh/CVE-2026-11645.svg)

## CVE-2026-119977
> WordPress Core is vulnerable to Remote Code Execution in versions 4.7 through 7.1.3. This is due to predictable, web-accessible staging paths used during full-package core upgrades. This makes it possible for unauthenticated attackers to execute code on the server during the upgrade window.

- [https://github.com/BugStealers/CVE-2026-119977](https://github.com/BugStealers/CVE-2026-119977) : ![starts](https://img.shields.io/github/stars/BugStealers/CVE-2026-119977.svg) ![forks](https://img.shields.io/github/forks/BugStealers/CVE-2026-119977.svg)
- [https://github.com/mehmet-emir-eroglu/CVE-2026-119977](https://github.com/mehmet-emir-eroglu/CVE-2026-119977) : ![starts](https://img.shields.io/github/stars/mehmet-emir-eroglu/CVE-2026-119977.svg) ![forks](https://img.shields.io/github/forks/mehmet-emir-eroglu/CVE-2026-119977.svg)

## CVE-2026-121265
> SQL::Abstract versions before 2.000003 for Perl allow SQL injection via an arrayref column value in insert and update.

With the array_datatypes option off, which is the default, insert(), update() and values() treat an arrayref column value as literal SQL. Its first element goes into the SQL text unescaped and the rest become bind values. A JSON array, or a repeated form field decoded as an arrayref, is such a value.

An application that passes request data as column values to insert or update 

- [https://github.com/googlesky/CVE-2026-121265](https://github.com/googlesky/CVE-2026-121265) : ![starts](https://img.shields.io/github/stars/googlesky/CVE-2026-121265.svg) ![forks](https://img.shields.io/github/forks/googlesky/CVE-2026-121265.svg)

## CVE-2026-123158
> sshd in OpenSSH before 10.6p2 on Linux, when musl libc is used without PAM, lacks a workaround for a password authentication bypass (related to misinterpretation of whether a string is intended to be a password hash). For some configurations of accounts, any password between 256 and 1024 characters succeeds. An example of a platform using musl libc without PAM is Alpine Linux.

- [https://github.com/Galaxy-sc/CVE-2026-123158](https://github.com/Galaxy-sc/CVE-2026-123158) : ![starts](https://img.shields.io/github/stars/Galaxy-sc/CVE-2026-123158.svg) ![forks](https://img.shields.io/github/forks/Galaxy-sc/CVE-2026-123158.svg)
- [https://github.com/GarphenGate/cve-2026-123158-defender-toolkit](https://github.com/GarphenGate/cve-2026-123158-defender-toolkit) : ![starts](https://img.shields.io/github/stars/GarphenGate/cve-2026-123158-defender-toolkit.svg) ![forks](https://img.shields.io/github/forks/GarphenGate/cve-2026-123158-defender-toolkit.svg)
- [https://github.com/liamromanis101/MaSSHole](https://github.com/liamromanis101/MaSSHole) : ![starts](https://img.shields.io/github/stars/liamromanis101/MaSSHole.svg) ![forks](https://img.shields.io/github/forks/liamromanis101/MaSSHole.svg)

## CVE-2026-123488
> Craft CMS 4.0.0 before 4.18.9 and 5.0.0 before 5.11.2 contains an unauthenticated SQL injection vulnerability in the element search endpoint because the attribute parameter is concatenated into the query unsanitized and emulated PDO prepares allow stacked statements. Remote attackers can read and write the database, setting the admin flag or overwriting password hashes in the users table to gain administrator access.

- [https://github.com/dinosn/CVE-2026-123488-CraftCMS-Lab](https://github.com/dinosn/CVE-2026-123488-CraftCMS-Lab) : ![starts](https://img.shields.io/github/stars/dinosn/CVE-2026-123488-CraftCMS-Lab.svg) ![forks](https://img.shields.io/github/forks/dinosn/CVE-2026-123488-CraftCMS-Lab.svg)

## CVE-2026-123753

- [https://github.com/googlesky/CVE-2026-123753](https://github.com/googlesky/CVE-2026-123753) : ![starts](https://img.shields.io/github/stars/googlesky/CVE-2026-123753.svg) ![forks](https://img.shields.io/github/forks/googlesky/CVE-2026-123753.svg)

## CVE-2026-124040
> CivetWeb through 1.16, when built with USE_HTTP2 and enable_http2 on, contains a use-after-free vulnerability in handle_http2() that retains freed :method and :path pointers. Unauthenticated remote attackers can send a later HEADERS frame omitting these pseudo-headers to influence request method or path seen by access rules, or crash the server.

- [https://github.com/zeetee1235/CVE-2026-124040](https://github.com/zeetee1235/CVE-2026-124040) : ![starts](https://img.shields.io/github/stars/zeetee1235/CVE-2026-124040.svg) ![forks](https://img.shields.io/github/forks/zeetee1235/CVE-2026-124040.svg)

## CVE-2026-13684

- [https://github.com/maxprog-svg/CVE-2026-13684](https://github.com/maxprog-svg/CVE-2026-13684) : ![starts](https://img.shields.io/github/stars/maxprog-svg/CVE-2026-13684.svg) ![forks](https://img.shields.io/github/forks/maxprog-svg/CVE-2026-13684.svg)

## CVE-2026-15409

- [https://github.com/ashrafzaryouh/CVE-2026-15409](https://github.com/ashrafzaryouh/CVE-2026-15409) : ![starts](https://img.shields.io/github/stars/ashrafzaryouh/CVE-2026-15409.svg) ![forks](https://img.shields.io/github/forks/ashrafzaryouh/CVE-2026-15409.svg)

## CVE-2026-19553
> ssl.SSLContext.wrap_bio() didn&#x27;t require the server_hostname argument
to not be None if ssl.SSLContext.check_hostname was set. Due to a
missing parameter check in SSLObject, if the server_hostname argument
isn&#x27;t supplied then hostname verification would be silently skipped.


This defect could lead to programs where certificate hostname verification
*appeared* to be succeeding with SSLContext.check_hostname = True and no
ValueError being raised due to misconfiguration.


If the program passes a 

- [https://github.com/monkeyyey/acw3-tls-lab](https://github.com/monkeyyey/acw3-tls-lab) : ![starts](https://img.shields.io/github/stars/monkeyyey/acw3-tls-lab.svg) ![forks](https://img.shields.io/github/forks/monkeyyey/acw3-tls-lab.svg)

## CVE-2026-19868
> An authentication enforcement vulnerability in SonicOS SSLVPN service may allow a user with valid credentials for an alternate authentication method to bypass SAML authentication controls. Successful exploitation may also bypass SAML-enforced multi-factor authentication (MFA).

- [https://github.com/foxcornlab/sonicwall-sonicos-scanner](https://github.com/foxcornlab/sonicwall-sonicos-scanner) : ![starts](https://img.shields.io/github/stars/foxcornlab/sonicwall-sonicos-scanner.svg) ![forks](https://img.shields.io/github/forks/foxcornlab/sonicwall-sonicos-scanner.svg)

## CVE-2026-20131

- [https://github.com/ashrafzaryouh/CVE-2026-20131](https://github.com/ashrafzaryouh/CVE-2026-20131) : ![starts](https://img.shields.io/github/stars/ashrafzaryouh/CVE-2026-20131.svg) ![forks](https://img.shields.io/github/forks/ashrafzaryouh/CVE-2026-20131.svg)

## CVE-2026-20700

- [https://github.com/haroonwattoo556677-max/ios-forensic-exploitation-framework](https://github.com/haroonwattoo556677-max/ios-forensic-exploitation-framework) : ![starts](https://img.shields.io/github/stars/haroonwattoo556677-max/ios-forensic-exploitation-framework.svg) ![forks](https://img.shields.io/github/forks/haroonwattoo556677-max/ios-forensic-exploitation-framework.svg)

## CVE-2026-25089

- [https://github.com/ashrafzaryouh/CVE-2026-25089](https://github.com/ashrafzaryouh/CVE-2026-25089) : ![starts](https://img.shields.io/github/stars/ashrafzaryouh/CVE-2026-25089.svg) ![forks](https://img.shields.io/github/forks/ashrafzaryouh/CVE-2026-25089.svg)

## CVE-2026-2699

- [https://github.com/ashrafzaryouh/CVE-2026-2699](https://github.com/ashrafzaryouh/CVE-2026-2699) : ![starts](https://img.shields.io/github/stars/ashrafzaryouh/CVE-2026-2699.svg) ![forks](https://img.shields.io/github/forks/ashrafzaryouh/CVE-2026-2699.svg)

## CVE-2026-41462

- [https://github.com/ashrafzaryouh/CVE-2026-41462](https://github.com/ashrafzaryouh/CVE-2026-41462) : ![starts](https://img.shields.io/github/stars/ashrafzaryouh/CVE-2026-41462.svg) ![forks](https://img.shields.io/github/forks/ashrafzaryouh/CVE-2026-41462.svg)

## CVE-2026-42016

- [https://github.com/dylvie/CVE-2026-42016_CVE-2026-42018](https://github.com/dylvie/CVE-2026-42016_CVE-2026-42018) : ![starts](https://img.shields.io/github/stars/dylvie/CVE-2026-42016_CVE-2026-42018.svg) ![forks](https://img.shields.io/github/forks/dylvie/CVE-2026-42016_CVE-2026-42018.svg)

## CVE-2026-42018
> JFrog Artifactory could return an internal anonymous-user token to an unauthenticated caller when anonymous access is disabled, potentially exposing sensitive resources.

- [https://github.com/dylvie/CVE-2026-42016_CVE-2026-42018](https://github.com/dylvie/CVE-2026-42016_CVE-2026-42018) : ![starts](https://img.shields.io/github/stars/dylvie/CVE-2026-42016_CVE-2026-42018.svg) ![forks](https://img.shields.io/github/forks/dylvie/CVE-2026-42016_CVE-2026-42018.svg)

## CVE-2026-43284
> In the Linux kernel, the following vulnerability has been resolved:

xfrm: esp: avoid in-place decrypt on shared skb frags

MSG_SPLICE_PAGES can attach pages from a pipe directly to an skb. TCP
marks such skbs with SKBFL_SHARED_FRAG after skb_splice_from_iter(),
so later paths that may modify packet data can first make a private
copy. The IPv4/IPv6 datagram append paths did not set this flag when
splicing pages into UDP skbs.

That leaves an ESP-in-UDP packet made from shared pipe pages looking


- [https://github.com/Jean7z/DFRoot-DirtyFrag](https://github.com/Jean7z/DFRoot-DirtyFrag) : ![starts](https://img.shields.io/github/stars/Jean7z/DFRoot-DirtyFrag.svg) ![forks](https://img.shields.io/github/forks/Jean7z/DFRoot-DirtyFrag.svg)
- [https://github.com/nemoiwkryang/pd2301-dirtyfrag-root](https://github.com/nemoiwkryang/pd2301-dirtyfrag-root) : ![starts](https://img.shields.io/github/stars/nemoiwkryang/pd2301-dirtyfrag-root.svg) ![forks](https://img.shields.io/github/forks/nemoiwkryang/pd2301-dirtyfrag-root.svg)

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
- [https://github.com/Viper-Boss/iqoo-neo5-temp-root](https://github.com/Viper-Boss/iqoo-neo5-temp-root) : ![starts](https://img.shields.io/github/stars/Viper-Boss/iqoo-neo5-temp-root.svg) ![forks](https://img.shields.io/github/forks/Viper-Boss/iqoo-neo5-temp-root.svg)

## CVE-2026-4480
> A flaw was found in the Samba printing subsystem. Samba passes the client-controlled job description string to the command configured with the &quot;print command&quot; setting via the &quot;%J&quot;
substitution character without escaping shell meta characters. A remote attacker could exploit this vulnerability by sending a specially crafted print job description that contains unescaped shell characters. This could lead to remote code execution on the affected system.

- [https://github.com/ashrafzaryouh/CVE-2026-4480](https://github.com/ashrafzaryouh/CVE-2026-4480) : ![starts](https://img.shields.io/github/stars/ashrafzaryouh/CVE-2026-4480.svg) ![forks](https://img.shields.io/github/forks/ashrafzaryouh/CVE-2026-4480.svg)

## CVE-2026-56848

- [https://github.com/CompleteTech-Security/node-cve-2026-56848-check](https://github.com/CompleteTech-Security/node-cve-2026-56848-check) : ![starts](https://img.shields.io/github/stars/CompleteTech-Security/node-cve-2026-56848-check.svg) ![forks](https://img.shields.io/github/forks/CompleteTech-Security/node-cve-2026-56848-check.svg)

## CVE-2026-63030
> WordPress 6.9.x before 6.9.5 and 7.0.x before 7.0.2 is affected by a REST API batch endpoint route confusion issue which, combined with the author__not_in WP_Query SQL Injection (CVE-2026-60137), could allow an attacker to perform SQL Injection and achieve Remote Code Execution.

- [https://github.com/noxcrypt-x/CVE-2026-63030](https://github.com/noxcrypt-x/CVE-2026-63030) : ![starts](https://img.shields.io/github/stars/noxcrypt-x/CVE-2026-63030.svg) ![forks](https://img.shields.io/github/forks/noxcrypt-x/CVE-2026-63030.svg)

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

- [https://github.com/000999888111/op13-cve-2026-64560](https://github.com/000999888111/op13-cve-2026-64560) : ![starts](https://img.shields.io/github/stars/000999888111/op13-cve-2026-64560.svg) ![forks](https://img.shields.io/github/forks/000999888111/op13-cve-2026-64560.svg)

## CVE-2026-6952

- [https://github.com/stevejiang0509/zyxel-cve-2026-6952-model-scope](https://github.com/stevejiang0509/zyxel-cve-2026-6952-model-scope) : ![starts](https://img.shields.io/github/stars/stevejiang0509/zyxel-cve-2026-6952-model-scope.svg) ![forks](https://img.shields.io/github/forks/stevejiang0509/zyxel-cve-2026-6952-model-scope.svg)

## CVE-2026-83844

- [https://github.com/blkph0x/CVE-2026-83844_POC](https://github.com/blkph0x/CVE-2026-83844_POC) : ![starts](https://img.shields.io/github/stars/blkph0x/CVE-2026-83844_POC.svg) ![forks](https://img.shields.io/github/forks/blkph0x/CVE-2026-83844_POC.svg)

## CVE-2026-87690
> The Metasploit Framework post module post/apple_ios/gather/ios_image_gather is affected by a relative path traversal vulnerability (CWE-22). The module interpolates file names taken from a Meterpreter directory listing — data fully controlled by a hostile or tampered iOS device — directly into the local destination path passed to client.fs.file.download_file(), with no sanitization. The underlying stdapi sink (lib/rex/post/meterpreter/extensions/stdapi/fs/file.rb) writes to whatever path is supp

- [https://github.com/h00die/CVE-2026-87690-POC-Metasploit-Dir-Traverse-to-RCE](https://github.com/h00die/CVE-2026-87690-POC-Metasploit-Dir-Traverse-to-RCE) : ![starts](https://img.shields.io/github/stars/h00die/CVE-2026-87690-POC-Metasploit-Dir-Traverse-to-RCE.svg) ![forks](https://img.shields.io/github/forks/h00die/CVE-2026-87690-POC-Metasploit-Dir-Traverse-to-RCE.svg)

## CVE-2026-8932

- [https://github.com/ashrafzaryouh/CVE-2026-8932](https://github.com/ashrafzaryouh/CVE-2026-8932) : ![starts](https://img.shields.io/github/stars/ashrafzaryouh/CVE-2026-8932.svg) ![forks](https://img.shields.io/github/forks/ashrafzaryouh/CVE-2026-8932.svg)

## CVE-2026-98260
> In the Linux kernel, the following vulnerability has been resolved:

exec: Cleanup POSIX timers right after de_thread()

A per-thread CPU timer holds a reference to the PID of the thread it is
attached to and, while it is armed, its node is queued in that thread&#x27;s
posix_cputimers. The task is looked up by that PID.

When a non-leader thread exec()s, de_thread() changes which task owns
that PID. pid_task(timer-&gt;it.cpu.pid, PIDTYPE_PID) then returns NULL,
but the node is still queued on tsk, which

- [https://github.com/MocLG/Time-My-Galaxy](https://github.com/MocLG/Time-My-Galaxy) : ![starts](https://img.shields.io/github/stars/MocLG/Time-My-Galaxy.svg) ![forks](https://img.shields.io/github/forks/MocLG/Time-My-Galaxy.svg)
- [https://github.com/knowlily/cve-2026-98260-bvl-an16](https://github.com/knowlily/cve-2026-98260-bvl-an16) : ![starts](https://img.shields.io/github/stars/knowlily/cve-2026-98260-bvl-an16.svg) ![forks](https://img.shields.io/github/forks/knowlily/cve-2026-98260-bvl-an16.svg)
- [https://github.com/knowlily/m6-shell](https://github.com/knowlily/m6-shell) : ![starts](https://img.shields.io/github/stars/knowlily/m6-shell.svg) ![forks](https://img.shields.io/github/forks/knowlily/m6-shell.svg)

## CVE-2026-99273
> In the Linux kernel, the following vulnerability has been resolved:

ksmbd: reserve space for the UTF-16 terminator in stream info

smb_strtoUTF16() always writes a terminating zero UTF-16 unit after the
converted characters, but get_file_stream_info() budgets only
sizeof(struct smb2_file_stream_info) + streamlen * 2 for a stream entry
and sizeof(struct smb2_file_stream_info) + 7 * 2 for the trailing
&quot;::$DATA&quot; entry. When an entry exactly fills the 448-byte small response
buffer, the terminator 

- [https://github.com/googlesky/CVE-2026-99273](https://github.com/googlesky/CVE-2026-99273) : ![starts](https://img.shields.io/github/stars/googlesky/CVE-2026-99273.svg) ![forks](https://img.shields.io/github/forks/googlesky/CVE-2026-99273.svg)
