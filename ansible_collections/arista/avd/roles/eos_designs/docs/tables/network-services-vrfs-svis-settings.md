<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>&lt;network_services_keys.name&gt;</samp>](## "<network_services_keys.name>") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;-&nbsp;name</samp>](## "<network_services_keys.name>.[].name") | String | Required, Unique |  |  | Specify a tenant name.<br>Tenant provide a construct to group L3 VRFs and L2 VLANs.<br>Networks services can be filtered by tenant name.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vrfs</samp>](## "<network_services_keys.name>.[].vrfs") | List, items: Dictionary |  |  |  | VRFs will only be configured on a node if any of the underlying objects like `svis` or `l3_interfaces` apply to the node.<br><br>It is recommended to only define a VRF in one Tenant. If the same VRF name is used across multiple tenants and those tenants<br>are accepted by `filter.tenants` on the node, any object set under the duplicate VRFs must either be unique or be an exact match.<br><br>VRF "default" is partially supported under network-services. Currently the supported options for "default" vrf are route-target,<br>route-distinguisher settings, structured_config, raw_eos_cli in bgp and SVIs are the only supported interface type.<br>Vlan-aware-bundles are supported as well inside default vrf. OSPF is not supported currently.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "<network_services_keys.name>.[].vrfs.[].name") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;svis</samp>](## "<network_services_keys.name>.[].vrfs.[].svis") | List, items: Dictionary |  |  |  | List of SVIs.<br>This will create both the L3 SVI and L2 VLAN based on filters applied to the node.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;id</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].id") | Integer | Required, Unique |  | Min: 1<br>Max: 4096 | SVI interface id and VLAN id. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].name") | String | Required |  |  | VLAN name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;profile</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].profile") | String |  |  |  | SVI profile name to apply.<br>SVI can refer to one svi_profile which again can refer to another svi_profile to inherit settings in up to two levels (svi -> svi_profile -> svi_parent_profile).<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tags</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].tags") | List, items: String |  | `['all']` |  | Tags leveraged for networks services filtering.<br>Tags are matched against "filter.tags" defined under node type settings.<br>Tags are also matched against the "node_group" name under node type settings.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].tags.[]") | String |  |  |  | Tag value. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].nodes") | List, items: Dictionary |  |  |  | Define node specific configuration, such as unique IP addresses.<br>Any keys set here will be merged onto the SVI config, except `structured_config` keys which will replace the `structured_config` set on SVI level.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;node</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].nodes.[].node") | String | Required, Unique |  |  | l3_leaf inventory hostname |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tags</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].nodes.[].tags") | List, items: String |  | `['all']` |  | Tags leveraged for networks services filtering.<br>Tags are matched against "filter.tags" defined under node type settings.<br>Tags are also matched against the "node_group" name under node type settings.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].nodes.[].tags.[]") | String |  |  |  | Tag value. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].nodes.[].name") | String |  |  |  | VLAN name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].nodes.[].enabled") | Boolean |  |  |  | Enable or disable interface |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].nodes.[].description") | String |  |  |  | SVI description. By default set to VLAN name.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].nodes.[].ip_address") | String |  |  |  | IPv4_address/Mask. Usually set under "nodes" to have unique IPv4 addresses per node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_address</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].nodes.[].ipv6_address") | String |  |  |  | IPv6_address/Mask. Usually set under "nodes" to have unique IPv6 addresses per node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_enable</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].nodes.[].ipv6_enable") | Boolean |  |  |  | Explicitly enable/disable link-local IPv6 addressing. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_address_virtual</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].nodes.[].ip_address_virtual") | String |  |  |  | IPv4_address/Mask<br>IPv4 VXLAN Anycast IP address<br>Conserves IP addresses in VXLAN deployments as it doesn't require unique IP addresses on each node.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_address_virtual</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].nodes.[].ipv6_address_virtual") <span style="color:red">deprecated</span> | String |  |  |  | IPv6_address/Mask<br>ipv6 address virtuals to configure VXLAN Anycast IP address (Optional)<br>If both "ipv6_address_virtual" and "ipv6_address_virtuals" are set, all addresses will be configured<br><span style="color:red">This key is deprecated. Support will be removed in AVD version 5.0.0. Use <samp>ipv6_address_virtuals</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_address_virtuals</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].nodes.[].ipv6_address_virtuals") | List, items: String |  |  |  | IPv6 VXLAN Anycast IP addresses<br>Conserves IPv6 addresses in VXLAN deployments as it doesn't require unique IPv6 addresses on each node.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].nodes.[].ipv6_address_virtuals.[]") | String |  |  |  | IPv6_address/Mask |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_address_virtual_secondaries</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].nodes.[].ip_address_virtual_secondaries") | List, items: String |  |  |  | Secondary IPv4 VXLAN Anycast IP addresses |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].nodes.[].ip_address_virtual_secondaries.[]") | String |  |  |  | IPv4_address/Mask |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_virtual_router_addresses</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].nodes.[].ip_virtual_router_addresses") | List, items: String |  |  |  | IPv4 VARP addresses.<br>Requires an IP address to be configured on the SVI.<br>If ip_address_virtual is also set, ip_virtual_router_addresses will take precedence<br>_if_ there is an ip_address configured for the node.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].nodes.[].ip_virtual_router_addresses.[]") | String |  |  |  | IPv4_address/Mask or IPv4_address<br>IPv4_address/Mask will also configure a static route to the SVI per best practice.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_virtual_router_addresses</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].nodes.[].ipv6_virtual_router_addresses") | List, items: String |  |  |  | IPv6 VARP addresses.<br>Requires an IPv6 address to be configured on the SVI.<br>If ipv6_address_virtuals is also set, ipv6_virtual_router_addresses will take precedence<br>_if_ there is an ipv6_address configured for the node.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].nodes.[].ipv6_virtual_router_addresses.[]") | String |  |  |  | IPv6_address |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_helpers</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].nodes.[].ip_helpers") | List, items: Dictionary |  |  |  | IP helper for DHCP relay |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;ip_helper</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].nodes.[].ip_helpers.[].ip_helper") | String | Required, Unique |  |  | IPv4 DHCP server IP |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_interface</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].nodes.[].ip_helpers.[].source_interface") | String |  |  |  | Interface name to originate DHCP relay packets to DHCP server. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_vrf</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].nodes.[].ip_helpers.[].source_vrf") | String |  |  |  | VRF to originate DHCP relay packets to DHCP server. If not set, EOS uses the VRF on the SVI. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vni_override</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].nodes.[].vni_override") | Integer |  |  | Min: 1<br>Max: 16777215 | By default the VNI will be derived from "mac_vrf_vni_base".<br>The vni_override allows us to override this value and statically define it (optional).<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rt_override</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].nodes.[].rt_override") | String |  |  |  | By default the MAC VRF RT will be derived from mac_vrf_id_base + vlan_id.<br>The rt_override allows us to override this value and statically define it.<br>rt_override will default to vni_override if set.<br><br>rt_override supports two formats:<br>  - A single number which will be used in the RT fields instead of mac_vrf_id/mac_vrf_vni (see 'overlay_rt_type' for details).<br>  - A full RT string with colon seperator which will override the full RT.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rd_override</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].nodes.[].rd_override") | String |  |  |  | By default the MAC VRF RD will be derived from mac_vrf_id_base + vlan_id.<br>The rt_override allows us to override this value and statically define it.<br>rd_override will default to rt_override or vni_override if set.<br><br>rd_override supports two formats:<br>  - A single number which will be used in the RD assigned number field instead of mac_vrf_id/mac_vrf_vni (see 'overlay_rd_type' for details).<br>  - A full RD string with colon seperator which will override the full RD.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;trunk_groups</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].nodes.[].trunk_groups") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].nodes.[].trunk_groups.[]") | String |  |  |  | Trunk groups are used for limiting vlans to trunk ports assigned to the same trunk group.<br>Requires "enable_trunk_groups: true".<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vxlan</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].nodes.[].vxlan") | Boolean |  | `True` |  | Extend this SVI over VXLAN. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mtu</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].nodes.[].mtu") | Integer |  |  |  | Interface MTU. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].nodes.[].bgp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].nodes.[].bgp.structured_config") | Dictionary |  |  |  | Structured configuration and EOS CLI commands rendered on router_bgp.vlans.[id=<vlan>]<br>This configuration will not be applied to vlan aware bundles<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].nodes.[].bgp.raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the Router BGP, VLAN definition in the final EOS configuration.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].nodes.[].raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the VLAN interface in the final EOS configuration.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].nodes.[].structured_config") | Dictionary |  |  |  | Custom structured config added under vlan_interfaces.[name=<interface>] for eos_cli_config_gen.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].enabled") | Boolean |  |  |  | Enable or disable interface |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].description") | String |  |  |  | SVI description. By default set to VLAN name.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].ip_address") | String |  |  |  | IPv4_address/Mask. Usually set under "nodes" to have unique IPv4 addresses per node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_address</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].ipv6_address") | String |  |  |  | IPv6_address/Mask. Usually set under "nodes" to have unique IPv6 addresses per node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_enable</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].ipv6_enable") | Boolean |  |  |  | Explicitly enable/disable link-local IPv6 addressing. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_address_virtual</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].ip_address_virtual") | String |  |  |  | IPv4_address/Mask<br>IPv4 VXLAN Anycast IP address<br>Conserves IP addresses in VXLAN deployments as it doesn't require unique IP addresses on each node.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_address_virtual</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].ipv6_address_virtual") <span style="color:red">deprecated</span> | String |  |  |  | IPv6_address/Mask<br>ipv6 address virtuals to configure VXLAN Anycast IP address (Optional)<br>If both "ipv6_address_virtual" and "ipv6_address_virtuals" are set, all addresses will be configured<br><span style="color:red">This key is deprecated. Support will be removed in AVD version 5.0.0. Use <samp>ipv6_address_virtuals</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_address_virtuals</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].ipv6_address_virtuals") | List, items: String |  |  |  | IPv6 VXLAN Anycast IP addresses<br>Conserves IPv6 addresses in VXLAN deployments as it doesn't require unique IPv6 addresses on each node.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].ipv6_address_virtuals.[]") | String |  |  |  | IPv6_address/Mask |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_address_virtual_secondaries</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].ip_address_virtual_secondaries") | List, items: String |  |  |  | Secondary IPv4 VXLAN Anycast IP addresses |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].ip_address_virtual_secondaries.[]") | String |  |  |  | IPv4_address/Mask |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_virtual_router_addresses</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].ip_virtual_router_addresses") | List, items: String |  |  |  | IPv4 VARP addresses.<br>Requires an IP address to be configured on the SVI.<br>If ip_address_virtual is also set, ip_virtual_router_addresses will take precedence<br>_if_ there is an ip_address configured for the node.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].ip_virtual_router_addresses.[]") | String |  |  |  | IPv4_address/Mask or IPv4_address<br>IPv4_address/Mask will also configure a static route to the SVI per best practice.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_virtual_router_addresses</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].ipv6_virtual_router_addresses") | List, items: String |  |  |  | IPv6 VARP addresses.<br>Requires an IPv6 address to be configured on the SVI.<br>If ipv6_address_virtuals is also set, ipv6_virtual_router_addresses will take precedence<br>_if_ there is an ipv6_address configured for the node.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].ipv6_virtual_router_addresses.[]") | String |  |  |  | IPv6_address |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_helpers</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].ip_helpers") | List, items: Dictionary |  |  |  | IP helper for DHCP relay |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;ip_helper</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].ip_helpers.[].ip_helper") | String | Required, Unique |  |  | IPv4 DHCP server IP |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_interface</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].ip_helpers.[].source_interface") | String |  |  |  | Interface name to originate DHCP relay packets to DHCP server. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_vrf</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].ip_helpers.[].source_vrf") | String |  |  |  | VRF to originate DHCP relay packets to DHCP server. If not set, EOS uses the VRF on the SVI. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vni_override</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].vni_override") | Integer |  |  | Min: 1<br>Max: 16777215 | By default the VNI will be derived from "mac_vrf_vni_base".<br>The vni_override allows us to override this value and statically define it (optional).<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rt_override</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].rt_override") | String |  |  |  | By default the MAC VRF RT will be derived from mac_vrf_id_base + vlan_id.<br>The rt_override allows us to override this value and statically define it.<br>rt_override will default to vni_override if set.<br><br>rt_override supports two formats:<br>  - A single number which will be used in the RT fields instead of mac_vrf_id/mac_vrf_vni (see 'overlay_rt_type' for details).<br>  - A full RT string with colon seperator which will override the full RT.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rd_override</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].rd_override") | String |  |  |  | By default the MAC VRF RD will be derived from mac_vrf_id_base + vlan_id.<br>The rt_override allows us to override this value and statically define it.<br>rd_override will default to rt_override or vni_override if set.<br><br>rd_override supports two formats:<br>  - A single number which will be used in the RD assigned number field instead of mac_vrf_id/mac_vrf_vni (see 'overlay_rd_type' for details).<br>  - A full RD string with colon seperator which will override the full RD.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;trunk_groups</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].trunk_groups") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].trunk_groups.[]") | String |  |  |  | Trunk groups are used for limiting vlans to trunk ports assigned to the same trunk group.<br>Requires "enable_trunk_groups: true".<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vxlan</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].vxlan") | Boolean |  | `True` |  | Extend this SVI over VXLAN. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mtu</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].mtu") | Integer |  |  |  | Interface MTU. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].bgp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].bgp.structured_config") | Dictionary |  |  |  | Structured configuration and EOS CLI commands rendered on router_bgp.vlans.[id=<vlan>]<br>This configuration will not be applied to vlan aware bundles<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].bgp.raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the Router BGP, VLAN definition in the final EOS configuration.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the VLAN interface in the final EOS configuration.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].structured_config") | Dictionary |  |  |  | Custom structured config added under vlan_interfaces.[name=<interface>] for eos_cli_config_gen.<br> |

=== "YAML"

    ```yaml
    <network_services_keys.name>:

        # Specify a tenant name.
        # Tenant provide a construct to group L3 VRFs and L2 VLANs.
        # Networks services can be filtered by tenant name.
      - name: <str; required; unique>

        # VRFs will only be configured on a node if any of the underlying objects like `svis` or `l3_interfaces` apply to the node.

        # It is recommended to only define a VRF in one Tenant. If the same VRF name is used across multiple tenants and those tenants
        # are accepted by `filter.tenants` on the node, any object set under the duplicate VRFs must either be unique or be an exact match.

        # VRF "default" is partially supported under network-services. Currently the supported options for "default" vrf are route-target,
        # route-distinguisher settings, structured_config, raw_eos_cli in bgp and SVIs are the only supported interface type.
        # Vlan-aware-bundles are supported as well inside default vrf. OSPF is not supported currently.
        vrfs:
          - name: <str; required; unique>

            # List of SVIs.
            # This will create both the L3 SVI and L2 VLAN based on filters applied to the node.
            svis:

                # SVI interface id and VLAN id.
              - id: <int; 1-4096; required; unique>

                # VLAN name.
                name: <str; required>

                # SVI profile name to apply.
                # SVI can refer to one svi_profile which again can refer to another svi_profile to inherit settings in up to two levels (svi -> svi_profile -> svi_parent_profile).
                profile: <str>

                # Tags leveraged for networks services filtering.
                # Tags are matched against "filter.tags" defined under node type settings.
                # Tags are also matched against the "node_group" name under node type settings.
                tags: # default=['all']

                    # Tag value.
                  - <str>

                # Define node specific configuration, such as unique IP addresses.
                # Any keys set here will be merged onto the SVI config, except `structured_config` keys which will replace the `structured_config` set on SVI level.
                nodes:

                    # l3_leaf inventory hostname
                  - node: <str; required; unique>

                    # Tags leveraged for networks services filtering.
                    # Tags are matched against "filter.tags" defined under node type settings.
                    # Tags are also matched against the "node_group" name under node type settings.
                    tags: # default=['all']

                        # Tag value.
                      - <str>

                    # VLAN name
                    name: <str>

                    # Enable or disable interface
                    enabled: <bool>

                    # SVI description. By default set to VLAN name.
                    description: <str>

                    # IPv4_address/Mask. Usually set under "nodes" to have unique IPv4 addresses per node.
                    ip_address: <str>

                    # IPv6_address/Mask. Usually set under "nodes" to have unique IPv6 addresses per node.
                    ipv6_address: <str>

                    # Explicitly enable/disable link-local IPv6 addressing.
                    ipv6_enable: <bool>

                    # IPv4_address/Mask
                    # IPv4 VXLAN Anycast IP address
                    # Conserves IP addresses in VXLAN deployments as it doesn't require unique IP addresses on each node.
                    ip_address_virtual: <str>

                    # IPv6_address/Mask
                    # ipv6 address virtuals to configure VXLAN Anycast IP address (Optional)
                    # If both "ipv6_address_virtual" and "ipv6_address_virtuals" are set, all addresses will be configured
                    # This key is deprecated.
                    # Support will be removed in AVD version 5.0.0.
                    # Use <samp>ipv6_address_virtuals</samp> instead.
                    ipv6_address_virtual: <str>

                    # IPv6 VXLAN Anycast IP addresses
                    # Conserves IPv6 addresses in VXLAN deployments as it doesn't require unique IPv6 addresses on each node.
                    ipv6_address_virtuals:

                        # IPv6_address/Mask
                      - <str>

                    # Secondary IPv4 VXLAN Anycast IP addresses
                    ip_address_virtual_secondaries:

                        # IPv4_address/Mask
                      - <str>

                    # IPv4 VARP addresses.
                    # Requires an IP address to be configured on the SVI.
                    # If ip_address_virtual is also set, ip_virtual_router_addresses will take precedence
                    # _if_ there is an ip_address configured for the node.
                    ip_virtual_router_addresses:

                        # IPv4_address/Mask or IPv4_address
                        # IPv4_address/Mask will also configure a static route to the SVI per best practice.
                      - <str>

                    # IPv6 VARP addresses.
                    # Requires an IPv6 address to be configured on the SVI.
                    # If ipv6_address_virtuals is also set, ipv6_virtual_router_addresses will take precedence
                    # _if_ there is an ipv6_address configured for the node.
                    ipv6_virtual_router_addresses:

                        # IPv6_address
                      - <str>

                    # IP helper for DHCP relay
                    ip_helpers:

                        # IPv4 DHCP server IP
                      - ip_helper: <str; required; unique>

                        # Interface name to originate DHCP relay packets to DHCP server.
                        source_interface: <str>

                        # VRF to originate DHCP relay packets to DHCP server. If not set, EOS uses the VRF on the SVI.
                        source_vrf: <str>

                    # By default the VNI will be derived from "mac_vrf_vni_base".
                    # The vni_override allows us to override this value and statically define it (optional).
                    vni_override: <int; 1-16777215>

                    # By default the MAC VRF RT will be derived from mac_vrf_id_base + vlan_id.
                    # The rt_override allows us to override this value and statically define it.
                    # rt_override will default to vni_override if set.

                    # rt_override supports two formats:
                    #   - A single number which will be used in the RT fields instead of mac_vrf_id/mac_vrf_vni (see 'overlay_rt_type' for details).
                    #   - A full RT string with colon seperator which will override the full RT.
                    rt_override: <str>

                    # By default the MAC VRF RD will be derived from mac_vrf_id_base + vlan_id.
                    # The rt_override allows us to override this value and statically define it.
                    # rd_override will default to rt_override or vni_override if set.

                    # rd_override supports two formats:
                    #   - A single number which will be used in the RD assigned number field instead of mac_vrf_id/mac_vrf_vni (see 'overlay_rd_type' for details).
                    #   - A full RD string with colon seperator which will override the full RD.
                    rd_override: <str>
                    trunk_groups:

                        # Trunk groups are used for limiting vlans to trunk ports assigned to the same trunk group.
                        # Requires "enable_trunk_groups: true".
                      - <str>

                    # Extend this SVI over VXLAN.
                    vxlan: <bool; default=True>

                    # Interface MTU.
                    mtu: <int>
                    bgp:

                      # Structured configuration and EOS CLI commands rendered on router_bgp.vlans.[id=<vlan>]
                      # This configuration will not be applied to vlan aware bundles
                      structured_config: <dict>

                      # EOS CLI rendered directly on the Router BGP, VLAN definition in the final EOS configuration.
                      raw_eos_cli: <str>

                    # EOS CLI rendered directly on the VLAN interface in the final EOS configuration.
                    raw_eos_cli: <str>

                    # Custom structured config added under vlan_interfaces.[name=<interface>] for eos_cli_config_gen.
                    structured_config: <dict>

                # Enable or disable interface
                enabled: <bool>

                # SVI description. By default set to VLAN name.
                description: <str>

                # IPv4_address/Mask. Usually set under "nodes" to have unique IPv4 addresses per node.
                ip_address: <str>

                # IPv6_address/Mask. Usually set under "nodes" to have unique IPv6 addresses per node.
                ipv6_address: <str>

                # Explicitly enable/disable link-local IPv6 addressing.
                ipv6_enable: <bool>

                # IPv4_address/Mask
                # IPv4 VXLAN Anycast IP address
                # Conserves IP addresses in VXLAN deployments as it doesn't require unique IP addresses on each node.
                ip_address_virtual: <str>

                # IPv6_address/Mask
                # ipv6 address virtuals to configure VXLAN Anycast IP address (Optional)
                # If both "ipv6_address_virtual" and "ipv6_address_virtuals" are set, all addresses will be configured
                # This key is deprecated.
                # Support will be removed in AVD version 5.0.0.
                # Use <samp>ipv6_address_virtuals</samp> instead.
                ipv6_address_virtual: <str>

                # IPv6 VXLAN Anycast IP addresses
                # Conserves IPv6 addresses in VXLAN deployments as it doesn't require unique IPv6 addresses on each node.
                ipv6_address_virtuals:

                    # IPv6_address/Mask
                  - <str>

                # Secondary IPv4 VXLAN Anycast IP addresses
                ip_address_virtual_secondaries:

                    # IPv4_address/Mask
                  - <str>

                # IPv4 VARP addresses.
                # Requires an IP address to be configured on the SVI.
                # If ip_address_virtual is also set, ip_virtual_router_addresses will take precedence
                # _if_ there is an ip_address configured for the node.
                ip_virtual_router_addresses:

                    # IPv4_address/Mask or IPv4_address
                    # IPv4_address/Mask will also configure a static route to the SVI per best practice.
                  - <str>

                # IPv6 VARP addresses.
                # Requires an IPv6 address to be configured on the SVI.
                # If ipv6_address_virtuals is also set, ipv6_virtual_router_addresses will take precedence
                # _if_ there is an ipv6_address configured for the node.
                ipv6_virtual_router_addresses:

                    # IPv6_address
                  - <str>

                # IP helper for DHCP relay
                ip_helpers:

                    # IPv4 DHCP server IP
                  - ip_helper: <str; required; unique>

                    # Interface name to originate DHCP relay packets to DHCP server.
                    source_interface: <str>

                    # VRF to originate DHCP relay packets to DHCP server. If not set, EOS uses the VRF on the SVI.
                    source_vrf: <str>

                # By default the VNI will be derived from "mac_vrf_vni_base".
                # The vni_override allows us to override this value and statically define it (optional).
                vni_override: <int; 1-16777215>

                # By default the MAC VRF RT will be derived from mac_vrf_id_base + vlan_id.
                # The rt_override allows us to override this value and statically define it.
                # rt_override will default to vni_override if set.

                # rt_override supports two formats:
                #   - A single number which will be used in the RT fields instead of mac_vrf_id/mac_vrf_vni (see 'overlay_rt_type' for details).
                #   - A full RT string with colon seperator which will override the full RT.
                rt_override: <str>

                # By default the MAC VRF RD will be derived from mac_vrf_id_base + vlan_id.
                # The rt_override allows us to override this value and statically define it.
                # rd_override will default to rt_override or vni_override if set.

                # rd_override supports two formats:
                #   - A single number which will be used in the RD assigned number field instead of mac_vrf_id/mac_vrf_vni (see 'overlay_rd_type' for details).
                #   - A full RD string with colon seperator which will override the full RD.
                rd_override: <str>
                trunk_groups:

                    # Trunk groups are used for limiting vlans to trunk ports assigned to the same trunk group.
                    # Requires "enable_trunk_groups: true".
                  - <str>

                # Extend this SVI over VXLAN.
                vxlan: <bool; default=True>

                # Interface MTU.
                mtu: <int>
                bgp:

                  # Structured configuration and EOS CLI commands rendered on router_bgp.vlans.[id=<vlan>]
                  # This configuration will not be applied to vlan aware bundles
                  structured_config: <dict>

                  # EOS CLI rendered directly on the Router BGP, VLAN definition in the final EOS configuration.
                  raw_eos_cli: <str>

                # EOS CLI rendered directly on the VLAN interface in the final EOS configuration.
                raw_eos_cli: <str>

                # Custom structured config added under vlan_interfaces.[name=<interface>] for eos_cli_config_gen.
                structured_config: <dict>
    ```
