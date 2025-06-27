<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>digital_twin</samp>](## "digital_twin") | Dictionary |  |  |  | PREVIEW: This option is marked as "preview", meaning the data models or generated configuration can change at any time.<br>Global settings to configure the Digital Twin of the Fabric.<br>These settings are required when `avd_digital_twin_mode` is `true` |
    | [<samp>&nbsp;&nbsp;environment</samp>](## "digital_twin.environment") | String |  | `act` | Valid Values:<br>- <code>act</code> | Targeted Digital Twin environment. |
    | [<samp>&nbsp;&nbsp;fabric</samp>](## "digital_twin.fabric") | Dictionary | Required |  |  | Settings for Digital Twin fabric devices. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;os_version</samp>](## "digital_twin.fabric.os_version") | String |  |  |  | OS version for Digital Twin fabric devices. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;username</samp>](## "digital_twin.fabric.username") | String | Required |  |  | Username for Digital Twin fabric devices. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;password</samp>](## "digital_twin.fabric.password") | String | Required |  |  | Cleartext password for Digital Twin fabric devices. |

=== "YAML"

    ```yaml
    # PREVIEW: This option is marked as "preview", meaning the data models or generated configuration can change at any time.
    # Global settings to configure the Digital Twin of the Fabric.
    # These settings are required when `avd_digital_twin_mode` is `true`
    digital_twin:

      # Targeted Digital Twin environment.
      environment: <str; "act"; default="act">

      # Settings for Digital Twin fabric devices.
      fabric: # required

        # OS version for Digital Twin fabric devices.
        os_version: <str>

        # Username for Digital Twin fabric devices.
        username: <str; required>

        # Cleartext password for Digital Twin fabric devices.
        password: <str; required>
    ```
