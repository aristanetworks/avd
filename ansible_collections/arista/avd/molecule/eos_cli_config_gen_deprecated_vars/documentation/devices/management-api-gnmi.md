# management-api-gnmi
# Table of Contents

- [Management](#management)
  - [Management API GNMI](#management-api-gnmi)

# Management

## Management API GNMI

### Management API GNMI Summary

| VRF with GNMI | OCTA |
| ------------- | ---- |
| MGMT | enabled |
| MONITORING | enabled |

### Management API gnmi configuration

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
