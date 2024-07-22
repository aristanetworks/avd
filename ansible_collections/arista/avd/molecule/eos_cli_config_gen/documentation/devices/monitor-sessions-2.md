# monitor-sessions-2

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [Monitoring](#monitoring)
  - [Monitor Sessions](#monitor-sessions)
  - [Monitor Sessions Default](#monitor-sessions-default)

## Management

### Management Interfaces

#### Management Interfaces Summary

##### IPv4

| Management Interface | Description | Type | VRF | IP Address | Gateway |
| -------------------- | ----------- | ---- | --- | ---------- | ------- |
| Management1 | oob_management | oob | MGMT | 10.73.255.122/24 | 10.73.255.2 |

##### IPv6

| Management Interface | Description | Type | VRF | IPv6 Address | IPv6 Gateway |
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

## Monitoring

### Monitor Sessions

#### Monitor Sessions Summary

### Monitor Sessions Default

| Settings | Values |
| -------- | ------ |
| Encapsulation GRE Payload | inner-packet |

#### Monitor Sessions Device Configuration

```eos
!
monitor session default encapsulation gre payload inner-packet
```
