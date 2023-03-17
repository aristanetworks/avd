# management-interfaces

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)

## Management

### Management Interfaces

#### Management Interfaces Summary

##### IPv4

| Management Interface | description | Type | VRF | IP Address | Gateway |
| -------------------- | ----------- | ---- | --- | ---------- | ------- |
| Management1 | oob_management | oob | MGMT | 10.73.255.122/24 | 10.73.255.2 |
| Vlan123 | inband_management | inband | default | 10.73.0.123/24 | 10.73.0.1 |

##### IPv6

| Management Interface | description | Type | VRF | IPv6 Address | IPv6 Gateway |
| -------------------- | ----------- | ---- | --- | ------------ | ------------ |
| Management1 | oob_management | oob | MGMT | - | - |
| Vlan123 | inband_management | inband | default | - | - |

#### Management Interfaces Device Configuration

```eos
!
interface Management1
   description oob_management
   vrf MGMT
   ip address 10.73.255.122/24
!
interface Vlan123
   description inband_management
   ip address 10.73.0.123/24
   ip virtual-router address 10.73.0.1
```
