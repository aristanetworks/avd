# EOS_DESIGNS_UNIT_TESTS

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
| EOS_DESIGNS_UNIT_TESTS | spine | cvp-instance-ips-cvaas | - | - | Provisioned |
| EOS_DESIGNS_UNIT_TESTS | l3leaf | DC1-BL1A | - | - | Provisioned |
| EOS_DESIGNS_UNIT_TESTS | l3leaf | DC1-BL1B | - | - | Provisioned |
| EOS_DESIGNS_UNIT_TESTS | l3leaf | DC1-BL2A | - | - | Provisioned |
| EOS_DESIGNS_UNIT_TESTS | l3leaf | DC1-BL2B | - | - | Provisioned |
| EOS_DESIGNS_UNIT_TESTS | l3leaf | DC1-CL1A | - | - | Provisioned |
| EOS_DESIGNS_UNIT_TESTS | l3leaf | DC1-CL1B | - | - | Provisioned |
| EOS_DESIGNS_UNIT_TESTS | l2leaf | DC1-L2LEAF1A | - | - | Provisioned |
| EOS_DESIGNS_UNIT_TESTS | l2leaf | DC1-L2LEAF1B | - | - | Provisioned |
| EOS_DESIGNS_UNIT_TESTS | l2leaf | DC1-L2LEAF2A | - | - | Provisioned |
| EOS_DESIGNS_UNIT_TESTS | l2leaf | DC1-L2LEAF2B | - | - | Provisioned |
| EOS_DESIGNS_UNIT_TESTS | l2leaf | DC1-L2LEAF3A | 192.168.200.116/24 | vEOS-LAB | Provisioned |
| EOS_DESIGNS_UNIT_TESTS | l2leaf | DC1-L2LEAF4A | 192.168.200.119/24 | vEOS-LAB | Provisioned |
| EOS_DESIGNS_UNIT_TESTS | l2leaf | DC1-L2LEAF5A | - | - | Provisioned |
| EOS_DESIGNS_UNIT_TESTS | l2leaf | DC1-L2LEAF5B | - | - | Provisioned |
| EOS_DESIGNS_UNIT_TESTS | l3leaf | DC1-LEAF1A | - | - | Provisioned |
| EOS_DESIGNS_UNIT_TESTS | l3leaf | DC1-LEAF2A | - | - | Provisioned |
| EOS_DESIGNS_UNIT_TESTS | l3leaf | DC1-LEAF2B | - | - | Provisioned |
| EOS_DESIGNS_UNIT_TESTS | spine | DC1-SPINE1 | - | - | Provisioned |
| EOS_DESIGNS_UNIT_TESTS | spine | DC1-SPINE2 | - | - | Provisioned |
| EOS_DESIGNS_UNIT_TESTS | spine | DC1-SPINE3 | - | - | Provisioned |
| EOS_DESIGNS_UNIT_TESTS | spine | DC1-SPINE4 | - | - | Provisioned |
| EOS_DESIGNS_UNIT_TESTS | l3leaf | DC1-SVC3A | - | - | Provisioned |
| EOS_DESIGNS_UNIT_TESTS | l3leaf | DC1-SVC3B | - | - | Provisioned |
| EOS_DESIGNS_UNIT_TESTS | l3leaf | evpn_services_l2_only_false | - | - | Provisioned |
| EOS_DESIGNS_UNIT_TESTS | l3leaf | evpn_services_l2_only_true | - | - | Provisioned |
| EOS_DESIGNS_UNIT_TESTS | l2leaf | mgmt_interface_default | 1.1.1.2 | - | Provisioned |
| EOS_DESIGNS_UNIT_TESTS | l2leaf | mgmt_interface_fabric | 1.1.1.2 | - | Provisioned |
| EOS_DESIGNS_UNIT_TESTS | l2leaf | mgmt_interface_host | 1.1.1.2 | 7500R2 | Provisioned |
| EOS_DESIGNS_UNIT_TESTS | l2leaf | mgmt_interface_platform | 1.1.1.2 | 7500R2 | Provisioned |
| EOS_DESIGNS_UNIT_TESTS | l2leaf | MH-L2LEAF1A | 192.168.201.201/24 | vEOS-LAB | Provisioned |
| EOS_DESIGNS_UNIT_TESTS | l3leaf | MH-LEAF1A | - | - | Provisioned |
| EOS_DESIGNS_UNIT_TESTS | l3leaf | MH-LEAF1B | - | - | Provisioned |
| EOS_DESIGNS_UNIT_TESTS | l3leaf | MH-LEAF2A | - | - | Provisioned |

> Provision status is based on Ansible inventory declaration and do not represent real status from CloudVision.

## Fabric Switches with inband Management IP
| POD | Type | Node | Management IP | Inband Interface |
| --- | ---- | ---- | ------------- | ---------------- |

# Fabric Topology

| Type | Node | Node Interface | Peer Type | Peer Node | Peer Interface |
| ---- | ---- | -------------- | --------- | ----------| -------------- |

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

## Loopback0 Interfaces Node Allocation

| POD | Node | Loopback0 |
| --- | ---- | --------- |

## VTEP Loopback VXLAN Tunnel Source Interfaces (VTEPs Only)

| VTEP Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| --------------------- | ------------------- | ------------------ | ------------------ |

## VTEP Loopback Node allocation

| POD | Node | Loopback1 |
| --- | ---- | --------- |
