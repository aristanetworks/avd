# management-gnmi

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

| VRF with GNMI | OCTA |
| ------------- | ---- |
| MGMT | enabled |
| MONITORING | enabled |


#### Management API gnmi configuration

```eos
!
management api gnmi
   transport grpc MGMT
      ip access-group ACL-GNMI
      vrf MGMT
   transport grpc MONITORING
      vrf MONITORING
   provider eos-native
```
