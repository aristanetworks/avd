<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>default_mgmt_method</samp>](## "default_mgmt_method") | String |  | `oob` | Valid Values:<br>- <code>oob</code><br>- <code>inband</code><br>- <code>none</code> | `default_mgmt_method` controls the default VRF and source interface used for the following management and monitoring protocols configured with AVD Design:<br>  - `aaa_settings`<br>  - `cv_settings`<br>  - `logging_settings`<br>  - `management_eapi`<br>  - `ntp_settings`<br>  - `sflow_settings`<br>  - `snmp_settings`<br>  - `ssh_settings`<br><br>`oob` means the protocols will be configured with the VRF set by `mgmt_interface_vrf` and `mgmt_interface` as the source interface.<br>`inband` means the protocols will be configured with the VRF set by `inband_mgmt_vrf` and `inband_mgmt_interface` as the source interface.<br>`none` means the VRF and or interface must be manually set for each protocol.<br>This can be overridden under the settings for each protocol.<br> |
    | [<samp>ipv6_mgmt_destination_networks</samp>](## "ipv6_mgmt_destination_networks") | List, items: String |  |  |  | List of IPv6 prefixes to configure as static routes towards the OOB IPv6 Management interface gateway.<br>Replaces the default route.<br> |
    | [<samp>&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "ipv6_mgmt_destination_networks.[]") | String |  |  |  | IPv6_network/Mask. |
    | [<samp>ipv6_mgmt_gateway</samp>](## "ipv6_mgmt_gateway") | String |  |  | Format: ipv6 | OOB Management interface gateway in IPv6 format.<br>Used as next-hop for default gateway or static routes defined under 'ipv6_mgmt_destination_networks'.<br> |
    | [<samp>mgmt_destination_networks</samp>](## "mgmt_destination_networks") <span style="color:red">deprecated</span> | List, items: String |  |  |  | List of IPv4 prefixes to configure as static routes towards the OOB Management interface gateway.<br>Replaces the default route.<br>This setting is ignored when 'mgmt_ip' is set to 'dhcp' and 'avd_design_future.accept_dhcp_default_route_for_mgmt_ip_dhcp: true', since the DHCP server will provide the default route.<span style="color:red">This key is deprecated. Support will be removed in AVD version 7.0.0. Use <samp>mgmt_ipv4.static_routes</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "mgmt_destination_networks.[]") | String |  |  |  | IPv4_address/Mask. |
    | [<samp>mgmt_gateway</samp>](## "mgmt_gateway") <span style="color:red">deprecated</span> | String |  |  |  | OOB Management interface gateway in IPv4 format.<br>Used as next-hop for default gateway or static routes defined under 'mgmt_destination_networks'.<br>This setting is ignored when 'mgmt_ip' is set to 'dhcp' and 'avd_design_future.accept_dhcp_default_route_for_mgmt_ip_dhcp: true', since the DHCP server will provide the gateway.<br><span style="color:red">This key is deprecated. Support will be removed in AVD version 7.0.0. Use <samp>mgmt_ipv4.gateway</samp> instead.</span> |
    | [<samp>mgmt_interface</samp>](## "mgmt_interface") <span style="color:red">deprecated</span> | String |  | `Management1` |  | OOB Management interface.<span style="color:red">This key is deprecated. Support will be removed in AVD version 7.0.0. Use <samp>mgmt_interface_settings.interface</samp> instead.</span> |
    | [<samp>mgmt_interface_description</samp>](## "mgmt_interface_description") <span style="color:red">deprecated</span> | String |  | `OOB_MANAGEMENT` |  | Management interface description.<br><span style="color:red">This key is deprecated. Support will be removed in AVD version 7.0.0. Use <samp>mgmt_interface_settings.description</samp> instead.</span> |
    | [<samp>mgmt_interface_settings</samp>](## "mgmt_interface_settings") | Dictionary |  |  |  | Out-of-Band (OOB) management interface settings.<br>These settings override the corresponding global variables where applicable. |
    | [<samp>&nbsp;&nbsp;description</samp>](## "mgmt_interface_settings.description") | String |  | `OOB_MANAGEMENT` |  | Interface description configured on the management interface. |
    | [<samp>&nbsp;&nbsp;vrf</samp>](## "mgmt_interface_settings.vrf") | String |  | `MGMT` |  | VRF name used for the management interface. |
    | [<samp>&nbsp;&nbsp;vrf_routing</samp>](## "mgmt_interface_settings.vrf_routing") | Boolean |  | `False` |  | Enable IP routing in the management VRF. |
    | [<samp>&nbsp;&nbsp;interface</samp>](## "mgmt_interface_settings.interface") | String |  | `Management1` |  | Name of the management interface (e.g. Management0, Management1). |
    | [<samp>&nbsp;&nbsp;lldp</samp>](## "mgmt_interface_settings.lldp") | Dictionary |  |  |  | LLDP settings for the management interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;transmit</samp>](## "mgmt_interface_settings.lldp.transmit") | Boolean |  |  |  | Enable LLDP transmission on the management interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;receive</samp>](## "mgmt_interface_settings.lldp.receive") | Boolean |  |  |  | Enable LLDP reception on the management interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ztp_vlan</samp>](## "mgmt_interface_settings.lldp.ztp_vlan") | Integer |  |  |  | VLAN ID advertised via LLDP for Zero Touch Provisioning (ZTP). |
    | [<samp>mgmt_interface_vrf</samp>](## "mgmt_interface_vrf") <span style="color:red">deprecated</span> | String |  | `MGMT` |  | OOB Management VRF.<span style="color:red">This key is deprecated. Support will be removed in AVD version 7.0.0. Use <samp>mgmt_interface_settings.vrf</samp> instead.</span> |
    | [<samp>mgmt_ipv4</samp>](## "mgmt_ipv4") | Dictionary |  |  |  | IPv4 OOB Management settings. |
    | [<samp>&nbsp;&nbsp;dhcp</samp>](## "mgmt_ipv4.dhcp") | Boolean |  |  |  | Use DHCP for IP addressing on the management interface.<br>Per-device override: 'mgmt_ip' (takes precedence). |
    | [<samp>&nbsp;&nbsp;gateway</samp>](## "mgmt_ipv4.gateway") | String |  |  |  | OOB Management gateway in IPv4 format applied to all devices.<br>Used as next-hop for the default route or static routes defined under `mgmt_ipv4.static_routes`.<br>Per-device override: `mgmt_gateway` (takes precedence).<br>This setting is ignored when using DHCP for the management IP and<br>'avd_design_future.accept_dhcp_default_route_for_mgmt_ip_dhcp: true', since the DHCP server<br>will provide the gateway. |
    | [<samp>&nbsp;&nbsp;static_routes</samp>](## "mgmt_ipv4.static_routes") | List, items: Dictionary |  |  |  | List of IPv4 prefixes to configure as static routes towards the OOB Management gateway.<br>When set, these specific prefixes replace the default route (0.0.0.0/0).<br>This setting is ignored when using DHCP for the management IP and<br>'avd_design_future.accept_dhcp_default_route_for_mgmt_ip_dhcp: true', since the DHCP server<br>will provide the default route. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;prefix</samp>](## "mgmt_ipv4.static_routes.[].prefix") | String | Required |  |  | IPv4_address/Mask. |
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

    # List of IPv6 prefixes to configure as static routes towards the OOB IPv6 Management interface gateway.
    # Replaces the default route.
    ipv6_mgmt_destination_networks:

        # IPv6_network/Mask.
      - <str>

    # OOB Management interface gateway in IPv6 format.
    # Used as next-hop for default gateway or static routes defined under 'ipv6_mgmt_destination_networks'.
    ipv6_mgmt_gateway: <str>

    # List of IPv4 prefixes to configure as static routes towards the OOB Management interface gateway.
    # Replaces the default route.
    # This setting is ignored when 'mgmt_ip' is set to 'dhcp' and 'avd_design_future.accept_dhcp_default_route_for_mgmt_ip_dhcp: true', since the DHCP server will provide the default route.
    # This key is deprecated.
    # Support will be removed in AVD version 7.0.0.
    # Use `mgmt_ipv4.static_routes` instead.
    mgmt_destination_networks:

        # IPv4_address/Mask.
      - <str>

    # OOB Management interface gateway in IPv4 format.
    # Used as next-hop for default gateway or static routes defined under 'mgmt_destination_networks'.
    # This setting is ignored when 'mgmt_ip' is set to 'dhcp' and 'avd_design_future.accept_dhcp_default_route_for_mgmt_ip_dhcp: true', since the DHCP server will provide the gateway.
    # This key is deprecated.
    # Support will be removed in AVD version 7.0.0.
    # Use `mgmt_ipv4.gateway` instead.
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

    # IPv4 OOB Management settings.
    mgmt_ipv4:

      # Use DHCP for IP addressing on the management interface.
      # Per-device override: 'mgmt_ip' (takes precedence).
      dhcp: <bool>

      # OOB Management gateway in IPv4 format applied to all devices.
      # Used as next-hop for the default route or static routes defined under `mgmt_ipv4.static_routes`.
      # Per-device override: `mgmt_gateway` (takes precedence).
      # This setting is ignored when using DHCP for the management IP and
      # 'avd_design_future.accept_dhcp_default_route_for_mgmt_ip_dhcp: true', since the DHCP server
      # will provide the gateway.
      gateway: <str>

      # List of IPv4 prefixes to configure as static routes towards the OOB Management gateway.
      # When set, these specific prefixes replace the default route (0.0.0.0/0).
      # This setting is ignored when using DHCP for the management IP and
      # 'avd_design_future.accept_dhcp_default_route_for_mgmt_ip_dhcp: true', since the DHCP server
      # will provide the default route.
      static_routes:

          # IPv4_address/Mask.
        - prefix: <str; required>

    # Configure IP routing for the OOB Management VRF.
    # This key is deprecated.
    # Support will be removed in AVD version 7.0.0.
    # Use `mgmt_interface_settings.vrf_routing` instead.
    mgmt_vrf_routing: <bool; default=False>
    ```
