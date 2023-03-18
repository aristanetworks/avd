# router-bgp
# Table of Contents

- [Routing](#routing)
  - [Router BGP](#router-bgp)

# Routing

## Router BGP

### Router BGP Summary

| BGP AS | Router ID |
| ------ | --------- |
| 65101|  192.168.255.3 |

### Router BGP Peer Groups

#### EVPN-OVERLAY-PEERS

| Settings | Value |
| -------- | ----- |
| Address Family | evpn |
| Remote AS | 65001 |
| Source | Loopback0 |

### BGP Neighbors

| Neighbor | Remote AS | VRF | Shutdown | Send-community | Maximum-routes | Allowas-in | BFD | RIB Pre-Policy Retain | Route-Reflector Client | Passive |
| -------- | --------- | --- | -------- | -------------- | -------------- | ---------- | --- | --------------------- | ---------------------- | ------- |
| 192.168.255.1 | Inherited from peer group EVPN-OVERLAY-PEERS | default | - | - | - | - | - | - | - | - |
| 192.168.255.2 | Inherited from peer group EVPN-OVERLAY-PEERS | default | - | - | - | - | - | - | - | - |
| 10.255.251.1 | Inherited from peer group EVPN-OVERLAY-PEERS | TENANT_A_PROJECT01 | - | - | - | - | - | - | - | - |

### BGP Neighbor Interfaces

| Neighbor Interface | VRF | Peer Group | Remote AS | Peer Filter |
| ------------------ | --- | ---------- | --------- | ----------- |
| Ethernet2 | default | EVPN-OVERLAY-PEERS | 65102 | - |
| Ethernet27 | TENANT_A_PROJECT01 | MLAG-IPv4-UNDERLAY-PEER | 1 | - |

### BGP Route Aggregation

| Prefix | AS Set | Summary Only | Attribute Map | Match Map | Advertise Only |
| ------ | ------ | ------------ | ------------- | --------- | -------------- |
| 1.1.1.0/24 | False | False | - | - | True |
| 2.2.1.0/24 | False | False | - | - | False |

### Router BGP EVPN Address Family

#### EVPN Peer Groups

| Peer Group | Activate | Encapsulation |
| ---------- | -------- | ------------- |
| EVPN-OVERLAY-PEERS | True | default |

### Router BGP VPN-IPv4 Address Family

#### VPN-IPv4 Neighbors

| Neighbor | Activate | Route-map In | Route-map Out |
| -------- | -------- | ------------ | ------------- |
| 192.168.255.4 | True | - | - |

#### VPN-IPv4 Peer Groups

| Peer Group | Activate | Route-map In | Route-map Out |
| ---------- | -------- | ------------ | ------------- |
| EVPN-OVERLAY-PEERS | True | - | - |

### Router BGP VPN-IPv6 Address Family

#### VPN-IPv6 Neighbors

| Neighbor | Activate | Route-map In | Route-map Out |
| -------- | -------- | ------------ | ------------- |
| 2001:cafe:192:168::4 | True | - | - |

#### VPN-IPv6 Peer Groups

| Peer Group | Activate | Route-map In | Route-map Out |
| ---------- | -------- | ------------ | ------------- |
| EVPN-OVERLAY-PEERS | True | - | - |

### Router BGP VLAN Aware Bundles

| VLAN Aware Bundle | Route-Distinguisher | Both Route-Target | Import Route Target | Export Route-Target | Redistribute | VLANs |
| ----------------- | ------------------- | ----------------- | ------------------- | ------------------- | ------------ | ----- |
| TENANT_A_PROJECT01 | 192.168.255.3:11 | 11:11 | - | - | learned | 110 |

### Router BGP VLANs

| VLAN | Route-Distinguisher | Both Route-Target | Import Route Target | Export Route-Target | Redistribute |
| ---- | ------------------- | ----------------- | ------------------- | ------------------- | ------------ |
| 24 | 10.50.64.15:10024 | 1:10024 | - | - |  |

### Router BGP VRFs

| VRF | Route-Distinguisher | Redistribute |
| --- | ------------------- | ------------ |
| TENANT_A_PROJECT01 | 192.168.255.3:11 | connected<br>static |

### Router BGP Device Configuration

```eos
!
router bgp 65101
   router-id 192.168.255.3
   neighbor EVPN-OVERLAY-PEERS peer group
   neighbor EVPN-OVERLAY-PEERS remote-as 65001
   neighbor EVPN-OVERLAY-PEERS update-source Loopback0
   neighbor interface Ethernet2 peer-group EVPN-OVERLAY-PEERS remote-as 65102
   neighbor 192.168.255.1 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.255.2 peer group EVPN-OVERLAY-PEERS
   aggregate-address 1.1.1.0/24 advertise-only
   aggregate-address 2.2.1.0/24
   redistribute connected route-map RM-CONN-2-BGP
   !
   vlan 24
      rd 10.50.64.15:10024
      route-target both 1:10024
   !
   vlan-aware-bundle TENANT_A_PROJECT01
      rd 192.168.255.3:11
      route-target both 11:11
      redistribute learned
      vlan 110
   !
   address-family evpn
      neighbor EVPN-OVERLAY-PEERS activate
   !
   address-family rt-membership
      neighbor EVPN-OVERLAY-PEERS activate
   !
   address-family ipv4
      neighbor EVPN-OVERLAY-PEERS activate
      neighbor 192.0.2.1 prefix-list PL-FOO-v4-IN in
      neighbor 192.0.2.1 prefix-list PL-FOO-v4-OUT out
      network 10.0.0.0/8
      network 172.16.0.0/12
      network 192.168.0.0/16 route-map RM-FOO-MATCH
   !
   address-family ipv4 multicast
      neighbor EVPN-OVERLAY-PEERS activate
      redistribute attached-host
   !
   address-family ipv6
      neighbor EVPN-OVERLAY-PEERS activate
      neighbor 2001:db8::1 prefix-list PL-FOO-v6-IN in
      neighbor 2001:db8::1 prefix-list PL-FOO-v6-OUT out
      network 2001:db8:100::/40
      network 2001:db8:200::/40 route-map RM-BAR-MATCH
      redistribute static route-map RM-IPV6-STATIC-TO-BGP
   !
   address-family vpn-ipv4
      neighbor EVPN-OVERLAY-PEERS activate
      neighbor 192.168.255.4 activate
   !
   address-family vpn-ipv6
      neighbor EVPN-OVERLAY-PEERS activate
      neighbor 2001:cafe:192:168::4 activate
   !
   vrf TENANT_A_PROJECT01
      rd 192.168.255.3:11
      route-target import evpn 11:11
      route-target export evpn 11:11
      router-id 192.168.255.3
      neighbor interface Ethernet27 peer-group MLAG-IPv4-UNDERLAY-PEER remote-as 1
      neighbor 10.255.251.1 peer group EVPN-OVERLAY-PEERS
      network 10.0.0.0/8
      network 100.64.0.0/10
      aggregate-address 0.0.0.0/0 as-set summary-only attribute-map RM-BGP-AGG-APPLY-SET
      redistribute connected
      redistribute static route-map RM-CONN-2-BGP
      !
      address-family ipv4
         neighbor TEST_PEER_GRP activate
         neighbor 10.2.3.4 activate
         neighbor 10.2.3.4 route-map RM-10.2.3.4-SET-NEXT-HOP-OUT out
         neighbor 10.2.3.5 activate
         neighbor 10.2.3.5 route-map RM-10.2.3.5-SET-NEXT-HOP-IN in
         network 10.0.0.0/8
         network 100.64.0.0/10 route-map RM-10.2.3.4
```
