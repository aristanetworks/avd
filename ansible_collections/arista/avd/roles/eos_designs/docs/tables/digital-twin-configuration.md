<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>digital_twin</samp>](## "digital_twin") | Dictionary |  |  |  | PREVIEW: This option is marked as "preview", meaning the data models or generated configuration can change at any time.<br>Global settings to configure the Digital Twin of the Fabric. |
    | [<samp>&nbsp;&nbsp;environment</samp>](## "digital_twin.environment") | String |  | `act` | Valid Values:<br>- <code>act</code> | Targeted Digital Twin environment. |
    | [<samp>&nbsp;&nbsp;fabric</samp>](## "digital_twin.fabric") | Dictionary | Required |  |  | Global Digital Twin settings related to the configuration of fabric nodes. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;os_version</samp>](## "digital_twin.fabric.os_version") | String |  |  |  | Desired Digital Twin OS version for fabric nodes. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;username</samp>](## "digital_twin.fabric.username") | String | Required |  |  | Desired Digital Twin username for fabric nodes. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;password</samp>](## "digital_twin.fabric.password") | String | Required |  |  | Desired Digital Twin clear-text password for fabric nodes. |
    | [<samp>digital_twin_mode</samp>](## "digital_twin_mode") | Boolean |  | `False` |  | PREVIEW: This option is marked as "preview", meaning the data models or generated configuration can change at any time.<br>Enable generation of the Digital Twin version of the fabric (Digital Twin topology, adjusted configuration, etc.).<br>`digital_twin.enabled` must also be set to `true` under the nodes that are to be included in Digital Twin metadata.<br>Devices that are not enabled will be configured as `is_deployed: false` to ensure all interfaces and peerings towards them are shutdown. |

=== "YAML"

    ```yaml
    # PREVIEW: This option is marked as "preview", meaning the data models or generated configuration can change at any time.
    # Global settings to configure the Digital Twin of the Fabric.
    digital_twin:

      # Targeted Digital Twin environment.
      environment: <str; "act"; default="act">

      # Global Digital Twin settings related to the configuration of fabric nodes.
      fabric: # required

        # Desired Digital Twin OS version for fabric nodes.
        os_version: <str>

        # Desired Digital Twin username for fabric nodes.
        username: <str; required>

        # Desired Digital Twin clear-text password for fabric nodes.
        password: <str; required>

    # PREVIEW: This option is marked as "preview", meaning the data models or generated configuration can change at any time.
    # Enable generation of the Digital Twin version of the fabric (Digital Twin topology, adjusted configuration, etc.).
    # `digital_twin.enabled` must also be set to `true` under the nodes that are to be included in Digital Twin metadata.
    # Devices that are not enabled will be configured as `is_deployed: false` to ensure all interfaces and peerings towards them are shutdown.
    digital_twin_mode: <bool; default=False>
    ```
