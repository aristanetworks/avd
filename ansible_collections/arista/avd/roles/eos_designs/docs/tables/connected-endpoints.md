<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp><connected_endpoints_keys.key></samp>](## "<connected_endpoints_keys.key>") | List, items: Dictionary |  |  |  | This should be applied to group_vars or host_vars where endpoints are connecting.<br>`connected_endpoints_keys.key` is one of the keys under "connected_endpoints_keys".<br>The default keys are `servers`, `firewalls`, `routers`, `load_balancers`, and `storage_arrays`.<br> |
    | [<samp>&nbsp;&nbsp;- name</samp>](## "<connected_endpoints_keys.key>.[].name") | String | Required, Unique |  |  | Endpoint name will be used in the switchport description. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;rack</samp>](## "<connected_endpoints_keys.key>.[].rack") | String |  |  |  | Rack is used for documentation purposes only. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;adapters</samp>](## "<connected_endpoints_keys.key>.[].adapters") | List, items: Dictionary |  |  |  | A list of adapters, group by adapters leveraging the same port-profile. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- switch_ports</samp>](## "<connected_endpoints_keys.key>.[].adapters.[].switch_ports") | List, items: String | Required |  |  | List of switch interfaces.<br>The lists `endpoint_ports`, `switch_ports`, and `switches` must have the same length.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "<connected_endpoints_keys.key>.[].adapters.[].switch_ports.[].&lt;str&gt;") | String |  |  |  | Switchport interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;switches</samp>](## "<connected_endpoints_keys.key>.[].adapters.[].switches") | List, items: String | Required |  |  | List of switches.<br>The lists `endpoint_ports`, `switch_ports`, and `switches` must have the same length.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "<connected_endpoints_keys.key>.[].adapters.[].switches.[].&lt;str&gt;") | String |  |  |  | Device |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;endpoint_ports</samp>](## "<connected_endpoints_keys.key>.[].adapters.[].endpoint_ports") | List, items: String |  |  |  | Endpoint ports is used for description, required unless `description` or `descriptions` is set.<br>The lists `endpoint_ports`, `switch_ports`, `descriptions` and `switches` must have the same length.<br>Each list item is one switchport.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "<connected_endpoints_keys.key>.[].adapters.[].endpoint_ports.[].&lt;str&gt;") | String |  |  |  | Interface name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;descriptions</samp>](## "<connected_endpoints_keys.key>.[].adapters.[].descriptions") | List |  |  |  | Unique description per port. When set, takes priority over description.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;server_ports</samp>](## "<connected_endpoints_keys.key>.[].adapters.[].server_ports") <span style="color:red">removed</span> | List, items: String |  |  |  | <span style="color:red">This key was removed. Support was removed in AVD version 4.0.0. Use <samp>endpoint_ports</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "<connected_endpoints_keys.key>.[].adapters.[].server_ports.[].&lt;str&gt;") | String |  |  |  | Used for documentation purposes. |

=== "YAML"

    ```yaml
    <connected_endpoints_keys.key>:
      - name: <str>
        rack: <str>
        adapters:
          - switch_ports:
              - <str>
            switches:
              - <str>
            endpoint_ports:
              - <str>
            descriptions:
    ```
