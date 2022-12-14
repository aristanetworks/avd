!!! warning
    This document describes the data model for AVD 4.x. It may or may not work in previous versions.

## Port Profiles

### Description

Optional profiles to share common settings for connected_endpoints and/or network_ports
Keys are the same as used under endpoints adapters. Keys defined under endpoints adapters take precedence.

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>port_profiles</samp>](## "port_profiles") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;- description</samp>](## "port_profiles.[].description") | String |  |  |  | Interface descriptions Description. |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;dot1x</samp>](## "port_profiles.[].dot1x") | Dictionary |  |  |  | 802.1x |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;authentication_failure</samp>](## "port_profiles.[].dot1x.authentication_failure") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "port_profiles.[].dot1x.authentication_failure.action") | String |  |  | Valid Values:<br>- allow<br>- drop |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;allow_vlan</samp>](## "port_profiles.[].dot1x.authentication_failure.allow_vlan") | Integer |  |  | Min: 1<br>Max: 4094 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;host_mode</samp>](## "port_profiles.[].dot1x.host_mode") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "port_profiles.[].dot1x.host_mode.mode") | String |  |  | Valid Values:<br>- multi-host<br>- single-host |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;multi_host_authenticated</samp>](## "port_profiles.[].dot1x.host_mode.multi_host_authenticated") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mac_based_authentication</samp>](## "port_profiles.[].dot1x.mac_based_authentication") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;always</samp>](## "port_profiles.[].dot1x.mac_based_authentication.always") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "port_profiles.[].dot1x.mac_based_authentication.enabled") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;host_mode_common</samp>](## "port_profiles.[].dot1x.mac_based_authentication.host_mode_common") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pae</samp>](## "port_profiles.[].dot1x.pae") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "port_profiles.[].dot1x.pae.mode") | String |  |  | Valid Values:<br>- authenticator |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;port_control</samp>](## "port_profiles.[].dot1x.port_control") | String |  |  | Valid Values:<br>- auto<br>- force-authorized<br>- force-unauthorized |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;port_control_force_authorized_phone</samp>](## "port_profiles.[].dot1x.port_control_force_authorized_phone") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;reauthentication</samp>](## "port_profiles.[].dot1x.reauthentication") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;reauthorization_request_limit</samp>](## "port_profiles.[].dot1x.reauthorization_request_limit") | Integer |  |  | Min: 1<br>Max: 10 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;timeout</samp>](## "port_profiles.[].dot1x.timeout") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;idle_host</samp>](## "port_profiles.[].dot1x.timeout.idle_host") | Integer |  |  | Min: 10<br>Max: 65535 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;quiet_period</samp>](## "port_profiles.[].dot1x.timeout.quiet_period") | Integer |  |  | Min: 1<br>Max: 65535 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;reauth_period</samp>](## "port_profiles.[].dot1x.timeout.reauth_period") | String |  |  |  | Range 60-4294967295 or "server" |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;reauth_timeout_ignore</samp>](## "port_profiles.[].dot1x.timeout.reauth_timeout_ignore") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tx_period</samp>](## "port_profiles.[].dot1x.timeout.tx_period") | Integer |  |  | Min: 1<br>Max: 65535 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "port_profiles.[].enabled") | Boolean |  | True |  | Administrative state, setting to false will set port to 'shutdown' in intended configuration<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;endpoint_ports</samp>](## "port_profiles.[].endpoint_ports") | List, items: String |  |  |  | The lists "endpoint_ports", "switch_ports" and "switches" must have the same length.<br>Each list item is one switchport.<br>Endpoint port(s) is used for description, required unless description is set.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "port_profiles.[].endpoint_ports.[].&lt;str&gt;") | String |  |  |  | Interface name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ethernet_segment</samp>](## "port_profiles.[].ethernet_segment") | Dictionary |  |  |  | Settings for all- or single-active EVPN multihoming |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;designated_forwarder_algorithm</samp>](## "port_profiles.[].ethernet_segment.designated_forwarder_algorithm") | String |  |  | Valid Values:<br>- auto<br>- modulus<br>- preference | Configure DF algorithm and preferences<br>- auto: Use preference-based algorithm and assign preference based on position of device in the 'switches' list<br>   e.g. assuming a list of three switches, this would assign a preference of 200 to the first switch, 100 to the 2nd and 0 to the third<br>- preference: Set preference for each switch manually using designated_forwarder_preferences key<br>- modulus: Use the default modulus-based algorithm<br>If omitted, Port-Channels use the EOS default of modulus<br>If omitted, Ethernet interfaces default to the 'auto' mechanism detailed above<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;designated_forwarder_preferences</samp>](## "port_profiles.[].ethernet_segment.designated_forwarder_preferences") | List, items: String |  |  |  | Manual preference as described above, required only for preference algorithm |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "port_profiles.[].ethernet_segment.designated_forwarder_preferences.[].&lt;str&gt;") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dont_preempt</samp>](## "port_profiles.[].ethernet_segment.dont_preempt") | Boolean |  |  |  | Disable preemption for single-active forwarding when auto/manual DF preference is configured. |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;redundancy</samp>](## "port_profiles.[].ethernet_segment.redundancy") | String |  |  | Valid Values:<br>- all-active<br>- single-active | If omitted, Port-Channels use the EOS default of all-active<br>If omitted, Ethernet interfaces are configured as single-active<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;short_esi</samp>](## "port_profiles.[].ethernet_segment.short_esi") | String | Required |  |  | In format xxxx:xxxx:xxxx or "auto"<br>Define a manual short-esi (be careful using this on profiles) or auto-generate an ESI<br>Please see the notes under "EVPN A/A ESI dual- and single-attached endpoint scenarios" before setting short_esi: auto<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;flowcontrol</samp>](## "port_profiles.[].flowcontrol") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;received</samp>](## "port_profiles.[].flowcontrol.received") | String |  |  | Valid Values:<br>- received<br>- send<br>- on |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;l2_mtu</samp>](## "port_profiles.[].l2_mtu") | Integer |  |  |  | This should only be defined for platforms supporting the "l2 mtu" CLI |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;link_tracking</samp>](## "port_profiles.[].link_tracking") | Dictionary |  |  |  | Configure the downstream interfaces of a respective Link Tracking Group<br>If port_channel is defined in an adapter then port-channel interface is configured to be the downstream<br>else all the ethernet-interfaces will be configured as downstream -> to configure single-active EVPN multihomed networks<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "port_profiles.[].link_tracking.enabled") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "port_profiles.[].link_tracking.name") | String |  |  |  | Tracking group name<br>The default group name is taken from fabric variable of the switch, link_tracking.groups[0].name with default value being "LT_GROUP1".<br>Optional if default link_tracking settings are configured on the node.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "port_profiles.[].mode") | String |  |  | Valid Values:<br>- access<br>- dot1q-tunnel<br>- trunk | Interface mode |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;monitor_sessions</samp>](## "port_profiles.[].monitor_sessions") | List, items: Dictionary |  |  |  | Monitor Session configuration - Use defined switchports as source or destination for monitoring sessions |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "port_profiles.[].monitor_sessions.[].name") | String | Required |  |  | Session name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;role</samp>](## "port_profiles.[].monitor_sessions.[].role") | String |  |  | Valid Values:<br>- source<br>- destination |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;session_settings</samp>](## "port_profiles.[].monitor_sessions.[].session_settings") | Dictionary |  |  |  | Session settings are defined per session name. Different session_settings with for same session name will be combined/merged |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_group</samp>](## "port_profiles.[].monitor_sessions.[].session_settings.access_group") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "port_profiles.[].monitor_sessions.[].session_settings.access_group.name") | String |  |  |  | ACL Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "port_profiles.[].monitor_sessions.[].session_settings.access_group.type") | String |  |  | Valid Values:<br>- ip<br>- ipv6<br>- mac |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;encapsulation_gre_metadata_tx</samp>](## "port_profiles.[].monitor_sessions.[].session_settings.encapsulation_gre_metadata_tx") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;header_remove_size</samp>](## "port_profiles.[].monitor_sessions.[].session_settings.header_remove_size") | Integer |  |  |  | Number of bytes to remove from header |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rate_limit_per_egress_chip</samp>](## "port_profiles.[].monitor_sessions.[].session_settings.rate_limit_per_egress_chip") | String |  |  |  | Ratelimit and unit as string.<br>Examples:<br>  "100000 bps"<br>  "100 kbps"<br>  "10 mbps"<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rate_limit_per_ingress_chip</samp>](## "port_profiles.[].monitor_sessions.[].session_settings.rate_limit_per_ingress_chip") | String |  |  |  | Ratelimit and unit as string.<br>Examples:<br>  "100000 bps"<br>  "100 kbps"<br>  "10 mbps"<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sample</samp>](## "port_profiles.[].monitor_sessions.[].session_settings.sample") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;truncate</samp>](## "port_profiles.[].monitor_sessions.[].session_settings.truncate") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "port_profiles.[].monitor_sessions.[].session_settings.truncate.enabled") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;size</samp>](## "port_profiles.[].monitor_sessions.[].session_settings.truncate.size") | Integer |  |  |  | Size in bytes |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_settings</samp>](## "port_profiles.[].monitor_sessions.[].source_settings") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_group</samp>](## "port_profiles.[].monitor_sessions.[].source_settings.access_group") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "port_profiles.[].monitor_sessions.[].source_settings.access_group.name") | String |  |  |  | ACL Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority</samp>](## "port_profiles.[].monitor_sessions.[].source_settings.access_group.priority") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "port_profiles.[].monitor_sessions.[].source_settings.access_group.type") | String |  |  | Valid Values:<br>- ip<br>- ipv6<br>- mac |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction</samp>](## "port_profiles.[].monitor_sessions.[].source_settings.direction") | String |  |  | Valid Values:<br>- rx<br>- tx<br>- both |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mtu</samp>](## "port_profiles.[].mtu") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;native_vlan</samp>](## "port_profiles.[].native_vlan") | Integer |  |  |  | Native VLAN for a trunk port<br>If setting both native_vlan and native_vlan_tag, native_vlan_tag takes precedence<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;native_vlan_tag</samp>](## "port_profiles.[].native_vlan_tag") | Boolean |  | False |  | If setting both native_vlan and native_vlan_tag, native_vlan_tag takes precedence |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;port_channel</samp>](## "port_profiles.[].port_channel") | Dictionary |  |  |  | Used for port-channel adapter |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;channel_id</samp>](## "port_profiles.[].port_channel.channel_id") | Integer |  |  |  | Port-Channel ID, Optional<br>If no channel_id is specified, an id is generated from the first switch port in the port channel<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "port_profiles.[].port_channel.description") | String |  |  |  | Port-Channel Description - added after endpoint name in the description, Optional |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "port_profiles.[].port_channel.enabled") | Boolean |  | True |  | Port-Channel administrative state, Optional<br>setting to false will set port to 'shutdown' in intended configuration<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;esi</samp>](## "port_profiles.[].port_channel.esi") | String |  |  |  | Format xxxx:xxxx:xxxx |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;lacp_fallback</samp>](## "port_profiles.[].port_channel.lacp_fallback") | Dictionary |  |  |  | LACP Fallback configuration |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "port_profiles.[].port_channel.lacp_fallback.mode") | String |  |  | Valid Values:<br>- static | Currently only static mode is supported |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;timeout</samp>](## "port_profiles.[].port_channel.lacp_fallback.timeout") | Integer |  |  |  | Timeout in seconds, Optional - default is 90 seconds |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "port_profiles.[].port_channel.mode") | String | Required |  | Valid Values:<br>- active<br>- passive<br>- on | Port-Channel Mode |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;short_esi</samp>](## "port_profiles.[].port_channel.short_esi") | String |  |  |  | In format xxxx:xxxx:xxxx or "auto" |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;subinterfaces</samp>](## "port_profiles.[].port_channel.subinterfaces") | List, items: Dictionary |  |  |  | Port-Channel L2 Subinterfaces<br>Subinterfaces are only supported on routed port-channels, which means they cannot be configured on MLAG port-channels.<br>Setting short_esi: auto generates the short_esi automatically using a hash of configuration elements.<br>Please see the notes under "EVPN A/A ESI dual-attached endpoint scenario" before setting short_esi: auto.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- encapsulation_vlan</samp>](## "port_profiles.[].port_channel.subinterfaces.[].encapsulation_vlan") | Dictionary |  |  |  | Client vlan id encapsulation<br>Default is subinterface number<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;client_dot1q</samp>](## "port_profiles.[].port_channel.subinterfaces.[].encapsulation_vlan.client_dot1q") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;number</samp>](## "port_profiles.[].port_channel.subinterfaces.[].number") | Integer |  |  |  | Subinterface number |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;short_esi</samp>](## "port_profiles.[].port_channel.subinterfaces.[].short_esi") | String |  |  |  | In format xxxx:xxxx:xxxx or "auto"<br>Required for multihomed port-channels with subinterfaces<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vlan_id</samp>](## "port_profiles.[].port_channel.subinterfaces.[].vlan_id") | Integer |  |  |  | VLAN ID to bridge<br>Default is subinterface number<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;profile</samp>](## "port_profiles.[].profile") | String | Required, Unique |  |  | Port-profile name, to inherit configuration. |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ptp</samp>](## "port_profiles.[].ptp") | Dictionary |  |  |  | PTP Enable |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enable</samp>](## "port_profiles.[].ptp.enable") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;qos_profile</samp>](## "port_profiles.[].qos_profile") | String |  |  |  | QOS profile name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "port_profiles.[].raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the ethernet interface in the final EOS configuration |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;server_ports</samp>](## "port_profiles.[].server_ports") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "port_profiles.[].server_ports.[].&lt;str&gt;") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;short_esi</samp>](## "port_profiles.[].short_esi") | String |  |  | Valid Values:<br>- auto | Allocates an automatic short_esi to all ports using this profile<br>Please see the notes under "EVPN A/A ESI dual-attached endpoint examples" in this document before setting short_esi: auto.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_bpdufilter</samp>](## "port_profiles.[].spanning_tree_bpdufilter") | String |  |  | Valid Values:<br>- enabled<br>- disabled<br>- True<br>- False |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_bpduguard</samp>](## "port_profiles.[].spanning_tree_bpduguard") | String |  |  | Valid Values:<br>- enabled<br>- disabled<br>- True<br>- False |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_portfast</samp>](## "port_profiles.[].spanning_tree_portfast") | String |  |  | Valid Values:<br>- edge<br>- network |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;speed</samp>](## "port_profiles.[].speed") | String |  |  |  | < interface_speed or forced interface_speed or auto interface_speed ><br>Adapter speed - if not specified will be auto.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;storm_control</samp>](## "port_profiles.[].storm_control") | Dictionary |  |  |  | Storm control settings applied on port toward the endpoint |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;all</samp>](## "port_profiles.[].storm_control.all") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;level</samp>](## "port_profiles.[].storm_control.all.level") | Integer |  |  |  | Configure maximum storm-control level |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unit</samp>](## "port_profiles.[].storm_control.all.unit") | String |  | percent | Valid Values:<br>- percent<br>- pps | Optional var and is hardware dependent |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;broadcast</samp>](## "port_profiles.[].storm_control.broadcast") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;level</samp>](## "port_profiles.[].storm_control.broadcast.level") | Integer |  |  |  | Configure maximum storm-control level |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unit</samp>](## "port_profiles.[].storm_control.broadcast.unit") | String |  | percent | Valid Values:<br>- percent<br>- pps | Optional var and is hardware dependent |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;multicast</samp>](## "port_profiles.[].storm_control.multicast") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;level</samp>](## "port_profiles.[].storm_control.multicast.level") | Integer |  |  |  | Configure maximum storm-control level |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unit</samp>](## "port_profiles.[].storm_control.multicast.unit") | String |  | percent | Valid Values:<br>- percent<br>- pps | Optional var and is hardware dependent |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unknown_unicast</samp>](## "port_profiles.[].storm_control.unknown_unicast") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;level</samp>](## "port_profiles.[].storm_control.unknown_unicast.level") | Integer |  |  |  | Configure maximum storm-control level |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unit</samp>](## "port_profiles.[].storm_control.unknown_unicast.unit") | String |  | percent | Valid Values:<br>- percent<br>- pps | Optional var and is hardware dependentOptional var and is hardware dependent |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;switch_ports</samp>](## "port_profiles.[].switch_ports") | List, items: String | Required |  |  | List of switch interfac(es) |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "port_profiles.[].switch_ports.[].&lt;str&gt;") | String |  |  |  | Switchport interface |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;switches</samp>](## "port_profiles.[].switches") | List, items: String | Required |  |  | List of switch(es) |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "port_profiles.[].switches.[].&lt;str&gt;") | String |  |  |  | Device |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;trunk_groups</samp>](## "port_profiles.[].trunk_groups") | List, items: String |  |  |  | Required with "enable_trunk_groups: true"<br>Trunk Groups are used for limiting vlans on trunk ports to vlans with the same Trunk Group<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "port_profiles.[].trunk_groups.[].&lt;str&gt;") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vlans</samp>](## "port_profiles.[].vlans") | String |  |  |  | Interface vlans - if not set, the EOS default is that all vlans are allowed for trunk ports and vlan 1 will be used for access ports. |

### YAML

```yaml
port_profiles:
  - description: <str>
    dot1x:
      authentication_failure:
        action: <str>
        allow_vlan: <int>
      host_mode:
        mode: <str>
        multi_host_authenticated: <bool>
      mac_based_authentication:
        always: <bool>
        enabled: <bool>
        host_mode_common: <bool>
      pae:
        mode: <str>
      port_control: <str>
      port_control_force_authorized_phone: <bool>
      reauthentication: <bool>
      reauthorization_request_limit: <int>
      timeout:
        idle_host: <int>
        quiet_period: <int>
        reauth_period: <str>
        reauth_timeout_ignore: <bool>
        tx_period: <int>
    enabled: <bool>
    endpoint_ports:
      - <str>
    ethernet_segment:
      designated_forwarder_algorithm: <str>
      designated_forwarder_preferences:
        - <str>
      dont_preempt: <bool>
      redundancy: <str>
      short_esi: <str>
    flowcontrol:
      received: <str>
    l2_mtu: <int>
    link_tracking:
      enabled: <bool>
      name: <str>
    mode: <str>
    monitor_sessions:
      - name: <str>
        role: <str>
        session_settings:
          access_group:
            name: <str>
            type: <str>
          encapsulation_gre_metadata_tx: <bool>
          header_remove_size: <int>
          rate_limit_per_egress_chip: <str>
          rate_limit_per_ingress_chip: <str>
          sample: <int>
          truncate:
            enabled: <bool>
            size: <int>
        source_settings:
          access_group:
            name: <str>
            priority: <int>
            type: <str>
          direction: <str>
    mtu: <int>
    native_vlan: <int>
    native_vlan_tag: <bool>
    port_channel:
      channel_id: <int>
      description: <str>
      enabled: <bool>
      esi: <str>
      lacp_fallback:
        mode: <str>
        timeout: <int>
      mode: <str>
      short_esi: <str>
      subinterfaces:
        - encapsulation_vlan:
            client_dot1q: <int>
          number: <int>
          short_esi: <str>
          vlan_id: <int>
    profile: <str>
    ptp:
      enable: <bool>
    qos_profile: <str>
    raw_eos_cli: <str>
    server_ports:
      - <str>
    short_esi: <str>
    spanning_tree_bpdufilter: <str>
    spanning_tree_bpduguard: <str>
    spanning_tree_portfast: <str>
    speed: <str>
    storm_control:
      all:
        level: <int>
        unit: <str>
      broadcast:
        level: <int>
        unit: <str>
      multicast:
        level: <int>
        unit: <str>
      unknown_unicast:
        level: <int>
        unit: <str>
    switch_ports:
      - <str>
    switches:
      - <str>
    trunk_groups:
      - <str>
    vlans: <str>
```
