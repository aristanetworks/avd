# host1

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
  - [IP Name Server Groups](#ip-name-server-groups)
- [Authentication](#authentication)
  - [IP TACACS Source Interfaces](#ip-tacacs-source-interfaces)
  - [IP RADIUS Source Interfaces](#ip-radius-source-interfaces)
- [ACL](#acl)
  - [IPv6 Extended Access-lists](#ipv6-extended-access-lists)

## Management

### Management Interfaces

#### Management Interfaces Summary

##### IPv4

| Management Interface | Description | Type | VRF | IP Address | Gateway |
| -------------------- | ----------- | ---- | --- | ---------- | ------- |
| Management1 | Test_ipv6_address | oob | default | 10.2.255.3/32 | - |

##### IPv6

| Management Interface | Description | Type | VRF | IPv6 Address | IPv6 Gateway | ND RA RX Accept | ND RA Disabled | ND Managed Config Flag |
| -------------------- | ----------- | ---- | --- | ------------ | ------------ | --------------- | -------------- | ---------------------- |
| Management1 | Test_ipv6_address | oob | default | 2002::CAFE/128 | - | - | - | - |

#### Management Interfaces Device Configuration

```eos
!
interface Management1
   description Test_ipv6_address
   ip address 10.2.255.3/32
   ipv6 address 2002::CAFE/128
```

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

## ACL

### IPv6 Extended Access-lists

#### IPv6 Extended Access-lists Summary

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
   5 deny ipv6 fe80::/64 any
   10 permit ipv6 fe90::/64 any
!
ipv6 access-list TEST2
   counters per-entry
   5 permit ipv6 2001:db8::/64 any
   10 deny ipv6 2001:db8::/32 any
!
ipv6 access-list TEST3
   5 deny ipv6 2001:db8:1000::/64 any
   10 permit ipv6 2001:db8::/32 any
!
ipv6 access-list acl_qos_tc0_v6
   10 permit ipv6 any any dscp cs1
!
ipv6 access-list acl_qos_tc5_v6
   10 permit ipv6 any 2001:db8::/48
```
