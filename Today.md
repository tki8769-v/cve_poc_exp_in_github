# Update 2026-11-09
## CVE-2012-0694

- [https://github.com/marinovharisan/CVE-2012-0694-SugarCRM-PoC](https://github.com/marinovharisan/CVE-2012-0694-SugarCRM-PoC) : ![starts](https://img.shields.io/github/stars/marinovharisan/CVE-2012-0694-SugarCRM-PoC.svg) ![forks](https://img.shields.io/github/forks/marinovharisan/CVE-2012-0694-SugarCRM-PoC.svg)

## CVE-2015-7547

- [https://github.com/federiconbaez/cortex9-glibc-getaddrinfo-dual-buffer-state-model](https://github.com/federiconbaez/cortex9-glibc-getaddrinfo-dual-buffer-state-model) : ![starts](https://img.shields.io/github/stars/federiconbaez/cortex9-glibc-getaddrinfo-dual-buffer-state-model.svg) ![forks](https://img.shields.io/github/forks/federiconbaez/cortex9-glibc-getaddrinfo-dual-buffer-state-model.svg)

## CVE-2016-1834

- [https://github.com/federiconbaez/cortex9-libxml2-strncat-length-wrap-model](https://github.com/federiconbaez/cortex9-libxml2-strncat-length-wrap-model) : ![starts](https://img.shields.io/github/stars/federiconbaez/cortex9-libxml2-strncat-length-wrap-model.svg) ![forks](https://img.shields.io/github/forks/federiconbaez/cortex9-libxml2-strncat-length-wrap-model.svg)

## CVE-2020-8927

- [https://github.com/federiconbaez/cortex9-brotli-uncompressed-copy-narrowing-model](https://github.com/federiconbaez/cortex9-brotli-uncompressed-copy-narrowing-model) : ![starts](https://img.shields.io/github/stars/federiconbaez/cortex9-brotli-uncompressed-copy-narrowing-model.svg) ![forks](https://img.shields.io/github/forks/federiconbaez/cortex9-brotli-uncompressed-copy-narrowing-model.svg)

## CVE-2021-3711
> In order to decrypt SM2 encrypted data an application is expected to call the API function EVP_PKEY_decrypt(). Typically an application will call this function twice. The first time, on entry, the &quot;out&quot; parameter can be NULL and, on exit, the &quot;outlen&quot; parameter is populated with the buffer size required to hold the decrypted plaintext. The application can then allocate a sufficiently sized buffer and call EVP_PKEY_decrypt() again, but this time passing a non-NULL value for the &quot;out&quot; parameter. A

- [https://github.com/federiconbaez/cortex9-openssl-sm2-plaintext-size-model](https://github.com/federiconbaez/cortex9-openssl-sm2-plaintext-size-model) : ![starts](https://img.shields.io/github/stars/federiconbaez/cortex9-openssl-sm2-plaintext-size-model.svg) ![forks](https://img.shields.io/github/forks/federiconbaez/cortex9-openssl-sm2-plaintext-size-model.svg)

## CVE-2021-40444

- [https://github.com/m4madturk/CVE-2021-40444](https://github.com/m4madturk/CVE-2021-40444) : ![starts](https://img.shields.io/github/stars/m4madturk/CVE-2021-40444.svg) ![forks](https://img.shields.io/github/forks/m4madturk/CVE-2021-40444.svg)

## CVE-2021-41773

- [https://github.com/R3leant/CVE-2021-41773](https://github.com/R3leant/CVE-2021-41773) : ![starts](https://img.shields.io/github/stars/R3leant/CVE-2021-41773.svg) ![forks](https://img.shields.io/github/forks/R3leant/CVE-2021-41773.svg)

## CVE-2021-44228

- [https://github.com/sejauhkayuh/Vulnerable-and-Outdated-Components-Insiden-Log4Shell-CVE-2021-44228-](https://github.com/sejauhkayuh/Vulnerable-and-Outdated-Components-Insiden-Log4Shell-CVE-2021-44228-) : ![starts](https://img.shields.io/github/stars/sejauhkayuh/Vulnerable-and-Outdated-Components-Insiden-Log4Shell-CVE-2021-44228-.svg) ![forks](https://img.shields.io/github/forks/sejauhkayuh/Vulnerable-and-Outdated-Components-Insiden-Log4Shell-CVE-2021-44228-.svg)

## CVE-2023-0286
> There is a type confusion vulnerability relating to X.400 address processing
inside an X.509 GeneralName. X.400 addresses were parsed as an ASN1_STRING but
the public structure definition for GENERAL_NAME incorrectly specified the type
of the x400Address field as ASN1_TYPE. This field is subsequently interpreted by
the OpenSSL function GENERAL_NAME_cmp as an ASN1_TYPE rather than an
ASN1_STRING.

When CRL checking is enabled (i.e. the application sets the
X509_V_FLAG_CRL_CHECK flag), this vulner

- [https://github.com/federiconbaez/cortex9-openssl-x400-generalname-type-confusion-model](https://github.com/federiconbaez/cortex9-openssl-x400-generalname-type-confusion-model) : ![starts](https://img.shields.io/github/stars/federiconbaez/cortex9-openssl-x400-generalname-type-confusion-model.svg) ![forks](https://img.shields.io/github/forks/federiconbaez/cortex9-openssl-x400-generalname-type-confusion-model.svg)

## CVE-2023-33107

- [https://github.com/markutell/CVE-2023-33107-SO51A](https://github.com/markutell/CVE-2023-33107-SO51A) : ![starts](https://img.shields.io/github/stars/markutell/CVE-2023-33107-SO51A.svg) ![forks](https://img.shields.io/github/forks/markutell/CVE-2023-33107-SO51A.svg)

## CVE-2023-36845

- [https://github.com/cxb2523/ccfb-pointwise-20261109-010-cve-2023-36845-scanner](https://github.com/cxb2523/ccfb-pointwise-20261109-010-cve-2023-36845-scanner) : ![starts](https://img.shields.io/github/stars/cxb2523/ccfb-pointwise-20261109-010-cve-2023-36845-scanner.svg) ![forks](https://img.shields.io/github/forks/cxb2523/ccfb-pointwise-20261109-010-cve-2023-36845-scanner.svg)

## CVE-2023-4863

- [https://github.com/federiconbaez/cortex9-libwebp-huffman-table-sizing-model](https://github.com/federiconbaez/cortex9-libwebp-huffman-table-sizing-model) : ![starts](https://img.shields.io/github/stars/federiconbaez/cortex9-libwebp-huffman-table-sizing-model.svg) ![forks](https://img.shields.io/github/forks/federiconbaez/cortex9-libwebp-huffman-table-sizing-model.svg)

## CVE-2024-38063

- [https://github.com/omarbabba779xx/ethical-hacking-tp5-vulnerability-analysis-nmap-nse](https://github.com/omarbabba779xx/ethical-hacking-tp5-vulnerability-analysis-nmap-nse) : ![starts](https://img.shields.io/github/stars/omarbabba779xx/ethical-hacking-tp5-vulnerability-analysis-nmap-nse.svg) ![forks](https://img.shields.io/github/forks/omarbabba779xx/ethical-hacking-tp5-vulnerability-analysis-nmap-nse.svg)

## CVE-2024-44068

- [https://github.com/privacyportalUK/PP-Root](https://github.com/privacyportalUK/PP-Root) : ![starts](https://img.shields.io/github/stars/privacyportalUK/PP-Root.svg) ![forks](https://img.shields.io/github/forks/privacyportalUK/PP-Root.svg)

## CVE-2025-31161

- [https://github.com/ashrafzaryouh/CVE-2025-31161](https://github.com/ashrafzaryouh/CVE-2025-31161) : ![starts](https://img.shields.io/github/stars/ashrafzaryouh/CVE-2025-31161.svg) ![forks](https://img.shields.io/github/forks/ashrafzaryouh/CVE-2025-31161.svg)

## CVE-2025-48583

- [https://github.com/helloguy1234/CVE-2025-48583-PoC](https://github.com/helloguy1234/CVE-2025-48583-PoC) : ![starts](https://img.shields.io/github/stars/helloguy1234/CVE-2025-48583-PoC.svg) ![forks](https://img.shields.io/github/forks/helloguy1234/CVE-2025-48583-PoC.svg)

## CVE-2026-102268
> PyJWT is a Python implementation of JSON Web Token standards. Prior to 2.14.0, is_pem_format in jwt/utils.py is affected because is_pem_format does not recognize every PEM representation accepted by the cryptography loader. This occurs when an application mixes HMAC and asymmetric algorithms and supplies a mutated public-key PEM as raw key bytes. As a result, HMACAlgorithm.prepare_key treats the unrecognized asymmetric public key as an HMAC secret. Consequently, an attacker who knows the public 

- [https://github.com/federiconbaez/cortex9-pyjwt-pem-detection-alg-confusion-model](https://github.com/federiconbaez/cortex9-pyjwt-pem-detection-alg-confusion-model) : ![starts](https://img.shields.io/github/stars/federiconbaez/cortex9-pyjwt-pem-detection-alg-confusion-model.svg) ![forks](https://img.shields.io/github/forks/federiconbaez/cortex9-pyjwt-pem-detection-alg-confusion-model.svg)

## CVE-2026-102422
> shell-quote&#x27;s `quote()` function emits a `{ comment }` token as `#` followed by its text, which comments out the rest of the shell line, including the opening quote of any later string token. A line terminator (\n, \r, U+2028, U+2029) in that later string therefore ends the comment, and the rest of the string is parsed as shell input: `quote([&#x27;echo&#x27;, &#x27;ok&#x27;, { comment: &#x27;x&#x27; }, &#x27;a\nid;#&#x27;])` runs `id` in sh, bash, dash, ksh and zsh. `parse()` emits a comment token for a `#` in the middle of a word (f

- [https://github.com/federiconbaez/cortex9-shell-quote-comment-line-terminator-model](https://github.com/federiconbaez/cortex9-shell-quote-comment-line-terminator-model) : ![starts](https://img.shields.io/github/stars/federiconbaez/cortex9-shell-quote-comment-line-terminator-model.svg) ![forks](https://img.shields.io/github/forks/federiconbaez/cortex9-shell-quote-comment-line-terminator-model.svg)

## CVE-2026-104851
> fsspec is a specification and Python implementation framework for filesystem interfaces. From 0.9.0 until 2026.6.0, fsspec.implementations.reference.ReferenceFileSystem evaluates fields from Kerchunk reference JSON documents through unrestricted jinja2.Template(...).render(...) calls in _process_references1._render_jinja, _process_templates, and _process_gen in fsspec/implementations/reference.py. A document supplied inline or fetched from an attacker-controlled URL can provide template expressi

- [https://github.com/federiconbaez/cortex9-fsspec-reference-jinja-ssti-model](https://github.com/federiconbaez/cortex9-fsspec-reference-jinja-ssti-model) : ![starts](https://img.shields.io/github/stars/federiconbaez/cortex9-fsspec-reference-jinja-ssti-model.svg) ![forks](https://img.shields.io/github/forks/federiconbaez/cortex9-fsspec-reference-jinja-ssti-model.svg)

## CVE-2026-106451
> yawkat LZ4 Java provides LZ4 compression for Java. From 1.7.0 until 1.11.4, net.jpountz.util.Native.load() uses File.createTempFile to create an exclusive temporary .lck file but derives the native-library path by removing the suffix, then FileOutputStream opens that predictable path without exclusive creation, allowing another local user with access to the same shared temporary directory to create or replace the library file before System.load() uses it. Successful exploitation depends on share

- [https://github.com/federiconbaez/cortex9-lz4java-tmp-native-lib-predictable-name-model](https://github.com/federiconbaez/cortex9-lz4java-tmp-native-lib-predictable-name-model) : ![starts](https://img.shields.io/github/stars/federiconbaez/cortex9-lz4java-tmp-native-lib-predictable-name-model.svg) ![forks](https://img.shields.io/github/forks/federiconbaez/cortex9-lz4java-tmp-native-lib-predictable-name-model.svg)

## CVE-2026-107720
> fast-jwt provides fast JSON Web Token (JWT) implementation. Prior to 6.3.1, fast-jwt createVerifier accepts an unsigned JWT when key is an empty string or null and algorithms is a non-empty allowlist. Falsy synchronous keys bypass prepareKeyOrSecret, allowedAlgorithms remains active, hasKey is false, and the empty signature avoids the verifySignature gate. An attacker can therefore submit a token containing arbitrary claims without possessing a signing key, resulting in authentication or authori

- [https://github.com/federiconbaez/cortex9-fastjwt-empty-key-unsigned-accept-model](https://github.com/federiconbaez/cortex9-fastjwt-empty-key-unsigned-accept-model) : ![starts](https://img.shields.io/github/stars/federiconbaez/cortex9-fastjwt-empty-key-unsigned-accept-model.svg) ![forks](https://img.shields.io/github/forks/federiconbaez/cortex9-fastjwt-empty-key-unsigned-accept-model.svg)

## CVE-2026-108360
> PhpSpreadsheet is a pure PHP library for reading and writing spreadsheet files. Prior to 1.30.7, 2.1.19, 2.4.8, 3.10.8, and 5.10.0, Worksheet\Drawing::setPath validates only the initial external-image URL with setIsWhitelisted when setAllowExternalImages is enabled. The HTTP stream context permits PHP to follow a redirect without applying the callback to the redirected URL, so a permitted image host can redirect the server to an internal address and cause a blind GET request. The response body i

- [https://github.com/federiconbaez/cortex9-phpspreadsheet-redirect-whitelist-ssrf-model](https://github.com/federiconbaez/cortex9-phpspreadsheet-redirect-whitelist-ssrf-model) : ![starts](https://img.shields.io/github/stars/federiconbaez/cortex9-phpspreadsheet-redirect-whitelist-ssrf-model.svg) ![forks](https://img.shields.io/github/forks/federiconbaez/cortex9-phpspreadsheet-redirect-whitelist-ssrf-model.svg)

## CVE-2026-109372
> ZITADEL 4.x before 4.19.2 and 3.x through 3.4.15 contains an authentication bypass in the SAML identity-provider intent callback, which verifies the assertion signature using the provider named in the request URL but resolves the user from the login intent without checking they match. Attackers with organization-administrator permission can register a SAML provider with their own signing key to obtain authenticated sessions as any user linked to another SAML provider on the instance, including i

- [https://github.com/federiconbaez/cortex9-zitadel-saml-idp-intent-mismatch-model](https://github.com/federiconbaez/cortex9-zitadel-saml-idp-intent-mismatch-model) : ![starts](https://img.shields.io/github/stars/federiconbaez/cortex9-zitadel-saml-idp-intent-mismatch-model.svg) ![forks](https://img.shields.io/github/forks/federiconbaez/cortex9-zitadel-saml-idp-intent-mismatch-model.svg)

## CVE-2026-109618
> PHP uses longjmp() for out-of-memory (OOM) errors to exit the current context and abort handling of the request. Some contexts may not properly account for this scenario and leave request memory in an uninitialized state before performing an allocation. The subsequent request cleanup procedure may read or branch on this memory. Multiple OOM strategies can consistently trigger this condition and lead to remote code execution (RCE).

- [https://github.com/Ghxstsec/PHP2SHELL-POC](https://github.com/Ghxstsec/PHP2SHELL-POC) : ![starts](https://img.shields.io/github/stars/Ghxstsec/PHP2SHELL-POC.svg) ![forks](https://img.shields.io/github/forks/Ghxstsec/PHP2SHELL-POC.svg)
- [https://github.com/Ya0h4cker/CVE-2026-109618-and-CVE-2026-109619](https://github.com/Ya0h4cker/CVE-2026-109618-and-CVE-2026-109619) : ![starts](https://img.shields.io/github/stars/Ya0h4cker/CVE-2026-109618-and-CVE-2026-109619.svg) ![forks](https://img.shields.io/github/forks/Ya0h4cker/CVE-2026-109618-and-CVE-2026-109619.svg)
- [https://github.com/ashrafzaryouh/CVE-2026-109618](https://github.com/ashrafzaryouh/CVE-2026-109618) : ![starts](https://img.shields.io/github/stars/ashrafzaryouh/CVE-2026-109618.svg) ![forks](https://img.shields.io/github/forks/ashrafzaryouh/CVE-2026-109618.svg)
- [https://github.com/hosun-hwang/CVE-2026-109618-CVE-2026-109619_PoC](https://github.com/hosun-hwang/CVE-2026-109618-CVE-2026-109619_PoC) : ![starts](https://img.shields.io/github/stars/hosun-hwang/CVE-2026-109618-CVE-2026-109619_PoC.svg) ![forks](https://img.shields.io/github/forks/hosun-hwang/CVE-2026-109618-CVE-2026-109619_PoC.svg)

## CVE-2026-109619
> PHP has various global state that temporarily points into request memory. In some scenarios, global state may not be correctly reset, or may be repopulated after being reset. The global state may then refer to request memory even after it has been freed. Subsequent requests may read or branch on this stale state before it is fully initialized. Multiple strategies can trigger this condition and produce remote code execution (RCE).

- [https://github.com/Ya0h4cker/CVE-2026-109618-and-CVE-2026-109619](https://github.com/Ya0h4cker/CVE-2026-109618-and-CVE-2026-109619) : ![starts](https://img.shields.io/github/stars/Ya0h4cker/CVE-2026-109618-and-CVE-2026-109619.svg) ![forks](https://img.shields.io/github/forks/Ya0h4cker/CVE-2026-109618-and-CVE-2026-109619.svg)
- [https://github.com/che3axujnya/cve-2026-109618-cve-2026-109619-poc](https://github.com/che3axujnya/cve-2026-109618-cve-2026-109619-poc) : ![starts](https://img.shields.io/github/stars/che3axujnya/cve-2026-109618-cve-2026-109619-poc.svg) ![forks](https://img.shields.io/github/forks/che3axujnya/cve-2026-109618-cve-2026-109619-poc.svg)
- [https://github.com/hosun-hwang/CVE-2026-109618-CVE-2026-109619_PoC](https://github.com/hosun-hwang/CVE-2026-109618-CVE-2026-109619_PoC) : ![starts](https://img.shields.io/github/stars/hosun-hwang/CVE-2026-109618-CVE-2026-109619_PoC.svg) ![forks](https://img.shields.io/github/forks/hosun-hwang/CVE-2026-109618-CVE-2026-109619_PoC.svg)

## CVE-2026-110634
> git-diff before 2.0.7 contains an OS command injection vulnerability that allows attackers to execute shell commands by supplying crafted strings to the gitDiff API. Attackers who control a diffed document string can embed $(cmd) or backtick substitutions that shelljs.exec evaluates, running commands with Node.js process privileges.

- [https://github.com/federiconbaez/cortex9-git-diff-shell-hash-object-injection-model](https://github.com/federiconbaez/cortex9-git-diff-shell-hash-object-injection-model) : ![starts](https://img.shields.io/github/stars/federiconbaez/cortex9-git-diff-shell-hash-object-injection-model.svg) ![forks](https://img.shields.io/github/forks/federiconbaez/cortex9-git-diff-shell-hash-object-injection-model.svg)

## CVE-2026-111497
> A buffer overflow vulnerability in the Brotli decoder (c/dec/decode.c) in Google Brotli versions 1.0.3 through 1.2.0 on all platforms allows a remote unauthenticated attacker to corrupt adjacent decoder state memory, disclose sensitive memory contents, cause a denial of service, or potentially execute arbitrary code using a crafted Brotli-compressed stream.





Users need to update any Brotli libraries or binaries between 1.0.3 through 1.2.0 to the latest available version: 1.0.10 or 1.1.1 or 1

- [https://github.com/hosun-hwang/CVE-2026-111497_PoC](https://github.com/hosun-hwang/CVE-2026-111497_PoC) : ![starts](https://img.shields.io/github/stars/hosun-hwang/CVE-2026-111497_PoC.svg) ![forks](https://img.shields.io/github/forks/hosun-hwang/CVE-2026-111497_PoC.svg)

## CVE-2026-112900
> Pillow is a Python imaging library. From 2.6.0 until 13.0.0, Pillow is vulnerable to argument injection when invoking Ghostscript for EPS input. EpsImagePlugin.Ghostscript passes a caller-controlled input filename after -f without converting it to a safe absolute path, so a name beginning with a hyphen can be interpreted as a Ghostscript option. An attacker who controls the filename can inject Ghostscript arguments. Arbitrary command execution specifically requires a leading @ argument-file file

- [https://github.com/federiconbaez/cortex9-pillow-ghostscript-argv-injection-model](https://github.com/federiconbaez/cortex9-pillow-ghostscript-argv-injection-model) : ![starts](https://img.shields.io/github/stars/federiconbaez/cortex9-pillow-ghostscript-argv-injection-model.svg) ![forks](https://img.shields.io/github/forks/federiconbaez/cortex9-pillow-ghostscript-argv-injection-model.svg)

## CVE-2026-112936
> filelock is a platform-independent file lock for Python. From 3.20.4 until 4.0.9, ReadWriteLock and AsyncReadWriteLock versions from 3.20.4 resolve the lock path and pass it to SQLite without rejecting a final symbolic link, allowing another local user who can create names in the lock directory to redirect database creation and locking or split mutual exclusion between targets. This issue is fixed in version 4.0.9.

- [https://github.com/federiconbaez/cortex9-filelock-sqlite-symlink-follow-model](https://github.com/federiconbaez/cortex9-filelock-sqlite-symlink-follow-model) : ![starts](https://img.shields.io/github/stars/federiconbaez/cortex9-filelock-sqlite-symlink-follow-model.svg) ![forks](https://img.shields.io/github/forks/federiconbaez/cortex9-filelock-sqlite-symlink-follow-model.svg)

## CVE-2026-113386
> Roundcube Webmail before 1.6.20 and 1.7.x before 1.7.5 are affected by IMAP command injection. A remote authenticated attacker can exploit this via CRLF sequences injected into the _uid parameter of the mail/headers and mail/viewsource actions to execute arbitrary IMAP commands.

- [https://github.com/Neo-XeD/CVE-2026-113386](https://github.com/Neo-XeD/CVE-2026-113386) : ![starts](https://img.shields.io/github/stars/Neo-XeD/CVE-2026-113386.svg) ![forks](https://img.shields.io/github/forks/Neo-XeD/CVE-2026-113386.svg)

## CVE-2026-114140
> The nbconvert tool, jupyter nbconvert, converts Jupyter notebooks to various other formats via Jinja templates. From 5.4.0 until 7.17.2, ExtractOutputPreprocessor in nbconvert/preprocessors/extractoutput.py joins the attacker-controlled cell output metadata filename to output_files_dir without limiting the result to the intended directory. When a victim converts a malicious notebook with the markdown, LaTeX, reStructuredText, or AsciiDoc exporter, path traversal in the output filename can write 

- [https://github.com/federiconbaez/cortex9-nbconvert-output-filename-traversal-model](https://github.com/federiconbaez/cortex9-nbconvert-output-filename-traversal-model) : ![starts](https://img.shields.io/github/stars/federiconbaez/cortex9-nbconvert-output-filename-traversal-model.svg) ![forks](https://img.shields.io/github/forks/federiconbaez/cortex9-nbconvert-output-filename-traversal-model.svg)

## CVE-2026-11499
> A vulnerability was determined in Tenda HG7, HG9 and HG10 300001138_en_xpon. This affects the function formDOMAINBLK of the file /boaform/formDOMAINBLK. Executing a manipulation of the argument blkDomain can lead to stack-based buffer overflow. The attack may be performed from remote.

- [https://github.com/ashrafzaryouh/CVE-2026-11499](https://github.com/ashrafzaryouh/CVE-2026-11499) : ![starts](https://img.shields.io/github/stars/ashrafzaryouh/CVE-2026-11499.svg) ![forks](https://img.shields.io/github/forks/ashrafzaryouh/CVE-2026-11499.svg)

## CVE-2026-115878
> Stanza is a Stanford NLP Python library for tokenization, sentence segmentation, NER, and parsing of many human languages. From 1.14.0 until 1.15.0, loading an attacker-supplied lemmatizer checkpoint can execute arbitrary code because stanza/models/lemma/trainer.py stores pos_dict as gzip-compressed pickle bytes and Trainer.load passes the decompressed stream to unrestricted pickle.loads. The outer torch.load call uses weights_only=True, but the nested bytes are treated as a primitive and are no

- [https://github.com/federiconbaez/cortex9-stanza-lemma-pickle-to-json-model](https://github.com/federiconbaez/cortex9-stanza-lemma-pickle-to-json-model) : ![starts](https://img.shields.io/github/stars/federiconbaez/cortex9-stanza-lemma-pickle-to-json-model.svg) ![forks](https://img.shields.io/github/forks/federiconbaez/cortex9-stanza-lemma-pickle-to-json-model.svg)

## CVE-2026-116567
> FreeSWITCH is a Software Defined Telecom Stack enabling the digital transformation from proprietary telecom switches to a software implementation that runs on any commodity hardware. Prior to 1.11.2, rtmp_handle_control() rendered an RTMP user-control message into a 200-byte stack buffer using an unbounded sprintf loop controlled by the wire message length. A body of roughly 70 bytes or more overflowed the stack before any RTMP login, because the handshake authenticates neither side. The flaw af

- [https://github.com/carterlasalle/CVE-2026-116567](https://github.com/carterlasalle/CVE-2026-116567) : ![starts](https://img.shields.io/github/stars/carterlasalle/CVE-2026-116567.svg) ![forks](https://img.shields.io/github/forks/carterlasalle/CVE-2026-116567.svg)

## CVE-2026-116580
> Seroval facilitates JavaScript value stringification, including complex structures beyond JSON.stringify capabilities. Prior to 1.6.8, fromJSON rebuilds an AsyncIteratorFactoryInstance by calling source.on(listener) without requiring source to be a genuine internal stream. With untrusted Seroval input and an application plugin that returns a callable value or an object exposing an on method, a crafted node can reuse an identifier so the deserializer invokes the plugin-produced value. This is an 

- [https://github.com/federiconbaez/cortex9-seroval-node-id-type-confusion-model](https://github.com/federiconbaez/cortex9-seroval-node-id-type-confusion-model) : ![starts](https://img.shields.io/github/stars/federiconbaez/cortex9-seroval-node-id-type-confusion-model.svg) ![forks](https://img.shields.io/github/forks/federiconbaez/cortex9-seroval-node-id-type-confusion-model.svg)

## CVE-2026-117083

- [https://github.com/gabrielunknown/intelbras_1200_bypass](https://github.com/gabrielunknown/intelbras_1200_bypass) : ![starts](https://img.shields.io/github/stars/gabrielunknown/intelbras_1200_bypass.svg) ![forks](https://img.shields.io/github/forks/gabrielunknown/intelbras_1200_bypass.svg)

## CVE-2026-11800

- [https://github.com/federiconbaez/cortex9-keycloak-jwt-grant-alg-confusion-model](https://github.com/federiconbaez/cortex9-keycloak-jwt-grant-alg-confusion-model) : ![starts](https://img.shields.io/github/stars/federiconbaez/cortex9-keycloak-jwt-grant-alg-confusion-model.svg) ![forks](https://img.shields.io/github/forks/federiconbaez/cortex9-keycloak-jwt-grant-alg-confusion-model.svg)

## CVE-2026-118378
> Tabularis before 0.28.0 contains an SQL injection vulnerability in its SQLite driver that allows MCP clients to execute stacked statements by supplying a crafted table_name to the describe_table tool. Attackers, including AI agents steered by untrusted content, can close the quoted PRAGMA argument and append statements to read, modify, or drop SQLite data, bypassing read-only mode and write approval.

- [https://github.com/squeeze440/CVE-2026-118378-tabularis-PoC](https://github.com/squeeze440/CVE-2026-118378-tabularis-PoC) : ![starts](https://img.shields.io/github/stars/squeeze440/CVE-2026-118378-tabularis-PoC.svg) ![forks](https://img.shields.io/github/forks/squeeze440/CVE-2026-118378-tabularis-PoC.svg)

## CVE-2026-118650
> Echo is a Go web framework. Prior to 4.16.0 and 5.4.0, a globally mounted middleware.Static instance can interpret an encoded request path differently from Echo&#x27;s router because the router matches the still-encoded path while the static handler uses the decoded URL.Path. The advisory demonstrates an encoded slash resolving to a file under the static root through the global static middleware, but the source is internally inconsistent about whether a route or group guard protects the corresponding

- [https://github.com/federiconbaez/cortex9-echo-static-encoded-segment-bypass-model](https://github.com/federiconbaez/cortex9-echo-static-encoded-segment-bypass-model) : ![starts](https://img.shields.io/github/stars/federiconbaez/cortex9-echo-static-encoded-segment-bypass-model.svg) ![forks](https://img.shields.io/github/forks/federiconbaez/cortex9-echo-static-encoded-segment-bypass-model.svg)

## CVE-2026-118669
> OAuthLib is an implementation of the OAuth request-signing logic for Python 3.6+. Prior to 4.0.0, the client_credentials and Resource Owner Password Credentials token grant handlers can authenticate request.client as one confidential client while retaining an attacker-supplied request.client_id for validate_grant_type and validate_scopes. A lower-privilege authenticated client can therefore cause grant and scope authorization to use another client&#x27;s identity when an application validator relies 

- [https://github.com/federiconbaez/cortex9-oauthlib-token-grant-client-id-confusion-model](https://github.com/federiconbaez/cortex9-oauthlib-token-grant-client-id-confusion-model) : ![starts](https://img.shields.io/github/stars/federiconbaez/cortex9-oauthlib-token-grant-client-id-confusion-model.svg) ![forks](https://img.shields.io/github/forks/federiconbaez/cortex9-oauthlib-token-grant-client-id-confusion-model.svg)

## CVE-2026-119200
> Nuxt is an open-source web development framework for Vue.js. From 4.6.0 until 4.6.3, Nuxt resolves literal or percent-encoded dot segments before rendering a page while Nitro routing, server/middleware checks, and server route rules evaluate the unresolved path. A request such as /%2e/admin can therefore render app/pages/admin.vue and its server-rendered data while checks keyed to /admin, redirects, or per-route security headers do not apply. API handlers, appMiddleware, Nuxt 3, and Nuxt 4.0.0 t

- [https://github.com/federiconbaez/cortex9-nuxt-dot-segment-middleware-bypass-model](https://github.com/federiconbaez/cortex9-nuxt-dot-segment-middleware-bypass-model) : ![starts](https://img.shields.io/github/stars/federiconbaez/cortex9-nuxt-dot-segment-middleware-bypass-model.svg) ![forks](https://img.shields.io/github/forks/federiconbaez/cortex9-nuxt-dot-segment-middleware-bypass-model.svg)

## CVE-2026-123158
> sshd in OpenSSH before 10.6p2 on Linux, when musl libc is used without PAM, lacks a workaround for a password authentication bypass (related to misinterpretation of whether a string is intended to be a password hash). For some configurations of accounts, any password between 256 and 1024 characters succeeds. An example of a platform using musl libc without PAM is Alpine Linux.

- [https://github.com/D1se0/CVE-2026-123158](https://github.com/D1se0/CVE-2026-123158) : ![starts](https://img.shields.io/github/stars/D1se0/CVE-2026-123158.svg) ![forks](https://img.shields.io/github/forks/D1se0/CVE-2026-123158.svg)
- [https://github.com/aciddust/CVE-2026-123158-LAB](https://github.com/aciddust/CVE-2026-123158-LAB) : ![starts](https://img.shields.io/github/stars/aciddust/CVE-2026-123158-LAB.svg) ![forks](https://img.shields.io/github/forks/aciddust/CVE-2026-123158-LAB.svg)

## CVE-2026-123488
> Craft CMS 4.0.0 before 4.18.9 and 5.0.0 before 5.11.2 contains an unauthenticated SQL injection vulnerability in the element search endpoint because the attribute parameter is concatenated into the query unsanitized and emulated PDO prepares allow stacked statements. Remote attackers can read and write the database, setting the admin flag or overwriting password hashes in the users table to gain administrator access.

- [https://github.com/ashrafzaryouh/CVE-2026-123488](https://github.com/ashrafzaryouh/CVE-2026-123488) : ![starts](https://img.shields.io/github/stars/ashrafzaryouh/CVE-2026-123488.svg) ![forks](https://img.shields.io/github/forks/ashrafzaryouh/CVE-2026-123488.svg)

## CVE-2026-124450
> OpenEMR before 8.3.0 contains a broken access control and path traversal vulnerability in the fax/sms module disposeDocument action via an unvalidated file_path parameter. Authenticated low-privilege users can read sqlconf.php to recover database credentials and write arbitrary files as the web user, enabling remote code execution.

- [https://github.com/Nxploited/CVE-2026-124450](https://github.com/Nxploited/CVE-2026-124450) : ![starts](https://img.shields.io/github/stars/Nxploited/CVE-2026-124450.svg) ![forks](https://img.shields.io/github/forks/Nxploited/CVE-2026-124450.svg)

## CVE-2026-124552
> Webmin through 2.670 contains a stored cross-site scripting vulnerability in the Shorewall and Shorewall6 modules&#x27; list.cgi, which renders table fields and COMMENT lines unescaped. Authenticated users with table edit permission can store JavaScript via savecmt.cgi or table entries that executes when other users, including root, view the list page.

- [https://github.com/googlesky/CVE-2026-124552](https://github.com/googlesky/CVE-2026-124552) : ![starts](https://img.shields.io/github/stars/googlesky/CVE-2026-124552.svg) ![forks](https://img.shields.io/github/forks/googlesky/CVE-2026-124552.svg)

## CVE-2026-14431

- [https://github.com/djayaGit/CVE-2026-14431](https://github.com/djayaGit/CVE-2026-14431) : ![starts](https://img.shields.io/github/stars/djayaGit/CVE-2026-14431.svg) ![forks](https://img.shields.io/github/forks/djayaGit/CVE-2026-14431.svg)

## CVE-2026-20253

- [https://github.com/NSK-394/owasp-nettacker-contribution](https://github.com/NSK-394/owasp-nettacker-contribution) : ![starts](https://img.shields.io/github/stars/NSK-394/owasp-nettacker-contribution.svg) ![forks](https://img.shields.io/github/forks/NSK-394/owasp-nettacker-contribution.svg)
- [https://github.com/ashrafzaryouh/CVE-2026-20253](https://github.com/ashrafzaryouh/CVE-2026-20253) : ![starts](https://img.shields.io/github/stars/ashrafzaryouh/CVE-2026-20253.svg) ![forks](https://img.shields.io/github/forks/ashrafzaryouh/CVE-2026-20253.svg)

## CVE-2026-23813

- [https://github.com/cyberaeonic/security-research](https://github.com/cyberaeonic/security-research) : ![starts](https://img.shields.io/github/stars/cyberaeonic/security-research.svg) ![forks](https://img.shields.io/github/forks/cyberaeonic/security-research.svg)

## CVE-2026-24061
> telnetd in GNU Inetutils through 2.7 allows remote authentication bypass via a &quot;-f root&quot; value for the USER environment variable.

- [https://github.com/ashrafzaryouh/CVE-2026-24061](https://github.com/ashrafzaryouh/CVE-2026-24061) : ![starts](https://img.shields.io/github/stars/ashrafzaryouh/CVE-2026-24061.svg) ![forks](https://img.shields.io/github/forks/ashrafzaryouh/CVE-2026-24061.svg)
- [https://github.com/hosun-hwang/CVE-2026-24061_PoC](https://github.com/hosun-hwang/CVE-2026-24061_PoC) : ![starts](https://img.shields.io/github/stars/hosun-hwang/CVE-2026-24061_PoC.svg) ![forks](https://img.shields.io/github/forks/hosun-hwang/CVE-2026-24061_PoC.svg)

## CVE-2026-26189

- [https://github.com/federiconbaez/cortex9-trivy-action-envfile-source-injection-model](https://github.com/federiconbaez/cortex9-trivy-action-envfile-source-injection-model) : ![starts](https://img.shields.io/github/stars/federiconbaez/cortex9-trivy-action-envfile-source-injection-model.svg) ![forks](https://img.shields.io/github/forks/federiconbaez/cortex9-trivy-action-envfile-source-injection-model.svg)

## CVE-2026-2835

- [https://github.com/federiconbaez/cortex9-pingora-http10-te-smuggling-model](https://github.com/federiconbaez/cortex9-pingora-http10-te-smuggling-model) : ![starts](https://img.shields.io/github/stars/federiconbaez/cortex9-pingora-http10-te-smuggling-model.svg) ![forks](https://img.shields.io/github/forks/federiconbaez/cortex9-pingora-http10-te-smuggling-model.svg)

## CVE-2026-31431
> In the Linux kernel, the following vulnerability has been resolved:

crypto: algif_aead - Revert to operating out-of-place

This mostly reverts commit 72548b093ee3 except for the copying of
the associated data.

There is no benefit in operating in-place in algif_aead since the
source and destination come from different mappings.  Get rid of
all the complexity added for in-place operation and just copy the
AD directly.

- [https://github.com/hosun-hwang/CVE-2026-31431_PoC](https://github.com/hosun-hwang/CVE-2026-31431_PoC) : ![starts](https://img.shields.io/github/stars/hosun-hwang/CVE-2026-31431_PoC.svg) ![forks](https://img.shields.io/github/forks/hosun-hwang/CVE-2026-31431_PoC.svg)

## CVE-2026-31864

- [https://github.com/federiconbaez/cortex9-jumpserver-yaml-jinja-sandbox-model](https://github.com/federiconbaez/cortex9-jumpserver-yaml-jinja-sandbox-model) : ![starts](https://img.shields.io/github/stars/federiconbaez/cortex9-jumpserver-yaml-jinja-sandbox-model.svg) ![forks](https://img.shields.io/github/forks/federiconbaez/cortex9-jumpserver-yaml-jinja-sandbox-model.svg)

## CVE-2026-33050
> GeoNode is a geospatial content management system, a platform for the management and publication of geospatial data. Prior to 5.1.0, a crafted vector file layer name supplied during upload allows a low-privileged remote user to inject shell syntax and execute arbitrary operating-system commands on the GeoNode server. This issue is fixed in version 5.1.0.

- [https://github.com/federiconbaez/cortex9-geonode-layer-name-command-injection-model](https://github.com/federiconbaez/cortex9-geonode-layer-name-command-injection-model) : ![starts](https://img.shields.io/github/stars/federiconbaez/cortex9-geonode-layer-name-command-injection-model.svg) ![forks](https://img.shields.io/github/forks/federiconbaez/cortex9-geonode-layer-name-command-injection-model.svg)

## CVE-2026-35616

- [https://github.com/ashrafzaryouh/CVE-2026-35616](https://github.com/ashrafzaryouh/CVE-2026-35616) : ![starts](https://img.shields.io/github/stars/ashrafzaryouh/CVE-2026-35616.svg) ![forks](https://img.shields.io/github/forks/ashrafzaryouh/CVE-2026-35616.svg)

## CVE-2026-39883

- [https://github.com/NinjaShadowBoy/SSI-cve-39883-lab](https://github.com/NinjaShadowBoy/SSI-cve-39883-lab) : ![starts](https://img.shields.io/github/stars/NinjaShadowBoy/SSI-cve-39883-lab.svg) ![forks](https://img.shields.io/github/forks/NinjaShadowBoy/SSI-cve-39883-lab.svg)

## CVE-2026-40175

- [https://github.com/ashrafzaryouh/CVE-2026-40175](https://github.com/ashrafzaryouh/CVE-2026-40175) : ![starts](https://img.shields.io/github/stars/ashrafzaryouh/CVE-2026-40175.svg) ![forks](https://img.shields.io/github/forks/ashrafzaryouh/CVE-2026-40175.svg)

## CVE-2026-41940
> cPanel and WHM versions after 11.40 contain an authentication bypass vulnerability in the login flow that allows unauthenticated remote attackers to gain unauthorized access to the control panel.

- [https://github.com/ashrafzaryouh/CVE-2026-41940](https://github.com/ashrafzaryouh/CVE-2026-41940) : ![starts](https://img.shields.io/github/stars/ashrafzaryouh/CVE-2026-41940.svg) ![forks](https://img.shields.io/github/forks/ashrafzaryouh/CVE-2026-41940.svg)
- [https://github.com/ryhnmhrdka/CVE-2026-41940](https://github.com/ryhnmhrdka/CVE-2026-41940) : ![starts](https://img.shields.io/github/stars/ryhnmhrdka/CVE-2026-41940.svg) ![forks](https://img.shields.io/github/forks/ryhnmhrdka/CVE-2026-41940.svg)
- [https://github.com/ylerpeek/CVE-2026-41940-PoC-3](https://github.com/ylerpeek/CVE-2026-41940-PoC-3) : ![starts](https://img.shields.io/github/stars/ylerpeek/CVE-2026-41940-PoC-3.svg) ![forks](https://img.shields.io/github/forks/ylerpeek/CVE-2026-41940-PoC-3.svg)

## CVE-2026-50656

- [https://github.com/ashrafzaryouh/CVE-2026-50656](https://github.com/ashrafzaryouh/CVE-2026-50656) : ![starts](https://img.shields.io/github/stars/ashrafzaryouh/CVE-2026-50656.svg) ![forks](https://img.shields.io/github/forks/ashrafzaryouh/CVE-2026-50656.svg)

## CVE-2026-50751

- [https://github.com/ashrafzaryouh/CVE-2026-50751](https://github.com/ashrafzaryouh/CVE-2026-50751) : ![starts](https://img.shields.io/github/stars/ashrafzaryouh/CVE-2026-50751.svg) ![forks](https://img.shields.io/github/forks/ashrafzaryouh/CVE-2026-50751.svg)

## CVE-2026-53359
> In the Linux kernel, the following vulnerability has been resolved:

KVM: x86: Fix shadow paging use-after-free due to unexpected role

Commit 0cb2af2ea66ad (&quot;KVM: x86: Fix shadow paging use-after-free due
to unexpected GFN&quot;) fixed a shadow paging mismatch between stored and
computed GFNs; the bug could be triggered by changing a PDE mapping from
outside the guest, and then deleting a memslot.  The rmap_remove()
call would miss entries created after the PDE change because the GFN
of the leaf SPT

- [https://github.com/ashrafzaryouh/CVE-2026-53359](https://github.com/ashrafzaryouh/CVE-2026-53359) : ![starts](https://img.shields.io/github/stars/ashrafzaryouh/CVE-2026-53359.svg) ![forks](https://img.shields.io/github/forks/ashrafzaryouh/CVE-2026-53359.svg)

## CVE-2026-54017

- [https://github.com/federiconbaez/cortex9-open-webui-proxy-multidecode-traversal-model](https://github.com/federiconbaez/cortex9-open-webui-proxy-multidecode-traversal-model) : ![starts](https://img.shields.io/github/stars/federiconbaez/cortex9-open-webui-proxy-multidecode-traversal-model.svg) ![forks](https://img.shields.io/github/forks/federiconbaez/cortex9-open-webui-proxy-multidecode-traversal-model.svg)

## CVE-2026-55797
> Argo CD is a declarative, GitOps continuous delivery tool for Kubernetes. From 2.11.0 until 3.3.15, 3.4.10, 3.5.4, and 3.6.0-rc2, the Argo CD repo-server is vulnerable to command injection when it clones, tests, or fetches an SSH Git repository configured with a proxy URL. The proxy host and port are embedded in an SSH ProxyCommand that is executed through a shell without neutralizing shell metacharacters. A user who can create or update a repository or repository credential template can supply 

- [https://github.com/federiconbaez/cortex9-argocd-git-ssh-proxy-url-injection-model](https://github.com/federiconbaez/cortex9-argocd-git-ssh-proxy-url-injection-model) : ![starts](https://img.shields.io/github/stars/federiconbaez/cortex9-argocd-git-ssh-proxy-url-injection-model.svg) ![forks](https://img.shields.io/github/forks/federiconbaez/cortex9-argocd-git-ssh-proxy-url-injection-model.svg)

## CVE-2026-56712

- [https://github.com/SaiTeja-Erukude/CVE-2026-56712-cog-ssrf](https://github.com/SaiTeja-Erukude/CVE-2026-56712-cog-ssrf) : ![starts](https://img.shields.io/github/stars/SaiTeja-Erukude/CVE-2026-56712-cog-ssrf.svg) ![forks](https://img.shields.io/github/forks/SaiTeja-Erukude/CVE-2026-56712-cog-ssrf.svg)

## CVE-2026-57845
> Hugging Face Datasets through 5.1.0 contains an insecure deserialization vulnerability that allows attackers to execute arbitrary Python code by crafting a malicious pickle file loaded through the deprecated pandas packaged builder. Attackers can supply a pickle-backed dataset that is processed by Pandas._generate_tables via pandas.read_pickle() without validation, so when a victim calls datasets.load_dataset(&quot;pandas&quot;, data_files=...), the embedded __reduce__ payload executes code with the victi

- [https://github.com/Sun-Wukhan/pickle-sentry](https://github.com/Sun-Wukhan/pickle-sentry) : ![starts](https://img.shields.io/github/stars/Sun-Wukhan/pickle-sentry.svg) ![forks](https://img.shields.io/github/forks/Sun-Wukhan/pickle-sentry.svg)

## CVE-2026-58882
> In decodeWapPdu of WapPushOverSms.java, there is a possible out of bounds read due to an integer overflow. This could lead to a remote denial of service with no additional execution privileges needed. User interaction is not needed for exploitation.

- [https://github.com/uzairdeveloper223/Defib](https://github.com/uzairdeveloper223/Defib) : ![starts](https://img.shields.io/github/stars/uzairdeveloper223/Defib.svg) ![forks](https://img.shields.io/github/forks/uzairdeveloper223/Defib.svg)

## CVE-2026-60004

- [https://github.com/ashrafzaryouh/CVE-2026-60004](https://github.com/ashrafzaryouh/CVE-2026-60004) : ![starts](https://img.shields.io/github/stars/ashrafzaryouh/CVE-2026-60004.svg) ![forks](https://img.shields.io/github/forks/ashrafzaryouh/CVE-2026-60004.svg)

## CVE-2026-62367
> Vikunja is an open-source self-hosted task management platform. In versions 1.0.0 through 2.3.0, when an administrator enables the per-provider `emailfallback` option on an OpenID Connect provider, Vikunja links an SSO login to a pre-existing local (username+password) account using only the `email` claim from the IdP. The fallback never checks an `email_verified` (or Microsoft `xms_edov`) signal and never requires the matched account&#x27;s password. An attacker who can obtain a token from the config

- [https://github.com/federiconbaez/cortex9-vikunja-oidc-email-verified-linking-model](https://github.com/federiconbaez/cortex9-vikunja-oidc-email-verified-linking-model) : ![starts](https://img.shields.io/github/stars/federiconbaez/cortex9-vikunja-oidc-email-verified-linking-model.svg) ![forks](https://img.shields.io/github/forks/federiconbaez/cortex9-vikunja-oidc-email-verified-linking-model.svg)

## CVE-2026-63292
> Stack-based buffer overflow in mod_vhost_alias in Apache Software Foundation Apache HTTP Server through 2.4.68 on all platforms allows a remote client to cause a denial of service or potentially execute arbitrary code via an HTTP request with a Host header exceeding 8192 bytes when VirtualDocumentRoot uses a hostname format specifier and LimitRequestFieldSize is raised above the default.

Users are recommended to upgrade to version 2.4.69, which fixes this issue.

- [https://github.com/ashrafzaryouh/CVE-2026-63292](https://github.com/ashrafzaryouh/CVE-2026-63292) : ![starts](https://img.shields.io/github/stars/ashrafzaryouh/CVE-2026-63292.svg) ![forks](https://img.shields.io/github/forks/ashrafzaryouh/CVE-2026-63292.svg)

## CVE-2026-63686
> A NULL pointer dereference in mod_xml2enc in Apache Software Foundation Apache HTTP Server before 2.4.69 on all platforms allows an untrusted backend server to cause a denial of service via a proxied response with a charset whose conversion partially succeeds then fails.

Users are recommended to upgrade to version 2.4.69, which fixes this issue.

- [https://github.com/duruton/CVE-2026-63686-Dalton-Tim-](https://github.com/duruton/CVE-2026-63686-Dalton-Tim-) : ![starts](https://img.shields.io/github/stars/duruton/CVE-2026-63686-Dalton-Tim-.svg) ![forks](https://img.shields.io/github/forks/duruton/CVE-2026-63686-Dalton-Tim-.svg)

## CVE-2026-64849
> MLflow is an open source AI engineering platform for agents, large language models, and machine learning models. Starting in 3.3.0 and prior to 3.15.0, the unauthenticated POST /api/2.0/mlflow/webhooks/{id}/test endpoint calls _validate_webhook_url() in mlflow/utils/validation.py only for the original URL while mlflow/webhooks/delivery.py follows redirects and re-resolves the hostname without pinning the validated address, allowing attackers to reach internal or cloud metadata services and recei

- [https://github.com/federiconbaez/cortex9-mlflow-webhook-dns-rebinding-toctou-model](https://github.com/federiconbaez/cortex9-mlflow-webhook-dns-rebinding-toctou-model) : ![starts](https://img.shields.io/github/stars/federiconbaez/cortex9-mlflow-webhook-dns-rebinding-toctou-model.svg) ![forks](https://img.shields.io/github/forks/federiconbaez/cortex9-mlflow-webhook-dns-rebinding-toctou-model.svg)

## CVE-2026-65600
> Traefik versions &lt;= v2.11.51, &gt;= v3.6.0 &lt;= v3.6.22, and &gt;= v3.7.0 &lt;= v3.7.6 contain an authentication bypass via path traversal in the ReplacePathRegex middleware. When ReplacePathRegex is configured with a regex that captures user-controlled path segments without a mandatory path separator (e.g. regex &quot;^/api(.*)&quot;, replacement &quot;/$1&quot;), the middleware forwards the replaced path to the backend without validating that it matches its normalized form. An unauthenticated remote attacker can send a craf

- [https://github.com/federiconbaez/cortex9-traefik-replacepathregex-normalization-model](https://github.com/federiconbaez/cortex9-traefik-replacepathregex-normalization-model) : ![starts](https://img.shields.io/github/stars/federiconbaez/cortex9-traefik-replacepathregex-normalization-model.svg) ![forks](https://img.shields.io/github/forks/federiconbaez/cortex9-traefik-replacepathregex-normalization-model.svg)

## CVE-2026-72422

- [https://github.com/federiconbaez/cortex9-ksmbd-preauth-info-race-model](https://github.com/federiconbaez/cortex9-ksmbd-preauth-info-race-model) : ![starts](https://img.shields.io/github/stars/federiconbaez/cortex9-ksmbd-preauth-info-race-model.svg) ![forks](https://img.shields.io/github/forks/federiconbaez/cortex9-ksmbd-preauth-info-race-model.svg)

## CVE-2026-73802
> Gitea Runner passes workflow-controlled container options into Docker job container configuration while privileged mode is disabled. Host namespace settings, expanded capabilities, and security profile overrides can remain effective despite Privileged being forced false. A workflow author able to run jobs on an affected Docker-backed runner can use these options to access host namespaces and execute commands as root on the runner host, bypassing the intended container isolation.

- [https://github.com/sn0x-sharma/Gitea2shell-Sandbox-Escape-to-Host-RCE](https://github.com/sn0x-sharma/Gitea2shell-Sandbox-Escape-to-Host-RCE) : ![starts](https://img.shields.io/github/stars/sn0x-sharma/Gitea2shell-Sandbox-Escape-to-Host-RCE.svg) ![forks](https://img.shields.io/github/forks/sn0x-sharma/Gitea2shell-Sandbox-Escape-to-Host-RCE.svg)

## CVE-2026-73858
> Solspace Freeform plugin for Craft CMS 5.x is a super flexible form-building tool. From 5.0.0 through 5.10.13, submitted values from public Freeform forms can be evaluated by the isolated Twig renderer when rendered into HTML attributes. An unauthenticated attacker can place Twig expressions in submitted field values, including value attributes, and receive evaluated PHP, operating-system, or Craft filesystem-path constants in the form response. The isolated context was not shown to expose Craft

- [https://github.com/federiconbaez/cortex9-freeform-attribute-twig-render-model](https://github.com/federiconbaez/cortex9-freeform-attribute-twig-render-model) : ![starts](https://img.shields.io/github/stars/federiconbaez/cortex9-freeform-attribute-twig-render-model.svg) ![forks](https://img.shields.io/github/forks/federiconbaez/cortex9-freeform-attribute-twig-render-model.svg)

## CVE-2026-75037

- [https://github.com/federiconbaez/cortex9-lact-polkit-pid-subject-bypass-model](https://github.com/federiconbaez/cortex9-lact-polkit-pid-subject-bypass-model) : ![starts](https://img.shields.io/github/stars/federiconbaez/cortex9-lact-polkit-pid-subject-bypass-model.svg) ![forks](https://img.shields.io/github/forks/federiconbaez/cortex9-lact-polkit-pid-subject-bypass-model.svg)

## CVE-2026-79657
> NLTK versions before 3.10.3 contain a remote code execution vulnerability in allowlisted pickle loaders that trust entire module namespaces instead of specific safe callables. Attackers can craft malicious pickle payloads invoking dangerous in-namespace functions like ReppTokenizer._execute and numpy.f2py.crackfortran.myeval through pickle REDUCE to execute arbitrary commands during model or tokenizer artifact loading.

- [https://github.com/federiconbaez/cortex9-nltk-pickle-allowlist-prefix-model](https://github.com/federiconbaez/cortex9-nltk-pickle-allowlist-prefix-model) : ![starts](https://img.shields.io/github/stars/federiconbaez/cortex9-nltk-pickle-allowlist-prefix-model.svg) ![forks](https://img.shields.io/github/forks/federiconbaez/cortex9-nltk-pickle-allowlist-prefix-model.svg)

## CVE-2026-83844

- [https://github.com/HackingLZ/CVE-2026-83844-public](https://github.com/HackingLZ/CVE-2026-83844-public) : ![starts](https://img.shields.io/github/stars/HackingLZ/CVE-2026-83844-public.svg) ![forks](https://img.shields.io/github/forks/HackingLZ/CVE-2026-83844-public.svg)
- [https://github.com/ashrafzaryouh/CVE-2026-83844](https://github.com/ashrafzaryouh/CVE-2026-83844) : ![starts](https://img.shields.io/github/stars/ashrafzaryouh/CVE-2026-83844.svg) ![forks](https://img.shields.io/github/forks/ashrafzaryouh/CVE-2026-83844.svg)

## CVE-2026-84380

- [https://github.com/federiconbaez/cortex9-httpx2-cl-te-framing-conflict-model](https://github.com/federiconbaez/cortex9-httpx2-cl-te-framing-conflict-model) : ![starts](https://img.shields.io/github/stars/federiconbaez/cortex9-httpx2-cl-te-framing-conflict-model.svg) ![forks](https://img.shields.io/github/forks/federiconbaez/cortex9-httpx2-cl-te-framing-conflict-model.svg)

## CVE-2026-8461

- [https://github.com/ashrafzaryouh/CVE-2026-8461](https://github.com/ashrafzaryouh/CVE-2026-8461) : ![starts](https://img.shields.io/github/stars/ashrafzaryouh/CVE-2026-8461.svg) ![forks](https://img.shields.io/github/forks/ashrafzaryouh/CVE-2026-8461.svg)

## CVE-2026-88771
> Improper input validation vulnerability in Citrix NetScaler ADC and Citrix NetScaler Gateway.

This issue affects ADC: before 14.1-73.37, before 13.1-64.23, before 14.1-73.37 FIPS, and before 13.1.37.279 FIPS and NDcPP; Gateway: before 14.1-73.37 and before 13.1-64.23 leading to an unauthenticated attacker to execute arbitrary commands.

- [https://github.com/CompleteTech-Security/netscaler-pitscaler-cve-2026-88771-check](https://github.com/CompleteTech-Security/netscaler-pitscaler-cve-2026-88771-check) : ![starts](https://img.shields.io/github/stars/CompleteTech-Security/netscaler-pitscaler-cve-2026-88771-check.svg) ![forks](https://img.shields.io/github/forks/CompleteTech-Security/netscaler-pitscaler-cve-2026-88771-check.svg)
- [https://github.com/irfanr-source/Get-NetScalerTimeline](https://github.com/irfanr-source/Get-NetScalerTimeline) : ![starts](https://img.shields.io/github/stars/irfanr-source/Get-NetScalerTimeline.svg) ![forks](https://img.shields.io/github/forks/irfanr-source/Get-NetScalerTimeline.svg)

## CVE-2026-88772
> Vulnerability in Citrix NetScaler ADC and Citrix NetScaler Gateway.

This issue affects ADC: before 14.1-73.37, before 13.1-64.23, before 14.1-73.37 FIPS, and before 13.1.37.279 FIPS and NDcPP; Gateway: before 14.1-73.37 and before 13.1-64.23 leading to Remote Code Execution or Denial of Service

- [https://github.com/CompleteTech-Security/netscaler-pitscaler-cve-2026-88772-check](https://github.com/CompleteTech-Security/netscaler-pitscaler-cve-2026-88772-check) : ![starts](https://img.shields.io/github/stars/CompleteTech-Security/netscaler-pitscaler-cve-2026-88772-check.svg) ![forks](https://img.shields.io/github/forks/CompleteTech-Security/netscaler-pitscaler-cve-2026-88772-check.svg)

## CVE-2026-92080
> Improper Limitation of a Pathname to a Restricted Directory (&#x27;Path Traversal&#x27;) vulnerability in TÜBİTAK BİLGEM Software Technologies Research Institute pardus-boot-repair allows Path Traversal.

This issue affects pardus-boot-repair: from 1.0.8 before 1.1.0.

- [https://github.com/ozcanpng/CVE-2026-92080](https://github.com/ozcanpng/CVE-2026-92080) : ![starts](https://img.shields.io/github/stars/ozcanpng/CVE-2026-92080.svg) ![forks](https://img.shields.io/github/forks/ozcanpng/CVE-2026-92080.svg)

## CVE-2026-92606

- [https://github.com/ozcanpng/CVE-2026-92606](https://github.com/ozcanpng/CVE-2026-92606) : ![starts](https://img.shields.io/github/stars/ozcanpng/CVE-2026-92606.svg) ![forks](https://img.shields.io/github/forks/ozcanpng/CVE-2026-92606.svg)

## CVE-2026-94434

- [https://github.com/ozcanpng/CVE-2026-94434](https://github.com/ozcanpng/CVE-2026-94434) : ![starts](https://img.shields.io/github/stars/ozcanpng/CVE-2026-94434.svg) ![forks](https://img.shields.io/github/forks/ozcanpng/CVE-2026-94434.svg)

## CVE-2026-96760
> Authlib (v1.7.2 and below) contains a signature verification bypass vulnerability. The JsonWebSignature.deserialize_json() method accepts a JSON Serialization JWS object and returns the payload as successfully verified without checking for a signature and without requiring a cryptographic key.

- [https://github.com/federiconbaez/cortex9-authlib-jws-json-empty-signatures-model](https://github.com/federiconbaez/cortex9-authlib-jws-json-empty-signatures-model) : ![starts](https://img.shields.io/github/stars/federiconbaez/cortex9-authlib-jws-json-empty-signatures-model.svg) ![forks](https://img.shields.io/github/forks/federiconbaez/cortex9-authlib-jws-json-empty-signatures-model.svg)

## CVE-2026-96889
> A flaw was found in librsvg. When processing an SVG document containing nested XML inclusions (Xincludes) with duplicate entity declarations, a use-after-free error can occur. This vulnerability arises because the library incorrectly frees an XML entity that is still in use by the parser. An attacker could potentially exploit this to cause a denial of service or execute arbitrary code.

- [https://github.com/anishadhikari02/cve-2026-96889-payload](https://github.com/anishadhikari02/cve-2026-96889-payload) : ![starts](https://img.shields.io/github/stars/anishadhikari02/cve-2026-96889-payload.svg) ![forks](https://img.shields.io/github/forks/anishadhikari02/cve-2026-96889-payload.svg)

## CVE-2026-98260
> In the Linux kernel, the following vulnerability has been resolved:

exec: Cleanup POSIX timers right after de_thread()

A per-thread CPU timer holds a reference to the PID of the thread it is
attached to and, while it is armed, its node is queued in that thread&#x27;s
posix_cputimers. The task is looked up by that PID.

When a non-leader thread exec()s, de_thread() changes which task owns
that PID. pid_task(timer-&gt;it.cpu.pid, PIDTYPE_PID) then returns NULL,
but the node is still queued on tsk, which

- [https://github.com/Yunnijian/Shark](https://github.com/Yunnijian/Shark) : ![starts](https://img.shields.io/github/stars/Yunnijian/Shark.svg) ![forks](https://img.shields.io/github/forks/Yunnijian/Shark.svg)
- [https://github.com/arkylin/CVE-2026-98260-Asteroids](https://github.com/arkylin/CVE-2026-98260-Asteroids) : ![starts](https://img.shields.io/github/stars/arkylin/CVE-2026-98260-Asteroids.svg) ![forks](https://img.shields.io/github/forks/arkylin/CVE-2026-98260-Asteroids.svg)
- [https://github.com/cuteaplane/opd2051example](https://github.com/cuteaplane/opd2051example) : ![starts](https://img.shields.io/github/stars/cuteaplane/opd2051example.svg) ![forks](https://img.shields.io/github/forks/cuteaplane/opd2051example.svg)

## CVE-2026-98432
> In the Linux kernel, the following vulnerability has been resolved:

ipv4: free inet_opt and ireq_opt after an RCU grace period

tcp_v4_syn_recv_sock() transfers ownership of ireq-&gt;ireq_opt to the
child socket (newinet-&gt;inet_opt) without copying it.

Another cpu can concurrently process a retransmitted SYN for the same
request socket, and send a SYNACK from tcp_check_req().
tcp_v4_send_synack() and inet_csk_route_req() read ireq-&gt;ireq_opt
under rcu_read_lock() only, and ip_build_and_send_pkt() a

- [https://github.com/ashrafzaryouh/CVE-2026-98432](https://github.com/ashrafzaryouh/CVE-2026-98432) : ![starts](https://img.shields.io/github/stars/ashrafzaryouh/CVE-2026-98432.svg) ![forks](https://img.shields.io/github/forks/ashrafzaryouh/CVE-2026-98432.svg)
- [https://github.com/jackykeung/CVE-2026-98432-Verified-Attack](https://github.com/jackykeung/CVE-2026-98432-Verified-Attack) : ![starts](https://img.shields.io/github/stars/jackykeung/CVE-2026-98432-Verified-Attack.svg) ![forks](https://img.shields.io/github/forks/jackykeung/CVE-2026-98432-Verified-Attack.svg)
- [https://github.com/rootagi/CVE-2026-98432](https://github.com/rootagi/CVE-2026-98432) : ![starts](https://img.shields.io/github/stars/rootagi/CVE-2026-98432.svg) ![forks](https://img.shields.io/github/forks/rootagi/CVE-2026-98432.svg)
