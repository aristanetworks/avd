<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>ip_radius</samp>](## "ip_radius") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;source_interface</samp>](## "ip_radius.source_interface") | String |  |  |  | Define `source_interface` for VRF default. |
    | [<samp>&nbsp;&nbsp;vrfs</samp>](## "ip_radius.vrfs") | List, items: Dictionary |  |  |  | Define `source interfaces` for any VRF other than default. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "ip_radius.vrfs.[].name") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_interface</samp>](## "ip_radius.vrfs.[].source_interface") | String | Required |  |  |  |
    | [<samp>ip_radius_source_interfaces</samp>](## "ip_radius_source_interfaces") <span style="color:red">deprecated</span> | List, items: Dictionary |  |  |  | <span style="color:red">This key is deprecated. Support will be removed in AVD version 7.0.0. Use <samp>ip_radius</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;-&nbsp;name</samp>](## "ip_radius_source_interfaces.[].name") | String |  |  |  | Interface Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "ip_radius_source_interfaces.[].vrf") | String |  |  |  | VRF Name. |

=== "YAML"

    ```yaml
    ip_radius:

      # Define `source_interface` for VRF default.
      source_interface: <str>

      # Define `source interfaces` for any VRF other than default.
      vrfs:
        - name: <str; required; unique>
          source_interface: <str; required>
    # This key is deprecated.
    # Support will be removed in AVD version 7.0.0.
    # Use `ip_radius` instead.
    ip_radius_source_interfaces:

        # Interface Name.
      - name: <str>

        # VRF Name.
        vrf: <str>
    ```
