<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>avd_design_future</samp>](## "avd_design_future") | Dictionary |  |  |  | Opt-in to future AVD behaviors which will become default behaviors in a future AVD major version. |
    | [<samp>&nbsp;&nbsp;accept_dhcp_default_route_for_mgmt_ip_dhcp</samp>](## "avd_design_future.accept_dhcp_default_route_for_mgmt_ip_dhcp") | Boolean |  | `False` |  | Configure management interface to accept DHCP default route when the management IP is set to 'dhcp'. |

=== "YAML"

    ```yaml
    # Opt-in to future AVD behaviors which will become default behaviors in a future AVD major version.
    avd_design_future:

      # Configure management interface to accept DHCP default route when the management IP is set to 'dhcp'.
      accept_dhcp_default_route_for_mgmt_ip_dhcp: <bool; default=False>
    ```
