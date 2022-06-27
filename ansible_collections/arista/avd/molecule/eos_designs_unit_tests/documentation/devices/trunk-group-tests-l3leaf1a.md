# trunk-group-tests-l3leaf1a
# Table of Contents

- [Management](#management)
  - [Management API HTTP](#management-api-http)
- [Authentication](#authentication)
- [Monitoring](#monitoring)
- [MLAG](#mlag)
  - [MLAG Summary](#mlag-summary)
  - [MLAG Device Configuration](#mlag-device-configuration)
- [Spanning Tree](#spanning-tree)
  - [Spanning Tree Summary](#spanning-tree-summary)
  - [Spanning Tree Device Configuration](#spanning-tree-device-configuration)
- [Internal VLAN Allocation Policy](#internal-vlan-allocation-policy)
  - [Internal VLAN Allocation Policy Summary](#internal-vlan-allocation-policy-summary)
  - [Internal VLAN Allocation Policy Configuration](#internal-vlan-allocation-policy-configuration)
- [VLANs](#vlans)
  - [VLANs Summary](#vlans-summary)
  - [VLANs Device Configuration](#vlans-device-configuration)
- [Interfaces](#interfaces)
  - [Ethernet Interfaces](#ethernet-interfaces)
  - [Port-Channel Interfaces](#port-channel-interfaces)
  - [Loopback Interfaces](#loopback-interfaces)
  - [VLAN Interfaces](#vlan-interfaces)
  - [VXLAN Interface](#vxlan-interface)
- [Routing](#routing)
  - [Service Routing Protocols Model](#service-routing-protocols-model)
  - [Virtual Router MAC Address](#virtual-router-mac-address)
  - [IP Routing](#ip-routing)
  - [IPv6 Routing](#ipv6-routing)
  - [Static Routes](#static-routes)
  - [Router BGP](#router-bgp)
- [BFD](#bfd)
  - [Router BFD](#router-bfd)
- [Multicast](#multicast)
  - [IP IGMP Snooping](#ip-igmp-snooping)
- [Filters](#filters)
  - [Prefix-lists](#prefix-lists)
  - [Route-maps](#route-maps)
- [ACL](#acl)
- [VRF Instances](#vrf-instances)
  - [VRF Instances Summary](#vrf-instances-summary)
  - [VRF Instances Device Configuration](#vrf-instances-device-configuration)
- [Quality Of Service](#quality-of-service)

# Management

## Management API HTTP

### Management API HTTP Summary

| HTTP | HTTPS | Default Services |
| ---- | ----- | ---------------- |
| False | True | - |

### Management API VRF Access

| VRF Name | IPv4 ACL | IPv6 ACL |
| -------- | -------- | -------- |
| MGMT | - | - |

### Management API HTTP Configuration

```eos
!
management api http-commands
   protocol https
   no shutdown
   !
   vrf MGMT
      no shutdown
```

# Authentication

# Monitoring

# MLAG

## MLAG Summary

| Domain-id | Local-interface | Peer-address | Peer-link |
| --------- | --------------- | ------------ | --------- |
| TRUNK_GROUP_TESTS_L3LEAF1 | Vlan4094 | 10.255.248.1 | Port-Channel3 |

Dual primary detection is disabled.

## MLAG Device Configuration

```eos
!
mlag configuration
   domain-id TRUNK_GROUP_TESTS_L3LEAF1
   local-interface Vlan4094
   peer-address 10.255.248.1
   peer-link Port-Channel3
   reload-delay mlag 300
   reload-delay non-mlag 330
```

# Spanning Tree

## Spanning Tree Summary

STP mode: **mstp**

### Global Spanning-Tree Settings

- Spanning Tree disabled for VLANs: **4093-4094**

## Spanning Tree Device Configuration

```eos
!
no spanning-tree vlan-id 4093-4094
```

# Internal VLAN Allocation Policy

## Internal VLAN Allocation Policy Summary

| Policy Allocation | Range Beginning | Range Ending |
| ------------------| --------------- | ------------ |
| ascending | 1006 | 1199 |

## Internal VLAN Allocation Policy Configuration

```eos
!
vlan internal order ascending range 1006 1199
```

# VLANs

## VLANs Summary

| VLAN ID | Name | Trunk Groups |
| ------- | ---- | ------------ |
| 100 | svi100_with_trunk_groups | TRUNK_GROUP_TESTS_L2LEAF1 TG_100 TG_NOT_MATCHING_ANY_SERVERS MLAG |
| 110 | l2vlan110_with_trunk_groups | TRUNK_GROUP_TESTS_L2LEAF1 TG_100 TG_NOT_MATCHING_ANY_SERVERS MLAG |
| 200 | svi200_with_trunk_groups | TRUNK_GROUP_TESTS_L2LEAF1 TG_200 TG_NOT_MATCHING_ANY_SERVERS MLAG |
| 210 | l2vlan210_with_trunk_groups | TRUNK_GROUP_TESTS_L2LEAF1 TG_200 TG_NOT_MATCHING_ANY_SERVERS MLAG |
| 300 | svi300_with_trunk_groups | TRUNK_GROUP_TESTS_L2LEAF1 TG_300 TG_NOT_MATCHING_ANY_SERVERS MLAG |
| 310 | l2vlan310_with_trunk_groups | TRUNK_GROUP_TESTS_L2LEAF1 TG_300 TG_NOT_MATCHING_ANY_SERVERS MLAG |
| 398 | svi398_without_trunk_groups | TRUNK_GROUP_TESTS_L2LEAF1 MLAG |
| 399 | l2vlan399_without_trunk_groups | TRUNK_GROUP_TESTS_L2LEAF1 MLAG |
| 3099 | MLAG_iBGP_TG_100 | LEAF_PEER_L3 |
| 3199 | MLAG_iBGP_TG_200 | LEAF_PEER_L3 |
| 3299 | MLAG_iBGP_TG_300 | LEAF_PEER_L3 |
| 4093 | LEAF_PEER_L3 | LEAF_PEER_L3 |
| 4094 | MLAG_PEER | MLAG |

## VLANs Device Configuration

```eos
!
vlan 100
   name svi100_with_trunk_groups
   trunk group MLAG
   trunk group TG_100
   trunk group TG_NOT_MATCHING_ANY_SERVERS
   trunk group TRUNK_GROUP_TESTS_L2LEAF1
!
vlan 110
   name l2vlan110_with_trunk_groups
   trunk group MLAG
   trunk group TG_100
   trunk group TG_NOT_MATCHING_ANY_SERVERS
   trunk group TRUNK_GROUP_TESTS_L2LEAF1
!
vlan 200
   name svi200_with_trunk_groups
   trunk group MLAG
   trunk group TG_200
   trunk group TG_NOT_MATCHING_ANY_SERVERS
   trunk group TRUNK_GROUP_TESTS_L2LEAF1
!
vlan 210
   name l2vlan210_with_trunk_groups
   trunk group MLAG
   trunk group TG_200
   trunk group TG_NOT_MATCHING_ANY_SERVERS
   trunk group TRUNK_GROUP_TESTS_L2LEAF1
!
vlan 300
   name svi300_with_trunk_groups
   trunk group MLAG
   trunk group TG_300
   trunk group TG_NOT_MATCHING_ANY_SERVERS
   trunk group TRUNK_GROUP_TESTS_L2LEAF1
!
vlan 310
   name l2vlan310_with_trunk_groups
   trunk group MLAG
   trunk group TG_300
   trunk group TG_NOT_MATCHING_ANY_SERVERS
   trunk group TRUNK_GROUP_TESTS_L2LEAF1
!
vlan 398
   name svi398_without_trunk_groups
   trunk group MLAG
   trunk group TRUNK_GROUP_TESTS_L2LEAF1
!
vlan 399
   name l2vlan399_without_trunk_groups
   trunk group MLAG
   trunk group TRUNK_GROUP_TESTS_L2LEAF1
!
vlan 3099
   name MLAG_iBGP_TG_100
   trunk group LEAF_PEER_L3
!
vlan 3199
   name MLAG_iBGP_TG_200
   trunk group LEAF_PEER_L3
!
vlan 3299
   name MLAG_iBGP_TG_300
   trunk group LEAF_PEER_L3
!
vlan 4093
   name LEAF_PEER_L3
   trunk group LEAF_PEER_L3
!
vlan 4094
   name MLAG_PEER
   trunk group MLAG
```

# Interfaces

## Ethernet Interfaces

### Ethernet Interfaces Summary

#### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | Channel-Group |
| --------- | ----------- | ---- | ----- | ----------- | ----------- | ------------- |
| Ethernet1 | TRUNK-GROUP-TESTS-L2LEAF1A_Ethernet1 | *trunk | *- | *- | *['TRUNK_GROUP_TESTS_L2LEAF1'] | 1 |
| Ethernet2 | TRUNK-GROUP-TESTS-L2LEAF1B_Ethernet1 | *trunk | *- | *- | *['TRUNK_GROUP_TESTS_L2LEAF1'] | 1 |
| Ethernet3 | MLAG_PEER_trunk-group-tests-l3leaf1b_Ethernet3 | *trunk | *2-4094 | *- | *['LEAF_PEER_L3', 'MLAG'] | 3 |
| Ethernet4 | MLAG_PEER_trunk-group-tests-l3leaf1b_Ethernet4 | *trunk | *2-4094 | *- | *['LEAF_PEER_L3', 'MLAG'] | 3 |
| Ethernet11 |  server_with_tg_100_Nic1 | trunk | - | - | ['TG_100', 'TG_NOT_MATCHING_ANY_VLANS'] | - |
| Ethernet13 | server_with_tg_300_Nic1 | *trunk | *- | *- | *['TG_300', 'TG_NOT_MATCHING_ANY_VLANS'] | 13 |

*Inherited from Port-Channel Interface

### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet1
   description TRUNK-GROUP-TESTS-L2LEAF1A_Ethernet1
   no shutdown
   channel-group 1 mode active
!
interface Ethernet2
   description TRUNK-GROUP-TESTS-L2LEAF1B_Ethernet1
   no shutdown
   channel-group 1 mode active
!
interface Ethernet3
   description MLAG_PEER_trunk-group-tests-l3leaf1b_Ethernet3
   no shutdown
   channel-group 3 mode active
!
interface Ethernet4
   description MLAG_PEER_trunk-group-tests-l3leaf1b_Ethernet4
   no shutdown
   channel-group 3 mode active
!
interface Ethernet11
   description server_with_tg_100_Nic1
   no shutdown
   switchport mode trunk
   switchport trunk group TG_100
   switchport trunk group TG_NOT_MATCHING_ANY_VLANS
   switchport
!
interface Ethernet13
   description server_with_tg_300_Nic1
   no shutdown
   channel-group 13 mode active
```

## Port-Channel Interfaces

### Port-Channel Interfaces Summary

#### L2

| Interface | Description | Type | Mode | VLANs | Native VLAN | Trunk Group | LACP Fallback Timeout | LACP Fallback Mode | MLAG ID | EVPN ESI |
| --------- | ----------- | ---- | ---- | ----- | ----------- | ------------| --------------------- | ------------------ | ------- | -------- |
| Port-Channel1 | TRUNK_GROUP_TESTS_L2LEAF1_Po1 | switched | trunk | - | - | ['TRUNK_GROUP_TESTS_L2LEAF1'] | - | - | 1 | - |
| Port-Channel3 | MLAG_PEER_trunk-group-tests-l3leaf1b_Po3 | switched | trunk | 2-4094 | - | ['LEAF_PEER_L3', 'MLAG'] | - | - | - | - |
| Port-Channel13 | server_with_tg_300_portchannel | switched | trunk | - | - | ['TG_300', 'TG_NOT_MATCHING_ANY_VLANS'] | - | - | 13 | - |

### Port-Channel Interfaces Device Configuration

```eos
!
interface Port-Channel1
   description TRUNK_GROUP_TESTS_L2LEAF1_Po1
   no shutdown
   switchport
   switchport mode trunk
   switchport trunk group TRUNK_GROUP_TESTS_L2LEAF1
   mlag 1
!
interface Port-Channel3
   description MLAG_PEER_trunk-group-tests-l3leaf1b_Po3
   no shutdown
   switchport
   switchport trunk allowed vlan 2-4094
   switchport mode trunk
   switchport trunk group LEAF_PEER_L3
   switchport trunk group MLAG
!
interface Port-Channel13
   description server_with_tg_300_portchannel
   no shutdown
   switchport
   switchport mode trunk
   switchport trunk group TG_300
   switchport trunk group TG_NOT_MATCHING_ANY_VLANS
   mlag 13
```

## Loopback Interfaces

### Loopback Interfaces Summary

#### IPv4

| Interface | Description | VRF | IP Address |
| --------- | ----------- | --- | ---------- |
| Loopback0 | EVPN_Overlay_Peering | default | 192.168.250.9/32 |
| Loopback1 | VTEP_VXLAN_Tunnel_Source | default | 192.168.249.9/32 |

#### IPv6

| Interface | Description | VRF | IPv6 Address |
| --------- | ----------- | --- | ------------ |
| Loopback0 | EVPN_Overlay_Peering | default | - |
| Loopback1 | VTEP_VXLAN_Tunnel_Source | default | - |


### Loopback Interfaces Device Configuration

```eos
!
interface Loopback0
   description EVPN_Overlay_Peering
   no shutdown
   ip address 192.168.250.9/32
!
interface Loopback1
   description VTEP_VXLAN_Tunnel_Source
   no shutdown
   ip address 192.168.249.9/32
```

## VLAN Interfaces

### VLAN Interfaces Summary

| Interface | Description | VRF |  MTU | Shutdown |
| --------- | ----------- | --- | ---- | -------- |
| Vlan100 | svi100_with_trunk_groups | TG_100 | - | false |
| Vlan200 | svi200_with_trunk_groups | TG_200 | - | false |
| Vlan300 | svi300_with_trunk_groups | TG_300 | - | false |
| Vlan398 | svi398_without_trunk_groups | TG_300 | - | false |
| Vlan3099 | MLAG_PEER_L3_iBGP: vrf TG_100 | TG_100 | 9000 | false |
| Vlan3199 | MLAG_PEER_L3_iBGP: vrf TG_200 | TG_200 | 9000 | false |
| Vlan3299 | MLAG_PEER_L3_iBGP: vrf TG_300 | TG_300 | 9000 | false |
| Vlan4093 | MLAG_PEER_L3_PEERING | default | 9000 | false |
| Vlan4094 | MLAG_PEER | default | 9000 | false |

#### IPv4

| Interface | VRF | IP Address | IP Address Virtual | IP Router Virtual Address | VRRP | ACL In | ACL Out |
| --------- | --- | ---------- | ------------------ | ------------------------- | ---- | ------ | ------- |
| Vlan100 |  TG_100  |  -  |  10.1.0.1/24  |  -  |  -  |  -  |  -  |
| Vlan200 |  TG_200  |  -  |  10.2.0.1/24  |  -  |  -  |  -  |  -  |
| Vlan300 |  TG_300  |  -  |  10.3.0.1/24  |  -  |  -  |  -  |  -  |
| Vlan398 |  TG_300  |  -  |  10.3.1.1/24  |  -  |  -  |  -  |  -  |
| Vlan3099 |  TG_100  |  10.255.247.0/31  |  -  |  -  |  -  |  -  |  -  |
| Vlan3199 |  TG_200  |  10.255.247.0/31  |  -  |  -  |  -  |  -  |  -  |
| Vlan3299 |  TG_300  |  10.255.247.0/31  |  -  |  -  |  -  |  -  |  -  |
| Vlan4093 |  default  |  10.255.247.0/31  |  -  |  -  |  -  |  -  |  -  |
| Vlan4094 |  default  |  10.255.248.0/31  |  -  |  -  |  -  |  -  |  -  |

### VLAN Interfaces Device Configuration

```eos
!
interface Vlan100
   description svi100_with_trunk_groups
   no shutdown
   vrf TG_100
   ip address virtual 10.1.0.1/24
!
interface Vlan200
   description svi200_with_trunk_groups
   no shutdown
   vrf TG_200
   ip address virtual 10.2.0.1/24
!
interface Vlan300
   description svi300_with_trunk_groups
   no shutdown
   vrf TG_300
   ip address virtual 10.3.0.1/24
!
interface Vlan398
   description svi398_without_trunk_groups
   no shutdown
   vrf TG_300
   ip address virtual 10.3.1.1/24
!
interface Vlan3099
   description MLAG_PEER_L3_iBGP: vrf TG_100
   no shutdown
   mtu 9000
   vrf TG_100
   ip address 10.255.247.0/31
!
interface Vlan3199
   description MLAG_PEER_L3_iBGP: vrf TG_200
   no shutdown
   mtu 9000
   vrf TG_200
   ip address 10.255.247.0/31
!
interface Vlan3299
   description MLAG_PEER_L3_iBGP: vrf TG_300
   no shutdown
   mtu 9000
   vrf TG_300
   ip address 10.255.247.0/31
!
interface Vlan4093
   description MLAG_PEER_L3_PEERING
   no shutdown
   mtu 9000
   ip address 10.255.247.0/31
!
interface Vlan4094
   description MLAG_PEER
   no shutdown
   mtu 9000
   no autostate
   ip address 10.255.248.0/31
```

## VXLAN Interface

### VXLAN Interface Summary

| Setting | Value |
| ------- | ----- |
| Source Interface | Loopback1 |
| UDP port | 4789 |
| EVPN MLAG Shared Router MAC | mlag-system-id |

#### VLAN to VNI, Flood List and Multicast Group Mappings

| VLAN | VNI | Flood List | Multicast Group |
| ---- | --- | ---------- | --------------- |
| 100 | 10100 | - | - |
| 110 | 10110 | - | - |
| 200 | 10200 | - | - |
| 210 | 10210 | - | - |
| 300 | 10300 | - | - |
| 310 | 10310 | - | - |
| 398 | 10398 | - | - |
| 399 | 10399 | - | - |

#### VRF to VNI and Multicast Group Mappings

| VRF | VNI | Multicast Group |
| ---- | --- | --------------- |
| TG_100 | 100 | - |
| TG_200 | 200 | - |
| TG_300 | 300 | - |

### VXLAN Interface Device Configuration

```eos
!
interface Vxlan1
   description trunk-group-tests-l3leaf1a_VTEP
   vxlan source-interface Loopback1
   vxlan virtual-router encapsulation mac-address mlag-system-id
   vxlan udp-port 4789
   vxlan vlan 100 vni 10100
   vxlan vlan 110 vni 10110
   vxlan vlan 200 vni 10200
   vxlan vlan 210 vni 10210
   vxlan vlan 300 vni 10300
   vxlan vlan 310 vni 10310
   vxlan vlan 398 vni 10398
   vxlan vlan 399 vni 10399
   vxlan vrf TG_100 vni 100
   vxlan vrf TG_200 vni 200
   vxlan vrf TG_300 vni 300
```

# Routing
## Service Routing Protocols Model

Multi agent routing protocol model enabled

```eos
!
service routing protocols model multi-agent
```

## Virtual Router MAC Address

### Virtual Router MAC Address Summary

#### Virtual Router MAC Address: 00:dc:00:00:00:0a

### Virtual Router MAC Address Configuration

```eos
!
ip virtual-router mac-address 00:dc:00:00:00:0a
```

## IP Routing

### IP Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | true |
| MGMT | false |
| TG_100 | true |
| TG_200 | true |
| TG_300 | true |

### IP Routing Device Configuration

```eos
!
ip routing
no ip routing vrf MGMT
ip routing vrf TG_100
ip routing vrf TG_200
ip routing vrf TG_300
```
## IPv6 Routing

### IPv6 Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | false |
| MGMT | false |
| TG_100 | false |
| TG_200 | false |
| TG_300 | false |

## Static Routes

### Static Routes Summary

| VRF | Destination Prefix | Next Hop IP             | Exit interface      | Administrative Distance       | Tag               | Route Name                    | Metric         |
| --- | ------------------ | ----------------------- | ------------------- | ----------------------------- | ----------------- | ----------------------------- | -------------- |
| MGMT | 0.0.0.0/0 | 1.1.1.1 | - | 1 | - | - | - |

### Static Routes Device Configuration

```eos
!
ip route vrf MGMT 0.0.0.0/0 1.1.1.1
```

## Router BGP

### Router BGP Summary

| BGP AS | Router ID |
| ------ | --------- |
| 65001|  192.168.250.9 |

| BGP Tuning |
| ---------- |
| maximum-paths 4 ecmp 4 |

### Router BGP Peer Groups

#### EVPN-OVERLAY-PEERS

| Settings | Value |
| -------- | ----- |
| Address Family | evpn |
| Source | Loopback0 |
| BFD | True |
| Ebgp multihop | 3 |
| Send community | all |
| Maximum routes | 0 (no limit) |

#### IPv4-UNDERLAY-PEERS

| Settings | Value |
| -------- | ----- |
| Address Family | ipv4 |
| Send community | all |
| Maximum routes | 12000 |

#### MLAG-IPv4-UNDERLAY-PEER

| Settings | Value |
| -------- | ----- |
| Address Family | ipv4 |
| Remote AS | 65001 |
| Next-hop self | True |
| Send community | all |
| Maximum routes | 12000 |

### BGP Neighbors

| Neighbor | Remote AS | VRF | Shutdown | Send-community | Maximum-routes | Allowas-in | BFD | RIB Pre-Policy Retain |
| -------- | --------- | --- | -------- | -------------- | -------------- | ---------- | --- | --------------------- |
| 10.255.247.1 | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | default | - | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | - | - | - |
| 10.255.247.1 | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | TG_100 | - | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | - | - | - |
| 10.255.247.1 | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | TG_200 | - | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | - | - | - |
| 10.255.247.1 | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | TG_300 | - | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | - | - | - |

### Router BGP EVPN Address Family

#### EVPN Peer Groups

| Peer Group | Activate |
| ---------- | -------- |
| EVPN-OVERLAY-PEERS | True |

### Router BGP VLANs

| VLAN | Route-Distinguisher | Both Route-Target | Import Route Target | Export Route-Target | Redistribute |
| ---- | ------------------- | ----------------- | ------------------- | ------------------- | ------------ |
| 100 | 192.168.250.9:10100 | 10100:10100 | - | - | learned |
| 110 | 192.168.250.9:10110 | 10110:10110 | - | - | learned |
| 200 | 192.168.250.9:10200 | 10200:10200 | - | - | learned |
| 210 | 192.168.250.9:10210 | 10210:10210 | - | - | learned |
| 300 | 192.168.250.9:10300 | 10300:10300 | - | - | learned |
| 310 | 192.168.250.9:10310 | 10310:10310 | - | - | learned |
| 398 | 192.168.250.9:10398 | 10398:10398 | - | - | learned |
| 399 | 192.168.250.9:10399 | 10399:10399 | - | - | learned |

### Router BGP VRFs

| VRF | Route-Distinguisher | Redistribute |
| --- | ------------------- | ------------ |
| TG_100 | 192.168.250.9:100 | connected |
| TG_200 | 192.168.250.9:200 | connected |
| TG_300 | 192.168.250.9:300 | connected |

### Router BGP Device Configuration

```eos
!
router bgp 65001
   router-id 192.168.250.9
   maximum-paths 4 ecmp 4
   neighbor EVPN-OVERLAY-PEERS peer group
   neighbor EVPN-OVERLAY-PEERS update-source Loopback0
   neighbor EVPN-OVERLAY-PEERS bfd
   neighbor EVPN-OVERLAY-PEERS ebgp-multihop 3
   neighbor EVPN-OVERLAY-PEERS send-community
   neighbor EVPN-OVERLAY-PEERS maximum-routes 0
   neighbor IPv4-UNDERLAY-PEERS peer group
   neighbor IPv4-UNDERLAY-PEERS send-community
   neighbor IPv4-UNDERLAY-PEERS maximum-routes 12000
   neighbor MLAG-IPv4-UNDERLAY-PEER peer group
   neighbor MLAG-IPv4-UNDERLAY-PEER remote-as 65001
   neighbor MLAG-IPv4-UNDERLAY-PEER next-hop-self
   neighbor MLAG-IPv4-UNDERLAY-PEER description trunk-group-tests-l3leaf1b
   neighbor MLAG-IPv4-UNDERLAY-PEER send-community
   neighbor MLAG-IPv4-UNDERLAY-PEER maximum-routes 12000
   neighbor MLAG-IPv4-UNDERLAY-PEER route-map RM-MLAG-PEER-IN in
   neighbor 10.255.247.1 peer group MLAG-IPv4-UNDERLAY-PEER
   neighbor 10.255.247.1 description trunk-group-tests-l3leaf1b
   redistribute connected route-map RM-CONN-2-BGP
   !
   vlan 100
      rd 192.168.250.9:10100
      route-target both 10100:10100
      redistribute learned
   !
   vlan 110
      rd 192.168.250.9:10110
      route-target both 10110:10110
      redistribute learned
   !
   vlan 200
      rd 192.168.250.9:10200
      route-target both 10200:10200
      redistribute learned
   !
   vlan 210
      rd 192.168.250.9:10210
      route-target both 10210:10210
      redistribute learned
   !
   vlan 300
      rd 192.168.250.9:10300
      route-target both 10300:10300
      redistribute learned
   !
   vlan 310
      rd 192.168.250.9:10310
      route-target both 10310:10310
      redistribute learned
   !
   vlan 398
      rd 192.168.250.9:10398
      route-target both 10398:10398
      redistribute learned
   !
   vlan 399
      rd 192.168.250.9:10399
      route-target both 10399:10399
      redistribute learned
   !
   address-family evpn
      neighbor EVPN-OVERLAY-PEERS activate
   !
   address-family ipv4
      no neighbor EVPN-OVERLAY-PEERS activate
      neighbor IPv4-UNDERLAY-PEERS activate
      neighbor MLAG-IPv4-UNDERLAY-PEER activate
   !
   vrf TG_100
      rd 192.168.250.9:100
      route-target import evpn 100:100
      route-target export evpn 100:100
      router-id 192.168.250.9
      neighbor 10.255.247.1 peer group MLAG-IPv4-UNDERLAY-PEER
      redistribute connected
   !
   vrf TG_200
      rd 192.168.250.9:200
      route-target import evpn 200:200
      route-target export evpn 200:200
      router-id 192.168.250.9
      neighbor 10.255.247.1 peer group MLAG-IPv4-UNDERLAY-PEER
      redistribute connected
   !
   vrf TG_300
      rd 192.168.250.9:300
      route-target import evpn 300:300
      route-target export evpn 300:300
      router-id 192.168.250.9
      neighbor 10.255.247.1 peer group MLAG-IPv4-UNDERLAY-PEER
      redistribute connected
```

# BFD

## Router BFD

### Router BFD Multihop Summary

| Interval | Minimum RX | Multiplier |
| -------- | ---------- | ---------- |
| 300 | 300 | 3 |

### Router BFD Device Configuration

```eos
!
router bfd
   multihop interval 300 min-rx 300 multiplier 3
```

# Multicast

## IP IGMP Snooping

### IP IGMP Snooping Summary

| IGMP Snooping | Fast Leave | Interface Restart Query | Proxy | Restart Query Interval | Robustness Variable |
| ------------- | ---------- | ----------------------- | ----- | ---------------------- | ------------------- |
| Enabled | - | - | - | - | - |

### IP IGMP Snooping Device Configuration

```eos
```

# Filters

## Prefix-lists

### Prefix-lists Summary

#### PL-LOOPBACKS-EVPN-OVERLAY

| Sequence | Action |
| -------- | ------ |
| 10 | permit 192.168.250.0/24 eq 32 |
| 20 | permit 192.168.249.0/24 eq 32 |

### Prefix-lists Device Configuration

```eos
!
ip prefix-list PL-LOOPBACKS-EVPN-OVERLAY
   seq 10 permit 192.168.250.0/24 eq 32
   seq 20 permit 192.168.249.0/24 eq 32
```

## Route-maps

### Route-maps Summary

#### RM-CONN-2-BGP

| Sequence | Type | Match and/or Set |
| -------- | ---- | ---------------- |
| 10 | permit | match ip address prefix-list PL-LOOPBACKS-EVPN-OVERLAY |

#### RM-MLAG-PEER-IN

| Sequence | Type | Match and/or Set |
| -------- | ---- | ---------------- |
| 10 | permit | set origin incomplete |

### Route-maps Device Configuration

```eos
!
route-map RM-CONN-2-BGP permit 10
   match ip address prefix-list PL-LOOPBACKS-EVPN-OVERLAY
!
route-map RM-MLAG-PEER-IN permit 10
   description Make routes learned over MLAG Peer-link less preferred on spines to ensure optimal routing
   set origin incomplete
```

# ACL

# VRF Instances

## VRF Instances Summary

| VRF Name | IP Routing |
| -------- | ---------- |
| MGMT | disabled |
| TG_100 | enabled |
| TG_200 | enabled |
| TG_300 | enabled |

## VRF Instances Device Configuration

```eos
!
vrf instance MGMT
!
vrf instance TG_100
!
vrf instance TG_200
!
vrf instance TG_300
```

# Quality Of Service
