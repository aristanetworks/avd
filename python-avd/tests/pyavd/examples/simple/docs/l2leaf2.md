# l2leaf2

## Table of Contents

<!-- toc -->
<!-- toc -->

## Authentication

### Enable Password

Enable password has been disabled

## Internal VLAN Allocation Policy

### Internal VLAN Allocation Policy Summary

| Policy Allocation | Range Beginning | Range Ending |
| ----------------- | --------------- | ------------ |
| ascending | 1006 | 1199 |

### Internal VLAN Allocation Policy Device Configuration

```eos
!
vlan internal order ascending range 1006 1199
```

## VLANs

### VLANs Summary

| VLAN ID | Name | Trunk Groups |
| ------- | ---- | ------------ |
| 101 | VLAN101 | - |
| 102 | VLAN102 | - |

### VLANs Device Configuration

```eos
!
vlan 101
   name VLAN101
!
vlan 102
   name VLAN102
```

## Interfaces

### Ethernet Interfaces

#### Ethernet Interfaces Summary

##### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | Channel-Group |
| --------- | ----------- | ---- | ----- | ----------- | ----------- | ------------- |
| Ethernet1 | User port | trunk | 100-200,222,456,999-3000 | - | - | - |
| Ethernet2 | User port | trunk | 100-200,222,456,999-3000 | - | - | - |
| Ethernet2/1 | L2_l3leaf2_Ethernet2/3 | *trunk | *101-102 | *- | *- | 21 |
| Ethernet2/2 | L2_l3leaf1_Ethernet2/4 | *trunk | *101-102 | *- | *- | 21 |
| Ethernet3 | User port | trunk | 100-200,222,456,999-3000 | - | - | - |
| Ethernet4 | User port | trunk | 100-200,222,456,999-3000 | - | - | - |
| Ethernet5 | User port | trunk | 100-200,222,456,999-3000 | - | - | - |
| Ethernet6 | User port | trunk | 100-200,222,456,999-3000 | - | - | - |
| Ethernet7 | User port | trunk | 100-200,222,456,999-3000 | - | - | - |
| Ethernet8 | User port | trunk | 100-200,222,456,999-3000 | - | - | - |
| Ethernet9 | User port | trunk | 100-200,222,456,999-3000 | - | - | - |
| Ethernet10 | User port | trunk | 100-200,222,456,999-3000 | - | - | - |
| Ethernet11 | User port | trunk | 100-200,222,456,999-3000 | - | - | - |
| Ethernet12 | User port | trunk | 100-200,222,456,999-3000 | - | - | - |
| Ethernet13 | User port | trunk | 100-200,222,456,999-3000 | - | - | - |
| Ethernet14 | User port | trunk | 100-200,222,456,999-3000 | - | - | - |
| Ethernet15 | User port | trunk | 100-200,222,456,999-3000 | - | - | - |
| Ethernet16 | User port | trunk | 100-200,222,456,999-3000 | - | - | - |
| Ethernet17 | User port | trunk | 100-200,222,456,999-3000 | - | - | - |
| Ethernet18 | User port | trunk | 100-200,222,456,999-3000 | - | - | - |
| Ethernet19 | User port | trunk | 100-200,222,456,999-3000 | - | - | - |
| Ethernet20 | User port | trunk | 100-200,222,456,999-3000 | - | - | - |
| Ethernet21 | User port | trunk | 100-200,222,456,999-3000 | - | - | - |
| Ethernet22 | User port | trunk | 100-200,222,456,999-3000 | - | - | - |
| Ethernet23 | User port | trunk | 100-200,222,456,999-3000 | - | - | - |
| Ethernet24 | User port | trunk | 100-200,222,456,999-3000 | - | - | - |
| Ethernet25 | Phone port | trunk phone | - | 200 | - | - |
| Ethernet26 | Phone port | trunk phone | - | 200 | - | - |
| Ethernet27 | Phone port | trunk phone | - | 200 | - | - |
| Ethernet28 | Phone port | trunk phone | - | 200 | - | - |
| Ethernet29 | Phone port | trunk phone | - | 200 | - | - |
| Ethernet30 | Phone port | trunk phone | - | 200 | - | - |
| Ethernet31 | Phone port | trunk phone | - | 200 | - | - |
| Ethernet32 | Phone port | trunk phone | - | 200 | - | - |
| Ethernet33 | Phone port | trunk phone | - | 200 | - | - |
| Ethernet34 | Phone port | trunk phone | - | 200 | - | - |
| Ethernet35 | Phone port | trunk phone | - | 200 | - | - |
| Ethernet36 | Phone port | trunk phone | - | 200 | - | - |
| Ethernet37 | Phone port | trunk phone | - | 200 | - | - |
| Ethernet38 | Phone port | trunk phone | - | 200 | - | - |
| Ethernet39 | Phone port | trunk phone | - | 200 | - | - |
| Ethernet40 | Phone port | trunk phone | - | 200 | - | - |
| Ethernet41 | Phone port | trunk phone | - | 200 | - | - |
| Ethernet42 | Phone port | trunk phone | - | 200 | - | - |
| Ethernet43 | Phone port | trunk phone | - | 200 | - | - |
| Ethernet44 | Phone port | trunk phone | - | 200 | - | - |
| Ethernet45 | Phone port | trunk phone | - | 200 | - | - |
| Ethernet46 | Phone port | trunk phone | - | 200 | - | - |
| Ethernet47 | Phone port | trunk phone | - | 200 | - | - |
| Ethernet48 | Phone port | trunk phone | - | 200 | - | - |

*Inherited from Port-Channel Interface

#### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet1
   description User port
   no shutdown
   switchport trunk allowed vlan 100-200,456,222,999,1000-3000
   switchport mode trunk
   switchport
!
interface Ethernet2
   description User port
   no shutdown
   switchport trunk allowed vlan 100-200,456,222,999,1000-3000
   switchport mode trunk
   switchport
!
interface Ethernet2/1
   description L2_l3leaf2_Ethernet2/3
   no shutdown
   channel-group 21 mode active
!
interface Ethernet2/2
   description L2_l3leaf1_Ethernet2/4
   no shutdown
   channel-group 21 mode active
!
interface Ethernet3
   description User port
   no shutdown
   switchport trunk allowed vlan 100-200,456,222,999,1000-3000
   switchport mode trunk
   switchport
!
interface Ethernet4
   description User port
   no shutdown
   switchport trunk allowed vlan 100-200,456,222,999,1000-3000
   switchport mode trunk
   switchport
!
interface Ethernet5
   description User port
   no shutdown
   switchport trunk allowed vlan 100-200,456,222,999,1000-3000
   switchport mode trunk
   switchport
!
interface Ethernet6
   description User port
   no shutdown
   switchport trunk allowed vlan 100-200,456,222,999,1000-3000
   switchport mode trunk
   switchport
!
interface Ethernet7
   description User port
   no shutdown
   switchport trunk allowed vlan 100-200,456,222,999,1000-3000
   switchport mode trunk
   switchport
!
interface Ethernet8
   description User port
   no shutdown
   switchport trunk allowed vlan 100-200,456,222,999,1000-3000
   switchport mode trunk
   switchport
!
interface Ethernet9
   description User port
   no shutdown
   switchport trunk allowed vlan 100-200,456,222,999,1000-3000
   switchport mode trunk
   switchport
!
interface Ethernet10
   description User port
   no shutdown
   switchport trunk allowed vlan 100-200,456,222,999,1000-3000
   switchport mode trunk
   switchport
!
interface Ethernet11
   description User port
   no shutdown
   switchport trunk allowed vlan 100-200,456,222,999,1000-3000
   switchport mode trunk
   switchport
!
interface Ethernet12
   description User port
   no shutdown
   switchport trunk allowed vlan 100-200,456,222,999,1000-3000
   switchport mode trunk
   switchport
!
interface Ethernet13
   description User port
   no shutdown
   switchport trunk allowed vlan 100-200,456,222,999,1000-3000
   switchport mode trunk
   switchport
!
interface Ethernet14
   description User port
   no shutdown
   switchport trunk allowed vlan 100-200,456,222,999,1000-3000
   switchport mode trunk
   switchport
!
interface Ethernet15
   description User port
   no shutdown
   switchport trunk allowed vlan 100-200,456,222,999,1000-3000
   switchport mode trunk
   switchport
!
interface Ethernet16
   description User port
   no shutdown
   switchport trunk allowed vlan 100-200,456,222,999,1000-3000
   switchport mode trunk
   switchport
!
interface Ethernet17
   description User port
   no shutdown
   switchport trunk allowed vlan 100-200,456,222,999,1000-3000
   switchport mode trunk
   switchport
!
interface Ethernet18
   description User port
   no shutdown
   switchport trunk allowed vlan 100-200,456,222,999,1000-3000
   switchport mode trunk
   switchport
!
interface Ethernet19
   description User port
   no shutdown
   switchport trunk allowed vlan 100-200,456,222,999,1000-3000
   switchport mode trunk
   switchport
!
interface Ethernet20
   description User port
   no shutdown
   switchport trunk allowed vlan 100-200,456,222,999,1000-3000
   switchport mode trunk
   switchport
!
interface Ethernet21
   description User port
   no shutdown
   switchport trunk allowed vlan 100-200,456,222,999,1000-3000
   switchport mode trunk
   switchport
!
interface Ethernet22
   description User port
   no shutdown
   switchport trunk allowed vlan 100-200,456,222,999,1000-3000
   switchport mode trunk
   switchport
!
interface Ethernet23
   description User port
   no shutdown
   switchport trunk allowed vlan 100-200,456,222,999,1000-3000
   switchport mode trunk
   switchport
!
interface Ethernet24
   description User port
   no shutdown
   switchport trunk allowed vlan 100-200,456,222,999,1000-3000
   switchport mode trunk
   switchport
!
interface Ethernet25
   description Phone port
   no shutdown
   switchport trunk native vlan 200
   switchport mode trunk phone
   switchport
!
interface Ethernet26
   description Phone port
   no shutdown
   switchport trunk native vlan 200
   switchport mode trunk phone
   switchport
!
interface Ethernet27
   description Phone port
   no shutdown
   switchport trunk native vlan 200
   switchport mode trunk phone
   switchport
!
interface Ethernet28
   description Phone port
   no shutdown
   switchport trunk native vlan 200
   switchport mode trunk phone
   switchport
!
interface Ethernet29
   description Phone port
   no shutdown
   switchport trunk native vlan 200
   switchport mode trunk phone
   switchport
!
interface Ethernet30
   description Phone port
   no shutdown
   switchport trunk native vlan 200
   switchport mode trunk phone
   switchport
!
interface Ethernet31
   description Phone port
   no shutdown
   switchport trunk native vlan 200
   switchport mode trunk phone
   switchport
!
interface Ethernet32
   description Phone port
   no shutdown
   switchport trunk native vlan 200
   switchport mode trunk phone
   switchport
!
interface Ethernet33
   description Phone port
   no shutdown
   switchport trunk native vlan 200
   switchport mode trunk phone
   switchport
!
interface Ethernet34
   description Phone port
   no shutdown
   switchport trunk native vlan 200
   switchport mode trunk phone
   switchport
!
interface Ethernet35
   description Phone port
   no shutdown
   switchport trunk native vlan 200
   switchport mode trunk phone
   switchport
!
interface Ethernet36
   description Phone port
   no shutdown
   switchport trunk native vlan 200
   switchport mode trunk phone
   switchport
!
interface Ethernet37
   description Phone port
   no shutdown
   switchport trunk native vlan 200
   switchport mode trunk phone
   switchport
!
interface Ethernet38
   description Phone port
   no shutdown
   switchport trunk native vlan 200
   switchport mode trunk phone
   switchport
!
interface Ethernet39
   description Phone port
   no shutdown
   switchport trunk native vlan 200
   switchport mode trunk phone
   switchport
!
interface Ethernet40
   description Phone port
   no shutdown
   switchport trunk native vlan 200
   switchport mode trunk phone
   switchport
!
interface Ethernet41
   description Phone port
   no shutdown
   switchport trunk native vlan 200
   switchport mode trunk phone
   switchport
!
interface Ethernet42
   description Phone port
   no shutdown
   switchport trunk native vlan 200
   switchport mode trunk phone
   switchport
!
interface Ethernet43
   description Phone port
   no shutdown
   switchport trunk native vlan 200
   switchport mode trunk phone
   switchport
!
interface Ethernet44
   description Phone port
   no shutdown
   switchport trunk native vlan 200
   switchport mode trunk phone
   switchport
!
interface Ethernet45
   description Phone port
   no shutdown
   switchport trunk native vlan 200
   switchport mode trunk phone
   switchport
!
interface Ethernet46
   description Phone port
   no shutdown
   switchport trunk native vlan 200
   switchport mode trunk phone
   switchport
!
interface Ethernet47
   description Phone port
   no shutdown
   switchport trunk native vlan 200
   switchport mode trunk phone
   switchport
!
interface Ethernet48
   description Phone port
   no shutdown
   switchport trunk native vlan 200
   switchport mode trunk phone
   switchport
```

### Port-Channel Interfaces

#### Port-Channel Interfaces Summary

##### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | LACP Fallback Timeout | LACP Fallback Mode | MLAG ID | EVPN ESI |
| --------- | ----------- | ---- | ----- | ----------- | ----------- | --------------------- | ------------------ | ------- | -------- |
| Port-Channel21 | L2_l3leaf2_Port-Channel23 | trunk | 101-102 | - | - | - | - | - | - |

#### Port-Channel Interfaces Device Configuration

```eos
!
interface Port-Channel21
   description L2_l3leaf2_Port-Channel23
   no shutdown
   switchport trunk allowed vlan 101-102
   switchport mode trunk
   switchport
```

## Routing

### Service Routing Protocols Model

Multi agent routing protocol model enabled

```eos
!
service routing protocols model multi-agent
```

### IP Routing

#### IP Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | False |
| MGMT | False |

#### IP Routing Device Configuration

```eos
no ip routing vrf MGMT
```

### IPv6 Routing

#### IPv6 Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | False |
| MGMT | false |

## Multicast

### IP IGMP Snooping

#### IP IGMP Snooping Summary

| IGMP Snooping | Fast Leave | Interface Restart Query | Proxy | Restart Query Interval | Robustness Variable |
| ------------- | ---------- | ----------------------- | ----- | ---------------------- | ------------------- |
| Enabled | - | - | - | - | - |

#### IP IGMP Snooping Device Configuration

```eos
```

## VRF Instances

### VRF Instances Summary

| VRF Name | RD | IP Routing |
| -------- | --- | ---------- |
| MGMT | - | disabled |

### VRF Instances Device Configuration

```eos
!
vrf instance MGMT
```
