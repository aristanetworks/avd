# host1

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
  - [IP Name Servers](#ip-name-servers)
  - [Domain Lookup](#domain-lookup)
  - [Management SSH](#management-ssh)
  - [Management API gNMI](#management-api-gnmi)
  - [Management API HTTP](#management-api-http)
- [Authentication](#authentication)
  - [Local Users](#local-users)
  - [RADIUS Server](#radius-server)
- [Monitoring](#monitoring)
  - [TerminAttr Daemon](#terminattr-daemon)
  - [Custom daemons](#custom-daemons)
  - [Logging](#logging)
  - [SNMP](#snmp)
  - [SFlow](#sflow)
  - [VM Tracer Sessions](#vm-tracer-sessions)
  - [Event Handler](#event-handler)
  - [Flow Tracking](#flow-tracking)
- [Hardware TCAM Profile](#hardware-tcam-profile)
  - [Custom TCAM profiles](#custom-tcam-profiles)
  - [Hardware TCAM configuration](#hardware-tcam-configuration)
- [Spanning Tree](#spanning-tree)
  - [Spanning Tree Summary](#spanning-tree-summary)
  - [Spanning Tree Device Configuration](#spanning-tree-device-configuration)
- [VLANs](#vlans)
  - [VLANs Summary](#vlans-summary)
  - [VLANs Device Configuration](#vlans-device-configuration)
- [Interfaces](#interfaces)
  - [Interface Profiles](#interface-profiles)
  - [Ethernet Interfaces](#ethernet-interfaces)
  - [Port-Channel Interfaces](#port-channel-interfaces)
  - [Loopback Interfaces](#loopback-interfaces)
  - [Tunnel Interfaces](#tunnel-interfaces)
  - [VLAN Interfaces](#vlan-interfaces)
  - [VXLAN Interface](#vxlan-interface)
- [Routing](#routing)
  - [IP Routing](#ip-routing)
  - [IPv6 Routing](#ipv6-routing)
  - [Router General](#router-general)
  - [Router OSPF](#router-ospf)
  - [Router ISIS](#router-isis)
  - [Router BGP](#router-bgp)
  - [PBR Policy Maps](#pbr-policy-maps)
- [Multicast](#multicast)
  - [IP IGMP Snooping](#ip-igmp-snooping)
  - [PIM Sparse Mode](#pim-sparse-mode)
- [Filters](#filters)
  - [Community-lists](#community-lists)
  - [Peer Filters](#peer-filters)
  - [Prefix-lists](#prefix-lists)
  - [IPv6 Prefix-lists](#ipv6-prefix-lists)
  - [Route-maps](#route-maps)
  - [IP Extended Community Lists](#ip-extended-community-lists)
  - [IP Extended Community RegExp Lists](#ip-extended-community-regexp-lists)
  - [Match-lists](#match-lists)
- [802.1X Port Security](#8021x-port-security)
  - [802.1X Summary](#8021x-summary)
- [ACL](#acl)
  - [Standard Access-lists](#standard-access-lists)
  - [Extended Access-lists](#extended-access-lists)
  - [IPv6 Standard Access-lists](#ipv6-standard-access-lists)
  - [IPv6 Extended Access-lists](#ipv6-extended-access-lists)
- [VRF Instances](#vrf-instances)
  - [VRF Instances Summary](#vrf-instances-summary)
  - [VRF Instances Device Configuration](#vrf-instances-device-configuration)
- [Virtual Source NAT](#virtual-source-nat)
  - [Virtual Source NAT Summary](#virtual-source-nat-summary)
  - [Virtual Source NAT Configuration](#virtual-source-nat-configuration)
- [MACsec](#macsec)
  - [MACsec Summary](#macsec-summary)
  - [MACsec Device Configuration](#macsec-device-configuration)
  - [Traffic Policies information](#traffic-policies-information)
- [Quality Of Service](#quality-of-service)
  - [QOS Class Maps](#qos-class-maps)
  - [QOS Policy Maps](#qos-policy-maps)
  - [QOS Profiles](#qos-profiles)
- [STUN](#stun)
  - [STUN Server](#stun-server)
  - [STUN Device Configuration](#stun-device-configuration)
- [Maintenance Mode](#maintenance-mode)
  - [BGP Groups](#bgp-groups)
  - [Interface Groups](#interface-groups)
  - [Maintenance](#maintenance)

## Management

### Management Interfaces

#### Management Interfaces Summary

##### IPv4

| Management Interface | description | Type | VRF | IP Address | Gateway |
| -------------------- | ----------- | ---- | --- | ---------- | ------- |
| Management1 | oob_management | oob | MGMT | 10.73.255.122/24 | 10.73.255.2 |

##### IPv6

| Management Interface | description | Type | VRF | IPv6 Address | IPv6 Gateway |
| -------------------- | ----------- | ---- | --- | ------------ | ------------ |
| Management1 | oob_management | oob | MGMT | - | - |

#### Management Interfaces Device Configuration

```eos
!
interface Management1
   description oob_management
   vrf MGMT
   ip address 10.73.255.122/24
```

### IP Name Servers

#### IP Name Servers Summary

| Name Server | VRF | Priority |
| ----------- | --- | -------- |
| 10.10.128.10 | mgt | - |
| 10.10.129.10 | mgt | - |

#### IP Name Servers Device Configuration

```eos
ip name-server vrf mgt 10.10.128.10
ip name-server vrf mgt 10.10.129.10
```

### Domain Lookup

#### DNS Domain Lookup Summary

| Source interface | vrf |
| ---------------- | --- |
| Loopback0 | - |
| Management0 | mgt |

#### DNS Domain Lookup Device Configuration

```eos
ip domain lookup source-interface Loopback0
ip domain lookup vrf mgt source-interface Management0
```

### Management SSH


#### SSH timeout and management

| Idle Timeout | SSH Management |
| ------------ | -------------- |
| default | Enabled |

#### Max number of SSH sessions limit and per-host limit

| Connection Limit | Max from a single Host |
| ---------------- | ---------------------- |
| - | - |

#### Ciphers and algorithms

| Ciphers | Key-exchange methods | MAC algorithms | Hostkey server algorithms |
|---------|----------------------|----------------|---------------------------|
| default | default | default | default |

#### VRFs

| VRF | Status |
| --- | ------ |
| mgt | Enabled |

#### Management SSH Configuration

```eos
!
management ssh
   !
   vrf mgt
      no shutdown
```

### Management API gNMI

#### Management API gNMI Summary

| VRF with gNMI | OCTA |
| ------------- | ---- |
| MGMT | enabled |
| MONITORING | enabled |

#### Management API gNMI configuration

```eos
!
management api gnmi
   transport grpc MGMT
      ip access-group ACL-GNMI
      vrf MGMT
   transport grpc MONITORING
      vrf MONITORING
   provider eos-native
```

### Management API HTTP

#### Management API HTTP Summary

| HTTP | HTTPS | Default Services |
| ---- | ----- | ---------------- |
| False | True | - |

#### Management API VRF Access

| VRF Name | IPv4 ACL | IPv6 ACL |
| -------- | -------- | -------- |
| mgt | ACL-API | - |

#### Management API HTTP Configuration

```eos
!
management api http-commands
   no shutdown
   !
   vrf mgt
      no shutdown
      ip access-group ACL-API
```

## Authentication

### Local Users

#### Local Users Summary

| User | Privilege | Role | Disabled | Shell |
| ---- | --------- | ---- | -------- | ----- |
| admin | 15 | network-admin | False | - |

#### Local Users Device Configuration

```eos
!
username admin privilege 15 role network-admin nopassword
```

### RADIUS Server

#### RADIUS Server Hosts

| VRF | RADIUS Servers | Timeout | Retransmit |
| --- | -------------- | ------- | ---------- |
| mgt | 10.10.10.157 | - | - |
| default | 10.10.10.249 | - | - |
| default | 10.10.10.158 | - | - |

#### RADIUS Server Device Configuration

```eos
!
radius-server host 10.10.10.157 vrf mgt key 7 <removed>
radius-server host 10.10.10.249 key 7 <removed>
radius-server host 10.10.10.158 key 7 <removed>
```

## Monitoring

### TerminAttr Daemon

#### TerminAttr Daemon Summary

| CV Compression | CloudVision Servers | VRF | Authentication | Smash Excludes | Ingest Exclude | Bypass AAA |
| -------------- | ------------------- | --- | -------------- | -------------- | -------------- | ---------- |
| gzip | 10.20.20.1:9910 | mgt | key,<removed> | - | - | False |
| gzip | 10.30.30.1:9910 | mgt | token,/tmp/tokenDC2 | - | - | False |

#### TerminAttr Daemon Device Configuration

```eos
!
daemon TerminAttr
   exec /usr/bin/TerminAttr -cvopt DC1.addr=10.20.20.1:9910 -cvopt DC1.auth=key,<removed> -cvopt DC1.vrf=mgt -cvopt DC2.addr=10.30.30.1:9910 -cvopt DC2.auth=token,/tmp/tokenDC2 -cvopt DC2.vrf=mgt -taillogs
   no shutdown
```

### Custom daemons

#### Custom Daemons Device Configuration

```eos
!
daemon ocprometheus
   exec /usr/bin/ocprometheus -config /usr/bin/ocprometheus.yml -addr localhost:6042
   no shutdown
!
daemon random
   exec /usr/bin/random
   shutdown
```

### Logging

#### Logging Servers and Features Summary

| Type | Level |
| -----| ----- |

| VRF | Source Interface |
| --- | ---------------- |
| mgt | Management0 |

| VRF | Hosts | Ports | Protocol |
| --- | ----- | ----- | -------- |
| mgt | 10.10.10.7 | Default | UDP |
| mgt | 30.30.30.7 | 100, 200 | TCP |
| mgt | 40.40.40.7 | 300, 400 | UDP |

#### Logging Servers and Features Device Configuration

```eos
!
logging vrf mgt host 10.10.10.7
logging vrf mgt host 30.30.30.7 100 200 protocol tcp
logging vrf mgt host 40.40.40.7 300 400
logging vrf mgt source-interface Management0
logging policy match match-list molecule discard
```

### SNMP

#### SNMP Configuration Summary

| Contact | Location | SNMP Traps | State |
| ------- | -------- | ---------- | ----- |
| - | - | All | Disabled |

#### SNMP Local Interfaces

| Local Interface | VRF |
| --------------- | --- |
| Management1 | MGMT |
| Loopback0 | default |
| Loopback12 | Tenant_A_APP_Zone |

#### SNMP Views Configuration

| View | MIB Family Name | Status |
| ---- | --------------- | ------ |
| VW-WRITE | iso | Included |

#### SNMP Communities

| Community | Access | Access List IPv4 | Access List IPv6 | View |
| --------- | ------ | ---------------- | ---------------- | ---- |
| <removed> | ro | onur | - | - |
| <removed> | rw | SNMP-MGMT | SNMP-MGMT | VW-READ |
| <removed> | ro | - | - | - |

#### SNMP Device Configuration

```eos
!
snmp-server vrf MGMT local-interface Management1
snmp-server local-interface Loopback0
snmp-server vrf Tenant_A_APP_Zone local-interface Loopback12
snmp-server view VW-WRITE iso included
snmp-server community <removed> ro onur
snmp-server community <removed> view VW-READ rw ipv6 SNMP-MGMT SNMP-MGMT
snmp-server community <removed> ro
```

### SFlow

#### SFlow Summary

| VRF | SFlow Source | SFlow Destination | Port |
| --- | ------------ | ----------------- | ---- |
| MGMT | - | 10.6.75.59 | 6343 |
| MGMT | - | 10.6.75.62 | 123 |
| MGMT | Ethernet3 | - | - |
| default | - | 10.6.75.62 | 123 |
| default | - | 10.6.75.61 | 6343 |

sFlow is disabled.

#### SFlow Device Configuration

```eos
!
sflow vrf MGMT destination 10.6.75.59
sflow vrf MGMT destination 10.6.75.62 123
sflow vrf MGMT source-interface Ethernet3
sflow destination 10.6.75.61
sflow destination 10.6.75.62 123
```

### VM Tracer Sessions

#### VM Tracer Summary

| Session | URL | Username | Autovlan | Source Interface |
| ------- | --- | -------- | -------- | ---------------- |
| session_1 | https://192.168.0.10 | user1 | disabled | Management1 |
| session_2 | https://192.168.0.10 | user1 | enabled | - |

#### VM Tracer Device Configuration

```eos
!
vmtracer session session_1
   url https://192.168.0.10
   username user1
   password 7 encrypted_password
   autovlan disable
   source-interface Management1
!
vmtracer session session_2
   url https://192.168.0.10
   username user1
   password 7 encrypted_password
```

### Event Handler

#### Event Handler Summary

| Handler | Action Type | Action | Trigger |
| ------- | ----------- | ------ | ------- |
| CONFIG_VERSIONING | bash | <code>FN=/mnt/flash/startup-config; LFN="`ls -1 $FN.*-* \| tail -n 1`"; if [ -z "$LFN" -o -n "`diff -I 'last modified' $FN $LFN`" ]; then cp $FN $FN.`date +%Y%m%d-%H%M%S`; ls -1r $FN.*-* \| tail -n +11 \| xargs -I % rm %; fi</code> | on-startup-config |
| evpn-blacklist-recovery | bash | <code>FastCli -p 15 -c "clear bgp evpn host-flap"</code> | on-logging |

#### Event Handler Device Configuration

```eos
!
event-handler CONFIG_VERSIONING
   trigger on-startup-config
   action bash FN=/mnt/flash/startup-config; LFN="`ls -1 $FN.*-* | tail -n 1`"; if [ -z "$LFN" -o -n "`diff -I 'last modified' $FN $LFN`" ]; then cp $FN $FN.`date +%Y%m%d-%H%M%S`; ls -1r $FN.*-* | tail -n +11 | xargs -I % rm %; fi
   delay 0
!
event-handler evpn-blacklist-recovery
   trigger on-logging
      regex EVPN-3-BLACKLISTED_DUPLICATE_MAC
   action bash FastCli -p 15 -c "clear bgp evpn host-flap"
   delay 300
   asynchronous
```

### Flow Tracking

#### Flow Tracking Sampled

| Sample Size | Minimum Sample Size | Hardware Offload for IPv4 | Hardware Offload for IPv6 |
| ----------- | ------------------- | ------------------------- | ------------------------- |
| 666 | default | disabled | disabled |

##### Trackers Summary

| Tracker Name | Record Export On Inactive Timeout | Record Export On Interval | MPLS | Number of Exporters | Applied On | Table Size |
| ------------ | --------------------------------- | ------------------------- | ---- | ------------------- | ---------- | ---------- |
| T1 | 3666 | 5666 | True | 0 |  | - |
| T2 | - | - | False | 1 |  | 614400 |
| T3 | - | - | - | 4 |  | 100000 |

##### Exporters Summary

| Tracker Name | Exporter Name | Collector IP/Host | Collector Port | Local Interface |
| ------------ | ------------- | ----------------- | -------------- | --------------- |
| T2 | T2-E1 | - | - | No local interface |
| T3 | T3-E1 | - | - | No local interface |
| T3 | T3-E2 | - | - | No local interface |
| T3 | T3-E3 | - | - | Management1 |
| T3 | T3-E4 | - | - | No local interface |

#### Flow Tracking Configuration

```eos
!
flow tracking sampled
   sample 666
   tracker T1
      record export on inactive timeout 3666
      record export on interval 5666
      record export mpls
   tracker T2
      exporter T2-E1
         collector 42.42.42.42
      flow table size 614400 entries
   tracker T3
      exporter T3-E1
      exporter T3-E2
         collector 10.10.10.10 port 777
      exporter T3-E3
         collector this.is.my.awesome.collector.dns.name port 888
         format ipfix version 10
         local interface Management1
         template interval 424242
      exporter T3-E4
         collector dead:beef::cafe
      flow table size 100000 entries
   no shutdown
```

## Hardware TCAM Profile

TCAM profile __`traffic_policy`__ is active

### Custom TCAM profiles

Following TCAM profiles are configured on device:

- Profile Name: `traffic_policy`

### Hardware TCAM configuration

```eos
!
hardware tcam
   profile traffic_policy
! EOS_CLI inserted directly

   !
   system profile traffic_policy
```

## Spanning Tree

### Spanning Tree Summary

STP mode: **mstp**

#### MSTP Instance and Priority

| Instance(s) | Priority |
| -------- | -------- |
| 0 | 4096 |
| 100-200 | 8192 |

#### MST Configuration

| Variable | Value |
| -------- | -------- |
| Name | test |
| Revision | 5 |
| Instance 2 | VLAN(s) 15,16,17,18 |
| Instance 3 | VLAN(s) 15 |
| Instance 4 | VLAN(s) 200-300 |

### Spanning Tree Device Configuration

```eos
!
spanning-tree mode mstp
spanning-tree mst 0 priority 4096
spanning-tree mst 100-200 priority 8192
!
spanning-tree mst configuration
   name test
   revision 5
   instance 2 vlan 15,16,17,18
   instance 3 vlan 15
   instance 4 vlan 200-300
```

## VLANs

### VLANs Summary

| VLAN ID | Name | Trunk Groups |
| ------- | ---- | ------------ |
| 110 | PR01-DMZ | - |
| 111 | PRIVATE_VLAN_COMMUNITY | - |

#### Private VLANs

| Primary Vlan ID | Secondary VLAN ID | Private Vlan Type |
| --------------- | ----------------- | ----------------- |
| community | 111 | 110 |

### VLANs Device Configuration

```eos
!
vlan 110
   name PR01-DMZ
!
vlan 111
   name PRIVATE_VLAN_COMMUNITY
   private-vlan community primary vlan 110
```

## Interfaces

### Interface Profiles

#### Interface Profiles Summary

- TEST-PROFILE-1

#### Interface Profiles Configuration

```eos
!
interface profile TEST-PROFILE-1
   command description Molecule
   command no switchport
   command no lldp transmit
```

### Ethernet Interfaces

#### Ethernet Interfaces Summary

##### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | Channel-Group |
| --------- | ----------- | ---- | ----- | ----------- | ----------- | ------------- |
| Ethernet31 |  DOT1X Testing - force-unauthorized - no phone | access | - | - | - | - |

*Inherited from Port-Channel Interface

##### Flexible Encapsulation Interfaces

| Interface | Description | Type | Vlan ID | Client Unmatched | Client Dot1q VLAN | Client Dot1q Outer Tag | Client Dot1q Inner Tag | Network Retain Client Encapsulation | Network Dot1q VLAN | Network Dot1q Outer Tag | Network Dot1q Inner Tag |
| --------- | ----------- | ---- | ------- | -----------------| ----------------- | ---------------------- | ---------------------- | ----------------------------------- | ------------------ | ----------------------- | ----------------------- |
| Ethernet26.1 | TENANT_A pseudowire 1 interface | l2dot1q | - | True | - | - | - | False | - | - | - |

##### IPv4

| Interface | Description | Type | Channel Group | IP Address | VRF |  MTU | Shutdown | ACL In | ACL Out |
| --------- | ----------- | -----| ------------- | ---------- | ----| ---- | -------- | ------ | ------- |
| Ethernet47 | IP Helper | routed | - | 172.31.255.1/31 | default | - | - | - | - |

##### IPv6

| Interface | Description | Type | Channel Group | IPv6 Address | VRF | MTU | Shutdown | ND RA Disabled | Managed Config Flag | IPv6 ACL In | IPv6 ACL Out |
| --------- | ----------- | ---- | --------------| ------------ | --- | --- | -------- | -------------- | -------------------| ----------- | ------------ |
| Ethernet3 | P2P_LINK_TO_DC1-SPINE2_Ethernet2 | routed | - | 2002:ABDC::1/64 | default | 1500 | - | - | - | - | - |

#### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet3
   description P2P_LINK_TO_DC1-SPINE2_Ethernet2
   mtu 1500
   no switchport
   ipv6 enable
   ipv6 address 2002:ABDC::1/64
   ipv6 nd prefix 2345:ABCD:3FE0::1/96 infinite 50 no-autoconfig
   ipv6 nd prefix 2345:ABCD:3FE0::2/96 50 infinite
   ipv6 nd prefix 2345:ABCD:3FE0::3/96 100000 no-autoconfig
!
interface Ethernet5
   description Molecule Routing
   no shutdown
   mtu 9100
   no switchport
   ip ospf cost 99
   ip ospf network point-to-point
   ip ospf authentication message-digest
   ip ospf authentication-key 7 <removed>
   ip ospf area 100
   ip ospf message-digest-key 1 sha512 7 <removed>
!
interface Ethernet26
   no switchport
!
interface Ethernet26.1
   description TENANT_A pseudowire 1 interface
   encapsulation vlan
      client unmatched
!
interface Ethernet31
   description DOT1X Testing - force-unauthorized - no phone
   switchport
   dot1x port-control force-unauthorized
!
interface Ethernet47
   description IP Helper
   no switchport
   ip address 172.31.255.1/31
   ip helper-address 10.10.64.151
   ip helper-address 10.10.96.101 source-interface Loopback0
   ip helper-address 10.10.96.150 vrf MGMT source-interface Loopback0
   ip helper-address 10.10.96.151 vrf MGMT
```

### Port-Channel Interfaces

#### Port-Channel Interfaces Summary

##### L2

| Interface | Description | Type | Mode | VLANs | Native VLAN | Trunk Group | LACP Fallback Timeout | LACP Fallback Mode | MLAG ID | EVPN ESI |
| --------- | ----------- | ---- | ---- | ----- | ----------- | ------------| --------------------- | ------------------ | ------- | -------- |
| Port-Channel1 | SRV01_bond0 | switched | trunk | 2-3000 | - | - | - | - | - | 0000:0000:0404:0404:0303 |
| Port-Channel51 | ipv6_prefix | switched | trunk | 1-500 | - | - | - | - | - | - |

##### Flexible Encapsulation Interfaces

| Interface | Description | Type | Vlan ID | Client Unmatched | Client Dot1q VLAN | Client Dot1q Outer Tag | Client Dot1q Inner Tag | Network Retain Client Encapsulation | Network Dot1q VLAN | Network Dot1q Outer Tag | Network Dot1q Inner Tag |
| --------- | ----------- | ---- | ------- | -----------------| ----------------- | ---------------------- | ---------------------- | ----------------------------------- | ------------------ | ----------------------- | ----------------------- |
| Port-Channel2.1000 | L2 Subinterface | l2dot1q | 1000 | False | 100 | - | - | True | - | - | - |

#### Port-Channel Interfaces Device Configuration

```eos
!
interface Port-Channel1
   description SRV01_bond0
   switchport
   switchport trunk allowed vlan 2-3000
   switchport mode trunk
   evpn ethernet-segment
      identifier 0000:0000:0404:0404:0303
      route-target import 04:04:03:03:02:02
   lacp system-id 0303.0202.0101
!
interface Port-Channel2
   description Flexencap Port-Channel
   no switchport
!
interface Port-Channel2.1000
   description L2 Subinterface
   vlan id 1000
   encapsulation vlan
      client dot1q 100 network client
   evpn ethernet-segment
      identifier 0000:0000:0303:0202:0101
      route-target import 03:03:02:02:01:01
   lacp system-id 0303.0202.0101
!
interface Port-Channel51
   description ipv6_prefix
   switchport
   switchport trunk allowed vlan 1-500
   switchport mode trunk
   ipv6 nd prefix a1::/64 infinite infinite no-autoconfig
!
interface Port-Channel100
   logging event link-status
   no switchport
```

### Loopback Interfaces

#### Loopback Interfaces Summary

##### IPv4

| Interface | Description | VRF | IP Address |
| --------- | ----------- | --- | ---------- |
| Loopback0 | EVPN_Overlay_Peering | default | 192.168.255.3/32 |
| Loopback1 | VTEP_VXLAN_Tunnel_Source | default | 192.168.254.3/32 |

##### IPv6

| Interface | Description | VRF | IPv6 Address |
| --------- | ----------- | --- | ------------ |
| Loopback0 | EVPN_Overlay_Peering | default | - |
| Loopback1 | VTEP_VXLAN_Tunnel_Source | default | - |


#### Loopback Interfaces Device Configuration

```eos
!
interface Loopback0
   description EVPN_Overlay_Peering
   ip address 192.168.255.3/32
!
interface Loopback1
   description VTEP_VXLAN_Tunnel_Source
   ip address 192.168.254.3/32
```

### Tunnel Interfaces

#### Tunnel Interfaces Summary

| Interface | Description | VRF | MTU | Shutdown | Source Interface | Destination | PMTU-Discovery |
| --------- | ----------- | --- | --- | -------- | ---------------- | ----------- | -------------- |
| Tunnel3 | test dual stack | default | 1500 | - | Ethernet42 | 1.1.1.1 | - |
| Tunnel4 | test no tcp_mss | default | 1500 | - | Ethernet42 | 1.1.1.1 | - |

##### IPv4

| Interface | VRF | IP Address | TCP MSS | TCP MSS Direction | ACL In | ACL Out |
| --------- | --- | ---------- | ------- | ----------------- | ------ | ------- |
| Tunnel3 | default | 64.64.64.64/24 | - | - | - | - |
| Tunnel4 | default | 64.64.64.64/24 | - | - | - | - |

##### IPv6

| Interface | VRF | IPv6 Address | TCP MSS | TCP MSS Direction | IPv6 ACL In | IPv6 ACL Out |
| --------- | --- | ------------ | ------- | ----------------- | ----------- | ------------ |
| Tunnel3 | default | beef::64/64 | - | - | - | - |
| Tunnel4 | default | beef::64/64 | - | - | - | - |

#### Tunnel Interfaces Device Configuration

```eos
!
interface Tunnel3
   description test dual stack
   mtu 1500
   ip address 64.64.64.64/24
   ipv6 enable
   ipv6 address beef::64/64
   tunnel source interface Ethernet42
   tunnel destination 1.1.1.1
!
interface Tunnel4
   description test no tcp_mss
   mtu 1500
   ip address 64.64.64.64/24
   ipv6 enable
   ipv6 address beef::64/64
   tunnel source interface Ethernet42
   tunnel destination 1.1.1.1
```

### VLAN Interfaces

#### VLAN Interfaces Summary

| Interface | Description | VRF |  MTU | Shutdown |
| --------- | ----------- | --- | ---- | -------- |
| Vlan1 | test ipv6_address_virtual | default | - | - |
| Vlan2 | test ipv6_address_virtual and ipv6_address_virtuals | default | - | - |
| Vlan3 | test ipv6_address_virtual | default | - | - |
| Vlan42 | SVI Description | default | - | False |

##### IPv4

| Interface | VRF | IP Address | IP Address Virtual | IP Router Virtual Address | VRRP | ACL In | ACL Out |
| --------- | --- | ---------- | ------------------ | ------------------------- | ---- | ------ | ------- |
| Vlan1 |  default  |  -  |  -  |  -  |  -  |  -  |  -  |
| Vlan2 |  default  |  -  |  -  |  -  |  -  |  -  |  -  |
| Vlan3 |  default  |  -  |  -  |  -  |  -  |  -  |  -  |
| Vlan42 |  default  |  -  |  10.10.42.1/24  |  -  |  -  |  -  |  -  |

##### IPv6

| Interface | VRF | IPv6 Address | IPv6 Virtual Addresses | Virtual Router Address | VRRP | ND RA Disabled | Managed Config Flag | IPv6 ACL In | IPv6 ACL Out |
| --------- | --- | ------------ | ---------------------- | ---------------------- | ---- | -------------- | ------------------- | ----------- | ------------ |
| Vlan1 | default | - | fc00:10:10:1::1/64 | - | - | - | - | - | - |
| Vlan2 | default | 1b11:3a00:22b0:5200::15/64 | fc00:10:10:2::1/64, fc00:10:11:2::1/64, fc00:10:12:2::1/64 | - | - | - | True | - | - |
| Vlan3 | default | 1b11:3a00:22b3:5200::15/64 | - | fc00:10:10:3::1/64 | - | - | - | - | - |

#### VLAN Interfaces Device Configuration

```eos
!
interface Vlan1
   description test ipv6_address_virtual
   ipv6 enable
   ipv6 address virtual fc00:10:10:1::1/64
!
interface Vlan2
   description test ipv6_address_virtual and ipv6_address_virtuals
   ipv6 enable
   ipv6 address 1b11:3a00:22b0:5200::15/64
   ipv6 address virtual fc00:10:10:2::1/64
   ipv6 address virtual fc00:10:11:2::1/64
   ipv6 address virtual fc00:10:12:2::1/64
   ipv6 nd managed-config-flag
   ipv6 nd prefix 1b11:3a00:22b0:5200::/64 infinite infinite no-autoconfig
!
interface Vlan3
   description test ipv6_address_virtual
   ipv6 enable
   ipv6 address 1b11:3a00:22b3:5200::15/64
   ipv6 virtual-router address fc00:10:10:3::1/64
!
interface Vlan42
   description SVI Description
   no shutdown
   ip helper-address 10.10.64.150 source-interface Loopback0
   ip helper-address 10.10.96.150 source-interface Loopback0
   ip helper-address 10.10.96.151 source-interface Loopback0
   ip address virtual 10.10.42.1/24
```

### VXLAN Interface

#### VXLAN Interface Summary

| Setting | Value |
| ------- | ----- |
| UDP port | 4789 |

##### VLAN to VNI, Flood List and Multicast Group Mappings

| VLAN | VNI | Flood List | Multicast Group |
| ---- | --- | ---------- | --------------- |
| 110 | 10110 | - | 239.9.1.4 |
| 111 | 10111 | 10.1.1.10<br/>10.1.1.11 | - |
| 112 | - | - | 239.9.1.6 |

##### VRF to VNI and Multicast Group Mappings

| VRF | VNI | Multicast Group |
| ---- | --- | --------------- |
| Tenant_A_OP_Zone | 10 | 232.0.0.10 |
| Tenant_A_WEB_Zone | 11 | - |

#### VXLAN Interface Device Configuration

```eos
!
interface Vxlan1
   vxlan vlan 110 vni 10110
   vxlan vlan 111 vni 10111
   vxlan vlan 111 flood vtep 10.1.1.10 10.1.1.11
   vxlan vrf Tenant_A_OP_Zone vni 10
   vxlan vrf Tenant_A_WEB_Zone vni 11
   vxlan vlan 110 multicast group 239.9.1.4
   vxlan vlan 112 multicast group 239.9.1.6
   vxlan vrf Tenant_A_OP_Zone multicast group 232.0.0.10
```

## Routing

### IP Routing

#### IP Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | False |
| MGMT | False |
| TENANT_A_PROJECT01 | True |
| TENANT_A_PROJECT02 | True |

#### IP Routing Device Configuration

```eos
no ip routing vrf MGMT
ip routing vrf TENANT_A_PROJECT01
ip routing vrf TENANT_A_PROJECT02
```

### IPv6 Routing

#### IPv6 Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | False |
| MGMT | false |
| TENANT_A_PROJECT01 | false |
| TENANT_A_PROJECT02 | false |

### Router General

#### VRF Route leaking

| VRF | Source VRF | Route Map Policy |
|-----|------------|------------------|
| BLUE-C2 | BLUE-C1 | RM-BLUE-LEAKING |

#### Router General configuration

```eos
!
router general
   vrf BLUE-C2
      leak routes source-vrf BLUE-C1 subscribe-policy RM-BLUE-LEAKING
      exit
   !
   exit
```

### Router OSPF

#### Router OSPF Summary

| Process ID | Router ID | Default Passive Interface | No Passive Interface | BFD | Max LSA | Default Information Originate | Log Adjacency Changes Detail | Auto Cost Reference Bandwidth | Maximum Paths | MPLS LDP Sync Default | Distribute List In |
| ---------- | --------- | ------------------------- | -------------------- | --- | ------- | ----------------------------- | ---------------------------- | ----------------------------- | ------------- | --------------------- | ------------------ |
| 100 | - | disabled |- | disabled | default | disabled | disabled | - | - | - | - |

#### Router OSPF Areas

| Process ID | Area | Area Type | Filter Networks | Filter Prefix List | Additional Options |
| ---------- | ---- | --------- | --------------- | ------------------ | ------------------ |
| 100 | 0.0.0.2 | normal | 1.1.1.0/24, 2.2.2.0/24 | - |  |
| 100 | 3 | normal | - | PL-OSPF-FILTERING |  |

#### OSPF Interfaces

| Interface | Area | Cost | Point To Point |
| -------- | -------- | -------- | -------- |
| Ethernet5 | 100 | 99 | True |

#### Router OSPF Device Configuration

```eos
!
router ospf 100
   network 198.51.100.0/24 area 0.0.0.1
   network 203.0.113.0/24 area 0.0.0.2
   area 0.0.0.2 filter 1.1.1.0/24
   area 0.0.0.2 filter 2.2.2.0/24
   area 3 filter prefix-list PL-OSPF-FILTERING
```

### Router ISIS

#### Router ISIS Summary

| Settings | Value |
| -------- | ----- |
| Instance | EVPN_UNDERLAY |
| Address Family | ipv4 unicast, ipv6 unicast |

#### ISIS Interfaces Summary

| Interface | ISIS Instance | ISIS Metric | Interface Mode |
| --------- | ------------- | ----------- | -------------- |

#### Router ISIS Device Configuration

```eos
!
router isis EVPN_UNDERLAY
   !
   address-family ipv4 unicast
      maximum-paths 2
      fast-reroute ti-lfa mode link-protection
   address-family ipv6 unicast
      maximum-paths 2
      fast-reroute ti-lfa mode link-protection
   !
```

### Router BGP

#### Router BGP Summary

| BGP AS | Router ID |
| ------ | --------- |
| 65101 | 192.168.255.3 |

#### Router BGP Peer Groups

##### EVPN-OVERLAY-PEERS

| Settings | Value |
| -------- | ----- |
| Address Family | evpn |
| Remote AS | 65001 |
| Listen range prefix | 10.10.10.0/24 |
| Source | Loopback0 |

#### BGP Neighbors

| Neighbor | Remote AS | VRF | Shutdown | Send-community | Maximum-routes | Allowas-in | BFD | RIB Pre-Policy Retain | Route-Reflector Client | Passive |
| -------- | --------- | --- | -------- | -------------- | -------------- | ---------- | --- | --------------------- | ---------------------- | ------- |
| 192.168.255.1 | Inherited from peer group EVPN-OVERLAY-PEERS | default | - | - | - | - | - | - | - | - |
| 192.168.255.2 | Inherited from peer group EVPN-OVERLAY-PEERS | default | - | - | - | - | - | - | - | - |
| 10.255.251.1 | Inherited from peer group EVPN-OVERLAY-PEERS | TENANT_A_PROJECT01 | - | - | - | - | - | - | - | - |
| 10.2.3.4 | - | TENANT_A_PROJECT01 | - | - | - | - | - | - | - | - |
| 10.2.3.5 | - | TENANT_A_PROJECT01 | - | - | - | - | - | - | - | - |

#### BGP Neighbor Interfaces

| Neighbor Interface | VRF | Peer Group | Remote AS | Peer Filter |
| ------------------ | --- | ---------- | --------- | ----------- |
| Ethernet2 | default | EVPN-OVERLAY-PEERS | 65102 | - |
| Ethernet27 | TENANT_A_PROJECT01 | MLAG-IPv4-UNDERLAY-PEER | 1 | - |

#### BGP Route Aggregation

| Prefix | AS Set | Summary Only | Attribute Map | Match Map | Advertise Only |
| ------ | ------ | ------------ | ------------- | --------- | -------------- |
| 1.1.1.0/24 | False | False | - | - | True |
| 2.2.1.0/24 | False | False | - | - | False |

#### Router BGP EVPN Address Family

##### EVPN Peer Groups

| Peer Group | Activate | Encapsulation |
| ---------- | -------- | ------------- |
| EVPN-OVERLAY-PEERS | True | default |

#### Router BGP VPN-IPv4 Address Family

##### VPN-IPv4 Neighbors

| Neighbor | Activate | Route-map In | Route-map Out |
| -------- | -------- | ------------ | ------------- |
| 192.168.255.4 | True | - | - |

##### VPN-IPv4 Peer Groups

| Peer Group | Activate | Route-map In | Route-map Out |
| ---------- | -------- | ------------ | ------------- |
| EVPN-OVERLAY-PEERS | True | - | - |

#### Router BGP VPN-IPv6 Address Family

##### VPN-IPv6 Neighbors

| Neighbor | Activate | Route-map In | Route-map Out |
| -------- | -------- | ------------ | ------------- |
| 2001:cafe:192:168::4 | True | - | - |

##### VPN-IPv6 Peer Groups

| Peer Group | Activate | Route-map In | Route-map Out |
| ---------- | -------- | ------------ | ------------- |
| EVPN-OVERLAY-PEERS | True | - | - |

#### Router BGP VLAN Aware Bundles

| VLAN Aware Bundle | Route-Distinguisher | Both Route-Target | Import Route Target | Export Route-Target | Redistribute | VLANs |
| ----------------- | ------------------- | ----------------- | ------------------- | ------------------- | ------------ | ----- |
| TENANT_A_PROJECT01 | 192.168.255.3:11 | 11:11 | - | - | learned | 110 |

#### Router BGP VLANs

| VLAN | Route-Distinguisher | Both Route-Target | Import Route Target | Export Route-Target | Redistribute |
| ---- | ------------------- | ----------------- | ------------------- | ------------------- | ------------ |
| 24 | 10.50.64.15:10024 | 1:10024 | - | - |  |

#### Router BGP VRFs

| VRF | Route-Distinguisher | Redistribute |
| --- | ------------------- | ------------ |
| TENANT_A_PROJECT01 | 192.168.255.3:11 | connected<br>static |

#### Router BGP Device Configuration

```eos
!
router bgp 65101
   router-id 192.168.255.3
   bgp listen range 10.10.10.0/24 peer-group EVPN-OVERLAY-PEERS peer-filter myfilter
   neighbor EVPN-OVERLAY-PEERS peer group
   neighbor EVPN-OVERLAY-PEERS remote-as 65001
   neighbor EVPN-OVERLAY-PEERS update-source Loopback0
   neighbor interface Ethernet2 peer-group EVPN-OVERLAY-PEERS remote-as 65102
   neighbor 192.168.255.1 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.255.2 peer group EVPN-OVERLAY-PEERS
   aggregate-address 1.1.1.0/24 advertise-only
   aggregate-address 2.2.1.0/24
   redistribute connected route-map RM-CONN-2-BGP
   !
   vlan 24
      rd 10.50.64.15:10024
      route-target both 1:10024
   !
   vlan-aware-bundle TENANT_A_PROJECT01
      rd 192.168.255.3:11
      route-target both 11:11
      redistribute learned
      vlan 110
   !
   address-family evpn
      neighbor EVPN-OVERLAY-PEERS activate
   !
   address-family rt-membership
      neighbor EVPN-OVERLAY-PEERS activate
   !
   address-family ipv4
      neighbor EVPN-OVERLAY-PEERS next-hop address-family ipv6 originate
      neighbor EVPN-OVERLAY-PEERS activate
      neighbor 192.0.2.1 prefix-list PL-FOO-v4-IN in
      neighbor 192.0.2.1 prefix-list PL-FOO-v4-OUT out
      network 10.0.0.0/8
      network 172.16.0.0/12
      network 192.168.0.0/16 route-map RM-FOO-MATCH
   !
   address-family ipv4 multicast
      neighbor EVPN-OVERLAY-PEERS activate
      redistribute attached-host
   !
   address-family ipv6
      neighbor EVPN-OVERLAY-PEERS activate
      neighbor 2001:db8::1 prefix-list PL-FOO-v6-IN in
      neighbor 2001:db8::1 prefix-list PL-FOO-v6-OUT out
      network 2001:db8:100::/40
      network 2001:db8:200::/40 route-map RM-BAR-MATCH
      redistribute static route-map RM-IPV6-STATIC-TO-BGP
   !
   address-family vpn-ipv4
      neighbor EVPN-OVERLAY-PEERS activate
      neighbor 192.168.255.4 activate
   !
   address-family vpn-ipv6
      neighbor EVPN-OVERLAY-PEERS activate
      neighbor 2001:cafe:192:168::4 activate
   !
   vrf TENANT_A_PROJECT01
      rd 192.168.255.3:11
      route-target import evpn 11:11
      route-target export evpn 11:11
      router-id 192.168.255.3
      neighbor interface Ethernet27 peer-group MLAG-IPv4-UNDERLAY-PEER remote-as 1
      neighbor 10.255.251.1 peer group EVPN-OVERLAY-PEERS
      network 10.0.0.0/8
      network 100.64.0.0/10
      aggregate-address 0.0.0.0/0 as-set summary-only attribute-map RM-BGP-AGG-APPLY-SET
      redistribute connected
      redistribute static route-map RM-CONN-2-BGP
      !
      address-family ipv4
         neighbor 10.2.3.4 activate
         neighbor 10.2.3.4 prefix-list PL-TEST-IN-AF4 in
         neighbor 10.2.3.4 prefix-list PL-TEST-OUT-AF4 out
         neighbor 10.2.3.5 activate
         neighbor 10.2.3.5 prefix-list PL-TEST-IN in
         neighbor 10.2.3.5 prefix-list PL-TEST-OUT out
         neighbor 10.255.251.1 prefix-list PL-TEST-IN in
         neighbor 10.255.251.1 prefix-list PL-TEST-OUT out
      !
      address-family ipv4
         neighbor TEST_PEER_GRP activate
         neighbor 10.2.3.4 activate
         neighbor 10.2.3.4 route-map RM-10.2.3.4-SET-NEXT-HOP-OUT out
         neighbor 10.2.3.5 activate
         neighbor 10.2.3.5 route-map RM-10.2.3.5-SET-NEXT-HOP-IN in
         network 10.0.0.0/8
         network 100.64.0.0/10 route-map RM-10.2.3.4
```

### PBR Policy Maps

#### PBR Policy Maps Summary

##### PM_PBR_BREAKOUT

| Class | Index | Drop | Nexthop | Recursive |
| ----- | ----- | ---- | ------- | --------- |
| CM_PBR_EXCLUDE | - | - | - | - |
| CM_PBR_INCLUDE | - | - | 192.168.4.2 | True |

#### PBR Policy Maps Configuration

```eos
!
policy-map type pbr PM_PBR_BREAKOUT
   class CM_PBR_EXCLUDE
   !
   class CM_PBR_INCLUDE
      set nexthop recursive 192.168.4.2
```

## Multicast

### IP IGMP Snooping

#### IP IGMP Snooping Summary

| IGMP Snooping | Fast Leave | Interface Restart Query | Proxy | Restart Query Interval | Robustness Variable |
| ------------- | ---------- | ----------------------- | ----- | ---------------------- | ------------------- |
| Enabled | - | - | - | - | - |

##### IP IGMP Snooping Vlan Summary

| Vlan | IGMP Snooping | Fast Leave | Max Groups | Proxy |
| ---- | ------------- | ---------- | ---------- | ----- |
| 10 | True | - | - | - |
| 20 | False | - | - | - |
| 30 | False | - | - | - |

#### IP IGMP Snooping Device Configuration

```eos
!
ip igmp snooping vlan 10
no ip igmp snooping vlan 20
no ip igmp snooping vlan 30
```

### PIM Sparse Mode

#### Router PIM Sparse Mode

##### IP Sparse Mode Information

BFD enabled: True

####### IP Rendezvous Information

| Rendezvous Point Address | Group Address | Access Lists | Priority | Hashmask | Override |
| ------------------------ | ------------- | ------------ | -------- | -------- | -------- |
| 10.238.1.161 | 239.12.12.12/32, 239.12.12.13/32 | - | - | - | - |

####### IP Anycast Information

| IP Anycast Address | Other Rendezvous Point Address | Register Count |
| ------------------ | ------------------------------ | -------------- |
| 10.38.1.161 | 10.50.64.16 | 15 |

##### Router Multicast Device Configuration

```eos
!
router pim sparse-mode
   ipv4
      bfd
      rp address 10.238.1.161 239.12.12.12/32
      rp address 10.238.1.161 239.12.12.13/32
      anycast-rp 10.38.1.161 10.50.64.16 register-count 15
```

## Filters

### Community-lists

#### Community-lists Summary

| Name | Action |
| -------- | ------ |
| TEST1 | permit 1000:1000 |
| TEST2 | permit 2000:3000 |

#### Community-lists Device Configuration

```eos
!
ip community-list TEST1 permit 1000:1000
ip community-list TEST2 permit 2000:3000
```

### Peer Filters

#### Peer Filters Summary

##### PF1

| Sequence | Match |
| -------- | ----- |
| 10 | as-range 1-2 result reject |
| 20 | as-range 1-100 result accept |

##### PF2

| Sequence | Match |
| -------- | ----- |
| 30 | as-range 65000 result accept |

#### Peer Filters Device Configuration

```eos
!
peer-filter PF1
   10 match as-range 1-2 result reject
   20 match as-range 1-100 result accept
!
peer-filter PF2
   30 match as-range 65000 result accept
```

### Prefix-lists

#### Prefix-lists Summary

##### PL-LOOPBACKS-EVPN-OVERLAY

| Sequence | Action |
| -------- | ------ |
| 10 | permit 192.168.255.0/24 eq 32 |
| 20 | permit 192.168.254.0/24 eq 32 |

#### Prefix-lists Device Configuration

```eos
!
ip prefix-list PL-LOOPBACKS-EVPN-OVERLAY
   seq 10 permit 192.168.255.0/24 eq 32
   seq 20 permit 192.168.254.0/24 eq 32
```

### IPv6 Prefix-lists

#### IPv6 Prefix-lists Summary

##### PL-IPV6-LOOPBACKS

| Sequence | Action |
| -------- | ------ |
| 10 | permit 1b11:3a00:22b0:0082::/64 eq 128 |

#### IPv6 Prefix-lists Device Configuration

```eos
!
ipv6 prefix-list PL-IPV6-LOOPBACKS
   seq 10 permit 1b11:3a00:22b0:0082::/64 eq 128
```

### Route-maps

#### Route-maps Summary

##### RM-CONN-BL-BGP

| Sequence | Type | Match | Set | Sub-Route-Map | Continue |
| -------- | ---- | ----- | --- | ------------- | -------- |
| 10 | deny | ip address prefix-list PL-MLAG | - | - | - |

#### Route-maps Device Configuration

```eos
!
route-map RM-CONN-BL-BGP deny 10
   match ip address prefix-list PL-MLAG
```

### IP Extended Community Lists

#### IP Extended Community Lists Summary

| List Name | Type | Extended Communities |
| --------- | ---- | -------------------- |
| TEST1 | permit | 65000:65000 |
| TEST1 | deny | 65002:65002 |
| TEST2 | deny | 65001:65001 |

#### IP Extended Community Lists configuration

```eos
!
ip extcommunity-list TEST1 permit 65000:65000
ip extcommunity-list TEST1 deny 65002:65002
!
ip extcommunity-list TEST2 deny 65001:65001
```

### IP Extended Community RegExp Lists

#### IP Extended Community RegExp Lists Summary

| List Name | Type | Regular Expression |
| --------- | ---- | ------------------ |
| TEST1 | permit | 65[0-9]{3}:[0-9]+ |
| TEST1 | deny | .* |
| TEST2 | deny | 6500[0-1]:650[0-9][0-9] |

#### IP Extended Community RegExp Lists configuration

```eos
!
ip extcommunity-list regexp TEST1 permit 65[0-9]{3}:[0-9]+
ip extcommunity-list regexp TEST1 deny .*
!
ip extcommunity-list regexp TEST2 deny 6500[0-1]:650[0-9][0-9]
```

### Match-lists

#### Match-list Input String Summary

##### molecule

| Sequence | Match Regex |
| -------- | ------ |
| 10 | ^.*MOLECULE.*$ |
| 20 | ^.*TESTING.*$ |


#### Match-lists Device Configuration

```eos
!
match-list input string molecule
   10 match regex ^.*MOLECULE.*$
   20 match regex ^.*TESTING.*$
```

## 802.1X Port Security

### 802.1X Summary

#### 802.1X Interfaces

| Interface | PAE Mode | State | Phone Force Authorized | Reauthentication | Auth Failure Action | Host Mode | Mac Based Auth | Eapol |
| --------- | -------- | ------| ---------------------- | ---------------- | ------------------- | --------- | -------------- | ------ |
| Ethernet31 | - | force-unauthorized | - | - | - | - | - | - |

## ACL

### Standard Access-lists

#### Standard Access-lists Summary

##### ACL-API

| Sequence | Action |
| -------- | ------ |
| 10 | remark ACL to restrict access to switch API to CVP and Ansible |
| 20 | permit host 10.10.10.10 |
| 30 | permit host 10.10.10.11 |
| 40 | permit host 10.10.10.12 |

#### Standard Access-lists Device Configuration

```eos
!
ip access-list standard ACL-API
   10 remark ACL to restrict access to switch API to CVP and Ansible
   20 permit host 10.10.10.10
   30 permit host 10.10.10.11
   40 permit host 10.10.10.12
```

### Extended Access-lists

#### Extended Access-lists Summary

##### ACL-01

| Sequence | Action |
| -------- | ------ |
| 10 | remark ACL to restrict access to switch API to CVP and Ansible |
| 20 | deny ip host 192.0.2.1 any |
| 30 | permit ip 192.0.2.0/24 any |

#### Extended Access-lists Device Configuration

```eos
!
ip access-list ACL-01
   10 remark ACL to restrict access to switch API to CVP and Ansible
   20 deny ip host 192.0.2.1 any
   30 permit ip 192.0.2.0/24 any
```

### IPv6 Standard Access-lists

#### IPv6 Standard Access-lists Summary

##### TEST4

| Sequence | Action |
| -------- | ------ |
| 5 | deny fe80::/64 |
| 10 | permit fe90::/64 |

#### IPv6 Standard Access-lists Device Configuration

```eos
!
ipv6 access-list standard TEST4
   5 deny fe80::/64
   10 permit fe90::/64
```

### IPv6 Extended Access-lists

#### IPv6 Extended Access-lists Summary

##### TEST1

| Sequence | Action |
| -------- | ------ |
| 5 | deny ipv6 fe80::/64 any |
| 10 | permit ipv6 fe90::/64 any |

#### IPv6 Extended Access-lists Device Configuration

```eos
!
ipv6 access-list TEST1
   5 deny ipv6 fe80::/64 any
   10 permit ipv6 fe90::/64 any
```

## VRF Instances

### VRF Instances Summary

| VRF Name | IP Routing |
| -------- | ---------- |
| MGMT | disabled |
| TENANT_A_PROJECT01 | enabled |
| TENANT_A_PROJECT02 | enabled |

### VRF Instances Device Configuration

```eos
!
vrf instance MGMT
!
vrf instance TENANT_A_PROJECT01
!
vrf instance TENANT_A_PROJECT02
```

## Virtual Source NAT

### Virtual Source NAT Summary

| Source NAT VRF | Source NAT IP Address |
| -------------- | --------------------- |
| TEST_01 | 1.1.1.1 |
| TEST_02 | 1.1.1.2 |

### Virtual Source NAT Configuration

```eos
!
ip address virtual source-nat vrf TEST_01 address 1.1.1.1
ip address virtual source-nat vrf TEST_02 address 1.1.1.2
```

## MACsec

### MACsec Summary

License is installed.

FIPS restrictions enabled.

#### MACsec Profiles Summary

**Profile A1:**

Settings:

| Cipher | Key-Server Priority | Rekey-Period | SCI |
| ------ | ------------------- | ------------ | --- |
| - | - | - | True |

Keys:


**Profile A2:**

Settings:

| Cipher | Key-Server Priority | Rekey-Period | SCI |
| ------ | ------------------- | ------------ | --- |
| - | - | - | - |

Keys:

| Key ID | Fallback |
| ------ |  -------- |
| 1234b | - |

### MACsec Device Configuration

```eos
!
mac security
   license license1 123456
   fips restrictions
   !
   profile A1
      sci
   profile A2
      key 1234b 7 <removed>
```

### Traffic Policies information

**IPv4 Field sets**

| Field Set Name | Values |
| -------------- | ------ |
| DEMO-01 | 10.0.0.0/8<br/>192.168.0.0/16 |
| DEMO-02 | 172.16.0.0/12<br/>224.0.0.0/8 |

**IPv6 Field sets**

| Field Set Name | Values |
| -------------- | ------ |
| DEMO-03 | aaaa::/64<br/>bbbb::/64 |

**L4 Port Field sets**

| Field Set Name | Values |
| -------------- | ------ |
| SERVICE-DEMO | 10,20,80,440-450|

#### Traffic Policies

**BLUE-C1-POLICY:**

| Match set | Type | Sources | Destinations | Protocol | Source Port(s) | Destination port(s) | Action |
| --------- | ---- | ------- | ------------ | -------- | -------------- | ------------------- | ------ |
| BLUE-C1-POLICY-02 | ipv4 | DEMO-01<br/>DEMO-02 | ANY | tcp<br/>icmp | ANY | SERVICE-DEMO | action: PASS<br/>counter: DEMO-TRAFFIC<br/>dscp marking: 60 |

#### Traffic Policies Device Configuration

```eos
!
traffic-policies
   field-set ipv4 prefix DEMO-01
      10.0.0.0/8 192.168.0.0/16
   !
   field-set ipv4 prefix DEMO-02
      172.16.0.0/12 224.0.0.0/8
   !
   field-set ipv6 prefix DEMO-03
      aaaa::/64 bbbb::/64
   !
   field-set l4-port SERVICE-DEMO
      10,20,80,440-450
   !
   traffic-policy BLUE-C1-POLICY
      counter DEMO-TRAFFIC
      match BLUE-C1-POLICY-02 ipv4
         source prefix field-set DEMO-01 DEMO-02
         protocol tcp flags established destination port field-set SERVICE-DEMO
         protocol icmp
         actions
            count DEMO-TRAFFIC
            set dscp 60
         !
      !
   !
```

## Quality Of Service

### QOS Class Maps

#### QOS Class Maps Summary

| Name | Field | Value |
| ---- | ----- | ----- |
| CM_REPLICATION_LD | acl | ACL_REPLICATION_LD |
| CM_REPLICATION_LD2 | vlan | 200 |
| CM_REPLICATION_LD3 | cos | 3 |

#### Class-maps Device Configuration

```eos
!
class-map type qos match-any CM_REPLICATION_LD
   match ip access-group ACL_REPLICATION_LD
!
class-map type qos match-any CM_REPLICATION_LD2
   match vlan 200
!
class-map type qos match-any CM_REPLICATION_LD3
   match cos 3
!
class-map type pbr match-any CM_PBR_EXCLUDE
   match ip access-group ACL_PBR_EXCLUDE
!
class-map type pbr match-any CM_PBR_INCLUDE
   match ip access-group ACL_PBR_INCLUDE
```

### QOS Policy Maps

#### QOS Policy Maps Summary

**PM_REPLICATION_LD**

| class | Set | Value |
| ----- | --- | ----- |
| CM_REPLICATION_LD | dscp | af11 |
| CM_REPLICATION_LD | traffic_class | 2 |
| CM_REPLICATION_LD | drop_precedence | 1 |

#### QOS Policy Maps configuration

```eos
!
policy-map type quality-of-service PM_REPLICATION_LD
   class CM_REPLICATION_LD
      set dscp af11
      set traffic-class 2
      set drop-precedence 1
```

### QOS Profiles

#### QOS Profiles Summary


QOS Profile: **test**

**Settings**

| Default COS | Default DSCP | Trust | Shape Rate | QOS Service Policy |
| ----------- | ------------ | ----- | ---------- | ------------------ |
| - | 46 | dscp | 80 percent | - |

**TX Queues**

| TX queue | Type | Bandwidth | Priority | Shape Rate | Comment |
| -------- | ---- | --------- | -------- | ---------- | ------- |
| 1 | All | 50 | no priority | - | - |
| 2 | Unicast | 50 | no priority | - | - |
| 3 | Multicast | 50 | no priority | - | - |

#### QOS Profile Device Configuration

```eos
!
qos profile test
   qos trust dscp
   qos dscp 46
   shape rate 80 percent
   !
   tx-queue 1
      bandwidth percent 50
      no priority
   !
   uc-tx-queue 2
      bandwidth percent 50
      no priority
   !
   mc-tx-queue 3
      bandwidth percent 50
      no priority
```

## STUN

### STUN Server

| Server local interfaces |
| ----------------------- |
| ethernet1 |

### STUN Device Configuration

```eos
!
stun
   server
      local-interface ethernet1
```

## Maintenance Mode

### BGP Groups

#### BGP Groups Summary

| BGP group | VRF Name | Neighbors | BGP maintenance profiles |
| --------- | -------- | --------- | ------------------------ |
| bar | red | peer-group-baz | downlink-neighbors |
| foo | - | 169.254.1.1<br>fe80::1 | BP1 |

#### BGP Groups Configuration

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
```

### Interface Groups

#### Interface Groups Summary

| Interface Group | Interfaces | Interface maintenance profile | BGP maintenance profiles |
| --------------- | ---------- | ----------------------------- | ------------------------ |
| QSFP_Interface_Group | Ethernet1,5 | uplink-interfaces | BP1 |
| SFP_Interface_Group | Ethernet10-20<br>Ethernet30-48 | IP1 | BP1 |

#### Interface Groups Configuration

```eos
!
group interface QSFP_Interface_Group
   interface Ethernet1,5
   maintenance profile interface uplink-interfaces
!
group interface SFP_Interface_Group
   interface Ethernet10-20
   interface Ethernet30-48
```

### Maintenance

#### Maintenance defaults

Default maintenance bgp profile: **BP1**

Default maintenance interface profile: **IP1**

Default maintenance unit profile: **UP1**

#### Maintenance profiles

| BGP profile | Initiator route-map |
| ----------- | ------------------- |
| BP1 | RM-MAINTENANCE |
| BP2 | RM-MAINTENANCE2 |
| BP3 | RM-MAINTENANCE3 |

| Interface profile | Rate monitoring load interval (s) | Rate monitoring threshold in/out (kbps) | Shutdown Max Delay |
|-------------------|-----------------------------------|-----------------------------------------|--------------------|
| IP1 | 10 | 500 | 300 |

| Unit profile | on-boot duration (s) |
| ------------ | -------------------- |
| UP1 | 900 |
| UP2 | 600 |

#### Maintenance units

| Unit | Interface groups | BGP groups | Unit profile | Quiesce |
| ---- | ---------------- | ---------- | ------------ | ------- |
| System | - | - | UP1 | No |
| UNIT1 | INTERFACE_GROUP_1 | BGP_GROUP_1<br/>BGP_GROUP_2 | UP1 | No |

#### Maintenance configuration

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
   profile unit UP1 default
   !
   profile interface IP1
      rate-monitoring load-interval 10
      rate-monitoring threshold 500
      shutdown max-delay 300
   !
   profile unit UP1
      on-boot duration 900
   !
   profile unit UP2
      on-boot duration 600
   !
   unit System
   !
   unit UNIT1
      group bgp BGP_GROUP_1
      group bgp BGP_GROUP_2
      group interface INTERFACE_GROUP_1
      profile unit UP1
```
