# router-bgp-evpn
# Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [Authentication](#authentication)
- [Monitoring](#monitoring)
- [Internal VLAN Allocation Policy](#internal-vlan-allocation-policy)
  - [Internal VLAN Allocation Policy Summary](#internal-vlan-allocation-policy-summary)
- [Interfaces](#interfaces)
- [Routing](#routing)
  - [IP Routing](#ip-routing)
  - [IPv6 Routing](#ipv6-routing)
  - [Router BGP](#router-bgp)
- [Multicast](#multicast)
- [Filters](#filters)
- [ACL](#acl)
- [Quality Of Service](#quality-of-service)

# Management

## Management Interfaces

### Management Interfaces Summary

#### IPv4

| Management Interface | description | Type | VRF | IP Address | Gateway |
| -------------------- | ----------- | ---- | --- | ---------- | ------- |
| Management1 | oob_management | oob | MGMT | 10.73.255.122/24 | 10.73.255.2 |

#### IPv6

| Management Interface | description | Type | VRF | IPv6 Address | IPv6 Gateway |
| -------------------- | ----------- | ---- | --- | ------------ | ------------ |
| Management1 | oob_management | oob | MGMT | -  | - |

### Management Interfaces Device Configuration

```eos
!
interface Management1
   description oob_management
   vrf MGMT
   ip address 10.73.255.122/24
```

# Authentication

# Monitoring

# Internal VLAN Allocation Policy

## Internal VLAN Allocation Policy Summary

**Default Allocation Policy**

| Policy Allocation | Range Beginning | Range Ending |
| ------------------| --------------- | ------------ |
| ascending | 1006 | 4094 |

# Interfaces

# Routing

## IP Routing

### IP Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | false |

### IP Routing Device Configuration

```eos
```
## IPv6 Routing

### IPv6 Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | false |

## Router BGP

### Router BGP Summary

| BGP AS | Router ID |
| ------ | --------- |
| 65101|  192.168.255.3 |

| BGP Tuning |
| ---------- |
| no bgp default ipv4-unicast |
| distance bgp 20 200 200 |
| graceful-restart restart-time 300 |
| graceful-restart |
| maximum-paths 2 ecmp 2 |

### Router BGP Peer Groups

#### EVPN-OVERLAY-PEERS

| Settings | Value |
| -------- | ----- |
| Address Family | evpn |
| Allowas-in | Allowed, allowed 3 (default) times |
| Remote AS | 65001 |
| Source | Loopback0 |
| BFD | True |
| Ebgp multihop | 3 |
| Send community | all |
| Maximum routes | 0 (no limit) |

#### MLAG-IPv4-UNDERLAY-PEER

| Settings | Value |
| -------- | ----- |
| Address Family | ipv4 |
| Remote AS | 65101 |
| Next-hop self | True |
| Send community | all |
| Maximum routes | 12000 (warning-limit 80 percent, warning-only) |

### BGP Neighbors

| Neighbor | Remote AS | VRF | Shutdown | Send-community | Maximum-routes | Allowas-in | BFD | RIB Pre-Policy Retain |
| -------- | --------- | --- | -------- | -------------- | -------------- | ---------- | --- | --------------------- |
| 192.168.255.1 | Inherited from peer group EVPN-OVERLAY-PEERS | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | Allowed, allowed 5 times | Inherited from peer group EVPN-OVERLAY-PEERS | - |
| 192.168.255.2 | Inherited from peer group EVPN-OVERLAY-PEERS | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - |
| 192.168.255.3 | - | default | - | - | 52000 (warning-limit 2000, warning-only) | Allowed, allowed 5 times | - | - |
| 10.255.251.1 | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | TENANT_A_PROJECT01 | - | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | 15000 (warning-limit 50 percent) | - | - | - |
| 10.255.251.1 | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | TENANT_A_PROJECT02 | - | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | - | - | - |

### BGP Neighbor Interfaces

| Neighbor Interface | VRF | Peer Group | Remote AS | Peer Filter |
| ------------------ | --- | ---------- | --------- | ----------- |
| Ethernet27 | TENANT_A_PROJECT02 | MLAG-IPv4-UNDERLAY-PEER | 1 | - |
| Ethernet28 | TENANT_A_PROJECT02 | MLAG-IPv4-UNDERLAY-PEER | - | SOME_FILTER |

### Router BGP EVPN Address Family

#### EVPN Peer Groups

| Peer Group | Activate |
| ---------- | -------- |
| EVPN-OVERLAY-PEERS | True |
| MLAG-IPv4-UNDERLAY-PEER | False |

#### EVPN Host Flapping Settings

| State | Window | Threshold | Expiry Timeout |
| ----- | ------ | --------- | -------------- |
| Enabled | 10 Seconds | 1 | 3 Seconds |

#### EVPN DCI Gateway Summary

| Settings | Value |
| -------- | ----- |
| Remote Domain Peer Groups | EVPN-OVERLAY-PEERS |
| L3 Gateway Configured | True |
| L3 Gateway Inter-domain | True |

### Router BGP VLAN Aware Bundles

| VLAN Aware Bundle | Route-Distinguisher | Both Route-Target | Import Route Target | Export Route-Target | Redistribute | VLANs |
| ----------------- | ------------------- | ----------------- | ------------------- | ------------------- | ------------ | ----- |
| B-ELAN-201 | 192.168.255.3:20201 | 20201:20201 | - | - | learned<br>no host-routes | 201 |
| TENANT_A_PROJECT01 | 192.168.255.3:11 | 11:11<br>remote 2:11 | - | - | learned<br>igmp<br>no connected | 110 |
| TENANT_A_PROJECT02 | 192.168.255.3:12 | 12:12 | remote 2:12 | remote 2:12 | learned | 112 |

### Router BGP VLANs

| VLAN | Route-Distinguisher | Both Route-Target | Import Route Target | Export Route-Target | Redistribute |
| ---- | ------------------- | ----------------- | ------------------- | ------------------- | ------------ |
| 2488 | 145.245.21.0:1 | 145.245.21.0:1 | - | - | no learned |

### Router BGP VRFs

| VRF | Route-Distinguisher | Redistribute |
| --- | ------------------- | ------------ |
| TENANT_A_PROJECT01 | 192.168.255.3:11 | connected |
| TENANT_A_PROJECT02 | 192.168.255.3:12 | connected |

### Router BGP Device Configuration

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
   neighbor EVPN-OVERLAY-PEERS allowas-in
   neighbor EVPN-OVERLAY-PEERS ebgp-multihop 3
   neighbor EVPN-OVERLAY-PEERS password 7 q+VNViP5i4rVjW1cxFv2wA==
   neighbor EVPN-OVERLAY-PEERS send-community
   neighbor EVPN-OVERLAY-PEERS maximum-routes 0
   neighbor MLAG-IPv4-UNDERLAY-PEER peer group
   neighbor MLAG-IPv4-UNDERLAY-PEER remote-as 65101
   neighbor MLAG-IPv4-UNDERLAY-PEER next-hop-self
   neighbor MLAG-IPv4-UNDERLAY-PEER password 7 vnEaG8gMeQf3d3cN6PktXQ==
   neighbor MLAG-IPv4-UNDERLAY-PEER send-community
   neighbor MLAG-IPv4-UNDERLAY-PEER maximum-routes 12000 warning-limit 80 percent warning-only
   neighbor MLAG-IPv4-UNDERLAY-PEER route-map RM-MLAG-PEER-IN in
   neighbor MLAG-IPv4-UNDERLAY-PEER route-map RM-MLAG-PEER-OUT out
   neighbor 192.168.255.1 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.255.1 allowas-in 5
   neighbor 192.168.255.2 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.255.3 allowas-in 5
   neighbor 192.168.255.3 maximum-routes 52000 warning-limit 2000 warning-only
   !
   vlan 2488
      rd 145.245.21.0:1
      route-target both 145.245.21.0:1
      no redistribute learned
   !
   vlan-aware-bundle B-ELAN-201
      rd 192.168.255.3:20201
      route-target both 20201:20201
      redistribute learned
      no redistribute host-routes
      vlan 201
   !
   vlan-aware-bundle TENANT_A_PROJECT01
      rd 192.168.255.3:11
      route-target both 11:11
      route-target import export evpn domain remote 2:11
      redistribute igmp
      redistribute learned
      no redistribute connected
      vlan 110
   !
   vlan-aware-bundle TENANT_A_PROJECT02
      rd 192.168.255.3:12
      rd evpn domain remote 192.168.255.3:12
      route-target both 12:12
      route-target import evpn domain remote 2:12
      route-target export evpn domain remote 2:12
      redistribute learned
      vlan 112
   !
   address-family evpn
      host-flap detection window 10 threshold 1 expiry timeout 3 seconds
      domain identifier 65101:0
      neighbor EVPN-OVERLAY-PEERS activate
      neighbor EVPN-OVERLAY-PEERS domain remote
      no neighbor MLAG-IPv4-UNDERLAY-PEER activate
      neighbor default next-hop-self received-evpn-routes route-type ip-prefix inter-domain
   !
   address-family ipv4
      no neighbor EVPN-OVERLAY-PEERS activate
   !
   vrf TENANT_A_PROJECT01
      rd 192.168.255.3:11
      evpn multicast
      route-target import evpn 11:11
      route-target export evpn 11:11
      router-id 192.168.255.3
      neighbor 10.255.251.1 peer group MLAG-IPv4-UNDERLAY-PEER
      neighbor 10.255.251.1 maximum-routes 15000 warning-limit 50 percent
      redistribute connected
   !
   vrf TENANT_A_PROJECT02
      rd 192.168.255.3:12
      route-target import evpn 12:12
      route-target export evpn 12:12
      router-id 192.168.255.3
      neighbor interface Ethernet27 peer-group MLAG-IPv4-UNDERLAY-PEER remote-as 1
      neighbor interface Ethernet28 peer-group MLAG-IPv4-UNDERLAY-PEER peer-filter SOME_FILTER
      neighbor 10.255.251.1 peer group MLAG-IPv4-UNDERLAY-PEER
      redistribute connected
```

# Multicast

# Filters

# ACL

# Quality Of Service
