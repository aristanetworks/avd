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
  - [VTEP Loopback VXLAN Tunnel Source Interfaces (VTEPs Only)](#vtep-loopback-vxlan-tunnel-source-interfaces-vteps-only)
  - [VTEP Loopback Node allocation](#vtep-loopback-node-allocation)

## Fabric Switches and Management IP

| POD | Type | Node | Management IP | Platform | Provisioned in CloudVision | Serial Number |
| --- | ---- | ---- | ------------- | -------- | -------------------------- | ------------- |
| FABRIC | l3leaf | dc1-leaf1a | 192.168.0.21/24 | cEOS | Provisioned | - |
| FABRIC | l3leaf | dc1-leaf1b | 192.168.0.22/24 | cEOS | Provisioned | - |
| FABRIC | l3leaf | dc1-leaf2a | 192.168.0.23/24 | cEOS | Provisioned | - |
| FABRIC | l3leaf | dc1-leaf2b | 192.168.0.24/24 | cEOS | Provisioned | - |
| FABRIC | spine | dc1-spine1 | 192.168.0.11/24 | cEOS | Provisioned | - |
| FABRIC | spine | dc1-spine2 | 192.168.0.12/24 | cEOS | Provisioned | - |
| FABRIC | spine | dc1-spine3 | 192.168.0.13/24 | cEOS | Provisioned | - |
| FABRIC | spine | dc1-spine4 | 192.168.0.14/24 | cEOS | Provisioned | - |
| FABRIC | super-spine | dc1-ss1 | 192.168.0.25/24 | cEOS | Provisioned | - |
| FABRIC | super-spine | dc1-ss2 | 192.168.0.26/24 | cEOS | Provisioned | - |

> Provision status is based on Ansible inventory declaration and do not represent real status from CloudVision.

### Fabric Switches with inband Management IP

| POD | Type | Node | Management IP | Inband Interface |
| --- | ---- | ---- | ------------- | ---------------- |

## Fabric Topology

| Type | Node | Node Interface | Peer Type | Peer Node | Peer Interface |
| ---- | ---- | -------------- | --------- | ----------| -------------- |
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

### VTEP Loopback VXLAN Tunnel Source Interfaces (VTEPs Only)

| VTEP Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| --------------------- | ------------------- | ------------------ | ------------------ |
| 192.168.102.0/24 | 256 | 4 | 1.57 % |

### VTEP Loopback Node allocation

| POD | Node | Loopback1 |
| --- | ---- | --------- |
| FABRIC | dc1-leaf1a | 192.168.102.1/32 |
| FABRIC | dc1-leaf1b | 192.168.102.1/32 |
| FABRIC | dc1-leaf2a | 192.168.102.3/32 |
| FABRIC | dc1-leaf2b | 192.168.102.3/32 |
