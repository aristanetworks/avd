# DC1_FABRIC

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
  - [Connected Endpoint Keys](#connected-endpoint-keys)
  - [Firewalls](#firewalls)
  - [Servers](#servers)
  - [Port Profiles](#port-profiles)

## Fabric Switches and Management IP

| POD | Type | Node | Management IP | Platform | Provisioned in CloudVision | Serial Number |
| --- | ---- | ---- | ------------- | -------- | -------------------------- | ------------- |
| DC1_FABRIC | l2leaf | LEAF1 | 172.16.100.105/24 | cEOS-LAB | Provisioned | - |
| DC1_FABRIC | l2leaf | LEAF2 | 172.16.100.106/24 | cEOS-LAB | Provisioned | - |
| DC1_FABRIC | l2leaf | LEAF3 | 172.16.100.107/24 | cEOS-LAB | Provisioned | - |
| DC1_FABRIC | l2leaf | LEAF4 | 172.16.100.108/24 | cEOS-LAB | Provisioned | - |
| DC1_FABRIC | l2spine | SPINE1 | 172.16.100.101/24 | cEOS-LAB | Provisioned | - |
| DC1_FABRIC | l2spine | SPINE2 | 172.16.100.102/24 | cEOS-LAB | Provisioned | - |

> Provision status is based on Ansible inventory declaration and do not represent real status from CloudVision.

### Fabric Switches with inband Management IP

| POD | Type | Node | Management IP | Inband Interface |
| --- | ---- | ---- | ------------- | ---------------- |

## Fabric Topology

| Type | Node | Node Interface | Peer Type | Peer Node | Peer Interface |
| ---- | ---- | -------------- | --------- | ----------| -------------- |
| l2leaf | LEAF1 | Ethernet1 | l2spine | SPINE1 | Ethernet1 |
| l2leaf | LEAF1 | Ethernet2 | l2spine | SPINE2 | Ethernet1 |
| l2leaf | LEAF1 | Ethernet47 | mlag_peer | LEAF2 | Ethernet47 |
| l2leaf | LEAF1 | Ethernet48 | mlag_peer | LEAF2 | Ethernet48 |
| l2leaf | LEAF2 | Ethernet1 | l2spine | SPINE1 | Ethernet2 |
| l2leaf | LEAF2 | Ethernet2 | l2spine | SPINE2 | Ethernet2 |
| l2leaf | LEAF3 | Ethernet1 | l2spine | SPINE1 | Ethernet3 |
| l2leaf | LEAF3 | Ethernet2 | l2spine | SPINE2 | Ethernet3 |
| l2leaf | LEAF3 | Ethernet47 | mlag_peer | LEAF4 | Ethernet47 |
| l2leaf | LEAF3 | Ethernet48 | mlag_peer | LEAF4 | Ethernet48 |
| l2leaf | LEAF4 | Ethernet1 | l2spine | SPINE1 | Ethernet4 |
| l2leaf | LEAF4 | Ethernet2 | l2spine | SPINE2 | Ethernet4 |
| l2spine | SPINE1 | Ethernet47 | mlag_peer | SPINE2 | Ethernet47 |
| l2spine | SPINE1 | Ethernet48 | mlag_peer | SPINE2 | Ethernet48 |

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
| ------------------ | ------------------- | ------------------ | ------------------ |

### VTEP Loopback Node allocation

| POD | Node | Loopback1 |
| --- | ---- | --------- |

## Connected Endpoints

### Connected Endpoint Keys

| Key | Type | Description |
| --- | ---- | ----------- |
| firewalls | firewall | - |
| servers | server | - |

### Firewalls

| Name | Port | Fabric Device | Fabric Port | Description | Shutdown | Type | Mode | VLANs | Profile |
| ---- | ---- | ------------- | ------------| ----------- | -------- | ---- | ---- | ----- | ------- |
| FIREWALL | Eth1 | SPINE1 | Ethernet5 | FIREWALL_Eth1 | False | - | - | - | PP-FIREWALL |
| FIREWALL | Eth2 | SPINE2 | Ethernet5 | FIREWALL_Eth2 | False | - | - | - | PP-FIREWALL |

### Servers

| Name | Port | Fabric Device | Fabric Port | Description | Shutdown | Type | Mode | VLANs | Profile |
| ---- | ---- | ------------- | ------------| ----------- | -------- | ---- | ---- | ----- | ------- |
| Host2 | Eth1 | LEAF4 | Ethernet3 | Host2_Eth1 | False | - | - | - | PP-ORANGE |
| HostA | Eth1 | LEAF1 | Ethernet3 | HostA_Eth1 | False | - | - | - | PP-BLUE |
| HostB | Eth1 | LEAF2 | Ethernet3 | HostB_Eth1 | False | - | - | - | PP-GREEN |
| HostC | Eth1 | LEAF3 | Ethernet3 | HostC_Eth1 | False | - | - | - | PP-BLUE |

### Port Profiles

| Profile Name | Parent Profile |
| ------------ | -------------- |
| PP-BLUE | PP-DEFAULTS |
| PP-DEFAULTS | - |
| PP-FIREWALL | - |
| PP-GREEN | PP-DEFAULTS |
| PP-ORANGE | PP-DEFAULTS |
