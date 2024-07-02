<!--
  ~ Copyright (c) 2024 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>ptp</samp>](## "ptp") <span style="color:red">deprecated</span> | Dictionary |  |  |  | Common PTP settings.<br>`ptp_settings` replaces the old `ptp` key. `ptp_settings` takes precedence.<span style="color:red">This key is deprecated. Support will be removed in AVD version v5.0.0. Use <samp>ptp_settings</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;enabled</samp>](## "ptp.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;profile</samp>](## "ptp.profile") | String |  | `aes67-r16-2016` | Valid Values:<br>- <code>aes67</code><br>- <code>smpte2059-2</code><br>- <code>aes67-r16-2016</code> |  |
    | [<samp>&nbsp;&nbsp;domain</samp>](## "ptp.domain") | Integer |  |  | Min: 0<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;auto_clock_identity</samp>](## "ptp.auto_clock_identity") | Boolean |  | `True` |  |  |

=== "YAML"

    ```yaml
    # Common PTP settings.
    # `ptp_settings` replaces the old `ptp` key. `ptp_settings` takes precedence.
    # This key is deprecated.
    # Support will be removed in AVD version v5.0.0.
    # Use <samp>ptp_settings</samp> instead.
    ptp:
      enabled: <bool>
      profile: <str; "aes67" | "smpte2059-2" | "aes67-r16-2016"; default="aes67-r16-2016">
      domain: <int; 0-255>
      auto_clock_identity: <bool; default=True>
    ```
