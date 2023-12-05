# boot

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [System Boot Settings](#system-boot-settings)
  - [Boot Secret Summary](#boot-secret-summary)
  - [System Boot Device Configuration](#system-boot-device-configuration)

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

## System Boot Settings

### Boot Secret Summary

- The md5 hashed Aboot password is configured

### System Boot Device Configuration

```eos
!
boot secret 5 <removed>
```
