# ip-http-client-source-interface

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
  - [IP HTTP Client Source Interfaces](#ip-http-client-source-interfaces)

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

### IP HTTP Client Source Interfaces

#### IP HTTP Client Source Interfaces

| VRF | Source Interface Name |
| --- | --------------- |
| default | Loopback0 |
| MGMT | Management0 |
| default | Ethernet10 |

#### IP HTTP Client Source Interfaces Device Configuration

```eos
!
ip http client local-interface Loopback0 vrf default
!
ip http client local-interface Management0 vrf MGMT
!
ip http client local-interface Ethernet10
```
