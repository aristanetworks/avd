# DC2-POD1-SPINE2

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
  - [Management API HTTP](#management-api-http)
- [Authentication](#authentication)
  - [Local Users](#local-users)
  - [Enable Password](#enable-password)
- [Monitoring](#monitoring)
  - [SNMP](#snmp)
- [Spanning Tree](#spanning-tree)
  - [Spanning Tree Summary](#spanning-tree-summary)
  - [Spanning Tree Device Configuration](#spanning-tree-device-configuration)
- [Internal VLAN Allocation Policy](#internal-vlan-allocation-policy)
  - [Internal VLAN Allocation Policy Summary](#internal-vlan-allocation-policy-summary)
  - [Internal VLAN Allocation Policy Device Configuration](#internal-vlan-allocation-policy-device-configuration)
- [Interfaces](#interfaces)
  - [Ethernet Interfaces](#ethernet-interfaces)
  - [Loopback Interfaces](#loopback-interfaces)
- [Routing](#routing)
  - [Service Routing Protocols Model](#service-routing-protocols-model)
  - [IP Routing](#ip-routing)
  - [IPv6 Routing](#ipv6-routing)
  - [Static Routes](#static-routes)
  - [Router BGP](#router-bgp)
- [Filters](#filters)
  - [Prefix-lists](#prefix-lists)
  - [Route-maps](#route-maps)
- [VRF Instances](#vrf-instances)
  - [VRF Instances Summary](#vrf-instances-summary)
  - [VRF Instances Device Configuration](#vrf-instances-device-configuration)
- [EOS CLI Device Configuration](#eos-cli-device-configuration)

## Management

### Management Interfaces

#### Management Interfaces Summary

##### IPv4

| Management Interface | Description | Type | VRF | IP Address | Gateway |
| -------------------- | ----------- | ---- | --- | ---------- | ------- |
| Management1 | oob_management | oob | MGMT | 192.168.1.21/24 | 192.168.1.254 |

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
   ip address 192.168.1.21/24
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

#### Local Users Device Configuration

```eos
!
username admin privilege 15 role network-admin secret sha512 <removed>
```

### Enable Password

Enable password has been disabled

## Monitoring

### SNMP

#### SNMP Configuration Summary

| Contact | Location | SNMP Traps | State |
| ------- | -------- | ---------- | ----- |
| - | TWODC_5STAGE_CLOS DC2 DC2_POD1 DC2-POD1-SPINE2 | All | Disabled |

#### SNMP Device Configuration

```eos
!
snmp-server location TWODC_5STAGE_CLOS DC2 DC2_POD1 DC2-POD1-SPINE2
```

## Spanning Tree

### Spanning Tree Summary

STP mode: **none**

### Spanning Tree Device Configuration

```eos
!
spanning-tree mode none
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

## Interfaces

### Ethernet Interfaces

#### Ethernet Interfaces Summary

##### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | Channel-Group |
| --------- | ----------- | ---- | ----- | ----------- | ----------- | ------------- |

*Inherited from Port-Channel Interface

##### IPv4

| Interface | Description | Channel Group | IP Address | VRF |  MTU | Shutdown | ACL In | ACL Out |
| --------- | ----------- | ------------- | ---------- | ----| ---- | -------- | ------ | ------- |
| Ethernet1 | P2P_LINK_TO_DC2-SUPER-SPINE1_Ethernet2 | - | 172.16.21.3/31 | default | - | False | - | - |
| Ethernet2 | P2P_LINK_TO_DC2-SUPER-SPINE2_Ethernet2 | - | 172.16.21.67/31 | default | - | False | - | - |
| Ethernet3 | P2P_LINK_TO_DC2-POD1-LEAF1A_Ethernet2 | - | 172.17.210.2/31 | default | - | False | - | - |
| Ethernet4 | P2P_LINK_TO_DC2-POD1-LEAF2A_Ethernet2 | - | 172.17.210.6/31 | default | - | False | - | - |
| Ethernet5 | P2P_LINK_TO_DC1-POD2-SPINE2_Ethernet4 | - | 200.200.200.201/24 | default | - | False | - | - |

#### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet1
   description P2P_LINK_TO_DC2-SUPER-SPINE1_Ethernet2
   no shutdown
   no switchport
   ip address 172.16.21.3/31
   ptp enable
   service-profile QOS-PROFILE
!
interface Ethernet2
   description P2P_LINK_TO_DC2-SUPER-SPINE2_Ethernet2
   no shutdown
   no switchport
   ip address 172.16.21.67/31
   ptp enable
   service-profile QOS-PROFILE
!
interface Ethernet3
   description P2P_LINK_TO_DC2-POD1-LEAF1A_Ethernet2
   no shutdown
   no switchport
   ip address 172.17.210.2/31
   ptp enable
   service-profile QOS-PROFILE
!
interface Ethernet4
   description P2P_LINK_TO_DC2-POD1-LEAF2A_Ethernet2
   no shutdown
   no switchport
   ip address 172.17.210.6/31
   ptp enable
   service-profile QOS-PROFILE
!
interface Ethernet5
   description P2P_LINK_TO_DC1-POD2-SPINE2_Ethernet4
   no shutdown
   no switchport
   ip address 200.200.200.201/24
   ptp enable
```

### Loopback Interfaces

#### Loopback Interfaces Summary

##### IPv4

| Interface | Description | VRF | IP Address |
| --------- | ----------- | --- | ---------- |
| Loopback0 | ROUTER_ID | default | 172.16.210.2/32 |

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
   ip address 172.16.210.2/32
```

## Routing

### Service Routing Protocols Model

Multi agent routing protocol model enabled

```eos
!
service routing protocols model multi-agent
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
| MGMT | 0.0.0.0/0 | 192.168.1.254 | - | 1 | - | - | - |

#### Static Routes Device Configuration

```eos
!
ip route vrf MGMT 0.0.0.0/0 192.168.1.254
```

### Router BGP

ASN Notation: asplain

#### Router BGP Summary

| BGP AS | Router ID |
| ------ | --------- |
| 65210 | 172.16.210.2 |

| BGP Tuning |
| ---------- |
| distance bgp 20 200 200 |
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

#### BGP Neighbors

| Neighbor | Remote AS | VRF | Shutdown | Send-community | Maximum-routes | Allowas-in | BFD | RIB Pre-Policy Retain | Route-Reflector Client | Passive | TTL Max Hops |
| -------- | --------- | --- | -------- | -------------- | -------------- | ---------- | --- | --------------------- | ---------------------- | ------- | ------------ |
| 172.16.21.2 | 65200 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - | - |
| 172.16.21.66 | 65200 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - | - |
| 172.17.210.3 | 65211 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - | - |
| 172.17.210.7 | 65212 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - | - |
| 200.200.200.101 | 65112 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | False | - | - | - | - |

#### Router BGP Device Configuration

```eos
!
router bgp 65210
   router-id 172.16.210.2
   maximum-paths 4 ecmp 4
   update wait-install
   no bgp default ipv4-unicast
   distance bgp 20 200 200
   neighbor IPv4-UNDERLAY-PEERS peer group
   neighbor IPv4-UNDERLAY-PEERS send-community
   neighbor IPv4-UNDERLAY-PEERS maximum-routes 12000
   neighbor 172.16.21.2 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.16.21.2 remote-as 65200
   neighbor 172.16.21.2 description DC2-SUPER-SPINE1_Ethernet2
   neighbor 172.16.21.66 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.16.21.66 remote-as 65200
   neighbor 172.16.21.66 description DC2-SUPER-SPINE2_Ethernet2
   neighbor 172.17.210.3 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.210.3 remote-as 65211
   neighbor 172.17.210.3 description DC2-POD1-LEAF1A_Ethernet2
   neighbor 172.17.210.7 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.210.7 remote-as 65212
   neighbor 172.17.210.7 description DC2-POD1-LEAF2A_Ethernet2
   neighbor 200.200.200.101 peer group IPv4-UNDERLAY-PEERS
   neighbor 200.200.200.101 remote-as 65112
   neighbor 200.200.200.101 description DC1-POD2-SPINE2
   no neighbor 200.200.200.101 bfd
   redistribute connected route-map RM-CONN-2-BGP
   !
   address-family ipv4
      neighbor IPv4-UNDERLAY-PEERS activate
```

## Filters

### Prefix-lists

#### Prefix-lists Summary

##### PL-LOOPBACKS-EVPN-OVERLAY

| Sequence | Action |
| -------- | ------ |
| 10 | permit 172.16.210.0/24 eq 32 |

#### Prefix-lists Device Configuration

```eos
!
ip prefix-list PL-LOOPBACKS-EVPN-OVERLAY
   seq 10 permit 172.16.210.0/24 eq 32
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

### VRF Instances Device Configuration

```eos
!
vrf instance MGMT
```

## EOS CLI Device Configuration

```eos
!
interface Loopback1009
  description Loopback created from raw_eos_cli under spine defaults in DC2 POD1

interface Loopback1111
  description Loopback created from raw_eos_cli under platform_settings vEOS-LAB

```
