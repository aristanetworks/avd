<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>digital_twin</samp>](## "digital_twin") | Dictionary |  |  |  | PREVIEW: This option is marked as "preview", meaning the data models or generated configuration can change at any time.<br>Global settings to configure the Digital Twin of the Fabric. |
    | [<samp>&nbsp;&nbsp;environment</samp>](## "digital_twin.environment") | String |  | `act` | Valid Values:<br>- <code>act</code> | Targeted Digital Twin environment. |
    | [<samp>&nbsp;&nbsp;act_cloudeos_username</samp>](## "digital_twin.act_cloudeos_username") | String |  | `cvpadmin` |  | Username for ACT Digital Twin 'cloudeos' nodes. |
    | [<samp>&nbsp;&nbsp;act_cloudeos_password</samp>](## "digital_twin.act_cloudeos_password") | String |  | `cvp123!` |  | Password for ACT Digital Twin 'cloudeos' nodes. |
    | [<samp>&nbsp;&nbsp;act_cloudeos_os_version</samp>](## "digital_twin.act_cloudeos_os_version") | String |  | `4.33.2F` |  | OS version for ACT Digital Twin 'cloudeos' nodes. |
    | [<samp>&nbsp;&nbsp;act_cvp_username</samp>](## "digital_twin.act_cvp_username") | String |  | `root` |  | Username for ACT Digital Twin 'cvp' nodes. |
    | [<samp>&nbsp;&nbsp;act_cvp_password</samp>](## "digital_twin.act_cvp_password") | String |  | `cvproot` |  | Password for ACT Digital Twin 'cvp' nodes. |
    | [<samp>&nbsp;&nbsp;act_cvp_os_version</samp>](## "digital_twin.act_cvp_os_version") | String |  | `2024.3.2` |  | OS version for ACT Digital Twin 'cvp' nodes. |
    | [<samp>&nbsp;&nbsp;act_generic_username</samp>](## "digital_twin.act_generic_username") | String |  | `ansible` |  | Username for ACT Digital Twin 'generic' nodes. |
    | [<samp>&nbsp;&nbsp;act_generic_password</samp>](## "digital_twin.act_generic_password") | String |  | `ansible` |  | Password for ACT Digital Twin 'generic' nodes. |
    | [<samp>&nbsp;&nbsp;act_generic_os_version</samp>](## "digital_twin.act_generic_os_version") | String |  | `ubuntu-2204-lts` |  | OS version for ACT Digital Twin 'generic' nodes. |
    | [<samp>&nbsp;&nbsp;act_third_party_username</samp>](## "digital_twin.act_third_party_username") | String |  | `ansible` |  | Username for ACT Digital Twin 'third-party' nodes. |
    | [<samp>&nbsp;&nbsp;act_third_party_password</samp>](## "digital_twin.act_third_party_password") | String |  | `ansible` |  | Password for ACT Digital Twin 'third-party' nodes. |
    | [<samp>&nbsp;&nbsp;act_third_party_os_version</samp>](## "digital_twin.act_third_party_os_version") | String |  | `byod` |  | OS version for ACT Digital Twin 'third-party' nodes. |
    | [<samp>&nbsp;&nbsp;act_tools_server_username</samp>](## "digital_twin.act_tools_server_username") | String |  | `ansible` |  | Username for ACT Digital Twin 'tools-server' nodes. |
    | [<samp>&nbsp;&nbsp;act_tools_server_password</samp>](## "digital_twin.act_tools_server_password") | String |  | `ansible` |  | Password for ACT Digital Twin 'tools-server' nodes. |
    | [<samp>&nbsp;&nbsp;act_tools_server_os_version</samp>](## "digital_twin.act_tools_server_os_version") | String |  | `ubuntu-2204-lts` |  | OS version for ACT Digital Twin 'tools-server' nodes. |
    | [<samp>&nbsp;&nbsp;act_veos_username</samp>](## "digital_twin.act_veos_username") | String |  | `cvpadmin` |  | Username for ACT Digital Twin 'veos' nodes. |
    | [<samp>&nbsp;&nbsp;act_veos_password</samp>](## "digital_twin.act_veos_password") | String |  | `cvp123!` |  | Password for ACT Digital Twin 'veos' nodes. |
    | [<samp>&nbsp;&nbsp;act_veos_os_version</samp>](## "digital_twin.act_veos_os_version") | String |  | `4.33.1.1F` |  | OS version for ACT Digital Twin 'veos' nodes. |
    | [<samp>&nbsp;&nbsp;auxiliary_systems</samp>](## "digital_twin.auxiliary_systems") | List, items: Dictionary |  |  |  | Auxiliary systems (e.g., CloudVision portal, general Linux servers) deployed as part of the Digital Twin infrastructure alongside the fabric devices.<br>Specific auxiliary system will be rendered only if their 'node_type' is matching the targeted Digital Twin environment. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;node_name</samp>](## "digital_twin.auxiliary_systems.[].node_name") | String | Required |  |  | Name of the auxiliary system. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;node_type</samp>](## "digital_twin.auxiliary_systems.[].node_type") | String | Required |  | Valid Values:<br>- <code>act-tools-server</code> | Node type of the auxiliary system.<br>Naming convention: '<digital_twin_environment>-<node_type>'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;act_os_version</samp>](## "digital_twin.auxiliary_systems.[].act_os_version") | String |  |  |  | OS version of the auxiliary system.<br>Overrides parent `digital_twin.act_<node_type>_os_version` value. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;act_mgmt_ip</samp>](## "digital_twin.auxiliary_systems.[].act_mgmt_ip") | String |  |  | Format: cidr | Management interface IPv4 address of the auxiliary system.<br>Required for ACT auxiliary system. |

=== "YAML"

    ```yaml
    # PREVIEW: This option is marked as "preview", meaning the data models or generated configuration can change at any time.
    # Global settings to configure the Digital Twin of the Fabric.
    digital_twin:

      # Targeted Digital Twin environment.
      environment: <str; "act"; default="act">

      # Username for ACT Digital Twin 'cloudeos' nodes.
      act_cloudeos_username: <str; default="cvpadmin">

      # Password for ACT Digital Twin 'cloudeos' nodes.
      act_cloudeos_password: <str; default="cvp123!">

      # OS version for ACT Digital Twin 'cloudeos' nodes.
      act_cloudeos_os_version: <str; default="4.33.2F">

      # Username for ACT Digital Twin 'cvp' nodes.
      act_cvp_username: <str; default="root">

      # Password for ACT Digital Twin 'cvp' nodes.
      act_cvp_password: <str; default="cvproot">

      # OS version for ACT Digital Twin 'cvp' nodes.
      act_cvp_os_version: <str; default="2024.3.2">

      # Username for ACT Digital Twin 'generic' nodes.
      act_generic_username: <str; default="ansible">

      # Password for ACT Digital Twin 'generic' nodes.
      act_generic_password: <str; default="ansible">

      # OS version for ACT Digital Twin 'generic' nodes.
      act_generic_os_version: <str; default="ubuntu-2204-lts">

      # Username for ACT Digital Twin 'third-party' nodes.
      act_third_party_username: <str; default="ansible">

      # Password for ACT Digital Twin 'third-party' nodes.
      act_third_party_password: <str; default="ansible">

      # OS version for ACT Digital Twin 'third-party' nodes.
      act_third_party_os_version: <str; default="byod">

      # Username for ACT Digital Twin 'tools-server' nodes.
      act_tools_server_username: <str; default="ansible">

      # Password for ACT Digital Twin 'tools-server' nodes.
      act_tools_server_password: <str; default="ansible">

      # OS version for ACT Digital Twin 'tools-server' nodes.
      act_tools_server_os_version: <str; default="ubuntu-2204-lts">

      # Username for ACT Digital Twin 'veos' nodes.
      act_veos_username: <str; default="cvpadmin">

      # Password for ACT Digital Twin 'veos' nodes.
      act_veos_password: <str; default="cvp123!">

      # OS version for ACT Digital Twin 'veos' nodes.
      act_veos_os_version: <str; default="4.33.1.1F">

      # Auxiliary systems (e.g., CloudVision portal, general Linux servers) deployed as part of the Digital Twin infrastructure alongside the fabric devices.
      # Specific auxiliary system will be rendered only if their 'node_type' is matching the targeted Digital Twin environment.
      auxiliary_systems:

          # Name of the auxiliary system.
        - node_name: <str; required>

          # Node type of the auxiliary system.
          # Naming convention: '<digital_twin_environment>-<node_type>'.
          node_type: <str; "act-tools-server"; required>

          # OS version of the auxiliary system.
          # Overrides parent `digital_twin.act_<node_type>_os_version` value.
          act_os_version: <str>

          # Management interface IPv4 address of the auxiliary system.
          # Required for ACT auxiliary system.
          act_mgmt_ip: <str>
    ```
