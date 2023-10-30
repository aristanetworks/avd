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
| pod1 | l3leaf | dc1-pod1-leaf1a | 172.16.1.101/24 | vEOS-lab | Provisioned | - |
| pod1 | l3leaf | dc1-pod1-leaf1b | 172.16.1.102/24 | vEOS-lab | Provisioned | - |
| pod1 | l2leaf | dc1-pod1-leaf1c | 172.16.1.151/24 | vEOS-lab | Provisioned | - |
| pod1 | spine | dc1-pod1-spine1 | 172.16.1.11/24 | vEOS-lab | Provisioned | - |
| pod2 | l3leaf | dc1-pod2-leaf1a | 172.16.2.101/24 | vEOS-lab | Provisioned | - |
| pod2 | spine | dc1-pod2-spine1 | 172.16.2.11/24 | vEOS-lab | Provisioned | - |
| superspines | super-spine | dc1-super-spine1 | 172.16.1.1/24 | vEOS-lab | Provisioned | - |

> Provision status is based on Ansible inventory declaration and do not represent real status from CloudVision.

### Fabric Switches with inband Management IP

| POD | Type | Node | Management IP | Inband Interface |
| --- | ---- | ---- | ------------- | ---------------- |

## Fabric Topology

| Type | Node | Node Interface | Peer Type | Peer Node | Peer Interface |
| ---- | ---- | -------------- | --------- | ----------| -------------- |
| l3leaf | dc1-pod1-leaf1a | Ethernet1 | spine | dc1-pod1-spine1 | Ethernet1 |
| l3leaf | dc1-pod1-leaf1a | Ethernet3 | mlag_peer | dc1-pod1-leaf1b | Ethernet3 |
| l3leaf | dc1-pod1-leaf1a | Ethernet4 | mlag_peer | dc1-pod1-leaf1b | Ethernet4 |
| l3leaf | dc1-pod1-leaf1a | Ethernet8 | l2leaf | dc1-pod1-leaf1c | Ethernet1 |
| l3leaf | dc1-pod1-leaf1b | Ethernet1 | spine | dc1-pod1-spine1 | Ethernet2 |
| l3leaf | dc1-pod1-leaf1b | Ethernet8 | l2leaf | dc1-pod1-leaf1c | Ethernet2 |
| spine | dc1-pod1-spine1 | Ethernet10 | super-spine | dc1-super-spine1 | Ethernet1 |
| l3leaf | dc1-pod2-leaf1a | Ethernet1 | spine | dc1-pod2-spine1 | Ethernet1 |
| spine | dc1-pod2-spine1 | Ethernet10 | super-spine | dc1-super-spine1 | Ethernet4 |

## Fabric IP Allocation

### Fabric Point-To-Point Links

| Uplink IPv4 Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ---------------- | ------------------- | ------------------ | ------------------ |
| 10.255.255.0/26 | 64 | 10 | 15.63 % |

### Point-To-Point Links Node Allocation

| Node | Node Interface | Node IP Address | Peer Node | Peer Interface | Peer IP Address |
| ---- | -------------- | --------------- | --------- | -------------- | --------------- |
| dc1-pod1-leaf1a | Ethernet1 | 10.255.255.1/31 | dc1-pod1-spine1 | Ethernet1 | 10.255.255.0/31 |
| dc1-pod1-leaf1b | Ethernet1 | 10.255.255.3/31 | dc1-pod1-spine1 | Ethernet2 | 10.255.255.2/31 |
| dc1-pod1-spine1 | Ethernet10 | 10.255.255.1/31 | dc1-super-spine1 | Ethernet1 | 10.255.255.0/31 |
| dc1-pod2-leaf1a | Ethernet1 | 10.255.255.9/31 | dc1-pod2-spine1 | Ethernet1 | 10.255.255.8/31 |
| dc1-pod2-spine1 | Ethernet10 | 10.255.255.3/31 | dc1-super-spine1 | Ethernet4 | 10.255.255.2/31 |

### Loopback Interfaces (BGP EVPN Peering)

| Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ------------- | ------------------- | ------------------ | ------------------ |
| 10.255.0.0/27 | 32 | 6 | 18.75 % |

### Loopback0 Interfaces Node Allocation

| POD | Node | Loopback0 |
| --- | ---- | --------- |
| pod1 | dc1-pod1-leaf1a | 10.255.0.3/32 |
| pod1 | dc1-pod1-leaf1b | 10.255.0.4/32 |
| pod1 | dc1-pod1-spine1 | 10.255.0.1/32 |
| pod2 | dc1-pod2-leaf1a | 10.255.0.7/32 |
| pod2 | dc1-pod2-spine1 | 10.255.0.2/32 |
| superspines | dc1-super-spine1 | 10.255.0.1/32 |

### VTEP Loopback VXLAN Tunnel Source Interfaces (VTEPs Only)

| VTEP Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| --------------------- | ------------------- | ------------------ | ------------------ |
| 10.255.1.0/27 | 32 | 3 | 9.38 % |

### VTEP Loopback Node allocation

| POD | Node | Loopback1 |
| --- | ---- | --------- |
| pod1 | dc1-pod1-leaf1a | 10.255.1.3/32 |
| pod1 | dc1-pod1-leaf1b | 10.255.1.3/32 |
| pod2 | dc1-pod2-leaf1a | 10.255.1.7/32 |
