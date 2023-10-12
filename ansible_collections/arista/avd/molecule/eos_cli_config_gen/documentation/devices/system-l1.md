# system-l1

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [Interfaces](#interfaces)
  - [System L1 Switch Parameters](#system-l1-switch-parameters)

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

## Interfaces

### System L1 Switch Parameters

#### Configuration for Handling Unsupported L1 Interface Configurations

| Unsupported Type | action |
| ---------------- | -------|
| Speed/duplex | warn |
| Forward error correction | error |

#### System L1 Configuration

```eos
!
system l1
   unsupported speed action warn
   unsupported error-correction action error
```
