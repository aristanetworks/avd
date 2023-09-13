<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>port_profiles</samp>](## "port_profiles") | List, items: Dictionary |  |  |  | Optional profiles to share common settings for connected_endpoints and/or network_ports.<br>Keys are the same used under endpoints adapters. Keys defined under endpoints adapters take precedence.<br> |
    | [<samp>&nbsp;&nbsp;- profile</samp>](## "port_profiles.[].profile") | String | Required, Unique |  |  | Port profile name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;parent_profile</samp>](## "port_profiles.[].parent_profile") | String |  |  |  | Parent profile is optional.<br>Port_profiles can refer to another port_profile to inherit settings in up to two levels (adapter->profile->parent_profile). |

=== "YAML"

    ```yaml
    # Optional profiles to share common settings for connected_endpoints and/or network_ports.
    # Keys are the same used under endpoints adapters. Keys defined under endpoints adapters take precedence.
    port_profiles:

        # Port profile name.
      - profile: <str; required; unique>

        # Parent profile is optional.
        # Port_profiles can refer to another port_profile to inherit settings in up to two levels (adapter->profile->parent_profile).
        parent_profile: <str>
    ```
