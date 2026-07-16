<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>eos_config_future</samp>](## "eos_config_future") | Dictionary |  |  |  | Opt-in to future EOS CLI behaviors which will become default behaviors in a future AVD major version. |
    | [<samp>&nbsp;&nbsp;always_render_ip_routing_separator</samp>](## "eos_config_future.always_render_ip_routing_separator") | Boolean |  | `False` |  | Available from AVD 6.2.0.<br>Always render a '!' before the '(no) ip routing' command section.<br>Without this the '!' is missing when only configuring routing for VRFs. |
    | [<samp>&nbsp;&nbsp;render_combined_separator_for_ipv6_hardware_and_unicast_routing</samp>](## "eos_config_future.render_combined_separator_for_ipv6_hardware_and_unicast_routing") | Boolean |  | `False` |  | Available from AVD 6.4.0.<br>Render a single '!' separator for the combined IPv6 routing block when any of these are rendered:<br>- 'ipv6 unicast-routing'<br>- 'ipv6 unicast-routing vrf <vrf_name>'<br>- 'ipv6 hardware fib optimize prefixes profile <profile_name>'<br>Also render the '!' separator before the VRF IPv6 unicast-routing section even when 'ipv6 unicast-routing' and 'ipv6 hardware fib optimize prefixes' are not present globally, as long as at least one VRF is configured for IPv6 routing.<br>When 'false', separators are handled by each individual section. |
    | [<samp>&nbsp;&nbsp;new_ip_radius_cli_order</samp>](## "eos_config_future.new_ip_radius_cli_order") | Boolean |  | `False` |  | Available from AVD 6.1.0.<br>When `true`, renders the new EOS CLI order using `ip_radius`, sorted by VRF name.<br>When `false` (default), renders the legacy CLI order using `ip_radius_source_interfaces`, sorted by source interface name. |
    | [<samp>&nbsp;&nbsp;new_ip_tacacs_cli_order</samp>](## "eos_config_future.new_ip_tacacs_cli_order") | Boolean |  | `False` |  | Available from AVD 6.1.0.<br>When `true`, renders the new EOS CLI order using `ip_tacacs`, sorted by VRF name.<br>When `false` (default), renders the legacy CLI order using `ip_tacacs_source_interfaces`, sorted by source interface name. |
    | [<samp>&nbsp;&nbsp;only_render_mpls_rsvp_with_settings</samp>](## "eos_config_future.only_render_mpls_rsvp_with_settings") | Boolean |  | `False` |  | Available from AVD 6.2.0.<br>When `true`, only renders the `mpls rsvp` CLI block when at least one `mpls.rsvp.*` setting is defined.<br>When `false` (default), renders `mpls rsvp` whenever `mpls.rsvp` is defined, even if no sub-settings are set. |
    | [<samp>&nbsp;&nbsp;render_monitor_layer1_without_enabled</samp>](## "eos_config_future.render_monitor_layer1_without_enabled") | Boolean |  | `False` |  | Available from AVD 6.3.0.<br>When `true`, renders the `monitor layer1` CLI block only if `monitor_layer1.logging_transceiver.*` / `monitor_layer1.logging_mac_fault` sub-setting is `true` no matter the value of `monitor_layer1.enabled` is `true` or `false`.<br>When `false` (default), renders the `monitor layer1` cli block only if `monitor_layer1.enabled` is `true`. |
    | [<samp>&nbsp;&nbsp;render_spanning_tree_portfast_edge</samp>](## "eos_config_future.render_spanning_tree_portfast_edge") | Boolean |  | `False` |  | Available from AVD 6.3.0.<br>When `true`, renders `spanning-tree portfast edge` on `ethernet_interfaces` and `port_channel_interfaces` when `spanning_tree_portfast` is set to `edge`, matching the running-config preserved by EOS 4.33.2F and later.<br>When `false` (default), renders the legacy `spanning-tree portfast` without the `edge` keyword. |

=== "YAML"

    ```yaml
    # Opt-in to future EOS CLI behaviors which will become default behaviors in a future AVD major version.
    eos_config_future:

      # Available from AVD 6.2.0.
      # Always render a '!' before the '(no) ip routing' command section.
      # Without this the '!' is missing when only configuring routing for VRFs.
      always_render_ip_routing_separator: <bool; default=False>

      # Available from AVD 6.4.0.
      # Render a single '!' separator for the combined IPv6 routing block when any of these are rendered:
      # - 'ipv6 unicast-routing'
      # - 'ipv6 unicast-routing vrf <vrf_name>'
      # - 'ipv6 hardware fib optimize prefixes profile <profile_name>'
      # Also render the '!' separator before the VRF IPv6 unicast-routing section even when 'ipv6 unicast-routing' and 'ipv6 hardware fib optimize prefixes' are not present globally, as long as at least one VRF is configured for IPv6 routing.
      # When 'false', separators are handled by each individual section.
      render_combined_separator_for_ipv6_hardware_and_unicast_routing: <bool; default=False>

      # Available from AVD 6.1.0.
      # When `true`, renders the new EOS CLI order using `ip_radius`, sorted by VRF name.
      # When `false` (default), renders the legacy CLI order using `ip_radius_source_interfaces`, sorted by source interface name.
      new_ip_radius_cli_order: <bool; default=False>

      # Available from AVD 6.1.0.
      # When `true`, renders the new EOS CLI order using `ip_tacacs`, sorted by VRF name.
      # When `false` (default), renders the legacy CLI order using `ip_tacacs_source_interfaces`, sorted by source interface name.
      new_ip_tacacs_cli_order: <bool; default=False>

      # Available from AVD 6.2.0.
      # When `true`, only renders the `mpls rsvp` CLI block when at least one `mpls.rsvp.*` setting is defined.
      # When `false` (default), renders `mpls rsvp` whenever `mpls.rsvp` is defined, even if no sub-settings are set.
      only_render_mpls_rsvp_with_settings: <bool; default=False>

      # Available from AVD 6.3.0.
      # When `true`, renders the `monitor layer1` CLI block only if `monitor_layer1.logging_transceiver.*` / `monitor_layer1.logging_mac_fault` sub-setting is `true` no matter the value of `monitor_layer1.enabled` is `true` or `false`.
      # When `false` (default), renders the `monitor layer1` cli block only if `monitor_layer1.enabled` is `true`.
      render_monitor_layer1_without_enabled: <bool; default=False>

      # Available from AVD 6.3.0.
      # When `true`, renders `spanning-tree portfast edge` on `ethernet_interfaces` and `port_channel_interfaces` when `spanning_tree_portfast` is set to `edge`, matching the running-config preserved by EOS 4.33.2F and later.
      # When `false` (default), renders the legacy `spanning-tree portfast` without the `edge` keyword.
      render_spanning_tree_portfast_edge: <bool; default=False>
    ```
