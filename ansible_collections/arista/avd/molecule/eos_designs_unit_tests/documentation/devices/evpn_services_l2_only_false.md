# evpn_services_l2_only_false
# Table of Contents

- [Management](#management)
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
- [Internal VLAN Allocation Policy](#internal-vlan-allocation-policy)
  - [Internal VLAN Allocation Policy Summary](#internal-vlan-allocation-policy-summary)
  - [Internal VLAN Allocation Policy Configuration](#internal-vlan-allocation-policy-configuration)
- [VLANs](#vlans)
  - [VLANs Summary](#vlans-summary)
  - [VLANs Device Configuration](#vlans-device-configuration)
- [Interfaces](#interfaces)
  - [Loopback Interfaces](#loopback-interfaces)
  - [VLAN Interfaces](#vlan-interfaces)
  - [VXLAN Interface](#vxlan-interface)
- [Routing](#routing)
  - [Service Routing Protocols Model](#service-routing-protocols-model)
  - [Virtual Router MAC Address](#virtual-router-mac-address)
  - [IP Routing](#ip-routing)
  - [IPv6 Routing](#ipv6-routing)
  - [Static Routes](#static-routes)
  - [IPv6 Static Routes](#ipv6-static-routes)
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
| example@example.com | EOS_DESIGNS_UNIT_TESTS evpn_services_l2_only_false | All | Disabled |

### SNMP Device Configuration

```eos
!
snmp-server contact example@example.com
snmp-server location EOS_DESIGNS_UNIT_TESTS evpn_services_l2_only_false
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
| 110 | Tenant_A_OP_Zone_1 | - |
| 111 | Tenant_A_OP_Zone_2 | - |
| 112 | Tenant_A_OP_Zone_3 | - |
| 120 | Tenant_A_WEB_Zone_1 | - |
| 121 | Tenant_A_WEBZone_2 | - |
| 130 | Tenant_A_APP_Zone_1 | - |
| 131 | Tenant_A_APP_Zone_2 | - |
| 132 | Tenant_A_APP_Zone_3 | - |
| 140 | Tenant_A_DB_BZone_1 | - |
| 141 | Tenant_A_DB_Zone_2 | - |
| 150 | Tenant_A_WAN_Zone_1 | - |
| 151 | svi_with_no_tags | - |
| 160 | Tenant_A_VMOTION | - |
| 161 | Tenant_A_NFS | - |
| 162 | l2vlan_with_no_tags | - |
| 210 | Tenant_B_OP_Zone_1 | - |
| 211 | Tenant_B_OP_Zone_2 | - |
| 250 | Tenant_B_WAN_Zone_1 | - |
| 310 | Tenant_C_OP_Zone_1 | - |
| 311 | Tenant_C_OP_Zone_2 | - |
| 350 | Tenant_C_WAN_Zone_1 | - |
| 410 | Tenant_D_v6_OP_Zone_1 | - |
| 411 | Tenant_D_v6_OP_Zone_2 | - |
| 412 | Tenant_D_v6_OP_Zone_1 | - |
| 450 | Tenant_D_v6_WAN_Zone_1 | - |
| 451 | Tenant_D_v6_WAN_Zone_2 | - |
| 452 | Tenant_D_v6_WAN_Zone_3 | - |

## VLANs Device Configuration

```eos
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
vlan 132
   name Tenant_A_APP_Zone_3
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
vlan 151
   name svi_with_no_tags
!
vlan 160
   name Tenant_A_VMOTION
!
vlan 161
   name Tenant_A_NFS
!
vlan 162
   name l2vlan_with_no_tags
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
vlan 410
   name Tenant_D_v6_OP_Zone_1
!
vlan 411
   name Tenant_D_v6_OP_Zone_2
!
vlan 412
   name Tenant_D_v6_OP_Zone_1
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

## Loopback Interfaces

### Loopback Interfaces Summary

#### IPv4

| Interface | Description | VRF | IP Address |
| --------- | ----------- | --- | ---------- |
| Loopback0 | EVPN_Overlay_Peering | default | 192.168.255.109/32 |
| Loopback1 | VTEP_VXLAN_Tunnel_Source | default | 192.168.254.109/32 |
| Loopback100 | Tenant_A_OP_Zone_VTEP_DIAGNOSTICS | Tenant_A_OP_Zone | 10.255.1.109/32 |

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
   ip address 192.168.255.109/32
!
interface Loopback1
   description VTEP_VXLAN_Tunnel_Source
   no shutdown
   ip address 192.168.254.109/32
!
interface Loopback100
   description Tenant_A_OP_Zone_VTEP_DIAGNOSTICS
   no shutdown
   vrf Tenant_A_OP_Zone
   ip address 10.255.1.109/32
```

## VLAN Interfaces

### VLAN Interfaces Summary

| Interface | Description | VRF |  MTU | Shutdown |
| --------- | ----------- | --- | ---- | -------- |
| Vlan110 | Tenant_A_OP_Zone_1 | Tenant_A_OP_Zone | - | false |
| Vlan111 | Tenant_A_OP_Zone_2 | Tenant_A_OP_Zone | - | false |
| Vlan112 | Tenant_A_OP_Zone_3 | Tenant_A_OP_Zone | 1560 | false |
| Vlan120 | Tenant_A_WEB_Zone_1 | Tenant_A_WEB_Zone | - | false |
| Vlan121 | Tenant_A_WEBZone_2 | Tenant_A_WEB_Zone | 1560 | true |
| Vlan130 | Tenant_A_APP_Zone_1 | Tenant_A_APP_Zone | - | false |
| Vlan131 | Tenant_A_APP_Zone_2 | Tenant_A_APP_Zone | - | false |
| Vlan132 | Tenant_A_APP_Zone_3 | Tenant_A_APP_Zone | - | false |
| Vlan140 | Tenant_A_DB_BZone_1 | Tenant_A_DB_Zone | - | false |
| Vlan141 | Tenant_A_DB_Zone_2 | Tenant_A_DB_Zone | - | false |
| Vlan150 | Tenant_A_WAN_Zone_1 | Tenant_A_WAN_Zone | - | false |
| Vlan151 | svi_with_no_tags | Tenant_A_WAN_Zone | - | false |
| Vlan210 | Tenant_B_OP_Zone_1 | Tenant_B_OP_Zone | - | false |
| Vlan211 | Tenant_B_OP_Zone_2 | Tenant_B_OP_Zone | - | false |
| Vlan250 | Tenant_B_WAN_Zone_1 | Tenant_B_WAN_Zone | - | false |
| Vlan310 | Tenant_C_OP_Zone_1 | Tenant_C_OP_Zone | - | false |
| Vlan311 | Tenant_C_OP_Zone_2 | Tenant_C_OP_Zone | - | false |
| Vlan350 | Tenant_C_WAN_Zone_1 | Tenant_C_WAN_Zone | - | false |
| Vlan410 | Tenant_D_v6_OP_Zone_1 | Tenant_D_OP_Zone | - | false |
| Vlan411 | Tenant_D_v6_OP_Zone_2 | Tenant_D_OP_Zone | - | false |
| Vlan412 | Tenant_D_v6_OP_Zone_1 | Tenant_D_OP_Zone | 1560 | false |
| Vlan450 | Tenant_D_v6_WAN_Zone_1 | Tenant_D_WAN_Zone | - | false |
| Vlan451 | Tenant_D_v6_WAN_Zone_2 | Tenant_D_WAN_Zone | 1560 | false |
| Vlan452 | Tenant_D_v6_WAN_Zone_3 | Tenant_D_WAN_Zone | 1560 | false |

#### IPv4

| Interface | VRF | IP Address | IP Address Virtual | IP Router Virtual Address | VRRP | ACL In | ACL Out |
| --------- | --- | ---------- | ------------------ | ------------------------- | ---- | ------ | ------- |
| Vlan110 |  Tenant_A_OP_Zone  |  -  |  10.1.10.1/24  |  -  |  -  |  -  |  -  |
| Vlan111 |  Tenant_A_OP_Zone  |  -  |  10.1.11.1/24  |  -  |  -  |  -  |  -  |
| Vlan112 |  Tenant_A_OP_Zone  |  -  |  -  |  -  |  -  |  -  |  -  |
| Vlan120 |  Tenant_A_WEB_Zone  |  -  |  10.1.20.1/24  |  -  |  -  |  -  |  -  |
| Vlan121 |  Tenant_A_WEB_Zone  |  -  |  10.1.10.254/24  |  -  |  -  |  -  |  -  |
| Vlan130 |  Tenant_A_APP_Zone  |  -  |  10.1.30.1/24  |  -  |  -  |  -  |  -  |
| Vlan131 |  Tenant_A_APP_Zone  |  -  |  10.1.31.1/24  |  -  |  -  |  -  |  -  |
| Vlan132 |  Tenant_A_APP_Zone  |  -  |  -  |  10.1.32.254, 10.2.32.254/24, 10.3.32.254/24  |  -  |  -  |  -  |
| Vlan140 |  Tenant_A_DB_Zone  |  -  |  10.1.40.1/24  |  -  |  -  |  -  |  -  |
| Vlan141 |  Tenant_A_DB_Zone  |  -  |  10.1.41.1/24  |  -  |  -  |  -  |  -  |
| Vlan150 |  Tenant_A_WAN_Zone  |  -  |  10.1.40.1/24  |  -  |  -  |  -  |  -  |
| Vlan151 |  Tenant_A_WAN_Zone  |  -  |  10.1.51.1/24  |  -  |  -  |  -  |  -  |
| Vlan210 |  Tenant_B_OP_Zone  |  -  |  10.2.10.1/24  |  -  |  -  |  -  |  -  |
| Vlan211 |  Tenant_B_OP_Zone  |  -  |  10.2.11.1/24  |  -  |  -  |  -  |  -  |
| Vlan250 |  Tenant_B_WAN_Zone  |  -  |  10.2.50.1/24  |  -  |  -  |  -  |  -  |
| Vlan310 |  Tenant_C_OP_Zone  |  -  |  10.3.10.1/24  |  -  |  -  |  -  |  -  |
| Vlan311 |  Tenant_C_OP_Zone  |  -  |  10.3.11.1/24  |  -  |  -  |  -  |  -  |
| Vlan350 |  Tenant_C_WAN_Zone  |  -  |  10.3.50.1/24  |  -  |  -  |  -  |  -  |
| Vlan410 |  Tenant_D_OP_Zone  |  -  |  10.3.10.1/24  |  -  |  -  |  -  |  -  |
| Vlan411 |  Tenant_D_OP_Zone  |  -  |  -  |  10.3.11.1/24  |  -  |  -  |  -  |
| Vlan412 |  Tenant_D_OP_Zone  |  -  |  10.4.12.254/24  |  -  |  -  |  -  |  -  |
| Vlan450 |  Tenant_D_WAN_Zone  |  -  |  -  |  -  |  -  |  -  |  -  |
| Vlan451 |  Tenant_D_WAN_Zone  |  -  |  -  |  -  |  -  |  -  |  -  |
| Vlan452 |  Tenant_D_WAN_Zone  |  -  |  10.4.12.254/24  |  -  |  -  |  -  |  -  |

#### IPv6

| Interface | VRF | IPv6 Address | IPv6 Virtual Address | Virtual Router Address | VRRP | ND RA Disabled | Managed Config Flag | IPv6 ACL In | IPv6 ACL Out |
| --------- | --- | ------------ | -------------------- | ---------------------- | ---- | -------------- | ------------------- | ----------- | ------------ |
| Vlan410 | Tenant_D_OP_Zone | - | 2001:db8:310::1/64 | - | - | - | - | - | - |
| Vlan412 | Tenant_D_OP_Zone | - | 2001:db8:412::1/64 | - | - | - | - | - | - |
| Vlan450 | Tenant_D_WAN_Zone | - | 2001:db8:355::1/64 | - | - | - | - | - | - |
| Vlan451 | Tenant_D_WAN_Zone | - | 2001:db8:451::1/64 | - | - | - | - | - | - |
| Vlan452 | Tenant_D_WAN_Zone | - | 2001:db8:412::1/64 | - | - | - | - | - | - |

### VLAN Interfaces Device Configuration

```eos
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
interface Vlan132
   description Tenant_A_APP_Zone_3
   no shutdown
   vrf Tenant_A_APP_Zone
   ip virtual-router address 10.1.32.254
   ip virtual-router address 10.2.32.254/24
   ip virtual-router address 10.3.32.254/24
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
interface Vlan151
   description svi_with_no_tags
   no shutdown
   vrf Tenant_A_WAN_Zone
   ip address virtual 10.1.51.1/24
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
interface Vlan410
   description Tenant_D_v6_OP_Zone_1
   no shutdown
   vrf Tenant_D_OP_Zone
   ipv6 address virtual 2001:db8:310::1/64
   ip address virtual 10.3.10.1/24
!
interface Vlan411
   description Tenant_D_v6_OP_Zone_2
   no shutdown
   vrf Tenant_D_OP_Zone
   ipv6 virtual-router address 2001:db8:311::1/64
   ip virtual-router address 10.3.11.1/24
!
interface Vlan412
   description Tenant_D_v6_OP_Zone_1
   no shutdown
   mtu 1560
   vrf Tenant_D_OP_Zone
   ipv6 address virtual 2001:db8:412::1/64
   ip address virtual 10.4.12.254/24
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
| 110 | 10110 | - | - |
| 111 | 50111 | - | - |
| 112 | 10112 | - | - |
| 120 | 10120 | - | - |
| 121 | 10121 | - | - |
| 130 | 10130 | - | - |
| 131 | 10131 | - | - |
| 132 | 10132 | - | - |
| 140 | 10140 | - | - |
| 141 | 10141 | - | - |
| 150 | 10150 | - | - |
| 151 | 10151 | - | - |
| 160 | 10160 | - | - |
| 161 | 10161 | - | - |
| 162 | 10162 | - | - |
| 210 | 20210 | - | - |
| 211 | 20211 | - | - |
| 250 | 20250 | - | - |
| 310 | 30310 | - | - |
| 311 | 30311 | - | - |
| 350 | 30350 | - | - |
| 410 | 40410 | - | - |
| 411 | 40411 | - | - |
| 412 | 40412 | - | - |
| 450 | 40450 | - | - |
| 451 | 40451 | - | - |
| 452 | 40452 | - | - |

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
| Tenant_D_OP_Zone | 40 | - |
| Tenant_D_WAN_Zone | 41 | - |

### VXLAN Interface Device Configuration

```eos
!
interface Vxlan1
   description evpn_services_l2_only_false_VTEP
   vxlan source-interface Loopback1
   vxlan udp-port 4789
   vxlan vlan 110 vni 10110
   vxlan vlan 111 vni 50111
   vxlan vlan 112 vni 10112
   vxlan vlan 120 vni 10120
   vxlan vlan 121 vni 10121
   vxlan vlan 130 vni 10130
   vxlan vlan 131 vni 10131
   vxlan vlan 132 vni 10132
   vxlan vlan 140 vni 10140
   vxlan vlan 141 vni 10141
   vxlan vlan 150 vni 10150
   vxlan vlan 151 vni 10151
   vxlan vlan 160 vni 10160
   vxlan vlan 161 vni 10161
   vxlan vlan 162 vni 10162
   vxlan vlan 210 vni 20210
   vxlan vlan 211 vni 20211
   vxlan vlan 250 vni 20250
   vxlan vlan 310 vni 30310
   vxlan vlan 311 vni 30311
   vxlan vlan 350 vni 30350
   vxlan vlan 410 vni 40410
   vxlan vlan 411 vni 40411
   vxlan vlan 412 vni 40412
   vxlan vlan 450 vni 40450
   vxlan vlan 451 vni 40451
   vxlan vlan 452 vni 40452
   vxlan vrf Tenant_A_APP_Zone vni 12
   vxlan vrf Tenant_A_DB_Zone vni 13
   vxlan vrf Tenant_A_OP_Zone vni 10
   vxlan vrf Tenant_A_WAN_Zone vni 14
   vxlan vrf Tenant_A_WEB_Zone vni 11
   vxlan vrf Tenant_B_OP_Zone vni 20
   vxlan vrf Tenant_B_WAN_Zone vni 21
   vxlan vrf Tenant_C_OP_Zone vni 30
   vxlan vrf Tenant_C_WAN_Zone vni 31
   vxlan vrf Tenant_D_OP_Zone vni 40
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
| Tenant_A_DB_Zone | true |
| Tenant_A_OP_Zone | true |
| Tenant_A_WAN_Zone | true |
| Tenant_A_WEB_Zone | true |
| Tenant_B_OP_Zone | true |
| Tenant_B_WAN_Zone | true |
| Tenant_C_OP_Zone | true |
| Tenant_C_WAN_Zone | true |
| Tenant_D_OP_Zone | true |
| Tenant_D_WAN_Zone | true |

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
ip routing vrf Tenant_D_OP_Zone
ip routing vrf Tenant_D_WAN_Zone
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
| Tenant_D_OP_Zone | true |
| Tenant_D_WAN_Zone | true |

## Static Routes

### Static Routes Summary

| VRF | Destination Prefix | Next Hop IP             | Exit interface      | Administrative Distance       | Tag               | Route Name                    | Metric         |
| --- | ------------------ | ----------------------- | ------------------- | ----------------------------- | ----------------- | ----------------------------- | -------------- |
| MGMT | 0.0.0.0/0 | 192.168.200.5 | - | 1 | - | - | - |
| Tenant_A_APP_Zone | 10.2.32.0/24 | - | Vlan132 | 1 | - | VARP | - |
| Tenant_A_APP_Zone | 10.3.32.0/24 | - | Vlan132 | 1 | - | VARP | - |
| Tenant_D_OP_Zone | 10.3.11.0/24 | - | Vlan411 | 1 | - | VARP | - |

### Static Routes Device Configuration

```eos
!
ip route vrf MGMT 0.0.0.0/0 192.168.200.5
ip route vrf Tenant_A_APP_Zone 10.2.32.0/24 Vlan132 name VARP
ip route vrf Tenant_A_APP_Zone 10.3.32.0/24 Vlan132 name VARP
ip route vrf Tenant_D_OP_Zone 10.3.11.0/24 Vlan411 name VARP
```

## IPv6 Static Routes

### IPv6 Static Routes Summary

| VRF | Destination Prefix | Next Hop IP             | Exit interface      | Administrative Distance       | Tag               | Route Name                    | Metric         |
| --- | ------------------ | ----------------------- | ------------------- | ----------------------------- | ----------------- | ----------------------------- | -------------- |
| Tenant_D_OP_Zone | 2001:db8:311::/64 | - | Vlan411 | 1 | - | VARPv6 | - |

### Static Routes Device Configuration

```eos
!
ipv6 route vrf Tenant_D_OP_Zone 2001:db8:311::/64 Vlan411 name VARPv6
```

## Router BGP

### Router BGP Summary

| BGP AS | Router ID |
| ------ | --------- |
| 101|  192.168.255.109 |

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
| l2vlan_with_no_tags | 192.168.255.109:20162 | 20162:20162 | - | - | learned | 162 |
| Tenant_A_APP_Zone | 192.168.255.109:12 | 12:12 | - | - | learned | 130-132 |
| Tenant_A_DB_Zone | 192.168.255.109:13 | 13:13 | - | - | learned | 140-141 |
| Tenant_A_NFS | 192.168.255.109:20161 | 20161:20161 | - | - | learned | 161 |
| Tenant_A_OP_Zone | 192.168.255.109:9 | 9:9 | - | - | learned | 110-112 |
| Tenant_A_VMOTION | 192.168.255.109:20160 | 20160:20160 | - | - | learned | 160 |
| Tenant_A_WAN_Zone | 192.168.255.109:14 | 14:14 | - | - | learned | 150-151 |
| Tenant_A_WEB_Zone | 192.168.255.109:11 | 11:11 | - | - | learned | 120-121 |
| Tenant_B_OP_Zone | 192.168.255.109:20 | 20:20 | - | - | learned | 210-211 |
| Tenant_B_WAN_Zone | 192.168.255.109:21 | 21:21 | - | - | learned | 250 |
| Tenant_C_OP_Zone | 192.168.255.109:30 | 30:30 | - | - | learned | 310-311 |
| Tenant_C_WAN_Zone | 192.168.255.109:31 | 31:31 | - | - | learned | 350 |
| Tenant_D_OP_Zone | 192.168.255.109:40 | 40:40 | - | - | learned | 410-412 |
| Tenant_D_WAN_Zone | 192.168.255.109:41 | 41:41 | - | - | learned | 450-452 |

### Router BGP VRFs

| VRF | Route-Distinguisher | Redistribute |
| --- | ------------------- | ------------ |
| Tenant_A_APP_Zone | 192.168.255.109:12 | connected |
| Tenant_A_DB_Zone | 192.168.255.109:13 | connected |
| Tenant_A_OP_Zone | 192.168.255.109:9 | connected |
| Tenant_A_WAN_Zone | 192.168.255.109:14 | connected |
| Tenant_A_WEB_Zone | 192.168.255.109:11 | connected |
| Tenant_B_OP_Zone | 192.168.255.109:20 | connected |
| Tenant_B_WAN_Zone | 192.168.255.109:21 | connected |
| Tenant_C_OP_Zone | 192.168.255.109:30 | connected |
| Tenant_C_WAN_Zone | 192.168.255.109:31 | connected |
| Tenant_D_OP_Zone | 192.168.255.109:40 | connected |
| Tenant_D_WAN_Zone | 192.168.255.109:41 | connected |

### Router BGP Device Configuration

```eos
!
router bgp 101
   router-id 192.168.255.109
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
   redistribute connected route-map RM-CONN-2-BGP
   !
   vlan-aware-bundle l2vlan_with_no_tags
      rd 192.168.255.109:20162
      route-target both 20162:20162
      redistribute learned
      vlan 162
   !
   vlan-aware-bundle Tenant_A_APP_Zone
      rd 192.168.255.109:12
      route-target both 12:12
      redistribute learned
      vlan 130-132
   !
   vlan-aware-bundle Tenant_A_DB_Zone
      rd 192.168.255.109:13
      route-target both 13:13
      redistribute learned
      vlan 140-141
   !
   vlan-aware-bundle Tenant_A_NFS
      rd 192.168.255.109:20161
      route-target both 20161:20161
      redistribute learned
      vlan 161
   !
   vlan-aware-bundle Tenant_A_OP_Zone
      rd 192.168.255.109:9
      route-target both 9:9
      redistribute learned
      vlan 110-112
   !
   vlan-aware-bundle Tenant_A_VMOTION
      rd 192.168.255.109:20160
      route-target both 20160:20160
      redistribute learned
      vlan 160
   !
   vlan-aware-bundle Tenant_A_WAN_Zone
      rd 192.168.255.109:14
      route-target both 14:14
      redistribute learned
      vlan 150-151
   !
   vlan-aware-bundle Tenant_A_WEB_Zone
      rd 192.168.255.109:11
      route-target both 11:11
      redistribute learned
      vlan 120-121
   !
   vlan-aware-bundle Tenant_B_OP_Zone
      rd 192.168.255.109:20
      route-target both 20:20
      redistribute learned
      vlan 210-211
   !
   vlan-aware-bundle Tenant_B_WAN_Zone
      rd 192.168.255.109:21
      route-target both 21:21
      redistribute learned
      vlan 250
   !
   vlan-aware-bundle Tenant_C_OP_Zone
      rd 192.168.255.109:30
      route-target both 30:30
      redistribute learned
      vlan 310-311
   !
   vlan-aware-bundle Tenant_C_WAN_Zone
      rd 192.168.255.109:31
      route-target both 31:31
      redistribute learned
      vlan 350
   !
   vlan-aware-bundle Tenant_D_OP_Zone
      rd 192.168.255.109:40
      route-target both 40:40
      redistribute learned
      vlan 410-412
   !
   vlan-aware-bundle Tenant_D_WAN_Zone
      rd 192.168.255.109:41
      route-target both 41:41
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
      rd 192.168.255.109:12
      route-target import evpn 12:12
      route-target export evpn 12:12
      router-id 192.168.255.109
      redistribute connected
   !
   vrf Tenant_A_DB_Zone
      rd 192.168.255.109:13
      route-target import evpn 13:13
      route-target export evpn 13:13
      router-id 192.168.255.109
      redistribute connected
   !
   vrf Tenant_A_OP_Zone
      rd 192.168.255.109:9
      route-target import evpn 9:9
      route-target export evpn 9:9
      router-id 192.168.255.109
      redistribute connected
   !
   vrf Tenant_A_WAN_Zone
      rd 192.168.255.109:14
      route-target import evpn 14:14
      route-target import evpn 65000:456
      route-target export evpn 14:14
      route-target export evpn 65000:789
      router-id 192.168.255.109
      redistribute connected
   !
   vrf Tenant_A_WEB_Zone
      rd 192.168.255.109:11
      route-target import evpn 11:11
      route-target export evpn 11:11
      router-id 192.168.255.109
      redistribute connected
   !
   vrf Tenant_B_OP_Zone
      rd 192.168.255.109:20
      route-target import evpn 20:20
      route-target export evpn 20:20
      router-id 192.168.255.109
      redistribute connected
   !
   vrf Tenant_B_WAN_Zone
      rd 192.168.255.109:21
      route-target import evpn 21:21
      route-target export evpn 21:21
      router-id 192.168.255.109
      redistribute connected
   !
   vrf Tenant_C_OP_Zone
      rd 192.168.255.109:30
      route-target import evpn 30:30
      route-target export evpn 30:30
      router-id 192.168.255.109
      redistribute connected
   !
   vrf Tenant_C_WAN_Zone
      rd 192.168.255.109:31
      route-target import evpn 31:31
      route-target export evpn 31:31
      router-id 192.168.255.109
      redistribute connected
   !
   vrf Tenant_D_OP_Zone
      rd 192.168.255.109:40
      route-target import evpn 40:40
      route-target export evpn 40:40
      router-id 192.168.255.109
      redistribute connected
   !
   vrf Tenant_D_WAN_Zone
      rd 192.168.255.109:41
      route-target import evpn 41:41
      route-target export evpn 41:41
      router-id 192.168.255.109
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
| Tenant_A_DB_Zone | enabled |
| Tenant_A_OP_Zone | enabled |
| Tenant_A_WAN_Zone | enabled |
| Tenant_A_WEB_Zone | enabled |
| Tenant_B_OP_Zone | enabled |
| Tenant_B_WAN_Zone | enabled |
| Tenant_C_OP_Zone | enabled |
| Tenant_C_WAN_Zone | enabled |
| Tenant_D_OP_Zone | enabled |
| Tenant_D_WAN_Zone | enabled |

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
!
vrf instance Tenant_D_OP_Zone
!
vrf instance Tenant_D_WAN_Zone
```

# Virtual Source NAT

## Virtual Source NAT Summary

| Source NAT VRF | Source NAT IP Address |
| -------------- | --------------------- |
| Tenant_A_OP_Zone | 10.255.1.109 |

## Virtual Source NAT Configuration

```eos
!
ip address virtual source-nat vrf Tenant_A_OP_Zone address 10.255.1.109
```

# Quality Of Service
