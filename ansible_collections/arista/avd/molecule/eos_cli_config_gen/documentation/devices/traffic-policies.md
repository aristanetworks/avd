# traffic-policies

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [Interfaces](#interfaces)
  - [Ethernet Interfaces](#ethernet-interfaces)
  - [Port-Channel Interfaces](#port-channel-interfaces)
  - [Traffic Policies information](#traffic-policies-information)

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

## Interfaces

### Ethernet Interfaces

#### Ethernet Interfaces Summary

##### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | Channel-Group |
| --------- | ----------- | ---- | ----- | ----------- | ----------- | ------------- |

*Inherited from Port-Channel Interface

#### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet1
   no switchport
   traffic-policy input BLUE-C1-POLICY
   traffic-policy output BLUE-C2-POLICY
```

### Port-Channel Interfaces

#### Port-Channel Interfaces Summary

##### L2

| Interface | Description | Type | Mode | VLANs | Native VLAN | Trunk Group | LACP Fallback Timeout | LACP Fallback Mode | MLAG ID | EVPN ESI |
| --------- | ----------- | ---- | ---- | ----- | ----------- | ------------| --------------------- | ------------------ | ------- | -------- |

#### Port-Channel Interfaces Device Configuration

```eos
!
interface Port-Channel2
   no switchport
   traffic-policy input BLUE-C1-POLICY
   traffic-policy output BLUE-C2-POLICY
```

### Traffic Policies information

#### IPv4 Field Sets

| Field Set Name | Values |
| -------------- | ------ |
| DEMO-01 | 10.0.0.0/8<br/>192.168.0.0/16 |
| DEMO-02 | 172.16.0.0/12<br/>224.0.0.0/8 |

#### L4 Port Field Sets

| Field Set Name | Values |
| -------------- | ------ |
| SERVICE-DEMO | 10,20,80,440-450|

#### Traffic Policies

##### BLUE-C1-POLICY

| Match set | Type | Sources | Destinations | Protocol | Source Port(s) | Destination port(s) | Action |
| --------- | ---- | ------- | ------------ | -------- | -------------- | ------------------- | ------ |
| BLUE-C1-POLICY-01 | ipv4 | 10.0.0.0/8<br/>192.168.0.0/16 | DEMO-01 | tcp<br/>udp | SERVICE-DEMO | ANY | action: PASS<br/>traffic-class: 5 |
| BLUE-C1-POLICY-02 | ipv4 | DEMO-01<br/>DEMO-02 | ANY | tcp<br/>icmp | ANY | SERVICE-DEMO | action: PASS<br/>counter: DEMO-TRAFFIC<br/>dscp marking: 60 |
| BLUE-C1-POLICY-03 | ipv4 | DEMO-01 | ANY | icmp | ANY | ANY | action: DROP<br/>counter: DROP-PACKETS<br/>logging |
| BLUE-C1-POLICY-04 | ipv4 | DEMO-02 | DEMO-01 | tcp<br/>icmp | 22 | ANY | action: PASS<br/>traffic-class: 5 |
| BLUE-C1-POLICY-05 | ipv4 | DEMO-02 | DEMO-01 | tcp | ANY | ANY | action: PASS<br/>traffic-class: 5 |
| BLUE-C1-POLICY-06 | ipv4 | ANY | ANY | neighbors<br/>ip<br/>udp<br/>tcp<br/>icmp | SERVICE-DEMO | 1,10-20 | action: PASS |
| BLUE-C1-POLICY-07 | ipv4 | ANY | 10.0.0.0/8<br/>192.168.0.0/16 | ANY |  |  | default action: PASS |
| BLUE-C1-POLICY-08 | ipv4 | ANY | DEMO-01 | udp<br/>tcp | ANY | SERVICE-DEMO | default action: PASS |

##### BLUE-C2-POLICY

| Match set | Type | Sources | Destinations | Protocol | Source Port(s) | Destination port(s) | Action |
| --------- | ---- | ------- | ------------ | -------- | -------------- | ------------------- | ------ |
| BLUE-C2-POLICY-01 | ipv4 | 10.0.0.0/8<br/>192.168.0.0/16 | ANY | tcp<br/>icmp | 1,10-20 | ANY | action: PASS<br/>traffic-class: 5 |
| BLUE-C2-POLICY-02 | ipv4 | DEMO-01<br/>DEMO-02 | ANY | tcp<br/>icmp | SERVICE-DEMO | ANY | action: PASS<br/>counter: DEMO-TRAFFIC<br/>dscp marking: 60 |
| BLUE-C2-POLICY-03 | ipv4 | DEMO-01 | ANY | tcp | ANY | ANY | action: DROP |

##### BLUE-C3-POLICY

##### BLUE-C4-POLICY

##### BLUE-C5-POLICY

##### BLUE-C6-POLICY

##### BLUE-C7-POLICY

| Match set | Type | Sources | Destinations | Protocol | Source Port(s) | Destination port(s) | Action |
| --------- | ---- | ------- | ------------ | -------- | -------------- | ------------------- | ------ |
| BLUE-C7-POLICY-01 | ipv4 | ANY | ANY | neighbors | ANY | ANY | default action: PASS |

##### Traffic-Policy Interfaces

| Interface | Input Traffic-Policy | Output Traffic-Policy |
| --------- | -------------------- | --------------------- |
| Ethernet1 | BLUE-C1-POLICY | BLUE-C2-POLICY |
| Port-Channel2 | BLUE-C1-POLICY | BLUE-C2-POLICY |

#### Traffic Policies Device Configuration

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
         protocol udp flags initial source port field-set SERVICE-DEMO
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
         protocol icmp type echo echo-reply code all
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
      match BLUE-C1-POLICY-06 ipv4
         protocol neighbors bgp
         protocol udp destination port 1,10-20
         protocol tcp flags initial source port 22
         protocol icmp
         !
      !
      match BLUE-C1-POLICY-07 ipv4
         destination prefix 10.0.0.0/8 192.168.0.0/16
         !
      !
      match BLUE-C1-POLICY-08 ipv4
         destination prefix 10.0.0.0/8 192.168.0.0/16
         destination prefix field-set DEMO-01
         protocol udp flags initial destination port 1,10-20
         protocol tcp destination port field-set SERVICE-DEMO
         !
      !
      match ipv4-all-default ipv4
         actions
            drop
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
         !
      !
      match ipv4-all-default ipv4
         actions
            drop
            log
   !
   traffic-policy BLUE-C3-POLICY
      match ipv4-all-default ipv4
         actions
            count test
            set traffic class 10
            set dscp 11
   !
   traffic-policy BLUE-C4-POLICY
      match ipv6-all-default ipv6
         actions
            count test
            set traffic class 10
            set dscp 11
   !
   traffic-policy BLUE-C5-POLICY
      match ipv6-all-default ipv6
         actions
            drop
            log
   !
   traffic-policy BLUE-C6-POLICY
      match ipv6-all-default ipv6
         actions
            drop
   !
   traffic-policy BLUE-C7-POLICY
      match BLUE-C7-POLICY-01 ipv4
         protocol neighbors bgp
         !
      !
   !
```
