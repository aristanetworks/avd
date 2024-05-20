<!--
  ~ Copyright (c) 2024 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>dot1x</samp>](## "dot1x") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;system_auth_control</samp>](## "dot1x.system_auth_control") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;protocol_lldp_bypass</samp>](## "dot1x.protocol_lldp_bypass") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;protocol_bpdu_bypass</samp>](## "dot1x.protocol_bpdu_bypass") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;dynamic_authorization</samp>](## "dot1x.dynamic_authorization") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;mac_based_authentication</samp>](## "dot1x.mac_based_authentication") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;delay</samp>](## "dot1x.mac_based_authentication.delay") | Integer |  |  | Min: 0<br>Max: 300 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;hold_period</samp>](## "dot1x.mac_based_authentication.hold_period") | Integer |  |  | Min: 1<br>Max: 300 |  |
    | [<samp>&nbsp;&nbsp;radius_av_pair</samp>](## "dot1x.radius_av_pair") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;service_type</samp>](## "dot1x.radius_av_pair.service_type") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;framed_mtu</samp>](## "dot1x.radius_av_pair.framed_mtu") | Integer |  |  | Min: 68<br>Max: 9236 |  |
    | [<samp>&nbsp;&nbsp;aaa</samp>](## "dot1x.aaa") | Dictionary |  |  |  | Configure AAA parameters. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;unresponsive</samp>](## "dot1x.aaa.unresponsive") | Dictionary |  |  |  | Configure AAA timeout options. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;eap_response</samp>](## "dot1x.aaa.unresponsive.eap_response") | String |  |  | Valid Values:<br>- <code>success</code><br>- <code>disabled</code> | EAP response to send. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "dot1x.aaa.unresponsive.action") | Dictionary |  |  |  | Set action for supplicant when AAA times out. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;apply_cached_results</samp>](## "dot1x.aaa.unresponsive.action.apply_cached_results") | Boolean |  |  |  | Use results from a previous AAA response. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cached_results_timeout</samp>](## "dot1x.aaa.unresponsive.action.cached_results_timeout") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;time_duration</samp>](## "dot1x.aaa.unresponsive.action.cached_results_timeout.time_duration") | Integer |  |  | Min: 1 | Enable caching for a specific duration -<br><1-10000>      duration in days<br><1-14400000>   duration in minutes<br><1-240000>     duration in hours<br><1-864000000>  duration in seconds |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;time_duration_unit</samp>](## "dot1x.aaa.unresponsive.action.cached_results_timeout.time_duration_unit") | String | Required |  | Valid Values:<br>- <code>days</code><br>- <code>hours</code><br>- <code>minutes</code><br>- <code>seconds</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;apply_alternate</samp>](## "dot1x.aaa.unresponsive.action.apply_alternate") | Boolean |  |  |  | Apply alternate action if primary action fails.<br>eg. aaa unresponsive action apply cached-results else traffic allow |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;traffic_allow</samp>](## "dot1x.aaa.unresponsive.action.traffic_allow") | Boolean |  |  |  | Set action for supplicant traffic when AAA times out. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;traffic_allow_vlan</samp>](## "dot1x.aaa.unresponsive.action.traffic_allow_vlan") | Integer |  |  | Min: 1<br>Max: 4094 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;phone_action</samp>](## "dot1x.aaa.unresponsive.phone_action") | Dictionary |  |  |  | Set action for supplicant when AAA times out. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;apply_cached_results</samp>](## "dot1x.aaa.unresponsive.phone_action.apply_cached_results") | Boolean |  |  |  | Use results from a previous AAA response. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cached_results_timeout</samp>](## "dot1x.aaa.unresponsive.phone_action.cached_results_timeout") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;time_duration</samp>](## "dot1x.aaa.unresponsive.phone_action.cached_results_timeout.time_duration") | Integer |  |  | Min: 1 | Enable caching for a specific duration -<br><1-10000>      duration in days<br><1-14400000>   duration in minutes<br><1-240000>     duration in hours<br><1-864000000>  duration in seconds |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;time_duration_unit</samp>](## "dot1x.aaa.unresponsive.phone_action.cached_results_timeout.time_duration_unit") | String | Required |  | Valid Values:<br>- <code>days</code><br>- <code>hours</code><br>- <code>minutes</code><br>- <code>seconds</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;apply_alternate</samp>](## "dot1x.aaa.unresponsive.phone_action.apply_alternate") | Boolean |  |  |  | Apply alternate action if primary action fails.<br>eg. aaa unresponsive phone action apply cached-results else traffic allow |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;traffic_allow</samp>](## "dot1x.aaa.unresponsive.phone_action.traffic_allow") | Boolean |  |  |  | Set action for supplicant traffic when AAA times out. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;recovery_action_reauthenticate</samp>](## "dot1x.aaa.unresponsive.recovery_action_reauthenticate") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;accounting_update_interval</samp>](## "dot1x.aaa.accounting_update_interval") | Integer |  |  | Min: 5<br>Max: 65535 | Interval period in seconds. |

=== "YAML"

    ```yaml
    dot1x:
      system_auth_control: <bool>
      protocol_lldp_bypass: <bool>
      protocol_bpdu_bypass: <bool>
      dynamic_authorization: <bool>
      mac_based_authentication:
        delay: <int; 0-300>
        hold_period: <int; 1-300>
      radius_av_pair:
        service_type: <bool>
        framed_mtu: <int; 68-9236>

      # Configure AAA parameters.
      aaa:

        # Configure AAA timeout options.
        unresponsive:

          # EAP response to send.
          eap_response: <str; "success" | "disabled">

          # Set action for supplicant when AAA times out.
          action:

            # Use results from a previous AAA response.
            apply_cached_results: <bool>
            cached_results_timeout:

              # Enable caching for a specific duration -
              # <1-10000>      duration in days
              # <1-14400000>   duration in minutes
              # <1-240000>     duration in hours
              # <1-864000000>  duration in seconds
              time_duration: <int; >=1>
              time_duration_unit: <str; "days" | "hours" | "minutes" | "seconds"; required>

            # Apply alternate action if primary action fails.
            # eg. aaa unresponsive action apply cached-results else traffic allow
            apply_alternate: <bool>

            # Set action for supplicant traffic when AAA times out.
            traffic_allow: <bool>
            traffic_allow_vlan: <int; 1-4094>

          # Set action for supplicant when AAA times out.
          phone_action:

            # Use results from a previous AAA response.
            apply_cached_results: <bool>
            cached_results_timeout:

              # Enable caching for a specific duration -
              # <1-10000>      duration in days
              # <1-14400000>   duration in minutes
              # <1-240000>     duration in hours
              # <1-864000000>  duration in seconds
              time_duration: <int; >=1>
              time_duration_unit: <str; "days" | "hours" | "minutes" | "seconds"; required>

            # Apply alternate action if primary action fails.
            # eg. aaa unresponsive phone action apply cached-results else traffic allow
            apply_alternate: <bool>

            # Set action for supplicant traffic when AAA times out.
            traffic_allow: <bool>
          recovery_action_reauthenticate: <bool>

        # Interval period in seconds.
        accounting_update_interval: <int; 5-65535>
    ```
