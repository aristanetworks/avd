# router-isis

# Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
  - [DNS Domain](#dns-domain)
  - [Name Servers](#name-servers)
  - [Domain Lookup](#domain-lookup)
  - [NTP](#ntp)
  - [Management SSH](#management-ssh)
  - [Management GNMI](#management-api-gnmi)
  - [Management API](#Management-api-http)
- [Authentication](#authentication)
  - [Local Users](#local-users)
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
  - [Logging](#logging)
  - [SFlow](#sflow)
  - [Hardware Counters](#hardware-counters)
  - [VM Tracer Sessions](#vm-tracer-sessions)
  - [Event Handler](#event-handler)
- [MLAG](#mlag)
- [Spanning Tree](#spanning-tree)
- [Internal VLAN Allocation Policy](#internal-vlan-allocation-policy)
- [VLANs](#vlans)
- [Interfaces](#interfaces)
  - [Ethernet Interfaces](#ethernet-interfaces)
  - [Port-Channel Interfaces](#port-channel-interfaces)
  - [Loopback Interfaces](#loopback-interfaces)
  - [VLAN Interfaces](#vlan-interfaces)
  - [VXLAN Interface](#vxlan-interface)
- [Routing](#routing)
  - [Virtual Router MAC Address](#virtual-router-mac-address)
  - [IP Routing](#ip-routing)
  - [IPv6 Routing](#ipv6-routing)
  - [Static Routes](#static-routes)
  - [Router ISIS](#router-isis)
  - [Router BGP](#router-bgp)
  - [Router BFD](#router-bfd)
- [Multicast](#multicast)
  - [IP IGMP Snooping](#ip-igmp-snooping)
  - [Router Multicast](#router-multicast)
  - [Router PIM Sparse Mode](#router-pim-sparse-mode)
- [Filters](#filters)
  - [Community Lists](#community-lists)
  - [Peer Filters](#peer-filters)
  - [Prefix Lists](#prefix-lists)
  - [IPv6 Prefix Lists](#ipv6-prefix-lists)
  - [Route Maps](#route-maps)
  - [IP Extended Communities](#ip-extended-communities)
- [ACL](#acl)
  - [Standard Access-lists](#standard-access-lists)
  - [Extended Access-lists](#extended-access-lists)
  - [IPv6 Standard Access-lists](#ipv6-standard-access-lists)
  - [IPv6 Extended Access-lists](#ipv6-extended-access-lists)
- [VRF Instances](#vrf-instances)
- [Virtual Source NAT](#virtual-source-nat)
- [Platform](#platform)
- [Router L2 VPN](#router-l2-vpn)
- [IP DHCP Relay](#ip-dhcp-relay)

# Management

## Management Interfaces

### Management Interfaces Summary

IPv4

| Management Interface | description | VRF | IP Address | Gateway |
| -------------------- | ----------- | --- | ---------- | ------- |
| Management1 | oob_management | MGMT | 10.73.254.11/24 | 10.73.254.253 |

IPv6

| Management Interface | description | VRF | IPv6 Address | IPv6 Gateway |
| -------------------- | ----------- | --- | ------------ | ------------ |
| Management1 | oob_management | MGMT | not configured  | not configured |

### Management Interfaces Device Configuration

```eos
!
interface Management1
   description oob_management
   vrf MGMT
   ip address 10.73.254.11/24
```

## DNS Domain

DNS domain not defined

## Domain-List

Domain-list not defined

## Name Servers

No Name Servers defined

## Domain Lookup

DNS domain lookup not defined

## NTP

No NTP servers defined

## Management SSH

Management SSH is not defined

## Management API GNMI

Management API gnmi is not defined
  
## Management API HTTP


Management API HTTP is not defined

# Authentication

## Local Users

No Users Defined

## TACACS Servers

TACACS servers not configured

## IP TACACS Source Interfaces

IP TACACS source interfaces not defined

## RADIUS Servers

RADIUS servers not configured

## AAA Server Groups

AAA server groups not defined

## AAA Authentication

AAA authentication not defined

## AAA Authorization

AAA authorization not defined

## AAA Accounting

AAA accounting not defined

# Management Security

Management Security not defined

# Aliases

Aliases not defined

# Monitoring

## TerminAttr Daemon

TerminAttr Daemon not defined

## Logging

No logging settings defined

## SFlow

No sFlow defined

## Hardware Counters

No Hardware Counters defined

## VM Tracer Sessions

No VM tracer session defined

## Event Handler

No Event Handler Defined

# MLAG

MLAG not defined

# Spanning Tree

Spanning-Tree Not Defined

# Internal VLAN Allocation Policy

## Internal VLAN Allocation Policy Summary

**Default Allocation Policy**

| Policy Allocation | Range Beginning | Range Ending |
| ------------------| --------------- | ------------ |
| ascending | 1006 | 4094 |

# VLANs

No VLANs defined

# Interfaces

## Ethernet Interfaces

### Ethernet Interfaces Summary

| Interface | Description | MTU | Type | Mode | Allowed VLANs (Trunk) | Trunk Group | VRF | IP Address | Channel-Group ID | Channel-Group Type |
| --------- | ----------- | --- | ---- | ---- | --------------------- | ----------- | --- | ---------- | ---------------- | ------------------ |
| Ethernet1 | P2P_LINK_TO_EAPI-SPINE1_Ethernet1 | 1500 | routed | access | - | - | - | 172.31.255.1/31 | - | - |
| Ethernet2 | P2P_LINK_TO_EAPI-SPINE2_Ethernet1 | 1500 | routed | access | - | - | - | 172.31.255.3/31 | - | - |
| Ethernet3 | MLAG_PEER_EAPI-LEAF1B_Ethernet3 | *1500 | *switched | *access | - | - | - | - | 3 | active |

*Inherited from Port-Channel Interface

### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet1
   description P2P_LINK_TO_EAPI-SPINE1_Ethernet1
   no switchport
   ip address 172.31.255.1/31
   isis enable EVPN_UNDERLAY
   isis metric 50
   isis network point-to-point
!
interface Ethernet2
   description P2P_LINK_TO_EAPI-SPINE2_Ethernet1
   no switchport
   ip address 172.31.255.3/31
   isis enable EVPN_UNDERLAY
   isis metric 50
   isis network point-to-point
!
interface Ethernet3
   description MLAG_PEER_EAPI-LEAF1B_Ethernet3
   channel-group 3 mode active
```

## Port-Channel Interfaces

No Port-Channels defined

## Loopback Interfaces

### Loopback Interfaces Summary

IPv4

| Interface | Description | VRF | IP Address |
| --------- | ----------- | --- | ---------- |
| Loopback0 | EVPN_Overlay_Peering | Global Routing Table | 192.168.255.3/32 |
| Loopback1 | VTEP_VXLAN_Tunnel_Source | Global Routing Table | 192.168.254.3/32 |

IPv6

| Interface | Description | VRF | IPv6 Address |
| --------- | ----------- | --- | ------------ |
| Loopback0 | EVPN_Overlay_Peering | Global Routing Table | - |
| Loopback1 | VTEP_VXLAN_Tunnel_Source | Global Routing Table | - |

### Loopback Interfaces Device Configuration

```eos
!
interface Loopback0
   description EVPN_Overlay_Peering
   ip address 192.168.255.3/32
   isis enable EVPN_UNDERLAY
   isis passive
!
interface Loopback1
   description VTEP_VXLAN_Tunnel_Source
   ip address 192.168.254.3/32
   isis enable EVPN_UNDERLAY
   isis passive
```

## VLAN Interfaces

### VLAN Interfaces Summary

| Interface | Description | VRF | IP Address | IP Address Virtual | IP Router Virtual Address (vARP) |
| --------- | ----------- | --- | ---------- | ------------------ | -------------------------------- |
| Vlan110 | PR01-DEMO | TENANT_A_PROJECT01 | - | 10.1.10.254/24 | - |
| Vlan4093 | MLAG_PEER_L3_PEERING | Global Routing Table | 10.255.251.0/31 | - | - |
| Vlan4094 | MLAG_PEER | Global Routing Table | 10.255.252.0/31 | - | - |

### VLAN Interfaces Device Configuration

```eos
!
interface Vlan110
   description PR01-DEMO
   vrf TENANT_A_PROJECT01
   ip address virtual 10.1.10.254/24
!
interface Vlan4093
   description MLAG_PEER_L3_PEERING
   ip address 10.255.251.0/31
   isis enable EVPN_UNDERLAY
   isis metric 50
   isis network point-to-point
!
interface Vlan4094
   description MLAG_PEER
   no autostate
   ip address 10.255.252.0/31
```

## VXLAN Interface

No VXLAN interface defined

# Routing

## Virtual Router MAC Address

IP Virtual Router MAC Address is not defined

## IP Routing

### IP Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default |  False| 

### IP Routing Device Configuration

```eos
```
## IPv6 Routing

### IPv6 Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default |  False | 

## Static Routes


## IPv6 Static Routes


## Router ISIS

### Router ISIS Summary

| Settings | Value |
| -------- | ----- |
| Instance | EVPN_UNDERLAY |
| Net-ID | 49.0001.0001.0001.0001.00 |
| Type | level-2 |
| Address Family | ipv4 unicast |

### ISIS interfaces Summary

| Interface | ISIS instance | ISIS metric | Interface mode |
| -------- | -------- | -------- | -------- |
| Ethernet1 | EVPN_UNDERLAY |  50 |  point-to-point |
| Ethernet2 | EVPN_UNDERLAY |  50 |  point-to-point |
| Vlan4093 | EVPN_UNDERLAY |  50 |  point-to-point |
| Loopback0 | EVPN_UNDERLAY |  - |  passive |
| Loopback1 | EVPN_UNDERLAY |  - |  passive |

### Router ISIS Device Configuration

```eos
router isis EVPN_UNDERLAY
   net 49.0001.0001.0001.0001.00
   is-type level-2
   router-id ipv4 192.168.255.3
   log-adjacency-changes
   !
   address-family ipv4 unicast
      maximum-paths 2
   !
!
```


## Router BGP

Router BGP not defined

## Router BFD

### Router BFD Multihop Summary

| Interval | Minimum RX | Multiplier |
| -------- | ---------- | ---------- |
| 300 | 300 | 3 |

*No device configuration required - default values

# Multicast

## IP IGMP Snooping

No IP IGMP configuration

## Router Multicast

Routing multicast not defined

## Router PIM Sparse Mode

Router PIM sparse mode not defined

# Filters

## Community Lists

Community Lists not defined

## Peer Filters

No Peer Filters defined

## Prefix Lists

Prefix lists not defined

## IPv6 Prefix Lists

IPv6 Prefix lists not defined

## Route Maps

No route maps defined

## IP Extended Communities

No Extended community defined

# ACL

## Standard Access-lists

Standard Access-lists not defined

## Extended Access-lists

Extended Access-lists not defined

## IPv6 Standard Access-lists

IPv6 Standard Access-lists not defined

## IPv6 Extended Access-lists

IPv6 Extended Access-lists not defined

# VRF Instances

No VRFs defined

# Virtual Source NAT

Virtual Source NAT is not defined

# Platform

No Platform parameters defined

# Router L2 VPN

Router L2 VPN not defined

# IP DHCP Relay

IP DHCP Relay not defined

# Custom Templates

No Custom Templates Defined
