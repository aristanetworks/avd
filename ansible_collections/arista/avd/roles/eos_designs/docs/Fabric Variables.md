---
search:
  boost: 2
---

# Fabric Variables

## BFD Settings

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>bfd_multihop</samp>](## "bfd_multihop") | Dictionary |  |  |  | BFD Multihop tuning |
    | [<samp>&nbsp;&nbsp;interval</samp>](## "bfd_multihop.interval") | Integer |  | 300 | Min: 50<br>Max: 60000 |  |
    | [<samp>&nbsp;&nbsp;min_rx</samp>](## "bfd_multihop.min_rx") | Integer |  | 300 | Min: 50<br>Max: 60000 |  |
    | [<samp>&nbsp;&nbsp;multiplier</samp>](## "bfd_multihop.multiplier") | Integer |  | 3 | Min: 3<br>Max: 50 |  |

=== "YAML"

    ```yaml
    bfd_multihop:
      interval: <int>
      min_rx: <int>
      multiplier: <int>
    ```

## BGP multi-path Settings

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>bgp_ecmp</samp>](## "bgp_ecmp") | Integer |  | 4 |  | Maximum ECMP for BGP multi-path |
    | [<samp>bgp_maximum_paths</samp>](## "bgp_maximum_paths") | Integer |  | 4 | Min: 1<br>Max: 512 | Maximum Paths for BGP multi-path |

=== "YAML"

    ```yaml
    bgp_ecmp: <int>
    bgp_maximum_paths: <int>
    ```

## BGP Peer Groups

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>bgp_peer_groups</samp>](## "bgp_peer_groups") | Dictionary |  |  |  | Leverage an Arista EOS switch to generate the encrypted password using the correct peer group name.<br>Note that the name of the peer groups use '-' instead of '_' in EOS configuration.<br> |
    | [<samp>&nbsp;&nbsp;ipv4_underlay_peers</samp>](## "bgp_peer_groups.ipv4_underlay_peers") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "bgp_peer_groups.ipv4_underlay_peers.name") | String |  | IPv4-UNDERLAY-PEERS |  | Name of peer group. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;password</samp>](## "bgp_peer_groups.ipv4_underlay_peers.password") | String |  |  |  | Type 7 encrypted password. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "bgp_peer_groups.ipv4_underlay_peers.structured_config") | Dictionary |  |  |  | Custom structured config added under router_bgp.peer_groups.<name> for eos_cli_config_gen |
    | [<samp>&nbsp;&nbsp;mlag_ipv4_underlay_peer</samp>](## "bgp_peer_groups.mlag_ipv4_underlay_peer") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "bgp_peer_groups.mlag_ipv4_underlay_peer.name") | String |  | MLAG-IPv4-UNDERLAY-PEER |  | Name of peer group. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;password</samp>](## "bgp_peer_groups.mlag_ipv4_underlay_peer.password") | String |  |  |  | Type 7 encrypted password. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "bgp_peer_groups.mlag_ipv4_underlay_peer.structured_config") | Dictionary |  |  |  | Custom structured config added under router_bgp.peer_groups.<name> for eos_cli_config_gen |
    | [<samp>&nbsp;&nbsp;evpn_overlay_peers</samp>](## "bgp_peer_groups.evpn_overlay_peers") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "bgp_peer_groups.evpn_overlay_peers.name") | String |  | EVPN-OVERLAY-PEERS |  | Name of peer group. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;password</samp>](## "bgp_peer_groups.evpn_overlay_peers.password") | String |  |  |  | Type 7 encrypted password. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "bgp_peer_groups.evpn_overlay_peers.structured_config") | Dictionary |  |  |  | Custom structured config added under router_bgp.peer_groups.<name> for eos_cli_config_gen |
    | [<samp>&nbsp;&nbsp;evpn_overlay_core</samp>](## "bgp_peer_groups.evpn_overlay_core") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "bgp_peer_groups.evpn_overlay_core.name") | String |  | EVPN-OVERLAY-CORE |  | Name of peer group. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;password</samp>](## "bgp_peer_groups.evpn_overlay_core.password") | String |  |  |  | Type 7 encrypted password. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "bgp_peer_groups.evpn_overlay_core.structured_config") | Dictionary |  |  |  | Custom structured config added under router_bgp.peer_groups.<name> for eos_cli_config_gen |
    | [<samp>&nbsp;&nbsp;mpls_overlay_peers</samp>](## "bgp_peer_groups.mpls_overlay_peers") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "bgp_peer_groups.mpls_overlay_peers.name") | String |  | MPLS-OVERLAY-PEERS |  | Name of peer group. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;password</samp>](## "bgp_peer_groups.mpls_overlay_peers.password") | String |  |  |  | Type 7 encrypted password. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "bgp_peer_groups.mpls_overlay_peers.structured_config") | Dictionary |  |  |  | Custom structured config added under router_bgp.peer_groups.<name> for eos_cli_config_gen |
    | [<samp>&nbsp;&nbsp;rr_overlay_peers</samp>](## "bgp_peer_groups.rr_overlay_peers") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "bgp_peer_groups.rr_overlay_peers.name") | String |  | RR-OVERLAY-PEERS |  | Name of peer group. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;password</samp>](## "bgp_peer_groups.rr_overlay_peers.password") | String |  |  |  | Type 7 encrypted password. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "bgp_peer_groups.rr_overlay_peers.structured_config") | Dictionary |  |  |  | Custom structured config added under router_bgp.peer_groups.<name> for eos_cli_config_gen |
    | [<samp>&nbsp;&nbsp;ipvpn_gateway_peers</samp>](## "bgp_peer_groups.ipvpn_gateway_peers") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "bgp_peer_groups.ipvpn_gateway_peers.name") | String |  | IPVPN-GATEWAY-PEERS |  | Name of peer group. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;password</samp>](## "bgp_peer_groups.ipvpn_gateway_peers.password") | String |  |  |  | Type 7 encrypted password. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "bgp_peer_groups.ipvpn_gateway_peers.structured_config") | Dictionary |  |  |  | Custom structured config added under router_bgp.peer_groups.<name> for eos_cli_config_gen |
    | [<samp>&nbsp;&nbsp;IPv4_UNDERLAY_PEERS</samp>](## "bgp_peer_groups.IPv4_UNDERLAY_PEERS") <span style="color:red">removed</span> | Dictionary |  |  |  | <span style="color:red">This key was removed. Support was removed in AVD version 4.0.0. Use <samp>bgp_peer_groups.ipv4_underlay_peers</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;MLAG_IPv4_UNDERLAY_PEER</samp>](## "bgp_peer_groups.MLAG_IPv4_UNDERLAY_PEER") <span style="color:red">removed</span> | Dictionary |  |  |  | <span style="color:red">This key was removed. Support was removed in AVD version 4.0.0. Use <samp>bgp_peer_groups.mlag_ipv4_underlay_peer</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;EVPN_OVERLAY_PEERS</samp>](## "bgp_peer_groups.EVPN_OVERLAY_PEERS") <span style="color:red">removed</span> | Dictionary |  |  |  | <span style="color:red">This key was removed. Support was removed in AVD version 4.0.0. Use <samp>bgp_peer_groups.evpn_overlay_peers</samp> instead.</span> |

=== "YAML"

    ```yaml
    bgp_peer_groups:
      ipv4_underlay_peers:
        name: <str>
        password: <str>
        structured_config: <dict>
      mlag_ipv4_underlay_peer:
        name: <str>
        password: <str>
        structured_config: <dict>
      evpn_overlay_peers:
        name: <str>
        password: <str>
        structured_config: <dict>
      evpn_overlay_core:
        name: <str>
        password: <str>
        structured_config: <dict>
      mpls_overlay_peers:
        name: <str>
        password: <str>
        structured_config: <dict>
      rr_overlay_peers:
        name: <str>
        password: <str>
        structured_config: <dict>
      ipvpn_gateway_peers:
        name: <str>
        password: <str>
        structured_config: <dict>
      IPv4_UNDERLAY_PEERS: <dict>
      MLAG_IPv4_UNDERLAY_PEER: <dict>
      EVPN_OVERLAY_PEERS: <dict>
    ```

## BGP Settings

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>bgp_as</samp>](## "bgp_as") | String |  |  |  | AS number to use to configure overlay when "overlay_routing_protocol" == ibgp |
    | [<samp>bgp_default_ipv4_unicast</samp>](## "bgp_default_ipv4_unicast") | Boolean |  | False |  | Default activation of IPv4 unicast address-family on all IPv4 neighbors.<br>It is best practice to disable activation.<br> |
    | [<samp>bgp_graceful_restart</samp>](## "bgp_graceful_restart") | Dictionary |  |  |  | Graceful BGP restart allows a BGP speaker with separate control plane and data plane processing to continue forwarding traffic during a BGP restart.<br>Its neighbors (receiving speakers) may retain routing information from the restarting speaker while a BGP session with it is being re-established, reducing route flapping.<br> |
    | [<samp>&nbsp;&nbsp;enabled</samp>](## "bgp_graceful_restart.enabled") | Boolean |  | True |  | Enable or disable graceful restart helper mode for all BGP peers. |
    | [<samp>&nbsp;&nbsp;restart_time</samp>](## "bgp_graceful_restart.restart_time") | Integer |  | 300 | Min: 1<br>Max: 3600 | Restart time in seconds. |
    | [<samp>bgp_mesh_pes</samp>](## "bgp_mesh_pes") | Boolean |  | False |  | Whether to configure an iBGP full mesh between PEs, either because there is no RR used or other reasons. |
    | [<samp>underlay_filter_peer_as</samp>](## "underlay_filter_peer_as") | Boolean |  | False |  | Configure route-map on eBGP sessions towards underlay peers, where prefixes with the peer's ASN in the AS Path are filtered away.<br>This is very useful in very large scale networks not using EVPN overlays, where convergence will be quicker by not having to return<br>all updates received from Spine-1 to Spine-2 just for Spine-2 to throw them away because of AS Path loop detection.<br>Note this key is ignored when EVPN is configured.<br> |

=== "YAML"

    ```yaml
    bgp_as: <str>
    bgp_default_ipv4_unicast: <bool>
    bgp_graceful_restart:
      enabled: <bool>
      restart_time: <int>
    bgp_mesh_pes: <bool>
    underlay_filter_peer_as: <bool>
    ```

## EVPN Settings

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>evpn_ebgp_gateway_multihop</samp>](## "evpn_ebgp_gateway_multihop") | Integer |  | 15 |  | Default of 15, considering a large value to avoid BGP reachability issues in very complex DCI networks.<br>Adapt the value for your specific topology.<br> |
    | [<samp>evpn_ebgp_multihop</samp>](## "evpn_ebgp_multihop") | Integer |  | 3 |  | Default of 3, the recommended value for a 3 stage spine and leaf topology.<br>Set to a higher value to allow for very large and complex topologies.<br> |
    | [<samp>evpn_hostflap_detection</samp>](## "evpn_hostflap_detection") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;enabled</samp>](## "evpn_hostflap_detection.enabled") | Boolean |  | True |  | If set to false it will disable EVPN host-flap detection |
    | [<samp>&nbsp;&nbsp;threshold</samp>](## "evpn_hostflap_detection.threshold") | Integer |  | 5 |  | Minimum number of MAC moves that indicate a MAC duplication issue |
    | [<samp>&nbsp;&nbsp;window</samp>](## "evpn_hostflap_detection.window") | Integer |  | 180 |  | Time (in seconds) to detect a MAC duplication issue |
    | [<samp>&nbsp;&nbsp;expiry_timeout</samp>](## "evpn_hostflap_detection.expiry_timeout") | Integer |  |  |  | Time (in seconds) to purge a MAC duplication issue |
    | [<samp>evpn_import_pruning</samp>](## "evpn_import_pruning") | Boolean |  | False |  | Enable VPN import pruning (Min. EOS 4.24.2F)<br>The Route Target extended communities carried by incoming VPN paths will<br>be examined. If none of those Route Targets have been configured for import,<br>the path will be immediately discarded<br> |
    | [<samp>evpn_multicast</samp>](## "evpn_multicast") | Boolean |  | False |  | General Configuration required for EVPN Multicast. "evpn_l2_multicast" must also be configured under the Network Services (tenants).<br>Requires "underlay_multicast: true" and IGMP snooping enabled globally (default).<br>For MLAG devices Route Distinguisher must be unique since this feature will create multi-vtep configuration.<br>Warning !!! For Trident3 based platforms i.e 7050X3, 7300X3, 720XP and 722XP<br>  The Following default platform setting will be configured: "platform trident forwarding-table partition flexible exact-match 16384 l2-shared 98304 l3-shared 131072"<br>  All forwarding agents will be restarted when this configuration is applied.<br>  You can tune the settings by overridding the default variable: "platform_settings[platforms].trident_forwarding_table_partition:"<br>  Please contact an Arista representative for help with determining the appropriate values for your environment.<br> |
    | [<samp>evpn_overlay_bgp_rtc</samp>](## "evpn_overlay_bgp_rtc") | Boolean |  | False |  | Enable Route Target Membership Constraint Address Family on EVPN overlay BGP peerings (Min. EOS 4.25.1F)<br>Requires use eBGP as overlay protocol.<br> |
    | [<samp>evpn_prevent_readvertise_to_server</samp>](## "evpn_prevent_readvertise_to_server") | Boolean |  | False |  | Configure route-map on eBGP sessions towards route-servers, where prefixes with the peer's ASN in the AS Path are filtered away.<br>This is very useful in large-scale networks, where convergence will be quicker by not returning all updates received<br>from Route-server-1 to Router-server-2 just for Route-server-2 to throw them away because of AS Path loop detection.<br> |
    | [<samp>evpn_short_esi_prefix</samp>](## "evpn_short_esi_prefix") | String |  | 0000:0000: |  | Configure prefix for "short_esi" values |
    | [<samp>evpn_vlan_aware_bundles</samp>](## "evpn_vlan_aware_bundles") | Boolean |  | False |  | Enable vlan aware bundles for EVPN MAC-VRF<br>Old variable name vxlan_vlan_aware_bundles, supported for backward-compatibility.<br> |

=== "YAML"

    ```yaml
    evpn_ebgp_gateway_multihop: <int>
    evpn_ebgp_multihop: <int>
    evpn_hostflap_detection:
      enabled: <bool>
      threshold: <int>
      window: <int>
      expiry_timeout: <int>
    evpn_import_pruning: <bool>
    evpn_multicast: <bool>
    evpn_overlay_bgp_rtc: <bool>
    evpn_prevent_readvertise_to_server: <bool>
    evpn_short_esi_prefix: <str>
    evpn_vlan_aware_bundles: <bool>
    ```

## IPv6 Underlay Settings

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>overlay_mlag_rfc5549</samp>](## "overlay_mlag_rfc5549") | Boolean |  | False |  | IPv6 Unnumbered for MLAG iBGP connections.<br>Requires "underlay_rfc5549: true".<br> |
    | [<samp>overlay_routing_protocol_address_family</samp>](## "overlay_routing_protocol_address_family") | String |  | ipv4 | Valid Values:<br>- ipv4<br>- ipv6 | When set to `ipv6`, enable overlay EVPN peering with IPv6 addresses.<br>This feature depends on underlay_ipv6 variable. As of today, only RFC5549 is capable to transport IPv6 in the underlay.<br> |
    | [<samp>underlay_ipv6</samp>](## "underlay_ipv6") | Boolean |  | False |  | This feature allows IPv6 underlay routing protocol with RFC5549 addresses to be used along with IPv4 advertisements as VXLAN tunnel endpoints.<br>Requires "underlay_rfc5549: true" and "loopback_ipv6_pool" under the "Fabric Topology"<br> |
    | [<samp>underlay_rfc5549</samp>](## "underlay_rfc5549") | Boolean |  | False |  | Point to Point Underlay with RFC 5549(eBGP), i.e. IPv6 Unnumbered<br>Requires "underlay_routing_protocol: ebgp"<br> |

=== "YAML"

    ```yaml
    overlay_mlag_rfc5549: <bool>
    overlay_routing_protocol_address_family: <str>
    underlay_ipv6: <bool>
    underlay_rfc5549: <bool>
    ```

## ISIS Settings

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>isis_advertise_passive_only</samp>](## "isis_advertise_passive_only") | Boolean |  | False |  |  |
    | [<samp>isis_area_id</samp>](## "isis_area_id") | String |  | 49.0001 |  |  |
    | [<samp>isis_default_circuit_type</samp>](## "isis_default_circuit_type") | String |  | level-2 | Valid Values:<br>- level-1-2<br>- level-1<br>- level-2 | These fabric level parameters can be used with core_interfaces running ISIS, and may be overridden on link profile or link level. |
    | [<samp>isis_default_is_type</samp>](## "isis_default_is_type") | String |  | level-2 | Valid Values:<br>- level-1-2<br>- level-1<br>- level-2 |  |
    | [<samp>isis_default_metric</samp>](## "isis_default_metric") | Integer |  | 50 |  | These fabric level parameters can be used with core_interfaces running ISIS, and may be overridden at link profile or link level. |
    | [<samp>isis_ti_lfa</samp>](## "isis_ti_lfa") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;enabled</samp>](## "isis_ti_lfa.enabled") | Boolean |  | False |  |  |
    | [<samp>&nbsp;&nbsp;protection</samp>](## "isis_ti_lfa.protection") | String |  |  | Valid Values:<br>- link<br>- node |  |
    | [<samp>&nbsp;&nbsp;local_convergence_delay</samp>](## "isis_ti_lfa.local_convergence_delay") | Integer |  | 10000 |  | Local convergence delay in milliseconds |
    | [<samp>underlay_isis_instance_name</samp>](## "underlay_isis_instance_name") | String |  |  |  | Default -> "EVPN_UNDERLAY" for l3ls, "CORE" for mpls |

=== "YAML"

    ```yaml
    isis_advertise_passive_only: <bool>
    isis_area_id: <str>
    isis_default_circuit_type: <str>
    isis_default_is_type: <str>
    isis_default_metric: <int>
    isis_ti_lfa:
      enabled: <bool>
      protection: <str>
      local_convergence_delay: <int>
    underlay_isis_instance_name: <str>
    ```

## MAC Address Table Settings

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>mac_address_table</samp>](## "mac_address_table") | Dictionary |  |  |  | MAC address-table aging time<br>Use to change the EOS default of 300.<br> |
    | [<samp>&nbsp;&nbsp;aging_time</samp>](## "mac_address_table.aging_time") | Integer |  |  | Min: 0<br>Max: 1000000 | Aging time in seconds 10-1000000.<br>Enter 0 to disable aging.<br> |

=== "YAML"

    ```yaml
    mac_address_table:
      aging_time: <int>
    ```

## MLAG Settings

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>mlag_ibgp_peering_vrfs</samp>](## "mlag_ibgp_peering_vrfs") | Dictionary |  |  |  | On mlag leafs, an SVI interface is defined per vrf, to establish iBGP peering (required when there are MLAG leafs in topology)<br>The SVI id will be derived from the base vlan defined: mlag_ibgp_peering_vrfs.base_vlan + (vrf_id or vrf_vni) - 1<br>Depending on the values of vrf_id / vrf_vni it may be required to adjust the base_vlan to avoid overlaps or invalid vlan ids.<br>The SVI ip address derived from mlag_l3_peer_ipv4_pool is re-used across all iBGP peerings.<br> |
    | [<samp>&nbsp;&nbsp;base_vlan</samp>](## "mlag_ibgp_peering_vrfs.base_vlan") | Integer |  | 3000 | Min: 1<br>Max: 4093 |  |

=== "YAML"

    ```yaml
    mlag_ibgp_peering_vrfs:
      base_vlan: <int>
    ```

## Multicast Settings

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>default_igmp_snooping_enabled</samp>](## "default_igmp_snooping_enabled") | Boolean |  | True |  | When set to false, disables IGMP snooping at fabric level and overrides per vlan settings.<br> |
    | [<samp>underlay_multicast</samp>](## "underlay_multicast") | Boolean |  | False |  | Enable Multicast in the underlay on all p2p uplink interfaces and mlag l3 peer interface.<br>Specifically PIM Sparse-Mode will be configured on all routed underlay interfaces.<br>No other configuration is added, so the underlay will only support Source-Specific Multicast (SSM)<br>The configuration is intended to be used as multicast underlay for EVPN OISM overlay<br> |

=== "YAML"

    ```yaml
    default_igmp_snooping_enabled: <bool>
    underlay_multicast: <bool>
    ```

## OSPF Settings

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>underlay_ospf_area</samp>](## "underlay_ospf_area") | String |  | 0.0.0.0 | Format: ipv4 |  |
    | [<samp>underlay_ospf_bfd_enable</samp>](## "underlay_ospf_bfd_enable") | Boolean |  | False |  |  |
    | [<samp>underlay_ospf_max_lsa</samp>](## "underlay_ospf_max_lsa") | Integer |  | 12000 |  |  |
    | [<samp>underlay_ospf_process_id</samp>](## "underlay_ospf_process_id") | Integer |  | 100 |  |  |

=== "YAML"

    ```yaml
    underlay_ospf_area: <str>
    underlay_ospf_bfd_enable: <bool>
    underlay_ospf_max_lsa: <int>
    underlay_ospf_process_id: <int>
    ```

## Overlay General Settings

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>overlay_loopback_description</samp>](## "overlay_loopback_description") | String |  |  |  | Customize the description on overlay interface Loopback0. |
    | [<samp>vtep_vvtep_ip</samp>](## "vtep_vvtep_ip") | String |  |  |  | IP Address used as Virtual VTEP. Will be configured as secondary IP on Loopback1.<br>This is only needed for centralized routing designs.<br> |

=== "YAML"

    ```yaml
    overlay_loopback_description: <str>
    vtep_vvtep_ip: <str>
    ```

## PTP Profiles

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>ptp_profiles</samp>](## "ptp_profiles") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;- profile</samp>](## "ptp_profiles.[].profile") | String |  |  |  | PTP profile. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;announce</samp>](## "ptp_profiles.[].announce") | Dictionary |  |  |  | PTP announce interval. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interval</samp>](## "ptp_profiles.[].announce.interval") | Integer |  |  | Min: -7<br>Max: 4 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;timeout</samp>](## "ptp_profiles.[].announce.timeout") | Integer |  |  | Min: 2<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;delay_req</samp>](## "ptp_profiles.[].delay_req") | Integer |  |  | Min: -7<br>Max: 8 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;sync_message</samp>](## "ptp_profiles.[].sync_message") | Dictionary |  |  |  | PTP sync message interval. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interval</samp>](## "ptp_profiles.[].sync_message.interval") | Integer |  |  | Min: -7<br>Max: 3 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;transport</samp>](## "ptp_profiles.[].transport") | String |  |  | Valid Values:<br>- ipv4 |  |

=== "YAML"

    ```yaml
    ptp_profiles:
      - profile: <str>
        announce:
          interval: <int>
          timeout: <int>
        delay_req: <int>
        sync_message:
          interval: <int>
        transport: <str>
    ```

## Routing Protocol Selection

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>overlay_her_flood_list_per_vni</samp>](## "overlay_her_flood_list_per_vni") | Boolean |  | False |  | When using Head-End Replication, configure flood-lists per VNI.<br>By default HER will be configured with a common flood-list containing all VTEPs.<br>This behavior can be changed to per-VNI flood-lists by setting `overlay_her_flood_list_per_vni: true`.<br>This will make `eos_designs` consider configured VLANs per VTEP, and only include the relevant VTEPs to each VNI's flood-list.<br> |
    | [<samp>overlay_her_flood_list_scope</samp>](## "overlay_her_flood_list_scope") | String |  | fabric | Valid Values:<br>- fabric<br>- dc | When using Head-End Replication, set the scope of flood-lists to Fabric or DC.<br>By default all VTEPs in the Fabric (part of the inventory group referenced by "fabric_name") are added to the flood-lists.<br>This can be changed to all VTEPs in the DC (part of the inventory group referenced by "dc_name").<br>This is useful if Border Leaf switches are dividing the VXLAN overlay into separate domains.<br> |
    | [<samp>overlay_routing_protocol</samp>](## "overlay_routing_protocol") | String |  | ebgp | Value is converted to lower case<br>Valid Values:<br>- ebgp<br>- ibgp<br>- cvx<br>- her<br>- none | - The following overlay routing protocols are supported:<br>  - eBGP: Configures fabric with eBGP, default for l3ls-evpn design.<br>  - iBGP: Configured fabric with iBGP, only supported with OSPF or ISIS variants in underlay, default for mpls design.<br>  - CVX: Configures fabric to leverage CloudVision eXchange as the overlay controller.<br>  - HER: Configures fabric with Head-End Replication, configures static VXLAN flood-lists instead of using a dynamic overlay protocol.<br>  - none: No overlay configuration will be generated, default for l2ls design.<br> |
    | [<samp>underlay_routing_protocol</samp>](## "underlay_routing_protocol") | String |  |  | Value is converted to lower case<br>Valid Values:<br>- ebgp<br>- ospf<br>- isis<br>- isis-sr<br>- isis-ldp<br>- isis-sr-ldp<br>- ospf-ldp | - The following underlay routing protocols are supported:<br>  - EBGP (default for l3ls-evpn)<br>  - OSPF.<br>  - ISIS.<br>  - ISIS-SR*.<br>  - ISIS-LDP*.<br>  - ISIS-SR-LDP*.<br>  - OSPF-LDP*.<br>- The variables should be applied to all devices in the fabric.<br>*Only supported with core_interfaces data model.<br> |

=== "YAML"

    ```yaml
    overlay_her_flood_list_per_vni: <bool>
    overlay_her_flood_list_scope: <str>
    overlay_routing_protocol: <str>
    underlay_routing_protocol: <str>
    ```

## Uplink Settings

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>shutdown_interfaces_towards_undeployed_peers</samp>](## "shutdown_interfaces_towards_undeployed_peers") | Boolean |  | False |  | - It is possible to provision configurations for a complete topology but flag devices as undeployed using the host level variable `is_deployed: false`.<br><br>```yaml<br># Use at the host level<br>is_deployed: < true or false or default -> true ><br>```<br><br>- By default, this will have no impact within the `eos_designs` role. Configs will still be generated by the `eos_cli_config_gen` role and will still be pushed by the `eos_config_deploy_eapi` directly to devices if used.<br>- However, if the `eos_config_deploy_cvp` role is used to push configurations, CloudVision will ignore the devices flagged  as `is_deployed: false` and not attempt to configure them.<br>- If the device is not present in the network due to CloudVision not configuring the device, `eos_validate_state` role will fail tests on peers of the undeployed device trying to verify that interfaces are up.<br>- To overcome this and shutdown interfaces towards undeployed peers, the variable `shutdown_interfaces_towards_undeployed_peers` can be used, satisfying the `eos_validate_state` role interface tests.<br>- Again, this is only an issue if `eos_config_deploy_cvp` is used and the devices are not present in the network. |

=== "YAML"

    ```yaml
    shutdown_interfaces_towards_undeployed_peers: <bool>
    ```

## Uplinks Settings

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>p2p_uplinks_mtu</samp>](## "p2p_uplinks_mtu") | Integer |  | 9214 | Min: 68<br>Max: 65535 | Point to Point Links MTU |
    | [<samp>p2p_uplinks_qos_profile</samp>](## "p2p_uplinks_qos_profile") | String |  |  |  | QOS Profile assigned on all infrastructure links |
    | [<samp>uplink_ptp</samp>](## "uplink_ptp") | Dictionary |  |  |  | Enable PTP on all infrastructure links |
    | [<samp>&nbsp;&nbsp;enable</samp>](## "uplink_ptp.enable") | Boolean |  | False |  |  |

=== "YAML"

    ```yaml
    p2p_uplinks_mtu: <int>
    p2p_uplinks_qos_profile: <str>
    uplink_ptp:
      enable: <bool>
    ```

## VLAN Settings

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>enable_trunk_groups</samp>](## "enable_trunk_groups") | Boolean |  | False |  | Enable Trunk Group support across eos_designs<br>Warning: Because of the nature of the EOS Trunk Group feature, enabling this is "all or nothing".<br>*All* vlans and *all* trunks towards connected endpoints must be using trunk groups as well.<br>If trunk groups are not assigned to a trunk, no vlans will be enabled on that trunk.<br>See "Details on enable_trunk_groups" below before enabling this feature.<br> |
    | [<samp>internal_vlan_order</samp>](## "internal_vlan_order") | Dictionary |  |  |  | Internal vlan allocation order and range. |
    | [<samp>&nbsp;&nbsp;allocation</samp>](## "internal_vlan_order.allocation") | String | Required | ascending | Valid Values:<br>- ascending<br>- descending |  |
    | [<samp>&nbsp;&nbsp;range</samp>](## "internal_vlan_order.range") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;beginning</samp>](## "internal_vlan_order.range.beginning") | Integer | Required | 1006 | Min: 2<br>Max: 4094 | First VLAN ID. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ending</samp>](## "internal_vlan_order.range.ending") | Integer | Required | 1199 | Min: 2<br>Max: 4094 | Last VLAN ID. |
    | [<samp>only_local_vlan_trunk_groups</samp>](## "only_local_vlan_trunk_groups") | Boolean |  | False |  | A vlan can have many trunk_groups assigned. To avoid unneeded configuration changes on all leaf<br>switches when a new trunk group is added, this feature will only configure the vlan trunk groups<br>matched with local connected_endpoints.<br>See "Details on only_local_vlan_trunk_groups" below.<br>Requires "enable_trunk_groups: true"<br> |
    | [<samp>trunk_groups</samp>](## "trunk_groups") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;mlag</samp>](## "trunk_groups.mlag") | Dictionary |  |  |  | Trunk Group used for MLAG VLAN (Typically VLAN 4094)<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "trunk_groups.mlag.name") | String |  | MLAG |  |  |
    | [<samp>&nbsp;&nbsp;mlag_l3</samp>](## "trunk_groups.mlag_l3") | Dictionary |  |  |  | Trunk Group used for MLAG L3 peering VLAN and for VRF L3 peering VLANs (Typically VLAN 4093)<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "trunk_groups.mlag_l3.name") | String |  | LEAF_PEER_L3 |  |  |
    | [<samp>&nbsp;&nbsp;uplink</samp>](## "trunk_groups.uplink") | Dictionary |  |  |  | Trunk Group used on L2 Leaf switches when "enable_trunk_groups" is set<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "trunk_groups.uplink.name") | String |  | UPLINK |  |  |

=== "YAML"

    ```yaml
    enable_trunk_groups: <bool>
    internal_vlan_order:
      allocation: <str>
      range:
        beginning: <int>
        ending: <int>
    only_local_vlan_trunk_groups: <bool>
    trunk_groups:
      mlag:
        name: <str>
      mlag_l3:
        name: <str>
      uplink:
        name: <str>
    ```
