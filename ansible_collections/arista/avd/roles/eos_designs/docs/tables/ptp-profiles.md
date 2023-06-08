=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>ptp_profiles</samp>](## "ptp_profiles") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;- profile</samp>](## "ptp_profiles.[].profile") | String |  |  |  | PTP profile. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;announce</samp>](## "ptp_profiles.[].announce") | Dictionary |  |  |  | PTP announce interval. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interval</samp>](## "ptp_profiles.[].announce.interval") | Integer |  |  | Min: -7<br>Max: 4 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;timeout</samp>](## "ptp_profiles.[].announce.timeout") | Integer |  |  | Min: 2<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;delay_req</samp>](## "ptp_profiles.[].delay_req") | Integer |  |  | Min: -7<br>Max: 8 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;sync_message</samp>](## "ptp_profiles.[].sync_message") | Dictionary |  |  |  | PTP sync message interval. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interval</samp>](## "ptp_profiles.[].sync_message.interval") | Integer |  |  | Min: -7<br>Max: 3 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;transport</samp>](## "ptp_profiles.[].transport") | String |  |  | Valid Values:<br>- ipv4 |  |

=== "YAML"

    ```yaml
    ptp_profiles:
      - profile: <str>
        announce:
          interval: <int>
          timeout: <int>
        delay_req: <int>
        sync_message:
          interval: <int>
        transport: <str>
    ```
