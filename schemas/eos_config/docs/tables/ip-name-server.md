<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>ip_name_server</samp>](## "ip_name_server") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;vrfs</samp>](## "ip_name_server.vrfs") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "ip_name_server.vrfs.[].name") | String | Required, Unique |  |  | VRF Name.<br>Use "default" for the default VRF. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;servers</samp>](## "ip_name_server.vrfs.[].servers") | List, items: Dictionary | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;ip_address</samp>](## "ip_name_server.vrfs.[].servers.[].ip_address") | String | Required, Unique |  |  | IPv4 or IPv6 address for DNS server. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority</samp>](## "ip_name_server.vrfs.[].servers.[].priority") | Integer |  |  | Min: 0<br>Max: 4 | Priority value (lower is first). |
    | [<samp>ip_name_servers</samp>](## "ip_name_servers") <span style="color:red">removed</span> | List |  |  |  | <span style="color:red">This key was removed. Support was removed in AVD version 6.0.0. Use <samp>ip_name_server</samp> instead.</span> |

=== "YAML"

    ```yaml
    ip_name_server:
      vrfs:

          # VRF Name.
          # Use "default" for the default VRF.
        - name: <str; required; unique>
          servers: # required

              # IPv4 or IPv6 address for DNS server.
            - ip_address: <str; required; unique>

              # Priority value (lower is first).
              priority: <int; 0-4>
    ```
