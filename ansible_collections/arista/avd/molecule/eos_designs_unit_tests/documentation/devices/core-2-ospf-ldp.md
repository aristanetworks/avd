# core-2-ospf-ldp
# Table of Contents

- [Management](#management)
  - [Management API HTTP](#management-api-http)
- [Authentication](#authentication)
- [Monitoring](#monitoring)
- [Spanning Tree](#spanning-tree)
  - [Spanning Tree Summary](#spanning-tree-summary)
  - [Spanning Tree Device Configuration](#spanning-tree-device-configuration)
- [Internal VLAN Allocation Policy](#internal-vlan-allocation-policy)
  - [Internal VLAN Allocation Policy Summary](#internal-vlan-allocation-policy-summary)
  - [Internal VLAN Allocation Policy Configuration](#internal-vlan-allocation-policy-configuration)
- [Interfaces](#interfaces)
  - [Ethernet Interfaces](#ethernet-interfaces)
  - [Port-Channel Interfaces](#port-channel-interfaces)
  - [Loopback Interfaces](#loopback-interfaces)
- [Routing](#routing)
  - [Service Routing Protocols Model](#service-routing-protocols-model)
  - [IP Routing](#ip-routing)
  - [IPv6 Routing](#ipv6-routing)
  - [Static Routes](#static-routes)
  - [Router OSPF](#router-ospf)
- [MPLS](#mpls)
  - [MPLS and LDP](#mpls-and-ldp)
  - [MPLS Interfaces](#mpls-interfaces)
- [Multicast](#multicast)
- [Filters](#filters)
- [ACL](#acl)
- [VRF Instances](#vrf-instances)
  - [VRF Instances Summary](#vrf-instances-summary)
  - [VRF Instances Device Configuration](#vrf-instances-device-configuration)
- [Quality Of Service](#quality-of-service)

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

# Monitoring

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
| Ethernet1 | P2P_LINK_TO_core-1-isis-sr-ldp_Ethernet1 | routed | - | unnumbered loopback0 | default | 1500 | false | - | - |
| Ethernet2 | P2P_LINK_TO_core-1-isis-sr-ldp_Ethernet2 | routed | - | 100.123.123.3/31 | default | 1601 | false | - | - |
| Ethernet3 | P2P_LINK_TO_core-1-isis-sr-ldp_Ethernet3 | routed | - | 100.64.48.5/31 | default | 1500 | false | - | - |
| Ethernet4 | P2P_LINK_TO_core-1-isis-sr-ldp_Ethernet4 | routed | - | 100.64.48.7/31 | default | 1500 | false | - | - |
| Ethernet5 | P2P_LINK_TO_core-1-isis-sr-ldp_Ethernet5 | routed | - | 100.64.48.9/31 | default | 1500 | false | - | - |
| Ethernet6 | P2P_LINK_TO_core-1-isis-sr-ldp_Ethernet6 | routed | - | unnumbered loopback0 | default | 1602 | false | - | - |
| Ethernet10 | P2P_LINK_TO_core-1-isis-sr-ldp_Ethernet10 | routed | - | 100.64.48.13/31 | default | 1500 | false | - | - |
| Ethernet12 | P2P_LINK_TO_core-1-isis-sr-ldp_Port-Channel12 | *routed | 12 | *100.64.48.17/31 | **default | *1500 | *false | **- | **- |
| Ethernet13 | P2P_LINK_TO_core-1-isis-sr-ldp_Port-Channel12 | *routed | 12 | *100.64.48.17/31 | **default | *1500 | *false | **- | **- |
*Inherited from Port-Channel Interface

#### IPv6

| Interface | Description | Type | Channel Group | IPv6 Address | VRF | MTU | Shutdown | ND RA Disabled | Managed Config Flag | IPv6 ACL In | IPv6 ACL Out |
| --------- | ----------- | ---- | --------------| ------------ | --- | --- | -------- | -------------- | -------------------| ----------- | ------------ |
| Ethernet1 | P2P_LINK_TO_core-1-isis-sr-ldp_Ethernet1 | routed | - | - | default | 1500 | false | - | - | - | - |
| Ethernet3 | P2P_LINK_TO_core-1-isis-sr-ldp_Ethernet3 | routed | - | - | default | 1500 | false | - | - | - | - |
| Ethernet4 | P2P_LINK_TO_core-1-isis-sr-ldp_Ethernet4 | routed | - | - | default | 1500 | false | - | - | - | - |
| Ethernet5 | P2P_LINK_TO_core-1-isis-sr-ldp_Ethernet5 | routed | - | - | default | 1500 | false | - | - | - | - |
| Ethernet6 | P2P_LINK_TO_core-1-isis-sr-ldp_Ethernet6 | routed | - | - | default | 1602 | false | - | - | - | - |
| Ethernet12 | P2P_LINK_TO_core-1-isis-sr-ldp_Port-Channel12 | *routed | 12 | *- | *default | *1500 | *false | *- | *- | *- | *- |
| Ethernet13 | P2P_LINK_TO_core-1-isis-sr-ldp_Port-Channel12 | *routed | 12 | *- | *default | *1500 | *false | *- | *- | *- | *- |
 *Inherited from Port-Channel Interface

### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet1
   description P2P_LINK_TO_core-1-isis-sr-ldp_Ethernet1
   no shutdown
   mtu 1500
   speed forced 1000full
   no switchport
   ip address unnumbered loopback0
   ipv6 enable
   mpls ldp igp sync
   mpls ldp interface
   mpls ip
   ip ospf network point-to-point
   ip ospf area 0.0.0.0
!
interface Ethernet2
   description P2P_LINK_TO_core-1-isis-sr-ldp_Ethernet2
   no shutdown
   mtu 1601
   speed 100full
   no switchport
   ip address 100.123.123.3/31
   mpls ldp igp sync
   mpls ldp interface
   mpls ip
   ip ospf network point-to-point
   ip ospf area 0.0.0.0
   service-profile test_qos_profile
!
interface Ethernet3
   description P2P_LINK_TO_core-1-isis-sr-ldp_Ethernet3
   no shutdown
   mtu 1500
   speed forced 1000full
   no switchport
   ip address 100.64.48.5/31
   ipv6 enable
   mpls ldp igp sync
   mpls ldp interface
   mpls ip
   ip ospf network point-to-point
   ip ospf area 0.0.0.0
!
interface Ethernet4
   description P2P_LINK_TO_core-1-isis-sr-ldp_Ethernet4
   no shutdown
   mtu 1500
   speed forced 1000full
   no switchport
   ip address 100.64.48.7/31
   ipv6 enable
   ip ospf network point-to-point
   ip ospf area 0.0.0.0
!
interface Ethernet5
   description P2P_LINK_TO_core-1-isis-sr-ldp_Ethernet5
   no shutdown
   mtu 1500
   speed forced 1000full
   no switchport
   ip address 100.64.48.9/31
   ipv6 enable
   mpls ip
   ip ospf network point-to-point
   ip ospf area 0.0.0.0
!
interface Ethernet6
   description P2P_LINK_TO_core-1-isis-sr-ldp_Ethernet6
   no shutdown
   mtu 1602
   speed 100full
   no switchport
   ip address unnumbered loopback0
   ipv6 enable
   mpls ldp igp sync
   mpls ldp interface
   mpls ip
   ip ospf network point-to-point
   ip ospf area 0.0.0.0
   service-profile test_qos_profile
!
interface Ethernet10
   description P2P_LINK_TO_core-1-isis-sr-ldp_Ethernet10
   no shutdown
   mtu 1500
   speed forced 1000full
   no switchport
   ip address 100.64.48.13/31
   mpls ldp igp sync
   mpls ldp interface
   mpls ip
   ip ospf network point-to-point
   ip ospf area 0.0.0.0
!
interface Ethernet12
   description P2P_LINK_TO_core-1-isis-sr-ldp_Port-Channel12
   no shutdown
   channel-group 12 mode active
!
interface Ethernet13
   description P2P_LINK_TO_core-1-isis-sr-ldp_Port-Channel12
   no shutdown
   channel-group 12 mode active
```

## Port-Channel Interfaces

### Port-Channel Interfaces Summary

#### L2

| Interface | Description | Type | Mode | VLANs | Native VLAN | Trunk Group | LACP Fallback Timeout | LACP Fallback Mode | MLAG ID | EVPN ESI |
| --------- | ----------- | ---- | ---- | ----- | ----------- | ------------| --------------------- | ------------------ | ------- | -------- |

#### IPv4

| Interface | Description | Type | MLAG ID | IP Address | VRF | MTU | Shutdown | ACL In | ACL Out |
| --------- | ----------- | ---- | ------- | ---------- | --- | --- | -------- | ------ | ------- |
| Port-Channel12 | P2P_LINK_TO_core-1-isis-sr-ldp_Port-Channel12 | routed | - | 100.64.48.17/31 | default | 1500 | false | - | - |

### Port-Channel Interfaces Device Configuration

```eos
!
interface Port-Channel12
   description P2P_LINK_TO_core-1-isis-sr-ldp_Port-Channel12
   no shutdown
   mtu 1500
   no switchport
   ip address 100.64.48.17/31
   ipv6 enable
   ip ospf network point-to-point
   ip ospf area 0.0.0.0
   mpls ip
   mpls ldp interface
   mpls ldp igp sync
```

## Loopback Interfaces

### Loopback Interfaces Summary

#### IPv4

| Interface | Description | VRF | IP Address |
| --------- | ----------- | --- | ---------- |
| Loopback0 | LSR_Router_ID | default | 10.0.0.2/32 |

#### IPv6

| Interface | Description | VRF | IPv6 Address |
| --------- | ----------- | --- | ------------ |
| Loopback0 | LSR_Router_ID | default | 2000:1234:ffff:ffff::2/128 |


### Loopback Interfaces Device Configuration

```eos
!
interface Loopback0
   description LSR_Router_ID
   no shutdown
   ip address 10.0.0.2/32
   ipv6 address 2000:1234:ffff:ffff::2/128
   ip ospf area 0.0.0.0
   mpls ldp interface
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
| default | true |
| MGMT | false |

### IPv6 Routing Device Configuration

```eos
!
ipv6 unicast-routing
```

## Static Routes

### Static Routes Summary

| VRF | Destination Prefix | Next Hop IP             | Exit interface      | Administrative Distance       | Tag               | Route Name                    | Metric         |
| --- | ------------------ | ----------------------- | ------------------- | ----------------------------- | ----------------- | ----------------------------- | -------------- |
| MGMT | 0.0.0.0/0 | 192.168.0.1 | - | 1 | - | - | - |

### Static Routes Device Configuration

```eos
!
ip route vrf MGMT 0.0.0.0/0 192.168.0.1
```

## Router OSPF

### Router OSPF Summary

| Process ID | Router ID | Default Passive Interface | No Passive Interface | BFD | Max LSA | Default Information Originate | Log Adjacency Changes Detail | Auto Cost Reference Bandwidth | Maximum Paths | MPLS LDP Sync Default | Distribute List In |
| ---------- | --------- | ------------------------- | -------------------- | --- | ------- | ----------------------------- | ---------------------------- | ----------------------------- | ------------- | --------------------- | ------------------ |
| 101 | 10.0.0.2 | enabled | Ethernet1 <br> Ethernet2 <br> Ethernet3 <br> Ethernet4 <br> Ethernet5 <br> Ethernet6 <br> Ethernet10 <br> Port-Channel12 <br> | enabled | 12000 | disabled | disabled | - | - | - | - |

### OSPF Interfaces

| Interface | Area | Cost | Point To Point |
| -------- | -------- | -------- | -------- |
| Ethernet1 | 0.0.0.0 | - | True |
| Ethernet2 | 0.0.0.0 | - | True |
| Ethernet3 | 0.0.0.0 | - | True |
| Ethernet4 | 0.0.0.0 | - | True |
| Ethernet5 | 0.0.0.0 | - | True |
| Ethernet6 | 0.0.0.0 | - | True |
| Ethernet10 | 0.0.0.0 | - | True |
| Port-Channel12 | 0.0.0.0 | - | True |
| Loopback0 | 0.0.0.0 | - | - |

### Router OSPF Device Configuration

```eos
!
router ospf 101
   router-id 10.0.0.2
   passive-interface default
   no passive-interface Ethernet1
   no passive-interface Ethernet2
   no passive-interface Ethernet3
   no passive-interface Ethernet4
   no passive-interface Ethernet5
   no passive-interface Ethernet6
   no passive-interface Ethernet10
   no passive-interface Port-Channel12
   bfd default
   max-lsa 12000
```

# MPLS

## MPLS and LDP

### MPLS and LDP Summary

| Setting | Value |
| -------- | ---- |
| MPLS IP Enabled | True |
| LDP Enabled | True |
| LDP Router ID | 10.0.0.2 |
| LDP Interface Disabled Default | True |
| LDP Transport-Address Interface | Loopback0 |

### MPLS and LDP Configuration

```eos
!
mpls ip
!
mpls ldp
   interface disabled default
   router-id 10.0.0.2
   no shutdown
   transport-address interface Loopback0
```

## MPLS Interfaces

| Interface | MPLS IP Enabled | LDP Enabled | IGP Sync |
| --------- | --------------- | ----------- | -------- |
| Ethernet1 | True | True | True |
| Ethernet2 | True | True | True |
| Ethernet3 | True | True | True |
| Ethernet5 | True | - | - |
| Ethernet6 | True | True | True |
| Ethernet10 | True | True | True |
| Loopback0 | - | True | - |
| Port-Channel12 | True | True | True |

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
