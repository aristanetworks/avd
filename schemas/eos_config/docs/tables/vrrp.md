<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>vrrp</samp>](## "vrrp") | Dictionary |  |  |  | Global VRRP configuration. |
    | [<samp>&nbsp;&nbsp;ipv4</samp>](## "vrrp.ipv4") | Dictionary |  |  |  | VRRP IPv4 configuration. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;authentication_anti_replay</samp>](## "vrrp.ipv4.authentication_anti_replay") | Boolean |  |  |  | Enable anti-replay validation for authenticated IPv4 VRRPv2 advertisements.<br>Supported in EOS starting 4.33.10M, 4.34.8M, 4.35.6M and 4.36.2F. |

=== "YAML"

    ```yaml
    # Global VRRP configuration.
    vrrp:

      # VRRP IPv4 configuration.
      ipv4:

        # Enable anti-replay validation for authenticated IPv4 VRRPv2 advertisements.
        # Supported in EOS starting 4.33.10M, 4.34.8M, 4.35.6M and 4.36.2F.
        authentication_anti_replay: <bool>
    ```
