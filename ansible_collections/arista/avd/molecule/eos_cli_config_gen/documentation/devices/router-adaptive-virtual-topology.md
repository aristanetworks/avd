# router-adaptive-virtual-topology

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [Routing](#routing)
  - [Router Adaptive Virtual Topology](#router-adaptive-virtual-topology)

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

### Router Adaptive Virtual Topology

#### Router Adaptive Virtual Topology Summary

Topology role: transit region

| Hierarchy | Name | ID |
| --------- | ---- | -- |
| Region | North_America | 1 |
| Zone | Canada | 2 |
| Site | Ottawa | 99 |

#### Router Adaptive Virtual Topology Configuration

```eos
!
router adaptive-virtual-topology
   topology role transit region
   region North_America id 1
   zone Canada id 2
   site Ottawa id 99
```
