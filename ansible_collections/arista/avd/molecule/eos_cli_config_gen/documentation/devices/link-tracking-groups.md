# link-tracking-groups

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
  - [Link Tracking](#link-tracking)

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

### Link Tracking

#### Link Tracking Groups Summary

| Group Name | Minimum Links | Recovery Delay |
| ---------- | ------------- | -------------- |
| EVPN_MH_ES1 | 30 | 500 |
| EVPN_MH_ES2 | - | - |

#### Link Tracking Groups Device Configuration

```eos
!
link tracking group EVPN_MH_ES1
   links minimum 30
   recovery delay 500
link tracking group EVPN_MH_ES2
```
