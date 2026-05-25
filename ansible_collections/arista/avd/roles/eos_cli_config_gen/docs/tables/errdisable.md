<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>errdisable</samp>](## "errdisable") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;detect</samp>](## "errdisable.detect") <span style="color:red">deprecated</span> | Dictionary |  |  |  | <span style="color:red">This key is deprecated. Support will be removed in AVD version 7.0.0. Use <samp>detect_cause</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;causes</samp>](## "errdisable.detect.causes") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "errdisable.detect.causes.[]") | String |  |  | Valid Values:<br>- <code>acl</code><br>- <code>arp-inspection</code><br>- <code>dot1x</code><br>- <code>dot1x-coa</code><br>- <code>dot1x-phone-classification</code><br>- <code>dot1x-session-replace</code><br>- <code>error-correction-encoding</code><br>- <code>hardware-speed-group</code><br>- <code>interface-speed</code><br>- <code>internal-error</code><br>- <code>link-change</code><br>- <code>port-breakout</code><br>- <code>storm-control</code><br>- <code>switchcard-unreachable</code><br>- <code>tapagg</code><br>- <code>transceiver-adapter</code><br>- <code>xcvr-misconfigured</code><br>- <code>xcvr-overheat</code><br>- <code>xcvr-power-unsupported</code> | Specifies the events that should trigger this action.<br>The list of supported causes depends on both the EOS version and the hardware platform. |
    | [<samp>&nbsp;&nbsp;detect_cause</samp>](## "errdisable.detect_cause") | Dictionary |  |  |  | Specifies the events that should trigger this action.<br>The list of supported causes depends on both the EOS version and the hardware platform. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;acl</samp>](## "errdisable.detect_cause.acl") | Boolean |  |  |  | Enable/Disable detection for ACL errors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;arp_inspection</samp>](## "errdisable.detect_cause.arp_inspection") | Boolean |  |  |  | Enable/Disable detection for ARP inspection errors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;dot1x</samp>](## "errdisable.detect_cause.dot1x") | Boolean |  |  |  | Enable/Disable detection for 802.1X errors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;dot1x_coa</samp>](## "errdisable.detect_cause.dot1x_coa") | Boolean |  |  |  | Enable/Disable detection for 802.1X Change of Authorization errors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;dot1x_phone_classification</samp>](## "errdisable.detect_cause.dot1x_phone_classification") | Boolean |  |  |  | Enable/Disable detection for 802.1X phone classification errors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;dot1x_session_replace</samp>](## "errdisable.detect_cause.dot1x_session_replace") | Boolean |  |  |  | Enable/Disable detection for 802.1X session replace errors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;error_correction_encoding</samp>](## "errdisable.detect_cause.error_correction_encoding") | Boolean |  |  |  | Enable/Disable detection for error correction encoding errors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;fabric_capacity_low</samp>](## "errdisable.detect_cause.fabric_capacity_low") | Boolean |  |  |  | Enable/Disable detection for fabric capacity low errors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;hardware_speed_group</samp>](## "errdisable.detect_cause.hardware_speed_group") | Boolean |  |  |  | Enable/Disable detection for hardware speed group errors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;interface_speed</samp>](## "errdisable.detect_cause.interface_speed") | Boolean |  |  |  | Enable/Disable detection for interface speed errors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;internal_error</samp>](## "errdisable.detect_cause.internal_error") | Boolean |  |  |  | Enable/Disable detection for internal errors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;link_change</samp>](## "errdisable.detect_cause.link_change") | Boolean |  |  |  | Enable/Disable detection for link change errors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;port_breakout</samp>](## "errdisable.detect_cause.port_breakout") | Boolean |  |  |  | Enable/Disable detection for port breakout errors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;storm_control</samp>](## "errdisable.detect_cause.storm_control") | Boolean |  |  |  | Enable/Disable detection for storm control errors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;switchcard_unreachable</samp>](## "errdisable.detect_cause.switchcard_unreachable") | Boolean |  |  |  | Enable/Disable detection for switchcard unreachable errors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;tapagg</samp>](## "errdisable.detect_cause.tapagg") | Boolean |  |  |  | Enable/Disable detection for tap aggregation errors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;tpid</samp>](## "errdisable.detect_cause.tpid") | Boolean |  |  |  | Enable/Disable detection for TPID errors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;transceiver_adapter</samp>](## "errdisable.detect_cause.transceiver_adapter") | Boolean |  |  |  | Enable/Disable detection for transceiver adapter errors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;xcvr_misconfigured</samp>](## "errdisable.detect_cause.xcvr_misconfigured") | Boolean |  |  |  | Enable/Disable detection for transceiver misconfiguration errors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;xcvr_overheat</samp>](## "errdisable.detect_cause.xcvr_overheat") | Boolean |  |  |  | Enable/Disable detection for transceiver overheat errors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;xcvr_power_unsupported</samp>](## "errdisable.detect_cause.xcvr_power_unsupported") | Boolean |  |  |  | Enable/Disable detection for unsupported transceiver power errors. |
    | [<samp>&nbsp;&nbsp;recovery</samp>](## "errdisable.recovery") <span style="color:red">deprecated</span> | Dictionary |  |  |  | <span style="color:red">This key is deprecated. Support will be removed in AVD version 7.0.0. Use <samp>recovery_cause or recovery_interval</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;causes</samp>](## "errdisable.recovery.causes") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "errdisable.recovery.causes.[].name") | String | Required, Unique |  | Valid Values:<br>- <code>acl</code><br>- <code>arp-inspection</code><br>- <code>bpduguard</code><br>- <code>dot1x</code><br>- <code>dot1x-coa</code><br>- <code>dot1x-phone-classification</code><br>- <code>dot1x-session-replace</code><br>- <code>error-correction-encoding</code><br>- <code>hardware-speed-group</code><br>- <code>hitless-reload-down</code><br>- <code>interface-speed</code><br>- <code>internal-error</code><br>- <code>lacp-rate-limit</code><br>- <code>link-flap</code><br>- <code>no-internal-vlan</code><br>- <code>port-breakout</code><br>- <code>portchannelguard</code><br>- <code>portsec</code><br>- <code>speed-misconfigured</code><br>- <code>storm-control</code><br>- <code>stuck-queue</code><br>- <code>switchcard-unreachable</code><br>- <code>tap-port-init</code><br>- <code>tapagg</code><br>- <code>transceiver-adapter</code><br>- <code>uplink-failure-detection</code><br>- <code>xcvr-misconfigured</code><br>- <code>xcvr-overheat</code><br>- <code>xcvr-power-unsupported</code><br>- <code>xcvr-unsupported</code> | Specifies the type of event that can trigger recovery actions.<br>The list of supported causes depends on both the EOS version and the hardware platform. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interval</samp>](## "errdisable.recovery.causes.[].interval") | Integer |  |  | Min: 30<br>Max: 86400 | Interval for each recovery cause in seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;interval</samp>](## "errdisable.recovery.interval") | Integer |  |  | Min: 30<br>Max: 86400 | Interval in seconds. |
    | [<samp>&nbsp;&nbsp;recovery_cause</samp>](## "errdisable.recovery_cause") | Dictionary |  |  |  | Specifies the type of event that can trigger recovery actions.<br>The list of supported causes depends on both the EOS version and the hardware platform. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;acl</samp>](## "errdisable.recovery_cause.acl") | Dictionary |  |  |  | Recovery settings for ACL errors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "errdisable.recovery_cause.acl.enabled") | Boolean | Required |  |  | Enable recovery for ACL errors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interval</samp>](## "errdisable.recovery_cause.acl.interval") | Integer |  |  | Min: 30<br>Max: 86400 | Interval for ACL recovery in seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;arp_inspection</samp>](## "errdisable.recovery_cause.arp_inspection") | Dictionary |  |  |  | Recovery settings for ARP inspection errors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "errdisable.recovery_cause.arp_inspection.enabled") | Boolean | Required |  |  | Enable recovery for ARP inspection errors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interval</samp>](## "errdisable.recovery_cause.arp_inspection.interval") | Integer |  |  | Min: 30<br>Max: 86400 | Interval for ARP inspection recovery in seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;bpduguard</samp>](## "errdisable.recovery_cause.bpduguard") | Dictionary |  |  |  | Recovery settings for BPDU guard errors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "errdisable.recovery_cause.bpduguard.enabled") | Boolean | Required |  |  | Enable recovery for BPDU guard errors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interval</samp>](## "errdisable.recovery_cause.bpduguard.interval") | Integer |  |  | Min: 30<br>Max: 86400 | Interval for BPDU guard recovery in seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;dot1x</samp>](## "errdisable.recovery_cause.dot1x") | Dictionary |  |  |  | Recovery settings for 802.1X errors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "errdisable.recovery_cause.dot1x.enabled") | Boolean | Required |  |  | Enable recovery for 802.1X errors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interval</samp>](## "errdisable.recovery_cause.dot1x.interval") | Integer |  |  | Min: 30<br>Max: 86400 | Interval for 802.1X recovery in seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;dot1x_coa</samp>](## "errdisable.recovery_cause.dot1x_coa") | Dictionary |  |  |  | Recovery settings for 802.1X Change of Authorization errors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "errdisable.recovery_cause.dot1x_coa.enabled") | Boolean | Required |  |  | Enable recovery for 802.1X Change of Authorization errors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interval</samp>](## "errdisable.recovery_cause.dot1x_coa.interval") | Integer |  |  | Min: 30<br>Max: 86400 | Interval for 802.1X Change of Authorization recovery in seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;dot1x_phone_classification</samp>](## "errdisable.recovery_cause.dot1x_phone_classification") | Dictionary |  |  |  | Recovery settings for 802.1X phone classification errors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "errdisable.recovery_cause.dot1x_phone_classification.enabled") | Boolean | Required |  |  | Enable recovery for 802.1X phone classification errors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interval</samp>](## "errdisable.recovery_cause.dot1x_phone_classification.interval") | Integer |  |  | Min: 30<br>Max: 86400 | Interval for 802.1X phone classification recovery in seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;dot1x_session_replace</samp>](## "errdisable.recovery_cause.dot1x_session_replace") | Dictionary |  |  |  | Recovery settings for 802.1X session replace errors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "errdisable.recovery_cause.dot1x_session_replace.enabled") | Boolean | Required |  |  | Enable recovery for 802.1X session replace errors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interval</samp>](## "errdisable.recovery_cause.dot1x_session_replace.interval") | Integer |  |  | Min: 30<br>Max: 86400 | Interval for 802.1X session replace recovery in seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;error_correction_encoding</samp>](## "errdisable.recovery_cause.error_correction_encoding") | Dictionary |  |  |  | Recovery settings for error correction encoding errors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "errdisable.recovery_cause.error_correction_encoding.enabled") | Boolean | Required |  |  | Enable recovery for error correction encoding errors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interval</samp>](## "errdisable.recovery_cause.error_correction_encoding.interval") | Integer |  |  | Min: 30<br>Max: 86400 | Interval for error correction encoding recovery in seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;fabric_capacity_low</samp>](## "errdisable.recovery_cause.fabric_capacity_low") | Dictionary |  |  |  | Recovery settings for fabric capacity low errors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "errdisable.recovery_cause.fabric_capacity_low.enabled") | Boolean | Required |  |  | Enable recovery for fabric capacity low errors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interval</samp>](## "errdisable.recovery_cause.fabric_capacity_low.interval") | Integer |  |  | Min: 30<br>Max: 86400 | Interval for fabric capacity low recovery in seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;hardware_speed_group</samp>](## "errdisable.recovery_cause.hardware_speed_group") | Dictionary |  |  |  | Recovery settings for hardware speed group errors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "errdisable.recovery_cause.hardware_speed_group.enabled") | Boolean | Required |  |  | Enable recovery for hardware speed group errors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interval</samp>](## "errdisable.recovery_cause.hardware_speed_group.interval") | Integer |  |  | Min: 30<br>Max: 86400 | Interval for hardware speed group recovery in seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;hitless_reload_down</samp>](## "errdisable.recovery_cause.hitless_reload_down") | Dictionary |  |  |  | Recovery settings for hitless reload down errors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "errdisable.recovery_cause.hitless_reload_down.enabled") | Boolean | Required |  |  | Enable recovery for hitless reload down errors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interval</samp>](## "errdisable.recovery_cause.hitless_reload_down.interval") | Integer |  |  | Min: 30<br>Max: 86400 | Interval for hitless reload down recovery in seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;interface_speed</samp>](## "errdisable.recovery_cause.interface_speed") | Dictionary |  |  |  | Recovery settings for interface speed errors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "errdisable.recovery_cause.interface_speed.enabled") | Boolean | Required |  |  | Enable recovery for interface speed errors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interval</samp>](## "errdisable.recovery_cause.interface_speed.interval") | Integer |  |  | Min: 30<br>Max: 86400 | Interval for interface speed recovery in seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;internal_error</samp>](## "errdisable.recovery_cause.internal_error") | Dictionary |  |  |  | Recovery settings for internal errors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "errdisable.recovery_cause.internal_error.enabled") | Boolean | Required |  |  | Enable recovery for internal errors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interval</samp>](## "errdisable.recovery_cause.internal_error.interval") | Integer |  |  | Min: 30<br>Max: 86400 | Interval for internal error recovery in seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;lacp_rate_limit</samp>](## "errdisable.recovery_cause.lacp_rate_limit") | Dictionary |  |  |  | Recovery settings for LACP rate limit errors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "errdisable.recovery_cause.lacp_rate_limit.enabled") | Boolean | Required |  |  | Enable recovery for LACP rate limit errors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interval</samp>](## "errdisable.recovery_cause.lacp_rate_limit.interval") | Integer |  |  | Min: 30<br>Max: 86400 | Interval for LACP rate limit recovery in seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;link_flap</samp>](## "errdisable.recovery_cause.link_flap") | Dictionary |  |  |  | Recovery settings for link flap errors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "errdisable.recovery_cause.link_flap.enabled") | Boolean | Required |  |  | Enable recovery for link flap errors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interval</samp>](## "errdisable.recovery_cause.link_flap.interval") | Integer |  |  | Min: 30<br>Max: 86400 | Interval for link flap recovery in seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;no_internal_vlan</samp>](## "errdisable.recovery_cause.no_internal_vlan") | Dictionary |  |  |  | Recovery settings for no internal VLAN errors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "errdisable.recovery_cause.no_internal_vlan.enabled") | Boolean | Required |  |  | Enable recovery for no internal VLAN errors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interval</samp>](## "errdisable.recovery_cause.no_internal_vlan.interval") | Integer |  |  | Min: 30<br>Max: 86400 | Interval for no internal VLAN recovery in seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;port_breakout</samp>](## "errdisable.recovery_cause.port_breakout") | Dictionary |  |  |  | Recovery settings for port breakout errors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "errdisable.recovery_cause.port_breakout.enabled") | Boolean | Required |  |  | Enable recovery for port breakout errors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interval</samp>](## "errdisable.recovery_cause.port_breakout.interval") | Integer |  |  | Min: 30<br>Max: 86400 | Interval for port breakout recovery in seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;portchannelguard</samp>](## "errdisable.recovery_cause.portchannelguard") | Dictionary |  |  |  | Recovery settings for port-channel guard errors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "errdisable.recovery_cause.portchannelguard.enabled") | Boolean | Required |  |  | Enable recovery for port-channel guard errors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interval</samp>](## "errdisable.recovery_cause.portchannelguard.interval") | Integer |  |  | Min: 30<br>Max: 86400 | Interval for port-channel guard recovery in seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;portsec</samp>](## "errdisable.recovery_cause.portsec") | Dictionary |  |  |  | Recovery settings for port security errors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "errdisable.recovery_cause.portsec.enabled") | Boolean | Required |  |  | Enable recovery for port security errors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interval</samp>](## "errdisable.recovery_cause.portsec.interval") | Integer |  |  | Min: 30<br>Max: 86400 | Interval for port security recovery in seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;speed_misconfigured</samp>](## "errdisable.recovery_cause.speed_misconfigured") | Dictionary |  |  |  | Recovery settings for speed misconfigured errors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "errdisable.recovery_cause.speed_misconfigured.enabled") | Boolean | Required |  |  | Enable recovery for speed misconfigured errors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interval</samp>](## "errdisable.recovery_cause.speed_misconfigured.interval") | Integer |  |  | Min: 30<br>Max: 86400 | Interval for speed misconfigured recovery in seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;storm_control</samp>](## "errdisable.recovery_cause.storm_control") | Dictionary |  |  |  | Recovery settings for storm control errors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "errdisable.recovery_cause.storm_control.enabled") | Boolean | Required |  |  | Enable recovery for storm control errors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interval</samp>](## "errdisable.recovery_cause.storm_control.interval") | Integer |  |  | Min: 30<br>Max: 86400 | Interval for storm control recovery in seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;stuck_queue</samp>](## "errdisable.recovery_cause.stuck_queue") | Dictionary |  |  |  | Recovery settings for stuck queue errors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "errdisable.recovery_cause.stuck_queue.enabled") | Boolean | Required |  |  | Enable recovery for stuck queue errors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interval</samp>](## "errdisable.recovery_cause.stuck_queue.interval") | Integer |  |  | Min: 30<br>Max: 86400 | Interval for stuck queue recovery in seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;switchcard_unreachable</samp>](## "errdisable.recovery_cause.switchcard_unreachable") | Dictionary |  |  |  | Recovery settings for switchcard unreachable errors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "errdisable.recovery_cause.switchcard_unreachable.enabled") | Boolean | Required |  |  | Enable recovery for switchcard unreachable errors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interval</samp>](## "errdisable.recovery_cause.switchcard_unreachable.interval") | Integer |  |  | Min: 30<br>Max: 86400 | Interval for switchcard unreachable recovery in seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;tap_port_init</samp>](## "errdisable.recovery_cause.tap_port_init") | Dictionary |  |  |  | Recovery settings for tap port init errors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "errdisable.recovery_cause.tap_port_init.enabled") | Boolean | Required |  |  | Enable recovery for tap port init errors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interval</samp>](## "errdisable.recovery_cause.tap_port_init.interval") | Integer |  |  | Min: 30<br>Max: 86400 | Interval for tap port init recovery in seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;tapagg</samp>](## "errdisable.recovery_cause.tapagg") | Dictionary |  |  |  | Recovery settings for tap aggregation errors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "errdisable.recovery_cause.tapagg.enabled") | Boolean | Required |  |  | Enable recovery for tap aggregation errors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interval</samp>](## "errdisable.recovery_cause.tapagg.interval") | Integer |  |  | Min: 30<br>Max: 86400 | Interval for tap aggregation recovery in seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;tpid</samp>](## "errdisable.recovery_cause.tpid") | Dictionary |  |  |  | Recovery settings for TPID errors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "errdisable.recovery_cause.tpid.enabled") | Boolean | Required |  |  | Enable recovery for TPID errors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interval</samp>](## "errdisable.recovery_cause.tpid.interval") | Integer |  |  | Min: 30<br>Max: 86400 | Interval for TPID recovery in seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;transceiver_adapter</samp>](## "errdisable.recovery_cause.transceiver_adapter") | Dictionary |  |  |  | Recovery settings for transceiver adapter errors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "errdisable.recovery_cause.transceiver_adapter.enabled") | Boolean | Required |  |  | Enable recovery for transceiver adapter errors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interval</samp>](## "errdisable.recovery_cause.transceiver_adapter.interval") | Integer |  |  | Min: 30<br>Max: 86400 | Interval for transceiver adapter recovery in seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;uplink_failure_detection</samp>](## "errdisable.recovery_cause.uplink_failure_detection") | Dictionary |  |  |  | Recovery settings for uplink failure detection errors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "errdisable.recovery_cause.uplink_failure_detection.enabled") | Boolean | Required |  |  | Enable recovery for uplink failure detection errors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interval</samp>](## "errdisable.recovery_cause.uplink_failure_detection.interval") | Integer |  |  | Min: 30<br>Max: 86400 | Interval for uplink failure detection recovery in seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;xcvr_misconfigured</samp>](## "errdisable.recovery_cause.xcvr_misconfigured") | Dictionary |  |  |  | Recovery settings for transceiver misconfiguration errors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "errdisable.recovery_cause.xcvr_misconfigured.enabled") | Boolean | Required |  |  | Enable recovery for transceiver misconfiguration errors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interval</samp>](## "errdisable.recovery_cause.xcvr_misconfigured.interval") | Integer |  |  | Min: 30<br>Max: 86400 | Interval for transceiver misconfiguration recovery in seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;xcvr_overheat</samp>](## "errdisable.recovery_cause.xcvr_overheat") | Dictionary |  |  |  | Recovery settings for transceiver overheat errors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "errdisable.recovery_cause.xcvr_overheat.enabled") | Boolean | Required |  |  | Enable recovery for transceiver overheat errors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interval</samp>](## "errdisable.recovery_cause.xcvr_overheat.interval") | Integer |  |  | Min: 30<br>Max: 86400 | Interval for transceiver overheat recovery in seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;xcvr_power_unsupported</samp>](## "errdisable.recovery_cause.xcvr_power_unsupported") | Dictionary |  |  |  | Recovery settings for unsupported transceiver power errors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "errdisable.recovery_cause.xcvr_power_unsupported.enabled") | Boolean | Required |  |  | Enable recovery for unsupported transceiver power errors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interval</samp>](## "errdisable.recovery_cause.xcvr_power_unsupported.interval") | Integer |  |  | Min: 30<br>Max: 86400 | Interval for unsupported transceiver power recovery in seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;xcvr_unsupported</samp>](## "errdisable.recovery_cause.xcvr_unsupported") | Dictionary |  |  |  | Recovery settings for unsupported transceiver errors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "errdisable.recovery_cause.xcvr_unsupported.enabled") | Boolean | Required |  |  | Enable recovery for unsupported transceiver errors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interval</samp>](## "errdisable.recovery_cause.xcvr_unsupported.interval") | Integer |  |  | Min: 30<br>Max: 86400 | Interval for unsupported transceiver recovery in seconds. |
    | [<samp>&nbsp;&nbsp;recovery_interval</samp>](## "errdisable.recovery_interval") | Integer |  |  | Min: 30<br>Max: 86400 | Default recovery interval in seconds applied to all recovery causes. EOS default is 300 seconds. |

=== "YAML"

    ```yaml
    errdisable:
      # This key is deprecated.
      # Support will be removed in AVD version 7.0.0.
      # Use `detect_cause` instead.
      detect:
        causes:

            # Specifies the events that should trigger this action.
            # The list of supported causes depends on both the EOS version and the hardware platform.
          - <str; "acl" | "arp-inspection" | "dot1x" | "dot1x-coa" | "dot1x-phone-classification" | "dot1x-session-replace" | "error-correction-encoding" | "hardware-speed-group" | "interface-speed" | "internal-error" | "link-change" | "port-breakout" | "storm-control" | "switchcard-unreachable" | "tapagg" | "transceiver-adapter" | "xcvr-misconfigured" | "xcvr-overheat" | "xcvr-power-unsupported">

      # Specifies the events that should trigger this action.
      # The list of supported causes depends on both the EOS version and the hardware platform.
      detect_cause:

        # Enable/Disable detection for ACL errors.
        acl: <bool>

        # Enable/Disable detection for ARP inspection errors.
        arp_inspection: <bool>

        # Enable/Disable detection for 802.1X errors.
        dot1x: <bool>

        # Enable/Disable detection for 802.1X Change of Authorization errors.
        dot1x_coa: <bool>

        # Enable/Disable detection for 802.1X phone classification errors.
        dot1x_phone_classification: <bool>

        # Enable/Disable detection for 802.1X session replace errors.
        dot1x_session_replace: <bool>

        # Enable/Disable detection for error correction encoding errors.
        error_correction_encoding: <bool>

        # Enable/Disable detection for fabric capacity low errors.
        fabric_capacity_low: <bool>

        # Enable/Disable detection for hardware speed group errors.
        hardware_speed_group: <bool>

        # Enable/Disable detection for interface speed errors.
        interface_speed: <bool>

        # Enable/Disable detection for internal errors.
        internal_error: <bool>

        # Enable/Disable detection for link change errors.
        link_change: <bool>

        # Enable/Disable detection for port breakout errors.
        port_breakout: <bool>

        # Enable/Disable detection for storm control errors.
        storm_control: <bool>

        # Enable/Disable detection for switchcard unreachable errors.
        switchcard_unreachable: <bool>

        # Enable/Disable detection for tap aggregation errors.
        tapagg: <bool>

        # Enable/Disable detection for TPID errors.
        tpid: <bool>

        # Enable/Disable detection for transceiver adapter errors.
        transceiver_adapter: <bool>

        # Enable/Disable detection for transceiver misconfiguration errors.
        xcvr_misconfigured: <bool>

        # Enable/Disable detection for transceiver overheat errors.
        xcvr_overheat: <bool>

        # Enable/Disable detection for unsupported transceiver power errors.
        xcvr_power_unsupported: <bool>
      # This key is deprecated.
      # Support will be removed in AVD version 7.0.0.
      # Use `recovery_cause` or `recovery_interval` instead.
      recovery:
        causes:

            # Specifies the type of event that can trigger recovery actions.
            # The list of supported causes depends on both the EOS version and the hardware platform.
          - name: <str; "acl" | "arp-inspection" | "bpduguard" | "dot1x" | "dot1x-coa" | "dot1x-phone-classification" | "dot1x-session-replace" | "error-correction-encoding" | "hardware-speed-group" | "hitless-reload-down" | "interface-speed" | "internal-error" | "lacp-rate-limit" | "link-flap" | "no-internal-vlan" | "port-breakout" | "portchannelguard" | "portsec" | "speed-misconfigured" | "storm-control" | "stuck-queue" | "switchcard-unreachable" | "tap-port-init" | "tapagg" | "transceiver-adapter" | "uplink-failure-detection" | "xcvr-misconfigured" | "xcvr-overheat" | "xcvr-power-unsupported" | "xcvr-unsupported"; required; unique>

            # Interval for each recovery cause in seconds.
            interval: <int; 30-86400>

        # Interval in seconds.
        interval: <int; 30-86400>

      # Specifies the type of event that can trigger recovery actions.
      # The list of supported causes depends on both the EOS version and the hardware platform.
      recovery_cause:

        # Recovery settings for ACL errors.
        acl:

          # Enable recovery for ACL errors.
          enabled: <bool; required>

          # Interval for ACL recovery in seconds.
          interval: <int; 30-86400>

        # Recovery settings for ARP inspection errors.
        arp_inspection:

          # Enable recovery for ARP inspection errors.
          enabled: <bool; required>

          # Interval for ARP inspection recovery in seconds.
          interval: <int; 30-86400>

        # Recovery settings for BPDU guard errors.
        bpduguard:

          # Enable recovery for BPDU guard errors.
          enabled: <bool; required>

          # Interval for BPDU guard recovery in seconds.
          interval: <int; 30-86400>

        # Recovery settings for 802.1X errors.
        dot1x:

          # Enable recovery for 802.1X errors.
          enabled: <bool; required>

          # Interval for 802.1X recovery in seconds.
          interval: <int; 30-86400>

        # Recovery settings for 802.1X Change of Authorization errors.
        dot1x_coa:

          # Enable recovery for 802.1X Change of Authorization errors.
          enabled: <bool; required>

          # Interval for 802.1X Change of Authorization recovery in seconds.
          interval: <int; 30-86400>

        # Recovery settings for 802.1X phone classification errors.
        dot1x_phone_classification:

          # Enable recovery for 802.1X phone classification errors.
          enabled: <bool; required>

          # Interval for 802.1X phone classification recovery in seconds.
          interval: <int; 30-86400>

        # Recovery settings for 802.1X session replace errors.
        dot1x_session_replace:

          # Enable recovery for 802.1X session replace errors.
          enabled: <bool; required>

          # Interval for 802.1X session replace recovery in seconds.
          interval: <int; 30-86400>

        # Recovery settings for error correction encoding errors.
        error_correction_encoding:

          # Enable recovery for error correction encoding errors.
          enabled: <bool; required>

          # Interval for error correction encoding recovery in seconds.
          interval: <int; 30-86400>

        # Recovery settings for fabric capacity low errors.
        fabric_capacity_low:

          # Enable recovery for fabric capacity low errors.
          enabled: <bool; required>

          # Interval for fabric capacity low recovery in seconds.
          interval: <int; 30-86400>

        # Recovery settings for hardware speed group errors.
        hardware_speed_group:

          # Enable recovery for hardware speed group errors.
          enabled: <bool; required>

          # Interval for hardware speed group recovery in seconds.
          interval: <int; 30-86400>

        # Recovery settings for hitless reload down errors.
        hitless_reload_down:

          # Enable recovery for hitless reload down errors.
          enabled: <bool; required>

          # Interval for hitless reload down recovery in seconds.
          interval: <int; 30-86400>

        # Recovery settings for interface speed errors.
        interface_speed:

          # Enable recovery for interface speed errors.
          enabled: <bool; required>

          # Interval for interface speed recovery in seconds.
          interval: <int; 30-86400>

        # Recovery settings for internal errors.
        internal_error:

          # Enable recovery for internal errors.
          enabled: <bool; required>

          # Interval for internal error recovery in seconds.
          interval: <int; 30-86400>

        # Recovery settings for LACP rate limit errors.
        lacp_rate_limit:

          # Enable recovery for LACP rate limit errors.
          enabled: <bool; required>

          # Interval for LACP rate limit recovery in seconds.
          interval: <int; 30-86400>

        # Recovery settings for link flap errors.
        link_flap:

          # Enable recovery for link flap errors.
          enabled: <bool; required>

          # Interval for link flap recovery in seconds.
          interval: <int; 30-86400>

        # Recovery settings for no internal VLAN errors.
        no_internal_vlan:

          # Enable recovery for no internal VLAN errors.
          enabled: <bool; required>

          # Interval for no internal VLAN recovery in seconds.
          interval: <int; 30-86400>

        # Recovery settings for port breakout errors.
        port_breakout:

          # Enable recovery for port breakout errors.
          enabled: <bool; required>

          # Interval for port breakout recovery in seconds.
          interval: <int; 30-86400>

        # Recovery settings for port-channel guard errors.
        portchannelguard:

          # Enable recovery for port-channel guard errors.
          enabled: <bool; required>

          # Interval for port-channel guard recovery in seconds.
          interval: <int; 30-86400>

        # Recovery settings for port security errors.
        portsec:

          # Enable recovery for port security errors.
          enabled: <bool; required>

          # Interval for port security recovery in seconds.
          interval: <int; 30-86400>

        # Recovery settings for speed misconfigured errors.
        speed_misconfigured:

          # Enable recovery for speed misconfigured errors.
          enabled: <bool; required>

          # Interval for speed misconfigured recovery in seconds.
          interval: <int; 30-86400>

        # Recovery settings for storm control errors.
        storm_control:

          # Enable recovery for storm control errors.
          enabled: <bool; required>

          # Interval for storm control recovery in seconds.
          interval: <int; 30-86400>

        # Recovery settings for stuck queue errors.
        stuck_queue:

          # Enable recovery for stuck queue errors.
          enabled: <bool; required>

          # Interval for stuck queue recovery in seconds.
          interval: <int; 30-86400>

        # Recovery settings for switchcard unreachable errors.
        switchcard_unreachable:

          # Enable recovery for switchcard unreachable errors.
          enabled: <bool; required>

          # Interval for switchcard unreachable recovery in seconds.
          interval: <int; 30-86400>

        # Recovery settings for tap port init errors.
        tap_port_init:

          # Enable recovery for tap port init errors.
          enabled: <bool; required>

          # Interval for tap port init recovery in seconds.
          interval: <int; 30-86400>

        # Recovery settings for tap aggregation errors.
        tapagg:

          # Enable recovery for tap aggregation errors.
          enabled: <bool; required>

          # Interval for tap aggregation recovery in seconds.
          interval: <int; 30-86400>

        # Recovery settings for TPID errors.
        tpid:

          # Enable recovery for TPID errors.
          enabled: <bool; required>

          # Interval for TPID recovery in seconds.
          interval: <int; 30-86400>

        # Recovery settings for transceiver adapter errors.
        transceiver_adapter:

          # Enable recovery for transceiver adapter errors.
          enabled: <bool; required>

          # Interval for transceiver adapter recovery in seconds.
          interval: <int; 30-86400>

        # Recovery settings for uplink failure detection errors.
        uplink_failure_detection:

          # Enable recovery for uplink failure detection errors.
          enabled: <bool; required>

          # Interval for uplink failure detection recovery in seconds.
          interval: <int; 30-86400>

        # Recovery settings for transceiver misconfiguration errors.
        xcvr_misconfigured:

          # Enable recovery for transceiver misconfiguration errors.
          enabled: <bool; required>

          # Interval for transceiver misconfiguration recovery in seconds.
          interval: <int; 30-86400>

        # Recovery settings for transceiver overheat errors.
        xcvr_overheat:

          # Enable recovery for transceiver overheat errors.
          enabled: <bool; required>

          # Interval for transceiver overheat recovery in seconds.
          interval: <int; 30-86400>

        # Recovery settings for unsupported transceiver power errors.
        xcvr_power_unsupported:

          # Enable recovery for unsupported transceiver power errors.
          enabled: <bool; required>

          # Interval for unsupported transceiver power recovery in seconds.
          interval: <int; 30-86400>

        # Recovery settings for unsupported transceiver errors.
        xcvr_unsupported:

          # Enable recovery for unsupported transceiver errors.
          enabled: <bool; required>

          # Interval for unsupported transceiver recovery in seconds.
          interval: <int; 30-86400>

      # Default recovery interval in seconds applied to all recovery causes. EOS default is 300 seconds.
      recovery_interval: <int; 30-86400>
    ```
