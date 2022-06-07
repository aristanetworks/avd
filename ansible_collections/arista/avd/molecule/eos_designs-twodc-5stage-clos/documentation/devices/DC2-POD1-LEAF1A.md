# DC2-POD1-LEAF1A
# Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
  - [Domain-list](#domain-list)
  - [Management API HTTP](#management-api-http)
- [Authentication](#authentication)
  - [Local Users](#local-users)
- [Monitoring](#monitoring)
  - [SNMP](#snmp)
- [Spanning Tree](#spanning-tree)
  - [Spanning Tree Summary](#spanning-tree-summary)
  - [Spanning Tree Device Configuration](#spanning-tree-device-configuration)
- [Internal VLAN Allocation Policy](#internal-vlan-allocation-policy)
  - [Internal VLAN Allocation Policy Summary](#internal-vlan-allocation-policy-summary)
  - [Internal VLAN Allocation Policy Configuration](#internal-vlan-allocation-policy-configuration)
- [VLANs](#vlans)
  - [VLANs Summary](#vlans-summary)
  - [VLANs Device Configuration](#vlans-device-configuration)
- [Interfaces](#interfaces)
  - [Ethernet Interfaces](#ethernet-interfaces)
  - [Port-Channel Interfaces](#port-channel-interfaces)
  - [Loopback Interfaces](#loopback-interfaces)
  - [VLAN Interfaces](#vlan-interfaces)
  - [VXLAN Interface](#vxlan-interface)
- [Routing](#routing)
  - [Service Routing Protocols Model](#service-routing-protocols-model)
  - [Virtual Router MAC Address](#virtual-router-mac-address)
  - [IP Routing](#ip-routing)
  - [IPv6 Routing](#ipv6-routing)
  - [Static Routes](#static-routes)
  - [Router BGP](#router-bgp)
- [BFD](#bfd)
  - [Router BFD](#router-bfd)
- [Multicast](#multicast)
  - [IP IGMP Snooping](#ip-igmp-snooping)
- [Filters](#filters)
  - [Prefix-lists](#prefix-lists)
  - [Route-maps](#route-maps)
- [ACL](#acl)
- [VRF Instances](#vrf-instances)
  - [VRF Instances Summary](#vrf-instances-summary)
  - [VRF Instances Device Configuration](#vrf-instances-device-configuration)
- [Virtual Source NAT](#virtual-source-nat)
  - [Virtual Source NAT Summary](#virtual-source-nat-summary)
  - [Virtual Source NAT Configuration](#virtual-source-nat-configuration)
- [Quality Of Service](#quality-of-service)
- [EOS CLI](#eos-cli)

# Management

## Management Interfaces

### Management Interfaces Summary

#### IPv4

| Management Interface | description | Type | VRF | IP Address | Gateway |
| -------------------- | ----------- | ---- | --- | ---------- | ------- |
| Management1 | oob_management | oob | MGMT | 192.168.1.22/24 | 192.168.1.254 |

#### IPv6

| Management Interface | description | Type | VRF | IPv6 Address | IPv6 Gateway |
| -------------------- | ----------- | ---- | --- | ------------ | ------------ |
| Management1 | oob_management | oob | MGMT | -  | - |

### Management Interfaces Device Configuration

```eos
!
interface Management1
   description oob_management
   no shutdown
   vrf MGMT
   ip address 192.168.1.22/24
```

## Domain-list

### Domain-list:
 - structured-config.set.under.vrf.common-vrf

### Domain-list Device Configuration

```eos
ip domain-list structured-config.set.under.vrf.common-vrf
!
```

## Management API HTTP

### Management API HTTP Summary

| HTTP | HTTPS | Default Services |
| ---- | ----- | ---------------- |
| False | True | - |

### Management API VRF Access

| VRF Name | IPv4 ACL | IPv6 ACL |
| -------- | -------- | -------- |
| MGMT | - | - |

### Management API HTTP Configuration

```eos
!
management api http-commands
   protocol https
   no shutdown
   !
   vrf MGMT
      no shutdown
```

# Authentication

## Local Users

### Local Users Summary

| User | Privilege | Role |
| ---- | --------- | ---- |
| admin | 15 | network-admin |

### Local Users Device Configuration

```eos
!
username admin privilege 15 role network-admin secret sha512 $6$eJ5TvI8oru5i9e8G$R1X/SbtGTk9xoEHEBQASc7SC2nHYmi.crVgp2pXuCXwxsXEA81e4E0cXgQ6kX08fIeQzauqhv2kS.RGJFCon5/
```

# Monitoring

## SNMP

### SNMP Configuration Summary

| Contact | Location | SNMP Traps | State |
| ------- | -------- | ---------- | ----- |
| - | TWODC_5STAGE_CLOS DC2 DC2_POD1 DC2-POD1-LEAF1A | All | Disabled |

### SNMP Device Configuration

```eos
!
snmp-server location TWODC_5STAGE_CLOS DC2 DC2_POD1 DC2-POD1-LEAF1A
```

# Spanning Tree

## Spanning Tree Summary

STP mode: **rstp**

### Global Spanning-Tree Settings

- Global RSTP priority: 4096

## Spanning Tree Device Configuration

```eos
!
spanning-tree mode rstp
spanning-tree priority 4096
```

# Internal VLAN Allocation Policy

## Internal VLAN Allocation Policy Summary

| Policy Allocation | Range Beginning | Range Ending |
| ------------------| --------------- | ------------ |
| ascending | 1006 | 1199 |

## Internal VLAN Allocation Policy Configuration

```eos
!
vlan internal order ascending range 1006 1199
```

# VLANs

## VLANs Summary

| VLAN ID | Name | Trunk Groups |
| ------- | ---- | ------------ |
| 4092 | L2LEAF_INBAND_MGMT | - |

## VLANs Device Configuration

```eos
!
vlan 4092
   name L2LEAF_INBAND_MGMT
```

# Interfaces

## Ethernet Interfaces

### Ethernet Interfaces Summary

#### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | Channel-Group |
| --------- | ----------- | ---- | ----- | ----------- | ----------- | ------------- |
| Ethernet3 | DC2-POD1-L2LEAF1A_Ethernet1 | *trunk | *4092 | *- | *- | 3 |

*Inherited from Port-Channel Interface

#### IPv4

| Interface | Description | Type | Channel Group | IP Address | VRF |  MTU | Shutdown | ACL In | ACL Out |
| --------- | ----------- | -----| ------------- | ---------- | ----| ---- | -------- | ------ | ------- |
| Ethernet1 | P2P_LINK_TO_DC2-POD1-SPINE1_Ethernet3 | routed | - | 172.17.210.1/31 | default | 1500 | false | - | - |
| Ethernet2 | P2P_LINK_TO_DC2-POD1-SPINE2_Ethernet3 | routed | - | 172.17.210.3/31 | default | 1500 | false | - | - |
| Ethernet6 | P2P_LINK_TO_DC1.POD1.LEAF2A_Ethernet7 | routed | - | 100.100.100.201/24 | default | 1500 | false | - | - |
| Ethernet7 | P2P_LINK_TO_DC1-POD1-LEAF2B_Ethernet7 | routed | - | 11.1.0.39/31 | default | 1499 | false | - | - |

### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet1
   description P2P_LINK_TO_DC2-POD1-SPINE1_Ethernet3
   no shutdown
   mtu 1500
   no switchport
   ip address 172.17.210.1/31
   ptp enable
   service-profile QOS-PROFILE
!
interface Ethernet2
   description P2P_LINK_TO_DC2-POD1-SPINE2_Ethernet3
   no shutdown
   mtu 1500
   no switchport
   ip address 172.17.210.3/31
   ptp enable
   service-profile QOS-PROFILE
!
interface Ethernet3
   description DC2-POD1-L2LEAF1A_Ethernet1
   no shutdown
   channel-group 3 mode active
!
interface Ethernet6
   description P2P_LINK_TO_DC1.POD1.LEAF2A_Ethernet7
   no shutdown
   mtu 1500
   no switchport
   ip address 100.100.100.201/24
!
interface Ethernet7
   description P2P_LINK_TO_DC1-POD1-LEAF2B_Ethernet7
   no shutdown
   mtu 1499
   no switchport
   ip address 11.1.0.39/31
   ptp enable
```

## Port-Channel Interfaces

### Port-Channel Interfaces Summary

#### L2

| Interface | Description | Type | Mode | VLANs | Native VLAN | Trunk Group | LACP Fallback Timeout | LACP Fallback Mode | MLAG ID | EVPN ESI |
| --------- | ----------- | ---- | ---- | ----- | ----------- | ------------| --------------------- | ------------------ | ------- | -------- |
| Port-Channel3 | DC2-POD1-L2LEAF1A_Po1 | switched | trunk | 4092 | - | - | - | - | - | - |

### Port-Channel Interfaces Device Configuration

```eos
!
interface Port-Channel3
   description DC2-POD1-L2LEAF1A_Po1
   no shutdown
   switchport
   switchport trunk allowed vlan 4092
   switchport mode trunk
   service-profile QOS-PROFILE
```

## Loopback Interfaces

### Loopback Interfaces Summary

#### IPv4

| Interface | Description | VRF | IP Address |
| --------- | ----------- | --- | ---------- |
| Loopback0 | EVPN_Overlay_Peering | default | 172.16.210.3/32 |
| Loopback1 | VTEP_VXLAN_Tunnel_Source | default | 172.18.210.3/32 |
| Loopback100 | vrf_with_loopbacks_from_overlapping_pool_VTEP_DIAGNOSTICS | vrf_with_loopbacks_from_overlapping_pool | 10.100.0.3/32 |
| Loopback101 | vrf_with_loopbacks_from_pod_pools_VTEP_DIAGNOSTICS | vrf_with_loopbacks_from_pod_pools | 10.101.201.3/32 |

#### IPv6

| Interface | Description | VRF | IPv6 Address |
| --------- | ----------- | --- | ------------ |
| Loopback0 | EVPN_Overlay_Peering | default | - |
| Loopback1 | VTEP_VXLAN_Tunnel_Source | default | - |
| Loopback100 | vrf_with_loopbacks_from_overlapping_pool_VTEP_DIAGNOSTICS | vrf_with_loopbacks_from_overlapping_pool | - |
| Loopback101 | vrf_with_loopbacks_from_pod_pools_VTEP_DIAGNOSTICS | vrf_with_loopbacks_from_pod_pools | - |


### Loopback Interfaces Device Configuration

```eos
!
interface Loopback0
   description EVPN_Overlay_Peering
   no shutdown
   ip address 172.16.210.3/32
!
interface Loopback1
   description VTEP_VXLAN_Tunnel_Source
   no shutdown
   ip address 172.18.210.3/32
!
interface Loopback100
   description vrf_with_loopbacks_from_overlapping_pool_VTEP_DIAGNOSTICS
   no shutdown
   vrf vrf_with_loopbacks_from_overlapping_pool
   ip address 10.100.0.3/32
!
interface Loopback101
   description vrf_with_loopbacks_from_pod_pools_VTEP_DIAGNOSTICS
   no shutdown
   vrf vrf_with_loopbacks_from_pod_pools
   ip address 10.101.201.3/32
```

## VLAN Interfaces

### VLAN Interfaces Summary

| Interface | Description | VRF |  MTU | Shutdown |
| --------- | ----------- | --- | ---- | -------- |
| Vlan4092 | L2LEAF_INBAND_MGMT | default | 1500 | false |

#### IPv4

| Interface | VRF | IP Address | IP Address Virtual | IP Router Virtual Address | VRRP | ACL In | ACL Out |
| --------- | --- | ---------- | ------------------ | ------------------------- | ---- | ------ | ------- |
| Vlan4092 |  default  |  172.21.210.2/24  |  -  |  172.21.210.1  |  -  |  -  |  -  |

### VLAN Interfaces Device Configuration

```eos
!
interface Vlan4092
   description L2LEAF_INBAND_MGMT
   no shutdown
   mtu 1500
   ip address 172.21.210.2/24
   ip attached-host route export 19
   ip virtual-router address 172.21.210.1
```

## VXLAN Interface

### VXLAN Interface Summary

| Setting | Value |
| ------- | ----- |
| Source Interface | Loopback1 |
| UDP port | 4789 |

#### VRF to VNI and Multicast Group Mappings

| VRF | VNI | Multicast Group |
| ---- | --- | --------------- |
| Common_VRF | 1025 | - |
| vrf_with_loopbacks_dc1_pod1_only | 1102 | - |
| vrf_with_loopbacks_from_overlapping_pool | 1100 | - |
| vrf_with_loopbacks_from_pod_pools | 1101 | - |

### VXLAN Interface Device Configuration

```eos
!
interface Vxlan1
   description DC2-POD1-LEAF1A_VTEP
   vxlan source-interface Loopback1
   vxlan udp-port 4789
   vxlan vrf Common_VRF vni 1025
   vxlan vrf vrf_with_loopbacks_dc1_pod1_only vni 1102
   vxlan vrf vrf_with_loopbacks_from_overlapping_pool vni 1100
   vxlan vrf vrf_with_loopbacks_from_pod_pools vni 1101
```

# Routing
## Service Routing Protocols Model

Multi agent routing protocol model enabled

```eos
!
service routing protocols model multi-agent
```

## Virtual Router MAC Address

### Virtual Router MAC Address Summary

#### Virtual Router MAC Address: 00:1c:73:00:dc:01

### Virtual Router MAC Address Configuration

```eos
!
ip virtual-router mac-address 00:1c:73:00:dc:01
```

## IP Routing

### IP Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | true |
| Common_VRF | true |
| MGMT | false |
| vrf_with_loopbacks_dc1_pod1_only | true |
| vrf_with_loopbacks_from_overlapping_pool | true |
| vrf_with_loopbacks_from_pod_pools | true |

### IP Routing Device Configuration

```eos
!
ip routing
ip routing vrf Common_VRF
no ip routing vrf MGMT
ip routing vrf vrf_with_loopbacks_dc1_pod1_only
ip routing vrf vrf_with_loopbacks_from_overlapping_pool
ip routing vrf vrf_with_loopbacks_from_pod_pools
```
## IPv6 Routing

### IPv6 Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | false |
| Common_VRF | false |
| MGMT | false |
| vrf_with_loopbacks_dc1_pod1_only | false |
| vrf_with_loopbacks_from_overlapping_pool | false |
| vrf_with_loopbacks_from_pod_pools | false |

## Static Routes

### Static Routes Summary

| VRF | Destination Prefix | Next Hop IP             | Exit interface      | Administrative Distance       | Tag               | Route Name                    | Metric         |
| --- | ------------------ | ----------------------- | ------------------- | ----------------------------- | ----------------- | ----------------------------- | -------------- |
| MGMT | 0.0.0.0/0 | 192.168.1.254 | - | 1 | - | - | - |

### Static Routes Device Configuration

```eos
!
ip route vrf MGMT 0.0.0.0/0 192.168.1.254
```

## Router BGP

### Router BGP Summary

| BGP AS | Router ID |
| ------ | --------- |
| 65211|  172.16.210.3 |

| BGP Tuning |
| ---------- |
| no bgp default ipv4-unicast |
| distance bgp 20 200 200 |
| graceful-restart restart-time 300 |
| graceful-restart |
| maximum-paths 4 ecmp 4 |

### Router BGP Peer Groups

#### EVPN-OVERLAY-PEERS

| Settings | Value |
| -------- | ----- |
| Address Family | evpn |
| Next-hop unchanged | True |
| Source | Loopback0 |
| BFD | True |
| Ebgp multihop | 5 |
| Send community | all |
| Maximum routes | 0 (no limit) |

#### IPv4-UNDERLAY-PEERS

| Settings | Value |
| -------- | ----- |
| Address Family | ipv4 |
| Send community | all |
| Maximum routes | 12000 |

### BGP Neighbors

| Neighbor | Remote AS | VRF | Shutdown | Send-community | Maximum-routes | Allowas-in | BFD | RIB Pre-Policy Retain |
| -------- | --------- | --- | -------- | -------------- | -------------- | ---------- | --- | --------------------- |
| 11.1.0.38 | 65120 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | True | - |
| 100.100.100.101 | 65112.100 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - |
| 172.16.10.1 | 65101 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - |
| 172.16.10.2 | 65102 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - |
| 172.16.110.1 | 65110.100 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - |
| 172.16.110.3 | 65111.100 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - |
| 172.16.210.4 | 65212 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - |
| 172.17.210.0 | 65210 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - |
| 172.17.210.2 | 65210 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - |

### Router BGP EVPN Address Family

#### EVPN Peer Groups

| Peer Group | Activate |
| ---------- | -------- |
| EVPN-OVERLAY-PEERS | True |

### Router BGP VRFs

| VRF | Route-Distinguisher | Redistribute |
| --- | ------------------- | ------------ |
| Common_VRF | 172.16.210.3:1025 | connected |
| vrf_with_loopbacks_dc1_pod1_only | 172.16.210.3:1102 | connected |
| vrf_with_loopbacks_from_overlapping_pool | 172.16.210.3:1100 | connected |
| vrf_with_loopbacks_from_pod_pools | 172.16.210.3:1101 | connected |

### Router BGP Device Configuration

```eos
!
router bgp 65211
   router-id 172.16.210.3
   no bgp default ipv4-unicast
   distance bgp 20 200 200
   graceful-restart restart-time 300
   graceful-restart
   maximum-paths 4 ecmp 4
   neighbor EVPN-OVERLAY-PEERS peer group
   neighbor EVPN-OVERLAY-PEERS next-hop-unchanged
   neighbor EVPN-OVERLAY-PEERS update-source Loopback0
   neighbor EVPN-OVERLAY-PEERS bfd
   neighbor EVPN-OVERLAY-PEERS ebgp-multihop 5
   neighbor EVPN-OVERLAY-PEERS send-community
   neighbor EVPN-OVERLAY-PEERS maximum-routes 0
   neighbor IPv4-UNDERLAY-PEERS peer group
   neighbor IPv4-UNDERLAY-PEERS send-community
   neighbor IPv4-UNDERLAY-PEERS maximum-routes 12000
   neighbor 11.1.0.38 peer group IPv4-UNDERLAY-PEERS
   neighbor 11.1.0.38 remote-as 65120
   neighbor 11.1.0.38 description DC1-POD1-LEAF2B
   neighbor 11.1.0.38 bfd
   neighbor 100.100.100.101 peer group IPv4-UNDERLAY-PEERS
   neighbor 100.100.100.101 remote-as 65112.100
   neighbor 100.100.100.101 description DC1.POD1.LEAF2A
   neighbor 172.16.10.1 peer group EVPN-OVERLAY-PEERS
   neighbor 172.16.10.1 remote-as 65101
   neighbor 172.16.10.1 description DC1-RS1
   neighbor 172.16.10.2 peer group EVPN-OVERLAY-PEERS
   neighbor 172.16.10.2 remote-as 65102
   neighbor 172.16.10.2 description DC1-RS2
   neighbor 172.16.110.1 peer group EVPN-OVERLAY-PEERS
   neighbor 172.16.110.1 remote-as 65110.100
   neighbor 172.16.110.1 description DC1-POD1-SPINE1
   neighbor 172.16.110.3 peer group EVPN-OVERLAY-PEERS
   neighbor 172.16.110.3 remote-as 65111.100
   neighbor 172.16.110.3 description DC1-POD1-LEAF1A
   neighbor 172.16.210.4 peer group EVPN-OVERLAY-PEERS
   neighbor 172.16.210.4 remote-as 65212
   neighbor 172.16.210.4 description DC2-POD1-LEAF2A
   neighbor 172.17.210.0 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.210.0 remote-as 65210
   neighbor 172.17.210.0 description DC2-POD1-SPINE1_Ethernet3
   neighbor 172.17.210.2 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.210.2 remote-as 65210
   neighbor 172.17.210.2 description DC2-POD1-SPINE2_Ethernet3
   redistribute attached-host
   redistribute connected route-map RM-CONN-2-BGP
   !
   address-family evpn
      neighbor EVPN-OVERLAY-PEERS activate
   !
   address-family rt-membership
      neighbor EVPN-OVERLAY-PEERS activate
      neighbor EVPN-OVERLAY-PEERS default-route-target only
   !
   address-family ipv4
      no neighbor EVPN-OVERLAY-PEERS activate
      neighbor IPv4-UNDERLAY-PEERS activate
   !
   vrf Common_VRF
      rd 172.16.210.3:1025
      route-target import evpn 1025:1025
      route-target export evpn 1025:1025
      router-id 172.16.210.3
      redistribute connected
      !
      comment
      Comment created from raw_eos_cli under BGP for VRF Common_VRF
      EOF

   !
   vrf vrf_with_loopbacks_dc1_pod1_only
      rd 172.16.210.3:1102
      route-target import evpn 1102:1102
      route-target export evpn 1102:1102
      router-id 172.16.210.3
      redistribute connected
   !
   vrf vrf_with_loopbacks_from_overlapping_pool
      rd 172.16.210.3:1100
      route-target import evpn 1100:1100
      route-target export evpn 1100:1100
      router-id 172.16.210.3
      redistribute connected
   !
   vrf vrf_with_loopbacks_from_pod_pools
      rd 172.16.210.3:1101
      route-target import evpn 1101:1101
      route-target export evpn 1101:1101
      router-id 172.16.210.3
      redistribute connected
```

# BFD

## Router BFD

### Router BFD Multihop Summary

| Interval | Minimum RX | Multiplier |
| -------- | ---------- | ---------- |
| 300 | 300 | 3 |

### Router BFD Device Configuration

```eos
!
router bfd
   multihop interval 300 min-rx 300 multiplier 3
```

# Multicast

## IP IGMP Snooping

### IP IGMP Snooping Summary

| IGMP Snooping | Fast Leave | Interface Restart Query | Proxy | Restart Query Interval | Robustness Variable |
| ------------- | ---------- | ----------------------- | ----- | ---------------------- | ------------------- |
| Enabled | - | - | - | - | - |

### IP IGMP Snooping Device Configuration

```eos
```

# Filters

## Prefix-lists

### Prefix-lists Summary

#### PL-L2LEAF-INBAND-MGMT

| Sequence | Action |
| -------- | ------ |
| 10 | permit 172.21.210.0/24 |

#### PL-LOOPBACKS-EVPN-OVERLAY

| Sequence | Action |
| -------- | ------ |
| 10 | permit 172.16.210.0/24 eq 32 |
| 20 | permit 172.18.210.0/24 eq 32 |

### Prefix-lists Device Configuration

```eos
!
ip prefix-list PL-L2LEAF-INBAND-MGMT
   seq 10 permit 172.21.210.0/24
!
ip prefix-list PL-LOOPBACKS-EVPN-OVERLAY
   seq 10 permit 172.16.210.0/24 eq 32
   seq 20 permit 172.18.210.0/24 eq 32
```

## Route-maps

### Route-maps Summary

#### RM-CONN-2-BGP

| Sequence | Type | Match and/or Set |
| -------- | ---- | ---------------- |
| 10 | permit | match ip address prefix-list PL-LOOPBACKS-EVPN-OVERLAY |
| 20 | permit | match ip address prefix-list PL-L2LEAF-INBAND-MGMT |

### Route-maps Device Configuration

```eos
!
route-map RM-CONN-2-BGP permit 10
   match ip address prefix-list PL-LOOPBACKS-EVPN-OVERLAY
!
route-map RM-CONN-2-BGP permit 20
   match ip address prefix-list PL-L2LEAF-INBAND-MGMT
```

# ACL

# VRF Instances

## VRF Instances Summary

| VRF Name | IP Routing |
| -------- | ---------- |
| Common_VRF | enabled |
| MGMT | disabled |
| vrf_with_loopbacks_dc1_pod1_only | enabled |
| vrf_with_loopbacks_from_overlapping_pool | enabled |
| vrf_with_loopbacks_from_pod_pools | enabled |

## VRF Instances Device Configuration

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

# Virtual Source NAT

## Virtual Source NAT Summary

| Source NAT VRF | Source NAT IP Address |
| -------------- | --------------------- |
| vrf_with_loopbacks_from_overlapping_pool | 10.100.0.3 |
| vrf_with_loopbacks_from_pod_pools | 10.101.201.3 |

## Virtual Source NAT Configuration

```eos
!
ip address virtual source-nat vrf vrf_with_loopbacks_from_overlapping_pool address 10.100.0.3
ip address virtual source-nat vrf vrf_with_loopbacks_from_pod_pools address 10.101.201.3
```

# Quality Of Service

# EOS CLI

```eos
!
interface Loopback1010
  description Loopback created from raw_eos_cli under l3leaf defaults in DC2 POD1

interface Loopback1111
  description Loopback created from raw_eos_cli under platform_settings vEOS-LAB

interface Loopback1000
  description Loopback created from raw_eos_cli under VRF Common_VRF

```
