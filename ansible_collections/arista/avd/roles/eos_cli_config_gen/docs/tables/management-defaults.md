<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>management_defaults</samp>](## "management_defaults") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;secret</samp>](## "management_defaults.secret") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;hash</samp>](## "management_defaults.secret.hash") | String |  |  | Valid Values:<br>- md5<br>- sha512 |  |

=== "YAML"

    ```yaml
    management_defaults:
      secret:
        hash: <str>
    ```
