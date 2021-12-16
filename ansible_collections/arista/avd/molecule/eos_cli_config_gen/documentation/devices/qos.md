# qos
# Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [Authentication](#authentication)
- [Monitoring](#monitoring)
- [Internal VLAN Allocation Policy](#internal-vlan-allocation-policy)
  - [Internal VLAN Allocation Policy Summary](#internal-vlan-allocation-policy-summary)
- [Interfaces](#interfaces)
  - [Ethernet Interfaces](#ethernet-interfaces)
  - [Port-Channel Interfaces](#port-channel-interfaces)
- [Routing](#routing)
  - [IP Routing](#ip-routing)
  - [IPv6 Routing](#ipv6-routing)
- [Multicast](#multicast)
- [Filters](#filters)
- [ACL](#acl)
- [Quality Of Service](#quality-of-service)
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

# Authentication

# Monitoring

# Internal VLAN Allocation Policy

## Internal VLAN Allocation Policy Summary

**Default Allocation Policy**

| Policy Allocation | Range Beginning | Range Ending |
| ------------------| --------------- | ------------ |
| ascending | 1006 | 4094 |

# Interfaces

## Ethernet Interfaces

### Ethernet Interfaces Summary

#### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | Channel-Group |
| --------- | ----------- | ---- | ----- | ----------- | ----------- | ------------- |
| Ethernet3 | MLAG_PEER_DC1-LEAF1B_Ethernet3 | *trunk | *2-4094 | *- | *['LEAF_PEER_L3', 'MLAG'] | 3 |
| Ethernet4 | MLAG_PEER_DC1-LEAF1B_Ethernet4 | *trunk | *2-4094 | *- | *['LEAF_PEER_L3', 'MLAG'] | 3 |
| Ethernet6 |  SRV-POD02_Eth1 | trunk | 110-111,210-211 | - | - | - |

*Inherited from Port-Channel Interface

#### IPv4

| Interface | Description | Type | Channel Group | IP Address | VRF |  MTU | Shutdown | ACL In | ACL Out |
| --------- | ----------- | -----| ------------- | ---------- | ----| ---- | -------- | ------ | ------- |
| Ethernet1 | P2P_LINK_TO_DC1-SPINE1_Ethernet1 | routed | - | 172.31.255.1/31 | default | 1500 | - | - | - |

### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet1
   description P2P_LINK_TO_DC1-SPINE1_Ethernet1
   mtu 1500
   no switchport
   qos trust dscp
   qos dscp 48
   ip address 172.31.255.1/31
   service-profile test
!
interface Ethernet3
   description MLAG_PEER_DC1-LEAF1B_Ethernet3
   channel-group 3 mode active
!
interface Ethernet4
   description MLAG_PEER_DC1-LEAF1B_Ethernet4
   channel-group 3 mode active
!
interface Ethernet6
   description SRV-POD02_Eth1
   switchport
   switchport trunk allowed vlan 110-111,210-211
   switchport mode trunk
   qos trust cos
   qos cos 2
   service-profile experiment
```

## Port-Channel Interfaces

### Port-Channel Interfaces Summary

#### L2

| Interface | Description | Type | Mode | VLANs | Native VLAN | Trunk Group | LACP Fallback Timeout | LACP Fallback Mode | MLAG ID | EVPN ESI |
| --------- | ----------- | ---- | ---- | ----- | ----------- | ------------| --------------------- | ------------------ | ------- | -------- |
| Port-Channel3 | MLAG_PEER_DC1-LEAF1B_Po3 | switched | trunk | 2-4094 | - | ['LEAF_PEER_L3', 'MLAG'] | - | - | - | - |

### Port-Channel Interfaces Device Configuration

```eos
!
interface Port-Channel3
   description MLAG_PEER_DC1-LEAF1B_Po3
   switchport
   switchport trunk allowed vlan 2-4094
   switchport mode trunk
   switchport trunk group LEAF_PEER_L3
   switchport trunk group MLAG
   qos trust cos
   qos cos 2
   service-profile experiment
```

# Routing

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

# Multicast

# Filters

# ACL

# Quality Of Service

## QOS

### QOS Summary

QOS rewrite DSCP: **enabled**

#### QOS Mappings


| COS to Traffic Class mappings |
| ----------------------------- |
| 1 2 3 4 to traffic-class 2 |
| 3 to traffic-class 3 |


| DSCP to Traffic Class mappings |
| ------------------------------ |
| 8 9 10 11 12 13 14 15 16 17 19 21 23 24 25 27 29 31 32 33 35 37 39 40 41 42 43 44 45 47 49 50 51 52 53 54 55 57 58 59 60 61 62 63 to traffic-class 1 |
| 18 20 22 26 28 30 34 36 38 to traffic-class 4 drop-precedence 2 |
| 46 to traffic-class 5 |


| Traffic Class to DSCP or COS mappings |
| ------------------------------------- |
| 1 to dscp 56 |
| 2 4 5 to cos 7 |
| 6 to tx-queue 2 |

### QOS Device Configuration

```eos
!
qos rewrite dscp
qos map cos 1 2 3 4 to traffic-class 2
qos map cos 3 to traffic-class 3
qos map dscp 8 9 10 11 12 13 14 15 16 17 19 21 23 24 25 27 29 31 32 33 35 37 39 40 41 42 43 44 45 47 49 50 51 52 53 54 55 57 58 59 60 61 62 63 to traffic-class 1
qos map dscp 18 20 22 26 28 30 34 36 38 to traffic-class 4 drop-precedence 2
qos map dscp 46 to traffic-class 5
qos map traffic-class 1 to dscp 56
qos map traffic-class 2 4 5 to cos 7
qos map traffic-class 6 to tx-queue 2
```

## QOS Profiles

### QOS Profiles Summary


QOS Profile: **experiment**

**Settings**

| Default COS | Default DSCP | Trust | Shape Rate |
| ----------- | ------------ | ----- | ---------- |
| 2 | - | cos | - |

**Tx-queues**

| Tx-queue | Bandwidth | Priority | Shape Rate |
| -------- | --------- | -------- | ---------- |
| 3 | 30 | no priority | - |
| 4 | 10 | - | - |
| 5 | 40 | - | - |
| 7 | 30 | - | 40 percent |

QOS Profile: **no_qos_trust**

**Settings**

| Default COS | Default DSCP | Trust | Shape Rate |
| ----------- | ------------ | ----- | ---------- |
| 3 | 4 | disabled | - |

QOS Profile: **test**

**Settings**

| Default COS | Default DSCP | Trust | Shape Rate |
| ----------- | ------------ | ----- | ---------- |
| - | 46 | dscp | 80 percent |

**Tx-queues**

| Tx-queue | Bandwidth | Priority | Shape Rate |
| -------- | --------- | -------- | ---------- |
| 1 | 50 | no priority | - |
| 2 | 10 | priority strict | - |
| 4 | 10 | - | - |

### QOS Profile Device Configuration

```eos
!
qos profile experiment
   qos trust cos
   qos cos 2
   !
   tx-queue 3
      bandwidth percent 30
      no priority
   !
   tx-queue 4
      bandwidth guaranteed percent 10
   !
   tx-queue 5
      bandwidth percent 40
   !
   tx-queue 7
      bandwidth percent 30
      shape rate 40 percent
!
qos profile no_qos_trust
   no qos trust
   qos cos 3
   qos dscp 4
!
qos profile test
   qos trust dscp
   qos dscp 46
   shape rate 80 percent
   !
   tx-queue 1
      bandwidth percent 50
      no priority
   !
   tx-queue 2
      bandwidth percent 10
      priority strict
   !
   tx-queue 4
      bandwidth guaranteed percent 10
```

### QOS Interfaces

| Interface | Trust | Default DSCP | Default COS | Shape rate |
| --------- | ----- | ------------ | ----------- | ---------- |
| Ethernet1 | dscp | 48 | - | - |
| Ethernet6 | cos | - | 2 | - |
| Port-Channel3 | cos | - | 2 | - |
