<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>default_mgmt_method</samp>](## "default_mgmt_method") | String |  | `oob` | Valid Values:<br>- oob<br>- inband<br>- none | `default_mgmt_method` controls the default VRF and source interface used for the following management and monitoring protocols configured with `eos_designs`:<br>  - `cv_settings`<br>  - `dns_settings`<br>  - `ntp_settings`<br>  - `sflow_settings`<br><br>`oob` means the protocols will be configured with the VRF set by `mgmt_interface_vrf` and `mgmt_interface` as the source interface.<br>`inband` means the protocols will be configured with the VRF set by `inband_mgmt_vrf` and `inband_mgmt_interface` as the source interface.<br>`none` means the VRF and or interface must be manually set for each protocol.<br>This can be overridden under the settings for each protocol.<br> |
    | [<samp>mgmt_destination_networks</samp>](## "mgmt_destination_networks") | List, items: String |  |  |  | List of IPv4 prefixes to configure as static routes towards the OOB Management interface gateway.<br>Replaces the default route. |
    | [<samp>&nbsp;&nbsp;- &lt;str&gt;</samp>](## "mgmt_destination_networks.[].&lt;str&gt;") | String |  |  |  | IPv4_address/Mask. |
    | [<samp>mgmt_gateway</samp>](## "mgmt_gateway") | String |  |  |  | OOB Management interface gateway in IPv4 format.<br>Used as next-hop for default gateway or static routes defined under 'mgmt_destination_networks'. |
    | [<samp>mgmt_interface</samp>](## "mgmt_interface") | String |  | `Management1` |  | OOB Management interface. |
    | [<samp>mgmt_interface_description</samp>](## "mgmt_interface_description") | String |  | `oob_management` |  | Management interface description.<br> |
    | [<samp>mgmt_interface_vrf</samp>](## "mgmt_interface_vrf") | String |  | `MGMT` |  | OOB Management VRF. |
    | [<samp>mgmt_vrf_routing</samp>](## "mgmt_vrf_routing") | Boolean |  | `False` |  | Configure IP routing for the OOB Management VRF. |

=== "YAML"

    ```yaml
    default_mgmt_method: <str>
    mgmt_destination_networks:
      - <str>
    mgmt_gateway: <str>
    mgmt_interface: <str>
    mgmt_interface_description: <str>
    mgmt_interface_vrf: <str>
    mgmt_vrf_routing: <bool>
    ```
