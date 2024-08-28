<!--
  ~ Copyright (c) 2024 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>eos_designs_documentation</samp>](## "eos_designs_documentation") | Dictionary |  |  |  | Control fabric documentation generation.<br> |
    | [<samp>&nbsp;&nbsp;enable</samp>](## "eos_designs_documentation.enable") | Boolean |  | `True` |  | Generate fabric-wide documentation. |
    | [<samp>&nbsp;&nbsp;connected_endpoints</samp>](## "eos_designs_documentation.connected_endpoints") | Boolean |  | `False` |  | Include connected endpoints in the fabric-wide documentation.<br> |

=== "YAML"

    ```yaml
    # Control fabric documentation generation.
    eos_designs_documentation:

      # Generate fabric-wide documentation.
      enable: <bool; default=True>

      # Include connected endpoints in the fabric-wide documentation.
      connected_endpoints: <bool; default=False>
    ```
