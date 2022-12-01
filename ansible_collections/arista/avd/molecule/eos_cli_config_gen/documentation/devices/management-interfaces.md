# management-interfaces
# Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [Authentication](#authentication)
- [Monitoring](#monitoring)
- [Internal VLAN Allocation Policy](#internal-vlan-allocation-policy)
  - [Internal VLAN Allocation Policy Summary](#internal-vlan-allocation-policy-summary)
- [Interfaces](#interfaces)
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
| Management0 | - | oob | default | 10.0.0.0 | - |
| Management1 | oob_management | oob | MGMT | 10.73.255.122/24 | 10.73.255.2 |
| Management42 | - | oob | default | - | - |
| Vlan123 | inband_management | inband | default | 10.73.0.123/24 | 10.73.0.1 |

#### IPv6

| Management Interface | description | Type | VRF | IPv6 Address | IPv6 Gateway |
| -------------------- | ----------- | ---- | --- | ------------ | ------------ |
| Management0 | - | oob | default | - | - |
| Management1 | oob_management | oob | MGMT | - | - |
| Management42 | - | oob | default | - | - |
| Vlan123 | inband_management | inband | default | - | - |

### Management Interfaces Device Configuration

```eos
!
interface Management0
   mac-address 00:1c:73:00:00:aa
   ip address 10.0.0.0
!
interface Management1
   description oob_management
   vrf MGMT
   ip address 10.73.255.122/24
!
interface Management42
   shutdown
!
interface Vlan123
   description inband_management
   mtu 1500
   ip address 10.73.0.123/24
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

# Routing

## IP Routing

### IP Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | False |

### IP Routing Device Configuration

```eos
```
## IPv6 Routing

### IPv6 Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | False |

# Multicast

# Filters

# ACL

# Quality Of Service
