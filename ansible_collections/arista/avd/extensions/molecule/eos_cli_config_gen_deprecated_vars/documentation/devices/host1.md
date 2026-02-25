# host1

## Table of Contents

- [Management](#management)
  - [IP Name Server Groups](#ip-name-server-groups)
- [Authentication](#authentication)
  - [IP RADIUS Source Interfaces](#ip-radius-source-interfaces)
- [ACL](#acl)
  - [Standard Access-lists](#standard-access-lists)

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

## ACL

### Standard Access-lists

#### Standard Access-lists Summary

##### ACL-API

| Sequence | Action | Source | Remark | Log | Mirror Session |
| -------- | ------ | ------ | ------ | --- | ------------- |
| 10 | remark ACL to restrict access to switch API to CVP and Ansible |
| 20 | permit host 10.10.10.10 |
#### Standard Access-lists Device Configuration

```eos
!
ip access-list standard ACL-API
   10 remark ACL to restrict access to switch API to CVP and Ansible
   20 permit host 10.10.10.10
```
