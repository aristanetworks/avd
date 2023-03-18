# policy-maps
# Table of Contents

- [Routing](#routing)
  - [PBR Policy Maps](#pbr-policy-maps)
- [Quality Of Service](#quality-of-service)
  - [QOS Policy Maps](#qos-policy-maps)

# Routing

## PBR Policy Maps

### PBR Policy Maps Summary

#### PM_PBR_BREAKOUT

| Class | Index | Drop | Nexthop | Recursive |
| ----- | ----- | ---- | ------- | --------- |
| CM_PBR_EXCLUDE | - | - | - | - |
| CM_PBR_INCLUDE | - | - | 192.168.4.2 | True |

### PBR Policy Maps Configuration

```eos
!
policy-map type pbr PM_PBR_BREAKOUT
   class CM_PBR_EXCLUDE
   !
   class CM_PBR_INCLUDE
      set nexthop recursive 192.168.4.2
```

# Quality Of Service

## QOS Policy Maps

### QOS Policy Maps Summary

**PM_REPLICATION_LD**

| class | Set | Value |
| ----- | --- | ----- |
| CM_REPLICATION_LD | dscp | af11 |
| CM_REPLICATION_LD | traffic_class | 2 |
| CM_REPLICATION_LD | drop_precedence | 1 |

### QOS Policy Maps configuration

```eos
!
policy-map type quality-of-service PM_REPLICATION_LD
   class CM_REPLICATION_LD
      set dscp af11
      set traffic-class 2
      set drop-precedence 1
```
