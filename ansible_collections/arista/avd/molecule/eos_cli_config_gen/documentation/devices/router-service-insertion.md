# router-service-insertion

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [Routing](#routing)
- [Connections](#connections)
  - [Connections Through Ethernet Interface](#connections-through-ethernet-interface)
  - [Connections Through Tunnel Interface](#connections-through-tunnel-interface)
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

## Connections

### Connections Through Ethernet Interface

| Name | Interface | Next Hop | Monitor Connectivity Host |
| ---- | --------- | -------- | ------------------------- |
| connection1 | Ethernet2/2.2 | 10.10.10.10 | host1 |
| connection4 | Ethernet3/1.1 | 10.10.10.10 | host4 |

### Connections Through Tunnel Interface

| Name | Primary Interface | Secondary Interface | Monitor Connectivity Host |
| ---- | ----------------- | ------------------- | ------------------------- |
| connection2 | Tunnel2 | Tunnel3 | host2 |
| connection3 | Tunnel4 | Tunnel5 | host3 |

## Router Service-Insertion Configuration

```eos
!
router service-insertion
   connection connection1
      interface Ethernet2/2.2 next-hop 10.10.10.10
      monitor connectivity host host1
   connection connection2
      interface Tunnel2 primary
      interface Tunnel3 secondary
      monitor connectivity host host2
   connection connection3
      interface Tunnel4 primary
      interface Tunnel5 secondary
      monitor connectivity host host3
   connection connection4
      interface Ethernet3/1.1 next-hop 10.10.10.10
      monitor connectivity host host4
```
