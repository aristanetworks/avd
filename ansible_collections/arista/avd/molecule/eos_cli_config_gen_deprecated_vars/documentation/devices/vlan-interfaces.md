# vlan-interfaces

## Table of Contents

- [Interfaces](#interfaces)
  - [VLAN Interfaces](#vlan-interfaces)

## Interfaces

### VLAN Interfaces

#### VLAN Interfaces Summary

| Interface | Description | VRF |  MTU | Shutdown |
| --------- | ----------- | --- | ---- | -------- |
| Vlan1 | test ipv6_address_virtual | default | - | - |
| Vlan2 | test ipv6_address_virtual and ipv6_address_virtuals | default | - | - |

##### IPv4

| Interface | VRF | IP Address | IP Address Virtual | IP Router Virtual Address | VRRP | ACL In | ACL Out |
| --------- | --- | ---------- | ------------------ | ------------------------- | ---- | ------ | ------- |
| Vlan1 |  default  |  -  |  -  |  -  |  -  |  -  |  -  |
| Vlan2 |  default  |  -  |  -  |  -  |  -  |  -  |  -  |

##### IPv6

| Interface | VRF | IPv6 Address | IPv6 Virtual Addresses | Virtual Router Address | VRRP | ND RA Disabled | Managed Config Flag | IPv6 ACL In | IPv6 ACL Out |
| --------- | --- | ------------ | -------------------- | ---------------------- | ---- | -------------- | ------------------- | ----------- | ------------ |
| Vlan1 | default | - | fc00:10:10:1::1/64 | - | - | - | - | - | - |
| Vlan2 | default | - | fc00:10:10:2::1/64, fc00:10:11:2::1/64, fc00:10:12:2::1/64 | - | - | - | - | - | - |

#### VLAN Interfaces Device Configuration

```eos
!
interface Vlan1
   description test ipv6_address_virtual
   ipv6 enable
   ipv6 address virtual fc00:10:10:1::1/64
!
interface Vlan2
   description test ipv6_address_virtual and ipv6_address_virtuals
   ipv6 enable
   ipv6 address virtual fc00:10:10:2::1/64
   ipv6 address virtual fc00:10:11:2::1/64
   ipv6 address virtual fc00:10:12:2::1/64
```
