# ip-nat

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [IP NAT](#ip-nat)
  - [NAT Pools](#nat-pools)

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

## IP NAT
Kernel Buffer Size: 64 MB

### NAT Pools
- Pool Name: **prefix_16**

  Pool Prefix Length: 16

  Pool Utilization Threshold: 1 (action: log)

  Pool Ranges:

  | First IP Address  | Last IP Address | First Port | Last Port |
  | ----------------- | --------------- | ---------- | --------- |
  | 10.0.0.1 | 10.0.255.254 | n.a. | n.a. |
  | 10.1.0.0 | 10.1.255.255 | 1024 | 65535 |

- Pool Name: **prefix_32**

  Pool Prefix Length: 32

  Pool Ranges:

  | First IP Address  | Last IP Address | First Port | Last Port |
  | ----------------- | --------------- | ---------- | --------- |
  | 10.2.0.1 | 10.2.0.1 | n.a. | n.a. |

- Pool Name: **prefix_24**

  Pool Prefix Length: 24

  Pool Utilization Threshold: 100 (action: log)

  Pool Ranges:

  | First IP Address  | Last IP Address | First Port | Last Port |
  | ----------------- | --------------- | ---------- | --------- |
  | 10.3.0.1 | 10.3.0.254 | n.a. | n.a. |
  | 10.3.1.0 | 10.3.1.255 | 1024 | 65535 |

