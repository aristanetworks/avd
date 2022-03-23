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
  - [Extended Access-lists](#extended-access-lists)
  - [IPv6 Extended Access-lists](#ipv6-extended-access-lists)
- [Quality Of Service](#quality-of-service)
  - [QOS](#qos)
  - [QOS Class Maps](#qos-class-maps)
  - [QOS Policy Maps](#qos-policy-maps)
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
| Ethernet7 |  Test-with-policymap | trunk | 110-111,210-211 | - | - | - |

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
   ip address 172.31.255.1/31
   qos trust dscp
   qos dscp 48
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
   switchport trunk allowed vlan 110-111,210-211
   switchport mode trunk
   switchport
   qos trust cos
   qos cos 2
   service-profile experiment
!
interface Ethernet7
   description Test-with-policymap
   switchport trunk allowed vlan 110-111,210-211
   switchport mode trunk
   switchport
   service-profile qprof_testwithpolicy
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
| default | false |

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

## Extended Access-lists

### Extended Access-lists Summary

#### acl_qos_tc0_v4

| Sequence | Action |
| -------- | ------ |
| 10 | permit ip any 192.0.2.0/29 |

#### acl_qos_tc5_v4

| Sequence | Action |
| -------- | ------ |
| 10 | permit ip any any dscp ef |

### Extended Access-lists Device Configuration

```eos
!
ip access-list acl_qos_tc0_v4
   10 permit ip any 192.0.2.0/29
!
ip access-list acl_qos_tc5_v4
   10 permit ip any any dscp ef
```

## IPv6 Extended Access-lists

### IPv6 Extended Access-lists Summary

#### acl_qos_tc0_v6

| Sequence | Action |
| -------- | ------ |
| 10 | permit ipv6 any any dscp cs1 |

#### acl_qos_tc5_v6

| Sequence | Action |
| -------- | ------ |
| 10 | permit ipv6 any 2001:db8::/48 |

### IPv6 Extended Access-lists Device Configuration

```eos
!
ipv6 access-list acl_qos_tc0_v6
   10 permit ipv6 any any dscp cs1
!
ipv6 access-list acl_qos_tc5_v6
   10 permit ipv6 any 2001:db8::/48
```

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

## QOS Class Maps

### QOS Class Maps Summary

| Name | Field | Value |
| ---- | ----- | ----- |
| cmap_tc0_v4 | acl | acl_qos_tc0_v4 |
| cmap_tc0_v6 | - | - |
| cmap_tc5_v4 | acl | acl_qos_tc5_v4 |
| cmap_tc5_v6 | - | - |

### Class-maps Device Configuration

```eos
!
class-map type qos match-any cmap_tc0_v4
   match ip access-group acl_qos_tc0_v4
!
class-map type qos match-any cmap_tc0_v6
   match ipv6 access-group acl_qos_tc0_v6
!
class-map type qos match-any cmap_tc5_v4
   match ip access-group acl_qos_tc5_v4
!
class-map type qos match-any cmap_tc5_v6
   match ipv6 access-group acl_qos_tc5_v6
```

## QOS Policy Maps

### QOS Policy Maps Summary

**pmap_test1**

| class | Set | Value |
| ----- | --- | ----- |
| cmap_tc0_v4 | traffic_class | 0 |
| cmap_tc5_v4 | traffic_class | 5 |
| cmap_tc5_v6 | traffic_class | 5 |
| cmap_tc0_v6 | traffic_class | 0 |
| class-default | traffic_class | 1 |

### QOS Policy Maps configuration

```eos
!
policy-map type quality-of-service pmap_test1
   class cmap_tc0_v4
      set traffic-class 0
   !
   class cmap_tc5_v4
      set traffic-class 5
   !
   class cmap_tc5_v6
      set traffic-class 5
   !
   class cmap_tc0_v6
      set traffic-class 0
   !
   class class-default
      set traffic-class 1
```

## QOS Profiles

### QOS Profiles Summary


QOS Profile: **experiment**

**Settings**

| Default COS | Default DSCP | Trust | Shape Rate | QOS Service Policy |
| ----------- | ------------ | ----- | ---------- | ------------------ |
| 2 | - | cos | - | test_qos_policy_v1 |

**TX Queues**

| TX queue | Type | Bandwidth | Priority | Shape Rate |
| -------- | ---- | --------- | -------- | ---------- |
| 3 | All | 30 | no priority | - |
| 4 | All | 10 | - | - |
| 5 | All | 40 | - | - |
| 7 | All | 30 | - | 40 percent |

QOS Profile: **no_qos_trust**

**Settings**

| Default COS | Default DSCP | Trust | Shape Rate | QOS Service Policy |
| ----------- | ------------ | ----- | ---------- | ------------------ |
| 3 | 4 | disabled | - | - |

QOS Profile: **qprof_testwithpolicy**

**Settings**

| Default COS | Default DSCP | Trust | Shape Rate | QOS Service Policy |
| ----------- | ------------ | ----- | ---------- | ------------------ |
| - | - | - | - | pmap_test1 |

**TX Queues**

| TX queue | Type | Bandwidth | Priority | Shape Rate |
| -------- | ---- | --------- | -------- | ---------- |
| 0 | All | 1 | - | - |
| 1 | All | 80 | - | - |
| 5 | All | 19 | no priority | - |

QOS Profile: **test**

**Settings**

| Default COS | Default DSCP | Trust | Shape Rate | QOS Service Policy |
| ----------- | ------------ | ----- | ---------- | ------------------ |
| - | 46 | dscp | 80 percent | - |

**TX Queues**

| TX queue | Type | Bandwidth | Priority | Shape Rate |
| -------- | ---- | --------- | -------- | ---------- |
| 1 | All | 50 | no priority | - |
| 2 | All | 10 | priority strict | - |
| 4 | All | 10 | - | - |

QOS Profile: **uc_mc_queues_test**

**Settings**

| Default COS | Default DSCP | Trust | Shape Rate | QOS Service Policy |
| ----------- | ------------ | ----- | ---------- | ------------------ |
| - | - | - | - | - |

**TX Queues**

| TX queue | Type | Bandwidth | Priority | Shape Rate |
| -------- | ---- | --------- | -------- | ---------- |
| 1 | Unicast | 50 | no priority | - |
| 2 | Unicast | 10 | priority strict | - |
| 4 | Unicast | 10 | - | - |
| 1 | Multicast | 50 | no priority | - |
| 2 | Multicast | 10 | priority strict | - |
| 4 | Multicast | 10 | - | - |

### QOS Profile Device Configuration

```eos
!
qos profile experiment
   qos trust cos
   qos cos 2
   service-policy type qos input test_qos_policy_v1
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
qos profile qprof_testwithpolicy
   service-policy type qos input pmap_test1
   !
   tx-queue 0
      bandwidth percent 1
   !
   tx-queue 1
      bandwidth percent 80
   !
   tx-queue 5
      bandwidth percent 19
      no priority
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
!
qos profile uc_mc_queues_test
   !
   uc-tx-queue 1
      bandwidth percent 50
      no priority
   !
   uc-tx-queue 2
      bandwidth percent 10
      priority strict
   !
   uc-tx-queue 4
      bandwidth guaranteed percent 10
   !
   mc-tx-queue 1
      bandwidth percent 50
      no priority
   !
   mc-tx-queue 2
      bandwidth percent 10
      priority strict
   !
   mc-tx-queue 4
      bandwidth guaranteed percent 10
```

### QOS Interfaces

| Interface | Trust | Default DSCP | Default COS | Shape rate |
| --------- | ----- | ------------ | ----------- | ---------- |
| Ethernet1 | dscp | 48 | - | - |
| Ethernet6 | cos | - | 2 | - |
| Port-Channel3 | cos | - | 2 | - |
