# spanning-tree
# Table of Contents

- [Spanning Tree](#spanning-tree)
  - [Spanning Tree Summary](#spanning-tree-summary)
  - [Spanning Tree Device Configuration](#spanning-tree-device-configuration)

# Spanning Tree

## Spanning Tree Summary

STP mode: **mstp**

### MSTP Instance and Priority

| Instance(s) | Priority |
| -------- | -------- |
| 0 | 4096 |
| 100-200 | 8192 |

### MST Configuration

| Variable | Value |
| -------- | -------- |
| Name | test |
| Revision | 5 |
| Instance 2 | VLAN(s) 15,16,17,18 |
| Instance 3 | VLAN(s) 15 |
| Instance 4 | VLAN(s) 200-300 |

## Spanning Tree Device Configuration

```eos
!
spanning-tree mode mstp
spanning-tree mst 0 priority 4096
spanning-tree mst 100-200 priority 8192
!
spanning-tree mst configuration
   name test
   revision 5
   instance 2 vlan 15,16,17,18
   instance 3 vlan 15
   instance 4 vlan 200-300
```
