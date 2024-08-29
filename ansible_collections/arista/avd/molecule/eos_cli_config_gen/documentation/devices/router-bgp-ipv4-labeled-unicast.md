# router-bgp-ipv4-labeled-unicast

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [Routing](#routing)
  - [Router BGP](#router-bgp)

## Management

### Management Interfaces

#### Management Interfaces Summary

##### IPv4

| Management Interface | Description | Type | VRF | IP Address | Gateway |
| -------------------- | ----------- | ---- | --- | ---------- | ------- |
| Management1 | oob_management | oob | MGMT | 10.73.255.122/24 | 10.73.255.2 |

##### IPv6

| Management Interface | Description | Type | VRF | IPv6 Address | IPv6 Gateway |
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

ASN Notation: asplain

#### Router BGP Summary

| BGP AS | Router ID |
| ------ | --------- |
| 65101 | 192.168.255.3 |

| BGP Tuning |
| ---------- |
| no bgp default ipv4-unicast |
| distance bgp 20 200 200 |
| graceful-restart restart-time 300 |
| graceful-restart |
| maximum-paths 2 ecmp 2 |

#### Router BGP Peer Groups

##### EVPN-OVERLAY-PEERS

| Settings | Value |
| -------- | ----- |
| Address Family | evpn |
| Remote AS | 65001 |
| Source | Loopback0 |
| RIB Pre-Policy Retain | True (All) |
| BFD | True |
| Ebgp multihop | 3 |
| Default originate | True |
| Send community | all |
| Maximum routes | 0 (no limit) |

##### MLAG-IPv4-UNDERLAY-PEER

| Settings | Value |
| -------- | ----- |
| Address Family | ipv4 |
| Remote AS | 65101 |

##### PG-BGP-LU

| Settings | Value |
| -------- | ----- |
| Address Family | IPv4 Labeled-Unicast |
| Remote AS | 65555 |
| Source | Loopback0 |

#### BGP Neighbors

| Neighbor | Remote AS | VRF | Shutdown | Send-community | Maximum-routes | Allowas-in | BFD | RIB Pre-Policy Retain | Route-Reflector Client | Passive | TTL Max Hops |
| -------- | --------- | --- | -------- | -------------- | -------------- | ---------- | --- | --------------------- | ---------------------- | ------- | ------------ |
| 192.168.255.1 | Inherited from peer group EVPN-OVERLAY-PEERS | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - |
| 192.168.255.2 | Inherited from peer group EVPN-OVERLAY-PEERS | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - |
| 198.51.100.3 | Inherited from peer group PG-BGP-LU | default | - | - | - | - | - | - | - | - | - |

#### Router BGP IPv4 Labeled Unicast

##### General Settings

| Settings | Value |
| -------- | ----- |
| Update - wait-for-convergence | Enabled |
| Next-hop Unchanged | True |
| label local-termination | implicit-null |
##### IPv4 BGP-LU Peer-groups

| Peer-group | Activate | Route-map In | Route-map Out | RCF In | RCF Out |
| ---------- | -------- | ------------ | ------------- | ------ | ------- |
| PG-BGP-LU | True | - | - | - | - |
##### IPv4 BGP-LU Neighbors

| Neighbor | Activate | Route-map In | Route-map Out | RCF In | RCF Out |
| -------- | -------- | ------------ | ------------- | ------ | ------- |
| 198.51.100.1 | True | - | - | RCF_TEST(ARGS) | - |
| 198.51.100.2 | False | - | RM_OUT_TEST | - | - |

#### Router BGP Device Configuration

```eos
!
router bgp 65101
   router-id 192.168.255.3
   no bgp default ipv4-unicast
   distance bgp 20 200 200
   graceful-restart restart-time 300
   graceful-restart
   maximum-paths 2 ecmp 2
   neighbor EVPN-OVERLAY-PEERS peer group
   neighbor EVPN-OVERLAY-PEERS remote-as 65001
   neighbor EVPN-OVERLAY-PEERS update-source Loopback0
   neighbor EVPN-OVERLAY-PEERS bfd
   neighbor EVPN-OVERLAY-PEERS rib-in pre-policy retain all
   neighbor EVPN-OVERLAY-PEERS ebgp-multihop 3
   neighbor EVPN-OVERLAY-PEERS password 7 <removed>
   neighbor EVPN-OVERLAY-PEERS default-originate route-map RM-FOO always
   neighbor EVPN-OVERLAY-PEERS send-community
   neighbor EVPN-OVERLAY-PEERS maximum-routes 0
   neighbor MLAG-IPv4-UNDERLAY-PEER peer group
   neighbor MLAG-IPv4-UNDERLAY-PEER remote-as 65101
   neighbor PG-BGP-LU peer group
   neighbor PG-BGP-LU remote-as 65555
   neighbor PG-BGP-LU update-source Loopback0
   neighbor 192.168.255.1 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.255.2 peer group EVPN-OVERLAY-PEERS
   neighbor 198.51.100.3 peer group PG-BGP-LU
   !
   address-family ipv4 labeled-unicast
      update wait-for-convergence
      bgp missing-policy direction in action deny
      bgp additional-paths receive
      bgp additional-paths send ecmp
      bgp next-hop-unchanged
      neighbor PG-BGP-LU activate
      neighbor 198.51.100.1 activate
      neighbor 198.51.100.1 additional-paths receive
      neighbor 198.51.100.1 rcf in RCF_TEST(ARGS)
      neighbor 198.51.100.1 graceful-restart
      neighbor 198.51.100.1 additional-paths send ecmp
      neighbor 198.51.100.1 maximum-routes 0
      no neighbor 198.51.100.2 activate
      neighbor 198.51.100.2 route-map RM_OUT_TEST out
      neighbor 198.51.100.2 graceful-restart-helper stale-route route-map RM_STALE
      neighbor 198.51.100.2 next-hop-unchanged
      neighbor 198.51.100.2 aigp-session
      neighbor 198.51.100.2 multi-path
      network 203.0.113.0/25 route-map RM-TEST
      network 203.0.113.128/25
      label local-termination implicit-null
      tunnel source-protocol isis segment-routing
      tunnel source-protocol ldp rcf TEST(ARGS)
      aigp-session confederation
      aigp-session ebgp
```
