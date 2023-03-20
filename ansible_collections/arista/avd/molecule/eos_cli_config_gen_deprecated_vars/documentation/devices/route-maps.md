# route-maps
# Table of Contents

- [Filters](#filters)
  - [Route-maps](#route-maps)

# Filters

## Route-maps

### Route-maps Summary

#### RM-CONN-BL-BGP

| Sequence | Type | Match | Set | Sub-Route-Map | Continue |
| -------- | ---- | ----- | --- | ------------- | -------- |
| 10 | deny | ip address prefix-list PL-MLAG | - | - | - |

### Route-maps Device Configuration

```eos
!
route-map RM-CONN-BL-BGP deny 10
   match ip address prefix-list PL-MLAG
```
