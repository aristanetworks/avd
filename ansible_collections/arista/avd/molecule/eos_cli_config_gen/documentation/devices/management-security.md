# management-security

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [Management Security](#management-security)
  - [Management Security Summary](#management-security-summary)
  - [Management Security SSL Profiles](#management-security-ssl-profiles)
  - [Management Security Configuration](#management-security-configuration)

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

## Management Security

### Management Security Summary

| Settings | Value |
| -------- | ----- |
| Entropy source | hardware |
| Common password encryption key | True |
| Reversible password encryption | aes-256-gcm |
| Minimum password length | 17 |

### Management Security SSL Profiles

| SSL Profile Name | TLS protocol accepted | Certificate filename | Key filename | Cipher List |
| ---------------- | --------------------- | -------------------- | ------------ | ----------- |
| certificate-profile | - | eAPI.crt | eAPI.key | - |
| cipher-list-profile | - | - | - | ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-SHA384 |
| tls-single-version-profile-as-float | 1.0 | - | - | - |
| tls-single-version-profile-as-string | 1.1 | - | - | - |
| tls-versions-profile | 1.0 1.1 | - | - | - |

### Management Security Configuration

```eos
!
management security
   entropy source hardware
   password encryption-key common
   password encryption reversible aes-256-gcm
   password minimum length 17
   ssl profile certificate-profile
      certificate eAPI.crt key eAPI.key
   ssl profile cipher-list-profile
      cipher-list ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-SHA384
   ssl profile tls-single-version-profile-as-float
      tls versions 1.0
   ssl profile tls-single-version-profile-as-string
      tls versions 1.1
   ssl profile tls-versions-profile
      tls versions 1.0 1.1
```
