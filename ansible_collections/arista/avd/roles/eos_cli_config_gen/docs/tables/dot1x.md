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
    | [<samp>&nbsp;&nbsp;aaa</samp>](## "dot1x.aaa") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;unresponsive</samp>](## "dot1x.aaa.unresponsive") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;eap_response</samp>](## "dot1x.aaa.unresponsive.eap_response") | String |  |  | Valid Values:<br>- <code>success</code><br>- <code>disabled</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "dot1x.aaa.unresponsive.action") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;apply_cached_results</samp>](## "dot1x.aaa.unresponsive.action.apply_cached_results") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cached_results_timeout</samp>](## "dot1x.aaa.unresponsive.action.cached_results_timeout") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;time_duration</samp>](## "dot1x.aaa.unresponsive.action.cached_results_timeout.time_duration") | Integer |  |  | Min: 1 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;time_duration_unit</samp>](## "dot1x.aaa.unresponsive.action.cached_results_timeout.time_duration_unit") | String | Required |  | Valid Values:<br>- <code>days</code><br>- <code>hours</code><br>- <code>minutes</code><br>- <code>seconds</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;traffic_allow</samp>](## "dot1x.aaa.unresponsive.action.traffic_allow") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;traffic_allow_vlan</samp>](## "dot1x.aaa.unresponsive.action.traffic_allow_vlan") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;phone_action</samp>](## "dot1x.aaa.unresponsive.phone_action") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;apply_cached_results</samp>](## "dot1x.aaa.unresponsive.phone_action.apply_cached_results") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cached_results_timeout</samp>](## "dot1x.aaa.unresponsive.phone_action.cached_results_timeout") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;time_duration</samp>](## "dot1x.aaa.unresponsive.phone_action.cached_results_timeout.time_duration") | Integer |  |  | Min: 1 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;time_duration_unit</samp>](## "dot1x.aaa.unresponsive.phone_action.cached_results_timeout.time_duration_unit") | String | Required |  | Valid Values:<br>- <code>days</code><br>- <code>hours</code><br>- <code>minutes</code><br>- <code>seconds</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;traffic_allow</samp>](## "dot1x.aaa.unresponsive.phone_action.traffic_allow") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;recovery_action_reauthenticate</samp>](## "dot1x.aaa.unresponsive.recovery_action_reauthenticate") | Boolean |  |  |  |  |

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
      aaa:
        unresponsive:
          eap_response: <str; "success" | "disabled">
          action:
            apply_cached_results: <bool>
            cached_results_timeout:
              time_duration: <int; >=1>
              time_duration_unit: <str; "days" | "hours" | "minutes" | "seconds"; required>
            traffic_allow: <bool>
            traffic_allow_vlan: <int>
          phone_action:
            apply_cached_results: <bool>
            cached_results_timeout:
              time_duration: <int; >=1>
              time_duration_unit: <str; "days" | "hours" | "minutes" | "seconds"; required>
            traffic_allow: <bool>
          recovery_action_reauthenticate: <bool>
    ```
