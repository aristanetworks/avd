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
    | [<samp>&nbsp;&nbsp;connected_endpoints</samp>](## "eos_designs_documentation.connected_endpoints") | Boolean |  | `False` |  | Include connected endpoints in the fabric-wide documentation.<br>This is `false` by default to avoid cluttering documentation for projects with thousands of endpoints. |
    | [<samp>&nbsp;&nbsp;topology_csv</samp>](## "eos_designs_documentation.topology_csv") | Boolean |  | `False` |  | Generate Topology CSV with all interfaces towards other devices. |
    | [<samp>&nbsp;&nbsp;p2p_links_csv</samp>](## "eos_designs_documentation.p2p_links_csv") | Boolean |  | `False` |  | Generate P2P links CSV with all routed point-to-point links between devices. |

=== "YAML"

    ```yaml
    # Control fabric documentation generation.
    eos_designs_documentation:

      # Generate fabric-wide documentation.
      enable: <bool; default=True>

      # Include connected endpoints in the fabric-wide documentation.
      # This is `false` by default to avoid cluttering documentation for projects with thousands of endpoints.
      connected_endpoints: <bool; default=False>

      # Generate Topology CSV with all interfaces towards other devices.
      topology_csv: <bool; default=False>

      # Generate P2P links CSV with all routed point-to-point links between devices.
      p2p_links_csv: <bool; default=False>
    ```
