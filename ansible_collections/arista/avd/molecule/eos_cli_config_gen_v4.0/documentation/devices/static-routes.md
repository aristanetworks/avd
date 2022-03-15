# static-routes
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
  - [Static Routes](#static-routes)
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

## Static Routes

### Static Routes Summary

| VRF | Destination Prefix | Next Hop IP             | Exit interface      | Administrative Distance       | Tag               | Route Name                    | Metric         |
| --- | ------------------ | ----------------------- | ------------------- | ----------------------------- | ----------------- | ----------------------------- | -------------- |
| default | 1.1.1.0/24 | 10.1.1.1 | vlan101 | 1 | - | - | - |
| default | 1.1.2.0/24 | 10.1.1.1 | vlan101 | 200 | 666 | RT-TO-FAKE-DMZ | - |
| customer01 | 1.2.1.0/24 | 10.1.2.1 | vlan202 | 1 | - | - | - |
| customer01 | 1.2.2.0/24 | 10.1.2.1 | vlan101 | 201 | 667 | RT-TO-FAKE-DMZ | - |
| APP | 10.3.4.0/24 | 1.2.3.4 | - | 1 | - | - | - |
| APP | 10.3.5.0/24 | - | Null0 | 1 | - | - | - |

### Static Routes Device Configuration

```eos
!
ip route 1.1.1.0/24 Vlan101 10.1.1.1
ip route 1.1.2.0/24 Vlan101 10.1.1.1 200 tag 666 name RT-TO-FAKE-DMZ
ip route vrf customer01 1.2.1.0/24 Vlan202 10.1.2.1
ip route vrf customer01 1.2.2.0/24 Vlan101 10.1.2.1 201 tag 667 name RT-TO-FAKE-DMZ
ip route vrf APP 10.3.4.0/24 1.2.3.4
ip route vrf APP 10.3.5.0/24 Null0
```

# Multicast

# Filters

# ACL

# Quality Of Service
