# FABRIC

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
| FABRIC | leaf | amber-leaf1 | 10.252.0.22/24 | 7280R2 | Provisioned |
| FABRIC | leaf | amber-leaf2 | 10.252.0.23/24 | 7020R | Provisioned |
| FABRIC | spine | amber-spine1 | 10.252.0.21/24 | 7280R3 | Provisioned |
| FABRIC | leaf | blue-leaf1 | 10.252.0.25/24 | 7280R2 | Provisioned |
| FABRIC | leaf | blue-leaf2 | 10.252.0.26/24 | 7020R | Provisioned |
| FABRIC | spine | blue-spine1 | 10.252.0.24/24 | 7280R3 | Provisioned |

> Provision status is based on Ansible inventory declaration and do not represent real status from CloudVision.

## Fabric Switches with inband Management IP
| POD | Type | Node | Management IP | Inband Interface |
| --- | ---- | ---- | ------------- | ---------------- |

# Fabric Topology

| Type | Node | Node Interface | Peer Type | Peer Node | Peer Interface |
| ---- | ---- | -------------- | --------- | ----------| -------------- |
| leaf | amber-leaf1 | Ethernet49/1 | spine | amber-spine1 | Ethernet1/1 |
| leaf | amber-leaf1 | Ethernet50/1 | spine | amber-spine1 | Ethernet2/1 |
| leaf | amber-leaf2 | Ethernet49 | spine | amber-spine1 | Ethernet3/1 |
| leaf | amber-leaf2 | Ethernet50 | spine | amber-spine1 | Ethernet3/2 |
| leaf | amber-leaf2 | Ethernet51 | spine | amber-spine1 | Ethernet3/3 |
| leaf | amber-leaf2 | Ethernet52 | spine | amber-spine1 | Ethernet3/4 |
| leaf | blue-leaf1 | Ethernet49/1 | spine | blue-spine1 | Ethernet1/1 |
| leaf | blue-leaf1 | Ethernet50/1 | spine | blue-spine1 | Ethernet2/1 |
| leaf | blue-leaf2 | Ethernet49 | spine | blue-spine1 | Ethernet3/1 |
| leaf | blue-leaf2 | Ethernet50 | spine | blue-spine1 | Ethernet3/2 |
| leaf | blue-leaf2 | Ethernet51 | spine | blue-spine1 | Ethernet3/3 |
| leaf | blue-leaf2 | Ethernet52 | spine | blue-spine1 | Ethernet3/4 |

# Fabric IP Allocation

## Fabric Point-To-Point Links

| Uplink IPv4 Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ---------------- | ------------------- | ------------------ | ------------------ |
| 10.252.11.0/24 | 256 | 12 | 4.69 % |
| 10.252.15.0/24 | 256 | 12 | 4.69 % |

## Point-To-Point Links Node Allocation

| Node | Node Interface | Node IP Address | Peer Node | Peer Interface | Peer IP Address |
| ---- | -------------- | --------------- | --------- | -------------- | --------------- |
| amber-leaf1 | Ethernet49/1 | 10.252.11.1/31 | amber-spine1 | Ethernet1/1 | 10.252.11.0/31 |
| amber-leaf1 | Ethernet50/1 | 10.252.11.3/31 | amber-spine1 | Ethernet2/1 | 10.252.11.2/31 |
| amber-leaf2 | Ethernet49 | 10.252.11.9/31 | amber-spine1 | Ethernet3/1 | 10.252.11.8/31 |
| amber-leaf2 | Ethernet50 | 10.252.11.11/31 | amber-spine1 | Ethernet3/2 | 10.252.11.10/31 |
| amber-leaf2 | Ethernet51 | 10.252.11.13/31 | amber-spine1 | Ethernet3/3 | 10.252.11.12/31 |
| amber-leaf2 | Ethernet52 | 10.252.11.15/31 | amber-spine1 | Ethernet3/4 | 10.252.11.14/31 |
| blue-leaf1 | Ethernet49/1 | 10.252.15.1/31 | blue-spine1 | Ethernet1/1 | 10.252.15.0/31 |
| blue-leaf1 | Ethernet50/1 | 10.252.15.3/31 | blue-spine1 | Ethernet2/1 | 10.252.15.2/31 |
| blue-leaf2 | Ethernet49 | 10.252.15.9/31 | blue-spine1 | Ethernet3/1 | 10.252.15.8/31 |
| blue-leaf2 | Ethernet50 | 10.252.15.11/31 | blue-spine1 | Ethernet3/2 | 10.252.15.10/31 |
| blue-leaf2 | Ethernet51 | 10.252.15.13/31 | blue-spine1 | Ethernet3/3 | 10.252.15.12/31 |
| blue-leaf2 | Ethernet52 | 10.252.15.15/31 | blue-spine1 | Ethernet3/4 | 10.252.15.14/31 |

## Loopback Interfaces (BGP EVPN Peering)

| Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ------------- | ------------------- | ------------------ | ------------------ |
| 10.252.8.0/26 | 64 | 3 | 4.69 % |
| 10.252.12.0/26 | 64 | 3 | 4.69 % |

## Loopback0 Interfaces Node Allocation

| POD | Node | Loopback0 |
| --- | ---- | --------- |
| FABRIC | amber-leaf1 | 10.252.8.3/32 |
| FABRIC | amber-leaf2 | 10.252.8.4/32 |
| FABRIC | amber-spine1 | 10.252.8.1/32 |
| FABRIC | blue-leaf1 | 10.252.12.3/32 |
| FABRIC | blue-leaf2 | 10.252.12.4/32 |
| FABRIC | blue-spine1 | 10.252.12.1/32 |

## VTEP Loopback VXLAN Tunnel Source Interfaces (VTEPs Only)

| VTEP Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| --------------------- | ------------------- | ------------------ | ------------------ |

## VTEP Loopback Node allocation

| POD | Node | Loopback1 |
| --- | ---- | --------- |
