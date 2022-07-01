# network-ports-tests.1
# Table of Contents

- [Management](#management)
  - [Management API HTTP](#management-api-http)
- [Authentication](#authentication)
- [Monitoring](#monitoring)
- [Internal VLAN Allocation Policy](#internal-vlan-allocation-policy)
  - [Internal VLAN Allocation Policy Summary](#internal-vlan-allocation-policy-summary)
  - [Internal VLAN Allocation Policy Configuration](#internal-vlan-allocation-policy-configuration)
- [Interfaces](#interfaces)
  - [Ethernet Interfaces](#ethernet-interfaces)
- [Routing](#routing)
  - [Service Routing Protocols Model](#service-routing-protocols-model)
  - [IP Routing](#ip-routing)
  - [IPv6 Routing](#ipv6-routing)
  - [Static Routes](#static-routes)
- [Multicast](#multicast)
  - [IP IGMP Snooping](#ip-igmp-snooping)
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
| Ethernet1 |  PCs | access | 100 | - | - | - |
| Ethernet2 |  PCs | access | 100 | - | - | - |
| Ethernet2/1 |  PCs | access | 100 | - | - | - |
| Ethernet2/2 |  PCs | access | 100 | - | - | - |
| Ethernet2/3 |  PCs | access | 100 | - | - | - |
| Ethernet2/4 |  PCs | access | 100 | - | - | - |
| Ethernet2/5 |  PCs | access | 100 | - | - | - |
| Ethernet2/6 |  PCs | access | 100 | - | - | - |
| Ethernet2/7 |  PCs | access | 100 | - | - | - |
| Ethernet2/8 |  PCs | access | 100 | - | - | - |
| Ethernet2/9 |  PCs | access | 100 | - | - | - |
| Ethernet2/10 |  PCs | access | 100 | - | - | - |
| Ethernet2/11 |  PCs | access | 100 | - | - | - |
| Ethernet2/12 |  PCs | access | 100 | - | - | - |
| Ethernet2/13 |  PCs | access | 100 | - | - | - |
| Ethernet2/14 |  PCs | access | 100 | - | - | - |
| Ethernet2/15 |  PCs | access | 100 | - | - | - |
| Ethernet2/16 |  PCs | access | 100 | - | - | - |
| Ethernet2/17 |  PCs | access | 100 | - | - | - |
| Ethernet2/18 |  PCs | access | 100 | - | - | - |
| Ethernet2/19 |  PCs | access | 100 | - | - | - |
| Ethernet2/20 |  PCs | access | 100 | - | - | - |
| Ethernet2/21 |  PCs | access | 100 | - | - | - |
| Ethernet2/22 |  PCs | access | 100 | - | - | - |
| Ethernet2/23 |  PCs | access | 100 | - | - | - |
| Ethernet2/24 |  PCs | access | 100 | - | - | - |
| Ethernet2/25 |  PCs | access | 100 | - | - | - |
| Ethernet2/26 |  PCs | access | 100 | - | - | - |
| Ethernet2/27 |  PCs | access | 100 | - | - | - |
| Ethernet2/28 |  PCs | access | 100 | - | - | - |
| Ethernet2/29 |  PCs | access | 100 | - | - | - |
| Ethernet2/30 |  PCs | access | 100 | - | - | - |
| Ethernet2/31 |  PCs | access | 100 | - | - | - |
| Ethernet2/32 |  PCs | access | 100 | - | - | - |
| Ethernet2/33 |  PCs | access | 100 | - | - | - |
| Ethernet2/34 |  PCs | access | 100 | - | - | - |
| Ethernet2/35 |  PCs | access | 100 | - | - | - |
| Ethernet2/36 |  PCs | access | 100 | - | - | - |
| Ethernet2/37 |  PCs | access | 100 | - | - | - |
| Ethernet2/38 |  PCs | access | 100 | - | - | - |
| Ethernet2/39 |  PCs | access | 100 | - | - | - |
| Ethernet2/40 |  PCs | access | 100 | - | - | - |
| Ethernet2/41 |  PCs | access | 100 | - | - | - |
| Ethernet2/42 |  PCs | access | 100 | - | - | - |
| Ethernet2/43 |  PCs | access | 100 | - | - | - |
| Ethernet2/44 |  PCs | access | 100 | - | - | - |
| Ethernet2/45 |  PCs | access | 100 | - | - | - |
| Ethernet2/46 |  PCs | access | 100 | - | - | - |
| Ethernet2/47 |  PCs | access | 100 | - | - | - |
| Ethernet2/48 |  PCs | access | 100 | - | - | - |
| Ethernet3 |  PCs | access | 100 | - | - | - |
| Ethernet4 |  PCs | access | 100 | - | - | - |

*Inherited from Port-Channel Interface

### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet1
   description PCs
   no shutdown
   switchport access vlan 100
   switchport mode access
   switchport
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet2
   description PCs
   no shutdown
   switchport access vlan 100
   switchport mode access
   switchport
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet2/1
   description PCs
   no shutdown
   switchport access vlan 100
   switchport mode access
   switchport
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet2/2
   description PCs
   no shutdown
   switchport access vlan 100
   switchport mode access
   switchport
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet2/3
   description PCs
   no shutdown
   switchport access vlan 100
   switchport mode access
   switchport
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet2/4
   description PCs
   no shutdown
   switchport access vlan 100
   switchport mode access
   switchport
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet2/5
   description PCs
   no shutdown
   switchport access vlan 100
   switchport mode access
   switchport
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet2/6
   description PCs
   no shutdown
   switchport access vlan 100
   switchport mode access
   switchport
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet2/7
   description PCs
   no shutdown
   switchport access vlan 100
   switchport mode access
   switchport
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet2/8
   description PCs
   no shutdown
   switchport access vlan 100
   switchport mode access
   switchport
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet2/9
   description PCs
   no shutdown
   switchport access vlan 100
   switchport mode access
   switchport
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet2/10
   description PCs
   no shutdown
   switchport access vlan 100
   switchport mode access
   switchport
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet2/11
   description PCs
   no shutdown
   switchport access vlan 100
   switchport mode access
   switchport
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet2/12
   description PCs
   no shutdown
   switchport access vlan 100
   switchport mode access
   switchport
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet2/13
   description PCs
   no shutdown
   switchport access vlan 100
   switchport mode access
   switchport
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet2/14
   description PCs
   no shutdown
   switchport access vlan 100
   switchport mode access
   switchport
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet2/15
   description PCs
   no shutdown
   switchport access vlan 100
   switchport mode access
   switchport
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet2/16
   description PCs
   no shutdown
   switchport access vlan 100
   switchport mode access
   switchport
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet2/17
   description PCs
   no shutdown
   switchport access vlan 100
   switchport mode access
   switchport
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet2/18
   description PCs
   no shutdown
   switchport access vlan 100
   switchport mode access
   switchport
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet2/19
   description PCs
   no shutdown
   switchport access vlan 100
   switchport mode access
   switchport
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet2/20
   description PCs
   no shutdown
   switchport access vlan 100
   switchport mode access
   switchport
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet2/21
   description PCs
   no shutdown
   switchport access vlan 100
   switchport mode access
   switchport
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet2/22
   description PCs
   no shutdown
   switchport access vlan 100
   switchport mode access
   switchport
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet2/23
   description PCs
   no shutdown
   switchport access vlan 100
   switchport mode access
   switchport
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet2/24
   description PCs
   no shutdown
   switchport access vlan 100
   switchport mode access
   switchport
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet2/25
   description PCs
   no shutdown
   switchport access vlan 100
   switchport mode access
   switchport
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet2/26
   description PCs
   no shutdown
   switchport access vlan 100
   switchport mode access
   switchport
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet2/27
   description PCs
   no shutdown
   switchport access vlan 100
   switchport mode access
   switchport
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet2/28
   description PCs
   no shutdown
   switchport access vlan 100
   switchport mode access
   switchport
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet2/29
   description PCs
   no shutdown
   switchport access vlan 100
   switchport mode access
   switchport
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet2/30
   description PCs
   no shutdown
   switchport access vlan 100
   switchport mode access
   switchport
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet2/31
   description PCs
   no shutdown
   switchport access vlan 100
   switchport mode access
   switchport
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet2/32
   description PCs
   no shutdown
   switchport access vlan 100
   switchport mode access
   switchport
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet2/33
   description PCs
   no shutdown
   switchport access vlan 100
   switchport mode access
   switchport
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet2/34
   description PCs
   no shutdown
   switchport access vlan 100
   switchport mode access
   switchport
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet2/35
   description PCs
   no shutdown
   switchport access vlan 100
   switchport mode access
   switchport
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet2/36
   description PCs
   no shutdown
   switchport access vlan 100
   switchport mode access
   switchport
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet2/37
   description PCs
   no shutdown
   switchport access vlan 100
   switchport mode access
   switchport
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet2/38
   description PCs
   no shutdown
   switchport access vlan 100
   switchport mode access
   switchport
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet2/39
   description PCs
   no shutdown
   switchport access vlan 100
   switchport mode access
   switchport
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet2/40
   description PCs
   no shutdown
   switchport access vlan 100
   switchport mode access
   switchport
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet2/41
   description PCs
   no shutdown
   switchport access vlan 100
   switchport mode access
   switchport
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet2/42
   description PCs
   no shutdown
   switchport access vlan 100
   switchport mode access
   switchport
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet2/43
   description PCs
   no shutdown
   switchport access vlan 100
   switchport mode access
   switchport
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet2/44
   description PCs
   no shutdown
   switchport access vlan 100
   switchport mode access
   switchport
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet2/45
   description PCs
   no shutdown
   switchport access vlan 100
   switchport mode access
   switchport
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet2/46
   description PCs
   no shutdown
   switchport access vlan 100
   switchport mode access
   switchport
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet2/47
   description PCs
   no shutdown
   switchport access vlan 100
   switchport mode access
   switchport
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet2/48
   description PCs
   no shutdown
   switchport access vlan 100
   switchport mode access
   switchport
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet3
   description PCs
   no shutdown
   switchport access vlan 100
   switchport mode access
   switchport
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet4
   description PCs
   no shutdown
   switchport access vlan 100
   switchport mode access
   switchport
   spanning-tree portfast
   spanning-tree bpdufilter enable
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
| MGMT | 0.0.0.0/0 | 192.168.0.1 | - | 1 | - | - | - |

### Static Routes Device Configuration

```eos
!
ip route vrf MGMT 0.0.0.0/0 192.168.0.1
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
