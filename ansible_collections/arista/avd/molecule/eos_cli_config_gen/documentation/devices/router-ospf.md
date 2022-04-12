# router-ospf
# Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [Authentication](#authentication)
- [Monitoring](#monitoring)
- [Internal VLAN Allocation Policy](#internal-vlan-allocation-policy)
  - [Internal VLAN Allocation Policy Summary](#internal-vlan-allocation-policy-summary)
- [Interfaces](#interfaces)
  - [Ethernet Interfaces](#ethernet-interfaces)
  - [Port-Channel Interfaces](#port-channel-interfaces)
  - [Loopback Interfaces](#loopback-interfaces)
  - [VLAN Interfaces](#vlan-interfaces)
- [Routing](#routing)
  - [IP Routing](#ip-routing)
  - [IPv6 Routing](#ipv6-routing)
  - [Router OSPF](#router-ospf)
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

## Ethernet Interfaces

### Ethernet Interfaces Summary

#### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | Channel-Group |
| --------- | ----------- | ---- | ----- | ----------- | ----------- | ------------- |

*Inherited from Port-Channel Interface

### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet1
   no switchport
   ip ospf cost 99
   ip ospf network point-to-point
   ip ospf authentication message-digest
   ip ospf area 0.0.0.1
   ip ospf message-digest-key 55 md5 7 ABCDEFGHIJKLMNOPQRSTUVWXYZ
```

## Port-Channel Interfaces

### Port-Channel Interfaces Summary

#### L2

| Interface | Description | Type | Mode | VLANs | Native VLAN | Trunk Group | LACP Fallback Timeout | LACP Fallback Mode | MLAG ID | EVPN ESI |
| --------- | ----------- | ---- | ---- | ----- | ----------- | ------------| --------------------- | ------------------ | ------- | -------- |

### Port-Channel Interfaces Device Configuration

```eos
!
interface Port-Channel12
   no switchport
   ip ospf network point-to-point
   ip ospf area 0.0.0.12
   ip ospf cost 99
   ip ospf authentication message-digest
   ip ospf message-digest-key 55 md5 7 ABCDEFGHIJKLMNOPQRSTUVWXYZ
```

## Loopback Interfaces

### Loopback Interfaces Summary

#### IPv4

| Interface | Description | VRF | IP Address |
| --------- | ----------- | --- | ---------- |
| Loopback2 | - | default | - |

#### IPv6

| Interface | Description | VRF | IPv6 Address |
| --------- | ----------- | --- | ------------ |
| Loopback2 | - | default | - |


### Loopback Interfaces Device Configuration

```eos
!
interface Loopback2
   ip ospf area 0.0.0.2
```

## VLAN Interfaces

### VLAN Interfaces Summary

| Interface | Description | VRF |  MTU | Shutdown |
| --------- | ----------- | --- | ---- | -------- |
| Vlan24 | - | default | - | - |

#### IPv4

| Interface | VRF | IP Address | IP Address Virtual | IP Router Virtual Address | VRRP | ACL In | ACL Out |
| --------- | --- | ---------- | ------------------ | ------------------------- | ---- | ------ | ------- |
| Vlan24 |  default  |  -  |  -  |  -  |  -  |  -  |  -  |

### VLAN Interfaces Device Configuration

```eos
!
interface Vlan24
   ip ospf network point-to-point
   ip ospf area 0.0.0.24
   ip ospf cost 99
   ip ospf authentication message-digest
   ip ospf message-digest-key 55 md5 7 ABCDEFGHIJKLMNOPQRSTUVWXYZ
```

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

## Router OSPF

### Router OSPF Summary

| Process ID | Router ID | Default Passive Interface | No Passive Interface | BFD | Max LSA | Default Information Originate | Log Adjacency Changes Detail | Auto Cost Reference Bandwidth | Maximum Paths | MPLS LDP Sync Default | Distribute List In |
| ---------- | --------- | ------------------------- | -------------------- | --- | ------- | ----------------------------- | ---------------------------- | ----------------------------- | ------------- | --------------------- | ------------------ |
| 100 | 192.168.255.3 | enabled | Ethernet1 <br> Ethernet2 <br> Vlan4093 <br> | enabled | 12000 | disabled | disabled | 100 | 10 | True | route-map RM-OSPF-DIST-IN |
| 101 | 1.0.1.1 | enabled | Ethernet2.101 <br> | disabled | default | disabled | enabled | - | - | - | - |
| 200 | 192.168.254.1 | disabled |- | disabled | 5 | Always | enabled | - | - | - | - |
| 300 | - | disabled |- | disabled | default | disabled | disabled | - | - | - | - |
| 400 | - | disabled |- | disabled | default | disabled | disabled | - | - | - | - |
| 500 | - | disabled |- | disabled | default | disabled | disabled | - | - | - | - |
| 600 | - | disabled |- | disabled | default | disabled | disabled | - | - | - | - |

### Router OSPF Distance

| Process ID | Intra Area | Inter Area | External |
| ---------- | ---------- | ---------- | -------- |
| 100 | 50 | 70 | 60 |

### Router OSPF Router Redistribution

| Process ID | Source Protocol | Route Map |
| ---------- | --------------- | --------- |
| 100 | connected | - |
| 100 | static | - |
| 100 | bgp | - |
| 200 | connected | rm-ospf-connected |
| 200 | static | rm-ospf-static |
| 200 | bgp | rm-ospf-bgp |

### Router OSPF Router Max-Metric

| Process ID | Router-LSA | External-LSA (metric) | Include Stub | On Startup Delay | Summary-LSA (metric) |
| ---------- | ---------- | --------------------- | ------------ | ---------------- | -------------------- |
| 300 | enabled | disabled | disabled | disabled | disabled |
| 400 | enabled | enabled | enabled | wait-for-bgp | enabled |
| 500 | enabled | enabled (123) | disabled | 222 | enabled (456) |

### Router OSPF timers

| Process ID | LSA rx | LSA tx (initial/min/max) | SPF (initial/min/max) |
| ---------- | ------ | ------------------------ | --------------------- |
| 101 | 100 | 100 / 200 / 300 | 100 / 200 / 300 |
| 200 | 100 | - | - |

### Router OSPF route summary

| Process ID | Prefix | Tag | Attribute Route Map | Not Advertised |
|------------|--------|-----|---------------------|----------------|
| 101 | 10.0.0.0/8 | - | - | - |
| 101 | 20.0.0.0/8 | 10 | - | - |
| 101 | 30.0.0.0/8 | - | RM-OSPF_SUMMARY | - |
| 101 | 40.0.0.0/8 | - | - | True |

### Router OSPF Areas

| Process ID | Area | Area Type | Filter Networks | Filter Prefix List | Additional Options |
| ---------- | ---- | --------- | --------------- | ------------------ | ------------------ |
| 200 | 0.0.0.2 | normal | 1.1.1.0/24, 2.2.2.0/24 | - |  |
| 200 | 0.0.0.3 | normal | - | PL-OSPF-FILTERING |  |
| 600 | 0.0.0.1 | normal | - | - |  |
| 600 | 0.0.10.11 | stub | - | - | no-summary |
| 600 | 0.0.20.20 | nssa | - | - |  |
| 600 | 0.0.20.21 | nssa | - | - | no-summary |
| 600 | 0.0.20.22 | nssa | - | - | nssa-only |
| 600 | 0.0.20.23 | nssa | - | - | default-information-originate |
| 600 | 0.0.20.24 | nssa | - | - | default-information-originate metric 50 |
| 600 | 0.0.20.25 | nssa | - | - | no-summary, default-information-originate metric-type 1 |
| 600 | 0.0.20.26 | nssa | - | - | no-summary, default-information-originate metric 50 metric-type 1, nssa-only |

### OSPF Interfaces

| Interface | Area | Cost | Point To Point |
| -------- | -------- | -------- | -------- |
| Ethernet1 | 0.0.0.1 | 99 | True |
| Port-Channel12 | 0.0.0.12 | 99 | True |
| Vlan24 | 0.0.0.24 | 99 | True |
| Loopback2 | 0.0.0.2 | - | - |

### Router OSPF Device Configuration

```eos
!
router ospf 100
   router-id 192.168.255.3
   distance ospf intra-area 50
   distance ospf external 60
   distance ospf inter-area 70
   passive-interface default
   no passive-interface Ethernet1
   no passive-interface Ethernet2
   no passive-interface Vlan4093
   network 198.51.100.0/24 area 0.0.0.1
   network 203.0.113.0/24 area 0.0.0.2
   bfd default
   distribute-list route-map RM-OSPF-DIST-IN in
   max-lsa 12000
   default-information originate
   redistribute static
   redistribute connected
   redistribute bgp
   auto-cost reference-bandwidth 100
   maximum-paths 10
   mpls ldp sync default
!
router ospf 101 vrf CUSTOMER01
   log-adjacency-changes detail
   router-id 1.0.1.1
   passive-interface default
   no passive-interface Ethernet2.101
   timers lsa rx min interval 100
   timers lsa tx delay initial 100 200 300
   timers spf delay initial 100 200 300
   summary-address 10.0.0.0/8
   summary-address 20.0.0.0/8 tag 10
   summary-address 30.0.0.0/8 attribute-map RM-OSPF_SUMMARY
   summary-address 40.0.0.0/8 not-advertise
!
router ospf 200 vrf ospf_zone
   log-adjacency-changes detail
   router-id 192.168.254.1
   area 0.0.0.2 filter 1.1.1.0/24
   area 0.0.0.2 filter 2.2.2.0/24
   area 0.0.0.3 filter prefix-list PL-OSPF-FILTERING
   max-lsa 5
   timers lsa rx min interval 100
   default-information originate always
   redistribute static route-map rm-ospf-static
   redistribute connected route-map rm-ospf-connected
   redistribute bgp route-map rm-ospf-bgp
!
router ospf 300
   max-metric router-lsa
!
router ospf 400
   max-metric router-lsa external-lsa include-stub on-startup wait-for-bgp summary-lsa
!
router ospf 500
   max-metric router-lsa external-lsa 123 on-startup 222 summary-lsa 456
!
router ospf 600
   area 0.0.10.11 stub no-summary
   area 0.0.20.20 nssa
   area 0.0.20.21 nssa no-summary
   area 0.0.20.22 nssa nssa-only
   area 0.0.20.23 nssa default-information-originate
   area 0.0.20.24 nssa default-information-originate metric 50
   area 0.0.20.25 nssa no-summary
   area 0.0.20.25 nssa default-information-originate metric-type 1
   area 0.0.20.26 nssa no-summary
   area 0.0.20.26 nssa default-information-originate metric 50 metric-type 1 nssa-only
```

# Multicast

# Filters

# ACL

# Quality Of Service
