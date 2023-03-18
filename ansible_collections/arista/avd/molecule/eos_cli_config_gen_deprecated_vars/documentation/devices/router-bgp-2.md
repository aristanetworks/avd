# router-bgp-2
# Table of Contents

- [Routing](#routing)
  - [Router BGP](#router-bgp)

# Routing

## Router BGP

### Router BGP Summary

| BGP AS | Router ID |
| ------ | --------- |
| 65101|  192.168.255.3 |

### Router BGP VRFs

| VRF | Route-Distinguisher | Redistribute |
| --- | ------------------- | ------------ |
| test | - | connected |

### Router BGP Device Configuration

```eos
!
router bgp 65101
   router-id 192.168.255.3
   redistribute connected
   !
   vrf test
      redistribute connected
```
