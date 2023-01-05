# system-control-plane
# Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
  - [System Control-Plane](#system-control-plane)
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

## System Control-Plane

#### TCP MSS Ceiling

| Protocol | Segment Size |
| -------- | -------------|
| IPv4 | 1344 |
| IPv6 | 1366 |

#### Control-Plane Access-Groups

| Protocol | VRF | Access-list |
| -------- | --- | ------------|
| IPv4 | default | acl4_1 |
| IPv4 | red | acl4_2 |
| IPv4 | default | acl4_3 |
| IPv6 | default | acl6_1 |
| IPv6 | blue | acl6_2 |
| IPv6 | default | acl6_3 |

### System Control-Plane Configuration

```eos
!
system control-plane
   tcp mss ceiling ipv4 1344 ipv6 1366
   ip access-group acl4_1 in
   ip access-group acl4_2 vrf red in
   ip access-group acl4_3 vrf default in
   ipv6 access-group acl6_1 in
   ipv6 access-group acl6_2 vrf blue in
   ipv6 access-group acl6_3 vrf default in
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

# ACL

# Quality Of Service
