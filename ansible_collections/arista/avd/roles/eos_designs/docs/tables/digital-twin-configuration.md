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
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;act_username</samp>](## "digital_twin.fabric.act_username") | String |  | `admin` |  | Username for ACT Digital Twin fabric devices. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;act_password</samp>](## "digital_twin.fabric.act_password") | String |  | `admin` |  | Cleartext password for ACT Digital Twin fabric devices. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;act_ensure_eapi_access</samp>](## "digital_twin.fabric.act_ensure_eapi_access") | Boolean |  | `False` |  | Enforces generated Digital Twin version of the EOS configuration for `veos` and `cloudeos` node types to always allow eAPI management over HTTPS in default VRF.<br>By default, ACT allocates a dedicated private (RFC1918) management IP address to each deployed node, which is routable only over the ACT VPN. This interface provides both eAPI and SSH access.<br>If a virtual vEOS or CloudEOS device's configuration later disables the eAPI service in the default VRF, it will also block ACT's eAPI access to the device. This prevents all eAPI access through the dedicated management interface, including access from the ACT UI's `command-api` and direct eAPI calls over the ACT VPN.<br>When this key is set to `True`, the generated Digital Twin configuration (`management api http-commands` section) will be updated to enable the eAPI service over HTTPS in the default VRF, ensuring access is maintained.<br>No adjustments are needed for the SSH service, as its access via the dedicated management interface cannot be blocked by the `management ssh` EOS configuration. |

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
        act_username: <str; default="admin">

        # Cleartext password for ACT Digital Twin fabric devices.
        act_password: <str; default="admin">

        # Enforces generated Digital Twin version of the EOS configuration for `veos` and `cloudeos` node types to always allow eAPI management over HTTPS in default VRF.
        # By default, ACT allocates a dedicated private (RFC1918) management IP address to each deployed node, which is routable only over the ACT VPN. This interface provides both eAPI and SSH access.
        # If a virtual vEOS or CloudEOS device's configuration later disables the eAPI service in the default VRF, it will also block ACT's eAPI access to the device. This prevents all eAPI access through the dedicated management interface, including access from the ACT UI's `command-api` and direct eAPI calls over the ACT VPN.
        # When this key is set to `True`, the generated Digital Twin configuration (`management api http-commands` section) will be updated to enable the eAPI service over HTTPS in the default VRF, ensuring access is maintained.
        # No adjustments are needed for the SSH service, as its access via the dedicated management interface cannot be blocked by the `management ssh` EOS configuration.
        act_ensure_eapi_access: <bool; default=False>
    ```
