<!--
  ~ Copyright (c) 2024 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>default_network_ports_description</samp>](## "default_network_ports_description") | String |  | `{endpoint?}` |  | Default description or description template to be used on all ports defined under `network_ports`.<br>This can be a template using the format string syntax.<br>The available template fields are:<br>  - `endpoint_type`: Always set to `network_port`.<br>  - `endpoint`: The value of the `endpoint` key if set.<br><br>By default the description is templated from the `endpoint` key if set. |

=== "YAML"

    ```yaml
    # Default description or description template to be used on all ports defined under `network_ports`.
    # This can be a template using the format string syntax.
    # The available template fields are:
    #   - `endpoint_type`: Always set to `network_port`.
    #   - `endpoint`: The value of the `endpoint` key if set.
    #
    # By default the description is templated from the `endpoint` key if set.
    default_network_ports_description: <str; default="{endpoint?}">
    ```
