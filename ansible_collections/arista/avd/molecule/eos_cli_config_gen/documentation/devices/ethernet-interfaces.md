# ethernet-interfaces
# Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [Authentication](#authentication)
- [Monitoring](#monitoring)
- [Internal VLAN Allocation Policy](#internal-vlan-allocation-policy)
  - [Internal VLAN Allocation Policy Summary](#internal-vlan-allocation-policy-summary)
- [Interfaces](#interfaces)
  - [Ethernet Interfaces](#ethernet-interfaces)
- [Routing](#routing)
  - [IP Routing](#ip-routing)
  - [IPv6 Routing](#ipv6-routing)
- [BFD](#bfd)
  - [BFD Interfaces](#bfd-interfaces)
- [MPLS](#mpls)
  - [MPLS Interfaces](#mpls-interfaces)
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
| Ethernet2 |  SRV-POD02_Eth1 | trunk | 110-111,210-211 | - | - | - |
| Ethernet4 |  Molecule IPv6 | access | - | - | - | - |
| Ethernet6 |  SRV-POD02_Eth1 | trunk | 110-111,210-211 | - | - | - |
| Ethernet7 |  Molecule L2 | access | - | - | - | - |
| Ethernet11 |  interface_in_mode_access_accepting_tagged_LACP | access | 200 | - | - | - |
| Ethernet12 |  interface_with_dot1q_tunnel | dot1q-tunnel | 300 | - | - | - |
| Ethernet13 |  interface_in_mode_access_with_voice | trunk phone | - | 100 | - | - |
| Ethernet14 |  SRV-POD02_Eth1 | trunk | 110-111,210-211 | - | - | - |
| Ethernet15 |  PVLAN Promiscuous Access - only one secondary | access | 110 | - | - | - |
| Ethernet16 |  PVLAN Promiscuous Trunk - vlan translation out | trunk | 110-112 | - | - | - |
| Ethernet17 |  PVLAN Secondary Trunk | trunk | 110-112 | - | - | - |
| Ethernet19 |  Switched port with no LLDP rx/tx | access | 110 | - | - | - |
| Ethernet21 |  200MBit/s shape | access | - | - | - | - |
| Ethernet22 |  10% shape | access | - | - | - | - |
| Ethernet23 |  Error-correction encoding | access | - | - | - | - |
| Ethernet24 |  Disable error-correction encoding | access | - | - | - | - |

*Inherited from Port-Channel Interface

#### Private VLAN

| Interface | PVLAN Mapping | Secondary Trunk |
| --------- | ------------- | ----------------|
| Ethernet15 | 111 | - |
| Ethernet17 | - | True |

#### VLAN Translations

| Interface | From VLAN ID(s) | To VLAN ID | Direction |
| --------- | --------------- | -----------| --------- |
| Ethernet16 | 111-112 | 110 | out

#### Link Tracking Groups

| Interface | Group Name | Direction |
| --------- | ---------- | --------- |
| Ethernet1 | EVPN_MH_ES1 | upstream |
| Ethernet3 | EVPN_MH_ES2 | downstream |

#### IPv4

| Interface | Description | Type | Channel Group | IP Address | VRF |  MTU | Shutdown | ACL In | ACL Out |
| --------- | ----------- | -----| ------------- | ---------- | ----| ---- | -------- | ------ | ------- |
| Ethernet1 | P2P_LINK_TO_DC1-SPINE1_Ethernet1 | routed | - | 172.31.255.1/31 | default | 1500 | - | - | - |
| Ethernet3 | P2P_LINK_TO_DC1-SPINE2_Ethernet2 | routed | - | 172.31.128.1/31 | default | 1500 | - | - | - |
| Ethernet8.101 | to WAN-ISP-01 Ethernet2.101 - VRF-C1 | l3dot1q | - | 172.31.128.1/31 | default | - | - | - | - |
| Ethernet9 | interface_with_mpls_enabled | routed | - | 172.31.128.9/31 | default | - | - | - | - |
| Ethernet10 | interface_with_mpls_disabled | routed | - | 172.31.128.10/31 | default | - | - | - | - |
| Ethernet18 | PBR Description | routed | - | 192.0.2.1/31 | default | 1500 | - | - | - |

#### IPv6

| Interface | Description | Type | Channel Group | IPv6 Address | VRF | MTU | Shutdown | ND RA Disabled | Managed Config Flag | IPv6 ACL In | IPv6 ACL Out |
| --------- | ----------- | ---- | --------------| ------------ | --- | --- | -------- | -------------- | -------------------| ----------- | ------------ |
| Ethernet3 | P2P_LINK_TO_DC1-SPINE2_Ethernet2 | routed | - | 2002:ABDC::1/64 | default | 1500 | - | - | *- | - | - |
| Ethernet4 | Molecule IPv6 | switchport | - | 2020::2020/64 | default | 9100 | true | true | true | IPv6_ACL_IN | IPv6_ACL_OUT |
| Ethernet8.101 | to WAN-ISP-01 Ethernet2.101 - VRF-C1 | l3dot1q | - | 2002:ABDC::1/64 | default | - | - | - | *- | - | - |

#### ISIS

| Interface | Channel Group | ISIS Instance | ISIS Metric | Mode | ISIS Circuit Type |
| --------- | ------------- | ------------- | ----------- | ---- | ----------------- |
| Ethernet5 | - | ISIS_TEST | 99 | point-to-point | level-2 |

#### Error Correction Encoding Interfaces

| Interface | Enabled |
| --------- | ------- |
| Ethernet23 | fire-code<br>reed-solomon |
| Ethernet24 | Disabled |

### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet1
   description P2P_LINK_TO_DC1-SPINE1_Ethernet1
   mtu 1500
   no switchport
   ip address 172.31.255.1/31
   bfd interval 500 min-rx 500 multiplier 5
   link tracking group EVPN_MH_ES1 upstream
   comment
   Comment created from eos_cli under ethernet_interfaces.Ethernet1
   EOF

!
interface Ethernet2
   description SRV-POD02_Eth1
   switchport
   switchport trunk allowed vlan 110-111,210-211
   switchport mode trunk
   storm-control all level 10
   storm-control broadcast level pps 500
   storm-control unknown-unicast level 1
!
interface Ethernet3
   description P2P_LINK_TO_DC1-SPINE2_Ethernet2
   mtu 1500
   no switchport
   ip address 172.31.128.1/31
   ipv6 enable
   ipv6 address 2002:ABDC::1/64
   ipv6 nd prefix 2345:ABCD:3FE0::1/96 infinite 50 no-autoconfig
   ipv6 nd prefix 2345:ABCD:3FE0::2/96 50 infinite
   ipv6 nd prefix 2345:ABCD:3FE0::3/96 100000 no-autoconfig
   link tracking group EVPN_MH_ES2 downstream
!
interface Ethernet4
   description Molecule IPv6
   shutdown
   mtu 9100
   switchport
   ipv6 enable
   ipv6 address 2020::2020/64
   ipv6 address FE80:FEA::AB65/64 link-local
   ipv6 nd ra disabled
   ipv6 nd managed-config-flag
   ipv6 access-group IPv6_ACL_IN in
   ipv6 access-group IPv6_ACL_OUT out
!
interface Ethernet5
   description Molecule Routing
   no shutdown
   mtu 9100
   no switchport
   ip ospf network point-to-point
   ip ospf area 100
   ip ospf cost 99
   ip ospf authentication message-digest
   ip ospf authentication-key 7 asfddja23452
   ip ospf message-digest-key 1 sha512 7 asfddja23452
   isis enable ISIS_TEST
   isis circuit-type level-2
   isis metric 99
   isis network point-to-point
   pim ipv4 sparse-mode
!
interface Ethernet6
   description SRV-POD02_Eth1
   logging event link-status
   switchport
   switchport trunk allowed vlan 110-111,210-211
   switchport mode trunk
!
interface Ethernet7
   description Molecule L2
   no shutdown
   mtu 7000
   switchport
   qos trust cos
   qos cos 5
   spanning-tree portfast
   spanning-tree bpdufilter enable
   spanning-tree bpduguard enable
   vmtracer vmware-esx
   ptp enable
   ptp announce interval 10
   ptp announce timeout 30
   ptp delay-req interval 20
   ptp delay-mechanism p2p
   ptp sync-message interval 5
   ptp role master
   ptp vlan all
   ptp transport layer2
   service-profile QoS
   storm-control all level 75
   storm-control broadcast level pps 10
   storm-control multicast level 50
   storm-control unknown-unicast level 10
   transceiver media override 100gbase-ar4
!
interface Ethernet8
   description to WAN-ISP1-01 Ethernet2
   no switchport
   no lldp transmit
   no lldp receive
!
interface Ethernet8.101
   description to WAN-ISP-01 Ethernet2.101 - VRF-C1
   encapsulation dot1q vlan 101
   ip address 172.31.128.1/31
   ipv6 enable
   ipv6 address 2002:ABDC::1/64
!
interface Ethernet9
   description interface_with_mpls_enabled
   no switchport
   ip address 172.31.128.9/31
   mpls ip
   mpls ldp interface
!
interface Ethernet10
   description interface_with_mpls_disabled
   no switchport
   ip address 172.31.128.10/31
   no mpls ip
   no mpls ldp interface
!
interface Ethernet11
   description interface_in_mode_access_accepting_tagged_LACP
   switchport
   switchport access vlan 200
   switchport mode access
   l2-protocol encapsulation dot1q vlan 200
!
interface Ethernet12
   description interface_with_dot1q_tunnel
   switchport
   switchport access vlan 300
   switchport mode dot1q-tunnel
!
interface Ethernet13
   description interface_in_mode_access_with_voice
   no logging event link-status
   switchport
   switchport trunk native vlan 100
   switchport phone vlan 70
   switchport phone trunk untagged
   switchport mode trunk phone
!
interface Ethernet14
   description SRV-POD02_Eth1
   logging event link-status
   switchport
   switchport trunk allowed vlan 110-111,210-211
   switchport mode trunk
!
interface Ethernet15
   description PVLAN Promiscuous Access - only one secondary
   switchport
   switchport access vlan 110
   switchport mode access
   switchport pvlan mapping 111
!
interface Ethernet16
   description PVLAN Promiscuous Trunk - vlan translation out
   switchport
   switchport trunk allowed vlan 110-112
   switchport mode trunk
   switchport vlan translation out 111-112 110
!
interface Ethernet17
   description PVLAN Secondary Trunk
   switchport
   switchport trunk allowed vlan 110-112
   switchport mode trunk
   switchport trunk private-vlan secondary
!
interface Ethernet18
   description PBR Description
   mtu 1500
   no switchport
   ip address 192.0.2.1/31
   service-policy type pbr input MyLANServicePolicy
!
interface Ethernet19
   description Switched port with no LLDP rx/tx
   switchport
   switchport access vlan 110
   switchport mode access
   no lldp transmit
   no lldp receive
!
interface Ethernet20
   description Port patched through patch-panel to pseudowire
   no switchport
   no lldp transmit
   no lldp receive
!
interface Ethernet21
   description 200MBit/s shape
   switchport
   no qos trust
   shape rate 200000 kbps
!
interface Ethernet22
   description 10% shape
   switchport
   shape rate 10 percent
!
interface Ethernet23
   description Error-correction encoding
   error-correction encoding fire-code
   error-correction encoding reed-solomon
   switchport
!
interface Ethernet24
   description Disable error-correction encoding
   no error-correction encoding
   switchport
```

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

# BFD

## BFD Interfaces

| Interface | Interval | Minimum RX | Multiplier |
| --------- | -------- | ---------- | ---------- |
| Ethernet1 | 500 | 500 | 5 |

# MPLS

## MPLS Interfaces

| Interface | MPLS IP Enabled | LDP Enabled | IGP Sync |
| --------- | --------------- | ----------- | -------- |
| Ethernet9 | True | True | - |
| Ethernet10 | False | False | - |

# Multicast

# Filters

# ACL

# Quality Of Service

### QOS Interfaces

| Interface | Trust | Default DSCP | Default COS | Shape rate |
| --------- | ----- | ------------ | ----------- | ---------- |
| Ethernet7 | cos | - | 5 | - |
| Ethernet21 | disabled | - | - | 200000 kbps |
| Ethernet22 | - | - | - | 10 percent |
