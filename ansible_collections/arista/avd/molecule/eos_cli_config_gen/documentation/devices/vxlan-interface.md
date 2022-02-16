# vxlan-interface
# Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [Authentication](#authentication)
- [Monitoring](#monitoring)
- [Internal VLAN Allocation Policy](#internal-vlan-allocation-policy)
  - [Internal VLAN Allocation Policy Summary](#internal-vlan-allocation-policy-summary)
- [Interfaces](#interfaces)
  - [VXLAN Interface](#vxlan-interface)
- [Routing](#routing)
  - [IP Routing](#ip-routing)
  - [IPv6 Routing](#ipv6-routing)
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

## VXLAN Interface

### VXLAN Interface Summary

| Setting | Value |
| ------- | ----- |
| Source Interface | Loopback0 |
| MLAG Source Interface | Loopback1 |
| UDP port | 4789 |
| EVPN MLAG Shared Router MAC | mlag-system-id |
| VXLAN flood-lists learning from data-plane | Enabled |
| Qos dscp propagation encapsulation | Enabled |
| Qos map dscp to traffic-class decapsulation | Enabled |

#### VLAN to VNI, Flood List and Multicast Group Mappings

| VLAN | VNI | Flood List | Multicast Group |
| ---- | --- | ---------- | --------------- |
| 110 | 10110 | - | 239.9.1.4 |
| 111 | 10111 | 10.1.1.10<br/>10.1.1.11 | - |

#### VRF to VNI and Multicast Group Mappings

| VRF | VNI | Multicast Group |
| ---- | --- | --------------- |
| Tenant_A_OP_Zone | 10 | 232.0.0.10 |
| Tenant_A_WEB_Zone | 11 | - |

#### Default Flood List

| Default Flood List |
| ------------------ |
| 10.1.0.10<br/>10.1.0.11 |

### VXLAN Interface Device Configuration

```eos
!
interface Vxlan1
   description DC1-LEAF2A_VTEP
   vxlan source-interface Loopback0
   vxlan virtual-router encapsulation mac-address mlag-system-id
   vxlan udp-port 4789
   vxlan flood vtep learned data-plane
   vxlan vlan 110 vni 10110
   vxlan vlan 111 vni 10111
   vxlan vlan 111 flood vtep 10.1.1.10 10.1.1.11
   vxlan vrf Tenant_A_OP_Zone vni 10
   vxlan vrf Tenant_A_WEB_Zone vni 11
   vxlan mlag source-interface Loopback1
   vxlan flood vtep 10.1.0.10 10.1.0.11
   vxlan qos dscp propagation encapsulation
   vxlan qos map dscp to traffic-class decapsulation
   vxlan vlan 110 multicast group 239.9.1.4
   vxlan vrf Tenant_A_OP_Zone multicast group 232.0.0.10
   vxlan encapsulation ipv4

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

# Quality Of Service
