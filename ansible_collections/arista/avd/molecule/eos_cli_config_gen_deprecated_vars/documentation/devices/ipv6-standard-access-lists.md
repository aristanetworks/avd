# ipv6-standard-access-lists
# Table of Contents

- [ACL](#acl)
  - [IPv6 Standard Access-lists](#ipv6-standard-access-lists)

# ACL

## IPv6 Standard Access-lists

### IPv6 Standard Access-lists Summary

#### TEST4

| Sequence | Action |
| -------- | ------ |
| 5 | deny fe80::/64 |
| 10 | permit fe90::/64 |

### IPv6 Standard Access-lists Device Configuration

```eos
!
ipv6 access-list standard TEST4
   5 deny fe80::/64
   10 permit fe90::/64
```
