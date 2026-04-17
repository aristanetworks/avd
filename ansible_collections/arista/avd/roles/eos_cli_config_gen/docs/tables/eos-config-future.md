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
    | [<samp>&nbsp;&nbsp;new_snmp_server_cli_order</samp>](## "eos_config_future.new_snmp_server_cli_order") | Dictionary |  |  |  | Opt-in to new EOS CLI order for `snmp_server` keys. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv4_acls</samp>](## "eos_config_future.new_snmp_server_cli_order.ipv4_acls") | Boolean |  | `False` |  | When `true`, renders IPv4 ACLs grouped under each VRF in the new EOS CLI order.<br>When `false` (default), renders the legacy CLI order with all IPv4 ACLs rendered at the end of the configuration. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_acls</samp>](## "eos_config_future.new_snmp_server_cli_order.ipv6_acls") | Boolean |  | `False` |  | When `true`, renders IPv6 ACLs grouped under each VRF in the new EOS CLI order.<br>When `false` (default), renders the legacy CLI order with all IPv6 ACLs rendered at the end of the configuration. |

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

      # Opt-in to new EOS CLI order for `snmp_server` keys.
      new_snmp_server_cli_order:

        # When `true`, renders IPv4 ACLs grouped under each VRF in the new EOS CLI order.
        # When `false` (default), renders the legacy CLI order with all IPv4 ACLs rendered at the end of the configuration.
        ipv4_acls: <bool; default=False>

        # When `true`, renders IPv6 ACLs grouped under each VRF in the new EOS CLI order.
        # When `false` (default), renders the legacy CLI order with all IPv6 ACLs rendered at the end of the configuration.
        ipv6_acls: <bool; default=False>
    ```
