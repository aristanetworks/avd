# port-channel-interfaces

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [Monitoring](#monitoring)
  - [SFlow](#sflow)
- [Interfaces](#interfaces)
  - [Ethernet Interfaces](#ethernet-interfaces)
  - [Port-Channel Interfaces](#port-channel-interfaces)
- [BFD](#bfd)
  - [BFD Interfaces](#bfd-interfaces)
- [MPLS](#mpls)
  - [MPLS Interfaces](#mpls-interfaces)
- [Multicast](#multicast)
  - [PIM Sparse Mode](#pim-sparse-mode)
- [Quality Of Service](#quality-of-service)

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

## Monitoring

### SFlow

#### SFlow Summary

sFlow is disabled.

#### SFlow Interfaces

| Interface | Ingress Enabled | Egress Enabled |
| --------- | --------------- | -------------- |
| Port-Channel117 | True | True |
| Port-Channel118 | True | True (unmodified) |
| Port-Channel119 | False | False |
| Port-Channel120 | False | False (unmodified) |

## Interfaces

### Ethernet Interfaces

#### Ethernet Interfaces Summary

##### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | Channel-Group |
| --------- | ----------- | ---- | ----- | ----------- | ----------- | ------------- |
| Ethernet3 | MLAG_PEER_DC1-LEAF1B_Ethernet3 | *trunk | *2-4094 | *- | *['LEAF_PEER_L3', 'MLAG'] | 3 |
| Ethernet4 | MLAG_PEER_DC1-LEAF1B_Ethernet4 | *trunk | *2-4094 | *- | *['LEAF_PEER_L3', 'MLAG'] | 3 |
| Ethernet5 | DC1-AGG01_Ethernet1 | *trunk | *110,201 | *- | *- | 5 |
| Ethernet10/1 | LAG Member | *access | *110 | *- | *- | 101 |
| Ethernet10/2 | LAG Member | *trunk | *110-112 | *- | *- | 102 |
| Ethernet10/3 | LAG Member | *trunk | *110-112 | *- | *- | 103 |
| Ethernet10/4 | LAG Member LACP fallback | *trunk | *112 | *- | *- | 104 |
| Ethernet11/2 | LAG Member LACP fallback LLDP ZTP VLAN | *trunk | *112 | *- | *- | 112 |
| Ethernet15 | DC1-AGG03_Ethernet1 | *trunk | *110,201 | *- | *- | 15 |
| Ethernet16 | DC1-AGG04_Ethernet1 | *trunk | *110,201 | *- | *- | 16 |
| Ethernet18 | LAG Member | *access | *110 | *- | *- | 109 |
| Ethernet50 | SRV-POD03_Eth1 | *trunk | *110,201 | *- | *- | 5 |

*Inherited from Port-Channel Interface

##### IPv4

| Interface | Description | Type | Channel Group | IP Address | VRF |  MTU | Shutdown | ACL In | ACL Out |
| --------- | ----------- | -----| ------------- | ---------- | ----| ---- | -------- | ------ | ------- |
| Ethernet17 | LAG Member | *routed | 17 | *192.0.2.3/31 | **default | **- | **- | **- | **- |
*Inherited from Port-Channel Interface

##### ISIS

| Interface | Channel Group | ISIS Instance | ISIS Metric | Mode | ISIS Circuit Type | Hello Padding | Authentication Mode |
| --------- | ------------- | ------------- | ----------- | ---- | ----------------- | ------------- | ------------------- |
| Ethernet10/10 | 110 | *ISIS_TEST | *99 | *point-to-point | *level-2 | *True | *text |
 *Inherited from Port-Channel Interface

##### Error Correction Encoding Interfaces

| Interface | Enabled |
| --------- | ------- |
| Ethernet11/1 | fire-code<br>reed-solomon |

#### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet3
   description MLAG_PEER_DC1-LEAF1B_Ethernet3
   channel-group 3 mode active
!
interface Ethernet4
   description MLAG_PEER_DC1-LEAF1B_Ethernet4
   channel-group 3 mode active
!
interface Ethernet5
   description DC1-AGG01_Ethernet1
   channel-group 5 mode active
   transceiver media override 100gbase-ar4
!
interface Ethernet8
   description MLAG_PEER_DC1-LEAF1B_Ethernet8
   channel-group 8 mode active
!
interface Ethernet10/1
   description LAG Member
   channel-group 101 mode active
!
interface Ethernet10/2
   description LAG Member
   channel-group 102 mode active
!
interface Ethernet10/3
   description LAG Member
   channel-group 103 mode active
!
interface Ethernet10/4
   description LAG Member LACP fallback
   switchport trunk allowed vlan 100
   switchport mode trunk
   switchport
   channel-group 104 mode active
   spanning-tree portfast
!
interface Ethernet10/10
   description isis_port_channel_member
   channel-group 110 mode active
!
interface Ethernet11/1
   description LAG Member with error_correction
   error-correction encoding fire-code
   error-correction encoding reed-solomon
   channel-group 111 mode active
!
interface Ethernet11/2
   description LAG Member LACP fallback LLDP ZTP VLAN
   switchport trunk allowed vlan 112
   switchport mode trunk
   switchport
   channel-group 112 mode active
   lldp tlv transmit ztp vlan 112
   spanning-tree portfast
!
interface Ethernet15
   description DC1-AGG03_Ethernet1
   channel-group 15 mode active
   lacp timer fast
   lacp timer multiplier 30
!
interface Ethernet16
   description DC1-AGG04_Ethernet1
   channel-group 16 mode active
   lacp timer normal
!
interface Ethernet17
   description LAG Member
   channel-group 17 mode active
!
interface Ethernet18
   description LAG Member
   channel-group 109 mode active
!
interface Ethernet50
   description SRV-POD03_Eth1
   channel-group 5 mode active
   no lldp transmit
   no lldp receive
```

### Port-Channel Interfaces

#### Port-Channel Interfaces Summary

##### L2

| Interface | Description | Type | Mode | VLANs | Native VLAN | Trunk Group | LACP Fallback Timeout | LACP Fallback Mode | MLAG ID | EVPN ESI |
| --------- | ----------- | ---- | ---- | ----- | ----------- | ------------| --------------------- | ------------------ | ------- | -------- |
| Port-Channel3 | MLAG_PEER_DC1-LEAF1B_Po3 | switched | trunk | 2-4094 | - | ['LEAF_PEER_L3', 'MLAG'] | - | - | - | - |
| Port-Channel5 | DC1_L2LEAF1_Po1 | switched | trunk | 110,201 | - | - | - | - | 5 | - |
| Port-Channel10 | SRV01_bond0 | switched | trunk | 2-3000 | - | - | - | - | - | 0000:0000:0404:0404:0303 |
| Port-Channel12 | interface_in_mode_access_with_voice | switched | trunk phone | - | 100 | - | - | - | - | - |
| Port-Channel13 | EVPN-Vxlan single-active redundancy | switched | access | - | - | - | - | - | - | 0000:0000:0000:0102:0304 |
| Port-Channel14 | EVPN-MPLS multihoming | switched | access | - | - | - | - | - | - | 0000:0000:0000:0102:0305 |
| Port-Channel15 | DC1_L2LEAF3_Po1 | switched | trunk | 110,201 | - | - | - | - | 15 | - |
| Port-Channel16 | DC1_L2LEAF4_Po1 | switched | trunk | 110,201 | - | - | - | - | 16 | - |
| Port-Channel20 | Po_in_mode_access_accepting_tagged_LACP_frames | switched | access | 200 | - | - | - | - | - | - |
| Port-Channel50 | SRV-POD03_PortChanne1 | switched | trunk | 1-4000 | - | - | - | - | - | 0000:0000:0303:0202:0101 |
| Port-Channel51 | ipv6_prefix | switched | trunk | 1-500 | - | - | - | - | - | - |
| Port-Channel100.101 | IFL for TENANT01 | switched | access | - | - | - | - | - | - | - |
| Port-Channel100.102 | IFL for TENANT02 | switched | access | - | - | - | - | - | - | - |
| Port-Channel101 | PVLAN Promiscuous Access - only one secondary | switched | access | 110 | - | - | - | - | - | - |
| Port-Channel102 | PVLAN Promiscuous Trunk - vlan translation out | switched | trunk | 110-112 | - | - | - | - | - | - |
| Port-Channel103 | PVLAN Secondary Trunk | switched | trunk | 110-112 | - | - | - | - | - | - |
| Port-Channel104 | LACP fallback individual | switched | trunk | 112 | - | - | 300 | individual | - | - |
| Port-Channel105 | bpdu disabled | switched | access | - | - | - | - | - | - | - |
| Port-Channel106 | bpdu enabled | switched | access | - | - | - | - | - | - | - |
| Port-Channel107 | bpdu true | switched | access | - | - | - | - | - | - | - |
| Port-Channel108 | bpdu false | switched | access | - | - | - | - | - | - | - |
| Port-Channel109 | Molecule ACLs | switched | access | 110 | - | - | - | - | - | - |
| Port-Channel112 | LACP fallback individual | switched | trunk | 112 | - | - | 5 | individual | - | - |
| Port-Channel115 | native-vlan-tag-precedence | switched | trunk | - | tag | - | - | - | - | - |
| Port-Channel121 | access_port_with_no_vlans | switched | access | - | - | - | - | - | - | - |
| Port-Channel122 | trunk_port_with_no_vlans | switched | trunk | - | - | - | - | - | - | - |

##### Encapsulation Dot1q Interfaces

| Interface | Description | Type | Vlan ID | Dot1q VLAN Tag |
| --------- | ----------- | -----| ------- | -------------- |
| Port-Channel8.101 | to Dev02 Port-Channel8.101 - VRF-C1 | l3dot1q | - | 101 |

##### Flexible Encapsulation Interfaces

| Interface | Description | Type | Vlan ID | Client Unmatched | Client Dot1q VLAN | Client Dot1q Outer Tag | Client Dot1q Inner Tag | Network Retain Client Encapsulation | Network Dot1q VLAN | Network Dot1q Outer Tag | Network Dot1q Inner Tag |
| --------- | ----------- | ---- | ------- | -----------------| ----------------- | ---------------------- | ---------------------- | ----------------------------------- | ------------------ | ----------------------- | ----------------------- |
| Port-Channel111.1 | TENANT_A pseudowire 1 interface | l2dot1q | - | True | - | - | - | False | - | - | - |
| Port-Channel111.100 | TENANT_A pseudowire 2 interface | l2dot1q | - | False | 100 | - | - | True | - | - | - |
| Port-Channel111.200 | TENANT_A pseudowire 3 interface | l2dot1q | - | False | 200 | - | - | False | - | - | - |
| Port-Channel111.300 | TENANT_A pseudowire 4 interface | l2dot1q | - | False | 300 | - | - | False | 400 | - | - |
| Port-Channel111.400 | TENANT_A pseudowire 3 interface | l2dot1q | - | False | - | 400 | 20 | False | - | 401 | 21 |
| Port-Channel111.1000 | L2 Subinterface | l2dot1q | 1000 | False | 100 | - | - | True | - | - | - |

##### Private VLAN

| Interface | PVLAN Mapping | Secondary Trunk |
| --------- | ------------- | ----------------|
| Port-Channel101 | 111 | - |
| Port-Channel103 | - | True |

##### VLAN Translations

| Interface | From VLAN ID(s) | To VLAN ID | Direction |
| --------- | --------------- | -----------| --------- |
| Port-Channel102 | 111-112 | 110 | out

##### EVPN Multihoming

####### EVPN Multihoming Summary

| Interface | Ethernet Segment Identifier | Multihoming Redundancy Mode | Route Target |
| --------- | --------------------------- | --------------------------- | ------------ |
| Port-Channel13 | 0000:0000:0000:0102:0304 | single-active | 00:00:01:02:03:04 |
| Port-Channel14 | 0000:0000:0000:0102:0305 | all-active | 00:00:01:02:03:05 |

####### Designated Forwarder Election Summary

| Interface | Algorithm | Preference Value | Dont Preempt | Hold time | Subsequent Hold Time | Candidate Reachability Required |
| --------- | --------- | ---------------- | ------------ | --------- | -------------------- | ------------------------------- |
| Port-Channel13 | preference | 100 | True | 10 | - | True |

####### EVPN-MPLS summary

| Interface | Shared Index | Tunnel Flood Filter Time |
| --------- | ------------ | ------------------------ |
| Port-Channel14 | 100 | 100 |

##### Link Tracking Groups

| Interface | Group Name | Direction |
| --------- | ---------- | --------- |
| Port-Channel5 | EVPN_MH_ES1 | downstream |
| Port-Channel15 | EVPN_MH_ES2 | upstream |

##### IPv4

| Interface | Description | Type | MLAG ID | IP Address | VRF | MTU | Shutdown | ACL In | ACL Out |
| --------- | ----------- | ---- | ------- | ---------- | --- | --- | -------- | ------ | ------- |
| Port-Channel8.101 | to Dev02 Port-Channel8.101 - VRF-C1 | routed | - | 10.1.2.3/31 | default | - | - | - | - |
| Port-Channel9 | - | routed | - | 10.9.2.3/31 | default | - | - | - | - |
| Port-Channel17 | PBR Description | routed | - | 192.0.2.3/31 | default | - | - | - | - |
| Port-Channel99 | MCAST | routed | - | 192.0.2.10/31 | default | - | - | - | - |
| Port-Channel113 | interface_with_mpls_enabled | routed | - | 172.31.128.9/31 | default | - | - | - | - |
| Port-Channel114 | interface_with_mpls_disabled | routed | - | 172.31.128.10/31 | default | - | - | - | - |

##### ISIS

| Interface | ISIS Instance | ISIS Metric | Mode | ISIS Circuit Type | Hello Padding | Authentication Mode |
| --------- | ------------- | ----------- | ---- | ----------------- | ------------- | ------------------- |
| Port-Channel110 | ISIS_TEST | 99 | point-to-point | level-2 | True | text |

#### Port-Channel Interfaces Device Configuration

```eos
!
interface Port-Channel3
   description MLAG_PEER_DC1-LEAF1B_Po3
   switchport
   switchport trunk allowed vlan 2-4094
   switchport mode trunk
   switchport trunk group LEAF_PEER_L3
   switchport trunk group MLAG
   no snmp trap link-change
   shape rate 200000 kbps
!
interface Port-Channel5
   description DC1_L2LEAF1_Po1
   bgp session tracker ST2
   switchport
   switchport trunk allowed vlan 110,201
   switchport mode trunk
   mlag 5
   storm-control broadcast level 1
   storm-control multicast level 1
   storm-control unknown-unicast level 1
   link tracking group EVPN_MH_ES1 downstream
   comment
   Comment created from eos_cli under port_channel_interfaces.Port-Channel5
   EOF

!
interface Port-Channel8
   description to Dev02 Port-channel 8
   no switchport
!
interface Port-Channel8.101
   description to Dev02 Port-Channel8.101 - VRF-C1
   encapsulation dot1q vlan 101
   ip address 10.1.2.3/31
!
interface Port-Channel9
   no switchport
   spanning-tree guard root
   ip address 10.9.2.3/31
   bfd interval 500 min-rx 500 multiplier 5
   bfd echo
!
interface Port-Channel10
   description SRV01_bond0
   switchport
   switchport trunk allowed vlan 2-3000
   switchport mode trunk
   evpn ethernet-segment
      identifier 0000:0000:0404:0404:0303
      route-target import 04:04:03:03:02:02
   shape rate 50 percent
!
interface Port-Channel12
   description interface_in_mode_access_with_voice
   switchport
   switchport trunk native vlan 100
   switchport phone vlan 70
   switchport phone trunk untagged
!
interface Port-Channel13
   description EVPN-Vxlan single-active redundancy
   switchport
   evpn ethernet-segment
      identifier 0000:0000:0000:0102:0304
      redundancy single-active
      designated-forwarder election algorithm preference 100 dont-preempt
      designated-forwarder election hold-time 10
      designated-forwarder election candidate reachability required
      route-target import 00:00:01:02:03:04
!
interface Port-Channel14
   description EVPN-MPLS multihoming
   switchport
   evpn ethernet-segment
      identifier 0000:0000:0000:0102:0305
      mpls tunnel flood filter time 100
      mpls shared index 100
      route-target import 00:00:01:02:03:05
!
interface Port-Channel15
   description DC1_L2LEAF3_Po1
   switchport
   switchport trunk allowed vlan 110,201
   switchport mode trunk
   mlag 15
   spanning-tree guard loop
   link tracking group EVPN_MH_ES2 upstream
!
interface Port-Channel16
   description DC1_L2LEAF4_Po1
   switchport
   switchport trunk allowed vlan 110,201
   switchport mode trunk
   snmp trap link-change
   mlag 16
   spanning-tree guard none
!
interface Port-Channel17
   description PBR Description
   no switchport
   ip address 192.0.2.3/31
   service-policy type pbr input MyPolicy
!
interface Port-Channel20
   description Po_in_mode_access_accepting_tagged_LACP_frames
   switchport
   switchport access vlan 200
   l2-protocol encapsulation dot1q vlan 200
!
interface Port-Channel50
   description SRV-POD03_PortChanne1
   switchport
   switchport trunk allowed vlan 1-4000
   switchport mode trunk
   evpn ethernet-segment
      identifier 0000:0000:0303:0202:0101
      route-target import 03:03:02:02:01:01
   lacp system-id 0303.0202.0101
!
interface Port-Channel51
   description ipv6_prefix
   switchport
   switchport trunk allowed vlan 1-500
   switchport mode trunk
   ipv6 nd prefix a1::/64 infinite infinite no-autoconfig
!
interface Port-Channel99
   description MCAST
   no switchport
   ip address 192.0.2.10/31
   pim ipv4 sparse-mode
   pim ipv4 dr-priority 200
!
interface Port-Channel100
   logging event link-status
   no switchport
!
interface Port-Channel100.101
   description IFL for TENANT01
   logging event link-status
   mtu 1500
   switchport
   ip address 10.1.1.3/31
!
interface Port-Channel100.102
   description IFL for TENANT02
   no logging event link-status
   mtu 1500
   switchport
   vrf C2
   ip address 10.1.2.3/31
!
interface Port-Channel101
   description PVLAN Promiscuous Access - only one secondary
   switchport
   switchport access vlan 110
   switchport pvlan mapping 111
   no qos trust
!
interface Port-Channel102
   description PVLAN Promiscuous Trunk - vlan translation out
   switchport
   switchport trunk allowed vlan 110-112
   switchport mode trunk
   switchport vlan translation out 111-112 110
!
interface Port-Channel103
   description PVLAN Secondary Trunk
   switchport
   switchport trunk allowed vlan 110-112
   switchport mode trunk
   switchport trunk private-vlan secondary
!
interface Port-Channel104
   description LACP fallback individual
   switchport
   switchport trunk allowed vlan 112
   switchport mode trunk
   port-channel lacp fallback timeout 300
   port-channel lacp fallback individual
!
interface Port-Channel105
   description bpdu disabled
   switchport
   spanning-tree bpduguard disable
   spanning-tree bpdufilter disable
!
interface Port-Channel106
   description bpdu enabled
   switchport
   spanning-tree bpduguard enable
   spanning-tree bpdufilter enable
!
interface Port-Channel107
   description bpdu true
   switchport
   spanning-tree bpduguard enable
   spanning-tree bpdufilter enable
!
interface Port-Channel108
   description bpdu false
   switchport
!
interface Port-Channel109
   description Molecule ACLs
   switchport
   switchport access vlan 110
   ip access-group IPV4_ACL_IN in
   ip access-group IPV4_ACL_OUT out
   ipv6 access-group IPV6_ACL_IN in
   ipv6 access-group IPV6_ACL_OUT out
   mac access-group MAC_ACL_IN in
   mac access-group MAC_ACL_OUT out
!
interface Port-Channel110
   description isis_interface_knobs
   no switchport
   isis enable ISIS_TEST
   isis circuit-type level-2
   isis metric 99
   isis network point-to-point
   isis hello padding
   isis authentication mode text
   isis authentication key 7 asfddja23452
!
interface Port-Channel111
   description Flexencap Port-Channel
   no switchport
!
interface Port-Channel111.1
   description TENANT_A pseudowire 1 interface
   encapsulation vlan
      client unmatched
!
interface Port-Channel111.100
   description TENANT_A pseudowire 2 interface
   encapsulation vlan
      client dot1q 100 network client
!
interface Port-Channel111.200
   description TENANT_A pseudowire 3 interface
   encapsulation vlan
      client dot1q 200
!
interface Port-Channel111.300
   description TENANT_A pseudowire 4 interface
   encapsulation vlan
      client dot1q 300 network dot1q 400
!
interface Port-Channel111.400
   description TENANT_A pseudowire 3 interface
   encapsulation vlan
      client dot1q outer 400 inner 20 network dot1q outer 21 inner 401
!
interface Port-Channel111.1000
   description L2 Subinterface
   vlan id 1000
   encapsulation vlan
      client dot1q 100 network client
   evpn ethernet-segment
      identifier 0000:0000:0303:0202:0101
      route-target import 03:03:02:02:01:01
   lacp system-id 0303.0202.0101
!
interface Port-Channel112
   description LACP fallback individual
   switchport
   switchport trunk allowed vlan 112
   switchport mode trunk
   port-channel lacp fallback timeout 5
   port-channel lacp fallback individual
!
interface Port-Channel113
   description interface_with_mpls_enabled
   no switchport
   ip address 172.31.128.9/31
   mpls ip
   mpls ldp interface
   mpls ldp igp sync
!
interface Port-Channel114
   description interface_with_mpls_disabled
   no switchport
   ip address 172.31.128.10/31
   no mpls ip
   no mpls ldp interface
!
interface Port-Channel115
   description native-vlan-tag-precedence
   switchport
   switchport trunk native vlan tag
   switchport mode trunk
!
interface Port-Channel117
   description interface_with_sflow_ingress_egress_enabled
   no switchport
   sflow enable
   sflow egress enable
!
interface Port-Channel118
   description interface_with_sflow_ingress_egress_unmodified_enabled
   no switchport
   sflow enable
   sflow egress unmodified enable
!
interface Port-Channel119
   description interface_with_sflow_ingress_egress_disabled
   no switchport
   no sflow enable
   no sflow egress enable
!
interface Port-Channel120
   description interface_with_sflow_ingress_egress_unmodified_disabled
   no switchport
   no sflow enable
   no sflow egress unmodified enable
!
interface Port-Channel121
   description access_port_with_no_vlans
   switchport
!
interface Port-Channel122
   description trunk_port_with_no_vlans
   switchport
   switchport mode trunk
```

## BFD

### BFD Interfaces

| Interface | Interval | Minimum RX | Multiplier | Echo |
| --------- | -------- | ---------- | ---------- | ---- |
| Port-Channel9 | 500 | 500 | 5 | True |

## MPLS

### MPLS Interfaces

| Interface | MPLS IP Enabled | LDP Enabled | IGP Sync |
| --------- | --------------- | ----------- | -------- |
| Port-Channel113 | True | True | True |
| Port-Channel114 | False | False | - |

## Multicast

### PIM Sparse Mode

#### PIM Sparse Mode enabled interfaces

| Interface Name | VRF Name | IP Version | DR Priority | Local Interface |
| -------------- | -------- | ---------- | ----------- | --------------- |
| Port-Channel99 | - | IPv4 | 200 | - |

## Quality Of Service

#### QOS Interfaces

| Interface | Trust | Default DSCP | Default COS | Shape rate |
| --------- | ----- | ------------ | ----------- | ---------- |
| Port-Channel3 | - | - | - | 200000 kbps |
| Port-Channel10 | - | - | - | 50 percent |
| Port-Channel101 | disabled | - | - | - |
