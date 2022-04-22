# ptp
# Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
  - [PTP](#ptp)
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

## PTP

### PTP Summary

| PTP setting | Value |
| ----------- | ----- |
| Clock-identity | 123.123.123.123 |
| Source IP | 1.1.1.1 |
| Priority1 | 1 |
| Priority2 | 2 |
| TTL | 200 |
| Domain | 1 |
| Msg General | DSCP 4 |
| Msg Event | DSCP 8 |

### PTP Device Configuration

```eos
!
ptp clock-identity 123.123.123.123
ptp source ip 1.1.1.1
ptp priority1 1
ptp priority2 2
ptp ttl 200
ptp domain 1
ptp message-type general dscp 4 default
ptp message-type event dscp 8 default
ptp mode boundary
ptp forward-unicast
ptp monitor threshold offset-from-master 1234
ptp monitor threshold mean-path-delay 4321
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
| Ethernet3 |  P2P_LINK_TO_DC1-SPINE2_Ethernet5 | trunk | 2,14 | - | - | - |
| Ethernet5 | DC1-AGG01_Ethernet1 | *trunk | *110,201 | *- | *- | 5 |

*Inherited from Port-Channel Interface

#### IPv4

| Interface | Description | Type | Channel Group | IP Address | VRF |  MTU | Shutdown | ACL In | ACL Out |
| --------- | ----------- | -----| ------------- | ---------- | ----| ---- | -------- | ------ | ------- |
| Ethernet6 | P2P_LINK_TO_DC1-SPINE1_Ethernet6 | routed | - | 172.31.255.15/31 | default | 1500 | - | - | - |

### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet3
   description P2P_LINK_TO_DC1-SPINE2_Ethernet5
   switchport trunk allowed vlan 2,14
   switchport mode trunk
   switchport
   ptp enable
   ptp sync-message interval 1
   ptp delay-mechanism e2e
   ptp transport layer2
   ptp role dynamic
   ptp vlan 2
!
interface Ethernet5
   description DC1-AGG01_Ethernet1
   channel-group 5 mode active
!
interface Ethernet6
   description P2P_LINK_TO_DC1-SPINE1_Ethernet6
   mtu 1500
   no switchport
   ip address 172.31.255.15/31
   ptp enable
   ptp sync-message interval 1
   ptp delay-mechanism e2e
   ptp announce interval 3
   ptp transport ipv4
   ptp announce timeout 9
   ptp delay-req interval -7
   ptp role dynamic
```

## Port-Channel Interfaces

### Port-Channel Interfaces Summary

#### L2

| Interface | Description | Type | Mode | VLANs | Native VLAN | Trunk Group | LACP Fallback Timeout | LACP Fallback Mode | MLAG ID | EVPN ESI |
| --------- | ----------- | ---- | ---- | ----- | ----------- | ------------| --------------------- | ------------------ | ------- | -------- |
| Port-Channel5 | DC1_L2LEAF1_Po1 | switched | trunk | 110,201 | - | - | - | - | 5 | - |

### Port-Channel Interfaces Device Configuration

```eos
!
interface Port-Channel5
   description DC1_L2LEAF1_Po1
   switchport
   switchport trunk allowed vlan 110,201
   switchport mode trunk
   mlag 5
   ptp enable
   ptp delay-mechanism e2e
   ptp sync-message interval 1
   ptp role dynamic
   ptp vlan 2
   ptp transport layer2
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

# Quality Of Service
