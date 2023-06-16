# management-security

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [Management Security](#management-security)
  - [Management Security Summary](#management-security-summary)
  - [Management Security SSL Profiles](#management-security-ssl-profiles)
  - [SSL profile test1-chain-cert Certificates Summary](#ssl-profile-test1-chain-cert-certificates-summary)
  - [SSL profile test1-trust-cert Certificates Summary](#ssl-profile-test1-trust-cert-certificates-summary)
  - [SSL profile test2-chain-cert Certificates Summary](#ssl-profile-test2-chain-cert-certificates-summary)
  - [SSL profile test2-trust-cert Certificates Summary](#ssl-profile-test2-trust-cert-certificates-summary)
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
| test1-chain-cert | - | - | - | - |
| test1-trust-cert | - | - | - | - |
| test2-chain-cert | - | - | - | - |
| test2-trust-cert | - | - | - | - |
| tls-single-version-profile-as-float | 1.0 | - | - | - |
| tls-single-version-profile-as-string | 1.1 | - | - | - |
| tls-versions-profile | 1.0 1.1 | - | - | - |

### SSL profile test1-chain-cert Certificates Summary

| Chain Certificates | Requirement |
| ------------------ | ----------- |
| test-chain-cert1.crt, test-chain-cert2.crt | Basic Constraint CA |

### SSL profile test1-trust-cert Certificates Summary

| Trust Certificates | Requirement | Policy | System |
| ------------------ | ----------- | ------ | ------ |
| test-trust1.crt, test-trust2.crt | Basic Constraint CA | Ignore Expiry Date | - |

### SSL profile test2-chain-cert Certificates Summary

| Chain Certificates | Requirement |
| ------------------ | ----------- |
| - | Root CA Included |

### SSL profile test2-trust-cert Certificates Summary

| Trust Certificates | Requirement | Policy | System |
| ------------------ | ----------- | ------ | ------ |
| - | Hostname must be FQDN | - | Enabled |

### Management Security Configuration

```eos
!
management security
   entropy source hardware
   password encryption-key common
   password encryption reversible aes-256-gcm
   password minimum length 17
   password policy AVD_POLICY minimum digits 3
   password policy AVD_POLICY minimum length 10
   password policy AVD_POLICY minimum lower 2
   password policy AVD_POLICY minimum special 1
   password policy AVD_POLICY minimum upper 1
   password policy AVD_POLICY maximum repetitive 2
   password policy AVD_POLICY maximum sequential 2
   ssl profile certificate-profile
      certificate eAPI.crt key eAPI.key
   ssl profile cipher-list-profile
      cipher-list ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-SHA384
   ssl profile test1-chain-cert
      chain certificate test-chain-cert1.crt
      chain certificate test-chain-cert2.crt
      chain certificate requirement basic-constraint ca true
   ssl profile test1-trust-cert
      trust certificate test-trust1.crt
      trust certificate test-trust2.crt
      trust certificate requirement basic-constraint ca true
      trust certificate policy expiry-date ignore
   ssl profile test2-chain-cert
      chain certificate requirement include root-ca
   ssl profile test2-trust-cert
      trust certificate system
      trust certificate requirement hostname fqdn
   ssl profile tls-single-version-profile-as-float
      tls versions 1.0
   ssl profile tls-single-version-profile-as-string
      tls versions 1.1
   ssl profile tls-versions-profile
      tls versions 1.0 1.1
```
