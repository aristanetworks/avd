# DC1_FABRIC

# Table of Contents
<!-- toc -->

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

<!-- toc -->
# Fabric Switches and Management IP

| POD | Type | Node | Management IP | Platform | Provisioned in CloudVision |
| --- | ---- | ---- | ------------- | -------- | -------------------------- |
| DC1_FABRIC | l3leaf | DC1-BL1A | - | - | Provisioned |
| DC1_FABRIC | l3leaf | DC1-BL1B | - | - | Provisioned |
| DC1_FABRIC | l2leaf | DC1-L2LEAF1A | 192.168.200.112/24 | vEOS-LAB | Provisioned |
| DC1_FABRIC | l2leaf | DC1-L2LEAF2A | - | - | Provisioned |
| DC1_FABRIC | l2leaf | DC1-L2LEAF2B | - | - | Provisioned |
| DC1_FABRIC | l3leaf | DC1-LEAF1A | 192.168.200.105/24 | vEOS-LAB | Provisioned |
| DC1_FABRIC | l3leaf | DC1-LEAF2A | - | - | Provisioned |
| DC1_FABRIC | l3leaf | DC1-LEAF2B | - | - | Provisioned |
| DC1_FABRIC | spine | DC1-SPINE1 | 192.168.200.101/24 | vEOS-LAB | Provisioned |
| DC1_FABRIC | spine | DC1-SPINE2 | 192.168.200.102/24 | vEOS-LAB | Provisioned |
| DC1_FABRIC | spine | DC1-SPINE3 | 192.168.200.103/24 | vEOS-LAB | Provisioned |
| DC1_FABRIC | spine | DC1-SPINE4 | 192.168.200.104/24 | vEOS-LAB | Provisioned |
| DC1_FABRIC | l3leaf | DC1-SVC3A | - | - | Not Available |
| DC1_FABRIC | l3leaf | DC1-SVC3B | - | - | Not Available |

> Provision status is based on Ansible inventory declaration and do not represent real status from CloudVision.

## Fabric Switches with inband Management IP
| POD | Type | Node | Management IP | Inband Interface |
| --- | ---- | ---- | ------------- | ---------------- |

# Fabric Topology

| Type | Node | Node Interface | Peer Type | Peer Node | Peer Interface |
| ---- | ---- | -------------- | --------- | ----------| -------------- |
| l3leaf | DC1-LEAF1A | Ethernet1 | spine | DC1-SPINE1 | Ethernet1 |
| l3leaf | DC1-LEAF1A | Ethernet2 | spine | DC1-SPINE2 | Ethernet1 |
| l3leaf | DC1-LEAF1A | Ethernet3 | spine | DC1-SPINE3 | Ethernet1 |
| l3leaf | DC1-LEAF1A | Ethernet4 | spine | DC1-SPINE4 | Ethernet1 |

# Fabric IP Allocation

## Fabric Point-To-Point Links

| Uplink IPv4 Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ---------------- | ------------------- | ------------------ | ------------------ |
| 172.31.255.0/24 | 256 | 8 | 3.13 % |

## Point-To-Point Links Node Allocation

| Node | Node Interface | Node IP Address | Peer Node | Peer Interface | Peer IP Address |
| ---- | -------------- | --------------- | --------- | -------------- | --------------- |
| DC1-LEAF1A | Ethernet1 | 172.31.255.1/31 | DC1-SPINE1 | Ethernet1 | 172.31.255.0/31 |
| DC1-LEAF1A | Ethernet2 | 172.31.255.3/31 | DC1-SPINE2 | Ethernet1 | 172.31.255.2/31 |
| DC1-LEAF1A | Ethernet3 | 172.31.255.5/31 | DC1-SPINE3 | Ethernet1 | 172.31.255.4/31 |
| DC1-LEAF1A | Ethernet4 | 172.31.255.7/31 | DC1-SPINE4 | Ethernet1 | 172.31.255.6/31 |

## Loopback Interfaces (BGP EVPN Peering)

| Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ------------- | ------------------- | ------------------ | ------------------ |
| 192.168.255.0/24 | 256 | 5 | 1.96 % |

## Loopback0 Interfaces Node Allocation

| POD | Node | Loopback0 |
| --- | ---- | --------- |
| DC1_FABRIC | DC1-LEAF1A | 192.168.255.5/32 |
| DC1_FABRIC | DC1-SPINE1 | 192.168.255.1/32 |
| DC1_FABRIC | DC1-SPINE2 | 192.168.255.2/32 |
| DC1_FABRIC | DC1-SPINE3 | 192.168.255.3/32 |
| DC1_FABRIC | DC1-SPINE4 | 192.168.255.4/32 |

## VTEP Loopback VXLAN Tunnel Source Interfaces (VTEPs Only)

| VTEP Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| --------------------- | ------------------- | ------------------ | ------------------ |
| 192.168.254.0/24 | 256 | 1 | 0.4 % |

## VTEP Loopback Node allocation

| POD | Node | Loopback1 |
| --- | ---- | --------- |
| DC1_FABRIC | DC1-LEAF1A | 192.168.254.5/32 |
