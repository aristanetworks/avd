=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>eos_designs_documentation</samp>](## "eos_designs_documentation") | Dictionary |  |  |  | Control fabric documentation generation.<br> |
    | [<samp>&nbsp;&nbsp;connected_endpoints</samp>](## "eos_designs_documentation.connected_endpoints") | Boolean |  | `False` |  | Generate fabric-wide documentation for connected endpoints.<br> |

=== "YAML"

    ```yaml
    eos_designs_documentation:
      connected_endpoints: <bool>
    ```
