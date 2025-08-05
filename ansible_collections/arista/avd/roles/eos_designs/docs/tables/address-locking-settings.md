<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>address_locking_settings</samp>](## "address_locking_settings") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;dhcp_servers_ipv4</samp>](## "address_locking_settings.dhcp_servers_ipv4") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "address_locking_settings.dhcp_servers_ipv4.[]") | String |  |  |  | DHCP server IPv4 address. |
    | [<samp>&nbsp;&nbsp;local_interface</samp>](## "address_locking_settings.local_interface") | String |  |  |  | The value will be interpreted according to these rules:<br>  - `use_mgmt_interface` will configure the mgmt_interface as the local interface.<br>  - `use_inband_mgmt_interface` will configure the inband_mgmt_interface as the local interface.<br>  - `use_default_mgmt_method_interface` will configure mgmt_interface or inband_mgmt_interface as the local interface depending on the value of `default_mgmt_method`.<br>  - Any other string will be used directly as the local interface. |

=== "YAML"

    ```yaml
    address_locking_settings:
      dhcp_servers_ipv4:

          # DHCP server IPv4 address.
        - <str>

      # The value will be interpreted according to these rules:
      #   - `use_mgmt_interface` will configure the mgmt_interface as the local interface.
      #   - `use_inband_mgmt_interface` will configure the inband_mgmt_interface as the local interface.
      #   - `use_default_mgmt_method_interface` will configure mgmt_interface or inband_mgmt_interface as the local interface depending on the value of `default_mgmt_method`.
      #   - Any other string will be used directly as the local interface.
      local_interface: <str>
    ```
