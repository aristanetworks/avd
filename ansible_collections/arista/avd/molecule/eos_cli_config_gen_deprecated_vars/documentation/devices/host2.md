# host2

## Table of Contents

- [Routing](#routing)
  - [Router BGP](#router-bgp)

## Routing

### Router BGP

ASN Notation: asplain

#### Router BGP Summary

| BGP AS | Router ID |
| ------ | --------- |
| 65101 | 192.168.255.3 |

#### Router BGP EVPN Address Family

#### Router BGP Device Configuration

```eos
!
router bgp 65101
   router-id 192.168.255.3
   !
   address-family evpn
      bgp additional-paths receive
      bgp additional-paths send any
```
