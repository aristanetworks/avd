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
| Vlan42 | SVI Description | default | - | False |

##### IPv4

| Interface | VRF | IP Address | IP Address Virtual | IP Router Virtual Address | VRRP | ACL In | ACL Out |
| --------- | --- | ---------- | ------------------ | ------------------------- | ---- | ------ | ------- |
| Vlan1 |  default  |  -  |  -  |  -  |  -  |  -  |  -  |
| Vlan2 |  default  |  -  |  -  |  -  |  -  |  -  |  -  |
| Vlan42 |  default  |  -  |  10.10.42.1/24  |  -  |  -  |  -  |  -  |

##### IPv6

| Interface | VRF | IPv6 Address | IPv6 Virtual Addresses | Virtual Router Address | VRRP | ND RA Disabled | Managed Config Flag | IPv6 ACL In | IPv6 ACL Out |
| --------- | --- | ------------ | -------------------- | ---------------------- | ---- | -------------- | ------------------- | ----------- | ------------ |
| Vlan1 | default | - | fc00:10:10:1::1/64 | - | - | - | - | - | - |
| Vlan2 | default | 1b11:3a00:22b0:5200::15/64 | fc00:10:10:2::1/64, fc00:10:11:2::1/64, fc00:10:12:2::1/64 | - | - | - | True | - | - |

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
   ipv6 address 1b11:3a00:22b0:5200::15/64
   ipv6 address virtual fc00:10:10:2::1/64
   ipv6 address virtual fc00:10:11:2::1/64
   ipv6 address virtual fc00:10:12:2::1/64
   ipv6 nd managed-config-flag
   ipv6 nd prefix 1b11:3a00:22b0:5200::/64 infinite infinite no-autoconfig
!
interface Vlan42
   description SVI Description
   no shutdown
   ip helper-address 10.10.64.150 source-interface Loopback0
   ip helper-address 10.10.96.150 source-interface Loopback0
   ip helper-address 10.10.96.151 source-interface Loopback0
   ip address virtual 10.10.42.1/24
```
