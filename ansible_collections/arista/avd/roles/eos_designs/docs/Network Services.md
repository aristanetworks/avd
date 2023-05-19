---
search:
  boost: 2
---

# Network Services

## <Network Services Keys.Name>

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>&lt;network_services_keys.name&gt;</samp>](## "&lt;network_services_keys.name&gt;") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;- name</samp>](## "&lt;network_services_keys.name&gt;.[].name") | String | Required, Unique |  |  | Specify a tenant name.<br>Tenant provide a construct to group L3 VRFs and L2 VLANs.<br>Networks services can be filtered by tenant name.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mac_vrf_vni_base</samp>](## "&lt;network_services_keys.name&gt;.[].mac_vrf_vni_base") | Integer |  |  | Min: 0<br>Max: 16770000 | Base number for MAC VRF VXLAN Network Identifier (required with VXLAN).<br>VXLAN VNI is derived from the base number with simple addition.<br>i.e. mac_vrf_vni_base = 10000, svi 100 = VNI 10100, svi 300 = VNI 10300.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mac_vrf_id_base</samp>](## "&lt;network_services_keys.name&gt;.[].mac_vrf_id_base") | Integer |  |  | Min: 0<br>Max: 16770000 | If not set, "mac_vrf_vni_base" will be used.<br>Base number for MAC VRF RD/RT ID (Required unless mac_vrf_vni_base is set)<br>ID is derived from the base number with simple addition.<br>i.e. mac_vrf_id_base = 10000, svi 100 = RD/RT 10100, svi 300 = RD/RT 10300.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vlan_aware_bundle_number_base</samp>](## "&lt;network_services_keys.name&gt;.[].vlan_aware_bundle_number_base") | Integer |  | 0 |  | Base number for VLAN aware bundle RD/RT.<br>The "Assigned Number" part of RD/RT is derived from vrf_vni + vlan_aware_bundle_number_base.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;pseudowire_rt_base</samp>](## "&lt;network_services_keys.name&gt;.[].pseudowire_rt_base") | Integer |  |  |  | Pseudowire RT base, used to generate route targets for VPWS services.<br>Avoid overlapping route target spaces between different services.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;enable_mlag_ibgp_peering_vrfs</samp>](## "&lt;network_services_keys.name&gt;.[].enable_mlag_ibgp_peering_vrfs") | Boolean |  |  |  | MLAG iBGP peering per VRF.<br>By default an iBGP peering is configured per VRF between MLAG peers on separate VLANs.<br>Setting enable_mlag_ibgp_peering_vrfs: false under tenant will change this default to prevent configuration of these peerings and VLANs for all VRFs in the tenant.<br>This setting can be overridden per VRF.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;bgp_peer_groups</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups") | List, items: Dictionary |  |  |  | List of BGP peer groups definitions.<br>This will configure BGP peer groups to be used inside the tenant VRF for peering with external devices.<br>Since BGP peer groups are configured at higher BGP level, shared between VRFs,<br>peer_group names should not overlap between VRFs.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups.[].name") | String | Required, Unique |  |  | BGP peer group name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups.[].nodes") | List, items: String |  |  |  | Nodes is required to restrict configuration of BGP neighbors to certain nodes in the network.<br>If not set the peer-group is created on devices which have a bgp_peer mapped to the corresponding peer_group.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups.[].nodes.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups.[].type") | String |  |  |  | Key only used for documentation or validation purposes |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remote_as</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups.[].remote_as") | String |  |  |  | BGP AS <1-4294967295> or AS number in asdot notation <1-65535>.<0-65535> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;local_as</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups.[].local_as") | String |  |  |  | BGP AS <1-4294967295> or AS number in asdot notation <1-65535>.<0-65535> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups.[].description") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;shutdown</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups.[].shutdown") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;as_path</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups.[].as_path") | Dictionary |  |  |  | BGP AS-PATH options |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remote_as_replace_out</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups.[].as_path.remote_as_replace_out") | Boolean |  |  |  | Replace AS number with local AS number |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prepend_own_disabled</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups.[].as_path.prepend_own_disabled") | Boolean |  |  |  | Disable prepending own AS number to AS path |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remove_private_as</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups.[].remove_private_as") | Dictionary |  |  |  | Remove private AS numbers in outbound AS path |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups.[].remove_private_as.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;all</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups.[].remove_private_as.all") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;replace_as</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups.[].remove_private_as.replace_as") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remove_private_as_ingress</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups.[].remove_private_as_ingress") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups.[].remove_private_as_ingress.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;replace_as</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups.[].remove_private_as_ingress.replace_as") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer_filter</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups.[].peer_filter") | String |  |  |  | Peer-filter name<br>note: `bgp_listen_range_prefix` and `peer_filter` will be deprecated in AVD v4.0<br>These should not be mixed with the new `listen_ranges` key above to avoid conflicts.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;next_hop_unchanged</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups.[].next_hop_unchanged") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;update_source</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups.[].update_source") | String |  |  |  | IP address or interface name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_reflector_client</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups.[].route_reflector_client") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bfd</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups.[].bfd") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ebgp_multihop</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups.[].ebgp_multihop") | Integer |  |  | Min: 1<br>Max: 255 | Time-to-live in range of hops |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;next_hop_self</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups.[].next_hop_self") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;password</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups.[].password") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;passive</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups.[].passive") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default_originate</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups.[].default_originate") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups.[].default_originate.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;always</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups.[].default_originate.always") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups.[].default_originate.route_map") | String |  |  |  | Route-map name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;send_community</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups.[].send_community") | String |  |  |  | 'all' or a combination of 'standard', 'extended', 'large' and 'link-bandwidth (w/options)' |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maximum_routes</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups.[].maximum_routes") | Integer |  |  | Min: 0<br>Max: 4294967294 | Maximum number of routes (0 means unlimited) |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maximum_routes_warning_limit</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups.[].maximum_routes_warning_limit") | String |  |  |  | Maximum number of routes after which a warning is issued (0 means never warn) or<br>Percentage of maximum number of routes at which to warn ("<1-100> percent")<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maximum_routes_warning_only</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups.[].maximum_routes_warning_only") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;link_bandwidth</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups.[].link_bandwidth") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups.[].link_bandwidth.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups.[].link_bandwidth.default") | String |  |  |  | nn.nn(K|M|G) link speed in bits/second |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;allowas_in</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups.[].allowas_in") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups.[].allowas_in.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;times</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups.[].allowas_in.times") | Integer |  |  | Min: 1<br>Max: 10 | Number of local ASNs allowed in a BGP update |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;weight</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups.[].weight") | Integer |  |  | Min: 0<br>Max: 65535 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;timers</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups.[].timers") | String |  |  |  | BGP Keepalive and Hold Timer values in seconds as string "<0-3600> <0-3600>" |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rib_in_pre_policy_retain</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups.[].rib_in_pre_policy_retain") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups.[].rib_in_pre_policy_retain.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;all</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups.[].rib_in_pre_policy_retain.all") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_in</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups.[].route_map_in") | String |  |  |  | Inbound route-map name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_out</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups.[].route_map_out") | String |  |  |  | Outbound route-map name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp_listen_range_prefix</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups.[].bgp_listen_range_prefix") | String |  |  |  | IP prefix range<br>note: `bgp_listen_range_prefix` and `peer_filter` will be deprecated in AVD v4.0<br>These should not be mixed with the new `listen_ranges` key above to avoid conflicts.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;session_tracker</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups.[].session_tracker") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;evpn_l2_multicast</samp>](## "&lt;network_services_keys.name&gt;.[].evpn_l2_multicast") | Dictionary |  |  |  | Enable EVPN L2 Multicast for all SVIs and l2vlans within Tenant.<br>- Multicast group binding is created only for Multicast traffic. BULL traffic will use ingress-replication<br>- Configures binding between VXLAN, VLAN, and multicast group IPv4 address using the following formula:<br>  < evpn_l2_multicast.underlay_l2_multicast_group_ipv4_pool > + < vlan_id - 1 > + < evpn_l2_multicast.underlay_l2_multicast_group_ipv4_pool_offset >.<br>- The recommendation is to assign a /20 block within the 232.0.0.0/8 Source-Specific Multicast range.<br>- Enables `redistribute igmp` on the router bgp MAC VRF.<br>- When evpn_l2_multicast.enabled is true for a VLAN or a tenant, "igmp snooping" and "igmp snooping querier" will always be enabled - overriding those individual settings.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;network_services_keys.name&gt;.[].evpn_l2_multicast.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;underlay_l2_multicast_group_ipv4_pool</samp>](## "&lt;network_services_keys.name&gt;.[].evpn_l2_multicast.underlay_l2_multicast_group_ipv4_pool") | String |  |  |  | IPv4_address/Mask |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;underlay_l2_multicast_group_ipv4_pool_offset</samp>](## "&lt;network_services_keys.name&gt;.[].evpn_l2_multicast.underlay_l2_multicast_group_ipv4_pool_offset") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;evpn_l3_multicast</samp>](## "&lt;network_services_keys.name&gt;.[].evpn_l3_multicast") | Dictionary |  |  |  | Enable L3 Multicast for all SVIs and l3vlans within Tenant.<br>- In the evpn-l3ls design type, this enables L3 EVPN Multicast (aka OISM)<br>- Multicast group binding for VRF is created only for Multicast traffic. BULL traffic will use ingress-replication<br>- Configures binding between VXLAN, VLAN, and multicast group IPv4 address using the following formula:<br>  < l3_multicast.evpn_underlay_l3_multicast_group_ipv4_pool > + < vrf_vni - 1 > + < l3_multicast.evpn_underlay_l3_multicast_group_ipv4_pool_offset >.<br>- The recommendation is to assign a /20 block within the 232.0.0.0/8 Source-Specific Multicast range.<br>- If enabled on an SVI using the anycast default gateway feature, a diagnostic loopback (see below) MUST be configured to source IGMP traffic.<br>- Enables `evpn multicast` on the router bgp VRF.<br>- When enabled on an SVI:<br>     - If switch is part of an MLAG pair, enables "pim ipv4 sparse-mode" on the SVI.<br>     - If switch is standalone or A-A MH, enables "ip igmp" on the SVI.<br>     - If "ip address virtual" is configured, enables "pim ipv4 local-interface" and uses the diagnostic Loopback defined in the VRF<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;network_services_keys.name&gt;.[].evpn_l3_multicast.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_underlay_l3_multicast_group_ipv4_pool</samp>](## "&lt;network_services_keys.name&gt;.[].evpn_l3_multicast.evpn_underlay_l3_multicast_group_ipv4_pool") | String | Required |  |  | IPv4_address/Mask |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_underlay_l3_multicast_group_ipv4_pool_offset</samp>](## "&lt;network_services_keys.name&gt;.[].evpn_l3_multicast.evpn_underlay_l3_multicast_group_ipv4_pool_offset") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_peg</samp>](## "&lt;network_services_keys.name&gt;.[].evpn_l3_multicast.evpn_peg") | List, items: Dictionary |  |  |  | For each group of nodes, allow configuration of EVPN PEG options.<br>The first group of settings where the device's hostname is present in the 'nodes' list will be used.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- nodes</samp>](## "&lt;network_services_keys.name&gt;.[].evpn_l3_multicast.evpn_peg.[].nodes") | List, items: String |  |  |  | A description will be applied to all nodes with RP addresses configured if not set. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;network_services_keys.name&gt;.[].evpn_l3_multicast.evpn_peg.[].nodes.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;transit</samp>](## "&lt;network_services_keys.name&gt;.[].evpn_l3_multicast.evpn_peg.[].transit") | Boolean |  |  |  | Enable EVPN PEG transit mode. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;pim_rp_addresses</samp>](## "&lt;network_services_keys.name&gt;.[].pim_rp_addresses") | List, items: Dictionary |  |  |  | For each group of nodes, allow configuration of RP Addresses & associated groups.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- rps</samp>](## "&lt;network_services_keys.name&gt;.[].pim_rp_addresses.[].rps") | List, items: String |  |  | Min Length: 1 | List of Rendevouz Points |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;network_services_keys.name&gt;.[].pim_rp_addresses.[].rps.[].&lt;str&gt;") | String |  |  |  | RP address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "&lt;network_services_keys.name&gt;.[].pim_rp_addresses.[].nodes") | List, items: String |  |  |  | Restrict configuration to specific nodes.<br>Configuration Will be applied to all nodes if not set.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;network_services_keys.name&gt;.[].pim_rp_addresses.[].nodes.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;groups</samp>](## "&lt;network_services_keys.name&gt;.[].pim_rp_addresses.[].groups") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;network_services_keys.name&gt;.[].pim_rp_addresses.[].groups.[].&lt;str&gt;") | String |  |  |  | Group_prefix/mask |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;igmp_snooping_querier</samp>](## "&lt;network_services_keys.name&gt;.[].igmp_snooping_querier") | Dictionary |  |  |  | Enable IGMP snooping querier for each SVI/l2vlan within tenant, by default using IP address of Loopback 0.<br>When enabled, IGMP snooping querier will only be configured on L3 devices, i.e., uplink_type: p2p.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;network_services_keys.name&gt;.[].igmp_snooping_querier.enabled") | Boolean |  |  |  | Will be enabled automatically if "evpn_l2_multicast" is enabled. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_address</samp>](## "&lt;network_services_keys.name&gt;.[].igmp_snooping_querier.source_address") | String |  |  | Format: ipv4 | Default IP address of Loopback0 |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;version</samp>](## "&lt;network_services_keys.name&gt;.[].igmp_snooping_querier.version") | Integer |  | 2 | Valid Values:<br>- 1<br>- 2<br>- 3 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;evpn_l2_multi_domain</samp>](## "&lt;network_services_keys.name&gt;.[].evpn_l2_multi_domain") | Boolean |  | True |  | Explicitly extend all VLANs/VLAN-Aware Bundles inside the tenant to remote EVPN domains. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vrfs</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs") | List, items: Dictionary |  |  |  | VRF "default" is supported under network-services. Currently the supported options for "default" vrf are route-target,<br>route-distinguisher settings, structured_config, raw_eos_cli in bgp and SVIs are the only supported interface type.<br>Vlan-aware-bundles are supported as well inside default vrf. OSPF is not supported currently.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].name") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;address_families</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].address_families") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].address_families.[].&lt;str&gt;") | String |  |  | Valid Values:<br>- evpn<br>- vpn-ipv4<br>- vpn-ipv6 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].description") | String |  |  |  | VRF description |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf_vni</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].vrf_vni") | Integer |  |  | Min: 1<br>Max: 16777215 | Required if "vrf_id" is not set.<br>The VRF VNI range is not limited, but if vrf_id is not set, "vrf_vni" is used for calculating MLAG iBGP peering vlan id.<br>See "mlag_ibgp_peering_vrfs.base_vlan" for details.<br>If vrf_vni > 10000 make sure to adjust "mac_vrf_vni_base" accordingly to avoid overlap.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf_id</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].vrf_id") | Integer |  |  | Min: 1<br>Max: 1024 | Required if "vrf_vni" is not set.<br>"vrf_id" is used as default value for "vrf_vni" and "ospf.process_id" unless those are set.<br>"vrf_id" is preferred over "vrf_vni" for VRF RD/RT ID before vrf_vni<br>"vrf_id" is preferred over "vrf_vni" for MLAG iBGP peering vlan, see "mlag_ibgp_peering_vrfs.base_vlan" for details<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_ibgp_peering_ipv4_pool</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].mlag_ibgp_peering_ipv4_pool") | String |  |  |  | IPv4_address/Mask<br>The subnet used for iBGP peering in the VRF.<br>Each MLAG pair will be assigned a subnet based on the ID of the primary MLAG switch<br>If not set, "mlag_peer_l3_ipv4_pool" or "mlag_peer_ipv4_pool" will be used<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_helpers</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].ip_helpers") | List, items: Dictionary |  |  |  | IP helper for DHCP relay |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- ip_helper</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].ip_helpers.[].ip_helper") | String | Required, Unique |  |  | IPv4 DHCP server IP |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_interface</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].ip_helpers.[].source_interface") | String |  |  |  | Interface name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_vrf</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].ip_helpers.[].source_vrf") | String |  |  |  | VRF to originate DHCP relay packets to DHCP server. If not set, uses current VRF |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enable_mlag_ibgp_peering_vrfs</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].enable_mlag_ibgp_peering_vrfs") | Boolean |  |  |  | MLAG iBGP peering per VRF.<br>By default an iBGP peering is configured per VRF between MLAG peers on separate VLANs.<br>Setting enable_mlag_ibgp_peering_vrfs: false under vrf will change this default and/or override the tenant-wide setting<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_ibgp_peering_vlan</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].mlag_ibgp_peering_vlan") | Integer |  |  | Min: 1<br>Max: 4096 | Manually define the VLAN used on the MLAG pair for the iBGP session.<br>By default this parameter is calculated using the following formula: <mlag_ibgp_peering_vrfs.base_vlan> + <vrf_id> - 1<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vtep_diagnostic</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].vtep_diagnostic") | Dictionary |  |  |  | Enable VTEP Network diagnostics.<br>This will create a loopback with virtual source-nat enable to perform diagnostics from the switch<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loopback</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].vtep_diagnostic.loopback") | Integer |  |  | Min: 2<br>Max: 2100 | Loopback interface number, required (when vtep_diagnotics defined)<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loopback_description</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].vtep_diagnostic.loopback_description") | String |  |  |  | Provide a custom description for loopback interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loopback_ip_range</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].vtep_diagnostic.loopback_ip_range") | String |  |  |  | IPv4_address/Mask<br>Loopback ip range, a unique ip is derived from this ranged and assigned<br>to each l3 leaf based on it's unique id, ptional (loopback is not created unless loopback_ip_range or loopback_ip_pools are set)<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loopback_ip_pools</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].vtep_diagnostic.loopback_ip_pools") | List, items: Dictionary |  |  |  | For inventories with multiple PODs a loopback range can be set per POD to avoid overlaps.<br>This only takes effect when loopback_ip_range is not defined, ptional (loopback is not created unless loopback_ip_range or loopback_ip_pools are set)<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- pod</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].vtep_diagnostic.loopback_ip_pools.[].pod") | String |  |  |  | POD name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4_pool</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].vtep_diagnostic.loopback_ip_pools.[].ipv4_pool") | String |  |  |  | IPv4_address/Mask |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ospf</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].ospf") | Dictionary |  |  |  | Router OSPF configuration.<br>This will create an OSPF routing instance in the tenant VRF. If there is no nodes definition, the OSPF instance will be<br>created on all leafs where the VRF is deployed. This will also cause automatic OSPF redistribution into BGP unless<br>explicitly turned off with "redistribute_ospf: false".<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].ospf.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;process_id</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].ospf.process_id") | Integer |  |  |  | If not set, "vrf_id" will be used. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;router_id</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].ospf.router_id") | String |  |  |  | If not set, switch router_id will be used. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;max_lsa</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].ospf.max_lsa") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bfd</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].ospf.bfd") | Boolean |  | False |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;redistribute_bgp</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].ospf.redistribute_bgp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].ospf.redistribute_bgp.enabled") | Boolean |  | True |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].ospf.redistribute_bgp.route_map") | String |  |  |  | Route-map name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;redistribute_connected</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].ospf.redistribute_connected") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].ospf.redistribute_connected.enabled") | Boolean |  | False |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].ospf.redistribute_connected.route_map") | String |  |  |  | Route-map name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].ospf.nodes") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].ospf.nodes.[].&lt;str&gt;") | String |  |  |  | Hostname |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;redistribute_ospf</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].redistribute_ospf") | Boolean |  | True |  | Non-selectively enabling or disabling redistribute ospf inside the VRF. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_l3_multicast</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].evpn_l3_multicast") | Dictionary |  |  |  | Explicitly enable or disable evpn_l3_multicast to override setting of `<network_services_key>.[].evpn_l3_multicast.enabled`.<br>Allow override of `<network_services_key>.[].evpn_l3_multicast` node_settings.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].evpn_l3_multicast.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_peg</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].evpn_l3_multicast.evpn_peg") | List, items: Dictionary |  |  |  | For each group of nodes, allow configuration of EVPN PEG features. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- nodes</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].evpn_l3_multicast.evpn_peg.[].nodes") | List |  |  |  | Restrict configuration to specific nodes.<br>Will apply to all nodes with RP addresses configured if not set.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;transit</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].evpn_l3_multicast.evpn_peg.[].transit") | Boolean |  | False |  | Enable EVPN PEG transit mode. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pim_rp_addresses</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].pim_rp_addresses") | List, items: Dictionary |  |  |  | For each group of nodes, allow configuration of RP Addresses & associated groups.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- rps</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].pim_rp_addresses.[].rps") | List, items: String |  |  |  | A minimum of one RP must be specified. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].pim_rp_addresses.[].rps.[].&lt;str&gt;") | String |  |  |  | RP address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].pim_rp_addresses.[].nodes") | List, items: String |  |  |  | Restrict configuration to specific nodes.<br>Configuration Will be applied to all nodes if not set.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].pim_rp_addresses.[].nodes.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;groups</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].pim_rp_addresses.[].groups") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].pim_rp_addresses.[].groups.[].&lt;str&gt;") | String |  |  |  | Group_prefix/mask |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_l2_multi_domain</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].evpn_l2_multi_domain") | Boolean |  |  |  | Explicitly extend all VLANs/VLAN-Aware Bundles inside the VRF to remote EVPN domains.<br>Overrides `<network_services_key>.[].evpn_l2_multi_domain`.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;svis</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis") | List, items: Dictionary |  |  |  | List of SVIs<br>This will create both the L3 SVI and L2 VLAN based on filters applied to the node..<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- id</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].id") | Integer | Required, Unique |  | Min: 1<br>Max: 4096 | SVI interface id and VLAN id. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].name") | String | Required |  |  | VLAN name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;profile</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].profile") | String |  |  |  | SVI profile name to apply.<br>SVI can refer to one svi_profile which again can refer to another svi_profile to inherit settings in up to two levels (svi -> svi_profile -> svi_parent_profile).<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes") | List, items: Dictionary |  |  |  | Define node specific configuration, such as unique IP addresses. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- node</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].node") | String | Required, Unique |  |  | l3_leaf inventory hostname |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].name") | String |  |  |  | VLAN name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].enabled") | Boolean |  |  |  | Enable or disable interface |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].description") | String |  |  |  | SVI description. By default set to VLAN name.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].ip_address") | String |  |  |  | IPv4_address/Mask. Usually set under "nodes" to have unique IPv4 addresses per node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_address</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].ipv6_address") | String |  |  |  | IPv6_address/Mask. Usually set under "nodes" to have unique IPv6 addresses per node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_enable</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].ipv6_enable") | Boolean |  |  |  | Explicitly enable/disable link-local IPv6 addressing. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_address_virtual</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].ip_address_virtual") | String |  |  |  | IPv4_address/Mask<br>IPv4 VXLAN Anycast IP address<br>Conserves IP addresses in VXLAN deployments as it doesn't require unique IP addresses on each node.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_address_virtual</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].ipv6_address_virtual") | String |  |  |  | IPv6_address/Mask<br>ipv6 address virtuals to configure VXLAN Anycast IP address (Optional)<br>The below "ipv6_address_virtual" key will be deprecated in AVD v4.0 in favor of the new "ipv6_address_virtuals"<br>If both "ipv6_address_virtual" and "ipv6_address_virtuals" are set, all addresses will be configured<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_address_virtuals</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].ipv6_address_virtuals") | List, items: String |  |  |  | IPv6 VXLAN Anycast IP addresses<br>Conserves IPv6 addresses in VXLAN deployments as it doesn't require unique IPv6 addresses on each node.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].ipv6_address_virtuals.[].&lt;str&gt;") | String |  |  |  | IPv6_address/Mask |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_address_virtual_secondaries</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].ip_address_virtual_secondaries") | List, items: String |  |  |  | Secondary IPv4 VXLAN Anycast IP addresses |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].ip_address_virtual_secondaries.[].&lt;str&gt;") | String |  |  |  | IPv4_address/Mask |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_virtual_router_addresses</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].ip_virtual_router_addresses") | List, items: String |  |  |  | IPv4 VARP addresses.<br>Requires an IP address to be configured on the SVI.<br>If ip_address_virtual is also set, ip_virtual_router_addresses will take precedence<br>_if_ there is an ip_address configured for the node.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].ip_virtual_router_addresses.[].&lt;str&gt;") | String |  |  |  | IPv4_address/Mask or IPv4_address<br>IPv4_address/Mask will also configure a static route to the SVI per best practice.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_virtual_router_addresses</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].ipv6_virtual_router_addresses") | List, items: String |  |  |  | IPv6 VARP addresses.<br>Requires an IPv6 address to be configured on the SVI.<br>If ipv6_address_virtuals is also set, ipv6_virtual_router_addresses will take precedence<br>_if_ there is an ipv6_address configured for the node.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].ipv6_virtual_router_addresses.[].&lt;str&gt;") | String |  |  |  | IPv6_address |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_helpers</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].ip_helpers") | List, items: Dictionary |  |  |  | IP helper for DHCP relay |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- ip_helper</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].ip_helpers.[].ip_helper") | String | Required, Unique |  |  | IPv4 DHCP server IP |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_interface</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].ip_helpers.[].source_interface") | String |  |  |  | Interface name to originate DHCP relay packets to DHCP server. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_vrf</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].ip_helpers.[].source_vrf") | String |  |  |  | VRF to originate DHCP relay packets to DHCP server. If not set, EOS uses the VRF on the SVI. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vni_override</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].vni_override") | Integer |  |  | Min: 1<br>Max: 16777215 | By default the VNI will be derived from "mac_vrf_vni_base"<br>The vni_override allows us to override this value and statically define it (optional)<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rt_override</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].rt_override") | Integer |  |  | Min: 1<br>Max: 16777215 | By default the MAC VRF RD/RT ID will be derived from "mac_vrf_id_base"<br>The rt_override allows us to override this value and statically define it (optional)<br>If not set, vni_override will be used.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tags</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].tags") | List, items: String |  | ['all'] |  | Tags leveraged for networks services filtering<br>Tags are matched against "filter.tags" defined under Fabric Topology variables<br>Tags are also matched against the "node_group" name under Fabric Topology variables<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].tags.[].&lt;str&gt;") | String |  |  |  | Tag value |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;trunk_groups</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].trunk_groups") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].trunk_groups.[].&lt;str&gt;") | String |  |  |  | Trunk groups are used for limiting vlans to trunk ports assigned to the same trunk group<br>Requires "enable_trunk_groups: true"<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_l2_multicast</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].evpn_l2_multicast") | Dictionary |  |  |  | Explicitly enable or disable evpn_l2_multicast to override setting of `<network_services_key>.[].evpn_l2_multicast.enabled`.<br>When evpn_l2_multicast.enabled is set to true for a vlan or a tenant, "igmp snooping" and "igmp snooping querier" will always be enabled, overriding those individual settings.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].evpn_l2_multicast.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_l3_multicast</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].evpn_l3_multicast") | Dictionary |  |  |  | Explicitly enable or disable evpn_l3_multicast to override setting of `<network_services_key>.[].evpn_l3_multicast.enabled` and `<network_services_key>.[].vrfs.[].evpn_l3_multicast.enabled`.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].evpn_l3_multicast.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;igmp_snooping_enabled</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].igmp_snooping_enabled") | Boolean |  |  |  | Enable IGMP Snooping (Enabled by default on EOS) |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;igmp_snooping_querier</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].igmp_snooping_querier") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].igmp_snooping_querier.enabled") | Boolean |  |  |  | Will be enabled automatically if evpn_l2_multicast is enabled. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_address</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].igmp_snooping_querier.source_address") | String |  |  |  | IPv4_address<br>If not set, IP address of "Loopback0" will be used.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;version</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].igmp_snooping_querier.version") | Integer |  |  | Valid Values:<br>- 1<br>- 2<br>- 3 | IGMP Version (By default EOS uses IGMP version 2 for IGMP querier) |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vxlan</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].vxlan") | Boolean |  | True |  | Extend this SVI over VXLAN |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mtu</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].mtu") | Integer |  |  |  | Interface MTU |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ospf</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].ospf") | Dictionary |  |  |  | OSPF interface configuration |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].ospf.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;point_to_point</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].ospf.point_to_point") | Boolean |  | True |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;area</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].ospf.area") | String |  | 0 |  | OSPF area ID |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cost</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].ospf.cost") | Integer |  |  |  | OSPF link cost |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;authentication</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].ospf.authentication") | String |  |  | Valid Values:<br>- simple<br>- message-digest |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;simple_auth_key</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].ospf.simple_auth_key") | String |  |  |  | Password used with simple authentication |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;message_digest_keys</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].ospf.message_digest_keys") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- id</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].ospf.message_digest_keys.[].id") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hash_algorithm</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].ospf.message_digest_keys.[].hash_algorithm") | String |  | sha512 | Valid Values:<br>- md5<br>- sha1<br>- sha256<br>- sha384<br>- sha512 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].ospf.message_digest_keys.[].key") | String |  |  |  | Type 7 encrypted key |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].bgp") | Dictionary |  |  |  | Structured configuration and EOS CLI commands rendered on router_bgp.vlans<br>This configuration will not be applied to vlan aware bundles<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].bgp.structured_config") | Dictionary |  |  |  | Custom structured config added under vlan_interfaces.<interface> for eos_cli_config_gen.<br>Overrides the setting on SVI level.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].bgp.raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the VLAN interface in the final EOS configuration<br>Overrides the setting on SVI level.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the VLAN interface in the final EOS configuration<br>Overrides the setting on SVI level<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].structured_config") | Dictionary |  |  |  | Custom structured config added under vlan_interfaces.<interface> for eos_cli_config_gen.<br>Overrides the setting on SVI level. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].enabled") | Boolean |  |  |  | Enable or disable interface |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].description") | String |  |  |  | SVI description. By default set to VLAN name.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].ip_address") | String |  |  |  | IPv4_address/Mask. Usually set under "nodes" to have unique IPv4 addresses per node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_address</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].ipv6_address") | String |  |  |  | IPv6_address/Mask. Usually set under "nodes" to have unique IPv6 addresses per node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_enable</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].ipv6_enable") | Boolean |  |  |  | Explicitly enable/disable link-local IPv6 addressing. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_address_virtual</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].ip_address_virtual") | String |  |  |  | IPv4_address/Mask<br>IPv4 VXLAN Anycast IP address<br>Conserves IP addresses in VXLAN deployments as it doesn't require unique IP addresses on each node.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_address_virtual</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].ipv6_address_virtual") | String |  |  |  | IPv6_address/Mask<br>ipv6 address virtuals to configure VXLAN Anycast IP address (Optional)<br>The below "ipv6_address_virtual" key will be deprecated in AVD v4.0 in favor of the new "ipv6_address_virtuals"<br>If both "ipv6_address_virtual" and "ipv6_address_virtuals" are set, all addresses will be configured<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_address_virtuals</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].ipv6_address_virtuals") | List, items: String |  |  |  | IPv6 VXLAN Anycast IP addresses<br>Conserves IPv6 addresses in VXLAN deployments as it doesn't require unique IPv6 addresses on each node.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].ipv6_address_virtuals.[].&lt;str&gt;") | String |  |  |  | IPv6_address/Mask |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_address_virtual_secondaries</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].ip_address_virtual_secondaries") | List, items: String |  |  |  | Secondary IPv4 VXLAN Anycast IP addresses |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].ip_address_virtual_secondaries.[].&lt;str&gt;") | String |  |  |  | IPv4_address/Mask |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_virtual_router_addresses</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].ip_virtual_router_addresses") | List, items: String |  |  |  | IPv4 VARP addresses.<br>Requires an IP address to be configured on the SVI.<br>If ip_address_virtual is also set, ip_virtual_router_addresses will take precedence<br>_if_ there is an ip_address configured for the node.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].ip_virtual_router_addresses.[].&lt;str&gt;") | String |  |  |  | IPv4_address/Mask or IPv4_address<br>IPv4_address/Mask will also configure a static route to the SVI per best practice.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_virtual_router_addresses</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].ipv6_virtual_router_addresses") | List, items: String |  |  |  | IPv6 VARP addresses.<br>Requires an IPv6 address to be configured on the SVI.<br>If ipv6_address_virtuals is also set, ipv6_virtual_router_addresses will take precedence<br>_if_ there is an ipv6_address configured for the node.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].ipv6_virtual_router_addresses.[].&lt;str&gt;") | String |  |  |  | IPv6_address |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_helpers</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].ip_helpers") | List, items: Dictionary |  |  |  | IP helper for DHCP relay |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- ip_helper</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].ip_helpers.[].ip_helper") | String | Required, Unique |  |  | IPv4 DHCP server IP |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_interface</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].ip_helpers.[].source_interface") | String |  |  |  | Interface name to originate DHCP relay packets to DHCP server. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_vrf</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].ip_helpers.[].source_vrf") | String |  |  |  | VRF to originate DHCP relay packets to DHCP server. If not set, EOS uses the VRF on the SVI. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vni_override</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].vni_override") | Integer |  |  | Min: 1<br>Max: 16777215 | By default the VNI will be derived from "mac_vrf_vni_base"<br>The vni_override allows us to override this value and statically define it (optional)<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rt_override</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].rt_override") | Integer |  |  | Min: 1<br>Max: 16777215 | By default the MAC VRF RD/RT ID will be derived from "mac_vrf_id_base"<br>The rt_override allows us to override this value and statically define it (optional)<br>If not set, vni_override will be used.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tags</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].tags") | List, items: String |  | ['all'] |  | Tags leveraged for networks services filtering<br>Tags are matched against "filter.tags" defined under Fabric Topology variables<br>Tags are also matched against the "node_group" name under Fabric Topology variables<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].tags.[].&lt;str&gt;") | String |  |  |  | Tag value |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;trunk_groups</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].trunk_groups") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].trunk_groups.[].&lt;str&gt;") | String |  |  |  | Trunk groups are used for limiting vlans to trunk ports assigned to the same trunk group<br>Requires "enable_trunk_groups: true"<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_l2_multicast</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].evpn_l2_multicast") | Dictionary |  |  |  | Explicitly enable or disable evpn_l2_multicast to override setting of `<network_services_key>.[].evpn_l2_multicast.enabled`.<br>When evpn_l2_multicast.enabled is set to true for a vlan or a tenant, "igmp snooping" and "igmp snooping querier" will always be enabled, overriding those individual settings.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].evpn_l2_multicast.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_l3_multicast</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].evpn_l3_multicast") | Dictionary |  |  |  | Explicitly enable or disable evpn_l3_multicast to override setting of `<network_services_key>.[].evpn_l3_multicast.enabled` and `<network_services_key>.[].vrfs.[].evpn_l3_multicast.enabled`.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].evpn_l3_multicast.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;igmp_snooping_enabled</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].igmp_snooping_enabled") | Boolean |  |  |  | Enable IGMP Snooping (Enabled by default on EOS) |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;igmp_snooping_querier</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].igmp_snooping_querier") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].igmp_snooping_querier.enabled") | Boolean |  |  |  | Will be enabled automatically if evpn_l2_multicast is enabled. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_address</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].igmp_snooping_querier.source_address") | String |  |  |  | IPv4_address<br>If not set, IP address of "Loopback0" will be used.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;version</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].igmp_snooping_querier.version") | Integer |  |  | Valid Values:<br>- 1<br>- 2<br>- 3 | IGMP Version (By default EOS uses IGMP version 2 for IGMP querier) |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vxlan</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].vxlan") | Boolean |  | True |  | Extend this SVI over VXLAN |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mtu</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].mtu") | Integer |  |  |  | Interface MTU |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ospf</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].ospf") | Dictionary |  |  |  | OSPF interface configuration |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].ospf.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;point_to_point</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].ospf.point_to_point") | Boolean |  | True |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;area</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].ospf.area") | String |  | 0 |  | OSPF area ID |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cost</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].ospf.cost") | Integer |  |  |  | OSPF link cost |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;authentication</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].ospf.authentication") | String |  |  | Valid Values:<br>- simple<br>- message-digest |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;simple_auth_key</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].ospf.simple_auth_key") | String |  |  |  | Password used with simple authentication |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;message_digest_keys</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].ospf.message_digest_keys") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- id</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].ospf.message_digest_keys.[].id") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hash_algorithm</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].ospf.message_digest_keys.[].hash_algorithm") | String |  | sha512 | Valid Values:<br>- md5<br>- sha1<br>- sha256<br>- sha384<br>- sha512 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].ospf.message_digest_keys.[].key") | String |  |  |  | Type 7 encrypted key |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].bgp") | Dictionary |  |  |  | Structured configuration and EOS CLI commands rendered on router_bgp.vlans<br>This configuration will not be applied to vlan aware bundles<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].bgp.structured_config") | Dictionary |  |  |  | Custom structured config added under vlan_interfaces.<interface> for eos_cli_config_gen.<br>Overrides the setting on SVI level.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].bgp.raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the VLAN interface in the final EOS configuration<br>Overrides the setting on SVI level.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the VLAN interface in the final EOS configuration<br>Overrides the setting on SVI level<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].structured_config") | Dictionary |  |  |  | Custom structured config added under vlan_interfaces.<interface> for eos_cli_config_gen.<br>Overrides the setting on SVI level. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;l3_interfaces</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].l3_interfaces") | List, items: Dictionary |  |  |  | List of L3 interfaces.<br>This will create IP routed interface inside VRF. Length of interfaces, nodes and ip_addresses must match.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- interfaces</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].l3_interfaces.[].interfaces") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].l3_interfaces.[].interfaces.[].&lt;str&gt;") | String |  |  |  | Interface name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;encapsulation_dot1q_vlan</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].l3_interfaces.[].encapsulation_dot1q_vlan") | List, items: Integer |  |  |  | For sub-interfaces the dot1q vlan is derived from the interface name by default, but can also be specified. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;int&gt;</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].l3_interfaces.[].encapsulation_dot1q_vlan.[].&lt;int&gt;") | Integer |  |  | Min: 1<br>Max: 4094 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_addresses</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].l3_interfaces.[].ip_addresses") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].l3_interfaces.[].ip_addresses.[].&lt;str&gt;") | String |  |  |  | IPv4_address/Mask |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].l3_interfaces.[].nodes") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].l3_interfaces.[].nodes.[].&lt;str&gt;") | String |  |  |  | Node |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].l3_interfaces.[].description") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;descriptions</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].l3_interfaces.[].descriptions") | List, items: String |  |  |  | "descriptions" has precedence over "description"<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].l3_interfaces.[].descriptions.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].l3_interfaces.[].enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mtu</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].l3_interfaces.[].mtu") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ospf</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].l3_interfaces.[].ospf") | Dictionary |  |  |  | OSPF interface configuration |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].l3_interfaces.[].ospf.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;point_to_point</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].l3_interfaces.[].ospf.point_to_point") | Boolean |  | False |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;area</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].l3_interfaces.[].ospf.area") | Integer |  | 0 |  | OSPF area id |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cost</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].l3_interfaces.[].ospf.cost") | Integer |  |  |  | OSPF link cost |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;authentication</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].l3_interfaces.[].ospf.authentication") | String |  |  | Valid Values:<br>- simple<br>- message-digest |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;simple_auth_key</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].l3_interfaces.[].ospf.simple_auth_key") | String |  |  |  | Password used with simple authentication |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;message_digest_keys</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].l3_interfaces.[].ospf.message_digest_keys") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- id</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].l3_interfaces.[].ospf.message_digest_keys.[].id") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hash_algorithm</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].l3_interfaces.[].ospf.message_digest_keys.[].hash_algorithm") | String |  | sha512 | Valid Values:<br>- md5<br>- sha1<br>- sha256<br>- sha384<br>- sha512 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].l3_interfaces.[].ospf.message_digest_keys.[].key") | String |  |  |  | Key password |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pim</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].l3_interfaces.[].pim") | Dictionary |  |  |  | Enable PIM sparse-mode on the interface; requires "evpn_l3_multicast" to be enabled on the VRF/Tenant<br>Enabling this implicitly makes the device a PIM External Gateway (PEG) in EVPN designs only.<br>At least one RP address must be configured for EVPN PEG to be configured.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].l3_interfaces.[].pim.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].l3_interfaces.[].structured_config") | Dictionary |  |  |  | Custom structured config added under vlan_interfaces.<interface> for eos_cli_config_gen.<br>Overrides the setting on SVI level.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].l3_interfaces.[].raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the VLAN interface in the final EOS configuration<br>Overrides the setting on SVI level.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;static_routes</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].static_routes") | List, items: Dictionary |  |  |  | List of static routes for v4 and/or v6.<br>This will create static routes inside the tenant VRF.<br>If nodes are not specified, all l3leafs that carry the VRF will also be applied the static routes.<br>If a node has a static route in the VRF, redistribute static will be automatically enabled in that VRF.<br>This automatic behavior can be overridden non-selectively with the redistribute_static knob for the VRF.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- destination_address_prefix</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].static_routes.[].destination_address_prefix") | String |  |  |  | IPv4_address |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;gateway</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].static_routes.[].gateway") | String |  |  |  | IPv4_address |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;track_bfd</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].static_routes.[].track_bfd") | Boolean |  |  |  | Track next-hop using BFD |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;distance</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].static_routes.[].distance") | Integer |  |  | Min: 1<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tag</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].static_routes.[].tag") | Integer |  |  | Min: 0<br>Max: 4294967295 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].static_routes.[].name") | String |  |  |  | description |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;metric</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].static_routes.[].metric") | Integer |  |  | Min: 0<br>Max: 4294967295 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interface</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].static_routes.[].interface") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].static_routes.[].nodes") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].static_routes.[].nodes.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_static_routes</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].ipv6_static_routes") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- destination_address_prefix</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].ipv6_static_routes.[].destination_address_prefix") | String |  |  |  | IPv6_address |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;gateway</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].ipv6_static_routes.[].gateway") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;track_bfd</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].ipv6_static_routes.[].track_bfd") | Boolean |  |  |  | Track next-hop using BFD |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;distance</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].ipv6_static_routes.[].distance") | Integer |  |  | Min: 1<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tag</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].ipv6_static_routes.[].tag") | Integer |  |  | Min: 0<br>Max: 4294967295 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].ipv6_static_routes.[].name") | String |  |  |  | description |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;metric</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].ipv6_static_routes.[].metric") | Integer |  |  | Min: 0<br>Max: 4294967295 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interface</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].ipv6_static_routes.[].interface") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].ipv6_static_routes.[].nodes") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].ipv6_static_routes.[].nodes.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;redistribute_static</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].redistribute_static") | Boolean |  |  |  | Non-selectively enabling or disabling redistribute static inside the VRF. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp_peers</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peers") | List, items: Dictionary |  |  |  | List of BGP peer definitions.<br>This will configure BGP neighbors inside the tenant VRF for peering with external devices.<br>The configured peer will automatically be activated for ipv4 or ipv6 address family based on the ip address.<br>Note, only ipv4 and ipv6 address families are currently supported in eos_designs.<br>For other address families, use custom_structured configuration with eos_cli_config_gen.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- ip_address</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peers.[].ip_address") | String | Required, Unique |  |  | IPv4_address or IPv6_address |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer_group</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peers.[].peer_group") | String |  |  |  | Peer group name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remote_as</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peers.[].remote_as") | Integer |  |  |  | Remote ASN |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peers.[].description") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;password</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peers.[].password") | String |  |  |  | Encrypted password |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;send_community</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peers.[].send_community") | String |  |  |  | 'all' or a combination of 'standard', 'extended', 'large' and 'link-bandwidth (w/options)'<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;next_hop_self</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peers.[].next_hop_self") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;timers</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peers.[].timers") | String |  |  |  | BGP Keepalive and Hold Timer values in seconds as string <0-3600> <0-3600> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maximum_routes</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peers.[].maximum_routes") | Integer |  |  | Min: 0<br>Max: 4294967294 | Maximum number of routes (0 means unlimited) |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default_originate</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peers.[].default_originate") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;always</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peers.[].default_originate.always") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;update_source</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peers.[].update_source") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ebgp_multihop</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peers.[].ebgp_multihop") | Integer |  |  | Min: 1<br>Max: 255 | Time-to-live in range of hops |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peers.[].nodes") | List, items: String |  |  |  | Nodes is required to restrict configuration of BGP neighbors to certain nodes in the network. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peers.[].nodes.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;set_ipv4_next_hop</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peers.[].set_ipv4_next_hop") | String |  |  |  | IPv4_address<br>Next hop settings can be either ipv4 or ipv6 for one neighbor, this will be applied by a uniquely generated route-map per neighbor.<br>Next hop takes precedence over route_map_out.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;set_ipv6_next_hop</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peers.[].set_ipv6_next_hop") | String |  |  |  | IPv6_address<br>Next hop settings can be either ipv4 or ipv6 for one neighbor, this will be applied by a uniquely generated route-map per neighbor.<br>Next hop takes precedence over route_map_out.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_out</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peers.[].route_map_out") | String |  |  |  | Route-map name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_in</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peers.[].route_map_in") | String |  |  |  | Route-map name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefix_list_in</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peers.[].prefix_list_in") | String |  |  |  | Prefix list name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefix_list_out</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peers.[].prefix_list_out") | String |  |  |  | Prefix list name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;local_as</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peers.[].local_as") | String |  |  |  | Local BGP ASN<br>eg. "65001.1200"<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;weight</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peers.[].weight") | Integer |  |  | Min: 0<br>Max: 65535 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bfd</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peers.[].bfd") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp.raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the VLAN interface in the final EOS configuration<br>Overrides the setting on SVI level.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp.structured_config") | Dictionary |  |  |  | Custom structured config added under vlan_interfaces.<interface> for eos_cli_config_gen.<br>Overrides the setting on SVI level.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp_peer_groups</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups") | List, items: Dictionary |  |  |  | List of BGP peer groups definitions.<br>This will configure BGP peer groups to be used inside the tenant VRF for peering with external devices.<br>Since BGP peer groups are configured at higher BGP level, shared between VRFs,<br>peer_group names should not overlap between VRFs.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups.[].name") | String |  |  |  | BGP peer group name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups.[].nodes") | List, items: String |  |  |  | Nodes is required to restrict configuration of BGP neighbors to certain nodes in the network.<br>If not set the peer-group is created on devices which have a bgp_peer mapped to the corresponding peer_group.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups.[].nodes.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups.[].type") | String |  |  |  | Key only used for documentation or validation purposes |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remote_as</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups.[].remote_as") | String |  |  |  | BGP AS <1-4294967295> or AS number in asdot notation <1-65535>.<0-65535> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;local_as</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups.[].local_as") | String |  |  |  | BGP AS <1-4294967295> or AS number in asdot notation <1-65535>.<0-65535> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups.[].description") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;shutdown</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups.[].shutdown") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;as_path</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups.[].as_path") | Dictionary |  |  |  | BGP AS-PATH options |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remote_as_replace_out</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups.[].as_path.remote_as_replace_out") | Boolean |  |  |  | Replace AS number with local AS number |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prepend_own_disabled</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups.[].as_path.prepend_own_disabled") | Boolean |  |  |  | Disable prepending own AS number to AS path |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remove_private_as</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups.[].remove_private_as") | Dictionary |  |  |  | Remove private AS numbers in outbound AS path |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups.[].remove_private_as.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;all</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups.[].remove_private_as.all") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;replace_as</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups.[].remove_private_as.replace_as") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remove_private_as_ingress</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups.[].remove_private_as_ingress") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups.[].remove_private_as_ingress.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;replace_as</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups.[].remove_private_as_ingress.replace_as") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer_filter</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups.[].peer_filter") | String |  |  |  | Peer-filter name<br>note: `bgp_listen_range_prefix` and `peer_filter` will be deprecated in AVD v4.0<br>These should not be mixed with the new `listen_ranges` key above to avoid conflicts.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;next_hop_unchanged</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups.[].next_hop_unchanged") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;update_source</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups.[].update_source") | String |  |  |  | IP address or interface name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_reflector_client</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups.[].route_reflector_client") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bfd</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups.[].bfd") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ebgp_multihop</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups.[].ebgp_multihop") | Integer |  |  | Min: 1<br>Max: 255 | Time-to-live in range of hops |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;next_hop_self</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups.[].next_hop_self") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;password</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups.[].password") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;passive</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups.[].passive") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default_originate</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups.[].default_originate") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups.[].default_originate.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;always</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups.[].default_originate.always") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups.[].default_originate.route_map") | String |  |  |  | Route-map name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;send_community</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups.[].send_community") | String |  |  |  | 'all' or a combination of 'standard', 'extended', 'large' and 'link-bandwidth (w/options)' |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maximum_routes</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups.[].maximum_routes") | Integer |  |  | Min: 0<br>Max: 4294967294 | Maximum number of routes (0 means unlimited) |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maximum_routes_warning_limit</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups.[].maximum_routes_warning_limit") | String |  |  |  | Maximum number of routes after which a warning is issued (0 means never warn) or<br>Percentage of maximum number of routes at which to warn ("<1-100> percent")<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maximum_routes_warning_only</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups.[].maximum_routes_warning_only") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;link_bandwidth</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups.[].link_bandwidth") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups.[].link_bandwidth.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups.[].link_bandwidth.default") | String |  |  |  | nn.nn(K|M|G) link speed in bits/second |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;allowas_in</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups.[].allowas_in") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups.[].allowas_in.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;times</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups.[].allowas_in.times") | Integer |  |  | Min: 1<br>Max: 10 | Number of local ASNs allowed in a BGP update |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;weight</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups.[].weight") | Integer |  |  | Min: 0<br>Max: 65535 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;timers</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups.[].timers") | String |  |  |  | BGP Keepalive and Hold Timer values in seconds as string "<0-3600> <0-3600>" |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rib_in_pre_policy_retain</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups.[].rib_in_pre_policy_retain") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups.[].rib_in_pre_policy_retain.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;all</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups.[].rib_in_pre_policy_retain.all") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_in</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups.[].route_map_in") | String |  |  |  | Inbound route-map name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_out</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups.[].route_map_out") | String |  |  |  | Outbound route-map name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp_listen_range_prefix</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups.[].bgp_listen_range_prefix") | String |  |  |  | IP prefix range<br>note: `bgp_listen_range_prefix` and `peer_filter` will be deprecated in AVD v4.0<br>These should not be mixed with the new `listen_ranges` key above to avoid conflicts.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;session_tracker</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups.[].session_tracker") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;additional_route_targets</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].additional_route_targets") | List, items: Dictionary |  |  |  | Configuration of extra route-targets for this VRF. Useful for route-leaking or gateway between address families. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- type</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].additional_route_targets.[].type") | String |  |  | Valid Values:<br>- import<br>- export |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;address_family</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].additional_route_targets.[].address_family") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_target</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].additional_route_targets.[].route_target") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].additional_route_targets.[].nodes") | List, items: String |  |  |  | Nodes is required to restrict configuration of BGP neighbors to certain nodes in the network.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].additional_route_targets.[].nodes.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the VLAN interface in the final EOS configuration<br>Overrides the setting on SVI level.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].structured_config") | Dictionary |  |  |  | Custom structured config added under vlan_interfaces.<interface> for eos_cli_config_gen.<br>Overrides the setting on SVI level.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;l2vlans</samp>](## "&lt;network_services_keys.name&gt;.[].l2vlans") | List, items: Dictionary |  |  |  | Define L2 network services organized by vlan id. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- id</samp>](## "&lt;network_services_keys.name&gt;.[].l2vlans.[].id") | Integer | Required, Unique |  | Min: 1<br>Max: 4094 | VLAN ID |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vni_override</samp>](## "&lt;network_services_keys.name&gt;.[].l2vlans.[].vni_override") | Integer |  |  | Min: 1<br>Max: 16777215 | By default the VNI will be derived from mac_vrf_vni_base<br>The vni_override, allows to override this value and statically define it.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rt_override</samp>](## "&lt;network_services_keys.name&gt;.[].l2vlans.[].rt_override") | Integer |  |  | Min: 1<br>Max: 16777215 | By default the MAC VRF RD/RT ID will be derived from mac_vrf_id_base<br>The rt_override allows us to override this value and statically define it.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "&lt;network_services_keys.name&gt;.[].l2vlans.[].name") | String | Required |  |  | VLAN name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tags</samp>](## "&lt;network_services_keys.name&gt;.[].l2vlans.[].tags") | List, items: String |  |  |  | Tags leveraged for networks services filtering<br>Tags are matched against filter.tags defined under Fabric Topology variables<br>Tags are also matched against the node_group name under Fabric Topology variables<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;network_services_keys.name&gt;.[].l2vlans.[].tags.[].&lt;str&gt;") | String |  | all |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vxlan</samp>](## "&lt;network_services_keys.name&gt;.[].l2vlans.[].vxlan") | Boolean |  | True |  | Extend this L2VLAN over VXLAN |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;trunk_groups</samp>](## "&lt;network_services_keys.name&gt;.[].l2vlans.[].trunk_groups") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;network_services_keys.name&gt;.[].l2vlans.[].trunk_groups.[].&lt;str&gt;") | String |  |  |  | Trunk groups are used for limiting vlans to trunk ports assigned to the same trunk group<br>Requires enable_trunk_groups: true<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_l2_multicast</samp>](## "&lt;network_services_keys.name&gt;.[].l2vlans.[].evpn_l2_multicast") | Dictionary |  |  |  | Explicitly enable or disable evpn_l2_multicast to override setting of `<network_services_key>.[].evpn_l2_multicast.enabled`.<br>When evpn_l2_multicast.enabled is set to true for a vlan or a tenant, igmp snooping and igmp snooping querier will always be enabled, overriding those individual settings.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;network_services_keys.name&gt;.[].l2vlans.[].evpn_l2_multicast.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;igmp_snooping_enabled</samp>](## "&lt;network_services_keys.name&gt;.[].l2vlans.[].igmp_snooping_enabled") | Boolean |  | True |  | Activate or deactivate IGMP snooping |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;igmp_snooping_querier</samp>](## "&lt;network_services_keys.name&gt;.[].l2vlans.[].igmp_snooping_querier") | Dictionary |  |  |  | Enable igmp snooping querier, by default using IP address of Loopback 0.<br>When enabled, igmp snooping querier will only be configured on l3 devices, i.e., uplink_type: p2p.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;network_services_keys.name&gt;.[].l2vlans.[].igmp_snooping_querier.enabled") | Boolean |  |  |  | Will be enabled automatically if evpn_l2_multicast is enabled. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_address</samp>](## "&lt;network_services_keys.name&gt;.[].l2vlans.[].igmp_snooping_querier.source_address") | String |  |  |  | IPv4_address<br>If not set, IP address of "Loopback0" will be used.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;version</samp>](## "&lt;network_services_keys.name&gt;.[].l2vlans.[].igmp_snooping_querier.version") | Integer |  | 2 | Valid Values:<br>- 1<br>- 2<br>- 3 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp</samp>](## "&lt;network_services_keys.name&gt;.[].l2vlans.[].bgp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "&lt;network_services_keys.name&gt;.[].l2vlans.[].bgp.structured_config") | Dictionary |  |  |  | Structured configuration for eos_cli_config_gen rendered on router_bgp.vlans.<br>This configuration will not be applied to vlan aware bundles.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "&lt;network_services_keys.name&gt;.[].l2vlans.[].bgp.raw_eos_cli") | String |  |  |  | EOS cli commands rendered on router_bgp.vlans.<br>This configuration will not be applied to vlan aware bundles.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;point_to_point_services</samp>](## "&lt;network_services_keys.name&gt;.[].point_to_point_services") | List, items: Dictionary |  |  |  | Point to point services (pseudowires).<br>Only supported for node types with "network_services.l1: true".<br>By default this is only set for node type "pe" with "design.type: mpls"<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "&lt;network_services_keys.name&gt;.[].point_to_point_services.[].name") | String | Required, Unique |  |  | Pseudowire name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "&lt;network_services_keys.name&gt;.[].point_to_point_services.[].type") | String |  | vpws-pseudowire | Valid Values:<br>- vpws-pseudowire |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;subinterfaces</samp>](## "&lt;network_services_keys.name&gt;.[].point_to_point_services.[].subinterfaces") | List, items: Dictionary |  |  |  | Subinterfaces will create subinterfaces and additional pseudowires/patch panel config for each endpoint. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- number</samp>](## "&lt;network_services_keys.name&gt;.[].point_to_point_services.[].subinterfaces.[].number") | Integer | Required, Unique |  |  | Subinterface number |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;endpoints</samp>](## "&lt;network_services_keys.name&gt;.[].point_to_point_services.[].endpoints") | List, items: Dictionary |  |  | Min Length: 2<br>Max Length: 2 | Pseudowire terminating endpoints. Must have exactly two items. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- id</samp>](## "&lt;network_services_keys.name&gt;.[].point_to_point_services.[].endpoints.[].id") | Integer | Required |  |  | Pseudowire ID on this endpoint |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "&lt;network_services_keys.name&gt;.[].point_to_point_services.[].endpoints.[].nodes") | List, items: String | Required |  | Min Length: 1 | Usually one node. With ESI multihoming we support two nodes per pseudowire endpoint<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;network_services_keys.name&gt;.[].point_to_point_services.[].endpoints.[].nodes.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interfaces</samp>](## "&lt;network_services_keys.name&gt;.[].point_to_point_services.[].endpoints.[].interfaces") | List, items: String | Required |  | Min Length: 1 | Interfaces patched to the pseudowire on this endpoints.<br>The list of interfaces is mapped to the list of nodes, so they must have the same length.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;network_services_keys.name&gt;.[].point_to_point_services.[].endpoints.[].interfaces.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;port_channel</samp>](## "&lt;network_services_keys.name&gt;.[].point_to_point_services.[].endpoints.[].port_channel") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "&lt;network_services_keys.name&gt;.[].point_to_point_services.[].endpoints.[].port_channel.mode") | String |  |  | Valid Values:<br>- active<br>- on |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;short_esi</samp>](## "&lt;network_services_keys.name&gt;.[].point_to_point_services.[].endpoints.[].port_channel.short_esi") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;lldp_disable</samp>](## "&lt;network_services_keys.name&gt;.[].point_to_point_services.[].lldp_disable") | Boolean |  |  |  | Disable LLDP RX/TX on port mode pseudowire services |

=== "YAML"

    ```yaml
    <network_services_keys.name>:
      - name: <str>
        mac_vrf_vni_base: <int>
        mac_vrf_id_base: <int>
        vlan_aware_bundle_number_base: <int>
        pseudowire_rt_base: <int>
        enable_mlag_ibgp_peering_vrfs: <bool>
        bgp_peer_groups:
          - name: <str>
            nodes:
              - <str>
            type: <str>
            remote_as: <str>
            local_as: <str>
            description: <str>
            shutdown: <bool>
            as_path:
              remote_as_replace_out: <bool>
              prepend_own_disabled: <bool>
            remove_private_as:
              enabled: <bool>
              all: <bool>
              replace_as: <bool>
            remove_private_as_ingress:
              enabled: <bool>
              replace_as: <bool>
            peer_filter: <str>
            next_hop_unchanged: <bool>
            update_source: <str>
            route_reflector_client: <bool>
            bfd: <bool>
            ebgp_multihop: <int>
            next_hop_self: <bool>
            password: <str>
            passive: <bool>
            default_originate:
              enabled: <bool>
              always: <bool>
              route_map: <str>
            send_community: <str>
            maximum_routes: <int>
            maximum_routes_warning_limit: <str>
            maximum_routes_warning_only: <bool>
            link_bandwidth:
              enabled: <bool>
              default: <str>
            allowas_in:
              enabled: <bool>
              times: <int>
            weight: <int>
            timers: <str>
            rib_in_pre_policy_retain:
              enabled: <bool>
              all: <bool>
            route_map_in: <str>
            route_map_out: <str>
            bgp_listen_range_prefix: <str>
            session_tracker: <str>
        evpn_l2_multicast:
          enabled: <bool>
          underlay_l2_multicast_group_ipv4_pool: <str>
          underlay_l2_multicast_group_ipv4_pool_offset: <int>
        evpn_l3_multicast:
          enabled: <bool>
          evpn_underlay_l3_multicast_group_ipv4_pool: <str>
          evpn_underlay_l3_multicast_group_ipv4_pool_offset: <int>
          evpn_peg:
            - nodes:
                - <str>
              transit: <bool>
        pim_rp_addresses:
          - rps:
              - <str>
            nodes:
              - <str>
            groups:
              - <str>
        igmp_snooping_querier:
          enabled: <bool>
          source_address: <str>
          version: <int>
        evpn_l2_multi_domain: <bool>
        vrfs:
          - name: <str>
            address_families:
              - <str>
            description: <str>
            vrf_vni: <int>
            vrf_id: <int>
            mlag_ibgp_peering_ipv4_pool: <str>
            ip_helpers:
              - ip_helper: <str>
                source_interface: <str>
                source_vrf: <str>
            enable_mlag_ibgp_peering_vrfs: <bool>
            mlag_ibgp_peering_vlan: <int>
            vtep_diagnostic:
              loopback: <int>
              loopback_description: <str>
              loopback_ip_range: <str>
              loopback_ip_pools:
                - pod: <str>
                  ipv4_pool: <str>
            ospf:
              enabled: <bool>
              process_id: <int>
              router_id: <str>
              max_lsa: <int>
              bfd: <bool>
              redistribute_bgp:
                enabled: <bool>
                route_map: <str>
              redistribute_connected:
                enabled: <bool>
                route_map: <str>
              nodes:
                - <str>
            redistribute_ospf: <bool>
            evpn_l3_multicast:
              enabled: <bool>
              evpn_peg:
                - nodes:
                  transit: <bool>
            pim_rp_addresses:
              - rps:
                  - <str>
                nodes:
                  - <str>
                groups:
                  - <str>
            evpn_l2_multi_domain: <bool>
            svis:
              - id: <int>
                name: <str>
                profile: <str>
                nodes:
                  - node: <str>
                    name: <str>
                    enabled: <bool>
                    description: <str>
                    ip_address: <str>
                    ipv6_address: <str>
                    ipv6_enable: <bool>
                    ip_address_virtual: <str>
                    ipv6_address_virtual: <str>
                    ipv6_address_virtuals:
                      - <str>
                    ip_address_virtual_secondaries:
                      - <str>
                    ip_virtual_router_addresses:
                      - <str>
                    ipv6_virtual_router_addresses:
                      - <str>
                    ip_helpers:
                      - ip_helper: <str>
                        source_interface: <str>
                        source_vrf: <str>
                    vni_override: <int>
                    rt_override: <int>
                    tags:
                      - <str>
                    trunk_groups:
                      - <str>
                    evpn_l2_multicast:
                      enabled: <bool>
                    evpn_l3_multicast:
                      enabled: <bool>
                    igmp_snooping_enabled: <bool>
                    igmp_snooping_querier:
                      enabled: <bool>
                      source_address: <str>
                      version: <int>
                    vxlan: <bool>
                    mtu: <int>
                    ospf:
                      enabled: <bool>
                      point_to_point: <bool>
                      area: <str>
                      cost: <int>
                      authentication: <str>
                      simple_auth_key: <str>
                      message_digest_keys:
                        - id: <int>
                          hash_algorithm: <str>
                          key: <str>
                    bgp:
                      structured_config:
                      raw_eos_cli: <str>
                    raw_eos_cli: <str>
                    structured_config:
                enabled: <bool>
                description: <str>
                ip_address: <str>
                ipv6_address: <str>
                ipv6_enable: <bool>
                ip_address_virtual: <str>
                ipv6_address_virtual: <str>
                ipv6_address_virtuals:
                  - <str>
                ip_address_virtual_secondaries:
                  - <str>
                ip_virtual_router_addresses:
                  - <str>
                ipv6_virtual_router_addresses:
                  - <str>
                ip_helpers:
                  - ip_helper: <str>
                    source_interface: <str>
                    source_vrf: <str>
                vni_override: <int>
                rt_override: <int>
                tags:
                  - <str>
                trunk_groups:
                  - <str>
                evpn_l2_multicast:
                  enabled: <bool>
                evpn_l3_multicast:
                  enabled: <bool>
                igmp_snooping_enabled: <bool>
                igmp_snooping_querier:
                  enabled: <bool>
                  source_address: <str>
                  version: <int>
                vxlan: <bool>
                mtu: <int>
                ospf:
                  enabled: <bool>
                  point_to_point: <bool>
                  area: <str>
                  cost: <int>
                  authentication: <str>
                  simple_auth_key: <str>
                  message_digest_keys:
                    - id: <int>
                      hash_algorithm: <str>
                      key: <str>
                bgp:
                  structured_config:
                  raw_eos_cli: <str>
                raw_eos_cli: <str>
                structured_config:
            l3_interfaces:
              - interfaces:
                  - <str>
                encapsulation_dot1q_vlan:
                  - <int>
                ip_addresses:
                  - <str>
                nodes:
                  - <str>
                description: <str>
                descriptions:
                  - <str>
                enabled: <bool>
                mtu: <int>
                ospf:
                  enabled: <bool>
                  point_to_point: <bool>
                  area: <int>
                  cost: <int>
                  authentication: <str>
                  simple_auth_key: <str>
                  message_digest_keys:
                    - id: <int>
                      hash_algorithm: <str>
                      key: <str>
                pim:
                  enabled: <bool>
                structured_config:
                raw_eos_cli: <str>
            static_routes:
              - destination_address_prefix: <str>
                gateway: <str>
                track_bfd: <bool>
                distance: <int>
                tag: <int>
                name: <str>
                metric: <int>
                interface: <str>
                nodes:
                  - <str>
            ipv6_static_routes:
              - destination_address_prefix: <str>
                gateway: <str>
                track_bfd: <bool>
                distance: <int>
                tag: <int>
                name: <str>
                metric: <int>
                interface: <str>
                nodes:
                  - <str>
            redistribute_static: <bool>
            bgp_peers:
              - ip_address: <str>
                peer_group: <str>
                remote_as: <int>
                description: <str>
                password: <str>
                send_community: <str>
                next_hop_self: <bool>
                timers: <str>
                maximum_routes: <int>
                default_originate:
                  always: <bool>
                update_source: <str>
                ebgp_multihop: <int>
                nodes:
                  - <str>
                set_ipv4_next_hop: <str>
                set_ipv6_next_hop: <str>
                route_map_out: <str>
                route_map_in: <str>
                prefix_list_in: <str>
                prefix_list_out: <str>
                local_as: <str>
                weight: <int>
                bfd: <bool>
            bgp:
              raw_eos_cli: <str>
              structured_config:
            bgp_peer_groups:
              - name: <str>
                nodes:
                  - <str>
                type: <str>
                remote_as: <str>
                local_as: <str>
                description: <str>
                shutdown: <bool>
                as_path:
                  remote_as_replace_out: <bool>
                  prepend_own_disabled: <bool>
                remove_private_as:
                  enabled: <bool>
                  all: <bool>
                  replace_as: <bool>
                remove_private_as_ingress:
                  enabled: <bool>
                  replace_as: <bool>
                peer_filter: <str>
                next_hop_unchanged: <bool>
                update_source: <str>
                route_reflector_client: <bool>
                bfd: <bool>
                ebgp_multihop: <int>
                next_hop_self: <bool>
                password: <str>
                passive: <bool>
                default_originate:
                  enabled: <bool>
                  always: <bool>
                  route_map: <str>
                send_community: <str>
                maximum_routes: <int>
                maximum_routes_warning_limit: <str>
                maximum_routes_warning_only: <bool>
                link_bandwidth:
                  enabled: <bool>
                  default: <str>
                allowas_in:
                  enabled: <bool>
                  times: <int>
                weight: <int>
                timers: <str>
                rib_in_pre_policy_retain:
                  enabled: <bool>
                  all: <bool>
                route_map_in: <str>
                route_map_out: <str>
                bgp_listen_range_prefix: <str>
                session_tracker: <str>
            additional_route_targets:
              - type: <str>
                address_family: <str>
                route_target: <str>
                nodes:
                  - <str>
            raw_eos_cli: <str>
            structured_config:
        l2vlans:
          - id: <int>
            vni_override: <int>
            rt_override: <int>
            name: <str>
            tags:
              - <str>
            vxlan: <bool>
            trunk_groups:
              - <str>
            evpn_l2_multicast:
              enabled: <bool>
            igmp_snooping_enabled: <bool>
            igmp_snooping_querier:
              enabled: <bool>
              source_address: <str>
              version: <int>
            bgp:
              structured_config:
              raw_eos_cli: <str>
        point_to_point_services:
          - name: <str>
            type: <str>
            subinterfaces:
              - number: <int>
            endpoints:
              - id: <int>
                nodes:
                  - <str>
                interfaces:
                  - <str>
                port_channel:
                  mode: <str>
                  short_esi: <str>
            lldp_disable: <bool>
    ```

## Global Network Services Settings

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>evpn_rd_type</samp>](## "evpn_rd_type") <span style="color:red">removed</span> | Dictionary |  |  |  | <span style="color:red">This key was removed. Support was removed in AVD version 4.0.0. Use <samp>overlay_rd_type</samp> instead.</span> |
    | [<samp>evpn_rt_type</samp>](## "evpn_rt_type") <span style="color:red">removed</span> | Dictionary |  |  |  | <span style="color:red">This key was removed. Support was removed in AVD version 4.0.0. Use <samp>overlay_rt_type</samp> instead.</span> |
    | [<samp>overlay_rd_type</samp>](## "overlay_rd_type") | Dictionary |  |  |  | Specify RD type.<br>Route Distinguisher (RD) for L2 / L3 services is set to <overlay_loopback>:<vni> per default.<br>By configuring overlay_rd_type the Administrator subfield (first part of RD) can be set to other values.<br>Note:<br>RD is a 48-bit value which is split into <16-bit>:<32-bit> or <32-bit>:<16-bit>.<br>For loopback or 32-bit ASN/number the VNI can only be a 16-bit number.<br>For 16-bit ASN/number the VNI can be a 32-bit number.<br> |
    | [<samp>&nbsp;&nbsp;admin_subfield</samp>](## "overlay_rd_type.admin_subfield") | String |  | overlay_loopback_ip |  | "vtep_loopback" or "bgp_as" or <IPv4 Address> or interger between <0-65535> or integer between <0-4294967295> or "overlay_loopback_ip".<br> |
    | [<samp>&nbsp;&nbsp;admin_subfield_offset</samp>](## "overlay_rd_type.admin_subfield_offset") | String |  |  |  | Offset can only be used if admin_subfield is an interger between <0-4294967295> or "switch_id".<br>Total value of admin_subfield + admin_subfield_offset must be <= 4294967295. |
    | [<samp>overlay_rt_type</samp>](## "overlay_rt_type") | Dictionary |  |  |  | Specify RT type.<br>Route Target (RT) for L2 / L3 services is set to <vni>:<vni> per default.<br>By configuring overlay_rt_type the Administrator subfield (first part of RT) can be set to other values.<br>Notes:<br>RT is a 48-bit value which is split into <16-bit>:<32-bit> or <32-bit>:<16-bit>.<br>For 32-bit ASN/number the VNI can only be a 16-bit number.<br>For 16-bit ASN/number the VNI can be a 32-bit number.<br> |
    | [<samp>&nbsp;&nbsp;admin_subfield</samp>](## "overlay_rt_type.admin_subfield") | String |  | mac_vrf_id |  | "bgp_as" or interger between <0-65535> or integer between <0-4294967295>.<br> |

=== "YAML"

    ```yaml
    evpn_rd_type:
    evpn_rt_type:
    overlay_rd_type:
      admin_subfield: <str>
      admin_subfield_offset: <str>
    overlay_rt_type:
      admin_subfield: <str>
    ```

## Network Services Keys

Define network services keys, to define grouping of network services.
This provides the ability to define various keys of your choice to better organize/group your data.
This should be defined in top level group_var for the fabric.

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>network_services_keys</samp>](## "network_services_keys") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;- name</samp>](## "network_services_keys.[].name") | String | Required, Unique |  |  |  |

=== "YAML"

    ```yaml
    network_services_keys:
      - name: <str>
    ```

## Svi Profiles

Profiles to share common settings for SVIs under `<network_services_key>.[].vrfs.svis`.
Keys are the same used under SVIs. Keys defined under SVIs take precedence.
Note: structured configuration is not merged recursively and will be taken directly from the most specific level in the following order:
1. svi.nodes[inventory_hostname].structured_config
2. svi_profile.nodes[inventory_hostname].structured_config
3. svi_parent_profile.nodes[inventory_hostname].structured_config
4. svi.structured_config
5. svi_profile.structured_config
6. svi_parent_profile.structured_config

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>svi_profiles</samp>](## "svi_profiles") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;- profile</samp>](## "svi_profiles.[].profile") | String | Required, Unique |  |  | Profile name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;parent_profile</samp>](## "svi_profiles.[].parent_profile") | String |  |  |  | Parent SVI profile name to apply.<br>svi_profiles can refer to another svi_profile to inherit settings in up to two levels (svi -> svi_profile -> svi_parent_profile). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "svi_profiles.[].nodes") | List, items: Dictionary |  |  |  | Define node specific configuration, such as unique IP addresses. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- node</samp>](## "svi_profiles.[].nodes.[].node") | String | Required, Unique |  |  | l3_leaf inventory hostname |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "svi_profiles.[].nodes.[].name") | String |  |  |  | VLAN name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "svi_profiles.[].nodes.[].enabled") | Boolean |  |  |  | Enable or disable interface |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "svi_profiles.[].nodes.[].description") | String |  |  |  | SVI description. By default set to VLAN name.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "svi_profiles.[].nodes.[].ip_address") | String |  |  |  | IPv4_address/Mask. Usually set under "nodes" to have unique IPv4 addresses per node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_address</samp>](## "svi_profiles.[].nodes.[].ipv6_address") | String |  |  |  | IPv6_address/Mask. Usually set under "nodes" to have unique IPv6 addresses per node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_enable</samp>](## "svi_profiles.[].nodes.[].ipv6_enable") | Boolean |  |  |  | Explicitly enable/disable link-local IPv6 addressing. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_address_virtual</samp>](## "svi_profiles.[].nodes.[].ip_address_virtual") | String |  |  |  | IPv4_address/Mask<br>IPv4 VXLAN Anycast IP address<br>Conserves IP addresses in VXLAN deployments as it doesn't require unique IP addresses on each node.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_address_virtual</samp>](## "svi_profiles.[].nodes.[].ipv6_address_virtual") | String |  |  |  | IPv6_address/Mask<br>ipv6 address virtuals to configure VXLAN Anycast IP address (Optional)<br>The below "ipv6_address_virtual" key will be deprecated in AVD v4.0 in favor of the new "ipv6_address_virtuals"<br>If both "ipv6_address_virtual" and "ipv6_address_virtuals" are set, all addresses will be configured<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_address_virtuals</samp>](## "svi_profiles.[].nodes.[].ipv6_address_virtuals") | List, items: String |  |  |  | IPv6 VXLAN Anycast IP addresses<br>Conserves IPv6 addresses in VXLAN deployments as it doesn't require unique IPv6 addresses on each node.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "svi_profiles.[].nodes.[].ipv6_address_virtuals.[].&lt;str&gt;") | String |  |  |  | IPv6_address/Mask |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_address_virtual_secondaries</samp>](## "svi_profiles.[].nodes.[].ip_address_virtual_secondaries") | List, items: String |  |  |  | Secondary IPv4 VXLAN Anycast IP addresses |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "svi_profiles.[].nodes.[].ip_address_virtual_secondaries.[].&lt;str&gt;") | String |  |  |  | IPv4_address/Mask |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_virtual_router_addresses</samp>](## "svi_profiles.[].nodes.[].ip_virtual_router_addresses") | List, items: String |  |  |  | IPv4 VARP addresses.<br>Requires an IP address to be configured on the SVI.<br>If ip_address_virtual is also set, ip_virtual_router_addresses will take precedence<br>_if_ there is an ip_address configured for the node.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "svi_profiles.[].nodes.[].ip_virtual_router_addresses.[].&lt;str&gt;") | String |  |  |  | IPv4_address/Mask or IPv4_address<br>IPv4_address/Mask will also configure a static route to the SVI per best practice.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_virtual_router_addresses</samp>](## "svi_profiles.[].nodes.[].ipv6_virtual_router_addresses") | List, items: String |  |  |  | IPv6 VARP addresses.<br>Requires an IPv6 address to be configured on the SVI.<br>If ipv6_address_virtuals is also set, ipv6_virtual_router_addresses will take precedence<br>_if_ there is an ipv6_address configured for the node.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "svi_profiles.[].nodes.[].ipv6_virtual_router_addresses.[].&lt;str&gt;") | String |  |  |  | IPv6_address |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_helpers</samp>](## "svi_profiles.[].nodes.[].ip_helpers") | List, items: Dictionary |  |  |  | IP helper for DHCP relay |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- ip_helper</samp>](## "svi_profiles.[].nodes.[].ip_helpers.[].ip_helper") | String | Required, Unique |  |  | IPv4 DHCP server IP |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_interface</samp>](## "svi_profiles.[].nodes.[].ip_helpers.[].source_interface") | String |  |  |  | Interface name to originate DHCP relay packets to DHCP server. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_vrf</samp>](## "svi_profiles.[].nodes.[].ip_helpers.[].source_vrf") | String |  |  |  | VRF to originate DHCP relay packets to DHCP server. If not set, EOS uses the VRF on the SVI. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vni_override</samp>](## "svi_profiles.[].nodes.[].vni_override") | Integer |  |  | Min: 1<br>Max: 16777215 | By default the VNI will be derived from "mac_vrf_vni_base"<br>The vni_override allows us to override this value and statically define it (optional)<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rt_override</samp>](## "svi_profiles.[].nodes.[].rt_override") | Integer |  |  | Min: 1<br>Max: 16777215 | By default the MAC VRF RD/RT ID will be derived from "mac_vrf_id_base"<br>The rt_override allows us to override this value and statically define it (optional)<br>If not set, vni_override will be used.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tags</samp>](## "svi_profiles.[].nodes.[].tags") | List, items: String |  | ['all'] |  | Tags leveraged for networks services filtering<br>Tags are matched against "filter.tags" defined under Fabric Topology variables<br>Tags are also matched against the "node_group" name under Fabric Topology variables<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "svi_profiles.[].nodes.[].tags.[].&lt;str&gt;") | String |  |  |  | Tag value |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;trunk_groups</samp>](## "svi_profiles.[].nodes.[].trunk_groups") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "svi_profiles.[].nodes.[].trunk_groups.[].&lt;str&gt;") | String |  |  |  | Trunk groups are used for limiting vlans to trunk ports assigned to the same trunk group<br>Requires "enable_trunk_groups: true"<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_l2_multicast</samp>](## "svi_profiles.[].nodes.[].evpn_l2_multicast") | Dictionary |  |  |  | Explicitly enable or disable evpn_l2_multicast to override setting of `<network_services_key>.[].evpn_l2_multicast.enabled`.<br>When evpn_l2_multicast.enabled is set to true for a vlan or a tenant, "igmp snooping" and "igmp snooping querier" will always be enabled, overriding those individual settings.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "svi_profiles.[].nodes.[].evpn_l2_multicast.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_l3_multicast</samp>](## "svi_profiles.[].nodes.[].evpn_l3_multicast") | Dictionary |  |  |  | Explicitly enable or disable evpn_l3_multicast to override setting of `<network_services_key>.[].evpn_l3_multicast.enabled` and `<network_services_key>.[].vrfs.[].evpn_l3_multicast.enabled`.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "svi_profiles.[].nodes.[].evpn_l3_multicast.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;igmp_snooping_enabled</samp>](## "svi_profiles.[].nodes.[].igmp_snooping_enabled") | Boolean |  |  |  | Enable IGMP Snooping (Enabled by default on EOS) |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;igmp_snooping_querier</samp>](## "svi_profiles.[].nodes.[].igmp_snooping_querier") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "svi_profiles.[].nodes.[].igmp_snooping_querier.enabled") | Boolean |  |  |  | Will be enabled automatically if evpn_l2_multicast is enabled. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_address</samp>](## "svi_profiles.[].nodes.[].igmp_snooping_querier.source_address") | String |  |  |  | IPv4_address<br>If not set, IP address of "Loopback0" will be used.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;version</samp>](## "svi_profiles.[].nodes.[].igmp_snooping_querier.version") | Integer |  |  | Valid Values:<br>- 1<br>- 2<br>- 3 | IGMP Version (By default EOS uses IGMP version 2 for IGMP querier) |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vxlan</samp>](## "svi_profiles.[].nodes.[].vxlan") | Boolean |  | True |  | Extend this SVI over VXLAN |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mtu</samp>](## "svi_profiles.[].nodes.[].mtu") | Integer |  |  |  | Interface MTU |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ospf</samp>](## "svi_profiles.[].nodes.[].ospf") | Dictionary |  |  |  | OSPF interface configuration |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "svi_profiles.[].nodes.[].ospf.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;point_to_point</samp>](## "svi_profiles.[].nodes.[].ospf.point_to_point") | Boolean |  | True |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;area</samp>](## "svi_profiles.[].nodes.[].ospf.area") | String |  | 0 |  | OSPF area ID |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cost</samp>](## "svi_profiles.[].nodes.[].ospf.cost") | Integer |  |  |  | OSPF link cost |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;authentication</samp>](## "svi_profiles.[].nodes.[].ospf.authentication") | String |  |  | Valid Values:<br>- simple<br>- message-digest |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;simple_auth_key</samp>](## "svi_profiles.[].nodes.[].ospf.simple_auth_key") | String |  |  |  | Password used with simple authentication |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;message_digest_keys</samp>](## "svi_profiles.[].nodes.[].ospf.message_digest_keys") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- id</samp>](## "svi_profiles.[].nodes.[].ospf.message_digest_keys.[].id") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hash_algorithm</samp>](## "svi_profiles.[].nodes.[].ospf.message_digest_keys.[].hash_algorithm") | String |  | sha512 | Valid Values:<br>- md5<br>- sha1<br>- sha256<br>- sha384<br>- sha512 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key</samp>](## "svi_profiles.[].nodes.[].ospf.message_digest_keys.[].key") | String |  |  |  | Type 7 encrypted key |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp</samp>](## "svi_profiles.[].nodes.[].bgp") | Dictionary |  |  |  | Structured configuration and EOS CLI commands rendered on router_bgp.vlans<br>This configuration will not be applied to vlan aware bundles<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "svi_profiles.[].nodes.[].bgp.structured_config") | Dictionary |  |  |  | Custom structured config added under vlan_interfaces.<interface> for eos_cli_config_gen.<br>Overrides the setting on SVI level.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "svi_profiles.[].nodes.[].bgp.raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the VLAN interface in the final EOS configuration<br>Overrides the setting on SVI level.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "svi_profiles.[].nodes.[].raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the VLAN interface in the final EOS configuration<br>Overrides the setting on SVI level<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "svi_profiles.[].nodes.[].structured_config") | Dictionary |  |  |  | Custom structured config added under vlan_interfaces.<interface> for eos_cli_config_gen.<br>Overrides the setting on SVI level. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "svi_profiles.[].name") | String |  |  |  | VLAN name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "svi_profiles.[].enabled") | Boolean |  |  |  | Enable or disable interface |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "svi_profiles.[].description") | String |  |  |  | SVI description. By default set to VLAN name.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "svi_profiles.[].ip_address") | String |  |  |  | IPv4_address/Mask. Usually set under "nodes" to have unique IPv4 addresses per node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_address</samp>](## "svi_profiles.[].ipv6_address") | String |  |  |  | IPv6_address/Mask. Usually set under "nodes" to have unique IPv6 addresses per node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_enable</samp>](## "svi_profiles.[].ipv6_enable") | Boolean |  |  |  | Explicitly enable/disable link-local IPv6 addressing. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_address_virtual</samp>](## "svi_profiles.[].ip_address_virtual") | String |  |  |  | IPv4_address/Mask<br>IPv4 VXLAN Anycast IP address<br>Conserves IP addresses in VXLAN deployments as it doesn't require unique IP addresses on each node.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_address_virtual</samp>](## "svi_profiles.[].ipv6_address_virtual") | String |  |  |  | IPv6_address/Mask<br>ipv6 address virtuals to configure VXLAN Anycast IP address (Optional)<br>The below "ipv6_address_virtual" key will be deprecated in AVD v4.0 in favor of the new "ipv6_address_virtuals"<br>If both "ipv6_address_virtual" and "ipv6_address_virtuals" are set, all addresses will be configured<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_address_virtuals</samp>](## "svi_profiles.[].ipv6_address_virtuals") | List, items: String |  |  |  | IPv6 VXLAN Anycast IP addresses<br>Conserves IPv6 addresses in VXLAN deployments as it doesn't require unique IPv6 addresses on each node.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "svi_profiles.[].ipv6_address_virtuals.[].&lt;str&gt;") | String |  |  |  | IPv6_address/Mask |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_address_virtual_secondaries</samp>](## "svi_profiles.[].ip_address_virtual_secondaries") | List, items: String |  |  |  | Secondary IPv4 VXLAN Anycast IP addresses |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "svi_profiles.[].ip_address_virtual_secondaries.[].&lt;str&gt;") | String |  |  |  | IPv4_address/Mask |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_virtual_router_addresses</samp>](## "svi_profiles.[].ip_virtual_router_addresses") | List, items: String |  |  |  | IPv4 VARP addresses.<br>Requires an IP address to be configured on the SVI.<br>If ip_address_virtual is also set, ip_virtual_router_addresses will take precedence<br>_if_ there is an ip_address configured for the node.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "svi_profiles.[].ip_virtual_router_addresses.[].&lt;str&gt;") | String |  |  |  | IPv4_address/Mask or IPv4_address<br>IPv4_address/Mask will also configure a static route to the SVI per best practice.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_virtual_router_addresses</samp>](## "svi_profiles.[].ipv6_virtual_router_addresses") | List, items: String |  |  |  | IPv6 VARP addresses.<br>Requires an IPv6 address to be configured on the SVI.<br>If ipv6_address_virtuals is also set, ipv6_virtual_router_addresses will take precedence<br>_if_ there is an ipv6_address configured for the node.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "svi_profiles.[].ipv6_virtual_router_addresses.[].&lt;str&gt;") | String |  |  |  | IPv6_address |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_helpers</samp>](## "svi_profiles.[].ip_helpers") | List, items: Dictionary |  |  |  | IP helper for DHCP relay |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- ip_helper</samp>](## "svi_profiles.[].ip_helpers.[].ip_helper") | String | Required, Unique |  |  | IPv4 DHCP server IP |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_interface</samp>](## "svi_profiles.[].ip_helpers.[].source_interface") | String |  |  |  | Interface name to originate DHCP relay packets to DHCP server. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_vrf</samp>](## "svi_profiles.[].ip_helpers.[].source_vrf") | String |  |  |  | VRF to originate DHCP relay packets to DHCP server. If not set, EOS uses the VRF on the SVI. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vni_override</samp>](## "svi_profiles.[].vni_override") | Integer |  |  | Min: 1<br>Max: 16777215 | By default the VNI will be derived from "mac_vrf_vni_base"<br>The vni_override allows us to override this value and statically define it (optional)<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;rt_override</samp>](## "svi_profiles.[].rt_override") | Integer |  |  | Min: 1<br>Max: 16777215 | By default the MAC VRF RD/RT ID will be derived from "mac_vrf_id_base"<br>The rt_override allows us to override this value and statically define it (optional)<br>If not set, vni_override will be used.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;tags</samp>](## "svi_profiles.[].tags") | List, items: String |  | ['all'] |  | Tags leveraged for networks services filtering<br>Tags are matched against "filter.tags" defined under Fabric Topology variables<br>Tags are also matched against the "node_group" name under Fabric Topology variables<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "svi_profiles.[].tags.[].&lt;str&gt;") | String |  |  |  | Tag value |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;trunk_groups</samp>](## "svi_profiles.[].trunk_groups") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "svi_profiles.[].trunk_groups.[].&lt;str&gt;") | String |  |  |  | Trunk groups are used for limiting vlans to trunk ports assigned to the same trunk group<br>Requires "enable_trunk_groups: true"<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;evpn_l2_multicast</samp>](## "svi_profiles.[].evpn_l2_multicast") | Dictionary |  |  |  | Explicitly enable or disable evpn_l2_multicast to override setting of `<network_services_key>.[].evpn_l2_multicast.enabled`.<br>When evpn_l2_multicast.enabled is set to true for a vlan or a tenant, "igmp snooping" and "igmp snooping querier" will always be enabled, overriding those individual settings.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "svi_profiles.[].evpn_l2_multicast.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;evpn_l3_multicast</samp>](## "svi_profiles.[].evpn_l3_multicast") | Dictionary |  |  |  | Explicitly enable or disable evpn_l3_multicast to override setting of `<network_services_key>.[].evpn_l3_multicast.enabled` and `<network_services_key>.[].vrfs.[].evpn_l3_multicast.enabled`.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "svi_profiles.[].evpn_l3_multicast.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;igmp_snooping_enabled</samp>](## "svi_profiles.[].igmp_snooping_enabled") | Boolean |  |  |  | Enable IGMP Snooping (Enabled by default on EOS) |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;igmp_snooping_querier</samp>](## "svi_profiles.[].igmp_snooping_querier") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "svi_profiles.[].igmp_snooping_querier.enabled") | Boolean |  |  |  | Will be enabled automatically if evpn_l2_multicast is enabled. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_address</samp>](## "svi_profiles.[].igmp_snooping_querier.source_address") | String |  |  |  | IPv4_address<br>If not set, IP address of "Loopback0" will be used.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;version</samp>](## "svi_profiles.[].igmp_snooping_querier.version") | Integer |  |  | Valid Values:<br>- 1<br>- 2<br>- 3 | IGMP Version (By default EOS uses IGMP version 2 for IGMP querier) |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vxlan</samp>](## "svi_profiles.[].vxlan") | Boolean |  | True |  | Extend this SVI over VXLAN |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mtu</samp>](## "svi_profiles.[].mtu") | Integer |  |  |  | Interface MTU |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ospf</samp>](## "svi_profiles.[].ospf") | Dictionary |  |  |  | OSPF interface configuration |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "svi_profiles.[].ospf.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;point_to_point</samp>](## "svi_profiles.[].ospf.point_to_point") | Boolean |  | True |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;area</samp>](## "svi_profiles.[].ospf.area") | String |  | 0 |  | OSPF area ID |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cost</samp>](## "svi_profiles.[].ospf.cost") | Integer |  |  |  | OSPF link cost |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;authentication</samp>](## "svi_profiles.[].ospf.authentication") | String |  |  | Valid Values:<br>- simple<br>- message-digest |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;simple_auth_key</samp>](## "svi_profiles.[].ospf.simple_auth_key") | String |  |  |  | Password used with simple authentication |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;message_digest_keys</samp>](## "svi_profiles.[].ospf.message_digest_keys") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- id</samp>](## "svi_profiles.[].ospf.message_digest_keys.[].id") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hash_algorithm</samp>](## "svi_profiles.[].ospf.message_digest_keys.[].hash_algorithm") | String |  | sha512 | Valid Values:<br>- md5<br>- sha1<br>- sha256<br>- sha384<br>- sha512 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key</samp>](## "svi_profiles.[].ospf.message_digest_keys.[].key") | String |  |  |  | Type 7 encrypted key |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;bgp</samp>](## "svi_profiles.[].bgp") | Dictionary |  |  |  | Structured configuration and EOS CLI commands rendered on router_bgp.vlans<br>This configuration will not be applied to vlan aware bundles<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "svi_profiles.[].bgp.structured_config") | Dictionary |  |  |  | Custom structured config added under vlan_interfaces.<interface> for eos_cli_config_gen.<br>Overrides the setting on SVI level.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "svi_profiles.[].bgp.raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the VLAN interface in the final EOS configuration<br>Overrides the setting on SVI level.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "svi_profiles.[].raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the VLAN interface in the final EOS configuration<br>Overrides the setting on SVI level<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "svi_profiles.[].structured_config") | Dictionary |  |  |  | Custom structured config added under vlan_interfaces.<interface> for eos_cli_config_gen.<br>Overrides the setting on SVI level. |

=== "YAML"

    ```yaml
    svi_profiles:
      - profile: <str>
        parent_profile: <str>
        nodes:
          - node: <str>
            name: <str>
            enabled: <bool>
            description: <str>
            ip_address: <str>
            ipv6_address: <str>
            ipv6_enable: <bool>
            ip_address_virtual: <str>
            ipv6_address_virtual: <str>
            ipv6_address_virtuals:
              - <str>
            ip_address_virtual_secondaries:
              - <str>
            ip_virtual_router_addresses:
              - <str>
            ipv6_virtual_router_addresses:
              - <str>
            ip_helpers:
              - ip_helper: <str>
                source_interface: <str>
                source_vrf: <str>
            vni_override: <int>
            rt_override: <int>
            tags:
              - <str>
            trunk_groups:
              - <str>
            evpn_l2_multicast:
              enabled: <bool>
            evpn_l3_multicast:
              enabled: <bool>
            igmp_snooping_enabled: <bool>
            igmp_snooping_querier:
              enabled: <bool>
              source_address: <str>
              version: <int>
            vxlan: <bool>
            mtu: <int>
            ospf:
              enabled: <bool>
              point_to_point: <bool>
              area: <str>
              cost: <int>
              authentication: <str>
              simple_auth_key: <str>
              message_digest_keys:
                - id: <int>
                  hash_algorithm: <str>
                  key: <str>
            bgp:
              structured_config:
              raw_eos_cli: <str>
            raw_eos_cli: <str>
            structured_config:
        name: <str>
        enabled: <bool>
        description: <str>
        ip_address: <str>
        ipv6_address: <str>
        ipv6_enable: <bool>
        ip_address_virtual: <str>
        ipv6_address_virtual: <str>
        ipv6_address_virtuals:
          - <str>
        ip_address_virtual_secondaries:
          - <str>
        ip_virtual_router_addresses:
          - <str>
        ipv6_virtual_router_addresses:
          - <str>
        ip_helpers:
          - ip_helper: <str>
            source_interface: <str>
            source_vrf: <str>
        vni_override: <int>
        rt_override: <int>
        tags:
          - <str>
        trunk_groups:
          - <str>
        evpn_l2_multicast:
          enabled: <bool>
        evpn_l3_multicast:
          enabled: <bool>
        igmp_snooping_enabled: <bool>
        igmp_snooping_querier:
          enabled: <bool>
          source_address: <str>
          version: <int>
        vxlan: <bool>
        mtu: <int>
        ospf:
          enabled: <bool>
          point_to_point: <bool>
          area: <str>
          cost: <int>
          authentication: <str>
          simple_auth_key: <str>
          message_digest_keys:
            - id: <int>
              hash_algorithm: <str>
              key: <str>
        bgp:
          structured_config:
          raw_eos_cli: <str>
        raw_eos_cli: <str>
        structured_config:
    ```
