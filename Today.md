# Update 2026-10-02
## CVE-2026-103752
> Unauthenticated Privilege Escalation in Authorizer &lt;= 3.15.3 versions.

- [https://github.com/anoxhunterdump-ctrl/CVE-2026-103752-Authorizer-Privilege-Escalation](https://github.com/anoxhunterdump-ctrl/CVE-2026-103752-Authorizer-Privilege-Escalation) : ![starts](https://img.shields.io/github/stars/anoxhunterdump-ctrl/CVE-2026-103752-Authorizer-Privilege-Escalation.svg) ![forks](https://img.shields.io/github/forks/anoxhunterdump-ctrl/CVE-2026-103752-Authorizer-Privilege-Escalation.svg)

## CVE-2026-14378
> The DevKit Pro plugin for WordPress is vulnerable to Authentication Bypass Leading to Administrator Account Takeover in all versions up to, and including, 2.3.0 This is due to the `revert_switch` handler trusting the attacker-controlled `original_user_id` cookie as the privileged identity: `verify_nonce_and_capability()` incorrectly checks the `manage_options` capability on the user identified by the cookie rather than on the actual requester via `current_user_can()`, while the switch-back form 

- [https://github.com/anoxhunterdump-ctrl/CVE-2026-14378-DevKit-Pro-Auth-Bypass](https://github.com/anoxhunterdump-ctrl/CVE-2026-14378-DevKit-Pro-Auth-Bypass) : ![starts](https://img.shields.io/github/stars/anoxhunterdump-ctrl/CVE-2026-14378-DevKit-Pro-Auth-Bypass.svg) ![forks](https://img.shields.io/github/forks/anoxhunterdump-ctrl/CVE-2026-14378-DevKit-Pro-Auth-Bypass.svg)
- [https://github.com/murrez/CVE-2026-14378](https://github.com/murrez/CVE-2026-14378) : ![starts](https://img.shields.io/github/stars/murrez/CVE-2026-14378.svg) ![forks](https://img.shields.io/github/forks/murrez/CVE-2026-14378.svg)

## CVE-2026-19445
> A remote, unauthenticated TLS client can make a server crash or call
through a freed pointer if its sni_callback assigns a different context to
SSLSocket.context (the documented way to select a certificate per server
name) and nothing else keeps the original ssl.SSLContext alive. Typical
cases are servers that create an SSLContext per connection or replace it
while connections are open; servers that wrap their listening socket with
it are not affected.


Mitigation: keep a reference to every SSL

- [https://github.com/abraxas/cve-2026-19445-sni-uaf](https://github.com/abraxas/cve-2026-19445-sni-uaf) : ![starts](https://img.shields.io/github/stars/abraxas/cve-2026-19445-sni-uaf.svg) ![forks](https://img.shields.io/github/forks/abraxas/cve-2026-19445-sni-uaf.svg)

## CVE-2026-19553
> ssl.SSLContext.wrap_bio() didn&#x27;t require the server_hostname argument
to not be None if ssl.SSLContext.check_hostname was set. Due to a
missing parameter check in SSLObject, if the server_hostname argument
isn&#x27;t supplied then hostname verification would be silently skipped.


This defect could lead to programs where certificate hostname verification
*appeared* to be succeeding with SSLContext.check_hostname = True and no
ValueError being raised due to misconfiguration.


If the program passes a 

- [https://github.com/abraxas/cve-2026-19553-wrap-bio](https://github.com/abraxas/cve-2026-19553-wrap-bio) : ![starts](https://img.shields.io/github/stars/abraxas/cve-2026-19553-wrap-bio.svg) ![forks](https://img.shields.io/github/forks/abraxas/cve-2026-19553-wrap-bio.svg)

## CVE-2026-19660
> The Divi Membership plugin for WordPress is vulnerable to Authentication Bypass in all versions up to, and including, 2.3.0. The `process_paypal_callback` function, hooked to the `init` action, accepts a base64-encoded `paypal_param` GET parameter with no IPN validation, no cryptographic signature check, no ownership verification, and no nonce, allowing it to trust an entirely attacker-controlled user ID value that is passed directly to `wp_set_current_user()` and `wp_set_auth_cookie()`. This ma

- [https://github.com/murrez/CVE-2026-19660](https://github.com/murrez/CVE-2026-19660) : ![starts](https://img.shields.io/github/stars/murrez/CVE-2026-19660.svg) ![forks](https://img.shields.io/github/forks/murrez/CVE-2026-19660.svg)

## CVE-2026-43499

- [https://github.com/yexiaoqq/rmg-s9110-research](https://github.com/yexiaoqq/rmg-s9110-research) : ![starts](https://img.shields.io/github/stars/yexiaoqq/rmg-s9110-research.svg) ![forks](https://img.shields.io/github/forks/yexiaoqq/rmg-s9110-research.svg)
