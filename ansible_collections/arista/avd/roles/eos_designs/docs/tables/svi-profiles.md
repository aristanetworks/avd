=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>svi_profiles</samp>](## "svi_profiles") | List, items: Dictionary |  |  |  | Profiles to share common settings for SVIs under `<network_services_key>.[].vrfs.svis`.<br>Keys are the same used under SVIs. Keys defined under SVIs take precedence.<br>Note: structured configuration is not merged recursively and will be taken directly from the most specific level in the following order:<br>1. svi.nodes[inventory_hostname].structured_config<br>2. svi_profile.nodes[inventory_hostname].structured_config<br>3. svi_parent_profile.nodes[inventory_hostname].structured_config<br>4. svi.structured_config<br>5. svi_profile.structured_config<br>6. svi_parent_profile.structured_config<br> |
    | [<samp>&nbsp;&nbsp;- profile</samp>](## "svi_profiles.[].profile") | String | Required, Unique |  |  | Profile name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;parent_profile</samp>](## "svi_profiles.[].parent_profile") | String |  |  |  | Parent SVI profile name to apply.<br>svi_profiles can refer to another svi_profile to inherit settings in up to two levels (svi -> svi_profile -> svi_parent_profile). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "svi_profiles.[].nodes") | List, items: Dictionary |  |  |  | Define node specific configuration, such as unique IP addresses.<br>Any keys set here will be merged onto the SVI config, except `structured_config` keys which will replace the `structured_config` set on SVI level.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- node</samp>](## "svi_profiles.[].nodes.[].node") | String | Required, Unique |  |  | l3_leaf inventory hostname |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "svi_profiles.[].nodes.[].name") | String |  |  |  | VLAN name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "svi_profiles.[].nodes.[].enabled") | Boolean |  |  |  | Enable or disable interface |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "svi_profiles.[].nodes.[].description") | String |  |  |  | SVI description. By default set to VLAN name.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "svi_profiles.[].nodes.[].ip_address") | String |  |  |  | IPv4_address/Mask. Usually set under "nodes" to have unique IPv4 addresses per node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_address</samp>](## "svi_profiles.[].nodes.[].ipv6_address") | String |  |  |  | IPv6_address/Mask. Usually set under "nodes" to have unique IPv6 addresses per node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_enable</samp>](## "svi_profiles.[].nodes.[].ipv6_enable") | Boolean |  |  |  | Explicitly enable/disable link-local IPv6 addressing. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_address_virtual</samp>](## "svi_profiles.[].nodes.[].ip_address_virtual") | String |  |  |  | IPv4_address/Mask<br>IPv4 VXLAN Anycast IP address<br>Conserves IP addresses in VXLAN deployments as it doesn't require unique IP addresses on each node.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_address_virtual</samp>](## "svi_profiles.[].nodes.[].ipv6_address_virtual") <span style="color:red">deprecated</span> | String |  |  |  | IPv6_address/Mask<br>ipv6 address virtuals to configure VXLAN Anycast IP address (Optional)<br>If both "ipv6_address_virtual" and "ipv6_address_virtuals" are set, all addresses will be configured<br><span style="color:red">This key is deprecated. Support will be removed in AVD version 5.0.0. Use <samp>ipv6_address_virtuals</samp> instead.</span> |
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
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vni_override</samp>](## "svi_profiles.[].nodes.[].vni_override") | Integer |  |  | Min: 1<br>Max: 16777215 | By default the VNI will be derived from "mac_vrf_vni_base".<br>The vni_override allows us to override this value and statically define it (optional).<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rt_override</samp>](## "svi_profiles.[].nodes.[].rt_override") | Integer |  |  | Min: 1<br>Max: 16777215 | By default the MAC VRF RD/RT ID will be derived from "mac_vrf_id_base".<br>The rt_override allows us to override this value and statically define it (optional).<br>If not set, vni_override will be used.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tags</samp>](## "svi_profiles.[].nodes.[].tags") | List, items: String |  | See (+) on YAML tab |  | Tags leveraged for networks services filtering.<br>Tags are matched against "filter.tags" defined under node type settings.<br>Tags are also matched against the "node_group" name under node type settings.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "svi_profiles.[].nodes.[].tags.[].&lt;str&gt;") | String |  |  |  | Tag value. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;trunk_groups</samp>](## "svi_profiles.[].nodes.[].trunk_groups") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "svi_profiles.[].nodes.[].trunk_groups.[].&lt;str&gt;") | String |  |  |  | Trunk groups are used for limiting vlans to trunk ports assigned to the same trunk group.<br>Requires "enable_trunk_groups: true".<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_l2_multicast</samp>](## "svi_profiles.[].nodes.[].evpn_l2_multicast") | Dictionary |  |  |  | Explicitly enable or disable evpn_l2_multicast to override setting of `<network_services_key>.[].evpn_l2_multicast.enabled`.<br>When evpn_l2_multicast.enabled is set to true for a vlan or a tenant, "igmp snooping" and "igmp snooping querier" will always be enabled, overriding those individual settings.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "svi_profiles.[].nodes.[].evpn_l2_multicast.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_l3_multicast</samp>](## "svi_profiles.[].nodes.[].evpn_l3_multicast") | Dictionary |  |  |  | Explicitly enable or disable evpn_l3_multicast to override setting of `<network_services_key>.[].evpn_l3_multicast.enabled` and `<network_services_key>.[].vrfs.[].evpn_l3_multicast.enabled`.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "svi_profiles.[].nodes.[].evpn_l3_multicast.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;igmp_snooping_enabled</samp>](## "svi_profiles.[].nodes.[].igmp_snooping_enabled") | Boolean |  |  |  | Enable IGMP Snooping (Enabled by default on EOS). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;igmp_snooping_querier</samp>](## "svi_profiles.[].nodes.[].igmp_snooping_querier") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "svi_profiles.[].nodes.[].igmp_snooping_querier.enabled") | Boolean |  |  |  | Will be enabled automatically if evpn_l2_multicast is enabled. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_address</samp>](## "svi_profiles.[].nodes.[].igmp_snooping_querier.source_address") | String |  |  |  | IPv4_address<br>If not set, IP address of "Loopback0" will be used.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;version</samp>](## "svi_profiles.[].nodes.[].igmp_snooping_querier.version") | Integer |  |  | Valid Values:<br>- 1<br>- 2<br>- 3 | IGMP Version (By default EOS uses IGMP version 2 for IGMP querier). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vxlan</samp>](## "svi_profiles.[].nodes.[].vxlan") | Boolean |  | `True` |  | Extend this SVI over VXLAN. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mtu</samp>](## "svi_profiles.[].nodes.[].mtu") | Integer |  |  |  | Interface MTU. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ospf</samp>](## "svi_profiles.[].nodes.[].ospf") | Dictionary |  |  |  | OSPF interface configuration. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "svi_profiles.[].nodes.[].ospf.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;point_to_point</samp>](## "svi_profiles.[].nodes.[].ospf.point_to_point") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;area</samp>](## "svi_profiles.[].nodes.[].ospf.area") | String |  | `0` |  | OSPF area ID. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cost</samp>](## "svi_profiles.[].nodes.[].ospf.cost") | Integer |  |  |  | OSPF link cost. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;authentication</samp>](## "svi_profiles.[].nodes.[].ospf.authentication") | String |  |  | Valid Values:<br>- simple<br>- message-digest |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;simple_auth_key</samp>](## "svi_profiles.[].nodes.[].ospf.simple_auth_key") | String |  |  |  | Password used with simple authentication. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;message_digest_keys</samp>](## "svi_profiles.[].nodes.[].ospf.message_digest_keys") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- id</samp>](## "svi_profiles.[].nodes.[].ospf.message_digest_keys.[].id") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hash_algorithm</samp>](## "svi_profiles.[].nodes.[].ospf.message_digest_keys.[].hash_algorithm") | String |  | `sha512` | Valid Values:<br>- md5<br>- sha1<br>- sha256<br>- sha384<br>- sha512 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key</samp>](## "svi_profiles.[].nodes.[].ospf.message_digest_keys.[].key") | String |  |  |  | Type 7 encrypted key. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp</samp>](## "svi_profiles.[].nodes.[].bgp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "svi_profiles.[].nodes.[].bgp.structured_config") | Dictionary |  |  |  | Structured configuration and EOS CLI commands rendered on router_bgp.vlans.<br>This configuration will not be applied to vlan aware bundles<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "svi_profiles.[].nodes.[].bgp.raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the Router BGP, VLAN definition in the final EOS configuration.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "svi_profiles.[].nodes.[].raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the VLAN interface in the final EOS configuration.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "svi_profiles.[].nodes.[].structured_config") | Dictionary |  |  |  | Custom structured config added under vlan_interfaces.<interface> for eos_cli_config_gen. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "svi_profiles.[].name") | String |  |  |  | VLAN name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "svi_profiles.[].enabled") | Boolean |  |  |  | Enable or disable interface |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "svi_profiles.[].description") | String |  |  |  | SVI description. By default set to VLAN name.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "svi_profiles.[].ip_address") | String |  |  |  | IPv4_address/Mask. Usually set under "nodes" to have unique IPv4 addresses per node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_address</samp>](## "svi_profiles.[].ipv6_address") | String |  |  |  | IPv6_address/Mask. Usually set under "nodes" to have unique IPv6 addresses per node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_enable</samp>](## "svi_profiles.[].ipv6_enable") | Boolean |  |  |  | Explicitly enable/disable link-local IPv6 addressing. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_address_virtual</samp>](## "svi_profiles.[].ip_address_virtual") | String |  |  |  | IPv4_address/Mask<br>IPv4 VXLAN Anycast IP address<br>Conserves IP addresses in VXLAN deployments as it doesn't require unique IP addresses on each node.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_address_virtual</samp>](## "svi_profiles.[].ipv6_address_virtual") <span style="color:red">deprecated</span> | String |  |  |  | IPv6_address/Mask<br>ipv6 address virtuals to configure VXLAN Anycast IP address (Optional)<br>If both "ipv6_address_virtual" and "ipv6_address_virtuals" are set, all addresses will be configured<br><span style="color:red">This key is deprecated. Support will be removed in AVD version 5.0.0. Use <samp>ipv6_address_virtuals</samp> instead.</span> |
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
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vni_override</samp>](## "svi_profiles.[].vni_override") | Integer |  |  | Min: 1<br>Max: 16777215 | By default the VNI will be derived from "mac_vrf_vni_base".<br>The vni_override allows us to override this value and statically define it (optional).<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;rt_override</samp>](## "svi_profiles.[].rt_override") | Integer |  |  | Min: 1<br>Max: 16777215 | By default the MAC VRF RD/RT ID will be derived from "mac_vrf_id_base".<br>The rt_override allows us to override this value and statically define it (optional).<br>If not set, vni_override will be used.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;tags</samp>](## "svi_profiles.[].tags") | List, items: String |  | See (+) on YAML tab |  | Tags leveraged for networks services filtering.<br>Tags are matched against "filter.tags" defined under node type settings.<br>Tags are also matched against the "node_group" name under node type settings.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "svi_profiles.[].tags.[].&lt;str&gt;") | String |  |  |  | Tag value. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;trunk_groups</samp>](## "svi_profiles.[].trunk_groups") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "svi_profiles.[].trunk_groups.[].&lt;str&gt;") | String |  |  |  | Trunk groups are used for limiting vlans to trunk ports assigned to the same trunk group.<br>Requires "enable_trunk_groups: true".<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;evpn_l2_multicast</samp>](## "svi_profiles.[].evpn_l2_multicast") | Dictionary |  |  |  | Explicitly enable or disable evpn_l2_multicast to override setting of `<network_services_key>.[].evpn_l2_multicast.enabled`.<br>When evpn_l2_multicast.enabled is set to true for a vlan or a tenant, "igmp snooping" and "igmp snooping querier" will always be enabled, overriding those individual settings.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "svi_profiles.[].evpn_l2_multicast.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;evpn_l3_multicast</samp>](## "svi_profiles.[].evpn_l3_multicast") | Dictionary |  |  |  | Explicitly enable or disable evpn_l3_multicast to override setting of `<network_services_key>.[].evpn_l3_multicast.enabled` and `<network_services_key>.[].vrfs.[].evpn_l3_multicast.enabled`.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "svi_profiles.[].evpn_l3_multicast.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;igmp_snooping_enabled</samp>](## "svi_profiles.[].igmp_snooping_enabled") | Boolean |  |  |  | Enable IGMP Snooping (Enabled by default on EOS). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;igmp_snooping_querier</samp>](## "svi_profiles.[].igmp_snooping_querier") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "svi_profiles.[].igmp_snooping_querier.enabled") | Boolean |  |  |  | Will be enabled automatically if evpn_l2_multicast is enabled. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_address</samp>](## "svi_profiles.[].igmp_snooping_querier.source_address") | String |  |  |  | IPv4_address<br>If not set, IP address of "Loopback0" will be used.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;version</samp>](## "svi_profiles.[].igmp_snooping_querier.version") | Integer |  |  | Valid Values:<br>- 1<br>- 2<br>- 3 | IGMP Version (By default EOS uses IGMP version 2 for IGMP querier). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vxlan</samp>](## "svi_profiles.[].vxlan") | Boolean |  | `True` |  | Extend this SVI over VXLAN. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mtu</samp>](## "svi_profiles.[].mtu") | Integer |  |  |  | Interface MTU. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ospf</samp>](## "svi_profiles.[].ospf") | Dictionary |  |  |  | OSPF interface configuration. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "svi_profiles.[].ospf.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;point_to_point</samp>](## "svi_profiles.[].ospf.point_to_point") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;area</samp>](## "svi_profiles.[].ospf.area") | String |  | `0` |  | OSPF area ID. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cost</samp>](## "svi_profiles.[].ospf.cost") | Integer |  |  |  | OSPF link cost. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;authentication</samp>](## "svi_profiles.[].ospf.authentication") | String |  |  | Valid Values:<br>- simple<br>- message-digest |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;simple_auth_key</samp>](## "svi_profiles.[].ospf.simple_auth_key") | String |  |  |  | Password used with simple authentication. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;message_digest_keys</samp>](## "svi_profiles.[].ospf.message_digest_keys") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- id</samp>](## "svi_profiles.[].ospf.message_digest_keys.[].id") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hash_algorithm</samp>](## "svi_profiles.[].ospf.message_digest_keys.[].hash_algorithm") | String |  | `sha512` | Valid Values:<br>- md5<br>- sha1<br>- sha256<br>- sha384<br>- sha512 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key</samp>](## "svi_profiles.[].ospf.message_digest_keys.[].key") | String |  |  |  | Type 7 encrypted key. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;bgp</samp>](## "svi_profiles.[].bgp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "svi_profiles.[].bgp.structured_config") | Dictionary |  |  |  | Structured configuration and EOS CLI commands rendered on router_bgp.vlans.<br>This configuration will not be applied to vlan aware bundles<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "svi_profiles.[].bgp.raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the Router BGP, VLAN definition in the final EOS configuration.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "svi_profiles.[].raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the VLAN interface in the final EOS configuration.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "svi_profiles.[].structured_config") | Dictionary |  |  |  | Custom structured config added under vlan_interfaces.<interface> for eos_cli_config_gen. |

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
    1 # (28)!
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
              structured_config: <dict>
              raw_eos_cli: <str>
            raw_eos_cli: <str>
            structured_config: <dict>
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
    2 # (81)!
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
          structured_config: <dict>
          raw_eos_cli: <str>
        raw_eos_cli: <str>
        structured_config: <dict>
    ```

    0. Default Value

        ```yaml
        '        tags':
        - all

        ```
    0. Default Value

        ```yaml
        '    tags':
        - all

        ```
