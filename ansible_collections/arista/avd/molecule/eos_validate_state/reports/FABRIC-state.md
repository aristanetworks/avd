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
| 830 | 0 | 0 | 0 |

### Summary Totals Devices Under Tests

| DUT | Total Tests | Tests Passed | Tests Failed | Tests Skipped | Categories Failed | Categories Skipped |
| --- | ----------- | ------------ | ------------ | ------------- | ----------------- | ------------------ |
| dc1-leaf1a | 73 | 0 | 0 | 0 | - | - |
| dc1-leaf1b | 73 | 0 | 0 | 0 | - | - |
| dc1-leaf1c | 12 | 0 | 0 | 0 | - | - |
| dc1-leaf2a | 75 | 0 | 0 | 0 | - | - |
| dc1-leaf2c | 11 | 0 | 0 | 0 | - | - |
| dc1-spine1 | 24 | 0 | 0 | 0 | - | - |
| dc1-spine2 | 24 | 0 | 0 | 0 | - | - |
| dc2-leaf1a | 73 | 0 | 0 | 0 | - | - |
| dc2-leaf1b | 73 | 0 | 0 | 0 | - | - |
| dc2-leaf1c | 12 | 0 | 0 | 0 | - | - |
| dc2-leaf2a | 78 | 0 | 0 | 0 | - | - |
| dc2-leaf2b | 74 | 0 | 0 | 0 | - | - |
| dc2-leaf2c | 12 | 0 | 0 | 0 | - | - |
| dc2-leaf3a.arista.com | 70 | 0 | 0 | 0 | - | - |
| dc2-leaf3b.arista.com | 70 | 0 | 0 | 0 | - | - |
| dc2-spine1 | 38 | 0 | 0 | 0 | - | - |
| dc2-spine2 | 38 | 0 | 0 | 0 | - | - |

### Summary Totals Per Category

| Test Category | Total Tests | Tests Passed | Tests Failed | Tests Skipped |
| ------------- | ----------- | ------------ | ------------ | ------------- |
| BGP | 97 | 0 | 0 | 0 |
| Hardware | 68 | 0 | 0 | 0 |
| Interface State | 237 | 0 | 0 | 0 |
| IP Reachability | 38 | 0 | 0 | 0 |
| LLDP Topology | 68 | 0 | 0 | 0 |
| Loopback0 Reachability | 117 | 0 | 0 | 0 |
| MLAG | 9 | 0 | 0 | 0 |
| NTP | 17 | 0 | 0 | 0 |
| Routing Table | 162 | 0 | 0 | 0 |
| Security | 17 | 0 | 0 | 0 |

## Failed Test Results Summary

| Test ID | Node | Test Categories | Test Description | Test | Test Result | Messages |
| ------- | ---- | --------------- | ---------------- | ---- | ----------- | -------- |

## All Test Results

| Test ID | Node | Test Categories | Test Description | Test | Test Result | Messages |
| ------- | ---- | --------------- | ---------------- | ---- | ----------- | -------- |
| 1 | dc1-leaf1a | BGP | ArBGP is configured and operating | ArBGP | NOT RUN | - |
| 2 | dc1-leaf1a | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.255.0.1 | NOT RUN | - |
| 3 | dc1-leaf1a | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.255.0.2 | NOT RUN | - |
| 4 | dc1-leaf1a | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.255.1.97 | NOT RUN | - |
| 5 | dc1-leaf1a | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.255.255.0 | NOT RUN | - |
| 6 | dc1-leaf1a | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.255.255.2 | NOT RUN | - |
| 7 | dc1-leaf1a | Hardware | Verifies if the device temperature is within the acceptable range. | VerifyTemperature | NOT RUN | - |
| 8 | dc1-leaf1a | Hardware | Verifies if the fans status are within the accepted states list. | VerifyEnvironmentCooling | NOT RUN | - |
| 9 | dc1-leaf1a | Hardware | Verifies if the power supplies status are within the accepted states list. | VerifyEnvironmentPower | NOT RUN | - |
| 10 | dc1-leaf1a | Hardware | Verifies the transceiver's manufacturer against a list of approved manufacturers. | VerifyTransceiversManufacturers | NOT RUN | - |
| 11 | dc1-leaf1a | Interface State | Ethernet Interface & Line Protocol == 'up' | Ethernet1 - P2P_LINK_TO_DC1-SPINE1_Ethernet1 | NOT RUN | - |
| 12 | dc1-leaf1a | Interface State | Ethernet Interface & Line Protocol == 'up' | Ethernet2 - P2P_LINK_TO_DC1-SPINE2_Ethernet1 | NOT RUN | - |
| 13 | dc1-leaf1a | Interface State | Ethernet Interface & Line Protocol == 'up' | Ethernet3 - MLAG_PEER_dc1-leaf1b_Ethernet3 | NOT RUN | - |
| 14 | dc1-leaf1a | Interface State | Ethernet Interface & Line Protocol == 'up' | Ethernet4 - MLAG_PEER_dc1-leaf1b_Ethernet4 | NOT RUN | - |
| 15 | dc1-leaf1a | Interface State | Ethernet Interface & Line Protocol == 'up' | Ethernet5 - dc1-leaf1-server1_PCI1 | NOT RUN | - |
| 16 | dc1-leaf1a | Interface State | Ethernet Interface & Line Protocol == 'up' | Ethernet8 - DC1-LEAF1C_Ethernet1 | NOT RUN | - |
| 17 | dc1-leaf1a | Interface State | Loopback Interface Status & Line Protocol == 'up' | Loopback0 - EVPN_Overlay_Peering | NOT RUN | - |
| 18 | dc1-leaf1a | Interface State | Loopback Interface Status & Line Protocol == 'up' | Loopback1 - VTEP_VXLAN_Tunnel_Source | NOT RUN | - |
| 19 | dc1-leaf1a | Interface State | Loopback Interface Status & Line Protocol == 'up' | Loopback10 - VRF10_VTEP_DIAGNOSTICS | NOT RUN | - |
| 20 | dc1-leaf1a | Interface State | Loopback Interface Status & Line Protocol == 'up' | Loopback11 - VRF11_VTEP_DIAGNOSTICS | NOT RUN | - |
| 21 | dc1-leaf1a | Interface State | Port-Channel Interface & Line Protocol == 'up' | Port-Channel3 - MLAG_PEER_dc1-leaf1b_Po3 | NOT RUN | - |
| 22 | dc1-leaf1a | Interface State | Port-Channel Interface & Line Protocol == 'up' | Port-Channel5 - dc1-leaf1-server1_PortChannel dc1-leaf1-server1 | NOT RUN | - |
| 23 | dc1-leaf1a | Interface State | Port-Channel Interface & Line Protocol == 'up' | Port-Channel8 - DC1-LEAF1C_Po1 | NOT RUN | - |
| 24 | dc1-leaf1a | Interface State | Vlan Interface & Line Protocol == 'up' | Vlan11 - VRF10_VLAN11 | NOT RUN | - |
| 25 | dc1-leaf1a | Interface State | Vlan Interface & Line Protocol == 'up' | Vlan12 - VRF10_VLAN12 | NOT RUN | - |
| 26 | dc1-leaf1a | Interface State | Vlan Interface & Line Protocol == 'up' | Vlan21 - VRF11_VLAN21 | NOT RUN | - |
| 27 | dc1-leaf1a | Interface State | Vlan Interface & Line Protocol == 'up' | Vlan22 - VRF11_VLAN22 | NOT RUN | - |
| 28 | dc1-leaf1a | Interface State | Vlan Interface & Line Protocol == 'up' | Vlan3009 - MLAG_PEER_L3_iBGP: vrf VRF10 | NOT RUN | - |
| 29 | dc1-leaf1a | Interface State | Vlan Interface & Line Protocol == 'up' | Vlan3010 - MLAG_PEER_L3_iBGP: vrf VRF11 | NOT RUN | - |
| 30 | dc1-leaf1a | Interface State | Vlan Interface & Line Protocol == 'up' | Vlan4093 - MLAG_PEER_L3_PEERING | NOT RUN | - |
| 31 | dc1-leaf1a | Interface State | Vlan Interface & Line Protocol == 'up' | Vlan4094 - MLAG_PEER | NOT RUN | - |
| 32 | dc1-leaf1a | Interface State | Vxlan Interface Status & Line Protocol == 'up' | Vxlan1 | NOT RUN | - |
| 33 | dc1-leaf1a | IP Reachability | ip reachability test p2p links | Source: dc1-leaf1a_Ethernet1 - Destination: dc1-spine1_Ethernet1 | NOT RUN | - |
| 34 | dc1-leaf1a | IP Reachability | ip reachability test p2p links | Source: dc1-leaf1a_Ethernet2 - Destination: dc1-spine2_Ethernet1 | NOT RUN | - |
| 35 | dc1-leaf1a | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet1 - remote: dc1-spine1_Ethernet1 | NOT RUN | - |
| 36 | dc1-leaf1a | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet2 - remote: dc1-spine2_Ethernet1 | NOT RUN | - |
| 37 | dc1-leaf1a | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet3 - remote: dc1-leaf1b_Ethernet3 | NOT RUN | - |
| 38 | dc1-leaf1a | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet4 - remote: dc1-leaf1b_Ethernet4 | NOT RUN | - |
| 39 | dc1-leaf1a | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet8 - remote: dc1-leaf1c_Ethernet1 | NOT RUN | - |
| 40 | dc1-leaf1a | Loopback0 Reachability | Loopback0 Reachability | Source: dc1-leaf1a - 10.255.0.3/32 Destination: 10.255.0.1 | NOT RUN | - |
| 41 | dc1-leaf1a | Loopback0 Reachability | Loopback0 Reachability | Source: dc1-leaf1a - 10.255.0.3/32 Destination: 10.255.0.2 | NOT RUN | - |
| 42 | dc1-leaf1a | Loopback0 Reachability | Loopback0 Reachability | Source: dc1-leaf1a - 10.255.0.3/32 Destination: 10.255.0.3 | NOT RUN | - |
| 43 | dc1-leaf1a | Loopback0 Reachability | Loopback0 Reachability | Source: dc1-leaf1a - 10.255.0.3/32 Destination: 10.255.0.4 | NOT RUN | - |
| 44 | dc1-leaf1a | Loopback0 Reachability | Loopback0 Reachability | Source: dc1-leaf1a - 10.255.0.3/32 Destination: 10.255.0.5 | NOT RUN | - |
| 45 | dc1-leaf1a | Loopback0 Reachability | Loopback0 Reachability | Source: dc1-leaf1a - 10.255.0.3/32 Destination: 10.255.128.11 | NOT RUN | - |
| 46 | dc1-leaf1a | Loopback0 Reachability | Loopback0 Reachability | Source: dc1-leaf1a - 10.255.0.3/32 Destination: 10.255.128.12 | NOT RUN | - |
| 47 | dc1-leaf1a | Loopback0 Reachability | Loopback0 Reachability | Source: dc1-leaf1a - 10.255.0.3/32 Destination: 10.255.128.13 | NOT RUN | - |
| 48 | dc1-leaf1a | Loopback0 Reachability | Loopback0 Reachability | Source: dc1-leaf1a - 10.255.0.3/32 Destination: 10.255.128.14 | NOT RUN | - |
| 49 | dc1-leaf1a | Loopback0 Reachability | Loopback0 Reachability | Source: dc1-leaf1a - 10.255.0.3/32 Destination: 10.255.128.15 | NOT RUN | - |
| 50 | dc1-leaf1a | Loopback0 Reachability | Loopback0 Reachability | Source: dc1-leaf1a - 10.255.0.3/32 Destination: 10.255.128.16 | NOT RUN | - |
| 51 | dc1-leaf1a | Loopback0 Reachability | Loopback0 Reachability | Source: dc1-leaf1a - 10.255.0.3/32 Destination: 10.255.128.17 | NOT RUN | - |
| 52 | dc1-leaf1a | Loopback0 Reachability | Loopback0 Reachability | Source: dc1-leaf1a - 10.255.0.3/32 Destination: 10.255.128.18 | NOT RUN | - |
| 53 | dc1-leaf1a | MLAG | This test verifies the health status of the MLAG configuration. | VerifyMlagStatus | NOT RUN | - |
| 54 | dc1-leaf1a | NTP | Synchronised with NTP server | NTP | NOT RUN | - |
| 55 | dc1-leaf1a | Routing Table | Remote Lo0 address | 10.255.0.1 | NOT RUN | - |
| 56 | dc1-leaf1a | Routing Table | Remote Lo0 address | 10.255.0.2 | NOT RUN | - |
| 57 | dc1-leaf1a | Routing Table | Remote Lo0 address | 10.255.0.3 | NOT RUN | - |
| 58 | dc1-leaf1a | Routing Table | Remote Lo0 address | 10.255.0.4 | NOT RUN | - |
| 59 | dc1-leaf1a | Routing Table | Remote Lo0 address | 10.255.0.5 | NOT RUN | - |
| 60 | dc1-leaf1a | Routing Table | Remote Lo0 address | 10.255.128.11 | NOT RUN | - |
| 61 | dc1-leaf1a | Routing Table | Remote Lo0 address | 10.255.128.12 | NOT RUN | - |
| 62 | dc1-leaf1a | Routing Table | Remote Lo0 address | 10.255.128.13 | NOT RUN | - |
| 63 | dc1-leaf1a | Routing Table | Remote Lo0 address | 10.255.128.14 | NOT RUN | - |
| 64 | dc1-leaf1a | Routing Table | Remote Lo0 address | 10.255.128.15 | NOT RUN | - |
| 65 | dc1-leaf1a | Routing Table | Remote Lo0 address | 10.255.128.16 | NOT RUN | - |
| 66 | dc1-leaf1a | Routing Table | Remote Lo0 address | 10.255.128.17 | NOT RUN | - |
| 67 | dc1-leaf1a | Routing Table | Remote Lo0 address | 10.255.128.18 | NOT RUN | - |
| 68 | dc1-leaf1a | Routing Table | Remote VTEP address | 10.255.1.3 | NOT RUN | - |
| 69 | dc1-leaf1a | Routing Table | Remote VTEP address | 10.255.1.5 | NOT RUN | - |
| 70 | dc1-leaf1a | Routing Table | Remote VTEP address | 10.255.129.13 | NOT RUN | - |
| 71 | dc1-leaf1a | Routing Table | Remote VTEP address | 10.255.129.15 | NOT RUN | - |
| 72 | dc1-leaf1a | Routing Table | Remote VTEP address | 10.255.129.17 | NOT RUN | - |
| 73 | dc1-leaf1a | Security | Verifies if eAPI HTTPS server SSL profile is configured and valid. | VerifyAPIHttpsSSL | NOT RUN | - |
| 74 | dc1-leaf1b | BGP | ArBGP is configured and operating | ArBGP | NOT RUN | - |
| 75 | dc1-leaf1b | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.255.0.1 | NOT RUN | - |
| 76 | dc1-leaf1b | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.255.0.2 | NOT RUN | - |
| 77 | dc1-leaf1b | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.255.1.96 | NOT RUN | - |
| 78 | dc1-leaf1b | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.255.255.4 | NOT RUN | - |
| 79 | dc1-leaf1b | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.255.255.6 | NOT RUN | - |
| 80 | dc1-leaf1b | Hardware | Verifies if the device temperature is within the acceptable range. | VerifyTemperature | NOT RUN | - |
| 81 | dc1-leaf1b | Hardware | Verifies if the fans status are within the accepted states list. | VerifyEnvironmentCooling | NOT RUN | - |
| 82 | dc1-leaf1b | Hardware | Verifies if the power supplies status are within the accepted states list. | VerifyEnvironmentPower | NOT RUN | - |
| 83 | dc1-leaf1b | Hardware | Verifies the transceiver's manufacturer against a list of approved manufacturers. | VerifyTransceiversManufacturers | NOT RUN | - |
| 84 | dc1-leaf1b | Interface State | Ethernet Interface & Line Protocol == 'up' | Ethernet1 - P2P_LINK_TO_DC1-SPINE1_Ethernet2 | NOT RUN | - |
| 85 | dc1-leaf1b | Interface State | Ethernet Interface & Line Protocol == 'up' | Ethernet2 - P2P_LINK_TO_DC1-SPINE2_Ethernet2 | NOT RUN | - |
| 86 | dc1-leaf1b | Interface State | Ethernet Interface & Line Protocol == 'up' | Ethernet3 - MLAG_PEER_dc1-leaf1a_Ethernet3 | NOT RUN | - |
| 87 | dc1-leaf1b | Interface State | Ethernet Interface & Line Protocol == 'up' | Ethernet4 - MLAG_PEER_dc1-leaf1a_Ethernet4 | NOT RUN | - |
| 88 | dc1-leaf1b | Interface State | Ethernet Interface & Line Protocol == 'up' | Ethernet5 - dc1-leaf1-server1_PCI2 | NOT RUN | - |
| 89 | dc1-leaf1b | Interface State | Ethernet Interface & Line Protocol == 'up' | Ethernet8 - DC1-LEAF1C_Ethernet2 | NOT RUN | - |
| 90 | dc1-leaf1b | Interface State | Loopback Interface Status & Line Protocol == 'up' | Loopback0 - EVPN_Overlay_Peering | NOT RUN | - |
| 91 | dc1-leaf1b | Interface State | Loopback Interface Status & Line Protocol == 'up' | Loopback1 - VTEP_VXLAN_Tunnel_Source | NOT RUN | - |
| 92 | dc1-leaf1b | Interface State | Loopback Interface Status & Line Protocol == 'up' | Loopback10 - VRF10_VTEP_DIAGNOSTICS | NOT RUN | - |
| 93 | dc1-leaf1b | Interface State | Loopback Interface Status & Line Protocol == 'up' | Loopback11 - VRF11_VTEP_DIAGNOSTICS | NOT RUN | - |
| 94 | dc1-leaf1b | Interface State | Port-Channel Interface & Line Protocol == 'up' | Port-Channel3 - MLAG_PEER_dc1-leaf1a_Po3 | NOT RUN | - |
| 95 | dc1-leaf1b | Interface State | Port-Channel Interface & Line Protocol == 'up' | Port-Channel5 - dc1-leaf1-server1_PortChannel dc1-leaf1-server1 | NOT RUN | - |
| 96 | dc1-leaf1b | Interface State | Port-Channel Interface & Line Protocol == 'up' | Port-Channel8 - DC1-LEAF1C_Po1 | NOT RUN | - |
| 97 | dc1-leaf1b | Interface State | Vlan Interface & Line Protocol == 'up' | Vlan11 - VRF10_VLAN11 | NOT RUN | - |
| 98 | dc1-leaf1b | Interface State | Vlan Interface & Line Protocol == 'up' | Vlan12 - VRF10_VLAN12 | NOT RUN | - |
| 99 | dc1-leaf1b | Interface State | Vlan Interface & Line Protocol == 'up' | Vlan21 - VRF11_VLAN21 | NOT RUN | - |
| 100 | dc1-leaf1b | Interface State | Vlan Interface & Line Protocol == 'up' | Vlan22 - VRF11_VLAN22 | NOT RUN | - |
| 101 | dc1-leaf1b | Interface State | Vlan Interface & Line Protocol == 'up' | Vlan3009 - MLAG_PEER_L3_iBGP: vrf VRF10 | NOT RUN | - |
| 102 | dc1-leaf1b | Interface State | Vlan Interface & Line Protocol == 'up' | Vlan3010 - MLAG_PEER_L3_iBGP: vrf VRF11 | NOT RUN | - |
| 103 | dc1-leaf1b | Interface State | Vlan Interface & Line Protocol == 'up' | Vlan4093 - MLAG_PEER_L3_PEERING | NOT RUN | - |
| 104 | dc1-leaf1b | Interface State | Vlan Interface & Line Protocol == 'up' | Vlan4094 - MLAG_PEER | NOT RUN | - |
| 105 | dc1-leaf1b | Interface State | Vxlan Interface Status & Line Protocol == 'up' | Vxlan1 | NOT RUN | - |
| 106 | dc1-leaf1b | IP Reachability | ip reachability test p2p links | Source: dc1-leaf1b_Ethernet1 - Destination: dc1-spine1_Ethernet2 | NOT RUN | - |
| 107 | dc1-leaf1b | IP Reachability | ip reachability test p2p links | Source: dc1-leaf1b_Ethernet2 - Destination: dc1-spine2_Ethernet2 | NOT RUN | - |
| 108 | dc1-leaf1b | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet1 - remote: dc1-spine1_Ethernet2 | NOT RUN | - |
| 109 | dc1-leaf1b | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet2 - remote: dc1-spine2_Ethernet2 | NOT RUN | - |
| 110 | dc1-leaf1b | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet3 - remote: dc1-leaf1a_Ethernet3 | NOT RUN | - |
| 111 | dc1-leaf1b | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet4 - remote: dc1-leaf1a_Ethernet4 | NOT RUN | - |
| 112 | dc1-leaf1b | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet8 - remote: dc1-leaf1c_Ethernet2 | NOT RUN | - |
| 113 | dc1-leaf1b | Loopback0 Reachability | Loopback0 Reachability | Source: dc1-leaf1b - 10.255.0.4/32 Destination: 10.255.0.1 | NOT RUN | - |
| 114 | dc1-leaf1b | Loopback0 Reachability | Loopback0 Reachability | Source: dc1-leaf1b - 10.255.0.4/32 Destination: 10.255.0.2 | NOT RUN | - |
| 115 | dc1-leaf1b | Loopback0 Reachability | Loopback0 Reachability | Source: dc1-leaf1b - 10.255.0.4/32 Destination: 10.255.0.3 | NOT RUN | - |
| 116 | dc1-leaf1b | Loopback0 Reachability | Loopback0 Reachability | Source: dc1-leaf1b - 10.255.0.4/32 Destination: 10.255.0.4 | NOT RUN | - |
| 117 | dc1-leaf1b | Loopback0 Reachability | Loopback0 Reachability | Source: dc1-leaf1b - 10.255.0.4/32 Destination: 10.255.0.5 | NOT RUN | - |
| 118 | dc1-leaf1b | Loopback0 Reachability | Loopback0 Reachability | Source: dc1-leaf1b - 10.255.0.4/32 Destination: 10.255.128.11 | NOT RUN | - |
| 119 | dc1-leaf1b | Loopback0 Reachability | Loopback0 Reachability | Source: dc1-leaf1b - 10.255.0.4/32 Destination: 10.255.128.12 | NOT RUN | - |
| 120 | dc1-leaf1b | Loopback0 Reachability | Loopback0 Reachability | Source: dc1-leaf1b - 10.255.0.4/32 Destination: 10.255.128.13 | NOT RUN | - |
| 121 | dc1-leaf1b | Loopback0 Reachability | Loopback0 Reachability | Source: dc1-leaf1b - 10.255.0.4/32 Destination: 10.255.128.14 | NOT RUN | - |
| 122 | dc1-leaf1b | Loopback0 Reachability | Loopback0 Reachability | Source: dc1-leaf1b - 10.255.0.4/32 Destination: 10.255.128.15 | NOT RUN | - |
| 123 | dc1-leaf1b | Loopback0 Reachability | Loopback0 Reachability | Source: dc1-leaf1b - 10.255.0.4/32 Destination: 10.255.128.16 | NOT RUN | - |
| 124 | dc1-leaf1b | Loopback0 Reachability | Loopback0 Reachability | Source: dc1-leaf1b - 10.255.0.4/32 Destination: 10.255.128.17 | NOT RUN | - |
| 125 | dc1-leaf1b | Loopback0 Reachability | Loopback0 Reachability | Source: dc1-leaf1b - 10.255.0.4/32 Destination: 10.255.128.18 | NOT RUN | - |
| 126 | dc1-leaf1b | MLAG | This test verifies the health status of the MLAG configuration. | VerifyMlagStatus | NOT RUN | - |
| 127 | dc1-leaf1b | NTP | Synchronised with NTP server | NTP | NOT RUN | - |
| 128 | dc1-leaf1b | Routing Table | Remote Lo0 address | 10.255.0.1 | NOT RUN | - |
| 129 | dc1-leaf1b | Routing Table | Remote Lo0 address | 10.255.0.2 | NOT RUN | - |
| 130 | dc1-leaf1b | Routing Table | Remote Lo0 address | 10.255.0.3 | NOT RUN | - |
| 131 | dc1-leaf1b | Routing Table | Remote Lo0 address | 10.255.0.4 | NOT RUN | - |
| 132 | dc1-leaf1b | Routing Table | Remote Lo0 address | 10.255.0.5 | NOT RUN | - |
| 133 | dc1-leaf1b | Routing Table | Remote Lo0 address | 10.255.128.11 | NOT RUN | - |
| 134 | dc1-leaf1b | Routing Table | Remote Lo0 address | 10.255.128.12 | NOT RUN | - |
| 135 | dc1-leaf1b | Routing Table | Remote Lo0 address | 10.255.128.13 | NOT RUN | - |
| 136 | dc1-leaf1b | Routing Table | Remote Lo0 address | 10.255.128.14 | NOT RUN | - |
| 137 | dc1-leaf1b | Routing Table | Remote Lo0 address | 10.255.128.15 | NOT RUN | - |
| 138 | dc1-leaf1b | Routing Table | Remote Lo0 address | 10.255.128.16 | NOT RUN | - |
| 139 | dc1-leaf1b | Routing Table | Remote Lo0 address | 10.255.128.17 | NOT RUN | - |
| 140 | dc1-leaf1b | Routing Table | Remote Lo0 address | 10.255.128.18 | NOT RUN | - |
| 141 | dc1-leaf1b | Routing Table | Remote VTEP address | 10.255.1.3 | NOT RUN | - |
| 142 | dc1-leaf1b | Routing Table | Remote VTEP address | 10.255.1.5 | NOT RUN | - |
| 143 | dc1-leaf1b | Routing Table | Remote VTEP address | 10.255.129.13 | NOT RUN | - |
| 144 | dc1-leaf1b | Routing Table | Remote VTEP address | 10.255.129.15 | NOT RUN | - |
| 145 | dc1-leaf1b | Routing Table | Remote VTEP address | 10.255.129.17 | NOT RUN | - |
| 146 | dc1-leaf1b | Security | Verifies if eAPI HTTPS server SSL profile is configured and valid. | VerifyAPIHttpsSSL | NOT RUN | - |
| 147 | dc1-leaf1c | Hardware | Verifies if the device temperature is within the acceptable range. | VerifyTemperature | NOT RUN | - |
| 148 | dc1-leaf1c | Hardware | Verifies if the fans status are within the accepted states list. | VerifyEnvironmentCooling | NOT RUN | - |
| 149 | dc1-leaf1c | Hardware | Verifies if the power supplies status are within the accepted states list. | VerifyEnvironmentPower | NOT RUN | - |
| 150 | dc1-leaf1c | Hardware | Verifies the transceiver's manufacturer against a list of approved manufacturers. | VerifyTransceiversManufacturers | NOT RUN | - |
| 151 | dc1-leaf1c | Interface State | Ethernet Interface & Line Protocol == 'up' | Ethernet1 - DC1-LEAF1A_Ethernet8 | NOT RUN | - |
| 152 | dc1-leaf1c | Interface State | Ethernet Interface & Line Protocol == 'up' | Ethernet2 - DC1-LEAF1B_Ethernet8 | NOT RUN | - |
| 153 | dc1-leaf1c | Interface State | Ethernet Interface & Line Protocol == 'up' | Ethernet5 - dc1-leaf1-server1_iLO | NOT RUN | - |
| 154 | dc1-leaf1c | Interface State | Port-Channel Interface & Line Protocol == 'up' | Port-Channel1 - DC1_L3_LEAF1_Po8 | NOT RUN | - |
| 155 | dc1-leaf1c | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet1 - remote: dc1-leaf1a_Ethernet8 | NOT RUN | - |
| 156 | dc1-leaf1c | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet2 - remote: dc1-leaf1b_Ethernet8 | NOT RUN | - |
| 157 | dc1-leaf1c | NTP | Synchronised with NTP server | NTP | NOT RUN | - |
| 158 | dc1-leaf1c | Security | Verifies if eAPI HTTPS server SSL profile is configured and valid. | VerifyAPIHttpsSSL | NOT RUN | - |
| 159 | dc1-leaf2a | BGP | ArBGP is configured and operating | ArBGP | NOT RUN | - |
| 160 | dc1-leaf2a | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.255.0.1 | NOT RUN | - |
| 161 | dc1-leaf2a | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.255.0.2 | NOT RUN | - |
| 162 | dc1-leaf2a | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.255.128.15 | NOT RUN | - |
| 163 | dc1-leaf2a | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.255.255.10 | NOT RUN | - |
| 164 | dc1-leaf2a | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.255.255.8 | NOT RUN | - |
| 165 | dc1-leaf2a | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 192.168.100.1 | NOT RUN | - |
| 166 | dc1-leaf2a | Hardware | Verifies if the device temperature is within the acceptable range. | VerifyTemperature | NOT RUN | - |
| 167 | dc1-leaf2a | Hardware | Verifies if the fans status are within the accepted states list. | VerifyEnvironmentCooling | NOT RUN | - |
| 168 | dc1-leaf2a | Hardware | Verifies if the power supplies status are within the accepted states list. | VerifyEnvironmentPower | NOT RUN | - |
| 169 | dc1-leaf2a | Hardware | Verifies the transceiver's manufacturer against a list of approved manufacturers. | VerifyTransceiversManufacturers | NOT RUN | - |
| 170 | dc1-leaf2a | Interface State | Ethernet Interface & Line Protocol == 'up' | Ethernet1 - P2P_LINK_TO_DC1-SPINE1_Ethernet3 | NOT RUN | - |
| 171 | dc1-leaf2a | Interface State | Ethernet Interface & Line Protocol == 'up' | Ethernet2 - P2P_LINK_TO_DC1-SPINE2_Ethernet3 | NOT RUN | - |
| 172 | dc1-leaf2a | Interface State | Ethernet Interface & Line Protocol == 'up' | Ethernet3 - MLAG_PEER_dc1-leaf2b_Ethernet3 | NOT RUN | - |
| 173 | dc1-leaf2a | Interface State | Ethernet Interface & Line Protocol == 'up' | Ethernet4 - MLAG_PEER_dc1-leaf2b_Ethernet4 | NOT RUN | - |
| 174 | dc1-leaf2a | Interface State | Ethernet Interface & Line Protocol == 'up' | Ethernet5 - dc1-leaf2-server1_PCI1 | NOT RUN | - |
| 175 | dc1-leaf2a | Interface State | Ethernet Interface & Line Protocol == 'up' | Ethernet6 - P2P_LINK_TO_dc2-leaf2a_Ethernet6 | NOT RUN | - |
| 176 | dc1-leaf2a | Interface State | Ethernet Interface & Line Protocol == 'up' | Ethernet8 - DC1-LEAF2C_Ethernet1 | NOT RUN | - |
| 177 | dc1-leaf2a | Interface State | Loopback Interface Status & Line Protocol == 'up' | Loopback0 - EVPN_Overlay_Peering | NOT RUN | - |
| 178 | dc1-leaf2a | Interface State | Loopback Interface Status & Line Protocol == 'up' | Loopback1 - VTEP_VXLAN_Tunnel_Source | NOT RUN | - |
| 179 | dc1-leaf2a | Interface State | Loopback Interface Status & Line Protocol == 'up' | Loopback10 - VRF10_VTEP_DIAGNOSTICS | NOT RUN | - |
| 180 | dc1-leaf2a | Interface State | Loopback Interface Status & Line Protocol == 'up' | Loopback11 - VRF11_VTEP_DIAGNOSTICS | NOT RUN | - |
| 181 | dc1-leaf2a | Interface State | Port-Channel Interface & Line Protocol == 'up' | Port-Channel3 - MLAG_PEER_dc1-leaf2b_Po3 | NOT RUN | - |
| 182 | dc1-leaf2a | Interface State | Port-Channel Interface & Line Protocol == 'up' | Port-Channel5 - dc1-leaf2-server1_PortChannel dc1-leaf2-server1 | NOT RUN | - |
| 183 | dc1-leaf2a | Interface State | Port-Channel Interface & Line Protocol == 'up' | Port-Channel8 - DC1-LEAF2C_Po1 | NOT RUN | - |
| 184 | dc1-leaf2a | Interface State | Vlan Interface & Line Protocol == 'up' | Vlan11 - VRF10_VLAN11 | NOT RUN | - |
| 185 | dc1-leaf2a | Interface State | Vlan Interface & Line Protocol == 'up' | Vlan12 - VRF10_VLAN12 | NOT RUN | - |
| 186 | dc1-leaf2a | Interface State | Vlan Interface & Line Protocol == 'up' | Vlan21 - VRF11_VLAN21 | NOT RUN | - |
| 187 | dc1-leaf2a | Interface State | Vlan Interface & Line Protocol == 'up' | Vlan22 - VRF11_VLAN22 | NOT RUN | - |
| 188 | dc1-leaf2a | Interface State | Vlan Interface & Line Protocol == 'up' | Vlan3009 - MLAG_PEER_L3_iBGP: vrf VRF10 | NOT RUN | - |
| 189 | dc1-leaf2a | Interface State | Vlan Interface & Line Protocol == 'up' | Vlan3010 - MLAG_PEER_L3_iBGP: vrf VRF11 | NOT RUN | - |
| 190 | dc1-leaf2a | Interface State | Vlan Interface & Line Protocol == 'up' | Vlan4093 - MLAG_PEER_L3_PEERING | NOT RUN | - |
| 191 | dc1-leaf2a | Interface State | Vlan Interface & Line Protocol == 'up' | Vlan4094 - MLAG_PEER | NOT RUN | - |
| 192 | dc1-leaf2a | Interface State | Vxlan Interface Status & Line Protocol == 'up' | Vxlan1 | NOT RUN | - |
| 193 | dc1-leaf2a | IP Reachability | ip reachability test p2p links | Source: dc1-leaf2a_Ethernet1 - Destination: dc1-spine1_Ethernet3 | NOT RUN | - |
| 194 | dc1-leaf2a | IP Reachability | ip reachability test p2p links | Source: dc1-leaf2a_Ethernet2 - Destination: dc1-spine2_Ethernet3 | NOT RUN | - |
| 195 | dc1-leaf2a | IP Reachability | ip reachability test p2p links | Source: dc1-leaf2a_Ethernet6 - Destination: dc2-leaf2a_Ethernet6 | NOT RUN | - |
| 196 | dc1-leaf2a | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet1 - remote: dc1-spine1_Ethernet3 | NOT RUN | - |
| 197 | dc1-leaf2a | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet2 - remote: dc1-spine2_Ethernet3 | NOT RUN | - |
| 198 | dc1-leaf2a | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet6 - remote: dc2-leaf2a_Ethernet6 | NOT RUN | - |
| 199 | dc1-leaf2a | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet8 - remote: dc1-leaf2c_Ethernet1 | NOT RUN | - |
| 200 | dc1-leaf2a | Loopback0 Reachability | Loopback0 Reachability | Source: dc1-leaf2a - 10.255.0.5/32 Destination: 10.255.0.1 | NOT RUN | - |
| 201 | dc1-leaf2a | Loopback0 Reachability | Loopback0 Reachability | Source: dc1-leaf2a - 10.255.0.5/32 Destination: 10.255.0.2 | NOT RUN | - |
| 202 | dc1-leaf2a | Loopback0 Reachability | Loopback0 Reachability | Source: dc1-leaf2a - 10.255.0.5/32 Destination: 10.255.0.3 | NOT RUN | - |
| 203 | dc1-leaf2a | Loopback0 Reachability | Loopback0 Reachability | Source: dc1-leaf2a - 10.255.0.5/32 Destination: 10.255.0.4 | NOT RUN | - |
| 204 | dc1-leaf2a | Loopback0 Reachability | Loopback0 Reachability | Source: dc1-leaf2a - 10.255.0.5/32 Destination: 10.255.0.5 | NOT RUN | - |
| 205 | dc1-leaf2a | Loopback0 Reachability | Loopback0 Reachability | Source: dc1-leaf2a - 10.255.0.5/32 Destination: 10.255.128.11 | NOT RUN | - |
| 206 | dc1-leaf2a | Loopback0 Reachability | Loopback0 Reachability | Source: dc1-leaf2a - 10.255.0.5/32 Destination: 10.255.128.12 | NOT RUN | - |
| 207 | dc1-leaf2a | Loopback0 Reachability | Loopback0 Reachability | Source: dc1-leaf2a - 10.255.0.5/32 Destination: 10.255.128.13 | NOT RUN | - |
| 208 | dc1-leaf2a | Loopback0 Reachability | Loopback0 Reachability | Source: dc1-leaf2a - 10.255.0.5/32 Destination: 10.255.128.14 | NOT RUN | - |
| 209 | dc1-leaf2a | Loopback0 Reachability | Loopback0 Reachability | Source: dc1-leaf2a - 10.255.0.5/32 Destination: 10.255.128.15 | NOT RUN | - |
| 210 | dc1-leaf2a | Loopback0 Reachability | Loopback0 Reachability | Source: dc1-leaf2a - 10.255.0.5/32 Destination: 10.255.128.16 | NOT RUN | - |
| 211 | dc1-leaf2a | Loopback0 Reachability | Loopback0 Reachability | Source: dc1-leaf2a - 10.255.0.5/32 Destination: 10.255.128.17 | NOT RUN | - |
| 212 | dc1-leaf2a | Loopback0 Reachability | Loopback0 Reachability | Source: dc1-leaf2a - 10.255.0.5/32 Destination: 10.255.128.18 | NOT RUN | - |
| 213 | dc1-leaf2a | MLAG | This test verifies the health status of the MLAG configuration. | VerifyMlagStatus | NOT RUN | - |
| 214 | dc1-leaf2a | NTP | Synchronised with NTP server | NTP | NOT RUN | - |
| 215 | dc1-leaf2a | Routing Table | Remote Lo0 address | 10.255.0.1 | NOT RUN | - |
| 216 | dc1-leaf2a | Routing Table | Remote Lo0 address | 10.255.0.2 | NOT RUN | - |
| 217 | dc1-leaf2a | Routing Table | Remote Lo0 address | 10.255.0.3 | NOT RUN | - |
| 218 | dc1-leaf2a | Routing Table | Remote Lo0 address | 10.255.0.4 | NOT RUN | - |
| 219 | dc1-leaf2a | Routing Table | Remote Lo0 address | 10.255.0.5 | NOT RUN | - |
| 220 | dc1-leaf2a | Routing Table | Remote Lo0 address | 10.255.128.11 | NOT RUN | - |
| 221 | dc1-leaf2a | Routing Table | Remote Lo0 address | 10.255.128.12 | NOT RUN | - |
| 222 | dc1-leaf2a | Routing Table | Remote Lo0 address | 10.255.128.13 | NOT RUN | - |
| 223 | dc1-leaf2a | Routing Table | Remote Lo0 address | 10.255.128.14 | NOT RUN | - |
| 224 | dc1-leaf2a | Routing Table | Remote Lo0 address | 10.255.128.15 | NOT RUN | - |
| 225 | dc1-leaf2a | Routing Table | Remote Lo0 address | 10.255.128.16 | NOT RUN | - |
| 226 | dc1-leaf2a | Routing Table | Remote Lo0 address | 10.255.128.17 | NOT RUN | - |
| 227 | dc1-leaf2a | Routing Table | Remote Lo0 address | 10.255.128.18 | NOT RUN | - |
| 228 | dc1-leaf2a | Routing Table | Remote VTEP address | 10.255.1.3 | NOT RUN | - |
| 229 | dc1-leaf2a | Routing Table | Remote VTEP address | 10.255.1.5 | NOT RUN | - |
| 230 | dc1-leaf2a | Routing Table | Remote VTEP address | 10.255.129.13 | NOT RUN | - |
| 231 | dc1-leaf2a | Routing Table | Remote VTEP address | 10.255.129.15 | NOT RUN | - |
| 232 | dc1-leaf2a | Routing Table | Remote VTEP address | 10.255.129.17 | NOT RUN | - |
| 233 | dc1-leaf2a | Security | Verifies if eAPI HTTPS server SSL profile is configured and valid. | VerifyAPIHttpsSSL | NOT RUN | - |
| 234 | dc1-leaf2c | Hardware | Verifies if the device temperature is within the acceptable range. | VerifyTemperature | NOT RUN | - |
| 235 | dc1-leaf2c | Hardware | Verifies if the fans status are within the accepted states list. | VerifyEnvironmentCooling | NOT RUN | - |
| 236 | dc1-leaf2c | Hardware | Verifies if the power supplies status are within the accepted states list. | VerifyEnvironmentPower | NOT RUN | - |
| 237 | dc1-leaf2c | Hardware | Verifies the transceiver's manufacturer against a list of approved manufacturers. | VerifyTransceiversManufacturers | NOT RUN | - |
| 238 | dc1-leaf2c | Interface State | Ethernet Interface & Line Protocol == 'adminDown' | Ethernet2 - DC1-LEAF2B_Ethernet8 | NOT RUN | - |
| 239 | dc1-leaf2c | Interface State | Ethernet Interface & Line Protocol == 'up' | Ethernet1 - DC1-LEAF2A_Ethernet8 | NOT RUN | - |
| 240 | dc1-leaf2c | Interface State | Ethernet Interface & Line Protocol == 'up' | Ethernet5 - dc1-leaf2-server1_iLO | NOT RUN | - |
| 241 | dc1-leaf2c | Interface State | Port-Channel Interface & Line Protocol == 'up' | Port-Channel1 - DC1_L3_LEAF2_Po8 | NOT RUN | - |
| 242 | dc1-leaf2c | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet1 - remote: dc1-leaf2a_Ethernet8 | NOT RUN | - |
| 243 | dc1-leaf2c | NTP | Synchronised with NTP server | NTP | NOT RUN | - |
| 244 | dc1-leaf2c | Security | Verifies if eAPI HTTPS server SSL profile is configured and valid. | VerifyAPIHttpsSSL | NOT RUN | - |
| 245 | dc1-spine1 | BGP | ArBGP is configured and operating | ArBGP | NOT RUN | - |
| 246 | dc1-spine1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.255.0.3 | NOT RUN | - |
| 247 | dc1-spine1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.255.0.4 | NOT RUN | - |
| 248 | dc1-spine1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.255.0.5 | NOT RUN | - |
| 249 | dc1-spine1 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.255.255.1 | NOT RUN | - |
| 250 | dc1-spine1 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.255.255.5 | NOT RUN | - |
| 251 | dc1-spine1 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.255.255.9 | NOT RUN | - |
| 252 | dc1-spine1 | Hardware | Verifies if the device temperature is within the acceptable range. | VerifyTemperature | NOT RUN | - |
| 253 | dc1-spine1 | Hardware | Verifies if the fans status are within the accepted states list. | VerifyEnvironmentCooling | NOT RUN | - |
| 254 | dc1-spine1 | Hardware | Verifies if the power supplies status are within the accepted states list. | VerifyEnvironmentPower | NOT RUN | - |
| 255 | dc1-spine1 | Hardware | Verifies the transceiver's manufacturer against a list of approved manufacturers. | VerifyTransceiversManufacturers | NOT RUN | - |
| 256 | dc1-spine1 | Interface State | Ethernet Interface & Line Protocol == 'adminDown' | Ethernet4 - P2P_LINK_TO_DC1-LEAF2B_Ethernet1 | NOT RUN | - |
| 257 | dc1-spine1 | Interface State | Ethernet Interface & Line Protocol == 'up' | Ethernet1 - P2P_LINK_TO_DC1-LEAF1A_Ethernet1 | NOT RUN | - |
| 258 | dc1-spine1 | Interface State | Ethernet Interface & Line Protocol == 'up' | Ethernet2 - P2P_LINK_TO_DC1-LEAF1B_Ethernet1 | NOT RUN | - |
| 259 | dc1-spine1 | Interface State | Ethernet Interface & Line Protocol == 'up' | Ethernet3 - P2P_LINK_TO_DC1-LEAF2A_Ethernet1 | NOT RUN | - |
| 260 | dc1-spine1 | Interface State | Loopback Interface Status & Line Protocol == 'up' | Loopback0 - EVPN_Overlay_Peering | NOT RUN | - |
| 261 | dc1-spine1 | IP Reachability | ip reachability test p2p links | Source: dc1-spine1_Ethernet1 - Destination: dc1-leaf1a_Ethernet1 | NOT RUN | - |
| 262 | dc1-spine1 | IP Reachability | ip reachability test p2p links | Source: dc1-spine1_Ethernet2 - Destination: dc1-leaf1b_Ethernet1 | NOT RUN | - |
| 263 | dc1-spine1 | IP Reachability | ip reachability test p2p links | Source: dc1-spine1_Ethernet3 - Destination: dc1-leaf2a_Ethernet1 | NOT RUN | - |
| 264 | dc1-spine1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet1 - remote: dc1-leaf1a_Ethernet1 | NOT RUN | - |
| 265 | dc1-spine1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet2 - remote: dc1-leaf1b_Ethernet1 | NOT RUN | - |
| 266 | dc1-spine1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet3 - remote: dc1-leaf2a_Ethernet1 | NOT RUN | - |
| 267 | dc1-spine1 | NTP | Synchronised with NTP server | NTP | NOT RUN | - |
| 268 | dc1-spine1 | Security | Verifies if eAPI HTTPS server SSL profile is configured and valid. | VerifyAPIHttpsSSL | NOT RUN | - |
| 269 | dc1-spine2 | BGP | ArBGP is configured and operating | ArBGP | NOT RUN | - |
| 270 | dc1-spine2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.255.0.3 | NOT RUN | - |
| 271 | dc1-spine2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.255.0.4 | NOT RUN | - |
| 272 | dc1-spine2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.255.0.5 | NOT RUN | - |
| 273 | dc1-spine2 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.255.255.11 | NOT RUN | - |
| 274 | dc1-spine2 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.255.255.3 | NOT RUN | - |
| 275 | dc1-spine2 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.255.255.7 | NOT RUN | - |
| 276 | dc1-spine2 | Hardware | Verifies if the device temperature is within the acceptable range. | VerifyTemperature | NOT RUN | - |
| 277 | dc1-spine2 | Hardware | Verifies if the fans status are within the accepted states list. | VerifyEnvironmentCooling | NOT RUN | - |
| 278 | dc1-spine2 | Hardware | Verifies if the power supplies status are within the accepted states list. | VerifyEnvironmentPower | NOT RUN | - |
| 279 | dc1-spine2 | Hardware | Verifies the transceiver's manufacturer against a list of approved manufacturers. | VerifyTransceiversManufacturers | NOT RUN | - |
| 280 | dc1-spine2 | Interface State | Ethernet Interface & Line Protocol == 'adminDown' | Ethernet4 - P2P_LINK_TO_DC1-LEAF2B_Ethernet2 | NOT RUN | - |
| 281 | dc1-spine2 | Interface State | Ethernet Interface & Line Protocol == 'up' | Ethernet1 - P2P_LINK_TO_DC1-LEAF1A_Ethernet2 | NOT RUN | - |
| 282 | dc1-spine2 | Interface State | Ethernet Interface & Line Protocol == 'up' | Ethernet2 - P2P_LINK_TO_DC1-LEAF1B_Ethernet2 | NOT RUN | - |
| 283 | dc1-spine2 | Interface State | Ethernet Interface & Line Protocol == 'up' | Ethernet3 - P2P_LINK_TO_DC1-LEAF2A_Ethernet2 | NOT RUN | - |
| 284 | dc1-spine2 | Interface State | Loopback Interface Status & Line Protocol == 'up' | Loopback0 - EVPN_Overlay_Peering | NOT RUN | - |
| 285 | dc1-spine2 | IP Reachability | ip reachability test p2p links | Source: dc1-spine2_Ethernet1 - Destination: dc1-leaf1a_Ethernet2 | NOT RUN | - |
| 286 | dc1-spine2 | IP Reachability | ip reachability test p2p links | Source: dc1-spine2_Ethernet2 - Destination: dc1-leaf1b_Ethernet2 | NOT RUN | - |
| 287 | dc1-spine2 | IP Reachability | ip reachability test p2p links | Source: dc1-spine2_Ethernet3 - Destination: dc1-leaf2a_Ethernet2 | NOT RUN | - |
| 288 | dc1-spine2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet1 - remote: dc1-leaf1a_Ethernet2 | NOT RUN | - |
| 289 | dc1-spine2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet2 - remote: dc1-leaf1b_Ethernet2 | NOT RUN | - |
| 290 | dc1-spine2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet3 - remote: dc1-leaf2a_Ethernet2 | NOT RUN | - |
| 291 | dc1-spine2 | NTP | Synchronised with NTP server | NTP | NOT RUN | - |
| 292 | dc1-spine2 | Security | Verifies if eAPI HTTPS server SSL profile is configured and valid. | VerifyAPIHttpsSSL | NOT RUN | - |
| 293 | dc2-leaf1a | BGP | ArBGP is configured and operating | ArBGP | NOT RUN | - |
| 294 | dc2-leaf1a | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.255.128.11 | NOT RUN | - |
| 295 | dc2-leaf1a | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.255.128.12 | NOT RUN | - |
| 296 | dc2-leaf1a | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.255.129.117 | NOT RUN | - |
| 297 | dc2-leaf1a | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.255.255.104 | NOT RUN | - |
| 298 | dc2-leaf1a | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.255.255.106 | NOT RUN | - |
| 299 | dc2-leaf1a | Hardware | Verifies if the device temperature is within the acceptable range. | VerifyTemperature | NOT RUN | - |
| 300 | dc2-leaf1a | Hardware | Verifies if the fans status are within the accepted states list. | VerifyEnvironmentCooling | NOT RUN | - |
| 301 | dc2-leaf1a | Hardware | Verifies if the power supplies status are within the accepted states list. | VerifyEnvironmentPower | NOT RUN | - |
| 302 | dc2-leaf1a | Hardware | Verifies the transceiver's manufacturer against a list of approved manufacturers. | VerifyTransceiversManufacturers | NOT RUN | - |
| 303 | dc2-leaf1a | Interface State | Ethernet Interface & Line Protocol == 'up' | Ethernet1 - P2P_LINK_TO_DC2-SPINE1_Ethernet1 | NOT RUN | - |
| 304 | dc2-leaf1a | Interface State | Ethernet Interface & Line Protocol == 'up' | Ethernet2 - P2P_LINK_TO_DC2-SPINE2_Ethernet1 | NOT RUN | - |
| 305 | dc2-leaf1a | Interface State | Ethernet Interface & Line Protocol == 'up' | Ethernet3 - MLAG_PEER_dc2-leaf1b_Ethernet3 | NOT RUN | - |
| 306 | dc2-leaf1a | Interface State | Ethernet Interface & Line Protocol == 'up' | Ethernet4 - MLAG_PEER_dc2-leaf1b_Ethernet4 | NOT RUN | - |
| 307 | dc2-leaf1a | Interface State | Ethernet Interface & Line Protocol == 'up' | Ethernet5 - dc2-leaf1-server1_PCI1 | NOT RUN | - |
| 308 | dc2-leaf1a | Interface State | Ethernet Interface & Line Protocol == 'up' | Ethernet8 - DC2-LEAF1C_Ethernet1 | NOT RUN | - |
| 309 | dc2-leaf1a | Interface State | Loopback Interface Status & Line Protocol == 'up' | Loopback0 - EVPN_Overlay_Peering | NOT RUN | - |
| 310 | dc2-leaf1a | Interface State | Loopback Interface Status & Line Protocol == 'up' | Loopback1 - VTEP_VXLAN_Tunnel_Source | NOT RUN | - |
| 311 | dc2-leaf1a | Interface State | Loopback Interface Status & Line Protocol == 'up' | Loopback10 - VRF10_VTEP_DIAGNOSTICS | NOT RUN | - |
| 312 | dc2-leaf1a | Interface State | Loopback Interface Status & Line Protocol == 'up' | Loopback11 - VRF11_VTEP_DIAGNOSTICS | NOT RUN | - |
| 313 | dc2-leaf1a | Interface State | Port-Channel Interface & Line Protocol == 'up' | Port-Channel3 - MLAG_PEER_dc2-leaf1b_Po3 | NOT RUN | - |
| 314 | dc2-leaf1a | Interface State | Port-Channel Interface & Line Protocol == 'up' | Port-Channel5 - dc2-leaf1-server1_PortChannel dc2-leaf1-server1 | NOT RUN | - |
| 315 | dc2-leaf1a | Interface State | Port-Channel Interface & Line Protocol == 'up' | Port-Channel8 - DC2-LEAF1C_Po1 | NOT RUN | - |
| 316 | dc2-leaf1a | Interface State | Vlan Interface & Line Protocol == 'up' | Vlan11 - VRF10_VLAN11 | NOT RUN | - |
| 317 | dc2-leaf1a | Interface State | Vlan Interface & Line Protocol == 'up' | Vlan12 - VRF10_VLAN12 | NOT RUN | - |
| 318 | dc2-leaf1a | Interface State | Vlan Interface & Line Protocol == 'up' | Vlan21 - VRF11_VLAN21 | NOT RUN | - |
| 319 | dc2-leaf1a | Interface State | Vlan Interface & Line Protocol == 'up' | Vlan22 - VRF11_VLAN22 | NOT RUN | - |
| 320 | dc2-leaf1a | Interface State | Vlan Interface & Line Protocol == 'up' | Vlan3009 - MLAG_PEER_L3_iBGP: vrf VRF10 | NOT RUN | - |
| 321 | dc2-leaf1a | Interface State | Vlan Interface & Line Protocol == 'up' | Vlan3010 - MLAG_PEER_L3_iBGP: vrf VRF11 | NOT RUN | - |
| 322 | dc2-leaf1a | Interface State | Vlan Interface & Line Protocol == 'up' | Vlan4093 - MLAG_PEER_L3_PEERING | NOT RUN | - |
| 323 | dc2-leaf1a | Interface State | Vlan Interface & Line Protocol == 'up' | Vlan4094 - MLAG_PEER | NOT RUN | - |
| 324 | dc2-leaf1a | Interface State | Vxlan Interface Status & Line Protocol == 'up' | Vxlan1 | NOT RUN | - |
| 325 | dc2-leaf1a | IP Reachability | ip reachability test p2p links | Source: dc2-leaf1a_Ethernet1 - Destination: dc2-spine1_Ethernet1 | NOT RUN | - |
| 326 | dc2-leaf1a | IP Reachability | ip reachability test p2p links | Source: dc2-leaf1a_Ethernet2 - Destination: dc2-spine2_Ethernet1 | NOT RUN | - |
| 327 | dc2-leaf1a | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet1 - remote: dc2-spine1_Ethernet1 | NOT RUN | - |
| 328 | dc2-leaf1a | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet2 - remote: dc2-spine2_Ethernet1 | NOT RUN | - |
| 329 | dc2-leaf1a | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet3 - remote: dc2-leaf1b_Ethernet3 | NOT RUN | - |
| 330 | dc2-leaf1a | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet4 - remote: dc2-leaf1b_Ethernet4 | NOT RUN | - |
| 331 | dc2-leaf1a | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet8 - remote: dc2-leaf1c_Ethernet1 | NOT RUN | - |
| 332 | dc2-leaf1a | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf1a - 10.255.128.13/32 Destination: 10.255.0.1 | NOT RUN | - |
| 333 | dc2-leaf1a | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf1a - 10.255.128.13/32 Destination: 10.255.0.2 | NOT RUN | - |
| 334 | dc2-leaf1a | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf1a - 10.255.128.13/32 Destination: 10.255.0.3 | NOT RUN | - |
| 335 | dc2-leaf1a | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf1a - 10.255.128.13/32 Destination: 10.255.0.4 | NOT RUN | - |
| 336 | dc2-leaf1a | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf1a - 10.255.128.13/32 Destination: 10.255.0.5 | NOT RUN | - |
| 337 | dc2-leaf1a | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf1a - 10.255.128.13/32 Destination: 10.255.128.11 | NOT RUN | - |
| 338 | dc2-leaf1a | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf1a - 10.255.128.13/32 Destination: 10.255.128.12 | NOT RUN | - |
| 339 | dc2-leaf1a | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf1a - 10.255.128.13/32 Destination: 10.255.128.13 | NOT RUN | - |
| 340 | dc2-leaf1a | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf1a - 10.255.128.13/32 Destination: 10.255.128.14 | NOT RUN | - |
| 341 | dc2-leaf1a | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf1a - 10.255.128.13/32 Destination: 10.255.128.15 | NOT RUN | - |
| 342 | dc2-leaf1a | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf1a - 10.255.128.13/32 Destination: 10.255.128.16 | NOT RUN | - |
| 343 | dc2-leaf1a | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf1a - 10.255.128.13/32 Destination: 10.255.128.17 | NOT RUN | - |
| 344 | dc2-leaf1a | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf1a - 10.255.128.13/32 Destination: 10.255.128.18 | NOT RUN | - |
| 345 | dc2-leaf1a | MLAG | This test verifies the health status of the MLAG configuration. | VerifyMlagStatus | NOT RUN | - |
| 346 | dc2-leaf1a | NTP | Synchronised with NTP server | NTP | NOT RUN | - |
| 347 | dc2-leaf1a | Routing Table | Remote Lo0 address | 10.255.0.1 | NOT RUN | - |
| 348 | dc2-leaf1a | Routing Table | Remote Lo0 address | 10.255.0.2 | NOT RUN | - |
| 349 | dc2-leaf1a | Routing Table | Remote Lo0 address | 10.255.0.3 | NOT RUN | - |
| 350 | dc2-leaf1a | Routing Table | Remote Lo0 address | 10.255.0.4 | NOT RUN | - |
| 351 | dc2-leaf1a | Routing Table | Remote Lo0 address | 10.255.0.5 | NOT RUN | - |
| 352 | dc2-leaf1a | Routing Table | Remote Lo0 address | 10.255.128.11 | NOT RUN | - |
| 353 | dc2-leaf1a | Routing Table | Remote Lo0 address | 10.255.128.12 | NOT RUN | - |
| 354 | dc2-leaf1a | Routing Table | Remote Lo0 address | 10.255.128.13 | NOT RUN | - |
| 355 | dc2-leaf1a | Routing Table | Remote Lo0 address | 10.255.128.14 | NOT RUN | - |
| 356 | dc2-leaf1a | Routing Table | Remote Lo0 address | 10.255.128.15 | NOT RUN | - |
| 357 | dc2-leaf1a | Routing Table | Remote Lo0 address | 10.255.128.16 | NOT RUN | - |
| 358 | dc2-leaf1a | Routing Table | Remote Lo0 address | 10.255.128.17 | NOT RUN | - |
| 359 | dc2-leaf1a | Routing Table | Remote Lo0 address | 10.255.128.18 | NOT RUN | - |
| 360 | dc2-leaf1a | Routing Table | Remote VTEP address | 10.255.1.3 | NOT RUN | - |
| 361 | dc2-leaf1a | Routing Table | Remote VTEP address | 10.255.1.5 | NOT RUN | - |
| 362 | dc2-leaf1a | Routing Table | Remote VTEP address | 10.255.129.13 | NOT RUN | - |
| 363 | dc2-leaf1a | Routing Table | Remote VTEP address | 10.255.129.15 | NOT RUN | - |
| 364 | dc2-leaf1a | Routing Table | Remote VTEP address | 10.255.129.17 | NOT RUN | - |
| 365 | dc2-leaf1a | Security | Verifies if eAPI HTTPS server SSL profile is configured and valid. | VerifyAPIHttpsSSL | NOT RUN | - |
| 366 | dc2-leaf1b | BGP | ArBGP is configured and operating | ArBGP | NOT RUN | - |
| 367 | dc2-leaf1b | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.255.128.11 | NOT RUN | - |
| 368 | dc2-leaf1b | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.255.128.12 | NOT RUN | - |
| 369 | dc2-leaf1b | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.255.129.116 | NOT RUN | - |
| 370 | dc2-leaf1b | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.255.255.108 | NOT RUN | - |
| 371 | dc2-leaf1b | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.255.255.110 | NOT RUN | - |
| 372 | dc2-leaf1b | Hardware | Verifies if the device temperature is within the acceptable range. | VerifyTemperature | NOT RUN | - |
| 373 | dc2-leaf1b | Hardware | Verifies if the fans status are within the accepted states list. | VerifyEnvironmentCooling | NOT RUN | - |
| 374 | dc2-leaf1b | Hardware | Verifies if the power supplies status are within the accepted states list. | VerifyEnvironmentPower | NOT RUN | - |
| 375 | dc2-leaf1b | Hardware | Verifies the transceiver's manufacturer against a list of approved manufacturers. | VerifyTransceiversManufacturers | NOT RUN | - |
| 376 | dc2-leaf1b | Interface State | Ethernet Interface & Line Protocol == 'up' | Ethernet1 - P2P_LINK_TO_DC2-SPINE1_Ethernet2 | NOT RUN | - |
| 377 | dc2-leaf1b | Interface State | Ethernet Interface & Line Protocol == 'up' | Ethernet2 - P2P_LINK_TO_DC2-SPINE2_Ethernet2 | NOT RUN | - |
| 378 | dc2-leaf1b | Interface State | Ethernet Interface & Line Protocol == 'up' | Ethernet3 - MLAG_PEER_dc2-leaf1a_Ethernet3 | NOT RUN | - |
| 379 | dc2-leaf1b | Interface State | Ethernet Interface & Line Protocol == 'up' | Ethernet4 - MLAG_PEER_dc2-leaf1a_Ethernet4 | NOT RUN | - |
| 380 | dc2-leaf1b | Interface State | Ethernet Interface & Line Protocol == 'up' | Ethernet5 - dc2-leaf1-server1_PCI2 | NOT RUN | - |
| 381 | dc2-leaf1b | Interface State | Ethernet Interface & Line Protocol == 'up' | Ethernet8 - DC2-LEAF1C_Ethernet2 | NOT RUN | - |
| 382 | dc2-leaf1b | Interface State | Loopback Interface Status & Line Protocol == 'up' | Loopback0 - EVPN_Overlay_Peering | NOT RUN | - |
| 383 | dc2-leaf1b | Interface State | Loopback Interface Status & Line Protocol == 'up' | Loopback1 - VTEP_VXLAN_Tunnel_Source | NOT RUN | - |
| 384 | dc2-leaf1b | Interface State | Loopback Interface Status & Line Protocol == 'up' | Loopback10 - VRF10_VTEP_DIAGNOSTICS | NOT RUN | - |
| 385 | dc2-leaf1b | Interface State | Loopback Interface Status & Line Protocol == 'up' | Loopback11 - VRF11_VTEP_DIAGNOSTICS | NOT RUN | - |
| 386 | dc2-leaf1b | Interface State | Port-Channel Interface & Line Protocol == 'up' | Port-Channel3 - MLAG_PEER_dc2-leaf1a_Po3 | NOT RUN | - |
| 387 | dc2-leaf1b | Interface State | Port-Channel Interface & Line Protocol == 'up' | Port-Channel5 - dc2-leaf1-server1_PortChannel dc2-leaf1-server1 | NOT RUN | - |
| 388 | dc2-leaf1b | Interface State | Port-Channel Interface & Line Protocol == 'up' | Port-Channel8 - DC2-LEAF1C_Po1 | NOT RUN | - |
| 389 | dc2-leaf1b | Interface State | Vlan Interface & Line Protocol == 'up' | Vlan11 - VRF10_VLAN11 | NOT RUN | - |
| 390 | dc2-leaf1b | Interface State | Vlan Interface & Line Protocol == 'up' | Vlan12 - VRF10_VLAN12 | NOT RUN | - |
| 391 | dc2-leaf1b | Interface State | Vlan Interface & Line Protocol == 'up' | Vlan21 - VRF11_VLAN21 | NOT RUN | - |
| 392 | dc2-leaf1b | Interface State | Vlan Interface & Line Protocol == 'up' | Vlan22 - VRF11_VLAN22 | NOT RUN | - |
| 393 | dc2-leaf1b | Interface State | Vlan Interface & Line Protocol == 'up' | Vlan3009 - MLAG_PEER_L3_iBGP: vrf VRF10 | NOT RUN | - |
| 394 | dc2-leaf1b | Interface State | Vlan Interface & Line Protocol == 'up' | Vlan3010 - MLAG_PEER_L3_iBGP: vrf VRF11 | NOT RUN | - |
| 395 | dc2-leaf1b | Interface State | Vlan Interface & Line Protocol == 'up' | Vlan4093 - MLAG_PEER_L3_PEERING | NOT RUN | - |
| 396 | dc2-leaf1b | Interface State | Vlan Interface & Line Protocol == 'up' | Vlan4094 - MLAG_PEER | NOT RUN | - |
| 397 | dc2-leaf1b | Interface State | Vxlan Interface Status & Line Protocol == 'up' | Vxlan1 | NOT RUN | - |
| 398 | dc2-leaf1b | IP Reachability | ip reachability test p2p links | Source: dc2-leaf1b_Ethernet1 - Destination: dc2-spine1_Ethernet2 | NOT RUN | - |
| 399 | dc2-leaf1b | IP Reachability | ip reachability test p2p links | Source: dc2-leaf1b_Ethernet2 - Destination: dc2-spine2_Ethernet2 | NOT RUN | - |
| 400 | dc2-leaf1b | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet1 - remote: dc2-spine1_Ethernet2 | NOT RUN | - |
| 401 | dc2-leaf1b | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet2 - remote: dc2-spine2_Ethernet2 | NOT RUN | - |
| 402 | dc2-leaf1b | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet3 - remote: dc2-leaf1a_Ethernet3 | NOT RUN | - |
| 403 | dc2-leaf1b | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet4 - remote: dc2-leaf1a_Ethernet4 | NOT RUN | - |
| 404 | dc2-leaf1b | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet8 - remote: dc2-leaf1c_Ethernet2 | NOT RUN | - |
| 405 | dc2-leaf1b | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf1b - 10.255.128.14/32 Destination: 10.255.0.1 | NOT RUN | - |
| 406 | dc2-leaf1b | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf1b - 10.255.128.14/32 Destination: 10.255.0.2 | NOT RUN | - |
| 407 | dc2-leaf1b | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf1b - 10.255.128.14/32 Destination: 10.255.0.3 | NOT RUN | - |
| 408 | dc2-leaf1b | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf1b - 10.255.128.14/32 Destination: 10.255.0.4 | NOT RUN | - |
| 409 | dc2-leaf1b | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf1b - 10.255.128.14/32 Destination: 10.255.0.5 | NOT RUN | - |
| 410 | dc2-leaf1b | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf1b - 10.255.128.14/32 Destination: 10.255.128.11 | NOT RUN | - |
| 411 | dc2-leaf1b | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf1b - 10.255.128.14/32 Destination: 10.255.128.12 | NOT RUN | - |
| 412 | dc2-leaf1b | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf1b - 10.255.128.14/32 Destination: 10.255.128.13 | NOT RUN | - |
| 413 | dc2-leaf1b | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf1b - 10.255.128.14/32 Destination: 10.255.128.14 | NOT RUN | - |
| 414 | dc2-leaf1b | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf1b - 10.255.128.14/32 Destination: 10.255.128.15 | NOT RUN | - |
| 415 | dc2-leaf1b | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf1b - 10.255.128.14/32 Destination: 10.255.128.16 | NOT RUN | - |
| 416 | dc2-leaf1b | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf1b - 10.255.128.14/32 Destination: 10.255.128.17 | NOT RUN | - |
| 417 | dc2-leaf1b | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf1b - 10.255.128.14/32 Destination: 10.255.128.18 | NOT RUN | - |
| 418 | dc2-leaf1b | MLAG | This test verifies the health status of the MLAG configuration. | VerifyMlagStatus | NOT RUN | - |
| 419 | dc2-leaf1b | NTP | Synchronised with NTP server | NTP | NOT RUN | - |
| 420 | dc2-leaf1b | Routing Table | Remote Lo0 address | 10.255.0.1 | NOT RUN | - |
| 421 | dc2-leaf1b | Routing Table | Remote Lo0 address | 10.255.0.2 | NOT RUN | - |
| 422 | dc2-leaf1b | Routing Table | Remote Lo0 address | 10.255.0.3 | NOT RUN | - |
| 423 | dc2-leaf1b | Routing Table | Remote Lo0 address | 10.255.0.4 | NOT RUN | - |
| 424 | dc2-leaf1b | Routing Table | Remote Lo0 address | 10.255.0.5 | NOT RUN | - |
| 425 | dc2-leaf1b | Routing Table | Remote Lo0 address | 10.255.128.11 | NOT RUN | - |
| 426 | dc2-leaf1b | Routing Table | Remote Lo0 address | 10.255.128.12 | NOT RUN | - |
| 427 | dc2-leaf1b | Routing Table | Remote Lo0 address | 10.255.128.13 | NOT RUN | - |
| 428 | dc2-leaf1b | Routing Table | Remote Lo0 address | 10.255.128.14 | NOT RUN | - |
| 429 | dc2-leaf1b | Routing Table | Remote Lo0 address | 10.255.128.15 | NOT RUN | - |
| 430 | dc2-leaf1b | Routing Table | Remote Lo0 address | 10.255.128.16 | NOT RUN | - |
| 431 | dc2-leaf1b | Routing Table | Remote Lo0 address | 10.255.128.17 | NOT RUN | - |
| 432 | dc2-leaf1b | Routing Table | Remote Lo0 address | 10.255.128.18 | NOT RUN | - |
| 433 | dc2-leaf1b | Routing Table | Remote VTEP address | 10.255.1.3 | NOT RUN | - |
| 434 | dc2-leaf1b | Routing Table | Remote VTEP address | 10.255.1.5 | NOT RUN | - |
| 435 | dc2-leaf1b | Routing Table | Remote VTEP address | 10.255.129.13 | NOT RUN | - |
| 436 | dc2-leaf1b | Routing Table | Remote VTEP address | 10.255.129.15 | NOT RUN | - |
| 437 | dc2-leaf1b | Routing Table | Remote VTEP address | 10.255.129.17 | NOT RUN | - |
| 438 | dc2-leaf1b | Security | Verifies if eAPI HTTPS server SSL profile is configured and valid. | VerifyAPIHttpsSSL | NOT RUN | - |
| 439 | dc2-leaf1c | Hardware | Verifies if the device temperature is within the acceptable range. | VerifyTemperature | NOT RUN | - |
| 440 | dc2-leaf1c | Hardware | Verifies if the fans status are within the accepted states list. | VerifyEnvironmentCooling | NOT RUN | - |
| 441 | dc2-leaf1c | Hardware | Verifies if the power supplies status are within the accepted states list. | VerifyEnvironmentPower | NOT RUN | - |
| 442 | dc2-leaf1c | Hardware | Verifies the transceiver's manufacturer against a list of approved manufacturers. | VerifyTransceiversManufacturers | NOT RUN | - |
| 443 | dc2-leaf1c | Interface State | Ethernet Interface & Line Protocol == 'up' | Ethernet1 - DC2-LEAF1A_Ethernet8 | NOT RUN | - |
| 444 | dc2-leaf1c | Interface State | Ethernet Interface & Line Protocol == 'up' | Ethernet2 - DC2-LEAF1B_Ethernet8 | NOT RUN | - |
| 445 | dc2-leaf1c | Interface State | Ethernet Interface & Line Protocol == 'up' | Ethernet5 - dc2-leaf1-server1_iLO | NOT RUN | - |
| 446 | dc2-leaf1c | Interface State | Port-Channel Interface & Line Protocol == 'up' | Port-Channel1 - DC2_L3_LEAF1_Po8 | NOT RUN | - |
| 447 | dc2-leaf1c | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet1 - remote: dc2-leaf1a_Ethernet8 | NOT RUN | - |
| 448 | dc2-leaf1c | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet2 - remote: dc2-leaf1b_Ethernet8 | NOT RUN | - |
| 449 | dc2-leaf1c | NTP | Synchronised with NTP server | NTP | NOT RUN | - |
| 450 | dc2-leaf1c | Security | Verifies if eAPI HTTPS server SSL profile is configured and valid. | VerifyAPIHttpsSSL | NOT RUN | - |
| 451 | dc2-leaf2a | BGP | ArBGP is configured and operating | ArBGP | NOT RUN | - |
| 452 | dc2-leaf2a | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.255.0.5 | NOT RUN | - |
| 453 | dc2-leaf2a | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.255.128.11 | NOT RUN | - |
| 454 | dc2-leaf2a | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.255.128.12 | NOT RUN | - |
| 455 | dc2-leaf2a | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.255.129.121 | NOT RUN | - |
| 456 | dc2-leaf2a | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.255.255.112 | NOT RUN | - |
| 457 | dc2-leaf2a | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.255.255.114 | NOT RUN | - |
| 458 | dc2-leaf2a | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 192.168.100.0 | NOT RUN | - |
| 459 | dc2-leaf2a | Hardware | Verifies if the device temperature is within the acceptable range. | VerifyTemperature | NOT RUN | - |
| 460 | dc2-leaf2a | Hardware | Verifies if the fans status are within the accepted states list. | VerifyEnvironmentCooling | NOT RUN | - |
| 461 | dc2-leaf2a | Hardware | Verifies if the power supplies status are within the accepted states list. | VerifyEnvironmentPower | NOT RUN | - |
| 462 | dc2-leaf2a | Hardware | Verifies the transceiver's manufacturer against a list of approved manufacturers. | VerifyTransceiversManufacturers | NOT RUN | - |
| 463 | dc2-leaf2a | Interface State | Ethernet Interface & Line Protocol == 'up' | Ethernet1 - P2P_LINK_TO_DC2-SPINE1_Ethernet3 | NOT RUN | - |
| 464 | dc2-leaf2a | Interface State | Ethernet Interface & Line Protocol == 'up' | Ethernet2 - P2P_LINK_TO_DC2-SPINE2_Ethernet3 | NOT RUN | - |
| 465 | dc2-leaf2a | Interface State | Ethernet Interface & Line Protocol == 'up' | Ethernet3 - MLAG_PEER_dc2-leaf2b_Ethernet3 | NOT RUN | - |
| 466 | dc2-leaf2a | Interface State | Ethernet Interface & Line Protocol == 'up' | Ethernet4 - MLAG_PEER_dc2-leaf2b_Ethernet4 | NOT RUN | - |
| 467 | dc2-leaf2a | Interface State | Ethernet Interface & Line Protocol == 'up' | Ethernet5 - dc2-leaf2-server1_PCI1 | NOT RUN | - |
| 468 | dc2-leaf2a | Interface State | Ethernet Interface & Line Protocol == 'up' | Ethernet6 - P2P_LINK_TO_dc1-leaf2a_Ethernet6 | NOT RUN | - |
| 469 | dc2-leaf2a | Interface State | Ethernet Interface & Line Protocol == 'up' | Ethernet8 - DC2-LEAF2C_Ethernet1 | NOT RUN | - |
| 470 | dc2-leaf2a | Interface State | Loopback Interface Status & Line Protocol == 'up' | Loopback0 - EVPN_Overlay_Peering | NOT RUN | - |
| 471 | dc2-leaf2a | Interface State | Loopback Interface Status & Line Protocol == 'up' | Loopback1 - VTEP_VXLAN_Tunnel_Source | NOT RUN | - |
| 472 | dc2-leaf2a | Interface State | Loopback Interface Status & Line Protocol == 'up' | Loopback10 - VRF10_VTEP_DIAGNOSTICS | NOT RUN | - |
| 473 | dc2-leaf2a | Interface State | Loopback Interface Status & Line Protocol == 'up' | Loopback11 - VRF11_VTEP_DIAGNOSTICS | NOT RUN | - |
| 474 | dc2-leaf2a | Interface State | Port-Channel Interface & Line Protocol == 'up' | Port-Channel3 - MLAG_PEER_dc2-leaf2b_Po3 | NOT RUN | - |
| 475 | dc2-leaf2a | Interface State | Port-Channel Interface & Line Protocol == 'up' | Port-Channel5 - dc2-leaf2-server1_PortChannel dc2-leaf2-server1 | NOT RUN | - |
| 476 | dc2-leaf2a | Interface State | Port-Channel Interface & Line Protocol == 'up' | Port-Channel8 - DC2-LEAF2C_Po1 | NOT RUN | - |
| 477 | dc2-leaf2a | Interface State | Vlan Interface & Line Protocol == 'up' | Vlan11 - VRF10_VLAN11 | NOT RUN | - |
| 478 | dc2-leaf2a | Interface State | Vlan Interface & Line Protocol == 'up' | Vlan12 - VRF10_VLAN12 | NOT RUN | - |
| 479 | dc2-leaf2a | Interface State | Vlan Interface & Line Protocol == 'up' | Vlan21 - VRF11_VLAN21 | NOT RUN | - |
| 480 | dc2-leaf2a | Interface State | Vlan Interface & Line Protocol == 'up' | Vlan22 - VRF11_VLAN22 | NOT RUN | - |
| 481 | dc2-leaf2a | Interface State | Vlan Interface & Line Protocol == 'up' | Vlan3009 - MLAG_PEER_L3_iBGP: vrf VRF10 | NOT RUN | - |
| 482 | dc2-leaf2a | Interface State | Vlan Interface & Line Protocol == 'up' | Vlan3010 - MLAG_PEER_L3_iBGP: vrf VRF11 | NOT RUN | - |
| 483 | dc2-leaf2a | Interface State | Vlan Interface & Line Protocol == 'up' | Vlan4093 - MLAG_PEER_L3_PEERING | NOT RUN | - |
| 484 | dc2-leaf2a | Interface State | Vlan Interface & Line Protocol == 'up' | Vlan4094 - MLAG_PEER | NOT RUN | - |
| 485 | dc2-leaf2a | Interface State | Vxlan Interface Status & Line Protocol == 'up' | Vxlan1 | NOT RUN | - |
| 486 | dc2-leaf2a | IP Reachability | ip reachability test p2p links | Source: dc2-leaf2a_Ethernet1 - Destination: dc2-spine1_Ethernet3 | NOT RUN | - |
| 487 | dc2-leaf2a | IP Reachability | ip reachability test p2p links | Source: dc2-leaf2a_Ethernet2 - Destination: dc2-spine2_Ethernet3 | NOT RUN | - |
| 488 | dc2-leaf2a | IP Reachability | ip reachability test p2p links | Source: dc2-leaf2a_Ethernet6 - Destination: dc1-leaf2a_Ethernet6 | NOT RUN | - |
| 489 | dc2-leaf2a | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet1 - remote: dc2-spine1_Ethernet3 | NOT RUN | - |
| 490 | dc2-leaf2a | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet2 - remote: dc2-spine2_Ethernet3 | NOT RUN | - |
| 491 | dc2-leaf2a | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet3 - remote: dc2-leaf2b_Ethernet3 | NOT RUN | - |
| 492 | dc2-leaf2a | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet4 - remote: dc2-leaf2b_Ethernet4 | NOT RUN | - |
| 493 | dc2-leaf2a | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet6 - remote: dc1-leaf2a_Ethernet6 | NOT RUN | - |
| 494 | dc2-leaf2a | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet8 - remote: dc2-leaf2c_Ethernet1 | NOT RUN | - |
| 495 | dc2-leaf2a | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf2a - 10.255.128.15/32 Destination: 10.255.0.1 | NOT RUN | - |
| 496 | dc2-leaf2a | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf2a - 10.255.128.15/32 Destination: 10.255.0.2 | NOT RUN | - |
| 497 | dc2-leaf2a | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf2a - 10.255.128.15/32 Destination: 10.255.0.3 | NOT RUN | - |
| 498 | dc2-leaf2a | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf2a - 10.255.128.15/32 Destination: 10.255.0.4 | NOT RUN | - |
| 499 | dc2-leaf2a | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf2a - 10.255.128.15/32 Destination: 10.255.0.5 | NOT RUN | - |
| 500 | dc2-leaf2a | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf2a - 10.255.128.15/32 Destination: 10.255.128.11 | NOT RUN | - |
| 501 | dc2-leaf2a | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf2a - 10.255.128.15/32 Destination: 10.255.128.12 | NOT RUN | - |
| 502 | dc2-leaf2a | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf2a - 10.255.128.15/32 Destination: 10.255.128.13 | NOT RUN | - |
| 503 | dc2-leaf2a | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf2a - 10.255.128.15/32 Destination: 10.255.128.14 | NOT RUN | - |
| 504 | dc2-leaf2a | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf2a - 10.255.128.15/32 Destination: 10.255.128.15 | NOT RUN | - |
| 505 | dc2-leaf2a | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf2a - 10.255.128.15/32 Destination: 10.255.128.16 | NOT RUN | - |
| 506 | dc2-leaf2a | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf2a - 10.255.128.15/32 Destination: 10.255.128.17 | NOT RUN | - |
| 507 | dc2-leaf2a | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf2a - 10.255.128.15/32 Destination: 10.255.128.18 | NOT RUN | - |
| 508 | dc2-leaf2a | MLAG | This test verifies the health status of the MLAG configuration. | VerifyMlagStatus | NOT RUN | - |
| 509 | dc2-leaf2a | NTP | Synchronised with NTP server | NTP | NOT RUN | - |
| 510 | dc2-leaf2a | Routing Table | Remote Lo0 address | 10.255.0.1 | NOT RUN | - |
| 511 | dc2-leaf2a | Routing Table | Remote Lo0 address | 10.255.0.2 | NOT RUN | - |
| 512 | dc2-leaf2a | Routing Table | Remote Lo0 address | 10.255.0.3 | NOT RUN | - |
| 513 | dc2-leaf2a | Routing Table | Remote Lo0 address | 10.255.0.4 | NOT RUN | - |
| 514 | dc2-leaf2a | Routing Table | Remote Lo0 address | 10.255.0.5 | NOT RUN | - |
| 515 | dc2-leaf2a | Routing Table | Remote Lo0 address | 10.255.128.11 | NOT RUN | - |
| 516 | dc2-leaf2a | Routing Table | Remote Lo0 address | 10.255.128.12 | NOT RUN | - |
| 517 | dc2-leaf2a | Routing Table | Remote Lo0 address | 10.255.128.13 | NOT RUN | - |
| 518 | dc2-leaf2a | Routing Table | Remote Lo0 address | 10.255.128.14 | NOT RUN | - |
| 519 | dc2-leaf2a | Routing Table | Remote Lo0 address | 10.255.128.15 | NOT RUN | - |
| 520 | dc2-leaf2a | Routing Table | Remote Lo0 address | 10.255.128.16 | NOT RUN | - |
| 521 | dc2-leaf2a | Routing Table | Remote Lo0 address | 10.255.128.17 | NOT RUN | - |
| 522 | dc2-leaf2a | Routing Table | Remote Lo0 address | 10.255.128.18 | NOT RUN | - |
| 523 | dc2-leaf2a | Routing Table | Remote VTEP address | 10.255.1.3 | NOT RUN | - |
| 524 | dc2-leaf2a | Routing Table | Remote VTEP address | 10.255.1.5 | NOT RUN | - |
| 525 | dc2-leaf2a | Routing Table | Remote VTEP address | 10.255.129.13 | NOT RUN | - |
| 526 | dc2-leaf2a | Routing Table | Remote VTEP address | 10.255.129.15 | NOT RUN | - |
| 527 | dc2-leaf2a | Routing Table | Remote VTEP address | 10.255.129.17 | NOT RUN | - |
| 528 | dc2-leaf2a | Security | Verifies if eAPI HTTPS server SSL profile is configured and valid. | VerifyAPIHttpsSSL | NOT RUN | - |
| 529 | dc2-leaf2b | BGP | ArBGP is configured and operating | ArBGP | NOT RUN | - |
| 530 | dc2-leaf2b | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.255.128.11 | NOT RUN | - |
| 531 | dc2-leaf2b | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.255.128.12 | NOT RUN | - |
| 532 | dc2-leaf2b | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.255.129.120 | NOT RUN | - |
| 533 | dc2-leaf2b | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.255.255.116 | NOT RUN | - |
| 534 | dc2-leaf2b | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.255.255.118 | NOT RUN | - |
| 535 | dc2-leaf2b | Hardware | Verifies if the device temperature is within the acceptable range. | VerifyTemperature | NOT RUN | - |
| 536 | dc2-leaf2b | Hardware | Verifies if the fans status are within the accepted states list. | VerifyEnvironmentCooling | NOT RUN | - |
| 537 | dc2-leaf2b | Hardware | Verifies if the power supplies status are within the accepted states list. | VerifyEnvironmentPower | NOT RUN | - |
| 538 | dc2-leaf2b | Hardware | Verifies the transceiver's manufacturer against a list of approved manufacturers. | VerifyTransceiversManufacturers | NOT RUN | - |
| 539 | dc2-leaf2b | Interface State | Ethernet Interface & Line Protocol == 'up' | Ethernet1 - P2P_LINK_TO_DC2-SPINE1_Ethernet4 | NOT RUN | - |
| 540 | dc2-leaf2b | Interface State | Ethernet Interface & Line Protocol == 'up' | Ethernet2 - P2P_LINK_TO_DC2-SPINE2_Ethernet4 | NOT RUN | - |
| 541 | dc2-leaf2b | Interface State | Ethernet Interface & Line Protocol == 'up' | Ethernet3 - MLAG_PEER_dc2-leaf2a_Ethernet3 | NOT RUN | - |
| 542 | dc2-leaf2b | Interface State | Ethernet Interface & Line Protocol == 'up' | Ethernet4 - MLAG_PEER_dc2-leaf2a_Ethernet4 | NOT RUN | - |
| 543 | dc2-leaf2b | Interface State | Ethernet Interface & Line Protocol == 'up' | Ethernet5 - dc2-leaf2-server1_PCI2 | NOT RUN | - |
| 544 | dc2-leaf2b | Interface State | Ethernet Interface & Line Protocol == 'up' | Ethernet6 - P2P_LINK_TO_dc1-leaf2b_Ethernet6 | NOT RUN | - |
| 545 | dc2-leaf2b | Interface State | Ethernet Interface & Line Protocol == 'up' | Ethernet8 - DC2-LEAF2C_Ethernet2 | NOT RUN | - |
| 546 | dc2-leaf2b | Interface State | Loopback Interface Status & Line Protocol == 'up' | Loopback0 - EVPN_Overlay_Peering | NOT RUN | - |
| 547 | dc2-leaf2b | Interface State | Loopback Interface Status & Line Protocol == 'up' | Loopback1 - VTEP_VXLAN_Tunnel_Source | NOT RUN | - |
| 548 | dc2-leaf2b | Interface State | Loopback Interface Status & Line Protocol == 'up' | Loopback10 - VRF10_VTEP_DIAGNOSTICS | NOT RUN | - |
| 549 | dc2-leaf2b | Interface State | Loopback Interface Status & Line Protocol == 'up' | Loopback11 - VRF11_VTEP_DIAGNOSTICS | NOT RUN | - |
| 550 | dc2-leaf2b | Interface State | Port-Channel Interface & Line Protocol == 'up' | Port-Channel3 - MLAG_PEER_dc2-leaf2a_Po3 | NOT RUN | - |
| 551 | dc2-leaf2b | Interface State | Port-Channel Interface & Line Protocol == 'up' | Port-Channel5 - dc2-leaf2-server1_PortChannel dc2-leaf2-server1 | NOT RUN | - |
| 552 | dc2-leaf2b | Interface State | Port-Channel Interface & Line Protocol == 'up' | Port-Channel8 - DC2-LEAF2C_Po1 | NOT RUN | - |
| 553 | dc2-leaf2b | Interface State | Vlan Interface & Line Protocol == 'up' | Vlan11 - VRF10_VLAN11 | NOT RUN | - |
| 554 | dc2-leaf2b | Interface State | Vlan Interface & Line Protocol == 'up' | Vlan12 - VRF10_VLAN12 | NOT RUN | - |
| 555 | dc2-leaf2b | Interface State | Vlan Interface & Line Protocol == 'up' | Vlan21 - VRF11_VLAN21 | NOT RUN | - |
| 556 | dc2-leaf2b | Interface State | Vlan Interface & Line Protocol == 'up' | Vlan22 - VRF11_VLAN22 | NOT RUN | - |
| 557 | dc2-leaf2b | Interface State | Vlan Interface & Line Protocol == 'up' | Vlan3009 - MLAG_PEER_L3_iBGP: vrf VRF10 | NOT RUN | - |
| 558 | dc2-leaf2b | Interface State | Vlan Interface & Line Protocol == 'up' | Vlan3010 - MLAG_PEER_L3_iBGP: vrf VRF11 | NOT RUN | - |
| 559 | dc2-leaf2b | Interface State | Vlan Interface & Line Protocol == 'up' | Vlan4093 - MLAG_PEER_L3_PEERING | NOT RUN | - |
| 560 | dc2-leaf2b | Interface State | Vlan Interface & Line Protocol == 'up' | Vlan4094 - MLAG_PEER | NOT RUN | - |
| 561 | dc2-leaf2b | Interface State | Vxlan Interface Status & Line Protocol == 'up' | Vxlan1 | NOT RUN | - |
| 562 | dc2-leaf2b | IP Reachability | ip reachability test p2p links | Source: dc2-leaf2b_Ethernet1 - Destination: dc2-spine1_Ethernet4 | NOT RUN | - |
| 563 | dc2-leaf2b | IP Reachability | ip reachability test p2p links | Source: dc2-leaf2b_Ethernet2 - Destination: dc2-spine2_Ethernet4 | NOT RUN | - |
| 564 | dc2-leaf2b | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet1 - remote: dc2-spine1_Ethernet4 | NOT RUN | - |
| 565 | dc2-leaf2b | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet2 - remote: dc2-spine2_Ethernet4 | NOT RUN | - |
| 566 | dc2-leaf2b | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet3 - remote: dc2-leaf2a_Ethernet3 | NOT RUN | - |
| 567 | dc2-leaf2b | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet4 - remote: dc2-leaf2a_Ethernet4 | NOT RUN | - |
| 568 | dc2-leaf2b | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet8 - remote: dc2-leaf2c_Ethernet2 | NOT RUN | - |
| 569 | dc2-leaf2b | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf2b - 10.255.128.16/32 Destination: 10.255.0.1 | NOT RUN | - |
| 570 | dc2-leaf2b | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf2b - 10.255.128.16/32 Destination: 10.255.0.2 | NOT RUN | - |
| 571 | dc2-leaf2b | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf2b - 10.255.128.16/32 Destination: 10.255.0.3 | NOT RUN | - |
| 572 | dc2-leaf2b | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf2b - 10.255.128.16/32 Destination: 10.255.0.4 | NOT RUN | - |
| 573 | dc2-leaf2b | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf2b - 10.255.128.16/32 Destination: 10.255.0.5 | NOT RUN | - |
| 574 | dc2-leaf2b | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf2b - 10.255.128.16/32 Destination: 10.255.128.11 | NOT RUN | - |
| 575 | dc2-leaf2b | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf2b - 10.255.128.16/32 Destination: 10.255.128.12 | NOT RUN | - |
| 576 | dc2-leaf2b | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf2b - 10.255.128.16/32 Destination: 10.255.128.13 | NOT RUN | - |
| 577 | dc2-leaf2b | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf2b - 10.255.128.16/32 Destination: 10.255.128.14 | NOT RUN | - |
| 578 | dc2-leaf2b | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf2b - 10.255.128.16/32 Destination: 10.255.128.15 | NOT RUN | - |
| 579 | dc2-leaf2b | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf2b - 10.255.128.16/32 Destination: 10.255.128.16 | NOT RUN | - |
| 580 | dc2-leaf2b | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf2b - 10.255.128.16/32 Destination: 10.255.128.17 | NOT RUN | - |
| 581 | dc2-leaf2b | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf2b - 10.255.128.16/32 Destination: 10.255.128.18 | NOT RUN | - |
| 582 | dc2-leaf2b | MLAG | This test verifies the health status of the MLAG configuration. | VerifyMlagStatus | NOT RUN | - |
| 583 | dc2-leaf2b | NTP | Synchronised with NTP server | NTP | NOT RUN | - |
| 584 | dc2-leaf2b | Routing Table | Remote Lo0 address | 10.255.0.1 | NOT RUN | - |
| 585 | dc2-leaf2b | Routing Table | Remote Lo0 address | 10.255.0.2 | NOT RUN | - |
| 586 | dc2-leaf2b | Routing Table | Remote Lo0 address | 10.255.0.3 | NOT RUN | - |
| 587 | dc2-leaf2b | Routing Table | Remote Lo0 address | 10.255.0.4 | NOT RUN | - |
| 588 | dc2-leaf2b | Routing Table | Remote Lo0 address | 10.255.0.5 | NOT RUN | - |
| 589 | dc2-leaf2b | Routing Table | Remote Lo0 address | 10.255.128.11 | NOT RUN | - |
| 590 | dc2-leaf2b | Routing Table | Remote Lo0 address | 10.255.128.12 | NOT RUN | - |
| 591 | dc2-leaf2b | Routing Table | Remote Lo0 address | 10.255.128.13 | NOT RUN | - |
| 592 | dc2-leaf2b | Routing Table | Remote Lo0 address | 10.255.128.14 | NOT RUN | - |
| 593 | dc2-leaf2b | Routing Table | Remote Lo0 address | 10.255.128.15 | NOT RUN | - |
| 594 | dc2-leaf2b | Routing Table | Remote Lo0 address | 10.255.128.16 | NOT RUN | - |
| 595 | dc2-leaf2b | Routing Table | Remote Lo0 address | 10.255.128.17 | NOT RUN | - |
| 596 | dc2-leaf2b | Routing Table | Remote Lo0 address | 10.255.128.18 | NOT RUN | - |
| 597 | dc2-leaf2b | Routing Table | Remote VTEP address | 10.255.1.3 | NOT RUN | - |
| 598 | dc2-leaf2b | Routing Table | Remote VTEP address | 10.255.1.5 | NOT RUN | - |
| 599 | dc2-leaf2b | Routing Table | Remote VTEP address | 10.255.129.13 | NOT RUN | - |
| 600 | dc2-leaf2b | Routing Table | Remote VTEP address | 10.255.129.15 | NOT RUN | - |
| 601 | dc2-leaf2b | Routing Table | Remote VTEP address | 10.255.129.17 | NOT RUN | - |
| 602 | dc2-leaf2b | Security | Verifies if eAPI HTTPS server SSL profile is configured and valid. | VerifyAPIHttpsSSL | NOT RUN | - |
| 603 | dc2-leaf2c | Hardware | Verifies if the device temperature is within the acceptable range. | VerifyTemperature | NOT RUN | - |
| 604 | dc2-leaf2c | Hardware | Verifies if the fans status are within the accepted states list. | VerifyEnvironmentCooling | NOT RUN | - |
| 605 | dc2-leaf2c | Hardware | Verifies if the power supplies status are within the accepted states list. | VerifyEnvironmentPower | NOT RUN | - |
| 606 | dc2-leaf2c | Hardware | Verifies the transceiver's manufacturer against a list of approved manufacturers. | VerifyTransceiversManufacturers | NOT RUN | - |
| 607 | dc2-leaf2c | Interface State | Ethernet Interface & Line Protocol == 'up' | Ethernet1 - DC2-LEAF2A_Ethernet8 | NOT RUN | - |
| 608 | dc2-leaf2c | Interface State | Ethernet Interface & Line Protocol == 'up' | Ethernet2 - DC2-LEAF2B_Ethernet8 | NOT RUN | - |
| 609 | dc2-leaf2c | Interface State | Ethernet Interface & Line Protocol == 'up' | Ethernet5 - dc2-leaf2-server1_iLO | NOT RUN | - |
| 610 | dc2-leaf2c | Interface State | Port-Channel Interface & Line Protocol == 'up' | Port-Channel1 - DC2_L3_LEAF2_Po8 | NOT RUN | - |
| 611 | dc2-leaf2c | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet1 - remote: dc2-leaf2a_Ethernet8 | NOT RUN | - |
| 612 | dc2-leaf2c | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet2 - remote: dc2-leaf2b_Ethernet8 | NOT RUN | - |
| 613 | dc2-leaf2c | NTP | Synchronised with NTP server | NTP | NOT RUN | - |
| 614 | dc2-leaf2c | Security | Verifies if eAPI HTTPS server SSL profile is configured and valid. | VerifyAPIHttpsSSL | NOT RUN | - |
| 615 | dc2-leaf3a.arista.com | BGP | ArBGP is configured and operating | ArBGP | NOT RUN | - |
| 616 | dc2-leaf3a.arista.com | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.255.128.11 | NOT RUN | - |
| 617 | dc2-leaf3a.arista.com | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.255.128.12 | NOT RUN | - |
| 618 | dc2-leaf3a.arista.com | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.255.129.125 | NOT RUN | - |
| 619 | dc2-leaf3a.arista.com | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.255.255.120 | NOT RUN | - |
| 620 | dc2-leaf3a.arista.com | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.255.255.122 | NOT RUN | - |
| 621 | dc2-leaf3a.arista.com | Hardware | Verifies if the device temperature is within the acceptable range. | VerifyTemperature | NOT RUN | - |
| 622 | dc2-leaf3a.arista.com | Hardware | Verifies if the fans status are within the accepted states list. | VerifyEnvironmentCooling | NOT RUN | - |
| 623 | dc2-leaf3a.arista.com | Hardware | Verifies if the power supplies status are within the accepted states list. | VerifyEnvironmentPower | NOT RUN | - |
| 624 | dc2-leaf3a.arista.com | Hardware | Verifies the transceiver's manufacturer against a list of approved manufacturers. | VerifyTransceiversManufacturers | NOT RUN | - |
| 625 | dc2-leaf3a.arista.com | Interface State | Ethernet Interface & Line Protocol == 'up' | Ethernet1 - P2P_LINK_TO_DC2-SPINE1_Ethernet5 | NOT RUN | - |
| 626 | dc2-leaf3a.arista.com | Interface State | Ethernet Interface & Line Protocol == 'up' | Ethernet11 - dc2-leaf3-fw1_e1 | NOT RUN | - |
| 627 | dc2-leaf3a.arista.com | Interface State | Ethernet Interface & Line Protocol == 'up' | Ethernet2 - P2P_LINK_TO_DC2-SPINE2_Ethernet5 | NOT RUN | - |
| 628 | dc2-leaf3a.arista.com | Interface State | Ethernet Interface & Line Protocol == 'up' | Ethernet3 - MLAG_PEER_dc2-leaf3b.arista.com_Ethernet3 | NOT RUN | - |
| 629 | dc2-leaf3a.arista.com | Interface State | Ethernet Interface & Line Protocol == 'up' | Ethernet4 - MLAG_PEER_dc2-leaf3b.arista.com_Ethernet4 | NOT RUN | - |
| 630 | dc2-leaf3a.arista.com | Interface State | Loopback Interface Status & Line Protocol == 'up' | Loopback0 - EVPN_Overlay_Peering | NOT RUN | - |
| 631 | dc2-leaf3a.arista.com | Interface State | Loopback Interface Status & Line Protocol == 'up' | Loopback1 - VTEP_VXLAN_Tunnel_Source | NOT RUN | - |
| 632 | dc2-leaf3a.arista.com | Interface State | Loopback Interface Status & Line Protocol == 'up' | Loopback10 - VRF10_VTEP_DIAGNOSTICS | NOT RUN | - |
| 633 | dc2-leaf3a.arista.com | Interface State | Loopback Interface Status & Line Protocol == 'up' | Loopback11 - VRF11_VTEP_DIAGNOSTICS | NOT RUN | - |
| 634 | dc2-leaf3a.arista.com | Interface State | Port-Channel Interface & Line Protocol == 'up' | Port-Channel11 - dc2-leaf3-fw1_PortChannel | NOT RUN | - |
| 635 | dc2-leaf3a.arista.com | Interface State | Port-Channel Interface & Line Protocol == 'up' | Port-Channel3 - MLAG_PEER_dc2-leaf3b.arista.com_Po3 | NOT RUN | - |
| 636 | dc2-leaf3a.arista.com | Interface State | Vlan Interface & Line Protocol == 'up' | Vlan11 - VRF10_VLAN11 | NOT RUN | - |
| 637 | dc2-leaf3a.arista.com | Interface State | Vlan Interface & Line Protocol == 'up' | Vlan12 - VRF10_VLAN12 | NOT RUN | - |
| 638 | dc2-leaf3a.arista.com | Interface State | Vlan Interface & Line Protocol == 'up' | Vlan21 - VRF11_VLAN21 | NOT RUN | - |
| 639 | dc2-leaf3a.arista.com | Interface State | Vlan Interface & Line Protocol == 'up' | Vlan22 - VRF11_VLAN22 | NOT RUN | - |
| 640 | dc2-leaf3a.arista.com | Interface State | Vlan Interface & Line Protocol == 'up' | Vlan3009 - MLAG_PEER_L3_iBGP: vrf VRF10 | NOT RUN | - |
| 641 | dc2-leaf3a.arista.com | Interface State | Vlan Interface & Line Protocol == 'up' | Vlan3010 - MLAG_PEER_L3_iBGP: vrf VRF11 | NOT RUN | - |
| 642 | dc2-leaf3a.arista.com | Interface State | Vlan Interface & Line Protocol == 'up' | Vlan4093 - MLAG_PEER_L3_PEERING | NOT RUN | - |
| 643 | dc2-leaf3a.arista.com | Interface State | Vlan Interface & Line Protocol == 'up' | Vlan4094 - MLAG_PEER | NOT RUN | - |
| 644 | dc2-leaf3a.arista.com | Interface State | Vxlan Interface Status & Line Protocol == 'up' | Vxlan1 | NOT RUN | - |
| 645 | dc2-leaf3a.arista.com | IP Reachability | ip reachability test p2p links | Source: dc2-leaf3a.arista.com_Ethernet1 - Destination: dc2-spine1_Ethernet5 | NOT RUN | - |
| 646 | dc2-leaf3a.arista.com | IP Reachability | ip reachability test p2p links | Source: dc2-leaf3a.arista.com_Ethernet2 - Destination: dc2-spine2_Ethernet5 | NOT RUN | - |
| 647 | dc2-leaf3a.arista.com | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet1 - remote: dc2-spine1_Ethernet5 | NOT RUN | - |
| 648 | dc2-leaf3a.arista.com | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet2 - remote: dc2-spine2_Ethernet5 | NOT RUN | - |
| 649 | dc2-leaf3a.arista.com | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet3 - remote: dc2-leaf3b.arista.com_Ethernet3 | NOT RUN | - |
| 650 | dc2-leaf3a.arista.com | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet4 - remote: dc2-leaf3b.arista.com_Ethernet4 | NOT RUN | - |
| 651 | dc2-leaf3a.arista.com | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf3a.arista.com - 10.255.128.17/32 Destination: 10.255.0.1 | NOT RUN | - |
| 652 | dc2-leaf3a.arista.com | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf3a.arista.com - 10.255.128.17/32 Destination: 10.255.0.2 | NOT RUN | - |
| 653 | dc2-leaf3a.arista.com | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf3a.arista.com - 10.255.128.17/32 Destination: 10.255.0.3 | NOT RUN | - |
| 654 | dc2-leaf3a.arista.com | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf3a.arista.com - 10.255.128.17/32 Destination: 10.255.0.4 | NOT RUN | - |
| 655 | dc2-leaf3a.arista.com | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf3a.arista.com - 10.255.128.17/32 Destination: 10.255.0.5 | NOT RUN | - |
| 656 | dc2-leaf3a.arista.com | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf3a.arista.com - 10.255.128.17/32 Destination: 10.255.128.11 | NOT RUN | - |
| 657 | dc2-leaf3a.arista.com | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf3a.arista.com - 10.255.128.17/32 Destination: 10.255.128.12 | NOT RUN | - |
| 658 | dc2-leaf3a.arista.com | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf3a.arista.com - 10.255.128.17/32 Destination: 10.255.128.13 | NOT RUN | - |
| 659 | dc2-leaf3a.arista.com | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf3a.arista.com - 10.255.128.17/32 Destination: 10.255.128.14 | NOT RUN | - |
| 660 | dc2-leaf3a.arista.com | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf3a.arista.com - 10.255.128.17/32 Destination: 10.255.128.15 | NOT RUN | - |
| 661 | dc2-leaf3a.arista.com | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf3a.arista.com - 10.255.128.17/32 Destination: 10.255.128.16 | NOT RUN | - |
| 662 | dc2-leaf3a.arista.com | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf3a.arista.com - 10.255.128.17/32 Destination: 10.255.128.17 | NOT RUN | - |
| 663 | dc2-leaf3a.arista.com | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf3a.arista.com - 10.255.128.17/32 Destination: 10.255.128.18 | NOT RUN | - |
| 664 | dc2-leaf3a.arista.com | MLAG | This test verifies the health status of the MLAG configuration. | VerifyMlagStatus | NOT RUN | - |
| 665 | dc2-leaf3a.arista.com | NTP | Synchronised with NTP server | NTP | NOT RUN | - |
| 666 | dc2-leaf3a.arista.com | Routing Table | Remote Lo0 address | 10.255.0.1 | NOT RUN | - |
| 667 | dc2-leaf3a.arista.com | Routing Table | Remote Lo0 address | 10.255.0.2 | NOT RUN | - |
| 668 | dc2-leaf3a.arista.com | Routing Table | Remote Lo0 address | 10.255.0.3 | NOT RUN | - |
| 669 | dc2-leaf3a.arista.com | Routing Table | Remote Lo0 address | 10.255.0.4 | NOT RUN | - |
| 670 | dc2-leaf3a.arista.com | Routing Table | Remote Lo0 address | 10.255.0.5 | NOT RUN | - |
| 671 | dc2-leaf3a.arista.com | Routing Table | Remote Lo0 address | 10.255.128.11 | NOT RUN | - |
| 672 | dc2-leaf3a.arista.com | Routing Table | Remote Lo0 address | 10.255.128.12 | NOT RUN | - |
| 673 | dc2-leaf3a.arista.com | Routing Table | Remote Lo0 address | 10.255.128.13 | NOT RUN | - |
| 674 | dc2-leaf3a.arista.com | Routing Table | Remote Lo0 address | 10.255.128.14 | NOT RUN | - |
| 675 | dc2-leaf3a.arista.com | Routing Table | Remote Lo0 address | 10.255.128.15 | NOT RUN | - |
| 676 | dc2-leaf3a.arista.com | Routing Table | Remote Lo0 address | 10.255.128.16 | NOT RUN | - |
| 677 | dc2-leaf3a.arista.com | Routing Table | Remote Lo0 address | 10.255.128.17 | NOT RUN | - |
| 678 | dc2-leaf3a.arista.com | Routing Table | Remote Lo0 address | 10.255.128.18 | NOT RUN | - |
| 679 | dc2-leaf3a.arista.com | Routing Table | Remote VTEP address | 10.255.1.3 | NOT RUN | - |
| 680 | dc2-leaf3a.arista.com | Routing Table | Remote VTEP address | 10.255.1.5 | NOT RUN | - |
| 681 | dc2-leaf3a.arista.com | Routing Table | Remote VTEP address | 10.255.129.13 | NOT RUN | - |
| 682 | dc2-leaf3a.arista.com | Routing Table | Remote VTEP address | 10.255.129.15 | NOT RUN | - |
| 683 | dc2-leaf3a.arista.com | Routing Table | Remote VTEP address | 10.255.129.17 | NOT RUN | - |
| 684 | dc2-leaf3a.arista.com | Security | Verifies if eAPI HTTPS server SSL profile is configured and valid. | VerifyAPIHttpsSSL | NOT RUN | - |
| 685 | dc2-leaf3b.arista.com | BGP | ArBGP is configured and operating | ArBGP | NOT RUN | - |
| 686 | dc2-leaf3b.arista.com | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.255.128.11 | NOT RUN | - |
| 687 | dc2-leaf3b.arista.com | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.255.128.12 | NOT RUN | - |
| 688 | dc2-leaf3b.arista.com | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.255.129.124 | NOT RUN | - |
| 689 | dc2-leaf3b.arista.com | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.255.255.124 | NOT RUN | - |
| 690 | dc2-leaf3b.arista.com | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.255.255.126 | NOT RUN | - |
| 691 | dc2-leaf3b.arista.com | Hardware | Verifies if the device temperature is within the acceptable range. | VerifyTemperature | NOT RUN | - |
| 692 | dc2-leaf3b.arista.com | Hardware | Verifies if the fans status are within the accepted states list. | VerifyEnvironmentCooling | NOT RUN | - |
| 693 | dc2-leaf3b.arista.com | Hardware | Verifies if the power supplies status are within the accepted states list. | VerifyEnvironmentPower | NOT RUN | - |
| 694 | dc2-leaf3b.arista.com | Hardware | Verifies the transceiver's manufacturer against a list of approved manufacturers. | VerifyTransceiversManufacturers | NOT RUN | - |
| 695 | dc2-leaf3b.arista.com | Interface State | Ethernet Interface & Line Protocol == 'adminDown' | Ethernet11 - dc2-leaf3-fw1_e1 | NOT RUN | - |
| 696 | dc2-leaf3b.arista.com | Interface State | Ethernet Interface & Line Protocol == 'up' | Ethernet1 - P2P_LINK_TO_DC2-SPINE1_Ethernet6 | NOT RUN | - |
| 697 | dc2-leaf3b.arista.com | Interface State | Ethernet Interface & Line Protocol == 'up' | Ethernet2 - P2P_LINK_TO_DC2-SPINE2_Ethernet6 | NOT RUN | - |
| 698 | dc2-leaf3b.arista.com | Interface State | Ethernet Interface & Line Protocol == 'up' | Ethernet3 - MLAG_PEER_dc2-leaf3a.arista.com_Ethernet3 | NOT RUN | - |
| 699 | dc2-leaf3b.arista.com | Interface State | Ethernet Interface & Line Protocol == 'up' | Ethernet4 - MLAG_PEER_dc2-leaf3a.arista.com_Ethernet4 | NOT RUN | - |
| 700 | dc2-leaf3b.arista.com | Interface State | Loopback Interface Status & Line Protocol == 'up' | Loopback0 - EVPN_Overlay_Peering | NOT RUN | - |
| 701 | dc2-leaf3b.arista.com | Interface State | Loopback Interface Status & Line Protocol == 'up' | Loopback1 - VTEP_VXLAN_Tunnel_Source | NOT RUN | - |
| 702 | dc2-leaf3b.arista.com | Interface State | Loopback Interface Status & Line Protocol == 'up' | Loopback10 - VRF10_VTEP_DIAGNOSTICS | NOT RUN | - |
| 703 | dc2-leaf3b.arista.com | Interface State | Loopback Interface Status & Line Protocol == 'up' | Loopback11 - VRF11_VTEP_DIAGNOSTICS | NOT RUN | - |
| 704 | dc2-leaf3b.arista.com | Interface State | Port-Channel Interface & Line Protocol == 'up' | Port-Channel11 - dc2-leaf3-fw1_PortChannel | NOT RUN | - |
| 705 | dc2-leaf3b.arista.com | Interface State | Port-Channel Interface & Line Protocol == 'up' | Port-Channel3 - MLAG_PEER_dc2-leaf3a.arista.com_Po3 | NOT RUN | - |
| 706 | dc2-leaf3b.arista.com | Interface State | Vlan Interface & Line Protocol == 'up' | Vlan11 - VRF10_VLAN11 | NOT RUN | - |
| 707 | dc2-leaf3b.arista.com | Interface State | Vlan Interface & Line Protocol == 'up' | Vlan12 - VRF10_VLAN12 | NOT RUN | - |
| 708 | dc2-leaf3b.arista.com | Interface State | Vlan Interface & Line Protocol == 'up' | Vlan21 - VRF11_VLAN21 | NOT RUN | - |
| 709 | dc2-leaf3b.arista.com | Interface State | Vlan Interface & Line Protocol == 'up' | Vlan22 - VRF11_VLAN22 | NOT RUN | - |
| 710 | dc2-leaf3b.arista.com | Interface State | Vlan Interface & Line Protocol == 'up' | Vlan3009 - MLAG_PEER_L3_iBGP: vrf VRF10 | NOT RUN | - |
| 711 | dc2-leaf3b.arista.com | Interface State | Vlan Interface & Line Protocol == 'up' | Vlan3010 - MLAG_PEER_L3_iBGP: vrf VRF11 | NOT RUN | - |
| 712 | dc2-leaf3b.arista.com | Interface State | Vlan Interface & Line Protocol == 'up' | Vlan4093 - MLAG_PEER_L3_PEERING | NOT RUN | - |
| 713 | dc2-leaf3b.arista.com | Interface State | Vlan Interface & Line Protocol == 'up' | Vlan4094 - MLAG_PEER | NOT RUN | - |
| 714 | dc2-leaf3b.arista.com | Interface State | Vxlan Interface Status & Line Protocol == 'up' | Vxlan1 | NOT RUN | - |
| 715 | dc2-leaf3b.arista.com | IP Reachability | ip reachability test p2p links | Source: dc2-leaf3b.arista.com_Ethernet1 - Destination: dc2-spine1_Ethernet6 | NOT RUN | - |
| 716 | dc2-leaf3b.arista.com | IP Reachability | ip reachability test p2p links | Source: dc2-leaf3b.arista.com_Ethernet2 - Destination: dc2-spine2_Ethernet6 | NOT RUN | - |
| 717 | dc2-leaf3b.arista.com | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet1 - remote: dc2-spine1_Ethernet6 | NOT RUN | - |
| 718 | dc2-leaf3b.arista.com | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet2 - remote: dc2-spine2_Ethernet6 | NOT RUN | - |
| 719 | dc2-leaf3b.arista.com | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet3 - remote: dc2-leaf3a.arista.com_Ethernet3 | NOT RUN | - |
| 720 | dc2-leaf3b.arista.com | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet4 - remote: dc2-leaf3a.arista.com_Ethernet4 | NOT RUN | - |
| 721 | dc2-leaf3b.arista.com | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf3b.arista.com - 10.255.128.18/32 Destination: 10.255.0.1 | NOT RUN | - |
| 722 | dc2-leaf3b.arista.com | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf3b.arista.com - 10.255.128.18/32 Destination: 10.255.0.2 | NOT RUN | - |
| 723 | dc2-leaf3b.arista.com | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf3b.arista.com - 10.255.128.18/32 Destination: 10.255.0.3 | NOT RUN | - |
| 724 | dc2-leaf3b.arista.com | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf3b.arista.com - 10.255.128.18/32 Destination: 10.255.0.4 | NOT RUN | - |
| 725 | dc2-leaf3b.arista.com | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf3b.arista.com - 10.255.128.18/32 Destination: 10.255.0.5 | NOT RUN | - |
| 726 | dc2-leaf3b.arista.com | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf3b.arista.com - 10.255.128.18/32 Destination: 10.255.128.11 | NOT RUN | - |
| 727 | dc2-leaf3b.arista.com | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf3b.arista.com - 10.255.128.18/32 Destination: 10.255.128.12 | NOT RUN | - |
| 728 | dc2-leaf3b.arista.com | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf3b.arista.com - 10.255.128.18/32 Destination: 10.255.128.13 | NOT RUN | - |
| 729 | dc2-leaf3b.arista.com | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf3b.arista.com - 10.255.128.18/32 Destination: 10.255.128.14 | NOT RUN | - |
| 730 | dc2-leaf3b.arista.com | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf3b.arista.com - 10.255.128.18/32 Destination: 10.255.128.15 | NOT RUN | - |
| 731 | dc2-leaf3b.arista.com | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf3b.arista.com - 10.255.128.18/32 Destination: 10.255.128.16 | NOT RUN | - |
| 732 | dc2-leaf3b.arista.com | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf3b.arista.com - 10.255.128.18/32 Destination: 10.255.128.17 | NOT RUN | - |
| 733 | dc2-leaf3b.arista.com | Loopback0 Reachability | Loopback0 Reachability | Source: dc2-leaf3b.arista.com - 10.255.128.18/32 Destination: 10.255.128.18 | NOT RUN | - |
| 734 | dc2-leaf3b.arista.com | MLAG | This test verifies the health status of the MLAG configuration. | VerifyMlagStatus | NOT RUN | - |
| 735 | dc2-leaf3b.arista.com | NTP | Synchronised with NTP server | NTP | NOT RUN | - |
| 736 | dc2-leaf3b.arista.com | Routing Table | Remote Lo0 address | 10.255.0.1 | NOT RUN | - |
| 737 | dc2-leaf3b.arista.com | Routing Table | Remote Lo0 address | 10.255.0.2 | NOT RUN | - |
| 738 | dc2-leaf3b.arista.com | Routing Table | Remote Lo0 address | 10.255.0.3 | NOT RUN | - |
| 739 | dc2-leaf3b.arista.com | Routing Table | Remote Lo0 address | 10.255.0.4 | NOT RUN | - |
| 740 | dc2-leaf3b.arista.com | Routing Table | Remote Lo0 address | 10.255.0.5 | NOT RUN | - |
| 741 | dc2-leaf3b.arista.com | Routing Table | Remote Lo0 address | 10.255.128.11 | NOT RUN | - |
| 742 | dc2-leaf3b.arista.com | Routing Table | Remote Lo0 address | 10.255.128.12 | NOT RUN | - |
| 743 | dc2-leaf3b.arista.com | Routing Table | Remote Lo0 address | 10.255.128.13 | NOT RUN | - |
| 744 | dc2-leaf3b.arista.com | Routing Table | Remote Lo0 address | 10.255.128.14 | NOT RUN | - |
| 745 | dc2-leaf3b.arista.com | Routing Table | Remote Lo0 address | 10.255.128.15 | NOT RUN | - |
| 746 | dc2-leaf3b.arista.com | Routing Table | Remote Lo0 address | 10.255.128.16 | NOT RUN | - |
| 747 | dc2-leaf3b.arista.com | Routing Table | Remote Lo0 address | 10.255.128.17 | NOT RUN | - |
| 748 | dc2-leaf3b.arista.com | Routing Table | Remote Lo0 address | 10.255.128.18 | NOT RUN | - |
| 749 | dc2-leaf3b.arista.com | Routing Table | Remote VTEP address | 10.255.1.3 | NOT RUN | - |
| 750 | dc2-leaf3b.arista.com | Routing Table | Remote VTEP address | 10.255.1.5 | NOT RUN | - |
| 751 | dc2-leaf3b.arista.com | Routing Table | Remote VTEP address | 10.255.129.13 | NOT RUN | - |
| 752 | dc2-leaf3b.arista.com | Routing Table | Remote VTEP address | 10.255.129.15 | NOT RUN | - |
| 753 | dc2-leaf3b.arista.com | Routing Table | Remote VTEP address | 10.255.129.17 | NOT RUN | - |
| 754 | dc2-leaf3b.arista.com | Security | Verifies if eAPI HTTPS server SSL profile is configured and valid. | VerifyAPIHttpsSSL | NOT RUN | - |
| 755 | dc2-spine1 | BGP | ArBGP is configured and operating | ArBGP | NOT RUN | - |
| 756 | dc2-spine1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.255.128.13 | NOT RUN | - |
| 757 | dc2-spine1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.255.128.14 | NOT RUN | - |
| 758 | dc2-spine1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.255.128.15 | NOT RUN | - |
| 759 | dc2-spine1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.255.128.16 | NOT RUN | - |
| 760 | dc2-spine1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.255.128.17 | NOT RUN | - |
| 761 | dc2-spine1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.255.128.18 | NOT RUN | - |
| 762 | dc2-spine1 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.255.255.105 | NOT RUN | - |
| 763 | dc2-spine1 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.255.255.109 | NOT RUN | - |
| 764 | dc2-spine1 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.255.255.113 | NOT RUN | - |
| 765 | dc2-spine1 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.255.255.117 | NOT RUN | - |
| 766 | dc2-spine1 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.255.255.121 | NOT RUN | - |
| 767 | dc2-spine1 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.255.255.125 | NOT RUN | - |
| 768 | dc2-spine1 | Hardware | Verifies if the device temperature is within the acceptable range. | VerifyTemperature | NOT RUN | - |
| 769 | dc2-spine1 | Hardware | Verifies if the fans status are within the accepted states list. | VerifyEnvironmentCooling | NOT RUN | - |
| 770 | dc2-spine1 | Hardware | Verifies if the power supplies status are within the accepted states list. | VerifyEnvironmentPower | NOT RUN | - |
| 771 | dc2-spine1 | Hardware | Verifies the transceiver's manufacturer against a list of approved manufacturers. | VerifyTransceiversManufacturers | NOT RUN | - |
| 772 | dc2-spine1 | Interface State | Ethernet Interface & Line Protocol == 'up' | Ethernet1 - P2P_LINK_TO_DC2-LEAF1A_Ethernet1 | NOT RUN | - |
| 773 | dc2-spine1 | Interface State | Ethernet Interface & Line Protocol == 'up' | Ethernet2 - P2P_LINK_TO_DC2-LEAF1B_Ethernet1 | NOT RUN | - |
| 774 | dc2-spine1 | Interface State | Ethernet Interface & Line Protocol == 'up' | Ethernet3 - P2P_LINK_TO_DC2-LEAF2A_Ethernet1 | NOT RUN | - |
| 775 | dc2-spine1 | Interface State | Ethernet Interface & Line Protocol == 'up' | Ethernet4 - P2P_LINK_TO_DC2-LEAF2B_Ethernet1 | NOT RUN | - |
| 776 | dc2-spine1 | Interface State | Ethernet Interface & Line Protocol == 'up' | Ethernet5 - P2P_LINK_TO_DC2-LEAF3A.ARISTA.COM_Ethernet1 | NOT RUN | - |
| 777 | dc2-spine1 | Interface State | Ethernet Interface & Line Protocol == 'up' | Ethernet6 - P2P_LINK_TO_DC2-LEAF3B.ARISTA.COM_Ethernet1 | NOT RUN | - |
| 778 | dc2-spine1 | Interface State | Loopback Interface Status & Line Protocol == 'up' | Loopback0 - EVPN_Overlay_Peering | NOT RUN | - |
| 779 | dc2-spine1 | IP Reachability | ip reachability test p2p links | Source: dc2-spine1_Ethernet1 - Destination: dc2-leaf1a_Ethernet1 | NOT RUN | - |
| 780 | dc2-spine1 | IP Reachability | ip reachability test p2p links | Source: dc2-spine1_Ethernet2 - Destination: dc2-leaf1b_Ethernet1 | NOT RUN | - |
| 781 | dc2-spine1 | IP Reachability | ip reachability test p2p links | Source: dc2-spine1_Ethernet3 - Destination: dc2-leaf2a_Ethernet1 | NOT RUN | - |
| 782 | dc2-spine1 | IP Reachability | ip reachability test p2p links | Source: dc2-spine1_Ethernet4 - Destination: dc2-leaf2b_Ethernet1 | NOT RUN | - |
| 783 | dc2-spine1 | IP Reachability | ip reachability test p2p links | Source: dc2-spine1_Ethernet5 - Destination: dc2-leaf3a.arista.com_Ethernet1 | NOT RUN | - |
| 784 | dc2-spine1 | IP Reachability | ip reachability test p2p links | Source: dc2-spine1_Ethernet6 - Destination: dc2-leaf3b.arista.com_Ethernet1 | NOT RUN | - |
| 785 | dc2-spine1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet1 - remote: dc2-leaf1a_Ethernet1 | NOT RUN | - |
| 786 | dc2-spine1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet2 - remote: dc2-leaf1b_Ethernet1 | NOT RUN | - |
| 787 | dc2-spine1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet3 - remote: dc2-leaf2a_Ethernet1 | NOT RUN | - |
| 788 | dc2-spine1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet4 - remote: dc2-leaf2b_Ethernet1 | NOT RUN | - |
| 789 | dc2-spine1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet5 - remote: dc2-leaf3a.arista.com_Ethernet1 | NOT RUN | - |
| 790 | dc2-spine1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet6 - remote: dc2-leaf3b.arista.com_Ethernet1 | NOT RUN | - |
| 791 | dc2-spine1 | NTP | Synchronised with NTP server | NTP | NOT RUN | - |
| 792 | dc2-spine1 | Security | Verifies if eAPI HTTPS server SSL profile is configured and valid. | VerifyAPIHttpsSSL | NOT RUN | - |
| 793 | dc2-spine2 | BGP | ArBGP is configured and operating | ArBGP | NOT RUN | - |
| 794 | dc2-spine2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.255.128.13 | NOT RUN | - |
| 795 | dc2-spine2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.255.128.14 | NOT RUN | - |
| 796 | dc2-spine2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.255.128.15 | NOT RUN | - |
| 797 | dc2-spine2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.255.128.16 | NOT RUN | - |
| 798 | dc2-spine2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.255.128.17 | NOT RUN | - |
| 799 | dc2-spine2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.255.128.18 | NOT RUN | - |
| 800 | dc2-spine2 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.255.255.107 | NOT RUN | - |
| 801 | dc2-spine2 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.255.255.111 | NOT RUN | - |
| 802 | dc2-spine2 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.255.255.115 | NOT RUN | - |
| 803 | dc2-spine2 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.255.255.119 | NOT RUN | - |
| 804 | dc2-spine2 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.255.255.123 | NOT RUN | - |
| 805 | dc2-spine2 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.255.255.127 | NOT RUN | - |
| 806 | dc2-spine2 | Hardware | Verifies if the device temperature is within the acceptable range. | VerifyTemperature | NOT RUN | - |
| 807 | dc2-spine2 | Hardware | Verifies if the fans status are within the accepted states list. | VerifyEnvironmentCooling | NOT RUN | - |
| 808 | dc2-spine2 | Hardware | Verifies if the power supplies status are within the accepted states list. | VerifyEnvironmentPower | NOT RUN | - |
| 809 | dc2-spine2 | Hardware | Verifies the transceiver's manufacturer against a list of approved manufacturers. | VerifyTransceiversManufacturers | NOT RUN | - |
| 810 | dc2-spine2 | Interface State | Ethernet Interface & Line Protocol == 'up' | Ethernet1 - P2P_LINK_TO_DC2-LEAF1A_Ethernet2 | NOT RUN | - |
| 811 | dc2-spine2 | Interface State | Ethernet Interface & Line Protocol == 'up' | Ethernet2 - P2P_LINK_TO_DC2-LEAF1B_Ethernet2 | NOT RUN | - |
| 812 | dc2-spine2 | Interface State | Ethernet Interface & Line Protocol == 'up' | Ethernet3 - P2P_LINK_TO_DC2-LEAF2A_Ethernet2 | NOT RUN | - |
| 813 | dc2-spine2 | Interface State | Ethernet Interface & Line Protocol == 'up' | Ethernet4 - P2P_LINK_TO_DC2-LEAF2B_Ethernet2 | NOT RUN | - |
| 814 | dc2-spine2 | Interface State | Ethernet Interface & Line Protocol == 'up' | Ethernet5 - P2P_LINK_TO_DC2-LEAF3A.ARISTA.COM_Ethernet2 | NOT RUN | - |
| 815 | dc2-spine2 | Interface State | Ethernet Interface & Line Protocol == 'up' | Ethernet6 - P2P_LINK_TO_DC2-LEAF3B.ARISTA.COM_Ethernet2 | NOT RUN | - |
| 816 | dc2-spine2 | Interface State | Loopback Interface Status & Line Protocol == 'up' | Loopback0 - EVPN_Overlay_Peering | NOT RUN | - |
| 817 | dc2-spine2 | IP Reachability | ip reachability test p2p links | Source: dc2-spine2_Ethernet1 - Destination: dc2-leaf1a_Ethernet2 | NOT RUN | - |
| 818 | dc2-spine2 | IP Reachability | ip reachability test p2p links | Source: dc2-spine2_Ethernet2 - Destination: dc2-leaf1b_Ethernet2 | NOT RUN | - |
| 819 | dc2-spine2 | IP Reachability | ip reachability test p2p links | Source: dc2-spine2_Ethernet3 - Destination: dc2-leaf2a_Ethernet2 | NOT RUN | - |
| 820 | dc2-spine2 | IP Reachability | ip reachability test p2p links | Source: dc2-spine2_Ethernet4 - Destination: dc2-leaf2b_Ethernet2 | NOT RUN | - |
| 821 | dc2-spine2 | IP Reachability | ip reachability test p2p links | Source: dc2-spine2_Ethernet5 - Destination: dc2-leaf3a.arista.com_Ethernet2 | NOT RUN | - |
| 822 | dc2-spine2 | IP Reachability | ip reachability test p2p links | Source: dc2-spine2_Ethernet6 - Destination: dc2-leaf3b.arista.com_Ethernet2 | NOT RUN | - |
| 823 | dc2-spine2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet1 - remote: dc2-leaf1a_Ethernet2 | NOT RUN | - |
| 824 | dc2-spine2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet2 - remote: dc2-leaf1b_Ethernet2 | NOT RUN | - |
| 825 | dc2-spine2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet3 - remote: dc2-leaf2a_Ethernet2 | NOT RUN | - |
| 826 | dc2-spine2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet4 - remote: dc2-leaf2b_Ethernet2 | NOT RUN | - |
| 827 | dc2-spine2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet5 - remote: dc2-leaf3a.arista.com_Ethernet2 | NOT RUN | - |
| 828 | dc2-spine2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet6 - remote: dc2-leaf3b.arista.com_Ethernet2 | NOT RUN | - |
| 829 | dc2-spine2 | NTP | Synchronised with NTP server | NTP | NOT RUN | - |
| 830 | dc2-spine2 | Security | Verifies if eAPI HTTPS server SSL profile is configured and valid. | VerifyAPIHttpsSSL | NOT RUN | - |
