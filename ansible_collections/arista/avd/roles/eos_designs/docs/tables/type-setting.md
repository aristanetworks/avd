=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>type</samp>](## "type") | String |  |  | Valid Values:<br>- <value(s) of node_type_keys.type> | The `type:` variable needs to be defined for each device in the fabric.<br>This is leveraged to load the appropriate template to generate the configuration. |

=== "YAML"

    ```yaml
    type: <str>
    ```
