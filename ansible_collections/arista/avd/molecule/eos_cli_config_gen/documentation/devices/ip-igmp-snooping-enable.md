# ip-igmp-snooping-enable
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
  - [IP IGMP Snooping](#ip-igmp-snooping)
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

# Multicast

## IP IGMP Snooping

### IP IGMP Snooping Summary

| Global Settings | Values |
| --------------- | ------ |
| IGMP snooping | Enabled |
| Fast-leave | True |
| Interface restart query | 500 |
| Proxy | True |
| Restart query interval | 30 |
| Robustness variable | 2 |

| Global Querier Settings | Values |
| ----------------------- | ------ |
| Address | 10.10.10.1 |
| Enabled | True |
| Last member query count | 2 |
| Last member query interval | 5 |
| Max response time | 10 |
| Query interval | 40 |
| Startup query count | 2 |
| Startup query interval | 20 |
| Version | 3 |

#### IP IGMP Snooping Vlan 23 Settings Summary

| Settings | Values |
| -------- | ------ |
| IGMP snooping | Enabled |
| Fast-leave | True |
| Max groups | 20 |
| Proxy | True |

| Vlan Querier Settings | Values |
| --------------------- | ------ |
| Address | 10.10.23.1 |
| Enabled | True |
| Last member query count | 2 |
| Last member query interval | 5 |
| Max response time | 10 |
| Query interval | 40 |
| Startup query count | 2 |
| Startup query interval | 20 |
| Version | 3 |

#### IP IGMP Snooping Vlan 24 Settings Summary

| Settings | Values |
| -------- | ------ |
| IGMP snooping | Enabled |
| Fast-leave | False |
| Proxy | False |

#### IP IGMP Snooping Vlan 25 Settings Summary

| Settings | Values |
| -------- | ------ |
| IGMP snooping | Disabled |

### IP IGMP Snooping Device Configuration

```eos
!
ip igmp snooping
ip igmp snooping robustness-variable 2
ip igmp snooping restart query-interval 30
ip igmp snooping interface-restart-query 500
ip igmp snooping fast-leave
ip igmp snooping vlan 23
ip igmp snooping vlan 23 querier
ip igmp snooping vlan 23 querier address 10.10.23.1
ip igmp snooping vlan 23 querier query-interval 40
ip igmp snooping vlan 23 querier max-response-time 10
ip igmp snooping vlan 23 querier last-member-query-interval 5
ip igmp snooping vlan 23 querier last-member-query-count 2
ip igmp snooping vlan 23 querier startup-query-interval 20
ip igmp snooping vlan 23 querier startup-query-count 2
ip igmp snooping vlan 23 querier version 3
ip igmp snooping vlan 23 max-groups 20
ip igmp snooping vlan 23 fast-leave
ip igmp snooping vlan 24
no ip igmp snooping vlan 24 fast-leave
no ip igmp snooping vlan 25
ip igmp snooping querier
ip igmp snooping querier address 10.10.10.1
ip igmp snooping querier query-interval 40
ip igmp snooping querier max-response-time 10
ip igmp snooping querier last-member-query-interval 5
ip igmp snooping querier last-member-query-count 2
ip igmp snooping querier startup-query-interval 20
ip igmp snooping querier startup-query-count 2
ip igmp snooping querier version 3
!
ip igmp snooping vlan 23 proxy
no ip igmp snooping vlan 24 proxy
ip igmp snooping proxy
```

# Filters

# ACL

# Quality Of Service
