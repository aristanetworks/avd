<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>platform_speed_groups</samp>](## "platform_speed_groups") | List, items: Dictionary |  |  |  | Set Hardware Speed Groups per Platform. |
    | [<samp>&nbsp;&nbsp;-&nbsp;platform</samp>](## "platform_speed_groups.[].platform") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;speeds</samp>](## "platform_speed_groups.[].speeds") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;speed</samp>](## "platform_speed_groups.[].speeds.[].speed") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;speed_groups</samp>](## "platform_speed_groups.[].speeds.[].speed_groups") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "platform_speed_groups.[].speeds.[].speed_groups.[]") | String |  |  |  |  |

=== "YAML"

    ```yaml
    # Set Hardware Speed Groups per Platform.
    platform_speed_groups:
      - platform: <str; required; unique>
        speeds:
          - speed: <str; required; unique>
            speed_groups:
              - <str>
    ```
