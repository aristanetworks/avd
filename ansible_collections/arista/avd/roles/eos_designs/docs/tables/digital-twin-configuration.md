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
    | [<samp>&nbsp;&nbsp;fabric</samp>](## "digital_twin.fabric") | Dictionary | Required |  |  | Settings for Digital Twin fabric devices. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;act_os_version</samp>](## "digital_twin.fabric.act_os_version") | String |  |  |  | OS version for ACT Digital Twin fabric devices. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;act_username</samp>](## "digital_twin.fabric.act_username") | String |  | `cvpadmin` |  | Username for ACT Digital Twin fabric devices. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;act_password</samp>](## "digital_twin.fabric.act_password") | String |  | `cvp123!` |  | Cleartext password for ACT Digital Twin fabric devices. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;act_internet_access</samp>](## "digital_twin.fabric.act_internet_access") | Boolean |  | `False` |  | Specifies if the ACT Digital Twin device is deployed with direct access to the Internet.<br>This option applies only to the 'cloudeos' and 'veos' node types and will be ignored for all other ACT node types.<br>ACT does not provide direct Internet access to cloudeos or veos devices by default. |
    | [<samp>&nbsp;&nbsp;use_default_interfaces_of_digital_twin_platform</samp>](## "digital_twin.use_default_interfaces_of_digital_twin_platform") | Boolean |  | `False` |  | In Digital Twin mode, AVD can either use the default interfaces of the original or the digital twin platform (as set in `platform_settings.[].digital_twin.platform`). |

=== "YAML"

    ```yaml
    # PREVIEW: This option is marked as "preview", meaning the data models or generated configuration can change at any time.
    # Global settings to configure the Digital Twin of the Fabric.
    digital_twin:

      # Targeted Digital Twin environment.
      environment: <str; "act"; default="act">

      # Settings for Digital Twin fabric devices.
      fabric: # required

        # OS version for ACT Digital Twin fabric devices.
        act_os_version: <str>

        # Username for ACT Digital Twin fabric devices.
        act_username: <str; default="cvpadmin">

        # Cleartext password for ACT Digital Twin fabric devices.
        act_password: <str; default="cvp123!">

        # Specifies if the ACT Digital Twin device is deployed with direct access to the Internet.
        # This option applies only to the 'cloudeos' and 'veos' node types and will be ignored for all other ACT node types.
        # ACT does not provide direct Internet access to cloudeos or veos devices by default.
        act_internet_access: <bool; default=False>

      # In Digital Twin mode, AVD can either use the default interfaces of the original or the digital twin platform (as set in `platform_settings.[].digital_twin.platform`).
      use_default_interfaces_of_digital_twin_platform: <bool; default=False>
    ```
