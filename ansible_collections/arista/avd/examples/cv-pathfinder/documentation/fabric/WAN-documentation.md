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
| WAN | l3leaf | border1-site1 | 192.168.17.14/24 | - | Provisioned | - |
| WAN | l3leaf | border2-site1 | 192.168.17.15/24 | - | Provisioned | - |
| WAN | spine | inet-cloud | 192.168.17.31/24 | - | Provisioned | - |
| WAN | l3leaf | leaf1-site2 | 192.168.17.18/24 | - | Provisioned | - |
| WAN | l2leaf | leaf1-site3 | 192.168.17.21/24 | - | Provisioned | - |
| WAN | l3leaf | leaf2-site2 | 192.168.17.19/24 | - | Provisioned | - |
| WAN | spine | mpls-cloud | 192.168.17.30/24 | - | Provisioned | - |
| WAN | wan_rr | pf1 | 192.168.17.10/24 | - | Provisioned | - |
| WAN | wan_rr | pf2 | 192.168.17.11/24 | - | Provisioned | - |
| WAN | wan_router | wan1-site1 | 192.168.17.12/24 | - | Provisioned | - |
| WAN | wan_router | wan1-site2 | 192.168.17.16/24 | - | Provisioned | - |
| WAN | wan_router | wan1-site3 | 192.168.17.20/24 | - | Provisioned | - |
| WAN | wan_router | wan2-site1 | 192.168.17.13/24 | - | Provisioned | - |
| WAN | wan_router | wan2-site2 | 192.168.17.17/24 | - | Provisioned | - |

> Provision status is based on Ansible inventory declaration and do not represent real status from CloudVision.

### Fabric Switches with inband Management IP

| POD | Type | Node | Management IP | Inband Interface |
| --- | ---- | ---- | ------------- | ---------------- |

## Fabric Topology

| Type | Node | Node Interface | Peer Type | Peer Node | Peer Interface |
| ---- | ---- | -------------- | --------- | ----------| -------------- |
| l3leaf | border1-site1 | Ethernet3 | wan_router | wan1-site1 | Ethernet1 |
| l3leaf | border1-site1 | Ethernet3.100 | wan_router | wan1-site1 | Ethernet1.100 |
| l3leaf | border1-site1 | Ethernet3.101 | wan_router | wan1-site1 | Ethernet1.101 |
| l3leaf | border1-site1 | Ethernet4 | wan_router | wan2-site1 | Ethernet1 |
| l3leaf | border1-site1 | Ethernet4.100 | wan_router | wan2-site1 | Ethernet1.100 |
| l3leaf | border1-site1 | Ethernet4.101 | wan_router | wan2-site1 | Ethernet1.101 |
| l3leaf | border1-site1 | Ethernet5 | mlag_peer | border2-site1 | Ethernet5 |
| l3leaf | border1-site1 | Ethernet6 | mlag_peer | border2-site1 | Ethernet6 |
| l3leaf | border2-site1 | Ethernet3 | wan_router | wan1-site1 | Ethernet2 |
| l3leaf | border2-site1 | Ethernet3.100 | wan_router | wan1-site1 | Ethernet2.100 |
| l3leaf | border2-site1 | Ethernet3.101 | wan_router | wan1-site1 | Ethernet2.101 |
| l3leaf | border2-site1 | Ethernet4 | wan_router | wan2-site1 | Ethernet2 |
| l3leaf | border2-site1 | Ethernet4.100 | wan_router | wan2-site1 | Ethernet2.100 |
| l3leaf | border2-site1 | Ethernet4.101 | wan_router | wan2-site1 | Ethernet2.101 |
| l3leaf | leaf1-site2 | Ethernet3 | wan_router | wan1-site2 | Ethernet1 |
| l3leaf | leaf1-site2 | Ethernet3.100 | wan_router | wan1-site2 | Ethernet1.100 |
| l3leaf | leaf1-site2 | Ethernet3.101 | wan_router | wan1-site2 | Ethernet1.101 |
| l3leaf | leaf1-site2 | Ethernet5 | mlag_peer | leaf2-site2 | Ethernet5 |
| l3leaf | leaf1-site2 | Ethernet6 | mlag_peer | leaf2-site2 | Ethernet6 |
| l2leaf | leaf1-site3 | Ethernet1 | wan_router | wan1-site3 | Ethernet1 |
| l2leaf | leaf1-site3 | Ethernet1 | wan_router | wan1-site3 | Ethernet1 |
| l3leaf | leaf2-site2 | Ethernet3 | wan_router | wan2-site2 | Ethernet1 |
| l3leaf | leaf2-site2 | Ethernet3.100 | wan_router | wan2-site2 | Ethernet1.100 |
| l3leaf | leaf2-site2 | Ethernet3.101 | wan_router | wan2-site2 | Ethernet1.101 |

## Fabric IP Allocation

### Fabric Point-To-Point Links

| Uplink IPv4 Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ---------------- | ------------------- | ------------------ | ------------------ |
| 10.0.1.0/24 | 256 | 24 | 9.38 % |
| 10.0.2.0/24 | 256 | 12 | 4.69 % |
| 10.0.3.0/24 | 256 | 0 | 0.0 % |

### Point-To-Point Links Node Allocation

| Node | Node Interface | Node IP Address | Peer Node | Peer Interface | Peer IP Address |
| ---- | -------------- | --------------- | --------- | -------------- | --------------- |
| border1-site1 | Ethernet3 | 10.0.1.8/31 | wan1-site1 | Ethernet1 | 10.0.1.9/31 |
| border1-site1 | Ethernet3.100 | 10.0.1.8/31 | wan1-site1 | Ethernet1.100 | 10.0.1.9/31 |
| border1-site1 | Ethernet3.101 | 10.0.1.8/31 | wan1-site1 | Ethernet1.101 | 10.0.1.9/31 |
| border1-site1 | Ethernet4 | 10.0.1.12/31 | wan2-site1 | Ethernet1 | 10.0.1.13/31 |
| border1-site1 | Ethernet4.100 | 10.0.1.12/31 | wan2-site1 | Ethernet1.100 | 10.0.1.13/31 |
| border1-site1 | Ethernet4.101 | 10.0.1.12/31 | wan2-site1 | Ethernet1.101 | 10.0.1.13/31 |
| border2-site1 | Ethernet3 | 10.0.1.10/31 | wan1-site1 | Ethernet2 | 10.0.1.11/31 |
| border2-site1 | Ethernet3.100 | 10.0.1.10/31 | wan1-site1 | Ethernet2.100 | 10.0.1.11/31 |
| border2-site1 | Ethernet3.101 | 10.0.1.10/31 | wan1-site1 | Ethernet2.101 | 10.0.1.11/31 |
| border2-site1 | Ethernet4 | 10.0.1.14/31 | wan2-site1 | Ethernet2 | 10.0.1.15/31 |
| border2-site1 | Ethernet4.100 | 10.0.1.14/31 | wan2-site1 | Ethernet2.100 | 10.0.1.15/31 |
| border2-site1 | Ethernet4.101 | 10.0.1.14/31 | wan2-site1 | Ethernet2.101 | 10.0.1.15/31 |
| leaf1-site2 | Ethernet3 | 10.0.2.12/31 | wan1-site2 | Ethernet1 | 10.0.2.13/31 |
| leaf1-site2 | Ethernet3.100 | 10.0.2.12/31 | wan1-site2 | Ethernet1.100 | 10.0.2.13/31 |
| leaf1-site2 | Ethernet3.101 | 10.0.2.12/31 | wan1-site2 | Ethernet1.101 | 10.0.2.13/31 |
| leaf2-site2 | Ethernet3 | 10.0.2.14/31 | wan2-site2 | Ethernet1 | 10.0.2.15/31 |
| leaf2-site2 | Ethernet3.100 | 10.0.2.14/31 | wan2-site2 | Ethernet1.100 | 10.0.2.15/31 |
| leaf2-site2 | Ethernet3.101 | 10.0.2.14/31 | wan2-site2 | Ethernet1.101 | 10.0.2.15/31 |

### Loopback Interfaces (BGP EVPN Peering)

| Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ------------- | ------------------- | ------------------ | ------------------ |
| 172.31.255.0/24 | 256 | 2 | 0.79 % |
| 192.168.255.0/24 | 256 | 11 | 4.3 % |

### Loopback0 Interfaces Node Allocation

| POD | Node | Loopback0 |
| --- | ---- | --------- |
| WAN | border1-site1 | 192.168.255.5/32 |
| WAN | border2-site1 | 192.168.255.6/32 |
| WAN | inet-cloud | 172.31.255.23/32 |
| WAN | leaf1-site2 | 192.168.255.9/32 |
| WAN | leaf2-site2 | 192.168.255.10/32 |
| WAN | mpls-cloud | 172.31.255.22/32 |
| WAN | pf1 | 192.168.255.1/32 |
| WAN | pf2 | 192.168.255.2/32 |
| WAN | wan1-site1 | 192.168.255.3/32 |
| WAN | wan1-site2 | 192.168.255.7/32 |
| WAN | wan1-site3 | 192.168.255.11/32 |
| WAN | wan2-site1 | 192.168.255.4/32 |
| WAN | wan2-site2 | 192.168.255.8/32 |

### VTEP Loopback VXLAN Tunnel Source Interfaces (VTEPs Only)

| VTEP Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ------------------ | ------------------- | ------------------ | ------------------ |
| 192.168.42.0/24 | 256 | 4 | 1.57 % |

### VTEP Loopback Node allocation

| POD | Node | Loopback1 |
| --- | ---- | --------- |
| WAN | border1-site1 | 192.168.42.5/32 |
| WAN | border2-site1 | 192.168.42.5/32 |
| WAN | leaf1-site2 | 192.168.42.9/32 |
| WAN | leaf2-site2 | 192.168.42.9/32 |
