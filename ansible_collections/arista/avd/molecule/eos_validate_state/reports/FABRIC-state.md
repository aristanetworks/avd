# Validate State Report

**Table of Contents:**

- [Validate State Report](validate-state-report)
  - [Test Results Summary](#test-results-summary)
  - [Failed Test Results Summary](#failed-test-results-summary)
  - [All Test Results](#all-test-results)

## Test Results Summary

### Summary Totals

| Total Tests | Total Tests Passed | Total Tests Failed | Total Tests Skipped |
| ----------- | ------------------ | ------------------ | ------------------- |
| 620 | 0 | 0 | 620 |

### Summary Totals Devices Under Tests

| DUT | Total Tests | Tests Passed | Tests Failed | Tests Skipped | Categories Failed | Categories Skipped |
| --- | ----------- | ------------ | ------------ | ------------- | ----------------- | ------------------ |
| dc1-leaf1a | 67 | 0 | 0 | 67 |  | BGP, Hardware, IP Reachability, Interface State, LLDP Topology, Loopback0 Reachability, MLAG, NTP, Routing Table |
| dc1-leaf1b | 67 | 0 | 0 | 67 |  | BGP, Hardware, IP Reachability, Interface State, LLDP Topology, Loopback0 Reachability, MLAG, NTP, Routing Table |
| dc1-leaf1c | 11 | 0 | 0 | 11 |  | Hardware, Interface State, LLDP Topology, NTP |
| dc1-leaf2a | 69 | 0 | 0 | 69 |  | BGP, Hardware, IP Reachability, Interface State, LLDP Topology, Loopback0 Reachability, MLAG, NTP, Routing Table |
| dc1-leaf2c | 10 | 0 | 0 | 10 |  | Hardware, Interface State, LLDP Topology, NTP |
| dc1-spine1 | 23 | 0 | 0 | 23 |  | BGP, Hardware, IP Reachability, Interface State, LLDP Topology, NTP |
| dc1-spine2 | 23 | 0 | 0 | 23 |  | BGP, Hardware, IP Reachability, Interface State, LLDP Topology, NTP |
| dc2-leaf1a | 67 | 0 | 0 | 67 |  | BGP, Hardware, IP Reachability, Interface State, LLDP Topology, Loopback0 Reachability, MLAG, NTP, Routing Table |
| dc2-leaf1b | 67 | 0 | 0 | 67 |  | BGP, Hardware, IP Reachability, Interface State, LLDP Topology, Loopback0 Reachability, MLAG, NTP, Routing Table |
| dc2-leaf1c | 11 | 0 | 0 | 11 |  | Hardware, Interface State, LLDP Topology, NTP |
| dc2-leaf2a | 72 | 0 | 0 | 72 |  | BGP, Hardware, IP Reachability, Interface State, LLDP Topology, Loopback0 Reachability, MLAG, NTP, Routing Table |
| dc2-leaf2b | 68 | 0 | 0 | 68 |  | BGP, Hardware, IP Reachability, Interface State, LLDP Topology, Loopback0 Reachability, MLAG, NTP, Routing Table |
| dc2-leaf2c | 11 | 0 | 0 | 11 |  | Hardware, Interface State, LLDP Topology, NTP |
| dc2-spine1 | 27 | 0 | 0 | 27 |  | BGP, Hardware, IP Reachability, Interface State, LLDP Topology, NTP |
| dc2-spine2 | 27 | 0 | 0 | 27 |  | BGP, Hardware, IP Reachability, Interface State, LLDP Topology, NTP |

### Summary Totals Per Category

| Test Category | Total Tests | Tests Passed | Tests Failed | Tests Skipped |
| ------------- | ----------- | ------------ | ------------ | ------------- |
| BGP | 77 | 0 | 0 | 77 |
| Hardware | 60 | 0 | 0 | 60 |
| IP Reachability | 30 | 0 | 0 | 30 |
| Interface State | 193 | 0 | 0 | 193 |
| LLDP Topology | 56 | 0 | 0 | 56 |
| Loopback0 Reachability | 77 | 0 | 0 | 77 |
| MLAG | 7 | 0 | 0 | 7 |
| NTP | 15 | 0 | 0 | 15 |
| Routing Table | 105 | 0 | 0 | 105 |

## Failed Test Results Summary

| Test ID | Node | Test Category | Test Description | Test | Test Result | Failure Reasons |
| ------- | ---- | ------------- | ---------------- | ---- | ----------- | --------------- |

## All Test Results

| Test ID | Node | Test Category | Test Description | Test | Test Result | Failure Reasons |
| ------- | ---- | ------------- | ---------------- | ---- | ----------- | --------------- |
| 1 | dc1-leaf1a | BGP | ArBGP is configured and operating | ArBGP | SKIPPED | Dry run! |
| 2 | dc1-leaf1a | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.255.0.1 | SKIPPED | Dry run! |
| 3 | dc1-leaf1a | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.255.0.2 | SKIPPED | Dry run! |
| 4 | dc1-leaf1a | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.255.1.97 | SKIPPED | Dry run! |
| 5 | dc1-leaf1a | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.255.255.0 | SKIPPED | Dry run! |
| 6 | dc1-leaf1a | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.255.255.2 | SKIPPED | Dry run! |
| 7 | dc1-leaf1a | Hardware | Verifies if the power supplies status are within the accepted states list. | VerifyEnvironmentPower | SKIPPED | Dry run! |
| 8 | dc1-leaf1a | Hardware | Verifies if the fans status are within the accepted states list. | VerifyEnvironmentCooling | SKIPPED | Dry run! |
| 9 | dc1-leaf1a | Hardware | Verifies if the device temperature is within the acceptable range. | VerifyTemperature | SKIPPED | Dry run! |
| 10 | dc1-leaf1a | Hardware | Verifies the transceiver's manufacturer against a list of approved manufacturers. | VerifyTransceiversManufacturers | SKIPPED | Dry run! |
| 11 | dc1-leaf1a | IP Reachability | ip reachability test p2p links | Source: dc1-leaf1a_Ethernet1 - Destination: dc1-spine1_Ethernet1 | SKIPPED | Dry run! |
| 12 | dc1-leaf1a | IP Reachability | ip reachability test p2p links | Source: dc1-leaf1a_Ethernet2 - Destination: dc1-spine2_Ethernet1 | SKIPPED | Dry run! |
| 13 | dc1-leaf1a | Interface State | Ethernet Interface & Line Protocol == \"up\" | Ethernet1 - P2P_LINK_TO_DC1-SPINE1_Ethernet1 | SKIPPED | Dry run! |
| 14 | dc1-leaf1a | Interface State | Ethernet Interface & Line Protocol == \"up\" | Ethernet2 - P2P_LINK_TO_DC1-SPINE2_Ethernet1 | SKIPPED | Dry run! |
| 15 | dc1-leaf1a | Interface State | Ethernet Interface & Line Protocol == \"up\" | Ethernet3 - MLAG_PEER_dc1-leaf1b_Ethernet3 | SKIPPED | Dry run! |
| 16 | dc1-leaf1a | Interface State | Ethernet Interface & Line Protocol == \"up\" | Ethernet4 - MLAG_PEER_dc1-leaf1b_Ethernet4 | SKIPPED | Dry run! |
| 17 | dc1-leaf1a | Interface State | Ethernet Interface & Line Protocol == \"up\" | Ethernet5 - dc1-leaf1-server1_PCI1 | SKIPPED | Dry run! |
| 18 | dc1-leaf1a | Interface State | Ethernet Interface & Line Protocol == \"up\" | Ethernet8 - DC1-LEAF1C_Ethernet1 | SKIPPED | Dry run! |
| 19 | dc1-leaf1a | Interface State | Loopback Interface Status & Line Protocol == \"up\" | Loopback0 - EVPN_Overlay_Peering | SKIPPED | Dry run! |
| 20 | dc1-leaf1a | Interface State | Loopback Interface Status & Line Protocol == \"up\" | Loopback1 - VTEP_VXLAN_Tunnel_Source | SKIPPED | Dry run! |
| 21 | dc1-leaf1a | Interface State | Loopback Interface Status & Line Protocol == \"up\" | Loopback10 - VRF10_VTEP_DIAGNOSTICS | SKIPPED | Dry run! |
| 22 | dc1-leaf1a | Interface State | Loopback Interface Status & Line Protocol == \"up\" | Loopback11 - VRF11_VTEP_DIAGNOSTICS | SKIPPED | Dry run! |
| 23 | dc1-leaf1a | Interface State | Port-Channel Interface & Line Protocol == \"up\" | Port-Channel3 - MLAG_PEER_dc1-leaf1b_Po3 | SKIPPED | Dry run! |
| 24 | dc1-leaf1a | Interface State | Port-Channel Interface & Line Protocol == \"up\" | Port-Channel5 - dc1-leaf1-server1_PortChannel dc1-leaf1-server1 | SKIPPED | Dry run! |
| 25 | dc1-leaf1a | Interface State | Port-Channel Interface & Line Protocol == \"up\" | Port-Channel8 - DC1-LEAF1C_Po1 | SKIPPED | Dry run! |
| 26 | dc1-leaf1a | Interface State | Vlan Interface & Line Protocol == \"up\" | Vlan11 - VRF10_VLAN11 | SKIPPED | Dry run! |
| 27 | dc1-leaf1a | Interface State | Vlan Interface & Line Protocol == \"up\" | Vlan12 - VRF10_VLAN12 | SKIPPED | Dry run! |
| 28 | dc1-leaf1a | Interface State | Vlan Interface & Line Protocol == \"up\" | Vlan21 - VRF11_VLAN21 | SKIPPED | Dry run! |
| 29 | dc1-leaf1a | Interface State | Vlan Interface & Line Protocol == \"up\" | Vlan22 - VRF11_VLAN22 | SKIPPED | Dry run! |
| 30 | dc1-leaf1a | Interface State | Vlan Interface & Line Protocol == \"up\" | Vlan3009 - MLAG_PEER_L3_iBGP: vrf VRF10 | SKIPPED | Dry run! |
| 31 | dc1-leaf1a | Interface State | Vlan Interface & Line Protocol == \"up\" | Vlan3010 - MLAG_PEER_L3_iBGP: vrf VRF11 | SKIPPED | Dry run! |
| 32 | dc1-leaf1a | Interface State | Vlan Interface & Line Protocol == \"up\" | Vlan4093 - MLAG_PEER_L3_PEERING | SKIPPED | Dry run! |
| 33 | dc1-leaf1a | Interface State | Vlan Interface & Line Protocol == \"up\" | Vlan4094 - MLAG_PEER | SKIPPED | Dry run! |
| 34 | dc1-leaf1a | Interface State | Vxlan Interface Status & Line Protocol == \"up\" | Vxlan1 | SKIPPED | Dry run! |
| 35 | dc1-leaf1a | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet1 - remote: dc1-spine1_Ethernet1 | SKIPPED | Dry run! |
| 36 | dc1-leaf1a | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet2 - remote: dc1-spine2_Ethernet1 | SKIPPED | Dry run! |
| 37 | dc1-leaf1a | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet3 - remote: dc1-leaf1b_Ethernet3 | SKIPPED | Dry run! |
| 38 | dc1-leaf1a | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet4 - remote: dc1-leaf1b_Ethernet4 | SKIPPED | Dry run! |
| 39 | dc1-leaf1a | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet8 - remote: dc1-leaf1c_Ethernet1 | SKIPPED | Dry run! |
| 40 | dc1-leaf1a | Loopback0 Reachability | Loopback0 Reachability | Source: dc1-leaf1a - 10.255.0.3/32 Destination: 10.255.0.1 | SKIPPED | Dry run! |
| 41 | dc1-leaf1a | Loopback0 Reachability | Loopback0 Reachability | Source: dc1-leaf1a - 10.255.0.3/32 Destination: 10.255.0.2 | SKIPPED | Dry run! |
| 42 | dc1-leaf1a | Loopback0 Reachability | Loopback0 Reachability | Source: dc1-leaf1a - 10.255.0.3/32 Destination: 10.255.0.3 | SKIPPED | Dry run! |
| 43 | dc1-leaf1a | Loopback0 Reachability | Loopback0 Reachability | Source: dc1-leaf1a - 10.255.0.3/32 Destination: 10.255.0.4 | SKIPPED | Dry run! |
| 44 | dc1-leaf1a | Loopback0 Reachability | Loopback0 Reachability | Source: dc1-leaf1a - 10.255.0.3/32 Destination: 10.255.0.5 | SKIPPED | Dry run! |
| 45 | dc1-leaf1a | Loopback0 Reachability | Loopback0 Reachability | Source: dc1-leaf1a - 10.255.0.3/32 Destination: 10.255.128.11 | SKIPPED | Dry run! |
| 46 | dc1-leaf1a | Loopback0 Reachability | Loopback0 Reachability | Source: dc1-leaf1a - 10.255.0.3/32 Destination: 10.255.128.12 | SKIPPED | Dry run! |
| 47 | dc1-leaf1a | Loopback0 Reachability | Loopback0 Reachability | Source: dc1-leaf1a - 10.255.0.3/32 Destination: 10.255.128.13 | SKIPPED | Dry run! |
| 48 | dc1-leaf1a | Loopback0 Reachability | Loopback0 Reachability | Source: dc1-leaf1a - 10.255.0.3/32 Destination: 10.255.128.14 | SKIPPED | Dry run! |
| 49 | dc1-leaf1a | Loopback0 Reachability | Loopback0 Reachability | Source: dc1-leaf1a - 10.255.0.3/32 Destination: 10.255.128.15 | SKIPPED | Dry run! |
| 50 | dc1-leaf1a | Loopback0 Reachability | Loopback0 Reachability | Source: dc1-leaf1a - 10.255.0.3/32 Destination: 10.255.128.16 | SKIPPED | Dry run! |
| 51 | dc1-leaf1a | MLAG | MLAG State active & Status connected | MLAG | SKIPPED | Dry run! |
| 52 | dc1-leaf1a | NTP | Synchronised with NTP server | NTP | SKIPPED | Dry run! |
| 53 | dc1-leaf1a | Routing Table | Remote Lo0 address | 10.255.0.1 | SKIPPED | Dry run! |
| 54 | dc1-leaf1a | Routing Table | Remote Lo0 address | 10.255.0.2 | SKIPPED | Dry run! |
| 55 | dc1-leaf1a | Routing Table | Remote Lo0 address | 10.255.0.3 | SKIPPED | Dry run! |
| 56 | dc1-leaf1a | Routing Table | Remote Lo0 address | 10.255.0.4 | SKIPPED | Dry run! |
| 57 | dc1-leaf1a | Routing Table | Remote Lo0 address | 10.255.0.5 | SKIPPED | Dry run! |
| 58 | dc1-leaf1a | Routing Table | Remote VTEP address | 10.255.1.3 | SKIPPED | Dry run! |
| 59 | dc1-leaf1a | Routing Table | Remote VTEP address | 10.255.1.5 | SKIPPED | Dry run! |
| 60 | dc1-leaf1a | Routing Table | Remote Lo0 address | 10.255.128.11 | SKIPPED | Dry run! |
| 61 | dc1-leaf1a | Routing Table | Remote Lo0 address | 10.255.128.12 | SKIPPED | Dry run! |
| 62 | dc1-leaf1a | Routing Table | Remote Lo0 address | 10.255.128.13 | SKIPPED | Dry run! |
| 63 | dc1-leaf1a | Routing Table | Remote Lo0 address | 10.255.128.14 | SKIPPED | Dry run! |
| 64 | dc1-leaf1a | Routing Table | Remote Lo0 address | 10.255.128.15 | SKIPPED | Dry run! |
| 65 | dc1-leaf1a | Routing Table | Remote Lo0 address | 10.255.128.16 | SKIPPED | Dry run! |
| 66 | dc1-leaf1a | Routing Table | Remote VTEP address | 10.255.129.13 | SKIPPED | Dry run! |
| 67 | dc1-leaf1a | Routing Table | Remote VTEP address | 10.255.129.15 | SKIPPED | Dry run! |
| 68 | dc1-leaf1b | BGP | ArBGP is configured and operating | ArBGP | SKIPPED | Dry run! |
| 69 | dc1-leaf1b | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.255.0.1 | SKIPPED | Dry run! |
| 70 | dc1-leaf1b | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.255.0.2 | SKIPPED | Dry run! |
| 71 | dc1-leaf1b | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.255.1.96 | SKIPPED | Dry run! |
| 72 | dc1-leaf1b | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.255.255.4 | SKIPPED | Dry run! |
| 73 | dc1-leaf1b | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.255.255.6 | SKIPPED | Dry run! |
| 74 | dc1-leaf1b | Hardware | Verifies if the power supplies status are within the accepted states list. | VerifyEnvironmentPower | SKIPPED | Dry run! |
| 75 | dc1-leaf1b | Hardware | Verifies if the fans status are within the accepted states list. | VerifyEnvironmentCooling | SKIPPED | Dry run! |
| 76 | dc1-leaf1b | Hardware | Verifies if the device temperature is within the acceptable range. | VerifyTemperature | SKIPPED | Dry run! |
| 77 | dc1-leaf1b | Hardware | Verifies the transceiver's manufacturer against a list of approved manufacturers. | VerifyTransceiversManufacturers | SKIPPED | Dry run! |
| 78 | dc1-leaf1b | IP Reachability | ip reachability test p2p links | Source: dc1-leaf1b_Ethernet1 - Destination: dc1-spine1_Ethernet2 | SKIPPED | Dry run! |
| 79 | dc1-leaf1b | IP Reachability | ip reachability test p2p links | Source: dc1-leaf1b_Ethernet2 - Destination: dc1-spine2_Ethernet2 | SKIPPED | Dry run! |
| 80 | dc1-leaf1b | Interface State | Ethernet Interface & Line Protocol == \"up\" | Ethernet1 - P2P_LINK_TO_DC1-SPINE1_Ethernet2 | SKIPPED | Dry run! |
| 81 | dc1-leaf1b | Interface State | Ethernet Interface & Line Protocol == \"up\" | Ethernet2 - P2P_LINK_TO_DC1-SPINE2_Ethernet2 | SKIPPED | Dry run! |
| 82 | dc1-leaf1b | Interface State | Ethernet Interface & Line Protocol == \"up\" | Ethernet3 - MLAG_PEER_dc1-leaf1a_Ethernet3 | SKIPPED | Dry run! |
| 83 | dc1-leaf1b | Interface State | Ethernet Interface & Line Protocol == \"up\" | Ethernet4 - MLAG_PEER_dc1-leaf1a_Ethernet4 | SKIPPED | Dry run! |
| 84 | dc1-leaf1b | Interface State | Ethernet Interface & Line Protocol == \"up\" | Ethernet5 - dc1-leaf1-server1_PCI2 | SKIPPED | Dry run! |
| 85 | dc1-leaf1b | Interface State | Ethernet Interface & Line Protocol == \"up\" | Ethernet8 - DC1-LEAF1C_Ethernet2 | SKIPPED | Dry run! |
| 86 | dc1-leaf1b | Interface State | Loopback Interface Status & Line Protocol == \"up\" | Loopback0 - EVPN_Overlay_Peering | SKIPPED | Dry run! |
| 87 | dc1-leaf1b | Interface State | Loopback Interface Status & Line Protocol == \"up\" | Loopback1 - VTEP_VXLAN_Tunnel_Source | SKIPPED | Dry run! |
| 88 | dc1-leaf1b | Interface State | Loopback Interface Status & Line Protocol == \"up\" | Loopback10 - VRF10_VTEP_DIAGNOSTICS | SKIPPED | Dry run! |
| 89 | dc1-leaf1b | Interface State | Loopback Interface Status & Line Protocol == \"up\" | Loopback11 - VRF11_VTEP_DIAGNOSTICS | SKIPPED | Dry run! |
| 90 | dc1-leaf1b | Interface State | Port-Channel Interface & Line Protocol == \"up\" | Port-Channel3 - MLAG_PEER_dc1-leaf1a_Po3 | SKIPPED | Dry run! |
| 91 | dc1-leaf1b | Interface State | Port-Channel Interface & Line Protocol == \"up\" | Port-Channel5 - dc1-leaf1-server1_PortChannel dc1-leaf1-server1 | SKIPPED | Dry run! |
| 92 | dc1-leaf1b | Interface State | Port-Channel Interface & Line Protocol == \"up\" | Port-Channel8 - DC1-LEAF1C_Po1 | SKIPPED | Dry run! |
| 93 | dc1-leaf1b | Interface State | Vlan Interface & Line Protocol == \"up\" | Vlan11 - VRF10_VLAN11 | SKIPPED | Dry run! |
| 94 | dc1-leaf1b | Interface State | Vlan Interface & Line Protocol == \"up\" | Vlan12 - VRF10_VLAN12 | SKIPPED | Dry run! |
| 95 | dc1-leaf1b | Interface State | Vlan Interface & Line Protocol == \"up\" | Vlan21 - VRF11_VLAN21 | SKIPPED | Dry run! |
| 96 | dc1-leaf1b | Interface State | Vlan Interface & Line Protocol == \"up\" | Vlan22 - VRF11_VLAN22 | SKIPPED | Dry run! |
| 97 | dc1-leaf1b | Interface State | Vlan Interface & Line Protocol == \"up\" | Vlan3009 - MLAG_PEER_L3_iBGP: vrf VRF10 | SKIPPED | Dry run! |
| 98 | dc1-leaf1b | Interface State | Vlan Interface & Line Protocol == \"up\" | Vlan3010 - MLAG_PEER_L3_iBGP: vrf VRF11 | SKIPPED | Dry run! |
| 99 | dc1-leaf1b | Interface State | Vlan Interface & Line Protocol == \"up\" | Vlan4093 - MLAG_PEER_L3_PEERING | SKIPPED | Dry run! |
| 100 | dc1-leaf1b | Interface State | Vlan Interface & Line Protocol == \"up\" | Vlan4094 - MLAG_PEER | SKIPPED | Dry run! |
| 101 | dc1-leaf1b | Interface State | Vxlan Interface Status & Line Protocol == \"up\" | Vxlan1 | SKIPPED | Dry run! |
| 102 | dc1-leaf1b | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet1 - remote: dc1-spine1_Ethernet2 | SKIPPED | Dry run! |
| 103 | dc1-leaf1b | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet2 - remote: dc1-spine2_Ethernet2 | SKIPPED | Dry run! |
| 104 | dc1-leaf1b | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet3 - remote: dc1-leaf1a_Ethernet3 | SKIPPED | Dry run! |
| 105 | dc1-leaf1b | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet4 - remote: dc1-leaf1a_Ethernet4 | SKIPPED | Dry run! |
| 106 | dc1-leaf1b | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet8 - remote: dc1-leaf1c_Ethernet2 | SKIPPED | Dry run! |
| 107 | dc1-leaf1b | Loopback0 Reachability | Loopback0 Reachability | Source: dc1-leaf1b - 10.255.0.4/32 Destination: 10.255.0.1 | SKIPPED | Dry run! |
| 108 | dc1-leaf1b | Loopback0 Reachability | Loopback0 Reachability | Source: dc1-leaf1b - 10.255.0.4/32 Destination: 10.255.0.2 | SKIPPED | Dry run! |
| 109 | dc1-leaf1b | Loopback0 Reachability | Loopback0 Reachability | Source: dc1-leaf1b - 10.255.0.4/32 Destination: 10.255.0.3 | SKIPPED | Dry run! |
| 110 | dc1-leaf1b | Loopback0 Reachability | Loopback0 Reachability | Source: dc1-leaf1b - 10.255.0.4/32 Destination: 10.255.0.4 | SKIPPED | Dry run! |
| 111 | dc1-leaf1b | Loopback0 Reachability | Loopback0 Reachability | Source: dc1-leaf1b - 10.255.0.4/32 Destination: 10.255.0.5 | SKIPPED | Dry run! |
| 112 | dc1-leaf1b | Loopback0 Reachability | Loopback0 Reachability | Source: dc1-leaf1b - 10.255.0.4/32 Destination: 10.255.128.11 | SKIPPED | Dry run! |
| 113 | dc1-leaf1b | Loopback0 Reachability | Loopback0 Reachability | Source: dc1-leaf1b - 10.255.0.4/32 Destination: 10.255.128.12 | SKIPPED | Dry run! |
| 114 | dc1-leaf1b | Loopback0 Reachability | Loopback0 Reachability | Source: dc1-leaf1b - 10.255.0.4/32 Destination: 10.255.128.13 | SKIPPED | Dry run! |
| 115 | dc1-leaf1b | Loopback0 Reachability | Loopback0 Reachability | Source: dc1-leaf1b - 10.255.0.4/32 Destination: 10.255.128.14 | SKIPPED | Dry run! |
| 116 | dc1-leaf1b | Loopback0 Reachability | Loopback0 Reachability | Source: dc1-leaf1b - 10.255.0.4/32 Destination: 10.255.128.15 | SKIPPED | Dry run! |
| 117 | dc1-leaf1b | Loopback0 Reachability | Loopback0 Reachability | Source: dc1-leaf1b - 10.255.0.4/32 Destination: 10.255.128.16 | SKIPPED | Dry run! |
| 118 | dc1-leaf1b | MLAG | MLAG State active & Status connected | MLAG | SKIPPED | Dry run! |
| 119 | dc1-leaf1b | NTP | Synchronised with NTP server | NTP | SKIPPED | Dry run! |
| 120 | dc1-leaf1b | Routing Table | Remote Lo0 address | 10.255.0.1 | SKIPPED | Dry run! |
| 121 | dc1-leaf1b | Routing Table | Remote Lo0 address | 10.255.0.2 | SKIPPED | Dry run! |
| 122 | dc1-leaf1b | Routing Table | Remote Lo0 address | 10.255.0.3 | SKIPPED | Dry run! |
| 123 | dc1-leaf1b | Routing Table | Remote Lo0 address | 10.255.0.4 | SKIPPED | Dry run! |
| 124 | dc1-leaf1b | Routing Table | Remote Lo0 address | 10.255.0.5 | SKIPPED | Dry run! |
| 125 | dc1-leaf1b | Routing Table | Remote VTEP address | 10.255.1.3 | SKIPPED | Dry run! |
| 126 | dc1-leaf1b | Routing Table | Remote VTEP address | 10.255.1.5 | SKIPPED | Dry run! |
| 127 | dc1-leaf1b | Routing Table | Remote Lo0 address | 10.255.128.11 | SKIPPED | Dry run! |
| 128 | dc1-leaf1b | Routing Table | Remote Lo0 address | 10.255.128.12 | SKIPPED | Dry run! |
| 129 | dc1-leaf1b | Routing Table | Remote Lo0 address | 10.255.128.13 | SKIPPED | Dry run! |
| 130 | dc1-leaf1b | Routing Table | Remote Lo0 address | 10.255.128.14 | SKIPPED | Dry run! |
| 131 | dc1-leaf1b | Routing Table | Remote Lo0 address | 10.255.128.15 | SKIPPED | Dry run! |
| 132 | dc1-leaf1b | Routing Table | Remote Lo0 address | 10.255.128.16 | SKIPPED | Dry run! |
| 133 | dc1-leaf1b | Routing Table | Remote VTEP address | 10.255.129.13 | SKIPPED | Dry run! |
| 134 | dc1-leaf1b | Routing Table | Remote VTEP address | 10.255.129.15 | SKIPPED | Dry run! |
| 135 | dc1-leaf1c | Hardware | Verifies if the power supplies status are within the accepted states list. | VerifyEnvironmentPower | SKIPPED | Dry run! |
| 136 | dc1-leaf1c | Hardware | Verifies if the fans status are within the accepted states list. | VerifyEnvironmentCooling | SKIPPED | Dry run! |
| 137 | dc1-leaf1c | Hardware | Verifies if the device temperature is within the acceptable range. | VerifyTemperature | SKIPPED | Dry run! |
| 138 | dc1-leaf1c | Hardware | Verifies the transceiver's manufacturer against a list of approved manufacturers. | VerifyTransceiversManufacturers | SKIPPED | Dry run! |
| 139 | dc1-leaf1c | Interface State | Ethernet Interface & Line Protocol == \"up\" | Ethernet1 - DC1-LEAF1A_Ethernet8 | SKIPPED | Dry run! |
| 140 | dc1-leaf1c | Interface State | Ethernet Interface & Line Protocol == \"up\" | Ethernet2 - DC1-LEAF1B_Ethernet8 | SKIPPED | Dry run! |
| 141 | dc1-leaf1c | Interface State | Ethernet Interface & Line Protocol == \"up\" | Ethernet5 - dc1-leaf1-server1_iLO | SKIPPED | Dry run! |
| 142 | dc1-leaf1c | Interface State | Port-Channel Interface & Line Protocol == \"up\" | Port-Channel1 - DC1_L3_LEAF1_Po8 | SKIPPED | Dry run! |
| 143 | dc1-leaf1c | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet1 - remote: dc1-leaf1a_Ethernet8 | SKIPPED | Dry run! |
| 144 | dc1-leaf1c | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet2 - remote: dc1-leaf1b_Ethernet8 | SKIPPED | Dry run! |
| 145 | dc1-leaf1c | NTP | Synchronised with NTP server | NTP | SKIPPED | Dry run! |
| 146 | dc1-leaf2a | BGP | ArBGP is configured and operating | ArBGP | SKIPPED | Dry run! |
| 147 | dc1-leaf2a | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.255.0.1 | SKIPPED | Dry run! |
| 148 | dc1-leaf2a | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.255.0.2 | SKIPPED | Dry run! |
| 149 | dc1-leaf2a | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.255.128.15 | SKIPPED | Dry run! |
| 150 | dc1-leaf2a | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.255.255.10 | SKIPPED | Dry run! |
| 151 | dc1-leaf2a | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.255.255.8 | SKIPPED | Dry run! |
| 152 | dc1-leaf2a | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 192.168.100.1 | SKIPPED | Dry run! |
| 153 | dc1-leaf2a | Hardware | Verifies if the power supplies status are within the accepted states list. | VerifyEnvironmentPower | SKIPPED | Dry run! |
| 154 | dc1-leaf2a | Hardware | Verifies if the fans status are within the accepted states list. | VerifyEnvironmentCooling | SKIPPED | Dry run! |
| 155 | dc1-leaf2a | Hardware | Verifies if the device temperature is within the acceptable range. | VerifyTemperature | SKIPPED | Dry run! |
| 156 | dc1-leaf2a | Hardware | Verifies the transceiver's manufacturer against a list of approved manufacturers. | VerifyTransceiversManufacturers | SKIPPED | Dry run! |
| 157 | dc1-leaf2a | IP Reachability | ip reachability test p2p links | Source: dc1-leaf2a_Ethernet1 - Destination: dc1-spine1_Ethernet3 | SKIPPED | Dry run! |
| 158 | dc1-leaf2a | IP Reachability | ip reachability test p2p links | Source: dc1-leaf2a_Ethernet2 - Destination: dc1-spine2_Ethernet3 | SKIPPED | Dry run! |
| 159 | dc1-leaf2a | IP Reachability | ip reachability test p2p links | Source: dc1-leaf2a_Ethernet6 - Destination: dc2-leaf2a_Ethernet6 | SKIPPED | Dry run! |
| 160 | dc1-leaf2a | Interface State | Ethernet Interface & Line Protocol == \"up\" | Ethernet1 - P2P_LINK_TO_DC1-SPINE1_Ethernet3 | SKIPPED | Dry run! |
| 161 | dc1-leaf2a | Interface State | Ethernet Interface & Line Protocol == \"up\" | Ethernet2 - P2P_LINK_TO_DC1-SPINE2_Ethernet3 | SKIPPED | Dry run! |
| 162 | dc1-leaf2a | Interface State | Ethernet Interface & Line Protocol == \"up\" | Ethernet3 - MLAG_PEER_dc1-leaf2b_Ethernet3 | SKIPPED | Dry run! |
| 163 | dc1-leaf2a | Interface State | Ethernet Interface & Line Protocol == \"up\" | Ethernet4 - MLAG_PEER_dc1-leaf2b_Ethernet4 | SKIPPED | Dry run! |
| 164 | dc1-leaf2a | Interface State | Ethernet Interface & Line Protocol == \"up\" | Ethernet5 - dc1-leaf2-server1_PCI1 | SKIPPED | Dry run! |
| 165 | dc1-leaf2a | Interface State | Ethernet Interface & Line Protocol == \"up\" | Ethernet6 - P2P_LINK_TO_dc2-leaf2a_Ethernet6 | SKIPPED | Dry run! |
| 166 | dc1-leaf2a | Interface State | Ethernet Interface & Line Protocol == \"up\" | Ethernet8 - DC1-LEAF2C_Ethernet1 | SKIPPED | Dry run! |
| 167 | dc1-leaf2a | Interface State | Loopback Interface Status & Line Protocol == \"up\" | Loopback0 - EVPN_Overlay_Peering | SKIPPED | Dry run! |
| 168 | dc1-leaf2a | Interface State | Loopback Interface Status & Line Protocol == \"up\" | Loopback1 - VTEP_VXLAN_Tunnel_Source | SKIPPED | Dry run! |
| 169 | dc1-leaf2a | Interface State | Loopback Interface Status & Line Protocol == \"up\" | Loopback10 - VRF10_VTEP_DIAGNOSTICS | SKIPPED | Dry run! |
| 170 | dc1-leaf2a | Interface State | Loopback Interface Status & Line Protocol == \"up\" | Loopback11 - VRF11_VTEP_DIAGNOSTICS | SKIPPED | Dry run! |
| 171 | dc1-leaf2a | Interface State | Port-Channel Interface & Line Protocol == \"up\" | Port-Channel3 - MLAG_PEER_dc1-leaf2b_Po3 | SKIPPED | Dry run! |
| 172 | dc1-leaf2a | Interface State | Port-Channel Interface & Line Protocol == \"up\" | Port-Channel5 - dc1-leaf2-server1_PortChannel dc1-leaf2-server1 | SKIPPED | Dry run! |
| 173 | dc1-leaf2a | Interface State | Port-Channel Interface & Line Protocol == \"up\" | Port-Channel8 - DC1-LEAF2C_Po1 | SKIPPED | Dry run! |
| 174 | dc1-leaf2a | Interface State | Vlan Interface & Line Protocol == \"up\" | Vlan11 - VRF10_VLAN11 | SKIPPED | Dry run! |
| 175 | dc1-leaf2a | Interface State | Vlan Interface & Line Protocol == \"up\" | Vlan12 - VRF10_VLAN12 | SKIPPED | Dry run! |
| 176 | dc1-leaf2a | Interface State | Vlan Interface & Line Protocol == \"up\" | Vlan21 - VRF11_VLAN21 | SKIPPED | Dry run! |
| 177 | dc1-leaf2a | Interface State | Vlan Interface & Line Protocol == \"up\" | Vlan22 - VRF11_VLAN22 | SKIPPED | Dry run! |
| 178 | dc1-leaf2a | Interface State | Vlan Interface & Line Protocol == \"up\" | Vlan3009 - MLAG_PEER_L3_iBGP: vrf VRF10 | SKIPPED | Dry run! |
| 179 | dc1-leaf2a | Interface State | Vlan Interface & Line Protocol == \"up\" | Vlan3010 - MLAG_PEER_L3_iBGP: vrf VRF11 | SKIPPED | Dry run! |
| 180 | dc1-leaf2a | Interface State | Vlan Interface & Line Protocol == \"up\" | Vlan4093 - MLAG_PEER_L3_PEERING | SKIPPED | Dry run! |
| 181 | dc1-leaf2a | Interface State | Vlan Interface & Line Protocol == \"up\" | Vlan4094 - MLAG_PEER | SKIPPED | Dry run! |
| 182 | dc1-leaf2a | Interface State | Vxlan Interface Status & Line Protocol == \"up\" | Vxlan1 | SKIPPED | Dry run! |
| 183 | dc1-leaf2a | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet1 - remote: dc1-spine1_Ethernet3 | SKIPPED | Dry run! |
| 184 | dc1-leaf2a | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet2 - remote: dc1-spine2_Ethernet3 | SKIPPED | Dry run! |
| 185 | dc1-leaf2a | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet6 - remote: dc2-leaf2a_Ethernet6 | SKIPPED | Dry run! |
| 186 | dc1-leaf2a | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet8 - remote: dc1-leaf2c_Ethernet1 | SKIPPED | Dry run! |
| 187 | dc1-leaf2a | Loopback0 Reachability | Loopback0 Reachability | Source: dc1-leaf2a - 10.255.0.5/32 Destination: 10.255.0.1 | SKIPPED | Dry run! |
| 188 | dc1-leaf2a | Loopback0 Reachability | Loopback0 Reachability | Source: dc1-leaf2a - 10.255.0.5/32 Destination: 10.255.0.2 | SKIPPED | Dry run! |
| 189 | dc1-leaf2a | Loopback0 Reachability | Loopback0 Reachability | Source: dc1-leaf2a - 10.255.0.5/32 Destination: 10.255.0.3 | SKIPPED | Dry run! |
| 190 | dc1-leaf2a | Loopback0 Reachability | Loopback0 Reachability | Source: dc1-leaf2a - 10.255.0.5/32 Destination: 10.255.0.4 | SKIPPED | Dry run! |
| 191 | dc1-leaf2a | Loopback0 Reachability | Loopback0 Reachability | Source: dc1-leaf2a - 10.255.0.5/32 Destination: 10.255.0.5 | SKIPPED | Dry run! |
| 192 | dc1-leaf2a | Loopback0 Reachability | Loopback0 Reachability | Source: dc1-leaf2a - 10.255.0.5/32 Destination: 10.255.128.11 | SKIPPED | Dry run! |
| 193 | dc1-leaf2a | Loopback0 Reachability | Loopback0 Reachability | Source: dc1-leaf2a - 10.255.0.5/32 Destination: 10.255.128.12 | SKIPPED | Dry run! |
| 194 | dc1-leaf2a | Loopback0 Reachability | Loopback0 Reachability | Source: dc1-leaf2a - 10.255.0.5/32 Destination: 10.255.128.13 | SKIPPED | Dry run! |
| 195 | dc1-leaf2a | Loopback0 Reachability | Loopback0 Reachability | Source: dc1-leaf2a - 10.255.0.5/32 Destination: 10.255.128.14 | SKIPPED | Dry run! |
| 196 | dc1-leaf2a | Loopback0 Reachability | Loopback0 Reachability | Source: dc1-leaf2a - 10.255.0.5/32 Destination: 10.255.128.15 | SKIPPED | Dry run! |
| 197 | dc1-leaf2a | Loopback0 Reachability | Loopback0 Reachability | Source: dc1-leaf2a - 10.255.0.5/32 Destination: 10.255.128.16 | SKIPPED | Dry run! |
| 198 | dc1-leaf2a | MLAG | MLAG State active & Status connected | MLAG | SKIPPED | Dry run! |
| 199 | dc1-leaf2a | NTP | Synchronised with NTP server | NTP | SKIPPED | Dry run! |
| 200 | dc1-leaf2a | Routing Table | Remote Lo0 address | 10.255.0.1 | SKIPPED | Dry run! |
| 201 | dc1-leaf2a | Routing Table | Remote Lo0 address | 10.255.0.2 | SKIPPED | Dry run! |
| 202 | dc1-leaf2a | Routing Table | Remote Lo0 address | 10.255.0.3 | SKIPPED | Dry run! |
| 203 | dc1-leaf2a | Routing Table | Remote Lo0 address | 10.255.0.4 | SKIPPED | Dry run! |
| 204 | dc1-leaf2a | Routing Table | Remote Lo0 address | 10.255.0.5 | SKIPPED | Dry run! |
| 205 | dc1-leaf2a | Routing Table | Remote VTEP address | 10.255.1.3 | SKIPPED | Dry run! |
| 206 | dc1-leaf2a | Routing Table | Remote VTEP address | 10.255.1.5 | SKIPPED | Dry run! |
| 207 | dc1-leaf2a | Routing Table | Remote Lo0 address | 10.255.128.11 | SKIPPED | Dry run! |
| 208 | dc1-leaf2a | Routing Table | Remote Lo0 address | 10.255.128.12 | SKIPPED | Dry run! |
| 209 | dc1-leaf2a | Routing Table | Remote Lo0 address | 10.255.128.13 | SKIPPED | Dry run! |
| 210 | dc1-leaf2a | Routing Table | Remote Lo0 address | 10.255.128.14 | SKIPPED | Dry run! |
| 211 | dc1-leaf2a | Routing Table | Remote Lo0 address | 10.255.128.15 | SKIPPED | Dry run! |
| 212 | dc1-leaf2a | Routing Table | Remote Lo0 address | 10.255.128.16 | SKIPPED | Dry run! |
| 213 | dc1-leaf2a | Routing Table | Remote VTEP address | 10.255.129.13 | SKIPPED | Dry run! |
| 214 | dc1-leaf2a | Routing Table | Remote VTEP address | 10.255.129.15 | SKIPPED | Dry run! |
| 215 | dc1-leaf2c | Hardware | Verifies if the power supplies status are within the accepted states list. | VerifyEnvironmentPower | SKIPPED | Dry run! |
| 216 | dc1-leaf2c | Hardware | Verifies if the fans status are within the accepted states list. | VerifyEnvironmentCooling | SKIPPED | Dry run! |
| 217 | dc1-leaf2c | Hardware | Verifies if the device temperature is within the acceptable range. | VerifyTemperature | SKIPPED | Dry run! |
| 218 | dc1-leaf2c | Hardware | Verifies the transceiver's manufacturer against a list of approved manufacturers. | VerifyTransceiversManufacturers | SKIPPED | Dry run! |
| 219 | dc1-leaf2c | Interface State | Ethernet Interface & Line Protocol == \"up\" | Ethernet1 - DC1-LEAF2A_Ethernet8 | SKIPPED | Dry run! |
| 220 | dc1-leaf2c | Interface State | Ethernet Interface & Line Protocol == \"adminDown\" | Ethernet2 - DC1-LEAF2B_Ethernet8 | SKIPPED | Dry run! |
| 221 | dc1-leaf2c | Interface State | Ethernet Interface & Line Protocol == \"up\" | Ethernet5 - dc1-leaf2-server1_iLO | SKIPPED | Dry run! |
| 222 | dc1-leaf2c | Interface State | Port-Channel Interface & Line Protocol == \"up\" | Port-Channel1 - DC1_L3_LEAF2_Po8 | SKIPPED | Dry run! |
| 223 | dc1-leaf2c | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet1 - remote: dc1-leaf2a_Ethernet8 | SKIPPED | Dry run! |
| 224 | dc1-leaf2c | NTP | Synchronised with NTP server | NTP | SKIPPED | Dry run! |
| 225 | dc1-spine1 | BGP | ArBGP is configured and operating | ArBGP | SKIPPED | Dry run! |
| 226 | dc1-spine1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.255.0.3 | SKIPPED | Dry run! |
| 227 | dc1-spine1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.255.0.4 | SKIPPED | Dry run! |
| 228 | dc1-spine1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.255.0.5 | SKIPPED | Dry run! |
| 229 | dc1-spine1 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.255.255.1 | SKIPPED | Dry run! |
| 230 | dc1-spine1 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.255.255.5 | SKIPPED | Dry run! |
| 231 | dc1-spine1 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.255.255.9 | SKIPPED | Dry run! |
| 232 | dc1-spine1 | Hardware | Verifies if the power supplies status are within the accepted states list. | VerifyEnvironmentPower | SKIPPED | Dry run! |
| 233 | dc1-spine1 | Hardware | Verifies if the fans status are within the accepted states list. | VerifyEnvironmentCooling | SKIPPED | Dry run! |
| 234 | dc1-spine1 | Hardware | Verifies if the device temperature is within the acceptable range. | VerifyTemperature | SKIPPED | Dry run! |
| 235 | dc1-spine1 | Hardware | Verifies the transceiver's manufacturer against a list of approved manufacturers. | VerifyTransceiversManufacturers | SKIPPED | Dry run! |
| 236 | dc1-spine1 | IP Reachability | ip reachability test p2p links | Source: dc1-spine1_Ethernet1 - Destination: dc1-leaf1a_Ethernet1 | SKIPPED | Dry run! |
| 237 | dc1-spine1 | IP Reachability | ip reachability test p2p links | Source: dc1-spine1_Ethernet2 - Destination: dc1-leaf1b_Ethernet1 | SKIPPED | Dry run! |
| 238 | dc1-spine1 | IP Reachability | ip reachability test p2p links | Source: dc1-spine1_Ethernet3 - Destination: dc1-leaf2a_Ethernet1 | SKIPPED | Dry run! |
| 239 | dc1-spine1 | Interface State | Ethernet Interface & Line Protocol == \"up\" | Ethernet1 - P2P_LINK_TO_DC1-LEAF1A_Ethernet1 | SKIPPED | Dry run! |
| 240 | dc1-spine1 | Interface State | Ethernet Interface & Line Protocol == \"up\" | Ethernet2 - P2P_LINK_TO_DC1-LEAF1B_Ethernet1 | SKIPPED | Dry run! |
| 241 | dc1-spine1 | Interface State | Ethernet Interface & Line Protocol == \"up\" | Ethernet3 - P2P_LINK_TO_DC1-LEAF2A_Ethernet1 | SKIPPED | Dry run! |
| 242 | dc1-spine1 | Interface State | Ethernet Interface & Line Protocol == \"adminDown\" | Ethernet4 - P2P_LINK_TO_DC1-LEAF2B_Ethernet1 | SKIPPED | Dry run! |
| 243 | dc1-spine1 | Interface State | Loopback Interface Status & Line Protocol == \"up\" | Loopback0 - EVPN_Overlay_Peering | SKIPPED | Dry run! |
| 244 | dc1-spine1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet1 - remote: dc1-leaf1a_Ethernet1 | SKIPPED | Dry run! |
| 245 | dc1-spine1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet2 - remote: dc1-leaf1b_Ethernet1 | SKIPPED | Dry run! |
| 246 | dc1-spine1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet3 - remote: dc1-leaf2a_Ethernet1 | SKIPPED | Dry run! |
| 247 | dc1-spine1 | NTP | Synchronised with NTP server | NTP | SKIPPED | Dry run! |
| 248 | dc1-spine2 | BGP | ArBGP is configured and operating | ArBGP | SKIPPED | Dry run! |
| 249 | dc1-spine2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.255.0.3 | SKIPPED | Dry run! |
| 250 | dc1-spine2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.255.0.4 | SKIPPED | Dry run! |
| 251 | dc1-spine2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.255.0.5 | SKIPPED | Dry run! |
| 252 | dc1-spine2 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.255.255.11 | SKIPPED | Dry run! |
| 253 | dc1-spine2 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.255.255.3 | SKIPPED | Dry run! |
| 254 | dc1-spine2 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.255.255.7 | SKIPPED | Dry run! |
| 255 | dc1-spine2 | Hardware | Verifies if the power supplies status are within the accepted states list. | VerifyEnvironmentPower | SKIPPED | Dry run! |
| 256 | dc1-spine2 | Hardware | Verifies if the fans status are within the accepted states list. | VerifyEnvironmentCooling | SKIPPED | Dry run! |
| 257 | dc1-spine2 | Hardware | Verifies if the device temperature is within the acceptable range. | VerifyTemperature | SKIPPED | Dry run! |
| 258 | dc1-spine2 | Hardware | Verifies the transceiver's manufacturer against a list of approved manufacturers. | VerifyTransceiversManufacturers | SKIPPED | Dry run! |
| 259 | dc1-spine2 | IP Reachability | ip reachability test p2p links | Source: dc1-spine2_Ethernet1 - Destination: dc1-leaf1a_Ethernet2 | SKIPPED | Dry run! |
| 260 | dc1-spine2 | IP Reachability | ip reachability test p2p links | Source: dc1-spine2_Ethernet2 - Destination: dc1-leaf1b_Ethernet2 | SKIPPED | Dry run! |
| 261 | dc1-spine2 | IP Reachability | ip reachability test p2p links | Source: dc1-spine2_Ethernet3 - Destination: dc1-leaf2a_Ethernet2 | SKIPPED | Dry run! |
| 262 | dc1-spine2 | Interface State | Ethernet Interface & Line Protocol == \"up\" | Ethernet1 - P2P_LINK_TO_DC1-LEAF1A_Ethernet2 | SKIPPED | Dry run! |
| 263 | dc1-spine2 | Interface State | Ethernet Interface & Line Protocol == \"up\" | Ethernet2 - P2P_LINK_TO_DC1-LEAF1B_Ethernet2 | SKIPPED | Dry run! |
| 264 | dc1-spine2 | Interface State | Ethernet Interface & Line Protocol == \"up\" | Ethernet3 - P2P_LINK_TO_DC1-LEAF2A_Ethernet2 | SKIPPED | Dry run! |
| 265 | dc1-spine2 | Interface State | Ethernet Interface & Line Protocol == \"adminDown\" | Ethernet4 - P2P_LINK_TO_DC1-LEAF2B_Ethernet2 | SKIPPED | Dry run! |
| 266 | dc1-spine2 | Interface State | Loopback Interface Status & Line Protocol == \"up\" | Loopback0 - EVPN_Overlay_Peering | SKIPPED | Dry run! |
| 267 | dc1-spine2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet1 - remote: dc1-leaf1a_Ethernet2 | SKIPPED | Dry run! |
| 268 | dc1-spine2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet2 - remote: dc1-leaf1b_Ethernet2 | SKIPPED | Dry run! |
| 269 | dc1-spine2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet3 - remote: dc1-leaf2a_Ethernet2 | SKIPPED | Dry run! |
| 270 | dc1-spine2 | NTP | Synchronised with NTP server | NTP | SKIPPED | Dry run! |
| 271 | dc2-leaf1a | BGP | ArBGP is configured and operating | ArBGP | SKIPPED | Dry run! |
| 272 | dc2-leaf1a | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.255.128.11 | SKIPPED | Dry run! |
| 273 | dc2-leaf1a | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.255.128.12 | SKIPPED | Dry run! |
| 274 | dc2-leaf1a | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.255.129.117 | SKIPPED | Dry run! |
| 275 | dc2-leaf1a | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.255.255.104 | SKIPPED | Dry run! |
| 276 | dc2-leaf1a | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.255.255.106 | SKIPPED | Dry run! |
| 277 | dc2-leaf1a | Hardware | Verifies if the power supplies status are within the accepted states list. | VerifyEnvironmentPower | SKIPPED | Dry run! |
| 278 | dc2-leaf1a | Hardware | Verifies if the fans status are within the accepted states list. | VerifyEnvironmentCooling | SKIPPED | Dry run! |
| 279 | dc2-leaf1a | Hardware | Verifies if the device temperature is within the acceptable range. | VerifyTemperature | SKIPPED | Dry run! |
| 280 | dc2-leaf1a | Hardware | Verifies the transceiver's manufacturer against a list of approved manufacturers. | VerifyTransceiversManufacturers | SKIPPED | Dry run! |
| 281 | dc2-leaf1a | IP Reachability | ip reachability test p2p links | Source: dc2-leaf1a_Ethernet1 - Destination: dc2-spine1_Ethernet1 | SKIPPED | Dry run! |
| 282 | dc2-leaf1a | IP Reachability | ip reachability test p2p links | Source: dc2-leaf1a_Ethernet2 - Destination: dc2-spine2_Ethernet1 | SKIPPED | Dry run! |
| 283 | dc2-leaf1a | Interface State | Ethernet Interface & Line Protocol == \"up\" | Ethernet1 - P2P_LINK_TO_DC2-SPINE1_Ethernet1 | SKIPPED | Dry run! |
| 284 | dc2-leaf1a | Interface State | Ethernet Interface & Line Protocol == \"up\" | Ethernet2 - P2P_LINK_TO_DC2-SPINE2_Ethernet1 | SKIPPED | Dry run! |
| 285 | dc2-leaf1a | Interface State | Ethernet Interface & Line Protocol == \"up\" | Ethernet3 - MLAG_PEER_dc2-leaf1b_Ethernet3 | SKIPPED | Dry run! |
| 286 | dc2-leaf1a | Interface State | Ethernet Interface & Line Protocol == \"up\" | Ethernet4 - MLAG_PEER_dc2-leaf1b_Ethernet4 | SKIPPED | Dry run! |
| 287 | dc2-leaf1a | Interface State | Ethernet Interface & Line Protocol == \"up\" | Ethernet5 - dc2-leaf1-server1_PCI1 | SKIPPED | Dry run! |
| 288 | dc2-leaf1a | Interface State | Ethernet Interface & Line Protocol == \"up\" | Ethernet8 - DC2-LEAF1C_Ethernet1 | SKIPPED | Dry run! |
| 289 | dc2-leaf1a | Interface State | Loopback Interface Status & Line Protocol == \"up\" | Loopback0 - EVPN_Overlay_Peering | SKIPPED | Dry run! |
| 290 | dc2-leaf1a | Interface State | Loopback Interface Status & Line Protocol == \"up\" | Loopback1 - VTEP_VXLAN_Tunnel_Source | SKIPPED | Dry run! |
| 291 | dc2-leaf1a | Interface State | Loopback Interface Status & Line Protocol == \"up\" | Loopback10 - VRF10_VTEP_DIAGNOSTICS | SKIPPED | Dry run! |
| 292 | dc2-leaf1a | Interface State | Loopback Interface Status & Line Protocol == \"up\" | Loopback11 - VRF11_VTEP_DIAGNOSTICS | SKIPPED | Dry run! |
| 293 | dc2-leaf1a | Interface State | Port-Channel Interface & Line Protocol == \"up\" | Port-Channel3 - MLAG_PEER_dc2-leaf1b_Po3 | SKIPPED | Dry run! |
| 294 | dc2-leaf1a | Interface State | Port-Channel Interface & Line Protocol == \"up\" | Port-Channel5 - dc2-leaf1-server1_PortChannel dc2-leaf1-server1 | SKIPPED | Dry run! |
| 295 | dc2-leaf1a | Interface State | Port-Channel Interface & Line Protocol == \"up\" | Port-Channel8 - DC2-LEAF1C_Po1 | SKIPPED | Dry run! |
| 296 | dc2-leaf1a | Interface State | Vlan Interface & Line Protocol == \"up\" | Vlan11 - VRF10_VLAN11 | SKIPPED | Dry run! |
| 297 | dc2-leaf1a | Interface State | Vlan Interface & Line Protocol == \"up\" | Vlan12 - VRF10_VLAN12 | SKIPPED | Dry run! |
| 298 | dc2-leaf1a | Interface State | Vlan Interface & Line Protocol == \"up\" | Vlan21 - VRF11_VLAN21 | SKIPPED | Dry run! |
| 299 | dc2-leaf1a | Interface State | Vlan Interface & Line Protocol == \"up\" | Vlan22 - VRF11_VLAN22 | SKIPPED | Dry run! |
| 300 | dc2-leaf1a | Interface State | Vlan Interface & Line Protocol == \"up\" | Vlan3009 - MLAG_PEER_L3_iBGP: vrf VRF10 | SKIPPED | Dry run! |
| 301 | dc2-leaf1a | Interface State | Vlan Interface & Line Protocol == \"up\" | Vlan3010 - MLAG_PEER_L3_iBGP: vrf VRF11 | SKIPPED | Dry run! |
| 302 | dc2-leaf1a | Interface State | Vlan Interface & Line Protocol == \"up\" | Vlan4093 - MLAG_PEER_L3_PEERING | SKIPPED | Dry run! |
| 303 | dc2-leaf1a | Interface State | Vlan Interface & Line Protocol == \"up\" | Vlan4094 - MLAG_PEER | SKIPPED | Dry run! |
| 304 | dc2-leaf1a | Interface State | Vxlan Interface Status & Line Protocol == \"up\" | Vxlan1 | SKIPPED | Dry run! |
| 305 | dc2-leaf1a | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet1 - remote: dc2-spine1_Ethernet1 | SKIPPED | Dry run! |
| 306 | dc2-leaf1a | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet2 - remote: dc2-spine2_Ethernet1 | SKIPPED | Dry run! |
| 307 | dc2-leaf1a | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet3 - remote: dc2-leaf1b_Ethernet3 | SKIPPED | Dry run! |
| 308 | dc2-leaf1a | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet4 - remote: dc2-leaf1b_Ethernet4 | SKIPPED | Dry run! |
| 309 | dc2-leaf1a | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet8 - remote: dc2-leaf1c_Ethernet1 | SKIPPED | Dry run! |
| 310 | dc2-leaf1a | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf1a - 10.255.128.13/32 Destination: 10.255.0.1 | SKIPPED | Dry run! |
| 311 | dc2-leaf1a | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf1a - 10.255.128.13/32 Destination: 10.255.0.2 | SKIPPED | Dry run! |
| 312 | dc2-leaf1a | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf1a - 10.255.128.13/32 Destination: 10.255.0.3 | SKIPPED | Dry run! |
| 313 | dc2-leaf1a | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf1a - 10.255.128.13/32 Destination: 10.255.0.4 | SKIPPED | Dry run! |
| 314 | dc2-leaf1a | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf1a - 10.255.128.13/32 Destination: 10.255.0.5 | SKIPPED | Dry run! |
| 315 | dc2-leaf1a | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf1a - 10.255.128.13/32 Destination: 10.255.128.11 | SKIPPED | Dry run! |
| 316 | dc2-leaf1a | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf1a - 10.255.128.13/32 Destination: 10.255.128.12 | SKIPPED | Dry run! |
| 317 | dc2-leaf1a | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf1a - 10.255.128.13/32 Destination: 10.255.128.13 | SKIPPED | Dry run! |
| 318 | dc2-leaf1a | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf1a - 10.255.128.13/32 Destination: 10.255.128.14 | SKIPPED | Dry run! |
| 319 | dc2-leaf1a | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf1a - 10.255.128.13/32 Destination: 10.255.128.15 | SKIPPED | Dry run! |
| 320 | dc2-leaf1a | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf1a - 10.255.128.13/32 Destination: 10.255.128.16 | SKIPPED | Dry run! |
| 321 | dc2-leaf1a | MLAG | MLAG State active & Status connected | MLAG | SKIPPED | Dry run! |
| 322 | dc2-leaf1a | NTP | Synchronised with NTP server | NTP | SKIPPED | Dry run! |
| 323 | dc2-leaf1a | Routing Table | Remote Lo0 address | 10.255.0.1 | SKIPPED | Dry run! |
| 324 | dc2-leaf1a | Routing Table | Remote Lo0 address | 10.255.0.2 | SKIPPED | Dry run! |
| 325 | dc2-leaf1a | Routing Table | Remote Lo0 address | 10.255.0.3 | SKIPPED | Dry run! |
| 326 | dc2-leaf1a | Routing Table | Remote Lo0 address | 10.255.0.4 | SKIPPED | Dry run! |
| 327 | dc2-leaf1a | Routing Table | Remote Lo0 address | 10.255.0.5 | SKIPPED | Dry run! |
| 328 | dc2-leaf1a | Routing Table | Remote VTEP address | 10.255.1.3 | SKIPPED | Dry run! |
| 329 | dc2-leaf1a | Routing Table | Remote VTEP address | 10.255.1.5 | SKIPPED | Dry run! |
| 330 | dc2-leaf1a | Routing Table | Remote Lo0 address | 10.255.128.11 | SKIPPED | Dry run! |
| 331 | dc2-leaf1a | Routing Table | Remote Lo0 address | 10.255.128.12 | SKIPPED | Dry run! |
| 332 | dc2-leaf1a | Routing Table | Remote Lo0 address | 10.255.128.13 | SKIPPED | Dry run! |
| 333 | dc2-leaf1a | Routing Table | Remote Lo0 address | 10.255.128.14 | SKIPPED | Dry run! |
| 334 | dc2-leaf1a | Routing Table | Remote Lo0 address | 10.255.128.15 | SKIPPED | Dry run! |
| 335 | dc2-leaf1a | Routing Table | Remote Lo0 address | 10.255.128.16 | SKIPPED | Dry run! |
| 336 | dc2-leaf1a | Routing Table | Remote VTEP address | 10.255.129.13 | SKIPPED | Dry run! |
| 337 | dc2-leaf1a | Routing Table | Remote VTEP address | 10.255.129.15 | SKIPPED | Dry run! |
| 338 | dc2-leaf1b | BGP | ArBGP is configured and operating | ArBGP | SKIPPED | Dry run! |
| 339 | dc2-leaf1b | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.255.128.11 | SKIPPED | Dry run! |
| 340 | dc2-leaf1b | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.255.128.12 | SKIPPED | Dry run! |
| 341 | dc2-leaf1b | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.255.129.116 | SKIPPED | Dry run! |
| 342 | dc2-leaf1b | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.255.255.108 | SKIPPED | Dry run! |
| 343 | dc2-leaf1b | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.255.255.110 | SKIPPED | Dry run! |
| 344 | dc2-leaf1b | Hardware | Verifies if the power supplies status are within the accepted states list. | VerifyEnvironmentPower | SKIPPED | Dry run! |
| 345 | dc2-leaf1b | Hardware | Verifies if the fans status are within the accepted states list. | VerifyEnvironmentCooling | SKIPPED | Dry run! |
| 346 | dc2-leaf1b | Hardware | Verifies if the device temperature is within the acceptable range. | VerifyTemperature | SKIPPED | Dry run! |
| 347 | dc2-leaf1b | Hardware | Verifies the transceiver's manufacturer against a list of approved manufacturers. | VerifyTransceiversManufacturers | SKIPPED | Dry run! |
| 348 | dc2-leaf1b | IP Reachability | ip reachability test p2p links | Source: dc2-leaf1b_Ethernet1 - Destination: dc2-spine1_Ethernet2 | SKIPPED | Dry run! |
| 349 | dc2-leaf1b | IP Reachability | ip reachability test p2p links | Source: dc2-leaf1b_Ethernet2 - Destination: dc2-spine2_Ethernet2 | SKIPPED | Dry run! |
| 350 | dc2-leaf1b | Interface State | Ethernet Interface & Line Protocol == \"up\" | Ethernet1 - P2P_LINK_TO_DC2-SPINE1_Ethernet2 | SKIPPED | Dry run! |
| 351 | dc2-leaf1b | Interface State | Ethernet Interface & Line Protocol == \"up\" | Ethernet2 - P2P_LINK_TO_DC2-SPINE2_Ethernet2 | SKIPPED | Dry run! |
| 352 | dc2-leaf1b | Interface State | Ethernet Interface & Line Protocol == \"up\" | Ethernet3 - MLAG_PEER_dc2-leaf1a_Ethernet3 | SKIPPED | Dry run! |
| 353 | dc2-leaf1b | Interface State | Ethernet Interface & Line Protocol == \"up\" | Ethernet4 - MLAG_PEER_dc2-leaf1a_Ethernet4 | SKIPPED | Dry run! |
| 354 | dc2-leaf1b | Interface State | Ethernet Interface & Line Protocol == \"up\" | Ethernet5 - dc2-leaf1-server1_PCI2 | SKIPPED | Dry run! |
| 355 | dc2-leaf1b | Interface State | Ethernet Interface & Line Protocol == \"up\" | Ethernet8 - DC2-LEAF1C_Ethernet2 | SKIPPED | Dry run! |
| 356 | dc2-leaf1b | Interface State | Loopback Interface Status & Line Protocol == \"up\" | Loopback0 - EVPN_Overlay_Peering | SKIPPED | Dry run! |
| 357 | dc2-leaf1b | Interface State | Loopback Interface Status & Line Protocol == \"up\" | Loopback1 - VTEP_VXLAN_Tunnel_Source | SKIPPED | Dry run! |
| 358 | dc2-leaf1b | Interface State | Loopback Interface Status & Line Protocol == \"up\" | Loopback10 - VRF10_VTEP_DIAGNOSTICS | SKIPPED | Dry run! |
| 359 | dc2-leaf1b | Interface State | Loopback Interface Status & Line Protocol == \"up\" | Loopback11 - VRF11_VTEP_DIAGNOSTICS | SKIPPED | Dry run! |
| 360 | dc2-leaf1b | Interface State | Port-Channel Interface & Line Protocol == \"up\" | Port-Channel3 - MLAG_PEER_dc2-leaf1a_Po3 | SKIPPED | Dry run! |
| 361 | dc2-leaf1b | Interface State | Port-Channel Interface & Line Protocol == \"up\" | Port-Channel5 - dc2-leaf1-server1_PortChannel dc2-leaf1-server1 | SKIPPED | Dry run! |
| 362 | dc2-leaf1b | Interface State | Port-Channel Interface & Line Protocol == \"up\" | Port-Channel8 - DC2-LEAF1C_Po1 | SKIPPED | Dry run! |
| 363 | dc2-leaf1b | Interface State | Vlan Interface & Line Protocol == \"up\" | Vlan11 - VRF10_VLAN11 | SKIPPED | Dry run! |
| 364 | dc2-leaf1b | Interface State | Vlan Interface & Line Protocol == \"up\" | Vlan12 - VRF10_VLAN12 | SKIPPED | Dry run! |
| 365 | dc2-leaf1b | Interface State | Vlan Interface & Line Protocol == \"up\" | Vlan21 - VRF11_VLAN21 | SKIPPED | Dry run! |
| 366 | dc2-leaf1b | Interface State | Vlan Interface & Line Protocol == \"up\" | Vlan22 - VRF11_VLAN22 | SKIPPED | Dry run! |
| 367 | dc2-leaf1b | Interface State | Vlan Interface & Line Protocol == \"up\" | Vlan3009 - MLAG_PEER_L3_iBGP: vrf VRF10 | SKIPPED | Dry run! |
| 368 | dc2-leaf1b | Interface State | Vlan Interface & Line Protocol == \"up\" | Vlan3010 - MLAG_PEER_L3_iBGP: vrf VRF11 | SKIPPED | Dry run! |
| 369 | dc2-leaf1b | Interface State | Vlan Interface & Line Protocol == \"up\" | Vlan4093 - MLAG_PEER_L3_PEERING | SKIPPED | Dry run! |
| 370 | dc2-leaf1b | Interface State | Vlan Interface & Line Protocol == \"up\" | Vlan4094 - MLAG_PEER | SKIPPED | Dry run! |
| 371 | dc2-leaf1b | Interface State | Vxlan Interface Status & Line Protocol == \"up\" | Vxlan1 | SKIPPED | Dry run! |
| 372 | dc2-leaf1b | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet1 - remote: dc2-spine1_Ethernet2 | SKIPPED | Dry run! |
| 373 | dc2-leaf1b | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet2 - remote: dc2-spine2_Ethernet2 | SKIPPED | Dry run! |
| 374 | dc2-leaf1b | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet3 - remote: dc2-leaf1a_Ethernet3 | SKIPPED | Dry run! |
| 375 | dc2-leaf1b | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet4 - remote: dc2-leaf1a_Ethernet4 | SKIPPED | Dry run! |
| 376 | dc2-leaf1b | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet8 - remote: dc2-leaf1c_Ethernet2 | SKIPPED | Dry run! |
| 377 | dc2-leaf1b | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf1b - 10.255.128.14/32 Destination: 10.255.0.1 | SKIPPED | Dry run! |
| 378 | dc2-leaf1b | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf1b - 10.255.128.14/32 Destination: 10.255.0.2 | SKIPPED | Dry run! |
| 379 | dc2-leaf1b | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf1b - 10.255.128.14/32 Destination: 10.255.0.3 | SKIPPED | Dry run! |
| 380 | dc2-leaf1b | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf1b - 10.255.128.14/32 Destination: 10.255.0.4 | SKIPPED | Dry run! |
| 381 | dc2-leaf1b | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf1b - 10.255.128.14/32 Destination: 10.255.0.5 | SKIPPED | Dry run! |
| 382 | dc2-leaf1b | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf1b - 10.255.128.14/32 Destination: 10.255.128.11 | SKIPPED | Dry run! |
| 383 | dc2-leaf1b | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf1b - 10.255.128.14/32 Destination: 10.255.128.12 | SKIPPED | Dry run! |
| 384 | dc2-leaf1b | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf1b - 10.255.128.14/32 Destination: 10.255.128.13 | SKIPPED | Dry run! |
| 385 | dc2-leaf1b | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf1b - 10.255.128.14/32 Destination: 10.255.128.14 | SKIPPED | Dry run! |
| 386 | dc2-leaf1b | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf1b - 10.255.128.14/32 Destination: 10.255.128.15 | SKIPPED | Dry run! |
| 387 | dc2-leaf1b | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf1b - 10.255.128.14/32 Destination: 10.255.128.16 | SKIPPED | Dry run! |
| 388 | dc2-leaf1b | MLAG | MLAG State active & Status connected | MLAG | SKIPPED | Dry run! |
| 389 | dc2-leaf1b | NTP | Synchronised with NTP server | NTP | SKIPPED | Dry run! |
| 390 | dc2-leaf1b | Routing Table | Remote Lo0 address | 10.255.0.1 | SKIPPED | Dry run! |
| 391 | dc2-leaf1b | Routing Table | Remote Lo0 address | 10.255.0.2 | SKIPPED | Dry run! |
| 392 | dc2-leaf1b | Routing Table | Remote Lo0 address | 10.255.0.3 | SKIPPED | Dry run! |
| 393 | dc2-leaf1b | Routing Table | Remote Lo0 address | 10.255.0.4 | SKIPPED | Dry run! |
| 394 | dc2-leaf1b | Routing Table | Remote Lo0 address | 10.255.0.5 | SKIPPED | Dry run! |
| 395 | dc2-leaf1b | Routing Table | Remote VTEP address | 10.255.1.3 | SKIPPED | Dry run! |
| 396 | dc2-leaf1b | Routing Table | Remote VTEP address | 10.255.1.5 | SKIPPED | Dry run! |
| 397 | dc2-leaf1b | Routing Table | Remote Lo0 address | 10.255.128.11 | SKIPPED | Dry run! |
| 398 | dc2-leaf1b | Routing Table | Remote Lo0 address | 10.255.128.12 | SKIPPED | Dry run! |
| 399 | dc2-leaf1b | Routing Table | Remote Lo0 address | 10.255.128.13 | SKIPPED | Dry run! |
| 400 | dc2-leaf1b | Routing Table | Remote Lo0 address | 10.255.128.14 | SKIPPED | Dry run! |
| 401 | dc2-leaf1b | Routing Table | Remote Lo0 address | 10.255.128.15 | SKIPPED | Dry run! |
| 402 | dc2-leaf1b | Routing Table | Remote Lo0 address | 10.255.128.16 | SKIPPED | Dry run! |
| 403 | dc2-leaf1b | Routing Table | Remote VTEP address | 10.255.129.13 | SKIPPED | Dry run! |
| 404 | dc2-leaf1b | Routing Table | Remote VTEP address | 10.255.129.15 | SKIPPED | Dry run! |
| 405 | dc2-leaf1c | Hardware | Verifies if the power supplies status are within the accepted states list. | VerifyEnvironmentPower | SKIPPED | Dry run! |
| 406 | dc2-leaf1c | Hardware | Verifies if the fans status are within the accepted states list. | VerifyEnvironmentCooling | SKIPPED | Dry run! |
| 407 | dc2-leaf1c | Hardware | Verifies if the device temperature is within the acceptable range. | VerifyTemperature | SKIPPED | Dry run! |
| 408 | dc2-leaf1c | Hardware | Verifies the transceiver's manufacturer against a list of approved manufacturers. | VerifyTransceiversManufacturers | SKIPPED | Dry run! |
| 409 | dc2-leaf1c | Interface State | Ethernet Interface & Line Protocol == \"up\" | Ethernet1 - DC2-LEAF1A_Ethernet8 | SKIPPED | Dry run! |
| 410 | dc2-leaf1c | Interface State | Ethernet Interface & Line Protocol == \"up\" | Ethernet2 - DC2-LEAF1B_Ethernet8 | SKIPPED | Dry run! |
| 411 | dc2-leaf1c | Interface State | Ethernet Interface & Line Protocol == \"up\" | Ethernet5 - dc2-leaf1-server1_iLO | SKIPPED | Dry run! |
| 412 | dc2-leaf1c | Interface State | Port-Channel Interface & Line Protocol == \"up\" | Port-Channel1 - DC2_L3_LEAF1_Po8 | SKIPPED | Dry run! |
| 413 | dc2-leaf1c | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet1 - remote: dc2-leaf1a_Ethernet8 | SKIPPED | Dry run! |
| 414 | dc2-leaf1c | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet2 - remote: dc2-leaf1b_Ethernet8 | SKIPPED | Dry run! |
| 415 | dc2-leaf1c | NTP | Synchronised with NTP server | NTP | SKIPPED | Dry run! |
| 416 | dc2-leaf2a | BGP | ArBGP is configured and operating | ArBGP | SKIPPED | Dry run! |
| 417 | dc2-leaf2a | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.255.0.5 | SKIPPED | Dry run! |
| 418 | dc2-leaf2a | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.255.128.11 | SKIPPED | Dry run! |
| 419 | dc2-leaf2a | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.255.128.12 | SKIPPED | Dry run! |
| 420 | dc2-leaf2a | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.255.129.121 | SKIPPED | Dry run! |
| 421 | dc2-leaf2a | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.255.255.112 | SKIPPED | Dry run! |
| 422 | dc2-leaf2a | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.255.255.114 | SKIPPED | Dry run! |
| 423 | dc2-leaf2a | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 192.168.100.0 | SKIPPED | Dry run! |
| 424 | dc2-leaf2a | Hardware | Verifies if the power supplies status are within the accepted states list. | VerifyEnvironmentPower | SKIPPED | Dry run! |
| 425 | dc2-leaf2a | Hardware | Verifies if the fans status are within the accepted states list. | VerifyEnvironmentCooling | SKIPPED | Dry run! |
| 426 | dc2-leaf2a | Hardware | Verifies if the device temperature is within the acceptable range. | VerifyTemperature | SKIPPED | Dry run! |
| 427 | dc2-leaf2a | Hardware | Verifies the transceiver's manufacturer against a list of approved manufacturers. | VerifyTransceiversManufacturers | SKIPPED | Dry run! |
| 428 | dc2-leaf2a | IP Reachability | ip reachability test p2p links | Source: dc2-leaf2a_Ethernet1 - Destination: dc2-spine1_Ethernet3 | SKIPPED | Dry run! |
| 429 | dc2-leaf2a | IP Reachability | ip reachability test p2p links | Source: dc2-leaf2a_Ethernet2 - Destination: dc2-spine2_Ethernet3 | SKIPPED | Dry run! |
| 430 | dc2-leaf2a | IP Reachability | ip reachability test p2p links | Source: dc2-leaf2a_Ethernet6 - Destination: dc1-leaf2a_Ethernet6 | SKIPPED | Dry run! |
| 431 | dc2-leaf2a | Interface State | Ethernet Interface & Line Protocol == \"up\" | Ethernet1 - P2P_LINK_TO_DC2-SPINE1_Ethernet3 | SKIPPED | Dry run! |
| 432 | dc2-leaf2a | Interface State | Ethernet Interface & Line Protocol == \"up\" | Ethernet2 - P2P_LINK_TO_DC2-SPINE2_Ethernet3 | SKIPPED | Dry run! |
| 433 | dc2-leaf2a | Interface State | Ethernet Interface & Line Protocol == \"up\" | Ethernet3 - MLAG_PEER_dc2-leaf2b_Ethernet3 | SKIPPED | Dry run! |
| 434 | dc2-leaf2a | Interface State | Ethernet Interface & Line Protocol == \"up\" | Ethernet4 - MLAG_PEER_dc2-leaf2b_Ethernet4 | SKIPPED | Dry run! |
| 435 | dc2-leaf2a | Interface State | Ethernet Interface & Line Protocol == \"up\" | Ethernet5 - dc2-leaf2-server1_PCI1 | SKIPPED | Dry run! |
| 436 | dc2-leaf2a | Interface State | Ethernet Interface & Line Protocol == \"up\" | Ethernet6 - P2P_LINK_TO_dc1-leaf2a_Ethernet6 | SKIPPED | Dry run! |
| 437 | dc2-leaf2a | Interface State | Ethernet Interface & Line Protocol == \"up\" | Ethernet8 - DC2-LEAF2C_Ethernet1 | SKIPPED | Dry run! |
| 438 | dc2-leaf2a | Interface State | Loopback Interface Status & Line Protocol == \"up\" | Loopback0 - EVPN_Overlay_Peering | SKIPPED | Dry run! |
| 439 | dc2-leaf2a | Interface State | Loopback Interface Status & Line Protocol == \"up\" | Loopback1 - VTEP_VXLAN_Tunnel_Source | SKIPPED | Dry run! |
| 440 | dc2-leaf2a | Interface State | Loopback Interface Status & Line Protocol == \"up\" | Loopback10 - VRF10_VTEP_DIAGNOSTICS | SKIPPED | Dry run! |
| 441 | dc2-leaf2a | Interface State | Loopback Interface Status & Line Protocol == \"up\" | Loopback11 - VRF11_VTEP_DIAGNOSTICS | SKIPPED | Dry run! |
| 442 | dc2-leaf2a | Interface State | Port-Channel Interface & Line Protocol == \"up\" | Port-Channel3 - MLAG_PEER_dc2-leaf2b_Po3 | SKIPPED | Dry run! |
| 443 | dc2-leaf2a | Interface State | Port-Channel Interface & Line Protocol == \"up\" | Port-Channel5 - dc2-leaf2-server1_PortChannel dc2-leaf2-server1 | SKIPPED | Dry run! |
| 444 | dc2-leaf2a | Interface State | Port-Channel Interface & Line Protocol == \"up\" | Port-Channel8 - DC2-LEAF2C_Po1 | SKIPPED | Dry run! |
| 445 | dc2-leaf2a | Interface State | Vlan Interface & Line Protocol == \"up\" | Vlan11 - VRF10_VLAN11 | SKIPPED | Dry run! |
| 446 | dc2-leaf2a | Interface State | Vlan Interface & Line Protocol == \"up\" | Vlan12 - VRF10_VLAN12 | SKIPPED | Dry run! |
| 447 | dc2-leaf2a | Interface State | Vlan Interface & Line Protocol == \"up\" | Vlan21 - VRF11_VLAN21 | SKIPPED | Dry run! |
| 448 | dc2-leaf2a | Interface State | Vlan Interface & Line Protocol == \"up\" | Vlan22 - VRF11_VLAN22 | SKIPPED | Dry run! |
| 449 | dc2-leaf2a | Interface State | Vlan Interface & Line Protocol == \"up\" | Vlan3009 - MLAG_PEER_L3_iBGP: vrf VRF10 | SKIPPED | Dry run! |
| 450 | dc2-leaf2a | Interface State | Vlan Interface & Line Protocol == \"up\" | Vlan3010 - MLAG_PEER_L3_iBGP: vrf VRF11 | SKIPPED | Dry run! |
| 451 | dc2-leaf2a | Interface State | Vlan Interface & Line Protocol == \"up\" | Vlan4093 - MLAG_PEER_L3_PEERING | SKIPPED | Dry run! |
| 452 | dc2-leaf2a | Interface State | Vlan Interface & Line Protocol == \"up\" | Vlan4094 - MLAG_PEER | SKIPPED | Dry run! |
| 453 | dc2-leaf2a | Interface State | Vxlan Interface Status & Line Protocol == \"up\" | Vxlan1 | SKIPPED | Dry run! |
| 454 | dc2-leaf2a | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet1 - remote: dc2-spine1_Ethernet3 | SKIPPED | Dry run! |
| 455 | dc2-leaf2a | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet2 - remote: dc2-spine2_Ethernet3 | SKIPPED | Dry run! |
| 456 | dc2-leaf2a | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet3 - remote: dc2-leaf2b_Ethernet3 | SKIPPED | Dry run! |
| 457 | dc2-leaf2a | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet4 - remote: dc2-leaf2b_Ethernet4 | SKIPPED | Dry run! |
| 458 | dc2-leaf2a | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet6 - remote: dc1-leaf2a_Ethernet6 | SKIPPED | Dry run! |
| 459 | dc2-leaf2a | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet8 - remote: dc2-leaf2c_Ethernet1 | SKIPPED | Dry run! |
| 460 | dc2-leaf2a | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf2a - 10.255.128.15/32 Destination: 10.255.0.1 | SKIPPED | Dry run! |
| 461 | dc2-leaf2a | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf2a - 10.255.128.15/32 Destination: 10.255.0.2 | SKIPPED | Dry run! |
| 462 | dc2-leaf2a | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf2a - 10.255.128.15/32 Destination: 10.255.0.3 | SKIPPED | Dry run! |
| 463 | dc2-leaf2a | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf2a - 10.255.128.15/32 Destination: 10.255.0.4 | SKIPPED | Dry run! |
| 464 | dc2-leaf2a | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf2a - 10.255.128.15/32 Destination: 10.255.0.5 | SKIPPED | Dry run! |
| 465 | dc2-leaf2a | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf2a - 10.255.128.15/32 Destination: 10.255.128.11 | SKIPPED | Dry run! |
| 466 | dc2-leaf2a | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf2a - 10.255.128.15/32 Destination: 10.255.128.12 | SKIPPED | Dry run! |
| 467 | dc2-leaf2a | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf2a - 10.255.128.15/32 Destination: 10.255.128.13 | SKIPPED | Dry run! |
| 468 | dc2-leaf2a | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf2a - 10.255.128.15/32 Destination: 10.255.128.14 | SKIPPED | Dry run! |
| 469 | dc2-leaf2a | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf2a - 10.255.128.15/32 Destination: 10.255.128.15 | SKIPPED | Dry run! |
| 470 | dc2-leaf2a | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf2a - 10.255.128.15/32 Destination: 10.255.128.16 | SKIPPED | Dry run! |
| 471 | dc2-leaf2a | MLAG | MLAG State active & Status connected | MLAG | SKIPPED | Dry run! |
| 472 | dc2-leaf2a | NTP | Synchronised with NTP server | NTP | SKIPPED | Dry run! |
| 473 | dc2-leaf2a | Routing Table | Remote Lo0 address | 10.255.0.1 | SKIPPED | Dry run! |
| 474 | dc2-leaf2a | Routing Table | Remote Lo0 address | 10.255.0.2 | SKIPPED | Dry run! |
| 475 | dc2-leaf2a | Routing Table | Remote Lo0 address | 10.255.0.3 | SKIPPED | Dry run! |
| 476 | dc2-leaf2a | Routing Table | Remote Lo0 address | 10.255.0.4 | SKIPPED | Dry run! |
| 477 | dc2-leaf2a | Routing Table | Remote Lo0 address | 10.255.0.5 | SKIPPED | Dry run! |
| 478 | dc2-leaf2a | Routing Table | Remote VTEP address | 10.255.1.3 | SKIPPED | Dry run! |
| 479 | dc2-leaf2a | Routing Table | Remote VTEP address | 10.255.1.5 | SKIPPED | Dry run! |
| 480 | dc2-leaf2a | Routing Table | Remote Lo0 address | 10.255.128.11 | SKIPPED | Dry run! |
| 481 | dc2-leaf2a | Routing Table | Remote Lo0 address | 10.255.128.12 | SKIPPED | Dry run! |
| 482 | dc2-leaf2a | Routing Table | Remote Lo0 address | 10.255.128.13 | SKIPPED | Dry run! |
| 483 | dc2-leaf2a | Routing Table | Remote Lo0 address | 10.255.128.14 | SKIPPED | Dry run! |
| 484 | dc2-leaf2a | Routing Table | Remote Lo0 address | 10.255.128.15 | SKIPPED | Dry run! |
| 485 | dc2-leaf2a | Routing Table | Remote Lo0 address | 10.255.128.16 | SKIPPED | Dry run! |
| 486 | dc2-leaf2a | Routing Table | Remote VTEP address | 10.255.129.13 | SKIPPED | Dry run! |
| 487 | dc2-leaf2a | Routing Table | Remote VTEP address | 10.255.129.15 | SKIPPED | Dry run! |
| 488 | dc2-leaf2b | BGP | ArBGP is configured and operating | ArBGP | SKIPPED | Dry run! |
| 489 | dc2-leaf2b | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.255.128.11 | SKIPPED | Dry run! |
| 490 | dc2-leaf2b | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.255.128.12 | SKIPPED | Dry run! |
| 491 | dc2-leaf2b | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.255.129.120 | SKIPPED | Dry run! |
| 492 | dc2-leaf2b | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.255.255.116 | SKIPPED | Dry run! |
| 493 | dc2-leaf2b | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.255.255.118 | SKIPPED | Dry run! |
| 494 | dc2-leaf2b | Hardware | Verifies if the power supplies status are within the accepted states list. | VerifyEnvironmentPower | SKIPPED | Dry run! |
| 495 | dc2-leaf2b | Hardware | Verifies if the fans status are within the accepted states list. | VerifyEnvironmentCooling | SKIPPED | Dry run! |
| 496 | dc2-leaf2b | Hardware | Verifies if the device temperature is within the acceptable range. | VerifyTemperature | SKIPPED | Dry run! |
| 497 | dc2-leaf2b | Hardware | Verifies the transceiver's manufacturer against a list of approved manufacturers. | VerifyTransceiversManufacturers | SKIPPED | Dry run! |
| 498 | dc2-leaf2b | IP Reachability | ip reachability test p2p links | Source: dc2-leaf2b_Ethernet1 - Destination: dc2-spine1_Ethernet4 | SKIPPED | Dry run! |
| 499 | dc2-leaf2b | IP Reachability | ip reachability test p2p links | Source: dc2-leaf2b_Ethernet2 - Destination: dc2-spine2_Ethernet4 | SKIPPED | Dry run! |
| 500 | dc2-leaf2b | Interface State | Ethernet Interface & Line Protocol == \"up\" | Ethernet1 - P2P_LINK_TO_DC2-SPINE1_Ethernet4 | SKIPPED | Dry run! |
| 501 | dc2-leaf2b | Interface State | Ethernet Interface & Line Protocol == \"up\" | Ethernet2 - P2P_LINK_TO_DC2-SPINE2_Ethernet4 | SKIPPED | Dry run! |
| 502 | dc2-leaf2b | Interface State | Ethernet Interface & Line Protocol == \"up\" | Ethernet3 - MLAG_PEER_dc2-leaf2a_Ethernet3 | SKIPPED | Dry run! |
| 503 | dc2-leaf2b | Interface State | Ethernet Interface & Line Protocol == \"up\" | Ethernet4 - MLAG_PEER_dc2-leaf2a_Ethernet4 | SKIPPED | Dry run! |
| 504 | dc2-leaf2b | Interface State | Ethernet Interface & Line Protocol == \"up\" | Ethernet5 - dc2-leaf2-server1_PCI2 | SKIPPED | Dry run! |
| 505 | dc2-leaf2b | Interface State | Ethernet Interface & Line Protocol == \"up\" | Ethernet6 - P2P_LINK_TO_dc1-leaf2b_Ethernet6 | SKIPPED | Dry run! |
| 506 | dc2-leaf2b | Interface State | Ethernet Interface & Line Protocol == \"up\" | Ethernet8 - DC2-LEAF2C_Ethernet2 | SKIPPED | Dry run! |
| 507 | dc2-leaf2b | Interface State | Loopback Interface Status & Line Protocol == \"up\" | Loopback0 - EVPN_Overlay_Peering | SKIPPED | Dry run! |
| 508 | dc2-leaf2b | Interface State | Loopback Interface Status & Line Protocol == \"up\" | Loopback1 - VTEP_VXLAN_Tunnel_Source | SKIPPED | Dry run! |
| 509 | dc2-leaf2b | Interface State | Loopback Interface Status & Line Protocol == \"up\" | Loopback10 - VRF10_VTEP_DIAGNOSTICS | SKIPPED | Dry run! |
| 510 | dc2-leaf2b | Interface State | Loopback Interface Status & Line Protocol == \"up\" | Loopback11 - VRF11_VTEP_DIAGNOSTICS | SKIPPED | Dry run! |
| 511 | dc2-leaf2b | Interface State | Port-Channel Interface & Line Protocol == \"up\" | Port-Channel3 - MLAG_PEER_dc2-leaf2a_Po3 | SKIPPED | Dry run! |
| 512 | dc2-leaf2b | Interface State | Port-Channel Interface & Line Protocol == \"up\" | Port-Channel5 - dc2-leaf2-server1_PortChannel dc2-leaf2-server1 | SKIPPED | Dry run! |
| 513 | dc2-leaf2b | Interface State | Port-Channel Interface & Line Protocol == \"up\" | Port-Channel8 - DC2-LEAF2C_Po1 | SKIPPED | Dry run! |
| 514 | dc2-leaf2b | Interface State | Vlan Interface & Line Protocol == \"up\" | Vlan11 - VRF10_VLAN11 | SKIPPED | Dry run! |
| 515 | dc2-leaf2b | Interface State | Vlan Interface & Line Protocol == \"up\" | Vlan12 - VRF10_VLAN12 | SKIPPED | Dry run! |
| 516 | dc2-leaf2b | Interface State | Vlan Interface & Line Protocol == \"up\" | Vlan21 - VRF11_VLAN21 | SKIPPED | Dry run! |
| 517 | dc2-leaf2b | Interface State | Vlan Interface & Line Protocol == \"up\" | Vlan22 - VRF11_VLAN22 | SKIPPED | Dry run! |
| 518 | dc2-leaf2b | Interface State | Vlan Interface & Line Protocol == \"up\" | Vlan3009 - MLAG_PEER_L3_iBGP: vrf VRF10 | SKIPPED | Dry run! |
| 519 | dc2-leaf2b | Interface State | Vlan Interface & Line Protocol == \"up\" | Vlan3010 - MLAG_PEER_L3_iBGP: vrf VRF11 | SKIPPED | Dry run! |
| 520 | dc2-leaf2b | Interface State | Vlan Interface & Line Protocol == \"up\" | Vlan4093 - MLAG_PEER_L3_PEERING | SKIPPED | Dry run! |
| 521 | dc2-leaf2b | Interface State | Vlan Interface & Line Protocol == \"up\" | Vlan4094 - MLAG_PEER | SKIPPED | Dry run! |
| 522 | dc2-leaf2b | Interface State | Vxlan Interface Status & Line Protocol == \"up\" | Vxlan1 | SKIPPED | Dry run! |
| 523 | dc2-leaf2b | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet1 - remote: dc2-spine1_Ethernet4 | SKIPPED | Dry run! |
| 524 | dc2-leaf2b | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet2 - remote: dc2-spine2_Ethernet4 | SKIPPED | Dry run! |
| 525 | dc2-leaf2b | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet3 - remote: dc2-leaf2a_Ethernet3 | SKIPPED | Dry run! |
| 526 | dc2-leaf2b | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet4 - remote: dc2-leaf2a_Ethernet4 | SKIPPED | Dry run! |
| 527 | dc2-leaf2b | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet8 - remote: dc2-leaf2c_Ethernet2 | SKIPPED | Dry run! |
| 528 | dc2-leaf2b | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf2b - 10.255.128.16/32 Destination: 10.255.0.1 | SKIPPED | Dry run! |
| 529 | dc2-leaf2b | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf2b - 10.255.128.16/32 Destination: 10.255.0.2 | SKIPPED | Dry run! |
| 530 | dc2-leaf2b | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf2b - 10.255.128.16/32 Destination: 10.255.0.3 | SKIPPED | Dry run! |
| 531 | dc2-leaf2b | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf2b - 10.255.128.16/32 Destination: 10.255.0.4 | SKIPPED | Dry run! |
| 532 | dc2-leaf2b | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf2b - 10.255.128.16/32 Destination: 10.255.0.5 | SKIPPED | Dry run! |
| 533 | dc2-leaf2b | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf2b - 10.255.128.16/32 Destination: 10.255.128.11 | SKIPPED | Dry run! |
| 534 | dc2-leaf2b | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf2b - 10.255.128.16/32 Destination: 10.255.128.12 | SKIPPED | Dry run! |
| 535 | dc2-leaf2b | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf2b - 10.255.128.16/32 Destination: 10.255.128.13 | SKIPPED | Dry run! |
| 536 | dc2-leaf2b | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf2b - 10.255.128.16/32 Destination: 10.255.128.14 | SKIPPED | Dry run! |
| 537 | dc2-leaf2b | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf2b - 10.255.128.16/32 Destination: 10.255.128.15 | SKIPPED | Dry run! |
| 538 | dc2-leaf2b | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf2b - 10.255.128.16/32 Destination: 10.255.128.16 | SKIPPED | Dry run! |
| 539 | dc2-leaf2b | MLAG | MLAG State active & Status connected | MLAG | SKIPPED | Dry run! |
| 540 | dc2-leaf2b | NTP | Synchronised with NTP server | NTP | SKIPPED | Dry run! |
| 541 | dc2-leaf2b | Routing Table | Remote Lo0 address | 10.255.0.1 | SKIPPED | Dry run! |
| 542 | dc2-leaf2b | Routing Table | Remote Lo0 address | 10.255.0.2 | SKIPPED | Dry run! |
| 543 | dc2-leaf2b | Routing Table | Remote Lo0 address | 10.255.0.3 | SKIPPED | Dry run! |
| 544 | dc2-leaf2b | Routing Table | Remote Lo0 address | 10.255.0.4 | SKIPPED | Dry run! |
| 545 | dc2-leaf2b | Routing Table | Remote Lo0 address | 10.255.0.5 | SKIPPED | Dry run! |
| 546 | dc2-leaf2b | Routing Table | Remote VTEP address | 10.255.1.3 | SKIPPED | Dry run! |
| 547 | dc2-leaf2b | Routing Table | Remote VTEP address | 10.255.1.5 | SKIPPED | Dry run! |
| 548 | dc2-leaf2b | Routing Table | Remote Lo0 address | 10.255.128.11 | SKIPPED | Dry run! |
| 549 | dc2-leaf2b | Routing Table | Remote Lo0 address | 10.255.128.12 | SKIPPED | Dry run! |
| 550 | dc2-leaf2b | Routing Table | Remote Lo0 address | 10.255.128.13 | SKIPPED | Dry run! |
| 551 | dc2-leaf2b | Routing Table | Remote Lo0 address | 10.255.128.14 | SKIPPED | Dry run! |
| 552 | dc2-leaf2b | Routing Table | Remote Lo0 address | 10.255.128.15 | SKIPPED | Dry run! |
| 553 | dc2-leaf2b | Routing Table | Remote Lo0 address | 10.255.128.16 | SKIPPED | Dry run! |
| 554 | dc2-leaf2b | Routing Table | Remote VTEP address | 10.255.129.13 | SKIPPED | Dry run! |
| 555 | dc2-leaf2b | Routing Table | Remote VTEP address | 10.255.129.15 | SKIPPED | Dry run! |
| 556 | dc2-leaf2c | Hardware | Verifies if the power supplies status are within the accepted states list. | VerifyEnvironmentPower | SKIPPED | Dry run! |
| 557 | dc2-leaf2c | Hardware | Verifies if the fans status are within the accepted states list. | VerifyEnvironmentCooling | SKIPPED | Dry run! |
| 558 | dc2-leaf2c | Hardware | Verifies if the device temperature is within the acceptable range. | VerifyTemperature | SKIPPED | Dry run! |
| 559 | dc2-leaf2c | Hardware | Verifies the transceiver's manufacturer against a list of approved manufacturers. | VerifyTransceiversManufacturers | SKIPPED | Dry run! |
| 560 | dc2-leaf2c | Interface State | Ethernet Interface & Line Protocol == \"up\" | Ethernet1 - DC2-LEAF2A_Ethernet8 | SKIPPED | Dry run! |
| 561 | dc2-leaf2c | Interface State | Ethernet Interface & Line Protocol == \"up\" | Ethernet2 - DC2-LEAF2B_Ethernet8 | SKIPPED | Dry run! |
| 562 | dc2-leaf2c | Interface State | Ethernet Interface & Line Protocol == \"up\" | Ethernet5 - dc2-leaf2-server1_iLO | SKIPPED | Dry run! |
| 563 | dc2-leaf2c | Interface State | Port-Channel Interface & Line Protocol == \"up\" | Port-Channel1 - DC2_L3_LEAF2_Po8 | SKIPPED | Dry run! |
| 564 | dc2-leaf2c | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet1 - remote: dc2-leaf2a_Ethernet8 | SKIPPED | Dry run! |
| 565 | dc2-leaf2c | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet2 - remote: dc2-leaf2b_Ethernet8 | SKIPPED | Dry run! |
| 566 | dc2-leaf2c | NTP | Synchronised with NTP server | NTP | SKIPPED | Dry run! |
| 567 | dc2-spine1 | BGP | ArBGP is configured and operating | ArBGP | SKIPPED | Dry run! |
| 568 | dc2-spine1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.255.128.13 | SKIPPED | Dry run! |
| 569 | dc2-spine1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.255.128.14 | SKIPPED | Dry run! |
| 570 | dc2-spine1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.255.128.15 | SKIPPED | Dry run! |
| 571 | dc2-spine1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.255.128.16 | SKIPPED | Dry run! |
| 572 | dc2-spine1 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.255.255.105 | SKIPPED | Dry run! |
| 573 | dc2-spine1 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.255.255.109 | SKIPPED | Dry run! |
| 574 | dc2-spine1 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.255.255.113 | SKIPPED | Dry run! |
| 575 | dc2-spine1 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.255.255.117 | SKIPPED | Dry run! |
| 576 | dc2-spine1 | Hardware | Verifies if the power supplies status are within the accepted states list. | VerifyEnvironmentPower | SKIPPED | Dry run! |
| 577 | dc2-spine1 | Hardware | Verifies if the fans status are within the accepted states list. | VerifyEnvironmentCooling | SKIPPED | Dry run! |
| 578 | dc2-spine1 | Hardware | Verifies if the device temperature is within the acceptable range. | VerifyTemperature | SKIPPED | Dry run! |
| 579 | dc2-spine1 | Hardware | Verifies the transceiver's manufacturer against a list of approved manufacturers. | VerifyTransceiversManufacturers | SKIPPED | Dry run! |
| 580 | dc2-spine1 | IP Reachability | ip reachability test p2p links | Source: dc2-spine1_Ethernet1 - Destination: dc2-leaf1a_Ethernet1 | SKIPPED | Dry run! |
| 581 | dc2-spine1 | IP Reachability | ip reachability test p2p links | Source: dc2-spine1_Ethernet2 - Destination: dc2-leaf1b_Ethernet1 | SKIPPED | Dry run! |
| 582 | dc2-spine1 | IP Reachability | ip reachability test p2p links | Source: dc2-spine1_Ethernet3 - Destination: dc2-leaf2a_Ethernet1 | SKIPPED | Dry run! |
| 583 | dc2-spine1 | IP Reachability | ip reachability test p2p links | Source: dc2-spine1_Ethernet4 - Destination: dc2-leaf2b_Ethernet1 | SKIPPED | Dry run! |
| 584 | dc2-spine1 | Interface State | Ethernet Interface & Line Protocol == \"up\" | Ethernet1 - P2P_LINK_TO_DC2-LEAF1A_Ethernet1 | SKIPPED | Dry run! |
| 585 | dc2-spine1 | Interface State | Ethernet Interface & Line Protocol == \"up\" | Ethernet2 - P2P_LINK_TO_DC2-LEAF1B_Ethernet1 | SKIPPED | Dry run! |
| 586 | dc2-spine1 | Interface State | Ethernet Interface & Line Protocol == \"up\" | Ethernet3 - P2P_LINK_TO_DC2-LEAF2A_Ethernet1 | SKIPPED | Dry run! |
| 587 | dc2-spine1 | Interface State | Ethernet Interface & Line Protocol == \"up\" | Ethernet4 - P2P_LINK_TO_DC2-LEAF2B_Ethernet1 | SKIPPED | Dry run! |
| 588 | dc2-spine1 | Interface State | Loopback Interface Status & Line Protocol == \"up\" | Loopback0 - EVPN_Overlay_Peering | SKIPPED | Dry run! |
| 589 | dc2-spine1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet1 - remote: dc2-leaf1a_Ethernet1 | SKIPPED | Dry run! |
| 590 | dc2-spine1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet2 - remote: dc2-leaf1b_Ethernet1 | SKIPPED | Dry run! |
| 591 | dc2-spine1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet3 - remote: dc2-leaf2a_Ethernet1 | SKIPPED | Dry run! |
| 592 | dc2-spine1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet4 - remote: dc2-leaf2b_Ethernet1 | SKIPPED | Dry run! |
| 593 | dc2-spine1 | NTP | Synchronised with NTP server | NTP | SKIPPED | Dry run! |
| 594 | dc2-spine2 | BGP | ArBGP is configured and operating | ArBGP | SKIPPED | Dry run! |
| 595 | dc2-spine2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.255.128.13 | SKIPPED | Dry run! |
| 596 | dc2-spine2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.255.128.14 | SKIPPED | Dry run! |
| 597 | dc2-spine2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.255.128.15 | SKIPPED | Dry run! |
| 598 | dc2-spine2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.255.128.16 | SKIPPED | Dry run! |
| 599 | dc2-spine2 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.255.255.107 | SKIPPED | Dry run! |
| 600 | dc2-spine2 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.255.255.111 | SKIPPED | Dry run! |
| 601 | dc2-spine2 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.255.255.115 | SKIPPED | Dry run! |
| 602 | dc2-spine2 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.255.255.119 | SKIPPED | Dry run! |
| 603 | dc2-spine2 | Hardware | Verifies if the power supplies status are within the accepted states list. | VerifyEnvironmentPower | SKIPPED | Dry run! |
| 604 | dc2-spine2 | Hardware | Verifies if the fans status are within the accepted states list. | VerifyEnvironmentCooling | SKIPPED | Dry run! |
| 605 | dc2-spine2 | Hardware | Verifies if the device temperature is within the acceptable range. | VerifyTemperature | SKIPPED | Dry run! |
| 606 | dc2-spine2 | Hardware | Verifies the transceiver's manufacturer against a list of approved manufacturers. | VerifyTransceiversManufacturers | SKIPPED | Dry run! |
| 607 | dc2-spine2 | IP Reachability | ip reachability test p2p links | Source: dc2-spine2_Ethernet1 - Destination: dc2-leaf1a_Ethernet2 | SKIPPED | Dry run! |
| 608 | dc2-spine2 | IP Reachability | ip reachability test p2p links | Source: dc2-spine2_Ethernet2 - Destination: dc2-leaf1b_Ethernet2 | SKIPPED | Dry run! |
| 609 | dc2-spine2 | IP Reachability | ip reachability test p2p links | Source: dc2-spine2_Ethernet3 - Destination: dc2-leaf2a_Ethernet2 | SKIPPED | Dry run! |
| 610 | dc2-spine2 | IP Reachability | ip reachability test p2p links | Source: dc2-spine2_Ethernet4 - Destination: dc2-leaf2b_Ethernet2 | SKIPPED | Dry run! |
| 611 | dc2-spine2 | Interface State | Ethernet Interface & Line Protocol == \"up\" | Ethernet1 - P2P_LINK_TO_DC2-LEAF1A_Ethernet2 | SKIPPED | Dry run! |
| 612 | dc2-spine2 | Interface State | Ethernet Interface & Line Protocol == \"up\" | Ethernet2 - P2P_LINK_TO_DC2-LEAF1B_Ethernet2 | SKIPPED | Dry run! |
| 613 | dc2-spine2 | Interface State | Ethernet Interface & Line Protocol == \"up\" | Ethernet3 - P2P_LINK_TO_DC2-LEAF2A_Ethernet2 | SKIPPED | Dry run! |
| 614 | dc2-spine2 | Interface State | Ethernet Interface & Line Protocol == \"up\" | Ethernet4 - P2P_LINK_TO_DC2-LEAF2B_Ethernet2 | SKIPPED | Dry run! |
| 615 | dc2-spine2 | Interface State | Loopback Interface Status & Line Protocol == \"up\" | Loopback0 - EVPN_Overlay_Peering | SKIPPED | Dry run! |
| 616 | dc2-spine2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet1 - remote: dc2-leaf1a_Ethernet2 | SKIPPED | Dry run! |
| 617 | dc2-spine2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet2 - remote: dc2-leaf1b_Ethernet2 | SKIPPED | Dry run! |
| 618 | dc2-spine2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet3 - remote: dc2-leaf2a_Ethernet2 | SKIPPED | Dry run! |
| 619 | dc2-spine2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet4 - remote: dc2-leaf2b_Ethernet2 | SKIPPED | Dry run! |
| 620 | dc2-spine2 | NTP | Synchronised with NTP server | NTP | SKIPPED | Dry run! |

