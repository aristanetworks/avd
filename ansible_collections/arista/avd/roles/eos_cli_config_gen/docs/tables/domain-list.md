<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>domain_list</samp>](## "domain_list") | List, items: String |  |  |  | Search list of DNS domains |
    | [<samp>&nbsp;&nbsp;- &lt;str&gt;</samp>](## "domain_list.[].&lt;str&gt;") | String |  |  |  | Domain name |

=== "YAML"

    ```yaml
    domain_list:
      - <str>
    ```
