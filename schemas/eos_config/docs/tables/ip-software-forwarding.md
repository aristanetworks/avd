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
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;exceed_action_drop</samp>](## "ip_software_forwarding.mtu.exceed_action_drop") | Boolean |  |  |  | Drop packets that exceed the MTU on software-forwarded paths.<br>Introduced in EOS 4.36.1F, 4.35.4M, 4.34.6M, 4.33.8M, 4.32.11M to mitigate Security Advisory 0142. |

=== "YAML"

    ```yaml
    ip_software_forwarding:
      mtu:

        # Drop packets that exceed the MTU on software-forwarded paths.
        # Introduced in EOS 4.36.1F, 4.35.4M, 4.34.6M, 4.33.8M, 4.32.11M to mitigate Security Advisory 0142.
        exceed_action_drop: <bool>
    ```
