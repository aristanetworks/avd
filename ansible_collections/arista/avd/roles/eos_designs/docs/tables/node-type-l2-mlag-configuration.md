<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>&lt;node_type_keys.key&gt;</samp>](## "<node_type_keys.key>") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;defaults</samp>](## "<node_type_keys.key>.defaults") | Dictionary |  |  |  | Define variables for all nodes of this type. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mlag_port_channel_structured_config</samp>](## "<node_type_keys.key>.defaults.mlag_port_channel_structured_config") | Dictionary |  |  |  | Custom structured config applied to MLAG peer link port-channel id.<br>Added under port_channel_interfaces.[name=<interface>] for eos_cli_config_gen.<br>Overrides the settings on the port-channel interface level.<br>"mlag_port_channel_structured_config" is applied after "structured_config", so it can override "structured_config" defined on node-level.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mlag_peer_vlan_structured_config</samp>](## "<node_type_keys.key>.defaults.mlag_peer_vlan_structured_config") | Dictionary |  |  |  | Custom structured config applied to MLAG Peer Link (control link) SVI interface id.<br>Added under vlan_interfaces.[name=<interface>] for eos_cli_config_gen.<br>Overrides the settings on the vlan interface level.<br>"mlag_peer_vlan_structured_config" is applied after "structured_config", so it can override "structured_config" defined on node-level.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mlag_peer_l3_vlan_structured_config</samp>](## "<node_type_keys.key>.defaults.mlag_peer_l3_vlan_structured_config") | Dictionary |  |  |  | Custom structured config applied to MLAG underlay L3 peering SVI interface id.<br>Added under vlan_interfaces.[name=<interface>] for eos_cli_config_gen.<br>Overrides the settings on the vlan interface level.<br>"mlag_peer_l3_vlan_structured_config" is applied after "structured_config", so it can override "structured_config" defined on node-level.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mlag</samp>](## "<node_type_keys.key>.defaults.mlag") | Boolean |  | `True` |  | Enable / Disable auto MLAG, when two nodes are defined in node group. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mlag_dual_primary_detection</samp>](## "<node_type_keys.key>.defaults.mlag_dual_primary_detection") | Boolean |  | `False` |  | Enable / Disable MLAG dual primary detection. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mlag_ibgp_origin_incomplete</samp>](## "<node_type_keys.key>.defaults.mlag_ibgp_origin_incomplete") | Boolean |  | `True` |  | Set origin of routes received from MLAG iBGP peer to incomplete.<br>The purpose is to optimize routing for leaf loopbacks from spine perspective and<br>avoid suboptimal routing via peerlink for control plane traffic.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mlag_interfaces</samp>](## "<node_type_keys.key>.defaults.mlag_interfaces") | List, items: String |  |  |  | Each list item supports range syntax that can be expanded into a list of interfaces.<br>Required when MLAG leafs are present in the topology.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "<node_type_keys.key>.defaults.mlag_interfaces.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mlag_interfaces_speed</samp>](## "<node_type_keys.key>.defaults.mlag_interfaces_speed") | String |  |  | Valid Values:<br>- <code>100full</code><br>- <code>100g</code><br>- <code>100g-1</code><br>- <code>100g-2</code><br>- <code>100g-4</code><br>- <code>100half</code><br>- <code>10full</code><br>- <code>10g</code><br>- <code>10half</code><br>- <code>1g</code><br>- <code>200g</code><br>- <code>200g-2</code><br>- <code>200g-4</code><br>- <code>25g</code><br>- <code>400g</code><br>- <code>400g-4</code><br>- <code>400g-8</code><br>- <code>40g</code><br>- <code>50g</code><br>- <code>50g-1</code><br>- <code>50g-2</code><br>- <code>800g-8</code><br>- <code>sfp-1000baset auto 100full</code><br>- <code>1.6t-8</code><br>- <code>100mfull</code><br>- <code>100mhalf</code><br>- <code>10mfull</code><br>- <code>10mhalf</code><br>- <code>200g-1</code><br>- <code>400g-2</code><br>- <code>40g-4</code><br>- <code>800g-4</code><br>- <code>auto</code><br>- <code>auto 10000full</code><br>- <code>auto 1000full</code><br>- <code>auto 100full</code><br>- <code>auto 100g-1</code><br>- <code>auto 100g-2</code><br>- <code>auto 100g-4</code><br>- <code>auto 100gfull</code><br>- <code>auto 100half</code><br>- <code>auto 10full</code><br>- <code>auto 10gfull</code><br>- <code>auto 10half</code><br>- <code>auto 1gfull</code><br>- <code>auto 2.5gfull</code><br>- <code>auto 200g-2</code><br>- <code>auto 200g-4</code><br>- <code>auto 25gfull</code><br>- <code>auto 400g-4</code><br>- <code>auto 400g-8</code><br>- <code>auto 40gfull</code><br>- <code>auto 50g-1</code><br>- <code>auto 50g-2</code><br>- <code>auto 50gfull</code><br>- <code>auto 5gfull</code><br>- <code>auto 800g-8</code><br>- <code>auto 1.6t-8</code><br>- <code>auto 100mfull</code><br>- <code>auto 100mhalf</code><br>- <code>auto 10g</code><br>- <code>auto 10mfull</code><br>- <code>auto 10mhalf</code><br>- <code>auto 1g</code><br>- <code>auto 2.5g</code><br>- <code>auto 200g-1</code><br>- <code>auto 25g</code><br>- <code>auto 400g-2</code><br>- <code>auto 40g-4</code><br>- <code>auto 5g</code><br>- <code>auto 800g-4</code><br>- <code>forced 10000full</code><br>- <code>forced 1000full</code><br>- <code>forced 1000half</code><br>- <code>forced 100full</code><br>- <code>forced 100gfull</code><br>- <code>forced 100half</code><br>- <code>forced 10full</code><br>- <code>forced 10half</code><br>- <code>forced 25gfull</code><br>- <code>forced 40gfull</code><br>- <code>forced 50gfull</code> | Set MLAG interface speed.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mlag_peer_l3_vlan</samp>](## "<node_type_keys.key>.defaults.mlag_peer_l3_vlan") | Integer |  | `4093` | Min: 0<br>Max: 4094 | Underlay L3 peering SVI interface id.<br>If set to 0 or the same vlan as mlag_peer_vlan, the mlag_peer_vlan will be used for L3 peering.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mlag_peer_l3_ipv4_pool</samp>](## "<node_type_keys.key>.defaults.mlag_peer_l3_ipv4_pool") | String |  |  | Format: ipv4_pool | Comma separated list of prefixes (IPv4 address/Mask) or ranges (IPv4_address-IPv4_address).<br>The IPv4 subnet used for MLAG underlay L3 peering is derived from this pool based on the node id of the first MLAG switch.<br>Required when MLAG leafs present in topology and they are using a separate L3 peering VLAN.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mlag_peer_l3_ipv6_pool</samp>](## "<node_type_keys.key>.defaults.mlag_peer_l3_ipv6_pool") | String |  |  | Format: ipv6_pool | Comma separated list of prefixes (IPv6 address/Mask) or ranges (IPv6_address-IPv6_address).<br>The IPv6 subnet used for MLAG underlay L3 peering is derived from this pool based on the node id of the first MLAG switch.<br>Required when MLAG leafs present in topology and they are using a separate L3 peering VLAN.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mlag_peer_vlan</samp>](## "<node_type_keys.key>.defaults.mlag_peer_vlan") | Integer |  | `4094` | Min: 1<br>Max: 4094 | MLAG Peer Link (control link) SVI interface id. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mlag_peer_link_allowed_vlans</samp>](## "<node_type_keys.key>.defaults.mlag_peer_link_allowed_vlans") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mlag_peer_address_family</samp>](## "<node_type_keys.key>.defaults.mlag_peer_address_family") | String |  | `ipv4` | Valid Values:<br>- <code>ipv4</code><br>- <code>ipv6</code> | IP address family used to establish MLAG Peer Link (control link).<br>`ipv6` requires EOS version 4.31.1F or higher.<br>Note: `ipv6` is not supported in combination with a common MLAG peer link VLAN (ex. `mlag_peer_l3_vlan` set to 4094). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mlag_peer_ipv4_pool</samp>](## "<node_type_keys.key>.defaults.mlag_peer_ipv4_pool") | String |  |  | Format: ipv4_pool | Comma separated list of prefixes (IPv4 address/Mask) or ranges (IPv4_address-IPv4_address).<br>The IPv4 address used for MLAG Peer Link (control link) is derived from this pool based on the node id of the first MLAG switch.<br>Required for MLAG leafs when `mlag_peer_address_family` is `ipv4` (default). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mlag_peer_ipv6_pool</samp>](## "<node_type_keys.key>.defaults.mlag_peer_ipv6_pool") | String |  |  | Format: ipv6_pool | Comma separated list of prefixes (IPv6 address/Mask) or ranges (IPv6_address-IPv6_address).<br>The IPv6 address used for MLAG Peer Link (control link) is derived from this pool based on the node id of the first MLAG switch.<br>Required for MLAG leafs when `mlag_peer_address_family` is `ipv6`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mlag_port_channel_id</samp>](## "<node_type_keys.key>.defaults.mlag_port_channel_id") | Integer |  |  |  | If not set, the mlag port-channel id is generated based on the digits of the first interface present in 'mlag_interfaces'.<br>Valid port-channel id numbers are < 1-2000 > for EOS < 4.25.0F and < 1 - 999999 > for EOS >= 4.25.0F.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mlag_domain_id</samp>](## "<node_type_keys.key>.defaults.mlag_domain_id") | String |  |  |  | MLAG Domain ID. If not set the node group name (Set with "group" key) will be used. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_mode</samp>](## "<node_type_keys.key>.defaults.spanning_tree_mode") | String |  |  | Valid Values:<br>- <code>mstp</code><br>- <code>rstp</code><br>- <code>rapid-pvst</code><br>- <code>none</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_priority</samp>](## "<node_type_keys.key>.defaults.spanning_tree_priority") | Integer |  | `32768` |  | Spanning-tree priority configured for the selected mode.<br>For `rapid-pvst` the priority can also be set per VLAN under network services. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_root_super</samp>](## "<node_type_keys.key>.defaults.spanning_tree_root_super") | Boolean |  | `False` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_mst_pvst_boundary</samp>](## "<node_type_keys.key>.defaults.spanning_tree_mst_pvst_boundary") | Boolean |  |  |  | Enable MST PVST border ports. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_port_id_allocation_port_channel_range</samp>](## "<node_type_keys.key>.defaults.spanning_tree_port_id_allocation_port_channel_range") | Dictionary |  |  |  | Specify range of port-ids to reserve for port-channels. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;minimum</samp>](## "<node_type_keys.key>.defaults.spanning_tree_port_id_allocation_port_channel_range.minimum") | Integer | Required |  | Min: 1<br>Max: 2048 | Specify minimum value for reserved range. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maximum</samp>](## "<node_type_keys.key>.defaults.spanning_tree_port_id_allocation_port_channel_range.maximum") | Integer | Required |  | Min: 1<br>Max: 2048 | Specify maximum value for reserved range. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;virtual_router_mac_address</samp>](## "<node_type_keys.key>.defaults.virtual_router_mac_address") | String |  |  | Format: mac | Virtual router mac address for anycast gateway. |
    | [<samp>&nbsp;&nbsp;node_groups</samp>](## "<node_type_keys.key>.node_groups") | List, items: Dictionary |  |  |  | Define variables related to all nodes part of this group. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;group</samp>](## "<node_type_keys.key>.node_groups.[].group") | String | Required, Unique |  |  | The Node Group Name is used for MLAG domain unless set with 'mlag_domain_id'.<br>The Node Group Name is also used for peer description on downstream switches' uplinks.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "<node_type_keys.key>.node_groups.[].nodes") | List, items: Dictionary |  |  |  | Define variables per node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].name") | String | Required, Unique |  |  | The Node Name is used as "hostname". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_port_channel_structured_config</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].mlag_port_channel_structured_config") | Dictionary |  |  |  | Custom structured config applied to MLAG peer link port-channel id.<br>Added under port_channel_interfaces.[name=<interface>] for eos_cli_config_gen.<br>Overrides the settings on the port-channel interface level.<br>"mlag_port_channel_structured_config" is applied after "structured_config", so it can override "structured_config" defined on node-level.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_peer_vlan_structured_config</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].mlag_peer_vlan_structured_config") | Dictionary |  |  |  | Custom structured config applied to MLAG Peer Link (control link) SVI interface id.<br>Added under vlan_interfaces.[name=<interface>] for eos_cli_config_gen.<br>Overrides the settings on the vlan interface level.<br>"mlag_peer_vlan_structured_config" is applied after "structured_config", so it can override "structured_config" defined on node-level.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_peer_l3_vlan_structured_config</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].mlag_peer_l3_vlan_structured_config") | Dictionary |  |  |  | Custom structured config applied to MLAG underlay L3 peering SVI interface id.<br>Added under vlan_interfaces.[name=<interface>] for eos_cli_config_gen.<br>Overrides the settings on the vlan interface level.<br>"mlag_peer_l3_vlan_structured_config" is applied after "structured_config", so it can override "structured_config" defined on node-level.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].mlag") | Boolean |  | `True` |  | Enable / Disable auto MLAG, when two nodes are defined in node group. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_dual_primary_detection</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].mlag_dual_primary_detection") | Boolean |  | `False` |  | Enable / Disable MLAG dual primary detection. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_ibgp_origin_incomplete</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].mlag_ibgp_origin_incomplete") | Boolean |  | `True` |  | Set origin of routes received from MLAG iBGP peer to incomplete.<br>The purpose is to optimize routing for leaf loopbacks from spine perspective and<br>avoid suboptimal routing via peerlink for control plane traffic.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_interfaces</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].mlag_interfaces") | List, items: String |  |  |  | Each list item supports range syntax that can be expanded into a list of interfaces.<br>Required when MLAG leafs are present in the topology.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].mlag_interfaces.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_interfaces_speed</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].mlag_interfaces_speed") | String |  |  | Valid Values:<br>- <code>100full</code><br>- <code>100g</code><br>- <code>100g-1</code><br>- <code>100g-2</code><br>- <code>100g-4</code><br>- <code>100half</code><br>- <code>10full</code><br>- <code>10g</code><br>- <code>10half</code><br>- <code>1g</code><br>- <code>200g</code><br>- <code>200g-2</code><br>- <code>200g-4</code><br>- <code>25g</code><br>- <code>400g</code><br>- <code>400g-4</code><br>- <code>400g-8</code><br>- <code>40g</code><br>- <code>50g</code><br>- <code>50g-1</code><br>- <code>50g-2</code><br>- <code>800g-8</code><br>- <code>sfp-1000baset auto 100full</code><br>- <code>1.6t-8</code><br>- <code>100mfull</code><br>- <code>100mhalf</code><br>- <code>10mfull</code><br>- <code>10mhalf</code><br>- <code>200g-1</code><br>- <code>400g-2</code><br>- <code>40g-4</code><br>- <code>800g-4</code><br>- <code>auto</code><br>- <code>auto 10000full</code><br>- <code>auto 1000full</code><br>- <code>auto 100full</code><br>- <code>auto 100g-1</code><br>- <code>auto 100g-2</code><br>- <code>auto 100g-4</code><br>- <code>auto 100gfull</code><br>- <code>auto 100half</code><br>- <code>auto 10full</code><br>- <code>auto 10gfull</code><br>- <code>auto 10half</code><br>- <code>auto 1gfull</code><br>- <code>auto 2.5gfull</code><br>- <code>auto 200g-2</code><br>- <code>auto 200g-4</code><br>- <code>auto 25gfull</code><br>- <code>auto 400g-4</code><br>- <code>auto 400g-8</code><br>- <code>auto 40gfull</code><br>- <code>auto 50g-1</code><br>- <code>auto 50g-2</code><br>- <code>auto 50gfull</code><br>- <code>auto 5gfull</code><br>- <code>auto 800g-8</code><br>- <code>auto 1.6t-8</code><br>- <code>auto 100mfull</code><br>- <code>auto 100mhalf</code><br>- <code>auto 10g</code><br>- <code>auto 10mfull</code><br>- <code>auto 10mhalf</code><br>- <code>auto 1g</code><br>- <code>auto 2.5g</code><br>- <code>auto 200g-1</code><br>- <code>auto 25g</code><br>- <code>auto 400g-2</code><br>- <code>auto 40g-4</code><br>- <code>auto 5g</code><br>- <code>auto 800g-4</code><br>- <code>forced 10000full</code><br>- <code>forced 1000full</code><br>- <code>forced 1000half</code><br>- <code>forced 100full</code><br>- <code>forced 100gfull</code><br>- <code>forced 100half</code><br>- <code>forced 10full</code><br>- <code>forced 10half</code><br>- <code>forced 25gfull</code><br>- <code>forced 40gfull</code><br>- <code>forced 50gfull</code> | Set MLAG interface speed.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_peer_l3_vlan</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].mlag_peer_l3_vlan") | Integer |  | `4093` | Min: 0<br>Max: 4094 | Underlay L3 peering SVI interface id.<br>If set to 0 or the same vlan as mlag_peer_vlan, the mlag_peer_vlan will be used for L3 peering.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_peer_l3_ipv4_pool</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].mlag_peer_l3_ipv4_pool") | String |  |  | Format: ipv4_pool | Comma separated list of prefixes (IPv4 address/Mask) or ranges (IPv4_address-IPv4_address).<br>The IPv4 subnet used for MLAG underlay L3 peering is derived from this pool based on the node id of the first MLAG switch.<br>Required when MLAG leafs present in topology and they are using a separate L3 peering VLAN.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_peer_l3_ipv6_pool</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].mlag_peer_l3_ipv6_pool") | String |  |  | Format: ipv6_pool | Comma separated list of prefixes (IPv6 address/Mask) or ranges (IPv6_address-IPv6_address).<br>The IPv6 subnet used for MLAG underlay L3 peering is derived from this pool based on the node id of the first MLAG switch.<br>Required when MLAG leafs present in topology and they are using a separate L3 peering VLAN.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_peer_vlan</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].mlag_peer_vlan") | Integer |  | `4094` | Min: 1<br>Max: 4094 | MLAG Peer Link (control link) SVI interface id. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_peer_link_allowed_vlans</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].mlag_peer_link_allowed_vlans") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_peer_address_family</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].mlag_peer_address_family") | String |  | `ipv4` | Valid Values:<br>- <code>ipv4</code><br>- <code>ipv6</code> | IP address family used to establish MLAG Peer Link (control link).<br>`ipv6` requires EOS version 4.31.1F or higher.<br>Note: `ipv6` is not supported in combination with a common MLAG peer link VLAN (ex. `mlag_peer_l3_vlan` set to 4094). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_peer_ipv4_pool</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].mlag_peer_ipv4_pool") | String |  |  | Format: ipv4_pool | Comma separated list of prefixes (IPv4 address/Mask) or ranges (IPv4_address-IPv4_address).<br>The IPv4 address used for MLAG Peer Link (control link) is derived from this pool based on the node id of the first MLAG switch.<br>Required for MLAG leafs when `mlag_peer_address_family` is `ipv4` (default). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_peer_ipv6_pool</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].mlag_peer_ipv6_pool") | String |  |  | Format: ipv6_pool | Comma separated list of prefixes (IPv6 address/Mask) or ranges (IPv6_address-IPv6_address).<br>The IPv6 address used for MLAG Peer Link (control link) is derived from this pool based on the node id of the first MLAG switch.<br>Required for MLAG leafs when `mlag_peer_address_family` is `ipv6`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_port_channel_id</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].mlag_port_channel_id") | Integer |  |  |  | If not set, the mlag port-channel id is generated based on the digits of the first interface present in 'mlag_interfaces'.<br>Valid port-channel id numbers are < 1-2000 > for EOS < 4.25.0F and < 1 - 999999 > for EOS >= 4.25.0F.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_domain_id</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].mlag_domain_id") | String |  |  |  | MLAG Domain ID. If not set the node group name (Set with "group" key) will be used. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_mode</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].spanning_tree_mode") | String |  |  | Valid Values:<br>- <code>mstp</code><br>- <code>rstp</code><br>- <code>rapid-pvst</code><br>- <code>none</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_priority</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].spanning_tree_priority") | Integer |  | `32768` |  | Spanning-tree priority configured for the selected mode.<br>For `rapid-pvst` the priority can also be set per VLAN under network services. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_root_super</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].spanning_tree_root_super") | Boolean |  | `False` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_mst_pvst_boundary</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].spanning_tree_mst_pvst_boundary") | Boolean |  |  |  | Enable MST PVST border ports. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_port_id_allocation_port_channel_range</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].spanning_tree_port_id_allocation_port_channel_range") | Dictionary |  |  |  | Specify range of port-ids to reserve for port-channels. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;minimum</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].spanning_tree_port_id_allocation_port_channel_range.minimum") | Integer | Required |  | Min: 1<br>Max: 2048 | Specify minimum value for reserved range. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maximum</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].spanning_tree_port_id_allocation_port_channel_range.maximum") | Integer | Required |  | Min: 1<br>Max: 2048 | Specify maximum value for reserved range. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;virtual_router_mac_address</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].virtual_router_mac_address") | String |  |  | Format: mac | Virtual router mac address for anycast gateway. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_port_channel_structured_config</samp>](## "<node_type_keys.key>.node_groups.[].mlag_port_channel_structured_config") | Dictionary |  |  |  | Custom structured config applied to MLAG peer link port-channel id.<br>Added under port_channel_interfaces.[name=<interface>] for eos_cli_config_gen.<br>Overrides the settings on the port-channel interface level.<br>"mlag_port_channel_structured_config" is applied after "structured_config", so it can override "structured_config" defined on node-level.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_peer_vlan_structured_config</samp>](## "<node_type_keys.key>.node_groups.[].mlag_peer_vlan_structured_config") | Dictionary |  |  |  | Custom structured config applied to MLAG Peer Link (control link) SVI interface id.<br>Added under vlan_interfaces.[name=<interface>] for eos_cli_config_gen.<br>Overrides the settings on the vlan interface level.<br>"mlag_peer_vlan_structured_config" is applied after "structured_config", so it can override "structured_config" defined on node-level.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_peer_l3_vlan_structured_config</samp>](## "<node_type_keys.key>.node_groups.[].mlag_peer_l3_vlan_structured_config") | Dictionary |  |  |  | Custom structured config applied to MLAG underlay L3 peering SVI interface id.<br>Added under vlan_interfaces.[name=<interface>] for eos_cli_config_gen.<br>Overrides the settings on the vlan interface level.<br>"mlag_peer_l3_vlan_structured_config" is applied after "structured_config", so it can override "structured_config" defined on node-level.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag</samp>](## "<node_type_keys.key>.node_groups.[].mlag") | Boolean |  | `True` |  | Enable / Disable auto MLAG, when two nodes are defined in node group. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_dual_primary_detection</samp>](## "<node_type_keys.key>.node_groups.[].mlag_dual_primary_detection") | Boolean |  | `False` |  | Enable / Disable MLAG dual primary detection. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_ibgp_origin_incomplete</samp>](## "<node_type_keys.key>.node_groups.[].mlag_ibgp_origin_incomplete") | Boolean |  | `True` |  | Set origin of routes received from MLAG iBGP peer to incomplete.<br>The purpose is to optimize routing for leaf loopbacks from spine perspective and<br>avoid suboptimal routing via peerlink for control plane traffic.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_interfaces</samp>](## "<node_type_keys.key>.node_groups.[].mlag_interfaces") | List, items: String |  |  |  | Each list item supports range syntax that can be expanded into a list of interfaces.<br>Required when MLAG leafs are present in the topology.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "<node_type_keys.key>.node_groups.[].mlag_interfaces.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_interfaces_speed</samp>](## "<node_type_keys.key>.node_groups.[].mlag_interfaces_speed") | String |  |  | Valid Values:<br>- <code>100full</code><br>- <code>100g</code><br>- <code>100g-1</code><br>- <code>100g-2</code><br>- <code>100g-4</code><br>- <code>100half</code><br>- <code>10full</code><br>- <code>10g</code><br>- <code>10half</code><br>- <code>1g</code><br>- <code>200g</code><br>- <code>200g-2</code><br>- <code>200g-4</code><br>- <code>25g</code><br>- <code>400g</code><br>- <code>400g-4</code><br>- <code>400g-8</code><br>- <code>40g</code><br>- <code>50g</code><br>- <code>50g-1</code><br>- <code>50g-2</code><br>- <code>800g-8</code><br>- <code>sfp-1000baset auto 100full</code><br>- <code>1.6t-8</code><br>- <code>100mfull</code><br>- <code>100mhalf</code><br>- <code>10mfull</code><br>- <code>10mhalf</code><br>- <code>200g-1</code><br>- <code>400g-2</code><br>- <code>40g-4</code><br>- <code>800g-4</code><br>- <code>auto</code><br>- <code>auto 10000full</code><br>- <code>auto 1000full</code><br>- <code>auto 100full</code><br>- <code>auto 100g-1</code><br>- <code>auto 100g-2</code><br>- <code>auto 100g-4</code><br>- <code>auto 100gfull</code><br>- <code>auto 100half</code><br>- <code>auto 10full</code><br>- <code>auto 10gfull</code><br>- <code>auto 10half</code><br>- <code>auto 1gfull</code><br>- <code>auto 2.5gfull</code><br>- <code>auto 200g-2</code><br>- <code>auto 200g-4</code><br>- <code>auto 25gfull</code><br>- <code>auto 400g-4</code><br>- <code>auto 400g-8</code><br>- <code>auto 40gfull</code><br>- <code>auto 50g-1</code><br>- <code>auto 50g-2</code><br>- <code>auto 50gfull</code><br>- <code>auto 5gfull</code><br>- <code>auto 800g-8</code><br>- <code>auto 1.6t-8</code><br>- <code>auto 100mfull</code><br>- <code>auto 100mhalf</code><br>- <code>auto 10g</code><br>- <code>auto 10mfull</code><br>- <code>auto 10mhalf</code><br>- <code>auto 1g</code><br>- <code>auto 2.5g</code><br>- <code>auto 200g-1</code><br>- <code>auto 25g</code><br>- <code>auto 400g-2</code><br>- <code>auto 40g-4</code><br>- <code>auto 5g</code><br>- <code>auto 800g-4</code><br>- <code>forced 10000full</code><br>- <code>forced 1000full</code><br>- <code>forced 1000half</code><br>- <code>forced 100full</code><br>- <code>forced 100gfull</code><br>- <code>forced 100half</code><br>- <code>forced 10full</code><br>- <code>forced 10half</code><br>- <code>forced 25gfull</code><br>- <code>forced 40gfull</code><br>- <code>forced 50gfull</code> | Set MLAG interface speed.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_peer_l3_vlan</samp>](## "<node_type_keys.key>.node_groups.[].mlag_peer_l3_vlan") | Integer |  | `4093` | Min: 0<br>Max: 4094 | Underlay L3 peering SVI interface id.<br>If set to 0 or the same vlan as mlag_peer_vlan, the mlag_peer_vlan will be used for L3 peering.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_peer_l3_ipv4_pool</samp>](## "<node_type_keys.key>.node_groups.[].mlag_peer_l3_ipv4_pool") | String |  |  | Format: ipv4_pool | Comma separated list of prefixes (IPv4 address/Mask) or ranges (IPv4_address-IPv4_address).<br>The IPv4 subnet used for MLAG underlay L3 peering is derived from this pool based on the node id of the first MLAG switch.<br>Required when MLAG leafs present in topology and they are using a separate L3 peering VLAN.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_peer_l3_ipv6_pool</samp>](## "<node_type_keys.key>.node_groups.[].mlag_peer_l3_ipv6_pool") | String |  |  | Format: ipv6_pool | Comma separated list of prefixes (IPv6 address/Mask) or ranges (IPv6_address-IPv6_address).<br>The IPv6 subnet used for MLAG underlay L3 peering is derived from this pool based on the node id of the first MLAG switch.<br>Required when MLAG leafs present in topology and they are using a separate L3 peering VLAN.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_peer_vlan</samp>](## "<node_type_keys.key>.node_groups.[].mlag_peer_vlan") | Integer |  | `4094` | Min: 1<br>Max: 4094 | MLAG Peer Link (control link) SVI interface id. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_peer_link_allowed_vlans</samp>](## "<node_type_keys.key>.node_groups.[].mlag_peer_link_allowed_vlans") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_peer_address_family</samp>](## "<node_type_keys.key>.node_groups.[].mlag_peer_address_family") | String |  | `ipv4` | Valid Values:<br>- <code>ipv4</code><br>- <code>ipv6</code> | IP address family used to establish MLAG Peer Link (control link).<br>`ipv6` requires EOS version 4.31.1F or higher.<br>Note: `ipv6` is not supported in combination with a common MLAG peer link VLAN (ex. `mlag_peer_l3_vlan` set to 4094). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_peer_ipv4_pool</samp>](## "<node_type_keys.key>.node_groups.[].mlag_peer_ipv4_pool") | String |  |  | Format: ipv4_pool | Comma separated list of prefixes (IPv4 address/Mask) or ranges (IPv4_address-IPv4_address).<br>The IPv4 address used for MLAG Peer Link (control link) is derived from this pool based on the node id of the first MLAG switch.<br>Required for MLAG leafs when `mlag_peer_address_family` is `ipv4` (default). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_peer_ipv6_pool</samp>](## "<node_type_keys.key>.node_groups.[].mlag_peer_ipv6_pool") | String |  |  | Format: ipv6_pool | Comma separated list of prefixes (IPv6 address/Mask) or ranges (IPv6_address-IPv6_address).<br>The IPv6 address used for MLAG Peer Link (control link) is derived from this pool based on the node id of the first MLAG switch.<br>Required for MLAG leafs when `mlag_peer_address_family` is `ipv6`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_port_channel_id</samp>](## "<node_type_keys.key>.node_groups.[].mlag_port_channel_id") | Integer |  |  |  | If not set, the mlag port-channel id is generated based on the digits of the first interface present in 'mlag_interfaces'.<br>Valid port-channel id numbers are < 1-2000 > for EOS < 4.25.0F and < 1 - 999999 > for EOS >= 4.25.0F.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_domain_id</samp>](## "<node_type_keys.key>.node_groups.[].mlag_domain_id") | String |  |  |  | MLAG Domain ID. If not set the node group name (Set with "group" key) will be used. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_mode</samp>](## "<node_type_keys.key>.node_groups.[].spanning_tree_mode") | String |  |  | Valid Values:<br>- <code>mstp</code><br>- <code>rstp</code><br>- <code>rapid-pvst</code><br>- <code>none</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_priority</samp>](## "<node_type_keys.key>.node_groups.[].spanning_tree_priority") | Integer |  | `32768` |  | Spanning-tree priority configured for the selected mode.<br>For `rapid-pvst` the priority can also be set per VLAN under network services. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_root_super</samp>](## "<node_type_keys.key>.node_groups.[].spanning_tree_root_super") | Boolean |  | `False` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_mst_pvst_boundary</samp>](## "<node_type_keys.key>.node_groups.[].spanning_tree_mst_pvst_boundary") | Boolean |  |  |  | Enable MST PVST border ports. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_port_id_allocation_port_channel_range</samp>](## "<node_type_keys.key>.node_groups.[].spanning_tree_port_id_allocation_port_channel_range") | Dictionary |  |  |  | Specify range of port-ids to reserve for port-channels. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;minimum</samp>](## "<node_type_keys.key>.node_groups.[].spanning_tree_port_id_allocation_port_channel_range.minimum") | Integer | Required |  | Min: 1<br>Max: 2048 | Specify minimum value for reserved range. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maximum</samp>](## "<node_type_keys.key>.node_groups.[].spanning_tree_port_id_allocation_port_channel_range.maximum") | Integer | Required |  | Min: 1<br>Max: 2048 | Specify maximum value for reserved range. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;virtual_router_mac_address</samp>](## "<node_type_keys.key>.node_groups.[].virtual_router_mac_address") | String |  |  | Format: mac | Virtual router mac address for anycast gateway. |
    | [<samp>&nbsp;&nbsp;nodes</samp>](## "<node_type_keys.key>.nodes") | List, items: Dictionary |  |  |  | Define variables per node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "<node_type_keys.key>.nodes.[].name") | String | Required, Unique |  |  | The Node Name is used as "hostname". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_port_channel_structured_config</samp>](## "<node_type_keys.key>.nodes.[].mlag_port_channel_structured_config") | Dictionary |  |  |  | Custom structured config applied to MLAG peer link port-channel id.<br>Added under port_channel_interfaces.[name=<interface>] for eos_cli_config_gen.<br>Overrides the settings on the port-channel interface level.<br>"mlag_port_channel_structured_config" is applied after "structured_config", so it can override "structured_config" defined on node-level.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_peer_vlan_structured_config</samp>](## "<node_type_keys.key>.nodes.[].mlag_peer_vlan_structured_config") | Dictionary |  |  |  | Custom structured config applied to MLAG Peer Link (control link) SVI interface id.<br>Added under vlan_interfaces.[name=<interface>] for eos_cli_config_gen.<br>Overrides the settings on the vlan interface level.<br>"mlag_peer_vlan_structured_config" is applied after "structured_config", so it can override "structured_config" defined on node-level.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_peer_l3_vlan_structured_config</samp>](## "<node_type_keys.key>.nodes.[].mlag_peer_l3_vlan_structured_config") | Dictionary |  |  |  | Custom structured config applied to MLAG underlay L3 peering SVI interface id.<br>Added under vlan_interfaces.[name=<interface>] for eos_cli_config_gen.<br>Overrides the settings on the vlan interface level.<br>"mlag_peer_l3_vlan_structured_config" is applied after "structured_config", so it can override "structured_config" defined on node-level.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag</samp>](## "<node_type_keys.key>.nodes.[].mlag") | Boolean |  | `True` |  | Enable / Disable auto MLAG, when two nodes are defined in node group. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_dual_primary_detection</samp>](## "<node_type_keys.key>.nodes.[].mlag_dual_primary_detection") | Boolean |  | `False` |  | Enable / Disable MLAG dual primary detection. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_ibgp_origin_incomplete</samp>](## "<node_type_keys.key>.nodes.[].mlag_ibgp_origin_incomplete") | Boolean |  | `True` |  | Set origin of routes received from MLAG iBGP peer to incomplete.<br>The purpose is to optimize routing for leaf loopbacks from spine perspective and<br>avoid suboptimal routing via peerlink for control plane traffic.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_interfaces</samp>](## "<node_type_keys.key>.nodes.[].mlag_interfaces") | List, items: String |  |  |  | Each list item supports range syntax that can be expanded into a list of interfaces.<br>Required when MLAG leafs are present in the topology.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "<node_type_keys.key>.nodes.[].mlag_interfaces.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_interfaces_speed</samp>](## "<node_type_keys.key>.nodes.[].mlag_interfaces_speed") | String |  |  | Valid Values:<br>- <code>100full</code><br>- <code>100g</code><br>- <code>100g-1</code><br>- <code>100g-2</code><br>- <code>100g-4</code><br>- <code>100half</code><br>- <code>10full</code><br>- <code>10g</code><br>- <code>10half</code><br>- <code>1g</code><br>- <code>200g</code><br>- <code>200g-2</code><br>- <code>200g-4</code><br>- <code>25g</code><br>- <code>400g</code><br>- <code>400g-4</code><br>- <code>400g-8</code><br>- <code>40g</code><br>- <code>50g</code><br>- <code>50g-1</code><br>- <code>50g-2</code><br>- <code>800g-8</code><br>- <code>sfp-1000baset auto 100full</code><br>- <code>1.6t-8</code><br>- <code>100mfull</code><br>- <code>100mhalf</code><br>- <code>10mfull</code><br>- <code>10mhalf</code><br>- <code>200g-1</code><br>- <code>400g-2</code><br>- <code>40g-4</code><br>- <code>800g-4</code><br>- <code>auto</code><br>- <code>auto 10000full</code><br>- <code>auto 1000full</code><br>- <code>auto 100full</code><br>- <code>auto 100g-1</code><br>- <code>auto 100g-2</code><br>- <code>auto 100g-4</code><br>- <code>auto 100gfull</code><br>- <code>auto 100half</code><br>- <code>auto 10full</code><br>- <code>auto 10gfull</code><br>- <code>auto 10half</code><br>- <code>auto 1gfull</code><br>- <code>auto 2.5gfull</code><br>- <code>auto 200g-2</code><br>- <code>auto 200g-4</code><br>- <code>auto 25gfull</code><br>- <code>auto 400g-4</code><br>- <code>auto 400g-8</code><br>- <code>auto 40gfull</code><br>- <code>auto 50g-1</code><br>- <code>auto 50g-2</code><br>- <code>auto 50gfull</code><br>- <code>auto 5gfull</code><br>- <code>auto 800g-8</code><br>- <code>auto 1.6t-8</code><br>- <code>auto 100mfull</code><br>- <code>auto 100mhalf</code><br>- <code>auto 10g</code><br>- <code>auto 10mfull</code><br>- <code>auto 10mhalf</code><br>- <code>auto 1g</code><br>- <code>auto 2.5g</code><br>- <code>auto 200g-1</code><br>- <code>auto 25g</code><br>- <code>auto 400g-2</code><br>- <code>auto 40g-4</code><br>- <code>auto 5g</code><br>- <code>auto 800g-4</code><br>- <code>forced 10000full</code><br>- <code>forced 1000full</code><br>- <code>forced 1000half</code><br>- <code>forced 100full</code><br>- <code>forced 100gfull</code><br>- <code>forced 100half</code><br>- <code>forced 10full</code><br>- <code>forced 10half</code><br>- <code>forced 25gfull</code><br>- <code>forced 40gfull</code><br>- <code>forced 50gfull</code> | Set MLAG interface speed.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_peer_l3_vlan</samp>](## "<node_type_keys.key>.nodes.[].mlag_peer_l3_vlan") | Integer |  | `4093` | Min: 0<br>Max: 4094 | Underlay L3 peering SVI interface id.<br>If set to 0 or the same vlan as mlag_peer_vlan, the mlag_peer_vlan will be used for L3 peering.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_peer_l3_ipv4_pool</samp>](## "<node_type_keys.key>.nodes.[].mlag_peer_l3_ipv4_pool") | String |  |  | Format: ipv4_pool | Comma separated list of prefixes (IPv4 address/Mask) or ranges (IPv4_address-IPv4_address).<br>The IPv4 subnet used for MLAG underlay L3 peering is derived from this pool based on the node id of the first MLAG switch.<br>Required when MLAG leafs present in topology and they are using a separate L3 peering VLAN.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_peer_l3_ipv6_pool</samp>](## "<node_type_keys.key>.nodes.[].mlag_peer_l3_ipv6_pool") | String |  |  | Format: ipv6_pool | Comma separated list of prefixes (IPv6 address/Mask) or ranges (IPv6_address-IPv6_address).<br>The IPv6 subnet used for MLAG underlay L3 peering is derived from this pool based on the node id of the first MLAG switch.<br>Required when MLAG leafs present in topology and they are using a separate L3 peering VLAN.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_peer_vlan</samp>](## "<node_type_keys.key>.nodes.[].mlag_peer_vlan") | Integer |  | `4094` | Min: 1<br>Max: 4094 | MLAG Peer Link (control link) SVI interface id. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_peer_link_allowed_vlans</samp>](## "<node_type_keys.key>.nodes.[].mlag_peer_link_allowed_vlans") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_peer_address_family</samp>](## "<node_type_keys.key>.nodes.[].mlag_peer_address_family") | String |  | `ipv4` | Valid Values:<br>- <code>ipv4</code><br>- <code>ipv6</code> | IP address family used to establish MLAG Peer Link (control link).<br>`ipv6` requires EOS version 4.31.1F or higher.<br>Note: `ipv6` is not supported in combination with a common MLAG peer link VLAN (ex. `mlag_peer_l3_vlan` set to 4094). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_peer_ipv4_pool</samp>](## "<node_type_keys.key>.nodes.[].mlag_peer_ipv4_pool") | String |  |  | Format: ipv4_pool | Comma separated list of prefixes (IPv4 address/Mask) or ranges (IPv4_address-IPv4_address).<br>The IPv4 address used for MLAG Peer Link (control link) is derived from this pool based on the node id of the first MLAG switch.<br>Required for MLAG leafs when `mlag_peer_address_family` is `ipv4` (default). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_peer_ipv6_pool</samp>](## "<node_type_keys.key>.nodes.[].mlag_peer_ipv6_pool") | String |  |  | Format: ipv6_pool | Comma separated list of prefixes (IPv6 address/Mask) or ranges (IPv6_address-IPv6_address).<br>The IPv6 address used for MLAG Peer Link (control link) is derived from this pool based on the node id of the first MLAG switch.<br>Required for MLAG leafs when `mlag_peer_address_family` is `ipv6`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_port_channel_id</samp>](## "<node_type_keys.key>.nodes.[].mlag_port_channel_id") | Integer |  |  |  | If not set, the mlag port-channel id is generated based on the digits of the first interface present in 'mlag_interfaces'.<br>Valid port-channel id numbers are < 1-2000 > for EOS < 4.25.0F and < 1 - 999999 > for EOS >= 4.25.0F.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_domain_id</samp>](## "<node_type_keys.key>.nodes.[].mlag_domain_id") | String |  |  |  | MLAG Domain ID. If not set the node group name (Set with "group" key) will be used. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_mode</samp>](## "<node_type_keys.key>.nodes.[].spanning_tree_mode") | String |  |  | Valid Values:<br>- <code>mstp</code><br>- <code>rstp</code><br>- <code>rapid-pvst</code><br>- <code>none</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_priority</samp>](## "<node_type_keys.key>.nodes.[].spanning_tree_priority") | Integer |  | `32768` |  | Spanning-tree priority configured for the selected mode.<br>For `rapid-pvst` the priority can also be set per VLAN under network services. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_root_super</samp>](## "<node_type_keys.key>.nodes.[].spanning_tree_root_super") | Boolean |  | `False` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_mst_pvst_boundary</samp>](## "<node_type_keys.key>.nodes.[].spanning_tree_mst_pvst_boundary") | Boolean |  |  |  | Enable MST PVST border ports. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_port_id_allocation_port_channel_range</samp>](## "<node_type_keys.key>.nodes.[].spanning_tree_port_id_allocation_port_channel_range") | Dictionary |  |  |  | Specify range of port-ids to reserve for port-channels. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;minimum</samp>](## "<node_type_keys.key>.nodes.[].spanning_tree_port_id_allocation_port_channel_range.minimum") | Integer | Required |  | Min: 1<br>Max: 2048 | Specify minimum value for reserved range. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maximum</samp>](## "<node_type_keys.key>.nodes.[].spanning_tree_port_id_allocation_port_channel_range.maximum") | Integer | Required |  | Min: 1<br>Max: 2048 | Specify maximum value for reserved range. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;virtual_router_mac_address</samp>](## "<node_type_keys.key>.nodes.[].virtual_router_mac_address") | String |  |  | Format: mac | Virtual router mac address for anycast gateway. |

=== "YAML"

    ```yaml
    <node_type_keys.key>:

      # Define variables for all nodes of this type.
      defaults:

        # Custom structured config applied to MLAG peer link port-channel id.
        # Added under port_channel_interfaces.[name=<interface>] for eos_cli_config_gen.
        # Overrides the settings on the port-channel interface level.
        # "mlag_port_channel_structured_config" is applied after "structured_config", so it can override "structured_config" defined on node-level.
        mlag_port_channel_structured_config: <dict>

        # Custom structured config applied to MLAG Peer Link (control link) SVI interface id.
        # Added under vlan_interfaces.[name=<interface>] for eos_cli_config_gen.
        # Overrides the settings on the vlan interface level.
        # "mlag_peer_vlan_structured_config" is applied after "structured_config", so it can override "structured_config" defined on node-level.
        mlag_peer_vlan_structured_config: <dict>

        # Custom structured config applied to MLAG underlay L3 peering SVI interface id.
        # Added under vlan_interfaces.[name=<interface>] for eos_cli_config_gen.
        # Overrides the settings on the vlan interface level.
        # "mlag_peer_l3_vlan_structured_config" is applied after "structured_config", so it can override "structured_config" defined on node-level.
        mlag_peer_l3_vlan_structured_config: <dict>

        # Enable / Disable auto MLAG, when two nodes are defined in node group.
        mlag: <bool; default=True>

        # Enable / Disable MLAG dual primary detection.
        mlag_dual_primary_detection: <bool; default=False>

        # Set origin of routes received from MLAG iBGP peer to incomplete.
        # The purpose is to optimize routing for leaf loopbacks from spine perspective and
        # avoid suboptimal routing via peerlink for control plane traffic.
        mlag_ibgp_origin_incomplete: <bool; default=True>

        # Each list item supports range syntax that can be expanded into a list of interfaces.
        # Required when MLAG leafs are present in the topology.
        mlag_interfaces:
          - <str>

        # Set MLAG interface speed.
        mlag_interfaces_speed: <str; "100full" | "100g" | "100g-1" | "100g-2" | "100g-4" | "100half" | "10full" | "10g" | "10half" | "1g" | "200g" | "200g-2" | "200g-4" | "25g" | "400g" | "400g-4" | "400g-8" | "40g" | "50g" | "50g-1" | "50g-2" | "800g-8" | "sfp-1000baset auto 100full" | "1.6t-8" | "100mfull" | "100mhalf" | "10mfull" | "10mhalf" | "200g-1" | "400g-2" | "40g-4" | "800g-4" | "auto" | "auto 10000full" | "auto 1000full" | "auto 100full" | "auto 100g-1" | "auto 100g-2" | "auto 100g-4" | "auto 100gfull" | "auto 100half" | "auto 10full" | "auto 10gfull" | "auto 10half" | "auto 1gfull" | "auto 2.5gfull" | "auto 200g-2" | "auto 200g-4" | "auto 25gfull" | "auto 400g-4" | "auto 400g-8" | "auto 40gfull" | "auto 50g-1" | "auto 50g-2" | "auto 50gfull" | "auto 5gfull" | "auto 800g-8" | "auto 1.6t-8" | "auto 100mfull" | "auto 100mhalf" | "auto 10g" | "auto 10mfull" | "auto 10mhalf" | "auto 1g" | "auto 2.5g" | "auto 200g-1" | "auto 25g" | "auto 400g-2" | "auto 40g-4" | "auto 5g" | "auto 800g-4" | "forced 10000full" | "forced 1000full" | "forced 1000half" | "forced 100full" | "forced 100gfull" | "forced 100half" | "forced 10full" | "forced 10half" | "forced 25gfull" | "forced 40gfull" | "forced 50gfull">

        # Underlay L3 peering SVI interface id.
        # If set to 0 or the same vlan as mlag_peer_vlan, the mlag_peer_vlan will be used for L3 peering.
        mlag_peer_l3_vlan: <int; 0-4094; default=4093>

        # Comma separated list of prefixes (IPv4 address/Mask) or ranges (IPv4_address-IPv4_address).
        # The IPv4 subnet used for MLAG underlay L3 peering is derived from this pool based on the node id of the first MLAG switch.
        # Required when MLAG leafs present in topology and they are using a separate L3 peering VLAN.
        mlag_peer_l3_ipv4_pool: <str>

        # Comma separated list of prefixes (IPv6 address/Mask) or ranges (IPv6_address-IPv6_address).
        # The IPv6 subnet used for MLAG underlay L3 peering is derived from this pool based on the node id of the first MLAG switch.
        # Required when MLAG leafs present in topology and they are using a separate L3 peering VLAN.
        mlag_peer_l3_ipv6_pool: <str>

        # MLAG Peer Link (control link) SVI interface id.
        mlag_peer_vlan: <int; 1-4094; default=4094>
        mlag_peer_link_allowed_vlans: <str>

        # IP address family used to establish MLAG Peer Link (control link).
        # `ipv6` requires EOS version 4.31.1F or higher.
        # Note: `ipv6` is not supported in combination with a common MLAG peer link VLAN (ex. `mlag_peer_l3_vlan` set to 4094).
        mlag_peer_address_family: <str; "ipv4" | "ipv6"; default="ipv4">

        # Comma separated list of prefixes (IPv4 address/Mask) or ranges (IPv4_address-IPv4_address).
        # The IPv4 address used for MLAG Peer Link (control link) is derived from this pool based on the node id of the first MLAG switch.
        # Required for MLAG leafs when `mlag_peer_address_family` is `ipv4` (default).
        mlag_peer_ipv4_pool: <str>

        # Comma separated list of prefixes (IPv6 address/Mask) or ranges (IPv6_address-IPv6_address).
        # The IPv6 address used for MLAG Peer Link (control link) is derived from this pool based on the node id of the first MLAG switch.
        # Required for MLAG leafs when `mlag_peer_address_family` is `ipv6`.
        mlag_peer_ipv6_pool: <str>

        # If not set, the mlag port-channel id is generated based on the digits of the first interface present in 'mlag_interfaces'.
        # Valid port-channel id numbers are < 1-2000 > for EOS < 4.25.0F and < 1 - 999999 > for EOS >= 4.25.0F.
        mlag_port_channel_id: <int>

        # MLAG Domain ID. If not set the node group name (Set with "group" key) will be used.
        mlag_domain_id: <str>
        spanning_tree_mode: <str; "mstp" | "rstp" | "rapid-pvst" | "none">

        # Spanning-tree priority configured for the selected mode.
        # For `rapid-pvst` the priority can also be set per VLAN under network services.
        spanning_tree_priority: <int; default=32768>
        spanning_tree_root_super: <bool; default=False>

        # Enable MST PVST border ports.
        spanning_tree_mst_pvst_boundary: <bool>

        # Specify range of port-ids to reserve for port-channels.
        spanning_tree_port_id_allocation_port_channel_range:

          # Specify minimum value for reserved range.
          minimum: <int; 1-2048; required>

          # Specify maximum value for reserved range.
          maximum: <int; 1-2048; required>

        # Virtual router mac address for anycast gateway.
        virtual_router_mac_address: <str>

      # Define variables related to all nodes part of this group.
      node_groups:

          # The Node Group Name is used for MLAG domain unless set with 'mlag_domain_id'.
          # The Node Group Name is also used for peer description on downstream switches' uplinks.
        - group: <str; required; unique>

          # Define variables per node.
          nodes:

              # The Node Name is used as "hostname".
            - name: <str; required; unique>

              # Custom structured config applied to MLAG peer link port-channel id.
              # Added under port_channel_interfaces.[name=<interface>] for eos_cli_config_gen.
              # Overrides the settings on the port-channel interface level.
              # "mlag_port_channel_structured_config" is applied after "structured_config", so it can override "structured_config" defined on node-level.
              mlag_port_channel_structured_config: <dict>

              # Custom structured config applied to MLAG Peer Link (control link) SVI interface id.
              # Added under vlan_interfaces.[name=<interface>] for eos_cli_config_gen.
              # Overrides the settings on the vlan interface level.
              # "mlag_peer_vlan_structured_config" is applied after "structured_config", so it can override "structured_config" defined on node-level.
              mlag_peer_vlan_structured_config: <dict>

              # Custom structured config applied to MLAG underlay L3 peering SVI interface id.
              # Added under vlan_interfaces.[name=<interface>] for eos_cli_config_gen.
              # Overrides the settings on the vlan interface level.
              # "mlag_peer_l3_vlan_structured_config" is applied after "structured_config", so it can override "structured_config" defined on node-level.
              mlag_peer_l3_vlan_structured_config: <dict>

              # Enable / Disable auto MLAG, when two nodes are defined in node group.
              mlag: <bool; default=True>

              # Enable / Disable MLAG dual primary detection.
              mlag_dual_primary_detection: <bool; default=False>

              # Set origin of routes received from MLAG iBGP peer to incomplete.
              # The purpose is to optimize routing for leaf loopbacks from spine perspective and
              # avoid suboptimal routing via peerlink for control plane traffic.
              mlag_ibgp_origin_incomplete: <bool; default=True>

              # Each list item supports range syntax that can be expanded into a list of interfaces.
              # Required when MLAG leafs are present in the topology.
              mlag_interfaces:
                - <str>

              # Set MLAG interface speed.
              mlag_interfaces_speed: <str; "100full" | "100g" | "100g-1" | "100g-2" | "100g-4" | "100half" | "10full" | "10g" | "10half" | "1g" | "200g" | "200g-2" | "200g-4" | "25g" | "400g" | "400g-4" | "400g-8" | "40g" | "50g" | "50g-1" | "50g-2" | "800g-8" | "sfp-1000baset auto 100full" | "1.6t-8" | "100mfull" | "100mhalf" | "10mfull" | "10mhalf" | "200g-1" | "400g-2" | "40g-4" | "800g-4" | "auto" | "auto 10000full" | "auto 1000full" | "auto 100full" | "auto 100g-1" | "auto 100g-2" | "auto 100g-4" | "auto 100gfull" | "auto 100half" | "auto 10full" | "auto 10gfull" | "auto 10half" | "auto 1gfull" | "auto 2.5gfull" | "auto 200g-2" | "auto 200g-4" | "auto 25gfull" | "auto 400g-4" | "auto 400g-8" | "auto 40gfull" | "auto 50g-1" | "auto 50g-2" | "auto 50gfull" | "auto 5gfull" | "auto 800g-8" | "auto 1.6t-8" | "auto 100mfull" | "auto 100mhalf" | "auto 10g" | "auto 10mfull" | "auto 10mhalf" | "auto 1g" | "auto 2.5g" | "auto 200g-1" | "auto 25g" | "auto 400g-2" | "auto 40g-4" | "auto 5g" | "auto 800g-4" | "forced 10000full" | "forced 1000full" | "forced 1000half" | "forced 100full" | "forced 100gfull" | "forced 100half" | "forced 10full" | "forced 10half" | "forced 25gfull" | "forced 40gfull" | "forced 50gfull">

              # Underlay L3 peering SVI interface id.
              # If set to 0 or the same vlan as mlag_peer_vlan, the mlag_peer_vlan will be used for L3 peering.
              mlag_peer_l3_vlan: <int; 0-4094; default=4093>

              # Comma separated list of prefixes (IPv4 address/Mask) or ranges (IPv4_address-IPv4_address).
              # The IPv4 subnet used for MLAG underlay L3 peering is derived from this pool based on the node id of the first MLAG switch.
              # Required when MLAG leafs present in topology and they are using a separate L3 peering VLAN.
              mlag_peer_l3_ipv4_pool: <str>

              # Comma separated list of prefixes (IPv6 address/Mask) or ranges (IPv6_address-IPv6_address).
              # The IPv6 subnet used for MLAG underlay L3 peering is derived from this pool based on the node id of the first MLAG switch.
              # Required when MLAG leafs present in topology and they are using a separate L3 peering VLAN.
              mlag_peer_l3_ipv6_pool: <str>

              # MLAG Peer Link (control link) SVI interface id.
              mlag_peer_vlan: <int; 1-4094; default=4094>
              mlag_peer_link_allowed_vlans: <str>

              # IP address family used to establish MLAG Peer Link (control link).
              # `ipv6` requires EOS version 4.31.1F or higher.
              # Note: `ipv6` is not supported in combination with a common MLAG peer link VLAN (ex. `mlag_peer_l3_vlan` set to 4094).
              mlag_peer_address_family: <str; "ipv4" | "ipv6"; default="ipv4">

              # Comma separated list of prefixes (IPv4 address/Mask) or ranges (IPv4_address-IPv4_address).
              # The IPv4 address used for MLAG Peer Link (control link) is derived from this pool based on the node id of the first MLAG switch.
              # Required for MLAG leafs when `mlag_peer_address_family` is `ipv4` (default).
              mlag_peer_ipv4_pool: <str>

              # Comma separated list of prefixes (IPv6 address/Mask) or ranges (IPv6_address-IPv6_address).
              # The IPv6 address used for MLAG Peer Link (control link) is derived from this pool based on the node id of the first MLAG switch.
              # Required for MLAG leafs when `mlag_peer_address_family` is `ipv6`.
              mlag_peer_ipv6_pool: <str>

              # If not set, the mlag port-channel id is generated based on the digits of the first interface present in 'mlag_interfaces'.
              # Valid port-channel id numbers are < 1-2000 > for EOS < 4.25.0F and < 1 - 999999 > for EOS >= 4.25.0F.
              mlag_port_channel_id: <int>

              # MLAG Domain ID. If not set the node group name (Set with "group" key) will be used.
              mlag_domain_id: <str>
              spanning_tree_mode: <str; "mstp" | "rstp" | "rapid-pvst" | "none">

              # Spanning-tree priority configured for the selected mode.
              # For `rapid-pvst` the priority can also be set per VLAN under network services.
              spanning_tree_priority: <int; default=32768>
              spanning_tree_root_super: <bool; default=False>

              # Enable MST PVST border ports.
              spanning_tree_mst_pvst_boundary: <bool>

              # Specify range of port-ids to reserve for port-channels.
              spanning_tree_port_id_allocation_port_channel_range:

                # Specify minimum value for reserved range.
                minimum: <int; 1-2048; required>

                # Specify maximum value for reserved range.
                maximum: <int; 1-2048; required>

              # Virtual router mac address for anycast gateway.
              virtual_router_mac_address: <str>

          # Custom structured config applied to MLAG peer link port-channel id.
          # Added under port_channel_interfaces.[name=<interface>] for eos_cli_config_gen.
          # Overrides the settings on the port-channel interface level.
          # "mlag_port_channel_structured_config" is applied after "structured_config", so it can override "structured_config" defined on node-level.
          mlag_port_channel_structured_config: <dict>

          # Custom structured config applied to MLAG Peer Link (control link) SVI interface id.
          # Added under vlan_interfaces.[name=<interface>] for eos_cli_config_gen.
          # Overrides the settings on the vlan interface level.
          # "mlag_peer_vlan_structured_config" is applied after "structured_config", so it can override "structured_config" defined on node-level.
          mlag_peer_vlan_structured_config: <dict>

          # Custom structured config applied to MLAG underlay L3 peering SVI interface id.
          # Added under vlan_interfaces.[name=<interface>] for eos_cli_config_gen.
          # Overrides the settings on the vlan interface level.
          # "mlag_peer_l3_vlan_structured_config" is applied after "structured_config", so it can override "structured_config" defined on node-level.
          mlag_peer_l3_vlan_structured_config: <dict>

          # Enable / Disable auto MLAG, when two nodes are defined in node group.
          mlag: <bool; default=True>

          # Enable / Disable MLAG dual primary detection.
          mlag_dual_primary_detection: <bool; default=False>

          # Set origin of routes received from MLAG iBGP peer to incomplete.
          # The purpose is to optimize routing for leaf loopbacks from spine perspective and
          # avoid suboptimal routing via peerlink for control plane traffic.
          mlag_ibgp_origin_incomplete: <bool; default=True>

          # Each list item supports range syntax that can be expanded into a list of interfaces.
          # Required when MLAG leafs are present in the topology.
          mlag_interfaces:
            - <str>

          # Set MLAG interface speed.
          mlag_interfaces_speed: <str; "100full" | "100g" | "100g-1" | "100g-2" | "100g-4" | "100half" | "10full" | "10g" | "10half" | "1g" | "200g" | "200g-2" | "200g-4" | "25g" | "400g" | "400g-4" | "400g-8" | "40g" | "50g" | "50g-1" | "50g-2" | "800g-8" | "sfp-1000baset auto 100full" | "1.6t-8" | "100mfull" | "100mhalf" | "10mfull" | "10mhalf" | "200g-1" | "400g-2" | "40g-4" | "800g-4" | "auto" | "auto 10000full" | "auto 1000full" | "auto 100full" | "auto 100g-1" | "auto 100g-2" | "auto 100g-4" | "auto 100gfull" | "auto 100half" | "auto 10full" | "auto 10gfull" | "auto 10half" | "auto 1gfull" | "auto 2.5gfull" | "auto 200g-2" | "auto 200g-4" | "auto 25gfull" | "auto 400g-4" | "auto 400g-8" | "auto 40gfull" | "auto 50g-1" | "auto 50g-2" | "auto 50gfull" | "auto 5gfull" | "auto 800g-8" | "auto 1.6t-8" | "auto 100mfull" | "auto 100mhalf" | "auto 10g" | "auto 10mfull" | "auto 10mhalf" | "auto 1g" | "auto 2.5g" | "auto 200g-1" | "auto 25g" | "auto 400g-2" | "auto 40g-4" | "auto 5g" | "auto 800g-4" | "forced 10000full" | "forced 1000full" | "forced 1000half" | "forced 100full" | "forced 100gfull" | "forced 100half" | "forced 10full" | "forced 10half" | "forced 25gfull" | "forced 40gfull" | "forced 50gfull">

          # Underlay L3 peering SVI interface id.
          # If set to 0 or the same vlan as mlag_peer_vlan, the mlag_peer_vlan will be used for L3 peering.
          mlag_peer_l3_vlan: <int; 0-4094; default=4093>

          # Comma separated list of prefixes (IPv4 address/Mask) or ranges (IPv4_address-IPv4_address).
          # The IPv4 subnet used for MLAG underlay L3 peering is derived from this pool based on the node id of the first MLAG switch.
          # Required when MLAG leafs present in topology and they are using a separate L3 peering VLAN.
          mlag_peer_l3_ipv4_pool: <str>

          # Comma separated list of prefixes (IPv6 address/Mask) or ranges (IPv6_address-IPv6_address).
          # The IPv6 subnet used for MLAG underlay L3 peering is derived from this pool based on the node id of the first MLAG switch.
          # Required when MLAG leafs present in topology and they are using a separate L3 peering VLAN.
          mlag_peer_l3_ipv6_pool: <str>

          # MLAG Peer Link (control link) SVI interface id.
          mlag_peer_vlan: <int; 1-4094; default=4094>
          mlag_peer_link_allowed_vlans: <str>

          # IP address family used to establish MLAG Peer Link (control link).
          # `ipv6` requires EOS version 4.31.1F or higher.
          # Note: `ipv6` is not supported in combination with a common MLAG peer link VLAN (ex. `mlag_peer_l3_vlan` set to 4094).
          mlag_peer_address_family: <str; "ipv4" | "ipv6"; default="ipv4">

          # Comma separated list of prefixes (IPv4 address/Mask) or ranges (IPv4_address-IPv4_address).
          # The IPv4 address used for MLAG Peer Link (control link) is derived from this pool based on the node id of the first MLAG switch.
          # Required for MLAG leafs when `mlag_peer_address_family` is `ipv4` (default).
          mlag_peer_ipv4_pool: <str>

          # Comma separated list of prefixes (IPv6 address/Mask) or ranges (IPv6_address-IPv6_address).
          # The IPv6 address used for MLAG Peer Link (control link) is derived from this pool based on the node id of the first MLAG switch.
          # Required for MLAG leafs when `mlag_peer_address_family` is `ipv6`.
          mlag_peer_ipv6_pool: <str>

          # If not set, the mlag port-channel id is generated based on the digits of the first interface present in 'mlag_interfaces'.
          # Valid port-channel id numbers are < 1-2000 > for EOS < 4.25.0F and < 1 - 999999 > for EOS >= 4.25.0F.
          mlag_port_channel_id: <int>

          # MLAG Domain ID. If not set the node group name (Set with "group" key) will be used.
          mlag_domain_id: <str>
          spanning_tree_mode: <str; "mstp" | "rstp" | "rapid-pvst" | "none">

          # Spanning-tree priority configured for the selected mode.
          # For `rapid-pvst` the priority can also be set per VLAN under network services.
          spanning_tree_priority: <int; default=32768>
          spanning_tree_root_super: <bool; default=False>

          # Enable MST PVST border ports.
          spanning_tree_mst_pvst_boundary: <bool>

          # Specify range of port-ids to reserve for port-channels.
          spanning_tree_port_id_allocation_port_channel_range:

            # Specify minimum value for reserved range.
            minimum: <int; 1-2048; required>

            # Specify maximum value for reserved range.
            maximum: <int; 1-2048; required>

          # Virtual router mac address for anycast gateway.
          virtual_router_mac_address: <str>

      # Define variables per node.
      nodes:

          # The Node Name is used as "hostname".
        - name: <str; required; unique>

          # Custom structured config applied to MLAG peer link port-channel id.
          # Added under port_channel_interfaces.[name=<interface>] for eos_cli_config_gen.
          # Overrides the settings on the port-channel interface level.
          # "mlag_port_channel_structured_config" is applied after "structured_config", so it can override "structured_config" defined on node-level.
          mlag_port_channel_structured_config: <dict>

          # Custom structured config applied to MLAG Peer Link (control link) SVI interface id.
          # Added under vlan_interfaces.[name=<interface>] for eos_cli_config_gen.
          # Overrides the settings on the vlan interface level.
          # "mlag_peer_vlan_structured_config" is applied after "structured_config", so it can override "structured_config" defined on node-level.
          mlag_peer_vlan_structured_config: <dict>

          # Custom structured config applied to MLAG underlay L3 peering SVI interface id.
          # Added under vlan_interfaces.[name=<interface>] for eos_cli_config_gen.
          # Overrides the settings on the vlan interface level.
          # "mlag_peer_l3_vlan_structured_config" is applied after "structured_config", so it can override "structured_config" defined on node-level.
          mlag_peer_l3_vlan_structured_config: <dict>

          # Enable / Disable auto MLAG, when two nodes are defined in node group.
          mlag: <bool; default=True>

          # Enable / Disable MLAG dual primary detection.
          mlag_dual_primary_detection: <bool; default=False>

          # Set origin of routes received from MLAG iBGP peer to incomplete.
          # The purpose is to optimize routing for leaf loopbacks from spine perspective and
          # avoid suboptimal routing via peerlink for control plane traffic.
          mlag_ibgp_origin_incomplete: <bool; default=True>

          # Each list item supports range syntax that can be expanded into a list of interfaces.
          # Required when MLAG leafs are present in the topology.
          mlag_interfaces:
            - <str>

          # Set MLAG interface speed.
          mlag_interfaces_speed: <str; "100full" | "100g" | "100g-1" | "100g-2" | "100g-4" | "100half" | "10full" | "10g" | "10half" | "1g" | "200g" | "200g-2" | "200g-4" | "25g" | "400g" | "400g-4" | "400g-8" | "40g" | "50g" | "50g-1" | "50g-2" | "800g-8" | "sfp-1000baset auto 100full" | "1.6t-8" | "100mfull" | "100mhalf" | "10mfull" | "10mhalf" | "200g-1" | "400g-2" | "40g-4" | "800g-4" | "auto" | "auto 10000full" | "auto 1000full" | "auto 100full" | "auto 100g-1" | "auto 100g-2" | "auto 100g-4" | "auto 100gfull" | "auto 100half" | "auto 10full" | "auto 10gfull" | "auto 10half" | "auto 1gfull" | "auto 2.5gfull" | "auto 200g-2" | "auto 200g-4" | "auto 25gfull" | "auto 400g-4" | "auto 400g-8" | "auto 40gfull" | "auto 50g-1" | "auto 50g-2" | "auto 50gfull" | "auto 5gfull" | "auto 800g-8" | "auto 1.6t-8" | "auto 100mfull" | "auto 100mhalf" | "auto 10g" | "auto 10mfull" | "auto 10mhalf" | "auto 1g" | "auto 2.5g" | "auto 200g-1" | "auto 25g" | "auto 400g-2" | "auto 40g-4" | "auto 5g" | "auto 800g-4" | "forced 10000full" | "forced 1000full" | "forced 1000half" | "forced 100full" | "forced 100gfull" | "forced 100half" | "forced 10full" | "forced 10half" | "forced 25gfull" | "forced 40gfull" | "forced 50gfull">

          # Underlay L3 peering SVI interface id.
          # If set to 0 or the same vlan as mlag_peer_vlan, the mlag_peer_vlan will be used for L3 peering.
          mlag_peer_l3_vlan: <int; 0-4094; default=4093>

          # Comma separated list of prefixes (IPv4 address/Mask) or ranges (IPv4_address-IPv4_address).
          # The IPv4 subnet used for MLAG underlay L3 peering is derived from this pool based on the node id of the first MLAG switch.
          # Required when MLAG leafs present in topology and they are using a separate L3 peering VLAN.
          mlag_peer_l3_ipv4_pool: <str>

          # Comma separated list of prefixes (IPv6 address/Mask) or ranges (IPv6_address-IPv6_address).
          # The IPv6 subnet used for MLAG underlay L3 peering is derived from this pool based on the node id of the first MLAG switch.
          # Required when MLAG leafs present in topology and they are using a separate L3 peering VLAN.
          mlag_peer_l3_ipv6_pool: <str>

          # MLAG Peer Link (control link) SVI interface id.
          mlag_peer_vlan: <int; 1-4094; default=4094>
          mlag_peer_link_allowed_vlans: <str>

          # IP address family used to establish MLAG Peer Link (control link).
          # `ipv6` requires EOS version 4.31.1F or higher.
          # Note: `ipv6` is not supported in combination with a common MLAG peer link VLAN (ex. `mlag_peer_l3_vlan` set to 4094).
          mlag_peer_address_family: <str; "ipv4" | "ipv6"; default="ipv4">

          # Comma separated list of prefixes (IPv4 address/Mask) or ranges (IPv4_address-IPv4_address).
          # The IPv4 address used for MLAG Peer Link (control link) is derived from this pool based on the node id of the first MLAG switch.
          # Required for MLAG leafs when `mlag_peer_address_family` is `ipv4` (default).
          mlag_peer_ipv4_pool: <str>

          # Comma separated list of prefixes (IPv6 address/Mask) or ranges (IPv6_address-IPv6_address).
          # The IPv6 address used for MLAG Peer Link (control link) is derived from this pool based on the node id of the first MLAG switch.
          # Required for MLAG leafs when `mlag_peer_address_family` is `ipv6`.
          mlag_peer_ipv6_pool: <str>

          # If not set, the mlag port-channel id is generated based on the digits of the first interface present in 'mlag_interfaces'.
          # Valid port-channel id numbers are < 1-2000 > for EOS < 4.25.0F and < 1 - 999999 > for EOS >= 4.25.0F.
          mlag_port_channel_id: <int>

          # MLAG Domain ID. If not set the node group name (Set with "group" key) will be used.
          mlag_domain_id: <str>
          spanning_tree_mode: <str; "mstp" | "rstp" | "rapid-pvst" | "none">

          # Spanning-tree priority configured for the selected mode.
          # For `rapid-pvst` the priority can also be set per VLAN under network services.
          spanning_tree_priority: <int; default=32768>
          spanning_tree_root_super: <bool; default=False>

          # Enable MST PVST border ports.
          spanning_tree_mst_pvst_boundary: <bool>

          # Specify range of port-ids to reserve for port-channels.
          spanning_tree_port_id_allocation_port_channel_range:

            # Specify minimum value for reserved range.
            minimum: <int; 1-2048; required>

            # Specify maximum value for reserved range.
            maximum: <int; 1-2048; required>

          # Virtual router mac address for anycast gateway.
          virtual_router_mac_address: <str>
    ```
