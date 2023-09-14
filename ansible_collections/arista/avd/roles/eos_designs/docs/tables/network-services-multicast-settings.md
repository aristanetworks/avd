<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>svi_profiles</samp>](## "svi_profiles") | List, items: Dictionary |  |  |  | Profiles to share common settings for SVIs under `<network_services_key>.[].vrfs.svis`.<br>Keys are the same used under SVIs. Keys defined under SVIs take precedence.<br>Note: structured configuration is not merged recursively and will be taken directly from the most specific level in the following order:<br>1. svi.nodes[inventory_hostname].structured_config<br>2. svi_profile.nodes[inventory_hostname].structured_config<br>3. svi_parent_profile.nodes[inventory_hostname].structured_config<br>4. svi.structured_config<br>5. svi_profile.structured_config<br>6. svi_parent_profile.structured_config<br> |
    | [<samp>&nbsp;&nbsp;- profile</samp>](## "svi_profiles.[].profile") | String | Required, Unique |  |  | Profile name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "svi_profiles.[].nodes") | List, items: Dictionary |  |  |  | Define node specific configuration, such as unique IP addresses.<br>Any keys set here will be merged onto the SVI config, except `structured_config` keys which will replace the `structured_config` set on SVI level.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- node</samp>](## "svi_profiles.[].nodes.[].node") | String | Required, Unique |  |  | l3_leaf inventory hostname |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_l2_multicast</samp>](## "svi_profiles.[].nodes.[].evpn_l2_multicast") | Dictionary |  |  |  | Explicitly enable or disable evpn_l2_multicast to override setting of `<network_services_key>.[].evpn_l2_multicast.enabled`.<br>When evpn_l2_multicast.enabled is set to true for a vlan or a tenant, "igmp snooping" and "igmp snooping querier" will always be enabled, overriding those individual settings.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "svi_profiles.[].nodes.[].evpn_l2_multicast.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_l3_multicast</samp>](## "svi_profiles.[].nodes.[].evpn_l3_multicast") | Dictionary |  |  |  | Explicitly enable or disable evpn_l3_multicast to override setting of `<network_services_key>.[].evpn_l3_multicast.enabled` and `<network_services_key>.[].vrfs.[].evpn_l3_multicast.enabled`.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "svi_profiles.[].nodes.[].evpn_l3_multicast.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;igmp_snooping_enabled</samp>](## "svi_profiles.[].nodes.[].igmp_snooping_enabled") | Boolean |  |  |  | Enable IGMP Snooping (Enabled by default on EOS). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;igmp_snooping_querier</samp>](## "svi_profiles.[].nodes.[].igmp_snooping_querier") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "svi_profiles.[].nodes.[].igmp_snooping_querier.enabled") | Boolean |  |  |  | Will be enabled automatically if evpn_l2_multicast is enabled. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_address</samp>](## "svi_profiles.[].nodes.[].igmp_snooping_querier.source_address") | String |  |  |  | IPv4_address<br>If not set, IP address of "Loopback0" will be used.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;version</samp>](## "svi_profiles.[].nodes.[].igmp_snooping_querier.version") | Integer |  |  | Valid Values:<br>- 1<br>- 2<br>- 3 | IGMP Version (By default EOS uses IGMP version 2 for IGMP querier). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;evpn_l2_multicast</samp>](## "svi_profiles.[].evpn_l2_multicast") | Dictionary |  |  |  | Explicitly enable or disable evpn_l2_multicast to override setting of `<network_services_key>.[].evpn_l2_multicast.enabled`.<br>When evpn_l2_multicast.enabled is set to true for a vlan or a tenant, "igmp snooping" and "igmp snooping querier" will always be enabled, overriding those individual settings.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "svi_profiles.[].evpn_l2_multicast.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;evpn_l3_multicast</samp>](## "svi_profiles.[].evpn_l3_multicast") | Dictionary |  |  |  | Explicitly enable or disable evpn_l3_multicast to override setting of `<network_services_key>.[].evpn_l3_multicast.enabled` and `<network_services_key>.[].vrfs.[].evpn_l3_multicast.enabled`.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "svi_profiles.[].evpn_l3_multicast.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;igmp_snooping_enabled</samp>](## "svi_profiles.[].igmp_snooping_enabled") | Boolean |  |  |  | Enable IGMP Snooping (Enabled by default on EOS). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;igmp_snooping_querier</samp>](## "svi_profiles.[].igmp_snooping_querier") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "svi_profiles.[].igmp_snooping_querier.enabled") | Boolean |  |  |  | Will be enabled automatically if evpn_l2_multicast is enabled. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_address</samp>](## "svi_profiles.[].igmp_snooping_querier.source_address") | String |  |  |  | IPv4_address<br>If not set, IP address of "Loopback0" will be used.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;version</samp>](## "svi_profiles.[].igmp_snooping_querier.version") | Integer |  |  | Valid Values:<br>- 1<br>- 2<br>- 3 | IGMP Version (By default EOS uses IGMP version 2 for IGMP querier). |
    | [<samp>&lt;network_services_keys.name&gt;</samp>](## "&lt;network_services_keys.name&gt;") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;- name</samp>](## "&lt;network_services_keys.name&gt;.[].name") | String | Required, Unique |  |  | Specify a tenant name.<br>Tenant provide a construct to group L3 VRFs and L2 VLANs.<br>Networks services can be filtered by tenant name.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;evpn_l2_multicast</samp>](## "&lt;network_services_keys.name&gt;.[].evpn_l2_multicast") | Dictionary |  |  |  | Enable EVPN L2 Multicast for all SVIs and l2vlans within Tenant.<br>- Multicast group binding is created only for Multicast traffic. BULL traffic will use ingress-replication.<br>- Configures binding between VXLAN, VLAN, and multicast group IPv4 address using the following formula:<br>  < evpn_l2_multicast.underlay_l2_multicast_group_ipv4_pool > + < vlan_id - 1 > + < evpn_l2_multicast.underlay_l2_multicast_group_ipv4_pool_offset >.<br>- The recommendation is to assign a /20 block within the 232.0.0.0/8 Source-Specific Multicast range.<br>- Enables `redistribute igmp` on the router bgp MAC VRF.<br>- When evpn_l2_multicast.enabled is true for a VLAN or a tenant, "igmp snooping" and "igmp snooping querier" will always be enabled - overriding those individual settings.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;network_services_keys.name&gt;.[].evpn_l2_multicast.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;underlay_l2_multicast_group_ipv4_pool</samp>](## "&lt;network_services_keys.name&gt;.[].evpn_l2_multicast.underlay_l2_multicast_group_ipv4_pool") | String |  |  |  | IPv4_address/Mask |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;underlay_l2_multicast_group_ipv4_pool_offset</samp>](## "&lt;network_services_keys.name&gt;.[].evpn_l2_multicast.underlay_l2_multicast_group_ipv4_pool_offset") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;evpn_l3_multicast</samp>](## "&lt;network_services_keys.name&gt;.[].evpn_l3_multicast") | Dictionary |  |  |  | Enable L3 Multicast for all SVIs and l3vlans within Tenant.<br>- In the evpn-l3ls design type, this enables L3 EVPN Multicast (aka OISM)'.<br>- Multicast group binding for VRF is created only for Multicast traffic. BULL traffic will use ingress-replication.<br>- Configures binding between VXLAN, VLAN, and multicast group IPv4 address using the following formula:<br>  < l3_multicast.evpn_underlay_l3_multicast_group_ipv4_pool > + < vrf_vni - 1 > + < l3_multicast.evpn_underlay_l3_multicast_group_ipv4_pool_offset >.<br>- The recommendation is to assign a /20 block within the 232.0.0.0/8 Source-Specific Multicast range.<br>- If enabled on an SVI using the anycast default gateway feature, a diagnostic loopback (see below) MUST be configured to source IGMP traffic.<br>- Enables `evpn multicast` on the router bgp VRF.<br>- When enabled on an SVI:<br>     - If switch is part of an MLAG pair, enables "pim ipv4 sparse-mode" on the SVI.<br>     - If switch is standalone or A-A MH, enables "ip igmp" on the SVI.<br>     - If "ip address virtual" is configured, enables "pim ipv4 local-interface" and uses the diagnostic Loopback defined in the VRF<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;network_services_keys.name&gt;.[].evpn_l3_multicast.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_underlay_l3_multicast_group_ipv4_pool</samp>](## "&lt;network_services_keys.name&gt;.[].evpn_l3_multicast.evpn_underlay_l3_multicast_group_ipv4_pool") | String | Required |  |  | IPv4_address/Mask |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_underlay_l3_multicast_group_ipv4_pool_offset</samp>](## "&lt;network_services_keys.name&gt;.[].evpn_l3_multicast.evpn_underlay_l3_multicast_group_ipv4_pool_offset") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_peg</samp>](## "&lt;network_services_keys.name&gt;.[].evpn_l3_multicast.evpn_peg") | List, items: Dictionary |  |  |  | For each group of nodes, allow configuration of EVPN PEG options.<br>The first group of settings where the device's hostname is present in the 'nodes' list will be used.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- nodes</samp>](## "&lt;network_services_keys.name&gt;.[].evpn_l3_multicast.evpn_peg.[].nodes") | List, items: String |  |  |  | A description will be applied to all nodes with RP addresses configured if not set. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;network_services_keys.name&gt;.[].evpn_l3_multicast.evpn_peg.[].nodes.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;transit</samp>](## "&lt;network_services_keys.name&gt;.[].evpn_l3_multicast.evpn_peg.[].transit") | Boolean |  |  |  | Enable EVPN PEG transit mode. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;pim_rp_addresses</samp>](## "&lt;network_services_keys.name&gt;.[].pim_rp_addresses") | List, items: Dictionary |  |  |  | For each group of nodes, allow configuration of RP Addresses & associated groups.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- rps</samp>](## "&lt;network_services_keys.name&gt;.[].pim_rp_addresses.[].rps") | List, items: String |  |  | Min Length: 1 | List of Rendevouz Points. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;network_services_keys.name&gt;.[].pim_rp_addresses.[].rps.[].&lt;str&gt;") | String |  |  |  | RP address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "&lt;network_services_keys.name&gt;.[].pim_rp_addresses.[].nodes") | List, items: String |  |  |  | Restrict configuration to specific nodes.<br>Configuration Will be applied to all nodes if not set.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;network_services_keys.name&gt;.[].pim_rp_addresses.[].nodes.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;groups</samp>](## "&lt;network_services_keys.name&gt;.[].pim_rp_addresses.[].groups") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;network_services_keys.name&gt;.[].pim_rp_addresses.[].groups.[].&lt;str&gt;") | String |  |  |  | Group_prefix/mask. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;igmp_snooping_querier</samp>](## "&lt;network_services_keys.name&gt;.[].igmp_snooping_querier") | Dictionary |  |  |  | Enable IGMP snooping querier for each SVI/l2vlan within tenant, by default using IP address of Loopback 0.<br>When enabled, IGMP snooping querier will only be configured on L3 devices, i.e., uplink_type: p2p.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;network_services_keys.name&gt;.[].igmp_snooping_querier.enabled") | Boolean |  |  |  | Will be enabled automatically if "evpn_l2_multicast" is enabled. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_address</samp>](## "&lt;network_services_keys.name&gt;.[].igmp_snooping_querier.source_address") | String |  |  | Format: ipv4 | Default IP address of Loopback0 |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;version</samp>](## "&lt;network_services_keys.name&gt;.[].igmp_snooping_querier.version") | Integer |  | `2` | Valid Values:<br>- 1<br>- 2<br>- 3 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vrfs</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs") | List, items: Dictionary |  |  |  | VRFs will only be configured on a node if any of the underlying objects like `svis` or `l3_interfaces` apply to the node.<br><br>It is recommended to only define a VRF in one Tenant. If the same VRF name is used across multiple tenants and those tenants<br>are accepted by `filter.tenants` on the node, any object set under the duplicate VRFs must either be unique or be an exact match.<br><br>VRF "default" is partially supported under network-services. Currently the supported options for "default" vrf are route-target,<br>route-distinguisher settings, structured_config, raw_eos_cli in bgp and SVIs are the only supported interface type.<br>Vlan-aware-bundles are supported as well inside default vrf. OSPF is not supported currently.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].name") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_l3_multicast</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].evpn_l3_multicast") | Dictionary |  |  |  | Explicitly enable or disable evpn_l3_multicast to override setting of `<network_services_key>.[].evpn_l3_multicast.enabled`.<br>Allow override of `<network_services_key>.[].evpn_l3_multicast` node_settings.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].evpn_l3_multicast.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_peg</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].evpn_l3_multicast.evpn_peg") | List, items: Dictionary |  |  |  | For each group of nodes, allow configuration of EVPN PEG features. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- nodes</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].evpn_l3_multicast.evpn_peg.[].nodes") | List, items: String |  |  |  | Restrict configuration to specific nodes.<br>Will apply to all nodes with RP addresses configured if not set.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].evpn_l3_multicast.evpn_peg.[].nodes.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;transit</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].evpn_l3_multicast.evpn_peg.[].transit") | Boolean |  | `False` |  | Enable EVPN PEG transit mode. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pim_rp_addresses</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].pim_rp_addresses") | List, items: Dictionary |  |  |  | For each group of nodes, allow configuration of RP Addresses & associated groups.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- rps</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].pim_rp_addresses.[].rps") | List, items: String |  |  |  | A minimum of one RP must be specified. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].pim_rp_addresses.[].rps.[].&lt;str&gt;") | String |  |  |  | RP address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].pim_rp_addresses.[].nodes") | List, items: String |  |  |  | Restrict configuration to specific nodes.<br>Configuration Will be applied to all nodes if not set.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].pim_rp_addresses.[].nodes.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;groups</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].pim_rp_addresses.[].groups") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].pim_rp_addresses.[].groups.[].&lt;str&gt;") | String |  |  |  | Group_prefix/mask. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_l2_multi_domain</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].evpn_l2_multi_domain") | Boolean |  |  |  | Explicitly extend all VLANs/VLAN-Aware Bundles inside the VRF to remote EVPN domains.<br>Overrides `<network_services_key>.[].evpn_l2_multi_domain`.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;svis</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis") | List, items: Dictionary |  |  |  | List of SVIs.<br>This will create both the L3 SVI and L2 VLAN based on filters applied to the node.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- id</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].id") | Integer | Required, Unique |  | Min: 1<br>Max: 4096 | SVI interface id and VLAN id. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes") | List, items: Dictionary |  |  |  | Define node specific configuration, such as unique IP addresses.<br>Any keys set here will be merged onto the SVI config, except `structured_config` keys which will replace the `structured_config` set on SVI level.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- node</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].node") | String | Required, Unique |  |  | l3_leaf inventory hostname |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_l2_multicast</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].evpn_l2_multicast") | Dictionary |  |  |  | Explicitly enable or disable evpn_l2_multicast to override setting of `<network_services_key>.[].evpn_l2_multicast.enabled`.<br>When evpn_l2_multicast.enabled is set to true for a vlan or a tenant, "igmp snooping" and "igmp snooping querier" will always be enabled, overriding those individual settings.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].evpn_l2_multicast.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_l3_multicast</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].evpn_l3_multicast") | Dictionary |  |  |  | Explicitly enable or disable evpn_l3_multicast to override setting of `<network_services_key>.[].evpn_l3_multicast.enabled` and `<network_services_key>.[].vrfs.[].evpn_l3_multicast.enabled`.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].evpn_l3_multicast.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;igmp_snooping_enabled</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].igmp_snooping_enabled") | Boolean |  |  |  | Enable IGMP Snooping (Enabled by default on EOS). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;igmp_snooping_querier</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].igmp_snooping_querier") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].igmp_snooping_querier.enabled") | Boolean |  |  |  | Will be enabled automatically if evpn_l2_multicast is enabled. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_address</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].igmp_snooping_querier.source_address") | String |  |  |  | IPv4_address<br>If not set, IP address of "Loopback0" will be used.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;version</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].igmp_snooping_querier.version") | Integer |  |  | Valid Values:<br>- 1<br>- 2<br>- 3 | IGMP Version (By default EOS uses IGMP version 2 for IGMP querier). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_l2_multicast</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].evpn_l2_multicast") | Dictionary |  |  |  | Explicitly enable or disable evpn_l2_multicast to override setting of `<network_services_key>.[].evpn_l2_multicast.enabled`.<br>When evpn_l2_multicast.enabled is set to true for a vlan or a tenant, "igmp snooping" and "igmp snooping querier" will always be enabled, overriding those individual settings.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].evpn_l2_multicast.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_l3_multicast</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].evpn_l3_multicast") | Dictionary |  |  |  | Explicitly enable or disable evpn_l3_multicast to override setting of `<network_services_key>.[].evpn_l3_multicast.enabled` and `<network_services_key>.[].vrfs.[].evpn_l3_multicast.enabled`.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].evpn_l3_multicast.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;igmp_snooping_enabled</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].igmp_snooping_enabled") | Boolean |  |  |  | Enable IGMP Snooping (Enabled by default on EOS). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;igmp_snooping_querier</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].igmp_snooping_querier") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].igmp_snooping_querier.enabled") | Boolean |  |  |  | Will be enabled automatically if evpn_l2_multicast is enabled. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_address</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].igmp_snooping_querier.source_address") | String |  |  |  | IPv4_address<br>If not set, IP address of "Loopback0" will be used.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;version</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].igmp_snooping_querier.version") | Integer |  |  | Valid Values:<br>- 1<br>- 2<br>- 3 | IGMP Version (By default EOS uses IGMP version 2 for IGMP querier). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;l2vlans</samp>](## "&lt;network_services_keys.name&gt;.[].l2vlans") | List, items: Dictionary |  |  |  | Define L2 network services organized by vlan id. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- id</samp>](## "&lt;network_services_keys.name&gt;.[].l2vlans.[].id") | Integer | Required, Unique |  | Min: 1<br>Max: 4094 | VLAN ID |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_l2_multicast</samp>](## "&lt;network_services_keys.name&gt;.[].l2vlans.[].evpn_l2_multicast") | Dictionary |  |  |  | Explicitly enable or disable evpn_l2_multicast to override setting of `<network_services_key>.[].evpn_l2_multicast.enabled`.<br>When evpn_l2_multicast.enabled is set to true for a vlan or a tenant, igmp snooping and igmp snooping querier will always be enabled, overriding those individual settings.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;network_services_keys.name&gt;.[].l2vlans.[].evpn_l2_multicast.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;igmp_snooping_enabled</samp>](## "&lt;network_services_keys.name&gt;.[].l2vlans.[].igmp_snooping_enabled") | Boolean |  | `True` |  | Activate or deactivate IGMP snooping. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;igmp_snooping_querier</samp>](## "&lt;network_services_keys.name&gt;.[].l2vlans.[].igmp_snooping_querier") | Dictionary |  |  |  | Enable igmp snooping querier, by default using IP address of Loopback 0.<br>When enabled, igmp snooping querier will only be configured on l3 devices, i.e., uplink_type: p2p.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;network_services_keys.name&gt;.[].l2vlans.[].igmp_snooping_querier.enabled") | Boolean |  |  |  | Will be enabled automatically if evpn_l2_multicast is enabled. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_address</samp>](## "&lt;network_services_keys.name&gt;.[].l2vlans.[].igmp_snooping_querier.source_address") | String |  |  |  | IPv4_address<br>If not set, IP address of "Loopback0" will be used.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;version</samp>](## "&lt;network_services_keys.name&gt;.[].l2vlans.[].igmp_snooping_querier.version") | Integer |  | `2` | Valid Values:<br>- 1<br>- 2<br>- 3 |  |

=== "YAML"

    ```yaml
    svi_profiles:
      - profile: <str>
        nodes:
          - node: <str>
            evpn_l2_multicast:
              enabled: <bool>
            evpn_l3_multicast:
              enabled: <bool>
            igmp_snooping_enabled: <bool>
            igmp_snooping_querier:
              enabled: <bool>
              source_address: <str>
              version: <int>
        evpn_l2_multicast:
          enabled: <bool>
        evpn_l3_multicast:
          enabled: <bool>
        igmp_snooping_enabled: <bool>
        igmp_snooping_querier:
          enabled: <bool>
          source_address: <str>
          version: <int>
    <network_services_keys.name>:
      - name: <str>
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
        vrfs:
          - name: <str>
            evpn_l3_multicast:
              enabled: <bool>
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
            evpn_l2_multi_domain: <bool>
            svis:
              - id: <int>
                nodes:
                  - node: <str>
                    evpn_l2_multicast:
                      enabled: <bool>
                    evpn_l3_multicast:
                      enabled: <bool>
                    igmp_snooping_enabled: <bool>
                    igmp_snooping_querier:
                      enabled: <bool>
                      source_address: <str>
                      version: <int>
                evpn_l2_multicast:
                  enabled: <bool>
                evpn_l3_multicast:
                  enabled: <bool>
                igmp_snooping_enabled: <bool>
                igmp_snooping_querier:
                  enabled: <bool>
                  source_address: <str>
                  version: <int>
        l2vlans:
          - id: <int>
            evpn_l2_multicast:
              enabled: <bool>
            igmp_snooping_enabled: <bool>
            igmp_snooping_querier:
              enabled: <bool>
              source_address: <str>
              version: <int>
    ```
