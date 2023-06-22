# amber-leaf1

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
  - [DNS Domain](#dns-domain)
  - [IP Name Servers](#ip-name-servers)
  - [NTP](#ntp)
  - [Management API gNMI](#management-api-gnmi)
  - [Management CVX Summary](#management-cvx-summary)
  - [Management API HTTP](#management-api-http)
  - [Management API Models](#management-api-models)
- [Authentication](#authentication)
  - [Local Users](#local-users)
  - [Roles](#roles)
  - [AAA Authentication](#aaa-authentication)
  - [AAA Authorization](#aaa-authorization)
- [Aliases](#aliases)
- [Monitoring](#monitoring)
  - [TerminAttr Daemon](#terminattr-daemon)
  - [MCS client Summary](#mcs-client-summary)
  - [SNMP](#snmp)
  - [SFlow](#sflow)
- [Monitor Connectivity](#monitor-connectivity)
  - [Global Configuration](#global-configuration)
  - [Vrf Configuration](#vrf-configuration)
  - [Monitor Connectivity Device Configuration](#monitor-connectivity-device-configuration)
- [Hardware TCAM Profile](#hardware-tcam-profile)
  - [Hardware TCAM configuration](#hardware-tcam-configuration)
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
- [Routing](#routing)
  - [Service Routing Protocols Model](#service-routing-protocols-model)
  - [Virtual Router MAC Address](#virtual-router-mac-address)
  - [IP Routing](#ip-routing)
  - [IPv6 Routing](#ipv6-routing)
  - [Static Routes](#static-routes)
  - [Router BGP](#router-bgp)
- [Multicast](#multicast)
  - [IP IGMP Snooping](#ip-igmp-snooping)
  - [Router Multicast](#router-multicast)
  - [PIM Sparse Mode](#pim-sparse-mode)
- [VRF Instances](#vrf-instances)
  - [VRF Instances Summary](#vrf-instances-summary)
  - [VRF Instances Device Configuration](#vrf-instances-device-configuration)
- [Platform](#platform)
  - [Platform Summary](#platform-summary)
  - [Platform Configuration](#platform-configuration)

## Management

### Management Interfaces

#### Management Interfaces Summary

##### IPv4

| Management Interface | description | Type | VRF | IP Address | Gateway |
| -------------------- | ----------- | ---- | --- | ---------- | ------- |
| Management1 | oob_management | oob | MGMT | 10.90.227.25/24 | 10.90.227.1 |

##### IPv6

| Management Interface | description | Type | VRF | IPv6 Address | IPv6 Gateway |
| -------------------- | ----------- | ---- | --- | ------------ | ------------ |
| Management1 | oob_management | oob | MGMT | - | - |

#### Management Interfaces Device Configuration

```eos
!
interface Management1
   description oob_management
   no shutdown
   vrf MGMT
   ip address 10.90.227.25/24
```

### DNS Domain

#### DNS domain: MnE.lab

#### DNS Domain Device Configuration

```eos
dns domain MnE.lab
!
```

### IP Name Servers

#### IP Name Servers Summary

| Name Server | VRF | Priority |
| ----------- | --- | -------- |
| 10.90.227.155 | MGMT | - |

#### IP Name Servers Device Configuration

```eos
ip name-server vrf MGMT 10.90.227.155
```

### NTP

#### NTP Summary

##### NTP Servers

| Server | VRF | Preferred | Burst | iBurst | Version | Min Poll | Max Poll | Local-interface | Key |
| ------ | --- | --------- | ----- | ------ | ------- | -------- | -------- | --------------- | --- |
| ntp.aristanetworks.com | MGMT | - | - | True | - | - | - | - | - |

#### NTP Device Configuration

```eos
!
ntp server vrf MGMT ntp.aristanetworks.com iburst
```

### Management API gNMI

#### Management API gNMI Summary

| Transport | SSL Profile | VRF | Notification Timestamp | ACL |
| --------- | ----------- | --- | ---------------------- | --- |
| grpc | - | MGMT | last-change-time | - |

Provider eos-native is configured.

#### Management API gNMI configuration

```eos
!
management api gnmi
   transport grpc grpc
      vrf MGMT
   provider eos-native
```

### Management CVX Summary

| Shutdown | CVX Servers |
| -------- | ----------- |
| False | 10.90.224.188 |

#### Management CVX configuration

```eos
!
management cvx
   no shutdown
   server host 10.90.224.188
   vrf MGMT
```

### Management API HTTP

#### Management API HTTP Summary

| HTTP | HTTPS | Default Services |
| ---- | ----- | ---------------- |
| False | True | - |

#### Management API VRF Access

| VRF Name | IPv4 ACL | IPv6 ACL |
| -------- | -------- | -------- |
| MGMT | - | - |

#### Management API HTTP Configuration

```eos
!
management api http-commands
   protocol https
   no shutdown
   !
   vrf MGMT
      no shutdown
```

### Management API Models

#### Management API Models Summary

| Provider | Path | Disabled |
| -------- | ---- | ------- |
| smash | bridging | False |
| smash | ptp | False |
| smash | routing | False |

#### Management API Models Configuration

```eos
!
management api models
   !
   provider smash
      path bridging
      path ptp
      path routing
```

## Authentication

### Local Users

#### Local Users Summary

| User | Privilege | Role | Disabled | Shell |
| ---- | --------- | ---- | -------- | ----- |
| admin | 15 | network-admin | False | - |
| cvpadmin | 15 | network-admin | False | - |
| dataminer | 1 | view-only | False | - |

#### Local Users Device Configuration

```eos
!
username admin privilege 15 role network-admin secret sha512 <removed>
username cvpadmin privilege 15 role network-admin secret sha512 <removed>
username dataminer privilege 1 role view-only secret sha512 <removed>
```

### Roles

#### Roles Summary

##### Role view-only

| Sequence | Action | Mode | Command |
| -------- | ------ | ---- | ------- |
| 10 | permit | - | enable |
| 20 | deny | exec | reload |
| 30 | deny | config-all | .* |
| 40 | deny | exec | clear .* |
| 50 | permit | - | show .* |
| 60 | permit | - | bash timeout 1 df -h |

#### Roles Device Configuration

```eos
!
role view-only
   10 permit command enable
   20 deny mode exec command reload
   30 deny mode config-all command .*
   40 deny mode exec command clear .*
   50 permit command show .*
   60 permit command bash timeout 1 df -h
```

### AAA Authentication

#### AAA Authentication Summary

| Type | Sub-type | User Stores |
| ---- | -------- | ---------- |
| Login | default | local |

#### AAA Authentication Device Configuration

```eos
aaa authentication login default local
!
```

### AAA Authorization

#### AAA Authorization Summary

| Type | User Stores |
| ---- | ----------- |
| Exec | local |

Authorization for configuration commands is disabled.

#### AAA Authorization Device Configuration

```eos
aaa authorization exec default local
!
```

## Aliases

```eos
alias sln show lldp neighbors
alias conint sh interface | I connected
alias connect show interfaces status connected
alias descr show int descr
alias drops watch 1 diff show int coun dis | nz
alias dump bash tcpdump -i %1
alias ptpcount watch 1 diff sh ptp interface counters | egrep 'Ethernet|Manage'| grep -v "received: 0" | grep -v sent
alias ptpmgmt watch 1 diff sh ptp int count | egrep "Management messages received: | Ethernet" | nz
alias rates watch 1 diff show int count rates | nz
alias routeage bash echo show ip route | cliribd
alias senz show interface counter error | nz
alias senzwatch watch 1 diff show interface counter error | nz
alias shmc show int | awk '/^[A-Z]/ { intf = $1 } /, address is/ { print intf, $6 }'
alias shptp show ptp int counters drop
alias snoopcount watch 1 diff sh ip igmp snooping counters | nz
alias snoopgroup watch 1 diff sh ip igmp snooping groups | nz
alias snz show interface counter | nz
alias spd show port-channel %1 detail all
alias sqnz show interface counter queue | nz
alias srnz show interface counter rate | nz
alias watchptp watch 1 diff sh ip igmp snooping group 224.0.1.129 | nz
alias igmpgroups show ip igmp snooping groups detail
alias ptpwatch watch 1 diff show ptp
alias sdnz show int count discard | nz
alias sie show ip igmp snoop counters err | nz
alias sqml show queue-monitor length

!
```

## Monitoring

### TerminAttr Daemon

#### TerminAttr Daemon Summary

| CV Compression | CloudVision Servers | VRF | Authentication | Smash Excludes | Ingest Exclude | Bypass AAA |
| -------------- | ------------------- | --- | -------------- | -------------- | -------------- | ---------- |
+
| gzip | apiserver.arista.io:443 | MGMT | token-secure,/tmp/cv-onboarding-token | ale,flexCounter,hardware,kni,pulse,strata | /Sysdb/cell/1/agent,/Sysdb/cell/2/agent | True |
| gzip | 10.244.132.193:9910 | MGMT | token,/tmp/devtoken | ale,flexCounter,hardware,kni,pulse,strata | /Sysdb/cell/1/agent,/Sysdb/cell/2/agent | True |
| gzip | 10.90.227.161:9910 | MGMT | token,/tmp/token | ale,flexCounter,hardware,kni,pulse,strata | /Sysdb/cell/1/agent,/Sysdb/cell/2/agent | True |

#### TerminAttr Daemon Device Configuration

```eos
!
daemon TerminAttr
   exec /usr/bin/TerminAttr -cvopt cvaas.addr=apiserver.arista.io:443 -cvopt cvaas.auth=token-secure,/tmp/cv-onboarding-token -cvopt cvaas.vrf=MGMT -cvopt dev.addr=10.244.132.193:9910 -cvopt dev.auth=token,/tmp/devtoken -cvopt dev.vrf=MGMT -cvopt lab.addr=10.90.227.161:9910 -cvopt lab.auth=token,/tmp/token -cvopt lab.vrf=MGMT -disableaaa -smashexcludes=ale,flexCounter,hardware,kni,pulse,strata -ingestexclude=/Sysdb/cell/1/agent,/Sysdb/cell/2/agent -taillogs
   no shutdown
```

### MCS client Summary

MCS client is enabled

#### MCS client configuration

```eos
!
mcs client
   no shutdown
```

### SNMP

#### SNMP Configuration Summary

| Contact | Location | SNMP Traps | State |
| ------- | -------- | ---------- | ----- |
| - | - | All | Disabled |

#### SNMP Communities

| Community | Access | Access List IPv4 | Access List IPv6 | View |
| --------- | ------ | ---------------- | ---------------- | ---- |
| <removed> | ro | - | - | - |
| <removed> | rw | - | - | - |

#### SNMP Device Configuration

```eos
!
snmp-server community <removed> ro
snmp-server community <removed> rw
```

### SFlow

#### SFlow Summary

| VRF | SFlow Source | SFlow Destination | Port |
| --- | ------------ | ----------------- | ---- |
| default | - | 127.0.0.1 | 6343 |
| default | loopback0 | - | - |

sFlow is enabled.

#### SFlow Device Configuration

```eos
!
sflow destination 127.0.0.1
sflow source-interface loopback0
sflow run
```

## Monitor Connectivity

### Global Configuration

#### Probing Configuration

| Enabled | Interval | Default Interface Set |
| ------- | -------- | --------------------- |
| True | - | - |

#### Host Parameters

| Host Name | Description | IPv4 Address | Probing Interface Set | URL |
| --------- | ----------- | ------------ | --------------------- | --- |
| GM1 | - | 172.24.121.65 | - | - |

### Vrf Configuration

| Name | Description | Default Interface Set |
| ---- | ----------- | --------------------- |
| MGMT | - | - |

#### Vrf MGMT Configuration

##### Host Parameters

| Host Name | Description | IPv4 Address | Probing Interface Set | URL |
| --------- | ----------- | ------------ | --------------------- | --- |
| aws-us-east-1 | aws-us-east-1 | 52.216.227.10 | - | http://fredcloudtracereast1.s3-website-us-east-1.amazonaws.com |
| aws-us-west-2 | aws-us-west-2 | 52.218.182.251 | - | http://fredwebsitebuckettest.s3-website-us-west-2.amazonaws.com |
| azure-eastus | aws-us-west-2 | 52.216.227.10 | - | http://fredcloudtracereast1.s3-website-us-east-1.amazonaws.com |
| Google | Google | 8.8.8.8 | - | - |

### Monitor Connectivity Device Configuration

```eos
!
monitor connectivity
   no shutdown
   !
   host GM1
      ip 172.24.121.65
   vrf MGMT
      !
      host aws-us-east-1
         description
         aws-us-east-1
         ip 52.216.227.10
         url http://fredcloudtracereast1.s3-website-us-east-1.amazonaws.com
      !
      host aws-us-west-2
         description
         aws-us-west-2
         ip 52.218.182.251
         url http://fredwebsitebuckettest.s3-website-us-west-2.amazonaws.com
      !
      host azure-eastus
         description
         aws-us-west-2
         ip 52.216.227.10
         url http://fredcloudtracereast1.s3-website-us-east-1.amazonaws.com
      !
      host Google
         description
         Google
         ip 8.8.8.8
```

## Hardware TCAM Profile

TCAM profile __`vxlan-routing`__ is active

### Hardware TCAM configuration

```eos
!
hardware tcam
   system profile vxlan-routing
```

## Spanning Tree

### Spanning Tree Summary

STP mode: **mstp**

#### MSTP Instance and Priority

| Instance(s) | Priority |
| -------- | -------- |
| 0 | 4096 |

### Spanning Tree Device Configuration

```eos
!
spanning-tree mode mstp
spanning-tree mst 0 priority 4096
```

## Internal VLAN Allocation Policy

### Internal VLAN Allocation Policy Summary

| Policy Allocation | Range Beginning | Range Ending |
| ------------------| --------------- | ------------ |
| ascending | 1006 | 1199 |

### Internal VLAN Allocation Policy Configuration

```eos
!
vlan internal order ascending range 1006 1199
```

## VLANs

### VLANs Summary

| VLAN ID | Name | Trunk Groups |
| ------- | ---- | ------------ |
| 111 | VLAN111 | - |
| 2252 | VLAN2252 | - |
| 2253 | VLAN2253 | - |

### VLANs Device Configuration

```eos
!
vlan 111
   name VLAN111
!
vlan 2252
   name VLAN2252
!
vlan 2253
   name VLAN2253
```

## Interfaces

### Ethernet Interfaces

#### Ethernet Interfaces Summary

##### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | Channel-Group |
| --------- | ----------- | ---- | ----- | ----------- | ----------- | ------------- |
| Ethernet1 |  AMBER_VLAN111 | access | 111 | - | - | - |
| Ethernet2 |  AMBER_VLAN111 | access | 111 | - | - | - |
| Ethernet3 |  AMBER_VLAN111 | access | 111 | - | - | - |
| Ethernet4 |  AMBER_VLAN111 | access | 111 | - | - | - |
| Ethernet5 |  AMBER_VLAN111 | access | 111 | - | - | - |
| Ethernet7 |  AMBER_VLAN111 | access | 111 | - | - | - |
| Ethernet8 |  AMBER_VLAN111 | access | 111 | - | - | - |
| Ethernet9 |  AMBER_VLAN111 | access | 111 | - | - | - |
| Ethernet10 |  AMBER_VLAN111 | access | 111 | - | - | - |
| Ethernet11 |  AMBER_VLAN111 | access | 111 | - | - | - |
| Ethernet12 |  AMBER_VLAN111 | access | 111 | - | - | - |
| Ethernet13 |  C100-1 P1-1 | access | 2253 | - | - | - |
| Ethernet14 |  C100-1 P1-2 | access | 2253 | - | - | - |
| Ethernet15 |  AMBER_VLAN111 | access | 111 | - | - | - |
| Ethernet16 |  C100-1 P1-4 | access | 2253 | - | - | - |
| Ethernet25 |  AMBER_VLAN111 | access | 111 | - | - | - |
| Ethernet26 |  AMBER_VLAN111 | access | 111 | - | - | - |
| Ethernet41 |  AMBER_VLAN111 | access | 111 | - | - | - |
| Ethernet42 |  AMBER_VLAN111 | access | 111 | - | - | - |
| Ethernet43 |  AMBER_VLAN111 | access | 111 | - | - | - |
| Ethernet44 |  AMBER_VLAN111 | access | 111 | - | - | - |
| Ethernet45 |  AMBER_VLAN111 | access | 111 | - | - | - |
| Ethernet46 |  AMBER_VLAN111 | access | 111 | - | - | - |
| Ethernet47 |  AMBER_VLAN111 | access | 111 | - | - | - |
| Ethernet48 |  AMBER_VLAN111 | access | 111 | - | - | - |
| Ethernet50/1 |  SHUTDOWN_SPINE_LINKS | access | - | - | - | - |
| Ethernet51/1 |  SHUTDOWN_SPINE_LINKS | access | - | - | - | - |
| Ethernet52/1 |  SHUTDOWN_SPINE_LINKS | access | - | - | - | - |
| Ethernet53/1 |  EVS Neuron | access | 2252 | - | - | - |

*Inherited from Port-Channel Interface

##### Multicast Routing

| Interface | IP Version | Static Routes Allowed | Multicast Boundaries |
| --------- | ---------- | --------------------- | -------------------- |
| Ethernet6 | IPv4 | True | - |
| Ethernet17 | IPv4 | True | - |
| Ethernet18 | IPv4 | True | - |
| Ethernet19 | IPv4 | True | - |
| Ethernet20 | IPv4 | True | - |
| Ethernet49/1 | IPv4 | True | - |
| Ethernet54/1 | IPv4 | True | - |

##### IPv4

| Interface | Description | Type | Channel Group | IP Address | VRF |  MTU | Shutdown | ACL In | ACL Out |
| --------- | ----------- | -----| ------------- | ---------- | ----| ---- | -------- | ------ | ------- |
| Ethernet6 | DirectOut EXBOX | routed | - | 192.168.40.22/30 | default | - | True | - | - |
| Ethernet17 | C100-2 P1-1 | routed | - | 172.24.225.49/30 | default | - | True | - | - |
| Ethernet18 | C100-2 P1-2 | routed | - | 172.24.225.53/30 | default | - | True | - | - |
| Ethernet19 | C100-2 P1-3 | routed | - | 172.24.225.57/30 | default | - | True | - | - |
| Ethernet20 | C100-2 P1-4 | routed | - | 172.24.225.61/30 | default | - | True | - | - |
| Ethernet49/1 | P2P_LINK_TO_AMBER-SPINE1_Ethernet1/1 | routed | - | 10.255.254.1/31 | default | 9214 | False | - | - |
| Ethernet54/1 | Imagine SNP-2118212563-Data-A | routed | - | 172.24.100.1/30 | default | - | False | - | - |

#### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet1
   description AMBER_VLAN111
   shutdown
   switchport access vlan 111
   switchport mode access
   switchport
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet2
   description AMBER_VLAN111
   shutdown
   switchport access vlan 111
   switchport mode access
   switchport
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet3
   description AMBER_VLAN111
   shutdown
   switchport access vlan 111
   switchport mode access
   switchport
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet4
   description AMBER_VLAN111
   shutdown
   switchport access vlan 111
   switchport mode access
   switchport
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet5
   description AMBER_VLAN111
   shutdown
   switchport access vlan 111
   switchport mode access
   switchport
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet6
   description DirectOut EXBOX
   shutdown
   speed forced 1000full
   no switchport
   ip address 192.168.40.22/30
   multicast ipv4 static
   pim ipv4 sparse-mode
   ptp enable
   ptp sync-message interval -3
   ptp announce interval 0
   ptp transport ipv4
   ptp announce timeout 3
   ptp delay-req interval -3
   ptp role master
!
interface Ethernet7
   description AMBER_VLAN111
   shutdown
   switchport access vlan 111
   switchport mode access
   switchport
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet8
   description AMBER_VLAN111
   shutdown
   switchport access vlan 111
   switchport mode access
   switchport
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet9
   description AMBER_VLAN111
   shutdown
   switchport access vlan 111
   switchport mode access
   switchport
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet10
   description AMBER_VLAN111
   shutdown
   switchport access vlan 111
   switchport mode access
   switchport
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet11
   description AMBER_VLAN111
   shutdown
   switchport access vlan 111
   switchport mode access
   switchport
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet12
   description AMBER_VLAN111
   shutdown
   switchport access vlan 111
   switchport mode access
   switchport
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet13
   description C100-1 P1-1
   no shutdown
   speed forced 10000full
   switchport access vlan 2253
   switchport mode access
   switchport
   ptp enable
   ptp sync-message interval -3
   ptp announce interval 0
   ptp transport ipv4
   ptp announce timeout 3
   ptp delay-req interval -3
   ptp role master
!
interface Ethernet14
   description C100-1 P1-2
   no shutdown
   speed forced 10000full
   switchport access vlan 2253
   switchport mode access
   switchport
   ptp enable
   ptp sync-message interval -3
   ptp announce interval 0
   ptp transport ipv4
   ptp announce timeout 3
   ptp delay-req interval -3
   ptp role master
!
interface Ethernet15
   description AMBER_VLAN111
   shutdown
   switchport access vlan 111
   switchport mode access
   switchport
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet16
   description C100-1 P1-4
   no shutdown
   speed forced 10000full
   switchport access vlan 2253
   switchport mode access
   switchport
   ptp enable
   ptp sync-message interval -3
   ptp announce interval 0
   ptp transport ipv4
   ptp announce timeout 3
   ptp delay-req interval -3
   ptp role master
!
interface Ethernet17
   description C100-2 P1-1
   shutdown
   speed forced 10000full
   no switchport
   ip address 172.24.225.49/30
   multicast ipv4 static
   pim ipv4 sparse-mode
   ptp enable
   ptp sync-message interval -3
   ptp announce interval 0
   ptp transport ipv4
   ptp announce timeout 3
   ptp delay-req interval -3
   ptp role master
!
interface Ethernet18
   description C100-2 P1-2
   shutdown
   speed forced 10000full
   no switchport
   ip address 172.24.225.53/30
   multicast ipv4 static
   pim ipv4 sparse-mode
   ptp enable
   ptp sync-message interval -3
   ptp announce interval 0
   ptp transport ipv4
   ptp announce timeout 3
   ptp delay-req interval -3
   ptp role master
!
interface Ethernet19
   description C100-2 P1-3
   shutdown
   speed forced 10000full
   no switchport
   ip address 172.24.225.57/30
   multicast ipv4 static
   pim ipv4 sparse-mode
   ptp enable
   ptp sync-message interval -3
   ptp announce interval 0
   ptp transport ipv4
   ptp announce timeout 3
   ptp delay-req interval -3
   ptp role master
!
interface Ethernet20
   description C100-2 P1-4
   shutdown
   speed forced 10000full
   no switchport
   ip address 172.24.225.61/30
   multicast ipv4 static
   pim ipv4 sparse-mode
   ptp enable
   ptp sync-message interval -3
   ptp announce interval 0
   ptp transport ipv4
   ptp announce timeout 3
   ptp delay-req interval -3
   ptp role master
!
interface Ethernet21
   description mcs senders/receivers
   shutdown
   speed forced 10000full
   no switchport
!
interface Ethernet22
   description mcs senders/receivers
   shutdown
   speed forced 10000full
   no switchport
!
interface Ethernet23
   description mcs senders/receivers
   shutdown
   speed forced 10000full
   no switchport
!
interface Ethernet24
   description mcs senders/receivers
   shutdown
   speed forced 10000full
   no switchport
!
interface Ethernet25
   description AMBER_VLAN111
   shutdown
   switchport access vlan 111
   switchport mode access
   switchport
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet26
   description AMBER_VLAN111
   shutdown
   switchport access vlan 111
   switchport mode access
   switchport
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet27
   description mcs senders/receivers
   shutdown
   speed forced 10000full
   no switchport
!
interface Ethernet28
   description mcs senders/receivers
   shutdown
   speed forced 10000full
   no switchport
!
interface Ethernet29
   description mcs senders/receivers
   shutdown
   speed forced 10000full
   no switchport
!
interface Ethernet30
   description mcs senders/receivers
   shutdown
   speed forced 10000full
   no switchport
!
interface Ethernet31
   description mcs senders/receivers
   shutdown
   speed forced 10000full
   no switchport
!
interface Ethernet32
   description mcs senders/receivers
   shutdown
   speed forced 10000full
   no switchport
!
interface Ethernet33
   description mcs senders/receivers
   shutdown
   speed forced 10000full
   no switchport
!
interface Ethernet34
   description mcs senders/receivers
   shutdown
   speed forced 10000full
   no switchport
!
interface Ethernet35
   description mcs senders/receivers
   shutdown
   speed forced 10000full
   no switchport
!
interface Ethernet36
   description mcs senders/receivers
   shutdown
   speed forced 10000full
   no switchport
!
interface Ethernet37
   description mcs senders/receivers
   shutdown
   speed forced 10000full
   no switchport
!
interface Ethernet38
   description mcs senders/receivers
   shutdown
   speed forced 10000full
   no switchport
!
interface Ethernet39
   description mcs senders/receivers
   shutdown
   speed forced 10000full
   no switchport
!
interface Ethernet40
   description mcs senders/receivers
   shutdown
   speed forced 10000full
   no switchport
!
interface Ethernet41
   description AMBER_VLAN111
   shutdown
   switchport access vlan 111
   switchport mode access
   switchport
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet42
   description AMBER_VLAN111
   shutdown
   switchport access vlan 111
   switchport mode access
   switchport
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet43
   description AMBER_VLAN111
   shutdown
   switchport access vlan 111
   switchport mode access
   switchport
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet44
   description AMBER_VLAN111
   shutdown
   switchport access vlan 111
   switchport mode access
   switchport
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet45
   description AMBER_VLAN111
   shutdown
   switchport access vlan 111
   switchport mode access
   switchport
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet46
   description AMBER_VLAN111
   shutdown
   switchport access vlan 111
   switchport mode access
   switchport
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet47
   description AMBER_VLAN111
   shutdown
   switchport access vlan 111
   switchport mode access
   switchport
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet48
   description AMBER_VLAN111
   shutdown
   switchport access vlan 111
   switchport mode access
   switchport
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet49/1
   description P2P_LINK_TO_AMBER-SPINE1_Ethernet1/1
   no shutdown
   mtu 9214
   no switchport
   ip address 10.255.254.1/31
   multicast ipv4 static
   pim ipv4 sparse-mode
!
interface Ethernet50/1
   description SHUTDOWN_SPINE_LINKS
   shutdown
   switchport
!
interface Ethernet51/1
   description SHUTDOWN_SPINE_LINKS
   shutdown
   switchport
!
interface Ethernet52/1
   description SHUTDOWN_SPINE_LINKS
   shutdown
   switchport
!
interface Ethernet53/1
   description EVS Neuron
   no shutdown
   speed forced 100Gfull
   switchport access vlan 2252
   switchport mode access
   switchport
   ptp enable
   ptp sync-message interval -3
   ptp announce interval 0
   ptp transport ipv4
   ptp announce timeout 3
   ptp delay-req interval -3
   ptp role master
!
interface Ethernet54/1
   description Imagine SNP-2118212563-Data-A
   no shutdown
   speed forced 100Gfull
   no switchport
   ip address 172.24.100.1/30
   multicast ipv4 static
   pim ipv4 sparse-mode
   ptp enable
   ptp sync-message interval -3
   ptp announce interval 0
   ptp transport ipv4
   ptp announce timeout 3
   ptp delay-req interval -3
   ptp role master
```

### Loopback Interfaces

#### Loopback Interfaces Summary

##### IPv4

| Interface | Description | VRF | IP Address |
| --------- | ----------- | --- | ---------- |
| Loopback0 | Router_ID | default | 10.255.1.3/32 |

##### IPv6

| Interface | Description | VRF | IPv6 Address |
| --------- | ----------- | --- | ------------ |
| Loopback0 | Router_ID | default | - |


#### Loopback Interfaces Device Configuration

```eos
!
interface Loopback0
   description Router_ID
   no shutdown
   ip address 10.255.1.3/32
```

### VLAN Interfaces

#### VLAN Interfaces Summary

| Interface | Description | VRF |  MTU | Shutdown |
| --------- | ----------- | --- | ---- | -------- |
| Vlan111 | VLAN111 | default | - | False |
| Vlan2252 | VLAN2252 | default | - | False |
| Vlan2253 | VLAN2253 | default | - | False |

##### IPv4

| Interface | VRF | IP Address | IP Address Virtual | IP Router Virtual Address | VRRP | ACL In | ACL Out |
| --------- | --- | ---------- | ------------------ | ------------------------- | ---- | ------ | ------- |
| Vlan111 |  default  |  10.252.9.1/24  |  -  |  -  |  -  |  -  |  -  |
| Vlan2252 |  default  |  172.24.225.17/28  |  -  |  -  |  -  |  -  |  -  |
| Vlan2253 |  default  |  172.24.225.33/28  |  -  |  -  |  -  |  -  |  -  |

##### Multicast Routing

| Interface | IP Version | Static Routes Allowed | Multicast Boundaries | Export Host Routes For Multicast Sources |
| --------- | ---------- | --------------------- | -------------------- | ---------------------------------------- |
| Vlan2252 | IPv4 | True | - | - |
| Vlan2253 | IPv4 | True | - | - |

#### VLAN Interfaces Device Configuration

```eos
!
interface Vlan111
   description VLAN111
   no shutdown
   no autostate
   ip address 10.252.9.1/24
   ip helper-address 10.252.4.253
!
interface Vlan2252
   description VLAN2252
   no shutdown
   no autostate
   ip address 172.24.225.17/28
   multicast ipv4 static
   pim ipv4 sparse-mode
!
interface Vlan2253
   description VLAN2253
   no shutdown
   no autostate
   ip address 172.24.225.33/28
   multicast ipv4 static
   pim ipv4 sparse-mode
```

## Routing

### Service Routing Protocols Model

Multi agent routing protocol model enabled

```eos
!
service routing protocols model multi-agent
```

### Virtual Router MAC Address

#### Virtual Router MAC Address Summary

##### Virtual Router MAC Address: 00:1c:73:00:00:99

#### Virtual Router MAC Address Configuration

```eos
!
ip virtual-router mac-address 00:1c:73:00:00:99
```

### IP Routing

#### IP Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | True |
| MGMT | False |

#### IP Routing Device Configuration

```eos
!
ip routing
no ip routing vrf MGMT
```

### IPv6 Routing

#### IPv6 Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | False |
| MGMT | false |

### Static Routes

#### Static Routes Summary

| VRF | Destination Prefix | Next Hop IP             | Exit interface      | Administrative Distance       | Tag               | Route Name                    | Metric         |
| --- | ------------------ | ----------------------- | ------------------- | ----------------------------- | ----------------- | ----------------------------- | -------------- |
| MGMT | 0.0.0.0/0 | 10.90.227.1 | - | 1 | - | - | - |

#### Static Routes Device Configuration

```eos
!
ip route vrf MGMT 0.0.0.0/0 10.90.227.1
```

### Router BGP

#### Router BGP Summary

| BGP AS | Router ID |
| ------ | --------- |
| 65101|  10.255.1.3 |

| BGP Tuning |
| ---------- |
| update wait-install |
| no bgp default ipv4-unicast |
| maximum-paths 4 ecmp 4 |

#### Router BGP Peer Groups

##### IPv4-UNDERLAY-PEERS

| Settings | Value |
| -------- | ----- |
| Address Family | ipv4 |
| Send community | all |
| Maximum routes | 12000 |

#### BGP Neighbors

| Neighbor | Remote AS | VRF | Shutdown | Send-community | Maximum-routes | Allowas-in | BFD | RIB Pre-Policy Retain | Route-Reflector Client | Passive |
| -------- | --------- | --- | -------- | -------------- | -------------- | ---------- | --- | --------------------- | ---------------------- | ------- |
| 10.255.254.0 | 65100 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |

#### Router BGP Device Configuration

```eos
!
router bgp 65101
   router-id 10.255.1.3
   maximum-paths 4 ecmp 4
   update wait-install
   no bgp default ipv4-unicast
   neighbor IPv4-UNDERLAY-PEERS peer group
   neighbor IPv4-UNDERLAY-PEERS password 7 <removed>
   neighbor IPv4-UNDERLAY-PEERS send-community
   neighbor IPv4-UNDERLAY-PEERS maximum-routes 12000
   neighbor 10.255.254.0 peer group IPv4-UNDERLAY-PEERS
   neighbor 10.255.254.0 remote-as 65100
   neighbor 10.255.254.0 description amber-spine1_Ethernet1/1
   redistribute connected
   !
   address-family ipv4
      neighbor IPv4-UNDERLAY-PEERS activate
```

## Multicast

### IP IGMP Snooping

#### IP IGMP Snooping Summary

| IGMP Snooping | Fast Leave | Interface Restart Query | Proxy | Restart Query Interval | Robustness Variable |
| ------------- | ---------- | ----------------------- | ----- | ---------------------- | ------------------- |
| Enabled | - | - | - | - | - |

#### IP IGMP Snooping Device Configuration

```eos
```

### Router Multicast

#### IP Router Multicast Summary

- Routing for IPv4 multicast is enabled.

#### Router Multicast Device Configuration

```eos
!
router multicast
   ipv4
      routing
```


### PIM Sparse Mode

#### Router PIM Sparse Mode

##### IP Sparse Mode Information

BFD enabled: False

####### IP Rendezvous Information

| Rendezvous Point Address | Group Address | Access Lists | Priority | Hashmask | Override |
| ------------------------ | ------------- | ------------ | -------- | -------- | -------- |
| 172.24.0.10 | - | - | - | - | - |

##### Router Multicast Device Configuration

```eos
!
router pim sparse-mode
   ipv4
      rp address 172.24.0.10
```

#### PIM Sparse Mode enabled interfaces

| Interface Name | VRF Name | IP Version | DR Priority | Local Interface |
| -------------- | -------- | ---------- | ----------- | --------------- |
| Ethernet6 | - | IPv4 | - | - |
| Ethernet17 | - | IPv4 | - | - |
| Ethernet18 | - | IPv4 | - | - |
| Ethernet19 | - | IPv4 | - | - |
| Ethernet20 | - | IPv4 | - | - |
| Ethernet49/1 | - | IPv4 | - | - |
| Ethernet54/1 | - | IPv4 | - | - |
| Vlan2252 | - | IPv4 | - | - |
| Vlan2253 | - | IPv4 | - | - |

## VRF Instances

### VRF Instances Summary

| VRF Name | IP Routing |
| -------- | ---------- |
| MGMT | disabled |

### VRF Instances Device Configuration

```eos
!
vrf instance MGMT
```

## Platform

### Platform Summary

#### Platform Sand Summary

| Settings | Value |
| -------- | ----- |
| Hardware Only Lag | True |

### Platform Configuration

```eos
!
platform sand lag hardware-only
```
