# ipv6-static-routes
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
  - [IPv6 Static Routes](#ipv6-static-routes)
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

## IPv6 Static Routes

### IPv6 Static Routes Summary

| VRF | Destination Prefix | Next Hop IP             | Exit interface      | Administrative Distance       | Tag               | Route Name                    | Metric         |
| --- | ------------------ | ----------------------- | ------------------- | ----------------------------- | ----------------- | ----------------------------- | -------------- |
| default | 2a01:cb04:4e6:d300::/64 | 2a01:cb04:4e6:d100::1 | vlan101 | 1 | - | - | - |
| default | 2a01:cb04:4e6:d400::/64 | 2a01:cb04:4e6:d100::1 | vlan101 | 200 | 666 | RT-TO-FAKE-DMZ | - |
| default | 2a01:cb04:4e6:d400::/64 | 2a01:cb04:4e6:d100::1 | vlan101 | 200 | 666 | RT-TO-FAKE-DB-ZONE | 100 |
| customer01 | 2a01:cb04:4e6:a300::/64 | 2a01:cb04:4e6:100::1 | vlan101 | 1 | - | - | - |
| customer01 | 2a01:cb04:4e6:a400::/64 | 2a01:cb04:4e6:100::1 | vlan101 | 201 | 667 | RT-TO-FAKE-DMZ | - |

### Static Routes Device Configuration

```eos
!
ipv6 route 2a01:cb04:4e6:d300::/64 Vlan101 2a01:cb04:4e6:d100::1
ipv6 route 2a01:cb04:4e6:d400::/64 Vlan101 2a01:cb04:4e6:d100::1 200 tag 666 name RT-TO-FAKE-DMZ
ipv6 route 2a01:cb04:4e6:d400::/64 Vlan101 2a01:cb04:4e6:d100::1 200 tag 666 name RT-TO-FAKE-DB-ZONE metric 100
ipv6 route vrf customer01 2a01:cb04:4e6:a300::/64 Vlan101 2a01:cb04:4e6:100::1
ipv6 route vrf customer01 2a01:cb04:4e6:a400::/64 Vlan101 2a01:cb04:4e6:100::1 201 tag 667 name RT-TO-FAKE-DMZ
```

# Multicast

# Filters

# ACL

# Quality Of Service
