# tap-aggregation
# Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [Authentication](#authentication)
- [Monitoring](#monitoring)
  - [Tap Aggregation](#tap-aggregation)
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

## Tap Aggregation

### Tap Aggregation Summary

| Settings | Values |
| -------- | ------ |
| Mode Exclusive | True |
| Mode Exclusive Profile | tap-aggregation-extended |
| Mode Exclusive No-Errdisable | Ethernet1/1, Ethetnet 42/1, Port-Channel200 |
| Encapsulation Dot1br Strip | True |
| Encapsulation Vn Tag Strip | True |
| Protocol LLDP Trap | True |
| Truncation Size | 169 |
| Mac Timestamp | Header Format 64-bit |
| Mac Timestamp | Header eth-type 5 |
| Mac FCS Error | pass-through |

### Tap Aggregation Configuration

```eos
!
tap aggregation
   mode exclusive profile tap-aggregation-extended
   mode exclusive no-errdisable Ethernet1/1
   mode exclusive no-errdisable Ethetnet 42/1
   mode exclusive no-errdisable Port-Channel200
   encapsulation dot1br strip
   encapsulation vn-tag strip
   protocol lldp trap
   truncation size 169
   mac timestamp header format 64-bit
   mac timestamp header eth-type 5
   mac fcs-error pass-through
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
