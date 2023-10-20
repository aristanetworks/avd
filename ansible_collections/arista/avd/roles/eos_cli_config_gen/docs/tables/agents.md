<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>agents</samp>](## "agents") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;- name</samp>](## "agents.[].name") | String | Required, Unique |  |  | Agent name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;environments</samp>](## "agents.[].environments") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "agents.[].environments.[].name") | String | Required, Unique |  |  | Environment variable name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;value</samp>](## "agents.[].environments.[].value") | String | Required |  |  | Environment variable value. |

=== "YAML"

    ```yaml
    agents:
      - name: <str>
        environments:
          - name: <str>
            value: <str>
    ```
