# router-bgp-v4-v6-evpn

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

Static routes not defined

## IPv6 Static Routes

IPv6 static routes not defined

## Router ISIS

Router ISIS not defined

## Router BGP

### Router BGP Summary

| BGP AS | Router ID |
| ------ | --------- |
| 65100|  10.50.64.15 |

| BGP Tuning |
| ---------- |
| no bgp default ipv4-unicast |
| update wait-install |
| distance bgp 20 200 200 |
| maximum-paths 4 ecmp 4 |

### Router BGP Peer Groups

#### EVPN-OVERLAY

| Settings | Value |
| -------- | ----- |
| Remote_as | 65000 |
| Next-hop unchanged | True |
| Source | Loopback0 |
| Bfd | true |
| Ebgp multihop | 5 |
| Send community | true |
| Maximum routes | 0 (no limit) |

#### IPV4-UNDERLAY

| Settings | Value |
| -------- | ----- |
| Remote_as | 65000 |
| Send community | true |
| Maximum routes | 12000 |

#### IPV4-UNDERLAY-MLAG

| Settings | Value |
| -------- | ----- |
| Remote_as | 65100 |
| Next-hop self | True |
| Send community | true |
| Maximum routes | 12000 |

#### IPV6-UNDERLAY

| Settings | Value |
| -------- | ----- |
| Remote_as | 65000 |
| Send community | true |
| Maximum routes | 12000 |

#### IPV6-UNDERLAY-MLAG

| Settings | Value |
| -------- | ----- |
| Remote_as | 65100 |
| Next-hop self | True |
| Send community | true |
| Maximum routes | 12000 |

### BGP Neighbors

| Neighbor | Remote AS |
| -------- | ---------
| 1.1.1.1 | 1 |
| 1b11:3a00:22b0:0088::1 | Inherited from peer group IPV6-UNDERLAY |
| 1b11:3a00:22b0:0088::3 | Inherited from peer group IPV6-UNDERLAY |
| 1b11:3a00:22b0:0088::5 | Inherited from peer group IPV6-UNDERLAY |
| 10.50.2.1 | Inherited from peer group IPV4-UNDERLAY |
| 10.50.2.3 | Inherited from peer group IPV4-UNDERLAY |
| 10.50.2.5 | Inherited from peer group IPV4-UNDERLAY |
| 10.50.64.11 | Inherited from peer group EVPN-OVERLAY |
| 10.50.64.12 | Inherited from peer group EVPN-OVERLAY |
| 10.50.64.13 | Inherited from peer group EVPN-OVERLAY |
| 169.254.252.1 | Inherited from peer group IPV4-UNDERLAY-MLAG |
| fe80::b%Vl4094 | Inherited from peer group IPV6-UNDERLAY-MLAG |

### Router BGP EVPN Address Family

#### Router BGP EVPN MAC-VRFs

##### VLAN Based

| VLAN | Route-Distinguisher | Both Route-Target | Import Route Target | Export Route-Target | Redistribute |
| ---- | ------------------- | ----------------- | ------------------- | ------------------- | ------------ |
| 24 | 10.50.64.15:10024 |  1:10024 |  -  | -  | learned |
| 41 | 10.50.64.15:10041 |  1:10041 |  -  | -  | learned |
| 42 | 10.50.64.15:10042 |  1:10042 |  -  | -  | learned |
| 65 | 10.50.64.15:10065 |  1:10065 |  -  | -  | learned |

#### Router BGP EVPN VRFs

| VRF | Route-Distinguisher | Redistribute |
| --- | ------------------- | ------------ |
| Tenant_A | 10.50.64.15:30001 | connected |
| Tenant_B | 10.50.64.15:30002 ||

### Router BGP Device Configuration

```eos
!
router bgp 65100
   router-id 10.50.64.15
   no bgp default ipv4-unicast
   update wait-install
   distance bgp 20 200 200
   maximum-paths 4 ecmp 4
   neighbor EVPN-OVERLAY peer group
   neighbor EVPN-OVERLAY remote-as 65000
   neighbor EVPN-OVERLAY next-hop-unchanged
   neighbor EVPN-OVERLAY update-source Loopback0
   neighbor EVPN-OVERLAY bfd
   neighbor EVPN-OVERLAY ebgp-multihop 5
   neighbor EVPN-OVERLAY password 7 $1c$G8BQN0ezkiJOX2cuAYpsEA==
   neighbor EVPN-OVERLAY send-community
   neighbor EVPN-OVERLAY maximum-routes 0
   neighbor IPV4-UNDERLAY peer group
   neighbor IPV4-UNDERLAY remote-as 65000
   neighbor IPV4-UNDERLAY password 7 $1c$G8BQN0ezkiJOX2cuAYpsEA==
   neighbor IPV4-UNDERLAY send-community
   neighbor IPV4-UNDERLAY maximum-routes 12000
   neighbor IPV4-UNDERLAY-MLAG peer group
   neighbor IPV4-UNDERLAY-MLAG remote-as 65100
   neighbor IPV4-UNDERLAY-MLAG next-hop-self
   neighbor IPV4-UNDERLAY-MLAG password 7 $1c$G8BQN0ezkiJOX2cuAYpsEA==
   neighbor IPV4-UNDERLAY-MLAG send-community
   neighbor IPV4-UNDERLAY-MLAG maximum-routes 12000
   neighbor IPV6-UNDERLAY peer group
   neighbor IPV6-UNDERLAY remote-as 65000
   neighbor IPV6-UNDERLAY password 7 $1c$G8BQN0ezkiJOX2cuAYpsEA==
   neighbor IPV6-UNDERLAY send-community
   neighbor IPV6-UNDERLAY maximum-routes 12000
   neighbor IPV6-UNDERLAY-MLAG peer group
   neighbor IPV6-UNDERLAY-MLAG remote-as 65100
   neighbor IPV6-UNDERLAY-MLAG next-hop-self
   neighbor IPV6-UNDERLAY-MLAG password 7 $1c$G8BQN0ezkiJOX2cuAYpsEA==
   neighbor IPV6-UNDERLAY-MLAG send-community
   neighbor IPV6-UNDERLAY-MLAG maximum-routes 12000
   neighbor 1.1.1.1 remote-as 1
   neighbor 1.1.1.1 description TEST
   neighbor 1b11:3a00:22b0:0088::1 peer group IPV6-UNDERLAY
   neighbor 1b11:3a00:22b0:0088::3 peer group IPV6-UNDERLAY
   neighbor 1b11:3a00:22b0:0088::5 peer group IPV6-UNDERLAY
   neighbor 10.50.2.1 peer group IPV4-UNDERLAY
   neighbor 10.50.2.3 peer group IPV4-UNDERLAY
   neighbor 10.50.2.5 peer group IPV4-UNDERLAY
   neighbor 10.50.64.11 peer group EVPN-OVERLAY
   neighbor 10.50.64.12 peer group EVPN-OVERLAY
   neighbor 10.50.64.13 peer group EVPN-OVERLAY
   neighbor 169.254.252.1 peer group IPV4-UNDERLAY-MLAG
   neighbor fe80::b%Vl4094 peer group IPV6-UNDERLAY-MLAG
   redistribute connected route-map RM-CONN-2-BGP
   redistribute static route-map RM-STATIC-2-BGP
   !
   vlan 24
      rd 10.50.64.15:10024
      route-target both 1:10024
      redistribute learned
   !
   vlan 41
      rd 10.50.64.15:10041
      route-target both 1:10041
      redistribute learned
   !
   vlan 42
      rd 10.50.64.15:10042
      route-target both 1:10042
      redistribute learned
   !
   vlan 65
      rd 10.50.64.15:10065
      route-target both 1:10065
      redistribute learned
   !
   address-family evpn
      neighbor EVPN-OVERLAY activate
   !
   address-family ipv4
      neighbor IPV4-UNDERLAY route-map RM-HIDE-AS-PATH in
      neighbor IPV4-UNDERLAY route-map RM-HIDE-AS-PATH out
      neighbor IPV4-UNDERLAY activate
      neighbor IPV4-UNDERLAY-MLAG activate
   !
   address-family ipv4 multicast
      neighbor IPV4-UNDERLAY activate
      neighbor IPV4-UNDERLAY-MLAG activate
      redistribute attached-host 
   !
   address-family ipv6
      neighbor IPV6-UNDERLAY route-map RM-HIDE-AS-PATH in
      neighbor IPV6-UNDERLAY route-map RM-HIDE-AS-PATH out
      neighbor IPV6-UNDERLAY activate
      neighbor IPV6-UNDERLAY-MLAG activate
   !
   vrf Tenant_A
      rd 10.50.64.15:30001
      route-target import evpn 1:30001
      route-target export evpn 1:30001
      redistribute connected
   !
   vrf Tenant_B
      rd 10.50.64.15:30002
      route-target import evpn 1:30002
      route-target export evpn 1:30002
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
