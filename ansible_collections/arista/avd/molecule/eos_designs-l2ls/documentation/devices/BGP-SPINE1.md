# BGP-SPINE1

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
  - [Management API HTTP](#management-api-http)
- [Authentication](#authentication)
  - [Enable Password](#enable-password)
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
  - [Prefix-lists](#prefix-lists)
  - [Route-maps](#route-maps)
- [VRF Instances](#vrf-instances)
  - [VRF Instances Summary](#vrf-instances-summary)
  - [VRF Instances Device Configuration](#vrf-instances-device-configuration)

## Management

### Management Interfaces

#### Management Interfaces Summary

##### IPv4

| Management Interface | Description | Type | VRF | IP Address | Gateway |
| -------------------- | ----------- | ---- | --- | ---------- | ------- |
| Management1 | OOB_MANAGEMENT | oob | MGMT | 192.168.0.1/24 | 172.31.0.1 |

##### IPv6

| Management Interface | Description | Type | VRF | IPv6 Address | IPv6 Gateway |
| -------------------- | ----------- | ---- | --- | ------------ | ------------ |
| Management1 | OOB_MANAGEMENT | oob | MGMT | - | - |

#### Management Interfaces Device Configuration

```eos
!
interface Management1
   description OOB_MANAGEMENT
   no shutdown
   vrf MGMT
   ip address 192.168.0.1/24
```

### Management API HTTP

#### Management API HTTP Summary

| HTTP | HTTPS | UNIX-Socket | Default Services |
| ---- | ----- | ----------- | ---------------- |
| False | True | - | - |

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

## Authentication

### Enable Password

Enable password has been disabled

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
| 3100 | MLAG_L3_VRF_New_VRF | MLAG |
| 4092 | INBAND_MGMT | - |
| 4094 | MLAG | MLAG |

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
vlan 3100
   name MLAG_L3_VRF_New_VRF
   trunk group MLAG
!
vlan 4092
   name INBAND_MGMT
!
vlan 4094
   name MLAG
   trunk group MLAG
```

## Interfaces

### Ethernet Interfaces

#### Ethernet Interfaces Summary

##### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | Channel-Group |
| --------- | ----------- | ---- | ----- | ----------- | ----------- | ------------- |
| Ethernet1 | L2_BGP-LEAF1_Ethernet1 | *trunk | *1,100,200,4092 | *- | *- | 1 |
| Ethernet2 | L2_BGP-LEAF2_Ethernet1 | *trunk | *1,100,200,4092 | *- | *- | 1 |
| Ethernet3 | MLAG_BGP-SPINE2_Ethernet3 | *trunk | *- | *- | *MLAG | 3 |
| Ethernet4 | MLAG_BGP-SPINE2_Ethernet4 | *trunk | *- | *- | *MLAG | 3 |
| Ethernet10 | - | - | - | - | - | - |
| Ethernet11 | - | - | - | - | - | - |
| Ethernet12 | - | *- | *- | *- | *- | 12 |
| Ethernet13 | - | *- | *- | *- | *- | 13 |
| Ethernet14 | FIREWALL_CAMPUS_EGRESS_FW_1_Eth0 | - | - | - | - | - |
| Ethernet15 | FIREWALL_CAMPUS_EGRESS_FW_1_Eth2 | - | - | - | - | - |
| Ethernet16 | FIREWALL_CAMPUS_EGRESS_FW_1_Eth4 | *- | *- | *- | *- | 16 |
| Ethernet17 | FIREWALL_CAMPUS_EGRESS_FW_1_Eth6 | *- | *- | *- | *- | 17 |

*Inherited from Port-Channel Interface

##### Encapsulation Dot1q Interfaces

| Interface | Description | Vlan ID | Dot1q VLAN Tag | Dot1q Inner VLAN Tag |
| --------- | ----------- | ------- | -------------- | -------------------- |
| Ethernet18.100 | - | - | 100 | - |
| Ethernet18.101 | - | - | 101 | - |

##### IPv4

| Interface | Description | Channel Group | IP Address | VRF |  MTU | Shutdown | ACL In | ACL Out |
| --------- | ----------- | ------------- | ---------- | ----| ---- | -------- | ------ | ------- |
| Ethernet5 | P2P_DUMMY-CORE_Ethernet1/3 | - | 192.168.253.4/31 | default | 9214 | False | - | - |
| Ethernet6 | P2P_DUMMY-CORE_Ethernet1/5 | - | 192.168.253.8/31 | default | 9214 | False | - | - |
| Ethernet7 | P2P_DUMMY-CORE_Ethernet1/7 | 7 | *192.168.253.12/31 | *default | *9214 | *False | *- | *- |
| Ethernet8 | P2P_DUMMY-CORE_Ethernet1/9 | 8 | *192.168.253.16/31 | *default | *9214 | *False | *- | *- |
| Ethernet9 | - | - | 10.0.1.0/31 | default | - | False | - | - |
| Ethernet18.100 | - | - | 10.0.1.4/31 | default | - | False | - | - |
| Ethernet18.101 | - | - | 10.0.1.8/31 | New_VRF | - | False | - | - |

*Inherited from Port-Channel Interface

#### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet1
   description L2_BGP-LEAF1_Ethernet1
   no shutdown
   channel-group 1 mode active
!
interface Ethernet2
   description L2_BGP-LEAF2_Ethernet1
   no shutdown
   channel-group 1 mode active
!
interface Ethernet3
   description MLAG_BGP-SPINE2_Ethernet3
   no shutdown
   channel-group 3 mode active
!
interface Ethernet4
   description MLAG_BGP-SPINE2_Ethernet4
   no shutdown
   channel-group 3 mode active
!
interface Ethernet5
   description P2P_DUMMY-CORE_Ethernet1/3
   no shutdown
   mtu 9214
   no switchport
   ip address 192.168.253.4/31
!
interface Ethernet6
   description P2P_DUMMY-CORE_Ethernet1/5
   no shutdown
   mtu 9214
   no switchport
   ip address 192.168.253.8/31
!
interface Ethernet7
   description P2P_DUMMY-CORE_Ethernet1/7
   no shutdown
   channel-group 7 mode active
!
interface Ethernet8
   description P2P_DUMMY-CORE_Ethernet1/9
   no shutdown
   channel-group 8 mode active
!
interface Ethernet9
   no shutdown
   no switchport
   ip address 10.0.1.0/31
!
interface Ethernet10
   no shutdown
   switchport
!
interface Ethernet11
   no shutdown
   switchport
!
interface Ethernet12
   no shutdown
   channel-group 12 mode active
!
interface Ethernet13
   no shutdown
   channel-group 13 mode active
!
interface Ethernet14
   description FIREWALL_CAMPUS_EGRESS_FW_1_Eth0
   no shutdown
   switchport
!
interface Ethernet15
   description FIREWALL_CAMPUS_EGRESS_FW_1_Eth2
   no shutdown
   switchport
!
interface Ethernet16
   description FIREWALL_CAMPUS_EGRESS_FW_1_Eth4
   no shutdown
   channel-group 16 mode active
!
interface Ethernet17
   description FIREWALL_CAMPUS_EGRESS_FW_1_Eth6
   no shutdown
   channel-group 17 mode active
!
interface Ethernet18
   no shutdown
   no switchport
!
interface Ethernet18.100
   no shutdown
   encapsulation dot1q vlan 100
   ip address 10.0.1.4/31
!
interface Ethernet18.101
   no shutdown
   encapsulation dot1q vlan 101
   vrf New_VRF
   ip address 10.0.1.8/31
```

### Port-Channel Interfaces

#### Port-Channel Interfaces Summary

##### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | LACP Fallback Timeout | LACP Fallback Mode | MLAG ID | EVPN ESI |
| --------- | ----------- | ---- | ----- | ----------- | ------------| --------------------- | ------------------ | ------- | -------- |
| Port-Channel1 | L2_BGP-LEAFS_Port-Channel1 | trunk | 1,100,200,4092 | - | - | - | - | 1 | - |
| Port-Channel3 | MLAG_BGP-SPINE2_Port-Channel3 | trunk | - | - | MLAG | - | - | - | - |
| Port-Channel12 | - | - | - | - | - | - | - | 12 | - |
| Port-Channel13 | - | - | - | - | - | - | - | 13 | - |
| Port-Channel16 | FIREWALL_CAMPUS_EGRESS_FW_1 | - | - | - | - | - | - | - | - |
| Port-Channel17 | FIREWALL_CAMPUS_EGRESS_FW_1 | - | - | - | - | - | - | - | - |

##### IPv4

| Interface | Description | MLAG ID | IP Address | VRF | MTU | Shutdown | ACL In | ACL Out |
| --------- | ----------- | ------- | ---------- | --- | --- | -------- | ------ | ------- |
| Port-Channel7 | P2P_DUMMY-CORE_Port-Channel17 | - | 192.168.253.12/31 | default | 9214 | False | - | - |
| Port-Channel8 | P2P_DUMMY-CORE_Port-Channel19 | - | 192.168.253.16/31 | default | 9214 | False | - | - |

#### Port-Channel Interfaces Device Configuration

```eos
!
interface Port-Channel1
   description L2_BGP-LEAFS_Port-Channel1
   no shutdown
   switchport trunk allowed vlan 1,100,200,4092
   switchport mode trunk
   switchport
   mlag 1
!
interface Port-Channel3
   description MLAG_BGP-SPINE2_Port-Channel3
   no shutdown
   switchport mode trunk
   switchport trunk group MLAG
   switchport
!
interface Port-Channel7
   description P2P_DUMMY-CORE_Port-Channel17
   no shutdown
   mtu 9214
   no switchport
   ip address 192.168.253.12/31
!
interface Port-Channel8
   description P2P_DUMMY-CORE_Port-Channel19
   no shutdown
   mtu 9214
   no switchport
   ip address 192.168.253.16/31
!
interface Port-Channel12
   no shutdown
   switchport
   mlag 12
!
interface Port-Channel13
   no shutdown
   switchport
   mlag 13
!
interface Port-Channel16
   description FIREWALL_CAMPUS_EGRESS_FW_1
   no shutdown
   switchport
!
interface Port-Channel17
   description FIREWALL_CAMPUS_EGRESS_FW_1
   no shutdown
   switchport
```

### Loopback Interfaces

#### Loopback Interfaces Summary

##### IPv4

| Interface | Description | VRF | IP Address |
| --------- | ----------- | --- | ---------- |
| Loopback0 | ROUTER_ID | default | 192.168.255.1/32 |

##### IPv6

| Interface | Description | VRF | IPv6 Address |
| --------- | ----------- | --- | ------------ |
| Loopback0 | ROUTER_ID | default | - |

#### Loopback Interfaces Device Configuration

```eos
!
interface Loopback0
   description ROUTER_ID
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
| Vlan3100 | MLAG_L3_VRF_New_VRF | New_VRF | 9214 | False |
| Vlan4092 | Inband Management | default | 1500 | False |
| Vlan4094 | MLAG | default | 9214 | False |

##### IPv4

| Interface | VRF | IP Address | IP Address Virtual | IP Router Virtual Address | ACL In | ACL Out |
| --------- | --- | ---------- | ------------------ | ------------------------- | ------ | ------- |
| Vlan1 |  default  |  -  |  10.1.1.1/24  |  -  |  -  |  -  |
| Vlan100 |  default  |  -  |  10.1.100.1/24  |  -  |  -  |  -  |
| Vlan200 |  default  |  -  |  10.1.200.1/24  |  -  |  -  |  -  |
| Vlan220 |  default  |  -  |  10.1.220.1/24  |  -  |  -  |  -  |
| Vlan3100 |  New_VRF  |  192.168.254.0/31  |  -  |  -  |  -  |  -  |
| Vlan4092 |  default  |  172.23.254.2/24  |  -  |  172.23.254.1  |  -  |  -  |
| Vlan4094 |  default  |  192.168.254.0/31  |  -  |  -  |  -  |  -  |

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
interface Vlan3100
   description MLAG_L3_VRF_New_VRF
   no shutdown
   mtu 9214
   vrf New_VRF
   ip address 192.168.254.0/31
!
interface Vlan4092
   description Inband Management
   no shutdown
   mtu 1500
   ip address 172.23.254.2/24
   ip attached-host route export 19
   ip virtual-router address 172.23.254.1
!
interface Vlan4094
   description MLAG
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
| New_VRF | True |

#### IP Routing Device Configuration

```eos
!
ip routing
no ip routing vrf MGMT
ip routing vrf New_VRF
```

### IPv6 Routing

#### IPv6 Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | False |
| MGMT | false |
| New_VRF | false |

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

ASN Notation: asplain

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

| Neighbor | Remote AS | VRF | Shutdown | Send-community | Maximum-routes | Allowas-in | BFD | RIB Pre-Policy Retain | Route-Reflector Client | Passive | TTL Max Hops |
| -------- | --------- | --- | -------- | -------------- | -------------- | ---------- | --- | --------------------- | ---------------------- | ------- | ------------ |
| 192.168.253.5 | 65000 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - | - |
| 192.168.253.9 | 65000 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - | - |
| 192.168.253.13 | 65000 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - | - |
| 192.168.253.17 | 65000 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - | - |
| 192.168.254.1 | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | default | - | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | - | - | - | - | - | - |

#### Router BGP Device Configuration

```eos
!
router bgp 65001
   router-id 192.168.255.1
   update wait-install
   no bgp default ipv4-unicast
   maximum-paths 4 ecmp 4
   neighbor IPv4-UNDERLAY-PEERS peer group
   neighbor IPv4-UNDERLAY-PEERS send-community
   neighbor IPv4-UNDERLAY-PEERS maximum-routes 12000
   neighbor MLAG-IPv4-UNDERLAY-PEER peer group
   neighbor MLAG-IPv4-UNDERLAY-PEER remote-as 65001
   neighbor MLAG-IPv4-UNDERLAY-PEER next-hop-self
   neighbor MLAG-IPv4-UNDERLAY-PEER description BGP-SPINE2
   neighbor MLAG-IPv4-UNDERLAY-PEER route-map RM-MLAG-PEER-IN in
   neighbor MLAG-IPv4-UNDERLAY-PEER send-community
   neighbor MLAG-IPv4-UNDERLAY-PEER maximum-routes 12000
   neighbor 192.168.253.5 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.253.5 remote-as 65000
   neighbor 192.168.253.5 description DUMMY-CORE
   neighbor 192.168.253.9 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.253.9 remote-as 65000
   neighbor 192.168.253.9 description DUMMY-CORE
   neighbor 192.168.253.13 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.253.13 remote-as 65000
   neighbor 192.168.253.13 description DUMMY-CORE
   neighbor 192.168.253.17 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.253.17 remote-as 65000
   neighbor 192.168.253.17 description DUMMY-CORE
   neighbor 192.168.254.1 peer group MLAG-IPv4-UNDERLAY-PEER
   neighbor 192.168.254.1 description BGP-SPINE2_Vlan4094
   redistribute connected
   redistribute attached-host
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

### Prefix-lists

#### Prefix-lists Summary

##### PL-MLAG-PEER-VRFS

| Sequence | Action |
| -------- | ------ |
| 10 | permit 192.168.254.0/31 |

#### Prefix-lists Device Configuration

```eos
!
ip prefix-list PL-MLAG-PEER-VRFS
   seq 10 permit 192.168.254.0/31
```

### Route-maps

#### Route-maps Summary

##### RM-CONN-2-BGP-VRFS

| Sequence | Type | Match | Set | Sub-Route-Map | Continue |
| -------- | ---- | ----- | --- | ------------- | -------- |
| 10 | deny | ip address prefix-list PL-MLAG-PEER-VRFS | - | - | - |
| 20 | permit | - | - | - | - |

##### RM-MLAG-PEER-IN

| Sequence | Type | Match | Set | Sub-Route-Map | Continue |
| -------- | ---- | ----- | --- | ------------- | -------- |
| 10 | permit | - | origin incomplete | - | - |

#### Route-maps Device Configuration

```eos
!
route-map RM-CONN-2-BGP-VRFS deny 10
   match ip address prefix-list PL-MLAG-PEER-VRFS
!
route-map RM-CONN-2-BGP-VRFS permit 20
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
| New_VRF | enabled |

### VRF Instances Device Configuration

```eos
!
vrf instance MGMT
!
vrf instance New_VRF
```
