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
    | [<samp>&nbsp;&nbsp;new_ip_routing_vrfs_separator</samp>](## "eos_config_future.new_ip_routing_vrfs_separator") | Boolean |  | `False` |  | When `true`, renders a `!` separator before the first VRF-scoped `ip routing` /<br>`ip routing ipv6 interfaces` / `no ip routing` line when no global `ip_routing`<br>or `ip_routing_ipv6_interfaces` directive is rendered.<br>When `false` (default), preserves the legacy output without the leading separator. |

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

      # When `true`, renders a `!` separator before the first VRF-scoped `ip routing` /
      # `ip routing ipv6 interfaces` / `no ip routing` line when no global `ip_routing`
      # or `ip_routing_ipv6_interfaces` directive is rendered.
      # When `false` (default), preserves the legacy output without the leading separator.
      new_ip_routing_vrfs_separator: <bool; default=False>
    ```
