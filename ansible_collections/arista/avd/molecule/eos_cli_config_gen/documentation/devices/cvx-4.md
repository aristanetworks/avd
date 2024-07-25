# cvx-4

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [CVX](#cvx)
  - [CVX Device Configuration](#cvx-device-configuration)

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

## CVX

| Peer Hosts |
| ---------- |
| 1.1.1.3, 2.2.2.3 |

### CVX Device Configuration

```eos
!
cvx
   peer host 1.1.1.3
   peer host 2.2.2.3
   service mcs
      shutdown
```
