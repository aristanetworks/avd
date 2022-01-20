# ntp
# Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
  - [NTP](#ntp)
- [Authentication](#authentication)
- [Monitoring](#monitoring)
- [Internal VLAN Allocation Policy](#internal-vlan-allocation-policy)
  - [Internal VLAN Allocation Policy Summary](#internal-vlan-allocation-policy-summary)
- [Interfaces](#interfaces)
- [Routing](#routing)
  - [IP Routing](#ip-routing)
  - [IPv6 Routing](#ipv6-routing)
- [Multicast](#multicast)
- [Filters](#filters)
- [ACL](#acl)
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

## NTP

### NTP Summary

#### NTP Local Interface

| Interface | VRF |
| --------- | --- |
| lo1 | default |

#### NTP Servers

| Server | VRF | Preferred | Burst | iBurst | Version | Min Poll | Max Poll | Local-interface | Key |
| ------ | --- | --------- | ----- | ------ | ------- | -------- | -------- | --------------- | --- |
| 1.2.3.4 | - | - | - | - | - | - | - | lo0 | - |
| 2.2.2.55 | - | - | - | - | - | - | - | - | - |
| 10.1.1.1 | - | - | - | - | - | - | - | - | - |
| 10.1.1.2 | - | True | - | - | - | - | - | - | - |
| 20.20.20.1 | - | - | - | - | - | - | - | - | 2 |
| ie.pool.ntp.org | - | - | False | True | - | - | - | - | 1 |

#### NTP Authentication

- Authentication enabled

- Trusted Keys: 1-2

#### NTP Authentication Keys

| ID | Algoritm |
| -- | -------- |
| 1 | md5 |
| 2 | sha1 |

### NTP Device Configuration

```eos
!
ntp authentication-key 1 md5 044F0E151B
ntp authentication-key 2 sha1 15060E1F10
ntp trusted-key 1-2
ntp authenticate
ntp local-interface lo1
ntp server 1.2.3.4 local-interface lo0
ntp server 2.2.2.55
ntp server 10.1.1.1
ntp server 10.1.1.2 prefer
ntp server 20.20.20.1 key 2
ntp server ie.pool.ntp.org iburst key 1
```

# Authentication

# Monitoring

# Internal VLAN Allocation Policy

## Internal VLAN Allocation Policy Summary

**Default Allocation Policy**

| Policy Allocation | Range Beginning | Range Ending |
| ------------------| --------------- | ------------ |
| ascending | 1006 | 4094 |

# Interfaces

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

# Quality Of Service
