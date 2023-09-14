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
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;bgp_as</samp>](## "&lt;node_type_keys.key&gt;.defaults.bgp_as") | String |  |  |  | Required with eBGP. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;bgp_defaults</samp>](## "&lt;node_type_keys.key&gt;.defaults.bgp_defaults") | List, items: String |  |  |  | List of EOS commands to apply to BGP daemon. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.defaults.bgp_defaults.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;evpn_role</samp>](## "&lt;node_type_keys.key&gt;.defaults.evpn_role") | String |  |  | Valid Values:<br>- client<br>- server<br>- none | Acting role in EVPN control plane.<br>Default is set in node_type definition from node_type_keys.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;evpn_route_servers</samp>](## "&lt;node_type_keys.key&gt;.defaults.evpn_route_servers") | List, items: String |  |  |  | List of nodes acting as EVPN Route-Servers / Route-Reflectors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.defaults.evpn_route_servers.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;node_groups</samp>](## "&lt;node_type_keys.key&gt;.node_groups") | List, items: Dictionary |  |  |  | Define variables related to all nodes part of this group. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- group</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].group") | String | Required, Unique |  |  | The Node Group Name is used for MLAG domain unless set with 'mlag_domain_id'.<br>The Node Group Name is also used for peer description on downstream switches' uplinks.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes") | List, items: Dictionary |  |  |  | Define variables per node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].name") | String | Required, Unique |  |  | The Node Name is used as "hostname". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp_as</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].bgp_as") | String |  |  |  | Required with eBGP. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp_defaults</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].bgp_defaults") | List, items: String |  |  |  | List of EOS commands to apply to BGP daemon. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].bgp_defaults.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_role</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].evpn_role") | String |  |  | Valid Values:<br>- client<br>- server<br>- none | Acting role in EVPN control plane.<br>Default is set in node_type definition from node_type_keys.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_route_servers</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].evpn_route_servers") | List, items: String |  |  |  | List of nodes acting as EVPN Route-Servers / Route-Reflectors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].evpn_route_servers.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp_as</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].bgp_as") | String |  |  |  | Required with eBGP. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp_defaults</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].bgp_defaults") | List, items: String |  |  |  | List of EOS commands to apply to BGP daemon. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].bgp_defaults.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_role</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].evpn_role") | String |  |  | Valid Values:<br>- client<br>- server<br>- none | Acting role in EVPN control plane.<br>Default is set in node_type definition from node_type_keys.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_route_servers</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].evpn_route_servers") | List, items: String |  |  |  | List of nodes acting as EVPN Route-Servers / Route-Reflectors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].evpn_route_servers.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;nodes</samp>](## "&lt;node_type_keys.key&gt;.nodes") | List, items: Dictionary |  |  |  | Define variables per node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].name") | String | Required, Unique |  |  | The Node Name is used as "hostname". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp_as</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].bgp_as") | String |  |  |  | Required with eBGP. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp_defaults</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].bgp_defaults") | List, items: String |  |  |  | List of EOS commands to apply to BGP daemon. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].bgp_defaults.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_role</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].evpn_role") | String |  |  | Valid Values:<br>- client<br>- server<br>- none | Acting role in EVPN control plane.<br>Default is set in node_type definition from node_type_keys.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_route_servers</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].evpn_route_servers") | List, items: String |  |  |  | List of nodes acting as EVPN Route-Servers / Route-Reflectors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].evpn_route_servers.[].&lt;str&gt;") | String |  |  |  |  |

=== "YAML"

    ```yaml
    <node_type_keys.key>:
      defaults:
        bgp_as: <str>
        bgp_defaults:
          - <str>
        evpn_role: <str>
        evpn_route_servers:
          - <str>
      node_groups:
        - group: <str>
          nodes:
            - name: <str>
              bgp_as: <str>
              bgp_defaults:
                - <str>
              evpn_role: <str>
              evpn_route_servers:
                - <str>
          bgp_as: <str>
          bgp_defaults:
            - <str>
          evpn_role: <str>
          evpn_route_servers:
            - <str>
      nodes:
        - name: <str>
          bgp_as: <str>
          bgp_defaults:
            - <str>
          evpn_role: <str>
          evpn_route_servers:
            - <str>
    ```
