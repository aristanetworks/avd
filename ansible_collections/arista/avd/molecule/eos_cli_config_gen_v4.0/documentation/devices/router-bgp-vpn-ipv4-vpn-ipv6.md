# router-bgp-vpn-ipv4-vpn-ipv6

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
| 65103|  192.168.255.3 |

| BGP Tuning |
| ---------- |
| no bgp default ipv4-unicast |
| distance bgp 20 200 200 |
| graceful-restart restart-time 300 |
| graceful-restart |
| maximum-paths 2 ecmp 2 |

#### Router BGP Peer Groups

##### MPLS-IBGP-PEERS

| Settings | Value |
| -------- | ----- |
| Address Family | vpn-ipv4, vpn-ipv6 |
| Remote AS | 65000 |
| Local AS | 65000 |
| Send community | all |
| Maximum routes | 0 (no limit) |

#### BGP Neighbors

| Neighbor | Remote AS | VRF | Shutdown | Send-community | Maximum-routes | Allowas-in | BFD | RIB Pre-Policy Retain | Route-Reflector Client | Passive |
| -------- | --------- | --- | -------- | -------------- | -------------- | ---------- | --- | --------------------- | ---------------------- | ------- |
| 192.168.255.1 | Inherited from peer group MPLS-IBGP-PEERS | default | - | Inherited from peer group MPLS-IBGP-PEERS | Inherited from peer group MPLS-IBGP-PEERS | - | - | - | - | - |
| 192.168.255.2 | Inherited from peer group MPLS-IBGP-PEERS | default | - | Inherited from peer group MPLS-IBGP-PEERS | Inherited from peer group MPLS-IBGP-PEERS | - | - | - | - | - |

#### Router BGP VPN-IPv4 Address Family

##### VPN-IPv4 Neighbors

| Neighbor | Activate | Route-map In | Route-map Out |
| -------- | -------- | ------------ | ------------- |
| 192.168.255.4 | True | - | - |

##### VPN-IPv4 Peer Groups

| Peer Group | Activate | Route-map In | Route-map Out |
| ---------- | -------- | ------------ | ------------- |
| MPLS-IBGP-PEERS | True | - | - |

#### Router BGP VPN-IPv6 Address Family

##### VPN-IPv6 Neighbors

| Neighbor | Activate | Route-map In | Route-map Out |
| -------- | -------- | ------------ | ------------- |
| 192.168.255.4 | True | - | - |

##### VPN-IPv6 Peer Groups

| Peer Group | Activate | Route-map In | Route-map Out |
| ---------- | -------- | ------------ | ------------- |
| MPLS-IBGP-PEERS | True | - | - |

#### Router BGP Device Configuration

```eos
!
router bgp 65103
   router-id 192.168.255.3
   no bgp default ipv4-unicast
   distance bgp 20 200 200
   graceful-restart restart-time 300
   graceful-restart
   maximum-paths 2 ecmp 2
   neighbor MPLS-IBGP-PEERS peer group
   neighbor MPLS-IBGP-PEERS remote-as 65000
   neighbor MPLS-IBGP-PEERS local-as 65000 no-prepend replace-as
   neighbor MPLS-IBGP-PEERS password 7 mWV4B6WpLCfOTyKATLWuBg==
   neighbor MPLS-IBGP-PEERS send-community
   neighbor MPLS-IBGP-PEERS maximum-routes 0
   neighbor 192.168.255.1 peer group MPLS-IBGP-PEERS
   neighbor 192.168.255.2 peer group MPLS-IBGP-PEERS
   !
   address-family vpn-ipv4
      domain identifier 3900000
      neighbor MPLS-IBGP-PEERS activate
      neighbor 192.168.255.4 activate
      neighbor default encapsulation mpls next-hop-self source-interface Loopback0
   !
   address-family vpn-ipv6
      domain identifier 3900000
      neighbor MPLS-IBGP-PEERS activate
      neighbor 192.168.255.4 activate
      neighbor default encapsulation mpls next-hop-self source-interface Loopback0
```
