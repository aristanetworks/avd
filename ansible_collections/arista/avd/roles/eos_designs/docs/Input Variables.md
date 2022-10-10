!!! warning
    This document describes the data model for AVD 4.x. It may or may not work in previous versions.

## BFD Multihop tunning

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>bfd_multihop</samp>](## "bfd_multihop") | Dictionary |  |  |  | BFD Multihop tunning |
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
| [<samp>bgp_as</samp>](## "bgp_as") | String |  |  |  | BGP AS |

### YAML

```yaml
bgp_as: <str>
```

## Bgp Ecmp

### Description

Maximum ECMP for BGP multi-path

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>bgp_ecmp</samp>](## "bgp_ecmp") | Integer |  |  |  |  |

### YAML

```yaml
bgp_ecmp: <int>
```

## Bgp Maximum Paths

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

## BGP peer group names and encrypted password

### Description

Leverage an Arista EOS switch to generate the encrypted password using the correct peer group name.
Note that the name of the peer groups use '-' instead of '_' in EOS configuration.

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>bgp_peer_groups</samp>](## "bgp_peer_groups") | Dictionary |  |  |  | BGP peer group names and encrypted password |
| [<samp>&nbsp;&nbsp;EVPN_OVERLAY_PEERS</samp>](## "bgp_peer_groups.EVPN_OVERLAY_PEERS") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "bgp_peer_groups.EVPN_OVERLAY_PEERS.name") | String |  | EVPN-OVERLAY-PEERS |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;password</samp>](## "bgp_peer_groups.EVPN_OVERLAY_PEERS.password") | String |  |  |  | Encrypted Password |
| [<samp>&nbsp;&nbsp;IPv4_UNDERLAY_PEERS</samp>](## "bgp_peer_groups.IPv4_UNDERLAY_PEERS") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "bgp_peer_groups.IPv4_UNDERLAY_PEERS.name") | String |  | IPv4-UNDERLAY-PEERS |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;password</samp>](## "bgp_peer_groups.IPv4_UNDERLAY_PEERS.password") | String |  |  |  | Encrypted Password |
| [<samp>&nbsp;&nbsp;MLAG_IPv4_UNDERLAY_PEER</samp>](## "bgp_peer_groups.MLAG_IPv4_UNDERLAY_PEER") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "bgp_peer_groups.MLAG_IPv4_UNDERLAY_PEER.name") | String |  | MLAG-IPv4-UNDERLAY-PEER |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;password</samp>](## "bgp_peer_groups.MLAG_IPv4_UNDERLAY_PEER.password") | String |  |  |  | Encrypted Password |
| [<samp>&nbsp;&nbsp;evpn_overlay_core</samp>](## "bgp_peer_groups.evpn_overlay_core") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "bgp_peer_groups.evpn_overlay_core.name") | String |  | EVPN-OVERLAY-CORE |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;password</samp>](## "bgp_peer_groups.evpn_overlay_core.password") | String |  |  |  | Encrypted Password |
| [<samp>&nbsp;&nbsp;evpn_overlay_peers</samp>](## "bgp_peer_groups.evpn_overlay_peers") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "bgp_peer_groups.evpn_overlay_peers.name") | String |  | EVPN-OVERLAY-PEERS |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;password</samp>](## "bgp_peer_groups.evpn_overlay_peers.password") | String |  |  |  | Encrypted Password |
| [<samp>&nbsp;&nbsp;ipv4_underlay_peers</samp>](## "bgp_peer_groups.ipv4_underlay_peers") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "bgp_peer_groups.ipv4_underlay_peers.name") | String |  | IPv4-UNDERLAY-PEERS |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;password</samp>](## "bgp_peer_groups.ipv4_underlay_peers.password") | String |  |  |  | Encrypted Password |
| [<samp>&nbsp;&nbsp;mlag_ipv4_underlay_peer</samp>](## "bgp_peer_groups.mlag_ipv4_underlay_peer") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "bgp_peer_groups.mlag_ipv4_underlay_peer.name") | String |  | MLAG-IPv4-UNDERLAY-PEER |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;password</samp>](## "bgp_peer_groups.mlag_ipv4_underlay_peer.password") | String |  |  |  | Encrypted Password |

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

## DC Name

### Description

Optional DC Name, only used in SNMP location and Fabric Documentation.
Recommended to be common between all devices within a Site

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>dc_name</samp>](## "dc_name") | String |  |  |  | DC Name |

### YAML

```yaml
dc_name: <str>
```

## Default IGMP Snooping enabled

### Description

Disable IGMP snooping at fabric level.
If set, it overrides per vlan settings

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>default_igmp_snooping_enabled</samp>](## "default_igmp_snooping_enabled") | Boolean |  | True |  | Default IGMP Snooping enabled |

### YAML

```yaml
default_igmp_snooping_enabled: <bool>
```

## EVPN Gateway EBGP Multihop

### Description

Default of 15, considering a large value to avoid BGP reachability issues in very complex DCI networks.
Adapt the value for your specific topology.

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>evpn_ebgp_gateway_multihop</samp>](## "evpn_ebgp_gateway_multihop") | Integer |  | 15 |  | EVPN Gateway EBGP Multihop |

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
| [<samp>evpn_ebgp_multihop</samp>](## "evpn_ebgp_multihop") | Integer |  | 3 |  | EVPN EBGP Multihop |

### YAML

```yaml
evpn_ebgp_multihop: <int>
```

## EVPN Host Flapping Settings

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>evpn_hostflap_detection</samp>](## "evpn_hostflap_detection") | Dictionary |  |  |  | EVPN Host Flapping Settings |
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
| [<samp>evpn_import_pruning</samp>](## "evpn_import_pruning") | Boolean |  | False |  | EVPN Import Pruning |

### YAML

```yaml
evpn_import_pruning: <bool>
```

## EVPN Overlay BGP RTC

### Description

Enable Route Target Membership Constraint Address Family on EVPN overlay BGP peerings (Min. EOS 4.25.1F)
Requires use eBGP as overlay protocol.

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>evpn_overlay_bgp_rtc</samp>](## "evpn_overlay_bgp_rtc") | Boolean |  | False |  | EVPN Overlay BGP RTC |

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
| [<samp>evpn_prevent_readvertise_to_server</samp>](## "evpn_prevent_readvertise_to_server") | Boolean |  | False |  | EVPN Prevent Readvertise to Server |

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
| [<samp>evpn_short_esi_prefix</samp>](## "evpn_short_esi_prefix") | String |  | 0000:0000: |  | EVPN Short ESI Prefix |

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
| [<samp>evpn_vlan_aware_bundles</samp>](## "evpn_vlan_aware_bundles") | Boolean |  | False |  | EVPN VLAN-Aware Bundles |

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
| [<samp>fabric_name</samp>](## "fabric_name") | String | Required |  |  | Fabric Name |

### YAML

```yaml
fabric_name: <str>
```

## ISIS Advertise Passive Only

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>isis_advertise_passive_only</samp>](## "isis_advertise_passive_only") | Boolean |  | False |  | ISIS Advertise Passive Only |

### YAML

```yaml
isis_advertise_passive_only: <bool>
```

## Underlay ISIS Area

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>isis_area_id</samp>](## "isis_area_id") | String |  | 49.0001 |  | Underlay ISIS Area |

### YAML

```yaml
isis_area_id: <str>
```

## ISIS Default IS Type

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>isis_default_is_type</samp>](## "isis_default_is_type") | String |  | level-2 | Valid Values:<br>- level-1-2<br>- level-1<br>- level-2 | ISIS Default IS Type |

### YAML

```yaml
isis_default_is_type: <str>
```

## ISIS TI-LFA

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>isis_ti_lfa</samp>](## "isis_ti_lfa") | Dictionary |  |  |  | ISIS TI-LFA |
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

## OOB Management Gateway IP

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>mgmt_gateway</samp>](## "mgmt_gateway") | String | Required |  | Format: ipv4 | OOB Management Gateway IP |

### YAML

```yaml
mgmt_gateway: <str>
```

## Node Types Definition

### Description

The node type definition is done under `node_type_keys`. This dictionary defines type of devices you can use in your topologies. Each node type can be configured to fit the role in the network.

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>node_type_keys</samp>](## "node_type_keys") | List, items: Dictionary |  |  |  | Node Types Definition |
| [<samp>&nbsp;&nbsp;- connected_endpoints</samp>](## "node_type_keys.[].connected_endpoints") | Boolean |  | False |  | Support connected endpoints on this node type |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;default_evpn_role</samp>](## "node_type_keys.[].default_evpn_role") | String |  | none | Valid Values:<br>- none<br>- client<br>- server | Default evpn_role. Can be overridden in topology vars |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;default_underlay_routing_protocol</samp>](## "node_type_keys.[].default_underlay_routing_protocol") | String |  | ebgp | Valid Values:<br>- ebgp<br>- ospf<br>- isis<br>- isis-sr<br>- isis-ldp<br>- isis-sr-ldp<br>- ospf-ldp | Set the default underlay routing_protocol.<br>Can be overridden by setting `underlay_routing_protocol` host/group_vars |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;interface_descriptions</samp>](## "node_type_keys.[].interface_descriptions") | Dictionary |  |  |  | Override interface description templates.<br>If not set, the default templates are inherited from `templates.interface_descriptions` |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;connected_endpoints_ethernet_interfaces</samp>](## "node_type_keys.[].interface_descriptions.connected_endpoints_ethernet_interfaces") | String |  |  |  | Path to J2 template |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;connected_endpoints_port_channel_interfaces</samp>](## "node_type_keys.[].interface_descriptions.connected_endpoints_port_channel_interfaces") | String |  |  |  | Path to J2 template |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;overlay_loopback_interface</samp>](## "node_type_keys.[].interface_descriptions.overlay_loopback_interface") | String |  |  |  | Path to J2 template |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;underlay_ethernet_interfaces</samp>](## "node_type_keys.[].interface_descriptions.underlay_ethernet_interfaces") | String |  |  |  | Path to J2 template |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;underlay_ethernet_mlag_interfaces</samp>](## "node_type_keys.[].interface_descriptions.underlay_ethernet_mlag_interfaces") | String |  |  |  | Path to J2 template |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;underlay_port_channel_interfaces</samp>](## "node_type_keys.[].interface_descriptions.underlay_port_channel_interfaces") | String |  |  |  | Path to J2 template |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;underlay_port_channel_mlag_interfaces</samp>](## "node_type_keys.[].interface_descriptions.underlay_port_channel_mlag_interfaces") | String |  |  |  | Path to J2 template |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vtep_loopback_interface</samp>](## "node_type_keys.[].interface_descriptions.vtep_loopback_interface") | String |  |  |  | Path to J2 template |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_addressing</samp>](## "node_type_keys.[].ip_addressing") | Dictionary |  |  |  | Override IP adressing templates.<br>If not set, the default templates are inherited from `templates.ip_addressing` |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_ip_primary</samp>](## "node_type_keys.[].ip_addressing.mlag_ip_primary") | String |  |  |  | Path to J2 template |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_ip_secondary</samp>](## "node_type_keys.[].ip_addressing.mlag_ip_secondary") | String |  |  |  | Path to J2 template |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_l3_ip_primary</samp>](## "node_type_keys.[].ip_addressing.mlag_l3_ip_primary") | String |  |  |  | Path to J2 template |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_l3_ip_secondary</samp>](## "node_type_keys.[].ip_addressing.mlag_l3_ip_secondary") | String |  |  |  | Path to J2 template |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;p2p_uplinks_ip</samp>](## "node_type_keys.[].ip_addressing.p2p_uplinks_ip") | String |  |  |  | Path to J2 template |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;p2p_uplinks_peer_ip</samp>](## "node_type_keys.[].ip_addressing.p2p_uplinks_peer_ip") | String |  |  |  | Path to J2 template |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;router_id</samp>](## "node_type_keys.[].ip_addressing.router_id") | String |  |  |  | Path to J2 template |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vtep_ip</samp>](## "node_type_keys.[].ip_addressing.vtep_ip") | String |  |  |  | Path to J2 template |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vtep_ip_mlag</samp>](## "node_type_keys.[].ip_addressing.vtep_ip_mlag") | String |  |  |  | Path to J2 template |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;key</samp>](## "node_type_keys.[].key") | String | Required, Unique |  |  | YAML Key used for defining Fabric Topology for this Node Type |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mlag_support</samp>](## "node_type_keys.[].mlag_support") | Boolean |  | False |  | Support MLAG on this node type |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mpls_lsr</samp>](## "node_type_keys.[].mpls_lsr") | Boolean |  | False |  | Is this node type a MPLS LSR |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;network_services</samp>](## "node_type_keys.[].network_services") | Dictionary |  |  |  | Support Network Services on this node type |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;l2</samp>](## "node_type_keys.[].network_services.l2") | Boolean |  | False |  | Support L2 Network Services (VLANs) for this node type |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;l3</samp>](## "node_type_keys.[].network_services.l3") | Boolean |  | False |  | Support L3 Network Services (VRFs, SVIs if `l2: true`) for this node type<br>Only supported with `underlay_router: true` |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "node_type_keys.[].type") | String | Required |  |  | Value of `type` key on devices of this Node Type |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;underlay_router</samp>](## "node_type_keys.[].underlay_router") | Boolean |  | True |  | Is this node type a L3 device |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;uplink_type</samp>](## "node_type_keys.[].uplink_type") | String |  | p2p | Valid Values:<br>- p2p<br>- port-channel | `uplink_type` must be `p2p`` if`vtep: true`or`underlay_router: true` |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vtep</samp>](## "node_type_keys.[].vtep") | Boolean |  | False |  | Is this node type a VXLAN VTEP |

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

## Point to Point Links MTU

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>p2p_uplinks_mtu</samp>](## "p2p_uplinks_mtu") | Integer |  | 9000 |  | Point to Point Links MTU |

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
| [<samp>p2p_uplinks_qos_profile</samp>](## "p2p_uplinks_qos_profile") | String |  |  |  | P2P Uplinks QoS Profile |

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
| [<samp>pod_name</samp>](## "pod_name") | String |  |  |  | POD Name |

### YAML

```yaml
pod_name: <str>
```

## Device Type

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>type</samp>](## "type") | String | Required |  | Valid Values:<br>- <value(s) of node_type_keys.type> | Device Type |

### YAML

```yaml
type: <str>
```

## Underlay ISIS Instance Name

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>underlay_isis_instance_name</samp>](## "underlay_isis_instance_name") | String |  | EVPN_UNDERLAY |  | Underlay ISIS Instance Name |

### YAML

```yaml
underlay_isis_instance_name: <str>
```

## Underlay OSPF Area

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>underlay_ospf_area</samp>](## "underlay_ospf_area") | String |  | 0.0.0.0 | Format: ipv4 | Underlay OSPF Area |

### YAML

```yaml
underlay_ospf_area: <str>
```

## Enable Underlay OSPF BFD

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>underlay_ospf_bfd_enable</samp>](## "underlay_ospf_bfd_enable") | Boolean |  | False |  | Enable Underlay OSPF BFD |

### YAML

```yaml
underlay_ospf_bfd_enable: <bool>
```

## Underlay OSPF Max LSA

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>underlay_ospf_max_lsa</samp>](## "underlay_ospf_max_lsa") | Integer |  | 12000 |  | Underlay OSPF Max LSA |

### YAML

```yaml
underlay_ospf_max_lsa: <int>
```

## Underlay OSPF Process ID

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>underlay_ospf_process_id</samp>](## "underlay_ospf_process_id") | Integer |  | 100 |  | Underlay OSPF Process ID |

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
| [<samp>underlay_rfc5549</samp>](## "underlay_rfc5549") | Boolean |  | False |  | Enable RFC5549 in Underlay |

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
| [<samp>uplink_ptp</samp>](## "uplink_ptp") | Dictionary |  |  |  | Uplink PTP |
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
| [<samp>vtep_vvtep_ip</samp>](## "vtep_vvtep_ip") | String |  |  | Format: ipv4_cidr | Virtual VTEP IP |

### YAML

```yaml
vtep_vvtep_ip: <str>
```
