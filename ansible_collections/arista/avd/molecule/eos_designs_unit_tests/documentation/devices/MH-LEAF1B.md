# MH-LEAF1B
# Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
  - [Name Servers](#name-servers)
  - [NTP](#ntp)
  - [Management API HTTP](#management-api-http)
- [Authentication](#authentication)
  - [Local Users](#local-users)
- [System Boot Settings](#system-boot-settings)
  - [Boot Secret Summary](#boot-secret-summary)
  - [System Boot Configuration](#system-boot-configuration)
- [Monitoring](#monitoring)
  - [TerminAttr Daemon](#terminattr-daemon)
  - [SNMP](#snmp)
  - [Link Tracking](#link-tracking)
- [LACP](#lacp)
  - [LACP Summary](#lacp-summary)
  - [LACP Device Configuration](#lacp-device-configuration)
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
  - [Route-maps](#route-maps)
- [ACL](#acl)
- [VRF Instances](#vrf-instances)
  - [VRF Instances Summary](#vrf-instances-summary)
  - [VRF Instances Device Configuration](#vrf-instances-device-configuration)
- [Virtual Source NAT](#virtual-source-nat)
  - [Virtual Source NAT Summary](#virtual-source-nat-summary)
  - [Virtual Source NAT Configuration](#virtual-source-nat-configuration)
- [Quality Of Service](#quality-of-service)

# Management

## Management Interfaces

### Management Interfaces Summary

#### IPv4

| Management Interface | description | Type | VRF | IP Address | Gateway |
| -------------------- | ----------- | ---- | --- | ---------- | ------- |
| Management1 | oob_management | oob | MGMT | 192.168.201.105/24 | 192.168.200.5 |

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
   ip address 192.168.201.105/24
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
| False | True | False |

### Management API VRF Access

| VRF Name | IPv4 ACL | IPv6 ACL |
| -------- | -------- | -------- |
| MGMT | - | - |

### Management API HTTP Configuration

```eos
!
management api http-commands
   protocol https
   no default-services
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
username cvpadmin ssh-key ssh-rsa AAAAB3NzaC1yc2EAA82spi2mkxp4FgaLi4CjWkpnL1A/MD7WhrSNgqXToF7QCb9Lidagy9IHafQxfu7LwkFdyQIMu8XNwDZIycuf29wHbDdz1N+YNVK8zwyNAbMOeKMqblsEm2YIorgjzQX1m9+/rJeFBKz77PSgeMp/Rc3txFVuSmFmeTy3aMkU= cvpadmin@hostmachine.local
```

# System Boot Settings

## Boot Secret Summary

- The sha512 hashed Aboot password is configured

## System Boot Configuration

```eos
!
boot secret sha512 a153de6290ff1409257ade45f
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

## SNMP

### SNMP Configuration Summary

| Contact | Location | SNMP Traps | State |
| ------- | -------- | ---------- | ----- |
| example@example.com | EOS_DESIGNS_UNIT_TESTS MH-LEAF1B | All | Disabled |

### SNMP Device Configuration

```eos
!
snmp-server contact example@example.com
snmp-server location EOS_DESIGNS_UNIT_TESTS MH-LEAF1B
```

## Link Tracking

### Link Tracking Groups Summary

| Group Name | Minimum Links | Recovery Delay |
| ---------- | ------------- | -------------- |
| LT_GROUP1 | - | 300 |

### Link Tracking Groups Configuration

```eos
!
link tracking group LT_GROUP1
   recovery delay 300
```

# LACP

## LACP Summary

| Port-id range | Rate-limit default | System-priority |
| ------------- | ------------------ | --------------- |
| 129 - 256 | - | - |

## LACP Device Configuration

```eos
!
lacp port-id range 129 256
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
| 310 | Tenant_X_OP_Zone_1 | - |

## VLANs Device Configuration

```eos
!
vlan 310
   name Tenant_X_OP_Zone_1
```

# Interfaces

## Ethernet Interfaces

### Ethernet Interfaces Summary

#### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | Channel-Group |
| --------- | ----------- | ---- | ----- | ----------- | ----------- | ------------- |
| Ethernet10 | server01_ES1_Eth2 | *access | *310 | *- | *- | 10 |
| Ethernet12 | server03_AUTO_ESI_Eth2 | *access | *310 | *- | *- | 12 |
| Ethernet13 | server04_AUTO_ESI_Profile_Eth2 | *access | *310 | *- | *- | 13 |
| Ethernet14 | server05_AUTO_ESI_Profile_Override_Eth2 | *access | *310 | *- | *- | 14 |
| Ethernet15 | server06_Single_Active_Port_Channel_Eth2 | *trunk | *310 | *- | *- | 15 |
| Ethernet16 | server07_Single_Active_Port_Channel_Manual_DF_Eth2 | *trunk | *310 | *- | *- | 16 |
| Ethernet17 |  server08_Single_Active_Ethernet_Eth2 | trunk | 310 | - | - | - |
| Ethernet18 |  server09_All_Active_Ethernet_Eth2 | trunk | 310 | - | - | - |
| Ethernet19 |  server10_Single_Active_Ethernet_Manual_DF_Eth2 | trunk | 310 | - | - | - |
| Ethernet20 | server11_Single_Active_Port_Channel_Manual_DF_Dont_Preempt_Eth2 | *trunk | *310 | *- | *- | 20 |
| Ethernet21 |  server12_Single_Active_Ethernet_Manual_DF_Dont_Preempt_Eth2 | trunk | 310 | - | - | - |
| Ethernet22 | server13_Single_Active_Port_Channel_Manual_DF_Dont_Preempt_modulus_Eth2 | *trunk | *310 | *- | *- | 22 |
| Ethernet23 |  server14_Single_Active_Ethernet_Manual_DF_Dont_Preempt_modulus_Eth2 | trunk | 310 | - | - | - |

*Inherited from Port-Channel Interface

#### Link Tracking Groups

| Interface | Group Name | Direction |
| --------- | ---------- | --------- |
| Ethernet1 | LT_GROUP1 | upstream |

#### IPv4

| Interface | Description | Type | Channel Group | IP Address | VRF |  MTU | Shutdown | ACL In | ACL Out |
| --------- | ----------- | -----| ------------- | ---------- | ----| ---- | -------- | ------ | ------- |
| Ethernet1 | P2P_LINK_TO_DC1-SPINE1_Ethernet20 | routed | - | 10.10.101.3/31 | default | 1500 | false | - | - |

#### EVPN Multihoming

##### EVPN Multihoming Summary

| Interface | Ethernet Segment Identifier | Multihoming Redundancy Mode | Route Target |
| --------- | --------------------------- | --------------------------- | ------------ |
| Ethernet17 | 0000:0000:213f:36b8:ff71 | single-active | 21:3f:36:b8:ff:71 |
| Ethernet18 | 0000:0000:00dd:00dd:00dd | all-active | 00:dd:00:dd:00:dd |
| Ethernet19 | 0000:0000:885b:86cc:8bac | single-active | 88:5b:86:cc:8b:ac |
| Ethernet21 | 0000:0000:5d0b:68d3:6ff9 | single-active | 5d:0b:68:d3:6f:f9 |
| Ethernet23 | 0000:0000:262b:7df9:c98b | single-active | 26:2b:7d:f9:c9:8b |

##### Designated Forwarder Election Summary

| Interface | Algorithm | Preference Value | Dont Preempt | Hold time | Subsequent Hold Time | Candidate Reachability Required |
| --------- | --------- | ---------------- | ------------ | --------- | -------------------- | ------------------------------- |
| Ethernet17 | preference | 0 | False | - | - | False |
| Ethernet18 | modulus | - | False | - | - | False |
| Ethernet19 | preference | 250 | False | - | - | False |
| Ethernet21 | preference | 250 | True | - | - | False |
| Ethernet23 | modulus | - | False | - | - | False |

### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet1
   description P2P_LINK_TO_DC1-SPINE1_Ethernet20
   no shutdown
   mtu 1500
   no switchport
   ip address 10.10.101.3/31
   link tracking group LT_GROUP1 upstream
!
interface Ethernet10
   description server01_ES1_Eth2
   no shutdown
   channel-group 10 mode active
!
interface Ethernet11
   description ROUTER02_WITH_SUBIF_Eth2
   no shutdown
   channel-group 11 mode active
!
interface Ethernet12
   description server03_AUTO_ESI_Eth2
   no shutdown
   channel-group 12 mode active
!
interface Ethernet13
   description server04_AUTO_ESI_Profile_Eth2
   no shutdown
   channel-group 13 mode active
!
interface Ethernet14
   description server05_AUTO_ESI_Profile_Override_Eth2
   no shutdown
   channel-group 14 mode active
!
interface Ethernet15
   description server06_Single_Active_Port_Channel_Eth2
   no shutdown
   channel-group 15 mode active
!
interface Ethernet16
   description server07_Single_Active_Port_Channel_Manual_DF_Eth2
   no shutdown
   channel-group 16 mode active
!
interface Ethernet17
   description server08_Single_Active_Ethernet_Eth2
   no shutdown
   switchport trunk allowed vlan 310
   switchport mode trunk
   switchport
   evpn ethernet-segment
      identifier 0000:0000:213f:36b8:ff71
      redundancy single-active
      designated-forwarder election algorithm preference 0
      route-target import 21:3f:36:b8:ff:71
!
interface Ethernet18
   description server09_All_Active_Ethernet_Eth2
   no shutdown
   switchport trunk allowed vlan 310
   switchport mode trunk
   switchport
   evpn ethernet-segment
      identifier 0000:0000:00dd:00dd:00dd
      redundancy all-active
      designated-forwarder election algorithm modulus
      route-target import 00:dd:00:dd:00:dd
!
interface Ethernet19
   description server10_Single_Active_Ethernet_Manual_DF_Eth2
   no shutdown
   switchport trunk allowed vlan 310
   switchport mode trunk
   switchport
   evpn ethernet-segment
      identifier 0000:0000:885b:86cc:8bac
      redundancy single-active
      designated-forwarder election algorithm preference 250
      route-target import 88:5b:86:cc:8b:ac
!
interface Ethernet20
   description server11_Single_Active_Port_Channel_Manual_DF_Dont_Preempt_Eth2
   no shutdown
   channel-group 20 mode active
!
interface Ethernet21
   description server12_Single_Active_Ethernet_Manual_DF_Dont_Preempt_Eth2
   no shutdown
   switchport trunk allowed vlan 310
   switchport mode trunk
   switchport
   evpn ethernet-segment
      identifier 0000:0000:5d0b:68d3:6ff9
      redundancy single-active
      designated-forwarder election algorithm preference 250 dont-preempt
      route-target import 5d:0b:68:d3:6f:f9
!
interface Ethernet22
   description server13_Single_Active_Port_Channel_Manual_DF_Dont_Preempt_modulus_Eth2
   no shutdown
   channel-group 22 mode active
!
interface Ethernet23
   description server14_Single_Active_Ethernet_Manual_DF_Dont_Preempt_modulus_Eth2
   no shutdown
   switchport trunk allowed vlan 310
   switchport mode trunk
   switchport
   evpn ethernet-segment
      identifier 0000:0000:262b:7df9:c98b
      redundancy single-active
      designated-forwarder election algorithm modulus
      route-target import 26:2b:7d:f9:c9:8b
```

## Port-Channel Interfaces

### Port-Channel Interfaces Summary

#### L2

| Interface | Description | Type | Mode | VLANs | Native VLAN | Trunk Group | LACP Fallback Timeout | LACP Fallback Mode | MLAG ID | EVPN ESI |
| --------- | ----------- | ---- | ---- | ----- | ----------- | ------------| --------------------- | ------------------ | ------- | -------- |
| Port-Channel10 | server01_ES1_PortChanne1 | switched | access | 310 | - | - | - | - | - | 0000:0000:0001:1010:1010 |
| Port-Channel12 | server03_AUTO_ESI_Auto-ESI PortChannel | switched | access | 310 | - | - | - | - | - | 0000:0000:fc87:ae24:2cb3 |
| Port-Channel13 | server04_AUTO_ESI_Profile_Auto-ESI PortChannel from profile | switched | access | 310 | - | - | - | - | - | 0000:0000:29cc:4043:0a29 |
| Port-Channel14 | server05_AUTO_ESI_Profile_Override_Auto-ESI PortChannel overridden on server | switched | access | 310 | - | - | - | - | - | 0000:0000:010a:010a:010a |
| Port-Channel15 | server06_Single_Active_Port_Channel_Single-Active ESI | switched | trunk | 310 | - | - | - | - | - | 0000:0000:2873:c14b:64ec |
| Port-Channel16 | server07_Single_Active_Port_Channel_Manual_DF_Single-Active ESI with Manual DF | switched | trunk | 310 | - | - | - | - | - | 0000:0000:ec11:73f8:7361 |
| Port-Channel20 | server11_Single_Active_Port_Channel_Manual_DF_Dont_Preempt_Single-Active ESI with Manual DF | switched | trunk | 310 | - | - | - | - | - | 0000:0000:47cb:834e:c0c7 |
| Port-Channel22 | server13_Single_Active_Port_Channel_Manual_DF_Dont_Preempt_modulus_Single-Active ESI with Manual DF | switched | trunk | 310 | - | - | - | - | - | 0000:0000:d716:1795:361e |

#### Flexible Encapsulation Interfaces

| Interface | Description | Type | Vlan ID | Client Unmatched | Client Dot1q VLAN | Client Dot1q Outer Tag | Client Dot1q Inner Tag | Network Retain Client Encapsulation | Network Dot1q VLAN | Network Dot1q Outer Tag | Network Dot1q Inner Tag |
| --------- | ----------- | ---- | ------- | -----------------| ----------------- | ---------------------- | ---------------------- | ----------------------------------- | ------------------ | ----------------------- | ----------------------- |
| Port-Channel11.101 | - | l2dot1q | 101 | False | 101 | - | - | True | - | - | - |
| Port-Channel11.102 | - | l2dot1q | 1102 | False | 2102 | - | - | True | - | - | - |
| Port-Channel11.103 | - | l2dot1q | 1103 | False | 2103 | - | - | True | - | - | - |
| Port-Channel11.104 | - | l2dot1q | 1104 | False | 2104 | - | - | True | - | - | - |

#### EVPN Multihoming

##### EVPN Multihoming Summary

| Interface | Ethernet Segment Identifier | Multihoming Redundancy Mode | Route Target |
| --------- | --------------------------- | --------------------------- | ------------ |
| Port-Channel10 | 0000:0000:0001:1010:1010 | all-active | 00:01:10:10:10:10 |
| Port-Channel11.101 | 0000:0000:0000:0000:0101 | all-active | 00:00:00:00:01:01 |
| Port-Channel11.102 | 0000:0000:0000:0000:0102 | all-active | 00:00:00:00:01:02 |
| Port-Channel11.103 | 0000:0000:c2c9:c85a:ed92 | all-active | c2:c9:c8:5a:ed:92 |
| Port-Channel11.104 | 0000:0000:5c8e:1f50:9fc4 | all-active | 5c:8e:1f:50:9f:c4 |
| Port-Channel12 | 0000:0000:fc87:ae24:2cb3 | all-active | fc:87:ae:24:2c:b3 |
| Port-Channel13 | 0000:0000:29cc:4043:0a29 | all-active | 29:cc:40:43:0a:29 |
| Port-Channel14 | 0000:0000:010a:010a:010a | all-active | 01:0a:01:0a:01:0a |
| Port-Channel15 | 0000:0000:2873:c14b:64ec | single-active | 28:73:c1:4b:64:ec |
| Port-Channel16 | 0000:0000:ec11:73f8:7361 | single-active | ec:11:73:f8:73:61 |
| Port-Channel20 | 0000:0000:47cb:834e:c0c7 | single-active | 47:cb:83:4e:c0:c7 |
| Port-Channel22 | 0000:0000:d716:1795:361e | single-active | d7:16:17:95:36:1e |

##### Designated Forwarder Election Summary

| Interface | Algorithm | Preference Value | Dont Preempt | Hold time | Subsequent Hold Time | Candidate Reachability Required |
| --------- | --------- | ---------------- | ------------ | --------- | -------------------- | ------------------------------- |
| Port-Channel15 | preference | 0 | False | - | - | False |
| Port-Channel16 | preference | 200 | False | - | - | False |
| Port-Channel20 | preference | 0 | True | - | - | False |
| Port-Channel22 | modulus | - | False | - | - | False |

#### Link Tracking Groups

| Interface | Group Name | Direction |
| --------- | ---------- | --------- |
| Port-Channel10 | LT_GROUP1 | downstream |
| Port-Channel12 | LT_GROUP1 | downstream |
| Port-Channel13 | LT_GROUP1 | downstream |
| Port-Channel14 | LT_GROUP1 | downstream |

### Port-Channel Interfaces Device Configuration

```eos
!
interface Port-Channel10
   description server01_ES1_PortChanne1
   no shutdown
   switchport
   switchport access vlan 310
   evpn ethernet-segment
      identifier 0000:0000:0001:1010:1010
      route-target import 00:01:10:10:10:10
   lacp system-id 0001.1010.1010
   link tracking group LT_GROUP1 downstream
!
interface Port-Channel11
   description ROUTER02_WITH_SUBIF_Testing L2 subinterfaces
   no shutdown
   no switchport
!
interface Port-Channel11.101
   vlan id 101
   encapsulation vlan
      client dot1q 101 network client
   evpn ethernet-segment
      identifier 0000:0000:0000:0000:0101
      route-target import 00:00:00:00:01:01
!
interface Port-Channel11.102
   vlan id 1102
   encapsulation vlan
      client dot1q 2102 network client
   evpn ethernet-segment
      identifier 0000:0000:0000:0000:0102
      route-target import 00:00:00:00:01:02
!
interface Port-Channel11.103
   vlan id 1103
   encapsulation vlan
      client dot1q 2103 network client
   evpn ethernet-segment
      identifier 0000:0000:c2c9:c85a:ed92
      route-target import c2:c9:c8:5a:ed:92
!
interface Port-Channel11.104
   vlan id 1104
   encapsulation vlan
      client dot1q 2104 network client
   evpn ethernet-segment
      identifier 0000:0000:5c8e:1f50:9fc4
      route-target import 5c:8e:1f:50:9f:c4
!
interface Port-Channel12
   description server03_AUTO_ESI_Auto-ESI PortChannel
   no shutdown
   switchport
   switchport access vlan 310
   evpn ethernet-segment
      identifier 0000:0000:fc87:ae24:2cb3
      route-target import fc:87:ae:24:2c:b3
   lacp system-id fc87.ae24.2cb3
   link tracking group LT_GROUP1 downstream
!
interface Port-Channel13
   description server04_AUTO_ESI_Profile_Auto-ESI PortChannel from profile
   no shutdown
   switchport
   switchport access vlan 310
   evpn ethernet-segment
      identifier 0000:0000:29cc:4043:0a29
      route-target import 29:cc:40:43:0a:29
   lacp system-id 29cc.4043.0a29
   link tracking group LT_GROUP1 downstream
!
interface Port-Channel14
   description server05_AUTO_ESI_Profile_Override_Auto-ESI PortChannel overridden on server
   no shutdown
   switchport
   switchport access vlan 310
   evpn ethernet-segment
      identifier 0000:0000:010a:010a:010a
      route-target import 01:0a:01:0a:01:0a
   lacp system-id 010a.010a.010a
   link tracking group LT_GROUP1 downstream
!
interface Port-Channel15
   description server06_Single_Active_Port_Channel_Single-Active ESI
   no shutdown
   switchport
   switchport trunk allowed vlan 310
   switchport mode trunk
   evpn ethernet-segment
      identifier 0000:0000:2873:c14b:64ec
      redundancy single-active
      designated-forwarder election algorithm preference 0
      route-target import 28:73:c1:4b:64:ec
   lacp system-id 2873.c14b.64ec
!
interface Port-Channel16
   description server07_Single_Active_Port_Channel_Manual_DF_Single-Active ESI with Manual DF
   no shutdown
   switchport
   switchport trunk allowed vlan 310
   switchport mode trunk
   evpn ethernet-segment
      identifier 0000:0000:ec11:73f8:7361
      redundancy single-active
      designated-forwarder election algorithm preference 200
      route-target import ec:11:73:f8:73:61
   lacp system-id ec11.73f8.7361
!
interface Port-Channel20
   description server11_Single_Active_Port_Channel_Manual_DF_Dont_Preempt_Single-Active ESI with Manual DF
   no shutdown
   switchport
   switchport trunk allowed vlan 310
   switchport mode trunk
   evpn ethernet-segment
      identifier 0000:0000:47cb:834e:c0c7
      redundancy single-active
      designated-forwarder election algorithm preference 0 dont-preempt
      route-target import 47:cb:83:4e:c0:c7
   lacp system-id 47cb.834e.c0c7
!
interface Port-Channel22
   description server13_Single_Active_Port_Channel_Manual_DF_Dont_Preempt_modulus_Single-Active ESI with Manual DF
   no shutdown
   switchport
   switchport trunk allowed vlan 310
   switchport mode trunk
   evpn ethernet-segment
      identifier 0000:0000:d716:1795:361e
      redundancy single-active
      designated-forwarder election algorithm modulus
      route-target import d7:16:17:95:36:1e
   lacp system-id d716.1795.361e
```

## Loopback Interfaces

### Loopback Interfaces Summary

#### IPv4

| Interface | Description | VRF | IP Address |
| --------- | ----------- | --- | ---------- |
| Loopback0 | EVPN_Overlay_Peering | default | 192.168.255.34/32 |
| Loopback1 | VTEP_VXLAN_Tunnel_Source | default | 192.168.254.34/32 |
| Loopback100 | Tenant_X_OP_Zone_VTEP_DIAGNOSTICS | Tenant_X_OP_Zone | 10.255.1.34/32 |

#### IPv6

| Interface | Description | VRF | IPv6 Address |
| --------- | ----------- | --- | ------------ |
| Loopback0 | EVPN_Overlay_Peering | default | - |
| Loopback1 | VTEP_VXLAN_Tunnel_Source | default | - |
| Loopback100 | Tenant_X_OP_Zone_VTEP_DIAGNOSTICS | Tenant_X_OP_Zone | - |


### Loopback Interfaces Device Configuration

```eos
!
interface Loopback0
   description EVPN_Overlay_Peering
   no shutdown
   ip address 192.168.255.34/32
!
interface Loopback1
   description VTEP_VXLAN_Tunnel_Source
   no shutdown
   ip address 192.168.254.34/32
!
interface Loopback100
   description Tenant_X_OP_Zone_VTEP_DIAGNOSTICS
   no shutdown
   vrf Tenant_X_OP_Zone
   ip address 10.255.1.34/32
```

## VLAN Interfaces

### VLAN Interfaces Summary

| Interface | Description | VRF |  MTU | Shutdown |
| --------- | ----------- | --- | ---- | -------- |
| Vlan310 | Tenant_X_OP_Zone_1 | Tenant_X_OP_Zone | - | false |

#### IPv4

| Interface | VRF | IP Address | IP Address Virtual | IP Router Virtual Address | VRRP | ACL In | ACL Out |
| --------- | --- | ---------- | ------------------ | ------------------------- | ---- | ------ | ------- |
| Vlan310 |  Tenant_X_OP_Zone  |  -  |  10.1.10.1/24  |  -  |  -  |  -  |  -  |

### VLAN Interfaces Device Configuration

```eos
!
interface Vlan310
   description Tenant_X_OP_Zone_1
   no shutdown
   vrf Tenant_X_OP_Zone
   ip address virtual 10.1.10.1/24
```

## VXLAN Interface

### VXLAN Interface Summary

| Setting | Value |
| ------- | ----- |
| Source Interface | Loopback1 |
| UDP port | 4789 |

#### VLAN to VNI, Flood List and Multicast Group Mappings

| VLAN | VNI | Flood List | Multicast Group |
| ---- | --- | ---------- | --------------- |
| 310 | 11310 | - | - |

#### VRF to VNI and Multicast Group Mappings

| VRF | VNI | Multicast Group |
| ---- | --- | --------------- |
| Tenant_X_OP_Zone | 20 | - |

### VXLAN Interface Device Configuration

```eos
!
interface Vxlan1
   description MH-LEAF1B_VTEP
   vxlan source-interface Loopback1
   vxlan udp-port 4789
   vxlan vlan 310 vni 11310
   vxlan vrf Tenant_X_OP_Zone vni 20
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

#### Virtual Router MAC Address: 00:1c:73:00:dc:01

### Virtual Router MAC Address Configuration

```eos
!
ip virtual-router mac-address 00:1c:73:00:dc:01
```

## IP Routing

### IP Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | true |
| MGMT | false |
| Tenant_X_OP_Zone | true |

### IP Routing Device Configuration

```eos
!
ip routing
no ip routing vrf MGMT
ip routing vrf Tenant_X_OP_Zone
```
## IPv6 Routing

### IPv6 Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | false |
| MGMT | false |
| Tenant_X_OP_Zone | false |

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
| 65152|  192.168.255.34 |

| BGP Tuning |
| ---------- |
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

#### UNDERLAY-PEERS

| Settings | Value |
| -------- | ----- |
| Address Family | ipv4 |
| Send community | all |
| Maximum routes | 12000 |

### BGP Neighbors

| Neighbor | Remote AS | VRF | Shutdown | Send-community | Maximum-routes | Allowas-in | BFD | RIB Pre-Policy Retain |
| -------- | --------- | --- | -------- | -------------- | -------------- | ---------- | --- | --------------------- |
| 10.10.101.2 | 65001 | default | - | Inherited from peer group UNDERLAY-PEERS | Inherited from peer group UNDERLAY-PEERS | - | - | - |
| 192.168.255.1 | 65001 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - |

### Router BGP EVPN Address Family

#### EVPN Peer Groups

| Peer Group | Activate |
| ---------- | -------- |
| EVPN-OVERLAY-PEERS | True |

#### EVPN Host Flapping Settings

| State | Window | Threshold | Expiry Timeout |
| ----- | ------ | --------- | -------------- |
| Enabled | 180 Seconds | 5 | 10 Seconds |

### Router BGP VLAN Aware Bundles

| VLAN Aware Bundle | Route-Distinguisher | Both Route-Target | Import Route Target | Export Route-Target | Redistribute | VLANs |
| ----------------- | ------------------- | ----------------- | ------------------- | ------------------- | ------------ | ----- |
| Tenant_X_OP_Zone | 192.168.255.34:20 | 20:20 | - | - | learned | 310 |

### Router BGP VRFs

| VRF | Route-Distinguisher | Redistribute |
| --- | ------------------- | ------------ |
| Tenant_X_OP_Zone | 192.168.255.34:20 | connected |

### Router BGP Device Configuration

```eos
!
router bgp 65152
   router-id 192.168.255.34
   maximum-paths 4 ecmp 4
   neighbor EVPN-OVERLAY-PEERS peer group
   neighbor EVPN-OVERLAY-PEERS update-source Loopback0
   neighbor EVPN-OVERLAY-PEERS bfd
   neighbor EVPN-OVERLAY-PEERS ebgp-multihop 3
   neighbor EVPN-OVERLAY-PEERS password 7 q+VNViP5i4rVjW1cxFv2wA==
   neighbor EVPN-OVERLAY-PEERS send-community
   neighbor EVPN-OVERLAY-PEERS maximum-routes 0
   neighbor UNDERLAY-PEERS peer group
   neighbor UNDERLAY-PEERS password 7 AQQvKeimxJu+uGQ/yYvv9w==
   neighbor UNDERLAY-PEERS send-community
   neighbor UNDERLAY-PEERS maximum-routes 12000
   neighbor 10.10.101.2 peer group UNDERLAY-PEERS
   neighbor 10.10.101.2 remote-as 65001
   neighbor 10.10.101.2 description DC1-SPINE1_Ethernet20
   neighbor 192.168.255.1 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.255.1 remote-as 65001
   neighbor 192.168.255.1 description DC1-SPINE1
   redistribute connected route-map RM-CONN-2-BGP
   !
   vlan-aware-bundle Tenant_X_OP_Zone
      rd 192.168.255.34:20
      route-target both 20:20
      redistribute learned
      vlan 310
   !
   address-family evpn
      host-flap detection window 180 threshold 5 expiry timeout 10 seconds
      neighbor EVPN-OVERLAY-PEERS activate
   !
   address-family ipv4
      no neighbor EVPN-OVERLAY-PEERS activate
      neighbor UNDERLAY-PEERS activate
   !
   vrf Tenant_X_OP_Zone
      rd 192.168.255.34:20
      route-target import evpn 20:20
      route-target export evpn 20:20
      router-id 192.168.255.34
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

### IP IGMP Snooping Device Configuration

```eos
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

# ACL

# VRF Instances

## VRF Instances Summary

| VRF Name | IP Routing |
| -------- | ---------- |
| MGMT | disabled |
| Tenant_X_OP_Zone | enabled |

## VRF Instances Device Configuration

```eos
!
vrf instance MGMT
!
vrf instance Tenant_X_OP_Zone
```

# Virtual Source NAT

## Virtual Source NAT Summary

| Source NAT VRF | Source NAT IP Address |
| -------------- | --------------------- |
| Tenant_X_OP_Zone | 10.255.1.34 |

## Virtual Source NAT Configuration

```eos
!
ip address virtual source-nat vrf Tenant_X_OP_Zone address 10.255.1.34
```

# Quality Of Service
