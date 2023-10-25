<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>fabric_numbering</samp>](## "fabric_numbering") | Dictionary |  |  |  | Automatic assignment of numbers for settings like Node ID. |
    | [<samp>&nbsp;&nbsp;id</samp>](## "fabric_numbering.id") | Dictionary |  |  |  | Assignement of Node ID. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;algorithm</samp>](## "fabric_numbering.id.algorithm") | String |  | `static` | Valid Values:<br>- static<br>- pool_manager | IDs will be automatically assigned according to the configured algorithm.<br>- `static` will use the statically set IDs under node setting.<br>- `pool_manager` will activate the pool manager for ID pools. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;pools_file</samp>](## "fabric_numbering.id.pools_file") | String |  |  |  | Path to file to use for storing ID pool data when using "pool_manager" as algorithm.<br>By default the path is "intended/data/<fabric_name>-ids.yml".<br><br>Note: Since the pool manager will remove stale entries after every run, each fabric should be using it's own file. |

=== "YAML"

    ```yaml
    fabric_numbering:
      id:
        algorithm: <str>
        pools_file: <str>
    ```
