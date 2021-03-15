# DC1-POD1-LEAF2B

# Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
  - [DNS Domain](#dns-domain)
  - [Name Servers](#name-servers)
  - [Domain Lookup](#domain-lookup)
  - [NTP](#ntp)
  - [Management SSH](#management-ssh)
  - [Management GNMI](#management-api-gnmi)
  - [Management API](#Management-api-http)
- [Authentication](#authentication)
  - [Local Users](#local-users)
  - [Enable Password](#enable-password)
  - [TACACS Servers](#tacacs-servers)
  - [IP TACACS Source Interfaces](#ip-tacacs-source-interfaces)
  - [RADIUS Servers](#radius-servers)
  - [AAA Server Groups](#aaa-server-groups)
  - [AAA Authentication](#aaa-authentication)
  - [AAA Authorization](#aaa-authorization)
  - [AAA Accounting](#aaa-accounting)
- [Management Security](#management-security)
- [Prompt](#prompt)
- [Aliases](#aliases)
- [Monitoring](#monitoring)
  - [TerminAttr Daemon](#terminattr-daemon)
  - [Logging](#logging)
  - [SNMP](#snmp)
  - [SFlow](#sflow)
  - [Hardware Counters](#hardware-counters)
  - [VM Tracer Sessions](#vm-tracer-sessions)
  - [Event Handler](#event-handler)
- [MLAG](#mlag)
- [Spanning Tree](#spanning-tree)
- [Internal VLAN Allocation Policy](#internal-vlan-allocation-policy)
- [VLANs](#vlans)
- [Interfaces](#interfaces)
  - [Switchport Default](#switchport-default)
  - [Interface Defaults](#interface-defaults)
  - [Ethernet Interfaces](#ethernet-interfaces)
  - [Port-Channel Interfaces](#port-channel-interfaces)
  - [Loopback Interfaces](#loopback-interfaces)
  - [VLAN Interfaces](#vlan-interfaces)
  - [VXLAN Interface](#vxlan-interface)
- [Routing](#routing)
  - [Virtual Router MAC Address](#virtual-router-mac-address)
  - [IP Routing](#ip-routing)
  - [IPv6 Routing](#ipv6-routing)
  - [Static Routes](#static-routes)
  - [IPv6 Static Routes](#ipv6-static-routes)
  - [Router General](#router-general)
  - [Router OSPF](#router-ospf)
  - [Router ISIS](#router-isis)
  - [Router BGP](#router-bgp)
  - [Router BFD](#router-bfd)
- [Multicast](#multicast)
  - [IP IGMP Snooping](#ip-igmp-snooping)
  - [Router Multicast](#router-multicast)
  - [Router PIM Sparse Mode](#router-pim-sparse-mode)
- [Filters](#filters)
  - [Community-lists](#community-lists)
  - [Peer Filters](#peer-filters)
  - [Prefix-lists](#prefix-lists)
  - [IPv6 Prefix-lists](#ipv6-prefix-lists)
  - [Route-maps](#route-maps)
  - [IP Extended Communities](#ip-extended-communities)
- [ACL](#acl)
  - [Standard Access-lists](#standard-access-lists)
  - [Extended Access-lists](#extended-access-lists)
  - [IPv6 Standard Access-lists](#ipv6-standard-access-lists)
  - [IPv6 Extended Access-lists](#ipv6-extended-access-lists)
- [VRF Instances](#vrf-instances)
- [Virtual Source NAT](#virtual-source-nat)
- [Platform](#platform)
- [Router L2 VPN](#router-l2-vpn)
- [IP DHCP Relay](#ip-dhcp-relay)
- [Errdisable](#errdisable)
- [MAC security](#mac-security)
- [QOS](#qos)
- [QOS Profiles](#qos-profiles)

# Management

## Management Interfaces

### Management Interfaces Summary

#### IPv4

| Management Interface | description | Type | VRF | IP Address | Gateway |
| -------------------- | ----------- | ---- | --- | ---------- | ------- |
| Management1 | oob_management | oob | MGMT | 192.168.1.9/16 | 192.168.1.254 |

#### IPv6

| Management Interface | description | Type | VRF | IPv6 Address | IPv6 Gateway |
| -------------------- | ----------- | ---- | --- | ------------ | ------------ |
| Management1 | oob_management | oob | MGMT | -  | - |

### Management Interfaces Device Configuration

```eos
!
interface Management1
   description oob_management
   no shutdown
   vrf MGMT
   ip address 192.168.1.9/16
```

## DNS Domain

DNS domain not defined

## Domain-list

Domain-list not defined

## Name Servers

No name servers defined

## Domain Lookup

DNS domain lookup not defined

## NTP

No NTP servers defined

## PTP

PTP is not defined.

## Management SSH

Management SSH not defined

## Management API GNMI

Management API gnmi is not defined

## Management API HTTP

### Management API HTTP Summary

| HTTP | HTTPS |
| ---------- | ---------- |
| default | true |

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

## Enable Password

Enable password not defined

## TACACS Servers

TACACS servers not defined

## IP TACACS Source Interfaces

IP TACACS source interfaces not defined

## RADIUS Servers

RADIUS servers not defined

## AAA Server Groups

AAA server groups not defined

## AAA Authentication

AAA authentication not defined

## AAA Authorization

AAA authorization not defined

## AAA Accounting

AAA accounting not defined

# Management Security

Management security not defined

# Prompt

Prompt not defined

# Aliases

Aliases not defined

# Monitoring

## TerminAttr Daemon

TerminAttr daemon not defined

## Logging

No logging settings defined

## SNMP

No SNMP settings defined

## SFlow

No sFlow defined

## Hardware Counters

No hardware counters defined

## VM Tracer Sessions

No VM tracer sessions defined

## Event Handler

No event handler defined

# MLAG

## MLAG Summary

| Domain-id | Local-interface | Peer-address | Peer-link |
| --------- | --------------- | ------------ | --------- |
| RACK2_MLAG | Vlan4094 | 172.19.110.2 | Port-Channel5 |

Dual primary detection is enabled. The detection delay is 5 seconds.

## MLAG Device Configuration

```eos
!
mlag configuration
   domain-id RACK2_MLAG
   local-interface Vlan4094
   peer-address 172.19.110.2
   peer-address heartbeat 192.168.1.8 vrf MGMT
   peer-link Port-Channel5
   dual-primary detection delay 5 action errdisable all-interfaces
   reload-delay mlag 300
   reload-delay non-mlag 330
```

# Spanning Tree

## Spanning Tree Summary

STP Root Super: **True**

STP mode: **mstp**

### MSTP Instance and Priority

| Instance(s) | Priority |
| -------- | -------- |
| 0 | 4096 |

### Global Spanning-Tree Settings

Spanning Tree disabled for VLANs: **4093-4094**

## Spanning Tree Device Configuration

```eos
!
spanning-tree root super
spanning-tree mode mstp
no spanning-tree vlan-id 4093-4094
spanning-tree mst 0 priority 4096
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
| 110 | Tenant_A_OP_Zone_1 | none  |
| 111 | Tenant_A_OP_Zone_2 | none  |
| 112 | Tenant_A_OP_Zone_3 | none  |
| 4085 | L2LEAF_INBAND_MGMT | none  |
| 4093 | LEAF_PEER_L3 | LEAF_PEER_L3  |
| 4094 | MLAG_PEER | MLAG  |

## VLANs Device Configuration

```eos
!
vlan 110
   name Tenant_A_OP_Zone_1
!
vlan 111
   name Tenant_A_OP_Zone_2
!
vlan 112
   name Tenant_A_OP_Zone_3
!
vlan 4085
   name L2LEAF_INBAND_MGMT
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

## Switchport Default

No switchport default defined

## Interface Defaults

No Interface Defaults defined

## Ethernet Interfaces

### Ethernet Interfaces Summary

#### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | Channel-Group |
| --------- | ----------- | ---- | ----- | ----------- | ----------- | ------------- |
| Ethernet3 | DC1-POD1-L2LEAF2A_Ethernet2 | *trunk | *110-112,4085 | *- | *- | 3 |
| Ethernet4 | DC1-POD1-L2LEAF2B_Ethernet2 | *trunk | *110-112,4085 | *- | *- | 3 |
| Ethernet5 | MLAG_PEER_DC1-POD1-LEAF2A_Ethernet5 | *trunk | *2-4094 | *- | *['LEAF_PEER_L3', 'MLAG'] | 5 |
| Ethernet6 | MLAG_PEER_DC1-POD1-LEAF2A_Ethernet6 | *trunk | *2-4094 | *- | *['LEAF_PEER_L3', 'MLAG'] | 5 |

*Inherited from Port-Channel Interface

#### IPv4

| Interface | Description | Type | Channel Group | IP Address | VRF |  MTU | Shutdown | ACL In | ACL Out |
| --------- | ----------- | -----| ------------- | ---------- | ----| ---- | -------- | ------ | ------- |
| Ethernet1 |  P2P_LINK_TO_DC1-POD1-SPINE1_Ethernet5  |  routed  | - |  172.17.110.9/31  |  default  |  1500  |  false  |  -  |  -  |
| Ethernet2 |  P2P_LINK_TO_DC1-POD1-SPINE2_Ethernet5  |  routed  | - |  172.17.110.11/31  |  default  |  1500  |  false  |  -  |  -  |
| Ethernet7 |  P2P_LINK_TO_DC2-POD1-LEAF1A_Ethernet7  |  routed  | - |  11.1.0.38/31  |  default  |  1499  |  false  |  -  |  -  |

### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet1
   description P2P_LINK_TO_DC1-POD1-SPINE1_Ethernet5
   no shutdown
   mtu 1500
   no switchport
   ip address 172.17.110.9/31
   ptp enable
   service-profile QOS-PROFILE
!
interface Ethernet2
   description P2P_LINK_TO_DC1-POD1-SPINE2_Ethernet5
   no shutdown
   mtu 1500
   no switchport
   ip address 172.17.110.11/31
   ptp enable
   service-profile QOS-PROFILE
!
interface Ethernet3
   description DC1-POD1-L2LEAF2A_Ethernet2
   no shutdown
   channel-group 3 mode active
!
interface Ethernet4
   description DC1-POD1-L2LEAF2B_Ethernet2
   no shutdown
   channel-group 3 mode active
!
interface Ethernet5
   description MLAG_PEER_DC1-POD1-LEAF2A_Ethernet5
   no shutdown
   channel-group 5 mode active
!
interface Ethernet6
   description MLAG_PEER_DC1-POD1-LEAF2A_Ethernet6
   no shutdown
   channel-group 5 mode active
!
interface Ethernet7
   description P2P_LINK_TO_DC2-POD1-LEAF1A_Ethernet7
   no shutdown
   mtu 1499
   no switchport
   ip address 11.1.0.38/31
   ptp enable
```

## Port-Channel Interfaces

### Port-Channel Interfaces Summary

#### L2

| Interface | Description | Type | Mode | VLANs | Native VLAN | Trunk Group | LACP Fallback Timeout | LACP Fallback Mode | MLAG ID | EVPN ESI |
| --------- | ----------- | ---- | ---- | ----- | ----------- | ------------| --------------------- | ------------------ | ------- | -------- |
| Port-Channel3 | RACK2_MLAG_Po1 | switched | trunk | 110-112,4085 | - | - | - | - | 3 | - |
| Port-Channel5 | MLAG_PEER_DC1-POD1-LEAF2A_Po5 | switched | trunk | 2-4094 | - | ['LEAF_PEER_L3', 'MLAG'] | - | - | - | - |

### Port-Channel Interfaces Device Configuration

```eos
!
interface Port-Channel3
   description RACK2_MLAG_Po1
   no shutdown
   switchport
   switchport trunk allowed vlan 110-112,4085
   switchport mode trunk
   mlag 3
   service-profile QOS-PROFILE
!
interface Port-Channel5
   description MLAG_PEER_DC1-POD1-LEAF2A_Po5
   no shutdown
   switchport
   switchport trunk allowed vlan 2-4094
   switchport mode trunk
   switchport trunk group LEAF_PEER_L3
   switchport trunk group MLAG
   service-profile QOS-PROFILE
```

## Loopback Interfaces

### Loopback Interfaces Summary

#### IPv4

| Interface | Description | VRF | IP Address |
| --------- | ----------- | --- | ---------- |
| Loopback0 | EVPN_Overlay_Peering | default | 172.16.110.5/32 |
| Loopback1 | VTEP_VXLAN_Tunnel_Source | default | 172.18.110.4/32 |

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
   ip address 172.16.110.5/32
!
interface Loopback1
   description VTEP_VXLAN_Tunnel_Source
   no shutdown
   ip address 172.18.110.4/32
```

## VLAN Interfaces

### VLAN Interfaces Summary

| Interface | Description | VRF |  MTU | Shutdown |
| --------- | ----------- | --- | ---- | -------- |
| Vlan110 |  Tenant_A_OP_Zone_1  |  Common_VRF  |  -  |  false  |
| Vlan111 |  Tenant_A_OP_Zone_2  |  Common_VRF  |  -  |  true  |
| Vlan112 |  Tenant_A_OP_Zone_3  |  Common_VRF  |  -  |  false  |
| Vlan4085 |  L2LEAF_INBAND_MGMT  |  default  |  1500  |  false  |
| Vlan4093 |  MLAG_PEER_L3_PEERING  |  default  |  1500  |  false  |
| Vlan4094 |  MLAG_PEER  |  default  |  1500  |  false  |

#### IPv4

| Interface | VRF | IP Address | IP Address Virtual | IP Router Virtual Address | VRRP | ACL In | ACL Out |
| --------- | --- | ---------- | ------------------ | ------------------------- | ---- | ------ | ------- |
| Vlan110 |  Common_VRF  |  -  |  10.1.10.1/24  |  -  |  -  |  -  |  -  |
| Vlan111 |  Common_VRF  |  -  |  10.1.11.1/24  |  -  |  -  |  -  |  -  |
| Vlan112 |  Common_VRF  |  -  |  10.1.12.1/24  |  -  |  -  |  -  |  -  |
| Vlan4085 |  default  |  172.21.110.3/24  |  -  |  172.21.110.1  |  -  |  -  |  -  |
| Vlan4093 |  default  |  172.20.110.3/31  |  -  |  -  |  -  |  -  |  -  |
| Vlan4094 |  default  |  172.19.110.3/31  |  -  |  -  |  -  |  -  |  -  |



### VLAN Interfaces Device Configuration

```eos
!
interface Vlan110
   description Tenant_A_OP_Zone_1
   no shutdown
   vrf Common_VRF
   ip address virtual 10.1.10.1/24
!
interface Vlan111
   description Tenant_A_OP_Zone_2
   shutdown
   vrf Common_VRF
   ip address virtual 10.1.11.1/24
!
interface Vlan112
   description Tenant_A_OP_Zone_3
   no shutdown
   vrf Common_VRF
   ip address virtual 10.1.12.1/24
!
interface Vlan4085
   description L2LEAF_INBAND_MGMT
   no shutdown
   mtu 1500
   ip address 172.21.110.3/24
   ip virtual-router address 172.21.110.1
   ip attached-host route export 19
!
interface Vlan4093
   description MLAG_PEER_L3_PEERING
   no shutdown
   mtu 1500
   ip address 172.20.110.3/31
!
interface Vlan4094
   description MLAG_PEER
   no shutdown
   mtu 1500
   no autostate
   ip address 172.19.110.3/31
```

## VXLAN Interface

### VXLAN Interface Summary

#### Source Interface: Loopback1

#### UDP port: 4789

#### VLAN to VNI Mappings

| VLAN | VNI |
| ---- | --- |
| 110 | 10110 |
| 111 | 50111 |
| 112 | 50112 |

#### VRF to VNI Mappings

| VLAN | VNI |
| ---- | --- |
| Common_VRF | 1025 |

### VXLAN Interface Device Configuration

```eos
!
interface Vxlan1
   vxlan source-interface Loopback1
   vxlan virtual-router encapsulation mac-address mlag-system-id
   vxlan udp-port 4789
   vxlan vlan 110 vni 10110
   vxlan vlan 111 vni 50111
   vxlan vlan 112 vni 50112
   vxlan vrf Common_VRF vni 1025
```

# Routing

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
| default | true|| Common_VRF | true |
| MGMT | false |

### IP Routing Device Configuration

```eos
!
ip routing
ip routing vrf Common_VRF
no ip routing vrf MGMT
```

## IPv6 Routing

### IPv6 Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | false || Common_VRF | false |
| MGMT | false |


## Static Routes

### Static Routes Summary

| VRF | Destination Prefix | Next Hop IP             | Exit interface      | Administrative Distance       | Tag               | Route Name                    | Metric         |
| --- | ------------------ | ----------------------- | ------------------- | ----------------------------- | ----------------- | ----------------------------- | -------------- |
| MGMT  | 0.0.0.0/0 |  192.168.1.254  |  -  |  1  |  -  |  -  |  - |

### Static Routes Device Configuration

```eos
!
ip route vrf MGMT 0.0.0.0/0 192.168.1.254
```

## IPv6 Static Routes

IPv6 static routes not defined

## ARP

Global ARP timeout not defined.

## Router General

Router general not defined

## Router OSPF

Router OSPF not defined

## Router ISIS

Router ISIS not defined

## Router BGP

### Router BGP Summary

| BGP AS | Router ID |
| ------ | --------- |
| 65112|  172.16.110.5 |

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
| Source | Loopback0 |
| Bfd | true |
| Ebgp multihop | 5 |
| Send community | true |
| Maximum routes | 0 (no limit) |

#### IPv4-UNDERLAY-PEERS

| Settings | Value |
| -------- | ----- |
| Address Family | ipv4 |
| Remote_as | 65110 |
| Send community | true |
| Maximum routes | 12000 |

#### MLAG-IPv4-UNDERLAY-PEER

| Settings | Value |
| -------- | ----- |
| Address Family | ipv4 |
| Remote_as | 65112 |
| Next-hop self | True |
| Send community | true |
| Maximum routes | 12000 |

### BGP Neighbors

| Neighbor | Remote AS | VRF |
| -------- | --------- | --- |
| 11.1.0.39 | 65211 | default |
| 172.16.10.1 | 65101 | default |
| 172.16.110.1 | 65110 | default |
| 172.16.110.3 | 65111 | default |
| 172.17.110.8 | Inherited from peer group IPv4-UNDERLAY-PEERS | default |
| 172.17.110.10 | Inherited from peer group IPv4-UNDERLAY-PEERS | default |
| 172.20.110.2 | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | default |

### Router BGP EVPN Address Family

#### Router BGP EVPN MAC-VRFs

##### VLAN Based

| VLAN | Route-Distinguisher | Both Route-Target | Import Route Target | Export Route-Target | Redistribute |
| ---- | ------------------- | ----------------- | ------------------- | ------------------- | ------------ |
| 110 | 172.16.110.5:10110 |  10110:10110 |  -  | -  | learned |
| 111 | 172.16.110.5:50111 |  50111:50111 |  -  | -  | learned |
| 112 | 172.16.110.5:50112 |  50112:50112 |  -  | -  | learned |

#### Router BGP EVPN VRFs

| VRF | Route-Distinguisher | Redistribute |
| --- | ------------------- | ------------ |
| Common_VRF | 172.16.110.5:1025 | connected |

### Router BGP Device Configuration

```eos
!
router bgp 65112
   router-id 172.16.110.5
   no bgp default ipv4-unicast
   distance bgp 20 200 200
   graceful-restart restart-time 300
   graceful-restart
   maximum-paths 4 ecmp 4
   neighbor EVPN-OVERLAY-PEERS peer group
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
   neighbor MLAG-IPv4-UNDERLAY-PEER peer group
   neighbor MLAG-IPv4-UNDERLAY-PEER remote-as 65112
   neighbor MLAG-IPv4-UNDERLAY-PEER next-hop-self
   neighbor MLAG-IPv4-UNDERLAY-PEER password 7 vnEaG8gMeQf3d3cN6PktXQ==
   neighbor MLAG-IPv4-UNDERLAY-PEER send-community
   neighbor MLAG-IPv4-UNDERLAY-PEER maximum-routes 12000
   neighbor MLAG-IPv4-UNDERLAY-PEER route-map RM-MLAG-PEER-IN in
   neighbor 11.1.0.39 peer group IPv4-UNDERLAY-PEERS
   neighbor 11.1.0.39 remote-as 65211
   neighbor 11.1.0.39 local-as 65120 no-prepend replace-as
   neighbor 11.1.0.39 description DC2-POD1-LEAF1A
   neighbor 11.1.0.39 bfd
   neighbor 172.16.10.1 peer group EVPN-OVERLAY-PEERS
   neighbor 172.16.10.1 remote-as 65101
   neighbor 172.16.10.1 description DC1-RS1
   neighbor 172.16.10.1 route-map RM-EVPN-FILTER-AS65101 out
   neighbor 172.16.110.1 peer group EVPN-OVERLAY-PEERS
   neighbor 172.16.110.1 remote-as 65110
   neighbor 172.16.110.1 description DC1-POD1-SPINE1
   neighbor 172.16.110.1 route-map RM-EVPN-FILTER-AS65110 out
   neighbor 172.16.110.3 peer group EVPN-OVERLAY-PEERS
   neighbor 172.16.110.3 remote-as 65111
   neighbor 172.16.110.3 description DC1-POD1-LEAF1A
   neighbor 172.16.110.3 route-map RM-EVPN-FILTER-AS65111 out
   neighbor 172.17.110.8 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.110.10 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.20.110.2 peer group MLAG-IPv4-UNDERLAY-PEER
   redistribute attached-host
   redistribute connected route-map RM-CONN-2-BGP
   !
   vlan 110
      rd 172.16.110.5:10110
      route-target both 10110:10110
      redistribute learned
   !
   vlan 111
      rd 172.16.110.5:50111
      route-target both 50111:50111
      redistribute learned
   !
   vlan 112
      rd 172.16.110.5:50112
      route-target both 50112:50112
      redistribute learned
   !
   address-family evpn
      neighbor EVPN-OVERLAY-PEERS activate
   !
   address-family rt-membership
      neighbor EVPN-OVERLAY-PEERS activate
   !
   address-family ipv4
      no neighbor EVPN-OVERLAY-PEERS activate
      neighbor IPv4-UNDERLAY-PEERS activate
      neighbor MLAG-IPv4-UNDERLAY-PEER activate
   !
   vrf Common_VRF
      rd 172.16.110.5:1025
      route-target import evpn 1025:1025
      route-target export evpn 1025:1025
      router-id 172.16.110.5
      redistribute connected
```

## Router BFD

### Router BFD Multihop Summary

| Interval | Minimum RX | Multiplier |
| -------- | ---------- | ---------- |
| 300 | 300 | 3 |

*No device configuration required - default values

# Multicast

## IP IGMP Snooping

### IP IGMP Snooping Summary

IGMP snooping is globally enabled.


### IP IGMP Snooping Device Configuration

```eos
```


## Router Multicast

Routing multicast not defined

## Router PIM Sparse Mode

Router PIM sparse mode not defined

# Filters

## Community-lists

Community-lists not defined

## Peer Filters

No peer filters defined

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

## IPv6 Prefix-lists

IPv6 prefix-lists not defined

## Route-maps

### Route-maps Summary

#### RM-CONN-2-BGP

| Sequence | Type | Match and/or Set |
| -------- | ---- | ---------------- |
| 10 | permit | match ip address prefix-list PL-LOOPBACKS-EVPN-OVERLAY |
| 20 | permit | match ip address prefix-list PL-L2LEAF-INBAND-MGMT |

#### RM-EVPN-FILTER-AS65101

| Sequence | Type | Match and/or Set |
| -------- | ---- | ---------------- |
| 10 | deny | match as 65101 |

#### RM-EVPN-FILTER-AS65110

| Sequence | Type | Match and/or Set |
| -------- | ---- | ---------------- |
| 10 | deny | match as 65110 |

#### RM-EVPN-FILTER-AS65111

| Sequence | Type | Match and/or Set |
| -------- | ---- | ---------------- |
| 10 | deny | match as 65111 |

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
route-map RM-CONN-2-BGP permit 20
   match ip address prefix-list PL-L2LEAF-INBAND-MGMT
!
route-map RM-EVPN-FILTER-AS65101 deny 10
   match as 65101
!
route-map RM-EVPN-FILTER-AS65101 permit 20
!
route-map RM-EVPN-FILTER-AS65110 deny 10
   match as 65110
!
route-map RM-EVPN-FILTER-AS65110 permit 20
!
route-map RM-EVPN-FILTER-AS65111 deny 10
   match as 65111
!
route-map RM-EVPN-FILTER-AS65111 permit 20
!
route-map RM-MLAG-PEER-IN permit 10
   description Make routes learned over MLAG Peer-link less preferred on spines to ensure optimal routing
   set origin incomplete
```

## IP Extended Communities

No extended community defined

# ACL

## Standard Access-lists

Standard access-lists not defined

## Extended Access-lists

Extended access-lists not defined

## IPv6 Standard Access-lists

IPv6 standard access-lists not defined

## IPv6 Extended Access-lists

IPv6 extended access-lists not defined

# VRF Instances

## VRF Instances Summary

| VRF Name | IP Routing |
| -------- | ---------- |
| Common_VRF | enabled |
| MGMT | disabled |

## VRF Instances Device Configuration

```eos
!
vrf instance Common_VRF
!
vrf instance MGMT
```

# Virtual Source NAT

Virtual source NAT not defined

# Platform

No platform parameters defined

# Router L2 VPN

Router L2 VPN not defined

# IP DHCP Relay

IP DHCP relay not defined

# Errdisable

Errdisable is not defined.

# MACsec

MACsec not defined

# QOS

QOS is not defined.

# QOS Profiles

QOS Profiles are not defined

# Custom Templates

No custom templates defined
