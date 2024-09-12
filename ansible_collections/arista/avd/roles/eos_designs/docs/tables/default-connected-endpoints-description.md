<!--
  ~ Copyright (c) 2024 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>default_connected_endpoints_description</samp>](## "default_connected_endpoints_description") | String |  | `{endpoint_type!u}_{endpoint}{endpoint_port?<_}` |  | Default description or description template to be used on all ports to connected endpoints.<br>This can be a template using the format string syntax.<br>The available template fields are:<br>  - `endpoint_type`: The `type` from `connected_endpoints_keys` like `server`, `router` etc.<br>  - `endpoint`: The name of the connected endpoint<br>  - `endpoint_port`: The value from `endpoint_ports` for this switch port if set.<br><br>By default the description is templated from the type, name and port of the endpoint if set. |

=== "YAML"

    ```yaml
    # Default description or description template to be used on all ports to connected endpoints.
    # This can be a template using the format string syntax.
    # The available template fields are:
    #   - `endpoint_type`: The `type` from `connected_endpoints_keys` like `server`, `router` etc.
    #   - `endpoint`: The name of the connected endpoint
    #   - `endpoint_port`: The value from `endpoint_ports` for this switch port if set.
    #
    # By default the description is templated from the type, name and port of the endpoint if set.
    default_connected_endpoints_description: <str; default="{endpoint_type!u}_{endpoint}{endpoint_port?<_}">
    ```
