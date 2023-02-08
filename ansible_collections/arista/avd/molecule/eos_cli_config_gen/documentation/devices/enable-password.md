# enable-password
# Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [Authentication](#authentication)
  - [Enable Password](#enable-password)

# Management

## Management Interfaces

### Management Interfaces Summary

#### IPv4

| Management Interface | description | Type | VRF | IP Address | Gateway |
| -------------------- | ----------- | ---- | --- | ---------- | ------- |
| Management1 | oob_management | oob | MGMT | 10.73.255.122/24 | 10.73.255.2 |

#### IPv6

| Management Interface | description | Type | VRF | IPv6 Address | IPv6 Gateway |
| -------------------- | ----------- | ---- | --- | ------------ | ------------ |
| Management1 | oob_management | oob | MGMT | - | - |

### Management Interfaces Device Configuration

```eos
!
interface Management1
   description oob_management
   vrf MGMT
   ip address 10.73.255.122/24
```

# Authentication

## Enable Password

sha512 encrypted enable password is configured
### Enable password configuration

```eos
!
enable password sha512 $6$nXycSRhVPaxRINPL$tM1MNjjRCbFD5di4XWsj8CPkm8Pdwmf9fVqRV015y3DXD4t1vi8CAWQpFP8Vbi9Y2i7.JuFey5UaafXvI6quD1
!
```
