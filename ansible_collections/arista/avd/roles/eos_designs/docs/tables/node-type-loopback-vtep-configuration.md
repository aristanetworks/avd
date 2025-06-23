<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>&lt;node_type_keys.key&gt;</samp>](## "<node_type_keys.key>") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;defaults</samp>](## "<node_type_keys.key>.defaults") | Dictionary |  |  |  | Define variables for all nodes of this type. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;loopback_ipv4_pool</samp>](## "<node_type_keys.key>.defaults.loopback_ipv4_pool") | String |  |  | Format: ipv4_pool | Comma separated list of prefixes (IPv4 address/Mask) or ranges (IPv4_address-IPv4_address).<br>The IPv4 address used for Loopback0 will be derived from this pool based on the node id and 'loopback_ipv4_offset'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;loopback_ipv4_address</samp>](## "<node_type_keys.key>.defaults.loopback_ipv4_address") | String |  |  | Format: ipv4 | IPv4 address without mask for Loopback0.<br>When set, it takes precedence over `loopback_ipv4_pool`.<br>Note: AVD does not check for validity of the IPv4 address and does not catch duplicates. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vtep_loopback_ipv4_pool</samp>](## "<node_type_keys.key>.defaults.vtep_loopback_ipv4_pool") | String |  |  | Format: ipv4_pool | Comma separated list of prefixes (IPv4 address/Mask) or ranges (IPv4_address-IPv4_address). The IPv4 address used for VTEP-Loopback will be derived from this pool based on the node id and 'loopback_ipv4_offset'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vtep_loopback_ipv6_pool</samp>](## "<node_type_keys.key>.defaults.vtep_loopback_ipv6_pool") | String |  |  | Format: ipv6_pool | Comma separated list of prefixes (IPv6 address/Mask) or ranges (IPv6_address-IPv6_address). The IPv6 address used for VTEP-Loopback will be derived from this pool based on the node id and 'loopback_ipv6_offset'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vtep_loopback_ipv4_address</samp>](## "<node_type_keys.key>.defaults.vtep_loopback_ipv4_address") | String |  |  | Format: ipv4 | IPv4 address without mask for VTEP-Loopback.<br>When set, it takes precedence over `vtep_loopback_ipv4_pool`.<br>Note: AVD does not check for validity of the IPv4 address and does not catch duplicates. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vtep_loopback_ipv6_address</samp>](## "<node_type_keys.key>.defaults.vtep_loopback_ipv6_address") | String |  |  | Format: ipv6 | IPv6 address without mask for VTEP-Loopback.<br>When set, it takes precedence over `vtep_loopback_ipv6_pool`.<br>Note: AVD does not check for validity of the IPv6 address and does not catch duplicates. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;loopback_ipv4_offset</samp>](## "<node_type_keys.key>.defaults.loopback_ipv4_offset") | Integer |  | `0` |  | Offset all assigned loopback IP addresses.<br>Required when the 'loopback_ipv4_pool' is the same for 2 different node_types (like spine and l3leaf) to avoid overlapping IPs.<br>For example, set the minimum offset l3leaf.defaults.loopback_ipv4_offset: < total # spine switches > or vice versa.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;router_id_pool</samp>](## "<node_type_keys.key>.defaults.router_id_pool") | String |  |  | Format: ipv4_pool | Required when underlay_ipv6_numbered is used to configured an IPv6 underlay and IPv6 overlay. router_id_pool is an IPv4 subnet used only for allocation of BGP router-id's since an IPv4 address will not exist on the device. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;loopback_ipv6_pool</samp>](## "<node_type_keys.key>.defaults.loopback_ipv6_pool") | String |  |  | Format: ipv6_pool | Comma separated list of prefixes (IPv6 address/Mask) or ranges (IPv6_address-IPv6_address). The IPv6 address used for Loopback0 will be derived from this pool based on the node id and 'loopback_ipv6_offset'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;loopback_ipv6_offset</samp>](## "<node_type_keys.key>.defaults.loopback_ipv6_offset") | Integer |  | `0` |  | Offset all assigned loopback IPv6 addresses.<br>Required when the 'loopback_ipv6_pool' is same for 2 different node_types (like spine and l3leaf) to avoid overlapping IPs.<br>For example, set the minimum offset l3leaf.defaults.loopback_ipv6_offset: < total # spine switches > or vice versa.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vtep</samp>](## "<node_type_keys.key>.defaults.vtep") | Boolean |  |  |  | Node is configured as a VTEP when applicable based on 'overlay_routing_protocol'.<br>Overrides VTEP setting inherited from node_type_keys. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vtep_loopback</samp>](## "<node_type_keys.key>.defaults.vtep_loopback") | String |  |  | Pattern: `Loopback[\d/]+` | Set VXLAN source interface. |
    | [<samp>&nbsp;&nbsp;node_groups</samp>](## "<node_type_keys.key>.node_groups") | List, items: Dictionary |  |  |  | Define variables related to all nodes part of this group. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;group</samp>](## "<node_type_keys.key>.node_groups.[].group") | String | Required, Unique |  |  | The Node Group Name is used for MLAG domain unless set with 'mlag_domain_id'.<br>The Node Group Name is also used for peer description on downstream switches' uplinks.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "<node_type_keys.key>.node_groups.[].nodes") | List, items: Dictionary |  |  |  | Define variables per node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].name") | String | Required, Unique |  |  | The Node Name is used as "hostname". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loopback_ipv4_pool</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].loopback_ipv4_pool") | String |  |  | Format: ipv4_pool | Comma separated list of prefixes (IPv4 address/Mask) or ranges (IPv4_address-IPv4_address).<br>The IPv4 address used for Loopback0 will be derived from this pool based on the node id and 'loopback_ipv4_offset'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loopback_ipv4_address</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].loopback_ipv4_address") | String |  |  | Format: ipv4 | IPv4 address without mask for Loopback0.<br>When set, it takes precedence over `loopback_ipv4_pool`.<br>Note: AVD does not check for validity of the IPv4 address and does not catch duplicates. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vtep_loopback_ipv4_pool</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].vtep_loopback_ipv4_pool") | String |  |  | Format: ipv4_pool | Comma separated list of prefixes (IPv4 address/Mask) or ranges (IPv4_address-IPv4_address). The IPv4 address used for VTEP-Loopback will be derived from this pool based on the node id and 'loopback_ipv4_offset'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vtep_loopback_ipv6_pool</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].vtep_loopback_ipv6_pool") | String |  |  | Format: ipv6_pool | Comma separated list of prefixes (IPv6 address/Mask) or ranges (IPv6_address-IPv6_address). The IPv6 address used for VTEP-Loopback will be derived from this pool based on the node id and 'loopback_ipv6_offset'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vtep_loopback_ipv4_address</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].vtep_loopback_ipv4_address") | String |  |  | Format: ipv4 | IPv4 address without mask for VTEP-Loopback.<br>When set, it takes precedence over `vtep_loopback_ipv4_pool`.<br>Note: AVD does not check for validity of the IPv4 address and does not catch duplicates. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vtep_loopback_ipv6_address</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].vtep_loopback_ipv6_address") | String |  |  | Format: ipv6 | IPv6 address without mask for VTEP-Loopback.<br>When set, it takes precedence over `vtep_loopback_ipv6_pool`.<br>Note: AVD does not check for validity of the IPv6 address and does not catch duplicates. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loopback_ipv4_offset</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].loopback_ipv4_offset") | Integer |  | `0` |  | Offset all assigned loopback IP addresses.<br>Required when the 'loopback_ipv4_pool' is the same for 2 different node_types (like spine and l3leaf) to avoid overlapping IPs.<br>For example, set the minimum offset l3leaf.defaults.loopback_ipv4_offset: < total # spine switches > or vice versa.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;router_id_pool</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].router_id_pool") | String |  |  | Format: ipv4_pool | Required when underlay_ipv6_numbered is used to configured an IPv6 underlay and IPv6 overlay. router_id_pool is an IPv4 subnet used only for allocation of BGP router-id's since an IPv4 address will not exist on the device. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loopback_ipv6_pool</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].loopback_ipv6_pool") | String |  |  | Format: ipv6_pool | Comma separated list of prefixes (IPv6 address/Mask) or ranges (IPv6_address-IPv6_address). The IPv6 address used for Loopback0 will be derived from this pool based on the node id and 'loopback_ipv6_offset'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loopback_ipv6_offset</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].loopback_ipv6_offset") | Integer |  | `0` |  | Offset all assigned loopback IPv6 addresses.<br>Required when the 'loopback_ipv6_pool' is same for 2 different node_types (like spine and l3leaf) to avoid overlapping IPs.<br>For example, set the minimum offset l3leaf.defaults.loopback_ipv6_offset: < total # spine switches > or vice versa.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vtep</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].vtep") | Boolean |  |  |  | Node is configured as a VTEP when applicable based on 'overlay_routing_protocol'.<br>Overrides VTEP setting inherited from node_type_keys. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vtep_loopback</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].vtep_loopback") | String |  |  | Pattern: `Loopback[\d/]+` | Set VXLAN source interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loopback_ipv4_pool</samp>](## "<node_type_keys.key>.node_groups.[].loopback_ipv4_pool") | String |  |  | Format: ipv4_pool | Comma separated list of prefixes (IPv4 address/Mask) or ranges (IPv4_address-IPv4_address).<br>The IPv4 address used for Loopback0 will be derived from this pool based on the node id and 'loopback_ipv4_offset'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loopback_ipv4_address</samp>](## "<node_type_keys.key>.node_groups.[].loopback_ipv4_address") | String |  |  | Format: ipv4 | IPv4 address without mask for Loopback0.<br>When set, it takes precedence over `loopback_ipv4_pool`.<br>Note: AVD does not check for validity of the IPv4 address and does not catch duplicates. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vtep_loopback_ipv4_pool</samp>](## "<node_type_keys.key>.node_groups.[].vtep_loopback_ipv4_pool") | String |  |  | Format: ipv4_pool | Comma separated list of prefixes (IPv4 address/Mask) or ranges (IPv4_address-IPv4_address). The IPv4 address used for VTEP-Loopback will be derived from this pool based on the node id and 'loopback_ipv4_offset'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vtep_loopback_ipv6_pool</samp>](## "<node_type_keys.key>.node_groups.[].vtep_loopback_ipv6_pool") | String |  |  | Format: ipv6_pool | Comma separated list of prefixes (IPv6 address/Mask) or ranges (IPv6_address-IPv6_address). The IPv6 address used for VTEP-Loopback will be derived from this pool based on the node id and 'loopback_ipv6_offset'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vtep_loopback_ipv4_address</samp>](## "<node_type_keys.key>.node_groups.[].vtep_loopback_ipv4_address") | String |  |  | Format: ipv4 | IPv4 address without mask for VTEP-Loopback.<br>When set, it takes precedence over `vtep_loopback_ipv4_pool`.<br>Note: AVD does not check for validity of the IPv4 address and does not catch duplicates. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vtep_loopback_ipv6_address</samp>](## "<node_type_keys.key>.node_groups.[].vtep_loopback_ipv6_address") | String |  |  | Format: ipv6 | IPv6 address without mask for VTEP-Loopback.<br>When set, it takes precedence over `vtep_loopback_ipv6_pool`.<br>Note: AVD does not check for validity of the IPv6 address and does not catch duplicates. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loopback_ipv4_offset</samp>](## "<node_type_keys.key>.node_groups.[].loopback_ipv4_offset") | Integer |  | `0` |  | Offset all assigned loopback IP addresses.<br>Required when the 'loopback_ipv4_pool' is the same for 2 different node_types (like spine and l3leaf) to avoid overlapping IPs.<br>For example, set the minimum offset l3leaf.defaults.loopback_ipv4_offset: < total # spine switches > or vice versa.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;router_id_pool</samp>](## "<node_type_keys.key>.node_groups.[].router_id_pool") | String |  |  | Format: ipv4_pool | Required when underlay_ipv6_numbered is used to configured an IPv6 underlay and IPv6 overlay. router_id_pool is an IPv4 subnet used only for allocation of BGP router-id's since an IPv4 address will not exist on the device. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loopback_ipv6_pool</samp>](## "<node_type_keys.key>.node_groups.[].loopback_ipv6_pool") | String |  |  | Format: ipv6_pool | Comma separated list of prefixes (IPv6 address/Mask) or ranges (IPv6_address-IPv6_address). The IPv6 address used for Loopback0 will be derived from this pool based on the node id and 'loopback_ipv6_offset'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loopback_ipv6_offset</samp>](## "<node_type_keys.key>.node_groups.[].loopback_ipv6_offset") | Integer |  | `0` |  | Offset all assigned loopback IPv6 addresses.<br>Required when the 'loopback_ipv6_pool' is same for 2 different node_types (like spine and l3leaf) to avoid overlapping IPs.<br>For example, set the minimum offset l3leaf.defaults.loopback_ipv6_offset: < total # spine switches > or vice versa.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vtep</samp>](## "<node_type_keys.key>.node_groups.[].vtep") | Boolean |  |  |  | Node is configured as a VTEP when applicable based on 'overlay_routing_protocol'.<br>Overrides VTEP setting inherited from node_type_keys. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vtep_loopback</samp>](## "<node_type_keys.key>.node_groups.[].vtep_loopback") | String |  |  | Pattern: `Loopback[\d/]+` | Set VXLAN source interface. |
    | [<samp>&nbsp;&nbsp;nodes</samp>](## "<node_type_keys.key>.nodes") | List, items: Dictionary |  |  |  | Define variables per node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "<node_type_keys.key>.nodes.[].name") | String | Required, Unique |  |  | The Node Name is used as "hostname". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loopback_ipv4_pool</samp>](## "<node_type_keys.key>.nodes.[].loopback_ipv4_pool") | String |  |  | Format: ipv4_pool | Comma separated list of prefixes (IPv4 address/Mask) or ranges (IPv4_address-IPv4_address).<br>The IPv4 address used for Loopback0 will be derived from this pool based on the node id and 'loopback_ipv4_offset'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loopback_ipv4_address</samp>](## "<node_type_keys.key>.nodes.[].loopback_ipv4_address") | String |  |  | Format: ipv4 | IPv4 address without mask for Loopback0.<br>When set, it takes precedence over `loopback_ipv4_pool`.<br>Note: AVD does not check for validity of the IPv4 address and does not catch duplicates. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vtep_loopback_ipv4_pool</samp>](## "<node_type_keys.key>.nodes.[].vtep_loopback_ipv4_pool") | String |  |  | Format: ipv4_pool | Comma separated list of prefixes (IPv4 address/Mask) or ranges (IPv4_address-IPv4_address). The IPv4 address used for VTEP-Loopback will be derived from this pool based on the node id and 'loopback_ipv4_offset'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vtep_loopback_ipv6_pool</samp>](## "<node_type_keys.key>.nodes.[].vtep_loopback_ipv6_pool") | String |  |  | Format: ipv6_pool | Comma separated list of prefixes (IPv6 address/Mask) or ranges (IPv6_address-IPv6_address). The IPv6 address used for VTEP-Loopback will be derived from this pool based on the node id and 'loopback_ipv6_offset'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vtep_loopback_ipv4_address</samp>](## "<node_type_keys.key>.nodes.[].vtep_loopback_ipv4_address") | String |  |  | Format: ipv4 | IPv4 address without mask for VTEP-Loopback.<br>When set, it takes precedence over `vtep_loopback_ipv4_pool`.<br>Note: AVD does not check for validity of the IPv4 address and does not catch duplicates. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vtep_loopback_ipv6_address</samp>](## "<node_type_keys.key>.nodes.[].vtep_loopback_ipv6_address") | String |  |  | Format: ipv6 | IPv6 address without mask for VTEP-Loopback.<br>When set, it takes precedence over `vtep_loopback_ipv6_pool`.<br>Note: AVD does not check for validity of the IPv6 address and does not catch duplicates. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loopback_ipv4_offset</samp>](## "<node_type_keys.key>.nodes.[].loopback_ipv4_offset") | Integer |  | `0` |  | Offset all assigned loopback IP addresses.<br>Required when the 'loopback_ipv4_pool' is the same for 2 different node_types (like spine and l3leaf) to avoid overlapping IPs.<br>For example, set the minimum offset l3leaf.defaults.loopback_ipv4_offset: < total # spine switches > or vice versa.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;router_id_pool</samp>](## "<node_type_keys.key>.nodes.[].router_id_pool") | String |  |  | Format: ipv4_pool | Required when underlay_ipv6_numbered is used to configured an IPv6 underlay and IPv6 overlay. router_id_pool is an IPv4 subnet used only for allocation of BGP router-id's since an IPv4 address will not exist on the device. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loopback_ipv6_pool</samp>](## "<node_type_keys.key>.nodes.[].loopback_ipv6_pool") | String |  |  | Format: ipv6_pool | Comma separated list of prefixes (IPv6 address/Mask) or ranges (IPv6_address-IPv6_address). The IPv6 address used for Loopback0 will be derived from this pool based on the node id and 'loopback_ipv6_offset'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loopback_ipv6_offset</samp>](## "<node_type_keys.key>.nodes.[].loopback_ipv6_offset") | Integer |  | `0` |  | Offset all assigned loopback IPv6 addresses.<br>Required when the 'loopback_ipv6_pool' is same for 2 different node_types (like spine and l3leaf) to avoid overlapping IPs.<br>For example, set the minimum offset l3leaf.defaults.loopback_ipv6_offset: < total # spine switches > or vice versa.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vtep</samp>](## "<node_type_keys.key>.nodes.[].vtep") | Boolean |  |  |  | Node is configured as a VTEP when applicable based on 'overlay_routing_protocol'.<br>Overrides VTEP setting inherited from node_type_keys. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vtep_loopback</samp>](## "<node_type_keys.key>.nodes.[].vtep_loopback") | String |  |  | Pattern: `Loopback[\d/]+` | Set VXLAN source interface. |
    | [<samp>fabric_ip_addressing</samp>](## "fabric_ip_addressing") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;loopback</samp>](## "fabric_ip_addressing.loopback") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_prefix_length</samp>](## "fabric_ip_addressing.loopback.ipv6_prefix_length") | Integer |  | `128` | Valid Values:<br>- <code>64</code><br>- <code>128</code> | IPv6 prefix length used for Router ID, VTEP and diagnostic loopbacks. |

=== "YAML"

    ```yaml
    <node_type_keys.key>:

      # Define variables for all nodes of this type.
      defaults:

        # Comma separated list of prefixes (IPv4 address/Mask) or ranges (IPv4_address-IPv4_address).
        # The IPv4 address used for Loopback0 will be derived from this pool based on the node id and 'loopback_ipv4_offset'.
        loopback_ipv4_pool: <str>

        # IPv4 address without mask for Loopback0.
        # When set, it takes precedence over `loopback_ipv4_pool`.
        # Note: AVD does not check for validity of the IPv4 address and does not catch duplicates.
        loopback_ipv4_address: <str>

        # Comma separated list of prefixes (IPv4 address/Mask) or ranges (IPv4_address-IPv4_address). The IPv4 address used for VTEP-Loopback will be derived from this pool based on the node id and 'loopback_ipv4_offset'.
        vtep_loopback_ipv4_pool: <str>

        # Comma separated list of prefixes (IPv6 address/Mask) or ranges (IPv6_address-IPv6_address). The IPv6 address used for VTEP-Loopback will be derived from this pool based on the node id and 'loopback_ipv6_offset'.
        vtep_loopback_ipv6_pool: <str>

        # IPv4 address without mask for VTEP-Loopback.
        # When set, it takes precedence over `vtep_loopback_ipv4_pool`.
        # Note: AVD does not check for validity of the IPv4 address and does not catch duplicates.
        vtep_loopback_ipv4_address: <str>

        # IPv6 address without mask for VTEP-Loopback.
        # When set, it takes precedence over `vtep_loopback_ipv6_pool`.
        # Note: AVD does not check for validity of the IPv6 address and does not catch duplicates.
        vtep_loopback_ipv6_address: <str>

        # Offset all assigned loopback IP addresses.
        # Required when the 'loopback_ipv4_pool' is the same for 2 different node_types (like spine and l3leaf) to avoid overlapping IPs.
        # For example, set the minimum offset l3leaf.defaults.loopback_ipv4_offset: < total # spine switches > or vice versa.
        loopback_ipv4_offset: <int; default=0>

        # Required when underlay_ipv6_numbered is used to configured an IPv6 underlay and IPv6 overlay. router_id_pool is an IPv4 subnet used only for allocation of BGP router-id's since an IPv4 address will not exist on the device.
        router_id_pool: <str>

        # Comma separated list of prefixes (IPv6 address/Mask) or ranges (IPv6_address-IPv6_address). The IPv6 address used for Loopback0 will be derived from this pool based on the node id and 'loopback_ipv6_offset'.
        loopback_ipv6_pool: <str>

        # Offset all assigned loopback IPv6 addresses.
        # Required when the 'loopback_ipv6_pool' is same for 2 different node_types (like spine and l3leaf) to avoid overlapping IPs.
        # For example, set the minimum offset l3leaf.defaults.loopback_ipv6_offset: < total # spine switches > or vice versa.
        loopback_ipv6_offset: <int; default=0>

        # Node is configured as a VTEP when applicable based on 'overlay_routing_protocol'.
        # Overrides VTEP setting inherited from node_type_keys.
        vtep: <bool>

        # Set VXLAN source interface.
        vtep_loopback: <str>

      # Define variables related to all nodes part of this group.
      node_groups:

          # The Node Group Name is used for MLAG domain unless set with 'mlag_domain_id'.
          # The Node Group Name is also used for peer description on downstream switches' uplinks.
        - group: <str; required; unique>

          # Define variables per node.
          nodes:

              # The Node Name is used as "hostname".
            - name: <str; required; unique>

              # Comma separated list of prefixes (IPv4 address/Mask) or ranges (IPv4_address-IPv4_address).
              # The IPv4 address used for Loopback0 will be derived from this pool based on the node id and 'loopback_ipv4_offset'.
              loopback_ipv4_pool: <str>

              # IPv4 address without mask for Loopback0.
              # When set, it takes precedence over `loopback_ipv4_pool`.
              # Note: AVD does not check for validity of the IPv4 address and does not catch duplicates.
              loopback_ipv4_address: <str>

              # Comma separated list of prefixes (IPv4 address/Mask) or ranges (IPv4_address-IPv4_address). The IPv4 address used for VTEP-Loopback will be derived from this pool based on the node id and 'loopback_ipv4_offset'.
              vtep_loopback_ipv4_pool: <str>

              # Comma separated list of prefixes (IPv6 address/Mask) or ranges (IPv6_address-IPv6_address). The IPv6 address used for VTEP-Loopback will be derived from this pool based on the node id and 'loopback_ipv6_offset'.
              vtep_loopback_ipv6_pool: <str>

              # IPv4 address without mask for VTEP-Loopback.
              # When set, it takes precedence over `vtep_loopback_ipv4_pool`.
              # Note: AVD does not check for validity of the IPv4 address and does not catch duplicates.
              vtep_loopback_ipv4_address: <str>

              # IPv6 address without mask for VTEP-Loopback.
              # When set, it takes precedence over `vtep_loopback_ipv6_pool`.
              # Note: AVD does not check for validity of the IPv6 address and does not catch duplicates.
              vtep_loopback_ipv6_address: <str>

              # Offset all assigned loopback IP addresses.
              # Required when the 'loopback_ipv4_pool' is the same for 2 different node_types (like spine and l3leaf) to avoid overlapping IPs.
              # For example, set the minimum offset l3leaf.defaults.loopback_ipv4_offset: < total # spine switches > or vice versa.
              loopback_ipv4_offset: <int; default=0>

              # Required when underlay_ipv6_numbered is used to configured an IPv6 underlay and IPv6 overlay. router_id_pool is an IPv4 subnet used only for allocation of BGP router-id's since an IPv4 address will not exist on the device.
              router_id_pool: <str>

              # Comma separated list of prefixes (IPv6 address/Mask) or ranges (IPv6_address-IPv6_address). The IPv6 address used for Loopback0 will be derived from this pool based on the node id and 'loopback_ipv6_offset'.
              loopback_ipv6_pool: <str>

              # Offset all assigned loopback IPv6 addresses.
              # Required when the 'loopback_ipv6_pool' is same for 2 different node_types (like spine and l3leaf) to avoid overlapping IPs.
              # For example, set the minimum offset l3leaf.defaults.loopback_ipv6_offset: < total # spine switches > or vice versa.
              loopback_ipv6_offset: <int; default=0>

              # Node is configured as a VTEP when applicable based on 'overlay_routing_protocol'.
              # Overrides VTEP setting inherited from node_type_keys.
              vtep: <bool>

              # Set VXLAN source interface.
              vtep_loopback: <str>

          # Comma separated list of prefixes (IPv4 address/Mask) or ranges (IPv4_address-IPv4_address).
          # The IPv4 address used for Loopback0 will be derived from this pool based on the node id and 'loopback_ipv4_offset'.
          loopback_ipv4_pool: <str>

          # IPv4 address without mask for Loopback0.
          # When set, it takes precedence over `loopback_ipv4_pool`.
          # Note: AVD does not check for validity of the IPv4 address and does not catch duplicates.
          loopback_ipv4_address: <str>

          # Comma separated list of prefixes (IPv4 address/Mask) or ranges (IPv4_address-IPv4_address). The IPv4 address used for VTEP-Loopback will be derived from this pool based on the node id and 'loopback_ipv4_offset'.
          vtep_loopback_ipv4_pool: <str>

          # Comma separated list of prefixes (IPv6 address/Mask) or ranges (IPv6_address-IPv6_address). The IPv6 address used for VTEP-Loopback will be derived from this pool based on the node id and 'loopback_ipv6_offset'.
          vtep_loopback_ipv6_pool: <str>

          # IPv4 address without mask for VTEP-Loopback.
          # When set, it takes precedence over `vtep_loopback_ipv4_pool`.
          # Note: AVD does not check for validity of the IPv4 address and does not catch duplicates.
          vtep_loopback_ipv4_address: <str>

          # IPv6 address without mask for VTEP-Loopback.
          # When set, it takes precedence over `vtep_loopback_ipv6_pool`.
          # Note: AVD does not check for validity of the IPv6 address and does not catch duplicates.
          vtep_loopback_ipv6_address: <str>

          # Offset all assigned loopback IP addresses.
          # Required when the 'loopback_ipv4_pool' is the same for 2 different node_types (like spine and l3leaf) to avoid overlapping IPs.
          # For example, set the minimum offset l3leaf.defaults.loopback_ipv4_offset: < total # spine switches > or vice versa.
          loopback_ipv4_offset: <int; default=0>

          # Required when underlay_ipv6_numbered is used to configured an IPv6 underlay and IPv6 overlay. router_id_pool is an IPv4 subnet used only for allocation of BGP router-id's since an IPv4 address will not exist on the device.
          router_id_pool: <str>

          # Comma separated list of prefixes (IPv6 address/Mask) or ranges (IPv6_address-IPv6_address). The IPv6 address used for Loopback0 will be derived from this pool based on the node id and 'loopback_ipv6_offset'.
          loopback_ipv6_pool: <str>

          # Offset all assigned loopback IPv6 addresses.
          # Required when the 'loopback_ipv6_pool' is same for 2 different node_types (like spine and l3leaf) to avoid overlapping IPs.
          # For example, set the minimum offset l3leaf.defaults.loopback_ipv6_offset: < total # spine switches > or vice versa.
          loopback_ipv6_offset: <int; default=0>

          # Node is configured as a VTEP when applicable based on 'overlay_routing_protocol'.
          # Overrides VTEP setting inherited from node_type_keys.
          vtep: <bool>

          # Set VXLAN source interface.
          vtep_loopback: <str>

      # Define variables per node.
      nodes:

          # The Node Name is used as "hostname".
        - name: <str; required; unique>

          # Comma separated list of prefixes (IPv4 address/Mask) or ranges (IPv4_address-IPv4_address).
          # The IPv4 address used for Loopback0 will be derived from this pool based on the node id and 'loopback_ipv4_offset'.
          loopback_ipv4_pool: <str>

          # IPv4 address without mask for Loopback0.
          # When set, it takes precedence over `loopback_ipv4_pool`.
          # Note: AVD does not check for validity of the IPv4 address and does not catch duplicates.
          loopback_ipv4_address: <str>

          # Comma separated list of prefixes (IPv4 address/Mask) or ranges (IPv4_address-IPv4_address). The IPv4 address used for VTEP-Loopback will be derived from this pool based on the node id and 'loopback_ipv4_offset'.
          vtep_loopback_ipv4_pool: <str>

          # Comma separated list of prefixes (IPv6 address/Mask) or ranges (IPv6_address-IPv6_address). The IPv6 address used for VTEP-Loopback will be derived from this pool based on the node id and 'loopback_ipv6_offset'.
          vtep_loopback_ipv6_pool: <str>

          # IPv4 address without mask for VTEP-Loopback.
          # When set, it takes precedence over `vtep_loopback_ipv4_pool`.
          # Note: AVD does not check for validity of the IPv4 address and does not catch duplicates.
          vtep_loopback_ipv4_address: <str>

          # IPv6 address without mask for VTEP-Loopback.
          # When set, it takes precedence over `vtep_loopback_ipv6_pool`.
          # Note: AVD does not check for validity of the IPv6 address and does not catch duplicates.
          vtep_loopback_ipv6_address: <str>

          # Offset all assigned loopback IP addresses.
          # Required when the 'loopback_ipv4_pool' is the same for 2 different node_types (like spine and l3leaf) to avoid overlapping IPs.
          # For example, set the minimum offset l3leaf.defaults.loopback_ipv4_offset: < total # spine switches > or vice versa.
          loopback_ipv4_offset: <int; default=0>

          # Required when underlay_ipv6_numbered is used to configured an IPv6 underlay and IPv6 overlay. router_id_pool is an IPv4 subnet used only for allocation of BGP router-id's since an IPv4 address will not exist on the device.
          router_id_pool: <str>

          # Comma separated list of prefixes (IPv6 address/Mask) or ranges (IPv6_address-IPv6_address). The IPv6 address used for Loopback0 will be derived from this pool based on the node id and 'loopback_ipv6_offset'.
          loopback_ipv6_pool: <str>

          # Offset all assigned loopback IPv6 addresses.
          # Required when the 'loopback_ipv6_pool' is same for 2 different node_types (like spine and l3leaf) to avoid overlapping IPs.
          # For example, set the minimum offset l3leaf.defaults.loopback_ipv6_offset: < total # spine switches > or vice versa.
          loopback_ipv6_offset: <int; default=0>

          # Node is configured as a VTEP when applicable based on 'overlay_routing_protocol'.
          # Overrides VTEP setting inherited from node_type_keys.
          vtep: <bool>

          # Set VXLAN source interface.
          vtep_loopback: <str>
    fabric_ip_addressing:
      loopback:

        # IPv6 prefix length used for Router ID, VTEP and diagnostic loopbacks.
        ipv6_prefix_length: <int; 64 | 128; default=128>
    ```
