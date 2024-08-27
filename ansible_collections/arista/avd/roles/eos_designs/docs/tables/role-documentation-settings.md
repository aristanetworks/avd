<!--
  ~ Copyright (c) 2024 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>avd_connected_endpoints_documentation</samp>](## "avd_connected_endpoints_documentation") | Boolean |  | `False` |  | Generate fabric-wide documentation for connected endpoints. |
    | [<samp>avd_fabric_documentation</samp>](## "avd_fabric_documentation") | Boolean |  | `True` |  | Generate fabric-wide documentation. |
    | [<samp>eos_designs_documentation</samp>](## "eos_designs_documentation") | Dictionary |  |  |  | Control fabric documentation generation.<br> |
    | [<samp>&nbsp;&nbsp;connected_endpoints</samp>](## "eos_designs_documentation.connected_endpoints") <span style="color:red">deprecated</span> | Boolean |  | `False` |  | Generate fabric-wide documentation for connected endpoints.<br><span style="color:red">This key is deprecated. Support will be removed in AVD version 6.0.0. Use <samp>avd_documentation_connected_endpoints</samp> instead.</span> |

=== "YAML"

    ```yaml
    # Generate fabric-wide documentation for connected endpoints.
    avd_connected_endpoints_documentation: <bool; default=False>

    # Generate fabric-wide documentation.
    avd_fabric_documentation: <bool; default=True>

    # Control fabric documentation generation.
    eos_designs_documentation:

      # Generate fabric-wide documentation for connected endpoints.
      # This key is deprecated.
      # Support will be removed in AVD version 6.0.0.
      # Use <samp>avd_documentation_connected_endpoints</samp> instead.
      connected_endpoints: <bool; default=False>
    ```
