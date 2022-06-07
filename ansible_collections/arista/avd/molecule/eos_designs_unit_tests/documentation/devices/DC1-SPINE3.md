# DC1-SPINE3
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
| Management0 | oob_management | oob | MGMT | 192.168.200.103/24 | 192.168.200.5 |

#### IPv6

| Management Interface | description | Type | VRF | IPv6 Address | IPv6 Gateway |
| -------------------- | ----------- | ---- | --- | ------------ | ------------ |
| Management0 | oob_management | oob | MGMT | -  | - |

### Management Interfaces Device Configuration

```eos
!
interface Management0
   description oob_management
   no shutdown
   vrf MGMT
   ip address 192.168.200.103/24
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
| example@example.com | EOS_DESIGNS_UNIT_TESTS DC1-SPINE3 | All | Disabled |

### SNMP Device Configuration

```eos
!
snmp-server contact example@example.com
snmp-server location EOS_DESIGNS_UNIT_TESTS DC1-SPINE3
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
| Ethernet1 | P2P_LINK_TO_DC1-LEAF1A_Ethernet3 | routed | - | 172.31.255.4/31 | default | 1500 | false | - | - |
| Ethernet2 | P2P_LINK_TO_DC1-LEAF2A_Ethernet3 | routed | - | 172.31.255.20/31 | default | 1500 | false | - | - |
| Ethernet3 | P2P_LINK_TO_DC1-LEAF2B_Ethernet3 | routed | - | 172.31.255.36/31 | default | 1500 | false | - | - |
| Ethernet4 | P2P_LINK_TO_DC1-SVC3A_Ethernet3 | routed | - | 172.31.255.52/31 | default | 1500 | false | - | - |
| Ethernet5 | P2P_LINK_TO_DC1-SVC3B_Ethernet3 | routed | - | 172.31.255.68/31 | default | 1500 | false | - | - |
| Ethernet6 | P2P_LINK_TO_DC1-BL1A_Ethernet3 | routed | - | 172.31.255.84/31 | default | 1500 | false | - | - |
| Ethernet7 | P2P_LINK_TO_DC1-BL1B_Ethernet3 | routed | - | 172.31.255.100/31 | default | 1500 | false | - | - |
| Ethernet8 | P2P_LINK_TO_DC1-BL2A_Ethernet3 | routed | - | 172.31.255.116/31 | default | 1500 | false | - | - |
| Ethernet9 | P2P_LINK_TO_DC1-BL2B_Ethernet3 | routed | - | 172.31.255.132/31 | default | 1500 | false | - | - |
| Ethernet14 | P2P_LINK_TO_DC1-CL1A_Ethernet3 | routed | - | 172.31.255.148/31 | default | 1500 | false | - | - |
| Ethernet15 | P2P_LINK_TO_DC1-CL1B_Ethernet3 | routed | - | 172.31.255.164/31 | default | 1500 | false | - | - |
| Ethernet16 | P2P_LINK_TO_DC1_UNDEPLOYED_LEAF1A_Ethernet3 | routed | - | 172.31.255.196/31 | default | 1500 | true | - | - |
| Ethernet17 | P2P_LINK_TO_DC1_UNDEPLOYED_LEAF1B_Ethernet3 | routed | - | 172.31.255.212/31 | default | 1500 | true | - | - |

### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet1
   description P2P_LINK_TO_DC1-LEAF1A_Ethernet3
   no shutdown
   mtu 1500
   speed forced 100gfull
   no switchport
   ip address 172.31.255.4/31
!
interface Ethernet2
   description P2P_LINK_TO_DC1-LEAF2A_Ethernet3
   no shutdown
   mtu 1500
   speed forced 100gfull
   no switchport
   ip address 172.31.255.20/31
!
interface Ethernet3
   description P2P_LINK_TO_DC1-LEAF2B_Ethernet3
   no shutdown
   mtu 1500
   speed forced 100gfull
   no switchport
   ip address 172.31.255.36/31
!
interface Ethernet4
   description P2P_LINK_TO_DC1-SVC3A_Ethernet3
   no shutdown
   mtu 1500
   speed forced 100gfull
   no switchport
   ip address 172.31.255.52/31
!
interface Ethernet5
   description P2P_LINK_TO_DC1-SVC3B_Ethernet3
   no shutdown
   mtu 1500
   speed forced 100gfull
   no switchport
   ip address 172.31.255.68/31
!
interface Ethernet6
   description P2P_LINK_TO_DC1-BL1A_Ethernet3
   no shutdown
   mtu 1500
   speed forced 100gfull
   no switchport
   ip address 172.31.255.84/31
!
interface Ethernet7
   description P2P_LINK_TO_DC1-BL1B_Ethernet3
   no shutdown
   mtu 1500
   speed forced 100gfull
   no switchport
   ip address 172.31.255.100/31
!
interface Ethernet8
   description P2P_LINK_TO_DC1-BL2A_Ethernet3
   no shutdown
   mtu 1500
   speed forced 100gfull
   no switchport
   ip address 172.31.255.116/31
!
interface Ethernet9
   description P2P_LINK_TO_DC1-BL2B_Ethernet3
   no shutdown
   mtu 1500
   speed forced 100gfull
   no switchport
   ip address 172.31.255.132/31
!
interface Ethernet14
   description P2P_LINK_TO_DC1-CL1A_Ethernet3
   no shutdown
   mtu 1500
   speed forced 100gfull
   no switchport
   ip address 172.31.255.148/31
!
interface Ethernet15
   description P2P_LINK_TO_DC1-CL1B_Ethernet3
   no shutdown
   mtu 1500
   speed forced 100gfull
   no switchport
   ip address 172.31.255.164/31
!
interface Ethernet16
   description P2P_LINK_TO_DC1_UNDEPLOYED_LEAF1A_Ethernet3
   shutdown
   mtu 1500
   speed forced 100gfull
   no switchport
   ip address 172.31.255.196/31
!
interface Ethernet17
   description P2P_LINK_TO_DC1_UNDEPLOYED_LEAF1B_Ethernet3
   shutdown
   mtu 1500
   speed forced 100gfull
   no switchport
   ip address 172.31.255.212/31
```

## Loopback Interfaces

### Loopback Interfaces Summary

#### IPv4

| Interface | Description | VRF | IP Address |
| --------- | ----------- | --- | ---------- |
| Loopback0 | EVPN_Overlay_Peering | default | 192.168.255.3/32 |

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
   ip address 192.168.255.3/32
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
| 65001|  192.168.255.3 |

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
| 172.31.255.5 | 65101 | default | - | Inherited from peer group UNDERLAY-PEERS | Inherited from peer group UNDERLAY-PEERS | - | - | - |
| 172.31.255.21 | 65102 | default | - | Inherited from peer group UNDERLAY-PEERS | Inherited from peer group UNDERLAY-PEERS | - | - | - |
| 172.31.255.37 | 65102 | default | - | Inherited from peer group UNDERLAY-PEERS | Inherited from peer group UNDERLAY-PEERS | - | - | - |
| 172.31.255.53 | 65103 | default | - | Inherited from peer group UNDERLAY-PEERS | Inherited from peer group UNDERLAY-PEERS | - | - | - |
| 172.31.255.69 | 65103 | default | - | Inherited from peer group UNDERLAY-PEERS | Inherited from peer group UNDERLAY-PEERS | - | - | - |
| 172.31.255.85 | 65104 | default | - | Inherited from peer group UNDERLAY-PEERS | Inherited from peer group UNDERLAY-PEERS | - | - | - |
| 172.31.255.101 | 65105 | default | - | Inherited from peer group UNDERLAY-PEERS | Inherited from peer group UNDERLAY-PEERS | - | - | - |
| 172.31.255.117 | 65106 | default | - | Inherited from peer group UNDERLAY-PEERS | Inherited from peer group UNDERLAY-PEERS | - | - | - |
| 172.31.255.133 | 65107 | default | - | Inherited from peer group UNDERLAY-PEERS | Inherited from peer group UNDERLAY-PEERS | - | - | - |
| 172.31.255.149 | 65108 | default | - | Inherited from peer group UNDERLAY-PEERS | Inherited from peer group UNDERLAY-PEERS | - | - | - |
| 172.31.255.165 | 65109 | default | - | Inherited from peer group UNDERLAY-PEERS | Inherited from peer group UNDERLAY-PEERS | - | - | - |
| 172.31.255.197 | 65110 | default | - | Inherited from peer group UNDERLAY-PEERS | Inherited from peer group UNDERLAY-PEERS | - | - | - |
| 172.31.255.213 | 65111 | default | - | Inherited from peer group UNDERLAY-PEERS | Inherited from peer group UNDERLAY-PEERS | - | - | - |
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

### Router BGP EVPN Address Family

#### EVPN Peer Groups

| Peer Group | Activate |
| ---------- | -------- |
| EVPN-OVERLAY-PEERS | True |

### Router BGP Device Configuration

```eos
!
router bgp 65001
   router-id 192.168.255.3
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
   neighbor 172.31.255.5 peer group UNDERLAY-PEERS
   neighbor 172.31.255.5 remote-as 65101
   neighbor 172.31.255.5 description DC1-LEAF1A_Ethernet3
   neighbor 172.31.255.21 peer group UNDERLAY-PEERS
   neighbor 172.31.255.21 remote-as 65102
   neighbor 172.31.255.21 description DC1-LEAF2A_Ethernet3
   neighbor 172.31.255.37 peer group UNDERLAY-PEERS
   neighbor 172.31.255.37 remote-as 65102
   neighbor 172.31.255.37 description DC1-LEAF2B_Ethernet3
   neighbor 172.31.255.53 peer group UNDERLAY-PEERS
   neighbor 172.31.255.53 remote-as 65103
   neighbor 172.31.255.53 description DC1-SVC3A_Ethernet3
   neighbor 172.31.255.69 peer group UNDERLAY-PEERS
   neighbor 172.31.255.69 remote-as 65103
   neighbor 172.31.255.69 description DC1-SVC3B_Ethernet3
   neighbor 172.31.255.85 peer group UNDERLAY-PEERS
   neighbor 172.31.255.85 remote-as 65104
   neighbor 172.31.255.85 description DC1-BL1A_Ethernet3
   neighbor 172.31.255.101 peer group UNDERLAY-PEERS
   neighbor 172.31.255.101 remote-as 65105
   neighbor 172.31.255.101 description DC1-BL1B_Ethernet3
   neighbor 172.31.255.117 peer group UNDERLAY-PEERS
   neighbor 172.31.255.117 remote-as 65106
   neighbor 172.31.255.117 description DC1-BL2A_Ethernet3
   neighbor 172.31.255.133 peer group UNDERLAY-PEERS
   neighbor 172.31.255.133 remote-as 65107
   neighbor 172.31.255.133 description DC1-BL2B_Ethernet3
   neighbor 172.31.255.149 peer group UNDERLAY-PEERS
   neighbor 172.31.255.149 remote-as 65108
   neighbor 172.31.255.149 description DC1-CL1A_Ethernet3
   neighbor 172.31.255.165 peer group UNDERLAY-PEERS
   neighbor 172.31.255.165 remote-as 65109
   neighbor 172.31.255.165 description DC1-CL1B_Ethernet3
   neighbor 172.31.255.197 peer group UNDERLAY-PEERS
   neighbor 172.31.255.197 remote-as 65110
   neighbor 172.31.255.197 description DC1_UNDEPLOYED_LEAF1A_Ethernet3
   neighbor 172.31.255.213 peer group UNDERLAY-PEERS
   neighbor 172.31.255.213 remote-as 65111
   neighbor 172.31.255.213 description DC1_UNDEPLOYED_LEAF1B_Ethernet3
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
