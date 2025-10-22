<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>campus</samp>](## "campus") | String |  |  |  | PREVIEW: This option is marked as "preview", meaning the data models or generated configuration can change at any time.<br>Name of the Campus fabric.<br>Used to generate CloudVision device tags with the `generate_cv_tags.campus_fabric` feature. |
    | [<samp>campus_access_pod</samp>](## "campus_access_pod") | String |  |  |  | PREVIEW: This option is marked as "preview", meaning the data models or generated configuration can change at any time.<br>Name of the Campus access pod.<br>Used to generate CloudVision device tags with the `generate_cv_tags.campus_fabric` feature. |
    | [<samp>campus_pod</samp>](## "campus_pod") | String |  |  |  | PREVIEW: This option is marked as "preview", meaning the data models or generated configuration can change at any time.<br>Name of the Campus pod.<br>Used to generate CloudVision device tags with the `generate_cv_tags.campus_fabric` feature. |
    | [<samp>dc_name</samp>](## "dc_name") | String |  |  |  | DC Name is used in:<br>- Fabric Documentation (Optional, falls back to fabric_name)<br>- SNMP Location: `snmp_settings.location` (Optional)<br>- HER Overlay DC scoped flood lists: `overlay_her_flood_list_scope: dc` (Required)<br> |
    | [<samp>fabric_name</samp>](## "fabric_name") | String | Required |  |  | Fabric Name, required to match Ansible Group name covering all devices in the Fabric, **must** be an inventory group name. |
    | [<samp>pod_name</samp>](## "pod_name") | String |  |  |  | POD Name is used in:<br>- Fabric Documentation (Optional, falls back to dc_name and then to fabric_name)<br>- SNMP Location: `snmp_settings.location` (Optional)<br>- VRF Loopbacks: `vtep_diagnostic.loopback_ip_pools.pod` (Required)<br><br>Recommended to be common between Spines and Leafs within a POD (One l3ls topology).<br> |

=== "YAML"

    ```yaml
    # PREVIEW: This option is marked as "preview", meaning the data models or generated configuration can change at any time.
    # Name of the Campus fabric.
    # Used to generate CloudVision device tags with the `generate_cv_tags.campus_fabric` feature.
    campus: <str>

    # PREVIEW: This option is marked as "preview", meaning the data models or generated configuration can change at any time.
    # Name of the Campus access pod.
    # Used to generate CloudVision device tags with the `generate_cv_tags.campus_fabric` feature.
    campus_access_pod: <str>

    # PREVIEW: This option is marked as "preview", meaning the data models or generated configuration can change at any time.
    # Name of the Campus pod.
    # Used to generate CloudVision device tags with the `generate_cv_tags.campus_fabric` feature.
    campus_pod: <str>

    # DC Name is used in:
    # - Fabric Documentation (Optional, falls back to fabric_name)
    # - SNMP Location: `snmp_settings.location` (Optional)
    # - HER Overlay DC scoped flood lists: `overlay_her_flood_list_scope: dc` (Required)
    dc_name: <str>

    # Fabric Name, required to match Ansible Group name covering all devices in the Fabric, **must** be an inventory group name.
    fabric_name: <str; required>

    # POD Name is used in:
    # - Fabric Documentation (Optional, falls back to dc_name and then to fabric_name)
    # - SNMP Location: `snmp_settings.location` (Optional)
    # - VRF Loopbacks: `vtep_diagnostic.loopback_ip_pools.pod` (Required)
    #
    # Recommended to be common between Spines and Leafs within a POD (One l3ls topology).
    pod_name: <str>
    ```
