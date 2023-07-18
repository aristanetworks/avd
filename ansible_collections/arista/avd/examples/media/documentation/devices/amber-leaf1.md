# amber-leaf1

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
  - [IP Name Servers](#ip-name-servers)
  - [NTP](#ntp)
  - [PTP](#ptp)
  - [Management API HTTP](#management-api-http)
- [Authentication](#authentication)
  - [Local Users](#local-users)
  - [AAA Authentication](#aaa-authentication)
  - [AAA Authorization](#aaa-authorization)
- [Monitoring](#monitoring)
  - [TerminAttr Daemon](#terminattr-daemon)
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
  - [IP Routing](#ip-routing)
  - [IPv6 Routing](#ipv6-routing)
  - [Static Routes](#static-routes)
  - [Router BGP](#router-bgp)
- [Multicast](#multicast)
  - [IP IGMP Snooping](#ip-igmp-snooping)
  - [Router Multicast](#router-multicast)
  - [PIM Sparse Mode](#pim-sparse-mode)
- [VRF Instances](#vrf-instances)
  - [VRF Instances Summary](#vrf-instances-summary)
  - [VRF Instances Device Configuration](#vrf-instances-device-configuration)

## Management

### Management Interfaces

#### Management Interfaces Summary

##### IPv4

| Management Interface | description | Type | VRF | IP Address | Gateway |
| -------------------- | ----------- | ---- | --- | ---------- | ------- |
| Management1 | oob_management | oob | MGMT | 172.16.1.111/24 | 10.90.227.1 |

##### IPv6

| Management Interface | description | Type | VRF | IPv6 Address | IPv6 Gateway |
| -------------------- | ----------- | ---- | --- | ------------ | ------------ |
| Management1 | oob_management | oob | MGMT | - | - |

#### Management Interfaces Device Configuration

```eos
!
interface Management1
   description oob_management
   no shutdown
   vrf MGMT
   ip address 172.16.1.111/24
```

### IP Name Servers

#### IP Name Servers Summary

| Name Server | VRF | Priority |
| ----------- | --- | -------- |
| 192.168.1.1 | MGMT | - |

#### IP Name Servers Device Configuration

```eos
ip name-server vrf MGMT 192.168.1.1
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
| 0.pool.ntp.org | MGMT | - | - | - | - | - | - | - | - |

#### NTP Device Configuration

```eos
!
ntp local-interface vrf MGMT Management1
ntp server vrf MGMT 0.pool.ntp.org
```

### PTP

#### PTP Summary

| Clock ID | Source IP | Priority 1 | Priority 2 | TTL | Domain | Mode | Forward Unicast |
| -------- | --------- | ---------- | ---------- | --- | ------ | ---- | --------------- |
| 00:1C:73:1e:00:01 | - | 30 | 1 | - | 127 | boundary | - |

#### PTP Device Configuration

```eos
!
ptp clock-identity 00:1C:73:1e:00:01
ptp priority1 30
ptp priority2 1
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

### Management API HTTP

#### Management API HTTP Summary

| HTTP | HTTPS | Default Services |
| ---- | ----- | ---------------- |
| False | True | - |

#### Management API VRF Access

| VRF Name | IPv4 ACL | IPv6 ACL |
| -------- | -------- | -------- |
| MGMT | - | - |

#### Management API HTTP Configuration

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
| ansible | 15 | network-admin | False | - |

#### Local Users Device Configuration

```eos
!
username admin privilege 15 role network-admin nopassword
username ansible privilege 15 role network-admin secret sha512 <removed>
```

### AAA Authentication

#### AAA Authentication Summary

| Type | Sub-type | User Stores |
| ---- | -------- | ---------- |
| Login | default | local |

#### AAA Authentication Device Configuration

```eos
aaa authentication login default local
!
```

### AAA Authorization

#### AAA Authorization Summary

| Type | User Stores |
| ---- | ----------- |
| Exec | local |

Authorization for configuration commands is disabled.

#### AAA Authorization Device Configuration

```eos
aaa authorization exec default local
!
```

## Monitoring

### TerminAttr Daemon

#### TerminAttr Daemon Summary

| CV Compression | CloudVision Servers | VRF | Authentication | Smash Excludes | Ingest Exclude | Bypass AAA |
| -------------- | ------------------- | --- | -------------- | -------------- | -------------- | ---------- |
| gzip | 192.168.1.12:9910 | MGMT | token,/tmp/token | ale,flexCounter,hardware,kni,pulse,strata | /Sysdb/cell/1/agent,/Sysdb/cell/2/agent | True |

#### TerminAttr Daemon Device Configuration

```eos
!
daemon TerminAttr
   exec /usr/bin/TerminAttr -cvaddr=192.168.1.12:9910 -cvauth=token,/tmp/token -cvvrf=MGMT -disableaaa -smashexcludes=ale,flexCounter,hardware,kni,pulse,strata -ingestexclude=/Sysdb/cell/1/agent,/Sysdb/cell/2/agent -taillogs
   no shutdown
```

## Spanning Tree

### Spanning Tree Summary

STP mode: **mstp**

#### MSTP Instance and Priority

| Instance(s) | Priority |
| -------- | -------- |
| 0 | 4096 |

### Spanning Tree Device Configuration

```eos
!
spanning-tree mode mstp
spanning-tree mst 0 priority 4096
```

## Internal VLAN Allocation Policy

### Internal VLAN Allocation Policy Summary

| Policy Allocation | Range Beginning | Range Ending |
| ------------------| --------------- | ------------ |
| ascending | 1006 | 1199 |

### Internal VLAN Allocation Policy Configuration

```eos
!
vlan internal order ascending range 1006 1199
```

## VLANs

### VLANs Summary

| VLAN ID | Name | Trunk Groups |
| ------- | ---- | ------------ |
| 111 | VLAN111 | - |

### VLANs Device Configuration

```eos
!
vlan 111
   name VLAN111
```

## Interfaces

### Ethernet Interfaces

#### Ethernet Interfaces Summary

##### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | Channel-Group |
| --------- | ----------- | ---- | ----- | ----------- | ----------- | ------------- |
| Ethernet3 |  AMBER_VLAN111 | access | 111 | - | - | - |
| Ethernet4 |  AMBER_VLAN111 | access | 111 | - | - | - |
| Ethernet5 |  AMBER_VLAN111 | access | 111 | - | - | - |
| Ethernet6 |  AMBER_VLAN111 | access | 111 | - | - | - |
| Ethernet7 |  AMBER_VLAN111 | access | 111 | - | - | - |
| Ethernet8 |  AMBER_VLAN111 | access | 111 | - | - | - |
| Ethernet9 |  AMBER_VLAN111 | access | 111 | - | - | - |
| Ethernet10 |  AMBER_VLAN111 | access | 111 | - | - | - |
| Ethernet11 |  AMBER_VLAN111 | access | 111 | - | - | - |
| Ethernet12 |  AMBER_VLAN111 | access | 111 | - | - | - |
| Ethernet13 |  AMBER_VLAN111 | access | 111 | - | - | - |
| Ethernet14 |  AMBER_VLAN111 | access | 111 | - | - | - |
| Ethernet15 |  AMBER_VLAN111 | access | 111 | - | - | - |
| Ethernet16 |  AMBER_VLAN111 | access | 111 | - | - | - |
| Ethernet17 |  AMBER_VLAN111 | access | 111 | - | - | - |
| Ethernet18 |  AMBER_VLAN111 | access | 111 | - | - | - |
| Ethernet19 |  AMBER_VLAN111 | access | 111 | - | - | - |
| Ethernet20 |  AMBER_VLAN111 | access | 111 | - | - | - |
| Ethernet21 |  AMBER_VLAN111 | access | 111 | - | - | - |
| Ethernet22 |  AMBER_VLAN111 | access | 111 | - | - | - |
| Ethernet23 |  AMBER_VLAN111 | access | 111 | - | - | - |
| Ethernet24 |  AMBER_VLAN111 | access | 111 | - | - | - |
| Ethernet25 |  AMBER_VLAN111 | access | 111 | - | - | - |
| Ethernet26 |  AMBER_VLAN111 | access | 111 | - | - | - |
| Ethernet27 |  AMBER_VLAN111 | access | 111 | - | - | - |
| Ethernet28 |  AMBER_VLAN111 | access | 111 | - | - | - |
| Ethernet29 |  AMBER_VLAN111 | access | 111 | - | - | - |
| Ethernet30 |  AMBER_VLAN111 | access | 111 | - | - | - |
| Ethernet31 |  AMBER_VLAN111 | access | 111 | - | - | - |
| Ethernet32 |  AMBER_VLAN111 | access | 111 | - | - | - |
| Ethernet33 |  AMBER_VLAN111 | access | 111 | - | - | - |
| Ethernet34 |  AMBER_VLAN111 | access | 111 | - | - | - |
| Ethernet35 |  AMBER_VLAN111 | access | 111 | - | - | - |
| Ethernet36 |  AMBER_VLAN111 | access | 111 | - | - | - |
| Ethernet37 |  AMBER_VLAN111 | access | 111 | - | - | - |
| Ethernet38 |  AMBER_VLAN111 | access | 111 | - | - | - |
| Ethernet39 |  AMBER_VLAN111 | access | 111 | - | - | - |
| Ethernet40 |  AMBER_VLAN111 | access | 111 | - | - | - |
| Ethernet41 |  AMBER_VLAN111 | access | 111 | - | - | - |
| Ethernet42 |  AMBER_VLAN111 | access | 111 | - | - | - |
| Ethernet43 |  AMBER_VLAN111 | access | 111 | - | - | - |
| Ethernet44 |  AMBER_VLAN111 | access | 111 | - | - | - |
| Ethernet45 |  AMBER_VLAN111 | access | 111 | - | - | - |
| Ethernet46 |  AMBER_VLAN111 | access | 111 | - | - | - |
| Ethernet47 |  AMBER_VLAN111 | access | 111 | - | - | - |
| Ethernet48 |  AMBER_VLAN111 | access | 111 | - | - | - |

*Inherited from Port-Channel Interface

##### IPv4

| Interface | Description | Type | Channel Group | IP Address | VRF |  MTU | Shutdown | ACL In | ACL Out |
| --------- | ----------- | -----| ------------- | ---------- | ----| ---- | -------- | ------ | ------- |
| Ethernet1 | P2P_LINK_TO_AMBER-SPINE1_Ethernet1 | routed | - | 10.255.254.1/31 | default | 1500 | False | - | - |
| Ethernet2 | P2P_LINK_TO_AMBER-SPINE1_Ethernet2 | routed | - | 10.255.254.3/31 | default | 1500 | False | - | - |

#### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet1
   description P2P_LINK_TO_AMBER-SPINE1_Ethernet1
   no shutdown
   mtu 1500
   no switchport
   ip address 10.255.254.1/31
   pim ipv4 sparse-mode
   ptp enable
   ptp sync-message interval -3
   ptp announce interval 0
   ptp transport ipv4
   ptp announce timeout 3
   ptp delay-req interval -3
!
interface Ethernet2
   description P2P_LINK_TO_AMBER-SPINE1_Ethernet2
   no shutdown
   mtu 1500
   no switchport
   ip address 10.255.254.3/31
   pim ipv4 sparse-mode
   ptp enable
   ptp sync-message interval -3
   ptp announce interval 0
   ptp transport ipv4
   ptp announce timeout 3
   ptp delay-req interval -3
!
interface Ethernet3
   description AMBER_VLAN111
   shutdown
   switchport access vlan 111
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
   description AMBER_VLAN111
   shutdown
   switchport access vlan 111
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
   description AMBER_VLAN111
   shutdown
   switchport access vlan 111
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
   description AMBER_VLAN111
   shutdown
   switchport access vlan 111
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
   description AMBER_VLAN111
   shutdown
   switchport access vlan 111
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
   description AMBER_VLAN111
   shutdown
   switchport access vlan 111
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
   description AMBER_VLAN111
   shutdown
   switchport access vlan 111
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
   description AMBER_VLAN111
   shutdown
   switchport access vlan 111
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
   description AMBER_VLAN111
   shutdown
   switchport access vlan 111
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
   description AMBER_VLAN111
   shutdown
   switchport access vlan 111
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
   description AMBER_VLAN111
   shutdown
   switchport access vlan 111
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
   description AMBER_VLAN111
   shutdown
   switchport access vlan 111
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
   description AMBER_VLAN111
   shutdown
   switchport access vlan 111
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
   description AMBER_VLAN111
   shutdown
   switchport access vlan 111
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
   description AMBER_VLAN111
   shutdown
   switchport access vlan 111
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
   description AMBER_VLAN111
   shutdown
   switchport access vlan 111
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
   description AMBER_VLAN111
   shutdown
   switchport access vlan 111
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
   description AMBER_VLAN111
   shutdown
   switchport access vlan 111
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
   description AMBER_VLAN111
   shutdown
   switchport access vlan 111
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
   description AMBER_VLAN111
   shutdown
   switchport access vlan 111
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
   description AMBER_VLAN111
   shutdown
   switchport access vlan 111
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
   description AMBER_VLAN111
   shutdown
   switchport access vlan 111
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
   description AMBER_VLAN111
   shutdown
   switchport access vlan 111
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
   description AMBER_VLAN111
   shutdown
   switchport access vlan 111
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
   description AMBER_VLAN111
   shutdown
   switchport access vlan 111
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
   description AMBER_VLAN111
   shutdown
   switchport access vlan 111
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
   description AMBER_VLAN111
   shutdown
   switchport access vlan 111
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
   description AMBER_VLAN111
   shutdown
   switchport access vlan 111
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
   description AMBER_VLAN111
   shutdown
   switchport access vlan 111
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
   description AMBER_VLAN111
   shutdown
   switchport access vlan 111
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
   description AMBER_VLAN111
   shutdown
   switchport access vlan 111
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
   description AMBER_VLAN111
   shutdown
   switchport access vlan 111
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
   description AMBER_VLAN111
   shutdown
   switchport access vlan 111
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
   description AMBER_VLAN111
   shutdown
   switchport access vlan 111
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
   description AMBER_VLAN111
   shutdown
   switchport access vlan 111
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
   description AMBER_VLAN111
   shutdown
   switchport access vlan 111
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
   description AMBER_VLAN111
   shutdown
   switchport access vlan 111
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
   description AMBER_VLAN111
   shutdown
   switchport access vlan 111
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
   description AMBER_VLAN111
   shutdown
   switchport access vlan 111
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
   description AMBER_VLAN111
   shutdown
   switchport access vlan 111
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
   description AMBER_VLAN111
   shutdown
   switchport access vlan 111
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
   description AMBER_VLAN111
   shutdown
   switchport access vlan 111
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
   description AMBER_VLAN111
   shutdown
   switchport access vlan 111
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
   description AMBER_VLAN111
   shutdown
   switchport access vlan 111
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
   description AMBER_VLAN111
   shutdown
   switchport access vlan 111
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
   description AMBER_VLAN111
   shutdown
   switchport access vlan 111
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
```

### Loopback Interfaces

#### Loopback Interfaces Summary

##### IPv4

| Interface | Description | VRF | IP Address |
| --------- | ----------- | --- | ---------- |
| Loopback0 | Router_ID | default | 10.255.1.2/32 |

##### IPv6

| Interface | Description | VRF | IPv6 Address |
| --------- | ----------- | --- | ------------ |
| Loopback0 | Router_ID | default | - |


#### Loopback Interfaces Device Configuration

```eos
!
interface Loopback0
   description Router_ID
   no shutdown
   ip address 10.255.1.2/32
```

### VLAN Interfaces

#### VLAN Interfaces Summary

| Interface | Description | VRF |  MTU | Shutdown |
| --------- | ----------- | --- | ---- | -------- |
| Vlan111 | VLAN111 | default | - | False |

##### IPv4

| Interface | VRF | IP Address | IP Address Virtual | IP Router Virtual Address | VRRP | ACL In | ACL Out |
| --------- | --- | ---------- | ------------------ | ------------------------- | ---- | ------ | ------- |
| Vlan111 |  default  |  10.10.111.1/24  |  -  |  -  |  -  |  -  |  -  |

#### VLAN Interfaces Device Configuration

```eos
!
interface Vlan111
   description VLAN111
   no shutdown
   ip address 10.10.111.1/24
   ip helper-address 10.252.4.253
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

| VRF | Destination Prefix | Next Hop IP             | Exit interface      | Administrative Distance       | Tag               | Route Name                    | Metric         |
| --- | ------------------ | ----------------------- | ------------------- | ----------------------------- | ----------------- | ----------------------------- | -------------- |
| MGMT | 0.0.0.0/0 | 10.90.227.1 | - | 1 | - | - | - |

#### Static Routes Device Configuration

```eos
!
ip route vrf MGMT 0.0.0.0/0 10.90.227.1
```

### Router BGP

#### Router BGP Summary

| BGP AS | Router ID |
| ------ | --------- |
| 65101|  10.255.1.2 |

| BGP Tuning |
| ---------- |
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

| Neighbor | Remote AS | VRF | Shutdown | Send-community | Maximum-routes | Allowas-in | BFD | RIB Pre-Policy Retain | Route-Reflector Client | Passive |
| -------- | --------- | --- | -------- | -------------- | -------------- | ---------- | --- | --------------------- | ---------------------- | ------- |
| 10.255.254.0 | 65100 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 10.255.254.2 | 65100 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |

#### Router BGP Device Configuration

```eos
!
router bgp 65101
   router-id 10.255.1.2
   maximum-paths 4 ecmp 4
   no bgp default ipv4-unicast
   neighbor IPv4-UNDERLAY-PEERS peer group
   neighbor IPv4-UNDERLAY-PEERS password 7 <removed>
   neighbor IPv4-UNDERLAY-PEERS send-community
   neighbor IPv4-UNDERLAY-PEERS maximum-routes 12000
   neighbor 10.255.254.0 peer group IPv4-UNDERLAY-PEERS
   neighbor 10.255.254.0 remote-as 65100
   neighbor 10.255.254.0 description amber-spine1_Ethernet1
   neighbor 10.255.254.2 peer group IPv4-UNDERLAY-PEERS
   neighbor 10.255.254.2 remote-as 65100
   neighbor 10.255.254.2 description amber-spine1_Ethernet2
   redistribute connected
   !
   address-family ipv4
      neighbor IPv4-UNDERLAY-PEERS activate
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

### Router Multicast

#### IP Router Multicast Summary

- Routing for IPv4 multicast is enabled.

#### Router Multicast Device Configuration

```eos
!
router multicast
   ipv4
      routing
```


### PIM Sparse Mode

#### PIM Sparse Mode enabled interfaces

| Interface Name | VRF Name | IP Version | DR Priority | Local Interface |
| -------------- | -------- | ---------- | ----------- | --------------- |
| Ethernet1 | - | IPv4 | - | - |
| Ethernet2 | - | IPv4 | - | - |

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
