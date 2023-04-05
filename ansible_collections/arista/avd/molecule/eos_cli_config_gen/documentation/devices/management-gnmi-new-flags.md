# management-gnmi-new-flags

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
  - [Management API GNMI](#management-api-gnmi)

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

### Management API GNMI

#### Management API GNMI Summary

| Transport | SSL Profile | VRF | Notification Timestamp | ACL |
| --------- | ----------- | --- | ---------------------- | --- |
| MGMT | gnmi | MGMT | send-time | acl1 |
| mytransport | - | - | send-time | acl1 |

| Transport | Destination | Destination Port | gNMI SSL Profile | Tunnel SSL Profile | VRF | Local Interface | Local Port | Target ID |
| --------- | ----------- | ---------------- | ---------------- | ------------------ | --- | --------------- | ---------- | --------- |

Provider eos-native is configured.

#### Management API gnmi configuration

```eos
!
management api gnmi
   transport grpc MGMT
      ssl profile gnmi
      vrf MGMT
      ip access-group acl1
      notification timestamp send-time
   transport grpc mytransport
      ip access-group acl1
      notification timestamp send-time
   provider eos-native
```
