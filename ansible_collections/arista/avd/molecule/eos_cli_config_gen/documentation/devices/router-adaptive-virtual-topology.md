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

| Settings | Value |
| -------- | ----- |
| Topology Role | transit region |
| Region | North America id 1 |
| Zone Name | Canada |
| Zone ID | 2 |
| Site | Ottawa |
| Site ID | 99 |

#### Router Adaptive Virtual Topology Configuration

```eos
!
router adaptive-virtual-topology
   topology role transit region
   region North America id 1
   zone Canada id 2
   site Ottawa id 99
```
