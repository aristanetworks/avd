# class-maps
# Table of Contents

- [Quality Of Service](#quality-of-service)
  - [QOS Class Maps](#qos-class-maps)

# Quality Of Service

## QOS Class Maps

### QOS Class Maps Summary

| Name | Field | Value |
| ---- | ----- | ----- |
| CM_REPLICATION_LD | acl | ACL_REPLICATION_LD |
| CM_REPLICATION_LD2 | vlan | 200 |
| CM_REPLICATION_LD3 | cos | 3 |

### Class-maps Device Configuration

```eos
!
class-map type qos match-any CM_REPLICATION_LD
   match ip access-group ACL_REPLICATION_LD
!
class-map type qos match-any CM_REPLICATION_LD2
   match vlan 200
!
class-map type qos match-any CM_REPLICATION_LD3
   match cos 3
!
class-map type pbr match-any CM_PBR_EXCLUDE
   match ip access-group ACL_PBR_EXCLUDE
!
class-map type pbr match-any CM_PBR_INCLUDE
   match ip access-group ACL_PBR_INCLUDE
```
