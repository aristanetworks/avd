<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>digital_twin</samp>](## "digital_twin") | Dictionary |  |  |  | PREVIEW: This option is marked as "preview", meaning the data models or generated configuration can change at any time.<br>Global settings to configure the Digital Twin of the Fabric. |
    | [<samp>&nbsp;&nbsp;environment</samp>](## "digital_twin.environment") | String |  | `act` | Valid Values:<br>- <code>act</code><br>- <code>containerlab</code> | Targeted Digital Twin environment. |
    | [<samp>&nbsp;&nbsp;fabric</samp>](## "digital_twin.fabric") | Dictionary | Required |  |  | Settings for Digital Twin fabric devices. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;act_os_version</samp>](## "digital_twin.fabric.act_os_version") | String |  |  |  | OS version for ACT Digital Twin fabric devices. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;act_username</samp>](## "digital_twin.fabric.act_username") | String |  | `cvpadmin` |  | Username for ACT Digital Twin fabric devices. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;act_password</samp>](## "digital_twin.fabric.act_password") | String |  | `cvp123!` |  | Cleartext password for ACT Digital Twin fabric devices. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;act_internet_access</samp>](## "digital_twin.fabric.act_internet_access") | Boolean |  | `False` |  | Specifies if the ACT Digital Twin device is deployed with direct access to the Internet.<br>This option applies only to the 'cloudeos' and 'veos' node types and will be ignored for all other ACT node types.<br>ACT does not provide direct Internet access to cloudeos or veos devices by default. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;act_ensure_eapi_access</samp>](## "digital_twin.fabric.act_ensure_eapi_access") | Boolean |  | `False` |  | Ensures eAPI remains accessible for automation and testing via ACT.<br>Clients connecting to device eAPI through ACT rely on access in the default VRF. If eAPI is reconfigured for a dedicated management VRF, this primary eAPI connectivity can be unintentionally broken.<br>Set this to `true` to enforce the required EOS configuration, guaranteeing eAPI over HTTPS is always enabled in the default VRF and preserving this connectivity.<br>Any IPv4 ACL applied to eAPI in the default VRF is removed. IPv6 ACLs and eAPI configuration for non-default VRFs are preserved. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;act_ensure_ssh_access</samp>](## "digital_twin.fabric.act_ensure_ssh_access") | Boolean |  | `False` |  | Ensures SSH remains accessible for automation and testing via ACT.<br>Clients connecting to device SSH through ACT rely on access in the default VRF. If SSH is disabled globally or in the default VRF (takes precedence over global setting), this primary SSH connectivity can be unintentionally broken.<br>Set this to `true` to enforce the required EOS configuration, guaranteeing SSH is enabled in the default VRF and preserving this connectivity.<br>Any IPv4 ACL applied to SSH in the default VRF is removed. IPv6 ACLs and SSH configuration for non-default VRFs are preserved. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;serial_number</samp>](## "digital_twin.fabric.serial_number") | String |  |  | Min Length: 1 | AVD string formatter template for generating the serial number of ACT Digital Twin devices.<br>When set, the rendered value is written into the device metadata and provided as the serial number in the ACT topology.<br>Can be overridden per device with `digital_twin.serial_number` at node level.<br>Supported template variables: `serial_number` (production serial number), `system_mac_address` (resolved production system MAC address), `hostname`, `device_id`, `fabric_name`.<br>The rendered value should be unique across all devices in the fabric. AVD does not enforce uniqueness automatically.<br>If unset, no serial number is included in the metadata or the ACT topology.<br>Applies only to `veos` and `cloudeos` node types. Ignored for all other ACT node types.<br>Ignored when `digital_twin.environment` is `containerlab`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;system_mac_address</samp>](## "digital_twin.fabric.system_mac_address") | String |  |  | Min Length: 1 | AVD string formatter template for generating the system MAC address of ACT Digital Twin devices.<br>When set, the rendered value is used throughout the device's EOS configuration (e.g., SNMPv3 engine ID), written into the device metadata, and provided as the system MAC address in the ACT topology.<br>Can be overridden per device with `digital_twin.system_mac_address` at node level.<br>Supported template variables: `serial_number` (production serial number), `system_mac_address` (production system MAC address), `hostname`, `device_id`, `fabric_name`.<br>The rendered value must be a unicast MAC address in `hhhh.hhhh.hhhh`, `hh:hh:hh:hh:hh:hh` or `hhhhhhhhhhhh` format (where `h` is a hexadecimal digit). The all-zero address is reserved and not accepted by EOS.<br>Regardless of the input format, the MAC address is normalized to `hh:hh:hh:hh:hh:hh` format.<br>The rendered value should be unique across all devices in the fabric. AVD does not enforce uniqueness automatically.<br>If unset, no system MAC address is included in the metadata or the ACT topology, and the production `system_mac_address` is used for EOS configuration.<br>Applies only to `veos` and `cloudeos` node types. Ignored for all other ACT node types.<br>Ignored when `digital_twin.environment` is `containerlab`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ztp</samp>](## "digital_twin.fabric.ztp") | Boolean |  | `False` |  | Enable ZTP (Zero Touch Provisioning) mode for all Digital Twin devices.<br>Can be overridden by `digital_twin.ztp` at node level.<br>Supported Digital Twin environments:<br>- `act`: Applies only to `veos` and `cloudeos` node types. Ignored for all other node types. |
    | [<samp>&nbsp;&nbsp;use_default_interfaces_of_digital_twin_platform</samp>](## "digital_twin.use_default_interfaces_of_digital_twin_platform") | Boolean |  | `False` |  | In Digital Twin mode, AVD can either use the default interfaces of the original or the digital twin platform (as set in `platform_settings.[].digital_twin.platform`). |

=== "YAML"

    ```yaml
    # PREVIEW: This option is marked as "preview", meaning the data models or generated configuration can change at any time.
    # Global settings to configure the Digital Twin of the Fabric.
    digital_twin:

      # Targeted Digital Twin environment.
      environment: <str; "act" | "containerlab"; default="act">

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

        # Ensures eAPI remains accessible for automation and testing via ACT.
        # Clients connecting to device eAPI through ACT rely on access in the default VRF. If eAPI is reconfigured for a dedicated management VRF, this primary eAPI connectivity can be unintentionally broken.
        # Set this to `true` to enforce the required EOS configuration, guaranteeing eAPI over HTTPS is always enabled in the default VRF and preserving this connectivity.
        # Any IPv4 ACL applied to eAPI in the default VRF is removed. IPv6 ACLs and eAPI configuration for non-default VRFs are preserved.
        act_ensure_eapi_access: <bool; default=False>

        # Ensures SSH remains accessible for automation and testing via ACT.
        # Clients connecting to device SSH through ACT rely on access in the default VRF. If SSH is disabled globally or in the default VRF (takes precedence over global setting), this primary SSH connectivity can be unintentionally broken.
        # Set this to `true` to enforce the required EOS configuration, guaranteeing SSH is enabled in the default VRF and preserving this connectivity.
        # Any IPv4 ACL applied to SSH in the default VRF is removed. IPv6 ACLs and SSH configuration for non-default VRFs are preserved.
        act_ensure_ssh_access: <bool; default=False>

        # AVD string formatter template for generating the serial number of ACT Digital Twin devices.
        # When set, the rendered value is written into the device metadata and provided as the serial number in the ACT topology.
        # Can be overridden per device with `digital_twin.serial_number` at node level.
        # Supported template variables: `serial_number` (production serial number), `system_mac_address` (resolved production system MAC address), `hostname`, `device_id`, `fabric_name`.
        # The rendered value should be unique across all devices in the fabric. AVD does not enforce uniqueness automatically.
        # If unset, no serial number is included in the metadata or the ACT topology.
        # Applies only to `veos` and `cloudeos` node types. Ignored for all other ACT node types.
        # Ignored when `digital_twin.environment` is `containerlab`.
        serial_number: <str; length >=1>

        # AVD string formatter template for generating the system MAC address of ACT Digital Twin devices.
        # When set, the rendered value is used throughout the device's EOS configuration (e.g., SNMPv3 engine ID), written into the device metadata, and provided as the system MAC address in the ACT topology.
        # Can be overridden per device with `digital_twin.system_mac_address` at node level.
        # Supported template variables: `serial_number` (production serial number), `system_mac_address` (production system MAC address), `hostname`, `device_id`, `fabric_name`.
        # The rendered value must be a unicast MAC address in `hhhh.hhhh.hhhh`, `hh:hh:hh:hh:hh:hh` or `hhhhhhhhhhhh` format (where `h` is a hexadecimal digit). The all-zero address is reserved and not accepted by EOS.
        # Regardless of the input format, the MAC address is normalized to `hh:hh:hh:hh:hh:hh` format.
        # The rendered value should be unique across all devices in the fabric. AVD does not enforce uniqueness automatically.
        # If unset, no system MAC address is included in the metadata or the ACT topology, and the production `system_mac_address` is used for EOS configuration.
        # Applies only to `veos` and `cloudeos` node types. Ignored for all other ACT node types.
        # Ignored when `digital_twin.environment` is `containerlab`.
        system_mac_address: <str; length >=1>

        # Enable ZTP (Zero Touch Provisioning) mode for all Digital Twin devices.
        # Can be overridden by `digital_twin.ztp` at node level.
        # Supported Digital Twin environments:
        # - `act`: Applies only to `veos` and `cloudeos` node types. Ignored for all other node types.
        ztp: <bool; default=False>

      # In Digital Twin mode, AVD can either use the default interfaces of the original or the digital twin platform (as set in `platform_settings.[].digital_twin.platform`).
      use_default_interfaces_of_digital_twin_platform: <bool; default=False>
    ```
