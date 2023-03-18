# bgp-groups
# Table of Contents

- [Maintenance Mode](#maintenance-mode)
  - [BGP Groups](#bgp-groups)

# Maintenance Mode

## BGP Groups

### BGP Groups Summary

| BGP group | VRF Name | Neighbors | BGP maintenance profiles |
| --------- | -------- | --------- | ------------------------ |
| bar | red | peer-group-baz | downlink-neighbors |
| foo | - | 169.254.1.1<br>fe80::1 | Default |

### BGP Groups Configuration

```eos
!
group bgp bar
   vrf red
   neighbor peer-group-baz
   maintenance profile bgp downlink-neighbors
!
group bgp foo
   neighbor 169.254.1.1
   neighbor fe80::1
```
