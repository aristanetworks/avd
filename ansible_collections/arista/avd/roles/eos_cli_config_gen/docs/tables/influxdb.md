<!--
  ~ Copyright (c) 2024 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>influxdb</samp>](## "influxdb") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;destinations</samp>](## "influxdb.destinations") | List, items: Dictionary |  |  |  | Configure telemetry output destinations. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "influxdb.destinations.[].name") | String | Required, Unique |  |  | InfluxDB connection name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "influxdb.destinations.[].vrf") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;database</samp>](## "influxdb.destinations.[].database") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;policy</samp>](## "influxdb.destinations.[].policy") | String |  |  |  | Confiure data retention policy. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;url</samp>](## "influxdb.destinations.[].url") | String |  |  |  | Configure URL for the destination. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;username</samp>](## "influxdb.destinations.[].username") | String |  |  |  | Configure login details with destination. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;password</samp>](## "influxdb.destinations.[].password") | String |  |  |  | Assign login password |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;encryption</samp>](## "influxdb.destinations.[].encryption") | String |  |  |  | 0: Indicates that keystring is not encrypted.<br>7: Speciefies that HIDDEN key will follow.<br>8a: Speciefies that AES-256-GCM encrypted key will follow. |
    | [<samp>&nbsp;&nbsp;source_standard_enabled</samp>](## "influxdb.source_standard_enabled") | Boolean |  |  |  | Enable standard set of telemetry. |
    | [<samp>&nbsp;&nbsp;source_sockets</samp>](## "influxdb.source_sockets") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "influxdb.source_sockets.[].name") | String | Required, Unique |  |  | Label of the socket connection. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;connection_limit</samp>](## "influxdb.source_sockets.[].connection_limit") | Integer |  |  | Min: 0<br>Max: 4294967295 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;url</samp>](## "influxdb.source_sockets.[].url") | String |  |  |  | Configure socket URL. |
    | [<samp>&nbsp;&nbsp;tags</samp>](## "influxdb.tags") | List, items: Dictionary |  |  |  | Add extra tag to the telemetry output. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "influxdb.tags.[].name") | String | Required, Unique |  |  | Specify the key of the global tag pair. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;value</samp>](## "influxdb.tags.[].value") | String |  |  |  | Specify the value of the global tag pair. |

=== "YAML"

    ```yaml
    influxdb:

      # Configure telemetry output destinations.
      destinations:

          # InfluxDB connection name.
        - name: <str; required; unique>
          vrf: <str>
          database: <str>

          # Confiure data retention policy.
          policy: <str>

          # Configure URL for the destination.
          url: <str>

          # Configure login details with destination.
          username: <str>

          # Assign login password
          password: <str>

          # 0: Indicates that keystring is not encrypted.
          # 7: Speciefies that HIDDEN key will follow.
          # 8a: Speciefies that AES-256-GCM encrypted key will follow.
          encryption: <str>

      # Enable standard set of telemetry.
      source_standard_enabled: <bool>
      source_sockets:

          # Label of the socket connection.
        - name: <str; required; unique>
          connection_limit: <int; 0-4294967295>

          # Configure socket URL.
          url: <str>

      # Add extra tag to the telemetry output.
      tags:

          # Specify the key of the global tag pair.
        - name: <str; required; unique>

          # Specify the value of the global tag pair.
          value: <str>
    ```
