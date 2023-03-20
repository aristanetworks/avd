# sflow
# Table of Contents

- [Monitoring](#monitoring)
  - [SFlow](#sflow)

# Monitoring

## SFlow

### SFlow Summary

| VRF | SFlow Source | SFlow Destination | Port |
| --- | ------------ | ----------------- | ---- |
| MGMT | - | 10.6.75.59 | 6343 |
| MGMT | - | 10.6.75.62 | 123 |
| MGMT | Ethernet3 | - | - |
| default | - | 10.6.75.62 | 123 |
| default | - | 10.6.75.61 | 6343 |

sFlow is disabled.

### SFlow Device Configuration

```eos
!
sflow vrf MGMT destination 10.6.75.59
sflow vrf MGMT destination 10.6.75.62 123
sflow vrf MGMT source-interface Ethernet3
sflow destination 10.6.75.61
sflow destination 10.6.75.62 123
```
