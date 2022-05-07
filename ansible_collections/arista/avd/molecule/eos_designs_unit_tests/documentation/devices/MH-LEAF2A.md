# MH-LEAF2A
# Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
  - [Name Servers](#name-servers)
  - [NTP](#ntp)
  - [Management API HTTP](#management-api-http)
- [Authentication](#authentication)
  - [Local Users](#local-users)
- [System Boot Settings](#system-boot-settings)
  - [Boot Secret Summary](#boot-secret-summary)
  - [System Boot Configuration](#system-boot-configuration)
- [Monitoring](#monitoring)
  - [TerminAttr Daemon](#terminattr-daemon)
  - [SNMP](#snmp)
  - [Link Tracking](#link-tracking)
- [LACP](#lacp)
  - [LACP Summary](#lacp-summary)
  - [LACP Device Configuration](#lacp-device-configuration)
- [Internal VLAN Allocation Policy](#internal-vlan-allocation-policy)
  - [Internal VLAN Allocation Policy Summary](#internal-vlan-allocation-policy-summary)
  - [Internal VLAN Allocation Policy Configuration](#internal-vlan-allocation-policy-configuration)
- [VLANs](#vlans)
  - [VLANs Summary](#vlans-summary)
  - [VLANs Device Configuration](#vlans-device-configuration)
- [Interfaces](#interfaces)
  - [Ethernet Interfaces](#ethernet-interfaces)
  - [Port-Channel Interfaces](#port-channel-interfaces)
  - [Loopback Interfaces](#loopback-interfaces)
  - [VLAN Interfaces](#vlan-interfaces)
  - [VXLAN Interface](#vxlan-interface)
- [Routing](#routing)
  - [Service Routing Protocols Model](#service-routing-protocols-model)
  - [Virtual Router MAC Address](#virtual-router-mac-address)
  - [IP Routing](#ip-routing)
  - [IPv6 Routing](#ipv6-routing)
  - [Static Routes](#static-routes)
  - [Router BGP](#router-bgp)
- [BFD](#bfd)
  - [Router BFD](#router-bfd)
- [Multicast](#multicast)
  - [IP IGMP Snooping](#ip-igmp-snooping)
- [Filters](#filters)
  - [Prefix-lists](#prefix-lists)
  - [Route-maps](#route-maps)
- [ACL](#acl)
- [VRF Instances](#vrf-instances)
  - [VRF Instances Summary](#vrf-instances-summary)
  - [VRF Instances Device Configuration](#vrf-instances-device-configuration)
- [Virtual Source NAT](#virtual-source-nat)
  - [Virtual Source NAT Summary](#virtual-source-nat-summary)
  - [Virtual Source NAT Configuration](#virtual-source-nat-configuration)
- [Quality Of Service](#quality-of-service)

# Management

## Management Interfaces

### Management Interfaces Summary

#### IPv4

| Management Interface | description | Type | VRF | IP Address | Gateway |
| -------------------- | ----------- | ---- | --- | ---------- | ------- |
| Management1 | oob_management | oob | MGMT | 192.168.201.106/24 | 192.168.200.5 |

#### IPv6

| Management Interface | description | Type | VRF | IPv6 Address | IPv6 Gateway |
| -------------------- | ----------- | ---- | --- | ------------ | ------------ |
| Management1 | oob_management | oob | MGMT | -  | - |

### Management Interfaces Device Configuration

```eos
!
interface Management1
   description oob_management
   no shutdown
   vrf MGMT
   ip address 192.168.201.106/24
```

## Name Servers

### Name Servers Summary

| Name Server | Source VRF |
| ----------- | ---------- |
| 192.168.200.5 | MGMT |
| 8.8.8.8 | MGMT |

### Name Servers Device Configuration

```eos
ip name-server vrf MGMT 8.8.8.8
ip name-server vrf MGMT 192.168.200.5
```

## NTP

### NTP Summary

#### NTP Local Interface

| Interface | VRF |
| --------- | --- |
| Management1 | MGMT |

#### NTP Servers

| Server | VRF | Preferred | Burst | iBurst | Version | Min Poll | Max Poll | Local-interface | Key |
| ------ | --- | --------- | ----- | ------ | ------- | -------- | -------- | --------------- | --- |
| 192.168.200.5 | MGMT | True | - | - | - | - | - | - | - |

### NTP Device Configuration

```eos
!
ntp local-interface vrf MGMT Management1
ntp server vrf MGMT 192.168.200.5 prefer
```

## Management API HTTP

### Management API HTTP Summary

| HTTP | HTTPS | Default Services |
| ---- | ----- | ---------------- |
| False | True | False |

### Management API VRF Access

| VRF Name | IPv4 ACL | IPv6 ACL |
| -------- | -------- | -------- |
| MGMT | - | - |

### Management API HTTP Configuration

```eos
!
management api http-commands
   protocol https
   no default-services
   no shutdown
   !
   vrf MGMT
      no shutdown
```

# Authentication

## Local Users

### Local Users Summary

| User | Privilege | Role |
| ---- | --------- | ---- |
| admin | 15 | network-admin |
| cvpadmin | 15 | network-admin |

### Local Users Device Configuration

```eos
!
username admin privilege 15 role network-admin nopassword
username cvpadmin privilege 15 role network-admin secret sha512 $6$rZKcbIZ7iWGAWTUM$TCgDn1KcavS0s.OV8lacMTUkxTByfzcGlFlYUWroxYuU7M/9bIodhRO7nXGzMweUxvbk8mJmQl8Bh44cRktUj.
username cvpadmin ssh-key ssh-rsa AAAAB3NzaC1yc2EAA82spi2mkxp4FgaLi4CjWkpnL1A/MD7WhrSNgqXToF7QCb9Lidagy9IHafQxfu7LwkFdyQIMu8XNwDZIycuf29wHbDdz1N+YNVK8zwyNAbMOeKMqblsEm2YIorgjzQX1m9+/rJeFBKz77PSgeMp/Rc3txFVuSmFmeTy3aMkU= cvpadmin@hostmachine.local
```

# System Boot Settings

## Boot Secret Summary

- The sha512 hashed Aboot password is configured

## System Boot Configuration

```eos
!
boot secret sha512 a153de6290ff1409257ade45f
```

# Monitoring

## TerminAttr Daemon

### TerminAttr Daemon Summary

| CV Compression | CloudVision Servers | VRF | Authentication | Smash Excludes | Ingest Exclude | Bypass AAA |
| -------------- | ------------------- | --- | -------------- | -------------- | -------------- | ---------- |
| gzip | 192.168.200.11:9910 | MGMT | key,telarista | ale,flexCounter,hardware,kni,pulse,strata | /Sysdb/cell/1/agent,/Sysdb/cell/2/agent | False |

### TerminAttr Daemon Device Configuration

```eos
!
daemon TerminAttr
   exec /usr/bin/TerminAttr -cvaddr=192.168.200.11:9910 -cvauth=key,telarista -cvvrf=MGMT -smashexcludes=ale,flexCounter,hardware,kni,pulse,strata -ingestexclude=/Sysdb/cell/1/agent,/Sysdb/cell/2/agent -taillogs
   no shutdown
```

## SNMP

### SNMP Configuration Summary

| Contact | Location | SNMP Traps | State |
| ------- | -------- | ---------- | ----- |
| example@example.com | EOS_DESIGNS_UNIT_TESTS MH-LEAF2A | All | Disabled |

### SNMP Device Configuration

```eos
!
snmp-server contact example@example.com
snmp-server location EOS_DESIGNS_UNIT_TESTS MH-LEAF2A
```

## Link Tracking

### Link Tracking Groups Summary

| Group Name | Minimum Links | Recovery Delay |
| ---------- | ------------- | -------------- |
| Eth-conn-to-router | - | 520 |

### Link Tracking Groups Configuration

```eos
!
link tracking group Eth-conn-to-router
   recovery delay 520
```

# LACP

## LACP Summary

| Port-id range | Rate-limit default | System-priority |
| ------------- | ------------------ | --------------- |
| 257 - 768 | - | - |

## LACP Device Configuration

```eos
!
lacp port-id range 257 768
```

# Internal VLAN Allocation Policy

## Internal VLAN Allocation Policy Summary

| Policy Allocation | Range Beginning | Range Ending |
| ------------------| --------------- | ------------ |
| ascending | 1006 | 1199 |

## Internal VLAN Allocation Policy Configuration

```eos
!
vlan internal order ascending range 1006 1199
```

# VLANs

## VLANs Summary

| VLAN ID | Name | Trunk Groups |
| ------- | ---- | ------------ |
| 310 | Tenant_X_OP_Zone_1 | - |
| 311 | Tenant_default_vrf | - |

## VLANs Device Configuration

```eos
!
vlan 310
   name Tenant_X_OP_Zone_1
!
vlan 311
   name Tenant_default_vrf
```

# Interfaces

## Ethernet Interfaces

### Ethernet Interfaces Summary

#### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | Channel-Group |
| --------- | ----------- | ---- | ----- | ----------- | ----------- | ------------- |
| Ethernet2 | MH-L2LEAF1A_Ethernet1 | *trunk | *310 | *- | *- | 2 |
| Ethernet10 |  ROUTER01_Eth1 | access | 310 | - | - | - |

*Inherited from Port-Channel Interface

#### Link Tracking Groups

| Interface | Group Name | Direction |
| --------- | ---------- | --------- |
| Ethernet1 | Eth-conn-to-router | upstream |
| Ethernet10 | Eth-conn-to-router | downstream |

#### IPv4

| Interface | Description | Type | Channel Group | IP Address | VRF |  MTU | Shutdown | ACL In | ACL Out |
| --------- | ----------- | -----| ------------- | ---------- | ----| ---- | -------- | ------ | ------- |
| Ethernet1 | P2P_LINK_TO_DC1-SPINE1_Ethernet12 | routed | - | 10.10.101.5/31 | default | 1500 | false | - | - |

### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet1
   description P2P_LINK_TO_DC1-SPINE1_Ethernet12
   no shutdown
   mtu 1500
   no switchport
   ip address 10.10.101.5/31
   link tracking group Eth-conn-to-router upstream
!
interface Ethernet2
   description MH-L2LEAF1A_Ethernet1
   no shutdown
   channel-group 2 mode active
!
interface Ethernet10
   description ROUTER01_Eth1
   no shutdown
   switchport access vlan 310
   switchport mode access
   switchport
   link tracking group Eth-conn-to-router downstream
```

## Port-Channel Interfaces

### Port-Channel Interfaces Summary

#### L2

| Interface | Description | Type | Mode | VLANs | Native VLAN | Trunk Group | LACP Fallback Timeout | LACP Fallback Mode | MLAG ID | EVPN ESI |
| --------- | ----------- | ---- | ---- | ----- | ----------- | ------------| --------------------- | ------------------ | ------- | -------- |
| Port-Channel2 | MH-L2LEAF1A_Po1 | switched | trunk | 310 | - | - | - | - | - | - |

### Port-Channel Interfaces Device Configuration

```eos
!
interface Port-Channel2
   description MH-L2LEAF1A_Po1
   no shutdown
   switchport
   switchport trunk allowed vlan 310
   switchport mode trunk
```

## Loopback Interfaces

### Loopback Interfaces Summary

#### IPv4

| Interface | Description | VRF | IP Address |
| --------- | ----------- | --- | ---------- |
| Loopback0 | EVPN_Overlay_Peering | default | 192.168.255.35/32 |
| Loopback1 | VTEP_VXLAN_Tunnel_Source | default | 192.168.254.35/32 |
| Loopback100 | Tenant_X_OP_Zone_VTEP_DIAGNOSTICS | Tenant_X_OP_Zone | 10.255.1.35/32 |

#### IPv6

| Interface | Description | VRF | IPv6 Address |
| --------- | ----------- | --- | ------------ |
| Loopback0 | EVPN_Overlay_Peering | default | - |
| Loopback1 | VTEP_VXLAN_Tunnel_Source | default | - |
| Loopback100 | Tenant_X_OP_Zone_VTEP_DIAGNOSTICS | Tenant_X_OP_Zone | - |


### Loopback Interfaces Device Configuration

```eos
!
interface Loopback0
   description EVPN_Overlay_Peering
   no shutdown
   ip address 192.168.255.35/32
!
interface Loopback1
   description VTEP_VXLAN_Tunnel_Source
   no shutdown
   ip address 192.168.254.35/32
!
interface Loopback100
   description Tenant_X_OP_Zone_VTEP_DIAGNOSTICS
   no shutdown
   vrf Tenant_X_OP_Zone
   ip address 10.255.1.35/32
```

## VLAN Interfaces

### VLAN Interfaces Summary

| Interface | Description | VRF |  MTU | Shutdown |
| --------- | ----------- | --- | ---- | -------- |
| Vlan310 | Tenant_X_OP_Zone_1 | Tenant_X_OP_Zone | - | false |
| Vlan311 | Tenant_default_vrf | default | - | false |

#### IPv4

| Interface | VRF | IP Address | IP Address Virtual | IP Router Virtual Address | VRRP | ACL In | ACL Out |
| --------- | --- | ---------- | ------------------ | ------------------------- | ---- | ------ | ------- |
| Vlan310 |  Tenant_X_OP_Zone  |  -  |  10.1.10.1/24  |  -  |  -  |  -  |  -  |
| Vlan311 |  default  |  -  |  10.2.10.1/24  |  -  |  -  |  -  |  -  |

### VLAN Interfaces Device Configuration

```eos
!
interface Vlan310
   description Tenant_X_OP_Zone_1
   no shutdown
   vrf Tenant_X_OP_Zone
   ip address virtual 10.1.10.1/24
!
interface Vlan311
   description Tenant_default_vrf
   no shutdown
   ip address virtual 10.2.10.1/24
```

## VXLAN Interface

### VXLAN Interface Summary

| Setting | Value |
| ------- | ----- |
| Source Interface | Loopback1 |
| UDP port | 4789 |

#### VLAN to VNI, Flood List and Multicast Group Mappings

| VLAN | VNI | Flood List | Multicast Group |
| ---- | --- | ---------- | --------------- |
| 310 | 11310 | - | - |
| 311 | 11311 | - | - |

#### VRF to VNI and Multicast Group Mappings

| VRF | VNI | Multicast Group |
| ---- | --- | --------------- |
| default | 21 | - |
| Tenant_X_OP_Zone | 20 | - |

### VXLAN Interface Device Configuration

```eos
!
interface Vxlan1
   description MH-LEAF2A_VTEP
   vxlan source-interface Loopback1
   vxlan udp-port 4789
   vxlan vlan 310 vni 11310
   vxlan vlan 311 vni 11311
   vxlan vrf default vni 21
   vxlan vrf Tenant_X_OP_Zone vni 20
```

# Routing
## Service Routing Protocols Model

Multi agent routing protocol model enabled

```eos
!
service routing protocols model multi-agent
```

## Virtual Router MAC Address

### Virtual Router MAC Address Summary

#### Virtual Router MAC Address: 00:1c:73:00:dc:01

### Virtual Router MAC Address Configuration

```eos
!
ip virtual-router mac-address 00:1c:73:00:dc:01
```

## IP Routing

### IP Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | true |
| MGMT | false |
| Tenant_X_OP_Zone | true |

### IP Routing Device Configuration

```eos
!
ip routing
no ip routing vrf MGMT
ip routing vrf Tenant_X_OP_Zone
```
## IPv6 Routing

### IPv6 Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | false |
| MGMT | false |
| Tenant_X_OP_Zone | false |

## Static Routes

### Static Routes Summary

| VRF | Destination Prefix | Next Hop IP             | Exit interface      | Administrative Distance       | Tag               | Route Name                    | Metric         |
| --- | ------------------ | ----------------------- | ------------------- | ----------------------------- | ----------------- | ----------------------------- | -------------- |
| MGMT | 0.0.0.0/0 | 192.168.200.5 | - | 1 | - | - | - |

### Static Routes Device Configuration

```eos
!
ip route vrf MGMT 0.0.0.0/0 192.168.200.5
```

## Router BGP

### Router BGP Summary

| BGP AS | Router ID |
| ------ | --------- |
| 65153|  192.168.255.35 |

| BGP Tuning |
| ---------- |
| maximum-paths 4 ecmp 4 |

### Router BGP Peer Groups

#### EVPN-OVERLAY-PEERS

| Settings | Value |
| -------- | ----- |
| Address Family | evpn |
| Source | Loopback0 |
| BFD | True |
| Ebgp multihop | 3 |
| Send community | all |
| Maximum routes | 0 (no limit) |

#### UNDERLAY-PEERS

| Settings | Value |
| -------- | ----- |
| Address Family | ipv4 |
| Send community | all |
| Maximum routes | 12000 |

### BGP Neighbors

| Neighbor | Remote AS | VRF | Shutdown | Send-community | Maximum-routes | Allowas-in | BFD | RIB Pre-Policy Retain |
| -------- | --------- | --- | -------- | -------------- | -------------- | ---------- | --- | --------------------- |
| 10.10.101.4 | 65001 | default | - | Inherited from peer group UNDERLAY-PEERS | Inherited from peer group UNDERLAY-PEERS | - | - | - |
| 192.168.255.1 | 65001 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - |

### Router BGP EVPN Address Family

#### EVPN Peer Groups

| Peer Group | Activate |
| ---------- | -------- |
| EVPN-OVERLAY-PEERS | True |

#### EVPN Host Flapping Settings

| State | Window | Threshold | Expiry Timeout |
| ----- | ------ | --------- | -------------- |
| Enabled | 180 Seconds | 5 | 10 Seconds |

### Router BGP VLAN Aware Bundles

| VLAN Aware Bundle | Route-Distinguisher | Both Route-Target | Import Route Target | Export Route-Target | Redistribute | VLANs |
| ----------------- | ------------------- | ----------------- | ------------------- | ------------------- | ------------ | ----- |
| default | 192.168.255.35:21 | 21:21 | - | - | learned | 311 |
| Tenant_X_OP_Zone | 192.168.255.35:20 | 20:20 | - | - | learned | 310 |

### Router BGP VRFs

| VRF | Route-Distinguisher | Redistribute |
| --- | ------------------- | ------------ |
| default | 192.168.255.35:21 | - |
| Tenant_X_OP_Zone | 192.168.255.35:20 | connected |

### Router BGP Device Configuration

```eos
!
router bgp 65153
   router-id 192.168.255.35
   maximum-paths 4 ecmp 4
   neighbor EVPN-OVERLAY-PEERS peer group
   neighbor EVPN-OVERLAY-PEERS update-source Loopback0
   neighbor EVPN-OVERLAY-PEERS bfd
   neighbor EVPN-OVERLAY-PEERS ebgp-multihop 3
   neighbor EVPN-OVERLAY-PEERS password 7 q+VNViP5i4rVjW1cxFv2wA==
   neighbor EVPN-OVERLAY-PEERS send-community
   neighbor EVPN-OVERLAY-PEERS maximum-routes 0
   neighbor UNDERLAY-PEERS peer group
   neighbor UNDERLAY-PEERS password 7 AQQvKeimxJu+uGQ/yYvv9w==
   neighbor UNDERLAY-PEERS send-community
   neighbor UNDERLAY-PEERS maximum-routes 12000
   neighbor UNDERLAY-PEERS route-map RM-BGP-UNDERLAY-PEERS-OUT out
   neighbor 10.10.101.4 peer group UNDERLAY-PEERS
   neighbor 10.10.101.4 remote-as 65001
   neighbor 10.10.101.4 description DC1-SPINE1_Ethernet12
   neighbor 192.168.255.1 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.255.1 remote-as 65001
   neighbor 192.168.255.1 description DC1-SPINE1
   redistribute connected route-map RM-CONN-2-BGP
   !
   vlan-aware-bundle default
      rd 192.168.255.35:21
      route-target both 21:21
      redistribute learned
      vlan 311
   !
   vlan-aware-bundle Tenant_X_OP_Zone
      rd 192.168.255.35:20
      route-target both 20:20
      redistribute learned
      vlan 310
   !
   address-family evpn
      host-flap detection window 180 threshold 5 expiry timeout 10 seconds
      neighbor EVPN-OVERLAY-PEERS activate
   !
   address-family ipv4
      no neighbor EVPN-OVERLAY-PEERS activate
      neighbor UNDERLAY-PEERS activate
   !
   vrf default
      rd 192.168.255.35:21
      route-target import evpn 21:21
      route-target export evpn 21:21
      route-target export evpn route-map RM-EVPN-EXPORT-VRF-DEFAULT
   !
   vrf Tenant_X_OP_Zone
      rd 192.168.255.35:20
      route-target import evpn 20:20
      route-target export evpn 20:20
      router-id 192.168.255.35
      redistribute connected
```

# BFD

## Router BFD

### Router BFD Multihop Summary

| Interval | Minimum RX | Multiplier |
| -------- | ---------- | ---------- |
| 1200 | 1200 | 3 |

### Router BFD Device Configuration

```eos
!
router bfd
   multihop interval 1200 min-rx 1200 multiplier 3
```

# Multicast

## IP IGMP Snooping

### IP IGMP Snooping Summary

| IGMP Snooping | Fast Leave | Interface Restart Query | Proxy | Restart Query Interval | Robustness Variable |
| ------------- | ---------- | ----------------------- | ----- | ---------------------- | ------------------- |
| Enabled | - | - | - | - | - |

### IP IGMP Snooping Device Configuration

```eos
```

# Filters

## Prefix-lists

### Prefix-lists Summary

#### PL-LOOPBACKS-EVPN-OVERLAY

| Sequence | Action |
| -------- | ------ |
| 10 | permit 192.168.255.0/24 eq 32 |
| 20 | permit 192.168.254.0/24 eq 32 |

#### PL-SVI-VRF-DEFAULT

| Sequence | Action |
| -------- | ------ |
| 10 | permit 10.2.10.0/24 |

### Prefix-lists Device Configuration

```eos
!
ip prefix-list PL-LOOPBACKS-EVPN-OVERLAY
   seq 10 permit 192.168.255.0/24 eq 32
   seq 20 permit 192.168.254.0/24 eq 32
!
ip prefix-list PL-SVI-VRF-DEFAULT
   seq 10 permit 10.2.10.0/24
```

## Route-maps

### Route-maps Summary

#### RM-BGP-UNDERLAY-PEERS-OUT

| Sequence | Type | Match and/or Set |
| -------- | ---- | ---------------- |
| 10 | deny | match ip address prefix-list PL-SVI-VRF-DEFAULT |

#### RM-CONN-2-BGP

| Sequence | Type | Match and/or Set |
| -------- | ---- | ---------------- |
| 10 | permit | match ip address prefix-list PL-LOOPBACKS-EVPN-OVERLAY |
| 30 | permit | match ip address prefix-list PL-SVI-VRF-DEFAULT |

#### RM-EVPN-EXPORT-VRF-DEFAULT

| Sequence | Type | Match and/or Set |
| -------- | ---- | ---------------- |
| 10 | permit | match ip address prefix-list PL-SVI-VRF-DEFAULT |

### Route-maps Device Configuration

```eos
!
route-map RM-BGP-UNDERLAY-PEERS-OUT deny 10
   match ip address prefix-list PL-SVI-VRF-DEFAULT
!
route-map RM-BGP-UNDERLAY-PEERS-OUT permit 20
!
route-map RM-CONN-2-BGP permit 10
   match ip address prefix-list PL-LOOPBACKS-EVPN-OVERLAY
!
route-map RM-CONN-2-BGP permit 30
   match ip address prefix-list PL-SVI-VRF-DEFAULT
!
route-map RM-EVPN-EXPORT-VRF-DEFAULT permit 10
   match ip address prefix-list PL-SVI-VRF-DEFAULT
```

# ACL

# VRF Instances

## VRF Instances Summary

| VRF Name | IP Routing |
| -------- | ---------- |
| MGMT | disabled |
| Tenant_X_OP_Zone | enabled |

## VRF Instances Device Configuration

```eos
!
vrf instance MGMT
!
vrf instance Tenant_X_OP_Zone
```

# Virtual Source NAT

## Virtual Source NAT Summary

| Source NAT VRF | Source NAT IP Address |
| -------------- | --------------------- |
| Tenant_X_OP_Zone | 10.255.1.35 |

## Virtual Source NAT Configuration

```eos
!
ip address virtual source-nat vrf Tenant_X_OP_Zone address 10.255.1.35
```

# Quality Of Service
