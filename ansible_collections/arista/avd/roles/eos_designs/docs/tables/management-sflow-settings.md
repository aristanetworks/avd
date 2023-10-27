<!--
  ~ Copyright (c) 2024 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>fabric_sflow</samp>](## "fabric_sflow") | Dictionary |  |  |  | Default enabling of sFlow for varous interface types across the fabric.<br>sFlow can also be enabled/disabled under each of the specific data models. |
    | [<samp>&nbsp;&nbsp;uplinks</samp>](## "fabric_sflow.uplinks") | Boolean |  |  |  | Enable sFlow on all fabric uplinks. |
    | [<samp>&nbsp;&nbsp;downlinks</samp>](## "fabric_sflow.downlinks") | Boolean |  |  |  | Enable sFlow on all fabric downlinks. |
    | [<samp>&nbsp;&nbsp;endpoints</samp>](## "fabric_sflow.endpoints") | Boolean |  |  |  | Enable sFlow on all endpoints ports. |
    | [<samp>&nbsp;&nbsp;l3_edge</samp>](## "fabric_sflow.l3_edge") | Boolean |  |  |  | Enable sFlow on all p2p_links defined under l3_edge. |
    | [<samp>&nbsp;&nbsp;core_interfaces</samp>](## "fabric_sflow.core_interfaces") | Boolean |  |  |  | Enable sFlow on all p2p_links defined under core_interfaces. |
    | [<samp>&nbsp;&nbsp;mlag_interfaces</samp>](## "fabric_sflow.mlag_interfaces") | Boolean |  |  |  | Enable sFlow on all MLAG peer interfaces. |
    | [<samp>sflow_settings</samp>](## "sflow_settings") | Dictionary |  |  |  | sFlow settings.<br>The sFlow process will only be configured if any interface is enabled for sFlow.<br>For source-interfaces see "source_interfaces.sflow"<br>For default enabling of sFlow for varous interface types across the fabric see "fabric_sflow" |
    | [<samp>&nbsp;&nbsp;destinations</samp>](## "sflow_settings.destinations") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;destination</samp>](## "sflow_settings.destinations.[].destination") | String | Required |  |  | sFlow destination IP address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;port</samp>](## "sflow_settings.destinations.[].port") | Integer |  |  |  | Port number |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "sflow_settings.destinations.[].vrf") | String |  |  |  | VRF Name.<br>Can be used in combination with "use_mgmt_interface_vrf" and "use_inband_mgmt_vrf" to configure the destination under multiple VRFs. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;use_mgmt_interface_vrf</samp>](## "sflow_settings.destinations.[].use_mgmt_interface_vrf") | Boolean |  |  |  | Configure the destination under the VRF set with "mgmt_interface_vrf". Can be used in combination with "vrf" and "use_inband_mgmt_vrf" to configure the destination under multiple VRFs. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;use_inband_mgmt_vrf</samp>](## "sflow_settings.destinations.[].use_inband_mgmt_vrf") | Boolean |  |  |  | Configure the destination under the VRF set with "inband_mgmt_vrf". Ignored if inband management is not configured for the device. Can be used in combination with "vrf" and "use_mgmt_interface_vrf" to configure the destination under multiple VRFs. |
    | [<samp>&nbsp;&nbsp;structured_config</samp>](## "sflow_settings.structured_config") | Dictionary |  |  |  | Custom structured config added under sflow for eos_cli_config_gen |

=== "YAML"

    ```yaml
    # Default enabling of sFlow for varous interface types across the fabric.
    # sFlow can also be enabled/disabled under each of the specific data models.
    fabric_sflow:

      # Enable sFlow on all fabric uplinks.
      uplinks: <bool>

      # Enable sFlow on all fabric downlinks.
      downlinks: <bool>

      # Enable sFlow on all endpoints ports.
      endpoints: <bool>

      # Enable sFlow on all p2p_links defined under l3_edge.
      l3_edge: <bool>

      # Enable sFlow on all p2p_links defined under core_interfaces.
      core_interfaces: <bool>

      # Enable sFlow on all MLAG peer interfaces.
      mlag_interfaces: <bool>

    # sFlow settings.
    # The sFlow process will only be configured if any interface is enabled for sFlow.
    # For source-interfaces see "source_interfaces.sflow"
    # For default enabling of sFlow for varous interface types across the fabric see "fabric_sflow"
    sflow_settings:
      destinations:

          # sFlow destination IP address.
        - destination: <str; required>

          # Port number
          port: <int>

          # VRF Name.
          # Can be used in combination with "use_mgmt_interface_vrf" and "use_inband_mgmt_vrf" to configure the destination under multiple VRFs.
          vrf: <str>

          # Configure the destination under the VRF set with "mgmt_interface_vrf". Can be used in combination with "vrf" and "use_inband_mgmt_vrf" to configure the destination under multiple VRFs.
          use_mgmt_interface_vrf: <bool>

          # Configure the destination under the VRF set with "inband_mgmt_vrf". Ignored if inband management is not configured for the device. Can be used in combination with "vrf" and "use_mgmt_interface_vrf" to configure the destination under multiple VRFs.
          use_inband_mgmt_vrf: <bool>

      # Custom structured config added under sflow for eos_cli_config_gen
      structured_config: <dict>
    ```
