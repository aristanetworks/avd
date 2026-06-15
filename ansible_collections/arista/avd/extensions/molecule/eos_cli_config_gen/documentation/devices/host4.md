# host4

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [Monitoring](#monitoring)
  - [TerminAttr Daemon](#terminattr-daemon)
- [Routing](#routing)
  - [IP Routing](#ip-routing)
  - [IPv6 Routing](#ipv6-routing)
  - [Router OSPF](#router-ospf)
  - [Router ISIS](#router-isis)
  - [Router BGP](#router-bgp)
- [MPLS](#mpls)
  - [MPLS and LDP](#mpls-and-ldp)
  - [MPLS Device Configuration](#mpls-device-configuration)
- [Multicast](#multicast)
  - [Router Multicast](#router-multicast)
- [VRF Instances](#vrf-instances)
  - [VRF Instances Summary](#vrf-instances-summary)
  - [VRF Instances Device Configuration](#vrf-instances-device-configuration)

## Management

### Management Interfaces

#### Management Interfaces Summary

##### IPv4

| Management Interface | Description | Type | VRF | IP Address | Gateway |
| -------------------- | ----------- | ---- | --- | ---------- | ------- |
| Management1 | OOB_MANAGEMENT | oob | MGMT | 10.73.255.122/24 | 10.73.255.2 |

##### IPv6

| Management Interface | Description | Type | VRF | IPv6 Address | IPv6 Gateway | ND RA Disabled | ND RA RX Accept | ND Managed Config Flag | ND Other Config Flag | ND Cache | ND RA DNS Servers |
| -------------------- | ----------- | ---- | --- | ------------ | ------------ | -------------- | --------------- | ---------------------- | -------------------- | -------- | ----------------- |
| Management1 | OOB_MANAGEMENT | oob | MGMT | - | - | - | - | - | - | - | - |

#### Management Interfaces Device Configuration

```eos
!
interface Management1
   description OOB_MANAGEMENT
   vrf MGMT
   ip address 10.73.255.122/24
```

## Monitoring

### TerminAttr Daemon

#### TerminAttr Daemon Summary

| CV Compression | CloudVision Servers | VRF | Authentication | Smash Excludes | Ingest Exclude | Bypass AAA |
| -------------- | ------------------- | --- | -------------- | -------------- | -------------- | ---------- |
| gzip | 10.10.10.8:9910,10.10.10.9:9910,10.10.10.10:9910 | mgt | certs,/persist/secure/ssl/terminattr/primary/certs/client.crt,/persist/secure/ssl/terminattr/primary/keys/client.key,/persist/secure/ssl/terminattr/primary/certs/ca.crt | ale,flexCounter,hardware,kni,pulse,strata | /Sysdb/cell/1/agent,/Sysdb/cell/2/agent | True |

#### TerminAttr Daemon Device Configuration

```eos
!
daemon TerminAttr
   exec /usr/bin/TerminAttr -cvaddr=10.10.10.8:9910,10.10.10.9:9910,10.10.10.10:9910 -cvauth=certs,/persist/secure/ssl/terminattr/primary/certs/client.crt,/persist/secure/ssl/terminattr/primary/keys/client.key,/persist/secure/ssl/terminattr/primary/certs/ca.crt -cvvrf=mgt -disableaaa -smashexcludes=ale,flexCounter,hardware,kni,pulse,strata -ingestexclude=/Sysdb/cell/1/agent,/Sysdb/cell/2/agent -taillogs
   no shutdown
```

## Routing

### IP Routing

#### IP Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | False |
| FUTURE_IPV4 | True |

#### IP Routing Device Configuration

```eos
!
ip routing vrf FUTURE_IPV4
```

### IPv6 Routing

#### IPv6 Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | False |
| FUTURE_IPV4 | false |

### Router OSPF

#### Router OSPF Summary

| Process ID | Router ID | Default Passive Interface | No Passive Interface | BFD | Max LSA | Default Information Originate | Log Adjacency Changes Detail | Auto Cost Reference Bandwidth | Maximum Paths | MPLS LDP Sync Default | Distribute List In |
| ---------- | --------- | ------------------------- | -------------------- | --- | ------- | ----------------------------- | ---------------------------- | ----------------------------- | ------------- | --------------------- | ------------------ |
| 703 | 10.255.0.4 | disabled | - | disabled | default | disabled | disabled | - | - | - | - |

#### Router OSPF Device Configuration

```eos
!
router ospf 703
   router-id 10.255.0.4
```

### Router ISIS

#### Router ISIS Summary

| Settings | Value |
| -------- | ----- |
| Instance | EVPN_UNDERLAY |

#### ISIS Interfaces Summary

| Interface | ISIS Instance | ISIS Metric | Interface Mode |
| --------- | ------------- | ----------- | -------------- |

#### Router ISIS Device Configuration

```eos
!
router isis EVPN_UNDERLAY
   authentication mode sha key-id 4 rx-disabled
   !
```

### Router BGP

ASN Notation: asplain

#### Router BGP Summary

| BGP AS | Router ID |
| ------ | --------- |
| 65001 | 192.168.255.3 |

| BGP AS | Cluster ID |
| ------ | --------- |
| 65001 | 192.0.2.44 |

| BGP Tuning |
| ---------- |
| graceful-restart-helper long-lived |
| bgp additional-paths send any |

#### Router BGP Peer Groups

##### PG-DOC-COVERAGE

| Settings | Value |
| -------- | ----- |
| Shutdown | True |
| Allowas-in | Allowed, allowed 2 times |
| Remote AS | 65044 |
| Route Reflector Client | Yes |
| Next-hop unchanged | True |
| Maximum routes | 100 (warning-limit 50) |
| Passive | True |

##### PG-VRF-DOC-COVERAGE

| Settings | Value |
| -------- | ----- |
| Allowas-in | Allowed, allowed 3 (default) times |
| Remote AS | 65045 |
| Route Reflector Client | Yes |

#### BGP Neighbors

| Neighbor | Remote AS | VRF | Shutdown | Send-community | Maximum-routes | Allowas-in | BFD | RIB Pre-Policy Retain | Route-Reflector Client | Passive | TTL Max Hops |
| -------- | --------- | --- | -------- | -------------- | -------------- | ---------- | --- | --------------------- | ---------------------- | ------- | ------------ |
| 192.0.2.100 | Inherited from peer group PG-DOC-COVERAGE | default | Inherited from peer group PG-DOC-COVERAGE | - | Inherited from peer group PG-DOC-COVERAGE | Inherited from peer group PG-DOC-COVERAGE | - | - | Inherited from peer group PG-DOC-COVERAGE | Inherited from peer group PG-DOC-COVERAGE | - |
| 192.0.2.101 | 65046 | default | - | - | 0 (no limit) | - | - | - | - | - | - |
| 192.0.2.102 | 65048 | default | - | - | 200 (warning-limit 100) | - | - | - | - | - | - |
| 192.0.2.10 | - | BGP_COVERAGE_IPV4 | - | - | - | - | - | True (All) | - | - | - |
| 192.0.2.11 | - | BGP_COVERAGE_IPV4 | - | - | - | - | - | - | - | - | - |
| 192.0.2.12 | - | BGP_COVERAGE_IPV4 | - | - | - | - | - | - | - | - | - |
| 192.0.2.14 | - | BGP_COVERAGE_IPV4 | - | - | - | - | - | - | - | - | - |
| 192.0.2.13 | Inherited from peer group PG-VRF-DOC-COVERAGE | BGP_COVERAGE_IPV4 | - | - | 300 (warning-limit 150) | Inherited from peer group PG-VRF-DOC-COVERAGE | - | - | Inherited from peer group PG-VRF-DOC-COVERAGE | - | - |

#### BGP Neighbor Interfaces

| Neighbor Interface | VRF | Peer Group | Remote AS | Peer Filter |
| ------------------ | --- | ---------- | --------- | ----------- |
| Ethernet41 | BGP_COVERAGE_IPV4 | PG-COVERAGE | 65041 | - |
| Ethernet42 | BGP_COVERAGE_IPV4 | PG-COVERAGE | - | PF-COVERAGE |

#### Router BGP EVPN Address Family

- Layer-2 In-place FEC update operation enabled

##### EVPN Host Flapping Settings

| State | Window | Threshold | Expiry Timeout |
| ----- | ------ | --------- | -------------- |
| Disabled | - | - | - |

#### Router BGP IPv4 Labeled Unicast

##### General Settings

| Settings | Value |
| -------- | ----- |

##### BGP LU RIB

| RIB | Enabled | Route-map |
| --- | ------- | --------- |
| Tunnel | True | RM-rib3 |

#### Router BGP Path-Selection Address Family

#### Router BGP VLAN Aware Bundles

| VLAN Aware Bundle | Route-Distinguisher | Both Route-Target | Import Route Target | Export Route-Target | Redistribute | VLANs |
| ----------------- | ------------------- | ----------------- | ------------------- | ------------------- | ------------ | ----- |
| BGP-COVERAGE-BUNDLE | 192.0.2.44:500 | 500:500<br>remote 500:501 | - | - | - | 500 |

#### Router BGP VLANs

| VLAN | Route-Distinguisher | Both Route-Target | Import Route Target | Export Route-Target | Redistribute |
| ---- | ------------------- | ----------------- | ------------------- | ------------------- | ------------ |
| 444 | 192.0.2.44:444 | 444:444<br>remote 444:445 | - | - | learned |

#### Router BGP VRFs

| VRF | Route-Distinguisher | Redistribute | Graceful Restart | EVPN Multicast |
| --- | ------------------- | ------------ | ---------------- | -------------- |
| BGP_COVERAGE_EVPN_MULTICAST | - | - | - | IPv4: True<br>Transit: False |
| BGP_COVERAGE_EVPN_MULTICAST_DEFAULT | - | - | - | IPv4: True<br>Transit: False |
| BGP_COVERAGE_IPV4 | - | - | - | IPv4: False<br>Transit: False |
| BGP_COVERAGE_IPV4_DISABLED | - | - | - | IPv4: False<br>Transit: False |
| BGP_COVERAGE_IPV6 | - | - | - | IPv4: False<br>Transit: False |
| BGP_COVERAGE_IPV6_ROUTE_MAP | - | - | - | IPv4: False<br>Transit: False |

#### Router BGP Device Configuration

```eos
!
router bgp 65001
   bgp labeled-unicast rib tunnel route-map RM-rib3
   router-id 192.168.255.3
   bgp cluster-id 192.0.2.44
   graceful-restart-helper long-lived
   bgp additional-paths send any
   neighbor PG-DOC-COVERAGE peer group
   neighbor PG-DOC-COVERAGE remote-as 65044
   neighbor PG-DOC-COVERAGE next-hop-unchanged
   neighbor PG-DOC-COVERAGE shutdown
   neighbor PG-DOC-COVERAGE passive
   neighbor PG-DOC-COVERAGE allowas-in 2
   neighbor PG-DOC-COVERAGE route-reflector-client
   neighbor PG-DOC-COVERAGE maximum-routes 100 warning-limit 50
   neighbor PG-VRF-DOC-COVERAGE peer group
   neighbor PG-VRF-DOC-COVERAGE remote-as 65045
   neighbor PG-VRF-DOC-COVERAGE allowas-in
   neighbor PG-VRF-DOC-COVERAGE route-reflector-client
   neighbor 192.0.2.100 peer group PG-DOC-COVERAGE
   neighbor 192.0.2.101 remote-as 65046
   neighbor 192.0.2.101 local-as 65047 no-prepend replace-as
   neighbor 192.0.2.101 update-source Loopback47
   neighbor 192.0.2.101 route-map RM-TOP-IN in
   neighbor 192.0.2.101 route-map RM-TOP-OUT out
   neighbor 192.0.2.101 maximum-routes 0
   neighbor 192.0.2.102 remote-as 65048
   neighbor 192.0.2.102 maximum-routes 200 warning-limit 100
   !
   vlan 444
      rd 192.0.2.44:444
      rd evpn domain remote 192.0.2.44:445
      route-target both 444:444
      route-target import export evpn domain remote 444:445
      redistribute learned
      !
      comment
      VLAN BGP coverage
   !
   vlan-aware-bundle BGP-COVERAGE-BUNDLE
      rd 192.0.2.44:500
      route-target both 500:500
      route-target import export evpn domain remote 500:501
      vlan 500
      !
      comment
      VLAN aware bundle BGP coverage
   !
   address-family evpn
      bgp additional-paths send any
      no host-flap detection
      layer-2 fec in-place update
   !
   address-family ipv4
      bgp additional-paths send ecmp
   !
   address-family ipv4 labeled-unicast
      bgp additional-paths send limit 10
   !
   address-family ipv6
      bgp additional-paths send limit 20
      neighbor 2001:db8:4::1 activate
      neighbor 2001:db8:4::1 additional-paths send any
   !
   address-family path-selection
      bgp additional-paths send any
   !
   vrf BGP_COVERAGE_EVPN_MULTICAST
      evpn multicast
         gateway dr election algorithm preference 100
   !
   vrf BGP_COVERAGE_EVPN_MULTICAST_DEFAULT
      evpn multicast
         gateway dr election algorithm modulus
   !
   vrf BGP_COVERAGE_IPV4
      neighbor 192.0.2.10 update-source Loopback10
      neighbor 192.0.2.10 rib-in pre-policy retain all
      neighbor 192.0.2.10 route-map RM-VRF-IN in
      no neighbor 192.0.2.11 additional-paths send
      neighbor 192.0.2.12 additional-paths send limit 11
      neighbor 192.0.2.12 peer-tag out discard PEER_TAG_DISCARD_OUT
      neighbor 192.0.2.13 peer group PG-VRF-DOC-COVERAGE
      neighbor 192.0.2.13 maximum-routes 300 warning-limit 150
      neighbor 192.0.2.14 additional-paths send any
      bgp redistribute-internal
      neighbor interface Ethernet41 peer-group PG-COVERAGE remote-as 65041
      neighbor interface Ethernet42 peer-group PG-COVERAGE peer-filter PF-COVERAGE
      !
      address-family ipv4
         bgp additional-paths send limit 12
         neighbor 192.0.2.20 additional-paths send ecmp limit 13
         neighbor 192.0.2.21 additional-paths send limit 14
         no bgp redistribute-internal
         redistribute connected route-map RM-CONNECTED
         redistribute dynamic rcf RCF_DYNAMIC()
         redistribute isis route-map RM-ISIS
         redistribute ospf match internal include leaked route-map RM-OSPF-INTERNAL
         redistribute ospfv3 include leaked route-map RM-OSPFV3
         redistribute static rcf RCF_STATIC()
      !
      address-family ipv4 multicast
         neighbor 192.0.2.30 activate
         redistribute isis rcf RCF-MCAST-ISIS()
         redistribute ospf route-map RM-MCAST-OSPF
         redistribute ospfv3 route-map RM-MCAST-OSPFV3
   !
   vrf BGP_COVERAGE_IPV4_DISABLED
      !
      address-family ipv4
         no bgp additional-paths send
   !
   vrf BGP_COVERAGE_IPV6
      !
      address-family ipv6
         no bgp additional-paths send
         neighbor 2001:db8::20 additional-paths send ecmp limit 15
         neighbor 2001:db8::21 additional-paths send limit 16
         no bgp redistribute-internal
         redistribute attached-host route-map RM-V6-HOST
         redistribute bgp leaked route-map RM-V6-BGP
         redistribute dhcp route-map RM-V6-DHCP
         redistribute connected include leaked route-map RM-V6-CONNECTED
         redistribute dynamic rcf RCF_V6_DYNAMIC()
         redistribute user
         redistribute isis include leaked rcf RCF_V6_ISIS()
         redistribute ospfv3 include leaked route-map RM-V6-OSPFV3
         redistribute ospfv3 match nssa-external 1 include leaked route-map RM-V6-OSPFV3-NSSA
         redistribute static include leaked rcf RCF_V6_STATIC()
      !
      address-family ipv6 multicast
         neighbor 2001:db8::30 activate
         neighbor 2001:db8::30 route-map RM-V6MCAST-OUT out
         neighbor 2001:db8::30 peer-tag in PEER_TAG_IN_V6MCAST
         neighbor 2001:db8::30 peer-tag out discard PEER_TAG_OUT_V6MCAST
         network ff08:2::/64 route-map RM-V6MCAST-NETWORK
         redistribute isis rcf RCF-V6MCAST-ISIS()
         redistribute ospf match internal route-map RM-V6MCAST-OSPF-INTERNAL
         redistribute ospfv3 route-map RM-V6MCAST-OSPFV3
   !
   vrf BGP_COVERAGE_IPV6_ROUTE_MAP
      !
      address-family ipv6
         redistribute dynamic route-map RM-V6-DYNAMIC
         redistribute isis route-map RM-V6-ISIS
```

## MPLS

### MPLS and LDP

#### MPLS and LDP Summary

| Setting | Value |
| -------- | ---- |
| MPLS IP Enabled | - |
| LDP Enabled | False |
| LDP Router ID | - |
| LDP Interface Disabled Default | - |
| LDP Transport-Address Interface | - |

### MPLS Device Configuration

```eos
!
mpls rsvp
```

## Multicast

### Router Multicast

#### IP Router Multicast Summary

- Multipathing disabled.

#### Router Multicast Device Configuration

```eos
!
router multicast
   ipv4
      multipath none
```

## VRF Instances

### VRF Instances Summary

| VRF Name | IP Routing |
| -------- | ---------- |
| FUTURE_IPV4 | enabled |

### VRF Instances Device Configuration

```eos
!
vrf instance FUTURE_IPV4
```
