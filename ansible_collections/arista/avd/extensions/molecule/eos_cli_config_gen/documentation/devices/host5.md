# host5

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [Monitoring](#monitoring)
  - [TerminAttr Daemon](#terminattr-daemon)
- [Routing](#routing)
  - [IP Routing](#ip-routing)
  - [IPv6 Routing](#ipv6-routing)
  - [Router BGP](#router-bgp)
- [Multicast](#multicast)
  - [Router Multicast](#router-multicast)
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

| Management Interface | Description | Type | VRF | IPv6 Address | IPv6 Gateway | ND RA Disabled | ND RA RX Accept | ND Managed Config Flag | ND Other Config Flag | ND Cache | ND RA DNS Servers |
| -------------------- | ----------- | ---- | --- | ------------ | ------------ | -------------- | --------------- | ---------------------- | -------------------- | -------- | ----------------- |
| Management1 | OOB_MANAGEMENT | oob | MGMT | - | - | - | - | - | - | - | - |

#### Management Interfaces Device Configuration

```eos
!
interface Management1
   description OOB_MANAGEMENT
   vrf MGMT
   ip address 10.73.255.122/24
```

## Monitoring

### TerminAttr Daemon

#### TerminAttr Daemon Summary

| CV Compression | CloudVision Servers | VRF | Authentication | Smash Excludes | Ingest Exclude | Bypass AAA |
| -------------- | ------------------- | --- | -------------- | -------------- | -------------- | ---------- |
| gzip | 192.0.2.1:9910,192.0.2.2:9910,192.0.2.3:9910 | mgt | token,/tmp/token | ale,flexCounter,hardware,kni,pulse,strata | /Sysdb/cell/1/agent,/Sysdb/cell/2/agent | False |

#### TerminAttr Daemon Device Configuration

```eos
!
daemon TerminAttr
   exec /usr/bin/TerminAttr -cvaddr=192.0.2.1:9910,192.0.2.2:9910,192.0.2.3:9910 -cvauth=token,/tmp/token -cvvrf=mgt -smashexcludes=ale,flexCounter,hardware,kni,pulse,strata -ingestexclude=/Sysdb/cell/1/agent,/Sysdb/cell/2/agent -taillogs
   no shutdown
```

## Routing

### IP Routing

#### IP Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | False |
| FUTURE_IPV6_INTERFACES | True (ipv6 interfaces) |

#### IP Routing Device Configuration

```eos
!
ip routing ipv6 interfaces vrf FUTURE_IPV6_INTERFACES
```

### IPv6 Routing

#### IPv6 Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | False |
| FUTURE_IPV6_INTERFACES | false |

### Router BGP

ASN Notation: asplain

#### Router BGP Summary

| BGP AS | Router ID |
| ------ | --------- |
| 65005 | 192.0.2.5 |

| BGP Tuning |
| ---------- |
| bgp additional-paths send backup |

#### BGP Neighbors

| Neighbor | Remote AS | VRF | Shutdown | Send-community | Maximum-routes | Allowas-in | BFD | RIB Pre-Policy Retain | Route-Reflector Client | Passive | TTL Max Hops |
| -------- | --------- | --- | -------- | -------------- | -------------- | ---------- | --- | --------------------- | ---------------------- | ------- | ------------ |
| 192.0.2.1 | 65001 | default | - | - | - | - | - | - | - | - | - |

#### Router BGP EVPN Address Family

- Next-hop-unchanged is explicitly configured (default behaviour)
- Next-hop MPLS resolution Primary-RIB : tunnel-rib host5-rib

#### Router BGP Device Configuration

```eos
!
router bgp 65005
   router-id 192.0.2.5
   bgp additional-paths send backup
   neighbor 192.0.2.1 remote-as 65001
   !
   address-family evpn
      bgp next-hop-unchanged
      next-hop mpls resolution ribs tunnel-rib host5-rib
```

## Multicast

### Router Multicast

#### IP Router Multicast Summary

- IPv6 software forwarding is handled by the Linux kernel.

#### Router Multicast Device Configuration

```eos
!
router multicast
   !
   ipv6
      software-forwarding kernel
```

## VRF Instances

### VRF Instances Summary

| VRF Name | IP Routing |
| -------- | ---------- |
| FUTURE_IPV6_INTERFACES | enabled (ipv6 interface) |

### VRF Instances Device Configuration

```eos
!
vrf instance FUTURE_IPV6_INTERFACES
```
