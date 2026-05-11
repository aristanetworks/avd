<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>avd_design_future</samp>](## "avd_design_future") | Dictionary |  |  |  | Opt-in to future AVD behaviors which will become default behaviors in a future AVD major version. |
    | [<samp>&nbsp;&nbsp;accept_dhcp_default_route_for_mgmt_ip_dhcp</samp>](## "avd_design_future.accept_dhcp_default_route_for_mgmt_ip_dhcp") | Boolean |  | `False` |  | Configure management interface to accept DHCP default route when the management IP is set to 'dhcp'. |
    | [<samp>&nbsp;&nbsp;remove_redundant_ipv4_unicast_for_peer_groups</samp>](## "avd_design_future.remove_redundant_ipv4_unicast_for_peer_groups") | Boolean |  | `False` |  | Deactivate the IPv4 unicast Address Family for BGP Peer Groups only when IPv4 is activated by default instead of always deactivating it. |
    | [<samp>&nbsp;&nbsp;raise_for_port_channels_without_members</samp>](## "avd_design_future.raise_for_port_channels_without_members") | Boolean |  | `False` |  | Raise an error if an L3 Port-Channel is configured without any member interfaces. |
    | [<samp>&nbsp;&nbsp;only_configure_mlag_vrfs_peer_group_when_used</samp>](## "avd_design_future.only_configure_mlag_vrfs_peer_group_when_used") | Boolean |  | `False` |  | Configure the `mlag_ipv4_vrfs_peer` BGP peer group only when needed. |
    | [<samp>&nbsp;&nbsp;raise_for_underlay_router_with_uplink_type_port_channel</samp>](## "avd_design_future.raise_for_underlay_router_with_uplink_type_port_channel") | Boolean |  | `False` |  | Raise an error if a node has both 'underlay_router: true' and 'uplink_type: port-channel' set,<br>since this combination is not supported. |
    | [<samp>&nbsp;&nbsp;configure_inband_mgmt_ipv6_vrf</samp>](## "avd_design_future.configure_inband_mgmt_ipv6_vrf") | Boolean |  | `False` |  | Configure `inband_mgmt_vrf` for IPv6 inband management. |
    | [<samp>&nbsp;&nbsp;only_configure_ipv6_inband_mgmt_prefix_list_when_used</samp>](## "avd_design_future.only_configure_ipv6_inband_mgmt_prefix_list_when_used") | Boolean |  | `False` |  | Configure `IPv6-PL-L2LEAF-INBAND-MGMT` prefix list only when it is needed. |

=== "YAML"

    ```yaml
    # Opt-in to future AVD behaviors which will become default behaviors in a future AVD major version.
    avd_design_future:

      # Configure management interface to accept DHCP default route when the management IP is set to 'dhcp'.
      accept_dhcp_default_route_for_mgmt_ip_dhcp: <bool; default=False>

      # Deactivate the IPv4 unicast Address Family for BGP Peer Groups only when IPv4 is activated by default instead of always deactivating it.
      remove_redundant_ipv4_unicast_for_peer_groups: <bool; default=False>

      # Raise an error if an L3 Port-Channel is configured without any member interfaces.
      raise_for_port_channels_without_members: <bool; default=False>

      # Configure the `mlag_ipv4_vrfs_peer` BGP peer group only when needed.
      only_configure_mlag_vrfs_peer_group_when_used: <bool; default=False>

      # Raise an error if a node has both 'underlay_router: true' and 'uplink_type: port-channel' set,
      # since this combination is not supported.
      raise_for_underlay_router_with_uplink_type_port_channel: <bool; default=False>

      # Configure `inband_mgmt_vrf` for IPv6 inband management.
      configure_inband_mgmt_ipv6_vrf: <bool; default=False>

      # Configure `IPv6-PL-L2LEAF-INBAND-MGMT` prefix list only when it is needed.
      only_configure_ipv6_inband_mgmt_prefix_list_when_used: <bool; default=False>
    ```
