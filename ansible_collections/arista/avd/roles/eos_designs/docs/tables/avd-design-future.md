<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>avd_design_future</samp>](## "avd_design_future") | Dictionary |  |  |  | Opt-in to future AVD behaviors which will become default behaviors in a future AVD major version. |
    | [<samp>&nbsp;&nbsp;ip_radius_source_interface_setting</samp>](## "avd_design_future.ip_radius_source_interface_setting") | Boolean |  | `False` |  | Enable improved RADIUS source interface configuration with separate keys for VRF default and other VRFs.<br><br>When enabled:<br>- VRF default: Uses `ip_radius.source_interface`<br>- Other VRFs: Uses `ip_radius.vrfs` list<br>- Enforces VRF name uniqueness<br>- Aligns with EOS CLI behavior (where "vrf default" is implicit)<br><br>When disabled (current):<br>- Uses `ip_radius_source_interfaces` list for all VRF combinations |
    | [<samp>&nbsp;&nbsp;bgp_always_disable_ipv4_unicast_for_peer_groups</samp>](## "avd_design_future.bgp_always_disable_ipv4_unicast_for_peer_groups") | Boolean |  | `True` |  | Deactivate the IPv4 unicast Address Family for BGP Peer Groups even when IPv4 is not activated by default. |
    | [<samp>&nbsp;&nbsp;ip_tacacs_source_interface_setting</samp>](## "avd_design_future.ip_tacacs_source_interface_setting") | Boolean |  | `False` |  | Enable improved TACACS source interface configuration with separate keys for VRF default and other VRFs.<br>When enabled:<br>- VRF default: Uses `ip_tacacs.source_interface`<br>- Other VRFs: Uses `ip_tacacs.vrfs` list<br>- Enforces VRF name uniqueness<br>- Aligns with EOS CLI behavior (where "vrf default" is implicit)<br>When disabled (current):<br>- Uses `ip_tacacs_source_interfaces` list for all VRF combinations |

=== "YAML"

    ```yaml
    # Opt-in to future AVD behaviors which will become default behaviors in a future AVD major version.
    avd_design_future:

      # Enable improved RADIUS source interface configuration with separate keys for VRF default and other VRFs.
      #
      # When enabled:
      # - VRF default: Uses `ip_radius.source_interface`
      # - Other VRFs: Uses `ip_radius.vrfs` list
      # - Enforces VRF name uniqueness
      # - Aligns with EOS CLI behavior (where "vrf default" is implicit)
      #
      # When disabled (current):
      # - Uses `ip_radius_source_interfaces` list for all VRF combinations
      ip_radius_source_interface_setting: <bool; default=False>

      # Deactivate the IPv4 unicast Address Family for BGP Peer Groups even when IPv4 is not activated by default.
      bgp_always_disable_ipv4_unicast_for_peer_groups: <bool; default=True>

      # Enable improved TACACS source interface configuration with separate keys for VRF default and other VRFs.
      # When enabled:
      # - VRF default: Uses `ip_tacacs.source_interface`
      # - Other VRFs: Uses `ip_tacacs.vrfs` list
      # - Enforces VRF name uniqueness
      # - Aligns with EOS CLI behavior (where "vrf default" is implicit)
      # When disabled (current):
      # - Uses `ip_tacacs_source_interfaces` list for all VRF combinations
      ip_tacacs_source_interface_setting: <bool; default=False>
    ```
