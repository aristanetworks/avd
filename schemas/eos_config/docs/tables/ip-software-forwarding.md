<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>ip_software_forwarding</samp>](## "ip_software_forwarding") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;mtu</samp>](## "ip_software_forwarding.mtu") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;size</samp>](## "ip_software_forwarding.mtu.size") | Integer |  |  | Min: 68<br>Max: 65535 | IPv4 software-forwarding MTU threshold in bytes.<br>Defaults to 1500 on EOS. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;exceed_action_drop</samp>](## "ip_software_forwarding.mtu.exceed_action_drop") | Boolean |  |  |  | Drop IPv4 packets larger than `mtu.size` in software.<br>Supported starting EOS 4.36.1F, 4.35.4M, 4.34.6M, 4.33.8M, 4.32.11M. |

=== "YAML"

    ```yaml
    ip_software_forwarding:
      mtu:

        # IPv4 software-forwarding MTU threshold in bytes.
        # Defaults to 1500 on EOS.
        size: <int; 68-65535>

        # Drop IPv4 packets larger than `mtu.size` in software.
        # Supported starting EOS 4.36.1F, 4.35.4M, 4.34.6M, 4.33.8M, 4.32.11M.
        exceed_action_drop: <bool>
    ```
