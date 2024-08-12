# L2LS

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
| L2LS_BGP | l2leaf | BGP-LEAF1 | - | - | Provisioned | - |
| L2LS_BGP | l2leaf | BGP-LEAF2 | - | - | Provisioned | - |
| L2LS_ISIS | l2leaf | ISIS-LEAF1 | 192.168.200.105/24 | vEOS-LAB | Provisioned | - |
| L2LS_L2ONLY | l2leaf | L2ONLY-LEAF1 | - | - | Provisioned | - |
| L2LS_L2ONLY | l2leaf | L2ONLY-LEAF2 | - | - | Provisioned | - |
| L2LS_OSPF | l2leaf | OSPF-LEAF1 | - | - | Provisioned | - |
| L2LS_OSPF | l2leaf | OSPF-LEAF2 | - | - | Provisioned | - |

> Provision status is based on Ansible inventory declaration and do not represent real status from CloudVision.

### Fabric Switches with inband Management IP

| POD | Type | Node | Management IP | Inband Interface |
| --- | ---- | ---- | ------------- | ---------------- |
| L2LS_BGP | l2leaf | BGP-LEAF1 | 172.23.254.4/24 | Vlan4092 |
| L2LS_BGP | l2leaf | BGP-LEAF2 | 172.23.254.5/24 | Vlan4092 |
| L2LS_ISIS | l2leaf | ISIS-LEAF1 | 172.23.254.4/24 | Vlan4092 |
| L2LS_L2ONLY | l2leaf | L2ONLY-LEAF1 | 172.23.254.4/24 | Vlan4092 |
| L2LS_L2ONLY | l2leaf | L2ONLY-LEAF2 | 172.23.254.5/24 | Vlan4092 |
| L2LS_OSPF | l2leaf | OSPF-LEAF1 | 172.23.254.4/24 | Vlan4092 |
| L2LS_OSPF | l2leaf | OSPF-LEAF2 | 172.23.254.5/24 | Vlan4092 |

## Fabric Topology

| Type | Node | Node Interface | Peer Type | Peer Node | Peer Interface |
| ---- | ---- | -------------- | --------- | ----------| -------------- |

## Fabric IP Allocation

### Fabric Point-To-Point Links

| Uplink IPv4 Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ---------------- | ------------------- | ------------------ | ------------------ |

### Point-To-Point Links Node Allocation

| Node | Node Interface | Node IP Address | Peer Node | Peer Interface | Peer IP Address |
| ---- | -------------- | --------------- | --------- | -------------- | --------------- |

### Loopback Interfaces (BGP EVPN Peering)

| Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ------------- | ------------------- | ------------------ | ------------------ |

### Loopback0 Interfaces Node Allocation

| POD | Node | Loopback0 |
| --- | ---- | --------- |

### VTEP Loopback VXLAN Tunnel Source Interfaces (VTEPs Only)

| VTEP Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| --------------------- | ------------------- | ------------------ | ------------------ |

### VTEP Loopback Node allocation

| POD | Node | Loopback1 |
| --- | ---- | --------- |
