<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>monitor_link_flap</samp>](## "monitor_link_flap") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;profile</samp>](## "monitor_link_flap.profile") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "monitor_link_flap.profile.[].name") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;damping_penalty</samp>](## "monitor_link_flap.profile.[].damping_penalty") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;decay_half_life</samp>](## "monitor_link_flap.profile.[].damping_penalty.decay_half_life") | Integer |  |  | Min: 1<br>Max: 5000 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mac_fault</samp>](## "monitor_link_flap.profile.[].damping_penalty.mac_fault") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;local</samp>](## "monitor_link_flap.profile.[].damping_penalty.mac_fault.local") | Integer |  |  | Min: 0<br>Max: 5000 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remote</samp>](## "monitor_link_flap.profile.[].damping_penalty.mac_fault.remote") | Integer |  |  | Min: 0<br>Max: 5000 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;threshold</samp>](## "monitor_link_flap.profile.[].damping_penalty.threshold") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maximum</samp>](## "monitor_link_flap.profile.[].damping_penalty.threshold.maximum") | Integer |  |  | Min: 0<br>Max: 1000000 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;reuse</samp>](## "monitor_link_flap.profile.[].damping_penalty.threshold.reuse") | Integer |  |  | Min: 0<br>Max: 1000000 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;suppression</samp>](## "monitor_link_flap.profile.[].damping_penalty.threshold.suppression") | Integer |  |  | Min: 0<br>Max: 1000000 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;max_flaps</samp>](## "monitor_link_flap.profile.[].max_flaps") | Integer |  |  | Min: 1<br>Max: 100 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;time</samp>](## "monitor_link_flap.profile.[].time") | Integer |  |  | Min: 1<br>Max: 1800 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;violations</samp>](## "monitor_link_flap.profile.[].violations") | Integer |  |  | Min: 1<br>Max: 1000 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;intervals</samp>](## "monitor_link_flap.profile.[].intervals") | Integer |  |  | Min: 1<br>Max: 1000 |  |
    | [<samp>&nbsp;&nbsp;default_profiles</samp>](## "monitor_link_flap.default_profiles") | List, items: String |  |  |  | The default-profile set may contain zero, one, or multiple profiles. When the default-profile set contains multiple profiles, error-disable criteria is satisfied when conditions match any profile. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "monitor_link_flap.default_profiles.[]") | String |  |  |  |  |

=== "YAML"

    ```yaml
    monitor_link_flap:
      profile:
        - name: <str; required; unique>
          damping_penalty:
            decay_half_life: <int; 1-5000>
            mac_fault:
              local: <int; 0-5000>
              remote: <int; 0-5000>
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
