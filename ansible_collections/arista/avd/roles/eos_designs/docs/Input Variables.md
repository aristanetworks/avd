!!! warning
    This document describes the data model for AVD 4.x. It may or may not work in previous versions.

## BFD Multihop tuning

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>bfd_multihop</samp>](## "bfd_multihop") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;interval</samp>](## "bfd_multihop.interval") | Integer |  | 300 |  |  |
| [<samp>&nbsp;&nbsp;min_rx</samp>](## "bfd_multihop.min_rx") | Integer |  | 300 |  |  |
| [<samp>&nbsp;&nbsp;multiplier</samp>](## "bfd_multihop.multiplier") | Integer |  | 3 |  |  |

### YAML

```yaml
bfd_multihop:
  interval: <int>
  min_rx: <int>
  multiplier: <int>
```

## BGP AS

### Description

AS number to use to configure overlay when "overlay_routing_protocol" == IBGP
### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>bgp_as</samp>](## "bgp_as") | String |  |  |  |  |

### YAML

```yaml
bgp_as: <str>
```

## BGP ECMP

### Description

Maximum ECMP for BGP multi-path
### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>bgp_ecmp</samp>](## "bgp_ecmp") | Integer |  | 4 |  |  |

### YAML

```yaml
bgp_ecmp: <int>
```

## BGP Maximum Paths

### Description

Maximum Paths for BGP multi-path
### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>bgp_maximum_paths</samp>](## "bgp_maximum_paths") | Integer |  | 4 |  |  |

### YAML

```yaml
bgp_maximum_paths: <int>
```

## BGP Mesh Pes

### Description

BGP Mesh PES
### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>bgp_mesh_pes</samp>](## "bgp_mesh_pes") | Boolean |  | False |  |  |

### YAML

```yaml
bgp_mesh_pes: <bool>
```

## BGP peer group names and encrypted password

### Description

Leverage an Arista EOS switch to generate the encrypted password using the correct peer group name.
Note that the name of the peer groups use '-' instead of '_' in EOS configuration.

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>bgp_peer_groups</samp>](## "bgp_peer_groups") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;EVPN_OVERLAY_PEERS</samp>](## "bgp_peer_groups.EVPN_OVERLAY_PEERS") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "bgp_peer_groups.EVPN_OVERLAY_PEERS.name") | String |  | EVPN-OVERLAY-PEERS |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;password</samp>](## "bgp_peer_groups.EVPN_OVERLAY_PEERS.password") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;IPv4_UNDERLAY_PEERS</samp>](## "bgp_peer_groups.IPv4_UNDERLAY_PEERS") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "bgp_peer_groups.IPv4_UNDERLAY_PEERS.name") | String |  | IPv4-UNDERLAY-PEERS |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;password</samp>](## "bgp_peer_groups.IPv4_UNDERLAY_PEERS.password") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;MLAG_IPv4_UNDERLAY_PEER</samp>](## "bgp_peer_groups.MLAG_IPv4_UNDERLAY_PEER") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "bgp_peer_groups.MLAG_IPv4_UNDERLAY_PEER.name") | String |  | MLAG-IPv4-UNDERLAY-PEER |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;password</samp>](## "bgp_peer_groups.MLAG_IPv4_UNDERLAY_PEER.password") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;evpn_overlay_core</samp>](## "bgp_peer_groups.evpn_overlay_core") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "bgp_peer_groups.evpn_overlay_core.name") | String |  | EVPN-OVERLAY-CORE |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;password</samp>](## "bgp_peer_groups.evpn_overlay_core.password") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;evpn_overlay_peers</samp>](## "bgp_peer_groups.evpn_overlay_peers") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "bgp_peer_groups.evpn_overlay_peers.name") | String |  | EVPN-OVERLAY-PEERS |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;password</samp>](## "bgp_peer_groups.evpn_overlay_peers.password") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;ipv4_underlay_peers</samp>](## "bgp_peer_groups.ipv4_underlay_peers") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "bgp_peer_groups.ipv4_underlay_peers.name") | String |  | IPv4-UNDERLAY-PEERS |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;password</samp>](## "bgp_peer_groups.ipv4_underlay_peers.password") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;mlag_ipv4_underlay_peer</samp>](## "bgp_peer_groups.mlag_ipv4_underlay_peer") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "bgp_peer_groups.mlag_ipv4_underlay_peer.name") | String |  | MLAG-IPv4-UNDERLAY-PEER |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;password</samp>](## "bgp_peer_groups.mlag_ipv4_underlay_peer.password") | String |  |  |  |  |

### YAML

```yaml
bgp_peer_groups:
  EVPN_OVERLAY_PEERS:
    name: <str>
    password: <str>
  IPv4_UNDERLAY_PEERS:
    name: <str>
    password: <str>
  MLAG_IPv4_UNDERLAY_PEER:
    name: <str>
    password: <str>
  evpn_overlay_core:
    name: <str>
    password: <str>
  evpn_overlay_peers:
    name: <str>
    password: <str>
  ipv4_underlay_peers:
    name: <str>
    password: <str>
  mlag_ipv4_underlay_peer:
    name: <str>
    password: <str>
```

## Default IGMP Snooping enabled

### Description

Disable IGMP snooping at fabric level.
If set, it overrides per vlan settings

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>default_igmp_snooping_enabled</samp>](## "default_igmp_snooping_enabled") | Boolean |  | True |  |  |

### YAML

```yaml
default_igmp_snooping_enabled: <bool>
```

## Default Node Types

### Description

Uses hostname matches against a regular expression to determine the node type.
### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>default_node_types</samp>](## "default_node_types") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;- match_hostnames</samp>](## "default_node_types.[].match_hostnames") | List, items: String | Required |  |  | Regular expressions to match against hostnames |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "default_node_types.[].match_hostnames.[].&lt;str&gt;") | String | Required |  |  | Regex needs to match full hostname (i.e. is bounded by ^ and $ elements) |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;node_type</samp>](## "default_node_types.[].node_type") | String | Required, Unique |  |  | Resulting node type when regex matches |

### YAML

```yaml
default_node_types:
  - match_hostnames:
      - <str>
    node_type: <str>
```

## AVD Design

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>design</samp>](## "design") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;type</samp>](## "design.type") | String |  | l3ls-evpn | Valid Values:<br>- l3ls-evpn<br>- mpls | By setting the `design.type` to `mpls`,<br>the default node-types and templates described in these documents will be used.<br> |

### YAML

```yaml
design:
  type: <str>
```

## Enable Trunk Group support across eos_designs

### Description

Warning: Because of the nature of the EOS Trunk Group feature, enabling this is "all or nothing".
*All* vlans and *all* trunks towards connected endpoints must be using trunk groups as well.
If trunk groups are not assigned to a trunk, no vlans will be enabled on that trunk.
See "Details on enable_trunk_groups" below before enabling this feature

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>enable_trunk_groups</samp>](## "enable_trunk_groups") | Boolean |  | False |  |  |

### YAML

```yaml
enable_trunk_groups: <bool>
```

## EVPN Gateway EBGP Multihop

### Description

Default of 15, considering a large value to avoid BGP reachability issues in very complex DCI networks.
Adapt the value for your specific topology.

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>evpn_ebgp_gateway_multihop</samp>](## "evpn_ebgp_gateway_multihop") | Integer |  | 15 |  |  |

### YAML

```yaml
evpn_ebgp_gateway_multihop: <int>
```

## EVPN EBGP Multihop

### Description

Default of 3, the recommended value for a 3 stage spine and leaf topology.
Set to a higher value to allow for very large and complex topologies.

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>evpn_ebgp_multihop</samp>](## "evpn_ebgp_multihop") | Integer |  | 3 |  |  |

### YAML

```yaml
evpn_ebgp_multihop: <int>
```

## EVPN Host Flapping Settings

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>evpn_hostflap_detection</samp>](## "evpn_hostflap_detection") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;enabled</samp>](## "evpn_hostflap_detection.enabled") | Boolean |  | True |  | If set to false it will disable EVPN host-flap detection |
| [<samp>&nbsp;&nbsp;expiry_timeout</samp>](## "evpn_hostflap_detection.expiry_timeout") | Integer |  |  |  | Time (in seconds) to purge a MAC duplication issue |
| [<samp>&nbsp;&nbsp;threshold</samp>](## "evpn_hostflap_detection.threshold") | Integer |  | 5 |  | Minimum number of MAC moves that indicate a MAC duplication issue |
| [<samp>&nbsp;&nbsp;window</samp>](## "evpn_hostflap_detection.window") | Integer |  | 180 |  | Time (in seconds) to detect a MAC duplication issue |

### YAML

```yaml
evpn_hostflap_detection:
  enabled: <bool>
  expiry_timeout: <int>
  threshold: <int>
  window: <int>
```

## EVPN Import Pruning

### Description

Enable VPN import pruning (Min. EOS 4.24.2F)
The Route Target extended communities carried by incoming VPN paths will
be examined. If none of those Route Targets have been configured for import,
the path will be immediately discarded

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>evpn_import_pruning</samp>](## "evpn_import_pruning") | Boolean |  | False |  |  |

### YAML

```yaml
evpn_import_pruning: <bool>
```

## Enable Fabric to support EVPN Multicast

### Description

General Configuration required for EVPN Multicast. "evpn_l2_multicast" must also be configured under the Network Services (tenants).
Requires "underlay_multicast: true" and IGMP snooping enabled globally (default).
For MLAG devices Route Distinguisher must be unique since this feature will create multi-vtep configuration.
Warning !!! For Trident3 based platforms i.e 7050X3, 7300X3, 720XP and 722XP
  The Following default platform setting will be configured: "platform trident forwarding-table partition flexible exact-match 16384 l2-shared 98304 l3-shared 131072"
  All forwarding agents will be restarted when this configuration is applied.
  You can tune the settings by overridding the default variable: "platform_settings[platforms].trident_forwarding_table_partition:"
  Please contact an Arista representative for help with determining the appropriate values for your environment.

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>evpn_multicast</samp>](## "evpn_multicast") | Boolean |  | False |  |  |

### YAML

```yaml
evpn_multicast: <bool>
```

## EVPN Overlay BGP RTC

### Description

Enable Route Target Membership Constraint Address Family on EVPN overlay BGP peerings (Min. EOS 4.25.1F)
Requires use eBGP as overlay protocol.

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>evpn_overlay_bgp_rtc</samp>](## "evpn_overlay_bgp_rtc") | Boolean |  | False |  |  |

### YAML

```yaml
evpn_overlay_bgp_rtc: <bool>
```

## EVPN Prevent Readvertise to Server

### Description

Configure route-map on eBGP sessions towards route-servers, where prefixes with the peer's ASN in the AS Path are filtered away.
This is very useful in very large scale networks, where convergence will be quicker by not having to return all updates received
from Route-server-1 to Router-server-2 just for Route-server-2 to throw them away because of AS Path loop detection.

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>evpn_prevent_readvertise_to_server</samp>](## "evpn_prevent_readvertise_to_server") | Boolean |  | False |  |  |

### YAML

```yaml
evpn_prevent_readvertise_to_server: <bool>
```

## EVPN Short ESI Prefix

### Description

Configure prefix for "short_esi" values
### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>evpn_short_esi_prefix</samp>](## "evpn_short_esi_prefix") | String |  | 0000:0000: |  |  |

### YAML

```yaml
evpn_short_esi_prefix: <str>
```

## EVPN VLAN-Aware Bundles

### Description

Enable vlan aware bundles for EVPN MAC-VRF
### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>evpn_vlan_aware_bundles</samp>](## "evpn_vlan_aware_bundles") | Boolean |  | False |  |  |

### YAML

```yaml
evpn_vlan_aware_bundles: <bool>
```

## Fabric Name

### Description

Fabric Name, required to match Ansible Group name covering all devices in the Fabric
### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>fabric_name</samp>](## "fabric_name") | String | Required |  |  |  |

### YAML

```yaml
fabric_name: <str>
```

## IPv4 Network/Mask assigned to Inband Management

### Description

Optional IP subnet assigned to Inband Management SVI on l2leafs in default VRF.
Parent l3leafs will have SVI with "ip virtual-router" and host-route injection based on ARP. This allows all l3leafs to reuse the same subnet
SVI IP address will be assigned as follows:
virtual-router: <subnet> + 1
l3leaf A      : <subnet> + 2 (same IP on all l3leaf A)
l3leaf B      : <subnet> + 3 (same IP on all l3leaf B)
l2leafs       : <subnet> + 3 + <l2leaf id>
GW on l2leafs : <subnet> + 1
Assign range larger than total l2leafs + 5
### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>inband_management_subnet</samp>](## "inband_management_subnet") | String |  |  |  |  |

### YAML

```yaml
inband_management_subnet: <str>
```

## Inband Management VLAN

### Description

VLAN number assigned to Inband Management SVI on l2leafs in default VRF.

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>inband_management_vlan</samp>](## "inband_management_vlan") | Integer |  | 4092 |  |  |

### YAML

```yaml
inband_management_vlan: <int>
```

## ISIS Advertise Passive Only

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>isis_advertise_passive_only</samp>](## "isis_advertise_passive_only") | Boolean |  | False |  |  |

### YAML

```yaml
isis_advertise_passive_only: <bool>
```

## Underlay ISIS Area

### Description

Required when "underlay_routing_protocol" == ISIS variants
### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>isis_area_id</samp>](## "isis_area_id") | String |  | 49.0001 |  |  |

### YAML

```yaml
isis_area_id: <str>
```

## ISIS Default IS Type

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>isis_default_is_type</samp>](## "isis_default_is_type") | String |  | level-2 | Valid Values:<br>- level-1-2<br>- level-1<br>- level-2 |  |

### YAML

```yaml
isis_default_is_type: <str>
```

## ISIS TI-LFA

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>isis_ti_lfa</samp>](## "isis_ti_lfa") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;enabled</samp>](## "isis_ti_lfa.enabled") | Boolean |  | False |  |  |
| [<samp>&nbsp;&nbsp;local_convergence_delay</samp>](## "isis_ti_lfa.local_convergence_delay") | Integer |  | 10000 |  | Local convergence delay in mpls |
| [<samp>&nbsp;&nbsp;protection</samp>](## "isis_ti_lfa.protection") | String |  |  | Valid Values:<br>- link<br>- node |  |

### YAML

```yaml
isis_ti_lfa:
  enabled: <bool>
  local_convergence_delay: <int>
  protection: <str>
```

## Node Type Keys

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>node_type_keys</samp>](## "node_type_keys") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;- connected_endpoints</samp>](## "node_type_keys.[].connected_endpoints") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;default_evpn_role</samp>](## "node_type_keys.[].default_evpn_role") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;default_underlay_routing_protocol</samp>](## "node_type_keys.[].default_underlay_routing_protocol") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;interface_descriptions</samp>](## "node_type_keys.[].interface_descriptions") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;connected_endpoints_ethernet_interfaces</samp>](## "node_type_keys.[].interface_descriptions.connected_endpoints_ethernet_interfaces") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;connected_endpoints_port_channel_interfaces</samp>](## "node_type_keys.[].interface_descriptions.connected_endpoints_port_channel_interfaces") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;overlay_loopback_interface</samp>](## "node_type_keys.[].interface_descriptions.overlay_loopback_interface") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;underlay_ethernet_interfaces</samp>](## "node_type_keys.[].interface_descriptions.underlay_ethernet_interfaces") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;underlay_ethernet_mlag_interfaces</samp>](## "node_type_keys.[].interface_descriptions.underlay_ethernet_mlag_interfaces") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;underlay_port_channel_interfaces</samp>](## "node_type_keys.[].interface_descriptions.underlay_port_channel_interfaces") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;underlay_port_channel_mlag_interfaces</samp>](## "node_type_keys.[].interface_descriptions.underlay_port_channel_mlag_interfaces") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vtep_loopback_interface</samp>](## "node_type_keys.[].interface_descriptions.vtep_loopback_interface") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_addressing</samp>](## "node_type_keys.[].ip_addressing") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_ip_primary</samp>](## "node_type_keys.[].ip_addressing.mlag_ip_primary") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_ip_secondary</samp>](## "node_type_keys.[].ip_addressing.mlag_ip_secondary") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_l3_ip_primary</samp>](## "node_type_keys.[].ip_addressing.mlag_l3_ip_primary") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_l3_ip_secondary</samp>](## "node_type_keys.[].ip_addressing.mlag_l3_ip_secondary") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;p2p_uplinks_ip</samp>](## "node_type_keys.[].ip_addressing.p2p_uplinks_ip") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;p2p_uplinks_peer_ip</samp>](## "node_type_keys.[].ip_addressing.p2p_uplinks_peer_ip") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;router_id</samp>](## "node_type_keys.[].ip_addressing.router_id") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vtep_ip</samp>](## "node_type_keys.[].ip_addressing.vtep_ip") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vtep_ip_mlag</samp>](## "node_type_keys.[].ip_addressing.vtep_ip_mlag") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;key</samp>](## "node_type_keys.[].key") | String | Required, Unique |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mlag_support</samp>](## "node_type_keys.[].mlag_support") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mpls_lsr</samp>](## "node_type_keys.[].mpls_lsr") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;network_services</samp>](## "node_type_keys.[].network_services") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;l2</samp>](## "node_type_keys.[].network_services.l2") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;l3</samp>](## "node_type_keys.[].network_services.l3") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "node_type_keys.[].type") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;underlay_router</samp>](## "node_type_keys.[].underlay_router") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;uplink_type</samp>](## "node_type_keys.[].uplink_type") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vtep</samp>](## "node_type_keys.[].vtep") | Boolean |  |  |  |  |

### YAML

```yaml
node_type_keys:
  - connected_endpoints: <bool>
    default_evpn_role: <str>
    default_underlay_routing_protocol: <str>
    interface_descriptions:
      connected_endpoints_ethernet_interfaces: <str>
      connected_endpoints_port_channel_interfaces: <str>
      overlay_loopback_interface: <str>
      underlay_ethernet_interfaces: <str>
      underlay_ethernet_mlag_interfaces: <str>
      underlay_port_channel_interfaces: <str>
      underlay_port_channel_mlag_interfaces: <str>
      vtep_loopback_interface: <str>
    ip_addressing:
      mlag_ip_primary: <str>
      mlag_ip_secondary: <str>
      mlag_l3_ip_primary: <str>
      mlag_l3_ip_secondary: <str>
      p2p_uplinks_ip: <str>
      p2p_uplinks_peer_ip: <str>
      router_id: <str>
      vtep_ip: <str>
      vtep_ip_mlag: <str>
    key: <str>
    mlag_support: <bool>
    mpls_lsr: <bool>
    network_services:
      l2: <bool>
      l3: <bool>
    type: <str>
    underlay_router: <bool>
    uplink_type: <str>
    vtep: <bool>
```

## Only Configure VLAN Trunk Groups used by local endpoints

### Description

A vlan can have many trunk_groups assigned. To avoid unneeded configuration changes on all leaf
switches when a new trunk group is added, this feature will only configure the vlan trunk groups
matched with local connected_endpoints.
See "Details on only_local_vlan_trunk_groups" below.
Requires "enable_trunk_groups: true"

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>only_local_vlan_trunk_groups</samp>](## "only_local_vlan_trunk_groups") | Boolean |  | False |  |  |

### YAML

```yaml
only_local_vlan_trunk_groups: <bool>
```

## Overlay Her Flood List Per VNI

### Description

When using Head-End Replication, configure flood-lists per VNI. | Optional
By default HER will be configured with a common flood-list containing all VTEPs. This behavior can be changed
to per-VNI flood-lists by setting `overlay_her_flood_list_per_vni: true`. This will make `eos_designs` consider
configured VLANs per VTEP, and only include the relevant VTEPs to each VNI's flood-list.

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>overlay_her_flood_list_per_vni</samp>](## "overlay_her_flood_list_per_vni") | Boolean |  | False |  |  |

### YAML

```yaml
overlay_her_flood_list_per_vni: <bool>
```

## Overlay HER Flood List Scope

### Description

When using Head-End Replication, set the scope of flood-lists to Fabric or DC
By default all VTEPs in the Fabric (part of the inventory group referenced by "fabric_name") are added
to the flood-lists. This can be changed to all VTEPs in the DC (part of the inventory group referenced
by "dc_name")
This is useful if Border Leaf switches are dividing the VXLAN overlay into separate domains.

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>overlay_her_flood_list_scope</samp>](## "overlay_her_flood_list_scope") | String |  | fabric | Valid Values:<br>- fabric<br>- dc |  |

### YAML

```yaml
overlay_her_flood_list_scope: <str>
```

## Overlay Loopback Description

### Description

Customizable overlay loopback description
### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>overlay_loopback_description</samp>](## "overlay_loopback_description") | String |  |  |  |  |

### YAML

```yaml
overlay_loopback_description: <str>
```

## Enable RFC 5549(iBGP)

### Description

IPv6 Unnumbered for MLAG iBGP connections.
Requires "underlay_rfc5549: true"

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>overlay_mlag_rfc5549</samp>](## "overlay_mlag_rfc5549") | Boolean |  | False |  |  |

### YAML

```yaml
overlay_mlag_rfc5549: <bool>
```

## Overlay Routing Protocol

### Description

- The following overlay routing protocols are supported:
  - EBGP (default for l3ls-evpn)
  - IBGP (only with OSPF or ISIS variants in underlay)

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>overlay_routing_protocol</samp>](## "overlay_routing_protocol") | String |  | ebgp | Valid Values:<br>- ebgp<br>- ibgp<br>- BGP |  |

### YAML

```yaml
overlay_routing_protocol: <str>
```

## Overlay Routing Protocol Address Family

### Description

Enable overlay EVPN peering with IPv6 addresses | Optional
This feature depends on underlay_ipv6 variable. As of today, only RFC5549 is capable to transport IPv6 in the underlay.

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>overlay_routing_protocol_address_family</samp>](## "overlay_routing_protocol_address_family") | String |  | ipv4 | Valid Values:<br>- ipv4<br>- ipv6 |  |

### YAML

```yaml
overlay_routing_protocol_address_family: <str>
```

## Point to Point Links MTU

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>p2p_uplinks_mtu</samp>](## "p2p_uplinks_mtu") | Integer |  | 9000 |  |  |

### YAML

```yaml
p2p_uplinks_mtu: <int>
```

## P2P Uplinks QoS Profile

### Description

QOS Profile assigned on all infrastructure links
### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>p2p_uplinks_qos_profile</samp>](## "p2p_uplinks_qos_profile") | String |  |  |  |  |

### YAML

```yaml
p2p_uplinks_qos_profile: <str>
```

## POD Name

### Description

POD Name, only used in Fabric Documentation | Optional, fallback to dc_name and then to fabric_name.
Recommended to be common between Spines, Leafs within a POD (One l3ls topology)

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>pod_name</samp>](## "pod_name") | String |  |  |  |  |

### YAML

```yaml
pod_name: <str>
```

## Shutdown Interfaces Towards Undeployed Peers

### Description

- It is possible to provision configurations for a complete topology but flag devices as undeployed using the host level variable `is_deployed: false`.

```yaml
# Use at the host level
is_deployed: < true | false | default -> true >
```

- By default, this will have no impact within the `eos_designs` role. Configs will still be generated by the `eos_cli_config_gen` role and will still be pushed by the `eos_config_deploy_eapi` directly to devices if used.
- However, if the `eos_config_deploy_cvp` role is used to push configurations, CloudVision will ignore the devices flagged  as `is_deployed: false` and not attempt to configure them.
- If the device is not present in the network due to CloudVision not configuring the device, `eos_validate_state` role will fail tests on peers of the undeployed device trying to verify that interfaces are up.
- To overcome this and shutdown interfaces towards undeployed peers, the variable `shutdown_interfaces_towards_undeployed_peers` can be used, satisfying the `eos_validate_state` role interface tests. Again, this is only an issue if `eos_config_deploy_cvp` is used and the devices are not present in the network.
### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>shutdown_interfaces_towards_undeployed_peers</samp>](## "shutdown_interfaces_towards_undeployed_peers") | Boolean |  | False |  |  |

### YAML

```yaml
shutdown_interfaces_towards_undeployed_peers: <bool>
```

## Trunk Group Names

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>trunk_groups</samp>](## "trunk_groups") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;mlag</samp>](## "trunk_groups.mlag") | Dictionary |  |  |  | "mlag" is the Trunk Group used for MLAG VLAN (Typically VLAN 4094)<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "trunk_groups.mlag.name") | String |  | MLAG |  |  |
| [<samp>&nbsp;&nbsp;mlag_l3</samp>](## "trunk_groups.mlag_l3") | Dictionary |  |  |  | "mlag_l3" is the Trunk Group used for MLAG L3 peering VLAN (Typically VLAN 4093)<br>"mlag_l3" is also the Trunk Group used for VRF L3 peering VLANs<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "trunk_groups.mlag_l3.name") | String |  | LEAF_PEER_L3 |  |  |
| [<samp>&nbsp;&nbsp;uplink</samp>](## "trunk_groups.uplink") | Dictionary |  |  |  | "uplink" is the Trunk Group used on L2 Leaf switches when "enable_trunk_groups" is set<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "trunk_groups.uplink.name") | String |  | UPLINK |  |  |

### YAML

```yaml
trunk_groups:
  mlag:
    name: <str>
  mlag_l3:
    name: <str>
  uplink:
    name: <str>
```

## Device Type

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>type</samp>](## "type") | String | Required |  | Valid Values:<br>- <value(s) of node_type_keys.type> |  |

### YAML

```yaml
type: <str>
```

## Underlay Filter Peer AS

### Description

Configure route-map on eBGP sessions towards underlay peers, where prefixes with the peer's ASN in the AS Path are filtered away.
This is very useful in very large scale networks not using EVPN overlays, where convergence will be quicker by not having to return
all updates received from Spine-1 to Spine-2 just for Spine-2 to throw them away because of AS Path loop detection.
Note this key is ignored when EVPN is configured.

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>underlay_filter_peer_as</samp>](## "underlay_filter_peer_as") | String |  | 0000:0000: |  |  |

### YAML

```yaml
underlay_filter_peer_as: <str>
```

## Enable IPv6 Address Family on underlay

### Description

This feature allows IPv6 underlay routing protocol with RFC5549 addresses to be used along with IPv4 advertisements as VXLAN tunnel endpoints.
Requires "underlay_rfc5549: true" and "loopback_ipv6_pool" under the "Fabric Topology"

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>underlay_ipv6</samp>](## "underlay_ipv6") | Boolean |  | False |  |  |

### YAML

```yaml
underlay_ipv6: <bool>
```

## Underlay ISIS Instance Name

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>underlay_isis_instance_name</samp>](## "underlay_isis_instance_name") | String |  | EVPN_UNDERLAY |  |  |

### YAML

```yaml
underlay_isis_instance_name: <str>
```

## Underlay Multicast

### Description

Enable Multicast in the underlay on all p2p uplink interfaces and mlag l3 peer interface.
Specifically PIM Sparse-Mode will be configured on all routed underlay interfaces.
No other configuration is added, so the underlay will only support Source-Specific Multicast (SSM)
The configuration is intended to be used as multicast underlay for EVPN OISM overlay

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>underlay_multicast</samp>](## "underlay_multicast") | Boolean |  | False |  |  |

### YAML

```yaml
underlay_multicast: <bool>
```

## Underlay OSPF Area

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>underlay_ospf_area</samp>](## "underlay_ospf_area") | String |  | 0.0.0.0 | Format: ipv4 |  |

### YAML

```yaml
underlay_ospf_area: <str>
```

## Enable Underlay OSPF BFD

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>underlay_ospf_bfd_enable</samp>](## "underlay_ospf_bfd_enable") | Boolean |  | False |  |  |

### YAML

```yaml
underlay_ospf_bfd_enable: <bool>
```

## Underlay OSPF Max LSA

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>underlay_ospf_max_lsa</samp>](## "underlay_ospf_max_lsa") | Integer |  | 12000 |  |  |

### YAML

```yaml
underlay_ospf_max_lsa: <int>
```

## Underlay OSPF Process ID

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>underlay_ospf_process_id</samp>](## "underlay_ospf_process_id") | Integer |  | 100 |  |  |

### YAML

```yaml
underlay_ospf_process_id: <int>
```

## Enable RFC5549 in Underlay

### Description

Point to Point Underlay with RFC 5549(eBGP), i.e. IPv6 Unnumbered
Requires "underlay_routing_protocol: ebgp"

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>underlay_rfc5549</samp>](## "underlay_rfc5549") | Boolean |  | False |  |  |

### YAML

```yaml
underlay_rfc5549: <bool>
```

## Underlay Routing Protocol

### Description

- The following underlay routing protocols are supported:
  - EBGP (default for l3ls-evpn)
  - OSPF.
  - ISIS.
  - ISIS-SR*.
  - ISIS-LDP*.
  - ISIS-SR-LDP*.
  - OSPF-LDP*.
- The variables should be applied to all devices in the fabric.

*Only supported with core_interfaces data model.

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>underlay_routing_protocol</samp>](## "underlay_routing_protocol") | String |  | ebgp | Valid Values:<br>- ebgp<br>- ospf<br>- isis<br>- isis-sr<br>- isis-ldp<br>- isis-sr-ldp<br>- ospf-ldp<br>- BGP |  |

### YAML

```yaml
underlay_routing_protocol: <str>
```

## Uplink PTP

### Description

Enable PTP on all infrastructure links
### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>uplink_ptp</samp>](## "uplink_ptp") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;enable</samp>](## "uplink_ptp.enable") | Boolean |  | False |  |  |

### YAML

```yaml
uplink_ptp:
  enable: <bool>
```

## Virtual VTEP IP

### Description

IP Address used as Virtual VTEP. Will be configured as secondary IP on loopback1
This is only needed for centralized routing designs

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>vtep_vvtep_ip</samp>](## "vtep_vvtep_ip") | String |  |  | Format: ipv4_cidr |  |

### YAML

```yaml
vtep_vvtep_ip: <str>
```
