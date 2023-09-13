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

=== "YAML"

    ```yaml
    ptp:
      enabled: <bool>
      profile: <str>
      domain: <int>
      auto_clock_identity: <bool>
    ```
