# Midtown

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
| Midtown | l3leaf | mtwn-fl1-lfa | - | 720XP | Provisioned | - |
| Midtown | l3leaf | mtwn-fl1-lfb | - | 720XP | Provisioned | - |
| Midtown | l2leaf | mtwn-fl1-m1 | - | 720XP | Provisioned | - |
| Midtown | l2leaf | mtwn-fl1-m2 | 172.16.1.151/24 | 720XP | Provisioned | - |
| Midtown | l2leaf | mtwn-fl1-m3 | - | 720XP | Provisioned | - |
| Midtown | l2leaf | mtwn-fl1-m4 | 172.16.1.151/24 | 720XP | Provisioned | - |
| Midtown | l2leaf | mtwn-fl1-m5 | - | 720XP | Provisioned | - |
| Midtown | l2leaf | mtwn-fl1-m6 | - | 720XP | Provisioned | - |
| Midtown | l2leaf | mtwn-fl1-m7 | - | 720XP | Provisioned | - |
| Midtown | l3leaf | mtwn-fl2-lfa | - | 720XP | Provisioned | - |
| Midtown | l3leaf | mtwn-fl2-lfb | - | 720XP | Provisioned | - |
| Midtown | l2leaf | mtwn-fl2-m1 | - | 720XP | Provisioned | - |
| Midtown | l2leaf | mtwn-fl2-m2 | - | 720XP | Provisioned | - |
| Midtown | l3leaf | mtwn-fl3-lfa | - | 720XP | Provisioned | - |
| Midtown | l2leaf | mtwn-fl3-m1 | - | 720XP | Provisioned | - |
| Midtown | spine | mtwn-spine1 | 172.16.1.11/24 | 7050SX3 | Provisioned | - |
| Midtown | spine | mtwn-spine2 | 172.16.1.12/24 | 7050SX3 | Provisioned | - |

> Provision status is based on Ansible inventory declaration and do not represent real status from CloudVision.

### Fabric Switches with inband Management IP

| POD | Type | Node | Management IP | Inband Interface |
| --- | ---- | ---- | ------------- | ---------------- |

## Fabric Topology

| Type | Node | Node Interface | Peer Type | Peer Node | Peer Interface |
| ---- | ---- | -------------- | --------- | ----------| -------------- |
| l3leaf | mtwn-fl1-lfa | Ethernet49 | mlag_peer | mtwn-fl1-lfb | Ethernet49 |
| l3leaf | mtwn-fl1-lfa | Ethernet50 | mlag_peer | mtwn-fl1-lfb | Ethernet50 |
| l3leaf | mtwn-fl1-lfa | Ethernet51 | spine | mtwn-spine1 | Ethernet1 |
| l3leaf | mtwn-fl1-lfa | Ethernet52 | spine | mtwn-spine2 | Ethernet1 |
| l3leaf | mtwn-fl1-lfa | Ethernet53 | l2leaf | mtwn-fl1-m1 | Ethernet49 |
| l3leaf | mtwn-fl1-lfa | Ethernet54 | l2leaf | mtwn-fl1-m2 | Ethernet49 |
| l3leaf | mtwn-fl1-lfb | Ethernet51 | spine | mtwn-spine1 | Ethernet2 |
| l3leaf | mtwn-fl1-lfb | Ethernet52 | spine | mtwn-spine2 | Ethernet2 |
| l3leaf | mtwn-fl1-lfb | Ethernet53 | l2leaf | mtwn-fl1-m1 | Ethernet50 |
| l3leaf | mtwn-fl1-lfb | Ethernet54 | l2leaf | mtwn-fl1-m2 | Ethernet50 |
| l2leaf | mtwn-fl1-m1 | Ethernet51 | mlag_peer | mtwn-fl1-m2 | Ethernet51 |
| l2leaf | mtwn-fl1-m1 | Ethernet52 | mlag_peer | mtwn-fl1-m2 | Ethernet52 |
| l2leaf | mtwn-fl1-m1 | Ethernet53 | l2leaf | mtwn-fl1-m3 | Ethernet49 |
| l2leaf | mtwn-fl1-m1 | Ethernet54 | l2leaf | mtwn-fl1-m4 | Ethernet49 |
| l2leaf | mtwn-fl1-m2 | Ethernet53 | l2leaf | mtwn-fl1-m3 | Ethernet50 |
| l2leaf | mtwn-fl1-m2 | Ethernet54 | l2leaf | mtwn-fl1-m4 | Ethernet50 |
| l2leaf | mtwn-fl1-m3 | Ethernet51 | mlag_peer | mtwn-fl1-m4 | Ethernet51 |
| l2leaf | mtwn-fl1-m3 | Ethernet52 | mlag_peer | mtwn-fl1-m4 | Ethernet52 |
| l2leaf | mtwn-fl1-m6 | Ethernet53 | l2leaf | mtwn-fl1-m7 | Ethernet49 |
| l3leaf | mtwn-fl2-lfa | Ethernet49 | mlag_peer | mtwn-fl2-lfb | Ethernet49 |
| l3leaf | mtwn-fl2-lfa | Ethernet50 | mlag_peer | mtwn-fl2-lfb | Ethernet50 |
| l3leaf | mtwn-fl2-lfa | Ethernet51 | spine | mtwn-spine1 | Ethernet3 |
| l3leaf | mtwn-fl2-lfa | Ethernet52 | spine | mtwn-spine2 | Ethernet3 |
| l3leaf | mtwn-fl2-lfa | Ethernet53 | l2leaf | mtwn-fl2-m1 | Ethernet49 |
| l3leaf | mtwn-fl2-lfb | Ethernet51 | spine | mtwn-spine1 | Ethernet4 |
| l3leaf | mtwn-fl2-lfb | Ethernet52 | spine | mtwn-spine2 | Ethernet4 |
| l3leaf | mtwn-fl2-lfb | Ethernet53 | l2leaf | mtwn-fl2-m2 | Ethernet49 |
| l3leaf | mtwn-fl3-lfa | Ethernet53 | l2leaf | mtwn-fl3-m1 | Ethernet49 |

## Fabric IP Allocation

### Fabric Point-To-Point Links

| Uplink IPv4 Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ---------------- | ------------------- | ------------------ | ------------------ |
| 10.255.255.0/24 | 256 | 16 | 6.25 % |

### Point-To-Point Links Node Allocation

| Node | Node Interface | Node IP Address | Peer Node | Peer Interface | Peer IP Address |
| ---- | -------------- | --------------- | --------- | -------------- | --------------- |
| mtwn-fl1-lfa | Ethernet51 | 10.255.255.1/31 | mtwn-spine1 | Ethernet1 | 10.255.255.0/31 |
| mtwn-fl1-lfa | Ethernet52 | 10.255.255.3/31 | mtwn-spine2 | Ethernet1 | 10.255.255.2/31 |
| mtwn-fl1-lfb | Ethernet51 | 10.255.255.5/31 | mtwn-spine1 | Ethernet2 | 10.255.255.4/31 |
| mtwn-fl1-lfb | Ethernet52 | 10.255.255.7/31 | mtwn-spine2 | Ethernet2 | 10.255.255.6/31 |
| mtwn-fl2-lfa | Ethernet51 | 10.255.255.9/31 | mtwn-spine1 | Ethernet3 | 10.255.255.8/31 |
| mtwn-fl2-lfa | Ethernet52 | 10.255.255.11/31 | mtwn-spine2 | Ethernet3 | 10.255.255.10/31 |
| mtwn-fl2-lfb | Ethernet51 | 10.255.255.13/31 | mtwn-spine1 | Ethernet4 | 10.255.255.12/31 |
| mtwn-fl2-lfb | Ethernet52 | 10.255.255.15/31 | mtwn-spine2 | Ethernet4 | 10.255.255.14/31 |

### Loopback Interfaces (BGP EVPN Peering)

| Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ------------- | ------------------- | ------------------ | ------------------ |
| 10.255.0.0/27 | 32 | 7 | 21.88 % |

### Loopback0 Interfaces Node Allocation

| POD | Node | Loopback0 |
| --- | ---- | --------- |
| Midtown | mtwn-fl1-lfa | 10.255.0.3/32 |
| Midtown | mtwn-fl1-lfb | 10.255.0.4/32 |
| Midtown | mtwn-fl2-lfa | 10.255.0.5/32 |
| Midtown | mtwn-fl2-lfb | 10.255.0.6/32 |
| Midtown | mtwn-fl3-lfa | 10.255.0.7/32 |
| Midtown | mtwn-spine1 | 10.255.0.1/32 |
| Midtown | mtwn-spine2 | 10.255.0.2/32 |

### VTEP Loopback VXLAN Tunnel Source Interfaces (VTEPs Only)

| VTEP Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| --------------------- | ------------------- | ------------------ | ------------------ |

### VTEP Loopback Node allocation

| POD | Node | Loopback1 |
| --- | ---- | --------- |
