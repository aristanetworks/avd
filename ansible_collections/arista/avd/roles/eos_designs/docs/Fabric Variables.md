---
search:
  boost: 2
---

# Fabric Variables

## Bgp Settings

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>underlay_filter_peer_as</samp>](## "underlay_filter_peer_as") | Boolean |  | False |  | Configure route-map on eBGP sessions towards underlay peers, where prefixes with the peer's ASN in the AS Path are filtered away.<br>This is very useful in very large scale networks not using EVPN overlays, where convergence will be quicker by not having to return<br>all updates received from Spine-1 to Spine-2 just for Spine-2 to throw them away because of AS Path loop detection.<br>Note this key is ignored when EVPN is configured.<br> |

=== "YAML"

    ```yaml
    underlay_filter_peer_as: <bool>
    ```

## Evpn Settings

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>evpn_ebgp_gateway_multihop</samp>](## "evpn_ebgp_gateway_multihop") | Integer |  | 15 |  | Default of 15, considering a large value to avoid BGP reachability issues in very complex DCI networks.<br>Adapt the value for your specific topology.<br> |
    | [<samp>evpn_ebgp_multihop</samp>](## "evpn_ebgp_multihop") | Integer |  | 3 |  | Default of 3, the recommended value for a 3 stage spine and leaf topology.<br>Set to a higher value to allow for very large and complex topologies.<br> |
    | [<samp>evpn_hostflap_detection</samp>](## "evpn_hostflap_detection") | Dictionary |  |  |  |  |
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
    evpn_import_pruning: <bool>
    evpn_multicast: <bool>
    evpn_overlay_bgp_rtc: <bool>
    evpn_prevent_readvertise_to_server: <bool>
    evpn_short_esi_prefix: <str>
    evpn_vlan_aware_bundles: <bool>
    ```

## Ipv6 Underlay Settings

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

## Isis Settings

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>isis_advertise_passive_only</samp>](## "isis_advertise_passive_only") | Boolean |  | False |  |  |
    | [<samp>isis_area_id</samp>](## "isis_area_id") | String |  | 49.0001 |  |  |
    | [<samp>isis_default_circuit_type</samp>](## "isis_default_circuit_type") | String |  | level-2 | Valid Values:<br>- level-1-2<br>- level-1<br>- level-2 | These fabric level parameters can be used with core_interfaces running ISIS, and may be overridden on link profile or link level. |
    | [<samp>isis_default_is_type</samp>](## "isis_default_is_type") | String |  | level-2 | Valid Values:<br>- level-1-2<br>- level-1<br>- level-2 |  |
    | [<samp>isis_default_metric</samp>](## "isis_default_metric") | Integer |  | 50 |  | These fabric level parameters can be used with core_interfaces running ISIS, and may be overridden at link profile or link level. |
    | [<samp>isis_ti_lfa</samp>](## "isis_ti_lfa") | Dictionary |  |  |  |  |
    | [<samp>underlay_isis_instance_name</samp>](## "underlay_isis_instance_name") | String |  |  |  | Default -> "EVPN_UNDERLAY" for l3ls, "CORE" for mpls |

=== "YAML"

    ```yaml
    isis_advertise_passive_only: <bool>
    isis_area_id: <str>
    isis_default_circuit_type: <str>
    isis_default_is_type: <str>
    isis_default_metric: <int>
    isis_ti_lfa:
    underlay_isis_instance_name: <str>
    ```

## Multicast Settings

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>underlay_multicast</samp>](## "underlay_multicast") | Boolean |  | False |  | Enable Multicast in the underlay on all p2p uplink interfaces and mlag l3 peer interface.<br>Specifically PIM Sparse-Mode will be configured on all routed underlay interfaces.<br>No other configuration is added, so the underlay will only support Source-Specific Multicast (SSM)<br>The configuration is intended to be used as multicast underlay for EVPN OISM overlay<br> |

=== "YAML"

    ```yaml
    underlay_multicast: <bool>
    ```

## Ospf Settings

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

## Uplinks Settings

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>p2p_uplinks_mtu</samp>](## "p2p_uplinks_mtu") | Integer |  | 9000 | Min: 68<br>Max: 65535 | Point to Point Links MTU |
    | [<samp>p2p_uplinks_qos_profile</samp>](## "p2p_uplinks_qos_profile") | String |  |  |  | QOS Profile assigned on all infrastructure links |
    | [<samp>uplink_ptp</samp>](## "uplink_ptp") | Dictionary |  |  |  | Enable PTP on all infrastructure links |

=== "YAML"

    ```yaml
    p2p_uplinks_mtu: <int>
    p2p_uplinks_qos_profile: <str>
    uplink_ptp:
    ```
