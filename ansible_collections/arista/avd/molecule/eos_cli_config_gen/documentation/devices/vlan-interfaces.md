# vlan-interfaces

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
  - [SNMP](#snmp)
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
  - [IPv6 Static Routes](#ipv6-static-routes)
  - [Router ISIS](#router-isis)
  - [Router BGP](#router-bgp)
  - [Router BFD](#router-bfd)
- [Multicast](#multicast)
  - [IP IGMP Snooping](#ip-igmp-snooping)
  - [Router Multicast](#router-multicast)
  - [Router PIM Sparse Mode](#router-pim-sparse-mode)
- [Filters](#filters)
  - [Community-lists](#community-lists)
  - [Peer Filters](#peer-filters)
  - [Prefix-lists](#prefix-lists)
  - [IPv6 Prefix-lists](#ipv6-prefix-lists)
  - [Route-maps](#route-maps)
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

#### IPv4

| Management Interface | description | VRF | IP Address | Gateway |
| -------------------- | ----------- | --- | ---------- | ------- |
| Management1 | oob_management | MGMT | 10.73.255.122/24 | 10.73.255.2 |

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
   ip address 10.73.255.122/24
```

## DNS Domain

DNS domain not defined

## Domain-list

Domain-list not defined

## Name Servers

No name servers defined

## Domain Lookup

DNS domain lookup not defined

## NTP

No NTP servers defined

## Management SSH

Management SSH not defined

## Management API GNMI

Management API gnmi is not defined

## Management API HTTP

Management API HTTP not defined

# Authentication

## Local Users

No users defined

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

TerminAttr daemon not defined

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

Spanning-tree not defined

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

No ethernet interface defined

## Port-Channel Interfaces

No port-channels defined

## Loopback Interfaces

No loopback interfaces defined

## VLAN Interfaces

### VLAN Interfaces Summary

| Interface | Description | VRF | IP Address | IP Address Virtual | IP Router Virtual Address (vARP) |
| --------- | ----------- | --- | ---------- | ------------------ | -------------------------------- |
| Vlan24 | SVI Description | default | - | 10.10.24.1/24 | - |
| Vlan41 | SVI Description | default | - | 10.10.41.1/24 | - |
| Vlan42 | SVI Description | default | - | 10.10.42.1/24 | - |
| Vlan75 | SVI Description | default | - | 10.10.75.1/24 | - |
| Vlan83 | SVI Description | default | - | 10.10.83.1/24 | - |
| Vlan84 | SVI Description | default | - | 10.10.84.1/24 | - |
| Vlan85 | SVI Description | default | 10.10.84.1/24 | - | - |
| Vlan87 | SVI Description | default | 10.10.87.1/24 | - | - |
| Vlan88 | SVI Description | default | - | 10.10.87.1/23 | - |
| Vlan89 | SVI Description | default | - | 10.10.144.3/20 | - |
| Vlan501 | SVI Description | default | 10.50.26.29/27 | - | - |
| Vlan1001 | SVI Description | Tenant_A | - | 10.1.1.1/24 | - |
| Vlan1002 | SVI Description | Tenant_A | - | 10.1.2.1/24 | - |
| Vlan2001 | SVI Description | Tenant_B | - | 10.2.1.1/24 | - |
| Vlan2002 | SVI Description | Tenant_B | - | 10.2.2.1/24 | - |
| Vlan4094 | SVI Description | default | 169.254.252.0/31 | - | - |


### VLAN Interfaces Device Configuration

```eos
!
interface Vlan24
   description SVI Description
   ip address virtual 10.10.24.1/24
   ipv6 address 1b11:3a00:22b0:6::15/64
   ipv6 nd managed-config-flag
   ipv6 nd prefix 1b11:3a00:22b0:6::/64 infinite infinite no-autoconfig
   ipv6 virtual-router address 1b11:3a00:22b0:6::1
!
interface Vlan41
   description SVI Description
   ip address virtual 10.10.41.1/24
   ip helper-address 10.10.64.150  source-interface Loopback0
   ip helper-address 10.10.96.150  source-interface Loopback0
   ip helper-address 10.10.96.151  source-interface Loopback0
!
interface Vlan42
   description SVI Description
   ip address virtual 10.10.42.1/24
!
interface Vlan75
   description SVI Description
   ip address virtual 10.10.75.1/24
   ipv6 address 1b11:3a00:22b0:1000::15/64
   ipv6 nd managed-config-flag
   ipv6 nd prefix 1b11:3a00:22b0:1000::/64 infinite infinite no-autoconfig
   ipv6 virtual-router address 1b11:3a00:22b0:1000::1
!
interface Vlan83
   description SVI Description
   ip address virtual 10.10.83.1/24
!
interface Vlan84
   description SVI Description
   ip address virtual 10.10.84.1/24
!
interface Vlan85
   description SVI Description
   ip address 10.10.84.1/24
!
interface Vlan87
   description SVI Description
   shutdown
   ip address 10.10.87.1/24
   ip access-group ACL_IN in
   ip access-group ACL_OUT out
!
interface Vlan88
   description SVI Description
   shutdown
   ip address virtual 10.10.87.1/23
!
interface Vlan89
   description SVI Description
   ip address virtual 10.10.144.3/20
   ipv6 address 1b11:3a00:22b0:5200::15/64
   ipv6 nd managed-config-flag
   ipv6 nd prefix 1b11:3a00:22b0:5200::/64 infinite infinite no-autoconfig
   multicast ipv4 source route export 
   pim ipv4 sparse-mode
   pim ipv4 local-interface Loopback0
   ipv6 virtual-router address 1b11:3a00:22b0:5200::3
!
interface Vlan501
   description SVI Description
   ip address 10.50.26.29/27
   ipv6 address 1b11:3a00:22b0:0088::207/127
   ipv6 nd ra disabled
!
interface Vlan1001
   description SVI Description
   vrf Tenant_A
   ip address virtual 10.1.1.1/24
   ipv6 address a1::1/64
   ipv6 nd managed-config-flag
   ipv6 nd prefix a1::/64 infinite infinite no-autoconfig
!
interface Vlan1002
   description SVI Description
   vrf Tenant_A
   ip address virtual 10.1.2.1/24
   ipv6 address a2::1/64
   ipv6 nd ra disabled
   ipv6 nd managed-config-flag
   ipv6 nd prefix a2::/64 infinite infinite no-autoconfig
!
interface Vlan2001
   description SVI Description
   vrf Tenant_B
   ip address virtual 10.2.1.1/24
!
interface Vlan2002
   description SVI Description
   vrf Tenant_B
   ip address virtual 10.2.2.1/24
!
interface Vlan4094
   description SVI Description
   mtu 9214
   ip address 169.254.252.0/31
   ipv6 address fe80::a/64 link-local
   pim ipv4 sparse-mode
```

## VXLAN Interface

No VXLAN interfaces defined

# Routing

## Virtual Router MAC Address

IP virtual router MAC address not defined

## IP Routing

### IP Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | false| 
### IP Routing Device Configuration

```eos
```

## IPv6 Routing

### IPv6 Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | false |

## Static Routes

Static routes not defined

## IPv6 Static Routes

IPv6 static routes not defined

## Router ISIS

Router ISIS not defined

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

## Community-lists

Community-lists not defined

## Peer Filters

No peer filters defined

## Prefix-lists

Prefix-lists not defined

## IPv6 Prefix-lists

IPv6 prefix-lists not defined

## Route-maps

No route-maps defined

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

No VRF instances defined

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
