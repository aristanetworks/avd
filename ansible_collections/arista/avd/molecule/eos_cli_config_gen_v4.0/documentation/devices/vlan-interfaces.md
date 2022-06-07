# vlan-interfaces
# Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [Authentication](#authentication)
- [Monitoring](#monitoring)
- [Internal VLAN Allocation Policy](#internal-vlan-allocation-policy)
  - [Internal VLAN Allocation Policy Summary](#internal-vlan-allocation-policy-summary)
- [Interfaces](#interfaces)
  - [VLAN Interfaces](#vlan-interfaces)
- [Routing](#routing)
  - [IP Routing](#ip-routing)
  - [IPv6 Routing](#ipv6-routing)
- [BFD](#bfd)
  - [BFD Interfaces](#bfd-interfaces)
- [Multicast](#multicast)
  - [PIM Sparse Mode](#pim-sparse-mode)
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

## VLAN Interfaces

### VLAN Interfaces Summary

| Interface | Description | VRF |  MTU | Shutdown |
| --------- | ----------- | --- | ---- | -------- |
| Vlan24 | SVI Description | default | - | false |
| Vlan41 | SVI Description | default | - | false |
| Vlan42 | SVI Description | default | - | false |
| Vlan75 | SVI Description | default | - | false |
| Vlan81 | IPv6 Virtual Address | Tenant_C | - | - |
| Vlan83 | SVI Description | default | - | false |
| Vlan84 | SVI Description | default | - | - |
| Vlan85 | SVI Description | default | - | - |
| Vlan86 | SVI Description | default | - | - |
| Vlan87 | SVI Description | default | - | true |
| Vlan88 | SVI Description | default | - | true |
| Vlan89 | SVI Description | default | - | false |
| Vlan90 | SVI Description | default | - | - |
| Vlan91 | PBR Description | default | - | true |
| Vlan110 | PVLAN Primary with vlan mapping | Tenant_A | - | false |
| Vlan501 | SVI Description | default | - | false |
| Vlan1001 | SVI Description | Tenant_A | - | false |
| Vlan1002 | SVI Description | Tenant_A | - | false |
| Vlan2001 | SVI Description | Tenant_B | - | - |
| Vlan2002 | SVI Description | Tenant_B | - | - |
| Vlan4094 | SVI Description | default | 9214 | - |

#### Private VLAN

| Interface | PVLAN Mapping |
| --------- | ------------- |
| Vlan110 | 111-112 |

#### IPv4

| Interface | VRF | IP Address | IP Address Virtual | IP Router Virtual Address | VRRP | ACL In | ACL Out |
| --------- | --- | ---------- | ------------------ | ------------------------- | ---- | ------ | ------- |
| Vlan24 |  default  |  -  |  10.10.24.1/24  |  -  |  -  |  -  |  -  |
| Vlan41 |  default  |  -  |  10.10.41.1/24  |  -  |  -  |  -  |  -  |
| Vlan42 |  default  |  -  |  10.10.42.1/24  |  -  |  -  |  -  |  -  |
| Vlan75 |  default  |  -  |  10.10.75.1/24  |  -  |  -  |  -  |  -  |
| Vlan81 |  Tenant_C  |  -  |  10.10.81.1/24  |  -  |  -  |  -  |  -  |
| Vlan83 |  default  |  -  |  10.10.83.1/24  |  -  |  -  |  -  |  -  |
| Vlan84 |  default  |  10.10.84.1/24  |  -  |  10.10.84.254, 10.11.84.254/24  |  -  |  -  |  -  |
| Vlan85 |  default  |  10.10.84.1/24  |  -  |  -  |  -  |  -  |  -  |
| Vlan86 |  default  |  10.10.83.1/24  |  -  |  -  |  -  |  -  |  -  |
| Vlan87 |  default  |  10.10.87.1/24  |  -  |  -  |  -  |  ACL_IN  |  ACL_OUT  |
| Vlan88 |  default  |  -  |  10.10.87.1/23  |  -  |  -  |  -  |  -  |
| Vlan89 |  default  |  -  |  10.10.144.3/20  |  -  |  -  |  -  |  -  |
| Vlan90 |  default  |  10.10.83.1/24  |  -  |  -  |  -  |  -  |  -  |
| Vlan91 |  default  |  -  |  -  |  -  |  -  |  -  |  -  |
| Vlan110 |  Tenant_A  |  -  |  -  |  -  |  -  |  -  |  -  |
| Vlan501 |  default  |  10.50.26.29/27  |  -  |  -  |  -  |  -  |  -  |
| Vlan1001 |  Tenant_A  |  -  |  10.1.1.1/24  |  -  |  -  |  -  |  -  |
| Vlan1002 |  Tenant_A  |  -  |  10.1.2.1/24  |  -  |  -  |  -  |  -  |
| Vlan2001 |  Tenant_B  |  -  |  10.2.1.1/24  |  -  |  -  |  -  |  -  |
| Vlan2002 |  Tenant_B  |  -  |  10.2.2.1/24  |  -  |  -  |  -  |  -  |
| Vlan4094 |  default  |  169.254.252.0/31  |  -  |  -  |  -  |  -  |  -  |

#### IPv6

| Interface | VRF | IPv6 Address | IPv6 Virtual Address | Virtual Router Address | VRRP | ND RA Disabled | Managed Config Flag | IPv6 ACL In | IPv6 ACL Out |
| --------- | --- | ------------ | -------------------- | ---------------------- | ---- | -------------- | ------------------- | ----------- | ------------ |
| Vlan24 | default | 1b11:3a00:22b0:6::15/64 | - | 1b11:3a00:22b0:6::1 | - | - | true | - | - |
| Vlan75 | default | 1b11:3a00:22b0:1000::15/64 | - | 1b11:3a00:22b0:1000::1 | - | - | true | - | - |
| Vlan81 | Tenant_C | - | fc00:10:10:81::1/64 | - | - | - | - | - | - |
| Vlan89 | default | 1b11:3a00:22b0:5200::15/64 | - | 1b11:3a00:22b0:5200::3 | - | - | true | - | - |
| Vlan501 | default | 1b11:3a00:22b0:0088::207/127 | - | - | - | true | - | - | - |
| Vlan1001 | Tenant_A | a1::1/64 | - | - | - | - | true | - | - |
| Vlan1002 | Tenant_A | a2::1/64 | - | - | - | true | true | - | - |

### VLAN Interfaces Device Configuration

```eos
!
interface Vlan24
   description SVI Description
   no shutdown
   ipv6 address 1b11:3a00:22b0:6::15/64
   ipv6 nd managed-config-flag
   ipv6 nd prefix 1b11:3a00:22b0:6::/64 infinite infinite no-autoconfig
   ipv6 virtual-router address 1b11:3a00:22b0:6::1
   ip address virtual 10.10.24.1/24
!
interface Vlan41
   description SVI Description
   no shutdown
   ip helper-address 10.10.64.150 source-interface Loopback0
   ip helper-address 10.10.96.150 source-interface Loopback0
   ip helper-address 10.10.96.151 source-interface Loopback0
   ip address virtual 10.10.41.1/24
!
interface Vlan42
   description SVI Description
   no shutdown
   ip helper-address 10.10.64.150 source-interface Loopback0
   ip helper-address 10.10.96.150 source-interface Loopback0
   ip helper-address 10.10.96.151 source-interface Loopback0
   ip address virtual 10.10.42.1/24
!
interface Vlan75
   description SVI Description
   no shutdown
   ipv6 address 1b11:3a00:22b0:1000::15/64
   ipv6 nd managed-config-flag
   ipv6 nd prefix 1b11:3a00:22b0:1000::/64 infinite infinite no-autoconfig
   ipv6 virtual-router address 1b11:3a00:22b0:1000::1
   ip address virtual 10.10.75.1/24
!
interface Vlan81
   description IPv6 Virtual Address
   vrf Tenant_C
   ipv6 enable
   ipv6 address virtual fc00:10:10:81::1/64
   ip address virtual 10.10.81.1/24
!
interface Vlan83
   description SVI Description
   no shutdown
   ip address virtual 10.10.83.1/24
   ip address virtual 10.11.83.1/24 secondary
   ip address virtual 10.11.84.1/24 secondary
!
interface Vlan84
   description SVI Description
   arp gratuitous accept
   arp monitor mac-address
   ip address 10.10.84.1/24
   ip virtual-router address 10.10.84.254
   ip virtual-router address 10.11.84.254/24
!
interface Vlan85
   description SVI Description
   arp cache dynamic capacity 50000
   ip address 10.10.84.1/24
   bfd interval 500 min-rx 500 multiplier 5
!
interface Vlan86
   description SVI Description
   ip address 10.10.83.1/24
   ip attached-host route export 10
!
interface Vlan87
   description SVI Description
   shutdown
   ip address 10.10.87.1/24
   ip access-group ACL_IN in
   ip access-group ACL_OUT out
!
interface Vlan88
   description SVI Description
   shutdown
   ip address virtual 10.10.87.1/23
!
interface Vlan89
   description SVI Description
   no shutdown
   ip helper-address 10.10.64.150 source-interface Loopback0
   ip helper-address 10.10.96.101 source-interface Loopback0
   ip helper-address 10.10.96.150 source-interface Loopback0
   ip helper-address 10.10.96.151 source-interface Loopback0
   ip igmp
   ipv6 address 1b11:3a00:22b0:5200::15/64
   ipv6 nd managed-config-flag
   ipv6 nd prefix 1b11:3a00:22b0:5200::/64 infinite infinite no-autoconfig
   multicast ipv4 source route export
   pim ipv4 sparse-mode
   pim ipv4 local-interface Loopback0
   ipv6 virtual-router address 1b11:3a00:22b0:5200::3
   ip address virtual 10.10.144.3/20
!
interface Vlan90
   description SVI Description
   ip address 10.10.83.1/24
   ip attached-host route export
!
interface Vlan91
   description PBR Description
   shutdown
   service-policy type pbr input MyServicePolicy
!
interface Vlan110
   description PVLAN Primary with vlan mapping
   no shutdown
   vrf Tenant_A
   pvlan mapping 111-112
!
interface Vlan501
   description SVI Description
   no shutdown
   ip address 10.50.26.29/27
   ipv6 address 1b11:3a00:22b0:0088::207/127
   ipv6 nd ra disabled
!
interface Vlan1001
   description SVI Description
   no shutdown
   vrf Tenant_A
   ipv6 address a1::1/64
   ipv6 nd managed-config-flag
   ipv6 nd prefix a1::/64 infinite infinite no-autoconfig
   ip address virtual 10.1.1.1/24
!
interface Vlan1002
   description SVI Description
   no shutdown
   vrf Tenant_A
   ipv6 address a2::1/64
   ipv6 nd ra disabled
   ipv6 nd managed-config-flag
   ipv6 nd prefix a2::/64 infinite infinite no-autoconfig
   ip address virtual 10.1.2.1/24
!
interface Vlan2001
   description SVI Description
   vrf Tenant_B
   ip address virtual 10.2.1.1/24
   comment
   Comment created from eos_cli under vlan_interfaces.Vlan2001
   EOF

!
interface Vlan2002
   description SVI Description
   no autostate
   vrf Tenant_B
   ip address virtual 10.2.2.1/24
!
interface Vlan4094
   description SVI Description
   mtu 9214
   ip address 169.254.252.0/31
   ipv6 address fe80::a/64 link-local
   pim ipv4 sparse-mode
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

# BFD

## BFD Interfaces

| Interface | Interval | Minimum RX | Multiplier | Echo |
| --------- | -------- | ---------- | ---------- | ---- |
| Vlan85 | 500 | 500 | 5 | - |

# Multicast

## PIM Sparse Mode

### PIM Sparse Mode enabled interfaces

| Interface Name | VRF Name | IP Version | DR Priority | Local Interface |
| -------------- | -------- | ---------- | ----------- | --------------- |
| Vlan89 | - | IPv4 | - | Loopback0 |
| Vlan4094 | - | IPv4 | - | - |

# Filters

# ACL

# Quality Of Service
