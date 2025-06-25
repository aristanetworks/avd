<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>underlay_ospf_area</samp>](## "underlay_ospf_area") | String |  | `0.0.0.0` | Format: ipv4 |  |
    | [<samp>underlay_ospf_authentication</samp>](## "underlay_ospf_authentication") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;enabled</samp>](## "underlay_ospf_authentication.enabled") | Boolean | Required | `False` |  |  |
    | [<samp>&nbsp;&nbsp;message_digest_keys</samp>](## "underlay_ospf_authentication.message_digest_keys") | List, items: Dictionary | Required |  | Min Length: 1<br>Max Length: 2 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;id</samp>](## "underlay_ospf_authentication.message_digest_keys.[].id") | Integer | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hash_algorithm</samp>](## "underlay_ospf_authentication.message_digest_keys.[].hash_algorithm") | String |  | `sha512` | Valid Values:<br>- <code>md5</code><br>- <code>sha1</code><br>- <code>sha256</code><br>- <code>sha384</code><br>- <code>sha512</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key</samp>](## "underlay_ospf_authentication.message_digest_keys.[].key") <span style="color:red">deprecated</span> | String |  |  | Min Length: 1<br>Max Length: 16 | Cleartext key.<br>To protect the password at rest it is strongly recommended to make use of a vault or similar.<span style="color:red">This key is deprecated. Support will be removed in AVD version 6.0.0. Use <samp>cleartext_key</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cleartext_key</samp>](## "underlay_ospf_authentication.message_digest_keys.[].cleartext_key") | String |  |  | Min Length: 1<br>Max Length: 16 | Cleartext key for OSPF message-digest authentication<br>To protect the password at rest it is strongly recommended to make use of a vault or similar. |
    | [<samp>underlay_ospf_bfd_enable</samp>](## "underlay_ospf_bfd_enable") | Boolean |  | `False` |  |  |
    | [<samp>underlay_ospf_graceful_restart</samp>](## "underlay_ospf_graceful_restart") | Boolean |  | `False` |  | Enable graceful restart for OSPF underlay. |
    | [<samp>underlay_ospf_max_lsa</samp>](## "underlay_ospf_max_lsa") | Integer |  | `12000` |  |  |
    | [<samp>underlay_ospf_process_id</samp>](## "underlay_ospf_process_id") | Integer |  | `100` |  |  |

=== "YAML"

    ```yaml
    underlay_ospf_area: <str; default="0.0.0.0">
    underlay_ospf_authentication:
      enabled: <bool; default=False; required>
      message_digest_keys: # 1-2 items; required
        - id: <int; required; unique>
          hash_algorithm: <str; "md5" | "sha1" | "sha256" | "sha384" | "sha512"; default="sha512">

          # Cleartext key.
          # To protect the password at rest it is strongly recommended to make use of a vault or similar.
          # This key is deprecated.
          # Support will be removed in AVD version 6.0.0.
          # Use `cleartext_key` instead.
          key: <str; length 1-16>

          # Cleartext key for OSPF message-digest authentication
          # To protect the password at rest it is strongly recommended to make use of a vault or similar.
          cleartext_key: <str; length 1-16>
    underlay_ospf_bfd_enable: <bool; default=False>

    # Enable graceful restart for OSPF underlay.
    underlay_ospf_graceful_restart: <bool; default=False>
    underlay_ospf_max_lsa: <int; default=12000>
    underlay_ospf_process_id: <int; default=100>
    ```
