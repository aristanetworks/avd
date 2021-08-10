# logging
# Table of Contents
<!-- toc -->
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

## Logging

### Logging Servers and Features Summary

| Type | Level |
| -----| ----- |
| Console | debugging |
| Buffer | informational  |
| Trap | informational |
| Synchronous | error |

| VRF | Source Interface |
| --- | ---------------- |
| default | Loopback0 |
| mgt | Management0 |

| VRF | Hosts |
| --- | ---------------- |
| default | 20.20.20.7 |
| mgt | 10.10.10.7 |

### Logging Servers and Features Device Configuration

```eos
!
logging console debugging
logging buffered 1000000 informational
logging trap informational
logging synchronous level error
logging source-interface Loopback0
logging host 20.20.20.7
logging vrf mgt source-interface Management0
logging vrf mgt host 10.10.10.7
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

# Quality Of Service
