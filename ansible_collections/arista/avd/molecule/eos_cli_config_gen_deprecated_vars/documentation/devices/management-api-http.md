# management-api-http
# Table of Contents

- [Management](#management)
  - [Management API HTTP](#management-api-http)

# Management

## Management API HTTP

### Management API HTTP Summary

| HTTP | HTTPS | Default Services |
| ---- | ----- | ---------------- |
| False | True | - |

### Management API VRF Access

| VRF Name | IPv4 ACL | IPv6 ACL |
| -------- | -------- | -------- |
| mgt | ACL-API | - |

### Management API HTTP Configuration

```eos
!
management api http-commands
   no shutdown
   !
   vrf mgt
      no shutdown
      ip access-group ACL-API
```
