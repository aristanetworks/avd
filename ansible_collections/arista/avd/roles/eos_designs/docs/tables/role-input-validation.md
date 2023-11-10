<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>&lt;network_services_keys.name&gt;</samp>](## "<network_services_keys.name>") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;-&nbsp;name</samp>](## "<network_services_keys.name>.[].name") | String | Required, Unique |  |  | Specify a tenant name.<br>Tenant provide a construct to group L3 VRFs and L2 VLANs.<br>Networks services can be filtered by tenant name.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vrfs</samp>](## "<network_services_keys.name>.[].vrfs") | List, items: Dictionary |  |  |  | VRFs will only be configured on a node if any of the underlying objects like `svis` or `l3_interfaces` apply to the node.<br><br>It is recommended to only define a VRF in one Tenant. If the same VRF name is used across multiple tenants and those tenants<br>are accepted by `filter.tenants` on the node, any object set under the duplicate VRFs must either be unique or be an exact match.<br><br>VRF "default" is partially supported under network-services. Currently the supported options for "default" vrf are route-target,<br>route-distinguisher settings, structured_config, raw_eos_cli in bgp and SVIs are the only supported interface type.<br>Vlan-aware-bundles are supported as well inside default vrf. OSPF is not supported currently.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "<network_services_keys.name>.[].vrfs.[].name") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "<network_services_keys.name>.[].vrfs.[].structured_config") | Dictionary |  |  |  | Custom structured config for eos_cli_config_gen. |
    | [<samp>&lt;node_type_keys.key&gt;</samp>](## "<node_type_keys.key>") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;defaults</samp>](## "<node_type_keys.key>.defaults") | Dictionary |  |  |  | Define variables for all nodes of this type. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "<node_type_keys.key>.defaults.structured_config") | Dictionary |  |  |  | Custom structured config for eos_cli_config_gen. |
    | [<samp>&nbsp;&nbsp;node_groups</samp>](## "<node_type_keys.key>.node_groups") | List, items: Dictionary |  |  |  | Define variables related to all nodes part of this group. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;group</samp>](## "<node_type_keys.key>.node_groups.[].group") | String | Required, Unique |  |  | The Node Group Name is used for MLAG domain unless set with 'mlag_domain_id'.<br>The Node Group Name is also used for peer description on downstream switches' uplinks.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "<node_type_keys.key>.node_groups.[].nodes") | List, items: Dictionary |  |  |  | Define variables per node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].name") | String | Required, Unique |  |  | The Node Name is used as "hostname". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].structured_config") | Dictionary |  |  |  | Custom structured config for eos_cli_config_gen. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "<node_type_keys.key>.node_groups.[].structured_config") | Dictionary |  |  |  | Custom structured config for eos_cli_config_gen. |
    | [<samp>&nbsp;&nbsp;nodes</samp>](## "<node_type_keys.key>.nodes") | List, items: Dictionary |  |  |  | Define variables per node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "<node_type_keys.key>.nodes.[].name") | String | Required, Unique |  |  | The Node Name is used as "hostname". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "<node_type_keys.key>.nodes.[].structured_config") | Dictionary |  |  |  | Custom structured config for eos_cli_config_gen. |
    | [<samp>avd_data_conversion_mode</samp>](## "avd_data_conversion_mode") | String |  | `debug` | Valid Values:<br>- <code>disabled</code><br>- <code>error</code><br>- <code>warning</code><br>- <code>info</code><br>- <code>debug</code><br>- <code>quiet</code> | Conversion Mode for AVD input data conversion.<br>Input data conversion will perform type conversion of input variables as defined in the schema.<br>The type conversion is intended to help the user to identify minor issues with the input data, while still allowing the data to be validated.<br>During conversion, messages will generated with information about the host(s) and key(s) which required conversion.<br>"disabled" means that conversion will not run - avoid this since conversion is also handling data deprecation and upgrade.<br>"error" will produce error messages and fail the task.<br>"warning" will produce warning messages.<br>"info" will produce regular log messages.<br>"debug" will produce hidden debug messages viewable with -v.<br>"quiet" will not produce any messages |
    | [<samp>avd_data_validation_mode</samp>](## "avd_data_validation_mode") | String |  | `warning` | Valid Values:<br>- <code>disabled</code><br>- <code>error</code><br>- <code>warning</code><br>- <code>info</code><br>- <code>debug</code> | Validation Mode for AVD input data validation.<br>Input data validation will validate the input variables according to the schema.<br>During validation, messages will generated with information about the host(s) and key(s) which failed validation.<br>"disabled" means that validation will not run.<br>"error" will produce error messages and fail the task.<br>"warning" will produce warning messages.<br>"info" will produce regular log messages.<br>"debug" will produce hidden debug messages viewable with -v. |

=== "YAML"

    ```yaml
    <network_services_keys.name>:

        # Specify a tenant name.
        # Tenant provide a construct to group L3 VRFs and L2 VLANs.
        # Networks services can be filtered by tenant name.
      - name: <str; required; unique>

        # VRFs will only be configured on a node if any of the underlying objects like `svis` or `l3_interfaces` apply to the node.

        # It is recommended to only define a VRF in one Tenant. If the same VRF name is used across multiple tenants and those tenants
        # are accepted by `filter.tenants` on the node, any object set under the duplicate VRFs must either be unique or be an exact match.

        # VRF "default" is partially supported under network-services. Currently the supported options for "default" vrf are route-target,
        # route-distinguisher settings, structured_config, raw_eos_cli in bgp and SVIs are the only supported interface type.
        # Vlan-aware-bundles are supported as well inside default vrf. OSPF is not supported currently.
        vrfs:
          - name: <str; required; unique>

            # Custom structured config for eos_cli_config_gen.
            structured_config: <dict>
    <node_type_keys.key>:

      # Define variables for all nodes of this type.
      defaults:

        # Custom structured config for eos_cli_config_gen.
        structured_config: <dict>

      # Define variables related to all nodes part of this group.
      node_groups:

          # The Node Group Name is used for MLAG domain unless set with 'mlag_domain_id'.
          # The Node Group Name is also used for peer description on downstream switches' uplinks.
        - group: <str; required; unique>

          # Define variables per node.
          nodes:

              # The Node Name is used as "hostname".
            - name: <str; required; unique>

              # Custom structured config for eos_cli_config_gen.
              structured_config: <dict>

          # Custom structured config for eos_cli_config_gen.
          structured_config: <dict>

      # Define variables per node.
      nodes:

          # The Node Name is used as "hostname".
        - name: <str; required; unique>

          # Custom structured config for eos_cli_config_gen.
          structured_config: <dict>

    # Conversion Mode for AVD input data conversion.
    # Input data conversion will perform type conversion of input variables as defined in the schema.
    # The type conversion is intended to help the user to identify minor issues with the input data, while still allowing the data to be validated.
    # During conversion, messages will generated with information about the host(s) and key(s) which required conversion.
    # "disabled" means that conversion will not run - avoid this since conversion is also handling data deprecation and upgrade.
    # "error" will produce error messages and fail the task.
    # "warning" will produce warning messages.
    # "info" will produce regular log messages.
    # "debug" will produce hidden debug messages viewable with -v.
    # "quiet" will not produce any messages
    avd_data_conversion_mode: <str; "disabled" | "error" | "warning" | "info" | "debug" | "quiet"; default="debug">

    # Validation Mode for AVD input data validation.
    # Input data validation will validate the input variables according to the schema.
    # During validation, messages will generated with information about the host(s) and key(s) which failed validation.
    # "disabled" means that validation will not run.
    # "error" will produce error messages and fail the task.
    # "warning" will produce warning messages.
    # "info" will produce regular log messages.
    # "debug" will produce hidden debug messages viewable with -v.
    avd_data_validation_mode: <str; "disabled" | "error" | "warning" | "info" | "debug"; default="warning">
    ```
