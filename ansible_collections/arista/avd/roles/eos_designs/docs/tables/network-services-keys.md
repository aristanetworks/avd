=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>network_services_keys</samp>](## "network_services_keys") | List, items: Dictionary |  |  |  | Define network services keys, to define grouping of network services.<br>This provides the ability to define various keys of your choice to better organize/group your data.<br>This should be defined in top level group_var for the fabric.<br> |
    | [<samp>&nbsp;&nbsp;- name</samp>](## "network_services_keys.[].name") | String | Required, Unique |  |  |  |

=== "YAML"

    ```yaml
    network_services_keys:
      - name: <str>
    ```
