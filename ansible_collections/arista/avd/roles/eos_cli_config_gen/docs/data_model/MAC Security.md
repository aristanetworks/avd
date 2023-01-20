---
search:
  boost: 2
---

# MAC Security

## MAC Security (MACsec)

=== "MAC Security (MACsec)"


    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>mac_security</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;license</samp> | Dictionary | Required |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;license_name</samp> | String | Required |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;license_key</samp> | String | Required |  |  |  |
    | <samp>&nbsp;&nbsp;fips_restrictions</samp> | Boolean | Required |  |  |  |
    | <samp>&nbsp;&nbsp;profiles</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp> | String | Required, Unique |  |  | Profile-Name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cipher</samp> | String |  |  | Valid Values:<br>- aes128-gcm<br>- aes128-gcm-xpn<br>- aes256-gcm<br>- aes256-gcm-xpn |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;connection_keys</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- id</samp> | String | Required, Unique |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;encrypted_key</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;fallback</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mka</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key_server_priority</samp> | Integer |  |  | Min: 0<br>Max: 255 |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;session</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rekey_period</samp> | Integer |  |  | Min: 30<br>Max: 100000 | Rekey period in seconds |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sci</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;l2_protocols</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ethernet_flow_control</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp> | String | Required |  | Valid Values:<br>- encrypt<br>- bypass |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;lldp</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp> | String | Required |  | Valid Values:<br>- bypass<br>- bypass unauthorized |  |

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
