# DC1-BL1B

# Table of Contents

- [DC1-BL1B](#dc1-bl1b)
- [Table of Contents](#table-of-contents)
- [Management](#management)
  - [Management Interfaces](#management-interfaces)
    - [Management Interfaces Summary](#management-interfaces-summary)
      - [IPv4](#ipv4)
      - [IPv6](#ipv6)
    - [Management Interfaces Device Configuration](#management-interfaces-device-configuration)
  - [DNS Domain](#dns-domain)
  - [Domain-list](#domain-list)
  - [Name Servers](#name-servers)
    - [Name Servers Summary](#name-servers-summary)
    - [Name Servers Device Configuration](#name-servers-device-configuration)
  - [Domain Lookup](#domain-lookup)
  - [NTP](#ntp)
    - [NTP Summary](#ntp-summary)
    - [NTP Device Configuration](#ntp-device-configuration)
  - [Management SSH](#management-ssh)
  - [Management API GNMI](#management-api-gnmi)
  - [Management API HTTP](#management-api-http)
    - [Management API HTTP Summary](#management-api-http-summary)
    - [Management API VRF Access](#management-api-vrf-access)
    - [Management API HTTP Configuration](#management-api-http-configuration)
- [Authentication](#authentication)
  - [Local Users](#local-users)
    - [Local Users Summary](#local-users-summary)
    - [Local Users Device Configuration](#local-users-device-configuration)
  - [TACACS Servers](#tacacs-servers)
  - [IP TACACS Source Interfaces](#ip-tacacs-source-interfaces)
  - [RADIUS Servers](#radius-servers)
  - [AAA Server Groups](#aaa-server-groups)
  - [AAA Authentication](#aaa-authentication)
  - [AAA Authorization](#aaa-authorization)
  - [AAA Accounting](#aaa-accounting)
- [Management Security](#management-security)
- [Aliases](#aliases)
- [Monitoring](#monitoring)
  - [TerminAttr Daemon](#terminattr-daemon)
    - [TerminAttr Daemon Summary](#terminattr-daemon-summary)
    - [TerminAttr Daemon Device Configuration](#terminattr-daemon-device-configuration)
  - [Logging](#logging)
  - [SNMP](#snmp)
  - [SFlow](#sflow)
  - [Hardware Counters](#hardware-counters)
  - [VM Tracer Sessions](#vm-tracer-sessions)
  - [Event Handler](#event-handler)
- [MLAG](#mlag)
- [Spanning Tree](#spanning-tree)
  - [Spanning Tree Summary](#spanning-tree-summary)
    - [MSTP Instance and Priority](#mstp-instance-and-priority)
  - [Spanning Tree Device Configuration](#spanning-tree-device-configuration)
- [Internal VLAN Allocation Policy](#internal-vlan-allocation-policy)
  - [Internal VLAN Allocation Policy Summary](#internal-vlan-allocation-policy-summary)
  - [Internal VLAN Allocation Policy Configuration](#internal-vlan-allocation-policy-configuration)
- [VLANs](#vlans)
  - [VLANs Summary](#vlans-summary)
  - [VLANs Device Configuration](#vlans-device-configuration)
- [Interfaces](#interfaces)
  - [Ethernet Interfaces](#ethernet-interfaces)
    - [Ethernet Interfaces Summary](#ethernet-interfaces-summary)
      - [L2](#l2)
      - [IPv4](#ipv4-1)
    - [Ethernet Interfaces Device Configuration](#ethernet-interfaces-device-configuration)
  - [Port-Channel Interfaces](#port-channel-interfaces)
  - [Loopback Interfaces](#loopback-interfaces)
    - [Loopback Interfaces Summary](#loopback-interfaces-summary)
      - [IPv4](#ipv4-2)
      - [IPv6](#ipv6-1)
    - [Loopback Interfaces Device Configuration](#loopback-interfaces-device-configuration)
  - [VLAN Interfaces](#vlan-interfaces)
    - [VLAN Interfaces Summary](#vlan-interfaces-summary)
      - [IPv4](#ipv4-3)
    - [VLAN Interfaces Device Configuration](#vlan-interfaces-device-configuration)
  - [VXLAN Interface](#vxlan-interface)
    - [VXLAN Interface Summary](#vxlan-interface-summary)
      - [Source Interface: Loopback1](#source-interface-loopback1)
      - [UDP port: 4789](#udp-port-4789)
      - [VLAN to VNI Mappings](#vlan-to-vni-mappings)
      - [VRF to VNI Mappings](#vrf-to-vni-mappings)
    - [VXLAN Interface Device Configuration](#vxlan-interface-device-configuration)
- [Routing](#routing)
  - [Virtual Router MAC Address](#virtual-router-mac-address)
    - [Virtual Router MAC Address Summary](#virtual-router-mac-address-summary)
      - [Virtual Router MAC Address: 00:dc:00:00:00:0a](#virtual-router-mac-address-00dc0000000a)
    - [Virtual Router MAC Address Configuration](#virtual-router-mac-address-configuration)
  - [IP Routing](#ip-routing)
    - [IP Routing Summary](#ip-routing-summary)
    - [IP Routing Device Configuration](#ip-routing-device-configuration)
  - [IPv6 Routing](#ipv6-routing)
    - [IPv6 Routing Summary](#ipv6-routing-summary)
  - [Static Routes](#static-routes)
    - [Static Routes Summary](#static-routes-summary)
    - [Static Routes Device Configuration](#static-routes-device-configuration)
  - [IPv6 Static Routes](#ipv6-static-routes)
  - [Router ISIS](#router-isis)
  - [Router BGP](#router-bgp)
    - [Router BGP Summary](#router-bgp-summary)
    - [Router BGP Peer Groups](#router-bgp-peer-groups)
      - [EVPN-OVERLAY-PEERS](#evpn-overlay-peers)
      - [IPv4-UNDERLAY-PEERS](#ipv4-underlay-peers)
    - [BGP Neighbors](#bgp-neighbors)
    - [Router BGP EVPN Address Family](#router-bgp-evpn-address-family)
      - [Router BGP EVPN MAC-VRFs](#router-bgp-evpn-mac-vrfs)
        - [VLAN aware bundles](#vlan-aware-bundles)
      - [Router BGP EVPN VRFs](#router-bgp-evpn-vrfs)
    - [Router BGP Device Configuration](#router-bgp-device-configuration)
  - [Router BFD](#router-bfd)
    - [Router BFD Multihop Summary](#router-bfd-multihop-summary)
    - [Router BFD Multihop Device Configuration](#router-bfd-multihop-device-configuration)
- [Multicast](#multicast)
  - [IP IGMP Snooping](#ip-igmp-snooping)
    - [IP IGMP Snooping Summary](#ip-igmp-snooping-summary)
  - [Router Multicast](#router-multicast)
  - [Router PIM Sparse Mode](#router-pim-sparse-mode)
- [Filters](#filters)
  - [Community-lists](#community-lists)
  - [Peer Filters](#peer-filters)
  - [Prefix-lists](#prefix-lists)
    - [Prefix-lists Summary](#prefix-lists-summary)
      - [PL-LOOPBACKS-EVPN-OVERLAY](#pl-loopbacks-evpn-overlay)
    - [Prefix-lists Device Configuration](#prefix-lists-device-configuration)
  - [IPv6 Prefix-lists](#ipv6-prefix-lists)
  - [Route-maps](#route-maps)
    - [Route-maps Summary](#route-maps-summary)
      - [RM-CONN-2-BGP](#rm-conn-2-bgp)
    - [Route-maps Device Configuration](#route-maps-device-configuration)
  - [IP Extended Communities](#ip-extended-communities)
- [ACL](#acl)
  - [Standard Access-lists](#standard-access-lists)
  - [Extended Access-lists](#extended-access-lists)
  - [IPv6 Standard Access-lists](#ipv6-standard-access-lists)
  - [IPv6 Extended Access-lists](#ipv6-extended-access-lists)
- [VRF Instances](#vrf-instances)
  - [VRF Instances Summary](#vrf-instances-summary)
  - [VRF Instances Device Configuration](#vrf-instances-device-configuration)
- [Virtual Source NAT](#virtual-source-nat)
- [Platform](#platform)
- [Router L2 VPN](#router-l2-vpn)
- [IP DHCP Relay](#ip-dhcp-relay)
- [Custom Templates](#custom-templates)

# Management

## Management Interfaces

### Management Interfaces Summary

#### IPv4

| Management Interface | description | VRF | IP Address | Gateway |
| -------------------- | ----------- | --- | ---------- | ------- |
| Management1 | oob_management | MGMT | 192.168.200.111/24 | 192.168.200.5 |

#### IPv6

| Management Interface | description | VRF | IPv6 Address | IPv6 Gateway |
| -------------------- | ----------- | --- | ------------ | ------------ |
| Management1 | oob_management | MGMT | -  | - |

### Management Interfaces Device Configuration

```eos
!
interface Management1
   description oob_management
   vrf MGMT
   ip address 192.168.200.111/24
```

## DNS Domain

DNS domain not defined

## Domain-list

Domain-list not defined

## Name Servers

### Name Servers Summary

| Name Server | Source VRF |
| ----------- | ---------- |
| 192.168.200.5 | MGMT |
| 8.8.8.8 | MGMT |

### Name Servers Device Configuration

```eos
ip name-server vrf MGMT 192.168.200.5
ip name-server vrf MGMT 8.8.8.8
```

## Domain Lookup

DNS domain lookup not defined

## NTP

### NTP Summary

- Local Interface: Management1

- VRF: MGMT

| Node | Primary |
| ---- | ------- |
| 192.168.200.5 | true |

### NTP Device Configuration

```eos
!
ntp local-interface vrf MGMT Management1
ntp server vrf MGMT 192.168.200.5 prefer
```

## Management SSH

Management SSH not defined

## Management API GNMI

Management API gnmi is not defined

## Management API HTTP

### Management API HTTP Summary

| HTTP | HTTPS |
| ---------- | ---------- |
|  default  |  true  |

### Management API VRF Access

| VRF Name | IPv4 ACL | IPv6 ACL |
| -------- | -------- | -------- |
| MGMT |  -  |  -  |

### Management API HTTP Configuration

```eos
!
management api http-commands
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

## TACACS Servers

TACACS servers not defined

## IP TACACS Source Interfaces

IP TACACS source interfaces not defined

## RADIUS Servers

RADIUS servers not defined

## AAA Server Groups

AAA server groups not defined

## AAA Authentication

AAA authentication not defined

## AAA Authorization

AAA authorization not defined

## AAA Accounting

AAA accounting not defined

# Management Security

Management security not defined

# Aliases

Aliases not defined

# Monitoring

## TerminAttr Daemon

### TerminAttr Daemon Summary

| CV Compression | Ingest gRPC URL | Ingest Authentication Key | Smash Excludes | Ingest Exclude | Ingest VRF |  NTP VRF |
| -------------- | --------------- | ------------------------- | -------------- | -------------- | ---------- | -------- |
| gzip | 192.168.200.11:9910 | telarista | ale,flexCounter,hardware,kni,pulse,strata | /Sysdb/cell/1/agent,/Sysdb/cell/2/agent | MGMT | MGMT |

### TerminAttr Daemon Device Configuration

```eos
!
daemon TerminAttr
   exec /usr/bin/TerminAttr -ingestgrpcurl=192.168.200.11:9910 -cvcompression=gzip -ingestauth=key,telarista -smashexcludes=ale,flexCounter,hardware,kni,pulse,strata -ingestexclude=/Sysdb/cell/1/agent,/Sysdb/cell/2/agent -ingestvrf=MGMT -taillogs
   no shutdown
```

## Logging

No logging settings defined

## SNMP

No SNMP settings defined

## SFlow

No sFlow defined

## Hardware Counters

No hardware counters defined

## VM Tracer Sessions

No VM tracer sessions defined

## Event Handler

No event handler defined

# MLAG

MLAG not defined

# Spanning Tree

## Spanning Tree Summary

Mode: mstp

### MSTP Instance and Priority

| Instance | Priority |
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
| 150 | Tenant_A_WAN_Zone_1 | none  |
| 250 | Tenant_B_WAN_Zone_1 | none  |
| 350 | Tenant_C_WAN_Zone_1 | none  |

## VLANs Device Configuration

```eos
!
vlan 150
   name Tenant_A_WAN_Zone_1
!
vlan 250
   name Tenant_B_WAN_Zone_1
!
vlan 350
   name Tenant_C_WAN_Zone_1
```

# Interfaces

## Ethernet Interfaces

### Ethernet Interfaces Summary

#### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | Channel-Group |
| --------- | ----------- | ---- | ----- | ----------- | ----------- | ------------- |
| Ethernet5 | MLAG_PEER_DC1-BL1A_Ethernet5 | *trunk | *2-4094 | *- | *['LEAF_PEER_L3', 'MLAG'] | 5 |
| Ethernet6 | MLAG_PEER_DC1-BL1A_Ethernet6 | *trunk | *2-4094 | *- | *['LEAF_PEER_L3', 'MLAG'] | 5 |

*Inherited from Port-Channel Interface

#### IPv4

| Interface | Description | Type | Channel Group | IP Address | VRF |  MTU | Shutdown | ACL In | ACL Out |
| --------- | ----------- | -----| ------------- | ---------- | ----| ---- | -------- | ------ | ------- |
| Ethernet1 |  P2P_LINK_TO_DC1-SPINE1_Ethernet7  |  routed  | - |  172.31.255.49/31  |  default  |  1500  |  -  |  -  |  -  |
| Ethernet2 |  P2P_LINK_TO_DC1-SPINE2_Ethernet7  |  routed  | - |  172.31.255.51/31  |  default  |  1500  |  -  |  -  |  -  |
| Ethernet3 |  P2P_LINK_TO_DC1-SPINE3_Ethernet7  |  routed  | - |  172.31.255.53/31  |  default  |  1500  |  -  |  -  |  -  |
| Ethernet4 |  P2P_LINK_TO_DC1-SPINE4_Ethernet7  |  routed  | - |  172.31.255.55/31  |  default  |  1500  |  -  |  -  |  -  |

### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet1
   description P2P_LINK_TO_DC1-SPINE1_Ethernet7
   no switchport
   ip address 172.31.255.49/31
!
interface Ethernet2
   description P2P_LINK_TO_DC1-SPINE2_Ethernet7
   no switchport
   ip address 172.31.255.51/31
!
interface Ethernet3
   description P2P_LINK_TO_DC1-SPINE3_Ethernet7
   no switchport
   ip address 172.31.255.53/31
!
interface Ethernet4
   description P2P_LINK_TO_DC1-SPINE4_Ethernet7
   no switchport
   ip address 172.31.255.55/31
```

## Port-Channel Interfaces

No port-channels defined

## Loopback Interfaces

### Loopback Interfaces Summary

#### IPv4

| Interface | Description | VRF | IP Address |
| --------- | ----------- | --- | ---------- |
| Loopback0 | EVPN_Overlay_Peering | default | 192.168.255.11/32 |
| Loopback1 | VTEP_VXLAN_Tunnel_Source | default | 192.168.254.11/32 |

#### IPv6

| Interface | Description | VRF | IPv6 Address |
| --------- | ----------- | --- | ------------ |
| Loopback0 | EVPN_Overlay_Peering | default | - |
| Loopback1 | VTEP_VXLAN_Tunnel_Source | default | - |


### Loopback Interfaces Device Configuration

```eos
!
interface Loopback0
   description EVPN_Overlay_Peering
   ip address 192.168.255.11/32
!
interface Loopback1
   description VTEP_VXLAN_Tunnel_Source
   ip address 192.168.254.11/32
```

## VLAN Interfaces

### VLAN Interfaces Summary

| Interface | Description | VRF |  MTU | Shutdown |
| --------- | ----------- | --- | ---- | -------- |
| Vlan150 |  Tenant_A_WAN_Zone_1  |  Tenant_A_WAN_Zone  |  -  |  false  |
| Vlan250 |  Tenant_B_WAN_Zone_1  |  Tenant_B_WAN_Zone  |  -  |  false  |
| Vlan350 |  Tenant_C_WAN_Zone_1  |  Tenant_C_WAN_Zone  |  -  |  false  |
| Vlan3013 |  MLAG_PEER_L3_iBGP: vrf Tenant_A_WAN_Zone  |  Tenant_A_WAN_Zone  |  -  |  -  |
| Vlan3020 |  MLAG_PEER_L3_iBGP: vrf Tenant_B_WAN_Zone  |  Tenant_B_WAN_Zone  |  -  |  -  |
| Vlan3030 |  MLAG_PEER_L3_iBGP: vrf Tenant_C_WAN_Zone  |  Tenant_C_WAN_Zone  |  -  |  -  |
| Vlan4093 |  MLAG_PEER_L3_PEERING  |  default  |  -  |  -  |
| Vlan4094 |  MLAG_PEER  |  default  |  1500  |  -  |

#### IPv4

| Interface | VRF | IP Address | IP Address Virtual | IP Router Virtual Address | VRRP | ACL In | ACL Out |
| --------- | --- | ---------- | ------------------ | ------------------------- | ---- | ------ | ------- |
| Vlan150 |  Tenant_A_WAN_Zone  |  -  |  10.1.40.1/24  |  -  |  -  |  -  |  -  |
| Vlan250 |  Tenant_B_WAN_Zone  |  -  |  10.2.50.1/24  |  -  |  -  |  -  |  -  |
| Vlan350 |  Tenant_C_WAN_Zone  |  -  |  10.3.50.1/24  |  -  |  -  |  -  |  -  |
| Vlan3013 |  Tenant_A_WAN_Zone  |  10.255.251.11/31  |  -  |  -  |  -  |  -  |  -  |
| Vlan3020 |  Tenant_B_WAN_Zone  |  10.255.251.11/31  |  -  |  -  |  -  |  -  |  -  |
| Vlan3030 |  Tenant_C_WAN_Zone  |  10.255.251.11/31  |  -  |  -  |  -  |  -  |  -  |
| Vlan4093 |  default  |  10.255.251.11/31  |  -  |  -  |  -  |  -  |  -  |
| Vlan4094 |  default  |  10.255.252.11/31  |  -  |  -  |  -  |  -  |  -  |

| Interface | Description | VRF | IP Address | IP Address Virtual | IP Router Virtual Address (vARP) |
| --------- | ----------- | --- | ---------- | ------------------ | -------------------------------- |
| Vlan150 | Tenant_A_WAN_Zone_1 | Tenant_A_WAN_Zone | - | 10.1.40.1/24 | - |
| Vlan250 | Tenant_B_WAN_Zone_1 | Tenant_B_WAN_Zone | - | 10.2.50.1/24 | - |
| Vlan350 | Tenant_C_WAN_Zone_1 | Tenant_C_WAN_Zone | - | 10.3.50.1/24 | - |


### VLAN Interfaces Device Configuration

```eos
!
interface Vlan150
   description Tenant_A_WAN_Zone_1
   vrf Tenant_A_WAN_Zone
   ip address virtual 10.1.40.1/24
!
interface Vlan250
   description Tenant_B_WAN_Zone_1
   vrf Tenant_B_WAN_Zone
   ip address virtual 10.2.50.1/24
!
interface Vlan350
   description Tenant_C_WAN_Zone_1
   vrf Tenant_C_WAN_Zone
   ip address virtual 10.3.50.1/24
```

## VXLAN Interface

### VXLAN Interface Summary

#### Source Interface: Loopback1

#### UDP port: 4789

#### VLAN to VNI Mappings

| VLAN | VNI |
| ---- | --- |
| 150 | 10150 |
| 250 | 20250 |
| 350 | 30350 |

#### VRF to VNI Mappings

| VLAN | VNI |
| ---- | --- |
| Tenant_A_WAN_Zone | 14 |
| Tenant_B_WAN_Zone | 21 |
| Tenant_C_WAN_Zone | 31 |

### VXLAN Interface Device Configuration

```eos
!
interface Vxlan1
   vxlan source-interface Loopback1
   vxlan udp-port 4789
   vxlan vlan 150 vni 10150
   vxlan vlan 250 vni 20250
   vxlan vlan 350 vni 30350
   vxlan vrf Tenant_A_WAN_Zone vni 14
   vxlan vrf Tenant_B_WAN_Zone vni 21
   vxlan vrf Tenant_C_WAN_Zone vni 31
```

# Routing

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
| default | true| | MGMT | false |
| Tenant_A_WAN_Zone | true |
| Tenant_B_WAN_Zone | true |
| Tenant_C_WAN_Zone | true |

### IP Routing Device Configuration

```eos
!
ip routing
no ip routing vrf MGMT
ip routing vrf Tenant_A_WAN_Zone
ip routing vrf Tenant_B_WAN_Zone
ip routing vrf Tenant_C_WAN_Zone
```

## IPv6 Routing

### IPv6 Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | false || MGMT | false |
| Tenant_A_WAN_Zone | false |
| Tenant_B_WAN_Zone | false |
| Tenant_C_WAN_Zone | false |


## Static Routes

### Static Routes Summary

| VRF | Destination Prefix | Next Hop IP             | Exit interface      | Administrative Distance       | Tag               | Route Name                    | Metric         |
| --- | ------------------ | ----------------------- | ------------------- | ----------------------------- | ----------------- | ----------------------------- | -------------- |
| MGMT  | 0.0.0.0/0 |  192.168.200.5  |  -  |  1  |  -  |  -  |  - |

### Static Routes Device Configuration

```eos
!
ip route vrf MGMT 0.0.0.0/0 192.168.200.5
```

## IPv6 Static Routes

IPv6 static routes not defined

## Router ISIS

Router ISIS not defined

## Router BGP

### Router BGP Summary

| BGP AS | Router ID |
| ------ | --------- |
| 65104|  192.168.255.11 |

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
| Remote_as | 65001 |
| Source | Loopback0 |
| Bfd | true |
| Ebgp multihop | 3 |
| Send community | true |
| Maximum routes | 0 (no limit) |

#### IPv4-UNDERLAY-PEERS

| Settings | Value |
| -------- | ----- |
| Address Family | ipv4 |
| Remote_as | 65001 |
| Send community | true |
| Maximum routes | 12000 |

### BGP Neighbors

| Neighbor | Remote AS |
| -------- | ---------
| 172.31.255.48 | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.31.255.50 | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.31.255.52 | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.31.255.54 | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 192.168.255.1 | Inherited from peer group EVPN-OVERLAY-PEERS |
| 192.168.255.2 | Inherited from peer group EVPN-OVERLAY-PEERS |
| 192.168.255.3 | Inherited from peer group EVPN-OVERLAY-PEERS |
| 192.168.255.4 | Inherited from peer group EVPN-OVERLAY-PEERS |

### Router BGP EVPN Address Family

#### Router BGP EVPN MAC-VRFs

##### VLAN aware bundles

| VLAN Aware Bundle | Route-Distinguisher | Both Route-Target | Import Route Target | Export Route-Target | Redistribute | VLANs |
| ----------------- | ------------------- | ----------------- | ------------------- | ------------------- | ------------ | ----- |
| Tenant_A_WAN_Zone | 192.168.255.11:14 |  14:14  |  |  | learned | 150 |
| Tenant_B_WAN_Zone | 192.168.255.11:21 |  21:21  |  |  | learned | 250 |
| Tenant_C_WAN_Zone | 192.168.255.11:31 |  31:31  |  |  | learned | 350 |

#### Router BGP EVPN VRFs

| VRF | Route-Distinguisher | Redistribute |
| --- | ------------------- | ------------ |
| Tenant_A_WAN_Zone | 192.168.255.11:14 | connected |
| Tenant_B_WAN_Zone | 192.168.255.11:21 | connected |
| Tenant_C_WAN_Zone | 192.168.255.11:31 | connected |

### Router BGP Device Configuration

```eos
!
router bgp 65104
   router-id 192.168.255.11
   no bgp default ipv4-unicast
   distance bgp 20 200 200
   maximum-paths 4 ecmp 4
   neighbor EVPN-OVERLAY-PEERS peer group
   neighbor EVPN-OVERLAY-PEERS remote-as 65001
   neighbor EVPN-OVERLAY-PEERS update-source Loopback0
   neighbor EVPN-OVERLAY-PEERS bfd
   neighbor EVPN-OVERLAY-PEERS ebgp-multihop 3
   neighbor EVPN-OVERLAY-PEERS password 7 q+VNViP5i4rVjW1cxFv2wA==
   neighbor EVPN-OVERLAY-PEERS send-community
   neighbor EVPN-OVERLAY-PEERS maximum-routes 0
   neighbor IPv4-UNDERLAY-PEERS peer group
   neighbor IPv4-UNDERLAY-PEERS remote-as 65001
   neighbor IPv4-UNDERLAY-PEERS password 7 AQQvKeimxJu+uGQ/yYvv9w==
   neighbor IPv4-UNDERLAY-PEERS send-community
   neighbor IPv4-UNDERLAY-PEERS maximum-routes 12000
   neighbor 172.31.255.48 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.31.255.50 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.31.255.52 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.31.255.54 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.255.1 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.255.2 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.255.3 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.255.4 peer group EVPN-OVERLAY-PEERS
   redistribute connected route-map RM-CONN-2-BGP
   !
   vlan-aware-bundle Tenant_A_WAN_Zone
      rd 192.168.255.11:14
      route-target both 14:14
      redistribute learned
      vlan 150
   !
   vlan-aware-bundle Tenant_B_WAN_Zone
      rd 192.168.255.11:21
      route-target both 21:21
      redistribute learned
      vlan 250
   !
   vlan-aware-bundle Tenant_C_WAN_Zone
      rd 192.168.255.11:31
      route-target both 31:31
      redistribute learned
      vlan 350
   !
   address-family evpn
      neighbor EVPN-OVERLAY-PEERS activate
      no neighbor IPv4-UNDERLAY-PEERS activate
   !
   address-family ipv4
      no neighbor EVPN-OVERLAY-PEERS activate
      neighbor IPv4-UNDERLAY-PEERS activate
   !
   vrf Tenant_A_WAN_Zone
      rd 192.168.255.11:14
      route-target import evpn 14:14
      route-target export evpn 14:14
      router-id 192.168.255.11
      redistribute connected
   !
   vrf Tenant_B_WAN_Zone
      rd 192.168.255.11:21
      route-target import evpn 21:21
      route-target export evpn 21:21
      router-id 192.168.255.11
      redistribute connected
   !
   vrf Tenant_C_WAN_Zone
      rd 192.168.255.11:31
      route-target import evpn 31:31
      route-target export evpn 31:31
      router-id 192.168.255.11
      redistribute connected
```

## Router BFD

### Router BFD Multihop Summary

| Interval | Minimum RX | Multiplier |
| -------- | ---------- | ---------- |
| 1200 | 1200 | 3 |

### Router BFD Multihop Device Configuration

```eos
!
router bfd
   multihop interval 1200 min-rx 1200 multiplier 3
```

# Multicast

## IP IGMP Snooping

### IP IGMP Snooping Summary

## Router Multicast

Routing multicast not defined

## Router PIM Sparse Mode

Router PIM sparse mode not defined

# Filters

## Community-lists

Community-lists not defined

## Peer Filters

No peer filters defined

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

IPv6 prefix-lists not defined

## Route-maps

### Route-maps Summary

#### RM-CONN-2-BGP

| Sequence | Type | Match and/or Set |
| -------- | ---- | ---------------- |
| 10 | permit | match ip address prefix-list PL-LOOPBACKS-EVPN-OVERLAY |

### Route-maps Device Configuration

```eos
!
route-map RM-CONN-2-BGP permit 10
   match ip address prefix-list PL-LOOPBACKS-EVPN-OVERLAY
```

## IP Extended Communities

No extended community defined

# ACL

## Standard Access-lists

Standard access-lists not defined

## Extended Access-lists

Extended access-lists not defined

## IPv6 Standard Access-lists

IPv6 standard access-lists not defined

## IPv6 Extended Access-lists

IPv6 extended access-lists not defined

# VRF Instances

## VRF Instances Summary

| VRF Name | IP Routing |
| -------- | ---------- |
| MGMT | disabled |
| Tenant_A_WAN_Zone | enabled |
| Tenant_B_WAN_Zone | enabled |
| Tenant_C_WAN_Zone | enabled |

## VRF Instances Device Configuration

```eos
!
vrf instance MGMT
!
vrf instance Tenant_A_WAN_Zone
!
vrf instance Tenant_B_WAN_Zone
!
vrf instance Tenant_C_WAN_Zone
```

# Virtual Source NAT

Virtual source NAT not defined

# Platform

No platform parameters defined

# Router L2 VPN

Router L2 VPN not defined

# IP DHCP Relay

IP DHCP relay not defined

# Custom Templates

No custom templates defined
