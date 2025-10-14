# TWODC_5STAGE_CLOS

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
- [Connected Endpoints](#connected-endpoints)
  - [Port Profiles](#port-profiles)

## Fabric Switches and Management IP

| POD | Type | Node | Management IP | Platform | Provisioned in CloudVision | Serial Number |
| --- | ---- | ---- | ------------- | -------- | -------------------------- | ------------- |
| DC1_POD1 | l2leaf | DC1-POD1-L2LEAF1A | 192.168.1.10/24 | CUSTOM-PLATFORM | Provisioned | - |
| DC1_POD1 | l2leaf | DC1-POD1-L2LEAF2A | 192.168.1.11/24 | vEOS-LAB | Provisioned | - |
| DC1_POD1 | l2leaf | DC1-POD1-L2LEAF2B | 192.168.1.12/24 | TOOLS-SERVER | Provisioned | - |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF1A | - | vEOS-LAB | Provisioned | - |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF1B | 192.168.1.26/24 | vEOS-LAB | Provisioned | - |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF2B | 192.168.1.9/16 | vEOS-LAB | Provisioned | - |
| DC1_POD1 | spine | DC1-POD1-SPINE1 | - | vEOS-LAB | Provisioned | - |
| DC1_POD1 | spine | DC1-POD1-SPINE2 | 192.168.1.6/24 | vEOS-LAB | Provisioned | DEADBEEFC0FFEE |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF1A | 192.168.1.15/24 | vEOS-LAB | Provisioned | - |
| DC1_POD2 | spine | DC1-POD2-SPINE1 | 192.168.1.13/24 | vEOS-LAB | Provisioned | - |
| DC1_POD2 | spine | DC1-POD2-SPINE2 | 192.168.1.14/24 | vEOS-LAB | Provisioned | - |
| DC1 | overlay-controller | DC1-RS1 | - | vEOS-LAB | Provisioned | - |
| DC1 | overlay-controller | DC1-RS2 | 192.168.1.4/24 | vEOS-LAB | Provisioned | - |
| DC1 | super-spine | DC1-SUPER-SPINE1 | - | vEOS-LAB | Provisioned | - |
| DC1 | super-spine | DC1-SUPER-SPINE2 | 192.168.1.2/24 | vEOS-LAB | Provisioned | - |
| DC1_POD1 | l3leaf | DC1.POD1.LEAF2A | 192.168.1.8/16 | vEOS-LAB | Provisioned | - |
| DC2_POD1 | l2leaf | DC2-POD1-L2LEAF1A | 192.168.1.23/24 | vEOS-LAB | Provisioned | - |
| DC2_POD1 | l2leaf | DC2-POD1-L2LEAF2A | 192.168.1.25/24 | vEOS-LAB | Provisioned | - |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF1A | 192.168.1.22/24 | vEOS-LAB | Provisioned | - |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF2A | 192.168.1.24/24 | vEOS-LAB | Provisioned | - |
| DC2_POD1 | spine | DC2-POD1-SPINE1 | 192.168.1.20/24 | vEOS-LAB | Provisioned | - |
| DC2_POD1 | spine | DC2-POD1-SPINE2 | 192.168.1.21/24 | vEOS-LAB | Provisioned | - |
| DC2 | overlay-controller | DC2-RS1 | 192.168.1.18/24 | vEOS-LAB | Provisioned | - |
| DC2 | overlay-controller | DC2-RS2 | 192.168.1.19/24 | vEOS-LAB | Provisioned | - |
| DC2 | super-spine | DC2-SUPER-SPINE1 | 192.168.1.16/24 | vEOS-LAB | Provisioned | - |
| DC2 | super-spine | DC2-SUPER-SPINE2 | 192.168.1.17/24 | vEOS-LAB | Provisioned | - |

> Provision status is based on Ansible inventory declaration and do not represent real status from CloudVision.

### Fabric Switches with inband Management IP

| POD | Type | Node | Management IP | Inband Interface |
| --- | ---- | ---- | ------------- | ---------------- |
| DC1_POD1 | l2leaf | DC1-POD1-L2LEAF1A | 172.21.110.4/24 | Vlan4085 |
| DC1_POD1 | l2leaf | DC1-POD1-L2LEAF2A | 172.21.110.5/24 | Vlan4085 |
| DC1_POD1 | l2leaf | DC1-POD1-L2LEAF2B | 172.21.110.6/24 | Vlan4085 |
| DC2_POD1 | l2leaf | DC2-POD1-L2LEAF1A | 172.21.210.4/24 | Vlan4092 |
| DC2_POD1 | l2leaf | DC2-POD1-L2LEAF2A | 172.21.210.5/24 | Vlan4092 |

## Fabric Topology

| Type | Node | Node Interface | Peer Type | Peer Node | Peer Interface |
| ---- | ---- | -------------- | --------- | ----------| -------------- |

## Fabric IP Allocation

### Fabric Point-To-Point Links

| Uplink IPv4 Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ---------------- | ------------------- | ------------------ | ------------------ |
| 172.16.11.0/24 | 256 | 0 | 0.0 % |
| 172.16.12.0/24 | 256 | 0 | 0.0 % |
| 172.16.21.0/24 | 256 | 0 | 0.0 % |
| 172.17.10.0/24 | 256 | 0 | 0.0 % |
| 172.17.20.0/24 | 256 | 0 | 0.0 % |
| 172.17.110.0/24 | 256 | 0 | 0.0 % |
| 172.17.120.0/24 | 256 | 0 | 0.0 % |
| 172.17.210.0/24 | 256 | 0 | 0.0 % |

### Point-To-Point Links Node Allocation

| Node | Node Interface | Node IP Address | Peer Node | Peer Interface | Peer IP Address |
| ---- | -------------- | --------------- | --------- | -------------- | --------------- |

### Loopback Interfaces (BGP EVPN Peering)

| Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ------------- | ------------------- | ------------------ | ------------------ |
| 172.16.10.0/24 | 256 | 2 | 0.79 % |
| 172.16.20.0/24 | 256 | 2 | 0.79 % |
| 172.16.100.0/24 | 256 | 2 | 0.79 % |
| 172.16.110.0/24 | 256 | 6 | 2.35 % |
| 172.16.120.0/24 | 256 | 3 | 1.18 % |
| 172.16.200.0/24 | 256 | 2 | 0.79 % |
| 172.16.210.0/24 | 256 | 4 | 1.57 % |

### Loopback0 Interfaces Node Allocation

| POD | Node | Loopback0 |
| --- | ---- | --------- |
| DC1_POD1 | DC1-POD1-LEAF1A | 172.16.110.3/32 |
| DC1_POD1 | DC1-POD1-LEAF1B | 172.16.110.6/32 |
| DC1_POD1 | DC1-POD1-LEAF2B | 172.16.110.5/32 |
| DC1_POD1 | DC1-POD1-SPINE1 | 172.16.110.1/32 |
| DC1_POD1 | DC1-POD1-SPINE2 | 172.16.110.2/32 |
| DC1_POD2 | DC1-POD2-LEAF1A | 172.16.120.3/32 |
| DC1_POD2 | DC1-POD2-SPINE1 | 172.16.120.1/32 |
| DC1_POD2 | DC1-POD2-SPINE2 | 172.16.120.2/32 |
| DC1 | DC1-RS1 | 172.16.10.1/32 |
| DC1 | DC1-RS2 | 172.16.10.2/32 |
| DC1 | DC1-SUPER-SPINE1 | 172.16.100.1/32 |
| DC1 | DC1-SUPER-SPINE2 | 172.16.100.2/32 |
| DC1_POD1 | DC1.POD1.LEAF2A | 172.16.110.4/32 |
| DC2_POD1 | DC2-POD1-LEAF1A | 172.16.210.3/32 |
| DC2_POD1 | DC2-POD1-LEAF2A | 172.16.210.4/32 |
| DC2_POD1 | DC2-POD1-SPINE1 | 172.16.210.1/32 |
| DC2_POD1 | DC2-POD1-SPINE2 | 172.16.210.2/32 |
| DC2 | DC2-RS1 | 172.16.20.1/32 |
| DC2 | DC2-RS2 | 172.16.20.2/32 |
| DC2 | DC2-SUPER-SPINE1 | 172.16.200.1/32 |
| DC2 | DC2-SUPER-SPINE2 | 172.16.200.2/32 |

### VTEP Loopback VXLAN Tunnel Source Interfaces (VTEPs Only)

| VTEP Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ------------------ | ------------------- | ------------------ | ------------------ |
| 172.18.110.0/24 | 256 | 3 | 1.18 % |
| 172.18.120.0/24 | 256 | 1 | 0.4 % |
| 172.18.210.0/24 | 256 | 2 | 0.79 % |

### VTEP Loopback Node allocation

| POD | Node | Loopback1 |
| --- | ---- | --------- |
| DC1_POD1 | DC1-POD1-LEAF1A | 172.18.110.3/32 |
| DC1_POD1 | DC1-POD1-LEAF2B | 172.18.110.4/32 |
| DC1_POD2 | DC1-POD2-LEAF1A | 172.18.120.3/32 |
| DC1_POD1 | DC1.POD1.LEAF2A | 172.18.110.4/32 |
| DC2_POD1 | DC2-POD1-LEAF1A | 172.18.210.3/32 |
| DC2_POD1 | DC2-POD1-LEAF2A | 172.18.210.4/32 |

## Connected Endpoints

No connected endpoint configured!

### Port Profiles

| Profile Name | Parent Profile |
| ------------ | -------------- |
| NESTED_TENANT_A | TENANT_A |
| TENANT_A | - |
