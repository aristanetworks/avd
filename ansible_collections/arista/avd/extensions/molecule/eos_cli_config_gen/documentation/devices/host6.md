# host6

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [Monitoring](#monitoring)
  - [SNMP](#snmp)
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

| Management Interface | Description | Type | VRF | IP Address | Gateway |
| -------------------- | ----------- | ---- | --- | ---------- | ------- |
| Management1 | OOB_MANAGEMENT | oob | MGMT | 10.73.255.122/24 | 10.73.255.2 |

##### IPv6

| Management Interface | Description | Type | VRF | IPv6 Address | IPv6 Gateway | ND RA Disabled | ND RA RX Accept | ND Managed Config Flag | ND Other Config Flag | ND Cache |
| -------------------- | ----------- | ---- | --- | ------------ | ------------ | -------------- | --------------- | ---------------------- | -------------------- | -------- |
| Management1 | OOB_MANAGEMENT | oob | MGMT | - | - | - | - | - | - | - |

#### Management Interfaces Device Configuration

```eos
!
interface Management1
   description OOB_MANAGEMENT
   vrf MGMT
   ip address 10.73.255.122/24
```

## Monitoring

### SNMP

#### SNMP Configuration Summary

| Contact | Location | SNMP Traps | State |
| ------- | -------- | ---------- | ----- |
| - | - | All | Disabled |

#### SNMP Hosts Configuration

| Host | VRF | Community | Username | Authentication level | SNMP Version |
| ---- | --- | --------- | -------- | -------------------- | ------------ |
| 10.6.75.121 | MGMT | SNMP-COMMUNITY-1 | - | - | 1 |
| 10.6.75.121 | MGMT | SNMP-COMMUNITY-2 | - | - | 2c |

#### SNMP Device Configuration

```eos
!
snmp-server host 10.6.75.121 vrf MGMT version 1 SNMP-COMMUNITY-1
snmp-server host 10.6.75.121 vrf MGMT version 2c SNMP-COMMUNITY-2
```

## Routing

### IP Routing

#### IP Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | False |
| MGMT | False |
| TENANT_A | True |
| TENANT_B | True (ipv6 interfaces) |

#### IP Routing Device Configuration

```eos
!
no ip routing vrf MGMT
ip routing vrf TENANT_A
ip routing ipv6 interfaces vrf TENANT_B
```

### IPv6 Routing

#### IPv6 Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | False |
| MGMT | false |
| TENANT_A | false |
| TENANT_B | false |

## VRF Instances

### VRF Instances Summary

| VRF Name | IP Routing |
| -------- | ---------- |
| MGMT | disabled |
| TENANT_A | enabled |
| TENANT_B | enabled (ipv6 interface) |

### VRF Instances Device Configuration

```eos
!
vrf instance MGMT
!
vrf instance TENANT_A
!
vrf instance TENANT_B
```
