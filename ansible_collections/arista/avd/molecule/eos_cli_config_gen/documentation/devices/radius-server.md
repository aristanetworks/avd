# radius-server

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [Authentication](#authentication)
  - [RADIUS Server](#radius-server)

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

## Authentication

### RADIUS Server

- Attribute 32 is included in access requests using hostname

- Dynamic Authorization is enabled on port 1700 with SSL profile SSL_PROFILE

#### RADIUS Server Hosts

| VRF | RADIUS Servers | Timeout | Retransmit |
| --- | -------------- | ------- | ---------- |
| mgt | 10.10.11.157 | 1 | 1 |
| mgt | 10.10.11.159 | - | 1 |
| mgt | 10.10.11.160 | 1 | - |
| mgt | 10.10.11.248 | - | - |
| default | 10.10.11.249 | 1 | 1 |
| default | 10.10.11.158 | 1 | 1 |

#### RADIUS Server Device Configuration

```eos
!
radius-server attribute 32 include-in-access-req hostname
radius-server dynamic-authorization port 1700 tls ssl-profile SSL_PROFILE
radius-server host 10.10.11.157 vrf mgt timeout 1 retransmit 1 key 7 <removed>
radius-server host 10.10.11.159 vrf mgt retransmit 1 key 7 <removed>
radius-server host 10.10.11.160 vrf mgt timeout 1 key 7 <removed>
radius-server host 10.10.11.248 vrf mgt key 7 <removed>
radius-server host 10.10.11.249 timeout 1 retransmit 1 key 7 <removed>
radius-server host 10.10.11.158 timeout 1 retransmit 1 key 7 <removed>
```
