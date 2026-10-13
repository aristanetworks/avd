<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>management_eapi</samp>](## "management_eapi") | Dictionary |  |  |  | Default is HTTPS management eAPI enabled.<br> |
    | [<samp>&nbsp;&nbsp;enabled</samp>](## "management_eapi.enabled") | Boolean |  |  |  | Enable/Disable api http-commands. |
    | [<samp>&nbsp;&nbsp;enable_http</samp>](## "management_eapi.enable_http") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;enable_https</samp>](## "management_eapi.enable_https") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;default_services</samp>](## "management_eapi.default_services") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;vrfs</samp>](## "management_eapi.vrfs") | List, items: Dictionary |  | See (+) on YAML tab |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "management_eapi.vrfs.[].name") | String | Required, Unique |  |  | VRF name.<br>The value will be interpreted according to these rules:<br>- `use_mgmt_interface_vrf` will configure the eAPI under the VRF set with `mgmt_interface_vrf`.<br>  An error will be raised if `mgmt_ip` or `ipv6_mgmt_ip` are not configured for the device.<br>- `use_inband_mgmt_vrf` will configure the eAPI under the VRF set with `inband_mgmt_vrf`.<br>  An error will be raised if inband management is not configured for the device.<br>- `use_default_mgmt_method_vrf` will configure the eAPI under VRF for one of the two options above depending on the value of `default_mgmt_method`.<br>- Any other string will be used directly as the VRF name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "management_eapi.vrfs.[].enabled") | Boolean | Required |  |  | Enable/disable Management eAPI for this VRF. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4_acl</samp>](## "management_eapi.vrfs.[].ipv4_acl") | String |  |  |  | IPv4 access-list name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_acl</samp>](## "management_eapi.vrfs.[].ipv6_acl") | String |  |  |  | IPv6 access-list name. |

=== "YAML"

    ```yaml
    # Default is HTTPS management eAPI enabled.
    management_eapi:

      # Enable/Disable api http-commands.
      enabled: <bool>
      enable_http: <bool>
      enable_https: <bool; default=True>
      default_services: <bool>
      vrfs: # (1)!

          # VRF name.
          # The value will be interpreted according to these rules:
          # - `use_mgmt_interface_vrf` will configure the eAPI under the VRF set with `mgmt_interface_vrf`.
          #   An error will be raised if `mgmt_ip` or `ipv6_mgmt_ip` are not configured for the device.
          # - `use_inband_mgmt_vrf` will configure the eAPI under the VRF set with `inband_mgmt_vrf`.
          #   An error will be raised if inband management is not configured for the device.
          # - `use_default_mgmt_method_vrf` will configure the eAPI under VRF for one of the two options above depending on the value of `default_mgmt_method`.
          # - Any other string will be used directly as the VRF name.
        - name: <str; required; unique>

          # Enable/disable Management eAPI for this VRF.
          enabled: <bool; required>

          # IPv4 access-list name.
          ipv4_acl: <str>

          # IPv6 access-list name.
          ipv6_acl: <str>
    ```

    1. Default Value

        ```yaml
        vrfs:
        - name: use_default_mgmt_method_vrf
          enabled: true
        ```
