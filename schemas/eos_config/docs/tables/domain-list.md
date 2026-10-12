<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>domain_list</samp>](## "domain_list") | List, items: String |  |  |  | Domain names to complete unqualified host names. |
    | [<samp>&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "domain_list.[]") | String |  |  |  | Domain name. |

=== "YAML"

    ```yaml
    # Domain names to complete unqualified host names.
    domain_list:

        # Domain name.
      - <str>
    ```
