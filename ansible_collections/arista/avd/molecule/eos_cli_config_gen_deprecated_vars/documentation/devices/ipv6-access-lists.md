# ipv6-access-lists
# Table of Contents

- [ACL](#acl)
  - [IPv6 Extended Access-lists](#ipv6-extended-access-lists)

# ACL

## IPv6 Extended Access-lists

### IPv6 Extended Access-lists Summary

#### TEST1

| Sequence | Action |
| -------- | ------ |
| 5 | deny ipv6 fe80::/64 any |
| 10 | permit ipv6 fe90::/64 any |

### IPv6 Extended Access-lists Device Configuration

```eos
!
ipv6 access-list TEST1
   5 deny ipv6 fe80::/64 any
   10 permit ipv6 fe90::/64 any
```
