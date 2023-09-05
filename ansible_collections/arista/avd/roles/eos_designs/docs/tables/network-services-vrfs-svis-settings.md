<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>&lt;network_services_keys.name&gt;</samp>](## "&lt;network_services_keys.name&gt;") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;- name</samp>](## "&lt;network_services_keys.name&gt;.[].name") | String | Required, Unique |  |  | Specify a tenant name.<br>Tenant provide a construct to group L3 VRFs and L2 VLANs.<br>Networks services can be filtered by tenant name.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vrfs</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs") | List, items: Dictionary |  |  |  | VRFs will only be configured on a node if any of the underlying objects like `svis` or `l3_interfaces` apply to the node.<br><br>It is recommended to only define a VRF in one Tenant. If the same VRF name is used across multiple tenants and those tenants<br>are accepted by `filter.tenants` on the node, any object set under the duplicate VRFs must either be unique or be an exact match.<br><br>VRF "default" is partially supported under network-services. Currently the supported options for "default" vrf are route-target,<br>route-distinguisher settings, structured_config, raw_eos_cli in bgp and SVIs are the only supported interface type.<br>Vlan-aware-bundles are supported as well inside default vrf. OSPF is not supported currently.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].name") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;svis</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis") | List, items: Dictionary |  |  |  | List of SVIs.<br>This will create both the L3 SVI and L2 VLAN based on filters applied to the node.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- id</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].id") | Integer | Required, Unique |  | Min: 1<br>Max: 4096 | SVI interface id and VLAN id. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].name") | String | Required |  |  | VLAN name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;profile</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].profile") | String |  |  |  | SVI profile name to apply.<br>SVI can refer to one svi_profile which again can refer to another svi_profile to inherit settings in up to two levels (svi -> svi_profile -> svi_parent_profile).<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes") | List, items: Dictionary |  |  |  | Define node specific configuration, such as unique IP addresses.<br>Any keys set here will be merged onto the SVI config, except `structured_config` keys which will replace the `structured_config` set on SVI level.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- node</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].node") | String | Required, Unique |  |  | l3_leaf inventory hostname |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].name") | String |  |  |  | VLAN name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].enabled") | Boolean |  |  |  | Enable or disable interface |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].description") | String |  |  |  | SVI description. By default set to VLAN name.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].ip_address") | String |  |  |  | IPv4_address/Mask. Usually set under "nodes" to have unique IPv4 addresses per node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_address</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].ipv6_address") | String |  |  |  | IPv6_address/Mask. Usually set under "nodes" to have unique IPv6 addresses per node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_enable</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].ipv6_enable") | Boolean |  |  |  | Explicitly enable/disable link-local IPv6 addressing. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_address_virtual</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].ip_address_virtual") | String |  |  |  | IPv4_address/Mask<br>IPv4 VXLAN Anycast IP address<br>Conserves IP addresses in VXLAN deployments as it doesn't require unique IP addresses on each node.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_address_virtual</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].ipv6_address_virtual") <span style="color:red">deprecated</span> | String |  |  |  | IPv6_address/Mask<br>ipv6 address virtuals to configure VXLAN Anycast IP address (Optional)<br>If both "ipv6_address_virtual" and "ipv6_address_virtuals" are set, all addresses will be configured<br><span style="color:red">This key is deprecated. Support will be removed in AVD version 5.0.0. Use <samp>ipv6_address_virtuals</samp> instead.</span> |
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
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vni_override</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].vni_override") | Integer |  |  | Min: 1<br>Max: 16777215 | By default the VNI will be derived from "mac_vrf_vni_base".<br>The vni_override allows us to override this value and statically define it (optional).<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rt_override</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].rt_override") | String |  |  |  | By default the MAC VRF RT will be derived from mac_vrf_id_base + vlan_id.<br>The rt_override allows us to override this value and statically define it.<br>rt_override will default to vni_override if set.<br><br>rt_override supports two formats:<br>  - A single number which will be used in the RT fields instead of mac_vrf_id/mac_vrf_vni (see 'overlay_rt_type' for details).<br>  - A full RT string with colon seperator which will override the full RT.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rd_override</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].rd_override") | String |  |  |  | By default the MAC VRF RD will be derived from mac_vrf_id_base + vlan_id.<br>The rt_override allows us to override this value and statically define it.<br>rd_override will default to rt_override or vni_override if set.<br><br>rd_override supports two formats:<br>  - A single number which will be used in the RD assigned number field instead of mac_vrf_id/mac_vrf_vni (see 'overlay_rd_type' for details).<br>  - A full RD string with colon seperator which will override the full RD.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tags</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].tags") | List, items: String |  | `['all']` |  | Tags leveraged for networks services filtering.<br>Tags are matched against "filter.tags" defined under node type settings.<br>Tags are also matched against the "node_group" name under node type settings.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].tags.[].&lt;str&gt;") | String |  |  |  | Tag value. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;trunk_groups</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].trunk_groups") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].trunk_groups.[].&lt;str&gt;") | String |  |  |  | Trunk groups are used for limiting vlans to trunk ports assigned to the same trunk group.<br>Requires "enable_trunk_groups: true".<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vxlan</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].vxlan") | Boolean |  | `True` |  | Extend this SVI over VXLAN. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mtu</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].mtu") | Integer |  |  |  | Interface MTU. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].bgp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].bgp.structured_config") | Dictionary |  |  |  | Structured configuration and EOS CLI commands rendered on router_bgp.vlans.[id=<vlan>]<br>This configuration will not be applied to vlan aware bundles<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].bgp.raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the Router BGP, VLAN definition in the final EOS configuration.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the VLAN interface in the final EOS configuration.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].structured_config") | Dictionary |  |  |  | Custom structured config added under vlan_interfaces.[name=<interface>] for eos_cli_config_gen.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].enabled") | Boolean |  |  |  | Enable or disable interface |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].description") | String |  |  |  | SVI description. By default set to VLAN name.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].ip_address") | String |  |  |  | IPv4_address/Mask. Usually set under "nodes" to have unique IPv4 addresses per node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_address</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].ipv6_address") | String |  |  |  | IPv6_address/Mask. Usually set under "nodes" to have unique IPv6 addresses per node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_enable</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].ipv6_enable") | Boolean |  |  |  | Explicitly enable/disable link-local IPv6 addressing. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_address_virtual</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].ip_address_virtual") | String |  |  |  | IPv4_address/Mask<br>IPv4 VXLAN Anycast IP address<br>Conserves IP addresses in VXLAN deployments as it doesn't require unique IP addresses on each node.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_address_virtual</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].ipv6_address_virtual") <span style="color:red">deprecated</span> | String |  |  |  | IPv6_address/Mask<br>ipv6 address virtuals to configure VXLAN Anycast IP address (Optional)<br>If both "ipv6_address_virtual" and "ipv6_address_virtuals" are set, all addresses will be configured<br><span style="color:red">This key is deprecated. Support will be removed in AVD version 5.0.0. Use <samp>ipv6_address_virtuals</samp> instead.</span> |
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
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vni_override</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].vni_override") | Integer |  |  | Min: 1<br>Max: 16777215 | By default the VNI will be derived from "mac_vrf_vni_base".<br>The vni_override allows us to override this value and statically define it (optional).<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rt_override</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].rt_override") | String |  |  |  | By default the MAC VRF RT will be derived from mac_vrf_id_base + vlan_id.<br>The rt_override allows us to override this value and statically define it.<br>rt_override will default to vni_override if set.<br><br>rt_override supports two formats:<br>  - A single number which will be used in the RT fields instead of mac_vrf_id/mac_vrf_vni (see 'overlay_rt_type' for details).<br>  - A full RT string with colon seperator which will override the full RT.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rd_override</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].rd_override") | String |  |  |  | By default the MAC VRF RD will be derived from mac_vrf_id_base + vlan_id.<br>The rt_override allows us to override this value and statically define it.<br>rd_override will default to rt_override or vni_override if set.<br><br>rd_override supports two formats:<br>  - A single number which will be used in the RD assigned number field instead of mac_vrf_id/mac_vrf_vni (see 'overlay_rd_type' for details).<br>  - A full RD string with colon seperator which will override the full RD.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tags</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].tags") | List, items: String |  | `['all']` |  | Tags leveraged for networks services filtering.<br>Tags are matched against "filter.tags" defined under node type settings.<br>Tags are also matched against the "node_group" name under node type settings.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].tags.[].&lt;str&gt;") | String |  |  |  | Tag value. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;trunk_groups</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].trunk_groups") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].trunk_groups.[].&lt;str&gt;") | String |  |  |  | Trunk groups are used for limiting vlans to trunk ports assigned to the same trunk group.<br>Requires "enable_trunk_groups: true".<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vxlan</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].vxlan") | Boolean |  | `True` |  | Extend this SVI over VXLAN. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mtu</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].mtu") | Integer |  |  |  | Interface MTU. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].bgp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].bgp.structured_config") | Dictionary |  |  |  | Structured configuration and EOS CLI commands rendered on router_bgp.vlans.[id=<vlan>]<br>This configuration will not be applied to vlan aware bundles<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].bgp.raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the Router BGP, VLAN definition in the final EOS configuration.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the VLAN interface in the final EOS configuration.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].structured_config") | Dictionary |  |  |  | Custom structured config added under vlan_interfaces.[name=<interface>] for eos_cli_config_gen.<br> |

=== "YAML"

    ```yaml
    <network_services_keys.name>:
      - name: <str>
        vrfs:
          - name: <str>
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
                    rt_override: <str>
                    rd_override: <str>
                    tags:
                      - <str>
                    trunk_groups:
                      - <str>
                    vxlan: <bool>
                    mtu: <int>
                    bgp:
                      structured_config: <dict>
                      raw_eos_cli: <str>
                    raw_eos_cli: <str>
                    structured_config: <dict>
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
                rt_override: <str>
                rd_override: <str>
                tags:
                  - <str>
                trunk_groups:
                  - <str>
                vxlan: <bool>
                mtu: <int>
                bgp:
                  structured_config: <dict>
                  raw_eos_cli: <str>
                raw_eos_cli: <str>
                structured_config: <dict>
    ```
