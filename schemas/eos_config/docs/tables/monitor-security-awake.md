<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>monitor_security</samp>](## "monitor_security") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;awake</samp>](## "monitor_security.awake") | Dictionary |  |  |  | Configuration of the Arista NDR (Awake) sensor.<br>Renders `monitor security awake`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;disabled</samp>](## "monitor_security.awake.disabled") | Boolean |  |  |  | Disable the NDR sensor.<br>`true` renders `disabled`, `false` renders `no disabled`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;flow_table_size_entries</samp>](## "monitor_security.awake.flow_table_size_entries") | Integer |  |  | Min: 1<br>Max: 614400 | Maximum number of entries in the flow table. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipfix_listener_port</samp>](## "monitor_security.awake.ipfix_listener_port") | Integer |  | `4739` | Min: 1<br>Max: 65535 | UDP port on which the sensor listens for IPFIX records. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;monitor_point_identifier</samp>](## "monitor_security.awake.monitor_point_identifier") | Integer |  |  | Min: 0<br>Max: 2147483647 | Identifier of this monitor point. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ndr_application</samp>](## "monitor_security.awake.ndr_application") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unknown_udp</samp>](## "monitor_security.awake.ndr_application.unknown_udp") | Boolean |  |  |  | Enable handling of unknown UDP applications. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;nucleus</samp>](## "monitor_security.awake.nucleus") | List, items: Dictionary | Required |  | Min Length: 1<br>Max Length: 2 | NDR Nucleus servers (minimum 1, maximum 2). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "monitor_security.awake.nucleus.[].name") | String | Required, Unique |  |  | Hostname of the Nucleus. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;destination</samp>](## "monitor_security.awake.nucleus.[].destination") | String | Required |  |  | IPv4 or IPv6 address or FQDN of the Nucleus. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;port</samp>](## "monitor_security.awake.nucleus.[].port") | Integer |  | `9094` | Min: 1<br>Max: 65535 | TCP port of the Nucleus. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;local_interface</samp>](## "monitor_security.awake.nucleus.[].local_interface") | String |  |  |  | Source interface for the connection to the Nucleus, e.g. `Loopback0`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ssl_profile</samp>](## "monitor_security.awake.nucleus.[].ssl_profile") | String |  |  |  | Name of the SSL profile used for the connection to the Nucleus. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;topic</samp>](## "monitor_security.awake.topic") | String |  | `packet-analysis-sessions` |  | Topic identifier. |

=== "YAML"

    ```yaml
    monitor_security:

      # Configuration of the Arista NDR (Awake) sensor.
      # Renders `monitor security awake`.
      awake:

        # Disable the NDR sensor.
        # `true` renders `disabled`, `false` renders `no disabled`.
        disabled: <bool>

        # Maximum number of entries in the flow table.
        flow_table_size_entries: <int; 1-614400>

        # UDP port on which the sensor listens for IPFIX records.
        ipfix_listener_port: <int; 1-65535; default=4739>

        # Identifier of this monitor point.
        monitor_point_identifier: <int; 0-2147483647>
        ndr_application:

          # Enable handling of unknown UDP applications.
          unknown_udp: <bool>

        # NDR Nucleus servers (minimum 1, maximum 2).
        nucleus: # 1-2 items; required

            # Hostname of the Nucleus.
          - name: <str; required; unique>

            # IPv4 or IPv6 address or FQDN of the Nucleus.
            destination: <str; required>

            # TCP port of the Nucleus.
            port: <int; 1-65535; default=9094>

            # Source interface for the connection to the Nucleus, e.g. `Loopback0`.
            local_interface: <str>

            # Name of the SSL profile used for the connection to the Nucleus.
            ssl_profile: <str>

        # Topic identifier.
        topic: <str; default="packet-analysis-sessions">
    ```
