<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>ptp</samp>](## "ptp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;enabled</samp>](## "ptp.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;profile</samp>](## "ptp.profile") | String |  | `aes67-r16-2016` | Valid Values:<br>- aes67<br>- smpte2059-2<br>- aes67-r16-2016 |  |
    | [<samp>&nbsp;&nbsp;domain</samp>](## "ptp.domain") | Integer |  |  | Min: 0<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;auto_clock_identity</samp>](## "ptp.auto_clock_identity") | Boolean |  | `True` |  |  |
    | [<samp>ptp_profiles</samp>](## "ptp_profiles") | List, items: Dictionary |  | See (+) on YAML tab |  |  |
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
    ptp:
      enabled: <bool>
      profile: <str>
      domain: <int>
      auto_clock_identity: <bool>
    ptp_profiles: # (1)!
      - profile: <str>
        announce:
          interval: <int>
          timeout: <int>
        delay_req: <int>
        sync_message:
          interval: <int>
        transport: <str>
    ```

    1. Default Value

        ```yaml
        ptp_profiles:
        - announce:
            interval: 0
            timeout: 3
          delay_req: -3
          profile: aes67-r16-2016
          sync_message:
            interval: -3
          transport: ipv4
        - announce:
            interval: -2
            timeout: 3
          delay_req: -4
          profile: smpte2059-2
          sync_message:
            interval: -4
          transport: ipv4
        - announce:
            interval: 2
            timeout: 3
          delay_req: 0
          profile: aes67
          sync_message:
            interval: 0
          transport: ipv4

        ```
