<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>avd_dir_mode</samp>](## "avd_dir_mode") | String |  | `0o775` |  | Directory permissions mode (octal string) to be applied to all directories created by the role. |

=== "YAML"

    ```yaml
    # Directory permissions mode (octal string) to be applied to all directories created by the role.
    avd_dir_mode: <str; default="0o775">
    ```
