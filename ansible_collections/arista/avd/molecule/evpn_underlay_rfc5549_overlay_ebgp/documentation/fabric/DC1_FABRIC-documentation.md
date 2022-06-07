# DC1_FABRIC

# Table of Contents

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

# Fabric Switches and Management IP

| POD | Type | Node | Management IP | Platform | Provisioned in CloudVision |
| --- | ---- | ---- | ------------- | -------- | -------------------------- |
| DC1_FABRIC | l3leaf | DC1-BL1A | 192.168.200.110/24 | 7280R | Provisioned |
| DC1_FABRIC | l3leaf | DC1-BL1B | 192.168.200.111/24 | 7280R | Provisioned |
| DC1_FABRIC | l2leaf | DC1-L2LEAF1A | 192.168.200.112/24 | vEOS-LAB | Provisioned |
| DC1_FABRIC | l2leaf | DC1-L2LEAF2A | 192.168.200.113/24 | vEOS-LAB | Provisioned |
| DC1_FABRIC | l2leaf | DC1-L2LEAF2B | 192.168.200.114/24 | vEOS-LAB | Provisioned |
| DC1_FABRIC | l3leaf | DC1-LEAF1A | 192.168.200.105/24 | 7280R | Provisioned |
| DC1_FABRIC | l3leaf | DC1-LEAF2A | 192.168.200.106/24 | 7280R | Provisioned |
| DC1_FABRIC | l3leaf | DC1-LEAF2B | 192.168.200.107/24 | 7280R | Provisioned |
| DC1_FABRIC | l3leaf | DC1-LEAF3A | 192.168.200.106/24 | 7280R | Provisioned |
| DC1_FABRIC | l3leaf | DC1-LEAF3B | 192.168.200.107/24 | 7280R | Provisioned |
| DC1_FABRIC | l3leaf | DC1-LEAF4A | 192.168.200.106/24 | 7280R | Provisioned |
| DC1_FABRIC | l3leaf | DC1-LEAF4B | 192.168.200.107/24 | 7280R | Provisioned |
| DC1_FABRIC | spine | DC1-SPINE1 | 192.168.200.101/24 | vEOS-LAB | Provisioned |
| DC1_FABRIC | spine | DC1-SPINE2 | 192.168.200.102/24 | vEOS-LAB | Provisioned |
| DC1_FABRIC | spine | DC1-SPINE3 | 192.168.200.103/24 | vEOS-LAB | Provisioned |
| DC1_FABRIC | spine | DC1-SPINE4 | 192.168.200.104/24 | vEOS-LAB | Provisioned |
| DC1_FABRIC | spine | DC1-SPINE5 | 192.168.200.105/24 | vEOS-LAB | Provisioned |
| DC1_FABRIC | spine | DC1-SPINE6 | 192.168.200.105/24 | vEOS-LAB | Provisioned |
| DC1_FABRIC | l3leaf | DC1-SVC3A | 192.168.200.108/24 | 7280R | Provisioned |
| DC1_FABRIC | l3leaf | DC1-SVC3B | 192.168.200.109/24 | 7280R | Provisioned |

> Provision status is based on Ansible inventory declaration and do not represent real status from CloudVision.

## Fabric Switches with inband Management IP
| POD | Type | Node | Management IP | Inband Interface |
| --- | ---- | ---- | ------------- | ---------------- |

# Fabric Topology

| Type | Node | Node Interface | Peer Type | Peer Node | Peer Interface |
| ---- | ---- | -------------- | --------- | ----------| -------------- |
| l3leaf | DC1-BL1A | Ethernet1 | spine | DC1-SPINE1 | Ethernet6 |
| l3leaf | DC1-BL1A | Ethernet2 | spine | DC1-SPINE2 | Ethernet6 |
| l3leaf | DC1-BL1A | Ethernet3 | spine | DC1-SPINE3 | Ethernet6 |
| l3leaf | DC1-BL1A | Ethernet4 | spine | DC1-SPINE4 | Ethernet6 |
| l3leaf | DC1-BL1A | Ethernet9 | l3leaf | DC1-BL1B | Ethernet9 |
| l3leaf | DC1-BL1A | Ethernet10 | l3leaf | DC1-BL1B | Ethernet10 |
| l3leaf | DC1-BL1B | Ethernet1 | spine | DC1-SPINE1 | Ethernet7 |
| l3leaf | DC1-BL1B | Ethernet2 | spine | DC1-SPINE2 | Ethernet7 |
| l3leaf | DC1-BL1B | Ethernet3 | spine | DC1-SPINE3 | Ethernet7 |
| l3leaf | DC1-BL1B | Ethernet4 | spine | DC1-SPINE4 | Ethernet7 |
| l2leaf | DC1-L2LEAF1A | Ethernet1 | l3leaf | DC1-LEAF2A | Ethernet7 |
| l2leaf | DC1-L2LEAF1A | Ethernet2 | l3leaf | DC1-LEAF2B | Ethernet7 |
| l2leaf | DC1-L2LEAF2A | Ethernet1 | l3leaf | DC1-SVC3A | Ethernet7 |
| l2leaf | DC1-L2LEAF2A | Ethernet2 | l3leaf | DC1-SVC3B | Ethernet7 |
| l2leaf | DC1-L2LEAF2A | Ethernet3 | mlag_peer | DC1-L2LEAF2B | Ethernet3 |
| l2leaf | DC1-L2LEAF2A | Ethernet4 | mlag_peer | DC1-L2LEAF2B | Ethernet4 |
| l2leaf | DC1-L2LEAF2B | Ethernet1 | l3leaf | DC1-SVC3A | Ethernet8 |
| l2leaf | DC1-L2LEAF2B | Ethernet2 | l3leaf | DC1-SVC3B | Ethernet8 |
| l3leaf | DC1-LEAF1A | Ethernet1 | spine | DC1-SPINE1 | Ethernet1 |
| l3leaf | DC1-LEAF1A | Ethernet2 | spine | DC1-SPINE2 | Ethernet1 |
| l3leaf | DC1-LEAF1A | Ethernet3 | spine | DC1-SPINE3 | Ethernet1 |
| l3leaf | DC1-LEAF1A | Ethernet4 | spine | DC1-SPINE4 | Ethernet1 |
| l3leaf | DC1-LEAF2A | Ethernet1 | spine | DC1-SPINE1 | Ethernet2 |
| l3leaf | DC1-LEAF2A | Ethernet2 | spine | DC1-SPINE2 | Ethernet2 |
| l3leaf | DC1-LEAF2A | Ethernet3 | spine | DC1-SPINE3 | Ethernet2 |
| l3leaf | DC1-LEAF2A | Ethernet4 | spine | DC1-SPINE4 | Ethernet2 |
| l3leaf | DC1-LEAF2A | Ethernet5 | mlag_peer | DC1-LEAF2B | Ethernet5 |
| l3leaf | DC1-LEAF2A | Ethernet6 | mlag_peer | DC1-LEAF2B | Ethernet6 |
| l3leaf | DC1-LEAF2B | Ethernet1 | spine | DC1-SPINE1 | Ethernet3 |
| l3leaf | DC1-LEAF2B | Ethernet2 | spine | DC1-SPINE2 | Ethernet3 |
| l3leaf | DC1-LEAF2B | Ethernet3 | spine | DC1-SPINE3 | Ethernet3 |
| l3leaf | DC1-LEAF2B | Ethernet4 | spine | DC1-SPINE4 | Ethernet3 |
| l3leaf | DC1-LEAF3A | Ethernet1 | spine | DC1-SPINE5 | Ethernet1 |
| l3leaf | DC1-LEAF3A | Ethernet5 | mlag_peer | DC1-LEAF3B | Ethernet5 |
| l3leaf | DC1-LEAF3A | Ethernet6 | mlag_peer | DC1-LEAF3B | Ethernet6 |
| l3leaf | DC1-LEAF3B | Ethernet1 | spine | DC1-SPINE5 | Ethernet2 |
| l3leaf | DC1-LEAF4A | Ethernet1 | spine | DC1-SPINE6 | Ethernet1 |
| l3leaf | DC1-LEAF4A | Ethernet5 | mlag_peer | DC1-LEAF4B | Ethernet5 |
| l3leaf | DC1-LEAF4A | Ethernet6 | mlag_peer | DC1-LEAF4B | Ethernet6 |
| l3leaf | DC1-LEAF4B | Ethernet1 | spine | DC1-SPINE6 | Ethernet2 |
| spine | DC1-SPINE1 | Ethernet4 | l3leaf | DC1-SVC3A | Ethernet1 |
| spine | DC1-SPINE1 | Ethernet5 | l3leaf | DC1-SVC3B | Ethernet1 |
| spine | DC1-SPINE2 | Ethernet4 | l3leaf | DC1-SVC3A | Ethernet2 |
| spine | DC1-SPINE2 | Ethernet5 | l3leaf | DC1-SVC3B | Ethernet2 |
| spine | DC1-SPINE3 | Ethernet4 | l3leaf | DC1-SVC3A | Ethernet3 |
| spine | DC1-SPINE3 | Ethernet5 | l3leaf | DC1-SVC3B | Ethernet3 |
| spine | DC1-SPINE4 | Ethernet4 | l3leaf | DC1-SVC3A | Ethernet4 |
| spine | DC1-SPINE4 | Ethernet5 | l3leaf | DC1-SVC3B | Ethernet4 |
| l3leaf | DC1-SVC3A | Ethernet5 | mlag_peer | DC1-SVC3B | Ethernet5 |
| l3leaf | DC1-SVC3A | Ethernet6 | mlag_peer | DC1-SVC3B | Ethernet6 |

# Fabric IP Allocation

## Fabric Point-To-Point Links

| Uplink IPv4 Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ---------------- | ------------------- | ------------------ | ------------------ |

## Point-To-Point Links Node Allocation

| Node | Node Interface | Node IP Address | Peer Node | Peer Interface | Peer IP Address |
| ---- | -------------- | --------------- | --------- | -------------- | --------------- |

## Loopback Interfaces (BGP EVPN Peering)

| Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ------------- | ------------------- | ------------------ | ------------------ |
| 192.168.255.0/24 | 256 | 17 | 6.65 % |

## Loopback0 Interfaces Node Allocation

| POD | Node | Loopback0 |
| --- | ---- | --------- |
| DC1_FABRIC | DC1-BL1A | 192.168.255.10/32 |
| DC1_FABRIC | DC1-BL1B | 192.168.255.11/32 |
| DC1_FABRIC | DC1-LEAF1A | 192.168.255.5/32 |
| DC1_FABRIC | DC1-LEAF2A | 192.168.255.6/32 |
| DC1_FABRIC | DC1-LEAF2B | 192.168.255.7/32 |
| DC1_FABRIC | DC1-LEAF3A | 192.168.255.12/32 |
| DC1_FABRIC | DC1-LEAF3B | 192.168.255.13/32 |
| DC1_FABRIC | DC1-LEAF4A | 192.168.255.14/32 |
| DC1_FABRIC | DC1-LEAF4B | 192.168.255.15/32 |
| DC1_FABRIC | DC1-SPINE1 | 192.168.255.1/32 |
| DC1_FABRIC | DC1-SPINE2 | 192.168.255.2/32 |
| DC1_FABRIC | DC1-SPINE3 | 192.168.255.3/32 |
| DC1_FABRIC | DC1-SPINE4 | 192.168.255.4/32 |
| DC1_FABRIC | DC1-SPINE5 | 192.168.255.5/32 |
| DC1_FABRIC | DC1-SPINE6 | 192.168.255.6/32 |
| DC1_FABRIC | DC1-SVC3A | 192.168.255.8/32 |
| DC1_FABRIC | DC1-SVC3B | 192.168.255.9/32 |

## VTEP Loopback VXLAN Tunnel Source Interfaces (VTEPs Only)

| VTEP Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| --------------------- | ------------------- | ------------------ | ------------------ |
| 192.168.254.0/24 | 256 | 11 | 4.3 % |

## VTEP Loopback Node allocation

| POD | Node | Loopback1 |
| --- | ---- | --------- |
| DC1_FABRIC | DC1-BL1A | 192.168.254.10/32 |
| DC1_FABRIC | DC1-BL1B | 192.168.254.11/32 |
| DC1_FABRIC | DC1-LEAF1A | 192.168.254.5/32 |
| DC1_FABRIC | DC1-LEAF2A | 192.168.254.6/32 |
| DC1_FABRIC | DC1-LEAF2B | 192.168.254.6/32 |
| DC1_FABRIC | DC1-LEAF3A | 192.168.254.12/32 |
| DC1_FABRIC | DC1-LEAF3B | 192.168.254.12/32 |
| DC1_FABRIC | DC1-LEAF4A | 192.168.254.14/32 |
| DC1_FABRIC | DC1-LEAF4B | 192.168.254.14/32 |
| DC1_FABRIC | DC1-SVC3A | 192.168.254.8/32 |
| DC1_FABRIC | DC1-SVC3B | 192.168.254.8/32 |
