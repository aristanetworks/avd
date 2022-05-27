# DC1-LEAF3B
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
- [Hardware TCAM Profile](#hardware-tcam-profile)
  - [Hardware TCAM configuration](#hardware-tcam-configuration)
- [MLAG](#mlag)
  - [MLAG Summary](#mlag-summary)
  - [MLAG Device Configuration](#mlag-device-configuration)
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
  - [Port-Channel Interfaces](#port-channel-interfaces)
  - [Loopback Interfaces](#loopback-interfaces)
  - [VLAN Interfaces](#vlan-interfaces)
  - [VXLAN Interface](#vxlan-interface)
- [Routing](#routing)
  - [Service Routing Protocols Model](#service-routing-protocols-model)
  - [Virtual Router MAC Address](#virtual-router-mac-address)
  - [IP Routing](#ip-routing)
  - [IPv6 Routing](#ipv6-routing)
  - [Static Routes](#static-routes)
  - [Router BGP](#router-bgp)
- [BFD](#bfd)
  - [Router BFD](#router-bfd)
- [Multicast](#multicast)
  - [IP IGMP Snooping](#ip-igmp-snooping)
- [Filters](#filters)
  - [Prefix-lists](#prefix-lists)
  - [IPv6 Prefix-lists](#ipv6-prefix-lists)
  - [Route-maps](#route-maps)
- [ACL](#acl)
- [VRF Instances](#vrf-instances)
  - [VRF Instances Summary](#vrf-instances-summary)
  - [VRF Instances Device Configuration](#vrf-instances-device-configuration)
- [Virtual Source NAT](#virtual-source-nat)
  - [Virtual Source NAT Summary](#virtual-source-nat-summary)
  - [Virtual Source NAT Configuration](#virtual-source-nat-configuration)
- [Platform](#platform)
  - [Platform Summary](#platform-summary)
  - [Platform Configuration](#platform-configuration)
- [Quality Of Service](#quality-of-service)

# Management

## Management Interfaces

### Management Interfaces Summary

#### IPv4

| Management Interface | description | Type | VRF | IP Address | Gateway |
| -------------------- | ----------- | ---- | --- | ---------- | ------- |
| Management1 | oob_management | oob | MGMT | 192.168.200.107/24 | 192.168.200.5 |

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
   ip address 192.168.200.107/24
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
| gzip | 192.168.200.11:9910 | MGMT | key,telarista | ale,flexCounter,hardware,kni,pulse,strata | /Sysdb/cell/1/agent,/Sysdb/cell/2/agent | False |

### TerminAttr Daemon Device Configuration

```eos
!
daemon TerminAttr
   exec /usr/bin/TerminAttr -cvaddr=192.168.200.11:9910 -cvauth=key,telarista -cvvrf=MGMT -smashexcludes=ale,flexCounter,hardware,kni,pulse,strata -ingestexclude=/Sysdb/cell/1/agent,/Sysdb/cell/2/agent -taillogs
   no shutdown
```

# Hardware TCAM Profile

TCAM profile __`vxlan-routing`__ is active

## Hardware TCAM configuration

```eos
!
hardware tcam
   system profile vxlan-routing
```

# MLAG

## MLAG Summary

| Domain-id | Local-interface | Peer-address | Peer-link |
| --------- | --------------- | ------------ | --------- |
| DC1_LEAF3 | Vlan4094 | 10.255.252.14 | Port-Channel5 |

Dual primary detection is disabled.

## MLAG Device Configuration

```eos
!
mlag configuration
   domain-id DC1_LEAF3
   local-interface Vlan4094
   peer-address 10.255.252.14
   peer-link Port-Channel5
   reload-delay mlag 900
   reload-delay non-mlag 1020
```

# Spanning Tree

## Spanning Tree Summary

STP mode: **mstp**

### MSTP Instance and Priority

| Instance(s) | Priority |
| -------- | -------- |
| 0 | 4096 |

### Global Spanning-Tree Settings

- Spanning Tree disabled for VLANs: **4093-4094**

## Spanning Tree Device Configuration

```eos
!
spanning-tree mode mstp
no spanning-tree vlan-id 4093-4094
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
| 2 | MLAG_iBGP_Tenant_C_OP_Zone | LEAF_PEER_L3 |
| 110 | Tenant_A_OP_Zone_1 | - |
| 111 | Tenant_A_OP_Zone_2 | - |
| 120 | Tenant_A_WEB_Zone_1 | - |
| 121 | Tenant_A_WEBZone_2 | - |
| 130 | Tenant_A_APP_Zone_1 | - |
| 131 | Tenant_A_APP_Zone_2 | - |
| 140 | Tenant_A_DB_BZone_1 | - |
| 141 | Tenant_A_DB_Zone_2 | - |
| 160 | Tenant_A_VMOTION | - |
| 161 | Tenant_A_NFS | - |
| 210 | Tenant_B_OP_Zone_1 | - |
| 211 | Tenant_B_OP_Zone_2 | - |
| 310 | Tenant_C_OP_Zone_1 | - |
| 311 | Tenant_C_OP_Zone_2 | - |
| 3009 | MLAG_iBGP_Tenant_A_OP_Zone | LEAF_PEER_L3 |
| 3010 | MLAG_iBGP_Tenant_A_WEB_Zone | LEAF_PEER_L3 |
| 3011 | MLAG_iBGP_Tenant_A_APP_Zone | LEAF_PEER_L3 |
| 3012 | MLAG_iBGP_Tenant_A_DB_Zone | LEAF_PEER_L3 |
| 3019 | MLAG_iBGP_Tenant_B_OP_Zone | LEAF_PEER_L3 |
| 4093 | LEAF_PEER_L3 | LEAF_PEER_L3 |
| 4094 | MLAG_PEER | MLAG |

## VLANs Device Configuration

```eos
!
vlan 2
   name MLAG_iBGP_Tenant_C_OP_Zone
   trunk group LEAF_PEER_L3
!
vlan 110
   name Tenant_A_OP_Zone_1
!
vlan 111
   name Tenant_A_OP_Zone_2
!
vlan 120
   name Tenant_A_WEB_Zone_1
!
vlan 121
   name Tenant_A_WEBZone_2
!
vlan 130
   name Tenant_A_APP_Zone_1
!
vlan 131
   name Tenant_A_APP_Zone_2
!
vlan 140
   name Tenant_A_DB_BZone_1
!
vlan 141
   name Tenant_A_DB_Zone_2
!
vlan 160
   name Tenant_A_VMOTION
!
vlan 161
   name Tenant_A_NFS
!
vlan 210
   name Tenant_B_OP_Zone_1
!
vlan 211
   name Tenant_B_OP_Zone_2
!
vlan 310
   name Tenant_C_OP_Zone_1
!
vlan 311
   name Tenant_C_OP_Zone_2
!
vlan 3009
   name MLAG_iBGP_Tenant_A_OP_Zone
   trunk group LEAF_PEER_L3
!
vlan 3010
   name MLAG_iBGP_Tenant_A_WEB_Zone
   trunk group LEAF_PEER_L3
!
vlan 3011
   name MLAG_iBGP_Tenant_A_APP_Zone
   trunk group LEAF_PEER_L3
!
vlan 3012
   name MLAG_iBGP_Tenant_A_DB_Zone
   trunk group LEAF_PEER_L3
!
vlan 3019
   name MLAG_iBGP_Tenant_B_OP_Zone
   trunk group LEAF_PEER_L3
!
vlan 4093
   name LEAF_PEER_L3
   trunk group LEAF_PEER_L3
!
vlan 4094
   name MLAG_PEER
   trunk group MLAG
```

# Interfaces

## Ethernet Interfaces

### Ethernet Interfaces Summary

#### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | Channel-Group |
| --------- | ----------- | ---- | ----- | ----------- | ----------- | ------------- |
| Ethernet5 | MLAG_PEER_DC1-LEAF3A_Ethernet5 | *trunk | *2-4094 | *- | *['LEAF_PEER_L3', 'MLAG'] | 5 |
| Ethernet6 | MLAG_PEER_DC1-LEAF3A_Ethernet6 | *trunk | *2-4094 | *- | *['LEAF_PEER_L3', 'MLAG'] | 5 |

*Inherited from Port-Channel Interface

#### IPv6

| Interface | Description | Type | Channel Group | IPv6 Address | VRF | MTU | Shutdown | ND RA Disabled | Managed Config Flag | IPv6 ACL In | IPv6 ACL Out |
| --------- | ----------- | ---- | --------------| ------------ | --- | --- | -------- | -------------- | -------------------| ----------- | ------------ |
| Ethernet1 | P2P_LINK_TO_DC1-SPINE5_Ethernet2 | routed | - | - | default | 1500 | false | - | - | - | - |

### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet1
   description P2P_LINK_TO_DC1-SPINE5_Ethernet2
   no shutdown
   mtu 1500
   no switchport
   ipv6 enable
!
interface Ethernet5
   description MLAG_PEER_DC1-LEAF3A_Ethernet5
   no shutdown
   channel-group 5 mode active
!
interface Ethernet6
   description MLAG_PEER_DC1-LEAF3A_Ethernet6
   no shutdown
   channel-group 5 mode active
```

## Port-Channel Interfaces

### Port-Channel Interfaces Summary

#### L2

| Interface | Description | Type | Mode | VLANs | Native VLAN | Trunk Group | LACP Fallback Timeout | LACP Fallback Mode | MLAG ID | EVPN ESI |
| --------- | ----------- | ---- | ---- | ----- | ----------- | ------------| --------------------- | ------------------ | ------- | -------- |
| Port-Channel5 | MLAG_PEER_DC1-LEAF3A_Po5 | switched | trunk | 2-4094 | - | ['LEAF_PEER_L3', 'MLAG'] | - | - | - | - |

### Port-Channel Interfaces Device Configuration

```eos
!
interface Port-Channel5
   description MLAG_PEER_DC1-LEAF3A_Po5
   no shutdown
   switchport
   switchport trunk allowed vlan 2-4094
   switchport mode trunk
   switchport trunk group LEAF_PEER_L3
   switchport trunk group MLAG
```

## Loopback Interfaces

### Loopback Interfaces Summary

#### IPv4

| Interface | Description | VRF | IP Address |
| --------- | ----------- | --- | ---------- |
| Loopback0 | EVPN_Overlay_Peering | default | 192.168.255.13/32 |
| Loopback1 | VTEP_VXLAN_Tunnel_Source | default | 192.168.254.12/32 |
| Loopback100 | Tenant_A_OP_Zone_VTEP_DIAGNOSTICS | Tenant_A_OP_Zone | 10.255.1.13/32 |

#### IPv6

| Interface | Description | VRF | IPv6 Address |
| --------- | ----------- | --- | ------------ |
| Loopback0 | EVPN_Overlay_Peering | default | 2001:1::d/128 |
| Loopback1 | VTEP_VXLAN_Tunnel_Source | default | - |
| Loopback100 | Tenant_A_OP_Zone_VTEP_DIAGNOSTICS | Tenant_A_OP_Zone | - |


### Loopback Interfaces Device Configuration

```eos
!
interface Loopback0
   description EVPN_Overlay_Peering
   no shutdown
   ip address 192.168.255.13/32
   ipv6 address 2001:1::d/128
!
interface Loopback1
   description VTEP_VXLAN_Tunnel_Source
   no shutdown
   ip address 192.168.254.12/32
!
interface Loopback100
   description Tenant_A_OP_Zone_VTEP_DIAGNOSTICS
   no shutdown
   vrf Tenant_A_OP_Zone
   ip address 10.255.1.13/32
```

## VLAN Interfaces

### VLAN Interfaces Summary

| Interface | Description | VRF |  MTU | Shutdown |
| --------- | ----------- | --- | ---- | -------- |
| Vlan2 | MLAG_PEER_L3_iBGP: vrf Tenant_C_OP_Zone | Tenant_C_OP_Zone | 1500 | false |
| Vlan110 | Tenant_A_OP_Zone_1 | Tenant_A_OP_Zone | - | false |
| Vlan111 | Tenant_A_OP_Zone_2 | Tenant_A_OP_Zone | - | false |
| Vlan120 | Tenant_A_WEB_Zone_1 | Tenant_A_WEB_Zone | - | false |
| Vlan121 | Tenant_A_WEBZone_2 | Tenant_A_WEB_Zone | 1560 | true |
| Vlan130 | Tenant_A_APP_Zone_1 | Tenant_A_APP_Zone | - | false |
| Vlan131 | Tenant_A_APP_Zone_2 | Tenant_A_APP_Zone | - | false |
| Vlan140 | Tenant_A_DB_BZone_1 | Tenant_A_DB_Zone | - | false |
| Vlan141 | Tenant_A_DB_Zone_2 | Tenant_A_DB_Zone | - | false |
| Vlan210 | Tenant_B_OP_Zone_1 | Tenant_B_OP_Zone | - | false |
| Vlan211 | Tenant_B_OP_Zone_2 | Tenant_B_OP_Zone | - | false |
| Vlan310 | Tenant_C_OP_Zone_1 | Tenant_C_OP_Zone | - | false |
| Vlan311 | Tenant_C_OP_Zone_2 | Tenant_C_OP_Zone | - | false |
| Vlan3009 | MLAG_PEER_L3_iBGP: vrf Tenant_A_OP_Zone | Tenant_A_OP_Zone | 1500 | false |
| Vlan3010 | MLAG_PEER_L3_iBGP: vrf Tenant_A_WEB_Zone | Tenant_A_WEB_Zone | 1500 | false |
| Vlan3011 | MLAG_PEER_L3_iBGP: vrf Tenant_A_APP_Zone | Tenant_A_APP_Zone | 1500 | false |
| Vlan3012 | MLAG_PEER_L3_iBGP: vrf Tenant_A_DB_Zone | Tenant_A_DB_Zone | 1500 | false |
| Vlan3019 | MLAG_PEER_L3_iBGP: vrf Tenant_B_OP_Zone | Tenant_B_OP_Zone | 1500 | false |
| Vlan4093 | MLAG_PEER_L3_PEERING | default | 1500 | false |
| Vlan4094 | MLAG_PEER | default | 1500 | false |

#### IPv4

| Interface | VRF | IP Address | IP Address Virtual | IP Router Virtual Address | VRRP | ACL In | ACL Out |
| --------- | --- | ---------- | ------------------ | ------------------------- | ---- | ------ | ------- |
| Vlan2 |  Tenant_C_OP_Zone  |  -  |  -  |  -  |  -  |  -  |  -  |
| Vlan110 |  Tenant_A_OP_Zone  |  -  |  10.1.10.1/24  |  -  |  -  |  -  |  -  |
| Vlan111 |  Tenant_A_OP_Zone  |  -  |  10.1.11.1/24  |  -  |  -  |  -  |  -  |
| Vlan120 |  Tenant_A_WEB_Zone  |  -  |  10.1.20.1/24  |  -  |  -  |  -  |  -  |
| Vlan121 |  Tenant_A_WEB_Zone  |  -  |  10.1.10.254/24  |  -  |  -  |  -  |  -  |
| Vlan130 |  Tenant_A_APP_Zone  |  -  |  10.1.30.1/24  |  -  |  -  |  -  |  -  |
| Vlan131 |  Tenant_A_APP_Zone  |  -  |  10.1.31.1/24  |  -  |  -  |  -  |  -  |
| Vlan140 |  Tenant_A_DB_Zone  |  -  |  10.1.40.1/24  |  -  |  -  |  -  |  -  |
| Vlan141 |  Tenant_A_DB_Zone  |  -  |  10.1.41.1/24  |  -  |  -  |  -  |  -  |
| Vlan210 |  Tenant_B_OP_Zone  |  -  |  10.2.10.1/24  |  -  |  -  |  -  |  -  |
| Vlan211 |  Tenant_B_OP_Zone  |  -  |  10.2.11.1/24  |  -  |  -  |  -  |  -  |
| Vlan310 |  Tenant_C_OP_Zone  |  -  |  10.3.10.1/24  |  -  |  -  |  -  |  -  |
| Vlan311 |  Tenant_C_OP_Zone  |  -  |  10.3.11.1/24  |  -  |  -  |  -  |  -  |
| Vlan3009 |  Tenant_A_OP_Zone  |  -  |  -  |  -  |  -  |  -  |  -  |
| Vlan3010 |  Tenant_A_WEB_Zone  |  -  |  -  |  -  |  -  |  -  |  -  |
| Vlan3011 |  Tenant_A_APP_Zone  |  -  |  -  |  -  |  -  |  -  |  -  |
| Vlan3012 |  Tenant_A_DB_Zone  |  -  |  -  |  -  |  -  |  -  |  -  |
| Vlan3019 |  Tenant_B_OP_Zone  |  -  |  -  |  -  |  -  |  -  |  -  |
| Vlan4093 |  default  |  -  |  -  |  -  |  -  |  -  |  -  |
| Vlan4094 |  default  |  10.255.252.15/31  |  -  |  -  |  -  |  -  |  -  |

### VLAN Interfaces Device Configuration

```eos
!
interface Vlan2
   description MLAG_PEER_L3_iBGP: vrf Tenant_C_OP_Zone
   no shutdown
   mtu 1500
   vrf Tenant_C_OP_Zone
   ipv6 enable
!
interface Vlan110
   description Tenant_A_OP_Zone_1
   no shutdown
   vrf Tenant_A_OP_Zone
   ip address virtual 10.1.10.1/24
!
interface Vlan111
   description Tenant_A_OP_Zone_2
   no shutdown
   vrf Tenant_A_OP_Zone
   ip helper-address 1.1.1.1 vrf MGMT source-interface lo100
   ip address virtual 10.1.11.1/24
!
interface Vlan120
   description Tenant_A_WEB_Zone_1
   no shutdown
   vrf Tenant_A_WEB_Zone
   ip helper-address 1.1.1.1 vrf TEST source-interface lo100
   ip address virtual 10.1.20.1/24
!
interface Vlan121
   description Tenant_A_WEBZone_2
   shutdown
   mtu 1560
   vrf Tenant_A_WEB_Zone
   ip address virtual 10.1.10.254/24
!
interface Vlan130
   description Tenant_A_APP_Zone_1
   no shutdown
   vrf Tenant_A_APP_Zone
   ip address virtual 10.1.30.1/24
!
interface Vlan131
   description Tenant_A_APP_Zone_2
   no shutdown
   vrf Tenant_A_APP_Zone
   ip address virtual 10.1.31.1/24
!
interface Vlan140
   description Tenant_A_DB_BZone_1
   no shutdown
   vrf Tenant_A_DB_Zone
   ip address virtual 10.1.40.1/24
!
interface Vlan141
   description Tenant_A_DB_Zone_2
   no shutdown
   vrf Tenant_A_DB_Zone
   ip address virtual 10.1.41.1/24
!
interface Vlan210
   description Tenant_B_OP_Zone_1
   no shutdown
   vrf Tenant_B_OP_Zone
   ip address virtual 10.2.10.1/24
!
interface Vlan211
   description Tenant_B_OP_Zone_2
   no shutdown
   vrf Tenant_B_OP_Zone
   ip address virtual 10.2.11.1/24
!
interface Vlan310
   description Tenant_C_OP_Zone_1
   no shutdown
   vrf Tenant_C_OP_Zone
   ip address virtual 10.3.10.1/24
!
interface Vlan311
   description Tenant_C_OP_Zone_2
   no shutdown
   vrf Tenant_C_OP_Zone
   ip address virtual 10.3.11.1/24
!
interface Vlan3009
   description MLAG_PEER_L3_iBGP: vrf Tenant_A_OP_Zone
   no shutdown
   mtu 1500
   vrf Tenant_A_OP_Zone
   ipv6 enable
!
interface Vlan3010
   description MLAG_PEER_L3_iBGP: vrf Tenant_A_WEB_Zone
   no shutdown
   mtu 1500
   vrf Tenant_A_WEB_Zone
   ipv6 enable
!
interface Vlan3011
   description MLAG_PEER_L3_iBGP: vrf Tenant_A_APP_Zone
   no shutdown
   mtu 1500
   vrf Tenant_A_APP_Zone
   ipv6 enable
!
interface Vlan3012
   description MLAG_PEER_L3_iBGP: vrf Tenant_A_DB_Zone
   no shutdown
   mtu 1500
   vrf Tenant_A_DB_Zone
   ipv6 enable
!
interface Vlan3019
   description MLAG_PEER_L3_iBGP: vrf Tenant_B_OP_Zone
   no shutdown
   mtu 1500
   vrf Tenant_B_OP_Zone
   ipv6 enable
!
interface Vlan4093
   description MLAG_PEER_L3_PEERING
   no shutdown
   mtu 1500
   ipv6 enable
!
interface Vlan4094
   description MLAG_PEER
   no shutdown
   mtu 1500
   no autostate
   ip address 10.255.252.15/31
```

## VXLAN Interface

### VXLAN Interface Summary

| Setting | Value |
| ------- | ----- |
| Source Interface | Loopback1 |
| UDP port | 4789 |
| EVPN MLAG Shared Router MAC | mlag-system-id |

#### VLAN to VNI, Flood List and Multicast Group Mappings

| VLAN | VNI | Flood List | Multicast Group |
| ---- | --- | ---------- | --------------- |
| 110 | 10110 | - | - |
| 111 | 50111 | - | - |
| 120 | 10120 | - | - |
| 121 | 10121 | - | - |
| 130 | 10130 | - | - |
| 131 | 10131 | - | - |
| 140 | 10140 | - | - |
| 141 | 10141 | - | - |
| 160 | 10160 | - | - |
| 161 | 10161 | - | - |
| 210 | 20210 | - | - |
| 211 | 20211 | - | - |
| 310 | 30310 | - | - |
| 311 | 30311 | - | - |

#### VRF to VNI and Multicast Group Mappings

| VRF | VNI | Multicast Group |
| ---- | --- | --------------- |
| Tenant_A_APP_Zone | 12 | - |
| Tenant_A_DB_Zone | 13 | - |
| Tenant_A_OP_Zone | 10 | - |
| Tenant_A_WEB_Zone | 11 | - |
| Tenant_B_OP_Zone | 20 | - |
| Tenant_C_OP_Zone | 30 | - |

### VXLAN Interface Device Configuration

```eos
!
interface Vxlan1
   description DC1-LEAF3B_VTEP
   vxlan source-interface Loopback1
   vxlan virtual-router encapsulation mac-address mlag-system-id
   vxlan udp-port 4789
   vxlan vlan 110 vni 10110
   vxlan vlan 111 vni 50111
   vxlan vlan 120 vni 10120
   vxlan vlan 121 vni 10121
   vxlan vlan 130 vni 10130
   vxlan vlan 131 vni 10131
   vxlan vlan 140 vni 10140
   vxlan vlan 141 vni 10141
   vxlan vlan 160 vni 10160
   vxlan vlan 161 vni 10161
   vxlan vlan 210 vni 20210
   vxlan vlan 211 vni 20211
   vxlan vlan 310 vni 30310
   vxlan vlan 311 vni 30311
   vxlan vrf Tenant_A_APP_Zone vni 12
   vxlan vrf Tenant_A_DB_Zone vni 13
   vxlan vrf Tenant_A_OP_Zone vni 10
   vxlan vrf Tenant_A_WEB_Zone vni 11
   vxlan vrf Tenant_B_OP_Zone vni 20
   vxlan vrf Tenant_C_OP_Zone vni 30
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

#### Virtual Router MAC Address: 00:dc:00:00:00:0a

### Virtual Router MAC Address Configuration

```eos
!
ip virtual-router mac-address 00:dc:00:00:00:0a
```

## IP Routing

### IP Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | true |
| MGMT | false |
| Tenant_A_APP_Zone | true |
| Tenant_A_DB_Zone | true |
| Tenant_A_OP_Zone | true |
| Tenant_A_WEB_Zone | true |
| Tenant_B_OP_Zone | true |
| Tenant_C_OP_Zone | true |

### IP Routing Device Configuration

```eos
!
ip routing
no ip routing vrf MGMT
ip routing vrf Tenant_A_APP_Zone
ip routing vrf Tenant_A_DB_Zone
ip routing vrf Tenant_A_OP_Zone
ip routing vrf Tenant_A_WEB_Zone
ip routing vrf Tenant_B_OP_Zone
ip routing vrf Tenant_C_OP_Zone
```
## IPv6 Routing

### IPv6 Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | true |
| MGMT | false |
| Tenant_A_APP_Zone | false |
| Tenant_A_DB_Zone | false |
| Tenant_A_OP_Zone | false |
| Tenant_A_WEB_Zone | false |
| Tenant_B_OP_Zone | false |
| Tenant_C_OP_Zone | false |

### IPv6 Routing Device Configuration

```eos
!
ipv6 unicast-routing
ip routing ipv6 interfaces
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

## Router BGP

### Router BGP Summary

| BGP AS | Router ID |
| ------ | --------- |
| 65106|  192.168.255.13 |

| BGP Tuning |
| ---------- |
| no bgp default ipv4-unicast |
| distance bgp 20 200 200 |
| maximum-paths 4 ecmp 4 |

### Router BGP Peer Groups

#### EVPN-OVERLAY-PEERS

| Settings | Value |
| -------- | ----- |
| Address Family | evpn |
| Source | Loopback0 |
| BFD | True |
| Ebgp multihop | 3 |
| Send community | all |
| Maximum routes | 0 (no limit) |

#### MLAG_PEER

| Settings | Value |
| -------- | ----- |
| Address Family | ipv4 |
| Remote AS | 65106 |
| Next-hop self | True |
| Send community | all |
| Maximum routes | 12000 |

#### UNDERLAY_PEERS

| Settings | Value |
| -------- | ----- |
| Address Family | ipv4 |
| Send community | all |
| Maximum routes | 12000 |

### BGP Neighbors

| Neighbor | Remote AS | VRF | Shutdown | Send-community | Maximum-routes | Allowas-in | BFD | RIB Pre-Policy Retain |
| -------- | --------- | --- | -------- | -------------- | -------------- | ---------- | --- | --------------------- |
| 2001:1::5 | 65001 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - |

### BGP Neighbor Interfaces

| Neighbor Interface | VRF | Peer Group | Remote AS | Peer Filter |
| ------------------ | --- | ---------- | --------- | ----------- |
| Ethernet1 | default | UNDERLAY_PEERS | 65001 | - |
| Vlan4093 | default | MLAG_PEER | 65106 | - |
| Vlan3011 | Tenant_A_APP_Zone | MLAG_PEER | 65106 | - |
| Vlan3012 | Tenant_A_DB_Zone | MLAG_PEER | 65106 | - |
| Vlan3009 | Tenant_A_OP_Zone | MLAG_PEER | 65106 | - |
| Vlan3010 | Tenant_A_WEB_Zone | MLAG_PEER | 65106 | - |
| Vlan3019 | Tenant_B_OP_Zone | MLAG_PEER | 65106 | - |
| Vlan2 | Tenant_C_OP_Zone | MLAG_PEER | 65106 | - |

### Router BGP EVPN Address Family

#### EVPN Peer Groups

| Peer Group | Activate |
| ---------- | -------- |
| EVPN-OVERLAY-PEERS | True |

#### EVPN Host Flapping Settings

| State | Window | Threshold | Expiry Timeout |
| ----- | ------ | --------- | -------------- |
| Enabled | 20 Seconds | 30 | - |

### Router BGP VLAN Aware Bundles

| VLAN Aware Bundle | Route-Distinguisher | Both Route-Target | Import Route Target | Export Route-Target | Redistribute | VLANs |
| ----------------- | ------------------- | ----------------- | ------------------- | ------------------- | ------------ | ----- |
| Tenant_A_APP_Zone | 192.168.255.13:12 | 12:12 | - | - | learned | 130-131 |
| Tenant_A_DB_Zone | 192.168.255.13:13 | 13:13 | - | - | learned | 140-141 |
| Tenant_A_NFS | 192.168.255.13:10161 | 10161:10161 | - | - | learned | 161 |
| Tenant_A_OP_Zone | 192.168.255.13:10 | 10:10 | - | - | learned | 110-111 |
| Tenant_A_VMOTION | 192.168.255.13:10160 | 10160:10160 | - | - | learned | 160 |
| Tenant_A_WEB_Zone | 192.168.255.13:11 | 11:11 | - | - | learned | 120-121 |
| Tenant_B_OP_Zone | 192.168.255.13:20 | 20:20 | - | - | learned | 210-211 |
| Tenant_C_OP_Zone | 192.168.255.13:30 | 30:30 | - | - | learned | 310-311 |

### Router BGP VRFs

| VRF | Route-Distinguisher | Redistribute |
| --- | ------------------- | ------------ |
| Tenant_A_APP_Zone | 192.168.255.13:12 | connected |
| Tenant_A_DB_Zone | 192.168.255.13:13 | connected |
| Tenant_A_OP_Zone | 192.168.255.13:10 | connected |
| Tenant_A_WEB_Zone | 192.168.255.13:11 | connected |
| Tenant_B_OP_Zone | 192.168.255.13:20 | connected |
| Tenant_C_OP_Zone | 192.168.255.13:30 | connected |

### Router BGP Device Configuration

```eos
!
router bgp 65106
   router-id 192.168.255.13
   no bgp default ipv4-unicast
   distance bgp 20 200 200
   maximum-paths 4 ecmp 4
   neighbor EVPN-OVERLAY-PEERS peer group
   neighbor EVPN-OVERLAY-PEERS update-source Loopback0
   neighbor EVPN-OVERLAY-PEERS bfd
   neighbor EVPN-OVERLAY-PEERS ebgp-multihop 3
   neighbor EVPN-OVERLAY-PEERS password 7 q+VNViP5i4rVjW1cxFv2wA==
   neighbor EVPN-OVERLAY-PEERS send-community
   neighbor EVPN-OVERLAY-PEERS maximum-routes 0
   neighbor MLAG_PEER peer group
   neighbor MLAG_PEER remote-as 65106
   neighbor MLAG_PEER next-hop-self
   neighbor MLAG_PEER description DC1-LEAF3A
   neighbor MLAG_PEER password 7 vnEaG8gMeQf3d3cN6PktXQ==
   neighbor MLAG_PEER send-community
   neighbor MLAG_PEER maximum-routes 12000
   neighbor MLAG_PEER route-map RM-MLAG-PEER-IN in
   neighbor UNDERLAY_PEERS peer group
   neighbor UNDERLAY_PEERS password 7 AQQvKeimxJu+uGQ/yYvv9w==
   neighbor UNDERLAY_PEERS send-community
   neighbor UNDERLAY_PEERS maximum-routes 12000
   neighbor interface Ethernet1 peer-group UNDERLAY_PEERS remote-as 65001
   neighbor interface Vlan4093 peer-group MLAG_PEER remote-as 65106
   neighbor 2001:1::5 peer group EVPN-OVERLAY-PEERS
   neighbor 2001:1::5 remote-as 65001
   neighbor 2001:1::5 description DC1-SPINE5
   redistribute connected route-map RM-CONN-2-BGP
   !
   vlan-aware-bundle Tenant_A_APP_Zone
      rd 192.168.255.13:12
      route-target both 12:12
      redistribute learned
      vlan 130-131
   !
   vlan-aware-bundle Tenant_A_DB_Zone
      rd 192.168.255.13:13
      route-target both 13:13
      redistribute learned
      vlan 140-141
   !
   vlan-aware-bundle Tenant_A_NFS
      rd 192.168.255.13:10161
      route-target both 10161:10161
      redistribute learned
      vlan 161
   !
   vlan-aware-bundle Tenant_A_OP_Zone
      rd 192.168.255.13:10
      route-target both 10:10
      redistribute learned
      vlan 110-111
   !
   vlan-aware-bundle Tenant_A_VMOTION
      rd 192.168.255.13:10160
      route-target both 10160:10160
      redistribute learned
      vlan 160
   !
   vlan-aware-bundle Tenant_A_WEB_Zone
      rd 192.168.255.13:11
      route-target both 11:11
      redistribute learned
      vlan 120-121
   !
   vlan-aware-bundle Tenant_B_OP_Zone
      rd 192.168.255.13:20
      route-target both 20:20
      redistribute learned
      vlan 210-211
   !
   vlan-aware-bundle Tenant_C_OP_Zone
      rd 192.168.255.13:30
      route-target both 30:30
      redistribute learned
      vlan 310-311
   !
   address-family evpn
      host-flap detection window 20 threshold 30
      neighbor EVPN-OVERLAY-PEERS activate
   !
   address-family ipv4
      no neighbor EVPN-OVERLAY-PEERS activate
      neighbor MLAG_PEER next-hop address-family ipv6 originate
      neighbor MLAG_PEER activate
      neighbor UNDERLAY_PEERS next-hop address-family ipv6 originate
      neighbor UNDERLAY_PEERS activate
   !
   address-family ipv6
      neighbor MLAG_PEER activate
      neighbor UNDERLAY_PEERS activate
   !
   vrf Tenant_A_APP_Zone
      rd 192.168.255.13:12
      route-target import evpn 12:12
      route-target export evpn 12:12
      router-id 192.168.255.13
      neighbor interface Vlan3011 peer-group MLAG_PEER remote-as 65106
      redistribute connected
   !
   vrf Tenant_A_DB_Zone
      rd 192.168.255.13:13
      route-target import evpn 13:13
      route-target export evpn 13:13
      router-id 192.168.255.13
      neighbor interface Vlan3012 peer-group MLAG_PEER remote-as 65106
      redistribute connected
   !
   vrf Tenant_A_OP_Zone
      rd 192.168.255.13:10
      route-target import evpn 10:10
      route-target export evpn 10:10
      router-id 192.168.255.13
      neighbor interface Vlan3009 peer-group MLAG_PEER remote-as 65106
      redistribute connected
   !
   vrf Tenant_A_WEB_Zone
      rd 192.168.255.13:11
      route-target import evpn 11:11
      route-target export evpn 11:11
      router-id 192.168.255.13
      neighbor interface Vlan3010 peer-group MLAG_PEER remote-as 65106
      redistribute connected
   !
   vrf Tenant_B_OP_Zone
      rd 192.168.255.13:20
      route-target import evpn 20:20
      route-target export evpn 20:20
      router-id 192.168.255.13
      neighbor interface Vlan3019 peer-group MLAG_PEER remote-as 65106
      redistribute connected
   !
   vrf Tenant_C_OP_Zone
      rd 192.168.255.13:30
      route-target import evpn 30:30
      route-target export evpn 30:30
      router-id 192.168.255.13
      neighbor interface Vlan2 peer-group MLAG_PEER remote-as 65106
      redistribute connected
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

## IP IGMP Snooping

### IP IGMP Snooping Summary

| IGMP Snooping | Fast Leave | Interface Restart Query | Proxy | Restart Query Interval | Robustness Variable |
| ------------- | ---------- | ----------------------- | ----- | ---------------------- | ------------------- |
| Enabled | - | - | - | - | - |

#### IP IGMP Snooping Vlan Summary

| Vlan | IGMP Snooping | Fast Leave | Max Groups | Proxy |
| ---- | ------------- | ---------- | ---------- | ----- |
| 120 | False | - | - | - |

### IP IGMP Snooping Device Configuration

```eos
!
no ip igmp snooping vlan 120
```

# Filters

## Prefix-lists

### Prefix-lists Summary

#### PL-LOOPBACKS-EVPN-OVERLAY

| Sequence | Action |
| -------- | ------ |
| 10 | permit 192.168.255.0/24 eq 32 |
| 20 | permit 192.168.254.0/24 eq 32 |

### Prefix-lists Device Configuration

```eos
!
ip prefix-list PL-LOOPBACKS-EVPN-OVERLAY
   seq 10 permit 192.168.255.0/24 eq 32
   seq 20 permit 192.168.254.0/24 eq 32
```

## IPv6 Prefix-lists

### IPv6 Prefix-lists Summary

#### PL-LOOPBACKS-EVPN-OVERLAY-V6

| Sequence | Action |
| -------- | ------ |
| 10 | permit 2001:1::/64 eq 128 |

### IPv6 Prefix-lists Device Configuration

```eos
!
ipv6 prefix-list PL-LOOPBACKS-EVPN-OVERLAY-V6
   seq 10 permit 2001:1::/64 eq 128
```

## Route-maps

### Route-maps Summary

#### RM-CONN-2-BGP

| Sequence | Type | Match and/or Set |
| -------- | ---- | ---------------- |
| 10 | permit | match ip address prefix-list PL-LOOPBACKS-EVPN-OVERLAY |
| 30 | permit | match ipv6 address prefix-list PL-LOOPBACKS-EVPN-OVERLAY-V6 |

#### RM-MLAG-PEER-IN

| Sequence | Type | Match and/or Set |
| -------- | ---- | ---------------- |
| 10 | permit | set origin incomplete |

### Route-maps Device Configuration

```eos
!
route-map RM-CONN-2-BGP permit 10
   match ip address prefix-list PL-LOOPBACKS-EVPN-OVERLAY
!
route-map RM-CONN-2-BGP permit 30
   match ipv6 address prefix-list PL-LOOPBACKS-EVPN-OVERLAY-V6
!
route-map RM-MLAG-PEER-IN permit 10
   description Make routes learned over MLAG Peer-link less preferred on spines to ensure optimal routing
   set origin incomplete
```

# ACL

# VRF Instances

## VRF Instances Summary

| VRF Name | IP Routing |
| -------- | ---------- |
| MGMT | disabled |
| Tenant_A_APP_Zone | enabled |
| Tenant_A_DB_Zone | enabled |
| Tenant_A_OP_Zone | enabled |
| Tenant_A_WEB_Zone | enabled |
| Tenant_B_OP_Zone | enabled |
| Tenant_C_OP_Zone | enabled |

## VRF Instances Device Configuration

```eos
!
vrf instance MGMT
!
vrf instance Tenant_A_APP_Zone
!
vrf instance Tenant_A_DB_Zone
!
vrf instance Tenant_A_OP_Zone
!
vrf instance Tenant_A_WEB_Zone
!
vrf instance Tenant_B_OP_Zone
!
vrf instance Tenant_C_OP_Zone
```

# Virtual Source NAT

## Virtual Source NAT Summary

| Source NAT VRF | Source NAT IP Address |
| -------------- | --------------------- |
| Tenant_A_OP_Zone | 10.255.1.13 |

## Virtual Source NAT Configuration

```eos
!
ip address virtual source-nat vrf Tenant_A_OP_Zone address 10.255.1.13
```

# Platform

## Platform Summary

### Platform Sand Summary

| Settings | Value |
| -------- | ----- |
| Hardware Only Lag | True |

## Platform Configuration

```eos
!
platform sand lag hardware-only
```

# Quality Of Service
