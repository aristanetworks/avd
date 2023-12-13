# ip-dhcp-relay

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [IP DHCP Relay](#ip-dhcp-relay)
  - [IP DHCP Relay](#ip-dhcp-relay-1)
  - [IP DHCP Relay Device Configuration](#ip-dhcp-relay-device-configuration)

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

## IP DHCP Relay

### IP DHCP Relay

IP DHCP Relay Option 82 is enabled.

### IP DHCP Relay Device Configuration

```eos
!
ip dhcp relay information option
```
