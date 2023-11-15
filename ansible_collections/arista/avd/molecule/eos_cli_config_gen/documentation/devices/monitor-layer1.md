# monitor-layer1

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [Monitor Layer1 Logging](#monitor-layer1-logging)
  - [Monitor Layer1 Device Configuration](#monitor-layer1-device-configuration)

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

## Monitor Layer1 Logging

| Logging |
| ------- |
| mac fault |
| transceiver dom |
| transceiver communication |

### Monitor Layer1 Device Configuration

```eos
!
monitor layer1
   logging transceiver dom
   logging transceiver communication
   logging mac fault
```
