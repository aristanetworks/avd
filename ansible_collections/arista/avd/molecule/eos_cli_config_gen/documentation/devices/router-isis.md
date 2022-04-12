# router-isis
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
  - [Router ISIS](#router-isis)
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
| Management1 | oob_management | oob | MGMT | 10.73.254.11/24 | 10.73.254.253 |

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
   ip address 10.73.254.11/24
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
| Ethernet3 | MLAG_PEER_EAPI-LEAF1B_Ethernet3 | *access | *- | *- | *- | 3 |

*Inherited from Port-Channel Interface

#### IPv4

| Interface | Description | Type | Channel Group | IP Address | VRF |  MTU | Shutdown | ACL In | ACL Out |
| --------- | ----------- | -----| ------------- | ---------- | ----| ---- | -------- | ------ | ------- |
| Ethernet1 | P2P_LINK_TO_EAPI-SPINE1_Ethernet1 | routed | - | 172.31.255.1/31 | default | 1500 | - | - | - |
| Ethernet2 | P2P_LINK_TO_EAPI-SPINE2_Ethernet1 | routed | - | 172.31.255.3/31 | default | 1500 | - | - | - |
| Ethernet4 | - | *routed | 4 | *10.9.2.3/31 | **default | **- | **- | **- | **- |
| Ethernet5 | - | *routed | 5 | *10.9.2.5/31 | **default | **- | **- | **- | **- |
| Ethernet6 | - | *routed | 6 | *10.9.2.7/31 | **default | **- | **- | **- | **- |
*Inherited from Port-Channel Interface

#### ISIS

| Interface | Channel Group | ISIS Instance | ISIS Metric | Mode | ISIS Circuit Type | Hello Padding | Authentication Mode |
| --------- | ------------- | ------------- | ----------- | ---- | ----------------- | ------------- | ------------------- |
| Ethernet1 | - | EVPN_UNDERLAY | 50 | point-to-point | - | - | - |
| Ethernet2 | - | EVPN_UNDERLAY | 50 | point-to-point | level-1-2 | - | - |
| Ethernet4 | 4 | *EVPN_UNDERLAY | *50 | *point-to-point | *level-2 | *- | *- |
| Ethernet5 | 5 | *EVPN_UNDERLAY | *50 | *passive | *- | *- | *- |
| Ethernet6 | 6 | *EVPN_UNDERLAY | *100 | *- | *level-1-2 | *- | *- |
 *Inherited from Port-Channel Interface

### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet1
   description P2P_LINK_TO_EAPI-SPINE1_Ethernet1
   mtu 1500
   no switchport
   ip address 172.31.255.1/31
   isis enable EVPN_UNDERLAY
   isis metric 50
   isis network point-to-point
!
interface Ethernet2
   description P2P_LINK_TO_EAPI-SPINE2_Ethernet1
   mtu 1500
   no switchport
   ip address 172.31.255.3/31
   isis enable EVPN_UNDERLAY
   isis circuit-type level-1-2
   isis metric 50
   isis network point-to-point
!
interface Ethernet3
   description MLAG_PEER_EAPI-LEAF1B_Ethernet3
   channel-group 3 mode active
!
interface Ethernet4
   channel-group 4 mode active
!
interface Ethernet5
   channel-group 5 mode active
!
interface Ethernet6
   channel-group 6 mode active
```

## Port-Channel Interfaces

### Port-Channel Interfaces Summary

#### L2

| Interface | Description | Type | Mode | VLANs | Native VLAN | Trunk Group | LACP Fallback Timeout | LACP Fallback Mode | MLAG ID | EVPN ESI |
| --------- | ----------- | ---- | ---- | ----- | ----------- | ------------| --------------------- | ------------------ | ------- | -------- |

#### IPv4

| Interface | Description | Type | MLAG ID | IP Address | VRF | MTU | Shutdown | ACL In | ACL Out |
| --------- | ----------- | ---- | ------- | ---------- | --- | --- | -------- | ------ | ------- |
| Port-Channel4 | - | routed | - | 10.9.2.3/31 | default | - | - | - | - |
| Port-Channel5 | - | routed | - | 10.9.2.5/31 | default | - | - | - | - |
| Port-Channel6 | - | routed | - | 10.9.2.7/31 | default | - | - | - | - |

#### ISIS

| Interface | ISIS Instance | ISIS Metric | Mode | ISIS Circuit Type | Hello Padding | Authentication Mode |
| --------- | ------------- | ----------- | ---- | ----------------- | ------------- | ------------------- |
| Port-Channel4 | EVPN_UNDERLAY | 50 | point-to-point | level-2 | - | - |
| Port-Channel5 | EVPN_UNDERLAY | 50 | passive | - | - | - |
| Port-Channel6 | EVPN_UNDERLAY | 100 | - | level-1-2 | - | - |

### Port-Channel Interfaces Device Configuration

```eos
!
interface Port-Channel4
   no switchport
   ip address 10.9.2.3/31
   isis enable EVPN_UNDERLAY
   isis circuit-type level-2
   isis metric 50
   isis network point-to-point
!
interface Port-Channel5
   no switchport
   ip address 10.9.2.5/31
   isis enable EVPN_UNDERLAY
   isis metric 50
   isis passive
!
interface Port-Channel6
   no switchport
   ip address 10.9.2.7/31
   isis enable EVPN_UNDERLAY
   isis circuit-type level-1-2
   isis metric 100
```

## Loopback Interfaces

### Loopback Interfaces Summary

#### IPv4

| Interface | Description | VRF | IP Address |
| --------- | ----------- | --- | ---------- |
| Loopback0 | EVPN_Overlay_Peering | default | 192.168.255.3/32 |
| Loopback1 | VTEP_VXLAN_Tunnel_Source | default | 192.168.254.3/32 |
| Loopback2 | ISIS-SR Node-SID | default | 10.1.255.3/32 |

#### IPv6

| Interface | Description | VRF | IPv6 Address |
| --------- | ----------- | --- | ------------ |
| Loopback0 | EVPN_Overlay_Peering | default | - |
| Loopback1 | VTEP_VXLAN_Tunnel_Source | default | - |
| Loopback2 | ISIS-SR Node-SID | default | - |

#### ISIS

| Interface | ISIS instance | ISIS metric | Interface mode |
| --------- | ------------- | ----------- | -------------- |
| Loopback0 | EVPN_UNDERLAY | - | passive |
| Loopback1 | EVPN_UNDERLAY | - | passive |
| Loopback2 | EVPN_UNDERLAY | 50 | passive |

### Loopback Interfaces Device Configuration

```eos
!
interface Loopback0
   description EVPN_Overlay_Peering
   ip address 192.168.255.3/32
   isis enable EVPN_UNDERLAY
   isis passive
!
interface Loopback1
   description VTEP_VXLAN_Tunnel_Source
   ip address 192.168.254.3/32
   isis enable EVPN_UNDERLAY
   isis passive
!
interface Loopback2
   description ISIS-SR Node-SID
   ip address 10.1.255.3/32
   isis enable EVPN_UNDERLAY
   isis passive
   isis metric 50
   node-segment ipv4 index 10
   node-segment ipv6 index 1000
```

## VLAN Interfaces

### VLAN Interfaces Summary

| Interface | Description | VRF |  MTU | Shutdown |
| --------- | ----------- | --- | ---- | -------- |
| Vlan110 | PR01-DEMO | TENANT_A_PROJECT01 | - | false |
| Vlan4093 | MLAG_PEER_L3_PEERING | default | - | - |
| Vlan4094 | MLAG_PEER | default | 1500 | - |

#### IPv4

| Interface | VRF | IP Address | IP Address Virtual | IP Router Virtual Address | VRRP | ACL In | ACL Out |
| --------- | --- | ---------- | ------------------ | ------------------------- | ---- | ------ | ------- |
| Vlan110 |  TENANT_A_PROJECT01  |  -  |  10.1.10.254/24  |  -  |  -  |  -  |  -  |
| Vlan4093 |  default  |  10.255.251.0/31  |  -  |  -  |  -  |  -  |  -  |
| Vlan4094 |  default  |  10.255.252.0/31  |  -  |  -  |  -  |  -  |  -  |

#### ISIS

| Interface | ISIS Instance | ISIS Metric | Mode |
| --------- | ------------- | ----------- | ---- |
| Vlan4093 | EVPN_UNDERLAY | 50 | point-to-point |

### VLAN Interfaces Device Configuration

```eos
!
interface Vlan110
   description PR01-DEMO
   no shutdown
   vrf TENANT_A_PROJECT01
   ip address virtual 10.1.10.254/24
!
interface Vlan4093
   description MLAG_PEER_L3_PEERING
   ip address 10.255.251.0/31
   isis enable EVPN_UNDERLAY
   isis metric 50
   isis network point-to-point
!
interface Vlan4094
   description MLAG_PEER
   mtu 1500
   no autostate
   ip address 10.255.252.0/31
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

## Router ISIS

### Router ISIS Summary

| Settings | Value |
| -------- | ----- |
| Instance | EVPN_UNDERLAY |
| Net-ID | 49.0001.0001.0001.0001.00 |
| Type | level-2 |
| Address Family | ipv4 unicast |
| Router-ID | 192.168.255.3 |
| Log Adjacency Changes | True |
| MPLS LDP Sync Default | True |
| Local Convergence Delay (ms) | 15000 |
| Advertise Passive-only | True |
| SR MPLS Enabled | True |

### ISIS Interfaces Summary

| Interface | ISIS Instance | ISIS Metric | Interface Mode |
| --------- | ------------- | ----------- | -------------- |
| Ethernet1 | EVPN_UNDERLAY | 50 | point-to-point |
| Ethernet2 | EVPN_UNDERLAY | 50 | point-to-point |
| Vlan4093 | EVPN_UNDERLAY | 50 | point-to-point |
| Loopback0 | EVPN_UNDERLAY | - | passive |
| Loopback1 | EVPN_UNDERLAY | - | passive |
| Loopback2 | EVPN_UNDERLAY | 50 | passive |

### ISIS Segment-routing Node-SID

| Loopback | IPv4 Index | IPv6 Index |
| -------- | ---------- | ---------- |
| Loopback2 | 10 | 1000 |

### Router ISIS Device Configuration

```eos
!
router isis EVPN_UNDERLAY
   net 49.0001.0001.0001.0001.00
   is-type level-2
   router-id ipv4 192.168.255.3
   log-adjacency-changes
   mpls ldp sync default
   timers local-convergence-delay 15000 protected-prefixes
   advertise passive-only
   !
   address-family ipv4 unicast
      maximum-paths 2
   !
   segment-routing mpls
      no shutdown
```

# Multicast

# Filters

# ACL

# Quality Of Service
