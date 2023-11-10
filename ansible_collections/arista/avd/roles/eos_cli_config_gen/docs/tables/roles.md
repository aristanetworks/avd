<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>roles</samp>](## "roles") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;- name</samp>](## "roles.[].name") | String |  |  |  | Role name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;sequence_numbers</samp>](## "roles.[].sequence_numbers") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- sequence</samp>](## "roles.[].sequence_numbers.[].sequence") | Integer |  |  |  | Sequence number |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "roles.[].sequence_numbers.[].action") | String |  |  | Valid Values:<br>- permit<br>- deny |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "roles.[].sequence_numbers.[].mode") | String |  |  |  | "config", "config-all", "exec" or mode key as string<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;command</samp>](## "roles.[].sequence_numbers.[].command") | String |  |  |  | Command as string |

=== "YAML"

    ```yaml
    roles:
      - name: <str>
        sequence_numbers:
          - sequence: <int>
            action: <str>
            mode: <str>
            command: <str>
    ```
