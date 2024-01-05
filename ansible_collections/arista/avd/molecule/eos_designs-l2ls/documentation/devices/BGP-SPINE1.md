# BGP-SPINE1

## Table of Contents

- [Management](#management)
  - [Management API HTTP](#management-api-http)
- [MLAG](#mlag)
  - [MLAG Summary](#mlag-summary)
  - [MLAG Device Configuration](#mlag-device-configuration)
- [Spanning Tree](#spanning-tree)
  - [Spanning Tree Summary](#spanning-tree-summary)
  - [Spanning Tree Device Configuration](#spanning-tree-device-configuration)
- [Internal VLAN Allocation Policy](#internal-vlan-allocation-policy)
  - [Internal VLAN Allocation Policy Summary](#internal-vlan-allocation-policy-summary)
  - [Internal VLAN Allocation Policy Device Configuration](#internal-vlan-allocation-policy-device-configuration)
- [VLANs](#vlans)
  - [VLANs Summary](#vlans-summary)
  - [VLANs Device Configuration](#vlans-device-configuration)
- [Interfaces](#interfaces)
  - [Ethernet Interfaces](#ethernet-interfaces)
  - [Port-Channel Interfaces](#port-channel-interfaces)
  - [Loopback Interfaces](#loopback-interfaces)
  - [VLAN Interfaces](#vlan-interfaces)
- [Routing](#routing)
  - [Service Routing Protocols Model](#service-routing-protocols-model)
  - [Virtual Router MAC Address](#virtual-router-mac-address)
  - [IP Routing](#ip-routing)
  - [IPv6 Routing](#ipv6-routing)
  - [Static Routes](#static-routes)
  - [Router BGP](#router-bgp)
- [Multicast](#multicast)
  - [IP IGMP Snooping](#ip-igmp-snooping)
- [Filters](#filters)
  - [Route-maps](#route-maps)
- [VRF Instances](#vrf-instances)
  - [VRF Instances Summary](#vrf-instances-summary)
  - [VRF Instances Device Configuration](#vrf-instances-device-configuration)

## Management

### Management API HTTP

#### Management API HTTP Summary

| HTTP | HTTPS | Default Services |
| ---- | ----- | ---------------- |
| False | True | - |

#### Management API VRF Access

| VRF Name | IPv4 ACL | IPv6 ACL |
| -------- | -------- | -------- |
| MGMT | - | - |

#### Management API HTTP Device Configuration

```eos
!
management api http-commands
   protocol https
   no shutdown
   !
   vrf MGMT
      no shutdown
```

## MLAG

### MLAG Summary

| Domain-id | Local-interface | Peer-address | Peer-link |
| --------- | --------------- | ------------ | --------- |
| BGP_SPINES | Vlan4094 | 192.168.254.1 | Port-Channel3 |

Dual primary detection is disabled.

### MLAG Device Configuration

```eos
!
mlag configuration
   domain-id BGP_SPINES
   local-interface Vlan4094
   peer-address 192.168.254.1
   peer-link Port-Channel3
   reload-delay mlag 300
   reload-delay non-mlag 330
```

## Spanning Tree

### Spanning Tree Summary

STP mode: **mstp**

#### Global Spanning-Tree Settings

- Spanning Tree disabled for VLANs: **4094**

### Spanning Tree Device Configuration

```eos
!
no spanning-tree vlan-id 4094
```

## Internal VLAN Allocation Policy

### Internal VLAN Allocation Policy Summary

| Policy Allocation | Range Beginning | Range Ending |
| ------------------| --------------- | ------------ |
| ascending | 1006 | 1199 |

### Internal VLAN Allocation Policy Device Configuration

```eos
!
vlan internal order ascending range 1006 1199
```

## VLANs

### VLANs Summary

| VLAN ID | Name | Trunk Groups |
| ------- | ---- | ------------ |
| 1 | SVI_1 | - |
| 100 | SVI_100 | - |
| 200 | SVI_200 | - |
| 220 | SVI_220 | - |
| 4094 | MLAG_PEER | MLAG |

### VLANs Device Configuration

```eos
!
vlan 1
   name SVI_1
!
vlan 100
   name SVI_100
!
vlan 200
   name SVI_200
!
vlan 220
   name SVI_220
!
vlan 4094
   name MLAG_PEER
   trunk group MLAG
```

## Interfaces

### Ethernet Interfaces

#### Ethernet Interfaces Summary

##### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | Channel-Group |
| --------- | ----------- | ---- | ----- | ----------- | ----------- | ------------- |
| Ethernet1 | BGP-LEAF1_Ethernet1 | *trunk | *1,100,200 | *- | *- | 1 |
| Ethernet2 | BGP-LEAF2_Ethernet1 | *trunk | *100 | *- | *- | 2 |
| Ethernet3 | MLAG_PEER_BGP-SPINE2_Ethernet3 | *trunk | *- | *- | *['LEAF_PEER_L3', 'MLAG'] | 3 |
| Ethernet4 | MLAG_PEER_BGP-SPINE2_Ethernet4 | *trunk | *- | *- | *['LEAF_PEER_L3', 'MLAG'] | 3 |

*Inherited from Port-Channel Interface

##### IPv4

| Interface | Description | Type | Channel Group | IP Address | VRF |  MTU | Shutdown | ACL In | ACL Out |
| --------- | ----------- | -----| ------------- | ---------- | ----| ---- | -------- | ------ | ------- |
| Ethernet5 | P2P_LINK_TO_DUMMY-CORE_Ethernet1/3 | routed | - | 192.168.253.4/31 | default | 9214 | False | - | - |

#### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet1
   description BGP-LEAF1_Ethernet1
   no shutdown
   channel-group 1 mode active
!
interface Ethernet2
   description BGP-LEAF2_Ethernet1
   no shutdown
   channel-group 2 mode active
!
interface Ethernet3
   description MLAG_PEER_BGP-SPINE2_Ethernet3
   no shutdown
   channel-group 3 mode active
!
interface Ethernet4
   description MLAG_PEER_BGP-SPINE2_Ethernet4
   no shutdown
   channel-group 3 mode active
!
interface Ethernet5
   description P2P_LINK_TO_DUMMY-CORE_Ethernet1/3
   no shutdown
   mtu 9214
   no switchport
   ip address 192.168.253.4/31
```

### Port-Channel Interfaces

#### Port-Channel Interfaces Summary

##### L2

| Interface | Description | Type | Mode | VLANs | Native VLAN | Trunk Group | LACP Fallback Timeout | LACP Fallback Mode | MLAG ID | EVPN ESI |
| --------- | ----------- | ---- | ---- | ----- | ----------- | ------------| --------------------- | ------------------ | ------- | -------- |
| Port-Channel1 | BGP-LEAF1_Po1 | switched | trunk | 1,100,200 | - | - | - | - | 1 | - |
| Port-Channel2 | BGP-LEAF2_Po1 | switched | trunk | 100 | - | - | - | - | 2 | - |
| Port-Channel3 | MLAG_PEER_BGP-SPINE2_Po3 | switched | trunk | - | - | ['LEAF_PEER_L3', 'MLAG'] | - | - | - | - |

#### Port-Channel Interfaces Device Configuration

```eos
!
interface Port-Channel1
   description BGP-LEAF1_Po1
   no shutdown
   switchport
   switchport trunk allowed vlan 1,100,200
   switchport mode trunk
   mlag 1
!
interface Port-Channel2
   description BGP-LEAF2_Po1
   no shutdown
   switchport
   switchport trunk allowed vlan 100
   switchport mode trunk
   mlag 2
!
interface Port-Channel3
   description MLAG_PEER_BGP-SPINE2_Po3
   no shutdown
   switchport
   switchport mode trunk
   switchport trunk group LEAF_PEER_L3
   switchport trunk group MLAG
```

### Loopback Interfaces

#### Loopback Interfaces Summary

##### IPv4

| Interface | Description | VRF | IP Address |
| --------- | ----------- | --- | ---------- |
| Loopback0 | Router_ID | default | 192.168.255.1/32 |

##### IPv6

| Interface | Description | VRF | IPv6 Address |
| --------- | ----------- | --- | ------------ |
| Loopback0 | Router_ID | default | - |

#### Loopback Interfaces Device Configuration

```eos
!
interface Loopback0
   description Router_ID
   no shutdown
   ip address 192.168.255.1/32
```

### VLAN Interfaces

#### VLAN Interfaces Summary

| Interface | Description | VRF |  MTU | Shutdown |
| --------- | ----------- | --- | ---- | -------- |
| Vlan1 | SVI_1 | default | - | False |
| Vlan100 | SVI_100 | default | - | False |
| Vlan200 | SVI_200 | default | - | False |
| Vlan220 | SVI_220 | default | - | False |
| Vlan4094 | MLAG_PEER | default | 9214 | False |

##### IPv4

| Interface | VRF | IP Address | IP Address Virtual | IP Router Virtual Address | VRRP | ACL In | ACL Out |
| --------- | --- | ---------- | ------------------ | ------------------------- | ---- | ------ | ------- |
| Vlan1 |  default  |  -  |  10.1.1.1/24  |  -  |  -  |  -  |  -  |
| Vlan100 |  default  |  -  |  10.1.100.1/24  |  -  |  -  |  -  |  -  |
| Vlan200 |  default  |  -  |  10.1.200.1/24  |  -  |  -  |  -  |  -  |
| Vlan220 |  default  |  -  |  10.1.220.1/24  |  -  |  -  |  -  |  -  |
| Vlan4094 |  default  |  192.168.254.0/31  |  -  |  -  |  -  |  -  |  -  |

#### VLAN Interfaces Device Configuration

```eos
!
interface Vlan1
   description SVI_1
   no shutdown
   ip address virtual 10.1.1.1/24
!
interface Vlan100
   description SVI_100
   no shutdown
   ip address virtual 10.1.100.1/24
!
interface Vlan200
   description SVI_200
   no shutdown
   ip address virtual 10.1.200.1/24
!
interface Vlan220
   description SVI_220
   no shutdown
   ip address virtual 10.1.220.1/24
!
interface Vlan4094
   description MLAG_PEER
   no shutdown
   mtu 9214
   no autostate
   ip address 192.168.254.0/31
```

## Routing

### Service Routing Protocols Model

Multi agent routing protocol model enabled

```eos
!
service routing protocols model multi-agent
```

### Virtual Router MAC Address

#### Virtual Router MAC Address Summary

Virtual Router MAC Address: 00:1c:73:00:00:99

#### Virtual Router MAC Address Device Configuration

```eos
!
ip virtual-router mac-address 00:1c:73:00:00:99
```

### IP Routing

#### IP Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | True |
| MGMT | False |

#### IP Routing Device Configuration

```eos
!
ip routing
no ip routing vrf MGMT
```

### IPv6 Routing

#### IPv6 Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | False |
| MGMT | false |

### Static Routes

#### Static Routes Summary

| VRF | Destination Prefix | Next Hop IP | Exit interface | Administrative Distance | Tag | Route Name | Metric |
| --- | ------------------ | ----------- | -------------- | ----------------------- | --- | ---------- | ------ |
| MGMT | 0.0.0.0/0 | 172.31.0.1 | - | 1 | - | - | - |

#### Static Routes Device Configuration

```eos
!
ip route vrf MGMT 0.0.0.0/0 172.31.0.1
```

### Router BGP

#### Router BGP Summary

| BGP AS | Router ID |
| ------ | --------- |
| 65001 | 192.168.255.1 |

| BGP Tuning |
| ---------- |
| update wait-install |
| no bgp default ipv4-unicast |
| maximum-paths 4 ecmp 4 |

#### Router BGP Peer Groups

##### IPv4-UNDERLAY-PEERS

| Settings | Value |
| -------- | ----- |
| Address Family | ipv4 |
| Send community | all |
| Maximum routes | 12000 |

##### MLAG-IPv4-UNDERLAY-PEER

| Settings | Value |
| -------- | ----- |
| Address Family | ipv4 |
| Remote AS | 65001 |
| Next-hop self | True |
| Send community | all |
| Maximum routes | 12000 |

#### BGP Neighbors

| Neighbor | Remote AS | VRF | Shutdown | Send-community | Maximum-routes | Allowas-in | BFD | RIB Pre-Policy Retain | Route-Reflector Client | Passive |
| -------- | --------- | --- | -------- | -------------- | -------------- | ---------- | --- | --------------------- | ---------------------- | ------- |
| 192.168.253.5 | 65000 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.254.1 | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | default | - | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | - | - | - | - | - |

#### Router BGP Device Configuration

```eos
!
router bgp 65001
   router-id 192.168.255.1
   maximum-paths 4 ecmp 4
   update wait-install
   no bgp default ipv4-unicast
   neighbor IPv4-UNDERLAY-PEERS peer group
   neighbor IPv4-UNDERLAY-PEERS send-community
   neighbor IPv4-UNDERLAY-PEERS maximum-routes 12000
   neighbor MLAG-IPv4-UNDERLAY-PEER peer group
   neighbor MLAG-IPv4-UNDERLAY-PEER remote-as 65001
   neighbor MLAG-IPv4-UNDERLAY-PEER next-hop-self
   neighbor MLAG-IPv4-UNDERLAY-PEER description BGP-SPINE2
   neighbor MLAG-IPv4-UNDERLAY-PEER send-community
   neighbor MLAG-IPv4-UNDERLAY-PEER maximum-routes 12000
   neighbor MLAG-IPv4-UNDERLAY-PEER route-map RM-MLAG-PEER-IN in
   neighbor 192.168.253.5 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.253.5 remote-as 65000
   neighbor 192.168.253.5 description DUMMY-CORE
   neighbor 192.168.254.1 peer group MLAG-IPv4-UNDERLAY-PEER
   neighbor 192.168.254.1 description BGP-SPINE2
   redistribute connected
   !
   address-family ipv4
      neighbor IPv4-UNDERLAY-PEERS activate
      neighbor MLAG-IPv4-UNDERLAY-PEER activate
```

## Multicast

### IP IGMP Snooping

#### IP IGMP Snooping Summary

| IGMP Snooping | Fast Leave | Interface Restart Query | Proxy | Restart Query Interval | Robustness Variable |
| ------------- | ---------- | ----------------------- | ----- | ---------------------- | ------------------- |
| Enabled | - | - | - | - | - |

#### IP IGMP Snooping Device Configuration

```eos
```

## Filters

### Route-maps

#### Route-maps Summary

##### RM-MLAG-PEER-IN

| Sequence | Type | Match | Set | Sub-Route-Map | Continue |
| -------- | ---- | ----- | --- | ------------- | -------- |
| 10 | permit | - | origin incomplete | - | - |

#### Route-maps Device Configuration

```eos
!
route-map RM-MLAG-PEER-IN permit 10
   description Make routes learned over MLAG Peer-link less preferred on spines to ensure optimal routing
   set origin incomplete
```

## VRF Instances

### VRF Instances Summary

| VRF Name | IP Routing |
| -------- | ---------- |
| MGMT | disabled |

### VRF Instances Device Configuration

```eos
!
vrf instance MGMT
```
