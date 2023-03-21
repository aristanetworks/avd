# platform

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [Platform](#platform)
  - [Platform Summary](#platform-summary)
  - [Platform Configuration](#platform-configuration)

## Management

### Management Interfaces

#### Management Interfaces Summary

##### IPv4

| Management Interface | description | Type | VRF | IP Address | Gateway |
| -------------------- | ----------- | ---- | --- | ---------- | ------- |
| Management1 | oob_management | oob | MGMT | 10.73.255.122/24 | 10.73.255.2 |

##### IPv6

| Management Interface | description | Type | VRF | IPv6 Address | IPv6 Gateway |
| -------------------- | ----------- | ---- | --- | ------------ | ------------ |
| Management1 | oob_management | oob | MGMT | - | - |

#### Management Interfaces Device Configuration

```eos
!
interface Management1
   description oob_management
   vrf MGMT
   ip address 10.73.255.122/24
```

## Platform

### Platform Summary

#### Platform Trident Summary

| Settings | Value |
| -------- | ----- |
| forwarding_table_partition | 2 |

#### Platform Sand Summary

| Settings | Value |
| -------- | ----- |
| Forwarding Mode | arad |
| Hardware Only Lag | True |
| Lag Mode | 512x32 |
| Default Multicast Replication | ingress |

### Platform Configuration

```eos
!
platform trident forwarding-table partition 2
platform sand lag hardware-only
platform sand lag mode 512x32
platform sand forwarding mode arad
platform sand multicast replication default ingress
```
