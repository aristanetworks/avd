# maintenance
# Table of Contents
<!-- toc -->

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
- [Maintenance](#maintenance)
  - [Maintenance](#maintenance-1)

<!-- toc -->
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
| default | false|
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

# Maintenance

## Maintenance

### Interface groups
| Interface group | Interface | BGP maintenance profiles | Interface maintenance Profiles |
|-----------------|-----------|--------------------------|--------------------------------|
| INTERFACE_GROUP_1| Ethernet10-11|  BP1, BP2|  IP1 |
| INTERFACE_GROUP_2| Ethernet10-11,Vlan10,100| -| - |
| INTERFACE_GROUP_3| Ethernet10,PortChannel10-11,17| -| - |
### Interface groups configuration
```eos
!
group interface INTERFACE_GROUP_1
   interface Ethernet10-11
   maintenance profile bgp BP1
   maintenance profile bgp BP2
   maintenance profile interface IP1
   exit
!
group interface INTERFACE_GROUP_2
   interface Ethernet10-11
   interface Vlan10,100
   exit
!
group interface INTERFACE_GROUP_3
   interface Ethernet10
   interface PortChannel10-11,17
   exit
```

### BGP groups
| BGP group | VRF | Neighbors | BGP maintenance profiles |
|-----------|-----|-----------|--------------------------|
| BGP_GROUP_1| default| 1.1.1.1, TEST-PEER_GROUP| - |
| BGP_GROUP_2| MGMT| 2.2.2.2| - |
### BGP groups configuration
```eos
!
group bgp BGP_GROUP_1
   neighbor 1.1.1.1
   neighbor TEST-PEER_GROUP
   exit
!
group bgp BGP_GROUP_2
   vrf MGMT
   neighbor 2.2.2.2
   exit
```

### Maintenance defaults

Default maintenance bgp profile: **BP1**

Default maintenance interface profile: **IP1**

Default maintenance unit profile: **IP1**

### Maintenance profiles

| BGP profile | Initiator route-map
| -------- | ----- |
| BP1 | RM-MAINTENANCE |
| BP2 | RM-MAINTENANCE2 |
| BP3 | RM-MAINTENANCE3 |

| Interface profile | Rate monitoring load interval | Rate monitoring threshold in/out |
|-------------------|-------------------------------|------------------|
| IP1| 10| 500 |

| Unit profile | on-boot duration |
| -------- | ----- |
| UP1 |900 |
| UP2 |600 |

### Maintenance units

| Unit | Interface groups | BGP groups | Unit profile | Quiesce |
|------|------------------|------------|--------------|---------|
| UNIT1| INTERFACE_GROUP_1| BGP_GROUP_1, BGP_GROUP_2| UP1|  No  |

### Maintenance configuration

```eos
!
maintenance
   profile bgp BP1
      initiator route-map RM-MAINTENANCE inout
   !
   profile bgp BP2
      initiator route-map RM-MAINTENANCE2 inout
   !
   profile bgp BP3
      initiator route-map RM-MAINTENANCE3 inout
   profile bgp BP1 default
   profile interface IP1 default
   profile unit IP1 default
   !
   profile interface IP1
      rate-monitoring load-interval 10
      rate-monitoring threshold 500
   !
   profile unit UP1
      on-boot duration 900
   !
   profile unit UP2
      on-boot duration 600
   !
   unit UNIT1
      group bgp BGP_GROUP_1
      group bgp BGP_GROUP_2
      group interface INTERFACE_GROUP_1
      profile unit UP1
```
