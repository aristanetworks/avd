<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>default_mgmt_method</samp>](## "default_mgmt_method") | String |  | `oob` | Valid Values:<br>- <code>oob</code><br>- <code>inband</code><br>- <code>none</code> | `default_mgmt_method` controls the default VRF and source interface used for the following management and monitoring protocols configured with AVD Design:<br>  - `aaa_settings`<br>  - `cv_settings`<br>  - `logging_settings`<br>  - `management_eapi`<br>  - `ntp_settings`<br>  - `sflow_settings`<br>  - `snmp_settings`<br>  - `ssh_settings`<br><br>`oob` means the protocols will be configured with the VRF set by `mgmt_interface_vrf` and `mgmt_interface` as the source interface.<br>`inband` means the protocols will be configured with the VRF set by `inband_mgmt_vrf` and `inband_mgmt_interface` as the source interface.<br>`none` means the VRF and or interface must be manually set for each protocol.<br>This can be overridden under the settings for each protocol.<br> |
    | [<samp>ipv4_subnets</samp>](## "ipv4_subnets") | List, items: Dictionary |  |  |  | Named IPv4 subnets used for address allocation.<br>Reference a subnet using `mgmt_interface_settings.ipv4_subnet` to generate OOB management addresses.<br>Address conflicts are checked across participating OOB management endpoints in the same fabric and VRF. |
    | [<samp>&nbsp;&nbsp;-&nbsp;name</samp>](## "ipv4_subnets.[].name") | String | Required, Unique |  | Min Length: 1 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;subnet</samp>](## "ipv4_subnets.[].subnet") | String | Required |  |  | Canonical IPv4 network in CIDR notation. Host bits must be zero. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;range</samp>](## "ipv4_subnets.[].range") | String |  |  |  | Optional inclusive host range within the subnet, for example `192.0.2.10-192.0.2.200`.<br>Defaults to all usable hosts. Network and broadcast addresses are excluded except for /31 and /32 subnets. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;allocation_policy</samp>](## "ipv4_subnets.[].allocation_policy") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;algorithm</samp>](## "ipv4_subnets.[].allocation_policy.algorithm") | String |  | `ascend` | Valid Values:<br>- <code>ascend</code><br>- <code>descend</code> | Address ordering within the allowed range.<br>With `device_id`, ID 1 selects the first or last allowed host respectively.<br>With `auto`, ordering selects new assignments; existing valid assignments are retained. |
    | [<samp>ipv6_mgmt_destination_networks</samp>](## "ipv6_mgmt_destination_networks") | List, items: String |  |  |  | List of IPv6 prefixes to configure as static routes towards the OOB IPv6 Management interface gateway.<br>Replaces the default route.<br>Ignored when 'avd_design_future.accept_ra_default_route_for_ipv6_mgmt_ip_auto_config: true' and<br>'ipv6_mgmt_ip' under node config is set to 'auto-config', since router<br>advertisements are expected to provide the gateway and default route.<br> |
    | [<samp>&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "ipv6_mgmt_destination_networks.[]") | String |  |  |  | IPv6_network/Mask. |
    | [<samp>ipv6_mgmt_gateway</samp>](## "ipv6_mgmt_gateway") | String |  |  | Format: ipv6 | OOB Management interface gateway in IPv6 format.<br>Used as next-hop for default gateway or static routes defined under 'ipv6_mgmt_destination_networks'.<br>Ignored when 'avd_design_future.accept_ra_default_route_for_ipv6_mgmt_ip_auto_config: true' and<br>'ipv6_mgmt_ip' under node config is set to 'auto-config', since router<br>advertisements are expected to provide the gateway and default route.<br> |
    | [<samp>mgmt_destination_networks</samp>](## "mgmt_destination_networks") | List, items: String |  |  |  | List of IPv4 prefixes to configure as static routes towards the OOB Management interface gateway.<br>Replaces the default route.<br>This setting is ignored when 'mgmt_ip' is set to 'dhcp' and 'avd_design_future.accept_dhcp_default_route_for_mgmt_ip_dhcp: true', since the DHCP server will provide the default route. |
    | [<samp>&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "mgmt_destination_networks.[]") | String |  |  |  | IPv4_address/Mask. |
    | [<samp>mgmt_gateway</samp>](## "mgmt_gateway") | String |  |  |  | OOB Management interface gateway in IPv4 format.<br>Used as next-hop for default gateway or static routes defined under 'mgmt_destination_networks'.<br>This setting is ignored when 'mgmt_ip' is set to 'dhcp' and 'avd_design_future.accept_dhcp_default_route_for_mgmt_ip_dhcp: true', since the DHCP server will provide the gateway.<br> |
    | [<samp>mgmt_interface</samp>](## "mgmt_interface") <span style="color:red">deprecated</span> | String |  | `Management1` |  | OOB Management interface.<span style="color:red">This key is deprecated. Support will be removed in AVD version 7.0.0. Use <samp>mgmt_interface_settings.interface</samp> instead.</span> |
    | [<samp>mgmt_interface_description</samp>](## "mgmt_interface_description") <span style="color:red">deprecated</span> | String |  | `OOB_MANAGEMENT` |  | Management interface description.<br><span style="color:red">This key is deprecated. Support will be removed in AVD version 7.0.0. Use <samp>mgmt_interface_settings.description</samp> instead.</span> |
    | [<samp>mgmt_interface_settings</samp>](## "mgmt_interface_settings") | Dictionary |  |  |  | Out-of-Band (OOB) management interface settings.<br>These settings override the corresponding global variables where applicable. |
    | [<samp>&nbsp;&nbsp;ipv4_subnet</samp>](## "mgmt_interface_settings.ipv4_subnet") | String |  |  |  | Name of an `ipv4_subnets` entry used to generate the OOB management IPv4 address.<br>An explicit node `mgmt_ip`, including `dhcp`, takes precedence.<br>Allocation mode is selected with `fabric_ip_addressing.management.ipv4_subnet.algorithm`.<br>Gateway settings are unchanged; the gateway is not inferred from the subnet. |
    | [<samp>&nbsp;&nbsp;description</samp>](## "mgmt_interface_settings.description") | String |  | `OOB_MANAGEMENT` |  | Interface description configured on the management interface. |
    | [<samp>&nbsp;&nbsp;vrf</samp>](## "mgmt_interface_settings.vrf") | String |  | `MGMT` |  | VRF name used for the management interface. |
    | [<samp>&nbsp;&nbsp;vrf_routing</samp>](## "mgmt_interface_settings.vrf_routing") | Boolean |  | `False` |  | Enable IP routing in the management VRF. |
    | [<samp>&nbsp;&nbsp;interface</samp>](## "mgmt_interface_settings.interface") | String |  | `Management1` |  | Name of the management interface (e.g. Management0, Management1). |
    | [<samp>&nbsp;&nbsp;lldp</samp>](## "mgmt_interface_settings.lldp") | Dictionary |  |  |  | LLDP settings for the management interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;transmit</samp>](## "mgmt_interface_settings.lldp.transmit") | Boolean |  |  |  | Enable LLDP transmission on the management interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;receive</samp>](## "mgmt_interface_settings.lldp.receive") | Boolean |  |  |  | Enable LLDP reception on the management interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ztp_vlan</samp>](## "mgmt_interface_settings.lldp.ztp_vlan") | Integer |  |  |  | VLAN ID advertised via LLDP for Zero Touch Provisioning (ZTP). |
    | [<samp>mgmt_interface_vrf</samp>](## "mgmt_interface_vrf") <span style="color:red">deprecated</span> | String |  | `MGMT` |  | OOB Management VRF.<span style="color:red">This key is deprecated. Support will be removed in AVD version 7.0.0. Use <samp>mgmt_interface_settings.vrf</samp> instead.</span> |
    | [<samp>mgmt_vrf_routing</samp>](## "mgmt_vrf_routing") <span style="color:red">deprecated</span> | Boolean |  | `False` |  | Configure IP routing for the OOB Management VRF.<span style="color:red">This key is deprecated. Support will be removed in AVD version 7.0.0. Use <samp>mgmt_interface_settings.vrf_routing</samp> instead.</span> |

=== "YAML"

    ```yaml
    # `default_mgmt_method` controls the default VRF and source interface used for the following management and monitoring protocols configured with AVD Design:
    #   - `aaa_settings`
    #   - `cv_settings`
    #   - `logging_settings`
    #   - `management_eapi`
    #   - `ntp_settings`
    #   - `sflow_settings`
    #   - `snmp_settings`
    #   - `ssh_settings`
    #
    # `oob` means the protocols will be configured with the VRF set by `mgmt_interface_vrf` and `mgmt_interface` as the source interface.
    # `inband` means the protocols will be configured with the VRF set by `inband_mgmt_vrf` and `inband_mgmt_interface` as the source interface.
    # `none` means the VRF and or interface must be manually set for each protocol.
    # This can be overridden under the settings for each protocol.
    default_mgmt_method: <str; "oob" | "inband" | "none"; default="oob">

    # Named IPv4 subnets used for address allocation.
    # Reference a subnet using `mgmt_interface_settings.ipv4_subnet` to generate OOB management addresses.
    # Address conflicts are checked across participating OOB management endpoints in the same fabric and VRF.
    ipv4_subnets:
      - name: <str; length >=1; required; unique>

        # Canonical IPv4 network in CIDR notation. Host bits must be zero.
        subnet: <str; required>

        # Optional inclusive host range within the subnet, for example `192.0.2.10-192.0.2.200`.
        # Defaults to all usable hosts. Network and broadcast addresses are excluded except for /31 and /32 subnets.
        range: <str>
        allocation_policy:

          # Address ordering within the allowed range.
          # With `device_id`, ID 1 selects the first or last allowed host respectively.
          # With `auto`, ordering selects new assignments; existing valid assignments are retained.
          algorithm: <str; "ascend" | "descend"; default="ascend">

    # List of IPv6 prefixes to configure as static routes towards the OOB IPv6 Management interface gateway.
    # Replaces the default route.
    # Ignored when 'avd_design_future.accept_ra_default_route_for_ipv6_mgmt_ip_auto_config: true' and
    # 'ipv6_mgmt_ip' under node config is set to 'auto-config', since router
    # advertisements are expected to provide the gateway and default route.
    ipv6_mgmt_destination_networks:

        # IPv6_network/Mask.
      - <str>

    # OOB Management interface gateway in IPv6 format.
    # Used as next-hop for default gateway or static routes defined under 'ipv6_mgmt_destination_networks'.
    # Ignored when 'avd_design_future.accept_ra_default_route_for_ipv6_mgmt_ip_auto_config: true' and
    # 'ipv6_mgmt_ip' under node config is set to 'auto-config', since router
    # advertisements are expected to provide the gateway and default route.
    ipv6_mgmt_gateway: <str>

    # List of IPv4 prefixes to configure as static routes towards the OOB Management interface gateway.
    # Replaces the default route.
    # This setting is ignored when 'mgmt_ip' is set to 'dhcp' and 'avd_design_future.accept_dhcp_default_route_for_mgmt_ip_dhcp: true', since the DHCP server will provide the default route.
    mgmt_destination_networks:

        # IPv4_address/Mask.
      - <str>

    # OOB Management interface gateway in IPv4 format.
    # Used as next-hop for default gateway or static routes defined under 'mgmt_destination_networks'.
    # This setting is ignored when 'mgmt_ip' is set to 'dhcp' and 'avd_design_future.accept_dhcp_default_route_for_mgmt_ip_dhcp: true', since the DHCP server will provide the gateway.
    mgmt_gateway: <str>

    # OOB Management interface.
    # This key is deprecated.
    # Support will be removed in AVD version 7.0.0.
    # Use `mgmt_interface_settings.interface` instead.
    mgmt_interface: <str; default="Management1">

    # Management interface description.
    # This key is deprecated.
    # Support will be removed in AVD version 7.0.0.
    # Use `mgmt_interface_settings.description` instead.
    mgmt_interface_description: <str; default="OOB_MANAGEMENT">

    # Out-of-Band (OOB) management interface settings.
    # These settings override the corresponding global variables where applicable.
    mgmt_interface_settings:

      # Name of an `ipv4_subnets` entry used to generate the OOB management IPv4 address.
      # An explicit node `mgmt_ip`, including `dhcp`, takes precedence.
      # Allocation mode is selected with `fabric_ip_addressing.management.ipv4_subnet.algorithm`.
      # Gateway settings are unchanged; the gateway is not inferred from the subnet.
      ipv4_subnet: <str>

      # Interface description configured on the management interface.
      description: <str; default="OOB_MANAGEMENT">

      # VRF name used for the management interface.
      vrf: <str; default="MGMT">

      # Enable IP routing in the management VRF.
      vrf_routing: <bool; default=False>

      # Name of the management interface (e.g. Management0, Management1).
      interface: <str; default="Management1">

      # LLDP settings for the management interface.
      lldp:

        # Enable LLDP transmission on the management interface.
        transmit: <bool>

        # Enable LLDP reception on the management interface.
        receive: <bool>

        # VLAN ID advertised via LLDP for Zero Touch Provisioning (ZTP).
        ztp_vlan: <int>

    # OOB Management VRF.
    # This key is deprecated.
    # Support will be removed in AVD version 7.0.0.
    # Use `mgmt_interface_settings.vrf` instead.
    mgmt_interface_vrf: <str; default="MGMT">

    # Configure IP routing for the OOB Management VRF.
    # This key is deprecated.
    # Support will be removed in AVD version 7.0.0.
    # Use `mgmt_interface_settings.vrf_routing` instead.
    mgmt_vrf_routing: <bool; default=False>
    ```
