---
search:
  boost: 2
---

# MLAG
## Multi-Chassis Link Aggregation (MLAG) Configuration

=== "Multi-Chassis Link Aggregation (MLAG) Configuration"


    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>mlag_configuration</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;domain_id</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;heartbeat_interval</samp> | Integer |  |  |  | Heartbeat interval in milliseconds |
    | <samp>&nbsp;&nbsp;local_interface</samp> | String |  |  |  | Local Interface Name |
    | <samp>&nbsp;&nbsp;peer_address</samp> | String |  |  |  | IPv4 Address |
    | <samp>&nbsp;&nbsp;peer_address_heartbeat</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;peer_ip</samp> | String |  |  |  | IPv4 Address |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp> | String |  |  |  | VRF Name |
    | <samp>&nbsp;&nbsp;dual_primary_detection_delay</samp> | Integer |  |  | Min: 0<br>Max: 86400 | Delay in seconds |
    | <samp>&nbsp;&nbsp;dual_primary_recovery_delay_mlag</samp> | Integer |  |  | Min: 0<br>Max: 86400 | Delay in seconds |
    | <samp>&nbsp;&nbsp;dual_primary_recovery_delay_non_mlag</samp> | Integer |  |  | Min: 0<br>Max: 86400 | Delay in seconds |
    | <samp>&nbsp;&nbsp;peer_link</samp> | String |  |  |  | Port-Channel interface name |
    | <samp>&nbsp;&nbsp;reload_delay_mlag</samp> | String |  |  |  | Delay in seconds <0-86400> or 'infinity' |
    | <samp>&nbsp;&nbsp;reload_delay_non_mlag</samp> | String |  |  |  | Delay in seconds <0-86400> or 'infinity' |

=== "YAML"

    ```yaml
    mlag_configuration:
      domain_id: <str>
      heartbeat_interval: <int>
      local_interface: <str>
      peer_address: <str>
      peer_address_heartbeat:
        peer_ip: <str>
        vrf: <str>
      dual_primary_detection_delay: <int>
      dual_primary_recovery_delay_mlag: <int>
      dual_primary_recovery_delay_non_mlag: <int>
      peer_link: <str>
      reload_delay_mlag: <str>
      reload_delay_non_mlag: <str>
    ```
