<!--
  ~ Copyright (c) 2024 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>influxdb</samp>](## "influxdb") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;vrf</samp>](## "influxdb.vrf") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;destinations</samp>](## "influxdb.destinations") | List, items: Dictionary |  |  |  | Configure telemetry output destinations. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "influxdb.destinations.[].name") | String | Required, Unique |  |  | InfluxDB connection name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;database</samp>](## "influxdb.destinations.[].database") | String |  |  |  | Set name of the database. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;data_retention_policy</samp>](## "influxdb.destinations.[].data_retention_policy") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;url</samp>](## "influxdb.destinations.[].url") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;username</samp>](## "influxdb.destinations.[].username") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;password</samp>](## "influxdb.destinations.[].password") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;password_type</samp>](## "influxdb.destinations.[].password_type") | String |  | `7` | Valid Values:<br>- <code>0</code><br>- <code>7</code><br>- <code>8a</code> |  |
    | [<samp>&nbsp;&nbsp;source_group_standard_disabled</samp>](## "influxdb.source_group_standard_disabled") | Boolean |  |  |  | Disable standard set of telemetry. |
    | [<samp>&nbsp;&nbsp;source_sockets</samp>](## "influxdb.source_sockets") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "influxdb.source_sockets.[].name") | String | Required, Unique |  |  | Label of the socket connection. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;connection_limit</samp>](## "influxdb.source_sockets.[].connection_limit") | Integer |  |  | Min: 0<br>Max: 4294967295 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;url</samp>](## "influxdb.source_sockets.[].url") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;tags</samp>](## "influxdb.tags") | List, items: Dictionary |  |  |  | Extra tags added to the telemetry output. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "influxdb.tags.[].name") | String | Required, Unique |  |  | Key of the global tag pair. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;value</samp>](## "influxdb.tags.[].value") | String |  |  |  | Value of the global tag pair. |

=== "YAML"

    ```yaml
    influxdb:
      vrf: <str>

      # Configure telemetry output destinations.
      destinations:

          # InfluxDB connection name.
        - name: <str; required; unique>

          # Set name of the database.
          database: <str>
          data_retention_policy: <str>
          url: <str>
          username: <str>
          password: <str>
          password_type: <str; "0" | "7" | "8a"; default="7">

      # Disable standard set of telemetry.
      source_group_standard_disabled: <bool>
      source_sockets:

          # Label of the socket connection.
        - name: <str; required; unique>
          connection_limit: <int; 0-4294967295>
          url: <str>

      # Extra tags added to the telemetry output.
      tags:

          # Key of the global tag pair.
        - name: <str; required; unique>

          # Value of the global tag pair.
          value: <str>
    ```
