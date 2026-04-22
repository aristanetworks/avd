# FABRIC

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
| FABRIC | l3leaf | dc1-leaf1a | 172.16.1.21/24 | cEOSLab | Provisioned | - |
| FABRIC | l3leaf | dc1-leaf1b | 172.16.1.22/24 | cEOSLab | Provisioned | - |
| FABRIC | l3leaf | dc1-leaf2a | 172.16.1.23/24 | cEOSLab | Provisioned | - |
| FABRIC | l3leaf | dc1-leaf2b | 172.16.1.24/24 | cEOSLab | Provisioned | - |
| FABRIC | spine | dc1-spine1 | 172.16.1.11/24 | cEOSLab | Provisioned | - |
| FABRIC | spine | dc1-spine2 | 172.16.1.12/24 | cEOSLab | Provisioned | - |
| FABRIC | spine | dc1-spine3 | 172.16.1.13/24 | cEOSLab | Provisioned | - |
| FABRIC | spine | dc1-spine4 | 172.16.1.14/24 | cEOSLab | Provisioned | - |
| FABRIC | super-spine | dc1-ss1 | 172.16.1.25/24 | cEOSLab | Provisioned | - |
| FABRIC | super-spine | dc1-ss2 | 172.16.1.26/24 | cEOSLab | Provisioned | - |

> Provision status is based on Ansible inventory declaration and do not represent real status from CloudVision.

### Fabric Switches with inband Management IP

| POD | Type | Node | Management IP | Inband Interface |
| --- | ---- | ---- | ------------- | ---------------- |

## Fabric Topology

| Type | Node | Node Interface | Peer Type | Peer Node | Peer Interface |
| ---- | ---- | -------------- | --------- | --------- | -------------- |
| l3leaf | dc1-leaf1a | Ethernet1 | spine | dc1-spine1 | Ethernet3 |
| l3leaf | dc1-leaf1a | Ethernet2 | spine | dc1-spine2 | Ethernet3 |
| l3leaf | dc1-leaf1a | Ethernet3 | mlag_peer | dc1-leaf1b | Ethernet3 |
| l3leaf | dc1-leaf1a | Ethernet4 | mlag_peer | dc1-leaf1b | Ethernet4 |
| l3leaf | dc1-leaf1b | Ethernet1 | spine | dc1-spine1 | Ethernet4 |
| l3leaf | dc1-leaf1b | Ethernet2 | spine | dc1-spine2 | Ethernet4 |
| l3leaf | dc1-leaf2a | Ethernet1 | spine | dc1-spine3 | Ethernet3 |
| l3leaf | dc1-leaf2a | Ethernet2 | spine | dc1-spine4 | Ethernet3 |
| l3leaf | dc1-leaf2a | Ethernet3 | mlag_peer | dc1-leaf2b | Ethernet3 |
| l3leaf | dc1-leaf2a | Ethernet4 | mlag_peer | dc1-leaf2b | Ethernet4 |
| l3leaf | dc1-leaf2b | Ethernet1 | spine | dc1-spine3 | Ethernet4 |
| l3leaf | dc1-leaf2b | Ethernet2 | spine | dc1-spine4 | Ethernet4 |
| spine | dc1-spine1 | Ethernet1 | super-spine | dc1-ss1 | Ethernet1 |
| spine | dc1-spine1 | Ethernet2 | super-spine | dc1-ss2 | Ethernet1 |
| spine | dc1-spine2 | Ethernet1 | super-spine | dc1-ss1 | Ethernet2 |
| spine | dc1-spine2 | Ethernet2 | super-spine | dc1-ss2 | Ethernet2 |
| spine | dc1-spine3 | Ethernet1 | super-spine | dc1-ss1 | Ethernet3 |
| spine | dc1-spine3 | Ethernet2 | super-spine | dc1-ss2 | Ethernet3 |
| spine | dc1-spine4 | Ethernet1 | super-spine | dc1-ss1 | Ethernet4 |
| spine | dc1-spine4 | Ethernet2 | super-spine | dc1-ss2 | Ethernet4 |

## Fabric IP Allocation

### Fabric Point-To-Point Links

| Uplink IPv4 Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ---------------- | ------------------- | ------------------ | ------------------ |
| 192.168.103.0/24 | 256 | 32 | 12.5 % |

### Point-To-Point Links Node Allocation

| Node | Node Interface | Node IP Address | Peer Node | Peer Interface | Peer IP Address |
| ---- | -------------- | --------------- | --------- | -------------- | --------------- |
| dc1-leaf1a | Ethernet1 | 192.168.103.1/31 | dc1-spine1 | Ethernet3 | 192.168.103.0/31 |
| dc1-leaf1a | Ethernet2 | 192.168.103.3/31 | dc1-spine2 | Ethernet3 | 192.168.103.2/31 |
| dc1-leaf1b | Ethernet1 | 192.168.103.5/31 | dc1-spine1 | Ethernet4 | 192.168.103.4/31 |
| dc1-leaf1b | Ethernet2 | 192.168.103.7/31 | dc1-spine2 | Ethernet4 | 192.168.103.6/31 |
| dc1-leaf2a | Ethernet1 | 192.168.103.9/31 | dc1-spine3 | Ethernet3 | 192.168.103.8/31 |
| dc1-leaf2a | Ethernet2 | 192.168.103.11/31 | dc1-spine4 | Ethernet3 | 192.168.103.10/31 |
| dc1-leaf2b | Ethernet1 | 192.168.103.13/31 | dc1-spine3 | Ethernet4 | 192.168.103.12/31 |
| dc1-leaf2b | Ethernet2 | 192.168.103.15/31 | dc1-spine4 | Ethernet4 | 192.168.103.14/31 |
| dc1-spine1 | Ethernet1 | 192.168.103.41/31 | dc1-ss1 | Ethernet1 | 192.168.103.40/31 |
| dc1-spine1 | Ethernet2 | 192.168.103.43/31 | dc1-ss2 | Ethernet1 | 192.168.103.42/31 |
| dc1-spine2 | Ethernet1 | 192.168.103.45/31 | dc1-ss1 | Ethernet2 | 192.168.103.44/31 |
| dc1-spine2 | Ethernet2 | 192.168.103.47/31 | dc1-ss2 | Ethernet2 | 192.168.103.46/31 |
| dc1-spine3 | Ethernet1 | 192.168.103.49/31 | dc1-ss1 | Ethernet3 | 192.168.103.48/31 |
| dc1-spine3 | Ethernet2 | 192.168.103.51/31 | dc1-ss2 | Ethernet3 | 192.168.103.50/31 |
| dc1-spine4 | Ethernet1 | 192.168.103.53/31 | dc1-ss1 | Ethernet4 | 192.168.103.52/31 |
| dc1-spine4 | Ethernet2 | 192.168.103.55/31 | dc1-ss2 | Ethernet4 | 192.168.103.54/31 |

### Loopback Interfaces (BGP EVPN Peering)

| Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ------------- | ------------------- | ------------------ | ------------------ |
| 192.168.101.0/24 | 256 | 10 | 3.91 % |

### Loopback0 Interfaces Node Allocation

| POD | Node | Loopback0 |
| --- | ---- | --------- |
| FABRIC | dc1-leaf1a | 192.168.101.1/32 |
| FABRIC | dc1-leaf1b | 192.168.101.2/32 |
| FABRIC | dc1-leaf2a | 192.168.101.3/32 |
| FABRIC | dc1-leaf2b | 192.168.101.4/32 |
| FABRIC | dc1-spine1 | 192.168.101.11/32 |
| FABRIC | dc1-spine2 | 192.168.101.12/32 |
| FABRIC | dc1-spine3 | 192.168.101.13/32 |
| FABRIC | dc1-spine4 | 192.168.101.14/32 |
| FABRIC | dc1-ss1 | 192.168.101.201/32 |
| FABRIC | dc1-ss2 | 192.168.101.202/32 |

### VRF Summary

| VRF | RD Pattern | Import RT | Export RT | Nodes |
| --- | ---------- | --------- | --------- | ----- |
| VRF_A | 10 | 10:10 | 10:10 | dc1-leaf1a, dc1-leaf1b, dc1-leaf2a, dc1-leaf2b |

### BGP Peer Groups

| Peer Group | Remote AS | Update Source | BFD | Send Community | Nodes |
| ---------- | --------- | ------------- | --- | -------------- | ----- |
| EVPN-OVERLAY-PEERS | - | Loopback0 | Yes | all | dc1-leaf1a, dc1-leaf1b, dc1-leaf2a, dc1-leaf2b, dc1-spine1, dc1-spine2, dc1-spine3, dc1-spine4, dc1-ss1, dc1-ss2 |
| IPv4-UNDERLAY-PEERS | - | - | No | all | dc1-leaf1a, dc1-leaf1b, dc1-leaf2a, dc1-leaf2b, dc1-spine1, dc1-spine2, dc1-spine3, dc1-spine4, dc1-ss1, dc1-ss2 |
| MLAG-IPv4-UNDERLAY-PEER | - | - | No | all | dc1-leaf1a, dc1-leaf1b, dc1-leaf2a, dc1-leaf2b |

### BGP Neighbors

| Node | Type | Neighbor IP | Peer Group | Remote AS | Description |
| ---- | ---- | ----------- | ---------- | --------- | ----------- |
| dc1-leaf1a | l3leaf | 10.255.251.1 | MLAG-IPv4-UNDERLAY-PEER | - | dc1-leaf1b_Vlan4093 |
| dc1-leaf1a | l3leaf | 192.168.103.0 | IPv4-UNDERLAY-PEERS | 65001 | dc1-spine1_Ethernet3 |
| dc1-leaf1a | l3leaf | 192.168.103.2 | IPv4-UNDERLAY-PEERS | 65001 | dc1-spine2_Ethernet3 |
| dc1-leaf1a | l3leaf | 192.168.101.11 | EVPN-OVERLAY-PEERS | 65001 | dc1-spine1_Loopback0 |
| dc1-leaf1a | l3leaf | 192.168.101.12 | EVPN-OVERLAY-PEERS | 65001 | dc1-spine2_Loopback0 |
| dc1-leaf1b | l3leaf | 10.255.251.0 | MLAG-IPv4-UNDERLAY-PEER | - | dc1-leaf1a_Vlan4093 |
| dc1-leaf1b | l3leaf | 192.168.103.4 | IPv4-UNDERLAY-PEERS | 65001 | dc1-spine1_Ethernet4 |
| dc1-leaf1b | l3leaf | 192.168.103.6 | IPv4-UNDERLAY-PEERS | 65001 | dc1-spine2_Ethernet4 |
| dc1-leaf1b | l3leaf | 192.168.101.11 | EVPN-OVERLAY-PEERS | 65001 | dc1-spine1_Loopback0 |
| dc1-leaf1b | l3leaf | 192.168.101.12 | EVPN-OVERLAY-PEERS | 65001 | dc1-spine2_Loopback0 |
| dc1-leaf2a | l3leaf | 10.255.251.5 | MLAG-IPv4-UNDERLAY-PEER | - | dc1-leaf2b_Vlan4093 |
| dc1-leaf2a | l3leaf | 192.168.103.8 | IPv4-UNDERLAY-PEERS | 65002 | dc1-spine3_Ethernet3 |
| dc1-leaf2a | l3leaf | 192.168.103.10 | IPv4-UNDERLAY-PEERS | 65002 | dc1-spine4_Ethernet3 |
| dc1-leaf2a | l3leaf | 192.168.101.13 | EVPN-OVERLAY-PEERS | 65002 | dc1-spine3_Loopback0 |
| dc1-leaf2a | l3leaf | 192.168.101.14 | EVPN-OVERLAY-PEERS | 65002 | dc1-spine4_Loopback0 |
| dc1-leaf2b | l3leaf | 10.255.251.4 | MLAG-IPv4-UNDERLAY-PEER | - | dc1-leaf2a_Vlan4093 |
| dc1-leaf2b | l3leaf | 192.168.103.12 | IPv4-UNDERLAY-PEERS | 65002 | dc1-spine3_Ethernet4 |
| dc1-leaf2b | l3leaf | 192.168.103.14 | IPv4-UNDERLAY-PEERS | 65002 | dc1-spine4_Ethernet4 |
| dc1-leaf2b | l3leaf | 192.168.101.13 | EVPN-OVERLAY-PEERS | 65002 | dc1-spine3_Loopback0 |
| dc1-leaf2b | l3leaf | 192.168.101.14 | EVPN-OVERLAY-PEERS | 65002 | dc1-spine4_Loopback0 |
| dc1-spine1 | spine | 192.168.103.40 | IPv4-UNDERLAY-PEERS | 65000 | dc1-ss1_Ethernet1 |
| dc1-spine1 | spine | 192.168.103.42 | IPv4-UNDERLAY-PEERS | 65000 | dc1-ss2_Ethernet1 |
| dc1-spine1 | spine | 192.168.103.1 | IPv4-UNDERLAY-PEERS | 65100 | dc1-leaf1a_Ethernet1 |
| dc1-spine1 | spine | 192.168.103.5 | IPv4-UNDERLAY-PEERS | 65100 | dc1-leaf1b_Ethernet1 |
| dc1-spine1 | spine | 192.168.101.201 | EVPN-OVERLAY-PEERS | 65000 | dc1-ss1_Loopback0 |
| dc1-spine1 | spine | 192.168.101.202 | EVPN-OVERLAY-PEERS | 65000 | dc1-ss2_Loopback0 |
| dc1-spine1 | spine | 192.168.101.1 | EVPN-OVERLAY-PEERS | 65100 | dc1-leaf1a_Loopback0 |
| dc1-spine1 | spine | 192.168.101.2 | EVPN-OVERLAY-PEERS | 65100 | dc1-leaf1b_Loopback0 |
| dc1-spine2 | spine | 192.168.103.44 | IPv4-UNDERLAY-PEERS | 65000 | dc1-ss1_Ethernet2 |
| dc1-spine2 | spine | 192.168.103.46 | IPv4-UNDERLAY-PEERS | 65000 | dc1-ss2_Ethernet2 |
| dc1-spine2 | spine | 192.168.103.3 | IPv4-UNDERLAY-PEERS | 65100 | dc1-leaf1a_Ethernet2 |
| dc1-spine2 | spine | 192.168.103.7 | IPv4-UNDERLAY-PEERS | 65100 | dc1-leaf1b_Ethernet2 |
| dc1-spine2 | spine | 192.168.101.201 | EVPN-OVERLAY-PEERS | 65000 | dc1-ss1_Loopback0 |
| dc1-spine2 | spine | 192.168.101.202 | EVPN-OVERLAY-PEERS | 65000 | dc1-ss2_Loopback0 |
| dc1-spine2 | spine | 192.168.101.1 | EVPN-OVERLAY-PEERS | 65100 | dc1-leaf1a_Loopback0 |
| dc1-spine2 | spine | 192.168.101.2 | EVPN-OVERLAY-PEERS | 65100 | dc1-leaf1b_Loopback0 |
| dc1-spine3 | spine | 192.168.103.48 | IPv4-UNDERLAY-PEERS | 65000 | dc1-ss1_Ethernet3 |
| dc1-spine3 | spine | 192.168.103.50 | IPv4-UNDERLAY-PEERS | 65000 | dc1-ss2_Ethernet3 |
| dc1-spine3 | spine | 192.168.103.9 | IPv4-UNDERLAY-PEERS | 65102 | dc1-leaf2a_Ethernet1 |
| dc1-spine3 | spine | 192.168.103.13 | IPv4-UNDERLAY-PEERS | 65102 | dc1-leaf2b_Ethernet1 |
| dc1-spine3 | spine | 192.168.101.201 | EVPN-OVERLAY-PEERS | 65000 | dc1-ss1_Loopback0 |
| dc1-spine3 | spine | 192.168.101.202 | EVPN-OVERLAY-PEERS | 65000 | dc1-ss2_Loopback0 |
| dc1-spine3 | spine | 192.168.101.3 | EVPN-OVERLAY-PEERS | 65102 | dc1-leaf2a_Loopback0 |
| dc1-spine3 | spine | 192.168.101.4 | EVPN-OVERLAY-PEERS | 65102 | dc1-leaf2b_Loopback0 |
| dc1-spine4 | spine | 192.168.103.52 | IPv4-UNDERLAY-PEERS | 65000 | dc1-ss1_Ethernet4 |
| dc1-spine4 | spine | 192.168.103.54 | IPv4-UNDERLAY-PEERS | 65000 | dc1-ss2_Ethernet4 |
| dc1-spine4 | spine | 192.168.103.11 | IPv4-UNDERLAY-PEERS | 65102 | dc1-leaf2a_Ethernet2 |
| dc1-spine4 | spine | 192.168.103.15 | IPv4-UNDERLAY-PEERS | 65102 | dc1-leaf2b_Ethernet2 |
| dc1-spine4 | spine | 192.168.101.201 | EVPN-OVERLAY-PEERS | 65000 | dc1-ss1_Loopback0 |
| dc1-spine4 | spine | 192.168.101.202 | EVPN-OVERLAY-PEERS | 65000 | dc1-ss2_Loopback0 |
| dc1-spine4 | spine | 192.168.101.3 | EVPN-OVERLAY-PEERS | 65102 | dc1-leaf2a_Loopback0 |
| dc1-spine4 | spine | 192.168.101.4 | EVPN-OVERLAY-PEERS | 65102 | dc1-leaf2b_Loopback0 |
| dc1-ss1 | super-spine | 192.168.103.41 | IPv4-UNDERLAY-PEERS | 65001 | dc1-spine1_Ethernet1 |
| dc1-ss1 | super-spine | 192.168.103.45 | IPv4-UNDERLAY-PEERS | 65001 | dc1-spine2_Ethernet1 |
| dc1-ss1 | super-spine | 192.168.103.49 | IPv4-UNDERLAY-PEERS | 65002 | dc1-spine3_Ethernet1 |
| dc1-ss1 | super-spine | 192.168.103.53 | IPv4-UNDERLAY-PEERS | 65002 | dc1-spine4_Ethernet1 |
| dc1-ss1 | super-spine | 192.168.101.11 | EVPN-OVERLAY-PEERS | 65001 | dc1-spine1_Loopback0 |
| dc1-ss1 | super-spine | 192.168.101.12 | EVPN-OVERLAY-PEERS | 65001 | dc1-spine2_Loopback0 |
| dc1-ss1 | super-spine | 192.168.101.13 | EVPN-OVERLAY-PEERS | 65002 | dc1-spine3_Loopback0 |
| dc1-ss1 | super-spine | 192.168.101.14 | EVPN-OVERLAY-PEERS | 65002 | dc1-spine4_Loopback0 |
| dc1-ss2 | super-spine | 192.168.103.43 | IPv4-UNDERLAY-PEERS | 65001 | dc1-spine1_Ethernet2 |
| dc1-ss2 | super-spine | 192.168.103.47 | IPv4-UNDERLAY-PEERS | 65001 | dc1-spine2_Ethernet2 |
| dc1-ss2 | super-spine | 192.168.103.51 | IPv4-UNDERLAY-PEERS | 65002 | dc1-spine3_Ethernet2 |
| dc1-ss2 | super-spine | 192.168.103.55 | IPv4-UNDERLAY-PEERS | 65002 | dc1-spine4_Ethernet2 |
| dc1-ss2 | super-spine | 192.168.101.11 | EVPN-OVERLAY-PEERS | 65001 | dc1-spine1_Loopback0 |
| dc1-ss2 | super-spine | 192.168.101.12 | EVPN-OVERLAY-PEERS | 65001 | dc1-spine2_Loopback0 |
| dc1-ss2 | super-spine | 192.168.101.13 | EVPN-OVERLAY-PEERS | 65002 | dc1-spine3_Loopback0 |
| dc1-ss2 | super-spine | 192.168.101.14 | EVPN-OVERLAY-PEERS | 65002 | dc1-spine4_Loopback0 |

### VRF Routing Protocols

| Node | Type | VRF | Router ID | Redistribute |
| ---- | ---- | --- | --------- | ------------ |
| dc1-leaf1a | l3leaf | VRF_A | 192.168.101.1 | connected |
| dc1-leaf1b | l3leaf | VRF_A | 192.168.101.2 | connected |
| dc1-leaf2a | l3leaf | VRF_A | 192.168.101.3 | connected |
| dc1-leaf2b | l3leaf | VRF_A | 192.168.101.4 | connected |

### VTEP Loopback VXLAN Tunnel Source Interfaces (VTEPs Only)

| VTEP Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ------------------ | ------------------- | ------------------ | ------------------ |
| 192.168.102.0/24 | 256 | 4 | 1.57 % |

### VTEP Loopback Node allocation

| POD | Node | Loopback1 |
| --- | ---- | --------- |
| FABRIC | dc1-leaf1a | 192.168.102.1/32 |
| FABRIC | dc1-leaf1b | 192.168.102.1/32 |
| FABRIC | dc1-leaf2a | 192.168.102.3/32 |
| FABRIC | dc1-leaf2b | 192.168.102.3/32 |
