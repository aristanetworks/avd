# core-1-isis-sr-ldp
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
  - [Router ISIS](#router-isis)
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
| Ethernet1 | P2P_LINK_TO_core-2-ospf-ldp_Ethernet1 | routed | - | unnumbered loopback0 | default | 1500 | false | - | - |
| Ethernet2 | P2P_LINK_TO_core-2-ospf-ldp_Ethernet2 | routed | - | 100.123.123.2/31 | default | 1601 | false | - | - |
| Ethernet3 | P2P_LINK_TO_core-2-ospf-ldp_Ethernet3 | routed | - | 100.64.48.4/31 | default | 1500 | false | - | - |
| Ethernet4 | P2P_LINK_TO_core-2-ospf-ldp_Ethernet4 | routed | - | 100.64.48.6/31 | default | 1500 | false | - | - |
| Ethernet5 | P2P_LINK_TO_core-2-ospf-ldp_Ethernet5 | routed | - | 100.64.48.8/31 | default | 1500 | false | - | - |
| Ethernet6 | P2P_LINK_TO_core-2-ospf-ldp_Ethernet6 | routed | - | unnumbered loopback0 | default | 1602 | false | - | - |
| Ethernet10 | P2P_LINK_TO_core-2-ospf-ldp_Ethernet10 | routed | - | 100.64.48.12/31 | default | 1500 | false | - | - |
| Ethernet12 | P2P_LINK_TO_core-2-ospf-ldp_Port-Channel12 | *routed | 12 | *100.64.48.16/31 | **default | *1500 | *false | **- | **- |
| Ethernet13 | P2P_LINK_TO_core-2-ospf-ldp_Port-Channel12 | *routed | 12 | *100.64.48.16/31 | **default | *1500 | *false | **- | **- |
*Inherited from Port-Channel Interface

#### IPv6

| Interface | Description | Type | Channel Group | IPv6 Address | VRF | MTU | Shutdown | ND RA Disabled | Managed Config Flag | IPv6 ACL In | IPv6 ACL Out |
| --------- | ----------- | ---- | --------------| ------------ | --- | --- | -------- | -------------- | -------------------| ----------- | ------------ |
| Ethernet1 | P2P_LINK_TO_core-2-ospf-ldp_Ethernet1 | routed | - | - | default | 1500 | false | - | - | - | - |
| Ethernet3 | P2P_LINK_TO_core-2-ospf-ldp_Ethernet3 | routed | - | - | default | 1500 | false | - | - | - | - |
| Ethernet4 | P2P_LINK_TO_core-2-ospf-ldp_Ethernet4 | routed | - | - | default | 1500 | false | - | - | - | - |
| Ethernet5 | P2P_LINK_TO_core-2-ospf-ldp_Ethernet5 | routed | - | - | default | 1500 | false | - | - | - | - |
| Ethernet6 | P2P_LINK_TO_core-2-ospf-ldp_Ethernet6 | routed | - | - | default | 1602 | false | - | - | - | - |
| Ethernet12 | P2P_LINK_TO_core-2-ospf-ldp_Port-Channel12 | *routed | 12 | *- | *default | *1500 | *false | *- | *- | *- | *- |
| Ethernet13 | P2P_LINK_TO_core-2-ospf-ldp_Port-Channel12 | *routed | 12 | *- | *default | *1500 | *false | *- | *- | *- | *- |
 *Inherited from Port-Channel Interface

#### ISIS

| Interface | Channel Group | ISIS Instance | ISIS Metric | Mode | ISIS Circuit Type | Hello Padding | Authentication Mode |
| --------- | ------------- | ------------- | ----------- | ---- | ----------------- | ------------- | ------------------- |
| Ethernet1 | - | CORE | 60 | point-to-point | level-2 | False | md5 |
| Ethernet2 | - | CORE | 60 | point-to-point | level-1 | True | - |
| Ethernet3 | - | CORE | 60 | point-to-point | level-2 | False | md5 |
| Ethernet4 | - | CORE | 60 | point-to-point | level-2 | False | md5 |
| Ethernet5 | - | CORE | 60 | point-to-point | level-2 | False | md5 |
| Ethernet6 | - | CORE | 70 | point-to-point | level-1-2 | True | md5 |
| Ethernet10 | - | CORE | 50 | point-to-point | level-2 | True | - |
| Ethernet12 | 12 | *CORE | *60 | *point-to-point | *level-2 | *False | *md5 |
| Ethernet13 | 12 | *CORE | *60 | *point-to-point | *level-2 | *False | *md5 |
 *Inherited from Port-Channel Interface

### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet1
   description P2P_LINK_TO_core-2-ospf-ldp_Ethernet1
   no shutdown
   mtu 1500
   speed forced 1000full
   no switchport
   ip address unnumbered loopback0
   ipv6 enable
   mpls ldp igp sync
   mpls ldp interface
   mpls ip
   isis enable CORE
   isis circuit-type level-2
   isis metric 60
   no isis hello padding
   isis network point-to-point
   isis authentication mode md5
   isis authentication key 7 $1c$sTNAlR6rKSw=
!
interface Ethernet2
   description P2P_LINK_TO_core-2-ospf-ldp_Ethernet2
   no shutdown
   mtu 1601
   speed 100full
   no switchport
   ip address 100.123.123.2/31
   mpls ldp igp sync
   mpls ldp interface
   mpls ip
   service-profile test_qos_profile
   isis enable CORE
   isis circuit-type level-1
   isis metric 60
   isis hello padding
   isis network point-to-point
!
interface Ethernet3
   description P2P_LINK_TO_core-2-ospf-ldp_Ethernet3
   no shutdown
   mtu 1500
   speed forced 1000full
   no switchport
   ip address 100.64.48.4/31
   ipv6 enable
   mpls ldp igp sync
   mpls ldp interface
   mpls ip
   isis enable CORE
   isis circuit-type level-2
   isis metric 60
   no isis hello padding
   isis network point-to-point
   isis authentication mode md5
   isis authentication key 7 $1c$sTNAlR6rKSw=
!
interface Ethernet4
   description P2P_LINK_TO_core-2-ospf-ldp_Ethernet4
   no shutdown
   mtu 1500
   speed forced 1000full
   no switchport
   ip address 100.64.48.6/31
   ipv6 enable
   isis enable CORE
   isis circuit-type level-2
   isis metric 60
   no isis hello padding
   isis network point-to-point
   isis authentication mode md5
   isis authentication key 7 $1c$sTNAlR6rKSw=
!
interface Ethernet5
   description P2P_LINK_TO_core-2-ospf-ldp_Ethernet5
   no shutdown
   mtu 1500
   speed forced 1000full
   no switchport
   ip address 100.64.48.8/31
   ipv6 enable
   mpls ip
   isis enable CORE
   isis circuit-type level-2
   isis metric 60
   no isis hello padding
   isis network point-to-point
   isis authentication mode md5
   isis authentication key 7 $1c$sTNAlR6rKSw=
!
interface Ethernet6
   description P2P_LINK_TO_core-2-ospf-ldp_Ethernet6
   no shutdown
   mtu 1602
   speed 100full
   no switchport
   ip address unnumbered loopback0
   ipv6 enable
   mpls ldp igp sync
   mpls ldp interface
   mpls ip
   service-profile test_qos_profile
   isis enable CORE
   isis circuit-type level-1-2
   isis metric 70
   isis hello padding
   isis network point-to-point
   isis authentication mode md5
   isis authentication key 7 $1c$sTNAlR6rKSw=
!
interface Ethernet10
   description P2P_LINK_TO_core-2-ospf-ldp_Ethernet10
   no shutdown
   mtu 1500
   speed forced 1000full
   no switchport
   ip address 100.64.48.12/31
   mpls ldp igp sync
   mpls ldp interface
   mpls ip
   isis enable CORE
   isis circuit-type level-2
   isis metric 50
   isis hello padding
   isis network point-to-point
!
interface Ethernet12
   description P2P_LINK_TO_core-2-ospf-ldp_Port-Channel12
   no shutdown
   channel-group 12 mode active
!
interface Ethernet13
   description P2P_LINK_TO_core-2-ospf-ldp_Port-Channel12
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
| Port-Channel12 | P2P_LINK_TO_core-2-ospf-ldp_Port-Channel12 | routed | - | 100.64.48.16/31 | default | 1500 | false | - | - |

#### ISIS

| Interface | ISIS Instance | ISIS Metric | Mode | ISIS Circuit Type | Hello Padding | Authentication Mode |
| --------- | ------------- | ----------- | ---- | ----------------- | ------------- | ------------------- |
| Port-Channel12 | CORE | 60 | point-to-point | level-2 | False | md5 |

### Port-Channel Interfaces Device Configuration

```eos
!
interface Port-Channel12
   description P2P_LINK_TO_core-2-ospf-ldp_Port-Channel12
   no shutdown
   mtu 1500
   no switchport
   ip address 100.64.48.16/31
   ipv6 enable
   mpls ip
   mpls ldp interface
   mpls ldp igp sync
   isis enable CORE
   isis circuit-type level-2
   isis metric 60
   isis network point-to-point
   no isis hello padding
   isis authentication mode md5
   isis authentication key 7 $1c$sTNAlR6rKSw=
```

## Loopback Interfaces

### Loopback Interfaces Summary

#### IPv4

| Interface | Description | VRF | IP Address |
| --------- | ----------- | --- | ---------- |
| Loopback0 | LSR_Router_ID | default | 10.0.0.1/32 |

#### IPv6

| Interface | Description | VRF | IPv6 Address |
| --------- | ----------- | --- | ------------ |
| Loopback0 | LSR_Router_ID | default | 2000:1234:ffff:ffff::1/128 |

#### ISIS

| Interface | ISIS instance | ISIS metric | Interface mode |
| --------- | ------------- | ----------- | -------------- |
| Loopback0 | CORE | - | passive |

### Loopback Interfaces Device Configuration

```eos
!
interface Loopback0
   description LSR_Router_ID
   no shutdown
   ip address 10.0.0.1/32
   ipv6 address 2000:1234:ffff:ffff::1/128
   isis enable CORE
   isis passive
   mpls ldp interface
   node-segment ipv4 index 201
   node-segment ipv6 index 201
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

## Router ISIS

### Router ISIS Summary

| Settings | Value |
| -------- | ----- |
| Instance | CORE |
| Net-ID | 49.0001.0000.0001.0001.00 |
| Type | level-2 |
| Address Family | ipv4 unicast, ipv6 unicast |
| Router-ID | 10.0.0.1 |
| Log Adjacency Changes | True |
| MPLS LDP Sync Default | True |
| Local Convergence Delay (ms) | 15000 |
| Advertise Passive-only | True |
| SR MPLS Enabled | True |

### ISIS Interfaces Summary

| Interface | ISIS Instance | ISIS Metric | Interface Mode |
| --------- | ------------- | ----------- | -------------- |
| Ethernet1 | CORE | 60 | point-to-point |
| Ethernet2 | CORE | 60 | point-to-point |
| Ethernet3 | CORE | 60 | point-to-point |
| Ethernet4 | CORE | 60 | point-to-point |
| Ethernet5 | CORE | 60 | point-to-point |
| Ethernet6 | CORE | 70 | point-to-point |
| Ethernet10 | CORE | 50 | point-to-point |
| Loopback0 | CORE | - | passive |

### ISIS Segment-routing Node-SID

| Loopback | IPv4 Index | IPv6 Index |
| -------- | ---------- | ---------- |
| Loopback0 | 201 | 201 |

### Router ISIS Device Configuration

```eos
!
router isis CORE
   net 49.0001.0000.0001.0001.00
   is-type level-2
   router-id ipv4 10.0.0.1
   log-adjacency-changes
   mpls ldp sync default
   timers local-convergence-delay 15000 protected-prefixes
   advertise passive-only
   !
   address-family ipv4 unicast
      maximum-paths 4
      fast-reroute ti-lfa mode link-protection
   address-family ipv6 unicast
      maximum-paths 4
      fast-reroute ti-lfa mode link-protection
   !
   segment-routing mpls
      no shutdown
```

# MPLS

## MPLS and LDP

### MPLS and LDP Summary

| Setting | Value |
| -------- | ---- |
| MPLS IP Enabled | True |
| LDP Enabled | True |
| LDP Router ID | 10.0.0.1 |
| LDP Interface Disabled Default | True |
| LDP Transport-Address Interface | Loopback0 |

### MPLS and LDP Configuration

```eos
!
mpls ip
!
mpls ldp
   interface disabled default
   router-id 10.0.0.1
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
