# traffic-policies
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
- [Routing](#routing)
  - [IP Routing](#ip-routing)
  - [IPv6 Routing](#ipv6-routing)
- [Multicast](#multicast)
- [Filters](#filters)
- [ACL](#acl)
  - [Traffic Policies information](#traffic-policies-information)
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
   traffic-policy input BLUE-C1-POLICY
   traffic-policy output BLUE-C2-POLICY
```

## Port-Channel Interfaces

### Port-Channel Interfaces Summary

#### L2

| Interface | Description | Type | Mode | VLANs | Native VLAN | Trunk Group | LACP Fallback Timeout | LACP Fallback Mode | MLAG ID | EVPN ESI |
| --------- | ----------- | ---- | ---- | ----- | ----------- | ------------| --------------------- | ------------------ | ------- | -------- |

### Port-Channel Interfaces Device Configuration

```eos
!
interface Port-Channel2
   no switchport
   traffic-policy input BLUE-C1-POLICY
   traffic-policy output BLUE-C2-POLICY
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

# Multicast

# Filters

# ACL

## Traffic Policies information

**IPv4 Field sets**

| Field Set Name | Values |
| -------------- | ------ |
| DEMO-01 | 10.0.0.0/8<br/>192.168.0.0/16 |
| DEMO-02 | 172.16.0.0/12<br/>224.0.0.0/8 |

**IPv6 Field sets**

No IPv6 field-set configured.

**L4 Port Field sets**

| Field Set Name | Values |
| -------------- | ------ |
| SERVICE-DEMO | 10,20,80,440-450|

### Traffic Policies

**BLUE-C1-POLICY:**

| Match set | Type | Sources | Destinations | Protocol | Source Port(s) | Destination port(s) | Action |
| --------- | ---- | ------- | ------------ | -------- | -------------- | ------------------- | ------ |
| BLUE-C1-POLICY-01 | ipv4 | 10.0.0.0/8<br/>192.168.0.0/16 | DEMO-01 | tcp | 1,10-20 | ANY | action: PASS<br/>traffic-class: 5 |
| BLUE-C1-POLICY-02 | ipv4 | DEMO-01<br/>DEMO-02 | ANY | tcp<br/>icmp | ANY | SERVICE-DEMO | action: PASS<br/>counter: DEMO-TRAFFIC<br/>dscp marking: 60 |
| BLUE-C1-POLICY-03 | ipv4 | DEMO-01 | ANY | icmp | ANY | ANY | action: DROP<br/>counter: DROP-PACKETS<br/>logging |
| BLUE-C1-POLICY-04 | ipv4 | DEMO-02 | DEMO-01 | tcp<br/>icmp | 22 | ANY | action: PASS<br/>traffic-class: 5 |
| BLUE-C1-POLICY-05 | ipv4 | DEMO-02 | DEMO-01 | tcp | ANY | ANY | action: PASS<br/>traffic-class: 5 |


**BLUE-C2-POLICY:**

| Match set | Type | Sources | Destinations | Protocol | Source Port(s) | Destination port(s) | Action |
| --------- | ---- | ------- | ------------ | -------- | -------------- | ------------------- | ------ |
| BLUE-C2-POLICY-01 | ipv4 | 10.0.0.0/8<br/>192.168.0.0/16 | ANY | tcp<br/>icmp | 1,10-20 | ANY | action: PASS<br/>traffic-class: 5 |
| BLUE-C2-POLICY-02 | ipv4 | DEMO-01<br/>DEMO-02 | ANY | tcp<br/>icmp | SERVICE-DEMO | ANY | action: PASS<br/>counter: DEMO-TRAFFIC<br/>dscp marking: 60 |
| BLUE-C2-POLICY-03 | ipv4 | DEMO-01 | ANY | tcp | ANY | ANY | action: DROP<br/>logging |


#### Traffic-Policy Interfaces

| Interface | Input Traffic-Policy | Output Traffic-Policy |
| --------- | -------------------- | --------------------- |
| Ethernet1 | BLUE-C1-POLICY | BLUE-C2-POLICY |
| Port-Channel2 | BLUE-C1-POLICY | BLUE-C2-POLICY |

### Traffic Policies Device Configuration

```eos
!
traffic-policies
   counter interface per-interface ingress
   field-set ipv4 prefix DEMO-01
      10.0.0.0/8 192.168.0.0/16
   !
   field-set ipv4 prefix DEMO-02
      172.16.0.0/12 224.0.0.0/8
   !
   field-set l4-port SERVICE-DEMO
      10,20,80,440-450
   !
   traffic-policy BLUE-C1-POLICY
      counter DEMO-TRAFFIC DROP-PACKETS
      match BLUE-C1-POLICY-01 ipv4
         source prefix 10.0.0.0/8 192.168.0.0/16
         destination prefix field-set DEMO-01
         protocol tcp source port 1,10-20
         ttl 10, 20-30
         actions
            set traffic class 5
         !
      !
      match BLUE-C1-POLICY-02 ipv4
         source prefix field-set DEMO-01 DEMO-02
         protocol tcp flags established destination port field-set SERVICE-DEMO
         protocol icmp
         actions
            count DEMO-TRAFFIC
            set dscp 60
         !
      !
      match BLUE-C1-POLICY-03 ipv4
         source prefix field-set DEMO-01
         protocol icmp
         fragment offset 1124, 2000-2010
         actions
            count DROP-PACKETS
            drop
            log
         !
      !
      match BLUE-C1-POLICY-04 ipv4
         source prefix field-set DEMO-02
         destination prefix field-set DEMO-01
         protocol tcp flags established source port 22
         protocol icmp
         actions
            set traffic class 5
         !
      !
      match BLUE-C1-POLICY-05 ipv4
         source prefix field-set DEMO-02
         destination prefix field-set DEMO-01
         protocol tcp
         fragment
         actions
            set traffic class 5
         !
      !
   !
   traffic-policy BLUE-C2-POLICY
      counter DEMO-TRAFFIC
      match BLUE-C2-POLICY-01 ipv4
         source prefix 10.0.0.0/8 192.168.0.0/16
         protocol tcp source port 1,10-20
         protocol icmp
         actions
            set traffic class 5
         !
      !
      match BLUE-C2-POLICY-02 ipv4
         source prefix field-set DEMO-01 DEMO-02
         protocol tcp source port field-set SERVICE-DEMO
         protocol icmp
         actions
            count DEMO-TRAFFIC
            set dscp 60
         !
      !
      match BLUE-C2-POLICY-03 ipv4
         source prefix field-set DEMO-01
         protocol tcp
         actions
            drop
            log
         !
      !
      match ipv4-all-default ipv4
         actions
            drop
            log
   !
```

# Quality Of Service
