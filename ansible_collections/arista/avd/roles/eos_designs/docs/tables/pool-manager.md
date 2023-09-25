<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>pool_manager</samp>](## "pool_manager") | Dictionary |  |  |  | Pool Manager used for automatic assignment of pool values. |
    | [<samp>&nbsp;&nbsp;activate</samp>](## "pool_manager.activate") | Boolean |  | `False` |  | Activate the pool manager for all supported pools.<br>Can be overridden per pool. |
    | [<samp>&nbsp;&nbsp;id</samp>](## "pool_manager.id") | Dictionary |  |  |  | Automatic assignement of Node ID.<br><br>The pools are dynamically built and matched on the following device data:<br>- `fabric_name`<br>- `dc_name`<br>- `pod_name`<br>- `type`<br>Note: This means changing any of these fields may renumber the devices!<br><br>Each pool will assign first available ID starting from 1.<br><br>Stale entries will be removed from each pool automatically on every run.<br>A stale entry is any entry not accessed during the run. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;activate</samp>](## "pool_manager.id.activate") | Boolean |  |  |  | Activate the pool manager for ID pools.<br>Overrides the activation on pool manager. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;path</samp>](## "pool_manager.id.path") | String |  |  |  | Path to file to use for storing ID pool data.<br>By default the path is "intended/data/<fabric_name>-ids.yml".<br><br>Note: Since stale entries are removed per run, each fabric should be using it's own file. |

=== "YAML"

    ```yaml
    pool_manager:
      activate: <bool>
      id:
        activate: <bool>
        path: <str>
    ```
