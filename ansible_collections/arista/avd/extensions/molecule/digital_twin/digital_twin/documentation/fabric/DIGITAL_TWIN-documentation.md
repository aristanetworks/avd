# DIGITAL_TWIN

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
| DIGITAL_TWIN | l2leaf | digital-twin-adjust-oob-mgmt-1 | 192.168.1.1/32 | vEOS-lab | Provisioned | - |
| DIGITAL_TWIN | l2leaf | digital-twin-adjust-oob-mgmt-2 | 192.168.1.2/32 | vEOS-lab | Provisioned | - |
| DIGITAL_TWIN | l2leaf | digital-twin-adjust-oob-mgmt-3 | - | vEOS-lab | Provisioned | - |
| DIGITAL_TWIN | l2leaf | digital-twin-adjust-oob-mgmt-4 | 192.168.1.4/32 | custom-platform | Provisioned | - |
| DIGITAL_TWIN | l2spine | digital-twin-default-interfaces-digital-twin-platform | 10.10.10.100/24 | vEOS-lab | Provisioned | - |
| DIGITAL_TWIN | l2leaf | digital-twin-default-interfaces-original-platform | 10.10.10.101/24 | vEOS-lab | Provisioned | - |
| DIGITAL_TWIN | l2leaf | digital-twin-enforce-eapi-1 | 192.168.0.1/32 | vEOS-lab | Provisioned | - |
| DIGITAL_TWIN | l2leaf | digital-twin-enforce-eapi-2 | 192.168.0.2/32 | vEOS-lab | Provisioned | - |
| DIGITAL_TWIN | l2leaf | digital-twin-enforce-eapi-3 | 192.168.0.3/32 | vEOS-lab | Provisioned | - |
| DIGITAL_TWIN | l2leaf | digital-twin-enforce-eapi-4 | 192.168.0.4/32 | vEOS-lab | Provisioned | - |
| DIGITAL_TWIN | l3leaf | digital-twin-ethernet-ports-1 | 192.169.3.1/32 | vEOS-lab | Provisioned | - |
| DIGITAL_TWIN | l3leaf | digital-twin-ethernet-ports-3 | 192.169.3.3/32 | custom-platform | Provisioned | - |
| DIGITAL_TWIN | l2leaf | digital-twin-veos-no-mgmt | - | vEOS-lab | Provisioned | - |
| DIGITAL_TWIN | l3leaf | digital.twin.ethernet.ports.2 | 192.169.3.2/32 | vEOS-lab | Provisioned | - |

> Provision status is based on Ansible inventory declaration and do not represent real status from CloudVision.

### Fabric Switches with inband Management IP

| POD | Type | Node | Management IP | Inband Interface |
| --- | ---- | ---- | ------------- | ---------------- |
| DIGITAL_TWIN | l2leaf | digital-twin-adjust-oob-mgmt-3 | 192.168.1.3/32 | Vlan4092 |

## Fabric Topology

| Type | Node | Node Interface | Peer Type | Peer Node | Peer Interface |
| ---- | ---- | -------------- | --------- | --------- | -------------- |
| l2spine | digital-twin-default-interfaces-digital-twin-platform | Ethernet3 | l2leaf | digital-twin-default-interfaces-original-platform | Ethernet2 |
| l3leaf | digital-twin-ethernet-ports-1 | Ethernet3 | l3leaf | digital.twin.ethernet.ports.2 | Ethernet3 |
| l3leaf | digital-twin-ethernet-ports-1 | Ethernet4 | mlag_peer | digital.twin.ethernet.ports.2 | Ethernet4 |
| l3leaf | digital-twin-ethernet-ports-1 | Ethernet5 | mlag_peer | digital.twin.ethernet.ports.2 | Ethernet5 |
| l3leaf | digital-twin-ethernet-ports-1 | Ethernet6 | l3leaf | digital-twin-ethernet-ports-3 | Ethernet6 |
| l3leaf | digital-twin-ethernet-ports-1 | Ethernet11 | l3leaf | digital.twin.ethernet.ports.2 | Ethernet11 |
| l3leaf | digital-twin-ethernet-ports-1 | Ethernet11.100 | l3leaf | digital.twin.ethernet.ports.2 | Ethernet11.100 |
| l3leaf | digital-twin-ethernet-ports-1 | Ethernet11.101 | l3leaf | digital.twin.ethernet.ports.2 | Ethernet11.101 |
| l3leaf | digital-twin-ethernet-ports-1 | Ethernet14 | l3leaf | digital.twin.ethernet.ports.2 | Ethernet14 |

## Fabric IP Allocation

### Fabric Point-To-Point Links

| Uplink IPv4 Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ---------------- | ------------------- | ------------------ | ------------------ |
| 192.168.3.112/28 | 16 | 4 | 25.0 % |

### Point-To-Point Links Node Allocation

| Node | Node Interface | Node IP Address | Peer Node | Peer Interface | Peer IP Address |
| ---- | -------------- | --------------- | --------- | -------------- | --------------- |
| digital-twin-ethernet-ports-1 | Ethernet3 | 192.168.3.114/31 | digital.twin.ethernet.ports.2 | Ethernet3 | 192.168.3.115/31 |
| digital-twin-ethernet-ports-1 | Ethernet6 | 192.168.3.112/31 | digital-twin-ethernet-ports-3 | Ethernet6 | 192.168.3.113/31 |
| digital-twin-ethernet-ports-1 | Ethernet11 | 192.168.3.184/31 | digital.twin.ethernet.ports.2 | Ethernet11 | 192.168.3.185/31 |
| digital-twin-ethernet-ports-1 | Ethernet11.100 | 192.168.3.186/31 | digital.twin.ethernet.ports.2 | Ethernet11.100 | 192.168.3.187/31 |
| digital-twin-ethernet-ports-1 | Ethernet11.101 | 192.168.3.188/31 | digital.twin.ethernet.ports.2 | Ethernet11.101 | 192.168.3.189/31 |

### Loopback Interfaces (BGP EVPN Peering)

| Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ------------- | ------------------- | ------------------ | ------------------ |
| 192.168.3.128/28 | 16 | 3 | 18.75 % |

### Loopback0 Interfaces Node Allocation

| POD | Node | Loopback0 |
| --- | ---- | --------- |
| DIGITAL_TWIN | digital-twin-ethernet-ports-1 | 192.168.3.129/32 |
| DIGITAL_TWIN | digital-twin-ethernet-ports-3 | 192.168.3.129/32 |
| DIGITAL_TWIN | digital.twin.ethernet.ports.2 | 192.168.3.130/32 |

### VTEP Loopback VXLAN Tunnel Source Interfaces (VTEPs Only)

| VTEP Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ------------------ | ------------------- | ------------------ | ------------------ |
| 192.168.3.144/28 | 16 | 3 | 18.75 % |

### VTEP Loopback Node allocation

| POD | Node | Loopback1 |
| --- | ---- | --------- |
| DIGITAL_TWIN | digital-twin-ethernet-ports-1 | 192.168.3.145/32 |
| DIGITAL_TWIN | digital-twin-ethernet-ports-3 | 192.168.3.145/32 |
| DIGITAL_TWIN | digital.twin.ethernet.ports.2 | 192.168.3.145/32 |
