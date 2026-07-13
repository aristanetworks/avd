<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>default_igmp_snooping_enabled</samp>](## "default_igmp_snooping_enabled") | Boolean |  | `True` |  | When set to false, disables IGMP snooping at fabric level and overrides per vlan settings.<br> |
    | [<samp>default_interface_mtu</samp>](## "default_interface_mtu") | Integer |  |  | Min: 68<br>Max: 65535 | Default interface MTU configured on EOS under "interface defaults".<br>Can be overridden per platform under platform settings.<br> |
    | [<samp>errdisable_settings</samp>](## "errdisable_settings") | Dictionary |  |  |  | Errdisable settings for the device.<br>Causes are filtered based on platform feature support defined in<br>`platform_settings.feature_support.errdisable_causes.<cause>.detection` and<br>`platform_settings.feature_support.errdisable_causes.<cause>.recovery`. |
    | [<samp>&nbsp;&nbsp;recovery_interval</samp>](## "errdisable_settings.recovery_interval") | Integer |  |  | Min: 30<br>Max: 86400 | Interval for all recovery causes in seconds. |
    | [<samp>&nbsp;&nbsp;causes</samp>](## "errdisable_settings.causes") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;acl</samp>](## "errdisable_settings.causes.acl") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;detection</samp>](## "errdisable_settings.causes.acl.detection") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;recovery</samp>](## "errdisable_settings.causes.acl.recovery") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;recovery_interval</samp>](## "errdisable_settings.causes.acl.recovery_interval") | Integer |  |  | Min: 30<br>Max: 86400 | Interval for each recovery cause in seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;arp_inspection</samp>](## "errdisable_settings.causes.arp_inspection") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;detection</samp>](## "errdisable_settings.causes.arp_inspection.detection") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;recovery</samp>](## "errdisable_settings.causes.arp_inspection.recovery") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;recovery_interval</samp>](## "errdisable_settings.causes.arp_inspection.recovery_interval") | Integer |  |  | Min: 30<br>Max: 86400 | Interval for each recovery cause in seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;bpduguard</samp>](## "errdisable_settings.causes.bpduguard") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;recovery</samp>](## "errdisable_settings.causes.bpduguard.recovery") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;recovery_interval</samp>](## "errdisable_settings.causes.bpduguard.recovery_interval") | Integer |  |  | Min: 30<br>Max: 86400 | Interval for each recovery cause in seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;dot1x</samp>](## "errdisable_settings.causes.dot1x") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;detection</samp>](## "errdisable_settings.causes.dot1x.detection") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;recovery</samp>](## "errdisable_settings.causes.dot1x.recovery") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;recovery_interval</samp>](## "errdisable_settings.causes.dot1x.recovery_interval") | Integer |  |  | Min: 30<br>Max: 86400 | Interval for each recovery cause in seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;dot1x_coa</samp>](## "errdisable_settings.causes.dot1x_coa") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;detection</samp>](## "errdisable_settings.causes.dot1x_coa.detection") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;recovery</samp>](## "errdisable_settings.causes.dot1x_coa.recovery") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;recovery_interval</samp>](## "errdisable_settings.causes.dot1x_coa.recovery_interval") | Integer |  |  | Min: 30<br>Max: 86400 | Interval for each recovery cause in seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;dot1x_phone_classification</samp>](## "errdisable_settings.causes.dot1x_phone_classification") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;detection</samp>](## "errdisable_settings.causes.dot1x_phone_classification.detection") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;recovery</samp>](## "errdisable_settings.causes.dot1x_phone_classification.recovery") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;recovery_interval</samp>](## "errdisable_settings.causes.dot1x_phone_classification.recovery_interval") | Integer |  |  | Min: 30<br>Max: 86400 | Interval for each recovery cause in seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;dot1x_session_replace</samp>](## "errdisable_settings.causes.dot1x_session_replace") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;detection</samp>](## "errdisable_settings.causes.dot1x_session_replace.detection") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;recovery</samp>](## "errdisable_settings.causes.dot1x_session_replace.recovery") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;recovery_interval</samp>](## "errdisable_settings.causes.dot1x_session_replace.recovery_interval") | Integer |  |  | Min: 30<br>Max: 86400 | Interval for each recovery cause in seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;error_correction_encoding</samp>](## "errdisable_settings.causes.error_correction_encoding") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;detection</samp>](## "errdisable_settings.causes.error_correction_encoding.detection") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;recovery</samp>](## "errdisable_settings.causes.error_correction_encoding.recovery") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;recovery_interval</samp>](## "errdisable_settings.causes.error_correction_encoding.recovery_interval") | Integer |  |  | Min: 30<br>Max: 86400 | Interval for each recovery cause in seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;fabric_capacity_low</samp>](## "errdisable_settings.causes.fabric_capacity_low") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;detection</samp>](## "errdisable_settings.causes.fabric_capacity_low.detection") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;recovery</samp>](## "errdisable_settings.causes.fabric_capacity_low.recovery") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;recovery_interval</samp>](## "errdisable_settings.causes.fabric_capacity_low.recovery_interval") | Integer |  |  | Min: 30<br>Max: 86400 | Interval for each recovery cause in seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;hardware_speed_group</samp>](## "errdisable_settings.causes.hardware_speed_group") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;detection</samp>](## "errdisable_settings.causes.hardware_speed_group.detection") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;recovery</samp>](## "errdisable_settings.causes.hardware_speed_group.recovery") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;recovery_interval</samp>](## "errdisable_settings.causes.hardware_speed_group.recovery_interval") | Integer |  |  | Min: 30<br>Max: 86400 | Interval for each recovery cause in seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;hitless_reload_down</samp>](## "errdisable_settings.causes.hitless_reload_down") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;recovery</samp>](## "errdisable_settings.causes.hitless_reload_down.recovery") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;recovery_interval</samp>](## "errdisable_settings.causes.hitless_reload_down.recovery_interval") | Integer |  |  | Min: 30<br>Max: 86400 | Interval for each recovery cause in seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;interface_speed</samp>](## "errdisable_settings.causes.interface_speed") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;detection</samp>](## "errdisable_settings.causes.interface_speed.detection") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;recovery</samp>](## "errdisable_settings.causes.interface_speed.recovery") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;recovery_interval</samp>](## "errdisable_settings.causes.interface_speed.recovery_interval") | Integer |  |  | Min: 30<br>Max: 86400 | Interval for each recovery cause in seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;internal_error</samp>](## "errdisable_settings.causes.internal_error") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;detection</samp>](## "errdisable_settings.causes.internal_error.detection") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;recovery</samp>](## "errdisable_settings.causes.internal_error.recovery") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;recovery_interval</samp>](## "errdisable_settings.causes.internal_error.recovery_interval") | Integer |  |  | Min: 30<br>Max: 86400 | Interval for each recovery cause in seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;lacp_rate_limit</samp>](## "errdisable_settings.causes.lacp_rate_limit") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;recovery</samp>](## "errdisable_settings.causes.lacp_rate_limit.recovery") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;recovery_interval</samp>](## "errdisable_settings.causes.lacp_rate_limit.recovery_interval") | Integer |  |  | Min: 30<br>Max: 86400 | Interval for each recovery cause in seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;link_change</samp>](## "errdisable_settings.causes.link_change") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;detection</samp>](## "errdisable_settings.causes.link_change.detection") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;link_flap</samp>](## "errdisable_settings.causes.link_flap") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;recovery</samp>](## "errdisable_settings.causes.link_flap.recovery") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;recovery_interval</samp>](## "errdisable_settings.causes.link_flap.recovery_interval") | Integer |  |  | Min: 30<br>Max: 86400 | Interval for each recovery cause in seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;no_internal_vlan</samp>](## "errdisable_settings.causes.no_internal_vlan") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;recovery</samp>](## "errdisable_settings.causes.no_internal_vlan.recovery") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;recovery_interval</samp>](## "errdisable_settings.causes.no_internal_vlan.recovery_interval") | Integer |  |  | Min: 30<br>Max: 86400 | Interval for each recovery cause in seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;port_breakout</samp>](## "errdisable_settings.causes.port_breakout") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;detection</samp>](## "errdisable_settings.causes.port_breakout.detection") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;recovery</samp>](## "errdisable_settings.causes.port_breakout.recovery") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;recovery_interval</samp>](## "errdisable_settings.causes.port_breakout.recovery_interval") | Integer |  |  | Min: 30<br>Max: 86400 | Interval for each recovery cause in seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;portchannelguard</samp>](## "errdisable_settings.causes.portchannelguard") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;recovery</samp>](## "errdisable_settings.causes.portchannelguard.recovery") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;recovery_interval</samp>](## "errdisable_settings.causes.portchannelguard.recovery_interval") | Integer |  |  | Min: 30<br>Max: 86400 | Interval for each recovery cause in seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;portsec</samp>](## "errdisable_settings.causes.portsec") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;recovery</samp>](## "errdisable_settings.causes.portsec.recovery") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;recovery_interval</samp>](## "errdisable_settings.causes.portsec.recovery_interval") | Integer |  |  | Min: 30<br>Max: 86400 | Interval for each recovery cause in seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;speed_misconfigured</samp>](## "errdisable_settings.causes.speed_misconfigured") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;recovery</samp>](## "errdisable_settings.causes.speed_misconfigured.recovery") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;recovery_interval</samp>](## "errdisable_settings.causes.speed_misconfigured.recovery_interval") | Integer |  |  | Min: 30<br>Max: 86400 | Interval for each recovery cause in seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;storm_control</samp>](## "errdisable_settings.causes.storm_control") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;detection</samp>](## "errdisable_settings.causes.storm_control.detection") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;recovery</samp>](## "errdisable_settings.causes.storm_control.recovery") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;recovery_interval</samp>](## "errdisable_settings.causes.storm_control.recovery_interval") | Integer |  |  | Min: 30<br>Max: 86400 | Interval for each recovery cause in seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;stuck_queue</samp>](## "errdisable_settings.causes.stuck_queue") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;recovery</samp>](## "errdisable_settings.causes.stuck_queue.recovery") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;recovery_interval</samp>](## "errdisable_settings.causes.stuck_queue.recovery_interval") | Integer |  |  | Min: 30<br>Max: 86400 | Interval for each recovery cause in seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;switchcard_unreachable</samp>](## "errdisable_settings.causes.switchcard_unreachable") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;detection</samp>](## "errdisable_settings.causes.switchcard_unreachable.detection") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;recovery</samp>](## "errdisable_settings.causes.switchcard_unreachable.recovery") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;recovery_interval</samp>](## "errdisable_settings.causes.switchcard_unreachable.recovery_interval") | Integer |  |  | Min: 30<br>Max: 86400 | Interval for each recovery cause in seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;tap_port_init</samp>](## "errdisable_settings.causes.tap_port_init") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;recovery</samp>](## "errdisable_settings.causes.tap_port_init.recovery") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;recovery_interval</samp>](## "errdisable_settings.causes.tap_port_init.recovery_interval") | Integer |  |  | Min: 30<br>Max: 86400 | Interval for each recovery cause in seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;tapagg</samp>](## "errdisable_settings.causes.tapagg") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;detection</samp>](## "errdisable_settings.causes.tapagg.detection") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;recovery</samp>](## "errdisable_settings.causes.tapagg.recovery") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;recovery_interval</samp>](## "errdisable_settings.causes.tapagg.recovery_interval") | Integer |  |  | Min: 30<br>Max: 86400 | Interval for each recovery cause in seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;tpid</samp>](## "errdisable_settings.causes.tpid") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;detection</samp>](## "errdisable_settings.causes.tpid.detection") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;recovery</samp>](## "errdisable_settings.causes.tpid.recovery") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;recovery_interval</samp>](## "errdisable_settings.causes.tpid.recovery_interval") | Integer |  |  | Min: 30<br>Max: 86400 | Interval for each recovery cause in seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;transceiver_adapter</samp>](## "errdisable_settings.causes.transceiver_adapter") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;detection</samp>](## "errdisable_settings.causes.transceiver_adapter.detection") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;recovery</samp>](## "errdisable_settings.causes.transceiver_adapter.recovery") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;recovery_interval</samp>](## "errdisable_settings.causes.transceiver_adapter.recovery_interval") | Integer |  |  | Min: 30<br>Max: 86400 | Interval for each recovery cause in seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;uplink_failure_detection</samp>](## "errdisable_settings.causes.uplink_failure_detection") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;recovery</samp>](## "errdisable_settings.causes.uplink_failure_detection.recovery") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;recovery_interval</samp>](## "errdisable_settings.causes.uplink_failure_detection.recovery_interval") | Integer |  |  | Min: 30<br>Max: 86400 | Interval for each recovery cause in seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;xcvr_misconfigured</samp>](## "errdisable_settings.causes.xcvr_misconfigured") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;detection</samp>](## "errdisable_settings.causes.xcvr_misconfigured.detection") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;recovery</samp>](## "errdisable_settings.causes.xcvr_misconfigured.recovery") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;recovery_interval</samp>](## "errdisable_settings.causes.xcvr_misconfigured.recovery_interval") | Integer |  |  | Min: 30<br>Max: 86400 | Interval for each recovery cause in seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;xcvr_overheat</samp>](## "errdisable_settings.causes.xcvr_overheat") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;detection</samp>](## "errdisable_settings.causes.xcvr_overheat.detection") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;recovery</samp>](## "errdisable_settings.causes.xcvr_overheat.recovery") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;recovery_interval</samp>](## "errdisable_settings.causes.xcvr_overheat.recovery_interval") | Integer |  |  | Min: 30<br>Max: 86400 | Interval for each recovery cause in seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;xcvr_power_unsupported</samp>](## "errdisable_settings.causes.xcvr_power_unsupported") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;detection</samp>](## "errdisable_settings.causes.xcvr_power_unsupported.detection") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;recovery</samp>](## "errdisable_settings.causes.xcvr_power_unsupported.recovery") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;recovery_interval</samp>](## "errdisable_settings.causes.xcvr_power_unsupported.recovery_interval") | Integer |  |  | Min: 30<br>Max: 86400 | Interval for each recovery cause in seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;xcvr_unsupported</samp>](## "errdisable_settings.causes.xcvr_unsupported") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;recovery</samp>](## "errdisable_settings.causes.xcvr_unsupported.recovery") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;recovery_interval</samp>](## "errdisable_settings.causes.xcvr_unsupported.recovery_interval") | Integer |  |  | Min: 30<br>Max: 86400 | Interval for each recovery cause in seconds. |
    | [<samp>general_settings</samp>](## "general_settings") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;interface_defaults</samp>](## "general_settings.interface_defaults") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ethernet_shutdown</samp>](## "general_settings.interface_defaults.ethernet_shutdown") | Boolean |  | `False` |  | Shutdown Ethernet interfaces by default unless they are explicitly enabled. |
    | [<samp>&nbsp;&nbsp;arp</samp>](## "general_settings.arp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;persistent</samp>](## "general_settings.arp.persistent") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "general_settings.arp.persistent.enabled") | Boolean | Required |  |  | Restore the ARP cache after reboot. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;refresh_delay</samp>](## "general_settings.arp.persistent.refresh_delay") | Integer |  |  | Min: 600<br>Max: 3600 | Time to wait in seconds before refreshing the ARP cache after reboot (EOS default 600). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;aging</samp>](## "general_settings.arp.aging") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;timeout_default</samp>](## "general_settings.arp.aging.timeout_default") | Integer |  |  | Min: 60<br>Max: 65535 | Timeout in seconds. |
    | [<samp>&nbsp;&nbsp;ip_icmp_redirect</samp>](## "general_settings.ip_icmp_redirect") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;dhcp_relay</samp>](## "general_settings.dhcp_relay") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;information_option</samp>](## "general_settings.dhcp_relay.information_option") | Boolean |  | `False` |  | Enables the insertion of DHCP Relay Agent Information (Option 82). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;tunnel_requests_disabled</samp>](## "general_settings.dhcp_relay.tunnel_requests_disabled") | Boolean |  | `False` |  | Blocks DHCP relay for packets received over VXLAN tunnels.<br>This is a VTEP-specific optimization and will only be configured on VXLAN VTEPs. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mlag_peerlink_requests_disabled</samp>](## "general_settings.dhcp_relay.mlag_peerlink_requests_disabled") | Boolean |  | `False` |  | Blocks DHCP relay for packets arriving via the MLAG peer-link.<br>This will only be configured on VXLAN VTEPs which are also MLAG devices. |
    | [<samp>&nbsp;&nbsp;suspended_vlans</samp>](## "general_settings.suspended_vlans") | List, items: Dictionary |  |  |  | List of VLANs to create in a suspended state. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;id</samp>](## "general_settings.suspended_vlans.[].id") | Integer | Required, Unique |  | Min: 1<br>Max: 4094 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "general_settings.suspended_vlans.[].name") | String |  |  |  |  |
    | [<samp>hardware_counters</samp>](## "hardware_counters") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;features</samp>](## "hardware_counters.features") | List, items: Dictionary |  |  |  | This data model allows to configure the list of hardware counters feature<br>available on Arista platforms.<br><br>The `name` key accepts a list of valid_values which MUST be updated to support<br>new feature as they are released in EOS.<br><br>The available values of the different keys like 'direction' or 'address_type'<br>are feature and hardware dependent and this model DOES NOT validate that the<br>combinations are valid. It is the responsibility of the user of this data model<br>to make sure that the rendered CLI is accepted by the targeted device.<br><br>Examples:<br><br>  * Use:<br>    ```yaml<br>    hardware_counters:<br>      features:<br>        - name: ip<br>          direction: out<br>          layer3: true<br>          units_packets: true<br>    ```<br><br>    to render:<br>    ```eos<br>    hardware counter feature ip out layer3 units packets<br>    ```<br>  * Use:<br>    ```yaml<br>    hardware_counters:<br>      features:<br>        - name: route<br>          address_type: ipv4<br>          vrf: test<br>          prefix: 192.168.0.0/24<br>    ```<br><br>    to render:<br>    ```eos<br>    hardware counter feature route ipv4 vrf test 192.168.0.0/24<br>    ```<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "hardware_counters.features.[].name") | String | Required |  | Valid Values:<br>- <code>acl</code><br>- <code>decap-group</code><br>- <code>directflow</code><br>- <code>ecn</code><br>- <code>flow-spec</code><br>- <code>gre tunnel interface</code><br>- <code>ip</code><br>- <code>mpls interface</code><br>- <code>mpls lfib</code><br>- <code>mpls tunnel</code><br>- <code>multicast</code><br>- <code>nexthop</code><br>- <code>pbr</code><br>- <code>pdp</code><br>- <code>policing interface</code><br>- <code>qos</code><br>- <code>qos dual-rate-policer</code><br>- <code>route</code><br>- <code>routed-port</code><br>- <code>segment-security</code><br>- <code>subinterface</code><br>- <code>tapagg</code><br>- <code>traffic-class</code><br>- <code>traffic-policy</code><br>- <code>traffic-policy vlan-interface</code><br>- <code>vlan</code><br>- <code>vlan-interface</code><br>- <code>vni decap</code><br>- <code>vni encap</code><br>- <code>vtep decap</code><br>- <code>vtep encap</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction</samp>](## "hardware_counters.features.[].direction") | String |  |  | Valid Values:<br>- <code>in</code><br>- <code>out</code><br>- <code>cpu</code> | Most features support only 'in' and 'out'. Some like traffic-policy support 'cpu'.<br>Some features DO NOT have any direction.<br>This validation IS NOT made by the schemas.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "hardware_counters.features.[].enabled") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;address_type</samp>](## "hardware_counters.features.[].address_type") | String |  |  | Valid Values:<br>- <code>ipv4</code><br>- <code>ipv6</code><br>- <code>mac</code> | Supported only for the following features:<br>- acl: [ipv4, ipv6, mac] if direction is 'out'<br>- multicast: [ipv4, ipv6]<br>- route: [ipv4, ipv6]<br>This validation IS NOT made by the schemas.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;layer3</samp>](## "hardware_counters.features.[].layer3") | Boolean |  |  |  | Supported only for the 'ip' feature.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "hardware_counters.features.[].vrf") | String |  |  |  | Supported only for the 'route' feature.<br>This validation IS NOT made by the schemas.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefix</samp>](## "hardware_counters.features.[].prefix") | String |  |  |  | Supported only for the 'route' feature.<br>Mandatory for the 'route' feature.<br>This validation IS NOT made by the schemas.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;units_packets</samp>](## "hardware_counters.features.[].units_packets") | Boolean |  |  |  |  |
    | [<samp>internal_vlan_order</samp>](## "internal_vlan_order") | Dictionary |  | See (+) on YAML tab |  | Internal vlan allocation order and range. |
    | [<samp>&nbsp;&nbsp;allocation</samp>](## "internal_vlan_order.allocation") | String | Required |  | Valid Values:<br>- <code>ascending</code><br>- <code>descending</code> |  |
    | [<samp>&nbsp;&nbsp;range</samp>](## "internal_vlan_order.range") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;beginning</samp>](## "internal_vlan_order.range.beginning") | Integer | Required |  | Min: 2<br>Max: 4094 | First VLAN ID. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ending</samp>](## "internal_vlan_order.range.ending") | Integer | Required |  | Min: 2<br>Max: 4094 | Last VLAN ID. |
    | [<samp>mac_address_table</samp>](## "mac_address_table") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;aging_time</samp>](## "mac_address_table.aging_time") | Integer |  |  | Min: 0<br>Max: 1000000 | Aging time in seconds 10-1000000.<br>Enter 0 to disable aging.<br> |
    | [<samp>&nbsp;&nbsp;notification_host_flap</samp>](## "mac_address_table.notification_host_flap") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;logging</samp>](## "mac_address_table.notification_host_flap.logging") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;detection</samp>](## "mac_address_table.notification_host_flap.detection") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;window</samp>](## "mac_address_table.notification_host_flap.detection.window") | Integer |  |  | Min: 2<br>Max: 300 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;moves</samp>](## "mac_address_table.notification_host_flap.detection.moves") | Integer |  |  | Min: 2<br>Max: 10 |  |
    | [<samp>&nbsp;&nbsp;static_entries</samp>](## "mac_address_table.static_entries") | List, items: Dictionary |  |  |  | Add static MAC address entries. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;mac_address</samp>](## "mac_address_table.static_entries.[].mac_address") | String | Required |  | Pattern: `[0-9A-Fa-f]{4}\.[0-9A-Fa-f]{4}\.[0-9A-Fa-f]{4}` | The static MAC address to configure.<br>The combination of 'mac_address' and 'vlan' must be unique across all static entries. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vlan</samp>](## "mac_address_table.static_entries.[].vlan") | Integer | Required |  |  | The VLAN ID associated with the MAC address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;drop</samp>](## "mac_address_table.static_entries.[].drop") | Boolean |  |  |  | If true, traffic destined for this MAC address on the specified VLAN will be dropped.<br>This option is mutually exclusive with 'interface' and takes precedence if both are defined. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interface</samp>](## "mac_address_table.static_entries.[].interface") | String |  |  |  | The allowed hardware Ethernet interface, LAG interface, or VXLAN tunnel interface associated with this MAC address and VLAN.<br>This option is mutually exclusive with 'drop'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;eligibility_forwarding</samp>](## "mac_address_table.static_entries.[].eligibility_forwarding") | Boolean |  |  |  | Enable the ability to forward traffic on the specified interface and VLAN for this MAC address.<br>This option is only applicable when 'interface' is defined. |
    | [<samp>redundancy</samp>](## "redundancy") | Dictionary |  |  |  | Redundancy for chassis platforms with dual supervisors | Optional. |
    | [<samp>&nbsp;&nbsp;protocol</samp>](## "redundancy.protocol") | String |  |  | Valid Values:<br>- <code>sso</code><br>- <code>rpr</code> |  |
    | [<samp>serial_number</samp>](## "serial_number") | String |  |  |  | Serial Number of the device.<br>Used for documentation purpose in the fabric documentation as can also be used by the 'cv_deploy' role.<br>"serial_number" can also be set directly under node type settings.<br>If both are set, the value under node type settings takes precedence.<br> |
    | [<samp>system_mac_address</samp>](## "system_mac_address") | String |  |  |  | Set to the same MAC address as available in "show version" on the device.<br>"system_mac_address" can also be set under node type settings.<br>If both are set, the value under node type settings takes precedence.<br> |

=== "YAML"

    ```yaml
    # When set to false, disables IGMP snooping at fabric level and overrides per vlan settings.
    default_igmp_snooping_enabled: <bool; default=True>

    # Default interface MTU configured on EOS under "interface defaults".
    # Can be overridden per platform under platform settings.
    default_interface_mtu: <int; 68-65535>

    # Errdisable settings for the device.
    # Causes are filtered based on platform feature support defined in
    # `platform_settings.feature_support.errdisable_causes.<cause>.detection` and
    # `platform_settings.feature_support.errdisable_causes.<cause>.recovery`.
    errdisable_settings:

      # Interval for all recovery causes in seconds.
      recovery_interval: <int; 30-86400>
      causes:
        acl:
          detection: <bool>
          recovery: <bool>

          # Interval for each recovery cause in seconds.
          recovery_interval: <int; 30-86400>
        arp_inspection:
          detection: <bool>
          recovery: <bool>

          # Interval for each recovery cause in seconds.
          recovery_interval: <int; 30-86400>
        bpduguard:
          recovery: <bool>

          # Interval for each recovery cause in seconds.
          recovery_interval: <int; 30-86400>
        dot1x:
          detection: <bool>
          recovery: <bool>

          # Interval for each recovery cause in seconds.
          recovery_interval: <int; 30-86400>
        dot1x_coa:
          detection: <bool>
          recovery: <bool>

          # Interval for each recovery cause in seconds.
          recovery_interval: <int; 30-86400>
        dot1x_phone_classification:
          detection: <bool>
          recovery: <bool>

          # Interval for each recovery cause in seconds.
          recovery_interval: <int; 30-86400>
        dot1x_session_replace:
          detection: <bool>
          recovery: <bool>

          # Interval for each recovery cause in seconds.
          recovery_interval: <int; 30-86400>
        error_correction_encoding:
          detection: <bool>
          recovery: <bool>

          # Interval for each recovery cause in seconds.
          recovery_interval: <int; 30-86400>
        fabric_capacity_low:
          detection: <bool>
          recovery: <bool>

          # Interval for each recovery cause in seconds.
          recovery_interval: <int; 30-86400>
        hardware_speed_group:
          detection: <bool>
          recovery: <bool>

          # Interval for each recovery cause in seconds.
          recovery_interval: <int; 30-86400>
        hitless_reload_down:
          recovery: <bool>

          # Interval for each recovery cause in seconds.
          recovery_interval: <int; 30-86400>
        interface_speed:
          detection: <bool>
          recovery: <bool>

          # Interval for each recovery cause in seconds.
          recovery_interval: <int; 30-86400>
        internal_error:
          detection: <bool>
          recovery: <bool>

          # Interval for each recovery cause in seconds.
          recovery_interval: <int; 30-86400>
        lacp_rate_limit:
          recovery: <bool>

          # Interval for each recovery cause in seconds.
          recovery_interval: <int; 30-86400>
        link_change:
          detection: <bool>
        link_flap:
          recovery: <bool>

          # Interval for each recovery cause in seconds.
          recovery_interval: <int; 30-86400>
        no_internal_vlan:
          recovery: <bool>

          # Interval for each recovery cause in seconds.
          recovery_interval: <int; 30-86400>
        port_breakout:
          detection: <bool>
          recovery: <bool>

          # Interval for each recovery cause in seconds.
          recovery_interval: <int; 30-86400>
        portchannelguard:
          recovery: <bool>

          # Interval for each recovery cause in seconds.
          recovery_interval: <int; 30-86400>
        portsec:
          recovery: <bool>

          # Interval for each recovery cause in seconds.
          recovery_interval: <int; 30-86400>
        speed_misconfigured:
          recovery: <bool>

          # Interval for each recovery cause in seconds.
          recovery_interval: <int; 30-86400>
        storm_control:
          detection: <bool>
          recovery: <bool>

          # Interval for each recovery cause in seconds.
          recovery_interval: <int; 30-86400>
        stuck_queue:
          recovery: <bool>

          # Interval for each recovery cause in seconds.
          recovery_interval: <int; 30-86400>
        switchcard_unreachable:
          detection: <bool>
          recovery: <bool>

          # Interval for each recovery cause in seconds.
          recovery_interval: <int; 30-86400>
        tap_port_init:
          recovery: <bool>

          # Interval for each recovery cause in seconds.
          recovery_interval: <int; 30-86400>
        tapagg:
          detection: <bool>
          recovery: <bool>

          # Interval for each recovery cause in seconds.
          recovery_interval: <int; 30-86400>
        tpid:
          detection: <bool>
          recovery: <bool>

          # Interval for each recovery cause in seconds.
          recovery_interval: <int; 30-86400>
        transceiver_adapter:
          detection: <bool>
          recovery: <bool>

          # Interval for each recovery cause in seconds.
          recovery_interval: <int; 30-86400>
        uplink_failure_detection:
          recovery: <bool>

          # Interval for each recovery cause in seconds.
          recovery_interval: <int; 30-86400>
        xcvr_misconfigured:
          detection: <bool>
          recovery: <bool>

          # Interval for each recovery cause in seconds.
          recovery_interval: <int; 30-86400>
        xcvr_overheat:
          detection: <bool>
          recovery: <bool>

          # Interval for each recovery cause in seconds.
          recovery_interval: <int; 30-86400>
        xcvr_power_unsupported:
          detection: <bool>
          recovery: <bool>

          # Interval for each recovery cause in seconds.
          recovery_interval: <int; 30-86400>
        xcvr_unsupported:
          recovery: <bool>

          # Interval for each recovery cause in seconds.
          recovery_interval: <int; 30-86400>
    general_settings:
      interface_defaults:

        # Shutdown Ethernet interfaces by default unless they are explicitly enabled.
        ethernet_shutdown: <bool; default=False>
      arp:
        persistent:

          # Restore the ARP cache after reboot.
          enabled: <bool; required>

          # Time to wait in seconds before refreshing the ARP cache after reboot (EOS default 600).
          refresh_delay: <int; 600-3600>
        aging:

          # Timeout in seconds.
          timeout_default: <int; 60-65535>
      ip_icmp_redirect: <bool>
      dhcp_relay:

        # Enables the insertion of DHCP Relay Agent Information (Option 82).
        information_option: <bool; default=False>

        # Blocks DHCP relay for packets received over VXLAN tunnels.
        # This is a VTEP-specific optimization and will only be configured on VXLAN VTEPs.
        tunnel_requests_disabled: <bool; default=False>

        # Blocks DHCP relay for packets arriving via the MLAG peer-link.
        # This will only be configured on VXLAN VTEPs which are also MLAG devices.
        mlag_peerlink_requests_disabled: <bool; default=False>

      # List of VLANs to create in a suspended state.
      suspended_vlans:
        - id: <int; 1-4094; required; unique>
          name: <str>
    hardware_counters:

      # This data model allows to configure the list of hardware counters feature
      # available on Arista platforms.
      #
      # The `name` key accepts a list of valid_values which MUST be updated to support
      # new feature as they are released in EOS.
      #
      # The available values of the different keys like 'direction' or 'address_type'
      # are feature and hardware dependent and this model DOES NOT validate that the
      # combinations are valid. It is the responsibility of the user of this data model
      # to make sure that the rendered CLI is accepted by the targeted device.
      #
      # Examples:
      #
      #   * Use:
      #     ```yaml
      #     hardware_counters:
      #       features:
      #         - name: ip
      #           direction: out
      #           layer3: true
      #           units_packets: true
      #     ```
      #
      #     to render:
      #     ```eos
      #     hardware counter feature ip out layer3 units packets
      #     ```
      #   * Use:
      #     ```yaml
      #     hardware_counters:
      #       features:
      #         - name: route
      #           address_type: ipv4
      #           vrf: test
      #           prefix: 192.168.0.0/24
      #     ```
      #
      #     to render:
      #     ```eos
      #     hardware counter feature route ipv4 vrf test 192.168.0.0/24
      #     ```
      features:
        - name: <str; "acl" | "decap-group" | "directflow" | "ecn" | "flow-spec" | "gre tunnel interface" | "ip" | "mpls interface" | "mpls lfib" | "mpls tunnel" | "multicast" | "nexthop" | "pbr" | "pdp" | "policing interface" | "qos" | "qos dual-rate-policer" | "route" | "routed-port" | "segment-security" | "subinterface" | "tapagg" | "traffic-class" | "traffic-policy" | "traffic-policy vlan-interface" | "vlan" | "vlan-interface" | "vni decap" | "vni encap" | "vtep decap" | "vtep encap"; required>

          # Most features support only 'in' and 'out'. Some like traffic-policy support 'cpu'.
          # Some features DO NOT have any direction.
          # This validation IS NOT made by the schemas.
          direction: <str; "in" | "out" | "cpu">
          enabled: <bool; default=True>

          # Supported only for the following features:
          # - acl: [ipv4, ipv6, mac] if direction is 'out'
          # - multicast: [ipv4, ipv6]
          # - route: [ipv4, ipv6]
          # This validation IS NOT made by the schemas.
          address_type: <str; "ipv4" | "ipv6" | "mac">

          # Supported only for the 'ip' feature.
          layer3: <bool>

          # Supported only for the 'route' feature.
          # This validation IS NOT made by the schemas.
          vrf: <str>

          # Supported only for the 'route' feature.
          # Mandatory for the 'route' feature.
          # This validation IS NOT made by the schemas.
          prefix: <str>
          units_packets: <bool>

    # Internal vlan allocation order and range.
    internal_vlan_order: # (1)!
      allocation: <str; "ascending" | "descending"; required>
      range:

        # First VLAN ID.
        beginning: <int; 2-4094; required>

        # Last VLAN ID.
        ending: <int; 2-4094; required>
    mac_address_table:

      # Aging time in seconds 10-1000000.
      # Enter 0 to disable aging.
      aging_time: <int; 0-1000000>
      notification_host_flap:
        logging: <bool>
        detection:
          window: <int; 2-300>
          moves: <int; 2-10>

      # Add static MAC address entries.
      static_entries:

          # The static MAC address to configure.
          # The combination of 'mac_address' and 'vlan' must be unique across all static entries.
        - mac_address: <str; required>

          # The VLAN ID associated with the MAC address.
          vlan: <int; required>

          # If true, traffic destined for this MAC address on the specified VLAN will be dropped.
          # This option is mutually exclusive with 'interface' and takes precedence if both are defined.
          drop: <bool>

          # The allowed hardware Ethernet interface, LAG interface, or VXLAN tunnel interface associated with this MAC address and VLAN.
          # This option is mutually exclusive with 'drop'.
          interface: <str>

          # Enable the ability to forward traffic on the specified interface and VLAN for this MAC address.
          # This option is only applicable when 'interface' is defined.
          eligibility_forwarding: <bool>

    # Redundancy for chassis platforms with dual supervisors | Optional.
    redundancy:
      protocol: <str; "sso" | "rpr">

    # Serial Number of the device.
    # Used for documentation purpose in the fabric documentation as can also be used by the 'cv_deploy' role.
    # "serial_number" can also be set directly under node type settings.
    # If both are set, the value under node type settings takes precedence.
    serial_number: <str>

    # Set to the same MAC address as available in "show version" on the device.
    # "system_mac_address" can also be set under node type settings.
    # If both are set, the value under node type settings takes precedence.
    system_mac_address: <str>
    ```

    1. Default Value

        ```yaml
        internal_vlan_order:
          allocation: ascending
          range:
            beginning: 1006
            ending: 1199
        ```
