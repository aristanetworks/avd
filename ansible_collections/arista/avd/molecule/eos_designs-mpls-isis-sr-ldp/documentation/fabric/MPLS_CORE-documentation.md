# MPLS_CORE

# Table of Contents

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

# Fabric Switches and Management IP

| POD | Type | Node | Management IP | Platform | Provisioned in CloudVision |
| --- | ---- | ---- | ------------- | -------- | -------------------------- |
| MPLS_CORE | pe | SITE1-LER1 | 192.168.200.105/24 | 7280SR3 | Provisioned |
| MPLS_CORE | pe | SITE1-LER2 | 192.168.200.106/24 | 7280SR3 | Provisioned |
| MPLS_CORE | p | SITE1-LSR1 | 192.168.200.101/24 | - | Provisioned |
| MPLS_CORE | p | SITE1-LSR2 | 192.168.200.102/24 | - | Provisioned |
| MPLS_CORE | rr | SITE1-RR1 | 10.30.30.108/24 | 7280SR3 | Provisioned |
| MPLS_CORE | pe | SITE2-LER1 | 192.168.200.107/24 | 7280SR3 | Provisioned |
| MPLS_CORE | p | SITE2-LSR1 | 192.168.200.103/24 | - | Provisioned |
| MPLS_CORE | p | SITE2-LSR2 | 192.168.200.104/24 | - | Provisioned |
| MPLS_CORE | rr | SITE2-RR1 | 10.30.30.109/24 | 7280SR3 | Provisioned |
| MPLS_CORE | pe | SITE3-LER1 | 192.168.200.110/24 | 7280SR3 | Provisioned |

> Provision status is based on Ansible inventory declaration and do not represent real status from CloudVision.

## Fabric Switches with inband Management IP
| POD | Type | Node | Management IP | Inband Interface |
| --- | ---- | ---- | ------------- | ---------------- |

# Fabric Topology

| Type | Node | Node Interface | Peer Type | Peer Node | Peer Interface |
| ---- | ---- | -------------- | --------- | ----------| -------------- |
| pe | SITE1-LER1 | Ethernet1 | p | SITE1-LSR1 | Ethernet1 |
| pe | SITE1-LER1 | Ethernet2 | pe | SITE1-LER2 | Ethernet2 |
| pe | SITE1-LER2 | Ethernet1 | p | SITE1-LSR2 | Ethernet1 |
| p | SITE1-LSR1 | Ethernet3 | p | SITE2-LSR1 | Ethernet3 |
| p | SITE1-LSR1 | Ethernet4 | rr | SITE1-RR1 | Ethernet4 |
| p | SITE1-LSR2 | Ethernet3 | p | SITE2-LSR2 | Ethernet3 |
| pe | SITE2-LER1 | Ethernet1 | p | SITE2-LSR1 | Ethernet1 |
| p | SITE2-LSR1 | Ethernet4 | rr | SITE2-RR1 | Ethernet4 |

# Fabric IP Allocation

## Fabric Point-To-Point Links

| Uplink IPv4 Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ---------------- | ------------------- | ------------------ | ------------------ |

## Point-To-Point Links Node Allocation

| Node | Node Interface | Node IP Address | Peer Node | Peer Interface | Peer IP Address |
| ---- | -------------- | --------------- | --------- | -------------- | --------------- |
| SITE1-LER1 | Ethernet1 | 100.64.48.0/31 | SITE1-LSR1 | Ethernet1 | 100.64.48.1/31 |
| SITE1-LER1 | Ethernet2 | 100.64.48.4/31 | SITE1-LER2 | Ethernet2 | 100.64.48.5/31 |
| SITE1-LER2 | Ethernet1 | 100.64.48.2/31 | SITE1-LSR2 | Ethernet1 | 100.64.48.3/31 |
| SITE1-LSR1 | Ethernet3 | 100.64.48.8/31 | SITE2-LSR1 | Ethernet3 | 100.64.48.9/31 |
| SITE1-LSR1 | Ethernet4 | 100.64.48.6/31 | SITE1-RR1 | Ethernet4 | 100.64.48.7/31 |
| SITE1-LSR2 | Ethernet3 | 100.64.48.10/31 | SITE2-LSR2 | Ethernet3 | 100.64.48.11/31 |
| SITE2-LER1 | Ethernet1 | 100.64.48.15/31 | SITE2-LSR1 | Ethernet1 | 100.64.48.14/31 |
| SITE2-LSR1 | Ethernet4 | 100.64.48.12/31 | SITE2-RR1 | Ethernet4 | 100.64.48.13/31 |

## Loopback Interfaces (BGP EVPN Peering)

| Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ------------- | ------------------- | ------------------ | ------------------ |
| 100.70.0.0/24 | 256 | 10 | 3.91 % |

## Loopback0 Interfaces Node Allocation

| POD | Node | Loopback0 |
| --- | ---- | --------- |
| MPLS_CORE | SITE1-LER1 | 100.70.0.5/32 |
| MPLS_CORE | SITE1-LER2 | 100.70.0.6/32 |
| MPLS_CORE | SITE1-LSR1 | 100.70.0.1/32 |
| MPLS_CORE | SITE1-LSR2 | 100.70.0.2/32 |
| MPLS_CORE | SITE1-RR1 | 100.70.0.8/32 |
| MPLS_CORE | SITE2-LER1 | 100.70.0.7/32 |
| MPLS_CORE | SITE2-LSR1 | 100.70.0.3/32 |
| MPLS_CORE | SITE2-LSR2 | 100.70.0.4/32 |
| MPLS_CORE | SITE2-RR1 | 100.70.0.9/32 |
| MPLS_CORE | SITE3-LER1 | 100.70.0.10/32 |

## ISIS CLNS interfaces

| POD | Node | CLNS Address |
| --- | ---- | ------------ |
| MPLS_CORE | SITE1-LER1 | 49.0001.0000.0001.0005.00 |
| MPLS_CORE | SITE1-LER2 | 49.0001.0000.0001.0006.00 |
| MPLS_CORE | SITE1-LSR1 | 49.0001.0000.0000.0001.00 |
| MPLS_CORE | SITE1-LSR2 | 49.0001.0000.0000.0002.00 |
| MPLS_CORE | SITE1-RR1 | 49.0001.0000.0002.0008.00 |
| MPLS_CORE | SITE2-LER1 | 49.0001.0000.0001.0007.00 |
| MPLS_CORE | SITE2-LSR1 | 49.0001.0000.0000.0003.00 |
| MPLS_CORE | SITE2-LSR2 | 49.0001.0000.0000.0004.00 |
| MPLS_CORE | SITE2-RR1 | 49.0001.0000.0002.0009.00 |
| MPLS_CORE | SITE3-LER1 | 49.0001.0000.0001.0010.00 |

## VTEP Loopback VXLAN Tunnel Source Interfaces (VTEPs Only)

| VTEP Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| --------------------- | ------------------- | ------------------ | ------------------ |

## VTEP Loopback Node allocation

| POD | Node | Loopback1 |
| --- | ---- | --------- |
