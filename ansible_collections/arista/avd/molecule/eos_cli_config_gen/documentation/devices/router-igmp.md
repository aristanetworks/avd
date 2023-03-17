# router-igmp

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [Multicast](#multicast)
  - [Router IGMP](#router-igmp)

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

## Multicast

### Router IGMP

#### Router IGMP Summary

| Settings | Value |
| -------- | ----- |
| SSM Aware | True |

#### Router IGMP Device Configuration

```eos
!
router igmp
   ssm aware
```
