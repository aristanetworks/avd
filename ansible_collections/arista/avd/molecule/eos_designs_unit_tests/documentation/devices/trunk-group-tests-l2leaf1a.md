# trunk-group-tests-l2leaf1a
# Table of Contents

- [Management](#management)
  - [Management API HTTP](#management-api-http)
- [Authentication](#authentication)
- [Monitoring](#monitoring)
- [MLAG](#mlag)
  - [MLAG Summary](#mlag-summary)
  - [MLAG Device Configuration](#mlag-device-configuration)
- [Spanning Tree](#spanning-tree)
  - [Spanning Tree Summary](#spanning-tree-summary)
  - [Spanning Tree Device Configuration](#spanning-tree-device-configuration)
- [Internal VLAN Allocation Policy](#internal-vlan-allocation-policy)
  - [Internal VLAN Allocation Policy Summary](#internal-vlan-allocation-policy-summary)
  - [Internal VLAN Allocation Policy Configuration](#internal-vlan-allocation-policy-configuration)
- [VLANs](#vlans)
  - [VLANs Summary](#vlans-summary)
  - [VLANs Device Configuration](#vlans-device-configuration)
- [Interfaces](#interfaces)
  - [Ethernet Interfaces](#ethernet-interfaces)
  - [Port-Channel Interfaces](#port-channel-interfaces)
  - [VLAN Interfaces](#vlan-interfaces)
- [Routing](#routing)
  - [Service Routing Protocols Model](#service-routing-protocols-model)
  - [IP Routing](#ip-routing)
  - [IPv6 Routing](#ipv6-routing)
  - [Static Routes](#static-routes)
- [Multicast](#multicast)
  - [IP IGMP Snooping](#ip-igmp-snooping)
- [Filters](#filters)
- [ACL](#acl)
- [VRF Instances](#vrf-instances)
  - [VRF Instances Summary](#vrf-instances-summary)
  - [VRF Instances Device Configuration](#vrf-instances-device-configuration)
- [Quality Of Service](#quality-of-service)

# Management

## Management API HTTP

### Management API HTTP Summary

| HTTP | HTTPS | Default Services |
| ---- | ----- | ---------------- |
| False | True | - |

### Management API VRF Access

| VRF Name | IPv4 ACL | IPv6 ACL |
| -------- | -------- | -------- |
| MGMT | - | - |

### Management API HTTP Configuration

```eos
!
management api http-commands
   protocol https
   no shutdown
   !
   vrf MGMT
      no shutdown
```

# Authentication

# Monitoring

# MLAG

## MLAG Summary

| Domain-id | Local-interface | Peer-address | Peer-link |
| --------- | --------------- | ------------ | --------- |
| TRUNK_GROUP_TESTS_L2LEAF1 | Vlan4094 | 10.255.248.1 | Port-Channel3 |

Dual primary detection is disabled.

## MLAG Device Configuration

```eos
!
mlag configuration
   domain-id TRUNK_GROUP_TESTS_L2LEAF1
   local-interface Vlan4094
   peer-address 10.255.248.1
   peer-link Port-Channel3
   reload-delay mlag 300
   reload-delay non-mlag 330
```

# Spanning Tree

## Spanning Tree Summary

STP mode: **mstp**

### Global Spanning-Tree Settings

- Spanning Tree disabled for VLANs: **4094**

## Spanning Tree Device Configuration

```eos
!
no spanning-tree vlan-id 4094
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
| 100 | svi100_with_trunk_groups | TG_100 TG_NOT_MATCHING_ANY_SERVERS MLAG UPLINK |
| 110 | l2vlan110_with_trunk_groups | TG_100 TG_NOT_MATCHING_ANY_SERVERS MLAG UPLINK |
| 200 | svi200_with_trunk_groups | TG_200 TG_NOT_MATCHING_ANY_SERVERS MLAG UPLINK |
| 210 | l2vlan210_with_trunk_groups | TG_200 TG_NOT_MATCHING_ANY_SERVERS MLAG UPLINK |
| 300 | svi300_with_trunk_groups | TG_300 TG_NOT_MATCHING_ANY_SERVERS MLAG UPLINK |
| 310 | l2vlan310_with_trunk_groups | TG_300 TG_NOT_MATCHING_ANY_SERVERS MLAG UPLINK |
| 398 | svi398_without_trunk_groups | MLAG UPLINK |
| 399 | l2vlan399_without_trunk_groups | MLAG UPLINK |
| 4094 | MLAG_PEER | MLAG |

## VLANs Device Configuration

```eos
!
vlan 100
   name svi100_with_trunk_groups
   trunk group MLAG
   trunk group TG_100
   trunk group TG_NOT_MATCHING_ANY_SERVERS
   trunk group UPLINK
!
vlan 110
   name l2vlan110_with_trunk_groups
   trunk group MLAG
   trunk group TG_100
   trunk group TG_NOT_MATCHING_ANY_SERVERS
   trunk group UPLINK
!
vlan 200
   name svi200_with_trunk_groups
   trunk group MLAG
   trunk group TG_200
   trunk group TG_NOT_MATCHING_ANY_SERVERS
   trunk group UPLINK
!
vlan 210
   name l2vlan210_with_trunk_groups
   trunk group MLAG
   trunk group TG_200
   trunk group TG_NOT_MATCHING_ANY_SERVERS
   trunk group UPLINK
!
vlan 300
   name svi300_with_trunk_groups
   trunk group MLAG
   trunk group TG_300
   trunk group TG_NOT_MATCHING_ANY_SERVERS
   trunk group UPLINK
!
vlan 310
   name l2vlan310_with_trunk_groups
   trunk group MLAG
   trunk group TG_300
   trunk group TG_NOT_MATCHING_ANY_SERVERS
   trunk group UPLINK
!
vlan 398
   name svi398_without_trunk_groups
   trunk group MLAG
   trunk group UPLINK
!
vlan 399
   name l2vlan399_without_trunk_groups
   trunk group MLAG
   trunk group UPLINK
!
vlan 4094
   name MLAG_PEER
   trunk group MLAG
```

# Interfaces

## Ethernet Interfaces

### Ethernet Interfaces Summary

#### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | Channel-Group |
| --------- | ----------- | ---- | ----- | ----------- | ----------- | ------------- |
| Ethernet1 | TRUNK-GROUP-TESTS-L3LEAF1A_Ethernet1 | *trunk | *- | *- | *['UPLINK'] | 1 |
| Ethernet2 | TRUNK-GROUP-TESTS-L3LEAF1B_Ethernet1 | *trunk | *- | *- | *['UPLINK'] | 1 |
| Ethernet3 | MLAG_PEER_trunk-group-tests-l2leaf1b_Ethernet3 | *trunk | *2-4094 | *- | *['MLAG'] | 3 |
| Ethernet4 | MLAG_PEER_trunk-group-tests-l2leaf1b_Ethernet4 | *trunk | *2-4094 | *- | *['MLAG'] | 3 |
| Ethernet13 | server_with_tg_300_Nic3 | *trunk | *- | *- | *['TG_300', 'TG_NOT_MATCHING_ANY_VLANS'] | 13 |

*Inherited from Port-Channel Interface

### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet1
   description TRUNK-GROUP-TESTS-L3LEAF1A_Ethernet1
   no shutdown
   channel-group 1 mode active
!
interface Ethernet2
   description TRUNK-GROUP-TESTS-L3LEAF1B_Ethernet1
   no shutdown
   channel-group 1 mode active
!
interface Ethernet3
   description MLAG_PEER_trunk-group-tests-l2leaf1b_Ethernet3
   no shutdown
   channel-group 3 mode active
!
interface Ethernet4
   description MLAG_PEER_trunk-group-tests-l2leaf1b_Ethernet4
   no shutdown
   channel-group 3 mode active
!
interface Ethernet13
   description server_with_tg_300_Nic3
   no shutdown
   channel-group 13 mode active
```

## Port-Channel Interfaces

### Port-Channel Interfaces Summary

#### L2

| Interface | Description | Type | Mode | VLANs | Native VLAN | Trunk Group | LACP Fallback Timeout | LACP Fallback Mode | MLAG ID | EVPN ESI |
| --------- | ----------- | ---- | ---- | ----- | ----------- | ------------| --------------------- | ------------------ | ------- | -------- |
| Port-Channel1 | TRUNK_GROUP_TESTS_L3LEAF1_Po1 | switched | trunk | - | - | ['UPLINK'] | - | - | 1 | - |
| Port-Channel3 | MLAG_PEER_trunk-group-tests-l2leaf1b_Po3 | switched | trunk | 2-4094 | - | ['MLAG'] | - | - | - | - |
| Port-Channel13 | server_with_tg_300_portchannel | switched | trunk | - | - | ['TG_300', 'TG_NOT_MATCHING_ANY_VLANS'] | - | - | 13 | - |

### Port-Channel Interfaces Device Configuration

```eos
!
interface Port-Channel1
   description TRUNK_GROUP_TESTS_L3LEAF1_Po1
   no shutdown
   switchport
   switchport mode trunk
   switchport trunk group UPLINK
   mlag 1
!
interface Port-Channel3
   description MLAG_PEER_trunk-group-tests-l2leaf1b_Po3
   no shutdown
   switchport
   switchport trunk allowed vlan 2-4094
   switchport mode trunk
   switchport trunk group MLAG
!
interface Port-Channel13
   description server_with_tg_300_portchannel
   no shutdown
   switchport
   switchport mode trunk
   switchport trunk group TG_300
   switchport trunk group TG_NOT_MATCHING_ANY_VLANS
   mlag 13
```

## VLAN Interfaces

### VLAN Interfaces Summary

| Interface | Description | VRF |  MTU | Shutdown |
| --------- | ----------- | --- | ---- | -------- |
| Vlan4094 | MLAG_PEER | default | 9000 | false |

#### IPv4

| Interface | VRF | IP Address | IP Address Virtual | IP Router Virtual Address | VRRP | ACL In | ACL Out |
| --------- | --- | ---------- | ------------------ | ------------------------- | ---- | ------ | ------- |
| Vlan4094 |  default  |  10.255.248.0/31  |  -  |  -  |  -  |  -  |  -  |

### VLAN Interfaces Device Configuration

```eos
!
interface Vlan4094
   description MLAG_PEER
   no shutdown
   mtu 9000
   no autostate
   ip address 10.255.248.0/31
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
| MGMT | 0.0.0.0/0 | 1.1.1.1 | - | 1 | - | - | - |

### Static Routes Device Configuration

```eos
!
ip route vrf MGMT 0.0.0.0/0 1.1.1.1
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
