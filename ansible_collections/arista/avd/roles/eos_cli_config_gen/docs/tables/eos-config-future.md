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
    | [<samp>&nbsp;&nbsp;new_ip_radius_cli_order</samp>](## "eos_config_future.new_ip_radius_cli_order") | Boolean |  | `False` |  | Available from AVD 6.1.0.<br>When `true`, renders the new EOS CLI order using `ip_radius`, sorted by VRF name.<br>When `false` (default), renders the legacy CLI order using `ip_radius_source_interfaces`, sorted by source interface name. |
    | [<samp>&nbsp;&nbsp;new_ip_tacacs_cli_order</samp>](## "eos_config_future.new_ip_tacacs_cli_order") | Boolean |  | `False` |  | Available from AVD 6.1.0.<br>When `true`, renders the new EOS CLI order using `ip_tacacs`, sorted by VRF name.<br>When `false` (default), renders the legacy CLI order using `ip_tacacs_source_interfaces`, sorted by source interface name. |
    | [<samp>&nbsp;&nbsp;only_render_mpls_rsvp_with_settings</samp>](## "eos_config_future.only_render_mpls_rsvp_with_settings") | Boolean |  | `False` |  | Available from AVD 6.2.0.<br>When `true`, only renders the `mpls rsvp` CLI block when at least one `mpls.rsvp.*` setting is defined.<br>When `false` (default), renders `mpls rsvp` whenever `mpls.rsvp` is defined, even if no sub-settings are set. |
    | [<samp>&nbsp;&nbsp;render_monitor_layer1_without_enabled</samp>](## "eos_config_future.render_monitor_layer1_without_enabled") | Boolean |  | `False` |  | Available from AVD 6.3.0.<br>When `true`, renders the `monitor layer1` CLI block only if `monitor_layer1.logging_transceiver.*` / `monitor_layer1.logging_mac_fault` sub-setting is `true` no matter the value of `monitor_layer1.enabled` is `true` or `false`.<br>When `false` (default), renders the `monitor layer1` cli block only if `monitor_layer1.enabled` is `true`. |
    | [<samp>&nbsp;&nbsp;render_spanning_tree_portfast_edge</samp>](## "eos_config_future.render_spanning_tree_portfast_edge") | Boolean |  | `False` |  | Available from AVD 6.3.0.<br>When `true`, renders `spanning-tree portfast edge` on `ethernet_interfaces` and `port_channel_interfaces` when `spanning_tree_portfast` is set to `edge`, matching the running-config preserved by EOS 4.33.2F and later.<br>When `false` (default), renders the legacy `spanning-tree portfast` without the `edge` keyword. |
    | [<samp>&nbsp;&nbsp;only_render_separator_with_boot_secret_key</samp>](## "eos_config_future.only_render_separator_with_boot_secret_key") | Boolean |  | `False` |  | Available from AVD 6.4.0.<br>When `true`, the '!' separator before 'boot secret' is only rendered when `boot.secret.key` is provided.<br>When `false` (default), the '!' separator is always rendered when `boot.secret` is defined, even if `boot.secret.key` is missing, for backward compatibility. |

=== "YAML"

    ```yaml
    # Opt-in to future EOS CLI behaviors which will become default behaviors in a future AVD major version.
    eos_config_future:

      # Available from AVD 6.2.0.
      # Always render a '!' before the '(no) ip routing' command section.
      # Without this the '!' is missing when only configuring routing for VRFs.
      always_render_ip_routing_separator: <bool; default=False>

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

      # Available from AVD 6.4.0.
      # When `true`, the '!' separator before 'boot secret' is only rendered when `boot.secret.key` is provided.
      # When `false` (default), the '!' separator is always rendered when `boot.secret` is defined, even if `boot.secret.key` is missing, for backward compatibility.
      only_render_separator_with_boot_secret_key: <bool; default=False>
    ```
