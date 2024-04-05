
<!--
  ~ Copyright (c) 2024 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# Validate State Report

**Table of Contents:**

- [Validate State Report](validate-state-report)
  - [Test Results Summary](#test-results-summary)
  - [Failed Test Results Summary](#failed-test-results-summary)
  - [All Test Results](#all-test-results)

## Test Results Summary

### Summary Totals

| Total Tests | Total Tests Passed | Total Tests Failed |
| ----------- | ------------------ | ------------------ |
| 341 | 341 | 0 |

### Summary Totals Devices Under Tests

| DUT | Total Tests | Tests Passed | Tests Failed | Categories Failed |
| --- | ----------- | ------------ | ------------ | ----------------- |
| leaf1 |  51 | 51 | 0 | - |
| leaf2 |  51 | 51 | 0 | - |
| leaf3 |  51 | 51 | 0 | - |
| leaf4 |  50 | 50 | 0 | - |
| spine1 |  23 | 23 | 0 | - |
| spine2 |  23 | 23 | 0 | - |
| spine3 |  23 | 23 | 0 | - |
| spine4 |  23 | 23 | 0 | - |
| superspine1 |  23 | 23 | 0 | - |
| superspine2 |  23 | 23 | 0 | - |

### Summary Totals Per Category

| Test Category | Total Tests | Tests Passed | Tests Failed |
| ------------- | ----------- | ------------ | ------------ |
| NTP |  10 | 10 | 0 |
| Interface State |  89 | 89 | 0 |
| LLDP Topology |  40 | 40 | 0 |
| MLAG |  4 | 4 | 0 |
| IP Reachability |  32 | 32 | 0 |
| BGP |  78 | 78 | 0 |
| Routing Table |  48 | 48 | 0 |
| Loopback0 Reachability |  40 | 40 | 0 |

## Failed Test Results Summary

| Test ID | Node | Test Category | Test Description | Test | Test Result | Failure Reason |
| ------- | ---- | ------------- | ---------------- | ---- | ----------- | -------------- |

## All Test Results

| Test ID | Node | Test Category | Test Description | Test | Test Result | Failure Reason |
| ------- | ---- | ------------- | ---------------- | ---- | ----------- | -------------- |
| 1 | leaf1 | NTP | Synchronised with NTP server | NTP | PASS | - |
| 2 | leaf2 | NTP | Synchronised with NTP server | NTP | PASS | - |
| 3 | leaf3 | NTP | Synchronised with NTP server | NTP | PASS | - |
| 4 | leaf4 | NTP | Synchronised with NTP server | NTP | PASS | - |
| 5 | spine1 | NTP | Synchronised with NTP server | NTP | PASS | - |
| 6 | spine2 | NTP | Synchronised with NTP server | NTP | PASS | - |
| 7 | spine3 | NTP | Synchronised with NTP server | NTP | PASS | - |
| 8 | spine4 | NTP | Synchronised with NTP server | NTP | PASS | - |
| 9 | superspine1 | NTP | Synchronised with NTP server | NTP | PASS | - |
| 10 | superspine2 | NTP | Synchronised with NTP server | NTP | PASS | - |
| 11 | leaf1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet1 - MLAG_PEER_leaf2_Ethernet1 | PASS | - |
| 12 | leaf1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet2 - MLAG_PEER_leaf2_Ethernet2 | PASS | - |
| 13 | leaf1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet3 - P2P_LINK_TO_SPINE1_Ethernet3 | PASS | - |
| 14 | leaf1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet4 - P2P_LINK_TO_SPINE2_Ethernet3 | PASS | - |
| 15 | leaf1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet7 - host1 | PASS | - |
| 16 | leaf2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet1 - MLAG_PEER_leaf1_Ethernet1 | PASS | - |
| 17 | leaf2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet2 - MLAG_PEER_leaf1_Ethernet2 | PASS | - |
| 18 | leaf2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet3 - P2P_LINK_TO_SPINE1_Ethernet4 | PASS | - |
| 19 | leaf2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet4 - P2P_LINK_TO_SPINE2_Ethernet4 | PASS | - |
| 20 | leaf2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet7 - host1 | PASS | - |
| 21 | leaf3 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet1 - MLAG_PEER_leaf4_Ethernet1 | PASS | - |
| 22 | leaf3 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet2 - MLAG_PEER_leaf4_Ethernet2 | PASS | - |
| 23 | leaf3 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet5 - P2P_LINK_TO_SPINE3_Ethernet5 | PASS | - |
| 24 | leaf3 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet6 - P2P_LINK_TO_SPINE4_Ethernet5 | PASS | - |
| 25 | leaf3 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet7 - host2 | PASS | - |
| 26 | leaf4 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet1 - MLAG_PEER_leaf3_Ethernet1 | PASS | - |
| 27 | leaf4 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet2 - MLAG_PEER_leaf3_Ethernet2 | PASS | - |
| 28 | leaf4 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet5 - P2P_LINK_TO_SPINE3_Ethernet6 | PASS | - |
| 29 | leaf4 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet6 - P2P_LINK_TO_SPINE4_Ethernet6 | PASS | - |
| 30 | leaf4 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet9 -  | PASS | - |
| 31 | spine1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet3 - P2P_LINK_TO_LEAF1_Ethernet3 | PASS | - |
| 32 | spine1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet4 - P2P_LINK_TO_LEAF2_Ethernet3 | PASS | - |
| 33 | spine1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet7 - P2P_LINK_TO_SUPERSPINE1_Ethernet3 | PASS | - |
| 34 | spine1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet8 - P2P_LINK_TO_SUPERSPINE2_Ethernet3 | PASS | - |
| 35 | spine2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet3 - P2P_LINK_TO_LEAF1_Ethernet4 | PASS | - |
| 36 | spine2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet4 - P2P_LINK_TO_LEAF2_Ethernet4 | PASS | - |
| 37 | spine2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet7 - P2P_LINK_TO_SUPERSPINE1_Ethernet4 | PASS | - |
| 38 | spine2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet8 - P2P_LINK_TO_SUPERSPINE2_Ethernet4 | PASS | - |
| 39 | spine3 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet5 - P2P_LINK_TO_LEAF3_Ethernet5 | PASS | - |
| 40 | spine3 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet6 - P2P_LINK_TO_LEAF4_Ethernet5 | PASS | - |
| 41 | spine3 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet7 - P2P_LINK_TO_SUPERSPINE1_Ethernet5 | PASS | - |
| 42 | spine3 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet8 - P2P_LINK_TO_SUPERSPINE2_Ethernet5 | PASS | - |
| 43 | spine4 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet5 - P2P_LINK_TO_LEAF3_Ethernet6 | PASS | - |
| 44 | spine4 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet6 - P2P_LINK_TO_LEAF4_Ethernet6 | PASS | - |
| 45 | spine4 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet7 - P2P_LINK_TO_SUPERSPINE1_Ethernet6 | PASS | - |
| 46 | spine4 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet8 - P2P_LINK_TO_SUPERSPINE2_Ethernet6 | PASS | - |
| 47 | superspine1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet3 - P2P_LINK_TO_SPINE1_Ethernet7 | PASS | - |
| 48 | superspine1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet4 - P2P_LINK_TO_SPINE2_Ethernet7 | PASS | - |
| 49 | superspine1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet5 - P2P_LINK_TO_SPINE3_Ethernet7 | PASS | - |
| 50 | superspine1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet6 - P2P_LINK_TO_SPINE4_Ethernet7 | PASS | - |
| 51 | superspine2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet3 - P2P_LINK_TO_SPINE1_Ethernet8 | PASS | - |
| 52 | superspine2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet4 - P2P_LINK_TO_SPINE2_Ethernet8 | PASS | - |
| 53 | superspine2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet5 - P2P_LINK_TO_SPINE3_Ethernet8 | PASS | - |
| 54 | superspine2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet6 - P2P_LINK_TO_SPINE4_Ethernet8 | PASS | - |
| 55 | leaf1 | Interface State | Port-Channel Interface & Line Protocol == "up" | Port-Channel1 - MLAG_PEER_leaf2_Po1 | PASS | - |
| 56 | leaf1 | Interface State | Port-Channel Interface & Line Protocol == "up" | Port-Channel7 - host1_PortChannel host1 | PASS | - |
| 57 | leaf2 | Interface State | Port-Channel Interface & Line Protocol == "up" | Port-Channel1 - MLAG_PEER_leaf1_Po1 | PASS | - |
| 58 | leaf2 | Interface State | Port-Channel Interface & Line Protocol == "up" | Port-Channel7 - host1_PortChannel host1 | PASS | - |
| 59 | leaf3 | Interface State | Port-Channel Interface & Line Protocol == "up" | Port-Channel1 - MLAG_PEER_leaf4_Po1 | PASS | - |
| 60 | leaf3 | Interface State | Port-Channel Interface & Line Protocol == "up" | Port-Channel7 - host2_PortChannel host2 | PASS | - |
| 61 | leaf4 | Interface State | Port-Channel Interface & Line Protocol == "up" | Port-Channel1 - MLAG_PEER_leaf3_Po1 | PASS | - |
| 62 | leaf1 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan4093 - MLAG_PEER_L3_PEERING | PASS | - |
| 63 | leaf1 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan4094 - MLAG_PEER | PASS | - |
| 64 | leaf1 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan10 - DMZ | PASS | - |
| 65 | leaf1 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan20 - Internal | PASS | - |
| 66 | leaf1 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan3009 - MLAG_PEER_L3_iBGP: vrf VRF_A | PASS | - |
| 67 | leaf2 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan4093 - MLAG_PEER_L3_PEERING | PASS | - |
| 68 | leaf2 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan4094 - MLAG_PEER | PASS | - |
| 69 | leaf2 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan10 - DMZ | PASS | - |
| 70 | leaf2 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan20 - Internal | PASS | - |
| 71 | leaf2 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan3009 - MLAG_PEER_L3_iBGP: vrf VRF_A | PASS | - |
| 72 | leaf3 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan4093 - MLAG_PEER_L3_PEERING | PASS | - |
| 73 | leaf3 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan4094 - MLAG_PEER | PASS | - |
| 74 | leaf3 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan10 - DMZ | PASS | - |
| 75 | leaf3 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan20 - Internal | PASS | - |
| 76 | leaf3 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan3009 - MLAG_PEER_L3_iBGP: vrf VRF_A | PASS | - |
| 77 | leaf4 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan4093 - MLAG_PEER_L3_PEERING | PASS | - |
| 78 | leaf4 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan4094 - MLAG_PEER | PASS | - |
| 79 | leaf4 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan10 - DMZ | PASS | - |
| 80 | leaf4 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan20 - Internal | PASS | - |
| 81 | leaf4 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan3009 - MLAG_PEER_L3_iBGP: vrf VRF_A | PASS | - |
| 82 | leaf1 | Interface State | Vxlan Interface Status & Line Protocol == "up" | Vxlan1 | PASS | - |
| 83 | leaf2 | Interface State | Vxlan Interface Status & Line Protocol == "up" | Vxlan1 | PASS | - |
| 84 | leaf3 | Interface State | Vxlan Interface Status & Line Protocol == "up" | Vxlan1 | PASS | - |
| 85 | leaf4 | Interface State | Vxlan Interface Status & Line Protocol == "up" | Vxlan1 | PASS | - |
| 86 | leaf1 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback0 - EVPN_Overlay_Peering | PASS | - |
| 87 | leaf1 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback1 - VTEP_VXLAN_Tunnel_Source | PASS | - |
| 88 | leaf2 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback0 - EVPN_Overlay_Peering | PASS | - |
| 89 | leaf2 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback1 - VTEP_VXLAN_Tunnel_Source | PASS | - |
| 90 | leaf3 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback0 - EVPN_Overlay_Peering | PASS | - |
| 91 | leaf3 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback1 - VTEP_VXLAN_Tunnel_Source | PASS | - |
| 92 | leaf4 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback0 - EVPN_Overlay_Peering | PASS | - |
| 93 | leaf4 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback1 - VTEP_VXLAN_Tunnel_Source | PASS | - |
| 94 | spine1 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback0 - EVPN_Overlay_Peering | PASS | - |
| 95 | spine2 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback0 - EVPN_Overlay_Peering | PASS | - |
| 96 | spine3 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback0 - EVPN_Overlay_Peering | PASS | - |
| 97 | spine4 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback0 - EVPN_Overlay_Peering | PASS | - |
| 98 | superspine1 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback0 - EVPN_Overlay_Peering | PASS | - |
| 99 | superspine2 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback0 - EVPN_Overlay_Peering | PASS | - |
| 100 | leaf1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet1 - remote: leaf2_Ethernet1 | PASS | - |
| 101 | leaf1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet2 - remote: leaf2_Ethernet2 | PASS | - |
| 102 | leaf1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet3 - remote: spine1_Ethernet3 | PASS | - |
| 103 | leaf1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet4 - remote: spine2_Ethernet3 | PASS | - |
| 104 | leaf2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet1 - remote: leaf1_Ethernet1 | PASS | - |
| 105 | leaf2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet2 - remote: leaf1_Ethernet2 | PASS | - |
| 106 | leaf2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet3 - remote: spine1_Ethernet4 | PASS | - |
| 107 | leaf2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet4 - remote: spine2_Ethernet4 | PASS | - |
| 108 | leaf3 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet1 - remote: leaf4_Ethernet1 | PASS | - |
| 109 | leaf3 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet2 - remote: leaf4_Ethernet2 | PASS | - |
| 110 | leaf3 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet5 - remote: spine3_Ethernet5 | PASS | - |
| 111 | leaf3 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet6 - remote: spine4_Ethernet5 | PASS | - |
| 112 | leaf4 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet1 - remote: leaf3_Ethernet1 | PASS | - |
| 113 | leaf4 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet2 - remote: leaf3_Ethernet2 | PASS | - |
| 114 | leaf4 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet5 - remote: spine3_Ethernet6 | PASS | - |
| 115 | leaf4 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet6 - remote: spine4_Ethernet6 | PASS | - |
| 116 | spine1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet3 - remote: leaf1_Ethernet3 | PASS | - |
| 117 | spine1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet4 - remote: leaf2_Ethernet3 | PASS | - |
| 118 | spine1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet7 - remote: superspine1_Ethernet3 | PASS | - |
| 119 | spine1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet8 - remote: superspine2_Ethernet3 | PASS | - |
| 120 | spine2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet3 - remote: leaf1_Ethernet4 | PASS | - |
| 121 | spine2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet4 - remote: leaf2_Ethernet4 | PASS | - |
| 122 | spine2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet7 - remote: superspine1_Ethernet4 | PASS | - |
| 123 | spine2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet8 - remote: superspine2_Ethernet4 | PASS | - |
| 124 | spine3 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet5 - remote: leaf3_Ethernet5 | PASS | - |
| 125 | spine3 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet6 - remote: leaf4_Ethernet5 | PASS | - |
| 126 | spine3 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet7 - remote: superspine1_Ethernet5 | PASS | - |
| 127 | spine3 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet8 - remote: superspine2_Ethernet5 | PASS | - |
| 128 | spine4 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet5 - remote: leaf3_Ethernet6 | PASS | - |
| 129 | spine4 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet6 - remote: leaf4_Ethernet6 | PASS | - |
| 130 | spine4 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet7 - remote: superspine1_Ethernet6 | PASS | - |
| 131 | spine4 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet8 - remote: superspine2_Ethernet6 | PASS | - |
| 132 | superspine1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet3 - remote: spine1_Ethernet7 | PASS | - |
| 133 | superspine1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet4 - remote: spine2_Ethernet7 | PASS | - |
| 134 | superspine1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet5 - remote: spine3_Ethernet7 | PASS | - |
| 135 | superspine1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet6 - remote: spine4_Ethernet7 | PASS | - |
| 136 | superspine2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet3 - remote: spine1_Ethernet8 | PASS | - |
| 137 | superspine2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet4 - remote: spine2_Ethernet8 | PASS | - |
| 138 | superspine2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet5 - remote: spine3_Ethernet8 | PASS | - |
| 139 | superspine2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet6 - remote: spine4_Ethernet8 | PASS | - |
| 140 | leaf1 | MLAG | MLAG State active & Status connected | MLAG | PASS | - |
| 141 | leaf2 | MLAG | MLAG State active & Status connected | MLAG | PASS | - |
| 142 | leaf3 | MLAG | MLAG State active & Status connected | MLAG | PASS | - |
| 143 | leaf4 | MLAG | MLAG State active & Status connected | MLAG | PASS | - |
| 144 | leaf1 | IP Reachability | ip reachability test p2p links | Source: leaf1_Ethernet3 - Destination: spine1_Ethernet3 | PASS | - |
| 145 | leaf1 | IP Reachability | ip reachability test p2p links | Source: leaf1_Ethernet4 - Destination: spine2_Ethernet3 | PASS | - |
| 146 | leaf2 | IP Reachability | ip reachability test p2p links | Source: leaf2_Ethernet3 - Destination: spine1_Ethernet4 | PASS | - |
| 147 | leaf2 | IP Reachability | ip reachability test p2p links | Source: leaf2_Ethernet4 - Destination: spine2_Ethernet4 | PASS | - |
| 148 | leaf3 | IP Reachability | ip reachability test p2p links | Source: leaf3_Ethernet5 - Destination: spine3_Ethernet5 | PASS | - |
| 149 | leaf3 | IP Reachability | ip reachability test p2p links | Source: leaf3_Ethernet6 - Destination: spine4_Ethernet5 | PASS | - |
| 150 | leaf4 | IP Reachability | ip reachability test p2p links | Source: leaf4_Ethernet5 - Destination: spine3_Ethernet6 | PASS | - |
| 151 | leaf4 | IP Reachability | ip reachability test p2p links | Source: leaf4_Ethernet6 - Destination: spine4_Ethernet6 | PASS | - |
| 152 | spine1 | IP Reachability | ip reachability test p2p links | Source: spine1_Ethernet3 - Destination: leaf1_Ethernet3 | PASS | - |
| 153 | spine1 | IP Reachability | ip reachability test p2p links | Source: spine1_Ethernet4 - Destination: leaf2_Ethernet3 | PASS | - |
| 154 | spine1 | IP Reachability | ip reachability test p2p links | Source: spine1_Ethernet7 - Destination: superspine1_Ethernet3 | PASS | - |
| 155 | spine1 | IP Reachability | ip reachability test p2p links | Source: spine1_Ethernet8 - Destination: superspine2_Ethernet3 | PASS | - |
| 156 | spine2 | IP Reachability | ip reachability test p2p links | Source: spine2_Ethernet3 - Destination: leaf1_Ethernet4 | PASS | - |
| 157 | spine2 | IP Reachability | ip reachability test p2p links | Source: spine2_Ethernet4 - Destination: leaf2_Ethernet4 | PASS | - |
| 158 | spine2 | IP Reachability | ip reachability test p2p links | Source: spine2_Ethernet7 - Destination: superspine1_Ethernet4 | PASS | - |
| 159 | spine2 | IP Reachability | ip reachability test p2p links | Source: spine2_Ethernet8 - Destination: superspine2_Ethernet4 | PASS | - |
| 160 | spine3 | IP Reachability | ip reachability test p2p links | Source: spine3_Ethernet5 - Destination: leaf3_Ethernet5 | PASS | - |
| 161 | spine3 | IP Reachability | ip reachability test p2p links | Source: spine3_Ethernet6 - Destination: leaf4_Ethernet5 | PASS | - |
| 162 | spine3 | IP Reachability | ip reachability test p2p links | Source: spine3_Ethernet7 - Destination: superspine1_Ethernet5 | PASS | - |
| 163 | spine3 | IP Reachability | ip reachability test p2p links | Source: spine3_Ethernet8 - Destination: superspine2_Ethernet5 | PASS | - |
| 164 | spine4 | IP Reachability | ip reachability test p2p links | Source: spine4_Ethernet5 - Destination: leaf3_Ethernet6 | PASS | - |
| 165 | spine4 | IP Reachability | ip reachability test p2p links | Source: spine4_Ethernet6 - Destination: leaf4_Ethernet6 | PASS | - |
| 166 | spine4 | IP Reachability | ip reachability test p2p links | Source: spine4_Ethernet7 - Destination: superspine1_Ethernet6 | PASS | - |
| 167 | spine4 | IP Reachability | ip reachability test p2p links | Source: spine4_Ethernet8 - Destination: superspine2_Ethernet6 | PASS | - |
| 168 | superspine1 | IP Reachability | ip reachability test p2p links | Source: superspine1_Ethernet3 - Destination: spine1_Ethernet7 | PASS | - |
| 169 | superspine1 | IP Reachability | ip reachability test p2p links | Source: superspine1_Ethernet4 - Destination: spine2_Ethernet7 | PASS | - |
| 170 | superspine1 | IP Reachability | ip reachability test p2p links | Source: superspine1_Ethernet5 - Destination: spine3_Ethernet7 | PASS | - |
| 171 | superspine1 | IP Reachability | ip reachability test p2p links | Source: superspine1_Ethernet6 - Destination: spine4_Ethernet7 | PASS | - |
| 172 | superspine2 | IP Reachability | ip reachability test p2p links | Source: superspine2_Ethernet3 - Destination: spine1_Ethernet8 | PASS | - |
| 173 | superspine2 | IP Reachability | ip reachability test p2p links | Source: superspine2_Ethernet4 - Destination: spine2_Ethernet8 | PASS | - |
| 174 | superspine2 | IP Reachability | ip reachability test p2p links | Source: superspine2_Ethernet5 - Destination: spine3_Ethernet8 | PASS | - |
| 175 | superspine2 | IP Reachability | ip reachability test p2p links | Source: superspine2_Ethernet6 - Destination: spine4_Ethernet8 | PASS | - |
| 176 | leaf1 | BGP | ArBGP is configured and operating | ArBGP | PASS | - |
| 177 | leaf2 | BGP | ArBGP is configured and operating | ArBGP | PASS | - |
| 178 | leaf3 | BGP | ArBGP is configured and operating | ArBGP | PASS | - |
| 179 | leaf4 | BGP | ArBGP is configured and operating | ArBGP | PASS | - |
| 180 | spine1 | BGP | ArBGP is configured and operating | ArBGP | PASS | - |
| 181 | spine2 | BGP | ArBGP is configured and operating | ArBGP | PASS | - |
| 182 | spine3 | BGP | ArBGP is configured and operating | ArBGP | PASS | - |
| 183 | spine4 | BGP | ArBGP is configured and operating | ArBGP | PASS | - |
| 184 | superspine1 | BGP | ArBGP is configured and operating | ArBGP | PASS | - |
| 185 | superspine2 | BGP | ArBGP is configured and operating | ArBGP | PASS | - |
| 186 | leaf1 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.255.251.1 | PASS | - |
| 187 | leaf1 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 192.168.103.0 | PASS | - |
| 188 | leaf1 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 192.168.103.2 | PASS | - |
| 189 | leaf2 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.255.251.0 | PASS | - |
| 190 | leaf2 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 192.168.103.4 | PASS | - |
| 191 | leaf2 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 192.168.103.6 | PASS | - |
| 192 | leaf3 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.255.251.5 | PASS | - |
| 193 | leaf3 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 192.168.103.8 | PASS | - |
| 194 | leaf3 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 192.168.103.10 | PASS | - |
| 195 | leaf4 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.255.251.4 | PASS | - |
| 196 | leaf4 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 192.168.103.12 | PASS | - |
| 197 | leaf4 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 192.168.103.14 | PASS | - |
| 198 | spine1 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 192.168.103.1 | PASS | - |
| 199 | spine1 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 192.168.103.5 | PASS | - |
| 200 | spine1 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 192.168.103.40 | PASS | - |
| 201 | spine1 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 192.168.103.42 | PASS | - |
| 202 | spine2 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 192.168.103.3 | PASS | - |
| 203 | spine2 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 192.168.103.7 | PASS | - |
| 204 | spine2 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 192.168.103.44 | PASS | - |
| 205 | spine2 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 192.168.103.46 | PASS | - |
| 206 | spine3 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 192.168.103.9 | PASS | - |
| 207 | spine3 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 192.168.103.13 | PASS | - |
| 208 | spine3 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 192.168.103.48 | PASS | - |
| 209 | spine3 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 192.168.103.50 | PASS | - |
| 210 | spine4 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 192.168.103.11 | PASS | - |
| 211 | spine4 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 192.168.103.15 | PASS | - |
| 212 | spine4 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 192.168.103.52 | PASS | - |
| 213 | spine4 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 192.168.103.54 | PASS | - |
| 214 | superspine1 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 192.168.103.41 | PASS | - |
| 215 | superspine1 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 192.168.103.45 | PASS | - |
| 216 | superspine1 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 192.168.103.49 | PASS | - |
| 217 | superspine1 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 192.168.103.53 | PASS | - |
| 218 | superspine2 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 192.168.103.43 | PASS | - |
| 219 | superspine2 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 192.168.103.47 | PASS | - |
| 220 | superspine2 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 192.168.103.51 | PASS | - |
| 221 | superspine2 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 192.168.103.55 | PASS | - |
| 222 | leaf1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.11 | PASS | - |
| 223 | leaf1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.12 | PASS | - |
| 224 | leaf2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.11 | PASS | - |
| 225 | leaf2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.12 | PASS | - |
| 226 | leaf3 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.13 | PASS | - |
| 227 | leaf3 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.14 | PASS | - |
| 228 | leaf4 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.13 | PASS | - |
| 229 | leaf4 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.14 | PASS | - |
| 230 | spine1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.201 | PASS | - |
| 231 | spine1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.202 | PASS | - |
| 232 | spine1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.1 | PASS | - |
| 233 | spine1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.2 | PASS | - |
| 234 | spine2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.201 | PASS | - |
| 235 | spine2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.202 | PASS | - |
| 236 | spine2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.1 | PASS | - |
| 237 | spine2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.2 | PASS | - |
| 238 | spine3 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.201 | PASS | - |
| 239 | spine3 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.202 | PASS | - |
| 240 | spine3 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.3 | PASS | - |
| 241 | spine3 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.4 | PASS | - |
| 242 | spine4 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.201 | PASS | - |
| 243 | spine4 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.202 | PASS | - |
| 244 | spine4 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.3 | PASS | - |
| 245 | spine4 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.4 | PASS | - |
| 246 | superspine1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.11 | PASS | - |
| 247 | superspine1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.12 | PASS | - |
| 248 | superspine1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.13 | PASS | - |
| 249 | superspine1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.14 | PASS | - |
| 250 | superspine2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.11 | PASS | - |
| 251 | superspine2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.12 | PASS | - |
| 252 | superspine2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.13 | PASS | - |
| 253 | superspine2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.14 | PASS | - |
| 254 | leaf1 | Routing Table | Remote VTEP address | 192.168.102.1 | PASS | - |
| 255 | leaf1 | Routing Table | Remote VTEP address | 192.168.102.3 | PASS | - |
| 256 | leaf2 | Routing Table | Remote VTEP address | 192.168.102.1 | PASS | - |
| 257 | leaf2 | Routing Table | Remote VTEP address | 192.168.102.3 | PASS | - |
| 258 | leaf3 | Routing Table | Remote VTEP address | 192.168.102.1 | PASS | - |
| 259 | leaf3 | Routing Table | Remote VTEP address | 192.168.102.3 | PASS | - |
| 260 | leaf4 | Routing Table | Remote VTEP address | 192.168.102.1 | PASS | - |
| 261 | leaf4 | Routing Table | Remote VTEP address | 192.168.102.3 | PASS | - |
| 262 | leaf1 | Routing Table | Remote Lo0 address | 192.168.101.1 | PASS | - |
| 263 | leaf1 | Routing Table | Remote Lo0 address | 192.168.101.2 | PASS | - |
| 264 | leaf1 | Routing Table | Remote Lo0 address | 192.168.101.3 | PASS | - |
| 265 | leaf1 | Routing Table | Remote Lo0 address | 192.168.101.4 | PASS | - |
| 266 | leaf1 | Routing Table | Remote Lo0 address | 192.168.101.11 | PASS | - |
| 267 | leaf1 | Routing Table | Remote Lo0 address | 192.168.101.12 | PASS | - |
| 268 | leaf1 | Routing Table | Remote Lo0 address | 192.168.101.13 | PASS | - |
| 269 | leaf1 | Routing Table | Remote Lo0 address | 192.168.101.14 | PASS | - |
| 270 | leaf1 | Routing Table | Remote Lo0 address | 192.168.101.201 | PASS | - |
| 271 | leaf1 | Routing Table | Remote Lo0 address | 192.168.101.202 | PASS | - |
| 272 | leaf2 | Routing Table | Remote Lo0 address | 192.168.101.1 | PASS | - |
| 273 | leaf2 | Routing Table | Remote Lo0 address | 192.168.101.2 | PASS | - |
| 274 | leaf2 | Routing Table | Remote Lo0 address | 192.168.101.3 | PASS | - |
| 275 | leaf2 | Routing Table | Remote Lo0 address | 192.168.101.4 | PASS | - |
| 276 | leaf2 | Routing Table | Remote Lo0 address | 192.168.101.11 | PASS | - |
| 277 | leaf2 | Routing Table | Remote Lo0 address | 192.168.101.12 | PASS | - |
| 278 | leaf2 | Routing Table | Remote Lo0 address | 192.168.101.13 | PASS | - |
| 279 | leaf2 | Routing Table | Remote Lo0 address | 192.168.101.14 | PASS | - |
| 280 | leaf2 | Routing Table | Remote Lo0 address | 192.168.101.201 | PASS | - |
| 281 | leaf2 | Routing Table | Remote Lo0 address | 192.168.101.202 | PASS | - |
| 282 | leaf3 | Routing Table | Remote Lo0 address | 192.168.101.1 | PASS | - |
| 283 | leaf3 | Routing Table | Remote Lo0 address | 192.168.101.2 | PASS | - |
| 284 | leaf3 | Routing Table | Remote Lo0 address | 192.168.101.3 | PASS | - |
| 285 | leaf3 | Routing Table | Remote Lo0 address | 192.168.101.4 | PASS | - |
| 286 | leaf3 | Routing Table | Remote Lo0 address | 192.168.101.11 | PASS | - |
| 287 | leaf3 | Routing Table | Remote Lo0 address | 192.168.101.12 | PASS | - |
| 288 | leaf3 | Routing Table | Remote Lo0 address | 192.168.101.13 | PASS | - |
| 289 | leaf3 | Routing Table | Remote Lo0 address | 192.168.101.14 | PASS | - |
| 290 | leaf3 | Routing Table | Remote Lo0 address | 192.168.101.201 | PASS | - |
| 291 | leaf3 | Routing Table | Remote Lo0 address | 192.168.101.202 | PASS | - |
| 292 | leaf4 | Routing Table | Remote Lo0 address | 192.168.101.1 | PASS | - |
| 293 | leaf4 | Routing Table | Remote Lo0 address | 192.168.101.2 | PASS | - |
| 294 | leaf4 | Routing Table | Remote Lo0 address | 192.168.101.3 | PASS | - |
| 295 | leaf4 | Routing Table | Remote Lo0 address | 192.168.101.4 | PASS | - |
| 296 | leaf4 | Routing Table | Remote Lo0 address | 192.168.101.11 | PASS | - |
| 297 | leaf4 | Routing Table | Remote Lo0 address | 192.168.101.12 | PASS | - |
| 298 | leaf4 | Routing Table | Remote Lo0 address | 192.168.101.13 | PASS | - |
| 299 | leaf4 | Routing Table | Remote Lo0 address | 192.168.101.14 | PASS | - |
| 300 | leaf4 | Routing Table | Remote Lo0 address | 192.168.101.201 | PASS | - |
| 301 | leaf4 | Routing Table | Remote Lo0 address | 192.168.101.202 | PASS | - |
| 302 | leaf1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf1 - 192.168.101.1 Destination: 192.168.101.1 | PASS | - |
| 303 | leaf1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf1 - 192.168.101.1 Destination: 192.168.101.2 | PASS | - |
| 304 | leaf1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf1 - 192.168.101.1 Destination: 192.168.101.3 | PASS | - |
| 305 | leaf1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf1 - 192.168.101.1 Destination: 192.168.101.4 | PASS | - |
| 306 | leaf1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf1 - 192.168.101.1 Destination: 192.168.101.11 | PASS | - |
| 307 | leaf1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf1 - 192.168.101.1 Destination: 192.168.101.12 | PASS | - |
| 308 | leaf1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf1 - 192.168.101.1 Destination: 192.168.101.13 | PASS | - |
| 309 | leaf1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf1 - 192.168.101.1 Destination: 192.168.101.14 | PASS | - |
| 310 | leaf1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf1 - 192.168.101.1 Destination: 192.168.101.201 | PASS | - |
| 311 | leaf1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf1 - 192.168.101.1 Destination: 192.168.101.202 | PASS | - |
| 312 | leaf2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf2 - 192.168.101.2 Destination: 192.168.101.1 | PASS | - |
| 313 | leaf2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf2 - 192.168.101.2 Destination: 192.168.101.2 | PASS | - |
| 314 | leaf2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf2 - 192.168.101.2 Destination: 192.168.101.3 | PASS | - |
| 315 | leaf2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf2 - 192.168.101.2 Destination: 192.168.101.4 | PASS | - |
| 316 | leaf2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf2 - 192.168.101.2 Destination: 192.168.101.11 | PASS | - |
| 317 | leaf2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf2 - 192.168.101.2 Destination: 192.168.101.12 | PASS | - |
| 318 | leaf2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf2 - 192.168.101.2 Destination: 192.168.101.13 | PASS | - |
| 319 | leaf2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf2 - 192.168.101.2 Destination: 192.168.101.14 | PASS | - |
| 320 | leaf2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf2 - 192.168.101.2 Destination: 192.168.101.201 | PASS | - |
| 321 | leaf2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf2 - 192.168.101.2 Destination: 192.168.101.202 | PASS | - |
| 322 | leaf3 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf3 - 192.168.101.3 Destination: 192.168.101.1 | PASS | - |
| 323 | leaf3 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf3 - 192.168.101.3 Destination: 192.168.101.2 | PASS | - |
| 324 | leaf3 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf3 - 192.168.101.3 Destination: 192.168.101.3 | PASS | - |
| 325 | leaf3 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf3 - 192.168.101.3 Destination: 192.168.101.4 | PASS | - |
| 326 | leaf3 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf3 - 192.168.101.3 Destination: 192.168.101.11 | PASS | - |
| 327 | leaf3 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf3 - 192.168.101.3 Destination: 192.168.101.12 | PASS | - |
| 328 | leaf3 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf3 - 192.168.101.3 Destination: 192.168.101.13 | PASS | - |
| 329 | leaf3 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf3 - 192.168.101.3 Destination: 192.168.101.14 | PASS | - |
| 330 | leaf3 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf3 - 192.168.101.3 Destination: 192.168.101.201 | PASS | - |
| 331 | leaf3 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf3 - 192.168.101.3 Destination: 192.168.101.202 | PASS | - |
| 332 | leaf4 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf4 - 192.168.101.4 Destination: 192.168.101.1 | PASS | - |
| 333 | leaf4 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf4 - 192.168.101.4 Destination: 192.168.101.2 | PASS | - |
| 334 | leaf4 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf4 - 192.168.101.4 Destination: 192.168.101.3 | PASS | - |
| 335 | leaf4 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf4 - 192.168.101.4 Destination: 192.168.101.4 | PASS | - |
| 336 | leaf4 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf4 - 192.168.101.4 Destination: 192.168.101.11 | PASS | - |
| 337 | leaf4 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf4 - 192.168.101.4 Destination: 192.168.101.12 | PASS | - |
| 338 | leaf4 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf4 - 192.168.101.4 Destination: 192.168.101.13 | PASS | - |
| 339 | leaf4 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf4 - 192.168.101.4 Destination: 192.168.101.14 | PASS | - |
| 340 | leaf4 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf4 - 192.168.101.4 Destination: 192.168.101.201 | PASS | - |
| 341 | leaf4 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf4 - 192.168.101.4 Destination: 192.168.101.202 | PASS | - |
