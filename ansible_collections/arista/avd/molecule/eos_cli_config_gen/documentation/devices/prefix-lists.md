# prefix-lists
# Table of Contents

- [prefix-lists](#prefix-lists)
- [Table of Contents](#table-of-contents)
- [Management](#management)
  - [Management Interfaces](#management-interfaces)
    - [Management Interfaces Summary](#management-interfaces-summary)
      - [IPv4](#ipv4)
      - [IPv6](#ipv6)
    - [Management Interfaces Device Configuration](#management-interfaces-device-configuration)
- [Authentication](#authentication)
- [Monitoring](#monitoring)
- [Internal VLAN Allocation Policy](#internal-vlan-allocation-policy)
  - [Internal VLAN Allocation Policy Summary](#internal-vlan-allocation-policy-summary)
- [Interfaces](#interfaces)
- [Routing](#routing)
  - [IP Routing](#ip-routing)
    - [IP Routing Summary](#ip-routing-summary)
    - [IP Routing Device Configuration](#ip-routing-device-configuration)
  - [IPv6 Routing](#ipv6-routing)
    - [IPv6 Routing Summary](#ipv6-routing-summary)
- [Multicast](#multicast)
- [Filters](#filters)
  - [Dynamic Prefix-lists](#dynamic-prefix-lists)
    - [Dynamic Prefix-lists Summary](#dynamic-prefix-lists-summary)
      - [DYNAMIC_PREFIX_LIST_NAME_1](#dynamic_prefix_list_name_1)
      - [DYNAMIC_PREFIX_LIST_NAME_2](#dynamic_prefix_list_name_2)
    - [Dynamic Prefix-lists Device Configuration](#dynamic-prefix-lists-device-configuration)
  - [Prefix-lists](#prefix-lists-1)
    - [Prefix-lists Summary](#prefix-lists-summary)
      - [PL-LOOPBACKS-EVPN-OVERLAY](#pl-loopbacks-evpn-overlay)
    - [Prefix-lists Device Configuration](#prefix-lists-device-configuration)
  - [IPv6 Prefix-lists](#ipv6-prefix-lists)
    - [IPv6 Prefix-lists Summary](#ipv6-prefix-lists-summary)
      - [PL-IPV6-LOOPBACKS](#pl-ipv6-loopbacks)
    - [IPv6 Prefix-lists Device Configuration](#ipv6-prefix-lists-device-configuration)
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

# Multicast

# Filters

## Dynamic Prefix-lists

### Dynamic Prefix-lists Summary

#### DYNAMIC_PREFIX_LIST_NAME_1

| Match Map | Prefix-list |
| --------- | ----------- |
|Test_1 | IPV4_PREFIX_LIST |

#### DYNAMIC_PREFIX_LIST_NAME_2

| Match Map | Prefix-list |
| --------- | ----------- |
|Test_2 | IPV6_PREFIX_LIST |

### Dynamic Prefix-lists Device Configuration

```eos
dynamic pefix-list DYNAMIC_PREFIX_LIST_NAME_1
   match_map Test_1
    prefix_list ipv4 IPV4_PREFIX_LIST
!
dynamic pefix-list DYNAMIC_PREFIX_LIST_NAME_2
   match_map Test_2
    prefix_list ipv6 IPV6_PREFIX_LIST
!
```

## Prefix-lists

### Prefix-lists Summary

#### PL-LOOPBACKS-EVPN-OVERLAY

| Sequence | Action |
| -------- | ------ |
| 10 | permit 192.168.255.0/24 eq 32 |
| 20 | permit 192.168.254.0/24 eq 32 |

### Prefix-lists Device Configuration

```eos
!
ip prefix-list PL-LOOPBACKS-EVPN-OVERLAY
   seq 10 permit 192.168.255.0/24 eq 32
   seq 20 permit 192.168.254.0/24 eq 32
```

## IPv6 Prefix-lists

### IPv6 Prefix-lists Summary

#### PL-IPV6-LOOPBACKS

| Sequence | Action |
| -------- | ------ |
| 10 | permit 1b11:3a00:22b0:0082::/64 eq 128 |

### IPv6 Prefix-lists Device Configuration

```eos
!
ipv6 prefix-list PL-IPV6-LOOPBACKS
   seq 10 permit 1b11:3a00:22b0:0082::/64 eq 128
```

# ACL

# Quality Of Service
