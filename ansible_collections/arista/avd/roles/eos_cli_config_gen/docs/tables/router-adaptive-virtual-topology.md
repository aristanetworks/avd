<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>router_adaptive_virtual_topology</samp>](## "router_adaptive_virtual_topology") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;topology_role</samp>](## "router_adaptive_virtual_topology.topology_role") | String |  |  | Valid Values:<br>- edge<br>- pathfinder<br>- transit region<br>- transit zone | Role name. |
    | [<samp>&nbsp;&nbsp;region</samp>](## "router_adaptive_virtual_topology.region") | Dictionary |  |  |  | Region name and ID. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "router_adaptive_virtual_topology.region.name") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;id</samp>](## "router_adaptive_virtual_topology.region.id") | Integer | Required |  | Min: 1<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;zone</samp>](## "router_adaptive_virtual_topology.zone") | Dictionary |  |  |  | Zone name and ID. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "router_adaptive_virtual_topology.zone.name") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;id</samp>](## "router_adaptive_virtual_topology.zone.id") | Integer | Required |  | Min: 1<br>Max: 10000 |  |
    | [<samp>&nbsp;&nbsp;site</samp>](## "router_adaptive_virtual_topology.site") | Dictionary |  |  |  | Site name and ID. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "router_adaptive_virtual_topology.site.name") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;id</samp>](## "router_adaptive_virtual_topology.site.id") | Integer | Required |  | Min: 1<br>Max: 10000 |  |

=== "YAML"

    ```yaml
    router_adaptive_virtual_topology:
      topology_role: <str>
      region:
        name: <str>
        id: <int>
      zone:
        name: <str>
        id: <int>
      site:
        name: <str>
        id: <int>
    ```
