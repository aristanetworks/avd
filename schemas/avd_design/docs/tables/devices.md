<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>device_profile</samp>](## "device_profile") | String |  |  |  | PREVIEW - This datamodel is still under development and may change or get removed at any time.<br>Inherit settings from a device profile defined under `device_profiles`.<br>If the device is defined under `devices` it is recommended to set the `profile` there instead.<br>Max two levels of profile inheritance: device -> profile -> parent_profile |
    | [<samp>device_profiles</samp>](## "device_profiles") | List, items: Dictionary |  |  |  | PREVIEW - This datamodel is still under development and may change or get removed at any time. |
    | [<samp>&nbsp;&nbsp;-&nbsp;name</samp>](## "device_profiles.[].name") | String | Required, Unique |  |  | Profile Name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;parent_profile</samp>](## "device_profiles.[].parent_profile") | String |  |  |  | Inherit settings from a parent profile defined under `device_profiles`.<br>Max two levels of profile inheritance: device -> profile -> parent_profile |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "device_profiles.[].type") | String |  |  |  | Set the type of the device as defined under `node_type_keys`.<br>This takes precedence over the global `type` key. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mlag_group</samp>](## "device_profiles.[].mlag_group") | String |  |  |  | Name of MLAG group. Exactly two devices must share the same mlag_group.<br>The group is used for creating MLAG Pairs, for port-channel descriptions on peers and for MLAG domain-id (unless mlag_domain_id is set). |
    | [<samp>devices</samp>](## "devices") | List, items: Dictionary |  |  |  | PREVIEW - This datamodel is still under development and may change or get removed at any time. |
    | [<samp>&nbsp;&nbsp;-&nbsp;profile</samp>](## "devices.[].profile") | String |  |  |  | Inherit settings from a profile defined under `device_profiles`.<br>Max two levels of profile inheritance: device -> profile -> parent_profile<br>This takes precedence over the global `device_profile` key. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "devices.[].type") | String |  |  |  | Set the type of the device as defined under `node_type_keys`.<br>This takes precedence over the global `type` key. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mlag_group</samp>](## "devices.[].mlag_group") | String |  |  |  | Name of MLAG group. Exactly two devices must share the same mlag_group.<br>The group is used for creating MLAG Pairs, for port-channel descriptions on peers and for MLAG domain-id (unless mlag_domain_id is set). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "devices.[].name") | String | Required, Unique |  |  | The Node Name is used as "hostname". |

=== "YAML"

    ```yaml
    # PREVIEW - This datamodel is still under development and may change or get removed at any time.
    # Inherit settings from a device profile defined under `device_profiles`.
    # If the device is defined under `devices` it is recommended to set the `profile` there instead.
    # Max two levels of profile inheritance: device -> profile -> parent_profile
    device_profile: <str>

    # PREVIEW - This datamodel is still under development and may change or get removed at any time.
    device_profiles:

        # Profile Name
      - name: <str; required; unique>

        # Inherit settings from a parent profile defined under `device_profiles`.
        # Max two levels of profile inheritance: device -> profile -> parent_profile
        parent_profile: <str>

        # Set the type of the device as defined under `node_type_keys`.
        # This takes precedence over the global `type` key.
        type: <str>

        # Name of MLAG group. Exactly two devices must share the same mlag_group.
        # The group is used for creating MLAG Pairs, for port-channel descriptions on peers and for MLAG domain-id (unless mlag_domain_id is set).
        mlag_group: <str>

    # PREVIEW - This datamodel is still under development and may change or get removed at any time.
    devices:

        # Inherit settings from a profile defined under `device_profiles`.
        # Max two levels of profile inheritance: device -> profile -> parent_profile
        # This takes precedence over the global `device_profile` key.
      - profile: <str>

        # Set the type of the device as defined under `node_type_keys`.
        # This takes precedence over the global `type` key.
        type: <str>

        # Name of MLAG group. Exactly two devices must share the same mlag_group.
        # The group is used for creating MLAG Pairs, for port-channel descriptions on peers and for MLAG domain-id (unless mlag_domain_id is set).
        mlag_group: <str>

        # The Node Name is used as "hostname".
        name: <str; required; unique>
    ```
