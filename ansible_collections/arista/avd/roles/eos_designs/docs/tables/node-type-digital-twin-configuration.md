<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>&lt;node_type_keys.key&gt;</samp>](## "<node_type_keys.key>") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;defaults</samp>](## "<node_type_keys.key>.defaults") | Dictionary |  |  |  | Define variables for all nodes of this type. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;digital_twin</samp>](## "<node_type_keys.key>.defaults.digital_twin") | Dictionary |  |  |  | Set the OS version and management IP address for the digital twin of the associated node(s). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;os_version</samp>](## "<node_type_keys.key>.defaults.digital_twin.os_version") | String |  |  |  | Desired OS version.<br>Overrides global `digital_twin.fabric.os_version` flag. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mgmt_ip</samp>](## "<node_type_keys.key>.defaults.digital_twin.mgmt_ip") | String |  |  | Format: cidr | Desired management interface IPv4 address.<br>Overrides the dynamically generated (from the pool `digital_twin.fabric.mgmt_ipv4_pool`) Digital Twin MGMT IP. |
    | [<samp>&nbsp;&nbsp;node_groups</samp>](## "<node_type_keys.key>.node_groups") | List, items: Dictionary |  |  |  | Define variables related to all nodes part of this group. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;group</samp>](## "<node_type_keys.key>.node_groups.[].group") | String | Required, Unique |  |  | The Node Group Name is used for MLAG domain unless set with 'mlag_domain_id'.<br>The Node Group Name is also used for peer description on downstream switches' uplinks.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "<node_type_keys.key>.node_groups.[].nodes") | List, items: Dictionary |  |  |  | Define variables per node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].name") | String | Required, Unique |  |  | The Node Name is used as "hostname". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;digital_twin</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].digital_twin") | Dictionary |  |  |  | Set the OS version and management IP address for the digital twin of the associated node(s). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;os_version</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].digital_twin.os_version") | String |  |  |  | Desired OS version.<br>Overrides global `digital_twin.fabric.os_version` flag. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mgmt_ip</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].digital_twin.mgmt_ip") | String |  |  | Format: cidr | Desired management interface IPv4 address.<br>Overrides the dynamically generated (from the pool `digital_twin.fabric.mgmt_ipv4_pool`) Digital Twin MGMT IP. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;digital_twin</samp>](## "<node_type_keys.key>.node_groups.[].digital_twin") | Dictionary |  |  |  | Set the OS version and management IP address for the digital twin of the associated node(s). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;os_version</samp>](## "<node_type_keys.key>.node_groups.[].digital_twin.os_version") | String |  |  |  | Desired OS version.<br>Overrides global `digital_twin.fabric.os_version` flag. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mgmt_ip</samp>](## "<node_type_keys.key>.node_groups.[].digital_twin.mgmt_ip") | String |  |  | Format: cidr | Desired management interface IPv4 address.<br>Overrides the dynamically generated (from the pool `digital_twin.fabric.mgmt_ipv4_pool`) Digital Twin MGMT IP. |
    | [<samp>&nbsp;&nbsp;nodes</samp>](## "<node_type_keys.key>.nodes") | List, items: Dictionary |  |  |  | Define variables per node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "<node_type_keys.key>.nodes.[].name") | String | Required, Unique |  |  | The Node Name is used as "hostname". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;digital_twin</samp>](## "<node_type_keys.key>.nodes.[].digital_twin") | Dictionary |  |  |  | Set the OS version and management IP address for the digital twin of the associated node(s). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;os_version</samp>](## "<node_type_keys.key>.nodes.[].digital_twin.os_version") | String |  |  |  | Desired OS version.<br>Overrides global `digital_twin.fabric.os_version` flag. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mgmt_ip</samp>](## "<node_type_keys.key>.nodes.[].digital_twin.mgmt_ip") | String |  |  | Format: cidr | Desired management interface IPv4 address.<br>Overrides the dynamically generated (from the pool `digital_twin.fabric.mgmt_ipv4_pool`) Digital Twin MGMT IP. |

=== "YAML"

    ```yaml
    <node_type_keys.key>:

      # Define variables for all nodes of this type.
      defaults:

        # Set the OS version and management IP address for the digital twin of the associated node(s).
        digital_twin:

          # Desired OS version.
          # Overrides global `digital_twin.fabric.os_version` flag.
          os_version: <str>

          # Desired management interface IPv4 address.
          # Overrides the dynamically generated (from the pool `digital_twin.fabric.mgmt_ipv4_pool`) Digital Twin MGMT IP.
          mgmt_ip: <str>

      # Define variables related to all nodes part of this group.
      node_groups:

          # The Node Group Name is used for MLAG domain unless set with 'mlag_domain_id'.
          # The Node Group Name is also used for peer description on downstream switches' uplinks.
        - group: <str; required; unique>

          # Define variables per node.
          nodes:

              # The Node Name is used as "hostname".
            - name: <str; required; unique>

              # Set the OS version and management IP address for the digital twin of the associated node(s).
              digital_twin:

                # Desired OS version.
                # Overrides global `digital_twin.fabric.os_version` flag.
                os_version: <str>

                # Desired management interface IPv4 address.
                # Overrides the dynamically generated (from the pool `digital_twin.fabric.mgmt_ipv4_pool`) Digital Twin MGMT IP.
                mgmt_ip: <str>

          # Set the OS version and management IP address for the digital twin of the associated node(s).
          digital_twin:

            # Desired OS version.
            # Overrides global `digital_twin.fabric.os_version` flag.
            os_version: <str>

            # Desired management interface IPv4 address.
            # Overrides the dynamically generated (from the pool `digital_twin.fabric.mgmt_ipv4_pool`) Digital Twin MGMT IP.
            mgmt_ip: <str>

      # Define variables per node.
      nodes:

          # The Node Name is used as "hostname".
        - name: <str; required; unique>

          # Set the OS version and management IP address for the digital twin of the associated node(s).
          digital_twin:

            # Desired OS version.
            # Overrides global `digital_twin.fabric.os_version` flag.
            os_version: <str>

            # Desired management interface IPv4 address.
            # Overrides the dynamically generated (from the pool `digital_twin.fabric.mgmt_ipv4_pool`) Digital Twin MGMT IP.
            mgmt_ip: <str>
    ```
