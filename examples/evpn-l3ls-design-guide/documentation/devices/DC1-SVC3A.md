# DC1-SVC3A

## Management Interfaces

### Management Interfaces Summary

| Management Interface | description | VRF | IP Address | Gateway |
| -------------------- | ----------- | --- | ---------- | ------- |
| Management1 | oob_management| MGMT | 192.168.2.108/24 | 192.168.2.1 |

### Management Interfaces Device Configuration

```eos
interface Management1
   description oob_management
   vrf MGMT
   ip address 192.168.2.108/24
!
```

## TerminAttr Daemon

### TerminAttr Daemon Summary

| CV Compression | Ingest gRPC URL | Ingest Authentication Key | Smash Excludes | Ingest Exclude | Ingest VRF |  NTP VRF |
| -------------- | --------------- | ------------------------- | -------------- | -------------- | ---------- | -------- |
| gzip | 192.168.2.201:9910 | telarista | ale,flexCounter,hardware,kni,pulse,strata | /Sysdb/cell/1/agent,/Sysdb/cell/2/agent | MGMT | MGMT |

### TerminAttr Daemon Device Configuration

```eos
daemon TerminAttr
   exec /usr/bin/TerminAttr -cvcompression=gzip -ingestgrpcurl=192.168.2.201:9910 -taillogs -ingestauth=key,telarista -smashexcludes=ale,flexCounter,hardware,kni,pulse,strata -ingestexclude=/Sysdb/cell/1/agent,/Sysdb/cell/2/agent -ingestvrf=MGMT -ntpvrf=MGMT
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
vlan internal allocation policy ascending range 1006 1199
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
| 0 | 4096 |

### Spanning Tree Device Configuration

```eos
spanning-tree mode mstp
no spanning-tree vlan-id 4094
spanning-tree mst 0 priority 4096
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
| 110 | Tenant_A_OPZone_1 | none  |
| 111 | Tenant_A_OPZone_2 | none  |
| 210 | Tenant_B_OPZone_1 | none  |
| 211 | Tenant_B_OPZone_2 | none  |
| 310 | Tenant_C_OPZone_1 | none  |
| 311 | Tenant_C_OPZone_2 | none  |
| 3000 | MLAG_iBGP_Tenant_A_OPZone | LEAF_PEER_L3  |
| 3001 | MLAG_iBGP_Tenant_B_OPZone | LEAF_PEER_L3  |
| 3002 | MLAG_iBGP_Tenant_C_OPZone | LEAF_PEER_L3  |
| 4093 | LEAF_PEER_L3 | LEAF_PEER_L3  |
| 4094 | MLAG_PEER | MLAG  |

### VLANs Device Configuration

```eos
vlan 110
   name Tenant_A_OPZone_1
!
vlan 111
   name Tenant_A_OPZone_2
!
vlan 210
   name Tenant_B_OPZone_1
!
vlan 211
   name Tenant_B_OPZone_2
!
vlan 310
   name Tenant_C_OPZone_1
!
vlan 311
   name Tenant_C_OPZone_2
!
vlan 3000
   name MLAG_iBGP_Tenant_A_OPZone
   trunk group LEAF_PEER_L3
!
vlan 3001
   name MLAG_iBGP_Tenant_B_OPZone
   trunk group LEAF_PEER_L3
!
vlan 3002
   name MLAG_iBGP_Tenant_C_OPZone
   trunk group LEAF_PEER_L3
!
vlan 4093
   name LEAF_PEER_L3
   trunk group LEAF_PEER_L3
!
vlan 4094
   name MLAG_PEER
   trunk group MLAG
!
```

## VRF Instances

### VRF Instances Summary

| VRF Name | IP Routing |
| -------- | ---------- |
| MGMT |  disabled |
| Tenant_A_OPZone |  enabled |
| Tenant_B_OPZone |  enabled |
| Tenant_C_OPZone |  enabled |

### VRF Instances Device Configuration

```eos
vrf instance MGMT
!
vrf instance Tenant_A_OPZone
!
vrf instance Tenant_B_OPZone
!
vrf instance Tenant_C_OPZone
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
| Port-Channel3 | MLAG_PEER_DC1-SVC3B_Po3 | 1500 | switched | trunk | 2-4094 | LEAF_PEER_L3<br> MLAG | - | - | - |
| Port-Channel5 | DC1_L2LEAF5_Po1 | 1500 | switched | trunk | 2-4092 | - | 5 | - | - |
| Port-Channel10 | server03_PortChanne1 | 1500 | switched | trunk | 110-111,210-211 | - | 10 | - | - |
| Port-Channel11 | server04_PortChanne1 | 1500 | switched | trunk | 110-111,210-211 | - | 11 | - | - |

### Port-Channel Interfaces Device Configuration

```eos
interface Port-Channel3
   description MLAG_PEER_DC1-SVC3B_Po3
   switchport trunk allowed vlan 2-4094
   switchport mode trunk
   switchport trunk group LEAF_PEER_L3
   switchport trunk group MLAG
!
interface Port-Channel5
   description DC1_L2LEAF5_Po1
   switchport trunk allowed vlan 2-4092
   switchport mode trunk
   mlag 5
!
interface Port-Channel10
   description server03_PortChanne1
   switchport trunk allowed vlan 110-111,210-211
   switchport mode trunk
   mlag 10
!
interface Port-Channel11
   description server04_PortChanne1
   switchport trunk allowed vlan 110-111,210-211
   switchport mode trunk
   mlag 11
!
```

## Ethernet Interfaces

### Ethernet Interfaces Summary

| Interface | Description | MTU | Type | Mode | Allowed VLANs (Trunk) | Trunk Group | VRF | IP Address | Channel-Group ID | Channel-Group Type |
| --------- | ----------- | --- | ---- | ---- | --------------------- | ----------- | --- | ---------- | ---------------- | ------------------ |
| Ethernet1 | P2P_UPLINK_TO_DC1-SPINE1_Ethernet4 | 1500 | routed | access | - | - | - | 172.31.255.13/31 | - | - |
| Ethernet2 | P2P_UPLINK_TO_DC1-SPINE2_Ethernet4 | 1500 | routed | access | - | - | - | 172.31.255.15/31 | - | - |
| Ethernet3 | MLAG_PEER_DC1-SVC3B_Ethernet3 | *1500 | *switched | *trunk | *2-4094 | *LEAF_PEER_L3<br> *MLAG | - | - | 3 | active |
| Ethernet4 | MLAG_PEER_DC1-SVC3B_Ethernet4 | *1500 | *switched | *trunk | *2-4094 | *LEAF_PEER_L3<br> *MLAG | - | - | 3 | active |
| Ethernet5 | DC1-L2LEAF5A_Ethernet1 | *1500 | *switched | *trunk | *2-4092 | - | - | - | 5 | active |
| Ethernet6 | DC1-L2LEAF5B_Ethernet1 | *1500 | *switched | *trunk | *2-4092 | - | - | - | 5 | active |
| Ethernet10 | server03_Eth1 | *1500 | *switched | *trunk | *110-111,210-211 | - | - | - | 10 | active |
| Ethernet11 | server04_Eth1 | *1500 | *switched | *trunk | *110-111,210-211 | - | - | - | 11 | active |

*Inherited from Port-Channel Interface

### Ethernet Interfaces Device Configuration

```eos
interface Ethernet1
   description P2P_UPLINK_TO_DC1-SPINE1_Ethernet4
   no switchport
   ip address 172.31.255.13/31
!
interface Ethernet2
   description P2P_UPLINK_TO_DC1-SPINE2_Ethernet4
   no switchport
   ip address 172.31.255.15/31
!
interface Ethernet3
   description MLAG_PEER_DC1-SVC3B_Ethernet3
   channel-group 3 mode active
!
interface Ethernet4
   description MLAG_PEER_DC1-SVC3B_Ethernet4
   channel-group 3 mode active
!
interface Ethernet5
   description DC1-L2LEAF5A_Ethernet1
   channel-group 5 mode active
!
interface Ethernet6
   description DC1-L2LEAF5B_Ethernet1
   channel-group 5 mode active
!
interface Ethernet10
   description server03_Eth1
   channel-group 10 mode active
!
interface Ethernet11
   description server04_Eth1
   channel-group 11 mode active
!
```

## Loopback Interfaces

### Loopback Interfaces Summary

| Interface | Description | VRF | IP Address |
| --------- | ----------- | --- | ---------- |
| Loopback0 | EVPN_Overlay_Peering | Global Routing Table | 192.168.255.6/32 |
| Loopback1 | VTEP_VXLAN_Tunnel_Source | Global Routing Table | 192.168.254.6/32 |
| Loopback101 | Tenant_A_OPZone_VTEP_DIAGNOSTICS | Tenant_A_OPZone | 10.1.255.6/32 |
| Loopback202 | Tenant_B_OPZone_VTEP_DIAGNOSTICS | Tenant_B_OPZone | 10.2.255.6/32 |
| Loopback303 | Tenant_C_OPZone_VTEP_DIAGNOSTICS | Tenant_C_OPZone | 10.3.255.6/32 |

### Loopback Interfaces Device Configuration

```eos
interface Loopback0
   description EVPN_Overlay_Peering
   ip address 192.168.255.6/32
!
interface Loopback1
   description VTEP_VXLAN_Tunnel_Source
   ip address 192.168.254.6/32
!
interface Loopback101
   description Tenant_A_OPZone_VTEP_DIAGNOSTICS
   vrf Tenant_A_OPZone
   ip address 10.1.255.6/32
!
interface Loopback202
   description Tenant_B_OPZone_VTEP_DIAGNOSTICS
   vrf Tenant_B_OPZone
   ip address 10.2.255.6/32
!
interface Loopback303
   description Tenant_C_OPZone_VTEP_DIAGNOSTICS
   vrf Tenant_C_OPZone
   ip address 10.3.255.6/32
!
```

## VLAN Interfaces

### VLAN Interfaces Summary

| Interface | Description | VRF | IP Address | Virtual | IP Address Secondary | Virtual |
| --------- | ----------- | --- | ---------- | ------- | -------------------- | ------- |
| Vlan110 | Tenant_A_OPZone_1 | Tenant_A_OPZone  | 10.1.10.1/24 | True | 10.1.100.1/24 | True |
| Vlan111 | Tenant_A_OPZone_2 | Tenant_A_OPZone  | 10.1.11.1/24 | True | - | - |
| Vlan210 | Tenant_B_OPZone_1 | Tenant_B_OPZone  | 10.2.10.1/24 | True | - | - |
| Vlan211 | Tenant_B_OPZone_2 | Tenant_B_OPZone  | 10.2.11.1/24 | True | - | - |
| Vlan310 | Tenant_C_OPZone_1 | Tenant_C_OPZone  | 10.3.10.1/24 | True | - | - |
| Vlan311 | Tenant_C_OPZone_2 | Tenant_C_OPZone  | 10.3.11.1/24 | True | - | - |
| Vlan3000 | MLAG_PEER_L3_iBGP: vrf Tenant_A_OPZone | Tenant_A_OPZone  | 10.255.251.6/31 | - | - | - |
| Vlan3001 | MLAG_PEER_L3_iBGP: vrf Tenant_B_OPZone | Tenant_B_OPZone  | 10.255.251.6/31 | - | - | - |
| Vlan3002 | MLAG_PEER_L3_iBGP: vrf Tenant_C_OPZone | Tenant_C_OPZone  | 10.255.251.6/31 | - | - | - |
| Vlan4093 | MLAG_PEER_L3_iBGP | Global Routing Table  | 10.255.251.6/31 | - | - | - |
| Vlan4094 | MLAG_PEER | Global Routing Table  | 10.255.252.6/31 | - | - | - |

### VLAN Interfaces Device Configuration

```eos
interface Vlan110
   description Tenant_A_OPZone_1
   vrf Tenant_A_OPZone
   ip address virtual 10.1.10.1/24
   ip address virtual 10.1.100.1/24 secondary
!
interface Vlan111
   description Tenant_A_OPZone_2
   vrf Tenant_A_OPZone
   ip address virtual 10.1.11.1/24
!
interface Vlan210
   description Tenant_B_OPZone_1
   vrf Tenant_B_OPZone
   ip address virtual 10.2.10.1/24
!
interface Vlan211
   description Tenant_B_OPZone_2
   vrf Tenant_B_OPZone
   ip address virtual 10.2.11.1/24
!
interface Vlan310
   description Tenant_C_OPZone_1
   vrf Tenant_C_OPZone
   ip address virtual 10.3.10.1/24
!
interface Vlan311
   description Tenant_C_OPZone_2
   vrf Tenant_C_OPZone
   ip address virtual 10.3.11.1/24
!
interface Vlan3000
   description MLAG_PEER_L3_iBGP: vrf Tenant_A_OPZone
   vrf Tenant_A_OPZone
   ip address 10.255.251.6/31
!
interface Vlan3001
   description MLAG_PEER_L3_iBGP: vrf Tenant_B_OPZone
   vrf Tenant_B_OPZone
   ip address 10.255.251.6/31
!
interface Vlan3002
   description MLAG_PEER_L3_iBGP: vrf Tenant_C_OPZone
   vrf Tenant_C_OPZone
   ip address 10.255.251.6/31
!
interface Vlan4093
   description MLAG_PEER_L3_iBGP
   ip address 10.255.251.6/31
!
interface Vlan4094
   description MLAG_PEER
   no autostate
   ip address 10.255.252.6/31
!
```

## VXLAN Interface

### VXLAN Interface Summary

**Source Interface:** Loopback1
**UDP port:** 4789

**VLAN to VNI Mappings:**

| VLAN | VNI |
| ---- | --- |
| 110 | 10110 |
| 111 | 10111 |
| 210 | 20210 |
| 211 | 20211 |
| 310 | 30310 |
| 311 | 30311 |

**VRF to VNI Mappings:**

| VLAN | VNI |
| ---- | --- |
| Tenant_A_OPZone | 15001 |
| Tenant_B_OPZone | 25002 |
| Tenant_C_OPZone | 35003 |

### VXLAN Interface Device Configuration

```eos
interface Vxlan1
   vxlan source-interface Loopback1
   vxlan virtual-router encapsulation mac-address mlag-system-id
   vxlan udp-port 4789
   vxlan vlan 110 vni 10110
   vxlan vlan 111 vni 10111
   vxlan vlan 210 vni 20210
   vxlan vlan 211 vni 20211
   vxlan vlan 310 vni 30310
   vxlan vlan 311 vni 30311
   vxlan vrf Tenant_A_OPZone vni 15001
   vxlan vrf Tenant_B_OPZone vni 25002
   vxlan vrf Tenant_C_OPZone vni 35003
!
```

## Virtual Router MAC Address

### Virtual Router MAC Address Summary

**Virtual Router MAC Address:** 00:1c:73:00:dc:01

### Virtual Router MAC Address Device Configuration

```eos
ip virtual-router mac-address 00:1c:73:00:dc:01
```

## Virtual Source NAT

### Virtual Source NAT Summary

| Source NAT VRF | Source NAT IP Address |
| -------------- | --------------------- |
| Tenant_A_OPZone | 10.1.255.6 |
| Tenant_B_OPZone | 10.2.255.6 |
| Tenant_C_OPZone | 10.3.255.6 |

### Virtual Source NAT Device Configuration

```eos
ip address virtual source-nat vrf Tenant_A_OPZone address 10.1.255.6
ip address virtual source-nat vrf Tenant_B_OPZone address 10.2.255.6
ip address virtual source-nat vrf Tenant_C_OPZone address 10.3.255.6
!
```

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
| Tenant_A_OPZone | True |
| Tenant_B_OPZone | True |
| Tenant_C_OPZone | True |

### IP Routing Device Configuration

```eos
ip routing
no ip routing vrf MGMT
ip routing vrf Tenant_A_OPZone
ip routing vrf Tenant_B_OPZone
ip routing vrf Tenant_C_OPZone
!
```

## Prefix Lists

### Prefix Lists Summary

**PL-LOOPBACKS-EVPN-OVERLAY:**

| Sequence | Action |
| -------- | ------ |
| 10 | permit 192.168.255.0/24 eq 32 |
| 20 | permit 192.168.254.0/24 eq 32 |

**PL-P2P-UNDERLAY:**

| Sequence | Action |
| -------- | ------ |
| 10 | permit 172.31.255.0/24 le 31 |
| 20 | permit 10.255.251.0/24 le 31 |

### Prefix Lists Device Configuration

```eos
ip prefix-list PL-LOOPBACKS-EVPN-OVERLAY
   seq 10 permit 192.168.255.0/24 eq 32
   seq 20 permit 192.168.254.0/24 eq 32
!
ip prefix-list PL-P2P-UNDERLAY
   seq 10 permit 172.31.255.0/24 le 31
   seq 20 permit 10.255.251.0/24 le 31
!
```

## MLAG

### MLAG Summary

| domain-id | local-interface | peer-address | peer-link |
| --------- | --------------- | ------------ | --------- |
| DC1_SVC3 | Vlan4094 | 10.255.252.7 | Port-Channel3 |

### MLAG Device Configuration

```eos
mlag configuration
   domain-id DC1_SVC3
   local-interface Vlan4094
   peer-address 10.255.252.7
   peer-link Port-Channel3
!
```

## Route Maps

### Route Maps Summary

**RM-CONN-2-BGP:**

| Sequence | Type | Match |
| -------- | ---- | ----- |
| 10 | permit | ip address prefix-list PL-LOOPBACKS-EVPN-OVERLAY |
| 20 | permit | ip address prefix-list PL-P2P-UNDERLAY |

### Route Maps Device Configuration

```eos
route-map RM-CONN-2-BGP permit 10
   match ip address prefix-list PL-LOOPBACKS-EVPN-OVERLAY
!
route-map RM-CONN-2-BGP permit 20
   match ip address prefix-list PL-P2P-UNDERLAY
!
```

## Peer Filters

No Peer Filters defined

## Router BGP

### Router BGP Summary

| BGP AS | Router ID |
| ------ | --------- |
| 65103|  192.168.255.6 |

| BGP Tuning |
| ---------- |
| no bgp default ipv4-unicast |
| distance bgp 20 200 200 |
| graceful-restart restart-time 300 |
| graceful-restart |
| maximum-paths 2 ecmp 2 |

### Router BGP Peer Groups

**EVPN-OVERLAY-PEERS**:

| Settings | Value |
| -------- | ----- |
| Address Family | evpn |
| remote_as | 65001 |
| source | Loopback0 |
| bfd | True |
| ebgp multihop | 3 |
| send community | true |
| maximum routes | 0 (no limit) |
**Neighbors:**

| Neighbor | Remote AS |
| -------- | ---------
| 192.168.255.1 | *65001  |
| 192.168.255.2 | *65001  |

*Inherited from peer group

**IPv4-UNDERLAY-PEERS**:

| Settings | Value |
| -------- | ----- |
| Address Family | ipv4 |
| remote_as | 65001 |
| send community | true |
| maximum routes | 12000 |
**Neighbors:**

| Neighbor | Remote AS |
| -------- | ---------
| 172.31.255.12 | *65001  |
| 172.31.255.14 | *65001  |

*Inherited from peer group

**MLAG-IPv4-UNDERLAY-PEER**:

| Settings | Value |
| -------- | ----- |
| Address Family | ipv4 |
| remote_as | 65103 |
| next-hop self | True |
| send community | true |
| maximum routes | 12000 |
**Neighbors:**

| Neighbor | Remote AS |
| -------- | ---------
| 10.255.251.7 | *65103  |

*Inherited from peer group

### Router BGP EVPN Address Family

#### Router BGP EVPN MAC-VRFs

**VLAN aware bundles:**

| VLAN Aware Bundle | Route-Distinguisher | Route Target | Redistribute | VLANs |
| ----------------- | ------------------- | ------------ | ------------ | ----- |
| Tenant_A_OPZone | 192.168.255.6:15001 | both 15001:15001 | learned | 110-111 |
| Tenant_B_OPZone | 192.168.255.6:25002 | both 25002:25002 | learned | 210-211 |
| Tenant_C_OPZone | 192.168.255.6:35003 | both 35003:35003 | learned | 310-311 |

#### Router BGP EVPN VRFs

| VRF | Route-Distinguisher | Route Target | Redistribute |
| --- | ------------------- | ------------ | ------------ |
| Tenant_A_OPZone | 192.168.255.6:15001 | import 15001:15001<br> export 15001:15001 | connected |
| Tenant_B_OPZone | 192.168.255.6:25002 | import 25002:25002<br> export 25002:25002 | connected |
| Tenant_C_OPZone | 192.168.255.6:35003 | import 35003:35003<br> export 35003:35003 | connected |

### Router BGP Device Configuration

```eos
router bgp 65103
   router-id 192.168.255.6
   no bgp default ipv4-unicast
   distance bgp 20 200 200
   graceful-restart restart-time 300
   graceful-restart
   maximum-paths 2 ecmp 2
   neighbor EVPN-OVERLAY-PEERS peer group
   neighbor EVPN-OVERLAY-PEERS remote-as 65001
   neighbor EVPN-OVERLAY-PEERS update-source Loopback0
   neighbor EVPN-OVERLAY-PEERS bfd
   neighbor EVPN-OVERLAY-PEERS ebgp-multihop 3
   neighbor EVPN-OVERLAY-PEERS password 7 q+VNViP5i4rVjW1cxFv2wA==
   neighbor EVPN-OVERLAY-PEERS send-community
   neighbor EVPN-OVERLAY-PEERS maximum-routes 0
   neighbor IPv4-UNDERLAY-PEERS peer group
   neighbor IPv4-UNDERLAY-PEERS remote-as 65001
   neighbor IPv4-UNDERLAY-PEERS password 7 AQQvKeimxJu+uGQ/yYvv9w==
   neighbor IPv4-UNDERLAY-PEERS send-community
   neighbor IPv4-UNDERLAY-PEERS maximum-routes 12000
   neighbor MLAG-IPv4-UNDERLAY-PEER peer group
   neighbor MLAG-IPv4-UNDERLAY-PEER remote-as 65103
   neighbor MLAG-IPv4-UNDERLAY-PEER next-hop-self
   neighbor MLAG-IPv4-UNDERLAY-PEER password 7 vnEaG8gMeQf3d3cN6PktXQ==
   neighbor MLAG-IPv4-UNDERLAY-PEER send-community
   neighbor MLAG-IPv4-UNDERLAY-PEER maximum-routes 12000
   neighbor 10.255.251.7 peer group MLAG-IPv4-UNDERLAY-PEER
   neighbor 172.31.255.12 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.31.255.14 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.255.1 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.255.2 peer group EVPN-OVERLAY-PEERS
   redistribute connected route-map RM-CONN-2-BGP
   !
   vlan-aware-bundle Tenant_A_OPZone
      rd 192.168.255.6:15001
      route-target both 15001:15001
      redistribute learned
      vlan 110-111
   !
   vlan-aware-bundle Tenant_B_OPZone
      rd 192.168.255.6:25002
      route-target both 25002:25002
      redistribute learned
      vlan 210-211
   !
   vlan-aware-bundle Tenant_C_OPZone
      rd 192.168.255.6:35003
      route-target both 35003:35003
      redistribute learned
      vlan 310-311
   !
   address-family evpn
      neighbor EVPN-OVERLAY-PEERS activate
      no neighbor IPv4-UNDERLAY-PEERS activate
      no neighbor MLAG-IPv4-UNDERLAY-PEER activate
   !
   address-family ipv4
      no neighbor EVPN-OVERLAY-PEERS activate
      neighbor IPv4-UNDERLAY-PEERS activate
      neighbor MLAG-IPv4-UNDERLAY-PEER activate
   !
   vrf Tenant_A_OPZone
      rd 192.168.255.6:15001
      route-target import evpn 15001:15001
      route-target export evpn 15001:15001
      neighbor 10.255.251.7 peer group MLAG-IPv4-UNDERLAY-PEER
      redistribute connected
   !
   vrf Tenant_B_OPZone
      rd 192.168.255.6:25002
      route-target import evpn 25002:25002
      route-target export evpn 25002:25002
      neighbor 10.255.251.7 peer group MLAG-IPv4-UNDERLAY-PEER
      redistribute connected
   !
   vrf Tenant_C_OPZone
      rd 192.168.255.6:35003
      route-target import evpn 35003:35003
      route-target export evpn 35003:35003
      neighbor 10.255.251.7 peer group MLAG-IPv4-UNDERLAY-PEER
      redistribute connected
!
```
