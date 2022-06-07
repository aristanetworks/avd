# DC1-LEAF1A
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
- [Spanning Tree](#spanning-tree)
  - [Spanning Tree Summary](#spanning-tree-summary)
  - [Spanning Tree Device Configuration](#spanning-tree-device-configuration)
- [Internal VLAN Allocation Policy](#internal-vlan-allocation-policy)
  - [Internal VLAN Allocation Policy Summary](#internal-vlan-allocation-policy-summary)
  - [Internal VLAN Allocation Policy Configuration](#internal-vlan-allocation-policy-configuration)
- [VLANs](#vlans)
  - [VLANs Summary](#vlans-summary)
  - [VLANs Device Configuration](#vlans-device-configuration)
- [Interfaces](#interfaces)
  - [Ethernet Interfaces](#ethernet-interfaces)
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
- [Quality Of Service](#quality-of-service)

# Management

## Management Interfaces

### Management Interfaces Summary

#### IPv4

| Management Interface | description | Type | VRF | IP Address | Gateway |
| -------------------- | ----------- | ---- | --- | ---------- | ------- |
| Management1 | oob_management | oob | MGMT | 192.168.200.105/24 | 192.168.200.5 |

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
   ip address 192.168.200.105/24
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
| example@example.com | EOS_DESIGNS_UNIT_TESTS rackA DC1-LEAF1A | All | Disabled |

### SNMP Device Configuration

```eos
!
snmp-server contact example@example.com
snmp-server location EOS_DESIGNS_UNIT_TESTS rackA DC1-LEAF1A
```

# Spanning Tree

## Spanning Tree Summary

STP mode: **mstp**

STP Root Super: **True**

### MSTP Instance and Priority

| Instance(s) | Priority |
| -------- | -------- |
| 0 | 4096 |

## Spanning Tree Device Configuration

```eos
!
spanning-tree root super
spanning-tree mode mstp
spanning-tree mst 0 priority 4096
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
| 120 | Tenant_A_WEB_Zone_1 | - |
| 121 | Tenant_A_WEBZone_2 | - |
| 130 | Tenant_A_APP_Zone_1 | - |
| 131 | Tenant_A_APP_Zone_2 | - |
| 132 | Tenant_A_APP_Zone_3 | - |
| 450 | Tenant_D_v6_WAN_Zone_1 | - |
| 451 | Tenant_D_v6_WAN_Zone_2 | - |
| 452 | Tenant_D_v6_WAN_Zone_3 | - |

## VLANs Device Configuration

```eos
!
vlan 120
   name Tenant_A_WEB_Zone_1
!
vlan 121
   name Tenant_A_WEBZone_2
!
vlan 130
   name Tenant_A_APP_Zone_1
!
vlan 131
   name Tenant_A_APP_Zone_2
!
vlan 132
   name Tenant_A_APP_Zone_3
!
vlan 450
   name Tenant_D_v6_WAN_Zone_1
!
vlan 451
   name Tenant_D_v6_WAN_Zone_2
!
vlan 452
   name Tenant_D_v6_WAN_Zone_3
```

# Interfaces

## Ethernet Interfaces

### Ethernet Interfaces Summary

#### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | Channel-Group |
| --------- | ----------- | ---- | ----- | ----------- | ----------- | ------------- |
| Ethernet6 |  server02_SINGLE_NODE_TRUNK_Eth1 | trunk | 1-4094 | - | - | - |
| Ethernet7 |  server02_SINGLE_NODE_Eth1 | access | 110 | - | - | - |

*Inherited from Port-Channel Interface

#### IPv4

| Interface | Description | Type | Channel Group | IP Address | VRF |  MTU | Shutdown | ACL In | ACL Out |
| --------- | ----------- | -----| ------------- | ---------- | ----| ---- | -------- | ------ | ------- |
| Ethernet1 | P2P_LINK_TO_DC1-SPINE1_Ethernet1 | routed | - | 172.31.255.1/31 | default | 1500 | false | - | - |
| Ethernet2 | P2P_LINK_TO_DC1-SPINE2_Ethernet1 | routed | - | 172.31.255.3/31 | default | 1500 | false | - | - |
| Ethernet3 | P2P_LINK_TO_DC1-SPINE3_Ethernet1 | routed | - | 172.31.255.5/31 | default | 1500 | false | - | - |
| Ethernet4 | P2P_LINK_TO_DC1-SPINE4_Ethernet1 | routed | - | 172.31.255.7/31 | default | 1500 | false | - | - |

### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet1
   description P2P_LINK_TO_DC1-SPINE1_Ethernet1
   no shutdown
   mtu 1500
   speed forced 100gfull
   no switchport
   ip address 172.31.255.1/31
!
interface Ethernet2
   description P2P_LINK_TO_DC1-SPINE2_Ethernet1
   no shutdown
   mtu 1500
   speed forced 100gfull
   no switchport
   ip address 172.31.255.3/31
!
interface Ethernet3
   description P2P_LINK_TO_DC1-SPINE3_Ethernet1
   no shutdown
   mtu 1500
   speed forced 100gfull
   no switchport
   ip address 172.31.255.5/31
!
interface Ethernet4
   description P2P_LINK_TO_DC1-SPINE4_Ethernet1
   no shutdown
   mtu 1500
   speed forced 100gfull
   no switchport
   ip address 172.31.255.7/31
!
interface Ethernet6
   description server02_SINGLE_NODE_TRUNK_Eth1
   no shutdown
   l2 mtu 8000
   switchport trunk allowed vlan 1-4094
   switchport mode trunk
   switchport
   storm-control all level 10
   storm-control broadcast level pps 100
   storm-control multicast level 1
   storm-control unknown-unicast level 2
   spanning-tree portfast
!
interface Ethernet7
   description server02_SINGLE_NODE_Eth1
   no shutdown
   switchport access vlan 110
   switchport mode access
   switchport
```

## Loopback Interfaces

### Loopback Interfaces Summary

#### IPv4

| Interface | Description | VRF | IP Address |
| --------- | ----------- | --- | ---------- |
| Loopback0 | EVPN_Overlay_Peering | default | 192.168.255.9/32 |
| Loopback1 | VTEP_VXLAN_Tunnel_Source | default | 192.168.254.9/32 |

#### IPv6

| Interface | Description | VRF | IPv6 Address |
| --------- | ----------- | --- | ------------ |
| Loopback0 | EVPN_Overlay_Peering | default | - |
| Loopback1 | VTEP_VXLAN_Tunnel_Source | default | - |


### Loopback Interfaces Device Configuration

```eos
!
interface Loopback0
   description EVPN_Overlay_Peering
   no shutdown
   ip address 192.168.255.9/32
!
interface Loopback1
   description VTEP_VXLAN_Tunnel_Source
   no shutdown
   ip address 192.168.254.9/32
```

## VLAN Interfaces

### VLAN Interfaces Summary

| Interface | Description | VRF |  MTU | Shutdown |
| --------- | ----------- | --- | ---- | -------- |
| Vlan120 | Tenant_A_WEB_Zone_1 | Tenant_A_WEB_Zone | - | false |
| Vlan121 | Tenant_A_WEBZone_2 | Tenant_A_WEB_Zone | 1560 | true |
| Vlan130 | Tenant_A_APP_Zone_1 | Tenant_A_APP_Zone | - | false |
| Vlan131 | Tenant_A_APP_Zone_2 | Tenant_A_APP_Zone | - | false |
| Vlan132 | Tenant_A_APP_Zone_3 | Tenant_A_APP_Zone | - | false |
| Vlan450 | Tenant_D_v6_WAN_Zone_1 | Tenant_D_WAN_Zone | - | false |
| Vlan451 | Tenant_D_v6_WAN_Zone_2 | Tenant_D_WAN_Zone | 1560 | false |
| Vlan452 | Tenant_D_v6_WAN_Zone_3 | Tenant_D_WAN_Zone | 1560 | false |

#### IPv4

| Interface | VRF | IP Address | IP Address Virtual | IP Router Virtual Address | VRRP | ACL In | ACL Out |
| --------- | --- | ---------- | ------------------ | ------------------------- | ---- | ------ | ------- |
| Vlan120 |  Tenant_A_WEB_Zone  |  -  |  10.1.20.1/24  |  -  |  -  |  -  |  -  |
| Vlan121 |  Tenant_A_WEB_Zone  |  -  |  10.1.10.254/24  |  -  |  -  |  -  |  -  |
| Vlan130 |  Tenant_A_APP_Zone  |  -  |  10.1.30.1/24  |  -  |  -  |  -  |  -  |
| Vlan131 |  Tenant_A_APP_Zone  |  -  |  10.1.31.1/24  |  -  |  -  |  -  |  -  |
| Vlan132 |  Tenant_A_APP_Zone  |  10.1.32.1/24  |  -  |  10.1.32.254, 10.2.32.254/24, 10.3.32.254/24  |  -  |  -  |  -  |
| Vlan450 |  Tenant_D_WAN_Zone  |  -  |  -  |  -  |  -  |  -  |  -  |
| Vlan451 |  Tenant_D_WAN_Zone  |  -  |  -  |  -  |  -  |  -  |  -  |
| Vlan452 |  Tenant_D_WAN_Zone  |  -  |  10.4.12.254/24  |  -  |  -  |  -  |  -  |

#### IPv6

| Interface | VRF | IPv6 Address | IPv6 Virtual Address | Virtual Router Address | VRRP | ND RA Disabled | Managed Config Flag | IPv6 ACL In | IPv6 ACL Out |
| --------- | --- | ------------ | -------------------- | ---------------------- | ---- | -------------- | ------------------- | ----------- | ------------ |
| Vlan450 | Tenant_D_WAN_Zone | - | 2001:db8:355::1/64 | - | - | - | - | - | - |
| Vlan451 | Tenant_D_WAN_Zone | - | 2001:db8:451::1/64 | - | - | - | - | - | - |
| Vlan452 | Tenant_D_WAN_Zone | - | 2001:db8:412::1/64 | - | - | - | - | - | - |

### VLAN Interfaces Device Configuration

```eos
!
interface Vlan120
   description Tenant_A_WEB_Zone_1
   no shutdown
   vrf Tenant_A_WEB_Zone
   ip helper-address 1.1.1.1 vrf TEST source-interface lo100
   ip address virtual 10.1.20.1/24
   ip address virtual 10.2.20.1/24 secondary
   ip address virtual 10.2.21.1/24 secondary
!
interface Vlan121
   description Tenant_A_WEBZone_2
   shutdown
   mtu 1560
   vrf Tenant_A_WEB_Zone
   ip address virtual 10.1.10.254/24
!
interface Vlan130
   description Tenant_A_APP_Zone_1
   no shutdown
   vrf Tenant_A_APP_Zone
   ip address virtual 10.1.30.1/24
!
interface Vlan131
   description Tenant_A_APP_Zone_2
   no shutdown
   vrf Tenant_A_APP_Zone
   ip address virtual 10.1.31.1/24
!
interface Vlan132
   description Tenant_A_APP_Zone_3
   no shutdown
   vrf Tenant_A_APP_Zone
   ip address 10.1.32.1/24
   ip virtual-router address 10.1.32.254
   ip virtual-router address 10.2.32.254/24
   ip virtual-router address 10.3.32.254/24
!
interface Vlan450
   description Tenant_D_v6_WAN_Zone_1
   no shutdown
   vrf Tenant_D_WAN_Zone
   ipv6 address virtual 2001:db8:355::1/64
!
interface Vlan451
   description Tenant_D_v6_WAN_Zone_2
   no shutdown
   mtu 1560
   vrf Tenant_D_WAN_Zone
   ipv6 address virtual 2001:db8:451::1/64
!
interface Vlan452
   description Tenant_D_v6_WAN_Zone_3
   no shutdown
   mtu 1560
   vrf Tenant_D_WAN_Zone
   ipv6 address virtual 2001:db8:412::1/64
   ip address virtual 10.4.12.254/24
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
| 120 | 10120 | - | - |
| 121 | 10121 | - | - |
| 130 | 10130 | - | - |
| 131 | 10131 | - | - |
| 132 | 10132 | - | - |
| 450 | 40450 | - | - |
| 451 | 40451 | - | - |
| 452 | 40452 | - | - |

#### VRF to VNI and Multicast Group Mappings

| VRF | VNI | Multicast Group |
| ---- | --- | --------------- |
| Tenant_A_APP_Zone | 12 | - |
| Tenant_A_WEB_Zone | 11 | - |
| Tenant_D_WAN_Zone | 41 | - |

### VXLAN Interface Device Configuration

```eos
!
interface Vxlan1
   description DC1-LEAF1A_VTEP
   vxlan source-interface Loopback1
   vxlan udp-port 4789
   vxlan vlan 120 vni 10120
   vxlan vlan 121 vni 10121
   vxlan vlan 130 vni 10130
   vxlan vlan 131 vni 10131
   vxlan vlan 132 vni 10132
   vxlan vlan 450 vni 40450
   vxlan vlan 451 vni 40451
   vxlan vlan 452 vni 40452
   vxlan vrf Tenant_A_APP_Zone vni 12
   vxlan vrf Tenant_A_WEB_Zone vni 11
   vxlan vrf Tenant_D_WAN_Zone vni 41
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

#### Virtual Router MAC Address: 00:dc:00:00:00:0a

### Virtual Router MAC Address Configuration

```eos
!
ip virtual-router mac-address 00:dc:00:00:00:0a
```

## IP Routing

### IP Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | true |
| MGMT | false |
| Tenant_A_APP_Zone | true |
| Tenant_A_WEB_Zone | true |
| Tenant_D_WAN_Zone | true |

### IP Routing Device Configuration

```eos
!
ip routing
no ip routing vrf MGMT
ip routing vrf Tenant_A_APP_Zone
ip routing vrf Tenant_A_WEB_Zone
ip routing vrf Tenant_D_WAN_Zone
```
## IPv6 Routing

### IPv6 Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | false |
| MGMT | false |
| Tenant_A_APP_Zone | false |
| Tenant_A_WEB_Zone | false |
| Tenant_D_WAN_Zone | true |

## Static Routes

### Static Routes Summary

| VRF | Destination Prefix | Next Hop IP             | Exit interface      | Administrative Distance       | Tag               | Route Name                    | Metric         |
| --- | ------------------ | ----------------------- | ------------------- | ----------------------------- | ----------------- | ----------------------------- | -------------- |
| MGMT | 0.0.0.0/0 | 192.168.200.5 | - | 1 | - | - | - |
| Tenant_A_APP_Zone | 10.2.32.0/24 | - | Vlan132 | 1 | - | VARP | - |
| Tenant_A_APP_Zone | 10.3.32.0/24 | - | Vlan132 | 1 | - | VARP | - |

### Static Routes Device Configuration

```eos
!
ip route vrf MGMT 0.0.0.0/0 192.168.200.5
ip route vrf Tenant_A_APP_Zone 10.2.32.0/24 Vlan132 name VARP
ip route vrf Tenant_A_APP_Zone 10.3.32.0/24 Vlan132 name VARP
```

## Router BGP

### Router BGP Summary

| BGP AS | Router ID |
| ------ | --------- |
| 65101|  192.168.255.9 |

| BGP Tuning |
| ---------- |
| no bgp default ipv4-unicast |
| distance bgp 20 200 200 |
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
| 172.31.255.0 | 65001 | default | - | Inherited from peer group UNDERLAY-PEERS | Inherited from peer group UNDERLAY-PEERS | - | - | - |
| 172.31.255.2 | 65001 | default | - | Inherited from peer group UNDERLAY-PEERS | Inherited from peer group UNDERLAY-PEERS | - | - | - |
| 172.31.255.4 | 65001 | default | - | Inherited from peer group UNDERLAY-PEERS | Inherited from peer group UNDERLAY-PEERS | - | - | - |
| 172.31.255.6 | 65001 | default | - | Inherited from peer group UNDERLAY-PEERS | Inherited from peer group UNDERLAY-PEERS | - | - | - |
| 192.168.255.1 | 65001 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - |
| 192.168.255.2 | 65001 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - |
| 192.168.255.3 | 65001 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - |
| 192.168.255.4 | 65001 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - |

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
| Tenant_A_APP_Zone | 1.1.1.1:12 | 1234:12 | - | - | learned | 130-132 |
| Tenant_A_WEB_Zone | 1.1.1.1:11 | 1234:11 | - | - | learned | 120-121 |
| Tenant_D_WAN_Zone | 1.1.1.1:41 | 1234:41 | - | - | learned | 450-452 |

### Router BGP VRFs

| VRF | Route-Distinguisher | Redistribute |
| --- | ------------------- | ------------ |
| Tenant_A_APP_Zone | 1.1.1.1:12 | connected |
| Tenant_A_WEB_Zone | 1.1.1.1:11 | connected |
| Tenant_D_WAN_Zone | 1.1.1.1:41 | connected |

### Router BGP Device Configuration

```eos
!
router bgp 65101
   router-id 192.168.255.9
   no bgp default ipv4-unicast
   distance bgp 20 200 200
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
   neighbor 172.31.255.0 peer group UNDERLAY-PEERS
   neighbor 172.31.255.0 remote-as 65001
   neighbor 172.31.255.0 description DC1-SPINE1_Ethernet1
   neighbor 172.31.255.2 peer group UNDERLAY-PEERS
   neighbor 172.31.255.2 remote-as 65001
   neighbor 172.31.255.2 description DC1-SPINE2_Ethernet1
   neighbor 172.31.255.4 peer group UNDERLAY-PEERS
   neighbor 172.31.255.4 remote-as 65001
   neighbor 172.31.255.4 description DC1-SPINE3_Ethernet1
   neighbor 172.31.255.6 peer group UNDERLAY-PEERS
   neighbor 172.31.255.6 remote-as 65001
   neighbor 172.31.255.6 description DC1-SPINE4_Ethernet1
   neighbor 192.168.255.1 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.255.1 remote-as 65001
   neighbor 192.168.255.1 description DC1-SPINE1
   neighbor 192.168.255.2 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.255.2 remote-as 65001
   neighbor 192.168.255.2 description DC1-SPINE2
   neighbor 192.168.255.3 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.255.3 remote-as 65001
   neighbor 192.168.255.3 description DC1-SPINE3
   neighbor 192.168.255.4 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.255.4 remote-as 65001
   neighbor 192.168.255.4 description DC1-SPINE4
   redistribute connected route-map RM-CONN-2-BGP
   !
   vlan-aware-bundle Tenant_A_APP_Zone
      rd 1.1.1.1:12
      route-target both 1234:12
      redistribute learned
      vlan 130-132
   !
   vlan-aware-bundle Tenant_A_WEB_Zone
      rd 1.1.1.1:11
      route-target both 1234:11
      redistribute learned
      vlan 120-121
   !
   vlan-aware-bundle Tenant_D_WAN_Zone
      rd 1.1.1.1:41
      route-target both 1234:41
      redistribute learned
      vlan 450-452
   !
   address-family evpn
      host-flap detection window 180 threshold 5 expiry timeout 10 seconds
      neighbor EVPN-OVERLAY-PEERS activate
   !
   address-family ipv4
      no neighbor EVPN-OVERLAY-PEERS activate
      neighbor UNDERLAY-PEERS activate
   !
   vrf Tenant_A_APP_Zone
      rd 1.1.1.1:12
      route-target import evpn 1234:12
      route-target export evpn 1234:12
      router-id 192.168.255.9
      redistribute connected
   !
   vrf Tenant_A_WEB_Zone
      rd 1.1.1.1:11
      route-target import evpn 1234:11
      route-target export evpn 1234:11
      router-id 192.168.255.9
      redistribute connected
   !
   vrf Tenant_D_WAN_Zone
      rd 1.1.1.1:41
      route-target import evpn 1234:41
      route-target export evpn 1234:41
      router-id 192.168.255.9
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

#### IP IGMP Snooping Vlan Summary

| Vlan | IGMP Snooping | Fast Leave | Max Groups | Proxy |
| ---- | ------------- | ---------- | ---------- | ----- |
| 120 | False | - | - | - |

### IP IGMP Snooping Device Configuration

```eos
!
no ip igmp snooping vlan 120
```

# Filters

## Prefix-lists

### Prefix-lists Summary

#### PL-LOOPBACKS-EVPN-OVERLAY

| Sequence | Action |
| -------- | ------ |
| 10 | permit 192.168.255.0/24 eq 32 |
| 20 | permit 192.168.254.0/24 eq 32 |

### Prefix-lists Device Configuration

```eos
!
ip prefix-list PL-LOOPBACKS-EVPN-OVERLAY
   seq 10 permit 192.168.255.0/24 eq 32
   seq 20 permit 192.168.254.0/24 eq 32
```

## Route-maps

### Route-maps Summary

#### RM-CONN-2-BGP

| Sequence | Type | Match and/or Set |
| -------- | ---- | ---------------- |
| 10 | permit | match ip address prefix-list PL-LOOPBACKS-EVPN-OVERLAY |

### Route-maps Device Configuration

```eos
!
route-map RM-CONN-2-BGP permit 10
   match ip address prefix-list PL-LOOPBACKS-EVPN-OVERLAY
```

# ACL

# VRF Instances

## VRF Instances Summary

| VRF Name | IP Routing |
| -------- | ---------- |
| MGMT | disabled |
| Tenant_A_APP_Zone | enabled |
| Tenant_A_WEB_Zone | enabled |
| Tenant_D_WAN_Zone | enabled |

## VRF Instances Device Configuration

```eos
!
vrf instance MGMT
!
vrf instance Tenant_A_APP_Zone
!
vrf instance Tenant_A_WEB_Zone
!
vrf instance Tenant_D_WAN_Zone
```

# Quality Of Service
