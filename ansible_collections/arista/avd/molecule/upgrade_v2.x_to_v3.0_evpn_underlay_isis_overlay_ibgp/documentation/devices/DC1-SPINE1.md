# DC1-SPINE1
# Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
  - [Name Servers](#name-servers)
  - [NTP](#ntp)
  - [Management API HTTP](#management-api-http)
- [Authentication](#authentication)
  - [Local Users](#local-users)
- [Monitoring](#monitoring)
  - [TerminAttr Daemon](#terminattr-daemon)
- [Spanning Tree](#spanning-tree)
  - [Spanning Tree Summary](#spanning-tree-summary)
  - [Spanning Tree Device Configuration](#spanning-tree-device-configuration)
- [Internal VLAN Allocation Policy](#internal-vlan-allocation-policy)
  - [Internal VLAN Allocation Policy Summary](#internal-vlan-allocation-policy-summary)
  - [Internal VLAN Allocation Policy Configuration](#internal-vlan-allocation-policy-configuration)
- [Interfaces](#interfaces)
  - [Ethernet Interfaces](#ethernet-interfaces)
  - [Loopback Interfaces](#loopback-interfaces)
- [Routing](#routing)
  - [Service Routing Protocols Model](#service-routing-protocols-model)
  - [IP Routing](#ip-routing)
  - [IPv6 Routing](#ipv6-routing)
  - [Static Routes](#static-routes)
  - [Router ISIS](#router-isis)
  - [Router BGP](#router-bgp)
- [BFD](#bfd)
  - [Router BFD](#router-bfd)
- [Multicast](#multicast)
- [Filters](#filters)
- [ACL](#acl)
- [VRF Instances](#vrf-instances)
  - [VRF Instances Summary](#vrf-instances-summary)
  - [VRF Instances Device Configuration](#vrf-instances-device-configuration)
- [Quality Of Service](#quality-of-service)

# Management

## Management Interfaces

### Management Interfaces Summary

#### IPv4

| Management Interface | description | Type | VRF | IP Address | Gateway |
| -------------------- | ----------- | ---- | --- | ---------- | ------- |
| Management1 | oob_management | oob | MGMT | 192.168.200.101/24 | 192.168.200.5 |

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
   ip address 192.168.200.101/24
```

## Name Servers

### Name Servers Summary

| Name Server | Source VRF |
| ----------- | ---------- |
| 192.168.200.5 | MGMT |
| 8.8.8.8 | MGMT |

### Name Servers Device Configuration

```eos
ip name-server vrf MGMT 8.8.8.8
ip name-server vrf MGMT 192.168.200.5
```

## NTP

### NTP Summary

#### NTP Local Interface

| Interface | VRF |
| --------- | --- |
| Management1 | MGMT |

#### NTP Servers

| Server | VRF | Preferred | Burst | iBurst | Version | Min Poll | Max Poll | Local-interface | Key |
| ------ | --- | --------- | ----- | ------ | ------- | -------- | -------- | --------------- | --- |
| 192.168.200.5 | MGMT | True | - | - | - | - | - | - | - |

### NTP Device Configuration

```eos
!
ntp local-interface vrf MGMT Management1
ntp server vrf MGMT 192.168.200.5 prefer
```

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
| cvpadmin | 15 | network-admin |

### Local Users Device Configuration

```eos
!
username admin privilege 15 role network-admin nopassword
username cvpadmin privilege 15 role network-admin secret sha512 $6$rZKcbIZ7iWGAWTUM$TCgDn1KcavS0s.OV8lacMTUkxTByfzcGlFlYUWroxYuU7M/9bIodhRO7nXGzMweUxvbk8mJmQl8Bh44cRktUj.
```

# Monitoring

## TerminAttr Daemon

### TerminAttr Daemon Summary

| CV Compression | CloudVision Servers | VRF | Authentication | Smash Excludes | Ingest Exclude | Bypass AAA |
| -------------- | ------------------- | --- | -------------- | -------------- | -------------- | ---------- |
| gzip | 192.168.200.11:9910 | MGMT | key,telarista | ale,flexCounter,hardware,kni,pulse,strata | /Sysdb/cell/1/agent,/Sysdb/cell/2/agent | True |

### TerminAttr Daemon Device Configuration

```eos
!
daemon TerminAttr
   exec /usr/bin/TerminAttr -cvaddr=192.168.200.11:9910 -cvauth=key,telarista -cvvrf=MGMT -disableaaa -smashexcludes=ale,flexCounter,hardware,kni,pulse,strata -ingestexclude=/Sysdb/cell/1/agent,/Sysdb/cell/2/agent -taillogs
   no shutdown
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

# Interfaces

## Ethernet Interfaces

### Ethernet Interfaces Summary

#### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | Channel-Group |
| --------- | ----------- | ---- | ----- | ----------- | ----------- | ------------- |

*Inherited from Port-Channel Interface

#### IPv4

| Interface | Description | Type | Channel Group | IP Address | VRF |  MTU | Shutdown | ACL In | ACL Out |
| --------- | ----------- | -----| ------------- | ---------- | ----| ---- | -------- | ------ | ------- |
| Ethernet1 | P2P_LINK_TO_DC1-LEAF1A_Ethernet1 | routed | - | 172.31.255.0/31 | default | 1500 | false | - | - |
| Ethernet2 | P2P_LINK_TO_DC1-LEAF2A_Ethernet1 | routed | - | 172.31.255.8/31 | default | 1500 | false | - | - |
| Ethernet3 | P2P_LINK_TO_DC1-LEAF2B_Ethernet1 | routed | - | 172.31.255.16/31 | default | 1500 | false | - | - |
| Ethernet4 | P2P_LINK_TO_DC1-SVC3A_Ethernet1 | routed | - | 172.31.255.24/31 | default | 1500 | false | - | - |
| Ethernet5 | P2P_LINK_TO_DC1-SVC3B_Ethernet1 | routed | - | 172.31.255.32/31 | default | 1500 | false | - | - |
| Ethernet6 | P2P_LINK_TO_DC1-BL1A_Ethernet1 | routed | - | 172.31.255.40/31 | default | 1500 | false | - | - |
| Ethernet7 | P2P_LINK_TO_DC1-BL1B_Ethernet1 | routed | - | 172.31.255.48/31 | default | 1500 | false | - | - |

#### ISIS

| Interface | Channel Group | ISIS Instance | ISIS Metric | Mode | ISIS Circuit Type | Hello Padding | Authentication Mode |
| --------- | ------------- | ------------- | ----------- | ---- | ----------------- | ------------- | ------------------- |
| Ethernet1 | - | EVPN_UNDERLAY | 50 | point-to-point | - | - | - |
| Ethernet2 | - | EVPN_UNDERLAY | 50 | point-to-point | - | - | - |
| Ethernet3 | - | EVPN_UNDERLAY | 50 | point-to-point | - | - | - |
| Ethernet4 | - | EVPN_UNDERLAY | 50 | point-to-point | - | - | - |
| Ethernet5 | - | EVPN_UNDERLAY | 50 | point-to-point | - | - | - |
| Ethernet6 | - | EVPN_UNDERLAY | 50 | point-to-point | - | - | - |
| Ethernet7 | - | EVPN_UNDERLAY | 50 | point-to-point | - | - | - |

### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet1
   description P2P_LINK_TO_DC1-LEAF1A_Ethernet1
   no shutdown
   mtu 1500
   no switchport
   ip address 172.31.255.0/31
   isis enable EVPN_UNDERLAY
   isis metric 50
   isis network point-to-point
!
interface Ethernet2
   description P2P_LINK_TO_DC1-LEAF2A_Ethernet1
   no shutdown
   mtu 1500
   no switchport
   ip address 172.31.255.8/31
   isis enable EVPN_UNDERLAY
   isis metric 50
   isis network point-to-point
!
interface Ethernet3
   description P2P_LINK_TO_DC1-LEAF2B_Ethernet1
   no shutdown
   mtu 1500
   no switchport
   ip address 172.31.255.16/31
   isis enable EVPN_UNDERLAY
   isis metric 50
   isis network point-to-point
!
interface Ethernet4
   description P2P_LINK_TO_DC1-SVC3A_Ethernet1
   no shutdown
   mtu 1500
   no switchport
   ip address 172.31.255.24/31
   isis enable EVPN_UNDERLAY
   isis metric 50
   isis network point-to-point
!
interface Ethernet5
   description P2P_LINK_TO_DC1-SVC3B_Ethernet1
   no shutdown
   mtu 1500
   no switchport
   ip address 172.31.255.32/31
   isis enable EVPN_UNDERLAY
   isis metric 50
   isis network point-to-point
!
interface Ethernet6
   description P2P_LINK_TO_DC1-BL1A_Ethernet1
   no shutdown
   mtu 1500
   no switchport
   ip address 172.31.255.40/31
   isis enable EVPN_UNDERLAY
   isis metric 50
   isis network point-to-point
!
interface Ethernet7
   description P2P_LINK_TO_DC1-BL1B_Ethernet1
   no shutdown
   mtu 1500
   no switchport
   ip address 172.31.255.48/31
   isis enable EVPN_UNDERLAY
   isis metric 50
   isis network point-to-point
```

## Loopback Interfaces

### Loopback Interfaces Summary

#### IPv4

| Interface | Description | VRF | IP Address |
| --------- | ----------- | --- | ---------- |
| Loopback0 | EVPN_Overlay_Peering | default | 192.168.255.1/32 |

#### IPv6

| Interface | Description | VRF | IPv6 Address |
| --------- | ----------- | --- | ------------ |
| Loopback0 | EVPN_Overlay_Peering | default | - |

#### ISIS

| Interface | ISIS instance | ISIS metric | Interface mode |
| --------- | ------------- | ----------- | -------------- |
| Loopback0 | EVPN_UNDERLAY | - | passive |

### Loopback Interfaces Device Configuration

```eos
!
interface Loopback0
   description EVPN_Overlay_Peering
   no shutdown
   ip address 192.168.255.1/32
   isis enable EVPN_UNDERLAY
   isis passive
```

# Routing
## Service Routing Protocols Model

Multi agent routing protocol model enabled

```eos
!
service routing protocols model multi-agent
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
| MGMT | 0.0.0.0/0 | 192.168.200.5 | - | 1 | - | - | - |

### Static Routes Device Configuration

```eos
!
ip route vrf MGMT 0.0.0.0/0 192.168.200.5
```

## Router ISIS

### Router ISIS Summary

| Settings | Value |
| -------- | ----- |
| Instance | EVPN_UNDERLAY |
| Net-ID | 49.0001.0001.0000.0001.00 |
| Type | level-2 |
| Address Family | ipv4 unicast |
| Router-ID | 192.168.255.1 |
| Log Adjacency Changes | True |

### ISIS Interfaces Summary

| Interface | ISIS Instance | ISIS Metric | Interface Mode |
| --------- | ------------- | ----------- | -------------- |
| Ethernet1 | EVPN_UNDERLAY | 50 | point-to-point |
| Ethernet2 | EVPN_UNDERLAY | 50 | point-to-point |
| Ethernet3 | EVPN_UNDERLAY | 50 | point-to-point |
| Ethernet4 | EVPN_UNDERLAY | 50 | point-to-point |
| Ethernet5 | EVPN_UNDERLAY | 50 | point-to-point |
| Ethernet6 | EVPN_UNDERLAY | 50 | point-to-point |
| Ethernet7 | EVPN_UNDERLAY | 50 | point-to-point |
| Loopback0 | EVPN_UNDERLAY | - | passive |

### Router ISIS Device Configuration

```eos
!
router isis EVPN_UNDERLAY
   net 49.0001.0001.0000.0001.00
   is-type level-2
   router-id ipv4 192.168.255.1
   log-adjacency-changes
   !
   address-family ipv4 unicast
      maximum-paths 4
   !
```

## Router BGP

### Router BGP Summary

| BGP AS | Router ID |
| ------ | --------- |
| 65000|  192.168.255.1 |

| BGP AS | Cluster ID |
| ------ | --------- |
| 65000|  192.168.255.1 |

| BGP Tuning |
| ---------- |
| no bgp default ipv4-unicast |
| distance bgp 20 200 200 |
| maximum-paths 4 ecmp 4 |

### Router BGP Peer Groups

#### OVERLAY-PEERS

| Settings | Value |
| -------- | ----- |
| Address Family | evpn |
| Remote AS | 65000 |
| Route Reflector Client | Yes |
| Source | Loopback0 |
| BFD | True |
| Send community | all |
| Maximum routes | 0 (no limit) |

### BGP Neighbors

| Neighbor | Remote AS | VRF | Shutdown | Send-community | Maximum-routes | Allowas-in | BFD | RIB Pre-Policy Retain |
| -------- | --------- | --- | -------- | -------------- | -------------- | ---------- | --- | --------------------- |
| 192.168.255.5 | Inherited from peer group OVERLAY-PEERS | default | - | Inherited from peer group OVERLAY-PEERS | Inherited from peer group OVERLAY-PEERS | - | Inherited from peer group OVERLAY-PEERS | - |
| 192.168.255.6 | Inherited from peer group OVERLAY-PEERS | default | - | Inherited from peer group OVERLAY-PEERS | Inherited from peer group OVERLAY-PEERS | - | Inherited from peer group OVERLAY-PEERS | - |
| 192.168.255.7 | Inherited from peer group OVERLAY-PEERS | default | - | Inherited from peer group OVERLAY-PEERS | Inherited from peer group OVERLAY-PEERS | - | Inherited from peer group OVERLAY-PEERS | - |
| 192.168.255.8 | Inherited from peer group OVERLAY-PEERS | default | - | Inherited from peer group OVERLAY-PEERS | Inherited from peer group OVERLAY-PEERS | - | Inherited from peer group OVERLAY-PEERS | - |
| 192.168.255.9 | Inherited from peer group OVERLAY-PEERS | default | - | Inherited from peer group OVERLAY-PEERS | Inherited from peer group OVERLAY-PEERS | - | Inherited from peer group OVERLAY-PEERS | - |
| 192.168.255.10 | Inherited from peer group OVERLAY-PEERS | default | - | Inherited from peer group OVERLAY-PEERS | Inherited from peer group OVERLAY-PEERS | - | Inherited from peer group OVERLAY-PEERS | - |
| 192.168.255.11 | Inherited from peer group OVERLAY-PEERS | default | - | Inherited from peer group OVERLAY-PEERS | Inherited from peer group OVERLAY-PEERS | - | Inherited from peer group OVERLAY-PEERS | - |

### Router BGP EVPN Address Family

#### EVPN Peer Groups

| Peer Group | Activate |
| ---------- | -------- |
| OVERLAY-PEERS | True |

### Router BGP Device Configuration

```eos
!
router bgp 65000
   router-id 192.168.255.1
   bgp cluster-id 192.168.255.1
   no bgp default ipv4-unicast
   distance bgp 20 200 200
   maximum-paths 4 ecmp 4
   neighbor OVERLAY-PEERS peer group
   neighbor OVERLAY-PEERS remote-as 65000
   neighbor OVERLAY-PEERS update-source Loopback0
   neighbor OVERLAY-PEERS route-reflector-client
   neighbor OVERLAY-PEERS bfd
   neighbor OVERLAY-PEERS password 7 q+VNViP5i4rVjW1cxFv2wA==
   neighbor OVERLAY-PEERS send-community
   neighbor OVERLAY-PEERS maximum-routes 0
   neighbor 192.168.255.5 peer group OVERLAY-PEERS
   neighbor 192.168.255.5 description DC1-LEAF1A
   neighbor 192.168.255.6 peer group OVERLAY-PEERS
   neighbor 192.168.255.6 description DC1-LEAF2A
   neighbor 192.168.255.7 peer group OVERLAY-PEERS
   neighbor 192.168.255.7 description DC1-LEAF2B
   neighbor 192.168.255.8 peer group OVERLAY-PEERS
   neighbor 192.168.255.8 description DC1-SVC3A
   neighbor 192.168.255.9 peer group OVERLAY-PEERS
   neighbor 192.168.255.9 description DC1-SVC3B
   neighbor 192.168.255.10 peer group OVERLAY-PEERS
   neighbor 192.168.255.10 description DC1-BL1A
   neighbor 192.168.255.11 peer group OVERLAY-PEERS
   neighbor 192.168.255.11 description DC1-BL1B
   !
   address-family evpn
      neighbor OVERLAY-PEERS activate
   !
   address-family ipv4
      no neighbor OVERLAY-PEERS activate
```

# BFD

## Router BFD

### Router BFD Multihop Summary

| Interval | Minimum RX | Multiplier |
| -------- | ---------- | ---------- |
| 1200 | 1200 | 3 |

### Router BFD Device Configuration

```eos
!
router bfd
   multihop interval 1200 min-rx 1200 multiplier 3
```

# Multicast

# Filters

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
