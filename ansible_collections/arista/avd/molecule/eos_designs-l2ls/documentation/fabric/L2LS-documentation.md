# L2LS

## Table of Contents

- [Fabric Switches and Management IP](#fabric-switches-and-management-ip)
  - [Fabric Switches with inband Management IP](#fabric-switches-with-inband-management-ip)
- [Fabric Topology](#fabric-topology)
- [Fabric IP Allocation](#fabric-ip-allocation)
  - [Fabric Point-To-Point Links](#fabric-point-to-point-links)
  - [Point-To-Point Links Node Allocation](#point-to-point-links-node-allocation)
  - [Loopback Interfaces (BGP EVPN Peering)](#loopback-interfaces-bgp-evpn-peering)
  - [Loopback0 Interfaces Node Allocation](#loopback0-interfaces-node-allocation)
  - [ISIS CLNS interfaces](#isis-clns-interfaces)
  - [VTEP Loopback VXLAN Tunnel Source Interfaces (VTEPs Only)](#vtep-loopback-vxlan-tunnel-source-interfaces-vteps-only)
  - [VTEP Loopback Node allocation](#vtep-loopback-node-allocation)

## Fabric Switches and Management IP

| POD | Type | Node | Management IP | Platform | Provisioned in CloudVision | Serial Number |
| --- | ---- | ---- | ------------- | -------- | -------------------------- | ------------- |
| L2LS_BGP | leaf | BGP-LEAF1 | - | - | Provisioned | - |
| L2LS_BGP | leaf | BGP-LEAF2 | - | - | Provisioned | - |
| L2LS_BGP | l3spine | BGP-SPINE1 | - | - | Provisioned | - |
| L2LS_BGP | l3spine | BGP-SPINE2 | - | - | Provisioned | - |
| L2LS_ISIS | leaf | ISIS-LEAF1 | 192.168.200.105/24 | vEOS-LAB | Provisioned | - |
| L2LS_ISIS | l3spine | ISIS-SPINE1 | 192.168.200.101/24 | vEOS-LAB | Provisioned | - |
| L2LS_L2ONLY | leaf | L2ONLY-LEAF1 | - | - | Provisioned | - |
| L2LS_L2ONLY | leaf | L2ONLY-LEAF2 | - | - | Provisioned | - |
| L2LS_L2ONLY | spine | L2ONLY-SPINE1 | - | - | Provisioned | - |
| L2LS_L2ONLY | spine | L2ONLY-SPINE2 | - | - | Provisioned | - |
| L2LS_OSPF | leaf | OSPF-LEAF1 | - | - | Provisioned | - |
| L2LS_OSPF | leaf | OSPF-LEAF2 | - | - | Provisioned | - |
| L2LS_OSPF | l3spine | OSPF-SPINE1 | - | - | Provisioned | - |
| L2LS_OSPF | l3spine | OSPF-SPINE2 | - | - | Provisioned | - |

> Provision status is based on Ansible inventory declaration and do not represent real status from CloudVision.

### Fabric Switches with inband Management IP

| POD | Type | Node | Management IP | Inband Interface |
| --- | ---- | ---- | ------------- | ---------------- |

## Fabric Topology

| Type | Node | Node Interface | Peer Type | Peer Node | Peer Interface |
| ---- | ---- | -------------- | --------- | ----------| -------------- |
| leaf | BGP-LEAF1 | Ethernet1 | l3spine | BGP-SPINE1 | Ethernet1 |
| leaf | BGP-LEAF1 | Ethernet2 | l3spine | BGP-SPINE2 | Ethernet1 |
| leaf | BGP-LEAF2 | Ethernet1 | l3spine | BGP-SPINE1 | Ethernet2 |
| leaf | BGP-LEAF2 | Ethernet2 | l3spine | BGP-SPINE2 | Ethernet2 |
| l3spine | BGP-SPINE1 | Ethernet3 | mlag_peer | BGP-SPINE2 | Ethernet3 |
| l3spine | BGP-SPINE1 | Ethernet4 | mlag_peer | BGP-SPINE2 | Ethernet4 |
| leaf | ISIS-LEAF1 | Ethernet1 | l3spine | ISIS-SPINE1 | Ethernet1 |
| leaf | L2ONLY-LEAF1 | Ethernet1 | spine | L2ONLY-SPINE1 | Ethernet1 |
| leaf | L2ONLY-LEAF1 | Ethernet2 | spine | L2ONLY-SPINE2 | Ethernet1 |
| leaf | L2ONLY-LEAF2 | Ethernet1 | spine | L2ONLY-SPINE1 | Ethernet2 |
| leaf | L2ONLY-LEAF2 | Ethernet2 | spine | L2ONLY-SPINE2 | Ethernet2 |
| spine | L2ONLY-SPINE1 | Ethernet3 | mlag_peer | L2ONLY-SPINE2 | Ethernet3 |
| spine | L2ONLY-SPINE1 | Ethernet4 | mlag_peer | L2ONLY-SPINE2 | Ethernet4 |
| leaf | OSPF-LEAF1 | Ethernet1 | l3spine | OSPF-SPINE1 | Ethernet1 |
| leaf | OSPF-LEAF1 | Ethernet2 | l3spine | OSPF-SPINE2 | Ethernet1 |
| leaf | OSPF-LEAF2 | Ethernet1 | l3spine | OSPF-SPINE1 | Ethernet2 |
| leaf | OSPF-LEAF2 | Ethernet2 | l3spine | OSPF-SPINE2 | Ethernet2 |
| l3spine | OSPF-SPINE1 | Ethernet3 | mlag_peer | OSPF-SPINE2 | Ethernet3 |
| l3spine | OSPF-SPINE1 | Ethernet4 | mlag_peer | OSPF-SPINE2 | Ethernet4 |

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
| 192.168.255.0/24 | 256 | 5 | 1.96 % |

### Loopback0 Interfaces Node Allocation

| POD | Node | Loopback0 |
| --- | ---- | --------- |
| L2LS_BGP | BGP-SPINE1 | 192.168.255.1/32 |
| L2LS_BGP | BGP-SPINE2 | 192.168.255.2/32 |
| L2LS_ISIS | ISIS-SPINE1 | 192.168.255.1/32 |
| L2LS_OSPF | OSPF-SPINE1 | 192.168.255.1/32 |
| L2LS_OSPF | OSPF-SPINE2 | 192.168.255.2/32 |

### ISIS CLNS interfaces

| POD | Node | CLNS Address |
| --- | ---- | ------------ |
| L2LS_ISIS | ISIS-SPINE1 | 49.0001.0001.0000.0001.00 |

### VTEP Loopback VXLAN Tunnel Source Interfaces (VTEPs Only)

| VTEP Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| --------------------- | ------------------- | ------------------ | ------------------ |

### VTEP Loopback Node allocation

| POD | Node | Loopback1 |
| --- | ---- | --------- |
