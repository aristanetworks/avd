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
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;algorithm</samp>](## "fabric_numbering.id.algorithm") | String |  |  | Valid Values:<br>- pool_manager | If set, IDs will be automatically assigned using the configured algorithm unless statically configured under the node settings.<br><br>- "pool_manager" will activate the pool manager for ID pools.<br><br>  The pools are dynamically built and matched on the following device data:<br>  - `fabric_name`<br>  - `dc_name`<br>  - `pod_name`<br>  - `type`<br><br>  Note: This means changing any of these fields may renumber the devices!<br><br>  Each pool will assign the first available ID starting from 1.<br><br>  Stale entries will be reclaimed from each pool automatically after every run.<br>  A stale entry is an entry that was not accessed during the run. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;pools_file</samp>](## "fabric_numbering.id.pools_file") | String |  |  |  | Path to file to use for storing ID pool data when using "pool_manager" as algorithm.<br>By default the path is "intended/data/<fabric_name>-ids.yml".<br><br>Note: Since the pool manager will remove stale entries after every run, each fabric should be using it's own file. |

=== "YAML"

    ```yaml
    fabric_numbering:
      id:
        algorithm: <str>
        pools_file: <str>
    ```
