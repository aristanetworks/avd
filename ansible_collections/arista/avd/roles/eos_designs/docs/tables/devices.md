<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
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
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;kernel_ecmp_cli</samp>](## "device_profiles.[].kernel_ecmp_cli") | Boolean |  | `True` |  | Use EOS CLI to configure kernel forwarding ECMP programming.<br>For EOS kernel forwarding, ECMP programming can be enabled in two different ways, depending on the EOS version.<br>- For newer EOS versions (starting 4.33.2) use the proper CLI.<br>- For older EOS versions use an agent environment variable. Changing this requires restarting the KernelFib agent. |
    | [<samp>devices</samp>](## "devices") | List, items: Dictionary |  |  |  | PREVIEW - This datamodel is still under development and may change or get removed at any time. |
    | [<samp>&nbsp;&nbsp;-&nbsp;profile</samp>](## "devices.[].profile") | String |  |  |  | Inherit settings from a profile defined under `device_profiles`.<br>Max two levels of profile inheritance: device -> profile -> parent_profile<br>This takes precedence over the global `device_profile` key. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "devices.[].type") | String |  |  |  | Set the type of the device as defined under `node_type_keys`.<br>This takes precedence over the global `type` key. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mlag_group</samp>](## "devices.[].mlag_group") | String |  |  |  | Name of MLAG group. Exactly two devices must share the same mlag_group.<br>The group is used for creating MLAG Pairs, for port-channel descriptions on peers and for MLAG domain-id (unless mlag_domain_id is set). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "devices.[].name") | String | Required, Unique |  |  | The Node Name is used as "hostname". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;kernel_ecmp_cli</samp>](## "devices.[].kernel_ecmp_cli") | Boolean |  | `True` |  | Use EOS CLI to configure kernel forwarding ECMP programming.<br>For EOS kernel forwarding, ECMP programming can be enabled in two different ways, depending on the EOS version.<br>- For newer EOS versions (starting 4.33.2) use the proper CLI.<br>- For older EOS versions use an agent environment variable. Changing this requires restarting the KernelFib agent. |

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

        # Use EOS CLI to configure kernel forwarding ECMP programming.
        # For EOS kernel forwarding, ECMP programming can be enabled in two different ways, depending on the EOS version.
        # - For newer EOS versions (starting 4.33.2) use the proper CLI.
        # - For older EOS versions use an agent environment variable. Changing this requires restarting the KernelFib agent.
        kernel_ecmp_cli: <bool; default=True>

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

        # Use EOS CLI to configure kernel forwarding ECMP programming.
        # For EOS kernel forwarding, ECMP programming can be enabled in two different ways, depending on the EOS version.
        # - For newer EOS versions (starting 4.33.2) use the proper CLI.
        # - For older EOS versions use an agent environment variable. Changing this requires restarting the KernelFib agent.
        kernel_ecmp_cli: <bool; default=True>
    ```
