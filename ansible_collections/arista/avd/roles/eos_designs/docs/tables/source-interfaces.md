=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>source_interfaces</samp>](## "source_interfaces") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;radius</samp>](## "source_interfaces.radius") | Dictionary |  |  |  | Set Radius source interfaces based on other `eos_designs` settings.<br>By default, no source interfaces will be added. They can still be configured manually using `ip_radius_source_interfaces` in `eos_cli_config_gen`.<br>EOS supports a single source interface per VRF, so an error will be raised in case of conflicts.<br>Errors will also be raised if an interface is not found for a device. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mgmt_interface</samp>](## "source_interfaces.radius.mgmt_interface") | Boolean |  |  |  | Set a Radius source interface with the `mgmt_interface` for the device and the VRF set by `mgmt_interface_vrf`.<br>`mgmt_interface` is typically the out-of-band Management interface, and can be set under the node settings, platform settings or as a group/host var. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;inband_mgmt_interface</samp>](## "source_interfaces.radius.inband_mgmt_interface") | Boolean |  |  |  | Add a Radius source interface with the `inband_mgmt_interface` for the device and the VRF set by `inband_mgmt_vrf`.<br>`inband_mgmt_interface` is typically a loopback or SVI interface, and can be set under the node settings. |
    | [<samp>&nbsp;&nbsp;tacacs</samp>](## "source_interfaces.tacacs") | Dictionary |  |  |  | Set Tacacs source interfaces based on other `eos_designs` settings.<br>By default, no source interfaces will be added. They can still be configured manually using `ip_tacacs_source_interfaces` in `eos_cli_config_gen`.<br>EOS supports a single source interface per VRF, so an error will be raised in case of conflicts.<br>Errors will also be raised if an interface is not found for a device. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mgmt_interface</samp>](## "source_interfaces.tacacs.mgmt_interface") | Boolean |  |  |  | Set a Tacacs source interface with the `mgmt_interface` for the device and the VRF set by `mgmt_interface_vrf`.<br>`mgmt_interface` is typically the out-of-band Management interface, and can be set under the node settings, platform settings or as a group/host var. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;inband_mgmt_interface</samp>](## "source_interfaces.tacacs.inband_mgmt_interface") | Boolean |  |  |  | Add a Tacacs source interface with the `inband_mgmt_interface` for the device and the VRF set by `inband_mgmt_vrf`.<br>`inband_mgmt_interface` is typically a loopback or SVI interface, and can be set under the node settings. |

=== "YAML"

    ```yaml
    source_interfaces:
      radius:
        mgmt_interface: <bool>
        inband_mgmt_interface: <bool>
      tacacs:
        mgmt_interface: <bool>
        inband_mgmt_interface: <bool>
    ```
