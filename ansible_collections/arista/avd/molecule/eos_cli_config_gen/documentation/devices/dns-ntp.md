# dns-ntp

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
  - [DNS Domain](#dns-domain)
  - [Name Servers](#name-servers)
  - [Domain Lookup](#domain-lookup)
  - [NTP](#ntp)

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

### DNS Domain

#### DNS domain: test.local

#### DNS Domain Device Configuration

```eos
dns domain test.local
!
```

### Name Servers

#### Name Servers Summary

| Name Server | Source VRF |
| ----------- | ---------- |
| 10.10.128.10 | mgt |
| 10.10.129.10 | mgt |

#### Name Servers Device Configuration

```eos
ip name-server vrf mgt 10.10.128.10
ip name-server vrf mgt 10.10.129.10
```

### Domain Lookup

#### DNS Domain Lookup Summary

| Source interface | vrf |
| ---------------- | --- |
| Loopback0 | - |
| Management0 | mgt |

#### DNS Domain Lookup Device Configuration

```eos
ip domain lookup source-interface Loopback0
ip domain lookup vrf mgt source-interface Management0
```

### NTP

#### NTP Summary

##### NTP Local Interface

| Interface | VRF |
| --------- | --- |
| Management0 | mgt |

##### NTP Servers

| Server | VRF | Preferred | Burst | iBurst | Version | Min Poll | Max Poll | Local-interface | Key |
| ------ | --- | --------- | ----- | ------ | ------- | -------- | -------- | --------------- | --- |
| 10.10.111.1 | mgt | True | - | - | - | - | - | - | - |
| 10.10.111.2 | mgt | - | - | - | - | - | - | - | - |

##### NTP Authentication

- Authentication enabled (Servers only)

- Trusted Keys: 1-2

##### NTP Authentication Keys

| ID | Algorithm |
| -- | -------- |
| 1 | md5 |
| 2 | sha1 |

#### NTP Device Configuration

```eos
!
ntp authentication-key 1 md5 044F0E151B
ntp authentication-key 2 sha1 15060E1F10
ntp trusted-key 1-2
ntp authenticate servers
ntp local-interface vrf mgt Management0
ntp server vrf mgt 10.10.111.1 prefer
ntp server vrf mgt 10.10.111.2
```
