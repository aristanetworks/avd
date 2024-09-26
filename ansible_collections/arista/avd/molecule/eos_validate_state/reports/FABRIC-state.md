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
| 2666 | 0 | 0 | 0 |

### Summary Totals Device Under Test

| Device Under Test | Total Tests | Tests Passed | Tests Failed | Tests Skipped | Categories Failed | Categories Skipped |
| ------------------| ----------- | ------------ | ------------ | ------------- | ----------------- | ------------------ |
| dc1-leaf1a | 160 | 0 | 0 | 0 | - | - |
| dc1-leaf1b | 151 | 0 | 0 | 0 | - | - |
| dc1-leaf1c | 90 | 0 | 0 | 0 | - | - |
| dc1-leaf2a | 148 | 0 | 0 | 0 | - | - |
| dc1-leaf2c | 113 | 0 | 0 | 0 | - | - |
| dc1-spine1 | 116 | 0 | 0 | 0 | - | - |
| dc1-spine2 | 116 | 0 | 0 | 0 | - | - |
| dc1-svc-leaf1a | 129 | 0 | 0 | 0 | - | - |
| dc1-svc-leaf1b | 129 | 0 | 0 | 0 | - | - |
| dc1-wan1 | 96 | 0 | 0 | 0 | - | - |
| dc1-wan2 | 96 | 0 | 0 | 0 | - | - |
| dc2-leaf1a | 162 | 0 | 0 | 0 | - | - |
| dc2-leaf1b | 162 | 0 | 0 | 0 | - | - |
| dc2-leaf1c | 72 | 0 | 0 | 0 | - | - |
| dc2-leaf2a | 167 | 0 | 0 | 0 | - | - |
| dc2-leaf2b | 163 | 0 | 0 | 0 | - | - |
| dc2-leaf2c | 72 | 0 | 0 | 0 | - | - |
| dc2-leaf3a.arista.com | 169 | 0 | 0 | 0 | - | - |
| dc2-leaf3b.arista.com | 159 | 0 | 0 | 0 | - | - |
| dc2-spine1 | 98 | 0 | 0 | 0 | - | - |
| dc2-spine2 | 98 | 0 | 0 | 0 | - | - |

### Summary Totals Per Category

| Test Category | Total Tests | Tests Passed | Tests Failed | Tests Skipped |
| ------------- | ----------- | ------------ | ------------ | ------------- |
| AAA | 147 | 0 | 0 | 0 |
| BFD | 6 | 0 | 0 | 0 |
| BGP | 131 | 0 | 0 | 0 |
| Configuration | 42 | 0 | 0 | 0 |
| Connectivity | 369 | 0 | 0 | 0 |
| Field Notices | 42 | 0 | 0 | 0 |
| Greent | 42 | 0 | 0 | 0 |
| Hardware | 231 | 0 | 0 | 0 |
| Interfaces | 319 | 0 | 0 | 0 |
| LANZ | 21 | 0 | 0 | 0 |
| Logging | 48 | 0 | 0 | 0 |
| MLAG | 41 | 0 | 0 | 0 |
| Multicast | 12 | 0 | 0 | 0 |
| OSPF | 6 | 0 | 0 | 0 |
| PTP | 105 | 0 | 0 | 0 |
| Profiles | 4 | 0 | 0 | 0 |
| Routing | 297 | 0 | 0 | 0 |
| SNMP | 63 | 0 | 0 | 0 |
| STP | 30 | 0 | 0 | 0 |
| STUN | 25 | 0 | 0 | 0 |
| Security | 321 | 0 | 0 | 0 |
| Services | 84 | 0 | 0 | 0 |
| Software | 44 | 0 | 0 | 0 |
| System | 210 | 0 | 0 | 0 |
| VLAN | 21 | 0 | 0 | 0 |
| VXLAN | 5 | 0 | 0 | 0 |

## Failed Test Results Summary

| ID | Device Under Test | Categories | Test | Description | Inputs | Result | Messages |
| -- | ----------------- | ---------- | ---- | ----------- | ------ | -------| -------- |

## All Test Results

| ID | Device Under Test | Categories | Test | Description | Inputs | Result | Messages |
| -- | ----------------- | ---------- | ---- | ----------- | ------ | -------| -------- |
| 1 | dc1-leaf1a | AAA | VerifyAcctConsoleMethods | Verifies the AAA accounting console method lists for different accounting types (system, exec, commands, dot1x). | - | NOT RUN | - |
| 2 | dc1-leaf1a | AAA | VerifyAcctDefaultMethods | Verifies the AAA accounting default method lists for different accounting types (system, exec, commands, dot1x). | - | NOT RUN | - |
| 3 | dc1-leaf1a | AAA | VerifyAuthenMethods | Verifies the AAA authentication method lists for different authentication types (login, enable, dot1x). | - | NOT RUN | - |
| 4 | dc1-leaf1a | AAA | VerifyAuthzMethods | Verifies the AAA authorization method lists for different authorization types (commands, exec). | - | NOT RUN | - |
| 5 | dc1-leaf1a | AAA | VerifyTacacsServerGroups | Verifies if the provided TACACS server group(s) are configured. | - | NOT RUN | - |
| 6 | dc1-leaf1a | AAA | VerifyTacacsServers | Verifies TACACS servers are configured for a specified VRF. | - | NOT RUN | - |
| 7 | dc1-leaf1a | AAA | VerifyTacacsSourceIntf | Verifies TACACS source-interface for a specified VRF. | - | NOT RUN | - |
| 8 | dc1-leaf1a | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: 10.1.1.1 | NOT RUN | - |
| 9 | dc1-leaf1a | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: dc1-spine1 (IP: 10.255.0.1) | NOT RUN | - |
| 10 | dc1-leaf1a | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: dc1-spine2 (IP: 10.255.0.2) | NOT RUN | - |
| 11 | dc1-leaf1a | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: dc1-leaf1b (IP: 10.255.1.97) | NOT RUN | - |
| 12 | dc1-leaf1a | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: dc1-spine1 (IP: 10.255.255.0) | NOT RUN | - |
| 13 | dc1-leaf1a | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: dc1-spine2 (IP: 10.255.255.2) | NOT RUN | - |
| 14 | dc1-leaf1a | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: dc1-wan1 (IP: 10.255.255.1) | NOT RUN | - |
| 15 | dc1-leaf1a | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: dc1-wan2 (IP: 10.255.255.5) | NOT RUN | - |
| 16 | dc1-leaf1a | Configuration | VerifyRunningConfigDiffs | Verifies there is no difference between the running-config and the startup-config | - | NOT RUN | - |
| 17 | dc1-leaf1a | Configuration | VerifyZeroTouch | Verifies ZeroTouch is disabled | - | NOT RUN | - |
| 18 | dc1-leaf1a | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet1 - Remote: dc1-spine1 Ethernet1 | NOT RUN | - |
| 19 | dc1-leaf1a | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet2 - Remote: dc1-spine2 Ethernet1 | NOT RUN | - |
| 20 | dc1-leaf1a | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet3 - Remote: dc1-leaf1b Ethernet3 | NOT RUN | - |
| 21 | dc1-leaf1a | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet4 - Remote: dc1-leaf1b Ethernet4 | NOT RUN | - |
| 22 | dc1-leaf1a | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet6 - Remote: dc1-wan1 Ethernet1 | NOT RUN | - |
| 23 | dc1-leaf1a | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet7 - Remote: dc1-wan2 Ethernet1 | NOT RUN | - |
| 24 | dc1-leaf1a | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet8 - Remote: dc1-leaf1c Ethernet1 | NOT RUN | - |
| 25 | dc1-leaf1a | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.0.3) - Destination: dc1-leaf1a Loopback0 (IP: 10.255.0.3) | NOT RUN | - |
| 26 | dc1-leaf1a | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.0.3) - Destination: dc1-leaf1b Loopback0 (IP: 10.255.0.4) | NOT RUN | - |
| 27 | dc1-leaf1a | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.0.3) - Destination: dc1-leaf2a Loopback0 (IP: 10.255.0.5) | NOT RUN | - |
| 28 | dc1-leaf1a | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.0.3) - Destination: dc1-spine1 Loopback0 (IP: 10.255.0.1) | NOT RUN | - |
| 29 | dc1-leaf1a | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.0.3) - Destination: dc1-spine2 Loopback0 (IP: 10.255.0.2) | NOT RUN | - |
| 30 | dc1-leaf1a | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.0.3) - Destination: dc1-svc-leaf1a Loopback0 (IP: 10.33.0.5) | NOT RUN | - |
| 31 | dc1-leaf1a | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.0.3) - Destination: dc1-svc-leaf1b Loopback0 (IP: 10.33.0.6) | NOT RUN | - |
| 32 | dc1-leaf1a | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.0.3) - Destination: dc1-wan1 Loopback0 (IP: 10.255.2.1) | NOT RUN | - |
| 33 | dc1-leaf1a | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.0.3) - Destination: dc1-wan2 Loopback0 (IP: 10.255.2.2) | NOT RUN | - |
| 34 | dc1-leaf1a | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.0.3) - Destination: dc2-leaf1a Loopback0 (IP: 10.255.128.13) | NOT RUN | - |
| 35 | dc1-leaf1a | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.0.3) - Destination: dc2-leaf1b Loopback0 (IP: 10.255.128.14) | NOT RUN | - |
| 36 | dc1-leaf1a | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.0.3) - Destination: dc2-leaf2a Loopback0 (IP: 10.255.128.15) | NOT RUN | - |
| 37 | dc1-leaf1a | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.0.3) - Destination: dc2-leaf2b Loopback0 (IP: 10.255.128.16) | NOT RUN | - |
| 38 | dc1-leaf1a | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.0.3) - Destination: dc2-leaf3a.arista.com Loopback0 (IP: 10.255.128.17) | NOT RUN | - |
| 39 | dc1-leaf1a | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.0.3) - Destination: dc2-leaf3b.arista.com Loopback0 (IP: 10.255.128.18) | NOT RUN | - |
| 40 | dc1-leaf1a | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.0.3) - Destination: dc2-spine1 Loopback0 (IP: 10.255.128.11) | NOT RUN | - |
| 41 | dc1-leaf1a | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.0.3) - Destination: dc2-spine2 Loopback0 (IP: 10.255.128.12) | NOT RUN | - |
| 42 | dc1-leaf1a | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet1 (IP: 10.255.255.1) - Destination: dc1-spine1 Ethernet1 (IP: 10.255.255.0) | NOT RUN | - |
| 43 | dc1-leaf1a | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet2 (IP: 10.255.255.3) - Destination: dc1-spine2 Ethernet1 (IP: 10.255.255.2) | NOT RUN | - |
| 44 | dc1-leaf1a | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet6 (IP: 10.255.255.0) - Destination: dc1-wan1 Ethernet1 (IP: 10.255.255.1) | NOT RUN | - |
| 45 | dc1-leaf1a | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet7 (IP: 10.255.255.4) - Destination: dc1-wan2 Ethernet1 (IP: 10.255.255.5) | NOT RUN | - |
| 46 | dc1-leaf1a | Field Notices | VerifyFieldNotice44Resolution | Verifies that the device is using the correct Aboot version per FN0044. | - | NOT RUN | - |
| 47 | dc1-leaf1a | Field Notices | VerifyFieldNotice72Resolution | Verifies if the device is exposed to FN0072, and if the issue has been mitigated. | - | NOT RUN | - |
| 48 | dc1-leaf1a | Greent | VerifyGreenT | Verifies if a GreenT policy is created. | - | NOT RUN | - |
| 49 | dc1-leaf1a | Greent | VerifyGreenTCounters | Verifies if the GreenT counters are incremented. | - | NOT RUN | - |
| 50 | dc1-leaf1a | Hardware | VerifyAdverseDrops | Verifies there are no adverse drops on DCS-7280 and DCS-7500 family switches. | - | NOT RUN | - |
| 51 | dc1-leaf1a | Hardware | VerifyEnvironmentCooling | Verifies the status of power supply fans and all fan trays. | - | NOT RUN | - |
| 52 | dc1-leaf1a | Hardware | VerifyEnvironmentCooling | Verifies the status of power supply fans and all fan trays. | Accepted States: 'ok', 'Not Present' | NOT RUN | - |
| 53 | dc1-leaf1a | Hardware | VerifyEnvironmentPower | Verifies the power supplies status. | - | NOT RUN | - |
| 54 | dc1-leaf1a | Hardware | VerifyEnvironmentPower | Verifies the power supplies status. | Accepted States: 'ok', 'Not Present' | NOT RUN | - |
| 55 | dc1-leaf1a | Hardware | VerifyEnvironmentSystemCooling | Verifies the system cooling status. | - | NOT RUN | - |
| 56 | dc1-leaf1a | Hardware | VerifyTemperature | Verifies the device temperature. | - | NOT RUN | - |
| 57 | dc1-leaf1a | Hardware | VerifyTemperature | Verifies the device temperature. | - | NOT RUN | - |
| 58 | dc1-leaf1a | Hardware | VerifyTransceiversManufacturers | Verifies if all transceivers come from approved manufacturers. | - | NOT RUN | - |
| 59 | dc1-leaf1a | Hardware | VerifyTransceiversManufacturers | Verifies if all transceivers come from approved manufacturers. | Accepted Manufacturers: 'Arastra, Inc.', 'Arista Networks', 'Generic', 'Not Present' | NOT RUN | - |
| 60 | dc1-leaf1a | Hardware | VerifyTransceiversTemperature | Verifies the transceivers temperature. | - | NOT RUN | - |
| 61 | dc1-leaf1a | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet1 - P2P_LINK_TO_DC1-SPINE1_Ethernet1 = 'up' | NOT RUN | - |
| 62 | dc1-leaf1a | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet2 - P2P_LINK_TO_DC1-SPINE2_Ethernet1 = 'up' | NOT RUN | - |
| 63 | dc1-leaf1a | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet3 - MLAG_dc1-leaf1b_Ethernet3 = 'up' | NOT RUN | - |
| 64 | dc1-leaf1a | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet4 - MLAG_dc1-leaf1b_Ethernet4 = 'up' | NOT RUN | - |
| 65 | dc1-leaf1a | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet5 - SERVER_dc1-leaf1-server1_PCI1 = 'up' | NOT RUN | - |
| 66 | dc1-leaf1a | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet6 - P2P_LINK_TO_DC1-WAN1_Ethernet1 = 'up' | NOT RUN | - |
| 67 | dc1-leaf1a | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet7 - P2P_LINK_TO_DC1-WAN2_Ethernet1 = 'up' | NOT RUN | - |
| 68 | dc1-leaf1a | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet8 - DC1-LEAF1C_Ethernet1 = 'up' | NOT RUN | - |
| 69 | dc1-leaf1a | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback0 - ROUTER_ID = 'up' | NOT RUN | - |
| 70 | dc1-leaf1a | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback1 - VXLAN_TUNNEL_SOURCE = 'up' | NOT RUN | - |
| 71 | dc1-leaf1a | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback10 - VRF10_VTEP_DIAGNOSTICS = 'up' | NOT RUN | - |
| 72 | dc1-leaf1a | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback11 - VRF11_VTEP_DIAGNOSTICS = 'up' | NOT RUN | - |
| 73 | dc1-leaf1a | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel3 - MLAG_dc1-leaf1b_Port-Channel3 = 'up' | NOT RUN | - |
| 74 | dc1-leaf1a | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel5 - PortChannel dc1-leaf1-server1 = 'up' | NOT RUN | - |
| 75 | dc1-leaf1a | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel8 - DC1-LEAF1C_Po1 = 'up' | NOT RUN | - |
| 76 | dc1-leaf1a | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan11 - VRF10_VLAN11 = 'up' | NOT RUN | - |
| 77 | dc1-leaf1a | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan12 - VRF10_VLAN12 = 'up' | NOT RUN | - |
| 78 | dc1-leaf1a | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan21 - VRF11_VLAN21 = 'up' | NOT RUN | - |
| 79 | dc1-leaf1a | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan22 - VRF11_VLAN22 = 'up' | NOT RUN | - |
| 80 | dc1-leaf1a | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan3009 - MLAG_L3_VRF_VRF10 = 'up' | NOT RUN | - |
| 81 | dc1-leaf1a | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan3010 - MLAG_L3_VRF_VRF11 = 'up' | NOT RUN | - |
| 82 | dc1-leaf1a | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan4085 - Inband Management = 'up' | NOT RUN | - |
| 83 | dc1-leaf1a | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan4093 - MLAG_L3 = 'up' | NOT RUN | - |
| 84 | dc1-leaf1a | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan4094 - MLAG = 'up' | NOT RUN | - |
| 85 | dc1-leaf1a | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vxlan1 = 'up' | NOT RUN | - |
| 86 | dc1-leaf1a | LANZ | VerifyLANZ | Verifies if LANZ is enabled. | - | NOT RUN | - |
| 87 | dc1-leaf1a | MLAG | VerifyMlagStatus | Verifies the health status of the MLAG configuration. | - | NOT RUN | - |
| 88 | dc1-leaf1a | Profiles | VerifyTcamProfile | Verifies the device TCAM profile. | - | NOT RUN | - |
| 89 | dc1-leaf1a | Profiles | VerifyUnifiedForwardingTableMode | Verifies the device is using the expected UFT mode. | - | NOT RUN | - |
| 90 | dc1-leaf1a | PTP | VerifyPtpGMStatus | Verifies that the device is locked to a valid PTP Grandmaster. | - | NOT RUN | - |
| 91 | dc1-leaf1a | PTP | VerifyPtpLockStatus | Verifies that the device was locked to the upstream PTP GM in the last minute. | - | NOT RUN | - |
| 92 | dc1-leaf1a | PTP | VerifyPtpModeStatus | Verifies that the device is configured as a PTP Boundary Clock. | - | NOT RUN | - |
| 93 | dc1-leaf1a | PTP | VerifyPtpOffset | Verifies that the PTP timing offset is within +/- 1000ns from the master clock. | - | NOT RUN | - |
| 94 | dc1-leaf1a | PTP | VerifyPtpPortModeStatus | Verifies the PTP interfaces state. | - | NOT RUN | - |
| 95 | dc1-leaf1a | Routing | VerifyRoutingProtocolModel | Verifies the configured routing protocol model. | Routing protocol model: multi-agent | NOT RUN | - |
| 96 | dc1-leaf1a | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.0.1 - Peer: dc1-spine1 | NOT RUN | - |
| 97 | dc1-leaf1a | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.0.2 - Peer: dc1-spine2 | NOT RUN | - |
| 98 | dc1-leaf1a | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.0.3 - Peer: dc1-leaf1a | NOT RUN | - |
| 99 | dc1-leaf1a | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.0.4 - Peer: dc1-leaf1b | NOT RUN | - |
| 100 | dc1-leaf1a | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.0.5 - Peer: dc1-leaf2a | NOT RUN | - |
| 101 | dc1-leaf1a | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.1.3 - Peer: dc1-leaf1a | NOT RUN | - |
| 102 | dc1-leaf1a | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.1.5 - Peer: dc1-leaf2a | NOT RUN | - |
| 103 | dc1-leaf1a | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.128.11 - Peer: dc2-spine1 | NOT RUN | - |
| 104 | dc1-leaf1a | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.128.12 - Peer: dc2-spine2 | NOT RUN | - |
| 105 | dc1-leaf1a | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.128.13 - Peer: dc2-leaf1a | NOT RUN | - |
| 106 | dc1-leaf1a | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.128.14 - Peer: dc2-leaf1b | NOT RUN | - |
| 107 | dc1-leaf1a | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.128.15 - Peer: dc2-leaf2a | NOT RUN | - |
| 108 | dc1-leaf1a | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.128.16 - Peer: dc2-leaf2b | NOT RUN | - |
| 109 | dc1-leaf1a | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.128.17 - Peer: dc2-leaf3a.arista.com | NOT RUN | - |
| 110 | dc1-leaf1a | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.128.18 - Peer: dc2-leaf3b.arista.com | NOT RUN | - |
| 111 | dc1-leaf1a | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.129.13 - Peer: dc2-leaf1a | NOT RUN | - |
| 112 | dc1-leaf1a | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.129.15 - Peer: dc2-leaf2a | NOT RUN | - |
| 113 | dc1-leaf1a | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.129.17 - Peer: dc2-leaf3a.arista.com | NOT RUN | - |
| 114 | dc1-leaf1a | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.2.1 - Peer: dc1-wan1 | NOT RUN | - |
| 115 | dc1-leaf1a | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.2.2 - Peer: dc1-wan2 | NOT RUN | - |
| 116 | dc1-leaf1a | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.33.0.5 - Peer: dc1-svc-leaf1a | NOT RUN | - |
| 117 | dc1-leaf1a | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.33.0.6 - Peer: dc1-svc-leaf1b | NOT RUN | - |
| 118 | dc1-leaf1a | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.33.1.5 - Peer: dc1-svc-leaf1a | NOT RUN | - |
| 119 | dc1-leaf1a | Security | VerifyAPIHttpsSSL | Verifies if the eAPI has a valid SSL profile. | - | NOT RUN | - |
| 120 | dc1-leaf1a | Security | VerifyAPIHttpsSSL | Verifies if the eAPI has a valid SSL profile. | eAPI HTTPS SSL Profile: eAPI_SSL_Profile | NOT RUN | - |
| 121 | dc1-leaf1a | Security | VerifyAPIHttpStatus | Verifies if eAPI HTTP server is disabled globally. | - | NOT RUN | - |
| 122 | dc1-leaf1a | Security | VerifyAPIIPv4Acl | Verifies if eAPI has the right number IPv4 ACL(s) configured for a specified VRF. | - | NOT RUN | - |
| 123 | dc1-leaf1a | Security | VerifyAPIIPv6Acl | Verifies if eAPI has the right number IPv6 ACL(s) configured for a specified VRF. | - | NOT RUN | - |
| 124 | dc1-leaf1a | Security | VerifyAPISSLCertificate | Verifies the eAPI SSL certificate expiry, common subject name, encryption algorithm and key size. | - | NOT RUN | - |
| 125 | dc1-leaf1a | Security | VerifyBannerLogin | Verifies the login banner of a device. | - | NOT RUN | - |
| 126 | dc1-leaf1a | Security | VerifyBannerMotd | Verifies the motd banner of a device. | - | NOT RUN | - |
| 127 | dc1-leaf1a | Security | VerifyIPSecConnHealth | Verifies all IPv4 security connections. | - | NOT RUN | - |
| 128 | dc1-leaf1a | Security | VerifyIPv4ACL | Verifies the configuration of IPv4 ACLs. | - | NOT RUN | - |
| 129 | dc1-leaf1a | Security | VerifySpecificIPSecConn | Verifies IPv4 security connections for a peer. | - | NOT RUN | - |
| 130 | dc1-leaf1a | Security | VerifySSHIPv4Acl | Verifies if the SSHD agent has IPv4 ACL(s) configured. | - | NOT RUN | - |
| 131 | dc1-leaf1a | Security | VerifySSHIPv6Acl | Verifies if the SSHD agent has IPv6 ACL(s) configured. | - | NOT RUN | - |
| 132 | dc1-leaf1a | Security | VerifySSHStatus | Verifies if the SSHD agent is disabled in the default VRF. | - | NOT RUN | - |
| 133 | dc1-leaf1a | Security | VerifyTelnetStatus | Verifies if Telnet is disabled in the default VRF. | - | NOT RUN | - |
| 134 | dc1-leaf1a | Services | VerifyDNSLookup | Verifies the DNS name to IP address resolution. | - | NOT RUN | - |
| 135 | dc1-leaf1a | Services | VerifyDNSServers | Verifies if the DNS servers are correctly configured. | - | NOT RUN | - |
| 136 | dc1-leaf1a | Services | VerifyErrdisableRecovery | Verifies the errdisable recovery reason, status, and interval. | - | NOT RUN | - |
| 137 | dc1-leaf1a | Services | VerifyHostname | Verifies the hostname of a device. | - | NOT RUN | - |
| 138 | dc1-leaf1a | SNMP | VerifySnmpIPv4Acl | Verifies if the SNMP agent has IPv4 ACL(s) configured. | - | NOT RUN | - |
| 139 | dc1-leaf1a | SNMP | VerifySnmpIPv6Acl | Verifies if the SNMP agent has IPv6 ACL(s) configured. | - | NOT RUN | - |
| 140 | dc1-leaf1a | SNMP | VerifySnmpStatus | Verifies if the SNMP agent is enabled. | - | NOT RUN | - |
| 141 | dc1-leaf1a | Software | VerifyEOSExtensions | Verifies that all EOS extensions installed on the device are enabled for boot persistence. | - | NOT RUN | - |
| 142 | dc1-leaf1a | Software | VerifyEOSVersion | Verifies the EOS version of the device. | - | NOT RUN | - |
| 143 | dc1-leaf1a | Software | VerifyTerminAttrVersion | Verifies the TerminAttr version of the device. | - | NOT RUN | - |
| 144 | dc1-leaf1a | STUN | VerifyStunClient | Verifies the STUN client is configured with the specified IPv4 source address and port. Validate the public IP and port if provided. | - | NOT RUN | - |
| 145 | dc1-leaf1a | System | VerifyAgentLogs | Verifies there are no agent crash reports. | - | NOT RUN | - |
| 146 | dc1-leaf1a | System | VerifyCoredump | Verifies there are no core dump files. | - | NOT RUN | - |
| 147 | dc1-leaf1a | System | VerifyCPUUtilization | Verifies whether the CPU utilization is below 75%. | - | NOT RUN | - |
| 148 | dc1-leaf1a | System | VerifyFileSystemUtilization | Verifies that no partition is utilizing more than 75% of its disk space. | - | NOT RUN | - |
| 149 | dc1-leaf1a | System | VerifyMemoryUtilization | Verifies whether the memory utilization is below 75%. | - | NOT RUN | - |
| 150 | dc1-leaf1a | System | VerifyNTP | Verifies if NTP is synchronised. | - | NOT RUN | - |
| 151 | dc1-leaf1a | System | VerifyNTP | Verifies if NTP is synchronised. | - | NOT RUN | - |
| 152 | dc1-leaf1a | System | VerifyReloadCause | Verifies the last reload cause of the device. | - | NOT RUN | - |
| 153 | dc1-leaf1a | System | VerifyReloadCause | Verifies the last reload cause of the device. | - | NOT RUN | - |
| 154 | dc1-leaf1a | System | VerifyUptime | Verifies the device uptime. | - | NOT RUN | - |
| 155 | dc1-leaf1a | VLAN | VerifyVlanInternalPolicy | Verifies the VLAN internal allocation policy and the range of VLANs. | - | NOT RUN | - |
| 156 | dc1-leaf1a | VXLAN | VerifyVxlan1ConnSettings | Verifies the interface vxlan1 source interface and UDP port. | - | NOT RUN | - |
| 157 | dc1-leaf1a | VXLAN | VerifyVxlan1Interface | Verifies the Vxlan1 interface status. | - | NOT RUN | - |
| 158 | dc1-leaf1a | VXLAN | VerifyVxlanConfigSanity | Verifies there are no VXLAN config-sanity inconsistencies. | - | NOT RUN | - |
| 159 | dc1-leaf1a | VXLAN | VerifyVxlanVniBinding | Verifies the VNI-VLAN bindings of the Vxlan1 interface. | - | NOT RUN | - |
| 160 | dc1-leaf1a | VXLAN | VerifyVxlanVtep | Verifies the VTEP peers of the Vxlan1 interface | - | NOT RUN | - |
| 161 | dc1-leaf1b | AAA | VerifyAcctConsoleMethods | Verifies the AAA accounting console method lists for different accounting types (system, exec, commands, dot1x). | - | NOT RUN | - |
| 162 | dc1-leaf1b | AAA | VerifyAcctDefaultMethods | Verifies the AAA accounting default method lists for different accounting types (system, exec, commands, dot1x). | - | NOT RUN | - |
| 163 | dc1-leaf1b | AAA | VerifyAuthenMethods | Verifies the AAA authentication method lists for different authentication types (login, enable, dot1x). | - | NOT RUN | - |
| 164 | dc1-leaf1b | AAA | VerifyAuthzMethods | Verifies the AAA authorization method lists for different authorization types (commands, exec). | - | NOT RUN | - |
| 165 | dc1-leaf1b | AAA | VerifyTacacsServerGroups | Verifies if the provided TACACS server group(s) are configured. | - | NOT RUN | - |
| 166 | dc1-leaf1b | AAA | VerifyTacacsServers | Verifies TACACS servers are configured for a specified VRF. | - | NOT RUN | - |
| 167 | dc1-leaf1b | AAA | VerifyTacacsSourceIntf | Verifies TACACS source-interface for a specified VRF. | - | NOT RUN | - |
| 168 | dc1-leaf1b | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: dc1-spine1 (IP: 10.255.0.1) | NOT RUN | - |
| 169 | dc1-leaf1b | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: dc1-spine2 (IP: 10.255.0.2) | NOT RUN | - |
| 170 | dc1-leaf1b | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: dc1-leaf1a (IP: 10.255.1.96) | NOT RUN | - |
| 171 | dc1-leaf1b | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: dc1-spine1 (IP: 10.255.255.4) | NOT RUN | - |
| 172 | dc1-leaf1b | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: dc1-spine2 (IP: 10.255.255.6) | NOT RUN | - |
| 173 | dc1-leaf1b | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: dc1-wan1 (IP: 10.255.255.3) | NOT RUN | - |
| 174 | dc1-leaf1b | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: dc1-wan2 (IP: 10.255.255.7) | NOT RUN | - |
| 175 | dc1-leaf1b | Configuration | VerifyRunningConfigDiffs | Verifies there is no difference between the running-config and the startup-config | - | NOT RUN | - |
| 176 | dc1-leaf1b | Configuration | VerifyZeroTouch | Verifies ZeroTouch is disabled | - | NOT RUN | - |
| 177 | dc1-leaf1b | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet1 - Remote: dc1-spine1 Ethernet2 | NOT RUN | - |
| 178 | dc1-leaf1b | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet2 - Remote: dc1-spine2 Ethernet2 | NOT RUN | - |
| 179 | dc1-leaf1b | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet3 - Remote: dc1-leaf1a Ethernet3 | NOT RUN | - |
| 180 | dc1-leaf1b | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet4 - Remote: dc1-leaf1a Ethernet4 | NOT RUN | - |
| 181 | dc1-leaf1b | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet6 - Remote: dc1-wan1 Ethernet2 | NOT RUN | - |
| 182 | dc1-leaf1b | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet7 - Remote: dc1-wan2 Ethernet2 | NOT RUN | - |
| 183 | dc1-leaf1b | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet8 - Remote: dc1-leaf1c Ethernet2 | NOT RUN | - |
| 184 | dc1-leaf1b | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.0.4) - Destination: dc1-leaf1a Loopback0 (IP: 10.255.0.3) | NOT RUN | - |
| 185 | dc1-leaf1b | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.0.4) - Destination: dc1-leaf1b Loopback0 (IP: 10.255.0.4) | NOT RUN | - |
| 186 | dc1-leaf1b | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.0.4) - Destination: dc1-leaf2a Loopback0 (IP: 10.255.0.5) | NOT RUN | - |
| 187 | dc1-leaf1b | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.0.4) - Destination: dc1-spine1 Loopback0 (IP: 10.255.0.1) | NOT RUN | - |
| 188 | dc1-leaf1b | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.0.4) - Destination: dc1-spine2 Loopback0 (IP: 10.255.0.2) | NOT RUN | - |
| 189 | dc1-leaf1b | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.0.4) - Destination: dc1-svc-leaf1a Loopback0 (IP: 10.33.0.5) | NOT RUN | - |
| 190 | dc1-leaf1b | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.0.4) - Destination: dc1-svc-leaf1b Loopback0 (IP: 10.33.0.6) | NOT RUN | - |
| 191 | dc1-leaf1b | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.0.4) - Destination: dc1-wan1 Loopback0 (IP: 10.255.2.1) | NOT RUN | - |
| 192 | dc1-leaf1b | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.0.4) - Destination: dc1-wan2 Loopback0 (IP: 10.255.2.2) | NOT RUN | - |
| 193 | dc1-leaf1b | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.0.4) - Destination: dc2-leaf1a Loopback0 (IP: 10.255.128.13) | NOT RUN | - |
| 194 | dc1-leaf1b | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.0.4) - Destination: dc2-leaf1b Loopback0 (IP: 10.255.128.14) | NOT RUN | - |
| 195 | dc1-leaf1b | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.0.4) - Destination: dc2-leaf2a Loopback0 (IP: 10.255.128.15) | NOT RUN | - |
| 196 | dc1-leaf1b | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.0.4) - Destination: dc2-leaf2b Loopback0 (IP: 10.255.128.16) | NOT RUN | - |
| 197 | dc1-leaf1b | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.0.4) - Destination: dc2-leaf3a.arista.com Loopback0 (IP: 10.255.128.17) | NOT RUN | - |
| 198 | dc1-leaf1b | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.0.4) - Destination: dc2-leaf3b.arista.com Loopback0 (IP: 10.255.128.18) | NOT RUN | - |
| 199 | dc1-leaf1b | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.0.4) - Destination: dc2-spine1 Loopback0 (IP: 10.255.128.11) | NOT RUN | - |
| 200 | dc1-leaf1b | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.0.4) - Destination: dc2-spine2 Loopback0 (IP: 10.255.128.12) | NOT RUN | - |
| 201 | dc1-leaf1b | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet1 (IP: 10.255.255.5) - Destination: dc1-spine1 Ethernet2 (IP: 10.255.255.4) | NOT RUN | - |
| 202 | dc1-leaf1b | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet2 (IP: 10.255.255.7) - Destination: dc1-spine2 Ethernet2 (IP: 10.255.255.6) | NOT RUN | - |
| 203 | dc1-leaf1b | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet6 (IP: 10.255.255.2) - Destination: dc1-wan1 Ethernet2 (IP: 10.255.255.3) | NOT RUN | - |
| 204 | dc1-leaf1b | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet7 (IP: 10.255.255.6) - Destination: dc1-wan2 Ethernet2 (IP: 10.255.255.7) | NOT RUN | - |
| 205 | dc1-leaf1b | Field Notices | VerifyFieldNotice44Resolution | Verifies that the device is using the correct Aboot version per FN0044. | - | NOT RUN | - |
| 206 | dc1-leaf1b | Field Notices | VerifyFieldNotice72Resolution | Verifies if the device is exposed to FN0072, and if the issue has been mitigated. | - | NOT RUN | - |
| 207 | dc1-leaf1b | Greent | VerifyGreenT | Verifies if a GreenT policy is created. | - | NOT RUN | - |
| 208 | dc1-leaf1b | Greent | VerifyGreenTCounters | Verifies if the GreenT counters are incremented. | - | NOT RUN | - |
| 209 | dc1-leaf1b | Hardware | VerifyAdverseDrops | Verifies there are no adverse drops on DCS-7280 and DCS-7500 family switches. | - | NOT RUN | - |
| 210 | dc1-leaf1b | Hardware | VerifyEnvironmentCooling | Verifies the status of power supply fans and all fan trays. | - | NOT RUN | - |
| 211 | dc1-leaf1b | Hardware | VerifyEnvironmentCooling | Verifies the status of power supply fans and all fan trays. | Accepted States: 'ok' | NOT RUN | - |
| 212 | dc1-leaf1b | Hardware | VerifyEnvironmentPower | Verifies the power supplies status. | - | NOT RUN | - |
| 213 | dc1-leaf1b | Hardware | VerifyEnvironmentPower | Verifies the power supplies status. | Accepted States: 'ok' | NOT RUN | - |
| 214 | dc1-leaf1b | Hardware | VerifyEnvironmentSystemCooling | Verifies the system cooling status. | - | NOT RUN | - |
| 215 | dc1-leaf1b | Hardware | VerifyTemperature | Verifies the device temperature. | - | NOT RUN | - |
| 216 | dc1-leaf1b | Hardware | VerifyTemperature | Verifies the device temperature. | - | NOT RUN | - |
| 217 | dc1-leaf1b | Hardware | VerifyTransceiversManufacturers | Verifies if all transceivers come from approved manufacturers. | - | NOT RUN | - |
| 218 | dc1-leaf1b | Hardware | VerifyTransceiversManufacturers | Verifies if all transceivers come from approved manufacturers. | Accepted Manufacturers: 'Arista Networks', 'Arastra, Inc.', 'Not Present' | NOT RUN | - |
| 219 | dc1-leaf1b | Hardware | VerifyTransceiversTemperature | Verifies the transceivers temperature. | - | NOT RUN | - |
| 220 | dc1-leaf1b | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet1 - P2P_LINK_TO_DC1-SPINE1_Ethernet2 = 'up' | NOT RUN | - |
| 221 | dc1-leaf1b | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet2 - P2P_LINK_TO_DC1-SPINE2_Ethernet2 = 'up' | NOT RUN | - |
| 222 | dc1-leaf1b | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet3 - MLAG_dc1-leaf1a_Ethernet3 = 'up' | NOT RUN | - |
| 223 | dc1-leaf1b | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet4 - MLAG_dc1-leaf1a_Ethernet4 = 'up' | NOT RUN | - |
| 224 | dc1-leaf1b | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet5 - SERVER_dc1-leaf1-server1_PCI2 = 'up' | NOT RUN | - |
| 225 | dc1-leaf1b | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet6 - P2P_LINK_TO_DC1-WAN1_Ethernet2 = 'up' | NOT RUN | - |
| 226 | dc1-leaf1b | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet7 - P2P_LINK_TO_DC1-WAN2_Ethernet2 = 'up' | NOT RUN | - |
| 227 | dc1-leaf1b | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet8 - DC1-LEAF1C_Ethernet2 = 'up' | NOT RUN | - |
| 228 | dc1-leaf1b | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback0 - ROUTER_ID = 'up' | NOT RUN | - |
| 229 | dc1-leaf1b | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback1 - VXLAN_TUNNEL_SOURCE = 'up' | NOT RUN | - |
| 230 | dc1-leaf1b | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback10 - VRF10_VTEP_DIAGNOSTICS = 'up' | NOT RUN | - |
| 231 | dc1-leaf1b | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback11 - VRF11_VTEP_DIAGNOSTICS = 'up' | NOT RUN | - |
| 232 | dc1-leaf1b | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel3 - MLAG_dc1-leaf1a_Port-Channel3 = 'up' | NOT RUN | - |
| 233 | dc1-leaf1b | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel5 - PortChannel dc1-leaf1-server1 = 'up' | NOT RUN | - |
| 234 | dc1-leaf1b | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel8 - DC1-LEAF1C_Po1 = 'up' | NOT RUN | - |
| 235 | dc1-leaf1b | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan11 - VRF10_VLAN11 = 'up' | NOT RUN | - |
| 236 | dc1-leaf1b | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan12 - VRF10_VLAN12 = 'up' | NOT RUN | - |
| 237 | dc1-leaf1b | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan21 - VRF11_VLAN21 = 'up' | NOT RUN | - |
| 238 | dc1-leaf1b | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan22 - VRF11_VLAN22 = 'up' | NOT RUN | - |
| 239 | dc1-leaf1b | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan3009 - MLAG_L3_VRF_VRF10 = 'up' | NOT RUN | - |
| 240 | dc1-leaf1b | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan3010 - MLAG_L3_VRF_VRF11 = 'up' | NOT RUN | - |
| 241 | dc1-leaf1b | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan4085 - Inband Management = 'up' | NOT RUN | - |
| 242 | dc1-leaf1b | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan4093 - MLAG_L3 = 'up' | NOT RUN | - |
| 243 | dc1-leaf1b | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan4094 - MLAG = 'up' | NOT RUN | - |
| 244 | dc1-leaf1b | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vxlan1 = 'up' | NOT RUN | - |
| 245 | dc1-leaf1b | LANZ | VerifyLANZ | Verifies if LANZ is enabled. | - | NOT RUN | - |
| 246 | dc1-leaf1b | MLAG | VerifyMlagStatus | Verifies the health status of the MLAG configuration. | - | NOT RUN | - |
| 247 | dc1-leaf1b | PTP | VerifyPtpGMStatus | Verifies that the device is locked to a valid PTP Grandmaster. | - | NOT RUN | - |
| 248 | dc1-leaf1b | PTP | VerifyPtpLockStatus | Verifies that the device was locked to the upstream PTP GM in the last minute. | - | NOT RUN | - |
| 249 | dc1-leaf1b | PTP | VerifyPtpModeStatus | Verifies that the device is configured as a PTP Boundary Clock. | - | NOT RUN | - |
| 250 | dc1-leaf1b | PTP | VerifyPtpOffset | Verifies that the PTP timing offset is within +/- 1000ns from the master clock. | - | NOT RUN | - |
| 251 | dc1-leaf1b | PTP | VerifyPtpPortModeStatus | Verifies the PTP interfaces state. | - | NOT RUN | - |
| 252 | dc1-leaf1b | Routing | VerifyRoutingProtocolModel | Verifies the configured routing protocol model. | Routing protocol model: multi-agent | NOT RUN | - |
| 253 | dc1-leaf1b | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.0.1 - Peer: dc1-spine1 | NOT RUN | - |
| 254 | dc1-leaf1b | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.0.2 - Peer: dc1-spine2 | NOT RUN | - |
| 255 | dc1-leaf1b | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.0.3 - Peer: dc1-leaf1a | NOT RUN | - |
| 256 | dc1-leaf1b | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.0.4 - Peer: dc1-leaf1b | NOT RUN | - |
| 257 | dc1-leaf1b | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.0.5 - Peer: dc1-leaf2a | NOT RUN | - |
| 258 | dc1-leaf1b | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.1.3 - Peer: dc1-leaf1a | NOT RUN | - |
| 259 | dc1-leaf1b | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.1.5 - Peer: dc1-leaf2a | NOT RUN | - |
| 260 | dc1-leaf1b | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.128.11 - Peer: dc2-spine1 | NOT RUN | - |
| 261 | dc1-leaf1b | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.128.12 - Peer: dc2-spine2 | NOT RUN | - |
| 262 | dc1-leaf1b | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.128.13 - Peer: dc2-leaf1a | NOT RUN | - |
| 263 | dc1-leaf1b | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.128.14 - Peer: dc2-leaf1b | NOT RUN | - |
| 264 | dc1-leaf1b | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.128.15 - Peer: dc2-leaf2a | NOT RUN | - |
| 265 | dc1-leaf1b | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.128.16 - Peer: dc2-leaf2b | NOT RUN | - |
| 266 | dc1-leaf1b | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.128.17 - Peer: dc2-leaf3a.arista.com | NOT RUN | - |
| 267 | dc1-leaf1b | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.128.18 - Peer: dc2-leaf3b.arista.com | NOT RUN | - |
| 268 | dc1-leaf1b | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.129.13 - Peer: dc2-leaf1a | NOT RUN | - |
| 269 | dc1-leaf1b | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.129.15 - Peer: dc2-leaf2a | NOT RUN | - |
| 270 | dc1-leaf1b | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.129.17 - Peer: dc2-leaf3a.arista.com | NOT RUN | - |
| 271 | dc1-leaf1b | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.2.1 - Peer: dc1-wan1 | NOT RUN | - |
| 272 | dc1-leaf1b | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.2.2 - Peer: dc1-wan2 | NOT RUN | - |
| 273 | dc1-leaf1b | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.33.0.5 - Peer: dc1-svc-leaf1a | NOT RUN | - |
| 274 | dc1-leaf1b | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.33.0.6 - Peer: dc1-svc-leaf1b | NOT RUN | - |
| 275 | dc1-leaf1b | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.33.1.5 - Peer: dc1-svc-leaf1a | NOT RUN | - |
| 276 | dc1-leaf1b | Security | VerifyAPIHttpsSSL | Verifies if the eAPI has a valid SSL profile. | - | NOT RUN | - |
| 277 | dc1-leaf1b | Security | VerifyAPIHttpsSSL | Verifies if the eAPI has a valid SSL profile. | eAPI HTTPS SSL Profile: eAPI_SSL_Profile | NOT RUN | - |
| 278 | dc1-leaf1b | Security | VerifyAPIHttpStatus | Verifies if eAPI HTTP server is disabled globally. | - | NOT RUN | - |
| 279 | dc1-leaf1b | Security | VerifyAPIIPv4Acl | Verifies if eAPI has the right number IPv4 ACL(s) configured for a specified VRF. | - | NOT RUN | - |
| 280 | dc1-leaf1b | Security | VerifyAPIIPv6Acl | Verifies if eAPI has the right number IPv6 ACL(s) configured for a specified VRF. | - | NOT RUN | - |
| 281 | dc1-leaf1b | Security | VerifyAPISSLCertificate | Verifies the eAPI SSL certificate expiry, common subject name, encryption algorithm and key size. | - | NOT RUN | - |
| 282 | dc1-leaf1b | Security | VerifyBannerLogin | Verifies the login banner of a device. | - | NOT RUN | - |
| 283 | dc1-leaf1b | Security | VerifyBannerMotd | Verifies the motd banner of a device. | - | NOT RUN | - |
| 284 | dc1-leaf1b | Security | VerifyIPSecConnHealth | Verifies all IPv4 security connections. | - | NOT RUN | - |
| 285 | dc1-leaf1b | Security | VerifyIPv4ACL | Verifies the configuration of IPv4 ACLs. | - | NOT RUN | - |
| 286 | dc1-leaf1b | Security | VerifySpecificIPSecConn | Verifies IPv4 security connections for a peer. | - | NOT RUN | - |
| 287 | dc1-leaf1b | Security | VerifySSHIPv4Acl | Verifies if the SSHD agent has IPv4 ACL(s) configured. | - | NOT RUN | - |
| 288 | dc1-leaf1b | Security | VerifySSHIPv6Acl | Verifies if the SSHD agent has IPv6 ACL(s) configured. | - | NOT RUN | - |
| 289 | dc1-leaf1b | Security | VerifySSHStatus | Verifies if the SSHD agent is disabled in the default VRF. | - | NOT RUN | - |
| 290 | dc1-leaf1b | Security | VerifyTelnetStatus | Verifies if Telnet is disabled in the default VRF. | - | NOT RUN | - |
| 291 | dc1-leaf1b | Services | VerifyDNSLookup | Verifies the DNS name to IP address resolution. | - | NOT RUN | - |
| 292 | dc1-leaf1b | Services | VerifyDNSServers | Verifies if the DNS servers are correctly configured. | - | NOT RUN | - |
| 293 | dc1-leaf1b | Services | VerifyErrdisableRecovery | Verifies the errdisable recovery reason, status, and interval. | - | NOT RUN | - |
| 294 | dc1-leaf1b | Services | VerifyHostname | Verifies the hostname of a device. | - | NOT RUN | - |
| 295 | dc1-leaf1b | SNMP | VerifySnmpIPv4Acl | Verifies if the SNMP agent has IPv4 ACL(s) configured. | - | NOT RUN | - |
| 296 | dc1-leaf1b | SNMP | VerifySnmpIPv6Acl | Verifies if the SNMP agent has IPv6 ACL(s) configured. | - | NOT RUN | - |
| 297 | dc1-leaf1b | SNMP | VerifySnmpStatus | Verifies if the SNMP agent is enabled. | - | NOT RUN | - |
| 298 | dc1-leaf1b | Software | VerifyEOSVersion | Verifies the EOS version of the device. | - | NOT RUN | - |
| 299 | dc1-leaf1b | Software | VerifyTerminAttrVersion | Verifies the TerminAttr version of the device. | - | NOT RUN | - |
| 300 | dc1-leaf1b | STUN | VerifyStunClient | Verifies the STUN client is configured with the specified IPv4 source address and port. Validate the public IP and port if provided. | - | NOT RUN | - |
| 301 | dc1-leaf1b | System | VerifyAgentLogs | Verifies there are no agent crash reports. | - | NOT RUN | - |
| 302 | dc1-leaf1b | System | VerifyCoredump | Verifies there are no core dump files. | - | NOT RUN | - |
| 303 | dc1-leaf1b | System | VerifyCPUUtilization | Verifies whether the CPU utilization is below 75%. | - | NOT RUN | - |
| 304 | dc1-leaf1b | System | VerifyFileSystemUtilization | Verifies that no partition is utilizing more than 75% of its disk space. | - | NOT RUN | - |
| 305 | dc1-leaf1b | System | VerifyMemoryUtilization | Verifies whether the memory utilization is below 75%. | - | NOT RUN | - |
| 306 | dc1-leaf1b | System | VerifyNTP | Verifies if NTP is synchronised. | - | NOT RUN | - |
| 307 | dc1-leaf1b | System | VerifyNTP | Verifies if NTP is synchronised. | - | NOT RUN | - |
| 308 | dc1-leaf1b | System | VerifyReloadCause | Verifies the last reload cause of the device. | - | NOT RUN | - |
| 309 | dc1-leaf1b | System | VerifyReloadCause | Verifies the last reload cause of the device. | - | NOT RUN | - |
| 310 | dc1-leaf1b | System | VerifyUptime | Verifies the device uptime. | - | NOT RUN | - |
| 311 | dc1-leaf1b | VLAN | VerifyVlanInternalPolicy | Verifies the VLAN internal allocation policy and the range of VLANs. | - | NOT RUN | - |
| 312 | dc1-leaf1c | AAA | VerifyAcctConsoleMethods | Verifies the AAA accounting console method lists for different accounting types (system, exec, commands, dot1x). | - | NOT RUN | - |
| 313 | dc1-leaf1c | AAA | VerifyAcctDefaultMethods | Verifies the AAA accounting default method lists for different accounting types (system, exec, commands, dot1x). | - | NOT RUN | - |
| 314 | dc1-leaf1c | AAA | VerifyAuthenMethods | Verifies the AAA authentication method lists for different authentication types (login, enable, dot1x). | - | NOT RUN | - |
| 315 | dc1-leaf1c | AAA | VerifyAuthzMethods | Verifies the AAA authorization method lists for different authorization types (commands, exec). | - | NOT RUN | - |
| 316 | dc1-leaf1c | AAA | VerifyTacacsServerGroups | Verifies if the provided TACACS server group(s) are configured. | - | NOT RUN | - |
| 317 | dc1-leaf1c | AAA | VerifyTacacsServers | Verifies TACACS servers are configured for a specified VRF. | - | NOT RUN | - |
| 318 | dc1-leaf1c | AAA | VerifyTacacsSourceIntf | Verifies TACACS source-interface for a specified VRF. | - | NOT RUN | - |
| 319 | dc1-leaf1c | Configuration | VerifyRunningConfigDiffs | Verifies there is no difference between the running-config and the startup-config | - | NOT RUN | - |
| 320 | dc1-leaf1c | Configuration | VerifyZeroTouch | Verifies ZeroTouch is disabled | - | NOT RUN | - |
| 321 | dc1-leaf1c | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet1 - Remote: dc1-leaf1a Ethernet8 | NOT RUN | - |
| 322 | dc1-leaf1c | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet2 - Remote: dc1-leaf1b Ethernet8 | NOT RUN | - |
| 323 | dc1-leaf1c | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Inband MGMT SVI Vlan4085 (IP: 172.21.110.4) - Destination: dc1-leaf1a Loopback0 (IP: 10.255.0.3) | NOT RUN | - |
| 324 | dc1-leaf1c | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Inband MGMT SVI Vlan4085 (IP: 172.21.110.4) - Destination: dc1-leaf1b Loopback0 (IP: 10.255.0.4) | NOT RUN | - |
| 325 | dc1-leaf1c | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Inband MGMT SVI Vlan4085 (IP: 172.21.110.4) - Destination: dc1-leaf2a Loopback0 (IP: 10.255.0.5) | NOT RUN | - |
| 326 | dc1-leaf1c | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Inband MGMT SVI Vlan4085 (IP: 172.21.110.4) - Destination: dc1-spine1 Loopback0 (IP: 10.255.0.1) | NOT RUN | - |
| 327 | dc1-leaf1c | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Inband MGMT SVI Vlan4085 (IP: 172.21.110.4) - Destination: dc1-spine2 Loopback0 (IP: 10.255.0.2) | NOT RUN | - |
| 328 | dc1-leaf1c | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Inband MGMT SVI Vlan4085 (IP: 172.21.110.4) - Destination: dc1-svc-leaf1a Loopback0 (IP: 10.33.0.5) | NOT RUN | - |
| 329 | dc1-leaf1c | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Inband MGMT SVI Vlan4085 (IP: 172.21.110.4) - Destination: dc1-svc-leaf1b Loopback0 (IP: 10.33.0.6) | NOT RUN | - |
| 330 | dc1-leaf1c | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Inband MGMT SVI Vlan4085 (IP: 172.21.110.4) - Destination: dc1-wan1 Loopback0 (IP: 10.255.2.1) | NOT RUN | - |
| 331 | dc1-leaf1c | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Inband MGMT SVI Vlan4085 (IP: 172.21.110.4) - Destination: dc1-wan2 Loopback0 (IP: 10.255.2.2) | NOT RUN | - |
| 332 | dc1-leaf1c | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Inband MGMT SVI Vlan4085 (IP: 172.21.110.4) - Destination: dc2-leaf1a Loopback0 (IP: 10.255.128.13) | NOT RUN | - |
| 333 | dc1-leaf1c | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Inband MGMT SVI Vlan4085 (IP: 172.21.110.4) - Destination: dc2-leaf1b Loopback0 (IP: 10.255.128.14) | NOT RUN | - |
| 334 | dc1-leaf1c | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Inband MGMT SVI Vlan4085 (IP: 172.21.110.4) - Destination: dc2-leaf2a Loopback0 (IP: 10.255.128.15) | NOT RUN | - |
| 335 | dc1-leaf1c | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Inband MGMT SVI Vlan4085 (IP: 172.21.110.4) - Destination: dc2-leaf2b Loopback0 (IP: 10.255.128.16) | NOT RUN | - |
| 336 | dc1-leaf1c | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Inband MGMT SVI Vlan4085 (IP: 172.21.110.4) - Destination: dc2-leaf3a.arista.com Loopback0 (IP: 10.255.128.17) | NOT RUN | - |
| 337 | dc1-leaf1c | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Inband MGMT SVI Vlan4085 (IP: 172.21.110.4) - Destination: dc2-leaf3b.arista.com Loopback0 (IP: 10.255.128.18) | NOT RUN | - |
| 338 | dc1-leaf1c | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Inband MGMT SVI Vlan4085 (IP: 172.21.110.4) - Destination: dc2-spine1 Loopback0 (IP: 10.255.128.11) | NOT RUN | - |
| 339 | dc1-leaf1c | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Inband MGMT SVI Vlan4085 (IP: 172.21.110.4) - Destination: dc2-spine2 Loopback0 (IP: 10.255.128.12) | NOT RUN | - |
| 340 | dc1-leaf1c | Field Notices | VerifyFieldNotice44Resolution | Verifies that the device is using the correct Aboot version per FN0044. | - | NOT RUN | - |
| 341 | dc1-leaf1c | Field Notices | VerifyFieldNotice72Resolution | Verifies if the device is exposed to FN0072, and if the issue has been mitigated. | - | NOT RUN | - |
| 342 | dc1-leaf1c | Greent | VerifyGreenT | Verifies if a GreenT policy is created. | - | NOT RUN | - |
| 343 | dc1-leaf1c | Greent | VerifyGreenTCounters | Verifies if the GreenT counters are incremented. | - | NOT RUN | - |
| 344 | dc1-leaf1c | Hardware | VerifyAdverseDrops | Verifies there are no adverse drops on DCS-7280 and DCS-7500 family switches. | - | NOT RUN | - |
| 345 | dc1-leaf1c | Hardware | VerifyEnvironmentCooling | Verifies the status of power supply fans and all fan trays. | - | NOT RUN | - |
| 346 | dc1-leaf1c | Hardware | VerifyEnvironmentCooling | Verifies the status of power supply fans and all fan trays. | Accepted States: 'ok' | NOT RUN | - |
| 347 | dc1-leaf1c | Hardware | VerifyEnvironmentPower | Verifies the power supplies status. | - | NOT RUN | - |
| 348 | dc1-leaf1c | Hardware | VerifyEnvironmentPower | Verifies the power supplies status. | Accepted States: 'ok' | NOT RUN | - |
| 349 | dc1-leaf1c | Hardware | VerifyEnvironmentSystemCooling | Verifies the system cooling status. | - | NOT RUN | - |
| 350 | dc1-leaf1c | Hardware | VerifyTemperature | Verifies the device temperature. | - | NOT RUN | - |
| 351 | dc1-leaf1c | Hardware | VerifyTemperature | Verifies the device temperature. | - | NOT RUN | - |
| 352 | dc1-leaf1c | Hardware | VerifyTransceiversManufacturers | Verifies if all transceivers come from approved manufacturers. | - | NOT RUN | - |
| 353 | dc1-leaf1c | Hardware | VerifyTransceiversManufacturers | Verifies if all transceivers come from approved manufacturers. | Accepted Manufacturers: 'Arista Networks', 'Arastra, Inc.', 'Not Present' | NOT RUN | - |
| 354 | dc1-leaf1c | Hardware | VerifyTransceiversTemperature | Verifies the transceivers temperature. | - | NOT RUN | - |
| 355 | dc1-leaf1c | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet1 - DC1-LEAF1A_Ethernet8 = 'up' | NOT RUN | - |
| 356 | dc1-leaf1c | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet2 - DC1-LEAF1B_Ethernet8 = 'up' | NOT RUN | - |
| 357 | dc1-leaf1c | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet5 - SERVER_dc1-leaf1-server1_iLO = 'up' | NOT RUN | - |
| 358 | dc1-leaf1c | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel1 - DC1_L3_LEAF1_Po8 = 'up' | NOT RUN | - |
| 359 | dc1-leaf1c | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan4085 - L2LEAF_INBAND_MGMT = 'up' | NOT RUN | - |
| 360 | dc1-leaf1c | LANZ | VerifyLANZ | Verifies if LANZ is enabled. | - | NOT RUN | - |
| 361 | dc1-leaf1c | PTP | VerifyPtpGMStatus | Verifies that the device is locked to a valid PTP Grandmaster. | - | NOT RUN | - |
| 362 | dc1-leaf1c | PTP | VerifyPtpLockStatus | Verifies that the device was locked to the upstream PTP GM in the last minute. | - | NOT RUN | - |
| 363 | dc1-leaf1c | PTP | VerifyPtpModeStatus | Verifies that the device is configured as a PTP Boundary Clock. | - | NOT RUN | - |
| 364 | dc1-leaf1c | PTP | VerifyPtpOffset | Verifies that the PTP timing offset is within +/- 1000ns from the master clock. | - | NOT RUN | - |
| 365 | dc1-leaf1c | PTP | VerifyPtpPortModeStatus | Verifies the PTP interfaces state. | - | NOT RUN | - |
| 366 | dc1-leaf1c | Security | VerifyAPIHttpsSSL | Verifies if the eAPI has a valid SSL profile. | - | NOT RUN | - |
| 367 | dc1-leaf1c | Security | VerifyAPIHttpsSSL | Verifies if the eAPI has a valid SSL profile. | eAPI HTTPS SSL Profile: eAPI_SSL_Profile | NOT RUN | - |
| 368 | dc1-leaf1c | Security | VerifyAPIHttpStatus | Verifies if eAPI HTTP server is disabled globally. | - | NOT RUN | - |
| 369 | dc1-leaf1c | Security | VerifyAPIIPv4Acl | Verifies if eAPI has the right number IPv4 ACL(s) configured for a specified VRF. | - | NOT RUN | - |
| 370 | dc1-leaf1c | Security | VerifyAPIIPv6Acl | Verifies if eAPI has the right number IPv6 ACL(s) configured for a specified VRF. | - | NOT RUN | - |
| 371 | dc1-leaf1c | Security | VerifyAPISSLCertificate | Verifies the eAPI SSL certificate expiry, common subject name, encryption algorithm and key size. | - | NOT RUN | - |
| 372 | dc1-leaf1c | Security | VerifyBannerLogin | Verifies the login banner of a device. | - | NOT RUN | - |
| 373 | dc1-leaf1c | Security | VerifyBannerMotd | Verifies the motd banner of a device. | - | NOT RUN | - |
| 374 | dc1-leaf1c | Security | VerifyIPSecConnHealth | Verifies all IPv4 security connections. | - | NOT RUN | - |
| 375 | dc1-leaf1c | Security | VerifyIPv4ACL | Verifies the configuration of IPv4 ACLs. | - | NOT RUN | - |
| 376 | dc1-leaf1c | Security | VerifySpecificIPSecConn | Verifies IPv4 security connections for a peer. | - | NOT RUN | - |
| 377 | dc1-leaf1c | Security | VerifySSHIPv4Acl | Verifies if the SSHD agent has IPv4 ACL(s) configured. | - | NOT RUN | - |
| 378 | dc1-leaf1c | Security | VerifySSHIPv6Acl | Verifies if the SSHD agent has IPv6 ACL(s) configured. | - | NOT RUN | - |
| 379 | dc1-leaf1c | Security | VerifySSHStatus | Verifies if the SSHD agent is disabled in the default VRF. | - | NOT RUN | - |
| 380 | dc1-leaf1c | Security | VerifyTelnetStatus | Verifies if Telnet is disabled in the default VRF. | - | NOT RUN | - |
| 381 | dc1-leaf1c | Services | VerifyDNSLookup | Verifies the DNS name to IP address resolution. | - | NOT RUN | - |
| 382 | dc1-leaf1c | Services | VerifyDNSServers | Verifies if the DNS servers are correctly configured. | - | NOT RUN | - |
| 383 | dc1-leaf1c | Services | VerifyErrdisableRecovery | Verifies the errdisable recovery reason, status, and interval. | - | NOT RUN | - |
| 384 | dc1-leaf1c | Services | VerifyHostname | Verifies the hostname of a device. | - | NOT RUN | - |
| 385 | dc1-leaf1c | SNMP | VerifySnmpIPv4Acl | Verifies if the SNMP agent has IPv4 ACL(s) configured. | - | NOT RUN | - |
| 386 | dc1-leaf1c | SNMP | VerifySnmpIPv6Acl | Verifies if the SNMP agent has IPv6 ACL(s) configured. | - | NOT RUN | - |
| 387 | dc1-leaf1c | SNMP | VerifySnmpStatus | Verifies if the SNMP agent is enabled. | - | NOT RUN | - |
| 388 | dc1-leaf1c | Software | VerifyEOSVersion | Verifies the EOS version of the device. | - | NOT RUN | - |
| 389 | dc1-leaf1c | Software | VerifyTerminAttrVersion | Verifies the TerminAttr version of the device. | - | NOT RUN | - |
| 390 | dc1-leaf1c | STUN | VerifyStunClient | Verifies the STUN client is configured with the specified IPv4 source address and port. Validate the public IP and port if provided. | - | NOT RUN | - |
| 391 | dc1-leaf1c | System | VerifyAgentLogs | Verifies there are no agent crash reports. | - | NOT RUN | - |
| 392 | dc1-leaf1c | System | VerifyCoredump | Verifies there are no core dump files. | - | NOT RUN | - |
| 393 | dc1-leaf1c | System | VerifyCPUUtilization | Verifies whether the CPU utilization is below 75%. | - | NOT RUN | - |
| 394 | dc1-leaf1c | System | VerifyFileSystemUtilization | Verifies that no partition is utilizing more than 75% of its disk space. | - | NOT RUN | - |
| 395 | dc1-leaf1c | System | VerifyMemoryUtilization | Verifies whether the memory utilization is below 75%. | - | NOT RUN | - |
| 396 | dc1-leaf1c | System | VerifyNTP | Verifies if NTP is synchronised. | - | NOT RUN | - |
| 397 | dc1-leaf1c | System | VerifyNTP | Verifies if NTP is synchronised. | - | NOT RUN | - |
| 398 | dc1-leaf1c | System | VerifyReloadCause | Verifies the last reload cause of the device. | - | NOT RUN | - |
| 399 | dc1-leaf1c | System | VerifyReloadCause | Verifies the last reload cause of the device. | - | NOT RUN | - |
| 400 | dc1-leaf1c | System | VerifyUptime | Verifies the device uptime. | - | NOT RUN | - |
| 401 | dc1-leaf1c | VLAN | VerifyVlanInternalPolicy | Verifies the VLAN internal allocation policy and the range of VLANs. | - | NOT RUN | - |
| 402 | dc1-leaf2a | AAA | VerifyAcctConsoleMethods | Verifies the AAA accounting console method lists for different accounting types (system, exec, commands, dot1x). | - | NOT RUN | - |
| 403 | dc1-leaf2a | AAA | VerifyAcctDefaultMethods | Verifies the AAA accounting default method lists for different accounting types (system, exec, commands, dot1x). | - | NOT RUN | - |
| 404 | dc1-leaf2a | AAA | VerifyAuthenMethods | Verifies the AAA authentication method lists for different authentication types (login, enable, dot1x). | - | NOT RUN | - |
| 405 | dc1-leaf2a | AAA | VerifyAuthzMethods | Verifies the AAA authorization method lists for different authorization types (commands, exec). | - | NOT RUN | - |
| 406 | dc1-leaf2a | AAA | VerifyTacacsServerGroups | Verifies if the provided TACACS server group(s) are configured. | - | NOT RUN | - |
| 407 | dc1-leaf2a | AAA | VerifyTacacsServers | Verifies TACACS servers are configured for a specified VRF. | - | NOT RUN | - |
| 408 | dc1-leaf2a | AAA | VerifyTacacsSourceIntf | Verifies TACACS source-interface for a specified VRF. | - | NOT RUN | - |
| 409 | dc1-leaf2a | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: dc1-spine1 (IP: 10.255.0.1) | NOT RUN | - |
| 410 | dc1-leaf2a | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: dc1-spine2 (IP: 10.255.0.2) | NOT RUN | - |
| 411 | dc1-leaf2a | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: dc2-leaf2a (IP: 10.255.128.15) | NOT RUN | - |
| 412 | dc1-leaf2a | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: dc1-spine1 (IP: 10.255.255.8) | NOT RUN | - |
| 413 | dc1-leaf2a | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: dc1-spine2 (IP: 10.255.255.10) | NOT RUN | - |
| 414 | dc1-leaf2a | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: dc2-leaf2a (IP: 192.168.100.1) | NOT RUN | - |
| 415 | dc1-leaf2a | Configuration | VerifyRunningConfigDiffs | Verifies there is no difference between the running-config and the startup-config | - | NOT RUN | - |
| 416 | dc1-leaf2a | Configuration | VerifyZeroTouch | Verifies ZeroTouch is disabled | - | NOT RUN | - |
| 417 | dc1-leaf2a | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet1 - Remote: dc1-spine1 Ethernet3 | NOT RUN | - |
| 418 | dc1-leaf2a | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet2 - Remote: dc1-spine2 Ethernet3 | NOT RUN | - |
| 419 | dc1-leaf2a | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet6 - Remote: dc2-leaf2a Ethernet6 | NOT RUN | - |
| 420 | dc1-leaf2a | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet8 - Remote: dc1-leaf2c Ethernet1 | NOT RUN | - |
| 421 | dc1-leaf2a | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.0.5) - Destination: dc1-leaf1a Loopback0 (IP: 10.255.0.3) | NOT RUN | - |
| 422 | dc1-leaf2a | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.0.5) - Destination: dc1-leaf1b Loopback0 (IP: 10.255.0.4) | NOT RUN | - |
| 423 | dc1-leaf2a | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.0.5) - Destination: dc1-leaf2a Loopback0 (IP: 10.255.0.5) | NOT RUN | - |
| 424 | dc1-leaf2a | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.0.5) - Destination: dc1-spine1 Loopback0 (IP: 10.255.0.1) | NOT RUN | - |
| 425 | dc1-leaf2a | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.0.5) - Destination: dc1-spine2 Loopback0 (IP: 10.255.0.2) | NOT RUN | - |
| 426 | dc1-leaf2a | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.0.5) - Destination: dc1-svc-leaf1a Loopback0 (IP: 10.33.0.5) | NOT RUN | - |
| 427 | dc1-leaf2a | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.0.5) - Destination: dc1-svc-leaf1b Loopback0 (IP: 10.33.0.6) | NOT RUN | - |
| 428 | dc1-leaf2a | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.0.5) - Destination: dc1-wan1 Loopback0 (IP: 10.255.2.1) | NOT RUN | - |
| 429 | dc1-leaf2a | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.0.5) - Destination: dc1-wan2 Loopback0 (IP: 10.255.2.2) | NOT RUN | - |
| 430 | dc1-leaf2a | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.0.5) - Destination: dc2-leaf1a Loopback0 (IP: 10.255.128.13) | NOT RUN | - |
| 431 | dc1-leaf2a | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.0.5) - Destination: dc2-leaf1b Loopback0 (IP: 10.255.128.14) | NOT RUN | - |
| 432 | dc1-leaf2a | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.0.5) - Destination: dc2-leaf2a Loopback0 (IP: 10.255.128.15) | NOT RUN | - |
| 433 | dc1-leaf2a | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.0.5) - Destination: dc2-leaf2b Loopback0 (IP: 10.255.128.16) | NOT RUN | - |
| 434 | dc1-leaf2a | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.0.5) - Destination: dc2-leaf3a.arista.com Loopback0 (IP: 10.255.128.17) | NOT RUN | - |
| 435 | dc1-leaf2a | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.0.5) - Destination: dc2-leaf3b.arista.com Loopback0 (IP: 10.255.128.18) | NOT RUN | - |
| 436 | dc1-leaf2a | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.0.5) - Destination: dc2-spine1 Loopback0 (IP: 10.255.128.11) | NOT RUN | - |
| 437 | dc1-leaf2a | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.0.5) - Destination: dc2-spine2 Loopback0 (IP: 10.255.128.12) | NOT RUN | - |
| 438 | dc1-leaf2a | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet1 (IP: 10.255.255.9) - Destination: dc1-spine1 Ethernet3 (IP: 10.255.255.8) | NOT RUN | - |
| 439 | dc1-leaf2a | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet2 (IP: 10.255.255.11) - Destination: dc1-spine2 Ethernet3 (IP: 10.255.255.10) | NOT RUN | - |
| 440 | dc1-leaf2a | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet6 (IP: 192.168.100.0) - Destination: dc2-leaf2a Ethernet6 (IP: 192.168.100.1) | NOT RUN | - |
| 441 | dc1-leaf2a | Field Notices | VerifyFieldNotice44Resolution | Verifies that the device is using the correct Aboot version per FN0044. | - | NOT RUN | - |
| 442 | dc1-leaf2a | Field Notices | VerifyFieldNotice72Resolution | Verifies if the device is exposed to FN0072, and if the issue has been mitigated. | - | NOT RUN | - |
| 443 | dc1-leaf2a | Greent | VerifyGreenT | Verifies if a GreenT policy is created. | - | NOT RUN | - |
| 444 | dc1-leaf2a | Greent | VerifyGreenTCounters | Verifies if the GreenT counters are incremented. | - | NOT RUN | - |
| 445 | dc1-leaf2a | Hardware | VerifyAdverseDrops | Verifies there are no adverse drops on DCS-7280 and DCS-7500 family switches. | - | NOT RUN | - |
| 446 | dc1-leaf2a | Hardware | VerifyEnvironmentCooling | Verifies the status of power supply fans and all fan trays. | - | NOT RUN | - |
| 447 | dc1-leaf2a | Hardware | VerifyEnvironmentCooling | Verifies the status of power supply fans and all fan trays. | Accepted States: 'ok' | NOT RUN | - |
| 448 | dc1-leaf2a | Hardware | VerifyEnvironmentPower | Verifies the power supplies status. | - | NOT RUN | - |
| 449 | dc1-leaf2a | Hardware | VerifyEnvironmentPower | Verifies the power supplies status. | Accepted States: 'ok' | NOT RUN | - |
| 450 | dc1-leaf2a | Hardware | VerifyEnvironmentSystemCooling | Verifies the system cooling status. | - | NOT RUN | - |
| 451 | dc1-leaf2a | Hardware | VerifyTemperature | Verifies the device temperature. | - | NOT RUN | - |
| 452 | dc1-leaf2a | Hardware | VerifyTemperature | Verifies the device temperature. | - | NOT RUN | - |
| 453 | dc1-leaf2a | Hardware | VerifyTransceiversManufacturers | Verifies if all transceivers come from approved manufacturers. | - | NOT RUN | - |
| 454 | dc1-leaf2a | Hardware | VerifyTransceiversManufacturers | Verifies if all transceivers come from approved manufacturers. | Accepted Manufacturers: 'Arista Networks', 'Arastra, Inc.', 'Not Present' | NOT RUN | - |
| 455 | dc1-leaf2a | Hardware | VerifyTransceiversTemperature | Verifies the transceivers temperature. | - | NOT RUN | - |
| 456 | dc1-leaf2a | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet1 - P2P_LINK_TO_DC1-SPINE1_Ethernet3 = 'up' | NOT RUN | - |
| 457 | dc1-leaf2a | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet2 - P2P_LINK_TO_DC1-SPINE2_Ethernet3 = 'up' | NOT RUN | - |
| 458 | dc1-leaf2a | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet3 - MLAG_dc1-leaf2b_Ethernet3 = 'up' | NOT RUN | - |
| 459 | dc1-leaf2a | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet4 - MLAG_dc1-leaf2b_Ethernet4 = 'up' | NOT RUN | - |
| 460 | dc1-leaf2a | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet5 - SERVER_dc1-leaf2-server1_PCI1 = 'up' | NOT RUN | - |
| 461 | dc1-leaf2a | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet6 - P2P_LINK_TO_dc2-leaf2a_Ethernet6 = 'up' | NOT RUN | - |
| 462 | dc1-leaf2a | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet8 - DC1-LEAF2C_Ethernet1 = 'up' | NOT RUN | - |
| 463 | dc1-leaf2a | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback0 - ROUTER_ID = 'up' | NOT RUN | - |
| 464 | dc1-leaf2a | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback1 - VXLAN_TUNNEL_SOURCE = 'up' | NOT RUN | - |
| 465 | dc1-leaf2a | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback10 - VRF10_VTEP_DIAGNOSTICS = 'up' | NOT RUN | - |
| 466 | dc1-leaf2a | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback11 - VRF11_VTEP_DIAGNOSTICS = 'up' | NOT RUN | - |
| 467 | dc1-leaf2a | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel3 - MLAG_dc1-leaf2b_Port-Channel3 = 'up' | NOT RUN | - |
| 468 | dc1-leaf2a | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel5 - SERVER_dc1-leaf2-server1_PortChannel dc1-leaf2-server1 = 'up' | NOT RUN | - |
| 469 | dc1-leaf2a | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel8 - DC1-LEAF2C_Po1 = 'up' | NOT RUN | - |
| 470 | dc1-leaf2a | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan11 - VRF10_VLAN11 = 'up' | NOT RUN | - |
| 471 | dc1-leaf2a | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan12 - VRF10_VLAN12 = 'up' | NOT RUN | - |
| 472 | dc1-leaf2a | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan21 - VRF11_VLAN21 = 'up' | NOT RUN | - |
| 473 | dc1-leaf2a | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan22 - VRF11_VLAN22 = 'up' | NOT RUN | - |
| 474 | dc1-leaf2a | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan3009 - MLAG_L3_VRF_VRF10 = 'up' | NOT RUN | - |
| 475 | dc1-leaf2a | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan3010 - MLAG_L3_VRF_VRF11 = 'up' | NOT RUN | - |
| 476 | dc1-leaf2a | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan4085 - Inband Management = 'up' | NOT RUN | - |
| 477 | dc1-leaf2a | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan4093 - MLAG_L3 = 'up' | NOT RUN | - |
| 478 | dc1-leaf2a | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan4094 - MLAG = 'up' | NOT RUN | - |
| 479 | dc1-leaf2a | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vxlan1 = 'up' | NOT RUN | - |
| 480 | dc1-leaf2a | LANZ | VerifyLANZ | Verifies if LANZ is enabled. | - | NOT RUN | - |
| 481 | dc1-leaf2a | MLAG | VerifyMlagStatus | Verifies the health status of the MLAG configuration. | - | NOT RUN | - |
| 482 | dc1-leaf2a | Profiles | VerifyTcamProfile | Verifies the device TCAM profile. | - | NOT RUN | - |
| 483 | dc1-leaf2a | Profiles | VerifyUnifiedForwardingTableMode | Verifies the device is using the expected UFT mode. | - | NOT RUN | - |
| 484 | dc1-leaf2a | PTP | VerifyPtpGMStatus | Verifies that the device is locked to a valid PTP Grandmaster. | - | NOT RUN | - |
| 485 | dc1-leaf2a | PTP | VerifyPtpLockStatus | Verifies that the device was locked to the upstream PTP GM in the last minute. | - | NOT RUN | - |
| 486 | dc1-leaf2a | PTP | VerifyPtpModeStatus | Verifies that the device is configured as a PTP Boundary Clock. | - | NOT RUN | - |
| 487 | dc1-leaf2a | PTP | VerifyPtpOffset | Verifies that the PTP timing offset is within +/- 1000ns from the master clock. | - | NOT RUN | - |
| 488 | dc1-leaf2a | PTP | VerifyPtpPortModeStatus | Verifies the PTP interfaces state. | - | NOT RUN | - |
| 489 | dc1-leaf2a | Routing | VerifyRoutingProtocolModel | Verifies the configured routing protocol model. | Routing protocol model: multi-agent | NOT RUN | - |
| 490 | dc1-leaf2a | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.0.1 - Peer: dc1-spine1 | NOT RUN | - |
| 491 | dc1-leaf2a | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.0.2 - Peer: dc1-spine2 | NOT RUN | - |
| 492 | dc1-leaf2a | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.0.3 - Peer: dc1-leaf1a | NOT RUN | - |
| 493 | dc1-leaf2a | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.0.4 - Peer: dc1-leaf1b | NOT RUN | - |
| 494 | dc1-leaf2a | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.0.5 - Peer: dc1-leaf2a | NOT RUN | - |
| 495 | dc1-leaf2a | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.1.3 - Peer: dc1-leaf1a | NOT RUN | - |
| 496 | dc1-leaf2a | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.1.5 - Peer: dc1-leaf2a | NOT RUN | - |
| 497 | dc1-leaf2a | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.128.11 - Peer: dc2-spine1 | NOT RUN | - |
| 498 | dc1-leaf2a | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.128.12 - Peer: dc2-spine2 | NOT RUN | - |
| 499 | dc1-leaf2a | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.128.13 - Peer: dc2-leaf1a | NOT RUN | - |
| 500 | dc1-leaf2a | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.128.14 - Peer: dc2-leaf1b | NOT RUN | - |
| 501 | dc1-leaf2a | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.128.15 - Peer: dc2-leaf2a | NOT RUN | - |
| 502 | dc1-leaf2a | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.128.16 - Peer: dc2-leaf2b | NOT RUN | - |
| 503 | dc1-leaf2a | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.128.17 - Peer: dc2-leaf3a.arista.com | NOT RUN | - |
| 504 | dc1-leaf2a | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.128.18 - Peer: dc2-leaf3b.arista.com | NOT RUN | - |
| 505 | dc1-leaf2a | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.129.13 - Peer: dc2-leaf1a | NOT RUN | - |
| 506 | dc1-leaf2a | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.129.15 - Peer: dc2-leaf2a | NOT RUN | - |
| 507 | dc1-leaf2a | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.129.17 - Peer: dc2-leaf3a.arista.com | NOT RUN | - |
| 508 | dc1-leaf2a | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.2.1 - Peer: dc1-wan1 | NOT RUN | - |
| 509 | dc1-leaf2a | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.2.2 - Peer: dc1-wan2 | NOT RUN | - |
| 510 | dc1-leaf2a | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.33.0.5 - Peer: dc1-svc-leaf1a | NOT RUN | - |
| 511 | dc1-leaf2a | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.33.0.6 - Peer: dc1-svc-leaf1b | NOT RUN | - |
| 512 | dc1-leaf2a | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.33.1.5 - Peer: dc1-svc-leaf1a | NOT RUN | - |
| 513 | dc1-leaf2a | Security | VerifyAPIHttpsSSL | Verifies if the eAPI has a valid SSL profile. | - | NOT RUN | - |
| 514 | dc1-leaf2a | Security | VerifyAPIHttpsSSL | Verifies if the eAPI has a valid SSL profile. | eAPI HTTPS SSL Profile: eAPI_SSL_Profile | NOT RUN | - |
| 515 | dc1-leaf2a | Security | VerifyAPIHttpStatus | Verifies if eAPI HTTP server is disabled globally. | - | NOT RUN | - |
| 516 | dc1-leaf2a | Security | VerifyAPIIPv4Acl | Verifies if eAPI has the right number IPv4 ACL(s) configured for a specified VRF. | - | NOT RUN | - |
| 517 | dc1-leaf2a | Security | VerifyAPIIPv6Acl | Verifies if eAPI has the right number IPv6 ACL(s) configured for a specified VRF. | - | NOT RUN | - |
| 518 | dc1-leaf2a | Security | VerifyAPISSLCertificate | Verifies the eAPI SSL certificate expiry, common subject name, encryption algorithm and key size. | - | NOT RUN | - |
| 519 | dc1-leaf2a | Security | VerifyBannerLogin | Verifies the login banner of a device. | - | NOT RUN | - |
| 520 | dc1-leaf2a | Security | VerifyBannerMotd | Verifies the motd banner of a device. | - | NOT RUN | - |
| 521 | dc1-leaf2a | Security | VerifyIPSecConnHealth | Verifies all IPv4 security connections. | - | NOT RUN | - |
| 522 | dc1-leaf2a | Security | VerifyIPv4ACL | Verifies the configuration of IPv4 ACLs. | - | NOT RUN | - |
| 523 | dc1-leaf2a | Security | VerifySpecificIPSecConn | Verifies IPv4 security connections for a peer. | - | NOT RUN | - |
| 524 | dc1-leaf2a | Security | VerifySSHIPv4Acl | Verifies if the SSHD agent has IPv4 ACL(s) configured. | - | NOT RUN | - |
| 525 | dc1-leaf2a | Security | VerifySSHIPv6Acl | Verifies if the SSHD agent has IPv6 ACL(s) configured. | - | NOT RUN | - |
| 526 | dc1-leaf2a | Security | VerifySSHStatus | Verifies if the SSHD agent is disabled in the default VRF. | - | NOT RUN | - |
| 527 | dc1-leaf2a | Security | VerifyTelnetStatus | Verifies if Telnet is disabled in the default VRF. | - | NOT RUN | - |
| 528 | dc1-leaf2a | Services | VerifyDNSLookup | Verifies the DNS name to IP address resolution. | - | NOT RUN | - |
| 529 | dc1-leaf2a | Services | VerifyDNSServers | Verifies if the DNS servers are correctly configured. | - | NOT RUN | - |
| 530 | dc1-leaf2a | Services | VerifyErrdisableRecovery | Verifies the errdisable recovery reason, status, and interval. | - | NOT RUN | - |
| 531 | dc1-leaf2a | Services | VerifyHostname | Verifies the hostname of a device. | - | NOT RUN | - |
| 532 | dc1-leaf2a | SNMP | VerifySnmpIPv4Acl | Verifies if the SNMP agent has IPv4 ACL(s) configured. | - | NOT RUN | - |
| 533 | dc1-leaf2a | SNMP | VerifySnmpIPv6Acl | Verifies if the SNMP agent has IPv6 ACL(s) configured. | - | NOT RUN | - |
| 534 | dc1-leaf2a | SNMP | VerifySnmpStatus | Verifies if the SNMP agent is enabled. | - | NOT RUN | - |
| 535 | dc1-leaf2a | Software | VerifyEOSExtensions | Verifies that all EOS extensions installed on the device are enabled for boot persistence. | - | NOT RUN | - |
| 536 | dc1-leaf2a | Software | VerifyEOSVersion | Verifies the EOS version of the device. | - | NOT RUN | - |
| 537 | dc1-leaf2a | Software | VerifyTerminAttrVersion | Verifies the TerminAttr version of the device. | - | NOT RUN | - |
| 538 | dc1-leaf2a | STUN | VerifyStunClient | Verifies the STUN client is configured with the specified IPv4 source address and port. Validate the public IP and port if provided. | - | NOT RUN | - |
| 539 | dc1-leaf2a | System | VerifyAgentLogs | Verifies there are no agent crash reports. | - | NOT RUN | - |
| 540 | dc1-leaf2a | System | VerifyCoredump | Verifies there are no core dump files. | - | NOT RUN | - |
| 541 | dc1-leaf2a | System | VerifyCPUUtilization | Verifies whether the CPU utilization is below 75%. | - | NOT RUN | - |
| 542 | dc1-leaf2a | System | VerifyFileSystemUtilization | Verifies that no partition is utilizing more than 75% of its disk space. | - | NOT RUN | - |
| 543 | dc1-leaf2a | System | VerifyMemoryUtilization | Verifies whether the memory utilization is below 75%. | - | NOT RUN | - |
| 544 | dc1-leaf2a | System | VerifyNTP | Verifies if NTP is synchronised. | - | NOT RUN | - |
| 545 | dc1-leaf2a | System | VerifyNTP | Verifies if NTP is synchronised. | - | NOT RUN | - |
| 546 | dc1-leaf2a | System | VerifyReloadCause | Verifies the last reload cause of the device. | - | NOT RUN | - |
| 547 | dc1-leaf2a | System | VerifyReloadCause | Verifies the last reload cause of the device. | - | NOT RUN | - |
| 548 | dc1-leaf2a | System | VerifyUptime | Verifies the device uptime. | - | NOT RUN | - |
| 549 | dc1-leaf2a | VLAN | VerifyVlanInternalPolicy | Verifies the VLAN internal allocation policy and the range of VLANs. | - | NOT RUN | - |
| 550 | dc1-leaf2c | AAA | VerifyAcctConsoleMethods | Verifies the AAA accounting console method lists for different accounting types (system, exec, commands, dot1x). | - | NOT RUN | - |
| 551 | dc1-leaf2c | AAA | VerifyAcctDefaultMethods | Verifies the AAA accounting default method lists for different accounting types (system, exec, commands, dot1x). | - | NOT RUN | - |
| 552 | dc1-leaf2c | AAA | VerifyAuthenMethods | Verifies the AAA authentication method lists for different authentication types (login, enable, dot1x). | - | NOT RUN | - |
| 553 | dc1-leaf2c | AAA | VerifyAuthzMethods | Verifies the AAA authorization method lists for different authorization types (commands, exec). | - | NOT RUN | - |
| 554 | dc1-leaf2c | AAA | VerifyTacacsServerGroups | Verifies if the provided TACACS server group(s) are configured. | - | NOT RUN | - |
| 555 | dc1-leaf2c | AAA | VerifyTacacsServers | Verifies TACACS servers are configured for a specified VRF. | - | NOT RUN | - |
| 556 | dc1-leaf2c | AAA | VerifyTacacsSourceIntf | Verifies TACACS source-interface for a specified VRF. | - | NOT RUN | - |
| 557 | dc1-leaf2c | Configuration | VerifyRunningConfigDiffs | Verifies there is no difference between the running-config and the startup-config | - | NOT RUN | - |
| 558 | dc1-leaf2c | Configuration | VerifyZeroTouch | Verifies ZeroTouch is disabled | - | NOT RUN | - |
| 559 | dc1-leaf2c | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet1 - Remote: dc1-leaf2a Ethernet8 | NOT RUN | - |
| 560 | dc1-leaf2c | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Inband MGMT SVI Vlan4085 (IP: 172.21.110.5) - Destination: dc1-leaf1a Loopback0 (IP: 10.255.0.3) | NOT RUN | - |
| 561 | dc1-leaf2c | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Inband MGMT SVI Vlan4085 (IP: 172.21.110.5) - Destination: dc1-leaf1b Loopback0 (IP: 10.255.0.4) | NOT RUN | - |
| 562 | dc1-leaf2c | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Inband MGMT SVI Vlan4085 (IP: 172.21.110.5) - Destination: dc1-leaf2a Loopback0 (IP: 10.255.0.5) | NOT RUN | - |
| 563 | dc1-leaf2c | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Inband MGMT SVI Vlan4085 (IP: 172.21.110.5) - Destination: dc1-spine1 Loopback0 (IP: 10.255.0.1) | NOT RUN | - |
| 564 | dc1-leaf2c | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Inband MGMT SVI Vlan4085 (IP: 172.21.110.5) - Destination: dc1-spine2 Loopback0 (IP: 10.255.0.2) | NOT RUN | - |
| 565 | dc1-leaf2c | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Inband MGMT SVI Vlan4085 (IP: 172.21.110.5) - Destination: dc1-svc-leaf1a Loopback0 (IP: 10.33.0.5) | NOT RUN | - |
| 566 | dc1-leaf2c | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Inband MGMT SVI Vlan4085 (IP: 172.21.110.5) - Destination: dc1-svc-leaf1b Loopback0 (IP: 10.33.0.6) | NOT RUN | - |
| 567 | dc1-leaf2c | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Inband MGMT SVI Vlan4085 (IP: 172.21.110.5) - Destination: dc1-wan1 Loopback0 (IP: 10.255.2.1) | NOT RUN | - |
| 568 | dc1-leaf2c | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Inband MGMT SVI Vlan4085 (IP: 172.21.110.5) - Destination: dc1-wan2 Loopback0 (IP: 10.255.2.2) | NOT RUN | - |
| 569 | dc1-leaf2c | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Inband MGMT SVI Vlan4085 (IP: 172.21.110.5) - Destination: dc2-leaf1a Loopback0 (IP: 10.255.128.13) | NOT RUN | - |
| 570 | dc1-leaf2c | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Inband MGMT SVI Vlan4085 (IP: 172.21.110.5) - Destination: dc2-leaf1b Loopback0 (IP: 10.255.128.14) | NOT RUN | - |
| 571 | dc1-leaf2c | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Inband MGMT SVI Vlan4085 (IP: 172.21.110.5) - Destination: dc2-leaf2a Loopback0 (IP: 10.255.128.15) | NOT RUN | - |
| 572 | dc1-leaf2c | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Inband MGMT SVI Vlan4085 (IP: 172.21.110.5) - Destination: dc2-leaf2b Loopback0 (IP: 10.255.128.16) | NOT RUN | - |
| 573 | dc1-leaf2c | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Inband MGMT SVI Vlan4085 (IP: 172.21.110.5) - Destination: dc2-leaf3a.arista.com Loopback0 (IP: 10.255.128.17) | NOT RUN | - |
| 574 | dc1-leaf2c | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Inband MGMT SVI Vlan4085 (IP: 172.21.110.5) - Destination: dc2-leaf3b.arista.com Loopback0 (IP: 10.255.128.18) | NOT RUN | - |
| 575 | dc1-leaf2c | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Inband MGMT SVI Vlan4085 (IP: 172.21.110.5) - Destination: dc2-spine1 Loopback0 (IP: 10.255.128.11) | NOT RUN | - |
| 576 | dc1-leaf2c | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Inband MGMT SVI Vlan4085 (IP: 172.21.110.5) - Destination: dc2-spine2 Loopback0 (IP: 10.255.128.12) | NOT RUN | - |
| 577 | dc1-leaf2c | Field Notices | VerifyFieldNotice44Resolution | Verifies that the device is using the correct Aboot version per FN0044. | - | NOT RUN | - |
| 578 | dc1-leaf2c | Field Notices | VerifyFieldNotice72Resolution | Verifies if the device is exposed to FN0072, and if the issue has been mitigated. | - | NOT RUN | - |
| 579 | dc1-leaf2c | Greent | VerifyGreenT | Verifies if a GreenT policy is created. | - | NOT RUN | - |
| 580 | dc1-leaf2c | Greent | VerifyGreenTCounters | Verifies if the GreenT counters are incremented. | - | NOT RUN | - |
| 581 | dc1-leaf2c | Hardware | VerifyAdverseDrops | Verifies there are no adverse drops on DCS-7280 and DCS-7500 family switches. | - | NOT RUN | - |
| 582 | dc1-leaf2c | Hardware | VerifyEnvironmentCooling | Verifies the status of power supply fans and all fan trays. | - | NOT RUN | - |
| 583 | dc1-leaf2c | Hardware | VerifyEnvironmentCooling | Verifies the status of power supply fans and all fan trays. | Accepted States: 'ok' | NOT RUN | - |
| 584 | dc1-leaf2c | Hardware | VerifyEnvironmentPower | Verifies the power supplies status. | - | NOT RUN | - |
| 585 | dc1-leaf2c | Hardware | VerifyEnvironmentPower | Verifies the power supplies status. | Accepted States: 'ok' | NOT RUN | - |
| 586 | dc1-leaf2c | Hardware | VerifyEnvironmentSystemCooling | Verifies the system cooling status. | - | NOT RUN | - |
| 587 | dc1-leaf2c | Hardware | VerifyTemperature | Verifies the device temperature. | - | NOT RUN | - |
| 588 | dc1-leaf2c | Hardware | VerifyTemperature | Verifies the device temperature. | - | NOT RUN | - |
| 589 | dc1-leaf2c | Hardware | VerifyTransceiversManufacturers | Verifies if all transceivers come from approved manufacturers. | - | NOT RUN | - |
| 590 | dc1-leaf2c | Hardware | VerifyTransceiversManufacturers | Verifies if all transceivers come from approved manufacturers. | Accepted Manufacturers: 'Arista Networks', 'Arastra, Inc.', 'Not Present' | NOT RUN | - |
| 591 | dc1-leaf2c | Hardware | VerifyTransceiversTemperature | Verifies the transceivers temperature. | - | NOT RUN | - |
| 592 | dc1-leaf2c | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet1 - DC1-LEAF2A_Ethernet8 = 'up' | NOT RUN | - |
| 593 | dc1-leaf2c | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet2 - DC1-LEAF2B_Ethernet8 = 'adminDown' | NOT RUN | - |
| 594 | dc1-leaf2c | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet5 - SERVER_dc1-leaf2-server1_iLO = 'up' | NOT RUN | - |
| 595 | dc1-leaf2c | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel1 - DC1_L3_LEAF2_Po8 = 'up' | NOT RUN | - |
| 596 | dc1-leaf2c | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan4085 - L2LEAF_INBAND_MGMT = 'up' | NOT RUN | - |
| 597 | dc1-leaf2c | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vxlan1 = 'up' | NOT RUN | - |
| 598 | dc1-leaf2c | LANZ | VerifyLANZ | Verifies if LANZ is enabled. | - | NOT RUN | - |
| 599 | dc1-leaf2c | PTP | VerifyPtpGMStatus | Verifies that the device is locked to a valid PTP Grandmaster. | - | NOT RUN | - |
| 600 | dc1-leaf2c | PTP | VerifyPtpLockStatus | Verifies that the device was locked to the upstream PTP GM in the last minute. | - | NOT RUN | - |
| 601 | dc1-leaf2c | PTP | VerifyPtpModeStatus | Verifies that the device is configured as a PTP Boundary Clock. | - | NOT RUN | - |
| 602 | dc1-leaf2c | PTP | VerifyPtpOffset | Verifies that the PTP timing offset is within +/- 1000ns from the master clock. | - | NOT RUN | - |
| 603 | dc1-leaf2c | PTP | VerifyPtpPortModeStatus | Verifies the PTP interfaces state. | - | NOT RUN | - |
| 604 | dc1-leaf2c | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.0.1 - Peer: dc1-spine1 | NOT RUN | - |
| 605 | dc1-leaf2c | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.0.2 - Peer: dc1-spine2 | NOT RUN | - |
| 606 | dc1-leaf2c | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.0.3 - Peer: dc1-leaf1a | NOT RUN | - |
| 607 | dc1-leaf2c | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.0.4 - Peer: dc1-leaf1b | NOT RUN | - |
| 608 | dc1-leaf2c | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.0.5 - Peer: dc1-leaf2a | NOT RUN | - |
| 609 | dc1-leaf2c | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.1.3 - Peer: dc1-leaf1a | NOT RUN | - |
| 610 | dc1-leaf2c | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.1.5 - Peer: dc1-leaf2a | NOT RUN | - |
| 611 | dc1-leaf2c | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.128.11 - Peer: dc2-spine1 | NOT RUN | - |
| 612 | dc1-leaf2c | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.128.12 - Peer: dc2-spine2 | NOT RUN | - |
| 613 | dc1-leaf2c | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.128.13 - Peer: dc2-leaf1a | NOT RUN | - |
| 614 | dc1-leaf2c | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.128.14 - Peer: dc2-leaf1b | NOT RUN | - |
| 615 | dc1-leaf2c | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.128.15 - Peer: dc2-leaf2a | NOT RUN | - |
| 616 | dc1-leaf2c | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.128.16 - Peer: dc2-leaf2b | NOT RUN | - |
| 617 | dc1-leaf2c | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.128.17 - Peer: dc2-leaf3a.arista.com | NOT RUN | - |
| 618 | dc1-leaf2c | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.128.18 - Peer: dc2-leaf3b.arista.com | NOT RUN | - |
| 619 | dc1-leaf2c | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.129.13 - Peer: dc2-leaf1a | NOT RUN | - |
| 620 | dc1-leaf2c | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.129.15 - Peer: dc2-leaf2a | NOT RUN | - |
| 621 | dc1-leaf2c | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.129.17 - Peer: dc2-leaf3a.arista.com | NOT RUN | - |
| 622 | dc1-leaf2c | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.2.1 - Peer: dc1-wan1 | NOT RUN | - |
| 623 | dc1-leaf2c | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.2.2 - Peer: dc1-wan2 | NOT RUN | - |
| 624 | dc1-leaf2c | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.33.0.5 - Peer: dc1-svc-leaf1a | NOT RUN | - |
| 625 | dc1-leaf2c | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.33.0.6 - Peer: dc1-svc-leaf1b | NOT RUN | - |
| 626 | dc1-leaf2c | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.33.1.5 - Peer: dc1-svc-leaf1a | NOT RUN | - |
| 627 | dc1-leaf2c | Security | VerifyAPIHttpsSSL | Verifies if the eAPI has a valid SSL profile. | - | NOT RUN | - |
| 628 | dc1-leaf2c | Security | VerifyAPIHttpsSSL | Verifies if the eAPI has a valid SSL profile. | eAPI HTTPS SSL Profile: eAPI_SSL_Profile | NOT RUN | - |
| 629 | dc1-leaf2c | Security | VerifyAPIHttpStatus | Verifies if eAPI HTTP server is disabled globally. | - | NOT RUN | - |
| 630 | dc1-leaf2c | Security | VerifyAPIIPv4Acl | Verifies if eAPI has the right number IPv4 ACL(s) configured for a specified VRF. | - | NOT RUN | - |
| 631 | dc1-leaf2c | Security | VerifyAPIIPv6Acl | Verifies if eAPI has the right number IPv6 ACL(s) configured for a specified VRF. | - | NOT RUN | - |
| 632 | dc1-leaf2c | Security | VerifyAPISSLCertificate | Verifies the eAPI SSL certificate expiry, common subject name, encryption algorithm and key size. | - | NOT RUN | - |
| 633 | dc1-leaf2c | Security | VerifyBannerLogin | Verifies the login banner of a device. | - | NOT RUN | - |
| 634 | dc1-leaf2c | Security | VerifyBannerMotd | Verifies the motd banner of a device. | - | NOT RUN | - |
| 635 | dc1-leaf2c | Security | VerifyIPSecConnHealth | Verifies all IPv4 security connections. | - | NOT RUN | - |
| 636 | dc1-leaf2c | Security | VerifyIPv4ACL | Verifies the configuration of IPv4 ACLs. | - | NOT RUN | - |
| 637 | dc1-leaf2c | Security | VerifySpecificIPSecConn | Verifies IPv4 security connections for a peer. | - | NOT RUN | - |
| 638 | dc1-leaf2c | Security | VerifySSHIPv4Acl | Verifies if the SSHD agent has IPv4 ACL(s) configured. | - | NOT RUN | - |
| 639 | dc1-leaf2c | Security | VerifySSHIPv6Acl | Verifies if the SSHD agent has IPv6 ACL(s) configured. | - | NOT RUN | - |
| 640 | dc1-leaf2c | Security | VerifySSHStatus | Verifies if the SSHD agent is disabled in the default VRF. | - | NOT RUN | - |
| 641 | dc1-leaf2c | Security | VerifyTelnetStatus | Verifies if Telnet is disabled in the default VRF. | - | NOT RUN | - |
| 642 | dc1-leaf2c | Services | VerifyDNSLookup | Verifies the DNS name to IP address resolution. | - | NOT RUN | - |
| 643 | dc1-leaf2c | Services | VerifyDNSServers | Verifies if the DNS servers are correctly configured. | - | NOT RUN | - |
| 644 | dc1-leaf2c | Services | VerifyErrdisableRecovery | Verifies the errdisable recovery reason, status, and interval. | - | NOT RUN | - |
| 645 | dc1-leaf2c | Services | VerifyHostname | Verifies the hostname of a device. | - | NOT RUN | - |
| 646 | dc1-leaf2c | SNMP | VerifySnmpIPv4Acl | Verifies if the SNMP agent has IPv4 ACL(s) configured. | - | NOT RUN | - |
| 647 | dc1-leaf2c | SNMP | VerifySnmpIPv6Acl | Verifies if the SNMP agent has IPv6 ACL(s) configured. | - | NOT RUN | - |
| 648 | dc1-leaf2c | SNMP | VerifySnmpStatus | Verifies if the SNMP agent is enabled. | - | NOT RUN | - |
| 649 | dc1-leaf2c | Software | VerifyEOSVersion | Verifies the EOS version of the device. | - | NOT RUN | - |
| 650 | dc1-leaf2c | Software | VerifyTerminAttrVersion | Verifies the TerminAttr version of the device. | - | NOT RUN | - |
| 651 | dc1-leaf2c | STUN | VerifyStunClient | Verifies the STUN client is configured with the specified IPv4 source address and port. Validate the public IP and port if provided. | - | NOT RUN | - |
| 652 | dc1-leaf2c | System | VerifyAgentLogs | Verifies there are no agent crash reports. | - | NOT RUN | - |
| 653 | dc1-leaf2c | System | VerifyCoredump | Verifies there are no core dump files. | - | NOT RUN | - |
| 654 | dc1-leaf2c | System | VerifyCPUUtilization | Verifies whether the CPU utilization is below 75%. | - | NOT RUN | - |
| 655 | dc1-leaf2c | System | VerifyFileSystemUtilization | Verifies that no partition is utilizing more than 75% of its disk space. | - | NOT RUN | - |
| 656 | dc1-leaf2c | System | VerifyMemoryUtilization | Verifies whether the memory utilization is below 75%. | - | NOT RUN | - |
| 657 | dc1-leaf2c | System | VerifyNTP | Verifies if NTP is synchronised. | - | NOT RUN | - |
| 658 | dc1-leaf2c | System | VerifyNTP | Verifies if NTP is synchronised. | - | NOT RUN | - |
| 659 | dc1-leaf2c | System | VerifyReloadCause | Verifies the last reload cause of the device. | - | NOT RUN | - |
| 660 | dc1-leaf2c | System | VerifyReloadCause | Verifies the last reload cause of the device. | - | NOT RUN | - |
| 661 | dc1-leaf2c | System | VerifyUptime | Verifies the device uptime. | - | NOT RUN | - |
| 662 | dc1-leaf2c | VLAN | VerifyVlanInternalPolicy | Verifies the VLAN internal allocation policy and the range of VLANs. | - | NOT RUN | - |
| 663 | dc1-spine1 | AAA | VerifyAcctConsoleMethods | Verifies the AAA accounting console method lists for different accounting types (system, exec, commands, dot1x). | - | NOT RUN | - |
| 664 | dc1-spine1 | AAA | VerifyAcctDefaultMethods | Verifies the AAA accounting default method lists for different accounting types (system, exec, commands, dot1x). | - | NOT RUN | - |
| 665 | dc1-spine1 | AAA | VerifyAuthenMethods | Verifies the AAA authentication method lists for different authentication types (login, enable, dot1x). | - | NOT RUN | - |
| 666 | dc1-spine1 | AAA | VerifyAuthzMethods | Verifies the AAA authorization method lists for different authorization types (commands, exec). | - | NOT RUN | - |
| 667 | dc1-spine1 | AAA | VerifyTacacsServerGroups | Verifies if the provided TACACS server group(s) are configured. | - | NOT RUN | - |
| 668 | dc1-spine1 | AAA | VerifyTacacsServers | Verifies TACACS servers are configured for a specified VRF. | - | NOT RUN | - |
| 669 | dc1-spine1 | AAA | VerifyTacacsSourceIntf | Verifies TACACS source-interface for a specified VRF. | - | NOT RUN | - |
| 670 | dc1-spine1 | BFD | VerifyBFDPeersHealth | Verifies the health of all IPv4 BFD peers. | - | NOT RUN | - |
| 671 | dc1-spine1 | BFD | VerifyBFDPeersIntervals | Verifies the timers of the IPv4 BFD peers in the specified VRF. | - | NOT RUN | - |
| 672 | dc1-spine1 | BFD | VerifyBFDSpecificPeers | Verifies the IPv4 BFD peer's sessions and remote disc in the specified VRF. | - | NOT RUN | - |
| 673 | dc1-spine1 | BGP | VerifyBGPAdvCommunities | Verifies the advertised communities of a BGP peer. | - | NOT RUN | - |
| 674 | dc1-spine1 | BGP | VerifyBGPExchangedRoutes | Verifies the advertised and received routes of BGP peers. | - | NOT RUN | - |
| 675 | dc1-spine1 | BGP | VerifyBGPPeerASNCap | Verifies the four octet asn capabilities of a BGP peer. | - | NOT RUN | - |
| 676 | dc1-spine1 | BGP | VerifyBGPPeerCount | Verifies the count of BGP peers. | - | NOT RUN | - |
| 677 | dc1-spine1 | BGP | VerifyBGPPeerMD5Auth | Verifies the MD5 authentication and state of a BGP peer. | - | NOT RUN | - |
| 678 | dc1-spine1 | BGP | VerifyBGPPeerMPCaps | Verifies the multiprotocol capabilities of a BGP peer. | - | NOT RUN | - |
| 679 | dc1-spine1 | BGP | VerifyBGPPeerRouteRefreshCap | Verifies the route refresh capabilities of a BGP peer. | - | NOT RUN | - |
| 680 | dc1-spine1 | BGP | VerifyBGPPeersHealth | Verifies the health of BGP peers | - | NOT RUN | - |
| 681 | dc1-spine1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | - | NOT RUN | - |
| 682 | dc1-spine1 | BGP | VerifyBGPTimers | Verifies the timers of a BGP peer. | - | NOT RUN | - |
| 683 | dc1-spine1 | BGP | VerifyEVPNType2Route | Verifies the EVPN Type-2 routes for a given IPv4 or MAC address and VNI. | - | NOT RUN | - |
| 684 | dc1-spine1 | Configuration | VerifyRunningConfigDiffs | Verifies there is no difference between the running-config and the startup-config | - | NOT RUN | - |
| 685 | dc1-spine1 | Configuration | VerifyZeroTouch | Verifies ZeroTouch is disabled | - | NOT RUN | - |
| 686 | dc1-spine1 | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet1 - Remote: dc1-leaf1a Ethernet1 | NOT RUN | - |
| 687 | dc1-spine1 | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet2 - Remote: dc1-leaf1b Ethernet1 | NOT RUN | - |
| 688 | dc1-spine1 | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet3 - Remote: dc1-leaf2a Ethernet1 | NOT RUN | - |
| 689 | dc1-spine1 | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet5 - Remote: dc1-svc-leaf1a Ethernet1 | NOT RUN | - |
| 690 | dc1-spine1 | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet6 - Remote: dc1-svc-leaf1b Ethernet1 | NOT RUN | - |
| 691 | dc1-spine1 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet1 (IP: 10.255.255.0) - Destination: dc1-leaf1a Ethernet1 (IP: 10.255.255.1) | NOT RUN | - |
| 692 | dc1-spine1 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet2 (IP: 10.255.255.4) - Destination: dc1-leaf1b Ethernet1 (IP: 10.255.255.5) | NOT RUN | - |
| 693 | dc1-spine1 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet3 (IP: 10.255.255.8) - Destination: dc1-leaf2a Ethernet1 (IP: 10.255.255.9) | NOT RUN | - |
| 694 | dc1-spine1 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet5 (IP: 10.33.255.16) - Destination: dc1-svc-leaf1a Ethernet1 (IP: 10.33.255.17) | NOT RUN | - |
| 695 | dc1-spine1 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet6 (IP: 10.33.255.20) - Destination: dc1-svc-leaf1b Ethernet1 (IP: 10.33.255.21) | NOT RUN | - |
| 696 | dc1-spine1 | Field Notices | VerifyFieldNotice44Resolution | Verifies that the device is using the correct Aboot version per FN0044. | - | NOT RUN | - |
| 697 | dc1-spine1 | Field Notices | VerifyFieldNotice72Resolution | Verifies if the device is exposed to FN0072, and if the issue has been mitigated. | - | NOT RUN | - |
| 698 | dc1-spine1 | Greent | VerifyGreenT | Verifies if a GreenT policy is created. | - | NOT RUN | - |
| 699 | dc1-spine1 | Greent | VerifyGreenTCounters | Verifies if the GreenT counters are incremented. | - | NOT RUN | - |
| 700 | dc1-spine1 | Hardware | VerifyAdverseDrops | Verifies there are no adverse drops on DCS-7280 and DCS-7500 family switches. | - | NOT RUN | - |
| 701 | dc1-spine1 | Hardware | VerifyEnvironmentCooling | Verifies the status of power supply fans and all fan trays. | - | NOT RUN | - |
| 702 | dc1-spine1 | Hardware | VerifyEnvironmentCooling | Verifies the status of power supply fans and all fan trays. | Accepted States: 'ok' | NOT RUN | - |
| 703 | dc1-spine1 | Hardware | VerifyEnvironmentPower | Verifies the power supplies status. | - | NOT RUN | - |
| 704 | dc1-spine1 | Hardware | VerifyEnvironmentPower | Verifies the power supplies status. | Accepted States: 'ok' | NOT RUN | - |
| 705 | dc1-spine1 | Hardware | VerifyEnvironmentSystemCooling | Verifies the system cooling status. | - | NOT RUN | - |
| 706 | dc1-spine1 | Hardware | VerifyTemperature | Verifies the device temperature. | - | NOT RUN | - |
| 707 | dc1-spine1 | Hardware | VerifyTemperature | Verifies the device temperature. | - | NOT RUN | - |
| 708 | dc1-spine1 | Hardware | VerifyTransceiversManufacturers | Verifies if all transceivers come from approved manufacturers. | - | NOT RUN | - |
| 709 | dc1-spine1 | Hardware | VerifyTransceiversManufacturers | Verifies if all transceivers come from approved manufacturers. | Accepted Manufacturers: 'Arista Networks', 'Arastra, Inc.', 'Not Present' | NOT RUN | - |
| 710 | dc1-spine1 | Hardware | VerifyTransceiversTemperature | Verifies the transceivers temperature. | - | NOT RUN | - |
| 711 | dc1-spine1 | Interfaces | VerifyIllegalLACP | Verifies there are no illegal LACP packets in all port channels. | - | NOT RUN | - |
| 712 | dc1-spine1 | Interfaces | VerifyInterfaceDiscards | Verifies there are no interface discard counters. | - | NOT RUN | - |
| 713 | dc1-spine1 | Interfaces | VerifyInterfaceErrDisabled | Verifies there are no interfaces in the errdisabled state. | - | NOT RUN | - |
| 714 | dc1-spine1 | Interfaces | VerifyInterfaceErrors | Verifies there are no interface error counters. | - | NOT RUN | - |
| 715 | dc1-spine1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | - | NOT RUN | - |
| 716 | dc1-spine1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet1 - P2P_LINK_TO_DC1-LEAF1A_Ethernet1 = 'up' | NOT RUN | - |
| 717 | dc1-spine1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet2 - P2P_LINK_TO_DC1-LEAF1B_Ethernet1 = 'up' | NOT RUN | - |
| 718 | dc1-spine1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet3 - P2P_LINK_TO_DC1-LEAF2A_Ethernet1 = 'up' | NOT RUN | - |
| 719 | dc1-spine1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet4 - P2P_LINK_TO_DC1-LEAF2B_Ethernet1 = 'adminDown' | NOT RUN | - |
| 720 | dc1-spine1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet5 - P2P_LINK_TO_DC1-SVC-LEAF1A_Ethernet1 = 'up' | NOT RUN | - |
| 721 | dc1-spine1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet6 - P2P_LINK_TO_DC1-SVC-LEAF1B_Ethernet1 = 'up' | NOT RUN | - |
| 722 | dc1-spine1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback0 - ROUTER_ID = 'up' | NOT RUN | - |
| 723 | dc1-spine1 | Interfaces | VerifyInterfaceUtilization | Verifies that the utilization of interfaces is below a certain threshold. | - | NOT RUN | - |
| 724 | dc1-spine1 | Interfaces | VerifyIPProxyARP | Verifies if Proxy ARP is enabled. | - | NOT RUN | - |
| 725 | dc1-spine1 | Interfaces | VerifyL2MTU | Verifies the global L2 MTU of all L2 interfaces. | - | NOT RUN | - |
| 726 | dc1-spine1 | Interfaces | VerifyL3MTU | Verifies the global L3 MTU of all L3 interfaces. | - | NOT RUN | - |
| 727 | dc1-spine1 | Interfaces | VerifyLoopbackCount | Verifies the number of loopback interfaces and their status. | - | NOT RUN | - |
| 728 | dc1-spine1 | Interfaces | VerifyPortChannels | Verifies there are no inactive ports in all port channels. | - | NOT RUN | - |
| 729 | dc1-spine1 | Interfaces | VerifyStormControlDrops | Verifies there are no interface storm-control drop counters. | - | NOT RUN | - |
| 730 | dc1-spine1 | Interfaces | VerifySVI | Verifies the status of all SVIs. | - | NOT RUN | - |
| 731 | dc1-spine1 | LANZ | VerifyLANZ | Verifies if LANZ is enabled. | - | NOT RUN | - |
| 732 | dc1-spine1 | OSPF | VerifyOSPFMaxLSA | Verifies all OSPF instances did not cross the maximum LSA threshold. | - | NOT RUN | - |
| 733 | dc1-spine1 | OSPF | VerifyOSPFNeighborCount | Verifies the number of OSPF neighbors in FULL state is the one we expect. | - | NOT RUN | - |
| 734 | dc1-spine1 | OSPF | VerifyOSPFNeighborState | Verifies all OSPF neighbors are in FULL state. | - | NOT RUN | - |
| 735 | dc1-spine1 | PTP | VerifyPtpGMStatus | Verifies that the device is locked to a valid PTP Grandmaster. | - | NOT RUN | - |
| 736 | dc1-spine1 | PTP | VerifyPtpLockStatus | Verifies that the device was locked to the upstream PTP GM in the last minute. | - | NOT RUN | - |
| 737 | dc1-spine1 | PTP | VerifyPtpModeStatus | Verifies that the device is configured as a PTP Boundary Clock. | - | NOT RUN | - |
| 738 | dc1-spine1 | PTP | VerifyPtpOffset | Verifies that the PTP timing offset is within +/- 1000ns from the master clock. | - | NOT RUN | - |
| 739 | dc1-spine1 | PTP | VerifyPtpPortModeStatus | Verifies the PTP interfaces state. | - | NOT RUN | - |
| 740 | dc1-spine1 | Routing | VerifyRoutingProtocolModel | Verifies the configured routing protocol model. | - | NOT RUN | - |
| 741 | dc1-spine1 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | - | NOT RUN | - |
| 742 | dc1-spine1 | Routing | VerifyRoutingTableSize | Verifies the size of the IP routing table of the default VRF. | - | NOT RUN | - |
| 743 | dc1-spine1 | Security | VerifyAPIHttpsSSL | Verifies if the eAPI has a valid SSL profile. | - | NOT RUN | - |
| 744 | dc1-spine1 | Security | VerifyAPIHttpsSSL | Verifies if the eAPI has a valid SSL profile. | eAPI HTTPS SSL Profile: eAPI_SSL_Profile | NOT RUN | - |
| 745 | dc1-spine1 | Security | VerifyAPIHttpStatus | Verifies if eAPI HTTP server is disabled globally. | - | NOT RUN | - |
| 746 | dc1-spine1 | Security | VerifyAPIIPv4Acl | Verifies if eAPI has the right number IPv4 ACL(s) configured for a specified VRF. | - | NOT RUN | - |
| 747 | dc1-spine1 | Security | VerifyAPIIPv6Acl | Verifies if eAPI has the right number IPv6 ACL(s) configured for a specified VRF. | - | NOT RUN | - |
| 748 | dc1-spine1 | Security | VerifyAPISSLCertificate | Verifies the eAPI SSL certificate expiry, common subject name, encryption algorithm and key size. | - | NOT RUN | - |
| 749 | dc1-spine1 | Security | VerifyBannerLogin | Verifies the login banner of a device. | - | NOT RUN | - |
| 750 | dc1-spine1 | Security | VerifyBannerMotd | Verifies the motd banner of a device. | - | NOT RUN | - |
| 751 | dc1-spine1 | Security | VerifyIPSecConnHealth | Verifies all IPv4 security connections. | - | NOT RUN | - |
| 752 | dc1-spine1 | Security | VerifyIPv4ACL | Verifies the configuration of IPv4 ACLs. | - | NOT RUN | - |
| 753 | dc1-spine1 | Security | VerifySpecificIPSecConn | Verifies IPv4 security connections for a peer. | - | NOT RUN | - |
| 754 | dc1-spine1 | Security | VerifySSHIPv4Acl | Verifies if the SSHD agent has IPv4 ACL(s) configured. | - | NOT RUN | - |
| 755 | dc1-spine1 | Security | VerifySSHIPv6Acl | Verifies if the SSHD agent has IPv6 ACL(s) configured. | - | NOT RUN | - |
| 756 | dc1-spine1 | Security | VerifySSHStatus | Verifies if the SSHD agent is disabled in the default VRF. | - | NOT RUN | - |
| 757 | dc1-spine1 | Security | VerifyTelnetStatus | Verifies if Telnet is disabled in the default VRF. | - | NOT RUN | - |
| 758 | dc1-spine1 | Services | VerifyDNSLookup | Verifies the DNS name to IP address resolution. | - | NOT RUN | - |
| 759 | dc1-spine1 | Services | VerifyDNSServers | Verifies if the DNS servers are correctly configured. | - | NOT RUN | - |
| 760 | dc1-spine1 | Services | VerifyErrdisableRecovery | Verifies the errdisable recovery reason, status, and interval. | - | NOT RUN | - |
| 761 | dc1-spine1 | Services | VerifyHostname | Verifies the hostname of a device. | - | NOT RUN | - |
| 762 | dc1-spine1 | SNMP | VerifySnmpIPv4Acl | Verifies if the SNMP agent has IPv4 ACL(s) configured. | - | NOT RUN | - |
| 763 | dc1-spine1 | SNMP | VerifySnmpIPv6Acl | Verifies if the SNMP agent has IPv6 ACL(s) configured. | - | NOT RUN | - |
| 764 | dc1-spine1 | SNMP | VerifySnmpStatus | Verifies if the SNMP agent is enabled. | - | NOT RUN | - |
| 765 | dc1-spine1 | Software | VerifyEOSVersion | Verifies the EOS version of the device. | - | NOT RUN | - |
| 766 | dc1-spine1 | Software | VerifyTerminAttrVersion | Verifies the TerminAttr version of the device. | - | NOT RUN | - |
| 767 | dc1-spine1 | STUN | VerifyStunClient | Verifies the STUN client is configured with the specified IPv4 source address and port. Validate the public IP and port if provided. | - | NOT RUN | - |
| 768 | dc1-spine1 | System | VerifyAgentLogs | Verifies there are no agent crash reports. | - | NOT RUN | - |
| 769 | dc1-spine1 | System | VerifyCoredump | Verifies there are no core dump files. | - | NOT RUN | - |
| 770 | dc1-spine1 | System | VerifyCPUUtilization | Verifies whether the CPU utilization is below 75%. | - | NOT RUN | - |
| 771 | dc1-spine1 | System | VerifyFileSystemUtilization | Verifies that no partition is utilizing more than 75% of its disk space. | - | NOT RUN | - |
| 772 | dc1-spine1 | System | VerifyMemoryUtilization | Verifies whether the memory utilization is below 75%. | - | NOT RUN | - |
| 773 | dc1-spine1 | System | VerifyNTP | Verifies if NTP is synchronised. | - | NOT RUN | - |
| 774 | dc1-spine1 | System | VerifyNTP | Verifies if NTP is synchronised. | - | NOT RUN | - |
| 775 | dc1-spine1 | System | VerifyReloadCause | Verifies the last reload cause of the device. | - | NOT RUN | - |
| 776 | dc1-spine1 | System | VerifyReloadCause | Verifies the last reload cause of the device. | - | NOT RUN | - |
| 777 | dc1-spine1 | System | VerifyUptime | Verifies the device uptime. | - | NOT RUN | - |
| 778 | dc1-spine1 | VLAN | VerifyVlanInternalPolicy | Verifies the VLAN internal allocation policy and the range of VLANs. | - | NOT RUN | - |
| 779 | dc1-spine2 | AAA | VerifyAcctConsoleMethods | Verifies the AAA accounting console method lists for different accounting types (system, exec, commands, dot1x). | - | NOT RUN | - |
| 780 | dc1-spine2 | AAA | VerifyAcctDefaultMethods | Verifies the AAA accounting default method lists for different accounting types (system, exec, commands, dot1x). | - | NOT RUN | - |
| 781 | dc1-spine2 | AAA | VerifyAuthenMethods | Verifies the AAA authentication method lists for different authentication types (login, enable, dot1x). | - | NOT RUN | - |
| 782 | dc1-spine2 | AAA | VerifyAuthzMethods | Verifies the AAA authorization method lists for different authorization types (commands, exec). | - | NOT RUN | - |
| 783 | dc1-spine2 | AAA | VerifyTacacsServerGroups | Verifies if the provided TACACS server group(s) are configured. | - | NOT RUN | - |
| 784 | dc1-spine2 | AAA | VerifyTacacsServers | Verifies TACACS servers are configured for a specified VRF. | - | NOT RUN | - |
| 785 | dc1-spine2 | AAA | VerifyTacacsSourceIntf | Verifies TACACS source-interface for a specified VRF. | - | NOT RUN | - |
| 786 | dc1-spine2 | BFD | VerifyBFDPeersHealth | Verifies the health of all IPv4 BFD peers. | - | NOT RUN | - |
| 787 | dc1-spine2 | BFD | VerifyBFDPeersIntervals | Verifies the timers of the IPv4 BFD peers in the specified VRF. | - | NOT RUN | - |
| 788 | dc1-spine2 | BFD | VerifyBFDSpecificPeers | Verifies the IPv4 BFD peer's sessions and remote disc in the specified VRF. | - | NOT RUN | - |
| 789 | dc1-spine2 | BGP | VerifyBGPAdvCommunities | Verifies the advertised communities of a BGP peer. | - | NOT RUN | - |
| 790 | dc1-spine2 | BGP | VerifyBGPExchangedRoutes | Verifies the advertised and received routes of BGP peers. | - | NOT RUN | - |
| 791 | dc1-spine2 | BGP | VerifyBGPPeerASNCap | Verifies the four octet asn capabilities of a BGP peer. | - | NOT RUN | - |
| 792 | dc1-spine2 | BGP | VerifyBGPPeerCount | Verifies the count of BGP peers. | - | NOT RUN | - |
| 793 | dc1-spine2 | BGP | VerifyBGPPeerMD5Auth | Verifies the MD5 authentication and state of a BGP peer. | - | NOT RUN | - |
| 794 | dc1-spine2 | BGP | VerifyBGPPeerMPCaps | Verifies the multiprotocol capabilities of a BGP peer. | - | NOT RUN | - |
| 795 | dc1-spine2 | BGP | VerifyBGPPeerRouteRefreshCap | Verifies the route refresh capabilities of a BGP peer. | - | NOT RUN | - |
| 796 | dc1-spine2 | BGP | VerifyBGPPeersHealth | Verifies the health of BGP peers | - | NOT RUN | - |
| 797 | dc1-spine2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | - | NOT RUN | - |
| 798 | dc1-spine2 | BGP | VerifyBGPTimers | Verifies the timers of a BGP peer. | - | NOT RUN | - |
| 799 | dc1-spine2 | BGP | VerifyEVPNType2Route | Verifies the EVPN Type-2 routes for a given IPv4 or MAC address and VNI. | - | NOT RUN | - |
| 800 | dc1-spine2 | Configuration | VerifyRunningConfigDiffs | Verifies there is no difference between the running-config and the startup-config | - | NOT RUN | - |
| 801 | dc1-spine2 | Configuration | VerifyZeroTouch | Verifies ZeroTouch is disabled | - | NOT RUN | - |
| 802 | dc1-spine2 | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet1 - Remote: dc1-leaf1a Ethernet2 | NOT RUN | - |
| 803 | dc1-spine2 | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet2 - Remote: dc1-leaf1b Ethernet2 | NOT RUN | - |
| 804 | dc1-spine2 | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet3 - Remote: dc1-leaf2a Ethernet2 | NOT RUN | - |
| 805 | dc1-spine2 | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet5 - Remote: dc1-svc-leaf1a Ethernet2 | NOT RUN | - |
| 806 | dc1-spine2 | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet6 - Remote: dc1-svc-leaf1b Ethernet2 | NOT RUN | - |
| 807 | dc1-spine2 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet1 (IP: 10.255.255.2) - Destination: dc1-leaf1a Ethernet2 (IP: 10.255.255.3) | NOT RUN | - |
| 808 | dc1-spine2 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet2 (IP: 10.255.255.6) - Destination: dc1-leaf1b Ethernet2 (IP: 10.255.255.7) | NOT RUN | - |
| 809 | dc1-spine2 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet3 (IP: 10.255.255.10) - Destination: dc1-leaf2a Ethernet2 (IP: 10.255.255.11) | NOT RUN | - |
| 810 | dc1-spine2 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet5 (IP: 10.33.255.18) - Destination: dc1-svc-leaf1a Ethernet2 (IP: 10.33.255.19) | NOT RUN | - |
| 811 | dc1-spine2 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet6 (IP: 10.33.255.22) - Destination: dc1-svc-leaf1b Ethernet2 (IP: 10.33.255.23) | NOT RUN | - |
| 812 | dc1-spine2 | Field Notices | VerifyFieldNotice44Resolution | Verifies that the device is using the correct Aboot version per FN0044. | - | NOT RUN | - |
| 813 | dc1-spine2 | Field Notices | VerifyFieldNotice72Resolution | Verifies if the device is exposed to FN0072, and if the issue has been mitigated. | - | NOT RUN | - |
| 814 | dc1-spine2 | Greent | VerifyGreenT | Verifies if a GreenT policy is created. | - | NOT RUN | - |
| 815 | dc1-spine2 | Greent | VerifyGreenTCounters | Verifies if the GreenT counters are incremented. | - | NOT RUN | - |
| 816 | dc1-spine2 | Hardware | VerifyAdverseDrops | Verifies there are no adverse drops on DCS-7280 and DCS-7500 family switches. | - | NOT RUN | - |
| 817 | dc1-spine2 | Hardware | VerifyEnvironmentCooling | Verifies the status of power supply fans and all fan trays. | - | NOT RUN | - |
| 818 | dc1-spine2 | Hardware | VerifyEnvironmentCooling | Verifies the status of power supply fans and all fan trays. | Accepted States: 'ok' | NOT RUN | - |
| 819 | dc1-spine2 | Hardware | VerifyEnvironmentPower | Verifies the power supplies status. | - | NOT RUN | - |
| 820 | dc1-spine2 | Hardware | VerifyEnvironmentPower | Verifies the power supplies status. | Accepted States: 'ok' | NOT RUN | - |
| 821 | dc1-spine2 | Hardware | VerifyEnvironmentSystemCooling | Verifies the system cooling status. | - | NOT RUN | - |
| 822 | dc1-spine2 | Hardware | VerifyTemperature | Verifies the device temperature. | - | NOT RUN | - |
| 823 | dc1-spine2 | Hardware | VerifyTemperature | Verifies the device temperature. | - | NOT RUN | - |
| 824 | dc1-spine2 | Hardware | VerifyTransceiversManufacturers | Verifies if all transceivers come from approved manufacturers. | - | NOT RUN | - |
| 825 | dc1-spine2 | Hardware | VerifyTransceiversManufacturers | Verifies if all transceivers come from approved manufacturers. | Accepted Manufacturers: 'Arista Networks', 'Arastra, Inc.', 'Not Present' | NOT RUN | - |
| 826 | dc1-spine2 | Hardware | VerifyTransceiversTemperature | Verifies the transceivers temperature. | - | NOT RUN | - |
| 827 | dc1-spine2 | Interfaces | VerifyIllegalLACP | Verifies there are no illegal LACP packets in all port channels. | - | NOT RUN | - |
| 828 | dc1-spine2 | Interfaces | VerifyInterfaceDiscards | Verifies there are no interface discard counters. | - | NOT RUN | - |
| 829 | dc1-spine2 | Interfaces | VerifyInterfaceErrDisabled | Verifies there are no interfaces in the errdisabled state. | - | NOT RUN | - |
| 830 | dc1-spine2 | Interfaces | VerifyInterfaceErrors | Verifies there are no interface error counters. | - | NOT RUN | - |
| 831 | dc1-spine2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | - | NOT RUN | - |
| 832 | dc1-spine2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet1 - P2P_LINK_TO_DC1-LEAF1A_Ethernet2 = 'up' | NOT RUN | - |
| 833 | dc1-spine2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet2 - P2P_LINK_TO_DC1-LEAF1B_Ethernet2 = 'up' | NOT RUN | - |
| 834 | dc1-spine2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet3 - P2P_LINK_TO_DC1-LEAF2A_Ethernet2 = 'up' | NOT RUN | - |
| 835 | dc1-spine2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet4 - P2P_LINK_TO_DC1-LEAF2B_Ethernet2 = 'adminDown' | NOT RUN | - |
| 836 | dc1-spine2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet5 - P2P_LINK_TO_DC1-SVC-LEAF1A_Ethernet2 = 'up' | NOT RUN | - |
| 837 | dc1-spine2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet6 - P2P_LINK_TO_DC1-SVC-LEAF1B_Ethernet2 = 'up' | NOT RUN | - |
| 838 | dc1-spine2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback0 - ROUTER_ID = 'up' | NOT RUN | - |
| 839 | dc1-spine2 | Interfaces | VerifyInterfaceUtilization | Verifies that the utilization of interfaces is below a certain threshold. | - | NOT RUN | - |
| 840 | dc1-spine2 | Interfaces | VerifyIPProxyARP | Verifies if Proxy ARP is enabled. | - | NOT RUN | - |
| 841 | dc1-spine2 | Interfaces | VerifyL2MTU | Verifies the global L2 MTU of all L2 interfaces. | - | NOT RUN | - |
| 842 | dc1-spine2 | Interfaces | VerifyL3MTU | Verifies the global L3 MTU of all L3 interfaces. | - | NOT RUN | - |
| 843 | dc1-spine2 | Interfaces | VerifyLoopbackCount | Verifies the number of loopback interfaces and their status. | - | NOT RUN | - |
| 844 | dc1-spine2 | Interfaces | VerifyPortChannels | Verifies there are no inactive ports in all port channels. | - | NOT RUN | - |
| 845 | dc1-spine2 | Interfaces | VerifyStormControlDrops | Verifies there are no interface storm-control drop counters. | - | NOT RUN | - |
| 846 | dc1-spine2 | Interfaces | VerifySVI | Verifies the status of all SVIs. | - | NOT RUN | - |
| 847 | dc1-spine2 | LANZ | VerifyLANZ | Verifies if LANZ is enabled. | - | NOT RUN | - |
| 848 | dc1-spine2 | OSPF | VerifyOSPFMaxLSA | Verifies all OSPF instances did not cross the maximum LSA threshold. | - | NOT RUN | - |
| 849 | dc1-spine2 | OSPF | VerifyOSPFNeighborCount | Verifies the number of OSPF neighbors in FULL state is the one we expect. | - | NOT RUN | - |
| 850 | dc1-spine2 | OSPF | VerifyOSPFNeighborState | Verifies all OSPF neighbors are in FULL state. | - | NOT RUN | - |
| 851 | dc1-spine2 | PTP | VerifyPtpGMStatus | Verifies that the device is locked to a valid PTP Grandmaster. | - | NOT RUN | - |
| 852 | dc1-spine2 | PTP | VerifyPtpLockStatus | Verifies that the device was locked to the upstream PTP GM in the last minute. | - | NOT RUN | - |
| 853 | dc1-spine2 | PTP | VerifyPtpModeStatus | Verifies that the device is configured as a PTP Boundary Clock. | - | NOT RUN | - |
| 854 | dc1-spine2 | PTP | VerifyPtpOffset | Verifies that the PTP timing offset is within +/- 1000ns from the master clock. | - | NOT RUN | - |
| 855 | dc1-spine2 | PTP | VerifyPtpPortModeStatus | Verifies the PTP interfaces state. | - | NOT RUN | - |
| 856 | dc1-spine2 | Routing | VerifyRoutingProtocolModel | Verifies the configured routing protocol model. | - | NOT RUN | - |
| 857 | dc1-spine2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | - | NOT RUN | - |
| 858 | dc1-spine2 | Routing | VerifyRoutingTableSize | Verifies the size of the IP routing table of the default VRF. | - | NOT RUN | - |
| 859 | dc1-spine2 | Security | VerifyAPIHttpsSSL | Verifies if the eAPI has a valid SSL profile. | - | NOT RUN | - |
| 860 | dc1-spine2 | Security | VerifyAPIHttpsSSL | Verifies if the eAPI has a valid SSL profile. | eAPI HTTPS SSL Profile: eAPI_SSL_Profile | NOT RUN | - |
| 861 | dc1-spine2 | Security | VerifyAPIHttpStatus | Verifies if eAPI HTTP server is disabled globally. | - | NOT RUN | - |
| 862 | dc1-spine2 | Security | VerifyAPIIPv4Acl | Verifies if eAPI has the right number IPv4 ACL(s) configured for a specified VRF. | - | NOT RUN | - |
| 863 | dc1-spine2 | Security | VerifyAPIIPv6Acl | Verifies if eAPI has the right number IPv6 ACL(s) configured for a specified VRF. | - | NOT RUN | - |
| 864 | dc1-spine2 | Security | VerifyAPISSLCertificate | Verifies the eAPI SSL certificate expiry, common subject name, encryption algorithm and key size. | - | NOT RUN | - |
| 865 | dc1-spine2 | Security | VerifyBannerLogin | Verifies the login banner of a device. | - | NOT RUN | - |
| 866 | dc1-spine2 | Security | VerifyBannerMotd | Verifies the motd banner of a device. | - | NOT RUN | - |
| 867 | dc1-spine2 | Security | VerifyIPSecConnHealth | Verifies all IPv4 security connections. | - | NOT RUN | - |
| 868 | dc1-spine2 | Security | VerifyIPv4ACL | Verifies the configuration of IPv4 ACLs. | - | NOT RUN | - |
| 869 | dc1-spine2 | Security | VerifySpecificIPSecConn | Verifies IPv4 security connections for a peer. | - | NOT RUN | - |
| 870 | dc1-spine2 | Security | VerifySSHIPv4Acl | Verifies if the SSHD agent has IPv4 ACL(s) configured. | - | NOT RUN | - |
| 871 | dc1-spine2 | Security | VerifySSHIPv6Acl | Verifies if the SSHD agent has IPv6 ACL(s) configured. | - | NOT RUN | - |
| 872 | dc1-spine2 | Security | VerifySSHStatus | Verifies if the SSHD agent is disabled in the default VRF. | - | NOT RUN | - |
| 873 | dc1-spine2 | Security | VerifyTelnetStatus | Verifies if Telnet is disabled in the default VRF. | - | NOT RUN | - |
| 874 | dc1-spine2 | Services | VerifyDNSLookup | Verifies the DNS name to IP address resolution. | - | NOT RUN | - |
| 875 | dc1-spine2 | Services | VerifyDNSServers | Verifies if the DNS servers are correctly configured. | - | NOT RUN | - |
| 876 | dc1-spine2 | Services | VerifyErrdisableRecovery | Verifies the errdisable recovery reason, status, and interval. | - | NOT RUN | - |
| 877 | dc1-spine2 | Services | VerifyHostname | Verifies the hostname of a device. | - | NOT RUN | - |
| 878 | dc1-spine2 | SNMP | VerifySnmpIPv4Acl | Verifies if the SNMP agent has IPv4 ACL(s) configured. | - | NOT RUN | - |
| 879 | dc1-spine2 | SNMP | VerifySnmpIPv6Acl | Verifies if the SNMP agent has IPv6 ACL(s) configured. | - | NOT RUN | - |
| 880 | dc1-spine2 | SNMP | VerifySnmpStatus | Verifies if the SNMP agent is enabled. | - | NOT RUN | - |
| 881 | dc1-spine2 | Software | VerifyEOSVersion | Verifies the EOS version of the device. | - | NOT RUN | - |
| 882 | dc1-spine2 | Software | VerifyTerminAttrVersion | Verifies the TerminAttr version of the device. | - | NOT RUN | - |
| 883 | dc1-spine2 | STUN | VerifyStunClient | Verifies the STUN client is configured with the specified IPv4 source address and port. Validate the public IP and port if provided. | - | NOT RUN | - |
| 884 | dc1-spine2 | System | VerifyAgentLogs | Verifies there are no agent crash reports. | - | NOT RUN | - |
| 885 | dc1-spine2 | System | VerifyCoredump | Verifies there are no core dump files. | - | NOT RUN | - |
| 886 | dc1-spine2 | System | VerifyCPUUtilization | Verifies whether the CPU utilization is below 75%. | - | NOT RUN | - |
| 887 | dc1-spine2 | System | VerifyFileSystemUtilization | Verifies that no partition is utilizing more than 75% of its disk space. | - | NOT RUN | - |
| 888 | dc1-spine2 | System | VerifyMemoryUtilization | Verifies whether the memory utilization is below 75%. | - | NOT RUN | - |
| 889 | dc1-spine2 | System | VerifyNTP | Verifies if NTP is synchronised. | - | NOT RUN | - |
| 890 | dc1-spine2 | System | VerifyNTP | Verifies if NTP is synchronised. | - | NOT RUN | - |
| 891 | dc1-spine2 | System | VerifyReloadCause | Verifies the last reload cause of the device. | - | NOT RUN | - |
| 892 | dc1-spine2 | System | VerifyReloadCause | Verifies the last reload cause of the device. | - | NOT RUN | - |
| 893 | dc1-spine2 | System | VerifyUptime | Verifies the device uptime. | - | NOT RUN | - |
| 894 | dc1-spine2 | VLAN | VerifyVlanInternalPolicy | Verifies the VLAN internal allocation policy and the range of VLANs. | - | NOT RUN | - |
| 895 | dc1-svc-leaf1a | AAA | VerifyAcctConsoleMethods | Verifies the AAA accounting console method lists for different accounting types (system, exec, commands, dot1x). | - | NOT RUN | - |
| 896 | dc1-svc-leaf1a | AAA | VerifyAcctDefaultMethods | Verifies the AAA accounting default method lists for different accounting types (system, exec, commands, dot1x). | - | NOT RUN | - |
| 897 | dc1-svc-leaf1a | AAA | VerifyAuthenMethods | Verifies the AAA authentication method lists for different authentication types (login, enable, dot1x). | - | NOT RUN | - |
| 898 | dc1-svc-leaf1a | AAA | VerifyAuthzMethods | Verifies the AAA authorization method lists for different authorization types (commands, exec). | - | NOT RUN | - |
| 899 | dc1-svc-leaf1a | AAA | VerifyTacacsServerGroups | Verifies if the provided TACACS server group(s) are configured. | - | NOT RUN | - |
| 900 | dc1-svc-leaf1a | AAA | VerifyTacacsServers | Verifies TACACS servers are configured for a specified VRF. | - | NOT RUN | - |
| 901 | dc1-svc-leaf1a | AAA | VerifyTacacsSourceIntf | Verifies TACACS source-interface for a specified VRF. | - | NOT RUN | - |
| 902 | dc1-svc-leaf1a | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: dc1-spine1 (IP: 10.255.0.1) | NOT RUN | - |
| 903 | dc1-svc-leaf1a | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: dc1-spine2 (IP: 10.255.0.2) | NOT RUN | - |
| 904 | dc1-svc-leaf1a | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: dc1-spine1 (IP: 10.33.255.16) | NOT RUN | - |
| 905 | dc1-svc-leaf1a | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: dc1-spine2 (IP: 10.33.255.18) | NOT RUN | - |
| 906 | dc1-svc-leaf1a | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: dc1-svc-leaf1b (IP: 10.33.1.105) | NOT RUN | - |
| 907 | dc1-svc-leaf1a | Configuration | VerifyRunningConfigDiffs | Verifies there is no difference between the running-config and the startup-config | - | NOT RUN | - |
| 908 | dc1-svc-leaf1a | Configuration | VerifyZeroTouch | Verifies ZeroTouch is disabled | - | NOT RUN | - |
| 909 | dc1-svc-leaf1a | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet1 - Remote: dc1-spine1 Ethernet5 | NOT RUN | - |
| 910 | dc1-svc-leaf1a | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet2 - Remote: dc1-spine2 Ethernet5 | NOT RUN | - |
| 911 | dc1-svc-leaf1a | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet3 - Remote: dc1-svc-leaf1b Ethernet3 | NOT RUN | - |
| 912 | dc1-svc-leaf1a | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet4 - Remote: dc1-svc-leaf1b Ethernet4 | NOT RUN | - |
| 913 | dc1-svc-leaf1a | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.33.0.5) - Destination: dc1-leaf1a Loopback0 (IP: 10.255.0.3) | NOT RUN | - |
| 914 | dc1-svc-leaf1a | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.33.0.5) - Destination: dc1-leaf1b Loopback0 (IP: 10.255.0.4) | NOT RUN | - |
| 915 | dc1-svc-leaf1a | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.33.0.5) - Destination: dc1-leaf2a Loopback0 (IP: 10.255.0.5) | NOT RUN | - |
| 916 | dc1-svc-leaf1a | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.33.0.5) - Destination: dc1-spine1 Loopback0 (IP: 10.255.0.1) | NOT RUN | - |
| 917 | dc1-svc-leaf1a | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.33.0.5) - Destination: dc1-spine2 Loopback0 (IP: 10.255.0.2) | NOT RUN | - |
| 918 | dc1-svc-leaf1a | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.33.0.5) - Destination: dc1-svc-leaf1a Loopback0 (IP: 10.33.0.5) | NOT RUN | - |
| 919 | dc1-svc-leaf1a | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.33.0.5) - Destination: dc1-svc-leaf1b Loopback0 (IP: 10.33.0.6) | NOT RUN | - |
| 920 | dc1-svc-leaf1a | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.33.0.5) - Destination: dc1-wan1 Loopback0 (IP: 10.255.2.1) | NOT RUN | - |
| 921 | dc1-svc-leaf1a | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.33.0.5) - Destination: dc1-wan2 Loopback0 (IP: 10.255.2.2) | NOT RUN | - |
| 922 | dc1-svc-leaf1a | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.33.0.5) - Destination: dc2-leaf1a Loopback0 (IP: 10.255.128.13) | NOT RUN | - |
| 923 | dc1-svc-leaf1a | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.33.0.5) - Destination: dc2-leaf1b Loopback0 (IP: 10.255.128.14) | NOT RUN | - |
| 924 | dc1-svc-leaf1a | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.33.0.5) - Destination: dc2-leaf2a Loopback0 (IP: 10.255.128.15) | NOT RUN | - |
| 925 | dc1-svc-leaf1a | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.33.0.5) - Destination: dc2-leaf2b Loopback0 (IP: 10.255.128.16) | NOT RUN | - |
| 926 | dc1-svc-leaf1a | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.33.0.5) - Destination: dc2-leaf3a.arista.com Loopback0 (IP: 10.255.128.17) | NOT RUN | - |
| 927 | dc1-svc-leaf1a | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.33.0.5) - Destination: dc2-leaf3b.arista.com Loopback0 (IP: 10.255.128.18) | NOT RUN | - |
| 928 | dc1-svc-leaf1a | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.33.0.5) - Destination: dc2-spine1 Loopback0 (IP: 10.255.128.11) | NOT RUN | - |
| 929 | dc1-svc-leaf1a | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.33.0.5) - Destination: dc2-spine2 Loopback0 (IP: 10.255.128.12) | NOT RUN | - |
| 930 | dc1-svc-leaf1a | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet1 (IP: 10.33.255.17) - Destination: dc1-spine1 Ethernet5 (IP: 10.33.255.16) | NOT RUN | - |
| 931 | dc1-svc-leaf1a | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet2 (IP: 10.33.255.19) - Destination: dc1-spine2 Ethernet5 (IP: 10.33.255.18) | NOT RUN | - |
| 932 | dc1-svc-leaf1a | Field Notices | VerifyFieldNotice44Resolution | Verifies that the device is using the correct Aboot version per FN0044. | - | NOT RUN | - |
| 933 | dc1-svc-leaf1a | Field Notices | VerifyFieldNotice72Resolution | Verifies if the device is exposed to FN0072, and if the issue has been mitigated. | - | NOT RUN | - |
| 934 | dc1-svc-leaf1a | Greent | VerifyGreenT | Verifies if a GreenT policy is created. | - | NOT RUN | - |
| 935 | dc1-svc-leaf1a | Greent | VerifyGreenTCounters | Verifies if the GreenT counters are incremented. | - | NOT RUN | - |
| 936 | dc1-svc-leaf1a | Hardware | VerifyAdverseDrops | Verifies there are no adverse drops on DCS-7280 and DCS-7500 family switches. | - | NOT RUN | - |
| 937 | dc1-svc-leaf1a | Hardware | VerifyEnvironmentCooling | Verifies the status of power supply fans and all fan trays. | - | NOT RUN | - |
| 938 | dc1-svc-leaf1a | Hardware | VerifyEnvironmentCooling | Verifies the status of power supply fans and all fan trays. | Accepted States: 'ok' | NOT RUN | - |
| 939 | dc1-svc-leaf1a | Hardware | VerifyEnvironmentPower | Verifies the power supplies status. | - | NOT RUN | - |
| 940 | dc1-svc-leaf1a | Hardware | VerifyEnvironmentPower | Verifies the power supplies status. | Accepted States: 'ok' | NOT RUN | - |
| 941 | dc1-svc-leaf1a | Hardware | VerifyEnvironmentSystemCooling | Verifies the system cooling status. | - | NOT RUN | - |
| 942 | dc1-svc-leaf1a | Hardware | VerifyTemperature | Verifies the device temperature. | - | NOT RUN | - |
| 943 | dc1-svc-leaf1a | Hardware | VerifyTemperature | Verifies the device temperature. | - | NOT RUN | - |
| 944 | dc1-svc-leaf1a | Hardware | VerifyTransceiversManufacturers | Verifies if all transceivers come from approved manufacturers. | - | NOT RUN | - |
| 945 | dc1-svc-leaf1a | Hardware | VerifyTransceiversManufacturers | Verifies if all transceivers come from approved manufacturers. | Accepted Manufacturers: 'Arista Networks', 'Arastra, Inc.', 'Not Present' | NOT RUN | - |
| 946 | dc1-svc-leaf1a | Hardware | VerifyTransceiversTemperature | Verifies the transceivers temperature. | - | NOT RUN | - |
| 947 | dc1-svc-leaf1a | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet1 - P2P_LINK_TO_DC1-SPINE1_Ethernet5 = 'up' | NOT RUN | - |
| 948 | dc1-svc-leaf1a | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet2 - P2P_LINK_TO_DC1-SPINE2_Ethernet5 = 'up' | NOT RUN | - |
| 949 | dc1-svc-leaf1a | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet3 - MLAG_dc1-svc-leaf1b_Ethernet3 = 'up' | NOT RUN | - |
| 950 | dc1-svc-leaf1a | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet4 - MLAG_dc1-svc-leaf1b_Ethernet4 = 'up' | NOT RUN | - |
| 951 | dc1-svc-leaf1a | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback0 - ROUTER_ID = 'up' | NOT RUN | - |
| 952 | dc1-svc-leaf1a | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback1 - VXLAN_TUNNEL_SOURCE = 'up' | NOT RUN | - |
| 953 | dc1-svc-leaf1a | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel3 - MLAG_dc1-svc-leaf1b_Port-Channel3 = 'up' | NOT RUN | - |
| 954 | dc1-svc-leaf1a | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan4093 - MLAG_L3 = 'up' | NOT RUN | - |
| 955 | dc1-svc-leaf1a | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan4094 - MLAG = 'up' | NOT RUN | - |
| 956 | dc1-svc-leaf1a | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vxlan1 = 'up' | NOT RUN | - |
| 957 | dc1-svc-leaf1a | LANZ | VerifyLANZ | Verifies if LANZ is enabled. | - | NOT RUN | - |
| 958 | dc1-svc-leaf1a | MLAG | VerifyMlagStatus | Verifies the health status of the MLAG configuration. | - | NOT RUN | - |
| 959 | dc1-svc-leaf1a | PTP | VerifyPtpGMStatus | Verifies that the device is locked to a valid PTP Grandmaster. | - | NOT RUN | - |
| 960 | dc1-svc-leaf1a | PTP | VerifyPtpLockStatus | Verifies that the device was locked to the upstream PTP GM in the last minute. | - | NOT RUN | - |
| 961 | dc1-svc-leaf1a | PTP | VerifyPtpModeStatus | Verifies that the device is configured as a PTP Boundary Clock. | - | NOT RUN | - |
| 962 | dc1-svc-leaf1a | PTP | VerifyPtpOffset | Verifies that the PTP timing offset is within +/- 1000ns from the master clock. | - | NOT RUN | - |
| 963 | dc1-svc-leaf1a | PTP | VerifyPtpPortModeStatus | Verifies the PTP interfaces state. | - | NOT RUN | - |
| 964 | dc1-svc-leaf1a | Routing | VerifyRoutingProtocolModel | Verifies the configured routing protocol model. | Routing protocol model: multi-agent | NOT RUN | - |
| 965 | dc1-svc-leaf1a | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.0.1 - Peer: dc1-spine1 | NOT RUN | - |
| 966 | dc1-svc-leaf1a | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.0.2 - Peer: dc1-spine2 | NOT RUN | - |
| 967 | dc1-svc-leaf1a | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.0.3 - Peer: dc1-leaf1a | NOT RUN | - |
| 968 | dc1-svc-leaf1a | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.0.4 - Peer: dc1-leaf1b | NOT RUN | - |
| 969 | dc1-svc-leaf1a | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.0.5 - Peer: dc1-leaf2a | NOT RUN | - |
| 970 | dc1-svc-leaf1a | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.1.3 - Peer: dc1-leaf1a | NOT RUN | - |
| 971 | dc1-svc-leaf1a | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.1.5 - Peer: dc1-leaf2a | NOT RUN | - |
| 972 | dc1-svc-leaf1a | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.128.11 - Peer: dc2-spine1 | NOT RUN | - |
| 973 | dc1-svc-leaf1a | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.128.12 - Peer: dc2-spine2 | NOT RUN | - |
| 974 | dc1-svc-leaf1a | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.128.13 - Peer: dc2-leaf1a | NOT RUN | - |
| 975 | dc1-svc-leaf1a | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.128.14 - Peer: dc2-leaf1b | NOT RUN | - |
| 976 | dc1-svc-leaf1a | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.128.15 - Peer: dc2-leaf2a | NOT RUN | - |
| 977 | dc1-svc-leaf1a | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.128.16 - Peer: dc2-leaf2b | NOT RUN | - |
| 978 | dc1-svc-leaf1a | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.128.17 - Peer: dc2-leaf3a.arista.com | NOT RUN | - |
| 979 | dc1-svc-leaf1a | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.128.18 - Peer: dc2-leaf3b.arista.com | NOT RUN | - |
| 980 | dc1-svc-leaf1a | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.129.13 - Peer: dc2-leaf1a | NOT RUN | - |
| 981 | dc1-svc-leaf1a | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.129.15 - Peer: dc2-leaf2a | NOT RUN | - |
| 982 | dc1-svc-leaf1a | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.129.17 - Peer: dc2-leaf3a.arista.com | NOT RUN | - |
| 983 | dc1-svc-leaf1a | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.2.1 - Peer: dc1-wan1 | NOT RUN | - |
| 984 | dc1-svc-leaf1a | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.2.2 - Peer: dc1-wan2 | NOT RUN | - |
| 985 | dc1-svc-leaf1a | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.33.0.5 - Peer: dc1-svc-leaf1a | NOT RUN | - |
| 986 | dc1-svc-leaf1a | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.33.0.6 - Peer: dc1-svc-leaf1b | NOT RUN | - |
| 987 | dc1-svc-leaf1a | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.33.1.5 - Peer: dc1-svc-leaf1a | NOT RUN | - |
| 988 | dc1-svc-leaf1a | Security | VerifyAPIHttpsSSL | Verifies if the eAPI has a valid SSL profile. | - | NOT RUN | - |
| 989 | dc1-svc-leaf1a | Security | VerifyAPIHttpsSSL | Verifies if the eAPI has a valid SSL profile. | eAPI HTTPS SSL Profile: eAPI_SSL_Profile | NOT RUN | - |
| 990 | dc1-svc-leaf1a | Security | VerifyAPIHttpStatus | Verifies if eAPI HTTP server is disabled globally. | - | NOT RUN | - |
| 991 | dc1-svc-leaf1a | Security | VerifyAPIIPv4Acl | Verifies if eAPI has the right number IPv4 ACL(s) configured for a specified VRF. | - | NOT RUN | - |
| 992 | dc1-svc-leaf1a | Security | VerifyAPIIPv6Acl | Verifies if eAPI has the right number IPv6 ACL(s) configured for a specified VRF. | - | NOT RUN | - |
| 993 | dc1-svc-leaf1a | Security | VerifyAPISSLCertificate | Verifies the eAPI SSL certificate expiry, common subject name, encryption algorithm and key size. | - | NOT RUN | - |
| 994 | dc1-svc-leaf1a | Security | VerifyBannerLogin | Verifies the login banner of a device. | - | NOT RUN | - |
| 995 | dc1-svc-leaf1a | Security | VerifyBannerMotd | Verifies the motd banner of a device. | - | NOT RUN | - |
| 996 | dc1-svc-leaf1a | Security | VerifyIPSecConnHealth | Verifies all IPv4 security connections. | - | NOT RUN | - |
| 997 | dc1-svc-leaf1a | Security | VerifyIPv4ACL | Verifies the configuration of IPv4 ACLs. | - | NOT RUN | - |
| 998 | dc1-svc-leaf1a | Security | VerifySpecificIPSecConn | Verifies IPv4 security connections for a peer. | - | NOT RUN | - |
| 999 | dc1-svc-leaf1a | Security | VerifySSHIPv4Acl | Verifies if the SSHD agent has IPv4 ACL(s) configured. | - | NOT RUN | - |
| 1000 | dc1-svc-leaf1a | Security | VerifySSHIPv6Acl | Verifies if the SSHD agent has IPv6 ACL(s) configured. | - | NOT RUN | - |
| 1001 | dc1-svc-leaf1a | Security | VerifySSHStatus | Verifies if the SSHD agent is disabled in the default VRF. | - | NOT RUN | - |
| 1002 | dc1-svc-leaf1a | Security | VerifyTelnetStatus | Verifies if Telnet is disabled in the default VRF. | - | NOT RUN | - |
| 1003 | dc1-svc-leaf1a | Services | VerifyDNSLookup | Verifies the DNS name to IP address resolution. | - | NOT RUN | - |
| 1004 | dc1-svc-leaf1a | Services | VerifyDNSServers | Verifies if the DNS servers are correctly configured. | - | NOT RUN | - |
| 1005 | dc1-svc-leaf1a | Services | VerifyErrdisableRecovery | Verifies the errdisable recovery reason, status, and interval. | - | NOT RUN | - |
| 1006 | dc1-svc-leaf1a | Services | VerifyHostname | Verifies the hostname of a device. | - | NOT RUN | - |
| 1007 | dc1-svc-leaf1a | SNMP | VerifySnmpIPv4Acl | Verifies if the SNMP agent has IPv4 ACL(s) configured. | - | NOT RUN | - |
| 1008 | dc1-svc-leaf1a | SNMP | VerifySnmpIPv6Acl | Verifies if the SNMP agent has IPv6 ACL(s) configured. | - | NOT RUN | - |
| 1009 | dc1-svc-leaf1a | SNMP | VerifySnmpStatus | Verifies if the SNMP agent is enabled. | - | NOT RUN | - |
| 1010 | dc1-svc-leaf1a | Software | VerifyEOSVersion | Verifies the EOS version of the device. | - | NOT RUN | - |
| 1011 | dc1-svc-leaf1a | Software | VerifyTerminAttrVersion | Verifies the TerminAttr version of the device. | - | NOT RUN | - |
| 1012 | dc1-svc-leaf1a | STUN | VerifyStunClient | Verifies the STUN client is configured with the specified IPv4 source address and port. Validate the public IP and port if provided. | - | NOT RUN | - |
| 1013 | dc1-svc-leaf1a | System | VerifyAgentLogs | Verifies there are no agent crash reports. | - | NOT RUN | - |
| 1014 | dc1-svc-leaf1a | System | VerifyCoredump | Verifies there are no core dump files. | - | NOT RUN | - |
| 1015 | dc1-svc-leaf1a | System | VerifyCPUUtilization | Verifies whether the CPU utilization is below 75%. | - | NOT RUN | - |
| 1016 | dc1-svc-leaf1a | System | VerifyFileSystemUtilization | Verifies that no partition is utilizing more than 75% of its disk space. | - | NOT RUN | - |
| 1017 | dc1-svc-leaf1a | System | VerifyMemoryUtilization | Verifies whether the memory utilization is below 75%. | - | NOT RUN | - |
| 1018 | dc1-svc-leaf1a | System | VerifyNTP | Verifies if NTP is synchronised. | - | NOT RUN | - |
| 1019 | dc1-svc-leaf1a | System | VerifyNTP | Verifies if NTP is synchronised. | - | NOT RUN | - |
| 1020 | dc1-svc-leaf1a | System | VerifyReloadCause | Verifies the last reload cause of the device. | - | NOT RUN | - |
| 1021 | dc1-svc-leaf1a | System | VerifyReloadCause | Verifies the last reload cause of the device. | - | NOT RUN | - |
| 1022 | dc1-svc-leaf1a | System | VerifyUptime | Verifies the device uptime. | - | NOT RUN | - |
| 1023 | dc1-svc-leaf1a | VLAN | VerifyVlanInternalPolicy | Verifies the VLAN internal allocation policy and the range of VLANs. | - | NOT RUN | - |
| 1024 | dc1-svc-leaf1b | AAA | VerifyAcctConsoleMethods | Verifies the AAA accounting console method lists for different accounting types (system, exec, commands, dot1x). | - | NOT RUN | - |
| 1025 | dc1-svc-leaf1b | AAA | VerifyAcctDefaultMethods | Verifies the AAA accounting default method lists for different accounting types (system, exec, commands, dot1x). | - | NOT RUN | - |
| 1026 | dc1-svc-leaf1b | AAA | VerifyAuthenMethods | Verifies the AAA authentication method lists for different authentication types (login, enable, dot1x). | - | NOT RUN | - |
| 1027 | dc1-svc-leaf1b | AAA | VerifyAuthzMethods | Verifies the AAA authorization method lists for different authorization types (commands, exec). | - | NOT RUN | - |
| 1028 | dc1-svc-leaf1b | AAA | VerifyTacacsServerGroups | Verifies if the provided TACACS server group(s) are configured. | - | NOT RUN | - |
| 1029 | dc1-svc-leaf1b | AAA | VerifyTacacsServers | Verifies TACACS servers are configured for a specified VRF. | - | NOT RUN | - |
| 1030 | dc1-svc-leaf1b | AAA | VerifyTacacsSourceIntf | Verifies TACACS source-interface for a specified VRF. | - | NOT RUN | - |
| 1031 | dc1-svc-leaf1b | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: dc1-spine1 (IP: 10.255.0.1) | NOT RUN | - |
| 1032 | dc1-svc-leaf1b | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: dc1-spine2 (IP: 10.255.0.2) | NOT RUN | - |
| 1033 | dc1-svc-leaf1b | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: dc1-spine1 (IP: 10.33.255.20) | NOT RUN | - |
| 1034 | dc1-svc-leaf1b | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: dc1-spine2 (IP: 10.33.255.22) | NOT RUN | - |
| 1035 | dc1-svc-leaf1b | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: dc1-svc-leaf1a (IP: 10.33.1.104) | NOT RUN | - |
| 1036 | dc1-svc-leaf1b | Configuration | VerifyRunningConfigDiffs | Verifies there is no difference between the running-config and the startup-config | - | NOT RUN | - |
| 1037 | dc1-svc-leaf1b | Configuration | VerifyZeroTouch | Verifies ZeroTouch is disabled | - | NOT RUN | - |
| 1038 | dc1-svc-leaf1b | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet1 - Remote: dc1-spine1 Ethernet6 | NOT RUN | - |
| 1039 | dc1-svc-leaf1b | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet2 - Remote: dc1-spine2 Ethernet6 | NOT RUN | - |
| 1040 | dc1-svc-leaf1b | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet3 - Remote: dc1-svc-leaf1a Ethernet3 | NOT RUN | - |
| 1041 | dc1-svc-leaf1b | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet4 - Remote: dc1-svc-leaf1a Ethernet4 | NOT RUN | - |
| 1042 | dc1-svc-leaf1b | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.33.0.6) - Destination: dc1-leaf1a Loopback0 (IP: 10.255.0.3) | NOT RUN | - |
| 1043 | dc1-svc-leaf1b | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.33.0.6) - Destination: dc1-leaf1b Loopback0 (IP: 10.255.0.4) | NOT RUN | - |
| 1044 | dc1-svc-leaf1b | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.33.0.6) - Destination: dc1-leaf2a Loopback0 (IP: 10.255.0.5) | NOT RUN | - |
| 1045 | dc1-svc-leaf1b | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.33.0.6) - Destination: dc1-spine1 Loopback0 (IP: 10.255.0.1) | NOT RUN | - |
| 1046 | dc1-svc-leaf1b | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.33.0.6) - Destination: dc1-spine2 Loopback0 (IP: 10.255.0.2) | NOT RUN | - |
| 1047 | dc1-svc-leaf1b | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.33.0.6) - Destination: dc1-svc-leaf1a Loopback0 (IP: 10.33.0.5) | NOT RUN | - |
| 1048 | dc1-svc-leaf1b | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.33.0.6) - Destination: dc1-svc-leaf1b Loopback0 (IP: 10.33.0.6) | NOT RUN | - |
| 1049 | dc1-svc-leaf1b | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.33.0.6) - Destination: dc1-wan1 Loopback0 (IP: 10.255.2.1) | NOT RUN | - |
| 1050 | dc1-svc-leaf1b | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.33.0.6) - Destination: dc1-wan2 Loopback0 (IP: 10.255.2.2) | NOT RUN | - |
| 1051 | dc1-svc-leaf1b | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.33.0.6) - Destination: dc2-leaf1a Loopback0 (IP: 10.255.128.13) | NOT RUN | - |
| 1052 | dc1-svc-leaf1b | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.33.0.6) - Destination: dc2-leaf1b Loopback0 (IP: 10.255.128.14) | NOT RUN | - |
| 1053 | dc1-svc-leaf1b | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.33.0.6) - Destination: dc2-leaf2a Loopback0 (IP: 10.255.128.15) | NOT RUN | - |
| 1054 | dc1-svc-leaf1b | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.33.0.6) - Destination: dc2-leaf2b Loopback0 (IP: 10.255.128.16) | NOT RUN | - |
| 1055 | dc1-svc-leaf1b | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.33.0.6) - Destination: dc2-leaf3a.arista.com Loopback0 (IP: 10.255.128.17) | NOT RUN | - |
| 1056 | dc1-svc-leaf1b | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.33.0.6) - Destination: dc2-leaf3b.arista.com Loopback0 (IP: 10.255.128.18) | NOT RUN | - |
| 1057 | dc1-svc-leaf1b | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.33.0.6) - Destination: dc2-spine1 Loopback0 (IP: 10.255.128.11) | NOT RUN | - |
| 1058 | dc1-svc-leaf1b | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.33.0.6) - Destination: dc2-spine2 Loopback0 (IP: 10.255.128.12) | NOT RUN | - |
| 1059 | dc1-svc-leaf1b | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet1 (IP: 10.33.255.21) - Destination: dc1-spine1 Ethernet6 (IP: 10.33.255.20) | NOT RUN | - |
| 1060 | dc1-svc-leaf1b | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet2 (IP: 10.33.255.23) - Destination: dc1-spine2 Ethernet6 (IP: 10.33.255.22) | NOT RUN | - |
| 1061 | dc1-svc-leaf1b | Field Notices | VerifyFieldNotice44Resolution | Verifies that the device is using the correct Aboot version per FN0044. | - | NOT RUN | - |
| 1062 | dc1-svc-leaf1b | Field Notices | VerifyFieldNotice72Resolution | Verifies if the device is exposed to FN0072, and if the issue has been mitigated. | - | NOT RUN | - |
| 1063 | dc1-svc-leaf1b | Greent | VerifyGreenT | Verifies if a GreenT policy is created. | - | NOT RUN | - |
| 1064 | dc1-svc-leaf1b | Greent | VerifyGreenTCounters | Verifies if the GreenT counters are incremented. | - | NOT RUN | - |
| 1065 | dc1-svc-leaf1b | Hardware | VerifyAdverseDrops | Verifies there are no adverse drops on DCS-7280 and DCS-7500 family switches. | - | NOT RUN | - |
| 1066 | dc1-svc-leaf1b | Hardware | VerifyEnvironmentCooling | Verifies the status of power supply fans and all fan trays. | - | NOT RUN | - |
| 1067 | dc1-svc-leaf1b | Hardware | VerifyEnvironmentCooling | Verifies the status of power supply fans and all fan trays. | Accepted States: 'ok' | NOT RUN | - |
| 1068 | dc1-svc-leaf1b | Hardware | VerifyEnvironmentPower | Verifies the power supplies status. | - | NOT RUN | - |
| 1069 | dc1-svc-leaf1b | Hardware | VerifyEnvironmentPower | Verifies the power supplies status. | Accepted States: 'ok' | NOT RUN | - |
| 1070 | dc1-svc-leaf1b | Hardware | VerifyEnvironmentSystemCooling | Verifies the system cooling status. | - | NOT RUN | - |
| 1071 | dc1-svc-leaf1b | Hardware | VerifyTemperature | Verifies the device temperature. | - | NOT RUN | - |
| 1072 | dc1-svc-leaf1b | Hardware | VerifyTemperature | Verifies the device temperature. | - | NOT RUN | - |
| 1073 | dc1-svc-leaf1b | Hardware | VerifyTransceiversManufacturers | Verifies if all transceivers come from approved manufacturers. | - | NOT RUN | - |
| 1074 | dc1-svc-leaf1b | Hardware | VerifyTransceiversManufacturers | Verifies if all transceivers come from approved manufacturers. | Accepted Manufacturers: 'Arista Networks', 'Arastra, Inc.', 'Not Present' | NOT RUN | - |
| 1075 | dc1-svc-leaf1b | Hardware | VerifyTransceiversTemperature | Verifies the transceivers temperature. | - | NOT RUN | - |
| 1076 | dc1-svc-leaf1b | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet1 - P2P_LINK_TO_DC1-SPINE1_Ethernet6 = 'up' | NOT RUN | - |
| 1077 | dc1-svc-leaf1b | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet2 - P2P_LINK_TO_DC1-SPINE2_Ethernet6 = 'up' | NOT RUN | - |
| 1078 | dc1-svc-leaf1b | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet3 - MLAG_dc1-svc-leaf1a_Ethernet3 = 'up' | NOT RUN | - |
| 1079 | dc1-svc-leaf1b | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet4 - MLAG_dc1-svc-leaf1a_Ethernet4 = 'up' | NOT RUN | - |
| 1080 | dc1-svc-leaf1b | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback0 - ROUTER_ID = 'up' | NOT RUN | - |
| 1081 | dc1-svc-leaf1b | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback1 - VXLAN_TUNNEL_SOURCE = 'up' | NOT RUN | - |
| 1082 | dc1-svc-leaf1b | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel3 - MLAG_dc1-svc-leaf1a_Port-Channel3 = 'up' | NOT RUN | - |
| 1083 | dc1-svc-leaf1b | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan4093 - MLAG_L3 = 'up' | NOT RUN | - |
| 1084 | dc1-svc-leaf1b | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan4094 - MLAG = 'up' | NOT RUN | - |
| 1085 | dc1-svc-leaf1b | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vxlan1 = 'up' | NOT RUN | - |
| 1086 | dc1-svc-leaf1b | LANZ | VerifyLANZ | Verifies if LANZ is enabled. | - | NOT RUN | - |
| 1087 | dc1-svc-leaf1b | MLAG | VerifyMlagStatus | Verifies the health status of the MLAG configuration. | - | NOT RUN | - |
| 1088 | dc1-svc-leaf1b | PTP | VerifyPtpGMStatus | Verifies that the device is locked to a valid PTP Grandmaster. | - | NOT RUN | - |
| 1089 | dc1-svc-leaf1b | PTP | VerifyPtpLockStatus | Verifies that the device was locked to the upstream PTP GM in the last minute. | - | NOT RUN | - |
| 1090 | dc1-svc-leaf1b | PTP | VerifyPtpModeStatus | Verifies that the device is configured as a PTP Boundary Clock. | - | NOT RUN | - |
| 1091 | dc1-svc-leaf1b | PTP | VerifyPtpOffset | Verifies that the PTP timing offset is within +/- 1000ns from the master clock. | - | NOT RUN | - |
| 1092 | dc1-svc-leaf1b | PTP | VerifyPtpPortModeStatus | Verifies the PTP interfaces state. | - | NOT RUN | - |
| 1093 | dc1-svc-leaf1b | Routing | VerifyRoutingProtocolModel | Verifies the configured routing protocol model. | Routing protocol model: multi-agent | NOT RUN | - |
| 1094 | dc1-svc-leaf1b | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.0.1 - Peer: dc1-spine1 | NOT RUN | - |
| 1095 | dc1-svc-leaf1b | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.0.2 - Peer: dc1-spine2 | NOT RUN | - |
| 1096 | dc1-svc-leaf1b | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.0.3 - Peer: dc1-leaf1a | NOT RUN | - |
| 1097 | dc1-svc-leaf1b | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.0.4 - Peer: dc1-leaf1b | NOT RUN | - |
| 1098 | dc1-svc-leaf1b | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.0.5 - Peer: dc1-leaf2a | NOT RUN | - |
| 1099 | dc1-svc-leaf1b | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.1.3 - Peer: dc1-leaf1a | NOT RUN | - |
| 1100 | dc1-svc-leaf1b | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.1.5 - Peer: dc1-leaf2a | NOT RUN | - |
| 1101 | dc1-svc-leaf1b | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.128.11 - Peer: dc2-spine1 | NOT RUN | - |
| 1102 | dc1-svc-leaf1b | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.128.12 - Peer: dc2-spine2 | NOT RUN | - |
| 1103 | dc1-svc-leaf1b | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.128.13 - Peer: dc2-leaf1a | NOT RUN | - |
| 1104 | dc1-svc-leaf1b | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.128.14 - Peer: dc2-leaf1b | NOT RUN | - |
| 1105 | dc1-svc-leaf1b | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.128.15 - Peer: dc2-leaf2a | NOT RUN | - |
| 1106 | dc1-svc-leaf1b | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.128.16 - Peer: dc2-leaf2b | NOT RUN | - |
| 1107 | dc1-svc-leaf1b | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.128.17 - Peer: dc2-leaf3a.arista.com | NOT RUN | - |
| 1108 | dc1-svc-leaf1b | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.128.18 - Peer: dc2-leaf3b.arista.com | NOT RUN | - |
| 1109 | dc1-svc-leaf1b | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.129.13 - Peer: dc2-leaf1a | NOT RUN | - |
| 1110 | dc1-svc-leaf1b | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.129.15 - Peer: dc2-leaf2a | NOT RUN | - |
| 1111 | dc1-svc-leaf1b | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.129.17 - Peer: dc2-leaf3a.arista.com | NOT RUN | - |
| 1112 | dc1-svc-leaf1b | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.2.1 - Peer: dc1-wan1 | NOT RUN | - |
| 1113 | dc1-svc-leaf1b | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.2.2 - Peer: dc1-wan2 | NOT RUN | - |
| 1114 | dc1-svc-leaf1b | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.33.0.5 - Peer: dc1-svc-leaf1a | NOT RUN | - |
| 1115 | dc1-svc-leaf1b | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.33.0.6 - Peer: dc1-svc-leaf1b | NOT RUN | - |
| 1116 | dc1-svc-leaf1b | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.33.1.5 - Peer: dc1-svc-leaf1a | NOT RUN | - |
| 1117 | dc1-svc-leaf1b | Security | VerifyAPIHttpsSSL | Verifies if the eAPI has a valid SSL profile. | - | NOT RUN | - |
| 1118 | dc1-svc-leaf1b | Security | VerifyAPIHttpsSSL | Verifies if the eAPI has a valid SSL profile. | eAPI HTTPS SSL Profile: eAPI_SSL_Profile | NOT RUN | - |
| 1119 | dc1-svc-leaf1b | Security | VerifyAPIHttpStatus | Verifies if eAPI HTTP server is disabled globally. | - | NOT RUN | - |
| 1120 | dc1-svc-leaf1b | Security | VerifyAPIIPv4Acl | Verifies if eAPI has the right number IPv4 ACL(s) configured for a specified VRF. | - | NOT RUN | - |
| 1121 | dc1-svc-leaf1b | Security | VerifyAPIIPv6Acl | Verifies if eAPI has the right number IPv6 ACL(s) configured for a specified VRF. | - | NOT RUN | - |
| 1122 | dc1-svc-leaf1b | Security | VerifyAPISSLCertificate | Verifies the eAPI SSL certificate expiry, common subject name, encryption algorithm and key size. | - | NOT RUN | - |
| 1123 | dc1-svc-leaf1b | Security | VerifyBannerLogin | Verifies the login banner of a device. | - | NOT RUN | - |
| 1124 | dc1-svc-leaf1b | Security | VerifyBannerMotd | Verifies the motd banner of a device. | - | NOT RUN | - |
| 1125 | dc1-svc-leaf1b | Security | VerifyIPSecConnHealth | Verifies all IPv4 security connections. | - | NOT RUN | - |
| 1126 | dc1-svc-leaf1b | Security | VerifyIPv4ACL | Verifies the configuration of IPv4 ACLs. | - | NOT RUN | - |
| 1127 | dc1-svc-leaf1b | Security | VerifySpecificIPSecConn | Verifies IPv4 security connections for a peer. | - | NOT RUN | - |
| 1128 | dc1-svc-leaf1b | Security | VerifySSHIPv4Acl | Verifies if the SSHD agent has IPv4 ACL(s) configured. | - | NOT RUN | - |
| 1129 | dc1-svc-leaf1b | Security | VerifySSHIPv6Acl | Verifies if the SSHD agent has IPv6 ACL(s) configured. | - | NOT RUN | - |
| 1130 | dc1-svc-leaf1b | Security | VerifySSHStatus | Verifies if the SSHD agent is disabled in the default VRF. | - | NOT RUN | - |
| 1131 | dc1-svc-leaf1b | Security | VerifyTelnetStatus | Verifies if Telnet is disabled in the default VRF. | - | NOT RUN | - |
| 1132 | dc1-svc-leaf1b | Services | VerifyDNSLookup | Verifies the DNS name to IP address resolution. | - | NOT RUN | - |
| 1133 | dc1-svc-leaf1b | Services | VerifyDNSServers | Verifies if the DNS servers are correctly configured. | - | NOT RUN | - |
| 1134 | dc1-svc-leaf1b | Services | VerifyErrdisableRecovery | Verifies the errdisable recovery reason, status, and interval. | - | NOT RUN | - |
| 1135 | dc1-svc-leaf1b | Services | VerifyHostname | Verifies the hostname of a device. | - | NOT RUN | - |
| 1136 | dc1-svc-leaf1b | SNMP | VerifySnmpIPv4Acl | Verifies if the SNMP agent has IPv4 ACL(s) configured. | - | NOT RUN | - |
| 1137 | dc1-svc-leaf1b | SNMP | VerifySnmpIPv6Acl | Verifies if the SNMP agent has IPv6 ACL(s) configured. | - | NOT RUN | - |
| 1138 | dc1-svc-leaf1b | SNMP | VerifySnmpStatus | Verifies if the SNMP agent is enabled. | - | NOT RUN | - |
| 1139 | dc1-svc-leaf1b | Software | VerifyEOSVersion | Verifies the EOS version of the device. | - | NOT RUN | - |
| 1140 | dc1-svc-leaf1b | Software | VerifyTerminAttrVersion | Verifies the TerminAttr version of the device. | - | NOT RUN | - |
| 1141 | dc1-svc-leaf1b | STUN | VerifyStunClient | Verifies the STUN client is configured with the specified IPv4 source address and port. Validate the public IP and port if provided. | - | NOT RUN | - |
| 1142 | dc1-svc-leaf1b | System | VerifyAgentLogs | Verifies there are no agent crash reports. | - | NOT RUN | - |
| 1143 | dc1-svc-leaf1b | System | VerifyCoredump | Verifies there are no core dump files. | - | NOT RUN | - |
| 1144 | dc1-svc-leaf1b | System | VerifyCPUUtilization | Verifies whether the CPU utilization is below 75%. | - | NOT RUN | - |
| 1145 | dc1-svc-leaf1b | System | VerifyFileSystemUtilization | Verifies that no partition is utilizing more than 75% of its disk space. | - | NOT RUN | - |
| 1146 | dc1-svc-leaf1b | System | VerifyMemoryUtilization | Verifies whether the memory utilization is below 75%. | - | NOT RUN | - |
| 1147 | dc1-svc-leaf1b | System | VerifyNTP | Verifies if NTP is synchronised. | - | NOT RUN | - |
| 1148 | dc1-svc-leaf1b | System | VerifyNTP | Verifies if NTP is synchronised. | - | NOT RUN | - |
| 1149 | dc1-svc-leaf1b | System | VerifyReloadCause | Verifies the last reload cause of the device. | - | NOT RUN | - |
| 1150 | dc1-svc-leaf1b | System | VerifyReloadCause | Verifies the last reload cause of the device. | - | NOT RUN | - |
| 1151 | dc1-svc-leaf1b | System | VerifyUptime | Verifies the device uptime. | - | NOT RUN | - |
| 1152 | dc1-svc-leaf1b | VLAN | VerifyVlanInternalPolicy | Verifies the VLAN internal allocation policy and the range of VLANs. | - | NOT RUN | - |
| 1153 | dc1-wan1 | AAA | VerifyAcctConsoleMethods | Verifies the AAA accounting console method lists for different accounting types (system, exec, commands, dot1x). | - | NOT RUN | - |
| 1154 | dc1-wan1 | AAA | VerifyAcctDefaultMethods | Verifies the AAA accounting default method lists for different accounting types (system, exec, commands, dot1x). | - | NOT RUN | - |
| 1155 | dc1-wan1 | AAA | VerifyAuthenMethods | Verifies the AAA authentication method lists for different authentication types (login, enable, dot1x). | - | NOT RUN | - |
| 1156 | dc1-wan1 | AAA | VerifyAuthzMethods | Verifies the AAA authorization method lists for different authorization types (commands, exec). | - | NOT RUN | - |
| 1157 | dc1-wan1 | AAA | VerifyTacacsServerGroups | Verifies if the provided TACACS server group(s) are configured. | - | NOT RUN | - |
| 1158 | dc1-wan1 | AAA | VerifyTacacsServers | Verifies TACACS servers are configured for a specified VRF. | - | NOT RUN | - |
| 1159 | dc1-wan1 | AAA | VerifyTacacsSourceIntf | Verifies TACACS source-interface for a specified VRF. | - | NOT RUN | - |
| 1160 | dc1-wan1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: dc1-leaf1a (IP: 10.255.255.10) | NOT RUN | - |
| 1161 | dc1-wan1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: dc1-leaf1b (IP: 10.255.255.20) | NOT RUN | - |
| 1162 | dc1-wan1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: dc1-wan2 (IP: 10.255.1.2) | NOT RUN | - |
| 1163 | dc1-wan1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 SR-TE Peer: dc1-leaf1a (IP: 10.255.255.10) | NOT RUN | - |
| 1164 | dc1-wan1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 SR-TE Peer: dc1-leaf1b (IP: 10.255.255.20) | NOT RUN | - |
| 1165 | dc1-wan1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: dc1-leaf1a (IP: 10.255.255.0) | NOT RUN | - |
| 1166 | dc1-wan1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: dc1-leaf1b (IP: 10.255.255.2) | NOT RUN | - |
| 1167 | dc1-wan1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP Link-State Peer: dc1-leaf1a (IP: 10.255.255.10) | NOT RUN | - |
| 1168 | dc1-wan1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP Link-State Peer: dc1-leaf1b (IP: 10.255.255.20) | NOT RUN | - |
| 1169 | dc1-wan1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP Path-Selection Peer: dc1-leaf1a (IP: 10.255.255.10) | NOT RUN | - |
| 1170 | dc1-wan1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP Path-Selection Peer: dc1-leaf1b (IP: 10.255.255.20) | NOT RUN | - |
| 1171 | dc1-wan1 | Configuration | VerifyRunningConfigDiffs | Verifies there is no difference between the running-config and the startup-config | - | NOT RUN | - |
| 1172 | dc1-wan1 | Configuration | VerifyZeroTouch | Verifies ZeroTouch is disabled | - | NOT RUN | - |
| 1173 | dc1-wan1 | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet1 - Remote: dc1-leaf1a Ethernet6 | NOT RUN | - |
| 1174 | dc1-wan1 | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet2 - Remote: dc1-leaf1b Ethernet6 | NOT RUN | - |
| 1175 | dc1-wan1 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Dps1 (IP: 10.255.1.1) - Destination: dc1-wan1 Dps1 (IP: 10.255.1.1) | NOT RUN | - |
| 1176 | dc1-wan1 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Dps1 (IP: 10.255.1.1) - Destination: dc1-wan2 Dps1 (IP: 10.255.1.2) | NOT RUN | - |
| 1177 | dc1-wan1 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet1 (IP: 10.255.255.1) - Destination: dc1-leaf1a Ethernet6 (IP: 10.255.255.0) | NOT RUN | - |
| 1178 | dc1-wan1 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet2 (IP: 10.255.255.3) - Destination: dc1-leaf1b Ethernet6 (IP: 10.255.255.2) | NOT RUN | - |
| 1179 | dc1-wan1 | Field Notices | VerifyFieldNotice44Resolution | Verifies that the device is using the correct Aboot version per FN0044. | - | NOT RUN | - |
| 1180 | dc1-wan1 | Field Notices | VerifyFieldNotice72Resolution | Verifies if the device is exposed to FN0072, and if the issue has been mitigated. | - | NOT RUN | - |
| 1181 | dc1-wan1 | Greent | VerifyGreenT | Verifies if a GreenT policy is created. | - | NOT RUN | - |
| 1182 | dc1-wan1 | Greent | VerifyGreenTCounters | Verifies if the GreenT counters are incremented. | - | NOT RUN | - |
| 1183 | dc1-wan1 | Hardware | VerifyAdverseDrops | Verifies there are no adverse drops on DCS-7280 and DCS-7500 family switches. | - | NOT RUN | - |
| 1184 | dc1-wan1 | Hardware | VerifyEnvironmentCooling | Verifies the status of power supply fans and all fan trays. | - | NOT RUN | - |
| 1185 | dc1-wan1 | Hardware | VerifyEnvironmentCooling | Verifies the status of power supply fans and all fan trays. | Accepted States: 'ok' | NOT RUN | - |
| 1186 | dc1-wan1 | Hardware | VerifyEnvironmentPower | Verifies the power supplies status. | - | NOT RUN | - |
| 1187 | dc1-wan1 | Hardware | VerifyEnvironmentPower | Verifies the power supplies status. | Accepted States: 'ok' | NOT RUN | - |
| 1188 | dc1-wan1 | Hardware | VerifyEnvironmentSystemCooling | Verifies the system cooling status. | - | NOT RUN | - |
| 1189 | dc1-wan1 | Hardware | VerifyTemperature | Verifies the device temperature. | - | NOT RUN | - |
| 1190 | dc1-wan1 | Hardware | VerifyTemperature | Verifies the device temperature. | - | NOT RUN | - |
| 1191 | dc1-wan1 | Hardware | VerifyTransceiversManufacturers | Verifies if all transceivers come from approved manufacturers. | - | NOT RUN | - |
| 1192 | dc1-wan1 | Hardware | VerifyTransceiversManufacturers | Verifies if all transceivers come from approved manufacturers. | Accepted Manufacturers: 'Arista Networks', 'Arastra, Inc.', 'Not Present' | NOT RUN | - |
| 1193 | dc1-wan1 | Hardware | VerifyTransceiversTemperature | Verifies the transceivers temperature. | - | NOT RUN | - |
| 1194 | dc1-wan1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Dps1 - DPS Interface = 'up' | NOT RUN | - |
| 1195 | dc1-wan1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet1 - P2P_LINK_TO_DC1-LEAF1A_Ethernet6 = 'up' | NOT RUN | - |
| 1196 | dc1-wan1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet2 - P2P_LINK_TO_DC1-LEAF1B_Ethernet6 = 'up' | NOT RUN | - |
| 1197 | dc1-wan1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet3 - mpls-sp-1_DC1-MPLS-3 = 'up' | NOT RUN | - |
| 1198 | dc1-wan1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet4 - isp-1_DC1-INET-3 = 'up' | NOT RUN | - |
| 1199 | dc1-wan1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback0 - ROUTER_ID = 'up' | NOT RUN | - |
| 1200 | dc1-wan1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vxlan1 = 'up' | NOT RUN | - |
| 1201 | dc1-wan1 | LANZ | VerifyLANZ | Verifies if LANZ is enabled. | - | NOT RUN | - |
| 1202 | dc1-wan1 | PTP | VerifyPtpGMStatus | Verifies that the device is locked to a valid PTP Grandmaster. | - | NOT RUN | - |
| 1203 | dc1-wan1 | PTP | VerifyPtpLockStatus | Verifies that the device was locked to the upstream PTP GM in the last minute. | - | NOT RUN | - |
| 1204 | dc1-wan1 | PTP | VerifyPtpModeStatus | Verifies that the device is configured as a PTP Boundary Clock. | - | NOT RUN | - |
| 1205 | dc1-wan1 | PTP | VerifyPtpOffset | Verifies that the PTP timing offset is within +/- 1000ns from the master clock. | - | NOT RUN | - |
| 1206 | dc1-wan1 | PTP | VerifyPtpPortModeStatus | Verifies the PTP interfaces state. | - | NOT RUN | - |
| 1207 | dc1-wan1 | Routing | VerifyRoutingProtocolModel | Verifies the configured routing protocol model. | Routing protocol model: multi-agent | NOT RUN | - |
| 1208 | dc1-wan1 | Security | VerifyAPIHttpsSSL | Verifies if the eAPI has a valid SSL profile. | - | NOT RUN | - |
| 1209 | dc1-wan1 | Security | VerifyAPIHttpsSSL | Verifies if the eAPI has a valid SSL profile. | eAPI HTTPS SSL Profile: eAPI_SSL_Profile | NOT RUN | - |
| 1210 | dc1-wan1 | Security | VerifyAPIHttpStatus | Verifies if eAPI HTTP server is disabled globally. | - | NOT RUN | - |
| 1211 | dc1-wan1 | Security | VerifyAPIIPv4Acl | Verifies if eAPI has the right number IPv4 ACL(s) configured for a specified VRF. | - | NOT RUN | - |
| 1212 | dc1-wan1 | Security | VerifyAPIIPv6Acl | Verifies if eAPI has the right number IPv6 ACL(s) configured for a specified VRF. | - | NOT RUN | - |
| 1213 | dc1-wan1 | Security | VerifyAPISSLCertificate | Verifies the eAPI SSL certificate expiry, common subject name, encryption algorithm and key size. | - | NOT RUN | - |
| 1214 | dc1-wan1 | Security | VerifyBannerLogin | Verifies the login banner of a device. | - | NOT RUN | - |
| 1215 | dc1-wan1 | Security | VerifyBannerMotd | Verifies the motd banner of a device. | - | NOT RUN | - |
| 1216 | dc1-wan1 | Security | VerifyIPSecConnHealth | Verifies all IPv4 security connections. | - | NOT RUN | - |
| 1217 | dc1-wan1 | Security | VerifyIPv4ACL | Verifies the configuration of IPv4 ACLs. | - | NOT RUN | - |
| 1218 | dc1-wan1 | Security | VerifySpecificIPSecConn | Verifies IPv4 security connections for a peer. | - | NOT RUN | - |
| 1219 | dc1-wan1 | Security | VerifySpecificIPSecConn | Verifies IPv4 security connections for a peer. | IPv4 Peer: 10.255.1.2 VRF: default | NOT RUN | - |
| 1220 | dc1-wan1 | Security | VerifySpecificIPSecConn | Verifies IPv4 security connections for a peer. | IPv4 Peer: 10.255.255.10 VRF: default | NOT RUN | - |
| 1221 | dc1-wan1 | Security | VerifySpecificIPSecConn | Verifies IPv4 security connections for a peer. | IPv4 Peer: 10.255.255.20 VRF: default | NOT RUN | - |
| 1222 | dc1-wan1 | Security | VerifySSHIPv4Acl | Verifies if the SSHD agent has IPv4 ACL(s) configured. | - | NOT RUN | - |
| 1223 | dc1-wan1 | Security | VerifySSHIPv6Acl | Verifies if the SSHD agent has IPv6 ACL(s) configured. | - | NOT RUN | - |
| 1224 | dc1-wan1 | Security | VerifySSHStatus | Verifies if the SSHD agent is disabled in the default VRF. | - | NOT RUN | - |
| 1225 | dc1-wan1 | Security | VerifyTelnetStatus | Verifies if Telnet is disabled in the default VRF. | - | NOT RUN | - |
| 1226 | dc1-wan1 | Services | VerifyDNSLookup | Verifies the DNS name to IP address resolution. | - | NOT RUN | - |
| 1227 | dc1-wan1 | Services | VerifyDNSServers | Verifies if the DNS servers are correctly configured. | - | NOT RUN | - |
| 1228 | dc1-wan1 | Services | VerifyErrdisableRecovery | Verifies the errdisable recovery reason, status, and interval. | - | NOT RUN | - |
| 1229 | dc1-wan1 | Services | VerifyHostname | Verifies the hostname of a device. | - | NOT RUN | - |
| 1230 | dc1-wan1 | SNMP | VerifySnmpIPv4Acl | Verifies if the SNMP agent has IPv4 ACL(s) configured. | - | NOT RUN | - |
| 1231 | dc1-wan1 | SNMP | VerifySnmpIPv6Acl | Verifies if the SNMP agent has IPv6 ACL(s) configured. | - | NOT RUN | - |
| 1232 | dc1-wan1 | SNMP | VerifySnmpStatus | Verifies if the SNMP agent is enabled. | - | NOT RUN | - |
| 1233 | dc1-wan1 | Software | VerifyEOSVersion | Verifies the EOS version of the device. | - | NOT RUN | - |
| 1234 | dc1-wan1 | Software | VerifyTerminAttrVersion | Verifies the TerminAttr version of the device. | - | NOT RUN | - |
| 1235 | dc1-wan1 | STUN | VerifyStunClient | Verifies the STUN client is configured with the specified IPv4 source address and port. Validate the public IP and port if provided. | - | NOT RUN | - |
| 1236 | dc1-wan1 | STUN | VerifyStunClient | Verifies the STUN client is configured with the specified IPv4 source address and port. Validate the public IP and port if provided. | Source IPv4 Address: 100.64.3.2 Source Port: 4500 | NOT RUN | - |
| 1237 | dc1-wan1 | STUN | VerifyStunClient | Verifies the STUN client is configured with the specified IPv4 source address and port. Validate the public IP and port if provided. | Source IPv4 Address: 172.18.3.2 Source Port: 4500 | NOT RUN | - |
| 1238 | dc1-wan1 | System | VerifyAgentLogs | Verifies there are no agent crash reports. | - | NOT RUN | - |
| 1239 | dc1-wan1 | System | VerifyCoredump | Verifies there are no core dump files. | - | NOT RUN | - |
| 1240 | dc1-wan1 | System | VerifyCPUUtilization | Verifies whether the CPU utilization is below 75%. | - | NOT RUN | - |
| 1241 | dc1-wan1 | System | VerifyFileSystemUtilization | Verifies that no partition is utilizing more than 75% of its disk space. | - | NOT RUN | - |
| 1242 | dc1-wan1 | System | VerifyMemoryUtilization | Verifies whether the memory utilization is below 75%. | - | NOT RUN | - |
| 1243 | dc1-wan1 | System | VerifyNTP | Verifies if NTP is synchronised. | - | NOT RUN | - |
| 1244 | dc1-wan1 | System | VerifyNTP | Verifies if NTP is synchronised. | - | NOT RUN | - |
| 1245 | dc1-wan1 | System | VerifyReloadCause | Verifies the last reload cause of the device. | - | NOT RUN | - |
| 1246 | dc1-wan1 | System | VerifyReloadCause | Verifies the last reload cause of the device. | - | NOT RUN | - |
| 1247 | dc1-wan1 | System | VerifyUptime | Verifies the device uptime. | - | NOT RUN | - |
| 1248 | dc1-wan1 | VLAN | VerifyVlanInternalPolicy | Verifies the VLAN internal allocation policy and the range of VLANs. | - | NOT RUN | - |
| 1249 | dc1-wan2 | AAA | VerifyAcctConsoleMethods | Verifies the AAA accounting console method lists for different accounting types (system, exec, commands, dot1x). | - | NOT RUN | - |
| 1250 | dc1-wan2 | AAA | VerifyAcctDefaultMethods | Verifies the AAA accounting default method lists for different accounting types (system, exec, commands, dot1x). | - | NOT RUN | - |
| 1251 | dc1-wan2 | AAA | VerifyAuthenMethods | Verifies the AAA authentication method lists for different authentication types (login, enable, dot1x). | - | NOT RUN | - |
| 1252 | dc1-wan2 | AAA | VerifyAuthzMethods | Verifies the AAA authorization method lists for different authorization types (commands, exec). | - | NOT RUN | - |
| 1253 | dc1-wan2 | AAA | VerifyTacacsServerGroups | Verifies if the provided TACACS server group(s) are configured. | - | NOT RUN | - |
| 1254 | dc1-wan2 | AAA | VerifyTacacsServers | Verifies TACACS servers are configured for a specified VRF. | - | NOT RUN | - |
| 1255 | dc1-wan2 | AAA | VerifyTacacsSourceIntf | Verifies TACACS source-interface for a specified VRF. | - | NOT RUN | - |
| 1256 | dc1-wan2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: dc1-leaf1a (IP: 10.255.255.10) | NOT RUN | - |
| 1257 | dc1-wan2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: dc1-leaf1b (IP: 10.255.255.20) | NOT RUN | - |
| 1258 | dc1-wan2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: dc1-wan1 (IP: 10.255.1.1) | NOT RUN | - |
| 1259 | dc1-wan2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 SR-TE Peer: dc1-leaf1a (IP: 10.255.255.10) | NOT RUN | - |
| 1260 | dc1-wan2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 SR-TE Peer: dc1-leaf1b (IP: 10.255.255.20) | NOT RUN | - |
| 1261 | dc1-wan2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: dc1-leaf1a (IP: 10.255.255.4) | NOT RUN | - |
| 1262 | dc1-wan2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: dc1-leaf1b (IP: 10.255.255.6) | NOT RUN | - |
| 1263 | dc1-wan2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP Link-State Peer: dc1-leaf1a (IP: 10.255.255.10) | NOT RUN | - |
| 1264 | dc1-wan2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP Link-State Peer: dc1-leaf1b (IP: 10.255.255.20) | NOT RUN | - |
| 1265 | dc1-wan2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP Path-Selection Peer: dc1-leaf1a (IP: 10.255.255.10) | NOT RUN | - |
| 1266 | dc1-wan2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP Path-Selection Peer: dc1-leaf1b (IP: 10.255.255.20) | NOT RUN | - |
| 1267 | dc1-wan2 | Configuration | VerifyRunningConfigDiffs | Verifies there is no difference between the running-config and the startup-config | - | NOT RUN | - |
| 1268 | dc1-wan2 | Configuration | VerifyZeroTouch | Verifies ZeroTouch is disabled | - | NOT RUN | - |
| 1269 | dc1-wan2 | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet1 - Remote: dc1-leaf1a Ethernet7 | NOT RUN | - |
| 1270 | dc1-wan2 | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet2 - Remote: dc1-leaf1b Ethernet7 | NOT RUN | - |
| 1271 | dc1-wan2 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Dps1 (IP: 10.255.1.2) - Destination: dc1-wan1 Dps1 (IP: 10.255.1.1) | NOT RUN | - |
| 1272 | dc1-wan2 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Dps1 (IP: 10.255.1.2) - Destination: dc1-wan2 Dps1 (IP: 10.255.1.2) | NOT RUN | - |
| 1273 | dc1-wan2 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet1 (IP: 10.255.255.5) - Destination: dc1-leaf1a Ethernet7 (IP: 10.255.255.4) | NOT RUN | - |
| 1274 | dc1-wan2 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet2 (IP: 10.255.255.7) - Destination: dc1-leaf1b Ethernet7 (IP: 10.255.255.6) | NOT RUN | - |
| 1275 | dc1-wan2 | Field Notices | VerifyFieldNotice44Resolution | Verifies that the device is using the correct Aboot version per FN0044. | - | NOT RUN | - |
| 1276 | dc1-wan2 | Field Notices | VerifyFieldNotice72Resolution | Verifies if the device is exposed to FN0072, and if the issue has been mitigated. | - | NOT RUN | - |
| 1277 | dc1-wan2 | Greent | VerifyGreenT | Verifies if a GreenT policy is created. | - | NOT RUN | - |
| 1278 | dc1-wan2 | Greent | VerifyGreenTCounters | Verifies if the GreenT counters are incremented. | - | NOT RUN | - |
| 1279 | dc1-wan2 | Hardware | VerifyAdverseDrops | Verifies there are no adverse drops on DCS-7280 and DCS-7500 family switches. | - | NOT RUN | - |
| 1280 | dc1-wan2 | Hardware | VerifyEnvironmentCooling | Verifies the status of power supply fans and all fan trays. | - | NOT RUN | - |
| 1281 | dc1-wan2 | Hardware | VerifyEnvironmentCooling | Verifies the status of power supply fans and all fan trays. | Accepted States: 'ok' | NOT RUN | - |
| 1282 | dc1-wan2 | Hardware | VerifyEnvironmentPower | Verifies the power supplies status. | - | NOT RUN | - |
| 1283 | dc1-wan2 | Hardware | VerifyEnvironmentPower | Verifies the power supplies status. | Accepted States: 'ok' | NOT RUN | - |
| 1284 | dc1-wan2 | Hardware | VerifyEnvironmentSystemCooling | Verifies the system cooling status. | - | NOT RUN | - |
| 1285 | dc1-wan2 | Hardware | VerifyTemperature | Verifies the device temperature. | - | NOT RUN | - |
| 1286 | dc1-wan2 | Hardware | VerifyTemperature | Verifies the device temperature. | - | NOT RUN | - |
| 1287 | dc1-wan2 | Hardware | VerifyTransceiversManufacturers | Verifies if all transceivers come from approved manufacturers. | - | NOT RUN | - |
| 1288 | dc1-wan2 | Hardware | VerifyTransceiversManufacturers | Verifies if all transceivers come from approved manufacturers. | Accepted Manufacturers: 'Arista Networks', 'Arastra, Inc.', 'Not Present' | NOT RUN | - |
| 1289 | dc1-wan2 | Hardware | VerifyTransceiversTemperature | Verifies the transceivers temperature. | - | NOT RUN | - |
| 1290 | dc1-wan2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Dps1 - DPS Interface = 'up' | NOT RUN | - |
| 1291 | dc1-wan2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet1 - P2P_LINK_TO_DC1-LEAF1A_Ethernet7 = 'up' | NOT RUN | - |
| 1292 | dc1-wan2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet2 - P2P_LINK_TO_DC1-LEAF1B_Ethernet7 = 'up' | NOT RUN | - |
| 1293 | dc1-wan2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet3 - mpls-sp-1_DC1-MPLS-4 = 'up' | NOT RUN | - |
| 1294 | dc1-wan2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet4 - isp-1_DC1-INET-4 = 'up' | NOT RUN | - |
| 1295 | dc1-wan2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback0 - ROUTER_ID = 'up' | NOT RUN | - |
| 1296 | dc1-wan2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vxlan1 = 'up' | NOT RUN | - |
| 1297 | dc1-wan2 | LANZ | VerifyLANZ | Verifies if LANZ is enabled. | - | NOT RUN | - |
| 1298 | dc1-wan2 | PTP | VerifyPtpGMStatus | Verifies that the device is locked to a valid PTP Grandmaster. | - | NOT RUN | - |
| 1299 | dc1-wan2 | PTP | VerifyPtpLockStatus | Verifies that the device was locked to the upstream PTP GM in the last minute. | - | NOT RUN | - |
| 1300 | dc1-wan2 | PTP | VerifyPtpModeStatus | Verifies that the device is configured as a PTP Boundary Clock. | - | NOT RUN | - |
| 1301 | dc1-wan2 | PTP | VerifyPtpOffset | Verifies that the PTP timing offset is within +/- 1000ns from the master clock. | - | NOT RUN | - |
| 1302 | dc1-wan2 | PTP | VerifyPtpPortModeStatus | Verifies the PTP interfaces state. | - | NOT RUN | - |
| 1303 | dc1-wan2 | Routing | VerifyRoutingProtocolModel | Verifies the configured routing protocol model. | Routing protocol model: multi-agent | NOT RUN | - |
| 1304 | dc1-wan2 | Security | VerifyAPIHttpsSSL | Verifies if the eAPI has a valid SSL profile. | - | NOT RUN | - |
| 1305 | dc1-wan2 | Security | VerifyAPIHttpsSSL | Verifies if the eAPI has a valid SSL profile. | eAPI HTTPS SSL Profile: eAPI_SSL_Profile | NOT RUN | - |
| 1306 | dc1-wan2 | Security | VerifyAPIHttpStatus | Verifies if eAPI HTTP server is disabled globally. | - | NOT RUN | - |
| 1307 | dc1-wan2 | Security | VerifyAPIIPv4Acl | Verifies if eAPI has the right number IPv4 ACL(s) configured for a specified VRF. | - | NOT RUN | - |
| 1308 | dc1-wan2 | Security | VerifyAPIIPv6Acl | Verifies if eAPI has the right number IPv6 ACL(s) configured for a specified VRF. | - | NOT RUN | - |
| 1309 | dc1-wan2 | Security | VerifyAPISSLCertificate | Verifies the eAPI SSL certificate expiry, common subject name, encryption algorithm and key size. | - | NOT RUN | - |
| 1310 | dc1-wan2 | Security | VerifyBannerLogin | Verifies the login banner of a device. | - | NOT RUN | - |
| 1311 | dc1-wan2 | Security | VerifyBannerMotd | Verifies the motd banner of a device. | - | NOT RUN | - |
| 1312 | dc1-wan2 | Security | VerifyIPSecConnHealth | Verifies all IPv4 security connections. | - | NOT RUN | - |
| 1313 | dc1-wan2 | Security | VerifyIPv4ACL | Verifies the configuration of IPv4 ACLs. | - | NOT RUN | - |
| 1314 | dc1-wan2 | Security | VerifySpecificIPSecConn | Verifies IPv4 security connections for a peer. | - | NOT RUN | - |
| 1315 | dc1-wan2 | Security | VerifySpecificIPSecConn | Verifies IPv4 security connections for a peer. | IPv4 Peer: 10.255.1.1 VRF: default | NOT RUN | - |
| 1316 | dc1-wan2 | Security | VerifySpecificIPSecConn | Verifies IPv4 security connections for a peer. | IPv4 Peer: 10.255.255.10 VRF: default | NOT RUN | - |
| 1317 | dc1-wan2 | Security | VerifySpecificIPSecConn | Verifies IPv4 security connections for a peer. | IPv4 Peer: 10.255.255.20 VRF: default | NOT RUN | - |
| 1318 | dc1-wan2 | Security | VerifySSHIPv4Acl | Verifies if the SSHD agent has IPv4 ACL(s) configured. | - | NOT RUN | - |
| 1319 | dc1-wan2 | Security | VerifySSHIPv6Acl | Verifies if the SSHD agent has IPv6 ACL(s) configured. | - | NOT RUN | - |
| 1320 | dc1-wan2 | Security | VerifySSHStatus | Verifies if the SSHD agent is disabled in the default VRF. | - | NOT RUN | - |
| 1321 | dc1-wan2 | Security | VerifyTelnetStatus | Verifies if Telnet is disabled in the default VRF. | - | NOT RUN | - |
| 1322 | dc1-wan2 | Services | VerifyDNSLookup | Verifies the DNS name to IP address resolution. | - | NOT RUN | - |
| 1323 | dc1-wan2 | Services | VerifyDNSServers | Verifies if the DNS servers are correctly configured. | - | NOT RUN | - |
| 1324 | dc1-wan2 | Services | VerifyErrdisableRecovery | Verifies the errdisable recovery reason, status, and interval. | - | NOT RUN | - |
| 1325 | dc1-wan2 | Services | VerifyHostname | Verifies the hostname of a device. | - | NOT RUN | - |
| 1326 | dc1-wan2 | SNMP | VerifySnmpIPv4Acl | Verifies if the SNMP agent has IPv4 ACL(s) configured. | - | NOT RUN | - |
| 1327 | dc1-wan2 | SNMP | VerifySnmpIPv6Acl | Verifies if the SNMP agent has IPv6 ACL(s) configured. | - | NOT RUN | - |
| 1328 | dc1-wan2 | SNMP | VerifySnmpStatus | Verifies if the SNMP agent is enabled. | - | NOT RUN | - |
| 1329 | dc1-wan2 | Software | VerifyEOSVersion | Verifies the EOS version of the device. | - | NOT RUN | - |
| 1330 | dc1-wan2 | Software | VerifyTerminAttrVersion | Verifies the TerminAttr version of the device. | - | NOT RUN | - |
| 1331 | dc1-wan2 | STUN | VerifyStunClient | Verifies the STUN client is configured with the specified IPv4 source address and port. Validate the public IP and port if provided. | - | NOT RUN | - |
| 1332 | dc1-wan2 | STUN | VerifyStunClient | Verifies the STUN client is configured with the specified IPv4 source address and port. Validate the public IP and port if provided. | Source IPv4 Address: 100.64.4.2 Source Port: 4500 | NOT RUN | - |
| 1333 | dc1-wan2 | STUN | VerifyStunClient | Verifies the STUN client is configured with the specified IPv4 source address and port. Validate the public IP and port if provided. | Source IPv4 Address: 172.18.4.2 Source Port: 4500 | NOT RUN | - |
| 1334 | dc1-wan2 | System | VerifyAgentLogs | Verifies there are no agent crash reports. | - | NOT RUN | - |
| 1335 | dc1-wan2 | System | VerifyCoredump | Verifies there are no core dump files. | - | NOT RUN | - |
| 1336 | dc1-wan2 | System | VerifyCPUUtilization | Verifies whether the CPU utilization is below 75%. | - | NOT RUN | - |
| 1337 | dc1-wan2 | System | VerifyFileSystemUtilization | Verifies that no partition is utilizing more than 75% of its disk space. | - | NOT RUN | - |
| 1338 | dc1-wan2 | System | VerifyMemoryUtilization | Verifies whether the memory utilization is below 75%. | - | NOT RUN | - |
| 1339 | dc1-wan2 | System | VerifyNTP | Verifies if NTP is synchronised. | - | NOT RUN | - |
| 1340 | dc1-wan2 | System | VerifyNTP | Verifies if NTP is synchronised. | - | NOT RUN | - |
| 1341 | dc1-wan2 | System | VerifyReloadCause | Verifies the last reload cause of the device. | - | NOT RUN | - |
| 1342 | dc1-wan2 | System | VerifyReloadCause | Verifies the last reload cause of the device. | - | NOT RUN | - |
| 1343 | dc1-wan2 | System | VerifyUptime | Verifies the device uptime. | - | NOT RUN | - |
| 1344 | dc1-wan2 | VLAN | VerifyVlanInternalPolicy | Verifies the VLAN internal allocation policy and the range of VLANs. | - | NOT RUN | - |
| 1345 | dc2-leaf1a | AAA | VerifyAcctConsoleMethods | Verifies the AAA accounting console method lists for different accounting types (system, exec, commands, dot1x). | - | NOT RUN | - |
| 1346 | dc2-leaf1a | AAA | VerifyAcctDefaultMethods | Verifies the AAA accounting default method lists for different accounting types (system, exec, commands, dot1x). | - | NOT RUN | - |
| 1347 | dc2-leaf1a | AAA | VerifyAuthenMethods | Verifies the AAA authentication method lists for different authentication types (login, enable, dot1x). | - | NOT RUN | - |
| 1348 | dc2-leaf1a | AAA | VerifyAuthzMethods | Verifies the AAA authorization method lists for different authorization types (commands, exec). | - | NOT RUN | - |
| 1349 | dc2-leaf1a | AAA | VerifyTacacsServerGroups | Verifies if the provided TACACS server group(s) are configured. | - | NOT RUN | - |
| 1350 | dc2-leaf1a | AAA | VerifyTacacsServers | Verifies TACACS servers are configured for a specified VRF. | - | NOT RUN | - |
| 1351 | dc2-leaf1a | AAA | VerifyTacacsSourceIntf | Verifies TACACS source-interface for a specified VRF. | - | NOT RUN | - |
| 1352 | dc2-leaf1a | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: dc2-spine1 (IP: 10.255.128.11) | NOT RUN | - |
| 1353 | dc2-leaf1a | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: dc2-spine2 (IP: 10.255.128.12) | NOT RUN | - |
| 1354 | dc2-leaf1a | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: dc2-leaf1b (IP: 10.255.129.117) | NOT RUN | - |
| 1355 | dc2-leaf1a | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: dc2-spine1 (IP: 10.255.255.104) | NOT RUN | - |
| 1356 | dc2-leaf1a | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: dc2-spine2 (IP: 10.255.255.106) | NOT RUN | - |
| 1357 | dc2-leaf1a | Configuration | VerifyRunningConfigDiffs | Verifies there is no difference between the running-config and the startup-config | - | NOT RUN | - |
| 1358 | dc2-leaf1a | Configuration | VerifyZeroTouch | Verifies ZeroTouch is disabled | - | NOT RUN | - |
| 1359 | dc2-leaf1a | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet1 - Remote: dc2-spine1 Ethernet1 | NOT RUN | - |
| 1360 | dc2-leaf1a | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet2 - Remote: dc2-spine2 Ethernet1 | NOT RUN | - |
| 1361 | dc2-leaf1a | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet3 - Remote: dc2-leaf1b Ethernet3 | NOT RUN | - |
| 1362 | dc2-leaf1a | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet4 - Remote: dc2-leaf1b Ethernet4 | NOT RUN | - |
| 1363 | dc2-leaf1a | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet8 - Remote: dc2-leaf1c Ethernet1 | NOT RUN | - |
| 1364 | dc2-leaf1a | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.128.13) - Destination: dc1-leaf1a Loopback0 (IP: 10.255.0.3) | NOT RUN | - |
| 1365 | dc2-leaf1a | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.128.13) - Destination: dc1-leaf1b Loopback0 (IP: 10.255.0.4) | NOT RUN | - |
| 1366 | dc2-leaf1a | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.128.13) - Destination: dc1-leaf2a Loopback0 (IP: 10.255.0.5) | NOT RUN | - |
| 1367 | dc2-leaf1a | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.128.13) - Destination: dc1-spine1 Loopback0 (IP: 10.255.0.1) | NOT RUN | - |
| 1368 | dc2-leaf1a | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.128.13) - Destination: dc1-spine2 Loopback0 (IP: 10.255.0.2) | NOT RUN | - |
| 1369 | dc2-leaf1a | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.128.13) - Destination: dc1-svc-leaf1a Loopback0 (IP: 10.33.0.5) | NOT RUN | - |
| 1370 | dc2-leaf1a | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.128.13) - Destination: dc1-svc-leaf1b Loopback0 (IP: 10.33.0.6) | NOT RUN | - |
| 1371 | dc2-leaf1a | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.128.13) - Destination: dc1-wan1 Loopback0 (IP: 10.255.2.1) | NOT RUN | - |
| 1372 | dc2-leaf1a | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.128.13) - Destination: dc1-wan2 Loopback0 (IP: 10.255.2.2) | NOT RUN | - |
| 1373 | dc2-leaf1a | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.128.13) - Destination: dc2-leaf1a Loopback0 (IP: 10.255.128.13) | NOT RUN | - |
| 1374 | dc2-leaf1a | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.128.13) - Destination: dc2-leaf1b Loopback0 (IP: 10.255.128.14) | NOT RUN | - |
| 1375 | dc2-leaf1a | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.128.13) - Destination: dc2-leaf2a Loopback0 (IP: 10.255.128.15) | NOT RUN | - |
| 1376 | dc2-leaf1a | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.128.13) - Destination: dc2-leaf2b Loopback0 (IP: 10.255.128.16) | NOT RUN | - |
| 1377 | dc2-leaf1a | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.128.13) - Destination: dc2-leaf3a.arista.com Loopback0 (IP: 10.255.128.17) | NOT RUN | - |
| 1378 | dc2-leaf1a | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.128.13) - Destination: dc2-leaf3b.arista.com Loopback0 (IP: 10.255.128.18) | NOT RUN | - |
| 1379 | dc2-leaf1a | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.128.13) - Destination: dc2-spine1 Loopback0 (IP: 10.255.128.11) | NOT RUN | - |
| 1380 | dc2-leaf1a | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.128.13) - Destination: dc2-spine2 Loopback0 (IP: 10.255.128.12) | NOT RUN | - |
| 1381 | dc2-leaf1a | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet1 (IP: 10.255.255.105) - Destination: dc2-spine1 Ethernet1 (IP: 10.255.255.104) | NOT RUN | - |
| 1382 | dc2-leaf1a | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet2 (IP: 10.255.255.107) - Destination: dc2-spine2 Ethernet1 (IP: 10.255.255.106) | NOT RUN | - |
| 1383 | dc2-leaf1a | Field Notices | VerifyFieldNotice44Resolution | Verifies that the device is using the correct Aboot version per FN0044. | - | NOT RUN | - |
| 1384 | dc2-leaf1a | Field Notices | VerifyFieldNotice72Resolution | Verifies if the device is exposed to FN0072, and if the issue has been mitigated. | - | NOT RUN | - |
| 1385 | dc2-leaf1a | Greent | VerifyGreenT | Verifies if a GreenT policy is created. | - | NOT RUN | - |
| 1386 | dc2-leaf1a | Greent | VerifyGreenTCounters | Verifies if the GreenT counters are incremented. | - | NOT RUN | - |
| 1387 | dc2-leaf1a | Hardware | VerifyAdverseDrops | Verifies there are no adverse drops on DCS-7280 and DCS-7500 family switches. | - | NOT RUN | - |
| 1388 | dc2-leaf1a | Hardware | VerifyEnvironmentCooling | Verifies the status of power supply fans and all fan trays. | - | NOT RUN | - |
| 1389 | dc2-leaf1a | Hardware | VerifyEnvironmentCooling | Verifies the status of power supply fans and all fan trays. | Accepted States: 'ok' | NOT RUN | - |
| 1390 | dc2-leaf1a | Hardware | VerifyEnvironmentPower | Verifies the power supplies status. | - | NOT RUN | - |
| 1391 | dc2-leaf1a | Hardware | VerifyEnvironmentPower | Verifies the power supplies status. | Accepted States: 'ok' | NOT RUN | - |
| 1392 | dc2-leaf1a | Hardware | VerifyEnvironmentSystemCooling | Verifies the system cooling status. | - | NOT RUN | - |
| 1393 | dc2-leaf1a | Hardware | VerifyTemperature | Verifies the device temperature. | - | NOT RUN | - |
| 1394 | dc2-leaf1a | Hardware | VerifyTemperature | Verifies the device temperature. | - | NOT RUN | - |
| 1395 | dc2-leaf1a | Hardware | VerifyTransceiversManufacturers | Verifies if all transceivers come from approved manufacturers. | - | NOT RUN | - |
| 1396 | dc2-leaf1a | Hardware | VerifyTransceiversManufacturers | Verifies if all transceivers come from approved manufacturers. | Accepted Manufacturers: 'Arista Networks', 'Arastra, Inc.', 'Not Present' | NOT RUN | - |
| 1397 | dc2-leaf1a | Hardware | VerifyTransceiversTemperature | Verifies the transceivers temperature. | - | NOT RUN | - |
| 1398 | dc2-leaf1a | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet1 - P2P_LINK_TO_DC2-SPINE1_Ethernet1 = 'up' | NOT RUN | - |
| 1399 | dc2-leaf1a | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet2 - P2P_LINK_TO_DC2-SPINE2_Ethernet1 = 'up' | NOT RUN | - |
| 1400 | dc2-leaf1a | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet3 - MLAG_dc2-leaf1b_Ethernet3 = 'up' | NOT RUN | - |
| 1401 | dc2-leaf1a | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet4 - MLAG_dc2-leaf1b_Ethernet4 = 'up' | NOT RUN | - |
| 1402 | dc2-leaf1a | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet5 - SERVER_dc2-leaf1-server1_PCI1 = 'up' | NOT RUN | - |
| 1403 | dc2-leaf1a | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet8 - DC2-LEAF1C_Ethernet1 = 'up' | NOT RUN | - |
| 1404 | dc2-leaf1a | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback0 - ROUTER_ID = 'up' | NOT RUN | - |
| 1405 | dc2-leaf1a | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback1 - VXLAN_TUNNEL_SOURCE = 'up' | NOT RUN | - |
| 1406 | dc2-leaf1a | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback10 - VRF10_VTEP_DIAGNOSTICS = 'up' | NOT RUN | - |
| 1407 | dc2-leaf1a | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback11 - VRF11_VTEP_DIAGNOSTICS = 'up' | NOT RUN | - |
| 1408 | dc2-leaf1a | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel3 - MLAG_dc2-leaf1b_Port-Channel3 = 'up' | NOT RUN | - |
| 1409 | dc2-leaf1a | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel5 - PortChannel dc2-leaf1-server1 = 'up' | NOT RUN | - |
| 1410 | dc2-leaf1a | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel8 - DC2-LEAF1C_Po1 = 'up' | NOT RUN | - |
| 1411 | dc2-leaf1a | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan11 - VRF10_VLAN11 = 'up' | NOT RUN | - |
| 1412 | dc2-leaf1a | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan12 - VRF10_VLAN12 = 'up' | NOT RUN | - |
| 1413 | dc2-leaf1a | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan21 - VRF11_VLAN21 = 'up' | NOT RUN | - |
| 1414 | dc2-leaf1a | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan22 - VRF11_VLAN22 = 'up' | NOT RUN | - |
| 1415 | dc2-leaf1a | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan3009 - MLAG_L3_VRF_VRF10 = 'up' | NOT RUN | - |
| 1416 | dc2-leaf1a | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan3010 - MLAG_L3_VRF_VRF11 = 'up' | NOT RUN | - |
| 1417 | dc2-leaf1a | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan4093 - MLAG_L3 = 'up' | NOT RUN | - |
| 1418 | dc2-leaf1a | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan4094 - MLAG = 'up' | NOT RUN | - |
| 1419 | dc2-leaf1a | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vxlan1 = 'up' | NOT RUN | - |
| 1420 | dc2-leaf1a | LANZ | VerifyLANZ | Verifies if LANZ is enabled. | - | NOT RUN | - |
| 1421 | dc2-leaf1a | Logging | VerifyLoggingAccounting | Verifies if AAA accounting logs are generated. | - | NOT RUN | - |
| 1422 | dc2-leaf1a | Logging | VerifyLoggingErrors | Verifies there are no syslog messages with a severity of ERRORS or higher. | - | NOT RUN | - |
| 1423 | dc2-leaf1a | Logging | VerifyLoggingHostname | Verifies if logs are generated with the device FQDN. | - | NOT RUN | - |
| 1424 | dc2-leaf1a | Logging | VerifyLoggingHosts | Verifies logging hosts (syslog servers) for a specified VRF. | - | NOT RUN | - |
| 1425 | dc2-leaf1a | Logging | VerifyLoggingLogsGeneration | Verifies if logs are generated. | - | NOT RUN | - |
| 1426 | dc2-leaf1a | Logging | VerifyLoggingPersistent | Verifies if logging persistent is enabled and logs are saved in flash. | - | NOT RUN | - |
| 1427 | dc2-leaf1a | Logging | VerifyLoggingSourceInt | Verifies logging source-interface for a specified VRF. | - | NOT RUN | - |
| 1428 | dc2-leaf1a | Logging | VerifyLoggingTimestamp | Verifies if logs are generated with the riate timestamp. | - | NOT RUN | - |
| 1429 | dc2-leaf1a | MLAG | VerifyMlagConfigSanity | Verifies there are no MLAG config-sanity inconsistencies. | - | NOT RUN | - |
| 1430 | dc2-leaf1a | MLAG | VerifyMlagDualPrimary | Verifies the MLAG dual-primary detection parameters. | - | NOT RUN | - |
| 1431 | dc2-leaf1a | MLAG | VerifyMlagInterfaces | Verifies there are no inactive or active-partial MLAG ports. | - | NOT RUN | - |
| 1432 | dc2-leaf1a | MLAG | VerifyMlagReloadDelay | Verifies the MLAG reload-delay parameters. | - | NOT RUN | - |
| 1433 | dc2-leaf1a | MLAG | VerifyMlagStatus | Verifies the health status of the MLAG configuration. | - | NOT RUN | - |
| 1434 | dc2-leaf1a | MLAG | VerifyMlagStatus | Verifies the health status of the MLAG configuration. | - | NOT RUN | - |
| 1435 | dc2-leaf1a | Multicast | VerifyIGMPSnoopingGlobal | Verifies the IGMP snooping global configuration. | - | NOT RUN | - |
| 1436 | dc2-leaf1a | Multicast | VerifyIGMPSnoopingVlans | Verifies the IGMP snooping status for the provided VLANs. | - | NOT RUN | - |
| 1437 | dc2-leaf1a | PTP | VerifyPtpGMStatus | Verifies that the device is locked to a valid PTP Grandmaster. | - | NOT RUN | - |
| 1438 | dc2-leaf1a | PTP | VerifyPtpLockStatus | Verifies that the device was locked to the upstream PTP GM in the last minute. | - | NOT RUN | - |
| 1439 | dc2-leaf1a | PTP | VerifyPtpModeStatus | Verifies that the device is configured as a PTP Boundary Clock. | - | NOT RUN | - |
| 1440 | dc2-leaf1a | PTP | VerifyPtpOffset | Verifies that the PTP timing offset is within +/- 1000ns from the master clock. | - | NOT RUN | - |
| 1441 | dc2-leaf1a | PTP | VerifyPtpPortModeStatus | Verifies the PTP interfaces state. | - | NOT RUN | - |
| 1442 | dc2-leaf1a | Routing | VerifyRoutingProtocolModel | Verifies the configured routing protocol model. | Routing protocol model: multi-agent | NOT RUN | - |
| 1443 | dc2-leaf1a | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.0.1 - Peer: dc1-spine1 | NOT RUN | - |
| 1444 | dc2-leaf1a | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.0.2 - Peer: dc1-spine2 | NOT RUN | - |
| 1445 | dc2-leaf1a | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.0.3 - Peer: dc1-leaf1a | NOT RUN | - |
| 1446 | dc2-leaf1a | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.0.4 - Peer: dc1-leaf1b | NOT RUN | - |
| 1447 | dc2-leaf1a | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.0.5 - Peer: dc1-leaf2a | NOT RUN | - |
| 1448 | dc2-leaf1a | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.1.3 - Peer: dc1-leaf1a | NOT RUN | - |
| 1449 | dc2-leaf1a | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.1.5 - Peer: dc1-leaf2a | NOT RUN | - |
| 1450 | dc2-leaf1a | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.128.11 - Peer: dc2-spine1 | NOT RUN | - |
| 1451 | dc2-leaf1a | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.128.12 - Peer: dc2-spine2 | NOT RUN | - |
| 1452 | dc2-leaf1a | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.128.13 - Peer: dc2-leaf1a | NOT RUN | - |
| 1453 | dc2-leaf1a | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.128.14 - Peer: dc2-leaf1b | NOT RUN | - |
| 1454 | dc2-leaf1a | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.128.15 - Peer: dc2-leaf2a | NOT RUN | - |
| 1455 | dc2-leaf1a | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.128.16 - Peer: dc2-leaf2b | NOT RUN | - |
| 1456 | dc2-leaf1a | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.128.17 - Peer: dc2-leaf3a.arista.com | NOT RUN | - |
| 1457 | dc2-leaf1a | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.128.18 - Peer: dc2-leaf3b.arista.com | NOT RUN | - |
| 1458 | dc2-leaf1a | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.129.13 - Peer: dc2-leaf1a | NOT RUN | - |
| 1459 | dc2-leaf1a | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.129.15 - Peer: dc2-leaf2a | NOT RUN | - |
| 1460 | dc2-leaf1a | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.129.17 - Peer: dc2-leaf3a.arista.com | NOT RUN | - |
| 1461 | dc2-leaf1a | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.2.1 - Peer: dc1-wan1 | NOT RUN | - |
| 1462 | dc2-leaf1a | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.2.2 - Peer: dc1-wan2 | NOT RUN | - |
| 1463 | dc2-leaf1a | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.33.0.5 - Peer: dc1-svc-leaf1a | NOT RUN | - |
| 1464 | dc2-leaf1a | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.33.0.6 - Peer: dc1-svc-leaf1b | NOT RUN | - |
| 1465 | dc2-leaf1a | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.33.1.5 - Peer: dc1-svc-leaf1a | NOT RUN | - |
| 1466 | dc2-leaf1a | Security | VerifyAPIHttpsSSL | Verifies if the eAPI has a valid SSL profile. | - | NOT RUN | - |
| 1467 | dc2-leaf1a | Security | VerifyAPIHttpsSSL | Verifies if the eAPI has a valid SSL profile. | eAPI HTTPS SSL Profile: eAPI_SSL_Profile | NOT RUN | - |
| 1468 | dc2-leaf1a | Security | VerifyAPIHttpStatus | Verifies if eAPI HTTP server is disabled globally. | - | NOT RUN | - |
| 1469 | dc2-leaf1a | Security | VerifyAPIIPv4Acl | Verifies if eAPI has the right number IPv4 ACL(s) configured for a specified VRF. | - | NOT RUN | - |
| 1470 | dc2-leaf1a | Security | VerifyAPIIPv6Acl | Verifies if eAPI has the right number IPv6 ACL(s) configured for a specified VRF. | - | NOT RUN | - |
| 1471 | dc2-leaf1a | Security | VerifyAPISSLCertificate | Verifies the eAPI SSL certificate expiry, common subject name, encryption algorithm and key size. | - | NOT RUN | - |
| 1472 | dc2-leaf1a | Security | VerifyBannerLogin | Verifies the login banner of a device. | - | NOT RUN | - |
| 1473 | dc2-leaf1a | Security | VerifyBannerMotd | Verifies the motd banner of a device. | - | NOT RUN | - |
| 1474 | dc2-leaf1a | Security | VerifyIPSecConnHealth | Verifies all IPv4 security connections. | - | NOT RUN | - |
| 1475 | dc2-leaf1a | Security | VerifyIPv4ACL | Verifies the configuration of IPv4 ACLs. | - | NOT RUN | - |
| 1476 | dc2-leaf1a | Security | VerifySpecificIPSecConn | Verifies IPv4 security connections for a peer. | - | NOT RUN | - |
| 1477 | dc2-leaf1a | Security | VerifySSHIPv4Acl | Verifies if the SSHD agent has IPv4 ACL(s) configured. | - | NOT RUN | - |
| 1478 | dc2-leaf1a | Security | VerifySSHIPv6Acl | Verifies if the SSHD agent has IPv6 ACL(s) configured. | - | NOT RUN | - |
| 1479 | dc2-leaf1a | Security | VerifySSHStatus | Verifies if the SSHD agent is disabled in the default VRF. | - | NOT RUN | - |
| 1480 | dc2-leaf1a | Security | VerifyTelnetStatus | Verifies if Telnet is disabled in the default VRF. | - | NOT RUN | - |
| 1481 | dc2-leaf1a | Services | VerifyDNSLookup | Verifies the DNS name to IP address resolution. | - | NOT RUN | - |
| 1482 | dc2-leaf1a | Services | VerifyDNSServers | Verifies if the DNS servers are correctly configured. | - | NOT RUN | - |
| 1483 | dc2-leaf1a | Services | VerifyErrdisableRecovery | Verifies the errdisable recovery reason, status, and interval. | - | NOT RUN | - |
| 1484 | dc2-leaf1a | Services | VerifyHostname | Verifies the hostname of a device. | - | NOT RUN | - |
| 1485 | dc2-leaf1a | SNMP | VerifySnmpIPv4Acl | Verifies if the SNMP agent has IPv4 ACL(s) configured. | - | NOT RUN | - |
| 1486 | dc2-leaf1a | SNMP | VerifySnmpIPv6Acl | Verifies if the SNMP agent has IPv6 ACL(s) configured. | - | NOT RUN | - |
| 1487 | dc2-leaf1a | SNMP | VerifySnmpStatus | Verifies if the SNMP agent is enabled. | - | NOT RUN | - |
| 1488 | dc2-leaf1a | Software | VerifyEOSVersion | Verifies the EOS version of the device. | - | NOT RUN | - |
| 1489 | dc2-leaf1a | Software | VerifyTerminAttrVersion | Verifies the TerminAttr version of the device. | - | NOT RUN | - |
| 1490 | dc2-leaf1a | STP | VerifySTPBlockedPorts | Verifies there is no STP blocked ports. | - | NOT RUN | - |
| 1491 | dc2-leaf1a | STP | VerifySTPCounters | Verifies there is no errors in STP BPDU packets. | - | NOT RUN | - |
| 1492 | dc2-leaf1a | STP | VerifySTPForwardingPorts | Verifies that all interfaces are forwarding for a provided list of VLAN(s). | - | NOT RUN | - |
| 1493 | dc2-leaf1a | STP | VerifySTPMode | Verifies the configured STP mode for a provided list of VLAN(s). | - | NOT RUN | - |
| 1494 | dc2-leaf1a | STP | VerifySTPRootPriority | Verifies the STP root priority for a provided list of VLAN or MST instance ID(s). | - | NOT RUN | - |
| 1495 | dc2-leaf1a | STUN | VerifyStunClient | Verifies the STUN client is configured with the specified IPv4 source address and port. Validate the public IP and port if provided. | - | NOT RUN | - |
| 1496 | dc2-leaf1a | System | VerifyAgentLogs | Verifies there are no agent crash reports. | - | NOT RUN | - |
| 1497 | dc2-leaf1a | System | VerifyCoredump | Verifies there are no core dump files. | - | NOT RUN | - |
| 1498 | dc2-leaf1a | System | VerifyCPUUtilization | Verifies whether the CPU utilization is below 75%. | - | NOT RUN | - |
| 1499 | dc2-leaf1a | System | VerifyFileSystemUtilization | Verifies that no partition is utilizing more than 75% of its disk space. | - | NOT RUN | - |
| 1500 | dc2-leaf1a | System | VerifyMemoryUtilization | Verifies whether the memory utilization is below 75%. | - | NOT RUN | - |
| 1501 | dc2-leaf1a | System | VerifyNTP | Verifies if NTP is synchronised. | - | NOT RUN | - |
| 1502 | dc2-leaf1a | System | VerifyNTP | Verifies if NTP is synchronised. | - | NOT RUN | - |
| 1503 | dc2-leaf1a | System | VerifyReloadCause | Verifies the last reload cause of the device. | - | NOT RUN | - |
| 1504 | dc2-leaf1a | System | VerifyReloadCause | Verifies the last reload cause of the device. | - | NOT RUN | - |
| 1505 | dc2-leaf1a | System | VerifyUptime | Verifies the device uptime. | - | NOT RUN | - |
| 1506 | dc2-leaf1a | VLAN | VerifyVlanInternalPolicy | Verifies the VLAN internal allocation policy and the range of VLANs. | - | NOT RUN | - |
| 1507 | dc2-leaf1b | AAA | VerifyAcctConsoleMethods | Verifies the AAA accounting console method lists for different accounting types (system, exec, commands, dot1x). | - | NOT RUN | - |
| 1508 | dc2-leaf1b | AAA | VerifyAcctDefaultMethods | Verifies the AAA accounting default method lists for different accounting types (system, exec, commands, dot1x). | - | NOT RUN | - |
| 1509 | dc2-leaf1b | AAA | VerifyAuthenMethods | Verifies the AAA authentication method lists for different authentication types (login, enable, dot1x). | - | NOT RUN | - |
| 1510 | dc2-leaf1b | AAA | VerifyAuthzMethods | Verifies the AAA authorization method lists for different authorization types (commands, exec). | - | NOT RUN | - |
| 1511 | dc2-leaf1b | AAA | VerifyTacacsServerGroups | Verifies if the provided TACACS server group(s) are configured. | - | NOT RUN | - |
| 1512 | dc2-leaf1b | AAA | VerifyTacacsServers | Verifies TACACS servers are configured for a specified VRF. | - | NOT RUN | - |
| 1513 | dc2-leaf1b | AAA | VerifyTacacsSourceIntf | Verifies TACACS source-interface for a specified VRF. | - | NOT RUN | - |
| 1514 | dc2-leaf1b | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: dc2-spine1 (IP: 10.255.128.11) | NOT RUN | - |
| 1515 | dc2-leaf1b | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: dc2-spine2 (IP: 10.255.128.12) | NOT RUN | - |
| 1516 | dc2-leaf1b | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: dc2-leaf1a (IP: 10.255.129.116) | NOT RUN | - |
| 1517 | dc2-leaf1b | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: dc2-spine1 (IP: 10.255.255.108) | NOT RUN | - |
| 1518 | dc2-leaf1b | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: dc2-spine2 (IP: 10.255.255.110) | NOT RUN | - |
| 1519 | dc2-leaf1b | Configuration | VerifyRunningConfigDiffs | Verifies there is no difference between the running-config and the startup-config | - | NOT RUN | - |
| 1520 | dc2-leaf1b | Configuration | VerifyZeroTouch | Verifies ZeroTouch is disabled | - | NOT RUN | - |
| 1521 | dc2-leaf1b | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet1 - Remote: dc2-spine1 Ethernet2 | NOT RUN | - |
| 1522 | dc2-leaf1b | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet2 - Remote: dc2-spine2 Ethernet2 | NOT RUN | - |
| 1523 | dc2-leaf1b | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet3 - Remote: dc2-leaf1a Ethernet3 | NOT RUN | - |
| 1524 | dc2-leaf1b | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet4 - Remote: dc2-leaf1a Ethernet4 | NOT RUN | - |
| 1525 | dc2-leaf1b | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet8 - Remote: dc2-leaf1c Ethernet2 | NOT RUN | - |
| 1526 | dc2-leaf1b | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.128.14) - Destination: dc1-leaf1a Loopback0 (IP: 10.255.0.3) | NOT RUN | - |
| 1527 | dc2-leaf1b | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.128.14) - Destination: dc1-leaf1b Loopback0 (IP: 10.255.0.4) | NOT RUN | - |
| 1528 | dc2-leaf1b | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.128.14) - Destination: dc1-leaf2a Loopback0 (IP: 10.255.0.5) | NOT RUN | - |
| 1529 | dc2-leaf1b | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.128.14) - Destination: dc1-spine1 Loopback0 (IP: 10.255.0.1) | NOT RUN | - |
| 1530 | dc2-leaf1b | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.128.14) - Destination: dc1-spine2 Loopback0 (IP: 10.255.0.2) | NOT RUN | - |
| 1531 | dc2-leaf1b | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.128.14) - Destination: dc1-svc-leaf1a Loopback0 (IP: 10.33.0.5) | NOT RUN | - |
| 1532 | dc2-leaf1b | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.128.14) - Destination: dc1-svc-leaf1b Loopback0 (IP: 10.33.0.6) | NOT RUN | - |
| 1533 | dc2-leaf1b | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.128.14) - Destination: dc1-wan1 Loopback0 (IP: 10.255.2.1) | NOT RUN | - |
| 1534 | dc2-leaf1b | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.128.14) - Destination: dc1-wan2 Loopback0 (IP: 10.255.2.2) | NOT RUN | - |
| 1535 | dc2-leaf1b | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.128.14) - Destination: dc2-leaf1a Loopback0 (IP: 10.255.128.13) | NOT RUN | - |
| 1536 | dc2-leaf1b | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.128.14) - Destination: dc2-leaf1b Loopback0 (IP: 10.255.128.14) | NOT RUN | - |
| 1537 | dc2-leaf1b | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.128.14) - Destination: dc2-leaf2a Loopback0 (IP: 10.255.128.15) | NOT RUN | - |
| 1538 | dc2-leaf1b | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.128.14) - Destination: dc2-leaf2b Loopback0 (IP: 10.255.128.16) | NOT RUN | - |
| 1539 | dc2-leaf1b | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.128.14) - Destination: dc2-leaf3a.arista.com Loopback0 (IP: 10.255.128.17) | NOT RUN | - |
| 1540 | dc2-leaf1b | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.128.14) - Destination: dc2-leaf3b.arista.com Loopback0 (IP: 10.255.128.18) | NOT RUN | - |
| 1541 | dc2-leaf1b | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.128.14) - Destination: dc2-spine1 Loopback0 (IP: 10.255.128.11) | NOT RUN | - |
| 1542 | dc2-leaf1b | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.128.14) - Destination: dc2-spine2 Loopback0 (IP: 10.255.128.12) | NOT RUN | - |
| 1543 | dc2-leaf1b | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet1 (IP: 10.255.255.109) - Destination: dc2-spine1 Ethernet2 (IP: 10.255.255.108) | NOT RUN | - |
| 1544 | dc2-leaf1b | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet2 (IP: 10.255.255.111) - Destination: dc2-spine2 Ethernet2 (IP: 10.255.255.110) | NOT RUN | - |
| 1545 | dc2-leaf1b | Field Notices | VerifyFieldNotice44Resolution | Verifies that the device is using the correct Aboot version per FN0044. | - | NOT RUN | - |
| 1546 | dc2-leaf1b | Field Notices | VerifyFieldNotice72Resolution | Verifies if the device is exposed to FN0072, and if the issue has been mitigated. | - | NOT RUN | - |
| 1547 | dc2-leaf1b | Greent | VerifyGreenT | Verifies if a GreenT policy is created. | - | NOT RUN | - |
| 1548 | dc2-leaf1b | Greent | VerifyGreenTCounters | Verifies if the GreenT counters are incremented. | - | NOT RUN | - |
| 1549 | dc2-leaf1b | Hardware | VerifyAdverseDrops | Verifies there are no adverse drops on DCS-7280 and DCS-7500 family switches. | - | NOT RUN | - |
| 1550 | dc2-leaf1b | Hardware | VerifyEnvironmentCooling | Verifies the status of power supply fans and all fan trays. | - | NOT RUN | - |
| 1551 | dc2-leaf1b | Hardware | VerifyEnvironmentCooling | Verifies the status of power supply fans and all fan trays. | Accepted States: 'ok' | NOT RUN | - |
| 1552 | dc2-leaf1b | Hardware | VerifyEnvironmentPower | Verifies the power supplies status. | - | NOT RUN | - |
| 1553 | dc2-leaf1b | Hardware | VerifyEnvironmentPower | Verifies the power supplies status. | Accepted States: 'ok' | NOT RUN | - |
| 1554 | dc2-leaf1b | Hardware | VerifyEnvironmentSystemCooling | Verifies the system cooling status. | - | NOT RUN | - |
| 1555 | dc2-leaf1b | Hardware | VerifyTemperature | Verifies the device temperature. | - | NOT RUN | - |
| 1556 | dc2-leaf1b | Hardware | VerifyTemperature | Verifies the device temperature. | - | NOT RUN | - |
| 1557 | dc2-leaf1b | Hardware | VerifyTransceiversManufacturers | Verifies if all transceivers come from approved manufacturers. | - | NOT RUN | - |
| 1558 | dc2-leaf1b | Hardware | VerifyTransceiversManufacturers | Verifies if all transceivers come from approved manufacturers. | Accepted Manufacturers: 'Arista Networks', 'Arastra, Inc.', 'Not Present' | NOT RUN | - |
| 1559 | dc2-leaf1b | Hardware | VerifyTransceiversTemperature | Verifies the transceivers temperature. | - | NOT RUN | - |
| 1560 | dc2-leaf1b | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet1 - P2P_LINK_TO_DC2-SPINE1_Ethernet2 = 'up' | NOT RUN | - |
| 1561 | dc2-leaf1b | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet2 - P2P_LINK_TO_DC2-SPINE2_Ethernet2 = 'up' | NOT RUN | - |
| 1562 | dc2-leaf1b | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet3 - MLAG_dc2-leaf1a_Ethernet3 = 'up' | NOT RUN | - |
| 1563 | dc2-leaf1b | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet4 - MLAG_dc2-leaf1a_Ethernet4 = 'up' | NOT RUN | - |
| 1564 | dc2-leaf1b | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet5 - SERVER_dc2-leaf1-server1_PCI2 = 'up' | NOT RUN | - |
| 1565 | dc2-leaf1b | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet8 - DC2-LEAF1C_Ethernet2 = 'up' | NOT RUN | - |
| 1566 | dc2-leaf1b | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback0 - ROUTER_ID = 'up' | NOT RUN | - |
| 1567 | dc2-leaf1b | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback1 - VXLAN_TUNNEL_SOURCE = 'up' | NOT RUN | - |
| 1568 | dc2-leaf1b | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback10 - VRF10_VTEP_DIAGNOSTICS = 'up' | NOT RUN | - |
| 1569 | dc2-leaf1b | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback11 - VRF11_VTEP_DIAGNOSTICS = 'up' | NOT RUN | - |
| 1570 | dc2-leaf1b | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel3 - MLAG_dc2-leaf1a_Port-Channel3 = 'up' | NOT RUN | - |
| 1571 | dc2-leaf1b | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel5 - PortChannel dc2-leaf1-server1 = 'up' | NOT RUN | - |
| 1572 | dc2-leaf1b | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel8 - DC2-LEAF1C_Po1 = 'up' | NOT RUN | - |
| 1573 | dc2-leaf1b | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan11 - VRF10_VLAN11 = 'up' | NOT RUN | - |
| 1574 | dc2-leaf1b | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan12 - VRF10_VLAN12 = 'up' | NOT RUN | - |
| 1575 | dc2-leaf1b | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan21 - VRF11_VLAN21 = 'up' | NOT RUN | - |
| 1576 | dc2-leaf1b | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan22 - VRF11_VLAN22 = 'up' | NOT RUN | - |
| 1577 | dc2-leaf1b | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan3009 - MLAG_L3_VRF_VRF10 = 'up' | NOT RUN | - |
| 1578 | dc2-leaf1b | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan3010 - MLAG_L3_VRF_VRF11 = 'up' | NOT RUN | - |
| 1579 | dc2-leaf1b | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan4093 - MLAG_L3 = 'up' | NOT RUN | - |
| 1580 | dc2-leaf1b | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan4094 - MLAG = 'up' | NOT RUN | - |
| 1581 | dc2-leaf1b | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vxlan1 = 'up' | NOT RUN | - |
| 1582 | dc2-leaf1b | LANZ | VerifyLANZ | Verifies if LANZ is enabled. | - | NOT RUN | - |
| 1583 | dc2-leaf1b | Logging | VerifyLoggingAccounting | Verifies if AAA accounting logs are generated. | - | NOT RUN | - |
| 1584 | dc2-leaf1b | Logging | VerifyLoggingErrors | Verifies there are no syslog messages with a severity of ERRORS or higher. | - | NOT RUN | - |
| 1585 | dc2-leaf1b | Logging | VerifyLoggingHostname | Verifies if logs are generated with the device FQDN. | - | NOT RUN | - |
| 1586 | dc2-leaf1b | Logging | VerifyLoggingHosts | Verifies logging hosts (syslog servers) for a specified VRF. | - | NOT RUN | - |
| 1587 | dc2-leaf1b | Logging | VerifyLoggingLogsGeneration | Verifies if logs are generated. | - | NOT RUN | - |
| 1588 | dc2-leaf1b | Logging | VerifyLoggingPersistent | Verifies if logging persistent is enabled and logs are saved in flash. | - | NOT RUN | - |
| 1589 | dc2-leaf1b | Logging | VerifyLoggingSourceInt | Verifies logging source-interface for a specified VRF. | - | NOT RUN | - |
| 1590 | dc2-leaf1b | Logging | VerifyLoggingTimestamp | Verifies if logs are generated with the riate timestamp. | - | NOT RUN | - |
| 1591 | dc2-leaf1b | MLAG | VerifyMlagConfigSanity | Verifies there are no MLAG config-sanity inconsistencies. | - | NOT RUN | - |
| 1592 | dc2-leaf1b | MLAG | VerifyMlagDualPrimary | Verifies the MLAG dual-primary detection parameters. | - | NOT RUN | - |
| 1593 | dc2-leaf1b | MLAG | VerifyMlagInterfaces | Verifies there are no inactive or active-partial MLAG ports. | - | NOT RUN | - |
| 1594 | dc2-leaf1b | MLAG | VerifyMlagReloadDelay | Verifies the MLAG reload-delay parameters. | - | NOT RUN | - |
| 1595 | dc2-leaf1b | MLAG | VerifyMlagStatus | Verifies the health status of the MLAG configuration. | - | NOT RUN | - |
| 1596 | dc2-leaf1b | MLAG | VerifyMlagStatus | Verifies the health status of the MLAG configuration. | - | NOT RUN | - |
| 1597 | dc2-leaf1b | Multicast | VerifyIGMPSnoopingGlobal | Verifies the IGMP snooping global configuration. | - | NOT RUN | - |
| 1598 | dc2-leaf1b | Multicast | VerifyIGMPSnoopingVlans | Verifies the IGMP snooping status for the provided VLANs. | - | NOT RUN | - |
| 1599 | dc2-leaf1b | PTP | VerifyPtpGMStatus | Verifies that the device is locked to a valid PTP Grandmaster. | - | NOT RUN | - |
| 1600 | dc2-leaf1b | PTP | VerifyPtpLockStatus | Verifies that the device was locked to the upstream PTP GM in the last minute. | - | NOT RUN | - |
| 1601 | dc2-leaf1b | PTP | VerifyPtpModeStatus | Verifies that the device is configured as a PTP Boundary Clock. | - | NOT RUN | - |
| 1602 | dc2-leaf1b | PTP | VerifyPtpOffset | Verifies that the PTP timing offset is within +/- 1000ns from the master clock. | - | NOT RUN | - |
| 1603 | dc2-leaf1b | PTP | VerifyPtpPortModeStatus | Verifies the PTP interfaces state. | - | NOT RUN | - |
| 1604 | dc2-leaf1b | Routing | VerifyRoutingProtocolModel | Verifies the configured routing protocol model. | Routing protocol model: multi-agent | NOT RUN | - |
| 1605 | dc2-leaf1b | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.0.1 - Peer: dc1-spine1 | NOT RUN | - |
| 1606 | dc2-leaf1b | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.0.2 - Peer: dc1-spine2 | NOT RUN | - |
| 1607 | dc2-leaf1b | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.0.3 - Peer: dc1-leaf1a | NOT RUN | - |
| 1608 | dc2-leaf1b | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.0.4 - Peer: dc1-leaf1b | NOT RUN | - |
| 1609 | dc2-leaf1b | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.0.5 - Peer: dc1-leaf2a | NOT RUN | - |
| 1610 | dc2-leaf1b | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.1.3 - Peer: dc1-leaf1a | NOT RUN | - |
| 1611 | dc2-leaf1b | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.1.5 - Peer: dc1-leaf2a | NOT RUN | - |
| 1612 | dc2-leaf1b | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.128.11 - Peer: dc2-spine1 | NOT RUN | - |
| 1613 | dc2-leaf1b | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.128.12 - Peer: dc2-spine2 | NOT RUN | - |
| 1614 | dc2-leaf1b | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.128.13 - Peer: dc2-leaf1a | NOT RUN | - |
| 1615 | dc2-leaf1b | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.128.14 - Peer: dc2-leaf1b | NOT RUN | - |
| 1616 | dc2-leaf1b | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.128.15 - Peer: dc2-leaf2a | NOT RUN | - |
| 1617 | dc2-leaf1b | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.128.16 - Peer: dc2-leaf2b | NOT RUN | - |
| 1618 | dc2-leaf1b | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.128.17 - Peer: dc2-leaf3a.arista.com | NOT RUN | - |
| 1619 | dc2-leaf1b | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.128.18 - Peer: dc2-leaf3b.arista.com | NOT RUN | - |
| 1620 | dc2-leaf1b | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.129.13 - Peer: dc2-leaf1a | NOT RUN | - |
| 1621 | dc2-leaf1b | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.129.15 - Peer: dc2-leaf2a | NOT RUN | - |
| 1622 | dc2-leaf1b | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.129.17 - Peer: dc2-leaf3a.arista.com | NOT RUN | - |
| 1623 | dc2-leaf1b | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.2.1 - Peer: dc1-wan1 | NOT RUN | - |
| 1624 | dc2-leaf1b | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.2.2 - Peer: dc1-wan2 | NOT RUN | - |
| 1625 | dc2-leaf1b | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.33.0.5 - Peer: dc1-svc-leaf1a | NOT RUN | - |
| 1626 | dc2-leaf1b | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.33.0.6 - Peer: dc1-svc-leaf1b | NOT RUN | - |
| 1627 | dc2-leaf1b | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.33.1.5 - Peer: dc1-svc-leaf1a | NOT RUN | - |
| 1628 | dc2-leaf1b | Security | VerifyAPIHttpsSSL | Verifies if the eAPI has a valid SSL profile. | - | NOT RUN | - |
| 1629 | dc2-leaf1b | Security | VerifyAPIHttpsSSL | Verifies if the eAPI has a valid SSL profile. | eAPI HTTPS SSL Profile: eAPI_SSL_Profile | NOT RUN | - |
| 1630 | dc2-leaf1b | Security | VerifyAPIHttpStatus | Verifies if eAPI HTTP server is disabled globally. | - | NOT RUN | - |
| 1631 | dc2-leaf1b | Security | VerifyAPIIPv4Acl | Verifies if eAPI has the right number IPv4 ACL(s) configured for a specified VRF. | - | NOT RUN | - |
| 1632 | dc2-leaf1b | Security | VerifyAPIIPv6Acl | Verifies if eAPI has the right number IPv6 ACL(s) configured for a specified VRF. | - | NOT RUN | - |
| 1633 | dc2-leaf1b | Security | VerifyAPISSLCertificate | Verifies the eAPI SSL certificate expiry, common subject name, encryption algorithm and key size. | - | NOT RUN | - |
| 1634 | dc2-leaf1b | Security | VerifyBannerLogin | Verifies the login banner of a device. | - | NOT RUN | - |
| 1635 | dc2-leaf1b | Security | VerifyBannerMotd | Verifies the motd banner of a device. | - | NOT RUN | - |
| 1636 | dc2-leaf1b | Security | VerifyIPSecConnHealth | Verifies all IPv4 security connections. | - | NOT RUN | - |
| 1637 | dc2-leaf1b | Security | VerifyIPv4ACL | Verifies the configuration of IPv4 ACLs. | - | NOT RUN | - |
| 1638 | dc2-leaf1b | Security | VerifySpecificIPSecConn | Verifies IPv4 security connections for a peer. | - | NOT RUN | - |
| 1639 | dc2-leaf1b | Security | VerifySSHIPv4Acl | Verifies if the SSHD agent has IPv4 ACL(s) configured. | - | NOT RUN | - |
| 1640 | dc2-leaf1b | Security | VerifySSHIPv6Acl | Verifies if the SSHD agent has IPv6 ACL(s) configured. | - | NOT RUN | - |
| 1641 | dc2-leaf1b | Security | VerifySSHStatus | Verifies if the SSHD agent is disabled in the default VRF. | - | NOT RUN | - |
| 1642 | dc2-leaf1b | Security | VerifyTelnetStatus | Verifies if Telnet is disabled in the default VRF. | - | NOT RUN | - |
| 1643 | dc2-leaf1b | Services | VerifyDNSLookup | Verifies the DNS name to IP address resolution. | - | NOT RUN | - |
| 1644 | dc2-leaf1b | Services | VerifyDNSServers | Verifies if the DNS servers are correctly configured. | - | NOT RUN | - |
| 1645 | dc2-leaf1b | Services | VerifyErrdisableRecovery | Verifies the errdisable recovery reason, status, and interval. | - | NOT RUN | - |
| 1646 | dc2-leaf1b | Services | VerifyHostname | Verifies the hostname of a device. | - | NOT RUN | - |
| 1647 | dc2-leaf1b | SNMP | VerifySnmpIPv4Acl | Verifies if the SNMP agent has IPv4 ACL(s) configured. | - | NOT RUN | - |
| 1648 | dc2-leaf1b | SNMP | VerifySnmpIPv6Acl | Verifies if the SNMP agent has IPv6 ACL(s) configured. | - | NOT RUN | - |
| 1649 | dc2-leaf1b | SNMP | VerifySnmpStatus | Verifies if the SNMP agent is enabled. | - | NOT RUN | - |
| 1650 | dc2-leaf1b | Software | VerifyEOSVersion | Verifies the EOS version of the device. | - | NOT RUN | - |
| 1651 | dc2-leaf1b | Software | VerifyTerminAttrVersion | Verifies the TerminAttr version of the device. | - | NOT RUN | - |
| 1652 | dc2-leaf1b | STP | VerifySTPBlockedPorts | Verifies there is no STP blocked ports. | - | NOT RUN | - |
| 1653 | dc2-leaf1b | STP | VerifySTPCounters | Verifies there is no errors in STP BPDU packets. | - | NOT RUN | - |
| 1654 | dc2-leaf1b | STP | VerifySTPForwardingPorts | Verifies that all interfaces are forwarding for a provided list of VLAN(s). | - | NOT RUN | - |
| 1655 | dc2-leaf1b | STP | VerifySTPMode | Verifies the configured STP mode for a provided list of VLAN(s). | - | NOT RUN | - |
| 1656 | dc2-leaf1b | STP | VerifySTPRootPriority | Verifies the STP root priority for a provided list of VLAN or MST instance ID(s). | - | NOT RUN | - |
| 1657 | dc2-leaf1b | STUN | VerifyStunClient | Verifies the STUN client is configured with the specified IPv4 source address and port. Validate the public IP and port if provided. | - | NOT RUN | - |
| 1658 | dc2-leaf1b | System | VerifyAgentLogs | Verifies there are no agent crash reports. | - | NOT RUN | - |
| 1659 | dc2-leaf1b | System | VerifyCoredump | Verifies there are no core dump files. | - | NOT RUN | - |
| 1660 | dc2-leaf1b | System | VerifyCPUUtilization | Verifies whether the CPU utilization is below 75%. | - | NOT RUN | - |
| 1661 | dc2-leaf1b | System | VerifyFileSystemUtilization | Verifies that no partition is utilizing more than 75% of its disk space. | - | NOT RUN | - |
| 1662 | dc2-leaf1b | System | VerifyMemoryUtilization | Verifies whether the memory utilization is below 75%. | - | NOT RUN | - |
| 1663 | dc2-leaf1b | System | VerifyNTP | Verifies if NTP is synchronised. | - | NOT RUN | - |
| 1664 | dc2-leaf1b | System | VerifyNTP | Verifies if NTP is synchronised. | - | NOT RUN | - |
| 1665 | dc2-leaf1b | System | VerifyReloadCause | Verifies the last reload cause of the device. | - | NOT RUN | - |
| 1666 | dc2-leaf1b | System | VerifyReloadCause | Verifies the last reload cause of the device. | - | NOT RUN | - |
| 1667 | dc2-leaf1b | System | VerifyUptime | Verifies the device uptime. | - | NOT RUN | - |
| 1668 | dc2-leaf1b | VLAN | VerifyVlanInternalPolicy | Verifies the VLAN internal allocation policy and the range of VLANs. | - | NOT RUN | - |
| 1669 | dc2-leaf1c | AAA | VerifyAcctConsoleMethods | Verifies the AAA accounting console method lists for different accounting types (system, exec, commands, dot1x). | - | NOT RUN | - |
| 1670 | dc2-leaf1c | AAA | VerifyAcctDefaultMethods | Verifies the AAA accounting default method lists for different accounting types (system, exec, commands, dot1x). | - | NOT RUN | - |
| 1671 | dc2-leaf1c | AAA | VerifyAuthenMethods | Verifies the AAA authentication method lists for different authentication types (login, enable, dot1x). | - | NOT RUN | - |
| 1672 | dc2-leaf1c | AAA | VerifyAuthzMethods | Verifies the AAA authorization method lists for different authorization types (commands, exec). | - | NOT RUN | - |
| 1673 | dc2-leaf1c | AAA | VerifyTacacsServerGroups | Verifies if the provided TACACS server group(s) are configured. | - | NOT RUN | - |
| 1674 | dc2-leaf1c | AAA | VerifyTacacsServers | Verifies TACACS servers are configured for a specified VRF. | - | NOT RUN | - |
| 1675 | dc2-leaf1c | AAA | VerifyTacacsSourceIntf | Verifies TACACS source-interface for a specified VRF. | - | NOT RUN | - |
| 1676 | dc2-leaf1c | Configuration | VerifyRunningConfigDiffs | Verifies there is no difference between the running-config and the startup-config | - | NOT RUN | - |
| 1677 | dc2-leaf1c | Configuration | VerifyZeroTouch | Verifies ZeroTouch is disabled | - | NOT RUN | - |
| 1678 | dc2-leaf1c | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet1 - Remote: dc2-leaf1a Ethernet8 | NOT RUN | - |
| 1679 | dc2-leaf1c | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet2 - Remote: dc2-leaf1b Ethernet8 | NOT RUN | - |
| 1680 | dc2-leaf1c | Field Notices | VerifyFieldNotice44Resolution | Verifies that the device is using the correct Aboot version per FN0044. | - | NOT RUN | - |
| 1681 | dc2-leaf1c | Field Notices | VerifyFieldNotice72Resolution | Verifies if the device is exposed to FN0072, and if the issue has been mitigated. | - | NOT RUN | - |
| 1682 | dc2-leaf1c | Greent | VerifyGreenT | Verifies if a GreenT policy is created. | - | NOT RUN | - |
| 1683 | dc2-leaf1c | Greent | VerifyGreenTCounters | Verifies if the GreenT counters are incremented. | - | NOT RUN | - |
| 1684 | dc2-leaf1c | Hardware | VerifyAdverseDrops | Verifies there are no adverse drops on DCS-7280 and DCS-7500 family switches. | - | NOT RUN | - |
| 1685 | dc2-leaf1c | Hardware | VerifyEnvironmentCooling | Verifies the status of power supply fans and all fan trays. | - | NOT RUN | - |
| 1686 | dc2-leaf1c | Hardware | VerifyEnvironmentCooling | Verifies the status of power supply fans and all fan trays. | Accepted States: 'ok' | NOT RUN | - |
| 1687 | dc2-leaf1c | Hardware | VerifyEnvironmentPower | Verifies the power supplies status. | - | NOT RUN | - |
| 1688 | dc2-leaf1c | Hardware | VerifyEnvironmentPower | Verifies the power supplies status. | Accepted States: 'ok' | NOT RUN | - |
| 1689 | dc2-leaf1c | Hardware | VerifyEnvironmentSystemCooling | Verifies the system cooling status. | - | NOT RUN | - |
| 1690 | dc2-leaf1c | Hardware | VerifyTemperature | Verifies the device temperature. | - | NOT RUN | - |
| 1691 | dc2-leaf1c | Hardware | VerifyTemperature | Verifies the device temperature. | - | NOT RUN | - |
| 1692 | dc2-leaf1c | Hardware | VerifyTransceiversManufacturers | Verifies if all transceivers come from approved manufacturers. | - | NOT RUN | - |
| 1693 | dc2-leaf1c | Hardware | VerifyTransceiversManufacturers | Verifies if all transceivers come from approved manufacturers. | Accepted Manufacturers: 'Arista Networks', 'Arastra, Inc.', 'Not Present' | NOT RUN | - |
| 1694 | dc2-leaf1c | Hardware | VerifyTransceiversTemperature | Verifies the transceivers temperature. | - | NOT RUN | - |
| 1695 | dc2-leaf1c | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet1 - DC2-LEAF1A_Ethernet8 = 'up' | NOT RUN | - |
| 1696 | dc2-leaf1c | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet2 - DC2-LEAF1B_Ethernet8 = 'up' | NOT RUN | - |
| 1697 | dc2-leaf1c | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet5 - SERVER_dc2-leaf1-server1_iLO = 'up' | NOT RUN | - |
| 1698 | dc2-leaf1c | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel1 - DC2_L3_LEAF1_Po8 = 'up' | NOT RUN | - |
| 1699 | dc2-leaf1c | LANZ | VerifyLANZ | Verifies if LANZ is enabled. | - | NOT RUN | - |
| 1700 | dc2-leaf1c | PTP | VerifyPtpGMStatus | Verifies that the device is locked to a valid PTP Grandmaster. | - | NOT RUN | - |
| 1701 | dc2-leaf1c | PTP | VerifyPtpLockStatus | Verifies that the device was locked to the upstream PTP GM in the last minute. | - | NOT RUN | - |
| 1702 | dc2-leaf1c | PTP | VerifyPtpModeStatus | Verifies that the device is configured as a PTP Boundary Clock. | - | NOT RUN | - |
| 1703 | dc2-leaf1c | PTP | VerifyPtpOffset | Verifies that the PTP timing offset is within +/- 1000ns from the master clock. | - | NOT RUN | - |
| 1704 | dc2-leaf1c | PTP | VerifyPtpPortModeStatus | Verifies the PTP interfaces state. | - | NOT RUN | - |
| 1705 | dc2-leaf1c | Security | VerifyAPIHttpsSSL | Verifies if the eAPI has a valid SSL profile. | - | NOT RUN | - |
| 1706 | dc2-leaf1c | Security | VerifyAPIHttpsSSL | Verifies if the eAPI has a valid SSL profile. | eAPI HTTPS SSL Profile: eAPI_SSL_Profile | NOT RUN | - |
| 1707 | dc2-leaf1c | Security | VerifyAPIHttpStatus | Verifies if eAPI HTTP server is disabled globally. | - | NOT RUN | - |
| 1708 | dc2-leaf1c | Security | VerifyAPIIPv4Acl | Verifies if eAPI has the right number IPv4 ACL(s) configured for a specified VRF. | - | NOT RUN | - |
| 1709 | dc2-leaf1c | Security | VerifyAPIIPv6Acl | Verifies if eAPI has the right number IPv6 ACL(s) configured for a specified VRF. | - | NOT RUN | - |
| 1710 | dc2-leaf1c | Security | VerifyAPISSLCertificate | Verifies the eAPI SSL certificate expiry, common subject name, encryption algorithm and key size. | - | NOT RUN | - |
| 1711 | dc2-leaf1c | Security | VerifyBannerLogin | Verifies the login banner of a device. | - | NOT RUN | - |
| 1712 | dc2-leaf1c | Security | VerifyBannerMotd | Verifies the motd banner of a device. | - | NOT RUN | - |
| 1713 | dc2-leaf1c | Security | VerifyIPSecConnHealth | Verifies all IPv4 security connections. | - | NOT RUN | - |
| 1714 | dc2-leaf1c | Security | VerifyIPv4ACL | Verifies the configuration of IPv4 ACLs. | - | NOT RUN | - |
| 1715 | dc2-leaf1c | Security | VerifySpecificIPSecConn | Verifies IPv4 security connections for a peer. | - | NOT RUN | - |
| 1716 | dc2-leaf1c | Security | VerifySSHIPv4Acl | Verifies if the SSHD agent has IPv4 ACL(s) configured. | - | NOT RUN | - |
| 1717 | dc2-leaf1c | Security | VerifySSHIPv6Acl | Verifies if the SSHD agent has IPv6 ACL(s) configured. | - | NOT RUN | - |
| 1718 | dc2-leaf1c | Security | VerifySSHStatus | Verifies if the SSHD agent is disabled in the default VRF. | - | NOT RUN | - |
| 1719 | dc2-leaf1c | Security | VerifyTelnetStatus | Verifies if Telnet is disabled in the default VRF. | - | NOT RUN | - |
| 1720 | dc2-leaf1c | Services | VerifyDNSLookup | Verifies the DNS name to IP address resolution. | - | NOT RUN | - |
| 1721 | dc2-leaf1c | Services | VerifyDNSServers | Verifies if the DNS servers are correctly configured. | - | NOT RUN | - |
| 1722 | dc2-leaf1c | Services | VerifyErrdisableRecovery | Verifies the errdisable recovery reason, status, and interval. | - | NOT RUN | - |
| 1723 | dc2-leaf1c | Services | VerifyHostname | Verifies the hostname of a device. | - | NOT RUN | - |
| 1724 | dc2-leaf1c | SNMP | VerifySnmpIPv4Acl | Verifies if the SNMP agent has IPv4 ACL(s) configured. | - | NOT RUN | - |
| 1725 | dc2-leaf1c | SNMP | VerifySnmpIPv6Acl | Verifies if the SNMP agent has IPv6 ACL(s) configured. | - | NOT RUN | - |
| 1726 | dc2-leaf1c | SNMP | VerifySnmpStatus | Verifies if the SNMP agent is enabled. | - | NOT RUN | - |
| 1727 | dc2-leaf1c | Software | VerifyEOSVersion | Verifies the EOS version of the device. | - | NOT RUN | - |
| 1728 | dc2-leaf1c | Software | VerifyTerminAttrVersion | Verifies the TerminAttr version of the device. | - | NOT RUN | - |
| 1729 | dc2-leaf1c | STUN | VerifyStunClient | Verifies the STUN client is configured with the specified IPv4 source address and port. Validate the public IP and port if provided. | - | NOT RUN | - |
| 1730 | dc2-leaf1c | System | VerifyAgentLogs | Verifies there are no agent crash reports. | - | NOT RUN | - |
| 1731 | dc2-leaf1c | System | VerifyCoredump | Verifies there are no core dump files. | - | NOT RUN | - |
| 1732 | dc2-leaf1c | System | VerifyCPUUtilization | Verifies whether the CPU utilization is below 75%. | - | NOT RUN | - |
| 1733 | dc2-leaf1c | System | VerifyFileSystemUtilization | Verifies that no partition is utilizing more than 75% of its disk space. | - | NOT RUN | - |
| 1734 | dc2-leaf1c | System | VerifyMemoryUtilization | Verifies whether the memory utilization is below 75%. | - | NOT RUN | - |
| 1735 | dc2-leaf1c | System | VerifyNTP | Verifies if NTP is synchronised. | - | NOT RUN | - |
| 1736 | dc2-leaf1c | System | VerifyNTP | Verifies if NTP is synchronised. | - | NOT RUN | - |
| 1737 | dc2-leaf1c | System | VerifyReloadCause | Verifies the last reload cause of the device. | - | NOT RUN | - |
| 1738 | dc2-leaf1c | System | VerifyReloadCause | Verifies the last reload cause of the device. | - | NOT RUN | - |
| 1739 | dc2-leaf1c | System | VerifyUptime | Verifies the device uptime. | - | NOT RUN | - |
| 1740 | dc2-leaf1c | VLAN | VerifyVlanInternalPolicy | Verifies the VLAN internal allocation policy and the range of VLANs. | - | NOT RUN | - |
| 1741 | dc2-leaf2a | AAA | VerifyAcctConsoleMethods | Verifies the AAA accounting console method lists for different accounting types (system, exec, commands, dot1x). | - | NOT RUN | - |
| 1742 | dc2-leaf2a | AAA | VerifyAcctDefaultMethods | Verifies the AAA accounting default method lists for different accounting types (system, exec, commands, dot1x). | - | NOT RUN | - |
| 1743 | dc2-leaf2a | AAA | VerifyAuthenMethods | Verifies the AAA authentication method lists for different authentication types (login, enable, dot1x). | - | NOT RUN | - |
| 1744 | dc2-leaf2a | AAA | VerifyAuthzMethods | Verifies the AAA authorization method lists for different authorization types (commands, exec). | - | NOT RUN | - |
| 1745 | dc2-leaf2a | AAA | VerifyTacacsServerGroups | Verifies if the provided TACACS server group(s) are configured. | - | NOT RUN | - |
| 1746 | dc2-leaf2a | AAA | VerifyTacacsServers | Verifies TACACS servers are configured for a specified VRF. | - | NOT RUN | - |
| 1747 | dc2-leaf2a | AAA | VerifyTacacsSourceIntf | Verifies TACACS source-interface for a specified VRF. | - | NOT RUN | - |
| 1748 | dc2-leaf2a | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: dc1-leaf2a (IP: 10.255.0.5) | NOT RUN | - |
| 1749 | dc2-leaf2a | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: dc2-spine1 (IP: 10.255.128.11) | NOT RUN | - |
| 1750 | dc2-leaf2a | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: dc2-spine2 (IP: 10.255.128.12) | NOT RUN | - |
| 1751 | dc2-leaf2a | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: dc1-leaf2a (IP: 192.168.100.0) | NOT RUN | - |
| 1752 | dc2-leaf2a | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: dc2-leaf2b (IP: 10.255.129.121) | NOT RUN | - |
| 1753 | dc2-leaf2a | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: dc2-spine1 (IP: 10.255.255.112) | NOT RUN | - |
| 1754 | dc2-leaf2a | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: dc2-spine2 (IP: 10.255.255.114) | NOT RUN | - |
| 1755 | dc2-leaf2a | Configuration | VerifyRunningConfigDiffs | Verifies there is no difference between the running-config and the startup-config | - | NOT RUN | - |
| 1756 | dc2-leaf2a | Configuration | VerifyZeroTouch | Verifies ZeroTouch is disabled | - | NOT RUN | - |
| 1757 | dc2-leaf2a | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet1 - Remote: dc2-spine1 Ethernet3 | NOT RUN | - |
| 1758 | dc2-leaf2a | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet2 - Remote: dc2-spine2 Ethernet3 | NOT RUN | - |
| 1759 | dc2-leaf2a | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet3 - Remote: dc2-leaf2b Ethernet3 | NOT RUN | - |
| 1760 | dc2-leaf2a | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet4 - Remote: dc2-leaf2b Ethernet4 | NOT RUN | - |
| 1761 | dc2-leaf2a | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet6 - Remote: dc1-leaf2a Ethernet6 | NOT RUN | - |
| 1762 | dc2-leaf2a | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet8 - Remote: dc2-leaf2c Ethernet1 | NOT RUN | - |
| 1763 | dc2-leaf2a | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.128.15) - Destination: dc1-leaf1a Loopback0 (IP: 10.255.0.3) | NOT RUN | - |
| 1764 | dc2-leaf2a | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.128.15) - Destination: dc1-leaf1b Loopback0 (IP: 10.255.0.4) | NOT RUN | - |
| 1765 | dc2-leaf2a | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.128.15) - Destination: dc1-leaf2a Loopback0 (IP: 10.255.0.5) | NOT RUN | - |
| 1766 | dc2-leaf2a | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.128.15) - Destination: dc1-spine1 Loopback0 (IP: 10.255.0.1) | NOT RUN | - |
| 1767 | dc2-leaf2a | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.128.15) - Destination: dc1-spine2 Loopback0 (IP: 10.255.0.2) | NOT RUN | - |
| 1768 | dc2-leaf2a | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.128.15) - Destination: dc1-svc-leaf1a Loopback0 (IP: 10.33.0.5) | NOT RUN | - |
| 1769 | dc2-leaf2a | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.128.15) - Destination: dc1-svc-leaf1b Loopback0 (IP: 10.33.0.6) | NOT RUN | - |
| 1770 | dc2-leaf2a | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.128.15) - Destination: dc1-wan1 Loopback0 (IP: 10.255.2.1) | NOT RUN | - |
| 1771 | dc2-leaf2a | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.128.15) - Destination: dc1-wan2 Loopback0 (IP: 10.255.2.2) | NOT RUN | - |
| 1772 | dc2-leaf2a | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.128.15) - Destination: dc2-leaf1a Loopback0 (IP: 10.255.128.13) | NOT RUN | - |
| 1773 | dc2-leaf2a | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.128.15) - Destination: dc2-leaf1b Loopback0 (IP: 10.255.128.14) | NOT RUN | - |
| 1774 | dc2-leaf2a | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.128.15) - Destination: dc2-leaf2a Loopback0 (IP: 10.255.128.15) | NOT RUN | - |
| 1775 | dc2-leaf2a | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.128.15) - Destination: dc2-leaf2b Loopback0 (IP: 10.255.128.16) | NOT RUN | - |
| 1776 | dc2-leaf2a | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.128.15) - Destination: dc2-leaf3a.arista.com Loopback0 (IP: 10.255.128.17) | NOT RUN | - |
| 1777 | dc2-leaf2a | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.128.15) - Destination: dc2-leaf3b.arista.com Loopback0 (IP: 10.255.128.18) | NOT RUN | - |
| 1778 | dc2-leaf2a | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.128.15) - Destination: dc2-spine1 Loopback0 (IP: 10.255.128.11) | NOT RUN | - |
| 1779 | dc2-leaf2a | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.128.15) - Destination: dc2-spine2 Loopback0 (IP: 10.255.128.12) | NOT RUN | - |
| 1780 | dc2-leaf2a | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet1 (IP: 10.255.255.113) - Destination: dc2-spine1 Ethernet3 (IP: 10.255.255.112) | NOT RUN | - |
| 1781 | dc2-leaf2a | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet2 (IP: 10.255.255.115) - Destination: dc2-spine2 Ethernet3 (IP: 10.255.255.114) | NOT RUN | - |
| 1782 | dc2-leaf2a | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet6 (IP: 192.168.100.1) - Destination: dc1-leaf2a Ethernet6 (IP: 192.168.100.0) | NOT RUN | - |
| 1783 | dc2-leaf2a | Field Notices | VerifyFieldNotice44Resolution | Verifies that the device is using the correct Aboot version per FN0044. | - | NOT RUN | - |
| 1784 | dc2-leaf2a | Field Notices | VerifyFieldNotice72Resolution | Verifies if the device is exposed to FN0072, and if the issue has been mitigated. | - | NOT RUN | - |
| 1785 | dc2-leaf2a | Greent | VerifyGreenT | Verifies if a GreenT policy is created. | - | NOT RUN | - |
| 1786 | dc2-leaf2a | Greent | VerifyGreenTCounters | Verifies if the GreenT counters are incremented. | - | NOT RUN | - |
| 1787 | dc2-leaf2a | Hardware | VerifyAdverseDrops | Verifies there are no adverse drops on DCS-7280 and DCS-7500 family switches. | - | NOT RUN | - |
| 1788 | dc2-leaf2a | Hardware | VerifyEnvironmentCooling | Verifies the status of power supply fans and all fan trays. | - | NOT RUN | - |
| 1789 | dc2-leaf2a | Hardware | VerifyEnvironmentCooling | Verifies the status of power supply fans and all fan trays. | Accepted States: 'ok' | NOT RUN | - |
| 1790 | dc2-leaf2a | Hardware | VerifyEnvironmentPower | Verifies the power supplies status. | - | NOT RUN | - |
| 1791 | dc2-leaf2a | Hardware | VerifyEnvironmentPower | Verifies the power supplies status. | Accepted States: 'ok' | NOT RUN | - |
| 1792 | dc2-leaf2a | Hardware | VerifyEnvironmentSystemCooling | Verifies the system cooling status. | - | NOT RUN | - |
| 1793 | dc2-leaf2a | Hardware | VerifyTemperature | Verifies the device temperature. | - | NOT RUN | - |
| 1794 | dc2-leaf2a | Hardware | VerifyTemperature | Verifies the device temperature. | - | NOT RUN | - |
| 1795 | dc2-leaf2a | Hardware | VerifyTransceiversManufacturers | Verifies if all transceivers come from approved manufacturers. | - | NOT RUN | - |
| 1796 | dc2-leaf2a | Hardware | VerifyTransceiversManufacturers | Verifies if all transceivers come from approved manufacturers. | Accepted Manufacturers: 'Arista Networks', 'Arastra, Inc.', 'Not Present' | NOT RUN | - |
| 1797 | dc2-leaf2a | Hardware | VerifyTransceiversTemperature | Verifies the transceivers temperature. | - | NOT RUN | - |
| 1798 | dc2-leaf2a | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet1 - P2P_LINK_TO_DC2-SPINE1_Ethernet3 = 'up' | NOT RUN | - |
| 1799 | dc2-leaf2a | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet2 - P2P_LINK_TO_DC2-SPINE2_Ethernet3 = 'up' | NOT RUN | - |
| 1800 | dc2-leaf2a | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet3 - MLAG_dc2-leaf2b_Ethernet3 = 'up' | NOT RUN | - |
| 1801 | dc2-leaf2a | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet4 - MLAG_dc2-leaf2b_Ethernet4 = 'up' | NOT RUN | - |
| 1802 | dc2-leaf2a | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet5 - SERVER_dc2-leaf2-server1_PCI1 = 'up' | NOT RUN | - |
| 1803 | dc2-leaf2a | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet6 - P2P_LINK_TO_dc1-leaf2a_Ethernet6 = 'up' | NOT RUN | - |
| 1804 | dc2-leaf2a | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet8 - DC2-LEAF2C_Ethernet1 = 'up' | NOT RUN | - |
| 1805 | dc2-leaf2a | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback0 - ROUTER_ID = 'up' | NOT RUN | - |
| 1806 | dc2-leaf2a | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback1 - VXLAN_TUNNEL_SOURCE = 'up' | NOT RUN | - |
| 1807 | dc2-leaf2a | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback10 - VRF10_VTEP_DIAGNOSTICS = 'up' | NOT RUN | - |
| 1808 | dc2-leaf2a | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback11 - VRF11_VTEP_DIAGNOSTICS = 'up' | NOT RUN | - |
| 1809 | dc2-leaf2a | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel3 - MLAG_dc2-leaf2b_Port-Channel3 = 'up' | NOT RUN | - |
| 1810 | dc2-leaf2a | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel5 - SERVER_dc2-leaf2-server1_PortChannel dc2-leaf2-server1 = 'up' | NOT RUN | - |
| 1811 | dc2-leaf2a | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel8 - DC2-LEAF2C_Po1 = 'up' | NOT RUN | - |
| 1812 | dc2-leaf2a | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan11 - VRF10_VLAN11 = 'up' | NOT RUN | - |
| 1813 | dc2-leaf2a | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan12 - VRF10_VLAN12 = 'up' | NOT RUN | - |
| 1814 | dc2-leaf2a | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan21 - VRF11_VLAN21 = 'up' | NOT RUN | - |
| 1815 | dc2-leaf2a | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan22 - VRF11_VLAN22 = 'up' | NOT RUN | - |
| 1816 | dc2-leaf2a | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan3009 - MLAG_L3_VRF_VRF10 = 'up' | NOT RUN | - |
| 1817 | dc2-leaf2a | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan3010 - MLAG_L3_VRF_VRF11 = 'up' | NOT RUN | - |
| 1818 | dc2-leaf2a | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan4093 - MLAG_L3 = 'up' | NOT RUN | - |
| 1819 | dc2-leaf2a | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan4094 - MLAG = 'up' | NOT RUN | - |
| 1820 | dc2-leaf2a | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vxlan1 = 'up' | NOT RUN | - |
| 1821 | dc2-leaf2a | LANZ | VerifyLANZ | Verifies if LANZ is enabled. | - | NOT RUN | - |
| 1822 | dc2-leaf2a | Logging | VerifyLoggingAccounting | Verifies if AAA accounting logs are generated. | - | NOT RUN | - |
| 1823 | dc2-leaf2a | Logging | VerifyLoggingErrors | Verifies there are no syslog messages with a severity of ERRORS or higher. | - | NOT RUN | - |
| 1824 | dc2-leaf2a | Logging | VerifyLoggingHostname | Verifies if logs are generated with the device FQDN. | - | NOT RUN | - |
| 1825 | dc2-leaf2a | Logging | VerifyLoggingHosts | Verifies logging hosts (syslog servers) for a specified VRF. | - | NOT RUN | - |
| 1826 | dc2-leaf2a | Logging | VerifyLoggingLogsGeneration | Verifies if logs are generated. | - | NOT RUN | - |
| 1827 | dc2-leaf2a | Logging | VerifyLoggingPersistent | Verifies if logging persistent is enabled and logs are saved in flash. | - | NOT RUN | - |
| 1828 | dc2-leaf2a | Logging | VerifyLoggingSourceInt | Verifies logging source-interface for a specified VRF. | - | NOT RUN | - |
| 1829 | dc2-leaf2a | Logging | VerifyLoggingTimestamp | Verifies if logs are generated with the riate timestamp. | - | NOT RUN | - |
| 1830 | dc2-leaf2a | MLAG | VerifyMlagConfigSanity | Verifies there are no MLAG config-sanity inconsistencies. | - | NOT RUN | - |
| 1831 | dc2-leaf2a | MLAG | VerifyMlagDualPrimary | Verifies the MLAG dual-primary detection parameters. | - | NOT RUN | - |
| 1832 | dc2-leaf2a | MLAG | VerifyMlagInterfaces | Verifies there are no inactive or active-partial MLAG ports. | - | NOT RUN | - |
| 1833 | dc2-leaf2a | MLAG | VerifyMlagReloadDelay | Verifies the MLAG reload-delay parameters. | - | NOT RUN | - |
| 1834 | dc2-leaf2a | MLAG | VerifyMlagStatus | Verifies the health status of the MLAG configuration. | - | NOT RUN | - |
| 1835 | dc2-leaf2a | MLAG | VerifyMlagStatus | Verifies the health status of the MLAG configuration. | - | NOT RUN | - |
| 1836 | dc2-leaf2a | Multicast | VerifyIGMPSnoopingGlobal | Verifies the IGMP snooping global configuration. | - | NOT RUN | - |
| 1837 | dc2-leaf2a | Multicast | VerifyIGMPSnoopingVlans | Verifies the IGMP snooping status for the provided VLANs. | - | NOT RUN | - |
| 1838 | dc2-leaf2a | PTP | VerifyPtpGMStatus | Verifies that the device is locked to a valid PTP Grandmaster. | - | NOT RUN | - |
| 1839 | dc2-leaf2a | PTP | VerifyPtpLockStatus | Verifies that the device was locked to the upstream PTP GM in the last minute. | - | NOT RUN | - |
| 1840 | dc2-leaf2a | PTP | VerifyPtpModeStatus | Verifies that the device is configured as a PTP Boundary Clock. | - | NOT RUN | - |
| 1841 | dc2-leaf2a | PTP | VerifyPtpOffset | Verifies that the PTP timing offset is within +/- 1000ns from the master clock. | - | NOT RUN | - |
| 1842 | dc2-leaf2a | PTP | VerifyPtpPortModeStatus | Verifies the PTP interfaces state. | - | NOT RUN | - |
| 1843 | dc2-leaf2a | Routing | VerifyRoutingProtocolModel | Verifies the configured routing protocol model. | Routing protocol model: multi-agent | NOT RUN | - |
| 1844 | dc2-leaf2a | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.0.1 - Peer: dc1-spine1 | NOT RUN | - |
| 1845 | dc2-leaf2a | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.0.2 - Peer: dc1-spine2 | NOT RUN | - |
| 1846 | dc2-leaf2a | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.0.3 - Peer: dc1-leaf1a | NOT RUN | - |
| 1847 | dc2-leaf2a | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.0.4 - Peer: dc1-leaf1b | NOT RUN | - |
| 1848 | dc2-leaf2a | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.0.5 - Peer: dc1-leaf2a | NOT RUN | - |
| 1849 | dc2-leaf2a | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.1.3 - Peer: dc1-leaf1a | NOT RUN | - |
| 1850 | dc2-leaf2a | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.1.5 - Peer: dc1-leaf2a | NOT RUN | - |
| 1851 | dc2-leaf2a | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.128.11 - Peer: dc2-spine1 | NOT RUN | - |
| 1852 | dc2-leaf2a | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.128.12 - Peer: dc2-spine2 | NOT RUN | - |
| 1853 | dc2-leaf2a | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.128.13 - Peer: dc2-leaf1a | NOT RUN | - |
| 1854 | dc2-leaf2a | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.128.14 - Peer: dc2-leaf1b | NOT RUN | - |
| 1855 | dc2-leaf2a | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.128.15 - Peer: dc2-leaf2a | NOT RUN | - |
| 1856 | dc2-leaf2a | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.128.16 - Peer: dc2-leaf2b | NOT RUN | - |
| 1857 | dc2-leaf2a | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.128.17 - Peer: dc2-leaf3a.arista.com | NOT RUN | - |
| 1858 | dc2-leaf2a | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.128.18 - Peer: dc2-leaf3b.arista.com | NOT RUN | - |
| 1859 | dc2-leaf2a | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.129.13 - Peer: dc2-leaf1a | NOT RUN | - |
| 1860 | dc2-leaf2a | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.129.15 - Peer: dc2-leaf2a | NOT RUN | - |
| 1861 | dc2-leaf2a | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.129.17 - Peer: dc2-leaf3a.arista.com | NOT RUN | - |
| 1862 | dc2-leaf2a | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.2.1 - Peer: dc1-wan1 | NOT RUN | - |
| 1863 | dc2-leaf2a | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.2.2 - Peer: dc1-wan2 | NOT RUN | - |
| 1864 | dc2-leaf2a | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.33.0.5 - Peer: dc1-svc-leaf1a | NOT RUN | - |
| 1865 | dc2-leaf2a | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.33.0.6 - Peer: dc1-svc-leaf1b | NOT RUN | - |
| 1866 | dc2-leaf2a | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.33.1.5 - Peer: dc1-svc-leaf1a | NOT RUN | - |
| 1867 | dc2-leaf2a | Security | VerifyAPIHttpsSSL | Verifies if the eAPI has a valid SSL profile. | - | NOT RUN | - |
| 1868 | dc2-leaf2a | Security | VerifyAPIHttpsSSL | Verifies if the eAPI has a valid SSL profile. | eAPI HTTPS SSL Profile: eAPI_SSL_Profile | NOT RUN | - |
| 1869 | dc2-leaf2a | Security | VerifyAPIHttpStatus | Verifies if eAPI HTTP server is disabled globally. | - | NOT RUN | - |
| 1870 | dc2-leaf2a | Security | VerifyAPIIPv4Acl | Verifies if eAPI has the right number IPv4 ACL(s) configured for a specified VRF. | - | NOT RUN | - |
| 1871 | dc2-leaf2a | Security | VerifyAPIIPv6Acl | Verifies if eAPI has the right number IPv6 ACL(s) configured for a specified VRF. | - | NOT RUN | - |
| 1872 | dc2-leaf2a | Security | VerifyAPISSLCertificate | Verifies the eAPI SSL certificate expiry, common subject name, encryption algorithm and key size. | - | NOT RUN | - |
| 1873 | dc2-leaf2a | Security | VerifyBannerLogin | Verifies the login banner of a device. | - | NOT RUN | - |
| 1874 | dc2-leaf2a | Security | VerifyBannerMotd | Verifies the motd banner of a device. | - | NOT RUN | - |
| 1875 | dc2-leaf2a | Security | VerifyIPSecConnHealth | Verifies all IPv4 security connections. | - | NOT RUN | - |
| 1876 | dc2-leaf2a | Security | VerifyIPv4ACL | Verifies the configuration of IPv4 ACLs. | - | NOT RUN | - |
| 1877 | dc2-leaf2a | Security | VerifySpecificIPSecConn | Verifies IPv4 security connections for a peer. | - | NOT RUN | - |
| 1878 | dc2-leaf2a | Security | VerifySSHIPv4Acl | Verifies if the SSHD agent has IPv4 ACL(s) configured. | - | NOT RUN | - |
| 1879 | dc2-leaf2a | Security | VerifySSHIPv6Acl | Verifies if the SSHD agent has IPv6 ACL(s) configured. | - | NOT RUN | - |
| 1880 | dc2-leaf2a | Security | VerifySSHStatus | Verifies if the SSHD agent is disabled in the default VRF. | - | NOT RUN | - |
| 1881 | dc2-leaf2a | Security | VerifyTelnetStatus | Verifies if Telnet is disabled in the default VRF. | - | NOT RUN | - |
| 1882 | dc2-leaf2a | Services | VerifyDNSLookup | Verifies the DNS name to IP address resolution. | - | NOT RUN | - |
| 1883 | dc2-leaf2a | Services | VerifyDNSServers | Verifies if the DNS servers are correctly configured. | - | NOT RUN | - |
| 1884 | dc2-leaf2a | Services | VerifyErrdisableRecovery | Verifies the errdisable recovery reason, status, and interval. | - | NOT RUN | - |
| 1885 | dc2-leaf2a | Services | VerifyHostname | Verifies the hostname of a device. | - | NOT RUN | - |
| 1886 | dc2-leaf2a | SNMP | VerifySnmpIPv4Acl | Verifies if the SNMP agent has IPv4 ACL(s) configured. | - | NOT RUN | - |
| 1887 | dc2-leaf2a | SNMP | VerifySnmpIPv6Acl | Verifies if the SNMP agent has IPv6 ACL(s) configured. | - | NOT RUN | - |
| 1888 | dc2-leaf2a | SNMP | VerifySnmpStatus | Verifies if the SNMP agent is enabled. | - | NOT RUN | - |
| 1889 | dc2-leaf2a | Software | VerifyEOSVersion | Verifies the EOS version of the device. | - | NOT RUN | - |
| 1890 | dc2-leaf2a | Software | VerifyTerminAttrVersion | Verifies the TerminAttr version of the device. | - | NOT RUN | - |
| 1891 | dc2-leaf2a | STP | VerifySTPBlockedPorts | Verifies there is no STP blocked ports. | - | NOT RUN | - |
| 1892 | dc2-leaf2a | STP | VerifySTPCounters | Verifies there is no errors in STP BPDU packets. | - | NOT RUN | - |
| 1893 | dc2-leaf2a | STP | VerifySTPForwardingPorts | Verifies that all interfaces are forwarding for a provided list of VLAN(s). | - | NOT RUN | - |
| 1894 | dc2-leaf2a | STP | VerifySTPMode | Verifies the configured STP mode for a provided list of VLAN(s). | - | NOT RUN | - |
| 1895 | dc2-leaf2a | STP | VerifySTPRootPriority | Verifies the STP root priority for a provided list of VLAN or MST instance ID(s). | - | NOT RUN | - |
| 1896 | dc2-leaf2a | STUN | VerifyStunClient | Verifies the STUN client is configured with the specified IPv4 source address and port. Validate the public IP and port if provided. | - | NOT RUN | - |
| 1897 | dc2-leaf2a | System | VerifyAgentLogs | Verifies there are no agent crash reports. | - | NOT RUN | - |
| 1898 | dc2-leaf2a | System | VerifyCoredump | Verifies there are no core dump files. | - | NOT RUN | - |
| 1899 | dc2-leaf2a | System | VerifyCPUUtilization | Verifies whether the CPU utilization is below 75%. | - | NOT RUN | - |
| 1900 | dc2-leaf2a | System | VerifyFileSystemUtilization | Verifies that no partition is utilizing more than 75% of its disk space. | - | NOT RUN | - |
| 1901 | dc2-leaf2a | System | VerifyMemoryUtilization | Verifies whether the memory utilization is below 75%. | - | NOT RUN | - |
| 1902 | dc2-leaf2a | System | VerifyNTP | Verifies if NTP is synchronised. | - | NOT RUN | - |
| 1903 | dc2-leaf2a | System | VerifyNTP | Verifies if NTP is synchronised. | - | NOT RUN | - |
| 1904 | dc2-leaf2a | System | VerifyReloadCause | Verifies the last reload cause of the device. | - | NOT RUN | - |
| 1905 | dc2-leaf2a | System | VerifyReloadCause | Verifies the last reload cause of the device. | - | NOT RUN | - |
| 1906 | dc2-leaf2a | System | VerifyUptime | Verifies the device uptime. | - | NOT RUN | - |
| 1907 | dc2-leaf2a | VLAN | VerifyVlanInternalPolicy | Verifies the VLAN internal allocation policy and the range of VLANs. | - | NOT RUN | - |
| 1908 | dc2-leaf2b | AAA | VerifyAcctConsoleMethods | Verifies the AAA accounting console method lists for different accounting types (system, exec, commands, dot1x). | - | NOT RUN | - |
| 1909 | dc2-leaf2b | AAA | VerifyAcctDefaultMethods | Verifies the AAA accounting default method lists for different accounting types (system, exec, commands, dot1x). | - | NOT RUN | - |
| 1910 | dc2-leaf2b | AAA | VerifyAuthenMethods | Verifies the AAA authentication method lists for different authentication types (login, enable, dot1x). | - | NOT RUN | - |
| 1911 | dc2-leaf2b | AAA | VerifyAuthzMethods | Verifies the AAA authorization method lists for different authorization types (commands, exec). | - | NOT RUN | - |
| 1912 | dc2-leaf2b | AAA | VerifyTacacsServerGroups | Verifies if the provided TACACS server group(s) are configured. | - | NOT RUN | - |
| 1913 | dc2-leaf2b | AAA | VerifyTacacsServers | Verifies TACACS servers are configured for a specified VRF. | - | NOT RUN | - |
| 1914 | dc2-leaf2b | AAA | VerifyTacacsSourceIntf | Verifies TACACS source-interface for a specified VRF. | - | NOT RUN | - |
| 1915 | dc2-leaf2b | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: dc2-spine1 (IP: 10.255.128.11) | NOT RUN | - |
| 1916 | dc2-leaf2b | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: dc2-spine2 (IP: 10.255.128.12) | NOT RUN | - |
| 1917 | dc2-leaf2b | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: dc2-leaf2a (IP: 10.255.129.120) | NOT RUN | - |
| 1918 | dc2-leaf2b | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: dc2-spine1 (IP: 10.255.255.116) | NOT RUN | - |
| 1919 | dc2-leaf2b | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: dc2-spine2 (IP: 10.255.255.118) | NOT RUN | - |
| 1920 | dc2-leaf2b | Configuration | VerifyRunningConfigDiffs | Verifies there is no difference between the running-config and the startup-config | - | NOT RUN | - |
| 1921 | dc2-leaf2b | Configuration | VerifyZeroTouch | Verifies ZeroTouch is disabled | - | NOT RUN | - |
| 1922 | dc2-leaf2b | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet1 - Remote: dc2-spine1 Ethernet4 | NOT RUN | - |
| 1923 | dc2-leaf2b | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet2 - Remote: dc2-spine2 Ethernet4 | NOT RUN | - |
| 1924 | dc2-leaf2b | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet3 - Remote: dc2-leaf2a Ethernet3 | NOT RUN | - |
| 1925 | dc2-leaf2b | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet4 - Remote: dc2-leaf2a Ethernet4 | NOT RUN | - |
| 1926 | dc2-leaf2b | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet8 - Remote: dc2-leaf2c Ethernet2 | NOT RUN | - |
| 1927 | dc2-leaf2b | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.128.16) - Destination: dc1-leaf1a Loopback0 (IP: 10.255.0.3) | NOT RUN | - |
| 1928 | dc2-leaf2b | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.128.16) - Destination: dc1-leaf1b Loopback0 (IP: 10.255.0.4) | NOT RUN | - |
| 1929 | dc2-leaf2b | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.128.16) - Destination: dc1-leaf2a Loopback0 (IP: 10.255.0.5) | NOT RUN | - |
| 1930 | dc2-leaf2b | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.128.16) - Destination: dc1-spine1 Loopback0 (IP: 10.255.0.1) | NOT RUN | - |
| 1931 | dc2-leaf2b | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.128.16) - Destination: dc1-spine2 Loopback0 (IP: 10.255.0.2) | NOT RUN | - |
| 1932 | dc2-leaf2b | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.128.16) - Destination: dc1-svc-leaf1a Loopback0 (IP: 10.33.0.5) | NOT RUN | - |
| 1933 | dc2-leaf2b | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.128.16) - Destination: dc1-svc-leaf1b Loopback0 (IP: 10.33.0.6) | NOT RUN | - |
| 1934 | dc2-leaf2b | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.128.16) - Destination: dc1-wan1 Loopback0 (IP: 10.255.2.1) | NOT RUN | - |
| 1935 | dc2-leaf2b | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.128.16) - Destination: dc1-wan2 Loopback0 (IP: 10.255.2.2) | NOT RUN | - |
| 1936 | dc2-leaf2b | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.128.16) - Destination: dc2-leaf1a Loopback0 (IP: 10.255.128.13) | NOT RUN | - |
| 1937 | dc2-leaf2b | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.128.16) - Destination: dc2-leaf1b Loopback0 (IP: 10.255.128.14) | NOT RUN | - |
| 1938 | dc2-leaf2b | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.128.16) - Destination: dc2-leaf2a Loopback0 (IP: 10.255.128.15) | NOT RUN | - |
| 1939 | dc2-leaf2b | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.128.16) - Destination: dc2-leaf2b Loopback0 (IP: 10.255.128.16) | NOT RUN | - |
| 1940 | dc2-leaf2b | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.128.16) - Destination: dc2-leaf3a.arista.com Loopback0 (IP: 10.255.128.17) | NOT RUN | - |
| 1941 | dc2-leaf2b | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.128.16) - Destination: dc2-leaf3b.arista.com Loopback0 (IP: 10.255.128.18) | NOT RUN | - |
| 1942 | dc2-leaf2b | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.128.16) - Destination: dc2-spine1 Loopback0 (IP: 10.255.128.11) | NOT RUN | - |
| 1943 | dc2-leaf2b | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.128.16) - Destination: dc2-spine2 Loopback0 (IP: 10.255.128.12) | NOT RUN | - |
| 1944 | dc2-leaf2b | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet1 (IP: 10.255.255.117) - Destination: dc2-spine1 Ethernet4 (IP: 10.255.255.116) | NOT RUN | - |
| 1945 | dc2-leaf2b | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet2 (IP: 10.255.255.119) - Destination: dc2-spine2 Ethernet4 (IP: 10.255.255.118) | NOT RUN | - |
| 1946 | dc2-leaf2b | Field Notices | VerifyFieldNotice44Resolution | Verifies that the device is using the correct Aboot version per FN0044. | - | NOT RUN | - |
| 1947 | dc2-leaf2b | Field Notices | VerifyFieldNotice72Resolution | Verifies if the device is exposed to FN0072, and if the issue has been mitigated. | - | NOT RUN | - |
| 1948 | dc2-leaf2b | Greent | VerifyGreenT | Verifies if a GreenT policy is created. | - | NOT RUN | - |
| 1949 | dc2-leaf2b | Greent | VerifyGreenTCounters | Verifies if the GreenT counters are incremented. | - | NOT RUN | - |
| 1950 | dc2-leaf2b | Hardware | VerifyAdverseDrops | Verifies there are no adverse drops on DCS-7280 and DCS-7500 family switches. | - | NOT RUN | - |
| 1951 | dc2-leaf2b | Hardware | VerifyEnvironmentCooling | Verifies the status of power supply fans and all fan trays. | - | NOT RUN | - |
| 1952 | dc2-leaf2b | Hardware | VerifyEnvironmentCooling | Verifies the status of power supply fans and all fan trays. | Accepted States: 'ok' | NOT RUN | - |
| 1953 | dc2-leaf2b | Hardware | VerifyEnvironmentPower | Verifies the power supplies status. | - | NOT RUN | - |
| 1954 | dc2-leaf2b | Hardware | VerifyEnvironmentPower | Verifies the power supplies status. | Accepted States: 'ok' | NOT RUN | - |
| 1955 | dc2-leaf2b | Hardware | VerifyEnvironmentSystemCooling | Verifies the system cooling status. | - | NOT RUN | - |
| 1956 | dc2-leaf2b | Hardware | VerifyTemperature | Verifies the device temperature. | - | NOT RUN | - |
| 1957 | dc2-leaf2b | Hardware | VerifyTemperature | Verifies the device temperature. | - | NOT RUN | - |
| 1958 | dc2-leaf2b | Hardware | VerifyTransceiversManufacturers | Verifies if all transceivers come from approved manufacturers. | - | NOT RUN | - |
| 1959 | dc2-leaf2b | Hardware | VerifyTransceiversManufacturers | Verifies if all transceivers come from approved manufacturers. | Accepted Manufacturers: 'Arista Networks', 'Arastra, Inc.', 'Not Present' | NOT RUN | - |
| 1960 | dc2-leaf2b | Hardware | VerifyTransceiversTemperature | Verifies the transceivers temperature. | - | NOT RUN | - |
| 1961 | dc2-leaf2b | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet1 - P2P_LINK_TO_DC2-SPINE1_Ethernet4 = 'up' | NOT RUN | - |
| 1962 | dc2-leaf2b | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet2 - P2P_LINK_TO_DC2-SPINE2_Ethernet4 = 'up' | NOT RUN | - |
| 1963 | dc2-leaf2b | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet3 - MLAG_dc2-leaf2a_Ethernet3 = 'up' | NOT RUN | - |
| 1964 | dc2-leaf2b | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet4 - MLAG_dc2-leaf2a_Ethernet4 = 'up' | NOT RUN | - |
| 1965 | dc2-leaf2b | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet5 - SERVER_dc2-leaf2-server1_PCI2 = 'up' | NOT RUN | - |
| 1966 | dc2-leaf2b | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet6 - P2P_LINK_TO_dc1-leaf2b_Ethernet6 = 'up' | NOT RUN | - |
| 1967 | dc2-leaf2b | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet8 - DC2-LEAF2C_Ethernet2 = 'up' | NOT RUN | - |
| 1968 | dc2-leaf2b | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback0 - ROUTER_ID = 'up' | NOT RUN | - |
| 1969 | dc2-leaf2b | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback1 - VXLAN_TUNNEL_SOURCE = 'up' | NOT RUN | - |
| 1970 | dc2-leaf2b | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback10 - VRF10_VTEP_DIAGNOSTICS = 'up' | NOT RUN | - |
| 1971 | dc2-leaf2b | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback11 - VRF11_VTEP_DIAGNOSTICS = 'up' | NOT RUN | - |
| 1972 | dc2-leaf2b | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel3 - MLAG_dc2-leaf2a_Port-Channel3 = 'up' | NOT RUN | - |
| 1973 | dc2-leaf2b | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel5 - SERVER_dc2-leaf2-server1_PortChannel dc2-leaf2-server1 = 'up' | NOT RUN | - |
| 1974 | dc2-leaf2b | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel8 - DC2-LEAF2C_Po1 = 'up' | NOT RUN | - |
| 1975 | dc2-leaf2b | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan11 - VRF10_VLAN11 = 'up' | NOT RUN | - |
| 1976 | dc2-leaf2b | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan12 - VRF10_VLAN12 = 'up' | NOT RUN | - |
| 1977 | dc2-leaf2b | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan21 - VRF11_VLAN21 = 'up' | NOT RUN | - |
| 1978 | dc2-leaf2b | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan22 - VRF11_VLAN22 = 'up' | NOT RUN | - |
| 1979 | dc2-leaf2b | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan3009 - MLAG_L3_VRF_VRF10 = 'up' | NOT RUN | - |
| 1980 | dc2-leaf2b | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan3010 - MLAG_L3_VRF_VRF11 = 'up' | NOT RUN | - |
| 1981 | dc2-leaf2b | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan4093 - MLAG_L3 = 'up' | NOT RUN | - |
| 1982 | dc2-leaf2b | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan4094 - MLAG = 'up' | NOT RUN | - |
| 1983 | dc2-leaf2b | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vxlan1 = 'up' | NOT RUN | - |
| 1984 | dc2-leaf2b | LANZ | VerifyLANZ | Verifies if LANZ is enabled. | - | NOT RUN | - |
| 1985 | dc2-leaf2b | Logging | VerifyLoggingAccounting | Verifies if AAA accounting logs are generated. | - | NOT RUN | - |
| 1986 | dc2-leaf2b | Logging | VerifyLoggingErrors | Verifies there are no syslog messages with a severity of ERRORS or higher. | - | NOT RUN | - |
| 1987 | dc2-leaf2b | Logging | VerifyLoggingHostname | Verifies if logs are generated with the device FQDN. | - | NOT RUN | - |
| 1988 | dc2-leaf2b | Logging | VerifyLoggingHosts | Verifies logging hosts (syslog servers) for a specified VRF. | - | NOT RUN | - |
| 1989 | dc2-leaf2b | Logging | VerifyLoggingLogsGeneration | Verifies if logs are generated. | - | NOT RUN | - |
| 1990 | dc2-leaf2b | Logging | VerifyLoggingPersistent | Verifies if logging persistent is enabled and logs are saved in flash. | - | NOT RUN | - |
| 1991 | dc2-leaf2b | Logging | VerifyLoggingSourceInt | Verifies logging source-interface for a specified VRF. | - | NOT RUN | - |
| 1992 | dc2-leaf2b | Logging | VerifyLoggingTimestamp | Verifies if logs are generated with the riate timestamp. | - | NOT RUN | - |
| 1993 | dc2-leaf2b | MLAG | VerifyMlagConfigSanity | Verifies there are no MLAG config-sanity inconsistencies. | - | NOT RUN | - |
| 1994 | dc2-leaf2b | MLAG | VerifyMlagDualPrimary | Verifies the MLAG dual-primary detection parameters. | - | NOT RUN | - |
| 1995 | dc2-leaf2b | MLAG | VerifyMlagInterfaces | Verifies there are no inactive or active-partial MLAG ports. | - | NOT RUN | - |
| 1996 | dc2-leaf2b | MLAG | VerifyMlagReloadDelay | Verifies the MLAG reload-delay parameters. | - | NOT RUN | - |
| 1997 | dc2-leaf2b | MLAG | VerifyMlagStatus | Verifies the health status of the MLAG configuration. | - | NOT RUN | - |
| 1998 | dc2-leaf2b | MLAG | VerifyMlagStatus | Verifies the health status of the MLAG configuration. | - | NOT RUN | - |
| 1999 | dc2-leaf2b | Multicast | VerifyIGMPSnoopingGlobal | Verifies the IGMP snooping global configuration. | - | NOT RUN | - |
| 2000 | dc2-leaf2b | Multicast | VerifyIGMPSnoopingVlans | Verifies the IGMP snooping status for the provided VLANs. | - | NOT RUN | - |
| 2001 | dc2-leaf2b | PTP | VerifyPtpGMStatus | Verifies that the device is locked to a valid PTP Grandmaster. | - | NOT RUN | - |
| 2002 | dc2-leaf2b | PTP | VerifyPtpLockStatus | Verifies that the device was locked to the upstream PTP GM in the last minute. | - | NOT RUN | - |
| 2003 | dc2-leaf2b | PTP | VerifyPtpModeStatus | Verifies that the device is configured as a PTP Boundary Clock. | - | NOT RUN | - |
| 2004 | dc2-leaf2b | PTP | VerifyPtpOffset | Verifies that the PTP timing offset is within +/- 1000ns from the master clock. | - | NOT RUN | - |
| 2005 | dc2-leaf2b | PTP | VerifyPtpPortModeStatus | Verifies the PTP interfaces state. | - | NOT RUN | - |
| 2006 | dc2-leaf2b | Routing | VerifyRoutingProtocolModel | Verifies the configured routing protocol model. | Routing protocol model: multi-agent | NOT RUN | - |
| 2007 | dc2-leaf2b | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.0.1 - Peer: dc1-spine1 | NOT RUN | - |
| 2008 | dc2-leaf2b | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.0.2 - Peer: dc1-spine2 | NOT RUN | - |
| 2009 | dc2-leaf2b | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.0.3 - Peer: dc1-leaf1a | NOT RUN | - |
| 2010 | dc2-leaf2b | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.0.4 - Peer: dc1-leaf1b | NOT RUN | - |
| 2011 | dc2-leaf2b | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.0.5 - Peer: dc1-leaf2a | NOT RUN | - |
| 2012 | dc2-leaf2b | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.1.3 - Peer: dc1-leaf1a | NOT RUN | - |
| 2013 | dc2-leaf2b | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.1.5 - Peer: dc1-leaf2a | NOT RUN | - |
| 2014 | dc2-leaf2b | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.128.11 - Peer: dc2-spine1 | NOT RUN | - |
| 2015 | dc2-leaf2b | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.128.12 - Peer: dc2-spine2 | NOT RUN | - |
| 2016 | dc2-leaf2b | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.128.13 - Peer: dc2-leaf1a | NOT RUN | - |
| 2017 | dc2-leaf2b | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.128.14 - Peer: dc2-leaf1b | NOT RUN | - |
| 2018 | dc2-leaf2b | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.128.15 - Peer: dc2-leaf2a | NOT RUN | - |
| 2019 | dc2-leaf2b | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.128.16 - Peer: dc2-leaf2b | NOT RUN | - |
| 2020 | dc2-leaf2b | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.128.17 - Peer: dc2-leaf3a.arista.com | NOT RUN | - |
| 2021 | dc2-leaf2b | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.128.18 - Peer: dc2-leaf3b.arista.com | NOT RUN | - |
| 2022 | dc2-leaf2b | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.129.13 - Peer: dc2-leaf1a | NOT RUN | - |
| 2023 | dc2-leaf2b | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.129.15 - Peer: dc2-leaf2a | NOT RUN | - |
| 2024 | dc2-leaf2b | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.129.17 - Peer: dc2-leaf3a.arista.com | NOT RUN | - |
| 2025 | dc2-leaf2b | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.2.1 - Peer: dc1-wan1 | NOT RUN | - |
| 2026 | dc2-leaf2b | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.2.2 - Peer: dc1-wan2 | NOT RUN | - |
| 2027 | dc2-leaf2b | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.33.0.5 - Peer: dc1-svc-leaf1a | NOT RUN | - |
| 2028 | dc2-leaf2b | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.33.0.6 - Peer: dc1-svc-leaf1b | NOT RUN | - |
| 2029 | dc2-leaf2b | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.33.1.5 - Peer: dc1-svc-leaf1a | NOT RUN | - |
| 2030 | dc2-leaf2b | Security | VerifyAPIHttpsSSL | Verifies if the eAPI has a valid SSL profile. | - | NOT RUN | - |
| 2031 | dc2-leaf2b | Security | VerifyAPIHttpsSSL | Verifies if the eAPI has a valid SSL profile. | eAPI HTTPS SSL Profile: eAPI_SSL_Profile | NOT RUN | - |
| 2032 | dc2-leaf2b | Security | VerifyAPIHttpStatus | Verifies if eAPI HTTP server is disabled globally. | - | NOT RUN | - |
| 2033 | dc2-leaf2b | Security | VerifyAPIIPv4Acl | Verifies if eAPI has the right number IPv4 ACL(s) configured for a specified VRF. | - | NOT RUN | - |
| 2034 | dc2-leaf2b | Security | VerifyAPIIPv6Acl | Verifies if eAPI has the right number IPv6 ACL(s) configured for a specified VRF. | - | NOT RUN | - |
| 2035 | dc2-leaf2b | Security | VerifyAPISSLCertificate | Verifies the eAPI SSL certificate expiry, common subject name, encryption algorithm and key size. | - | NOT RUN | - |
| 2036 | dc2-leaf2b | Security | VerifyBannerLogin | Verifies the login banner of a device. | - | NOT RUN | - |
| 2037 | dc2-leaf2b | Security | VerifyBannerMotd | Verifies the motd banner of a device. | - | NOT RUN | - |
| 2038 | dc2-leaf2b | Security | VerifyIPSecConnHealth | Verifies all IPv4 security connections. | - | NOT RUN | - |
| 2039 | dc2-leaf2b | Security | VerifyIPv4ACL | Verifies the configuration of IPv4 ACLs. | - | NOT RUN | - |
| 2040 | dc2-leaf2b | Security | VerifySpecificIPSecConn | Verifies IPv4 security connections for a peer. | - | NOT RUN | - |
| 2041 | dc2-leaf2b | Security | VerifySSHIPv4Acl | Verifies if the SSHD agent has IPv4 ACL(s) configured. | - | NOT RUN | - |
| 2042 | dc2-leaf2b | Security | VerifySSHIPv6Acl | Verifies if the SSHD agent has IPv6 ACL(s) configured. | - | NOT RUN | - |
| 2043 | dc2-leaf2b | Security | VerifySSHStatus | Verifies if the SSHD agent is disabled in the default VRF. | - | NOT RUN | - |
| 2044 | dc2-leaf2b | Security | VerifyTelnetStatus | Verifies if Telnet is disabled in the default VRF. | - | NOT RUN | - |
| 2045 | dc2-leaf2b | Services | VerifyDNSLookup | Verifies the DNS name to IP address resolution. | - | NOT RUN | - |
| 2046 | dc2-leaf2b | Services | VerifyDNSServers | Verifies if the DNS servers are correctly configured. | - | NOT RUN | - |
| 2047 | dc2-leaf2b | Services | VerifyErrdisableRecovery | Verifies the errdisable recovery reason, status, and interval. | - | NOT RUN | - |
| 2048 | dc2-leaf2b | Services | VerifyHostname | Verifies the hostname of a device. | - | NOT RUN | - |
| 2049 | dc2-leaf2b | SNMP | VerifySnmpIPv4Acl | Verifies if the SNMP agent has IPv4 ACL(s) configured. | - | NOT RUN | - |
| 2050 | dc2-leaf2b | SNMP | VerifySnmpIPv6Acl | Verifies if the SNMP agent has IPv6 ACL(s) configured. | - | NOT RUN | - |
| 2051 | dc2-leaf2b | SNMP | VerifySnmpStatus | Verifies if the SNMP agent is enabled. | - | NOT RUN | - |
| 2052 | dc2-leaf2b | Software | VerifyEOSVersion | Verifies the EOS version of the device. | - | NOT RUN | - |
| 2053 | dc2-leaf2b | Software | VerifyTerminAttrVersion | Verifies the TerminAttr version of the device. | - | NOT RUN | - |
| 2054 | dc2-leaf2b | STP | VerifySTPBlockedPorts | Verifies there is no STP blocked ports. | - | NOT RUN | - |
| 2055 | dc2-leaf2b | STP | VerifySTPCounters | Verifies there is no errors in STP BPDU packets. | - | NOT RUN | - |
| 2056 | dc2-leaf2b | STP | VerifySTPForwardingPorts | Verifies that all interfaces are forwarding for a provided list of VLAN(s). | - | NOT RUN | - |
| 2057 | dc2-leaf2b | STP | VerifySTPMode | Verifies the configured STP mode for a provided list of VLAN(s). | - | NOT RUN | - |
| 2058 | dc2-leaf2b | STP | VerifySTPRootPriority | Verifies the STP root priority for a provided list of VLAN or MST instance ID(s). | - | NOT RUN | - |
| 2059 | dc2-leaf2b | STUN | VerifyStunClient | Verifies the STUN client is configured with the specified IPv4 source address and port. Validate the public IP and port if provided. | - | NOT RUN | - |
| 2060 | dc2-leaf2b | System | VerifyAgentLogs | Verifies there are no agent crash reports. | - | NOT RUN | - |
| 2061 | dc2-leaf2b | System | VerifyCoredump | Verifies there are no core dump files. | - | NOT RUN | - |
| 2062 | dc2-leaf2b | System | VerifyCPUUtilization | Verifies whether the CPU utilization is below 75%. | - | NOT RUN | - |
| 2063 | dc2-leaf2b | System | VerifyFileSystemUtilization | Verifies that no partition is utilizing more than 75% of its disk space. | - | NOT RUN | - |
| 2064 | dc2-leaf2b | System | VerifyMemoryUtilization | Verifies whether the memory utilization is below 75%. | - | NOT RUN | - |
| 2065 | dc2-leaf2b | System | VerifyNTP | Verifies if NTP is synchronised. | - | NOT RUN | - |
| 2066 | dc2-leaf2b | System | VerifyNTP | Verifies if NTP is synchronised. | - | NOT RUN | - |
| 2067 | dc2-leaf2b | System | VerifyReloadCause | Verifies the last reload cause of the device. | - | NOT RUN | - |
| 2068 | dc2-leaf2b | System | VerifyReloadCause | Verifies the last reload cause of the device. | - | NOT RUN | - |
| 2069 | dc2-leaf2b | System | VerifyUptime | Verifies the device uptime. | - | NOT RUN | - |
| 2070 | dc2-leaf2b | VLAN | VerifyVlanInternalPolicy | Verifies the VLAN internal allocation policy and the range of VLANs. | - | NOT RUN | - |
| 2071 | dc2-leaf2c | AAA | VerifyAcctConsoleMethods | Verifies the AAA accounting console method lists for different accounting types (system, exec, commands, dot1x). | - | NOT RUN | - |
| 2072 | dc2-leaf2c | AAA | VerifyAcctDefaultMethods | Verifies the AAA accounting default method lists for different accounting types (system, exec, commands, dot1x). | - | NOT RUN | - |
| 2073 | dc2-leaf2c | AAA | VerifyAuthenMethods | Verifies the AAA authentication method lists for different authentication types (login, enable, dot1x). | - | NOT RUN | - |
| 2074 | dc2-leaf2c | AAA | VerifyAuthzMethods | Verifies the AAA authorization method lists for different authorization types (commands, exec). | - | NOT RUN | - |
| 2075 | dc2-leaf2c | AAA | VerifyTacacsServerGroups | Verifies if the provided TACACS server group(s) are configured. | - | NOT RUN | - |
| 2076 | dc2-leaf2c | AAA | VerifyTacacsServers | Verifies TACACS servers are configured for a specified VRF. | - | NOT RUN | - |
| 2077 | dc2-leaf2c | AAA | VerifyTacacsSourceIntf | Verifies TACACS source-interface for a specified VRF. | - | NOT RUN | - |
| 2078 | dc2-leaf2c | Configuration | VerifyRunningConfigDiffs | Verifies there is no difference between the running-config and the startup-config | - | NOT RUN | - |
| 2079 | dc2-leaf2c | Configuration | VerifyZeroTouch | Verifies ZeroTouch is disabled | - | NOT RUN | - |
| 2080 | dc2-leaf2c | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet1 - Remote: dc2-leaf2a Ethernet8 | NOT RUN | - |
| 2081 | dc2-leaf2c | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet2 - Remote: dc2-leaf2b Ethernet8 | NOT RUN | - |
| 2082 | dc2-leaf2c | Field Notices | VerifyFieldNotice44Resolution | Verifies that the device is using the correct Aboot version per FN0044. | - | NOT RUN | - |
| 2083 | dc2-leaf2c | Field Notices | VerifyFieldNotice72Resolution | Verifies if the device is exposed to FN0072, and if the issue has been mitigated. | - | NOT RUN | - |
| 2084 | dc2-leaf2c | Greent | VerifyGreenT | Verifies if a GreenT policy is created. | - | NOT RUN | - |
| 2085 | dc2-leaf2c | Greent | VerifyGreenTCounters | Verifies if the GreenT counters are incremented. | - | NOT RUN | - |
| 2086 | dc2-leaf2c | Hardware | VerifyAdverseDrops | Verifies there are no adverse drops on DCS-7280 and DCS-7500 family switches. | - | NOT RUN | - |
| 2087 | dc2-leaf2c | Hardware | VerifyEnvironmentCooling | Verifies the status of power supply fans and all fan trays. | - | NOT RUN | - |
| 2088 | dc2-leaf2c | Hardware | VerifyEnvironmentCooling | Verifies the status of power supply fans and all fan trays. | Accepted States: 'ok' | NOT RUN | - |
| 2089 | dc2-leaf2c | Hardware | VerifyEnvironmentPower | Verifies the power supplies status. | - | NOT RUN | - |
| 2090 | dc2-leaf2c | Hardware | VerifyEnvironmentPower | Verifies the power supplies status. | Accepted States: 'ok' | NOT RUN | - |
| 2091 | dc2-leaf2c | Hardware | VerifyEnvironmentSystemCooling | Verifies the system cooling status. | - | NOT RUN | - |
| 2092 | dc2-leaf2c | Hardware | VerifyTemperature | Verifies the device temperature. | - | NOT RUN | - |
| 2093 | dc2-leaf2c | Hardware | VerifyTemperature | Verifies the device temperature. | - | NOT RUN | - |
| 2094 | dc2-leaf2c | Hardware | VerifyTransceiversManufacturers | Verifies if all transceivers come from approved manufacturers. | - | NOT RUN | - |
| 2095 | dc2-leaf2c | Hardware | VerifyTransceiversManufacturers | Verifies if all transceivers come from approved manufacturers. | Accepted Manufacturers: 'Arista Networks', 'Arastra, Inc.', 'Not Present' | NOT RUN | - |
| 2096 | dc2-leaf2c | Hardware | VerifyTransceiversTemperature | Verifies the transceivers temperature. | - | NOT RUN | - |
| 2097 | dc2-leaf2c | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet1 - DC2-LEAF2A_Ethernet8 = 'up' | NOT RUN | - |
| 2098 | dc2-leaf2c | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet2 - DC2-LEAF2B_Ethernet8 = 'up' | NOT RUN | - |
| 2099 | dc2-leaf2c | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet5 - SERVER_dc2-leaf2-server1_iLO = 'up' | NOT RUN | - |
| 2100 | dc2-leaf2c | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel1 - DC2_L3_LEAF2_Po8 = 'up' | NOT RUN | - |
| 2101 | dc2-leaf2c | LANZ | VerifyLANZ | Verifies if LANZ is enabled. | - | NOT RUN | - |
| 2102 | dc2-leaf2c | PTP | VerifyPtpGMStatus | Verifies that the device is locked to a valid PTP Grandmaster. | - | NOT RUN | - |
| 2103 | dc2-leaf2c | PTP | VerifyPtpLockStatus | Verifies that the device was locked to the upstream PTP GM in the last minute. | - | NOT RUN | - |
| 2104 | dc2-leaf2c | PTP | VerifyPtpModeStatus | Verifies that the device is configured as a PTP Boundary Clock. | - | NOT RUN | - |
| 2105 | dc2-leaf2c | PTP | VerifyPtpOffset | Verifies that the PTP timing offset is within +/- 1000ns from the master clock. | - | NOT RUN | - |
| 2106 | dc2-leaf2c | PTP | VerifyPtpPortModeStatus | Verifies the PTP interfaces state. | - | NOT RUN | - |
| 2107 | dc2-leaf2c | Security | VerifyAPIHttpsSSL | Verifies if the eAPI has a valid SSL profile. | - | NOT RUN | - |
| 2108 | dc2-leaf2c | Security | VerifyAPIHttpsSSL | Verifies if the eAPI has a valid SSL profile. | eAPI HTTPS SSL Profile: eAPI_SSL_Profile | NOT RUN | - |
| 2109 | dc2-leaf2c | Security | VerifyAPIHttpStatus | Verifies if eAPI HTTP server is disabled globally. | - | NOT RUN | - |
| 2110 | dc2-leaf2c | Security | VerifyAPIIPv4Acl | Verifies if eAPI has the right number IPv4 ACL(s) configured for a specified VRF. | - | NOT RUN | - |
| 2111 | dc2-leaf2c | Security | VerifyAPIIPv6Acl | Verifies if eAPI has the right number IPv6 ACL(s) configured for a specified VRF. | - | NOT RUN | - |
| 2112 | dc2-leaf2c | Security | VerifyAPISSLCertificate | Verifies the eAPI SSL certificate expiry, common subject name, encryption algorithm and key size. | - | NOT RUN | - |
| 2113 | dc2-leaf2c | Security | VerifyBannerLogin | Verifies the login banner of a device. | - | NOT RUN | - |
| 2114 | dc2-leaf2c | Security | VerifyBannerMotd | Verifies the motd banner of a device. | - | NOT RUN | - |
| 2115 | dc2-leaf2c | Security | VerifyIPSecConnHealth | Verifies all IPv4 security connections. | - | NOT RUN | - |
| 2116 | dc2-leaf2c | Security | VerifyIPv4ACL | Verifies the configuration of IPv4 ACLs. | - | NOT RUN | - |
| 2117 | dc2-leaf2c | Security | VerifySpecificIPSecConn | Verifies IPv4 security connections for a peer. | - | NOT RUN | - |
| 2118 | dc2-leaf2c | Security | VerifySSHIPv4Acl | Verifies if the SSHD agent has IPv4 ACL(s) configured. | - | NOT RUN | - |
| 2119 | dc2-leaf2c | Security | VerifySSHIPv6Acl | Verifies if the SSHD agent has IPv6 ACL(s) configured. | - | NOT RUN | - |
| 2120 | dc2-leaf2c | Security | VerifySSHStatus | Verifies if the SSHD agent is disabled in the default VRF. | - | NOT RUN | - |
| 2121 | dc2-leaf2c | Security | VerifyTelnetStatus | Verifies if Telnet is disabled in the default VRF. | - | NOT RUN | - |
| 2122 | dc2-leaf2c | Services | VerifyDNSLookup | Verifies the DNS name to IP address resolution. | - | NOT RUN | - |
| 2123 | dc2-leaf2c | Services | VerifyDNSServers | Verifies if the DNS servers are correctly configured. | - | NOT RUN | - |
| 2124 | dc2-leaf2c | Services | VerifyErrdisableRecovery | Verifies the errdisable recovery reason, status, and interval. | - | NOT RUN | - |
| 2125 | dc2-leaf2c | Services | VerifyHostname | Verifies the hostname of a device. | - | NOT RUN | - |
| 2126 | dc2-leaf2c | SNMP | VerifySnmpIPv4Acl | Verifies if the SNMP agent has IPv4 ACL(s) configured. | - | NOT RUN | - |
| 2127 | dc2-leaf2c | SNMP | VerifySnmpIPv6Acl | Verifies if the SNMP agent has IPv6 ACL(s) configured. | - | NOT RUN | - |
| 2128 | dc2-leaf2c | SNMP | VerifySnmpStatus | Verifies if the SNMP agent is enabled. | - | NOT RUN | - |
| 2129 | dc2-leaf2c | Software | VerifyEOSVersion | Verifies the EOS version of the device. | - | NOT RUN | - |
| 2130 | dc2-leaf2c | Software | VerifyTerminAttrVersion | Verifies the TerminAttr version of the device. | - | NOT RUN | - |
| 2131 | dc2-leaf2c | STUN | VerifyStunClient | Verifies the STUN client is configured with the specified IPv4 source address and port. Validate the public IP and port if provided. | - | NOT RUN | - |
| 2132 | dc2-leaf2c | System | VerifyAgentLogs | Verifies there are no agent crash reports. | - | NOT RUN | - |
| 2133 | dc2-leaf2c | System | VerifyCoredump | Verifies there are no core dump files. | - | NOT RUN | - |
| 2134 | dc2-leaf2c | System | VerifyCPUUtilization | Verifies whether the CPU utilization is below 75%. | - | NOT RUN | - |
| 2135 | dc2-leaf2c | System | VerifyFileSystemUtilization | Verifies that no partition is utilizing more than 75% of its disk space. | - | NOT RUN | - |
| 2136 | dc2-leaf2c | System | VerifyMemoryUtilization | Verifies whether the memory utilization is below 75%. | - | NOT RUN | - |
| 2137 | dc2-leaf2c | System | VerifyNTP | Verifies if NTP is synchronised. | - | NOT RUN | - |
| 2138 | dc2-leaf2c | System | VerifyNTP | Verifies if NTP is synchronised. | - | NOT RUN | - |
| 2139 | dc2-leaf2c | System | VerifyReloadCause | Verifies the last reload cause of the device. | - | NOT RUN | - |
| 2140 | dc2-leaf2c | System | VerifyReloadCause | Verifies the last reload cause of the device. | - | NOT RUN | - |
| 2141 | dc2-leaf2c | System | VerifyUptime | Verifies the device uptime. | - | NOT RUN | - |
| 2142 | dc2-leaf2c | VLAN | VerifyVlanInternalPolicy | Verifies the VLAN internal allocation policy and the range of VLANs. | - | NOT RUN | - |
| 2143 | dc2-leaf3a.arista.com | AAA | VerifyAcctConsoleMethods | Verifies the AAA accounting console method lists for different accounting types (system, exec, commands, dot1x). | - | NOT RUN | - |
| 2144 | dc2-leaf3a.arista.com | AAA | VerifyAcctDefaultMethods | Verifies the AAA accounting default method lists for different accounting types (system, exec, commands, dot1x). | - | NOT RUN | - |
| 2145 | dc2-leaf3a.arista.com | AAA | VerifyAuthenMethods | Verifies the AAA authentication method lists for different authentication types (login, enable, dot1x). | - | NOT RUN | - |
| 2146 | dc2-leaf3a.arista.com | AAA | VerifyAuthzMethods | Verifies the AAA authorization method lists for different authorization types (commands, exec). | - | NOT RUN | - |
| 2147 | dc2-leaf3a.arista.com | AAA | VerifyTacacsServerGroups | Verifies if the provided TACACS server group(s) are configured. | - | NOT RUN | - |
| 2148 | dc2-leaf3a.arista.com | AAA | VerifyTacacsServers | Verifies TACACS servers are configured for a specified VRF. | - | NOT RUN | - |
| 2149 | dc2-leaf3a.arista.com | AAA | VerifyTacacsSourceIntf | Verifies TACACS source-interface for a specified VRF. | - | NOT RUN | - |
| 2150 | dc2-leaf3a.arista.com | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: dc2-spine1 (IP: 10.255.128.11) | NOT RUN | - |
| 2151 | dc2-leaf3a.arista.com | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: dc2-spine2 (IP: 10.255.128.12) | NOT RUN | - |
| 2152 | dc2-leaf3a.arista.com | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: dc2-leaf3b.arista.com (IP: 10.255.129.125) | NOT RUN | - |
| 2153 | dc2-leaf3a.arista.com | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: dc2-spine1 (IP: 10.255.255.120) | NOT RUN | - |
| 2154 | dc2-leaf3a.arista.com | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: dc2-spine2 (IP: 10.255.255.122) | NOT RUN | - |
| 2155 | dc2-leaf3a.arista.com | Configuration | VerifyRunningConfigDiffs | Verifies there is no difference between the running-config and the startup-config | - | NOT RUN | - |
| 2156 | dc2-leaf3a.arista.com | Configuration | VerifyZeroTouch | Verifies ZeroTouch is disabled | - | NOT RUN | - |
| 2157 | dc2-leaf3a.arista.com | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet1 - Remote: dc2-spine1 Ethernet5 | NOT RUN | - |
| 2158 | dc2-leaf3a.arista.com | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet15 - Remote: dc2-leaf2b Ethernet2 | NOT RUN | - |
| 2159 | dc2-leaf3a.arista.com | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet2 - Remote: dc2-spine2 Ethernet5 | NOT RUN | - |
| 2160 | dc2-leaf3a.arista.com | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet3 - Remote: dc2-leaf3b.arista.com Ethernet3 | NOT RUN | - |
| 2161 | dc2-leaf3a.arista.com | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet4 - Remote: dc2-leaf3b.arista.com Ethernet4 | NOT RUN | - |
| 2162 | dc2-leaf3a.arista.com | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.128.17) - Destination: dc1-leaf1a Loopback0 (IP: 10.255.0.3) | NOT RUN | - |
| 2163 | dc2-leaf3a.arista.com | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.128.17) - Destination: dc1-leaf1b Loopback0 (IP: 10.255.0.4) | NOT RUN | - |
| 2164 | dc2-leaf3a.arista.com | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.128.17) - Destination: dc1-leaf2a Loopback0 (IP: 10.255.0.5) | NOT RUN | - |
| 2165 | dc2-leaf3a.arista.com | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.128.17) - Destination: dc1-spine1 Loopback0 (IP: 10.255.0.1) | NOT RUN | - |
| 2166 | dc2-leaf3a.arista.com | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.128.17) - Destination: dc1-spine2 Loopback0 (IP: 10.255.0.2) | NOT RUN | - |
| 2167 | dc2-leaf3a.arista.com | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.128.17) - Destination: dc1-svc-leaf1a Loopback0 (IP: 10.33.0.5) | NOT RUN | - |
| 2168 | dc2-leaf3a.arista.com | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.128.17) - Destination: dc1-svc-leaf1b Loopback0 (IP: 10.33.0.6) | NOT RUN | - |
| 2169 | dc2-leaf3a.arista.com | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.128.17) - Destination: dc1-wan1 Loopback0 (IP: 10.255.2.1) | NOT RUN | - |
| 2170 | dc2-leaf3a.arista.com | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.128.17) - Destination: dc1-wan2 Loopback0 (IP: 10.255.2.2) | NOT RUN | - |
| 2171 | dc2-leaf3a.arista.com | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.128.17) - Destination: dc2-leaf1a Loopback0 (IP: 10.255.128.13) | NOT RUN | - |
| 2172 | dc2-leaf3a.arista.com | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.128.17) - Destination: dc2-leaf1b Loopback0 (IP: 10.255.128.14) | NOT RUN | - |
| 2173 | dc2-leaf3a.arista.com | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.128.17) - Destination: dc2-leaf2a Loopback0 (IP: 10.255.128.15) | NOT RUN | - |
| 2174 | dc2-leaf3a.arista.com | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.128.17) - Destination: dc2-leaf2b Loopback0 (IP: 10.255.128.16) | NOT RUN | - |
| 2175 | dc2-leaf3a.arista.com | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.128.17) - Destination: dc2-leaf3a.arista.com Loopback0 (IP: 10.255.128.17) | NOT RUN | - |
| 2176 | dc2-leaf3a.arista.com | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.128.17) - Destination: dc2-leaf3b.arista.com Loopback0 (IP: 10.255.128.18) | NOT RUN | - |
| 2177 | dc2-leaf3a.arista.com | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.128.17) - Destination: dc2-spine1 Loopback0 (IP: 10.255.128.11) | NOT RUN | - |
| 2178 | dc2-leaf3a.arista.com | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.128.17) - Destination: dc2-spine2 Loopback0 (IP: 10.255.128.12) | NOT RUN | - |
| 2179 | dc2-leaf3a.arista.com | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet1 (IP: 10.255.255.121) - Destination: dc2-spine1 Ethernet5 (IP: 10.255.255.120) | NOT RUN | - |
| 2180 | dc2-leaf3a.arista.com | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet15 (IP: 1.1.1.1) - Destination: dc2-leaf2b Ethernet2 (IP: 10.255.255.119) | NOT RUN | - |
| 2181 | dc2-leaf3a.arista.com | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet2 (IP: 10.255.255.123) - Destination: dc2-spine2 Ethernet5 (IP: 10.255.255.122) | NOT RUN | - |
| 2182 | dc2-leaf3a.arista.com | Field Notices | VerifyFieldNotice44Resolution | Verifies that the device is using the correct Aboot version per FN0044. | - | NOT RUN | - |
| 2183 | dc2-leaf3a.arista.com | Field Notices | VerifyFieldNotice72Resolution | Verifies if the device is exposed to FN0072, and if the issue has been mitigated. | - | NOT RUN | - |
| 2184 | dc2-leaf3a.arista.com | Greent | VerifyGreenT | Verifies if a GreenT policy is created. | - | NOT RUN | - |
| 2185 | dc2-leaf3a.arista.com | Greent | VerifyGreenTCounters | Verifies if the GreenT counters are incremented. | - | NOT RUN | - |
| 2186 | dc2-leaf3a.arista.com | Hardware | VerifyAdverseDrops | Verifies there are no adverse drops on DCS-7280 and DCS-7500 family switches. | - | NOT RUN | - |
| 2187 | dc2-leaf3a.arista.com | Hardware | VerifyEnvironmentCooling | Verifies the status of power supply fans and all fan trays. | - | NOT RUN | - |
| 2188 | dc2-leaf3a.arista.com | Hardware | VerifyEnvironmentCooling | Verifies the status of power supply fans and all fan trays. | Accepted States: 'ok' | NOT RUN | - |
| 2189 | dc2-leaf3a.arista.com | Hardware | VerifyEnvironmentPower | Verifies the power supplies status. | - | NOT RUN | - |
| 2190 | dc2-leaf3a.arista.com | Hardware | VerifyEnvironmentPower | Verifies the power supplies status. | Accepted States: 'ok' | NOT RUN | - |
| 2191 | dc2-leaf3a.arista.com | Hardware | VerifyEnvironmentSystemCooling | Verifies the system cooling status. | - | NOT RUN | - |
| 2192 | dc2-leaf3a.arista.com | Hardware | VerifyTemperature | Verifies the device temperature. | - | NOT RUN | - |
| 2193 | dc2-leaf3a.arista.com | Hardware | VerifyTemperature | Verifies the device temperature. | - | NOT RUN | - |
| 2194 | dc2-leaf3a.arista.com | Hardware | VerifyTransceiversManufacturers | Verifies if all transceivers come from approved manufacturers. | - | NOT RUN | - |
| 2195 | dc2-leaf3a.arista.com | Hardware | VerifyTransceiversManufacturers | Verifies if all transceivers come from approved manufacturers. | Accepted Manufacturers: 'Arista Networks', 'Arastra, Inc.', 'Not Present' | NOT RUN | - |
| 2196 | dc2-leaf3a.arista.com | Hardware | VerifyTransceiversTemperature | Verifies the transceivers temperature. | - | NOT RUN | - |
| 2197 | dc2-leaf3a.arista.com | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet1 - P2P_LINK_TO_DC2-SPINE1_Ethernet5 = 'up' | NOT RUN | - |
| 2198 | dc2-leaf3a.arista.com | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet11 - dc2-leaf3-fw1_e1 = 'up' | NOT RUN | - |
| 2199 | dc2-leaf3a.arista.com | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet12 - Test_mode_and_vlans = 'up' | NOT RUN | - |
| 2200 | dc2-leaf3a.arista.com | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet13 - Test_native_vlan_and_trunk_groups = 'up' | NOT RUN | - |
| 2201 | dc2-leaf3a.arista.com | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet14 - Test_phone = 'up' | NOT RUN | - |
| 2202 | dc2-leaf3a.arista.com | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet15 - Test_type_routed = 'up' | NOT RUN | - |
| 2203 | dc2-leaf3a.arista.com | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet2 - P2P_LINK_TO_DC2-SPINE2_Ethernet5 = 'up' | NOT RUN | - |
| 2204 | dc2-leaf3a.arista.com | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet3 - MLAG_dc2-leaf3b.arista.com_Ethernet3 = 'up' | NOT RUN | - |
| 2205 | dc2-leaf3a.arista.com | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet4 - MLAG_dc2-leaf3b.arista.com_Ethernet4 = 'up' | NOT RUN | - |
| 2206 | dc2-leaf3a.arista.com | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback0 - ROUTER_ID = 'up' | NOT RUN | - |
| 2207 | dc2-leaf3a.arista.com | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback1 - VXLAN_TUNNEL_SOURCE = 'up' | NOT RUN | - |
| 2208 | dc2-leaf3a.arista.com | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback10 - VRF10_VTEP_DIAGNOSTICS = 'up' | NOT RUN | - |
| 2209 | dc2-leaf3a.arista.com | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback11 - VRF11_VTEP_DIAGNOSTICS = 'up' | NOT RUN | - |
| 2210 | dc2-leaf3a.arista.com | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel11 - dc2-leaf3-fw1_PortChannel = 'up' | NOT RUN | - |
| 2211 | dc2-leaf3a.arista.com | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel12 - Test_mode_and_vlans = 'up' | NOT RUN | - |
| 2212 | dc2-leaf3a.arista.com | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel13 - Test_native_vlan_and_trunk_groups = 'up' | NOT RUN | - |
| 2213 | dc2-leaf3a.arista.com | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel14 - Test_phone = 'up' | NOT RUN | - |
| 2214 | dc2-leaf3a.arista.com | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel15 - Test_type_routed = 'up' | NOT RUN | - |
| 2215 | dc2-leaf3a.arista.com | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel3 - MLAG_dc2-leaf3b.arista.com_Port-Channel3 = 'up' | NOT RUN | - |
| 2216 | dc2-leaf3a.arista.com | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan11 - VRF10_VLAN11 = 'up' | NOT RUN | - |
| 2217 | dc2-leaf3a.arista.com | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan12 - VRF10_VLAN12 = 'up' | NOT RUN | - |
| 2218 | dc2-leaf3a.arista.com | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan21 - VRF11_VLAN21 = 'up' | NOT RUN | - |
| 2219 | dc2-leaf3a.arista.com | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan22 - VRF11_VLAN22 = 'up' | NOT RUN | - |
| 2220 | dc2-leaf3a.arista.com | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan3009 - MLAG_L3_VRF_VRF10 = 'up' | NOT RUN | - |
| 2221 | dc2-leaf3a.arista.com | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan3010 - MLAG_L3_VRF_VRF11 = 'up' | NOT RUN | - |
| 2222 | dc2-leaf3a.arista.com | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan4093 - MLAG_L3 = 'up' | NOT RUN | - |
| 2223 | dc2-leaf3a.arista.com | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan4094 - MLAG = 'up' | NOT RUN | - |
| 2224 | dc2-leaf3a.arista.com | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vxlan1 = 'up' | NOT RUN | - |
| 2225 | dc2-leaf3a.arista.com | LANZ | VerifyLANZ | Verifies if LANZ is enabled. | - | NOT RUN | - |
| 2226 | dc2-leaf3a.arista.com | Logging | VerifyLoggingAccounting | Verifies if AAA accounting logs are generated. | - | NOT RUN | - |
| 2227 | dc2-leaf3a.arista.com | Logging | VerifyLoggingErrors | Verifies there are no syslog messages with a severity of ERRORS or higher. | - | NOT RUN | - |
| 2228 | dc2-leaf3a.arista.com | Logging | VerifyLoggingHostname | Verifies if logs are generated with the device FQDN. | - | NOT RUN | - |
| 2229 | dc2-leaf3a.arista.com | Logging | VerifyLoggingHosts | Verifies logging hosts (syslog servers) for a specified VRF. | - | NOT RUN | - |
| 2230 | dc2-leaf3a.arista.com | Logging | VerifyLoggingLogsGeneration | Verifies if logs are generated. | - | NOT RUN | - |
| 2231 | dc2-leaf3a.arista.com | Logging | VerifyLoggingPersistent | Verifies if logging persistent is enabled and logs are saved in flash. | - | NOT RUN | - |
| 2232 | dc2-leaf3a.arista.com | Logging | VerifyLoggingSourceInt | Verifies logging source-interface for a specified VRF. | - | NOT RUN | - |
| 2233 | dc2-leaf3a.arista.com | Logging | VerifyLoggingTimestamp | Verifies if logs are generated with the riate timestamp. | - | NOT RUN | - |
| 2234 | dc2-leaf3a.arista.com | MLAG | VerifyMlagConfigSanity | Verifies there are no MLAG config-sanity inconsistencies. | - | NOT RUN | - |
| 2235 | dc2-leaf3a.arista.com | MLAG | VerifyMlagDualPrimary | Verifies the MLAG dual-primary detection parameters. | - | NOT RUN | - |
| 2236 | dc2-leaf3a.arista.com | MLAG | VerifyMlagInterfaces | Verifies there are no inactive or active-partial MLAG ports. | - | NOT RUN | - |
| 2237 | dc2-leaf3a.arista.com | MLAG | VerifyMlagReloadDelay | Verifies the MLAG reload-delay parameters. | - | NOT RUN | - |
| 2238 | dc2-leaf3a.arista.com | MLAG | VerifyMlagStatus | Verifies the health status of the MLAG configuration. | - | NOT RUN | - |
| 2239 | dc2-leaf3a.arista.com | MLAG | VerifyMlagStatus | Verifies the health status of the MLAG configuration. | - | NOT RUN | - |
| 2240 | dc2-leaf3a.arista.com | Multicast | VerifyIGMPSnoopingGlobal | Verifies the IGMP snooping global configuration. | - | NOT RUN | - |
| 2241 | dc2-leaf3a.arista.com | Multicast | VerifyIGMPSnoopingVlans | Verifies the IGMP snooping status for the provided VLANs. | - | NOT RUN | - |
| 2242 | dc2-leaf3a.arista.com | PTP | VerifyPtpGMStatus | Verifies that the device is locked to a valid PTP Grandmaster. | - | NOT RUN | - |
| 2243 | dc2-leaf3a.arista.com | PTP | VerifyPtpLockStatus | Verifies that the device was locked to the upstream PTP GM in the last minute. | - | NOT RUN | - |
| 2244 | dc2-leaf3a.arista.com | PTP | VerifyPtpModeStatus | Verifies that the device is configured as a PTP Boundary Clock. | - | NOT RUN | - |
| 2245 | dc2-leaf3a.arista.com | PTP | VerifyPtpOffset | Verifies that the PTP timing offset is within +/- 1000ns from the master clock. | - | NOT RUN | - |
| 2246 | dc2-leaf3a.arista.com | PTP | VerifyPtpPortModeStatus | Verifies the PTP interfaces state. | - | NOT RUN | - |
| 2247 | dc2-leaf3a.arista.com | Routing | VerifyRoutingProtocolModel | Verifies the configured routing protocol model. | Routing protocol model: multi-agent | NOT RUN | - |
| 2248 | dc2-leaf3a.arista.com | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.0.1 - Peer: dc1-spine1 | NOT RUN | - |
| 2249 | dc2-leaf3a.arista.com | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.0.2 - Peer: dc1-spine2 | NOT RUN | - |
| 2250 | dc2-leaf3a.arista.com | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.0.3 - Peer: dc1-leaf1a | NOT RUN | - |
| 2251 | dc2-leaf3a.arista.com | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.0.4 - Peer: dc1-leaf1b | NOT RUN | - |
| 2252 | dc2-leaf3a.arista.com | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.0.5 - Peer: dc1-leaf2a | NOT RUN | - |
| 2253 | dc2-leaf3a.arista.com | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.1.3 - Peer: dc1-leaf1a | NOT RUN | - |
| 2254 | dc2-leaf3a.arista.com | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.1.5 - Peer: dc1-leaf2a | NOT RUN | - |
| 2255 | dc2-leaf3a.arista.com | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.128.11 - Peer: dc2-spine1 | NOT RUN | - |
| 2256 | dc2-leaf3a.arista.com | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.128.12 - Peer: dc2-spine2 | NOT RUN | - |
| 2257 | dc2-leaf3a.arista.com | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.128.13 - Peer: dc2-leaf1a | NOT RUN | - |
| 2258 | dc2-leaf3a.arista.com | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.128.14 - Peer: dc2-leaf1b | NOT RUN | - |
| 2259 | dc2-leaf3a.arista.com | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.128.15 - Peer: dc2-leaf2a | NOT RUN | - |
| 2260 | dc2-leaf3a.arista.com | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.128.16 - Peer: dc2-leaf2b | NOT RUN | - |
| 2261 | dc2-leaf3a.arista.com | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.128.17 - Peer: dc2-leaf3a.arista.com | NOT RUN | - |
| 2262 | dc2-leaf3a.arista.com | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.128.18 - Peer: dc2-leaf3b.arista.com | NOT RUN | - |
| 2263 | dc2-leaf3a.arista.com | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.129.13 - Peer: dc2-leaf1a | NOT RUN | - |
| 2264 | dc2-leaf3a.arista.com | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.129.15 - Peer: dc2-leaf2a | NOT RUN | - |
| 2265 | dc2-leaf3a.arista.com | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.129.17 - Peer: dc2-leaf3a.arista.com | NOT RUN | - |
| 2266 | dc2-leaf3a.arista.com | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.2.1 - Peer: dc1-wan1 | NOT RUN | - |
| 2267 | dc2-leaf3a.arista.com | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.2.2 - Peer: dc1-wan2 | NOT RUN | - |
| 2268 | dc2-leaf3a.arista.com | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.33.0.5 - Peer: dc1-svc-leaf1a | NOT RUN | - |
| 2269 | dc2-leaf3a.arista.com | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.33.0.6 - Peer: dc1-svc-leaf1b | NOT RUN | - |
| 2270 | dc2-leaf3a.arista.com | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.33.1.5 - Peer: dc1-svc-leaf1a | NOT RUN | - |
| 2271 | dc2-leaf3a.arista.com | Security | VerifyAPIHttpsSSL | Verifies if the eAPI has a valid SSL profile. | - | NOT RUN | - |
| 2272 | dc2-leaf3a.arista.com | Security | VerifyAPIHttpsSSL | Verifies if the eAPI has a valid SSL profile. | eAPI HTTPS SSL Profile: eAPI_SSL_Profile | NOT RUN | - |
| 2273 | dc2-leaf3a.arista.com | Security | VerifyAPIHttpStatus | Verifies if eAPI HTTP server is disabled globally. | - | NOT RUN | - |
| 2274 | dc2-leaf3a.arista.com | Security | VerifyAPIIPv4Acl | Verifies if eAPI has the right number IPv4 ACL(s) configured for a specified VRF. | - | NOT RUN | - |
| 2275 | dc2-leaf3a.arista.com | Security | VerifyAPIIPv6Acl | Verifies if eAPI has the right number IPv6 ACL(s) configured for a specified VRF. | - | NOT RUN | - |
| 2276 | dc2-leaf3a.arista.com | Security | VerifyAPISSLCertificate | Verifies the eAPI SSL certificate expiry, common subject name, encryption algorithm and key size. | - | NOT RUN | - |
| 2277 | dc2-leaf3a.arista.com | Security | VerifyBannerLogin | Verifies the login banner of a device. | - | NOT RUN | - |
| 2278 | dc2-leaf3a.arista.com | Security | VerifyBannerMotd | Verifies the motd banner of a device. | - | NOT RUN | - |
| 2279 | dc2-leaf3a.arista.com | Security | VerifyIPSecConnHealth | Verifies all IPv4 security connections. | - | NOT RUN | - |
| 2280 | dc2-leaf3a.arista.com | Security | VerifyIPv4ACL | Verifies the configuration of IPv4 ACLs. | - | NOT RUN | - |
| 2281 | dc2-leaf3a.arista.com | Security | VerifySpecificIPSecConn | Verifies IPv4 security connections for a peer. | - | NOT RUN | - |
| 2282 | dc2-leaf3a.arista.com | Security | VerifySSHIPv4Acl | Verifies if the SSHD agent has IPv4 ACL(s) configured. | - | NOT RUN | - |
| 2283 | dc2-leaf3a.arista.com | Security | VerifySSHIPv6Acl | Verifies if the SSHD agent has IPv6 ACL(s) configured. | - | NOT RUN | - |
| 2284 | dc2-leaf3a.arista.com | Security | VerifySSHStatus | Verifies if the SSHD agent is disabled in the default VRF. | - | NOT RUN | - |
| 2285 | dc2-leaf3a.arista.com | Security | VerifyTelnetStatus | Verifies if Telnet is disabled in the default VRF. | - | NOT RUN | - |
| 2286 | dc2-leaf3a.arista.com | Services | VerifyDNSLookup | Verifies the DNS name to IP address resolution. | - | NOT RUN | - |
| 2287 | dc2-leaf3a.arista.com | Services | VerifyDNSServers | Verifies if the DNS servers are correctly configured. | - | NOT RUN | - |
| 2288 | dc2-leaf3a.arista.com | Services | VerifyErrdisableRecovery | Verifies the errdisable recovery reason, status, and interval. | - | NOT RUN | - |
| 2289 | dc2-leaf3a.arista.com | Services | VerifyHostname | Verifies the hostname of a device. | - | NOT RUN | - |
| 2290 | dc2-leaf3a.arista.com | SNMP | VerifySnmpIPv4Acl | Verifies if the SNMP agent has IPv4 ACL(s) configured. | - | NOT RUN | - |
| 2291 | dc2-leaf3a.arista.com | SNMP | VerifySnmpIPv6Acl | Verifies if the SNMP agent has IPv6 ACL(s) configured. | - | NOT RUN | - |
| 2292 | dc2-leaf3a.arista.com | SNMP | VerifySnmpStatus | Verifies if the SNMP agent is enabled. | - | NOT RUN | - |
| 2293 | dc2-leaf3a.arista.com | Software | VerifyEOSVersion | Verifies the EOS version of the device. | - | NOT RUN | - |
| 2294 | dc2-leaf3a.arista.com | Software | VerifyTerminAttrVersion | Verifies the TerminAttr version of the device. | - | NOT RUN | - |
| 2295 | dc2-leaf3a.arista.com | STP | VerifySTPBlockedPorts | Verifies there is no STP blocked ports. | - | NOT RUN | - |
| 2296 | dc2-leaf3a.arista.com | STP | VerifySTPCounters | Verifies there is no errors in STP BPDU packets. | - | NOT RUN | - |
| 2297 | dc2-leaf3a.arista.com | STP | VerifySTPForwardingPorts | Verifies that all interfaces are forwarding for a provided list of VLAN(s). | - | NOT RUN | - |
| 2298 | dc2-leaf3a.arista.com | STP | VerifySTPMode | Verifies the configured STP mode for a provided list of VLAN(s). | - | NOT RUN | - |
| 2299 | dc2-leaf3a.arista.com | STP | VerifySTPRootPriority | Verifies the STP root priority for a provided list of VLAN or MST instance ID(s). | - | NOT RUN | - |
| 2300 | dc2-leaf3a.arista.com | STUN | VerifyStunClient | Verifies the STUN client is configured with the specified IPv4 source address and port. Validate the public IP and port if provided. | - | NOT RUN | - |
| 2301 | dc2-leaf3a.arista.com | System | VerifyAgentLogs | Verifies there are no agent crash reports. | - | NOT RUN | - |
| 2302 | dc2-leaf3a.arista.com | System | VerifyCoredump | Verifies there are no core dump files. | - | NOT RUN | - |
| 2303 | dc2-leaf3a.arista.com | System | VerifyCPUUtilization | Verifies whether the CPU utilization is below 75%. | - | NOT RUN | - |
| 2304 | dc2-leaf3a.arista.com | System | VerifyFileSystemUtilization | Verifies that no partition is utilizing more than 75% of its disk space. | - | NOT RUN | - |
| 2305 | dc2-leaf3a.arista.com | System | VerifyMemoryUtilization | Verifies whether the memory utilization is below 75%. | - | NOT RUN | - |
| 2306 | dc2-leaf3a.arista.com | System | VerifyNTP | Verifies if NTP is synchronised. | - | NOT RUN | - |
| 2307 | dc2-leaf3a.arista.com | System | VerifyNTP | Verifies if NTP is synchronised. | - | NOT RUN | - |
| 2308 | dc2-leaf3a.arista.com | System | VerifyReloadCause | Verifies the last reload cause of the device. | - | NOT RUN | - |
| 2309 | dc2-leaf3a.arista.com | System | VerifyReloadCause | Verifies the last reload cause of the device. | - | NOT RUN | - |
| 2310 | dc2-leaf3a.arista.com | System | VerifyUptime | Verifies the device uptime. | - | NOT RUN | - |
| 2311 | dc2-leaf3a.arista.com | VLAN | VerifyVlanInternalPolicy | Verifies the VLAN internal allocation policy and the range of VLANs. | - | NOT RUN | - |
| 2312 | dc2-leaf3b.arista.com | AAA | VerifyAcctConsoleMethods | Verifies the AAA accounting console method lists for different accounting types (system, exec, commands, dot1x). | - | NOT RUN | - |
| 2313 | dc2-leaf3b.arista.com | AAA | VerifyAcctDefaultMethods | Verifies the AAA accounting default method lists for different accounting types (system, exec, commands, dot1x). | - | NOT RUN | - |
| 2314 | dc2-leaf3b.arista.com | AAA | VerifyAuthenMethods | Verifies the AAA authentication method lists for different authentication types (login, enable, dot1x). | - | NOT RUN | - |
| 2315 | dc2-leaf3b.arista.com | AAA | VerifyAuthzMethods | Verifies the AAA authorization method lists for different authorization types (commands, exec). | - | NOT RUN | - |
| 2316 | dc2-leaf3b.arista.com | AAA | VerifyTacacsServerGroups | Verifies if the provided TACACS server group(s) are configured. | - | NOT RUN | - |
| 2317 | dc2-leaf3b.arista.com | AAA | VerifyTacacsServers | Verifies TACACS servers are configured for a specified VRF. | - | NOT RUN | - |
| 2318 | dc2-leaf3b.arista.com | AAA | VerifyTacacsSourceIntf | Verifies TACACS source-interface for a specified VRF. | - | NOT RUN | - |
| 2319 | dc2-leaf3b.arista.com | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: dc2-spine1 (IP: 10.255.128.11) | NOT RUN | - |
| 2320 | dc2-leaf3b.arista.com | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: dc2-spine2 (IP: 10.255.128.12) | NOT RUN | - |
| 2321 | dc2-leaf3b.arista.com | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: dc2-leaf3a.arista.com (IP: 10.255.129.124) | NOT RUN | - |
| 2322 | dc2-leaf3b.arista.com | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: dc2-spine1 (IP: 10.255.255.124) | NOT RUN | - |
| 2323 | dc2-leaf3b.arista.com | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: dc2-spine2 (IP: 10.255.255.126) | NOT RUN | - |
| 2324 | dc2-leaf3b.arista.com | Configuration | VerifyRunningConfigDiffs | Verifies there is no difference between the running-config and the startup-config | - | NOT RUN | - |
| 2325 | dc2-leaf3b.arista.com | Configuration | VerifyZeroTouch | Verifies ZeroTouch is disabled | - | NOT RUN | - |
| 2326 | dc2-leaf3b.arista.com | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet1 - Remote: dc2-spine1 Ethernet6 | NOT RUN | - |
| 2327 | dc2-leaf3b.arista.com | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet2 - Remote: dc2-spine2 Ethernet6 | NOT RUN | - |
| 2328 | dc2-leaf3b.arista.com | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet3 - Remote: dc2-leaf3a.arista.com Ethernet3 | NOT RUN | - |
| 2329 | dc2-leaf3b.arista.com | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet4 - Remote: dc2-leaf3a.arista.com Ethernet4 | NOT RUN | - |
| 2330 | dc2-leaf3b.arista.com | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.128.18) - Destination: dc1-leaf1a Loopback0 (IP: 10.255.0.3) | NOT RUN | - |
| 2331 | dc2-leaf3b.arista.com | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.128.18) - Destination: dc1-leaf1b Loopback0 (IP: 10.255.0.4) | NOT RUN | - |
| 2332 | dc2-leaf3b.arista.com | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.128.18) - Destination: dc1-leaf2a Loopback0 (IP: 10.255.0.5) | NOT RUN | - |
| 2333 | dc2-leaf3b.arista.com | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.128.18) - Destination: dc1-spine1 Loopback0 (IP: 10.255.0.1) | NOT RUN | - |
| 2334 | dc2-leaf3b.arista.com | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.128.18) - Destination: dc1-spine2 Loopback0 (IP: 10.255.0.2) | NOT RUN | - |
| 2335 | dc2-leaf3b.arista.com | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.128.18) - Destination: dc1-svc-leaf1a Loopback0 (IP: 10.33.0.5) | NOT RUN | - |
| 2336 | dc2-leaf3b.arista.com | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.128.18) - Destination: dc1-svc-leaf1b Loopback0 (IP: 10.33.0.6) | NOT RUN | - |
| 2337 | dc2-leaf3b.arista.com | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.128.18) - Destination: dc1-wan1 Loopback0 (IP: 10.255.2.1) | NOT RUN | - |
| 2338 | dc2-leaf3b.arista.com | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.128.18) - Destination: dc1-wan2 Loopback0 (IP: 10.255.2.2) | NOT RUN | - |
| 2339 | dc2-leaf3b.arista.com | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.128.18) - Destination: dc2-leaf1a Loopback0 (IP: 10.255.128.13) | NOT RUN | - |
| 2340 | dc2-leaf3b.arista.com | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.128.18) - Destination: dc2-leaf1b Loopback0 (IP: 10.255.128.14) | NOT RUN | - |
| 2341 | dc2-leaf3b.arista.com | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.128.18) - Destination: dc2-leaf2a Loopback0 (IP: 10.255.128.15) | NOT RUN | - |
| 2342 | dc2-leaf3b.arista.com | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.128.18) - Destination: dc2-leaf2b Loopback0 (IP: 10.255.128.16) | NOT RUN | - |
| 2343 | dc2-leaf3b.arista.com | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.128.18) - Destination: dc2-leaf3a.arista.com Loopback0 (IP: 10.255.128.17) | NOT RUN | - |
| 2344 | dc2-leaf3b.arista.com | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.128.18) - Destination: dc2-leaf3b.arista.com Loopback0 (IP: 10.255.128.18) | NOT RUN | - |
| 2345 | dc2-leaf3b.arista.com | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.128.18) - Destination: dc2-spine1 Loopback0 (IP: 10.255.128.11) | NOT RUN | - |
| 2346 | dc2-leaf3b.arista.com | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 10.255.128.18) - Destination: dc2-spine2 Loopback0 (IP: 10.255.128.12) | NOT RUN | - |
| 2347 | dc2-leaf3b.arista.com | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet1 (IP: 10.255.255.125) - Destination: dc2-spine1 Ethernet6 (IP: 10.255.255.124) | NOT RUN | - |
| 2348 | dc2-leaf3b.arista.com | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet2 (IP: 10.255.255.127) - Destination: dc2-spine2 Ethernet6 (IP: 10.255.255.126) | NOT RUN | - |
| 2349 | dc2-leaf3b.arista.com | Field Notices | VerifyFieldNotice44Resolution | Verifies that the device is using the correct Aboot version per FN0044. | - | NOT RUN | - |
| 2350 | dc2-leaf3b.arista.com | Field Notices | VerifyFieldNotice72Resolution | Verifies if the device is exposed to FN0072, and if the issue has been mitigated. | - | NOT RUN | - |
| 2351 | dc2-leaf3b.arista.com | Greent | VerifyGreenT | Verifies if a GreenT policy is created. | - | NOT RUN | - |
| 2352 | dc2-leaf3b.arista.com | Greent | VerifyGreenTCounters | Verifies if the GreenT counters are incremented. | - | NOT RUN | - |
| 2353 | dc2-leaf3b.arista.com | Hardware | VerifyAdverseDrops | Verifies there are no adverse drops on DCS-7280 and DCS-7500 family switches. | - | NOT RUN | - |
| 2354 | dc2-leaf3b.arista.com | Hardware | VerifyEnvironmentCooling | Verifies the status of power supply fans and all fan trays. | - | NOT RUN | - |
| 2355 | dc2-leaf3b.arista.com | Hardware | VerifyEnvironmentCooling | Verifies the status of power supply fans and all fan trays. | Accepted States: 'ok' | NOT RUN | - |
| 2356 | dc2-leaf3b.arista.com | Hardware | VerifyEnvironmentPower | Verifies the power supplies status. | - | NOT RUN | - |
| 2357 | dc2-leaf3b.arista.com | Hardware | VerifyEnvironmentPower | Verifies the power supplies status. | Accepted States: 'ok' | NOT RUN | - |
| 2358 | dc2-leaf3b.arista.com | Hardware | VerifyEnvironmentSystemCooling | Verifies the system cooling status. | - | NOT RUN | - |
| 2359 | dc2-leaf3b.arista.com | Hardware | VerifyTemperature | Verifies the device temperature. | - | NOT RUN | - |
| 2360 | dc2-leaf3b.arista.com | Hardware | VerifyTemperature | Verifies the device temperature. | - | NOT RUN | - |
| 2361 | dc2-leaf3b.arista.com | Hardware | VerifyTransceiversManufacturers | Verifies if all transceivers come from approved manufacturers. | - | NOT RUN | - |
| 2362 | dc2-leaf3b.arista.com | Hardware | VerifyTransceiversManufacturers | Verifies if all transceivers come from approved manufacturers. | Accepted Manufacturers: 'Arista Networks', 'Arastra, Inc.', 'Not Present' | NOT RUN | - |
| 2363 | dc2-leaf3b.arista.com | Hardware | VerifyTransceiversTemperature | Verifies the transceivers temperature. | - | NOT RUN | - |
| 2364 | dc2-leaf3b.arista.com | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet1 - P2P_LINK_TO_DC2-SPINE1_Ethernet6 = 'up' | NOT RUN | - |
| 2365 | dc2-leaf3b.arista.com | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet11 - dc2-leaf3-fw1_e1 = 'adminDown' | NOT RUN | - |
| 2366 | dc2-leaf3b.arista.com | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet2 - P2P_LINK_TO_DC2-SPINE2_Ethernet6 = 'up' | NOT RUN | - |
| 2367 | dc2-leaf3b.arista.com | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet3 - MLAG_dc2-leaf3a.arista.com_Ethernet3 = 'up' | NOT RUN | - |
| 2368 | dc2-leaf3b.arista.com | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet4 - MLAG_dc2-leaf3a.arista.com_Ethernet4 = 'up' | NOT RUN | - |
| 2369 | dc2-leaf3b.arista.com | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback0 - ROUTER_ID = 'up' | NOT RUN | - |
| 2370 | dc2-leaf3b.arista.com | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback1 - VXLAN_TUNNEL_SOURCE = 'up' | NOT RUN | - |
| 2371 | dc2-leaf3b.arista.com | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback10 - VRF10_VTEP_DIAGNOSTICS = 'up' | NOT RUN | - |
| 2372 | dc2-leaf3b.arista.com | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback11 - VRF11_VTEP_DIAGNOSTICS = 'up' | NOT RUN | - |
| 2373 | dc2-leaf3b.arista.com | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel11 - dc2-leaf3-fw1_PortChannel = 'up' | NOT RUN | - |
| 2374 | dc2-leaf3b.arista.com | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Port-Channel3 - MLAG_dc2-leaf3a.arista.com_Port-Channel3 = 'up' | NOT RUN | - |
| 2375 | dc2-leaf3b.arista.com | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan11 - VRF10_VLAN11 = 'up' | NOT RUN | - |
| 2376 | dc2-leaf3b.arista.com | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan12 - VRF10_VLAN12 = 'up' | NOT RUN | - |
| 2377 | dc2-leaf3b.arista.com | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan21 - VRF11_VLAN21 = 'up' | NOT RUN | - |
| 2378 | dc2-leaf3b.arista.com | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan22 - VRF11_VLAN22 = 'up' | NOT RUN | - |
| 2379 | dc2-leaf3b.arista.com | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan3009 - MLAG_L3_VRF_VRF10 = 'up' | NOT RUN | - |
| 2380 | dc2-leaf3b.arista.com | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan3010 - MLAG_L3_VRF_VRF11 = 'up' | NOT RUN | - |
| 2381 | dc2-leaf3b.arista.com | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan4093 - MLAG_L3 = 'up' | NOT RUN | - |
| 2382 | dc2-leaf3b.arista.com | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vlan4094 - MLAG = 'up' | NOT RUN | - |
| 2383 | dc2-leaf3b.arista.com | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Vxlan1 = 'up' | NOT RUN | - |
| 2384 | dc2-leaf3b.arista.com | LANZ | VerifyLANZ | Verifies if LANZ is enabled. | - | NOT RUN | - |
| 2385 | dc2-leaf3b.arista.com | Logging | VerifyLoggingAccounting | Verifies if AAA accounting logs are generated. | - | NOT RUN | - |
| 2386 | dc2-leaf3b.arista.com | Logging | VerifyLoggingErrors | Verifies there are no syslog messages with a severity of ERRORS or higher. | - | NOT RUN | - |
| 2387 | dc2-leaf3b.arista.com | Logging | VerifyLoggingHostname | Verifies if logs are generated with the device FQDN. | - | NOT RUN | - |
| 2388 | dc2-leaf3b.arista.com | Logging | VerifyLoggingHosts | Verifies logging hosts (syslog servers) for a specified VRF. | - | NOT RUN | - |
| 2389 | dc2-leaf3b.arista.com | Logging | VerifyLoggingLogsGeneration | Verifies if logs are generated. | - | NOT RUN | - |
| 2390 | dc2-leaf3b.arista.com | Logging | VerifyLoggingPersistent | Verifies if logging persistent is enabled and logs are saved in flash. | - | NOT RUN | - |
| 2391 | dc2-leaf3b.arista.com | Logging | VerifyLoggingSourceInt | Verifies logging source-interface for a specified VRF. | - | NOT RUN | - |
| 2392 | dc2-leaf3b.arista.com | Logging | VerifyLoggingTimestamp | Verifies if logs are generated with the riate timestamp. | - | NOT RUN | - |
| 2393 | dc2-leaf3b.arista.com | MLAG | VerifyMlagConfigSanity | Verifies there are no MLAG config-sanity inconsistencies. | - | NOT RUN | - |
| 2394 | dc2-leaf3b.arista.com | MLAG | VerifyMlagDualPrimary | Verifies the MLAG dual-primary detection parameters. | - | NOT RUN | - |
| 2395 | dc2-leaf3b.arista.com | MLAG | VerifyMlagInterfaces | Verifies there are no inactive or active-partial MLAG ports. | - | NOT RUN | - |
| 2396 | dc2-leaf3b.arista.com | MLAG | VerifyMlagReloadDelay | Verifies the MLAG reload-delay parameters. | - | NOT RUN | - |
| 2397 | dc2-leaf3b.arista.com | MLAG | VerifyMlagStatus | Verifies the health status of the MLAG configuration. | - | NOT RUN | - |
| 2398 | dc2-leaf3b.arista.com | MLAG | VerifyMlagStatus | Verifies the health status of the MLAG configuration. | - | NOT RUN | - |
| 2399 | dc2-leaf3b.arista.com | Multicast | VerifyIGMPSnoopingGlobal | Verifies the IGMP snooping global configuration. | - | NOT RUN | - |
| 2400 | dc2-leaf3b.arista.com | Multicast | VerifyIGMPSnoopingVlans | Verifies the IGMP snooping status for the provided VLANs. | - | NOT RUN | - |
| 2401 | dc2-leaf3b.arista.com | PTP | VerifyPtpGMStatus | Verifies that the device is locked to a valid PTP Grandmaster. | - | NOT RUN | - |
| 2402 | dc2-leaf3b.arista.com | PTP | VerifyPtpLockStatus | Verifies that the device was locked to the upstream PTP GM in the last minute. | - | NOT RUN | - |
| 2403 | dc2-leaf3b.arista.com | PTP | VerifyPtpModeStatus | Verifies that the device is configured as a PTP Boundary Clock. | - | NOT RUN | - |
| 2404 | dc2-leaf3b.arista.com | PTP | VerifyPtpOffset | Verifies that the PTP timing offset is within +/- 1000ns from the master clock. | - | NOT RUN | - |
| 2405 | dc2-leaf3b.arista.com | PTP | VerifyPtpPortModeStatus | Verifies the PTP interfaces state. | - | NOT RUN | - |
| 2406 | dc2-leaf3b.arista.com | Routing | VerifyRoutingProtocolModel | Verifies the configured routing protocol model. | Routing protocol model: multi-agent | NOT RUN | - |
| 2407 | dc2-leaf3b.arista.com | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.0.1 - Peer: dc1-spine1 | NOT RUN | - |
| 2408 | dc2-leaf3b.arista.com | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.0.2 - Peer: dc1-spine2 | NOT RUN | - |
| 2409 | dc2-leaf3b.arista.com | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.0.3 - Peer: dc1-leaf1a | NOT RUN | - |
| 2410 | dc2-leaf3b.arista.com | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.0.4 - Peer: dc1-leaf1b | NOT RUN | - |
| 2411 | dc2-leaf3b.arista.com | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.0.5 - Peer: dc1-leaf2a | NOT RUN | - |
| 2412 | dc2-leaf3b.arista.com | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.1.3 - Peer: dc1-leaf1a | NOT RUN | - |
| 2413 | dc2-leaf3b.arista.com | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.1.5 - Peer: dc1-leaf2a | NOT RUN | - |
| 2414 | dc2-leaf3b.arista.com | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.128.11 - Peer: dc2-spine1 | NOT RUN | - |
| 2415 | dc2-leaf3b.arista.com | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.128.12 - Peer: dc2-spine2 | NOT RUN | - |
| 2416 | dc2-leaf3b.arista.com | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.128.13 - Peer: dc2-leaf1a | NOT RUN | - |
| 2417 | dc2-leaf3b.arista.com | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.128.14 - Peer: dc2-leaf1b | NOT RUN | - |
| 2418 | dc2-leaf3b.arista.com | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.128.15 - Peer: dc2-leaf2a | NOT RUN | - |
| 2419 | dc2-leaf3b.arista.com | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.128.16 - Peer: dc2-leaf2b | NOT RUN | - |
| 2420 | dc2-leaf3b.arista.com | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.128.17 - Peer: dc2-leaf3a.arista.com | NOT RUN | - |
| 2421 | dc2-leaf3b.arista.com | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.128.18 - Peer: dc2-leaf3b.arista.com | NOT RUN | - |
| 2422 | dc2-leaf3b.arista.com | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.129.13 - Peer: dc2-leaf1a | NOT RUN | - |
| 2423 | dc2-leaf3b.arista.com | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.129.15 - Peer: dc2-leaf2a | NOT RUN | - |
| 2424 | dc2-leaf3b.arista.com | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.129.17 - Peer: dc2-leaf3a.arista.com | NOT RUN | - |
| 2425 | dc2-leaf3b.arista.com | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.2.1 - Peer: dc1-wan1 | NOT RUN | - |
| 2426 | dc2-leaf3b.arista.com | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.255.2.2 - Peer: dc1-wan2 | NOT RUN | - |
| 2427 | dc2-leaf3b.arista.com | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.33.0.5 - Peer: dc1-svc-leaf1a | NOT RUN | - |
| 2428 | dc2-leaf3b.arista.com | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.33.0.6 - Peer: dc1-svc-leaf1b | NOT RUN | - |
| 2429 | dc2-leaf3b.arista.com | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 10.33.1.5 - Peer: dc1-svc-leaf1a | NOT RUN | - |
| 2430 | dc2-leaf3b.arista.com | Security | VerifyAPIHttpsSSL | Verifies if the eAPI has a valid SSL profile. | - | NOT RUN | - |
| 2431 | dc2-leaf3b.arista.com | Security | VerifyAPIHttpsSSL | Verifies if the eAPI has a valid SSL profile. | eAPI HTTPS SSL Profile: eAPI_SSL_Profile | NOT RUN | - |
| 2432 | dc2-leaf3b.arista.com | Security | VerifyAPIHttpStatus | Verifies if eAPI HTTP server is disabled globally. | - | NOT RUN | - |
| 2433 | dc2-leaf3b.arista.com | Security | VerifyAPIIPv4Acl | Verifies if eAPI has the right number IPv4 ACL(s) configured for a specified VRF. | - | NOT RUN | - |
| 2434 | dc2-leaf3b.arista.com | Security | VerifyAPIIPv6Acl | Verifies if eAPI has the right number IPv6 ACL(s) configured for a specified VRF. | - | NOT RUN | - |
| 2435 | dc2-leaf3b.arista.com | Security | VerifyAPISSLCertificate | Verifies the eAPI SSL certificate expiry, common subject name, encryption algorithm and key size. | - | NOT RUN | - |
| 2436 | dc2-leaf3b.arista.com | Security | VerifyBannerLogin | Verifies the login banner of a device. | - | NOT RUN | - |
| 2437 | dc2-leaf3b.arista.com | Security | VerifyBannerMotd | Verifies the motd banner of a device. | - | NOT RUN | - |
| 2438 | dc2-leaf3b.arista.com | Security | VerifyIPSecConnHealth | Verifies all IPv4 security connections. | - | NOT RUN | - |
| 2439 | dc2-leaf3b.arista.com | Security | VerifyIPv4ACL | Verifies the configuration of IPv4 ACLs. | - | NOT RUN | - |
| 2440 | dc2-leaf3b.arista.com | Security | VerifySpecificIPSecConn | Verifies IPv4 security connections for a peer. | - | NOT RUN | - |
| 2441 | dc2-leaf3b.arista.com | Security | VerifySSHIPv4Acl | Verifies if the SSHD agent has IPv4 ACL(s) configured. | - | NOT RUN | - |
| 2442 | dc2-leaf3b.arista.com | Security | VerifySSHIPv6Acl | Verifies if the SSHD agent has IPv6 ACL(s) configured. | - | NOT RUN | - |
| 2443 | dc2-leaf3b.arista.com | Security | VerifySSHStatus | Verifies if the SSHD agent is disabled in the default VRF. | - | NOT RUN | - |
| 2444 | dc2-leaf3b.arista.com | Security | VerifyTelnetStatus | Verifies if Telnet is disabled in the default VRF. | - | NOT RUN | - |
| 2445 | dc2-leaf3b.arista.com | Services | VerifyDNSLookup | Verifies the DNS name to IP address resolution. | - | NOT RUN | - |
| 2446 | dc2-leaf3b.arista.com | Services | VerifyDNSServers | Verifies if the DNS servers are correctly configured. | - | NOT RUN | - |
| 2447 | dc2-leaf3b.arista.com | Services | VerifyErrdisableRecovery | Verifies the errdisable recovery reason, status, and interval. | - | NOT RUN | - |
| 2448 | dc2-leaf3b.arista.com | Services | VerifyHostname | Verifies the hostname of a device. | - | NOT RUN | - |
| 2449 | dc2-leaf3b.arista.com | SNMP | VerifySnmpIPv4Acl | Verifies if the SNMP agent has IPv4 ACL(s) configured. | - | NOT RUN | - |
| 2450 | dc2-leaf3b.arista.com | SNMP | VerifySnmpIPv6Acl | Verifies if the SNMP agent has IPv6 ACL(s) configured. | - | NOT RUN | - |
| 2451 | dc2-leaf3b.arista.com | SNMP | VerifySnmpStatus | Verifies if the SNMP agent is enabled. | - | NOT RUN | - |
| 2452 | dc2-leaf3b.arista.com | Software | VerifyEOSVersion | Verifies the EOS version of the device. | - | NOT RUN | - |
| 2453 | dc2-leaf3b.arista.com | Software | VerifyTerminAttrVersion | Verifies the TerminAttr version of the device. | - | NOT RUN | - |
| 2454 | dc2-leaf3b.arista.com | STP | VerifySTPBlockedPorts | Verifies there is no STP blocked ports. | - | NOT RUN | - |
| 2455 | dc2-leaf3b.arista.com | STP | VerifySTPCounters | Verifies there is no errors in STP BPDU packets. | - | NOT RUN | - |
| 2456 | dc2-leaf3b.arista.com | STP | VerifySTPForwardingPorts | Verifies that all interfaces are forwarding for a provided list of VLAN(s). | - | NOT RUN | - |
| 2457 | dc2-leaf3b.arista.com | STP | VerifySTPMode | Verifies the configured STP mode for a provided list of VLAN(s). | - | NOT RUN | - |
| 2458 | dc2-leaf3b.arista.com | STP | VerifySTPRootPriority | Verifies the STP root priority for a provided list of VLAN or MST instance ID(s). | - | NOT RUN | - |
| 2459 | dc2-leaf3b.arista.com | STUN | VerifyStunClient | Verifies the STUN client is configured with the specified IPv4 source address and port. Validate the public IP and port if provided. | - | NOT RUN | - |
| 2460 | dc2-leaf3b.arista.com | System | VerifyAgentLogs | Verifies there are no agent crash reports. | - | NOT RUN | - |
| 2461 | dc2-leaf3b.arista.com | System | VerifyCoredump | Verifies there are no core dump files. | - | NOT RUN | - |
| 2462 | dc2-leaf3b.arista.com | System | VerifyCPUUtilization | Verifies whether the CPU utilization is below 75%. | - | NOT RUN | - |
| 2463 | dc2-leaf3b.arista.com | System | VerifyFileSystemUtilization | Verifies that no partition is utilizing more than 75% of its disk space. | - | NOT RUN | - |
| 2464 | dc2-leaf3b.arista.com | System | VerifyMemoryUtilization | Verifies whether the memory utilization is below 75%. | - | NOT RUN | - |
| 2465 | dc2-leaf3b.arista.com | System | VerifyNTP | Verifies if NTP is synchronised. | - | NOT RUN | - |
| 2466 | dc2-leaf3b.arista.com | System | VerifyNTP | Verifies if NTP is synchronised. | - | NOT RUN | - |
| 2467 | dc2-leaf3b.arista.com | System | VerifyReloadCause | Verifies the last reload cause of the device. | - | NOT RUN | - |
| 2468 | dc2-leaf3b.arista.com | System | VerifyReloadCause | Verifies the last reload cause of the device. | - | NOT RUN | - |
| 2469 | dc2-leaf3b.arista.com | System | VerifyUptime | Verifies the device uptime. | - | NOT RUN | - |
| 2470 | dc2-leaf3b.arista.com | VLAN | VerifyVlanInternalPolicy | Verifies the VLAN internal allocation policy and the range of VLANs. | - | NOT RUN | - |
| 2471 | dc2-spine1 | AAA | VerifyAcctConsoleMethods | Verifies the AAA accounting console method lists for different accounting types (system, exec, commands, dot1x). | - | NOT RUN | - |
| 2472 | dc2-spine1 | AAA | VerifyAcctDefaultMethods | Verifies the AAA accounting default method lists for different accounting types (system, exec, commands, dot1x). | - | NOT RUN | - |
| 2473 | dc2-spine1 | AAA | VerifyAuthenMethods | Verifies the AAA authentication method lists for different authentication types (login, enable, dot1x). | - | NOT RUN | - |
| 2474 | dc2-spine1 | AAA | VerifyAuthzMethods | Verifies the AAA authorization method lists for different authorization types (commands, exec). | - | NOT RUN | - |
| 2475 | dc2-spine1 | AAA | VerifyTacacsServerGroups | Verifies if the provided TACACS server group(s) are configured. | - | NOT RUN | - |
| 2476 | dc2-spine1 | AAA | VerifyTacacsServers | Verifies TACACS servers are configured for a specified VRF. | - | NOT RUN | - |
| 2477 | dc2-spine1 | AAA | VerifyTacacsSourceIntf | Verifies TACACS source-interface for a specified VRF. | - | NOT RUN | - |
| 2478 | dc2-spine1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: dc2-leaf1a (IP: 10.255.128.13) | NOT RUN | - |
| 2479 | dc2-spine1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: dc2-leaf1b (IP: 10.255.128.14) | NOT RUN | - |
| 2480 | dc2-spine1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: dc2-leaf2a (IP: 10.255.128.15) | NOT RUN | - |
| 2481 | dc2-spine1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: dc2-leaf2b (IP: 10.255.128.16) | NOT RUN | - |
| 2482 | dc2-spine1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: dc2-leaf3a.arista.com (IP: 10.255.128.17) | NOT RUN | - |
| 2483 | dc2-spine1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: dc2-leaf3b.arista.com (IP: 10.255.128.18) | NOT RUN | - |
| 2484 | dc2-spine1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: dc2-leaf1a (IP: 10.255.255.105) | NOT RUN | - |
| 2485 | dc2-spine1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: dc2-leaf1b (IP: 10.255.255.109) | NOT RUN | - |
| 2486 | dc2-spine1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: dc2-leaf2a (IP: 10.255.255.113) | NOT RUN | - |
| 2487 | dc2-spine1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: dc2-leaf2b (IP: 10.255.255.117) | NOT RUN | - |
| 2488 | dc2-spine1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: dc2-leaf3a.arista.com (IP: 10.255.255.121) | NOT RUN | - |
| 2489 | dc2-spine1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: dc2-leaf3b.arista.com (IP: 10.255.255.125) | NOT RUN | - |
| 2490 | dc2-spine1 | Configuration | VerifyRunningConfigDiffs | Verifies there is no difference between the running-config and the startup-config | - | NOT RUN | - |
| 2491 | dc2-spine1 | Configuration | VerifyZeroTouch | Verifies ZeroTouch is disabled | - | NOT RUN | - |
| 2492 | dc2-spine1 | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet1 - Remote: dc2-leaf1a Ethernet1 | NOT RUN | - |
| 2493 | dc2-spine1 | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet2 - Remote: dc2-leaf1b Ethernet1 | NOT RUN | - |
| 2494 | dc2-spine1 | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet3 - Remote: dc2-leaf2a Ethernet1 | NOT RUN | - |
| 2495 | dc2-spine1 | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet4 - Remote: dc2-leaf2b Ethernet1 | NOT RUN | - |
| 2496 | dc2-spine1 | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet5 - Remote: dc2-leaf3a.arista.com Ethernet1 | NOT RUN | - |
| 2497 | dc2-spine1 | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet6 - Remote: dc2-leaf3b.arista.com Ethernet1 | NOT RUN | - |
| 2498 | dc2-spine1 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet1 (IP: 10.255.255.104) - Destination: dc2-leaf1a Ethernet1 (IP: 10.255.255.105) | NOT RUN | - |
| 2499 | dc2-spine1 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet2 (IP: 10.255.255.108) - Destination: dc2-leaf1b Ethernet1 (IP: 10.255.255.109) | NOT RUN | - |
| 2500 | dc2-spine1 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet3 (IP: 10.255.255.112) - Destination: dc2-leaf2a Ethernet1 (IP: 10.255.255.113) | NOT RUN | - |
| 2501 | dc2-spine1 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet4 (IP: 10.255.255.116) - Destination: dc2-leaf2b Ethernet1 (IP: 10.255.255.117) | NOT RUN | - |
| 2502 | dc2-spine1 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet5 (IP: 10.255.255.120) - Destination: dc2-leaf3a.arista.com Ethernet1 (IP: 10.255.255.121) | NOT RUN | - |
| 2503 | dc2-spine1 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet6 (IP: 10.255.255.124) - Destination: dc2-leaf3b.arista.com Ethernet1 (IP: 10.255.255.125) | NOT RUN | - |
| 2504 | dc2-spine1 | Field Notices | VerifyFieldNotice44Resolution | Verifies that the device is using the correct Aboot version per FN0044. | - | NOT RUN | - |
| 2505 | dc2-spine1 | Field Notices | VerifyFieldNotice72Resolution | Verifies if the device is exposed to FN0072, and if the issue has been mitigated. | - | NOT RUN | - |
| 2506 | dc2-spine1 | Greent | VerifyGreenT | Verifies if a GreenT policy is created. | - | NOT RUN | - |
| 2507 | dc2-spine1 | Greent | VerifyGreenTCounters | Verifies if the GreenT counters are incremented. | - | NOT RUN | - |
| 2508 | dc2-spine1 | Hardware | VerifyAdverseDrops | Verifies there are no adverse drops on DCS-7280 and DCS-7500 family switches. | - | NOT RUN | - |
| 2509 | dc2-spine1 | Hardware | VerifyEnvironmentCooling | Verifies the status of power supply fans and all fan trays. | - | NOT RUN | - |
| 2510 | dc2-spine1 | Hardware | VerifyEnvironmentCooling | Verifies the status of power supply fans and all fan trays. | Accepted States: 'ok' | NOT RUN | - |
| 2511 | dc2-spine1 | Hardware | VerifyEnvironmentPower | Verifies the power supplies status. | - | NOT RUN | - |
| 2512 | dc2-spine1 | Hardware | VerifyEnvironmentPower | Verifies the power supplies status. | Accepted States: 'ok' | NOT RUN | - |
| 2513 | dc2-spine1 | Hardware | VerifyEnvironmentSystemCooling | Verifies the system cooling status. | - | NOT RUN | - |
| 2514 | dc2-spine1 | Hardware | VerifyTemperature | Verifies the device temperature. | - | NOT RUN | - |
| 2515 | dc2-spine1 | Hardware | VerifyTemperature | Verifies the device temperature. | - | NOT RUN | - |
| 2516 | dc2-spine1 | Hardware | VerifyTransceiversManufacturers | Verifies if all transceivers come from approved manufacturers. | - | NOT RUN | - |
| 2517 | dc2-spine1 | Hardware | VerifyTransceiversManufacturers | Verifies if all transceivers come from approved manufacturers. | Accepted Manufacturers: 'Arista Networks', 'Arastra, Inc.', 'Not Present' | NOT RUN | - |
| 2518 | dc2-spine1 | Hardware | VerifyTransceiversTemperature | Verifies the transceivers temperature. | - | NOT RUN | - |
| 2519 | dc2-spine1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet1 - P2P_LINK_TO_DC2-LEAF1A_Ethernet1 = 'up' | NOT RUN | - |
| 2520 | dc2-spine1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet2 - P2P_LINK_TO_DC2-LEAF1B_Ethernet1 = 'up' | NOT RUN | - |
| 2521 | dc2-spine1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet3 - P2P_LINK_TO_DC2-LEAF2A_Ethernet1 = 'up' | NOT RUN | - |
| 2522 | dc2-spine1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet4 - P2P_LINK_TO_DC2-LEAF2B_Ethernet1 = 'up' | NOT RUN | - |
| 2523 | dc2-spine1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet5 - P2P_LINK_TO_DC2-LEAF3A.ARISTA.COM_Ethernet1 = 'up' | NOT RUN | - |
| 2524 | dc2-spine1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet6 - P2P_LINK_TO_DC2-LEAF3B.ARISTA.COM_Ethernet1 = 'up' | NOT RUN | - |
| 2525 | dc2-spine1 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback0 - ROUTER_ID = 'up' | NOT RUN | - |
| 2526 | dc2-spine1 | LANZ | VerifyLANZ | Verifies if LANZ is enabled. | - | NOT RUN | - |
| 2527 | dc2-spine1 | PTP | VerifyPtpGMStatus | Verifies that the device is locked to a valid PTP Grandmaster. | - | NOT RUN | - |
| 2528 | dc2-spine1 | PTP | VerifyPtpLockStatus | Verifies that the device was locked to the upstream PTP GM in the last minute. | - | NOT RUN | - |
| 2529 | dc2-spine1 | PTP | VerifyPtpModeStatus | Verifies that the device is configured as a PTP Boundary Clock. | - | NOT RUN | - |
| 2530 | dc2-spine1 | PTP | VerifyPtpOffset | Verifies that the PTP timing offset is within +/- 1000ns from the master clock. | - | NOT RUN | - |
| 2531 | dc2-spine1 | PTP | VerifyPtpPortModeStatus | Verifies the PTP interfaces state. | - | NOT RUN | - |
| 2532 | dc2-spine1 | Routing | VerifyRoutingProtocolModel | Verifies the configured routing protocol model. | Routing protocol model: multi-agent | NOT RUN | - |
| 2533 | dc2-spine1 | Security | VerifyAPIHttpsSSL | Verifies if the eAPI has a valid SSL profile. | - | NOT RUN | - |
| 2534 | dc2-spine1 | Security | VerifyAPIHttpsSSL | Verifies if the eAPI has a valid SSL profile. | eAPI HTTPS SSL Profile: eAPI_SSL_Profile | NOT RUN | - |
| 2535 | dc2-spine1 | Security | VerifyAPIHttpStatus | Verifies if eAPI HTTP server is disabled globally. | - | NOT RUN | - |
| 2536 | dc2-spine1 | Security | VerifyAPIIPv4Acl | Verifies if eAPI has the right number IPv4 ACL(s) configured for a specified VRF. | - | NOT RUN | - |
| 2537 | dc2-spine1 | Security | VerifyAPIIPv6Acl | Verifies if eAPI has the right number IPv6 ACL(s) configured for a specified VRF. | - | NOT RUN | - |
| 2538 | dc2-spine1 | Security | VerifyAPISSLCertificate | Verifies the eAPI SSL certificate expiry, common subject name, encryption algorithm and key size. | - | NOT RUN | - |
| 2539 | dc2-spine1 | Security | VerifyBannerLogin | Verifies the login banner of a device. | - | NOT RUN | - |
| 2540 | dc2-spine1 | Security | VerifyBannerMotd | Verifies the motd banner of a device. | - | NOT RUN | - |
| 2541 | dc2-spine1 | Security | VerifyIPSecConnHealth | Verifies all IPv4 security connections. | - | NOT RUN | - |
| 2542 | dc2-spine1 | Security | VerifyIPv4ACL | Verifies the configuration of IPv4 ACLs. | - | NOT RUN | - |
| 2543 | dc2-spine1 | Security | VerifySpecificIPSecConn | Verifies IPv4 security connections for a peer. | - | NOT RUN | - |
| 2544 | dc2-spine1 | Security | VerifySSHIPv4Acl | Verifies if the SSHD agent has IPv4 ACL(s) configured. | - | NOT RUN | - |
| 2545 | dc2-spine1 | Security | VerifySSHIPv6Acl | Verifies if the SSHD agent has IPv6 ACL(s) configured. | - | NOT RUN | - |
| 2546 | dc2-spine1 | Security | VerifySSHStatus | Verifies if the SSHD agent is disabled in the default VRF. | - | NOT RUN | - |
| 2547 | dc2-spine1 | Security | VerifyTelnetStatus | Verifies if Telnet is disabled in the default VRF. | - | NOT RUN | - |
| 2548 | dc2-spine1 | Services | VerifyDNSLookup | Verifies the DNS name to IP address resolution. | - | NOT RUN | - |
| 2549 | dc2-spine1 | Services | VerifyDNSServers | Verifies if the DNS servers are correctly configured. | - | NOT RUN | - |
| 2550 | dc2-spine1 | Services | VerifyErrdisableRecovery | Verifies the errdisable recovery reason, status, and interval. | - | NOT RUN | - |
| 2551 | dc2-spine1 | Services | VerifyHostname | Verifies the hostname of a device. | - | NOT RUN | - |
| 2552 | dc2-spine1 | SNMP | VerifySnmpIPv4Acl | Verifies if the SNMP agent has IPv4 ACL(s) configured. | - | NOT RUN | - |
| 2553 | dc2-spine1 | SNMP | VerifySnmpIPv6Acl | Verifies if the SNMP agent has IPv6 ACL(s) configured. | - | NOT RUN | - |
| 2554 | dc2-spine1 | SNMP | VerifySnmpStatus | Verifies if the SNMP agent is enabled. | - | NOT RUN | - |
| 2555 | dc2-spine1 | Software | VerifyEOSVersion | Verifies the EOS version of the device. | - | NOT RUN | - |
| 2556 | dc2-spine1 | Software | VerifyTerminAttrVersion | Verifies the TerminAttr version of the device. | - | NOT RUN | - |
| 2557 | dc2-spine1 | STUN | VerifyStunClient | Verifies the STUN client is configured with the specified IPv4 source address and port. Validate the public IP and port if provided. | - | NOT RUN | - |
| 2558 | dc2-spine1 | System | VerifyAgentLogs | Verifies there are no agent crash reports. | - | NOT RUN | - |
| 2559 | dc2-spine1 | System | VerifyCoredump | Verifies there are no core dump files. | - | NOT RUN | - |
| 2560 | dc2-spine1 | System | VerifyCPUUtilization | Verifies whether the CPU utilization is below 75%. | - | NOT RUN | - |
| 2561 | dc2-spine1 | System | VerifyFileSystemUtilization | Verifies that no partition is utilizing more than 75% of its disk space. | - | NOT RUN | - |
| 2562 | dc2-spine1 | System | VerifyMemoryUtilization | Verifies whether the memory utilization is below 75%. | - | NOT RUN | - |
| 2563 | dc2-spine1 | System | VerifyNTP | Verifies if NTP is synchronised. | - | NOT RUN | - |
| 2564 | dc2-spine1 | System | VerifyNTP | Verifies if NTP is synchronised. | - | NOT RUN | - |
| 2565 | dc2-spine1 | System | VerifyReloadCause | Verifies the last reload cause of the device. | - | NOT RUN | - |
| 2566 | dc2-spine1 | System | VerifyReloadCause | Verifies the last reload cause of the device. | - | NOT RUN | - |
| 2567 | dc2-spine1 | System | VerifyUptime | Verifies the device uptime. | - | NOT RUN | - |
| 2568 | dc2-spine1 | VLAN | VerifyVlanInternalPolicy | Verifies the VLAN internal allocation policy and the range of VLANs. | - | NOT RUN | - |
| 2569 | dc2-spine2 | AAA | VerifyAcctConsoleMethods | Verifies the AAA accounting console method lists for different accounting types (system, exec, commands, dot1x). | - | NOT RUN | - |
| 2570 | dc2-spine2 | AAA | VerifyAcctDefaultMethods | Verifies the AAA accounting default method lists for different accounting types (system, exec, commands, dot1x). | - | NOT RUN | - |
| 2571 | dc2-spine2 | AAA | VerifyAuthenMethods | Verifies the AAA authentication method lists for different authentication types (login, enable, dot1x). | - | NOT RUN | - |
| 2572 | dc2-spine2 | AAA | VerifyAuthzMethods | Verifies the AAA authorization method lists for different authorization types (commands, exec). | - | NOT RUN | - |
| 2573 | dc2-spine2 | AAA | VerifyTacacsServerGroups | Verifies if the provided TACACS server group(s) are configured. | - | NOT RUN | - |
| 2574 | dc2-spine2 | AAA | VerifyTacacsServers | Verifies TACACS servers are configured for a specified VRF. | - | NOT RUN | - |
| 2575 | dc2-spine2 | AAA | VerifyTacacsSourceIntf | Verifies TACACS source-interface for a specified VRF. | - | NOT RUN | - |
| 2576 | dc2-spine2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: dc2-leaf1a (IP: 10.255.128.13) | NOT RUN | - |
| 2577 | dc2-spine2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: dc2-leaf1b (IP: 10.255.128.14) | NOT RUN | - |
| 2578 | dc2-spine2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: dc2-leaf2a (IP: 10.255.128.15) | NOT RUN | - |
| 2579 | dc2-spine2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: dc2-leaf2b (IP: 10.255.128.16) | NOT RUN | - |
| 2580 | dc2-spine2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: dc2-leaf3a.arista.com (IP: 10.255.128.17) | NOT RUN | - |
| 2581 | dc2-spine2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP EVPN Peer: dc2-leaf3b.arista.com (IP: 10.255.128.18) | NOT RUN | - |
| 2582 | dc2-spine2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: dc2-leaf1a (IP: 10.255.255.107) | NOT RUN | - |
| 2583 | dc2-spine2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: dc2-leaf1b (IP: 10.255.255.111) | NOT RUN | - |
| 2584 | dc2-spine2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: dc2-leaf2a (IP: 10.255.255.115) | NOT RUN | - |
| 2585 | dc2-spine2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: dc2-leaf2b (IP: 10.255.255.119) | NOT RUN | - |
| 2586 | dc2-spine2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: dc2-leaf3a.arista.com (IP: 10.255.255.123) | NOT RUN | - |
| 2587 | dc2-spine2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s). | BGP IPv4 Unicast Peer: dc2-leaf3b.arista.com (IP: 10.255.255.127) | NOT RUN | - |
| 2588 | dc2-spine2 | Configuration | VerifyRunningConfigDiffs | Verifies there is no difference between the running-config and the startup-config | - | NOT RUN | - |
| 2589 | dc2-spine2 | Configuration | VerifyZeroTouch | Verifies ZeroTouch is disabled | - | NOT RUN | - |
| 2590 | dc2-spine2 | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet1 - Remote: dc2-leaf1a Ethernet2 | NOT RUN | - |
| 2591 | dc2-spine2 | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet2 - Remote: dc2-leaf1b Ethernet2 | NOT RUN | - |
| 2592 | dc2-spine2 | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet3 - Remote: dc2-leaf2a Ethernet2 | NOT RUN | - |
| 2593 | dc2-spine2 | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet4 - Remote: dc2-leaf2b Ethernet2 | NOT RUN | - |
| 2594 | dc2-spine2 | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet5 - Remote: dc2-leaf3a.arista.com Ethernet2 | NOT RUN | - |
| 2595 | dc2-spine2 | Connectivity | VerifyLLDPNeighbors | Verifies that the provided LLDP neighbors are connected properly. | Local: Ethernet6 - Remote: dc2-leaf3b.arista.com Ethernet2 | NOT RUN | - |
| 2596 | dc2-spine2 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet1 (IP: 10.255.255.106) - Destination: dc2-leaf1a Ethernet2 (IP: 10.255.255.107) | NOT RUN | - |
| 2597 | dc2-spine2 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet2 (IP: 10.255.255.110) - Destination: dc2-leaf1b Ethernet2 (IP: 10.255.255.111) | NOT RUN | - |
| 2598 | dc2-spine2 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet3 (IP: 10.255.255.114) - Destination: dc2-leaf2a Ethernet2 (IP: 10.255.255.115) | NOT RUN | - |
| 2599 | dc2-spine2 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet4 (IP: 10.255.255.118) - Destination: dc2-leaf2b Ethernet2 (IP: 10.255.255.119) | NOT RUN | - |
| 2600 | dc2-spine2 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet5 (IP: 10.255.255.122) - Destination: dc2-leaf3a.arista.com Ethernet2 (IP: 10.255.255.123) | NOT RUN | - |
| 2601 | dc2-spine2 | Connectivity | VerifyReachability | Test the network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet6 (IP: 10.255.255.126) - Destination: dc2-leaf3b.arista.com Ethernet2 (IP: 10.255.255.127) | NOT RUN | - |
| 2602 | dc2-spine2 | Field Notices | VerifyFieldNotice44Resolution | Verifies that the device is using the correct Aboot version per FN0044. | - | NOT RUN | - |
| 2603 | dc2-spine2 | Field Notices | VerifyFieldNotice72Resolution | Verifies if the device is exposed to FN0072, and if the issue has been mitigated. | - | NOT RUN | - |
| 2604 | dc2-spine2 | Greent | VerifyGreenT | Verifies if a GreenT policy is created. | - | NOT RUN | - |
| 2605 | dc2-spine2 | Greent | VerifyGreenTCounters | Verifies if the GreenT counters are incremented. | - | NOT RUN | - |
| 2606 | dc2-spine2 | Hardware | VerifyAdverseDrops | Verifies there are no adverse drops on DCS-7280 and DCS-7500 family switches. | - | NOT RUN | - |
| 2607 | dc2-spine2 | Hardware | VerifyEnvironmentCooling | Verifies the status of power supply fans and all fan trays. | - | NOT RUN | - |
| 2608 | dc2-spine2 | Hardware | VerifyEnvironmentCooling | Verifies the status of power supply fans and all fan trays. | Accepted States: 'ok' | NOT RUN | - |
| 2609 | dc2-spine2 | Hardware | VerifyEnvironmentPower | Verifies the power supplies status. | - | NOT RUN | - |
| 2610 | dc2-spine2 | Hardware | VerifyEnvironmentPower | Verifies the power supplies status. | Accepted States: 'ok' | NOT RUN | - |
| 2611 | dc2-spine2 | Hardware | VerifyEnvironmentSystemCooling | Verifies the system cooling status. | - | NOT RUN | - |
| 2612 | dc2-spine2 | Hardware | VerifyTemperature | Verifies the device temperature. | - | NOT RUN | - |
| 2613 | dc2-spine2 | Hardware | VerifyTemperature | Verifies the device temperature. | - | NOT RUN | - |
| 2614 | dc2-spine2 | Hardware | VerifyTransceiversManufacturers | Verifies if all transceivers come from approved manufacturers. | - | NOT RUN | - |
| 2615 | dc2-spine2 | Hardware | VerifyTransceiversManufacturers | Verifies if all transceivers come from approved manufacturers. | Accepted Manufacturers: 'Arista Networks', 'Arastra, Inc.', 'Not Present' | NOT RUN | - |
| 2616 | dc2-spine2 | Hardware | VerifyTransceiversTemperature | Verifies the transceivers temperature. | - | NOT RUN | - |
| 2617 | dc2-spine2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet1 - P2P_LINK_TO_DC2-LEAF1A_Ethernet2 = 'up' | NOT RUN | - |
| 2618 | dc2-spine2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet2 - P2P_LINK_TO_DC2-LEAF1B_Ethernet2 = 'up' | NOT RUN | - |
| 2619 | dc2-spine2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet3 - P2P_LINK_TO_DC2-LEAF2A_Ethernet2 = 'up' | NOT RUN | - |
| 2620 | dc2-spine2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet4 - P2P_LINK_TO_DC2-LEAF2B_Ethernet2 = 'up' | NOT RUN | - |
| 2621 | dc2-spine2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet5 - P2P_LINK_TO_DC2-LEAF3A.ARISTA.COM_Ethernet2 = 'up' | NOT RUN | - |
| 2622 | dc2-spine2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Ethernet6 - P2P_LINK_TO_DC2-LEAF3B.ARISTA.COM_Ethernet2 = 'up' | NOT RUN | - |
| 2623 | dc2-spine2 | Interfaces | VerifyInterfacesStatus | Verifies the status of the provided interfaces. | Interface Loopback0 - ROUTER_ID = 'up' | NOT RUN | - |
| 2624 | dc2-spine2 | LANZ | VerifyLANZ | Verifies if LANZ is enabled. | - | NOT RUN | - |
| 2625 | dc2-spine2 | PTP | VerifyPtpGMStatus | Verifies that the device is locked to a valid PTP Grandmaster. | - | NOT RUN | - |
| 2626 | dc2-spine2 | PTP | VerifyPtpLockStatus | Verifies that the device was locked to the upstream PTP GM in the last minute. | - | NOT RUN | - |
| 2627 | dc2-spine2 | PTP | VerifyPtpModeStatus | Verifies that the device is configured as a PTP Boundary Clock. | - | NOT RUN | - |
| 2628 | dc2-spine2 | PTP | VerifyPtpOffset | Verifies that the PTP timing offset is within +/- 1000ns from the master clock. | - | NOT RUN | - |
| 2629 | dc2-spine2 | PTP | VerifyPtpPortModeStatus | Verifies the PTP interfaces state. | - | NOT RUN | - |
| 2630 | dc2-spine2 | Routing | VerifyRoutingProtocolModel | Verifies the configured routing protocol model. | Routing protocol model: multi-agent | NOT RUN | - |
| 2631 | dc2-spine2 | Security | VerifyAPIHttpsSSL | Verifies if the eAPI has a valid SSL profile. | - | NOT RUN | - |
| 2632 | dc2-spine2 | Security | VerifyAPIHttpsSSL | Verifies if the eAPI has a valid SSL profile. | eAPI HTTPS SSL Profile: eAPI_SSL_Profile | NOT RUN | - |
| 2633 | dc2-spine2 | Security | VerifyAPIHttpStatus | Verifies if eAPI HTTP server is disabled globally. | - | NOT RUN | - |
| 2634 | dc2-spine2 | Security | VerifyAPIIPv4Acl | Verifies if eAPI has the right number IPv4 ACL(s) configured for a specified VRF. | - | NOT RUN | - |
| 2635 | dc2-spine2 | Security | VerifyAPIIPv6Acl | Verifies if eAPI has the right number IPv6 ACL(s) configured for a specified VRF. | - | NOT RUN | - |
| 2636 | dc2-spine2 | Security | VerifyAPISSLCertificate | Verifies the eAPI SSL certificate expiry, common subject name, encryption algorithm and key size. | - | NOT RUN | - |
| 2637 | dc2-spine2 | Security | VerifyBannerLogin | Verifies the login banner of a device. | - | NOT RUN | - |
| 2638 | dc2-spine2 | Security | VerifyBannerMotd | Verifies the motd banner of a device. | - | NOT RUN | - |
| 2639 | dc2-spine2 | Security | VerifyIPSecConnHealth | Verifies all IPv4 security connections. | - | NOT RUN | - |
| 2640 | dc2-spine2 | Security | VerifyIPv4ACL | Verifies the configuration of IPv4 ACLs. | - | NOT RUN | - |
| 2641 | dc2-spine2 | Security | VerifySpecificIPSecConn | Verifies IPv4 security connections for a peer. | - | NOT RUN | - |
| 2642 | dc2-spine2 | Security | VerifySSHIPv4Acl | Verifies if the SSHD agent has IPv4 ACL(s) configured. | - | NOT RUN | - |
| 2643 | dc2-spine2 | Security | VerifySSHIPv6Acl | Verifies if the SSHD agent has IPv6 ACL(s) configured. | - | NOT RUN | - |
| 2644 | dc2-spine2 | Security | VerifySSHStatus | Verifies if the SSHD agent is disabled in the default VRF. | - | NOT RUN | - |
| 2645 | dc2-spine2 | Security | VerifyTelnetStatus | Verifies if Telnet is disabled in the default VRF. | - | NOT RUN | - |
| 2646 | dc2-spine2 | Services | VerifyDNSLookup | Verifies the DNS name to IP address resolution. | - | NOT RUN | - |
| 2647 | dc2-spine2 | Services | VerifyDNSServers | Verifies if the DNS servers are correctly configured. | - | NOT RUN | - |
| 2648 | dc2-spine2 | Services | VerifyErrdisableRecovery | Verifies the errdisable recovery reason, status, and interval. | - | NOT RUN | - |
| 2649 | dc2-spine2 | Services | VerifyHostname | Verifies the hostname of a device. | - | NOT RUN | - |
| 2650 | dc2-spine2 | SNMP | VerifySnmpIPv4Acl | Verifies if the SNMP agent has IPv4 ACL(s) configured. | - | NOT RUN | - |
| 2651 | dc2-spine2 | SNMP | VerifySnmpIPv6Acl | Verifies if the SNMP agent has IPv6 ACL(s) configured. | - | NOT RUN | - |
| 2652 | dc2-spine2 | SNMP | VerifySnmpStatus | Verifies if the SNMP agent is enabled. | - | NOT RUN | - |
| 2653 | dc2-spine2 | Software | VerifyEOSVersion | Verifies the EOS version of the device. | - | NOT RUN | - |
| 2654 | dc2-spine2 | Software | VerifyTerminAttrVersion | Verifies the TerminAttr version of the device. | - | NOT RUN | - |
| 2655 | dc2-spine2 | STUN | VerifyStunClient | Verifies the STUN client is configured with the specified IPv4 source address and port. Validate the public IP and port if provided. | - | NOT RUN | - |
| 2656 | dc2-spine2 | System | VerifyAgentLogs | Verifies there are no agent crash reports. | - | NOT RUN | - |
| 2657 | dc2-spine2 | System | VerifyCoredump | Verifies there are no core dump files. | - | NOT RUN | - |
| 2658 | dc2-spine2 | System | VerifyCPUUtilization | Verifies whether the CPU utilization is below 75%. | - | NOT RUN | - |
| 2659 | dc2-spine2 | System | VerifyFileSystemUtilization | Verifies that no partition is utilizing more than 75% of its disk space. | - | NOT RUN | - |
| 2660 | dc2-spine2 | System | VerifyMemoryUtilization | Verifies whether the memory utilization is below 75%. | - | NOT RUN | - |
| 2661 | dc2-spine2 | System | VerifyNTP | Verifies if NTP is synchronised. | - | NOT RUN | - |
| 2662 | dc2-spine2 | System | VerifyNTP | Verifies if NTP is synchronised. | - | NOT RUN | - |
| 2663 | dc2-spine2 | System | VerifyReloadCause | Verifies the last reload cause of the device. | - | NOT RUN | - |
| 2664 | dc2-spine2 | System | VerifyReloadCause | Verifies the last reload cause of the device. | - | NOT RUN | - |
| 2665 | dc2-spine2 | System | VerifyUptime | Verifies the device uptime. | - | NOT RUN | - |
| 2666 | dc2-spine2 | VLAN | VerifyVlanInternalPolicy | Verifies the VLAN internal allocation policy and the range of VLANs. | - | NOT RUN | - |
