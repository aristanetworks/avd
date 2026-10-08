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
    | [<samp>&nbsp;&nbsp;accept_ra_default_route_for_ipv6_mgmt_ip_auto_config</samp>](## "avd_design_future.accept_ra_default_route_for_ipv6_mgmt_ip_auto_config") | Boolean |  | `False` |  | Available from AVD 6.4.0.<br>Configure management interface to accept Router Advertisement default route when the IPv6 management IP is set to 'auto-config'. |
    | [<samp>&nbsp;&nbsp;accept_dhcp_default_route_for_inband_mgmt_ip_dhcp</samp>](## "avd_design_future.accept_dhcp_default_route_for_inband_mgmt_ip_dhcp") | Boolean |  | `False` |  | Available from AVD 6.3.0.<br>Configure inband management interface to accept DHCP default route when the inband management IP is set to 'dhcp'. |
    | [<samp>&nbsp;&nbsp;allow_recursive_profile_inheritance</samp>](## "avd_design_future.allow_recursive_profile_inheritance") | Boolean |  | `False` |  | Available from AVD 6.5.0.<br>Allow `parent_profile` to inherit from its own `parent_profile` in `port_profiles`, `device_profiles`, `svi_profiles` and `l2vlan_profiles`. |
    | [<samp>&nbsp;&nbsp;configure_inband_mgmt_ipv6_vrf</samp>](## "avd_design_future.configure_inband_mgmt_ipv6_vrf") | Boolean |  | `False` |  | Available from AVD 6.2.0.<br>Configure `inband_mgmt_vrf` for IPv6 inband management. |
    | [<samp>&nbsp;&nbsp;consistent_uplink_vlans</samp>](## "avd_design_future.consistent_uplink_vlans") | Boolean |  | `False` |  | Available from AVD 6.2.0.<br>Always configure Port-Channel uplinks with consistent 'switchport trunk allowed' on both ends<br>and on all 'uplink_switches' even when available VLANs differ between the 'uplink_switches'. |
    | [<samp>&nbsp;&nbsp;fix_address_locking_dhcp_server_interfaces</samp>](## "avd_design_future.fix_address_locking_dhcp_server_interfaces") | Boolean |  | `False` |  | Available from AVD 6.4.0.<br>Fix support for `address_locking_settings.dhcp_server_interfaces`.<br>When enabled, `address_locking_settings.dhcp_server_interfaces` and `address_locking_settings.local_interface` are mutually exclusive. |
    | [<samp>&nbsp;&nbsp;fix_match_ipv6_prefix_list_on_mlag_route_map</samp>](## "avd_design_future.fix_match_ipv6_prefix_list_on_mlag_route_map") | Boolean |  | `False` |  | Available from AVD 6.4.0.<br>Fix to properly configure the `RM-CONN-2-BGP-VRFS` route-map with `match ipv6 address prefix-list`<br>instead of `match ip address prefix-list` when using `underlay_ipv6_numbered`. |
    | [<samp>&nbsp;&nbsp;fix_mlag_ibgp_peering_ipv6_pool</samp>](## "avd_design_future.fix_mlag_ibgp_peering_ipv6_pool") | Boolean |  | `False` |  | Available from AVD 6.5.0.<br>Fix the MLAG iBGP peering BGP neighbor in VRFs when using `underlay_ipv6_numbered`.<br>When enabled, the BGP neighbor is derived from the same IPv6 pool as the MLAG iBGP peering SVI,<br>using `mlag_ibgp_peering_ipv6_pool` when set, and `mlag_ibgp_peering_ipv4_pool` is ignored. |
    | [<samp>&nbsp;&nbsp;fix_mlag_vrf_peer_group_address_families</samp>](## "avd_design_future.fix_mlag_vrf_peer_group_address_families") | Boolean |  | `False` |  | Available from AVD 6.5.0.<br>Configure the same address families on the shared (`bgp_peer_groups.mlag_ipv4_underlay_peer`) and the dedicated<br>(`bgp_peer_groups.mlag_ipv4_vrfs_peer`) BGP peer groups for MLAG iBGP peerings in VRFs,<br>including the default VRF with `underlay_routing_protocol: none`.<br>The address families of the shared peer group also apply to the underlay MLAG iBGP peering in the default VRF.<br>The MLAG iBGP sessions in VRFs run over IPv6 with `underlay_rfc5549` and `overlay_mlag_rfc5549` (link-local), or with `underlay_ipv6_numbered`.<br>They run over IPv4 otherwise.<br>When they run over IPv6:<br>- With `overlay_mlag_rfc5549: true`, activate IPv4 with `next-hop address-family ipv6 originate`.<br>  With the shared peer group, `ip routing ipv6 interfaces` is also configured for the underlay MLAG iBGP peering.<br>- With `overlay_mlag_rfc5549: false`, IPv4 is not activated, since IPv4 routes without an IPv6 next hop cannot be used.<br>- With `underlay_ipv6: true`, activate IPv6.<br>`underlay_ipv6: true` is the way to carry IPv6 routes over the MLAG iBGP peerings in VRFs, and it only works when these sessions run over IPv6.<br>Raise an error when the MLAG iBGP sessions in VRFs run over IPv4 with `overlay_mlag_rfc5549: true` or with `underlay_ipv6: true`. |
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

      # Available from AVD 6.4.0.
      # Configure management interface to accept Router Advertisement default route when the IPv6 management IP is set to 'auto-config'.
      accept_ra_default_route_for_ipv6_mgmt_ip_auto_config: <bool; default=False>

      # Available from AVD 6.3.0.
      # Configure inband management interface to accept DHCP default route when the inband management IP is set to 'dhcp'.
      accept_dhcp_default_route_for_inband_mgmt_ip_dhcp: <bool; default=False>

      # Available from AVD 6.5.0.
      # Allow `parent_profile` to inherit from its own `parent_profile` in `port_profiles`, `device_profiles`, `svi_profiles` and `l2vlan_profiles`.
      allow_recursive_profile_inheritance: <bool; default=False>

      # Available from AVD 6.2.0.
      # Configure `inband_mgmt_vrf` for IPv6 inband management.
      configure_inband_mgmt_ipv6_vrf: <bool; default=False>

      # Available from AVD 6.2.0.
      # Always configure Port-Channel uplinks with consistent 'switchport trunk allowed' on both ends
      # and on all 'uplink_switches' even when available VLANs differ between the 'uplink_switches'.
      consistent_uplink_vlans: <bool; default=False>

      # Available from AVD 6.4.0.
      # Fix support for `address_locking_settings.dhcp_server_interfaces`.
      # When enabled, `address_locking_settings.dhcp_server_interfaces` and `address_locking_settings.local_interface` are mutually exclusive.
      fix_address_locking_dhcp_server_interfaces: <bool; default=False>

      # Available from AVD 6.4.0.
      # Fix to properly configure the `RM-CONN-2-BGP-VRFS` route-map with `match ipv6 address prefix-list`
      # instead of `match ip address prefix-list` when using `underlay_ipv6_numbered`.
      fix_match_ipv6_prefix_list_on_mlag_route_map: <bool; default=False>

      # Available from AVD 6.5.0.
      # Fix the MLAG iBGP peering BGP neighbor in VRFs when using `underlay_ipv6_numbered`.
      # When enabled, the BGP neighbor is derived from the same IPv6 pool as the MLAG iBGP peering SVI,
      # using `mlag_ibgp_peering_ipv6_pool` when set, and `mlag_ibgp_peering_ipv4_pool` is ignored.
      fix_mlag_ibgp_peering_ipv6_pool: <bool; default=False>

      # Available from AVD 6.5.0.
      # Configure the same address families on the shared (`bgp_peer_groups.mlag_ipv4_underlay_peer`) and the dedicated
      # (`bgp_peer_groups.mlag_ipv4_vrfs_peer`) BGP peer groups for MLAG iBGP peerings in VRFs,
      # including the default VRF with `underlay_routing_protocol: none`.
      # The address families of the shared peer group also apply to the underlay MLAG iBGP peering in the default VRF.
      # The MLAG iBGP sessions in VRFs run over IPv6 with `underlay_rfc5549` and `overlay_mlag_rfc5549` (link-local), or with `underlay_ipv6_numbered`.
      # They run over IPv4 otherwise.
      # When they run over IPv6:
      # - With `overlay_mlag_rfc5549: true`, activate IPv4 with `next-hop address-family ipv6 originate`.
      #   With the shared peer group, `ip routing ipv6 interfaces` is also configured for the underlay MLAG iBGP peering.
      # - With `overlay_mlag_rfc5549: false`, IPv4 is not activated, since IPv4 routes without an IPv6 next hop cannot be used.
      # - With `underlay_ipv6: true`, activate IPv6.
      # `underlay_ipv6: true` is the way to carry IPv6 routes over the MLAG iBGP peerings in VRFs, and it only works when these sessions run over IPv6.
      # Raise an error when the MLAG iBGP sessions in VRFs run over IPv4 with `overlay_mlag_rfc5549: true` or with `underlay_ipv6: true`.
      fix_mlag_vrf_peer_group_address_families: <bool; default=False>

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
