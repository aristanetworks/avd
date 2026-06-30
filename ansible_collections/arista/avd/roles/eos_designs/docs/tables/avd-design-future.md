<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>avd_design_future</samp>](## "avd_design_future") | Dictionary |  |  |  | Opt-in to future AVD behaviors which will become default behaviors in a future AVD major version. |
    | [<samp>&nbsp;&nbsp;accept_dhcp_default_route_for_mgmt_ip_dhcp</samp>](## "avd_design_future.accept_dhcp_default_route_for_mgmt_ip_dhcp") | Boolean |  | `False` |  | Available from AVD 6.2.0.<br>Configure management interface to accept DHCP default route when the management IP is set to 'dhcp'. |
    | [<samp>&nbsp;&nbsp;accept_ra_default_route_for_ipv6_mgmt_ip_auto_config</samp>](## "avd_design_future.accept_ra_default_route_for_ipv6_mgmt_ip_auto_config") | Boolean |  | `False` |  | Available from AVD 6.3.0.<br>Configure management interface to accept Router Advertisement default route when the IPv6 management IP is set to 'auto-config'. |
    | [<samp>&nbsp;&nbsp;accept_dhcp_default_route_for_inband_mgmt_ip_dhcp</samp>](## "avd_design_future.accept_dhcp_default_route_for_inband_mgmt_ip_dhcp") | Boolean |  | `False` |  | Available from AVD 6.3.0.<br>Configure inband management interface to accept DHCP default route when the inband management IP is set to 'dhcp'. |
    | [<samp>&nbsp;&nbsp;configure_inband_mgmt_ipv6_vrf</samp>](## "avd_design_future.configure_inband_mgmt_ipv6_vrf") | Boolean |  | `False` |  | Available from AVD 6.2.0.<br>Configure `inband_mgmt_vrf` for IPv6 inband management. |
    | [<samp>&nbsp;&nbsp;consistent_uplink_vlans</samp>](## "avd_design_future.consistent_uplink_vlans") | Boolean |  | `False` |  | Available from AVD 6.2.0.<br>Always configure Port-Channel uplinks with consistent 'switchport trunk allowed' on both ends<br>and on all 'uplink_switches' even when available VLANs differ between the 'uplink_switches'. |
    | [<samp>&nbsp;&nbsp;fix_radius_server_group_tls</samp>](## "avd_design_future.fix_radius_server_group_tls") | Boolean |  | `False` |  | Available from AVD 6.2.0.<br>Fix to configure TLS on RADIUS server group members to match their global RADIUS server configurations. |
    | [<samp>&nbsp;&nbsp;only_configure_ipv6_inband_mgmt_prefix_list_when_used</samp>](## "avd_design_future.only_configure_ipv6_inband_mgmt_prefix_list_when_used") | Boolean |  | `False` |  | Available from AVD 6.2.0.<br>Configure `IPv6-PL-L2LEAF-INBAND-MGMT` prefix list only when it is needed. |
    | [<samp>&nbsp;&nbsp;only_configure_mlag_vrfs_peer_group_when_used</samp>](## "avd_design_future.only_configure_mlag_vrfs_peer_group_when_used") | Boolean |  | `False` |  | Available from AVD 6.2.0.<br>Configure the `mlag_ipv4_vrfs_peer` BGP peer group only when needed. |
    | [<samp>&nbsp;&nbsp;only_configure_pvst_border_when_mode_is_mstp</samp>](## "avd_design_future.only_configure_pvst_border_when_mode_is_mstp") | Boolean |  | `False` |  | Available from AVD 6.3.0.<br>PVST border parameters have no effect unless the spanning-tree mode is MSTP.<br>When enabled, AVD renders PVST border configuration only when the spanning-tree mode is set to 'mstp'. |
    | [<samp>&nbsp;&nbsp;only_configure_route_map_connected_to_bgp_vrfs_when_used</samp>](## "avd_design_future.only_configure_route_map_connected_to_bgp_vrfs_when_used") | Boolean |  | `False` |  | Available from AVD 6.3.0.<br>Configure the 'RM-CONN-2-BGP-VRFS' route map only when it is needed.<br>The route map is skipped when both 'underlay_rfc5549' and 'overlay_mlag_rfc5549' are set,<br>since 'redistribute connected route-map' is not required in that case. |
    | [<samp>&nbsp;&nbsp;raise_for_port_channels_without_members</samp>](## "avd_design_future.raise_for_port_channels_without_members") | Boolean |  | `False` |  | Available from AVD 6.2.0.<br>Raise an error if an L3 Port-Channel is configured without any member interfaces. |
    | [<samp>&nbsp;&nbsp;raise_for_underlay_router_with_uplink_type_port_channel</samp>](## "avd_design_future.raise_for_underlay_router_with_uplink_type_port_channel") | Boolean |  | `False` |  | Available from AVD 6.2.0.<br>Raise an error if a node has both 'underlay_router: true' and 'uplink_type: port-channel' set,<br>since this combination is not supported. |
    | [<samp>&nbsp;&nbsp;remove_redundant_ipv4_unicast_for_peer_groups</samp>](## "avd_design_future.remove_redundant_ipv4_unicast_for_peer_groups") | Boolean |  | `False` |  | Available from AVD 6.1.0.<br>Deactivate the IPv4 unicast Address Family for BGP Peer Groups only when IPv4 is activated by default instead of always deactivating it. |

=== "YAML"

    ```yaml
    # Opt-in to future AVD behaviors which will become default behaviors in a future AVD major version.
    avd_design_future:

      # Available from AVD 6.2.0.
      # Configure management interface to accept DHCP default route when the management IP is set to 'dhcp'.
      accept_dhcp_default_route_for_mgmt_ip_dhcp: <bool; default=False>

      # Available from AVD 6.3.0.
      # Configure management interface to accept Router Advertisement default route when the IPv6 management IP is set to 'auto-config'.
      accept_ra_default_route_for_ipv6_mgmt_ip_auto_config: <bool; default=False>

      # Available from AVD 6.3.0.
      # Configure inband management interface to accept DHCP default route when the inband management IP is set to 'dhcp'.
      accept_dhcp_default_route_for_inband_mgmt_ip_dhcp: <bool; default=False>

      # Available from AVD 6.2.0.
      # Configure `inband_mgmt_vrf` for IPv6 inband management.
      configure_inband_mgmt_ipv6_vrf: <bool; default=False>

      # Available from AVD 6.2.0.
      # Always configure Port-Channel uplinks with consistent 'switchport trunk allowed' on both ends
      # and on all 'uplink_switches' even when available VLANs differ between the 'uplink_switches'.
      consistent_uplink_vlans: <bool; default=False>

      # Available from AVD 6.2.0.
      # Fix to configure TLS on RADIUS server group members to match their global RADIUS server configurations.
      fix_radius_server_group_tls: <bool; default=False>

      # Available from AVD 6.2.0.
      # Configure `IPv6-PL-L2LEAF-INBAND-MGMT` prefix list only when it is needed.
      only_configure_ipv6_inband_mgmt_prefix_list_when_used: <bool; default=False>

      # Available from AVD 6.2.0.
      # Configure the `mlag_ipv4_vrfs_peer` BGP peer group only when needed.
      only_configure_mlag_vrfs_peer_group_when_used: <bool; default=False>

      # Available from AVD 6.3.0.
      # PVST border parameters have no effect unless the spanning-tree mode is MSTP.
      # When enabled, AVD renders PVST border configuration only when the spanning-tree mode is set to 'mstp'.
      only_configure_pvst_border_when_mode_is_mstp: <bool; default=False>

      # Available from AVD 6.3.0.
      # Configure the 'RM-CONN-2-BGP-VRFS' route map only when it is needed.
      # The route map is skipped when both 'underlay_rfc5549' and 'overlay_mlag_rfc5549' are set,
      # since 'redistribute connected route-map' is not required in that case.
      only_configure_route_map_connected_to_bgp_vrfs_when_used: <bool; default=False>

      # Available from AVD 6.2.0.
      # Raise an error if an L3 Port-Channel is configured without any member interfaces.
      raise_for_port_channels_without_members: <bool; default=False>

      # Available from AVD 6.2.0.
      # Raise an error if a node has both 'underlay_router: true' and 'uplink_type: port-channel' set,
      # since this combination is not supported.
      raise_for_underlay_router_with_uplink_type_port_channel: <bool; default=False>

      # Available from AVD 6.1.0.
      # Deactivate the IPv4 unicast Address Family for BGP Peer Groups only when IPv4 is activated by default instead of always deactivating it.
      remove_redundant_ipv4_unicast_for_peer_groups: <bool; default=False>
    ```
