<!--
  ~ Copyright (c) 2024 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>influxdb</samp>](## "influxdb") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;destinations</samp>](## "influxdb.destinations") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "influxdb.destinations.[].name") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "influxdb.destinations.[].vrf") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;database</samp>](## "influxdb.destinations.[].database") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;policy</samp>](## "influxdb.destinations.[].policy") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;url</samp>](## "influxdb.destinations.[].url") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;username</samp>](## "influxdb.destinations.[].username") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;password</samp>](## "influxdb.destinations.[].password") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;encryption</samp>](## "influxdb.destinations.[].encryption") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;source_standard_enabled</samp>](## "influxdb.source_standard_enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;source_sockets</samp>](## "influxdb.source_sockets") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "influxdb.source_sockets.[].name") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;connection_limit</samp>](## "influxdb.source_sockets.[].connection_limit") | Integer |  |  | Min: 0<br>Max: 4294967295 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;url</samp>](## "influxdb.source_sockets.[].url") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;tags</samp>](## "influxdb.tags") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "influxdb.tags.[].name") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;value</samp>](## "influxdb.tags.[].value") | String |  |  |  |  |

=== "YAML"

    ```yaml
    influxdb:
      destinations:
        - name: <str; required; unique>
          vrf: <str>
          database: <str>
          policy: <str>
          url: <str>
          username: <str>
          password: <str>
          encryption: <int>
      source_standard_enabled: <bool>
      source_sockets:
        - name: <str; required; unique>
          connection_limit: <int; 0-4294967295>
          url: <str>
      tags:
        - name: <str; required; unique>
          value: <str>
    ```
