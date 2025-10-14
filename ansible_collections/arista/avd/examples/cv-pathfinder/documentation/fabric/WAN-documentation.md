# WAN

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
| WAN | spine | inet-cloud | 192.168.17.31/24 | vEOS-lab | Provisioned | - |
| WAN | spine | mpls-cloud | 192.168.17.30/24 | vEOS-lab | Provisioned | - |
| WAN | wan_rr | pf1 | 192.168.17.10/24 | CloudEOS | Provisioned | - |
| WAN | wan_rr | pf2 | 192.168.17.11/24 | CloudEOS | Provisioned | - |
| WAN | l3leaf | site1-border1 | 192.168.17.14/24 | vEOS-lab | Provisioned | - |
| WAN | l3leaf | site1-border2 | 192.168.17.15/24 | vEOS-lab | Provisioned | - |
| WAN | wan_router | site1-wan1 | 192.168.17.12/24 | CloudEOS | Provisioned | - |
| WAN | wan_router | site1-wan2 | 192.168.17.13/24 | CloudEOS | Provisioned | - |
| WAN | l3leaf | site2-leaf1 | 192.168.17.18/24 | vEOS-lab | Provisioned | - |
| WAN | l3leaf | site2-leaf2 | 192.168.17.19/24 | vEOS-lab | Provisioned | - |
| WAN | wan_router | site2-wan1 | 192.168.17.16/24 | CloudEOS | Provisioned | - |
| WAN | wan_router | site2-wan2 | 192.168.17.17/24 | CloudEOS | Provisioned | - |
| WAN | l2leaf | site3-leaf1 | 192.168.17.21/24 | vEOS-lab | Provisioned | - |
| WAN | wan_router | site3-wan1 | 192.168.17.20/24 | CloudEOS | Provisioned | - |
| WAN | l3leaf | site4-border1 | 192.168.17.23/24 | vEOS-lab | Provisioned | - |
| WAN | l3leaf | site4-border2 | 192.168.17.24/24 | vEOS-lab | Provisioned | - |
| WAN | wan_router | site4-wan1 | 192.168.17.22/24 | CloudEOS | Provisioned | - |

> Provision status is based on Ansible inventory declaration and do not represent real status from CloudVision.

### Fabric Switches with inband Management IP

| POD | Type | Node | Management IP | Inband Interface |
| --- | ---- | ---- | ------------- | ---------------- |

## Fabric Topology

| Type | Node | Node Interface | Peer Type | Peer Node | Peer Interface |
| ---- | ---- | -------------- | --------- | ----------| -------------- |

## Fabric IP Allocation

### Fabric Point-To-Point Links

| Uplink IPv4 Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ---------------- | ------------------- | ------------------ | ------------------ |
| 10.0.1.0/24 | 256 | 0 | 0.0 % |
| 10.0.2.0/24 | 256 | 0 | 0.0 % |
| 10.0.3.0/24 | 256 | 0 | 0.0 % |
| 10.0.4.0/24 | 256 | 0 | 0.0 % |

### Point-To-Point Links Node Allocation

| Node | Node Interface | Node IP Address | Peer Node | Peer Interface | Peer IP Address |
| ---- | -------------- | --------------- | --------- | -------------- | --------------- |

### Loopback Interfaces (BGP EVPN Peering)

| Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ------------- | ------------------- | ------------------ | ------------------ |
| 172.31.255.0/24 | 256 | 2 | 0.79 % |
| 192.168.255.0/24 | 256 | 14 | 5.47 % |

### Loopback0 Interfaces Node Allocation

| POD | Node | Loopback0 |
| --- | ---- | --------- |
| WAN | inet-cloud | 172.31.255.23/32 |
| WAN | mpls-cloud | 172.31.255.22/32 |
| WAN | pf1 | 192.168.255.1/32 |
| WAN | pf2 | 192.168.255.2/32 |
| WAN | site1-border1 | 192.168.255.5/32 |
| WAN | site1-border2 | 192.168.255.6/32 |
| WAN | site1-wan1 | 192.168.255.3/32 |
| WAN | site1-wan2 | 192.168.255.4/32 |
| WAN | site2-leaf1 | 192.168.255.9/32 |
| WAN | site2-leaf2 | 192.168.255.10/32 |
| WAN | site2-wan1 | 192.168.255.7/32 |
| WAN | site2-wan2 | 192.168.255.8/32 |
| WAN | site3-wan1 | 192.168.255.11/32 |
| WAN | site4-border1 | 192.168.255.13/32 |
| WAN | site4-border2 | 192.168.255.14/32 |
| WAN | site4-wan1 | 192.168.255.15/32 |

### VTEP Loopback VXLAN Tunnel Source Interfaces (VTEPs Only)

| VTEP Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ------------------ | ------------------- | ------------------ | ------------------ |
| 192.168.42.0/24 | 256 | 6 | 2.35 % |

### VTEP Loopback Node allocation

| POD | Node | Loopback1 |
| --- | ---- | --------- |
| WAN | site1-border1 | 192.168.42.5/32 |
| WAN | site1-border2 | 192.168.42.5/32 |
| WAN | site2-leaf1 | 192.168.42.9/32 |
| WAN | site2-leaf2 | 192.168.42.9/32 |
| WAN | site4-border1 | 192.168.42.13/32 |
| WAN | site4-border2 | 192.168.42.13/32 |
