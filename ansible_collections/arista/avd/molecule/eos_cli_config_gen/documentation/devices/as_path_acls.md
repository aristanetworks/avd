# as_path_acls
# Table of Contents
<!-- toc -->

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
  - [Standard Access-lists](#standard-access-lists)
- [Quality Of Service](#quality-of-service)

<!-- toc -->
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
| default | false|
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

## Standard Access-lists

### Standard Access-lists Summary

#### ACL-API
                      | NAME | Action | AS-Number or REGEX | any |
                      | -----| ------ | ------------------ | --- | 
ip as-path access-list BGP-ACL deny 65400 any
ip as-path access-list BGP-ACL deny 65400 any
ip as-path access-list BGP-ACL deny 65200 any
ip as-path access-list BGP-ACL deny 4200009999 any
ip as-path access-list BGP-ACL permit .* any
ip as-path access-list BGP-ACL deny 65400 any
ip as-path access-list BGP-ACL deny 65200 any
ip as-path access-list BGP-ACL deny 4200009999 any
ip as-path access-list BGP-ACL permit .* any

#### ACL-SSH


#### ACL-SSH-VRF


### Standard Access-lists Device Configuration

# Quality Of Service
