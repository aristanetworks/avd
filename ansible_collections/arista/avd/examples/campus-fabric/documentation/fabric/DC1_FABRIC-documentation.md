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
  - [VTEP Loopback VXLAN Tunnel Source Interfaces (VTEPs Only)](#vtep-loopback-vxlan-tunnel-source-interfaces-vteps-only)
  - [VTEP Loopback Node allocation](#vtep-loopback-node-allocation)

## Fabric Switches and Management IP

| POD | Type | Node | Management IP | Platform | Provisioned in CloudVision | Serial Number |
| --- | ---- | ---- | ------------- | -------- | -------------------------- | ------------- |
| DC1_FABRIC | l2leaf | LEAF1A | 172.16.100.103/24 | cEOSLab | Provisioned | - |
| DC1_FABRIC | l2leaf | LEAF1B | 172.16.100.104/24 | cEOSLab | Provisioned | - |
| DC1_FABRIC | l2leaf | LEAF2A | 172.16.100.105/24 | 720XP | Provisioned | - |
| DC1_FABRIC | l2leaf | LEAF3A | 172.16.100.106/24 | cEOSLab | Provisioned | - |
| DC1_FABRIC | l2leaf | LEAF3B | 172.16.100.107/24 | cEOSLab | Provisioned | - |
| DC1_FABRIC | l2leaf | LEAF3C | 172.16.100.108/24 | cEOSLab | Provisioned | - |
| DC1_FABRIC | l2leaf | LEAF3D | 172.16.100.109/24 | cEOSLab | Provisioned | - |
| DC1_FABRIC | l2leaf | LEAF3E | 172.16.100.110/24 | cEOSLab | Provisioned | - |
| DC1_FABRIC | l3spine | SPINE1 | 172.16.100.101/24 | cEOSLab | Provisioned | - |
| DC1_FABRIC | l3spine | SPINE2 | 172.16.100.102/24 | cEOSLab | Provisioned | - |

> Provision status is based on Ansible inventory declaration and do not represent real status from CloudVision.

### Fabric Switches with inband Management IP

| POD | Type | Node | Management IP | Inband Interface |
| --- | ---- | ---- | ------------- | ---------------- |
| DC1_FABRIC | l2leaf | LEAF1A | 10.10.10.6/24 | Vlan10 |
| DC1_FABRIC | l2leaf | LEAF1B | 10.10.10.7/24 | Vlan10 |
| DC1_FABRIC | l2leaf | LEAF2A | 10.10.10.8/24 | Vlan10 |
| DC1_FABRIC | l2leaf | LEAF3A | 10.10.10.9/24 | Vlan10 |
| DC1_FABRIC | l2leaf | LEAF3B | 10.10.10.10/24 | Vlan10 |
| DC1_FABRIC | l2leaf | LEAF3C | 10.10.10.11/24 | Vlan10 |
| DC1_FABRIC | l2leaf | LEAF3D | 10.10.10.12/24 | Vlan10 |
| DC1_FABRIC | l2leaf | LEAF3E | 10.10.10.13/24 | Vlan10 |

## Fabric Topology

| Type | Node | Node Interface | Peer Type | Peer Node | Peer Interface |
| ---- | ---- | -------------- | --------- | ----------| -------------- |
| l2leaf | LEAF1A | Ethernet51 | l3spine | SPINE1 | Ethernet1 |
| l2leaf | LEAF1A | Ethernet53 | mlag_peer | LEAF1B | Ethernet53 |
| l2leaf | LEAF1A | Ethernet54 | mlag_peer | LEAF1B | Ethernet54 |
| l2leaf | LEAF1B | Ethernet51 | l3spine | SPINE2 | Ethernet1 |
| l2leaf | LEAF2A | Ethernet1/1 | l3spine | SPINE1 | Ethernet49/1 |
| l2leaf | LEAF2A | Ethernet1/3 | l3spine | SPINE2 | Ethernet49/1 |
| l2leaf | LEAF3A | Ethernet97/1 | l3spine | SPINE1 | Ethernet50/1 |
| l2leaf | LEAF3A | Ethernet97/2 | l3spine | SPINE2 | Ethernet50/1 |
| l2leaf | LEAF3A | Ethernet97/3 | l2leaf | LEAF3C | Ethernet97/1 |
| l2leaf | LEAF3A | Ethernet97/4 | l2leaf | LEAF3D | Ethernet97/1 |
| l2leaf | LEAF3A | Ethernet98/1 | l2leaf | LEAF3E | Ethernet97/1 |
| l2leaf | LEAF3A | Ethernet98/3 | mlag_peer | LEAF3B | Ethernet98/3 |
| l2leaf | LEAF3A | Ethernet98/4 | mlag_peer | LEAF3B | Ethernet98/4 |
| l2leaf | LEAF3B | Ethernet97/1 | l3spine | SPINE1 | Ethernet51/1 |
| l2leaf | LEAF3B | Ethernet97/2 | l3spine | SPINE2 | Ethernet51/1 |
| l2leaf | LEAF3B | Ethernet97/3 | l2leaf | LEAF3C | Ethernet97/2 |
| l2leaf | LEAF3B | Ethernet97/4 | l2leaf | LEAF3D | Ethernet97/2 |
| l2leaf | LEAF3B | Ethernet98/1 | l2leaf | LEAF3E | Ethernet97/2 |
| l3spine | SPINE1 | Ethernet55/1 | mlag_peer | SPINE2 | Ethernet55/1 |
| l3spine | SPINE1 | Ethernet56/1 | mlag_peer | SPINE2 | Ethernet56/1 |

## Fabric IP Allocation

### Fabric Point-To-Point Links

| Uplink IPv4 Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ---------------- | ------------------- | ------------------ | ------------------ |

### Point-To-Point Links Node Allocation

| Node | Node Interface | Node IP Address | Peer Node | Peer Interface | Peer IP Address |
| ---- | -------------- | --------------- | --------- | -------------- | --------------- |

### Loopback Interfaces (BGP EVPN Peering)

| Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ------------- | ------------------- | ------------------ | ------------------ |
| 172.16.1.0/24 | 256 | 2 | 0.79 % |

### Loopback0 Interfaces Node Allocation

| POD | Node | Loopback0 |
| --- | ---- | --------- |
| DC1_FABRIC | SPINE1 | 172.16.1.1/32 |
| DC1_FABRIC | SPINE2 | 172.16.1.2/32 |

### VTEP Loopback VXLAN Tunnel Source Interfaces (VTEPs Only)

| VTEP Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ------------------ | ------------------- | ------------------ | ------------------ |

### VTEP Loopback Node allocation

| POD | Node | Loopback1 |
| --- | ---- | --------- |
