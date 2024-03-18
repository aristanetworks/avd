<!--
  ~ Copyright (c) 2024 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>router_internet_exit</samp>](## "router_internet_exit") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;policies</samp>](## "router_internet_exit.policies") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "router_internet_exit.policies.[].name") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;exit_groups</samp>](## "router_internet_exit.policies.[].exit_groups") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "router_internet_exit.policies.[].exit_groups.[].name") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;after</samp>](## "router_internet_exit.policies.[].exit_groups.[].after") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;before</samp>](## "router_internet_exit.policies.[].exit_groups.[].before") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;exit_groups</samp>](## "router_internet_exit.exit_groups") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "router_internet_exit.exit_groups.[].name") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;fib_default</samp>](## "router_internet_exit.exit_groups.[].fib_default") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;locals</samp>](## "router_internet_exit.exit_groups.[].locals") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;connection</samp>](## "router_internet_exit.exit_groups.[].locals.[].connection") | String |  |  |  |  |

=== "YAML"

    ```yaml
    router_internet_exit:
      policies:
        - name: <str; required; unique>
          exit_groups:
            - name: <str; required; unique>
              after: <str>
              before: <str>
      exit_groups:
        - name: <str; required; unique>
          fib_default: <bool>
          locals:
            - connection: <str>
    ```
