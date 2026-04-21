<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>errdisable</samp>](## "errdisable") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;detect</samp>](## "errdisable.detect") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;causes</samp>](## "errdisable.detect.causes") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "errdisable.detect.causes.[]") | String |  |  | Valid Values:<br>- <code>acl</code><br>- <code>arp-inspection</code><br>- <code>dot1x</code><br>- <code>dot1x-coa</code><br>- <code>dot1x-phone-classification</code><br>- <code>dot1x-session-replace</code><br>- <code>error-correction-encoding</code><br>- <code>hardware-speed-group</code><br>- <code>interface-speed</code><br>- <code>internal-error</code><br>- <code>link-change</code><br>- <code>port-breakout</code><br>- <code>storm-control</code><br>- <code>switchcard-unreachable</code><br>- <code>tapagg</code><br>- <code>transceiver-adapter</code><br>- <code>xcvr-misconfigured</code><br>- <code>xcvr-overheat</code><br>- <code>xcvr-power-unsupported</code> | Specifies the events that should trigger this action.<br>The list of supported causes depends on both the EOS version and the hardware platform. |
    | [<samp>&nbsp;&nbsp;recovery</samp>](## "errdisable.recovery") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;causes</samp>](## "errdisable.recovery.causes") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "errdisable.recovery.causes.[].name") | String | Required, Unique |  | Valid Values:<br>- <code>acl</code><br>- <code>arp-inspection</code><br>- <code>bpduguard</code><br>- <code>dot1x</code><br>- <code>dot1x-coa</code><br>- <code>dot1x-phone-classification</code><br>- <code>dot1x-session-replace</code><br>- <code>error-correction-encoding</code><br>- <code>hardware-speed-group</code><br>- <code>hitless-reload-down</code><br>- <code>interface-speed</code><br>- <code>internal-error</code><br>- <code>lacp-rate-limit</code><br>- <code>link-flap</code><br>- <code>no-internal-vlan</code><br>- <code>port-breakout</code><br>- <code>portchannelguard</code><br>- <code>portsec</code><br>- <code>speed-misconfigured</code><br>- <code>storm-control</code><br>- <code>stuck-queue</code><br>- <code>switchcard-unreachable</code><br>- <code>tap-port-init</code><br>- <code>tapagg</code><br>- <code>transceiver-adapter</code><br>- <code>uplink-failure-detection</code><br>- <code>xcvr-misconfigured</code><br>- <code>xcvr-overheat</code><br>- <code>xcvr-power-unsupported</code><br>- <code>xcvr-unsupported</code> | Specifies the type of event that can trigger recovery actions.<br>The list of supported causes depends on both the EOS version and the hardware platform. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interval</samp>](## "errdisable.recovery.causes.[].interval") | Integer |  |  | Min: 30<br>Max: 86400 | Interval for each recovery cause in seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;interval</samp>](## "errdisable.recovery.interval") | Integer |  |  | Min: 30<br>Max: 86400 | Interval in seconds. |

=== "YAML"

    ```yaml
    errdisable:
      detect:
        causes:

            # Specifies the events that should trigger this action.
            # The list of supported causes depends on both the EOS version and the hardware platform.
          - <str; "acl" | "arp-inspection" | "dot1x" | "dot1x-coa" | "dot1x-phone-classification" | "dot1x-session-replace" | "error-correction-encoding" | "hardware-speed-group" | "interface-speed" | "internal-error" | "link-change" | "port-breakout" | "storm-control" | "switchcard-unreachable" | "tapagg" | "transceiver-adapter" | "xcvr-misconfigured" | "xcvr-overheat" | "xcvr-power-unsupported">
      recovery:
        causes:

            # Specifies the type of event that can trigger recovery actions.
            # The list of supported causes depends on both the EOS version and the hardware platform.
          - name: <str; "acl" | "arp-inspection" | "bpduguard" | "dot1x" | "dot1x-coa" | "dot1x-phone-classification" | "dot1x-session-replace" | "error-correction-encoding" | "hardware-speed-group" | "hitless-reload-down" | "interface-speed" | "internal-error" | "lacp-rate-limit" | "link-flap" | "no-internal-vlan" | "port-breakout" | "portchannelguard" | "portsec" | "speed-misconfigured" | "storm-control" | "stuck-queue" | "switchcard-unreachable" | "tap-port-init" | "tapagg" | "transceiver-adapter" | "uplink-failure-detection" | "xcvr-misconfigured" | "xcvr-overheat" | "xcvr-power-unsupported" | "xcvr-unsupported"; required; unique>

            # Interval for each recovery cause in seconds.
            interval: <int; 30-86400>

        # Interval in seconds.
        interval: <int; 30-86400>
    ```
