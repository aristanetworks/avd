# monitor-connectivity
# Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [Authentication](#authentication)
- [Monitoring](#monitoring)
- [Monitor Connectivity](#monitor-connectivity)
  - [Global Configuration](#global-configuration)
  - [Vrf Configuration](#vrf-configuration)
  - [Monitor Connectivity Device Configuration](#monitor-connectivity-device-configuration)
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

# Monitor Connectivity

## Global Configuration

### Interface Sets

| Name | Interfaces |
| ---- | ---------- |
| GLOBAL_SET | Ethernet1-4 |
| HOST_SET | Loopback2-4, Loopback10-12 |

### Probing Configuration

| Enabled | Interval | Default Interface Set |
| ------- | -------- | --------------------- |
| True | 5 | GLOBAL_SET |

### Host Parameters

| Host Name | Description | IPv4 Address | Probing Interface Set | URL |
| --------- | ----------- | ------------ | --------------------- | --- |
| server1 | server1_connectivity_monitor | 10.10.10.1 | HOST_SET | https://server1.local.com |

## Vrf Configuration

| Name | Description | Default Interface Set |
| ---- | ----------- | --------------------- |
| red | vrf_connectivity_monitor | VRF_GLOBAL_SET |

### Vrf red Configuration

#### Interface Sets

| Name | Interfaces |
| ---- | ---------- |
| VRF_GLOBAL_SET | Vlan21-24, Vlan29-32 |
| VRF_HOST_SET | Loopback12-14, 19-23 |

#### Host Parameters

| Host Name | Description | IPv4 Address | Probing Interface Set | URL |
| --------- | ----------- | ------------ | --------------------- | --- |
| server2 | server2_connectivity_monitor | 10.10.20.1 | VRF_HOST_SET | https://server2.local.com |

## Monitor Connectivity Device Configuration

```eos
!
monitor connectivity
   interval 5
   no shutdown
   interface set GLOBAL_SET Ethernet1-4
   interface set HOST_SET Loopback2-4, Loopback10-12
   local-interfaces GLOBAL_SET address-only default
   !
   host server1
      description
      server1_connectivity_monitor
      local-interfaces HOST_SET address-only
      ip 10.10.10.1
      url https://server1.local.com
   vrf red
      interface set VRF_GLOBAL_SET Vlan21-24, Vlan29-32
      interface set VRF_HOST_SET Loopback12-14, 19-23
      local-interfaces VRF_GLOBAL_SET address-only default
      description
      vrf_connectivity_monitor
      !
      host server2
         description
         server2_connectivity_monitor
         local-interfaces VRF_HOST_SET address-only
         ip 10.10.20.1
         url https://server2.local.com
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
