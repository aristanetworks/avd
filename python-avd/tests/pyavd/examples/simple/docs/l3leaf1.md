# l3leaf1

## Table of Contents

<!-- toc -->
<!-- toc -->

## Authentication

### Enable Password

Enable password has been disabled

## Internal VLAN Allocation Policy

### Internal VLAN Allocation Policy Summary

| Policy Allocation | Range Beginning | Range Ending |
| ----------------- | --------------- | ------------ |
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
| 101 | VLAN101 | - |
| 102 | VLAN102 | - |

### VLANs Device Configuration

```eos
!
vlan 101
   name VLAN101
!
vlan 102
   name VLAN102
```

## Interfaces

### Ethernet Interfaces

#### Ethernet Interfaces Summary

##### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | Channel-Group |
| --------- | ----------- | ---- | ----- | ----------- | ----------- | ------------- |
| Ethernet1 | User port | trunk | 100-200,222,456,999-3000 | - | - | - |
| Ethernet1/4 | L2_l2leaf1_Ethernet1/2 | *trunk | *101-102 | *- | *- | 13 |
| Ethernet2 | User port | trunk | 100-200,222,456,999-3000 | - | - | - |
| Ethernet2/4 | L2_l2leaf2_Ethernet2/2 | *trunk | *101-102 | *- | *- | 23 |
| Ethernet3 | User port | trunk | 100-200,222,456,999-3000 | - | - | - |
| Ethernet4 | User port | trunk | 100-200,222,456,999-3000 | - | - | - |
| Ethernet5 | User port | trunk | 100-200,222,456,999-3000 | - | - | - |
| Ethernet6 | User port | trunk | 100-200,222,456,999-3000 | - | - | - |
| Ethernet7 | User port | trunk | 100-200,222,456,999-3000 | - | - | - |
| Ethernet8 | User port | trunk | 100-200,222,456,999-3000 | - | - | - |
| Ethernet9 | User port | trunk | 100-200,222,456,999-3000 | - | - | - |
| Ethernet10 | User port | trunk | 100-200,222,456,999-3000 | - | - | - |
| Ethernet11 | User port | trunk | 100-200,222,456,999-3000 | - | - | - |
| Ethernet12 | User port | trunk | 100-200,222,456,999-3000 | - | - | - |
| Ethernet13 | User port | trunk | 100-200,222,456,999-3000 | - | - | - |
| Ethernet14 | User port | trunk | 100-200,222,456,999-3000 | - | - | - |
| Ethernet15 | User port | trunk | 100-200,222,456,999-3000 | - | - | - |
| Ethernet16 | User port | trunk | 100-200,222,456,999-3000 | - | - | - |
| Ethernet17 | User port | trunk | 100-200,222,456,999-3000 | - | - | - |
| Ethernet18 | User port | trunk | 100-200,222,456,999-3000 | - | - | - |
| Ethernet19 | User port | trunk | 100-200,222,456,999-3000 | - | - | - |
| Ethernet20 | User port | trunk | 100-200,222,456,999-3000 | - | - | - |
| Ethernet21 | User port | trunk | 100-200,222,456,999-3000 | - | - | - |
| Ethernet22 | User port | trunk | 100-200,222,456,999-3000 | - | - | - |
| Ethernet23 | User port | trunk | 100-200,222,456,999-3000 | - | - | - |
| Ethernet24 | User port | trunk | 100-200,222,456,999-3000 | - | - | - |
| Ethernet25 | Phone port | trunk phone | - | 200 | - | - |
| Ethernet26 | Phone port | trunk phone | - | 200 | - | - |
| Ethernet27 | Phone port | trunk phone | - | 200 | - | - |
| Ethernet28 | Phone port | trunk phone | - | 200 | - | - |
| Ethernet29 | Phone port | trunk phone | - | 200 | - | - |
| Ethernet30 | Phone port | trunk phone | - | 200 | - | - |
| Ethernet31 | Phone port | trunk phone | - | 200 | - | - |
| Ethernet32 | Phone port | trunk phone | - | 200 | - | - |
| Ethernet33 | Phone port | trunk phone | - | 200 | - | - |
| Ethernet34 | Phone port | trunk phone | - | 200 | - | - |
| Ethernet35 | Phone port | trunk phone | - | 200 | - | - |
| Ethernet36 | Phone port | trunk phone | - | 200 | - | - |
| Ethernet37 | Phone port | trunk phone | - | 200 | - | - |
| Ethernet38 | Phone port | trunk phone | - | 200 | - | - |
| Ethernet39 | Phone port | trunk phone | - | 200 | - | - |
| Ethernet40 | Phone port | trunk phone | - | 200 | - | - |
| Ethernet41 | Phone port | trunk phone | - | 200 | - | - |
| Ethernet42 | Phone port | trunk phone | - | 200 | - | - |
| Ethernet43 | Phone port | trunk phone | - | 200 | - | - |
| Ethernet44 | Phone port | trunk phone | - | 200 | - | - |
| Ethernet45 | Phone port | trunk phone | - | 200 | - | - |
| Ethernet46 | Phone port | trunk phone | - | 200 | - | - |
| Ethernet47 | Phone port | trunk phone | - | 200 | - | - |
| Ethernet48 | Phone port | trunk phone | - | 200 | - | - |

*Inherited from Port-Channel Interface

##### IPv4

| Interface | Description | Channel Group | IP Address | VRF | MTU | Shutdown | ACL In | ACL Out |
| --------- | ----------- | ------------- | ---------- | --- | --- | -------- | ------ | ------- |
| Ethernet1/1 | P2P_spine1_Ethernet1/3 | - | 10.4.0.1/31 | default | 9214 | False | - | - |
| Ethernet1/2 | P2P_spine2_Ethernet1/4 | - | 10.4.0.3/31 | default | 9214 | False | - | - |

#### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet1
   description User port
   no shutdown
   switchport trunk allowed vlan 100-200,456,222,999,1000-3000
   switchport mode trunk
   switchport
!
interface Ethernet1/1
   description P2P_spine1_Ethernet1/3
   no shutdown
   mtu 9214
   no switchport
   ip address 10.4.0.1/31
!
interface Ethernet1/2
   description P2P_spine2_Ethernet1/4
   no shutdown
   mtu 9214
   no switchport
   ip address 10.4.0.3/31
!
interface Ethernet1/4
   description L2_l2leaf1_Ethernet1/2
   no shutdown
   channel-group 13 mode active
!
interface Ethernet2
   description User port
   no shutdown
   switchport trunk allowed vlan 100-200,456,222,999,1000-3000
   switchport mode trunk
   switchport
!
interface Ethernet2/4
   description L2_l2leaf2_Ethernet2/2
   no shutdown
   channel-group 23 mode active
!
interface Ethernet3
   description User port
   no shutdown
   switchport trunk allowed vlan 100-200,456,222,999,1000-3000
   switchport mode trunk
   switchport
!
interface Ethernet4
   description User port
   no shutdown
   switchport trunk allowed vlan 100-200,456,222,999,1000-3000
   switchport mode trunk
   switchport
!
interface Ethernet5
   description User port
   no shutdown
   switchport trunk allowed vlan 100-200,456,222,999,1000-3000
   switchport mode trunk
   switchport
!
interface Ethernet6
   description User port
   no shutdown
   switchport trunk allowed vlan 100-200,456,222,999,1000-3000
   switchport mode trunk
   switchport
!
interface Ethernet7
   description User port
   no shutdown
   switchport trunk allowed vlan 100-200,456,222,999,1000-3000
   switchport mode trunk
   switchport
!
interface Ethernet8
   description User port
   no shutdown
   switchport trunk allowed vlan 100-200,456,222,999,1000-3000
   switchport mode trunk
   switchport
!
interface Ethernet9
   description User port
   no shutdown
   switchport trunk allowed vlan 100-200,456,222,999,1000-3000
   switchport mode trunk
   switchport
!
interface Ethernet10
   description User port
   no shutdown
   switchport trunk allowed vlan 100-200,456,222,999,1000-3000
   switchport mode trunk
   switchport
!
interface Ethernet11
   description User port
   no shutdown
   switchport trunk allowed vlan 100-200,456,222,999,1000-3000
   switchport mode trunk
   switchport
!
interface Ethernet12
   description User port
   no shutdown
   switchport trunk allowed vlan 100-200,456,222,999,1000-3000
   switchport mode trunk
   switchport
!
interface Ethernet13
   description User port
   no shutdown
   switchport trunk allowed vlan 100-200,456,222,999,1000-3000
   switchport mode trunk
   switchport
!
interface Ethernet14
   description User port
   no shutdown
   switchport trunk allowed vlan 100-200,456,222,999,1000-3000
   switchport mode trunk
   switchport
!
interface Ethernet15
   description User port
   no shutdown
   switchport trunk allowed vlan 100-200,456,222,999,1000-3000
   switchport mode trunk
   switchport
!
interface Ethernet16
   description User port
   no shutdown
   switchport trunk allowed vlan 100-200,456,222,999,1000-3000
   switchport mode trunk
   switchport
!
interface Ethernet17
   description User port
   no shutdown
   switchport trunk allowed vlan 100-200,456,222,999,1000-3000
   switchport mode trunk
   switchport
!
interface Ethernet18
   description User port
   no shutdown
   switchport trunk allowed vlan 100-200,456,222,999,1000-3000
   switchport mode trunk
   switchport
!
interface Ethernet19
   description User port
   no shutdown
   switchport trunk allowed vlan 100-200,456,222,999,1000-3000
   switchport mode trunk
   switchport
!
interface Ethernet20
   description User port
   no shutdown
   switchport trunk allowed vlan 100-200,456,222,999,1000-3000
   switchport mode trunk
   switchport
!
interface Ethernet21
   description User port
   no shutdown
   switchport trunk allowed vlan 100-200,456,222,999,1000-3000
   switchport mode trunk
   switchport
!
interface Ethernet22
   description User port
   no shutdown
   switchport trunk allowed vlan 100-200,456,222,999,1000-3000
   switchport mode trunk
   switchport
!
interface Ethernet23
   description User port
   no shutdown
   switchport trunk allowed vlan 100-200,456,222,999,1000-3000
   switchport mode trunk
   switchport
!
interface Ethernet24
   description User port
   no shutdown
   switchport trunk allowed vlan 100-200,456,222,999,1000-3000
   switchport mode trunk
   switchport
!
interface Ethernet25
   description Phone port
   no shutdown
   switchport trunk native vlan 200
   switchport mode trunk phone
   switchport
!
interface Ethernet26
   description Phone port
   no shutdown
   switchport trunk native vlan 200
   switchport mode trunk phone
   switchport
!
interface Ethernet27
   description Phone port
   no shutdown
   switchport trunk native vlan 200
   switchport mode trunk phone
   switchport
!
interface Ethernet28
   description Phone port
   no shutdown
   switchport trunk native vlan 200
   switchport mode trunk phone
   switchport
!
interface Ethernet29
   description Phone port
   no shutdown
   switchport trunk native vlan 200
   switchport mode trunk phone
   switchport
!
interface Ethernet30
   description Phone port
   no shutdown
   switchport trunk native vlan 200
   switchport mode trunk phone
   switchport
!
interface Ethernet31
   description Phone port
   no shutdown
   switchport trunk native vlan 200
   switchport mode trunk phone
   switchport
!
interface Ethernet32
   description Phone port
   no shutdown
   switchport trunk native vlan 200
   switchport mode trunk phone
   switchport
!
interface Ethernet33
   description Phone port
   no shutdown
   switchport trunk native vlan 200
   switchport mode trunk phone
   switchport
!
interface Ethernet34
   description Phone port
   no shutdown
   switchport trunk native vlan 200
   switchport mode trunk phone
   switchport
!
interface Ethernet35
   description Phone port
   no shutdown
   switchport trunk native vlan 200
   switchport mode trunk phone
   switchport
!
interface Ethernet36
   description Phone port
   no shutdown
   switchport trunk native vlan 200
   switchport mode trunk phone
   switchport
!
interface Ethernet37
   description Phone port
   no shutdown
   switchport trunk native vlan 200
   switchport mode trunk phone
   switchport
!
interface Ethernet38
   description Phone port
   no shutdown
   switchport trunk native vlan 200
   switchport mode trunk phone
   switchport
!
interface Ethernet39
   description Phone port
   no shutdown
   switchport trunk native vlan 200
   switchport mode trunk phone
   switchport
!
interface Ethernet40
   description Phone port
   no shutdown
   switchport trunk native vlan 200
   switchport mode trunk phone
   switchport
!
interface Ethernet41
   description Phone port
   no shutdown
   switchport trunk native vlan 200
   switchport mode trunk phone
   switchport
!
interface Ethernet42
   description Phone port
   no shutdown
   switchport trunk native vlan 200
   switchport mode trunk phone
   switchport
!
interface Ethernet43
   description Phone port
   no shutdown
   switchport trunk native vlan 200
   switchport mode trunk phone
   switchport
!
interface Ethernet44
   description Phone port
   no shutdown
   switchport trunk native vlan 200
   switchport mode trunk phone
   switchport
!
interface Ethernet45
   description Phone port
   no shutdown
   switchport trunk native vlan 200
   switchport mode trunk phone
   switchport
!
interface Ethernet46
   description Phone port
   no shutdown
   switchport trunk native vlan 200
   switchport mode trunk phone
   switchport
!
interface Ethernet47
   description Phone port
   no shutdown
   switchport trunk native vlan 200
   switchport mode trunk phone
   switchport
!
interface Ethernet48
   description Phone port
   no shutdown
   switchport trunk native vlan 200
   switchport mode trunk phone
   switchport
```

### Port-Channel Interfaces

#### Port-Channel Interfaces Summary

##### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | LACP Fallback Timeout | LACP Fallback Mode | MLAG ID | EVPN ESI |
| --------- | ----------- | ---- | ----- | ----------- | ----------- | --------------------- | ------------------ | ------- | -------- |
| Port-Channel13 | L2_l2leaf1_Port-Channel11 | trunk | 101-102 | - | - | - | - | - | - |
| Port-Channel23 | L2_l2leaf2_Port-Channel21 | trunk | 101-102 | - | - | - | - | - | - |

#### Port-Channel Interfaces Device Configuration

```eos
!
interface Port-Channel13
   description L2_l2leaf1_Port-Channel11
   no shutdown
   switchport trunk allowed vlan 101-102
   switchport mode trunk
   switchport
!
interface Port-Channel23
   description L2_l2leaf2_Port-Channel21
   no shutdown
   switchport trunk allowed vlan 101-102
   switchport mode trunk
   switchport
```

### Loopback Interfaces

#### Loopback Interfaces Summary

##### IPv4

| Interface | Description | VRF | IP Address |
| --------- | ----------- | --- | ---------- |
| Loopback0 | ROUTER_ID | default | 10.1.0.1/32 |
| Loopback1 | VXLAN_TUNNEL_SOURCE | default | 10.2.0.1/32 |

##### IPv6

| Interface | Description | VRF | IPv6 Addresses |
| --------- | ----------- | --- | -------------- |
| Loopback0 | ROUTER_ID | default | - |
| Loopback1 | VXLAN_TUNNEL_SOURCE | default | - |

#### Loopback Interfaces Device Configuration

```eos
!
interface Loopback0
   description ROUTER_ID
   no shutdown
   ip address 10.1.0.1/32
!
interface Loopback1
   description VXLAN_TUNNEL_SOURCE
   no shutdown
   ip address 10.2.0.1/32
```

### VLAN Interfaces

#### VLAN Interfaces Summary

| Interface | Description | VRF | MTU | Shutdown |
| --------- | ----------- | --- | --- | -------- |
| Vlan101 | VLAN101 | VRF1 | - | True |
| Vlan102 | VLAN102 | VRF1 | - | True |

##### IPv4

| Interface | VRF | IP Address | IP Address Virtual | IP Router Virtual Address | ACL In | ACL Out |
| --------- | --- | ---------- | ------------------ | ------------------------- | ------ | ------- |
| Vlan101 | VRF1 | - | 10.1.1.1/24 | - | - | - |
| Vlan102 | VRF1 | - | 10.1.2.1/24 | - | - | - |

#### VLAN Interfaces Device Configuration

```eos
!
interface Vlan101
   description VLAN101
   shutdown
   vrf VRF1
   ip address virtual 10.1.1.1/24
!
interface Vlan102
   description VLAN102
   shutdown
   vrf VRF1
   ip address virtual 10.1.2.1/24
```

### VXLAN Interface

#### VXLAN Interface Summary

| Setting | Value |
| ------- | ----- |
| Source Interface | Loopback1 |
| UDP port | 4789 |

##### VLAN to VNI, Flood List and Multicast Group Mappings

| VLAN | VNI | Flood List | Multicast Group |
| ---- | --- | ---------- | --------------- |
| 101 | 10101 | - | - |
| 102 | 10102 | - | - |

##### VRF to VNI and Multicast Group Mappings

| VRF | VNI | Overlay Multicast Group to Encap Mappings |
| --- | --- | ----------------------------------------- |
| VRF1 | 1 | - |

#### VXLAN Interface Device Configuration

```eos
!
interface Vxlan1
   description l3leaf1_VTEP
   vxlan source-interface Loopback1
   vxlan udp-port 4789
   vxlan vlan 101 vni 10101
   vxlan vlan 102 vni 10102
   vxlan vrf VRF1 vni 1
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

Virtual Router MAC Address: 00:11:22:33:44:55

#### Virtual Router MAC Address Device Configuration

```eos
!
ip virtual-router mac-address 00:11:22:33:44:55
```

### IP Routing

#### IP Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | True |
| MGMT | False |
| VRF1 | True |

#### IP Routing Device Configuration

```eos
!
ip routing
no ip routing vrf MGMT
ip routing vrf VRF1
```

### IPv6 Routing

#### IPv6 Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | False |
| MGMT | false |
| VRF1 | false |

### Router BGP

ASN Notation: asdot

#### Router BGP Summary

| BGP AS | Router ID |
| ------ | --------- |
| 65000.1 | 10.1.0.1 |

| BGP Tuning |
| ---------- |
| update wait-install |
| no bgp default ipv4-unicast |
| maximum-paths 4 |

#### Router BGP Peer Groups

##### EVPN-OVERLAY-PEERS

| Settings | Value |
| -------- | ----- |
| Address Family | evpn |
| Source | Loopback0 |
| BFD | True |
| Ebgp multihop | 3 |
| Send community | all |
| Maximum routes | 0 (no limit) |

##### IPv4-UNDERLAY-PEERS

| Settings | Value |
| -------- | ----- |
| Address Family | ipv4 |
| Send community | all |
| Maximum routes | 256000 |

#### BGP Neighbors

| Neighbor | Remote AS | VRF | Shutdown | Send-community | Maximum-routes | Allowas-in | BFD | RIB Pre-Policy Retain | Route-Reflector Client | Passive | TTL Max Hops |
| -------- | --------- | --- | -------- | -------------- | -------------- | ---------- | --- | --------------------- | ---------------------- | ------- | ------------ |
| 10.0.0.1 | 65000.0 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 10.0.0.2 | 65000.0 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 10.4.0.0 | 65000.0 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - | - |
| 10.4.0.2 | 65000.0 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - | - |

#### Router BGP EVPN Address Family

##### EVPN Peer Groups

| Peer Group | Activate | Route-map In | Route-map Out | Peer-tag In | Peer-tag Out | Encapsulation | Next-hop-self Source Interface |
| ---------- | -------- | ------------ | ------------- | ----------- | ------------ | ------------- | ------------------------------ |
| EVPN-OVERLAY-PEERS | True | - | - | - | - | default | - |

#### Router BGP VLANs

| VLAN | Route-Distinguisher | Both Route-Target | Import Route Target | Export Route-Target | Redistribute |
| ---- | ------------------- | ----------------- | ------------------- | ------------------- | ------------ |
| 101 | 10.1.0.1:10101 | 10101:10101 | - | - | learned |
| 102 | 10.1.0.1:10102 | 10102:10102 | - | - | learned |

#### Router BGP VRFs

| VRF | Route-Distinguisher | Redistribute | Graceful Restart |
| --- | ------------------- | ------------ | ---------------- |
| VRF1 | 10.1.0.1:1 | connected | - |

#### Router BGP Device Configuration

```eos
!
router bgp 65000.1
   bgp asn notation asdot
   router-id 10.1.0.1
   update wait-install
   no bgp default ipv4-unicast
   maximum-paths 4
   neighbor EVPN-OVERLAY-PEERS peer group
   neighbor EVPN-OVERLAY-PEERS update-source Loopback0
   neighbor EVPN-OVERLAY-PEERS bfd
   neighbor EVPN-OVERLAY-PEERS ebgp-multihop 3
   neighbor EVPN-OVERLAY-PEERS send-community
   neighbor EVPN-OVERLAY-PEERS maximum-routes 0
   neighbor IPv4-UNDERLAY-PEERS peer group
   neighbor IPv4-UNDERLAY-PEERS send-community
   neighbor IPv4-UNDERLAY-PEERS maximum-routes 256000
   neighbor 10.0.0.1 peer group EVPN-OVERLAY-PEERS
   neighbor 10.0.0.1 remote-as 65000.0
   neighbor 10.0.0.1 description spine1_Loopback0
   neighbor 10.0.0.2 peer group EVPN-OVERLAY-PEERS
   neighbor 10.0.0.2 remote-as 65000.0
   neighbor 10.0.0.2 description spine2_Loopback0
   neighbor 10.4.0.0 peer group IPv4-UNDERLAY-PEERS
   neighbor 10.4.0.0 remote-as 65000.0
   neighbor 10.4.0.0 description spine1_Ethernet1/3
   neighbor 10.4.0.2 peer group IPv4-UNDERLAY-PEERS
   neighbor 10.4.0.2 remote-as 65000.0
   neighbor 10.4.0.2 description spine2_Ethernet1/4
   redistribute connected route-map RM-CONN-2-BGP
   !
   vlan 101
      rd 10.1.0.1:10101
      route-target both 10101:10101
      redistribute learned
   !
   vlan 102
      rd 10.1.0.1:10102
      route-target both 10102:10102
      redistribute learned
   !
   address-family evpn
      neighbor EVPN-OVERLAY-PEERS activate
   !
   address-family ipv4
      no neighbor EVPN-OVERLAY-PEERS activate
      neighbor IPv4-UNDERLAY-PEERS activate
   !
   vrf VRF1
      rd 10.1.0.1:1
      route-target import evpn 1:1
      route-target export evpn 1:1
      router-id 10.1.0.1
      redistribute connected
```

## BFD

### Router BFD

#### Router BFD Multihop Summary

| Interval | Minimum RX | Multiplier |
| -------- | ---------- | ---------- |
| 300 | 300 | 3 |

#### Router BFD Device Configuration

```eos
!
router bfd
   multihop interval 300 min-rx 300 multiplier 3
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

##### PL-LOOPBACKS-EVPN-OVERLAY

| Sequence | Action |
| -------- | ------ |
| 10 | permit 10.1.0.0/16 eq 32 |
| 20 | permit 10.2.0.0/16 eq 32 |

#### Prefix-lists Device Configuration

```eos
!
ip prefix-list PL-LOOPBACKS-EVPN-OVERLAY
   seq 10 permit 10.1.0.0/16 eq 32
   seq 20 permit 10.2.0.0/16 eq 32
```

### Route-maps

#### Route-maps Summary

##### RM-CONN-2-BGP

| Sequence | Type | Match | Set | Sub-Route-Map | Continue |
| -------- | ---- | ----- | --- | ------------- | -------- |
| 10 | permit | ip address prefix-list PL-LOOPBACKS-EVPN-OVERLAY | - | - | - |

#### Route-maps Device Configuration

```eos
!
route-map RM-CONN-2-BGP permit 10
   match ip address prefix-list PL-LOOPBACKS-EVPN-OVERLAY
```

## VRF Instances

### VRF Instances Summary

| VRF Name | IP Routing |
| -------- | ---------- |
| MGMT | disabled |
| VRF1 | enabled |

### VRF Instances Device Configuration

```eos
!
vrf instance MGMT
!
vrf instance VRF1
```
