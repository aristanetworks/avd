# blue-leaf1

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
  - [DNS Domain](#dns-domain)
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
  - [SFlow](#sflow)
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
- [VRF Instances](#vrf-instances)
  - [VRF Instances Summary](#vrf-instances-summary)
  - [VRF Instances Device Configuration](#vrf-instances-device-configuration)

## Management

### Management Interfaces

#### Management Interfaces Summary

##### IPv4

| Management Interface | description | Type | VRF | IP Address | Gateway |
| -------------------- | ----------- | ---- | --- | ---------- | ------- |
| Management1 | oob_management | oob | MGMT | 10.90.227.29/24 | 10.252.0.1 |

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
   ip address 10.90.227.29/24
```

### DNS Domain

#### DNS domain: MnE.lab

#### DNS Domain Device Configuration

```eos
dns domain MnE.lab
!
```

### IP Name Servers

#### IP Name Servers Summary

| Name Server | VRF | Priority |
| ----------- | --- | -------- |
| 10.90.227.155 | MGMT | - |

#### IP Name Servers Device Configuration

```eos
ip name-server vrf MGMT 10.90.227.155
```

### NTP

#### NTP Summary

##### NTP Servers

| Server | VRF | Preferred | Burst | iBurst | Version | Min Poll | Max Poll | Local-interface | Key |
| ------ | --- | --------- | ----- | ------ | ------- | -------- | -------- | --------------- | --- |
| ntp.aristanetworks.com | MGMT | - | - | True | - | - | - | - | - |

#### NTP Device Configuration

```eos
!
ntp server vrf MGMT ntp.aristanetworks.com iburst
```

### PTP

#### PTP Summary

| Clock ID | Source IP | Priority 1 | Priority 2 | TTL | Domain | Mode | Forward Unicast |
| -------- | --------- | ---------- | ---------- | --- | ------ | ---- | --------------- |
| 00:1C:73:1e:00:02 | - | 30 | 2 | - | 0 | boundary | - |

#### PTP Device Configuration

```eos
!
ptp clock-identity 00:1C:73:1e:00:02
ptp priority1 30
ptp priority2 2
ptp domain 0
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
| cvpadmin | 15 | network-admin | False | - |

#### Local Users Device Configuration

```eos
!
username admin privilege 15 role network-admin secret sha512 <removed>
username cvpadmin privilege 15 role network-admin secret sha512 <removed>
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
+
| gzip | apiserver.arista.io:443 | MGMT | token-secure,/tmp/cv-onboarding-token | - | - | False |
| gzip | 10.243.132.193:9910 | MGMT | token,/tmp/devtoken | - | - | False |
| gzip | 10.90.227.161:9910 | MGMT | token,/tmp/token | - | - | False |

#### TerminAttr Daemon Device Configuration

```eos
!
daemon TerminAttr
   exec /usr/bin/TerminAttr -cvopt cvaas.addr=apiserver.arista.io:443 -cvopt cvaas.auth=token-secure,/tmp/cv-onboarding-token -cvopt cvaas.vrf=MGMT -cvopt dev.addr=10.243.132.193:9910 -cvopt dev.auth=token,/tmp/devtoken -cvopt dev.vrf=MGMT -cvopt lab.addr=10.90.227.161:9910 -cvopt lab.auth=token,/tmp/token -cvopt lab.vrf=MGMT -taillogs
   no shutdown
```

### SFlow

#### SFlow Summary

| VRF | SFlow Source | SFlow Destination | Port |
| --- | ------------ | ----------------- | ---- |
| default | - | 127.0.0.1 | 6343 |
| default | loopback0 | - | - |

sFlow is enabled.

#### SFlow Device Configuration

```eos
!
sflow destination 127.0.0.1
sflow source-interface loopback0
sflow run
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
| 121 | VLAN121 | - |

### VLANs Device Configuration

```eos
!
vlan 121
   name VLAN121
```

## Interfaces

### Ethernet Interfaces

#### Ethernet Interfaces Summary

##### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | Channel-Group |
| --------- | ----------- | ---- | ----- | ----------- | ----------- | ------------- |
| Ethernet1 |  BLUE_VLAN121 | access | 121 | - | - | - |
| Ethernet2 |  BLUE_VLAN121 | access | 121 | - | - | - |
| Ethernet3 |  BLUE_VLAN121 | access | 121 | - | - | - |
| Ethernet4 |  BLUE_VLAN121 | access | 121 | - | - | - |
| Ethernet5 |  BLUE_VLAN121 | access | 121 | - | - | - |
| Ethernet6 |  BLUE_VLAN121 | access | 121 | - | - | - |
| Ethernet7 |  BLUE_VLAN121 | access | 121 | - | - | - |
| Ethernet8 |  BLUE_VLAN121 | access | 121 | - | - | - |
| Ethernet9 |  BLUE_VLAN121 | access | 121 | - | - | - |
| Ethernet10 |  BLUE_VLAN121 | access | 121 | - | - | - |
| Ethernet11 |  BLUE_VLAN121 | access | 121 | - | - | - |
| Ethernet12 |  BLUE_VLAN121 | access | 121 | - | - | - |
| Ethernet13 |  BLUE_VLAN121 | access | 121 | - | - | - |
| Ethernet14 |  BLUE_VLAN121 | access | 121 | - | - | - |
| Ethernet15 |  BLUE_VLAN121 | access | 121 | - | - | - |
| Ethernet16 |  BLUE_VLAN121 | access | 121 | - | - | - |
| Ethernet17 |  BLUE_VLAN121 | access | 121 | - | - | - |
| Ethernet18 |  BLUE_VLAN121 | access | 121 | - | - | - |
| Ethernet19 |  BLUE_VLAN121 | access | 121 | - | - | - |
| Ethernet20 |  BLUE_VLAN121 | access | 121 | - | - | - |
| Ethernet21 |  BLUE_VLAN121 | access | 121 | - | - | - |
| Ethernet22 |  BLUE_VLAN121 | access | 121 | - | - | - |
| Ethernet23 |  BLUE_VLAN121 | access | 121 | - | - | - |
| Ethernet24 |  BLUE_VLAN121 | access | 121 | - | - | - |
| Ethernet25 |  BLUE_VLAN121 | access | 121 | - | - | - |
| Ethernet26 |  BLUE_VLAN121 | access | 121 | - | - | - |
| Ethernet27 |  BLUE_VLAN121 | access | 121 | - | - | - |
| Ethernet28 |  BLUE_VLAN121 | access | 121 | - | - | - |
| Ethernet29 |  BLUE_VLAN121 | access | 121 | - | - | - |
| Ethernet30 |  BLUE_VLAN121 | access | 121 | - | - | - |
| Ethernet31 |  BLUE_VLAN121 | access | 121 | - | - | - |
| Ethernet32 |  BLUE_VLAN121 | access | 121 | - | - | - |
| Ethernet33 |  BLUE_VLAN121 | access | 121 | - | - | - |
| Ethernet34 |  BLUE_VLAN121 | access | 121 | - | - | - |
| Ethernet35 |  BLUE_VLAN121 | access | 121 | - | - | - |
| Ethernet36 |  BLUE_VLAN121 | access | 121 | - | - | - |
| Ethernet37 |  BLUE_VLAN121 | access | 121 | - | - | - |
| Ethernet38 |  BLUE_VLAN121 | access | 121 | - | - | - |
| Ethernet39 |  BLUE_VLAN121 | access | 121 | - | - | - |
| Ethernet40 |  BLUE_VLAN121 | access | 121 | - | - | - |
| Ethernet41 |  BLUE_VLAN121 | access | 121 | - | - | - |
| Ethernet42 |  BLUE_VLAN121 | access | 121 | - | - | - |
| Ethernet43 |  BLUE_VLAN121 | access | 121 | - | - | - |
| Ethernet44 |  BLUE_VLAN121 | access | 121 | - | - | - |
| Ethernet45 |  BLUE_VLAN121 | access | 121 | - | - | - |
| Ethernet46 |  BLUE_VLAN121 | access | 121 | - | - | - |
| Ethernet47 |  BLUE_VLAN121 | access | 121 | - | - | - |
| Ethernet48 |  BLUE_VLAN121 | access | 121 | - | - | - |

*Inherited from Port-Channel Interface

##### IPv4

| Interface | Description | Type | Channel Group | IP Address | VRF |  MTU | Shutdown | ACL In | ACL Out |
| --------- | ----------- | -----| ------------- | ---------- | ----| ---- | -------- | ------ | ------- |
| Ethernet51/1 | P2P_LINK_TO_BLUE-SPINE1_Ethernet17/1 | routed | - | 10.255.255.1/31 | default | 9214 | False | - | - |

#### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet1
   description BLUE_VLAN121
   no shutdown
   switchport access vlan 121
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
   description BLUE_VLAN121
   no shutdown
   switchport access vlan 121
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
   description BLUE_VLAN121
   no shutdown
   switchport access vlan 121
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
   description BLUE_VLAN121
   no shutdown
   switchport access vlan 121
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
   description BLUE_VLAN121
   no shutdown
   switchport access vlan 121
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
   description BLUE_VLAN121
   no shutdown
   switchport access vlan 121
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
   description BLUE_VLAN121
   no shutdown
   switchport access vlan 121
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
   description BLUE_VLAN121
   no shutdown
   switchport access vlan 121
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
   description BLUE_VLAN121
   no shutdown
   switchport access vlan 121
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
   description BLUE_VLAN121
   no shutdown
   switchport access vlan 121
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
   description BLUE_VLAN121
   no shutdown
   switchport access vlan 121
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
   description BLUE_VLAN121
   no shutdown
   switchport access vlan 121
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
   description BLUE_VLAN121
   no shutdown
   switchport access vlan 121
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
   description BLUE_VLAN121
   no shutdown
   switchport access vlan 121
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
   description BLUE_VLAN121
   no shutdown
   switchport access vlan 121
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
   description BLUE_VLAN121
   no shutdown
   switchport access vlan 121
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
   description BLUE_VLAN121
   no shutdown
   switchport access vlan 121
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
   description BLUE_VLAN121
   no shutdown
   switchport access vlan 121
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
   description BLUE_VLAN121
   no shutdown
   switchport access vlan 121
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
   description BLUE_VLAN121
   no shutdown
   switchport access vlan 121
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
   description BLUE_VLAN121
   no shutdown
   switchport access vlan 121
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
   description BLUE_VLAN121
   no shutdown
   switchport access vlan 121
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
   description BLUE_VLAN121
   no shutdown
   switchport access vlan 121
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
   description BLUE_VLAN121
   no shutdown
   switchport access vlan 121
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
   description BLUE_VLAN121
   no shutdown
   switchport access vlan 121
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
   description BLUE_VLAN121
   no shutdown
   switchport access vlan 121
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
   description BLUE_VLAN121
   no shutdown
   switchport access vlan 121
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
   description BLUE_VLAN121
   no shutdown
   switchport access vlan 121
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
   description BLUE_VLAN121
   no shutdown
   switchport access vlan 121
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
   description BLUE_VLAN121
   no shutdown
   switchport access vlan 121
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
   description BLUE_VLAN121
   no shutdown
   switchport access vlan 121
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
   description BLUE_VLAN121
   no shutdown
   switchport access vlan 121
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
   description BLUE_VLAN121
   no shutdown
   switchport access vlan 121
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
   description BLUE_VLAN121
   no shutdown
   switchport access vlan 121
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
   description BLUE_VLAN121
   no shutdown
   switchport access vlan 121
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
   description BLUE_VLAN121
   no shutdown
   switchport access vlan 121
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
   description BLUE_VLAN121
   no shutdown
   switchport access vlan 121
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
   description BLUE_VLAN121
   no shutdown
   switchport access vlan 121
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
   description BLUE_VLAN121
   no shutdown
   switchport access vlan 121
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
   description BLUE_VLAN121
   no shutdown
   switchport access vlan 121
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
   description BLUE_VLAN121
   no shutdown
   switchport access vlan 121
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
   description BLUE_VLAN121
   no shutdown
   switchport access vlan 121
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
   description BLUE_VLAN121
   no shutdown
   switchport access vlan 121
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
   description BLUE_VLAN121
   no shutdown
   switchport access vlan 121
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
   description BLUE_VLAN121
   no shutdown
   switchport access vlan 121
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
   description BLUE_VLAN121
   no shutdown
   switchport access vlan 121
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
   description BLUE_VLAN121
   no shutdown
   switchport access vlan 121
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
   description BLUE_VLAN121
   no shutdown
   switchport access vlan 121
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
   description P2P_LINK_TO_BLUE-SPINE1_Ethernet17/1
   no shutdown
   mtu 9214
   no switchport
   ip address 10.255.255.1/31
   pim ipv4 sparse-mode
   ptp enable
   ptp sync-message interval -3
   ptp announce interval 0
   ptp transport ipv4
   ptp announce timeout 3
   ptp delay-req interval -3
```

### Loopback Interfaces

#### Loopback Interfaces Summary

##### IPv4

| Interface | Description | VRF | IP Address |
| --------- | ----------- | --- | ---------- |
| Loopback0 | Router_ID | default | 10.255.2.3/32 |

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
   ip address 10.255.2.3/32
```

### VLAN Interfaces

#### VLAN Interfaces Summary

| Interface | Description | VRF |  MTU | Shutdown |
| --------- | ----------- | --- | ---- | -------- |
| Vlan121 | VLAN121 | default | - | False |

##### IPv4

| Interface | VRF | IP Address | IP Address Virtual | IP Router Virtual Address | VRRP | ACL In | ACL Out |
| --------- | --- | ---------- | ------------------ | ------------------------- | ---- | ------ | ------- |
| Vlan121 |  default  |  10.252.13.1/24  |  -  |  -  |  -  |  -  |  -  |

#### VLAN Interfaces Device Configuration

```eos
!
interface Vlan121
   description VLAN121
   no shutdown
   ip address 10.252.13.1/24
   ip helper-address 10.252.4.253
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

##### Virtual Router MAC Address: 00:1c:73:00:00:99

#### Virtual Router MAC Address Configuration

```eos
!
ip virtual-router mac-address 00:1c:73:00:00:99
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
| MGMT | 0.0.0.0/0 | 10.252.0.1 | - | 1 | - | - | - |

#### Static Routes Device Configuration

```eos
!
ip route vrf MGMT 0.0.0.0/0 10.252.0.1
```

### Router BGP

#### Router BGP Summary

| BGP AS | Router ID |
| ------ | --------- |
| 65201|  10.255.2.3 |

| BGP Tuning |
| ---------- |
| graceful-restart restart-time 300 |
| graceful-restart |
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

| Neighbor | Remote AS | VRF | Shutdown | Send-community | Maximum-routes | Allowas-in | BFD | RIB Pre-Policy Retain | Route-Reflector Client | Passive |
| -------- | --------- | --- | -------- | -------------- | -------------- | ---------- | --- | --------------------- | ---------------------- | ------- |
| 10.255.255.0 | 65200 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |

#### Router BGP Device Configuration

```eos
!
router bgp 65201
   router-id 10.255.2.3
   graceful-restart restart-time 300
   graceful-restart
   maximum-paths 4 ecmp 4
   update wait-install
   no bgp default ipv4-unicast
   neighbor IPv4-UNDERLAY-PEERS peer group
   neighbor IPv4-UNDERLAY-PEERS password 7 <removed>
   neighbor IPv4-UNDERLAY-PEERS send-community
   neighbor IPv4-UNDERLAY-PEERS maximum-routes 12000
   neighbor 10.255.255.0 peer group IPv4-UNDERLAY-PEERS
   neighbor 10.255.255.0 remote-as 65200
   neighbor 10.255.255.0 description blue-spine1_Ethernet17/1
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
| Ethernet51/1 | - | IPv4 | - | - |

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
