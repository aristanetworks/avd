# DC1-SVC3B
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
  - [Monitor Sessions](#monitor-sessions)
- [MLAG](#mlag)
  - [MLAG Summary](#mlag-summary)
  - [MLAG Device Configuration](#mlag-device-configuration)
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
| Management1 | oob_management | oob | MGMT | 192.168.200.109/24 | 192.168.200.5 |

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
   ip address 192.168.200.109/24
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
| example@example.com | EOS_DESIGNS_UNIT_TESTS DC1-SVC3B | All | Disabled |

### SNMP Device Configuration

```eos
!
snmp-server contact example@example.com
snmp-server location EOS_DESIGNS_UNIT_TESTS DC1-SVC3B
```

## Monitor Sessions

### Monitor Sessions Summary

#### MonitoringSessionServer18WithDest

##### MonitoringSessionServer18WithDest Sources

| Sources | Direction | Access Group Type | Access Group Name | Access Group Priority |
| ------- | --------- | ----------------- | ----------------- | --------------------- |
| Ethernet25 | rx | ip | MyIpACL | 5 |
| Port-Channel27 | tx | mac | MyMacACL | 5 |

##### MonitoringSessionServer18WithDest Destinations and Session Settings

| Settings | Values |
| -------- | ------ |
| Destinations | Ethernet26, Port-Channel42 |
| Encapsulation Gre Metadata Tx | True |
| Header Remove Size | 20 |
| Access Group Type | ip |
| Access Group Name | ip_acl |
| Rate Limit per Ingress Chip | 30 bps |
| Rate Limit per Egress Chip | 30 bps |
| Sample | 10 |
| Truncate Enabled | True |
| Truncate Size | 20 |

### Monitor Sessions Configuration

```eos
!
monitor session MonitoringSessionServer18WithDest source Ethernet25 rx ip access-group MyIpACL priority 5
monitor session MonitoringSessionServer18WithDest source Port-Channel27 tx mac access-group MyMacACL priority 5
monitor session MonitoringSessionServer18WithDest destination Ethernet26
monitor session MonitoringSessionServer18WithDest destination Port-Channel42
monitor session MonitoringSessionServer18WithDest encapsulation gre metadata tx
monitor session MonitoringSessionServer18WithDest header remove size 20
monitor session MonitoringSessionServer18WithDest ip access-group ip_acl
monitor session MonitoringSessionServer18WithDest rate-limit per-ingress-chip 30 bps
monitor session MonitoringSessionServer18WithDest rate-limit per-egress-chip 30 bps
monitor session MonitoringSessionServer18WithDest sample 10
monitor session MonitoringSessionServer18WithDest truncate size 20
```

# MLAG

## MLAG Summary

| Domain-id | Local-interface | Peer-address | Peer-link |
| --------- | --------------- | ------------ | --------- |
| DC1_SVC3 | Vlan4092 | 10.255.252.6 | Port-Channel2000 |

Dual primary detection is disabled.

## MLAG Device Configuration

```eos
!
mlag configuration
   domain-id DC1_SVC3
   local-interface Vlan4092
   peer-address 10.255.252.6
   peer-link Port-Channel2000
   reload-delay mlag 300
   reload-delay non-mlag 330
```

# Spanning Tree

## Spanning Tree Summary

STP mode: **mstp**

STP Root Super: **True**

### MSTP Instance and Priority

| Instance(s) | Priority |
| -------- | -------- |
| 0 | 4096 |

### Global Spanning-Tree Settings

- Spanning Tree disabled for VLANs: **4090,4092**

## Spanning Tree Device Configuration

```eos
!
spanning-tree root super
spanning-tree mode mstp
no spanning-tree vlan-id 4090,4092
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
| 2 | MLAG_iBGP_Tenant_C_OP_Zone | LEAF_PEER_L3 |
| 110 | Tenant_A_OP_Zone_1 | - |
| 111 | Tenant_A_OP_Zone_2 | - |
| 112 | Tenant_A_OP_Zone_3 | - |
| 120 | Tenant_A_WEB_Zone_1 | - |
| 121 | Tenant_A_WEBZone_2 | - |
| 130 | Tenant_A_APP_Zone_1 | - |
| 131 | Tenant_A_APP_Zone_2 | - |
| 140 | Tenant_A_DB_BZone_1 | - |
| 141 | Tenant_A_DB_Zone_2 | - |
| 150 | Tenant_A_WAN_Zone_1 | - |
| 160 | Tenant_A_VMOTION | - |
| 161 | Tenant_A_NFS | - |
| 210 | Tenant_B_OP_Zone_1 | - |
| 211 | Tenant_B_OP_Zone_2 | - |
| 250 | Tenant_B_WAN_Zone_1 | - |
| 310 | Tenant_C_OP_Zone_1 | - |
| 311 | Tenant_C_OP_Zone_2 | - |
| 350 | Tenant_C_WAN_Zone_1 | - |
| 3008 | MLAG_iBGP_Tenant_A_OP_Zone | LEAF_PEER_L3 |
| 3010 | MLAG_iBGP_Tenant_A_WEB_Zone | LEAF_PEER_L3 |
| 3011 | MLAG_iBGP_Tenant_A_APP_Zone | LEAF_PEER_L3 |
| 3012 | MLAG_iBGP_Tenant_A_DB_Zone | LEAF_PEER_L3 |
| 3013 | MLAG_iBGP_Tenant_A_WAN_Zone | LEAF_PEER_L3 |
| 3019 | MLAG_iBGP_Tenant_B_OP_Zone | LEAF_PEER_L3 |
| 3020 | MLAG_iBGP_Tenant_B_WAN_Zone | LEAF_PEER_L3 |
| 3030 | MLAG_iBGP_Tenant_C_WAN_Zone | LEAF_PEER_L3 |
| 4090 | LEAF_PEER_L3 | LEAF_PEER_L3 |
| 4092 | MLAG_PEER | MLAG |

## VLANs Device Configuration

```eos
!
vlan 2
   name MLAG_iBGP_Tenant_C_OP_Zone
   trunk group LEAF_PEER_L3
!
vlan 110
   name Tenant_A_OP_Zone_1
!
vlan 111
   name Tenant_A_OP_Zone_2
!
vlan 112
   name Tenant_A_OP_Zone_3
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
vlan 140
   name Tenant_A_DB_BZone_1
!
vlan 141
   name Tenant_A_DB_Zone_2
!
vlan 150
   name Tenant_A_WAN_Zone_1
!
vlan 160
   name Tenant_A_VMOTION
!
vlan 161
   name Tenant_A_NFS
!
vlan 210
   name Tenant_B_OP_Zone_1
!
vlan 211
   name Tenant_B_OP_Zone_2
!
vlan 250
   name Tenant_B_WAN_Zone_1
!
vlan 310
   name Tenant_C_OP_Zone_1
!
vlan 311
   name Tenant_C_OP_Zone_2
!
vlan 350
   name Tenant_C_WAN_Zone_1
!
vlan 3008
   name MLAG_iBGP_Tenant_A_OP_Zone
   trunk group LEAF_PEER_L3
!
vlan 3010
   name MLAG_iBGP_Tenant_A_WEB_Zone
   trunk group LEAF_PEER_L3
!
vlan 3011
   name MLAG_iBGP_Tenant_A_APP_Zone
   trunk group LEAF_PEER_L3
!
vlan 3012
   name MLAG_iBGP_Tenant_A_DB_Zone
   trunk group LEAF_PEER_L3
!
vlan 3013
   name MLAG_iBGP_Tenant_A_WAN_Zone
   trunk group LEAF_PEER_L3
!
vlan 3019
   name MLAG_iBGP_Tenant_B_OP_Zone
   trunk group LEAF_PEER_L3
!
vlan 3020
   name MLAG_iBGP_Tenant_B_WAN_Zone
   trunk group LEAF_PEER_L3
!
vlan 3030
   name MLAG_iBGP_Tenant_C_WAN_Zone
   trunk group LEAF_PEER_L3
!
vlan 4090
   name LEAF_PEER_L3
   trunk group LEAF_PEER_L3
!
vlan 4092
   name MLAG_PEER
   trunk group MLAG
```

# Interfaces

## Ethernet Interfaces

### Ethernet Interfaces Summary

#### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | Channel-Group |
| --------- | ----------- | ---- | ----- | ----------- | ----------- | ------------- |
| Ethernet5 | MLAG_PEER_DC1-SVC3A_Ethernet5 | *trunk | *1-4094 | *- | *['LEAF_PEER_L3', 'MLAG'] | 2000 |
| Ethernet6 | MLAG_PEER_DC1-SVC3A_Ethernet6 | *trunk | *1-4094 | *- | *['LEAF_PEER_L3', 'MLAG'] | 2000 |
| Ethernet7 | DC1-L2LEAF2A_Ethernet2 | *trunk | *110-112,120-121,130-131,140-141,150,160-161,210-211,250,310-311,350 | *- | *- | 7 |
| Ethernet8 | DC1-L2LEAF2B_Ethernet2 | *trunk | *110-112,120-121,130-131,140-141,150,160-161,210-211,250,310-311,350 | *- | *- | 7 |
| Ethernet11 |  server04_inherit_all_from_profile_Eth2 | trunk | 1-4094 | - | - | - |
| Ethernet12 |  server05_no_profile_Eth2 | trunk | 1-4094 | - | - | - |
| Ethernet13 |  server06_override_profile_Eth2 | access | 210 | - | - | - |
| Ethernet14 | server07_inherit_all_from_profile_port_channel_Eth2 | *trunk | *1-4094 | *- | *- | 14 |
| Ethernet15 | server08_no_profile_port_channel_Eth2 | *trunk | *1-4094 | *- | *- | 15 |
| Ethernet16 |  server09_override_profile_no_port_channel_Eth2 | access | 210 | - | - | - |
| Ethernet17 | server10_no_profile_port_channel_lacp_fallback_Eth2 | *trunk | *1-4094 | *- | *- | 17 |
| Ethernet18 | server11_inherit_profile_port_channel_lacp_fallback_Eth2 | *trunk | *1-4094 | *- | *- | 18 |
| Ethernet19 | server12_inherit_nested_profile_port_channel_lacp_fallback_Eth2 | *trunk | *1-4094 | *- | *- | 19 |
| Ethernet20 |  server13_disabled_interfaces_Eth2 | access | 110 | - | - | - |
| Ethernet21 |  server14_explicitly_enabled_interfaces_Eth2 | access | 110 | - | - | - |
| Ethernet22 | server15_port_channel_with_disabled_phy_interfaces_Eth2 | *access | *110 | *- | *- | 22 |
| Ethernet23 | server16_port_channel_with_disabled_port_channel_Eth2 | *access | *110 | *- | *- | 23 |
| Ethernet24 | server17_port_channel_with_disabled_phy_and_po_interfaces_Eth2 | *access | *110 | *- | *- | 24 |
| Ethernet25 |  server18_monitoring_session_source_phys_interfaces_Eth2 | access | 110 | - | - | - |
| Ethernet26 |  server19_monitoring_session_destination_phys_Eth2 | access | - | - | - | - |
| Ethernet27 | server18_monitoring_session_source_po_Eth4 | *access | *110 | *- | *- | 27 |
| Ethernet42 | server21_monitoring_session_destination_po_Eth2 | *access | *110 | *- | *- | 42 |

*Inherited from Port-Channel Interface

#### IPv4

| Interface | Description | Type | Channel Group | IP Address | VRF |  MTU | Shutdown | ACL In | ACL Out |
| --------- | ----------- | -----| ------------- | ---------- | ----| ---- | -------- | ------ | ------- |
| Ethernet1 | P2P_LINK_TO_DC1-SPINE1_Ethernet5 | routed | - | 172.31.255.65/31 | default | 1500 | false | - | - |
| Ethernet2 | P2P_LINK_TO_DC1-SPINE2_Ethernet5 | routed | - | 172.31.255.67/31 | default | 1500 | false | - | - |
| Ethernet3 | P2P_LINK_TO_DC1-SPINE3_Ethernet5 | routed | - | 172.31.255.69/31 | default | 1500 | false | - | - |
| Ethernet4 | P2P_LINK_TO_DC1-SPINE4_Ethernet5 | routed | - | 172.31.255.71/31 | default | 1500 | false | - | - |

### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet1
   description P2P_LINK_TO_DC1-SPINE1_Ethernet5
   no shutdown
   mtu 1500
   speed forced 100gfull
   no switchport
   ip address 172.31.255.65/31
!
interface Ethernet2
   description P2P_LINK_TO_DC1-SPINE2_Ethernet5
   no shutdown
   mtu 1500
   speed forced 100gfull
   no switchport
   ip address 172.31.255.67/31
!
interface Ethernet3
   description P2P_LINK_TO_DC1-SPINE3_Ethernet5
   no shutdown
   mtu 1500
   speed forced 100gfull
   no switchport
   ip address 172.31.255.69/31
!
interface Ethernet4
   description P2P_LINK_TO_DC1-SPINE4_Ethernet5
   no shutdown
   mtu 1500
   speed forced 100gfull
   no switchport
   ip address 172.31.255.71/31
!
interface Ethernet5
   description MLAG_PEER_DC1-SVC3A_Ethernet5
   no shutdown
   speed 100g
   channel-group 2000 mode active
!
interface Ethernet6
   description MLAG_PEER_DC1-SVC3A_Ethernet6
   no shutdown
   speed 100g
   channel-group 2000 mode active
!
interface Ethernet7
   description DC1-L2LEAF2A_Ethernet2
   no shutdown
   channel-group 7 mode active
!
interface Ethernet8
   description DC1-L2LEAF2B_Ethernet2
   no shutdown
   channel-group 7 mode active
!
interface Ethernet11
   description server04_inherit_all_from_profile_Eth2
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
   spanning-tree bpduguard disable
   spanning-tree bpdufilter disable
!
interface Ethernet12
   description server05_no_profile_Eth2
   no shutdown
   switchport trunk allowed vlan 1-4094
   switchport mode trunk
   switchport
   storm-control all level 10
   storm-control broadcast level pps 100
   storm-control multicast level 1
   storm-control unknown-unicast level 2
   spanning-tree portfast
   spanning-tree bpduguard disable
   spanning-tree bpdufilter enable
!
interface Ethernet13
   description server06_override_profile_Eth2
   no shutdown
   l2 mtu 8000
   switchport access vlan 210
   switchport mode access
   switchport
   storm-control all level pps 20
   storm-control broadcast level 200
   storm-control multicast level 1
   storm-control unknown-unicast level 2
   spanning-tree portfast network
   spanning-tree bpduguard enable
   spanning-tree bpdufilter disable
!
interface Ethernet14
   description server07_inherit_all_from_profile_port_channel_Eth2
   no shutdown
   channel-group 14 mode active
!
interface Ethernet15
   description server08_no_profile_port_channel_Eth2
   no shutdown
   channel-group 15 mode on
!
interface Ethernet16
   description server09_override_profile_no_port_channel_Eth2
   no shutdown
   l2 mtu 8000
   switchport access vlan 210
   switchport mode access
   switchport
   storm-control all level pps 20
   storm-control broadcast level 200
   storm-control multicast level 1
   storm-control unknown-unicast level 2
   spanning-tree portfast network
   spanning-tree bpduguard enable
   spanning-tree bpdufilter disable
!
interface Ethernet17
   description server10_no_profile_port_channel_lacp_fallback_Eth2
   no shutdown
   channel-group 17 mode active
   lacp port-priority 32768
!
interface Ethernet18
   description server11_inherit_profile_port_channel_lacp_fallback_Eth2
   no shutdown
   channel-group 18 mode active
   lacp port-priority 32768
!
interface Ethernet19
   description server12_inherit_nested_profile_port_channel_lacp_fallback_Eth2
   no shutdown
   channel-group 19 mode active
   lacp port-priority 32768
!
interface Ethernet20
   description server13_disabled_interfaces_Eth2
   shutdown
   switchport access vlan 110
   switchport mode access
   switchport
!
interface Ethernet21
   description server14_explicitly_enabled_interfaces_Eth2
   no shutdown
   switchport access vlan 110
   switchport mode access
   switchport
!
interface Ethernet22
   description server15_port_channel_with_disabled_phy_interfaces_Eth2
   shutdown
   channel-group 22 mode active
!
interface Ethernet23
   description server16_port_channel_with_disabled_port_channel_Eth2
   no shutdown
   channel-group 23 mode active
!
interface Ethernet24
   description server17_port_channel_with_disabled_phy_and_po_interfaces_Eth2
   shutdown
   channel-group 24 mode active
!
interface Ethernet25
   description server18_monitoring_session_source_phys_interfaces_Eth2
   no shutdown
   switchport access vlan 110
   switchport mode access
   switchport
!
interface Ethernet26
   description server19_monitoring_session_destination_phys_Eth2
   no shutdown
   switchport
!
interface Ethernet27
   description server18_monitoring_session_source_po_Eth4
   no shutdown
   channel-group 27 mode active
!
interface Ethernet42
   description server21_monitoring_session_destination_po_Eth2
   no shutdown
   channel-group 42 mode active
```

## Port-Channel Interfaces

### Port-Channel Interfaces Summary

#### L2

| Interface | Description | Type | Mode | VLANs | Native VLAN | Trunk Group | LACP Fallback Timeout | LACP Fallback Mode | MLAG ID | EVPN ESI |
| --------- | ----------- | ---- | ---- | ----- | ----------- | ------------| --------------------- | ------------------ | ------- | -------- |
| Port-Channel7 | DC1_L2LEAF2_Po1 | switched | trunk | 110-112,120-121,130-131,140-141,150,160-161,210-211,250,310-311,350 | - | - | - | - | 7 | - |
| Port-Channel14 | server07_inherit_all_from_profile_port_channel_ALL_WITH_SECURITY_PORT_CHANNEL | switched | trunk | 1-4094 | - | - | - | - | 14 | - |
| Port-Channel15 | server08_no_profile_port_channel_server08_no_profile_port_channel | switched | trunk | 1-4094 | - | - | - | - | 15 | - |
| Port-Channel17 | server10_no_profile_port_channel_lacp_fallback_server10_no_profile_port_channel_lacp_fallback | switched | trunk | 1-4094 | - | - | 90 | static | 17 | - |
| Port-Channel18 | server11_inherit_profile_port_channel_lacp_fallback_ALL_WITH_SECURITY_PORT_CHANNEL | switched | trunk | 1-4094 | - | - | 10 | static | 18 | - |
| Port-Channel19 | server12_inherit_nested_profile_port_channel_lacp_fallback_NESTED_ALL_WITH_SECURITY_PORT_CHANNEL | switched | trunk | 1-4094 | - | - | 10 | static | 19 | - |
| Port-Channel22 | server15_port_channel_with_disabled_phy_interfaces_server15_port_channel_with_disabled_phy_interfaces | switched | access | 110 | - | - | - | - | 22 | - |
| Port-Channel23 | server16_port_channel_with_disabled_port_channel_server16_port_channel_with_disabled_port_channel | switched | access | 110 | - | - | - | - | 23 | - |
| Port-Channel24 | server17_port_channel_with_disabled_phy_and_po_interfaces_server17_port_channel_with_disabled_phy_and_po_interfaces | switched | access | 110 | - | - | - | - | 24 | - |
| Port-Channel27 | server18_monitoring_session_source_po_server18_monitoring_session_source_po | switched | access | 110 | - | - | - | - | 27 | - |
| Port-Channel42 | server21_monitoring_session_destination_po_server21_monitoring_session_destination_po | switched | access | 110 | - | - | - | - | 42 | - |
| Port-Channel2000 | MLAG_PEER_DC1-SVC3A_Po2000 | switched | trunk | 1-4094 | - | ['LEAF_PEER_L3', 'MLAG'] | - | - | - | - |

### Port-Channel Interfaces Device Configuration

```eos
!
interface Port-Channel7
   description DC1_L2LEAF2_Po1
   no shutdown
   switchport
   switchport trunk allowed vlan 110-112,120-121,130-131,140-141,150,160-161,210-211,250,310-311,350
   switchport mode trunk
   mlag 7
!
interface Port-Channel14
   description server07_inherit_all_from_profile_port_channel_ALL_WITH_SECURITY_PORT_CHANNEL
   no shutdown
   switchport
   switchport trunk allowed vlan 1-4094
   switchport mode trunk
   mlag 14
   spanning-tree portfast
   spanning-tree bpduguard enable
   spanning-tree bpdufilter enable
   storm-control all level 10
   storm-control broadcast level pps 100
   storm-control multicast level 1
   storm-control unknown-unicast level 2
!
interface Port-Channel15
   description server08_no_profile_port_channel_server08_no_profile_port_channel
   no shutdown
   switchport
   switchport trunk allowed vlan 1-4094
   switchport mode trunk
   mlag 15
   spanning-tree portfast
   spanning-tree bpduguard disable
   spanning-tree bpdufilter enable
   storm-control all level 10
   storm-control broadcast level pps 100
   storm-control multicast level 1
   storm-control unknown-unicast level 2
!
interface Port-Channel17
   description server10_no_profile_port_channel_lacp_fallback_server10_no_profile_port_channel_lacp_fallback
   no shutdown
   switchport
   switchport trunk allowed vlan 1-4094
   switchport mode trunk
   port-channel lacp fallback timeout 90
   port-channel lacp fallback static
   mlag 17
   spanning-tree portfast
   spanning-tree bpduguard disable
   spanning-tree bpdufilter enable
   storm-control all level 10
   storm-control broadcast level pps 100
   storm-control multicast level 1
   storm-control unknown-unicast level 2
!
interface Port-Channel18
   description server11_inherit_profile_port_channel_lacp_fallback_ALL_WITH_SECURITY_PORT_CHANNEL
   no shutdown
   switchport
   switchport trunk allowed vlan 1-4094
   switchport mode trunk
   port-channel lacp fallback timeout 10
   port-channel lacp fallback static
   mlag 18
   spanning-tree portfast
   spanning-tree bpduguard enable
   spanning-tree bpdufilter enable
   storm-control all level 10
   storm-control broadcast level pps 100
   storm-control multicast level 1
   storm-control unknown-unicast level 2
!
interface Port-Channel19
   description server12_inherit_nested_profile_port_channel_lacp_fallback_NESTED_ALL_WITH_SECURITY_PORT_CHANNEL
   no shutdown
   switchport
   switchport trunk allowed vlan 1-4094
   switchport mode trunk
   port-channel lacp fallback timeout 10
   port-channel lacp fallback static
   mlag 19
   spanning-tree portfast
   spanning-tree bpduguard enable
   spanning-tree bpdufilter enable
   storm-control all level 10
   storm-control broadcast level pps 100
   storm-control multicast level 1
   storm-control unknown-unicast level 2
!
interface Port-Channel22
   description server15_port_channel_with_disabled_phy_interfaces_server15_port_channel_with_disabled_phy_interfaces
   no shutdown
   switchport
   switchport access vlan 110
   mlag 22
!
interface Port-Channel23
   description server16_port_channel_with_disabled_port_channel_server16_port_channel_with_disabled_port_channel
   shutdown
   switchport
   switchport access vlan 110
   mlag 23
!
interface Port-Channel24
   description server17_port_channel_with_disabled_phy_and_po_interfaces_server17_port_channel_with_disabled_phy_and_po_interfaces
   shutdown
   switchport
   switchport access vlan 110
   mlag 24
!
interface Port-Channel27
   description server18_monitoring_session_source_po_server18_monitoring_session_source_po
   no shutdown
   switchport
   switchport access vlan 110
   mlag 27
!
interface Port-Channel42
   description server21_monitoring_session_destination_po_server21_monitoring_session_destination_po
   no shutdown
   switchport
   switchport access vlan 110
   mlag 42
!
interface Port-Channel2000
   description MLAG_PEER_DC1-SVC3A_Po2000
   no shutdown
   switchport
   switchport trunk allowed vlan 1-4094
   switchport mode trunk
   switchport trunk group LEAF_PEER_L3
   switchport trunk group MLAG
```

## Loopback Interfaces

### Loopback Interfaces Summary

#### IPv4

| Interface | Description | VRF | IP Address |
| --------- | ----------- | --- | ---------- |
| Loopback0 | EVPN_Overlay_Peering | default | 192.168.255.13/32 |
| Loopback1 | VTEP_VXLAN_Tunnel_Source | default | 192.168.254.12/32 |
| Loopback100 | Tenant_A_OP_Zone_VTEP_DIAGNOSTICS | Tenant_A_OP_Zone | 10.255.1.13/32 |

#### IPv6

| Interface | Description | VRF | IPv6 Address |
| --------- | ----------- | --- | ------------ |
| Loopback0 | EVPN_Overlay_Peering | default | - |
| Loopback1 | VTEP_VXLAN_Tunnel_Source | default | - |
| Loopback100 | Tenant_A_OP_Zone_VTEP_DIAGNOSTICS | Tenant_A_OP_Zone | - |


### Loopback Interfaces Device Configuration

```eos
!
interface Loopback0
   description EVPN_Overlay_Peering
   no shutdown
   ip address 192.168.255.13/32
!
interface Loopback1
   description VTEP_VXLAN_Tunnel_Source
   no shutdown
   ip address 192.168.254.12/32
!
interface Loopback100
   description Tenant_A_OP_Zone_VTEP_DIAGNOSTICS
   no shutdown
   vrf Tenant_A_OP_Zone
   ip address 10.255.1.13/32
```

## VLAN Interfaces

### VLAN Interfaces Summary

| Interface | Description | VRF |  MTU | Shutdown |
| --------- | ----------- | --- | ---- | -------- |
| Vlan2 | MLAG_PEER_L3_iBGP: vrf Tenant_C_OP_Zone | Tenant_C_OP_Zone | 1500 | false |
| Vlan110 | Tenant_A_OP_Zone_1 | Tenant_A_OP_Zone | - | false |
| Vlan111 | Tenant_A_OP_Zone_2 | Tenant_A_OP_Zone | - | false |
| Vlan112 | Tenant_A_OP_Zone_3 | Tenant_A_OP_Zone | 1560 | false |
| Vlan120 | Tenant_A_WEB_Zone_1 | Tenant_A_WEB_Zone | - | false |
| Vlan121 | Tenant_A_WEBZone_2 | Tenant_A_WEB_Zone | 1560 | true |
| Vlan130 | Tenant_A_APP_Zone_1 | Tenant_A_APP_Zone | - | false |
| Vlan131 | Tenant_A_APP_Zone_2 | Tenant_A_APP_Zone | - | false |
| Vlan140 | Tenant_A_DB_BZone_1 | Tenant_A_DB_Zone | - | false |
| Vlan141 | Tenant_A_DB_Zone_2 | Tenant_A_DB_Zone | - | false |
| Vlan150 | Tenant_A_WAN_Zone_1 | Tenant_A_WAN_Zone | - | false |
| Vlan210 | Tenant_B_OP_Zone_1 | Tenant_B_OP_Zone | - | false |
| Vlan211 | Tenant_B_OP_Zone_2 | Tenant_B_OP_Zone | - | false |
| Vlan250 | Tenant_B_WAN_Zone_1 | Tenant_B_WAN_Zone | - | false |
| Vlan310 | Tenant_C_OP_Zone_1 | Tenant_C_OP_Zone | - | false |
| Vlan311 | Tenant_C_OP_Zone_2 | Tenant_C_OP_Zone | - | false |
| Vlan350 | Tenant_C_WAN_Zone_1 | Tenant_C_WAN_Zone | - | false |
| Vlan3008 | MLAG_PEER_L3_iBGP: vrf Tenant_A_OP_Zone | Tenant_A_OP_Zone | 1500 | false |
| Vlan3010 | MLAG_PEER_L3_iBGP: vrf Tenant_A_WEB_Zone | Tenant_A_WEB_Zone | 1500 | false |
| Vlan3011 | MLAG_PEER_L3_iBGP: vrf Tenant_A_APP_Zone | Tenant_A_APP_Zone | 1500 | false |
| Vlan3012 | MLAG_PEER_L3_iBGP: vrf Tenant_A_DB_Zone | Tenant_A_DB_Zone | 1500 | false |
| Vlan3013 | MLAG_PEER_L3_iBGP: vrf Tenant_A_WAN_Zone | Tenant_A_WAN_Zone | 1500 | false |
| Vlan3019 | MLAG_PEER_L3_iBGP: vrf Tenant_B_OP_Zone | Tenant_B_OP_Zone | 1500 | false |
| Vlan3020 | MLAG_PEER_L3_iBGP: vrf Tenant_B_WAN_Zone | Tenant_B_WAN_Zone | 1500 | false |
| Vlan3030 | MLAG_PEER_L3_iBGP: vrf Tenant_C_WAN_Zone | Tenant_C_WAN_Zone | 1500 | false |
| Vlan4090 | MLAG_PEER_L3_PEERING | default | 1500 | false |
| Vlan4092 | MLAG_PEER | default | 1500 | false |

#### IPv4

| Interface | VRF | IP Address | IP Address Virtual | IP Router Virtual Address | VRRP | ACL In | ACL Out |
| --------- | --- | ---------- | ------------------ | ------------------------- | ---- | ------ | ------- |
| Vlan2 |  Tenant_C_OP_Zone  |  10.255.251.7/31  |  -  |  -  |  -  |  -  |  -  |
| Vlan110 |  Tenant_A_OP_Zone  |  -  |  10.1.10.1/24  |  -  |  -  |  -  |  -  |
| Vlan111 |  Tenant_A_OP_Zone  |  -  |  10.1.11.1/24  |  -  |  -  |  -  |  -  |
| Vlan112 |  Tenant_A_OP_Zone  |  -  |  -  |  -  |  -  |  -  |  -  |
| Vlan120 |  Tenant_A_WEB_Zone  |  -  |  10.1.20.1/24  |  -  |  -  |  -  |  -  |
| Vlan121 |  Tenant_A_WEB_Zone  |  -  |  10.1.10.254/24  |  -  |  -  |  -  |  -  |
| Vlan130 |  Tenant_A_APP_Zone  |  -  |  10.1.30.1/24  |  -  |  -  |  -  |  -  |
| Vlan131 |  Tenant_A_APP_Zone  |  -  |  10.1.31.1/24  |  -  |  -  |  -  |  -  |
| Vlan140 |  Tenant_A_DB_Zone  |  -  |  10.1.40.1/24  |  -  |  -  |  -  |  -  |
| Vlan141 |  Tenant_A_DB_Zone  |  -  |  10.1.41.1/24  |  -  |  -  |  -  |  -  |
| Vlan150 |  Tenant_A_WAN_Zone  |  -  |  10.1.40.1/24  |  -  |  -  |  -  |  -  |
| Vlan210 |  Tenant_B_OP_Zone  |  -  |  10.2.10.1/24  |  -  |  -  |  -  |  -  |
| Vlan211 |  Tenant_B_OP_Zone  |  -  |  10.2.11.1/24  |  -  |  -  |  -  |  -  |
| Vlan250 |  Tenant_B_WAN_Zone  |  -  |  10.2.50.1/24  |  -  |  -  |  -  |  -  |
| Vlan310 |  Tenant_C_OP_Zone  |  -  |  10.3.10.1/24  |  -  |  -  |  -  |  -  |
| Vlan311 |  Tenant_C_OP_Zone  |  -  |  10.3.11.1/24  |  -  |  -  |  -  |  -  |
| Vlan350 |  Tenant_C_WAN_Zone  |  -  |  10.3.50.1/24  |  -  |  -  |  -  |  -  |
| Vlan3008 |  Tenant_A_OP_Zone  |  10.255.251.7/31  |  -  |  -  |  -  |  -  |  -  |
| Vlan3010 |  Tenant_A_WEB_Zone  |  10.255.251.7/31  |  -  |  -  |  -  |  -  |  -  |
| Vlan3011 |  Tenant_A_APP_Zone  |  10.255.251.7/31  |  -  |  -  |  -  |  -  |  -  |
| Vlan3012 |  Tenant_A_DB_Zone  |  10.255.251.7/31  |  -  |  -  |  -  |  -  |  -  |
| Vlan3013 |  Tenant_A_WAN_Zone  |  10.255.251.7/31  |  -  |  -  |  -  |  -  |  -  |
| Vlan3019 |  Tenant_B_OP_Zone  |  10.255.251.7/31  |  -  |  -  |  -  |  -  |  -  |
| Vlan3020 |  Tenant_B_WAN_Zone  |  10.255.251.7/31  |  -  |  -  |  -  |  -  |  -  |
| Vlan3030 |  Tenant_C_WAN_Zone  |  10.255.251.7/31  |  -  |  -  |  -  |  -  |  -  |
| Vlan4090 |  default  |  10.255.251.7/31  |  -  |  -  |  -  |  -  |  -  |
| Vlan4092 |  default  |  10.255.252.7/31  |  -  |  -  |  -  |  -  |  -  |

### VLAN Interfaces Device Configuration

```eos
!
interface Vlan2
   description MLAG_PEER_L3_iBGP: vrf Tenant_C_OP_Zone
   no shutdown
   mtu 1500
   vrf Tenant_C_OP_Zone
   ip address 10.255.251.7/31
!
interface Vlan110
   description Tenant_A_OP_Zone_1
   no shutdown
   vrf Tenant_A_OP_Zone
   ip address virtual 10.1.10.1/24
!
interface Vlan111
   description Tenant_A_OP_Zone_2
   no shutdown
   vrf Tenant_A_OP_Zone
   ip helper-address 1.1.1.1 vrf MGMT source-interface lo100
   ip address virtual 10.1.11.1/24
!
interface Vlan112
   description Tenant_A_OP_Zone_3
   no shutdown
   mtu 1560
   vrf Tenant_A_OP_Zone
   ip helper-address 2.2.2.2 vrf MGMT source-interface lo101
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
interface Vlan140
   description Tenant_A_DB_BZone_1
   no shutdown
   vrf Tenant_A_DB_Zone
   ip address virtual 10.1.40.1/24
!
interface Vlan141
   description Tenant_A_DB_Zone_2
   no shutdown
   vrf Tenant_A_DB_Zone
   ip address virtual 10.1.41.1/24
!
interface Vlan150
   description Tenant_A_WAN_Zone_1
   no shutdown
   vrf Tenant_A_WAN_Zone
   ip ospf area 1
   ip ospf cost 100
   ip ospf authentication
   ip ospf authentication-key 7 AQQvKeimxJu+uGQ/yYvv9w==
   ip address virtual 10.1.40.1/24
!
interface Vlan210
   description Tenant_B_OP_Zone_1
   no shutdown
   vrf Tenant_B_OP_Zone
   ip address virtual 10.2.10.1/24
!
interface Vlan211
   description Tenant_B_OP_Zone_2
   no shutdown
   vrf Tenant_B_OP_Zone
   ip address virtual 10.2.11.1/24
!
interface Vlan250
   description Tenant_B_WAN_Zone_1
   no shutdown
   vrf Tenant_B_WAN_Zone
   ip address virtual 10.2.50.1/24
!
interface Vlan310
   description Tenant_C_OP_Zone_1
   no shutdown
   vrf Tenant_C_OP_Zone
   ip address virtual 10.3.10.1/24
!
interface Vlan311
   description Tenant_C_OP_Zone_2
   no shutdown
   vrf Tenant_C_OP_Zone
   ip address virtual 10.3.11.1/24
!
interface Vlan350
   description Tenant_C_WAN_Zone_1
   no shutdown
   vrf Tenant_C_WAN_Zone
   ip address virtual 10.3.50.1/24
!
interface Vlan3008
   description MLAG_PEER_L3_iBGP: vrf Tenant_A_OP_Zone
   no shutdown
   mtu 1500
   vrf Tenant_A_OP_Zone
   ip address 10.255.251.7/31
!
interface Vlan3010
   description MLAG_PEER_L3_iBGP: vrf Tenant_A_WEB_Zone
   no shutdown
   mtu 1500
   vrf Tenant_A_WEB_Zone
   ip address 10.255.251.7/31
!
interface Vlan3011
   description MLAG_PEER_L3_iBGP: vrf Tenant_A_APP_Zone
   no shutdown
   mtu 1500
   vrf Tenant_A_APP_Zone
   ip address 10.255.251.7/31
!
interface Vlan3012
   description MLAG_PEER_L3_iBGP: vrf Tenant_A_DB_Zone
   no shutdown
   mtu 1500
   vrf Tenant_A_DB_Zone
   ip address 10.255.251.7/31
!
interface Vlan3013
   description MLAG_PEER_L3_iBGP: vrf Tenant_A_WAN_Zone
   no shutdown
   mtu 1500
   vrf Tenant_A_WAN_Zone
   ip address 10.255.251.7/31
!
interface Vlan3019
   description MLAG_PEER_L3_iBGP: vrf Tenant_B_OP_Zone
   no shutdown
   mtu 1500
   vrf Tenant_B_OP_Zone
   ip address 10.255.251.7/31
!
interface Vlan3020
   description MLAG_PEER_L3_iBGP: vrf Tenant_B_WAN_Zone
   no shutdown
   mtu 1500
   vrf Tenant_B_WAN_Zone
   ip address 10.255.251.7/31
!
interface Vlan3030
   description MLAG_PEER_L3_iBGP: vrf Tenant_C_WAN_Zone
   no shutdown
   mtu 1500
   vrf Tenant_C_WAN_Zone
   ip address 10.255.251.7/31
!
interface Vlan4090
   description MLAG_PEER_L3_PEERING
   no shutdown
   mtu 1500
   ip address 10.255.251.7/31
!
interface Vlan4092
   description MLAG_PEER
   no shutdown
   mtu 1500
   no autostate
   ip address 10.255.252.7/31
```

## VXLAN Interface

### VXLAN Interface Summary

| Setting | Value |
| ------- | ----- |
| Source Interface | Loopback1 |
| UDP port | 4789 |
| EVPN MLAG Shared Router MAC | mlag-system-id |

#### VLAN to VNI, Flood List and Multicast Group Mappings

| VLAN | VNI | Flood List | Multicast Group |
| ---- | --- | ---------- | --------------- |
| 110 | 10110 | - | - |
| 111 | 50111 | - | - |
| 112 | 10112 | - | - |
| 120 | 10120 | - | - |
| 121 | 10121 | - | - |
| 130 | 10130 | - | - |
| 131 | 10131 | - | - |
| 140 | 10140 | - | - |
| 141 | 10141 | - | - |
| 150 | 10150 | - | - |
| 160 | 10160 | - | - |
| 161 | 10161 | - | - |
| 210 | 20210 | - | - |
| 211 | 20211 | - | - |
| 250 | 20250 | - | - |
| 310 | 30310 | - | - |
| 311 | 30311 | - | - |
| 350 | 30350 | - | - |

#### VRF to VNI and Multicast Group Mappings

| VRF | VNI | Multicast Group |
| ---- | --- | --------------- |
| Tenant_A_APP_Zone | 12 | - |
| Tenant_A_DB_Zone | 13 | - |
| Tenant_A_OP_Zone | 10 | - |
| Tenant_A_WAN_Zone | 14 | - |
| Tenant_A_WEB_Zone | 11 | - |
| Tenant_B_OP_Zone | 20 | - |
| Tenant_B_WAN_Zone | 21 | - |
| Tenant_C_OP_Zone | 30 | - |
| Tenant_C_WAN_Zone | 31 | - |

### VXLAN Interface Device Configuration

```eos
!
interface Vxlan1
   description DC1-SVC3B_VTEP
   vxlan source-interface Loopback1
   vxlan virtual-router encapsulation mac-address mlag-system-id
   vxlan udp-port 4789
   vxlan vlan 110 vni 10110
   vxlan vlan 111 vni 50111
   vxlan vlan 112 vni 10112
   vxlan vlan 120 vni 10120
   vxlan vlan 121 vni 10121
   vxlan vlan 130 vni 10130
   vxlan vlan 131 vni 10131
   vxlan vlan 140 vni 10140
   vxlan vlan 141 vni 10141
   vxlan vlan 150 vni 10150
   vxlan vlan 160 vni 10160
   vxlan vlan 161 vni 10161
   vxlan vlan 210 vni 20210
   vxlan vlan 211 vni 20211
   vxlan vlan 250 vni 20250
   vxlan vlan 310 vni 30310
   vxlan vlan 311 vni 30311
   vxlan vlan 350 vni 30350
   vxlan vrf Tenant_A_APP_Zone vni 12
   vxlan vrf Tenant_A_DB_Zone vni 13
   vxlan vrf Tenant_A_OP_Zone vni 10
   vxlan vrf Tenant_A_WAN_Zone vni 14
   vxlan vrf Tenant_A_WEB_Zone vni 11
   vxlan vrf Tenant_B_OP_Zone vni 20
   vxlan vrf Tenant_B_WAN_Zone vni 21
   vxlan vrf Tenant_C_OP_Zone vni 30
   vxlan vrf Tenant_C_WAN_Zone vni 31
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
| Tenant_A_DB_Zone | true |
| Tenant_A_OP_Zone | true |
| Tenant_A_WAN_Zone | true |
| Tenant_A_WEB_Zone | true |
| Tenant_B_OP_Zone | true |
| Tenant_B_WAN_Zone | true |
| Tenant_C_OP_Zone | true |
| Tenant_C_WAN_Zone | true |

### IP Routing Device Configuration

```eos
!
ip routing
no ip routing vrf MGMT
ip routing vrf Tenant_A_APP_Zone
ip routing vrf Tenant_A_DB_Zone
ip routing vrf Tenant_A_OP_Zone
ip routing vrf Tenant_A_WAN_Zone
ip routing vrf Tenant_A_WEB_Zone
ip routing vrf Tenant_B_OP_Zone
ip routing vrf Tenant_B_WAN_Zone
ip routing vrf Tenant_C_OP_Zone
ip routing vrf Tenant_C_WAN_Zone
```
## IPv6 Routing

### IPv6 Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | false |
| MGMT | false |
| Tenant_A_APP_Zone | false |
| Tenant_A_DB_Zone | false |
| Tenant_A_OP_Zone | false |
| Tenant_A_WAN_Zone | false |
| Tenant_A_WEB_Zone | false |
| Tenant_B_OP_Zone | false |
| Tenant_B_WAN_Zone | false |
| Tenant_C_OP_Zone | false |
| Tenant_C_WAN_Zone | false |

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
| 65103|  192.168.255.13 |

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

#### MLAG-PEERS

| Settings | Value |
| -------- | ----- |
| Address Family | ipv4 |
| Remote AS | 65103 |
| Next-hop self | True |
| Send community | all |
| Maximum routes | 12000 |

#### UNDERLAY-PEERS

| Settings | Value |
| -------- | ----- |
| Address Family | ipv4 |
| Send community | all |
| Maximum routes | 12000 |

### BGP Neighbors

| Neighbor | Remote AS | VRF | Shutdown | Send-community | Maximum-routes | Allowas-in | BFD | RIB Pre-Policy Retain |
| -------- | --------- | --- | -------- | -------------- | -------------- | ---------- | --- | --------------------- |
| 10.255.251.6 | Inherited from peer group MLAG-PEERS | default | - | Inherited from peer group MLAG-PEERS | Inherited from peer group MLAG-PEERS | - | - | - |
| 172.31.255.64 | 65001 | default | - | Inherited from peer group UNDERLAY-PEERS | Inherited from peer group UNDERLAY-PEERS | - | - | - |
| 172.31.255.66 | 65001 | default | - | Inherited from peer group UNDERLAY-PEERS | Inherited from peer group UNDERLAY-PEERS | - | - | - |
| 172.31.255.68 | 65001 | default | - | Inherited from peer group UNDERLAY-PEERS | Inherited from peer group UNDERLAY-PEERS | - | - | - |
| 172.31.255.70 | 65001 | default | - | Inherited from peer group UNDERLAY-PEERS | Inherited from peer group UNDERLAY-PEERS | - | - | - |
| 192.168.255.1 | 65001 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - |
| 192.168.255.2 | 65001 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - |
| 192.168.255.3 | 65001 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - |
| 192.168.255.4 | 65001 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - |
| 10.255.251.6 | Inherited from peer group MLAG-PEERS | Tenant_A_APP_Zone | - | Inherited from peer group MLAG-PEERS | Inherited from peer group MLAG-PEERS | - | - | - |
| 10.255.251.6 | Inherited from peer group MLAG-PEERS | Tenant_A_DB_Zone | - | Inherited from peer group MLAG-PEERS | Inherited from peer group MLAG-PEERS | - | - | - |
| 10.255.251.6 | Inherited from peer group MLAG-PEERS | Tenant_A_OP_Zone | - | Inherited from peer group MLAG-PEERS | Inherited from peer group MLAG-PEERS | - | - | - |
| 10.255.251.6 | Inherited from peer group MLAG-PEERS | Tenant_A_WAN_Zone | - | Inherited from peer group MLAG-PEERS | Inherited from peer group MLAG-PEERS | - | - | - |
| 10.255.251.6 | Inherited from peer group MLAG-PEERS | Tenant_A_WEB_Zone | - | Inherited from peer group MLAG-PEERS | Inherited from peer group MLAG-PEERS | - | - | - |
| 10.255.251.6 | Inherited from peer group MLAG-PEERS | Tenant_B_OP_Zone | - | Inherited from peer group MLAG-PEERS | Inherited from peer group MLAG-PEERS | - | - | - |
| 10.255.251.6 | Inherited from peer group MLAG-PEERS | Tenant_B_WAN_Zone | - | Inherited from peer group MLAG-PEERS | Inherited from peer group MLAG-PEERS | - | - | - |
| 10.255.251.6 | Inherited from peer group MLAG-PEERS | Tenant_C_OP_Zone | - | Inherited from peer group MLAG-PEERS | Inherited from peer group MLAG-PEERS | - | - | - |
| 10.255.251.6 | Inherited from peer group MLAG-PEERS | Tenant_C_WAN_Zone | - | Inherited from peer group MLAG-PEERS | Inherited from peer group MLAG-PEERS | - | - | - |

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
| Tenant_A_APP_Zone | 65103:12 | 12:12 | - | - | learned | 130-131 |
| Tenant_A_DB_Zone | 65103:13 | 13:13 | - | - | learned | 140-141 |
| Tenant_A_NFS | 65103:20161 | 20161:20161 | - | - | learned | 161 |
| Tenant_A_OP_Zone | 65103:9 | 9:9 | - | - | learned | 110-112 |
| Tenant_A_VMOTION | 65103:20160 | 20160:20160 | - | - | learned | 160 |
| Tenant_A_WAN_Zone | 65103:14 | 14:14 | - | - | learned | 150 |
| Tenant_A_WEB_Zone | 65103:11 | 11:11 | - | - | learned | 120-121 |
| Tenant_B_OP_Zone | 65103:20 | 20:20 | - | - | learned | 210-211 |
| Tenant_B_WAN_Zone | 65103:21 | 21:21 | - | - | learned | 250 |
| Tenant_C_OP_Zone | 65103:30 | 30:30 | - | - | learned | 310-311 |
| Tenant_C_WAN_Zone | 65103:31 | 31:31 | - | - | learned | 350 |

### Router BGP VRFs

| VRF | Route-Distinguisher | Redistribute |
| --- | ------------------- | ------------ |
| Tenant_A_APP_Zone | 65103:12 | connected |
| Tenant_A_DB_Zone | 65103:13 | connected |
| Tenant_A_OP_Zone | 65103:9 | connected |
| Tenant_A_WAN_Zone | 65103:14 | connected |
| Tenant_A_WEB_Zone | 65103:11 | connected |
| Tenant_B_OP_Zone | 65103:20 | connected |
| Tenant_B_WAN_Zone | 65103:21 | connected |
| Tenant_C_OP_Zone | 65103:30 | connected |
| Tenant_C_WAN_Zone | 65103:31 | connected |

### Router BGP Device Configuration

```eos
!
router bgp 65103
   router-id 192.168.255.13
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
   neighbor MLAG-PEERS peer group
   neighbor MLAG-PEERS remote-as 65103
   neighbor MLAG-PEERS next-hop-self
   neighbor MLAG-PEERS description DC1-SVC3A
   neighbor MLAG-PEERS password 7 vnEaG8gMeQf3d3cN6PktXQ==
   neighbor MLAG-PEERS send-community
   neighbor MLAG-PEERS maximum-routes 12000
   neighbor MLAG-PEERS route-map RM-MLAG-PEER-IN in
   neighbor UNDERLAY-PEERS peer group
   neighbor UNDERLAY-PEERS password 7 AQQvKeimxJu+uGQ/yYvv9w==
   neighbor UNDERLAY-PEERS send-community
   neighbor UNDERLAY-PEERS maximum-routes 12000
   neighbor 10.255.251.6 peer group MLAG-PEERS
   neighbor 10.255.251.6 description DC1-SVC3A
   neighbor 172.31.255.64 peer group UNDERLAY-PEERS
   neighbor 172.31.255.64 remote-as 65001
   neighbor 172.31.255.64 description DC1-SPINE1_Ethernet5
   neighbor 172.31.255.66 peer group UNDERLAY-PEERS
   neighbor 172.31.255.66 remote-as 65001
   neighbor 172.31.255.66 description DC1-SPINE2_Ethernet5
   neighbor 172.31.255.68 peer group UNDERLAY-PEERS
   neighbor 172.31.255.68 remote-as 65001
   neighbor 172.31.255.68 description DC1-SPINE3_Ethernet5
   neighbor 172.31.255.70 peer group UNDERLAY-PEERS
   neighbor 172.31.255.70 remote-as 65001
   neighbor 172.31.255.70 description DC1-SPINE4_Ethernet5
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
      rd 65103:12
      route-target both 12:12
      redistribute learned
      vlan 130-131
   !
   vlan-aware-bundle Tenant_A_DB_Zone
      rd 65103:13
      route-target both 13:13
      redistribute learned
      vlan 140-141
   !
   vlan-aware-bundle Tenant_A_NFS
      rd 65103:20161
      route-target both 20161:20161
      redistribute learned
      vlan 161
   !
   vlan-aware-bundle Tenant_A_OP_Zone
      rd 65103:9
      route-target both 9:9
      redistribute learned
      vlan 110-112
   !
   vlan-aware-bundle Tenant_A_VMOTION
      rd 65103:20160
      route-target both 20160:20160
      redistribute learned
      vlan 160
   !
   vlan-aware-bundle Tenant_A_WAN_Zone
      rd 65103:14
      route-target both 14:14
      redistribute learned
      vlan 150
   !
   vlan-aware-bundle Tenant_A_WEB_Zone
      rd 65103:11
      route-target both 11:11
      redistribute learned
      vlan 120-121
   !
   vlan-aware-bundle Tenant_B_OP_Zone
      rd 65103:20
      route-target both 20:20
      redistribute learned
      vlan 210-211
   !
   vlan-aware-bundle Tenant_B_WAN_Zone
      rd 65103:21
      route-target both 21:21
      redistribute learned
      vlan 250
   !
   vlan-aware-bundle Tenant_C_OP_Zone
      rd 65103:30
      route-target both 30:30
      redistribute learned
      vlan 310-311
   !
   vlan-aware-bundle Tenant_C_WAN_Zone
      rd 65103:31
      route-target both 31:31
      redistribute learned
      vlan 350
   !
   address-family evpn
      host-flap detection window 180 threshold 5 expiry timeout 10 seconds
      neighbor EVPN-OVERLAY-PEERS activate
   !
   address-family ipv4
      no neighbor EVPN-OVERLAY-PEERS activate
      neighbor MLAG-PEERS activate
      neighbor UNDERLAY-PEERS activate
   !
   vrf Tenant_A_APP_Zone
      rd 65103:12
      route-target import evpn 12:12
      route-target export evpn 12:12
      router-id 192.168.255.13
      neighbor 10.255.251.6 peer group MLAG-PEERS
      redistribute connected
   !
   vrf Tenant_A_DB_Zone
      rd 65103:13
      route-target import evpn 13:13
      route-target export evpn 13:13
      router-id 192.168.255.13
      neighbor 10.255.251.6 peer group MLAG-PEERS
      redistribute connected
   !
   vrf Tenant_A_OP_Zone
      rd 65103:9
      route-target import evpn 9:9
      route-target export evpn 9:9
      router-id 192.168.255.13
      neighbor 10.255.251.6 peer group MLAG-PEERS
      redistribute connected
   !
   vrf Tenant_A_WAN_Zone
      rd 65103:14
      route-target import evpn 14:14
      route-target import evpn 65000:456
      route-target export evpn 14:14
      route-target export evpn 65000:789
      router-id 192.168.255.13
      neighbor 10.255.251.6 peer group MLAG-PEERS
      redistribute connected
   !
   vrf Tenant_A_WEB_Zone
      rd 65103:11
      route-target import evpn 11:11
      route-target export evpn 11:11
      router-id 192.168.255.13
      neighbor 10.255.251.6 peer group MLAG-PEERS
      redistribute connected
   !
   vrf Tenant_B_OP_Zone
      rd 65103:20
      route-target import evpn 20:20
      route-target export evpn 20:20
      router-id 192.168.255.13
      neighbor 10.255.251.6 peer group MLAG-PEERS
      redistribute connected
   !
   vrf Tenant_B_WAN_Zone
      rd 65103:21
      route-target import evpn 21:21
      route-target export evpn 21:21
      router-id 192.168.255.13
      neighbor 10.255.251.6 peer group MLAG-PEERS
      redistribute connected
   !
   vrf Tenant_C_OP_Zone
      rd 65103:30
      route-target import evpn 30:30
      route-target export evpn 30:30
      router-id 192.168.255.13
      neighbor 10.255.251.6 peer group MLAG-PEERS
      redistribute connected
   !
   vrf Tenant_C_WAN_Zone
      rd 65103:31
      route-target import evpn 31:31
      route-target export evpn 31:31
      router-id 192.168.255.13
      neighbor 10.255.251.6 peer group MLAG-PEERS
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

#### RM-MLAG-PEER-IN

| Sequence | Type | Match and/or Set |
| -------- | ---- | ---------------- |
| 10 | permit | set origin incomplete |

### Route-maps Device Configuration

```eos
!
route-map RM-CONN-2-BGP permit 10
   match ip address prefix-list PL-LOOPBACKS-EVPN-OVERLAY
!
route-map RM-MLAG-PEER-IN permit 10
   description Make routes learned over MLAG Peer-link less preferred on spines to ensure optimal routing
   set origin incomplete
```

# ACL

# VRF Instances

## VRF Instances Summary

| VRF Name | IP Routing |
| -------- | ---------- |
| MGMT | disabled |
| Tenant_A_APP_Zone | enabled |
| Tenant_A_DB_Zone | enabled |
| Tenant_A_OP_Zone | enabled |
| Tenant_A_WAN_Zone | enabled |
| Tenant_A_WEB_Zone | enabled |
| Tenant_B_OP_Zone | enabled |
| Tenant_B_WAN_Zone | enabled |
| Tenant_C_OP_Zone | enabled |
| Tenant_C_WAN_Zone | enabled |

## VRF Instances Device Configuration

```eos
!
vrf instance MGMT
!
vrf instance Tenant_A_APP_Zone
!
vrf instance Tenant_A_DB_Zone
!
vrf instance Tenant_A_OP_Zone
   description Tenant_A_OP_Zone
!
vrf instance Tenant_A_WAN_Zone
!
vrf instance Tenant_A_WEB_Zone
!
vrf instance Tenant_B_OP_Zone
!
vrf instance Tenant_B_WAN_Zone
!
vrf instance Tenant_C_OP_Zone
!
vrf instance Tenant_C_WAN_Zone
```

# Virtual Source NAT

## Virtual Source NAT Summary

| Source NAT VRF | Source NAT IP Address |
| -------------- | --------------------- |
| Tenant_A_OP_Zone | 10.255.1.13 |

## Virtual Source NAT Configuration

```eos
!
ip address virtual source-nat vrf Tenant_A_OP_Zone address 10.255.1.13
```

# Quality Of Service
