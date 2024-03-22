# router-service-insertion

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [Routing](#routing)
- [Network Services Information](#network-services-information)
- [Router Service-Insertion Configuration](#router-service-insertion-configuration)

## Management

### Management Interfaces

#### Management Interfaces Summary

##### IPv4

| Management Interface | Description | Type | VRF | IP Address | Gateway |
| -------------------- | ----------- | ---- | --- | ---------- | ------- |
| Management1 | oob_management | oob | MGMT | 10.73.255.122/24 | 10.73.255.2 |

##### IPv6

| Management Interface | Description | Type | VRF | IPv6 Address | IPv6 Gateway |
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

Router service-insertion is enabled.

## Network Services Information

| Name | Interface | next_hop_ip_address |
| ---- | --------- | ------------------- |
| connection1 | ethernet2 | 10.10.10.10 |

| Name | Primary Interface | Secondary Interface |
| ---- | ----------------- | ------------------- |
| connection2 | tunnel2 | tunnel3 |
| connection3 | tunnel4 | tunnel5 |

## Router Service-Insertion Configuration

```eos
!
router service-insertion
   connection connection1
      interface ethernet2 next-hop 10.10.10.10
      monitor connectivity host host1
   connection connection2
      interface tunnel2 primary
      interface tunnel3 secondary
      monitor connectivity host host2
   connection connection3
      interface tunnel4 primary
      interface tunnel5 secondary
      monitor connectivity host host3
```
