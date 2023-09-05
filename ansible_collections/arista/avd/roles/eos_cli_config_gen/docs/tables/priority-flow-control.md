<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>priority_flow_control</samp>](## "priority_flow_control") | Dictionary |  |  |  | Global Priority Flow Control settings.<br> |
    | [<samp>&nbsp;&nbsp;all_off</samp>](## "priority_flow_control.all_off") | Boolean |  |  |  | Disable PFC on all interfaces.<br> |
    | [<samp>&nbsp;&nbsp;watchdog</samp>](## "priority_flow_control.watchdog") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "priority_flow_control.watchdog.action") | String |  |  | Valid Values:<br>- drop<br>- no-drop | Action on stuck queue.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;timeout</samp>](## "priority_flow_control.watchdog.timeout") | String |  |  | Pattern: ^\d+(\.\d{1,2})?$ | Timeout in seconds after which port should be errdisabled or<br>should start dropping on congested priorities.<br>This should be decimal with up to 2 decimal point.<br>Example: 0.01 or 60<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;polling_interval</samp>](## "priority_flow_control.watchdog.polling_interval") | String |  |  | Pattern: ^\d+(\.\d{1,3})?$ | Time interval in seconds at which the watchdog should poll the queues.<br>This should be decimal with up to 3 decimal point.<br>Example: 0.005 or 60<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;recovery_time</samp>](## "priority_flow_control.watchdog.recovery_time") | String |  |  | Pattern: ^\d+(\.\d{1,2})?$ | Recovery-time in seconds after which stuck queue should<br>recover and start forwarding again.<br>This should be decimal with up to 2 decimal point.<br>Example: 0.01 or 60<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;override_action_drop</samp>](## "priority_flow_control.watchdog.override_action_drop") | Boolean |  |  |  | Override configured action on stuck queue to drop. |

=== "YAML"

    ```yaml
    priority_flow_control:
      all_off: <bool>
      watchdog:
        action: <str>
        timeout: <str>
        polling_interval: <str>
        recovery_time: <str>
        override_action_drop: <bool>
    ```
