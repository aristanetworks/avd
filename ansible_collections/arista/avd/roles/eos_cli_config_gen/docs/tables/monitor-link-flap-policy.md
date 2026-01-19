<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>monitor_link_flap_policy</samp>](## "monitor_link_flap_policy") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;damping_profiles</samp>](## "monitor_link_flap_policy.damping_profiles") | List, items: Dictionary |  |  |  | A list of damping profiles containing the set of parameters required by the damping logic, which is based on the BGP Route Flap Damping algorithm described in RFC2439. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "monitor_link_flap_policy.damping_profiles.[].name") | String | Required, Unique |  |  | The profile name should be unique over all defined profiles (damping_profiles and max_flap_profiles). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;penalty_decay</samp>](## "monitor_link_flap_policy.damping_profiles.[].penalty_decay") | Dictionary |  |  |  | Decay rate for penalty. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;half_life</samp>](## "monitor_link_flap_policy.damping_profiles.[].penalty_decay.half_life") | Integer | Required |  | Min: 1<br>Max: 5000 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;units</samp>](## "monitor_link_flap_policy.damping_profiles.[].penalty_decay.units") | String | Required |  | Valid Values:<br>- <code>minutes</code><br>- <code>seconds</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mac_fault_local_penalty</samp>](## "monitor_link_flap_policy.damping_profiles.[].mac_fault_local_penalty") | Integer |  |  | Min: 0<br>Max: 5000 | 0 refers to - No penalty, 1-5000 refers to penalty value for fault. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mac_fault_remote_penalty</samp>](## "monitor_link_flap_policy.damping_profiles.[].mac_fault_remote_penalty") | Integer |  |  | Min: 0<br>Max: 5000 | 0 refers to - No penalty, 1-5000 refers to penalty value for fault. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;penalty_threshold</samp>](## "monitor_link_flap_policy.damping_profiles.[].penalty_threshold") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maximum</samp>](## "monitor_link_flap_policy.damping_profiles.[].penalty_threshold.maximum") | Integer |  |  | Min: 0<br>Max: 1000000 | Maximum value of penalty for a link. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;reuse</samp>](## "monitor_link_flap_policy.damping_profiles.[].penalty_threshold.reuse") | Integer |  |  | Min: 0<br>Max: 1000000 | Value of penalty below which suppressed link would be reused. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;suppression</samp>](## "monitor_link_flap_policy.damping_profiles.[].penalty_threshold.suppression") | Integer |  |  | Min: 0<br>Max: 1000000 | Value of penalty above which link would be suppressed. |
    | [<samp>&nbsp;&nbsp;max_flap_profiles</samp>](## "monitor_link_flap_policy.max_flap_profiles") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "monitor_link_flap_policy.max_flap_profiles.[].name") | String | Required, Unique |  |  | The profile name should be unique over all defined profiles (damping_profiles and max_flap_profiles). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;max_flaps</samp>](## "monitor_link_flap_policy.max_flap_profiles.[].max_flaps") | Integer | Required |  | Min: 1<br>Max: 100 | Maximum number of flaps. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;time</samp>](## "monitor_link_flap_policy.max_flap_profiles.[].time") | Integer | Required |  | Min: 1<br>Max: 1800 | The time period that flaps are counted (in seconds). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;violations</samp>](## "monitor_link_flap_policy.max_flap_profiles.[].violations") | Integer |  |  | Min: 1<br>Max: 1000 | Number of violations to be detected. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;intervals</samp>](## "monitor_link_flap_policy.max_flap_profiles.[].intervals") | Integer |  |  | Min: 1<br>Max: 1000 | Intervals for monitoring violations. This key is required to configure violations. |
    | [<samp>&nbsp;&nbsp;default_profiles</samp>](## "monitor_link_flap_policy.default_profiles") | List, items: String |  |  | Min Length: 1 | The default-profile set may contain zero, one, or multiple profiles. When the default-profile set contains multiple profiles, error-disable criteria is satisfied when conditions match any profile. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "monitor_link_flap_policy.default_profiles.[]") | String |  |  |  |  |

=== "YAML"

    ```yaml
    monitor_link_flap_policy:

      # A list of damping profiles containing the set of parameters required by the damping logic, which is based on the BGP Route Flap Damping algorithm described in RFC2439.
      damping_profiles:

          # The profile name should be unique over all defined profiles (damping_profiles and max_flap_profiles).
        - name: <str; required; unique>

          # Decay rate for penalty.
          penalty_decay:
            half_life: <int; 1-5000; required>
            units: <str; "minutes" | "seconds"; required>

          # 0 refers to - No penalty, 1-5000 refers to penalty value for fault.
          mac_fault_local_penalty: <int; 0-5000>

          # 0 refers to - No penalty, 1-5000 refers to penalty value for fault.
          mac_fault_remote_penalty: <int; 0-5000>
          penalty_threshold:

            # Maximum value of penalty for a link.
            maximum: <int; 0-1000000>

            # Value of penalty below which suppressed link would be reused.
            reuse: <int; 0-1000000>

            # Value of penalty above which link would be suppressed.
            suppression: <int; 0-1000000>
      max_flap_profiles:

          # The profile name should be unique over all defined profiles (damping_profiles and max_flap_profiles).
        - name: <str; required; unique>

          # Maximum number of flaps.
          max_flaps: <int; 1-100; required>

          # The time period that flaps are counted (in seconds).
          time: <int; 1-1800; required>

          # Number of violations to be detected.
          violations: <int; 1-1000>

          # Intervals for monitoring violations. This key is required to configure violations.
          intervals: <int; 1-1000>

      # The default-profile set may contain zero, one, or multiple profiles. When the default-profile set contains multiple profiles, error-disable criteria is satisfied when conditions match any profile.
      default_profiles: # >=1 items
        - <str>
    ```
