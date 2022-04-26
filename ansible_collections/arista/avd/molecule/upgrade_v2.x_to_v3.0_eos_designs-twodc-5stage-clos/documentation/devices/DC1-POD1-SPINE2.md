# DC1-POD1-SPINE2
# Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
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
- [Interfaces](#interfaces)
  - [Ethernet Interfaces](#ethernet-interfaces)
  - [Loopback Interfaces](#loopback-interfaces)
- [Routing](#routing)
  - [Service Routing Protocols Model](#service-routing-protocols-model)
  - [IP Routing](#ip-routing)
  - [IPv6 Routing](#ipv6-routing)
  - [Static Routes](#static-routes)
  - [Router BGP](#router-bgp)
- [Multicast](#multicast)
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

## Management Interfaces

### Management Interfaces Summary

#### IPv4

| Management Interface | description | Type | VRF | IP Address | Gateway |
| -------------------- | ----------- | ---- | --- | ---------- | ------- |
| Management1 | oob_management | oob | MGMT | 192.168.1.6/24 | 192.168.1.254 |

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
   ip address 192.168.1.6/24
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
| - | TWODC_5STAGE_CLOS DC1 DC1_POD1 DC1-POD1-SPINE2 | All | Disabled |

### SNMP Device Configuration

```eos
!
snmp-server location TWODC_5STAGE_CLOS DC1 DC1_POD1 DC1-POD1-SPINE2
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
| Ethernet1 | P2P_LINK_TO_DC1-SUPER-SPINE1_Ethernet2 | routed | - | 172.16.11.3/31 | default | 1500 | false | - | - |
| Ethernet2 | P2P_LINK_TO_DC1-SUPER-SPINE2_Ethernet2 | routed | - | 172.16.11.67/31 | default | 1500 | false | - | - |
| Ethernet3 | P2P_LINK_TO_DC1-POD1-LEAF1A_Ethernet2 | routed | - | 172.17.110.2/31 | default | 1500 | false | - | - |
| Ethernet4 | P2P_LINK_TO_DC1-POD1-LEAF2A_Ethernet2 | routed | - | 172.17.110.6/31 | default | 1500 | false | - | - |
| Ethernet5 | P2P_LINK_TO_DC1-POD1-LEAF2B_Ethernet2 | routed | - | 172.17.110.10/31 | default | 1500 | false | - | - |

### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet1
   description P2P_LINK_TO_DC1-SUPER-SPINE1_Ethernet2
   no shutdown
   mtu 1500
   no switchport
   ip address 172.16.11.3/31
   ptp enable
   service-profile QOS-PROFILE
!
interface Ethernet2
   description P2P_LINK_TO_DC1-SUPER-SPINE2_Ethernet2
   no shutdown
   mtu 1500
   no switchport
   ip address 172.16.11.67/31
   ptp enable
   service-profile QOS-PROFILE
!
interface Ethernet3
   description P2P_LINK_TO_DC1-POD1-LEAF1A_Ethernet2
   no shutdown
   mtu 1500
   no switchport
   ip address 172.17.110.2/31
   ptp enable
   service-profile QOS-PROFILE
!
interface Ethernet4
   description P2P_LINK_TO_DC1-POD1-LEAF2A_Ethernet2
   no shutdown
   mtu 1500
   no switchport
   ip address 172.17.110.6/31
   ptp enable
   service-profile QOS-PROFILE
!
interface Ethernet5
   description P2P_LINK_TO_DC1-POD1-LEAF2B_Ethernet2
   no shutdown
   mtu 1500
   no switchport
   ip address 172.17.110.10/31
   ptp enable
   service-profile QOS-PROFILE
```

## Loopback Interfaces

### Loopback Interfaces Summary

#### IPv4

| Interface | Description | VRF | IP Address |
| --------- | ----------- | --- | ---------- |
| Loopback0 | EVPN_Overlay_Peering | default | 172.16.110.2/32 |

#### IPv6

| Interface | Description | VRF | IPv6 Address |
| --------- | ----------- | --- | ------------ |
| Loopback0 | EVPN_Overlay_Peering | default | - |


### Loopback Interfaces Device Configuration

```eos
!
interface Loopback0
   description EVPN_Overlay_Peering
   no shutdown
   ip address 172.16.110.2/32
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
| 65110|  172.16.110.2 |

| BGP Tuning |
| ---------- |
| no bgp default ipv4-unicast |
| distance bgp 20 200 200 |
| graceful-restart restart-time 300 |
| graceful-restart |
| maximum-paths 4 ecmp 4 |

### Router BGP Peer Groups

#### IPv4-UNDERLAY-PEERS

| Settings | Value |
| -------- | ----- |
| Address Family | ipv4 |
| Send community | all |
| Maximum routes | 12000 |

### BGP Neighbors

| Neighbor | Remote AS | VRF | Shutdown | Send-community | Maximum-routes | Allowas-in | BFD | RIB Pre-Policy Retain |
| -------- | --------- | --- | -------- | -------------- | -------------- | ---------- | --- | --------------------- |
| 172.16.11.2 | 65100 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - |
| 172.16.11.66 | 65100 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - |
| 172.17.110.3 | 65111 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - |
| 172.17.110.7 | 65112 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - |
| 172.17.110.11 | 65112 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - |

### Router BGP Device Configuration

```eos
!
router bgp 65110
   router-id 172.16.110.2
   no bgp default ipv4-unicast
   distance bgp 20 200 200
   graceful-restart restart-time 300
   graceful-restart
   maximum-paths 4 ecmp 4
   neighbor IPv4-UNDERLAY-PEERS peer group
   neighbor IPv4-UNDERLAY-PEERS password 7 AQQvKeimxJu+uGQ/yYvv9w==
   neighbor IPv4-UNDERLAY-PEERS send-community
   neighbor IPv4-UNDERLAY-PEERS maximum-routes 12000
   neighbor 172.16.11.2 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.16.11.2 remote-as 65100
   neighbor 172.16.11.2 description DC1-SUPER-SPINE1_Ethernet2
   neighbor 172.16.11.66 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.16.11.66 remote-as 65100
   neighbor 172.16.11.66 description DC1-SUPER-SPINE2_Ethernet2
   neighbor 172.17.110.3 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.110.3 remote-as 65111
   neighbor 172.17.110.3 description DC1-POD1-LEAF1A_Ethernet2
   neighbor 172.17.110.7 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.110.7 remote-as 65112
   neighbor 172.17.110.7 description DC1-POD1-LEAF2A_Ethernet2
   neighbor 172.17.110.11 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.110.11 remote-as 65112
   neighbor 172.17.110.11 description DC1-POD1-LEAF2B_Ethernet2
   redistribute connected route-map RM-CONN-2-BGP
   !
   address-family ipv4
      neighbor IPv4-UNDERLAY-PEERS activate
```

# Multicast

# Filters

## Prefix-lists

### Prefix-lists Summary

#### PL-LOOPBACKS-EVPN-OVERLAY

| Sequence | Action |
| -------- | ------ |
| 10 | permit 172.16.110.0/24 eq 32 |

### Prefix-lists Device Configuration

```eos
!
ip prefix-list PL-LOOPBACKS-EVPN-OVERLAY
   seq 10 permit 172.16.110.0/24 eq 32
```

## Route-maps

### Route-maps Summary

#### RM-CONN-2-BGP

| Sequence | Type | Match and/or Set |
| -------- | ---- | ---------------- |
| 10 | permit | match ip address prefix-list PL-LOOPBACKS-EVPN-OVERLAY |

### Route-maps Device Configuration

```eos
!
route-map RM-CONN-2-BGP permit 10
   match ip address prefix-list PL-LOOPBACKS-EVPN-OVERLAY
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
interface Loopback1111
  description Loopback created from raw_eos_cli under platform_settings vEOS-LAB

```
