<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>mac_security</samp>](## "mac_security") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;license</samp>](## "mac_security.license") | Dictionary | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;license_name</samp>](## "mac_security.license.license_name") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;license_key</samp>](## "mac_security.license.license_key") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;fips_restrictions</samp>](## "mac_security.fips_restrictions") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;profiles</samp>](## "mac_security.profiles") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "mac_security.profiles.[].name") | String | Required, Unique |  |  | Profile-Name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cipher</samp>](## "mac_security.profiles.[].cipher") | String |  |  | Valid Values:<br>- aes128-gcm<br>- aes128-gcm-xpn<br>- aes256-gcm<br>- aes256-gcm-xpn |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;connection_keys</samp>](## "mac_security.profiles.[].connection_keys") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- id</samp>](## "mac_security.profiles.[].connection_keys.[].id") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;encrypted_key</samp>](## "mac_security.profiles.[].connection_keys.[].encrypted_key") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;fallback</samp>](## "mac_security.profiles.[].connection_keys.[].fallback") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mka</samp>](## "mac_security.profiles.[].mka") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key_server_priority</samp>](## "mac_security.profiles.[].mka.key_server_priority") | Integer |  |  | Min: 0<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;session</samp>](## "mac_security.profiles.[].mka.session") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rekey_period</samp>](## "mac_security.profiles.[].mka.session.rekey_period") | Integer |  |  | Min: 30<br>Max: 100000 | Rekey period in seconds |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sci</samp>](## "mac_security.profiles.[].sci") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;l2_protocols</samp>](## "mac_security.profiles.[].l2_protocols") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ethernet_flow_control</samp>](## "mac_security.profiles.[].l2_protocols.ethernet_flow_control") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "mac_security.profiles.[].l2_protocols.ethernet_flow_control.mode") | String | Required |  | Valid Values:<br>- encrypt<br>- bypass |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;lldp</samp>](## "mac_security.profiles.[].l2_protocols.lldp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "mac_security.profiles.[].l2_protocols.lldp.mode") | String | Required |  | Valid Values:<br>- bypass<br>- bypass unauthorized |  |

=== "YAML"

    ```yaml
    mac_security:
      license:
        license_name: <str>
        license_key: <str>
      fips_restrictions: <bool>
      profiles:
        - name: <str>
          cipher: <str>
          connection_keys:
            - id: <str>
              encrypted_key: <str>
              fallback: <bool>
          mka:
            key_server_priority: <int>
            session:
              rekey_period: <int>
          sci: <bool>
          l2_protocols:
            ethernet_flow_control:
              mode: <str>
            lldp:
              mode: <str>
    ```
