# vlan-interfaces

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [Interfaces](#interfaces)
  - [VLAN Interfaces](#vlan-interfaces)
- [BFD](#bfd)
  - [BFD Interfaces](#bfd-interfaces)
- [Multicast](#multicast)
  - [PIM Sparse Mode](#pim-sparse-mode)

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

## Interfaces

### VLAN Interfaces

#### VLAN Interfaces Summary

| Interface | Description | VRF |  MTU | Shutdown |
| --------- | ----------- | --- | ---- | -------- |
| Vlan24 | SVI Description | default | - | False |
| Vlan25 | SVI Description | default | - | False |
| Vlan41 | SVI Description | default | - | False |
| Vlan42 | SVI Description | default | - | False |
| Vlan43 | SVI Description | default | - | False |
| Vlan44 | SVI Description | default | - | False |
| Vlan50 | IP NAT Testing | default | - | - |
| Vlan75 | SVI Description | default | - | False |
| Vlan81 | IPv6 Virtual Address | Tenant_C | - | - |
| Vlan83 | SVI Description | default | - | False |
| Vlan84 | SVI Description | default | - | - |
| Vlan85 | SVI Description | default | - | - |
| Vlan86 | SVI Description | default | - | - |
| Vlan87 | SVI Description | default | - | True |
| Vlan88 | SVI Description | default | - | True |
| Vlan89 | SVI Description | default | - | False |
| Vlan90 | SVI Description | default | - | - |
| Vlan91 | PBR Description | default | - | True |
| Vlan92 | SVI Description | default | - | - |
| Vlan110 | PVLAN Primary with vlan mapping | Tenant_A | - | False |
| Vlan333 | Multiple VRIDs and tracking | default | - | False |
| Vlan501 | SVI Description | default | - | False |
| Vlan667 | Multiple VRIDs | default | - | False |
| Vlan1001 | SVI Description | Tenant_A | - | False |
| Vlan1002 | SVI Description | Tenant_A | - | False |
| Vlan2001 | SVI Description | Tenant_B | - | - |
| Vlan2002 | SVI Description | Tenant_B | - | - |
| Vlan4094 | SVI Description | default | 9214 | - |

##### Private VLAN

| Interface | PVLAN Mapping |
| --------- | ------------- |
| Vlan110 | 111-112 |

##### IPv4

| Interface | VRF | IP Address | IP Address Virtual | IP Router Virtual Address | VRRP | ACL In | ACL Out |
| --------- | --- | ---------- | ------------------ | ------------------------- | ---- | ------ | ------- |
| Vlan24 |  default  |  -  |  10.10.24.1/24  |  -  |  -  |  -  |  -  |
| Vlan25 |  default  |  -  |  -  |  -  |  -  |  -  |  -  |
| Vlan41 |  default  |  -  |  10.10.41.1/24  |  -  |  -  |  -  |  -  |
| Vlan42 |  default  |  -  |  10.10.42.1/24  |  -  |  -  |  -  |  -  |
| Vlan43 |  default  |  -  |  -  |  -  |  -  |  -  |  -  |
| Vlan44 |  default  |  -  |  -  |  -  |  -  |  -  |  -  |
| Vlan50 |  default  |  -  |  -  |  -  |  -  |  -  |  -  |
| Vlan75 |  default  |  -  |  10.10.75.1/24  |  -  |  -  |  -  |  -  |
| Vlan81 |  Tenant_C  |  -  |  10.10.81.1/24  |  -  |  -  |  -  |  -  |
| Vlan83 |  default  |  -  |  10.10.83.1/24  |  -  |  -  |  -  |  -  |
| Vlan84 |  default  |  10.10.84.1/24  |  -  |  10.10.84.254, 10.11.84.254/24  |  -  |  -  |  -  |
| Vlan85 |  default  |  10.10.84.1/24  |  -  |  -  |  -  |  -  |  -  |
| Vlan86 |  default  |  10.10.83.1/24  |  -  |  -  |  -  |  -  |  -  |
| Vlan87 |  default  |  10.10.87.1/24  |  -  |  -  |  -  |  ACL_IN  |  ACL_OUT  |
| Vlan88 |  default  |  -  |  10.10.87.1/23  |  -  |  -  |  -  |  -  |
| Vlan89 |  default  |  -  |  10.10.144.3/20  |  -  |  -  |  -  |  -  |
| Vlan90 |  default  |  10.10.83.1/24  |  -  |  -  |  -  |  -  |  -  |
| Vlan91 |  default  |  -  |  -  |  -  |  -  |  -  |  -  |
| Vlan92 |  default  |  10.10.92.1/24  |  -  |  -  |  -  |  -  |  -  |
| Vlan110 |  Tenant_A  |  10.0.101.1/24  |  -  |  -  |  -  |  -  |  -  |
| Vlan333 |  default  |  192.0.2.2/25  |  -  |  -  |  -  |  -  |  -  |
| Vlan501 |  default  |  10.50.26.29/27  |  -  |  -  |  -  |  -  |  -  |
| Vlan667 |  default  |  192.0.2.2/25  |  -  |  -  |  -  |  -  |  -  |
| Vlan1001 |  Tenant_A  |  -  |  10.1.1.1/24  |  -  |  -  |  -  |  -  |
| Vlan1002 |  Tenant_A  |  -  |  10.1.2.1/24  |  -  |  -  |  -  |  -  |
| Vlan2001 |  Tenant_B  |  -  |  10.2.1.1/24  |  -  |  -  |  -  |  -  |
| Vlan2002 |  Tenant_B  |  -  |  10.2.2.1/24  |  -  |  -  |  -  |  -  |
| Vlan4094 |  default  |  169.254.252.0/31  |  -  |  -  |  -  |  -  |  -  |

##### IP NAT: Source Static

| Interface | Direction | Original IP | Original Port | Access List | Translated IP | Translated Port | Protocol | Group | Priority | Comment |
| --------- | --------- | ----------- | ------------- | ----------- | ------------- | --------------- | -------- | ----- | -------- | ------- |
| Vlan50 | - | 3.0.0.1 | - | - | 4.0.0.1 | - | - | - | 0 | - |

##### IP NAT: Source Dynamic

| Interface | Access List | NAT Type | Pool Name | Priority | Comment |
| --------- | ----------- | -------- | --------- | -------- | ------- |
| Vlan50 | ACL2 | pool | POOL2 | 0 | - |

##### IP NAT: Destination Static

| Interface | Direction | Original IP | Original Port | Access List | Translated IP | Translated Port | Protocol | Group | Priority | Comment |
| --------- | --------- | ----------- | ------------- | ----------- | ------------- | --------------- | -------- | ----- | -------- | ------- |
| Vlan50 | - | 1.0.0.1 | - | - | 2.0.0.1 | - | - | - | 0 | - |

##### IP NAT: Destination Dynamic

| Interface | Access List | Pool Name | Priority | Comment |
| --------- | ----------- | --------- | -------- | ------- |
| Vlan50 | ACL1 | POOL1 | 0 | - |

##### IPv6

| Interface | VRF | IPv6 Address | IPv6 Virtual Addresses | Virtual Router Address | VRRP | ND RA Disabled | Managed Config Flag | IPv6 ACL In | IPv6 ACL Out |
| --------- | --- | ------------ | ---------------------- | ---------------------- | ---- | -------------- | ------------------- | ----------- | ------------ |
| Vlan24 | default | 1b11:3a00:22b0:6::15/64 | - | 1b11:3a00:22b0:6::1 | - | - | True | - | - |
| Vlan25 | default | 1b11:3a00:22b0:16::16/64 | - | 1b11:3a00:22b0:16::15, 1b11:3a00:22b0:16::14 | - | - | - | - | - |
| Vlan43 | default | a0::1/64 | - | - | - | - | - | - | - |
| Vlan44 | default | a0::4/64 | - | - | - | - | - | - | - |
| Vlan75 | default | 1b11:3a00:22b0:1000::15/64 | - | 1b11:3a00:22b0:1000::1 | - | - | True | - | - |
| Vlan81 | Tenant_C | - | fc00:10:10:81::1/64, fc00:10:11:81::1/64, fc00:10:12:81::1/64 | - | - | - | - | - | - |
| Vlan89 | default | 1b11:3a00:22b0:5200::15/64 | - | 1b11:3a00:22b0:5200::3 | - | - | True | - | - |
| Vlan333 | default | 2001:db8::2/64 | - | - | - | - | - | - | - |
| Vlan501 | default | 1b11:3a00:22b0:0088::207/127 | - | - | - | True | - | - | - |
| Vlan667 | default | 2001:db8::2/64 | - | - | - | - | - | - | - |
| Vlan1001 | Tenant_A | a1::1/64 | - | - | - | - | True | - | - |
| Vlan1002 | Tenant_A | a2::1/64 | - | - | - | True | True | - | - |

##### VRRP Details

| Interface | VRRP-ID | Priority | Advertisement Interval | Preempt | Tracked Object Name(s) | Tracked Object Action(s) | IPv4 Virtual IP | IPv4 VRRP Version | IPv6 Virtual IP |
| --------- | ------- | -------- | ---------------------- | --------| ---------------------- | ------------------------ | --------------- | ----------------- | --------------- |
| Vlan333 | 1 | 105 | 2 | Enabled | ID1-TrackedObjectDecrement, ID1-TrackedObjectShutdown | Decrement 5, Shutdown | 192.0.2.1 | 2 | - |
| Vlan333 | 2 | - | - | Enabled | ID2-TrackedObjectDecrement, ID2-TrackedObjectShutdown | Decrement 10, Shutdown | - | 2 | 2001:db8::1 |
| Vlan333 | 3 | - | - | Disabled | - | - | 100.64.0.1 | 3 | - |
| Vlan667 | 1 | 105 | 2 | Enabled | - | - | 192.0.2.1 | 2 | - |
| Vlan667 | 2 | - | - | Enabled | - | - | - | 2 | 2001:db8::1 |

##### ISIS

| Interface | ISIS Instance | ISIS Metric | Mode |
| --------- | ------------- | ----------- | ---- |
| Vlan2002 | EVPN_UNDERLAY | - | - |

##### Multicast Routing

| Interface | IP Version | Static Routes Allowed | Multicast Boundaries | Export Host Routes For Multicast Sources |
| --------- | ---------- | --------------------- | -------------------- | ---------------------------------------- |
| Vlan75 | IPv4 | True | 224.0.1.0/24, 224.0.2.0/24 | - |
| Vlan75 | IPv6 | - | ff00::/16, ff01::/16 | - |
| Vlan89 | IPv4 | - | ACL_MULTICAST | True |
| Vlan89 | IPv6 | True | ACL_V6_MULTICAST_WITH_OUT | - |
| Vlan110 | IPv4 | True | ACL_MULTICAST | - |
| Vlan110 | IPv6 | - | - | True |

#### VLAN Interfaces Device Configuration

```eos
!
interface Vlan24
   description SVI Description
   no shutdown
   ipv6 address 1b11:3a00:22b0:6::15/64
   ipv6 nd managed-config-flag
   ipv6 nd prefix 1b11:3a00:22b0:6::/64 infinite infinite no-autoconfig
   ipv6 virtual-router address 1b11:3a00:22b0:6::1
   ip address virtual 10.10.24.1/24
!
interface Vlan25
   description SVI Description
   no shutdown
   ipv6 address 1b11:3a00:22b0:16::16/64
   ipv6 virtual-router address 1b11:3a00:22b0:16::15
   ipv6 virtual-router address 1b11:3a00:22b0:16::14
!
interface Vlan41
   description SVI Description
   no shutdown
   ip helper-address 10.10.64.150 source-interface Loopback0
   ip helper-address 10.10.96.150 source-interface Loopback0
   ip helper-address 10.10.96.151 source-interface Loopback0
   ip address virtual 10.10.41.1/24
!
interface Vlan42
   description SVI Description
   no shutdown
   ip helper-address 10.10.64.150 source-interface Loopback0
   ip helper-address 10.10.96.150 source-interface Loopback0
   ip helper-address 10.10.96.151 source-interface Loopback0
   ip address virtual 10.10.42.1/24
!
interface Vlan43
   description SVI Description
   no shutdown
   ipv6 dhcp relay destination a0::2 vrf TEST local-interface Loopback44 link-address a0::4
   ipv6 address a0::1/64
!
interface Vlan44
   description SVI Description
   no shutdown
   ipv6 dhcp relay destination a0::5 vrf TEST source-address a0::6 link-address a0::7
   ipv6 dhcp relay destination a0::8
   ipv6 address a0::4/64
!
interface Vlan50
   description IP NAT Testing
   ip nat source static 3.0.0.1 4.0.0.1
   ip nat source dynamic access-list ACL2 pool POOL2
   ip nat destination static 1.0.0.1 2.0.0.1
   ip nat destination dynamic access-list ACL1 pool POOL1
!
interface Vlan75
   description SVI Description
   no shutdown
   ipv6 address 1b11:3a00:22b0:1000::15/64
   ipv6 nd managed-config-flag
   ipv6 nd prefix 1b11:3a00:22b0:1000::/64 infinite infinite no-autoconfig
   multicast ipv4 boundary 224.0.1.0/24 out
   multicast ipv4 boundary 224.0.2.0/24
   multicast ipv6 boundary ff00::/16 out
   multicast ipv6 boundary ff01::/16 out
   multicast ipv4 static
   ipv6 virtual-router address 1b11:3a00:22b0:1000::1
   ip address virtual 10.10.75.1/24
!
interface Vlan81
   description IPv6 Virtual Address
   vrf Tenant_C
   ipv6 enable
   ipv6 address virtual fc00:10:10:81::1/64
   ipv6 address virtual fc00:10:11:81::1/64
   ipv6 address virtual fc00:10:12:81::1/64
   ip address virtual 10.10.81.1/24
!
interface Vlan83
   description SVI Description
   no shutdown
   ip address virtual 10.10.83.1/24
   ip address virtual 10.11.83.1/24 secondary
   ip address virtual 10.11.84.1/24 secondary
!
interface Vlan84
   description SVI Description
   arp gratuitous accept
   arp monitor mac-address
   ip address 10.10.84.1/24
   ip virtual-router address 10.10.84.254
   ip virtual-router address 10.11.84.254/24
!
interface Vlan85
   description SVI Description
   arp cache dynamic capacity 50000
   ip address 10.10.84.1/24
   bfd interval 500 min-rx 500 multiplier 5
   bfd echo
!
interface Vlan86
   description SVI Description
   ip address 10.10.83.1/24
   ip attached-host route export 10
!
interface Vlan87
   description SVI Description
   shutdown
   ip address 10.10.87.1/24
   ip access-group ACL_IN in
   ip access-group ACL_OUT out
!
interface Vlan88
   description SVI Description
   shutdown
   ip address virtual 10.10.87.1/23
!
interface Vlan89
   description SVI Description
   no shutdown
   ip helper-address 10.10.64.150 source-interface Loopback0
   ip helper-address 10.10.96.101 source-interface Loopback0
   ip helper-address 10.10.96.150 source-interface Loopback0
   ip helper-address 10.10.96.151 source-interface Loopback0
   ip igmp
   ip igmp version 2
   ipv6 address 1b11:3a00:22b0:5200::15/64
   ipv6 nd managed-config-flag
   ipv6 nd prefix 1b11:3a00:22b0:5200::/64 infinite infinite no-autoconfig
   multicast ipv4 boundary ACL_MULTICAST
   multicast ipv6 boundary ACL_V6_MULTICAST_WITH_OUT out
   multicast ipv4 source route export
   multicast ipv6 static
   pim ipv4 sparse-mode
   pim ipv4 local-interface Loopback0
   ipv6 virtual-router address 1b11:3a00:22b0:5200::3
   ip address virtual 10.10.144.3/20
!
interface Vlan90
   description SVI Description
   ip address 10.10.83.1/24
   ip attached-host route export
!
interface Vlan91
   description PBR Description
   shutdown
   service-policy type pbr input MyServicePolicy
!
interface Vlan92
   description SVI Description
   ip proxy-arp
   ip directed-broadcast
   ip address 10.10.92.1/24
!
interface Vlan110
   description PVLAN Primary with vlan mapping
   no shutdown
   vrf Tenant_A
   ip address 10.0.101.1/24
   multicast ipv4 boundary ACL_MULTICAST out
   multicast ipv6 source route export 20
   multicast ipv4 static
   pvlan mapping 111-112
!
interface Vlan333
   description Multiple VRIDs and tracking
   no shutdown
   arp aging timeout 180
   ip address 192.0.2.2/25
   ipv6 enable
   ipv6 address 2001:db8::2/64
   ipv6 address fe80::2/64 link-local
   vrrp 1 priority-level 105
   vrrp 1 advertisement interval 2
   vrrp 1 preempt delay minimum 30 reload 800
   vrrp 1 ipv4 192.0.2.1
   vrrp 1 tracked-object ID1-TrackedObjectDecrement decrement 5
   vrrp 1 tracked-object ID1-TrackedObjectShutdown shutdown
   vrrp 2 ipv6 2001:db8::1
   vrrp 2 tracked-object ID2-TrackedObjectDecrement decrement 10
   vrrp 2 tracked-object ID2-TrackedObjectShutdown shutdown
   no vrrp 3 preempt
   vrrp 3 timers delay reload 900
   vrrp 3 ipv4 100.64.0.1
   vrrp 3 ipv4 version 3
!
interface Vlan501
   description SVI Description
   no shutdown
   ip address 10.50.26.29/27
   ipv6 address 1b11:3a00:22b0:0088::207/127
   ipv6 nd ra disabled
!
interface Vlan667
   description Multiple VRIDs
   no shutdown
   arp aging timeout 180
   ip address 192.0.2.2/25
   ipv6 enable
   ipv6 address 2001:db8::2/64
   ipv6 address fe80::2/64 link-local
   vrrp 1 priority-level 105
   vrrp 1 advertisement interval 2
   vrrp 1 preempt delay minimum 30 reload 800
   vrrp 1 ipv4 192.0.2.1
   vrrp 2 ipv6 2001:db8::1
!
interface Vlan1001
   description SVI Description
   no shutdown
   vrf Tenant_A
   ipv6 address a1::1/64
   ipv6 nd managed-config-flag
   ipv6 nd prefix a1::/64 infinite infinite no-autoconfig
   ip address virtual 10.1.1.1/24
!
interface Vlan1002
   description SVI Description
   no shutdown
   vrf Tenant_A
   ipv6 address a2::1/64
   ipv6 nd ra disabled
   ipv6 nd managed-config-flag
   ipv6 nd prefix a2::/64 infinite infinite no-autoconfig
   ip address virtual 10.1.2.1/24
!
interface Vlan2001
   description SVI Description
   vrf Tenant_B
   ip address virtual 10.2.1.1/24
   comment
   Comment created from eos_cli under vlan_interfaces.Vlan2001
   EOF

!
interface Vlan2002
   description SVI Description
   no autostate
   vrf Tenant_B
   isis enable EVPN_UNDERLAY
   ip address virtual 10.2.2.1/24
!
interface Vlan4094
   description SVI Description
   mtu 9214
   ip address 169.254.252.0/31
   ipv6 address fe80::a/64 link-local
   pim ipv4 sparse-mode
   pim ipv4 dr-priority 200
```

## BFD

### BFD Interfaces

| Interface | Interval | Minimum RX | Multiplier | Echo |
| --------- | -------- | ---------- | ---------- | ---- |
| Vlan85 | 500 | 500 | 5 | True |

## Multicast

### PIM Sparse Mode

#### PIM Sparse Mode Enabled Interfaces

| Interface Name | VRF Name | IP Version | DR Priority | Local Interface |
| -------------- | -------- | ---------- | ----------- | --------------- |
| Vlan89 | - | IPv4 | - | Loopback0 |
| Vlan4094 | - | IPv4 | 200 | - |
