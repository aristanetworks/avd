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
| FABRIC | media_leaf | amber-leaf1 | 10.90.227.25/24 | 7280R2 | Provisioned | - |
| FABRIC | media_leaf | amber-leaf2 | 10.90.227.27/24 | 7280R2 | Provisioned | - |
| FABRIC | media_spine | amber-spine1 | 10.90.227.11/24 | 7280R2 | Provisioned | - |
| FABRIC | media_leaf | blue-leaf1 | 10.90.227.29/24 | 7050X3 | Provisioned | - |
| FABRIC | media_leaf | blue-leaf2 | 10.90.227.31/24 | 720XP | Provisioned | - |
| FABRIC | media_spine | blue-spine1 | 10.90.227.12/24 | 7050X3 | Provisioned | - |
| FABRIC | ptp_leaf | media-PTP-1 | 10.90.227.21/24 | 7020TR | Provisioned | - |
| FABRIC | ptp_leaf | media-PTP-2 | 10.90.227.23/24 | 7020TR | Provisioned | - |

> Provision status is based on Ansible inventory declaration and do not represent real status from CloudVision.

### Fabric Switches with inband Management IP

| POD | Type | Node | Management IP | Inband Interface |
| --- | ---- | ---- | ------------- | ---------------- |

## Fabric Topology

| Type | Node | Node Interface | Peer Type | Peer Node | Peer Interface |
| ---- | ---- | -------------- | --------- | ----------| -------------- |
| media_leaf | amber-leaf1 | Ethernet49/1 | media_spine | amber-spine1 | Ethernet1/1 |
| media_leaf | amber-leaf2 | Ethernet49/1 | media_spine | amber-spine1 | Ethernet3/1 |
| media_spine | amber-spine1 | Ethernet27/1 | ptp_leaf | media-PTP-1 | Ethernet51 |
| media_spine | amber-spine1 | Ethernet28/1 | ptp_leaf | media-PTP-2 | Ethernet51 |
| media_leaf | blue-leaf1 | Ethernet51/1 | media_spine | blue-spine1 | Ethernet17/1 |
| media_leaf | blue-leaf2 | Ethernet54/1 | media_spine | blue-spine1 | Ethernet25/1 |
| media_spine | blue-spine1 | Ethernet27/1 | ptp_leaf | media-PTP-1 | Ethernet52 |
| media_spine | blue-spine1 | Ethernet28/1 | ptp_leaf | media-PTP-2 | Ethernet52 |
| ptp_leaf | media-PTP-1 | Ethernet1 | ptp_leaf | media-PTP-2 | Ethernet1 |
| ptp_leaf | media-PTP-1 | Ethernet2 | ptp_leaf | media-PTP-2 | Ethernet2 |

## Fabric IP Allocation

### Fabric Point-To-Point Links

| Uplink IPv4 Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ---------------- | ------------------- | ------------------ | ------------------ |
| 10.255.253.0/26 | 64 | 8 | 12.5 % |
| 10.255.254.0/26 | 64 | 4 | 6.25 % |
| 10.255.255.0/26 | 64 | 4 | 6.25 % |

### Point-To-Point Links Node Allocation

| Node | Node Interface | Node IP Address | Peer Node | Peer Interface | Peer IP Address |
| ---- | -------------- | --------------- | --------- | -------------- | --------------- |
| amber-leaf1 | Ethernet49/1 | 10.255.254.1/31 | amber-spine1 | Ethernet1/1 | 10.255.254.0/31 |
| amber-leaf2 | Ethernet49/1 | 10.255.254.3/31 | amber-spine1 | Ethernet3/1 | 10.255.254.2/31 |
| amber-spine1 | Ethernet27/1 | 10.255.253.0/31 | media-PTP-1 | Ethernet51 | 10.255.253.1/31 |
| amber-spine1 | Ethernet28/1 | 10.255.253.4/31 | media-PTP-2 | Ethernet51 | 10.255.253.5/31 |
| blue-leaf1 | Ethernet51/1 | 10.255.255.1/31 | blue-spine1 | Ethernet17/1 | 10.255.255.0/31 |
| blue-leaf2 | Ethernet54/1 | 10.255.255.3/31 | blue-spine1 | Ethernet25/1 | 10.255.255.2/31 |
| blue-spine1 | Ethernet27/1 | 10.255.253.2/31 | media-PTP-1 | Ethernet52 | 10.255.253.3/31 |
| blue-spine1 | Ethernet28/1 | 10.255.253.6/31 | media-PTP-2 | Ethernet52 | 10.255.253.7/31 |

### Loopback Interfaces (BGP EVPN Peering)

| Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ------------- | ------------------- | ------------------ | ------------------ |
| 10.255.1.0/27 | 32 | 3 | 9.38 % |
| 10.255.2.0/27 | 32 | 3 | 9.38 % |
| 10.255.3.0/27 | 32 | 2 | 6.25 % |

### Loopback0 Interfaces Node Allocation

| POD | Node | Loopback0 |
| --- | ---- | --------- |
| FABRIC | amber-leaf1 | 10.255.1.3/32 |
| FABRIC | amber-leaf2 | 10.255.1.4/32 |
| FABRIC | amber-spine1 | 10.255.1.1/32 |
| FABRIC | blue-leaf1 | 10.255.2.3/32 |
| FABRIC | blue-leaf2 | 10.255.2.4/32 |
| FABRIC | blue-spine1 | 10.255.2.1/32 |
| FABRIC | media-PTP-1 | 10.255.3.1/32 |
| FABRIC | media-PTP-2 | 10.255.3.2/32 |

### VTEP Loopback VXLAN Tunnel Source Interfaces (VTEPs Only)

| VTEP Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| --------------------- | ------------------- | ------------------ | ------------------ |

### VTEP Loopback Node allocation

| POD | Node | Loopback1 |
| --- | ---- | --------- |
