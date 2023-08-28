<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>source_interfaces</samp>](## "source_interfaces") | Dictionary |  |  |  | Configure source-interfaces based on the management interfaces set for other `eos_designs` data models.<br>By default, no source-interfaces will be configured. They can still be configured manually using `eos_cli_config_gen` and custom structured configuration.<br>EOS supports a single source-interface per VRF, so an error will be raised in case of conflicts.<br>Errors will also be raised if an interface is not found for a device. |
    | [<samp>&nbsp;&nbsp;domain_lookup</samp>](## "source_interfaces.domain_lookup") | Dictionary |  |  |  | IP Domain Lookup source-interfaces. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mgmt_interface</samp>](## "source_interfaces.domain_lookup.mgmt_interface") | Boolean |  |  |  | Configure an IP Domain Lookup source-interface with the interface set by `mgmt_interface` for the VRF set by `mgmt_interface_vrf`.<br>`mgmt_interface` is typically the out-of-band Management interface, and can be set under the node settings, platform settings or as a group/host var. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;inband_mgmt_interface</samp>](## "source_interfaces.domain_lookup.inband_mgmt_interface") | Boolean |  |  |  | Configure an IP Domain Lookup source-interface with the interface set by `inband_mgmt_interface` for the VRF set by `inband_mgmt_vrf`.<br>`inband_mgmt_interface` is typically a loopback or SVI interface, and can be set under the node settings. |
    | [<samp>&nbsp;&nbsp;http_client</samp>](## "source_interfaces.http_client") | Dictionary |  |  |  | IP HTTP Client source-interfaces. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mgmt_interface</samp>](## "source_interfaces.http_client.mgmt_interface") | Boolean |  |  |  | Configure an IP HTTP Client source-interface with the interface set by `mgmt_interface` for the VRF set by `mgmt_interface_vrf`.<br>`mgmt_interface` is typically the out-of-band Management interface, and can be set under the node settings, platform settings or as a group/host var. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;inband_mgmt_interface</samp>](## "source_interfaces.http_client.inband_mgmt_interface") | Boolean |  |  |  | Configure an IP HTTP Client source-interface with the interface set by `inband_mgmt_interface` for the VRF set by `inband_mgmt_vrf`.<br>`inband_mgmt_interface` is typically a loopback or SVI interface, and can be set under the node settings. |
    | [<samp>&nbsp;&nbsp;radius</samp>](## "source_interfaces.radius") | Dictionary |  |  |  | IP Radius source-interfaces. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mgmt_interface</samp>](## "source_interfaces.radius.mgmt_interface") | Boolean |  |  |  | Configure an IP Radius source-interface with the interface set by `mgmt_interface` for the VRF set by `mgmt_interface_vrf`.<br>`mgmt_interface` is typically the out-of-band Management interface, and can be set under the node settings, platform settings or as a group/host var. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;inband_mgmt_interface</samp>](## "source_interfaces.radius.inband_mgmt_interface") | Boolean |  |  |  | Configure an IP Radius source-interface with the interface set by `inband_mgmt_interface` for the VRF set by `inband_mgmt_vrf`.<br>`inband_mgmt_interface` is typically a loopback or SVI interface, and can be set under the node settings. |
    | [<samp>&nbsp;&nbsp;ssh_client</samp>](## "source_interfaces.ssh_client") | Dictionary |  |  |  | IP SSH Client source-interfaces. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mgmt_interface</samp>](## "source_interfaces.ssh_client.mgmt_interface") | Boolean |  |  |  | Configure an IP SSH Client source-interface with the interface set by `mgmt_interface` for the VRF set by `mgmt_interface_vrf`.<br>`mgmt_interface` is typically the out-of-band Management interface, and can be set under the node settings, platform settings or as a group/host var. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;inband_mgmt_interface</samp>](## "source_interfaces.ssh_client.inband_mgmt_interface") | Boolean |  |  |  | Configure an IP SSH Client source-interface with the interface set by `inband_mgmt_interface` for the VRF set by `inband_mgmt_vrf`.<br>`inband_mgmt_interface` is typically a loopback or SVI interface, and can be set under the node settings. |
    | [<samp>&nbsp;&nbsp;tacacs</samp>](## "source_interfaces.tacacs") | Dictionary |  |  |  | IP Tacacs source-interfaces. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mgmt_interface</samp>](## "source_interfaces.tacacs.mgmt_interface") | Boolean |  |  |  | Configure an IP Tacacs source-interface with the interface set by `mgmt_interface` for the VRF set by `mgmt_interface_vrf`.<br>`mgmt_interface` is typically the out-of-band Management interface, and can be set under the node settings, platform settings or as a group/host var. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;inband_mgmt_interface</samp>](## "source_interfaces.tacacs.inband_mgmt_interface") | Boolean |  |  |  | Configure an IP Tacacs source-interface with the interface set by `inband_mgmt_interface` for the VRF set by `inband_mgmt_vrf`.<br>`inband_mgmt_interface` is typically a loopback or SVI interface, and can be set under the node settings. |

=== "YAML"

    ```yaml
    source_interfaces:
      domain_lookup:
        mgmt_interface: <bool>
        inband_mgmt_interface: <bool>
      http_client:
        mgmt_interface: <bool>
        inband_mgmt_interface: <bool>
      radius:
        mgmt_interface: <bool>
        inband_mgmt_interface: <bool>
      ssh_client:
        mgmt_interface: <bool>
        inband_mgmt_interface: <bool>
      tacacs:
        mgmt_interface: <bool>
        inband_mgmt_interface: <bool>
    ```
