=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>daemons</samp>](## "daemons") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;- name</samp>](## "daemons.[].name") | String | Required, Unique |  |  | Daemon Name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;exec</samp>](## "daemons.[].exec") | String | Required |  |  | command to run as a daemon<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "daemons.[].enabled") | Boolean |  | `True` |  |  |

=== "YAML"

    ```yaml
    daemons:
      - name: <str>
        exec: <str>
        enabled: <bool>
    ```
