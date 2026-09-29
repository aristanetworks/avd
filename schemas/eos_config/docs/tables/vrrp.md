<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>vrrp</samp>](## "vrrp") | Dictionary |  |  |  | Global VRRP configuration. |
    | [<samp>&nbsp;&nbsp;ipv4</samp>](## "vrrp.ipv4") | Dictionary |  |  |  | VRRPv2 IPv4 Authentication configuration. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;authentication_anti_replay</samp>](## "vrrp.ipv4.authentication_anti_replay") | Boolean | Required |  |  | Enable AH sequence number validation. |

=== "YAML"

    ```yaml
    # Global VRRP configuration.
    vrrp:

      # VRRPv2 IPv4 Authentication configuration.
      ipv4:

        # Enable AH sequence number validation.
        authentication_anti_replay: <bool; required>
    ```
