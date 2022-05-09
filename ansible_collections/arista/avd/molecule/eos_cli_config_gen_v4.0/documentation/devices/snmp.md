# snmp
# Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [Authentication](#authentication)
- [Monitoring](#monitoring)
  - [SNMP](#snmp)
- [Internal VLAN Allocation Policy](#internal-vlan-allocation-policy)
  - [Internal VLAN Allocation Policy Summary](#internal-vlan-allocation-policy-summary)
- [Interfaces](#interfaces)
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

## SNMP

### SNMP Configuration Summary

| Contact | Location | SNMP Traps | State |
| ------- | -------- | ---------- | ----- |
| DC1_OPS | DC1 | All | Enabled |

### SNMP ACLs
| IP | ACL | VRF |
| -- | --- | --- |
| IPv4 | SNMP-MGMT | MGMT |
| IPv4 | onur | default |
| IPv6 | SNMP-MGMT | MGMT |
| IPv6 | onur_v6 | default |

### SNMP Local Interfaces

| Local Interface | VRF |
| --------------- | --- |
| Management1 | MGMT |
| Loopback0 | default |
| Loopback12 | Tenant_A_APP_Zone |

### SNMP VRF Status

| VRF | Status |
| --- | ------ |
| default | Disabled |
| MGMT | Enabled |

### SNMP Hosts Configuration

| Host | VRF | Community | Username | Authentication level | SNMP Version |
| ---- |---- | --------- | -------- | -------------------- | ------------ |
| 10.6.75.121 | MGMT | SNMP-COMMUNITY-1 | - | - | 1 |
| 10.6.75.121 | MGMT | SNMP-COMMUNITY-2 | - | - | 2c |
| 10.6.75.122 | MGMT | SNMP-COMMUNITY-2 | - | - | 2c |
| 10.6.75.99 | MGMT | - | USER-READ | auth | 3 |
| 10.6.75.99 | MGMT | - | USER-WRITE | auth | 3 |
| 10.6.75.100 | MGMT | - | USER-READ | priv | 3 |

### SNMP Views Configuration

| View | MIB Family Name | Status |
| ---- | --------------- | ------ |
| VW-WRITE | iso | Included |
| VW-READ | iso | Included |

### SNMP Communities

| Community | Access | Access List IPv4 | Access List IPv6 | View |
| --------- | ------ | ---------------- | ---------------- | ---- |
| SNMP-COMMUNITY-1 | ro | onur | - | - |
| SNMP-COMMUNITY-2 | rw | SNMP-MGMT | SNMP-MGMT | VW-READ |
| SNMP-COMMUNITY-3 | ro | - | - | - |

### SNMP Groups Configuration

| Group | SNMP Version | Authentication | Read | Write | Notify |
| ----- | ------------ | -------------- | ---- | ----- | ------ |
| GRP-READ-ONLY | v3 | priv | v3read | - | - |
| GRP-READ-WRITE | v3 | auth | v3read | v3write | - |

### SNMP Users Configuration

| User | Group | Version | Authentication | Privacy | Remote Address | Remote Port | Engine ID |
| ---- | ----- | ------- | -------------- | ------- | -------------- | ----------- | --------- |
| USER-READ | GRP-READ-ONLY | v3 | sha | aes | - | - | - |
| USER-WRITE | GRP-READ-WRITE | v3 | sha | aes | - | - | - |

### SNMP Device Configuration

```eos
!
snmp-server contact DC1_OPS
snmp-server location DC1
snmp-server ipv4 access-list SNMP-MGMT vrf MGMT
snmp-server ipv4 access-list onur
snmp-server ipv6 access-list SNMP-MGMT vrf MGMT
snmp-server ipv6 access-list onur_v6
snmp-server vrf MGMT local-interface Management1
snmp-server local-interface Loopback0
snmp-server vrf Tenant_A_APP_Zone local-interface Loopback12
snmp-server view VW-WRITE iso included
snmp-server view VW-READ iso included
snmp-server community SNMP-COMMUNITY-1 ro onur
snmp-server community SNMP-COMMUNITY-2 view VW-READ rw ipv6 SNMP-MGMT SNMP-MGMT
snmp-server community SNMP-COMMUNITY-3 ro
snmp-server group GRP-READ-ONLY v3 priv read v3read
snmp-server group GRP-READ-WRITE v3 auth read v3read write v3write
snmp-server user USER-READ GRP-READ-ONLY v3 auth sha 7a07246a6e3467909098d01619e076adb4e2fe08 priv aes 7a07246a6e3467909098d01619e076ad
snmp-server user USER-WRITE GRP-READ-WRITE v3 auth sha 7a07246a6e3467909098d01619e076adb4e2fe08 priv aes 7a07246a6e3467909098d01619e076ad
snmp-server host 10.6.75.121 vrf MGMT version 1 SNMP-COMMUNITY-1
snmp-server host 10.6.75.121 vrf MGMT version 2c SNMP-COMMUNITY-2
snmp-server host 10.6.75.122 vrf MGMT version 2c SNMP-COMMUNITY-2
snmp-server host 10.6.75.99 vrf MGMT version 3 auth USER-READ
snmp-server host 10.6.75.99 vrf MGMT version 3 auth USER-WRITE
snmp-server host 10.6.75.100 vrf MGMT version 3 priv USER-READ
snmp-server enable traps
no snmp-server vrf default
snmp-server vrf MGMT
```

# Internal VLAN Allocation Policy

## Internal VLAN Allocation Policy Summary

**Default Allocation Policy**

| Policy Allocation | Range Beginning | Range Ending |
| ------------------| --------------- | ------------ |
| ascending | 1006 | 4094 |

# Interfaces

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
