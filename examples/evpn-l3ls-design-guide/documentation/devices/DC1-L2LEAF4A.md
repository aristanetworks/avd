# DC1-L2LEAF4A

## Management Interfaces

### Management Interfaces Summary

| Management Interface | description | VRF | IP Address | Gateway |
| -------------------- | ----------- | --- | ---------- | ------- |
| Management1 | oob_management| MGMT | 192.168.2.112/24 | 192.168.2.1 |

### Management Interfaces Device Configuration

```eos
interface Management1
   description oob_management
   vrf MGMT
   ip address 192.168.2.112/24
!
```

## Hardware Counters

No Hardware Counters defined

## TerminAttr Daemon

### TerminAttr Daemon Summary

| CV Compression | Ingest gRPC URL | Ingest Authentication Key | Smash Excludes | Ingest Exclude | Ingest VRF |  NTP VRF |
| -------------- | --------------- | ------------------------- | -------------- | -------------- | ---------- | -------- |
| gzip | 192.168.2.201:9910 | telarista | ale,flexCounter,hardware,kni,pulse,strata | /Sysdb/cell/1/agent,/Sysdb/cell/2/agent | MGMT | MGMT |

### TerminAttr Daemon Device Configuration

```eos
daemon TerminAttr
   exec /usr/bin/TerminAttr -ingestgrpcurl=192.168.2.201:9910 -cvcompression=gzip -ingestauth=key,telarista -smashexcludes=ale,flexCounter,hardware,kni,pulse,strata -ingestexclude=/Sysdb/cell/1/agent,/Sysdb/cell/2/agent -ingestvrf=MGMT -taillogs
   no shutdown
!
```

## Internal VLAN allocation Policy

### Internal VLAN Allocation Policy Summary

| Policy Allocation | Range Beginning | Range Ending |
| ------------------| --------------- | ------------ |
| ascending | 1006 | 1199 |

### Internal VLAN Allocation Policy Configuration

```eos
vlan internal order ascending range 1006 1199
!
```

## Name Servers

### Name Servers Summary

| Name Server | Source VRF |
| ----------- | ---------- |
| 192.168.2.1 | MGMT |
| 8.8.8.8 | MGMT |

### Name Servers Device Configuration

```eos
ip name-server vrf MGMT 192.168.2.1
ip name-server vrf MGMT 8.8.8.8
!
```

## NTP

### NTP Summary

Local Interface: Management1
VRF: MGMT

| Node | Primary |
| ---- | ------- |
| 0.north-america.pool.ntp.org | True |
| 1.north-america.pool.ntp.org | - |

### NTP Device Configuration

```eos
ntp local-interface vrf MGMT Management1
ntp server vrf MGMT 0.north-america.pool.ntp.org prefer
ntp server vrf MGMT 1.north-america.pool.ntp.org
!
```

## Spanning Tree

### Spanning Tree Summary

Mode: MSTP

| Instance | Priority |
| -------- | -------- |
| 0 | 16384 |

### Spanning Tree Device Configuration

```eos
spanning-tree mode mstp
spanning-tree mst 0 priority 16384
!
```

## AAA Authentication

AAA Not Configured

## Local Users

### Local Users Summary

| User | Privilege | role |
| ---- | --------- | ---- |
| admin | 15 | network-admin |
| cvpadmin | 15 | network-admin |

### Local Users Device Configuration

```eos
username admin privilege 15 role network-admin secret sha512 $6$Df86J4/SFMDE3/1K$Hef4KstdoxNDaami37cBquTWOTplC.miMPjXVgQxMe92.e5wxlnXOLlebgPj8Fz1KO0za/RCO7ZIs4Q6Eiq1g1
username cvpadmin privilege 15 role network-admin secret sha512 $6$rZKcbIZ7iWGAWTUM$TCgDn1KcavS0s.OV8lacMTUkxTByfzcGlFlYUWroxYuU7M/9bIodhRO7nXGzMweUxvbk8mJmQl8Bh44cRktUj.
!
```

## VLANs

### VLANs Summary

| VLAN ID | Name | Trunk Groups |
| ------- | ---- | ------------ |
| 110 | Tenant_A_OP_Zone_1 | none  |
| 111 | Tenant_A_OP_Zone_2 | none  |
| 120 | Tenant_A_WEB_Zone_1 | none  |
| 121 | Tenant_A_WEBZone_2 | none  |
| 130 | Tenant_A_APP_Zone_1 | none  |
| 131 | Tenant_A_APP_Zone_2 | none  |

### VLANs Device Configuration

```eos
vlan 110
   name Tenant_A_OP_Zone_1
!
vlan 111
   name Tenant_A_OP_Zone_2
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
```

## VRF Instances

### VRF Instances Summary

| VRF Name | IP Routing |
| -------- | ---------- |
| MGMT |  disabled |

### VRF Instances Device Configuration

```eos
vrf instance MGMT
!
```

## BFD Multihop Interval

### BFD Multihop Summary

| Interval | Minimum RX | Multiplier |
| -------- | ---------- | ---------- |
| 1200 | 1200 | 3 |

### BFD Multihop Device Configuration

```eos
bfd multihop interval 1200 min_rx 1200 multiplier 3
!
```

## Port-Channel Interfaces

### Port-Channel Interfaces Summary

| Interface | Description | MTU | Type | Mode | Allowed VLANs (trunk) | Trunk Group | MLAG ID | VRF | IP Address |
| --------- | ----------- | --- | ---- | ---- | --------------------- | ----------- | ------- | --- | ---------- |
| Port-Channel11 | DC1-LEAF2A_Po6 | 1500 | switched | trunk | 110-111,120-121,130-131 | - | 11 | - | - |

### Port-Channel Interfaces Device Configuration

```eos
interface Port-Channel11
   description DC1-LEAF2A_Po6
   switchport trunk allowed vlan 110-111,120-121,130-131
   switchport mode trunk
   mlag 11
!
```

## Ethernet Interfaces

### Ethernet Interfaces Summary

| Interface | Description | MTU | Type | Mode | Allowed VLANs (Trunk) | Trunk Group | VRF | IP Address | Channel-Group ID | Channel-Group Type |
| --------- | ----------- | --- | ---- | ---- | --------------------- | ----------- | --- | ---------- | ---------------- | ------------------ |
| Ethernet11 | DC1-LEAF2A_Ethernet6 | *1500 | *switched | *trunk | *110-111,120-121,130-131 | - | - | - | 11 | active |
| Ethernet12 | DC1-LEAF2B_Ethernet6 | *1500 | *switched | *trunk | *110-111,120-121,130-131 | - | - | - | 11 | active |

*Inherited from Port-Channel Interface

### Ethernet Interfaces Device Configuration

```eos
interface Ethernet11
   description DC1-LEAF2A_Ethernet6
   channel-group 11 mode active
!
interface Ethernet12
   description DC1-LEAF2B_Ethernet6
   channel-group 11 mode active
!
```

## Loopback Interfaces

No Loopback interfaces defined

## VLAN Interfaces

No VLAN interfaces defined

## VXLAN Interface

No VXLAN interface defined

## Virtual Router MAC Address & Virtual Source NAT


## Static Routes

### Static Routes Summary

| VRF | Destination Prefix | Fowarding Address / Interface |
| --- | ------------------ | ----------------------------- |
| MGMT | 0.0.0.0/0 | 192.168.2.1 |

### Static Routes Device Configuration

```eos
ip route vrf MGMT 0.0.0.0/0 192.168.2.1
!
```

## IP Routing

### IP Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| MGMT | False |

### IP Routing Device Configuration

```eos
ip routing
no ip routing vrf MGMT
!
```

## Prefix Lists

Prefix lists not defined

## MLAG

MLAG not defined

## Route Maps

No route maps defined

## Peer Filters

No Peer Filters defined

## Router BGP

Router BGP not defined
