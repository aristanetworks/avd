<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>&lt;node_type_keys.key&gt;</samp>](## "<node_type_keys.key>") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;defaults</samp>](## "<node_type_keys.key>.defaults") | Dictionary |  |  |  | Define variables for all nodes of this type. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;digital_twin</samp>](## "<node_type_keys.key>.defaults.digital_twin") | Dictionary |  |  |  | PREVIEW: This option is marked as "preview", meaning the data models or generated configuration can change at any time.<br>Set the OS version, management IP address, and management gateway for the digital twin of the associated node(s). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;act_os_version</samp>](## "<node_type_keys.key>.defaults.digital_twin.act_os_version") | String |  |  |  | Desired ACT Digital Twin OS version.<br>Overrides global `digital_twin.fabric.act_os_version` flag. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mgmt_ip</samp>](## "<node_type_keys.key>.defaults.digital_twin.mgmt_ip") | String |  |  | Format: cidr | Desired management interface IPv4 address for the Digital Twin.<br>In ACT Digital Twin mode, this address is used in the ACT topology.<br>If the regular `mgmt_ip` is set, this `digital_twin.mgmt_ip` address is also used for the generated OOB management interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mgmt_gateway</samp>](## "<node_type_keys.key>.defaults.digital_twin.mgmt_gateway") | String |  |  |  | Desired OOB management gateway for the Digital Twin.<br>In ACT Digital Twin mode, if the regular `mgmt_ip` is set, this `digital_twin.mgmt_gateway` address takes precedence over the regular management gateway for the generated OOB management interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;act_internet_access</samp>](## "<node_type_keys.key>.defaults.digital_twin.act_internet_access") | Boolean |  |  |  | Specifies if the ACT Digital Twin device is deployed with direct access to the Internet.<br>This option applies only to the 'cloudeos' and 'veos' node types and will be ignored for all other ACT node types.<br>ACT does not provide direct Internet access to cloudeos or veos devices by default.<br>Overrides global `digital_twin.fabric.act_internet_access` flag. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hardware_identity</samp>](## "<node_type_keys.key>.defaults.digital_twin.hardware_identity") | Dictionary |  |  |  | Settings controlling use of hardware identity values for the Digital Twin device.<br>Each setting overrides the corresponding global `digital_twin.fabric.hardware_identity` setting when defined. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;serial_number</samp>](## "<node_type_keys.key>.defaults.digital_twin.hardware_identity.serial_number") | Boolean |  |  |  | When set to `true`, provides the resolved device serial number as an input value to the Digital Twin environment.<br>A per-node `digital_twin.serial_number` value overrides the regular device `serial_number` for the Digital Twin device.<br>Supported Digital Twin environments:<br>- `act`: Applies only to `veos` and `cloudeos` node types. Ignored for all other node types. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;system_mac_address</samp>](## "<node_type_keys.key>.defaults.digital_twin.hardware_identity.system_mac_address") | Boolean |  |  |  | When set to `true`, provides the resolved device system MAC address as an input value to the Digital Twin environment.<br>A per-node `digital_twin.system_mac_address` value overrides the regular device `system_mac_address` for the Digital Twin device.<br>Supported Digital Twin environments:<br>- `act`: Applies only to `veos` and `cloudeos` node types. Ignored for all other node types. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;serial_number</samp>](## "<node_type_keys.key>.defaults.digital_twin.serial_number") | String |  |  |  | Serial number override for this Digital Twin device.<br>Used when `digital_twin.hardware_identity.serial_number` is set to `true`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;system_mac_address</samp>](## "<node_type_keys.key>.defaults.digital_twin.system_mac_address") | String |  |  |  | System MAC address override for this Digital Twin device.<br>Used when `digital_twin.hardware_identity.system_mac_address` is set to `true`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ztp</samp>](## "<node_type_keys.key>.defaults.digital_twin.ztp") | Boolean |  |  |  | Enable ZTP (Zero Touch Provisioning) mode for this Digital Twin device.<br>Supported Digital Twin environments:<br>- `act`: Applies only to `veos` and `cloudeos` node types. Ignored for all other node types.<br>Overrides global `digital_twin.fabric.ztp` when defined. |
    | [<samp>&nbsp;&nbsp;node_groups</samp>](## "<node_type_keys.key>.node_groups") | List, items: Dictionary |  |  |  | Define variables related to all nodes part of this group. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;group</samp>](## "<node_type_keys.key>.node_groups.[].group") | String | Required, Unique |  |  | The Node Group Name is used for MLAG domain unless set with 'mlag_domain_id'.<br>The Node Group Name is also used for peer description on downstream switches' uplinks.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "<node_type_keys.key>.node_groups.[].nodes") | List, items: Dictionary |  |  |  | Define variables per node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].name") | String | Required, Unique |  |  | The Node Name is used as "hostname". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;digital_twin</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].digital_twin") | Dictionary |  |  |  | PREVIEW: This option is marked as "preview", meaning the data models or generated configuration can change at any time.<br>Set the OS version, management IP address, and management gateway for the digital twin of the associated node(s). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;act_os_version</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].digital_twin.act_os_version") | String |  |  |  | Desired ACT Digital Twin OS version.<br>Overrides global `digital_twin.fabric.act_os_version` flag. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mgmt_ip</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].digital_twin.mgmt_ip") | String |  |  | Format: cidr | Desired management interface IPv4 address for the Digital Twin.<br>In ACT Digital Twin mode, this address is used in the ACT topology.<br>If the regular `mgmt_ip` is set, this `digital_twin.mgmt_ip` address is also used for the generated OOB management interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mgmt_gateway</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].digital_twin.mgmt_gateway") | String |  |  |  | Desired OOB management gateway for the Digital Twin.<br>In ACT Digital Twin mode, if the regular `mgmt_ip` is set, this `digital_twin.mgmt_gateway` address takes precedence over the regular management gateway for the generated OOB management interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;act_internet_access</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].digital_twin.act_internet_access") | Boolean |  |  |  | Specifies if the ACT Digital Twin device is deployed with direct access to the Internet.<br>This option applies only to the 'cloudeos' and 'veos' node types and will be ignored for all other ACT node types.<br>ACT does not provide direct Internet access to cloudeos or veos devices by default.<br>Overrides global `digital_twin.fabric.act_internet_access` flag. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hardware_identity</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].digital_twin.hardware_identity") | Dictionary |  |  |  | Settings controlling use of hardware identity values for the Digital Twin device.<br>Each setting overrides the corresponding global `digital_twin.fabric.hardware_identity` setting when defined. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;serial_number</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].digital_twin.hardware_identity.serial_number") | Boolean |  |  |  | When set to `true`, provides the resolved device serial number as an input value to the Digital Twin environment.<br>A per-node `digital_twin.serial_number` value overrides the regular device `serial_number` for the Digital Twin device.<br>Supported Digital Twin environments:<br>- `act`: Applies only to `veos` and `cloudeos` node types. Ignored for all other node types. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;system_mac_address</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].digital_twin.hardware_identity.system_mac_address") | Boolean |  |  |  | When set to `true`, provides the resolved device system MAC address as an input value to the Digital Twin environment.<br>A per-node `digital_twin.system_mac_address` value overrides the regular device `system_mac_address` for the Digital Twin device.<br>Supported Digital Twin environments:<br>- `act`: Applies only to `veos` and `cloudeos` node types. Ignored for all other node types. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;serial_number</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].digital_twin.serial_number") | String |  |  |  | Serial number override for this Digital Twin device.<br>Used when `digital_twin.hardware_identity.serial_number` is set to `true`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;system_mac_address</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].digital_twin.system_mac_address") | String |  |  |  | System MAC address override for this Digital Twin device.<br>Used when `digital_twin.hardware_identity.system_mac_address` is set to `true`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ztp</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].digital_twin.ztp") | Boolean |  |  |  | Enable ZTP (Zero Touch Provisioning) mode for this Digital Twin device.<br>Supported Digital Twin environments:<br>- `act`: Applies only to `veos` and `cloudeos` node types. Ignored for all other node types.<br>Overrides global `digital_twin.fabric.ztp` when defined. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;digital_twin</samp>](## "<node_type_keys.key>.node_groups.[].digital_twin") | Dictionary |  |  |  | PREVIEW: This option is marked as "preview", meaning the data models or generated configuration can change at any time.<br>Set the OS version, management IP address, and management gateway for the digital twin of the associated node(s). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;act_os_version</samp>](## "<node_type_keys.key>.node_groups.[].digital_twin.act_os_version") | String |  |  |  | Desired ACT Digital Twin OS version.<br>Overrides global `digital_twin.fabric.act_os_version` flag. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mgmt_ip</samp>](## "<node_type_keys.key>.node_groups.[].digital_twin.mgmt_ip") | String |  |  | Format: cidr | Desired management interface IPv4 address for the Digital Twin.<br>In ACT Digital Twin mode, this address is used in the ACT topology.<br>If the regular `mgmt_ip` is set, this `digital_twin.mgmt_ip` address is also used for the generated OOB management interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mgmt_gateway</samp>](## "<node_type_keys.key>.node_groups.[].digital_twin.mgmt_gateway") | String |  |  |  | Desired OOB management gateway for the Digital Twin.<br>In ACT Digital Twin mode, if the regular `mgmt_ip` is set, this `digital_twin.mgmt_gateway` address takes precedence over the regular management gateway for the generated OOB management interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;act_internet_access</samp>](## "<node_type_keys.key>.node_groups.[].digital_twin.act_internet_access") | Boolean |  |  |  | Specifies if the ACT Digital Twin device is deployed with direct access to the Internet.<br>This option applies only to the 'cloudeos' and 'veos' node types and will be ignored for all other ACT node types.<br>ACT does not provide direct Internet access to cloudeos or veos devices by default.<br>Overrides global `digital_twin.fabric.act_internet_access` flag. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hardware_identity</samp>](## "<node_type_keys.key>.node_groups.[].digital_twin.hardware_identity") | Dictionary |  |  |  | Settings controlling use of hardware identity values for the Digital Twin device.<br>Each setting overrides the corresponding global `digital_twin.fabric.hardware_identity` setting when defined. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;serial_number</samp>](## "<node_type_keys.key>.node_groups.[].digital_twin.hardware_identity.serial_number") | Boolean |  |  |  | When set to `true`, provides the resolved device serial number as an input value to the Digital Twin environment.<br>A per-node `digital_twin.serial_number` value overrides the regular device `serial_number` for the Digital Twin device.<br>Supported Digital Twin environments:<br>- `act`: Applies only to `veos` and `cloudeos` node types. Ignored for all other node types. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;system_mac_address</samp>](## "<node_type_keys.key>.node_groups.[].digital_twin.hardware_identity.system_mac_address") | Boolean |  |  |  | When set to `true`, provides the resolved device system MAC address as an input value to the Digital Twin environment.<br>A per-node `digital_twin.system_mac_address` value overrides the regular device `system_mac_address` for the Digital Twin device.<br>Supported Digital Twin environments:<br>- `act`: Applies only to `veos` and `cloudeos` node types. Ignored for all other node types. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;serial_number</samp>](## "<node_type_keys.key>.node_groups.[].digital_twin.serial_number") | String |  |  |  | Serial number override for this Digital Twin device.<br>Used when `digital_twin.hardware_identity.serial_number` is set to `true`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;system_mac_address</samp>](## "<node_type_keys.key>.node_groups.[].digital_twin.system_mac_address") | String |  |  |  | System MAC address override for this Digital Twin device.<br>Used when `digital_twin.hardware_identity.system_mac_address` is set to `true`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ztp</samp>](## "<node_type_keys.key>.node_groups.[].digital_twin.ztp") | Boolean |  |  |  | Enable ZTP (Zero Touch Provisioning) mode for this Digital Twin device.<br>Supported Digital Twin environments:<br>- `act`: Applies only to `veos` and `cloudeos` node types. Ignored for all other node types.<br>Overrides global `digital_twin.fabric.ztp` when defined. |
    | [<samp>&nbsp;&nbsp;nodes</samp>](## "<node_type_keys.key>.nodes") | List, items: Dictionary |  |  |  | Define variables per node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "<node_type_keys.key>.nodes.[].name") | String | Required, Unique |  |  | The Node Name is used as "hostname". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;digital_twin</samp>](## "<node_type_keys.key>.nodes.[].digital_twin") | Dictionary |  |  |  | PREVIEW: This option is marked as "preview", meaning the data models or generated configuration can change at any time.<br>Set the OS version, management IP address, and management gateway for the digital twin of the associated node(s). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;act_os_version</samp>](## "<node_type_keys.key>.nodes.[].digital_twin.act_os_version") | String |  |  |  | Desired ACT Digital Twin OS version.<br>Overrides global `digital_twin.fabric.act_os_version` flag. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mgmt_ip</samp>](## "<node_type_keys.key>.nodes.[].digital_twin.mgmt_ip") | String |  |  | Format: cidr | Desired management interface IPv4 address for the Digital Twin.<br>In ACT Digital Twin mode, this address is used in the ACT topology.<br>If the regular `mgmt_ip` is set, this `digital_twin.mgmt_ip` address is also used for the generated OOB management interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mgmt_gateway</samp>](## "<node_type_keys.key>.nodes.[].digital_twin.mgmt_gateway") | String |  |  |  | Desired OOB management gateway for the Digital Twin.<br>In ACT Digital Twin mode, if the regular `mgmt_ip` is set, this `digital_twin.mgmt_gateway` address takes precedence over the regular management gateway for the generated OOB management interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;act_internet_access</samp>](## "<node_type_keys.key>.nodes.[].digital_twin.act_internet_access") | Boolean |  |  |  | Specifies if the ACT Digital Twin device is deployed with direct access to the Internet.<br>This option applies only to the 'cloudeos' and 'veos' node types and will be ignored for all other ACT node types.<br>ACT does not provide direct Internet access to cloudeos or veos devices by default.<br>Overrides global `digital_twin.fabric.act_internet_access` flag. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hardware_identity</samp>](## "<node_type_keys.key>.nodes.[].digital_twin.hardware_identity") | Dictionary |  |  |  | Settings controlling use of hardware identity values for the Digital Twin device.<br>Each setting overrides the corresponding global `digital_twin.fabric.hardware_identity` setting when defined. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;serial_number</samp>](## "<node_type_keys.key>.nodes.[].digital_twin.hardware_identity.serial_number") | Boolean |  |  |  | When set to `true`, provides the resolved device serial number as an input value to the Digital Twin environment.<br>A per-node `digital_twin.serial_number` value overrides the regular device `serial_number` for the Digital Twin device.<br>Supported Digital Twin environments:<br>- `act`: Applies only to `veos` and `cloudeos` node types. Ignored for all other node types. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;system_mac_address</samp>](## "<node_type_keys.key>.nodes.[].digital_twin.hardware_identity.system_mac_address") | Boolean |  |  |  | When set to `true`, provides the resolved device system MAC address as an input value to the Digital Twin environment.<br>A per-node `digital_twin.system_mac_address` value overrides the regular device `system_mac_address` for the Digital Twin device.<br>Supported Digital Twin environments:<br>- `act`: Applies only to `veos` and `cloudeos` node types. Ignored for all other node types. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;serial_number</samp>](## "<node_type_keys.key>.nodes.[].digital_twin.serial_number") | String |  |  |  | Serial number override for this Digital Twin device.<br>Used when `digital_twin.hardware_identity.serial_number` is set to `true`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;system_mac_address</samp>](## "<node_type_keys.key>.nodes.[].digital_twin.system_mac_address") | String |  |  |  | System MAC address override for this Digital Twin device.<br>Used when `digital_twin.hardware_identity.system_mac_address` is set to `true`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ztp</samp>](## "<node_type_keys.key>.nodes.[].digital_twin.ztp") | Boolean |  |  |  | Enable ZTP (Zero Touch Provisioning) mode for this Digital Twin device.<br>Supported Digital Twin environments:<br>- `act`: Applies only to `veos` and `cloudeos` node types. Ignored for all other node types.<br>Overrides global `digital_twin.fabric.ztp` when defined. |
    | [<samp>device_profiles</samp>](## "device_profiles") | List, items: Dictionary |  |  |  | PREVIEW - This datamodel is still under development and may change or get removed at any time. |
    | [<samp>&nbsp;&nbsp;-&nbsp;name</samp>](## "device_profiles.[].name") | String | Required, Unique |  |  | Profile Name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;digital_twin</samp>](## "device_profiles.[].digital_twin") | Dictionary |  |  |  | PREVIEW: This option is marked as "preview", meaning the data models or generated configuration can change at any time.<br>Set the OS version, management IP address, and management gateway for the digital twin of the associated node(s). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;act_os_version</samp>](## "device_profiles.[].digital_twin.act_os_version") | String |  |  |  | Desired ACT Digital Twin OS version.<br>Overrides global `digital_twin.fabric.act_os_version` flag. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mgmt_ip</samp>](## "device_profiles.[].digital_twin.mgmt_ip") | String |  |  | Format: cidr | Desired management interface IPv4 address for the Digital Twin.<br>In ACT Digital Twin mode, this address is used in the ACT topology.<br>If the regular `mgmt_ip` is set, this `digital_twin.mgmt_ip` address is also used for the generated OOB management interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mgmt_gateway</samp>](## "device_profiles.[].digital_twin.mgmt_gateway") | String |  |  |  | Desired OOB management gateway for the Digital Twin.<br>In ACT Digital Twin mode, if the regular `mgmt_ip` is set, this `digital_twin.mgmt_gateway` address takes precedence over the regular management gateway for the generated OOB management interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;act_internet_access</samp>](## "device_profiles.[].digital_twin.act_internet_access") | Boolean |  |  |  | Specifies if the ACT Digital Twin device is deployed with direct access to the Internet.<br>This option applies only to the 'cloudeos' and 'veos' node types and will be ignored for all other ACT node types.<br>ACT does not provide direct Internet access to cloudeos or veos devices by default.<br>Overrides global `digital_twin.fabric.act_internet_access` flag. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hardware_identity</samp>](## "device_profiles.[].digital_twin.hardware_identity") | Dictionary |  |  |  | Settings controlling use of hardware identity values for the Digital Twin device.<br>Each setting overrides the corresponding global `digital_twin.fabric.hardware_identity` setting when defined. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;serial_number</samp>](## "device_profiles.[].digital_twin.hardware_identity.serial_number") | Boolean |  |  |  | When set to `true`, provides the resolved device serial number as an input value to the Digital Twin environment.<br>A per-node `digital_twin.serial_number` value overrides the regular device `serial_number` for the Digital Twin device.<br>Supported Digital Twin environments:<br>- `act`: Applies only to `veos` and `cloudeos` node types. Ignored for all other node types. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;system_mac_address</samp>](## "device_profiles.[].digital_twin.hardware_identity.system_mac_address") | Boolean |  |  |  | When set to `true`, provides the resolved device system MAC address as an input value to the Digital Twin environment.<br>A per-node `digital_twin.system_mac_address` value overrides the regular device `system_mac_address` for the Digital Twin device.<br>Supported Digital Twin environments:<br>- `act`: Applies only to `veos` and `cloudeos` node types. Ignored for all other node types. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;serial_number</samp>](## "device_profiles.[].digital_twin.serial_number") | String |  |  |  | Serial number override for this Digital Twin device.<br>Used when `digital_twin.hardware_identity.serial_number` is set to `true`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;system_mac_address</samp>](## "device_profiles.[].digital_twin.system_mac_address") | String |  |  |  | System MAC address override for this Digital Twin device.<br>Used when `digital_twin.hardware_identity.system_mac_address` is set to `true`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ztp</samp>](## "device_profiles.[].digital_twin.ztp") | Boolean |  |  |  | Enable ZTP (Zero Touch Provisioning) mode for this Digital Twin device.<br>Supported Digital Twin environments:<br>- `act`: Applies only to `veos` and `cloudeos` node types. Ignored for all other node types.<br>Overrides global `digital_twin.fabric.ztp` when defined. |
    | [<samp>devices</samp>](## "devices") | List, items: Dictionary |  |  |  | PREVIEW - This datamodel is still under development and may change or get removed at any time. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "devices.[].name") | String | Required, Unique |  |  | The Node Name is used as "hostname". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;digital_twin</samp>](## "devices.[].digital_twin") | Dictionary |  |  |  | PREVIEW: This option is marked as "preview", meaning the data models or generated configuration can change at any time.<br>Set the OS version, management IP address, and management gateway for the digital twin of the associated node(s). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;act_os_version</samp>](## "devices.[].digital_twin.act_os_version") | String |  |  |  | Desired ACT Digital Twin OS version.<br>Overrides global `digital_twin.fabric.act_os_version` flag. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mgmt_ip</samp>](## "devices.[].digital_twin.mgmt_ip") | String |  |  | Format: cidr | Desired management interface IPv4 address for the Digital Twin.<br>In ACT Digital Twin mode, this address is used in the ACT topology.<br>If the regular `mgmt_ip` is set, this `digital_twin.mgmt_ip` address is also used for the generated OOB management interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mgmt_gateway</samp>](## "devices.[].digital_twin.mgmt_gateway") | String |  |  |  | Desired OOB management gateway for the Digital Twin.<br>In ACT Digital Twin mode, if the regular `mgmt_ip` is set, this `digital_twin.mgmt_gateway` address takes precedence over the regular management gateway for the generated OOB management interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;act_internet_access</samp>](## "devices.[].digital_twin.act_internet_access") | Boolean |  |  |  | Specifies if the ACT Digital Twin device is deployed with direct access to the Internet.<br>This option applies only to the 'cloudeos' and 'veos' node types and will be ignored for all other ACT node types.<br>ACT does not provide direct Internet access to cloudeos or veos devices by default.<br>Overrides global `digital_twin.fabric.act_internet_access` flag. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hardware_identity</samp>](## "devices.[].digital_twin.hardware_identity") | Dictionary |  |  |  | Settings controlling use of hardware identity values for the Digital Twin device.<br>Each setting overrides the corresponding global `digital_twin.fabric.hardware_identity` setting when defined. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;serial_number</samp>](## "devices.[].digital_twin.hardware_identity.serial_number") | Boolean |  |  |  | When set to `true`, provides the resolved device serial number as an input value to the Digital Twin environment.<br>A per-node `digital_twin.serial_number` value overrides the regular device `serial_number` for the Digital Twin device.<br>Supported Digital Twin environments:<br>- `act`: Applies only to `veos` and `cloudeos` node types. Ignored for all other node types. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;system_mac_address</samp>](## "devices.[].digital_twin.hardware_identity.system_mac_address") | Boolean |  |  |  | When set to `true`, provides the resolved device system MAC address as an input value to the Digital Twin environment.<br>A per-node `digital_twin.system_mac_address` value overrides the regular device `system_mac_address` for the Digital Twin device.<br>Supported Digital Twin environments:<br>- `act`: Applies only to `veos` and `cloudeos` node types. Ignored for all other node types. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;serial_number</samp>](## "devices.[].digital_twin.serial_number") | String |  |  |  | Serial number override for this Digital Twin device.<br>Used when `digital_twin.hardware_identity.serial_number` is set to `true`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;system_mac_address</samp>](## "devices.[].digital_twin.system_mac_address") | String |  |  |  | System MAC address override for this Digital Twin device.<br>Used when `digital_twin.hardware_identity.system_mac_address` is set to `true`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ztp</samp>](## "devices.[].digital_twin.ztp") | Boolean |  |  |  | Enable ZTP (Zero Touch Provisioning) mode for this Digital Twin device.<br>Supported Digital Twin environments:<br>- `act`: Applies only to `veos` and `cloudeos` node types. Ignored for all other node types.<br>Overrides global `digital_twin.fabric.ztp` when defined. |

=== "YAML"

    ```yaml
    <node_type_keys.key>:

      # Define variables for all nodes of this type.
      defaults:

        # PREVIEW: This option is marked as "preview", meaning the data models or generated configuration can change at any time.
        # Set the OS version, management IP address, and management gateway for the digital twin of the associated node(s).
        digital_twin:

          # Desired ACT Digital Twin OS version.
          # Overrides global `digital_twin.fabric.act_os_version` flag.
          act_os_version: <str>

          # Desired management interface IPv4 address for the Digital Twin.
          # In ACT Digital Twin mode, this address is used in the ACT topology.
          # If the regular `mgmt_ip` is set, this `digital_twin.mgmt_ip` address is also used for the generated OOB management interface.
          mgmt_ip: <str>

          # Desired OOB management gateway for the Digital Twin.
          # In ACT Digital Twin mode, if the regular `mgmt_ip` is set, this `digital_twin.mgmt_gateway` address takes precedence over the regular management gateway for the generated OOB management interface.
          mgmt_gateway: <str>

          # Specifies if the ACT Digital Twin device is deployed with direct access to the Internet.
          # This option applies only to the 'cloudeos' and 'veos' node types and will be ignored for all other ACT node types.
          # ACT does not provide direct Internet access to cloudeos or veos devices by default.
          # Overrides global `digital_twin.fabric.act_internet_access` flag.
          act_internet_access: <bool>

          # Settings controlling use of hardware identity values for the Digital Twin device.
          # Each setting overrides the corresponding global `digital_twin.fabric.hardware_identity` setting when defined.
          hardware_identity:

            # When set to `true`, provides the resolved device serial number as an input value to the Digital Twin environment.
            # A per-node `digital_twin.serial_number` value overrides the regular device `serial_number` for the Digital Twin device.
            # Supported Digital Twin environments:
            # - `act`: Applies only to `veos` and `cloudeos` node types. Ignored for all other node types.
            serial_number: <bool>

            # When set to `true`, provides the resolved device system MAC address as an input value to the Digital Twin environment.
            # A per-node `digital_twin.system_mac_address` value overrides the regular device `system_mac_address` for the Digital Twin device.
            # Supported Digital Twin environments:
            # - `act`: Applies only to `veos` and `cloudeos` node types. Ignored for all other node types.
            system_mac_address: <bool>

          # Serial number override for this Digital Twin device.
          # Used when `digital_twin.hardware_identity.serial_number` is set to `true`.
          serial_number: <str>

          # System MAC address override for this Digital Twin device.
          # Used when `digital_twin.hardware_identity.system_mac_address` is set to `true`.
          system_mac_address: <str>

          # Enable ZTP (Zero Touch Provisioning) mode for this Digital Twin device.
          # Supported Digital Twin environments:
          # - `act`: Applies only to `veos` and `cloudeos` node types. Ignored for all other node types.
          # Overrides global `digital_twin.fabric.ztp` when defined.
          ztp: <bool>

      # Define variables related to all nodes part of this group.
      node_groups:

          # The Node Group Name is used for MLAG domain unless set with 'mlag_domain_id'.
          # The Node Group Name is also used for peer description on downstream switches' uplinks.
        - group: <str; required; unique>

          # Define variables per node.
          nodes:

              # The Node Name is used as "hostname".
            - name: <str; required; unique>

              # PREVIEW: This option is marked as "preview", meaning the data models or generated configuration can change at any time.
              # Set the OS version, management IP address, and management gateway for the digital twin of the associated node(s).
              digital_twin:

                # Desired ACT Digital Twin OS version.
                # Overrides global `digital_twin.fabric.act_os_version` flag.
                act_os_version: <str>

                # Desired management interface IPv4 address for the Digital Twin.
                # In ACT Digital Twin mode, this address is used in the ACT topology.
                # If the regular `mgmt_ip` is set, this `digital_twin.mgmt_ip` address is also used for the generated OOB management interface.
                mgmt_ip: <str>

                # Desired OOB management gateway for the Digital Twin.
                # In ACT Digital Twin mode, if the regular `mgmt_ip` is set, this `digital_twin.mgmt_gateway` address takes precedence over the regular management gateway for the generated OOB management interface.
                mgmt_gateway: <str>

                # Specifies if the ACT Digital Twin device is deployed with direct access to the Internet.
                # This option applies only to the 'cloudeos' and 'veos' node types and will be ignored for all other ACT node types.
                # ACT does not provide direct Internet access to cloudeos or veos devices by default.
                # Overrides global `digital_twin.fabric.act_internet_access` flag.
                act_internet_access: <bool>

                # Settings controlling use of hardware identity values for the Digital Twin device.
                # Each setting overrides the corresponding global `digital_twin.fabric.hardware_identity` setting when defined.
                hardware_identity:

                  # When set to `true`, provides the resolved device serial number as an input value to the Digital Twin environment.
                  # A per-node `digital_twin.serial_number` value overrides the regular device `serial_number` for the Digital Twin device.
                  # Supported Digital Twin environments:
                  # - `act`: Applies only to `veos` and `cloudeos` node types. Ignored for all other node types.
                  serial_number: <bool>

                  # When set to `true`, provides the resolved device system MAC address as an input value to the Digital Twin environment.
                  # A per-node `digital_twin.system_mac_address` value overrides the regular device `system_mac_address` for the Digital Twin device.
                  # Supported Digital Twin environments:
                  # - `act`: Applies only to `veos` and `cloudeos` node types. Ignored for all other node types.
                  system_mac_address: <bool>

                # Serial number override for this Digital Twin device.
                # Used when `digital_twin.hardware_identity.serial_number` is set to `true`.
                serial_number: <str>

                # System MAC address override for this Digital Twin device.
                # Used when `digital_twin.hardware_identity.system_mac_address` is set to `true`.
                system_mac_address: <str>

                # Enable ZTP (Zero Touch Provisioning) mode for this Digital Twin device.
                # Supported Digital Twin environments:
                # - `act`: Applies only to `veos` and `cloudeos` node types. Ignored for all other node types.
                # Overrides global `digital_twin.fabric.ztp` when defined.
                ztp: <bool>

          # PREVIEW: This option is marked as "preview", meaning the data models or generated configuration can change at any time.
          # Set the OS version, management IP address, and management gateway for the digital twin of the associated node(s).
          digital_twin:

            # Desired ACT Digital Twin OS version.
            # Overrides global `digital_twin.fabric.act_os_version` flag.
            act_os_version: <str>

            # Desired management interface IPv4 address for the Digital Twin.
            # In ACT Digital Twin mode, this address is used in the ACT topology.
            # If the regular `mgmt_ip` is set, this `digital_twin.mgmt_ip` address is also used for the generated OOB management interface.
            mgmt_ip: <str>

            # Desired OOB management gateway for the Digital Twin.
            # In ACT Digital Twin mode, if the regular `mgmt_ip` is set, this `digital_twin.mgmt_gateway` address takes precedence over the regular management gateway for the generated OOB management interface.
            mgmt_gateway: <str>

            # Specifies if the ACT Digital Twin device is deployed with direct access to the Internet.
            # This option applies only to the 'cloudeos' and 'veos' node types and will be ignored for all other ACT node types.
            # ACT does not provide direct Internet access to cloudeos or veos devices by default.
            # Overrides global `digital_twin.fabric.act_internet_access` flag.
            act_internet_access: <bool>

            # Settings controlling use of hardware identity values for the Digital Twin device.
            # Each setting overrides the corresponding global `digital_twin.fabric.hardware_identity` setting when defined.
            hardware_identity:

              # When set to `true`, provides the resolved device serial number as an input value to the Digital Twin environment.
              # A per-node `digital_twin.serial_number` value overrides the regular device `serial_number` for the Digital Twin device.
              # Supported Digital Twin environments:
              # - `act`: Applies only to `veos` and `cloudeos` node types. Ignored for all other node types.
              serial_number: <bool>

              # When set to `true`, provides the resolved device system MAC address as an input value to the Digital Twin environment.
              # A per-node `digital_twin.system_mac_address` value overrides the regular device `system_mac_address` for the Digital Twin device.
              # Supported Digital Twin environments:
              # - `act`: Applies only to `veos` and `cloudeos` node types. Ignored for all other node types.
              system_mac_address: <bool>

            # Serial number override for this Digital Twin device.
            # Used when `digital_twin.hardware_identity.serial_number` is set to `true`.
            serial_number: <str>

            # System MAC address override for this Digital Twin device.
            # Used when `digital_twin.hardware_identity.system_mac_address` is set to `true`.
            system_mac_address: <str>

            # Enable ZTP (Zero Touch Provisioning) mode for this Digital Twin device.
            # Supported Digital Twin environments:
            # - `act`: Applies only to `veos` and `cloudeos` node types. Ignored for all other node types.
            # Overrides global `digital_twin.fabric.ztp` when defined.
            ztp: <bool>

      # Define variables per node.
      nodes:

          # The Node Name is used as "hostname".
        - name: <str; required; unique>

          # PREVIEW: This option is marked as "preview", meaning the data models or generated configuration can change at any time.
          # Set the OS version, management IP address, and management gateway for the digital twin of the associated node(s).
          digital_twin:

            # Desired ACT Digital Twin OS version.
            # Overrides global `digital_twin.fabric.act_os_version` flag.
            act_os_version: <str>

            # Desired management interface IPv4 address for the Digital Twin.
            # In ACT Digital Twin mode, this address is used in the ACT topology.
            # If the regular `mgmt_ip` is set, this `digital_twin.mgmt_ip` address is also used for the generated OOB management interface.
            mgmt_ip: <str>

            # Desired OOB management gateway for the Digital Twin.
            # In ACT Digital Twin mode, if the regular `mgmt_ip` is set, this `digital_twin.mgmt_gateway` address takes precedence over the regular management gateway for the generated OOB management interface.
            mgmt_gateway: <str>

            # Specifies if the ACT Digital Twin device is deployed with direct access to the Internet.
            # This option applies only to the 'cloudeos' and 'veos' node types and will be ignored for all other ACT node types.
            # ACT does not provide direct Internet access to cloudeos or veos devices by default.
            # Overrides global `digital_twin.fabric.act_internet_access` flag.
            act_internet_access: <bool>

            # Settings controlling use of hardware identity values for the Digital Twin device.
            # Each setting overrides the corresponding global `digital_twin.fabric.hardware_identity` setting when defined.
            hardware_identity:

              # When set to `true`, provides the resolved device serial number as an input value to the Digital Twin environment.
              # A per-node `digital_twin.serial_number` value overrides the regular device `serial_number` for the Digital Twin device.
              # Supported Digital Twin environments:
              # - `act`: Applies only to `veos` and `cloudeos` node types. Ignored for all other node types.
              serial_number: <bool>

              # When set to `true`, provides the resolved device system MAC address as an input value to the Digital Twin environment.
              # A per-node `digital_twin.system_mac_address` value overrides the regular device `system_mac_address` for the Digital Twin device.
              # Supported Digital Twin environments:
              # - `act`: Applies only to `veos` and `cloudeos` node types. Ignored for all other node types.
              system_mac_address: <bool>

            # Serial number override for this Digital Twin device.
            # Used when `digital_twin.hardware_identity.serial_number` is set to `true`.
            serial_number: <str>

            # System MAC address override for this Digital Twin device.
            # Used when `digital_twin.hardware_identity.system_mac_address` is set to `true`.
            system_mac_address: <str>

            # Enable ZTP (Zero Touch Provisioning) mode for this Digital Twin device.
            # Supported Digital Twin environments:
            # - `act`: Applies only to `veos` and `cloudeos` node types. Ignored for all other node types.
            # Overrides global `digital_twin.fabric.ztp` when defined.
            ztp: <bool>

    # PREVIEW - This datamodel is still under development and may change or get removed at any time.
    device_profiles:

        # Profile Name
      - name: <str; required; unique>

        # PREVIEW: This option is marked as "preview", meaning the data models or generated configuration can change at any time.
        # Set the OS version, management IP address, and management gateway for the digital twin of the associated node(s).
        digital_twin:

          # Desired ACT Digital Twin OS version.
          # Overrides global `digital_twin.fabric.act_os_version` flag.
          act_os_version: <str>

          # Desired management interface IPv4 address for the Digital Twin.
          # In ACT Digital Twin mode, this address is used in the ACT topology.
          # If the regular `mgmt_ip` is set, this `digital_twin.mgmt_ip` address is also used for the generated OOB management interface.
          mgmt_ip: <str>

          # Desired OOB management gateway for the Digital Twin.
          # In ACT Digital Twin mode, if the regular `mgmt_ip` is set, this `digital_twin.mgmt_gateway` address takes precedence over the regular management gateway for the generated OOB management interface.
          mgmt_gateway: <str>

          # Specifies if the ACT Digital Twin device is deployed with direct access to the Internet.
          # This option applies only to the 'cloudeos' and 'veos' node types and will be ignored for all other ACT node types.
          # ACT does not provide direct Internet access to cloudeos or veos devices by default.
          # Overrides global `digital_twin.fabric.act_internet_access` flag.
          act_internet_access: <bool>

          # Settings controlling use of hardware identity values for the Digital Twin device.
          # Each setting overrides the corresponding global `digital_twin.fabric.hardware_identity` setting when defined.
          hardware_identity:

            # When set to `true`, provides the resolved device serial number as an input value to the Digital Twin environment.
            # A per-node `digital_twin.serial_number` value overrides the regular device `serial_number` for the Digital Twin device.
            # Supported Digital Twin environments:
            # - `act`: Applies only to `veos` and `cloudeos` node types. Ignored for all other node types.
            serial_number: <bool>

            # When set to `true`, provides the resolved device system MAC address as an input value to the Digital Twin environment.
            # A per-node `digital_twin.system_mac_address` value overrides the regular device `system_mac_address` for the Digital Twin device.
            # Supported Digital Twin environments:
            # - `act`: Applies only to `veos` and `cloudeos` node types. Ignored for all other node types.
            system_mac_address: <bool>

          # Serial number override for this Digital Twin device.
          # Used when `digital_twin.hardware_identity.serial_number` is set to `true`.
          serial_number: <str>

          # System MAC address override for this Digital Twin device.
          # Used when `digital_twin.hardware_identity.system_mac_address` is set to `true`.
          system_mac_address: <str>

          # Enable ZTP (Zero Touch Provisioning) mode for this Digital Twin device.
          # Supported Digital Twin environments:
          # - `act`: Applies only to `veos` and `cloudeos` node types. Ignored for all other node types.
          # Overrides global `digital_twin.fabric.ztp` when defined.
          ztp: <bool>

    # PREVIEW - This datamodel is still under development and may change or get removed at any time.
    devices:

        # The Node Name is used as "hostname".
        name: <str; required; unique>

        # PREVIEW: This option is marked as "preview", meaning the data models or generated configuration can change at any time.
        # Set the OS version, management IP address, and management gateway for the digital twin of the associated node(s).
        digital_twin:

          # Desired ACT Digital Twin OS version.
          # Overrides global `digital_twin.fabric.act_os_version` flag.
          act_os_version: <str>

          # Desired management interface IPv4 address for the Digital Twin.
          # In ACT Digital Twin mode, this address is used in the ACT topology.
          # If the regular `mgmt_ip` is set, this `digital_twin.mgmt_ip` address is also used for the generated OOB management interface.
          mgmt_ip: <str>

          # Desired OOB management gateway for the Digital Twin.
          # In ACT Digital Twin mode, if the regular `mgmt_ip` is set, this `digital_twin.mgmt_gateway` address takes precedence over the regular management gateway for the generated OOB management interface.
          mgmt_gateway: <str>

          # Specifies if the ACT Digital Twin device is deployed with direct access to the Internet.
          # This option applies only to the 'cloudeos' and 'veos' node types and will be ignored for all other ACT node types.
          # ACT does not provide direct Internet access to cloudeos or veos devices by default.
          # Overrides global `digital_twin.fabric.act_internet_access` flag.
          act_internet_access: <bool>

          # Settings controlling use of hardware identity values for the Digital Twin device.
          # Each setting overrides the corresponding global `digital_twin.fabric.hardware_identity` setting when defined.
          hardware_identity:

            # When set to `true`, provides the resolved device serial number as an input value to the Digital Twin environment.
            # A per-node `digital_twin.serial_number` value overrides the regular device `serial_number` for the Digital Twin device.
            # Supported Digital Twin environments:
            # - `act`: Applies only to `veos` and `cloudeos` node types. Ignored for all other node types.
            serial_number: <bool>

            # When set to `true`, provides the resolved device system MAC address as an input value to the Digital Twin environment.
            # A per-node `digital_twin.system_mac_address` value overrides the regular device `system_mac_address` for the Digital Twin device.
            # Supported Digital Twin environments:
            # - `act`: Applies only to `veos` and `cloudeos` node types. Ignored for all other node types.
            system_mac_address: <bool>

          # Serial number override for this Digital Twin device.
          # Used when `digital_twin.hardware_identity.serial_number` is set to `true`.
          serial_number: <str>

          # System MAC address override for this Digital Twin device.
          # Used when `digital_twin.hardware_identity.system_mac_address` is set to `true`.
          system_mac_address: <str>

          # Enable ZTP (Zero Touch Provisioning) mode for this Digital Twin device.
          # Supported Digital Twin environments:
          # - `act`: Applies only to `veos` and `cloudeos` node types. Ignored for all other node types.
          # Overrides global `digital_twin.fabric.ztp` when defined.
          ztp: <bool>
    ```
