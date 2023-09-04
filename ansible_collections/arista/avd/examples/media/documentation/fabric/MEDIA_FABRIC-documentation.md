# MEDIA_FABRIC

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
| MEDIA_FABRIC | media_leaf | amber-leaf1 | 172.16.1.111/24 | vEOS-lab | Provisioned | - |
| MEDIA_FABRIC | media_leaf | amber-leaf2 | 172.16.1.112/24 | vEOS-lab | Provisioned | - |
| MEDIA_FABRIC | media_spine | amber-spine1 | 172.16.1.11/24 | vEOS-lab | Provisioned | - |
| MEDIA_FABRIC | media_leaf | blue-leaf1 | 172.16.1.211/24 | vEOS-lab | Provisioned | - |
| MEDIA_FABRIC | media_leaf | blue-leaf2 | 172.16.1.212/24 | vEOS-lab | Provisioned | - |
| MEDIA_FABRIC | media_spine | blue-spine1 | 172.16.1.21/24 | vEOS-lab | Provisioned | - |
| MEDIA_FABRIC | ptp_leaf | media-PTP-1 | 172.16.3.101/24 | vEOS-lab | Provisioned | - |
| MEDIA_FABRIC | ptp_leaf | media-PTP-2 | 172.16.3.102/24 | vEOS-lab | Provisioned | - |

> Provision status is based on Ansible inventory declaration and do not represent real status from CloudVision.

### Fabric Switches with inband Management IP

| POD | Type | Node | Management IP | Inband Interface |
| --- | ---- | ---- | ------------- | ---------------- |

## Fabric Topology

| Type | Node | Node Interface | Peer Type | Peer Node | Peer Interface |
| ---- | ---- | -------------- | --------- | ----------| -------------- |
| media_leaf | amber-leaf1 | Ethernet1 | media_spine | amber-spine1 | Ethernet1 |
| media_leaf | amber-leaf1 | Ethernet2 | media_spine | amber-spine1 | Ethernet2 |
| media_leaf | amber-leaf2 | Ethernet1 | media_spine | amber-spine1 | Ethernet3 |
| media_leaf | amber-leaf2 | Ethernet2 | media_spine | amber-spine1 | Ethernet4 |
| media_spine | amber-spine1 | Ethernet5 | ptp_leaf | media-PTP-1 | Ethernet1 |
| media_spine | amber-spine1 | Ethernet6 | ptp_leaf | media-PTP-2 | Ethernet1 |
| media_leaf | blue-leaf1 | Ethernet1 | media_spine | blue-spine1 | Ethernet1 |
| media_leaf | blue-leaf1 | Ethernet2 | media_spine | blue-spine1 | Ethernet2 |
| media_leaf | blue-leaf2 | Ethernet1 | media_spine | blue-spine1 | Ethernet3 |
| media_leaf | blue-leaf2 | Ethernet2 | media_spine | blue-spine1 | Ethernet4 |
| media_spine | blue-spine1 | Ethernet5 | ptp_leaf | media-PTP-1 | Ethernet2 |
| media_spine | blue-spine1 | Ethernet6 | ptp_leaf | media-PTP-2 | Ethernet2 |
| ptp_leaf | media-PTP-1 | Ethernet3 | ptp_leaf | media-PTP-2 | Ethernet3 |
| ptp_leaf | media-PTP-1 | Ethernet4 | ptp_leaf | media-PTP-2 | Ethernet4 |

## Fabric IP Allocation

### Fabric Point-To-Point Links

| Uplink IPv4 Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ---------------- | ------------------- | ------------------ | ------------------ |
| 10.255.253.0/26 | 64 | 8 | 12.5 % |
| 10.255.254.0/26 | 64 | 8 | 12.5 % |
| 10.255.255.0/26 | 64 | 8 | 12.5 % |

### Point-To-Point Links Node Allocation

| Node | Node Interface | Node IP Address | Peer Node | Peer Interface | Peer IP Address |
| ---- | -------------- | --------------- | --------- | -------------- | --------------- |
| amber-leaf1 | Ethernet1 | 10.255.254.1/31 | amber-spine1 | Ethernet1 | 10.255.254.0/31 |
| amber-leaf1 | Ethernet2 | 10.255.254.3/31 | amber-spine1 | Ethernet2 | 10.255.254.2/31 |
| amber-leaf2 | Ethernet1 | 10.255.254.9/31 | amber-spine1 | Ethernet3 | 10.255.254.8/31 |
| amber-leaf2 | Ethernet2 | 10.255.254.11/31 | amber-spine1 | Ethernet4 | 10.255.254.10/31 |
| amber-spine1 | Ethernet5 | 10.255.253.0/31 | media-PTP-1 | Ethernet1 | 10.255.253.1/31 |
| amber-spine1 | Ethernet6 | 10.255.253.4/31 | media-PTP-2 | Ethernet1 | 10.255.253.5/31 |
| blue-leaf1 | Ethernet1 | 10.255.255.1/31 | blue-spine1 | Ethernet1 | 10.255.255.0/31 |
| blue-leaf1 | Ethernet2 | 10.255.255.3/31 | blue-spine1 | Ethernet2 | 10.255.255.2/31 |
| blue-leaf2 | Ethernet1 | 10.255.255.9/31 | blue-spine1 | Ethernet3 | 10.255.255.8/31 |
| blue-leaf2 | Ethernet2 | 10.255.255.11/31 | blue-spine1 | Ethernet4 | 10.255.255.10/31 |
| blue-spine1 | Ethernet5 | 10.255.253.2/31 | media-PTP-1 | Ethernet2 | 10.255.253.3/31 |
| blue-spine1 | Ethernet6 | 10.255.253.6/31 | media-PTP-2 | Ethernet2 | 10.255.253.7/31 |

### Loopback Interfaces (BGP EVPN Peering)

| Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ------------- | ------------------- | ------------------ | ------------------ |
| 10.255.1.0/27 | 32 | 3 | 9.38 % |
| 10.255.2.0/27 | 32 | 3 | 9.38 % |
| 10.255.3.0/27 | 32 | 2 | 6.25 % |

### Loopback0 Interfaces Node Allocation

| POD | Node | Loopback0 |
| --- | ---- | --------- |
| MEDIA_FABRIC | amber-leaf1 | 10.255.1.2/32 |
| MEDIA_FABRIC | amber-leaf2 | 10.255.1.3/32 |
| MEDIA_FABRIC | amber-spine1 | 10.255.1.1/32 |
| MEDIA_FABRIC | blue-leaf1 | 10.255.2.2/32 |
| MEDIA_FABRIC | blue-leaf2 | 10.255.2.3/32 |
| MEDIA_FABRIC | blue-spine1 | 10.255.2.1/32 |
| MEDIA_FABRIC | media-PTP-1 | 10.255.3.1/32 |
| MEDIA_FABRIC | media-PTP-2 | 10.255.3.2/32 |

### VTEP Loopback VXLAN Tunnel Source Interfaces (VTEPs Only)

| VTEP Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| --------------------- | ------------------- | ------------------ | ------------------ |

### VTEP Loopback Node allocation

| POD | Node | Loopback1 |
| --- | ---- | --------- |
