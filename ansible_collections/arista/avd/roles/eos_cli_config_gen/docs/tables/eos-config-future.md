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
    | [<samp>&nbsp;&nbsp;only_render_mpls_rsvp_with_settings</samp>](## "eos_config_future.only_render_mpls_rsvp_with_settings") | Boolean |  | `False` |  | When `true`, only renders the `mpls rsvp` CLI block when at least one `mpls.rsvp.*` setting is defined.<br>When `false` (default), renders `mpls rsvp` whenever `mpls.rsvp` is defined, even if no sub-settings are set. |
    | [<samp>&nbsp;&nbsp;only_render_no_logging_transceiver</samp>](## "eos_config_future.only_render_no_logging_transceiver") | Boolean |  | `False` |  | When `true`, only renders the `no logging transceiver` when `monitor_layer1.logging_transceiver.enabled` or `monitor_layer1.logging_transceiver.dom`<br> or `monitor_layer1.logging_transceiver.communication` are set to `false`.<br>When `false` (default), no config would appeare under `monitor layer1` if `monitor_layer1.logging_transceiver.enabled`<br> or `monitor_layer1.logging_transceiver.dom` or `monitor_layer1.logging_transceiver.communication` are set to `false`. |

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

      # When `true`, only renders the `mpls rsvp` CLI block when at least one `mpls.rsvp.*` setting is defined.
      # When `false` (default), renders `mpls rsvp` whenever `mpls.rsvp` is defined, even if no sub-settings are set.
      only_render_mpls_rsvp_with_settings: <bool; default=False>

      # When `true`, only renders the `no logging transceiver` when `monitor_layer1.logging_transceiver.enabled` or `monitor_layer1.logging_transceiver.dom`
      #  or `monitor_layer1.logging_transceiver.communication` are set to `false`.
      # When `false` (default), no config would appeare under `monitor layer1` if `monitor_layer1.logging_transceiver.enabled`
      #  or `monitor_layer1.logging_transceiver.dom` or `monitor_layer1.logging_transceiver.communication` are set to `false`.
      only_render_no_logging_transceiver: <bool; default=False>
    ```
