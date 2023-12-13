# policy-maps

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [Routing](#routing)
  - [PBR Policy Maps](#pbr-policy-maps)
- [Quality Of Service](#quality-of-service)
  - [QOS Policy Maps](#qos-policy-maps)

## Management

### Management Interfaces

#### Management Interfaces Summary

##### IPv4

| Management Interface | description | Type | VRF | IP Address | Gateway |
| -------------------- | ----------- | ---- | --- | ---------- | ------- |
| Management1 | oob_management | oob | MGMT | 10.73.255.122/24 | 10.73.255.2 |

##### IPv6

| Management Interface | description | Type | VRF | IPv6 Address | IPv6 Gateway |
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

## Routing

### PBR Policy Maps

#### PBR Policy Maps Summary

##### PM_PBR_BREAKOUT

| Class | Index | Drop | Nexthop | Recursive |
| ----- | ----- | ---- | ------- | --------- |
| CM_PBR_EXCLUDE | - | - | - | - |
| CM_PBR_INCLUDE | - | - | 192.168.4.2 | True |

#### PBR Policy Maps Device Configuration

```eos
!
policy-map type pbr PM_PBR_BREAKOUT
   class CM_PBR_EXCLUDE
   !
   class CM_PBR_INCLUDE
      set nexthop recursive 192.168.4.2
```

## Quality Of Service

### QOS Policy Maps

#### QOS Policy Maps Summary

##### PM_REPLICATION_LD

| class | Set | Value |
| ----- | --- | ----- |
| CM_REPLICATION_LD | dscp | af11 |
| CM_REPLICATION_LD | traffic_class | 2 |
| CM_REPLICATION_LD | drop_precedence | 1 |
| CM_REPLICATION_LD_2 | dscp | af11 |
| CM_REPLICATION_LD_2 | traffic_class | 2 |

##### PM_REPLICATION_LD2

| class | Set | Value |
| ----- | --- | ----- |
| CM_REPLICATION_LD | dscp | af11 |
| CM_REPLICATION_LD | cos | 4 |

#### QOS Policy Maps Device Configuration

```eos
!
policy-map type quality-of-service PM_REPLICATION_LD
   class CM_REPLICATION_LD
      set dscp af11
      set traffic-class 2
      set drop-precedence 1
   !
   class CM_REPLICATION_LD_2
      set dscp af11
      set traffic-class 2
!
policy-map type quality-of-service PM_REPLICATION_LD2
   class CM_REPLICATION_LD
      set dscp af11
      set cos 4
```
