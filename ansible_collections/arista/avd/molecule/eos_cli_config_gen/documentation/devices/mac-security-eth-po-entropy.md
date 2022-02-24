# mac-security-eth-po-entropy
# Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [Authentication](#authentication)
- [Management Security](#management-security)
  - [Management Security Summary](#management-security-summary)
  - [Management Security SSL Profiles](#management-security-ssl-profiles)
  - [Management Security Configuration](#management-security-configuration)
- [Monitoring](#monitoring)
- [Internal VLAN Allocation Policy](#internal-vlan-allocation-policy)
  - [Internal VLAN Allocation Policy Summary](#internal-vlan-allocation-policy-summary)
- [Interfaces](#interfaces)
  - [Ethernet Interfaces](#ethernet-interfaces)
  - [Port-Channel Interfaces](#port-channel-interfaces)
- [Routing](#routing)
  - [IP Routing](#ip-routing)
  - [IPv6 Routing](#ipv6-routing)
- [Multicast](#multicast)
- [Filters](#filters)
- [ACL](#acl)
- [MACsec](#macsec)
  - [MACsec Summary](#macsec-summary)
  - [MACsec Device Configuration](#macsec-device-configuration)
- [Quality Of Service](#quality-of-service)

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
| Management1 | oob_management | oob | MGMT | -  | - |

### Management Interfaces Device Configuration

```eos
!
interface Management1
   description oob_management
   vrf MGMT
   ip address 10.73.255.122/24
```

# Authentication

# Management Security

## Management Security Summary

| Settings | Value |
| -------- | ----- |
| Entropy source | hardware |
| Common password encryption key | True |

## Management Security SSL Profiles

| SSL Profile Name | TLS protocol accepted | Certificate filename | Key filename |
| ---------------- | --------------------- | -------------------- | ------------ |
| SSL_PROFILE | 1.1 1.2 | SSL_CERT | SSL_KEY |

## Management Security Configuration

```eos
!
management security
   entropy source hardware
   password encryption-key common
   ssl profile SSL_PROFILE
      tls versions 1.1 1.2
      certificate SSL_CERT key SSL_KEY
```

# Monitoring

# Internal VLAN Allocation Policy

## Internal VLAN Allocation Policy Summary

**Default Allocation Policy**

| Policy Allocation | Range Beginning | Range Ending |
| ------------------| --------------- | ------------ |
| ascending | 1006 | 4094 |

# Interfaces

## Ethernet Interfaces

### Ethernet Interfaces Summary

#### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | Channel-Group |
| --------- | ----------- | ---- | ----- | ----------- | ----------- | ------------- |
| Ethernet3 | DC1-AGG01_Ethernet1 | *trunk | *1-5 | *- | *- | 3 |

*Inherited from Port-Channel Interface

#### IPv4

| Interface | Description | Type | Channel Group | IP Address | VRF |  MTU | Shutdown | ACL In | ACL Out |
| --------- | ----------- | -----| ------------- | ---------- | ----| ---- | -------- | ------ | ------- |
| Ethernet1 | - | routed | - | 1.1.1.1/24 | default | - | - | - | - |

### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet1
   mac security profile A1
   no switchport
   ip address 1.1.1.1/24
!
interface Ethernet3
   description DC1-AGG01_Ethernet1
   mac security profile A1
   channel-group 3 mode active
```

## Port-Channel Interfaces

### Port-Channel Interfaces Summary

#### L2

| Interface | Description | Type | Mode | VLANs | Native VLAN | Trunk Group | LACP Fallback Timeout | LACP Fallback Mode | MLAG ID | EVPN ESI |
| --------- | ----------- | ---- | ---- | ----- | ----------- | ------------| --------------------- | ------------------ | ------- | -------- |
| Port-Channel3 | L2-PORT | switched | trunk | 1-5 | - | - | - | - | - | - |

### Port-Channel Interfaces Device Configuration

```eos
!
interface Port-Channel3
   description L2-PORT
   switchport
   switchport trunk allowed vlan 1-5
   switchport mode trunk
```

# Routing

## IP Routing

### IP Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | false |

### IP Routing Device Configuration

```eos
```
## IPv6 Routing

### IPv6 Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | false |

# Multicast

# Filters

# ACL

# MACsec

## MACsec Summary

License is installed.

FIPS restrictions enabled.

### MACsec Profiles Summary

**Profile A1:**

Settings:

| Cipher | Rekey-Period | SCI |
| ------ | ------------ | --- |
| aes128-gcm | 30 | True |

Keys:

| Key ID | Encrypted (Type 7) Key | Fallback |
| ------ | ---------------------- | -------- |
| 1234a | 025756085F535976 | - |
| 1234c | 10195F4C5144405A | True |

**Profile A2:**

Settings:

| Cipher | Rekey-Period | SCI |
| ------ | ------------ | --- |
| - | - | - |

Keys:

| Key ID | Encrypted (Type 7) Key | Fallback |
| ------ | ---------------------- | -------- |
| 1234b | 12485744465E5A53 | - |

## MACsec Device Configuration

```eos
!
mac security
   license license1 123456
   fips restrictions
   !
   profile A1
      cipher aes128-gcm
      key 1234a 7 025756085F535976
      key 1234c 7 10195F4C5144405A fallback
      mka session rekey-period 30
      sci
   profile A2
      key 1234b 7 12485744465E5A53
```

# Quality Of Service
