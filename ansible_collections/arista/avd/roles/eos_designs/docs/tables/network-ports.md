<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>network_ports</samp>](## "network_ports") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;- switches</samp>](## "network_ports.[].switches") | List, items: String |  |  |  | Regex matching the full hostname of one or more switches.<br>The regular expression must match the full hostname.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "network_ports.[].switches.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;switch_ports</samp>](## "network_ports.[].switch_ports") | List, items: String |  |  |  | List of ranges using AVD range_expand syntax.<br>For example:<br><br>switch_ports:<br>  - Ethernet1<br>  - Ethernet2-48<br><br>All switch_ports ranges are expanded into individual port configurations.<br><br>For more details and examples of the `range_expand` syntax, see the [arista.avd.range_expand documentation](../../../plugins/README.md#range_expand-filter)<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "network_ports.[].switch_ports.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "network_ports.[].description") | String |  |  |  | Description to be used on all ports. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;speed</samp>](## "network_ports.[].speed") | String |  |  |  | Set adapter speed: `< interface_speed >`, `forced < interface_speed >`, `auto < interface_speed >`.<br>If not specified will be auto.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;profile</samp>](## "network_ports.[].profile") | String |  |  |  | Port-profile name to inherit configuration. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "network_ports.[].enabled") | Boolean |  | `True` |  | Administrative state, setting to false will set the port to 'shutdown' in the intended configuration.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "network_ports.[].mode") | String |  |  | Valid Values:<br>- access<br>- dot1q-tunnel<br>- trunk<br>- trunk phone | Interface mode. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mtu</samp>](## "network_ports.[].mtu") | Integer |  |  | Min: 68<br>Max: 65535 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;l2_mtu</samp>](## "network_ports.[].l2_mtu") | Integer |  |  | Min: 68<br>Max: 9416 | This should only be defined for platforms supporting the "l2 mtu" CLI command. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;native_vlan</samp>](## "network_ports.[].native_vlan") | Integer |  |  | Min: 1<br>Max: 4094 | Native VLAN for a trunk port.<br>If both `native_vlan` and `native_vlan_tag`, `native_vlan_tag` takes precedence.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;native_vlan_tag</samp>](## "network_ports.[].native_vlan_tag") | Boolean |  | `False` |  | If both `native_vlan` and `native_vlan_tag`, `native_vlan_tag` takes precedence. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;trunk_groups</samp>](## "network_ports.[].trunk_groups") | List, items: String |  |  |  | Required with `enable_trunk_groups: true`.<br>Trunk Groups are used for limiting VLANs on trunk ports to VLANs with the same Trunk Group.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "network_ports.[].trunk_groups.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vlans</samp>](## "network_ports.[].vlans") | String |  |  |  | Interface VLANs - if not set, the EOS default is that all VLANs are allowed for trunk ports, and VLAN 1 will be used for access ports. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_portfast</samp>](## "network_ports.[].spanning_tree_portfast") | String |  |  | Valid Values:<br>- edge<br>- network |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_bpdufilter</samp>](## "network_ports.[].spanning_tree_bpdufilter") | String |  |  | Valid Values:<br>- enabled<br>- disabled<br>- True<br>- False<br>- true<br>- false |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_bpduguard</samp>](## "network_ports.[].spanning_tree_bpduguard") | String |  |  | Valid Values:<br>- enabled<br>- disabled<br>- True<br>- False<br>- true<br>- false |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;flowcontrol</samp>](## "network_ports.[].flowcontrol") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;received</samp>](## "network_ports.[].flowcontrol.received") | String |  |  | Valid Values:<br>- received<br>- send<br>- on |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;qos_profile</samp>](## "network_ports.[].qos_profile") | String |  |  |  | QOS profile name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ptp</samp>](## "network_ports.[].ptp") | Dictionary |  |  |  | The global PTP profile parameters will be applied to all connected endpoints where `ptp` is manually enabled.<br>`ptp role master` is set to ensure control over the PTP topology.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "network_ports.[].ptp.enabled") | Boolean |  | `False` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;endpoint_role</samp>](## "network_ports.[].ptp.endpoint_role") | String |  | `follower` | Valid Values:<br>- bmca<br>- default<br>- follower |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;profile</samp>](## "network_ports.[].ptp.profile") | String |  | `aes67-r16-2016` | Valid Values:<br>- aes67<br>- aes67-r16-2016<br>- smpte2059-2 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;sflow</samp>](## "network_ports.[].sflow") | Boolean |  |  |  | Configures sFlow on the interface. Overrides `fabric_sflow` setting.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;link_tracking</samp>](## "network_ports.[].link_tracking") | Dictionary |  |  |  | Configure the downstream interfaces of a respective Link Tracking Group.<br>If `port_channel` is defined in an adapter, then the port-channel interface is configured to be the downstream.<br>Else all the ethernet interfaces will be configured as downstream -> to configure single-active EVPN multihomed networks.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "network_ports.[].link_tracking.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "network_ports.[].link_tracking.name") | String |  |  |  | Tracking group name.<br>The default group name is taken from fabric variable of the switch, `link_tracking.groups[0].name` with default value being "LT_GROUP1".<br>Optional if default link_tracking settings are configured on the node.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;dot1x</samp>](## "network_ports.[].dot1x") | Dictionary |  |  |  | 802.1x |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;port_control</samp>](## "network_ports.[].dot1x.port_control") | String |  |  | Valid Values:<br>- auto<br>- force-authorized<br>- force-unauthorized |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;port_control_force_authorized_phone</samp>](## "network_ports.[].dot1x.port_control_force_authorized_phone") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;reauthentication</samp>](## "network_ports.[].dot1x.reauthentication") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pae</samp>](## "network_ports.[].dot1x.pae") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "network_ports.[].dot1x.pae.mode") | String |  |  | Valid Values:<br>- authenticator |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;authentication_failure</samp>](## "network_ports.[].dot1x.authentication_failure") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "network_ports.[].dot1x.authentication_failure.action") | String |  |  | Valid Values:<br>- allow<br>- drop |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;allow_vlan</samp>](## "network_ports.[].dot1x.authentication_failure.allow_vlan") | Integer |  |  | Min: 1<br>Max: 4094 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;host_mode</samp>](## "network_ports.[].dot1x.host_mode") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "network_ports.[].dot1x.host_mode.mode") | String |  |  | Valid Values:<br>- multi-host<br>- single-host |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;multi_host_authenticated</samp>](## "network_ports.[].dot1x.host_mode.multi_host_authenticated") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mac_based_authentication</samp>](## "network_ports.[].dot1x.mac_based_authentication") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "network_ports.[].dot1x.mac_based_authentication.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;always</samp>](## "network_ports.[].dot1x.mac_based_authentication.always") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;host_mode_common</samp>](## "network_ports.[].dot1x.mac_based_authentication.host_mode_common") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;timeout</samp>](## "network_ports.[].dot1x.timeout") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;idle_host</samp>](## "network_ports.[].dot1x.timeout.idle_host") | Integer |  |  | Min: 10<br>Max: 65535 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;quiet_period</samp>](## "network_ports.[].dot1x.timeout.quiet_period") | Integer |  |  | Min: 1<br>Max: 65535 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;reauth_period</samp>](## "network_ports.[].dot1x.timeout.reauth_period") | String |  |  |  | Range 60-4294967295 or "server". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;reauth_timeout_ignore</samp>](## "network_ports.[].dot1x.timeout.reauth_timeout_ignore") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tx_period</samp>](## "network_ports.[].dot1x.timeout.tx_period") | Integer |  |  | Min: 1<br>Max: 65535 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;reauthorization_request_limit</samp>](## "network_ports.[].dot1x.reauthorization_request_limit") | Integer |  |  | Min: 1<br>Max: 10 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;poe</samp>](## "network_ports.[].poe") | Dictionary |  |  |  | Power Over Ethernet settings applied on port. Only configured if platform supports PoE. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;disabled</samp>](## "network_ports.[].poe.disabled") | Boolean |  | `False` |  | Disable PoE on a POE capable port. PoE is enabled on all ports that support it by default in EOS. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority</samp>](## "network_ports.[].poe.priority") | String |  |  | Valid Values:<br>- critical<br>- high<br>- medium<br>- low | Prioritize a port's power in the event that one of the switch's power supplies loses power |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;reboot</samp>](## "network_ports.[].poe.reboot") | Dictionary |  |  |  | Set the PoE power behavior for a PoE port when the system is rebooted |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "network_ports.[].poe.reboot.action") | String |  |  | Valid Values:<br>- maintain<br>- power-off | PoE action for interface |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;link_down</samp>](## "network_ports.[].poe.link_down") | Dictionary |  |  |  | Set the PoE power behavior for a PoE port when the port goes down |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "network_ports.[].poe.link_down.action") | String |  |  | Valid Values:<br>- maintain<br>- power-off | PoE action for interface |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;power_off_delay</samp>](## "network_ports.[].poe.link_down.power_off_delay") | Integer |  |  | Min: 1<br>Max: 86400 | Number of seconds to delay shutting the power off after a link down event occurs. Default value is 5 seconds in EOS. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;shutdown</samp>](## "network_ports.[].poe.shutdown") | Dictionary |  |  |  | Set the PoE power behavior for a PoE port when the port is admin down |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "network_ports.[].poe.shutdown.action") | String |  |  | Valid Values:<br>- maintain<br>- power-off | PoE action for interface |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;limit</samp>](## "network_ports.[].poe.limit") | Dictionary |  |  |  | Override the hardware-negotiated power limit using either wattage or a power class. Note that if using a power class, AVD will automatically convert the class value to the wattage value corresponding to that power class. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;class</samp>](## "network_ports.[].poe.limit.class") | Integer |  |  | Min: 0<br>Max: 8 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;watts</samp>](## "network_ports.[].poe.limit.watts") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;fixed</samp>](## "network_ports.[].poe.limit.fixed") | Boolean |  |  |  | Set to ignore hardware classification |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;negotiation_lldp</samp>](## "network_ports.[].poe.negotiation_lldp") | Boolean |  |  |  | Disable to prevent port from negotiating power with powered devices over LLDP. Enabled by default in EOS. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;legacy_detect</samp>](## "network_ports.[].poe.legacy_detect") | Boolean |  |  |  | Allow a subset of legacy devices to work with the PoE switch. Disabled by default in EOS because it can cause false positive detections. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;storm_control</samp>](## "network_ports.[].storm_control") | Dictionary |  |  |  | Storm control settings applied on port toward the endpoint. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;all</samp>](## "network_ports.[].storm_control.all") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;level</samp>](## "network_ports.[].storm_control.all.level") | String |  |  |  | Configure maximum storm-control level. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unit</samp>](## "network_ports.[].storm_control.all.unit") | String |  | `percent` | Valid Values:<br>- percent<br>- pps | Optional variable and is hardware dependent. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;broadcast</samp>](## "network_ports.[].storm_control.broadcast") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;level</samp>](## "network_ports.[].storm_control.broadcast.level") | String |  |  |  | Configure maximum storm-control level. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unit</samp>](## "network_ports.[].storm_control.broadcast.unit") | String |  | `percent` | Valid Values:<br>- percent<br>- pps | Optional variable and is hardware dependent. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;multicast</samp>](## "network_ports.[].storm_control.multicast") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;level</samp>](## "network_ports.[].storm_control.multicast.level") | String |  |  |  | Configure maximum storm-control level. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unit</samp>](## "network_ports.[].storm_control.multicast.unit") | String |  | `percent` | Valid Values:<br>- percent<br>- pps | Optional variable and is hardware dependent. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unknown_unicast</samp>](## "network_ports.[].storm_control.unknown_unicast") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;level</samp>](## "network_ports.[].storm_control.unknown_unicast.level") | String |  |  |  | Configure maximum storm-control level. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unit</samp>](## "network_ports.[].storm_control.unknown_unicast.unit") | String |  | `percent` | Valid Values:<br>- percent<br>- pps | Optional variable and is hardware dependent. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;monitor_sessions</samp>](## "network_ports.[].monitor_sessions") | List, items: Dictionary |  |  |  | Used to define switchports as source or destination for monitoring sessions. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "network_ports.[].monitor_sessions.[].name") | String | Required |  |  | Session name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;role</samp>](## "network_ports.[].monitor_sessions.[].role") | String |  |  | Valid Values:<br>- source<br>- destination |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_settings</samp>](## "network_ports.[].monitor_sessions.[].source_settings") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction</samp>](## "network_ports.[].monitor_sessions.[].source_settings.direction") | String |  |  | Valid Values:<br>- rx<br>- tx<br>- both |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_group</samp>](## "network_ports.[].monitor_sessions.[].source_settings.access_group") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "network_ports.[].monitor_sessions.[].source_settings.access_group.type") | String |  |  | Valid Values:<br>- ip<br>- ipv6<br>- mac |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "network_ports.[].monitor_sessions.[].source_settings.access_group.name") | String |  |  |  | ACL name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority</samp>](## "network_ports.[].monitor_sessions.[].source_settings.access_group.priority") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;session_settings</samp>](## "network_ports.[].monitor_sessions.[].session_settings") | Dictionary |  |  |  | Session settings are defined per session name.<br>Different session_settings for the same session name will be combined/merged.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;encapsulation_gre_metadata_tx</samp>](## "network_ports.[].monitor_sessions.[].session_settings.encapsulation_gre_metadata_tx") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;header_remove_size</samp>](## "network_ports.[].monitor_sessions.[].session_settings.header_remove_size") | Integer |  |  |  | Number of bytes to remove from header. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_group</samp>](## "network_ports.[].monitor_sessions.[].session_settings.access_group") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "network_ports.[].monitor_sessions.[].session_settings.access_group.type") | String |  |  | Valid Values:<br>- ip<br>- ipv6<br>- mac |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "network_ports.[].monitor_sessions.[].session_settings.access_group.name") | String |  |  |  | ACL name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rate_limit_per_ingress_chip</samp>](## "network_ports.[].monitor_sessions.[].session_settings.rate_limit_per_ingress_chip") | String |  |  |  | Ratelimit and unit as string.<br>Examples:<br>  "100000 bps"<br>  "100 kbps"<br>  "10 mbps"<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rate_limit_per_egress_chip</samp>](## "network_ports.[].monitor_sessions.[].session_settings.rate_limit_per_egress_chip") | String |  |  |  | Ratelimit and unit as string.<br>Examples:<br>  "100000 bps"<br>  "100 kbps"<br>  "10 mbps"<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sample</samp>](## "network_ports.[].monitor_sessions.[].session_settings.sample") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;truncate</samp>](## "network_ports.[].monitor_sessions.[].session_settings.truncate") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "network_ports.[].monitor_sessions.[].session_settings.truncate.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;size</samp>](## "network_ports.[].monitor_sessions.[].session_settings.truncate.size") | Integer |  |  |  | Size in bytes |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ethernet_segment</samp>](## "network_ports.[].ethernet_segment") | Dictionary |  |  |  | Settings for all or single-active EVPN multihoming. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;short_esi</samp>](## "network_ports.[].ethernet_segment.short_esi") | String | Required |  |  | In format xxxx:xxxx:xxxx or "auto".<br>Define a manual short-esi (be careful using this on profiles) or set the value to "auto" to automatically generate the value.<br>Please see the notes under "EVPN A/A ESI dual and single-attached endpoint scenarios" before setting `short_esi: auto`.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;redundancy</samp>](## "network_ports.[].ethernet_segment.redundancy") | String |  |  | Valid Values:<br>- all-active<br>- single-active | If omitted, Port-Channels use the EOS default of all-active.<br>If omitted, Ethernet interfaces are configured as single-active.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;designated_forwarder_algorithm</samp>](## "network_ports.[].ethernet_segment.designated_forwarder_algorithm") | String |  |  | Valid Values:<br>- auto<br>- modulus<br>- preference | Configure DF algorithm and preferences.<br>- auto: Use preference-based algorithm and assign preference based on position of device in the 'switches' list,<br>  e.g., assuming a list of three switches, this would assign a preference of 200 to the first switch, 100 to the 2nd, and 0 to the third.<br>- preference: Set preference for each switch manually using designated_forwarder_preferences key.<br>- modulus: Use the default modulus-based algorithm.<br>If omitted, Port-Channels use the EOS default of modulus.<br>If omitted, Ethernet interfaces default to the 'auto' mechanism detailed above.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;designated_forwarder_preferences</samp>](## "network_ports.[].ethernet_segment.designated_forwarder_preferences") | List, items: String |  |  |  | Manual preference as described above, required only for preference algorithm. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "network_ports.[].ethernet_segment.designated_forwarder_preferences.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dont_preempt</samp>](## "network_ports.[].ethernet_segment.dont_preempt") | Boolean |  |  |  | Disable preemption for single-active forwarding when auto/manual DF preference is configured. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;port_channel</samp>](## "network_ports.[].port_channel") | Dictionary |  |  |  | Used for port-channel adapter. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "network_ports.[].port_channel.mode") | String |  |  | Valid Values:<br>- active<br>- passive<br>- on | Port-Channel Mode. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;channel_id</samp>](## "network_ports.[].port_channel.channel_id") | Integer |  |  |  | Port-Channel ID.<br>If no channel_id is specified, an id is generated from the first switch port in the port channel.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "network_ports.[].port_channel.description") | String |  |  |  | By default the description is built leveraging `<peer>` name or `adapter.description` when defined.<br>When this key is defined, it will append its content to the physical port description.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "network_ports.[].port_channel.enabled") | Boolean |  | `True` |  | Port-Channel administrative state.<br>Setting to false will set port to 'shutdown' in intended configuration.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;esi</samp>](## "network_ports.[].port_channel.esi") <span style="color:red">removed</span> | String |  |  |  | Format xxxx:xxxx:xxxx.<span style="color:red">This key was removed. Support was removed in AVD version 4.0.0. Use <samp>short_esi</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;short_esi</samp>](## "network_ports.[].port_channel.short_esi") <span style="color:red">deprecated</span> | String |  |  |  | In format xxxx:xxxx:xxxx or "auto".<span style="color:red">This key is deprecated. Support will be removed in AVD version 5.0.0. Use <samp>ethernet_segment.short_esi</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;lacp_fallback</samp>](## "network_ports.[].port_channel.lacp_fallback") | Dictionary |  |  |  | LACP fallback configuration. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "network_ports.[].port_channel.lacp_fallback.mode") | String |  |  | Valid Values:<br>- static | Currently only static mode is supported. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;timeout</samp>](## "network_ports.[].port_channel.lacp_fallback.timeout") | Integer |  |  |  | Timeout in seconds. EOS default is 90 seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;lacp_timer</samp>](## "network_ports.[].port_channel.lacp_timer") | Dictionary |  |  |  | LACP timer configuration. Applies only when Port-channel mode is not "on". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "network_ports.[].port_channel.lacp_timer.mode") | String |  |  | Valid Values:<br>- normal<br>- fast | LACP mode for interface members. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;multiplier</samp>](## "network_ports.[].port_channel.lacp_timer.multiplier") | Integer |  |  |  | Number of LACP BPDUs lost before deeming the peer down. EOS default is 3. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;subinterfaces</samp>](## "network_ports.[].port_channel.subinterfaces") | List, items: Dictionary |  |  |  | Port-Channel L2 Subinterfaces<br>Subinterfaces are only supported on routed port-channels, which means they cannot be configured on MLAG port-channels.<br>Setting short_esi: auto generates the short_esi automatically using a hash of configuration elements.<br>Please see the notes under "EVPN A/A ESI dual-attached endpoint scenario" before setting short_esi: auto.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- number</samp>](## "network_ports.[].port_channel.subinterfaces.[].number") | Integer |  |  |  | Subinterface number |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;short_esi</samp>](## "network_ports.[].port_channel.subinterfaces.[].short_esi") | String |  |  |  | In format xxxx:xxxx:xxxx or "auto"<br>Required for multihomed port-channels with subinterfaces<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vlan_id</samp>](## "network_ports.[].port_channel.subinterfaces.[].vlan_id") | Integer |  |  | Min: 1<br>Max: 4094 | VLAN ID to bridge.<br>Default is subinterface number.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;encapsulation_vlan</samp>](## "network_ports.[].port_channel.subinterfaces.[].encapsulation_vlan") | Dictionary |  |  |  | Client VLAN ID encapsulation.<br>Default is subinterface number.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;client_dot1q</samp>](## "network_ports.[].port_channel.subinterfaces.[].encapsulation_vlan.client_dot1q") | Integer |  |  | Min: 1<br>Max: 4094 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "network_ports.[].port_channel.raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the port-channel interface in the final EOS configuration. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "network_ports.[].port_channel.structured_config") | Dictionary |  |  |  | Custom structured config added under port_channel_interfaces.[name=<interface>] for eos_cli_config_gen. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "network_ports.[].raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the ethernet interface in the final EOS configuration. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "network_ports.[].structured_config") | Dictionary |  |  |  | Custom structured config added under ethernet_interfaces.[name=<interface>] for eos_cli_config_gen. |

=== "YAML"

    ```yaml
    network_ports:
      - switches:
          - <str>
        switch_ports:
          - <str>
        description: <str>
        speed: <str>
        profile: <str>
        enabled: <bool>
        mode: <str>
        mtu: <int>
        l2_mtu: <int>
        native_vlan: <int>
        native_vlan_tag: <bool>
        trunk_groups:
          - <str>
        vlans: <str>
        spanning_tree_portfast: <str>
        spanning_tree_bpdufilter: <str>
        spanning_tree_bpduguard: <str>
        flowcontrol:
          received: <str>
        qos_profile: <str>
        ptp:
          enabled: <bool>
          endpoint_role: <str>
          profile: <str>
        sflow: <bool>
        link_tracking:
          enabled: <bool>
          name: <str>
        dot1x:
          port_control: <str>
          port_control_force_authorized_phone: <bool>
          reauthentication: <bool>
          pae:
            mode: <str>
          authentication_failure:
            action: <str>
            allow_vlan: <int>
          host_mode:
            mode: <str>
            multi_host_authenticated: <bool>
          mac_based_authentication:
            enabled: <bool>
            always: <bool>
            host_mode_common: <bool>
          timeout:
            idle_host: <int>
            quiet_period: <int>
            reauth_period: <str>
            reauth_timeout_ignore: <bool>
            tx_period: <int>
          reauthorization_request_limit: <int>
        poe:
          disabled: <bool>
          priority: <str>
          reboot:
            action: <str>
          link_down:
            action: <str>
            power_off_delay: <int>
          shutdown:
            action: <str>
          limit:
            class: <int>
            watts: <str>
            fixed: <bool>
          negotiation_lldp: <bool>
          legacy_detect: <bool>
        storm_control:
          all:
            level: <str>
            unit: <str>
          broadcast:
            level: <str>
            unit: <str>
          multicast:
            level: <str>
            unit: <str>
          unknown_unicast:
            level: <str>
            unit: <str>
        monitor_sessions:
          - name: <str>
            role: <str>
            source_settings:
              direction: <str>
              access_group:
                type: <str>
                name: <str>
                priority: <int>
            session_settings:
              encapsulation_gre_metadata_tx: <bool>
              header_remove_size: <int>
              access_group:
                type: <str>
                name: <str>
              rate_limit_per_ingress_chip: <str>
              rate_limit_per_egress_chip: <str>
              sample: <int>
              truncate:
                enabled: <bool>
                size: <int>
        ethernet_segment:
          short_esi: <str>
          redundancy: <str>
          designated_forwarder_algorithm: <str>
          designated_forwarder_preferences:
            - <str>
          dont_preempt: <bool>
        port_channel:
          mode: <str>
          channel_id: <int>
          description: <str>
          enabled: <bool>
          short_esi: <str>
          lacp_fallback:
            mode: <str>
            timeout: <int>
          lacp_timer:
            mode: <str>
            multiplier: <int>
          subinterfaces:
            - number: <int>
              short_esi: <str>
              vlan_id: <int>
              encapsulation_vlan:
                client_dot1q: <int>
          raw_eos_cli: <str>
          structured_config: <dict>
        raw_eos_cli: <str>
        structured_config: <dict>
    ```
