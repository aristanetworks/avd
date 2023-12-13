<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>management_security</samp>](## "management_security") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;entropy_source</samp>](## "management_security.entropy_source") | String |  |  |  |  |
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
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "management_security.ssl_profiles.[].name") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tls_versions</samp>](## "management_security.ssl_profiles.[].tls_versions") | String |  |  |  | List of allowed TLS versions as string<br>Examples:<br>  - "1.0"<br>  - "1.0 1.1"<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cipher_list</samp>](## "management_security.ssl_profiles.[].cipher_list") | String |  |  |  | cipher_list syntax follows the openssl cipher strings format.<br>Colon (:) separated list of allowed ciphers as a string<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;trust_certificate</samp>](## "management_security.ssl_profiles.[].trust_certificate") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;certificates</samp>](## "management_security.ssl_profiles.[].trust_certificate.certificates") | List, items: String |  |  |  | List of trust certificate names<br>Examples:<br>  - test1.crt<br>  - test2.crt<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "management_security.ssl_profiles.[].trust_certificate.certificates.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;requirement</samp>](## "management_security.ssl_profiles.[].trust_certificate.requirement") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;basic_constraint_ca</samp>](## "management_security.ssl_profiles.[].trust_certificate.requirement.basic_constraint_ca") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hostname_fqdn</samp>](## "management_security.ssl_profiles.[].trust_certificate.requirement.hostname_fqdn") | Boolean |  |  |  | Enforce hostname to be FQDN without wildcard.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;policy_expiry_date_ignore</samp>](## "management_security.ssl_profiles.[].trust_certificate.policy_expiry_date_ignore") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;system</samp>](## "management_security.ssl_profiles.[].trust_certificate.system") | Boolean |  |  |  | Use system-supplied trust certificates.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;chain_certificate</samp>](## "management_security.ssl_profiles.[].chain_certificate") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;certificates</samp>](## "management_security.ssl_profiles.[].chain_certificate.certificates") | List, items: String |  |  |  | List of chain certificate names<br>Examples:<br>  - chain1.crt<br>  - chain2.crt<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "management_security.ssl_profiles.[].chain_certificate.certificates.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;requirement</samp>](## "management_security.ssl_profiles.[].chain_certificate.requirement") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;basic_constraint_ca</samp>](## "management_security.ssl_profiles.[].chain_certificate.requirement.basic_constraint_ca") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_root_ca</samp>](## "management_security.ssl_profiles.[].chain_certificate.requirement.include_root_ca") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;certificate</samp>](## "management_security.ssl_profiles.[].certificate") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;file</samp>](## "management_security.ssl_profiles.[].certificate.file") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key</samp>](## "management_security.ssl_profiles.[].certificate.key") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;certificate_revocation_lists</samp>](## "management_security.ssl_profiles.[].certificate_revocation_lists") | List, items: String |  |  |  | List of CRLs (Certificate Revocation List).<br>If specified, one CRL needs to be provided for every certificate in the chain, even if the revocation list in the CRL is empty.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "management_security.ssl_profiles.[].certificate_revocation_lists.[]") | String |  |  |  |  |

=== "YAML"

    ```yaml
    management_security:
      entropy_source: <str>
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
        - name: <str>

          # List of allowed TLS versions as string
          # Examples:
          #   - "1.0"
          #   - "1.0 1.1"
          tls_versions: <str>

          # cipher_list syntax follows the openssl cipher strings format.
          # Colon (:) separated list of allowed ciphers as a string
          cipher_list: <str>
          trust_certificate:

            # List of trust certificate names
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

            # List of chain certificate names
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
    ```
