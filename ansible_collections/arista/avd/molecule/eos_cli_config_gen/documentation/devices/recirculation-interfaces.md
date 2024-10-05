# recirculation-interfaces

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [Interfaces](#interfaces)
  - [Recirculation Interfaces](#recirculation-interfaces-1)

## Management

### Management Interfaces

#### Management Interfaces Summary

##### IPv4

| Management Interface | Description | Type | VRF | IP Address | Gateway |
| -------------------- | ----------- | ---- | --- | ---------- | ------- |
| Management1 | OOB_MANAGEMENT | oob | MGMT | 10.73.255.122/24 | 10.73.255.2 |

##### IPv6

| Management Interface | Description | Type | VRF | IPv6 Address | IPv6 Gateway |
| -------------------- | ----------- | ---- | --- | ------------ | ------------ |
| Management1 | OOB_MANAGEMENT | oob | MGMT | - | - |

#### Management Interfaces Device Configuration

```eos
!
interface Management1
   description OOB_MANAGEMENT
   vrf MGMT
   ip address 10.73.255.122/24
```

## Interfaces

### Recirculation Interfaces

#### Recirculation Interfaces Summary

| Interface | Description | Shutdown | Recirculation Features |
| --------- | ----------- | -------- | --------------- |
| Recirc-Channel1 | Test recirculation interface | - | cpu-mirror |
| Recirc-Channel2 | Test recirculation interface with shutdown | True | vxlan |

#### Recirculation Interfaces Device Configuration

```eos
!
interface Recirc-Channel1
   description Test recirculation interface
   switchport recirculation features cpu-mirror
   comment
   Comment created from eos_cli under recirculation_interfaces.Recirc-Channel1
   EOF

!
interface Recirc-Channel2
   description Test recirculation interface with shutdown
   shutdown
   switchport recirculation features vxlan
```
