<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>errdisable</samp>](## "errdisable") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;detect</samp>](## "errdisable.detect") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;causes</samp>](## "errdisable.detect.causes") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "errdisable.detect.causes.[].&lt;str&gt;") | String |  |  | Valid Values:<br>- acl<br>- arp-inspection<br>- dot1x<br>- link-change<br>- tapagg<br>- xcvr-misconfigured<br>- xcvr-overheat<br>- xcvr-power-unsupported |  |
    | [<samp>&nbsp;&nbsp;recovery</samp>](## "errdisable.recovery") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;causes</samp>](## "errdisable.recovery.causes") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "errdisable.recovery.causes.[].&lt;str&gt;") | String |  |  | Valid Values:<br>- arp-inspection<br>- bpduguard<br>- dot1x<br>- hitless-reload-down<br>- lacp-rate-limit<br>- link-flap<br>- no-internal-vlan<br>- portchannelguard<br>- portsec<br>- speed-misconfigured<br>- tap-port-init<br>- tapagg<br>- uplink-failure-detection<br>- xcvr-misconfigured<br>- xcvr-overheat<br>- xcvr-power-unsupported<br>- xcvr-unsupported |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;interval</samp>](## "errdisable.recovery.interval") | Integer |  | `300` | Min: 30<br>Max: 86400 | Interval in seconds |

=== "YAML"

    ```yaml
    errdisable:
      detect:
        causes:
          - <str>
      recovery:
        causes:
          - <str>
        interval: <int>
    ```
