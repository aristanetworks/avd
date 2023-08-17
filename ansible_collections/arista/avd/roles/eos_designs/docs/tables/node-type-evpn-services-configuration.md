<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>&lt;node_type_keys.key&gt;</samp>](## "&lt;node_type_keys.key&gt;") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;defaults</samp>](## "&lt;node_type_keys.key&gt;.defaults") | Dictionary |  |  |  | Define variables for all nodes of this type. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;evpn_services_l2_only</samp>](## "&lt;node_type_keys.key&gt;.defaults.evpn_services_l2_only") | Boolean |  | `False` |  | Possibility to prevent configuration of Tenant VRFs and SVIs.<br>Override node definition "network_services_l3" from node_type_keys.<br>This allows support for centralized routing.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;filter</samp>](## "&lt;node_type_keys.key&gt;.defaults.filter") | Dictionary |  |  |  | Filter L3 and L2 network services based on tenant and tags (and operation filter).<br>If filter is not defined it will default to all.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tenants</samp>](## "&lt;node_type_keys.key&gt;.defaults.filter.tenants") | List, items: String |  | `['all']` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.defaults.filter.tenants.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tags</samp>](## "&lt;node_type_keys.key&gt;.defaults.filter.tags") | List, items: String |  | `['all']` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.defaults.filter.tags.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;always_include_vrfs_in_tenants</samp>](## "&lt;node_type_keys.key&gt;.defaults.filter.always_include_vrfs_in_tenants") | List, items: String |  |  |  | List of tenants where VRFs will be configured even if VLANs are not included in tags.<br>Useful for L3 "border" leaf.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.defaults.filter.always_include_vrfs_in_tenants.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;only_vlans_in_use</samp>](## "&lt;node_type_keys.key&gt;.defaults.filter.only_vlans_in_use") | Boolean |  | `False` |  | Only configure VLANs, SVIs, VRFs in use by connected endpoints or downstream L2 switches.<br>Note! This feature only considers configuration managed by eos_designs.<br>This excludes structured_config, custom_structured_configuration_, raw_eos_cli, eos_cli, custom templates, configlets etc.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;igmp_snooping_enabled</samp>](## "&lt;node_type_keys.key&gt;.defaults.igmp_snooping_enabled") | Boolean |  | `True` |  | Activate or deactivate IGMP snooping on device level. |
    | [<samp>&nbsp;&nbsp;node_groups</samp>](## "&lt;node_type_keys.key&gt;.node_groups") | List, items: Dictionary |  |  |  | Define variables related to all nodes part of this group. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- group</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].group") | String | Required, Unique |  |  | The Node Group Name is used for MLAG domain unless set with 'mlag_domain_id'.<br>The Node Group Name is also used for peer description on downstream switches' uplinks.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes") | List, items: Dictionary |  |  |  | Define variables per node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].name") | String | Required, Unique |  |  | The Node Name is used as "hostname". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_services_l2_only</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].evpn_services_l2_only") | Boolean |  | `False` |  | Possibility to prevent configuration of Tenant VRFs and SVIs.<br>Override node definition "network_services_l3" from node_type_keys.<br>This allows support for centralized routing.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;filter</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].filter") | Dictionary |  |  |  | Filter L3 and L2 network services based on tenant and tags (and operation filter).<br>If filter is not defined it will default to all.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tenants</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].filter.tenants") | List, items: String |  | `['all']` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].filter.tenants.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tags</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].filter.tags") | List, items: String |  | `['all']` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].filter.tags.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;always_include_vrfs_in_tenants</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].filter.always_include_vrfs_in_tenants") | List, items: String |  |  |  | List of tenants where VRFs will be configured even if VLANs are not included in tags.<br>Useful for L3 "border" leaf.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].filter.always_include_vrfs_in_tenants.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;only_vlans_in_use</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].filter.only_vlans_in_use") | Boolean |  | `False` |  | Only configure VLANs, SVIs, VRFs in use by connected endpoints or downstream L2 switches.<br>Note! This feature only considers configuration managed by eos_designs.<br>This excludes structured_config, custom_structured_configuration_, raw_eos_cli, eos_cli, custom templates, configlets etc.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;igmp_snooping_enabled</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].igmp_snooping_enabled") | Boolean |  | `True` |  | Activate or deactivate IGMP snooping on device level. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_services_l2_only</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].evpn_services_l2_only") | Boolean |  | `False` |  | Possibility to prevent configuration of Tenant VRFs and SVIs.<br>Override node definition "network_services_l3" from node_type_keys.<br>This allows support for centralized routing.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;filter</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].filter") | Dictionary |  |  |  | Filter L3 and L2 network services based on tenant and tags (and operation filter).<br>If filter is not defined it will default to all.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tenants</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].filter.tenants") | List, items: String |  | `['all']` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].filter.tenants.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tags</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].filter.tags") | List, items: String |  | `['all']` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].filter.tags.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;always_include_vrfs_in_tenants</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].filter.always_include_vrfs_in_tenants") | List, items: String |  |  |  | List of tenants where VRFs will be configured even if VLANs are not included in tags.<br>Useful for L3 "border" leaf.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].filter.always_include_vrfs_in_tenants.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;only_vlans_in_use</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].filter.only_vlans_in_use") | Boolean |  | `False` |  | Only configure VLANs, SVIs, VRFs in use by connected endpoints or downstream L2 switches.<br>Note! This feature only considers configuration managed by eos_designs.<br>This excludes structured_config, custom_structured_configuration_, raw_eos_cli, eos_cli, custom templates, configlets etc.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;igmp_snooping_enabled</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].igmp_snooping_enabled") | Boolean |  | `True` |  | Activate or deactivate IGMP snooping on device level. |
    | [<samp>&nbsp;&nbsp;nodes</samp>](## "&lt;node_type_keys.key&gt;.nodes") | List, items: Dictionary |  |  |  | Define variables per node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].name") | String | Required, Unique |  |  | The Node Name is used as "hostname". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_services_l2_only</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].evpn_services_l2_only") | Boolean |  | `False` |  | Possibility to prevent configuration of Tenant VRFs and SVIs.<br>Override node definition "network_services_l3" from node_type_keys.<br>This allows support for centralized routing.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;filter</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].filter") | Dictionary |  |  |  | Filter L3 and L2 network services based on tenant and tags (and operation filter).<br>If filter is not defined it will default to all.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tenants</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].filter.tenants") | List, items: String |  | `['all']` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].filter.tenants.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tags</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].filter.tags") | List, items: String |  | `['all']` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].filter.tags.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;always_include_vrfs_in_tenants</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].filter.always_include_vrfs_in_tenants") | List, items: String |  |  |  | List of tenants where VRFs will be configured even if VLANs are not included in tags.<br>Useful for L3 "border" leaf.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].filter.always_include_vrfs_in_tenants.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;only_vlans_in_use</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].filter.only_vlans_in_use") | Boolean |  | `False` |  | Only configure VLANs, SVIs, VRFs in use by connected endpoints or downstream L2 switches.<br>Note! This feature only considers configuration managed by eos_designs.<br>This excludes structured_config, custom_structured_configuration_, raw_eos_cli, eos_cli, custom templates, configlets etc.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;igmp_snooping_enabled</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].igmp_snooping_enabled") | Boolean |  | `True` |  | Activate or deactivate IGMP snooping on device level. |

=== "YAML"

    ```yaml
    <node_type_keys.key>:
      defaults:
        evpn_services_l2_only: <bool>
        filter:
          tenants:
            - <str>
          tags:
            - <str>
          always_include_vrfs_in_tenants:
            - <str>
          only_vlans_in_use: <bool>
        igmp_snooping_enabled: <bool>
      node_groups:
        - group: <str>
          nodes:
            - name: <str>
              evpn_services_l2_only: <bool>
              filter:
                tenants:
                  - <str>
                tags:
                  - <str>
                always_include_vrfs_in_tenants:
                  - <str>
                only_vlans_in_use: <bool>
              igmp_snooping_enabled: <bool>
          evpn_services_l2_only: <bool>
          filter:
            tenants:
              - <str>
            tags:
              - <str>
            always_include_vrfs_in_tenants:
              - <str>
            only_vlans_in_use: <bool>
          igmp_snooping_enabled: <bool>
      nodes:
        - name: <str>
          evpn_services_l2_only: <bool>
          filter:
            tenants:
              - <str>
            tags:
              - <str>
            always_include_vrfs_in_tenants:
              - <str>
            only_vlans_in_use: <bool>
          igmp_snooping_enabled: <bool>
    ```
