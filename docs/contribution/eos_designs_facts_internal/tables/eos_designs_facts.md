<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>id</samp>](## "id") | Integer |  |  |  |  |
    | [<samp>type</samp>](## "type") | String | Required |  |  |  |
    | [<samp>platform</samp>](## "platform") | String |  |  |  |  |
    | [<samp>is_deployed</samp>](## "is_deployed") | Boolean | Required |  |  |  |
    | [<samp>serial_number</samp>](## "serial_number") | String |  |  |  |  |
    | [<samp>mgmt_interface</samp>](## "mgmt_interface") | String |  |  |  |  |
    | [<samp>mgmt_ip</samp>](## "mgmt_ip") | String |  |  |  |  |
    | [<samp>mpls_lsr</samp>](## "mpls_lsr") | Boolean | Required |  |  |  |
    | [<samp>evpn_multicast</samp>](## "evpn_multicast") | Boolean |  |  |  |  |
    | [<samp>loopback_ipv4_pool</samp>](## "loopback_ipv4_pool") | String |  |  |  |  |
    | [<samp>uplink_ipv4_pool</samp>](## "uplink_ipv4_pool") | String |  |  |  |  |
    | [<samp>downlink_pools</samp>](## "downlink_pools") | List, items: Dictionary |  |  |  | IPv4 pools used for links to downlink switches. Set this on the parent switch. Cannot be combined with `uplink_ipv4_pool` set on the downlink switch. |
    | [<samp>&nbsp;&nbsp;-&nbsp;ipv4_pool</samp>](## "downlink_pools.[].ipv4_pool") | String |  |  | Format: ipv4_pool | Comma separated list of prefixes (IPv4 address/Mask) or ranges (IPv4_address-IPv4_address).<br>IPv4 subnets used for links to downlink switches will be derived from this pool based on index the peer's uplink interface's index in 'downlink_interfaces'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;downlink_interfaces</samp>](## "downlink_pools.[].downlink_interfaces") | List, items: String |  |  |  | List of downlink interfaces or ranges of interfaces to use this pool. The index of the interface in this list will determine which subnet will be taken from the pool. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "downlink_pools.[].downlink_interfaces.[]") | String |  |  |  |  |
    | [<samp>bgp_as</samp>](## "bgp_as") | String |  |  |  |  |
    | [<samp>underlay_routing_protocol</samp>](## "underlay_routing_protocol") | String | Required |  |  |  |
    | [<samp>vtep_loopback_ipv4_pool</samp>](## "vtep_loopback_ipv4_pool") | String |  |  |  |  |
    | [<samp>inband_mgmt_subnet</samp>](## "inband_mgmt_subnet") | String |  |  |  |  |
    | [<samp>inband_mgmt_ipv6_subnet</samp>](## "inband_mgmt_ipv6_subnet") | String |  |  |  |  |
    | [<samp>inband_mgmt_vlan</samp>](## "inband_mgmt_vlan") | Integer |  |  |  |  |
    | [<samp>inband_ztp</samp>](## "inband_ztp") | Boolean |  |  |  |  |
    | [<samp>inband_ztp_vlan</samp>](## "inband_ztp_vlan") | Integer |  |  |  |  |
    | [<samp>inband_ztp_lacp_fallback_delay</samp>](## "inband_ztp_lacp_fallback_delay") | Integer |  |  |  |  |
    | [<samp>dc_name</samp>](## "dc_name") | String |  |  |  |  |
    | [<samp>group</samp>](## "group") | String |  |  |  |  |
    | [<samp>router_id</samp>](## "router_id") | String |  |  |  |  |
    | [<samp>inband_mgmt_ip</samp>](## "inband_mgmt_ip") | String |  |  |  | Used for fabric docs. |
    | [<samp>inband_mgmt_interface</samp>](## "inband_mgmt_interface") | String |  |  |  | Used for fabric docs. |
    | [<samp>pod</samp>](## "pod") | String | Required |  |  | Used for fabric docs. |
    | [<samp>connected_endpoints_keys</samp>](## "connected_endpoints_keys") | List, items: Dictionary | Required |  |  | List of connected_endpoints_keys in use on this device.<br>Used for fabric docs. |
    | [<samp>&nbsp;&nbsp;-&nbsp;key</samp>](## "connected_endpoints_keys.[].key") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "connected_endpoints_keys.[].type") | String |  |  |  | Type used for documentation. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "connected_endpoints_keys.[].description") | String |  |  |  | Description used for documentation. |
    | [<samp>port_profile_names</samp>](## "port_profile_names") | List, items: Dictionary |  |  |  | List of port_profiles configured - including the ones not in use.<br>Used for fabric docs. |
    | [<samp>&nbsp;&nbsp;-&nbsp;profile</samp>](## "port_profile_names.[].profile") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;parent_profile</samp>](## "port_profile_names.[].parent_profile") | String |  |  |  |  |
    | [<samp>mlag_peer</samp>](## "mlag_peer") | String |  |  |  |  |
    | [<samp>mlag_port_channel_id</samp>](## "mlag_port_channel_id") | Integer |  |  |  |  |
    | [<samp>mlag_interfaces</samp>](## "mlag_interfaces") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "mlag_interfaces.[]") | String |  |  |  |  |
    | [<samp>mlag_ip</samp>](## "mlag_ip") | String |  |  |  |  |
    | [<samp>mlag_l3_ip</samp>](## "mlag_l3_ip") | String |  |  |  |  |
    | [<samp>mlag_switch_ids</samp>](## "mlag_switch_ids") | Dictionary |  |  |  | The switch ids of both primary and secondary switches for a this node group. |
    | [<samp>&nbsp;&nbsp;primary</samp>](## "mlag_switch_ids.primary") | Integer | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;secondary</samp>](## "mlag_switch_ids.secondary") | Integer | Required |  |  |  |
    | [<samp>evpn_role</samp>](## "evpn_role") | String |  |  |  |  |
    | [<samp>mpls_overlay_role</samp>](## "mpls_overlay_role") | String |  |  |  |  |
    | [<samp>evpn_route_servers</samp>](## "evpn_route_servers") | List, items: String |  |  |  | For evpn clients the default value for EVPN Route Servers is the content of the uplink_switches variable set elsewhere.<br>For all other evpn roles there is no default. |
    | [<samp>&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "evpn_route_servers.[]") | String |  |  |  |  |
    | [<samp>mpls_route_reflectors</samp>](## "mpls_route_reflectors") | List, items: String |  |  |  | List of inventory hostname acting as MPLS route-reflectors. |
    | [<samp>&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "mpls_route_reflectors.[]") | String |  |  |  | Inventory_hostname_of_mpls_route_reflectors. |
    | [<samp>overlay</samp>](## "overlay") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;peering_address</samp>](## "overlay.peering_address") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;evpn_mpls</samp>](## "overlay.evpn_mpls") | Boolean | Required |  |  |  |
    | [<samp>vtep_ip</samp>](## "vtep_ip") | String |  |  |  |  |
    | [<samp>max_parallel_uplinks</samp>](## "max_parallel_uplinks") | Integer |  | `1` |  | Number of parallel links towards uplink switches.<br>Changing this value may change interface naming on uplinks (and corresponding downlinks).<br>Can be used to reserve interfaces for future parallel uplinks.<br> |
    | [<samp>max_uplink_switches</samp>](## "max_uplink_switches") | Integer | Required |  |  |  |
    | [<samp>uplinks</samp>](## "uplinks") | List, items: Dictionary | Required |  |  | List of uplinks with all parameters<br>These facts are leveraged by templates for this device when rendering uplinks<br>and by templates for peer devices when rendering downlinks |
    | [<samp>&nbsp;&nbsp;-&nbsp;interface</samp>](## "uplinks.[].interface") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;peer</samp>](## "uplinks.[].peer") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;peer_interface</samp>](## "uplinks.[].peer_interface") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;peer_type</samp>](## "uplinks.[].peer_type") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;peer_is_deployed</samp>](## "uplinks.[].peer_is_deployed") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;peer_bgp_as</samp>](## "uplinks.[].peer_bgp_as") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "uplinks.[].type") | String | Required |  | Valid Values:<br>- <code>underlay_p2p</code><br>- <code>underlay_l2</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;speed</samp>](## "uplinks.[].speed") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;bfd</samp>](## "uplinks.[].bfd") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;peer_speed</samp>](## "uplinks.[].peer_speed") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ptp</samp>](## "uplinks.[].ptp") | Dictionary |  |  |  | Enable PTP on all infrastructure links. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enable</samp>](## "uplinks.[].ptp.enable") | Boolean |  | `False` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mac_security</samp>](## "uplinks.[].mac_security") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;profile</samp>](## "uplinks.[].mac_security.profile") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;underlay_multicast</samp>](## "uplinks.[].underlay_multicast") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_enable</samp>](## "uplinks.[].ipv6_enable") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;prefix_length</samp>](## "uplinks.[].prefix_length") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "uplinks.[].ip_address") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;peer_ip_address</samp>](## "uplinks.[].peer_ip_address") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;link_tracking_groups</samp>](## "uplinks.[].link_tracking_groups") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "uplinks.[].link_tracking_groups.[].name") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction</samp>](## "uplinks.[].link_tracking_groups.[].direction") | String | Required |  | Valid Values:<br>- <code>upstream</code><br>- <code>downstream</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;peer_node_group</samp>](## "uplinks.[].peer_node_group") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;node_group</samp>](## "uplinks.[].node_group") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mlag</samp>](## "uplinks.[].mlag") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;peer_mlag</samp>](## "uplinks.[].peer_mlag") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;channel_group_id</samp>](## "uplinks.[].channel_group_id") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;peer_channel_group_id</samp>](## "uplinks.[].peer_channel_group_id") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;trunk_groups</samp>](## "uplinks.[].trunk_groups") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "uplinks.[].trunk_groups.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;peer_trunk_groups</samp>](## "uplinks.[].peer_trunk_groups") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "uplinks.[].peer_trunk_groups.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vlans</samp>](## "uplinks.[].vlans") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;native_vlan</samp>](## "uplinks.[].native_vlan") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;short_esi</samp>](## "uplinks.[].short_esi") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;peer_short_esi</samp>](## "uplinks.[].peer_short_esi") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_portfast</samp>](## "uplinks.[].spanning_tree_portfast") | String |  |  | Valid Values:<br>- <code>edge</code><br>- <code>network</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;peer_spanning_tree_portfast</samp>](## "uplinks.[].peer_spanning_tree_portfast") | String |  |  | Valid Values:<br>- <code>edge</code><br>- <code>network</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;sflow_enabled</samp>](## "uplinks.[].sflow_enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;flow_tracking</samp>](## "uplinks.[].flow_tracking") | Dictionary |  |  |  | Enable flow-tracking on all fabric uplinks. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "uplinks.[].flow_tracking.enabled") | Boolean |  | `False` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "uplinks.[].flow_tracking.name") | String |  | `FLOW-TRACKER` |  | Flow tracker name as defined in flow_tracking_settings. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;inband_ztp_vlan</samp>](## "uplinks.[].inband_ztp_vlan") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;inband_ztp_lacp_fallback_delay</samp>](## "uplinks.[].inband_ztp_lacp_fallback_delay") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;dhcp_server</samp>](## "uplinks.[].dhcp_server") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "uplinks.[].structured_config") | Dictionary |  |  |  | Custom structured config applied to "uplink_interfaces", and "uplink_switch_interfaces".<br>When uplink_type == "p2p", custom structured config added under ethernet_interfaces.[name=<interface>] for eos_cli_config_gen overrides the settings on the ethernet interface level.<br>When uplink_type == "port-channel", custom structured config added under port_channel_interfaces.[name=<interface>] for eos_cli_config_gen overrides the settings on the port-channel interface level.<br>"uplink_structured_config" is applied after "structured_config", so it can override "structured_config" defined on node-level.<br>Note! The content of this dictionary is _not_ validated by the schema, since it can be either ethernet_interfaces or port_channel_interfaces.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;subinterfaces</samp>](## "uplinks.[].subinterfaces") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;interface</samp>](## "uplinks.[].subinterfaces.[].interface") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer_interface</samp>](## "uplinks.[].subinterfaces.[].peer_interface") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "uplinks.[].subinterfaces.[].vrf") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;encapsulation_dot1q_vlan</samp>](## "uplinks.[].subinterfaces.[].encapsulation_dot1q_vlan") | Integer | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_enable</samp>](## "uplinks.[].subinterfaces.[].ipv6_enable") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefix_length</samp>](## "uplinks.[].subinterfaces.[].prefix_length") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "uplinks.[].subinterfaces.[].ip_address") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer_ip_address</samp>](## "uplinks.[].subinterfaces.[].peer_ip_address") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "uplinks.[].subinterfaces.[].structured_config") | Dictionary |  |  |  | Custom structured config applied to "uplink_interfaces", and "uplink_switch_interfaces".<br>When uplink_type == "p2p", custom structured config added under ethernet_interfaces.[name=<interface>] for eos_cli_config_gen overrides the settings on the ethernet interface level.<br>When uplink_type == "port-channel", custom structured config added under port_channel_interfaces.[name=<interface>] for eos_cli_config_gen overrides the settings on the port-channel interface level.<br>"uplink_structured_config" is applied after "structured_config", so it can override "structured_config" defined on node-level.<br>Note! The content of this dictionary is _not_ validated by the schema, since it can be either ethernet_interfaces or port_channel_interfaces.<br> |
    | [<samp>uplink_peers</samp>](## "uplink_peers") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "uplink_peers.[]") | String |  |  |  |  |
    | [<samp>uplink_switch_vrfs</samp>](## "uplink_switch_vrfs") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "uplink_switch_vrfs.[]") | String |  |  |  |  |
    | [<samp>vlans</samp>](## "vlans") | String | Required |  |  | Compressed list of vlans to be defined on this switch after filtering network services.<br>The filter is based on filter.tenants, filter.tags but not filter.only_vlans_in_use.<br><br>Ex. "1-100, 201-202"<br><br>This excludes the optional "uplink_native_vlan" if that vlan is not used for anything else.<br>This is to ensure that native vlan is not necessarily permitted on the uplink trunk. |
    | [<samp>endpoint_vlans</samp>](## "endpoint_vlans") | String |  |  |  | Compressed list of vlans in use by endpoints connected to this switch, downstream switches or MLAG peer and it's downstream switches. |
    | [<samp>local_endpoint_trunk_groups</samp>](## "local_endpoint_trunk_groups") | List, items: String |  |  |  | List of trunk_groups in use by endpoints connected to this switch. |
    | [<samp>&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "local_endpoint_trunk_groups.[]") | String |  |  |  |  |
    | [<samp>endpoint_trunk_groups</samp>](## "endpoint_trunk_groups") | List, items: String |  |  |  | List of trunk_groups in use by endpoints connected to this switch, downstream switches or MLAG peer and it's downstream switches. |
    | [<samp>&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "endpoint_trunk_groups.[]") | String |  |  |  |  |
    | [<samp>wan_path_groups</samp>](## "wan_path_groups") | List, items: Dictionary |  |  |  | List of path-groups used for the WAN configuration. |
    | [<samp>&nbsp;&nbsp;-&nbsp;interfaces</samp>](## "wan_path_groups.[].interfaces") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "wan_path_groups.[].interfaces.[].name") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;public_ip</samp>](## "wan_path_groups.[].interfaces.[].public_ip") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;connected_to_pathfinder</samp>](## "wan_path_groups.[].interfaces.[].connected_to_pathfinder") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;wan_circuit_id</samp>](## "wan_path_groups.[].interfaces.[].wan_circuit_id") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "wan_path_groups.[].name") | String | Required, Unique |  |  | Path-group name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;id</samp>](## "wan_path_groups.[].id") | Integer | Required |  |  | Path-group id.<br>Required until an auto ID algorithm is implemented. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "wan_path_groups.[].description") | String |  |  |  | Additional information about the path-group for documentation purposes. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipsec</samp>](## "wan_path_groups.[].ipsec") | Dictionary |  |  |  | Configuration of IPSec at the path-group level. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dynamic_peers</samp>](## "wan_path_groups.[].ipsec.dynamic_peers") | Boolean |  | `True` |  | Enable IPSec for dynamic peers. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;static_peers</samp>](## "wan_path_groups.[].ipsec.static_peers") | Boolean |  | `True` |  | Enable IPSec for static peers. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;import_path_groups</samp>](## "wan_path_groups.[].import_path_groups") | List, items: Dictionary |  |  |  | List of path-groups to import in this path-group. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;remote</samp>](## "wan_path_groups.[].import_path_groups.[].remote") | String |  |  |  | Remote path-group to import. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;local</samp>](## "wan_path_groups.[].import_path_groups.[].local") | String |  |  |  | Optional, if not set, the path-group `name` is used as local. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;default_preference</samp>](## "wan_path_groups.[].default_preference") | String |  | `preferred` |  | Preference value used when a preference is not given for a path-group in the `wan_virtual_topologies.policies` input or when<br>the path-group is used in an auto generated policy except if `excluded_from_default_policy` is set to `true.<br><br>Valid values are 1-65535 | "preferred" | "alternate".<br><br>`preferred` is converted to priority 1.<br>`alternate` is converted to priority 2. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;excluded_from_default_policy</samp>](## "wan_path_groups.[].excluded_from_default_policy") | Boolean |  | `False` |  | When set to `true`, the path-group is excluded from AVD auto generated policies. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;dps_keepalive</samp>](## "wan_path_groups.[].dps_keepalive") | Dictionary |  |  |  | Period between the transmission of consecutive keepalive messages, and failure threshold. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interval</samp>](## "wan_path_groups.[].dps_keepalive.interval") | String |  |  |  | Interval in milliseconds. Valid values are 50-60000 | "auto".<br><br>When auto, the interval and failure_threshold are automatically determined based on<br>path state. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;failure_threshold</samp>](## "wan_path_groups.[].dps_keepalive.failure_threshold") | Integer |  | `5` | Min: 2<br>Max: 100 | Failure threshold in number of lost keep-alive messages. |
    | [<samp>uplink_switch_interfaces</samp>](## "uplink_switch_interfaces") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "uplink_switch_interfaces.[]") | String |  |  |  |  |
    | [<samp>downlink_switches</samp>](## "downlink_switches") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "downlink_switches.[]") | String |  |  |  |  |
    | [<samp>evpn_route_server_clients</samp>](## "evpn_route_server_clients") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "evpn_route_server_clients.[]") | String |  |  |  |  |
    | [<samp>mpls_route_reflector_clients</samp>](## "mpls_route_reflector_clients") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "mpls_route_reflector_clients.[]") | String |  |  |  |  |

=== "YAML"

    ```yaml
    id: <int>
    type: <str; required>
    platform: <str>
    is_deployed: <bool; required>
    serial_number: <str>
    mgmt_interface: <str>
    mgmt_ip: <str>
    mpls_lsr: <bool; required>
    evpn_multicast: <bool>
    loopback_ipv4_pool: <str>
    uplink_ipv4_pool: <str>

    # IPv4 pools used for links to downlink switches. Set this on the parent switch. Cannot be combined with `uplink_ipv4_pool` set on the downlink switch.
    downlink_pools:

        # Comma separated list of prefixes (IPv4 address/Mask) or ranges (IPv4_address-IPv4_address).
        # IPv4 subnets used for links to downlink switches will be derived from this pool based on index the peer's uplink interface's index in 'downlink_interfaces'.
      - ipv4_pool: <str>

        # List of downlink interfaces or ranges of interfaces to use this pool. The index of the interface in this list will determine which subnet will be taken from the pool.
        downlink_interfaces:
          - <str>
    bgp_as: <str>
    underlay_routing_protocol: <str; required>
    vtep_loopback_ipv4_pool: <str>
    inband_mgmt_subnet: <str>
    inband_mgmt_ipv6_subnet: <str>
    inband_mgmt_vlan: <int>
    inband_ztp: <bool>
    inband_ztp_vlan: <int>
    inband_ztp_lacp_fallback_delay: <int>
    dc_name: <str>
    group: <str>
    router_id: <str>

    # Used for fabric docs.
    inband_mgmt_ip: <str>

    # Used for fabric docs.
    inband_mgmt_interface: <str>

    # Used for fabric docs.
    pod: <str; required>

    # List of connected_endpoints_keys in use on this device.
    # Used for fabric docs.
    connected_endpoints_keys: # required
      - key: <str; required; unique>

        # Type used for documentation.
        type: <str>

        # Description used for documentation.
        description: <str>

    # List of port_profiles configured - including the ones not in use.
    # Used for fabric docs.
    port_profile_names:
      - profile: <str; required>
        parent_profile: <str>
    mlag_peer: <str>
    mlag_port_channel_id: <int>
    mlag_interfaces:
      - <str>
    mlag_ip: <str>
    mlag_l3_ip: <str>

    # The switch ids of both primary and secondary switches for a this node group.
    mlag_switch_ids:
      primary: <int; required>
      secondary: <int; required>
    evpn_role: <str>
    mpls_overlay_role: <str>

    # For evpn clients the default value for EVPN Route Servers is the content of the uplink_switches variable set elsewhere.
    # For all other evpn roles there is no default.
    evpn_route_servers:
      - <str>

    # List of inventory hostname acting as MPLS route-reflectors.
    mpls_route_reflectors:

        # Inventory_hostname_of_mpls_route_reflectors.
      - <str>
    overlay:
      peering_address: <str>
      evpn_mpls: <bool; required>
    vtep_ip: <str>

    # Number of parallel links towards uplink switches.
    # Changing this value may change interface naming on uplinks (and corresponding downlinks).
    # Can be used to reserve interfaces for future parallel uplinks.
    max_parallel_uplinks: <int; default=1>
    max_uplink_switches: <int; required>

    # List of uplinks with all parameters
    # These facts are leveraged by templates for this device when rendering uplinks
    # and by templates for peer devices when rendering downlinks
    uplinks: # required
      - interface: <str; required>
        peer: <str; required>
        peer_interface: <str; required>
        peer_type: <str; required>
        peer_is_deployed: <bool; required>
        peer_bgp_as: <str>
        type: <str; "underlay_p2p" | "underlay_l2"; required>
        speed: <str>
        bfd: <bool>
        peer_speed: <str>

        # Enable PTP on all infrastructure links.
        ptp:
          enable: <bool; default=False>
        mac_security:
          profile: <str; required>
        underlay_multicast: <bool>
        ipv6_enable: <bool>
        prefix_length: <int>
        ip_address: <str>
        peer_ip_address: <str>
        link_tracking_groups:
          - name: <str; required; unique>
            direction: <str; "upstream" | "downstream"; required>
        peer_node_group: <str>
        node_group: <str>
        mlag: <bool>
        peer_mlag: <bool>
        channel_group_id: <int>
        peer_channel_group_id: <int>
        trunk_groups:
          - <str>
        peer_trunk_groups:
          - <str>
        vlans: <str>
        native_vlan: <int>
        short_esi: <str>
        peer_short_esi: <str>
        spanning_tree_portfast: <str; "edge" | "network">
        peer_spanning_tree_portfast: <str; "edge" | "network">
        sflow_enabled: <bool>

        # Enable flow-tracking on all fabric uplinks.
        flow_tracking:
          enabled: <bool; default=False>

          # Flow tracker name as defined in flow_tracking_settings.
          name: <str; default="FLOW-TRACKER">
        inband_ztp_vlan: <int>
        inband_ztp_lacp_fallback_delay: <int>
        dhcp_server: <bool>

        # Custom structured config applied to "uplink_interfaces", and "uplink_switch_interfaces".
        # When uplink_type == "p2p", custom structured config added under ethernet_interfaces.[name=<interface>] for eos_cli_config_gen overrides the settings on the ethernet interface level.
        # When uplink_type == "port-channel", custom structured config added under port_channel_interfaces.[name=<interface>] for eos_cli_config_gen overrides the settings on the port-channel interface level.
        # "uplink_structured_config" is applied after "structured_config", so it can override "structured_config" defined on node-level.
        # Note! The content of this dictionary is _not_ validated by the schema, since it can be either ethernet_interfaces or port_channel_interfaces.
        structured_config: <dict>
        subinterfaces:
          - interface: <str; required; unique>
            peer_interface: <str; required>
            vrf: <str; required>
            encapsulation_dot1q_vlan: <int; required>
            ipv6_enable: <bool>
            prefix_length: <int>
            ip_address: <str>
            peer_ip_address: <str>

            # Custom structured config applied to "uplink_interfaces", and "uplink_switch_interfaces".
            # When uplink_type == "p2p", custom structured config added under ethernet_interfaces.[name=<interface>] for eos_cli_config_gen overrides the settings on the ethernet interface level.
            # When uplink_type == "port-channel", custom structured config added under port_channel_interfaces.[name=<interface>] for eos_cli_config_gen overrides the settings on the port-channel interface level.
            # "uplink_structured_config" is applied after "structured_config", so it can override "structured_config" defined on node-level.
            # Note! The content of this dictionary is _not_ validated by the schema, since it can be either ethernet_interfaces or port_channel_interfaces.
            structured_config: <dict>
    uplink_peers:
      - <str>
    uplink_switch_vrfs:
      - <str>

    # Compressed list of vlans to be defined on this switch after filtering network services.
    # The filter is based on filter.tenants, filter.tags but not filter.only_vlans_in_use.
    #
    # Ex. "1-100, 201-202"
    #
    # This excludes the optional "uplink_native_vlan" if that vlan is not used for anything else.
    # This is to ensure that native vlan is not necessarily permitted on the uplink trunk.
    vlans: <str; required>

    # Compressed list of vlans in use by endpoints connected to this switch, downstream switches or MLAG peer and it's downstream switches.
    endpoint_vlans: <str>

    # List of trunk_groups in use by endpoints connected to this switch.
    local_endpoint_trunk_groups:
      - <str>

    # List of trunk_groups in use by endpoints connected to this switch, downstream switches or MLAG peer and it's downstream switches.
    endpoint_trunk_groups:
      - <str>

    # List of path-groups used for the WAN configuration.
    wan_path_groups:
      - interfaces:
          - name: <str; required>
            public_ip: <str>
            connected_to_pathfinder: <bool; required>
            wan_circuit_id: <str>

        # Path-group name.
        name: <str; required; unique>

        # Path-group id.
        # Required until an auto ID algorithm is implemented.
        id: <int; required>

        # Additional information about the path-group for documentation purposes.
        description: <str>

        # Configuration of IPSec at the path-group level.
        ipsec:

          # Enable IPSec for dynamic peers.
          dynamic_peers: <bool; default=True>

          # Enable IPSec for static peers.
          static_peers: <bool; default=True>

        # List of path-groups to import in this path-group.
        import_path_groups:

            # Remote path-group to import.
          - remote: <str>

            # Optional, if not set, the path-group `name` is used as local.
            local: <str>

        # Preference value used when a preference is not given for a path-group in the `wan_virtual_topologies.policies` input or when
        # the path-group is used in an auto generated policy except if `excluded_from_default_policy` is set to `true.
        #
        # Valid values are 1-65535 | "preferred" | "alternate".
        #
        # `preferred` is converted to priority 1.
        # `alternate` is converted to priority 2.
        default_preference: <str; default="preferred">

        # When set to `true`, the path-group is excluded from AVD auto generated policies.
        excluded_from_default_policy: <bool; default=False>

        # Period between the transmission of consecutive keepalive messages, and failure threshold.
        dps_keepalive:

          # Interval in milliseconds. Valid values are 50-60000 | "auto".
          #
          # When auto, the interval and failure_threshold are automatically determined based on
          # path state.
          interval: <str>

          # Failure threshold in number of lost keep-alive messages.
          failure_threshold: <int; 2-100; default=5>
    uplink_switch_interfaces:
      - <str>
    downlink_switches:
      - <str>
    evpn_route_server_clients:
      - <str>
    mpls_route_reflector_clients:
      - <str>
    ```
