# DC1-SVC3B

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
  - [IP Name Servers](#ip-name-servers)
  - [NTP](#ntp)
  - [Management API HTTP](#management-api-http)
- [Authentication](#authentication)
  - [Local Users](#local-users)
  - [Enable Password](#enable-password)
- [Monitoring](#monitoring)
  - [TerminAttr Daemon](#terminattr-daemon)
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
  - [VXLAN Interface](#vxlan-interface)
- [Routing](#routing)
  - [Service Routing Protocols Model](#service-routing-protocols-model)
  - [Virtual Router MAC Address](#virtual-router-mac-address)
  - [IP Routing](#ip-routing)
  - [IPv6 Routing](#ipv6-routing)
  - [Static Routes](#static-routes)
  - [Router OSPF](#router-ospf)
  - [Router BGP](#router-bgp)
- [BFD](#bfd)
  - [Router BFD](#router-bfd)
- [Multicast](#multicast)
  - [IP IGMP Snooping](#ip-igmp-snooping)
- [Filters](#filters)
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
| Management1 | oob_management | oob | MGMT | 192.168.200.109/24 | 192.168.200.5 |

##### IPv6

| Management Interface | Description | Type | VRF | IPv6 Address | IPv6 Gateway |
| -------------------- | ----------- | ---- | --- | ------------ | ------------ |
| Management1 | oob_management | oob | MGMT | - | - |

#### Management Interfaces Device Configuration

```eos
!
interface Management1
   description oob_management
   no shutdown
   vrf MGMT
   ip address 192.168.200.109/24
```

### IP Name Servers

#### IP Name Servers Summary

| Name Server | VRF | Priority |
| ----------- | --- | -------- |
| 192.168.200.5 | MGMT | - |
| 8.8.8.8 | MGMT | - |

#### IP Name Servers Device Configuration

```eos
ip name-server vrf MGMT 8.8.8.8
ip name-server vrf MGMT 192.168.200.5
```

### NTP

#### NTP Summary

##### NTP Local Interface

| Interface | VRF |
| --------- | --- |
| Management1 | MGMT |

##### NTP Servers

| Server | VRF | Preferred | Burst | iBurst | Version | Min Poll | Max Poll | Local-interface | Key |
| ------ | --- | --------- | ----- | ------ | ------- | -------- | -------- | --------------- | --- |
| 192.168.200.5 | MGMT | True | - | - | - | - | - | - | - |

#### NTP Device Configuration

```eos
!
ntp local-interface vrf MGMT Management1
ntp server vrf MGMT 192.168.200.5 prefer
```

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

## Authentication

### Local Users

#### Local Users Summary

| User | Privilege | Role | Disabled | Shell |
| ---- | --------- | ---- | -------- | ----- |
| admin | 15 | network-admin | False | - |
| cvpadmin | 15 | network-admin | False | - |

#### Local Users Device Configuration

```eos
!
username admin privilege 15 role network-admin nopassword
username cvpadmin privilege 15 role network-admin secret sha512 <removed>
```

### Enable Password

Enable password has been disabled

## Monitoring

### TerminAttr Daemon

#### TerminAttr Daemon Summary

| CV Compression | CloudVision Servers | VRF | Authentication | Smash Excludes | Ingest Exclude | Bypass AAA |
| -------------- | ------------------- | --- | -------------- | -------------- | -------------- | ---------- |
| gzip | 192.168.200.11:9910 | MGMT | key,telarista | ale,flexCounter,hardware,kni,pulse,strata | /Sysdb/cell/1/agent,/Sysdb/cell/2/agent | False |

#### TerminAttr Daemon Device Configuration

```eos
!
daemon TerminAttr
   exec /usr/bin/TerminAttr -cvaddr=192.168.200.11:9910 -cvauth=key,<removed> -cvvrf=MGMT -smashexcludes=ale,flexCounter,hardware,kni,pulse,strata -ingestexclude=/Sysdb/cell/1/agent,/Sysdb/cell/2/agent -taillogs
   no shutdown
```

## MLAG

### MLAG Summary

| Domain-id | Local-interface | Peer-address | Peer-link |
| --------- | --------------- | ------------ | --------- |
| DC1_SVC3 | Vlan4094 | 10.255.252.6 | Port-Channel5 |

Dual primary detection is disabled.

### MLAG Device Configuration

```eos
!
mlag configuration
   domain-id DC1_SVC3
   local-interface Vlan4094
   peer-address 10.255.252.6
   peer-link Port-Channel5
   reload-delay mlag 300
   reload-delay non-mlag 330
```

## Spanning Tree

### Spanning Tree Summary

STP mode: **mstp**

#### MSTP Instance and Priority

| Instance(s) | Priority |
| -------- | -------- |
| 0 | 4096 |

#### Global Spanning-Tree Settings

- Spanning Tree disabled for VLANs: **4094**

### Spanning Tree Device Configuration

```eos
!
spanning-tree mode mstp
no spanning-tree vlan-id 4094
spanning-tree mst 0 priority 4096
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
| 210 | Tenant_B_OP_Zone_1 | - |
| 3019 | MLAG_iBGP_Tenant_B_OP_Zone | LEAF_PEER_L3 |
| 4094 | MLAG_PEER | MLAG |

### VLANs Device Configuration

```eos
!
vlan 210
   name Tenant_B_OP_Zone_1
!
vlan 3019
   name MLAG_iBGP_Tenant_B_OP_Zone
   trunk group LEAF_PEER_L3
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
| Ethernet5 | MLAG_PEER_DC1-SVC3A_Ethernet5 | *trunk | *- | *- | *LEAF_PEER_L3, MLAG | 5 |
| Ethernet6 | MLAG_PEER_DC1-SVC3A_Ethernet6 | *trunk | *- | *- | *LEAF_PEER_L3, MLAG | 5 |
| Ethernet7 | DC1-L2LEAF2A_Ethernet2 | *trunk | *210 | *- | *- | 7 |
| Ethernet8 | DC1-L2LEAF2B_Ethernet2 | *trunk | *210 | *- | *- | 7 |

*Inherited from Port-Channel Interface

##### IPv4

| Interface | Description | Channel Group | IP Address | VRF |  MTU | Shutdown | ACL In | ACL Out |
| --------- | ----------- | ------------- | ---------- | ----| ---- | -------- | ------ | ------- |
| Ethernet1 | P2P_LINK_TO_DC1-SPINE1_Ethernet5 | - | 172.31.255.33/31 | default | 1500 | False | - | - |
| Ethernet2 | P2P_LINK_TO_DC1-SPINE2_Ethernet5 | - | 172.31.255.35/31 | default | 1500 | False | - | - |
| Ethernet3 | P2P_LINK_TO_DC1-SPINE3_Ethernet5 | - | 172.31.255.37/31 | default | 1500 | False | - | - |
| Ethernet4 | P2P_LINK_TO_DC1-SPINE4_Ethernet5 | - | 172.31.255.39/31 | default | 1500 | False | - | - |

#### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet1
   description P2P_LINK_TO_DC1-SPINE1_Ethernet5
   no shutdown
   mtu 1500
   no switchport
   ip address 172.31.255.33/31
   ip ospf network point-to-point
   ip ospf authentication message-digest
   ip ospf area 0.0.0.0
   ip ospf message-digest-key 1 sha256 7 <removed>
!
interface Ethernet2
   description P2P_LINK_TO_DC1-SPINE2_Ethernet5
   no shutdown
   mtu 1500
   no switchport
   ip address 172.31.255.35/31
   ip ospf network point-to-point
   ip ospf authentication message-digest
   ip ospf area 0.0.0.0
   ip ospf message-digest-key 1 sha256 7 <removed>
!
interface Ethernet3
   description P2P_LINK_TO_DC1-SPINE3_Ethernet5
   no shutdown
   mtu 1500
   no switchport
   ip address 172.31.255.37/31
   ip ospf network point-to-point
   ip ospf authentication message-digest
   ip ospf area 0.0.0.0
   ip ospf message-digest-key 1 sha256 7 <removed>
!
interface Ethernet4
   description P2P_LINK_TO_DC1-SPINE4_Ethernet5
   no shutdown
   mtu 1500
   no switchport
   ip address 172.31.255.39/31
   ip ospf network point-to-point
   ip ospf authentication message-digest
   ip ospf area 0.0.0.0
   ip ospf message-digest-key 1 sha256 7 <removed>
!
interface Ethernet5
   description MLAG_PEER_DC1-SVC3A_Ethernet5
   no shutdown
   channel-group 5 mode active
!
interface Ethernet6
   description MLAG_PEER_DC1-SVC3A_Ethernet6
   no shutdown
   channel-group 5 mode active
!
interface Ethernet7
   description DC1-L2LEAF2A_Ethernet2
   no shutdown
   channel-group 7 mode active
!
interface Ethernet8
   description DC1-L2LEAF2B_Ethernet2
   no shutdown
   channel-group 7 mode active
```

### Port-Channel Interfaces

#### Port-Channel Interfaces Summary

##### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | LACP Fallback Timeout | LACP Fallback Mode | MLAG ID | EVPN ESI |
| --------- | ----------- | ---- | ----- | ----------- | ------------| --------------------- | ------------------ | ------- | -------- |
| Port-Channel5 | MLAG_PEER_DC1-SVC3A_Po5 | trunk | - | - | LEAF_PEER_L3, MLAG | - | - | - | - |
| Port-Channel7 | DC1_L2LEAF2_Po1 | trunk | 210 | - | - | - | - | 7 | - |

#### Port-Channel Interfaces Device Configuration

```eos
!
interface Port-Channel5
   description MLAG_PEER_DC1-SVC3A_Po5
   no shutdown
   switchport
   switchport mode trunk
   switchport trunk group LEAF_PEER_L3
   switchport trunk group MLAG
!
interface Port-Channel7
   description DC1_L2LEAF2_Po1
   no shutdown
   switchport
   switchport trunk allowed vlan 210
   switchport mode trunk
   mlag 7
```

### Loopback Interfaces

#### Loopback Interfaces Summary

##### IPv4

| Interface | Description | VRF | IP Address |
| --------- | ----------- | --- | ---------- |
| Loopback0 | EVPN_Overlay_Peering | default | 192.168.255.9/32 |
| Loopback1 | VTEP_VXLAN_Tunnel_Source | default | 192.168.254.8/32 |

##### IPv6

| Interface | Description | VRF | IPv6 Address |
| --------- | ----------- | --- | ------------ |
| Loopback0 | EVPN_Overlay_Peering | default | - |
| Loopback1 | VTEP_VXLAN_Tunnel_Source | default | - |

#### Loopback Interfaces Device Configuration

```eos
!
interface Loopback0
   description EVPN_Overlay_Peering
   no shutdown
   ip address 192.168.255.9/32
   ip ospf area 0.0.0.0
!
interface Loopback1
   description VTEP_VXLAN_Tunnel_Source
   no shutdown
   ip address 192.168.254.8/32
   ip ospf area 0.0.0.0
```

### VLAN Interfaces

#### VLAN Interfaces Summary

| Interface | Description | VRF |  MTU | Shutdown |
| --------- | ----------- | --- | ---- | -------- |
| Vlan210 | Tenant_B_OP_Zone_1 | Tenant_B_OP_Zone | - | False |
| Vlan3019 | MLAG_PEER_L3_iBGP: vrf Tenant_B_OP_Zone | Tenant_B_OP_Zone | 1500 | False |
| Vlan4094 | MLAG_PEER | default | 1500 | False |

##### IPv4

| Interface | VRF | IP Address | IP Address Virtual | IP Router Virtual Address | ACL In | ACL Out |
| --------- | --- | ---------- | ------------------ | ------------------------- | ------ | ------- |
| Vlan210 |  Tenant_B_OP_Zone  |  -  |  10.2.10.1/24  |  -  |  -  |  -  |
| Vlan3019 |  Tenant_B_OP_Zone  |  10.255.252.7/31  |  -  |  -  |  -  |  -  |
| Vlan4094 |  default  |  10.255.252.7/31  |  -  |  -  |  -  |  -  |

#### VLAN Interfaces Device Configuration

```eos
!
interface Vlan210
   description Tenant_B_OP_Zone_1
   no shutdown
   vrf Tenant_B_OP_Zone
   ip address virtual 10.2.10.1/24
!
interface Vlan3019
   description MLAG_PEER_L3_iBGP: vrf Tenant_B_OP_Zone
   no shutdown
   mtu 1500
   vrf Tenant_B_OP_Zone
   ip address 10.255.252.7/31
!
interface Vlan4094
   description MLAG_PEER
   no shutdown
   mtu 1500
   no autostate
   ip address 10.255.252.7/31
   ip ospf network point-to-point
   ip ospf area 0.0.0.0
```

### VXLAN Interface

#### VXLAN Interface Summary

| Setting | Value |
| ------- | ----- |
| Source Interface | Loopback1 |
| UDP port | 4789 |
| EVPN MLAG Shared Router MAC | mlag-system-id |

##### VLAN to VNI, Flood List and Multicast Group Mappings

| VLAN | VNI | Flood List | Multicast Group |
| ---- | --- | ---------- | --------------- |
| 210 | 20210 | - | - |

##### VRF to VNI and Multicast Group Mappings

| VRF | VNI | Multicast Group |
| ---- | --- | --------------- |
| Tenant_B_OP_Zone | 20 | - |

#### VXLAN Interface Device Configuration

```eos
!
interface Vxlan1
   description DC1-SVC3B_VTEP
   vxlan source-interface Loopback1
   vxlan virtual-router encapsulation mac-address mlag-system-id
   vxlan udp-port 4789
   vxlan vlan 210 vni 20210
   vxlan vrf Tenant_B_OP_Zone vni 20
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

Virtual Router MAC Address: 00:dc:00:00:00:0a

#### Virtual Router MAC Address Device Configuration

```eos
!
ip virtual-router mac-address 00:dc:00:00:00:0a
```

### IP Routing

#### IP Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | True |
| MGMT | False |
| Tenant_B_OP_Zone | True |

#### IP Routing Device Configuration

```eos
!
ip routing
no ip routing vrf MGMT
ip routing vrf Tenant_B_OP_Zone
```

### IPv6 Routing

#### IPv6 Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | False |
| MGMT | false |
| Tenant_B_OP_Zone | false |

### Static Routes

#### Static Routes Summary

| VRF | Destination Prefix | Next Hop IP | Exit interface | Administrative Distance | Tag | Route Name | Metric |
| --- | ------------------ | ----------- | -------------- | ----------------------- | --- | ---------- | ------ |
| MGMT | 0.0.0.0/0 | 192.168.200.5 | - | 1 | - | - | - |

#### Static Routes Device Configuration

```eos
!
ip route vrf MGMT 0.0.0.0/0 192.168.200.5
```

### Router OSPF

#### Router OSPF Summary

| Process ID | Router ID | Default Passive Interface | No Passive Interface | BFD | Max LSA | Default Information Originate | Log Adjacency Changes Detail | Auto Cost Reference Bandwidth | Maximum Paths | MPLS LDP Sync Default | Distribute List In |
| ---------- | --------- | ------------------------- | -------------------- | --- | ------- | ----------------------------- | ---------------------------- | ----------------------------- | ------------- | --------------------- | ------------------ |
| 101 | 192.168.255.9 | enabled | Ethernet1 <br> Ethernet2 <br> Ethernet3 <br> Ethernet4 <br> Vlan4094 <br> | enabled | 12000 | disabled | disabled | - | - | - | - |

#### OSPF Interfaces

| Interface | Area | Cost | Point To Point |
| -------- | -------- | -------- | -------- |
| Ethernet1 | 0.0.0.0 | - | True |
| Ethernet2 | 0.0.0.0 | - | True |
| Ethernet3 | 0.0.0.0 | - | True |
| Ethernet4 | 0.0.0.0 | - | True |
| Vlan4094 | 0.0.0.0 | - | True |
| Loopback0 | 0.0.0.0 | - | - |
| Loopback1 | 0.0.0.0 | - | - |

#### Router OSPF Device Configuration

```eos
!
router ospf 101
   router-id 192.168.255.9
   passive-interface default
   no passive-interface Ethernet1
   no passive-interface Ethernet2
   no passive-interface Ethernet3
   no passive-interface Ethernet4
   no passive-interface Vlan4094
   bfd default
   max-lsa 12000
```

### Router BGP

ASN Notation: asplain

#### Router BGP Summary

| BGP AS | Router ID |
| ------ | --------- |
| 65103 | 192.168.255.9 |

| BGP Tuning |
| ---------- |
| distance bgp 20 200 200 |
| update wait-install |
| no bgp default ipv4-unicast |
| maximum-paths 10 ecmp 10 |

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

##### MLAG-IPv4-UNDERLAY-PEER

| Settings | Value |
| -------- | ----- |
| Address Family | ipv4 |
| Remote AS | 65103 |
| Next-hop self | True |
| Send community | all |
| Maximum routes | 12000 |

#### BGP Neighbors

| Neighbor | Remote AS | VRF | Shutdown | Send-community | Maximum-routes | Allowas-in | BFD | RIB Pre-Policy Retain | Route-Reflector Client | Passive | TTL Max Hops |
| -------- | --------- | --- | -------- | -------------- | -------------- | ---------- | --- | --------------------- | ---------------------- | ------- | ------------ |
| 192.168.255.1 | 65001 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 192.168.255.2 | 65001 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 192.168.255.3 | 65001 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 192.168.255.4 | 65001 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 10.255.252.6 | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | Tenant_B_OP_Zone | - | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | - | - | - | - | - | - |

#### Router BGP EVPN Address Family

##### EVPN Peer Groups

| Peer Group | Activate | Encapsulation |
| ---------- | -------- | ------------- |
| EVPN-OVERLAY-PEERS | True | default |

##### EVPN Host Flapping Settings

| State | Window | Threshold | Expiry Timeout |
| ----- | ------ | --------- | -------------- |
| Enabled | 180 Seconds | 30 | - |

#### Router BGP VLAN Aware Bundles

| VLAN Aware Bundle | Route-Distinguisher | Both Route-Target | Import Route Target | Export Route-Target | Redistribute | VLANs |
| ----------------- | ------------------- | ----------------- | ------------------- | ------------------- | ------------ | ----- |
| Tenant_B_OP_Zone | 192.168.255.9:20 | 20:20 | - | - | learned | 210 |

#### Router BGP VRFs

| VRF | Route-Distinguisher | Redistribute |
| --- | ------------------- | ------------ |
| Tenant_B_OP_Zone | 192.168.255.9:20 | connected |

#### Router BGP Device Configuration

```eos
!
router bgp 65103
   router-id 192.168.255.9
   maximum-paths 10 ecmp 10
   update wait-install
   no bgp default ipv4-unicast
   distance bgp 20 200 200
   neighbor EVPN-OVERLAY-PEERS peer group
   neighbor EVPN-OVERLAY-PEERS update-source Loopback0
   neighbor EVPN-OVERLAY-PEERS bfd
   neighbor EVPN-OVERLAY-PEERS ebgp-multihop 3
   neighbor EVPN-OVERLAY-PEERS password 7 <removed>
   neighbor EVPN-OVERLAY-PEERS send-community
   neighbor EVPN-OVERLAY-PEERS maximum-routes 0
   neighbor MLAG-IPv4-UNDERLAY-PEER peer group
   neighbor MLAG-IPv4-UNDERLAY-PEER remote-as 65103
   neighbor MLAG-IPv4-UNDERLAY-PEER next-hop-self
   neighbor MLAG-IPv4-UNDERLAY-PEER description DC1-SVC3A
   neighbor MLAG-IPv4-UNDERLAY-PEER password 7 <removed>
   neighbor MLAG-IPv4-UNDERLAY-PEER send-community
   neighbor MLAG-IPv4-UNDERLAY-PEER maximum-routes 12000
   neighbor MLAG-IPv4-UNDERLAY-PEER route-map RM-MLAG-PEER-IN in
   neighbor 192.168.255.1 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.255.1 remote-as 65001
   neighbor 192.168.255.1 description DC1-SPINE1
   neighbor 192.168.255.2 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.255.2 remote-as 65001
   neighbor 192.168.255.2 description DC1-SPINE2
   neighbor 192.168.255.3 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.255.3 remote-as 65001
   neighbor 192.168.255.3 description DC1-SPINE3
   neighbor 192.168.255.4 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.255.4 remote-as 65001
   neighbor 192.168.255.4 description DC1-SPINE4
   !
   vlan-aware-bundle Tenant_B_OP_Zone
      rd 192.168.255.9:20
      route-target both 20:20
      redistribute learned
      vlan 210
   !
   address-family evpn
      host-flap detection window 180 threshold 30
      neighbor EVPN-OVERLAY-PEERS activate
   !
   address-family ipv4
      no neighbor EVPN-OVERLAY-PEERS activate
      neighbor MLAG-IPv4-UNDERLAY-PEER activate
   !
   vrf Tenant_B_OP_Zone
      rd 192.168.255.9:20
      route-target import evpn 20:20
      route-target export evpn 20:20
      router-id 192.168.255.9
      update wait-install
      neighbor 10.255.252.6 peer group MLAG-IPv4-UNDERLAY-PEER
      neighbor 10.255.252.6 description DC1-SVC3A
      redistribute connected
```

## BFD

### Router BFD

#### Router BFD Multihop Summary

| Interval | Minimum RX | Multiplier |
| -------- | ---------- | ---------- |
| 1200 | 1200 | 3 |

#### Router BFD Device Configuration

```eos
!
router bfd
   multihop interval 1200 min-rx 1200 multiplier 3
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
| Tenant_B_OP_Zone | enabled |

### VRF Instances Device Configuration

```eos
!
vrf instance MGMT
!
vrf instance Tenant_B_OP_Zone
```
