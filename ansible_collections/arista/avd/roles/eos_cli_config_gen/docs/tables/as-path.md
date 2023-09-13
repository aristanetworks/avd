<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>as_path</samp>](## "as_path") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;regex_mode</samp>](## "as_path.regex_mode") | String |  |  | Valid Values:<br>- asn<br>- string |  |
    | [<samp>&nbsp;&nbsp;access_lists</samp>](## "as_path.access_lists") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "as_path.access_lists.[].name") | String |  |  |  | Access List Name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;entries</samp>](## "as_path.access_lists.[].entries") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- type</samp>](## "as_path.access_lists.[].entries.[].type") | String |  |  | Valid Values:<br>- permit<br>- deny |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;match</samp>](## "as_path.access_lists.[].entries.[].match") | String |  |  |  | Regex To Match |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;origin</samp>](## "as_path.access_lists.[].entries.[].origin") | String |  | `any` | Valid Values:<br>- any<br>- egp<br>- igp<br>- incomplete |  |

=== "YAML"

    ```yaml
    as_path:
      regex_mode: <str>
      access_lists:
        - name: <str>
          entries:
            - type: <str>
              match: <str>
              origin: <str>
    ```
