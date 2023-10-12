# router-bgp-evpn-route-server

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
| 65000 | 192.168.255.1 |

| BGP Tuning |
| ---------- |
| timers bgp 5 15 |
| bgp asn notation asdot |
| graceful-restart restart-time 300 |
| graceful-restart |
| update wait-for-convergence |
| update wait-install |
| bgp default ipv4-unicast |
| distance bgp 20 200 200 |
| maximum-paths 128 |

#### Router BGP Listen Ranges

| Prefix | Peer-ID Include Router ID | Peer Group | Peer-Filter | Remote-AS | VRF |
| ------ | ------------------------- | ---------- | ----------- | --------- | --- |
| 192.168.255.0/26 | - | EVPN-OVERLAY-PEERS | PF_AS_LEAVES | - | default |
| 192.168.0.0/24 | - | IPV4-UNDERLAY-PEERS | PF_AS_LEAVES | - | default |

#### Router BGP Peer Groups

##### EVPN-OVERLAY-PEERS

| Settings | Value |
| -------- | ----- |
| Address Family | evpn |
| Source | Loopback0 |
| BFD | True |
| Ebgp multihop | 2 |
| Send community | all |
| Maximum routes | 0 (no limit) |

##### IPV4-UNDERLAY-PEERS

| Settings | Value |
| -------- | ----- |
| Address Family | ipv4 |
| Send community | all |
| Maximum routes | 12000 (warning-only) |

#### Router BGP EVPN Address Family
- Next-hop-unchanged is explicitly configured (default behaviour)

##### EVPN Peer Groups

| Peer Group | Activate | Encapsulation |
| ---------- | -------- | ------------- |
| EVPN-OVERLAY-PEERS | True | default |

#### Router BGP Device Configuration

```eos
!
router bgp 65000
   router-id 192.168.255.1
   distance bgp 20 200 200
   graceful-restart restart-time 300
   graceful-restart
   maximum-paths 128
   update wait-for-convergence
   update wait-install
   bgp default ipv4-unicast
   timers bgp 5 15
   bgp asn notation asdot
   bgp listen range 192.168.255.0/26 peer-group EVPN-OVERLAY-PEERS peer-filter PF_AS_LEAVES
   bgp listen range 192.168.0.0/24 peer-group IPV4-UNDERLAY-PEERS peer-filter PF_AS_LEAVES
   neighbor EVPN-OVERLAY-PEERS peer group
   neighbor EVPN-OVERLAY-PEERS update-source Loopback0
   neighbor EVPN-OVERLAY-PEERS bfd
   neighbor EVPN-OVERLAY-PEERS ebgp-multihop 2
   neighbor EVPN-OVERLAY-PEERS password 7 <removed>
   neighbor EVPN-OVERLAY-PEERS send-community
   neighbor EVPN-OVERLAY-PEERS maximum-routes 0
   neighbor IPV4-UNDERLAY-PEERS peer group
   neighbor IPV4-UNDERLAY-PEERS password 7 <removed>
   neighbor IPV4-UNDERLAY-PEERS send-community
   neighbor IPV4-UNDERLAY-PEERS maximum-routes 12000 warning-only
   redistribute connected route-map RM_LOOPBACKS
   !
   address-family evpn
      neighbor EVPN-OVERLAY-PEERS activate
      bgp next-hop-unchanged
   !
   address-family rt-membership
      neighbor EVPN-OVERLAY-PEERS activate
   !
   address-family ipv4
      no neighbor EVPN-OVERLAY-PEERS activate
```
