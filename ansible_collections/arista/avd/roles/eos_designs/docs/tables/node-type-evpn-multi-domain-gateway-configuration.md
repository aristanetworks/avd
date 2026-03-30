<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>&lt;node_type_keys.key&gt;</samp>](## "<node_type_keys.key>") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;defaults</samp>](## "<node_type_keys.key>.defaults") | Dictionary |  |  |  | Define variables for all nodes of this type. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;evpn_gateway</samp>](## "<node_type_keys.key>.defaults.evpn_gateway") | Dictionary |  |  |  | Node is acting as EVPN Multi-Domain Gateway.<br>New BGP peer-group is generated between EVPN GWs in different domains or between GWs and Route Servers.<br>Name can be changed under "bgp_peer_groups.evpn_overlay_core" variable.<br>L3 rechability for different EVPN GWs must be already in place, it is recommended to use DCI & L3 Edge if Route Servers and GWs are not defined under the same Ansible inventory.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remote_peers</samp>](## "<node_type_keys.key>.defaults.evpn_gateway.remote_peers") | List, items: Dictionary |  |  |  | Define remote peers of the EVPN VXLAN Gateway.<br>If the hostname can be found in the inventory, ip_address and BGP ASN will be automatically populated. Manual override takes precedence.<br>If the peer's hostname can not be found in the inventory, ip_address and bgp_as must be defined.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;hostname</samp>](## "<node_type_keys.key>.defaults.evpn_gateway.remote_peers.[].hostname") | String | Required, Unique |  |  | Hostname of remote EVPN GW server. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "<node_type_keys.key>.defaults.evpn_gateway.remote_peers.[].ip_address") | String |  |  | Format: ipv4 | Peering IP of remote Route Server. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp_as</samp>](## "<node_type_keys.key>.defaults.evpn_gateway.remote_peers.[].bgp_as") | String |  |  |  | Remote Route Server's BGP AS <1-4294967295> or AS number in asdot notation "<1-65535>.<0-65535>".<br>For asdot notation in YAML inputs, the value must be put in quotes, to prevent it from being interpreted as a float number. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_l2</samp>](## "<node_type_keys.key>.defaults.evpn_gateway.evpn_l2") | Dictionary |  |  |  | Enable EVPN Gateway functionality for route-types 2 (MAC-IP) and 3 (IMET). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<node_type_keys.key>.defaults.evpn_gateway.evpn_l2.enabled") | Boolean |  | `False` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_l3</samp>](## "<node_type_keys.key>.defaults.evpn_gateway.evpn_l3") | Dictionary |  |  |  | Enable EVPN Gateway functionality for route-type 5 (IP-PREFIX). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<node_type_keys.key>.defaults.evpn_gateway.evpn_l3.enabled") | Boolean |  | `False` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inter_domain</samp>](## "<node_type_keys.key>.defaults.evpn_gateway.evpn_l3.inter_domain") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "<node_type_keys.key>.defaults.evpn_gateway.evpn_l3.mode") | String |  | `next-hop-self` | Valid Values:<br>- <code>next-hop-self</code><br>- <code>rd-rt-rewrite</code> | Defines the rewriting mode for EVPN L3 inter-domain routing.<br>- next-hop-self: (default) Forward EVPN IP-Prefix routes by only replacing the next-hop to the gateway itself.<br>- rd-rt-rewrite: Re-export local EVPN IP-Prefix routes with the RD and export RTs of the remote domain and vice versa.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;d_path</samp>](## "<node_type_keys.key>.defaults.evpn_gateway.d_path") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<node_type_keys.key>.defaults.evpn_gateway.d_path.enabled") | Boolean |  | `True` |  | Enable D-path for use with BGP bestpath selection algorithm. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;local_domain_id</samp>](## "<node_type_keys.key>.defaults.evpn_gateway.d_path.local_domain_id") | String | Required |  |  | ASN(asplain):local_admin or ASN(asdot):local_admin notation |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remote_domain_id</samp>](## "<node_type_keys.key>.defaults.evpn_gateway.d_path.remote_domain_id") | String | Required |  |  | ASN(asplain):local_admin or ASN(asdot):local_admin notation |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;all_active_multihoming</samp>](## "<node_type_keys.key>.defaults.evpn_gateway.all_active_multihoming") | Dictionary |  |  |  | Enable Active Active Multihoming architecture for EVPN Gateways.<br>Not supported with MLAG or IPVPN Gateway. Requires EVPN L3 inter-domain to be enabled. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<node_type_keys.key>.defaults.evpn_gateway.all_active_multihoming.enabled") | Boolean | Required |  |  | Enable Active Active Multihoming resiliency model. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enable_d_path</samp>](## "<node_type_keys.key>.defaults.evpn_gateway.all_active_multihoming.enable_d_path") <span style="color:red">deprecated</span> | Boolean |  | `True` |  | Enable D-path for use with BGP bestpath selection algorithm.<span style="color:red">This key is deprecated. Support will be removed in AVD version 7.0.0. Use <samp><node_type_key>.defaults.evpn_gateway.d_path.enabled or <node_type_key>.node_groups[].nodes[].evpn_gateway.d_path.enabled or <node_type_key>.node_groups[].evpn_gateway.d_path.enabled or <node_type_key>.nodes[].evpn_gateway.d_path.enabled or device_profiles[].evpn_gateway.d_path.enabled or devices[].evpn_gateway.d_path.enabled</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_domain_id_local</samp>](## "<node_type_keys.key>.defaults.evpn_gateway.all_active_multihoming.evpn_domain_id_local") <span style="color:red">deprecated</span> | String |  |  |  | ASN(asplain):local_admin or ASN(asdot):local_admin notation<span style="color:red">This key is deprecated. Support will be removed in AVD version 7.0.0. Use <samp><node_type_key>.defaults.evpn_gateway.d_path.local_domain_id_local or <node_type_key>.node_groups[].nodes[].evpn_gateway.d_path.local_domain_id_local or <node_type_key>.node_groups[].evpn_gateway.d_path.local_domain_id_local or <node_type_key>.nodes[].evpn_gateway.d_path.local_domain_id_local or device_profiles[].evpn_gateway.d_path.local_domain_id_local or devices[].evpn_gateway.d_path.local_domain_id_local</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_domain_id_remote</samp>](## "<node_type_keys.key>.defaults.evpn_gateway.all_active_multihoming.evpn_domain_id_remote") <span style="color:red">deprecated</span> | String |  |  |  | ASN(asplain):local_admin or ASN(asdot):local_admin notation<span style="color:red">This key is deprecated. Support will be removed in AVD version 7.0.0. Use <samp><node_type_key>.defaults.evpn_gateway.d_path.remote_domain_id or <node_type_key>.node_groups[].nodes[].evpn_gateway.d_path.remote_domain_id or <node_type_key>.node_groups[].evpn_gateway.d_path.remote_domain_id or <node_type_key>.nodes[].evpn_gateway.d_path.remote_domain_id or device_profiles[].evpn_gateway.d_path.remote_domain_id or devices[].evpn_gateway.d_path.remote_domain_id</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_ethernet_segment</samp>](## "<node_type_keys.key>.defaults.evpn_gateway.all_active_multihoming.evpn_ethernet_segment") | Dictionary | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;identifier</samp>](## "<node_type_keys.key>.defaults.evpn_gateway.all_active_multihoming.evpn_ethernet_segment.identifier") | String | Required |  |  | EVPN Ethernet Segment Identifier (Type 1 format) |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rt_import</samp>](## "<node_type_keys.key>.defaults.evpn_gateway.all_active_multihoming.evpn_ethernet_segment.rt_import") | String | Required |  |  | Low-order 6 bytes of ES-Import Route Target. |
    | [<samp>&nbsp;&nbsp;node_groups</samp>](## "<node_type_keys.key>.node_groups") | List, items: Dictionary |  |  |  | Define variables related to all nodes part of this group. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;group</samp>](## "<node_type_keys.key>.node_groups.[].group") | String | Required, Unique |  |  | The Node Group Name is used for MLAG domain unless set with 'mlag_domain_id'.<br>The Node Group Name is also used for peer description on downstream switches' uplinks.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "<node_type_keys.key>.node_groups.[].nodes") | List, items: Dictionary |  |  |  | Define variables per node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].name") | String | Required, Unique |  |  | The Node Name is used as "hostname". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_gateway</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].evpn_gateway") | Dictionary |  |  |  | Node is acting as EVPN Multi-Domain Gateway.<br>New BGP peer-group is generated between EVPN GWs in different domains or between GWs and Route Servers.<br>Name can be changed under "bgp_peer_groups.evpn_overlay_core" variable.<br>L3 rechability for different EVPN GWs must be already in place, it is recommended to use DCI & L3 Edge if Route Servers and GWs are not defined under the same Ansible inventory.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remote_peers</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].evpn_gateway.remote_peers") | List, items: Dictionary |  |  |  | Define remote peers of the EVPN VXLAN Gateway.<br>If the hostname can be found in the inventory, ip_address and BGP ASN will be automatically populated. Manual override takes precedence.<br>If the peer's hostname can not be found in the inventory, ip_address and bgp_as must be defined.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;hostname</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].evpn_gateway.remote_peers.[].hostname") | String | Required, Unique |  |  | Hostname of remote EVPN GW server. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].evpn_gateway.remote_peers.[].ip_address") | String |  |  | Format: ipv4 | Peering IP of remote Route Server. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp_as</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].evpn_gateway.remote_peers.[].bgp_as") | String |  |  |  | Remote Route Server's BGP AS <1-4294967295> or AS number in asdot notation "<1-65535>.<0-65535>".<br>For asdot notation in YAML inputs, the value must be put in quotes, to prevent it from being interpreted as a float number. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_l2</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].evpn_gateway.evpn_l2") | Dictionary |  |  |  | Enable EVPN Gateway functionality for route-types 2 (MAC-IP) and 3 (IMET). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].evpn_gateway.evpn_l2.enabled") | Boolean |  | `False` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_l3</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].evpn_gateway.evpn_l3") | Dictionary |  |  |  | Enable EVPN Gateway functionality for route-type 5 (IP-PREFIX). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].evpn_gateway.evpn_l3.enabled") | Boolean |  | `False` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inter_domain</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].evpn_gateway.evpn_l3.inter_domain") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].evpn_gateway.evpn_l3.mode") | String |  | `next-hop-self` | Valid Values:<br>- <code>next-hop-self</code><br>- <code>rd-rt-rewrite</code> | Defines the rewriting mode for EVPN L3 inter-domain routing.<br>- next-hop-self: (default) Forward EVPN IP-Prefix routes by only replacing the next-hop to the gateway itself.<br>- rd-rt-rewrite: Re-export local EVPN IP-Prefix routes with the RD and export RTs of the remote domain and vice versa.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;d_path</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].evpn_gateway.d_path") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].evpn_gateway.d_path.enabled") | Boolean |  | `True` |  | Enable D-path for use with BGP bestpath selection algorithm. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;local_domain_id</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].evpn_gateway.d_path.local_domain_id") | String | Required |  |  | ASN(asplain):local_admin or ASN(asdot):local_admin notation |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remote_domain_id</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].evpn_gateway.d_path.remote_domain_id") | String | Required |  |  | ASN(asplain):local_admin or ASN(asdot):local_admin notation |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;all_active_multihoming</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].evpn_gateway.all_active_multihoming") | Dictionary |  |  |  | Enable Active Active Multihoming architecture for EVPN Gateways.<br>Not supported with MLAG or IPVPN Gateway. Requires EVPN L3 inter-domain to be enabled. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].evpn_gateway.all_active_multihoming.enabled") | Boolean | Required |  |  | Enable Active Active Multihoming resiliency model. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enable_d_path</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].evpn_gateway.all_active_multihoming.enable_d_path") <span style="color:red">deprecated</span> | Boolean |  | `True` |  | Enable D-path for use with BGP bestpath selection algorithm.<span style="color:red">This key is deprecated. Support will be removed in AVD version 7.0.0. Use <samp><node_type_key>.defaults.evpn_gateway.d_path.enabled or <node_type_key>.node_groups[].nodes[].evpn_gateway.d_path.enabled or <node_type_key>.node_groups[].evpn_gateway.d_path.enabled or <node_type_key>.nodes[].evpn_gateway.d_path.enabled or device_profiles[].evpn_gateway.d_path.enabled or devices[].evpn_gateway.d_path.enabled</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_domain_id_local</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].evpn_gateway.all_active_multihoming.evpn_domain_id_local") <span style="color:red">deprecated</span> | String |  |  |  | ASN(asplain):local_admin or ASN(asdot):local_admin notation<span style="color:red">This key is deprecated. Support will be removed in AVD version 7.0.0. Use <samp><node_type_key>.defaults.evpn_gateway.d_path.local_domain_id_local or <node_type_key>.node_groups[].nodes[].evpn_gateway.d_path.local_domain_id_local or <node_type_key>.node_groups[].evpn_gateway.d_path.local_domain_id_local or <node_type_key>.nodes[].evpn_gateway.d_path.local_domain_id_local or device_profiles[].evpn_gateway.d_path.local_domain_id_local or devices[].evpn_gateway.d_path.local_domain_id_local</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_domain_id_remote</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].evpn_gateway.all_active_multihoming.evpn_domain_id_remote") <span style="color:red">deprecated</span> | String |  |  |  | ASN(asplain):local_admin or ASN(asdot):local_admin notation<span style="color:red">This key is deprecated. Support will be removed in AVD version 7.0.0. Use <samp><node_type_key>.defaults.evpn_gateway.d_path.remote_domain_id or <node_type_key>.node_groups[].nodes[].evpn_gateway.d_path.remote_domain_id or <node_type_key>.node_groups[].evpn_gateway.d_path.remote_domain_id or <node_type_key>.nodes[].evpn_gateway.d_path.remote_domain_id or device_profiles[].evpn_gateway.d_path.remote_domain_id or devices[].evpn_gateway.d_path.remote_domain_id</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_ethernet_segment</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].evpn_gateway.all_active_multihoming.evpn_ethernet_segment") | Dictionary | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;identifier</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].evpn_gateway.all_active_multihoming.evpn_ethernet_segment.identifier") | String | Required |  |  | EVPN Ethernet Segment Identifier (Type 1 format) |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rt_import</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].evpn_gateway.all_active_multihoming.evpn_ethernet_segment.rt_import") | String | Required |  |  | Low-order 6 bytes of ES-Import Route Target. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_gateway</samp>](## "<node_type_keys.key>.node_groups.[].evpn_gateway") | Dictionary |  |  |  | Node is acting as EVPN Multi-Domain Gateway.<br>New BGP peer-group is generated between EVPN GWs in different domains or between GWs and Route Servers.<br>Name can be changed under "bgp_peer_groups.evpn_overlay_core" variable.<br>L3 rechability for different EVPN GWs must be already in place, it is recommended to use DCI & L3 Edge if Route Servers and GWs are not defined under the same Ansible inventory.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remote_peers</samp>](## "<node_type_keys.key>.node_groups.[].evpn_gateway.remote_peers") | List, items: Dictionary |  |  |  | Define remote peers of the EVPN VXLAN Gateway.<br>If the hostname can be found in the inventory, ip_address and BGP ASN will be automatically populated. Manual override takes precedence.<br>If the peer's hostname can not be found in the inventory, ip_address and bgp_as must be defined.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;hostname</samp>](## "<node_type_keys.key>.node_groups.[].evpn_gateway.remote_peers.[].hostname") | String | Required, Unique |  |  | Hostname of remote EVPN GW server. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "<node_type_keys.key>.node_groups.[].evpn_gateway.remote_peers.[].ip_address") | String |  |  | Format: ipv4 | Peering IP of remote Route Server. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp_as</samp>](## "<node_type_keys.key>.node_groups.[].evpn_gateway.remote_peers.[].bgp_as") | String |  |  |  | Remote Route Server's BGP AS <1-4294967295> or AS number in asdot notation "<1-65535>.<0-65535>".<br>For asdot notation in YAML inputs, the value must be put in quotes, to prevent it from being interpreted as a float number. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_l2</samp>](## "<node_type_keys.key>.node_groups.[].evpn_gateway.evpn_l2") | Dictionary |  |  |  | Enable EVPN Gateway functionality for route-types 2 (MAC-IP) and 3 (IMET). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<node_type_keys.key>.node_groups.[].evpn_gateway.evpn_l2.enabled") | Boolean |  | `False` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_l3</samp>](## "<node_type_keys.key>.node_groups.[].evpn_gateway.evpn_l3") | Dictionary |  |  |  | Enable EVPN Gateway functionality for route-type 5 (IP-PREFIX). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<node_type_keys.key>.node_groups.[].evpn_gateway.evpn_l3.enabled") | Boolean |  | `False` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inter_domain</samp>](## "<node_type_keys.key>.node_groups.[].evpn_gateway.evpn_l3.inter_domain") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "<node_type_keys.key>.node_groups.[].evpn_gateway.evpn_l3.mode") | String |  | `next-hop-self` | Valid Values:<br>- <code>next-hop-self</code><br>- <code>rd-rt-rewrite</code> | Defines the rewriting mode for EVPN L3 inter-domain routing.<br>- next-hop-self: (default) Forward EVPN IP-Prefix routes by only replacing the next-hop to the gateway itself.<br>- rd-rt-rewrite: Re-export local EVPN IP-Prefix routes with the RD and export RTs of the remote domain and vice versa.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;d_path</samp>](## "<node_type_keys.key>.node_groups.[].evpn_gateway.d_path") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<node_type_keys.key>.node_groups.[].evpn_gateway.d_path.enabled") | Boolean |  | `True` |  | Enable D-path for use with BGP bestpath selection algorithm. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;local_domain_id</samp>](## "<node_type_keys.key>.node_groups.[].evpn_gateway.d_path.local_domain_id") | String | Required |  |  | ASN(asplain):local_admin or ASN(asdot):local_admin notation |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remote_domain_id</samp>](## "<node_type_keys.key>.node_groups.[].evpn_gateway.d_path.remote_domain_id") | String | Required |  |  | ASN(asplain):local_admin or ASN(asdot):local_admin notation |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;all_active_multihoming</samp>](## "<node_type_keys.key>.node_groups.[].evpn_gateway.all_active_multihoming") | Dictionary |  |  |  | Enable Active Active Multihoming architecture for EVPN Gateways.<br>Not supported with MLAG or IPVPN Gateway. Requires EVPN L3 inter-domain to be enabled. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<node_type_keys.key>.node_groups.[].evpn_gateway.all_active_multihoming.enabled") | Boolean | Required |  |  | Enable Active Active Multihoming resiliency model. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enable_d_path</samp>](## "<node_type_keys.key>.node_groups.[].evpn_gateway.all_active_multihoming.enable_d_path") <span style="color:red">deprecated</span> | Boolean |  | `True` |  | Enable D-path for use with BGP bestpath selection algorithm.<span style="color:red">This key is deprecated. Support will be removed in AVD version 7.0.0. Use <samp><node_type_key>.defaults.evpn_gateway.d_path.enabled or <node_type_key>.node_groups[].nodes[].evpn_gateway.d_path.enabled or <node_type_key>.node_groups[].evpn_gateway.d_path.enabled or <node_type_key>.nodes[].evpn_gateway.d_path.enabled or device_profiles[].evpn_gateway.d_path.enabled or devices[].evpn_gateway.d_path.enabled</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_domain_id_local</samp>](## "<node_type_keys.key>.node_groups.[].evpn_gateway.all_active_multihoming.evpn_domain_id_local") <span style="color:red">deprecated</span> | String |  |  |  | ASN(asplain):local_admin or ASN(asdot):local_admin notation<span style="color:red">This key is deprecated. Support will be removed in AVD version 7.0.0. Use <samp><node_type_key>.defaults.evpn_gateway.d_path.local_domain_id_local or <node_type_key>.node_groups[].nodes[].evpn_gateway.d_path.local_domain_id_local or <node_type_key>.node_groups[].evpn_gateway.d_path.local_domain_id_local or <node_type_key>.nodes[].evpn_gateway.d_path.local_domain_id_local or device_profiles[].evpn_gateway.d_path.local_domain_id_local or devices[].evpn_gateway.d_path.local_domain_id_local</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_domain_id_remote</samp>](## "<node_type_keys.key>.node_groups.[].evpn_gateway.all_active_multihoming.evpn_domain_id_remote") <span style="color:red">deprecated</span> | String |  |  |  | ASN(asplain):local_admin or ASN(asdot):local_admin notation<span style="color:red">This key is deprecated. Support will be removed in AVD version 7.0.0. Use <samp><node_type_key>.defaults.evpn_gateway.d_path.remote_domain_id or <node_type_key>.node_groups[].nodes[].evpn_gateway.d_path.remote_domain_id or <node_type_key>.node_groups[].evpn_gateway.d_path.remote_domain_id or <node_type_key>.nodes[].evpn_gateway.d_path.remote_domain_id or device_profiles[].evpn_gateway.d_path.remote_domain_id or devices[].evpn_gateway.d_path.remote_domain_id</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_ethernet_segment</samp>](## "<node_type_keys.key>.node_groups.[].evpn_gateway.all_active_multihoming.evpn_ethernet_segment") | Dictionary | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;identifier</samp>](## "<node_type_keys.key>.node_groups.[].evpn_gateway.all_active_multihoming.evpn_ethernet_segment.identifier") | String | Required |  |  | EVPN Ethernet Segment Identifier (Type 1 format) |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rt_import</samp>](## "<node_type_keys.key>.node_groups.[].evpn_gateway.all_active_multihoming.evpn_ethernet_segment.rt_import") | String | Required |  |  | Low-order 6 bytes of ES-Import Route Target. |
    | [<samp>&nbsp;&nbsp;nodes</samp>](## "<node_type_keys.key>.nodes") | List, items: Dictionary |  |  |  | Define variables per node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "<node_type_keys.key>.nodes.[].name") | String | Required, Unique |  |  | The Node Name is used as "hostname". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_gateway</samp>](## "<node_type_keys.key>.nodes.[].evpn_gateway") | Dictionary |  |  |  | Node is acting as EVPN Multi-Domain Gateway.<br>New BGP peer-group is generated between EVPN GWs in different domains or between GWs and Route Servers.<br>Name can be changed under "bgp_peer_groups.evpn_overlay_core" variable.<br>L3 rechability for different EVPN GWs must be already in place, it is recommended to use DCI & L3 Edge if Route Servers and GWs are not defined under the same Ansible inventory.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remote_peers</samp>](## "<node_type_keys.key>.nodes.[].evpn_gateway.remote_peers") | List, items: Dictionary |  |  |  | Define remote peers of the EVPN VXLAN Gateway.<br>If the hostname can be found in the inventory, ip_address and BGP ASN will be automatically populated. Manual override takes precedence.<br>If the peer's hostname can not be found in the inventory, ip_address and bgp_as must be defined.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;hostname</samp>](## "<node_type_keys.key>.nodes.[].evpn_gateway.remote_peers.[].hostname") | String | Required, Unique |  |  | Hostname of remote EVPN GW server. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "<node_type_keys.key>.nodes.[].evpn_gateway.remote_peers.[].ip_address") | String |  |  | Format: ipv4 | Peering IP of remote Route Server. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp_as</samp>](## "<node_type_keys.key>.nodes.[].evpn_gateway.remote_peers.[].bgp_as") | String |  |  |  | Remote Route Server's BGP AS <1-4294967295> or AS number in asdot notation "<1-65535>.<0-65535>".<br>For asdot notation in YAML inputs, the value must be put in quotes, to prevent it from being interpreted as a float number. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_l2</samp>](## "<node_type_keys.key>.nodes.[].evpn_gateway.evpn_l2") | Dictionary |  |  |  | Enable EVPN Gateway functionality for route-types 2 (MAC-IP) and 3 (IMET). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<node_type_keys.key>.nodes.[].evpn_gateway.evpn_l2.enabled") | Boolean |  | `False` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_l3</samp>](## "<node_type_keys.key>.nodes.[].evpn_gateway.evpn_l3") | Dictionary |  |  |  | Enable EVPN Gateway functionality for route-type 5 (IP-PREFIX). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<node_type_keys.key>.nodes.[].evpn_gateway.evpn_l3.enabled") | Boolean |  | `False` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inter_domain</samp>](## "<node_type_keys.key>.nodes.[].evpn_gateway.evpn_l3.inter_domain") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "<node_type_keys.key>.nodes.[].evpn_gateway.evpn_l3.mode") | String |  | `next-hop-self` | Valid Values:<br>- <code>next-hop-self</code><br>- <code>rd-rt-rewrite</code> | Defines the rewriting mode for EVPN L3 inter-domain routing.<br>- next-hop-self: (default) Forward EVPN IP-Prefix routes by only replacing the next-hop to the gateway itself.<br>- rd-rt-rewrite: Re-export local EVPN IP-Prefix routes with the RD and export RTs of the remote domain and vice versa.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;d_path</samp>](## "<node_type_keys.key>.nodes.[].evpn_gateway.d_path") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<node_type_keys.key>.nodes.[].evpn_gateway.d_path.enabled") | Boolean |  | `True` |  | Enable D-path for use with BGP bestpath selection algorithm. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;local_domain_id</samp>](## "<node_type_keys.key>.nodes.[].evpn_gateway.d_path.local_domain_id") | String | Required |  |  | ASN(asplain):local_admin or ASN(asdot):local_admin notation |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remote_domain_id</samp>](## "<node_type_keys.key>.nodes.[].evpn_gateway.d_path.remote_domain_id") | String | Required |  |  | ASN(asplain):local_admin or ASN(asdot):local_admin notation |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;all_active_multihoming</samp>](## "<node_type_keys.key>.nodes.[].evpn_gateway.all_active_multihoming") | Dictionary |  |  |  | Enable Active Active Multihoming architecture for EVPN Gateways.<br>Not supported with MLAG or IPVPN Gateway. Requires EVPN L3 inter-domain to be enabled. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<node_type_keys.key>.nodes.[].evpn_gateway.all_active_multihoming.enabled") | Boolean | Required |  |  | Enable Active Active Multihoming resiliency model. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enable_d_path</samp>](## "<node_type_keys.key>.nodes.[].evpn_gateway.all_active_multihoming.enable_d_path") <span style="color:red">deprecated</span> | Boolean |  | `True` |  | Enable D-path for use with BGP bestpath selection algorithm.<span style="color:red">This key is deprecated. Support will be removed in AVD version 7.0.0. Use <samp><node_type_key>.defaults.evpn_gateway.d_path.enabled or <node_type_key>.node_groups[].nodes[].evpn_gateway.d_path.enabled or <node_type_key>.node_groups[].evpn_gateway.d_path.enabled or <node_type_key>.nodes[].evpn_gateway.d_path.enabled or device_profiles[].evpn_gateway.d_path.enabled or devices[].evpn_gateway.d_path.enabled</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_domain_id_local</samp>](## "<node_type_keys.key>.nodes.[].evpn_gateway.all_active_multihoming.evpn_domain_id_local") <span style="color:red">deprecated</span> | String |  |  |  | ASN(asplain):local_admin or ASN(asdot):local_admin notation<span style="color:red">This key is deprecated. Support will be removed in AVD version 7.0.0. Use <samp><node_type_key>.defaults.evpn_gateway.d_path.local_domain_id_local or <node_type_key>.node_groups[].nodes[].evpn_gateway.d_path.local_domain_id_local or <node_type_key>.node_groups[].evpn_gateway.d_path.local_domain_id_local or <node_type_key>.nodes[].evpn_gateway.d_path.local_domain_id_local or device_profiles[].evpn_gateway.d_path.local_domain_id_local or devices[].evpn_gateway.d_path.local_domain_id_local</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_domain_id_remote</samp>](## "<node_type_keys.key>.nodes.[].evpn_gateway.all_active_multihoming.evpn_domain_id_remote") <span style="color:red">deprecated</span> | String |  |  |  | ASN(asplain):local_admin or ASN(asdot):local_admin notation<span style="color:red">This key is deprecated. Support will be removed in AVD version 7.0.0. Use <samp><node_type_key>.defaults.evpn_gateway.d_path.remote_domain_id or <node_type_key>.node_groups[].nodes[].evpn_gateway.d_path.remote_domain_id or <node_type_key>.node_groups[].evpn_gateway.d_path.remote_domain_id or <node_type_key>.nodes[].evpn_gateway.d_path.remote_domain_id or device_profiles[].evpn_gateway.d_path.remote_domain_id or devices[].evpn_gateway.d_path.remote_domain_id</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_ethernet_segment</samp>](## "<node_type_keys.key>.nodes.[].evpn_gateway.all_active_multihoming.evpn_ethernet_segment") | Dictionary | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;identifier</samp>](## "<node_type_keys.key>.nodes.[].evpn_gateway.all_active_multihoming.evpn_ethernet_segment.identifier") | String | Required |  |  | EVPN Ethernet Segment Identifier (Type 1 format) |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rt_import</samp>](## "<node_type_keys.key>.nodes.[].evpn_gateway.all_active_multihoming.evpn_ethernet_segment.rt_import") | String | Required |  |  | Low-order 6 bytes of ES-Import Route Target. |
    | [<samp>device_profiles</samp>](## "device_profiles") | List, items: Dictionary |  |  |  | PREVIEW - This datamodel is still under development and may change or get removed at any time. |
    | [<samp>&nbsp;&nbsp;-&nbsp;name</samp>](## "device_profiles.[].name") | String | Required, Unique |  |  | Profile Name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;evpn_gateway</samp>](## "device_profiles.[].evpn_gateway") | Dictionary |  |  |  | Node is acting as EVPN Multi-Domain Gateway.<br>New BGP peer-group is generated between EVPN GWs in different domains or between GWs and Route Servers.<br>Name can be changed under "bgp_peer_groups.evpn_overlay_core" variable.<br>L3 rechability for different EVPN GWs must be already in place, it is recommended to use DCI & L3 Edge if Route Servers and GWs are not defined under the same Ansible inventory.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remote_peers</samp>](## "device_profiles.[].evpn_gateway.remote_peers") | List, items: Dictionary |  |  |  | Define remote peers of the EVPN VXLAN Gateway.<br>If the hostname can be found in the inventory, ip_address and BGP ASN will be automatically populated. Manual override takes precedence.<br>If the peer's hostname can not be found in the inventory, ip_address and bgp_as must be defined.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;hostname</samp>](## "device_profiles.[].evpn_gateway.remote_peers.[].hostname") | String | Required, Unique |  |  | Hostname of remote EVPN GW server. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "device_profiles.[].evpn_gateway.remote_peers.[].ip_address") | String |  |  | Format: ipv4 | Peering IP of remote Route Server. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp_as</samp>](## "device_profiles.[].evpn_gateway.remote_peers.[].bgp_as") | String |  |  |  | Remote Route Server's BGP AS <1-4294967295> or AS number in asdot notation "<1-65535>.<0-65535>".<br>For asdot notation in YAML inputs, the value must be put in quotes, to prevent it from being interpreted as a float number. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_l2</samp>](## "device_profiles.[].evpn_gateway.evpn_l2") | Dictionary |  |  |  | Enable EVPN Gateway functionality for route-types 2 (MAC-IP) and 3 (IMET). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "device_profiles.[].evpn_gateway.evpn_l2.enabled") | Boolean |  | `False` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_l3</samp>](## "device_profiles.[].evpn_gateway.evpn_l3") | Dictionary |  |  |  | Enable EVPN Gateway functionality for route-type 5 (IP-PREFIX). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "device_profiles.[].evpn_gateway.evpn_l3.enabled") | Boolean |  | `False` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inter_domain</samp>](## "device_profiles.[].evpn_gateway.evpn_l3.inter_domain") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "device_profiles.[].evpn_gateway.evpn_l3.mode") | String |  | `next-hop-self` | Valid Values:<br>- <code>next-hop-self</code><br>- <code>rd-rt-rewrite</code> | Defines the rewriting mode for EVPN L3 inter-domain routing.<br>- next-hop-self: (default) Forward EVPN IP-Prefix routes by only replacing the next-hop to the gateway itself.<br>- rd-rt-rewrite: Re-export local EVPN IP-Prefix routes with the RD and export RTs of the remote domain and vice versa.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;d_path</samp>](## "device_profiles.[].evpn_gateway.d_path") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "device_profiles.[].evpn_gateway.d_path.enabled") | Boolean |  | `True` |  | Enable D-path for use with BGP bestpath selection algorithm. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;local_domain_id</samp>](## "device_profiles.[].evpn_gateway.d_path.local_domain_id") | String | Required |  |  | ASN(asplain):local_admin or ASN(asdot):local_admin notation |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remote_domain_id</samp>](## "device_profiles.[].evpn_gateway.d_path.remote_domain_id") | String | Required |  |  | ASN(asplain):local_admin or ASN(asdot):local_admin notation |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;all_active_multihoming</samp>](## "device_profiles.[].evpn_gateway.all_active_multihoming") | Dictionary |  |  |  | Enable Active Active Multihoming architecture for EVPN Gateways.<br>Not supported with MLAG or IPVPN Gateway. Requires EVPN L3 inter-domain to be enabled. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "device_profiles.[].evpn_gateway.all_active_multihoming.enabled") | Boolean | Required |  |  | Enable Active Active Multihoming resiliency model. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enable_d_path</samp>](## "device_profiles.[].evpn_gateway.all_active_multihoming.enable_d_path") <span style="color:red">deprecated</span> | Boolean |  | `True` |  | Enable D-path for use with BGP bestpath selection algorithm.<span style="color:red">This key is deprecated. Support will be removed in AVD version 7.0.0. Use <samp><node_type_key>.defaults.evpn_gateway.d_path.enabled or <node_type_key>.node_groups[].nodes[].evpn_gateway.d_path.enabled or <node_type_key>.node_groups[].evpn_gateway.d_path.enabled or <node_type_key>.nodes[].evpn_gateway.d_path.enabled or device_profiles[].evpn_gateway.d_path.enabled or devices[].evpn_gateway.d_path.enabled</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_domain_id_local</samp>](## "device_profiles.[].evpn_gateway.all_active_multihoming.evpn_domain_id_local") <span style="color:red">deprecated</span> | String |  |  |  | ASN(asplain):local_admin or ASN(asdot):local_admin notation<span style="color:red">This key is deprecated. Support will be removed in AVD version 7.0.0. Use <samp><node_type_key>.defaults.evpn_gateway.d_path.local_domain_id_local or <node_type_key>.node_groups[].nodes[].evpn_gateway.d_path.local_domain_id_local or <node_type_key>.node_groups[].evpn_gateway.d_path.local_domain_id_local or <node_type_key>.nodes[].evpn_gateway.d_path.local_domain_id_local or device_profiles[].evpn_gateway.d_path.local_domain_id_local or devices[].evpn_gateway.d_path.local_domain_id_local</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_domain_id_remote</samp>](## "device_profiles.[].evpn_gateway.all_active_multihoming.evpn_domain_id_remote") <span style="color:red">deprecated</span> | String |  |  |  | ASN(asplain):local_admin or ASN(asdot):local_admin notation<span style="color:red">This key is deprecated. Support will be removed in AVD version 7.0.0. Use <samp><node_type_key>.defaults.evpn_gateway.d_path.remote_domain_id or <node_type_key>.node_groups[].nodes[].evpn_gateway.d_path.remote_domain_id or <node_type_key>.node_groups[].evpn_gateway.d_path.remote_domain_id or <node_type_key>.nodes[].evpn_gateway.d_path.remote_domain_id or device_profiles[].evpn_gateway.d_path.remote_domain_id or devices[].evpn_gateway.d_path.remote_domain_id</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_ethernet_segment</samp>](## "device_profiles.[].evpn_gateway.all_active_multihoming.evpn_ethernet_segment") | Dictionary | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;identifier</samp>](## "device_profiles.[].evpn_gateway.all_active_multihoming.evpn_ethernet_segment.identifier") | String | Required |  |  | EVPN Ethernet Segment Identifier (Type 1 format) |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rt_import</samp>](## "device_profiles.[].evpn_gateway.all_active_multihoming.evpn_ethernet_segment.rt_import") | String | Required |  |  | Low-order 6 bytes of ES-Import Route Target. |
    | [<samp>devices</samp>](## "devices") | List, items: Dictionary |  |  |  | PREVIEW - This datamodel is still under development and may change or get removed at any time. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "devices.[].name") | String | Required, Unique |  |  | The Node Name is used as "hostname". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;evpn_gateway</samp>](## "devices.[].evpn_gateway") | Dictionary |  |  |  | Node is acting as EVPN Multi-Domain Gateway.<br>New BGP peer-group is generated between EVPN GWs in different domains or between GWs and Route Servers.<br>Name can be changed under "bgp_peer_groups.evpn_overlay_core" variable.<br>L3 rechability for different EVPN GWs must be already in place, it is recommended to use DCI & L3 Edge if Route Servers and GWs are not defined under the same Ansible inventory.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remote_peers</samp>](## "devices.[].evpn_gateway.remote_peers") | List, items: Dictionary |  |  |  | Define remote peers of the EVPN VXLAN Gateway.<br>If the hostname can be found in the inventory, ip_address and BGP ASN will be automatically populated. Manual override takes precedence.<br>If the peer's hostname can not be found in the inventory, ip_address and bgp_as must be defined.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;hostname</samp>](## "devices.[].evpn_gateway.remote_peers.[].hostname") | String | Required, Unique |  |  | Hostname of remote EVPN GW server. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "devices.[].evpn_gateway.remote_peers.[].ip_address") | String |  |  | Format: ipv4 | Peering IP of remote Route Server. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp_as</samp>](## "devices.[].evpn_gateway.remote_peers.[].bgp_as") | String |  |  |  | Remote Route Server's BGP AS <1-4294967295> or AS number in asdot notation "<1-65535>.<0-65535>".<br>For asdot notation in YAML inputs, the value must be put in quotes, to prevent it from being interpreted as a float number. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_l2</samp>](## "devices.[].evpn_gateway.evpn_l2") | Dictionary |  |  |  | Enable EVPN Gateway functionality for route-types 2 (MAC-IP) and 3 (IMET). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "devices.[].evpn_gateway.evpn_l2.enabled") | Boolean |  | `False` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_l3</samp>](## "devices.[].evpn_gateway.evpn_l3") | Dictionary |  |  |  | Enable EVPN Gateway functionality for route-type 5 (IP-PREFIX). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "devices.[].evpn_gateway.evpn_l3.enabled") | Boolean |  | `False` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inter_domain</samp>](## "devices.[].evpn_gateway.evpn_l3.inter_domain") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "devices.[].evpn_gateway.evpn_l3.mode") | String |  | `next-hop-self` | Valid Values:<br>- <code>next-hop-self</code><br>- <code>rd-rt-rewrite</code> | Defines the rewriting mode for EVPN L3 inter-domain routing.<br>- next-hop-self: (default) Forward EVPN IP-Prefix routes by only replacing the next-hop to the gateway itself.<br>- rd-rt-rewrite: Re-export local EVPN IP-Prefix routes with the RD and export RTs of the remote domain and vice versa.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;d_path</samp>](## "devices.[].evpn_gateway.d_path") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "devices.[].evpn_gateway.d_path.enabled") | Boolean |  | `True` |  | Enable D-path for use with BGP bestpath selection algorithm. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;local_domain_id</samp>](## "devices.[].evpn_gateway.d_path.local_domain_id") | String | Required |  |  | ASN(asplain):local_admin or ASN(asdot):local_admin notation |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remote_domain_id</samp>](## "devices.[].evpn_gateway.d_path.remote_domain_id") | String | Required |  |  | ASN(asplain):local_admin or ASN(asdot):local_admin notation |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;all_active_multihoming</samp>](## "devices.[].evpn_gateway.all_active_multihoming") | Dictionary |  |  |  | Enable Active Active Multihoming architecture for EVPN Gateways.<br>Not supported with MLAG or IPVPN Gateway. Requires EVPN L3 inter-domain to be enabled. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "devices.[].evpn_gateway.all_active_multihoming.enabled") | Boolean | Required |  |  | Enable Active Active Multihoming resiliency model. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enable_d_path</samp>](## "devices.[].evpn_gateway.all_active_multihoming.enable_d_path") <span style="color:red">deprecated</span> | Boolean |  | `True` |  | Enable D-path for use with BGP bestpath selection algorithm.<span style="color:red">This key is deprecated. Support will be removed in AVD version 7.0.0. Use <samp><node_type_key>.defaults.evpn_gateway.d_path.enabled or <node_type_key>.node_groups[].nodes[].evpn_gateway.d_path.enabled or <node_type_key>.node_groups[].evpn_gateway.d_path.enabled or <node_type_key>.nodes[].evpn_gateway.d_path.enabled or device_profiles[].evpn_gateway.d_path.enabled or devices[].evpn_gateway.d_path.enabled</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_domain_id_local</samp>](## "devices.[].evpn_gateway.all_active_multihoming.evpn_domain_id_local") <span style="color:red">deprecated</span> | String |  |  |  | ASN(asplain):local_admin or ASN(asdot):local_admin notation<span style="color:red">This key is deprecated. Support will be removed in AVD version 7.0.0. Use <samp><node_type_key>.defaults.evpn_gateway.d_path.local_domain_id_local or <node_type_key>.node_groups[].nodes[].evpn_gateway.d_path.local_domain_id_local or <node_type_key>.node_groups[].evpn_gateway.d_path.local_domain_id_local or <node_type_key>.nodes[].evpn_gateway.d_path.local_domain_id_local or device_profiles[].evpn_gateway.d_path.local_domain_id_local or devices[].evpn_gateway.d_path.local_domain_id_local</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_domain_id_remote</samp>](## "devices.[].evpn_gateway.all_active_multihoming.evpn_domain_id_remote") <span style="color:red">deprecated</span> | String |  |  |  | ASN(asplain):local_admin or ASN(asdot):local_admin notation<span style="color:red">This key is deprecated. Support will be removed in AVD version 7.0.0. Use <samp><node_type_key>.defaults.evpn_gateway.d_path.remote_domain_id or <node_type_key>.node_groups[].nodes[].evpn_gateway.d_path.remote_domain_id or <node_type_key>.node_groups[].evpn_gateway.d_path.remote_domain_id or <node_type_key>.nodes[].evpn_gateway.d_path.remote_domain_id or device_profiles[].evpn_gateway.d_path.remote_domain_id or devices[].evpn_gateway.d_path.remote_domain_id</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_ethernet_segment</samp>](## "devices.[].evpn_gateway.all_active_multihoming.evpn_ethernet_segment") | Dictionary | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;identifier</samp>](## "devices.[].evpn_gateway.all_active_multihoming.evpn_ethernet_segment.identifier") | String | Required |  |  | EVPN Ethernet Segment Identifier (Type 1 format) |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rt_import</samp>](## "devices.[].evpn_gateway.all_active_multihoming.evpn_ethernet_segment.rt_import") | String | Required |  |  | Low-order 6 bytes of ES-Import Route Target. |

=== "YAML"

    ```yaml
    <node_type_keys.key>:

      # Define variables for all nodes of this type.
      defaults:

        # Node is acting as EVPN Multi-Domain Gateway.
        # New BGP peer-group is generated between EVPN GWs in different domains or between GWs and Route Servers.
        # Name can be changed under "bgp_peer_groups.evpn_overlay_core" variable.
        # L3 rechability for different EVPN GWs must be already in place, it is recommended to use DCI & L3 Edge if Route Servers and GWs are not defined under the same Ansible inventory.
        evpn_gateway:

          # Define remote peers of the EVPN VXLAN Gateway.
          # If the hostname can be found in the inventory, ip_address and BGP ASN will be automatically populated. Manual override takes precedence.
          # If the peer's hostname can not be found in the inventory, ip_address and bgp_as must be defined.
          remote_peers:

              # Hostname of remote EVPN GW server.
            - hostname: <str; required; unique>

              # Peering IP of remote Route Server.
              ip_address: <str>

              # Remote Route Server's BGP AS <1-4294967295> or AS number in asdot notation "<1-65535>.<0-65535>".
              # For asdot notation in YAML inputs, the value must be put in quotes, to prevent it from being interpreted as a float number.
              bgp_as: <str>

          # Enable EVPN Gateway functionality for route-types 2 (MAC-IP) and 3 (IMET).
          evpn_l2:
            enabled: <bool; default=False>

          # Enable EVPN Gateway functionality for route-type 5 (IP-PREFIX).
          evpn_l3:
            enabled: <bool; default=False>
            inter_domain: <bool; default=True>

            # Defines the rewriting mode for EVPN L3 inter-domain routing.
            # - next-hop-self: (default) Forward EVPN IP-Prefix routes by only replacing the next-hop to the gateway itself.
            # - rd-rt-rewrite: Re-export local EVPN IP-Prefix routes with the RD and export RTs of the remote domain and vice versa.
            mode: <str; "next-hop-self" | "rd-rt-rewrite"; default="next-hop-self">
          d_path:

            # Enable D-path for use with BGP bestpath selection algorithm.
            enabled: <bool; default=True>

            # ASN(asplain):local_admin or ASN(asdot):local_admin notation
            local_domain_id: <str; required>

            # ASN(asplain):local_admin or ASN(asdot):local_admin notation
            remote_domain_id: <str; required>

          # Enable Active Active Multihoming architecture for EVPN Gateways.
          # Not supported with MLAG or IPVPN Gateway. Requires EVPN L3 inter-domain to be enabled.
          all_active_multihoming:

            # Enable Active Active Multihoming resiliency model.
            enabled: <bool; required>

            # Enable D-path for use with BGP bestpath selection algorithm.
            # This key is deprecated.
            # Support will be removed in AVD version 7.0.0.
            # Use `<node_type_key>.defaults.evpn_gateway.d_path.enabled` or `<node_type_key>.node_groups[].nodes[].evpn_gateway.d_path.enabled` or `<node_type_key>.node_groups[].evpn_gateway.d_path.enabled` or `<node_type_key>.nodes[].evpn_gateway.d_path.enabled` or `device_profiles[].evpn_gateway.d_path.enabled` or `devices[].evpn_gateway.d_path.enabled` instead.
            enable_d_path: <bool; default=True>

            # ASN(asplain):local_admin or ASN(asdot):local_admin notation
            # This key is deprecated.
            # Support will be removed in AVD version 7.0.0.
            # Use `<node_type_key>.defaults.evpn_gateway.d_path.local_domain_id_local` or `<node_type_key>.node_groups[].nodes[].evpn_gateway.d_path.local_domain_id_local` or `<node_type_key>.node_groups[].evpn_gateway.d_path.local_domain_id_local` or `<node_type_key>.nodes[].evpn_gateway.d_path.local_domain_id_local` or `device_profiles[].evpn_gateway.d_path.local_domain_id_local` or `devices[].evpn_gateway.d_path.local_domain_id_local` instead.
            evpn_domain_id_local: <str>

            # ASN(asplain):local_admin or ASN(asdot):local_admin notation
            # This key is deprecated.
            # Support will be removed in AVD version 7.0.0.
            # Use `<node_type_key>.defaults.evpn_gateway.d_path.remote_domain_id` or `<node_type_key>.node_groups[].nodes[].evpn_gateway.d_path.remote_domain_id` or `<node_type_key>.node_groups[].evpn_gateway.d_path.remote_domain_id` or `<node_type_key>.nodes[].evpn_gateway.d_path.remote_domain_id` or `device_profiles[].evpn_gateway.d_path.remote_domain_id` or `devices[].evpn_gateway.d_path.remote_domain_id` instead.
            evpn_domain_id_remote: <str>
            evpn_ethernet_segment: # required

              # EVPN Ethernet Segment Identifier (Type 1 format)
              identifier: <str; required>

              # Low-order 6 bytes of ES-Import Route Target.
              rt_import: <str; required>

      # Define variables related to all nodes part of this group.
      node_groups:

          # The Node Group Name is used for MLAG domain unless set with 'mlag_domain_id'.
          # The Node Group Name is also used for peer description on downstream switches' uplinks.
        - group: <str; required; unique>

          # Define variables per node.
          nodes:

              # The Node Name is used as "hostname".
            - name: <str; required; unique>

              # Node is acting as EVPN Multi-Domain Gateway.
              # New BGP peer-group is generated between EVPN GWs in different domains or between GWs and Route Servers.
              # Name can be changed under "bgp_peer_groups.evpn_overlay_core" variable.
              # L3 rechability for different EVPN GWs must be already in place, it is recommended to use DCI & L3 Edge if Route Servers and GWs are not defined under the same Ansible inventory.
              evpn_gateway:

                # Define remote peers of the EVPN VXLAN Gateway.
                # If the hostname can be found in the inventory, ip_address and BGP ASN will be automatically populated. Manual override takes precedence.
                # If the peer's hostname can not be found in the inventory, ip_address and bgp_as must be defined.
                remote_peers:

                    # Hostname of remote EVPN GW server.
                  - hostname: <str; required; unique>

                    # Peering IP of remote Route Server.
                    ip_address: <str>

                    # Remote Route Server's BGP AS <1-4294967295> or AS number in asdot notation "<1-65535>.<0-65535>".
                    # For asdot notation in YAML inputs, the value must be put in quotes, to prevent it from being interpreted as a float number.
                    bgp_as: <str>

                # Enable EVPN Gateway functionality for route-types 2 (MAC-IP) and 3 (IMET).
                evpn_l2:
                  enabled: <bool; default=False>

                # Enable EVPN Gateway functionality for route-type 5 (IP-PREFIX).
                evpn_l3:
                  enabled: <bool; default=False>
                  inter_domain: <bool; default=True>

                  # Defines the rewriting mode for EVPN L3 inter-domain routing.
                  # - next-hop-self: (default) Forward EVPN IP-Prefix routes by only replacing the next-hop to the gateway itself.
                  # - rd-rt-rewrite: Re-export local EVPN IP-Prefix routes with the RD and export RTs of the remote domain and vice versa.
                  mode: <str; "next-hop-self" | "rd-rt-rewrite"; default="next-hop-self">
                d_path:

                  # Enable D-path for use with BGP bestpath selection algorithm.
                  enabled: <bool; default=True>

                  # ASN(asplain):local_admin or ASN(asdot):local_admin notation
                  local_domain_id: <str; required>

                  # ASN(asplain):local_admin or ASN(asdot):local_admin notation
                  remote_domain_id: <str; required>

                # Enable Active Active Multihoming architecture for EVPN Gateways.
                # Not supported with MLAG or IPVPN Gateway. Requires EVPN L3 inter-domain to be enabled.
                all_active_multihoming:

                  # Enable Active Active Multihoming resiliency model.
                  enabled: <bool; required>

                  # Enable D-path for use with BGP bestpath selection algorithm.
                  # This key is deprecated.
                  # Support will be removed in AVD version 7.0.0.
                  # Use `<node_type_key>.defaults.evpn_gateway.d_path.enabled` or `<node_type_key>.node_groups[].nodes[].evpn_gateway.d_path.enabled` or `<node_type_key>.node_groups[].evpn_gateway.d_path.enabled` or `<node_type_key>.nodes[].evpn_gateway.d_path.enabled` or `device_profiles[].evpn_gateway.d_path.enabled` or `devices[].evpn_gateway.d_path.enabled` instead.
                  enable_d_path: <bool; default=True>

                  # ASN(asplain):local_admin or ASN(asdot):local_admin notation
                  # This key is deprecated.
                  # Support will be removed in AVD version 7.0.0.
                  # Use `<node_type_key>.defaults.evpn_gateway.d_path.local_domain_id_local` or `<node_type_key>.node_groups[].nodes[].evpn_gateway.d_path.local_domain_id_local` or `<node_type_key>.node_groups[].evpn_gateway.d_path.local_domain_id_local` or `<node_type_key>.nodes[].evpn_gateway.d_path.local_domain_id_local` or `device_profiles[].evpn_gateway.d_path.local_domain_id_local` or `devices[].evpn_gateway.d_path.local_domain_id_local` instead.
                  evpn_domain_id_local: <str>

                  # ASN(asplain):local_admin or ASN(asdot):local_admin notation
                  # This key is deprecated.
                  # Support will be removed in AVD version 7.0.0.
                  # Use `<node_type_key>.defaults.evpn_gateway.d_path.remote_domain_id` or `<node_type_key>.node_groups[].nodes[].evpn_gateway.d_path.remote_domain_id` or `<node_type_key>.node_groups[].evpn_gateway.d_path.remote_domain_id` or `<node_type_key>.nodes[].evpn_gateway.d_path.remote_domain_id` or `device_profiles[].evpn_gateway.d_path.remote_domain_id` or `devices[].evpn_gateway.d_path.remote_domain_id` instead.
                  evpn_domain_id_remote: <str>
                  evpn_ethernet_segment: # required

                    # EVPN Ethernet Segment Identifier (Type 1 format)
                    identifier: <str; required>

                    # Low-order 6 bytes of ES-Import Route Target.
                    rt_import: <str; required>

          # Node is acting as EVPN Multi-Domain Gateway.
          # New BGP peer-group is generated between EVPN GWs in different domains or between GWs and Route Servers.
          # Name can be changed under "bgp_peer_groups.evpn_overlay_core" variable.
          # L3 rechability for different EVPN GWs must be already in place, it is recommended to use DCI & L3 Edge if Route Servers and GWs are not defined under the same Ansible inventory.
          evpn_gateway:

            # Define remote peers of the EVPN VXLAN Gateway.
            # If the hostname can be found in the inventory, ip_address and BGP ASN will be automatically populated. Manual override takes precedence.
            # If the peer's hostname can not be found in the inventory, ip_address and bgp_as must be defined.
            remote_peers:

                # Hostname of remote EVPN GW server.
              - hostname: <str; required; unique>

                # Peering IP of remote Route Server.
                ip_address: <str>

                # Remote Route Server's BGP AS <1-4294967295> or AS number in asdot notation "<1-65535>.<0-65535>".
                # For asdot notation in YAML inputs, the value must be put in quotes, to prevent it from being interpreted as a float number.
                bgp_as: <str>

            # Enable EVPN Gateway functionality for route-types 2 (MAC-IP) and 3 (IMET).
            evpn_l2:
              enabled: <bool; default=False>

            # Enable EVPN Gateway functionality for route-type 5 (IP-PREFIX).
            evpn_l3:
              enabled: <bool; default=False>
              inter_domain: <bool; default=True>

              # Defines the rewriting mode for EVPN L3 inter-domain routing.
              # - next-hop-self: (default) Forward EVPN IP-Prefix routes by only replacing the next-hop to the gateway itself.
              # - rd-rt-rewrite: Re-export local EVPN IP-Prefix routes with the RD and export RTs of the remote domain and vice versa.
              mode: <str; "next-hop-self" | "rd-rt-rewrite"; default="next-hop-self">
            d_path:

              # Enable D-path for use with BGP bestpath selection algorithm.
              enabled: <bool; default=True>

              # ASN(asplain):local_admin or ASN(asdot):local_admin notation
              local_domain_id: <str; required>

              # ASN(asplain):local_admin or ASN(asdot):local_admin notation
              remote_domain_id: <str; required>

            # Enable Active Active Multihoming architecture for EVPN Gateways.
            # Not supported with MLAG or IPVPN Gateway. Requires EVPN L3 inter-domain to be enabled.
            all_active_multihoming:

              # Enable Active Active Multihoming resiliency model.
              enabled: <bool; required>

              # Enable D-path for use with BGP bestpath selection algorithm.
              # This key is deprecated.
              # Support will be removed in AVD version 7.0.0.
              # Use `<node_type_key>.defaults.evpn_gateway.d_path.enabled` or `<node_type_key>.node_groups[].nodes[].evpn_gateway.d_path.enabled` or `<node_type_key>.node_groups[].evpn_gateway.d_path.enabled` or `<node_type_key>.nodes[].evpn_gateway.d_path.enabled` or `device_profiles[].evpn_gateway.d_path.enabled` or `devices[].evpn_gateway.d_path.enabled` instead.
              enable_d_path: <bool; default=True>

              # ASN(asplain):local_admin or ASN(asdot):local_admin notation
              # This key is deprecated.
              # Support will be removed in AVD version 7.0.0.
              # Use `<node_type_key>.defaults.evpn_gateway.d_path.local_domain_id_local` or `<node_type_key>.node_groups[].nodes[].evpn_gateway.d_path.local_domain_id_local` or `<node_type_key>.node_groups[].evpn_gateway.d_path.local_domain_id_local` or `<node_type_key>.nodes[].evpn_gateway.d_path.local_domain_id_local` or `device_profiles[].evpn_gateway.d_path.local_domain_id_local` or `devices[].evpn_gateway.d_path.local_domain_id_local` instead.
              evpn_domain_id_local: <str>

              # ASN(asplain):local_admin or ASN(asdot):local_admin notation
              # This key is deprecated.
              # Support will be removed in AVD version 7.0.0.
              # Use `<node_type_key>.defaults.evpn_gateway.d_path.remote_domain_id` or `<node_type_key>.node_groups[].nodes[].evpn_gateway.d_path.remote_domain_id` or `<node_type_key>.node_groups[].evpn_gateway.d_path.remote_domain_id` or `<node_type_key>.nodes[].evpn_gateway.d_path.remote_domain_id` or `device_profiles[].evpn_gateway.d_path.remote_domain_id` or `devices[].evpn_gateway.d_path.remote_domain_id` instead.
              evpn_domain_id_remote: <str>
              evpn_ethernet_segment: # required

                # EVPN Ethernet Segment Identifier (Type 1 format)
                identifier: <str; required>

                # Low-order 6 bytes of ES-Import Route Target.
                rt_import: <str; required>

      # Define variables per node.
      nodes:

          # The Node Name is used as "hostname".
        - name: <str; required; unique>

          # Node is acting as EVPN Multi-Domain Gateway.
          # New BGP peer-group is generated between EVPN GWs in different domains or between GWs and Route Servers.
          # Name can be changed under "bgp_peer_groups.evpn_overlay_core" variable.
          # L3 rechability for different EVPN GWs must be already in place, it is recommended to use DCI & L3 Edge if Route Servers and GWs are not defined under the same Ansible inventory.
          evpn_gateway:

            # Define remote peers of the EVPN VXLAN Gateway.
            # If the hostname can be found in the inventory, ip_address and BGP ASN will be automatically populated. Manual override takes precedence.
            # If the peer's hostname can not be found in the inventory, ip_address and bgp_as must be defined.
            remote_peers:

                # Hostname of remote EVPN GW server.
              - hostname: <str; required; unique>

                # Peering IP of remote Route Server.
                ip_address: <str>

                # Remote Route Server's BGP AS <1-4294967295> or AS number in asdot notation "<1-65535>.<0-65535>".
                # For asdot notation in YAML inputs, the value must be put in quotes, to prevent it from being interpreted as a float number.
                bgp_as: <str>

            # Enable EVPN Gateway functionality for route-types 2 (MAC-IP) and 3 (IMET).
            evpn_l2:
              enabled: <bool; default=False>

            # Enable EVPN Gateway functionality for route-type 5 (IP-PREFIX).
            evpn_l3:
              enabled: <bool; default=False>
              inter_domain: <bool; default=True>

              # Defines the rewriting mode for EVPN L3 inter-domain routing.
              # - next-hop-self: (default) Forward EVPN IP-Prefix routes by only replacing the next-hop to the gateway itself.
              # - rd-rt-rewrite: Re-export local EVPN IP-Prefix routes with the RD and export RTs of the remote domain and vice versa.
              mode: <str; "next-hop-self" | "rd-rt-rewrite"; default="next-hop-self">
            d_path:

              # Enable D-path for use with BGP bestpath selection algorithm.
              enabled: <bool; default=True>

              # ASN(asplain):local_admin or ASN(asdot):local_admin notation
              local_domain_id: <str; required>

              # ASN(asplain):local_admin or ASN(asdot):local_admin notation
              remote_domain_id: <str; required>

            # Enable Active Active Multihoming architecture for EVPN Gateways.
            # Not supported with MLAG or IPVPN Gateway. Requires EVPN L3 inter-domain to be enabled.
            all_active_multihoming:

              # Enable Active Active Multihoming resiliency model.
              enabled: <bool; required>

              # Enable D-path for use with BGP bestpath selection algorithm.
              # This key is deprecated.
              # Support will be removed in AVD version 7.0.0.
              # Use `<node_type_key>.defaults.evpn_gateway.d_path.enabled` or `<node_type_key>.node_groups[].nodes[].evpn_gateway.d_path.enabled` or `<node_type_key>.node_groups[].evpn_gateway.d_path.enabled` or `<node_type_key>.nodes[].evpn_gateway.d_path.enabled` or `device_profiles[].evpn_gateway.d_path.enabled` or `devices[].evpn_gateway.d_path.enabled` instead.
              enable_d_path: <bool; default=True>

              # ASN(asplain):local_admin or ASN(asdot):local_admin notation
              # This key is deprecated.
              # Support will be removed in AVD version 7.0.0.
              # Use `<node_type_key>.defaults.evpn_gateway.d_path.local_domain_id_local` or `<node_type_key>.node_groups[].nodes[].evpn_gateway.d_path.local_domain_id_local` or `<node_type_key>.node_groups[].evpn_gateway.d_path.local_domain_id_local` or `<node_type_key>.nodes[].evpn_gateway.d_path.local_domain_id_local` or `device_profiles[].evpn_gateway.d_path.local_domain_id_local` or `devices[].evpn_gateway.d_path.local_domain_id_local` instead.
              evpn_domain_id_local: <str>

              # ASN(asplain):local_admin or ASN(asdot):local_admin notation
              # This key is deprecated.
              # Support will be removed in AVD version 7.0.0.
              # Use `<node_type_key>.defaults.evpn_gateway.d_path.remote_domain_id` or `<node_type_key>.node_groups[].nodes[].evpn_gateway.d_path.remote_domain_id` or `<node_type_key>.node_groups[].evpn_gateway.d_path.remote_domain_id` or `<node_type_key>.nodes[].evpn_gateway.d_path.remote_domain_id` or `device_profiles[].evpn_gateway.d_path.remote_domain_id` or `devices[].evpn_gateway.d_path.remote_domain_id` instead.
              evpn_domain_id_remote: <str>
              evpn_ethernet_segment: # required

                # EVPN Ethernet Segment Identifier (Type 1 format)
                identifier: <str; required>

                # Low-order 6 bytes of ES-Import Route Target.
                rt_import: <str; required>

    # PREVIEW - This datamodel is still under development and may change or get removed at any time.
    device_profiles:

        # Profile Name
      - name: <str; required; unique>

        # Node is acting as EVPN Multi-Domain Gateway.
        # New BGP peer-group is generated between EVPN GWs in different domains or between GWs and Route Servers.
        # Name can be changed under "bgp_peer_groups.evpn_overlay_core" variable.
        # L3 rechability for different EVPN GWs must be already in place, it is recommended to use DCI & L3 Edge if Route Servers and GWs are not defined under the same Ansible inventory.
        evpn_gateway:

          # Define remote peers of the EVPN VXLAN Gateway.
          # If the hostname can be found in the inventory, ip_address and BGP ASN will be automatically populated. Manual override takes precedence.
          # If the peer's hostname can not be found in the inventory, ip_address and bgp_as must be defined.
          remote_peers:

              # Hostname of remote EVPN GW server.
            - hostname: <str; required; unique>

              # Peering IP of remote Route Server.
              ip_address: <str>

              # Remote Route Server's BGP AS <1-4294967295> or AS number in asdot notation "<1-65535>.<0-65535>".
              # For asdot notation in YAML inputs, the value must be put in quotes, to prevent it from being interpreted as a float number.
              bgp_as: <str>

          # Enable EVPN Gateway functionality for route-types 2 (MAC-IP) and 3 (IMET).
          evpn_l2:
            enabled: <bool; default=False>

          # Enable EVPN Gateway functionality for route-type 5 (IP-PREFIX).
          evpn_l3:
            enabled: <bool; default=False>
            inter_domain: <bool; default=True>

            # Defines the rewriting mode for EVPN L3 inter-domain routing.
            # - next-hop-self: (default) Forward EVPN IP-Prefix routes by only replacing the next-hop to the gateway itself.
            # - rd-rt-rewrite: Re-export local EVPN IP-Prefix routes with the RD and export RTs of the remote domain and vice versa.
            mode: <str; "next-hop-self" | "rd-rt-rewrite"; default="next-hop-self">
          d_path:

            # Enable D-path for use with BGP bestpath selection algorithm.
            enabled: <bool; default=True>

            # ASN(asplain):local_admin or ASN(asdot):local_admin notation
            local_domain_id: <str; required>

            # ASN(asplain):local_admin or ASN(asdot):local_admin notation
            remote_domain_id: <str; required>

          # Enable Active Active Multihoming architecture for EVPN Gateways.
          # Not supported with MLAG or IPVPN Gateway. Requires EVPN L3 inter-domain to be enabled.
          all_active_multihoming:

            # Enable Active Active Multihoming resiliency model.
            enabled: <bool; required>

            # Enable D-path for use with BGP bestpath selection algorithm.
            # This key is deprecated.
            # Support will be removed in AVD version 7.0.0.
            # Use `<node_type_key>.defaults.evpn_gateway.d_path.enabled` or `<node_type_key>.node_groups[].nodes[].evpn_gateway.d_path.enabled` or `<node_type_key>.node_groups[].evpn_gateway.d_path.enabled` or `<node_type_key>.nodes[].evpn_gateway.d_path.enabled` or `device_profiles[].evpn_gateway.d_path.enabled` or `devices[].evpn_gateway.d_path.enabled` instead.
            enable_d_path: <bool; default=True>

            # ASN(asplain):local_admin or ASN(asdot):local_admin notation
            # This key is deprecated.
            # Support will be removed in AVD version 7.0.0.
            # Use `<node_type_key>.defaults.evpn_gateway.d_path.local_domain_id_local` or `<node_type_key>.node_groups[].nodes[].evpn_gateway.d_path.local_domain_id_local` or `<node_type_key>.node_groups[].evpn_gateway.d_path.local_domain_id_local` or `<node_type_key>.nodes[].evpn_gateway.d_path.local_domain_id_local` or `device_profiles[].evpn_gateway.d_path.local_domain_id_local` or `devices[].evpn_gateway.d_path.local_domain_id_local` instead.
            evpn_domain_id_local: <str>

            # ASN(asplain):local_admin or ASN(asdot):local_admin notation
            # This key is deprecated.
            # Support will be removed in AVD version 7.0.0.
            # Use `<node_type_key>.defaults.evpn_gateway.d_path.remote_domain_id` or `<node_type_key>.node_groups[].nodes[].evpn_gateway.d_path.remote_domain_id` or `<node_type_key>.node_groups[].evpn_gateway.d_path.remote_domain_id` or `<node_type_key>.nodes[].evpn_gateway.d_path.remote_domain_id` or `device_profiles[].evpn_gateway.d_path.remote_domain_id` or `devices[].evpn_gateway.d_path.remote_domain_id` instead.
            evpn_domain_id_remote: <str>
            evpn_ethernet_segment: # required

              # EVPN Ethernet Segment Identifier (Type 1 format)
              identifier: <str; required>

              # Low-order 6 bytes of ES-Import Route Target.
              rt_import: <str; required>

    # PREVIEW - This datamodel is still under development and may change or get removed at any time.
    devices:

        # The Node Name is used as "hostname".
        name: <str; required; unique>

        # Node is acting as EVPN Multi-Domain Gateway.
        # New BGP peer-group is generated between EVPN GWs in different domains or between GWs and Route Servers.
        # Name can be changed under "bgp_peer_groups.evpn_overlay_core" variable.
        # L3 rechability for different EVPN GWs must be already in place, it is recommended to use DCI & L3 Edge if Route Servers and GWs are not defined under the same Ansible inventory.
        evpn_gateway:

          # Define remote peers of the EVPN VXLAN Gateway.
          # If the hostname can be found in the inventory, ip_address and BGP ASN will be automatically populated. Manual override takes precedence.
          # If the peer's hostname can not be found in the inventory, ip_address and bgp_as must be defined.
          remote_peers:

              # Hostname of remote EVPN GW server.
            - hostname: <str; required; unique>

              # Peering IP of remote Route Server.
              ip_address: <str>

              # Remote Route Server's BGP AS <1-4294967295> or AS number in asdot notation "<1-65535>.<0-65535>".
              # For asdot notation in YAML inputs, the value must be put in quotes, to prevent it from being interpreted as a float number.
              bgp_as: <str>

          # Enable EVPN Gateway functionality for route-types 2 (MAC-IP) and 3 (IMET).
          evpn_l2:
            enabled: <bool; default=False>

          # Enable EVPN Gateway functionality for route-type 5 (IP-PREFIX).
          evpn_l3:
            enabled: <bool; default=False>
            inter_domain: <bool; default=True>

            # Defines the rewriting mode for EVPN L3 inter-domain routing.
            # - next-hop-self: (default) Forward EVPN IP-Prefix routes by only replacing the next-hop to the gateway itself.
            # - rd-rt-rewrite: Re-export local EVPN IP-Prefix routes with the RD and export RTs of the remote domain and vice versa.
            mode: <str; "next-hop-self" | "rd-rt-rewrite"; default="next-hop-self">
          d_path:

            # Enable D-path for use with BGP bestpath selection algorithm.
            enabled: <bool; default=True>

            # ASN(asplain):local_admin or ASN(asdot):local_admin notation
            local_domain_id: <str; required>

            # ASN(asplain):local_admin or ASN(asdot):local_admin notation
            remote_domain_id: <str; required>

          # Enable Active Active Multihoming architecture for EVPN Gateways.
          # Not supported with MLAG or IPVPN Gateway. Requires EVPN L3 inter-domain to be enabled.
          all_active_multihoming:

            # Enable Active Active Multihoming resiliency model.
            enabled: <bool; required>

            # Enable D-path for use with BGP bestpath selection algorithm.
            # This key is deprecated.
            # Support will be removed in AVD version 7.0.0.
            # Use `<node_type_key>.defaults.evpn_gateway.d_path.enabled` or `<node_type_key>.node_groups[].nodes[].evpn_gateway.d_path.enabled` or `<node_type_key>.node_groups[].evpn_gateway.d_path.enabled` or `<node_type_key>.nodes[].evpn_gateway.d_path.enabled` or `device_profiles[].evpn_gateway.d_path.enabled` or `devices[].evpn_gateway.d_path.enabled` instead.
            enable_d_path: <bool; default=True>

            # ASN(asplain):local_admin or ASN(asdot):local_admin notation
            # This key is deprecated.
            # Support will be removed in AVD version 7.0.0.
            # Use `<node_type_key>.defaults.evpn_gateway.d_path.local_domain_id_local` or `<node_type_key>.node_groups[].nodes[].evpn_gateway.d_path.local_domain_id_local` or `<node_type_key>.node_groups[].evpn_gateway.d_path.local_domain_id_local` or `<node_type_key>.nodes[].evpn_gateway.d_path.local_domain_id_local` or `device_profiles[].evpn_gateway.d_path.local_domain_id_local` or `devices[].evpn_gateway.d_path.local_domain_id_local` instead.
            evpn_domain_id_local: <str>

            # ASN(asplain):local_admin or ASN(asdot):local_admin notation
            # This key is deprecated.
            # Support will be removed in AVD version 7.0.0.
            # Use `<node_type_key>.defaults.evpn_gateway.d_path.remote_domain_id` or `<node_type_key>.node_groups[].nodes[].evpn_gateway.d_path.remote_domain_id` or `<node_type_key>.node_groups[].evpn_gateway.d_path.remote_domain_id` or `<node_type_key>.nodes[].evpn_gateway.d_path.remote_domain_id` or `device_profiles[].evpn_gateway.d_path.remote_domain_id` or `devices[].evpn_gateway.d_path.remote_domain_id` instead.
            evpn_domain_id_remote: <str>
            evpn_ethernet_segment: # required

              # EVPN Ethernet Segment Identifier (Type 1 format)
              identifier: <str; required>

              # Low-order 6 bytes of ES-Import Route Target.
              rt_import: <str; required>
    ```
