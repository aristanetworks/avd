!!! warning
    This document describes the data model for AVD 4.x. It may or may not work in previous versions.

## MLAG

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>&lt;node_type_keys.key&gt;</samp>](## "&lt;node_type_keys.key&gt;") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;defaults</samp>](## "&lt;node_type_keys.key&gt;.defaults") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mlag</samp>](## "&lt;node_type_keys.key&gt;.defaults.mlag") | Boolean |  | True |  | Enable / Disable auto MLAG, when two nodes are defined in node group. |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mlag_dual_primary_detection</samp>](## "&lt;node_type_keys.key&gt;.defaults.mlag_dual_primary_detection") | Boolean |  | False |  | Enable / Disable MLAG dual primary detection |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mlag_interfaces</samp>](## "&lt;node_type_keys.key&gt;.defaults.mlag_interfaces") | List, items: String |  |  |  | Required when MLAG leafs are present in the topology |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.defaults.mlag_interfaces.[].&lt;str&gt;") | String |  |  | Pattern: Ethernet[\d/]+ |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mlag_interfaces_speed</samp>](## "&lt;node_type_keys.key&gt;.defaults.mlag_interfaces_speed") | String |  |  |  | < interface_speed | forced interface_speed | auto interface_speed > |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mlag_peer_ipv4_pool</samp>](## "&lt;node_type_keys.key&gt;.defaults.mlag_peer_ipv4_pool") | String |  |  | Format: ipv4_cidr | IP address pool used for MLAG Peer Link (control link). IP is derived from the node id.<br>Required when MLAG leafs present in topology.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mlag_peer_l3_ipv4_pool</samp>](## "&lt;node_type_keys.key&gt;.defaults.mlag_peer_l3_ipv4_pool") | String |  |  | Format: ipv4_cidr | IP address pool used for MLAG underlay L3 peering. IP is derived from the node id.<br>Required when MLAG leafs present in topology and they are using a separate L3 peering VLAN.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mlag_peer_l3_vlan</samp>](## "&lt;node_type_keys.key&gt;.defaults.mlag_peer_l3_vlan") | Integer |  | 4093 | Min: 0<br>Max: 4094 | Underlay L3 peering SVI interface id<br>If set to 0 or the same vlan as mlag_peer_vlan, the mlag_peer_vlan will be used for L3 peering<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mlag_peer_link_allowed_vlans</samp>](## "&lt;node_type_keys.key&gt;.defaults.mlag_peer_link_allowed_vlans") | String |  | 2-4094 |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mlag_peer_vlan</samp>](## "&lt;node_type_keys.key&gt;.defaults.mlag_peer_vlan") | Integer |  | 4094 | Min: 1<br>Max: 4094 | MLAG Peer Link (control link) SVI interface id |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mlag_port_channel_id</samp>](## "&lt;node_type_keys.key&gt;.defaults.mlag_port_channel_id") | Integer |  |  |  | If not set, the mlag port-channel id is generated based on the digits of the first interface present in 'mlag_interfaces'. Valid port-channel id numbers are < 1-2000 > for EOS < 4.25.0F and < 1 - 999999 > for EOS >= 4.25.0F. |
| [<samp>&nbsp;&nbsp;node_groups</samp>](## "&lt;node_type_keys.key&gt;.node_groups") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- mlag</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].mlag") | Boolean |  | True |  | Enable / Disable auto MLAG, when two nodes are defined in node group. |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_dual_primary_detection</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].mlag_dual_primary_detection") | Boolean |  | False |  | Enable / Disable MLAG dual primary detection |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_interfaces</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].mlag_interfaces") | List, items: String |  |  |  | Required when MLAG leafs are present in the topology |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].mlag_interfaces.[].&lt;str&gt;") | String |  |  | Pattern: Ethernet[\d/]+ |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_interfaces_speed</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].mlag_interfaces_speed") | String |  |  |  | < interface_speed | forced interface_speed | auto interface_speed > |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_peer_ipv4_pool</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].mlag_peer_ipv4_pool") | String |  |  | Format: ipv4_cidr | IP address pool used for MLAG Peer Link (control link). IP is derived from the node id.<br>Required when MLAG leafs present in topology.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_peer_l3_ipv4_pool</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].mlag_peer_l3_ipv4_pool") | String |  |  | Format: ipv4_cidr | IP address pool used for MLAG underlay L3 peering. IP is derived from the node id.<br>Required when MLAG leafs present in topology and they are using a separate L3 peering VLAN.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_peer_l3_vlan</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].mlag_peer_l3_vlan") | Integer |  | 4093 | Min: 0<br>Max: 4094 | Underlay L3 peering SVI interface id<br>If set to 0 or the same vlan as mlag_peer_vlan, the mlag_peer_vlan will be used for L3 peering<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_peer_link_allowed_vlans</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].mlag_peer_link_allowed_vlans") | String |  | 2-4094 |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_peer_vlan</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].mlag_peer_vlan") | Integer |  | 4094 | Min: 1<br>Max: 4094 | MLAG Peer Link (control link) SVI interface id |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_port_channel_id</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].mlag_port_channel_id") | Integer |  |  |  | If not set, the mlag port-channel id is generated based on the digits of the first interface present in 'mlag_interfaces'. Valid port-channel id numbers are < 1-2000 > for EOS < 4.25.0F and < 1 - 999999 > for EOS >= 4.25.0F. |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes") | $ref |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- mlag</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].mlag") | Boolean |  | True |  | Enable / Disable auto MLAG, when two nodes are defined in node group. |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_dual_primary_detection</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].mlag_dual_primary_detection") | Boolean |  | False |  | Enable / Disable MLAG dual primary detection |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_interfaces</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].mlag_interfaces") | List, items: String |  |  |  | Required when MLAG leafs are present in the topology |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].mlag_interfaces.[].&lt;str&gt;") | String |  |  | Pattern: Ethernet[\d/]+ |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_interfaces_speed</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].mlag_interfaces_speed") | String |  |  |  | < interface_speed | forced interface_speed | auto interface_speed > |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_peer_ipv4_pool</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].mlag_peer_ipv4_pool") | String |  |  | Format: ipv4_cidr | IP address pool used for MLAG Peer Link (control link). IP is derived from the node id.<br>Required when MLAG leafs present in topology.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_peer_l3_ipv4_pool</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].mlag_peer_l3_ipv4_pool") | String |  |  | Format: ipv4_cidr | IP address pool used for MLAG underlay L3 peering. IP is derived from the node id.<br>Required when MLAG leafs present in topology and they are using a separate L3 peering VLAN.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_peer_l3_vlan</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].mlag_peer_l3_vlan") | Integer |  | 4093 | Min: 0<br>Max: 4094 | Underlay L3 peering SVI interface id<br>If set to 0 or the same vlan as mlag_peer_vlan, the mlag_peer_vlan will be used for L3 peering<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_peer_link_allowed_vlans</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].mlag_peer_link_allowed_vlans") | String |  | 2-4094 |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_peer_vlan</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].mlag_peer_vlan") | Integer |  | 4094 | Min: 1<br>Max: 4094 | MLAG Peer Link (control link) SVI interface id |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_port_channel_id</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].mlag_port_channel_id") | Integer |  |  |  | If not set, the mlag port-channel id is generated based on the digits of the first interface present in 'mlag_interfaces'. Valid port-channel id numbers are < 1-2000 > for EOS < 4.25.0F and < 1 - 999999 > for EOS >= 4.25.0F. |
| [<samp>&nbsp;&nbsp;nodes</samp>](## "&lt;node_type_keys.key&gt;.nodes") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- mlag</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].mlag") | Boolean |  | True |  | Enable / Disable auto MLAG, when two nodes are defined in node group. |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_dual_primary_detection</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].mlag_dual_primary_detection") | Boolean |  | False |  | Enable / Disable MLAG dual primary detection |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_interfaces</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].mlag_interfaces") | List, items: String |  |  |  | Required when MLAG leafs are present in the topology |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].mlag_interfaces.[].&lt;str&gt;") | String |  |  | Pattern: Ethernet[\d/]+ |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_interfaces_speed</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].mlag_interfaces_speed") | String |  |  |  | < interface_speed | forced interface_speed | auto interface_speed > |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_peer_ipv4_pool</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].mlag_peer_ipv4_pool") | String |  |  | Format: ipv4_cidr | IP address pool used for MLAG Peer Link (control link). IP is derived from the node id.<br>Required when MLAG leafs present in topology.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_peer_l3_ipv4_pool</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].mlag_peer_l3_ipv4_pool") | String |  |  | Format: ipv4_cidr | IP address pool used for MLAG underlay L3 peering. IP is derived from the node id.<br>Required when MLAG leafs present in topology and they are using a separate L3 peering VLAN.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_peer_l3_vlan</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].mlag_peer_l3_vlan") | Integer |  | 4093 | Min: 0<br>Max: 4094 | Underlay L3 peering SVI interface id<br>If set to 0 or the same vlan as mlag_peer_vlan, the mlag_peer_vlan will be used for L3 peering<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_peer_link_allowed_vlans</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].mlag_peer_link_allowed_vlans") | String |  | 2-4094 |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_peer_vlan</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].mlag_peer_vlan") | Integer |  | 4094 | Min: 1<br>Max: 4094 | MLAG Peer Link (control link) SVI interface id |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_port_channel_id</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].mlag_port_channel_id") | Integer |  |  |  | If not set, the mlag port-channel id is generated based on the digits of the first interface present in 'mlag_interfaces'. Valid port-channel id numbers are < 1-2000 > for EOS < 4.25.0F and < 1 - 999999 > for EOS >= 4.25.0F. |

### YAML

```yaml
<node_type_keys.key>:
  defaults:
    mlag: <bool>
    mlag_dual_primary_detection: <bool>
    mlag_interfaces:
      - <str>
    mlag_interfaces_speed: <str>
    mlag_peer_ipv4_pool: <str>
    mlag_peer_l3_ipv4_pool: <str>
    mlag_peer_l3_vlan: <int>
    mlag_peer_link_allowed_vlans: <str>
    mlag_peer_vlan: <int>
    mlag_port_channel_id: <int>
  node_groups:
    - mlag: <bool>
      mlag_dual_primary_detection: <bool>
      mlag_interfaces:
        - <str>
      mlag_interfaces_speed: <str>
      mlag_peer_ipv4_pool: <str>
      mlag_peer_l3_ipv4_pool: <str>
      mlag_peer_l3_vlan: <int>
      mlag_peer_link_allowed_vlans: <str>
      mlag_peer_vlan: <int>
      mlag_port_channel_id: <int>
      nodes:
        - mlag: <bool>
          mlag_dual_primary_detection: <bool>
          mlag_interfaces:
            - <str>
          mlag_interfaces_speed: <str>
          mlag_peer_ipv4_pool: <str>
          mlag_peer_l3_ipv4_pool: <str>
          mlag_peer_l3_vlan: <int>
          mlag_peer_link_allowed_vlans: <str>
          mlag_peer_vlan: <int>
          mlag_port_channel_id: <int>
  nodes:
    - mlag: <bool>
      mlag_dual_primary_detection: <bool>
      mlag_interfaces:
        - <str>
      mlag_interfaces_speed: <str>
      mlag_peer_ipv4_pool: <str>
      mlag_peer_l3_ipv4_pool: <str>
      mlag_peer_l3_vlan: <int>
      mlag_peer_link_allowed_vlans: <str>
      mlag_peer_vlan: <int>
      mlag_port_channel_id: <int>
```

## Node Type Structure

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>&lt;node_type_keys.key&gt;</samp>](## "&lt;node_type_keys.key&gt;") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;defaults</samp>](## "&lt;node_type_keys.key&gt;.defaults") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;bgp_as</samp>](## "&lt;node_type_keys.key&gt;.defaults.bgp_as") | String |  |  |  | Required with eBGP |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;bgp_defaults</samp>](## "&lt;node_type_keys.key&gt;.defaults.bgp_defaults") | List, items: String |  |  |  | List of EOS commands to apply to BGP daemon |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.defaults.bgp_defaults.[].&lt;str&gt;") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;evpn_gateway</samp>](## "&lt;node_type_keys.key&gt;.defaults.evpn_gateway") | Dictionary |  |  |  | Node is acting as EVPN Multi-Domain Gateway<br>New BGP peer-group is generated between EVPN GWs in different domains or between GWs and Route Servers. Name can be changed under "bgp_peer_groups.evpn_overlay_core" variable<br>L3 rechability for different EVPN GWs must be already in place, it is recommended to use DCI & L3 Edge if Route Servers and GWs are not defined under the same Ansible inventory.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_l2</samp>](## "&lt;node_type_keys.key&gt;.defaults.evpn_gateway.evpn_l2") | Dictionary |  |  |  | Enable EVPN Gateway functionality for route-types 2 (MAC-IP) and 3 (IMET) |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;node_type_keys.key&gt;.defaults.evpn_gateway.evpn_l2.enabled") | Boolean |  | False |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_l3</samp>](## "&lt;node_type_keys.key&gt;.defaults.evpn_gateway.evpn_l3") | Dictionary |  |  |  | Enable EVPN Gateway functionality for route-type 5 (IP-PREFIX) |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;node_type_keys.key&gt;.defaults.evpn_gateway.evpn_l3.enabled") | Boolean |  | False |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inter_domain</samp>](## "&lt;node_type_keys.key&gt;.defaults.evpn_gateway.evpn_l3.inter_domain") | Boolean |  | True |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remote_peers</samp>](## "&lt;node_type_keys.key&gt;.defaults.evpn_gateway.remote_peers") | List, items: Dictionary |  |  |  | Define remote peers of the EVPN VXLAN Gateway.<br>If the hostname can be found in the inventory, ip_address and BGP ASN will be automatically populated. Manual override takes precedence.<br>If the peer's hostname can not be found in the inventory, ip_address and bgp_as must be defined.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- bgp_as</samp>](## "&lt;node_type_keys.key&gt;.defaults.evpn_gateway.remote_peers.[].bgp_as") | String |  |  |  | BGP ASN of remote Route Server |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hostname</samp>](## "&lt;node_type_keys.key&gt;.defaults.evpn_gateway.remote_peers.[].hostname") | String |  |  |  | Hostname of remote EVPN GW server |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "&lt;node_type_keys.key&gt;.defaults.evpn_gateway.remote_peers.[].ip_address") | String |  |  | Format: ipv4 | Peering IP of remote Route Server |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;evpn_role</samp>](## "&lt;node_type_keys.key&gt;.defaults.evpn_role") | String |  |  | Valid Values:<br>- client<br>- server<br>- none | Acting role in EVPN control plane. Default is set in node_type definition from node_type_keys. |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;evpn_route_servers</samp>](## "&lt;node_type_keys.key&gt;.defaults.evpn_route_servers") | List, items: String |  |  |  | List of nodes acting as EVPN Route-Servers / Route-Reflectors |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.defaults.evpn_route_servers.[].&lt;str&gt;") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;evpn_services_l2_only</samp>](## "&lt;node_type_keys.key&gt;.defaults.evpn_services_l2_only") | Boolean |  | False |  | Possibility to prevent configuration of Tenant VRFs and SVIs<br>Override node definition "network_services_l3" from node_type_keys<br>This allows support for centralized routing.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;filter</samp>](## "&lt;node_type_keys.key&gt;.defaults.filter") | Dictionary |  |  |  | Filter L3 and L2 network services based on tenant and tags (and operation filter)<br>If filter is not defined it will default to all<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;always_include_vrfs_in_tenants</samp>](## "&lt;node_type_keys.key&gt;.defaults.filter.always_include_vrfs_in_tenants") | List, items: String |  |  |  | List of tenants where VRFs will be configured even if VLANs are not included in tags<br>Useful for L3 "border" leaf.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.defaults.filter.always_include_vrfs_in_tenants.[].&lt;str&gt;") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tags</samp>](## "&lt;node_type_keys.key&gt;.defaults.filter.tags") | List, items: String |  | ['all'] |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.defaults.filter.tags.[].&lt;str&gt;") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tenants</samp>](## "&lt;node_type_keys.key&gt;.defaults.filter.tenants") | List, items: String |  | ['all'] |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.defaults.filter.tenants.[].&lt;str&gt;") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;id</samp>](## "&lt;node_type_keys.key&gt;.defaults.id") | Integer |  |  |  | Unique identifier used for IP addressing and other algorithms |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;igmp_snooping_enabled</samp>](## "&lt;node_type_keys.key&gt;.defaults.igmp_snooping_enabled") | Boolean |  | True |  | Activate or deactivate IGMP snooping on device level |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;inband_management_subnet</samp>](## "&lt;node_type_keys.key&gt;.defaults.inband_management_subnet") | String |  |  | Format: ipv4_cidr | Optional IP subnet assigned to Inband Management SVI on l2leafs in default VRF.<br>Parent l3leafs will have SVI with "ip virtual-router" and host-route injection based on ARP. This allows all l3leafs to reuse the same subnet<br>SVI IP address will be assigned as follows:<br>virtual-router: <subnet> + 1<br>l3leaf A      : <subnet> + 2 (same IP on all l3leaf A)<br>l3leaf B      : <subnet> + 3 (same IP on all l3leaf B)<br>l2leafs       : <subnet> + 3 + <l2leaf id><br>GW on l2leafs : <subnet> + 1<br>Assign range larger than total l2leafs + 5<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;inband_management_vlan</samp>](## "&lt;node_type_keys.key&gt;.defaults.inband_management_vlan") | Integer |  | 4092 |  | VLAN number assigned to Inband Management SVI on l2leafs in default VRF |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;is_type</samp>](## "&lt;node_type_keys.key&gt;.defaults.is_type") | String |  | level-2 | Valid Values:<br>- level-1-2<br>- level-1<br>- level-2 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_maximum_paths</samp>](## "&lt;node_type_keys.key&gt;.defaults.isis_maximum_paths") | Integer |  |  |  | Number of path to configure in ECMP for ISIS |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_system_id_prefix</samp>](## "&lt;node_type_keys.key&gt;.defaults.isis_system_id_prefix") | String |  |  | Pattern: [0-9a-f]{4}\.[0-9a-f]{4} | (4.4 hexadecimal) |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;lacp_port_id_range</samp>](## "&lt;node_type_keys.key&gt;.defaults.lacp_port_id_range") | Dictionary |  |  |  | This will generate the "lacp port-id range", "begin" and "end" values based on node "id" and the number of nodes in the "node_group".<br>Unique LACP port-id ranges are recommended for EVPN Multihoming designs.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;node_type_keys.key&gt;.defaults.lacp_port_id_range.enabled") | Boolean |  | False |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;offset</samp>](## "&lt;node_type_keys.key&gt;.defaults.lacp_port_id_range.offset") | Integer |  | 0 |  | Offset is used to avoid overlapping port-id ranges of different switches<br>Useful when a "connected-endpoint" is connected to switches in different "node_groups".<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;size</samp>](## "&lt;node_type_keys.key&gt;.defaults.lacp_port_id_range.size") | Integer |  | 128 |  | Recommended size > = number of ports in the switch. |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;link_tracking</samp>](## "&lt;node_type_keys.key&gt;.defaults.link_tracking") | Dictionary |  |  |  | This configures the Link Tracking Group on a switch as well as adds the p2p-uplinks of the switch as the upstream interfaces.<br>Useful in EVPN multhoming designs.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;node_type_keys.key&gt;.defaults.link_tracking.enabled") | Boolean |  | False |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;groups</samp>](## "&lt;node_type_keys.key&gt;.defaults.link_tracking.groups") | List, items: Dictionary |  | [{'name': 'LT_GROUP1'}] |  | By default a single group named "LT_GROUP1" is defined with default values.<br>Any groups defined under "groups" will replace the default.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- links_minimum</samp>](## "&lt;node_type_keys.key&gt;.defaults.link_tracking.groups.[].links_minimum") | Integer |  |  | Min: 1<br>Max: 100000 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "&lt;node_type_keys.key&gt;.defaults.link_tracking.groups.[].name") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;recovery_delay</samp>](## "&lt;node_type_keys.key&gt;.defaults.link_tracking.groups.[].recovery_delay") | Integer |  |  | Min: 0<br>Max: 3600 | default -> platform_settings_mlag_reload_delay -> 300 |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;loopback_ipv4_offset</samp>](## "&lt;node_type_keys.key&gt;.defaults.loopback_ipv4_offset") | Integer |  | 0 |  | Offset all assigned loopback IP addresses.<br>Required when the < loopback_ipv4_pool > is same for 2 different node_types (like spine and l3leaf) to avoid over-lapping IPs.<br>For example, set the minimum offset l3leaf.defaults.loopback_ipv4_offset: < total # spine switches > or vice versa.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;loopback_ipv4_pool</samp>](## "&lt;node_type_keys.key&gt;.defaults.loopback_ipv4_pool") | String |  |  | Format: ipv4_cidr | IPv4 subnet for Loopback0 allocation |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;loopback_ipv6_offset</samp>](## "&lt;node_type_keys.key&gt;.defaults.loopback_ipv6_offset") | Integer |  | 0 |  | Offset all assigned loopback IPv6 addresses.<br>Required when the < loopback_ipv6_pool > is same for 2 different node_types (like spine and l3leaf) to avoid overlapping IPs.<br>For example, set the minimum offset l3leaf.defaults.loopback_ipv6_offset: < total # spine switches > or vice versa.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;loopback_ipv6_pool</samp>](## "&lt;node_type_keys.key&gt;.defaults.loopback_ipv6_pool") | String |  |  | Format: ipv6_cidr | IPv6 subnet for Loopback0 allocation |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;max_parallel_uplinks</samp>](## "&lt;node_type_keys.key&gt;.defaults.max_parallel_uplinks") | Integer |  |  |  | Number of parallel links towards uplink switches |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;max_uplink_switches</samp>](## "&lt;node_type_keys.key&gt;.defaults.max_uplink_switches") | Integer |  |  |  | Maximum number of uplink switches.<br>Changing this value may change IP Addressing on uplinks.<br>Can be used to reserve IP space for future expansions.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mgmt_interface</samp>](## "&lt;node_type_keys.key&gt;.defaults.mgmt_interface") | String |  |  |  | Management Interface Name<br>Default -> platform_management_interface -> mgmt_interface -> "Management1"<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mgmt_ip</samp>](## "&lt;node_type_keys.key&gt;.defaults.mgmt_ip") | String |  |  | Format: cidr | Management Interface IP Address |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;node_sid_base</samp>](## "&lt;node_type_keys.key&gt;.defaults.node_sid_base") | Integer |  | 0 |  | Node-SID base for isis-sr underlay variants. Combined with node id to generate ISIS-SR node-SID. |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;platform</samp>](## "&lt;node_type_keys.key&gt;.defaults.platform") | String |  |  |  | Arista platform family |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;rack</samp>](## "&lt;node_type_keys.key&gt;.defaults.rack") | String |  |  |  | Rack that the switch is located in (only used in snmp_settings location) |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "&lt;node_type_keys.key&gt;.defaults.raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the root level of the final EOS configuration |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;short_esi</samp>](## "&lt;node_type_keys.key&gt;.defaults.short_esi") | String |  |  |  | short_esi only valid for l2leaf devices using port-channel uplink<br>Setting short_esi to "auto" generates the short_esi automatically using a hash of configuration elements.<br>< 0000:0000:0000 | auto ><br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_mode</samp>](## "&lt;node_type_keys.key&gt;.defaults.spanning_tree_mode") | String |  |  | Valid Values:<br>- mstp<br>- rstp<br>- rapid-pvst<br>- none |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_priority</samp>](## "&lt;node_type_keys.key&gt;.defaults.spanning_tree_priority") | Integer |  | 32768 |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_root_super</samp>](## "&lt;node_type_keys.key&gt;.defaults.spanning_tree_root_super") | Boolean |  | False |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "&lt;node_type_keys.key&gt;.defaults.structured_config") | Dictionary |  |  |  | Custom structured config for eos_cli_config_gen |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;uplink_interface_speed</samp>](## "&lt;node_type_keys.key&gt;.defaults.uplink_interface_speed") | String |  |  |  | Point-to-Point interface speed - will apply to uplinks on both ends<br>< interface_speed | forced interface_speed | auto interface_speed ><br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;uplink_interfaces</samp>](## "&lt;node_type_keys.key&gt;.defaults.uplink_interfaces") | List, items: String |  |  |  | Local uplink interfaces |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.defaults.uplink_interfaces.[].&lt;str&gt;") | String |  |  | Pattern: Ethernet[\d/]+ |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;uplink_ipv4_pool</samp>](## "&lt;node_type_keys.key&gt;.defaults.uplink_ipv4_pool") | String |  |  | Format: ipv4_cidr | IPv4 subnet to use to connect to uplink switches |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;uplink_macsec</samp>](## "&lt;node_type_keys.key&gt;.defaults.uplink_macsec") | Dictionary |  |  |  | Enable MacSec on all uplinks |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;profile</samp>](## "&lt;node_type_keys.key&gt;.defaults.uplink_macsec.profile") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;uplink_ptp</samp>](## "&lt;node_type_keys.key&gt;.defaults.uplink_ptp") | Dictionary |  |  |  | Enable PTP on all infrastructure links |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enable</samp>](## "&lt;node_type_keys.key&gt;.defaults.uplink_ptp.enable") | Boolean |  | False |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;uplink_switch_interfaces</samp>](## "&lt;node_type_keys.key&gt;.defaults.uplink_switch_interfaces") | List, items: String |  |  |  | Interfaces located on uplink switches |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.defaults.uplink_switch_interfaces.[].&lt;str&gt;") | String |  |  | Pattern: Ethernet[\d/]+ |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;uplink_switches</samp>](## "&lt;node_type_keys.key&gt;.defaults.uplink_switches") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.defaults.uplink_switches.[].&lt;str&gt;") | String |  |  |  | Hostname of uplink switch |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;virtual_router_mac_address</samp>](## "&lt;node_type_keys.key&gt;.defaults.virtual_router_mac_address") | String |  |  | Format: mac | Virtual router mac address for anycast gateway |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vtep_loopback</samp>](## "&lt;node_type_keys.key&gt;.defaults.vtep_loopback") | String |  |  | Pattern: Loopback[\d/]+ | Set VXLAN source interface. |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vtep_loopback_ipv4_pool</samp>](## "&lt;node_type_keys.key&gt;.defaults.vtep_loopback_ipv4_pool") | String |  |  | Format: ipv4_cidr | IPv4 subnet for VTEP-Loopback allocation |
| [<samp>&nbsp;&nbsp;node_groups</samp>](## "&lt;node_type_keys.key&gt;.node_groups") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- bgp_as</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].bgp_as") | String |  |  |  | Required with eBGP |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp_defaults</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].bgp_defaults") | List, items: String |  |  |  | List of EOS commands to apply to BGP daemon |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].bgp_defaults.[].&lt;str&gt;") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_gateway</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].evpn_gateway") | Dictionary |  |  |  | Node is acting as EVPN Multi-Domain Gateway<br>New BGP peer-group is generated between EVPN GWs in different domains or between GWs and Route Servers. Name can be changed under "bgp_peer_groups.evpn_overlay_core" variable<br>L3 rechability for different EVPN GWs must be already in place, it is recommended to use DCI & L3 Edge if Route Servers and GWs are not defined under the same Ansible inventory.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_l2</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].evpn_gateway.evpn_l2") | Dictionary |  |  |  | Enable EVPN Gateway functionality for route-types 2 (MAC-IP) and 3 (IMET) |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].evpn_gateway.evpn_l2.enabled") | Boolean |  | False |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_l3</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].evpn_gateway.evpn_l3") | Dictionary |  |  |  | Enable EVPN Gateway functionality for route-type 5 (IP-PREFIX) |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].evpn_gateway.evpn_l3.enabled") | Boolean |  | False |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inter_domain</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].evpn_gateway.evpn_l3.inter_domain") | Boolean |  | True |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remote_peers</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].evpn_gateway.remote_peers") | List, items: Dictionary |  |  |  | Define remote peers of the EVPN VXLAN Gateway.<br>If the hostname can be found in the inventory, ip_address and BGP ASN will be automatically populated. Manual override takes precedence.<br>If the peer's hostname can not be found in the inventory, ip_address and bgp_as must be defined.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- bgp_as</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].evpn_gateway.remote_peers.[].bgp_as") | String |  |  |  | BGP ASN of remote Route Server |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hostname</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].evpn_gateway.remote_peers.[].hostname") | String |  |  |  | Hostname of remote EVPN GW server |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].evpn_gateway.remote_peers.[].ip_address") | String |  |  | Format: ipv4 | Peering IP of remote Route Server |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_role</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].evpn_role") | String |  |  | Valid Values:<br>- client<br>- server<br>- none | Acting role in EVPN control plane. Default is set in node_type definition from node_type_keys. |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_route_servers</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].evpn_route_servers") | List, items: String |  |  |  | List of nodes acting as EVPN Route-Servers / Route-Reflectors |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].evpn_route_servers.[].&lt;str&gt;") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_services_l2_only</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].evpn_services_l2_only") | Boolean |  | False |  | Possibility to prevent configuration of Tenant VRFs and SVIs<br>Override node definition "network_services_l3" from node_type_keys<br>This allows support for centralized routing.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;filter</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].filter") | Dictionary |  |  |  | Filter L3 and L2 network services based on tenant and tags (and operation filter)<br>If filter is not defined it will default to all<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;always_include_vrfs_in_tenants</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].filter.always_include_vrfs_in_tenants") | List, items: String |  |  |  | List of tenants where VRFs will be configured even if VLANs are not included in tags<br>Useful for L3 "border" leaf.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].filter.always_include_vrfs_in_tenants.[].&lt;str&gt;") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tags</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].filter.tags") | List, items: String |  | ['all'] |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].filter.tags.[].&lt;str&gt;") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tenants</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].filter.tenants") | List, items: String |  | ['all'] |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].filter.tenants.[].&lt;str&gt;") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;id</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].id") | Integer |  |  |  | Unique identifier used for IP addressing and other algorithms |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;igmp_snooping_enabled</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].igmp_snooping_enabled") | Boolean |  | True |  | Activate or deactivate IGMP snooping on device level |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inband_management_subnet</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].inband_management_subnet") | String |  |  | Format: ipv4_cidr | Optional IP subnet assigned to Inband Management SVI on l2leafs in default VRF.<br>Parent l3leafs will have SVI with "ip virtual-router" and host-route injection based on ARP. This allows all l3leafs to reuse the same subnet<br>SVI IP address will be assigned as follows:<br>virtual-router: <subnet> + 1<br>l3leaf A      : <subnet> + 2 (same IP on all l3leaf A)<br>l3leaf B      : <subnet> + 3 (same IP on all l3leaf B)<br>l2leafs       : <subnet> + 3 + <l2leaf id><br>GW on l2leafs : <subnet> + 1<br>Assign range larger than total l2leafs + 5<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inband_management_vlan</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].inband_management_vlan") | Integer |  | 4092 |  | VLAN number assigned to Inband Management SVI on l2leafs in default VRF |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;is_type</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].is_type") | String |  | level-2 | Valid Values:<br>- level-1-2<br>- level-1<br>- level-2 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_maximum_paths</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].isis_maximum_paths") | Integer |  |  |  | Number of path to configure in ECMP for ISIS |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_system_id_prefix</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].isis_system_id_prefix") | String |  |  | Pattern: [0-9a-f]{4}\.[0-9a-f]{4} | (4.4 hexadecimal) |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;lacp_port_id_range</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].lacp_port_id_range") | Dictionary |  |  |  | This will generate the "lacp port-id range", "begin" and "end" values based on node "id" and the number of nodes in the "node_group".<br>Unique LACP port-id ranges are recommended for EVPN Multihoming designs.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].lacp_port_id_range.enabled") | Boolean |  | False |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;offset</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].lacp_port_id_range.offset") | Integer |  | 0 |  | Offset is used to avoid overlapping port-id ranges of different switches<br>Useful when a "connected-endpoint" is connected to switches in different "node_groups".<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;size</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].lacp_port_id_range.size") | Integer |  | 128 |  | Recommended size > = number of ports in the switch. |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;link_tracking</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].link_tracking") | Dictionary |  |  |  | This configures the Link Tracking Group on a switch as well as adds the p2p-uplinks of the switch as the upstream interfaces.<br>Useful in EVPN multhoming designs.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].link_tracking.enabled") | Boolean |  | False |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;groups</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].link_tracking.groups") | List, items: Dictionary |  | [{'name': 'LT_GROUP1'}] |  | By default a single group named "LT_GROUP1" is defined with default values.<br>Any groups defined under "groups" will replace the default.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- links_minimum</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].link_tracking.groups.[].links_minimum") | Integer |  |  | Min: 1<br>Max: 100000 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].link_tracking.groups.[].name") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;recovery_delay</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].link_tracking.groups.[].recovery_delay") | Integer |  |  | Min: 0<br>Max: 3600 | default -> platform_settings_mlag_reload_delay -> 300 |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loopback_ipv4_offset</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].loopback_ipv4_offset") | Integer |  | 0 |  | Offset all assigned loopback IP addresses.<br>Required when the < loopback_ipv4_pool > is same for 2 different node_types (like spine and l3leaf) to avoid over-lapping IPs.<br>For example, set the minimum offset l3leaf.defaults.loopback_ipv4_offset: < total # spine switches > or vice versa.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loopback_ipv4_pool</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].loopback_ipv4_pool") | String |  |  | Format: ipv4_cidr | IPv4 subnet for Loopback0 allocation |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loopback_ipv6_offset</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].loopback_ipv6_offset") | Integer |  | 0 |  | Offset all assigned loopback IPv6 addresses.<br>Required when the < loopback_ipv6_pool > is same for 2 different node_types (like spine and l3leaf) to avoid overlapping IPs.<br>For example, set the minimum offset l3leaf.defaults.loopback_ipv6_offset: < total # spine switches > or vice versa.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loopback_ipv6_pool</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].loopback_ipv6_pool") | String |  |  | Format: ipv6_cidr | IPv6 subnet for Loopback0 allocation |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;max_parallel_uplinks</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].max_parallel_uplinks") | Integer |  |  |  | Number of parallel links towards uplink switches |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;max_uplink_switches</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].max_uplink_switches") | Integer |  |  |  | Maximum number of uplink switches.<br>Changing this value may change IP Addressing on uplinks.<br>Can be used to reserve IP space for future expansions.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mgmt_interface</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].mgmt_interface") | String |  |  |  | Management Interface Name<br>Default -> platform_management_interface -> mgmt_interface -> "Management1"<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mgmt_ip</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].mgmt_ip") | String |  |  | Format: cidr | Management Interface IP Address |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;node_sid_base</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].node_sid_base") | Integer |  | 0 |  | Node-SID base for isis-sr underlay variants. Combined with node id to generate ISIS-SR node-SID. |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;platform</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].platform") | String |  |  |  | Arista platform family |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rack</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].rack") | String |  |  |  | Rack that the switch is located in (only used in snmp_settings location) |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the root level of the final EOS configuration |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;short_esi</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].short_esi") | String |  |  |  | short_esi only valid for l2leaf devices using port-channel uplink<br>Setting short_esi to "auto" generates the short_esi automatically using a hash of configuration elements.<br>< 0000:0000:0000 | auto ><br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_mode</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].spanning_tree_mode") | String |  |  | Valid Values:<br>- mstp<br>- rstp<br>- rapid-pvst<br>- none |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_priority</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].spanning_tree_priority") | Integer |  | 32768 |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_root_super</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].spanning_tree_root_super") | Boolean |  | False |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].structured_config") | Dictionary |  |  |  | Custom structured config for eos_cli_config_gen |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_interface_speed</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].uplink_interface_speed") | String |  |  |  | Point-to-Point interface speed - will apply to uplinks on both ends<br>< interface_speed | forced interface_speed | auto interface_speed ><br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_interfaces</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].uplink_interfaces") | List, items: String |  |  |  | Local uplink interfaces |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].uplink_interfaces.[].&lt;str&gt;") | String |  |  | Pattern: Ethernet[\d/]+ |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_ipv4_pool</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].uplink_ipv4_pool") | String |  |  | Format: ipv4_cidr | IPv4 subnet to use to connect to uplink switches |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_macsec</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].uplink_macsec") | Dictionary |  |  |  | Enable MacSec on all uplinks |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;profile</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].uplink_macsec.profile") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_ptp</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].uplink_ptp") | Dictionary |  |  |  | Enable PTP on all infrastructure links |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enable</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].uplink_ptp.enable") | Boolean |  | False |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_switch_interfaces</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].uplink_switch_interfaces") | List, items: String |  |  |  | Interfaces located on uplink switches |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].uplink_switch_interfaces.[].&lt;str&gt;") | String |  |  | Pattern: Ethernet[\d/]+ |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_switches</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].uplink_switches") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].uplink_switches.[].&lt;str&gt;") | String |  |  |  | Hostname of uplink switch |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;virtual_router_mac_address</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].virtual_router_mac_address") | String |  |  | Format: mac | Virtual router mac address for anycast gateway |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vtep_loopback</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].vtep_loopback") | String |  |  | Pattern: Loopback[\d/]+ | Set VXLAN source interface. |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vtep_loopback_ipv4_pool</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].vtep_loopback_ipv4_pool") | String |  |  | Format: ipv4_cidr | IPv4 subnet for VTEP-Loopback allocation |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;group</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].group") | String | Required, Unique |  |  | The Node Group Name is used for MLAG domain |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes") | $ref |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- bgp_as</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].bgp_as") | String |  |  |  | Required with eBGP |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp_defaults</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].bgp_defaults") | List, items: String |  |  |  | List of EOS commands to apply to BGP daemon |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].bgp_defaults.[].&lt;str&gt;") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_gateway</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].evpn_gateway") | Dictionary |  |  |  | Node is acting as EVPN Multi-Domain Gateway<br>New BGP peer-group is generated between EVPN GWs in different domains or between GWs and Route Servers. Name can be changed under "bgp_peer_groups.evpn_overlay_core" variable<br>L3 rechability for different EVPN GWs must be already in place, it is recommended to use DCI & L3 Edge if Route Servers and GWs are not defined under the same Ansible inventory.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_l2</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].evpn_gateway.evpn_l2") | Dictionary |  |  |  | Enable EVPN Gateway functionality for route-types 2 (MAC-IP) and 3 (IMET) |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].evpn_gateway.evpn_l2.enabled") | Boolean |  | False |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_l3</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].evpn_gateway.evpn_l3") | Dictionary |  |  |  | Enable EVPN Gateway functionality for route-type 5 (IP-PREFIX) |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].evpn_gateway.evpn_l3.enabled") | Boolean |  | False |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inter_domain</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].evpn_gateway.evpn_l3.inter_domain") | Boolean |  | True |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remote_peers</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].evpn_gateway.remote_peers") | List, items: Dictionary |  |  |  | Define remote peers of the EVPN VXLAN Gateway.<br>If the hostname can be found in the inventory, ip_address and BGP ASN will be automatically populated. Manual override takes precedence.<br>If the peer's hostname can not be found in the inventory, ip_address and bgp_as must be defined.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- bgp_as</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].evpn_gateway.remote_peers.[].bgp_as") | String |  |  |  | BGP ASN of remote Route Server |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hostname</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].evpn_gateway.remote_peers.[].hostname") | String |  |  |  | Hostname of remote EVPN GW server |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].evpn_gateway.remote_peers.[].ip_address") | String |  |  | Format: ipv4 | Peering IP of remote Route Server |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_role</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].evpn_role") | String |  |  | Valid Values:<br>- client<br>- server<br>- none | Acting role in EVPN control plane. Default is set in node_type definition from node_type_keys. |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_route_servers</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].evpn_route_servers") | List, items: String |  |  |  | List of nodes acting as EVPN Route-Servers / Route-Reflectors |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].evpn_route_servers.[].&lt;str&gt;") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_services_l2_only</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].evpn_services_l2_only") | Boolean |  | False |  | Possibility to prevent configuration of Tenant VRFs and SVIs<br>Override node definition "network_services_l3" from node_type_keys<br>This allows support for centralized routing.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;filter</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].filter") | Dictionary |  |  |  | Filter L3 and L2 network services based on tenant and tags (and operation filter)<br>If filter is not defined it will default to all<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;always_include_vrfs_in_tenants</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].filter.always_include_vrfs_in_tenants") | List, items: String |  |  |  | List of tenants where VRFs will be configured even if VLANs are not included in tags<br>Useful for L3 "border" leaf.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].filter.always_include_vrfs_in_tenants.[].&lt;str&gt;") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tags</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].filter.tags") | List, items: String |  | ['all'] |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].filter.tags.[].&lt;str&gt;") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tenants</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].filter.tenants") | List, items: String |  | ['all'] |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].filter.tenants.[].&lt;str&gt;") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;id</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].id") | Integer |  |  |  | Unique identifier used for IP addressing and other algorithms |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;igmp_snooping_enabled</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].igmp_snooping_enabled") | Boolean |  | True |  | Activate or deactivate IGMP snooping on device level |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inband_management_subnet</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].inband_management_subnet") | String |  |  | Format: ipv4_cidr | Optional IP subnet assigned to Inband Management SVI on l2leafs in default VRF.<br>Parent l3leafs will have SVI with "ip virtual-router" and host-route injection based on ARP. This allows all l3leafs to reuse the same subnet<br>SVI IP address will be assigned as follows:<br>virtual-router: <subnet> + 1<br>l3leaf A      : <subnet> + 2 (same IP on all l3leaf A)<br>l3leaf B      : <subnet> + 3 (same IP on all l3leaf B)<br>l2leafs       : <subnet> + 3 + <l2leaf id><br>GW on l2leafs : <subnet> + 1<br>Assign range larger than total l2leafs + 5<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inband_management_vlan</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].inband_management_vlan") | Integer |  | 4092 |  | VLAN number assigned to Inband Management SVI on l2leafs in default VRF |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;is_type</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].is_type") | String |  | level-2 | Valid Values:<br>- level-1-2<br>- level-1<br>- level-2 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_maximum_paths</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].isis_maximum_paths") | Integer |  |  |  | Number of path to configure in ECMP for ISIS |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_system_id_prefix</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].isis_system_id_prefix") | String |  |  | Pattern: [0-9a-f]{4}\.[0-9a-f]{4} | (4.4 hexadecimal) |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;lacp_port_id_range</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].lacp_port_id_range") | Dictionary |  |  |  | This will generate the "lacp port-id range", "begin" and "end" values based on node "id" and the number of nodes in the "node_group".<br>Unique LACP port-id ranges are recommended for EVPN Multihoming designs.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].lacp_port_id_range.enabled") | Boolean |  | False |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;offset</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].lacp_port_id_range.offset") | Integer |  | 0 |  | Offset is used to avoid overlapping port-id ranges of different switches<br>Useful when a "connected-endpoint" is connected to switches in different "node_groups".<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;size</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].lacp_port_id_range.size") | Integer |  | 128 |  | Recommended size > = number of ports in the switch. |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;link_tracking</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].link_tracking") | Dictionary |  |  |  | This configures the Link Tracking Group on a switch as well as adds the p2p-uplinks of the switch as the upstream interfaces.<br>Useful in EVPN multhoming designs.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].link_tracking.enabled") | Boolean |  | False |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;groups</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].link_tracking.groups") | List, items: Dictionary |  | [{'name': 'LT_GROUP1'}] |  | By default a single group named "LT_GROUP1" is defined with default values.<br>Any groups defined under "groups" will replace the default.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- links_minimum</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].link_tracking.groups.[].links_minimum") | Integer |  |  | Min: 1<br>Max: 100000 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].link_tracking.groups.[].name") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;recovery_delay</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].link_tracking.groups.[].recovery_delay") | Integer |  |  | Min: 0<br>Max: 3600 | default -> platform_settings_mlag_reload_delay -> 300 |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loopback_ipv4_offset</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].loopback_ipv4_offset") | Integer |  | 0 |  | Offset all assigned loopback IP addresses.<br>Required when the < loopback_ipv4_pool > is same for 2 different node_types (like spine and l3leaf) to avoid over-lapping IPs.<br>For example, set the minimum offset l3leaf.defaults.loopback_ipv4_offset: < total # spine switches > or vice versa.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loopback_ipv4_pool</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].loopback_ipv4_pool") | String |  |  | Format: ipv4_cidr | IPv4 subnet for Loopback0 allocation |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loopback_ipv6_offset</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].loopback_ipv6_offset") | Integer |  | 0 |  | Offset all assigned loopback IPv6 addresses.<br>Required when the < loopback_ipv6_pool > is same for 2 different node_types (like spine and l3leaf) to avoid overlapping IPs.<br>For example, set the minimum offset l3leaf.defaults.loopback_ipv6_offset: < total # spine switches > or vice versa.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loopback_ipv6_pool</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].loopback_ipv6_pool") | String |  |  | Format: ipv6_cidr | IPv6 subnet for Loopback0 allocation |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;max_parallel_uplinks</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].max_parallel_uplinks") | Integer |  |  |  | Number of parallel links towards uplink switches |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;max_uplink_switches</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].max_uplink_switches") | Integer |  |  |  | Maximum number of uplink switches.<br>Changing this value may change IP Addressing on uplinks.<br>Can be used to reserve IP space for future expansions.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mgmt_interface</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].mgmt_interface") | String |  |  |  | Management Interface Name<br>Default -> platform_management_interface -> mgmt_interface -> "Management1"<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mgmt_ip</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].mgmt_ip") | String |  |  | Format: cidr | Management Interface IP Address |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;node_sid_base</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].node_sid_base") | Integer |  | 0 |  | Node-SID base for isis-sr underlay variants. Combined with node id to generate ISIS-SR node-SID. |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;platform</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].platform") | String |  |  |  | Arista platform family |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rack</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].rack") | String |  |  |  | Rack that the switch is located in (only used in snmp_settings location) |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the root level of the final EOS configuration |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;short_esi</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].short_esi") | String |  |  |  | short_esi only valid for l2leaf devices using port-channel uplink<br>Setting short_esi to "auto" generates the short_esi automatically using a hash of configuration elements.<br>< 0000:0000:0000 | auto ><br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_mode</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].spanning_tree_mode") | String |  |  | Valid Values:<br>- mstp<br>- rstp<br>- rapid-pvst<br>- none |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_priority</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].spanning_tree_priority") | Integer |  | 32768 |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_root_super</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].spanning_tree_root_super") | Boolean |  | False |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].structured_config") | Dictionary |  |  |  | Custom structured config for eos_cli_config_gen |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_interface_speed</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].uplink_interface_speed") | String |  |  |  | Point-to-Point interface speed - will apply to uplinks on both ends<br>< interface_speed | forced interface_speed | auto interface_speed ><br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_interfaces</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].uplink_interfaces") | List, items: String |  |  |  | Local uplink interfaces |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].uplink_interfaces.[].&lt;str&gt;") | String |  |  | Pattern: Ethernet[\d/]+ |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_ipv4_pool</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].uplink_ipv4_pool") | String |  |  | Format: ipv4_cidr | IPv4 subnet to use to connect to uplink switches |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_macsec</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].uplink_macsec") | Dictionary |  |  |  | Enable MacSec on all uplinks |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;profile</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].uplink_macsec.profile") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_ptp</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].uplink_ptp") | Dictionary |  |  |  | Enable PTP on all infrastructure links |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enable</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].uplink_ptp.enable") | Boolean |  | False |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_switch_interfaces</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].uplink_switch_interfaces") | List, items: String |  |  |  | Interfaces located on uplink switches |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].uplink_switch_interfaces.[].&lt;str&gt;") | String |  |  | Pattern: Ethernet[\d/]+ |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_switches</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].uplink_switches") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].uplink_switches.[].&lt;str&gt;") | String |  |  |  | Hostname of uplink switch |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;virtual_router_mac_address</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].virtual_router_mac_address") | String |  |  | Format: mac | Virtual router mac address for anycast gateway |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vtep_loopback</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].vtep_loopback") | String |  |  | Pattern: Loopback[\d/]+ | Set VXLAN source interface. |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vtep_loopback_ipv4_pool</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].vtep_loopback_ipv4_pool") | String |  |  | Format: ipv4_cidr | IPv4 subnet for VTEP-Loopback allocation |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mac_address</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].mac_address") | String |  |  |  | `mac_address` can only be set under the node and is used by the `arista.avd.dhcp_provisioner` role |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].name") | String | Required, Unique |  |  | The Node Name is used as "hostname" |
| [<samp>&nbsp;&nbsp;nodes</samp>](## "&lt;node_type_keys.key&gt;.nodes") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- bgp_as</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].bgp_as") | String |  |  |  | Required with eBGP |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp_defaults</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].bgp_defaults") | List, items: String |  |  |  | List of EOS commands to apply to BGP daemon |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].bgp_defaults.[].&lt;str&gt;") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_gateway</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].evpn_gateway") | Dictionary |  |  |  | Node is acting as EVPN Multi-Domain Gateway<br>New BGP peer-group is generated between EVPN GWs in different domains or between GWs and Route Servers. Name can be changed under "bgp_peer_groups.evpn_overlay_core" variable<br>L3 rechability for different EVPN GWs must be already in place, it is recommended to use DCI & L3 Edge if Route Servers and GWs are not defined under the same Ansible inventory.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_l2</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].evpn_gateway.evpn_l2") | Dictionary |  |  |  | Enable EVPN Gateway functionality for route-types 2 (MAC-IP) and 3 (IMET) |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].evpn_gateway.evpn_l2.enabled") | Boolean |  | False |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_l3</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].evpn_gateway.evpn_l3") | Dictionary |  |  |  | Enable EVPN Gateway functionality for route-type 5 (IP-PREFIX) |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].evpn_gateway.evpn_l3.enabled") | Boolean |  | False |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inter_domain</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].evpn_gateway.evpn_l3.inter_domain") | Boolean |  | True |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remote_peers</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].evpn_gateway.remote_peers") | List, items: Dictionary |  |  |  | Define remote peers of the EVPN VXLAN Gateway.<br>If the hostname can be found in the inventory, ip_address and BGP ASN will be automatically populated. Manual override takes precedence.<br>If the peer's hostname can not be found in the inventory, ip_address and bgp_as must be defined.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- bgp_as</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].evpn_gateway.remote_peers.[].bgp_as") | String |  |  |  | BGP ASN of remote Route Server |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hostname</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].evpn_gateway.remote_peers.[].hostname") | String |  |  |  | Hostname of remote EVPN GW server |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].evpn_gateway.remote_peers.[].ip_address") | String |  |  | Format: ipv4 | Peering IP of remote Route Server |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_role</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].evpn_role") | String |  |  | Valid Values:<br>- client<br>- server<br>- none | Acting role in EVPN control plane. Default is set in node_type definition from node_type_keys. |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_route_servers</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].evpn_route_servers") | List, items: String |  |  |  | List of nodes acting as EVPN Route-Servers / Route-Reflectors |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].evpn_route_servers.[].&lt;str&gt;") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_services_l2_only</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].evpn_services_l2_only") | Boolean |  | False |  | Possibility to prevent configuration of Tenant VRFs and SVIs<br>Override node definition "network_services_l3" from node_type_keys<br>This allows support for centralized routing.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;filter</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].filter") | Dictionary |  |  |  | Filter L3 and L2 network services based on tenant and tags (and operation filter)<br>If filter is not defined it will default to all<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;always_include_vrfs_in_tenants</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].filter.always_include_vrfs_in_tenants") | List, items: String |  |  |  | List of tenants where VRFs will be configured even if VLANs are not included in tags<br>Useful for L3 "border" leaf.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].filter.always_include_vrfs_in_tenants.[].&lt;str&gt;") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tags</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].filter.tags") | List, items: String |  | ['all'] |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].filter.tags.[].&lt;str&gt;") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tenants</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].filter.tenants") | List, items: String |  | ['all'] |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].filter.tenants.[].&lt;str&gt;") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;id</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].id") | Integer |  |  |  | Unique identifier used for IP addressing and other algorithms |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;igmp_snooping_enabled</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].igmp_snooping_enabled") | Boolean |  | True |  | Activate or deactivate IGMP snooping on device level |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inband_management_subnet</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].inband_management_subnet") | String |  |  | Format: ipv4_cidr | Optional IP subnet assigned to Inband Management SVI on l2leafs in default VRF.<br>Parent l3leafs will have SVI with "ip virtual-router" and host-route injection based on ARP. This allows all l3leafs to reuse the same subnet<br>SVI IP address will be assigned as follows:<br>virtual-router: <subnet> + 1<br>l3leaf A      : <subnet> + 2 (same IP on all l3leaf A)<br>l3leaf B      : <subnet> + 3 (same IP on all l3leaf B)<br>l2leafs       : <subnet> + 3 + <l2leaf id><br>GW on l2leafs : <subnet> + 1<br>Assign range larger than total l2leafs + 5<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inband_management_vlan</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].inband_management_vlan") | Integer |  | 4092 |  | VLAN number assigned to Inband Management SVI on l2leafs in default VRF |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;is_type</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].is_type") | String |  | level-2 | Valid Values:<br>- level-1-2<br>- level-1<br>- level-2 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_maximum_paths</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].isis_maximum_paths") | Integer |  |  |  | Number of path to configure in ECMP for ISIS |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_system_id_prefix</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].isis_system_id_prefix") | String |  |  | Pattern: [0-9a-f]{4}\.[0-9a-f]{4} | (4.4 hexadecimal) |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;lacp_port_id_range</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].lacp_port_id_range") | Dictionary |  |  |  | This will generate the "lacp port-id range", "begin" and "end" values based on node "id" and the number of nodes in the "node_group".<br>Unique LACP port-id ranges are recommended for EVPN Multihoming designs.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].lacp_port_id_range.enabled") | Boolean |  | False |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;offset</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].lacp_port_id_range.offset") | Integer |  | 0 |  | Offset is used to avoid overlapping port-id ranges of different switches<br>Useful when a "connected-endpoint" is connected to switches in different "node_groups".<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;size</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].lacp_port_id_range.size") | Integer |  | 128 |  | Recommended size > = number of ports in the switch. |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;link_tracking</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].link_tracking") | Dictionary |  |  |  | This configures the Link Tracking Group on a switch as well as adds the p2p-uplinks of the switch as the upstream interfaces.<br>Useful in EVPN multhoming designs.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].link_tracking.enabled") | Boolean |  | False |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;groups</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].link_tracking.groups") | List, items: Dictionary |  | [{'name': 'LT_GROUP1'}] |  | By default a single group named "LT_GROUP1" is defined with default values.<br>Any groups defined under "groups" will replace the default.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- links_minimum</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].link_tracking.groups.[].links_minimum") | Integer |  |  | Min: 1<br>Max: 100000 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].link_tracking.groups.[].name") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;recovery_delay</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].link_tracking.groups.[].recovery_delay") | Integer |  |  | Min: 0<br>Max: 3600 | default -> platform_settings_mlag_reload_delay -> 300 |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loopback_ipv4_offset</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].loopback_ipv4_offset") | Integer |  | 0 |  | Offset all assigned loopback IP addresses.<br>Required when the < loopback_ipv4_pool > is same for 2 different node_types (like spine and l3leaf) to avoid over-lapping IPs.<br>For example, set the minimum offset l3leaf.defaults.loopback_ipv4_offset: < total # spine switches > or vice versa.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loopback_ipv4_pool</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].loopback_ipv4_pool") | String |  |  | Format: ipv4_cidr | IPv4 subnet for Loopback0 allocation |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loopback_ipv6_offset</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].loopback_ipv6_offset") | Integer |  | 0 |  | Offset all assigned loopback IPv6 addresses.<br>Required when the < loopback_ipv6_pool > is same for 2 different node_types (like spine and l3leaf) to avoid overlapping IPs.<br>For example, set the minimum offset l3leaf.defaults.loopback_ipv6_offset: < total # spine switches > or vice versa.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loopback_ipv6_pool</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].loopback_ipv6_pool") | String |  |  | Format: ipv6_cidr | IPv6 subnet for Loopback0 allocation |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;max_parallel_uplinks</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].max_parallel_uplinks") | Integer |  |  |  | Number of parallel links towards uplink switches |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;max_uplink_switches</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].max_uplink_switches") | Integer |  |  |  | Maximum number of uplink switches.<br>Changing this value may change IP Addressing on uplinks.<br>Can be used to reserve IP space for future expansions.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mgmt_interface</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].mgmt_interface") | String |  |  |  | Management Interface Name<br>Default -> platform_management_interface -> mgmt_interface -> "Management1"<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mgmt_ip</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].mgmt_ip") | String |  |  | Format: cidr | Management Interface IP Address |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;node_sid_base</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].node_sid_base") | Integer |  | 0 |  | Node-SID base for isis-sr underlay variants. Combined with node id to generate ISIS-SR node-SID. |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;platform</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].platform") | String |  |  |  | Arista platform family |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rack</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].rack") | String |  |  |  | Rack that the switch is located in (only used in snmp_settings location) |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the root level of the final EOS configuration |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;short_esi</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].short_esi") | String |  |  |  | short_esi only valid for l2leaf devices using port-channel uplink<br>Setting short_esi to "auto" generates the short_esi automatically using a hash of configuration elements.<br>< 0000:0000:0000 | auto ><br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_mode</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].spanning_tree_mode") | String |  |  | Valid Values:<br>- mstp<br>- rstp<br>- rapid-pvst<br>- none |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_priority</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].spanning_tree_priority") | Integer |  | 32768 |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_root_super</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].spanning_tree_root_super") | Boolean |  | False |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].structured_config") | Dictionary |  |  |  | Custom structured config for eos_cli_config_gen |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_interface_speed</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].uplink_interface_speed") | String |  |  |  | Point-to-Point interface speed - will apply to uplinks on both ends<br>< interface_speed | forced interface_speed | auto interface_speed ><br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_interfaces</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].uplink_interfaces") | List, items: String |  |  |  | Local uplink interfaces |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].uplink_interfaces.[].&lt;str&gt;") | String |  |  | Pattern: Ethernet[\d/]+ |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_ipv4_pool</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].uplink_ipv4_pool") | String |  |  | Format: ipv4_cidr | IPv4 subnet to use to connect to uplink switches |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_macsec</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].uplink_macsec") | Dictionary |  |  |  | Enable MacSec on all uplinks |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;profile</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].uplink_macsec.profile") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_ptp</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].uplink_ptp") | Dictionary |  |  |  | Enable PTP on all infrastructure links |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enable</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].uplink_ptp.enable") | Boolean |  | False |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_switch_interfaces</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].uplink_switch_interfaces") | List, items: String |  |  |  | Interfaces located on uplink switches |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].uplink_switch_interfaces.[].&lt;str&gt;") | String |  |  | Pattern: Ethernet[\d/]+ |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_switches</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].uplink_switches") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].uplink_switches.[].&lt;str&gt;") | String |  |  |  | Hostname of uplink switch |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;virtual_router_mac_address</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].virtual_router_mac_address") | String |  |  | Format: mac | Virtual router mac address for anycast gateway |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vtep_loopback</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].vtep_loopback") | String |  |  | Pattern: Loopback[\d/]+ | Set VXLAN source interface. |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vtep_loopback_ipv4_pool</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].vtep_loopback_ipv4_pool") | String |  |  | Format: ipv4_cidr | IPv4 subnet for VTEP-Loopback allocation |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mac_address</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].mac_address") | String |  |  |  | `mac_address` can only be set under the node and is used by the `arista.avd.dhcp_provisioner` role |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].name") | String | Required, Unique |  |  | The Node Name is used as "hostname" |

### YAML

```yaml
<node_type_keys.key>:
  defaults:
    bgp_as: <str>
    bgp_defaults:
      - <str>
    evpn_gateway:
      evpn_l2:
        enabled: <bool>
      evpn_l3:
        enabled: <bool>
        inter_domain: <bool>
      remote_peers:
        - bgp_as: <str>
          hostname: <str>
          ip_address: <str>
    evpn_role: <str>
    evpn_route_servers:
      - <str>
    evpn_services_l2_only: <bool>
    filter:
      always_include_vrfs_in_tenants:
        - <str>
      tags:
        - <str>
      tenants:
        - <str>
    id: <int>
    igmp_snooping_enabled: <bool>
    inband_management_subnet: <str>
    inband_management_vlan: <int>
    is_type: <str>
    isis_maximum_paths: <int>
    isis_system_id_prefix: <str>
    lacp_port_id_range:
      enabled: <bool>
      offset: <int>
      size: <int>
    link_tracking:
      enabled: <bool>
      groups:
        - links_minimum: <int>
          name: <str>
          recovery_delay: <int>
    loopback_ipv4_offset: <int>
    loopback_ipv4_pool: <str>
    loopback_ipv6_offset: <int>
    loopback_ipv6_pool: <str>
    max_parallel_uplinks: <int>
    max_uplink_switches: <int>
    mgmt_interface: <str>
    mgmt_ip: <str>
    node_sid_base: <int>
    platform: <str>
    rack: <str>
    raw_eos_cli: <str>
    short_esi: <str>
    spanning_tree_mode: <str>
    spanning_tree_priority: <int>
    spanning_tree_root_super: <bool>
    structured_config:
    uplink_interface_speed: <str>
    uplink_interfaces:
      - <str>
    uplink_ipv4_pool: <str>
    uplink_macsec:
      profile: <str>
    uplink_ptp:
      enable: <bool>
    uplink_switch_interfaces:
      - <str>
    uplink_switches:
      - <str>
    virtual_router_mac_address: <str>
    vtep_loopback: <str>
    vtep_loopback_ipv4_pool: <str>
  node_groups:
    - bgp_as: <str>
      bgp_defaults:
        - <str>
      evpn_gateway:
        evpn_l2:
          enabled: <bool>
        evpn_l3:
          enabled: <bool>
          inter_domain: <bool>
        remote_peers:
          - bgp_as: <str>
            hostname: <str>
            ip_address: <str>
      evpn_role: <str>
      evpn_route_servers:
        - <str>
      evpn_services_l2_only: <bool>
      filter:
        always_include_vrfs_in_tenants:
          - <str>
        tags:
          - <str>
        tenants:
          - <str>
      id: <int>
      igmp_snooping_enabled: <bool>
      inband_management_subnet: <str>
      inband_management_vlan: <int>
      is_type: <str>
      isis_maximum_paths: <int>
      isis_system_id_prefix: <str>
      lacp_port_id_range:
        enabled: <bool>
        offset: <int>
        size: <int>
      link_tracking:
        enabled: <bool>
        groups:
          - links_minimum: <int>
            name: <str>
            recovery_delay: <int>
      loopback_ipv4_offset: <int>
      loopback_ipv4_pool: <str>
      loopback_ipv6_offset: <int>
      loopback_ipv6_pool: <str>
      max_parallel_uplinks: <int>
      max_uplink_switches: <int>
      mgmt_interface: <str>
      mgmt_ip: <str>
      node_sid_base: <int>
      platform: <str>
      rack: <str>
      raw_eos_cli: <str>
      short_esi: <str>
      spanning_tree_mode: <str>
      spanning_tree_priority: <int>
      spanning_tree_root_super: <bool>
      structured_config:
      uplink_interface_speed: <str>
      uplink_interfaces:
        - <str>
      uplink_ipv4_pool: <str>
      uplink_macsec:
        profile: <str>
      uplink_ptp:
        enable: <bool>
      uplink_switch_interfaces:
        - <str>
      uplink_switches:
        - <str>
      virtual_router_mac_address: <str>
      vtep_loopback: <str>
      vtep_loopback_ipv4_pool: <str>
      group: <str>
      nodes:
        - bgp_as: <str>
          bgp_defaults:
            - <str>
          evpn_gateway:
            evpn_l2:
              enabled: <bool>
            evpn_l3:
              enabled: <bool>
              inter_domain: <bool>
            remote_peers:
              - bgp_as: <str>
                hostname: <str>
                ip_address: <str>
          evpn_role: <str>
          evpn_route_servers:
            - <str>
          evpn_services_l2_only: <bool>
          filter:
            always_include_vrfs_in_tenants:
              - <str>
            tags:
              - <str>
            tenants:
              - <str>
          id: <int>
          igmp_snooping_enabled: <bool>
          inband_management_subnet: <str>
          inband_management_vlan: <int>
          is_type: <str>
          isis_maximum_paths: <int>
          isis_system_id_prefix: <str>
          lacp_port_id_range:
            enabled: <bool>
            offset: <int>
            size: <int>
          link_tracking:
            enabled: <bool>
            groups:
              - links_minimum: <int>
                name: <str>
                recovery_delay: <int>
          loopback_ipv4_offset: <int>
          loopback_ipv4_pool: <str>
          loopback_ipv6_offset: <int>
          loopback_ipv6_pool: <str>
          max_parallel_uplinks: <int>
          max_uplink_switches: <int>
          mgmt_interface: <str>
          mgmt_ip: <str>
          node_sid_base: <int>
          platform: <str>
          rack: <str>
          raw_eos_cli: <str>
          short_esi: <str>
          spanning_tree_mode: <str>
          spanning_tree_priority: <int>
          spanning_tree_root_super: <bool>
          structured_config:
          uplink_interface_speed: <str>
          uplink_interfaces:
            - <str>
          uplink_ipv4_pool: <str>
          uplink_macsec:
            profile: <str>
          uplink_ptp:
            enable: <bool>
          uplink_switch_interfaces:
            - <str>
          uplink_switches:
            - <str>
          virtual_router_mac_address: <str>
          vtep_loopback: <str>
          vtep_loopback_ipv4_pool: <str>
          mac_address: <str>
          name: <str>
  nodes:
    - bgp_as: <str>
      bgp_defaults:
        - <str>
      evpn_gateway:
        evpn_l2:
          enabled: <bool>
        evpn_l3:
          enabled: <bool>
          inter_domain: <bool>
        remote_peers:
          - bgp_as: <str>
            hostname: <str>
            ip_address: <str>
      evpn_role: <str>
      evpn_route_servers:
        - <str>
      evpn_services_l2_only: <bool>
      filter:
        always_include_vrfs_in_tenants:
          - <str>
        tags:
          - <str>
        tenants:
          - <str>
      id: <int>
      igmp_snooping_enabled: <bool>
      inband_management_subnet: <str>
      inband_management_vlan: <int>
      is_type: <str>
      isis_maximum_paths: <int>
      isis_system_id_prefix: <str>
      lacp_port_id_range:
        enabled: <bool>
        offset: <int>
        size: <int>
      link_tracking:
        enabled: <bool>
        groups:
          - links_minimum: <int>
            name: <str>
            recovery_delay: <int>
      loopback_ipv4_offset: <int>
      loopback_ipv4_pool: <str>
      loopback_ipv6_offset: <int>
      loopback_ipv6_pool: <str>
      max_parallel_uplinks: <int>
      max_uplink_switches: <int>
      mgmt_interface: <str>
      mgmt_ip: <str>
      node_sid_base: <int>
      platform: <str>
      rack: <str>
      raw_eos_cli: <str>
      short_esi: <str>
      spanning_tree_mode: <str>
      spanning_tree_priority: <int>
      spanning_tree_root_super: <bool>
      structured_config:
      uplink_interface_speed: <str>
      uplink_interfaces:
        - <str>
      uplink_ipv4_pool: <str>
      uplink_macsec:
        profile: <str>
      uplink_ptp:
        enable: <bool>
      uplink_switch_interfaces:
        - <str>
      uplink_switches:
        - <str>
      virtual_router_mac_address: <str>
      vtep_loopback: <str>
      vtep_loopback_ipv4_pool: <str>
      mac_address: <str>
      name: <str>
```
