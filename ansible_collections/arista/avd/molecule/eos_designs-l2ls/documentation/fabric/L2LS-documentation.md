# L2LS

# Table of Contents

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

# Fabric Switches and Management IP

| POD | Type | Node | Management IP | Platform | Provisioned in CloudVision |
| --- | ---- | ---- | ------------- | -------- | -------------------------- |
| L2LS_OSPF | leaf | OSPF-LEAF1 | - | - | Provisioned |
| L2LS_OSPF | leaf | OSPF-LEAF2 | - | - | Provisioned |
| L2LS_OSPF | spine | OSPF-SPINE1 | - | - | Provisioned |
| L2LS_OSPF | spine | OSPF-SPINE2 | - | - | Provisioned |

> Provision status is based on Ansible inventory declaration and do not represent real status from CloudVision.

## Fabric Switches with inband Management IP
| POD | Type | Node | Management IP | Inband Interface |
| --- | ---- | ---- | ------------- | ---------------- |

# Fabric Topology

| Type | Node | Node Interface | Peer Type | Peer Node | Peer Interface |
| ---- | ---- | -------------- | --------- | ----------| -------------- |
| leaf | OSPF-LEAF1 | Ethernet1 | spine | OSPF-SPINE1 | Ethernet1 |
| leaf | OSPF-LEAF1 | Ethernet2 | spine | OSPF-SPINE2 | Ethernet1 |
| leaf | OSPF-LEAF2 | Ethernet1 | spine | OSPF-SPINE1 | Ethernet2 |
| leaf | OSPF-LEAF2 | Ethernet2 | spine | OSPF-SPINE2 | Ethernet2 |
| spine | OSPF-SPINE1 | Ethernet3 | mlag_peer | OSPF-SPINE2 | Ethernet3 |
| spine | OSPF-SPINE1 | Ethernet4 | mlag_peer | OSPF-SPINE2 | Ethernet4 |

# Fabric IP Allocation

## Fabric Point-To-Point Links

| Uplink IPv4 Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ---------------- | ------------------- | ------------------ | ------------------ |

## Point-To-Point Links Node Allocation

| Node | Node Interface | Node IP Address | Peer Node | Peer Interface | Peer IP Address |
| ---- | -------------- | --------------- | --------- | -------------- | --------------- |

## Loopback Interfaces (BGP EVPN Peering)

| Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ------------- | ------------------- | ------------------ | ------------------ |
| 192.168.255.0/24 | 256 | 2 | 0.79 % |

## Loopback0 Interfaces Node Allocation

| POD | Node | Loopback0 |
| --- | ---- | --------- |
| L2LS_OSPF | OSPF-SPINE1 | 192.168.255.1/32 |
| L2LS_OSPF | OSPF-SPINE2 | 192.168.255.2/32 |

## VTEP Loopback VXLAN Tunnel Source Interfaces (VTEPs Only)

| VTEP Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| --------------------- | ------------------- | ------------------ | ------------------ |

## VTEP Loopback Node allocation

| POD | Node | Loopback1 |
| --- | ---- | --------- |
