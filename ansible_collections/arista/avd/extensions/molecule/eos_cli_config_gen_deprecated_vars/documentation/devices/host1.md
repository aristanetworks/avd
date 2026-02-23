# host1

## Table of Contents

- [Management](#management)
  - [IP Name Server Groups](#ip-name-server-groups)
- [ACL](#acl)
  - [Extended Access-lists](#extended-access-lists)
- [Authentication](#authentication)
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

## ACL

### Extended Access-lists

#### Extended Access-lists Summary

##### 4

| Sequence | Action |
| -------- | ------ |
| 10 | remark ACL to restrict access RFC1918 addresses |
| 20 | deny ip 10.0.0.0/8 any |
| 30 | permit ip 192.0.2.0/24 any |

##### ACL-01

| Sequence | Action |
| -------- | ------ |
| 10 | remark ACL to restrict access to switch API to CVP and Ansible |
| 20 | deny ip host 192.0.2.1 any |
| 30 | permit ip 192.0.2.0/24 any |

##### ACL-02

ACL has counting mode `counters per-entry` enabled!

| Sequence | Action |
| -------- | ------ |
| 10 | remark ACL to restrict access RFC1918 addresses |
| 20 | permit ip 10.0.0.0/8 any |
| 30 | permit ip 192.0.2.0/24 any |
| - | permit response traffic nat |

##### ACL-03

| Sequence | Action |
| -------- | ------ |
| 10 | remark ACL to restrict access RFC1918 addresses |
| 20 | deny ip 10.0.0.0/8 any |
| 30 | permit ip 192.0.2.0/24 any |

##### ACL-04

ACL has counting mode `counters per-entry` enabled!

| Sequence | Action |
| -------- | ------ |
| 20 | deny ip 12.0.0.0/8 any |
| 30 | permit ip 194.0.2.0/24 any |
| - | permit response traffic nat |

##### acl_qos_tc0_v4

| Sequence | Action |
| -------- | ------ |
| 10 | permit ip any 192.0.2.0/29 |

##### acl_qos_tc5_v4

| Sequence | Action |
| -------- | ------ |
| 10 | permit ip any any dscp ef |

#### Extended Access-lists Device Configuration

```eos
!
ip access-list 4
   10 remark ACL to restrict access RFC1918 addresses
   20 deny ip 10.0.0.0/8 any
   30 permit ip 192.0.2.0/24 any
!
ip access-list ACL-01
   10 remark ACL to restrict access to switch API to CVP and Ansible
   20 deny ip host 192.0.2.1 any
   30 permit ip 192.0.2.0/24 any
!
ip access-list ACL-02
   counters per-entry
   10 remark ACL to restrict access RFC1918 addresses
   20 permit ip 10.0.0.0/8 any
   30 permit ip 192.0.2.0/24 any
   permit response traffic nat
!
ip access-list ACL-03
   10 remark ACL to restrict access RFC1918 addresses
   20 deny ip 10.0.0.0/8 any
   30 permit ip 192.0.2.0/24 any
!
ip access-list ACL-04
   counters per-entry
   20 deny ip 12.0.0.0/8 any
   30 permit ip 194.0.2.0/24 any
   permit response traffic nat
!
ip access-list acl_qos_tc0_v4
   10 permit ip any 192.0.2.0/29
!
ip access-list acl_qos_tc5_v4
   10 permit ip any any dscp ef
## Authentication

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
