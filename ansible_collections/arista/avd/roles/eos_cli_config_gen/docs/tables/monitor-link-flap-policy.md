<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>monitor_link_flap_policy</samp>](## "monitor_link_flap_policy") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;profiles</samp>](## "monitor_link_flap_policy.profiles") | List, items: Dictionary |  |  |  | A list of damping profiles containing the set of parameters required by the damping logic, which is based on is based on the BGP Route Flap Damping algorithm described in RFC2439. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "monitor_link_flap_policy.profiles.[].name") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;damping_penalty</samp>](## "monitor_link_flap_policy.profiles.[].damping_penalty") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;decay</samp>](## "monitor_link_flap_policy.profiles.[].damping_penalty.decay") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;half_life</samp>](## "monitor_link_flap_policy.profiles.[].damping_penalty.decay.half_life") | Integer |  |  | Min: 1<br>Max: 5000 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;units</samp>](## "monitor_link_flap_policy.profiles.[].damping_penalty.decay.units") | String | Required |  | Valid Values:<br>- <code>minutes</code><br>- <code>seconds</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mac_fault</samp>](## "monitor_link_flap_policy.profiles.[].damping_penalty.mac_fault") | List, items: Dictionary |  |  |  | Penalty for MAC fault change. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;location</samp>](## "monitor_link_flap_policy.profiles.[].damping_penalty.mac_fault.[].location") | String | Required, Unique |  | Valid Values:<br>- <code>local</code><br>- <code>remote</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;penalty</samp>](## "monitor_link_flap_policy.profiles.[].damping_penalty.mac_fault.[].penalty") | Integer | Required |  | Min: 0<br>Max: 5000 | 0 refers to - No penalty, 1-5000 refers to penalty value for fault. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;threshold</samp>](## "monitor_link_flap_policy.profiles.[].damping_penalty.threshold") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maximum</samp>](## "monitor_link_flap_policy.profiles.[].damping_penalty.threshold.maximum") | Integer |  |  | Min: 0<br>Max: 1000000 | Maximum value of penalty for a link. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;reuse</samp>](## "monitor_link_flap_policy.profiles.[].damping_penalty.threshold.reuse") | Integer |  |  | Min: 0<br>Max: 1000000 | Value of penalty below which suppressed link would be reused. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;suppression</samp>](## "monitor_link_flap_policy.profiles.[].damping_penalty.threshold.suppression") | Integer |  |  | Min: 0<br>Max: 1000000 | Value of penalty above which link would be suppressed. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;max_flaps</samp>](## "monitor_link_flap_policy.profiles.[].max_flaps") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;flaps</samp>](## "monitor_link_flap_policy.profiles.[].max_flaps.flaps") | Integer | Required |  | Min: 1<br>Max: 100 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;time</samp>](## "monitor_link_flap_policy.profiles.[].max_flaps.time") | Integer | Required |  | Min: 1<br>Max: 1800 | The time period that flaps are counted (in seconds). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;violations</samp>](## "monitor_link_flap_policy.profiles.[].max_flaps.violations") | Integer |  |  | Min: 1<br>Max: 1000 | Number of violations to be detected. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;intervals</samp>](## "monitor_link_flap_policy.profiles.[].max_flaps.intervals") | Integer |  |  | Min: 1<br>Max: 1000 | Intervals for monitoring violations. |
    | [<samp>&nbsp;&nbsp;default_profiles</samp>](## "monitor_link_flap_policy.default_profiles") | List, items: String |  |  |  | The default-profile set may contain zero, one, or multiple profiles. When the default-profile set contains multiple profiles, error-disable criteria is satisfied when conditions match any profile. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "monitor_link_flap_policy.default_profiles.[]") | String |  |  |  |  |

=== "YAML"

    ```yaml
    monitor_link_flap_policy:

      # A list of damping profiles containing the set of parameters required by the damping logic, which is based on is based on the BGP Route Flap Damping algorithm described in RFC2439.
      profiles:
        - name: <str; required; unique>
          damping_penalty:
            decay:
              half_life: <int; 1-5000>
              units: <str; "minutes" | "seconds"; required>

            # Penalty for MAC fault change.
            mac_fault:
              - location: <str; "local" | "remote"; required; unique>

                # 0 refers to - No penalty, 1-5000 refers to penalty value for fault.
                penalty: <int; 0-5000; required>
            threshold:

              # Maximum value of penalty for a link.
              maximum: <int; 0-1000000>

              # Value of penalty below which suppressed link would be reused.
              reuse: <int; 0-1000000>

              # Value of penalty above which link would be suppressed.
              suppression: <int; 0-1000000>
          max_flaps:
            flaps: <int; 1-100; required>

            # The time period that flaps are counted (in seconds).
            time: <int; 1-1800; required>

            # Number of violations to be detected.
            violations: <int; 1-1000>

            # Intervals for monitoring violations.
            intervals: <int; 1-1000>

      # The default-profile set may contain zero, one, or multiple profiles. When the default-profile set contains multiple profiles, error-disable criteria is satisfied when conditions match any profile.
      default_profiles:
        - <str>
    ```
