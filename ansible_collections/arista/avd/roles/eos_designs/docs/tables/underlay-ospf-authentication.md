<!--
  ~ Copyright (c) 2024 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>underlay_ospf_authentication</samp>](## "underlay_ospf_authentication") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;enabled</samp>](## "underlay_ospf_authentication.enabled") | Boolean |  | `False` |  |  |
    | [<samp>&nbsp;&nbsp;message_digest_keys</samp>](## "underlay_ospf_authentication.message_digest_keys") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;id</samp>](## "underlay_ospf_authentication.message_digest_keys.[].id") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hash_algorithm</samp>](## "underlay_ospf_authentication.message_digest_keys.[].hash_algorithm") | String |  | `sha512` | Valid Values:<br>- <code>md5</code><br>- <code>sha1</code><br>- <code>sha256</code><br>- <code>sha384</code><br>- <code>sha512</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key</samp>](## "underlay_ospf_authentication.message_digest_keys.[].key") | String |  |  |  | Key password<br>Only plaintext passwords are supported here as the password will ned to be encrypted for every underlay interface.<br>To protect the password at rest it is recommended to make use of Ansible Vault or similar.<br> |

=== "YAML"

    ```yaml
    underlay_ospf_authentication:
      enabled: <bool; default=False>
      message_digest_keys:
        - id: <int>
          hash_algorithm: <str; "md5" | "sha1" | "sha256" | "sha384" | "sha512"; default="sha512">

          # Key password
          # Only plaintext passwords are supported here as the password will ned to be encrypted for every underlay interface.
          # To protect the password at rest it is recommended to make use of Ansible Vault or similar.
          key: <str>
    ```
