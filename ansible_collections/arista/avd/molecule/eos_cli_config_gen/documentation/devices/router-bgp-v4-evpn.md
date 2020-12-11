# router-bgp-v4-evpn

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
| 65101|  192.168.255.3 |

| BGP Tuning |
| ---------- |
| no bgp default ipv4-unicast |
| distance bgp 20 200 200 |
| graceful-restart restart-time 300 |
| graceful-restart |
| maximum-paths 2 ecmp 2 |

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

#### MLAG-IPv4-UNDERLAY-PEER

| Settings | Value |
| -------- | ----- |
| Address Family | ipv4 |
| Remote_as | 65101 |
| Next-hop self | True |
| Send community | true |
| Maximum routes | 12000 |

### BGP Neighbors

| Neighbor | Remote AS |
| -------- | ---------
| 10.255.251.1 | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER |
| 172.31.255.0 | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.31.255.2 | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 192.168.255.1 | Inherited from peer group EVPN-OVERLAY-PEERS |
| 192.168.255.2 | Inherited from peer group EVPN-OVERLAY-PEERS |

### Router BGP EVPN Address Family

#### Router BGP EVPN MAC-VRFs

##### VLAN aware bundles

| VLAN Aware Bundle | Route-Distinguisher | Both Route-Target | Import Route Target | Export Route-Target | Redistribute | VLANs |
| ----------------- | ------------------- | ----------------- | ------------------- | ------------------- | ------------ | ----- |
| B-ELAN-201 | 192.168.255.3:20201 |  20201:20201  |  |  | learned | 201 |
| TENANT_A_PROJECT01 | 192.168.255.3:11 |  11:11  |  |  | learned | 110 |
| TENANT_A_PROJECT02 | 192.168.255.3:12 |  12:12  |  |  | learned | 112 |

#### Router BGP EVPN VRFs

| VRF | Route-Distinguisher | Redistribute |
| --- | ------------------- | ------------ |
| TENANT_A_PROJECT01 | 192.168.255.3:11 | connected |
| TENANT_A_PROJECT02 | 192.168.255.3:12 | connected |

### Router BGP Device Configuration

```eos
!
router bgp 65101
   router-id 192.168.255.3
   no bgp default ipv4-unicast
   distance bgp 20 200 200
   graceful-restart restart-time 300
   graceful-restart
   maximum-paths 2 ecmp 2
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
   neighbor MLAG-IPv4-UNDERLAY-PEER peer group
   neighbor MLAG-IPv4-UNDERLAY-PEER remote-as 65101
   neighbor MLAG-IPv4-UNDERLAY-PEER next-hop-self
   neighbor MLAG-IPv4-UNDERLAY-PEER password 7 vnEaG8gMeQf3d3cN6PktXQ==
   neighbor MLAG-IPv4-UNDERLAY-PEER send-community
   neighbor MLAG-IPv4-UNDERLAY-PEER maximum-routes 12000
   neighbor 10.255.251.1 peer group MLAG-IPv4-UNDERLAY-PEER
   neighbor 172.31.255.0 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.31.255.2 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.255.1 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.255.2 peer group EVPN-OVERLAY-PEERS
   redistribute connected route-map RM-CONN-2-BGP
   !
   vlan-aware-bundle B-ELAN-201
      rd 192.168.255.3:20201
      route-target both 20201:20201
      redistribute learned
      vlan 201
   !
   vlan-aware-bundle TENANT_A_PROJECT01
      rd 192.168.255.3:11
      route-target both 11:11
      redistribute learned
      vlan 110
   !
   vlan-aware-bundle TENANT_A_PROJECT02
      rd 192.168.255.3:12
      route-target both 12:12
      redistribute learned
      vlan 112
   !
   address-family evpn
      neighbor EVPN-OVERLAY-PEERS activate
      no neighbor IPv4-UNDERLAY-PEERS activate
      no neighbor MLAG-IPv4-UNDERLAY-PEER activate
   !
   address-family ipv4
      no neighbor EVPN-OVERLAY-PEERS activate
      neighbor IPv4-UNDERLAY-PEERS activate
      neighbor MLAG-IPv4-UNDERLAY-PEER activate
   !
   vrf TENANT_A_PROJECT01
      rd 192.168.255.3:11
      route-target import evpn 11:11
      route-target export evpn 11:11
      router-id 192.168.255.3
      neighbor 10.255.251.1 peer group MLAG-IPv4-UNDERLAY-PEER
      redistribute connected
   !
   vrf TENANT_A_PROJECT02
      rd 192.168.255.3:12
      route-target import evpn 12:12
      route-target export evpn 12:12
      router-id 192.168.255.3
      neighbor 10.255.251.1 peer group MLAG-IPv4-UNDERLAY-PEER
      redistribute connected
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
