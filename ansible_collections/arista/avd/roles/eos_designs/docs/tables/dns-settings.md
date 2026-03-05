<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>dns_settings</samp>](## "dns_settings") | Dictionary |  |  |  | DNS settings |
    | [<samp>&nbsp;&nbsp;domain</samp>](## "dns_settings.domain") | String |  |  |  | DNS domain name like 'fabric.local' |
    | [<samp>&nbsp;&nbsp;servers</samp>](## "dns_settings.servers") | List, items: Dictionary | Required |  | Min Length: 1 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;vrf</samp>](## "dns_settings.servers.[].vrf") | String |  | `use_default_mgmt_method_vrf` |  | The value of `vrf` will be interpreted according to these rules:<br>- `use_mgmt_interface_vrf` will configure the DNS server under the VRF set with `mgmt_interface_vrf` and set the `mgmt_interface` as DNS lookup source-interface.<br>  An error will be raised if `mgmt_ip` or `ipv6_mgmt_ip` are not configured for the device.<br>- `use_inband_mgmt_vrf` will configure the DNS server under the VRF set with `inband_mgmt_vrf` and set the `inband_mgmt_interface` as DNS lookup source-interface.<br>  An error will be raised if inband management is not configured for the device.<br>- `use_default_mgmt_method_vrf` will configure the VRF and source-interface for one of the two options above depending on the value of `default_mgmt_method`.<br>- Any other string will be used directly as the VRF name. Remember to set the `dns_settings.vrfs[].source_interface` if needed. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "dns_settings.servers.[].ip_address") | String | Required |  |  | IPv4 or IPv6 address for DNS server. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority</samp>](## "dns_settings.servers.[].priority") | Integer |  |  | Min: 0<br>Max: 4 | Priority value (lower is first). |
    | [<samp>&nbsp;&nbsp;vrfs</samp>](## "dns_settings.vrfs") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "dns_settings.vrfs.[].name") | String | Required, Unique |  |  | VRF name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_interface</samp>](## "dns_settings.vrfs.[].source_interface") | String |  |  |  | Source interface to use for DNS lookups in this VRF.<br>If set for the VRFs defined by `mgmt_interface_vrf` or `inband_mgmt_vrf`, this setting will take precedence. |
    | [<samp>&nbsp;&nbsp;set_source_interfaces</samp>](## "dns_settings.set_source_interfaces") | Boolean |  | `True` |  | Automatically set source interface when VRF is set to `use_mgmt_interface_vrf`, `use_inband_mgmt_vrf` or `use_default_mgmt_method_vrf`.<br>Can be set to `false` to avoid changes when migrating from the old `name_servers` model. |

=== "YAML"

    ```yaml
    # DNS settings
    dns_settings:

      # DNS domain name like 'fabric.local'
      domain: <str>
      servers: # >=1 items; required

          # The value of `vrf` will be interpreted according to these rules:
          # - `use_mgmt_interface_vrf` will configure the DNS server under the VRF set with `mgmt_interface_vrf` and set the `mgmt_interface` as DNS lookup source-interface.
          #   An error will be raised if `mgmt_ip` or `ipv6_mgmt_ip` are not configured for the device.
          # - `use_inband_mgmt_vrf` will configure the DNS server under the VRF set with `inband_mgmt_vrf` and set the `inband_mgmt_interface` as DNS lookup source-interface.
          #   An error will be raised if inband management is not configured for the device.
          # - `use_default_mgmt_method_vrf` will configure the VRF and source-interface for one of the two options above depending on the value of `default_mgmt_method`.
          # - Any other string will be used directly as the VRF name. Remember to set the `dns_settings.vrfs[].source_interface` if needed.
        - vrf: <str; default="use_default_mgmt_method_vrf">

          # IPv4 or IPv6 address for DNS server.
          ip_address: <str; required>

          # Priority value (lower is first).
          priority: <int; 0-4>
      vrfs:

          # VRF name.
        - name: <str; required; unique>

          # Source interface to use for DNS lookups in this VRF.
          # If set for the VRFs defined by `mgmt_interface_vrf` or `inband_mgmt_vrf`, this setting will take precedence.
          source_interface: <str>

      # Automatically set source interface when VRF is set to `use_mgmt_interface_vrf`, `use_inband_mgmt_vrf` or `use_default_mgmt_method_vrf`.
      # Can be set to `false` to avoid changes when migrating from the old `name_servers` model.
      set_source_interfaces: <bool; default=True>
    ```
