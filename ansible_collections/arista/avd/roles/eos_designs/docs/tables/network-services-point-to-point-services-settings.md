<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>&lt;network_services_keys.name&gt;</samp>](## "&lt;network_services_keys.name&gt;") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;- name</samp>](## "&lt;network_services_keys.name&gt;.[].name") | String | Required, Unique |  |  | Specify a tenant name.<br>Tenant provide a construct to group L3 VRFs and L2 VLANs.<br>Networks services can be filtered by tenant name.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;pseudowire_rt_base</samp>](## "&lt;network_services_keys.name&gt;.[].pseudowire_rt_base") | Integer |  |  |  | Pseudowire RT base, used to generate route targets for VPWS services.<br>Avoid overlapping route target spaces between different services.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;point_to_point_services</samp>](## "&lt;network_services_keys.name&gt;.[].point_to_point_services") | List, items: Dictionary |  |  |  | Point to point services (pseudowires).<br>Only supported for node types with "network_services.l1: true".<br>By default this is only set for node type "pe" with "design.type: mpls"<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "&lt;network_services_keys.name&gt;.[].point_to_point_services.[].name") | String | Required, Unique |  |  | Pseudowire name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "&lt;network_services_keys.name&gt;.[].point_to_point_services.[].type") | String |  | `vpws-pseudowire` | Valid Values:<br>- vpws-pseudowire |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;subinterfaces</samp>](## "&lt;network_services_keys.name&gt;.[].point_to_point_services.[].subinterfaces") | List, items: Dictionary |  |  |  | Subinterfaces will create subinterfaces and additional pseudowires/patch panel config for each endpoint. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- number</samp>](## "&lt;network_services_keys.name&gt;.[].point_to_point_services.[].subinterfaces.[].number") | Integer | Required, Unique |  |  | Subinterface number |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;endpoints</samp>](## "&lt;network_services_keys.name&gt;.[].point_to_point_services.[].endpoints") | List, items: Dictionary |  |  | Min Length: 2<br>Max Length: 2 | Pseudowire terminating endpoints. Must have exactly two items. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- id</samp>](## "&lt;network_services_keys.name&gt;.[].point_to_point_services.[].endpoints.[].id") | Integer | Required |  |  | Pseudowire ID on this endpoint. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "&lt;network_services_keys.name&gt;.[].point_to_point_services.[].endpoints.[].nodes") | List, items: String | Required |  | Min Length: 1 | Usually one node. With ESI multihoming we support two nodes per pseudowire endpoint |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;network_services_keys.name&gt;.[].point_to_point_services.[].endpoints.[].nodes.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interfaces</samp>](## "&lt;network_services_keys.name&gt;.[].point_to_point_services.[].endpoints.[].interfaces") | List, items: String | Required |  | Min Length: 1 | Interfaces patched to the pseudowire on this endpoints.<br>The list of interfaces is mapped to the list of nodes, so they must have the same length.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;network_services_keys.name&gt;.[].point_to_point_services.[].endpoints.[].interfaces.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;port_channel</samp>](## "&lt;network_services_keys.name&gt;.[].point_to_point_services.[].endpoints.[].port_channel") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "&lt;network_services_keys.name&gt;.[].point_to_point_services.[].endpoints.[].port_channel.mode") | String |  |  | Valid Values:<br>- active<br>- on |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;short_esi</samp>](## "&lt;network_services_keys.name&gt;.[].point_to_point_services.[].endpoints.[].port_channel.short_esi") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;lldp_disable</samp>](## "&lt;network_services_keys.name&gt;.[].point_to_point_services.[].lldp_disable") | Boolean |  |  |  | Disable LLDP RX/TX on port mode pseudowire services. |

=== "YAML"

    ```yaml
    <network_services_keys.name>:
      - name: <str>
        pseudowire_rt_base: <int>
        point_to_point_services:
          - name: <str>
            type: <str>
            subinterfaces:
              - number: <int>
            endpoints:
              - id: <int>
                nodes:
                  - <str>
                interfaces:
                  - <str>
                port_channel:
                  mode: <str>
                  short_esi: <str>
            lldp_disable: <bool>
    ```
