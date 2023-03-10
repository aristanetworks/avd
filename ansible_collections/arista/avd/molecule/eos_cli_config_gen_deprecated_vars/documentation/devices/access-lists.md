# access-lists
# Table of Contents

- [ACL](#acl)
  - [Extended Access-lists](#extended-access-lists)

# ACL

## Extended Access-lists

### Extended Access-lists Summary

#### ACL-01

| Sequence | Action |
| -------- | ------ |
| 10 | remark ACL to restrict access to switch API to CVP and Ansible |
| 20 | deny ip host 192.0.2.1 any |
| 30 | permit ip 192.0.2.0/24 any |

### Extended Access-lists Device Configuration

```eos
!
ip access-list ACL-01
   10 remark ACL to restrict access to switch API to CVP and Ansible
   20 deny ip host 192.0.2.1 any
   30 permit ip 192.0.2.0/24 any
```
