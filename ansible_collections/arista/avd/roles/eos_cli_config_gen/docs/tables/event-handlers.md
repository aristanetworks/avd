<!--
  ~ Copyright (c) 2024 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>event_handlers</samp>](## "event_handlers") | List, items: Dictionary |  |  |  | Gives the ability to monitor and react to Syslog messages.<br>Event Handlers provide a powerful and flexible tool that can be used to apply self-healing actions,<br>customize the system behavior, and implement workarounds to problems discovered in the field.<br> |
    | [<samp>&nbsp;&nbsp;-&nbsp;name</samp>](## "event_handlers.[].name") | String | Required, Unique |  |  | Event Handler Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;action_type</samp>](## "event_handlers.[].action_type") | String |  |  | Valid Values:<br>- <code>bash</code><br>- <code>increment</code><br>- <code>log</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "event_handlers.[].action") | String |  |  |  | Command to execute.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;delay</samp>](## "event_handlers.[].delay") | Integer |  |  |  | Event-handler delay in seconds.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;trigger</samp>](## "event_handlers.[].trigger") | String |  |  | Valid Values:<br>- <code>on-boot</code><br>- <code>on-logging</code><br>- <code>on-startup-config</code><br>- <code>on-maintenance</code> | Configure event trigger condition.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;trigger_on_maintenance</samp>](## "event_handlers.[].trigger_on_maintenance") | Dictionary |  |  |  | Settings required for trigger 'on-maintenance'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;operation</samp>](## "event_handlers.[].trigger_on_maintenance.operation") | String | Required |  | Valid Values:<br>- <code>enter</code><br>- <code>exit</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp_peer</samp>](## "event_handlers.[].trigger_on_maintenance.bgp_peer") | String |  |  |  | Ipv4/Ipv6 address or peer group name.<br>Trigger condition occurs on maintenance operation of specified BGP peer. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "event_handlers.[].trigger_on_maintenance.action") | String | Required |  | Valid Values:<br>- <code>after</code><br>- <code>before</code><br>- <code>all</code><br>- <code>begin</code><br>- <code>end</code> | Action for maintenance operation. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;stage</samp>](## "event_handlers.[].trigger_on_maintenance.stage") | String |  |  | Valid Values:<br>- <code>bgp</code><br>- <code>linkdown</code><br>- <code>mlag</code><br>- <code>ratemon</code> | Action is triggered after/before specified stage. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "event_handlers.[].trigger_on_maintenance.vrf") | String |  |  |  | VRF name. VRF can be defined for "bgp_peer" only. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interface</samp>](## "event_handlers.[].trigger_on_maintenance.interface") | String |  |  |  | Trigger condition occurs on maintenance operation of specified interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unit</samp>](## "event_handlers.[].trigger_on_maintenance.unit") | String |  |  |  | Name of unit. Trigger condition occurs on maintenance operation of specified unit |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;regex</samp>](## "event_handlers.[].regex") | String |  |  |  | Regular expression to use for searching log messages. Required for on-logging trigger.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;asynchronous</samp>](## "event_handlers.[].asynchronous") | Boolean |  | `False` |  | Set the action to be non-blocking.<br> |

=== "YAML"

    ```yaml
    # Gives the ability to monitor and react to Syslog messages.
    # Event Handlers provide a powerful and flexible tool that can be used to apply self-healing actions,
    # customize the system behavior, and implement workarounds to problems discovered in the field.
    event_handlers:

        # Event Handler Name.
      - name: <str; required; unique>
        action_type: <str; "bash" | "increment" | "log">

        # Command to execute.
        action: <str>

        # Event-handler delay in seconds.
        delay: <int>

        # Configure event trigger condition.
        trigger: <str; "on-boot" | "on-logging" | "on-startup-config" | "on-maintenance">

        # Settings required for trigger 'on-maintenance'.
        trigger_on_maintenance:
          operation: <str; "enter" | "exit"; required>

          # Ipv4/Ipv6 address or peer group name.
          # Trigger condition occurs on maintenance operation of specified BGP peer.
          bgp_peer: <str>

          # Action for maintenance operation.
          action: <str; "after" | "before" | "all" | "begin" | "end"; required>

          # Action is triggered after/before specified stage.
          stage: <str; "bgp" | "linkdown" | "mlag" | "ratemon">

          # VRF name. VRF can be defined for "bgp_peer" only.
          vrf: <str>

          # Trigger condition occurs on maintenance operation of specified interface.
          interface: <str>

          # Name of unit. Trigger condition occurs on maintenance operation of specified unit
          unit: <str>

        # Regular expression to use for searching log messages. Required for on-logging trigger.
        regex: <str>

        # Set the action to be non-blocking.
        asynchronous: <bool; default=False>
    ```
