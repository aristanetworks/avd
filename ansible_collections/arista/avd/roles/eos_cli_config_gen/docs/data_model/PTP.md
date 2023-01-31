---
search:
  boost: 2
---

# PTP

## PTP

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>ptp</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;mode</samp> | String |  |  | Valid Values:<br>- boundary<br>- transparent |  |
    | <samp>&nbsp;&nbsp;forward_unicast</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;clock_identity</samp> | String |  |  |  | The clock-id in xx:xx:xx:xx:xx:xx format |
    | <samp>&nbsp;&nbsp;source</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;ip</samp> | String |  |  |  | Source IP |
    | <samp>&nbsp;&nbsp;priority1</samp> | Integer |  |  | Min: 0<br>Max: 255 |  |
    | <samp>&nbsp;&nbsp;priority2</samp> | Integer |  |  | Min: 0<br>Max: 255 |  |
    | <samp>&nbsp;&nbsp;ttl</samp> | Integer |  |  | Min: 1<br>Max: 254 |  |
    | <samp>&nbsp;&nbsp;domain</samp> | Integer |  |  | Min: 0<br>Max: 255 |  |
    | <samp>&nbsp;&nbsp;message_type</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;general</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dscp</samp> | Integer |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;event</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dscp</samp> | Integer |  |  |  |  |
    | <samp>&nbsp;&nbsp;monitor</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp> | Boolean |  | True |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;threshold</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;offset_from_master</samp> | Integer |  |  | Min: 0<br>Max: 1000000000 |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mean_path_delay</samp> | Integer |  |  | Min: 0<br>Max: 1000000000 |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;drop</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;offset_from_master</samp> | Integer |  |  | Min: 0<br>Max: 1000000000 |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mean_path_delay</samp> | Integer |  |  | Min: 0<br>Max: 1000000000 |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;missing_message</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;intervals</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;announce</samp> | Integer |  |  | Min: 2<br>Max: 255 |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;follow_up</samp> | Integer |  |  | Min: 2<br>Max: 255 |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sync</samp> | Integer |  |  | Min: 2<br>Max: 255 |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sequence_ids</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;announce</samp> | Integer |  |  | Min: 2<br>Max: 255 |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;delay_resp</samp> | Integer |  |  | Min: 2<br>Max: 255 |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;follow_up</samp> | Integer |  |  | Min: 2<br>Max: 255 |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sync</samp> | Integer |  |  | Min: 2<br>Max: 255 |  |

=== "YAML"

    ```yaml
    ptp:
      mode: <str>
      forward_unicast: <bool>
      clock_identity: <str>
      source:
        ip: <str>
      priority1: <int>
      priority2: <int>
      ttl: <int>
      domain: <int>
      message_type:
        general:
          dscp: <int>
        event:
          dscp: <int>
      monitor:
        enabled: <bool>
        threshold:
          offset_from_master: <int>
          mean_path_delay: <int>
          drop:
            offset_from_master: <int>
            mean_path_delay: <int>
        missing_message:
          intervals:
            announce: <int>
            follow_up: <int>
            sync: <int>
          sequence_ids:
            enabled: <bool>
            announce: <int>
            delay_resp: <int>
            follow_up: <int>
            sync: <int>
    ```
