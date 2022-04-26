# DC1-POD1-LEAF1A
# Table of Contents

- [Management](#management)
  - [Management API HTTP](#management-api-http)
- [Authentication](#authentication)
  - [Local Users](#local-users)
- [Monitoring](#monitoring)
  - [SNMP](#snmp)
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
- [EOS CLI](#eos-cli)

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

## Local Users

### Local Users Summary

| User | Privilege | Role |
| ---- | --------- | ---- |
| admin | 15 | network-admin |

### Local Users Device Configuration

```eos
!
username admin privilege 15 role network-admin secret sha512 $6$eJ5TvI8oru5i9e8G$R1X/SbtGTk9xoEHEBQASc7SC2nHYmi.crVgp2pXuCXwxsXEA81e4E0cXgQ6kX08fIeQzauqhv2kS.RGJFCon5/
```

# Monitoring

## SNMP

### SNMP Configuration Summary

| Contact | Location | SNMP Traps | State |
| ------- | -------- | ---------- | ----- |
| - | TWODC_5STAGE_CLOS DC1 DC1_POD1 DC1-POD1-LEAF1A | All | Disabled |

### SNMP Device Configuration

```eos
!
snmp-server location TWODC_5STAGE_CLOS DC1 DC1_POD1 DC1-POD1-LEAF1A
```

# Spanning Tree

## Spanning Tree Summary

STP mode: **none**

## Spanning Tree Device Configuration

```eos
!
spanning-tree mode none
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
| 4085 | L2LEAF_INBAND_MGMT | - |

## VLANs Device Configuration

```eos
!
vlan 4085
   name L2LEAF_INBAND_MGMT
```

# Interfaces

## Ethernet Interfaces

### Ethernet Interfaces Summary

#### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | Channel-Group |
| --------- | ----------- | ---- | ----- | ----------- | ----------- | ------------- |
| Ethernet3 | DC1-POD1-L2LEAF1A_Ethernet1 | *trunk | *4085 | *- | *- | 3 |

*Inherited from Port-Channel Interface

#### IPv4

| Interface | Description | Type | Channel Group | IP Address | VRF |  MTU | Shutdown | ACL In | ACL Out |
| --------- | ----------- | -----| ------------- | ---------- | ----| ---- | -------- | ------ | ------- |
| Ethernet1 | P2P_LINK_TO_DC1-POD1-SPINE1_Ethernet3 | routed | - | 172.17.110.1/31 | default | 1500 | false | - | - |
| Ethernet2 | P2P_LINK_TO_DC1-POD1-SPINE2_Ethernet3 | routed | - | 172.17.110.3/31 | default | 1500 | false | - | - |
| Ethernet4 | P2P_LINK_TO_DC1-RS1_Ethernet3 | routed | - | 172.17.10.4/31 | default | 1500 | false | - | - |

### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet1
   description P2P_LINK_TO_DC1-POD1-SPINE1_Ethernet3
   no shutdown
   mtu 1500
   no switchport
   ip address 172.17.110.1/31
   ptp enable
   service-profile QOS-PROFILE
!
interface Ethernet2
   description P2P_LINK_TO_DC1-POD1-SPINE2_Ethernet3
   no shutdown
   mtu 1500
   no switchport
   ip address 172.17.110.3/31
   ptp enable
   service-profile QOS-PROFILE
!
interface Ethernet3
   description DC1-POD1-L2LEAF1A_Ethernet1
   no shutdown
   channel-group 3 mode active
!
interface Ethernet4
   description P2P_LINK_TO_DC1-RS1_Ethernet3
   no shutdown
   mtu 1500
   no switchport
   ip address 172.17.10.4/31
   service-profile QOS-PROFILE
```

## Port-Channel Interfaces

### Port-Channel Interfaces Summary

#### L2

| Interface | Description | Type | Mode | VLANs | Native VLAN | Trunk Group | LACP Fallback Timeout | LACP Fallback Mode | MLAG ID | EVPN ESI |
| --------- | ----------- | ---- | ---- | ----- | ----------- | ------------| --------------------- | ------------------ | ------- | -------- |
| Port-Channel3 | DC1-POD1-L2LEAF1A_Po1 | switched | trunk | 4085 | - | - | - | - | - | - |

### Port-Channel Interfaces Device Configuration

```eos
!
interface Port-Channel3
   description DC1-POD1-L2LEAF1A_Po1
   no shutdown
   switchport
   switchport trunk allowed vlan 4085
   switchport mode trunk
   service-profile QOS-PROFILE
```

## Loopback Interfaces

### Loopback Interfaces Summary

#### IPv4

| Interface | Description | VRF | IP Address |
| --------- | ----------- | --- | ---------- |
| Loopback0 | EVPN_Overlay_Peering | default | 172.16.110.3/32 |
| Loopback1 | VTEP_VXLAN_Tunnel_Source | default | 172.18.110.3/32 |

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
   ip address 172.16.110.3/32
!
interface Loopback1
   description VTEP_VXLAN_Tunnel_Source
   no shutdown
   ip address 172.18.110.3/32
```

## VLAN Interfaces

### VLAN Interfaces Summary

| Interface | Description | VRF |  MTU | Shutdown |
| --------- | ----------- | --- | ---- | -------- |
| Vlan4085 | L2LEAF_INBAND_MGMT | default | 1500 | false |

#### IPv4

| Interface | VRF | IP Address | IP Address Virtual | IP Router Virtual Address | VRRP | ACL In | ACL Out |
| --------- | --- | ---------- | ------------------ | ------------------------- | ---- | ------ | ------- |
| Vlan4085 |  default  |  172.21.110.2/24  |  -  |  172.21.110.1  |  -  |  -  |  -  |

### VLAN Interfaces Device Configuration

```eos
!
interface Vlan4085
   description L2LEAF_INBAND_MGMT
   no shutdown
   mtu 1500
   ip address 172.21.110.2/24
   ip attached-host route export 19
   ip virtual-router address 172.21.110.1
```

## VXLAN Interface

### VXLAN Interface Summary

| Setting | Value |
| ------- | ----- |
| Source Interface | Loopback1 |
| UDP port | 4789 |

### VXLAN Interface Device Configuration

```eos
!
interface Vxlan1
   description DC1-POD1-LEAF1A_VTEP
   vxlan source-interface Loopback1
   vxlan udp-port 4789
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

#### Virtual Router MAC Address: 00:1c:73:00:dc:01

### Virtual Router MAC Address Configuration

```eos
!
ip virtual-router mac-address 00:1c:73:00:dc:01
```

## IP Routing

### IP Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | true |
| MGMT | false |

### IP Routing Device Configuration

```eos
!
ip routing
no ip routing vrf MGMT
```
## IPv6 Routing

### IPv6 Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | false |
| MGMT | false |

## Static Routes

### Static Routes Summary

| VRF | Destination Prefix | Next Hop IP             | Exit interface      | Administrative Distance       | Tag               | Route Name                    | Metric         |
| --- | ------------------ | ----------------------- | ------------------- | ----------------------------- | ----------------- | ----------------------------- | -------------- |
| MGMT | 0.0.0.0/0 | 192.168.1.254 | - | 1 | - | - | - |

### Static Routes Device Configuration

```eos
!
ip route vrf MGMT 0.0.0.0/0 192.168.1.254
```

## Router BGP

### Router BGP Summary

| BGP AS | Router ID |
| ------ | --------- |
| 65111|  172.16.110.3 |

| BGP Tuning |
| ---------- |
| no bgp default ipv4-unicast |
| distance bgp 20 200 200 |
| graceful-restart restart-time 300 |
| graceful-restart |
| maximum-paths 4 ecmp 4 |

### Router BGP Peer Groups

#### EVPN-OVERLAY-PEERS

| Settings | Value |
| -------- | ----- |
| Address Family | evpn |
| Remote AS | 65110 |
| Next-hop unchanged | True |
| Source | Loopback0 |
| BFD | True |
| Ebgp multihop | 5 |
| Send community | all |
| Maximum routes | 0 (no limit) |

#### IPv4-UNDERLAY-PEERS

| Settings | Value |
| -------- | ----- |
| Address Family | ipv4 |
| Remote AS | 65110 |
| Send community | all |
| Maximum routes | 12000 |

### BGP Neighbors

| Neighbor | Remote AS | VRF | Shutdown | Send-community | Maximum-routes | Allowas-in | BFD | RIB Pre-Policy Retain |
| -------- | --------- | --- | -------- | -------------- | -------------- | ---------- | --- | --------------------- |
| 172.16.20.1 | 65201 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - |
| 172.16.110.4 | 65112 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - |
| 172.16.110.5 | 65112 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - |
| 172.16.200.1 | 65200 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - |
| 172.16.210.1 | 65210 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - |
| 172.16.210.3 | 65211 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - |
| 172.17.10.5 | 65101 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | True | - |
| 172.17.110.0 | 65110 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - |
| 172.17.110.2 | 65110 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - |

### Router BGP EVPN Address Family

#### EVPN Peer Groups

| Peer Group | Activate |
| ---------- | -------- |
| EVPN-OVERLAY-PEERS | True |

### Router BGP Device Configuration

```eos
!
router bgp 65111
   router-id 172.16.110.3
   no bgp default ipv4-unicast
   distance bgp 20 200 200
   graceful-restart restart-time 300
   graceful-restart
   maximum-paths 4 ecmp 4
   neighbor EVPN-OVERLAY-PEERS peer group
   neighbor EVPN-OVERLAY-PEERS remote-as 65110
   neighbor EVPN-OVERLAY-PEERS next-hop-unchanged
   neighbor EVPN-OVERLAY-PEERS update-source Loopback0
   neighbor EVPN-OVERLAY-PEERS bfd
   neighbor EVPN-OVERLAY-PEERS ebgp-multihop 5
   neighbor EVPN-OVERLAY-PEERS password 7 q+VNViP5i4rVjW1cxFv2wA==
   neighbor EVPN-OVERLAY-PEERS send-community
   neighbor EVPN-OVERLAY-PEERS maximum-routes 0
   neighbor IPv4-UNDERLAY-PEERS peer group
   neighbor IPv4-UNDERLAY-PEERS remote-as 65110
   neighbor IPv4-UNDERLAY-PEERS password 7 AQQvKeimxJu+uGQ/yYvv9w==
   neighbor IPv4-UNDERLAY-PEERS send-community
   neighbor IPv4-UNDERLAY-PEERS maximum-routes 12000
   neighbor 172.16.20.1 peer group EVPN-OVERLAY-PEERS
   neighbor 172.16.20.1 remote-as 65201
   neighbor 172.16.20.1 description DC2-RS1
   neighbor 172.16.20.1 route-map RM-EVPN-FILTER-AS65201 out
   neighbor 172.16.110.4 peer group EVPN-OVERLAY-PEERS
   neighbor 172.16.110.4 remote-as 65112
   neighbor 172.16.110.4 description DC1-POD1-LEAF2A
   neighbor 172.16.110.5 peer group EVPN-OVERLAY-PEERS
   neighbor 172.16.110.5 remote-as 65112
   neighbor 172.16.110.5 description DC1-POD1-LEAF2B
   neighbor 172.16.200.1 peer group EVPN-OVERLAY-PEERS
   neighbor 172.16.200.1 remote-as 65200
   neighbor 172.16.200.1 description DC2-SUPER-SPINE1
   neighbor 172.16.200.1 route-map RM-EVPN-FILTER-AS65200 out
   neighbor 172.16.210.1 peer group EVPN-OVERLAY-PEERS
   neighbor 172.16.210.1 remote-as 65210
   neighbor 172.16.210.1 description DC2-POD1-SPINE1
   neighbor 172.16.210.1 route-map RM-EVPN-FILTER-AS65210 out
   neighbor 172.16.210.3 peer group EVPN-OVERLAY-PEERS
   neighbor 172.16.210.3 remote-as 65211
   neighbor 172.16.210.3 description DC2-POD1-LEAF1A
   neighbor 172.16.210.3 route-map RM-EVPN-FILTER-AS65211 out
   neighbor 172.17.10.5 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.10.5 remote-as 65101
   neighbor 172.17.10.5 description DC1-RS1_Ethernet3
   neighbor 172.17.10.5 bfd
   neighbor 172.17.110.0 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.110.0 remote-as 65110
   neighbor 172.17.110.0 description DC1-POD1-SPINE1_Ethernet3
   neighbor 172.17.110.2 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.110.2 remote-as 65110
   neighbor 172.17.110.2 description DC1-POD1-SPINE2_Ethernet3
   redistribute attached-host
   redistribute connected route-map RM-CONN-2-BGP
   !
   address-family evpn
      neighbor EVPN-OVERLAY-PEERS activate
   !
   address-family rt-membership
      neighbor EVPN-OVERLAY-PEERS activate
      neighbor EVPN-OVERLAY-PEERS default-route-target only
   !
   address-family ipv4
      no neighbor EVPN-OVERLAY-PEERS activate
      neighbor IPv4-UNDERLAY-PEERS activate
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

#### PL-L2LEAF-INBAND-MGMT

| Sequence | Action |
| -------- | ------ |
| 10 | permit 172.21.110.0/24 |

#### PL-LOOPBACKS-EVPN-OVERLAY

| Sequence | Action |
| -------- | ------ |
| 10 | permit 172.16.110.0/24 eq 32 |
| 20 | permit 172.18.110.0/24 eq 32 |

### Prefix-lists Device Configuration

```eos
!
ip prefix-list PL-L2LEAF-INBAND-MGMT
   seq 10 permit 172.21.110.0/24
!
ip prefix-list PL-LOOPBACKS-EVPN-OVERLAY
   seq 10 permit 172.16.110.0/24 eq 32
   seq 20 permit 172.18.110.0/24 eq 32
```

## Route-maps

### Route-maps Summary

#### RM-CONN-2-BGP

| Sequence | Type | Match and/or Set |
| -------- | ---- | ---------------- |
| 10 | permit | match ip address prefix-list PL-LOOPBACKS-EVPN-OVERLAY |
| 20 | permit | match ip address prefix-list PL-L2LEAF-INBAND-MGMT |

#### RM-EVPN-FILTER-AS65200

| Sequence | Type | Match and/or Set |
| -------- | ---- | ---------------- |
| 10 | deny | match as 65200 |

#### RM-EVPN-FILTER-AS65201

| Sequence | Type | Match and/or Set |
| -------- | ---- | ---------------- |
| 10 | deny | match as 65201 |

#### RM-EVPN-FILTER-AS65210

| Sequence | Type | Match and/or Set |
| -------- | ---- | ---------------- |
| 10 | deny | match as 65210 |

#### RM-EVPN-FILTER-AS65211

| Sequence | Type | Match and/or Set |
| -------- | ---- | ---------------- |
| 10 | deny | match as 65211 |

### Route-maps Device Configuration

```eos
!
route-map RM-CONN-2-BGP permit 10
   match ip address prefix-list PL-LOOPBACKS-EVPN-OVERLAY
!
route-map RM-CONN-2-BGP permit 20
   match ip address prefix-list PL-L2LEAF-INBAND-MGMT
!
route-map RM-EVPN-FILTER-AS65200 deny 10
   match as 65200
!
route-map RM-EVPN-FILTER-AS65200 permit 20
!
route-map RM-EVPN-FILTER-AS65201 deny 10
   match as 65201
!
route-map RM-EVPN-FILTER-AS65201 permit 20
!
route-map RM-EVPN-FILTER-AS65210 deny 10
   match as 65210
!
route-map RM-EVPN-FILTER-AS65210 permit 20
!
route-map RM-EVPN-FILTER-AS65211 deny 10
   match as 65211
!
route-map RM-EVPN-FILTER-AS65211 permit 20
```

# ACL

# VRF Instances

## VRF Instances Summary

| VRF Name | IP Routing |
| -------- | ---------- |
| MGMT | disabled |

## VRF Instances Device Configuration

```eos
!
vrf instance MGMT
```

# Quality Of Service

# EOS CLI

```eos
!
interface Loopback1002
  description Loopback created from raw_eos_cli under node DC1-POD1-LEAF1A

interface Loopback1111
  description Loopback created from raw_eos_cli under platform_settings vEOS-LAB

```
