# traffic-policies

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
- [Traffic Policies](#traffic-policies)
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

Static routes not defined

## IPv6 Static Routes

IPv6 static routes not defined

## ARP

Global ARP timeout not defined.

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

# Errdisable

Errdisable is not defined.

# Traffic Policies

### Traffic Policies information
**IPv4 Field sets**

| Field Set Name | Values |
| -------------- | ------ |
| DEMO-01 | 10.0.0.0/8<br/>192.168.0.0/16| | DEMO-02 | 172.16.0.0/12<br/>224.0.0.0/8| 
**IPv6 Field sets**

No IPv6 field-set configured.

**L4 Port Field sets**

| Field Set Name | Values |
| -------------- | ------ |
| SERVICE-DEMO | 10,20,80,440-450 | 
#### Traffic Policies
**BLUE-C1-POLICY:**

| Match set | Type | Sources | Destinations | Protocol | Action |
| --------- | ---- | ------- | ------------ | -------- | ------ |
 | BLUE-C1-POLICY-01 | ipv4 | 10.0.0.0/8<br/>192.168.0.0/16  | DEMO-01 |  tcp  (src: 1,10-20 )<br/> icmp <br/>|  traffic-class: 5<br/> action: pass |
 | BLUE-C1-POLICY-02 | ipv4 | DEMO-01<br/>DEMO-02  |  |  tcp  (dst: SERVICE-DEMO / flags: established)<br/> icmp <br/>|  counter: DEMO-TRAFFIC<br/>dscp code: 60<br/> action: pass |
 | BLUE-C1-POLICY-03 | ipv4 | DEMO-01  |  |  tcp <br/>|  counter: DROP-PACKETS<br/>logging: enabled<br/> action: drop<br/> |
 | BLUE-C1-POLICY-04 | ipv4 | DEMO-02  | DEMO-01 |  tcp  (src: 22 / flags: established)<br/> icmp <br/>|  traffic-class: 5<br/> action: pass |

**BLUE-C2-POLICY:**

| Match set | Type | Sources | Destinations | Protocol | Action |
| --------- | ---- | ------- | ------------ | -------- | ------ |
 | BLUE-C2-POLICY-01 | ipv4 | 10.0.0.0/8<br/>192.168.0.0/16  |  |  tcp  (src: 1,10-20 )<br/> icmp <br/>|  traffic-class: 5<br/> action: pass |
 | BLUE-C2-POLICY-02 | ipv4 | DEMO-01<br/>DEMO-02  |  |  tcp  (dst: SERVICE-DEMO )<br/> icmp <br/>|  counter: DEMO-TRAFFIC<br/>dscp code: 60<br/> action: pass |
 | BLUE-C2-POLICY-03 | ipv4 | DEMO-01  |  |  tcp <br/>|  logging: enabled<br/> action: drop<br/> |

### Traffic Policies Device Configuration

```eos
!
traffic-policies
   field-set ipv4 prefix DEMO-01
      10.0.0.0/8 192.168.0.0/16
   !
   field-set ipv4 prefix DEMO-02
      172.16.0.0/12 224.0.0.0/8
   !
   field-set l4-port SERVICE-DEMO
      10,20,80,440-450
   !
   traffic-policy BLUE-C1-POLICY
      counter DEMO-TRAFFIC DROP-PACKETS
      match BLUE-C1-POLICY-01 ipv4
         source prefix 10.0.0.0/8 192.168.0.0/16
         destination prefix field-set DEMO-01
         protocol tcp source port 1,10-20
         protocol icmp
         actions
            set traffic class 5
         !
      !
      match BLUE-C1-POLICY-02 ipv4
         source prefix field-set DEMO-01 DEMO-02
         protocol tcp flags established destination port field-set SERVICE-DEMO
         protocol icmp
         actions
            count DEMO-TRAFFIC
            set dscp 60
         !
      !
      match BLUE-C1-POLICY-03 ipv4
         source prefix field-set DEMO-01
         protocol tcp
         actions
            count DROP-PACKETS
            drop
            log
         !
      !
      match BLUE-C1-POLICY-04 ipv4
         source prefix field-set DEMO-02
         destination prefix field-set DEMO-01
         protocol tcp flags established source port 22
         protocol icmp
         actions
            set traffic class 5
         !
      !
   !
   traffic-policy BLUE-C2-POLICY
      counter DEMO-TRAFFIC
      match BLUE-C2-POLICY-01 ipv4
         source prefix 10.0.0.0/8 192.168.0.0/16
         protocol tcp source port 1,10-20
         protocol icmp
         actions
            set traffic class 5
         !
      !
      match BLUE-C2-POLICY-02 ipv4
         source prefix field-set DEMO-01 DEMO-02
         protocol tcp source port field-set SERVICE-DEMO
         protocol icmp
         actions
            count DEMO-TRAFFIC
            set dscp 60
         !
      !
      match BLUE-C2-POLICY-03 ipv4
         source prefix field-set DEMO-01
         protocol tcp
         actions
            drop
            log
         !
      !
   !
```

# MACsec

MACsec not defined

# QOS

QOS is not defined.

# QOS Profiles

QOS Profiles are not defined

# Custom Templates

No custom templates defined
