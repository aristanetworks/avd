# DC1_FABRIC

## Table of Contents

- [Fabric Switches and Management IP](#fabric-switches-and-management-ip)
  - [Fabric Switches with inband Management IP](#fabric-switches-with-inband-management-ip)
- [Fabric Topology](#fabric-topology)
- [Fabric IP Allocation](#fabric-ip-allocation)
  - [Fabric Point-To-Point Links](#fabric-point-to-point-links)
  - [Point-To-Point Links Node Allocation](#point-to-point-links-node-allocation)
  - [Loopback Interfaces (BGP EVPN Peering)](#loopback-interfaces-bgp-evpn-peering)
  - [Loopback0 Interfaces Node Allocation](#loopback0-interfaces-node-allocation)
  - [VRF Summary](#vrf-summary)
  - [BGP Peer Groups](#bgp-peer-groups)
  - [BGP Neighbors](#bgp-neighbors)
  - [VRF Routing Protocols](#vrf-routing-protocols)
  - [VTEP Loopback VXLAN Tunnel Source Interfaces (VTEPs Only)](#vtep-loopback-vxlan-tunnel-source-interfaces-vteps-only)
  - [VTEP Loopback Node allocation](#vtep-loopback-node-allocation)

## Fabric Switches and Management IP

| POD | Type | Node | Management IP | Platform | Provisioned in CloudVision | Serial Number |
| --- | ---- | ---- | ------------- | -------- | -------------------------- | ------------- |
| DC1_FABRIC | l3leaf | DC1-BL1A | 192.168.200.110/24 | 7280R | Provisioned | - |
| DC1_FABRIC | l3leaf | DC1-BL1B | 192.168.200.111/24 | 7280R | Provisioned | - |
| DC1_FABRIC | l2leaf | DC1-L2LEAF1A | 192.168.200.112/24 | vEOS-LAB | Provisioned | - |
| DC1_FABRIC | l2leaf | DC1-L2LEAF1B | 192.168.200.115/24 | vEOS-LAB | Provisioned | - |
| DC1_FABRIC | l2leaf | DC1-L2LEAF2A | 192.168.200.113/24 | vEOS-LAB | Provisioned | - |
| DC1_FABRIC | l2leaf | DC1-L2LEAF2B | 192.168.200.114/24 | vEOS-LAB | Provisioned | - |
| DC1_FABRIC | l2leaf | DC1-L2LEAF3A | 192.168.200.116/24 | vEOS-LAB | Provisioned | - |
| DC1_FABRIC | l3leaf | DC1-LEAF1A | 192.168.200.105/24 | 7050SX3 | Provisioned | - |
| DC1_FABRIC | l3leaf | DC1-LEAF2A | 192.168.200.106/24 | 7280R | Provisioned | - |
| DC1_FABRIC | l3leaf | DC1-LEAF2B | 192.168.200.107/24 | 7280R | Provisioned | - |
| DC1_FABRIC | spine | DC1-SPINE1 | 192.168.200.101/24 | 7050SX3 | Provisioned | - |
| DC1_FABRIC | spine | DC1-SPINE2 | 192.168.200.102/24 | 7050SX3 | Provisioned | - |
| DC1_FABRIC | spine | DC1-SPINE3 | 192.168.200.103/24 | 7050SX3 | Provisioned | - |
| DC1_FABRIC | spine | DC1-SPINE4 | 192.168.200.104/24 | 7050SX3 | Provisioned | - |
| DC1_FABRIC | l3leaf | DC1-SVC3A | 192.168.200.108/24 | 7050SX3 | Provisioned | - |
| DC1_FABRIC | l3leaf | DC1-SVC3B | 192.168.200.109/24 | 7050SX3 | Provisioned | - |

> Provision status is based on Ansible inventory declaration and do not represent real status from CloudVision.

### Fabric Switches with inband Management IP

| POD | Type | Node | Management IP | Inband Interface |
| --- | ---- | ---- | ------------- | ---------------- |

## Fabric Topology

| Type | Node | Node Interface | Peer Type | Peer Node | Peer Interface |
| ---- | ---- | -------------- | --------- | --------- | -------------- |
| l3leaf | DC1-BL1A | Ethernet41 | spine | DC1-SPINE1 | Ethernet6 |
| l3leaf | DC1-BL1A | Ethernet42 | spine | DC1-SPINE2 | Ethernet6 |
| l3leaf | DC1-BL1A | Ethernet43 | spine | DC1-SPINE3 | Ethernet6 |
| l3leaf | DC1-BL1A | Ethernet44 | spine | DC1-SPINE4 | Ethernet6 |
| l3leaf | DC1-BL1B | Ethernet45 | spine | DC1-SPINE1 | Ethernet7 |
| l3leaf | DC1-BL1B | Ethernet46 | spine | DC1-SPINE2 | Ethernet7 |
| l3leaf | DC1-BL1B | Ethernet47 | spine | DC1-SPINE3 | Ethernet7 |
| l3leaf | DC1-BL1B | Ethernet48 | spine | DC1-SPINE4 | Ethernet7 |
| l2leaf | DC1-L2LEAF1A | Ethernet1 | l3leaf | DC1-LEAF2A | Ethernet7 |
| l2leaf | DC1-L2LEAF1A | Ethernet2 | l3leaf | DC1-LEAF2B | Ethernet7 |
| l2leaf | DC1-L2LEAF1A | Ethernet3 | mlag_peer | DC1-L2LEAF1B | Ethernet3 |
| l2leaf | DC1-L2LEAF1A | Ethernet4 | mlag_peer | DC1-L2LEAF1B | Ethernet4 |
| l2leaf | DC1-L2LEAF1B | Ethernet1 | l3leaf | DC1-LEAF2A | Ethernet8 |
| l2leaf | DC1-L2LEAF1B | Ethernet2 | l3leaf | DC1-LEAF2B | Ethernet8 |
| l2leaf | DC1-L2LEAF2A | Ethernet1 | l3leaf | DC1-SVC3A | Ethernet7 |
| l2leaf | DC1-L2LEAF2A | Ethernet2 | l3leaf | DC1-SVC3B | Ethernet7 |
| l2leaf | DC1-L2LEAF2A | Ethernet3 | mlag_peer | DC1-L2LEAF2B | Ethernet3 |
| l2leaf | DC1-L2LEAF2A | Ethernet4 | mlag_peer | DC1-L2LEAF2B | Ethernet4 |
| l2leaf | DC1-L2LEAF2B | Ethernet1 | l3leaf | DC1-SVC3A | Ethernet8 |
| l2leaf | DC1-L2LEAF2B | Ethernet2 | l3leaf | DC1-SVC3B | Ethernet8 |
| l2leaf | DC1-L2LEAF3A | Ethernet1 | l3leaf | DC1-LEAF2A | Ethernet9 |
| l2leaf | DC1-L2LEAF3A | Ethernet2 | l3leaf | DC1-LEAF2B | Ethernet9 |
| l3leaf | DC1-LEAF1A | Ethernet1 | spine | DC1-SPINE1 | Ethernet1 |
| l3leaf | DC1-LEAF1A | Ethernet2 | spine | DC1-SPINE2 | Ethernet1 |
| l3leaf | DC1-LEAF1A | Ethernet3 | spine | DC1-SPINE3 | Ethernet1 |
| l3leaf | DC1-LEAF1A | Ethernet4 | spine | DC1-SPINE4 | Ethernet1 |
| l3leaf | DC1-LEAF2A | Ethernet1 | spine | DC1-SPINE1 | Ethernet2 |
| l3leaf | DC1-LEAF2A | Ethernet2 | spine | DC1-SPINE2 | Ethernet2 |
| l3leaf | DC1-LEAF2A | Ethernet3 | spine | DC1-SPINE3 | Ethernet2 |
| l3leaf | DC1-LEAF2A | Ethernet4 | spine | DC1-SPINE4 | Ethernet2 |
| l3leaf | DC1-LEAF2B | Ethernet1 | spine | DC1-SPINE1 | Ethernet3 |
| l3leaf | DC1-LEAF2B | Ethernet2 | spine | DC1-SPINE2 | Ethernet3 |
| l3leaf | DC1-LEAF2B | Ethernet3 | spine | DC1-SPINE3 | Ethernet3 |
| l3leaf | DC1-LEAF2B | Ethernet4 | spine | DC1-SPINE4 | Ethernet3 |
| spine | DC1-SPINE1 | Ethernet4 | l3leaf | DC1-SVC3A | Ethernet41 |
| spine | DC1-SPINE1 | Ethernet5 | l3leaf | DC1-SVC3B | Ethernet41 |
| spine | DC1-SPINE2 | Ethernet4 | l3leaf | DC1-SVC3A | Ethernet42 |
| spine | DC1-SPINE2 | Ethernet5 | l3leaf | DC1-SVC3B | Ethernet42 |
| spine | DC1-SPINE3 | Ethernet4 | l3leaf | DC1-SVC3A | Ethernet43 |
| spine | DC1-SPINE3 | Ethernet5 | l3leaf | DC1-SVC3B | Ethernet43 |
| spine | DC1-SPINE4 | Ethernet4 | l3leaf | DC1-SVC3A | Ethernet44 |
| spine | DC1-SPINE4 | Ethernet5 | l3leaf | DC1-SVC3B | Ethernet44 |
| l3leaf | DC1-SVC3A | Ethernet5 | mlag_peer | DC1-SVC3B | Ethernet5 |
| l3leaf | DC1-SVC3A | Ethernet6 | mlag_peer | DC1-SVC3B | Ethernet6 |

## Fabric IP Allocation

### Fabric Point-To-Point Links

| Uplink IPv4 Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ---------------- | ------------------- | ------------------ | ------------------ |
| 172.31.255.0/24 | 256 | 56 | 21.88 % |

### Point-To-Point Links Node Allocation

| Node | Node Interface | Node IP Address | Peer Node | Peer Interface | Peer IP Address |
| ---- | -------------- | --------------- | --------- | -------------- | --------------- |
| DC1-BL1A | Ethernet41 | 172.31.255.81/31 | DC1-SPINE1 | Ethernet6 | 172.31.255.80/31 |
| DC1-BL1A | Ethernet42 | 172.31.255.83/31 | DC1-SPINE2 | Ethernet6 | 172.31.255.82/31 |
| DC1-BL1A | Ethernet43 | 172.31.255.85/31 | DC1-SPINE3 | Ethernet6 | 172.31.255.84/31 |
| DC1-BL1A | Ethernet44 | 172.31.255.87/31 | DC1-SPINE4 | Ethernet6 | 172.31.255.86/31 |
| DC1-BL1B | Ethernet45 | 172.31.255.97/31 | DC1-SPINE1 | Ethernet7 | 172.31.255.96/31 |
| DC1-BL1B | Ethernet46 | 172.31.255.99/31 | DC1-SPINE2 | Ethernet7 | 172.31.255.98/31 |
| DC1-BL1B | Ethernet47 | 172.31.255.101/31 | DC1-SPINE3 | Ethernet7 | 172.31.255.100/31 |
| DC1-BL1B | Ethernet48 | 172.31.255.103/31 | DC1-SPINE4 | Ethernet7 | 172.31.255.102/31 |
| DC1-LEAF1A | Ethernet1 | 172.31.255.1/31 | DC1-SPINE1 | Ethernet1 | 172.31.255.0/31 |
| DC1-LEAF1A | Ethernet2 | 172.31.255.3/31 | DC1-SPINE2 | Ethernet1 | 172.31.255.2/31 |
| DC1-LEAF1A | Ethernet3 | 172.31.255.5/31 | DC1-SPINE3 | Ethernet1 | 172.31.255.4/31 |
| DC1-LEAF1A | Ethernet4 | 172.31.255.7/31 | DC1-SPINE4 | Ethernet1 | 172.31.255.6/31 |
| DC1-LEAF2A | Ethernet1 | 172.31.255.17/31 | DC1-SPINE1 | Ethernet2 | 172.31.255.16/31 |
| DC1-LEAF2A | Ethernet2 | 172.31.255.19/31 | DC1-SPINE2 | Ethernet2 | 172.31.255.18/31 |
| DC1-LEAF2A | Ethernet3 | 172.31.255.21/31 | DC1-SPINE3 | Ethernet2 | 172.31.255.20/31 |
| DC1-LEAF2A | Ethernet4 | 172.31.255.23/31 | DC1-SPINE4 | Ethernet2 | 172.31.255.22/31 |
| DC1-LEAF2B | Ethernet1 | 172.31.255.33/31 | DC1-SPINE1 | Ethernet3 | 172.31.255.32/31 |
| DC1-LEAF2B | Ethernet2 | 172.31.255.35/31 | DC1-SPINE2 | Ethernet3 | 172.31.255.34/31 |
| DC1-LEAF2B | Ethernet3 | 172.31.255.37/31 | DC1-SPINE3 | Ethernet3 | 172.31.255.36/31 |
| DC1-LEAF2B | Ethernet4 | 172.31.255.39/31 | DC1-SPINE4 | Ethernet3 | 172.31.255.38/31 |
| DC1-SPINE1 | Ethernet4 | 172.31.255.48/31 | DC1-SVC3A | Ethernet41 | 172.31.255.49/31 |
| DC1-SPINE1 | Ethernet5 | 172.31.255.64/31 | DC1-SVC3B | Ethernet41 | 172.31.255.65/31 |
| DC1-SPINE2 | Ethernet4 | 172.31.255.50/31 | DC1-SVC3A | Ethernet42 | 172.31.255.51/31 |
| DC1-SPINE2 | Ethernet5 | 172.31.255.66/31 | DC1-SVC3B | Ethernet42 | 172.31.255.67/31 |
| DC1-SPINE3 | Ethernet4 | 172.31.255.52/31 | DC1-SVC3A | Ethernet43 | 172.31.255.53/31 |
| DC1-SPINE3 | Ethernet5 | 172.31.255.68/31 | DC1-SVC3B | Ethernet43 | 172.31.255.69/31 |
| DC1-SPINE4 | Ethernet4 | 172.31.255.54/31 | DC1-SVC3A | Ethernet44 | 172.31.255.55/31 |
| DC1-SPINE4 | Ethernet5 | 172.31.255.70/31 | DC1-SVC3B | Ethernet44 | 172.31.255.71/31 |

### Loopback Interfaces (BGP EVPN Peering)

| Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ------------- | ------------------- | ------------------ | ------------------ |
| 192.168.255.0/24 | 256 | 11 | 4.3 % |

### Loopback0 Interfaces Node Allocation

| POD | Node | Loopback0 |
| --- | ---- | --------- |
| DC1_FABRIC | DC1-BL1A | 192.168.255.14/32 |
| DC1_FABRIC | DC1-BL1B | 192.168.255.15/32 |
| DC1_FABRIC | DC1-LEAF1A | 192.168.255.9/32 |
| DC1_FABRIC | DC1-LEAF2A | 192.168.255.10/32 |
| DC1_FABRIC | DC1-LEAF2B | 192.168.255.11/32 |
| DC1_FABRIC | DC1-SPINE1 | 192.168.255.1/32 |
| DC1_FABRIC | DC1-SPINE2 | 192.168.255.2/32 |
| DC1_FABRIC | DC1-SPINE3 | 192.168.255.3/32 |
| DC1_FABRIC | DC1-SPINE4 | 192.168.255.4/32 |
| DC1_FABRIC | DC1-SVC3A | 192.168.255.12/32 |
| DC1_FABRIC | DC1-SVC3B | 192.168.255.13/32 |

### VRF Summary

| VRF | RD Pattern | Import RT | Export RT | Nodes |
| --- | ---------- | --------- | --------- | ----- |
| Tenant_A_APP_Zone | 12 | 12:12 | 12:12 | DC1-LEAF1A, DC1-LEAF2A, DC1-LEAF2B, DC1-SVC3A, DC1-SVC3B |
| Tenant_A_DB_Zone | 13 | 13:13 | 13:13 | DC1-LEAF2A, DC1-LEAF2B, DC1-SVC3A, DC1-SVC3B |
| Tenant_A_OP_Zone | 10 | 10:10 | 10:10 | DC1-LEAF2A, DC1-LEAF2B, DC1-SVC3A, DC1-SVC3B |
| Tenant_A_WAN_Zone | 14 | 14:14, 65000:456 | 14:14, 65000:789 | DC1-BL1A, DC1-BL1B, DC1-SVC3A, DC1-SVC3B |
| Tenant_A_WEB_Zone | 11 | 11:11 | 11:11 | DC1-LEAF1A, DC1-LEAF2A, DC1-LEAF2B, DC1-SVC3A, DC1-SVC3B |
| Tenant_B_OP_Zone | 20 | 20:20 | 20:20 | DC1-BL1A, DC1-BL1B, DC1-LEAF2A, DC1-LEAF2B, DC1-SVC3A, DC1-SVC3B |
| Tenant_B_WAN_Zone | 21 | 21:21 | 21:21 | DC1-BL1A, DC1-BL1B, DC1-SVC3A, DC1-SVC3B |
| Tenant_C_OP_Zone | 30 | 30:30 | 30:30 | DC1-LEAF2A, DC1-LEAF2B, DC1-SVC3A, DC1-SVC3B |
| Tenant_C_WAN_Zone | 31 | 31:31 | 31:31 | DC1-BL1A, DC1-BL1B, DC1-SVC3A, DC1-SVC3B |
| Tenant_L3_VRF_Zone | 15 | 15:15 | 15:15 | DC1-BL1A, DC1-BL1B |

### BGP Peer Groups

| Peer Group | Remote AS | Update Source | BFD | Send Community | Nodes |
| ---------- | --------- | ------------- | --- | -------------- | ----- |
| EVPN-OVERLAY-PEERS | - | Loopback0 | Yes | all | DC1-BL1A, DC1-BL1B, DC1-LEAF1A, DC1-LEAF2A, DC1-LEAF2B, DC1-SPINE1, DC1-SPINE2, DC1-SPINE3, DC1-SPINE4, DC1-SVC3A, DC1-SVC3B |
| MLAG-PEERS | 65103 | - | No | all | DC1-SVC3A, DC1-SVC3B |
| UNDERLAY-PEERS | - | - | No | all | DC1-BL1A, DC1-BL1B, DC1-LEAF1A, DC1-LEAF2A, DC1-LEAF2B, DC1-SPINE1, DC1-SPINE2, DC1-SPINE3, DC1-SPINE4, DC1-SVC3A, DC1-SVC3B |

### BGP Neighbors

| Node | Type | Neighbor IP | Peer Group | Remote AS | Description |
| ---- | ---- | ----------- | ---------- | --------- | ----------- |
| DC1-BL1A | l3leaf | 172.31.255.80 | UNDERLAY-PEERS | 65001 | DC1-SPINE1_Ethernet6 |
| DC1-BL1A | l3leaf | 172.31.255.82 | UNDERLAY-PEERS | 65001 | DC1-SPINE2_Ethernet6 |
| DC1-BL1A | l3leaf | 172.31.255.84 | UNDERLAY-PEERS | 65001 | DC1-SPINE3_Ethernet6 |
| DC1-BL1A | l3leaf | 172.31.255.86 | UNDERLAY-PEERS | 65001 | DC1-SPINE4_Ethernet6 |
| DC1-BL1A | l3leaf | 192.168.255.1 | EVPN-OVERLAY-PEERS | 65001 | DC1-SPINE1_Loopback0 |
| DC1-BL1A | l3leaf | 192.168.255.2 | EVPN-OVERLAY-PEERS | 65001 | DC1-SPINE2_Loopback0 |
| DC1-BL1A | l3leaf | 192.168.255.3 | EVPN-OVERLAY-PEERS | 65001 | DC1-SPINE3_Loopback0 |
| DC1-BL1A | l3leaf | 192.168.255.4 | EVPN-OVERLAY-PEERS | 65001 | DC1-SPINE4_Loopback0 |
| DC1-BL1B | l3leaf | 172.31.255.96 | UNDERLAY-PEERS | 65001 | DC1-SPINE1_Ethernet7 |
| DC1-BL1B | l3leaf | 172.31.255.98 | UNDERLAY-PEERS | 65001 | DC1-SPINE2_Ethernet7 |
| DC1-BL1B | l3leaf | 172.31.255.100 | UNDERLAY-PEERS | 65001 | DC1-SPINE3_Ethernet7 |
| DC1-BL1B | l3leaf | 172.31.255.102 | UNDERLAY-PEERS | 65001 | DC1-SPINE4_Ethernet7 |
| DC1-BL1B | l3leaf | 192.168.255.1 | EVPN-OVERLAY-PEERS | 65001 | DC1-SPINE1_Loopback0 |
| DC1-BL1B | l3leaf | 192.168.255.2 | EVPN-OVERLAY-PEERS | 65001 | DC1-SPINE2_Loopback0 |
| DC1-BL1B | l3leaf | 192.168.255.3 | EVPN-OVERLAY-PEERS | 65001 | DC1-SPINE3_Loopback0 |
| DC1-BL1B | l3leaf | 192.168.255.4 | EVPN-OVERLAY-PEERS | 65001 | DC1-SPINE4_Loopback0 |
| DC1-LEAF1A | l3leaf | 172.31.255.0 | UNDERLAY-PEERS | 65001 | DC1-SPINE1_Ethernet1 |
| DC1-LEAF1A | l3leaf | 172.31.255.2 | UNDERLAY-PEERS | 65001 | DC1-SPINE2_Ethernet1 |
| DC1-LEAF1A | l3leaf | 172.31.255.4 | UNDERLAY-PEERS | 65001 | DC1-SPINE3_Ethernet1 |
| DC1-LEAF1A | l3leaf | 172.31.255.6 | UNDERLAY-PEERS | 65001 | DC1-SPINE4_Ethernet1 |
| DC1-LEAF1A | l3leaf | 192.168.255.1 | EVPN-OVERLAY-PEERS | 65001 | DC1-SPINE1_Loopback0 |
| DC1-LEAF1A | l3leaf | 192.168.255.2 | EVPN-OVERLAY-PEERS | 65001 | DC1-SPINE2_Loopback0 |
| DC1-LEAF1A | l3leaf | 192.168.255.3 | EVPN-OVERLAY-PEERS | 65001 | DC1-SPINE3_Loopback0 |
| DC1-LEAF1A | l3leaf | 192.168.255.4 | EVPN-OVERLAY-PEERS | 65001 | DC1-SPINE4_Loopback0 |
| DC1-LEAF2A | l3leaf | 172.31.255.16 | UNDERLAY-PEERS | 65001 | DC1-SPINE1_Ethernet2 |
| DC1-LEAF2A | l3leaf | 172.31.255.18 | UNDERLAY-PEERS | 65001 | DC1-SPINE2_Ethernet2 |
| DC1-LEAF2A | l3leaf | 172.31.255.20 | UNDERLAY-PEERS | 65001 | DC1-SPINE3_Ethernet2 |
| DC1-LEAF2A | l3leaf | 172.31.255.22 | UNDERLAY-PEERS | 65001 | DC1-SPINE4_Ethernet2 |
| DC1-LEAF2A | l3leaf | 192.168.255.1 | EVPN-OVERLAY-PEERS | 65001 | DC1-SPINE1_Loopback0 |
| DC1-LEAF2A | l3leaf | 192.168.255.2 | EVPN-OVERLAY-PEERS | 65001 | DC1-SPINE2_Loopback0 |
| DC1-LEAF2A | l3leaf | 192.168.255.3 | EVPN-OVERLAY-PEERS | 65001 | DC1-SPINE3_Loopback0 |
| DC1-LEAF2A | l3leaf | 192.168.255.4 | EVPN-OVERLAY-PEERS | 65001 | DC1-SPINE4_Loopback0 |
| DC1-LEAF2B | l3leaf | 172.31.255.32 | UNDERLAY-PEERS | 65001 | DC1-SPINE1_Ethernet3 |
| DC1-LEAF2B | l3leaf | 172.31.255.34 | UNDERLAY-PEERS | 65001 | DC1-SPINE2_Ethernet3 |
| DC1-LEAF2B | l3leaf | 172.31.255.36 | UNDERLAY-PEERS | 65001 | DC1-SPINE3_Ethernet3 |
| DC1-LEAF2B | l3leaf | 172.31.255.38 | UNDERLAY-PEERS | 65001 | DC1-SPINE4_Ethernet3 |
| DC1-LEAF2B | l3leaf | 192.168.255.1 | EVPN-OVERLAY-PEERS | 65001 | DC1-SPINE1_Loopback0 |
| DC1-LEAF2B | l3leaf | 192.168.255.2 | EVPN-OVERLAY-PEERS | 65001 | DC1-SPINE2_Loopback0 |
| DC1-LEAF2B | l3leaf | 192.168.255.3 | EVPN-OVERLAY-PEERS | 65001 | DC1-SPINE3_Loopback0 |
| DC1-LEAF2B | l3leaf | 192.168.255.4 | EVPN-OVERLAY-PEERS | 65001 | DC1-SPINE4_Loopback0 |
| DC1-SPINE1 | spine | 172.31.255.1 | UNDERLAY-PEERS | 65101 | DC1-LEAF1A_Ethernet1 |
| DC1-SPINE1 | spine | 172.31.255.17 | UNDERLAY-PEERS | 65102 | DC1-LEAF2A_Ethernet1 |
| DC1-SPINE1 | spine | 172.31.255.33 | UNDERLAY-PEERS | 65102 | DC1-LEAF2B_Ethernet1 |
| DC1-SPINE1 | spine | 172.31.255.49 | UNDERLAY-PEERS | 65103 | DC1-SVC3A_Ethernet41 |
| DC1-SPINE1 | spine | 172.31.255.65 | UNDERLAY-PEERS | 65103 | DC1-SVC3B_Ethernet41 |
| DC1-SPINE1 | spine | 172.31.255.81 | UNDERLAY-PEERS | 65104 | DC1-BL1A_Ethernet41 |
| DC1-SPINE1 | spine | 172.31.255.97 | UNDERLAY-PEERS | 65105 | DC1-BL1B_Ethernet45 |
| DC1-SPINE1 | spine | 192.168.255.14 | EVPN-OVERLAY-PEERS | 65104 | DC1-BL1A_Loopback0 |
| DC1-SPINE1 | spine | 192.168.255.15 | EVPN-OVERLAY-PEERS | 65105 | DC1-BL1B_Loopback0 |
| DC1-SPINE1 | spine | 192.168.255.9 | EVPN-OVERLAY-PEERS | 65101 | DC1-LEAF1A_Loopback0 |
| DC1-SPINE1 | spine | 192.168.255.10 | EVPN-OVERLAY-PEERS | 65102 | DC1-LEAF2A_Loopback0 |
| DC1-SPINE1 | spine | 192.168.255.11 | EVPN-OVERLAY-PEERS | 65102 | DC1-LEAF2B_Loopback0 |
| DC1-SPINE1 | spine | 192.168.255.12 | EVPN-OVERLAY-PEERS | 65103 | DC1-SVC3A_Loopback0 |
| DC1-SPINE1 | spine | 192.168.255.13 | EVPN-OVERLAY-PEERS | 65103 | DC1-SVC3B_Loopback0 |
| DC1-SPINE2 | spine | 172.31.255.3 | UNDERLAY-PEERS | 65101 | DC1-LEAF1A_Ethernet2 |
| DC1-SPINE2 | spine | 172.31.255.19 | UNDERLAY-PEERS | 65102 | DC1-LEAF2A_Ethernet2 |
| DC1-SPINE2 | spine | 172.31.255.35 | UNDERLAY-PEERS | 65102 | DC1-LEAF2B_Ethernet2 |
| DC1-SPINE2 | spine | 172.31.255.51 | UNDERLAY-PEERS | 65103 | DC1-SVC3A_Ethernet42 |
| DC1-SPINE2 | spine | 172.31.255.67 | UNDERLAY-PEERS | 65103 | DC1-SVC3B_Ethernet42 |
| DC1-SPINE2 | spine | 172.31.255.83 | UNDERLAY-PEERS | 65104 | DC1-BL1A_Ethernet42 |
| DC1-SPINE2 | spine | 172.31.255.99 | UNDERLAY-PEERS | 65105 | DC1-BL1B_Ethernet46 |
| DC1-SPINE2 | spine | 192.168.255.14 | EVPN-OVERLAY-PEERS | 65104 | DC1-BL1A_Loopback0 |
| DC1-SPINE2 | spine | 192.168.255.15 | EVPN-OVERLAY-PEERS | 65105 | DC1-BL1B_Loopback0 |
| DC1-SPINE2 | spine | 192.168.255.9 | EVPN-OVERLAY-PEERS | 65101 | DC1-LEAF1A_Loopback0 |
| DC1-SPINE2 | spine | 192.168.255.10 | EVPN-OVERLAY-PEERS | 65102 | DC1-LEAF2A_Loopback0 |
| DC1-SPINE2 | spine | 192.168.255.11 | EVPN-OVERLAY-PEERS | 65102 | DC1-LEAF2B_Loopback0 |
| DC1-SPINE2 | spine | 192.168.255.12 | EVPN-OVERLAY-PEERS | 65103 | DC1-SVC3A_Loopback0 |
| DC1-SPINE2 | spine | 192.168.255.13 | EVPN-OVERLAY-PEERS | 65103 | DC1-SVC3B_Loopback0 |
| DC1-SPINE3 | spine | 172.31.255.5 | UNDERLAY-PEERS | 65101 | DC1-LEAF1A_Ethernet3 |
| DC1-SPINE3 | spine | 172.31.255.21 | UNDERLAY-PEERS | 65102 | DC1-LEAF2A_Ethernet3 |
| DC1-SPINE3 | spine | 172.31.255.37 | UNDERLAY-PEERS | 65102 | DC1-LEAF2B_Ethernet3 |
| DC1-SPINE3 | spine | 172.31.255.53 | UNDERLAY-PEERS | 65103 | DC1-SVC3A_Ethernet43 |
| DC1-SPINE3 | spine | 172.31.255.69 | UNDERLAY-PEERS | 65103 | DC1-SVC3B_Ethernet43 |
| DC1-SPINE3 | spine | 172.31.255.85 | UNDERLAY-PEERS | 65104 | DC1-BL1A_Ethernet43 |
| DC1-SPINE3 | spine | 172.31.255.101 | UNDERLAY-PEERS | 65105 | DC1-BL1B_Ethernet47 |
| DC1-SPINE3 | spine | 192.168.255.14 | EVPN-OVERLAY-PEERS | 65104 | DC1-BL1A_Loopback0 |
| DC1-SPINE3 | spine | 192.168.255.15 | EVPN-OVERLAY-PEERS | 65105 | DC1-BL1B_Loopback0 |
| DC1-SPINE3 | spine | 192.168.255.9 | EVPN-OVERLAY-PEERS | 65101 | DC1-LEAF1A_Loopback0 |
| DC1-SPINE3 | spine | 192.168.255.10 | EVPN-OVERLAY-PEERS | 65102 | DC1-LEAF2A_Loopback0 |
| DC1-SPINE3 | spine | 192.168.255.11 | EVPN-OVERLAY-PEERS | 65102 | DC1-LEAF2B_Loopback0 |
| DC1-SPINE3 | spine | 192.168.255.12 | EVPN-OVERLAY-PEERS | 65103 | DC1-SVC3A_Loopback0 |
| DC1-SPINE3 | spine | 192.168.255.13 | EVPN-OVERLAY-PEERS | 65103 | DC1-SVC3B_Loopback0 |
| DC1-SPINE4 | spine | 172.31.255.7 | UNDERLAY-PEERS | 65101 | DC1-LEAF1A_Ethernet4 |
| DC1-SPINE4 | spine | 172.31.255.23 | UNDERLAY-PEERS | 65102 | DC1-LEAF2A_Ethernet4 |
| DC1-SPINE4 | spine | 172.31.255.39 | UNDERLAY-PEERS | 65102 | DC1-LEAF2B_Ethernet4 |
| DC1-SPINE4 | spine | 172.31.255.55 | UNDERLAY-PEERS | 65103 | DC1-SVC3A_Ethernet44 |
| DC1-SPINE4 | spine | 172.31.255.71 | UNDERLAY-PEERS | 65103 | DC1-SVC3B_Ethernet44 |
| DC1-SPINE4 | spine | 172.31.255.87 | UNDERLAY-PEERS | 65104 | DC1-BL1A_Ethernet44 |
| DC1-SPINE4 | spine | 172.31.255.103 | UNDERLAY-PEERS | 65105 | DC1-BL1B_Ethernet48 |
| DC1-SPINE4 | spine | 192.168.255.14 | EVPN-OVERLAY-PEERS | 65104 | DC1-BL1A_Loopback0 |
| DC1-SPINE4 | spine | 192.168.255.15 | EVPN-OVERLAY-PEERS | 65105 | DC1-BL1B_Loopback0 |
| DC1-SPINE4 | spine | 192.168.255.9 | EVPN-OVERLAY-PEERS | 65101 | DC1-LEAF1A_Loopback0 |
| DC1-SPINE4 | spine | 192.168.255.10 | EVPN-OVERLAY-PEERS | 65102 | DC1-LEAF2A_Loopback0 |
| DC1-SPINE4 | spine | 192.168.255.11 | EVPN-OVERLAY-PEERS | 65102 | DC1-LEAF2B_Loopback0 |
| DC1-SPINE4 | spine | 192.168.255.12 | EVPN-OVERLAY-PEERS | 65103 | DC1-SVC3A_Loopback0 |
| DC1-SPINE4 | spine | 192.168.255.13 | EVPN-OVERLAY-PEERS | 65103 | DC1-SVC3B_Loopback0 |
| DC1-SVC3A | l3leaf | 10.255.252.7 | MLAG-PEERS | - | DC1-SVC3B_Vlan4092 |
| DC1-SVC3A | l3leaf | 172.31.255.48 | UNDERLAY-PEERS | 65001 | DC1-SPINE1_Ethernet4 |
| DC1-SVC3A | l3leaf | 172.31.255.50 | UNDERLAY-PEERS | 65001 | DC1-SPINE2_Ethernet4 |
| DC1-SVC3A | l3leaf | 172.31.255.52 | UNDERLAY-PEERS | 65001 | DC1-SPINE3_Ethernet4 |
| DC1-SVC3A | l3leaf | 172.31.255.54 | UNDERLAY-PEERS | 65001 | DC1-SPINE4_Ethernet4 |
| DC1-SVC3A | l3leaf | 192.168.255.1 | EVPN-OVERLAY-PEERS | 65001 | DC1-SPINE1_Loopback0 |
| DC1-SVC3A | l3leaf | 192.168.255.2 | EVPN-OVERLAY-PEERS | 65001 | DC1-SPINE2_Loopback0 |
| DC1-SVC3A | l3leaf | 192.168.255.3 | EVPN-OVERLAY-PEERS | 65001 | DC1-SPINE3_Loopback0 |
| DC1-SVC3A | l3leaf | 192.168.255.4 | EVPN-OVERLAY-PEERS | 65001 | DC1-SPINE4_Loopback0 |
| DC1-SVC3B | l3leaf | 10.255.252.6 | MLAG-PEERS | - | DC1-SVC3A_Vlan4092 |
| DC1-SVC3B | l3leaf | 172.31.255.64 | UNDERLAY-PEERS | 65001 | DC1-SPINE1_Ethernet5 |
| DC1-SVC3B | l3leaf | 172.31.255.66 | UNDERLAY-PEERS | 65001 | DC1-SPINE2_Ethernet5 |
| DC1-SVC3B | l3leaf | 172.31.255.68 | UNDERLAY-PEERS | 65001 | DC1-SPINE3_Ethernet5 |
| DC1-SVC3B | l3leaf | 172.31.255.70 | UNDERLAY-PEERS | 65001 | DC1-SPINE4_Ethernet5 |
| DC1-SVC3B | l3leaf | 192.168.255.1 | EVPN-OVERLAY-PEERS | 65001 | DC1-SPINE1_Loopback0 |
| DC1-SVC3B | l3leaf | 192.168.255.2 | EVPN-OVERLAY-PEERS | 65001 | DC1-SPINE2_Loopback0 |
| DC1-SVC3B | l3leaf | 192.168.255.3 | EVPN-OVERLAY-PEERS | 65001 | DC1-SPINE3_Loopback0 |
| DC1-SVC3B | l3leaf | 192.168.255.4 | EVPN-OVERLAY-PEERS | 65001 | DC1-SPINE4_Loopback0 |

### VRF Routing Protocols

| Node | Type | VRF | Router ID | Redistribute |
| ---- | ---- | --- | --------- | ------------ |
| DC1-BL1A | l3leaf | Tenant_A_WAN_Zone | 192.168.255.14 | connected, static |
| DC1-BL1A | l3leaf | Tenant_L3_VRF_Zone | 192.168.255.14 | connected |
| DC1-BL1A | l3leaf | Tenant_B_OP_Zone | 192.168.255.14 | connected |
| DC1-BL1A | l3leaf | Tenant_B_WAN_Zone | 192.168.255.14 | connected |
| DC1-BL1A | l3leaf | Tenant_C_WAN_Zone | 192.168.255.14 | connected |
| DC1-BL1B | l3leaf | Tenant_A_WAN_Zone | 192.168.255.15 | connected, static |
| DC1-BL1B | l3leaf | Tenant_L3_VRF_Zone | 192.168.255.15 | connected |
| DC1-BL1B | l3leaf | Tenant_B_OP_Zone | 192.168.255.15 | connected |
| DC1-BL1B | l3leaf | Tenant_B_WAN_Zone | 192.168.255.15 | connected |
| DC1-BL1B | l3leaf | Tenant_C_WAN_Zone | 192.168.255.15 | connected |
| DC1-LEAF1A | l3leaf | Tenant_A_APP_Zone | 192.168.255.9 | connected |
| DC1-LEAF1A | l3leaf | Tenant_A_WEB_Zone | 192.168.255.9 | connected |
| DC1-LEAF2A | l3leaf | Tenant_A_APP_Zone | 192.168.255.10 | connected |
| DC1-LEAF2A | l3leaf | Tenant_A_DB_Zone | 192.168.255.10 | connected |
| DC1-LEAF2A | l3leaf | Tenant_A_OP_Zone | 192.168.255.10 | connected |
| DC1-LEAF2A | l3leaf | Tenant_A_WEB_Zone | 192.168.255.10 | connected |
| DC1-LEAF2A | l3leaf | Tenant_B_OP_Zone | 192.168.255.10 | connected |
| DC1-LEAF2A | l3leaf | Tenant_C_OP_Zone | 192.168.255.10 | connected |
| DC1-LEAF2B | l3leaf | Tenant_A_APP_Zone | 192.168.255.11 | connected |
| DC1-LEAF2B | l3leaf | Tenant_A_DB_Zone | 192.168.255.11 | connected |
| DC1-LEAF2B | l3leaf | Tenant_A_OP_Zone | 192.168.255.11 | connected |
| DC1-LEAF2B | l3leaf | Tenant_A_WEB_Zone | 192.168.255.11 | connected |
| DC1-LEAF2B | l3leaf | Tenant_B_OP_Zone | 192.168.255.11 | connected |
| DC1-LEAF2B | l3leaf | Tenant_C_OP_Zone | 192.168.255.11 | connected |
| DC1-SVC3A | l3leaf | Tenant_A_APP_Zone | 192.168.255.12 | connected |
| DC1-SVC3A | l3leaf | Tenant_A_DB_Zone | 192.168.255.12 | connected |
| DC1-SVC3A | l3leaf | Tenant_A_OP_Zone | 192.168.255.12 | connected |
| DC1-SVC3A | l3leaf | Tenant_A_WAN_Zone | 192.168.255.12 | connected, static |
| DC1-SVC3A | l3leaf | Tenant_A_WEB_Zone | 192.168.255.12 | connected |
| DC1-SVC3A | l3leaf | Tenant_B_OP_Zone | 192.168.255.12 | connected |
| DC1-SVC3A | l3leaf | Tenant_B_WAN_Zone | 192.168.255.12 | connected |
| DC1-SVC3A | l3leaf | Tenant_C_OP_Zone | 192.168.255.12 | connected |
| DC1-SVC3A | l3leaf | Tenant_C_WAN_Zone | 192.168.255.12 | connected |
| DC1-SVC3B | l3leaf | Tenant_A_APP_Zone | 192.168.255.13 | connected |
| DC1-SVC3B | l3leaf | Tenant_A_DB_Zone | 192.168.255.13 | connected |
| DC1-SVC3B | l3leaf | Tenant_A_OP_Zone | 192.168.255.13 | connected |
| DC1-SVC3B | l3leaf | Tenant_A_WAN_Zone | 192.168.255.13 | connected, static |
| DC1-SVC3B | l3leaf | Tenant_A_WEB_Zone | 192.168.255.13 | connected |
| DC1-SVC3B | l3leaf | Tenant_B_OP_Zone | 192.168.255.13 | connected |
| DC1-SVC3B | l3leaf | Tenant_B_WAN_Zone | 192.168.255.13 | connected |
| DC1-SVC3B | l3leaf | Tenant_C_OP_Zone | 192.168.255.13 | connected |
| DC1-SVC3B | l3leaf | Tenant_C_WAN_Zone | 192.168.255.13 | connected |

### VTEP Loopback VXLAN Tunnel Source Interfaces (VTEPs Only)

| VTEP Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ------------------ | ------------------- | ------------------ | ------------------ |
| 192.168.254.0/24 | 256 | 4 | 1.57 % |

### VTEP Loopback Node allocation

| POD | Node | Loopback1 |
| --- | ---- | --------- |
| DC1_FABRIC | DC1-BL1A | 192.168.254.14/32 |
| DC1_FABRIC | DC1-BL1B | 192.168.254.15/32 |
| DC1_FABRIC | DC1-SVC3A | 192.168.254.12/32 |
| DC1_FABRIC | DC1-SVC3B | 192.168.254.12/32 |
