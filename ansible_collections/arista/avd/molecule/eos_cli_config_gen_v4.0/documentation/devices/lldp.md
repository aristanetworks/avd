# lldp
# Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [Authentication](#authentication)
- [Monitoring](#monitoring)
- [LLDP](#lldp)
  - [LLDP Summary](#lldp-summary)
  - [LLDP Device Configuration](#lldp-device-configuration)
- [Internal VLAN Allocation Policy](#internal-vlan-allocation-policy)
  - [Internal VLAN Allocation Policy Summary](#internal-vlan-allocation-policy-summary)
- [Interfaces](#interfaces)
  - [Ethernet Interfaces](#ethernet-interfaces)
- [Routing](#routing)
  - [IP Routing](#ip-routing)
  - [IPv6 Routing](#ipv6-routing)
- [Multicast](#multicast)
- [Filters](#filters)
- [ACL](#acl)
- [Quality Of Service](#quality-of-service)

# Management

## Management Interfaces

### Management Interfaces Summary

#### IPv4

| Management Interface | description | Type | VRF | IP Address | Gateway |
| -------------------- | ----------- | ---- | --- | ---------- | ------- |
| Management1 | oob_management | oob | MGMT | 10.73.255.122/24 | 10.73.255.2 |

#### IPv6

| Management Interface | description | Type | VRF | IPv6 Address | IPv6 Gateway |
| -------------------- | ----------- | ---- | --- | ------------ | ------------ |
| Management1 | oob_management | oob | MGMT | -  | - |

### Management Interfaces Device Configuration

```eos
!
interface Management1
   description oob_management
   vrf MGMT
   ip address 10.73.255.122/24
```

# Authentication

# Monitoring

# LLDP

## LLDP Summary

### LLDP Global Settings

| Enabled | Management Address | Management VRF | Timer | Hold-Time | Re-initialization Timer | Drop Received Tagged Packets |
| ------- | ------------------ | -------------- | ----- | --------- | ----------------------- | ---------------------------- |
| False | 192.168.1.1/24 | Management | 30 | 90 | 2 | - |

### LLDP Explicit TLV Transmit Settings

| TLV | Transmit |
| --- | -------- |
| system-capabilities | False |
| system-description | True |

### LLDP Interface Settings

LLDP is **disabled** globally. Local interface configs will not apply.

| Interface | Transmit | Receive |
| --------- | -------- | ------- |
| Ethernet1 | False | False |
| Ethernet2 | False | True |
| Ethernet4 | True | False |

## LLDP Device Configuration

```eos
!
no lldp run
lldp timer 30
lldp hold-time 90
lldp management-address 192.168.1.1/24
lldp management-address vrf Management
no lldp tlv transmit system-capabilities
lldp tlv transmit system-description
```

# Internal VLAN Allocation Policy

## Internal VLAN Allocation Policy Summary

**Default Allocation Policy**

| Policy Allocation | Range Beginning | Range Ending |
| ------------------| --------------- | ------------ |
| ascending | 1006 | 4094 |

# Interfaces

## Ethernet Interfaces

### Ethernet Interfaces Summary

#### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | Channel-Group |
| --------- | ----------- | ---- | ----- | ----------- | ----------- | ------------- |
| Ethernet2 |  Switched port with no LLDP rx/tx | access | 110 | - | - | - |
| Ethernet3 |  No special LLDP settings | access | 110 | - | - | - |

*Inherited from Port-Channel Interface

### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet1
   description to WAN-ISP1-01 Ethernet2
   no switchport
   no lldp transmit
   no lldp receive
!
interface Ethernet2
   description Switched port with no LLDP rx/tx
   switchport access vlan 110
   switchport mode access
   switchport
   no lldp transmit
!
interface Ethernet3
   description No special LLDP settings
   switchport access vlan 110
   switchport mode access
   switchport
!
interface Ethernet4
   description test
   no switchport
   no lldp receive
```

# Routing

## IP Routing

### IP Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | false |

### IP Routing Device Configuration

```eos
```
## IPv6 Routing

### IPv6 Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | false |

# Multicast

# Filters

# ACL

# Quality Of Service
