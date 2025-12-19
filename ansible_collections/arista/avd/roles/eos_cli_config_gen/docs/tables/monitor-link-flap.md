<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>monitor_link_flap</samp>](## "monitor_link_flap") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;profiles</samp>](## "monitor_link_flap.profiles") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "monitor_link_flap.profiles.[].name") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;damping_penalty</samp>](## "monitor_link_flap.profiles.[].damping_penalty") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;decay</samp>](## "monitor_link_flap.profiles.[].damping_penalty.decay") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;half_life</samp>](## "monitor_link_flap.profiles.[].damping_penalty.decay.half_life") | Integer |  |  | Min: 1<br>Max: 5000 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;units</samp>](## "monitor_link_flap.profiles.[].damping_penalty.decay.units") | String | Required |  | Valid Values:<br>- <code>minutes</code><br>- <code>seconds</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mac_fault</samp>](## "monitor_link_flap.profiles.[].damping_penalty.mac_fault") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;location</samp>](## "monitor_link_flap.profiles.[].damping_penalty.mac_fault.[].location") | String | Required, Unique |  | Valid Values:<br>- <code>local</code><br>- <code>remote</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;penalty</samp>](## "monitor_link_flap.profiles.[].damping_penalty.mac_fault.[].penalty") | Integer | Required |  | Min: 0<br>Max: 5000 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;threshold</samp>](## "monitor_link_flap.profiles.[].damping_penalty.threshold") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maximum</samp>](## "monitor_link_flap.profiles.[].damping_penalty.threshold.maximum") | Integer |  |  | Min: 0<br>Max: 1000000 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;reuse</samp>](## "monitor_link_flap.profiles.[].damping_penalty.threshold.reuse") | Integer |  |  | Min: 0<br>Max: 1000000 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;suppression</samp>](## "monitor_link_flap.profiles.[].damping_penalty.threshold.suppression") | Integer |  |  | Min: 0<br>Max: 1000000 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;max_flaps</samp>](## "monitor_link_flap.profiles.[].max_flaps") | Integer |  |  | Min: 1<br>Max: 100 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;time</samp>](## "monitor_link_flap.profiles.[].time") | Integer |  |  | Min: 1<br>Max: 1800 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;violations</samp>](## "monitor_link_flap.profiles.[].violations") | Integer |  |  | Min: 1<br>Max: 1000 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;intervals</samp>](## "monitor_link_flap.profiles.[].intervals") | Integer |  |  | Min: 1<br>Max: 1000 |  |
    | [<samp>&nbsp;&nbsp;default_profiles</samp>](## "monitor_link_flap.default_profiles") | List, items: String |  |  |  | The default-profile set may contain zero, one, or multiple profiles. When the default-profile set contains multiple profiles, error-disable criteria is satisfied when conditions match any profile. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "monitor_link_flap.default_profiles.[]") | String |  |  |  |  |

=== "YAML"

    ```yaml
    monitor_link_flap:
      profiles:
        - name: <str; required; unique>
          damping_penalty:
            decay:
              half_life: <int; 1-5000>
              units: <str; "minutes" | "seconds"; required>
            mac_fault:
              - location: <str; "local" | "remote"; required; unique>
                penalty: <int; 0-5000; required>
            threshold:
              maximum: <int; 0-1000000>
              reuse: <int; 0-1000000>
              suppression: <int; 0-1000000>
          max_flaps: <int; 1-100>
          time: <int; 1-1800>
          violations: <int; 1-1000>
          intervals: <int; 1-1000>

      # The default-profile set may contain zero, one, or multiple profiles. When the default-profile set contains multiple profiles, error-disable criteria is satisfied when conditions match any profile.
      default_profiles:
        - <str>
    ```
