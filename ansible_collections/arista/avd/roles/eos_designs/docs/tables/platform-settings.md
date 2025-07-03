<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>custom_platform_settings</samp>](## "custom_platform_settings") | List, items: Dictionary |  |  |  | Custom Platform settings to override the default `platform_settings`. This list will be prepended to the list of `platform_settings`. The first entry containing `platforms` matching the `platform` node setting will be chosen. If no matches are found, the first entry containing a platform `default` will be chosen. |
    | [<samp>&nbsp;&nbsp;-&nbsp;platforms</samp>](## "custom_platform_settings.[].platforms") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "custom_platform_settings.[].platforms.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;trident_forwarding_table_partition</samp>](## "custom_platform_settings.[].trident_forwarding_table_partition") | String |  |  |  | Only applied when evpn_multicast is true. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;reload_delay</samp>](## "custom_platform_settings.[].reload_delay") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag</samp>](## "custom_platform_settings.[].reload_delay.mlag") | Integer |  |  | Min: 0<br>Max: 86400 | In seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;non_mlag</samp>](## "custom_platform_settings.[].reload_delay.non_mlag") | Integer |  |  | Min: 0<br>Max: 86400 | In seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;tcam_profile</samp>](## "custom_platform_settings.[].tcam_profile") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;lag_hardware_only</samp>](## "custom_platform_settings.[].lag_hardware_only") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;default_interface_mtu</samp>](## "custom_platform_settings.[].default_interface_mtu") | Integer |  |  | Min: 68<br>Max: 65535 | Default interface MTU configured on EOS under "interface defaults".<br>Takes precedence over the root key "default_interface_mtu".<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;p2p_uplinks_mtu</samp>](## "custom_platform_settings.[].p2p_uplinks_mtu") | Integer |  |  | Min: 68<br>Max: 65535 | Set MTU on point to point uplink interfaces.<br>Takes precedence over the root key "p2p_uplinks_mtu".<br><node_type>.uplink_mtu -> platform_settings.p2p_uplinks_mtu -> p2p_uplinks_mtu -> 9214.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;feature_support</samp>](## "custom_platform_settings.[].feature_support") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;queue_monitor</samp>](## "custom_platform_settings.[].feature_support.queue_monitor") | Boolean |  | `True` |  | Support for LANZ.<br>The feature will be ignored on platforms where this is false. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;queue_monitor_length_notify</samp>](## "custom_platform_settings.[].feature_support.queue_monitor_length_notify") | Boolean |  | `True` |  | Support for LANZ notifying mode. Requires the parent `queue_monitor` feature to be enabled.<br>The feature will be ignored on platforms where this is false. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interface_storm_control</samp>](## "custom_platform_settings.[].feature_support.interface_storm_control") | Boolean |  | `True` |  | Support for storm-control.<br>The feature will be ignored on platforms where this is false. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;poe</samp>](## "custom_platform_settings.[].feature_support.poe") | Boolean |  | `False` |  | Support for PoE.<br>The feature will be ignored on platforms where this is false. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;subinterface_mtu</samp>](## "custom_platform_settings.[].feature_support.subinterface_mtu") | Boolean |  | `True` |  | Support for MTU configuration under sub-interfaces.<br>When this key is set to False, MTU is not rendered under sub-interfaces even if it is set in the inputs.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;per_interface_mtu</samp>](## "custom_platform_settings.[].feature_support.per_interface_mtu") | Boolean |  | `True` |  | Support for configuration of per interface MTU for p2p links, MLAG SVIs and Network Services.<br>Effectively this means that all settings regarding interface MTU will be ignored if this is false.<br>Platforms without support for per interface MTU can use a single default interface MTU setting. Set this via "default_interface_mtu"<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;per_interface_l2_mtu</samp>](## "custom_platform_settings.[].feature_support.per_interface_l2_mtu") | Boolean |  | `True` |  | Support for configuration of per interface L2 MTU on Ethernet or Port-channel interfaces.<br>The feature will be ignored on platforms where this is false.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;per_interface_l2_mru</samp>](## "custom_platform_settings.[].feature_support.per_interface_l2_mru") | Boolean |  | `True` |  | Support for configuration of per interface L2 MRU (maximum receive unit) on Ethernet and Port-Channel interfaces.<br>The feature will be ignored on platforms where this is false.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp_update_wait_install</samp>](## "custom_platform_settings.[].feature_support.bgp_update_wait_install") | Boolean |  | `True` |  | Disables FIB updates and route advertisement when the BGP instance is initiated until the BGP convergence state is reached.<br>Can be overridden by setting "bgp_update_wait_install" host/group_vars.<br>The feature will be ignored on platforms where this is false.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp_update_wait_for_convergence</samp>](## "custom_platform_settings.[].feature_support.bgp_update_wait_for_convergence") | Boolean |  | `True` |  | Do not advertise reachability to a prefix until that prefix has been installed in hardware.<br>This will eliminate any temporary black holes due to a BGP speaker advertising reachability to a prefix that may not yet be installed into the forwarding plane.<br>Can be overridden by setting "bgp_update_wait_for_convergence" host/group_vars.<br>The feature will be ignored on platforms where this is false.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;platform_sfe_interface_profile</samp>](## "custom_platform_settings.[].feature_support.platform_sfe_interface_profile") | Dictionary |  |  |  | Support for Platform SFE Interface Profiles. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;supported</samp>](## "custom_platform_settings.[].feature_support.platform_sfe_interface_profile.supported") | Boolean |  | `False` |  | Capability flag for generation of SFE interface profile. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;max_rx_queues</samp>](## "custom_platform_settings.[].feature_support.platform_sfe_interface_profile.max_rx_queues") | Integer |  | `6` |  | Maximum rx_queue count supported on any interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_gateway_all_active_multihoming</samp>](## "custom_platform_settings.[].feature_support.evpn_gateway_all_active_multihoming") | Boolean |  | `False` |  | Support for all-active EVPN gateway redundancy.<br>An error will be raised if the feature is enabled and this is false. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hardware_counters</samp>](## "custom_platform_settings.[].feature_support.hardware_counters") | Boolean |  | `True` |  | Support for enabling counters using programmable hardware counter resources.<br>Setting this key to `false` for the specific platform will ignore all hardware counter features for this platform. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hardware_counter_features</samp>](## "custom_platform_settings.[].feature_support.hardware_counter_features") | Dictionary |  |  |  | Per-feature support for the hardware counters.<br>Features set to `false` will be ignored for this platform. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;acl</samp>](## "custom_platform_settings.[].feature_support.hardware_counter_features.acl") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;decap_group</samp>](## "custom_platform_settings.[].feature_support.hardware_counter_features.decap_group") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;directflow</samp>](## "custom_platform_settings.[].feature_support.hardware_counter_features.directflow") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ecn</samp>](## "custom_platform_settings.[].feature_support.hardware_counter_features.ecn") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;flow_spec</samp>](## "custom_platform_settings.[].feature_support.hardware_counter_features.flow_spec") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;gre_tunnel_interface</samp>](## "custom_platform_settings.[].feature_support.hardware_counter_features.gre_tunnel_interface") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip</samp>](## "custom_platform_settings.[].feature_support.hardware_counter_features.ip") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mpls_interface</samp>](## "custom_platform_settings.[].feature_support.hardware_counter_features.mpls_interface") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mpls_lfib</samp>](## "custom_platform_settings.[].feature_support.hardware_counter_features.mpls_lfib") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mpls_tunnel</samp>](## "custom_platform_settings.[].feature_support.hardware_counter_features.mpls_tunnel") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;multicast</samp>](## "custom_platform_settings.[].feature_support.hardware_counter_features.multicast") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nexthop</samp>](## "custom_platform_settings.[].feature_support.hardware_counter_features.nexthop") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pbr</samp>](## "custom_platform_settings.[].feature_support.hardware_counter_features.pbr") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pdp</samp>](## "custom_platform_settings.[].feature_support.hardware_counter_features.pdp") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;policing_interface</samp>](## "custom_platform_settings.[].feature_support.hardware_counter_features.policing_interface") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;qos</samp>](## "custom_platform_settings.[].feature_support.hardware_counter_features.qos") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;qos_dual_rate_policer</samp>](## "custom_platform_settings.[].feature_support.hardware_counter_features.qos_dual_rate_policer") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route</samp>](## "custom_platform_settings.[].feature_support.hardware_counter_features.route") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;routed_port</samp>](## "custom_platform_settings.[].feature_support.hardware_counter_features.routed_port") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;segment_security</samp>](## "custom_platform_settings.[].feature_support.hardware_counter_features.segment_security") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;subinterface</samp>](## "custom_platform_settings.[].feature_support.hardware_counter_features.subinterface") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tapagg</samp>](## "custom_platform_settings.[].feature_support.hardware_counter_features.tapagg") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;traffic_class</samp>](## "custom_platform_settings.[].feature_support.hardware_counter_features.traffic_class") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;traffic_policy</samp>](## "custom_platform_settings.[].feature_support.hardware_counter_features.traffic_policy") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vlan</samp>](## "custom_platform_settings.[].feature_support.hardware_counter_features.vlan") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vlan_interface</samp>](## "custom_platform_settings.[].feature_support.hardware_counter_features.vlan_interface") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vni_decap</samp>](## "custom_platform_settings.[].feature_support.hardware_counter_features.vni_decap") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vni_encap</samp>](## "custom_platform_settings.[].feature_support.hardware_counter_features.vni_encap") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vtep_decap</samp>](## "custom_platform_settings.[].feature_support.hardware_counter_features.vtep_decap") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vtep_encap</samp>](## "custom_platform_settings.[].feature_support.hardware_counter_features.vtep_encap") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hardware_speed_group</samp>](## "custom_platform_settings.[].feature_support.hardware_speed_group") | Boolean |  | `True` |  | Support for configurable speeds per speed-group.<br>The feature will be ignored on platforms where this is false. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;private_vlan</samp>](## "custom_platform_settings.[].feature_support.private_vlan") | Boolean |  | `True` |  | Support for PVLAN feature.<br>On platforms with additional requirements to use PVLAN, ex. 7280R/R2/R3 set this via "private_vlan" in the specific platform settings.<br>See the TOI at https://www.arista.com/en/support/toi/eos-4-25-0f/14609-support-for-private-vlan.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;management_interface</samp>](## "custom_platform_settings.[].management_interface") | String |  | `Management1` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;security_entropy_sources</samp>](## "custom_platform_settings.[].security_entropy_sources") | Dictionary |  |  |  | Entropy source improves the randomness of the numbers used to generate MACsec's cryptographic keys. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hardware</samp>](## "custom_platform_settings.[].security_entropy_sources.hardware") | Boolean |  |  |  | Use a hardware based source. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;haveged</samp>](## "custom_platform_settings.[].security_entropy_sources.haveged") | Boolean |  |  |  | Use the HAVEGE algorithm. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cpu_jitter</samp>](## "custom_platform_settings.[].security_entropy_sources.cpu_jitter") | Boolean |  |  |  | Use the Jitter RNG algorithm of a CPU based source. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hardware_exclusive</samp>](## "custom_platform_settings.[].security_entropy_sources.hardware_exclusive") | Boolean |  |  |  | Only use entropy from the hardware source. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "custom_platform_settings.[].structured_config") | Dictionary |  |  |  | Custom structured config for eos_cli_config_gen. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "custom_platform_settings.[].raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the root level of the final EOS configuration. |
    | [<samp>platform_settings</samp>](## "platform_settings") | List, items: Dictionary |  | See (+) on YAML tab |  | Platform settings. The first entry containing `platforms` matching the `platform` node setting will be chosen. If no matches are found, the first entry containing a platform `default` will be chosen. The default values will be overridden if `platform_settings` is defined. If you need to replace all the default platforms, it is recommended to copy the defaults and modify them. If you need to add custom platforms, create them under `custom_platform_settings`. Entries under `custom_platform_settings` will be matched before the equivalent entries from `platform_settings`. |
    | [<samp>&nbsp;&nbsp;-&nbsp;platforms</samp>](## "platform_settings.[].platforms") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "platform_settings.[].platforms.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;trident_forwarding_table_partition</samp>](## "platform_settings.[].trident_forwarding_table_partition") | String |  |  |  | Only applied when evpn_multicast is true. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;reload_delay</samp>](## "platform_settings.[].reload_delay") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag</samp>](## "platform_settings.[].reload_delay.mlag") | Integer |  |  | Min: 0<br>Max: 86400 | In seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;non_mlag</samp>](## "platform_settings.[].reload_delay.non_mlag") | Integer |  |  | Min: 0<br>Max: 86400 | In seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;tcam_profile</samp>](## "platform_settings.[].tcam_profile") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;lag_hardware_only</samp>](## "platform_settings.[].lag_hardware_only") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;default_interface_mtu</samp>](## "platform_settings.[].default_interface_mtu") | Integer |  |  | Min: 68<br>Max: 65535 | Default interface MTU configured on EOS under "interface defaults".<br>Takes precedence over the root key "default_interface_mtu".<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;p2p_uplinks_mtu</samp>](## "platform_settings.[].p2p_uplinks_mtu") | Integer |  |  | Min: 68<br>Max: 65535 | Set MTU on point to point uplink interfaces.<br>Takes precedence over the root key "p2p_uplinks_mtu".<br><node_type>.uplink_mtu -> platform_settings.p2p_uplinks_mtu -> p2p_uplinks_mtu -> 9214.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;feature_support</samp>](## "platform_settings.[].feature_support") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;queue_monitor</samp>](## "platform_settings.[].feature_support.queue_monitor") | Boolean |  | `True` |  | Support for LANZ.<br>The feature will be ignored on platforms where this is false. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;queue_monitor_length_notify</samp>](## "platform_settings.[].feature_support.queue_monitor_length_notify") | Boolean |  | `True` |  | Support for LANZ notifying mode. Requires the parent `queue_monitor` feature to be enabled.<br>The feature will be ignored on platforms where this is false. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interface_storm_control</samp>](## "platform_settings.[].feature_support.interface_storm_control") | Boolean |  | `True` |  | Support for storm-control.<br>The feature will be ignored on platforms where this is false. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;poe</samp>](## "platform_settings.[].feature_support.poe") | Boolean |  | `False` |  | Support for PoE.<br>The feature will be ignored on platforms where this is false. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;subinterface_mtu</samp>](## "platform_settings.[].feature_support.subinterface_mtu") | Boolean |  | `True` |  | Support for MTU configuration under sub-interfaces.<br>When this key is set to False, MTU is not rendered under sub-interfaces even if it is set in the inputs.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;per_interface_mtu</samp>](## "platform_settings.[].feature_support.per_interface_mtu") | Boolean |  | `True` |  | Support for configuration of per interface MTU for p2p links, MLAG SVIs and Network Services.<br>Effectively this means that all settings regarding interface MTU will be ignored if this is false.<br>Platforms without support for per interface MTU can use a single default interface MTU setting. Set this via "default_interface_mtu"<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;per_interface_l2_mtu</samp>](## "platform_settings.[].feature_support.per_interface_l2_mtu") | Boolean |  | `True` |  | Support for configuration of per interface L2 MTU on Ethernet or Port-channel interfaces.<br>The feature will be ignored on platforms where this is false.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;per_interface_l2_mru</samp>](## "platform_settings.[].feature_support.per_interface_l2_mru") | Boolean |  | `True` |  | Support for configuration of per interface L2 MRU (maximum receive unit) on Ethernet and Port-Channel interfaces.<br>The feature will be ignored on platforms where this is false.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp_update_wait_install</samp>](## "platform_settings.[].feature_support.bgp_update_wait_install") | Boolean |  | `True` |  | Disables FIB updates and route advertisement when the BGP instance is initiated until the BGP convergence state is reached.<br>Can be overridden by setting "bgp_update_wait_install" host/group_vars.<br>The feature will be ignored on platforms where this is false.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp_update_wait_for_convergence</samp>](## "platform_settings.[].feature_support.bgp_update_wait_for_convergence") | Boolean |  | `True` |  | Do not advertise reachability to a prefix until that prefix has been installed in hardware.<br>This will eliminate any temporary black holes due to a BGP speaker advertising reachability to a prefix that may not yet be installed into the forwarding plane.<br>Can be overridden by setting "bgp_update_wait_for_convergence" host/group_vars.<br>The feature will be ignored on platforms where this is false.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;platform_sfe_interface_profile</samp>](## "platform_settings.[].feature_support.platform_sfe_interface_profile") | Dictionary |  |  |  | Support for Platform SFE Interface Profiles. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;supported</samp>](## "platform_settings.[].feature_support.platform_sfe_interface_profile.supported") | Boolean |  | `False` |  | Capability flag for generation of SFE interface profile. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;max_rx_queues</samp>](## "platform_settings.[].feature_support.platform_sfe_interface_profile.max_rx_queues") | Integer |  | `6` |  | Maximum rx_queue count supported on any interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_gateway_all_active_multihoming</samp>](## "platform_settings.[].feature_support.evpn_gateway_all_active_multihoming") | Boolean |  | `False` |  | Support for all-active EVPN gateway redundancy.<br>An error will be raised if the feature is enabled and this is false. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hardware_counters</samp>](## "platform_settings.[].feature_support.hardware_counters") | Boolean |  | `True` |  | Support for enabling counters using programmable hardware counter resources.<br>Setting this key to `false` for the specific platform will ignore all hardware counter features for this platform. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hardware_counter_features</samp>](## "platform_settings.[].feature_support.hardware_counter_features") | Dictionary |  |  |  | Per-feature support for the hardware counters.<br>Features set to `false` will be ignored for this platform. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;acl</samp>](## "platform_settings.[].feature_support.hardware_counter_features.acl") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;decap_group</samp>](## "platform_settings.[].feature_support.hardware_counter_features.decap_group") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;directflow</samp>](## "platform_settings.[].feature_support.hardware_counter_features.directflow") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ecn</samp>](## "platform_settings.[].feature_support.hardware_counter_features.ecn") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;flow_spec</samp>](## "platform_settings.[].feature_support.hardware_counter_features.flow_spec") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;gre_tunnel_interface</samp>](## "platform_settings.[].feature_support.hardware_counter_features.gre_tunnel_interface") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip</samp>](## "platform_settings.[].feature_support.hardware_counter_features.ip") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mpls_interface</samp>](## "platform_settings.[].feature_support.hardware_counter_features.mpls_interface") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mpls_lfib</samp>](## "platform_settings.[].feature_support.hardware_counter_features.mpls_lfib") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mpls_tunnel</samp>](## "platform_settings.[].feature_support.hardware_counter_features.mpls_tunnel") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;multicast</samp>](## "platform_settings.[].feature_support.hardware_counter_features.multicast") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nexthop</samp>](## "platform_settings.[].feature_support.hardware_counter_features.nexthop") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pbr</samp>](## "platform_settings.[].feature_support.hardware_counter_features.pbr") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pdp</samp>](## "platform_settings.[].feature_support.hardware_counter_features.pdp") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;policing_interface</samp>](## "platform_settings.[].feature_support.hardware_counter_features.policing_interface") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;qos</samp>](## "platform_settings.[].feature_support.hardware_counter_features.qos") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;qos_dual_rate_policer</samp>](## "platform_settings.[].feature_support.hardware_counter_features.qos_dual_rate_policer") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route</samp>](## "platform_settings.[].feature_support.hardware_counter_features.route") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;routed_port</samp>](## "platform_settings.[].feature_support.hardware_counter_features.routed_port") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;segment_security</samp>](## "platform_settings.[].feature_support.hardware_counter_features.segment_security") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;subinterface</samp>](## "platform_settings.[].feature_support.hardware_counter_features.subinterface") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tapagg</samp>](## "platform_settings.[].feature_support.hardware_counter_features.tapagg") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;traffic_class</samp>](## "platform_settings.[].feature_support.hardware_counter_features.traffic_class") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;traffic_policy</samp>](## "platform_settings.[].feature_support.hardware_counter_features.traffic_policy") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vlan</samp>](## "platform_settings.[].feature_support.hardware_counter_features.vlan") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vlan_interface</samp>](## "platform_settings.[].feature_support.hardware_counter_features.vlan_interface") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vni_decap</samp>](## "platform_settings.[].feature_support.hardware_counter_features.vni_decap") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vni_encap</samp>](## "platform_settings.[].feature_support.hardware_counter_features.vni_encap") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vtep_decap</samp>](## "platform_settings.[].feature_support.hardware_counter_features.vtep_decap") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vtep_encap</samp>](## "platform_settings.[].feature_support.hardware_counter_features.vtep_encap") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hardware_speed_group</samp>](## "platform_settings.[].feature_support.hardware_speed_group") | Boolean |  | `True` |  | Support for configurable speeds per speed-group.<br>The feature will be ignored on platforms where this is false. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;private_vlan</samp>](## "platform_settings.[].feature_support.private_vlan") | Boolean |  | `True` |  | Support for PVLAN feature.<br>On platforms with additional requirements to use PVLAN, ex. 7280R/R2/R3 set this via "private_vlan" in the specific platform settings.<br>See the TOI at https://www.arista.com/en/support/toi/eos-4-25-0f/14609-support-for-private-vlan.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;management_interface</samp>](## "platform_settings.[].management_interface") | String |  | `Management1` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;security_entropy_sources</samp>](## "platform_settings.[].security_entropy_sources") | Dictionary |  |  |  | Entropy source improves the randomness of the numbers used to generate MACsec's cryptographic keys. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hardware</samp>](## "platform_settings.[].security_entropy_sources.hardware") | Boolean |  |  |  | Use a hardware based source. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;haveged</samp>](## "platform_settings.[].security_entropy_sources.haveged") | Boolean |  |  |  | Use the HAVEGE algorithm. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cpu_jitter</samp>](## "platform_settings.[].security_entropy_sources.cpu_jitter") | Boolean |  |  |  | Use the Jitter RNG algorithm of a CPU based source. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hardware_exclusive</samp>](## "platform_settings.[].security_entropy_sources.hardware_exclusive") | Boolean |  |  |  | Only use entropy from the hardware source. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "platform_settings.[].structured_config") | Dictionary |  |  |  | Custom structured config for eos_cli_config_gen. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "platform_settings.[].raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the root level of the final EOS configuration. |
    | [<samp>platform_speed_groups</samp>](## "platform_speed_groups") | List, items: Dictionary |  |  |  | Set Hardware Speed Groups per Platform. |
    | [<samp>&nbsp;&nbsp;-&nbsp;platform</samp>](## "platform_speed_groups.[].platform") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;speeds</samp>](## "platform_speed_groups.[].speeds") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;speed</samp>](## "platform_speed_groups.[].speeds.[].speed") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;speed_groups</samp>](## "platform_speed_groups.[].speeds.[].speed_groups") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "platform_speed_groups.[].speeds.[].speed_groups.[]") | String |  |  |  |  |

=== "YAML"

    ```yaml
    # Custom Platform settings to override the default `platform_settings`. This list will be prepended to the list of `platform_settings`. The first entry containing `platforms` matching the `platform` node setting will be chosen. If no matches are found, the first entry containing a platform `default` will be chosen.
    custom_platform_settings:
      - platforms:
          - <str>

        # Only applied when evpn_multicast is true.
        trident_forwarding_table_partition: <str>
        reload_delay:

          # In seconds.
          mlag: <int; 0-86400>

          # In seconds.
          non_mlag: <int; 0-86400>
        tcam_profile: <str>
        lag_hardware_only: <bool>

        # Default interface MTU configured on EOS under "interface defaults".
        # Takes precedence over the root key "default_interface_mtu".
        default_interface_mtu: <int; 68-65535>

        # Set MTU on point to point uplink interfaces.
        # Takes precedence over the root key "p2p_uplinks_mtu".
        # <node_type>.uplink_mtu -> platform_settings.p2p_uplinks_mtu -> p2p_uplinks_mtu -> 9214.
        p2p_uplinks_mtu: <int; 68-65535>
        feature_support:

          # Support for LANZ.
          # The feature will be ignored on platforms where this is false.
          queue_monitor: <bool; default=True>

          # Support for LANZ notifying mode. Requires the parent `queue_monitor` feature to be enabled.
          # The feature will be ignored on platforms where this is false.
          queue_monitor_length_notify: <bool; default=True>

          # Support for storm-control.
          # The feature will be ignored on platforms where this is false.
          interface_storm_control: <bool; default=True>

          # Support for PoE.
          # The feature will be ignored on platforms where this is false.
          poe: <bool; default=False>

          # Support for MTU configuration under sub-interfaces.
          # When this key is set to False, MTU is not rendered under sub-interfaces even if it is set in the inputs.
          subinterface_mtu: <bool; default=True>

          # Support for configuration of per interface MTU for p2p links, MLAG SVIs and Network Services.
          # Effectively this means that all settings regarding interface MTU will be ignored if this is false.
          # Platforms without support for per interface MTU can use a single default interface MTU setting. Set this via "default_interface_mtu"
          per_interface_mtu: <bool; default=True>

          # Support for configuration of per interface L2 MTU on Ethernet or Port-channel interfaces.
          # The feature will be ignored on platforms where this is false.
          per_interface_l2_mtu: <bool; default=True>

          # Support for configuration of per interface L2 MRU (maximum receive unit) on Ethernet and Port-Channel interfaces.
          # The feature will be ignored on platforms where this is false.
          per_interface_l2_mru: <bool; default=True>

          # Disables FIB updates and route advertisement when the BGP instance is initiated until the BGP convergence state is reached.
          # Can be overridden by setting "bgp_update_wait_install" host/group_vars.
          # The feature will be ignored on platforms where this is false.
          bgp_update_wait_install: <bool; default=True>

          # Do not advertise reachability to a prefix until that prefix has been installed in hardware.
          # This will eliminate any temporary black holes due to a BGP speaker advertising reachability to a prefix that may not yet be installed into the forwarding plane.
          # Can be overridden by setting "bgp_update_wait_for_convergence" host/group_vars.
          # The feature will be ignored on platforms where this is false.
          bgp_update_wait_for_convergence: <bool; default=True>

          # Support for Platform SFE Interface Profiles.
          platform_sfe_interface_profile:

            # Capability flag for generation of SFE interface profile.
            supported: <bool; default=False>

            # Maximum rx_queue count supported on any interface.
            max_rx_queues: <int; default=6>

          # Support for all-active EVPN gateway redundancy.
          # An error will be raised if the feature is enabled and this is false.
          evpn_gateway_all_active_multihoming: <bool; default=False>

          # Support for enabling counters using programmable hardware counter resources.
          # Setting this key to `false` for the specific platform will ignore all hardware counter features for this platform.
          hardware_counters: <bool; default=True>

          # Per-feature support for the hardware counters.
          # Features set to `false` will be ignored for this platform.
          hardware_counter_features:
            acl: <bool; default=True>
            decap_group: <bool; default=True>
            directflow: <bool; default=True>
            ecn: <bool; default=True>
            flow_spec: <bool; default=True>
            gre_tunnel_interface: <bool; default=True>
            ip: <bool; default=True>
            mpls_interface: <bool; default=True>
            mpls_lfib: <bool; default=True>
            mpls_tunnel: <bool; default=True>
            multicast: <bool; default=True>
            nexthop: <bool; default=True>
            pbr: <bool; default=True>
            pdp: <bool; default=True>
            policing_interface: <bool; default=True>
            qos: <bool; default=True>
            qos_dual_rate_policer: <bool; default=True>
            route: <bool; default=True>
            routed_port: <bool; default=True>
            segment_security: <bool; default=True>
            subinterface: <bool; default=True>
            tapagg: <bool; default=True>
            traffic_class: <bool; default=True>
            traffic_policy: <bool; default=True>
            vlan: <bool; default=True>
            vlan_interface: <bool; default=True>
            vni_decap: <bool; default=True>
            vni_encap: <bool; default=True>
            vtep_decap: <bool; default=True>
            vtep_encap: <bool; default=True>

          # Support for configurable speeds per speed-group.
          # The feature will be ignored on platforms where this is false.
          hardware_speed_group: <bool; default=True>

          # Support for PVLAN feature.
          # On platforms with additional requirements to use PVLAN, ex. 7280R/R2/R3 set this via "private_vlan" in the specific platform settings.
          # See the TOI at https://www.arista.com/en/support/toi/eos-4-25-0f/14609-support-for-private-vlan.
          private_vlan: <bool; default=True>
        management_interface: <str; default="Management1">

        # Entropy source improves the randomness of the numbers used to generate MACsec's cryptographic keys.
        security_entropy_sources:

          # Use a hardware based source.
          hardware: <bool>

          # Use the HAVEGE algorithm.
          haveged: <bool>

          # Use the Jitter RNG algorithm of a CPU based source.
          cpu_jitter: <bool>

          # Only use entropy from the hardware source.
          hardware_exclusive: <bool>

        # Custom structured config for eos_cli_config_gen.
        structured_config: <dict>

        # EOS CLI rendered directly on the root level of the final EOS configuration.
        raw_eos_cli: <str>

    # Platform settings. The first entry containing `platforms` matching the `platform` node setting will be chosen. If no matches are found, the first entry containing a platform `default` will be chosen. The default values will be overridden if `platform_settings` is defined. If you need to replace all the default platforms, it is recommended to copy the defaults and modify them. If you need to add custom platforms, create them under `custom_platform_settings`. Entries under `custom_platform_settings` will be matched before the equivalent entries from `platform_settings`.
    platform_settings: # (1)!
      - platforms:
          - <str>

        # Only applied when evpn_multicast is true.
        trident_forwarding_table_partition: <str>
        reload_delay:

          # In seconds.
          mlag: <int; 0-86400>

          # In seconds.
          non_mlag: <int; 0-86400>
        tcam_profile: <str>
        lag_hardware_only: <bool>

        # Default interface MTU configured on EOS under "interface defaults".
        # Takes precedence over the root key "default_interface_mtu".
        default_interface_mtu: <int; 68-65535>

        # Set MTU on point to point uplink interfaces.
        # Takes precedence over the root key "p2p_uplinks_mtu".
        # <node_type>.uplink_mtu -> platform_settings.p2p_uplinks_mtu -> p2p_uplinks_mtu -> 9214.
        p2p_uplinks_mtu: <int; 68-65535>
        feature_support:

          # Support for LANZ.
          # The feature will be ignored on platforms where this is false.
          queue_monitor: <bool; default=True>

          # Support for LANZ notifying mode. Requires the parent `queue_monitor` feature to be enabled.
          # The feature will be ignored on platforms where this is false.
          queue_monitor_length_notify: <bool; default=True>

          # Support for storm-control.
          # The feature will be ignored on platforms where this is false.
          interface_storm_control: <bool; default=True>

          # Support for PoE.
          # The feature will be ignored on platforms where this is false.
          poe: <bool; default=False>

          # Support for MTU configuration under sub-interfaces.
          # When this key is set to False, MTU is not rendered under sub-interfaces even if it is set in the inputs.
          subinterface_mtu: <bool; default=True>

          # Support for configuration of per interface MTU for p2p links, MLAG SVIs and Network Services.
          # Effectively this means that all settings regarding interface MTU will be ignored if this is false.
          # Platforms without support for per interface MTU can use a single default interface MTU setting. Set this via "default_interface_mtu"
          per_interface_mtu: <bool; default=True>

          # Support for configuration of per interface L2 MTU on Ethernet or Port-channel interfaces.
          # The feature will be ignored on platforms where this is false.
          per_interface_l2_mtu: <bool; default=True>

          # Support for configuration of per interface L2 MRU (maximum receive unit) on Ethernet and Port-Channel interfaces.
          # The feature will be ignored on platforms where this is false.
          per_interface_l2_mru: <bool; default=True>

          # Disables FIB updates and route advertisement when the BGP instance is initiated until the BGP convergence state is reached.
          # Can be overridden by setting "bgp_update_wait_install" host/group_vars.
          # The feature will be ignored on platforms where this is false.
          bgp_update_wait_install: <bool; default=True>

          # Do not advertise reachability to a prefix until that prefix has been installed in hardware.
          # This will eliminate any temporary black holes due to a BGP speaker advertising reachability to a prefix that may not yet be installed into the forwarding plane.
          # Can be overridden by setting "bgp_update_wait_for_convergence" host/group_vars.
          # The feature will be ignored on platforms where this is false.
          bgp_update_wait_for_convergence: <bool; default=True>

          # Support for Platform SFE Interface Profiles.
          platform_sfe_interface_profile:

            # Capability flag for generation of SFE interface profile.
            supported: <bool; default=False>

            # Maximum rx_queue count supported on any interface.
            max_rx_queues: <int; default=6>

          # Support for all-active EVPN gateway redundancy.
          # An error will be raised if the feature is enabled and this is false.
          evpn_gateway_all_active_multihoming: <bool; default=False>

          # Support for enabling counters using programmable hardware counter resources.
          # Setting this key to `false` for the specific platform will ignore all hardware counter features for this platform.
          hardware_counters: <bool; default=True>

          # Per-feature support for the hardware counters.
          # Features set to `false` will be ignored for this platform.
          hardware_counter_features:
            acl: <bool; default=True>
            decap_group: <bool; default=True>
            directflow: <bool; default=True>
            ecn: <bool; default=True>
            flow_spec: <bool; default=True>
            gre_tunnel_interface: <bool; default=True>
            ip: <bool; default=True>
            mpls_interface: <bool; default=True>
            mpls_lfib: <bool; default=True>
            mpls_tunnel: <bool; default=True>
            multicast: <bool; default=True>
            nexthop: <bool; default=True>
            pbr: <bool; default=True>
            pdp: <bool; default=True>
            policing_interface: <bool; default=True>
            qos: <bool; default=True>
            qos_dual_rate_policer: <bool; default=True>
            route: <bool; default=True>
            routed_port: <bool; default=True>
            segment_security: <bool; default=True>
            subinterface: <bool; default=True>
            tapagg: <bool; default=True>
            traffic_class: <bool; default=True>
            traffic_policy: <bool; default=True>
            vlan: <bool; default=True>
            vlan_interface: <bool; default=True>
            vni_decap: <bool; default=True>
            vni_encap: <bool; default=True>
            vtep_decap: <bool; default=True>
            vtep_encap: <bool; default=True>

          # Support for configurable speeds per speed-group.
          # The feature will be ignored on platforms where this is false.
          hardware_speed_group: <bool; default=True>

          # Support for PVLAN feature.
          # On platforms with additional requirements to use PVLAN, ex. 7280R/R2/R3 set this via "private_vlan" in the specific platform settings.
          # See the TOI at https://www.arista.com/en/support/toi/eos-4-25-0f/14609-support-for-private-vlan.
          private_vlan: <bool; default=True>
        management_interface: <str; default="Management1">

        # Entropy source improves the randomness of the numbers used to generate MACsec's cryptographic keys.
        security_entropy_sources:

          # Use a hardware based source.
          hardware: <bool>

          # Use the HAVEGE algorithm.
          haveged: <bool>

          # Use the Jitter RNG algorithm of a CPU based source.
          cpu_jitter: <bool>

          # Only use entropy from the hardware source.
          hardware_exclusive: <bool>

        # Custom structured config for eos_cli_config_gen.
        structured_config: <dict>

        # EOS CLI rendered directly on the root level of the final EOS configuration.
        raw_eos_cli: <str>

    # Set Hardware Speed Groups per Platform.
    platform_speed_groups:
      - platform: <str; required; unique>
        speeds:
          - speed: <str; required; unique>
            speed_groups:
              - <str>
    ```

    1. Default Value

        ```yaml
        platform_settings:
        - feature_support:
            queue_monitor_length_notify: false
          platforms:
          - default
          reload_delay:
            mlag: 300
            non_mlag: 330
        - feature_support:
            queue_monitor_length_notify: false
          platforms:
          - 7050X3
          reload_delay:
            mlag: 300
            non_mlag: 330
          trident_forwarding_table_partition: flexible exact-match 16384 l2-shared 98304 l3-shared
            131072
        - feature_support:
            poe: true
            queue_monitor_length_notify: false
          platforms:
          - 720XP
          reload_delay:
            mlag: 300
            non_mlag: 330
          trident_forwarding_table_partition: flexible exact-match 16000 l2-shared 18000 l3-shared
            22000
        - feature_support:
            poe: true
            queue_monitor_length_notify: false
          management_interface: Management0
          platforms:
          - '750'
          - '755'
          - '758'
          reload_delay:
            mlag: 300
            non_mlag: 330
        - feature_support:
            poe: true
            queue_monitor_length_notify: false
          platforms:
          - 720DP
          - 722XP
          - 710P
          reload_delay:
            mlag: 300
            non_mlag: 330
        - feature_support:
            per_interface_mtu: false
            queue_monitor_length_notify: false
          platforms:
          - 7010TX
          reload_delay:
            mlag: 300
            non_mlag: 330
        - feature_support:
            private_vlan: false
          lag_hardware_only: true
          platforms:
          - 7280R
          - 7280R2
          - 7020R
          reload_delay:
            mlag: 900
            non_mlag: 1020
          tcam_profile: vxlan-routing
        - feature_support:
            evpn_gateway_all_active_multihoming: true
            private_vlan: false
          platforms:
          - 7280R3
          reload_delay:
            mlag: 900
            non_mlag: 1020
          tcam_profile: vxlan-routing
        - feature_support:
            private_vlan: false
          lag_hardware_only: true
          management_interface: Management0
          platforms:
          - 7500R
          - 7500R2
          reload_delay:
            mlag: 900
            non_mlag: 1020
          tcam_profile: vxlan-routing
        - feature_support:
            evpn_gateway_all_active_multihoming: true
            private_vlan: false
          management_interface: Management0
          platforms:
          - 7500R3
          - 7800R3
          reload_delay:
            mlag: 900
            non_mlag: 1020
          tcam_profile: vxlan-routing
        - feature_support:
            bgp_update_wait_for_convergence: true
            bgp_update_wait_install: false
            interface_storm_control: true
            queue_monitor_length_notify: false
          management_interface: Management1/1
          platforms:
          - 7358X4
          reload_delay:
            mlag: 300
            non_mlag: 330
        - management_interface: Management0
          platforms:
          - 7368X4
          reload_delay:
            mlag: 300
            non_mlag: 330
        - management_interface: Management0
          platforms:
          - 7300X3
          reload_delay:
            mlag: 1200
            non_mlag: 1320
          trident_forwarding_table_partition: flexible exact-match 16384 l2-shared 98304 l3-shared
            131072
        - feature_support:
            bgp_update_wait_for_convergence: false
            bgp_update_wait_install: false
            evpn_gateway_all_active_multihoming: true
            interface_storm_control: false
            queue_monitor_length_notify: false
          platforms:
          - VEOS
          - VEOS-LAB
          - vEOS
          - vEOS-lab
          reload_delay:
            mlag: 300
            non_mlag: 330
        - feature_support:
            bgp_update_wait_for_convergence: false
            bgp_update_wait_install: false
            evpn_gateway_all_active_multihoming: true
            interface_storm_control: false
            queue_monitor_length_notify: false
          management_interface: Management0
          platforms:
          - CEOS
          - cEOS
          - ceos
          - cEOSLab
          reload_delay:
            mlag: 300
            non_mlag: 330
        - feature_support:
            bgp_update_wait_install: false
            interface_storm_control: false
            queue_monitor_length_notify: false
          p2p_uplinks_mtu: 9194
          platforms:
          - CloudEOS
        - feature_support:
            bgp_update_wait_for_convergence: true
            bgp_update_wait_install: false
            interface_storm_control: false
            platform_sfe_interface_profile:
              max_rx_queues: 6
              supported: true
            queue_monitor_length_notify: false
          management_interface: Management1/1
          p2p_uplinks_mtu: 9194
          platforms:
          - AWE-5310
          - AWE-7230R
        - feature_support:
            bgp_update_wait_for_convergence: true
            bgp_update_wait_install: false
            interface_storm_control: false
            platform_sfe_interface_profile:
              max_rx_queues: 16
              supported: true
            queue_monitor_length_notify: false
          management_interface: Management1/1
          p2p_uplinks_mtu: 9194
          platforms:
          - AWE-5510
          - AWE-7250R
        - feature_support:
            bgp_update_wait_for_convergence: true
            bgp_update_wait_install: false
            interface_storm_control: false
            poe: true
            queue_monitor_length_notify: false
          management_interface: Management1
          p2p_uplinks_mtu: 9194
          platforms:
          - AWE-7220R
        ```
