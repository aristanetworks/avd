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
  - [VRF Summary](#vrf-summary)
  - [BGP Peer Groups](#bgp-peer-groups)
  - [BGP Neighbors](#bgp-neighbors)
  - [VRF Routing Protocols](#vrf-routing-protocols)
  - [VTEP Loopback VXLAN Tunnel Source Interfaces (VTEPs Only)](#vtep-loopback-vxlan-tunnel-source-interfaces-vteps-only)
  - [VTEP Loopback Node allocation](#vtep-loopback-node-allocation)

## Fabric Switches and Management IP

| POD | Type | Node | Management IP | Platform | Provisioned in CloudVision | Serial Number |
| --- | ---- | ---- | ------------- | -------- | -------------------------- | ------------- |
| WAN | spine | inet-cloud | 192.168.17.31/24 | vEOS-lab | Provisioned | - |
| WAN | spine | mpls-cloud | 192.168.17.30/24 | vEOS-lab | Provisioned | - |
| WAN | wan_rr | pf1 | 192.168.17.10/24 | CloudEOS | Provisioned | - |
| WAN | wan_rr | pf2 | 192.168.17.11/24 | CloudEOS | Provisioned | - |
| WAN | l3leaf | site1-border1 | 192.168.17.14/24 | vEOS-lab | Provisioned | - |
| WAN | l3leaf | site1-border2 | 192.168.17.15/24 | vEOS-lab | Provisioned | - |
| WAN | wan_router | site1-wan1 | 192.168.17.12/24 | CloudEOS | Provisioned | - |
| WAN | wan_router | site1-wan2 | 192.168.17.13/24 | CloudEOS | Provisioned | - |
| WAN | l3leaf | site2-leaf1 | 192.168.17.18/24 | vEOS-lab | Provisioned | - |
| WAN | l3leaf | site2-leaf2 | 192.168.17.19/24 | vEOS-lab | Provisioned | - |
| WAN | wan_router | site2-wan1 | 192.168.17.16/24 | CloudEOS | Provisioned | - |
| WAN | wan_router | site2-wan2 | 192.168.17.17/24 | CloudEOS | Provisioned | - |
| WAN | l2leaf | site3-leaf1 | 192.168.17.21/24 | vEOS-lab | Provisioned | - |
| WAN | wan_router | site3-wan1 | 192.168.17.20/24 | CloudEOS | Provisioned | - |
| WAN | l3leaf | site4-border1 | 192.168.17.23/24 | vEOS-lab | Provisioned | - |
| WAN | l3leaf | site4-border2 | 192.168.17.24/24 | vEOS-lab | Provisioned | - |
| WAN | wan_router | site4-wan1 | 192.168.17.22/24 | CloudEOS | Provisioned | - |

> Provision status is based on Ansible inventory declaration and do not represent real status from CloudVision.

### Fabric Switches with inband Management IP

| POD | Type | Node | Management IP | Inband Interface |
| --- | ---- | ---- | ------------- | ---------------- |

## Fabric Topology

| Type | Node | Node Interface | Peer Type | Peer Node | Peer Interface |
| ---- | ---- | -------------- | --------- | --------- | -------------- |
| l3leaf | site1-border1 | Ethernet3 | wan_router | site1-wan1 | Ethernet1 |
| l3leaf | site1-border1 | Ethernet3.100 | wan_router | site1-wan1 | Ethernet1.100 |
| l3leaf | site1-border1 | Ethernet3.101 | wan_router | site1-wan1 | Ethernet1.101 |
| l3leaf | site1-border1 | Ethernet4 | wan_router | site1-wan2 | Ethernet1 |
| l3leaf | site1-border1 | Ethernet4.100 | wan_router | site1-wan2 | Ethernet1.100 |
| l3leaf | site1-border1 | Ethernet4.101 | wan_router | site1-wan2 | Ethernet1.101 |
| l3leaf | site1-border1 | Ethernet5 | mlag_peer | site1-border2 | Ethernet5 |
| l3leaf | site1-border1 | Ethernet6 | mlag_peer | site1-border2 | Ethernet6 |
| l3leaf | site1-border2 | Ethernet3 | wan_router | site1-wan1 | Ethernet2 |
| l3leaf | site1-border2 | Ethernet3.100 | wan_router | site1-wan1 | Ethernet2.100 |
| l3leaf | site1-border2 | Ethernet3.101 | wan_router | site1-wan1 | Ethernet2.101 |
| l3leaf | site1-border2 | Ethernet4 | wan_router | site1-wan2 | Ethernet2 |
| l3leaf | site1-border2 | Ethernet4.100 | wan_router | site1-wan2 | Ethernet2.100 |
| l3leaf | site1-border2 | Ethernet4.101 | wan_router | site1-wan2 | Ethernet2.101 |
| l3leaf | site2-leaf1 | Ethernet3 | wan_router | site2-wan1 | Ethernet1 |
| l3leaf | site2-leaf1 | Ethernet3.100 | wan_router | site2-wan1 | Ethernet1.100 |
| l3leaf | site2-leaf1 | Ethernet3.101 | wan_router | site2-wan1 | Ethernet1.101 |
| l3leaf | site2-leaf1 | Ethernet5 | mlag_peer | site2-leaf2 | Ethernet5 |
| l3leaf | site2-leaf1 | Ethernet6 | mlag_peer | site2-leaf2 | Ethernet6 |
| l3leaf | site2-leaf2 | Ethernet3 | wan_router | site2-wan2 | Ethernet1 |
| l3leaf | site2-leaf2 | Ethernet3.100 | wan_router | site2-wan2 | Ethernet1.100 |
| l3leaf | site2-leaf2 | Ethernet3.101 | wan_router | site2-wan2 | Ethernet1.101 |
| l2leaf | site3-leaf1 | Ethernet1 | wan_router | site3-wan1 | Ethernet1 |
| l2leaf | site3-leaf1 | Ethernet1 | wan_router | site3-wan1 | Ethernet1 |
| l2leaf | site3-leaf1 | Ethernet1 VLAN 42 | wan_router | site3-wan1 | Ethernet1.42 |
| l2leaf | site3-leaf1 | Ethernet1 VLAN 666 | wan_router | site3-wan1 | Ethernet1.666 |
| l3leaf | site4-border1 | Ethernet3 | wan_router | site4-wan1 | Ethernet1 |
| l3leaf | site4-border1 | Ethernet5 | mlag_peer | site4-border2 | Ethernet5 |
| l3leaf | site4-border1 | Ethernet6 | mlag_peer | site4-border2 | Ethernet6 |
| l3leaf | site4-border2 | Ethernet3 | wan_router | site4-wan1 | Ethernet2 |

## Fabric IP Allocation

### Fabric Point-To-Point Links

| Uplink IPv4 Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ---------------- | ------------------- | ------------------ | ------------------ |
| 10.0.1.0/24 | 256 | 24 | 9.38 % |
| 10.0.2.0/24 | 256 | 12 | 4.69 % |
| 10.0.3.0/24 | 256 | 0 | 0.0 % |
| 10.0.4.0/24 | 256 | 4 | 1.57 % |

### Point-To-Point Links Node Allocation

| Node | Node Interface | Node IP Address | Peer Node | Peer Interface | Peer IP Address |
| ---- | -------------- | --------------- | --------- | -------------- | --------------- |
| site1-border1 | Ethernet3 | 10.0.1.8/31 | site1-wan1 | Ethernet1 | 10.0.1.9/31 |
| site1-border1 | Ethernet3.100 | 10.0.1.8/31 | site1-wan1 | Ethernet1.100 | 10.0.1.9/31 |
| site1-border1 | Ethernet3.101 | 10.0.1.8/31 | site1-wan1 | Ethernet1.101 | 10.0.1.9/31 |
| site1-border1 | Ethernet4 | 10.0.1.12/31 | site1-wan2 | Ethernet1 | 10.0.1.13/31 |
| site1-border1 | Ethernet4.100 | 10.0.1.12/31 | site1-wan2 | Ethernet1.100 | 10.0.1.13/31 |
| site1-border1 | Ethernet4.101 | 10.0.1.12/31 | site1-wan2 | Ethernet1.101 | 10.0.1.13/31 |
| site1-border2 | Ethernet3 | 10.0.1.10/31 | site1-wan1 | Ethernet2 | 10.0.1.11/31 |
| site1-border2 | Ethernet3.100 | 10.0.1.10/31 | site1-wan1 | Ethernet2.100 | 10.0.1.11/31 |
| site1-border2 | Ethernet3.101 | 10.0.1.10/31 | site1-wan1 | Ethernet2.101 | 10.0.1.11/31 |
| site1-border2 | Ethernet4 | 10.0.1.14/31 | site1-wan2 | Ethernet2 | 10.0.1.15/31 |
| site1-border2 | Ethernet4.100 | 10.0.1.14/31 | site1-wan2 | Ethernet2.100 | 10.0.1.15/31 |
| site1-border2 | Ethernet4.101 | 10.0.1.14/31 | site1-wan2 | Ethernet2.101 | 10.0.1.15/31 |
| site2-leaf1 | Ethernet3 | 10.0.2.12/31 | site2-wan1 | Ethernet1 | 10.0.2.13/31 |
| site2-leaf1 | Ethernet3.100 | 10.0.2.12/31 | site2-wan1 | Ethernet1.100 | 10.0.2.13/31 |
| site2-leaf1 | Ethernet3.101 | 10.0.2.12/31 | site2-wan1 | Ethernet1.101 | 10.0.2.13/31 |
| site2-leaf2 | Ethernet3 | 10.0.2.14/31 | site2-wan2 | Ethernet1 | 10.0.2.15/31 |
| site2-leaf2 | Ethernet3.100 | 10.0.2.14/31 | site2-wan2 | Ethernet1.100 | 10.0.2.15/31 |
| site2-leaf2 | Ethernet3.101 | 10.0.2.14/31 | site2-wan2 | Ethernet1.101 | 10.0.2.15/31 |
| site4-border1 | Ethernet3 | 10.0.4.56/31 | site4-wan1 | Ethernet1 | 10.0.4.57/31 |
| site4-border2 | Ethernet3 | 10.0.4.58/31 | site4-wan1 | Ethernet2 | 10.0.4.59/31 |

### Loopback Interfaces (BGP EVPN Peering)

| Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ------------- | ------------------- | ------------------ | ------------------ |
| 172.31.255.0/24 | 256 | 2 | 0.79 % |
| 192.168.255.0/24 | 256 | 14 | 5.47 % |

### Loopback0 Interfaces Node Allocation

| POD | Node | Loopback0 |
| --- | ---- | --------- |
| WAN | inet-cloud | 172.31.255.23/32 |
| WAN | mpls-cloud | 172.31.255.22/32 |
| WAN | pf1 | 192.168.255.1/32 |
| WAN | pf2 | 192.168.255.2/32 |
| WAN | site1-border1 | 192.168.255.5/32 |
| WAN | site1-border2 | 192.168.255.6/32 |
| WAN | site1-wan1 | 192.168.255.3/32 |
| WAN | site1-wan2 | 192.168.255.4/32 |
| WAN | site2-leaf1 | 192.168.255.9/32 |
| WAN | site2-leaf2 | 192.168.255.10/32 |
| WAN | site2-wan1 | 192.168.255.7/32 |
| WAN | site2-wan2 | 192.168.255.8/32 |
| WAN | site3-wan1 | 192.168.255.11/32 |
| WAN | site4-border1 | 192.168.255.13/32 |
| WAN | site4-border2 | 192.168.255.14/32 |
| WAN | site4-wan1 | 192.168.255.15/32 |

### VRF Summary

| VRF | RD Pattern | Import RT | Export RT | Nodes |
| --- | ---------- | --------- | --------- | ----- |
| BLUE | 100 | 100:100 | 100:100 | site1-border1, site1-border2, site1-wan1, site1-wan2, site2-leaf1, site2-leaf2, site2-wan1, site2-wan2, site3-wan1, site4-border1, site4-border2, site4-wan1 |
| RED | 101 | 101:101 | 101:101 | site1-border1, site1-border2, site1-wan1, site1-wan2, site2-leaf1, site2-leaf2, site2-wan1, site2-wan2, site3-wan1, site4-border1, site4-border2, site4-wan1 |

### BGP Peer Groups

| Peer Group | Remote AS | Update Source | BFD | Send Community | Nodes |
| ---------- | --------- | ------------- | --- | -------------- | ----- |
| EVPN-OVERLAY-PEERS | - | Loopback0 | Yes | all | site4-border1, site4-wan1 |
| IPv4-UNDERLAY-PEERS | - | - | No | all | site1-border1, site1-border2, site1-wan1, site1-wan2, site2-leaf1, site2-leaf2, site2-wan1, site2-wan2, site4-border1, site4-border2, site4-wan1 |
| MLAG-IPv4-UNDERLAY-PEER | 65101 | - | No | all | site1-border1, site1-border2, site2-leaf1, site2-leaf2, site4-border1, site4-border2 |
| WAN-OVERLAY-PEERS | 65000 | Dps1 | Yes | all | pf1, pf2, site1-wan1, site1-wan2, site2-wan1, site2-wan2, site3-wan1, site4-wan1 |
| WAN-RR-OVERLAY-PEERS | 65000 | Dps1 | Yes | all | pf1, pf2 |

### BGP Neighbors

| Node | Type | Neighbor IP | Peer Group | Remote AS | Description |
| ---- | ---- | ----------- | ---------- | --------- | ----------- |
| inet-cloud | spine | 100.64.21.2 | - | 65000 | - |
| pf1 | wan_rr | 192.168.42.2 | WAN-RR-OVERLAY-PEERS | - | pf2_Dps1 |
| pf2 | wan_rr | 192.168.42.1 | WAN-RR-OVERLAY-PEERS | - | pf1_Dps1 |
| site1-border1 | l3leaf | 10.255.251.9 | MLAG-IPv4-UNDERLAY-PEER | - | site1-border2_Vlan4093 |
| site1-border1 | l3leaf | 10.0.1.9 | IPv4-UNDERLAY-PEERS | 65000 | site1-wan1_Ethernet1 |
| site1-border1 | l3leaf | 10.0.1.13 | IPv4-UNDERLAY-PEERS | 65000 | site1-wan2_Ethernet1 |
| site1-border2 | l3leaf | 10.255.251.8 | MLAG-IPv4-UNDERLAY-PEER | - | site1-border1_Vlan4093 |
| site1-border2 | l3leaf | 10.0.1.11 | IPv4-UNDERLAY-PEERS | 65000 | site1-wan1_Ethernet2 |
| site1-border2 | l3leaf | 10.0.1.15 | IPv4-UNDERLAY-PEERS | 65000 | site1-wan2_Ethernet2 |
| site1-wan1 | wan_router | 10.0.1.8 | IPv4-UNDERLAY-PEERS | 65101 | site1-border1_Ethernet3 |
| site1-wan1 | wan_router | 10.0.1.10 | IPv4-UNDERLAY-PEERS | 65101 | site1-border2_Ethernet3 |
| site1-wan1 | wan_router | 192.168.42.1 | WAN-OVERLAY-PEERS | - | pf1_Dps1 |
| site1-wan1 | wan_router | 192.168.42.2 | WAN-OVERLAY-PEERS | - | pf2_Dps1 |
| site1-wan1 | wan_router | 192.168.42.4 | - | 65000 | site1-wan2 |
| site1-wan2 | wan_router | 10.0.1.12 | IPv4-UNDERLAY-PEERS | 65101 | site1-border1_Ethernet4 |
| site1-wan2 | wan_router | 10.0.1.14 | IPv4-UNDERLAY-PEERS | 65101 | site1-border2_Ethernet4 |
| site1-wan2 | wan_router | 192.168.42.1 | WAN-OVERLAY-PEERS | - | pf1_Dps1 |
| site1-wan2 | wan_router | 192.168.42.2 | WAN-OVERLAY-PEERS | - | pf2_Dps1 |
| site1-wan2 | wan_router | 192.168.42.3 | - | 65000 | site1-wan1 |
| site2-leaf1 | l3leaf | 10.255.251.17 | MLAG-IPv4-UNDERLAY-PEER | - | site2-leaf2_Vlan4093 |
| site2-leaf1 | l3leaf | 10.0.2.13 | IPv4-UNDERLAY-PEERS | 65000 | site2-wan1_Ethernet1 |
| site2-leaf2 | l3leaf | 10.255.251.16 | MLAG-IPv4-UNDERLAY-PEER | - | site2-leaf1_Vlan4093 |
| site2-leaf2 | l3leaf | 10.0.2.15 | IPv4-UNDERLAY-PEERS | 65000 | site2-wan2_Ethernet1 |
| site2-wan1 | wan_router | 10.0.2.12 | IPv4-UNDERLAY-PEERS | 65102 | site2-leaf1_Ethernet3 |
| site2-wan1 | wan_router | 192.168.42.1 | WAN-OVERLAY-PEERS | - | pf1_Dps1 |
| site2-wan1 | wan_router | 192.168.42.2 | WAN-OVERLAY-PEERS | - | pf2_Dps1 |
| site2-wan1 | wan_router | 192.168.42.8 | - | 65000 | site2-wan2 |
| site2-wan2 | wan_router | 100.64.21.1 | - | 65666 | REGION2-INTERNET-CORP_inet-site2-wan2_inet-cloud_Ethernet7 |
| site2-wan2 | wan_router | 10.0.2.14 | IPv4-UNDERLAY-PEERS | 65102 | site2-leaf2_Ethernet3 |
| site2-wan2 | wan_router | 192.168.42.1 | WAN-OVERLAY-PEERS | - | pf1_Dps1 |
| site2-wan2 | wan_router | 192.168.42.2 | WAN-OVERLAY-PEERS | - | pf2_Dps1 |
| site2-wan2 | wan_router | 192.168.42.7 | - | 65000 | site2-wan1 |
| site3-wan1 | wan_router | 192.168.42.1 | WAN-OVERLAY-PEERS | - | pf1_Dps1 |
| site3-wan1 | wan_router | 192.168.42.2 | WAN-OVERLAY-PEERS | - | pf2_Dps1 |
| site4-border1 | l3leaf | 10.255.251.25 | MLAG-IPv4-UNDERLAY-PEER | - | site4-border2_Vlan4093 |
| site4-border1 | l3leaf | 10.0.4.57 | IPv4-UNDERLAY-PEERS | 65000 | site4-wan1_Ethernet1 |
| site4-border1 | l3leaf | 192.168.255.15 | EVPN-OVERLAY-PEERS | 65000 | site4-wan1_Loopback0 |
| site4-border2 | l3leaf | 10.255.251.24 | MLAG-IPv4-UNDERLAY-PEER | - | site4-border1_Vlan4093 |
| site4-border2 | l3leaf | 10.0.4.59 | IPv4-UNDERLAY-PEERS | 65000 | site4-wan1_Ethernet2 |
| site4-wan1 | wan_router | 10.0.4.56 | IPv4-UNDERLAY-PEERS | 65104 | site4-border1_Ethernet3 |
| site4-wan1 | wan_router | 10.0.4.58 | IPv4-UNDERLAY-PEERS | 65104 | site4-border2_Ethernet3 |
| site4-wan1 | wan_router | 192.168.255.13 | EVPN-OVERLAY-PEERS | 65104 | site4-border1_Loopback0 |
| site4-wan1 | wan_router | 192.168.42.1 | WAN-OVERLAY-PEERS | - | pf1_Dps1 |
| site4-wan1 | wan_router | 192.168.42.2 | WAN-OVERLAY-PEERS | - | pf2_Dps1 |

### VRF Routing Protocols

| Node | Type | VRF | Router ID | Redistribute |
| ---- | ---- | --- | --------- | ------------ |
| site1-border1 | l3leaf | BLUE | 192.168.255.5 | connected |
| site1-border1 | l3leaf | RED | 192.168.255.5 | connected |
| site1-border2 | l3leaf | BLUE | 192.168.255.6 | connected |
| site1-border2 | l3leaf | RED | 192.168.255.6 | connected |
| site1-wan1 | wan_router | BLUE | 192.168.255.3 | connected |
| site1-wan1 | wan_router | RED | 192.168.255.3 | connected |
| site1-wan2 | wan_router | BLUE | 192.168.255.4 | connected |
| site1-wan2 | wan_router | RED | 192.168.255.4 | connected |
| site2-leaf1 | l3leaf | BLUE | 192.168.255.9 | connected |
| site2-leaf1 | l3leaf | RED | 192.168.255.9 | connected |
| site2-leaf2 | l3leaf | BLUE | 192.168.255.10 | connected |
| site2-leaf2 | l3leaf | RED | 192.168.255.10 | connected |
| site2-wan1 | wan_router | BLUE | 192.168.255.7 | connected |
| site2-wan1 | wan_router | RED | 192.168.255.7 | connected |
| site2-wan2 | wan_router | BLUE | 192.168.255.8 | connected |
| site2-wan2 | wan_router | RED | 192.168.255.8 | connected |
| site3-wan1 | wan_router | BLUE | 192.168.255.11 | connected |
| site3-wan1 | wan_router | RED | 192.168.255.11 | connected |
| site4-border1 | l3leaf | BLUE | 192.168.255.13 | connected |
| site4-border1 | l3leaf | RED | 192.168.255.13 | connected |
| site4-border2 | l3leaf | BLUE | 192.168.255.14 | connected |
| site4-border2 | l3leaf | RED | 192.168.255.14 | connected |
| site4-wan1 | wan_router | BLUE | 192.168.255.15 | connected |
| site4-wan1 | wan_router | RED | 192.168.255.15 | connected |

### VTEP Loopback VXLAN Tunnel Source Interfaces (VTEPs Only)

| VTEP Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ------------------ | ------------------- | ------------------ | ------------------ |
| 192.168.42.0/24 | 256 | 6 | 2.35 % |

### VTEP Loopback Node allocation

| POD | Node | Loopback1 |
| --- | ---- | --------- |
| WAN | site1-border1 | 192.168.42.5/32 |
| WAN | site1-border2 | 192.168.42.5/32 |
| WAN | site2-leaf1 | 192.168.42.9/32 |
| WAN | site2-leaf2 | 192.168.42.9/32 |
| WAN | site4-border1 | 192.168.42.13/32 |
| WAN | site4-border2 | 192.168.42.13/32 |
