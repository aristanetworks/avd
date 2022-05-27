# management-api-models
# Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
  - [Management API Models](#management-api-models)
- [Authentication](#authentication)
- [Monitoring](#monitoring)
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

## Management API Models

### Management API Models Summary

| Provider | Path | Disabled |
| -------- | ---- | ------- |
| smash | flexCounters | False |
| smash | forwarding/srte/status/fec | False |
| smash | routing6/status | False |
| smash | routing/bgp/export/allPeerAdjRibIn | False |
| smash | routing/status | True |
| smash | tunnel/tunnelFib/entry | False |
| sysdb | /Sysdb/sys/logging/config/vrfLoggingHost/mgmt | True |
| sysdb | cell/1/agent | True |

### Management API Models Configuration

```eos
!
management api models
   !
   provider smash
      path flexCounters
      path forwarding/srte/status/fec
      path routing6/status
      path routing/bgp/export/allPeerAdjRibIn
      path routing/status disabled
      path tunnel/tunnelFib/entry
   !
   provider sysdb
      path /Sysdb/sys/logging/config/vrfLoggingHost/mgmt disabled
      path cell/1/agent disabled
```

# Authentication

# Monitoring

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
