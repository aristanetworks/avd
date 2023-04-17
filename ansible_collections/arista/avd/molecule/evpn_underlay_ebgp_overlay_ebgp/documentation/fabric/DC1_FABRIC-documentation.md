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
| ---- | ---- | -------------- | --------- | ----------| -------------- |
| l3leaf | DC1-BL1A | Ethernet41 | spine | DC1-SPINE1 | Ethernet6 |
| l3leaf | DC1-BL1A | Ethernet42 | spine | DC1-SPINE2 | Ethernet6 |
| l3leaf | DC1-BL1A | Ethernet43 | spine | DC1-SPINE3 | Ethernet6 |
| l3leaf | DC1-BL1A | Ethernet44 | spine | DC1-SPINE4 | Ethernet6 |

## Fabric IP Allocation

### Fabric Point-To-Point Links

| Uplink IPv4 Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ---------------- | ------------------- | ------------------ | ------------------ |
| 172.31.255.0/24 | 256 | 4 | 1.57 % |

### Point-To-Point Links Node Allocation

| Node | Node Interface | Node IP Address | Peer Node | Peer Interface | Peer IP Address |
| ---- | -------------- | --------------- | --------- | -------------- | --------------- |

### Loopback Interfaces (BGP EVPN Peering)

| Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ------------- | ------------------- | ------------------ | ------------------ |
| 192.168.255.0/24 | 256 | 1 | 0.4 % |

### Loopback0 Interfaces Node Allocation

| POD | Node | Loopback0 |
| --- | ---- | --------- |
| DC1_FABRIC | DC1-BL1A | 192.168.255.14/32 |

### VTEP Loopback VXLAN Tunnel Source Interfaces (VTEPs Only)

| VTEP Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| --------------------- | ------------------- | ------------------ | ------------------ |
| 192.168.254.0/24 | 256 | 1 | 0.4 % |

### VTEP Loopback Node allocation

| POD | Node | Loopback1 |
| --- | ---- | --------- |
| DC1_FABRIC | DC1-BL1A | 192.168.254.14/32 |
