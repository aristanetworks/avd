# host4

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [Monitoring](#monitoring)
  - [TerminAttr Daemon](#terminattr-daemon)
- [Routing](#routing)
  - [Router OSPF](#router-ospf)
  - [Router ISIS](#router-isis)
  - [Router BGP](#router-bgp)
- [MPLS](#mpls)
  - [MPLS and LDP](#mpls-and-ldp)
  - [MPLS Device Configuration](#mpls-device-configuration)
- [Multicast](#multicast)
  - [Router Multicast](#router-multicast)

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

### TerminAttr Daemon

#### TerminAttr Daemon Summary

| CV Compression | CloudVision Servers | VRF | Authentication | Smash Excludes | Ingest Exclude | Bypass AAA |
| -------------- | ------------------- | --- | -------------- | -------------- | -------------- | ---------- |
| gzip | 10.10.10.8:9910,10.10.10.9:9910,10.10.10.10:9910 | mgt | certs,/persist/secure/ssl/terminattr/primary/certs/client.crt,/persist/secure/ssl/terminattr/primary/keys/client.key,/persist/secure/ssl/terminattr/primary/certs/ca.crt | ale,flexCounter,hardware,kni,pulse,strata | /Sysdb/cell/1/agent,/Sysdb/cell/2/agent | True |

#### TerminAttr Daemon Device Configuration

```eos
!
daemon TerminAttr
   exec /usr/bin/TerminAttr -cvaddr=10.10.10.8:9910,10.10.10.9:9910,10.10.10.10:9910 -cvauth=certs,/persist/secure/ssl/terminattr/primary/certs/client.crt,/persist/secure/ssl/terminattr/primary/keys/client.key,/persist/secure/ssl/terminattr/primary/certs/ca.crt -cvvrf=mgt -disableaaa -smashexcludes=ale,flexCounter,hardware,kni,pulse,strata -ingestexclude=/Sysdb/cell/1/agent,/Sysdb/cell/2/agent -taillogs
   no shutdown
```

## Routing

### Router OSPF

#### Router OSPF Summary

| Process ID | Router ID | Default Passive Interface | No Passive Interface | BFD | Max LSA | Default Information Originate | Log Adjacency Changes Detail | Auto Cost Reference Bandwidth | Maximum Paths | MPLS LDP Sync Default | Distribute List In |
| ---------- | --------- | ------------------------- | -------------------- | --- | ------- | ----------------------------- | ---------------------------- | ----------------------------- | ------------- | --------------------- | ------------------ |
| 703 | 10.255.0.4 | disabled | - | disabled | default | disabled | disabled | - | - | - | - |

#### Router OSPF Device Configuration

```eos
!
router ospf 703
   router-id 10.255.0.4
```

### Router ISIS

#### Router ISIS Summary

| Settings | Value |
| -------- | ----- |
| Instance | EVPN_UNDERLAY |

#### ISIS Interfaces Summary

| Interface | ISIS Instance | ISIS Metric | Interface Mode |
| --------- | ------------- | ----------- | -------------- |

#### Router ISIS Device Configuration

```eos
!
router isis EVPN_UNDERLAY
   authentication mode sha key-id 4 rx-disabled
   !
```

### Router BGP

ASN Notation: asplain

#### Router BGP Summary

| BGP AS | Router ID |
| ------ | --------- |
| 65001 | 192.168.255.3 |

| BGP Tuning |
| ---------- |
| graceful-restart-helper long-lived |
| bgp additional-paths send ecmp |

#### Router BGP IPv4 Labeled Unicast

##### General Settings

| Settings | Value |
| -------- | ----- |

##### BGP LU RIB

| RIB | Enabled | Route-map |
| --- | ------- | --------- |
| Tunnel | True | RM-rib3 |

#### Router BGP Device Configuration

```eos
!
router bgp 65001
   bgp labeled-unicast rib tunnel route-map RM-rib3
   router-id 192.168.255.3
   graceful-restart-helper long-lived
   bgp additional-paths send ecmp
   !
   address-family ipv4
      bgp additional-paths send ecmp
   !
   address-family ipv4 labeled-unicast
      bgp additional-paths send limit 10
   !
   address-family ipv6
      bgp additional-paths send limit 20
```

## MPLS

### MPLS and LDP

#### MPLS and LDP Summary

| Setting | Value |
| -------- | ---- |
| MPLS IP Enabled | - |
| LDP Enabled | False |
| LDP Router ID | - |
| LDP Interface Disabled Default | - |
| LDP Transport-Address Interface | - |

### MPLS Device Configuration

```eos
!
mpls rsvp
```

## Multicast

### Router Multicast

#### IP Router Multicast Summary

- Multipathing disabled.

#### Router Multicast Device Configuration

```eos
!
router multicast
   ipv4
      multipath none
```
