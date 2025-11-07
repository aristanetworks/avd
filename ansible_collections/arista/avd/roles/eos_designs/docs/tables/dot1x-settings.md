<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>dot1x_settings</samp>](## "dot1x_settings") | Dictionary |  |  |  | Settings for 802.1X deployments. |
    | [<samp>&nbsp;&nbsp;enabled</samp>](## "dot1x_settings.enabled") | Boolean |  | `False` |  | Enable 802.1X port authentication on the switch. |
    | [<samp>&nbsp;&nbsp;protocol_bypasses</samp>](## "dot1x_settings.protocol_bypasses") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;bpdu</samp>](## "dot1x_settings.protocol_bypasses.bpdu") | Boolean |  | `True` |  | Allow BPDU packets from unauthenticated hosts/mac to be used for loop detection. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;lldp</samp>](## "dot1x_settings.protocol_bypasses.lldp") | Boolean |  | `True` |  | Allow LLDP packets to be processed even if the port is not authenticated. |
    | [<samp>&nbsp;&nbsp;dynamic_authorization</samp>](## "dot1x_settings.dynamic_authorization") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "dot1x_settings.dynamic_authorization.enabled") | Boolean |  | `True` |  | Enable RADIUS CoA (Change of Authorization) requests to be received to allow a RADIUS server to adjust an active client session. |

=== "YAML"

    ```yaml
    # Settings for 802.1X deployments.
    dot1x_settings:

      # Enable 802.1X port authentication on the switch.
      enabled: <bool; default=False>
      protocol_bypasses:

        # Allow BPDU packets from unauthenticated hosts/mac to be used for loop detection.
        bpdu: <bool; default=True>

        # Allow LLDP packets to be processed even if the port is not authenticated.
        lldp: <bool; default=True>
      dynamic_authorization:

        # Enable RADIUS CoA (Change of Authorization) requests to be received to allow a RADIUS server to adjust an active client session.
        enabled: <bool; default=True>
    ```
