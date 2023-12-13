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
    | [<samp>&nbsp;&nbsp;profile</samp>](## "ptp.profile") | String |  | `aes67-r16-2016` | Valid Values:<br>- <code>aes67</code><br>- <code>smpte2059-2</code><br>- <code>aes67-r16-2016</code> |  |
    | [<samp>&nbsp;&nbsp;domain</samp>](## "ptp.domain") | Integer |  |  | Min: 0<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;auto_clock_identity</samp>](## "ptp.auto_clock_identity") | Boolean |  | `True` |  |  |
    | [<samp>ptp_profiles</samp>](## "ptp_profiles") | List, items: Dictionary |  | See (+) on YAML tab |  |  |
    | [<samp>&nbsp;&nbsp;-&nbsp;profile</samp>](## "ptp_profiles.[].profile") | String |  |  |  | PTP profile. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;announce</samp>](## "ptp_profiles.[].announce") | Dictionary |  |  |  | PTP announce interval. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interval</samp>](## "ptp_profiles.[].announce.interval") | Integer |  |  | Min: -7<br>Max: 4 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;timeout</samp>](## "ptp_profiles.[].announce.timeout") | Integer |  |  | Min: 2<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;delay_req</samp>](## "ptp_profiles.[].delay_req") | Integer |  |  | Min: -7<br>Max: 8 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;sync_message</samp>](## "ptp_profiles.[].sync_message") | Dictionary |  |  |  | PTP sync message interval. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interval</samp>](## "ptp_profiles.[].sync_message.interval") | Integer |  |  | Min: -7<br>Max: 3 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;transport</samp>](## "ptp_profiles.[].transport") | String |  |  | Valid Values:<br>- <code>ipv4</code> |  |

=== "YAML"

    ```yaml
    ptp:
      enabled: <bool>
      profile: <str; "aes67" | "smpte2059-2" | "aes67-r16-2016"; default="aes67-r16-2016">
      domain: <int; 0-255>
      auto_clock_identity: <bool; default=True>
    ptp_profiles: # (1)!

        # PTP profile.
      - profile: <str>

        # PTP announce interval.
        announce:
          interval: <int; -7-4>
          timeout: <int; 2-255>
        delay_req: <int; -7-8>

        # PTP sync message interval.
        sync_message:
          interval: <int; -7-3>
        transport: <str; "ipv4">
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
