<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>vrrp</samp>](## "vrrp") | Dictionary |  |  |  | Global VRRP configuration. |
    | [<samp>&nbsp;&nbsp;ipv4</samp>](## "vrrp.ipv4") | Dictionary |  |  |  | VRRPv2 IPv4 Authentication configuration.<br>Introduced in EOS 4.36.2F, 4.35.6M, 4.34.8M, 4.33.10M. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;authentication_anti_replay</samp>](## "vrrp.ipv4.authentication_anti_replay") | Boolean |  |  |  | Enable anti-replay validation for authenticated IPv4 VRRPv2 advertisements. |

=== "YAML"

    ```yaml
    # Global VRRP configuration.
    vrrp:

      # VRRPv2 IPv4 Authentication configuration.
      # Introduced in EOS 4.36.2F, 4.35.6M, 4.34.8M, 4.33.10M.
      ipv4:

        # Enable anti-replay validation for authenticated IPv4 VRRPv2 advertisements.
        authentication_anti_replay: <bool>
    ```
