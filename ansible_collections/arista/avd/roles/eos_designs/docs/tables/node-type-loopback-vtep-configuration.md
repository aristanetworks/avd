<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>node</samp>](## "node") | Dictionary |  |  |  | This key should _only_ be set in hostvars since it is applied unconditionally and overrides any other setting under the node type keys like `l3leaf` or `spine`.<br>It is useful when generating device setting from other systems and sources, since the values can be set with a static path per device instead of having to insert it into the common `<node_type_key>` data structure.<br>Since MLAG groupings are currently picked up from node_groups with two members, MLAG devices must still be defined under the relevant `<node_type_key>`. |
    | [<samp>&nbsp;&nbsp;loopback_ipv4_pool</samp>](## "node.loopback_ipv4_pool") | String |  |  | Format: ipv4_cidr | IPv4 subnet for Loopback0 allocation. |
    | [<samp>&nbsp;&nbsp;vtep_loopback_ipv4_pool</samp>](## "node.vtep_loopback_ipv4_pool") | String |  |  | Format: ipv4_cidr | IPv4 subnet for VTEP-Loopback allocation. |
    | [<samp>&nbsp;&nbsp;loopback_ipv4_offset</samp>](## "node.loopback_ipv4_offset") | Integer |  | `0` |  | Offset all assigned loopback IP addresses.<br>Required when the < loopback_ipv4_pool > is same for 2 different node_types (like spine and l3leaf) to avoid over-lapping IPs.<br>For example, set the minimum offset l3leaf.defaults.loopback_ipv4_offset: < total # spine switches > or vice versa.<br> |
    | [<samp>&nbsp;&nbsp;loopback_ipv6_pool</samp>](## "node.loopback_ipv6_pool") | String |  |  | Format: ipv6_cidr | IPv6 subnet for Loopback0 allocation. |
    | [<samp>&nbsp;&nbsp;loopback_ipv6_offset</samp>](## "node.loopback_ipv6_offset") | Integer |  | `0` |  | Offset all assigned loopback IPv6 addresses.<br>Required when the < loopback_ipv6_pool > is same for 2 different node_types (like spine and l3leaf) to avoid overlapping IPs.<br>For example, set the minimum offset l3leaf.defaults.loopback_ipv6_offset: < total # spine switches > or vice versa.<br> |
    | [<samp>&nbsp;&nbsp;vtep</samp>](## "node.vtep") | Boolean |  |  |  | Node is configured as a VTEP when applicable based on 'overlay_routing_protocol'.<br>Overrides VTEP setting inherited from node_type_keys. |
    | [<samp>&nbsp;&nbsp;vtep_loopback</samp>](## "node.vtep_loopback") | String |  |  | Pattern: Loopback[\d/]+ | Set VXLAN source interface. |
    | [<samp>&lt;node_type_keys.key&gt;</samp>](## "&lt;node_type_keys.key&gt;") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;defaults</samp>](## "&lt;node_type_keys.key&gt;.defaults") | Dictionary |  |  |  | Define variables for all nodes of this type. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;loopback_ipv4_pool</samp>](## "&lt;node_type_keys.key&gt;.defaults.loopback_ipv4_pool") | String |  |  | Format: ipv4_cidr | IPv4 subnet for Loopback0 allocation. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vtep_loopback_ipv4_pool</samp>](## "&lt;node_type_keys.key&gt;.defaults.vtep_loopback_ipv4_pool") | String |  |  | Format: ipv4_cidr | IPv4 subnet for VTEP-Loopback allocation. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;loopback_ipv4_offset</samp>](## "&lt;node_type_keys.key&gt;.defaults.loopback_ipv4_offset") | Integer |  | `0` |  | Offset all assigned loopback IP addresses.<br>Required when the < loopback_ipv4_pool > is same for 2 different node_types (like spine and l3leaf) to avoid over-lapping IPs.<br>For example, set the minimum offset l3leaf.defaults.loopback_ipv4_offset: < total # spine switches > or vice versa.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;loopback_ipv6_pool</samp>](## "&lt;node_type_keys.key&gt;.defaults.loopback_ipv6_pool") | String |  |  | Format: ipv6_cidr | IPv6 subnet for Loopback0 allocation. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;loopback_ipv6_offset</samp>](## "&lt;node_type_keys.key&gt;.defaults.loopback_ipv6_offset") | Integer |  | `0` |  | Offset all assigned loopback IPv6 addresses.<br>Required when the < loopback_ipv6_pool > is same for 2 different node_types (like spine and l3leaf) to avoid overlapping IPs.<br>For example, set the minimum offset l3leaf.defaults.loopback_ipv6_offset: < total # spine switches > or vice versa.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vtep</samp>](## "&lt;node_type_keys.key&gt;.defaults.vtep") | Boolean |  |  |  | Node is configured as a VTEP when applicable based on 'overlay_routing_protocol'.<br>Overrides VTEP setting inherited from node_type_keys. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vtep_loopback</samp>](## "&lt;node_type_keys.key&gt;.defaults.vtep_loopback") | String |  |  | Pattern: Loopback[\d/]+ | Set VXLAN source interface. |
    | [<samp>&nbsp;&nbsp;node_groups</samp>](## "&lt;node_type_keys.key&gt;.node_groups") | List, items: Dictionary |  |  |  | Define variables related to all nodes part of this group. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- group</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].group") | String | Required, Unique |  |  | The Node Group Name is used for MLAG domain unless set with 'mlag_domain_id'.<br>The Node Group Name is also used for peer description on downstream switches' uplinks.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes") | List, items: Dictionary |  |  |  | Define variables per node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].name") | String | Required, Unique |  |  | The Node Name is used as "hostname". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loopback_ipv4_pool</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].loopback_ipv4_pool") | String |  |  | Format: ipv4_cidr | IPv4 subnet for Loopback0 allocation. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vtep_loopback_ipv4_pool</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].vtep_loopback_ipv4_pool") | String |  |  | Format: ipv4_cidr | IPv4 subnet for VTEP-Loopback allocation. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loopback_ipv4_offset</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].loopback_ipv4_offset") | Integer |  | `0` |  | Offset all assigned loopback IP addresses.<br>Required when the < loopback_ipv4_pool > is same for 2 different node_types (like spine and l3leaf) to avoid over-lapping IPs.<br>For example, set the minimum offset l3leaf.defaults.loopback_ipv4_offset: < total # spine switches > or vice versa.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loopback_ipv6_pool</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].loopback_ipv6_pool") | String |  |  | Format: ipv6_cidr | IPv6 subnet for Loopback0 allocation. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loopback_ipv6_offset</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].loopback_ipv6_offset") | Integer |  | `0` |  | Offset all assigned loopback IPv6 addresses.<br>Required when the < loopback_ipv6_pool > is same for 2 different node_types (like spine and l3leaf) to avoid overlapping IPs.<br>For example, set the minimum offset l3leaf.defaults.loopback_ipv6_offset: < total # spine switches > or vice versa.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vtep</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].vtep") | Boolean |  |  |  | Node is configured as a VTEP when applicable based on 'overlay_routing_protocol'.<br>Overrides VTEP setting inherited from node_type_keys. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vtep_loopback</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].vtep_loopback") | String |  |  | Pattern: Loopback[\d/]+ | Set VXLAN source interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loopback_ipv4_pool</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].loopback_ipv4_pool") | String |  |  | Format: ipv4_cidr | IPv4 subnet for Loopback0 allocation. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vtep_loopback_ipv4_pool</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].vtep_loopback_ipv4_pool") | String |  |  | Format: ipv4_cidr | IPv4 subnet for VTEP-Loopback allocation. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loopback_ipv4_offset</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].loopback_ipv4_offset") | Integer |  | `0` |  | Offset all assigned loopback IP addresses.<br>Required when the < loopback_ipv4_pool > is same for 2 different node_types (like spine and l3leaf) to avoid over-lapping IPs.<br>For example, set the minimum offset l3leaf.defaults.loopback_ipv4_offset: < total # spine switches > or vice versa.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loopback_ipv6_pool</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].loopback_ipv6_pool") | String |  |  | Format: ipv6_cidr | IPv6 subnet for Loopback0 allocation. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loopback_ipv6_offset</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].loopback_ipv6_offset") | Integer |  | `0` |  | Offset all assigned loopback IPv6 addresses.<br>Required when the < loopback_ipv6_pool > is same for 2 different node_types (like spine and l3leaf) to avoid overlapping IPs.<br>For example, set the minimum offset l3leaf.defaults.loopback_ipv6_offset: < total # spine switches > or vice versa.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vtep</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].vtep") | Boolean |  |  |  | Node is configured as a VTEP when applicable based on 'overlay_routing_protocol'.<br>Overrides VTEP setting inherited from node_type_keys. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vtep_loopback</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].vtep_loopback") | String |  |  | Pattern: Loopback[\d/]+ | Set VXLAN source interface. |
    | [<samp>&nbsp;&nbsp;nodes</samp>](## "&lt;node_type_keys.key&gt;.nodes") | List, items: Dictionary |  |  |  | Define variables per node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].name") | String | Required, Unique |  |  | The Node Name is used as "hostname". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loopback_ipv4_pool</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].loopback_ipv4_pool") | String |  |  | Format: ipv4_cidr | IPv4 subnet for Loopback0 allocation. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vtep_loopback_ipv4_pool</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].vtep_loopback_ipv4_pool") | String |  |  | Format: ipv4_cidr | IPv4 subnet for VTEP-Loopback allocation. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loopback_ipv4_offset</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].loopback_ipv4_offset") | Integer |  | `0` |  | Offset all assigned loopback IP addresses.<br>Required when the < loopback_ipv4_pool > is same for 2 different node_types (like spine and l3leaf) to avoid over-lapping IPs.<br>For example, set the minimum offset l3leaf.defaults.loopback_ipv4_offset: < total # spine switches > or vice versa.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loopback_ipv6_pool</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].loopback_ipv6_pool") | String |  |  | Format: ipv6_cidr | IPv6 subnet for Loopback0 allocation. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loopback_ipv6_offset</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].loopback_ipv6_offset") | Integer |  | `0` |  | Offset all assigned loopback IPv6 addresses.<br>Required when the < loopback_ipv6_pool > is same for 2 different node_types (like spine and l3leaf) to avoid overlapping IPs.<br>For example, set the minimum offset l3leaf.defaults.loopback_ipv6_offset: < total # spine switches > or vice versa.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vtep</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].vtep") | Boolean |  |  |  | Node is configured as a VTEP when applicable based on 'overlay_routing_protocol'.<br>Overrides VTEP setting inherited from node_type_keys. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vtep_loopback</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].vtep_loopback") | String |  |  | Pattern: Loopback[\d/]+ | Set VXLAN source interface. |

=== "YAML"

    ```yaml
    node:
      loopback_ipv4_pool: <str>
      vtep_loopback_ipv4_pool: <str>
      loopback_ipv4_offset: <int>
      loopback_ipv6_pool: <str>
      loopback_ipv6_offset: <int>
      vtep: <bool>
      vtep_loopback: <str>
    <node_type_keys.key>:
      defaults:
        loopback_ipv4_pool: <str>
        vtep_loopback_ipv4_pool: <str>
        loopback_ipv4_offset: <int>
        loopback_ipv6_pool: <str>
        loopback_ipv6_offset: <int>
        vtep: <bool>
        vtep_loopback: <str>
      node_groups:
        - group: <str>
          nodes:
            - name: <str>
              loopback_ipv4_pool: <str>
              vtep_loopback_ipv4_pool: <str>
              loopback_ipv4_offset: <int>
              loopback_ipv6_pool: <str>
              loopback_ipv6_offset: <int>
              vtep: <bool>
              vtep_loopback: <str>
          loopback_ipv4_pool: <str>
          vtep_loopback_ipv4_pool: <str>
          loopback_ipv4_offset: <int>
          loopback_ipv6_pool: <str>
          loopback_ipv6_offset: <int>
          vtep: <bool>
          vtep_loopback: <str>
      nodes:
        - name: <str>
          loopback_ipv4_pool: <str>
          vtep_loopback_ipv4_pool: <str>
          loopback_ipv4_offset: <int>
          loopback_ipv6_pool: <str>
          loopback_ipv6_offset: <int>
          vtep: <bool>
          vtep_loopback: <str>
    ```
