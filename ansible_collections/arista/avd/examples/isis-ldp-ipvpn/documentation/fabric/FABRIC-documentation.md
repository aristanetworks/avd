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
  - [ISIS CLNS interfaces](#isis-clns-interfaces)
  - [VTEP Loopback VXLAN Tunnel Source Interfaces (VTEPs Only)](#vtep-loopback-vxlan-tunnel-source-interfaces-vteps-only)
  - [VTEP Loopback Node allocation](#vtep-loopback-node-allocation)

## Fabric Switches and Management IP

| POD | Type | Node | Management IP | Platform | Provisioned in CloudVision | Serial Number |
| --- | ---- | ---- | ------------- | -------- | -------------------------- | ------------- |
| FABRIC | p | p1 | 172.16.1.11/24 | vEOS-lab | Provisioned | - |
| FABRIC | p | p2 | 172.16.1.12/24 | vEOS-lab | Provisioned | - |
| FABRIC | p | p3 | 172.16.1.13/24 | vEOS-lab | Provisioned | - |
| FABRIC | p | p4 | 172.16.1.14/24 | vEOS-lab | Provisioned | - |
| FABRIC | pe | pe1 | 172.16.1.101/24 | vEOS-lab | Provisioned | - |
| FABRIC | pe | pe2 | 172.16.1.102/24 | vEOS-lab | Provisioned | - |
| FABRIC | pe | pe3 | 172.16.1.103/24 | vEOS-lab | Provisioned | - |
| FABRIC | rr | rr1 | 172.16.1.151/24 | vEOS-lab | Provisioned | - |
| FABRIC | rr | rr2 | 172.16.1.152/24 | vEOS-lab | Provisioned | - |

> Provision status is based on Ansible inventory declaration and do not represent real status from CloudVision.

### Fabric Switches with inband Management IP

| POD | Type | Node | Management IP | Inband Interface |
| --- | ---- | ---- | ------------- | ---------------- |

## Fabric Topology

| Type | Node | Node Interface | Peer Type | Peer Node | Peer Interface |
| ---- | ---- | -------------- | --------- | ----------| -------------- |
| p | p1 | Ethernet1 | pe | pe1 | Ethernet1 |
| p | p1 | Ethernet2 | pe | pe2 | Ethernet2 |
| p | p1 | Ethernet3 | rr | rr1 | Ethernet3 |
| p | p1 | Ethernet4 | p | p2 | Ethernet4 |
| p | p2 | Ethernet1 | pe | pe2 | Ethernet1 |
| p | p2 | Ethernet2 | pe | pe1 | Ethernet2 |
| p | p2 | Ethernet3 | rr | rr2 | Ethernet3 |
| p | p3 | Ethernet1 | pe | pe3 | Ethernet1 |
| p | p3 | Ethernet2 | rr | rr1 | Ethernet2 |
| p | p3 | Ethernet4 | p | p4 | Ethernet4 |
| p | p4 | Ethernet2 | rr | rr2 | Ethernet2 |
| p | p4 | Ethernet3 | pe | pe3 | Ethernet3 |
| rr | rr1 | Ethernet4 | rr | rr2 | Ethernet4 |

## Fabric IP Allocation

### Fabric Point-To-Point Links

| Uplink IPv4 Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ---------------- | ------------------- | ------------------ | ------------------ |

### Point-To-Point Links Node Allocation

| Node | Node Interface | Node IP Address | Peer Node | Peer Interface | Peer IP Address |
| ---- | -------------- | --------------- | --------- | -------------- | --------------- |
| p1 | Ethernet1 | 10.255.3.1/31 | pe1 | Ethernet1 | 10.255.3.0/31 |
| p1 | Ethernet2 | 10.255.3.7/31 | pe2 | Ethernet2 | 10.255.3.6/31 |
| p1 | Ethernet3 | 10.255.3.11/31 | rr1 | Ethernet3 | 10.255.3.10/31 |
| p1 | Ethernet4 | 10.255.3.8/31 | p2 | Ethernet4 | 10.255.3.9/31 |
| p2 | Ethernet1 | 10.255.3.5/31 | pe2 | Ethernet1 | 10.255.3.4/31 |
| p2 | Ethernet2 | 10.255.3.3/31 | pe1 | Ethernet2 | 10.255.3.2/31 |
| p2 | Ethernet3 | 10.255.3.17/31 | rr2 | Ethernet3 | 10.255.3.16/31 |
| p3 | Ethernet1 | 10.255.3.23/31 | pe3 | Ethernet1 | 10.255.3.22/31 |
| p3 | Ethernet2 | 10.255.3.13/31 | rr1 | Ethernet2 | 10.255.3.12/31 |
| p3 | Ethernet4 | 10.255.3.20/31 | p4 | Ethernet4 | 10.255.3.21/31 |
| p4 | Ethernet2 | 10.255.3.19/31 | rr2 | Ethernet2 | 10.255.3.18/31 |
| p4 | Ethernet3 | 10.255.3.25/31 | pe3 | Ethernet3 | 10.255.3.24/31 |
| rr1 | Ethernet4 | 10.255.3.14/31 | rr2 | Ethernet4 | 10.255.3.15/31 |

### Loopback Interfaces (BGP EVPN Peering)

| Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ------------- | ------------------- | ------------------ | ------------------ |
| 10.255.0.0/27 | 32 | 4 | 12.5 % |
| 10.255.1.0/27 | 32 | 3 | 9.38 % |
| 10.255.2.0/27 | 32 | 2 | 6.25 % |

### Loopback0 Interfaces Node Allocation

| POD | Node | Loopback0 |
| --- | ---- | --------- |
| FABRIC | p1 | 10.255.0.1/32 |
| FABRIC | p2 | 10.255.0.2/32 |
| FABRIC | p3 | 10.255.0.3/32 |
| FABRIC | p4 | 10.255.0.4/32 |
| FABRIC | pe1 | 10.255.1.1/32 |
| FABRIC | pe2 | 10.255.1.2/32 |
| FABRIC | pe3 | 10.255.1.3/32 |
| FABRIC | rr1 | 10.255.2.1/32 |
| FABRIC | rr2 | 10.255.2.2/32 |

### ISIS CLNS interfaces

| POD | Node | CLNS Address |
| --- | ---- | ------------ |
| FABRIC | p1 | 49.0001.0000.0000.0001.00 |
| FABRIC | p2 | 49.0001.0000.0000.0002.00 |
| FABRIC | p3 | 49.0001.0000.0000.0003.00 |
| FABRIC | p4 | 49.0001.0000.0000.0004.00 |
| FABRIC | pe1 | 49.0001.0000.0001.0001.00 |
| FABRIC | pe2 | 49.0001.0000.0001.0002.00 |
| FABRIC | pe3 | 49.0001.0000.0001.0003.00 |
| FABRIC | rr1 | 49.0001.0000.0002.0001.00 |
| FABRIC | rr2 | 49.0001.0000.0002.0002.00 |

### VTEP Loopback VXLAN Tunnel Source Interfaces (VTEPs Only)

| VTEP Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| --------------------- | ------------------- | ------------------ | ------------------ |

### VTEP Loopback Node allocation

| POD | Node | Loopback1 |
| --- | ---- | --------- |
