<!--
  ~ Copyright (c) 2024 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>ptp_settings</samp>](## "ptp_settings") | Dictionary |  |  |  | The `ptp` setting is deprecated and it will be removed in version 5.0.0 to avoid conflict with `ptp` setting in eos_cli_config_gen. `ptp_settings` takes precedence when both `ptp` and `ptp_settings` are set. |
    | [<samp>&nbsp;&nbsp;enabled</samp>](## "ptp_settings.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;profile</samp>](## "ptp_settings.profile") | String |  | `aes67-r16-2016` | Valid Values:<br>- <code>aes67</code><br>- <code>smpte2059-2</code><br>- <code>aes67-r16-2016</code> |  |
    | [<samp>&nbsp;&nbsp;domain</samp>](## "ptp_settings.domain") | Integer |  |  | Min: 0<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;auto_clock_identity</samp>](## "ptp_settings.auto_clock_identity") | Boolean |  | `True` |  |  |

=== "YAML"

    ```yaml
    # The `ptp` setting is deprecated and it will be removed in version 5.0.0 to avoid conflict with `ptp` setting in eos_cli_config_gen. `ptp_settings` takes precedence when both `ptp` and `ptp_settings` are set.
    ptp_settings:
      enabled: <bool>
      profile: <str; "aes67" | "smpte2059-2" | "aes67-r16-2016"; default="aes67-r16-2016">
      domain: <int; 0-255>
      auto_clock_identity: <bool; default=True>
    ```
