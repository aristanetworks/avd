# router-general
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
  - [Router General](#router-general)
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

## Router General

- Global IPv4 Router ID: 10.1.2.3

- Global IPv6 Router ID: 2001:beef:cafe::1

- Nexthop fast fail-over is enabled.

### VRF Route leaking

| VRF | Source VRF | Route Map Policy |
|-----|------------|------------------|
| BLUE-C2 | BLUE-C1 | RM-BLUE-LEAKING |
| BLUE-C2 | BLUE-C3 | RM-BLUE-LEAKING |

### VRF Routes Dynamic Prefix-lists

| VRF | Dynamic Prefix-list |
|-----|---------------------|
| BLUE-C2 | DYNAMIC_TEST_PREFIX_LIST_1 |
| BLUE-C2 | DYNAMIC_TEST_PREFIX_LIST_2 |

### Router General configuration

```eos
!
router general
   router-id ipv4 10.1.2.3
   router-id ipv6 2001:beef:cafe::1
   hardware next-hop fast-failover
   !
   vrf BLUE-C2
      leak routes source-vrf BLUE-C1 subscribe-policy RM-BLUE-LEAKING
      leak routes source-vrf BLUE-C3 subscribe-policy RM-BLUE-LEAKING
      routes dynamic prefix-list DYNAMIC_TEST_PREFIX_LIST_1
      routes dynamic prefix-list DYNAMIC_TEST_PREFIX_LIST_2
   !
```

# Multicast

# Filters

# ACL

# Quality Of Service
