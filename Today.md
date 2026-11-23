# Update 2026-11-23
## CVE-2017-2636

- [https://github.com/OYMMYO/n_hdlc-cve-2017-2636](https://github.com/OYMMYO/n_hdlc-cve-2017-2636) : ![starts](https://img.shields.io/github/stars/OYMMYO/n_hdlc-cve-2017-2636.svg) ![forks](https://img.shields.io/github/forks/OYMMYO/n_hdlc-cve-2017-2636.svg)

## CVE-2021-44228

- [https://github.com/johnyProDev/CVE-2021-44228-Writeup](https://github.com/johnyProDev/CVE-2021-44228-Writeup) : ![starts](https://img.shields.io/github/stars/johnyProDev/CVE-2021-44228-Writeup.svg) ![forks](https://img.shields.io/github/forks/johnyProDev/CVE-2021-44228-Writeup.svg)

## CVE-2022-24905

- [https://github.com/googlesky/CVE-2022-24905](https://github.com/googlesky/CVE-2022-24905) : ![starts](https://img.shields.io/github/stars/googlesky/CVE-2022-24905.svg) ![forks](https://img.shields.io/github/forks/googlesky/CVE-2022-24905.svg)

## CVE-2026-0776

- [https://github.com/0xbye/CVE-2026-0776](https://github.com/0xbye/CVE-2026-0776) : ![starts](https://img.shields.io/github/stars/0xbye/CVE-2026-0776.svg) ![forks](https://img.shields.io/github/forks/0xbye/CVE-2026-0776.svg)

## CVE-2026-102697
> Ollama versions 0.14.0 before 0.31.2 contain an incorrect authorization vulnerability in the experimental agent mode Bash tool approval mechanism that fails to properly parse shell syntax. Attackers who can influence model output through prompt injection can execute additional shell commands by appending control operators like semicolons or logical operators to approved commands, bypassing the session approval requirement.

- [https://github.com/akinerkisa/llamasmuggle-cve-2026-102697](https://github.com/akinerkisa/llamasmuggle-cve-2026-102697) : ![starts](https://img.shields.io/github/stars/akinerkisa/llamasmuggle-cve-2026-102697.svg) ![forks](https://img.shields.io/github/forks/akinerkisa/llamasmuggle-cve-2026-102697.svg)

## CVE-2026-102945

- [https://github.com/googlesky/CVE-2026-102945](https://github.com/googlesky/CVE-2026-102945) : ![starts](https://img.shields.io/github/stars/googlesky/CVE-2026-102945.svg) ![forks](https://img.shields.io/github/forks/googlesky/CVE-2026-102945.svg)

## CVE-2026-103026
> Paymenter is a free and open-source webshop solution for management of hosting services. Prior to 1.5.7, the HasConfirmation trait in app/Livewire/Traits/HasConfirmation.php, included by app/Livewire/Component.php across 36 client-facing Livewire components, exposed executeConfirmedAction as a public action that invoked any component method accepted by method_exists. The action could call inherited InteractsWithProperties::fill(), whose data_set() writes arbitrary public properties, including st

- [https://github.com/googlesky/CVE-2026-103026](https://github.com/googlesky/CVE-2026-103026) : ![starts](https://img.shields.io/github/stars/googlesky/CVE-2026-103026.svg) ![forks](https://img.shields.io/github/forks/googlesky/CVE-2026-103026.svg)

## CVE-2026-103035
> TeamPass is a self-hosted collaborative password manager. Prior to 3.2.1.2, the update_folder action in app/sources/folders.queries.php allowed an authenticated, non-read-only user to re-parent a folder without checking whether the target folder or submitted parentId belonged to the caller&#x27;s user-accessible_folders set. Selecting a personal folder as the new parent passed the personal-folder guard and set personal_folder on the target, transferring the credential subtree into the attacker&#x27;s acce

- [https://github.com/googlesky/CVE-2026-103035](https://github.com/googlesky/CVE-2026-103035) : ![starts](https://img.shields.io/github/stars/googlesky/CVE-2026-103035.svg) ![forks](https://img.shields.io/github/forks/googlesky/CVE-2026-103035.svg)

## CVE-2026-104099

- [https://github.com/googlesky/CVE-2026-104099](https://github.com/googlesky/CVE-2026-104099) : ![starts](https://img.shields.io/github/stars/googlesky/CVE-2026-104099.svg) ![forks](https://img.shields.io/github/forks/googlesky/CVE-2026-104099.svg)

## CVE-2026-104129
> pREST (PostgreSQL REST) is an API that delivers an application on top of a Postgres database. Prior to 2.4.0, the vulnerable parameter is _groupby, handled by GroupByClause in adapters/postgres/postgres.go. adapters/postgres/postgres.go uses the weaker isSafeSQLExpression check for this function-expression branch instead of the stricter single-field validator used for _select. That check validates only the outer function name against a 13-function allowlist and permits nested subqueries, trailin

- [https://github.com/googlesky/CVE-2026-104129](https://github.com/googlesky/CVE-2026-104129) : ![starts](https://img.shields.io/github/stars/googlesky/CVE-2026-104129.svg) ![forks](https://img.shields.io/github/forks/googlesky/CVE-2026-104129.svg)

## CVE-2026-109618
> PHP uses longjmp() for out-of-memory (OOM) errors to exit the current context and abort handling of the request. Some contexts may not properly account for this scenario and leave request memory in an uninitialized state before performing an allocation. The subsequent request cleanup procedure may read or branch on this memory. Multiple OOM strategies can consistently trigger this condition and lead to remote code execution (RCE).

- [https://github.com/bipul-unexpected/CVE-2026-109618-2026-109619](https://github.com/bipul-unexpected/CVE-2026-109618-2026-109619) : ![starts](https://img.shields.io/github/stars/bipul-unexpected/CVE-2026-109618-2026-109619.svg) ![forks](https://img.shields.io/github/forks/bipul-unexpected/CVE-2026-109618-2026-109619.svg)

## CVE-2026-112554
> An out-of-bounds read was addressed with improved bounds checking. This issue is fixed in iOS 26.7.2 and iPadOS 26.7.2, iOS 27.2 and iPadOS 27.2, macOS Golden Gate 27.2, macOS Sequoia 15.8.2, macOS Tahoe 26.7.2. An app may be able to cause unexpected system termination or read kernel memory.

- [https://github.com/ecc521/CVE-2026-112554](https://github.com/ecc521/CVE-2026-112554) : ![starts](https://img.shields.io/github/stars/ecc521/CVE-2026-112554.svg) ![forks](https://img.shields.io/github/forks/ecc521/CVE-2026-112554.svg)

## CVE-2026-113910
> A memory initialization issue was addressed with improved memory handling. This issue is fixed in iOS 26.7.2 and iPadOS 26.7.2, iOS 27.2 and iPadOS 27.2, macOS Golden Gate 27.2, macOS Sequoia 15.8.2, macOS Tahoe 26.7.2, tvOS 27.2, visionOS 27.2, watchOS 27.2. An app may be able to disclose kernel memory.

- [https://github.com/ecc521/CVE-2026-113910](https://github.com/ecc521/CVE-2026-113910) : ![starts](https://img.shields.io/github/stars/ecc521/CVE-2026-113910.svg) ![forks](https://img.shields.io/github/forks/ecc521/CVE-2026-113910.svg)

## CVE-2026-114516

- [https://github.com/googlesky/CVE-2026-114516](https://github.com/googlesky/CVE-2026-114516) : ![starts](https://img.shields.io/github/stars/googlesky/CVE-2026-114516.svg) ![forks](https://img.shields.io/github/forks/googlesky/CVE-2026-114516.svg)

## CVE-2026-119077
> The ELEX WordPress HelpDesk &amp; Customer Ticketing System plugin for WordPress is vulnerable to PHP Object Injection in all versions up to, and including, 3.3.9 via the &#x27;form (specifically the attacker-controlled ticket_label field inside the url-encoded form string)&#x27; parameter parameter. This is due to missing server-side authentication and the absence of a class allowlist on deserialization, with the only guard being a nonce publicly emitted on any page carrying the [wsdesk_support] shortcode. T

- [https://github.com/v0nx6/CVE-2026-119077](https://github.com/v0nx6/CVE-2026-119077) : ![starts](https://img.shields.io/github/stars/v0nx6/CVE-2026-119077.svg) ![forks](https://img.shields.io/github/forks/v0nx6/CVE-2026-119077.svg)

## CVE-2026-120343
> A flaw has been found in mathurvishal CloudClassroom-PHP-Project. The impacted element is an unknown function of the file manageassessment2.php. This manipulation of the argument ExamName/Q1/Q2/Q3/Q4/Q5 causes cross site scripting. The attack is possible to be carried out remotely. The exploit has been published and may be used. This product adopts a rolling release strategy to maintain continuous delivery. Therefore, version details for affected or updated releases cannot be specified. The vend

- [https://github.com/capivara-research/CVE-2026-120343](https://github.com/capivara-research/CVE-2026-120343) : ![starts](https://img.shields.io/github/stars/capivara-research/CVE-2026-120343.svg) ![forks](https://img.shields.io/github/forks/capivara-research/CVE-2026-120343.svg)

## CVE-2026-120539

- [https://github.com/foxcornlab/buddypress-restrictions-scanner](https://github.com/foxcornlab/buddypress-restrictions-scanner) : ![starts](https://img.shields.io/github/stars/foxcornlab/buddypress-restrictions-scanner.svg) ![forks](https://img.shields.io/github/forks/foxcornlab/buddypress-restrictions-scanner.svg)

## CVE-2026-122247

- [https://github.com/googlesky/CVE-2026-122247](https://github.com/googlesky/CVE-2026-122247) : ![starts](https://img.shields.io/github/stars/googlesky/CVE-2026-122247.svg) ![forks](https://img.shields.io/github/forks/googlesky/CVE-2026-122247.svg)

## CVE-2026-123890
> VMware vCenter contains an authentication bypass vulnerability in the VMware Directory Service.
Affected versions: 9.1.x (fixed in 9.1.1.0200); 9.0.x (fixed in 9.0.2.0200); 8.0 (fixed in 8.0 U3m); 5.x (fixed in 5.2.5).
Telco Cloud Platform 3.0, 4.x, 5.0.x, 5.1.x, 5.2 and Telco Cloud Infrastructure 3.0 are also affected (see KB463116).

- [https://github.com/dinosn/CVE-2026-123890](https://github.com/dinosn/CVE-2026-123890) : ![starts](https://img.shields.io/github/stars/dinosn/CVE-2026-123890.svg) ![forks](https://img.shields.io/github/forks/dinosn/CVE-2026-123890.svg)

## CVE-2026-125396
> Ghostscript before 10.08.0 contains a -dSAFER bypass vulnerability in the .putgstringcopy procedure in gs_fonts.ps, which calls the privileged .forceput operator without checking operand types. Attackers can supply crafted PostScript or PDF documents that trigger a type error, recover .forceput via a custom error handler, and cause a use-after-free across save/restore to execute arbitrary code.

- [https://github.com/0xBlackash/CVE-2026-125396](https://github.com/0xBlackash/CVE-2026-125396) : ![starts](https://img.shields.io/github/stars/0xBlackash/CVE-2026-125396.svg) ![forks](https://img.shields.io/github/forks/0xBlackash/CVE-2026-125396.svg)

## CVE-2026-128136
> NLTK (Natural Language Toolkit) is a suite of open source Python modules, data sets, and tutorials supporting research and development in Natural Language Processing. From 3.10.0 until 3.10.4, allowlisted_pickle_load keys dangerous NumPy globals by export name, allowing submodule-local numpy.lib file input/output callables to evade the denylist under the broad module allowance used by TransitionParser. A crafted pickle can invoke recfromtxt to read a local file or open_memmap to create or trunca

- [https://github.com/googlesky/CVE-2026-128136](https://github.com/googlesky/CVE-2026-128136) : ![starts](https://img.shields.io/github/stars/googlesky/CVE-2026-128136.svg) ![forks](https://img.shields.io/github/forks/googlesky/CVE-2026-128136.svg)

## CVE-2026-128137
> NLTK (Natural Language Toolkit) is a suite of open source Python modules, data sets, and tutorials supporting research and development in Natural Language Processing. From 3.9.4 until 3.10.4, NLTK corpus-reader path pointers and view methods validate a requested relative path without consistently resolving intermediate directory symlinks against the reader&#x27;s scoped root. A local attacker who can place such a symlink can make abspaths or words reach a readable file outside the corpus root and dis

- [https://github.com/googlesky/CVE-2026-128137](https://github.com/googlesky/CVE-2026-128137) : ![starts](https://img.shields.io/github/stars/googlesky/CVE-2026-128137.svg) ![forks](https://img.shields.io/github/forks/googlesky/CVE-2026-128137.svg)

## CVE-2026-128138
> NLTK (Natural Language Toolkit) is a suite of open source Python modules, data sets, and tutorials supporting research and development in Natural Language Processing. From 3.10.3 until 3.10.4, the NLTK 3.10.3 JVM hardening validates Java launcher tokens in the options channel but appends the caller-controlled cmd sequence without requiring its first token to be a main class. Supplying -jar or an @argfile through nltk.internals.java or StanfordSegmenter.java_class can therefore execute attacker-s

- [https://github.com/googlesky/CVE-2026-128138](https://github.com/googlesky/CVE-2026-128138) : ![starts](https://img.shields.io/github/stars/googlesky/CVE-2026-128138.svg) ![forks](https://img.shields.io/github/forks/googlesky/CVE-2026-128138.svg)

## CVE-2026-128139
> NLTK (Natural Language Toolkit) is a suite of open source Python modules, data sets, and tutorials supporting research and development in Natural Language Processing. From 3.6 to 3.10.3, XMLCorpusView._read_xml_fragment accumulates 1 KiB blocks and repeatedly applies whole-buffer XML validation while a comment or CDATA terminator remains ahead. A large comment in an attacker-controlled corpus file causes quadratic CPU consumption through documented XML corpus readers across the affected range. O

- [https://github.com/googlesky/CVE-2026-128139](https://github.com/googlesky/CVE-2026-128139) : ![starts](https://img.shields.io/github/stars/googlesky/CVE-2026-128139.svg) ![forks](https://img.shields.io/github/forks/googlesky/CVE-2026-128139.svg)

## CVE-2026-128140
> NLTK (Natural Language Toolkit) is a suite of open source Python modules, data sets, and tutorials supporting research and development in Natural Language Processing. From 3.6.7 until 3.10.4, nltk.downloader follows collection membership without tracking already visited collection nodes. A self-referencing or mutually referencing collection index can therefore make the package-closure walk loop indefinitely while its queue and memory usage grow, denying service when a victim processes the attack

- [https://github.com/googlesky/CVE-2026-128140](https://github.com/googlesky/CVE-2026-128140) : ![starts](https://img.shields.io/github/stars/googlesky/CVE-2026-128140.svg) ![forks](https://img.shields.io/github/forks/googlesky/CVE-2026-128140.svg)

## CVE-2026-129221
> NLTK (Natural Language Toolkit) is a suite of open source Python modules, data sets, and tutorials supporting research and development in Natural Language Processing. Prior to 3.10.4, nltk.classify.weka.ARFF_Formatter writes attacker-controlled class labels into the Weka ARFF @ATTRIBUTE &#x27;-label-&#x27; declaration without safely formatting the label tokens. Crafted labels can alter the generated ARFF schema or records, corrupting classifier input and causing integrity loss or processing failure. This 

- [https://github.com/googlesky/CVE-2026-129221](https://github.com/googlesky/CVE-2026-129221) : ![starts](https://img.shields.io/github/stars/googlesky/CVE-2026-129221.svg) ![forks](https://img.shields.io/github/forks/googlesky/CVE-2026-129221.svg)

## CVE-2026-129496
> Timezone cache use-after-free can lead to remote code execution.

In non-thread-safe builds, a diagnostic written to a file-based error_log during module startup, for example for an invalid date.timezone value or a session configuration warning, causes the timezone cache to be allocated in startup memory that is freed while a reference to it is kept. A diagnostic raised early in the first request of a worker, such as the max_input_vars warning, then accesses the freed cache. On such a deployment

- [https://github.com/evenomn/CVE-2026-129496](https://github.com/evenomn/CVE-2026-129496) : ![starts](https://img.shields.io/github/stars/evenomn/CVE-2026-129496.svg) ![forks](https://img.shields.io/github/forks/evenomn/CVE-2026-129496.svg)

## CVE-2026-132252
> A vulnerability was found in October CMS up to 4.4.6. This affects the function validateExternalImageHost of the file modules/system/classes/resizeimages/ValidatesExternalImages.php of the component Image Resizer. Performing a manipulation of the argument url results in server-side request forgery. The attack may be initiated remotely. The complexity of an attack is rather high. The exploitability is reported as difficult. The exploit has been made public and could be used. Upgrading to version 

- [https://github.com/capivara-research/CVE-2026-132252](https://github.com/capivara-research/CVE-2026-132252) : ![starts](https://img.shields.io/github/stars/capivara-research/CVE-2026-132252.svg) ![forks](https://img.shields.io/github/forks/capivara-research/CVE-2026-132252.svg)

## CVE-2026-133112
> modified eCommerce Shopsoftware through 3.3.0 contains a cross-site request forgery vulnerability in gv_send.php because the action=process step never validates a CSRF token via check_secure_form(). Attackers can host an auto-submitting form that makes a logged-in customer send their gift voucher balance to an attacker-controlled email address for redemption.

- [https://github.com/capivara-research/CVE-2026-133112](https://github.com/capivara-research/CVE-2026-133112) : ![starts](https://img.shields.io/github/stars/capivara-research/CVE-2026-133112.svg) ![forks](https://img.shields.io/github/forks/capivara-research/CVE-2026-133112.svg)

## CVE-2026-133169
> modified eCommerce Shopsoftware through 3.3.0 contains a stored cross-site scripting vulnerability that allows authenticated administrators to inject scripts via the unsanitized products_model field. Attackers with product editing permission can store JavaScript that executes in browsers of other administrators, storefront visitors, and customers viewing carts and order history.

- [https://github.com/capivara-research/CVE-2026-133169](https://github.com/capivara-research/CVE-2026-133169) : ![starts](https://img.shields.io/github/stars/capivara-research/CVE-2026-133169.svg) ![forks](https://img.shields.io/github/forks/capivara-research/CVE-2026-133169.svg)

## CVE-2026-134732

- [https://github.com/googlesky/CVE-2026-134732](https://github.com/googlesky/CVE-2026-134732) : ![starts](https://img.shields.io/github/stars/googlesky/CVE-2026-134732.svg) ![forks](https://img.shields.io/github/forks/googlesky/CVE-2026-134732.svg)

## CVE-2026-134836

- [https://github.com/googlesky/CVE-2026-134836](https://github.com/googlesky/CVE-2026-134836) : ![starts](https://img.shields.io/github/stars/googlesky/CVE-2026-134836.svg) ![forks](https://img.shields.io/github/forks/googlesky/CVE-2026-134836.svg)

## CVE-2026-134837

- [https://github.com/googlesky/CVE-2026-134837](https://github.com/googlesky/CVE-2026-134837) : ![starts](https://img.shields.io/github/stars/googlesky/CVE-2026-134837.svg) ![forks](https://img.shields.io/github/forks/googlesky/CVE-2026-134837.svg)

## CVE-2026-134838

- [https://github.com/googlesky/CVE-2026-134838](https://github.com/googlesky/CVE-2026-134838) : ![starts](https://img.shields.io/github/stars/googlesky/CVE-2026-134838.svg) ![forks](https://img.shields.io/github/forks/googlesky/CVE-2026-134838.svg)

## CVE-2026-134839

- [https://github.com/googlesky/CVE-2026-134839](https://github.com/googlesky/CVE-2026-134839) : ![starts](https://img.shields.io/github/stars/googlesky/CVE-2026-134839.svg) ![forks](https://img.shields.io/github/forks/googlesky/CVE-2026-134839.svg)

## CVE-2026-134840

- [https://github.com/googlesky/CVE-2026-134840](https://github.com/googlesky/CVE-2026-134840) : ![starts](https://img.shields.io/github/stars/googlesky/CVE-2026-134840.svg) ![forks](https://img.shields.io/github/forks/googlesky/CVE-2026-134840.svg)

## CVE-2026-27119

- [https://github.com/googlesky/CVE-2026-27119](https://github.com/googlesky/CVE-2026-27119) : ![starts](https://img.shields.io/github/stars/googlesky/CVE-2026-27119.svg) ![forks](https://img.shields.io/github/forks/googlesky/CVE-2026-27119.svg)

## CVE-2026-31431
> In the Linux kernel, the following vulnerability has been resolved:

crypto: algif_aead - Revert to operating out-of-place

This mostly reverts commit 72548b093ee3 except for the copying of
the associated data.

There is no benefit in operating in-place in algif_aead since the
source and destination come from different mappings.  Get rid of
all the complexity added for in-place operation and just copy the
AD directly.

- [https://github.com/ssm-shell/copy-fail-ctypes](https://github.com/ssm-shell/copy-fail-ctypes) : ![starts](https://img.shields.io/github/stars/ssm-shell/copy-fail-ctypes.svg) ![forks](https://img.shields.io/github/forks/ssm-shell/copy-fail-ctypes.svg)

## CVE-2026-33203

- [https://github.com/googlesky/CVE-2026-33203](https://github.com/googlesky/CVE-2026-33203) : ![starts](https://img.shields.io/github/stars/googlesky/CVE-2026-33203.svg) ![forks](https://img.shields.io/github/forks/googlesky/CVE-2026-33203.svg)

## CVE-2026-33439

- [https://github.com/RockKingdom/CVE-2026-33439-Python-PoC](https://github.com/RockKingdom/CVE-2026-33439-Python-PoC) : ![starts](https://img.shields.io/github/stars/RockKingdom/CVE-2026-33439-Python-PoC.svg) ![forks](https://img.shields.io/github/forks/RockKingdom/CVE-2026-33439-Python-PoC.svg)
- [https://github.com/RockKingdom/CVE-2026-33439-Python-PoC-main](https://github.com/RockKingdom/CVE-2026-33439-Python-PoC-main) : ![starts](https://img.shields.io/github/stars/RockKingdom/CVE-2026-33439-Python-PoC-main.svg) ![forks](https://img.shields.io/github/forks/RockKingdom/CVE-2026-33439-Python-PoC-main.svg)

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

- [https://github.com/xiaquwan1001/P40pro-ghostlock](https://github.com/xiaquwan1001/P40pro-ghostlock) : ![starts](https://img.shields.io/github/stars/xiaquwan1001/P40pro-ghostlock.svg) ![forks](https://img.shields.io/github/forks/xiaquwan1001/P40pro-ghostlock.svg)

## CVE-2026-45325

- [https://github.com/googlesky/CVE-2026-45325](https://github.com/googlesky/CVE-2026-45325) : ![starts](https://img.shields.io/github/stars/googlesky/CVE-2026-45325.svg) ![forks](https://img.shields.io/github/forks/googlesky/CVE-2026-45325.svg)

## CVE-2026-49952

- [https://github.com/caviar-dynamo/CVE-2026-49952](https://github.com/caviar-dynamo/CVE-2026-49952) : ![starts](https://img.shields.io/github/stars/caviar-dynamo/CVE-2026-49952.svg) ![forks](https://img.shields.io/github/forks/caviar-dynamo/CVE-2026-49952.svg)

## CVE-2026-55621
> Incus is a system container and virtual machine manager. Prior to version 7.2.0, missing authorization checks exist for custom volume copying where an attacker knowing the name of a project that they don&#x27;t have access to and the name of a custom volume in that project can copy the custom volume to a new project. This issue could allow an attacker to access secrets in custom volumes they are not authorized to access. Version 7.2.0 patches the issue.

- [https://github.com/googlesky/CVE-2026-55621](https://github.com/googlesky/CVE-2026-55621) : ![starts](https://img.shields.io/github/stars/googlesky/CVE-2026-55621.svg) ![forks](https://img.shields.io/github/forks/googlesky/CVE-2026-55621.svg)

## CVE-2026-58882
> In decodeWapPdu of WapPushOverSms.java, there is a possible out of bounds read due to an integer overflow. This could lead to a remote denial of service with no additional execution privileges needed. User interaction is not needed for exploitation.

- [https://github.com/warsecurity/-CVE-2026-58882](https://github.com/warsecurity/-CVE-2026-58882) : ![starts](https://img.shields.io/github/stars/warsecurity/-CVE-2026-58882.svg) ![forks](https://img.shields.io/github/forks/warsecurity/-CVE-2026-58882.svg)

## CVE-2026-59988
> django-docutils provides reStructuredText support for Django. Prior to 0.30.0, public rendering paths including publish_doctree, publish_html_from_source, publish_html_from_doctree, publish_parts_from_doctree, the {% rst %} template tag, the rst template filter, DocutilsTemplates, and DocutilsView pass lower-trust reStructuredText to Docutils without disabling file_insertion_enabled, raw_enabled, ambient docutils.conf processing, or unsafe URI schemes and without consistently sanitizing doctrees

- [https://github.com/googlesky/CVE-2026-59988](https://github.com/googlesky/CVE-2026-59988) : ![starts](https://img.shields.io/github/stars/googlesky/CVE-2026-59988.svg) ![forks](https://img.shields.io/github/forks/googlesky/CVE-2026-59988.svg)

## CVE-2026-64638

- [https://github.com/secplayground/CVE-2026-64638-scanner-and-exploit](https://github.com/secplayground/CVE-2026-64638-scanner-and-exploit) : ![starts](https://img.shields.io/github/stars/secplayground/CVE-2026-64638-scanner-and-exploit.svg) ![forks](https://img.shields.io/github/forks/secplayground/CVE-2026-64638-scanner-and-exploit.svg)

## CVE-2026-68387

- [https://github.com/cybuildguild/CVE-2026-68387](https://github.com/cybuildguild/CVE-2026-68387) : ![starts](https://img.shields.io/github/stars/cybuildguild/CVE-2026-68387.svg) ![forks](https://img.shields.io/github/forks/cybuildguild/CVE-2026-68387.svg)

## CVE-2026-77309

- [https://github.com/googlesky/CVE-2026-77309](https://github.com/googlesky/CVE-2026-77309) : ![starts](https://img.shields.io/github/stars/googlesky/CVE-2026-77309.svg) ![forks](https://img.shields.io/github/forks/googlesky/CVE-2026-77309.svg)

## CVE-2026-77312

- [https://github.com/googlesky/CVE-2026-77312](https://github.com/googlesky/CVE-2026-77312) : ![starts](https://img.shields.io/github/stars/googlesky/CVE-2026-77312.svg) ![forks](https://img.shields.io/github/forks/googlesky/CVE-2026-77312.svg)

## CVE-2026-77367
> Daptin is a GraphQL/JSON-API headless CMS. Prior to 0.12.30, the generic GET /api/{entity} list endpoint accepts attacker-controlled sort values in PaginatedFindAllWithoutFilters in server/resource/resource_findallpaginated.go without validating the requested column against the table schema. The code uses those values for SELECT and ORDER BY identifier construction, so an embedded identifier quote can terminate the quoted identifier and make the remainder parse as SQL, allowing an unauthenticate

- [https://github.com/googlesky/CVE-2026-77367](https://github.com/googlesky/CVE-2026-77367) : ![starts](https://img.shields.io/github/stars/googlesky/CVE-2026-77367.svg) ![forks](https://img.shields.io/github/forks/googlesky/CVE-2026-77367.svg)

## CVE-2026-77369
> Daptin is a GraphQL/JSON-API headless CMS. From 0.11.4 until 0.12.30, the generic GET /yjs/:documentName WebSocket route in InitializeYjsResources requires a session but does not authorize the database resource selected by a typename.referenceId.columnName room name. The YJS initial-content provider then reads the selected file.* column without CanRead or CanUpdate checks, and bidirectional synchronization allows a low-privileged authenticated user to read or modify restricted row content. Unaut

- [https://github.com/googlesky/CVE-2026-77369](https://github.com/googlesky/CVE-2026-77369) : ![starts](https://img.shields.io/github/stars/googlesky/CVE-2026-77369.svg) ![forks](https://img.shields.io/github/forks/googlesky/CVE-2026-77369.svg)

## CVE-2026-77376
> Bolt is a fully open source, adaptable platform for building and running modern websites. Prior to 6.1.4, LoginFormAuthenticator accepts unsafe destinations for the login success redirect and login failure redirect. An attacker can direct a user to an attacker-controlled domain after authentication succeeds or fails, enabling phishing and potential token theft. This issue is fixed in version 6.1.4.

- [https://github.com/googlesky/CVE-2026-77376](https://github.com/googlesky/CVE-2026-77376) : ![starts](https://img.shields.io/github/stars/googlesky/CVE-2026-77376.svg) ![forks](https://img.shields.io/github/forks/googlesky/CVE-2026-77376.svg)

## CVE-2026-77377
> Bolt is a fully open source, adaptable platform for building and running modern websites. Prior to 6.1.4, the authenticated URL-upload endpoint and authenticated embed endpoint fetch user-supplied URLs server-side without protection against internal targets, allowing an attacker with the applicable backend permission to cause the Bolt server to request those targets. This issue is fixed in version 6.1.4.

- [https://github.com/googlesky/CVE-2026-77377](https://github.com/googlesky/CVE-2026-77377) : ![starts](https://img.shields.io/github/stars/googlesky/CVE-2026-77377.svg) ![forks](https://img.shields.io/github/forks/googlesky/CVE-2026-77377.svg)

## CVE-2026-77379
> Bolt is a fully open source, adaptable platform for building and running modern websites. Prior to 6.1.4, the public Relation API lacks an access-control filter. Unauthenticated users can query its REST endpoints and GraphQL endpoints to discover metadata about unpublished, draft, and viewless content. This issue is fixed in version 6.1.4.

- [https://github.com/googlesky/CVE-2026-77379](https://github.com/googlesky/CVE-2026-77379) : ![starts](https://img.shields.io/github/stars/googlesky/CVE-2026-77379.svg) ![forks](https://img.shields.io/github/forks/googlesky/CVE-2026-77379.svg)

## CVE-2026-77380
> Bolt is a fully open source, adaptable platform for building and running modern websites. Prior to 6.1.5, the /bolt/async/upload-url and /bolt/async/embed endpoints validate only a submitted URL before fetching it server-side. The fetchers then follow redirects without revalidating each destination, allowing an authenticated user to bypass UrlSafetyChecker and cause the server to request internal or cloud-metadata addresses. This issue is fixed in version 6.1.5.

- [https://github.com/googlesky/CVE-2026-77380](https://github.com/googlesky/CVE-2026-77380) : ![starts](https://img.shields.io/github/stars/googlesky/CVE-2026-77380.svg) ![forks](https://img.shields.io/github/forks/googlesky/CVE-2026-77380.svg)

## CVE-2026-77382
> falcon-rust is a Rust implementation of the Falcon post-quantum signature scheme. Prior to 0.2.0, the discrete-Gaussian sampler in src/samplerz.rs evaluates approx_exp, ber_exp, and sampler_z acceptance probabilities with FixedPoint64 values having only 32 fractional bits. The scaling in approx_exp quantizes its input and limits relative precision to about 2^-33, below Falcon&#x27;s required bound, causing reference known-answer vectors to diverge and invalidating the proof assumption that secret-dep

- [https://github.com/googlesky/CVE-2026-77382](https://github.com/googlesky/CVE-2026-77382) : ![starts](https://img.shields.io/github/stars/googlesky/CVE-2026-77382.svg) ![forks](https://img.shields.io/github/forks/googlesky/CVE-2026-77382.svg)

## CVE-2026-83816
> CodeWhale is a DeepSeek and MiMo coding agent for the terminal. Prior to 0.9.0, the ExecShellTool::approval_requirement_for path used is_parallel_readonly_command to downgrade commands to automatic approval based on a flag-stripped command allowlist. The allowlist treated fd, rg, and git grep as read-only even when fd -x or fd --exec, rg --pre, or git grep --open-files-in-pager selected an external program. registered_tool_approval_required returned without displaying a prompt for that automatic

- [https://github.com/googlesky/CVE-2026-83816](https://github.com/googlesky/CVE-2026-83816) : ![starts](https://img.shields.io/github/stars/googlesky/CVE-2026-83816.svg) ![forks](https://img.shields.io/github/forks/googlesky/CVE-2026-83816.svg)

## CVE-2026-83817
> CodeWhale is a DeepSeek and MiMo coding agent for the terminal. Prior to 0.9.0, DEFAULT_AUTOMATION_AUTO_APPROVE caused AutomationRecord::task_auto_approve to resolve an omitted setting to true, and the automation_create schema advertised the same insecure default. enqueue_run_task converted that omission into an explicit true value, bypassing the safer task-path fallback and selecting ApprovalMode::Bypass for each scheduled run. After a user approved creation of an apparently benign recurring au

- [https://github.com/googlesky/CVE-2026-83817](https://github.com/googlesky/CVE-2026-83817) : ![starts](https://img.shields.io/github/stars/googlesky/CVE-2026-83817.svg) ![forks](https://img.shields.io/github/forks/googlesky/CVE-2026-83817.svg)

## CVE-2026-95839
> containerd is an open-source container runtime. From 2.2.0 until 2.2.10, 2.3.7, and 2.4.2, image manifest processing through the transfer service can encounter a child descriptor containing the io.containerd.manifest.subject annotation and a malformed digest. Pulling or importing such an image, including through a default CRI PullImage request, can trigger an unrecovered panic and crash the containerd daemon. In Kubernetes, kubelet retries can repeatedly trigger the crash and disrupt container o

- [https://github.com/googlesky/CVE-2026-95839](https://github.com/googlesky/CVE-2026-95839) : ![starts](https://img.shields.io/github/stars/googlesky/CVE-2026-95839.svg) ![forks](https://img.shields.io/github/forks/googlesky/CVE-2026-95839.svg)
