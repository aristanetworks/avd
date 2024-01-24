# queue_monitor_length

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [Queue Monitor](#queue-monitor)
  - [Queue Monitor Length](#queue-monitor-length)
  - [Queue Monitor Configuration](#queue-monitor-configuration)

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

## Queue Monitor

### Queue Monitor Length

| Setting | Value |
| ------- | ----- |
| Enabled | True
| Logging Interval | 100 |
| Default Thresholds High | 100 |
| Default Thresholds Low | 10 |
| Notifying | enabled |
| TX Latency | enabled |
| CPU Thresholds High | 200000 |
| CPU Thresholds Low | 100000 |

### Queue Monitor Configuration

```eos
!
queue-monitor length
queue-monitor length default thresholds 100 10
queue-monitor length log 100
queue-monitor length notifying
queue-monitor length tx-latency
queue-monitor length cpu thresholds 200000 100000
```
