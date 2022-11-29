!!! warning
    This document describes the data model for AVD 4.x. It may or may not work in previous versions.

## BFD Multihop

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

## BGP As

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

## BGP Ecmp

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

## BGP Peer Groups

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

## Connected Endpoints Keys

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>connected_endpoints_keys</samp>](## "connected_endpoints_keys") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;- key</samp>](## "connected_endpoints_keys.[].key") | String | Required, Unique |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "connected_endpoints_keys.[].type") | String |  |  |  |  |

### YAML

```yaml
connected_endpoints_keys:
  - key: <str>
    type: <str>
```

## Custom Structured Configuration List Merge

### Description

The List-merge strategy can be changed using `custom_structured_configuration_list_merge` variable using any value accepted by `list_merge` on the Ansible Combine filter.

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>custom_structured_configuration_list_merge</samp>](## "custom_structured_configuration_list_merge") | String |  | replace | Valid Values:<br>- replace<br>- append<br>- keep<br>- prepend<br>- append_rp<br>- prepend_rp |  |

### YAML

```yaml
custom_structured_configuration_list_merge: <str>
```

## Custom Structured Configuration Prefix

### Description

Custom EOS Structured Configuration keys can be set on any group or host_var level using the name
of the corresponding `eos_cli_config_gen` key prefixed with content of `custom_structured_configuration_prefix`.
The content of Custom Structured Configuration variables will be combined with the structured config generated by the eos_designs role.
By default Lists are replaced and Dictionaries are updated. The combine is done recursively, so it is possible to update a sub-key of a variable set by
`eos_designs` role already.

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>custom_structured_configuration_prefix</samp>](## "custom_structured_configuration_prefix") | List |  | ['custom_structured_configuration_'] |  |  |

### YAML

```yaml
custom_structured_configuration_prefix:
```

## CVP Ingestauth Key

### Description

CloudVision Ingest Authentication key is required for on-prem CVP
### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>cvp_ingestauth_key</samp>](## "cvp_ingestauth_key") | String |  |  |  |  |

### YAML

```yaml
cvp_ingestauth_key: <str>
```

## CVP Instance IP

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>cvp_instance_ip</samp>](## "cvp_instance_ip") | String |  |  |  |  |

### YAML

```yaml
cvp_instance_ip: <str>
```

## CVP Instance Ips

### Description

You can either provide a list of IPs to target on-premise CloudVision cluster or
use DNS name for your CloudVision as a Service instance. If you have both on-prem and
CVaaS defined, only on-prem is going to be configured.

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>cvp_instance_ips</samp>](## "cvp_instance_ips") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;- &lt;str&gt;</samp>](## "cvp_instance_ips.[].&lt;str&gt;") | String |  |  |  |  |

### YAML

```yaml
cvp_instance_ips:
  - <str>
```

## CVP Token File

### Description

cvp_token_file is path to token file on switch
### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>cvp_token_file</samp>](## "cvp_token_file") | String |  | /tmp/cv-onboarding-token |  |  |

### YAML

```yaml
cvp_token_file: <str>
```

## Default IGMP Snooping Enabled

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

## Design

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

## Event Handlers

### Description

Gives ability to monitor and react to Syslog messages provides a powerful and flexible tool that can be used to apply self-healing actions,
customize the system behavior, and implement workarounds to problems discovered in the field.

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>event_handlers</samp>](## "event_handlers") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;- action</samp>](## "event_handlers.[].action") | String |  |  |  | Command to run when handler is triggered |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;action_type</samp>](## "event_handlers.[].action_type") | String |  |  | Valid Values:<br>- bash<br>- increment |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;asynchronous</samp>](## "event_handlers.[].asynchronous") | Boolean |  | False |  | Set the action to be non-blocking. |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;delay</samp>](## "event_handlers.[].delay") | Integer |  |  |  | Event-handler delay in seconds |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "event_handlers.[].name") | String | Required, Unique |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;regex</samp>](## "event_handlers.[].regex") | String |  |  |  | Regular expression to use for searching log messages. Required for on-logging trigger |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;trigger</samp>](## "event_handlers.[].trigger") | String |  |  | Valid Values:<br>- on-logging | Configure event trigger condition. |

### YAML

```yaml
event_handlers:
  - action: <str>
    action_type: <str>
    asynchronous: <bool>
    delay: <int>
    name: <str>
    regex: <str>
    trigger: <str>
```

## Evpn Ebgp Gateway Multihop

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

## Evpn Ebgp Multihop

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

## Evpn Hostflap Detection

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

## Evpn Import Pruning

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

## Evpn Multicast

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

## Evpn Overlay BGP Rtc

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

## Evpn Prevent Readvertise To Server

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

## Evpn Short Esi Prefix

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

## Evpn VLAN Aware Bundles

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

## Inband Management Subnet

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

## Internal VLAN Order

### Description

Internal vlan allocation order and range
### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>internal_vlan_order</samp>](## "internal_vlan_order") | Dictionary | Required |  |  |  |
| [<samp>&nbsp;&nbsp;allocation</samp>](## "internal_vlan_order.allocation") | String |  | ascending | Valid Values:<br>- ascending<br>- descending |  |
| [<samp>&nbsp;&nbsp;range</samp>](## "internal_vlan_order.range") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;beginning</samp>](## "internal_vlan_order.range.beginning") | Integer |  | 1006 |  | VLAN ID |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ending</samp>](## "internal_vlan_order.range.ending") | Integer |  | 1199 |  | VLAN ID |

### YAML

```yaml
internal_vlan_order:
  allocation: <str>
  range:
    beginning: <int>
    ending: <int>
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

## ISIS Area ID

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

## ISIS TI LFA

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

## L3 Edge

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>l3_edge</samp>](## "l3_edge") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;p2p_links</samp>](## "l3_edge.p2p_links") | List, items: Dictionary | Required |  |  | Any setting supported under p2p_links can be set and inherited from profile |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- as</samp>](## "l3_edge.p2p_links.[].as") | List, items: String |  |  |  | AS Numbers for BGP, required with bgp peering |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "l3_edge.p2p_links.[].as.[].&lt;str&gt;") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bfd</samp>](## "l3_edge.p2p_links.[].bfd") | Boolean |  | False |  | Enable BFD (only considered for BGP) |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;id</samp>](## "l3_edge.p2p_links.[].id") | Integer | Required, Unique |  |  | Unique id per subnet_summary. Used to calculate ip addresses | Required with ip_pool |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_in_underlay_protocol</samp>](## "l3_edge.p2p_links.[].include_in_underlay_protocol") | Boolean |  | False |  | Add this interface to underlay routing protocol |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interfaces</samp>](## "l3_edge.p2p_links.[].interfaces") | List, items: String |  |  |  | Interfaces where this link should be configured | Required |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "l3_edge.p2p_links.[].interfaces.[].&lt;str&gt;") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip</samp>](## "l3_edge.p2p_links.[].ip") | List, items: String |  |  |  | Specific IP addresses used on this P2P link | Optional (Requires ip_pool or subnet or ip) |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "l3_edge.p2p_links.[].ip.[].&lt;str&gt;") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_pool</samp>](## "l3_edge.p2p_links.[].ip_pool") | String |  |  |  | IP Pool defined under p2p_links_ip_pools. A /31 will be taken from the pool per P2P link | Optional (Requires ip_pool or subnet or ip) |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;macsec_profile</samp>](## "l3_edge.p2p_links.[].macsec_profile") | String |  |  |  | MAC Security Profile |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mtu</samp>](## "l3_edge.p2p_links.[].mtu") | Integer |  |  |  | MTU for this P2P link |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "l3_edge.p2p_links.[].nodes") | List, items: String |  |  |  | Nodes where this link should be configured | Required |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "l3_edge.p2p_links.[].nodes.[].&lt;str&gt;") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;profile</samp>](## "l3_edge.p2p_links.[].profile") | String |  |  |  | Profile defined under p2p_profiles |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ptp_enable</samp>](## "l3_edge.p2p_links.[].ptp_enable") | Boolean |  | False |  | Enable PTP |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;qos_profile</samp>](## "l3_edge.p2p_links.[].qos_profile") | String |  |  |  | QOS Service Profile |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;speed</samp>](## "l3_edge.p2p_links.[].speed") | String |  |  | Valid Values:<br>- speed<br>- auto speed<br>- forced speed | Speed | Optional |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;subnet</samp>](## "l3_edge.p2p_links.[].subnet") | String |  |  |  | Subnet used on this P2P link | Optional (Requires ip_pool or subnet or ip) |
| [<samp>&nbsp;&nbsp;p2p_links_ip_pools</samp>](## "l3_edge.p2p_links_ip_pools") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- ipv4_pool</samp>](## "l3_edge.p2p_links_ip_pools.[].ipv4_pool") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "l3_edge.p2p_links_ip_pools.[].name") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;p2p_links_profiles</samp>](## "l3_edge.p2p_links_profiles") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "l3_edge.p2p_links_profiles.[].name") | String |  |  |  |  |

### YAML

```yaml
l3_edge:
  p2p_links:
    - as:
        - <str>
      bfd: <bool>
      id: <int>
      include_in_underlay_protocol: <bool>
      interfaces:
        - <str>
      ip:
        - <str>
      ip_pool: <str>
      macsec_profile: <str>
      mtu: <int>
      nodes:
        - <str>
      profile: <str>
      ptp_enable: <bool>
      qos_profile: <str>
      speed: <str>
      subnet: <str>
  p2p_links_ip_pools:
    - ipv4_pool: <str>
      name: <str>
  p2p_links_profiles:
    - name: <str>
```

## Local Users

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>local_users</samp>](## "local_users") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;- name</samp>](## "local_users.[].name") | String | Required, Unique |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;no_password</samp>](## "local_users.[].no_password") | Boolean |  |  |  | If set a password will not be configured for this user. "sha512_password" MUST not be defined for this user. |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;privilege</samp>](## "local_users.[].privilege") | Integer |  |  | Min: 1<br>Max: 15 | Initial privilege level with local EXEC authorization. |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;role</samp>](## "local_users.[].role") | String |  |  |  | EOS RBAC Role to be assigned to the user such as "network-admin" or "network-operator" |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;sha512_password</samp>](## "local_users.[].sha512_password") | String |  |  |  | Must be the hash of the password. By default EOS salts the password with the username, so the simplest is to generate the hash on an EOS device using the same username. |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ssh_key</samp>](## "local_users.[].ssh_key") | String |  |  |  |  |

### YAML

```yaml
local_users:
  - name: <str>
    no_password: <bool>
    privilege: <int>
    role: <str>
    sha512_password: <str>
    ssh_key: <str>
```

## MAC Address Table

### Description

MAC address-table aging time
Use to change the EOS default of 300.

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>mac_address_table</samp>](## "mac_address_table") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;aging_time</samp>](## "mac_address_table.aging_time") | Integer |  |  |  | Time in seconds |

### YAML

```yaml
mac_address_table:
  aging_time: <int>
```

## Management Eapi

### Description

Default is https management eAPI enabled
### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>management_eapi</samp>](## "management_eapi") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;default_services</samp>](## "management_eapi.default_services") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;enable_http</samp>](## "management_eapi.enable_http") | Boolean |  | False |  |  |
| [<samp>&nbsp;&nbsp;enable_https</samp>](## "management_eapi.enable_https") | Boolean |  | True |  |  |

### YAML

```yaml
management_eapi:
  default_services: <bool>
  enable_http: <bool>
  enable_https: <bool>
```

## Mgmt Destination Networks

### Description

OOB mgmt interface destination networks - override default route
### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>mgmt_destination_networks</samp>](## "mgmt_destination_networks") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;- &lt;str&gt;</samp>](## "mgmt_destination_networks.[].&lt;str&gt;") | String |  |  |  |  |

### YAML

```yaml
mgmt_destination_networks:
  - <str>
```

## Mgmt Gateway

### Description

Management interface configuration
### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>mgmt_gateway</samp>](## "mgmt_gateway") | String |  |  |  |  |

### YAML

```yaml
mgmt_gateway: <str>
```

## Mgmt Interface

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>mgmt_interface</samp>](## "mgmt_interface") | String |  | Management1 |  |  |

### YAML

```yaml
mgmt_interface: <str>
```

## Mgmt Interface VRF

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>mgmt_interface_vrf</samp>](## "mgmt_interface_vrf") | String |  | MGMT |  |  |

### YAML

```yaml
mgmt_interface_vrf: <str>
```

## Mgmt VRF Routing

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>mgmt_vrf_routing</samp>](## "mgmt_vrf_routing") | Boolean |  | False |  |  |

### YAML

```yaml
mgmt_vrf_routing: <bool>
```

## MLAG Ibgp Peering VRFs

### Description

On mlag leafs, an SVI interface is defined per vrf, to establish iBGP peering (required when mlag leafs in topology)
The SVI id will be derived from the base vlan defined: mlag_ibgp_peering_vrfs.base_vlan + (vrf_id or vrf_vni) - 1
Depending on the values of vrf_id / vrf_id it may be required to adjust the base_vlan to avoid overlaps or invalid vlan ids.
The SVI ip address derived from mlag_l3_peer_ipv4_pool is re-used across all iBGP peerings.

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>mlag_ibgp_peering_vrfs</samp>](## "mlag_ibgp_peering_vrfs") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;base_vlan</samp>](## "mlag_ibgp_peering_vrfs.base_vlan") | Integer |  | 3000 | Min: 1<br>Max: 4000 |  |

### YAML

```yaml
mlag_ibgp_peering_vrfs:
  base_vlan: <int>
```

## Name Server

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>name_server</samp>](## "name_server") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;nodes</samp>](## "name_server.nodes") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "name_server.nodes.[].&lt;str&gt;") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;source</samp>](## "name_server.source") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "name_server.source.vrf") | String |  |  |  |  |

### YAML

```yaml
name_server:
  nodes:
    - <str>
  source:
    vrf: <str>
```

## Name Servers

### Description

Only eos_designs name_servers variables
### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>name_servers</samp>](## "name_servers") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;- &lt;str&gt;</samp>](## "name_servers.[].&lt;str&gt;") | String |  |  |  |  |

### YAML

```yaml
name_servers:
  - <str>
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

## Only Local VLAN Trunk Groups

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

## Overlay Her Flood List Per Vni

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

## Overlay Her Flood List Scope

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

## Overlay MLAG Rfc5549

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

## Overlay Rd Type

### Description

Specify RD type
Route Distinguisher (RD) for L2 / L3 services is set to <overlay_loopback>:<vni> per default.
By configuring overlay_rd_type the Administrator subfield (first part of RD) can be set to other values.

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>overlay_rd_type</samp>](## "overlay_rd_type") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;admin_subfield</samp>](## "overlay_rd_type.admin_subfield") | String |  |  |  | < "vtep_loopback" or "bgp_as" or < IPv4 Address > or <0-65535> or <0-4294967295>, default -> <overlay_loopback_ip> > |

### YAML

```yaml
overlay_rd_type:
  admin_subfield: <str>
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

## Overlay Rt Type

### Description

Specify RT type
Route Target (RT) for L2 / L3 services is set to <vni>:<vni> per default
By configuring overlay_rt_type the Administrator subfield (first part of RT) can be set to other values.

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>overlay_rt_type</samp>](## "overlay_rt_type") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;admin_subfield</samp>](## "overlay_rt_type.admin_subfield") | String |  |  |  | < "bgp_as" or <0-65535> or <0-4294967295>, default -> <mac_vrf_id> > |

### YAML

```yaml
overlay_rt_type:
  admin_subfield: <str>
```

## P2P Uplinks MTU

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>p2p_uplinks_mtu</samp>](## "p2p_uplinks_mtu") | Integer |  | 9000 |  |  |

### YAML

```yaml
p2p_uplinks_mtu: <int>
```

## P2P Uplinks QOS Profile

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

## Platform Settings

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>platform_settings</samp>](## "platform_settings") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;- feature_support</samp>](## "platform_settings.[].feature_support") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interface_storm_control</samp>](## "platform_settings.[].feature_support.interface_storm_control") | Boolean |  | True |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;queue_monitor_length_notify</samp>](## "platform_settings.[].feature_support.queue_monitor_length_notify") | Boolean |  | True |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;lag_hardware_only</samp>](## "platform_settings.[].lag_hardware_only") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;management_interface</samp>](## "platform_settings.[].management_interface") | String |  | Management1 |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;platforms</samp>](## "platform_settings.[].platforms") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "platform_settings.[].platforms.[].&lt;str&gt;") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "platform_settings.[].raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the root level of the final EOS configuration |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;reload_delay</samp>](## "platform_settings.[].reload_delay") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag</samp>](## "platform_settings.[].reload_delay.mlag") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;non_mlag</samp>](## "platform_settings.[].reload_delay.non_mlag") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;tcam_profile</samp>](## "platform_settings.[].tcam_profile") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;trident_forwarding_table_partition</samp>](## "platform_settings.[].trident_forwarding_table_partition") | String |  |  |  | Only applied when evpn_multicast is true |

### YAML

```yaml
platform_settings:
  - feature_support:
      interface_storm_control: <bool>
      queue_monitor_length_notify: <bool>
    lag_hardware_only: <bool>
    management_interface: <str>
    platforms:
      - <str>
    raw_eos_cli: <str>
    reload_delay:
      mlag: <int>
      non_mlag: <int>
    tcam_profile: <str>
    trident_forwarding_table_partition: <str>
```

## Platform Speed Groups

### Description

Set Hardware Speed Groups per Platform
### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>platform_speed_groups</samp>](## "platform_speed_groups") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;- platform</samp>](## "platform_speed_groups.[].platform") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;speeds</samp>](## "platform_speed_groups.[].speeds") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- speed</samp>](## "platform_speed_groups.[].speeds.[].speed") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;speed_groups</samp>](## "platform_speed_groups.[].speeds.[].speed_groups") | List, items: Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;int&gt;</samp>](## "platform_speed_groups.[].speeds.[].speed_groups.[].&lt;int&gt;") | Integer |  |  |  |  |

### YAML

```yaml
platform_speed_groups:
  - platform: <str>
    speeds:
      - speed: <str>
        speed_groups:
          - <int>
```

## Pod Name

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

## Redundancy

### Description

Redundancy for chassis platforms with dual supervisors | Optional
### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>redundancy</samp>](## "redundancy") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;protocol</samp>](## "redundancy.protocol") | String |  |  | Valid Values:<br>- sso<br>- rpr |  |

### YAML

```yaml
redundancy:
  protocol: <str>
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

## Snmp Settings

### Description

Set SNMP settings
### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>snmp_settings</samp>](## "snmp_settings") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;contact</samp>](## "snmp_settings.contact") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;location</samp>](## "snmp_settings.location") | Boolean |  | False |  | Formatted as: {{ fabric_name }} {{ dc_name }} {{ pod_name }} {{ switch_rack }} {{ inventory_hostname }} |

### YAML

```yaml
snmp_settings:
  contact: <str>
  location: <bool>
```

## Svi Profiles

### Description

Optional profiles to apply on SVI interfaces
Each profile can support all or some of the following keys according to your own needs.
Keys are the same used under SVI.
Svi_profiles can refer to another svi_profiles to inherit settings in up to two levels (svi->profile->parent_profile).

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>svi_profiles</samp>](## "svi_profiles") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;- enabled</samp>](## "svi_profiles.[].enabled") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;igmp_snooping_enabled</samp>](## "svi_profiles.[].igmp_snooping_enabled") | Boolean |  | True |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_address_virtual</samp>](## "svi_profiles.[].ip_address_virtual") | String |  |  |  | IPv4_address/Mask |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_address_virtual_secondaries</samp>](## "svi_profiles.[].ip_address_virtual_secondaries") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "svi_profiles.[].ip_address_virtual_secondaries.[].&lt;str&gt;") | String |  |  |  | IPv4_address/Mask |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_helpers</samp>](## "svi_profiles.[].ip_helpers") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- ip_helper</samp>](## "svi_profiles.[].ip_helpers.[].ip_helper") | String |  |  |  | IPv4 DHCP server IP |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_interface</samp>](## "svi_profiles.[].ip_helpers.[].source_interface") | String |  |  |  | Interface name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_vrf</samp>](## "svi_profiles.[].ip_helpers.[].source_vrf") | String |  |  |  | VRF to originate DHCP relay packets to DHCP server |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_virtual_router_addresses</samp>](## "svi_profiles.[].ip_virtual_router_addresses") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "svi_profiles.[].ip_virtual_router_addresses.[].&lt;str&gt;") | String |  |  |  | IPv4_address/Mask or IPv4_address |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mtu</samp>](## "svi_profiles.[].mtu") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "svi_profiles.[].name") | String |  |  |  | VLAN name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "svi_profiles.[].nodes") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- ip_address</samp>](## "svi_profiles.[].nodes.[].ip_address") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_address_virtual_secondaries</samp>](## "svi_profiles.[].nodes.[].ip_address_virtual_secondaries") | List, items: String |  |  |  | Should take config from svis[svi].nodes[node] |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "svi_profiles.[].nodes.[].ip_address_virtual_secondaries.[].&lt;str&gt;") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_helpers</samp>](## "svi_profiles.[].nodes.[].ip_helpers") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- ip_helper</samp>](## "svi_profiles.[].nodes.[].ip_helpers.[].ip_helper") | String |  |  |  | IPv4 DHCP server IP |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_interface</samp>](## "svi_profiles.[].nodes.[].ip_helpers.[].source_interface") | String |  |  |  | Interface name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_vrf</samp>](## "svi_profiles.[].nodes.[].ip_helpers.[].source_vrf") | String |  |  |  | VRF to originate DHCP relay packets to DHCP server |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_virtual_router_addresses</samp>](## "svi_profiles.[].nodes.[].ip_virtual_router_addresses") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "svi_profiles.[].nodes.[].ip_virtual_router_addresses.[].&lt;str&gt;") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_address</samp>](## "svi_profiles.[].nodes.[].ipv6_address") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_virtual_router_addresses</samp>](## "svi_profiles.[].nodes.[].ipv6_virtual_router_addresses") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "svi_profiles.[].nodes.[].ipv6_virtual_router_addresses.[].&lt;str&gt;") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "svi_profiles.[].nodes.[].name") | String | Required, Unique |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;parent_profile</samp>](## "svi_profiles.[].parent_profile") | String |  |  |  | SVI profile name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;profile</samp>](## "svi_profiles.[].profile") | String | Required, Unique |  |  | Profile name |

### YAML

```yaml
svi_profiles:
  - enabled: <bool>
    igmp_snooping_enabled: <bool>
    ip_address_virtual: <str>
    ip_address_virtual_secondaries:
      - <str>
    ip_helpers:
      - ip_helper: <str>
        source_interface: <str>
        source_vrf: <str>
    ip_virtual_router_addresses:
      - <str>
    mtu: <int>
    name: <str>
    nodes:
      - ip_address: <str>
        ip_address_virtual_secondaries:
          - <str>
        ip_helpers:
          - ip_helper: <str>
            source_interface: <str>
            source_vrf: <str>
        ip_virtual_router_addresses:
          - <str>
        ipv6_address: <str>
        ipv6_virtual_router_addresses:
          - <str>
        name: <str>
    parent_profile: <str>
    profile: <str>
```

## TerminAttr Disable AAA

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>terminattr_disable_aaa</samp>](## "terminattr_disable_aaa") | Boolean |  | False |  |  |

### YAML

```yaml
terminattr_disable_aaa: <bool>
```

## TerminAttr Ingestexclude

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>terminattr_ingestexclude</samp>](## "terminattr_ingestexclude") | String |  | /Sysdb/cell/1/agent,/Sysdb/cell/2/agent |  |  |

### YAML

```yaml
terminattr_ingestexclude: <str>
```

## TerminAttr Ingestgrpcurl Port

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>terminattr_ingestgrpcurl_port</samp>](## "terminattr_ingestgrpcurl_port") | Integer |  | 9910 |  |  |

### YAML

```yaml
terminattr_ingestgrpcurl_port: <int>
```

## TerminAttr Smashexcludes

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>terminattr_smashexcludes</samp>](## "terminattr_smashexcludes") | String |  | ale,flexCounter,hardware,kni,pulse,strata |  |  |

### YAML

```yaml
terminattr_smashexcludes: <str>
```

## Timezone

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>timezone</samp>](## "timezone") | String |  |  |  |  |

### YAML

```yaml
timezone: <str>
```

## Trunk Groups

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

## Type

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>type</samp>](## "type") | String | Required |  | Valid Values:<br>- <value(s) of node_type_keys.type> |  |

### YAML

```yaml
type: <str>
```

## Underlay Filter Peer As

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

## Underlay IPv6

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

## Underlay OSPF BFD Enable

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

## Underlay Rfc5549

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

## Vtep Vvtep IP

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

## <Connected Endpoints Keys.Key>

### Description

This should be applied to group_vars or host_vars where endpoints are connecting.
<connected_endpoints_keys.key> is one of the keys under "connected_endpoints_keys"
Default keys are "servers", "firewalls", "routers", "load_balancers" and "storage_arrays".

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>&lt;connected_endpoints_keys.key&gt;</samp>](## "&lt;connected_endpoints_keys.key&gt;") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;- adapters</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters") | List, items: Dictionary |  |  |  | A list of adapter(s), group by adapters leveraging the same port-profile. |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- description</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].description") | String |  |  |  | Interface descriptions Description. |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dot1x</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].dot1x") | Dictionary |  |  |  | 802.1x |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;authentication_failure</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].dot1x.authentication_failure") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].dot1x.authentication_failure.action") | String |  |  | Valid Values:<br>- allow<br>- drop |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;allow_vlan</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].dot1x.authentication_failure.allow_vlan") | Integer |  |  | Min: 1<br>Max: 4094 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;host_mode</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].dot1x.host_mode") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].dot1x.host_mode.mode") | String |  |  | Valid Values:<br>- multi-host<br>- single-host |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;multi_host_authenticated</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].dot1x.host_mode.multi_host_authenticated") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mac_based_authentication</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].dot1x.mac_based_authentication") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;always</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].dot1x.mac_based_authentication.always") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].dot1x.mac_based_authentication.enabled") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;host_mode_common</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].dot1x.mac_based_authentication.host_mode_common") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pae</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].dot1x.pae") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].dot1x.pae.mode") | String |  |  | Valid Values:<br>- authenticator |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;port_control</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].dot1x.port_control") | String |  |  | Valid Values:<br>- auto<br>- force-authorized<br>- force-unauthorized |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;port_control_force_authorized_phone</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].dot1x.port_control_force_authorized_phone") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;reauthentication</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].dot1x.reauthentication") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;reauthorization_request_limit</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].dot1x.reauthorization_request_limit") | Integer |  |  | Min: 1<br>Max: 10 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;timeout</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].dot1x.timeout") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;idle_host</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].dot1x.timeout.idle_host") | Integer |  |  | Min: 10<br>Max: 65535 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;quiet_period</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].dot1x.timeout.quiet_period") | Integer |  |  | Min: 1<br>Max: 65535 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;reauth_period</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].dot1x.timeout.reauth_period") | String |  |  |  | Range 60-4294967295 or "server" |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;reauth_timeout_ignore</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].dot1x.timeout.reauth_timeout_ignore") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tx_period</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].dot1x.timeout.tx_period") | Integer |  |  | Min: 1<br>Max: 65535 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].enabled") | Boolean |  | True |  | Administrative state, setting to false will set port to 'shutdown' in intended configuration<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;endpoint_ports</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].endpoint_ports") | List, items: String |  |  |  | The lists "endpoint_ports", "switch_ports" and "switches" must have the same length.<br>Each list item is one switchport.<br>Endpoint port(s) is used for description, required unless description is set.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].endpoint_ports.[].&lt;str&gt;") | String |  |  |  | Interface name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ethernet_segment</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].ethernet_segment") | Dictionary |  |  |  | Settings for all- or single-active EVPN multihoming |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;designated_forwarder_algorithm</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].ethernet_segment.designated_forwarder_algorithm") | String |  |  | Valid Values:<br>- auto<br>- modulus<br>- preference | Configure DF algorithm and preferences<br>- auto: Use preference-based algorithm and assign preference based on position of device in the 'switches' list<br>   e.g. assuming a list of three switches, this would assign a preference of 200 to the first switch, 100 to the 2nd and 0 to the third<br>- preference: Set preference for each switch manually using designated_forwarder_preferences key<br>- modulus: Use the default modulus-based algorithm<br>If omitted, Port-Channels use the EOS default of modulus<br>If omitted, Ethernet interfaces default to the 'auto' mechanism detailed above<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;designated_forwarder_preferences</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].ethernet_segment.designated_forwarder_preferences") | List, items: String |  |  |  | Manual preference as described above, required only for preference algorithm |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].ethernet_segment.designated_forwarder_preferences.[].&lt;str&gt;") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dont_preempt</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].ethernet_segment.dont_preempt") | Boolean |  |  |  | Disable preemption for single-active forwarding when auto/manual DF preference is configured. |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;redundancy</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].ethernet_segment.redundancy") | String |  |  | Valid Values:<br>- all-active<br>- single-active | If omitted, Port-Channels use the EOS default of all-active<br>If omitted, Ethernet interfaces are configured as single-active<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;short_esi</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].ethernet_segment.short_esi") | String | Required |  |  | In format xxxx:xxxx:xxxx or "auto"<br>Define a manual short-esi (be careful using this on profiles) or auto-generate an ESI<br>Please see the notes under "EVPN A/A ESI dual- and single-attached endpoint scenarios" before setting short_esi: auto<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;flowcontrol</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].flowcontrol") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;received</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].flowcontrol.received") | String |  |  | Valid Values:<br>- received<br>- send<br>- on |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;l2_mtu</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].l2_mtu") | Integer |  |  |  | This should only be defined for platforms supporting the "l2 mtu" CLI |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;link_tracking</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].link_tracking") | Dictionary |  |  |  | Configure the downstream interfaces of a respective Link Tracking Group<br>If port_channel is defined in an adapter then port-channel interface is configured to be the downstream<br>else all the ethernet-interfaces will be configured as downstream -> to configure single-active EVPN multihomed networks<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].link_tracking.enabled") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].link_tracking.name") | String |  |  |  | Tracking group name<br>The default group name is taken from fabric variable of the switch, link_tracking.groups[0].name with default value being "LT_GROUP1".<br>Optional if default link_tracking settings are configured on the node.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].mode") | String |  |  | Valid Values:<br>- access<br>- dot1q-tunnel<br>- trunk | Interface mode |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;monitor_sessions</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].monitor_sessions") | List, items: Dictionary |  |  |  | Monitor Session configuration - Use defined switchports as source or destination for monitoring sessions |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].monitor_sessions.[].name") | String | Required |  |  | Session name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;role</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].monitor_sessions.[].role") | String |  |  | Valid Values:<br>- source<br>- destination |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;session_settings</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].monitor_sessions.[].session_settings") | Dictionary |  |  |  | Session settings are defined per session name. Different session_settings with for same session name will be combined/merged |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_group</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].monitor_sessions.[].session_settings.access_group") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].monitor_sessions.[].session_settings.access_group.name") | String |  |  |  | ACL Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].monitor_sessions.[].session_settings.access_group.type") | String |  |  | Valid Values:<br>- ip<br>- ipv6<br>- mac |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;encapsulation_gre_metadata_tx</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].monitor_sessions.[].session_settings.encapsulation_gre_metadata_tx") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;header_remove_size</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].monitor_sessions.[].session_settings.header_remove_size") | Integer |  |  |  | Number of bytes to remove from header |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rate_limit_per_egress_chip</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].monitor_sessions.[].session_settings.rate_limit_per_egress_chip") | String |  |  |  | Ratelimit and unit as string.<br>Examples:<br>  "100000 bps"<br>  "100 kbps"<br>  "10 mbps"<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rate_limit_per_ingress_chip</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].monitor_sessions.[].session_settings.rate_limit_per_ingress_chip") | String |  |  |  | Ratelimit and unit as string.<br>Examples:<br>  "100000 bps"<br>  "100 kbps"<br>  "10 mbps"<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sample</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].monitor_sessions.[].session_settings.sample") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;truncate</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].monitor_sessions.[].session_settings.truncate") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].monitor_sessions.[].session_settings.truncate.enabled") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;size</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].monitor_sessions.[].session_settings.truncate.size") | Integer |  |  |  | Size in bytes |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_settings</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].monitor_sessions.[].source_settings") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_group</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].monitor_sessions.[].source_settings.access_group") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].monitor_sessions.[].source_settings.access_group.name") | String |  |  |  | ACL Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].monitor_sessions.[].source_settings.access_group.priority") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].monitor_sessions.[].source_settings.access_group.type") | String |  |  | Valid Values:<br>- ip<br>- ipv6<br>- mac |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].monitor_sessions.[].source_settings.direction") | String |  |  | Valid Values:<br>- rx<br>- tx<br>- both |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mtu</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].mtu") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;native_vlan</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].native_vlan") | Integer |  |  |  | Native VLAN for a trunk port<br>If setting both native_vlan and native_vlan_tag, native_vlan_tag takes precedence<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;native_vlan_tag</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].native_vlan_tag") | Boolean |  | False |  | If setting both native_vlan and native_vlan_tag, native_vlan_tag takes precedence |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;port_channel</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].port_channel") | Dictionary |  |  |  | Used for port-channel adapter |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;channel_id</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].port_channel.channel_id") | Integer |  |  |  | Port-Channel ID, Optional<br>If no channel_id is specified, an id is generated from the first switch port in the port channel<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].port_channel.description") | String |  |  |  | Port-Channel Description - added after endpoint name in the description, Optional |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].port_channel.enabled") | Boolean |  | True |  | Port-Channel administrative state, Optional<br>setting to false will set port to 'shutdown' in intended configuration<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;esi</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].port_channel.esi") | String |  |  |  | Format xxxx:xxxx:xxxx |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;lacp_fallback</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].port_channel.lacp_fallback") | Dictionary |  |  |  | LACP Fallback configuration |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].port_channel.lacp_fallback.mode") | String |  |  | Valid Values:<br>- static | Currently only static mode is supported |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;timeout</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].port_channel.lacp_fallback.timeout") | Integer |  |  |  | Timeout in seconds, Optional - default is 90 seconds |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].port_channel.mode") | String | Required |  | Valid Values:<br>- active<br>- passive<br>- on | Port-Channel Mode |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;short_esi</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].port_channel.short_esi") | String |  |  |  | In format xxxx:xxxx:xxxx or "auto" |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;subinterfaces</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].port_channel.subinterfaces") | List, items: Dictionary |  |  |  | Port-Channel L2 Subinterfaces<br>Subinterfaces are only supported on routed port-channels, which means they cannot be configured on MLAG port-channels.<br>Setting short_esi: auto generates the short_esi automatically using a hash of configuration elements.<br>Please see the notes under "EVPN A/A ESI dual-attached endpoint scenario" before setting short_esi: auto.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- encapsulation_vlan</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].port_channel.subinterfaces.[].encapsulation_vlan") | Dictionary |  |  |  | Client vlan id encapsulation<br>Default is subinterface number<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;client_dot1q</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].port_channel.subinterfaces.[].encapsulation_vlan.client_dot1q") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;number</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].port_channel.subinterfaces.[].number") | Integer |  |  |  | Subinterface number |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;short_esi</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].port_channel.subinterfaces.[].short_esi") | String |  |  |  | In format xxxx:xxxx:xxxx or "auto"<br>Required for multihomed port-channels with subinterfaces<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vlan_id</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].port_channel.subinterfaces.[].vlan_id") | Integer |  |  |  | VLAN ID to bridge<br>Default is subinterface number<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;profile</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].profile") | String |  |  |  | Port-profile name, to inherit configuration. |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ptp</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].ptp") | Dictionary |  |  |  | PTP Enable |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enable</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].ptp.enable") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;qos_profile</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].qos_profile") | String |  |  |  | QOS profile name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the ethernet interface in the final EOS configuration |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;server_ports</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].server_ports") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].server_ports.[].&lt;str&gt;") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;short_esi</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].short_esi") | String |  |  | Valid Values:<br>- auto | Allocates an automatic short_esi to all ports using this profile<br>Please see the notes under "EVPN A/A ESI dual-attached endpoint examples" in this document before setting short_esi: auto.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_bpdufilter</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].spanning_tree_bpdufilter") | String |  |  | Valid Values:<br>- enabled<br>- disabled<br>- True<br>- False |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_bpduguard</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].spanning_tree_bpduguard") | String |  |  | Valid Values:<br>- enabled<br>- disabled<br>- True<br>- False |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_portfast</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].spanning_tree_portfast") | String |  |  | Valid Values:<br>- edge<br>- network |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;speed</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].speed") | String |  |  |  | < interface_speed or forced interface_speed or auto interface_speed ><br>Adapter speed - if not specified will be auto.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;storm_control</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].storm_control") | Dictionary |  |  |  | Storm control settings applied on port toward the endpoint |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;all</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].storm_control.all") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;level</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].storm_control.all.level") | Integer |  |  |  | Configure maximum storm-control level |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unit</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].storm_control.all.unit") | String |  | percent | Valid Values:<br>- percent<br>- pps | Optional var and is hardware dependent |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;broadcast</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].storm_control.broadcast") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;level</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].storm_control.broadcast.level") | Integer |  |  |  | Configure maximum storm-control level |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unit</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].storm_control.broadcast.unit") | String |  | percent | Valid Values:<br>- percent<br>- pps | Optional var and is hardware dependent |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;multicast</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].storm_control.multicast") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;level</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].storm_control.multicast.level") | Integer |  |  |  | Configure maximum storm-control level |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unit</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].storm_control.multicast.unit") | String |  | percent | Valid Values:<br>- percent<br>- pps | Optional var and is hardware dependent |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unknown_unicast</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].storm_control.unknown_unicast") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;level</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].storm_control.unknown_unicast.level") | Integer |  |  |  | Configure maximum storm-control level |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unit</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].storm_control.unknown_unicast.unit") | String |  | percent | Valid Values:<br>- percent<br>- pps | Optional var and is hardware dependentOptional var and is hardware dependent |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;switch_ports</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].switch_ports") | List, items: String | Required |  |  | List of switch interfac(es) |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].switch_ports.[].&lt;str&gt;") | String |  |  |  | Switchport interface |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;switches</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].switches") | List, items: String | Required |  |  | List of switch(es) |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].switches.[].&lt;str&gt;") | String |  |  |  | Device |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;trunk_groups</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].trunk_groups") | List, items: String |  |  |  | Required with "enable_trunk_groups: true"<br>Trunk Groups are used for limiting vlans on trunk ports to vlans with the same Trunk Group<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].trunk_groups.[].&lt;str&gt;") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vlans</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].vlans") | String |  |  |  | Interface vlans - if not set, the EOS default is that all vlans are allowed for trunk ports and vlan 1 will be used for access ports. |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].name") | String | Required, Unique |  |  | Endpoint name, this will be used in the switchport description. |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;rack</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].rack") | String |  |  |  | Rack is used for documentation purposes only |

### YAML

```yaml
<connected_endpoints_keys.key>:
  - adapters:
      - description: <str>
        dot1x:
          authentication_failure:
            action: <str>
            allow_vlan: <int>
          host_mode:
            mode: <str>
            multi_host_authenticated: <bool>
          mac_based_authentication:
            always: <bool>
            enabled: <bool>
            host_mode_common: <bool>
          pae:
            mode: <str>
          port_control: <str>
          port_control_force_authorized_phone: <bool>
          reauthentication: <bool>
          reauthorization_request_limit: <int>
          timeout:
            idle_host: <int>
            quiet_period: <int>
            reauth_period: <str>
            reauth_timeout_ignore: <bool>
            tx_period: <int>
        enabled: <bool>
        endpoint_ports:
          - <str>
        ethernet_segment:
          designated_forwarder_algorithm: <str>
          designated_forwarder_preferences:
            - <str>
          dont_preempt: <bool>
          redundancy: <str>
          short_esi: <str>
        flowcontrol:
          received: <str>
        l2_mtu: <int>
        link_tracking:
          enabled: <bool>
          name: <str>
        mode: <str>
        monitor_sessions:
          - name: <str>
            role: <str>
            session_settings:
              access_group:
                name: <str>
                type: <str>
              encapsulation_gre_metadata_tx: <bool>
              header_remove_size: <int>
              rate_limit_per_egress_chip: <str>
              rate_limit_per_ingress_chip: <str>
              sample: <int>
              truncate:
                enabled: <bool>
                size: <int>
            source_settings:
              access_group:
                name: <str>
                priority: <int>
                type: <str>
              direction: <str>
        mtu: <int>
        native_vlan: <int>
        native_vlan_tag: <bool>
        port_channel:
          channel_id: <int>
          description: <str>
          enabled: <bool>
          esi: <str>
          lacp_fallback:
            mode: <str>
            timeout: <int>
          mode: <str>
          short_esi: <str>
          subinterfaces:
            - encapsulation_vlan:
                client_dot1q: <int>
              number: <int>
              short_esi: <str>
              vlan_id: <int>
        profile: <str>
        ptp:
          enable: <bool>
        qos_profile: <str>
        raw_eos_cli: <str>
        server_ports:
          - <str>
        short_esi: <str>
        spanning_tree_bpdufilter: <str>
        spanning_tree_bpduguard: <str>
        spanning_tree_portfast: <str>
        speed: <str>
        storm_control:
          all:
            level: <int>
            unit: <str>
          broadcast:
            level: <int>
            unit: <str>
          multicast:
            level: <int>
            unit: <str>
          unknown_unicast:
            level: <int>
            unit: <str>
        switch_ports:
          - <str>
        switches:
          - <str>
        trunk_groups:
          - <str>
        vlans: <str>
    name: <str>
    rack: <str>
```
