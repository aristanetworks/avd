<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>eos_designs_documentation</samp>](## "eos_designs_documentation") | Dictionary |  |  |  | Control fabric documentation generation.<br> |
    | [<samp>&nbsp;&nbsp;connected_endpoints</samp>](## "eos_designs_documentation.connected_endpoints") | Boolean |  | `False` |  | Generate fabric-wide documentation for connected endpoints.<br> |

=== "YAML"

    ```yaml
    # Control fabric documentation generation.
    eos_designs_documentation:

      # Generate fabric-wide documentation for connected endpoints.
      connected_endpoints: <bool; default=False>
    ```
