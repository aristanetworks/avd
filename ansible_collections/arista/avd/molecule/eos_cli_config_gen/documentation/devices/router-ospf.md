# router-ospf
# Table of Contents
<!-- toc -->

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
  - [Router OSPF](#router-ospf)
  - [Router BFD](#router-bfd)
- [Multicast](#multicast)
- [Filters](#filters)
- [ACL](#acl)

<!-- toc -->
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
| default | false|
### IP Routing Device Configuration

```eos
```
## IPv6 Routing

### IPv6 Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | false |

## Router OSPF

### Router OSPF Summary

| Process ID | Router ID | Default Passive Interface | No Passive Interface | BFD | Max LSA | Default Information Originate | Log Adjacency Changes Detail | Auto Cost Reference Bandwidth | Maximum Paths | MPLS LDP Sync Default |
| ---------- | --------- | ------------------------- | -------------------- | --- | ------- | ----------------------------- | ---------------------------- | ----------------------------- | ------------- | --------------------- |
| 100 | 192.168.255.3 | enabled |  Ethernet1 <br> Ethernet2 <br> Vlan4093 <br> | enabled | 12000 | disabled | disabled | 100 | 10 | True |
| 200 | 192.168.254.1 | disabled | - | disabled | 5 | Always | enabled | - | - | - |
| 300 | - | disabled | - | disabled | default | disabled | disabled | - | - | - |
| 400 | - | disabled | - | disabled | default | disabled | disabled | - | - | - |
| 500 | - | disabled | - | disabled | default | disabled | disabled | - | - | - |


### Router OSPF Router Redistribution

| Process ID | Redistribute Connected | Redistribute Connected Route-map | Redistribute Static | Redistribute Static Route-map |
| ---------- | ---------------------- | -------------------------------- | ------------------- | ----------------------------- |
| 100 | enabled| - | enabled | - |
| 200 | enabled| rm-ospf-connected | enabled | rm-ospf-static |

### Router OSPF Router Max-Metric

| Process ID | Router-LSA | External-LSA (metric) | Include Stub | On Startup Delay | Summary-LSA (metric) |
| ---------- | ---------- | --------------------- | ------------ | ---------------- | -------------------- |
| 300 | enabled | disabled | disabled | disabled | disabled |
| 400 | enabled | enabled | enabled | wait-for-bgp | enabled |
| 500 | enabled | enabled (123) | disabled | 222 | enabled (456) |

### Router OSPF Device Configuration

```eos
!
router ospf 100
   router-id 192.168.255.3
   passive-interface default
   no passive-interface Ethernet1
   no passive-interface Ethernet2
   no passive-interface Vlan4093
   bfd default
   max-lsa 12000
   default-information originate
   redistribute static
   redistribute connected
   auto-cost reference-bandwidth 100
   maximum-paths 10
   mpls ldp sync default
!
router ospf 200 vrf ospf_zone
   log-adjacency-changes detail
   router-id 192.168.254.1
   max-lsa 5
   default-information originate always
   redistribute static route-map rm-ospf-static
   redistribute connected route-map rm-ospf-connected
!
router ospf 300
   max-metric router-lsa
!
router ospf 400
   max-metric router-lsa external-lsa include-stub on-startup wait-for-bgp summary-lsa
!
router ospf 500
   max-metric router-lsa external-lsa 123 on-startup 222 summary-lsa 456
```

## Router BFD

### Router BFD Multihop Summary

| Interval | Minimum RX | Multiplier |
| -------- | ---------- | ---------- |
| 300 | 300 | 3 |

*No device configuration required - default values

# Multicast

# Filters

# ACL
