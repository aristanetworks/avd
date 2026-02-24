# host1

## Table of Contents

- [Management](#management)
  - [IP Name Server Groups](#ip-name-server-groups)

- [ACL](#acl)
  - [IPv6 Access-lists](#ipv6-access-lists)

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

### IPv6 Access-lists

#### IPv6 Access-lists Summary

##### acl_qos_tc0_v6

| Sequence | Action |
| -------- | ------ |
| 10 | permit ipv6 any any dscp cs1 |

##### acl_qos_tc5_v6

| Sequence | Action |
| -------- | ------ |
| 10 | permit ipv6 any 2001:db8::/48 |

##### TEST1

| Sequence | Action |
| -------- | ------ |
| 5 | deny ipv6 fe80::/64 any |
| 10 | permit ipv6 fe90::/64 any |

##### TEST2

ACL has counting mode `counters per-entry` enabled!

| Sequence | Action |
| -------- | ------ |
| 5 | permit ipv6 2001:db8::/64 any |
| 10 | deny ipv6 2001:db8::/32 any |

##### TEST3

| Sequence | Action |
| -------- | ------ |
| 5 | deny ipv6 2001:db8:1000::/64 any |
| 10 | permit ipv6 2001:db8::/32 any |

#### IPv6 Access-lists Device Configuration

```eos
!
ipv6 access-list TEST1
!
ipv6 access-list TEST2
   counters per-entry
!
ipv6 access-list TEST3
!
ipv6 access-list acl_qos_tc0_v6
!
ipv6 access-list acl_qos_tc5_v6

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
