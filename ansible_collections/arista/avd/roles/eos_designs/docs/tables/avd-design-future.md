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
    | [<samp>&nbsp;&nbsp;remove_peer_group_mlag_ipv4_vrfs_peer</samp>](## "avd_design_future.remove_peer_group_mlag_ipv4_vrfs_peer") | Boolean |  | `False` |  | Remove the `mlag_ipv4_vrfs_peer` BGP peer group from the generated configuration. |

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

      # Remove the `mlag_ipv4_vrfs_peer` BGP peer group from the generated configuration.
      remove_peer_group_mlag_ipv4_vrfs_peer: <bool; default=False>
    ```
