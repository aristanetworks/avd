<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>management_security</samp>](## "management_security") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;auto_certificate</samp>](## "management_security.auto_certificate") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;profiles</samp>](## "management_security.auto_certificate.profiles") | List, items: Dictionary |  |  |  | Profiles for automatic certificate enrollment and renewal. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "management_security.auto_certificate.profiles.[].name") | String | Required, Unique |  |  | Name of the certificate profile. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;digest</samp>](## "management_security.auto_certificate.profiles.[].digest") | String |  |  | Valid Values:<br>- <code>sha256</code><br>- <code>sha384</code><br>- <code>sha512</code> | Digest algorithm used to sign the Certificate Signing Request. Defaults to sha256 on EOS if unset. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key</samp>](## "management_security.auto_certificate.profiles.[].key") | String |  |  |  | Filename of the private key in the switch `sslkey:` directory. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;protocol_instance_name</samp>](## "management_security.auto_certificate.profiles.[].protocol_instance_name") | String |  |  |  | EST protocol profile name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;renewal</samp>](## "management_security.auto_certificate.profiles.[].renewal") | Integer |  |  | Min: 1<br>Max: 4294967295 | Renewal time in seconds. EOS default is 7200 seconds (2 hours). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;parameters</samp>](## "management_security.auto_certificate.profiles.[].parameters") | Dictionary |  |  |  | Parameters of the distinguished name and subject alternative name for the CSR. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;distinguished_name</samp>](## "management_security.auto_certificate.profiles.[].parameters.distinguished_name") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;common_name</samp>](## "management_security.auto_certificate.profiles.[].parameters.distinguished_name.common_name") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;country</samp>](## "management_security.auto_certificate.profiles.[].parameters.distinguished_name.country") | String |  |  | Pattern: `^[A-Z]{2}$` | ISO 3166-1 alpha-2 two-letter country code.<br>Example:<br>"US" for United States,<br>"DE" for Germany,<br>"IN" for India. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;email</samp>](## "management_security.auto_certificate.profiles.[].parameters.distinguished_name.email") | String |  |  | Pattern: `[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}` |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;locality</samp>](## "management_security.auto_certificate.profiles.[].parameters.distinguished_name.locality") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;organization</samp>](## "management_security.auto_certificate.profiles.[].parameters.distinguished_name.organization") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;organization_unit</samp>](## "management_security.auto_certificate.profiles.[].parameters.distinguished_name.organization_unit") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;serial_number</samp>](## "management_security.auto_certificate.profiles.[].parameters.distinguished_name.serial_number") | String |  |  |  | Serial Number for use in subject.<br>system: Use the device's serial number in subject. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;state</samp>](## "management_security.auto_certificate.profiles.[].parameters.distinguished_name.state") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;subject_alternative_name</samp>](## "management_security.auto_certificate.profiles.[].parameters.subject_alternative_name") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dns</samp>](## "management_security.auto_certificate.profiles.[].parameters.subject_alternative_name.dns") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "management_security.auto_certificate.profiles.[].parameters.subject_alternative_name.dns.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;email</samp>](## "management_security.auto_certificate.profiles.[].parameters.subject_alternative_name.email") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "management_security.auto_certificate.profiles.[].parameters.subject_alternative_name.email.[]") | String |  |  | Pattern: `[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}` |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip</samp>](## "management_security.auto_certificate.profiles.[].parameters.subject_alternative_name.ip") | List, items: String |  |  |  | IPv4/IPv6 addresses for use in subject-alternative-name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "management_security.auto_certificate.profiles.[].parameters.subject_alternative_name.ip.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uri</samp>](## "management_security.auto_certificate.profiles.[].parameters.subject_alternative_name.uri") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "management_security.auto_certificate.profiles.[].parameters.subject_alternative_name.uri.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;protocols</samp>](## "management_security.auto_certificate.protocols") | List, items: Dictionary |  |  |  | Protocols for automatic certificate enrollment and renewal. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "management_security.auto_certificate.protocols.[].name") | String | Required, Unique |  |  | Name of the EST profile. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;protocol</samp>](## "management_security.auto_certificate.protocols.[].protocol") | String | Required |  | Valid Values:<br>- <code>est</code> | Protocol to use to communicate with endpoint; only EST is supported currently. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;disabled</samp>](## "management_security.auto_certificate.protocols.[].disabled") | Boolean |  |  |  | Temporarily disable sending requests to the server. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;connection_retry</samp>](## "management_security.auto_certificate.protocols.[].connection_retry") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;count</samp>](## "management_security.auto_certificate.protocols.[].connection_retry.count") | Integer |  |  | Min: 0<br>Max: 4294967295 | Number of retries to attempt before giving up, if not configured the number of retries is infinite. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interval</samp>](## "management_security.auto_certificate.protocols.[].connection_retry.interval") | Integer |  |  | Min: 1<br>Max: 4294967295 | Number of seconds between retries. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;exponential_backoff</samp>](## "management_security.auto_certificate.protocols.[].connection_retry.exponential_backoff") | Boolean |  |  |  | Exponentially increase the interval between retries to a maximum of 24 hours. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;credentials</samp>](## "management_security.auto_certificate.protocols.[].credentials") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enroll</samp>](## "management_security.auto_certificate.protocols.[].credentials.enroll") | Dictionary |  |  |  | Token or username/secret for initial certificate enrollment.<br>If both token and username/secret are defined, token will take precedence.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;token</samp>](## "management_security.auto_certificate.protocols.[].credentials.enroll.token") | String |  |  |  | JSON Web Token for Bearer Authentication. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;token_type</samp>](## "management_security.auto_certificate.protocols.[].credentials.enroll.token_type") | String |  | `7` | Valid Values:<br>- <code>0</code><br>- <code>7</code><br>- <code>8a</code> | Encoding type of the token:<br>"0" = cleartext,<br>"7" = obfuscated,<br>"8a" = AES-256-GCM encrypted. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;username</samp>](## "management_security.auto_certificate.protocols.[].credentials.enroll.username") | String |  |  |  | Username for HTTP Basic Authentication. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;secret</samp>](## "management_security.auto_certificate.protocols.[].credentials.enroll.secret") | String |  |  |  | Password for HTTP Basic Authentication. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;secret_type</samp>](## "management_security.auto_certificate.protocols.[].credentials.enroll.secret_type") | String |  | `7` | Valid Values:<br>- <code>0</code><br>- <code>7</code><br>- <code>8a</code> | Encoding type of the token:<br>"0" = cleartext,<br>"7" = obfuscated,<br>"8a" = AES-256-GCM encrypted. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;re_enroll</samp>](## "management_security.auto_certificate.protocols.[].credentials.re_enroll") | Dictionary |  |  |  | Token or username/secret for certificate re-enrollment.<br>If both token and username/secret are defined, token will take precedence.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;token</samp>](## "management_security.auto_certificate.protocols.[].credentials.re_enroll.token") | String |  |  |  | JSON Web Token for Bearer Authentication. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;token_type</samp>](## "management_security.auto_certificate.protocols.[].credentials.re_enroll.token_type") | String |  | `7` | Valid Values:<br>- <code>0</code><br>- <code>7</code><br>- <code>8a</code> | Encoding type of the token:<br>"0" = cleartext,<br>"7" = obfuscated,<br>"8a" = AES-256-GCM encrypted. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;username</samp>](## "management_security.auto_certificate.protocols.[].credentials.re_enroll.username") | String |  |  |  | Username for HTTP Basic Authentication. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;secret</samp>](## "management_security.auto_certificate.protocols.[].credentials.re_enroll.secret") | String |  |  |  | Password for HTTP Basic Authentication. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;secret_type</samp>](## "management_security.auto_certificate.protocols.[].credentials.re_enroll.secret_type") | String |  | `7` | Valid Values:<br>- <code>0</code><br>- <code>7</code><br>- <code>8a</code> | Encoding type of the token:<br>"0" = cleartext,<br>"7" = obfuscated,<br>"8a" = AES-256-GCM encrypted. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;server</samp>](## "management_security.auto_certificate.protocols.[].server") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ssl_profile</samp>](## "management_security.auto_certificate.protocols.[].server.ssl_profile") | String |  |  |  | SSL profile name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;url</samp>](## "management_security.auto_certificate.protocols.[].server.url") | String |  |  | Pattern: `https://.+[^/]` | EST server URL. Must begin with `https://`. Should not end with `/` (the well-known EST paths are appended automatically). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "management_security.auto_certificate.protocols.[].server.vrf") | String |  |  |  | VRF used to reach the EST server. If unset, the default VRF is used on EOS. |
    | [<samp>&nbsp;&nbsp;entropy_sources</samp>](## "management_security.entropy_sources") | Dictionary |  |  |  | Source of entropy. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;hardware</samp>](## "management_security.entropy_sources.hardware") | Boolean |  |  |  | Use a hardware based source. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;haveged</samp>](## "management_security.entropy_sources.haveged") | Boolean |  |  |  | Use the HAVEGE algorithm. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;cpu_jitter</samp>](## "management_security.entropy_sources.cpu_jitter") | Boolean |  |  |  | Use the Jitter RNG algorithm of a CPU based source. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;hardware_exclusive</samp>](## "management_security.entropy_sources.hardware_exclusive") | Boolean |  |  |  | Only use entropy from the hardware source. |
    | [<samp>&nbsp;&nbsp;signature_verification</samp>](## "management_security.signature_verification") | Dictionary |  |  |  | Verify the SWIX signatures. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "management_security.signature_verification.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ssl_profile</samp>](## "management_security.signature_verification.ssl_profile") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;password</samp>](## "management_security.password") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;minimum_length</samp>](## "management_security.password.minimum_length") | Integer |  |  | Min: 1<br>Max: 32 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;encryption_key_common</samp>](## "management_security.password.encryption_key_common") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;encryption_reversible</samp>](## "management_security.password.encryption_reversible") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;policies</samp>](## "management_security.password.policies") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "management_security.password.policies.[].name") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;minimum</samp>](## "management_security.password.policies.[].minimum") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;digits</samp>](## "management_security.password.policies.[].minimum.digits") | Integer |  |  | Min: 1<br>Max: 65535 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;length</samp>](## "management_security.password.policies.[].minimum.length") | Integer |  |  | Min: 1<br>Max: 65535 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;lower</samp>](## "management_security.password.policies.[].minimum.lower") | Integer |  |  | Min: 1<br>Max: 65535 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;special</samp>](## "management_security.password.policies.[].minimum.special") | Integer |  |  | Min: 1<br>Max: 65535 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;upper</samp>](## "management_security.password.policies.[].minimum.upper") | Integer |  |  | Min: 1<br>Max: 65535 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maximum</samp>](## "management_security.password.policies.[].maximum") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;repetitive</samp>](## "management_security.password.policies.[].maximum.repetitive") | Integer |  |  | Min: 1<br>Max: 65535 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sequential</samp>](## "management_security.password.policies.[].maximum.sequential") | Integer |  |  | Min: 1<br>Max: 65535 |  |
    | [<samp>&nbsp;&nbsp;ssl_profiles</samp>](## "management_security.ssl_profiles") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "management_security.ssl_profiles.[].name") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;fips_restrictions</samp>](## "management_security.ssl_profiles.[].fips_restrictions") | Boolean |  |  |  | Use FIPS compliant algorithms. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tls_versions</samp>](## "management_security.ssl_profiles.[].tls_versions") | String |  |  |  | List of allowed TLS versions as string.<br>Examples:<br>  - "1.0"<br>  - "1.0 1.1"<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cipher_list</samp>](## "management_security.ssl_profiles.[].cipher_list") | String |  |  |  | cipher_list syntax follows the openssl cipher strings format.<br>Colon (:) separated list of allowed ciphers as a string.<br>Not supported on EOS version starting 4.32.0F, use the `ciphers` setting instead.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ciphers</samp>](## "management_security.ssl_profiles.[].ciphers") | Dictionary |  |  |  | This setting is applicable to EOS versions 4.32.0F and later. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;v1_0</samp>](## "management_security.ssl_profiles.[].ciphers.v1_0") | String |  |  |  | The cipher suites for TLS version 1.0, 1.1 and 1.2.<br>Colon (:) separated list of allowed ciphers as a string.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;v1_3</samp>](## "management_security.ssl_profiles.[].ciphers.v1_3") | String |  |  |  | The cipher suites for TLS version 1.3.<br>Colon (:) separated list of allowed ciphers as a string.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;trust_certificate</samp>](## "management_security.ssl_profiles.[].trust_certificate") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;certificates</samp>](## "management_security.ssl_profiles.[].trust_certificate.certificates") | List, items: String |  |  |  | List of trust certificate names.<br>Examples:<br>  - test1.crt<br>  - test2.crt<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "management_security.ssl_profiles.[].trust_certificate.certificates.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;requirement</samp>](## "management_security.ssl_profiles.[].trust_certificate.requirement") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;basic_constraint_ca</samp>](## "management_security.ssl_profiles.[].trust_certificate.requirement.basic_constraint_ca") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hostname_fqdn</samp>](## "management_security.ssl_profiles.[].trust_certificate.requirement.hostname_fqdn") | Boolean |  |  |  | Enforce hostname to be FQDN without wildcard.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;policy_expiry_date_ignore</samp>](## "management_security.ssl_profiles.[].trust_certificate.policy_expiry_date_ignore") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;system</samp>](## "management_security.ssl_profiles.[].trust_certificate.system") | Boolean |  |  |  | Use system-supplied trust certificates.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;chain_certificate</samp>](## "management_security.ssl_profiles.[].chain_certificate") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;certificates</samp>](## "management_security.ssl_profiles.[].chain_certificate.certificates") | List, items: String |  |  |  | List of chain certificate names.<br>Examples:<br>  - chain1.crt<br>  - chain2.crt<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "management_security.ssl_profiles.[].chain_certificate.certificates.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;requirement</samp>](## "management_security.ssl_profiles.[].chain_certificate.requirement") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;basic_constraint_ca</samp>](## "management_security.ssl_profiles.[].chain_certificate.requirement.basic_constraint_ca") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_root_ca</samp>](## "management_security.ssl_profiles.[].chain_certificate.requirement.include_root_ca") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;certificate</samp>](## "management_security.ssl_profiles.[].certificate") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;file</samp>](## "management_security.ssl_profiles.[].certificate.file") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key</samp>](## "management_security.ssl_profiles.[].certificate.key") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;certificate_revocation_lists</samp>](## "management_security.ssl_profiles.[].certificate_revocation_lists") | List, items: String |  |  |  | List of CRLs (Certificate Revocation List).<br>If specified, one CRL needs to be provided for every certificate in the chain, even if the revocation list in the CRL is empty.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "management_security.ssl_profiles.[].certificate_revocation_lists.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;shared_secret_profiles</samp>](## "management_security.shared_secret_profiles") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;profile</samp>](## "management_security.shared_secret_profiles.[].profile") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;secrets</samp>](## "management_security.shared_secret_profiles.[].secrets") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "management_security.shared_secret_profiles.[].secrets.[].name") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;secret</samp>](## "management_security.shared_secret_profiles.[].secrets.[].secret") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;secret_type</samp>](## "management_security.shared_secret_profiles.[].secrets.[].secret_type") | String |  | `7` | Valid Values:<br>- <code>0</code><br>- <code>7</code><br>- <code>8a</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;receive_lifetime</samp>](## "management_security.shared_secret_profiles.[].secrets.[].receive_lifetime") | Dictionary | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;infinite</samp>](## "management_security.shared_secret_profiles.[].secrets.[].receive_lifetime.infinite") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;start_date_time</samp>](## "management_security.shared_secret_profiles.[].secrets.[].receive_lifetime.start_date_time") | String |  |  |  | Start date and time of lifetime of the secret. End date should be greater than start date.<br>Formats supported:<br>1. mm/dd/yyyy hh:mm:ss<br>2. yyyy-mm-dd hh:mm:ss<br>e.g 2024-12-20 10:00:00 |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;end_date_time</samp>](## "management_security.shared_secret_profiles.[].secrets.[].receive_lifetime.end_date_time") | String |  |  |  | End date and time of lifetime of the secret. End date should be greater than start date.<br>Formats supported:<br>1. mm/dd/yyyy hh:mm:ss<br>2. yyyy-mm-dd hh:mm:ss<br>e.g 2024-12-20 10:00:00 |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;transmit_lifetime</samp>](## "management_security.shared_secret_profiles.[].secrets.[].transmit_lifetime") | Dictionary | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;infinite</samp>](## "management_security.shared_secret_profiles.[].secrets.[].transmit_lifetime.infinite") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;start_date_time</samp>](## "management_security.shared_secret_profiles.[].secrets.[].transmit_lifetime.start_date_time") | String |  |  |  | Start date and time of lifetime of the secret. End date should be greater than start date.<br>Formats supported:<br>1. mm/dd/yyyy hh:mm:ss<br>2. yyyy-mm-dd hh:mm:ss<br>e.g 2024-12-20 10:00:00 |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;end_date_time</samp>](## "management_security.shared_secret_profiles.[].secrets.[].transmit_lifetime.end_date_time") | String |  |  |  | End date and time of lifetime of the secret. End date should be greater than start date.<br>Formats supported:<br>1. mm/dd/yyyy hh:mm:ss<br>2. yyyy-mm-dd hh:mm:ss<br>e.g 2024-12-20 10:00:00 |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;local_time</samp>](## "management_security.shared_secret_profiles.[].secrets.[].local_time") | Boolean |  |  |  | Configuring secret using the local timezone from system clock. Default is UTC. |

=== "YAML"

    ```yaml
    management_security:
      auto_certificate:

        # Profiles for automatic certificate enrollment and renewal.
        profiles:

            # Name of the certificate profile.
          - name: <str; required; unique>

            # Digest algorithm used to sign the Certificate Signing Request. Defaults to sha256 on EOS if unset.
            digest: <str; "sha256" | "sha384" | "sha512">

            # Filename of the private key in the switch `sslkey:` directory.
            key: <str>

            # EST protocol profile name.
            protocol_instance_name: <str>

            # Renewal time in seconds. EOS default is 7200 seconds (2 hours).
            renewal: <int; 1-4294967295>

            # Parameters of the distinguished name and subject alternative name for the CSR.
            parameters:
              distinguished_name:
                common_name: <str>

                # ISO 3166-1 alpha-2 two-letter country code.
                # Example:
                # "US" for United States,
                # "DE" for Germany,
                # "IN" for India.
                country: <str>
                email: <str>
                locality: <str>
                organization: <str>
                organization_unit: <str>

                # Serial Number for use in subject.
                # system: Use the device's serial number in subject.
                serial_number: <str>
                state: <str>
              subject_alternative_name:
                dns:
                  - <str>
                email:
                  - <str>

                # IPv4/IPv6 addresses for use in subject-alternative-name.
                ip:
                  - <str>
                uri:
                  - <str>

        # Protocols for automatic certificate enrollment and renewal.
        protocols:

            # Name of the EST profile.
          - name: <str; required; unique>

            # Protocol to use to communicate with endpoint; only EST is supported currently.
            protocol: <str; "est"; required>

            # Temporarily disable sending requests to the server.
            disabled: <bool>
            connection_retry:

              # Number of retries to attempt before giving up, if not configured the number of retries is infinite.
              count: <int; 0-4294967295>

              # Number of seconds between retries.
              interval: <int; 1-4294967295>

              # Exponentially increase the interval between retries to a maximum of 24 hours.
              exponential_backoff: <bool>
            credentials:

              # Token or username/secret for initial certificate enrollment.
              # If both token and username/secret are defined, token will take precedence.
              enroll:

                # JSON Web Token for Bearer Authentication.
                token: <str>

                # Encoding type of the token:
                # "0" = cleartext,
                # "7" = obfuscated,
                # "8a" = AES-256-GCM encrypted.
                token_type: <str; "0" | "7" | "8a"; default="7">

                # Username for HTTP Basic Authentication.
                username: <str>

                # Password for HTTP Basic Authentication.
                secret: <str>

                # Encoding type of the token:
                # "0" = cleartext,
                # "7" = obfuscated,
                # "8a" = AES-256-GCM encrypted.
                secret_type: <str; "0" | "7" | "8a"; default="7">

              # Token or username/secret for certificate re-enrollment.
              # If both token and username/secret are defined, token will take precedence.
              re_enroll:

                # JSON Web Token for Bearer Authentication.
                token: <str>

                # Encoding type of the token:
                # "0" = cleartext,
                # "7" = obfuscated,
                # "8a" = AES-256-GCM encrypted.
                token_type: <str; "0" | "7" | "8a"; default="7">

                # Username for HTTP Basic Authentication.
                username: <str>

                # Password for HTTP Basic Authentication.
                secret: <str>

                # Encoding type of the token:
                # "0" = cleartext,
                # "7" = obfuscated,
                # "8a" = AES-256-GCM encrypted.
                secret_type: <str; "0" | "7" | "8a"; default="7">
            server:

              # SSL profile name.
              ssl_profile: <str>

              # EST server URL. Must begin with `https://`. Should not end with `/` (the well-known EST paths are appended automatically).
              url: <str>

              # VRF used to reach the EST server. If unset, the default VRF is used on EOS.
              vrf: <str>

      # Source of entropy.
      entropy_sources:

        # Use a hardware based source.
        hardware: <bool>

        # Use the HAVEGE algorithm.
        haveged: <bool>

        # Use the Jitter RNG algorithm of a CPU based source.
        cpu_jitter: <bool>

        # Only use entropy from the hardware source.
        hardware_exclusive: <bool>

      # Verify the SWIX signatures.
      signature_verification:
        enabled: <bool; required>
        ssl_profile: <str>
      password:
        minimum_length: <int; 1-32>
        encryption_key_common: <bool>
        encryption_reversible: <str>
        policies:
          - name: <str; required; unique>
            minimum:
              digits: <int; 1-65535>
              length: <int; 1-65535>
              lower: <int; 1-65535>
              special: <int; 1-65535>
              upper: <int; 1-65535>
            maximum:
              repetitive: <int; 1-65535>
              sequential: <int; 1-65535>
      ssl_profiles:
        - name: <str; required; unique>

          # Use FIPS compliant algorithms.
          fips_restrictions: <bool>

          # List of allowed TLS versions as string.
          # Examples:
          #   - "1.0"
          #   - "1.0 1.1"
          tls_versions: <str>

          # cipher_list syntax follows the openssl cipher strings format.
          # Colon (:) separated list of allowed ciphers as a string.
          # Not supported on EOS version starting 4.32.0F, use the `ciphers` setting instead.
          cipher_list: <str>

          # This setting is applicable to EOS versions 4.32.0F and later.
          ciphers:

            # The cipher suites for TLS version 1.0, 1.1 and 1.2.
            # Colon (:) separated list of allowed ciphers as a string.
            v1_0: <str>

            # The cipher suites for TLS version 1.3.
            # Colon (:) separated list of allowed ciphers as a string.
            v1_3: <str>
          trust_certificate:

            # List of trust certificate names.
            # Examples:
            #   - test1.crt
            #   - test2.crt
            certificates:
              - <str>
            requirement:
              basic_constraint_ca: <bool>

              # Enforce hostname to be FQDN without wildcard.
              hostname_fqdn: <bool>
            policy_expiry_date_ignore: <bool>

            # Use system-supplied trust certificates.
            system: <bool>
          chain_certificate:

            # List of chain certificate names.
            # Examples:
            #   - chain1.crt
            #   - chain2.crt
            certificates:
              - <str>
            requirement:
              basic_constraint_ca: <bool>
              include_root_ca: <bool>
          certificate:
            file: <str>
            key: <str>

          # List of CRLs (Certificate Revocation List).
          # If specified, one CRL needs to be provided for every certificate in the chain, even if the revocation list in the CRL is empty.
          certificate_revocation_lists:
            - <str>
      shared_secret_profiles:
        - profile: <str; required; unique>
          secrets:
            - name: <str; required; unique>
              secret: <str; required>
              secret_type: <str; "0" | "7" | "8a"; default="7">
              receive_lifetime: # required
                infinite: <bool>

                # Start date and time of lifetime of the secret. End date should be greater than start date.
                # Formats supported:
                # 1. mm/dd/yyyy hh:mm:ss
                # 2. yyyy-mm-dd hh:mm:ss
                # e.g 2024-12-20 10:00:00
                start_date_time: <str>

                # End date and time of lifetime of the secret. End date should be greater than start date.
                # Formats supported:
                # 1. mm/dd/yyyy hh:mm:ss
                # 2. yyyy-mm-dd hh:mm:ss
                # e.g 2024-12-20 10:00:00
                end_date_time: <str>
              transmit_lifetime: # required
                infinite: <bool>

                # Start date and time of lifetime of the secret. End date should be greater than start date.
                # Formats supported:
                # 1. mm/dd/yyyy hh:mm:ss
                # 2. yyyy-mm-dd hh:mm:ss
                # e.g 2024-12-20 10:00:00
                start_date_time: <str>

                # End date and time of lifetime of the secret. End date should be greater than start date.
                # Formats supported:
                # 1. mm/dd/yyyy hh:mm:ss
                # 2. yyyy-mm-dd hh:mm:ss
                # e.g 2024-12-20 10:00:00
                end_date_time: <str>

              # Configuring secret using the local timezone from system clock. Default is UTC.
              local_time: <bool>
    ```
