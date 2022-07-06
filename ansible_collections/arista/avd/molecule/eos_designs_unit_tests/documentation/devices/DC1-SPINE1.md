# DC1-SPINE1
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
- [Spanning Tree](#spanning-tree)
  - [Spanning Tree Summary](#spanning-tree-summary)
  - [Spanning Tree Device Configuration](#spanning-tree-device-configuration)
- [Internal VLAN Allocation Policy](#internal-vlan-allocation-policy)
  - [Internal VLAN Allocation Policy Summary](#internal-vlan-allocation-policy-summary)
  - [Internal VLAN Allocation Policy Configuration](#internal-vlan-allocation-policy-configuration)
- [Interfaces](#interfaces)
  - [Ethernet Interfaces](#ethernet-interfaces)
  - [Loopback Interfaces](#loopback-interfaces)
- [Routing](#routing)
  - [Service Routing Protocols Model](#service-routing-protocols-model)
  - [IP Routing](#ip-routing)
  - [IPv6 Routing](#ipv6-routing)
  - [Static Routes](#static-routes)
  - [Router BGP](#router-bgp)
- [BFD](#bfd)
  - [Router BFD](#router-bfd)
- [Multicast](#multicast)
- [Filters](#filters)
  - [Prefix-lists](#prefix-lists)
  - [Route-maps](#route-maps)
- [ACL](#acl)
- [VRF Instances](#vrf-instances)
  - [VRF Instances Summary](#vrf-instances-summary)
  - [VRF Instances Device Configuration](#vrf-instances-device-configuration)
- [Quality Of Service](#quality-of-service)

# Management

## Management Interfaces

### Management Interfaces Summary

#### IPv4

| Management Interface | description | Type | VRF | IP Address | Gateway |
| -------------------- | ----------- | ---- | --- | ---------- | ------- |
| Management1 | oob_management | oob | MGMT | 192.168.200.101/24 | 192.168.200.5 |

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
   ip address 192.168.200.101/24
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
| example@example.com | EOS_DESIGNS_UNIT_TESTS DC1-SPINE1 | All | Disabled |

### SNMP Device Configuration

```eos
!
snmp-server contact example@example.com
snmp-server location EOS_DESIGNS_UNIT_TESTS DC1-SPINE1
```

# Spanning Tree

## Spanning Tree Summary

STP mode: **none**

## Spanning Tree Device Configuration

```eos
!
spanning-tree mode none
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

# Interfaces

## Ethernet Interfaces

### Ethernet Interfaces Summary

#### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | Channel-Group |
| --------- | ----------- | ---- | ----- | ----------- | ----------- | ------------- |

*Inherited from Port-Channel Interface

#### IPv4

| Interface | Description | Type | Channel Group | IP Address | VRF |  MTU | Shutdown | ACL In | ACL Out |
| --------- | ----------- | -----| ------------- | ---------- | ----| ---- | -------- | ------ | ------- |
| Ethernet1/1 | P2P_LINK_TO_DC1-LEAF1A_Ethernet27 | routed | - | 172.31.254.0/31 | default | 1500 | false | - | - |
| Ethernet3/1 | P2P_LINK_TO_DC1-LEAF2A_Ethernet49/1 | routed | - | 172.31.254.32/31 | default | 1500 | false | - | - |
| Ethernet4/1 | P2P_LINK_TO_DC1-LEAF2A_Ethernet52/1 | routed | - | 172.31.254.38/31 | default | 1500 | false | - | - |
| Ethernet5/1 | P2P_LINK_TO_DC1-LEAF2B_Ethernet49/1 | routed | - | 172.31.254.64/31 | default | 1500 | false | - | - |
| Ethernet6/1 | P2P_LINK_TO_DC1-LEAF2B_Ethernet52/1 | routed | - | 172.31.254.70/31 | default | 1500 | false | - | - |
| Ethernet7/1 | P2P_LINK_TO_DC1-SVC3A_Ethernet49/1 | routed | - | 172.31.254.96/31 | default | 1500 | false | - | - |
| Ethernet9/1 | P2P_LINK_TO_DC1-SVC3B_Ethernet49/1 | routed | - | 172.31.254.128/31 | default | 1500 | false | - | - |
| Ethernet18 | P2P_LINK_TO_MLAG-OSPF-L3LEAF1B_Ethernet1 | routed | - | 10.10.101.8/31 | default | 1500 | false | - | - |
| Ethernet19 | P2P_LINK_TO_MH-LEAF1A_Ethernet1 | routed | - | 10.10.101.0/31 | default | 1500 | false | - | - |
| Ethernet20 | P2P_LINK_TO_MH-LEAF1B_Ethernet1 | routed | - | 10.10.101.2/31 | default | 1500 | false | - | - |
| Ethernet21 | P2P_LINK_TO_MH-LEAF2A_Ethernet1 | routed | - | 10.10.101.4/31 | default | 1500 | false | - | - |
| Ethernet22 | P2P_LINK_TO_DC1-BL1A_Ethernet1 | routed | - | 172.31.254.160/31 | default | 1500 | false | - | - |
| Ethernet23 | P2P_LINK_TO_DC1-BL1B_Ethernet1 | routed | - | 172.31.254.192/31 | default | 1500 | false | - | - |
| Ethernet24 | P2P_LINK_TO_DC1-BL2A_Ethernet1 | routed | - | 172.31.254.224/31 | default | 1500 | false | - | - |
| Ethernet25 | P2P_LINK_TO_DC1-BL2B_Ethernet1 | routed | - | 172.31.255.0/31 | default | 1500 | false | - | - |
| Ethernet26 | P2P_LINK_TO_DC1-CL1A_Ethernet1 | routed | - | 172.31.255.32/31 | default | 1500 | false | - | - |
| Ethernet27 | P2P_LINK_TO_DC1-CL1B_Ethernet1 | routed | - | 172.31.255.64/31 | default | 1500 | false | - | - |
| Ethernet28 | P2P_LINK_TO_DC1_UNDEPLOYED_LEAF1A_Ethernet49/1 | routed | - | 172.31.255.128/31 | default | 1500 | true | - | - |
| Ethernet29 | P2P_LINK_TO_DC1_UNDEPLOYED_LEAF1B_Ethernet49/1 | routed | - | 172.31.255.160/31 | default | 1500 | true | - | - |

### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet1/1
   description P2P_LINK_TO_DC1-LEAF1A_Ethernet27
   no shutdown
   mtu 1500
   speed forced 100gfull
   no switchport
   ip address 172.31.254.0/31
!
interface Ethernet3/1
   description P2P_LINK_TO_DC1-LEAF2A_Ethernet49/1
   no shutdown
   mtu 1500
   speed forced 100gfull
   no switchport
   ip address 172.31.254.32/31
!
interface Ethernet4/1
   description P2P_LINK_TO_DC1-LEAF2A_Ethernet52/1
   no shutdown
   mtu 1500
   speed forced 100gfull
   no switchport
   ip address 172.31.254.38/31
!
interface Ethernet5/1
   description P2P_LINK_TO_DC1-LEAF2B_Ethernet49/1
   no shutdown
   mtu 1500
   speed forced 100gfull
   no switchport
   ip address 172.31.254.64/31
!
interface Ethernet6/1
   description P2P_LINK_TO_DC1-LEAF2B_Ethernet52/1
   no shutdown
   mtu 1500
   speed forced 100gfull
   no switchport
   ip address 172.31.254.70/31
!
interface Ethernet7/1
   description P2P_LINK_TO_DC1-SVC3A_Ethernet49/1
   no shutdown
   mtu 1500
   speed forced 100gfull
   no switchport
   ip address 172.31.254.96/31
!
interface Ethernet9/1
   description P2P_LINK_TO_DC1-SVC3B_Ethernet49/1
   no shutdown
   mtu 1500
   speed forced 100gfull
   no switchport
   ip address 172.31.254.128/31
!
interface Ethernet18
   description P2P_LINK_TO_MLAG-OSPF-L3LEAF1B_Ethernet1
   no shutdown
   mtu 1500
   no switchport
   ip address 10.10.101.8/31
!
interface Ethernet19
   description P2P_LINK_TO_MH-LEAF1A_Ethernet1
   no shutdown
   mtu 1500
   no switchport
   ip address 10.10.101.0/31
!
interface Ethernet20
   description P2P_LINK_TO_MH-LEAF1B_Ethernet1
   no shutdown
   mtu 1500
   no switchport
   ip address 10.10.101.2/31
!
interface Ethernet21
   description P2P_LINK_TO_MH-LEAF2A_Ethernet1
   no shutdown
   mtu 1500
   no switchport
   ip address 10.10.101.4/31
!
interface Ethernet22
   description P2P_LINK_TO_DC1-BL1A_Ethernet1
   no shutdown
   mtu 1500
   speed forced 100gfull
   no switchport
   ip address 172.31.254.160/31
!
interface Ethernet23
   description P2P_LINK_TO_DC1-BL1B_Ethernet1
   no shutdown
   mtu 1500
   speed forced 100gfull
   no switchport
   ip address 172.31.254.192/31
!
interface Ethernet24
   description P2P_LINK_TO_DC1-BL2A_Ethernet1
   no shutdown
   mtu 1500
   speed forced 100gfull
   no switchport
   ip address 172.31.254.224/31
!
interface Ethernet25
   description P2P_LINK_TO_DC1-BL2B_Ethernet1
   no shutdown
   mtu 1500
   speed forced 100gfull
   no switchport
   ip address 172.31.255.0/31
!
interface Ethernet26
   description P2P_LINK_TO_DC1-CL1A_Ethernet1
   no shutdown
   mtu 1500
   speed forced 100gfull
   no switchport
   ip address 172.31.255.32/31
!
interface Ethernet27
   description P2P_LINK_TO_DC1-CL1B_Ethernet1
   no shutdown
   mtu 1500
   speed forced 100gfull
   no switchport
   ip address 172.31.255.64/31
!
interface Ethernet28
   description P2P_LINK_TO_DC1_UNDEPLOYED_LEAF1A_Ethernet49/1
   shutdown
   mtu 1500
   speed forced 100gfull
   no switchport
   ip address 172.31.255.128/31
!
interface Ethernet29
   description P2P_LINK_TO_DC1_UNDEPLOYED_LEAF1B_Ethernet49/1
   shutdown
   mtu 1500
   speed forced 100gfull
   no switchport
   ip address 172.31.255.160/31
```

## Loopback Interfaces

### Loopback Interfaces Summary

#### IPv4

| Interface | Description | VRF | IP Address |
| --------- | ----------- | --- | ---------- |
| Loopback0 | EVPN_Overlay_Peering | default | 192.168.255.1/32 |

#### IPv6

| Interface | Description | VRF | IPv6 Address |
| --------- | ----------- | --- | ------------ |
| Loopback0 | EVPN_Overlay_Peering | default | - |


### Loopback Interfaces Device Configuration

```eos
!
interface Loopback0
   description EVPN_Overlay_Peering
   no shutdown
   ip address 192.168.255.1/32
```

# Routing
## Service Routing Protocols Model

Multi agent routing protocol model enabled

```eos
!
service routing protocols model multi-agent
```

## IP Routing

### IP Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | true |
| MGMT | false |

### IP Routing Device Configuration

```eos
!
ip routing
no ip routing vrf MGMT
```
## IPv6 Routing

### IPv6 Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | false |
| MGMT | false |

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
| 65001|  192.168.255.1 |

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
| Next-hop unchanged | True |
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
| 10.10.101.1 | 65151 | default | - | Inherited from peer group UNDERLAY-PEERS | Inherited from peer group UNDERLAY-PEERS | - | - | - |
| 10.10.101.3 | 65152 | default | - | Inherited from peer group UNDERLAY-PEERS | Inherited from peer group UNDERLAY-PEERS | - | - | - |
| 10.10.101.5 | 65153 | default | - | Inherited from peer group UNDERLAY-PEERS | Inherited from peer group UNDERLAY-PEERS | - | - | - |
| 10.10.101.7 | 65161 | default | - | Inherited from peer group UNDERLAY-PEERS | Inherited from peer group UNDERLAY-PEERS | - | - | - |
| 10.10.101.9 | 65161 | default | - | Inherited from peer group UNDERLAY-PEERS | Inherited from peer group UNDERLAY-PEERS | - | - | - |
| 172.31.254.1 | 65101 | default | - | Inherited from peer group UNDERLAY-PEERS | Inherited from peer group UNDERLAY-PEERS | - | - | - |
| 172.31.254.33 | 65102 | default | - | Inherited from peer group UNDERLAY-PEERS | Inherited from peer group UNDERLAY-PEERS | - | - | - |
| 172.31.254.39 | 65102 | default | - | Inherited from peer group UNDERLAY-PEERS | Inherited from peer group UNDERLAY-PEERS | - | - | - |
| 172.31.254.65 | 65102 | default | - | Inherited from peer group UNDERLAY-PEERS | Inherited from peer group UNDERLAY-PEERS | - | - | - |
| 172.31.254.71 | 65102 | default | - | Inherited from peer group UNDERLAY-PEERS | Inherited from peer group UNDERLAY-PEERS | - | - | - |
| 172.31.254.97 | 65103 | default | - | Inherited from peer group UNDERLAY-PEERS | Inherited from peer group UNDERLAY-PEERS | - | - | - |
| 172.31.254.129 | 65103 | default | - | Inherited from peer group UNDERLAY-PEERS | Inherited from peer group UNDERLAY-PEERS | - | - | - |
| 172.31.254.161 | 65104 | default | - | Inherited from peer group UNDERLAY-PEERS | Inherited from peer group UNDERLAY-PEERS | - | - | - |
| 172.31.254.193 | 65105 | default | - | Inherited from peer group UNDERLAY-PEERS | Inherited from peer group UNDERLAY-PEERS | - | - | - |
| 172.31.254.225 | 65106 | default | - | Inherited from peer group UNDERLAY-PEERS | Inherited from peer group UNDERLAY-PEERS | - | - | - |
| 172.31.255.1 | 65107 | default | - | Inherited from peer group UNDERLAY-PEERS | Inherited from peer group UNDERLAY-PEERS | - | - | - |
| 172.31.255.33 | 65108 | default | - | Inherited from peer group UNDERLAY-PEERS | Inherited from peer group UNDERLAY-PEERS | - | - | - |
| 172.31.255.65 | 65109 | default | - | Inherited from peer group UNDERLAY-PEERS | Inherited from peer group UNDERLAY-PEERS | - | - | - |
| 172.31.255.129 | 65110 | default | - | Inherited from peer group UNDERLAY-PEERS | Inherited from peer group UNDERLAY-PEERS | - | - | - |
| 172.31.255.161 | 65111 | default | - | Inherited from peer group UNDERLAY-PEERS | Inherited from peer group UNDERLAY-PEERS | - | - | - |
| 192.168.255.9 | 65101 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - |
| 192.168.255.10 | 65102 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - |
| 192.168.255.11 | 65102 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - |
| 192.168.255.12 | 65103 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - |
| 192.168.255.13 | 65103 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - |
| 192.168.255.14 | 65104 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - |
| 192.168.255.15 | 65105 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - |
| 192.168.255.16 | 65106 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - |
| 192.168.255.17 | 65107 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - |
| 192.168.255.18 | 65108 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - |
| 192.168.255.19 | 65109 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - |
| 192.168.255.21 | 65110 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - |
| 192.168.255.22 | 65111 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - |
| 192.168.255.33 | 65151 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - |
| 192.168.255.34 | 65152 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - |
| 192.168.255.35 | 65153 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - |
| 192.168.255.36 | 65161 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - |
| 192.168.255.37 | 65161 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - |

### Router BGP EVPN Address Family

#### EVPN Peer Groups

| Peer Group | Activate |
| ---------- | -------- |
| EVPN-OVERLAY-PEERS | True |

### Router BGP Device Configuration

```eos
!
router bgp 65001
   router-id 192.168.255.1
   no bgp default ipv4-unicast
   distance bgp 20 200 200
   maximum-paths 4 ecmp 4
   neighbor EVPN-OVERLAY-PEERS peer group
   neighbor EVPN-OVERLAY-PEERS next-hop-unchanged
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
   neighbor 10.10.101.1 peer group UNDERLAY-PEERS
   neighbor 10.10.101.1 remote-as 65151
   neighbor 10.10.101.1 description MH-LEAF1A_Ethernet1
   neighbor 10.10.101.3 peer group UNDERLAY-PEERS
   neighbor 10.10.101.3 remote-as 65152
   neighbor 10.10.101.3 description MH-LEAF1B_Ethernet1
   neighbor 10.10.101.5 peer group UNDERLAY-PEERS
   neighbor 10.10.101.5 remote-as 65153
   neighbor 10.10.101.5 description MH-LEAF2A_Ethernet1
   neighbor 10.10.101.7 peer group UNDERLAY-PEERS
   neighbor 10.10.101.7 remote-as 65161
   neighbor 10.10.101.7 description MLAG-OSPF-L3LEAF1A_Ethernet1
   neighbor 10.10.101.9 peer group UNDERLAY-PEERS
   neighbor 10.10.101.9 remote-as 65161
   neighbor 10.10.101.9 description MLAG-OSPF-L3LEAF1B_Ethernet1
   neighbor 172.31.254.1 peer group UNDERLAY-PEERS
   neighbor 172.31.254.1 remote-as 65101
   neighbor 172.31.254.1 description DC1-LEAF1A_Ethernet27
   neighbor 172.31.254.33 peer group UNDERLAY-PEERS
   neighbor 172.31.254.33 remote-as 65102
   neighbor 172.31.254.33 description DC1-LEAF2A_Ethernet49/1
   neighbor 172.31.254.39 peer group UNDERLAY-PEERS
   neighbor 172.31.254.39 remote-as 65102
   neighbor 172.31.254.39 description DC1-LEAF2A_Ethernet52/1
   neighbor 172.31.254.65 peer group UNDERLAY-PEERS
   neighbor 172.31.254.65 remote-as 65102
   neighbor 172.31.254.65 description DC1-LEAF2B_Ethernet49/1
   neighbor 172.31.254.71 peer group UNDERLAY-PEERS
   neighbor 172.31.254.71 remote-as 65102
   neighbor 172.31.254.71 description DC1-LEAF2B_Ethernet52/1
   neighbor 172.31.254.97 peer group UNDERLAY-PEERS
   neighbor 172.31.254.97 remote-as 65103
   neighbor 172.31.254.97 description DC1-SVC3A_Ethernet49/1
   neighbor 172.31.254.129 peer group UNDERLAY-PEERS
   neighbor 172.31.254.129 remote-as 65103
   neighbor 172.31.254.129 description DC1-SVC3B_Ethernet49/1
   neighbor 172.31.254.161 peer group UNDERLAY-PEERS
   neighbor 172.31.254.161 remote-as 65104
   neighbor 172.31.254.161 description DC1-BL1A_Ethernet1
   neighbor 172.31.254.193 peer group UNDERLAY-PEERS
   neighbor 172.31.254.193 remote-as 65105
   neighbor 172.31.254.193 description DC1-BL1B_Ethernet1
   neighbor 172.31.254.225 peer group UNDERLAY-PEERS
   neighbor 172.31.254.225 remote-as 65106
   neighbor 172.31.254.225 description DC1-BL2A_Ethernet1
   neighbor 172.31.255.1 peer group UNDERLAY-PEERS
   neighbor 172.31.255.1 remote-as 65107
   neighbor 172.31.255.1 description DC1-BL2B_Ethernet1
   neighbor 172.31.255.33 peer group UNDERLAY-PEERS
   neighbor 172.31.255.33 remote-as 65108
   neighbor 172.31.255.33 description DC1-CL1A_Ethernet1
   neighbor 172.31.255.65 peer group UNDERLAY-PEERS
   neighbor 172.31.255.65 remote-as 65109
   neighbor 172.31.255.65 description DC1-CL1B_Ethernet1
   neighbor 172.31.255.129 peer group UNDERLAY-PEERS
   neighbor 172.31.255.129 remote-as 65110
   neighbor 172.31.255.129 description DC1_UNDEPLOYED_LEAF1A_Ethernet49/1
   neighbor 172.31.255.161 peer group UNDERLAY-PEERS
   neighbor 172.31.255.161 remote-as 65111
   neighbor 172.31.255.161 description DC1_UNDEPLOYED_LEAF1B_Ethernet49/1
   neighbor 192.168.255.9 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.255.9 remote-as 65101
   neighbor 192.168.255.9 description DC1-LEAF1A
   neighbor 192.168.255.10 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.255.10 remote-as 65102
   neighbor 192.168.255.10 description DC1-LEAF2A
   neighbor 192.168.255.11 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.255.11 remote-as 65102
   neighbor 192.168.255.11 description DC1-LEAF2B
   neighbor 192.168.255.12 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.255.12 remote-as 65103
   neighbor 192.168.255.12 description DC1-SVC3A
   neighbor 192.168.255.13 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.255.13 remote-as 65103
   neighbor 192.168.255.13 description DC1-SVC3B
   neighbor 192.168.255.14 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.255.14 remote-as 65104
   neighbor 192.168.255.14 description DC1-BL1A
   neighbor 192.168.255.15 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.255.15 remote-as 65105
   neighbor 192.168.255.15 description DC1-BL1B
   neighbor 192.168.255.16 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.255.16 remote-as 65106
   neighbor 192.168.255.16 description DC1-BL2A
   neighbor 192.168.255.17 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.255.17 remote-as 65107
   neighbor 192.168.255.17 description DC1-BL2B
   neighbor 192.168.255.18 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.255.18 remote-as 65108
   neighbor 192.168.255.18 description DC1-CL1A
   neighbor 192.168.255.19 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.255.19 remote-as 65109
   neighbor 192.168.255.19 description DC1-CL1B
   neighbor 192.168.255.21 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.255.21 remote-as 65110
   neighbor 192.168.255.21 description DC1_UNDEPLOYED_LEAF1A
   neighbor 192.168.255.22 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.255.22 remote-as 65111
   neighbor 192.168.255.22 description DC1_UNDEPLOYED_LEAF1B
   neighbor 192.168.255.33 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.255.33 remote-as 65151
   neighbor 192.168.255.33 description MH-LEAF1A
   neighbor 192.168.255.34 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.255.34 remote-as 65152
   neighbor 192.168.255.34 description MH-LEAF1B
   neighbor 192.168.255.35 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.255.35 remote-as 65153
   neighbor 192.168.255.35 description MH-LEAF2A
   neighbor 192.168.255.36 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.255.36 remote-as 65161
   neighbor 192.168.255.36 description MLAG-OSPF-L3LEAF1A
   neighbor 192.168.255.37 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.255.37 remote-as 65161
   neighbor 192.168.255.37 description MLAG-OSPF-L3LEAF1B
   redistribute connected route-map RM-CONN-2-BGP
   !
   address-family evpn
      neighbor EVPN-OVERLAY-PEERS activate
   !
   address-family ipv4
      no neighbor EVPN-OVERLAY-PEERS activate
      neighbor UNDERLAY-PEERS activate
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

# Filters

## Prefix-lists

### Prefix-lists Summary

#### PL-LOOPBACKS-EVPN-OVERLAY

| Sequence | Action |
| -------- | ------ |
| 10 | permit 192.168.255.0/24 eq 32 |

### Prefix-lists Device Configuration

```eos
!
ip prefix-list PL-LOOPBACKS-EVPN-OVERLAY
   seq 10 permit 192.168.255.0/24 eq 32
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

## VRF Instances Device Configuration

```eos
!
vrf instance MGMT
```

# Quality Of Service
