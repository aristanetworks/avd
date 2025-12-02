<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>errdisable</samp>](## "errdisable") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;detect</samp>](## "errdisable.detect") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;causes</samp>](## "errdisable.detect.causes") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "errdisable.detect.causes.[]") | String |  |  | Valid Values:<br>- <code>acl</code><br>- <code>arp-inspection</code><br>- <code>dot1x-coa</code><br>- <code>dot1x-phone-classification</code><br>- <code>dot1x-session-replace</code><br>- <code>link-change</code><br>- <code>stp-no-portid </code><br>- <code>tapagg</code> | Specifies the events that should trigger this action.<br>Supported values align with EOS 4.35.0F |
    | [<samp>&nbsp;&nbsp;recovery</samp>](## "errdisable.recovery") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;causes</samp>](## "errdisable.recovery.causes") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "errdisable.recovery.causes.[].name") | String | Required, Unique |  | Valid Values:<br>- <code>acl</code><br>- <code>arp-inspection</code><br>- <code>bpduguard</code><br>- <code>dot1x-coa</code><br>- <code>dot1x-phone-classification</code><br>- <code>dot1x-session-replace</code><br>- <code>hitless-reload-down</code><br>- <code>link-flap</code><br>- <code>no-internal-vlan</code><br>- <code>stp-no-portid</code><br>- <code>tapagg</code><br>- <code>uplink-failure-detection</code> | Specifies the type of event that can trigger recovery actions.<br>Supported values align with EOS 4.35.0F |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interval</samp>](## "errdisable.recovery.causes.[].interval") | Integer |  |  | Min: 30<br>Max: 86400 | Interval for each recovery cause in seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;interval</samp>](## "errdisable.recovery.interval") | Integer |  |  | Min: 30<br>Max: 86400 | Interval in seconds. |

=== "YAML"

    ```yaml
    errdisable:
      detect:
        causes:

            # Specifies the events that should trigger this action.
            # Supported values align with EOS 4.35.0F
          - <str; "acl" | "arp-inspection" | "dot1x-coa" | "dot1x-phone-classification" | "dot1x-session-replace" | "link-change" | "stp-no-portid " | "tapagg">
      recovery:
        causes:

            # Specifies the type of event that can trigger recovery actions.
            # Supported values align with EOS 4.35.0F
          - name: <str; "acl" | "arp-inspection" | "bpduguard" | "dot1x-coa" | "dot1x-phone-classification" | "dot1x-session-replace" | "hitless-reload-down" | "link-flap" | "no-internal-vlan" | "stp-no-portid" | "tapagg" | "uplink-failure-detection"; required; unique>

            # Interval for each recovery cause in seconds.
            interval: <int; 30-86400>

        # Interval in seconds.
        interval: <int; 30-86400>
    ```
