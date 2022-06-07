# DC1-POD1-LEAF2A
# Table of Contents

- [Management](#management)
  - [Management API HTTP](#management-api-http)
- [Authentication](#authentication)
  - [Local Users](#local-users)
- [Monitoring](#monitoring)
  - [SNMP](#snmp)
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
| - | TWODC_5STAGE_CLOS DC1 DC1_POD1 DC1-POD1-LEAF2A | All | Disabled |

### SNMP Device Configuration

```eos
!
snmp-server location TWODC_5STAGE_CLOS DC1 DC1_POD1 DC1-POD1-LEAF2A
```

# MLAG

## MLAG Summary

| Domain-id | Local-interface | Peer-address | Peer-link |
| --------- | --------------- | ------------ | --------- |
| RACK2_MLAG | Vlan4094 | 172.19.110.3 | Port-Channel5 |

Dual primary detection is enabled. The detection delay is 5 seconds.

## MLAG Device Configuration

```eos
!
mlag configuration
   domain-id RACK2_MLAG
   local-interface Vlan4094
   peer-address 172.19.110.3
   peer-address heartbeat 192.168.1.9 vrf MGMT
   peer-link Port-Channel5
   dual-primary detection delay 5 action errdisable all-interfaces
   reload-delay mlag 300
   reload-delay non-mlag 330
```

# Spanning Tree

## Spanning Tree Summary

STP mode: **mstp**

### MSTP Instance and Priority

| Instance(s) | Priority |
| -------- | -------- |
| 0 | 4096 |

### Global Spanning-Tree Settings

- Spanning Tree disabled for VLANs: **4093-4094**

## Spanning Tree Device Configuration

```eos
!
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
| 110 | Tenant_A_OP_Zone_1 | - |
| 111 | Tenant_A_OP_Zone_2 | - |
| 112 | Tenant_A_OP_Zone_3 | - |
| 2500 | web-l2-vlan | - |
| 2600 | web-l2-vlan-2 | - |
| 4085 | L2LEAF_INBAND_MGMT | - |
| 4093 | LEAF_PEER_L3 | LEAF_PEER_L3 |
| 4094 | MLAG_PEER | MLAG |

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
vlan 2500
   name web-l2-vlan
!
vlan 2600
   name web-l2-vlan-2
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

## Ethernet Interfaces

### Ethernet Interfaces Summary

#### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | Channel-Group |
| --------- | ----------- | ---- | ----- | ----------- | ----------- | ------------- |
| Ethernet3 | DC1-POD1-L2LEAF2A_Ethernet1 | *trunk | *110-112,2500,2600,4085 | *- | *- | 3 |
| Ethernet4 | DC1-POD1-L2LEAF2B_Ethernet1 | *trunk | *110-112,2500,2600,4085 | *- | *- | 3 |
| Ethernet5 | MLAG_PEER_DC1-POD1-LEAF2B_Ethernet5 | *trunk | *2-4094 | *- | *['LEAF_PEER_L3', 'MLAG'] | 5 |
| Ethernet6 | MLAG_PEER_DC1-POD1-LEAF2B_Ethernet6 | *trunk | *2-4094 | *- | *['LEAF_PEER_L3', 'MLAG'] | 5 |
| Ethernet16 | server-1_Eth1 | *access | *110 | *- | *- | 16 |
| Ethernet17 | server-1_Eth3 | *access | *110 | *- | *- | 17 |
| Ethernet18 | server-1_Eth5 | *access | *110 | *- | *- | 18 |
| Ethernet19 | server-1_Eth7 | *access | *110 | *- | *- | 19 |

*Inherited from Port-Channel Interface

#### IPv4

| Interface | Description | Type | Channel Group | IP Address | VRF |  MTU | Shutdown | ACL In | ACL Out |
| --------- | ----------- | -----| ------------- | ---------- | ----| ---- | -------- | ------ | ------- |
| Ethernet1 | P2P_LINK_TO_DC1-POD1-SPINE1_Ethernet4 | routed | - | 172.17.110.5/31 | default | 1500 | false | - | - |
| Ethernet2 | P2P_LINK_TO_DC1-POD1-SPINE2_Ethernet4 | routed | - | 172.17.110.7/31 | default | 1500 | false | - | - |
| Ethernet7 | P2P_LINK_TO_DC2-POD1-LEAF1A_Ethernet6 | routed | - | 100.100.100.101/24 | default | 1500 | false | - | - |

### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet1
   description P2P_LINK_TO_DC1-POD1-SPINE1_Ethernet4
   no shutdown
   mtu 1500
   no switchport
   ip address 172.17.110.5/31
   ptp enable
   service-profile QOS-PROFILE
!
interface Ethernet2
   description P2P_LINK_TO_DC1-POD1-SPINE2_Ethernet4
   no shutdown
   mtu 1500
   no switchport
   ip address 172.17.110.7/31
   ptp enable
   service-profile QOS-PROFILE
!
interface Ethernet3
   description DC1-POD1-L2LEAF2A_Ethernet1
   no shutdown
   channel-group 3 mode active
!
interface Ethernet4
   description DC1-POD1-L2LEAF2B_Ethernet1
   no shutdown
   channel-group 3 mode active
!
interface Ethernet5
   description MLAG_PEER_DC1-POD1-LEAF2B_Ethernet5
   no shutdown
   channel-group 5 mode active
!
interface Ethernet6
   description MLAG_PEER_DC1-POD1-LEAF2B_Ethernet6
   no shutdown
   channel-group 5 mode active
!
interface Ethernet7
   description P2P_LINK_TO_DC2-POD1-LEAF1A_Ethernet6
   no shutdown
   mtu 1500
   no switchport
   ip address 100.100.100.101/24
!
interface Ethernet16
   description server-1_Eth1
   no shutdown
   channel-group 16 mode active
   comment
   Comment created from raw_eos_cli under profile TENANT_A
   EOF

!
interface Ethernet17
   description server-1_Eth3
   no shutdown
   channel-group 17 mode active
   comment
   Comment created from raw_eos_cli under adapter for switch Eth17
   EOF

!
interface Ethernet18
   description server-1_Eth5
   no shutdown
   channel-group 18 mode active
   comment
   Comment created from raw_eos_cli under profile NESTED_TENANT_A
   EOF

!
interface Ethernet19
   description server-1_Eth7
   no shutdown
   channel-group 19 mode active
   comment
   Comment created from raw_eos_cli under profile NESTED_TENANT_A
   EOF

```

## Port-Channel Interfaces

### Port-Channel Interfaces Summary

#### L2

| Interface | Description | Type | Mode | VLANs | Native VLAN | Trunk Group | LACP Fallback Timeout | LACP Fallback Mode | MLAG ID | EVPN ESI |
| --------- | ----------- | ---- | ---- | ----- | ----------- | ------------| --------------------- | ------------------ | ------- | -------- |
| Port-Channel3 | RACK2_MLAG_Po1 | switched | trunk | 110-112,2500,2600,4085 | - | - | - | - | 3 | - |
| Port-Channel5 | MLAG_PEER_DC1-POD1-LEAF2B_Po5 | switched | trunk | 2-4094 | - | ['LEAF_PEER_L3', 'MLAG'] | - | - | - | - |
| Port-Channel16 | server-1_PortChannel | switched | access | 110 | - | - | - | - | 16 | - |
| Port-Channel17 | server-1_PortChannel | switched | access | 110 | - | - | - | - | 17 | - |
| Port-Channel18 | server-1_PortChannel | switched | access | 110 | - | - | - | - | 18 | - |
| Port-Channel19 | server-1_PortChannel | switched | access | 110 | - | - | - | - | 19 | - |

### Port-Channel Interfaces Device Configuration

```eos
!
interface Port-Channel3
   description RACK2_MLAG_Po1
   no shutdown
   switchport
   switchport trunk allowed vlan 110-112,2500,2600,4085
   switchport mode trunk
   mlag 3
   service-profile QOS-PROFILE
!
interface Port-Channel5
   description MLAG_PEER_DC1-POD1-LEAF2B_Po5
   no shutdown
   switchport
   switchport trunk allowed vlan 2-4094
   switchport mode trunk
   switchport trunk group LEAF_PEER_L3
   switchport trunk group MLAG
   service-profile QOS-PROFILE
!
interface Port-Channel16
   description server-1_PortChannel
   no shutdown
   switchport
   switchport access vlan 110
   mlag 16
   service-profile bar
!
interface Port-Channel17
   description server-1_PortChannel
   no shutdown
   switchport
   switchport access vlan 110
   mlag 17
   service-profile foo
!
interface Port-Channel18
   description server-1_PortChannel
   no shutdown
   switchport
   switchport access vlan 110
   mlag 18
   service-profile foo
   comment
   Comment created from raw_eos_cli under port_channel on profile NESTED_TENANT_A
   EOF

!
interface Port-Channel19
   description server-1_PortChannel
   no shutdown
   switchport
   switchport access vlan 110
   mlag 19
   service-profile foo
   comment
   Comment created from raw_eos_cli under adapter port_channel for switch Po19
   EOF

```

## Loopback Interfaces

### Loopback Interfaces Summary

#### IPv4

| Interface | Description | VRF | IP Address |
| --------- | ----------- | --- | ---------- |
| Loopback0 | EVPN_Overlay_Peering | default | 172.16.110.4/32 |
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
   ip address 172.16.110.4/32
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
| Vlan110 | Tenant_A_OP_Zone_1 | Common_VRF | - | false |
| Vlan111 | Tenant_A_OP_Zone_2 | Common_VRF | - | true |
| Vlan112 | Tenant_A_OP_Zone_3 | Common_VRF | - | false |
| Vlan4085 | L2LEAF_INBAND_MGMT | default | 1500 | false |
| Vlan4093 | MLAG_PEER_L3_PEERING | default | 1500 | false |
| Vlan4094 | MLAG_PEER | default | 1500 | false |

#### IPv4

| Interface | VRF | IP Address | IP Address Virtual | IP Router Virtual Address | VRRP | ACL In | ACL Out |
| --------- | --- | ---------- | ------------------ | ------------------------- | ---- | ------ | ------- |
| Vlan110 |  Common_VRF  |  -  |  10.1.10.1/24  |  -  |  -  |  -  |  -  |
| Vlan111 |  Common_VRF  |  -  |  10.1.11.1/24  |  -  |  -  |  -  |  -  |
| Vlan112 |  Common_VRF  |  -  |  10.1.12.1/24  |  -  |  -  |  -  |  -  |
| Vlan4085 |  default  |  172.21.110.2/24  |  -  |  172.21.110.1  |  -  |  -  |  -  |
| Vlan4093 |  default  |  172.20.110.2/31  |  -  |  -  |  -  |  -  |  -  |
| Vlan4094 |  default  |  172.19.110.2/31  |  -  |  -  |  -  |  -  |  -  |

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
   comment
   Comment created from raw_eos_cli under SVI 112 in VRF Common_VRF
   EOF

!
interface Vlan4085
   description L2LEAF_INBAND_MGMT
   no shutdown
   mtu 1500
   ip address 172.21.110.2/24
   ip attached-host route export 19
   ip virtual-router address 172.21.110.1
!
interface Vlan4093
   description MLAG_PEER_L3_PEERING
   no shutdown
   mtu 1500
   ip address 172.20.110.2/31
!
interface Vlan4094
   description MLAG_PEER
   no shutdown
   mtu 1500
   no autostate
   ip address 172.19.110.2/31
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
| 110 | 10110 | - | - |
| 111 | 50111 | - | - |
| 112 | 50112 | - | - |
| 2500 | 2500 | - | - |
| 2600 | 2600 | - | - |

#### VRF to VNI and Multicast Group Mappings

| VRF | VNI | Multicast Group |
| ---- | --- | --------------- |
| Common_VRF | 1025 | - |

### VXLAN Interface Device Configuration

```eos
!
interface Vxlan1
   description DC1-POD1-LEAF2A_VTEP
   vxlan source-interface Loopback1
   vxlan virtual-router encapsulation mac-address mlag-system-id
   vxlan udp-port 4789
   vxlan vlan 110 vni 10110
   vxlan vlan 111 vni 50111
   vxlan vlan 112 vni 50112
   vxlan vlan 2500 vni 2500
   vxlan vlan 2600 vni 2600
   vxlan vrf Common_VRF vni 1025
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
| Common_VRF | true |
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
| default | false |
| Common_VRF | false |
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
| 65112|  172.16.110.4 |

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

#### MLAG-IPv4-UNDERLAY-PEER

| Settings | Value |
| -------- | ----- |
| Address Family | ipv4 |
| Remote AS | 65112 |
| Next-hop self | True |
| Send community | all |
| Maximum routes | 12000 |

### BGP Neighbors

| Neighbor | Remote AS | VRF | Shutdown | Send-community | Maximum-routes | Allowas-in | BFD | RIB Pre-Policy Retain |
| -------- | --------- | --- | -------- | -------------- | -------------- | ---------- | --- | --------------------- |
| 100.100.100.201 | 65211 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - |
| 172.16.10.1 | 65101 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - |
| 172.16.110.1 | 65110 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - |
| 172.16.110.3 | 65111 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - |
| 172.17.110.4 | 65110 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - |
| 172.17.110.6 | 65110 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - |
| 172.20.110.3 | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | default | - | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | - | - | - |

### Router BGP EVPN Address Family

#### EVPN Peer Groups

| Peer Group | Activate |
| ---------- | -------- |
| EVPN-OVERLAY-PEERS | True |

### Router BGP VLANs

| VLAN | Route-Distinguisher | Both Route-Target | Import Route Target | Export Route-Target | Redistribute |
| ---- | ------------------- | ----------------- | ------------------- | ------------------- | ------------ |
| 110 | 172.16.110.4:10110 | 10110:10110 | - | - | learned |
| 111 | 172.16.110.4:50111 | 50111:50111 | - | - | learned |
| 112 | 172.16.110.4:50112 | 50112:50112 | - | - | learned |
| 2500 | 172.16.110.4:2500 | 2500:2500 | - | - | learned |
| 2600 | 172.16.110.4:2600 | 2600:2600 | - | - | learned |

### Router BGP VRFs

| VRF | Route-Distinguisher | Redistribute |
| --- | ------------------- | ------------ |
| Common_VRF | 172.16.110.4:1025 | connected |

### Router BGP Device Configuration

```eos
!
router bgp 65112
   router-id 172.16.110.4
   no bgp default ipv4-unicast
   distance bgp 20 200 200
   graceful-restart restart-time 300
   graceful-restart
   maximum-paths 4 ecmp 4
   neighbor EVPN-OVERLAY-PEERS peer group
   neighbor EVPN-OVERLAY-PEERS remote-as 65110
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
   neighbor MLAG-IPv4-UNDERLAY-PEER description DC1-POD1-LEAF2B
   neighbor MLAG-IPv4-UNDERLAY-PEER password 7 vnEaG8gMeQf3d3cN6PktXQ==
   neighbor MLAG-IPv4-UNDERLAY-PEER send-community
   neighbor MLAG-IPv4-UNDERLAY-PEER maximum-routes 12000
   neighbor MLAG-IPv4-UNDERLAY-PEER route-map RM-MLAG-PEER-IN in
   neighbor 100.100.100.201 peer group IPv4-UNDERLAY-PEERS
   neighbor 100.100.100.201 remote-as 65211
   neighbor 100.100.100.201 description DC2-POD1-LEAF1A
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
   neighbor 172.17.110.4 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.110.4 remote-as 65110
   neighbor 172.17.110.4 description DC1-POD1-SPINE1_Ethernet4
   neighbor 172.17.110.6 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.110.6 remote-as 65110
   neighbor 172.17.110.6 description DC1-POD1-SPINE2_Ethernet4
   neighbor 172.20.110.3 peer group MLAG-IPv4-UNDERLAY-PEER
   neighbor 172.20.110.3 description DC1-POD1-LEAF2B
   redistribute attached-host
   redistribute connected route-map RM-CONN-2-BGP
   !
   vlan 110
      rd 172.16.110.4:10110
      route-target both 10110:10110
      redistribute learned
   !
   vlan 111
      rd 172.16.110.4:50111
      route-target both 50111:50111
      redistribute learned
   !
   vlan 112
      rd 172.16.110.4:50112
      route-target both 50112:50112
      redistribute learned
   !
   vlan 2500
      rd 172.16.110.4:2500
      route-target both 2500:2500
      redistribute learned
   !
   vlan 2600
      rd 172.16.110.4:2600
      route-target both 2600:2600
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
      rd 172.16.110.4:1025
      route-target import evpn 1025:1025
      route-target export evpn 1025:1025
      router-id 172.16.110.4
      redistribute connected
      !
      comment
      Comment created from raw_eos_cli under BGP for VRF Common_VRF
      EOF

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

# ACL

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

# Quality Of Service

# EOS CLI

```eos
!
interface Loopback1002
  description Loopback created from raw_eos_cli under l3leaf node-group RACK2_MLAG

interface Loopback1111
  description Loopback created from raw_eos_cli under platform_settings vEOS-LAB

interface Loopback1000
  description Loopback created from raw_eos_cli under VRF Common_VRF

```
