<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>eos_config_future</samp>](## "eos_config_future") | Dictionary |  |  |  | Opt-in to future EOS CLI behaviors which will become default behaviors in a future AVD major version. |
    | [<samp>&nbsp;&nbsp;new_ip_radius_cli_order</samp>](## "eos_config_future.new_ip_radius_cli_order") | Boolean |  | `False` |  | When `true`, renders the new EOS CLI order using `ip_radius`, sorted by VRF name.<br>When `false` (default), renders the legacy CLI order using `ip_radius_source_interfaces`, sorted by source interface name. |
    | [<samp>&nbsp;&nbsp;new_ip_tacacs_cli_order</samp>](## "eos_config_future.new_ip_tacacs_cli_order") | Boolean |  | `False` |  | When `true`, renders the new EOS CLI order using `ip_tacacs`, sorted by VRF name.<br>When `false` (default), renders the legacy CLI order using `ip_tacacs_source_interfaces`, sorted by source interface name. |
    | [<samp>&nbsp;&nbsp;always_render_ip_routing_separator</samp>](## "eos_config_future.always_render_ip_routing_separator") | Boolean |  | `False` |  | Always render a '!' before the '(no) ip routing' command section.<br>Without this the '!' is missing when only configuring routing for VRFs. |

=== "YAML"

    ```yaml
    # Opt-in to future EOS CLI behaviors which will become default behaviors in a future AVD major version.
    eos_config_future:

      # When `true`, renders the new EOS CLI order using `ip_radius`, sorted by VRF name.
      # When `false` (default), renders the legacy CLI order using `ip_radius_source_interfaces`, sorted by source interface name.
      new_ip_radius_cli_order: <bool; default=False>

      # When `true`, renders the new EOS CLI order using `ip_tacacs`, sorted by VRF name.
      # When `false` (default), renders the legacy CLI order using `ip_tacacs_source_interfaces`, sorted by source interface name.
      new_ip_tacacs_cli_order: <bool; default=False>

      # Always render a '!' before the '(no) ip routing' command section.
      # Without this the '!' is missing when only configuring routing for VRFs.
      always_render_ip_routing_separator: <bool; default=False>
    ```
