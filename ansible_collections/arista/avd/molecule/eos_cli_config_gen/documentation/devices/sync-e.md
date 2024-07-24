# sync-e

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
  - [Synchronous Ethernet (SyncE) Settings](#synchronous-ethernet-synce-settings)
- [Interfaces](#interfaces)
  - [Ethernet Interfaces](#ethernet-interfaces)

## Management

### Management Interfaces

#### Management Interfaces Summary

##### IPv4

| Management Interface | Description | Type | VRF | IP Address | Gateway |
| -------------------- | ----------- | ---- | --- | ---------- | ------- |
| Management1 | oob_management | oob | MGMT | 10.73.255.122/24 | 10.73.255.2 |

##### IPv6

| Management Interface | Description | Type | VRF | IPv6 Address | IPv6 Gateway |
| -------------------- | ----------- | ---- | --- | ------------ | ------------ |
| Management1 | oob_management | oob | MGMT | - | - |

#### Management Interfaces Device Configuration

```eos
!
interface Management1
   description oob_management
   vrf MGMT
   ip address 10.73.255.122/24
```

### Synchronous Ethernet (SyncE) Settings

Synchronous Ethernet Network Option: 2

#### Synchronous Ethernet Device Configuration

```eos
!
sync-e
   network option 2
```

## Interfaces

### Ethernet Interfaces

#### Ethernet Interfaces Summary

##### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | Channel-Group |
| --------- | ----------- | ---- | ----- | ----------- | ----------- | ------------- |
| Ethernet3 |  P2P_LINK_TO_DC1-SPINE2_Ethernet5 | trunk | 2,14 | - | - | - |

*Inherited from Port-Channel Interface

##### IPv4

| Interface | Description | Type | Channel Group | IP Address | VRF |  MTU | Shutdown | ACL In | ACL Out |
| --------- | ----------- | -----| ------------- | ---------- | ----| ---- | -------- | ------ | ------- |
| Ethernet6 | P2P_LINK_TO_DC1-SPINE1_Ethernet6 | routed | - | 172.31.255.15/31 | default | 1500 | - | - | - |

#### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet3
   description P2P_LINK_TO_DC1-SPINE2_Ethernet5
   switchport trunk allowed vlan 2,14
   switchport mode trunk
   switchport
!
interface Ethernet5
   description DC1-AGG01_Ethernet1
!
interface Ethernet6
   description P2P_LINK_TO_DC1-SPINE1_Ethernet6
   mtu 1500
   no switchport
   ip address 172.31.255.15/31
```
