# router-bgp-vrf-address-families

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [Routing](#routing)
  - [Router BGP](#router-bgp)

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

### Router BGP

#### Router BGP Summary

| BGP AS | Router ID |
| ------ | --------- |
| 65001 | 1.0.1.1 |

#### Router BGP VRFs

| VRF | Route-Distinguisher | Redistribute |
| --- | ------------------- | ------------ |
| VRF01 | - | - |
| VRF02 | - | - |
| VRF03 | - | - |

#### Router BGP Device Configuration

```eos
!
router bgp 65001
   router-id 1.0.1.1
   !
   address-family flow-spec ipv4
      neighbor FOOBAR activate
   !
   address-family flow-spec ipv6
      no neighbor FOOBAR activate
   !
   address-family ipv4
      neighbor FOOBAR next-hop address-family ipv6 originate
      neighbor FOOBAR activate
   !
   address-family ipv4 multicast
      neighbor FOOBAR activate
   !
   address-family ipv6
      no neighbor FOOBAR activate
   !
   address-family ipv6 multicast
      no neighbor FOOBAR activate
   !
   vrf VRF01
      !
      address-family flow-spec ipv4
         bgp missing-policy direction in action permit
         bgp missing-policy direction out action permit
         neighbor 1.2.3.4 activate
      !
      address-family flow-spec ipv6
         bgp missing-policy direction in action permit
         bgp missing-policy direction out action deny
         neighbor aa::1 activate
      !
      address-family ipv4
         bgp missing-policy direction in action deny
         bgp missing-policy direction out action permit
         bgp additional-paths install ecmp-primary
         bgp additional-paths receive
         bgp additional-paths send ecmp limit 4
         neighbor 1.2.3.4 activate
         neighbor 1.2.3.4 route-map FOO in
         neighbor 1.2.3.4 route-map BAR out
         network 2.3.4.0/24 route-map BARFOO
      !
      address-family ipv4 multicast
         bgp missing-policy direction in action permit
         bgp missing-policy direction out action permit
         bgp additional-paths receive
         neighbor 1.2.3.4 route-map FOO in
         neighbor 1.2.3.4 route-map BAR out
         network 239.0.0.0/24 route-map BARFOO
      !
      address-family ipv6
         bgp missing-policy direction in action deny-in-out
         bgp missing-policy direction out action deny-in-out
         bgp additional-paths install
         bgp additional-paths receive
         bgp additional-paths send any
         neighbor aa::1 activate
         neighbor aa::1 route-map FOO in
         neighbor aa::1 route-map BAR out
         network aa::/64
      !
      address-family ipv6 multicast
         bgp missing-policy direction in action deny
         bgp missing-policy direction out action deny
         network ff08:1::/64
   !
   vrf VRF02
      !
      address-family ipv4
         bgp additional-paths send backup
      !
      address-family ipv6
         bgp additional-paths send limit 3
   !
   vrf VRF03
      !
      address-family ipv4
         bgp additional-paths send ecmp
```
