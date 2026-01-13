<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>ip_http_client</samp>](## "ip_http_client") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;source_interface</samp>](## "ip_http_client.source_interface") | String |  |  |  | Define `source_interface` for VRF default. |
    | [<samp>&nbsp;&nbsp;vrfs</samp>](## "ip_http_client.vrfs") | List, items: Dictionary |  |  |  | Define `source interfaces` for any VRF other than default. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "ip_http_client.vrfs.[].name") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_interface</samp>](## "ip_http_client.vrfs.[].source_interface") | String | Required |  |  |  |
    | [<samp>ip_http_client_source_interfaces</samp>](## "ip_http_client_source_interfaces") <span style="color:red">removed</span> | List |  |  |  | <span style="color:red">This key was removed. Support was removed in AVD version 6.0.0. Use <samp>ip_http_client</samp> instead.</span> |

=== "YAML"

    ```yaml
    ip_http_client:

      # Define `source_interface` for VRF default.
      source_interface: <str>

      # Define `source interfaces` for any VRF other than default.
      vrfs:
        - name: <str; required; unique>
          source_interface: <str; required>
    ```
