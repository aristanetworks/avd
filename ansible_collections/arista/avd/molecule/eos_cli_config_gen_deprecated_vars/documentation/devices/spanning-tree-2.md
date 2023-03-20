# spanning-tree-2
# Table of Contents

- [Spanning Tree](#spanning-tree)
  - [Spanning Tree Summary](#spanning-tree-summary)
  - [Spanning Tree Device Configuration](#spanning-tree-device-configuration)

# Spanning Tree

## Spanning Tree Summary

STP mode: **rapid-pvst**

### Rapid-PVST Instance and Priority

| Instance(s) | Priority |
| -------- | -------- |
| 1,2,3,4,5,10-15 | 4096 |
| 3 | 8192 |
| 100-500 | 16384 |

## Spanning Tree Device Configuration

```eos
!
spanning-tree mode rapid-pvst
spanning-tree vlan-id 1,2,3,4,5,10-15 priority 4096
spanning-tree vlan-id 3 priority 8192
spanning-tree vlan-id 100-500 priority 16384
```
