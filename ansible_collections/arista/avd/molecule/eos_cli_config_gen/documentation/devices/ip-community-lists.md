# ip-community-lists

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [Filters](#filters)
  - [Community-lists](#community-lists)
  - [IP Community-lists](#ip-community-lists)

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

## Filters

### Community-lists

#### Community-lists Summary

| Name | Action |
| -------- | ------ |
| TEST1 | permit 1000:1000 |
| TEST2 | permit 2000:3000 |

#### Community-lists Device Configuration

```eos
!
ip community-list TEST1 permit 1000:1000
ip community-list TEST2 permit 2000:3000
```

### IP Community-lists

#### IP Community-lists Summary

| Name | Action | Communities / Regexp |
| ---- | ------ | -------------------- |
| IP_CL_TEST1 | permit | 1001:1001, 1002:1002 |
| IP_CL_TEST1 | deny | 1010:1010 |
| IP_CL_TEST1 | permit | 20:* |
| IP_CL_TEST2 | deny | 1003:1003 |
| IP_RE_TEST1 | permit | ^$ |
| IP_RE_TEST2 | deny | ^100 |

#### IP Community-lists Device Configuration

```eos
!
ip community-list IP_CL_TEST1 permit 1001:1001 1002:1002
ip community-list IP_CL_TEST1 deny 1010:1010
ip community-list regexp IP_CL_TEST1 permit 20:*
ip community-list IP_CL_TEST2 deny 1003:1003
ip community-list regexp IP_RE_TEST1 permit ^$
ip community-list regexp IP_RE_TEST2 deny ^100
```
