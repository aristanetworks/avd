<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>cv_tags_topology_type</samp>](## "cv_tags_topology_type") | String |  |  |  | Device type that CloudVision should use when generating the Topology like "leaf", "spine", "core", "edge" or "member-leaf". Defaults to the setting under node_type_keys. |
    | [<samp>generate_cv_tags</samp>](## "generate_cv_tags") | Dictionary |  |  |  | Generate CloudVision Tags based on AVD data. |
    | [<samp>&nbsp;&nbsp;topology_hints</samp>](## "generate_cv_tags.topology_hints") | Boolean |  | `False` |  | Enable the generation of CloudVision Topology Tags (hints). |
    | [<samp>&nbsp;&nbsp;campus_fabric</samp>](## "generate_cv_tags.campus_fabric") | Boolean |  | `False` |  | PREVIEW: This option is marked as "preview", meaning the data models or generated configuration can change at any time.<br>Generate CloudVision device and interface Topology Tags for Campus fabric devices.<br>Device is treated as a Campus fabric device if:<br>  - The `campus` variable is assigned, either as native Ansible variable or as part of the `<node_type_keys.key>` AVD data construct.<br>  - The `generate_cv_tags.campus_fabric` variable is set to `True`.<br>When campus-related tags are generated for a device, generation of the DC-related tags is automatically disabled for that device.<br>AVD generates the following device tags for the Campus fabric devices based on the provided Campus-related input variables:<br>  - `Campus`<br>  - `Campus-Pod`<br>  - `Access-Pod`<br>  - `topology_hint_type`<br>  - `Role`<br>These tags are later used by CloudVision to render the correct network layout in the Topology view (`campusV2` network hierarchy) and Campus dashboards. |
    | [<samp>&nbsp;&nbsp;interface_tags</samp>](## "generate_cv_tags.interface_tags") | List, items: Dictionary |  |  |  | List of interface tags that should be generated. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "generate_cv_tags.interface_tags.[].name") | String | Required, Unique |  |  | Tag name to be assigned to generated tags. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;data_path</samp>](## "generate_cv_tags.interface_tags.[].data_path") | String |  |  |  | Structured config field/key path to be used to find the value for the tag. Dot notation is supported to reference values inside dictionaries.<br>For Example: 'data_path: channel_group.id' would set the tag with the value of the channel id of the interface. If there is no channel id, the tag is not created.<br>`data_path` is ignored if `value` is set. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;value</samp>](## "generate_cv_tags.interface_tags.[].value") | String |  |  |  | Value to be assigned to the tag. |
    | [<samp>&nbsp;&nbsp;device_tags</samp>](## "generate_cv_tags.device_tags") | List, items: Dictionary |  |  |  | List of device tags that should be generated. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "generate_cv_tags.device_tags.[].name") | String | Required |  |  | Tag name to be assigned to generated tags. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;data_path</samp>](## "generate_cv_tags.device_tags.[].data_path") | String |  |  |  | Structured config field/key path to be used to find the value for the tag. Dot notation is supported to reference values inside dictionaries.<br>For Example: 'data_path: router_bfd.multihop.interval' would set the tag with the value of the interval for multihop bfd. If this value is not specified in the structured config, the tag is not created.<br>`data_path` is ignored if `value` is set. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;value</samp>](## "generate_cv_tags.device_tags.[].value") | String |  |  |  | Value to be assigned to the tag. |
    | [<samp>custom_node_type_keys</samp>](## "custom_node_type_keys") | List, items: Dictionary |  |  |  | Define Custom Node Type Keys, to specify the properties of each node type in the fabric.<br>This allows for complete customization of the fabric layout and functionality.<br>`custom_node_type_keys` should be defined in top level group_var for the fabric.<br>These values will be combined with the defaults; custom node type keys named the same as a<br>default node_type_key will replace the default. |
    | [<samp>&nbsp;&nbsp;-&nbsp;key</samp>](## "custom_node_type_keys.[].key") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;cv_tags_topology_type</samp>](## "custom_node_type_keys.[].cv_tags_topology_type") | String |  |  |  | Device type that CloudVision should use when generating the Topology like "leaf", "spine", "core", "edge" or "member-leaf". |
    | [<samp>node_type_keys</samp>](## "node_type_keys") | List, items: Dictionary |  | See (+) on YAML tab |  | Define Node Type Keys, to specify the properties of each node type in the fabric.<br>This allows for complete customization of the fabric layout and functionality.<br>`node_type_keys` should be defined in top level group_var for the fabric.<br><br>The default values will be overridden if this key is defined.<br>If you need to change all the existing `node_type_keys`, it is recommended to copy the defaults and modify them.<br>If you need to add custom `node_type_keys`, create them under `custom_node_type_keys` - if named identically to default `node_type_keys` entries,<br>custom entries will replace the equivalent default entry. |
    | [<samp>&nbsp;&nbsp;-&nbsp;key</samp>](## "node_type_keys.[].key") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;cv_tags_topology_type</samp>](## "node_type_keys.[].cv_tags_topology_type") | String |  |  |  | Device type that CloudVision should use when generating the Topology like "leaf", "spine", "core", "edge" or "member-leaf". |

=== "YAML"

    ```yaml
    # Device type that CloudVision should use when generating the Topology like "leaf", "spine", "core", "edge" or "member-leaf". Defaults to the setting under node_type_keys.
    cv_tags_topology_type: <str>

    # Generate CloudVision Tags based on AVD data.
    generate_cv_tags:

      # Enable the generation of CloudVision Topology Tags (hints).
      topology_hints: <bool; default=False>

      # PREVIEW: This option is marked as "preview", meaning the data models or generated configuration can change at any time.
      # Generate CloudVision device and interface Topology Tags for Campus fabric devices.
      # Device is treated as a Campus fabric device if:
      #   - The `campus` variable is assigned, either as native Ansible variable or as part of the `<node_type_keys.key>` AVD data construct.
      #   - The `generate_cv_tags.campus_fabric` variable is set to `True`.
      # When campus-related tags are generated for a device, generation of the DC-related tags is automatically disabled for that device.
      # AVD generates the following device tags for the Campus fabric devices based on the provided Campus-related input variables:
      #   - `Campus`
      #   - `Campus-Pod`
      #   - `Access-Pod`
      #   - `topology_hint_type`
      #   - `Role`
      # These tags are later used by CloudVision to render the correct network layout in the Topology view (`campusV2` network hierarchy) and Campus dashboards.
      campus_fabric: <bool; default=False>

      # List of interface tags that should be generated.
      interface_tags:

          # Tag name to be assigned to generated tags.
        - name: <str; required; unique>

          # Structured config field/key path to be used to find the value for the tag. Dot notation is supported to reference values inside dictionaries.
          # For Example: 'data_path: channel_group.id' would set the tag with the value of the channel id of the interface. If there is no channel id, the tag is not created.
          # `data_path` is ignored if `value` is set.
          data_path: <str>

          # Value to be assigned to the tag.
          value: <str>

      # List of device tags that should be generated.
      device_tags:

          # Tag name to be assigned to generated tags.
        - name: <str; required>

          # Structured config field/key path to be used to find the value for the tag. Dot notation is supported to reference values inside dictionaries.
          # For Example: 'data_path: router_bfd.multihop.interval' would set the tag with the value of the interval for multihop bfd. If this value is not specified in the structured config, the tag is not created.
          # `data_path` is ignored if `value` is set.
          data_path: <str>

          # Value to be assigned to the tag.
          value: <str>

    # Define Custom Node Type Keys, to specify the properties of each node type in the fabric.
    # This allows for complete customization of the fabric layout and functionality.
    # `custom_node_type_keys` should be defined in top level group_var for the fabric.
    # These values will be combined with the defaults; custom node type keys named the same as a
    # default node_type_key will replace the default.
    custom_node_type_keys:
      - key: <str; required; unique>

        # Device type that CloudVision should use when generating the Topology like "leaf", "spine", "core", "edge" or "member-leaf".
        cv_tags_topology_type: <str>

    # Define Node Type Keys, to specify the properties of each node type in the fabric.
    # This allows for complete customization of the fabric layout and functionality.
    # `node_type_keys` should be defined in top level group_var for the fabric.
    #
    # The default values will be overridden if this key is defined.
    # If you need to change all the existing `node_type_keys`, it is recommended to copy the defaults and modify them.
    # If you need to add custom `node_type_keys`, create them under `custom_node_type_keys` - if named identically to default `node_type_keys` entries,
    # custom entries will replace the equivalent default entry.
    node_type_keys: # (1)!
      - key: <str; required; unique>

        # Device type that CloudVision should use when generating the Topology like "leaf", "spine", "core", "edge" or "member-leaf".
        cv_tags_topology_type: <str>
    ```

    1. Default Value

        ```yaml
        node_type_keys:
        - key: spine
          type: spine
          default_evpn_role: server
          default_ptp_priority1: 20
          cv_tags_topology_type: spine
        - key: l3leaf
          type: l3leaf
          connected_endpoints: true
          default_evpn_role: client
          mlag_support: true
          network_services:
            l2: true
            l3: true
          vtep: true
          default_ptp_priority1: 30
          cv_tags_topology_type: leaf
        - key: l2leaf
          type: l2leaf
          connected_endpoints: true
          mlag_support: true
          network_services:
            l2: true
          underlay_router: false
          uplink_type: port-channel
          cv_tags_topology_type: leaf
        - key: p
          type: p
          mpls_lsr: true
          default_mpls_overlay_role: none
          default_overlay_routing_protocol: ibgp
          default_underlay_routing_protocol: isis-sr
        - key: pe
          type: pe
          mpls_lsr: true
          connected_endpoints: true
          default_mpls_overlay_role: client
          default_evpn_role: client
          network_services:
            l1: true
            l2: true
            l3: true
          default_overlay_routing_protocol: ibgp
          default_underlay_routing_protocol: isis-sr
          default_overlay_address_families:
          - vpn-ipv4
          default_evpn_encapsulation: mpls
        - key: rr
          type: rr
          mpls_lsr: true
          default_mpls_overlay_role: server
          default_evpn_role: server
          default_overlay_routing_protocol: ibgp
          default_underlay_routing_protocol: isis-sr
          default_overlay_address_families:
          - vpn-ipv4
          default_evpn_encapsulation: mpls
        - key: l3spine
          type: l3spine
          connected_endpoints: true
          mlag_support: true
          network_services:
            l2: true
            l3: true
          default_overlay_routing_protocol: none
          default_underlay_routing_protocol: none
          cv_tags_topology_type: spine
        - key: leaf
          type: leaf
          connected_endpoints: true
          mlag_support: true
          network_services:
            l2: true,
          underlay_router: false
          uplink_type: port-channel
          cv_tags_topology_type: leaf
        - key: l2spine
          type: l2spine
          connected_endpoints: true
          mlag_support: true
          network_services:
            l2: true
          underlay_router: false
          uplink_type: port-channel
          cv_tags_topology_type: spine
        - key: super_spine
          type: super-spine
          cv_tags_topology_type: core
        - key: overlay_controller
          type: overlay-controller
          default_evpn_role: server
          cv_tags_topology_type: spine
        - key: wan_router
          type: wan_router
          default_evpn_role: client
          default_wan_role: client
          default_underlay_routing_protocol: none
          default_overlay_routing_protocol: ibgp
          default_flow_tracker_type: hardware
          vtep: true
          network_services:
            l3: true
        - key: wan_rr
          type: wan_rr
          default_evpn_role: server
          default_wan_role: server
          default_underlay_routing_protocol: none
          default_overlay_routing_protocol: ibgp
          default_flow_tracker_type: hardware
          vtep: true
          network_services:
            l3: true,
        ```
