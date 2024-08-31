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
| FABRIC | l3leaf | dc1-leaf1a | 172.16.1.101/24 | vEOS-lab | Provisioned | - |
| FABRIC | l3leaf | dc1-leaf1b | 172.16.1.102/24 | vEOS-lab | Provisioned | - |
| FABRIC | l2leaf | dc1-leaf1c | 172.16.1.151/24 | vEOS-lab | Provisioned | - |
| FABRIC | l3leaf | dc1-leaf2a | 172.16.1.103/24 | vEOS-lab | Provisioned | - |
| FABRIC | l3leaf | dc1-leaf2b | 172.16.1.104/24 | vEOS-lab | Provisioned | - |
| FABRIC | l2leaf | dc1-leaf2c | 172.16.1.152/24 | vEOS-lab | Provisioned | - |
| FABRIC | spine | dc1-spine1 | 172.16.1.11/24 | vEOS-lab | Provisioned | - |
| FABRIC | spine | dc1-spine2 | 172.16.1.12/24 | vEOS-lab | Provisioned | - |
| FABRIC | l3leaf | dc2-leaf1a | 172.16.1.111/24 | vEOS-lab | Provisioned | - |
| FABRIC | l3leaf | dc2-leaf1b | 172.16.1.112/24 | vEOS-lab | Provisioned | - |
| FABRIC | l2leaf | dc2-leaf1c | 172.16.1.161/24 | vEOS-lab | Provisioned | - |
| FABRIC | l3leaf | dc2-leaf2a | 172.16.1.113/24 | vEOS-lab | Provisioned | - |
| FABRIC | l3leaf | dc2-leaf2b | 172.16.1.114/24 | vEOS-lab | Provisioned | - |
| FABRIC | l2leaf | dc2-leaf2c | 172.16.1.162/24 | vEOS-lab | Provisioned | - |
| FABRIC | spine | dc2-spine1 | 172.16.1.21/24 | vEOS-lab | Provisioned | - |
| FABRIC | spine | dc2-spine2 | 172.16.1.22/24 | vEOS-lab | Provisioned | - |

> Provision status is based on Ansible inventory declaration and do not represent real status from CloudVision.

### Fabric Switches with inband Management IP

| POD | Type | Node | Management IP | Inband Interface |
| --- | ---- | ---- | ------------- | ---------------- |

## Fabric Topology

| Type | Node | Node Interface | Peer Type | Peer Node | Peer Interface |
| ---- | ---- | -------------- | --------- | ----------| -------------- |
| l3leaf | dc1-leaf1a | Ethernet1 | spine | dc1-spine1 | Ethernet1 |
| l3leaf | dc1-leaf1a | Ethernet2 | spine | dc1-spine2 | Ethernet1 |
| l3leaf | dc1-leaf1a | Ethernet3 | mlag_peer | dc1-leaf1b | Ethernet3 |
| l3leaf | dc1-leaf1a | Ethernet4 | mlag_peer | dc1-leaf1b | Ethernet4 |
| l3leaf | dc1-leaf1a | Ethernet8 | l2leaf | dc1-leaf1c | Ethernet1 |
| l3leaf | dc1-leaf1b | Ethernet1 | spine | dc1-spine1 | Ethernet2 |
| l3leaf | dc1-leaf1b | Ethernet2 | spine | dc1-spine2 | Ethernet2 |
| l3leaf | dc1-leaf1b | Ethernet8 | l2leaf | dc1-leaf1c | Ethernet2 |
| l3leaf | dc1-leaf2a | Ethernet1 | spine | dc1-spine1 | Ethernet3 |
| l3leaf | dc1-leaf2a | Ethernet2 | spine | dc1-spine2 | Ethernet3 |
| l3leaf | dc1-leaf2a | Ethernet3 | mlag_peer | dc1-leaf2b | Ethernet3 |
| l3leaf | dc1-leaf2a | Ethernet4 | mlag_peer | dc1-leaf2b | Ethernet4 |
| l3leaf | dc1-leaf2a | Ethernet6 | l3leaf | dc2-leaf2a | Ethernet6 |
| l3leaf | dc1-leaf2a | Ethernet8 | l2leaf | dc1-leaf2c | Ethernet1 |
| l3leaf | dc1-leaf2b | Ethernet1 | spine | dc1-spine1 | Ethernet4 |
| l3leaf | dc1-leaf2b | Ethernet2 | spine | dc1-spine2 | Ethernet4 |
| l3leaf | dc1-leaf2b | Ethernet6 | l3leaf | dc2-leaf2b | Ethernet6 |
| l3leaf | dc1-leaf2b | Ethernet8 | l2leaf | dc1-leaf2c | Ethernet2 |
| l3leaf | dc2-leaf1a | Ethernet1 | spine | dc2-spine1 | Ethernet1 |
| l3leaf | dc2-leaf1a | Ethernet2 | spine | dc2-spine2 | Ethernet1 |
| l3leaf | dc2-leaf1a | Ethernet3 | mlag_peer | dc2-leaf1b | Ethernet3 |
| l3leaf | dc2-leaf1a | Ethernet4 | mlag_peer | dc2-leaf1b | Ethernet4 |
| l3leaf | dc2-leaf1a | Ethernet8 | l2leaf | dc2-leaf1c | Ethernet1 |
| l3leaf | dc2-leaf1b | Ethernet1 | spine | dc2-spine1 | Ethernet2 |
| l3leaf | dc2-leaf1b | Ethernet2 | spine | dc2-spine2 | Ethernet2 |
| l3leaf | dc2-leaf1b | Ethernet8 | l2leaf | dc2-leaf1c | Ethernet2 |
| l3leaf | dc2-leaf2a | Ethernet1 | spine | dc2-spine1 | Ethernet3 |
| l3leaf | dc2-leaf2a | Ethernet2 | spine | dc2-spine2 | Ethernet3 |
| l3leaf | dc2-leaf2a | Ethernet3 | mlag_peer | dc2-leaf2b | Ethernet3 |
| l3leaf | dc2-leaf2a | Ethernet4 | mlag_peer | dc2-leaf2b | Ethernet4 |
| l3leaf | dc2-leaf2a | Ethernet8 | l2leaf | dc2-leaf2c | Ethernet1 |
| l3leaf | dc2-leaf2b | Ethernet1 | spine | dc2-spine1 | Ethernet4 |
| l3leaf | dc2-leaf2b | Ethernet2 | spine | dc2-spine2 | Ethernet4 |
| l3leaf | dc2-leaf2b | Ethernet8 | l2leaf | dc2-leaf2c | Ethernet2 |

## Fabric IP Allocation

### Fabric Point-To-Point Links

| Uplink IPv4 Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ---------------- | ------------------- | ------------------ | ------------------ |
| 10.255.255.0/26 | 64 | 16 | 25.0 % |
| 10.255.255.64/26 | 64 | 16 | 25.0 % |

### Point-To-Point Links Node Allocation

| Node | Node Interface | Node IP Address | Peer Node | Peer Interface | Peer IP Address |
| ---- | -------------- | --------------- | --------- | -------------- | --------------- |
| dc1-leaf1a | Ethernet1 | 10.255.255.1/31 | dc1-spine1 | Ethernet1 | 10.255.255.0/31 |
| dc1-leaf1a | Ethernet2 | 10.255.255.3/31 | dc1-spine2 | Ethernet1 | 10.255.255.2/31 |
| dc1-leaf1b | Ethernet1 | 10.255.255.5/31 | dc1-spine1 | Ethernet2 | 10.255.255.4/31 |
| dc1-leaf1b | Ethernet2 | 10.255.255.7/31 | dc1-spine2 | Ethernet2 | 10.255.255.6/31 |
| dc1-leaf2a | Ethernet1 | 10.255.255.9/31 | dc1-spine1 | Ethernet3 | 10.255.255.8/31 |
| dc1-leaf2a | Ethernet2 | 10.255.255.11/31 | dc1-spine2 | Ethernet3 | 10.255.255.10/31 |
| dc1-leaf2a | Ethernet6 | 172.16.100.0/31 | dc2-leaf2a | Ethernet6 | 172.16.100.1/31 |
| dc1-leaf2b | Ethernet1 | 10.255.255.13/31 | dc1-spine1 | Ethernet4 | 10.255.255.12/31 |
| dc1-leaf2b | Ethernet2 | 10.255.255.15/31 | dc1-spine2 | Ethernet4 | 10.255.255.14/31 |
| dc1-leaf2b | Ethernet6 | 172.16.100.2/31 | dc2-leaf2b | Ethernet6 | 172.16.100.3/31 |
| dc2-leaf1a | Ethernet1 | 10.255.255.105/31 | dc2-spine1 | Ethernet1 | 10.255.255.104/31 |
| dc2-leaf1a | Ethernet2 | 10.255.255.107/31 | dc2-spine2 | Ethernet1 | 10.255.255.106/31 |
| dc2-leaf1b | Ethernet1 | 10.255.255.109/31 | dc2-spine1 | Ethernet2 | 10.255.255.108/31 |
| dc2-leaf1b | Ethernet2 | 10.255.255.111/31 | dc2-spine2 | Ethernet2 | 10.255.255.110/31 |
| dc2-leaf2a | Ethernet1 | 10.255.255.113/31 | dc2-spine1 | Ethernet3 | 10.255.255.112/31 |
| dc2-leaf2a | Ethernet2 | 10.255.255.115/31 | dc2-spine2 | Ethernet3 | 10.255.255.114/31 |
| dc2-leaf2b | Ethernet1 | 10.255.255.117/31 | dc2-spine1 | Ethernet4 | 10.255.255.116/31 |
| dc2-leaf2b | Ethernet2 | 10.255.255.119/31 | dc2-spine2 | Ethernet4 | 10.255.255.118/31 |

### Loopback Interfaces (BGP EVPN Peering)

| Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ------------- | ------------------- | ------------------ | ------------------ |
| 10.255.0.0/27 | 32 | 6 | 18.75 % |
| 10.255.128.0/27 | 32 | 6 | 18.75 % |

### Loopback0 Interfaces Node Allocation

| POD | Node | Loopback0 |
| --- | ---- | --------- |
| FABRIC | dc1-leaf1a | 10.255.0.3/32 |
| FABRIC | dc1-leaf1b | 10.255.0.4/32 |
| FABRIC | dc1-leaf2a | 10.255.0.5/32 |
| FABRIC | dc1-leaf2b | 10.255.0.6/32 |
| FABRIC | dc1-spine1 | 10.255.0.1/32 |
| FABRIC | dc1-spine2 | 10.255.0.2/32 |
| FABRIC | dc2-leaf1a | 10.255.128.13/32 |
| FABRIC | dc2-leaf1b | 10.255.128.14/32 |
| FABRIC | dc2-leaf2a | 10.255.128.15/32 |
| FABRIC | dc2-leaf2b | 10.255.128.16/32 |
| FABRIC | dc2-spine1 | 10.255.128.11/32 |
| FABRIC | dc2-spine2 | 10.255.128.12/32 |

### VTEP Loopback VXLAN Tunnel Source Interfaces (VTEPs Only)

| VTEP Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ------------------ | ------------------- | ------------------ | ------------------ |
| 10.255.1.0/27 | 32 | 4 | 12.5 % |
| 10.255.129.0/27 | 32 | 4 | 12.5 % |

### VTEP Loopback Node allocation

| POD | Node | Loopback1 |
| --- | ---- | --------- |
| FABRIC | dc1-leaf1a | 10.255.1.3/32 |
| FABRIC | dc1-leaf1b | 10.255.1.3/32 |
| FABRIC | dc1-leaf2a | 10.255.1.5/32 |
| FABRIC | dc1-leaf2b | 10.255.1.5/32 |
| FABRIC | dc2-leaf1a | 10.255.129.13/32 |
| FABRIC | dc2-leaf1b | 10.255.129.13/32 |
| FABRIC | dc2-leaf2a | 10.255.129.15/32 |
| FABRIC | dc2-leaf2b | 10.255.129.15/32 |
