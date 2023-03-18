# router-ospf
# Table of Contents

- [Routing](#routing)
  - [Router OSPF](#router-ospf)

# Routing

## Router OSPF

### Router OSPF Summary

| Process ID | Router ID | Default Passive Interface | No Passive Interface | BFD | Max LSA | Default Information Originate | Log Adjacency Changes Detail | Auto Cost Reference Bandwidth | Maximum Paths | MPLS LDP Sync Default | Distribute List In |
| ---------- | --------- | ------------------------- | -------------------- | --- | ------- | ----------------------------- | ---------------------------- | ----------------------------- | ------------- | --------------------- | ------------------ |
| 100 | - | disabled |- | disabled | default | disabled | disabled | - | - | - | - |

### Router OSPF Areas

| Process ID | Area | Area Type | Filter Networks | Filter Prefix List | Additional Options |
| ---------- | ---- | --------- | --------------- | ------------------ | ------------------ |
| 100 | 0.0.0.2 | normal | 1.1.1.0/24, 2.2.2.0/24 | - |  |
| 100 | 3 | normal | - | PL-OSPF-FILTERING |  |

### Router OSPF Device Configuration

```eos
!
router ospf 100
   network 198.51.100.0/24 area 0.0.0.1
   network 203.0.113.0/24 area 0.0.0.2
   area 0.0.0.2 filter 1.1.1.0/24
   area 0.0.0.2 filter 2.2.2.0/24
   area 3 filter prefix-list PL-OSPF-FILTERING
```
