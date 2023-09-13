<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>event_handlers</samp>](## "event_handlers") | List, items: Dictionary |  |  |  | Gives the ability to monitor and react to Syslog messages.<br>Event Handlers provide a powerful and flexible tool that can be used to apply self-healing actions,<br>customize the system behavior, and implement workarounds to problems discovered in the field.<br> |
    | [<samp>&nbsp;&nbsp;- name</samp>](## "event_handlers.[].name") | String | Required, Unique |  |  | Event Handler Name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;action_type</samp>](## "event_handlers.[].action_type") | String |  |  | Valid Values:<br>- bash<br>- increment<br>- log |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "event_handlers.[].action") | String |  |  |  | Command to execute<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;delay</samp>](## "event_handlers.[].delay") | Integer |  |  |  | Event-handler delay in seconds<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;trigger</samp>](## "event_handlers.[].trigger") | String |  |  | Valid Values:<br>- on-logging<br>- on-startup-config | Configure event trigger condition.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;regex</samp>](## "event_handlers.[].regex") | String |  |  |  | Regular expression to use for searching log messages. Required for on-logging trigger<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;asynchronous</samp>](## "event_handlers.[].asynchronous") | Boolean |  | `False` |  | Set the action to be non-blocking. |

=== "YAML"

    ```yaml
    event_handlers:
      - name: <str>
        action_type: <str>
        action: <str>
        delay: <int>
        trigger: <str>
        regex: <str>
        asynchronous: <bool>
    ```
