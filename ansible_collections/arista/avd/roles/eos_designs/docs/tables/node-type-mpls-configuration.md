<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>&lt;node_type_keys.key&gt;</samp>](## "&lt;node_type_keys.key&gt;") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;defaults</samp>](## "&lt;node_type_keys.key&gt;.defaults") | Dictionary |  |  |  | Define variables for all nodes of this type. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mpls_overlay_role</samp>](## "&lt;node_type_keys.key&gt;.defaults.mpls_overlay_role") | String |  |  | Valid Values:<br>- client<br>- server<br>- none | Set the default mpls overlay role.<br>Acting role in overlay control plane.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;overlay_address_families</samp>](## "&lt;node_type_keys.key&gt;.defaults.overlay_address_families") | List, items: String |  |  |  | Set the default overlay address families.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.defaults.overlay_address_families.[].&lt;str&gt;") | String |  |  | Valid Values:<br>- evpn<br>- vpn-ipv4<br>- vpn-ipv6 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mpls_route_reflectors</samp>](## "&lt;node_type_keys.key&gt;.defaults.mpls_route_reflectors") | List, items: String |  |  |  | List of inventory hostname acting as MPLS route-reflectors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.defaults.mpls_route_reflectors.[].&lt;str&gt;") | String |  |  |  | Inventory_hostname_of_mpls_route_reflectors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;bgp_cluster_id</samp>](## "&lt;node_type_keys.key&gt;.defaults.bgp_cluster_id") | String |  |  |  | Set BGP cluster id. |
    | [<samp>&nbsp;&nbsp;node_groups</samp>](## "&lt;node_type_keys.key&gt;.node_groups") | List, items: Dictionary |  |  |  | Define variables related to all nodes part of this group. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- group</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].group") | String | Required, Unique |  |  | The Node Group Name is used for MLAG domain unless set with 'mlag_domain_id'.<br>The Node Group Name is also used for peer description on downstream switches' uplinks.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes") | List, items: Dictionary |  |  |  | Define variables per node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].name") | String | Required, Unique |  |  | The Node Name is used as "hostname". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mpls_overlay_role</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].mpls_overlay_role") | String |  |  | Valid Values:<br>- client<br>- server<br>- none | Set the default mpls overlay role.<br>Acting role in overlay control plane.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;overlay_address_families</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].overlay_address_families") | List, items: String |  |  |  | Set the default overlay address families.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].overlay_address_families.[].&lt;str&gt;") | String |  |  | Valid Values:<br>- evpn<br>- vpn-ipv4<br>- vpn-ipv6 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mpls_route_reflectors</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].mpls_route_reflectors") | List, items: String |  |  |  | List of inventory hostname acting as MPLS route-reflectors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].mpls_route_reflectors.[].&lt;str&gt;") | String |  |  |  | Inventory_hostname_of_mpls_route_reflectors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp_cluster_id</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].bgp_cluster_id") | String |  |  |  | Set BGP cluster id. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mpls_overlay_role</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].mpls_overlay_role") | String |  |  | Valid Values:<br>- client<br>- server<br>- none | Set the default mpls overlay role.<br>Acting role in overlay control plane.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;overlay_address_families</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].overlay_address_families") | List, items: String |  |  |  | Set the default overlay address families.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].overlay_address_families.[].&lt;str&gt;") | String |  |  | Valid Values:<br>- evpn<br>- vpn-ipv4<br>- vpn-ipv6 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mpls_route_reflectors</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].mpls_route_reflectors") | List, items: String |  |  |  | List of inventory hostname acting as MPLS route-reflectors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].mpls_route_reflectors.[].&lt;str&gt;") | String |  |  |  | Inventory_hostname_of_mpls_route_reflectors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp_cluster_id</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].bgp_cluster_id") | String |  |  |  | Set BGP cluster id. |
    | [<samp>&nbsp;&nbsp;nodes</samp>](## "&lt;node_type_keys.key&gt;.nodes") | List, items: Dictionary |  |  |  | Define variables per node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].name") | String | Required, Unique |  |  | The Node Name is used as "hostname". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mpls_overlay_role</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].mpls_overlay_role") | String |  |  | Valid Values:<br>- client<br>- server<br>- none | Set the default mpls overlay role.<br>Acting role in overlay control plane.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;overlay_address_families</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].overlay_address_families") | List, items: String |  |  |  | Set the default overlay address families.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].overlay_address_families.[].&lt;str&gt;") | String |  |  | Valid Values:<br>- evpn<br>- vpn-ipv4<br>- vpn-ipv6 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mpls_route_reflectors</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].mpls_route_reflectors") | List, items: String |  |  |  | List of inventory hostname acting as MPLS route-reflectors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].mpls_route_reflectors.[].&lt;str&gt;") | String |  |  |  | Inventory_hostname_of_mpls_route_reflectors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp_cluster_id</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].bgp_cluster_id") | String |  |  |  | Set BGP cluster id. |

=== "YAML"

    ```yaml
    <node_type_keys.key>:
      defaults:
        mpls_overlay_role: <str>
        overlay_address_families:
          - <str>
        mpls_route_reflectors:
          - <str>
        bgp_cluster_id: <str>
      node_groups:
        - group: <str>
          nodes:
            - name: <str>
              mpls_overlay_role: <str>
              overlay_address_families:
                - <str>
              mpls_route_reflectors:
                - <str>
              bgp_cluster_id: <str>
          mpls_overlay_role: <str>
          overlay_address_families:
            - <str>
          mpls_route_reflectors:
            - <str>
          bgp_cluster_id: <str>
      nodes:
        - name: <str>
          mpls_overlay_role: <str>
          overlay_address_families:
            - <str>
          mpls_route_reflectors:
            - <str>
          bgp_cluster_id: <str>
    ```
