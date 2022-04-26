# router-bgp-vpn-ipv4-vpn-ipv6
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
| 65103|  192.168.255.3 |

| BGP Tuning |
| ---------- |
| no bgp default ipv4-unicast |
| distance bgp 20 200 200 |
| graceful-restart restart-time 300 |
| graceful-restart |
| maximum-paths 2 ecmp 2 |

### Router BGP Peer Groups

#### MPLS-IBGP-PEERS

| Settings | Value |
| -------- | ----- |
| Address Family | vpn-ipv4, vpn-ipv6 |
| Remote AS | 65000 |
| Local AS | 65000 |
| Send community | all |
| Maximum routes | 0 (no limit) |

### BGP Neighbors

| Neighbor | Remote AS | VRF | Shutdown | Send-community | Maximum-routes | Allowas-in | BFD | RIB Pre-Policy Retain |
| -------- | --------- | --- | -------- | -------------- | -------------- | ---------- | --- | --------------------- |
| 192.168.255.1 | Inherited from peer group MPLS-IBGP-PEERS | default | - | Inherited from peer group MPLS-IBGP-PEERS | Inherited from peer group MPLS-IBGP-PEERS | - | - | - |
| 192.168.255.2 | Inherited from peer group MPLS-IBGP-PEERS | default | - | Inherited from peer group MPLS-IBGP-PEERS | Inherited from peer group MPLS-IBGP-PEERS | - | - | - |

### Router BGP Device Configuration

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
   neighbor MPLS-IBGP-PEERS password 7 AQQvKeimxJu+uGQ/yYvv9w==
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

# Multicast

# Filters

# ACL

# Quality Of Service
