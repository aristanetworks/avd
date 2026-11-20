<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>&lt;node_type_keys.key&gt;</samp>](## "<node_type_keys.key>") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;defaults</samp>](## "<node_type_keys.key>.defaults") | Dictionary |  |  |  | Define variables for all nodes of this type. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;site</samp>](## "<node_type_keys.key>.defaults.site") | String |  |  |  | Physical building or data center facility where the switch is located. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;location</samp>](## "<node_type_keys.key>.defaults.location") | String |  |  |  | Room, floor, data hall, or cage within the site where the switch is located. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;row</samp>](## "<node_type_keys.key>.defaults.row") | String |  |  |  | Row within the location where the switch is located. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;rack</samp>](## "<node_type_keys.key>.defaults.rack") | String |  |  |  | Rack within the row where the switch is located.<br>Used for CloudVision topology tags and SNMP location settings when enabled. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;rack_unit</samp>](## "<node_type_keys.key>.defaults.rack_unit") | String |  |  |  | Rack unit or range of rack units occupied by the switch. |
    | [<samp>&nbsp;&nbsp;node_groups</samp>](## "<node_type_keys.key>.node_groups") | List, items: Dictionary |  |  |  | Define variables related to all nodes part of this group. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;group</samp>](## "<node_type_keys.key>.node_groups.[].group") | String | Required, Unique |  |  | The Node Group Name is used for MLAG domain unless set with 'mlag_domain_id'.<br>The Node Group Name is also used for peer description on downstream switches' uplinks.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "<node_type_keys.key>.node_groups.[].nodes") | List, items: Dictionary |  |  |  | Define variables per node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].name") | String | Required, Unique |  |  | The Node Name is used as "hostname". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;site</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].site") | String |  |  |  | Physical building or data center facility where the switch is located. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;location</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].location") | String |  |  |  | Room, floor, data hall, or cage within the site where the switch is located. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;row</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].row") | String |  |  |  | Row within the location where the switch is located. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rack</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].rack") | String |  |  |  | Rack within the row where the switch is located.<br>Used for CloudVision topology tags and SNMP location settings when enabled. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rack_unit</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].rack_unit") | String |  |  |  | Rack unit or range of rack units occupied by the switch. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;site</samp>](## "<node_type_keys.key>.node_groups.[].site") | String |  |  |  | Physical building or data center facility where the switch is located. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;location</samp>](## "<node_type_keys.key>.node_groups.[].location") | String |  |  |  | Room, floor, data hall, or cage within the site where the switch is located. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;row</samp>](## "<node_type_keys.key>.node_groups.[].row") | String |  |  |  | Row within the location where the switch is located. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rack</samp>](## "<node_type_keys.key>.node_groups.[].rack") | String |  |  |  | Rack within the row where the switch is located.<br>Used for CloudVision topology tags and SNMP location settings when enabled. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rack_unit</samp>](## "<node_type_keys.key>.node_groups.[].rack_unit") | String |  |  |  | Rack unit or range of rack units occupied by the switch. |
    | [<samp>&nbsp;&nbsp;nodes</samp>](## "<node_type_keys.key>.nodes") | List, items: Dictionary |  |  |  | Define variables per node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "<node_type_keys.key>.nodes.[].name") | String | Required, Unique |  |  | The Node Name is used as "hostname". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;site</samp>](## "<node_type_keys.key>.nodes.[].site") | String |  |  |  | Physical building or data center facility where the switch is located. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;location</samp>](## "<node_type_keys.key>.nodes.[].location") | String |  |  |  | Room, floor, data hall, or cage within the site where the switch is located. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;row</samp>](## "<node_type_keys.key>.nodes.[].row") | String |  |  |  | Row within the location where the switch is located. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rack</samp>](## "<node_type_keys.key>.nodes.[].rack") | String |  |  |  | Rack within the row where the switch is located.<br>Used for CloudVision topology tags and SNMP location settings when enabled. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rack_unit</samp>](## "<node_type_keys.key>.nodes.[].rack_unit") | String |  |  |  | Rack unit or range of rack units occupied by the switch. |
    | [<samp>device_profiles</samp>](## "device_profiles") | List, items: Dictionary |  |  |  | PREVIEW - This datamodel is still under development and may change or get removed at any time. |
    | [<samp>&nbsp;&nbsp;-&nbsp;name</samp>](## "device_profiles.[].name") | String | Required, Unique |  |  | Profile Name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;site</samp>](## "device_profiles.[].site") | String |  |  |  | Physical building or data center facility where the switch is located. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;location</samp>](## "device_profiles.[].location") | String |  |  |  | Room, floor, data hall, or cage within the site where the switch is located. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;row</samp>](## "device_profiles.[].row") | String |  |  |  | Row within the location where the switch is located. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;rack</samp>](## "device_profiles.[].rack") | String |  |  |  | Rack within the row where the switch is located.<br>Used for CloudVision topology tags and SNMP location settings when enabled. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;rack_unit</samp>](## "device_profiles.[].rack_unit") | String |  |  |  | Rack unit or range of rack units occupied by the switch. |
    | [<samp>devices</samp>](## "devices") | List, items: Dictionary |  |  |  | PREVIEW - This datamodel is still under development and may change or get removed at any time. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "devices.[].name") | String | Required, Unique |  |  | The Node Name is used as "hostname". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;site</samp>](## "devices.[].site") | String |  |  |  | Physical building or data center facility where the switch is located. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;location</samp>](## "devices.[].location") | String |  |  |  | Room, floor, data hall, or cage within the site where the switch is located. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;row</samp>](## "devices.[].row") | String |  |  |  | Row within the location where the switch is located. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;rack</samp>](## "devices.[].rack") | String |  |  |  | Rack within the row where the switch is located.<br>Used for CloudVision topology tags and SNMP location settings when enabled. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;rack_unit</samp>](## "devices.[].rack_unit") | String |  |  |  | Rack unit or range of rack units occupied by the switch. |

=== "YAML"

    ```yaml
    <node_type_keys.key>:

      # Define variables for all nodes of this type.
      defaults:

        # Physical building or data center facility where the switch is located.
        site: <str>

        # Room, floor, data hall, or cage within the site where the switch is located.
        location: <str>

        # Row within the location where the switch is located.
        row: <str>

        # Rack within the row where the switch is located.
        # Used for CloudVision topology tags and SNMP location settings when enabled.
        rack: <str>

        # Rack unit or range of rack units occupied by the switch.
        rack_unit: <str>

      # Define variables related to all nodes part of this group.
      node_groups:

          # The Node Group Name is used for MLAG domain unless set with 'mlag_domain_id'.
          # The Node Group Name is also used for peer description on downstream switches' uplinks.
        - group: <str; required; unique>

          # Define variables per node.
          nodes:

              # The Node Name is used as "hostname".
            - name: <str; required; unique>

              # Physical building or data center facility where the switch is located.
              site: <str>

              # Room, floor, data hall, or cage within the site where the switch is located.
              location: <str>

              # Row within the location where the switch is located.
              row: <str>

              # Rack within the row where the switch is located.
              # Used for CloudVision topology tags and SNMP location settings when enabled.
              rack: <str>

              # Rack unit or range of rack units occupied by the switch.
              rack_unit: <str>

          # Physical building or data center facility where the switch is located.
          site: <str>

          # Room, floor, data hall, or cage within the site where the switch is located.
          location: <str>

          # Row within the location where the switch is located.
          row: <str>

          # Rack within the row where the switch is located.
          # Used for CloudVision topology tags and SNMP location settings when enabled.
          rack: <str>

          # Rack unit or range of rack units occupied by the switch.
          rack_unit: <str>

      # Define variables per node.
      nodes:

          # The Node Name is used as "hostname".
        - name: <str; required; unique>

          # Physical building or data center facility where the switch is located.
          site: <str>

          # Room, floor, data hall, or cage within the site where the switch is located.
          location: <str>

          # Row within the location where the switch is located.
          row: <str>

          # Rack within the row where the switch is located.
          # Used for CloudVision topology tags and SNMP location settings when enabled.
          rack: <str>

          # Rack unit or range of rack units occupied by the switch.
          rack_unit: <str>

    # PREVIEW - This datamodel is still under development and may change or get removed at any time.
    device_profiles:

        # Profile Name
      - name: <str; required; unique>

        # Physical building or data center facility where the switch is located.
        site: <str>

        # Room, floor, data hall, or cage within the site where the switch is located.
        location: <str>

        # Row within the location where the switch is located.
        row: <str>

        # Rack within the row where the switch is located.
        # Used for CloudVision topology tags and SNMP location settings when enabled.
        rack: <str>

        # Rack unit or range of rack units occupied by the switch.
        rack_unit: <str>

    # PREVIEW - This datamodel is still under development and may change or get removed at any time.
    devices:

        # The Node Name is used as "hostname".
        name: <str; required; unique>

        # Physical building or data center facility where the switch is located.
        site: <str>

        # Room, floor, data hall, or cage within the site where the switch is located.
        location: <str>

        # Row within the location where the switch is located.
        row: <str>

        # Rack within the row where the switch is located.
        # Used for CloudVision topology tags and SNMP location settings when enabled.
        rack: <str>

        # Rack unit or range of rack units occupied by the switch.
        rack_unit: <str>
    ```
