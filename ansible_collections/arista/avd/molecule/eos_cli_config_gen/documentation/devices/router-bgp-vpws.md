# router-bgp-vpws
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
  - [Router BGP](#router-bgp)
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

## Router BGP

### Router BGP Summary

| BGP AS | Router ID |
| ------ | --------- |
| 65101|  192.168.255.3 |

| BGP Tuning |
| ---------- |
| no bgp default ipv4-unicast |
| distance bgp 20 200 200 |
| graceful-restart restart-time 300 |
| graceful-restart |
| maximum-paths 2 ecmp 2 |

### Router BGP VPWS Instances

| Instance | Route-Distinguisher | Both Route-Target | MPLS Control Word | Label Flow | MTU | Pseudowire | Local ID | Remote ID |
| -------- | ------------------- | ----------------- | ----------------- | -----------| --- | ---------- | -------- | --------- |
| TENANT_A | 100.70.0.2:1000 | 65000:1000 | True | True | 1600 | TEN_A_site1_site3_pw | 15 | 35 |
| TENANT_A | 100.70.0.2:1000 | 65000:1000 | True | True | 1600 | TEN_A_site2_site5_pw | 25 | 57 |
| TENANT_B | 100.70.0.2:2000 | 65000:2000 | False | False | - | TEN_B_site2_site5_pw | 26 | 58 |

### Router BGP Device Configuration

```eos
!
router bgp 65101
   router-id 192.168.255.3
   no bgp default ipv4-unicast
   distance bgp 20 200 200
   graceful-restart restart-time 300
   graceful-restart
   maximum-paths 2 ecmp 2
   !
   vpws TENANT_A
      rd 100.70.0.2:1000
      route-target import export evpn 65000:1000
      mpls control-word
      label flow
      mtu 1600
      !
      pseudowire TEN_A_site1_site3_pw
         evpn vpws id local 15 remote 35
      !
      pseudowire TEN_A_site2_site5_pw
         evpn vpws id local 25 remote 57
   !
   vpws TENANT_B
      rd 100.70.0.2:2000
      route-target import export evpn 65000:2000
      !
      pseudowire TEN_B_site2_site5_pw
         evpn vpws id local 26 remote 58
```

# Multicast

# Filters

# ACL

# Quality Of Service
