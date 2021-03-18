# tcam-profile

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
  - [Enable Password](#enable-password)
  - [TACACS Servers](#tacacs-servers)
  - [IP TACACS Source Interfaces](#ip-tacacs-source-interfaces)
  - [RADIUS Servers](#radius-servers)
  - [AAA Server Groups](#aaa-server-groups)
  - [AAA Authentication](#aaa-authentication)
  - [AAA Authorization](#aaa-authorization)
  - [AAA Accounting](#aaa-accounting)
- [Management Security](#management-security)
- [Prompt](#prompt)
- [Aliases](#aliases)
- [Monitoring](#monitoring)
  - [TerminAttr Daemon](#terminattr-daemon)
  - [Logging](#logging)
  - [SNMP](#snmp)
  - [SFlow](#sflow)
  - [Hardware Counters](#hardware-counters)
  - [VM Tracer Sessions](#vm-tracer-sessions)
  - [Event Handler](#event-handler)
- [Hardware TCAM Profile](#hardware-tcam-profile)
- [MLAG](#mlag)
- [Spanning Tree](#spanning-tree)
- [Internal VLAN Allocation Policy](#internal-vlan-allocation-policy)
- [VLANs](#vlans)
- [Interfaces](#interfaces)
  - [Switchport Default](#switchport-default)
  - [Interface Defaults](#interface-defaults)
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
  - [Router General](#router-general)
  - [Router OSPF](#router-ospf)
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

| Management Interface | description | Type | VRF | IP Address | Gateway |
| -------------------- | ----------- | ---- | --- | ---------- | ------- |
| Management1 | oob_management | oob | MGMT | 10.73.255.122/24 | 10.73.255.2 |

#### IPv6

| Management Interface | description | Type | VRF | IPv6 Address | IPv6 Gateway |
| -------------------- | ----------- | ---- | --- | ------------ | ------------ |
| Management1 | oob_management | oob | MGMT | -  | - |

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

## Enable Password

Enable password not defined

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

# Prompt

Prompt not defined

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

# Hardware TCAM Profile


TCAM profile __`traffic_policy`__ is active

## Custom TCAM profiles

Following TCAM profiles are configured on device:

- Profile Name: `traffic_policy`

## Hardware TCAM configuration

```eos
!
hardware tcam
   profile traffic_policy
      feature acl port mac
          sequence 55
          key size limit 160
          key field dst-mac ether-type src-mac
          action count drop
          packet ipv4 forwarding bridged
          packet ipv4 forwarding routed
          packet ipv4 forwarding routed multicast
          packet ipv4 mpls ipv4 forwarding mpls decap
          packet ipv4 mpls ipv6 forwarding mpls decap
          packet ipv4 non-vxlan forwarding routed decap
          packet ipv4 vxlan forwarding bridged decap
          packet ipv6 forwarding bridged
          packet ipv6 forwarding routed
          packet ipv6 forwarding routed decap
          packet ipv6 forwarding routed multicast
          packet ipv6 ipv6 forwarding routed decap
          packet mpls forwarding bridged decap
          packet mpls ipv4 forwarding mpls
          packet mpls ipv6 forwarding mpls
          packet mpls non-ip forwarding mpls
          packet non-ip forwarding bridged
      !
      feature forwarding-destination mpls
          sequence 100
      !
      feature mirror ip
          sequence 80
          key size limit 160
          key field dscp dst-ip ip-frag ip-protocol l4-dst-port l4-ops l4-src-port src-ip tcp-control
          action count mirror set-policer
          packet ipv4 forwarding bridged
          packet ipv4 forwarding routed
          packet ipv4 forwarding routed multicast
          packet ipv4 non-vxlan forwarding routed decap
      !
      feature mpls
          sequence 5
          key size limit 160
          action drop redirect set-ecn
          packet ipv4 mpls ipv4 forwarding mpls decap
          packet ipv4 mpls ipv6 forwarding mpls decap
          packet mpls ipv4 forwarding mpls
          packet mpls ipv6 forwarding mpls
          packet mpls non-ip forwarding mpls
      !
      feature pbr ip
          sequence 60
          key size limit 160
          key field dscp dst-ip ip-frag ip-protocol l4-dst-port l4-ops-18b l4-src-port src-ip tcp-control
          action count redirect
          packet ipv4 forwarding routed
          packet ipv4 mpls ipv4 forwarding mpls decap
          packet ipv4 mpls ipv6 forwarding mpls decap
          packet ipv4 non-vxlan forwarding routed decap
          packet ipv4 vxlan forwarding bridged decap
      !
      feature pbr ipv6
          sequence 30
          key field dst-ipv6 ipv6-next-header l4-dst-port l4-src-port src-ipv6-high src-ipv6-low tcp-control
          action count redirect
          packet ipv6 forwarding routed
      !
      feature pbr mpls
          sequence 65
          key size limit 160
          key field mpls-inner-ip-tos
          action count drop redirect
          packet mpls ipv4 forwarding mpls
          packet mpls ipv6 forwarding mpls
          packet mpls non-ip forwarding mpls
      !
      feature qos ip
          sequence 75
          key size limit 160
          key field dscp dst-ip ip-frag ip-protocol l4-dst-port l4-ops l4-src-port src-ip tcp-control
          action set-dscp set-policer set-tc
          packet ipv4 forwarding routed
          packet ipv4 forwarding routed multicast
          packet ipv4 mpls ipv4 forwarding mpls decap
          packet ipv4 mpls ipv6 forwarding mpls decap
          packet ipv4 non-vxlan forwarding routed decap
      !
      feature qos ipv6
          sequence 70
          key field dst-ipv6 ipv6-next-header ipv6-traffic-class l4-dst-port l4-src-port src-ipv6-high src-ipv6-low
          action set-dscp set-policer set-tc
          packet ipv6 forwarding routed
      !
      feature traffic-policy port ipv4
          sequence 45
          key size limit 160
          key field dscp dst-ip-label icmp-type-code ip-frag ip-fragment-offset ip-length ip-protocol l4-dst-port l4-src-port src-ip-label tcp-control ttl
          action count drop log set-dscp set-tc
          packet ipv4 forwarding routed
      !
      feature traffic-policy port ipv6
          sequence 25
          key field dst-ipv6-label hop-limit icmp-type-code ipv6-length ipv6-next-header ipv6-traffic-class l4-dst-port l4-src-port src-ipv6-label tcp-control
          action count drop log set-dscp set-tc
          packet ipv6 forwarding routed
      !
      feature tunnel vxlan
          sequence 50
          key size limit 160
          packet ipv4 vxlan eth ipv4 forwarding routed decap
          packet ipv4 vxlan forwarding bridged decap
   !
   system profile traffic_policy
```

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

## Switchport Default

No switchport default defined

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

## Router General

Router general not defined

## Router OSPF

Router OSPF not defined

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

# MACsec

MACsec not defined

# QOS

QOS is not defined.

# QOS Profiles

QOS Profiles are not defined

# Custom Templates

No custom templates defined
