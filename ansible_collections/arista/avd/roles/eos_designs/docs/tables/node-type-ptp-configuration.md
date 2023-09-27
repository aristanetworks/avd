<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>&lt;node_type_keys.key&gt;</samp>](## "&lt;node_type_keys.key&gt;") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;defaults</samp>](## "&lt;node_type_keys.key&gt;.defaults") | Dictionary |  |  |  | Define variables for all nodes of this type. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ptp</samp>](## "&lt;node_type_keys.key&gt;.defaults.ptp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;node_type_keys.key&gt;.defaults.ptp.enabled") | Boolean |  | `False` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;profile</samp>](## "&lt;node_type_keys.key&gt;.defaults.ptp.profile") | String |  | `aes67-r16-2016` | Valid Values:<br>- aes67<br>- smpte2059-2<br>- aes67-r16-2016 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;domain</samp>](## "&lt;node_type_keys.key&gt;.defaults.ptp.domain") | Integer |  | `127` | Min: 0<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority1</samp>](## "&lt;node_type_keys.key&gt;.defaults.ptp.priority1") | Integer |  |  | Min: 0<br>Max: 255 | default -> automatically set based on node_type.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority2</samp>](## "&lt;node_type_keys.key&gt;.defaults.ptp.priority2") | Integer |  |  | Min: 0<br>Max: 255 | default -> (node_id modulus 256).<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;auto_clock_identity</samp>](## "&lt;node_type_keys.key&gt;.defaults.ptp.auto_clock_identity") | Boolean |  | `True` |  | If you prefer to have PTP clock identity be the system MAC-address of the switch, which is the default EOS behaviour, simply disable the automatic PTP clock identity.<br>default -> (clock_identity_prefix = 00:1C:73 (default)) + (PTP priority 1 as HEX) + ":00:" + (PTP priority 2 as HEX).<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;clock_identity_prefix</samp>](## "&lt;node_type_keys.key&gt;.defaults.ptp.clock_identity_prefix") | String |  |  |  | PTP clock idetentiy 3-byte prefix. i.e. "01:02:03".<br>By default the 3-byte prefix is "00:1C:73".<br>This can be overridden if auto_clock_identity is set to true (which is the default).<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;clock_identity</samp>](## "&lt;node_type_keys.key&gt;.defaults.ptp.clock_identity") | String |  |  |  | Set PTP clock identity manually. 6-byte value i.e. "01:02:03:04:05:06".<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_ip</samp>](## "&lt;node_type_keys.key&gt;.defaults.ptp.source_ip") | String |  |  |  | By default in EOS, PTP packets are sourced with an IP address from the routed port or from the relevant SVI, which is the recommended behaviour.<br>This can be set manually if required, for example, to a value of "10.1.2.3".<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ttl</samp>](## "&lt;node_type_keys.key&gt;.defaults.ptp.ttl") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;forward_unicast</samp>](## "&lt;node_type_keys.key&gt;.defaults.ptp.forward_unicast") | Boolean |  | `False` |  | Enable PTP unicast forwarding.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dscp</samp>](## "&lt;node_type_keys.key&gt;.defaults.ptp.dscp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;general_messages</samp>](## "&lt;node_type_keys.key&gt;.defaults.ptp.dscp.general_messages") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;event_messages</samp>](## "&lt;node_type_keys.key&gt;.defaults.ptp.dscp.event_messages") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;monitor</samp>](## "&lt;node_type_keys.key&gt;.defaults.ptp.monitor") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;node_type_keys.key&gt;.defaults.ptp.monitor.enabled") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;threshold</samp>](## "&lt;node_type_keys.key&gt;.defaults.ptp.monitor.threshold") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;offset_from_master</samp>](## "&lt;node_type_keys.key&gt;.defaults.ptp.monitor.threshold.offset_from_master") | Integer |  | `250` | Min: 0<br>Max: 1000000000 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mean_path_delay</samp>](## "&lt;node_type_keys.key&gt;.defaults.ptp.monitor.threshold.mean_path_delay") | Integer |  | `1500` | Min: 0<br>Max: 1000000000 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;drop</samp>](## "&lt;node_type_keys.key&gt;.defaults.ptp.monitor.threshold.drop") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;offset_from_master</samp>](## "&lt;node_type_keys.key&gt;.defaults.ptp.monitor.threshold.drop.offset_from_master") | Integer |  |  | Min: 0<br>Max: 1000000000 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mean_path_delay</samp>](## "&lt;node_type_keys.key&gt;.defaults.ptp.monitor.threshold.drop.mean_path_delay") | Integer |  |  | Min: 0<br>Max: 1000000000 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;missing_message</samp>](## "&lt;node_type_keys.key&gt;.defaults.ptp.monitor.missing_message") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;intervals</samp>](## "&lt;node_type_keys.key&gt;.defaults.ptp.monitor.missing_message.intervals") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;announce</samp>](## "&lt;node_type_keys.key&gt;.defaults.ptp.monitor.missing_message.intervals.announce") | Integer |  |  | Min: 2<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;follow_up</samp>](## "&lt;node_type_keys.key&gt;.defaults.ptp.monitor.missing_message.intervals.follow_up") | Integer |  |  | Min: 2<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sync</samp>](## "&lt;node_type_keys.key&gt;.defaults.ptp.monitor.missing_message.intervals.sync") | Integer |  |  | Min: 2<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sequence_ids</samp>](## "&lt;node_type_keys.key&gt;.defaults.ptp.monitor.missing_message.sequence_ids") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;node_type_keys.key&gt;.defaults.ptp.monitor.missing_message.sequence_ids.enabled") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;announce</samp>](## "&lt;node_type_keys.key&gt;.defaults.ptp.monitor.missing_message.sequence_ids.announce") | Integer |  | `3` | Min: 2<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;delay_resp</samp>](## "&lt;node_type_keys.key&gt;.defaults.ptp.monitor.missing_message.sequence_ids.delay_resp") | Integer |  | `3` | Min: 2<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;follow_up</samp>](## "&lt;node_type_keys.key&gt;.defaults.ptp.monitor.missing_message.sequence_ids.follow_up") | Integer |  | `3` | Min: 2<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sync</samp>](## "&lt;node_type_keys.key&gt;.defaults.ptp.monitor.missing_message.sequence_ids.sync") | Integer |  | `3` | Min: 2<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;node_groups</samp>](## "&lt;node_type_keys.key&gt;.node_groups") | List, items: Dictionary |  |  |  | Define variables related to all nodes part of this group. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- group</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].group") | String | Required, Unique |  |  | The Node Group Name is used for MLAG domain unless set with 'mlag_domain_id'.<br>The Node Group Name is also used for peer description on downstream switches' uplinks.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes") | List, items: Dictionary |  |  |  | Define variables per node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].name") | String | Required, Unique |  |  | The Node Name is used as "hostname". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ptp</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ptp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ptp.enabled") | Boolean |  | `False` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;profile</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ptp.profile") | String |  | `aes67-r16-2016` | Valid Values:<br>- aes67<br>- smpte2059-2<br>- aes67-r16-2016 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;domain</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ptp.domain") | Integer |  | `127` | Min: 0<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority1</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ptp.priority1") | Integer |  |  | Min: 0<br>Max: 255 | default -> automatically set based on node_type.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority2</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ptp.priority2") | Integer |  |  | Min: 0<br>Max: 255 | default -> (node_id modulus 256).<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;auto_clock_identity</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ptp.auto_clock_identity") | Boolean |  | `True` |  | If you prefer to have PTP clock identity be the system MAC-address of the switch, which is the default EOS behaviour, simply disable the automatic PTP clock identity.<br>default -> (clock_identity_prefix = 00:1C:73 (default)) + (PTP priority 1 as HEX) + ":00:" + (PTP priority 2 as HEX).<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;clock_identity_prefix</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ptp.clock_identity_prefix") | String |  |  |  | PTP clock idetentiy 3-byte prefix. i.e. "01:02:03".<br>By default the 3-byte prefix is "00:1C:73".<br>This can be overridden if auto_clock_identity is set to true (which is the default).<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;clock_identity</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ptp.clock_identity") | String |  |  |  | Set PTP clock identity manually. 6-byte value i.e. "01:02:03:04:05:06".<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_ip</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ptp.source_ip") | String |  |  |  | By default in EOS, PTP packets are sourced with an IP address from the routed port or from the relevant SVI, which is the recommended behaviour.<br>This can be set manually if required, for example, to a value of "10.1.2.3".<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ttl</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ptp.ttl") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;forward_unicast</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ptp.forward_unicast") | Boolean |  | `False` |  | Enable PTP unicast forwarding.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dscp</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ptp.dscp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;general_messages</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ptp.dscp.general_messages") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;event_messages</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ptp.dscp.event_messages") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;monitor</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ptp.monitor") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ptp.monitor.enabled") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;threshold</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ptp.monitor.threshold") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;offset_from_master</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ptp.monitor.threshold.offset_from_master") | Integer |  | `250` | Min: 0<br>Max: 1000000000 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mean_path_delay</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ptp.monitor.threshold.mean_path_delay") | Integer |  | `1500` | Min: 0<br>Max: 1000000000 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;drop</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ptp.monitor.threshold.drop") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;offset_from_master</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ptp.monitor.threshold.drop.offset_from_master") | Integer |  |  | Min: 0<br>Max: 1000000000 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mean_path_delay</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ptp.monitor.threshold.drop.mean_path_delay") | Integer |  |  | Min: 0<br>Max: 1000000000 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;missing_message</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ptp.monitor.missing_message") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;intervals</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ptp.monitor.missing_message.intervals") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;announce</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ptp.monitor.missing_message.intervals.announce") | Integer |  |  | Min: 2<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;follow_up</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ptp.monitor.missing_message.intervals.follow_up") | Integer |  |  | Min: 2<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sync</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ptp.monitor.missing_message.intervals.sync") | Integer |  |  | Min: 2<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sequence_ids</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ptp.monitor.missing_message.sequence_ids") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ptp.monitor.missing_message.sequence_ids.enabled") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;announce</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ptp.monitor.missing_message.sequence_ids.announce") | Integer |  | `3` | Min: 2<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;delay_resp</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ptp.monitor.missing_message.sequence_ids.delay_resp") | Integer |  | `3` | Min: 2<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;follow_up</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ptp.monitor.missing_message.sequence_ids.follow_up") | Integer |  | `3` | Min: 2<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sync</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ptp.monitor.missing_message.sequence_ids.sync") | Integer |  | `3` | Min: 2<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ptp</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ptp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ptp.enabled") | Boolean |  | `False` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;profile</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ptp.profile") | String |  | `aes67-r16-2016` | Valid Values:<br>- aes67<br>- smpte2059-2<br>- aes67-r16-2016 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;domain</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ptp.domain") | Integer |  | `127` | Min: 0<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority1</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ptp.priority1") | Integer |  |  | Min: 0<br>Max: 255 | default -> automatically set based on node_type.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority2</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ptp.priority2") | Integer |  |  | Min: 0<br>Max: 255 | default -> (node_id modulus 256).<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;auto_clock_identity</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ptp.auto_clock_identity") | Boolean |  | `True` |  | If you prefer to have PTP clock identity be the system MAC-address of the switch, which is the default EOS behaviour, simply disable the automatic PTP clock identity.<br>default -> (clock_identity_prefix = 00:1C:73 (default)) + (PTP priority 1 as HEX) + ":00:" + (PTP priority 2 as HEX).<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;clock_identity_prefix</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ptp.clock_identity_prefix") | String |  |  |  | PTP clock idetentiy 3-byte prefix. i.e. "01:02:03".<br>By default the 3-byte prefix is "00:1C:73".<br>This can be overridden if auto_clock_identity is set to true (which is the default).<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;clock_identity</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ptp.clock_identity") | String |  |  |  | Set PTP clock identity manually. 6-byte value i.e. "01:02:03:04:05:06".<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_ip</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ptp.source_ip") | String |  |  |  | By default in EOS, PTP packets are sourced with an IP address from the routed port or from the relevant SVI, which is the recommended behaviour.<br>This can be set manually if required, for example, to a value of "10.1.2.3".<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ttl</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ptp.ttl") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;forward_unicast</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ptp.forward_unicast") | Boolean |  | `False` |  | Enable PTP unicast forwarding.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dscp</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ptp.dscp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;general_messages</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ptp.dscp.general_messages") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;event_messages</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ptp.dscp.event_messages") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;monitor</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ptp.monitor") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ptp.monitor.enabled") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;threshold</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ptp.monitor.threshold") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;offset_from_master</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ptp.monitor.threshold.offset_from_master") | Integer |  | `250` | Min: 0<br>Max: 1000000000 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mean_path_delay</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ptp.monitor.threshold.mean_path_delay") | Integer |  | `1500` | Min: 0<br>Max: 1000000000 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;drop</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ptp.monitor.threshold.drop") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;offset_from_master</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ptp.monitor.threshold.drop.offset_from_master") | Integer |  |  | Min: 0<br>Max: 1000000000 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mean_path_delay</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ptp.monitor.threshold.drop.mean_path_delay") | Integer |  |  | Min: 0<br>Max: 1000000000 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;missing_message</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ptp.monitor.missing_message") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;intervals</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ptp.monitor.missing_message.intervals") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;announce</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ptp.monitor.missing_message.intervals.announce") | Integer |  |  | Min: 2<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;follow_up</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ptp.monitor.missing_message.intervals.follow_up") | Integer |  |  | Min: 2<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sync</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ptp.monitor.missing_message.intervals.sync") | Integer |  |  | Min: 2<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sequence_ids</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ptp.monitor.missing_message.sequence_ids") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ptp.monitor.missing_message.sequence_ids.enabled") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;announce</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ptp.monitor.missing_message.sequence_ids.announce") | Integer |  | `3` | Min: 2<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;delay_resp</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ptp.monitor.missing_message.sequence_ids.delay_resp") | Integer |  | `3` | Min: 2<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;follow_up</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ptp.monitor.missing_message.sequence_ids.follow_up") | Integer |  | `3` | Min: 2<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sync</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ptp.monitor.missing_message.sequence_ids.sync") | Integer |  | `3` | Min: 2<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;nodes</samp>](## "&lt;node_type_keys.key&gt;.nodes") | List, items: Dictionary |  |  |  | Define variables per node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].name") | String | Required, Unique |  |  | The Node Name is used as "hostname". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ptp</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ptp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ptp.enabled") | Boolean |  | `False` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;profile</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ptp.profile") | String |  | `aes67-r16-2016` | Valid Values:<br>- aes67<br>- smpte2059-2<br>- aes67-r16-2016 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;domain</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ptp.domain") | Integer |  | `127` | Min: 0<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority1</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ptp.priority1") | Integer |  |  | Min: 0<br>Max: 255 | default -> automatically set based on node_type.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority2</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ptp.priority2") | Integer |  |  | Min: 0<br>Max: 255 | default -> (node_id modulus 256).<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;auto_clock_identity</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ptp.auto_clock_identity") | Boolean |  | `True` |  | If you prefer to have PTP clock identity be the system MAC-address of the switch, which is the default EOS behaviour, simply disable the automatic PTP clock identity.<br>default -> (clock_identity_prefix = 00:1C:73 (default)) + (PTP priority 1 as HEX) + ":00:" + (PTP priority 2 as HEX).<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;clock_identity_prefix</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ptp.clock_identity_prefix") | String |  |  |  | PTP clock idetentiy 3-byte prefix. i.e. "01:02:03".<br>By default the 3-byte prefix is "00:1C:73".<br>This can be overridden if auto_clock_identity is set to true (which is the default).<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;clock_identity</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ptp.clock_identity") | String |  |  |  | Set PTP clock identity manually. 6-byte value i.e. "01:02:03:04:05:06".<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_ip</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ptp.source_ip") | String |  |  |  | By default in EOS, PTP packets are sourced with an IP address from the routed port or from the relevant SVI, which is the recommended behaviour.<br>This can be set manually if required, for example, to a value of "10.1.2.3".<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ttl</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ptp.ttl") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;forward_unicast</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ptp.forward_unicast") | Boolean |  | `False` |  | Enable PTP unicast forwarding.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dscp</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ptp.dscp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;general_messages</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ptp.dscp.general_messages") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;event_messages</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ptp.dscp.event_messages") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;monitor</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ptp.monitor") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ptp.monitor.enabled") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;threshold</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ptp.monitor.threshold") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;offset_from_master</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ptp.monitor.threshold.offset_from_master") | Integer |  | `250` | Min: 0<br>Max: 1000000000 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mean_path_delay</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ptp.monitor.threshold.mean_path_delay") | Integer |  | `1500` | Min: 0<br>Max: 1000000000 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;drop</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ptp.monitor.threshold.drop") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;offset_from_master</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ptp.monitor.threshold.drop.offset_from_master") | Integer |  |  | Min: 0<br>Max: 1000000000 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mean_path_delay</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ptp.monitor.threshold.drop.mean_path_delay") | Integer |  |  | Min: 0<br>Max: 1000000000 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;missing_message</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ptp.monitor.missing_message") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;intervals</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ptp.monitor.missing_message.intervals") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;announce</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ptp.monitor.missing_message.intervals.announce") | Integer |  |  | Min: 2<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;follow_up</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ptp.monitor.missing_message.intervals.follow_up") | Integer |  |  | Min: 2<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sync</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ptp.monitor.missing_message.intervals.sync") | Integer |  |  | Min: 2<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sequence_ids</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ptp.monitor.missing_message.sequence_ids") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ptp.monitor.missing_message.sequence_ids.enabled") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;announce</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ptp.monitor.missing_message.sequence_ids.announce") | Integer |  | `3` | Min: 2<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;delay_resp</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ptp.monitor.missing_message.sequence_ids.delay_resp") | Integer |  | `3` | Min: 2<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;follow_up</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ptp.monitor.missing_message.sequence_ids.follow_up") | Integer |  | `3` | Min: 2<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sync</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ptp.monitor.missing_message.sequence_ids.sync") | Integer |  | `3` | Min: 2<br>Max: 255 |  |

=== "YAML"

    ```yaml
    <node_type_keys.key>:
      defaults:
        ptp:
          enabled: <bool>
          profile: <str>
          domain: <int>
          priority1: <int>
          priority2: <int>
          auto_clock_identity: <bool>
          clock_identity_prefix: <str>
          clock_identity: <str>
          source_ip: <str>
          ttl: <int>
          forward_unicast: <bool>
          dscp:
            general_messages: <int>
            event_messages: <int>
          monitor:
            enabled: <bool>
            threshold:
              offset_from_master: <int>
              mean_path_delay: <int>
              drop:
                offset_from_master: <int>
                mean_path_delay: <int>
            missing_message:
              intervals:
                announce: <int>
                follow_up: <int>
                sync: <int>
              sequence_ids:
                enabled: <bool>
                announce: <int>
                delay_resp: <int>
                follow_up: <int>
                sync: <int>
      node_groups:
        - group: <str>
          nodes:
            - name: <str>
              ptp:
                enabled: <bool>
                profile: <str>
                domain: <int>
                priority1: <int>
                priority2: <int>
                auto_clock_identity: <bool>
                clock_identity_prefix: <str>
                clock_identity: <str>
                source_ip: <str>
                ttl: <int>
                forward_unicast: <bool>
                dscp:
                  general_messages: <int>
                  event_messages: <int>
                monitor:
                  enabled: <bool>
                  threshold:
                    offset_from_master: <int>
                    mean_path_delay: <int>
                    drop:
                      offset_from_master: <int>
                      mean_path_delay: <int>
                  missing_message:
                    intervals:
                      announce: <int>
                      follow_up: <int>
                      sync: <int>
                    sequence_ids:
                      enabled: <bool>
                      announce: <int>
                      delay_resp: <int>
                      follow_up: <int>
                      sync: <int>
          ptp:
            enabled: <bool>
            profile: <str>
            domain: <int>
            priority1: <int>
            priority2: <int>
            auto_clock_identity: <bool>
            clock_identity_prefix: <str>
            clock_identity: <str>
            source_ip: <str>
            ttl: <int>
            forward_unicast: <bool>
            dscp:
              general_messages: <int>
              event_messages: <int>
            monitor:
              enabled: <bool>
              threshold:
                offset_from_master: <int>
                mean_path_delay: <int>
                drop:
                  offset_from_master: <int>
                  mean_path_delay: <int>
              missing_message:
                intervals:
                  announce: <int>
                  follow_up: <int>
                  sync: <int>
                sequence_ids:
                  enabled: <bool>
                  announce: <int>
                  delay_resp: <int>
                  follow_up: <int>
                  sync: <int>
      nodes:
        - name: <str>
          ptp:
            enabled: <bool>
            profile: <str>
            domain: <int>
            priority1: <int>
            priority2: <int>
            auto_clock_identity: <bool>
            clock_identity_prefix: <str>
            clock_identity: <str>
            source_ip: <str>
            ttl: <int>
            forward_unicast: <bool>
            dscp:
              general_messages: <int>
              event_messages: <int>
            monitor:
              enabled: <bool>
              threshold:
                offset_from_master: <int>
                mean_path_delay: <int>
                drop:
                  offset_from_master: <int>
                  mean_path_delay: <int>
              missing_message:
                intervals:
                  announce: <int>
                  follow_up: <int>
                  sync: <int>
                sequence_ids:
                  enabled: <bool>
                  announce: <int>
                  delay_resp: <int>
                  follow_up: <int>
                  sync: <int>
    ```
