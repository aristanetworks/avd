# digital-twin-ethernet-ports-1

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
  - [Management API HTTP](#management-api-http)
- [Authentication](#authentication)
  - [Enable Password](#enable-password)
- [MLAG](#mlag)
  - [MLAG Summary](#mlag-summary)
  - [MLAG Device Configuration](#mlag-device-configuration)
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
  - [Port-Channel Interfaces](#port-channel-interfaces)
  - [Loopback Interfaces](#loopback-interfaces)
  - [VLAN Interfaces](#vlan-interfaces)
  - [VXLAN Interface](#vxlan-interface)
- [Routing](#routing)
  - [Service Routing Protocols Model](#service-routing-protocols-model)
  - [IP Routing](#ip-routing)
  - [IPv6 Routing](#ipv6-routing)
  - [Router BGP](#router-bgp)
- [BFD](#bfd)
  - [Router BFD](#router-bfd)
- [Multicast](#multicast)
  - [IP IGMP Snooping](#ip-igmp-snooping)
- [Filters](#filters)
  - [Prefix-lists](#prefix-lists)
  - [Route-maps](#route-maps)
- [VRF Instances](#vrf-instances)
  - [VRF Instances Summary](#vrf-instances-summary)
  - [VRF Instances Device Configuration](#vrf-instances-device-configuration)

## Management

### Management Interfaces

#### Management Interfaces Summary

##### IPv4

| Management Interface | Description | Type | VRF | IP Address | Gateway |
| -------------------- | ----------- | ---- | --- | ---------- | ------- |
| Management1 | OOB_MANAGEMENT | oob | MGMT | 192.169.3.1/32 | - |

##### IPv6

| Management Interface | Description | Type | VRF | IPv6 Address | IPv6 Gateway | ND RA Disabled | ND RA RX Accept | ND Managed Config Flag | ND Other Config Flag | ND Cache | ND RA DNS Servers |
| -------------------- | ----------- | ---- | --- | ------------ | ------------ | -------------- | --------------- | ---------------------- | -------------------- | -------- | ----------------- |
| Management1 | OOB_MANAGEMENT | oob | MGMT | - | - | - | - | - | - | - | - |

#### Management Interfaces Device Configuration

```eos
!
interface Management1
   description OOB_MANAGEMENT
   no shutdown
   vrf MGMT
   ip address 192.169.3.1/32
```

### Management API HTTP

#### Management API HTTP Summary

| HTTP | HTTPS | UNIX-Socket | Default Services | Session Timeout |
| ---- | ----- | ----------- | ---------------- | --------------- |
| False | True | - | - | 1440 minutes |

#### Management API VRF Access

| VRF Name | IPv4 ACL | IPv6 ACL |
| -------- | -------- | -------- |
| MGMT | - | - |

#### Management API HTTP Device Configuration

```eos
!
management api http-commands
   protocol https
   no shutdown
   !
   vrf MGMT
      no shutdown
```

## Authentication

### Enable Password

Enable password has been disabled

## MLAG

### MLAG Summary

| Domain-id | Local-interface | Peer-address | Peer-link |
| --------- | --------------- | ------------ | --------- |
| NODE_GROUP_A | Vlan4094 | 192.168.3.97 | Port-Channel4 |

Dual primary detection is disabled.

### MLAG Device Configuration

```eos
!
mlag configuration
   domain-id NODE_GROUP_A
   local-interface Vlan4094
   peer-address 192.168.3.97
   peer-link Port-Channel4
   reload-delay mlag 300
   reload-delay non-mlag 330
```

## Spanning Tree

### Spanning Tree Summary

STP mode: **mstp**

#### Global Spanning-Tree Settings

- Spanning Tree disabled for VLANs: **4093-4094**

### Spanning Tree Device Configuration

```eos
!
no spanning-tree vlan-id 4093-4094
```

## Internal VLAN Allocation Policy

### Internal VLAN Allocation Policy Summary

| Policy Allocation | Range Beginning | Range Ending |
| ----------------- | --------------- | ------------ |
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
| 1 | TENANT_A_VRF_A_SVI_A | - |
| 4093 | MLAG_L3 | MLAG |
| 4094 | MLAG | MLAG |

### VLANs Device Configuration

```eos
!
vlan 1
   name TENANT_A_VRF_A_SVI_A
!
vlan 4093
   name MLAG_L3
   trunk group MLAG
!
vlan 4094
   name MLAG
   trunk group MLAG
```

## Interfaces

### Ethernet Interfaces

#### Ethernet Interfaces Summary

##### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | Channel-Group |
| --------- | ----------- | ---- | ----- | ----------- | ----------- | ------------- |
| Ethernet1 | FIREWALL_firewall-1_Eth1 | - | - | - | - | - |
| Ethernet2 | - | - | - | - | - | - |
| Ethernet4 | MLAG_digital.twin.ethernet.ports.2_Ethernet4 | *trunk | *- | *- | *MLAG | 4 |
| Ethernet5 | MLAG_digital.twin.ethernet.ports.2_Ethernet5 | *trunk | *- | *- | *MLAG | 4 |
| Ethernet9 | FIREWALL_firewall-1_Eth3 | *- | *- | *- | *- | 9 |
| Ethernet16 | - | *- | *- | *- | *- | 16 |

*Inherited from Port-Channel Interface

##### Encapsulation Dot1q Interfaces

| Interface | Description | Vlan ID | Dot1q VLAN Tag | Dot1q Inner VLAN Tag |
| --------- | ----------- | ------- | -------------- | -------------------- |
| Ethernet10.100 | - | - | 100 | - |
| Ethernet10.101 | - | - | 101 | - |
| Ethernet20.100 | - | - | 100 | - |
| Ethernet21.100 | - | - | 100 | - |

##### IPv4

| Interface | Description | Channel Group | IP Address | VRF | MTU | Shutdown | ACL In | ACL Out |
| --------- | ----------- | ------------- | ---------- | --- | --- | -------- | ------ | ------- |
| Ethernet3 | P2P_digital.twin.ethernet.ports.2_Ethernet3 | - | 192.168.3.114/31 | default | 9214 | False | - | - |
| Ethernet6 | P2P_digital-twin-ethernet-ports-3_Ethernet6 | - | 192.168.3.112/31 | default | 9214 | False | - | - |
| Ethernet10 | - | - | 192.168.3.168/31 | TENANT_A_VRF_A | - | False | - | - |
| Ethernet10.100 | - | - | 192.168.3.160/31 | TENANT_A_VRF_A | - | False | - | - |
| Ethernet10.101 | - | - | 192.168.3.164/31 | TENANT_A_VRF_A | - | False | - | - |
| Ethernet11 | P2P_digital.twin.ethernet.ports.2_Ethernet11 | - | 192.168.3.184/31 | default | 9214 | False | - | - |
| Ethernet11.100 | P2P_digital.twin.ethernet.ports.2_Ethernet11.100 | - | 192.168.3.186/31 | default | 9214 | False | - | - |
| Ethernet11.101 | P2P_digital.twin.ethernet.ports.2_Ethernet11.101 | - | 192.168.3.188/31 | default | 9214 | False | - | - |
| Ethernet13 | P2P_external-device-1_Ethernet13 | - | 192.168.3.190/31 | default | 9214 | False | - | - |
| Ethernet13.100 | P2P_external-device-1_Ethernet13.100 | - | 192.168.3.192/31 | default | 9214 | False | - | - |
| Ethernet14 | P2P_digital.twin.ethernet.ports.2_Ethernet14 | 14 | *192.168.3.198/31 | *default | *9214 | *False | *- | *- |
| Ethernet15 | P2P_external-device-3_Ethernet15 | 15 | *192.168.3.200/31 | *default | *9214 | *False | *- | *- |
| Ethernet17 | - | 17 | *192.168.3.172/31 | *TENANT_A_VRF_A | *- | *False | *- | *- |
| Ethernet18 | - | 18 | *192.168.3.176/31 | *TENANT_A_VRF_A | *- | *False | *- | *- |
| Ethernet19 | - | - | 192.168.3.204/31 | default | - | False | - | - |
| Ethernet20.100 | - | - | 192.168.3.206/31 | default | - | False | - | - |
| Ethernet21 | - | - | 192.168.3.208/31 | default | - | False | - | - |
| Ethernet21.100 | - | - | 192.168.3.210/31 | default | - | False | - | - |
| Ethernet22 | - | 22 | *192.168.3.212/31 | *default | *- | *False | *- | *- |
| Ethernet23 | - | 23 | *192.168.3.214/31 | *default | *- | *False | *- | *- |

*Inherited from Port-Channel Interface

#### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet1
   description FIREWALL_firewall-1_Eth1
   no shutdown
   switchport
!
interface Ethernet2
   no shutdown
   switchport
!
interface Ethernet3
   description P2P_digital.twin.ethernet.ports.2_Ethernet3
   no shutdown
   mtu 9214
   no switchport
   ip address 192.168.3.114/31
!
interface Ethernet4
   description MLAG_digital.twin.ethernet.ports.2_Ethernet4
   no shutdown
   channel-group 4 mode active
!
interface Ethernet5
   description MLAG_digital.twin.ethernet.ports.2_Ethernet5
   no shutdown
   channel-group 4 mode active
!
interface Ethernet6
   description P2P_digital-twin-ethernet-ports-3_Ethernet6
   no shutdown
   mtu 9214
   no switchport
   ip address 192.168.3.112/31
!
interface Ethernet9
   description FIREWALL_firewall-1_Eth3
   no shutdown
   channel-group 9 mode active
!
interface Ethernet10
   no shutdown
   no switchport
   vrf TENANT_A_VRF_A
   ip address 192.168.3.168/31
!
interface Ethernet10.100
   no shutdown
   encapsulation dot1q vlan 100
   vrf TENANT_A_VRF_A
   ip address 192.168.3.160/31
!
interface Ethernet10.101
   no shutdown
   encapsulation dot1q vlan 101
   vrf TENANT_A_VRF_A
   ip address 192.168.3.164/31
!
interface Ethernet11
   description P2P_digital.twin.ethernet.ports.2_Ethernet11
   no shutdown
   mtu 9214
   no switchport
   ip address 192.168.3.184/31
!
interface Ethernet11.100
   description P2P_digital.twin.ethernet.ports.2_Ethernet11.100
   no shutdown
   mtu 9214
   no switchport
   ip address 192.168.3.186/31
!
interface Ethernet11.101
   description P2P_digital.twin.ethernet.ports.2_Ethernet11.101
   no shutdown
   mtu 9214
   no switchport
   ip address 192.168.3.188/31
!
interface Ethernet13
   description P2P_external-device-1_Ethernet13
   no shutdown
   mtu 9214
   no switchport
   ip address 192.168.3.190/31
!
interface Ethernet13.100
   description P2P_external-device-1_Ethernet13.100
   no shutdown
   mtu 9214
   no switchport
   ip address 192.168.3.192/31
!
interface Ethernet14
   description P2P_digital.twin.ethernet.ports.2_Ethernet14
   no shutdown
   channel-group 14 mode active
!
interface Ethernet15
   description P2P_external-device-3_Ethernet15
   no shutdown
   channel-group 15 mode active
!
interface Ethernet16
   no shutdown
   channel-group 16 mode active
!
interface Ethernet17
   no shutdown
   channel-group 17 mode active
!
interface Ethernet18
   no shutdown
   channel-group 18 mode active
!
interface Ethernet19
   no shutdown
   no switchport
   ip address 192.168.3.204/31
!
interface Ethernet20
   no shutdown
   no switchport
!
interface Ethernet20.100
   no shutdown
   encapsulation dot1q vlan 100
   ip address 192.168.3.206/31
!
interface Ethernet21
   no shutdown
   no switchport
   ip address 192.168.3.208/31
!
interface Ethernet21.100
   no shutdown
   encapsulation dot1q vlan 100
   ip address 192.168.3.210/31
!
interface Ethernet22
   no shutdown
   channel-group 22 mode active
!
interface Ethernet23
   no shutdown
   channel-group 23 mode active
```

### Port-Channel Interfaces

#### Port-Channel Interfaces Summary

##### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | LACP Fallback Timeout | LACP Fallback Mode | MLAG ID | EVPN ESI |
| --------- | ----------- | ---- | ----- | ----------- | ----------- | --------------------- | ------------------ | ------- | -------- |
| Port-Channel4 | MLAG_digital.twin.ethernet.ports.2_Port-Channel4 | trunk | - | - | MLAG | - | - | - | - |
| Port-Channel9 | FIREWALL_firewall-1 | - | - | - | - | - | - | 9 | - |
| Port-Channel16 | - | - | - | - | - | - | - | 16 | - |

##### Encapsulation Dot1q

| Interface | Description | Vlan ID | Dot1q VLAN Tag | Dot1q Inner VLAN Tag |
| --------- | ----------- | ------- | -------------- | -------------------- |
| Port-Channel17.100 | - | - | 100 | - |
| Port-Channel23.100 | - | - | 100 | - |

##### IPv4

| Interface | Description | MLAG ID | IP Address | VRF | MTU | Shutdown | ACL In | ACL Out |
| --------- | ----------- | ------- | ---------- | --- | --- | -------- | ------ | ------- |
| Port-Channel14 | P2P_digital.twin.ethernet.ports.2_Port-Channel14 | - | 192.168.3.198/31 | default | 9214 | False | - | - |
| Port-Channel15 | P2P_external-device-3_Port-Channel15 | - | 192.168.3.200/31 | default | 9214 | False | - | - |
| Port-Channel17 | - | - | 192.168.3.172/31 | TENANT_A_VRF_A | - | False | - | - |
| Port-Channel17.100 | - | - | 192.168.3.174/31 | TENANT_A_VRF_A | - | False | - | - |
| Port-Channel18 | - | - | 192.168.3.176/31 | TENANT_A_VRF_A | - | False | - | - |
| Port-Channel22 | - | - | 192.168.3.212/31 | default | - | False | - | - |
| Port-Channel23 | - | - | 192.168.3.214/31 | default | - | False | - | - |
| Port-Channel23.100 | - | - | 192.168.3.216/31 | default | - | False | - | - |

#### Port-Channel Interfaces Device Configuration

```eos
!
interface Port-Channel4
   description MLAG_digital.twin.ethernet.ports.2_Port-Channel4
   no shutdown
   switchport mode trunk
   switchport trunk group MLAG
   switchport
!
interface Port-Channel9
   description FIREWALL_firewall-1
   no shutdown
   switchport
   mlag 9
!
interface Port-Channel14
   description P2P_digital.twin.ethernet.ports.2_Port-Channel14
   no shutdown
   mtu 9214
   no switchport
   ip address 192.168.3.198/31
!
interface Port-Channel15
   description P2P_external-device-3_Port-Channel15
   no shutdown
   mtu 9214
   no switchport
   ip address 192.168.3.200/31
!
interface Port-Channel16
   no shutdown
   switchport
   mlag 16
!
interface Port-Channel17
   no shutdown
   no switchport
   vrf TENANT_A_VRF_A
   ip address 192.168.3.172/31
!
interface Port-Channel17.100
   no shutdown
   encapsulation dot1q vlan 100
   vrf TENANT_A_VRF_A
   ip address 192.168.3.174/31
!
interface Port-Channel18
   no shutdown
   no switchport
   vrf TENANT_A_VRF_A
   ip address 192.168.3.176/31
!
interface Port-Channel22
   no shutdown
   no switchport
   ip address 192.168.3.212/31
!
interface Port-Channel23
   no shutdown
   no switchport
   ip address 192.168.3.214/31
!
interface Port-Channel23.100
   no shutdown
   encapsulation dot1q vlan 100
   ip address 192.168.3.216/31
```

### Loopback Interfaces

#### Loopback Interfaces Summary

##### IPv4

| Interface | Description | VRF | IP Address |
| --------- | ----------- | --- | ---------- |
| Loopback0 | ROUTER_ID | default | 192.168.3.129/32 |
| Loopback1 | VXLAN_TUNNEL_SOURCE | default | 192.168.3.145/32 |

##### IPv6

| Interface | Description | VRF | IPv6 Addresses |
| --------- | ----------- | --- | -------------- |
| Loopback0 | ROUTER_ID | default | - |
| Loopback1 | VXLAN_TUNNEL_SOURCE | default | - |

#### Loopback Interfaces Device Configuration

```eos
!
interface Loopback0
   description ROUTER_ID
   no shutdown
   ip address 192.168.3.129/32
!
interface Loopback1
   description VXLAN_TUNNEL_SOURCE
   no shutdown
   ip address 192.168.3.145/32
```

### VLAN Interfaces

#### VLAN Interfaces Summary

| Interface | Description | VRF | MTU | Shutdown |
| --------- | ----------- | --- | --- | -------- |
| Vlan1 | TENANT_A_VRF_A_SVI_A | TENANT_A_VRF_A | - | False |
| Vlan4093 | MLAG_L3 | default | 9214 | False |
| Vlan4094 | MLAG | default | 9214 | False |

##### IPv4

| Interface | VRF | IP Address | IP Address Virtual | IP Router Virtual Address | ACL In | ACL Out |
| --------- | --- | ---------- | ------------------ | ------------------------- | ------ | ------- |
| Vlan1 | TENANT_A_VRF_A | - | - | - | - | - |
| Vlan4093 | default | 192.168.3.80/31 | - | - | - | - |
| Vlan4094 | default | 192.168.3.96/31 | - | - | - | - |

#### VLAN Interfaces Device Configuration

```eos
!
interface Vlan1
   description TENANT_A_VRF_A_SVI_A
   no shutdown
   vrf TENANT_A_VRF_A
!
interface Vlan4093
   description MLAG_L3
   no shutdown
   mtu 9214
   ip address 192.168.3.80/31
!
interface Vlan4094
   description MLAG
   no shutdown
   mtu 9214
   no autostate
   ip address 192.168.3.96/31
```

### VXLAN Interface

#### VXLAN Interface Summary

| Setting | Value |
| ------- | ----- |
| Source Interface | Loopback1 |
| UDP port | 4789 |
| EVPN MLAG Shared Router MAC | mlag-system-id |

##### VRF to VNI and Multicast Group Mappings

| VRF | VNI | Overlay Multicast Group to Encap Mappings |
| --- | --- | ----------------------------------------- |
| TENANT_A_VRF_A | 1025 | - |

#### VXLAN Interface Device Configuration

```eos
!
interface Vxlan1
   description digital-twin-ethernet-ports-1_VTEP
   vxlan source-interface Loopback1
   vxlan virtual-router encapsulation mac-address mlag-system-id
   vxlan udp-port 4789
   vxlan vrf TENANT_A_VRF_A vni 1025
```

## Routing

### Service Routing Protocols Model

Multi agent routing protocol model enabled

```eos
!
service routing protocols model multi-agent
```

### IP Routing

#### IP Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | True |
| MGMT | False |
| TENANT_A_VRF_A | True |

#### IP Routing Device Configuration

```eos
!
ip routing
no ip routing vrf MGMT
ip routing vrf TENANT_A_VRF_A
```

### IPv6 Routing

#### IPv6 Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | False |
| MGMT | false |
| TENANT_A_VRF_A | false |

### Router BGP

ASN Notation: asplain

#### Router BGP Summary

| BGP AS | Router ID |
| ------ | --------- |
| 65001 | 192.168.3.129 |

| BGP Tuning |
| ---------- |
| update wait-install |
| no bgp default ipv4-unicast |
| maximum-paths 4 |

#### Router BGP Peer Groups

##### IPv4-UNDERLAY-PEERS

| Settings | Value |
| -------- | ----- |
| Address Family | ipv4 |
| Send community | all |
| Maximum routes | 256000 |

##### MLAG-IPv4-UNDERLAY-PEER

| Settings | Value |
| -------- | ----- |
| Address Family | ipv4 |
| Remote AS | 65001 |
| Next-hop self | True |
| Send community | all |
| Maximum routes | 256000 |

#### BGP Neighbors

| Neighbor | Remote AS | VRF | Shutdown | Send-community | Maximum-routes | Allowas-in | BFD | RIB Pre-Policy Retain | Route-Reflector Client | Passive | TTL Max Hops | Maximum Advertise Routes |
| -------- | --------- | --- | -------- | -------------- | -------------- | ---------- | --- | --------------------- | ---------------------- | ------- | ------------ | ------------------------ |
| 192.168.3.81 | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | default | - | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | - | - | - | - | - | - | - |
| 192.168.3.113 | 65001 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - | - | - |
| 192.168.3.115 | 65001 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - | - | - |
| 192.168.3.185 | 65001 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - | - | - |
| 192.168.3.187 | 65001 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - | - | - |
| 192.168.3.189 | 65001 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - | - | - |
| 192.168.3.191 | 65001 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - | - | - |
| 192.168.3.193 | 65001 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - | - | - |
| 192.168.3.199 | 65001 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - | - | - |
| 192.168.3.201 | 65001 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - | - | - |

#### Router BGP VRFs

| VRF | Route-Distinguisher | Redistribute | Graceful Restart |
| --- | ------------------- | ------------ | ---------------- |
| TENANT_A_VRF_A | 192.168.3.129:1025 | connected | - |

#### Router BGP Device Configuration

```eos
!
router bgp 65001
   router-id 192.168.3.129
   update wait-install
   no bgp default ipv4-unicast
   maximum-paths 4
   neighbor IPv4-UNDERLAY-PEERS peer group
   neighbor IPv4-UNDERLAY-PEERS send-community
   neighbor IPv4-UNDERLAY-PEERS maximum-routes 256000
   neighbor MLAG-IPv4-UNDERLAY-PEER peer group
   neighbor MLAG-IPv4-UNDERLAY-PEER remote-as 65001
   neighbor MLAG-IPv4-UNDERLAY-PEER next-hop-self
   neighbor MLAG-IPv4-UNDERLAY-PEER description digital.twin.ethernet.ports.2
   neighbor MLAG-IPv4-UNDERLAY-PEER route-map RM-MLAG-PEER-IN in
   neighbor MLAG-IPv4-UNDERLAY-PEER send-community
   neighbor MLAG-IPv4-UNDERLAY-PEER maximum-routes 256000
   neighbor 192.168.3.81 peer group MLAG-IPv4-UNDERLAY-PEER
   neighbor 192.168.3.81 description digital.twin.ethernet.ports.2_Vlan4093
   neighbor 192.168.3.113 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.3.113 remote-as 65001
   neighbor 192.168.3.113 description digital-twin-ethernet-ports-3_Ethernet6
   neighbor 192.168.3.115 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.3.115 remote-as 65001
   neighbor 192.168.3.115 description digital.twin.ethernet.ports.2_Ethernet3
   neighbor 192.168.3.185 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.3.185 remote-as 65001
   neighbor 192.168.3.185 description digital.twin.ethernet.ports.2
   neighbor 192.168.3.187 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.3.187 remote-as 65001
   neighbor 192.168.3.187 description digital.twin.ethernet.ports.2
   neighbor 192.168.3.189 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.3.189 remote-as 65001
   neighbor 192.168.3.189 description digital.twin.ethernet.ports.2
   neighbor 192.168.3.191 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.3.191 remote-as 65001
   neighbor 192.168.3.191 description external-device-1
   neighbor 192.168.3.193 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.3.193 remote-as 65001
   neighbor 192.168.3.193 description external-device-1
   neighbor 192.168.3.199 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.3.199 remote-as 65001
   neighbor 192.168.3.199 description digital.twin.ethernet.ports.2
   neighbor 192.168.3.201 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.3.201 remote-as 65001
   neighbor 192.168.3.201 description external-device-3
   redistribute connected route-map RM-CONN-2-BGP
   !
   address-family ipv4
      neighbor IPv4-UNDERLAY-PEERS activate
      neighbor MLAG-IPv4-UNDERLAY-PEER activate
   !
   vrf TENANT_A_VRF_A
      rd 192.168.3.129:1025
      route-target import evpn 1025:1025
      route-target export evpn 1025:1025
      router-id 192.168.3.129
      redistribute connected
```

## BFD

### Router BFD

#### Router BFD Multihop Summary

| Interval | Minimum RX | Multiplier |
| -------- | ---------- | ---------- |
| 300 | 300 | 3 |

#### Router BFD Device Configuration

```eos
!
router bfd
   multihop interval 300 min-rx 300 multiplier 3
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

## Filters

### Prefix-lists

#### Prefix-lists Summary

##### PL-LOOPBACKS-EVPN-OVERLAY

| Sequence | Action |
| -------- | ------ |
| 10 | permit 192.168.3.128/28 eq 32 |
| 20 | permit 192.168.3.144/28 eq 32 |

#### Prefix-lists Device Configuration

```eos
!
ip prefix-list PL-LOOPBACKS-EVPN-OVERLAY
   seq 10 permit 192.168.3.128/28 eq 32
   seq 20 permit 192.168.3.144/28 eq 32
```

### Route-maps

#### Route-maps Summary

##### RM-CONN-2-BGP

| Sequence | Type | Match | Set | Sub-Route-Map | Continue |
| -------- | ---- | ----- | --- | ------------- | -------- |
| 10 | permit | ip address prefix-list PL-LOOPBACKS-EVPN-OVERLAY | - | - | - |

##### RM-MLAG-PEER-IN

| Sequence | Type | Match | Set | Sub-Route-Map | Continue |
| -------- | ---- | ----- | --- | ------------- | -------- |
| 10 | permit | - | origin incomplete | - | - |

#### Route-maps Device Configuration

```eos
!
route-map RM-CONN-2-BGP permit 10
   match ip address prefix-list PL-LOOPBACKS-EVPN-OVERLAY
!
route-map RM-MLAG-PEER-IN permit 10
   description Make routes learned over MLAG Peer-link less preferred on spines to ensure optimal routing
   set origin incomplete
```

## VRF Instances

### VRF Instances Summary

| VRF Name | IP Routing |
| -------- | ---------- |
| MGMT | disabled |
| TENANT_A_VRF_A | enabled |

### VRF Instances Device Configuration

```eos
!
vrf instance MGMT
!
vrf instance TENANT_A_VRF_A
```
