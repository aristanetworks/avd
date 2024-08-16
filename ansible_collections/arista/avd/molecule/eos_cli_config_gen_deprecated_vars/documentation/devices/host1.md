# host1

## Table of Contents

- [Interfaces](#interfaces)
  - [Ethernet Interfaces](#ethernet-interfaces)
  - [Port-Channel Interfaces](#port-channel-interfaces)

## Interfaces

### Ethernet Interfaces

#### Ethernet Interfaces Summary

##### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | Channel-Group |
| --------- | ----------- | ---- | ----- | ----------- | ----------- | ------------- |

*Inherited from Port-Channel Interface

##### Private VLAN

| Interface | PVLAN Mapping | Secondary Trunk |
| --------- | ------------- | ----------------|
| Ethernet4 | 2,3,4 | True |

##### VLAN Translations

| Interface |  Direction | From VLAN ID(s) | To VLAN ID | From Inner VLAN ID | To Inner VLAN ID | Network | Dot1q-tunnel |
| --------- |  --------- | --------------- | ---------- | ------------------ | ---------------- | ------- | ------------ |
| Ethernet4 | in | 23 | 50 | - | - | - | - |
| Ethernet4 | out | 25 | 49 | - | - | - | - |
| Ethernet4 | both | 34 | 60 | - | - | - | - |

##### Phone Interfaces

| Interface | Mode | Native VLAN | Phone VLAN | Phone VLAN Mode |
| --------- | ---- | ----------- | ---------- | --------------- |
| Ethernet3 | trunk phone | 20 | 20 | tagged |
| Port-Channel4 | trunk phone | 20 | 20 | tagged |

#### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet1
   switchport access vlan 100
   switchport mode access
!
interface Ethernet2
   switchport trunk native vlan 10
   switchport trunk allowed vlan 110
   switchport mode trunk
   switchport trunk group group1
   switchport trunk group group2
!
interface Ethernet3
   switchport trunk native vlan tag
   switchport phone vlan 20
   switchport phone trunk tagged
   switchport mode trunk phone
!
interface Ethernet4
   switchport vlan translation in 23 50
   switchport vlan translation out 25 49
   switchport vlan translation 34 60
   switchport trunk private-vlan secondary
   switchport pvlan mapping 2,3,4
```

### Port-Channel Interfaces

#### Port-Channel Interfaces Summary

##### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | LACP Fallback Timeout | LACP Fallback Mode | MLAG ID | EVPN ESI |
| --------- | ----------- | ---- | ----- | ----------- | ------------| --------------------- | ------------------ | ------- | -------- |

##### Private VLAN

| Interface | PVLAN Mapping | Secondary Trunk |
| --------- | ------------- | ----------------|
| Port-Channel5 | 2,3,4 | True |

##### VLAN Translations

| Interface |  Direction | From VLAN ID(s) | To VLAN ID | From Inner VLAN ID | To Inner VLAN ID | Network | Dot1q-tunnel |
| --------- |  --------- | --------------- | ---------- | ------------------ | ---------------- | ------- | ------------ |
| Port-Channel5 | in | 23 | 50 | - | - | - | - |
| Port-Channel5 | out | 25 | 49 | - | - | - | - |
| Port-Channel5 | both | 34 | 60 | - | - | - | - |

#### Port-Channel Interfaces Device Configuration

```eos
!
interface Port-Channel2
   switchport access vlan 100
!
interface Port-Channel3
   switchport trunk allowed vlan 110
   switchport trunk native vlan 10
   switchport mode trunk
   switchport trunk group group1
   switchport trunk group group2
!
interface Port-Channel4
   switchport trunk native vlan tag
   switchport phone vlan 20
   switchport phone trunk tagged
   switchport mode trunk phone
!
interface Port-Channel5
   switchport trunk private-vlan secondary
   switchport pvlan mapping 2,3,4
   switchport vlan translation in 23 50
   switchport vlan translation out 25 49
   switchport vlan translation 34 60
```
