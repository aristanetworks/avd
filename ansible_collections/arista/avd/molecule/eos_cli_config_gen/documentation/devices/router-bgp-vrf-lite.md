# router-bgp-vrf-lite

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
  - [Interface Defaults](#internet-defaults)
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
- [Errdisable](#errdisable)
- [MAC security](#mac-security)
- [QOS](#qos)
- [QOS Profiles](#qos-profiles)

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

## PTP

PTP is not defined.

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

## Interface Defaults

No Interface Defaults defined

## Ethernet Interfaces

No ethernet interface defined

## Port-Channel Interfaces

No port-channels defined

## Loopback Interfaces

No loopback interfaces defined

## VLAN Interfaces

No VLAN interfaces defined

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

### Static Routes Summary

| VRF | Destination Prefix | Next Hop IP             | Exit interface      | Administrative Distance       | Tag               | Route Name                    | Metric         |
| --- | ------------------ | ----------------------- | ------------------- | ----------------------------- | ----------------- | ----------------------------- | -------------- |
| BLUE-C1  | 193.1.0.0/24 |  -  |  Null0  |  1  |  -  |  -  |  - |
| BLUE-C1  | 193.1.1.0/24 |  -  |  Null0  |  1  |  -  |  -  |  - |
| BLUE-C1  | 193.1.2.0/24 |  -  |  Null0  |  1  |  -  |  -  |  - |

### Static Routes Device Configuration

```eos
!
ip route vrf BLUE-C1 193.1.0.0/24 Null0
ip route vrf BLUE-C1 193.1.1.0/24 Null0
ip route vrf BLUE-C1 193.1.2.0/24 Null0
```

## IPv6 Static Routes

IPv6 static routes not defined

## ARP

Global ARP timeout not defined.

## Router ISIS

Router ISIS not defined

## Router BGP

### Router BGP Summary

| BGP AS | Router ID |
| ------ | --------- |
| 65001|  1.0.1.1 |

| BGP Tuning |
| ---------- |
| no bgp default ipv4-unicast |
| distance bgp 20 200 200 |
| graceful-restart restart-time 300 |
| graceful-restart |

### Router BGP Peer Groups

#### OBS_WAN

| Settings | Value |
| -------- | ----- |
| Address Family | ipv4 |
| Remote_as | 65000 |

#### SEDI

| Settings | Value |
| -------- | ----- |
| Address Family | ipv4 |
| Remote_as | 65003 |
| Source | Loopback101 |
| Ebgp multihop | 10 |

#### WELCOME_ROUTERS

| Settings | Value |
| -------- | ----- |
| Address Family | ipv4 |
| Remote_as | 65001 |

### Router BGP EVPN Address Family

#### Router BGP EVPN MAC-VRFs

#### Router BGP EVPN VRFs

| VRF | Route-Distinguisher | Redistribute |
| --- | ------------------- | ------------ |
| BLUE-C1 | 1.0.1.1:101 | static |

### Router BGP Device Configuration

```eos
!
router bgp 65001
   router-id 1.0.1.1
   no bgp default ipv4-unicast
   distance bgp 20 200 200
   graceful-restart restart-time 300
   graceful-restart
   neighbor OBS_WAN description BGP Connection to OBS WAN CPE
   neighbor OBS_WAN peer group
   neighbor OBS_WAN remote-as 65000
   neighbor SEDI description BGP Connection to OBS WAN CPE
   neighbor SEDI peer group
   neighbor SEDI remote-as 65003
   neighbor SEDI update-source Loopback101
   neighbor SEDI ebgp-multihop 10
   neighbor WELCOME_ROUTERS description BGP Connection to WELCOME ROUTER 02
   neighbor WELCOME_ROUTERS peer group
   neighbor WELCOME_ROUTERS remote-as 65001
   redistribute static
   !
   address-family ipv4
      neighbor OBS_WAN activate
      neighbor SEDI route-map RM-BGP-EXPORT-DEFAULT-BLUE-C1 out
      neighbor SEDI activate
      neighbor WELCOME_ROUTERS activate
   !
   vrf BLUE-C1
      rd 1.0.1.1:101
      neighbor 10.1.1.0 peer group OBS_WAN
      neighbor 10.255.1.1 peer group WELCOME_ROUTERS
      neighbor 101.0.3.1 peer group SEDI
      redistribute static
      aggregate-address 0.0.0.0/0 as-set summary-only attribute-map RM-BGP-AGG-APPLY-SET
      aggregate-address 193.1.0.0/16 as-set summary-only attribute-map RM-BGP-AGG-APPLY-SET
```

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

### Prefix-lists Summary

#### PL-BGP-DEFAULT-BLUE-C1

| Sequence | Action |
| -------- | ------ |
| 10 | permit 0.0.0.0/0 le 1 |

### Prefix-lists Device Configuration

```eos
!
ip prefix-list PL-BGP-DEFAULT-BLUE-C1
   seq 10 permit 0.0.0.0/0 le 1
```

## IPv6 Prefix-lists

IPv6 prefix-lists not defined

## Route-maps

### Route-maps Summary

#### RM-BGP-AGG-APPLY-SET

| Sequence | Type | Match and/or Set |
| -------- | ---- | ---------------- |
| 10 | permit | set local-preference 50 |

#### RM-BGP-EXPORT-DEFAULT-BLUE-C1

| Sequence | Type | Match and/or Set |
| -------- | ---- | ---------------- |
| 10 | permit | match ip address prefix-list PL-BGP-DEFAULT-BLUE-C1 |

### Route-maps Device Configuration

```eos
!
route-map RM-BGP-AGG-APPLY-SET permit 10
   description RM for BGP AGG Set
   set local-preference 50
!
route-map RM-BGP-EXPORT-DEFAULT-BLUE-C1 permit 10
   description RM for BGP default route in BLUE-C1
   match ip address prefix-list PL-BGP-DEFAULT-BLUE-C1
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

No VRF instances defined

# Virtual Source NAT

Virtual source NAT not defined

# Platform

No platform parameters defined

# Router L2 VPN

Router L2 VPN not defined

# IP DHCP Relay

IP DHCP relay not defined

# Errdisable

Errdisable is not defined.

# MACsec

MACsec not defined

# QOS

QOS is not defined.

# QOS Profiles

QOS Profiles are not defined

# Custom Templates

No custom templates defined
