# management-gnmi-grpc-tunnel

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


| Transport | Destination | Port | gNMI SSL Profile | Tunnel SSL Profile | VRF | Local Interface | Local Port | Target ID |
| --------- | ----------- | ---- | ---------------- | ------------------ | --- | --------------- | ---------- | --------- |
| gnmic | 10.1.1.100 | 10000 | ssl_profile | ssl_profile | management | Management1 | 10001 | testid1 |


Provider eos-native is configured.

#### Management API gnmi configuration

```eos
!
management api gnmi
   transport grpc-tunnel gnmic
      no shutdown
      vrf management
      tunnel ssl profile ssl_profile
      gnmi ssl profile ssl_profile
      destination 10.1.1.100 port 10000
      local interface Management1 port 10001
      target testid1
   provider eos-native
```
