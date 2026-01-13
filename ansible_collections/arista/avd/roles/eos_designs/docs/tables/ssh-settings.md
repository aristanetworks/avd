<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>ssh_settings</samp>](## "ssh_settings") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;enabled</samp>](## "ssh_settings.enabled") | Boolean |  |  |  | Explicitly enable or disable management ssh for all VRFs. By default EOS enables management ssh for all VRFs. |
    | [<samp>&nbsp;&nbsp;vrfs</samp>](## "ssh_settings.vrfs") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "ssh_settings.vrfs.[].name") | String | Required, Unique |  |  | VRF name.<br>The value will be interpreted according to these rules:<br>- `use_mgmt_interface_vrf` will configure SSH for the VRF set with `mgmt_interface_vrf`.<br>  An error will be raised if `mgmt_ip` or `ipv6_mgmt_ip` are not configured for the device.<br>- `use_inband_mgmt_vrf` will configure SSH for the VRF set with `inband_mgmt_vrf`.<br>  An error will be raised if inband management is not configured for the device.<br>- `use_default_mgmt_method_vrf` will configure the VRF for one of the two options above depending on the value of `default_mgmt_method`.<br>- Any other string will be used directly as the VRF name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "ssh_settings.vrfs.[].enabled") | Boolean | Required |  |  | Enable SSH in VRF. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4_acl</samp>](## "ssh_settings.vrfs.[].ipv4_acl") | String |  |  |  | IPv4 access-list name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_acl</samp>](## "ssh_settings.vrfs.[].ipv6_acl") | String |  |  |  | IPv6 access-list name. |
    | [<samp>&nbsp;&nbsp;idle_timeout</samp>](## "ssh_settings.idle_timeout") | Integer |  |  | Min: 0<br>Max: 86400 | Idle timeout in minutes. |

=== "YAML"

    ```yaml
    ssh_settings:

      # Explicitly enable or disable management ssh for all VRFs. By default EOS enables management ssh for all VRFs.
      enabled: <bool>
      vrfs:

          # VRF name.
          # The value will be interpreted according to these rules:
          # - `use_mgmt_interface_vrf` will configure SSH for the VRF set with `mgmt_interface_vrf`.
          #   An error will be raised if `mgmt_ip` or `ipv6_mgmt_ip` are not configured for the device.
          # - `use_inband_mgmt_vrf` will configure SSH for the VRF set with `inband_mgmt_vrf`.
          #   An error will be raised if inband management is not configured for the device.
          # - `use_default_mgmt_method_vrf` will configure the VRF for one of the two options above depending on the value of `default_mgmt_method`.
          # - Any other string will be used directly as the VRF name.
        - name: <str; required; unique>

          # Enable SSH in VRF.
          enabled: <bool; required>

          # IPv4 access-list name.
          ipv4_acl: <str>

          # IPv6 access-list name.
          ipv6_acl: <str>

      # Idle timeout in minutes.
      idle_timeout: <int; 0-86400>
    ```
