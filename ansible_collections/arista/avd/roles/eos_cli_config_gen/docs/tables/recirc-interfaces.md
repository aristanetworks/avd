<!--
  ~ Copyright (c) 2024 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>recirc_interfaces</samp>](## "recirc_interfaces") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;-&nbsp;name</samp>](## "recirc_interfaces.[].name") | String | Required, Unique |  |  | Recirculation interface name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "recirc_interfaces.[].description") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;shutdown</samp>](## "recirc_interfaces.[].shutdown") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;recirculation_features</samp>](## "recirc_interfaces.[].recirculation_features") | String |  |  | Valid Values:<br>- <code>vxlan</code><br>- <code>telemetry inband</code><br>- <code>openflow</code><br>- <code>cpu-mirror</code> | Set the feature that will use this port for recirculation. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;eos_cli</samp>](## "recirc_interfaces.[].eos_cli") | String |  |  |  | Multiline String with EOS CLI rendered directly on the Dps interface in the final EOS configuration. |

=== "YAML"

    ```yaml
    recirc_interfaces:

        # Recirculation interface name.
      - name: <str; required; unique>
        description: <str>
        shutdown: <bool>

        # Set the feature that will use this port for recirculation.
        recirculation_features: <str; "vxlan" | "telemetry inband" | "openflow" | "cpu-mirror">

        # Multiline String with EOS CLI rendered directly on the Dps interface in the final EOS configuration.
        eos_cli: <str>
    ```
