<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>ip_tacacs</samp>](## "ip_tacacs") | Dictionary |  |  |  | IP TACACS source interface configuration.<br>This requires to set the 'eos_config_future.new_ip_tacacs_cli_order: true' to render the new CLI order. |
    | [<samp>&nbsp;&nbsp;source_interface</samp>](## "ip_tacacs.source_interface") | String |  |  |  | Define `source_interface` for VRF default. |
    | [<samp>&nbsp;&nbsp;vrfs</samp>](## "ip_tacacs.vrfs") | List, items: Dictionary |  |  |  | Define `source interfaces` for any VRF other than default. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "ip_tacacs.vrfs.[].name") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_interface</samp>](## "ip_tacacs.vrfs.[].source_interface") | String | Required |  |  |  |
    | [<samp>ip_tacacs_source_interfaces</samp>](## "ip_tacacs_source_interfaces") <span style="color:red">deprecated</span> | List, items: Dictionary |  |  |  | <span style="color:red">This key is deprecated. Support will be removed in AVD version 7.0.0. Use <samp>ip_tacacs</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;-&nbsp;name</samp>](## "ip_tacacs_source_interfaces.[].name") | String | Required |  |  | Interface name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "ip_tacacs_source_interfaces.[].vrf") | String |  |  |  |  |

=== "YAML"

    ```yaml
    # IP TACACS source interface configuration.
    # This requires to set the 'eos_config_future.new_ip_tacacs_cli_order: true' to render the new CLI order.
    ip_tacacs:

      # Define `source_interface` for VRF default.
      source_interface: <str>

      # Define `source interfaces` for any VRF other than default.
      vrfs:
        - name: <str; required; unique>
          source_interface: <str; required>
    # This key is deprecated.
    # Support will be removed in AVD version 7.0.0.
    # Use `ip_tacacs` instead.
    ip_tacacs_source_interfaces:

        # Interface name.
      - name: <str; required>
        vrf: <str>
    ```
