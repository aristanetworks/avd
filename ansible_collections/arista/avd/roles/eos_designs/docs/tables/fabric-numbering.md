<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>fabric_numbering</samp>](## "fabric_numbering") | Dictionary |  |  |  | PREVIEW: This feature is in marked as "preview", which means it is subject to change at any time.<br><br>Assignment policies for numbers like Node ID. |
    | [<samp>&nbsp;&nbsp;node_id</samp>](## "fabric_numbering.node_id") | Dictionary |  |  |  | Assignment policy for Node ID.<br>Node ID is mainly used for IP address assignment but can also affect BGP AS and/or<br>interface assignments depending on other settings. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;algorithm</samp>](## "fabric_numbering.node_id.algorithm") | String |  | `static` | Valid Values:<br>- <code>static</code><br>- <code>pool_manager</code> | IDs will be automatically assigned according to the configured algorithm.<br>- `static` will use the statically set IDs under node setting.<br>- `pool_manager` will activate the pool manager for ID pools.<br>  Any statically set ID under node settings will be reserved in the pool if possible.<br>  Otherwise an error will be raised. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;pools_file</samp>](## "fabric_numbering.node_id.pools_file") | String |  |  |  | Path to file to use for storing ID pool data when using "pool_manager" as algorithm.<br>This can be an absolute path or a path relative to current working directory.<br><br>By default the path is: `<root_dir>/intended/data/<fabric_name>-ids.yml`.<br><br>Note: Since the pool manager will remove stale entries after every run, each fabric should be using its own file. |
    | [<samp>fabric_numbering_node_id_pool</samp>](## "fabric_numbering_node_id_pool") | String |  | `fabric_name={fabric_name}{dc_name?</dc_name=}{pod_name?</pod_name=}{type?</type=}` |  | Name of Node ID pool or template used to render the name of each Node ID pool.<br>For each device the Node ID is assigned from a pool shared by all devices rendering the same pool name.<br>This can be modified to include fewer or more fields to keep separate pools or to use the same pool across areas.<br>This can be a template using the AVD string formatter syntax: https://avd.arista.com/devel/ansible_collections/arista/avd/roles/eos_designs/docs/how-to/custom-descriptions-names.html#avd-string-formatter-syntax.<br>The available template fields are:<br>  - `fabric_name`: The `fabric_name` assigned to the device.<br>  - `dc_name`: The `dc_name` assigned to the device.<br>  - `pod_name`: The `pod_name` assigned to the device.<br>  - `type`: The `type` assigned to the device.<br>  - `rack`: The `rack` assigned to the device.<br><br>By default the Node ID pool key is templated from `fabric_name`, `dc_name`, `pod_name` and `type`. |

=== "YAML"

    ```yaml
    # PREVIEW: This feature is in marked as "preview", which means it is subject to change at any time.
    #
    # Assignment policies for numbers like Node ID.
    fabric_numbering:

      # Assignment policy for Node ID.
      # Node ID is mainly used for IP address assignment but can also affect BGP AS and/or
      # interface assignments depending on other settings.
      node_id:

        # IDs will be automatically assigned according to the configured algorithm.
        # - `static` will use the statically set IDs under node setting.
        # - `pool_manager` will activate the pool manager for ID pools.
        #   Any statically set ID under node settings will be reserved in the pool if possible.
        #   Otherwise an error will be raised.
        algorithm: <str; "static" | "pool_manager"; default="static">

        # Path to file to use for storing ID pool data when using "pool_manager" as algorithm.
        # This can be an absolute path or a path relative to current working directory.
        #
        # By default the path is: `<root_dir>/intended/data/<fabric_name>-ids.yml`.
        #
        # Note: Since the pool manager will remove stale entries after every run, each fabric should be using its own file.
        pools_file: <str>

    # Name of Node ID pool or template used to render the name of each Node ID pool.
    # For each device the Node ID is assigned from a pool shared by all devices rendering the same pool name.
    # This can be modified to include fewer or more fields to keep separate pools or to use the same pool across areas.
    # This can be a template using the AVD string formatter syntax: https://avd.arista.com/devel/ansible_collections/arista/avd/roles/eos_designs/docs/how-to/custom-descriptions-names.html#avd-string-formatter-syntax.
    # The available template fields are:
    #   - `fabric_name`: The `fabric_name` assigned to the device.
    #   - `dc_name`: The `dc_name` assigned to the device.
    #   - `pod_name`: The `pod_name` assigned to the device.
    #   - `type`: The `type` assigned to the device.
    #   - `rack`: The `rack` assigned to the device.
    #
    # By default the Node ID pool key is templated from `fabric_name`, `dc_name`, `pod_name` and `type`.
    fabric_numbering_node_id_pool: <str; default="fabric_name={fabric_name}{dc_name?</dc_name=}{pod_name?</pod_name=}{type?</type=}">
    ```
