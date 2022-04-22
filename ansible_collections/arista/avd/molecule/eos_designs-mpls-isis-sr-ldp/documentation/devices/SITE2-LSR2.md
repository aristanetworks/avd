# SITE2-LSR2
# Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
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
- [EOS CLI](#eos-cli)

# Management

## Management Interfaces

### Management Interfaces Summary

#### IPv4

| Management Interface | description | Type | VRF | IP Address | Gateway |
| -------------------- | ----------- | ---- | --- | ---------- | ------- |
| Management1 | oob_management | oob | MGMT | 192.168.200.104/24 | 192.168.200.5 |

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
   ip address 192.168.200.104/24
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
| Ethernet3 | P2P_LINK_TO_SITE1-LSR2_Ethernet3 | routed | - | 100.64.48.11/31 | default | 9178 | false | - | - |
| Ethernet12 | P2P_LINK_TO_SITE2-LER1_Port-Channel11 | *routed | 12 | *100.64.48.16/31 | **default | *9178 | *false | **- | **- |
| Ethernet13 | P2P_LINK_TO_SITE2-LER1_Port-Channel11 | *routed | 12 | *100.64.48.16/31 | **default | *9178 | *false | **- | **- |
*Inherited from Port-Channel Interface

#### IPv6

| Interface | Description | Type | Channel Group | IPv6 Address | VRF | MTU | Shutdown | ND RA Disabled | Managed Config Flag | IPv6 ACL In | IPv6 ACL Out |
| --------- | ----------- | ---- | --------------| ------------ | --- | --- | -------- | -------------- | -------------------| ----------- | ------------ |
| Ethernet3 | P2P_LINK_TO_SITE1-LSR2_Ethernet3 | routed | - | - | default | 9178 | false | - | - | - | - |
| Ethernet12 | P2P_LINK_TO_SITE2-LER1_Port-Channel11 | *routed | 12 | *- | *default | *9178 | *false | *- | *- | *- | *- |
| Ethernet13 | P2P_LINK_TO_SITE2-LER1_Port-Channel11 | *routed | 12 | *- | *default | *9178 | *false | *- | *- | *- | *- |
 *Inherited from Port-Channel Interface

#### ISIS

| Interface | Channel Group | ISIS Instance | ISIS Metric | Mode | ISIS Circuit Type | Hello Padding | Authentication Mode |
| --------- | ------------- | ------------- | ----------- | ---- | ----------------- | ------------- | ------------------- |
| Ethernet3 | - | CUSTOM_NAME | 60 | point-to-point | level-2 | False | md5 |
| Ethernet12 | 12 | *CUSTOM_NAME | *60 | *point-to-point | *level-2 | *False | *md5 |
| Ethernet13 | 12 | *CUSTOM_NAME | *60 | *point-to-point | *level-2 | *False | *md5 |
 *Inherited from Port-Channel Interface

### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet3
   description P2P_LINK_TO_SITE1-LSR2_Ethernet3
   no shutdown
   mtu 9178
   speed forced 40gfull
   no switchport
   ip address 100.64.48.11/31
   ipv6 enable
   mpls ldp igp sync
   mpls ldp interface
   mpls ip
   isis enable CUSTOM_NAME
   isis circuit-type level-2
   isis metric 60
   no isis hello padding
   isis network point-to-point
   isis authentication mode md5
   isis authentication key 7 asdadjiwtelogkkdng
!
interface Ethernet12
   description P2P_LINK_TO_SITE2-LER1_Port-Channel11
   no shutdown
   channel-group 12 mode active
!
interface Ethernet13
   description P2P_LINK_TO_SITE2-LER1_Port-Channel11
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
| Port-Channel12 | P2P_LINK_TO_SITE2-LER1_Port-Channel11 | routed | - | 100.64.48.16/31 | default | 9178 | false | - | - |

#### ISIS

| Interface | ISIS Instance | ISIS Metric | Mode | ISIS Circuit Type | Hello Padding | Authentication Mode |
| --------- | ------------- | ----------- | ---- | ----------------- | ------------- | ------------------- |
| Port-Channel12 | CUSTOM_NAME | 60 | point-to-point | level-2 | False | md5 |

### Port-Channel Interfaces Device Configuration

```eos
!
interface Port-Channel12
   description P2P_LINK_TO_SITE2-LER1_Port-Channel11
   no shutdown
   mtu 9178
   no switchport
   ip address 100.64.48.16/31
   ipv6 enable
   mpls ip
   mpls ldp interface
   mpls ldp igp sync
   isis enable CUSTOM_NAME
   isis circuit-type level-2
   isis metric 60
   isis network point-to-point
   no isis hello padding
   isis authentication mode md5
   isis authentication key 7 asdadjiwtelogkkdng
```

## Loopback Interfaces

### Loopback Interfaces Summary

#### IPv4

| Interface | Description | VRF | IP Address |
| --------- | ----------- | --- | ---------- |
| Loopback0 | LSR_Router_ID | default | 100.70.0.4/32 |

#### IPv6

| Interface | Description | VRF | IPv6 Address |
| --------- | ----------- | --- | ------------ |
| Loopback0 | LSR_Router_ID | default | 2000:1234:ffff:ffff::4/128 |

#### ISIS

| Interface | ISIS instance | ISIS metric | Interface mode |
| --------- | ------------- | ----------- | -------------- |
| Loopback0 | CUSTOM_NAME | - | passive |

### Loopback Interfaces Device Configuration

```eos
!
interface Loopback0
   description LSR_Router_ID
   no shutdown
   ip address 100.70.0.4/32
   ipv6 address 2000:1234:ffff:ffff::4/128
   isis enable CUSTOM_NAME
   isis passive
   mpls ldp interface
   node-segment ipv4 index 304
   node-segment ipv6 index 304
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
| Instance | CUSTOM_NAME |
| Net-ID | 49.0001.0000.0000.0004.00 |
| Type | level-2 |
| Address Family | ipv4 unicast, ipv6 unicast |
| Router-ID | 100.70.0.4 |
| Log Adjacency Changes | True |
| MPLS LDP Sync Default | True |
| Local Convergence Delay (ms) | 15000 |
| Advertise Passive-only | True |
| SR MPLS Enabled | True |

### ISIS Interfaces Summary

| Interface | ISIS Instance | ISIS Metric | Interface Mode |
| --------- | ------------- | ----------- | -------------- |
| Ethernet3 | CUSTOM_NAME | 60 | point-to-point |
| Loopback0 | CUSTOM_NAME | - | passive |

### ISIS Segment-routing Node-SID

| Loopback | IPv4 Index | IPv6 Index |
| -------- | ---------- | ---------- |
| Loopback0 | 304 | 304 |

### Router ISIS Device Configuration

```eos
!
router isis CUSTOM_NAME
   net 49.0001.0000.0000.0004.00
   is-type level-2
   router-id ipv4 100.70.0.4
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
| LDP Router ID | 100.70.0.4 |
| LDP Interface Disabled Default | True |
| LDP Transport-Address Interface | Loopback0 |

### MPLS and LDP Configuration

```eos
!
mpls ip
!
mpls ldp
   interface disabled default
   router-id 100.70.0.4
   no shutdown
   transport-address interface Loopback0
```

## MPLS Interfaces

| Interface | MPLS IP Enabled | LDP Enabled | IGP Sync |
| --------- | --------------- | ----------- | -------- |
| Ethernet3 | True | True | True |
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

# EOS CLI

```eos
!
management security
   password encryption-key common

```
