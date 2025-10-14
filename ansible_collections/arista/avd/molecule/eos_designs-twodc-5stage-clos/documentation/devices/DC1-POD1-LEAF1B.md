# DC1-POD1-LEAF1B

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
  - [IP Domain-list](#ip-domain-list)
- [Authentication](#authentication)
  - [Local Users](#local-users)
  - [Enable Password](#enable-password)
- [Monitoring](#monitoring)
  - [SNMP](#snmp)
- [Spanning Tree](#spanning-tree)
  - [Spanning Tree Summary](#spanning-tree-summary)
  - [Spanning Tree Device Configuration](#spanning-tree-device-configuration)
- [Internal VLAN Allocation Policy](#internal-vlan-allocation-policy)
  - [Internal VLAN Allocation Policy Summary](#internal-vlan-allocation-policy-summary)
  - [Internal VLAN Allocation Policy Device Configuration](#internal-vlan-allocation-policy-device-configuration)
- [VLANs](#vlans)
  - [VLANs Summary](#vlans-summary)
  - [VLANs Device Configuration](#vlans-device-configuration)
- [Interfaces](#interfaces)
  - [Ethernet Interfaces](#ethernet-interfaces)
  - [Loopback Interfaces](#loopback-interfaces)
  - [VLAN Interfaces](#vlan-interfaces)
- [Routing](#routing)
  - [Service Routing Protocols Model](#service-routing-protocols-model)
  - [Virtual Router MAC Address](#virtual-router-mac-address)
  - [IP Routing](#ip-routing)
  - [IPv6 Routing](#ipv6-routing)
  - [Static Routes](#static-routes)
  - [Router BGP](#router-bgp)
- [Multicast](#multicast)
  - [IP IGMP Snooping](#ip-igmp-snooping)
- [VRF Instances](#vrf-instances)
  - [VRF Instances Summary](#vrf-instances-summary)
  - [VRF Instances Device Configuration](#vrf-instances-device-configuration)
- [EOS CLI Device Configuration](#eos-cli-device-configuration)

## Management

### Management Interfaces

#### Management Interfaces Summary

##### IPv4

| Management Interface | Description | Type | VRF | IP Address | Gateway |
| -------------------- | ----------- | ---- | --- | ---------- | ------- |
| Management1 | OOB_MANAGEMENT | oob | MGMT | 192.168.1.26/24 | 192.168.1.254 |

##### IPv6

| Management Interface | Description | Type | VRF | IPv6 Address | IPv6 Gateway |
| -------------------- | ----------- | ---- | --- | ------------ | ------------ |
| Management1 | OOB_MANAGEMENT | oob | MGMT | - | - |

#### Management Interfaces Device Configuration

```eos
!
interface Management1
   description OOB_MANAGEMENT
   no shutdown
   vrf MGMT
   ip address 192.168.1.26/24
```

### IP Domain-list

#### Domains List

- structured-config.set.under.vrf.common-vrf

#### IP Domain-list Device Configuration

```eos
ip domain-list structured-config.set.under.vrf.common-vrf
!
```

## Authentication

### Local Users

#### Local Users Summary

| User | Privilege | Role | Disabled | Shell |
| ---- | --------- | ---- | -------- | ----- |
| admin | 15 | network-admin | False | - |

#### Local Users Device Configuration

```eos
!
username admin privilege 15 role network-admin secret sha512 <removed>
```

### Enable Password

Enable password has been disabled

## Monitoring

### SNMP

#### SNMP Configuration Summary

| Contact | Location | SNMP Traps | State |
| ------- | -------- | ---------- | ----- |
| - | TWODC_5STAGE_CLOS DC1 DC1_POD1 DC1-POD1-LEAF1B | All | Disabled |

#### SNMP Device Configuration

```eos
!
snmp-server location TWODC_5STAGE_CLOS DC1 DC1_POD1 DC1-POD1-LEAF1B
```

## Spanning Tree

### Spanning Tree Summary

STP mode: **none**

### Spanning Tree Device Configuration

```eos
!
spanning-tree mode none
```

## Internal VLAN Allocation Policy

### Internal VLAN Allocation Policy Summary

| Policy Allocation | Range Beginning | Range Ending |
| ------------------| --------------- | ------------ |
| ascending | 1006 | 1199 |

### Internal VLAN Allocation Policy Device Configuration

```eos
!
vlan internal order ascending range 1006 1199
```

## VLANs

### VLANs Summary

| VLAN ID | Name | Trunk Groups |
| ------- | ---- | ------------ |
| 110 | Tenant_A_OP_Zone_1 | - |
| 111 | Tenant_A_OP_Zone_2 | - |
| 112 | Tenant_A_OP_Zone_3 | - |
| 113 | SVI_with_no_vxlan | - |
| 1100 | test_svi | - |
| 1101 | test_svi | - |
| 1102 | test_svi | - |
| 2500 | web-l2-vlan | - |
| 2600 | web-l2-vlan-2 | - |
| 2601 | l2vlan_with_no_vxlan | - |

### VLANs Device Configuration

```eos
!
vlan 110
   name Tenant_A_OP_Zone_1
!
vlan 111
   name Tenant_A_OP_Zone_2
!
vlan 112
   name Tenant_A_OP_Zone_3
!
vlan 113
   name SVI_with_no_vxlan
!
vlan 1100
   name test_svi
!
vlan 1101
   name test_svi
!
vlan 1102
   name test_svi
!
vlan 2500
   name web-l2-vlan
!
vlan 2600
   name web-l2-vlan-2
!
vlan 2601
   name l2vlan_with_no_vxlan
```

## Interfaces

### Ethernet Interfaces

#### Ethernet Interfaces Summary

##### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | Channel-Group |
| --------- | ----------- | ---- | ----- | ----------- | ----------- | ------------- |

*Inherited from Port-Channel Interface

##### Encapsulation Dot1q Interfaces

| Interface | Description | Vlan ID | Dot1q VLAN Tag | Dot1q Inner VLAN Tag |
| --------- | ----------- | ------- | -------------- | -------------------- |
| Ethernet1.1025 | P2P_DC1.POD1.LEAF2A_Ethernet13.1025_VRF_Common_VRF | - | 1025 | - |
| Ethernet1.1100 | P2P_DC1.POD1.LEAF2A_Ethernet13.1100_VRF_vrf_with_loopbacks_from_overlapping_pool | - | 1100 | - |
| Ethernet1.1101 | P2P_DC1.POD1.LEAF2A_Ethernet13.1101_VRF_vrf_with_loopbacks_from_pod_pools | - | 1101 | - |
| Ethernet1.1102 | P2P_DC1.POD1.LEAF2A_Ethernet13.1102_VRF_vrf_with_loopbacks_dc1_pod1_only | - | 1102 | - |
| Ethernet2.1025 | P2P_DC1-POD1-LEAF2B_Ethernet13.1025_VRF_Common_VRF | - | 1025 | - |
| Ethernet2.1100 | P2P_DC1-POD1-LEAF2B_Ethernet13.1100_VRF_vrf_with_loopbacks_from_overlapping_pool | - | 1100 | - |
| Ethernet2.1101 | P2P_DC1-POD1-LEAF2B_Ethernet13.1101_VRF_vrf_with_loopbacks_from_pod_pools | - | 1101 | - |
| Ethernet2.1102 | P2P_DC1-POD1-LEAF2B_Ethernet13.1102_VRF_vrf_with_loopbacks_dc1_pod1_only | - | 1102 | - |

##### IPv4

| Interface | Description | Channel Group | IP Address | VRF |  MTU | Shutdown | ACL In | ACL Out |
| --------- | ----------- | ------------- | ---------- | ----| ---- | -------- | ------ | ------- |
| Ethernet1 | P2P_DC1.POD1.LEAF2A_Ethernet13 | - | 172.17.110.13/31 | default | - | False | - | - |
| Ethernet1.1025 | P2P_DC1.POD1.LEAF2A_Ethernet13.1025_VRF_Common_VRF | - | 172.17.110.13/31 | Common_VRF | - | False | - | - |
| Ethernet1.1100 | P2P_DC1.POD1.LEAF2A_Ethernet13.1100_VRF_vrf_with_loopbacks_from_overlapping_pool | - | 172.17.110.13/31 | vrf_with_loopbacks_from_overlapping_pool | - | False | - | - |
| Ethernet1.1101 | P2P_DC1.POD1.LEAF2A_Ethernet13.1101_VRF_vrf_with_loopbacks_from_pod_pools | - | 172.17.110.13/31 | vrf_with_loopbacks_from_pod_pools | - | False | - | - |
| Ethernet1.1102 | P2P_DC1.POD1.LEAF2A_Ethernet13.1102_VRF_vrf_with_loopbacks_dc1_pod1_only | - | 172.17.110.13/31 | vrf_with_loopbacks_dc1_pod1_only | - | False | - | - |
| Ethernet2 | P2P_DC1-POD1-LEAF2B_Ethernet13 | - | 172.17.110.15/31 | default | - | False | - | - |
| Ethernet2.1025 | P2P_DC1-POD1-LEAF2B_Ethernet13.1025_VRF_Common_VRF | - | 172.17.110.15/31 | Common_VRF | - | False | - | - |
| Ethernet2.1100 | P2P_DC1-POD1-LEAF2B_Ethernet13.1100_VRF_vrf_with_loopbacks_from_overlapping_pool | - | 172.17.110.15/31 | vrf_with_loopbacks_from_overlapping_pool | - | False | - | - |
| Ethernet2.1101 | P2P_DC1-POD1-LEAF2B_Ethernet13.1101_VRF_vrf_with_loopbacks_from_pod_pools | - | 172.17.110.15/31 | vrf_with_loopbacks_from_pod_pools | - | False | - | - |
| Ethernet2.1102 | P2P_DC1-POD1-LEAF2B_Ethernet13.1102_VRF_vrf_with_loopbacks_dc1_pod1_only | - | 172.17.110.15/31 | vrf_with_loopbacks_dc1_pod1_only | - | False | - | - |

#### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet1
   description P2P_DC1.POD1.LEAF2A_Ethernet13
   no shutdown
   no switchport
   ip address 172.17.110.13/31
   mac security profile MACSEC_PROFILE
   ptp enable
   service-profile QOS-PROFILE
!
interface Ethernet1.1025
   description P2P_DC1.POD1.LEAF2A_Ethernet13.1025_VRF_Common_VRF
   no shutdown
   encapsulation dot1q vlan 1025
   vrf Common_VRF
   ip address 172.17.110.13/31
!
interface Ethernet1.1100
   description P2P_DC1.POD1.LEAF2A_Ethernet13.1100_VRF_vrf_with_loopbacks_from_overlapping_pool
   no shutdown
   encapsulation dot1q vlan 1100
   vrf vrf_with_loopbacks_from_overlapping_pool
   ip address 172.17.110.13/31
!
interface Ethernet1.1101
   description P2P_DC1.POD1.LEAF2A_Ethernet13.1101_VRF_vrf_with_loopbacks_from_pod_pools
   no shutdown
   encapsulation dot1q vlan 1101
   vrf vrf_with_loopbacks_from_pod_pools
   ip address 172.17.110.13/31
!
interface Ethernet1.1102
   description P2P_DC1.POD1.LEAF2A_Ethernet13.1102_VRF_vrf_with_loopbacks_dc1_pod1_only
   no shutdown
   encapsulation dot1q vlan 1102
   vrf vrf_with_loopbacks_dc1_pod1_only
   ip address 172.17.110.13/31
!
interface Ethernet2
   description P2P_DC1-POD1-LEAF2B_Ethernet13
   no shutdown
   no switchport
   ip address 172.17.110.15/31
   mac security profile MACSEC_PROFILE
   ptp enable
   service-profile QOS-PROFILE
!
interface Ethernet2.1025
   description P2P_DC1-POD1-LEAF2B_Ethernet13.1025_VRF_Common_VRF
   no shutdown
   encapsulation dot1q vlan 1025
   vrf Common_VRF
   ip address 172.17.110.15/31
!
interface Ethernet2.1100
   description P2P_DC1-POD1-LEAF2B_Ethernet13.1100_VRF_vrf_with_loopbacks_from_overlapping_pool
   no shutdown
   encapsulation dot1q vlan 1100
   vrf vrf_with_loopbacks_from_overlapping_pool
   ip address 172.17.110.15/31
!
interface Ethernet2.1101
   description P2P_DC1-POD1-LEAF2B_Ethernet13.1101_VRF_vrf_with_loopbacks_from_pod_pools
   no shutdown
   encapsulation dot1q vlan 1101
   vrf vrf_with_loopbacks_from_pod_pools
   ip address 172.17.110.15/31
!
interface Ethernet2.1102
   description P2P_DC1-POD1-LEAF2B_Ethernet13.1102_VRF_vrf_with_loopbacks_dc1_pod1_only
   no shutdown
   encapsulation dot1q vlan 1102
   vrf vrf_with_loopbacks_dc1_pod1_only
   ip address 172.17.110.15/31
```

### Loopback Interfaces

#### Loopback Interfaces Summary

##### IPv4

| Interface | Description | VRF | IP Address |
| --------- | ----------- | --- | ---------- |
| Loopback0 | ROUTER_ID | default | 172.16.110.6/32 |
| Loopback100 | DIAG_VRF_vrf_with_loopbacks_from_overlapping_pool | vrf_with_loopbacks_from_overlapping_pool | 10.100.0.6/32 |
| Loopback101 | DIAG_VRF_vrf_with_loopbacks_from_pod_pools | vrf_with_loopbacks_from_pod_pools | 10.101.101.6/32 |
| Loopback102 | DIAG_VRF_vrf_with_loopbacks_dc1_pod1_only | vrf_with_loopbacks_dc1_pod1_only | 10.102.101.6/32 |

##### IPv6

| Interface | Description | VRF | IPv6 Address |
| --------- | ----------- | --- | ------------ |
| Loopback0 | ROUTER_ID | default | - |
| Loopback100 | DIAG_VRF_vrf_with_loopbacks_from_overlapping_pool | vrf_with_loopbacks_from_overlapping_pool | - |
| Loopback101 | DIAG_VRF_vrf_with_loopbacks_from_pod_pools | vrf_with_loopbacks_from_pod_pools | 2001:db8:1::4/128 |
| Loopback102 | DIAG_VRF_vrf_with_loopbacks_dc1_pod1_only | vrf_with_loopbacks_dc1_pod1_only | - |

#### Loopback Interfaces Device Configuration

```eos
!
interface Loopback0
   description ROUTER_ID
   no shutdown
   ip address 172.16.110.6/32
!
interface Loopback100
   description DIAG_VRF_vrf_with_loopbacks_from_overlapping_pool
   no shutdown
   vrf vrf_with_loopbacks_from_overlapping_pool
   ip address 10.100.0.6/32
!
interface Loopback101
   description DIAG_VRF_vrf_with_loopbacks_from_pod_pools
   no shutdown
   vrf vrf_with_loopbacks_from_pod_pools
   ip address 10.101.101.6/32
   ipv6 address 2001:db8:1::4/128
!
interface Loopback102
   description DIAG_VRF_vrf_with_loopbacks_dc1_pod1_only
   no shutdown
   vrf vrf_with_loopbacks_dc1_pod1_only
   ip address 10.102.101.6/32
```

### VLAN Interfaces

#### VLAN Interfaces Summary

| Interface | Description | VRF |  MTU | Shutdown |
| --------- | ----------- | --- | ---- | -------- |
| Vlan110 | set from structured_config on svi (was Tenant_A_OP_Zone_1) | Common_VRF | - | False |
| Vlan111 | Tenant_A_OP_Zone_2 | Common_VRF | - | True |
| Vlan112 | Tenant_A_OP_Zone_3 | Common_VRF | - | False |
| Vlan113 | SVI_with_no_vxlan | Common_VRF | - | False |
| Vlan1100 | test_svi | vrf_with_loopbacks_from_overlapping_pool | - | False |
| Vlan1101 | test_svi | vrf_with_loopbacks_from_pod_pools | - | False |
| Vlan1102 | test_svi | vrf_with_loopbacks_dc1_pod1_only | - | False |

##### IPv4

| Interface | VRF | IP Address | IP Address Virtual | IP Router Virtual Address | ACL In | ACL Out |
| --------- | --- | ---------- | ------------------ | ------------------------- | ------ | ------- |
| Vlan110 |  Common_VRF  |  -  |  10.1.10.1/24  |  -  |  -  |  -  |
| Vlan111 |  Common_VRF  |  -  |  10.1.11.1/24  |  -  |  -  |  -  |
| Vlan112 |  Common_VRF  |  -  |  10.1.12.1/24  |  -  |  -  |  -  |
| Vlan113 |  Common_VRF  |  -  |  10.10.13.1/24  |  -  |  -  |  -  |
| Vlan1100 |  vrf_with_loopbacks_from_overlapping_pool  |  -  |  10.100.100.1/24  |  -  |  -  |  -  |
| Vlan1101 |  vrf_with_loopbacks_from_pod_pools  |  -  |  10.101.100.1/24  |  -  |  -  |  -  |
| Vlan1102 |  vrf_with_loopbacks_dc1_pod1_only  |  -  |  10.102.100.1/24  |  -  |  -  |  -  |

#### VLAN Interfaces Device Configuration

```eos
!
interface Vlan110
   description set from structured_config on svi (was Tenant_A_OP_Zone_1)
   no shutdown
   vrf Common_VRF
   ip address virtual 10.1.10.1/24
!
interface Vlan111
   description Tenant_A_OP_Zone_2
   shutdown
   vrf Common_VRF
   ip address virtual 10.1.11.1/24
!
interface Vlan112
   description Tenant_A_OP_Zone_3
   no shutdown
   vrf Common_VRF
   ip address virtual 10.1.12.1/24
   comment
   Comment created from raw_eos_cli under SVI 112 in VRF Common_VRF
   EOF

!
interface Vlan113
   description SVI_with_no_vxlan
   no shutdown
   vrf Common_VRF
   ip address virtual 10.10.13.1/24
!
interface Vlan1100
   description test_svi
   no shutdown
   vrf vrf_with_loopbacks_from_overlapping_pool
   ip address virtual 10.100.100.1/24
!
interface Vlan1101
   description test_svi
   no shutdown
   vrf vrf_with_loopbacks_from_pod_pools
   ip address virtual 10.101.100.1/24
!
interface Vlan1102
   description test_svi
   no shutdown
   vrf vrf_with_loopbacks_dc1_pod1_only
   ip address virtual 10.102.100.1/24
```

## Routing

### Service Routing Protocols Model

Multi agent routing protocol model enabled

```eos
!
service routing protocols model multi-agent
```

### Virtual Router MAC Address

#### Virtual Router MAC Address Summary

Virtual Router MAC Address: 00:1c:73:00:dc:01

#### Virtual Router MAC Address Device Configuration

```eos
!
ip virtual-router mac-address 00:1c:73:00:dc:01
```

### IP Routing

#### IP Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | True |
| Common_VRF | True |
| MGMT | False |
| vrf_with_loopbacks_dc1_pod1_only | True |
| vrf_with_loopbacks_from_overlapping_pool | True |
| vrf_with_loopbacks_from_pod_pools | True |

#### IP Routing Device Configuration

```eos
!
ip routing
ip routing vrf Common_VRF
no ip routing vrf MGMT
ip routing vrf vrf_with_loopbacks_dc1_pod1_only
ip routing vrf vrf_with_loopbacks_from_overlapping_pool
ip routing vrf vrf_with_loopbacks_from_pod_pools
```

### IPv6 Routing

#### IPv6 Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | False |
| Common_VRF | false |
| MGMT | false |
| vrf_with_loopbacks_dc1_pod1_only | false |
| vrf_with_loopbacks_from_overlapping_pool | false |
| vrf_with_loopbacks_from_pod_pools | false |

### Static Routes

#### Static Routes Summary

| VRF | Destination Prefix | Next Hop IP | Exit interface | Administrative Distance | Tag | Route Name | Metric |
| --- | ------------------ | ----------- | -------------- | ----------------------- | --- | ---------- | ------ |
| MGMT | 0.0.0.0/0 | 192.168.1.254 | - | 1 | - | - | - |

#### Static Routes Device Configuration

```eos
!
ip route vrf MGMT 0.0.0.0/0 192.168.1.254
```

### Router BGP

ASN Notation: asdot

#### Router BGP Summary

| BGP AS | Router ID |
| ------ | --------- |
| 65111.100 | 172.16.110.6 |

| BGP Tuning |
| ---------- |
| distance bgp 20 200 200 |
| update wait-install |
| no bgp default ipv4-unicast |
| maximum-paths 4 |

#### Router BGP Peer Groups

##### IPv4-UNDERLAY-PEERS

| Settings | Value |
| -------- | ----- |
| Address Family | ipv4 |
| Send community | all |
| Maximum routes | 12000 |

#### BGP Neighbors

| Neighbor | Remote AS | VRF | Shutdown | Send-community | Maximum-routes | Allowas-in | BFD | RIB Pre-Policy Retain | Route-Reflector Client | Passive | TTL Max Hops |
| -------- | --------- | --- | -------- | -------------- | -------------- | ---------- | --- | --------------------- | ---------------------- | ------- | ------------ |
| 172.17.110.12 | 65112.100 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - | - |
| 172.17.110.14 | 65112.100 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - | - |
| 172.17.110.12 | 65112.100 | Common_VRF | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - | - |
| 172.17.110.14 | 65112.100 | Common_VRF | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - | - |
| 172.17.110.12 | 65112.100 | vrf_with_loopbacks_dc1_pod1_only | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - | - |
| 172.17.110.14 | 65112.100 | vrf_with_loopbacks_dc1_pod1_only | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - | - |
| 172.17.110.12 | 65112.100 | vrf_with_loopbacks_from_overlapping_pool | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - | - |
| 172.17.110.14 | 65112.100 | vrf_with_loopbacks_from_overlapping_pool | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - | - |
| 172.17.110.12 | 65112.100 | vrf_with_loopbacks_from_pod_pools | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - | - |
| 172.17.110.14 | 65112.100 | vrf_with_loopbacks_from_pod_pools | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - | - |

#### Router BGP VRFs

| VRF | Route-Distinguisher | Redistribute | Graceful Restart |
| --- | ------------------- | ------------ | ---------------- |
| Common_VRF | 172.16.110.6:1025 | connected | - |
| vrf_with_loopbacks_dc1_pod1_only | 172.16.110.6:1102 | connected | - |
| vrf_with_loopbacks_from_overlapping_pool | 172.16.110.6:1100 | connected | - |
| vrf_with_loopbacks_from_pod_pools | 172.16.110.6:1101 | connected | - |

#### Router BGP Device Configuration

```eos
!
router bgp 65111.100
   bgp asn notation asdot
   router-id 172.16.110.6
   update wait-install
   no bgp default ipv4-unicast
   maximum-paths 4
   distance bgp 20 200 200
   neighbor IPv4-UNDERLAY-PEERS peer group
   neighbor IPv4-UNDERLAY-PEERS password 7 <removed>
   neighbor IPv4-UNDERLAY-PEERS send-community
   neighbor IPv4-UNDERLAY-PEERS maximum-routes 12000
   neighbor 172.17.110.12 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.110.12 remote-as 65112.100
   neighbor 172.17.110.12 description DC1.POD1.LEAF2A_Ethernet13
   neighbor 172.17.110.14 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.110.14 remote-as 65112.100
   neighbor 172.17.110.14 description DC1-POD1-LEAF2B_Ethernet13
   redistribute connected
   !
   address-family ipv4
      neighbor IPv4-UNDERLAY-PEERS activate
   !
   vrf Common_VRF
      rd 172.16.110.6:1025
      route-target import evpn 1025:1025
      route-target export evpn 1025:1025
      router-id 172.16.110.6
      neighbor 172.17.110.12 peer group IPv4-UNDERLAY-PEERS
      neighbor 172.17.110.12 remote-as 65112.100
      neighbor 172.17.110.12 description DC1.POD1.LEAF2A_Ethernet13.1025_vrf_Common_VRF
      neighbor 172.17.110.14 peer group IPv4-UNDERLAY-PEERS
      neighbor 172.17.110.14 remote-as 65112.100
      neighbor 172.17.110.14 description DC1-POD1-LEAF2B_Ethernet13.1025_vrf_Common_VRF
      redistribute connected
      !
      comment
      Comment created from raw_eos_cli under BGP for VRF Common_VRF
      EOF

   !
   vrf vrf_with_loopbacks_dc1_pod1_only
      rd 172.16.110.6:1102
      route-target import evpn 1102:1102
      route-target export evpn 1102:1102
      router-id 172.16.110.6
      neighbor 172.17.110.12 peer group IPv4-UNDERLAY-PEERS
      neighbor 172.17.110.12 remote-as 65112.100
      neighbor 172.17.110.12 description DC1.POD1.LEAF2A_Ethernet13.1102_vrf_vrf_with_loopbacks_dc1_pod1_only
      neighbor 172.17.110.14 peer group IPv4-UNDERLAY-PEERS
      neighbor 172.17.110.14 remote-as 65112.100
      neighbor 172.17.110.14 description DC1-POD1-LEAF2B_Ethernet13.1102_vrf_vrf_with_loopbacks_dc1_pod1_only
      redistribute connected
   !
   vrf vrf_with_loopbacks_from_overlapping_pool
      rd 172.16.110.6:1100
      route-target import evpn 1100:1100
      route-target export evpn 1100:1100
      router-id 172.16.110.6
      neighbor 172.17.110.12 peer group IPv4-UNDERLAY-PEERS
      neighbor 172.17.110.12 remote-as 65112.100
      neighbor 172.17.110.12 description DC1.POD1.LEAF2A_Ethernet13.1100_vrf_vrf_with_loopbacks_from_overlapping_pool
      neighbor 172.17.110.14 peer group IPv4-UNDERLAY-PEERS
      neighbor 172.17.110.14 remote-as 65112.100
      neighbor 172.17.110.14 description DC1-POD1-LEAF2B_Ethernet13.1100_vrf_vrf_with_loopbacks_from_overlapping_pool
      redistribute connected
   !
   vrf vrf_with_loopbacks_from_pod_pools
      rd 172.16.110.6:1101
      route-target import evpn 1101:1101
      route-target export evpn 1101:1101
      router-id 172.16.110.6
      neighbor 172.17.110.12 peer group IPv4-UNDERLAY-PEERS
      neighbor 172.17.110.12 remote-as 65112.100
      neighbor 172.17.110.12 description DC1.POD1.LEAF2A_Ethernet13.1101_vrf_vrf_with_loopbacks_from_pod_pools
      neighbor 172.17.110.14 peer group IPv4-UNDERLAY-PEERS
      neighbor 172.17.110.14 remote-as 65112.100
      neighbor 172.17.110.14 description DC1-POD1-LEAF2B_Ethernet13.1101_vrf_vrf_with_loopbacks_from_pod_pools
      redistribute connected
```

## Multicast

### IP IGMP Snooping

#### IP IGMP Snooping Summary

| IGMP Snooping | Fast Leave | Interface Restart Query | Proxy | Restart Query Interval | Robustness Variable |
| ------------- | ---------- | ----------------------- | ----- | ---------------------- | ------------------- |
| Enabled | - | - | - | - | - |

#### IP IGMP Snooping Device Configuration

```eos
```

## VRF Instances

### VRF Instances Summary

| VRF Name | IP Routing |
| -------- | ---------- |
| Common_VRF | enabled |
| MGMT | disabled |
| vrf_with_loopbacks_dc1_pod1_only | enabled |
| vrf_with_loopbacks_from_overlapping_pool | enabled |
| vrf_with_loopbacks_from_pod_pools | enabled |

### VRF Instances Device Configuration

```eos
!
vrf instance Common_VRF
!
vrf instance MGMT
!
vrf instance vrf_with_loopbacks_dc1_pod1_only
!
vrf instance vrf_with_loopbacks_from_overlapping_pool
!
vrf instance vrf_with_loopbacks_from_pod_pools
```

## EOS CLI Device Configuration

```eos
!
interface Loopback1001
  description Loopback created from raw_eos_cli under node-group RACK1_SINGLE

interface Loopback1111
  description Loopback created from raw_eos_cli under platform_settings vEOS-LAB

interface Loopback1000
  description Loopback created from raw_eos_cli under VRF Common_VRF

```
