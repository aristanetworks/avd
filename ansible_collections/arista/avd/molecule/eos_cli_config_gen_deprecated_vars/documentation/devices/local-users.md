# local-users
# Table of Contents

- [Authentication](#authentication)
  - [Local Users](#local-users)

# Authentication

## Local Users

### Local Users Summary

| User | Privilege | Role | Disabled | Shell |
| ---- | --------- | ---- | -------- | ----- |
| admin | 15 | network-admin | False | - |

### Local Users Device Configuration

```eos
!
username admin privilege 15 role network-admin nopassword
```
