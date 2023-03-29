# ip-routing

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [Routing](#routing)
  - [IP Routing](#ip-routing)
  - [IPv6 Routing](#ipv6-routing)
- [VRF Instances](#vrf-instances)
  - [VRF Instances Summary](#vrf-instances-summary)
  - [VRF Instances Device Configuration](#vrf-instances-device-configuration)

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

## Routing

### IP Routing

#### IP Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | True (ipv6 interfaces) |
| TEST1 | True |
| TEST2 | True (ipv6 interfaces) |

#### IP Routing Device Configuration

```eos
!
ip routing ipv6 interfaces
no ip icmp redirect
ip routing vrf TEST1
ip routing ipv6 interfaces vrf TEST2
```

### IPv6 Routing

#### IPv6 Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | True |
| default | true |
| TEST1 | true |
| TEST2 | false |

#### IPv6 Routing Device Configuration

```eos
!
ipv6 unicast-routing
ipv6 unicast-routing vrf TEST1
no ipv6 icmp redirect
```

## VRF Instances

### VRF Instances Summary

| VRF Name | IP Routing |
| -------- | ---------- |
| TEST1 | enabled |
| TEST2 | enabled (ipv6 interface) |

### VRF Instances Device Configuration

```eos
!
vrf instance TEST1
!
vrf instance TEST2
```
