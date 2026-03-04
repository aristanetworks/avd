# host1

## Table of Contents

- [Management](#management)
  - [IP Name Server Groups](#ip-name-server-groups)
- [Authentication](#authentication)
  - [IP TACACS Source Interfaces](#ip-tacacs-source-interfaces)
  - [IP RADIUS Source Interfaces](#ip-radius-source-interfaces)

## Management

### IP Name Server Groups

#### IP Name Server Groups Summary

##### mynameserver1

###### Name Server

| IP Address | VRF | Priority |
| ---------- | --- | -------- |
| 1.1.1.1 | default | 1 |
| 2.2.2.4 | vrf1 | 4 |
| 8.8.8.8 | vrf1 | - |

#### IP Name Server Groups Device Configuration

```eos
!
ip name-server group mynameserver1
   name-server vrf vrf1 8.8.8.8
   name-server vrf default 1.1.1.1 priority 1
   name-server vrf vrf1 2.2.2.4 priority 4
```

## Authentication

### IP TACACS Source Interfaces

#### IP TACACS Source Interfaces

| VRF | Source Interface Name |
| --- | --------------------- |
| default | Loopback1 |
| TEST1 | Loopback3 |
| default | Loopback10 |

#### IP TACACS Source Interfaces Device Configuration

```eos
!
ip tacacs vrf default source-interface Loopback1
ip tacacs vrf TEST1 source-interface Loopback3
ip tacacs source-interface Loopback10
```

### IP RADIUS Source Interfaces

#### IP RADIUS Source Interfaces

| VRF | Source Interface Name |
| --- | --------------- |
| default | Loopback1 |
| default | Loopback10 |
| MGMT | Management1 |

#### IP SOURCE Source Interfaces Device Configuration

```eos
!
ip radius vrf default source-interface Loopback1
ip radius source-interface Loopback10
ip radius vrf MGMT source-interface Management1
```
