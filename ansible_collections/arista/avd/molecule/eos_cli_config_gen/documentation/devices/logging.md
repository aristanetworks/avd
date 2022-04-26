# logging
# Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [Authentication](#authentication)
- [Monitoring](#monitoring)
  - [Logging](#logging)
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

# Authentication

# Monitoring

## Logging

### Logging Servers and Features Summary

| Type | Level |
| -----| ----- |
| Console | error |
| Buffer | warnings |
| Trap | disabled |
| Synchronous | critical |

| Format Type | Setting |
| ----------- | ------- |
| Timestamp | traditional year timezone |
| Hostname | hostname |
| Sequence-numbers | false |

| VRF | Source Interface |
| --- | ---------------- |
| default | Loopback0 |
| mgt | Management0 |

| VRF | Hosts | Ports | Protocol |
| --- | ----- | ----- | -------- |
| default | 20.20.20.7 | Default | UDP |
| default | 50.50.50.7 | 100, 200 | TCP |
| default | 60.60.60.7 | 100, 200 | UDP |
| mgt | 10.10.10.7 | Default | UDP |
| mgt | 30.30.30.7 | 100, 200 | TCP |
| mgt | 40.40.40.7 | 300, 400 | UDP |
| vrf_with_no_source_interface | 1.2.3.4 | Default | UDP |

### Logging Servers and Features Device Configuration

```eos
!
logging buffered 1000000 warnings
no logging trap
logging console error
logging synchronous level critical
logging host 20.20.20.7
logging host 50.50.50.7 100 200 protocol tcp
logging host 60.60.60.7 100 200
logging vrf mgt host 10.10.10.7
logging vrf mgt host 30.30.30.7 100 200 protocol tcp
logging vrf mgt host 40.40.40.7 300 400
logging vrf vrf_with_no_source_interface host 1.2.3.4
logging format timestamp traditional year timezone
logging source-interface Loopback0
logging vrf mgt source-interface Management0
```

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
