<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>radius_server</samp>](## "radius_server") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;attribute_32_include_in_access_req</samp>](## "radius_server.attribute_32_include_in_access_req") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;hostname</samp>](## "radius_server.attribute_32_include_in_access_req.hostname") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;format</samp>](## "radius_server.attribute_32_include_in_access_req.format") | String |  |  |  | Specify the format of the NAS-Identifier. If 'hostname' is set, this is ignored. |
    | [<samp>&nbsp;&nbsp;dynamic_authorization</samp>](## "radius_server.dynamic_authorization") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;port</samp>](## "radius_server.dynamic_authorization.port") | Integer |  |  | Min: 0<br>Max: 65535 | TCP Port |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;tls_ssl_profile</samp>](## "radius_server.dynamic_authorization.tls_ssl_profile") | String |  |  |  | Name of TLS profile |
    | [<samp>&nbsp;&nbsp;hosts</samp>](## "radius_server.hosts") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;host</samp>](## "radius_server.hosts.[].host") | String | Required, Unique |  |  | Host IP address or name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "radius_server.hosts.[].vrf") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;timeout</samp>](## "radius_server.hosts.[].timeout") | Integer |  |  | Min: 1<br>Max: 1000 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;retransmit</samp>](## "radius_server.hosts.[].retransmit") | Integer |  |  | Min: 0<br>Max: 100 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key</samp>](## "radius_server.hosts.[].key") | String |  |  |  | Encrypted key |

=== "YAML"

    ```yaml
    radius_server:
      attribute_32_include_in_access_req:
        hostname: <bool>

        # Specify the format of the NAS-Identifier. If 'hostname' is set, this is ignored.
        format: <str>
      dynamic_authorization:

        # TCP Port
        port: <int; 0-65535>

        # Name of TLS profile
        tls_ssl_profile: <str>
      hosts:

          # Host IP address or name
        - host: <str; required; unique>
          vrf: <str>
          timeout: <int; 1-1000>
          retransmit: <int; 0-100>

          # Encrypted key
          key: <str>
    ```
