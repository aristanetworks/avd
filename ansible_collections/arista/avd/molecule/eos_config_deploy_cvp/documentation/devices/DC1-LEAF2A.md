# DC1-LEAF2A

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
  - [IP Name Servers](#ip-name-servers)
  - [NTP](#ntp)
  - [Management API HTTP](#management-api-http)
- [Authentication](#authentication)
  - [Local Users](#local-users)
  - [Enable Password](#enable-password)
- [Monitoring](#monitoring)
  - [TerminAttr Daemon](#terminattr-daemon)
- [MLAG](#mlag)
  - [MLAG Summary](#mlag-summary)
  - [MLAG Device Configuration](#mlag-device-configuration)
- [Spanning Tree](#spanning-tree)
  - [Spanning Tree Summary](#spanning-tree-summary)
  - [Spanning Tree Device Configuration](#spanning-tree-device-configuration)
- [Internal VLAN Allocation Policy](#internal-vlan-allocation-policy)
  - [Internal VLAN Allocation Policy Summary](#internal-vlan-allocation-policy-summary)
  - [Internal VLAN Allocation Policy Device Configuration](#internal-vlan-allocation-policy-device-configuration)
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
  - [Route-maps](#route-maps)
- [VRF Instances](#vrf-instances)
  - [VRF Instances Summary](#vrf-instances-summary)
  - [VRF Instances Device Configuration](#vrf-instances-device-configuration)
- [Virtual Source NAT](#virtual-source-nat)
  - [Virtual Source NAT Summary](#virtual-source-nat-summary)
  - [Virtual Source NAT Configuration](#virtual-source-nat-configuration)

## Management

### Management Interfaces

#### Management Interfaces Summary

##### IPv4

| Management Interface | Description | Type | VRF | IP Address | Gateway |
| -------------------- | ----------- | ---- | --- | ---------- | ------- |
| Management1 | OOB_MANAGEMENT | oob | MGMT | 192.168.200.106/24 | 192.168.200.5 |

##### IPv6

| Management Interface | Description | Type | VRF | IPv6 Address | IPv6 Gateway |
| -------------------- | ----------- | ---- | --- | ------------ | ------------ |
| Management1 | OOB_MANAGEMENT | oob | MGMT | - | - |

#### Management Interfaces Device Configuration

```eos
!
interface Management1
   description OOB_MANAGEMENT
   no shutdown
   vrf MGMT
   ip address 192.168.200.106/24
```

### IP Name Servers

#### IP Name Servers Summary

| Name Server | VRF | Priority |
| ----------- | --- | -------- |
| 192.168.200.5 | MGMT | - |
| 8.8.8.8 | MGMT | - |

#### IP Name Servers Device Configuration

```eos
ip name-server vrf MGMT 8.8.8.8
ip name-server vrf MGMT 192.168.200.5
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
| 192.168.200.5 | MGMT | True | - | - | - | - | - | - | - |

#### NTP Device Configuration

```eos
!
ntp local-interface vrf MGMT Management1
ntp server vrf MGMT 192.168.200.5 prefer
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
| cvpadmin | 15 | network-admin | False | - |

#### Local Users Device Configuration

```eos
!
username admin privilege 15 role network-admin nopassword
username cvpadmin privilege 15 role network-admin secret sha512 <removed>
```

### Enable Password

Enable password has been disabled

## Monitoring

### TerminAttr Daemon

#### TerminAttr Daemon Summary

| CV Compression | CloudVision Servers | VRF | Authentication | Smash Excludes | Ingest Exclude | Bypass AAA |
| -------------- | ------------------- | --- | -------------- | -------------- | -------------- | ---------- |
| gzip | 192.168.200.11:9910 | MGMT | key,telarista | ale,flexCounter,hardware,kni,pulse,strata | /Sysdb/cell/1/agent,/Sysdb/cell/2/agent | False |

#### TerminAttr Daemon Device Configuration

```eos
!
daemon TerminAttr
   exec /usr/bin/TerminAttr -cvaddr=192.168.200.11:9910 -cvauth=key,<removed> -cvvrf=MGMT -smashexcludes=ale,flexCounter,hardware,kni,pulse,strata -ingestexclude=/Sysdb/cell/1/agent,/Sysdb/cell/2/agent -taillogs
   no shutdown
```

## MLAG

### MLAG Summary

| Domain-id | Local-interface | Peer-address | Peer-link |
| --------- | --------------- | ------------ | --------- |
| DC1_LEAF2 | Vlan4094 | 10.255.252.3 | Port-Channel5 |

Dual primary detection is disabled.

### MLAG Device Configuration

```eos
!
mlag configuration
   domain-id DC1_LEAF2
   local-interface Vlan4094
   peer-address 10.255.252.3
   peer-link Port-Channel5
   reload-delay mlag 300
   reload-delay non-mlag 330
```

## Spanning Tree

### Spanning Tree Summary

STP mode: **mstp**

#### MSTP Instance and Priority

| Instance(s) | Priority |
| -------- | -------- |
| 0 | 4096 |

#### Global Spanning-Tree Settings

- Spanning Tree disabled for VLANs: **4093-4094**

### Spanning Tree Device Configuration

```eos
!
spanning-tree mode mstp
no spanning-tree vlan-id 4093-4094
spanning-tree mst 0 priority 4096
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

## VLANs

### VLANs Summary

| VLAN ID | Name | Trunk Groups |
| ------- | ---- | ------------ |
| 110 | Tenant_A_OP_Zone_1 | - |
| 111 | Tenant_A_OP_Zone_2 | - |
| 120 | Tenant_A_WEB_Zone_1 | - |
| 121 | Tenant_A_WEBZone_2 | - |
| 130 | Tenant_A_APP_Zone_1 | - |
| 131 | Tenant_A_APP_Zone_2 | - |
| 140 | Tenant_A_DB_BZone_1 | - |
| 141 | Tenant_A_DB_Zone_2 | - |
| 210 | Tenant_B_OP_Zone_1 | - |
| 211 | Tenant_B_OP_Zone_2 | - |
| 310 | Tenant_C_OP_Zone_1 | - |
| 311 | Tenant_C_OP_Zone_2 | - |
| 3009 | MLAG_L3_VRF_Tenant_A_OP_Zone | MLAG |
| 3010 | MLAG_L3_VRF_Tenant_A_WEB_Zone | MLAG |
| 3011 | MLAG_L3_VRF_Tenant_A_APP_Zone | MLAG |
| 3012 | MLAG_L3_VRF_Tenant_A_DB_Zone | MLAG |
| 3019 | MLAG_L3_VRF_Tenant_B_OP_Zone | MLAG |
| 3029 | MLAG_L3_VRF_Tenant_C_OP_Zone | MLAG |
| 4093 | MLAG_L3 | MLAG |
| 4094 | MLAG | MLAG |

### VLANs Device Configuration

```eos
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
   name MLAG_L3_VRF_Tenant_A_OP_Zone
   trunk group MLAG
!
vlan 3010
   name MLAG_L3_VRF_Tenant_A_WEB_Zone
   trunk group MLAG
!
vlan 3011
   name MLAG_L3_VRF_Tenant_A_APP_Zone
   trunk group MLAG
!
vlan 3012
   name MLAG_L3_VRF_Tenant_A_DB_Zone
   trunk group MLAG
!
vlan 3019
   name MLAG_L3_VRF_Tenant_B_OP_Zone
   trunk group MLAG
!
vlan 3029
   name MLAG_L3_VRF_Tenant_C_OP_Zone
   trunk group MLAG
!
vlan 4093
   name MLAG_L3
   trunk group MLAG
!
vlan 4094
   name MLAG
   trunk group MLAG
```

## Interfaces

### Ethernet Interfaces

#### Ethernet Interfaces Summary

##### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | Channel-Group |
| --------- | ----------- | ---- | ----- | ----------- | ----------- | ------------- |
| Ethernet5 | MLAG_DC1-LEAF2B_Ethernet5 | *trunk | *- | *- | *MLAG | 5 |
| Ethernet6 | MLAG_DC1-LEAF2B_Ethernet6 | *trunk | *- | *- | *MLAG | 5 |
| Ethernet7 | DC1-L2LEAF1A_Ethernet1 | *trunk | *110-111,120-121,130-131 | *- | *- | 7 |
| Ethernet10 | SERVER_server01_MLAG_Eth2 | *trunk | *210-211 | *- | *- | 10 |

*Inherited from Port-Channel Interface

##### IPv4

| Interface | Description | Channel Group | IP Address | VRF |  MTU | Shutdown | ACL In | ACL Out |
| --------- | ----------- | ------------- | ---------- | ----| ---- | -------- | ------ | ------- |
| Ethernet1 | P2P_LINK_TO_DC1-SPINE1_Ethernet2 | - | 172.31.255.9/31 | default | 1500 | False | - | - |
| Ethernet2 | P2P_LINK_TO_DC1-SPINE2_Ethernet2 | - | 172.31.255.11/31 | default | 1500 | False | - | - |
| Ethernet3 | P2P_LINK_TO_DC1-SPINE3_Ethernet2 | - | 172.31.255.13/31 | default | 1500 | False | - | - |
| Ethernet4 | P2P_LINK_TO_DC1-SPINE4_Ethernet2 | - | 172.31.255.15/31 | default | 1500 | False | - | - |

#### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet1
   description P2P_LINK_TO_DC1-SPINE1_Ethernet2
   no shutdown
   mtu 1500
   no switchport
   ip address 172.31.255.9/31
!
interface Ethernet2
   description P2P_LINK_TO_DC1-SPINE2_Ethernet2
   no shutdown
   mtu 1500
   no switchport
   ip address 172.31.255.11/31
!
interface Ethernet3
   description P2P_LINK_TO_DC1-SPINE3_Ethernet2
   no shutdown
   mtu 1500
   no switchport
   ip address 172.31.255.13/31
!
interface Ethernet4
   description P2P_LINK_TO_DC1-SPINE4_Ethernet2
   no shutdown
   mtu 1500
   no switchport
   ip address 172.31.255.15/31
!
interface Ethernet5
   description MLAG_DC1-LEAF2B_Ethernet5
   no shutdown
   channel-group 5 mode active
!
interface Ethernet6
   description MLAG_DC1-LEAF2B_Ethernet6
   no shutdown
   channel-group 5 mode active
!
interface Ethernet7
   description DC1-L2LEAF1A_Ethernet1
   no shutdown
   channel-group 7 mode active
!
interface Ethernet10
   description SERVER_server01_MLAG_Eth2
   no shutdown
   channel-group 10 mode active
```

### Port-Channel Interfaces

#### Port-Channel Interfaces Summary

##### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | LACP Fallback Timeout | LACP Fallback Mode | MLAG ID | EVPN ESI |
| --------- | ----------- | ---- | ----- | ----------- | ------------| --------------------- | ------------------ | ------- | -------- |
| Port-Channel5 | MLAG_DC1-LEAF2B_Port-Channel5 | trunk | - | - | MLAG | - | - | - | - |
| Port-Channel7 | DC1-L2LEAF1A_Po1 | trunk | 110-111,120-121,130-131 | - | - | - | - | 7 | - |
| Port-Channel10 | SERVER_server01_MLAG | trunk | 210-211 | - | - | - | - | 10 | - |

#### Port-Channel Interfaces Device Configuration

```eos
!
interface Port-Channel5
   description MLAG_DC1-LEAF2B_Port-Channel5
   no shutdown
   switchport mode trunk
   switchport trunk group MLAG
   switchport
!
interface Port-Channel7
   description DC1-L2LEAF1A_Po1
   no shutdown
   switchport trunk allowed vlan 110-111,120-121,130-131
   switchport mode trunk
   switchport
   mlag 7
!
interface Port-Channel10
   description SERVER_server01_MLAG
   no shutdown
   switchport trunk allowed vlan 210-211
   switchport mode trunk
   switchport
   mlag 10
```

### Loopback Interfaces

#### Loopback Interfaces Summary

##### IPv4

| Interface | Description | VRF | IP Address |
| --------- | ----------- | --- | ---------- |
| Loopback0 | ROUTER_ID | default | 192.168.255.6/32 |
| Loopback1 | VXLAN_TUNNEL_SOURCE | default | 192.168.254.6/32 |
| Loopback100 | Tenant_A_OP_Zone_VTEP_DIAGNOSTICS | Tenant_A_OP_Zone | 10.255.1.6/32 |

##### IPv6

| Interface | Description | VRF | IPv6 Address |
| --------- | ----------- | --- | ------------ |
| Loopback0 | ROUTER_ID | default | - |
| Loopback1 | VXLAN_TUNNEL_SOURCE | default | - |
| Loopback100 | Tenant_A_OP_Zone_VTEP_DIAGNOSTICS | Tenant_A_OP_Zone | - |

#### Loopback Interfaces Device Configuration

```eos
!
interface Loopback0
   description ROUTER_ID
   no shutdown
   ip address 192.168.255.6/32
!
interface Loopback1
   description VXLAN_TUNNEL_SOURCE
   no shutdown
   ip address 192.168.254.6/32
!
interface Loopback100
   description Tenant_A_OP_Zone_VTEP_DIAGNOSTICS
   no shutdown
   vrf Tenant_A_OP_Zone
   ip address 10.255.1.6/32
```

### VLAN Interfaces

#### VLAN Interfaces Summary

| Interface | Description | VRF |  MTU | Shutdown |
| --------- | ----------- | --- | ---- | -------- |
| Vlan110 | Tenant_A_OP_Zone_1 | Tenant_A_OP_Zone | - | False |
| Vlan111 | Tenant_A_OP_Zone_2 | Tenant_A_OP_Zone | - | False |
| Vlan120 | Tenant_A_WEB_Zone_1 | Tenant_A_WEB_Zone | - | False |
| Vlan121 | Tenant_A_WEBZone_2 | Tenant_A_WEB_Zone | 1560 | True |
| Vlan130 | Tenant_A_APP_Zone_1 | Tenant_A_APP_Zone | - | False |
| Vlan131 | Tenant_A_APP_Zone_2 | Tenant_A_APP_Zone | - | False |
| Vlan140 | Tenant_A_DB_BZone_1 | Tenant_A_DB_Zone | - | False |
| Vlan141 | Tenant_A_DB_Zone_2 | Tenant_A_DB_Zone | - | False |
| Vlan210 | Tenant_B_OP_Zone_1 | Tenant_B_OP_Zone | - | False |
| Vlan211 | Tenant_B_OP_Zone_2 | Tenant_B_OP_Zone | - | False |
| Vlan310 | Tenant_C_OP_Zone_1 | Tenant_C_OP_Zone | - | False |
| Vlan311 | Tenant_C_OP_Zone_2 | Tenant_C_OP_Zone | - | False |
| Vlan3009 | MLAG_L3_VRF_Tenant_A_OP_Zone | Tenant_A_OP_Zone | 1500 | False |
| Vlan3010 | MLAG_L3_VRF_Tenant_A_WEB_Zone | Tenant_A_WEB_Zone | 1500 | False |
| Vlan3011 | MLAG_L3_VRF_Tenant_A_APP_Zone | Tenant_A_APP_Zone | 1500 | False |
| Vlan3012 | MLAG_L3_VRF_Tenant_A_DB_Zone | Tenant_A_DB_Zone | 1500 | False |
| Vlan3019 | MLAG_L3_VRF_Tenant_B_OP_Zone | Tenant_B_OP_Zone | 1500 | False |
| Vlan3029 | MLAG_L3_VRF_Tenant_C_OP_Zone | Tenant_C_OP_Zone | 1500 | False |
| Vlan4093 | MLAG_L3 | default | 1500 | False |
| Vlan4094 | MLAG | default | 1500 | False |

##### IPv4

| Interface | VRF | IP Address | IP Address Virtual | IP Router Virtual Address | ACL In | ACL Out |
| --------- | --- | ---------- | ------------------ | ------------------------- | ------ | ------- |
| Vlan110 |  Tenant_A_OP_Zone  |  -  |  10.1.10.1/24  |  -  |  -  |  -  |
| Vlan111 |  Tenant_A_OP_Zone  |  -  |  10.1.11.1/24  |  -  |  -  |  -  |
| Vlan120 |  Tenant_A_WEB_Zone  |  -  |  10.1.20.1/24  |  -  |  -  |  -  |
| Vlan121 |  Tenant_A_WEB_Zone  |  -  |  10.1.10.254/24  |  -  |  -  |  -  |
| Vlan130 |  Tenant_A_APP_Zone  |  -  |  10.1.30.1/24  |  -  |  -  |  -  |
| Vlan131 |  Tenant_A_APP_Zone  |  -  |  10.1.31.1/24  |  -  |  -  |  -  |
| Vlan140 |  Tenant_A_DB_Zone  |  -  |  10.1.40.1/24  |  -  |  -  |  -  |
| Vlan141 |  Tenant_A_DB_Zone  |  -  |  10.1.41.1/24  |  -  |  -  |  -  |
| Vlan210 |  Tenant_B_OP_Zone  |  -  |  10.2.10.1/24  |  -  |  -  |  -  |
| Vlan211 |  Tenant_B_OP_Zone  |  -  |  10.2.11.1/24  |  -  |  -  |  -  |
| Vlan310 |  Tenant_C_OP_Zone  |  -  |  10.3.10.1/24  |  -  |  -  |  -  |
| Vlan311 |  Tenant_C_OP_Zone  |  -  |  10.3.11.1/24  |  -  |  -  |  -  |
| Vlan3009 |  Tenant_A_OP_Zone  |  10.255.251.2/31  |  -  |  -  |  -  |  -  |
| Vlan3010 |  Tenant_A_WEB_Zone  |  10.255.251.2/31  |  -  |  -  |  -  |  -  |
| Vlan3011 |  Tenant_A_APP_Zone  |  10.255.251.2/31  |  -  |  -  |  -  |  -  |
| Vlan3012 |  Tenant_A_DB_Zone  |  10.255.251.2/31  |  -  |  -  |  -  |  -  |
| Vlan3019 |  Tenant_B_OP_Zone  |  10.255.251.2/31  |  -  |  -  |  -  |  -  |
| Vlan3029 |  Tenant_C_OP_Zone  |  10.255.251.2/31  |  -  |  -  |  -  |  -  |
| Vlan4093 |  default  |  10.255.251.2/31  |  -  |  -  |  -  |  -  |
| Vlan4094 |  default  |  10.255.252.2/31  |  -  |  -  |  -  |  -  |

#### VLAN Interfaces Device Configuration

```eos
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
   description MLAG_L3_VRF_Tenant_A_OP_Zone
   no shutdown
   mtu 1500
   vrf Tenant_A_OP_Zone
   ip address 10.255.251.2/31
!
interface Vlan3010
   description MLAG_L3_VRF_Tenant_A_WEB_Zone
   no shutdown
   mtu 1500
   vrf Tenant_A_WEB_Zone
   ip address 10.255.251.2/31
!
interface Vlan3011
   description MLAG_L3_VRF_Tenant_A_APP_Zone
   no shutdown
   mtu 1500
   vrf Tenant_A_APP_Zone
   ip address 10.255.251.2/31
!
interface Vlan3012
   description MLAG_L3_VRF_Tenant_A_DB_Zone
   no shutdown
   mtu 1500
   vrf Tenant_A_DB_Zone
   ip address 10.255.251.2/31
!
interface Vlan3019
   description MLAG_L3_VRF_Tenant_B_OP_Zone
   no shutdown
   mtu 1500
   vrf Tenant_B_OP_Zone
   ip address 10.255.251.2/31
!
interface Vlan3029
   description MLAG_L3_VRF_Tenant_C_OP_Zone
   no shutdown
   mtu 1500
   vrf Tenant_C_OP_Zone
   ip address 10.255.251.2/31
!
interface Vlan4093
   description MLAG_L3
   no shutdown
   mtu 1500
   ip address 10.255.251.2/31
!
interface Vlan4094
   description MLAG
   no shutdown
   mtu 1500
   no autostate
   ip address 10.255.252.2/31
```

### VXLAN Interface

#### VXLAN Interface Summary

| Setting | Value |
| ------- | ----- |
| Source Interface | Loopback1 |
| UDP port | 4789 |
| EVPN MLAG Shared Router MAC | mlag-system-id |

##### VLAN to VNI, Flood List and Multicast Group Mappings

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
| 210 | 20210 | - | - |
| 211 | 20211 | - | - |
| 310 | 30310 | - | - |
| 311 | 30311 | - | - |

##### VRF to VNI and Multicast Group Mappings

| VRF | VNI | Multicast Group |
| ---- | --- | --------------- |
| Tenant_A_APP_Zone | 12 | - |
| Tenant_A_DB_Zone | 13 | - |
| Tenant_A_OP_Zone | 10 | - |
| Tenant_A_WEB_Zone | 11 | - |
| Tenant_B_OP_Zone | 20 | - |
| Tenant_C_OP_Zone | 30 | - |

#### VXLAN Interface Device Configuration

```eos
!
interface Vxlan1
   description DC1-LEAF2A_VTEP
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

## Routing

### Service Routing Protocols Model

Multi agent routing protocol model enabled

```eos
!
service routing protocols model multi-agent
```

### Virtual Router MAC Address

#### Virtual Router MAC Address Summary

Virtual Router MAC Address: 00:dc:00:00:00:0a

#### Virtual Router MAC Address Device Configuration

```eos
!
ip virtual-router mac-address 00:dc:00:00:00:0a
```

### IP Routing

#### IP Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | True |
| MGMT | False |
| Tenant_A_APP_Zone | True |
| Tenant_A_DB_Zone | True |
| Tenant_A_OP_Zone | True |
| Tenant_A_WEB_Zone | True |
| Tenant_B_OP_Zone | True |
| Tenant_C_OP_Zone | True |

#### IP Routing Device Configuration

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

### IPv6 Routing

#### IPv6 Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | False |
| MGMT | false |
| Tenant_A_APP_Zone | false |
| Tenant_A_DB_Zone | false |
| Tenant_A_OP_Zone | false |
| Tenant_A_WEB_Zone | false |
| Tenant_B_OP_Zone | false |
| Tenant_C_OP_Zone | false |

### Static Routes

#### Static Routes Summary

| VRF | Destination Prefix | Next Hop IP | Exit interface | Administrative Distance | Tag | Route Name | Metric |
| --- | ------------------ | ----------- | -------------- | ----------------------- | --- | ---------- | ------ |
| MGMT | 0.0.0.0/0 | 192.168.200.5 | - | 1 | - | - | - |

#### Static Routes Device Configuration

```eos
!
ip route vrf MGMT 0.0.0.0/0 192.168.200.5
```

### Router BGP

ASN Notation: asplain

#### Router BGP Summary

| BGP AS | Router ID |
| ------ | --------- |
| 65102 | 192.168.255.6 |

| BGP Tuning |
| ---------- |
| distance bgp 20 200 200 |
| update wait-install |
| no bgp default ipv4-unicast |
| maximum-paths 4 ecmp 4 |

#### Router BGP Peer Groups

##### EVPN-OVERLAY-PEERS

| Settings | Value |
| -------- | ----- |
| Address Family | evpn |
| Source | Loopback0 |
| BFD | True |
| Ebgp multihop | 3 |
| Send community | all |
| Maximum routes | 0 (no limit) |

##### IPv4-UNDERLAY-PEERS

| Settings | Value |
| -------- | ----- |
| Address Family | ipv4 |
| Send community | all |
| Maximum routes | 12000 |

##### MLAG-IPv4-UNDERLAY-PEER

| Settings | Value |
| -------- | ----- |
| Address Family | ipv4 |
| Remote AS | 65102 |
| Next-hop self | True |
| Send community | all |
| Maximum routes | 12000 |

#### BGP Neighbors

| Neighbor | Remote AS | VRF | Shutdown | Send-community | Maximum-routes | Allowas-in | BFD | RIB Pre-Policy Retain | Route-Reflector Client | Passive | TTL Max Hops |
| -------- | --------- | --- | -------- | -------------- | -------------- | ---------- | --- | --------------------- | ---------------------- | ------- | ------------ |
| 10.255.251.3 | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | default | - | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | - | - | - | - | - | - |
| 172.31.255.8 | 65001 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - | - |
| 172.31.255.10 | 65001 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - | - |
| 172.31.255.12 | 65001 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - | - |
| 172.31.255.14 | 65001 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - | - |
| 192.168.255.1 | 65001 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 192.168.255.2 | 65001 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 192.168.255.3 | 65001 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 192.168.255.4 | 65001 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 10.255.251.3 | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | Tenant_A_APP_Zone | - | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | - | - | - | - | - | - |
| 10.255.251.3 | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | Tenant_A_DB_Zone | - | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | - | - | - | - | - | - |
| 10.255.251.3 | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | Tenant_A_OP_Zone | - | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | - | - | - | - | - | - |
| 10.255.251.3 | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | Tenant_A_WEB_Zone | - | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | - | - | - | - | - | - |
| 10.255.251.3 | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | Tenant_B_OP_Zone | - | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | - | - | - | - | - | - |
| 10.255.251.3 | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | Tenant_C_OP_Zone | - | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | - | - | - | - | - | - |

#### Router BGP EVPN Address Family

##### EVPN Peer Groups

| Peer Group | Activate | Encapsulation |
| ---------- | -------- | ------------- |
| EVPN-OVERLAY-PEERS | True | default |

#### Router BGP VLAN Aware Bundles

| VLAN Aware Bundle | Route-Distinguisher | Both Route-Target | Import Route Target | Export Route-Target | Redistribute | VLANs |
| ----------------- | ------------------- | ----------------- | ------------------- | ------------------- | ------------ | ----- |
| Tenant_A_APP_Zone | 192.168.255.6:12 | 12:12 | - | - | learned | 130-131 |
| Tenant_A_DB_Zone | 192.168.255.6:13 | 13:13 | - | - | learned | 140-141 |
| Tenant_A_OP_Zone | 192.168.255.6:10 | 10:10 | - | - | learned | 110-111 |
| Tenant_A_WEB_Zone | 192.168.255.6:11 | 11:11 | - | - | learned | 120-121 |
| Tenant_B_OP_Zone | 192.168.255.6:20 | 20:20 | - | - | learned | 210-211 |
| Tenant_C_OP_Zone | 192.168.255.6:30 | 30:30 | - | - | learned | 310-311 |

#### Router BGP VRFs

| VRF | Route-Distinguisher | Redistribute |
| --- | ------------------- | ------------ |
| Tenant_A_APP_Zone | 192.168.255.6:12 | connected |
| Tenant_A_DB_Zone | 192.168.255.6:13 | connected |
| Tenant_A_OP_Zone | 192.168.255.6:10 | connected |
| Tenant_A_WEB_Zone | 192.168.255.6:11 | connected |
| Tenant_B_OP_Zone | 192.168.255.6:20 | connected |
| Tenant_C_OP_Zone | 192.168.255.6:30 | connected |

#### Router BGP Device Configuration

```eos
!
router bgp 65102
   router-id 192.168.255.6
   maximum-paths 4 ecmp 4
   update wait-install
   no bgp default ipv4-unicast
   distance bgp 20 200 200
   neighbor EVPN-OVERLAY-PEERS peer group
   neighbor EVPN-OVERLAY-PEERS update-source Loopback0
   neighbor EVPN-OVERLAY-PEERS bfd
   neighbor EVPN-OVERLAY-PEERS ebgp-multihop 3
   neighbor EVPN-OVERLAY-PEERS password 7 <removed>
   neighbor EVPN-OVERLAY-PEERS send-community
   neighbor EVPN-OVERLAY-PEERS maximum-routes 0
   neighbor IPv4-UNDERLAY-PEERS peer group
   neighbor IPv4-UNDERLAY-PEERS password 7 <removed>
   neighbor IPv4-UNDERLAY-PEERS send-community
   neighbor IPv4-UNDERLAY-PEERS maximum-routes 12000
   neighbor MLAG-IPv4-UNDERLAY-PEER peer group
   neighbor MLAG-IPv4-UNDERLAY-PEER remote-as 65102
   neighbor MLAG-IPv4-UNDERLAY-PEER next-hop-self
   neighbor MLAG-IPv4-UNDERLAY-PEER description DC1-LEAF2B
   neighbor MLAG-IPv4-UNDERLAY-PEER password 7 <removed>
   neighbor MLAG-IPv4-UNDERLAY-PEER send-community
   neighbor MLAG-IPv4-UNDERLAY-PEER maximum-routes 12000
   neighbor MLAG-IPv4-UNDERLAY-PEER route-map RM-MLAG-PEER-IN in
   neighbor 10.255.251.3 peer group MLAG-IPv4-UNDERLAY-PEER
   neighbor 10.255.251.3 description DC1-LEAF2B
   neighbor 172.31.255.8 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.31.255.8 remote-as 65001
   neighbor 172.31.255.8 description DC1-SPINE1_Ethernet2
   neighbor 172.31.255.10 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.31.255.10 remote-as 65001
   neighbor 172.31.255.10 description DC1-SPINE2_Ethernet2
   neighbor 172.31.255.12 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.31.255.12 remote-as 65001
   neighbor 172.31.255.12 description DC1-SPINE3_Ethernet2
   neighbor 172.31.255.14 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.31.255.14 remote-as 65001
   neighbor 172.31.255.14 description DC1-SPINE4_Ethernet2
   neighbor 192.168.255.1 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.255.1 remote-as 65001
   neighbor 192.168.255.1 description DC1-SPINE1
   neighbor 192.168.255.2 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.255.2 remote-as 65001
   neighbor 192.168.255.2 description DC1-SPINE2
   neighbor 192.168.255.3 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.255.3 remote-as 65001
   neighbor 192.168.255.3 description DC1-SPINE3
   neighbor 192.168.255.4 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.255.4 remote-as 65001
   neighbor 192.168.255.4 description DC1-SPINE4
   redistribute connected route-map RM-CONN-2-BGP
   !
   vlan-aware-bundle Tenant_A_APP_Zone
      rd 192.168.255.6:12
      route-target both 12:12
      redistribute learned
      vlan 130-131
   !
   vlan-aware-bundle Tenant_A_DB_Zone
      rd 192.168.255.6:13
      route-target both 13:13
      redistribute learned
      vlan 140-141
   !
   vlan-aware-bundle Tenant_A_OP_Zone
      rd 192.168.255.6:10
      route-target both 10:10
      redistribute learned
      vlan 110-111
   !
   vlan-aware-bundle Tenant_A_WEB_Zone
      rd 192.168.255.6:11
      route-target both 11:11
      redistribute learned
      vlan 120-121
   !
   vlan-aware-bundle Tenant_B_OP_Zone
      rd 192.168.255.6:20
      route-target both 20:20
      redistribute learned
      vlan 210-211
   !
   vlan-aware-bundle Tenant_C_OP_Zone
      rd 192.168.255.6:30
      route-target both 30:30
      redistribute learned
      vlan 310-311
   !
   address-family evpn
      neighbor EVPN-OVERLAY-PEERS activate
   !
   address-family ipv4
      no neighbor EVPN-OVERLAY-PEERS activate
      neighbor IPv4-UNDERLAY-PEERS activate
      neighbor MLAG-IPv4-UNDERLAY-PEER activate
   !
   vrf Tenant_A_APP_Zone
      rd 192.168.255.6:12
      route-target import evpn 12:12
      route-target export evpn 12:12
      router-id 192.168.255.6
      update wait-install
      neighbor 10.255.251.3 peer group MLAG-IPv4-UNDERLAY-PEER
      neighbor 10.255.251.3 description DC1-LEAF2B
      redistribute connected
   !
   vrf Tenant_A_DB_Zone
      rd 192.168.255.6:13
      route-target import evpn 13:13
      route-target export evpn 13:13
      router-id 192.168.255.6
      update wait-install
      neighbor 10.255.251.3 peer group MLAG-IPv4-UNDERLAY-PEER
      neighbor 10.255.251.3 description DC1-LEAF2B
      redistribute connected
   !
   vrf Tenant_A_OP_Zone
      rd 192.168.255.6:10
      route-target import evpn 10:10
      route-target export evpn 10:10
      router-id 192.168.255.6
      update wait-install
      neighbor 10.255.251.3 peer group MLAG-IPv4-UNDERLAY-PEER
      neighbor 10.255.251.3 description DC1-LEAF2B
      redistribute connected
   !
   vrf Tenant_A_WEB_Zone
      rd 192.168.255.6:11
      route-target import evpn 11:11
      route-target export evpn 11:11
      router-id 192.168.255.6
      update wait-install
      neighbor 10.255.251.3 peer group MLAG-IPv4-UNDERLAY-PEER
      neighbor 10.255.251.3 description DC1-LEAF2B
      redistribute connected
   !
   vrf Tenant_B_OP_Zone
      rd 192.168.255.6:20
      route-target import evpn 20:20
      route-target export evpn 20:20
      router-id 192.168.255.6
      update wait-install
      neighbor 10.255.251.3 peer group MLAG-IPv4-UNDERLAY-PEER
      neighbor 10.255.251.3 description DC1-LEAF2B
      redistribute connected
   !
   vrf Tenant_C_OP_Zone
      rd 192.168.255.6:30
      route-target import evpn 30:30
      route-target export evpn 30:30
      router-id 192.168.255.6
      update wait-install
      neighbor 10.255.251.3 peer group MLAG-IPv4-UNDERLAY-PEER
      neighbor 10.255.251.3 description DC1-LEAF2B
      redistribute connected
```

## BFD

### Router BFD

#### Router BFD Multihop Summary

| Interval | Minimum RX | Multiplier |
| -------- | ---------- | ---------- |
| 1200 | 1200 | 3 |

#### Router BFD Device Configuration

```eos
!
router bfd
   multihop interval 1200 min-rx 1200 multiplier 3
```

## Multicast

### IP IGMP Snooping

#### IP IGMP Snooping Summary

| IGMP Snooping | Fast Leave | Interface Restart Query | Proxy | Restart Query Interval | Robustness Variable |
| ------------- | ---------- | ----------------------- | ----- | ---------------------- | ------------------- |
| Enabled | - | - | - | - | - |

##### IP IGMP Snooping Vlan Summary

| Vlan | IGMP Snooping | Fast Leave | Max Groups | Proxy |
| ---- | ------------- | ---------- | ---------- | ----- |
| 120 | False | - | - | - |

#### IP IGMP Snooping Device Configuration

```eos
!
no ip igmp snooping vlan 120
```

## Filters

### Prefix-lists

#### Prefix-lists Summary

##### PL-LOOPBACKS-EVPN-OVERLAY

| Sequence | Action |
| -------- | ------ |
| 10 | permit 192.168.255.0/24 eq 32 |
| 20 | permit 192.168.254.0/24 eq 32 |

#### Prefix-lists Device Configuration

```eos
!
ip prefix-list PL-LOOPBACKS-EVPN-OVERLAY
   seq 10 permit 192.168.255.0/24 eq 32
   seq 20 permit 192.168.254.0/24 eq 32
```

### Route-maps

#### Route-maps Summary

##### RM-CONN-2-BGP

| Sequence | Type | Match | Set | Sub-Route-Map | Continue |
| -------- | ---- | ----- | --- | ------------- | -------- |
| 10 | permit | ip address prefix-list PL-LOOPBACKS-EVPN-OVERLAY | - | - | - |

##### RM-MLAG-PEER-IN

| Sequence | Type | Match | Set | Sub-Route-Map | Continue |
| -------- | ---- | ----- | --- | ------------- | -------- |
| 10 | permit | - | origin incomplete | - | - |

#### Route-maps Device Configuration

```eos
!
route-map RM-CONN-2-BGP permit 10
   match ip address prefix-list PL-LOOPBACKS-EVPN-OVERLAY
!
route-map RM-MLAG-PEER-IN permit 10
   description Make routes learned over MLAG Peer-link less preferred on spines to ensure optimal routing
   set origin incomplete
```

## VRF Instances

### VRF Instances Summary

| VRF Name | IP Routing |
| -------- | ---------- |
| MGMT | disabled |
| Tenant_A_APP_Zone | enabled |
| Tenant_A_DB_Zone | enabled |
| Tenant_A_OP_Zone | enabled |
| Tenant_A_WEB_Zone | enabled |
| Tenant_B_OP_Zone | enabled |
| Tenant_C_OP_Zone | enabled |

### VRF Instances Device Configuration

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

## Virtual Source NAT

### Virtual Source NAT Summary

| Source NAT VRF | Source NAT IP Address |
| -------------- | --------------------- |
| Tenant_A_OP_Zone | 10.255.1.6 |

### Virtual Source NAT Configuration

```eos
!
ip address virtual source-nat vrf Tenant_A_OP_Zone address 10.255.1.6
```
