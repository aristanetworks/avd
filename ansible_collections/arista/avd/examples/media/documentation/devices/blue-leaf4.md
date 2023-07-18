# blue-leaf4
# Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
  - [PTP](#ptp)
  - [Management API HTTP](#management-api-http)
- [Authentication](#authentication)
  - [Local Users](#local-users)
- [Monitoring](#monitoring)
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
  - [Loopback Interfaces](#loopback-interfaces)
  - [VLAN Interfaces](#vlan-interfaces)
- [Routing](#routing)
  - [Service Routing Protocols Model](#service-routing-protocols-model)
  - [Virtual Router MAC Address](#virtual-router-mac-address)
  - [IP Routing](#ip-routing)
  - [IPv6 Routing](#ipv6-routing)
  - [Static Routes](#static-routes)
  - [Router BGP](#router-bgp)
- [Multicast](#multicast)
  - [IP IGMP Snooping](#ip-igmp-snooping)
  - [Router Multicast](#router-multicast)
  - [PIM Sparse Mode](#pim-sparse-mode)
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
| Management1 | oob_management | oob | MGMT | 192.168.0.22/24 | 192.168.0.1 |

#### IPv6

| Management Interface | description | Type | VRF | IPv6 Address | IPv6 Gateway |
| -------------------- | ----------- | ---- | --- | ------------ | ------------ |
| Management1 | oob_management | oob | MGMT | - | - |

### Management Interfaces Device Configuration

```eos
!
interface Management1
   description oob_management
   no shutdown
   vrf MGMT
   ip address 192.168.0.22/24
```

## PTP

### PTP Summary

| Clock ID | Source IP | Priority 1 | Priority 2 | TTL | Domain | Mode | Forward Unicast |
| -------- | --------- | ---------- | ---------- | --- | ------ | ---- | --------------- |
| 00:1C:73:1e:00:04 | - | 30 | 4 | - | 127 | boundary | - |

### PTP Device Configuration

```eos
!
ptp clock-identity 00:1C:73:1e:00:04
ptp priority1 30
ptp priority2 4
ptp domain 127
ptp mode boundary
ptp monitor threshold offset-from-master 250
ptp monitor threshold mean-path-delay 1500
ptp monitor sequence-id
ptp monitor threshold missing-message announce 3 sequence-ids
ptp monitor threshold missing-message delay-resp 3 sequence-ids
ptp monitor threshold missing-message follow-up 3 sequence-ids
ptp monitor threshold missing-message sync 3 sequence-ids
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

| User | Privilege | Role | Disabled |
| ---- | --------- | ---- | -------- |
| admin | 15 | network-admin | False |
| ansible | 15 | - | False |

### Local Users Device Configuration

```eos
!
username admin privilege 15 role network-admin nopassword
username ansible privilege 15 secret sha512 $6$7u4j1rkb3VELgcZE$EJt2Qff8kd/TapRoci0XaIZsL4tFzgq1YZBLD9c6f/knXzvcYY0NcMKndZeCv0T268knGKhOEwZAxqKjlMm920
```

# Monitoring

# Spanning Tree

## Spanning Tree Summary

STP mode: **mstp**

### MSTP Instance and Priority

| Instance(s) | Priority |
| -------- | -------- |
| 0 | 4096 |

## Spanning Tree Device Configuration

```eos
!
spanning-tree mode mstp
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
| 11 | VLAN11 | - |
| 12 | VLAN12 | - |

## VLANs Device Configuration

```eos
!
vlan 11
   name VLAN11
!
vlan 12
   name VLAN12
```

# Interfaces

## Ethernet Interfaces

### Ethernet Interfaces Summary

#### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | Channel-Group |
| --------- | ----------- | ---- | ----- | ----------- | ----------- | ------------- |
| Ethernet1 |  MEDIA | access | 11 | - | - | - |
| Ethernet2 |  MEDIA | access | 11 | - | - | - |
| Ethernet3 |  MEDIA | access | 11 | - | - | - |
| Ethernet4 |  MEDIA | access | 11 | - | - | - |
| Ethernet5 |  MEDIA | access | 11 | - | - | - |
| Ethernet6 |  MEDIA | access | 11 | - | - | - |
| Ethernet7 |  MEDIA | access | 11 | - | - | - |
| Ethernet8 |  MEDIA | access | 11 | - | - | - |
| Ethernet9 |  MEDIA | access | 11 | - | - | - |
| Ethernet10 |  MEDIA | access | 11 | - | - | - |
| Ethernet11 |  MEDIA | access | 11 | - | - | - |
| Ethernet12 |  MEDIA | access | 11 | - | - | - |
| Ethernet13 |  MEDIA | access | 11 | - | - | - |
| Ethernet14 |  MEDIA | access | 11 | - | - | - |
| Ethernet15 |  MEDIA | access | 11 | - | - | - |
| Ethernet16 |  MEDIA | access | 11 | - | - | - |
| Ethernet17 |  MEDIA | access | 11 | - | - | - |
| Ethernet18 |  MEDIA | access | 11 | - | - | - |
| Ethernet19 |  MEDIA | access | 11 | - | - | - |
| Ethernet20 |  MEDIA | access | 11 | - | - | - |
| Ethernet21 |  MEDIA | access | 11 | - | - | - |
| Ethernet22 |  MEDIA | access | 11 | - | - | - |
| Ethernet23 |  MEDIA | access | 11 | - | - | - |
| Ethernet24 |  MEDIA | access | 11 | - | - | - |
| Ethernet25 |  MEDIA | access | 11 | - | - | - |
| Ethernet26 |  MEDIA | access | 11 | - | - | - |
| Ethernet27 |  MEDIA | access | 11 | - | - | - |
| Ethernet28 |  MEDIA | access | 11 | - | - | - |
| Ethernet29 |  MEDIA | access | 11 | - | - | - |
| Ethernet30 |  MEDIA | access | 11 | - | - | - |
| Ethernet31 |  MEDIA | access | 11 | - | - | - |
| Ethernet32 |  MEDIA | access | 11 | - | - | - |
| Ethernet33 |  MEDIA | access | 11 | - | - | - |
| Ethernet34 |  MEDIA | access | 11 | - | - | - |
| Ethernet35 |  MEDIA | access | 11 | - | - | - |
| Ethernet36 |  MEDIA | access | 11 | - | - | - |
| Ethernet37 |  MEDIA | access | 11 | - | - | - |
| Ethernet38 |  MEDIA | access | 11 | - | - | - |
| Ethernet39 |  MEDIA | access | 11 | - | - | - |
| Ethernet40 |  MEDIA | access | 11 | - | - | - |
| Ethernet41 |  MEDIA | access | 11 | - | - | - |
| Ethernet42 |  MEDIA | access | 11 | - | - | - |
| Ethernet43 |  MEDIA | access | 11 | - | - | - |
| Ethernet44 |  MEDIA | access | 11 | - | - | - |
| Ethernet45 |  MEDIA | access | 11 | - | - | - |
| Ethernet46 |  MEDIA | access | 11 | - | - | - |
| Ethernet47 |  MEDIA | access | 11 | - | - | - |
| Ethernet48 |  MEDIA | access | 11 | - | - | - |

*Inherited from Port-Channel Interface

#### IPv4

| Interface | Description | Type | Channel Group | IP Address | VRF |  MTU | Shutdown | ACL In | ACL Out |
| --------- | ----------- | -----| ------------- | ---------- | ----| ---- | -------- | ------ | ------- |
| Ethernet51/1 | P2P_LINK_TO_BLUE-SPINE1_Ethernet5/1 | routed | - | 10.255.2.13/31 | default | 1500 | False | - | - |
| Ethernet52/1 | P2P_LINK_TO_BLUE-SPINE1_Ethernet6/1 | routed | - | 10.255.2.15/31 | default | 1500 | False | - | - |

### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet1
   description MEDIA
   no shutdown
   switchport access vlan 11
   switchport mode access
   switchport
   ptp enable
   ptp sync-message interval -3
   ptp announce interval 0
   ptp transport ipv4
   ptp announce timeout 3
   ptp delay-req interval -3
   ptp role master
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet2
   description MEDIA
   no shutdown
   switchport access vlan 11
   switchport mode access
   switchport
   ptp enable
   ptp sync-message interval -3
   ptp announce interval 0
   ptp transport ipv4
   ptp announce timeout 3
   ptp delay-req interval -3
   ptp role master
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet3
   description MEDIA
   no shutdown
   switchport access vlan 11
   switchport mode access
   switchport
   ptp enable
   ptp sync-message interval -3
   ptp announce interval 0
   ptp transport ipv4
   ptp announce timeout 3
   ptp delay-req interval -3
   ptp role master
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet4
   description MEDIA
   no shutdown
   switchport access vlan 11
   switchport mode access
   switchport
   ptp enable
   ptp sync-message interval -3
   ptp announce interval 0
   ptp transport ipv4
   ptp announce timeout 3
   ptp delay-req interval -3
   ptp role master
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet5
   description MEDIA
   no shutdown
   switchport access vlan 11
   switchport mode access
   switchport
   ptp enable
   ptp sync-message interval -3
   ptp announce interval 0
   ptp transport ipv4
   ptp announce timeout 3
   ptp delay-req interval -3
   ptp role master
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet6
   description MEDIA
   no shutdown
   switchport access vlan 11
   switchport mode access
   switchport
   ptp enable
   ptp sync-message interval -3
   ptp announce interval 0
   ptp transport ipv4
   ptp announce timeout 3
   ptp delay-req interval -3
   ptp role master
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet7
   description MEDIA
   no shutdown
   switchport access vlan 11
   switchport mode access
   switchport
   ptp enable
   ptp sync-message interval -3
   ptp announce interval 0
   ptp transport ipv4
   ptp announce timeout 3
   ptp delay-req interval -3
   ptp role master
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet8
   description MEDIA
   no shutdown
   switchport access vlan 11
   switchport mode access
   switchport
   ptp enable
   ptp sync-message interval -3
   ptp announce interval 0
   ptp transport ipv4
   ptp announce timeout 3
   ptp delay-req interval -3
   ptp role master
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet9
   description MEDIA
   no shutdown
   switchport access vlan 11
   switchport mode access
   switchport
   ptp enable
   ptp sync-message interval -3
   ptp announce interval 0
   ptp transport ipv4
   ptp announce timeout 3
   ptp delay-req interval -3
   ptp role master
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet10
   description MEDIA
   no shutdown
   switchport access vlan 11
   switchport mode access
   switchport
   ptp enable
   ptp sync-message interval -3
   ptp announce interval 0
   ptp transport ipv4
   ptp announce timeout 3
   ptp delay-req interval -3
   ptp role master
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet11
   description MEDIA
   no shutdown
   switchport access vlan 11
   switchport mode access
   switchport
   ptp enable
   ptp sync-message interval -3
   ptp announce interval 0
   ptp transport ipv4
   ptp announce timeout 3
   ptp delay-req interval -3
   ptp role master
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet12
   description MEDIA
   no shutdown
   switchport access vlan 11
   switchport mode access
   switchport
   ptp enable
   ptp sync-message interval -3
   ptp announce interval 0
   ptp transport ipv4
   ptp announce timeout 3
   ptp delay-req interval -3
   ptp role master
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet13
   description MEDIA
   no shutdown
   switchport access vlan 11
   switchport mode access
   switchport
   ptp enable
   ptp sync-message interval -3
   ptp announce interval 0
   ptp transport ipv4
   ptp announce timeout 3
   ptp delay-req interval -3
   ptp role master
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet14
   description MEDIA
   no shutdown
   switchport access vlan 11
   switchport mode access
   switchport
   ptp enable
   ptp sync-message interval -3
   ptp announce interval 0
   ptp transport ipv4
   ptp announce timeout 3
   ptp delay-req interval -3
   ptp role master
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet15
   description MEDIA
   no shutdown
   switchport access vlan 11
   switchport mode access
   switchport
   ptp enable
   ptp sync-message interval -3
   ptp announce interval 0
   ptp transport ipv4
   ptp announce timeout 3
   ptp delay-req interval -3
   ptp role master
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet16
   description MEDIA
   no shutdown
   switchport access vlan 11
   switchport mode access
   switchport
   ptp enable
   ptp sync-message interval -3
   ptp announce interval 0
   ptp transport ipv4
   ptp announce timeout 3
   ptp delay-req interval -3
   ptp role master
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet17
   description MEDIA
   no shutdown
   switchport access vlan 11
   switchport mode access
   switchport
   ptp enable
   ptp sync-message interval -3
   ptp announce interval 0
   ptp transport ipv4
   ptp announce timeout 3
   ptp delay-req interval -3
   ptp role master
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet18
   description MEDIA
   no shutdown
   switchport access vlan 11
   switchport mode access
   switchport
   ptp enable
   ptp sync-message interval -3
   ptp announce interval 0
   ptp transport ipv4
   ptp announce timeout 3
   ptp delay-req interval -3
   ptp role master
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet19
   description MEDIA
   no shutdown
   switchport access vlan 11
   switchport mode access
   switchport
   ptp enable
   ptp sync-message interval -3
   ptp announce interval 0
   ptp transport ipv4
   ptp announce timeout 3
   ptp delay-req interval -3
   ptp role master
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet20
   description MEDIA
   no shutdown
   switchport access vlan 11
   switchport mode access
   switchport
   ptp enable
   ptp sync-message interval -3
   ptp announce interval 0
   ptp transport ipv4
   ptp announce timeout 3
   ptp delay-req interval -3
   ptp role master
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet21
   description MEDIA
   no shutdown
   switchport access vlan 11
   switchport mode access
   switchport
   ptp enable
   ptp sync-message interval -3
   ptp announce interval 0
   ptp transport ipv4
   ptp announce timeout 3
   ptp delay-req interval -3
   ptp role master
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet22
   description MEDIA
   no shutdown
   switchport access vlan 11
   switchport mode access
   switchport
   ptp enable
   ptp sync-message interval -3
   ptp announce interval 0
   ptp transport ipv4
   ptp announce timeout 3
   ptp delay-req interval -3
   ptp role master
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet23
   description MEDIA
   no shutdown
   switchport access vlan 11
   switchport mode access
   switchport
   ptp enable
   ptp sync-message interval -3
   ptp announce interval 0
   ptp transport ipv4
   ptp announce timeout 3
   ptp delay-req interval -3
   ptp role master
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet24
   description MEDIA
   no shutdown
   switchport access vlan 11
   switchport mode access
   switchport
   ptp enable
   ptp sync-message interval -3
   ptp announce interval 0
   ptp transport ipv4
   ptp announce timeout 3
   ptp delay-req interval -3
   ptp role master
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet25
   description MEDIA
   no shutdown
   switchport access vlan 11
   switchport mode access
   switchport
   ptp enable
   ptp sync-message interval -3
   ptp announce interval 0
   ptp transport ipv4
   ptp announce timeout 3
   ptp delay-req interval -3
   ptp role master
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet26
   description MEDIA
   no shutdown
   switchport access vlan 11
   switchport mode access
   switchport
   ptp enable
   ptp sync-message interval -3
   ptp announce interval 0
   ptp transport ipv4
   ptp announce timeout 3
   ptp delay-req interval -3
   ptp role master
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet27
   description MEDIA
   no shutdown
   switchport access vlan 11
   switchport mode access
   switchport
   ptp enable
   ptp sync-message interval -3
   ptp announce interval 0
   ptp transport ipv4
   ptp announce timeout 3
   ptp delay-req interval -3
   ptp role master
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet28
   description MEDIA
   no shutdown
   switchport access vlan 11
   switchport mode access
   switchport
   ptp enable
   ptp sync-message interval -3
   ptp announce interval 0
   ptp transport ipv4
   ptp announce timeout 3
   ptp delay-req interval -3
   ptp role master
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet29
   description MEDIA
   no shutdown
   switchport access vlan 11
   switchport mode access
   switchport
   ptp enable
   ptp sync-message interval -3
   ptp announce interval 0
   ptp transport ipv4
   ptp announce timeout 3
   ptp delay-req interval -3
   ptp role master
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet30
   description MEDIA
   no shutdown
   switchport access vlan 11
   switchport mode access
   switchport
   ptp enable
   ptp sync-message interval -3
   ptp announce interval 0
   ptp transport ipv4
   ptp announce timeout 3
   ptp delay-req interval -3
   ptp role master
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet31
   description MEDIA
   no shutdown
   switchport access vlan 11
   switchport mode access
   switchport
   ptp enable
   ptp sync-message interval -3
   ptp announce interval 0
   ptp transport ipv4
   ptp announce timeout 3
   ptp delay-req interval -3
   ptp role master
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet32
   description MEDIA
   no shutdown
   switchport access vlan 11
   switchport mode access
   switchport
   ptp enable
   ptp sync-message interval -3
   ptp announce interval 0
   ptp transport ipv4
   ptp announce timeout 3
   ptp delay-req interval -3
   ptp role master
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet33
   description MEDIA
   no shutdown
   switchport access vlan 11
   switchport mode access
   switchport
   ptp enable
   ptp sync-message interval -3
   ptp announce interval 0
   ptp transport ipv4
   ptp announce timeout 3
   ptp delay-req interval -3
   ptp role master
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet34
   description MEDIA
   no shutdown
   switchport access vlan 11
   switchport mode access
   switchport
   ptp enable
   ptp sync-message interval -3
   ptp announce interval 0
   ptp transport ipv4
   ptp announce timeout 3
   ptp delay-req interval -3
   ptp role master
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet35
   description MEDIA
   no shutdown
   switchport access vlan 11
   switchport mode access
   switchport
   ptp enable
   ptp sync-message interval -3
   ptp announce interval 0
   ptp transport ipv4
   ptp announce timeout 3
   ptp delay-req interval -3
   ptp role master
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet36
   description MEDIA
   no shutdown
   switchport access vlan 11
   switchport mode access
   switchport
   ptp enable
   ptp sync-message interval -3
   ptp announce interval 0
   ptp transport ipv4
   ptp announce timeout 3
   ptp delay-req interval -3
   ptp role master
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet37
   description MEDIA
   no shutdown
   switchport access vlan 11
   switchport mode access
   switchport
   ptp enable
   ptp sync-message interval -3
   ptp announce interval 0
   ptp transport ipv4
   ptp announce timeout 3
   ptp delay-req interval -3
   ptp role master
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet38
   description MEDIA
   no shutdown
   switchport access vlan 11
   switchport mode access
   switchport
   ptp enable
   ptp sync-message interval -3
   ptp announce interval 0
   ptp transport ipv4
   ptp announce timeout 3
   ptp delay-req interval -3
   ptp role master
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet39
   description MEDIA
   no shutdown
   switchport access vlan 11
   switchport mode access
   switchport
   ptp enable
   ptp sync-message interval -3
   ptp announce interval 0
   ptp transport ipv4
   ptp announce timeout 3
   ptp delay-req interval -3
   ptp role master
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet40
   description MEDIA
   no shutdown
   switchport access vlan 11
   switchport mode access
   switchport
   ptp enable
   ptp sync-message interval -3
   ptp announce interval 0
   ptp transport ipv4
   ptp announce timeout 3
   ptp delay-req interval -3
   ptp role master
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet41
   description MEDIA
   no shutdown
   switchport access vlan 11
   switchport mode access
   switchport
   ptp enable
   ptp sync-message interval -3
   ptp announce interval 0
   ptp transport ipv4
   ptp announce timeout 3
   ptp delay-req interval -3
   ptp role master
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet42
   description MEDIA
   no shutdown
   switchport access vlan 11
   switchport mode access
   switchport
   ptp enable
   ptp sync-message interval -3
   ptp announce interval 0
   ptp transport ipv4
   ptp announce timeout 3
   ptp delay-req interval -3
   ptp role master
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet43
   description MEDIA
   no shutdown
   switchport access vlan 11
   switchport mode access
   switchport
   ptp enable
   ptp sync-message interval -3
   ptp announce interval 0
   ptp transport ipv4
   ptp announce timeout 3
   ptp delay-req interval -3
   ptp role master
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet44
   description MEDIA
   no shutdown
   switchport access vlan 11
   switchport mode access
   switchport
   ptp enable
   ptp sync-message interval -3
   ptp announce interval 0
   ptp transport ipv4
   ptp announce timeout 3
   ptp delay-req interval -3
   ptp role master
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet45
   description MEDIA
   no shutdown
   switchport access vlan 11
   switchport mode access
   switchport
   ptp enable
   ptp sync-message interval -3
   ptp announce interval 0
   ptp transport ipv4
   ptp announce timeout 3
   ptp delay-req interval -3
   ptp role master
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet46
   description MEDIA
   no shutdown
   switchport access vlan 11
   switchport mode access
   switchport
   ptp enable
   ptp sync-message interval -3
   ptp announce interval 0
   ptp transport ipv4
   ptp announce timeout 3
   ptp delay-req interval -3
   ptp role master
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet47
   description MEDIA
   no shutdown
   switchport access vlan 11
   switchport mode access
   switchport
   ptp enable
   ptp sync-message interval -3
   ptp announce interval 0
   ptp transport ipv4
   ptp announce timeout 3
   ptp delay-req interval -3
   ptp role master
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet48
   description MEDIA
   no shutdown
   switchport access vlan 11
   switchport mode access
   switchport
   ptp enable
   ptp sync-message interval -3
   ptp announce interval 0
   ptp transport ipv4
   ptp announce timeout 3
   ptp delay-req interval -3
   ptp role master
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet51/1
   description P2P_LINK_TO_BLUE-SPINE1_Ethernet5/1
   no shutdown
   mtu 1500
   no switchport
   ip address 10.255.2.13/31
   pim ipv4 sparse-mode
   ptp enable
   ptp sync-message interval -3
   ptp announce interval 0
   ptp transport ipv4
   ptp announce timeout 3
   ptp delay-req interval -3
!
interface Ethernet52/1
   description P2P_LINK_TO_BLUE-SPINE1_Ethernet6/1
   no shutdown
   mtu 1500
   no switchport
   ip address 10.255.2.15/31
   pim ipv4 sparse-mode
   ptp enable
   ptp sync-message interval -3
   ptp announce interval 0
   ptp transport ipv4
   ptp announce timeout 3
   ptp delay-req interval -3
```

## Loopback Interfaces

### Loopback Interfaces Summary

#### IPv4

| Interface | Description | VRF | IP Address |
| --------- | ----------- | --- | ---------- |
| Loopback0 | Router-id | default | 10.255.1.4/32 |

#### IPv6

| Interface | Description | VRF | IPv6 Address |
| --------- | ----------- | --- | ------------ |
| Loopback0 | Router-id | default | - |


### Loopback Interfaces Device Configuration

```eos
!
interface Loopback0
   description Router-id
   no shutdown
   ip address 10.255.1.4/32
```

## VLAN Interfaces

### VLAN Interfaces Summary

| Interface | Description | VRF |  MTU | Shutdown |
| --------- | ----------- | --- | ---- | -------- |
| Vlan11 | VLAN11 | default | - | False |
| Vlan12 | VLAN12 | default | - | False |

#### IPv4

| Interface | VRF | IP Address | IP Address Virtual | IP Router Virtual Address | VRRP | ACL In | ACL Out |
| --------- | --- | ---------- | ------------------ | ------------------------- | ---- | ------ | ------- |
| Vlan11 |  default  |  10.4.11.1/24  |  -  |  -  |  -  |  -  |  -  |
| Vlan12 |  default  |  10.4.12.1/24  |  -  |  -  |  -  |  -  |  -  |

### VLAN Interfaces Device Configuration

```eos
!
interface Vlan11
   description VLAN11
   no shutdown
   ip address 10.4.11.1/24
!
interface Vlan12
   description VLAN12
   no shutdown
   ip address 10.4.12.1/24
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

#### Virtual Router MAC Address: 00:1c:73:00:00:99

### Virtual Router MAC Address Configuration

```eos
!
ip virtual-router mac-address 00:1c:73:00:00:99
```

## IP Routing

### IP Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | True |
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
| default | False |
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

## Router BGP

### Router BGP Summary

| BGP AS | Router ID |
| ------ | --------- |
| 65104|  10.255.1.4 |

| BGP Tuning |
| ---------- |
| maximum-paths 4 ecmp 4 |

### Router BGP Peer Groups

#### IPv4-UNDERLAY-PEERS

| Settings | Value |
| -------- | ----- |
| Address Family | ipv4 |
| Send community | all |
| Maximum routes | 12000 |

### BGP Neighbors

| Neighbor | Remote AS | VRF | Shutdown | Send-community | Maximum-routes | Allowas-in | BFD | RIB Pre-Policy Retain | Route-Reflector Client |
| -------- | --------- | --- | -------- | -------------- | -------------- | ---------- | --- | --------------------- | ---------------------- |
| 10.255.2.12 | 65100 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - |
| 10.255.2.14 | 65100 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - |

### Router BGP Device Configuration

```eos
!
router bgp 65104
   router-id 10.255.1.4
   maximum-paths 4 ecmp 4
   neighbor IPv4-UNDERLAY-PEERS peer group
   neighbor IPv4-UNDERLAY-PEERS password 7 7x4B4rnJhZB438m9+BrBfQ==
   neighbor IPv4-UNDERLAY-PEERS send-community
   neighbor IPv4-UNDERLAY-PEERS maximum-routes 12000
   neighbor 10.255.2.12 peer group IPv4-UNDERLAY-PEERS
   neighbor 10.255.2.12 remote-as 65100
   neighbor 10.255.2.12 description blue-spine1_Ethernet5/1
   neighbor 10.255.2.14 peer group IPv4-UNDERLAY-PEERS
   neighbor 10.255.2.14 remote-as 65100
   neighbor 10.255.2.14 description blue-spine1_Ethernet6/1
   redistribute connected
   !
   address-family ipv4
      neighbor IPv4-UNDERLAY-PEERS activate
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

## Router Multicast

### IP Router Multicast Summary

- Routing for IPv4 multicast is enabled.

### Router Multicast Device Configuration

```eos
!
router multicast
   ipv4
      routing
```


## PIM Sparse Mode

### Router PIM Sparse Mode

#### IP Sparse Mode Information

BFD enabled: False

##### IP Rendezvous Information

| Rendezvous Point Address | Group Address | Access Lists | Priority | Hashmask | Override |
| ------------------------ | ------------- | ------------ | -------- | -------- | -------- |
| 10.255.0.1 | - | - | - | - | - |

#### Router Multicast Device Configuration

```eos
!
router pim sparse-mode
   ipv4
      rp address 10.255.0.1
```

### PIM Sparse Mode enabled interfaces

| Interface Name | VRF Name | IP Version | DR Priority | Local Interface |
| -------------- | -------- | ---------- | ----------- | --------------- |
| Ethernet51/1 | - | IPv4 | - | - |
| Ethernet52/1 | - | IPv4 | - | - |

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
