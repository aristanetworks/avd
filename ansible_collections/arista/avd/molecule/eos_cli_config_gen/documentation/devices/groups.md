# groups
# Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
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
- [Maintenance Mode](#maintenance-mode)
  - [BGP Groups](#bgp-groups)
  - [Interface Groups](#interface-groups)

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

# Maintenance Mode

## BGP Groups

### BGP Groups Summary

| BGP group | VRF Name | Neighbors | BGP maintenance profiles |
| --------- | -------- | --------- | ------------------------ |
| bar | red | peer-group-baz | downlink-neighbors |
| foo | - | 169.254.1.1<br>fe80::1 | ixp<br>uplink-neighbors |

### BGP Groups Configuration

```eos
!
group bgp bar
   vrf red
   neighbor peer-group-baz
   maintenance profile bgp downlink-neighbors
!
group bgp foo
   neighbor 169.254.1.1
   neighbor fe80::1
   maintenance profile bgp ixp
   maintenance profile bgp uplink-neighbors
```

## Interface Groups

### Interface Groups Summary

| Interface Group | Interfaces | Interface maintenance profile | BGP maintenance profiles |
| --------------- | ---------- | ----------------------------- | ------------------------ |
| QSFP_Interface_Group | Ethernet1,5 | uplink-interfaces | Default |
| SFP_Interface_Group | Ethernet10-20<br>Ethernet30-48 | downlink-interfaces<br>ix-interfaces | downlink-neighbors<br>local-ix |

### Interface Groups Configuration

```eos
!
group interface QSFP_Interface_Group
   interface Ethernet1,5
   maintenance profile interface uplink-interfaces
!
group interface SFP_Interface_Group
   interface Ethernet10-20
   interface Ethernet30-48
   maintenance profile interface downlink-interfaces
   maintenance profile interface ix-interfaces
   maintenance profile bgp downlink-neighbors
   maintenance profile bgp local-ix
```
