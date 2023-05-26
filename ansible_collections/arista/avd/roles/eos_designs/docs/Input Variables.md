---
search:
  boost: 2
---

# Input Variables

## <Connected Endpoints Keys.Key>

This should be applied to group_vars or host_vars where endpoints are connecting.
`connected_endpoints_keys.key` is one of the keys under "connected_endpoints_keys".
The default keys are `servers`, `firewalls`, `routers`, `load_balancers`, and `storage_arrays`.

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>&lt;connected_endpoints_keys.key&gt;</samp>](## "&lt;connected_endpoints_keys.key&gt;") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;- name</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].name") | String | Required, Unique |  |  | Endpoint name will be used in the switchport description. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;rack</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].rack") | String |  |  |  | Rack is used for documentation purposes only. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;adapters</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters") | List, items: Dictionary |  |  |  | A list of adapters, group by adapters leveraging the same port-profile. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- switch_ports</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].switch_ports") | List, items: String | Required |  |  | List of switch interfaces.<br>The lists `endpoint_ports`, `switch_ports`, and `switches` must have the same length.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].switch_ports.[].&lt;str&gt;") | String |  |  |  | Switchport interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;switches</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].switches") | List, items: String | Required |  |  | List of switches.<br>The lists `endpoint_ports`, `switch_ports`, and `switches` must have the same length.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].switches.[].&lt;str&gt;") | String |  |  |  | Device |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;server_ports</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].server_ports") <span style="color:red">removed</span> | List, items: String |  |  |  | <span style="color:red">This key was removed. Support was removed in AVD version 4.0.0. Use <samp>endpoint_ports</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].server_ports.[].&lt;str&gt;") | String |  |  |  | Used for documentation purposes |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;endpoint_ports</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].endpoint_ports") | List, items: String |  |  |  | Endpoint ports is used for description, required unless description is set.<br>The lists `endpoint_ports`, `switch_ports`, and `switches` must have the same length.<br>Each list item is one switchport.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].endpoint_ports.[].&lt;str&gt;") | String |  |  |  | Interface name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;speed</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].speed") | String |  |  |  | Set adapter speed: `< interface_speed >`, `forced < interface_speed >`, `auto < interface_speed >`.<br>If not specified will be auto.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].description") | String |  |  |  | By default the description is built leveraging `<peer>_<peer_interface>`.<br>When set this key will overide the default value on the physical ports.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;profile</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].profile") | String |  |  |  | Port-profile name to inherit configuration. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].enabled") | Boolean |  | True |  | Administrative state, setting to false will set the port to 'shutdown' in the intended configuration.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].mode") | String |  |  | Valid Values:<br>- access<br>- dot1q-tunnel<br>- trunk<br>- trunk phone | Interface mode. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mtu</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].mtu") | Integer |  |  | Min: 68<br>Max: 65535 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;l2_mtu</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].l2_mtu") | Integer |  |  | Min: 68<br>Max: 9416 | This should only be defined for platforms supporting the "l2 mtu" CLI command. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;native_vlan</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].native_vlan") | Integer |  |  | Min: 1<br>Max: 4094 | Native VLAN for a trunk port.<br>If both `native_vlan` and `native_vlan_tag`, `native_vlan_tag` takes precedence.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;native_vlan_tag</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].native_vlan_tag") | Boolean |  | False |  | If both `native_vlan` and `native_vlan_tag`, `native_vlan_tag` takes precedence. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;trunk_groups</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].trunk_groups") | List, items: String |  |  |  | Required with `enable_trunk_groups: true`.<br>Trunk Groups are used for limiting VLANs on trunk ports to VLANs with the same Trunk Group.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].trunk_groups.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vlans</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].vlans") | String |  |  |  | Interface VLANs - if not set, the EOS default is that all VLANs are allowed for trunk ports, and VLAN 1 will be used for access ports. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_portfast</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].spanning_tree_portfast") | String |  |  | Valid Values:<br>- edge<br>- network |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_bpdufilter</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].spanning_tree_bpdufilter") | String |  |  | Valid Values:<br>- enabled<br>- disabled<br>- True<br>- False<br>- true<br>- false |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_bpduguard</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].spanning_tree_bpduguard") | String |  |  | Valid Values:<br>- enabled<br>- disabled<br>- True<br>- False<br>- true<br>- false |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;flowcontrol</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].flowcontrol") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;received</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].flowcontrol.received") | String |  |  | Valid Values:<br>- received<br>- send<br>- on |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;qos_profile</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].qos_profile") | String |  |  |  | QOS profile name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ptp</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].ptp") | Dictionary |  |  |  | The global PTP profile parameters will be applied to all connected endpoints where `ptp` is manually enabled.<br>`ptp role master` is set to ensure control over the PTP topology.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].ptp.enabled") | Boolean |  | False |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;endpoint_role</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].ptp.endpoint_role") | String |  | follower | Valid Values:<br>- bmca<br>- default<br>- follower |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;profile</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].ptp.profile") | String |  | aes67-r16-2016 | Valid Values:<br>- aes67<br>- aes67-r16-2016<br>- smpte2059-2 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;link_tracking</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].link_tracking") | Dictionary |  |  |  | Configure the downstream interfaces of a respective Link Tracking Group.<br>If `port_channel` is defined in an adapter, then the port-channel interface is configured to be the downstream.<br>Else all the ethernet interfaces will be configured as downstream -> to configure single-active EVPN multihomed networks.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].link_tracking.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].link_tracking.name") | String |  |  |  | Tracking group name.<br>The default group name is taken from fabric variable of the switch, `link_tracking.groups[0].name` with default value being "LT_GROUP1".<br>Optional if default link_tracking settings are configured on the node.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dot1x</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].dot1x") | Dictionary |  |  |  | 802.1x |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;port_control</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].dot1x.port_control") | String |  |  | Valid Values:<br>- auto<br>- force-authorized<br>- force-unauthorized |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;port_control_force_authorized_phone</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].dot1x.port_control_force_authorized_phone") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;reauthentication</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].dot1x.reauthentication") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pae</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].dot1x.pae") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].dot1x.pae.mode") | String |  |  | Valid Values:<br>- authenticator |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;authentication_failure</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].dot1x.authentication_failure") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].dot1x.authentication_failure.action") | String |  |  | Valid Values:<br>- allow<br>- drop |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;allow_vlan</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].dot1x.authentication_failure.allow_vlan") | Integer |  |  | Min: 1<br>Max: 4094 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;host_mode</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].dot1x.host_mode") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].dot1x.host_mode.mode") | String |  |  | Valid Values:<br>- multi-host<br>- single-host |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;multi_host_authenticated</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].dot1x.host_mode.multi_host_authenticated") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mac_based_authentication</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].dot1x.mac_based_authentication") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].dot1x.mac_based_authentication.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;always</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].dot1x.mac_based_authentication.always") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;host_mode_common</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].dot1x.mac_based_authentication.host_mode_common") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;timeout</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].dot1x.timeout") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;idle_host</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].dot1x.timeout.idle_host") | Integer |  |  | Min: 10<br>Max: 65535 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;quiet_period</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].dot1x.timeout.quiet_period") | Integer |  |  | Min: 1<br>Max: 65535 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;reauth_period</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].dot1x.timeout.reauth_period") | String |  |  |  | Range 60-4294967295 or "server". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;reauth_timeout_ignore</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].dot1x.timeout.reauth_timeout_ignore") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tx_period</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].dot1x.timeout.tx_period") | Integer |  |  | Min: 1<br>Max: 65535 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;reauthorization_request_limit</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].dot1x.reauthorization_request_limit") | Integer |  |  | Min: 1<br>Max: 10 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;storm_control</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].storm_control") | Dictionary |  |  |  | Storm control settings applied on port toward the endpoint. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;all</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].storm_control.all") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;level</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].storm_control.all.level") | Integer |  |  |  | Configure maximum storm-control level. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unit</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].storm_control.all.unit") | String |  | percent | Valid Values:<br>- percent<br>- pps | Optional variable and is hardware dependent. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;broadcast</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].storm_control.broadcast") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;level</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].storm_control.broadcast.level") | Integer |  |  |  | Configure maximum storm-control level. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unit</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].storm_control.broadcast.unit") | String |  | percent | Valid Values:<br>- percent<br>- pps | Optional variable and is hardware dependent. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;multicast</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].storm_control.multicast") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;level</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].storm_control.multicast.level") | Integer |  |  |  | Configure maximum storm-control level. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unit</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].storm_control.multicast.unit") | String |  | percent | Valid Values:<br>- percent<br>- pps | Optional variable and is hardware dependent. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unknown_unicast</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].storm_control.unknown_unicast") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;level</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].storm_control.unknown_unicast.level") | Integer |  |  |  | Configure maximum storm-control level. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unit</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].storm_control.unknown_unicast.unit") | String |  | percent | Valid Values:<br>- percent<br>- pps | Optional variable and is hardware dependent. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;monitor_sessions</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].monitor_sessions") | List, items: Dictionary |  |  |  | Used to define switchports as source or destination for monitoring sessions. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].monitor_sessions.[].name") | String | Required |  |  | Session name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;role</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].monitor_sessions.[].role") | String |  |  | Valid Values:<br>- source<br>- destination |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_settings</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].monitor_sessions.[].source_settings") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].monitor_sessions.[].source_settings.direction") | String |  |  | Valid Values:<br>- rx<br>- tx<br>- both |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_group</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].monitor_sessions.[].source_settings.access_group") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].monitor_sessions.[].source_settings.access_group.type") | String |  |  | Valid Values:<br>- ip<br>- ipv6<br>- mac |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].monitor_sessions.[].source_settings.access_group.name") | String |  |  |  | ACL name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].monitor_sessions.[].source_settings.access_group.priority") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;session_settings</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].monitor_sessions.[].session_settings") | Dictionary |  |  |  | Session settings are defined per session name.<br>Different session_settings for the same session name will be combined/merged.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;encapsulation_gre_metadata_tx</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].monitor_sessions.[].session_settings.encapsulation_gre_metadata_tx") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;header_remove_size</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].monitor_sessions.[].session_settings.header_remove_size") | Integer |  |  |  | Number of bytes to remove from header. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_group</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].monitor_sessions.[].session_settings.access_group") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].monitor_sessions.[].session_settings.access_group.type") | String |  |  | Valid Values:<br>- ip<br>- ipv6<br>- mac |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].monitor_sessions.[].session_settings.access_group.name") | String |  |  |  | ACL name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rate_limit_per_ingress_chip</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].monitor_sessions.[].session_settings.rate_limit_per_ingress_chip") | String |  |  |  | Ratelimit and unit as string.<br>Examples:<br>  "100000 bps"<br>  "100 kbps"<br>  "10 mbps"<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rate_limit_per_egress_chip</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].monitor_sessions.[].session_settings.rate_limit_per_egress_chip") | String |  |  |  | Ratelimit and unit as string.<br>Examples:<br>  "100000 bps"<br>  "100 kbps"<br>  "10 mbps"<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sample</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].monitor_sessions.[].session_settings.sample") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;truncate</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].monitor_sessions.[].session_settings.truncate") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].monitor_sessions.[].session_settings.truncate.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;size</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].monitor_sessions.[].session_settings.truncate.size") | Integer |  |  |  | Size in bytes |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ethernet_segment</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].ethernet_segment") | Dictionary |  |  |  | Settings for all or single-active EVPN multihoming. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;short_esi</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].ethernet_segment.short_esi") | String | Required |  |  | In format xxxx:xxxx:xxxx or "auto".<br>Define a manual short-esi (be careful using this on profiles) or set the value to "auto" to automatically generate the value.<br>Please see the notes under "EVPN A/A ESI dual and single-attached endpoint scenarios" before setting `short_esi: auto`.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;redundancy</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].ethernet_segment.redundancy") | String |  |  | Valid Values:<br>- all-active<br>- single-active | If omitted, Port-Channels use the EOS default of all-active.<br>If omitted, Ethernet interfaces are configured as single-active.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;designated_forwarder_algorithm</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].ethernet_segment.designated_forwarder_algorithm") | String |  |  | Valid Values:<br>- auto<br>- modulus<br>- preference | Configure DF algorithm and preferences.<br>- auto: Use preference-based algorithm and assign preference based on position of device in the 'switches' list,<br>  e.g., assuming a list of three switches, this would assign a preference of 200 to the first switch, 100 to the 2nd, and 0 to the third.<br>- preference: Set preference for each switch manually using designated_forwarder_preferences key.<br>- modulus: Use the default modulus-based algorithm.<br>If omitted, Port-Channels use the EOS default of modulus.<br>If omitted, Ethernet interfaces default to the 'auto' mechanism detailed above.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;designated_forwarder_preferences</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].ethernet_segment.designated_forwarder_preferences") | List, items: String |  |  |  | Manual preference as described above, required only for preference algorithm. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].ethernet_segment.designated_forwarder_preferences.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dont_preempt</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].ethernet_segment.dont_preempt") | Boolean |  |  |  | Disable preemption for single-active forwarding when auto/manual DF preference is configured. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;port_channel</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].port_channel") | Dictionary |  |  |  | Used for port-channel adapter. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].port_channel.mode") | String |  |  | Valid Values:<br>- active<br>- passive<br>- on | Port-Channel Mode. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;channel_id</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].port_channel.channel_id") | Integer |  |  |  | Port-Channel ID.<br>If no channel_id is specified, an id is generated from the first switch port in the port channel.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].port_channel.description") | String |  |  |  | By default the description is built leveraging `<peer>` name or `adapter.description` when defined.<br>When this key is defined, it will append its content to the physical port description.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].port_channel.enabled") | Boolean |  | True |  | Port-Channel administrative state.<br>Setting to false will set port to 'shutdown' in intended configuration.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;esi</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].port_channel.esi") <span style="color:red">removed</span> | String |  |  |  | Format xxxx:xxxx:xxxx.<span style="color:red">This key was removed. Support was removed in AVD version 4.0.0. Use <samp>short_esi</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;short_esi</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].port_channel.short_esi") | String |  |  |  | In format xxxx:xxxx:xxxx or "auto". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;lacp_fallback</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].port_channel.lacp_fallback") | Dictionary |  |  |  | LACP fallback configuration. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].port_channel.lacp_fallback.mode") | String |  |  | Valid Values:<br>- static | Currently only static mode is supported. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;timeout</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].port_channel.lacp_fallback.timeout") | Integer |  |  |  | Timeout in seconds. EOS default is 90 seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;lacp_timer</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].port_channel.lacp_timer") | Dictionary |  |  |  | LACP timer configuration. Applies only when Port-channel mode is not "on". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].port_channel.lacp_timer.mode") | String |  |  | Valid Values:<br>- normal<br>- fast | LACP mode for interface members. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;multiplier</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].port_channel.lacp_timer.multiplier") | Integer |  |  |  | Number of LACP BPDUs lost before deeming the peer down. EOS default is 3. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;subinterfaces</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].port_channel.subinterfaces") | List, items: Dictionary |  |  |  | Port-Channel L2 Subinterfaces<br>Subinterfaces are only supported on routed port-channels, which means they cannot be configured on MLAG port-channels.<br>Setting short_esi: auto generates the short_esi automatically using a hash of configuration elements.<br>Please see the notes under "EVPN A/A ESI dual-attached endpoint scenario" before setting short_esi: auto.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- number</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].port_channel.subinterfaces.[].number") | Integer |  |  |  | Subinterface number |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;short_esi</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].port_channel.subinterfaces.[].short_esi") | String |  |  |  | In format xxxx:xxxx:xxxx or "auto"<br>Required for multihomed port-channels with subinterfaces<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vlan_id</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].port_channel.subinterfaces.[].vlan_id") | Integer |  |  | Min: 1<br>Max: 4094 | VLAN ID to bridge.<br>Default is subinterface number.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;encapsulation_vlan</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].port_channel.subinterfaces.[].encapsulation_vlan") | Dictionary |  |  |  | Client VLAN ID encapsulation.<br>Default is subinterface number.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;client_dot1q</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].port_channel.subinterfaces.[].encapsulation_vlan.client_dot1q") | Integer |  |  | Min: 1<br>Max: 4094 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].port_channel.raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the port-channel interface in the final EOS configuration. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].port_channel.structured_config") | Dictionary |  |  |  | Custom structured config added under port_channel_interfaces.<interface> for eos_cli_config_gen. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the ethernet interface in the final EOS configuration. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].structured_config") | Dictionary |  |  |  | Custom structured config added under ethernet_interfaces.<interface> for eos_cli_config_gen. |

=== "YAML"

    ```yaml
    <connected_endpoints_keys.key>:
      - name: <str>
        rack: <str>
        adapters:
          - switch_ports:
              - <str>
            switches:
              - <str>
            endpoint_ports:
              - <str>
            speed: <str>
            description: <str>
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

## <Network Services Keys.Name>

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>&lt;network_services_keys.name&gt;</samp>](## "&lt;network_services_keys.name&gt;") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;- name</samp>](## "&lt;network_services_keys.name&gt;.[].name") | String | Required, Unique |  |  | Specify a tenant name.<br>Tenant provide a construct to group L3 VRFs and L2 VLANs.<br>Networks services can be filtered by tenant name.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mac_vrf_vni_base</samp>](## "&lt;network_services_keys.name&gt;.[].mac_vrf_vni_base") | Integer |  |  | Min: 0<br>Max: 16770000 | Base number for MAC VRF VXLAN Network Identifier (required with VXLAN).<br>VXLAN VNI is derived from the base number with simple addition.<br>i.e. mac_vrf_vni_base = 10000, svi 100 = VNI 10100, svi 300 = VNI 10300.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mac_vrf_id_base</samp>](## "&lt;network_services_keys.name&gt;.[].mac_vrf_id_base") | Integer |  |  | Min: 0<br>Max: 16770000 | If not set, "mac_vrf_vni_base" will be used.<br>Base number for MAC VRF RD/RT ID (Required unless mac_vrf_vni_base is set)<br>ID is derived from the base number with simple addition.<br>i.e. mac_vrf_id_base = 10000, svi 100 = RD/RT 10100, svi 300 = RD/RT 10300.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vlan_aware_bundle_number_base</samp>](## "&lt;network_services_keys.name&gt;.[].vlan_aware_bundle_number_base") | Integer |  | 0 |  | Base number for VLAN aware bundle RD/RT.<br>The "Assigned Number" part of RD/RT is derived from vrf_vni + vlan_aware_bundle_number_base.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;pseudowire_rt_base</samp>](## "&lt;network_services_keys.name&gt;.[].pseudowire_rt_base") | Integer |  |  |  | Pseudowire RT base, used to generate route targets for VPWS services.<br>Avoid overlapping route target spaces between different services.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;enable_mlag_ibgp_peering_vrfs</samp>](## "&lt;network_services_keys.name&gt;.[].enable_mlag_ibgp_peering_vrfs") | Boolean |  |  |  | MLAG iBGP peering per VRF.<br>By default an iBGP peering is configured per VRF between MLAG peers on separate VLANs.<br>Setting enable_mlag_ibgp_peering_vrfs: false under tenant will change this default to prevent configuration of these peerings and VLANs for all VRFs in the tenant.<br>This setting can be overridden per VRF.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;bgp_peer_groups</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups") | List, items: Dictionary |  |  |  | List of BGP peer groups definitions.<br>This will configure BGP peer groups to be used inside the tenant VRF for peering with external devices.<br>Since BGP peer groups are configured at higher BGP level, shared between VRFs,<br>peer_group names should not overlap between VRFs.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups.[].name") | String | Required, Unique |  |  | BGP peer group name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups.[].nodes") | List, items: String |  |  |  | Nodes is required to restrict configuration of BGP neighbors to certain nodes in the network.<br>If not set the peer-group is created on devices which have a bgp_peer mapped to the corresponding peer_group.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups.[].nodes.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups.[].type") | String |  |  |  | Key only used for documentation or validation purposes |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remote_as</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups.[].remote_as") | String |  |  |  | BGP AS <1-4294967295> or AS number in asdot notation <1-65535>.<0-65535> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;local_as</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups.[].local_as") | String |  |  |  | BGP AS <1-4294967295> or AS number in asdot notation <1-65535>.<0-65535> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups.[].description") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;shutdown</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups.[].shutdown") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;as_path</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups.[].as_path") | Dictionary |  |  |  | BGP AS-PATH options |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remote_as_replace_out</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups.[].as_path.remote_as_replace_out") | Boolean |  |  |  | Replace AS number with local AS number |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prepend_own_disabled</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups.[].as_path.prepend_own_disabled") | Boolean |  |  |  | Disable prepending own AS number to AS path |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remove_private_as</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups.[].remove_private_as") | Dictionary |  |  |  | Remove private AS numbers in outbound AS path |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups.[].remove_private_as.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;all</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups.[].remove_private_as.all") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;replace_as</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups.[].remove_private_as.replace_as") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remove_private_as_ingress</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups.[].remove_private_as_ingress") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups.[].remove_private_as_ingress.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;replace_as</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups.[].remove_private_as_ingress.replace_as") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer_filter</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups.[].peer_filter") | String |  |  |  | Peer-filter name<br>note: `bgp_listen_range_prefix` and `peer_filter` will be deprecated in AVD v4.0<br>These should not be mixed with the new `listen_ranges` key above to avoid conflicts.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;next_hop_unchanged</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups.[].next_hop_unchanged") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;update_source</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups.[].update_source") | String |  |  |  | IP address or interface name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_reflector_client</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups.[].route_reflector_client") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bfd</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups.[].bfd") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ebgp_multihop</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups.[].ebgp_multihop") | Integer |  |  | Min: 1<br>Max: 255 | Time-to-live in range of hops |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;next_hop_self</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups.[].next_hop_self") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;password</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups.[].password") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;passive</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups.[].passive") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default_originate</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups.[].default_originate") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups.[].default_originate.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;always</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups.[].default_originate.always") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups.[].default_originate.route_map") | String |  |  |  | Route-map name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;send_community</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups.[].send_community") | String |  |  |  | 'all' or a combination of 'standard', 'extended', 'large' and 'link-bandwidth (w/options)' |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maximum_routes</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups.[].maximum_routes") | Integer |  |  | Min: 0<br>Max: 4294967294 | Maximum number of routes (0 means unlimited) |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maximum_routes_warning_limit</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups.[].maximum_routes_warning_limit") | String |  |  |  | Maximum number of routes after which a warning is issued (0 means never warn) or<br>Percentage of maximum number of routes at which to warn ("<1-100> percent")<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maximum_routes_warning_only</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups.[].maximum_routes_warning_only") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;link_bandwidth</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups.[].link_bandwidth") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups.[].link_bandwidth.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups.[].link_bandwidth.default") | String |  |  |  | nn.nn(K|M|G) link speed in bits/second |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;allowas_in</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups.[].allowas_in") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups.[].allowas_in.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;times</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups.[].allowas_in.times") | Integer |  |  | Min: 1<br>Max: 10 | Number of local ASNs allowed in a BGP update |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;weight</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups.[].weight") | Integer |  |  | Min: 0<br>Max: 65535 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;timers</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups.[].timers") | String |  |  |  | BGP Keepalive and Hold Timer values in seconds as string "<0-3600> <0-3600>" |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rib_in_pre_policy_retain</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups.[].rib_in_pre_policy_retain") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups.[].rib_in_pre_policy_retain.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;all</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups.[].rib_in_pre_policy_retain.all") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_in</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups.[].route_map_in") | String |  |  |  | Inbound route-map name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_out</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups.[].route_map_out") | String |  |  |  | Outbound route-map name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp_listen_range_prefix</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups.[].bgp_listen_range_prefix") | String |  |  |  | IP prefix range<br>note: `bgp_listen_range_prefix` and `peer_filter` will be deprecated in AVD v4.0<br>These should not be mixed with the new `listen_ranges` key above to avoid conflicts.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;session_tracker</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups.[].session_tracker") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;evpn_l2_multicast</samp>](## "&lt;network_services_keys.name&gt;.[].evpn_l2_multicast") | Dictionary |  |  |  | Enable EVPN L2 Multicast for all SVIs and l2vlans within Tenant.<br>- Multicast group binding is created only for Multicast traffic. BULL traffic will use ingress-replication<br>- Configures binding between VXLAN, VLAN, and multicast group IPv4 address using the following formula:<br>  < evpn_l2_multicast.underlay_l2_multicast_group_ipv4_pool > + < vlan_id - 1 > + < evpn_l2_multicast.underlay_l2_multicast_group_ipv4_pool_offset >.<br>- The recommendation is to assign a /20 block within the 232.0.0.0/8 Source-Specific Multicast range.<br>- Enables `redistribute igmp` on the router bgp MAC VRF.<br>- When evpn_l2_multicast.enabled is true for a VLAN or a tenant, "igmp snooping" and "igmp snooping querier" will always be enabled - overriding those individual settings.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;network_services_keys.name&gt;.[].evpn_l2_multicast.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;underlay_l2_multicast_group_ipv4_pool</samp>](## "&lt;network_services_keys.name&gt;.[].evpn_l2_multicast.underlay_l2_multicast_group_ipv4_pool") | String |  |  |  | IPv4_address/Mask |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;underlay_l2_multicast_group_ipv4_pool_offset</samp>](## "&lt;network_services_keys.name&gt;.[].evpn_l2_multicast.underlay_l2_multicast_group_ipv4_pool_offset") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;evpn_l3_multicast</samp>](## "&lt;network_services_keys.name&gt;.[].evpn_l3_multicast") | Dictionary |  |  |  | Enable L3 Multicast for all SVIs and l3vlans within Tenant.<br>- In the evpn-l3ls design type, this enables L3 EVPN Multicast (aka OISM)<br>- Multicast group binding for VRF is created only for Multicast traffic. BULL traffic will use ingress-replication<br>- Configures binding between VXLAN, VLAN, and multicast group IPv4 address using the following formula:<br>  < l3_multicast.evpn_underlay_l3_multicast_group_ipv4_pool > + < vrf_vni - 1 > + < l3_multicast.evpn_underlay_l3_multicast_group_ipv4_pool_offset >.<br>- The recommendation is to assign a /20 block within the 232.0.0.0/8 Source-Specific Multicast range.<br>- If enabled on an SVI using the anycast default gateway feature, a diagnostic loopback (see below) MUST be configured to source IGMP traffic.<br>- Enables `evpn multicast` on the router bgp VRF.<br>- When enabled on an SVI:<br>     - If switch is part of an MLAG pair, enables "pim ipv4 sparse-mode" on the SVI.<br>     - If switch is standalone or A-A MH, enables "ip igmp" on the SVI.<br>     - If "ip address virtual" is configured, enables "pim ipv4 local-interface" and uses the diagnostic Loopback defined in the VRF<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;network_services_keys.name&gt;.[].evpn_l3_multicast.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_underlay_l3_multicast_group_ipv4_pool</samp>](## "&lt;network_services_keys.name&gt;.[].evpn_l3_multicast.evpn_underlay_l3_multicast_group_ipv4_pool") | String | Required |  |  | IPv4_address/Mask |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_underlay_l3_multicast_group_ipv4_pool_offset</samp>](## "&lt;network_services_keys.name&gt;.[].evpn_l3_multicast.evpn_underlay_l3_multicast_group_ipv4_pool_offset") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_peg</samp>](## "&lt;network_services_keys.name&gt;.[].evpn_l3_multicast.evpn_peg") | List, items: Dictionary |  |  |  | For each group of nodes, allow configuration of EVPN PEG options.<br>The first group of settings where the device's hostname is present in the 'nodes' list will be used.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- nodes</samp>](## "&lt;network_services_keys.name&gt;.[].evpn_l3_multicast.evpn_peg.[].nodes") | List, items: String |  |  |  | A description will be applied to all nodes with RP addresses configured if not set. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;network_services_keys.name&gt;.[].evpn_l3_multicast.evpn_peg.[].nodes.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;transit</samp>](## "&lt;network_services_keys.name&gt;.[].evpn_l3_multicast.evpn_peg.[].transit") | Boolean |  |  |  | Enable EVPN PEG transit mode. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;pim_rp_addresses</samp>](## "&lt;network_services_keys.name&gt;.[].pim_rp_addresses") | List, items: Dictionary |  |  |  | For each group of nodes, allow configuration of RP Addresses & associated groups.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- rps</samp>](## "&lt;network_services_keys.name&gt;.[].pim_rp_addresses.[].rps") | List, items: String |  |  | Min Length: 1 | List of Rendevouz Points |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;network_services_keys.name&gt;.[].pim_rp_addresses.[].rps.[].&lt;str&gt;") | String |  |  |  | RP address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "&lt;network_services_keys.name&gt;.[].pim_rp_addresses.[].nodes") | List, items: String |  |  |  | Restrict configuration to specific nodes.<br>Configuration Will be applied to all nodes if not set.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;network_services_keys.name&gt;.[].pim_rp_addresses.[].nodes.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;groups</samp>](## "&lt;network_services_keys.name&gt;.[].pim_rp_addresses.[].groups") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;network_services_keys.name&gt;.[].pim_rp_addresses.[].groups.[].&lt;str&gt;") | String |  |  |  | Group_prefix/mask |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;igmp_snooping_querier</samp>](## "&lt;network_services_keys.name&gt;.[].igmp_snooping_querier") | Dictionary |  |  |  | Enable IGMP snooping querier for each SVI/l2vlan within tenant, by default using IP address of Loopback 0.<br>When enabled, IGMP snooping querier will only be configured on L3 devices, i.e., uplink_type: p2p.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;network_services_keys.name&gt;.[].igmp_snooping_querier.enabled") | Boolean |  |  |  | Will be enabled automatically if "evpn_l2_multicast" is enabled. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_address</samp>](## "&lt;network_services_keys.name&gt;.[].igmp_snooping_querier.source_address") | String |  |  | Format: ipv4 | Default IP address of Loopback0 |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;version</samp>](## "&lt;network_services_keys.name&gt;.[].igmp_snooping_querier.version") | Integer |  | 2 | Valid Values:<br>- 1<br>- 2<br>- 3 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;evpn_l2_multi_domain</samp>](## "&lt;network_services_keys.name&gt;.[].evpn_l2_multi_domain") | Boolean |  | True |  | Explicitly extend all VLANs/VLAN-Aware Bundles inside the tenant to remote EVPN domains. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vrfs</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs") | List, items: Dictionary |  |  |  | VRF "default" is supported under network-services. Currently the supported options for "default" vrf are route-target,<br>route-distinguisher settings, structured_config, raw_eos_cli in bgp and SVIs are the only supported interface type.<br>Vlan-aware-bundles are supported as well inside default vrf. OSPF is not supported currently.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].name") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;address_families</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].address_families") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].address_families.[].&lt;str&gt;") | String |  |  | Valid Values:<br>- evpn<br>- vpn-ipv4<br>- vpn-ipv6 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].description") | String |  |  |  | VRF description |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf_vni</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].vrf_vni") | Integer |  |  | Min: 1<br>Max: 16777215 | Required if "vrf_id" is not set.<br>The VRF VNI range is not limited, but if vrf_id is not set, "vrf_vni" is used for calculating MLAG iBGP peering vlan id.<br>See "mlag_ibgp_peering_vrfs.base_vlan" for details.<br>If vrf_vni > 10000 make sure to adjust "mac_vrf_vni_base" accordingly to avoid overlap.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf_id</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].vrf_id") | Integer |  |  | Min: 1<br>Max: 1024 | Required if "vrf_vni" is not set.<br>"vrf_id" is used as default value for "vrf_vni" and "ospf.process_id" unless those are set.<br>"vrf_id" is preferred over "vrf_vni" for VRF RD/RT ID before vrf_vni<br>"vrf_id" is preferred over "vrf_vni" for MLAG iBGP peering vlan, see "mlag_ibgp_peering_vrfs.base_vlan" for details<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_ibgp_peering_ipv4_pool</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].mlag_ibgp_peering_ipv4_pool") | String |  |  |  | IPv4_address/Mask<br>The subnet used for iBGP peering in the VRF.<br>Each MLAG pair will be assigned a subnet based on the ID of the primary MLAG switch<br>If not set, "mlag_peer_l3_ipv4_pool" or "mlag_peer_ipv4_pool" will be used<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_helpers</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].ip_helpers") | List, items: Dictionary |  |  |  | IP helper for DHCP relay |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- ip_helper</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].ip_helpers.[].ip_helper") | String | Required, Unique |  |  | IPv4 DHCP server IP |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_interface</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].ip_helpers.[].source_interface") | String |  |  |  | Interface name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_vrf</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].ip_helpers.[].source_vrf") | String |  |  |  | VRF to originate DHCP relay packets to DHCP server. If not set, uses current VRF |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enable_mlag_ibgp_peering_vrfs</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].enable_mlag_ibgp_peering_vrfs") | Boolean |  |  |  | MLAG iBGP peering per VRF.<br>By default an iBGP peering is configured per VRF between MLAG peers on separate VLANs.<br>Setting enable_mlag_ibgp_peering_vrfs: false under vrf will change this default and/or override the tenant-wide setting<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_ibgp_peering_vlan</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].mlag_ibgp_peering_vlan") | Integer |  |  | Min: 1<br>Max: 4096 | Manually define the VLAN used on the MLAG pair for the iBGP session.<br>By default this parameter is calculated using the following formula: <mlag_ibgp_peering_vrfs.base_vlan> + <vrf_id> - 1<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vtep_diagnostic</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].vtep_diagnostic") | Dictionary |  |  |  | Enable VTEP Network diagnostics.<br>This will create a loopback with virtual source-nat enable to perform diagnostics from the switch<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loopback</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].vtep_diagnostic.loopback") | Integer |  |  | Min: 2<br>Max: 2100 | Loopback interface number, required (when vtep_diagnotics defined)<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loopback_description</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].vtep_diagnostic.loopback_description") | String |  |  |  | Provide a custom description for loopback interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loopback_ip_range</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].vtep_diagnostic.loopback_ip_range") | String |  |  |  | IPv4_address/Mask<br>Loopback ip range, a unique ip is derived from this ranged and assigned<br>to each l3 leaf based on it's unique id, ptional (loopback is not created unless loopback_ip_range or loopback_ip_pools are set)<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loopback_ip_pools</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].vtep_diagnostic.loopback_ip_pools") | List, items: Dictionary |  |  |  | For inventories with multiple PODs a loopback range can be set per POD to avoid overlaps.<br>This only takes effect when loopback_ip_range is not defined, ptional (loopback is not created unless loopback_ip_range or loopback_ip_pools are set)<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- pod</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].vtep_diagnostic.loopback_ip_pools.[].pod") | String |  |  |  | POD name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4_pool</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].vtep_diagnostic.loopback_ip_pools.[].ipv4_pool") | String |  |  |  | IPv4_address/Mask |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ospf</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].ospf") | Dictionary |  |  |  | Router OSPF configuration.<br>This will create an OSPF routing instance in the tenant VRF. If there is no nodes definition, the OSPF instance will be<br>created on all leafs where the VRF is deployed. This will also cause automatic OSPF redistribution into BGP unless<br>explicitly turned off with "redistribute_ospf: false".<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].ospf.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;process_id</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].ospf.process_id") | Integer |  |  |  | If not set, "vrf_id" will be used. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;router_id</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].ospf.router_id") | String |  |  |  | If not set, switch router_id will be used. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;max_lsa</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].ospf.max_lsa") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bfd</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].ospf.bfd") | Boolean |  | False |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;redistribute_bgp</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].ospf.redistribute_bgp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].ospf.redistribute_bgp.enabled") | Boolean |  | True |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].ospf.redistribute_bgp.route_map") | String |  |  |  | Route-map name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;redistribute_connected</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].ospf.redistribute_connected") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].ospf.redistribute_connected.enabled") | Boolean |  | False |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].ospf.redistribute_connected.route_map") | String |  |  |  | Route-map name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].ospf.nodes") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].ospf.nodes.[].&lt;str&gt;") | String |  |  |  | Hostname |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;redistribute_ospf</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].redistribute_ospf") | Boolean |  | True |  | Non-selectively enabling or disabling redistribute ospf inside the VRF. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_l3_multicast</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].evpn_l3_multicast") | Dictionary |  |  |  | Explicitly enable or disable evpn_l3_multicast to override setting of `<network_services_key>.[].evpn_l3_multicast.enabled`.<br>Allow override of `<network_services_key>.[].evpn_l3_multicast` node_settings.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].evpn_l3_multicast.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_peg</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].evpn_l3_multicast.evpn_peg") | List, items: Dictionary |  |  |  | For each group of nodes, allow configuration of EVPN PEG features. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- nodes</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].evpn_l3_multicast.evpn_peg.[].nodes") | List |  |  |  | Restrict configuration to specific nodes.<br>Will apply to all nodes with RP addresses configured if not set.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;transit</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].evpn_l3_multicast.evpn_peg.[].transit") | Boolean |  | False |  | Enable EVPN PEG transit mode. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pim_rp_addresses</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].pim_rp_addresses") | List, items: Dictionary |  |  |  | For each group of nodes, allow configuration of RP Addresses & associated groups.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- rps</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].pim_rp_addresses.[].rps") | List, items: String |  |  |  | A minimum of one RP must be specified. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].pim_rp_addresses.[].rps.[].&lt;str&gt;") | String |  |  |  | RP address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].pim_rp_addresses.[].nodes") | List, items: String |  |  |  | Restrict configuration to specific nodes.<br>Configuration Will be applied to all nodes if not set.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].pim_rp_addresses.[].nodes.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;groups</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].pim_rp_addresses.[].groups") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].pim_rp_addresses.[].groups.[].&lt;str&gt;") | String |  |  |  | Group_prefix/mask |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_l2_multi_domain</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].evpn_l2_multi_domain") | Boolean |  |  |  | Explicitly extend all VLANs/VLAN-Aware Bundles inside the VRF to remote EVPN domains.<br>Overrides `<network_services_key>.[].evpn_l2_multi_domain`.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;svis</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis") | List, items: Dictionary |  |  |  | List of SVIs<br>This will create both the L3 SVI and L2 VLAN based on filters applied to the node..<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- id</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].id") | Integer | Required, Unique |  | Min: 1<br>Max: 4096 | SVI interface id and VLAN id. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].name") | String | Required |  |  | VLAN name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;profile</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].profile") | String |  |  |  | SVI profile name to apply.<br>SVI can refer to one svi_profile which again can refer to another svi_profile to inherit settings in up to two levels (svi -> svi_profile -> svi_parent_profile).<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes") | List, items: Dictionary |  |  |  | Define node specific configuration, such as unique IP addresses. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- node</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].node") | String | Required, Unique |  |  | l3_leaf inventory hostname |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].name") | String |  |  |  | VLAN name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].enabled") | Boolean |  |  |  | Enable or disable interface |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].description") | String |  |  |  | SVI description. By default set to VLAN name.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].ip_address") | String |  |  |  | IPv4_address/Mask. Usually set under "nodes" to have unique IPv4 addresses per node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_address</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].ipv6_address") | String |  |  |  | IPv6_address/Mask. Usually set under "nodes" to have unique IPv6 addresses per node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_enable</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].ipv6_enable") | Boolean |  |  |  | Explicitly enable/disable link-local IPv6 addressing. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_address_virtual</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].ip_address_virtual") | String |  |  |  | IPv4_address/Mask<br>IPv4 VXLAN Anycast IP address<br>Conserves IP addresses in VXLAN deployments as it doesn't require unique IP addresses on each node.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_address_virtual</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].ipv6_address_virtual") | String |  |  |  | IPv6_address/Mask<br>ipv6 address virtuals to configure VXLAN Anycast IP address (Optional)<br>The below "ipv6_address_virtual" key will be deprecated in AVD v4.0 in favor of the new "ipv6_address_virtuals"<br>If both "ipv6_address_virtual" and "ipv6_address_virtuals" are set, all addresses will be configured<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_address_virtuals</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].ipv6_address_virtuals") | List, items: String |  |  |  | IPv6 VXLAN Anycast IP addresses<br>Conserves IPv6 addresses in VXLAN deployments as it doesn't require unique IPv6 addresses on each node.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].ipv6_address_virtuals.[].&lt;str&gt;") | String |  |  |  | IPv6_address/Mask |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_address_virtual_secondaries</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].ip_address_virtual_secondaries") | List, items: String |  |  |  | Secondary IPv4 VXLAN Anycast IP addresses |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].ip_address_virtual_secondaries.[].&lt;str&gt;") | String |  |  |  | IPv4_address/Mask |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_virtual_router_addresses</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].ip_virtual_router_addresses") | List, items: String |  |  |  | IPv4 VARP addresses.<br>Requires an IP address to be configured on the SVI.<br>If ip_address_virtual is also set, ip_virtual_router_addresses will take precedence<br>_if_ there is an ip_address configured for the node.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].ip_virtual_router_addresses.[].&lt;str&gt;") | String |  |  |  | IPv4_address/Mask or IPv4_address<br>IPv4_address/Mask will also configure a static route to the SVI per best practice.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_virtual_router_addresses</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].ipv6_virtual_router_addresses") | List, items: String |  |  |  | IPv6 VARP addresses.<br>Requires an IPv6 address to be configured on the SVI.<br>If ipv6_address_virtuals is also set, ipv6_virtual_router_addresses will take precedence<br>_if_ there is an ipv6_address configured for the node.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].ipv6_virtual_router_addresses.[].&lt;str&gt;") | String |  |  |  | IPv6_address |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_helpers</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].ip_helpers") | List, items: Dictionary |  |  |  | IP helper for DHCP relay |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- ip_helper</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].ip_helpers.[].ip_helper") | String | Required, Unique |  |  | IPv4 DHCP server IP |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_interface</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].ip_helpers.[].source_interface") | String |  |  |  | Interface name to originate DHCP relay packets to DHCP server. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_vrf</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].ip_helpers.[].source_vrf") | String |  |  |  | VRF to originate DHCP relay packets to DHCP server. If not set, EOS uses the VRF on the SVI. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vni_override</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].vni_override") | Integer |  |  | Min: 1<br>Max: 16777215 | By default the VNI will be derived from "mac_vrf_vni_base"<br>The vni_override allows us to override this value and statically define it (optional)<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rt_override</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].rt_override") | Integer |  |  | Min: 1<br>Max: 16777215 | By default the MAC VRF RD/RT ID will be derived from "mac_vrf_id_base"<br>The rt_override allows us to override this value and statically define it (optional)<br>If not set, vni_override will be used.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tags</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].tags") | List, items: String |  | ['all'] |  | Tags leveraged for networks services filtering<br>Tags are matched against "filter.tags" defined under Fabric Topology variables<br>Tags are also matched against the "node_group" name under Fabric Topology variables<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].tags.[].&lt;str&gt;") | String |  |  |  | Tag value |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;trunk_groups</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].trunk_groups") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].trunk_groups.[].&lt;str&gt;") | String |  |  |  | Trunk groups are used for limiting vlans to trunk ports assigned to the same trunk group<br>Requires "enable_trunk_groups: true"<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_l2_multicast</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].evpn_l2_multicast") | Dictionary |  |  |  | Explicitly enable or disable evpn_l2_multicast to override setting of `<network_services_key>.[].evpn_l2_multicast.enabled`.<br>When evpn_l2_multicast.enabled is set to true for a vlan or a tenant, "igmp snooping" and "igmp snooping querier" will always be enabled, overriding those individual settings.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].evpn_l2_multicast.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_l3_multicast</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].evpn_l3_multicast") | Dictionary |  |  |  | Explicitly enable or disable evpn_l3_multicast to override setting of `<network_services_key>.[].evpn_l3_multicast.enabled` and `<network_services_key>.[].vrfs.[].evpn_l3_multicast.enabled`.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].evpn_l3_multicast.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;igmp_snooping_enabled</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].igmp_snooping_enabled") | Boolean |  |  |  | Enable IGMP Snooping (Enabled by default on EOS) |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;igmp_snooping_querier</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].igmp_snooping_querier") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].igmp_snooping_querier.enabled") | Boolean |  |  |  | Will be enabled automatically if evpn_l2_multicast is enabled. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_address</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].igmp_snooping_querier.source_address") | String |  |  |  | IPv4_address<br>If not set, IP address of "Loopback0" will be used.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;version</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].igmp_snooping_querier.version") | Integer |  |  | Valid Values:<br>- 1<br>- 2<br>- 3 | IGMP Version (By default EOS uses IGMP version 2 for IGMP querier) |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vxlan</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].vxlan") | Boolean |  | True |  | Extend this SVI over VXLAN |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mtu</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].mtu") | Integer |  |  |  | Interface MTU |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ospf</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].ospf") | Dictionary |  |  |  | OSPF interface configuration |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].ospf.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;point_to_point</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].ospf.point_to_point") | Boolean |  | True |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;area</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].ospf.area") | String |  | 0 |  | OSPF area ID |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cost</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].ospf.cost") | Integer |  |  |  | OSPF link cost |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;authentication</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].ospf.authentication") | String |  |  | Valid Values:<br>- simple<br>- message-digest |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;simple_auth_key</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].ospf.simple_auth_key") | String |  |  |  | Password used with simple authentication |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;message_digest_keys</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].ospf.message_digest_keys") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- id</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].ospf.message_digest_keys.[].id") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hash_algorithm</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].ospf.message_digest_keys.[].hash_algorithm") | String |  | sha512 | Valid Values:<br>- md5<br>- sha1<br>- sha256<br>- sha384<br>- sha512 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].ospf.message_digest_keys.[].key") | String |  |  |  | Type 7 encrypted key |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].bgp") | Dictionary |  |  |  | Structured configuration and EOS CLI commands rendered on router_bgp.vlans<br>This configuration will not be applied to vlan aware bundles<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].bgp.structured_config") | Dictionary |  |  |  | Custom structured config added under vlan_interfaces.<interface> for eos_cli_config_gen.<br>Overrides the setting on SVI level.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].bgp.raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the VLAN interface in the final EOS configuration<br>Overrides the setting on SVI level.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the VLAN interface in the final EOS configuration<br>Overrides the setting on SVI level<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].structured_config") | Dictionary |  |  |  | Custom structured config added under vlan_interfaces.<interface> for eos_cli_config_gen.<br>Overrides the setting on SVI level. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].enabled") | Boolean |  |  |  | Enable or disable interface |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].description") | String |  |  |  | SVI description. By default set to VLAN name.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].ip_address") | String |  |  |  | IPv4_address/Mask. Usually set under "nodes" to have unique IPv4 addresses per node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_address</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].ipv6_address") | String |  |  |  | IPv6_address/Mask. Usually set under "nodes" to have unique IPv6 addresses per node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_enable</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].ipv6_enable") | Boolean |  |  |  | Explicitly enable/disable link-local IPv6 addressing. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_address_virtual</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].ip_address_virtual") | String |  |  |  | IPv4_address/Mask<br>IPv4 VXLAN Anycast IP address<br>Conserves IP addresses in VXLAN deployments as it doesn't require unique IP addresses on each node.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_address_virtual</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].ipv6_address_virtual") | String |  |  |  | IPv6_address/Mask<br>ipv6 address virtuals to configure VXLAN Anycast IP address (Optional)<br>The below "ipv6_address_virtual" key will be deprecated in AVD v4.0 in favor of the new "ipv6_address_virtuals"<br>If both "ipv6_address_virtual" and "ipv6_address_virtuals" are set, all addresses will be configured<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_address_virtuals</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].ipv6_address_virtuals") | List, items: String |  |  |  | IPv6 VXLAN Anycast IP addresses<br>Conserves IPv6 addresses in VXLAN deployments as it doesn't require unique IPv6 addresses on each node.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].ipv6_address_virtuals.[].&lt;str&gt;") | String |  |  |  | IPv6_address/Mask |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_address_virtual_secondaries</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].ip_address_virtual_secondaries") | List, items: String |  |  |  | Secondary IPv4 VXLAN Anycast IP addresses |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].ip_address_virtual_secondaries.[].&lt;str&gt;") | String |  |  |  | IPv4_address/Mask |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_virtual_router_addresses</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].ip_virtual_router_addresses") | List, items: String |  |  |  | IPv4 VARP addresses.<br>Requires an IP address to be configured on the SVI.<br>If ip_address_virtual is also set, ip_virtual_router_addresses will take precedence<br>_if_ there is an ip_address configured for the node.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].ip_virtual_router_addresses.[].&lt;str&gt;") | String |  |  |  | IPv4_address/Mask or IPv4_address<br>IPv4_address/Mask will also configure a static route to the SVI per best practice.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_virtual_router_addresses</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].ipv6_virtual_router_addresses") | List, items: String |  |  |  | IPv6 VARP addresses.<br>Requires an IPv6 address to be configured on the SVI.<br>If ipv6_address_virtuals is also set, ipv6_virtual_router_addresses will take precedence<br>_if_ there is an ipv6_address configured for the node.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].ipv6_virtual_router_addresses.[].&lt;str&gt;") | String |  |  |  | IPv6_address |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_helpers</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].ip_helpers") | List, items: Dictionary |  |  |  | IP helper for DHCP relay |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- ip_helper</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].ip_helpers.[].ip_helper") | String | Required, Unique |  |  | IPv4 DHCP server IP |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_interface</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].ip_helpers.[].source_interface") | String |  |  |  | Interface name to originate DHCP relay packets to DHCP server. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_vrf</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].ip_helpers.[].source_vrf") | String |  |  |  | VRF to originate DHCP relay packets to DHCP server. If not set, EOS uses the VRF on the SVI. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vni_override</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].vni_override") | Integer |  |  | Min: 1<br>Max: 16777215 | By default the VNI will be derived from "mac_vrf_vni_base"<br>The vni_override allows us to override this value and statically define it (optional)<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rt_override</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].rt_override") | Integer |  |  | Min: 1<br>Max: 16777215 | By default the MAC VRF RD/RT ID will be derived from "mac_vrf_id_base"<br>The rt_override allows us to override this value and statically define it (optional)<br>If not set, vni_override will be used.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tags</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].tags") | List, items: String |  | ['all'] |  | Tags leveraged for networks services filtering<br>Tags are matched against "filter.tags" defined under Fabric Topology variables<br>Tags are also matched against the "node_group" name under Fabric Topology variables<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].tags.[].&lt;str&gt;") | String |  |  |  | Tag value |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;trunk_groups</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].trunk_groups") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].trunk_groups.[].&lt;str&gt;") | String |  |  |  | Trunk groups are used for limiting vlans to trunk ports assigned to the same trunk group<br>Requires "enable_trunk_groups: true"<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_l2_multicast</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].evpn_l2_multicast") | Dictionary |  |  |  | Explicitly enable or disable evpn_l2_multicast to override setting of `<network_services_key>.[].evpn_l2_multicast.enabled`.<br>When evpn_l2_multicast.enabled is set to true for a vlan or a tenant, "igmp snooping" and "igmp snooping querier" will always be enabled, overriding those individual settings.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].evpn_l2_multicast.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_l3_multicast</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].evpn_l3_multicast") | Dictionary |  |  |  | Explicitly enable or disable evpn_l3_multicast to override setting of `<network_services_key>.[].evpn_l3_multicast.enabled` and `<network_services_key>.[].vrfs.[].evpn_l3_multicast.enabled`.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].evpn_l3_multicast.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;igmp_snooping_enabled</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].igmp_snooping_enabled") | Boolean |  |  |  | Enable IGMP Snooping (Enabled by default on EOS) |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;igmp_snooping_querier</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].igmp_snooping_querier") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].igmp_snooping_querier.enabled") | Boolean |  |  |  | Will be enabled automatically if evpn_l2_multicast is enabled. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_address</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].igmp_snooping_querier.source_address") | String |  |  |  | IPv4_address<br>If not set, IP address of "Loopback0" will be used.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;version</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].igmp_snooping_querier.version") | Integer |  |  | Valid Values:<br>- 1<br>- 2<br>- 3 | IGMP Version (By default EOS uses IGMP version 2 for IGMP querier) |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vxlan</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].vxlan") | Boolean |  | True |  | Extend this SVI over VXLAN |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mtu</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].mtu") | Integer |  |  |  | Interface MTU |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ospf</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].ospf") | Dictionary |  |  |  | OSPF interface configuration |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].ospf.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;point_to_point</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].ospf.point_to_point") | Boolean |  | True |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;area</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].ospf.area") | String |  | 0 |  | OSPF area ID |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cost</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].ospf.cost") | Integer |  |  |  | OSPF link cost |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;authentication</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].ospf.authentication") | String |  |  | Valid Values:<br>- simple<br>- message-digest |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;simple_auth_key</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].ospf.simple_auth_key") | String |  |  |  | Password used with simple authentication |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;message_digest_keys</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].ospf.message_digest_keys") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- id</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].ospf.message_digest_keys.[].id") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hash_algorithm</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].ospf.message_digest_keys.[].hash_algorithm") | String |  | sha512 | Valid Values:<br>- md5<br>- sha1<br>- sha256<br>- sha384<br>- sha512 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].ospf.message_digest_keys.[].key") | String |  |  |  | Type 7 encrypted key |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].bgp") | Dictionary |  |  |  | Structured configuration and EOS CLI commands rendered on router_bgp.vlans<br>This configuration will not be applied to vlan aware bundles<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].bgp.structured_config") | Dictionary |  |  |  | Custom structured config added under vlan_interfaces.<interface> for eos_cli_config_gen.<br>Overrides the setting on SVI level.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].bgp.raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the VLAN interface in the final EOS configuration<br>Overrides the setting on SVI level.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the VLAN interface in the final EOS configuration<br>Overrides the setting on SVI level<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].structured_config") | Dictionary |  |  |  | Custom structured config added under vlan_interfaces.<interface> for eos_cli_config_gen.<br>Overrides the setting on SVI level. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;l3_interfaces</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].l3_interfaces") | List, items: Dictionary |  |  |  | List of L3 interfaces.<br>This will create IP routed interface inside VRF. Length of interfaces, nodes and ip_addresses must match.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- interfaces</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].l3_interfaces.[].interfaces") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].l3_interfaces.[].interfaces.[].&lt;str&gt;") | String |  |  |  | Interface name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;encapsulation_dot1q_vlan</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].l3_interfaces.[].encapsulation_dot1q_vlan") | List, items: Integer |  |  |  | For sub-interfaces the dot1q vlan is derived from the interface name by default, but can also be specified. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;int&gt;</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].l3_interfaces.[].encapsulation_dot1q_vlan.[].&lt;int&gt;") | Integer |  |  | Min: 1<br>Max: 4094 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_addresses</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].l3_interfaces.[].ip_addresses") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].l3_interfaces.[].ip_addresses.[].&lt;str&gt;") | String |  |  |  | IPv4_address/Mask |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].l3_interfaces.[].nodes") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].l3_interfaces.[].nodes.[].&lt;str&gt;") | String |  |  |  | Node |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].l3_interfaces.[].description") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;descriptions</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].l3_interfaces.[].descriptions") | List, items: String |  |  |  | "descriptions" has precedence over "description"<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].l3_interfaces.[].descriptions.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].l3_interfaces.[].enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mtu</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].l3_interfaces.[].mtu") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ospf</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].l3_interfaces.[].ospf") | Dictionary |  |  |  | OSPF interface configuration |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].l3_interfaces.[].ospf.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;point_to_point</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].l3_interfaces.[].ospf.point_to_point") | Boolean |  | False |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;area</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].l3_interfaces.[].ospf.area") | Integer |  | 0 |  | OSPF area id |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cost</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].l3_interfaces.[].ospf.cost") | Integer |  |  |  | OSPF link cost |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;authentication</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].l3_interfaces.[].ospf.authentication") | String |  |  | Valid Values:<br>- simple<br>- message-digest |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;simple_auth_key</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].l3_interfaces.[].ospf.simple_auth_key") | String |  |  |  | Password used with simple authentication |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;message_digest_keys</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].l3_interfaces.[].ospf.message_digest_keys") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- id</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].l3_interfaces.[].ospf.message_digest_keys.[].id") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hash_algorithm</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].l3_interfaces.[].ospf.message_digest_keys.[].hash_algorithm") | String |  | sha512 | Valid Values:<br>- md5<br>- sha1<br>- sha256<br>- sha384<br>- sha512 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].l3_interfaces.[].ospf.message_digest_keys.[].key") | String |  |  |  | Key password |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pim</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].l3_interfaces.[].pim") | Dictionary |  |  |  | Enable PIM sparse-mode on the interface; requires "evpn_l3_multicast" to be enabled on the VRF/Tenant<br>Enabling this implicitly makes the device a PIM External Gateway (PEG) in EVPN designs only.<br>At least one RP address must be configured for EVPN PEG to be configured.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].l3_interfaces.[].pim.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].l3_interfaces.[].structured_config") | Dictionary |  |  |  | Custom structured config added under vlan_interfaces.<interface> for eos_cli_config_gen.<br>Overrides the setting on SVI level.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].l3_interfaces.[].raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the VLAN interface in the final EOS configuration<br>Overrides the setting on SVI level.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;static_routes</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].static_routes") | List, items: Dictionary |  |  |  | List of static routes for v4 and/or v6.<br>This will create static routes inside the tenant VRF.<br>If nodes are not specified, all l3leafs that carry the VRF will also be applied the static routes.<br>If a node has a static route in the VRF, redistribute static will be automatically enabled in that VRF.<br>This automatic behavior can be overridden non-selectively with the redistribute_static knob for the VRF.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- destination_address_prefix</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].static_routes.[].destination_address_prefix") | String |  |  |  | IPv4_address |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;gateway</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].static_routes.[].gateway") | String |  |  |  | IPv4_address |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;track_bfd</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].static_routes.[].track_bfd") | Boolean |  |  |  | Track next-hop using BFD |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;distance</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].static_routes.[].distance") | Integer |  |  | Min: 1<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tag</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].static_routes.[].tag") | Integer |  |  | Min: 0<br>Max: 4294967295 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].static_routes.[].name") | String |  |  |  | description |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;metric</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].static_routes.[].metric") | Integer |  |  | Min: 0<br>Max: 4294967295 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interface</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].static_routes.[].interface") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].static_routes.[].nodes") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].static_routes.[].nodes.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_static_routes</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].ipv6_static_routes") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- destination_address_prefix</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].ipv6_static_routes.[].destination_address_prefix") | String |  |  |  | IPv6_address |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;gateway</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].ipv6_static_routes.[].gateway") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;track_bfd</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].ipv6_static_routes.[].track_bfd") | Boolean |  |  |  | Track next-hop using BFD |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;distance</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].ipv6_static_routes.[].distance") | Integer |  |  | Min: 1<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tag</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].ipv6_static_routes.[].tag") | Integer |  |  | Min: 0<br>Max: 4294967295 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].ipv6_static_routes.[].name") | String |  |  |  | description |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;metric</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].ipv6_static_routes.[].metric") | Integer |  |  | Min: 0<br>Max: 4294967295 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interface</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].ipv6_static_routes.[].interface") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].ipv6_static_routes.[].nodes") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].ipv6_static_routes.[].nodes.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;redistribute_static</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].redistribute_static") | Boolean |  |  |  | Non-selectively enabling or disabling redistribute static inside the VRF. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp_peers</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peers") | List, items: Dictionary |  |  |  | List of BGP peer definitions.<br>This will configure BGP neighbors inside the tenant VRF for peering with external devices.<br>The configured peer will automatically be activated for ipv4 or ipv6 address family based on the ip address.<br>Note, only ipv4 and ipv6 address families are currently supported in eos_designs.<br>For other address families, use custom_structured configuration with eos_cli_config_gen.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- ip_address</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peers.[].ip_address") | String | Required, Unique |  |  | IPv4_address or IPv6_address |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer_group</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peers.[].peer_group") | String |  |  |  | Peer group name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remote_as</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peers.[].remote_as") | Integer |  |  |  | Remote ASN |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peers.[].description") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;password</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peers.[].password") | String |  |  |  | Encrypted password |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;send_community</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peers.[].send_community") | String |  |  |  | 'all' or a combination of 'standard', 'extended', 'large' and 'link-bandwidth (w/options)'<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;next_hop_self</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peers.[].next_hop_self") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;timers</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peers.[].timers") | String |  |  |  | BGP Keepalive and Hold Timer values in seconds as string <0-3600> <0-3600> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maximum_routes</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peers.[].maximum_routes") | Integer |  |  | Min: 0<br>Max: 4294967294 | Maximum number of routes (0 means unlimited) |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default_originate</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peers.[].default_originate") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;always</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peers.[].default_originate.always") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;update_source</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peers.[].update_source") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ebgp_multihop</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peers.[].ebgp_multihop") | Integer |  |  | Min: 1<br>Max: 255 | Time-to-live in range of hops |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peers.[].nodes") | List, items: String |  |  |  | Nodes is required to restrict configuration of BGP neighbors to certain nodes in the network. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peers.[].nodes.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;set_ipv4_next_hop</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peers.[].set_ipv4_next_hop") | String |  |  |  | IPv4_address<br>Next hop settings can be either ipv4 or ipv6 for one neighbor, this will be applied by a uniquely generated route-map per neighbor.<br>Next hop takes precedence over route_map_out.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;set_ipv6_next_hop</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peers.[].set_ipv6_next_hop") | String |  |  |  | IPv6_address<br>Next hop settings can be either ipv4 or ipv6 for one neighbor, this will be applied by a uniquely generated route-map per neighbor.<br>Next hop takes precedence over route_map_out.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_out</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peers.[].route_map_out") | String |  |  |  | Route-map name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_in</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peers.[].route_map_in") | String |  |  |  | Route-map name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefix_list_in</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peers.[].prefix_list_in") | String |  |  |  | Prefix list name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefix_list_out</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peers.[].prefix_list_out") | String |  |  |  | Prefix list name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;local_as</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peers.[].local_as") | String |  |  |  | Local BGP ASN<br>eg. "65001.1200"<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;weight</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peers.[].weight") | Integer |  |  | Min: 0<br>Max: 65535 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bfd</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peers.[].bfd") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp.raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the VLAN interface in the final EOS configuration<br>Overrides the setting on SVI level.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp.structured_config") | Dictionary |  |  |  | Custom structured config added under vlan_interfaces.<interface> for eos_cli_config_gen.<br>Overrides the setting on SVI level.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp_peer_groups</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups") | List, items: Dictionary |  |  |  | List of BGP peer groups definitions.<br>This will configure BGP peer groups to be used inside the tenant VRF for peering with external devices.<br>Since BGP peer groups are configured at higher BGP level, shared between VRFs,<br>peer_group names should not overlap between VRFs.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups.[].name") | String |  |  |  | BGP peer group name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups.[].nodes") | List, items: String |  |  |  | Nodes is required to restrict configuration of BGP neighbors to certain nodes in the network.<br>If not set the peer-group is created on devices which have a bgp_peer mapped to the corresponding peer_group.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups.[].nodes.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups.[].type") | String |  |  |  | Key only used for documentation or validation purposes |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remote_as</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups.[].remote_as") | String |  |  |  | BGP AS <1-4294967295> or AS number in asdot notation <1-65535>.<0-65535> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;local_as</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups.[].local_as") | String |  |  |  | BGP AS <1-4294967295> or AS number in asdot notation <1-65535>.<0-65535> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups.[].description") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;shutdown</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups.[].shutdown") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;as_path</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups.[].as_path") | Dictionary |  |  |  | BGP AS-PATH options |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remote_as_replace_out</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups.[].as_path.remote_as_replace_out") | Boolean |  |  |  | Replace AS number with local AS number |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prepend_own_disabled</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups.[].as_path.prepend_own_disabled") | Boolean |  |  |  | Disable prepending own AS number to AS path |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remove_private_as</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups.[].remove_private_as") | Dictionary |  |  |  | Remove private AS numbers in outbound AS path |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups.[].remove_private_as.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;all</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups.[].remove_private_as.all") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;replace_as</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups.[].remove_private_as.replace_as") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remove_private_as_ingress</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups.[].remove_private_as_ingress") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups.[].remove_private_as_ingress.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;replace_as</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups.[].remove_private_as_ingress.replace_as") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer_filter</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups.[].peer_filter") | String |  |  |  | Peer-filter name<br>note: `bgp_listen_range_prefix` and `peer_filter` will be deprecated in AVD v4.0<br>These should not be mixed with the new `listen_ranges` key above to avoid conflicts.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;next_hop_unchanged</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups.[].next_hop_unchanged") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;update_source</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups.[].update_source") | String |  |  |  | IP address or interface name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_reflector_client</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups.[].route_reflector_client") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bfd</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups.[].bfd") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ebgp_multihop</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups.[].ebgp_multihop") | Integer |  |  | Min: 1<br>Max: 255 | Time-to-live in range of hops |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;next_hop_self</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups.[].next_hop_self") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;password</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups.[].password") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;passive</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups.[].passive") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default_originate</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups.[].default_originate") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups.[].default_originate.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;always</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups.[].default_originate.always") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups.[].default_originate.route_map") | String |  |  |  | Route-map name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;send_community</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups.[].send_community") | String |  |  |  | 'all' or a combination of 'standard', 'extended', 'large' and 'link-bandwidth (w/options)' |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maximum_routes</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups.[].maximum_routes") | Integer |  |  | Min: 0<br>Max: 4294967294 | Maximum number of routes (0 means unlimited) |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maximum_routes_warning_limit</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups.[].maximum_routes_warning_limit") | String |  |  |  | Maximum number of routes after which a warning is issued (0 means never warn) or<br>Percentage of maximum number of routes at which to warn ("<1-100> percent")<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maximum_routes_warning_only</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups.[].maximum_routes_warning_only") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;link_bandwidth</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups.[].link_bandwidth") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups.[].link_bandwidth.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups.[].link_bandwidth.default") | String |  |  |  | nn.nn(K|M|G) link speed in bits/second |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;allowas_in</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups.[].allowas_in") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups.[].allowas_in.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;times</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups.[].allowas_in.times") | Integer |  |  | Min: 1<br>Max: 10 | Number of local ASNs allowed in a BGP update |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;weight</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups.[].weight") | Integer |  |  | Min: 0<br>Max: 65535 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;timers</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups.[].timers") | String |  |  |  | BGP Keepalive and Hold Timer values in seconds as string "<0-3600> <0-3600>" |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rib_in_pre_policy_retain</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups.[].rib_in_pre_policy_retain") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups.[].rib_in_pre_policy_retain.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;all</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups.[].rib_in_pre_policy_retain.all") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_in</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups.[].route_map_in") | String |  |  |  | Inbound route-map name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_out</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups.[].route_map_out") | String |  |  |  | Outbound route-map name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp_listen_range_prefix</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups.[].bgp_listen_range_prefix") | String |  |  |  | IP prefix range<br>note: `bgp_listen_range_prefix` and `peer_filter` will be deprecated in AVD v4.0<br>These should not be mixed with the new `listen_ranges` key above to avoid conflicts.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;session_tracker</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups.[].session_tracker") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;additional_route_targets</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].additional_route_targets") | List, items: Dictionary |  |  |  | Configuration of extra route-targets for this VRF. Useful for route-leaking or gateway between address families. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- type</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].additional_route_targets.[].type") | String |  |  | Valid Values:<br>- import<br>- export |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;address_family</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].additional_route_targets.[].address_family") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_target</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].additional_route_targets.[].route_target") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].additional_route_targets.[].nodes") | List, items: String |  |  |  | Nodes is required to restrict configuration of BGP neighbors to certain nodes in the network.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].additional_route_targets.[].nodes.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the VLAN interface in the final EOS configuration<br>Overrides the setting on SVI level.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].structured_config") | Dictionary |  |  |  | Custom structured config added under vlan_interfaces.<interface> for eos_cli_config_gen.<br>Overrides the setting on SVI level.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;l2vlans</samp>](## "&lt;network_services_keys.name&gt;.[].l2vlans") | List, items: Dictionary |  |  |  | Define L2 network services organized by vlan id. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- id</samp>](## "&lt;network_services_keys.name&gt;.[].l2vlans.[].id") | Integer | Required, Unique |  | Min: 1<br>Max: 4094 | VLAN ID |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vni_override</samp>](## "&lt;network_services_keys.name&gt;.[].l2vlans.[].vni_override") | Integer |  |  | Min: 1<br>Max: 16777215 | By default the VNI will be derived from mac_vrf_vni_base<br>The vni_override, allows to override this value and statically define it.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rt_override</samp>](## "&lt;network_services_keys.name&gt;.[].l2vlans.[].rt_override") | Integer |  |  | Min: 1<br>Max: 16777215 | By default the MAC VRF RD/RT ID will be derived from mac_vrf_id_base<br>The rt_override allows us to override this value and statically define it.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "&lt;network_services_keys.name&gt;.[].l2vlans.[].name") | String | Required |  |  | VLAN name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tags</samp>](## "&lt;network_services_keys.name&gt;.[].l2vlans.[].tags") | List, items: String |  |  |  | Tags leveraged for networks services filtering<br>Tags are matched against filter.tags defined under Fabric Topology variables<br>Tags are also matched against the node_group name under Fabric Topology variables<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;network_services_keys.name&gt;.[].l2vlans.[].tags.[].&lt;str&gt;") | String |  | all |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vxlan</samp>](## "&lt;network_services_keys.name&gt;.[].l2vlans.[].vxlan") | Boolean |  | True |  | Extend this L2VLAN over VXLAN |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;trunk_groups</samp>](## "&lt;network_services_keys.name&gt;.[].l2vlans.[].trunk_groups") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;network_services_keys.name&gt;.[].l2vlans.[].trunk_groups.[].&lt;str&gt;") | String |  |  |  | Trunk groups are used for limiting vlans to trunk ports assigned to the same trunk group<br>Requires enable_trunk_groups: true<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_l2_multicast</samp>](## "&lt;network_services_keys.name&gt;.[].l2vlans.[].evpn_l2_multicast") | Dictionary |  |  |  | Explicitly enable or disable evpn_l2_multicast to override setting of `<network_services_key>.[].evpn_l2_multicast.enabled`.<br>When evpn_l2_multicast.enabled is set to true for a vlan or a tenant, igmp snooping and igmp snooping querier will always be enabled, overriding those individual settings.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;network_services_keys.name&gt;.[].l2vlans.[].evpn_l2_multicast.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;igmp_snooping_enabled</samp>](## "&lt;network_services_keys.name&gt;.[].l2vlans.[].igmp_snooping_enabled") | Boolean |  | True |  | Activate or deactivate IGMP snooping |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;igmp_snooping_querier</samp>](## "&lt;network_services_keys.name&gt;.[].l2vlans.[].igmp_snooping_querier") | Dictionary |  |  |  | Enable igmp snooping querier, by default using IP address of Loopback 0.<br>When enabled, igmp snooping querier will only be configured on l3 devices, i.e., uplink_type: p2p.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;network_services_keys.name&gt;.[].l2vlans.[].igmp_snooping_querier.enabled") | Boolean |  |  |  | Will be enabled automatically if evpn_l2_multicast is enabled. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_address</samp>](## "&lt;network_services_keys.name&gt;.[].l2vlans.[].igmp_snooping_querier.source_address") | String |  |  |  | IPv4_address<br>If not set, IP address of "Loopback0" will be used.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;version</samp>](## "&lt;network_services_keys.name&gt;.[].l2vlans.[].igmp_snooping_querier.version") | Integer |  | 2 | Valid Values:<br>- 1<br>- 2<br>- 3 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp</samp>](## "&lt;network_services_keys.name&gt;.[].l2vlans.[].bgp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "&lt;network_services_keys.name&gt;.[].l2vlans.[].bgp.structured_config") | Dictionary |  |  |  | Structured configuration for eos_cli_config_gen rendered on router_bgp.vlans.<br>This configuration will not be applied to vlan aware bundles.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "&lt;network_services_keys.name&gt;.[].l2vlans.[].bgp.raw_eos_cli") | String |  |  |  | EOS cli commands rendered on router_bgp.vlans.<br>This configuration will not be applied to vlan aware bundles.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;point_to_point_services</samp>](## "&lt;network_services_keys.name&gt;.[].point_to_point_services") | List, items: Dictionary |  |  |  | Point to point services (pseudowires).<br>Only supported for node types with "network_services.l1: true".<br>By default this is only set for node type "pe" with "design.type: mpls"<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "&lt;network_services_keys.name&gt;.[].point_to_point_services.[].name") | String | Required, Unique |  |  | Pseudowire name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "&lt;network_services_keys.name&gt;.[].point_to_point_services.[].type") | String |  | vpws-pseudowire | Valid Values:<br>- vpws-pseudowire |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;subinterfaces</samp>](## "&lt;network_services_keys.name&gt;.[].point_to_point_services.[].subinterfaces") | List, items: Dictionary |  |  |  | Subinterfaces will create subinterfaces and additional pseudowires/patch panel config for each endpoint. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- number</samp>](## "&lt;network_services_keys.name&gt;.[].point_to_point_services.[].subinterfaces.[].number") | Integer | Required, Unique |  |  | Subinterface number |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;endpoints</samp>](## "&lt;network_services_keys.name&gt;.[].point_to_point_services.[].endpoints") | List, items: Dictionary |  |  | Min Length: 2<br>Max Length: 2 | Pseudowire terminating endpoints. Must have exactly two items. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- id</samp>](## "&lt;network_services_keys.name&gt;.[].point_to_point_services.[].endpoints.[].id") | Integer | Required |  |  | Pseudowire ID on this endpoint |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "&lt;network_services_keys.name&gt;.[].point_to_point_services.[].endpoints.[].nodes") | List, items: String | Required |  | Min Length: 1 | Usually one node. With ESI multihoming we support two nodes per pseudowire endpoint<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;network_services_keys.name&gt;.[].point_to_point_services.[].endpoints.[].nodes.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interfaces</samp>](## "&lt;network_services_keys.name&gt;.[].point_to_point_services.[].endpoints.[].interfaces") | List, items: String | Required |  | Min Length: 1 | Interfaces patched to the pseudowire on this endpoints.<br>The list of interfaces is mapped to the list of nodes, so they must have the same length.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;network_services_keys.name&gt;.[].point_to_point_services.[].endpoints.[].interfaces.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;port_channel</samp>](## "&lt;network_services_keys.name&gt;.[].point_to_point_services.[].endpoints.[].port_channel") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "&lt;network_services_keys.name&gt;.[].point_to_point_services.[].endpoints.[].port_channel.mode") | String |  |  | Valid Values:<br>- active<br>- on |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;short_esi</samp>](## "&lt;network_services_keys.name&gt;.[].point_to_point_services.[].endpoints.[].port_channel.short_esi") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;lldp_disable</samp>](## "&lt;network_services_keys.name&gt;.[].point_to_point_services.[].lldp_disable") | Boolean |  |  |  | Disable LLDP RX/TX on port mode pseudowire services |

=== "YAML"

    ```yaml
    <network_services_keys.name>:
      - name: <str>
        mac_vrf_vni_base: <int>
        mac_vrf_id_base: <int>
        vlan_aware_bundle_number_base: <int>
        pseudowire_rt_base: <int>
        enable_mlag_ibgp_peering_vrfs: <bool>
        bgp_peer_groups:
          - name: <str>
            nodes:
              - <str>
            type: <str>
            remote_as: <str>
            local_as: <str>
            description: <str>
            shutdown: <bool>
            as_path:
              remote_as_replace_out: <bool>
              prepend_own_disabled: <bool>
            remove_private_as:
              enabled: <bool>
              all: <bool>
              replace_as: <bool>
            remove_private_as_ingress:
              enabled: <bool>
              replace_as: <bool>
            peer_filter: <str>
            next_hop_unchanged: <bool>
            update_source: <str>
            route_reflector_client: <bool>
            bfd: <bool>
            ebgp_multihop: <int>
            next_hop_self: <bool>
            password: <str>
            passive: <bool>
            default_originate:
              enabled: <bool>
              always: <bool>
              route_map: <str>
            send_community: <str>
            maximum_routes: <int>
            maximum_routes_warning_limit: <str>
            maximum_routes_warning_only: <bool>
            link_bandwidth:
              enabled: <bool>
              default: <str>
            allowas_in:
              enabled: <bool>
              times: <int>
            weight: <int>
            timers: <str>
            rib_in_pre_policy_retain:
              enabled: <bool>
              all: <bool>
            route_map_in: <str>
            route_map_out: <str>
            bgp_listen_range_prefix: <str>
            session_tracker: <str>
        evpn_l2_multicast:
          enabled: <bool>
          underlay_l2_multicast_group_ipv4_pool: <str>
          underlay_l2_multicast_group_ipv4_pool_offset: <int>
        evpn_l3_multicast:
          enabled: <bool>
          evpn_underlay_l3_multicast_group_ipv4_pool: <str>
          evpn_underlay_l3_multicast_group_ipv4_pool_offset: <int>
          evpn_peg:
            - nodes:
                - <str>
              transit: <bool>
        pim_rp_addresses:
          - rps:
              - <str>
            nodes:
              - <str>
            groups:
              - <str>
        igmp_snooping_querier:
          enabled: <bool>
          source_address: <str>
          version: <int>
        evpn_l2_multi_domain: <bool>
        vrfs:
          - name: <str>
            address_families:
              - <str>
            description: <str>
            vrf_vni: <int>
            vrf_id: <int>
            mlag_ibgp_peering_ipv4_pool: <str>
            ip_helpers:
              - ip_helper: <str>
                source_interface: <str>
                source_vrf: <str>
            enable_mlag_ibgp_peering_vrfs: <bool>
            mlag_ibgp_peering_vlan: <int>
            vtep_diagnostic:
              loopback: <int>
              loopback_description: <str>
              loopback_ip_range: <str>
              loopback_ip_pools:
                - pod: <str>
                  ipv4_pool: <str>
            ospf:
              enabled: <bool>
              process_id: <int>
              router_id: <str>
              max_lsa: <int>
              bfd: <bool>
              redistribute_bgp:
                enabled: <bool>
                route_map: <str>
              redistribute_connected:
                enabled: <bool>
                route_map: <str>
              nodes:
                - <str>
            redistribute_ospf: <bool>
            evpn_l3_multicast:
              enabled: <bool>
              evpn_peg:
                - nodes: <list>
                  transit: <bool>
            pim_rp_addresses:
              - rps:
                  - <str>
                nodes:
                  - <str>
                groups:
                  - <str>
            evpn_l2_multi_domain: <bool>
            svis:
              - id: <int>
                name: <str>
                profile: <str>
                nodes:
                  - node: <str>
                    name: <str>
                    enabled: <bool>
                    description: <str>
                    ip_address: <str>
                    ipv6_address: <str>
                    ipv6_enable: <bool>
                    ip_address_virtual: <str>
                    ipv6_address_virtual: <str>
                    ipv6_address_virtuals:
                      - <str>
                    ip_address_virtual_secondaries:
                      - <str>
                    ip_virtual_router_addresses:
                      - <str>
                    ipv6_virtual_router_addresses:
                      - <str>
                    ip_helpers:
                      - ip_helper: <str>
                        source_interface: <str>
                        source_vrf: <str>
                    vni_override: <int>
                    rt_override: <int>
                    tags:
                      - <str>
                    trunk_groups:
                      - <str>
                    evpn_l2_multicast:
                      enabled: <bool>
                    evpn_l3_multicast:
                      enabled: <bool>
                    igmp_snooping_enabled: <bool>
                    igmp_snooping_querier:
                      enabled: <bool>
                      source_address: <str>
                      version: <int>
                    vxlan: <bool>
                    mtu: <int>
                    ospf:
                      enabled: <bool>
                      point_to_point: <bool>
                      area: <str>
                      cost: <int>
                      authentication: <str>
                      simple_auth_key: <str>
                      message_digest_keys:
                        - id: <int>
                          hash_algorithm: <str>
                          key: <str>
                    bgp:
                      structured_config: <dict>
                      raw_eos_cli: <str>
                    raw_eos_cli: <str>
                    structured_config: <dict>
                enabled: <bool>
                description: <str>
                ip_address: <str>
                ipv6_address: <str>
                ipv6_enable: <bool>
                ip_address_virtual: <str>
                ipv6_address_virtual: <str>
                ipv6_address_virtuals:
                  - <str>
                ip_address_virtual_secondaries:
                  - <str>
                ip_virtual_router_addresses:
                  - <str>
                ipv6_virtual_router_addresses:
                  - <str>
                ip_helpers:
                  - ip_helper: <str>
                    source_interface: <str>
                    source_vrf: <str>
                vni_override: <int>
                rt_override: <int>
                tags:
                  - <str>
                trunk_groups:
                  - <str>
                evpn_l2_multicast:
                  enabled: <bool>
                evpn_l3_multicast:
                  enabled: <bool>
                igmp_snooping_enabled: <bool>
                igmp_snooping_querier:
                  enabled: <bool>
                  source_address: <str>
                  version: <int>
                vxlan: <bool>
                mtu: <int>
                ospf:
                  enabled: <bool>
                  point_to_point: <bool>
                  area: <str>
                  cost: <int>
                  authentication: <str>
                  simple_auth_key: <str>
                  message_digest_keys:
                    - id: <int>
                      hash_algorithm: <str>
                      key: <str>
                bgp:
                  structured_config: <dict>
                  raw_eos_cli: <str>
                raw_eos_cli: <str>
                structured_config: <dict>
            l3_interfaces:
              - interfaces:
                  - <str>
                encapsulation_dot1q_vlan:
                  - <int>
                ip_addresses:
                  - <str>
                nodes:
                  - <str>
                description: <str>
                descriptions:
                  - <str>
                enabled: <bool>
                mtu: <int>
                ospf:
                  enabled: <bool>
                  point_to_point: <bool>
                  area: <int>
                  cost: <int>
                  authentication: <str>
                  simple_auth_key: <str>
                  message_digest_keys:
                    - id: <int>
                      hash_algorithm: <str>
                      key: <str>
                pim:
                  enabled: <bool>
                structured_config: <dict>
                raw_eos_cli: <str>
            static_routes:
              - destination_address_prefix: <str>
                gateway: <str>
                track_bfd: <bool>
                distance: <int>
                tag: <int>
                name: <str>
                metric: <int>
                interface: <str>
                nodes:
                  - <str>
            ipv6_static_routes:
              - destination_address_prefix: <str>
                gateway: <str>
                track_bfd: <bool>
                distance: <int>
                tag: <int>
                name: <str>
                metric: <int>
                interface: <str>
                nodes:
                  - <str>
            redistribute_static: <bool>
            bgp_peers:
              - ip_address: <str>
                peer_group: <str>
                remote_as: <int>
                description: <str>
                password: <str>
                send_community: <str>
                next_hop_self: <bool>
                timers: <str>
                maximum_routes: <int>
                default_originate:
                  always: <bool>
                update_source: <str>
                ebgp_multihop: <int>
                nodes:
                  - <str>
                set_ipv4_next_hop: <str>
                set_ipv6_next_hop: <str>
                route_map_out: <str>
                route_map_in: <str>
                prefix_list_in: <str>
                prefix_list_out: <str>
                local_as: <str>
                weight: <int>
                bfd: <bool>
            bgp:
              raw_eos_cli: <str>
              structured_config: <dict>
            bgp_peer_groups:
              - name: <str>
                nodes:
                  - <str>
                type: <str>
                remote_as: <str>
                local_as: <str>
                description: <str>
                shutdown: <bool>
                as_path:
                  remote_as_replace_out: <bool>
                  prepend_own_disabled: <bool>
                remove_private_as:
                  enabled: <bool>
                  all: <bool>
                  replace_as: <bool>
                remove_private_as_ingress:
                  enabled: <bool>
                  replace_as: <bool>
                peer_filter: <str>
                next_hop_unchanged: <bool>
                update_source: <str>
                route_reflector_client: <bool>
                bfd: <bool>
                ebgp_multihop: <int>
                next_hop_self: <bool>
                password: <str>
                passive: <bool>
                default_originate:
                  enabled: <bool>
                  always: <bool>
                  route_map: <str>
                send_community: <str>
                maximum_routes: <int>
                maximum_routes_warning_limit: <str>
                maximum_routes_warning_only: <bool>
                link_bandwidth:
                  enabled: <bool>
                  default: <str>
                allowas_in:
                  enabled: <bool>
                  times: <int>
                weight: <int>
                timers: <str>
                rib_in_pre_policy_retain:
                  enabled: <bool>
                  all: <bool>
                route_map_in: <str>
                route_map_out: <str>
                bgp_listen_range_prefix: <str>
                session_tracker: <str>
            additional_route_targets:
              - type: <str>
                address_family: <str>
                route_target: <str>
                nodes:
                  - <str>
            raw_eos_cli: <str>
            structured_config: <dict>
        l2vlans:
          - id: <int>
            vni_override: <int>
            rt_override: <int>
            name: <str>
            tags:
              - <str>
            vxlan: <bool>
            trunk_groups:
              - <str>
            evpn_l2_multicast:
              enabled: <bool>
            igmp_snooping_enabled: <bool>
            igmp_snooping_querier:
              enabled: <bool>
              source_address: <str>
              version: <int>
            bgp:
              structured_config: <dict>
              raw_eos_cli: <str>
        point_to_point_services:
          - name: <str>
            type: <str>
            subinterfaces:
              - number: <int>
            endpoints:
              - id: <int>
                nodes:
                  - <str>
                interfaces:
                  - <str>
                port_channel:
                  mode: <str>
                  short_esi: <str>
            lldp_disable: <bool>
    ```

## <Node Type Keys.Key>

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>&lt;node_type_keys.key&gt;</samp>](## "&lt;node_type_keys.key&gt;") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;defaults</samp>](## "&lt;node_type_keys.key&gt;.defaults") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;id</samp>](## "&lt;node_type_keys.key&gt;.defaults.id") | Integer |  |  |  | Unique identifier used for IP addressing and other algorithms. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;platform</samp>](## "&lt;node_type_keys.key&gt;.defaults.platform") | String |  |  |  | Arista platform family. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mac_address</samp>](## "&lt;node_type_keys.key&gt;.defaults.mac_address") | String |  |  |  | Leverage to document management interface mac address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;system_mac_address</samp>](## "&lt;node_type_keys.key&gt;.defaults.system_mac_address") | String |  |  |  | System MAC Address in this following format: "xx:xx:xx:xx:xx:xx".<br>Set to the same MAC address as available in "show version" on the device.<br>"system_mac_address" can also be set directly as a hostvar.<br>If both are set, the setting under "Fabric Topology" takes precedence.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;serial_number</samp>](## "&lt;node_type_keys.key&gt;.defaults.serial_number") | String |  |  |  | Set to the Serial Number of the device<br>For  now only used for documentation purpose in the fabric documentation<br>and part of the structured_config<br>"serial_number" can also be set directly as a hostvar.<br>If both are set, the setting under "Fabric Topology" takes precedence.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;rack</samp>](## "&lt;node_type_keys.key&gt;.defaults.rack") | String |  |  |  | Rack that the switch is located in (only used in snmp_settings location). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mgmt_ip</samp>](## "&lt;node_type_keys.key&gt;.defaults.mgmt_ip") | String |  |  | Format: cidr | Node management interface IPv4 address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_mgmt_ip</samp>](## "&lt;node_type_keys.key&gt;.defaults.ipv6_mgmt_ip") | String |  |  | Format: cidr | Node management interface IPv6 address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mgmt_interface</samp>](## "&lt;node_type_keys.key&gt;.defaults.mgmt_interface") | String |  |  |  | Management Interface Name.<br>Default -> platform_management_interface -> mgmt_interface -> "Management1".<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;link_tracking</samp>](## "&lt;node_type_keys.key&gt;.defaults.link_tracking") | Dictionary |  |  |  | This configures the Link Tracking Group on a switch as well as adds the p2p-uplinks of the switch as the upstream interfaces.<br>Useful in EVPN multhoming designs.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;node_type_keys.key&gt;.defaults.link_tracking.enabled") | Boolean |  | False |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;groups</samp>](## "&lt;node_type_keys.key&gt;.defaults.link_tracking.groups") | List, items: Dictionary |  | [{'name': 'LT_GROUP1'}] |  | Link Tracking Groups.<br>By default a single group named "LT_GROUP1" is defined with default values.<br>Any groups defined under "groups" will replace the default.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "&lt;node_type_keys.key&gt;.defaults.link_tracking.groups.[].name") | String |  |  |  | Tracking group name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;recovery_delay</samp>](## "&lt;node_type_keys.key&gt;.defaults.link_tracking.groups.[].recovery_delay") | Integer |  |  | Min: 0<br>Max: 3600 | default -> platform_settings_mlag_reload_delay -> 300. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;links_minimum</samp>](## "&lt;node_type_keys.key&gt;.defaults.link_tracking.groups.[].links_minimum") | Integer |  |  | Min: 1<br>Max: 100000 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;lacp_port_id_range</samp>](## "&lt;node_type_keys.key&gt;.defaults.lacp_port_id_range") | Dictionary |  |  |  | This will generate the "lacp port-id range", "begin" and "end" values based on node "id" and the number of nodes in the "node_group".<br>Unique LACP port-id ranges are recommended for EVPN Multihoming designs.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;node_type_keys.key&gt;.defaults.lacp_port_id_range.enabled") | Boolean |  | False |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;size</samp>](## "&lt;node_type_keys.key&gt;.defaults.lacp_port_id_range.size") | Integer |  | 128 |  | Recommended size > = number of ports in the switch. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;offset</samp>](## "&lt;node_type_keys.key&gt;.defaults.lacp_port_id_range.offset") | Integer |  | 0 |  | Offset is used to avoid overlapping port-id ranges of different switches.<br>Useful when a "connected-endpoint" is connected to switches in different "node_groups".<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;always_configure_ip_routing</samp>](## "&lt;node_type_keys.key&gt;.defaults.always_configure_ip_routing") | Boolean |  | False |  | Force configuration of "ip routing" even on L2 devices.<br>Use this to retain behavior of AVD versions below 4.0.0.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "&lt;node_type_keys.key&gt;.defaults.raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the root level of the final EOS configuration. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "&lt;node_type_keys.key&gt;.defaults.structured_config") | Dictionary |  |  |  | Custom structured config for eos_cli_config_gen. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;uplink_ipv4_pool</samp>](## "&lt;node_type_keys.key&gt;.defaults.uplink_ipv4_pool") | String |  |  | Format: ipv4_cidr | IPv4 subnet to use to connect to uplink switches. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;uplink_interfaces</samp>](## "&lt;node_type_keys.key&gt;.defaults.uplink_interfaces") | List, items: String |  |  |  | Local uplink interfaces<br>Each list item supports range syntax that can be expanded into a list of interfaces.<br>If uplink_interfaces is not defined, platform-specific defaults (defined under default_interfaces) will be used instead.<br>Please note that default_interfaces are not defined by default, you should define these yourself.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.defaults.uplink_interfaces.[].&lt;str&gt;") | String |  |  | Pattern: Ethernet[\d/]+ |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;uplink_switch_interfaces</samp>](## "&lt;node_type_keys.key&gt;.defaults.uplink_switch_interfaces") | List, items: String |  |  |  | Interfaces located on uplink switches |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.defaults.uplink_switch_interfaces.[].&lt;str&gt;") | String |  |  | Pattern: Ethernet[\d/]+ |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;uplink_switches</samp>](## "&lt;node_type_keys.key&gt;.defaults.uplink_switches") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.defaults.uplink_switches.[].&lt;str&gt;") | String | Required |  |  | Hostname of uplink switch.<br>If parallel uplinks are in use, update max_parallel_uplinks below and specify each uplink switch multiple times.<br>e.g. uplink_switches: [ 'DC1-SPINE1', 'DC1-SPINE1', 'DC1-SPINE2', 'DC1-SPINE2' ].<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;uplink_interface_speed</samp>](## "&lt;node_type_keys.key&gt;.defaults.uplink_interface_speed") | String |  |  |  | Set point-to-Point interface speed and will apply to uplink interfaces on both ends.<br>interface_speed or forced interface_speed or auto interface_speed.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;max_uplink_switches</samp>](## "&lt;node_type_keys.key&gt;.defaults.max_uplink_switches") | Integer |  |  |  | Maximum number of uplink switches.<br>Changing this value may change IP Addressing on uplinks.<br>Can be used to reserve IP space for future expansions.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;max_parallel_uplinks</samp>](## "&lt;node_type_keys.key&gt;.defaults.max_parallel_uplinks") | Integer |  |  |  | Number of parallel links towards uplink switches.<br>Changing this value may change interface naming on uplinks (and corresponding downlinks).<br>Can be used to reserve interfaces for future parallel uplinks.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;uplink_bfd</samp>](## "&lt;node_type_keys.key&gt;.defaults.uplink_bfd") | Boolean |  | False |  | Enable bfd on uplink interfaces. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;uplink_native_vlan</samp>](## "&lt;node_type_keys.key&gt;.defaults.uplink_native_vlan") | Integer |  |  | Min: 1<br>Max: 4094 | Only applicable to switches with layer-2 port-channel uplinks.<br>A suspended (disabled) vlan will be created in both ends of the link unless the vlan is defined under network services.<br>By default the uplink will not have a native_vlan configured, so EOS defaults to vlan 1.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;uplink_ptp</samp>](## "&lt;node_type_keys.key&gt;.defaults.uplink_ptp") | Dictionary |  |  |  | Enable PTP on all infrastructure links. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enable</samp>](## "&lt;node_type_keys.key&gt;.defaults.uplink_ptp.enable") | Boolean |  | False |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;uplink_macsec</samp>](## "&lt;node_type_keys.key&gt;.defaults.uplink_macsec") | Dictionary |  |  |  | Enable MacSec on all uplinks. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;profile</samp>](## "&lt;node_type_keys.key&gt;.defaults.uplink_macsec.profile") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;uplink_structured_config</samp>](## "&lt;node_type_keys.key&gt;.defaults.uplink_structured_config") | Dictionary |  |  |  | Custom structured config applied to "uplink_interfaces", and "uplink_switch_interfaces".<br>When uplink_type == "p2p", custom structured config added under ethernet_interfaces.<interface> for eos_cli_config_gen overrides the settings on the ethernet interface level.<br>When uplink_type == "port-channel", custom structured config added under port_channel_interfaces.<interface> for eos_cli_config_gen overrides the settings on the port-channel interface level.<br>"uplink_structured_config" is applied after "structured_config", so it can override "structured_config" defined on node-level.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mlag_port_channel_structured_config</samp>](## "&lt;node_type_keys.key&gt;.defaults.mlag_port_channel_structured_config") | Dictionary |  |  |  | Custom structured config applied to MLAG peer link port-channel id.<br>Added under port_channel_interfaces.<interface> for eos_cli_config_gen.<br>Overrides the settings on the port-channel interface level.<br>"mlag_port_channel_structured_config" is applied after "structured_config", so it can override "structured_config" defined on node-level.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mlag_peer_vlan_structured_config</samp>](## "&lt;node_type_keys.key&gt;.defaults.mlag_peer_vlan_structured_config") | Dictionary |  |  |  | Custom structured config applied to MLAG Peer Link (control link) SVI interface id.<br>Added under vlan_interfaces.<interface> for eos_cli_config_gen.<br>Overrides the settings on the vlan interface level.<br>"mlag_peer_vlan_structured_config" is applied after "structured_config", so it can override "structured_config" defined on node-level.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mlag_peer_l3_vlan_structured_config</samp>](## "&lt;node_type_keys.key&gt;.defaults.mlag_peer_l3_vlan_structured_config") | Dictionary |  |  |  | Custom structured config applied to MLAG underlay L3 peering SVI interface id.<br>Added under vlan_interfaces.<interface> for eos_cli_config_gen.<br>Overrides the settings on the vlan interface level.<br>"mlag_peer_l3_vlan_structured_config" is applied after "structured_config", so it can override "structured_config" defined on node-level.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;short_esi</samp>](## "&lt;node_type_keys.key&gt;.defaults.short_esi") | String |  |  |  | short_esi only valid for l2leaf devices using port-channel uplink.<br>Setting short_esi to "auto" generates the short_esi automatically using a hash of configuration elements.<br>< 0000:0000:0000 | auto >.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_system_id_prefix</samp>](## "&lt;node_type_keys.key&gt;.defaults.isis_system_id_prefix") | String |  |  | Pattern: [0-9a-f]{4}\.[0-9a-f]{4} | (4.4 hexadecimal). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_maximum_paths</samp>](## "&lt;node_type_keys.key&gt;.defaults.isis_maximum_paths") | Integer |  |  |  | Number of path to configure in ECMP for ISIS. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;is_type</samp>](## "&lt;node_type_keys.key&gt;.defaults.is_type") | String |  | level-2 | Valid Values:<br>- level-1-2<br>- level-1<br>- level-2 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;node_sid_base</samp>](## "&lt;node_type_keys.key&gt;.defaults.node_sid_base") | Integer |  | 0 |  | Node-SID base for isis-sr underlay variants. Combined with node id to generate ISIS-SR node-SID. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;loopback_ipv4_pool</samp>](## "&lt;node_type_keys.key&gt;.defaults.loopback_ipv4_pool") | String |  |  | Format: ipv4_cidr | IPv4 subnet for Loopback0 allocation. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vtep_loopback_ipv4_pool</samp>](## "&lt;node_type_keys.key&gt;.defaults.vtep_loopback_ipv4_pool") | String |  |  | Format: ipv4_cidr | IPv4 subnet for VTEP-Loopback allocation. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;loopback_ipv4_offset</samp>](## "&lt;node_type_keys.key&gt;.defaults.loopback_ipv4_offset") | Integer |  | 0 |  | Offset all assigned loopback IP addresses.<br>Required when the < loopback_ipv4_pool > is same for 2 different node_types (like spine and l3leaf) to avoid over-lapping IPs.<br>For example, set the minimum offset l3leaf.defaults.loopback_ipv4_offset: < total # spine switches > or vice versa.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;loopback_ipv6_pool</samp>](## "&lt;node_type_keys.key&gt;.defaults.loopback_ipv6_pool") | String |  |  | Format: ipv6_cidr | IPv6 subnet for Loopback0 allocation. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;loopback_ipv6_offset</samp>](## "&lt;node_type_keys.key&gt;.defaults.loopback_ipv6_offset") | Integer |  | 0 |  | Offset all assigned loopback IPv6 addresses.<br>Required when the < loopback_ipv6_pool > is same for 2 different node_types (like spine and l3leaf) to avoid overlapping IPs.<br>For example, set the minimum offset l3leaf.defaults.loopback_ipv6_offset: < total # spine switches > or vice versa.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vtep_loopback</samp>](## "&lt;node_type_keys.key&gt;.defaults.vtep_loopback") | String |  |  | Pattern: Loopback[\d/]+ | Set VXLAN source interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;bgp_as</samp>](## "&lt;node_type_keys.key&gt;.defaults.bgp_as") | String |  |  |  | Required with eBGP. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;bgp_defaults</samp>](## "&lt;node_type_keys.key&gt;.defaults.bgp_defaults") | List, items: String |  |  |  | List of EOS commands to apply to BGP daemon. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.defaults.bgp_defaults.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;evpn_role</samp>](## "&lt;node_type_keys.key&gt;.defaults.evpn_role") | String |  |  | Valid Values:<br>- client<br>- server<br>- none | Acting role in EVPN control plane. Default is set in node_type definition from node_type_keys. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;evpn_route_servers</samp>](## "&lt;node_type_keys.key&gt;.defaults.evpn_route_servers") | List, items: String |  |  |  | List of nodes acting as EVPN Route-Servers / Route-Reflectors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.defaults.evpn_route_servers.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;evpn_services_l2_only</samp>](## "&lt;node_type_keys.key&gt;.defaults.evpn_services_l2_only") | Boolean |  | False |  | Possibility to prevent configuration of Tenant VRFs and SVIs.<br>Override node definition "network_services_l3" from node_type_keys.<br>This allows support for centralized routing.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;filter</samp>](## "&lt;node_type_keys.key&gt;.defaults.filter") | Dictionary |  |  |  | Filter L3 and L2 network services based on tenant and tags (and operation filter).<br>If filter is not defined it will default to all.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tenants</samp>](## "&lt;node_type_keys.key&gt;.defaults.filter.tenants") | List, items: String |  | ['all'] |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.defaults.filter.tenants.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tags</samp>](## "&lt;node_type_keys.key&gt;.defaults.filter.tags") | List, items: String |  | ['all'] |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.defaults.filter.tags.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;always_include_vrfs_in_tenants</samp>](## "&lt;node_type_keys.key&gt;.defaults.filter.always_include_vrfs_in_tenants") | List, items: String |  |  |  | List of tenants where VRFs will be configured even if VLANs are not included in tags<br>Useful for L3 "border" leaf.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.defaults.filter.always_include_vrfs_in_tenants.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;only_vlans_in_use</samp>](## "&lt;node_type_keys.key&gt;.defaults.filter.only_vlans_in_use") | Boolean |  | False |  | Only configure VLANs, SVIs, VRFs in use by connected endpoints or downstream L2 switches.<br>Note! This feature only considers configuration managed by eos_designs.<br>This excludes structured_config, custom_structured_configuration_, raw_eos_cli, eos_cli, custom templates, configlets etc.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;igmp_snooping_enabled</samp>](## "&lt;node_type_keys.key&gt;.defaults.igmp_snooping_enabled") | Boolean |  | True |  | Activate or deactivate IGMP snooping on device level. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;evpn_gateway</samp>](## "&lt;node_type_keys.key&gt;.defaults.evpn_gateway") | Dictionary |  |  |  | Node is acting as EVPN Multi-Domain Gateway.<br>New BGP peer-group is generated between EVPN GWs in different domains or between GWs and Route Servers.<br>Name can be changed under "bgp_peer_groups.evpn_overlay_core" variable.<br>L3 rechability for different EVPN GWs must be already in place, it is recommended to use DCI & L3 Edge if Route Servers and GWs are not defined under the same Ansible inventory.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remote_peers</samp>](## "&lt;node_type_keys.key&gt;.defaults.evpn_gateway.remote_peers") | List, items: Dictionary |  |  |  | Define remote peers of the EVPN VXLAN Gateway.<br>If the hostname can be found in the inventory, ip_address and BGP ASN will be automatically populated. Manual override takes precedence.<br>If the peer's hostname can not be found in the inventory, ip_address and bgp_as must be defined.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- hostname</samp>](## "&lt;node_type_keys.key&gt;.defaults.evpn_gateway.remote_peers.[].hostname") | String |  |  |  | Hostname of remote EVPN GW server. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "&lt;node_type_keys.key&gt;.defaults.evpn_gateway.remote_peers.[].ip_address") | String |  |  | Format: ipv4 | Peering IP of remote Route Server. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp_as</samp>](## "&lt;node_type_keys.key&gt;.defaults.evpn_gateway.remote_peers.[].bgp_as") | String |  |  |  | BGP ASN of remote Route Server. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_l2</samp>](## "&lt;node_type_keys.key&gt;.defaults.evpn_gateway.evpn_l2") | Dictionary |  |  |  | Enable EVPN Gateway functionality for route-types 2 (MAC-IP) and 3 (IMET). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;node_type_keys.key&gt;.defaults.evpn_gateway.evpn_l2.enabled") | Boolean |  | False |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_l3</samp>](## "&lt;node_type_keys.key&gt;.defaults.evpn_gateway.evpn_l3") | Dictionary |  |  |  | Enable EVPN Gateway functionality for route-type 5 (IP-PREFIX). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;node_type_keys.key&gt;.defaults.evpn_gateway.evpn_l3.enabled") | Boolean |  | False |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inter_domain</samp>](## "&lt;node_type_keys.key&gt;.defaults.evpn_gateway.evpn_l3.inter_domain") | Boolean |  | True |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipvpn_gateway</samp>](## "&lt;node_type_keys.key&gt;.defaults.ipvpn_gateway") | Dictionary |  |  |  | Node is acting as IP-VPN Gateway for EVPN to MPLS-IP-VPN Interworking. The BGP peer group used for this is "bgp_peer_groups.ipvpn_gateway_peers".<br>L3 Reachability is required for this to work, the preferred method to establish underlay connectivity is to use core_interfaces.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;node_type_keys.key&gt;.defaults.ipvpn_gateway.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_domain_id</samp>](## "&lt;node_type_keys.key&gt;.defaults.ipvpn_gateway.evpn_domain_id") | String |  | 65535:1 |  | Domain ID to assign to EVPN address family for use with D-path. Format <nn>:<nn>. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipvpn_domain_id</samp>](## "&lt;node_type_keys.key&gt;.defaults.ipvpn_gateway.ipvpn_domain_id") | String |  | 65535:2 |  | Domain ID to assign to IPVPN address families for use with D-path. Format <nn>:<nn>. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enable_d_path</samp>](## "&lt;node_type_keys.key&gt;.defaults.ipvpn_gateway.enable_d_path") | Boolean |  | True |  | Enable D-path for use with BGP bestpath selection algorithm. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maximum_routes</samp>](## "&lt;node_type_keys.key&gt;.defaults.ipvpn_gateway.maximum_routes") | Integer |  | 0 |  | Maximum routes to accept from IPVPN remote peers. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;local_as</samp>](## "&lt;node_type_keys.key&gt;.defaults.ipvpn_gateway.local_as") | String |  | none |  | Apply local-as to peering with IPVPN remote peers. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;address_families</samp>](## "&lt;node_type_keys.key&gt;.defaults.ipvpn_gateway.address_families") | List, items: String |  | ['vpn-ipv4'] |  | IPVPN address families to enable for remote peers. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.defaults.ipvpn_gateway.address_families.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remote_peers</samp>](## "&lt;node_type_keys.key&gt;.defaults.ipvpn_gateway.remote_peers") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- hostname</samp>](## "&lt;node_type_keys.key&gt;.defaults.ipvpn_gateway.remote_peers.[].hostname") | String | Required |  |  | Hostname of remote IPVPN Peer. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "&lt;node_type_keys.key&gt;.defaults.ipvpn_gateway.remote_peers.[].ip_address") | String | Required |  | Format: ipv4 | Peering IP of remote IPVPN Peer. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp_as</samp>](## "&lt;node_type_keys.key&gt;.defaults.ipvpn_gateway.remote_peers.[].bgp_as") | String | Required |  |  | BGP ASN of remote IPVPN Peer. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mlag</samp>](## "&lt;node_type_keys.key&gt;.defaults.mlag") | Boolean |  | True |  | Enable / Disable auto MLAG, when two nodes are defined in node group. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mlag_dual_primary_detection</samp>](## "&lt;node_type_keys.key&gt;.defaults.mlag_dual_primary_detection") | Boolean |  | False |  | Enable / Disable MLAG dual primary detection. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mlag_ibgp_origin_incomplete</samp>](## "&lt;node_type_keys.key&gt;.defaults.mlag_ibgp_origin_incomplete") | Boolean |  | True |  | Set origin of routes received from MLAG iBGP peer to incomplete.<br>The purpose is to optimize routing for leaf loopbacks from spine perspective and<br>avoid suboptimal routing via peerlink for control plane traffic.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mlag_interfaces</samp>](## "&lt;node_type_keys.key&gt;.defaults.mlag_interfaces") | List, items: String |  |  |  | Each list item supports range syntax that can be expanded into a list of interfaces.<br>Required when MLAG leafs are present in the topology.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.defaults.mlag_interfaces.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mlag_interfaces_speed</samp>](## "&lt;node_type_keys.key&gt;.defaults.mlag_interfaces_speed") | String |  |  |  | Set MLAG interface speed.<br>< interface_speed or forced interface_speed or auto interface_speed >.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mlag_peer_l3_vlan</samp>](## "&lt;node_type_keys.key&gt;.defaults.mlag_peer_l3_vlan") | Integer |  | 4093 | Min: 0<br>Max: 4094 | Underlay L3 peering SVI interface id.<br>If set to 0 or the same vlan as mlag_peer_vlan, the mlag_peer_vlan will be used for L3 peering.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mlag_peer_l3_ipv4_pool</samp>](## "&lt;node_type_keys.key&gt;.defaults.mlag_peer_l3_ipv4_pool") | String |  |  | Format: ipv4_cidr | IP address pool used for MLAG underlay L3 peering. IP is derived from the node id.<br>Required when MLAG leafs present in topology and they are using a separate L3 peering VLAN.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mlag_peer_vlan</samp>](## "&lt;node_type_keys.key&gt;.defaults.mlag_peer_vlan") | Integer |  | 4094 | Min: 1<br>Max: 4094 | MLAG Peer Link (control link) SVI interface id. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mlag_peer_link_allowed_vlans</samp>](## "&lt;node_type_keys.key&gt;.defaults.mlag_peer_link_allowed_vlans") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mlag_peer_ipv4_pool</samp>](## "&lt;node_type_keys.key&gt;.defaults.mlag_peer_ipv4_pool") | String |  |  | Format: ipv4_cidr | IP address pool used for MLAG Peer Link (control link). IP is derived from the node id.<br>Required when MLAG leafs present in topology.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mlag_port_channel_id</samp>](## "&lt;node_type_keys.key&gt;.defaults.mlag_port_channel_id") | Integer |  |  |  | If not set, the mlag port-channel id is generated based on the digits of the first interface present in 'mlag_interfaces'.<br>Valid port-channel id numbers are < 1-2000 > for EOS < 4.25.0F and < 1 - 999999 > for EOS >= 4.25.0F.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mlag_domain_id</samp>](## "&lt;node_type_keys.key&gt;.defaults.mlag_domain_id") | String |  |  |  | MLAG Domain ID. If not set the node group name (Set with "group" key) will be used. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_mode</samp>](## "&lt;node_type_keys.key&gt;.defaults.spanning_tree_mode") | String |  |  | Valid Values:<br>- mstp<br>- rstp<br>- rapid-pvst<br>- none |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_priority</samp>](## "&lt;node_type_keys.key&gt;.defaults.spanning_tree_priority") | Integer |  | 32768 |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_root_super</samp>](## "&lt;node_type_keys.key&gt;.defaults.spanning_tree_root_super") | Boolean |  | False |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;virtual_router_mac_address</samp>](## "&lt;node_type_keys.key&gt;.defaults.virtual_router_mac_address") | String |  |  | Format: mac | Virtual router mac address for anycast gateway. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;inband_mgmt_interface</samp>](## "&lt;node_type_keys.key&gt;.defaults.inband_mgmt_interface") | String |  |  |  | Pointer to interface used for inband management.<br>All configuration must be done using other data models like network services or structured_config.<br>'inband_mgmt_interface' is only used to refer to this interface as source in various management protocol settings (future feature).<br><br>On L2 switches, this defaults to Vlan<inband_mgmt_vlan> if either 'inband_mgmt_subnet' or 'inband_mgmt_ip' is set.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;inband_mgmt_vlan</samp>](## "&lt;node_type_keys.key&gt;.defaults.inband_mgmt_vlan") | Integer |  | 4092 |  | VLAN number used for inband management on L2 switches (switches using port-channel trunks as uplinks).<br>When using 'inband_mgmt_subnet' the VLAN and SVIs will be created automatically on this switch as well as all 'uplink_switches'.<br>When using 'inband_mgmt_ip' the VLAN and SVI will only be created on this device and added to uplink trunk. The VLAN and SVI on the parent switches must be created using network services data models. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;inband_mgmt_subnet</samp>](## "&lt;node_type_keys.key&gt;.defaults.inband_mgmt_subnet") | String |  |  | Format: ipv4_cidr | Optional IP subnet assigned to inband management SVIs on L2 switches (switches using port-channels as uplinks).<br>Parent l3leafs will have SVI with "ip virtual-router" and host-route injection based on ARP.<br>This allows all l3leafs to reuse the same subnet across multiple racks without VXLAN extension.<br>SVI IP address will be assigned as follows:<br>virtual-router: <subnet> + 1<br>l3leaf A      : <subnet> + 2 (same IP on all l3leaf A)<br>l3leaf B      : <subnet> + 3 (same IP on all l3leaf B)<br>l2leafs       : <subnet> + 3 + <l2leaf id><br>GW on l2leafs : <subnet> + 1<br>Assign range larger than total l2leafs + 5<br><br>Setting is ignored if 'inband_mgmt_ip' is set.<br><br>This setting is applicable to L2 switches (switches using port-channel trunks as uplinks).<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;inband_mgmt_ip</samp>](## "&lt;node_type_keys.key&gt;.defaults.inband_mgmt_ip") | String |  |  | Format: ipv4_cidr | IP address assigned to the inband management interface set with 'inband_mgmt_vlan'.<br>This overrides 'inband_mgmt_subnet', hence all behavior of 'inband_mgmt_subnet' is removed.<br><br>If this is set the VLAN and SVI will only be created on the L2 switch and added to uplink trunk.<br>The VLAN and SVI on the parent switches must be created using network services data models.<br><br>This setting is applicable to L2 switches (switches using port-channel trunks as uplinks).<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;inband_mgmt_gateway</samp>](## "&lt;node_type_keys.key&gt;.defaults.inband_mgmt_gateway") | String |  |  | Format: ipv4 | Default gateway configured in the 'inband_mgmt_vrf' when using 'inband_mgmt_ip'. Otherwise gateway is derived from 'inband_mgmt_subnet' if set.<br><br>This setting is applicable to L2 switches (switches using port-channel trunks as uplinks).<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;inband_mgmt_description</samp>](## "&lt;node_type_keys.key&gt;.defaults.inband_mgmt_description") | String |  | Inband Management |  | Description configured on the Inband Management SVI.<br><br>This setting is only applied on the devices where it is set, it does not automatically affect any parent/child devices configuration, so it must be set on each applicable node/node-group/node-type as needed. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;inband_mgmt_vlan_name</samp>](## "&lt;node_type_keys.key&gt;.defaults.inband_mgmt_vlan_name") | String |  | Inband Management |  | Name configured on the Inband Management VLAN.<br>This setting is only applied on the devices where it is set, it does not automatically affect any parent/child devices configuration, so it must be set on each applicable node/node-group/node-type as needed. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;inband_mgmt_vrf</samp>](## "&lt;node_type_keys.key&gt;.defaults.inband_mgmt_vrf") | String |  | default |  | VRF configured on the Inband Management Interface.<br>The VRF is created if not already created by other means.<br>This setting is only applied on the devices where it is set, it does not automatically affect any parent/child devices configuration, so it must be set on each applicable node/node-group/node-type as needed. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;inband_mgmt_mtu</samp>](## "&lt;node_type_keys.key&gt;.defaults.inband_mgmt_mtu") | Integer |  | 1500 |  | MTU configured on the Inband Management Interface.<br>This setting is only applied on the devices where it is set, it does not automatically affect any parent/child devices configuration, so it must be set on each applicable node/node-group/node-type as needed. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;inband_management_subnet</samp>](## "&lt;node_type_keys.key&gt;.defaults.inband_management_subnet") <span style="color:red">deprecated</span> | String |  |  | Format: ipv4_cidr | Optional IP subnet assigned to inband management SVIs on L2 switches (switches using port-channels as uplinks).<br>Parent l3leafs will have SVI with "ip virtual-router" and host-route injection based on ARP.<br>This allows all l3leafs to reuse the same subnet across multiple racks without VXLAN extension.<br>SVI IP address will be assigned as follows:<br>virtual-router: <subnet> + 1<br>l3leaf A      : <subnet> + 2 (same IP on all l3leaf A)<br>l3leaf B      : <subnet> + 3 (same IP on all l3leaf B)<br>l2leafs       : <subnet> + 3 + <l2leaf id><br>GW on l2leafs : <subnet> + 1<br>Assign range larger than total l2leafs + 5<br><br>Setting is ignored if 'inband_mgmt_ip' is set.<br><br>This setting is applicable to L2 switches (switches using port-channel trunks as uplinks).<br><span style="color:red">This key is deprecated. Support will be removed in AVD version 5.0.0. Use <samp>inband_mgmt_subnet</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;inband_management_vlan</samp>](## "&lt;node_type_keys.key&gt;.defaults.inband_management_vlan") <span style="color:red">deprecated</span> | Integer |  | 4092 |  | VLAN number used for inband management on L2 switches (switches using port-channel trunks as uplinks).<br>When using 'inband_mgmt_subnet' the VLAN and SVIs will be created automatically on this switch as well as all 'uplink_switches'.<br>When using 'inband_mgmt_ip' the VLAN and SVI will only be created on this device and added to uplink trunk. The VLAN and SVI on the parent switches must be created using network services data models.<span style="color:red">This key is deprecated. Support will be removed in AVD version 5.0.0. Use <samp>inband_mgmt_vlan</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mpls_overlay_role</samp>](## "&lt;node_type_keys.key&gt;.defaults.mpls_overlay_role") | String |  |  | Valid Values:<br>- client<br>- server<br>- none | Set the default mpls overlay role.<br>Acting role in overlay control plane.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;overlay_address_families</samp>](## "&lt;node_type_keys.key&gt;.defaults.overlay_address_families") | List, items: String |  |  |  | Set the default overlay address families.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.defaults.overlay_address_families.[].&lt;str&gt;") | String |  |  | Valid Values:<br>- evpn<br>- vpn-ipv4<br>- vpn-ipv6 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mpls_route_reflectors</samp>](## "&lt;node_type_keys.key&gt;.defaults.mpls_route_reflectors") | List, items: String |  |  |  | List of inventory hostname acting as MPLS route-reflectors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.defaults.mpls_route_reflectors.[].&lt;str&gt;") | String |  |  |  | Inventory_hostname_of_mpls_route_reflectors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;bgp_cluster_id</samp>](## "&lt;node_type_keys.key&gt;.defaults.bgp_cluster_id") | String |  |  |  | Set BGP cluster id. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ptp</samp>](## "&lt;node_type_keys.key&gt;.defaults.ptp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;node_type_keys.key&gt;.defaults.ptp.enabled") | Boolean |  | False |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;profile</samp>](## "&lt;node_type_keys.key&gt;.defaults.ptp.profile") | String |  | aes67-r16-2016 | Valid Values:<br>- aes67<br>- smpte2059-2<br>- aes67-r16-2016 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;domain</samp>](## "&lt;node_type_keys.key&gt;.defaults.ptp.domain") | Integer |  | 127 | Min: 0<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority1</samp>](## "&lt;node_type_keys.key&gt;.defaults.ptp.priority1") | Integer |  |  | Min: 0<br>Max: 255 | default -> automatically set based on node_type.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority2</samp>](## "&lt;node_type_keys.key&gt;.defaults.ptp.priority2") | Integer |  |  | Min: 0<br>Max: 255 | default -> (node_id modulus 256).<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;auto_clock_identity</samp>](## "&lt;node_type_keys.key&gt;.defaults.ptp.auto_clock_identity") | Boolean |  | True |  | If you prefer to have PTP clock identity be the system MAC-address of the switch, which is the default EOS behaviour, simply disable the automatic PTP clock identity.<br>default -> (clock_identity_prefix = 00:1C:73 (default)) + (PTP priority 1 as HEX) + ":00:" + (PTP priority 2 as HEX).<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;clock_identity_prefix</samp>](## "&lt;node_type_keys.key&gt;.defaults.ptp.clock_identity_prefix") | String |  |  |  | PTP clock idetentiy 3-byte prefix. i.e. "01:02:03".<br>By default the 3-byte prefix is "00:1C:73".<br>This can be overridden if auto_clock_identity is set to true (which is the default).<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;clock_identity</samp>](## "&lt;node_type_keys.key&gt;.defaults.ptp.clock_identity") | String |  |  |  | Set PTP clock identity manually. 6-byte value i.e. "01:02:03:04:05:06".<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_ip</samp>](## "&lt;node_type_keys.key&gt;.defaults.ptp.source_ip") | String |  |  |  | By default in EOS, PTP packets are sourced with an IP address from the routed port or from the relevant SVI, which is the recommended behaviour.<br>This can be set manually if required, for example, to a value of "10.1.2.3".<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ttl</samp>](## "&lt;node_type_keys.key&gt;.defaults.ptp.ttl") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;forward_unicast</samp>](## "&lt;node_type_keys.key&gt;.defaults.ptp.forward_unicast") | Boolean |  | False |  | Enable PTP unicast forwarding.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dscp</samp>](## "&lt;node_type_keys.key&gt;.defaults.ptp.dscp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;general_messages</samp>](## "&lt;node_type_keys.key&gt;.defaults.ptp.dscp.general_messages") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;event_messages</samp>](## "&lt;node_type_keys.key&gt;.defaults.ptp.dscp.event_messages") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;monitor</samp>](## "&lt;node_type_keys.key&gt;.defaults.ptp.monitor") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;node_type_keys.key&gt;.defaults.ptp.monitor.enabled") | Boolean |  | True |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;threshold</samp>](## "&lt;node_type_keys.key&gt;.defaults.ptp.monitor.threshold") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;offset_from_master</samp>](## "&lt;node_type_keys.key&gt;.defaults.ptp.monitor.threshold.offset_from_master") | Integer |  | 250 | Min: 0<br>Max: 1000000000 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mean_path_delay</samp>](## "&lt;node_type_keys.key&gt;.defaults.ptp.monitor.threshold.mean_path_delay") | Integer |  | 1500 | Min: 0<br>Max: 1000000000 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;drop</samp>](## "&lt;node_type_keys.key&gt;.defaults.ptp.monitor.threshold.drop") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;offset_from_master</samp>](## "&lt;node_type_keys.key&gt;.defaults.ptp.monitor.threshold.drop.offset_from_master") | Integer |  |  | Min: 0<br>Max: 1000000000 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mean_path_delay</samp>](## "&lt;node_type_keys.key&gt;.defaults.ptp.monitor.threshold.drop.mean_path_delay") | Integer |  |  | Min: 0<br>Max: 1000000000 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;missing_message</samp>](## "&lt;node_type_keys.key&gt;.defaults.ptp.monitor.missing_message") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;intervals</samp>](## "&lt;node_type_keys.key&gt;.defaults.ptp.monitor.missing_message.intervals") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;announce</samp>](## "&lt;node_type_keys.key&gt;.defaults.ptp.monitor.missing_message.intervals.announce") | Integer |  |  | Min: 2<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;follow_up</samp>](## "&lt;node_type_keys.key&gt;.defaults.ptp.monitor.missing_message.intervals.follow_up") | Integer |  |  | Min: 2<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sync</samp>](## "&lt;node_type_keys.key&gt;.defaults.ptp.monitor.missing_message.intervals.sync") | Integer |  |  | Min: 2<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sequence_ids</samp>](## "&lt;node_type_keys.key&gt;.defaults.ptp.monitor.missing_message.sequence_ids") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;node_type_keys.key&gt;.defaults.ptp.monitor.missing_message.sequence_ids.enabled") | Boolean |  | True |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;announce</samp>](## "&lt;node_type_keys.key&gt;.defaults.ptp.monitor.missing_message.sequence_ids.announce") | Integer |  | 3 | Min: 2<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;delay_resp</samp>](## "&lt;node_type_keys.key&gt;.defaults.ptp.monitor.missing_message.sequence_ids.delay_resp") | Integer |  | 3 | Min: 2<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;follow_up</samp>](## "&lt;node_type_keys.key&gt;.defaults.ptp.monitor.missing_message.sequence_ids.follow_up") | Integer |  | 3 | Min: 2<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sync</samp>](## "&lt;node_type_keys.key&gt;.defaults.ptp.monitor.missing_message.sequence_ids.sync") | Integer |  | 3 | Min: 2<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;node_groups</samp>](## "&lt;node_type_keys.key&gt;.node_groups") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- group</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].group") | String | Required, Unique |  |  | The Node Group Name is used for MLAG domain unless set with 'mlag_domain_id'.<br>The Node Group Name is also used for peer description on downstream switches' uplinks.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].name") | String | Required, Unique |  |  | The Node Name is used as "hostname". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;id</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].id") | Integer |  |  |  | Unique identifier used for IP addressing and other algorithms. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;platform</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].platform") | String |  |  |  | Arista platform family. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mac_address</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].mac_address") | String |  |  |  | Leverage to document management interface mac address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;system_mac_address</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].system_mac_address") | String |  |  |  | System MAC Address in this following format: "xx:xx:xx:xx:xx:xx".<br>Set to the same MAC address as available in "show version" on the device.<br>"system_mac_address" can also be set directly as a hostvar.<br>If both are set, the setting under "Fabric Topology" takes precedence.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;serial_number</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].serial_number") | String |  |  |  | Set to the Serial Number of the device<br>For  now only used for documentation purpose in the fabric documentation<br>and part of the structured_config<br>"serial_number" can also be set directly as a hostvar.<br>If both are set, the setting under "Fabric Topology" takes precedence.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rack</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].rack") | String |  |  |  | Rack that the switch is located in (only used in snmp_settings location). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mgmt_ip</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].mgmt_ip") | String |  |  | Format: cidr | Node management interface IPv4 address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_mgmt_ip</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ipv6_mgmt_ip") | String |  |  | Format: cidr | Node management interface IPv6 address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mgmt_interface</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].mgmt_interface") | String |  |  |  | Management Interface Name.<br>Default -> platform_management_interface -> mgmt_interface -> "Management1".<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;link_tracking</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].link_tracking") | Dictionary |  |  |  | This configures the Link Tracking Group on a switch as well as adds the p2p-uplinks of the switch as the upstream interfaces.<br>Useful in EVPN multhoming designs.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].link_tracking.enabled") | Boolean |  | False |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;groups</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].link_tracking.groups") | List, items: Dictionary |  | [{'name': 'LT_GROUP1'}] |  | Link Tracking Groups.<br>By default a single group named "LT_GROUP1" is defined with default values.<br>Any groups defined under "groups" will replace the default.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].link_tracking.groups.[].name") | String |  |  |  | Tracking group name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;recovery_delay</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].link_tracking.groups.[].recovery_delay") | Integer |  |  | Min: 0<br>Max: 3600 | default -> platform_settings_mlag_reload_delay -> 300. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;links_minimum</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].link_tracking.groups.[].links_minimum") | Integer |  |  | Min: 1<br>Max: 100000 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;lacp_port_id_range</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].lacp_port_id_range") | Dictionary |  |  |  | This will generate the "lacp port-id range", "begin" and "end" values based on node "id" and the number of nodes in the "node_group".<br>Unique LACP port-id ranges are recommended for EVPN Multihoming designs.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].lacp_port_id_range.enabled") | Boolean |  | False |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;size</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].lacp_port_id_range.size") | Integer |  | 128 |  | Recommended size > = number of ports in the switch. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;offset</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].lacp_port_id_range.offset") | Integer |  | 0 |  | Offset is used to avoid overlapping port-id ranges of different switches.<br>Useful when a "connected-endpoint" is connected to switches in different "node_groups".<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;always_configure_ip_routing</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].always_configure_ip_routing") | Boolean |  | False |  | Force configuration of "ip routing" even on L2 devices.<br>Use this to retain behavior of AVD versions below 4.0.0.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the root level of the final EOS configuration. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].structured_config") | Dictionary |  |  |  | Custom structured config for eos_cli_config_gen. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_ipv4_pool</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].uplink_ipv4_pool") | String |  |  | Format: ipv4_cidr | IPv4 subnet to use to connect to uplink switches. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_interfaces</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].uplink_interfaces") | List, items: String |  |  |  | Local uplink interfaces<br>Each list item supports range syntax that can be expanded into a list of interfaces.<br>If uplink_interfaces is not defined, platform-specific defaults (defined under default_interfaces) will be used instead.<br>Please note that default_interfaces are not defined by default, you should define these yourself.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].uplink_interfaces.[].&lt;str&gt;") | String |  |  | Pattern: Ethernet[\d/]+ |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_switch_interfaces</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].uplink_switch_interfaces") | List, items: String |  |  |  | Interfaces located on uplink switches |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].uplink_switch_interfaces.[].&lt;str&gt;") | String |  |  | Pattern: Ethernet[\d/]+ |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_switches</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].uplink_switches") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].uplink_switches.[].&lt;str&gt;") | String | Required |  |  | Hostname of uplink switch.<br>If parallel uplinks are in use, update max_parallel_uplinks below and specify each uplink switch multiple times.<br>e.g. uplink_switches: [ 'DC1-SPINE1', 'DC1-SPINE1', 'DC1-SPINE2', 'DC1-SPINE2' ].<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_interface_speed</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].uplink_interface_speed") | String |  |  |  | Set point-to-Point interface speed and will apply to uplink interfaces on both ends.<br>interface_speed or forced interface_speed or auto interface_speed.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;max_uplink_switches</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].max_uplink_switches") | Integer |  |  |  | Maximum number of uplink switches.<br>Changing this value may change IP Addressing on uplinks.<br>Can be used to reserve IP space for future expansions.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;max_parallel_uplinks</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].max_parallel_uplinks") | Integer |  |  |  | Number of parallel links towards uplink switches.<br>Changing this value may change interface naming on uplinks (and corresponding downlinks).<br>Can be used to reserve interfaces for future parallel uplinks.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_bfd</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].uplink_bfd") | Boolean |  | False |  | Enable bfd on uplink interfaces. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_native_vlan</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].uplink_native_vlan") | Integer |  |  | Min: 1<br>Max: 4094 | Only applicable to switches with layer-2 port-channel uplinks.<br>A suspended (disabled) vlan will be created in both ends of the link unless the vlan is defined under network services.<br>By default the uplink will not have a native_vlan configured, so EOS defaults to vlan 1.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_ptp</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].uplink_ptp") | Dictionary |  |  |  | Enable PTP on all infrastructure links. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enable</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].uplink_ptp.enable") | Boolean |  | False |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_macsec</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].uplink_macsec") | Dictionary |  |  |  | Enable MacSec on all uplinks. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;profile</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].uplink_macsec.profile") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_structured_config</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].uplink_structured_config") | Dictionary |  |  |  | Custom structured config applied to "uplink_interfaces", and "uplink_switch_interfaces".<br>When uplink_type == "p2p", custom structured config added under ethernet_interfaces.<interface> for eos_cli_config_gen overrides the settings on the ethernet interface level.<br>When uplink_type == "port-channel", custom structured config added under port_channel_interfaces.<interface> for eos_cli_config_gen overrides the settings on the port-channel interface level.<br>"uplink_structured_config" is applied after "structured_config", so it can override "structured_config" defined on node-level.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_port_channel_structured_config</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].mlag_port_channel_structured_config") | Dictionary |  |  |  | Custom structured config applied to MLAG peer link port-channel id.<br>Added under port_channel_interfaces.<interface> for eos_cli_config_gen.<br>Overrides the settings on the port-channel interface level.<br>"mlag_port_channel_structured_config" is applied after "structured_config", so it can override "structured_config" defined on node-level.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_peer_vlan_structured_config</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].mlag_peer_vlan_structured_config") | Dictionary |  |  |  | Custom structured config applied to MLAG Peer Link (control link) SVI interface id.<br>Added under vlan_interfaces.<interface> for eos_cli_config_gen.<br>Overrides the settings on the vlan interface level.<br>"mlag_peer_vlan_structured_config" is applied after "structured_config", so it can override "structured_config" defined on node-level.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_peer_l3_vlan_structured_config</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].mlag_peer_l3_vlan_structured_config") | Dictionary |  |  |  | Custom structured config applied to MLAG underlay L3 peering SVI interface id.<br>Added under vlan_interfaces.<interface> for eos_cli_config_gen.<br>Overrides the settings on the vlan interface level.<br>"mlag_peer_l3_vlan_structured_config" is applied after "structured_config", so it can override "structured_config" defined on node-level.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;short_esi</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].short_esi") | String |  |  |  | short_esi only valid for l2leaf devices using port-channel uplink.<br>Setting short_esi to "auto" generates the short_esi automatically using a hash of configuration elements.<br>< 0000:0000:0000 | auto >.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_system_id_prefix</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].isis_system_id_prefix") | String |  |  | Pattern: [0-9a-f]{4}\.[0-9a-f]{4} | (4.4 hexadecimal). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_maximum_paths</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].isis_maximum_paths") | Integer |  |  |  | Number of path to configure in ECMP for ISIS. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;is_type</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].is_type") | String |  | level-2 | Valid Values:<br>- level-1-2<br>- level-1<br>- level-2 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;node_sid_base</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].node_sid_base") | Integer |  | 0 |  | Node-SID base for isis-sr underlay variants. Combined with node id to generate ISIS-SR node-SID. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loopback_ipv4_pool</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].loopback_ipv4_pool") | String |  |  | Format: ipv4_cidr | IPv4 subnet for Loopback0 allocation. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vtep_loopback_ipv4_pool</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].vtep_loopback_ipv4_pool") | String |  |  | Format: ipv4_cidr | IPv4 subnet for VTEP-Loopback allocation. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loopback_ipv4_offset</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].loopback_ipv4_offset") | Integer |  | 0 |  | Offset all assigned loopback IP addresses.<br>Required when the < loopback_ipv4_pool > is same for 2 different node_types (like spine and l3leaf) to avoid over-lapping IPs.<br>For example, set the minimum offset l3leaf.defaults.loopback_ipv4_offset: < total # spine switches > or vice versa.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loopback_ipv6_pool</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].loopback_ipv6_pool") | String |  |  | Format: ipv6_cidr | IPv6 subnet for Loopback0 allocation. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loopback_ipv6_offset</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].loopback_ipv6_offset") | Integer |  | 0 |  | Offset all assigned loopback IPv6 addresses.<br>Required when the < loopback_ipv6_pool > is same for 2 different node_types (like spine and l3leaf) to avoid overlapping IPs.<br>For example, set the minimum offset l3leaf.defaults.loopback_ipv6_offset: < total # spine switches > or vice versa.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vtep_loopback</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].vtep_loopback") | String |  |  | Pattern: Loopback[\d/]+ | Set VXLAN source interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp_as</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].bgp_as") | String |  |  |  | Required with eBGP. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp_defaults</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].bgp_defaults") | List, items: String |  |  |  | List of EOS commands to apply to BGP daemon. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].bgp_defaults.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_role</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].evpn_role") | String |  |  | Valid Values:<br>- client<br>- server<br>- none | Acting role in EVPN control plane. Default is set in node_type definition from node_type_keys. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_route_servers</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].evpn_route_servers") | List, items: String |  |  |  | List of nodes acting as EVPN Route-Servers / Route-Reflectors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].evpn_route_servers.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_services_l2_only</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].evpn_services_l2_only") | Boolean |  | False |  | Possibility to prevent configuration of Tenant VRFs and SVIs.<br>Override node definition "network_services_l3" from node_type_keys.<br>This allows support for centralized routing.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;filter</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].filter") | Dictionary |  |  |  | Filter L3 and L2 network services based on tenant and tags (and operation filter).<br>If filter is not defined it will default to all.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tenants</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].filter.tenants") | List, items: String |  | ['all'] |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].filter.tenants.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tags</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].filter.tags") | List, items: String |  | ['all'] |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].filter.tags.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;always_include_vrfs_in_tenants</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].filter.always_include_vrfs_in_tenants") | List, items: String |  |  |  | List of tenants where VRFs will be configured even if VLANs are not included in tags<br>Useful for L3 "border" leaf.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].filter.always_include_vrfs_in_tenants.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;only_vlans_in_use</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].filter.only_vlans_in_use") | Boolean |  | False |  | Only configure VLANs, SVIs, VRFs in use by connected endpoints or downstream L2 switches.<br>Note! This feature only considers configuration managed by eos_designs.<br>This excludes structured_config, custom_structured_configuration_, raw_eos_cli, eos_cli, custom templates, configlets etc.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;igmp_snooping_enabled</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].igmp_snooping_enabled") | Boolean |  | True |  | Activate or deactivate IGMP snooping on device level. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_gateway</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].evpn_gateway") | Dictionary |  |  |  | Node is acting as EVPN Multi-Domain Gateway.<br>New BGP peer-group is generated between EVPN GWs in different domains or between GWs and Route Servers.<br>Name can be changed under "bgp_peer_groups.evpn_overlay_core" variable.<br>L3 rechability for different EVPN GWs must be already in place, it is recommended to use DCI & L3 Edge if Route Servers and GWs are not defined under the same Ansible inventory.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remote_peers</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].evpn_gateway.remote_peers") | List, items: Dictionary |  |  |  | Define remote peers of the EVPN VXLAN Gateway.<br>If the hostname can be found in the inventory, ip_address and BGP ASN will be automatically populated. Manual override takes precedence.<br>If the peer's hostname can not be found in the inventory, ip_address and bgp_as must be defined.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- hostname</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].evpn_gateway.remote_peers.[].hostname") | String |  |  |  | Hostname of remote EVPN GW server. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].evpn_gateway.remote_peers.[].ip_address") | String |  |  | Format: ipv4 | Peering IP of remote Route Server. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp_as</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].evpn_gateway.remote_peers.[].bgp_as") | String |  |  |  | BGP ASN of remote Route Server. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_l2</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].evpn_gateway.evpn_l2") | Dictionary |  |  |  | Enable EVPN Gateway functionality for route-types 2 (MAC-IP) and 3 (IMET). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].evpn_gateway.evpn_l2.enabled") | Boolean |  | False |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_l3</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].evpn_gateway.evpn_l3") | Dictionary |  |  |  | Enable EVPN Gateway functionality for route-type 5 (IP-PREFIX). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].evpn_gateway.evpn_l3.enabled") | Boolean |  | False |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inter_domain</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].evpn_gateway.evpn_l3.inter_domain") | Boolean |  | True |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipvpn_gateway</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ipvpn_gateway") | Dictionary |  |  |  | Node is acting as IP-VPN Gateway for EVPN to MPLS-IP-VPN Interworking. The BGP peer group used for this is "bgp_peer_groups.ipvpn_gateway_peers".<br>L3 Reachability is required for this to work, the preferred method to establish underlay connectivity is to use core_interfaces.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ipvpn_gateway.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_domain_id</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ipvpn_gateway.evpn_domain_id") | String |  | 65535:1 |  | Domain ID to assign to EVPN address family for use with D-path. Format <nn>:<nn>. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipvpn_domain_id</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ipvpn_gateway.ipvpn_domain_id") | String |  | 65535:2 |  | Domain ID to assign to IPVPN address families for use with D-path. Format <nn>:<nn>. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enable_d_path</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ipvpn_gateway.enable_d_path") | Boolean |  | True |  | Enable D-path for use with BGP bestpath selection algorithm. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maximum_routes</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ipvpn_gateway.maximum_routes") | Integer |  | 0 |  | Maximum routes to accept from IPVPN remote peers. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;local_as</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ipvpn_gateway.local_as") | String |  | none |  | Apply local-as to peering with IPVPN remote peers. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;address_families</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ipvpn_gateway.address_families") | List, items: String |  | ['vpn-ipv4'] |  | IPVPN address families to enable for remote peers. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ipvpn_gateway.address_families.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remote_peers</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ipvpn_gateway.remote_peers") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- hostname</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ipvpn_gateway.remote_peers.[].hostname") | String | Required |  |  | Hostname of remote IPVPN Peer. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ipvpn_gateway.remote_peers.[].ip_address") | String | Required |  | Format: ipv4 | Peering IP of remote IPVPN Peer. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp_as</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ipvpn_gateway.remote_peers.[].bgp_as") | String | Required |  |  | BGP ASN of remote IPVPN Peer. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].mlag") | Boolean |  | True |  | Enable / Disable auto MLAG, when two nodes are defined in node group. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_dual_primary_detection</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].mlag_dual_primary_detection") | Boolean |  | False |  | Enable / Disable MLAG dual primary detection. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_ibgp_origin_incomplete</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].mlag_ibgp_origin_incomplete") | Boolean |  | True |  | Set origin of routes received from MLAG iBGP peer to incomplete.<br>The purpose is to optimize routing for leaf loopbacks from spine perspective and<br>avoid suboptimal routing via peerlink for control plane traffic.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_interfaces</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].mlag_interfaces") | List, items: String |  |  |  | Each list item supports range syntax that can be expanded into a list of interfaces.<br>Required when MLAG leafs are present in the topology.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].mlag_interfaces.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_interfaces_speed</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].mlag_interfaces_speed") | String |  |  |  | Set MLAG interface speed.<br>< interface_speed or forced interface_speed or auto interface_speed >.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_peer_l3_vlan</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].mlag_peer_l3_vlan") | Integer |  | 4093 | Min: 0<br>Max: 4094 | Underlay L3 peering SVI interface id.<br>If set to 0 or the same vlan as mlag_peer_vlan, the mlag_peer_vlan will be used for L3 peering.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_peer_l3_ipv4_pool</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].mlag_peer_l3_ipv4_pool") | String |  |  | Format: ipv4_cidr | IP address pool used for MLAG underlay L3 peering. IP is derived from the node id.<br>Required when MLAG leafs present in topology and they are using a separate L3 peering VLAN.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_peer_vlan</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].mlag_peer_vlan") | Integer |  | 4094 | Min: 1<br>Max: 4094 | MLAG Peer Link (control link) SVI interface id. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_peer_link_allowed_vlans</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].mlag_peer_link_allowed_vlans") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_peer_ipv4_pool</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].mlag_peer_ipv4_pool") | String |  |  | Format: ipv4_cidr | IP address pool used for MLAG Peer Link (control link). IP is derived from the node id.<br>Required when MLAG leafs present in topology.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_port_channel_id</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].mlag_port_channel_id") | Integer |  |  |  | If not set, the mlag port-channel id is generated based on the digits of the first interface present in 'mlag_interfaces'.<br>Valid port-channel id numbers are < 1-2000 > for EOS < 4.25.0F and < 1 - 999999 > for EOS >= 4.25.0F.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_domain_id</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].mlag_domain_id") | String |  |  |  | MLAG Domain ID. If not set the node group name (Set with "group" key) will be used. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_mode</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].spanning_tree_mode") | String |  |  | Valid Values:<br>- mstp<br>- rstp<br>- rapid-pvst<br>- none |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_priority</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].spanning_tree_priority") | Integer |  | 32768 |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_root_super</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].spanning_tree_root_super") | Boolean |  | False |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;virtual_router_mac_address</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].virtual_router_mac_address") | String |  |  | Format: mac | Virtual router mac address for anycast gateway. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inband_mgmt_interface</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].inband_mgmt_interface") | String |  |  |  | Pointer to interface used for inband management.<br>All configuration must be done using other data models like network services or structured_config.<br>'inband_mgmt_interface' is only used to refer to this interface as source in various management protocol settings (future feature).<br><br>On L2 switches, this defaults to Vlan<inband_mgmt_vlan> if either 'inband_mgmt_subnet' or 'inband_mgmt_ip' is set.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inband_mgmt_vlan</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].inband_mgmt_vlan") | Integer |  | 4092 |  | VLAN number used for inband management on L2 switches (switches using port-channel trunks as uplinks).<br>When using 'inband_mgmt_subnet' the VLAN and SVIs will be created automatically on this switch as well as all 'uplink_switches'.<br>When using 'inband_mgmt_ip' the VLAN and SVI will only be created on this device and added to uplink trunk. The VLAN and SVI on the parent switches must be created using network services data models. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inband_mgmt_subnet</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].inband_mgmt_subnet") | String |  |  | Format: ipv4_cidr | Optional IP subnet assigned to inband management SVIs on L2 switches (switches using port-channels as uplinks).<br>Parent l3leafs will have SVI with "ip virtual-router" and host-route injection based on ARP.<br>This allows all l3leafs to reuse the same subnet across multiple racks without VXLAN extension.<br>SVI IP address will be assigned as follows:<br>virtual-router: <subnet> + 1<br>l3leaf A      : <subnet> + 2 (same IP on all l3leaf A)<br>l3leaf B      : <subnet> + 3 (same IP on all l3leaf B)<br>l2leafs       : <subnet> + 3 + <l2leaf id><br>GW on l2leafs : <subnet> + 1<br>Assign range larger than total l2leafs + 5<br><br>Setting is ignored if 'inband_mgmt_ip' is set.<br><br>This setting is applicable to L2 switches (switches using port-channel trunks as uplinks).<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inband_mgmt_ip</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].inband_mgmt_ip") | String |  |  | Format: ipv4_cidr | IP address assigned to the inband management interface set with 'inband_mgmt_vlan'.<br>This overrides 'inband_mgmt_subnet', hence all behavior of 'inband_mgmt_subnet' is removed.<br><br>If this is set the VLAN and SVI will only be created on the L2 switch and added to uplink trunk.<br>The VLAN and SVI on the parent switches must be created using network services data models.<br><br>This setting is applicable to L2 switches (switches using port-channel trunks as uplinks).<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inband_mgmt_gateway</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].inband_mgmt_gateway") | String |  |  | Format: ipv4 | Default gateway configured in the 'inband_mgmt_vrf' when using 'inband_mgmt_ip'. Otherwise gateway is derived from 'inband_mgmt_subnet' if set.<br><br>This setting is applicable to L2 switches (switches using port-channel trunks as uplinks).<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inband_mgmt_description</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].inband_mgmt_description") | String |  | Inband Management |  | Description configured on the Inband Management SVI.<br><br>This setting is only applied on the devices where it is set, it does not automatically affect any parent/child devices configuration, so it must be set on each applicable node/node-group/node-type as needed. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inband_mgmt_vlan_name</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].inband_mgmt_vlan_name") | String |  | Inband Management |  | Name configured on the Inband Management VLAN.<br>This setting is only applied on the devices where it is set, it does not automatically affect any parent/child devices configuration, so it must be set on each applicable node/node-group/node-type as needed. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inband_mgmt_vrf</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].inband_mgmt_vrf") | String |  | default |  | VRF configured on the Inband Management Interface.<br>The VRF is created if not already created by other means.<br>This setting is only applied on the devices where it is set, it does not automatically affect any parent/child devices configuration, so it must be set on each applicable node/node-group/node-type as needed. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inband_mgmt_mtu</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].inband_mgmt_mtu") | Integer |  | 1500 |  | MTU configured on the Inband Management Interface.<br>This setting is only applied on the devices where it is set, it does not automatically affect any parent/child devices configuration, so it must be set on each applicable node/node-group/node-type as needed. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inband_management_subnet</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].inband_management_subnet") <span style="color:red">deprecated</span> | String |  |  | Format: ipv4_cidr | Optional IP subnet assigned to inband management SVIs on L2 switches (switches using port-channels as uplinks).<br>Parent l3leafs will have SVI with "ip virtual-router" and host-route injection based on ARP.<br>This allows all l3leafs to reuse the same subnet across multiple racks without VXLAN extension.<br>SVI IP address will be assigned as follows:<br>virtual-router: <subnet> + 1<br>l3leaf A      : <subnet> + 2 (same IP on all l3leaf A)<br>l3leaf B      : <subnet> + 3 (same IP on all l3leaf B)<br>l2leafs       : <subnet> + 3 + <l2leaf id><br>GW on l2leafs : <subnet> + 1<br>Assign range larger than total l2leafs + 5<br><br>Setting is ignored if 'inband_mgmt_ip' is set.<br><br>This setting is applicable to L2 switches (switches using port-channel trunks as uplinks).<br><span style="color:red">This key is deprecated. Support will be removed in AVD version 5.0.0. Use <samp>inband_mgmt_subnet</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inband_management_vlan</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].inband_management_vlan") <span style="color:red">deprecated</span> | Integer |  | 4092 |  | VLAN number used for inband management on L2 switches (switches using port-channel trunks as uplinks).<br>When using 'inband_mgmt_subnet' the VLAN and SVIs will be created automatically on this switch as well as all 'uplink_switches'.<br>When using 'inband_mgmt_ip' the VLAN and SVI will only be created on this device and added to uplink trunk. The VLAN and SVI on the parent switches must be created using network services data models.<span style="color:red">This key is deprecated. Support will be removed in AVD version 5.0.0. Use <samp>inband_mgmt_vlan</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mpls_overlay_role</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].mpls_overlay_role") | String |  |  | Valid Values:<br>- client<br>- server<br>- none | Set the default mpls overlay role.<br>Acting role in overlay control plane.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;overlay_address_families</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].overlay_address_families") | List, items: String |  |  |  | Set the default overlay address families.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].overlay_address_families.[].&lt;str&gt;") | String |  |  | Valid Values:<br>- evpn<br>- vpn-ipv4<br>- vpn-ipv6 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mpls_route_reflectors</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].mpls_route_reflectors") | List, items: String |  |  |  | List of inventory hostname acting as MPLS route-reflectors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].mpls_route_reflectors.[].&lt;str&gt;") | String |  |  |  | Inventory_hostname_of_mpls_route_reflectors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp_cluster_id</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].bgp_cluster_id") | String |  |  |  | Set BGP cluster id. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ptp</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ptp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ptp.enabled") | Boolean |  | False |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;profile</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ptp.profile") | String |  | aes67-r16-2016 | Valid Values:<br>- aes67<br>- smpte2059-2<br>- aes67-r16-2016 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;domain</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ptp.domain") | Integer |  | 127 | Min: 0<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority1</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ptp.priority1") | Integer |  |  | Min: 0<br>Max: 255 | default -> automatically set based on node_type.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority2</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ptp.priority2") | Integer |  |  | Min: 0<br>Max: 255 | default -> (node_id modulus 256).<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;auto_clock_identity</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ptp.auto_clock_identity") | Boolean |  | True |  | If you prefer to have PTP clock identity be the system MAC-address of the switch, which is the default EOS behaviour, simply disable the automatic PTP clock identity.<br>default -> (clock_identity_prefix = 00:1C:73 (default)) + (PTP priority 1 as HEX) + ":00:" + (PTP priority 2 as HEX).<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;clock_identity_prefix</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ptp.clock_identity_prefix") | String |  |  |  | PTP clock idetentiy 3-byte prefix. i.e. "01:02:03".<br>By default the 3-byte prefix is "00:1C:73".<br>This can be overridden if auto_clock_identity is set to true (which is the default).<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;clock_identity</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ptp.clock_identity") | String |  |  |  | Set PTP clock identity manually. 6-byte value i.e. "01:02:03:04:05:06".<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_ip</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ptp.source_ip") | String |  |  |  | By default in EOS, PTP packets are sourced with an IP address from the routed port or from the relevant SVI, which is the recommended behaviour.<br>This can be set manually if required, for example, to a value of "10.1.2.3".<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ttl</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ptp.ttl") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;forward_unicast</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ptp.forward_unicast") | Boolean |  | False |  | Enable PTP unicast forwarding.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dscp</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ptp.dscp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;general_messages</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ptp.dscp.general_messages") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;event_messages</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ptp.dscp.event_messages") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;monitor</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ptp.monitor") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ptp.monitor.enabled") | Boolean |  | True |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;threshold</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ptp.monitor.threshold") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;offset_from_master</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ptp.monitor.threshold.offset_from_master") | Integer |  | 250 | Min: 0<br>Max: 1000000000 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mean_path_delay</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ptp.monitor.threshold.mean_path_delay") | Integer |  | 1500 | Min: 0<br>Max: 1000000000 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;drop</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ptp.monitor.threshold.drop") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;offset_from_master</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ptp.monitor.threshold.drop.offset_from_master") | Integer |  |  | Min: 0<br>Max: 1000000000 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mean_path_delay</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ptp.monitor.threshold.drop.mean_path_delay") | Integer |  |  | Min: 0<br>Max: 1000000000 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;missing_message</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ptp.monitor.missing_message") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;intervals</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ptp.monitor.missing_message.intervals") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;announce</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ptp.monitor.missing_message.intervals.announce") | Integer |  |  | Min: 2<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;follow_up</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ptp.monitor.missing_message.intervals.follow_up") | Integer |  |  | Min: 2<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sync</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ptp.monitor.missing_message.intervals.sync") | Integer |  |  | Min: 2<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sequence_ids</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ptp.monitor.missing_message.sequence_ids") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ptp.monitor.missing_message.sequence_ids.enabled") | Boolean |  | True |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;announce</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ptp.monitor.missing_message.sequence_ids.announce") | Integer |  | 3 | Min: 2<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;delay_resp</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ptp.monitor.missing_message.sequence_ids.delay_resp") | Integer |  | 3 | Min: 2<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;follow_up</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ptp.monitor.missing_message.sequence_ids.follow_up") | Integer |  | 3 | Min: 2<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sync</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].ptp.monitor.missing_message.sequence_ids.sync") | Integer |  | 3 | Min: 2<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;id</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].id") | Integer |  |  |  | Unique identifier used for IP addressing and other algorithms. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;platform</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].platform") | String |  |  |  | Arista platform family. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mac_address</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].mac_address") | String |  |  |  | Leverage to document management interface mac address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;system_mac_address</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].system_mac_address") | String |  |  |  | System MAC Address in this following format: "xx:xx:xx:xx:xx:xx".<br>Set to the same MAC address as available in "show version" on the device.<br>"system_mac_address" can also be set directly as a hostvar.<br>If both are set, the setting under "Fabric Topology" takes precedence.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;serial_number</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].serial_number") | String |  |  |  | Set to the Serial Number of the device<br>For  now only used for documentation purpose in the fabric documentation<br>and part of the structured_config<br>"serial_number" can also be set directly as a hostvar.<br>If both are set, the setting under "Fabric Topology" takes precedence.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rack</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].rack") | String |  |  |  | Rack that the switch is located in (only used in snmp_settings location). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mgmt_ip</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].mgmt_ip") | String |  |  | Format: cidr | Node management interface IPv4 address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_mgmt_ip</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ipv6_mgmt_ip") | String |  |  | Format: cidr | Node management interface IPv6 address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mgmt_interface</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].mgmt_interface") | String |  |  |  | Management Interface Name.<br>Default -> platform_management_interface -> mgmt_interface -> "Management1".<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;link_tracking</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].link_tracking") | Dictionary |  |  |  | This configures the Link Tracking Group on a switch as well as adds the p2p-uplinks of the switch as the upstream interfaces.<br>Useful in EVPN multhoming designs.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].link_tracking.enabled") | Boolean |  | False |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;groups</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].link_tracking.groups") | List, items: Dictionary |  | [{'name': 'LT_GROUP1'}] |  | Link Tracking Groups.<br>By default a single group named "LT_GROUP1" is defined with default values.<br>Any groups defined under "groups" will replace the default.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].link_tracking.groups.[].name") | String |  |  |  | Tracking group name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;recovery_delay</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].link_tracking.groups.[].recovery_delay") | Integer |  |  | Min: 0<br>Max: 3600 | default -> platform_settings_mlag_reload_delay -> 300. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;links_minimum</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].link_tracking.groups.[].links_minimum") | Integer |  |  | Min: 1<br>Max: 100000 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;lacp_port_id_range</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].lacp_port_id_range") | Dictionary |  |  |  | This will generate the "lacp port-id range", "begin" and "end" values based on node "id" and the number of nodes in the "node_group".<br>Unique LACP port-id ranges are recommended for EVPN Multihoming designs.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].lacp_port_id_range.enabled") | Boolean |  | False |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;size</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].lacp_port_id_range.size") | Integer |  | 128 |  | Recommended size > = number of ports in the switch. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;offset</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].lacp_port_id_range.offset") | Integer |  | 0 |  | Offset is used to avoid overlapping port-id ranges of different switches.<br>Useful when a "connected-endpoint" is connected to switches in different "node_groups".<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;always_configure_ip_routing</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].always_configure_ip_routing") | Boolean |  | False |  | Force configuration of "ip routing" even on L2 devices.<br>Use this to retain behavior of AVD versions below 4.0.0.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the root level of the final EOS configuration. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].structured_config") | Dictionary |  |  |  | Custom structured config for eos_cli_config_gen. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_ipv4_pool</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].uplink_ipv4_pool") | String |  |  | Format: ipv4_cidr | IPv4 subnet to use to connect to uplink switches. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_interfaces</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].uplink_interfaces") | List, items: String |  |  |  | Local uplink interfaces<br>Each list item supports range syntax that can be expanded into a list of interfaces.<br>If uplink_interfaces is not defined, platform-specific defaults (defined under default_interfaces) will be used instead.<br>Please note that default_interfaces are not defined by default, you should define these yourself.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].uplink_interfaces.[].&lt;str&gt;") | String |  |  | Pattern: Ethernet[\d/]+ |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_switch_interfaces</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].uplink_switch_interfaces") | List, items: String |  |  |  | Interfaces located on uplink switches |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].uplink_switch_interfaces.[].&lt;str&gt;") | String |  |  | Pattern: Ethernet[\d/]+ |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_switches</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].uplink_switches") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].uplink_switches.[].&lt;str&gt;") | String | Required |  |  | Hostname of uplink switch.<br>If parallel uplinks are in use, update max_parallel_uplinks below and specify each uplink switch multiple times.<br>e.g. uplink_switches: [ 'DC1-SPINE1', 'DC1-SPINE1', 'DC1-SPINE2', 'DC1-SPINE2' ].<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_interface_speed</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].uplink_interface_speed") | String |  |  |  | Set point-to-Point interface speed and will apply to uplink interfaces on both ends.<br>interface_speed or forced interface_speed or auto interface_speed.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;max_uplink_switches</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].max_uplink_switches") | Integer |  |  |  | Maximum number of uplink switches.<br>Changing this value may change IP Addressing on uplinks.<br>Can be used to reserve IP space for future expansions.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;max_parallel_uplinks</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].max_parallel_uplinks") | Integer |  |  |  | Number of parallel links towards uplink switches.<br>Changing this value may change interface naming on uplinks (and corresponding downlinks).<br>Can be used to reserve interfaces for future parallel uplinks.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_bfd</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].uplink_bfd") | Boolean |  | False |  | Enable bfd on uplink interfaces. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_native_vlan</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].uplink_native_vlan") | Integer |  |  | Min: 1<br>Max: 4094 | Only applicable to switches with layer-2 port-channel uplinks.<br>A suspended (disabled) vlan will be created in both ends of the link unless the vlan is defined under network services.<br>By default the uplink will not have a native_vlan configured, so EOS defaults to vlan 1.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_ptp</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].uplink_ptp") | Dictionary |  |  |  | Enable PTP on all infrastructure links. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enable</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].uplink_ptp.enable") | Boolean |  | False |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_macsec</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].uplink_macsec") | Dictionary |  |  |  | Enable MacSec on all uplinks. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;profile</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].uplink_macsec.profile") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_structured_config</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].uplink_structured_config") | Dictionary |  |  |  | Custom structured config applied to "uplink_interfaces", and "uplink_switch_interfaces".<br>When uplink_type == "p2p", custom structured config added under ethernet_interfaces.<interface> for eos_cli_config_gen overrides the settings on the ethernet interface level.<br>When uplink_type == "port-channel", custom structured config added under port_channel_interfaces.<interface> for eos_cli_config_gen overrides the settings on the port-channel interface level.<br>"uplink_structured_config" is applied after "structured_config", so it can override "structured_config" defined on node-level.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_port_channel_structured_config</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].mlag_port_channel_structured_config") | Dictionary |  |  |  | Custom structured config applied to MLAG peer link port-channel id.<br>Added under port_channel_interfaces.<interface> for eos_cli_config_gen.<br>Overrides the settings on the port-channel interface level.<br>"mlag_port_channel_structured_config" is applied after "structured_config", so it can override "structured_config" defined on node-level.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_peer_vlan_structured_config</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].mlag_peer_vlan_structured_config") | Dictionary |  |  |  | Custom structured config applied to MLAG Peer Link (control link) SVI interface id.<br>Added under vlan_interfaces.<interface> for eos_cli_config_gen.<br>Overrides the settings on the vlan interface level.<br>"mlag_peer_vlan_structured_config" is applied after "structured_config", so it can override "structured_config" defined on node-level.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_peer_l3_vlan_structured_config</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].mlag_peer_l3_vlan_structured_config") | Dictionary |  |  |  | Custom structured config applied to MLAG underlay L3 peering SVI interface id.<br>Added under vlan_interfaces.<interface> for eos_cli_config_gen.<br>Overrides the settings on the vlan interface level.<br>"mlag_peer_l3_vlan_structured_config" is applied after "structured_config", so it can override "structured_config" defined on node-level.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;short_esi</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].short_esi") | String |  |  |  | short_esi only valid for l2leaf devices using port-channel uplink.<br>Setting short_esi to "auto" generates the short_esi automatically using a hash of configuration elements.<br>< 0000:0000:0000 | auto >.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_system_id_prefix</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].isis_system_id_prefix") | String |  |  | Pattern: [0-9a-f]{4}\.[0-9a-f]{4} | (4.4 hexadecimal). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_maximum_paths</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].isis_maximum_paths") | Integer |  |  |  | Number of path to configure in ECMP for ISIS. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;is_type</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].is_type") | String |  | level-2 | Valid Values:<br>- level-1-2<br>- level-1<br>- level-2 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;node_sid_base</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].node_sid_base") | Integer |  | 0 |  | Node-SID base for isis-sr underlay variants. Combined with node id to generate ISIS-SR node-SID. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loopback_ipv4_pool</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].loopback_ipv4_pool") | String |  |  | Format: ipv4_cidr | IPv4 subnet for Loopback0 allocation. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vtep_loopback_ipv4_pool</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].vtep_loopback_ipv4_pool") | String |  |  | Format: ipv4_cidr | IPv4 subnet for VTEP-Loopback allocation. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loopback_ipv4_offset</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].loopback_ipv4_offset") | Integer |  | 0 |  | Offset all assigned loopback IP addresses.<br>Required when the < loopback_ipv4_pool > is same for 2 different node_types (like spine and l3leaf) to avoid over-lapping IPs.<br>For example, set the minimum offset l3leaf.defaults.loopback_ipv4_offset: < total # spine switches > or vice versa.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loopback_ipv6_pool</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].loopback_ipv6_pool") | String |  |  | Format: ipv6_cidr | IPv6 subnet for Loopback0 allocation. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loopback_ipv6_offset</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].loopback_ipv6_offset") | Integer |  | 0 |  | Offset all assigned loopback IPv6 addresses.<br>Required when the < loopback_ipv6_pool > is same for 2 different node_types (like spine and l3leaf) to avoid overlapping IPs.<br>For example, set the minimum offset l3leaf.defaults.loopback_ipv6_offset: < total # spine switches > or vice versa.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vtep_loopback</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].vtep_loopback") | String |  |  | Pattern: Loopback[\d/]+ | Set VXLAN source interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp_as</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].bgp_as") | String |  |  |  | Required with eBGP. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp_defaults</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].bgp_defaults") | List, items: String |  |  |  | List of EOS commands to apply to BGP daemon. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].bgp_defaults.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_role</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].evpn_role") | String |  |  | Valid Values:<br>- client<br>- server<br>- none | Acting role in EVPN control plane. Default is set in node_type definition from node_type_keys. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_route_servers</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].evpn_route_servers") | List, items: String |  |  |  | List of nodes acting as EVPN Route-Servers / Route-Reflectors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].evpn_route_servers.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_services_l2_only</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].evpn_services_l2_only") | Boolean |  | False |  | Possibility to prevent configuration of Tenant VRFs and SVIs.<br>Override node definition "network_services_l3" from node_type_keys.<br>This allows support for centralized routing.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;filter</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].filter") | Dictionary |  |  |  | Filter L3 and L2 network services based on tenant and tags (and operation filter).<br>If filter is not defined it will default to all.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tenants</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].filter.tenants") | List, items: String |  | ['all'] |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].filter.tenants.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tags</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].filter.tags") | List, items: String |  | ['all'] |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].filter.tags.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;always_include_vrfs_in_tenants</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].filter.always_include_vrfs_in_tenants") | List, items: String |  |  |  | List of tenants where VRFs will be configured even if VLANs are not included in tags<br>Useful for L3 "border" leaf.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].filter.always_include_vrfs_in_tenants.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;only_vlans_in_use</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].filter.only_vlans_in_use") | Boolean |  | False |  | Only configure VLANs, SVIs, VRFs in use by connected endpoints or downstream L2 switches.<br>Note! This feature only considers configuration managed by eos_designs.<br>This excludes structured_config, custom_structured_configuration_, raw_eos_cli, eos_cli, custom templates, configlets etc.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;igmp_snooping_enabled</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].igmp_snooping_enabled") | Boolean |  | True |  | Activate or deactivate IGMP snooping on device level. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_gateway</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].evpn_gateway") | Dictionary |  |  |  | Node is acting as EVPN Multi-Domain Gateway.<br>New BGP peer-group is generated between EVPN GWs in different domains or between GWs and Route Servers.<br>Name can be changed under "bgp_peer_groups.evpn_overlay_core" variable.<br>L3 rechability for different EVPN GWs must be already in place, it is recommended to use DCI & L3 Edge if Route Servers and GWs are not defined under the same Ansible inventory.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remote_peers</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].evpn_gateway.remote_peers") | List, items: Dictionary |  |  |  | Define remote peers of the EVPN VXLAN Gateway.<br>If the hostname can be found in the inventory, ip_address and BGP ASN will be automatically populated. Manual override takes precedence.<br>If the peer's hostname can not be found in the inventory, ip_address and bgp_as must be defined.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- hostname</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].evpn_gateway.remote_peers.[].hostname") | String |  |  |  | Hostname of remote EVPN GW server. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].evpn_gateway.remote_peers.[].ip_address") | String |  |  | Format: ipv4 | Peering IP of remote Route Server. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp_as</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].evpn_gateway.remote_peers.[].bgp_as") | String |  |  |  | BGP ASN of remote Route Server. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_l2</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].evpn_gateway.evpn_l2") | Dictionary |  |  |  | Enable EVPN Gateway functionality for route-types 2 (MAC-IP) and 3 (IMET). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].evpn_gateway.evpn_l2.enabled") | Boolean |  | False |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_l3</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].evpn_gateway.evpn_l3") | Dictionary |  |  |  | Enable EVPN Gateway functionality for route-type 5 (IP-PREFIX). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].evpn_gateway.evpn_l3.enabled") | Boolean |  | False |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inter_domain</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].evpn_gateway.evpn_l3.inter_domain") | Boolean |  | True |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipvpn_gateway</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ipvpn_gateway") | Dictionary |  |  |  | Node is acting as IP-VPN Gateway for EVPN to MPLS-IP-VPN Interworking. The BGP peer group used for this is "bgp_peer_groups.ipvpn_gateway_peers".<br>L3 Reachability is required for this to work, the preferred method to establish underlay connectivity is to use core_interfaces.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ipvpn_gateway.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_domain_id</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ipvpn_gateway.evpn_domain_id") | String |  | 65535:1 |  | Domain ID to assign to EVPN address family for use with D-path. Format <nn>:<nn>. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipvpn_domain_id</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ipvpn_gateway.ipvpn_domain_id") | String |  | 65535:2 |  | Domain ID to assign to IPVPN address families for use with D-path. Format <nn>:<nn>. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enable_d_path</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ipvpn_gateway.enable_d_path") | Boolean |  | True |  | Enable D-path for use with BGP bestpath selection algorithm. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maximum_routes</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ipvpn_gateway.maximum_routes") | Integer |  | 0 |  | Maximum routes to accept from IPVPN remote peers. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;local_as</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ipvpn_gateway.local_as") | String |  | none |  | Apply local-as to peering with IPVPN remote peers. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;address_families</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ipvpn_gateway.address_families") | List, items: String |  | ['vpn-ipv4'] |  | IPVPN address families to enable for remote peers. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ipvpn_gateway.address_families.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remote_peers</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ipvpn_gateway.remote_peers") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- hostname</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ipvpn_gateway.remote_peers.[].hostname") | String | Required |  |  | Hostname of remote IPVPN Peer. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ipvpn_gateway.remote_peers.[].ip_address") | String | Required |  | Format: ipv4 | Peering IP of remote IPVPN Peer. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp_as</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ipvpn_gateway.remote_peers.[].bgp_as") | String | Required |  |  | BGP ASN of remote IPVPN Peer. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].mlag") | Boolean |  | True |  | Enable / Disable auto MLAG, when two nodes are defined in node group. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_dual_primary_detection</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].mlag_dual_primary_detection") | Boolean |  | False |  | Enable / Disable MLAG dual primary detection. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_ibgp_origin_incomplete</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].mlag_ibgp_origin_incomplete") | Boolean |  | True |  | Set origin of routes received from MLAG iBGP peer to incomplete.<br>The purpose is to optimize routing for leaf loopbacks from spine perspective and<br>avoid suboptimal routing via peerlink for control plane traffic.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_interfaces</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].mlag_interfaces") | List, items: String |  |  |  | Each list item supports range syntax that can be expanded into a list of interfaces.<br>Required when MLAG leafs are present in the topology.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].mlag_interfaces.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_interfaces_speed</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].mlag_interfaces_speed") | String |  |  |  | Set MLAG interface speed.<br>< interface_speed or forced interface_speed or auto interface_speed >.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_peer_l3_vlan</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].mlag_peer_l3_vlan") | Integer |  | 4093 | Min: 0<br>Max: 4094 | Underlay L3 peering SVI interface id.<br>If set to 0 or the same vlan as mlag_peer_vlan, the mlag_peer_vlan will be used for L3 peering.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_peer_l3_ipv4_pool</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].mlag_peer_l3_ipv4_pool") | String |  |  | Format: ipv4_cidr | IP address pool used for MLAG underlay L3 peering. IP is derived from the node id.<br>Required when MLAG leafs present in topology and they are using a separate L3 peering VLAN.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_peer_vlan</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].mlag_peer_vlan") | Integer |  | 4094 | Min: 1<br>Max: 4094 | MLAG Peer Link (control link) SVI interface id. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_peer_link_allowed_vlans</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].mlag_peer_link_allowed_vlans") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_peer_ipv4_pool</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].mlag_peer_ipv4_pool") | String |  |  | Format: ipv4_cidr | IP address pool used for MLAG Peer Link (control link). IP is derived from the node id.<br>Required when MLAG leafs present in topology.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_port_channel_id</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].mlag_port_channel_id") | Integer |  |  |  | If not set, the mlag port-channel id is generated based on the digits of the first interface present in 'mlag_interfaces'.<br>Valid port-channel id numbers are < 1-2000 > for EOS < 4.25.0F and < 1 - 999999 > for EOS >= 4.25.0F.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_domain_id</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].mlag_domain_id") | String |  |  |  | MLAG Domain ID. If not set the node group name (Set with "group" key) will be used. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_mode</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].spanning_tree_mode") | String |  |  | Valid Values:<br>- mstp<br>- rstp<br>- rapid-pvst<br>- none |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_priority</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].spanning_tree_priority") | Integer |  | 32768 |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_root_super</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].spanning_tree_root_super") | Boolean |  | False |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;virtual_router_mac_address</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].virtual_router_mac_address") | String |  |  | Format: mac | Virtual router mac address for anycast gateway. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inband_mgmt_interface</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].inband_mgmt_interface") | String |  |  |  | Pointer to interface used for inband management.<br>All configuration must be done using other data models like network services or structured_config.<br>'inband_mgmt_interface' is only used to refer to this interface as source in various management protocol settings (future feature).<br><br>On L2 switches, this defaults to Vlan<inband_mgmt_vlan> if either 'inband_mgmt_subnet' or 'inband_mgmt_ip' is set.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inband_mgmt_vlan</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].inband_mgmt_vlan") | Integer |  | 4092 |  | VLAN number used for inband management on L2 switches (switches using port-channel trunks as uplinks).<br>When using 'inband_mgmt_subnet' the VLAN and SVIs will be created automatically on this switch as well as all 'uplink_switches'.<br>When using 'inband_mgmt_ip' the VLAN and SVI will only be created on this device and added to uplink trunk. The VLAN and SVI on the parent switches must be created using network services data models. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inband_mgmt_subnet</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].inband_mgmt_subnet") | String |  |  | Format: ipv4_cidr | Optional IP subnet assigned to inband management SVIs on L2 switches (switches using port-channels as uplinks).<br>Parent l3leafs will have SVI with "ip virtual-router" and host-route injection based on ARP.<br>This allows all l3leafs to reuse the same subnet across multiple racks without VXLAN extension.<br>SVI IP address will be assigned as follows:<br>virtual-router: <subnet> + 1<br>l3leaf A      : <subnet> + 2 (same IP on all l3leaf A)<br>l3leaf B      : <subnet> + 3 (same IP on all l3leaf B)<br>l2leafs       : <subnet> + 3 + <l2leaf id><br>GW on l2leafs : <subnet> + 1<br>Assign range larger than total l2leafs + 5<br><br>Setting is ignored if 'inband_mgmt_ip' is set.<br><br>This setting is applicable to L2 switches (switches using port-channel trunks as uplinks).<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inband_mgmt_ip</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].inband_mgmt_ip") | String |  |  | Format: ipv4_cidr | IP address assigned to the inband management interface set with 'inband_mgmt_vlan'.<br>This overrides 'inband_mgmt_subnet', hence all behavior of 'inband_mgmt_subnet' is removed.<br><br>If this is set the VLAN and SVI will only be created on the L2 switch and added to uplink trunk.<br>The VLAN and SVI on the parent switches must be created using network services data models.<br><br>This setting is applicable to L2 switches (switches using port-channel trunks as uplinks).<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inband_mgmt_gateway</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].inband_mgmt_gateway") | String |  |  | Format: ipv4 | Default gateway configured in the 'inband_mgmt_vrf' when using 'inband_mgmt_ip'. Otherwise gateway is derived from 'inband_mgmt_subnet' if set.<br><br>This setting is applicable to L2 switches (switches using port-channel trunks as uplinks).<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inband_mgmt_description</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].inband_mgmt_description") | String |  | Inband Management |  | Description configured on the Inband Management SVI.<br><br>This setting is only applied on the devices where it is set, it does not automatically affect any parent/child devices configuration, so it must be set on each applicable node/node-group/node-type as needed. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inband_mgmt_vlan_name</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].inband_mgmt_vlan_name") | String |  | Inband Management |  | Name configured on the Inband Management VLAN.<br>This setting is only applied on the devices where it is set, it does not automatically affect any parent/child devices configuration, so it must be set on each applicable node/node-group/node-type as needed. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inband_mgmt_vrf</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].inband_mgmt_vrf") | String |  | default |  | VRF configured on the Inband Management Interface.<br>The VRF is created if not already created by other means.<br>This setting is only applied on the devices where it is set, it does not automatically affect any parent/child devices configuration, so it must be set on each applicable node/node-group/node-type as needed. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inband_mgmt_mtu</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].inband_mgmt_mtu") | Integer |  | 1500 |  | MTU configured on the Inband Management Interface.<br>This setting is only applied on the devices where it is set, it does not automatically affect any parent/child devices configuration, so it must be set on each applicable node/node-group/node-type as needed. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inband_management_subnet</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].inband_management_subnet") <span style="color:red">deprecated</span> | String |  |  | Format: ipv4_cidr | Optional IP subnet assigned to inband management SVIs on L2 switches (switches using port-channels as uplinks).<br>Parent l3leafs will have SVI with "ip virtual-router" and host-route injection based on ARP.<br>This allows all l3leafs to reuse the same subnet across multiple racks without VXLAN extension.<br>SVI IP address will be assigned as follows:<br>virtual-router: <subnet> + 1<br>l3leaf A      : <subnet> + 2 (same IP on all l3leaf A)<br>l3leaf B      : <subnet> + 3 (same IP on all l3leaf B)<br>l2leafs       : <subnet> + 3 + <l2leaf id><br>GW on l2leafs : <subnet> + 1<br>Assign range larger than total l2leafs + 5<br><br>Setting is ignored if 'inband_mgmt_ip' is set.<br><br>This setting is applicable to L2 switches (switches using port-channel trunks as uplinks).<br><span style="color:red">This key is deprecated. Support will be removed in AVD version 5.0.0. Use <samp>inband_mgmt_subnet</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inband_management_vlan</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].inband_management_vlan") <span style="color:red">deprecated</span> | Integer |  | 4092 |  | VLAN number used for inband management on L2 switches (switches using port-channel trunks as uplinks).<br>When using 'inband_mgmt_subnet' the VLAN and SVIs will be created automatically on this switch as well as all 'uplink_switches'.<br>When using 'inband_mgmt_ip' the VLAN and SVI will only be created on this device and added to uplink trunk. The VLAN and SVI on the parent switches must be created using network services data models.<span style="color:red">This key is deprecated. Support will be removed in AVD version 5.0.0. Use <samp>inband_mgmt_vlan</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mpls_overlay_role</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].mpls_overlay_role") | String |  |  | Valid Values:<br>- client<br>- server<br>- none | Set the default mpls overlay role.<br>Acting role in overlay control plane.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;overlay_address_families</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].overlay_address_families") | List, items: String |  |  |  | Set the default overlay address families.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].overlay_address_families.[].&lt;str&gt;") | String |  |  | Valid Values:<br>- evpn<br>- vpn-ipv4<br>- vpn-ipv6 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mpls_route_reflectors</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].mpls_route_reflectors") | List, items: String |  |  |  | List of inventory hostname acting as MPLS route-reflectors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].mpls_route_reflectors.[].&lt;str&gt;") | String |  |  |  | Inventory_hostname_of_mpls_route_reflectors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp_cluster_id</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].bgp_cluster_id") | String |  |  |  | Set BGP cluster id. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ptp</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ptp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ptp.enabled") | Boolean |  | False |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;profile</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ptp.profile") | String |  | aes67-r16-2016 | Valid Values:<br>- aes67<br>- smpte2059-2<br>- aes67-r16-2016 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;domain</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ptp.domain") | Integer |  | 127 | Min: 0<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority1</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ptp.priority1") | Integer |  |  | Min: 0<br>Max: 255 | default -> automatically set based on node_type.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority2</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ptp.priority2") | Integer |  |  | Min: 0<br>Max: 255 | default -> (node_id modulus 256).<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;auto_clock_identity</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ptp.auto_clock_identity") | Boolean |  | True |  | If you prefer to have PTP clock identity be the system MAC-address of the switch, which is the default EOS behaviour, simply disable the automatic PTP clock identity.<br>default -> (clock_identity_prefix = 00:1C:73 (default)) + (PTP priority 1 as HEX) + ":00:" + (PTP priority 2 as HEX).<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;clock_identity_prefix</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ptp.clock_identity_prefix") | String |  |  |  | PTP clock idetentiy 3-byte prefix. i.e. "01:02:03".<br>By default the 3-byte prefix is "00:1C:73".<br>This can be overridden if auto_clock_identity is set to true (which is the default).<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;clock_identity</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ptp.clock_identity") | String |  |  |  | Set PTP clock identity manually. 6-byte value i.e. "01:02:03:04:05:06".<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_ip</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ptp.source_ip") | String |  |  |  | By default in EOS, PTP packets are sourced with an IP address from the routed port or from the relevant SVI, which is the recommended behaviour.<br>This can be set manually if required, for example, to a value of "10.1.2.3".<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ttl</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ptp.ttl") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;forward_unicast</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ptp.forward_unicast") | Boolean |  | False |  | Enable PTP unicast forwarding.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dscp</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ptp.dscp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;general_messages</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ptp.dscp.general_messages") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;event_messages</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ptp.dscp.event_messages") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;monitor</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ptp.monitor") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ptp.monitor.enabled") | Boolean |  | True |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;threshold</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ptp.monitor.threshold") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;offset_from_master</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ptp.monitor.threshold.offset_from_master") | Integer |  | 250 | Min: 0<br>Max: 1000000000 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mean_path_delay</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ptp.monitor.threshold.mean_path_delay") | Integer |  | 1500 | Min: 0<br>Max: 1000000000 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;drop</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ptp.monitor.threshold.drop") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;offset_from_master</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ptp.monitor.threshold.drop.offset_from_master") | Integer |  |  | Min: 0<br>Max: 1000000000 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mean_path_delay</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ptp.monitor.threshold.drop.mean_path_delay") | Integer |  |  | Min: 0<br>Max: 1000000000 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;missing_message</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ptp.monitor.missing_message") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;intervals</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ptp.monitor.missing_message.intervals") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;announce</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ptp.monitor.missing_message.intervals.announce") | Integer |  |  | Min: 2<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;follow_up</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ptp.monitor.missing_message.intervals.follow_up") | Integer |  |  | Min: 2<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sync</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ptp.monitor.missing_message.intervals.sync") | Integer |  |  | Min: 2<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sequence_ids</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ptp.monitor.missing_message.sequence_ids") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ptp.monitor.missing_message.sequence_ids.enabled") | Boolean |  | True |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;announce</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ptp.monitor.missing_message.sequence_ids.announce") | Integer |  | 3 | Min: 2<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;delay_resp</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ptp.monitor.missing_message.sequence_ids.delay_resp") | Integer |  | 3 | Min: 2<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;follow_up</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ptp.monitor.missing_message.sequence_ids.follow_up") | Integer |  | 3 | Min: 2<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sync</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].ptp.monitor.missing_message.sequence_ids.sync") | Integer |  | 3 | Min: 2<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;nodes</samp>](## "&lt;node_type_keys.key&gt;.nodes") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].name") | String | Required, Unique |  |  | The Node Name is used as "hostname". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;id</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].id") | Integer |  |  |  | Unique identifier used for IP addressing and other algorithms. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;platform</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].platform") | String |  |  |  | Arista platform family. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mac_address</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].mac_address") | String |  |  |  | Leverage to document management interface mac address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;system_mac_address</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].system_mac_address") | String |  |  |  | System MAC Address in this following format: "xx:xx:xx:xx:xx:xx".<br>Set to the same MAC address as available in "show version" on the device.<br>"system_mac_address" can also be set directly as a hostvar.<br>If both are set, the setting under "Fabric Topology" takes precedence.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;serial_number</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].serial_number") | String |  |  |  | Set to the Serial Number of the device<br>For  now only used for documentation purpose in the fabric documentation<br>and part of the structured_config<br>"serial_number" can also be set directly as a hostvar.<br>If both are set, the setting under "Fabric Topology" takes precedence.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rack</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].rack") | String |  |  |  | Rack that the switch is located in (only used in snmp_settings location). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mgmt_ip</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].mgmt_ip") | String |  |  | Format: cidr | Node management interface IPv4 address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_mgmt_ip</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ipv6_mgmt_ip") | String |  |  | Format: cidr | Node management interface IPv6 address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mgmt_interface</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].mgmt_interface") | String |  |  |  | Management Interface Name.<br>Default -> platform_management_interface -> mgmt_interface -> "Management1".<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;link_tracking</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].link_tracking") | Dictionary |  |  |  | This configures the Link Tracking Group on a switch as well as adds the p2p-uplinks of the switch as the upstream interfaces.<br>Useful in EVPN multhoming designs.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].link_tracking.enabled") | Boolean |  | False |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;groups</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].link_tracking.groups") | List, items: Dictionary |  | [{'name': 'LT_GROUP1'}] |  | Link Tracking Groups.<br>By default a single group named "LT_GROUP1" is defined with default values.<br>Any groups defined under "groups" will replace the default.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].link_tracking.groups.[].name") | String |  |  |  | Tracking group name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;recovery_delay</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].link_tracking.groups.[].recovery_delay") | Integer |  |  | Min: 0<br>Max: 3600 | default -> platform_settings_mlag_reload_delay -> 300. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;links_minimum</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].link_tracking.groups.[].links_minimum") | Integer |  |  | Min: 1<br>Max: 100000 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;lacp_port_id_range</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].lacp_port_id_range") | Dictionary |  |  |  | This will generate the "lacp port-id range", "begin" and "end" values based on node "id" and the number of nodes in the "node_group".<br>Unique LACP port-id ranges are recommended for EVPN Multihoming designs.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].lacp_port_id_range.enabled") | Boolean |  | False |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;size</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].lacp_port_id_range.size") | Integer |  | 128 |  | Recommended size > = number of ports in the switch. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;offset</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].lacp_port_id_range.offset") | Integer |  | 0 |  | Offset is used to avoid overlapping port-id ranges of different switches.<br>Useful when a "connected-endpoint" is connected to switches in different "node_groups".<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;always_configure_ip_routing</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].always_configure_ip_routing") | Boolean |  | False |  | Force configuration of "ip routing" even on L2 devices.<br>Use this to retain behavior of AVD versions below 4.0.0.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the root level of the final EOS configuration. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].structured_config") | Dictionary |  |  |  | Custom structured config for eos_cli_config_gen. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_ipv4_pool</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].uplink_ipv4_pool") | String |  |  | Format: ipv4_cidr | IPv4 subnet to use to connect to uplink switches. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_interfaces</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].uplink_interfaces") | List, items: String |  |  |  | Local uplink interfaces<br>Each list item supports range syntax that can be expanded into a list of interfaces.<br>If uplink_interfaces is not defined, platform-specific defaults (defined under default_interfaces) will be used instead.<br>Please note that default_interfaces are not defined by default, you should define these yourself.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].uplink_interfaces.[].&lt;str&gt;") | String |  |  | Pattern: Ethernet[\d/]+ |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_switch_interfaces</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].uplink_switch_interfaces") | List, items: String |  |  |  | Interfaces located on uplink switches |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].uplink_switch_interfaces.[].&lt;str&gt;") | String |  |  | Pattern: Ethernet[\d/]+ |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_switches</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].uplink_switches") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].uplink_switches.[].&lt;str&gt;") | String | Required |  |  | Hostname of uplink switch.<br>If parallel uplinks are in use, update max_parallel_uplinks below and specify each uplink switch multiple times.<br>e.g. uplink_switches: [ 'DC1-SPINE1', 'DC1-SPINE1', 'DC1-SPINE2', 'DC1-SPINE2' ].<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_interface_speed</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].uplink_interface_speed") | String |  |  |  | Set point-to-Point interface speed and will apply to uplink interfaces on both ends.<br>interface_speed or forced interface_speed or auto interface_speed.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;max_uplink_switches</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].max_uplink_switches") | Integer |  |  |  | Maximum number of uplink switches.<br>Changing this value may change IP Addressing on uplinks.<br>Can be used to reserve IP space for future expansions.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;max_parallel_uplinks</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].max_parallel_uplinks") | Integer |  |  |  | Number of parallel links towards uplink switches.<br>Changing this value may change interface naming on uplinks (and corresponding downlinks).<br>Can be used to reserve interfaces for future parallel uplinks.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_bfd</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].uplink_bfd") | Boolean |  | False |  | Enable bfd on uplink interfaces. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_native_vlan</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].uplink_native_vlan") | Integer |  |  | Min: 1<br>Max: 4094 | Only applicable to switches with layer-2 port-channel uplinks.<br>A suspended (disabled) vlan will be created in both ends of the link unless the vlan is defined under network services.<br>By default the uplink will not have a native_vlan configured, so EOS defaults to vlan 1.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_ptp</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].uplink_ptp") | Dictionary |  |  |  | Enable PTP on all infrastructure links. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enable</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].uplink_ptp.enable") | Boolean |  | False |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_macsec</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].uplink_macsec") | Dictionary |  |  |  | Enable MacSec on all uplinks. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;profile</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].uplink_macsec.profile") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_structured_config</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].uplink_structured_config") | Dictionary |  |  |  | Custom structured config applied to "uplink_interfaces", and "uplink_switch_interfaces".<br>When uplink_type == "p2p", custom structured config added under ethernet_interfaces.<interface> for eos_cli_config_gen overrides the settings on the ethernet interface level.<br>When uplink_type == "port-channel", custom structured config added under port_channel_interfaces.<interface> for eos_cli_config_gen overrides the settings on the port-channel interface level.<br>"uplink_structured_config" is applied after "structured_config", so it can override "structured_config" defined on node-level.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_port_channel_structured_config</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].mlag_port_channel_structured_config") | Dictionary |  |  |  | Custom structured config applied to MLAG peer link port-channel id.<br>Added under port_channel_interfaces.<interface> for eos_cli_config_gen.<br>Overrides the settings on the port-channel interface level.<br>"mlag_port_channel_structured_config" is applied after "structured_config", so it can override "structured_config" defined on node-level.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_peer_vlan_structured_config</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].mlag_peer_vlan_structured_config") | Dictionary |  |  |  | Custom structured config applied to MLAG Peer Link (control link) SVI interface id.<br>Added under vlan_interfaces.<interface> for eos_cli_config_gen.<br>Overrides the settings on the vlan interface level.<br>"mlag_peer_vlan_structured_config" is applied after "structured_config", so it can override "structured_config" defined on node-level.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_peer_l3_vlan_structured_config</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].mlag_peer_l3_vlan_structured_config") | Dictionary |  |  |  | Custom structured config applied to MLAG underlay L3 peering SVI interface id.<br>Added under vlan_interfaces.<interface> for eos_cli_config_gen.<br>Overrides the settings on the vlan interface level.<br>"mlag_peer_l3_vlan_structured_config" is applied after "structured_config", so it can override "structured_config" defined on node-level.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;short_esi</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].short_esi") | String |  |  |  | short_esi only valid for l2leaf devices using port-channel uplink.<br>Setting short_esi to "auto" generates the short_esi automatically using a hash of configuration elements.<br>< 0000:0000:0000 | auto >.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_system_id_prefix</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].isis_system_id_prefix") | String |  |  | Pattern: [0-9a-f]{4}\.[0-9a-f]{4} | (4.4 hexadecimal). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_maximum_paths</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].isis_maximum_paths") | Integer |  |  |  | Number of path to configure in ECMP for ISIS. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;is_type</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].is_type") | String |  | level-2 | Valid Values:<br>- level-1-2<br>- level-1<br>- level-2 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;node_sid_base</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].node_sid_base") | Integer |  | 0 |  | Node-SID base for isis-sr underlay variants. Combined with node id to generate ISIS-SR node-SID. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loopback_ipv4_pool</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].loopback_ipv4_pool") | String |  |  | Format: ipv4_cidr | IPv4 subnet for Loopback0 allocation. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vtep_loopback_ipv4_pool</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].vtep_loopback_ipv4_pool") | String |  |  | Format: ipv4_cidr | IPv4 subnet for VTEP-Loopback allocation. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loopback_ipv4_offset</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].loopback_ipv4_offset") | Integer |  | 0 |  | Offset all assigned loopback IP addresses.<br>Required when the < loopback_ipv4_pool > is same for 2 different node_types (like spine and l3leaf) to avoid over-lapping IPs.<br>For example, set the minimum offset l3leaf.defaults.loopback_ipv4_offset: < total # spine switches > or vice versa.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loopback_ipv6_pool</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].loopback_ipv6_pool") | String |  |  | Format: ipv6_cidr | IPv6 subnet for Loopback0 allocation. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loopback_ipv6_offset</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].loopback_ipv6_offset") | Integer |  | 0 |  | Offset all assigned loopback IPv6 addresses.<br>Required when the < loopback_ipv6_pool > is same for 2 different node_types (like spine and l3leaf) to avoid overlapping IPs.<br>For example, set the minimum offset l3leaf.defaults.loopback_ipv6_offset: < total # spine switches > or vice versa.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vtep_loopback</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].vtep_loopback") | String |  |  | Pattern: Loopback[\d/]+ | Set VXLAN source interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp_as</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].bgp_as") | String |  |  |  | Required with eBGP. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp_defaults</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].bgp_defaults") | List, items: String |  |  |  | List of EOS commands to apply to BGP daemon. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].bgp_defaults.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_role</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].evpn_role") | String |  |  | Valid Values:<br>- client<br>- server<br>- none | Acting role in EVPN control plane. Default is set in node_type definition from node_type_keys. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_route_servers</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].evpn_route_servers") | List, items: String |  |  |  | List of nodes acting as EVPN Route-Servers / Route-Reflectors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].evpn_route_servers.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_services_l2_only</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].evpn_services_l2_only") | Boolean |  | False |  | Possibility to prevent configuration of Tenant VRFs and SVIs.<br>Override node definition "network_services_l3" from node_type_keys.<br>This allows support for centralized routing.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;filter</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].filter") | Dictionary |  |  |  | Filter L3 and L2 network services based on tenant and tags (and operation filter).<br>If filter is not defined it will default to all.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tenants</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].filter.tenants") | List, items: String |  | ['all'] |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].filter.tenants.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tags</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].filter.tags") | List, items: String |  | ['all'] |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].filter.tags.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;always_include_vrfs_in_tenants</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].filter.always_include_vrfs_in_tenants") | List, items: String |  |  |  | List of tenants where VRFs will be configured even if VLANs are not included in tags<br>Useful for L3 "border" leaf.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].filter.always_include_vrfs_in_tenants.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;only_vlans_in_use</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].filter.only_vlans_in_use") | Boolean |  | False |  | Only configure VLANs, SVIs, VRFs in use by connected endpoints or downstream L2 switches.<br>Note! This feature only considers configuration managed by eos_designs.<br>This excludes structured_config, custom_structured_configuration_, raw_eos_cli, eos_cli, custom templates, configlets etc.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;igmp_snooping_enabled</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].igmp_snooping_enabled") | Boolean |  | True |  | Activate or deactivate IGMP snooping on device level. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_gateway</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].evpn_gateway") | Dictionary |  |  |  | Node is acting as EVPN Multi-Domain Gateway.<br>New BGP peer-group is generated between EVPN GWs in different domains or between GWs and Route Servers.<br>Name can be changed under "bgp_peer_groups.evpn_overlay_core" variable.<br>L3 rechability for different EVPN GWs must be already in place, it is recommended to use DCI & L3 Edge if Route Servers and GWs are not defined under the same Ansible inventory.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remote_peers</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].evpn_gateway.remote_peers") | List, items: Dictionary |  |  |  | Define remote peers of the EVPN VXLAN Gateway.<br>If the hostname can be found in the inventory, ip_address and BGP ASN will be automatically populated. Manual override takes precedence.<br>If the peer's hostname can not be found in the inventory, ip_address and bgp_as must be defined.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- hostname</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].evpn_gateway.remote_peers.[].hostname") | String |  |  |  | Hostname of remote EVPN GW server. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].evpn_gateway.remote_peers.[].ip_address") | String |  |  | Format: ipv4 | Peering IP of remote Route Server. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp_as</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].evpn_gateway.remote_peers.[].bgp_as") | String |  |  |  | BGP ASN of remote Route Server. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_l2</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].evpn_gateway.evpn_l2") | Dictionary |  |  |  | Enable EVPN Gateway functionality for route-types 2 (MAC-IP) and 3 (IMET). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].evpn_gateway.evpn_l2.enabled") | Boolean |  | False |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_l3</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].evpn_gateway.evpn_l3") | Dictionary |  |  |  | Enable EVPN Gateway functionality for route-type 5 (IP-PREFIX). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].evpn_gateway.evpn_l3.enabled") | Boolean |  | False |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inter_domain</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].evpn_gateway.evpn_l3.inter_domain") | Boolean |  | True |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipvpn_gateway</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ipvpn_gateway") | Dictionary |  |  |  | Node is acting as IP-VPN Gateway for EVPN to MPLS-IP-VPN Interworking. The BGP peer group used for this is "bgp_peer_groups.ipvpn_gateway_peers".<br>L3 Reachability is required for this to work, the preferred method to establish underlay connectivity is to use core_interfaces.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ipvpn_gateway.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_domain_id</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ipvpn_gateway.evpn_domain_id") | String |  | 65535:1 |  | Domain ID to assign to EVPN address family for use with D-path. Format <nn>:<nn>. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipvpn_domain_id</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ipvpn_gateway.ipvpn_domain_id") | String |  | 65535:2 |  | Domain ID to assign to IPVPN address families for use with D-path. Format <nn>:<nn>. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enable_d_path</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ipvpn_gateway.enable_d_path") | Boolean |  | True |  | Enable D-path for use with BGP bestpath selection algorithm. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maximum_routes</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ipvpn_gateway.maximum_routes") | Integer |  | 0 |  | Maximum routes to accept from IPVPN remote peers. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;local_as</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ipvpn_gateway.local_as") | String |  | none |  | Apply local-as to peering with IPVPN remote peers. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;address_families</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ipvpn_gateway.address_families") | List, items: String |  | ['vpn-ipv4'] |  | IPVPN address families to enable for remote peers. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ipvpn_gateway.address_families.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remote_peers</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ipvpn_gateway.remote_peers") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- hostname</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ipvpn_gateway.remote_peers.[].hostname") | String | Required |  |  | Hostname of remote IPVPN Peer. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ipvpn_gateway.remote_peers.[].ip_address") | String | Required |  | Format: ipv4 | Peering IP of remote IPVPN Peer. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp_as</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ipvpn_gateway.remote_peers.[].bgp_as") | String | Required |  |  | BGP ASN of remote IPVPN Peer. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].mlag") | Boolean |  | True |  | Enable / Disable auto MLAG, when two nodes are defined in node group. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_dual_primary_detection</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].mlag_dual_primary_detection") | Boolean |  | False |  | Enable / Disable MLAG dual primary detection. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_ibgp_origin_incomplete</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].mlag_ibgp_origin_incomplete") | Boolean |  | True |  | Set origin of routes received from MLAG iBGP peer to incomplete.<br>The purpose is to optimize routing for leaf loopbacks from spine perspective and<br>avoid suboptimal routing via peerlink for control plane traffic.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_interfaces</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].mlag_interfaces") | List, items: String |  |  |  | Each list item supports range syntax that can be expanded into a list of interfaces.<br>Required when MLAG leafs are present in the topology.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].mlag_interfaces.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_interfaces_speed</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].mlag_interfaces_speed") | String |  |  |  | Set MLAG interface speed.<br>< interface_speed or forced interface_speed or auto interface_speed >.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_peer_l3_vlan</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].mlag_peer_l3_vlan") | Integer |  | 4093 | Min: 0<br>Max: 4094 | Underlay L3 peering SVI interface id.<br>If set to 0 or the same vlan as mlag_peer_vlan, the mlag_peer_vlan will be used for L3 peering.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_peer_l3_ipv4_pool</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].mlag_peer_l3_ipv4_pool") | String |  |  | Format: ipv4_cidr | IP address pool used for MLAG underlay L3 peering. IP is derived from the node id.<br>Required when MLAG leafs present in topology and they are using a separate L3 peering VLAN.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_peer_vlan</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].mlag_peer_vlan") | Integer |  | 4094 | Min: 1<br>Max: 4094 | MLAG Peer Link (control link) SVI interface id. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_peer_link_allowed_vlans</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].mlag_peer_link_allowed_vlans") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_peer_ipv4_pool</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].mlag_peer_ipv4_pool") | String |  |  | Format: ipv4_cidr | IP address pool used for MLAG Peer Link (control link). IP is derived from the node id.<br>Required when MLAG leafs present in topology.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_port_channel_id</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].mlag_port_channel_id") | Integer |  |  |  | If not set, the mlag port-channel id is generated based on the digits of the first interface present in 'mlag_interfaces'.<br>Valid port-channel id numbers are < 1-2000 > for EOS < 4.25.0F and < 1 - 999999 > for EOS >= 4.25.0F.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_domain_id</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].mlag_domain_id") | String |  |  |  | MLAG Domain ID. If not set the node group name (Set with "group" key) will be used. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_mode</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].spanning_tree_mode") | String |  |  | Valid Values:<br>- mstp<br>- rstp<br>- rapid-pvst<br>- none |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_priority</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].spanning_tree_priority") | Integer |  | 32768 |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_root_super</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].spanning_tree_root_super") | Boolean |  | False |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;virtual_router_mac_address</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].virtual_router_mac_address") | String |  |  | Format: mac | Virtual router mac address for anycast gateway. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inband_mgmt_interface</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].inband_mgmt_interface") | String |  |  |  | Pointer to interface used for inband management.<br>All configuration must be done using other data models like network services or structured_config.<br>'inband_mgmt_interface' is only used to refer to this interface as source in various management protocol settings (future feature).<br><br>On L2 switches, this defaults to Vlan<inband_mgmt_vlan> if either 'inband_mgmt_subnet' or 'inband_mgmt_ip' is set.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inband_mgmt_vlan</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].inband_mgmt_vlan") | Integer |  | 4092 |  | VLAN number used for inband management on L2 switches (switches using port-channel trunks as uplinks).<br>When using 'inband_mgmt_subnet' the VLAN and SVIs will be created automatically on this switch as well as all 'uplink_switches'.<br>When using 'inband_mgmt_ip' the VLAN and SVI will only be created on this device and added to uplink trunk. The VLAN and SVI on the parent switches must be created using network services data models. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inband_mgmt_subnet</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].inband_mgmt_subnet") | String |  |  | Format: ipv4_cidr | Optional IP subnet assigned to inband management SVIs on L2 switches (switches using port-channels as uplinks).<br>Parent l3leafs will have SVI with "ip virtual-router" and host-route injection based on ARP.<br>This allows all l3leafs to reuse the same subnet across multiple racks without VXLAN extension.<br>SVI IP address will be assigned as follows:<br>virtual-router: <subnet> + 1<br>l3leaf A      : <subnet> + 2 (same IP on all l3leaf A)<br>l3leaf B      : <subnet> + 3 (same IP on all l3leaf B)<br>l2leafs       : <subnet> + 3 + <l2leaf id><br>GW on l2leafs : <subnet> + 1<br>Assign range larger than total l2leafs + 5<br><br>Setting is ignored if 'inband_mgmt_ip' is set.<br><br>This setting is applicable to L2 switches (switches using port-channel trunks as uplinks).<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inband_mgmt_ip</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].inband_mgmt_ip") | String |  |  | Format: ipv4_cidr | IP address assigned to the inband management interface set with 'inband_mgmt_vlan'.<br>This overrides 'inband_mgmt_subnet', hence all behavior of 'inband_mgmt_subnet' is removed.<br><br>If this is set the VLAN and SVI will only be created on the L2 switch and added to uplink trunk.<br>The VLAN and SVI on the parent switches must be created using network services data models.<br><br>This setting is applicable to L2 switches (switches using port-channel trunks as uplinks).<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inband_mgmt_gateway</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].inband_mgmt_gateway") | String |  |  | Format: ipv4 | Default gateway configured in the 'inband_mgmt_vrf' when using 'inband_mgmt_ip'. Otherwise gateway is derived from 'inband_mgmt_subnet' if set.<br><br>This setting is applicable to L2 switches (switches using port-channel trunks as uplinks).<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inband_mgmt_description</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].inband_mgmt_description") | String |  | Inband Management |  | Description configured on the Inband Management SVI.<br><br>This setting is only applied on the devices where it is set, it does not automatically affect any parent/child devices configuration, so it must be set on each applicable node/node-group/node-type as needed. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inband_mgmt_vlan_name</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].inband_mgmt_vlan_name") | String |  | Inband Management |  | Name configured on the Inband Management VLAN.<br>This setting is only applied on the devices where it is set, it does not automatically affect any parent/child devices configuration, so it must be set on each applicable node/node-group/node-type as needed. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inband_mgmt_vrf</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].inband_mgmt_vrf") | String |  | default |  | VRF configured on the Inband Management Interface.<br>The VRF is created if not already created by other means.<br>This setting is only applied on the devices where it is set, it does not automatically affect any parent/child devices configuration, so it must be set on each applicable node/node-group/node-type as needed. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inband_mgmt_mtu</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].inband_mgmt_mtu") | Integer |  | 1500 |  | MTU configured on the Inband Management Interface.<br>This setting is only applied on the devices where it is set, it does not automatically affect any parent/child devices configuration, so it must be set on each applicable node/node-group/node-type as needed. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inband_management_subnet</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].inband_management_subnet") <span style="color:red">deprecated</span> | String |  |  | Format: ipv4_cidr | Optional IP subnet assigned to inband management SVIs on L2 switches (switches using port-channels as uplinks).<br>Parent l3leafs will have SVI with "ip virtual-router" and host-route injection based on ARP.<br>This allows all l3leafs to reuse the same subnet across multiple racks without VXLAN extension.<br>SVI IP address will be assigned as follows:<br>virtual-router: <subnet> + 1<br>l3leaf A      : <subnet> + 2 (same IP on all l3leaf A)<br>l3leaf B      : <subnet> + 3 (same IP on all l3leaf B)<br>l2leafs       : <subnet> + 3 + <l2leaf id><br>GW on l2leafs : <subnet> + 1<br>Assign range larger than total l2leafs + 5<br><br>Setting is ignored if 'inband_mgmt_ip' is set.<br><br>This setting is applicable to L2 switches (switches using port-channel trunks as uplinks).<br><span style="color:red">This key is deprecated. Support will be removed in AVD version 5.0.0. Use <samp>inband_mgmt_subnet</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inband_management_vlan</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].inband_management_vlan") <span style="color:red">deprecated</span> | Integer |  | 4092 |  | VLAN number used for inband management on L2 switches (switches using port-channel trunks as uplinks).<br>When using 'inband_mgmt_subnet' the VLAN and SVIs will be created automatically on this switch as well as all 'uplink_switches'.<br>When using 'inband_mgmt_ip' the VLAN and SVI will only be created on this device and added to uplink trunk. The VLAN and SVI on the parent switches must be created using network services data models.<span style="color:red">This key is deprecated. Support will be removed in AVD version 5.0.0. Use <samp>inband_mgmt_vlan</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mpls_overlay_role</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].mpls_overlay_role") | String |  |  | Valid Values:<br>- client<br>- server<br>- none | Set the default mpls overlay role.<br>Acting role in overlay control plane.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;overlay_address_families</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].overlay_address_families") | List, items: String |  |  |  | Set the default overlay address families.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].overlay_address_families.[].&lt;str&gt;") | String |  |  | Valid Values:<br>- evpn<br>- vpn-ipv4<br>- vpn-ipv6 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mpls_route_reflectors</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].mpls_route_reflectors") | List, items: String |  |  |  | List of inventory hostname acting as MPLS route-reflectors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].mpls_route_reflectors.[].&lt;str&gt;") | String |  |  |  | Inventory_hostname_of_mpls_route_reflectors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp_cluster_id</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].bgp_cluster_id") | String |  |  |  | Set BGP cluster id. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ptp</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ptp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ptp.enabled") | Boolean |  | False |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;profile</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ptp.profile") | String |  | aes67-r16-2016 | Valid Values:<br>- aes67<br>- smpte2059-2<br>- aes67-r16-2016 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;domain</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ptp.domain") | Integer |  | 127 | Min: 0<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority1</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ptp.priority1") | Integer |  |  | Min: 0<br>Max: 255 | default -> automatically set based on node_type.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority2</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ptp.priority2") | Integer |  |  | Min: 0<br>Max: 255 | default -> (node_id modulus 256).<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;auto_clock_identity</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ptp.auto_clock_identity") | Boolean |  | True |  | If you prefer to have PTP clock identity be the system MAC-address of the switch, which is the default EOS behaviour, simply disable the automatic PTP clock identity.<br>default -> (clock_identity_prefix = 00:1C:73 (default)) + (PTP priority 1 as HEX) + ":00:" + (PTP priority 2 as HEX).<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;clock_identity_prefix</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ptp.clock_identity_prefix") | String |  |  |  | PTP clock idetentiy 3-byte prefix. i.e. "01:02:03".<br>By default the 3-byte prefix is "00:1C:73".<br>This can be overridden if auto_clock_identity is set to true (which is the default).<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;clock_identity</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ptp.clock_identity") | String |  |  |  | Set PTP clock identity manually. 6-byte value i.e. "01:02:03:04:05:06".<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_ip</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ptp.source_ip") | String |  |  |  | By default in EOS, PTP packets are sourced with an IP address from the routed port or from the relevant SVI, which is the recommended behaviour.<br>This can be set manually if required, for example, to a value of "10.1.2.3".<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ttl</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ptp.ttl") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;forward_unicast</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ptp.forward_unicast") | Boolean |  | False |  | Enable PTP unicast forwarding.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dscp</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ptp.dscp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;general_messages</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ptp.dscp.general_messages") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;event_messages</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ptp.dscp.event_messages") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;monitor</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ptp.monitor") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ptp.monitor.enabled") | Boolean |  | True |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;threshold</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ptp.monitor.threshold") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;offset_from_master</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ptp.monitor.threshold.offset_from_master") | Integer |  | 250 | Min: 0<br>Max: 1000000000 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mean_path_delay</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ptp.monitor.threshold.mean_path_delay") | Integer |  | 1500 | Min: 0<br>Max: 1000000000 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;drop</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ptp.monitor.threshold.drop") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;offset_from_master</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ptp.monitor.threshold.drop.offset_from_master") | Integer |  |  | Min: 0<br>Max: 1000000000 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mean_path_delay</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ptp.monitor.threshold.drop.mean_path_delay") | Integer |  |  | Min: 0<br>Max: 1000000000 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;missing_message</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ptp.monitor.missing_message") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;intervals</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ptp.monitor.missing_message.intervals") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;announce</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ptp.monitor.missing_message.intervals.announce") | Integer |  |  | Min: 2<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;follow_up</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ptp.monitor.missing_message.intervals.follow_up") | Integer |  |  | Min: 2<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sync</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ptp.monitor.missing_message.intervals.sync") | Integer |  |  | Min: 2<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sequence_ids</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ptp.monitor.missing_message.sequence_ids") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ptp.monitor.missing_message.sequence_ids.enabled") | Boolean |  | True |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;announce</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ptp.monitor.missing_message.sequence_ids.announce") | Integer |  | 3 | Min: 2<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;delay_resp</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ptp.monitor.missing_message.sequence_ids.delay_resp") | Integer |  | 3 | Min: 2<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;follow_up</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ptp.monitor.missing_message.sequence_ids.follow_up") | Integer |  | 3 | Min: 2<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sync</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].ptp.monitor.missing_message.sequence_ids.sync") | Integer |  | 3 | Min: 2<br>Max: 255 |  |

=== "YAML"

    ```yaml
    <node_type_keys.key>:
      defaults:
        id: <int>
        platform: <str>
        mac_address: <str>
        system_mac_address: <str>
        serial_number: <str>
        rack: <str>
        mgmt_ip: <str>
        ipv6_mgmt_ip: <str>
        mgmt_interface: <str>
        link_tracking:
          enabled: <bool>
          groups:
            - name: <str>
              recovery_delay: <int>
              links_minimum: <int>
        lacp_port_id_range:
          enabled: <bool>
          size: <int>
          offset: <int>
        always_configure_ip_routing: <bool>
        raw_eos_cli: <str>
        structured_config: <dict>
        uplink_ipv4_pool: <str>
        uplink_interfaces:
          - <str>
        uplink_switch_interfaces:
          - <str>
        uplink_switches:
          - <str>
        uplink_interface_speed: <str>
        max_uplink_switches: <int>
        max_parallel_uplinks: <int>
        uplink_bfd: <bool>
        uplink_native_vlan: <int>
        uplink_ptp:
          enable: <bool>
        uplink_macsec:
          profile: <str>
        uplink_structured_config: <dict>
        mlag_port_channel_structured_config: <dict>
        mlag_peer_vlan_structured_config: <dict>
        mlag_peer_l3_vlan_structured_config: <dict>
        short_esi: <str>
        isis_system_id_prefix: <str>
        isis_maximum_paths: <int>
        is_type: <str>
        node_sid_base: <int>
        loopback_ipv4_pool: <str>
        vtep_loopback_ipv4_pool: <str>
        loopback_ipv4_offset: <int>
        loopback_ipv6_pool: <str>
        loopback_ipv6_offset: <int>
        vtep_loopback: <str>
        bgp_as: <str>
        bgp_defaults:
          - <str>
        evpn_role: <str>
        evpn_route_servers:
          - <str>
        evpn_services_l2_only: <bool>
        filter:
          tenants:
            - <str>
          tags:
            - <str>
          always_include_vrfs_in_tenants:
            - <str>
          only_vlans_in_use: <bool>
        igmp_snooping_enabled: <bool>
        evpn_gateway:
          remote_peers:
            - hostname: <str>
              ip_address: <str>
              bgp_as: <str>
          evpn_l2:
            enabled: <bool>
          evpn_l3:
            enabled: <bool>
            inter_domain: <bool>
        ipvpn_gateway:
          enabled: <bool>
          evpn_domain_id: <str>
          ipvpn_domain_id: <str>
          enable_d_path: <bool>
          maximum_routes: <int>
          local_as: <str>
          address_families:
            - <str>
          remote_peers:
            - hostname: <str>
              ip_address: <str>
              bgp_as: <str>
        mlag: <bool>
        mlag_dual_primary_detection: <bool>
        mlag_ibgp_origin_incomplete: <bool>
        mlag_interfaces:
          - <str>
        mlag_interfaces_speed: <str>
        mlag_peer_l3_vlan: <int>
        mlag_peer_l3_ipv4_pool: <str>
        mlag_peer_vlan: <int>
        mlag_peer_link_allowed_vlans: <str>
        mlag_peer_ipv4_pool: <str>
        mlag_port_channel_id: <int>
        mlag_domain_id: <str>
        spanning_tree_mode: <str>
        spanning_tree_priority: <int>
        spanning_tree_root_super: <bool>
        virtual_router_mac_address: <str>
        inband_mgmt_interface: <str>
        inband_mgmt_vlan: <int>
        inband_mgmt_subnet: <str>
        inband_mgmt_ip: <str>
        inband_mgmt_gateway: <str>
        inband_mgmt_description: <str>
        inband_mgmt_vlan_name: <str>
        inband_mgmt_vrf: <str>
        inband_mgmt_mtu: <int>
        inband_management_subnet: <str>
        inband_management_vlan: <int>
        mpls_overlay_role: <str>
        overlay_address_families:
          - <str>
        mpls_route_reflectors:
          - <str>
        bgp_cluster_id: <str>
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
              id: <int>
              platform: <str>
              mac_address: <str>
              system_mac_address: <str>
              serial_number: <str>
              rack: <str>
              mgmt_ip: <str>
              ipv6_mgmt_ip: <str>
              mgmt_interface: <str>
              link_tracking:
                enabled: <bool>
                groups:
                  - name: <str>
                    recovery_delay: <int>
                    links_minimum: <int>
              lacp_port_id_range:
                enabled: <bool>
                size: <int>
                offset: <int>
              always_configure_ip_routing: <bool>
              raw_eos_cli: <str>
              structured_config: <dict>
              uplink_ipv4_pool: <str>
              uplink_interfaces:
                - <str>
              uplink_switch_interfaces:
                - <str>
              uplink_switches:
                - <str>
              uplink_interface_speed: <str>
              max_uplink_switches: <int>
              max_parallel_uplinks: <int>
              uplink_bfd: <bool>
              uplink_native_vlan: <int>
              uplink_ptp:
                enable: <bool>
              uplink_macsec:
                profile: <str>
              uplink_structured_config: <dict>
              mlag_port_channel_structured_config: <dict>
              mlag_peer_vlan_structured_config: <dict>
              mlag_peer_l3_vlan_structured_config: <dict>
              short_esi: <str>
              isis_system_id_prefix: <str>
              isis_maximum_paths: <int>
              is_type: <str>
              node_sid_base: <int>
              loopback_ipv4_pool: <str>
              vtep_loopback_ipv4_pool: <str>
              loopback_ipv4_offset: <int>
              loopback_ipv6_pool: <str>
              loopback_ipv6_offset: <int>
              vtep_loopback: <str>
              bgp_as: <str>
              bgp_defaults:
                - <str>
              evpn_role: <str>
              evpn_route_servers:
                - <str>
              evpn_services_l2_only: <bool>
              filter:
                tenants:
                  - <str>
                tags:
                  - <str>
                always_include_vrfs_in_tenants:
                  - <str>
                only_vlans_in_use: <bool>
              igmp_snooping_enabled: <bool>
              evpn_gateway:
                remote_peers:
                  - hostname: <str>
                    ip_address: <str>
                    bgp_as: <str>
                evpn_l2:
                  enabled: <bool>
                evpn_l3:
                  enabled: <bool>
                  inter_domain: <bool>
              ipvpn_gateway:
                enabled: <bool>
                evpn_domain_id: <str>
                ipvpn_domain_id: <str>
                enable_d_path: <bool>
                maximum_routes: <int>
                local_as: <str>
                address_families:
                  - <str>
                remote_peers:
                  - hostname: <str>
                    ip_address: <str>
                    bgp_as: <str>
              mlag: <bool>
              mlag_dual_primary_detection: <bool>
              mlag_ibgp_origin_incomplete: <bool>
              mlag_interfaces:
                - <str>
              mlag_interfaces_speed: <str>
              mlag_peer_l3_vlan: <int>
              mlag_peer_l3_ipv4_pool: <str>
              mlag_peer_vlan: <int>
              mlag_peer_link_allowed_vlans: <str>
              mlag_peer_ipv4_pool: <str>
              mlag_port_channel_id: <int>
              mlag_domain_id: <str>
              spanning_tree_mode: <str>
              spanning_tree_priority: <int>
              spanning_tree_root_super: <bool>
              virtual_router_mac_address: <str>
              inband_mgmt_interface: <str>
              inband_mgmt_vlan: <int>
              inband_mgmt_subnet: <str>
              inband_mgmt_ip: <str>
              inband_mgmt_gateway: <str>
              inband_mgmt_description: <str>
              inband_mgmt_vlan_name: <str>
              inband_mgmt_vrf: <str>
              inband_mgmt_mtu: <int>
              inband_management_subnet: <str>
              inband_management_vlan: <int>
              mpls_overlay_role: <str>
              overlay_address_families:
                - <str>
              mpls_route_reflectors:
                - <str>
              bgp_cluster_id: <str>
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
          id: <int>
          platform: <str>
          mac_address: <str>
          system_mac_address: <str>
          serial_number: <str>
          rack: <str>
          mgmt_ip: <str>
          ipv6_mgmt_ip: <str>
          mgmt_interface: <str>
          link_tracking:
            enabled: <bool>
            groups:
              - name: <str>
                recovery_delay: <int>
                links_minimum: <int>
          lacp_port_id_range:
            enabled: <bool>
            size: <int>
            offset: <int>
          always_configure_ip_routing: <bool>
          raw_eos_cli: <str>
          structured_config: <dict>
          uplink_ipv4_pool: <str>
          uplink_interfaces:
            - <str>
          uplink_switch_interfaces:
            - <str>
          uplink_switches:
            - <str>
          uplink_interface_speed: <str>
          max_uplink_switches: <int>
          max_parallel_uplinks: <int>
          uplink_bfd: <bool>
          uplink_native_vlan: <int>
          uplink_ptp:
            enable: <bool>
          uplink_macsec:
            profile: <str>
          uplink_structured_config: <dict>
          mlag_port_channel_structured_config: <dict>
          mlag_peer_vlan_structured_config: <dict>
          mlag_peer_l3_vlan_structured_config: <dict>
          short_esi: <str>
          isis_system_id_prefix: <str>
          isis_maximum_paths: <int>
          is_type: <str>
          node_sid_base: <int>
          loopback_ipv4_pool: <str>
          vtep_loopback_ipv4_pool: <str>
          loopback_ipv4_offset: <int>
          loopback_ipv6_pool: <str>
          loopback_ipv6_offset: <int>
          vtep_loopback: <str>
          bgp_as: <str>
          bgp_defaults:
            - <str>
          evpn_role: <str>
          evpn_route_servers:
            - <str>
          evpn_services_l2_only: <bool>
          filter:
            tenants:
              - <str>
            tags:
              - <str>
            always_include_vrfs_in_tenants:
              - <str>
            only_vlans_in_use: <bool>
          igmp_snooping_enabled: <bool>
          evpn_gateway:
            remote_peers:
              - hostname: <str>
                ip_address: <str>
                bgp_as: <str>
            evpn_l2:
              enabled: <bool>
            evpn_l3:
              enabled: <bool>
              inter_domain: <bool>
          ipvpn_gateway:
            enabled: <bool>
            evpn_domain_id: <str>
            ipvpn_domain_id: <str>
            enable_d_path: <bool>
            maximum_routes: <int>
            local_as: <str>
            address_families:
              - <str>
            remote_peers:
              - hostname: <str>
                ip_address: <str>
                bgp_as: <str>
          mlag: <bool>
          mlag_dual_primary_detection: <bool>
          mlag_ibgp_origin_incomplete: <bool>
          mlag_interfaces:
            - <str>
          mlag_interfaces_speed: <str>
          mlag_peer_l3_vlan: <int>
          mlag_peer_l3_ipv4_pool: <str>
          mlag_peer_vlan: <int>
          mlag_peer_link_allowed_vlans: <str>
          mlag_peer_ipv4_pool: <str>
          mlag_port_channel_id: <int>
          mlag_domain_id: <str>
          spanning_tree_mode: <str>
          spanning_tree_priority: <int>
          spanning_tree_root_super: <bool>
          virtual_router_mac_address: <str>
          inband_mgmt_interface: <str>
          inband_mgmt_vlan: <int>
          inband_mgmt_subnet: <str>
          inband_mgmt_ip: <str>
          inband_mgmt_gateway: <str>
          inband_mgmt_description: <str>
          inband_mgmt_vlan_name: <str>
          inband_mgmt_vrf: <str>
          inband_mgmt_mtu: <int>
          inband_management_subnet: <str>
          inband_management_vlan: <int>
          mpls_overlay_role: <str>
          overlay_address_families:
            - <str>
          mpls_route_reflectors:
            - <str>
          bgp_cluster_id: <str>
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
          id: <int>
          platform: <str>
          mac_address: <str>
          system_mac_address: <str>
          serial_number: <str>
          rack: <str>
          mgmt_ip: <str>
          ipv6_mgmt_ip: <str>
          mgmt_interface: <str>
          link_tracking:
            enabled: <bool>
            groups:
              - name: <str>
                recovery_delay: <int>
                links_minimum: <int>
          lacp_port_id_range:
            enabled: <bool>
            size: <int>
            offset: <int>
          always_configure_ip_routing: <bool>
          raw_eos_cli: <str>
          structured_config: <dict>
          uplink_ipv4_pool: <str>
          uplink_interfaces:
            - <str>
          uplink_switch_interfaces:
            - <str>
          uplink_switches:
            - <str>
          uplink_interface_speed: <str>
          max_uplink_switches: <int>
          max_parallel_uplinks: <int>
          uplink_bfd: <bool>
          uplink_native_vlan: <int>
          uplink_ptp:
            enable: <bool>
          uplink_macsec:
            profile: <str>
          uplink_structured_config: <dict>
          mlag_port_channel_structured_config: <dict>
          mlag_peer_vlan_structured_config: <dict>
          mlag_peer_l3_vlan_structured_config: <dict>
          short_esi: <str>
          isis_system_id_prefix: <str>
          isis_maximum_paths: <int>
          is_type: <str>
          node_sid_base: <int>
          loopback_ipv4_pool: <str>
          vtep_loopback_ipv4_pool: <str>
          loopback_ipv4_offset: <int>
          loopback_ipv6_pool: <str>
          loopback_ipv6_offset: <int>
          vtep_loopback: <str>
          bgp_as: <str>
          bgp_defaults:
            - <str>
          evpn_role: <str>
          evpn_route_servers:
            - <str>
          evpn_services_l2_only: <bool>
          filter:
            tenants:
              - <str>
            tags:
              - <str>
            always_include_vrfs_in_tenants:
              - <str>
            only_vlans_in_use: <bool>
          igmp_snooping_enabled: <bool>
          evpn_gateway:
            remote_peers:
              - hostname: <str>
                ip_address: <str>
                bgp_as: <str>
            evpn_l2:
              enabled: <bool>
            evpn_l3:
              enabled: <bool>
              inter_domain: <bool>
          ipvpn_gateway:
            enabled: <bool>
            evpn_domain_id: <str>
            ipvpn_domain_id: <str>
            enable_d_path: <bool>
            maximum_routes: <int>
            local_as: <str>
            address_families:
              - <str>
            remote_peers:
              - hostname: <str>
                ip_address: <str>
                bgp_as: <str>
          mlag: <bool>
          mlag_dual_primary_detection: <bool>
          mlag_ibgp_origin_incomplete: <bool>
          mlag_interfaces:
            - <str>
          mlag_interfaces_speed: <str>
          mlag_peer_l3_vlan: <int>
          mlag_peer_l3_ipv4_pool: <str>
          mlag_peer_vlan: <int>
          mlag_peer_link_allowed_vlans: <str>
          mlag_peer_ipv4_pool: <str>
          mlag_port_channel_id: <int>
          mlag_domain_id: <str>
          spanning_tree_mode: <str>
          spanning_tree_priority: <int>
          spanning_tree_root_super: <bool>
          virtual_router_mac_address: <str>
          inband_mgmt_interface: <str>
          inband_mgmt_vlan: <int>
          inband_mgmt_subnet: <str>
          inband_mgmt_ip: <str>
          inband_mgmt_gateway: <str>
          inband_mgmt_description: <str>
          inband_mgmt_vlan_name: <str>
          inband_mgmt_vrf: <str>
          inband_mgmt_mtu: <int>
          inband_management_subnet: <str>
          inband_management_vlan: <int>
          mpls_overlay_role: <str>
          overlay_address_families:
            - <str>
          mpls_route_reflectors:
            - <str>
          bgp_cluster_id: <str>
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

## AVD Data Conversion Mode

Conversion Mode for AVD input data conversion.
Input data conversion will perform type conversion of input variables as defined in the schema.
The type conversion is intended to help the user to identify minor issues with the input data, while still allowing the data to be validated.
During conversion, messages will generated with information about the host(s) and key(s) which required conversion.
"disabled" means that conversion will not run - avoid this since conversion is also handling data deprecation and upgrade.
"error" will produce error messages and fail the task.
"warning" will produce warning messages.
"info" will produce regular log messages.
"debug" will produce hidden debug messages viewable with -v.
"quiet" will not produce any messages

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>avd_data_conversion_mode</samp>](## "avd_data_conversion_mode") | String |  | debug | Valid Values:<br>- disabled<br>- error<br>- warning<br>- info<br>- debug<br>- quiet |  |

=== "YAML"

    ```yaml
    avd_data_conversion_mode: <str>
    ```

## AVD Data Validation Mode

Validation Mode for AVD input data validation.
Input data validation will validate the input variables according to the schema.
During validation, messages will generated with information about the host(s) and key(s) which failed validation.
"disabled" means that validation will not run.
"error" will produce error messages and fail the task.
"warning" will produce warning messages.
"info" will produce regular log messages.
"debug" will produce hidden debug messages viewable with -v.

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>avd_data_validation_mode</samp>](## "avd_data_validation_mode") | String |  | warning | Valid Values:<br>- disabled<br>- error<br>- warning<br>- info<br>- debug |  |

=== "YAML"

    ```yaml
    avd_data_validation_mode: <str>
    ```

## BFD Multihop

BFD Multihop tuning

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>bfd_multihop</samp>](## "bfd_multihop") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;interval</samp>](## "bfd_multihop.interval") | Integer |  | 300 | Min: 50<br>Max: 60000 |  |
    | [<samp>&nbsp;&nbsp;min_rx</samp>](## "bfd_multihop.min_rx") | Integer |  | 300 | Min: 50<br>Max: 60000 |  |
    | [<samp>&nbsp;&nbsp;multiplier</samp>](## "bfd_multihop.multiplier") | Integer |  | 3 | Min: 3<br>Max: 50 |  |

=== "YAML"

    ```yaml
    bfd_multihop:
      interval: <int>
      min_rx: <int>
      multiplier: <int>
    ```

## BGP As

AS number to use to configure overlay when "overlay_routing_protocol" == ibgp

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>bgp_as</samp>](## "bgp_as") | String |  |  |  |  |

=== "YAML"

    ```yaml
    bgp_as: <str>
    ```

## BGP Default IPv4 Unicast

Default activation of IPv4 unicast address-family on all IPv4 neighbors.
It is best practice to disable activation.

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>bgp_default_ipv4_unicast</samp>](## "bgp_default_ipv4_unicast") | Boolean |  | False |  |  |

=== "YAML"

    ```yaml
    bgp_default_ipv4_unicast: <bool>
    ```

## BGP Distance

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>bgp_distance</samp>](## "bgp_distance") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;external_routes</samp>](## "bgp_distance.external_routes") | Integer | Required |  | Min: 1<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;internal_routes</samp>](## "bgp_distance.internal_routes") | Integer | Required |  | Min: 1<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;local_routes</samp>](## "bgp_distance.local_routes") | Integer | Required |  | Min: 1<br>Max: 255 |  |

=== "YAML"

    ```yaml
    bgp_distance:
      external_routes: <int>
      internal_routes: <int>
      local_routes: <int>
    ```

## BGP Ecmp

Maximum ECMP for BGP multi-path

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>bgp_ecmp</samp>](## "bgp_ecmp") | Integer |  | 4 |  |  |

=== "YAML"

    ```yaml
    bgp_ecmp: <int>
    ```

## BGP Graceful Restart

Graceful BGP restart allows a BGP speaker with separate control plane and data plane processing to continue forwarding traffic during a BGP restart.
Its neighbors (receiving speakers) may retain routing information from the restarting speaker while a BGP session with it is being re-established, reducing route flapping.

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>bgp_graceful_restart</samp>](## "bgp_graceful_restart") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;enabled</samp>](## "bgp_graceful_restart.enabled") | Boolean |  | True |  | Enable or disable graceful restart helper mode for all BGP peers. |
    | [<samp>&nbsp;&nbsp;restart_time</samp>](## "bgp_graceful_restart.restart_time") | Integer |  | 300 | Min: 1<br>Max: 3600 | Restart time in seconds. |

=== "YAML"

    ```yaml
    bgp_graceful_restart:
      enabled: <bool>
      restart_time: <int>
    ```

## BGP Maximum Paths

Maximum Paths for BGP multi-path

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>bgp_maximum_paths</samp>](## "bgp_maximum_paths") | Integer |  | 4 | Min: 1<br>Max: 512 |  |

=== "YAML"

    ```yaml
    bgp_maximum_paths: <int>
    ```

## BGP Mesh Pes

Whether to configure an iBGP full mesh between PEs, either because there is no RR used or other reasons.

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>bgp_mesh_pes</samp>](## "bgp_mesh_pes") | Boolean |  | False |  |  |

=== "YAML"

    ```yaml
    bgp_mesh_pes: <bool>
    ```

## BGP Peer Groups

Leverage an Arista EOS switch to generate the encrypted password using the correct peer group name.
Note that the name of the peer groups use '-' instead of '_' in EOS configuration.

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>bgp_peer_groups</samp>](## "bgp_peer_groups") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;ipv4_underlay_peers</samp>](## "bgp_peer_groups.ipv4_underlay_peers") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "bgp_peer_groups.ipv4_underlay_peers.name") | String |  | IPv4-UNDERLAY-PEERS |  | Name of peer group. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;password</samp>](## "bgp_peer_groups.ipv4_underlay_peers.password") | String |  |  |  | Type 7 encrypted password. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "bgp_peer_groups.ipv4_underlay_peers.structured_config") | Dictionary |  |  |  | Custom structured config added under router_bgp.peer_groups.<name> for eos_cli_config_gen |
    | [<samp>&nbsp;&nbsp;mlag_ipv4_underlay_peer</samp>](## "bgp_peer_groups.mlag_ipv4_underlay_peer") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "bgp_peer_groups.mlag_ipv4_underlay_peer.name") | String |  | MLAG-IPv4-UNDERLAY-PEER |  | Name of peer group. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;password</samp>](## "bgp_peer_groups.mlag_ipv4_underlay_peer.password") | String |  |  |  | Type 7 encrypted password. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "bgp_peer_groups.mlag_ipv4_underlay_peer.structured_config") | Dictionary |  |  |  | Custom structured config added under router_bgp.peer_groups.<name> for eos_cli_config_gen |
    | [<samp>&nbsp;&nbsp;evpn_overlay_peers</samp>](## "bgp_peer_groups.evpn_overlay_peers") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "bgp_peer_groups.evpn_overlay_peers.name") | String |  | EVPN-OVERLAY-PEERS |  | Name of peer group. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;password</samp>](## "bgp_peer_groups.evpn_overlay_peers.password") | String |  |  |  | Type 7 encrypted password. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "bgp_peer_groups.evpn_overlay_peers.structured_config") | Dictionary |  |  |  | Custom structured config added under router_bgp.peer_groups.<name> for eos_cli_config_gen |
    | [<samp>&nbsp;&nbsp;evpn_overlay_core</samp>](## "bgp_peer_groups.evpn_overlay_core") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "bgp_peer_groups.evpn_overlay_core.name") | String |  | EVPN-OVERLAY-CORE |  | Name of peer group. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;password</samp>](## "bgp_peer_groups.evpn_overlay_core.password") | String |  |  |  | Type 7 encrypted password. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "bgp_peer_groups.evpn_overlay_core.structured_config") | Dictionary |  |  |  | Custom structured config added under router_bgp.peer_groups.<name> for eos_cli_config_gen |
    | [<samp>&nbsp;&nbsp;mpls_overlay_peers</samp>](## "bgp_peer_groups.mpls_overlay_peers") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "bgp_peer_groups.mpls_overlay_peers.name") | String |  | MPLS-OVERLAY-PEERS |  | Name of peer group. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;password</samp>](## "bgp_peer_groups.mpls_overlay_peers.password") | String |  |  |  | Type 7 encrypted password. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "bgp_peer_groups.mpls_overlay_peers.structured_config") | Dictionary |  |  |  | Custom structured config added under router_bgp.peer_groups.<name> for eos_cli_config_gen |
    | [<samp>&nbsp;&nbsp;rr_overlay_peers</samp>](## "bgp_peer_groups.rr_overlay_peers") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "bgp_peer_groups.rr_overlay_peers.name") | String |  | RR-OVERLAY-PEERS |  | Name of peer group. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;password</samp>](## "bgp_peer_groups.rr_overlay_peers.password") | String |  |  |  | Type 7 encrypted password. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "bgp_peer_groups.rr_overlay_peers.structured_config") | Dictionary |  |  |  | Custom structured config added under router_bgp.peer_groups.<name> for eos_cli_config_gen |
    | [<samp>&nbsp;&nbsp;ipvpn_gateway_peers</samp>](## "bgp_peer_groups.ipvpn_gateway_peers") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "bgp_peer_groups.ipvpn_gateway_peers.name") | String |  | IPVPN-GATEWAY-PEERS |  | Name of peer group. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;password</samp>](## "bgp_peer_groups.ipvpn_gateway_peers.password") | String |  |  |  | Type 7 encrypted password. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "bgp_peer_groups.ipvpn_gateway_peers.structured_config") | Dictionary |  |  |  | Custom structured config added under router_bgp.peer_groups.<name> for eos_cli_config_gen |
    | [<samp>&nbsp;&nbsp;IPv4_UNDERLAY_PEERS</samp>](## "bgp_peer_groups.IPv4_UNDERLAY_PEERS") <span style="color:red">removed</span> | Dictionary |  |  |  | <span style="color:red">This key was removed. Support was removed in AVD version 4.0.0. Use <samp>bgp_peer_groups.ipv4_underlay_peers</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;MLAG_IPv4_UNDERLAY_PEER</samp>](## "bgp_peer_groups.MLAG_IPv4_UNDERLAY_PEER") <span style="color:red">removed</span> | Dictionary |  |  |  | <span style="color:red">This key was removed. Support was removed in AVD version 4.0.0. Use <samp>bgp_peer_groups.mlag_ipv4_underlay_peer</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;EVPN_OVERLAY_PEERS</samp>](## "bgp_peer_groups.EVPN_OVERLAY_PEERS") <span style="color:red">removed</span> | Dictionary |  |  |  | <span style="color:red">This key was removed. Support was removed in AVD version 4.0.0. Use <samp>bgp_peer_groups.evpn_overlay_peers</samp> instead.</span> |

=== "YAML"

    ```yaml
    bgp_peer_groups:
      ipv4_underlay_peers:
        name: <str>
        password: <str>
        structured_config: <dict>
      mlag_ipv4_underlay_peer:
        name: <str>
        password: <str>
        structured_config: <dict>
      evpn_overlay_peers:
        name: <str>
        password: <str>
        structured_config: <dict>
      evpn_overlay_core:
        name: <str>
        password: <str>
        structured_config: <dict>
      mpls_overlay_peers:
        name: <str>
        password: <str>
        structured_config: <dict>
      rr_overlay_peers:
        name: <str>
        password: <str>
        structured_config: <dict>
      ipvpn_gateway_peers:
        name: <str>
        password: <str>
        structured_config: <dict>
    ```

## BGP Update Wait For Convergence

Disables FIB updates and route advertisement when the BGP instance is initiated until the BGP convergence state is reached.

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>bgp_update_wait_for_convergence</samp>](## "bgp_update_wait_for_convergence") | Boolean |  |  |  |  |

=== "YAML"

    ```yaml
    bgp_update_wait_for_convergence: <bool>
    ```

## BGP Update Wait Install

Do not advertise reachability to a prefix until that prefix has been installed in hardware.
This will eliminate any temporary black holes due to a BGP speaker advertising reachability to a prefix that may not yet be installed into the forwarding plane.

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>bgp_update_wait_install</samp>](## "bgp_update_wait_install") | Boolean |  |  |  |  |

=== "YAML"

    ```yaml
    bgp_update_wait_install: <bool>
    ```

## Connected Endpoints Keys

Define connected endpoints keys to define the grouping of endpoints connecting to the fabric.
This lets you specify various keys to better organize/group your data.
The connected endpoints keys should be defined in the top level group_var for the fabric.

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>connected_endpoints_keys</samp>](## "connected_endpoints_keys") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;- key</samp>](## "connected_endpoints_keys.[].key") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "connected_endpoints_keys.[].type") | String |  |  |  | Type used for documentation. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "connected_endpoints_keys.[].description") | String |  |  |  | Description used for documentation. |

=== "YAML"

    ```yaml
    connected_endpoints_keys:
      - key: <str>
        type: <str>
        description: <str>
    ```

## Core Interfaces

The `core_interfaces` data model can be used to configure L3 P2P links anywhere in the fabric.
It can be between two switches that are already part of the fabric inventory, or it can be towards another device,
where only one end of the link is on a switch in the fabric.

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>core_interfaces</samp>](## "core_interfaces") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;p2p_links_ip_pools</samp>](## "core_interfaces.p2p_links_ip_pools") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "core_interfaces.p2p_links_ip_pools.[].name") | String | Required, Unique |  |  | P2P pool name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4_pool</samp>](## "core_interfaces.p2p_links_ip_pools.[].ipv4_pool") | String |  |  |  | IPv4 address/Mask. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefix_size</samp>](## "core_interfaces.p2p_links_ip_pools.[].prefix_size") | Integer |  | 31 | Min: 8<br>Max: 31 | Subnet mask size. |
    | [<samp>&nbsp;&nbsp;p2p_links_profiles</samp>](## "core_interfaces.p2p_links_profiles") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "core_interfaces.p2p_links_profiles.[].name") | String | Required, Unique |  |  | P2P profile name. Any variable supported under p2p_links can be inherited from a profile. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;id</samp>](## "core_interfaces.p2p_links_profiles.[].id") | Integer |  |  |  | Unique id per subnet_summary. Used to calculate ip addresses.<br>Required with ip_pool. ID starting from 1.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;speed</samp>](## "core_interfaces.p2p_links_profiles.[].speed") | String |  |  |  | The values can be speed or auto speed or forced speed. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_pool</samp>](## "core_interfaces.p2p_links_profiles.[].ip_pool") | String |  |  |  | P2P pool name. IP Pool defined under p2p_links_ip_pools. A /31 will be taken from the pool per P2P link |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;subnet</samp>](## "core_interfaces.p2p_links_profiles.[].subnet") | String |  |  |  | IPv4 address/Mask. Subnet used on this P2P link. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip</samp>](## "core_interfaces.p2p_links_profiles.[].ip") | List, items: String |  |  |  | Specific IP addresses used on this P2P link. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "core_interfaces.p2p_links_profiles.[].ip.[].&lt;str&gt;") | String |  |  |  | Node IPv4 address/Mask. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_enable</samp>](## "core_interfaces.p2p_links_profiles.[].ipv6_enable") | Boolean |  | False |  | Allows turning on ipv6 for the link or profile (also autodetected based on underlay_rfc5549 and include_in_underlay_protocol). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "core_interfaces.p2p_links_profiles.[].nodes") | List, items: String |  |  |  | Nodes where this link should be configured. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "core_interfaces.p2p_links_profiles.[].nodes.[].&lt;str&gt;") | String |  |  |  | The values can be < node_a >, < node_b >.<br>ex.- [ core-1-isis-sr-ldp, core-2-ospf-ldp ].<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interfaces</samp>](## "core_interfaces.p2p_links_profiles.[].interfaces") | List, items: String |  |  |  | Interfaces where this link should be configured and Required unless using port-channels. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "core_interfaces.p2p_links_profiles.[].interfaces.[].&lt;str&gt;") | String |  |  |  | The value can be like < node_a_interface >, < node_b_interface >.<br>ex. - [ Ethernet2, Ethernet2 ].<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;as</samp>](## "core_interfaces.p2p_links_profiles.[].as") | List, items: String |  |  |  | AS numbers for BGP.<br>Required with bgp peering.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "core_interfaces.p2p_links_profiles.[].as.[].&lt;str&gt;") | String |  |  |  | The values can be like ["node_a_as", "node_b_as"]. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;descriptions</samp>](## "core_interfaces.p2p_links_profiles.[].descriptions") | List, items: String |  |  |  | Interface description. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "core_interfaces.p2p_links_profiles.[].descriptions.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_in_underlay_protocol</samp>](## "core_interfaces.p2p_links_profiles.[].include_in_underlay_protocol") | Boolean |  | True |  | Add this interface to underlay routing protocol. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_hello_padding</samp>](## "core_interfaces.p2p_links_profiles.[].isis_hello_padding") | Boolean |  | False |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_metric</samp>](## "core_interfaces.p2p_links_profiles.[].isis_metric") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_circuit_type</samp>](## "core_interfaces.p2p_links_profiles.[].isis_circuit_type") | String |  |  | Valid Values:<br>- level-1<br>- level-2<br>- level-1-2 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_authentication_mode</samp>](## "core_interfaces.p2p_links_profiles.[].isis_authentication_mode") | String |  |  | Valid Values:<br>- md5<br>- text |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_authentication_key</samp>](## "core_interfaces.p2p_links_profiles.[].isis_authentication_key") | String |  |  |  | Type-7 encrypted password. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mpls_ip</samp>](## "core_interfaces.p2p_links_profiles.[].mpls_ip") | Boolean |  |  |  | MPLS parameters. Default value is true if switch.mpls_lsr is true. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mpls_ldp</samp>](## "core_interfaces.p2p_links_profiles.[].mpls_ldp") | Boolean |  |  |  | MPLS parameters. Default value is true for ldp underlay variants, otherwise false. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mtu</samp>](## "core_interfaces.p2p_links_profiles.[].mtu") | Integer |  |  |  | MTU for this P2P link. Default value same as p2p_uplinks_mtu. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bfd</samp>](## "core_interfaces.p2p_links_profiles.[].bfd") | Boolean |  | False |  | Enable BFD (only considered for BGP). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ptp</samp>](## "core_interfaces.p2p_links_profiles.[].ptp") | Dictionary |  |  |  | PTP parameters. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "core_interfaces.p2p_links_profiles.[].ptp.enabled") | Boolean |  | False |  | Enable PTP |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;qos_profile</samp>](## "core_interfaces.p2p_links_profiles.[].qos_profile") | String |  |  |  | QOS service profile. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;macsec_profile</samp>](## "core_interfaces.p2p_links_profiles.[].macsec_profile") | String |  |  |  | MAC security profile. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;port_channel</samp>](## "core_interfaces.p2p_links_profiles.[].port_channel") | Dictionary |  |  |  | Port-channel parameters. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "core_interfaces.p2p_links_profiles.[].port_channel.mode") | String |  | active |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes_child_interfaces</samp>](## "core_interfaces.p2p_links_profiles.[].port_channel.nodes_child_interfaces") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- node</samp>](## "core_interfaces.p2p_links_profiles.[].port_channel.nodes_child_interfaces.[].node") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interfaces</samp>](## "core_interfaces.p2p_links_profiles.[].port_channel.nodes_child_interfaces.[].interfaces") | List, items: String |  |  |  | List of node interfaces. Ex.- [ 'node1 interface1', 'node1 interface2' ]. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "core_interfaces.p2p_links_profiles.[].port_channel.nodes_child_interfaces.[].interfaces.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "core_interfaces.p2p_links_profiles.[].raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the point-to-point interface in the final EOS configuration. |
    | [<samp>&nbsp;&nbsp;p2p_links</samp>](## "core_interfaces.p2p_links") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- nodes</samp>](## "core_interfaces.p2p_links.[].nodes") | List, items: String | Required |  |  | Nodes where this link should be configured. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "core_interfaces.p2p_links.[].nodes.[].&lt;str&gt;") | String |  |  |  | The values can be < node_a >, < node_b >.<br>ex.- [ core-1-isis-sr-ldp, core-2-ospf-ldp ].<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;profile</samp>](## "core_interfaces.p2p_links.[].profile") | String |  |  |  | P2P profile name. Profile defined under p2p_profiles. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;id</samp>](## "core_interfaces.p2p_links.[].id") | Integer |  |  |  | Unique id per subnet_summary. Used to calculate ip addresses.<br>Required with ip_pool. ID starting from 1.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;speed</samp>](## "core_interfaces.p2p_links.[].speed") | String |  |  |  | The values can be speed or auto speed or forced speed. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_pool</samp>](## "core_interfaces.p2p_links.[].ip_pool") | String |  |  |  | P2P pool name. IP Pool defined under p2p_links_ip_pools. A /31 will be taken from the pool per P2P link |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;subnet</samp>](## "core_interfaces.p2p_links.[].subnet") | String |  |  |  | IPv4 address/Mask. Subnet used on this P2P link. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip</samp>](## "core_interfaces.p2p_links.[].ip") | List, items: String |  |  |  | Specific IP addresses used on this P2P link. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "core_interfaces.p2p_links.[].ip.[].&lt;str&gt;") | String |  |  |  | Node IPv4 address/Mask. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_enable</samp>](## "core_interfaces.p2p_links.[].ipv6_enable") | Boolean |  | False |  | Allows turning on ipv6 for the link or profile (also autodetected based on underlay_rfc5549 and include_in_underlay_protocol). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interfaces</samp>](## "core_interfaces.p2p_links.[].interfaces") | List, items: String |  |  |  | Interfaces where this link should be configured and Required unless using port-channels. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "core_interfaces.p2p_links.[].interfaces.[].&lt;str&gt;") | String |  |  |  | The value can be like < node_a_interface >, < node_b_interface >.<br>ex. - [ Ethernet2, Ethernet2 ].<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;as</samp>](## "core_interfaces.p2p_links.[].as") | List, items: String |  |  |  | AS numbers for BGP.<br>Required with bgp peering.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "core_interfaces.p2p_links.[].as.[].&lt;str&gt;") | String |  |  |  | The values can be like ["node_a_as", "node_b_as"]. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;descriptions</samp>](## "core_interfaces.p2p_links.[].descriptions") | List, items: String |  |  |  | Interface description. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "core_interfaces.p2p_links.[].descriptions.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_in_underlay_protocol</samp>](## "core_interfaces.p2p_links.[].include_in_underlay_protocol") | Boolean |  | True |  | Add this interface to underlay routing protocol. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_hello_padding</samp>](## "core_interfaces.p2p_links.[].isis_hello_padding") | Boolean |  | False |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_metric</samp>](## "core_interfaces.p2p_links.[].isis_metric") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_circuit_type</samp>](## "core_interfaces.p2p_links.[].isis_circuit_type") | String |  |  | Valid Values:<br>- level-1<br>- level-2<br>- level-1-2 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_authentication_mode</samp>](## "core_interfaces.p2p_links.[].isis_authentication_mode") | String |  |  | Valid Values:<br>- md5<br>- text |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_authentication_key</samp>](## "core_interfaces.p2p_links.[].isis_authentication_key") | String |  |  |  | Type-7 encrypted password. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mpls_ip</samp>](## "core_interfaces.p2p_links.[].mpls_ip") | Boolean |  |  |  | MPLS parameters. Default value is true if switch.mpls_lsr is true. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mpls_ldp</samp>](## "core_interfaces.p2p_links.[].mpls_ldp") | Boolean |  |  |  | MPLS parameters. Default value is true for ldp underlay variants, otherwise false. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mtu</samp>](## "core_interfaces.p2p_links.[].mtu") | Integer |  |  |  | MTU for this P2P link. Default value same as p2p_uplinks_mtu. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bfd</samp>](## "core_interfaces.p2p_links.[].bfd") | Boolean |  | False |  | Enable BFD (only considered for BGP). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ptp</samp>](## "core_interfaces.p2p_links.[].ptp") | Dictionary |  |  |  | PTP parameters. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "core_interfaces.p2p_links.[].ptp.enabled") | Boolean |  | False |  | Enable PTP |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;qos_profile</samp>](## "core_interfaces.p2p_links.[].qos_profile") | String |  |  |  | QOS service profile. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;macsec_profile</samp>](## "core_interfaces.p2p_links.[].macsec_profile") | String |  |  |  | MAC security profile. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;port_channel</samp>](## "core_interfaces.p2p_links.[].port_channel") | Dictionary |  |  |  | Port-channel parameters. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "core_interfaces.p2p_links.[].port_channel.mode") | String |  | active |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes_child_interfaces</samp>](## "core_interfaces.p2p_links.[].port_channel.nodes_child_interfaces") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- node</samp>](## "core_interfaces.p2p_links.[].port_channel.nodes_child_interfaces.[].node") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interfaces</samp>](## "core_interfaces.p2p_links.[].port_channel.nodes_child_interfaces.[].interfaces") | List, items: String |  |  |  | List of node interfaces. Ex.- [ 'node1 interface1', 'node1 interface2' ]. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "core_interfaces.p2p_links.[].port_channel.nodes_child_interfaces.[].interfaces.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "core_interfaces.p2p_links.[].raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the point-to-point interface in the final EOS configuration. |

=== "YAML"

    ```yaml
    core_interfaces:
      p2p_links_ip_pools:
        - name: <str>
          ipv4_pool: <str>
          prefix_size: <int>
      p2p_links_profiles:
        - name: <str>
          id: <int>
          speed: <str>
          ip_pool: <str>
          subnet: <str>
          ip:
            - <str>
          ipv6_enable: <bool>
          nodes:
            - <str>
          interfaces:
            - <str>
          as:
            - <str>
          descriptions:
            - <str>
          include_in_underlay_protocol: <bool>
          isis_hello_padding: <bool>
          isis_metric: <int>
          isis_circuit_type: <str>
          isis_authentication_mode: <str>
          isis_authentication_key: <str>
          mpls_ip: <bool>
          mpls_ldp: <bool>
          mtu: <int>
          bfd: <bool>
          ptp:
            enabled: <bool>
          qos_profile: <str>
          macsec_profile: <str>
          port_channel:
            mode: <str>
            nodes_child_interfaces:
              - node: <str>
                interfaces:
                  - <str>
          raw_eos_cli: <str>
      p2p_links:
        - nodes:
            - <str>
          profile: <str>
          id: <int>
          speed: <str>
          ip_pool: <str>
          subnet: <str>
          ip:
            - <str>
          ipv6_enable: <bool>
          interfaces:
            - <str>
          as:
            - <str>
          descriptions:
            - <str>
          include_in_underlay_protocol: <bool>
          isis_hello_padding: <bool>
          isis_metric: <int>
          isis_circuit_type: <str>
          isis_authentication_mode: <str>
          isis_authentication_key: <str>
          mpls_ip: <bool>
          mpls_ldp: <bool>
          mtu: <int>
          bfd: <bool>
          ptp:
            enabled: <bool>
          qos_profile: <str>
          macsec_profile: <str>
          port_channel:
            mode: <str>
            nodes_child_interfaces:
              - node: <str>
                interfaces:
                  - <str>
          raw_eos_cli: <str>
    ```

## Custom Structured Configuration List Merge

The List-merge strategy used when merging custom structured configurations.

This applies to all vars prefixed by prefixes in `custom_structured_configuration_prefix`
and all data under the various `structured_config` options.

The available list merge strategies:
- `replace`:
  - Any list will be replaced with the list defined in custom structured configurations.
- `append`:
  - Existing list items with the same "Primary key"-value will be updated.
  - New items will be appended to the existing list (including duplicates).
- `keep`:
  - Only set list if there is no existing list or existing list is `None`.
- `prepend`:
  - Existing list items with the same "Primary key"-value will be updated.
  - New items will be prepended to the existing list (including duplicates).
- `append_rp`:
  - Existing list items with the same "Primary key"-value will be updated.
  - New unique items will be appended to the existing list.
- `prepend_rp`:
  - Existing list items with the same "Primary key"-value will be updated.
  - New unique items will be prepended to the existing list.

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>custom_structured_configuration_list_merge</samp>](## "custom_structured_configuration_list_merge") | String |  | append_rp | Valid Values:<br>- replace<br>- append<br>- keep<br>- prepend<br>- append_rp<br>- prepend_rp |  |

=== "YAML"

    ```yaml
    custom_structured_configuration_list_merge: <str>
    ```

## Custom Structured Configuration Prefix

Custom EOS Structured Configuration keys can be set on any group or host_var level using the name
of the corresponding `eos_cli_config_gen` key prefixed with content of `custom_structured_configuration_prefix`.

The content of Custom Structured Configuration variables will be merged with the structured config generated by the eos_designs role.

The merge is done recursively, so it is possible to update a sub-key of a variable set by `eos_designs` role already.

The merge follow these recursive merge strategies:
- New keys will be added for all types.
- Existing keys of type "List" with a "Primary key" set in the schema:
  - Strategy can be changed with `custom_structured_configuration_list_merge`. Default strategy:
    - Existing list items with the same "Primary key"-value will be updated.
    - New unique items will be appended to the existing list
- Other keys of type "List" will have new unique items appended the the existing list.
- Existing keys of type "Dictionary" will recursively merge
- Other existing keys will be replaced.

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>custom_structured_configuration_prefix</samp>](## "custom_structured_configuration_prefix") | List, items: String |  | ['custom_structured_configuration_'] |  |  |
    | [<samp>&nbsp;&nbsp;- &lt;str&gt;</samp>](## "custom_structured_configuration_prefix.[].&lt;str&gt;") | String |  |  |  |  |

=== "YAML"

    ```yaml
    custom_structured_configuration_prefix:
      - <str>
    ```

## CVP Ingestauth Key

On-premise CVP ingest auth key. If set, TerminAttr will be configured with key-based authentication for on-premise CVP.
If not set, TerminAttr will be configured with certificate based authentication:
- On-premise using token onboarding. Default token path is '/tmp/token'.
- CVaaS using token-secure onboarding. Default token path is '/tmp/cv-onboarding-token'.
Token must be copied to the device first.

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>cvp_ingestauth_key</samp>](## "cvp_ingestauth_key") | String |  |  |  |  |

=== "YAML"

    ```yaml
    cvp_ingestauth_key: <str>
    ```

## CVP Instance IP

IPv4 address or DNS name for CloudVision.
This variable only supports an on-premise single-node cluster or the DNS name of a CloudVision as a Service instance.

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>cvp_instance_ip</samp>](## "cvp_instance_ip") | String |  |  |  |  |

=== "YAML"

    ```yaml
    cvp_instance_ip: <str>
    ```

## CVP Instance Ips

List of IPv4 addresses or DNS names for CloudVision.
For on-premise CloudVision enter all the nodes of the cluster.
For CloudVision as a Service enter the DNS name of the instance.
`eos_designs` only supports one CloudVision cluster.

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>cvp_instance_ips</samp>](## "cvp_instance_ips") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;- &lt;str&gt;</samp>](## "cvp_instance_ips.[].&lt;str&gt;") | String |  |  |  | IPv4 address or DNS name for CloudVision |

=== "YAML"

    ```yaml
    cvp_instance_ips:
      - <str>
    ```

## CVP Token File

cvp_token_file is the path to the token file on the switch.
If not set the default locations for on-premise or CVaaS will be used.
See cvp_ingestauth_key for details.

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>cvp_token_file</samp>](## "cvp_token_file") | String |  |  |  |  |

=== "YAML"

    ```yaml
    cvp_token_file: <str>
    ```

## DC Name

DC Name, required to match Ansible Group name covering all devices in the DC.
Required for 5-stage CLOS (Super-spines).

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>dc_name</samp>](## "dc_name") | String |  |  |  |  |

=== "YAML"

    ```yaml
    dc_name: <str>
    ```

## Default IGMP Snooping Enabled

When set to false, disables IGMP snooping at fabric level and overrides per vlan settings.

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>default_igmp_snooping_enabled</samp>](## "default_igmp_snooping_enabled") | Boolean |  | True |  |  |

=== "YAML"

    ```yaml
    default_igmp_snooping_enabled: <bool>
    ```

## Default Interfaces

- Set default uplink, downlink, and MLAG interfaces, which will be used if these interfaces are not defined on a device (either directly or through inheritance).
- These are defined based on the combination of node_type (e.g., l3leaf or spine) and a regex for matching the platform.
- A list of interfaces or interface ranges can be specified.
- Each list item supports range syntax that can be expanded into a list of interfaces. Interface range examples:
  - Ethernet49-52/1: Expands to [ Ethernet49/1, Ethernet50/1, Ethernet51/1, Ethernet52/1 ]
  - Ethernet1/31-34/1: Expands to [ Ethernet1/31/1, Ethernet1/32/1, Ethernet1/33/1, Ethernet1/34/1 ]
  - Ethernet49-50,53-54: Expands to [ Ethernet49, Ethernet50, Ethernet53, Ethernet54 ]
  - Ethernet1-2/1-4: Expands to [ Ethernet1/1, Ethernet1/2, Ethernet1/3, Ethernet1/4, Ethernet2/1, Ethernet2/2, Ethernet2/3, Ethernet2/4 ]
- `uplink_interfaces` and `mlag_interfaces` under `default_interfaces` are directly inherited by `uplink_interfaces` and `mlag_interfaces`.
- `downlink_interfaces` are referenced by the child switch (e.g., the leaf in a leaf/spine network). The child switch leverages an upstream switch's `default_downlink_interfaces` using the child switch ID.  This is then used to build `uplink_switch_interfaces` for that child.
  - In the case of `max_parallel_uplinks` > 1 the `default_downlink_interfaces` are mapped with consecutive downlinks per child ID.
  - Example for `max_parallel_uplinks: 2`, downlink interfaces will be mapped as `[ <downlink1 to leaf-id1>, <downlink2 to leaf-id1>, <downlink1 to leaf-id2>, <downlink2 to leaf-id2> ...]`
- Please note that no default interfaces are defined in AVD itself. You will need to create your own based on the example below.

Example:

```yaml
default_interfaces:
  - types: [ spine, l3leaf ]
    platforms: [ "7050[SC]X3", vEOS.*, default ]
    uplink_interfaces: [ Ethernet49-54/1 ]
    mlag_interfaces: [ Ethernet55-56/1 ]
    downlink_interfaces: [ Ethernet1-32/1 ]
```

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>default_interfaces</samp>](## "default_interfaces") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;- types</samp>](## "default_interfaces.[].types") | List, items: String | Required |  |  | List of node type keys. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "default_interfaces.[].types.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;platforms</samp>](## "default_interfaces.[].platforms") | List, items: String | Required |  |  | List of platform families.<br>This is defined as a Python regular expression that matches the full platform type.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "default_interfaces.[].platforms.[].&lt;str&gt;") | String |  |  |  | Arista platform family regular expression. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;uplink_interfaces</samp>](## "default_interfaces.[].uplink_interfaces") | List, items: String |  |  |  | List of uplink interfaces or uplink interface ranges. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "default_interfaces.[].uplink_interfaces.[].&lt;str&gt;") | String |  |  |  | Interface range or interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mlag_interfaces</samp>](## "default_interfaces.[].mlag_interfaces") | List, items: String |  |  |  | List of MLAG interfaces or MLAG interface ranges. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "default_interfaces.[].mlag_interfaces.[].&lt;str&gt;") | String |  |  |  | Interface range or interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;downlink_interfaces</samp>](## "default_interfaces.[].downlink_interfaces") | List, items: String |  |  |  | List of downlink interfaces or downlink interface ranges. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "default_interfaces.[].downlink_interfaces.[].&lt;str&gt;") | String |  |  |  | Interface range or interface. |

=== "YAML"

    ```yaml
    default_interfaces:
      - types:
          - <str>
        platforms:
          - <str>
        uplink_interfaces:
          - <str>
        mlag_interfaces:
          - <str>
        downlink_interfaces:
          - <str>
    ```

## Default Node Types

Uses hostname matches against a regular expression to determine the node type.

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>default_node_types</samp>](## "default_node_types") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;- node_type</samp>](## "default_node_types.[].node_type") | String | Required, Unique |  |  | Resulting node type when regex matches. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;match_hostnames</samp>](## "default_node_types.[].match_hostnames") | List, items: String | Required |  |  | Regular expressions to match against hostnames. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "default_node_types.[].match_hostnames.[].&lt;str&gt;") | String | Required |  |  | Regex needs to match full hostname (i.e. is bounded by ^ and $ elements). |

=== "YAML"

    ```yaml
    default_node_types:
      - node_type: <str>
        match_hostnames:
          - <str>
    ```

## Design

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>design</samp>](## "design") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;type</samp>](## "design.type") | String |  | l3ls-evpn | Valid Values:<br>- l3ls-evpn<br>- mpls<br>- l2ls | By setting the design.type variable, the default node-types and templates described in these documents will be used.<br> |

=== "YAML"

    ```yaml
    design:
      type: <str>
    ```

## Enable Trunk Groups

Enable Trunk Group support across eos_designs
Warning: Because of the nature of the EOS Trunk Group feature, enabling this is "all or nothing".
*All* vlans and *all* trunks towards connected endpoints must be using trunk groups as well.
If trunk groups are not assigned to a trunk, no vlans will be enabled on that trunk.
See "Details on enable_trunk_groups" below before enabling this feature.

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>enable_trunk_groups</samp>](## "enable_trunk_groups") | Boolean |  | False |  |  |

=== "YAML"

    ```yaml
    enable_trunk_groups: <bool>
    ```

## EOS Designs Custom Templates

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>eos_designs_custom_templates</samp>](## "eos_designs_custom_templates") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;- template</samp>](## "eos_designs_custom_templates.[].template") | String | Required |  |  | Template file. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;options</samp>](## "eos_designs_custom_templates.[].options") | Dictionary |  |  |  | Template options |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;list_merge</samp>](## "eos_designs_custom_templates.[].options.list_merge") | String |  | append_rp |  | Merge strategy for lists |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;strip_empty_keys</samp>](## "eos_designs_custom_templates.[].options.strip_empty_keys") | Boolean |  | True |  | Filter out keys from the generated output if value is null/none/undefined |

=== "YAML"

    ```yaml
    eos_designs_custom_templates:
      - template: <str>
        options:
          list_merge: <str>
          strip_empty_keys: <bool>
    ```

## EOS Designs Documentation

Control fabric documentation generation.

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>eos_designs_documentation</samp>](## "eos_designs_documentation") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;connected_endpoints</samp>](## "eos_designs_documentation.connected_endpoints") | Boolean |  | False |  | Generate fabric-wide documentation for connected endpoints.<br> |

=== "YAML"

    ```yaml
    eos_designs_documentation:
      connected_endpoints: <bool>
    ```

## Event Handlers

Gives the ability to monitor and react to Syslog messages.
Event Handlers provide a powerful and flexible tool that can be used to apply self-healing actions,
customize the system behavior, and implement workarounds to problems discovered in the field.

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>event_handlers</samp>](## "event_handlers") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;- name</samp>](## "event_handlers.[].name") | String | Required, Unique |  |  | Event Handler Name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;action_type</samp>](## "event_handlers.[].action_type") | String |  |  | Valid Values:<br>- bash<br>- increment<br>- log |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "event_handlers.[].action") | String |  |  |  | Command to execute<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;delay</samp>](## "event_handlers.[].delay") | Integer |  |  |  | Event-handler delay in seconds<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;trigger</samp>](## "event_handlers.[].trigger") | String |  |  | Valid Values:<br>- on-logging<br>- on-startup-config | Configure event trigger condition.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;regex</samp>](## "event_handlers.[].regex") | String |  |  |  | Regular expression to use for searching log messages. Required for on-logging trigger<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;asynchronous</samp>](## "event_handlers.[].asynchronous") | Boolean |  | False |  | Set the action to be non-blocking. |

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

## EVPN Ebgp Gateway Inter Domain

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>evpn_ebgp_gateway_inter_domain</samp>](## "evpn_ebgp_gateway_inter_domain") | Boolean |  |  |  |  |

=== "YAML"

    ```yaml
    evpn_ebgp_gateway_inter_domain: <bool>
    ```

## EVPN Ebgp Gateway Multihop

Default of 15, considering a large value to avoid BGP reachability issues in very complex DCI networks.
Adapt the value for your specific topology.

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>evpn_ebgp_gateway_multihop</samp>](## "evpn_ebgp_gateway_multihop") | Integer |  | 15 |  |  |

=== "YAML"

    ```yaml
    evpn_ebgp_gateway_multihop: <int>
    ```

## EVPN Ebgp Multihop

Default of 3, the recommended value for a 3 stage spine and leaf topology.
Set to a higher value to allow for very large and complex topologies.

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>evpn_ebgp_multihop</samp>](## "evpn_ebgp_multihop") | Integer |  | 3 |  |  |

=== "YAML"

    ```yaml
    evpn_ebgp_multihop: <int>
    ```

## EVPN Hostflap Detection

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>evpn_hostflap_detection</samp>](## "evpn_hostflap_detection") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;enabled</samp>](## "evpn_hostflap_detection.enabled") | Boolean |  | True |  | If set to false it will disable EVPN host-flap detection |
    | [<samp>&nbsp;&nbsp;threshold</samp>](## "evpn_hostflap_detection.threshold") | Integer |  | 5 |  | Minimum number of MAC moves that indicate a MAC duplication issue |
    | [<samp>&nbsp;&nbsp;window</samp>](## "evpn_hostflap_detection.window") | Integer |  | 180 |  | Time (in seconds) to detect a MAC duplication issue |
    | [<samp>&nbsp;&nbsp;expiry_timeout</samp>](## "evpn_hostflap_detection.expiry_timeout") | Integer |  |  |  | Time (in seconds) to purge a MAC duplication issue |

=== "YAML"

    ```yaml
    evpn_hostflap_detection:
      enabled: <bool>
      threshold: <int>
      window: <int>
      expiry_timeout: <int>
    ```

## EVPN Import Pruning

Enable VPN import pruning (Min. EOS 4.24.2F)
The Route Target extended communities carried by incoming VPN paths will
be examined. If none of those Route Targets have been configured for import,
the path will be immediately discarded

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>evpn_import_pruning</samp>](## "evpn_import_pruning") | Boolean |  | False |  |  |

=== "YAML"

    ```yaml
    evpn_import_pruning: <bool>
    ```

## EVPN Multicast

General Configuration required for EVPN Multicast. "evpn_l2_multicast" must also be configured under the Network Services (tenants).
Requires "underlay_multicast: true" and IGMP snooping enabled globally (default).
For MLAG devices Route Distinguisher must be unique since this feature will create multi-vtep configuration.
Warning !!! For Trident3 based platforms i.e 7050X3, 7300X3, 720XP and 722XP
  The Following default platform setting will be configured: "platform trident forwarding-table partition flexible exact-match 16384 l2-shared 98304 l3-shared 131072"
  All forwarding agents will be restarted when this configuration is applied.
  You can tune the settings by overridding the default variable: "platform_settings[platforms].trident_forwarding_table_partition:"
  Please contact an Arista representative for help with determining the appropriate values for your environment.

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>evpn_multicast</samp>](## "evpn_multicast") | Boolean |  | False |  |  |

=== "YAML"

    ```yaml
    evpn_multicast: <bool>
    ```

## EVPN Overlay BGP Rtc

Enable Route Target Membership Constraint Address Family on EVPN overlay BGP peerings (Min. EOS 4.25.1F)
Requires use eBGP as overlay protocol.

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>evpn_overlay_bgp_rtc</samp>](## "evpn_overlay_bgp_rtc") | Boolean |  | False |  |  |

=== "YAML"

    ```yaml
    evpn_overlay_bgp_rtc: <bool>
    ```

## EVPN Prevent Readvertise To Server

Configure route-map on eBGP sessions towards route-servers, where prefixes with the peer's ASN in the AS Path are filtered away.
This is very useful in large-scale networks, where convergence will be quicker by not returning all updates received
from Route-server-1 to Router-server-2 just for Route-server-2 to throw them away because of AS Path loop detection.

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>evpn_prevent_readvertise_to_server</samp>](## "evpn_prevent_readvertise_to_server") | Boolean |  | False |  |  |

=== "YAML"

    ```yaml
    evpn_prevent_readvertise_to_server: <bool>
    ```

## EVPN Rd Type

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>evpn_rd_type</samp>](## "evpn_rd_type") <span style="color:red">removed</span> | Dictionary |  |  |  | <span style="color:red">This key was removed. Support was removed in AVD version 4.0.0. Use <samp>overlay_rd_type</samp> instead.</span> |

=== "YAML"

    ```yaml
    ```

## EVPN Rt Type

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>evpn_rt_type</samp>](## "evpn_rt_type") <span style="color:red">removed</span> | Dictionary |  |  |  | <span style="color:red">This key was removed. Support was removed in AVD version 4.0.0. Use <samp>overlay_rt_type</samp> instead.</span> |

=== "YAML"

    ```yaml
    ```

## EVPN Short Esi Prefix

Configure prefix for "short_esi" values

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>evpn_short_esi_prefix</samp>](## "evpn_short_esi_prefix") | String |  | 0000:0000: |  |  |

=== "YAML"

    ```yaml
    evpn_short_esi_prefix: <str>
    ```

## EVPN VLAN Aware Bundles

Enable vlan aware bundles for EVPN MAC-VRF

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>evpn_vlan_aware_bundles</samp>](## "evpn_vlan_aware_bundles") | Boolean |  | False |  |  |

=== "YAML"

    ```yaml
    evpn_vlan_aware_bundles: <bool>
    ```

## Fabric EVPN Encapsulation

Should be set to mpls for evpn-mpls scenario.

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>fabric_evpn_encapsulation</samp>](## "fabric_evpn_encapsulation") | String |  | vxlan | Valid Values:<br>- vxlan<br>- mpls |  |

=== "YAML"

    ```yaml
    fabric_evpn_encapsulation: <str>
    ```

## Fabric Name

Fabric Name, required to match Ansible Group name covering all devices in the Fabric, **must** be an inventory group name.

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>fabric_name</samp>](## "fabric_name") | String | Required |  |  |  |

=== "YAML"

    ```yaml
    fabric_name: <str>
    ```

## Hardware Counters

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>hardware_counters</samp>](## "hardware_counters") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;features</samp>](## "hardware_counters.features") | List, items: Dictionary |  |  |  | This data model allows to configure the list of hardware counters feature<br>available on Arista platforms.<br><br>The `name` key accepts a list of valid_values which MUST be updated to support<br>new feature as they are released in EOS.<br><br>The available values of the different keys like 'direction' or 'address_type'<br>are feature and hardware dependent and this model DOES NOT validate that the<br>combinations are valid. It is the responsability of the user of this data model<br>to make sure that the rendered CLI is accepted by the targeted device.<br><br>Examples:<br><br>  * Use:<br>    ```yaml<br>    hardware_counters:<br>      features:<br>        - name: ip<br>          direction: out<br>          layer3: true<br>          units_packets: true<br>    ```<br><br>    to render:<br>    ```eos<br>    hardware counter feature ip out layer3 units packets<br>    ```<br>  * Use:<br>    ```yaml<br>    hardware_counters:<br>      features:<br>        - name: route<br>          address_type: ipv4<br>          vrf: test<br>          prefix: 192.168.0.0/24<br>    ```<br><br>    to render:<br>    ```eos<br>    hardware counter feature route ipv4 vrf test 192.168.0.0/24<br>    ```<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "hardware_counters.features.[].name") | String |  |  | Valid Values:<br>- acl<br>- decap-group<br>- directflow<br>- ecn<br>- flow-spec<br>- gre tunnel interface<br>- ip<br>- mpls interface<br>- mpls lfib<br>- mpls tunnel<br>- multicast<br>- nexthop<br>- pbr<br>- pdp<br>- policing interface<br>- qos<br>- qos dual-rate-policer<br>- route<br>- routed-port<br>- subinterface<br>- tapagg<br>- traffic-class<br>- traffic-policy<br>- vlan<br>- vlan-interface<br>- vni decap<br>- vni encap<br>- vtep decap<br>- vtep encap |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction</samp>](## "hardware_counters.features.[].direction") | String |  |  | Valid Values:<br>- in<br>- out<br>- cpu | Most features support only 'in' and 'out'. Some like traffic-policy support 'cpu'.<br>Some features DO NOT have any direction.<br>This validation IS NOT made by the schemas.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;address_type</samp>](## "hardware_counters.features.[].address_type") | String |  |  | Valid Values:<br>- ipv4<br>- ipv6<br>- mac | Supported only for the following features:<br>- acl: [ipv4, ipv6, mac] if direction is 'out'<br>- multicast: [ipv4, ipv6]<br>- route: [ipv4, ipv6]<br>This validation IS NOT made by the schemas.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;layer3</samp>](## "hardware_counters.features.[].layer3") | Boolean |  |  |  | Supported only for the 'ip' feature<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "hardware_counters.features.[].vrf") | String |  |  |  | Supported only for the 'route' feature.<br>This validation IS NOT made by the schemas.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefix</samp>](## "hardware_counters.features.[].prefix") | String |  |  |  | Supported only for the 'route' feature.<br>Mandatory for the 'route' feature.<br>This validation IS NOT made by the schemas.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;units_packets</samp>](## "hardware_counters.features.[].units_packets") | Boolean |  |  |  |  |

=== "YAML"

    ```yaml
    hardware_counters:
      features:
        - name: <str>
          direction: <str>
          address_type: <str>
          layer3: <bool>
          vrf: <str>
          prefix: <str>
          units_packets: <bool>
    ```

## Internal VLAN Order

Internal vlan allocation order and range.

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>internal_vlan_order</samp>](## "internal_vlan_order") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;allocation</samp>](## "internal_vlan_order.allocation") | String | Required | ascending | Valid Values:<br>- ascending<br>- descending |  |
    | [<samp>&nbsp;&nbsp;range</samp>](## "internal_vlan_order.range") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;beginning</samp>](## "internal_vlan_order.range.beginning") | Integer | Required | 1006 | Min: 2<br>Max: 4094 | First VLAN ID. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ending</samp>](## "internal_vlan_order.range.ending") | Integer | Required | 1199 | Min: 2<br>Max: 4094 | Last VLAN ID. |

=== "YAML"

    ```yaml
    internal_vlan_order:
      allocation: <str>
      range:
        beginning: <int>
        ending: <int>
    ```

## IPv6 Management Destination Networks

List of IPv6 prefixes to configure as static routes towards the OOB IPv6 Management interface gateway.
Replaces the default route.

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>ipv6_mgmt_destination_networks</samp>](## "ipv6_mgmt_destination_networks") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;- &lt;str&gt;</samp>](## "ipv6_mgmt_destination_networks.[].&lt;str&gt;") | String |  |  |  | IPv6_network/Mask |

=== "YAML"

    ```yaml
    ipv6_mgmt_destination_networks:
      - <str>
    ```

## IPv6 Management Gateway

OOB Management interface gateway in IPv6 format.
Used as next-hop for default gateway or static routes defined under 'ipv6_mgmt_destination_networks'

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>ipv6_mgmt_gateway</samp>](## "ipv6_mgmt_gateway") | String |  |  | Format: ipv6 |  |

=== "YAML"

    ```yaml
    ipv6_mgmt_gateway: <str>
    ```

## IS Deployed

Is device already deployed in the fabric
When set to false, interfaces toward this device may be shutdown depending on the `shutdown_interfaces_towards_undeployed_peers` setting.
Furthermore `eos_config_deploy_cvp` will not attempt to move or apply configurations to the device.

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>is_deployed</samp>](## "is_deployed") | Boolean |  | True |  |  |

=== "YAML"

    ```yaml
    is_deployed: <bool>
    ```

## ISIS Advertise Passive Only

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>isis_advertise_passive_only</samp>](## "isis_advertise_passive_only") | Boolean |  | False |  |  |

=== "YAML"

    ```yaml
    isis_advertise_passive_only: <bool>
    ```

## ISIS Area ID

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>isis_area_id</samp>](## "isis_area_id") | String |  | 49.0001 |  |  |

=== "YAML"

    ```yaml
    isis_area_id: <str>
    ```

## ISIS Default Circuit Type

These fabric level parameters can be used with core_interfaces running ISIS, and may be overridden on link profile or link level.

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>isis_default_circuit_type</samp>](## "isis_default_circuit_type") | String |  | level-2 | Valid Values:<br>- level-1-2<br>- level-1<br>- level-2 |  |

=== "YAML"

    ```yaml
    isis_default_circuit_type: <str>
    ```

## ISIS Default IS Type

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>isis_default_is_type</samp>](## "isis_default_is_type") | String |  | level-2 | Valid Values:<br>- level-1-2<br>- level-1<br>- level-2 |  |

=== "YAML"

    ```yaml
    isis_default_is_type: <str>
    ```

## ISIS Default Metric

These fabric level parameters can be used with core_interfaces running ISIS, and may be overridden at link profile or link level.

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>isis_default_metric</samp>](## "isis_default_metric") | Integer |  | 50 |  |  |

=== "YAML"

    ```yaml
    isis_default_metric: <int>
    ```

## ISIS Maximum Paths

Number of path to configure in ECMP for ISIS.

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>isis_maximum_paths</samp>](## "isis_maximum_paths") | Integer |  |  |  |  |

=== "YAML"

    ```yaml
    isis_maximum_paths: <int>
    ```

## ISIS TI LFA

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>isis_ti_lfa</samp>](## "isis_ti_lfa") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;enabled</samp>](## "isis_ti_lfa.enabled") | Boolean |  | False |  |  |
    | [<samp>&nbsp;&nbsp;protection</samp>](## "isis_ti_lfa.protection") | String |  |  | Valid Values:<br>- link<br>- node |  |
    | [<samp>&nbsp;&nbsp;local_convergence_delay</samp>](## "isis_ti_lfa.local_convergence_delay") | Integer |  | 10000 |  | Local convergence delay in milliseconds |

=== "YAML"

    ```yaml
    isis_ti_lfa:
      enabled: <bool>
      protection: <str>
      local_convergence_delay: <int>
    ```

## L3 Edge

The `l3_edge` data model can be used to configure extra L3 P2P links anywhere in the fabric.
It can be between two switches that are already part of the fabric inventory, or it can be towards another device, where only one end of the link is on a switch in the fabric.
Fabric switches can be types `l3leaf`, `spine` or `super-spine`.

The data model supports using IP pools, Subnet per link or specifying the IP addresses manually.
For BGP peerings the AS number must be specified.
If the AS number is different than the AS number configured for the node, the local-as will be replaced on this BGP peering (`neighbor <ip> local-as <as> no-prepend replace-as`).

Make sure to configure the variables in a group_vars file covering all devices mentioned in the data model.

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>l3_edge</samp>](## "l3_edge") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;p2p_links_ip_pools</samp>](## "l3_edge.p2p_links_ip_pools") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "l3_edge.p2p_links_ip_pools.[].name") | String | Required, Unique |  |  | P2P pool name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4_pool</samp>](## "l3_edge.p2p_links_ip_pools.[].ipv4_pool") | String |  |  |  | IPv4 address/Mask. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefix_size</samp>](## "l3_edge.p2p_links_ip_pools.[].prefix_size") | Integer |  | 31 | Min: 8<br>Max: 31 | Subnet mask size. |
    | [<samp>&nbsp;&nbsp;p2p_links_profiles</samp>](## "l3_edge.p2p_links_profiles") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "l3_edge.p2p_links_profiles.[].name") | String | Required, Unique |  |  | P2P profile name. Any variable supported under p2p_links can be inherited from a profile. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;id</samp>](## "l3_edge.p2p_links_profiles.[].id") | Integer |  |  |  | Unique id per subnet_summary. Used to calculate ip addresses.<br>Required with ip_pool. ID starting from 1.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;speed</samp>](## "l3_edge.p2p_links_profiles.[].speed") | String |  |  |  | The values can be speed or auto speed or forced speed. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_pool</samp>](## "l3_edge.p2p_links_profiles.[].ip_pool") | String |  |  |  | P2P pool name. IP Pool defined under p2p_links_ip_pools. A /31 will be taken from the pool per P2P link |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;subnet</samp>](## "l3_edge.p2p_links_profiles.[].subnet") | String |  |  |  | IPv4 address/Mask. Subnet used on this P2P link. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip</samp>](## "l3_edge.p2p_links_profiles.[].ip") | List, items: String |  |  |  | Specific IP addresses used on this P2P link. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "l3_edge.p2p_links_profiles.[].ip.[].&lt;str&gt;") | String |  |  |  | Node IPv4 address/Mask. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_enable</samp>](## "l3_edge.p2p_links_profiles.[].ipv6_enable") | Boolean |  | False |  | Allows turning on ipv6 for the link or profile (also autodetected based on underlay_rfc5549 and include_in_underlay_protocol). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "l3_edge.p2p_links_profiles.[].nodes") | List, items: String |  |  |  | Nodes where this link should be configured. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "l3_edge.p2p_links_profiles.[].nodes.[].&lt;str&gt;") | String |  |  |  | The values can be < node_a >, < node_b >.<br>ex.- [ core-1-isis-sr-ldp, core-2-ospf-ldp ].<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interfaces</samp>](## "l3_edge.p2p_links_profiles.[].interfaces") | List, items: String |  |  |  | Interfaces where this link should be configured and Required unless using port-channels. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "l3_edge.p2p_links_profiles.[].interfaces.[].&lt;str&gt;") | String |  |  |  | The value can be like < node_a_interface >, < node_b_interface >.<br>ex. - [ Ethernet2, Ethernet2 ].<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;as</samp>](## "l3_edge.p2p_links_profiles.[].as") | List, items: String |  |  |  | AS numbers for BGP.<br>Required with bgp peering.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "l3_edge.p2p_links_profiles.[].as.[].&lt;str&gt;") | String |  |  |  | The values can be like ["node_a_as", "node_b_as"]. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;descriptions</samp>](## "l3_edge.p2p_links_profiles.[].descriptions") | List, items: String |  |  |  | Interface description. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "l3_edge.p2p_links_profiles.[].descriptions.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_in_underlay_protocol</samp>](## "l3_edge.p2p_links_profiles.[].include_in_underlay_protocol") | Boolean |  | True |  | Add this interface to underlay routing protocol. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_hello_padding</samp>](## "l3_edge.p2p_links_profiles.[].isis_hello_padding") | Boolean |  | False |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_metric</samp>](## "l3_edge.p2p_links_profiles.[].isis_metric") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_circuit_type</samp>](## "l3_edge.p2p_links_profiles.[].isis_circuit_type") | String |  |  | Valid Values:<br>- level-1<br>- level-2<br>- level-1-2 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_authentication_mode</samp>](## "l3_edge.p2p_links_profiles.[].isis_authentication_mode") | String |  |  | Valid Values:<br>- md5<br>- text |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_authentication_key</samp>](## "l3_edge.p2p_links_profiles.[].isis_authentication_key") | String |  |  |  | Type-7 encrypted password. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mpls_ip</samp>](## "l3_edge.p2p_links_profiles.[].mpls_ip") | Boolean |  |  |  | MPLS parameters. Default value is true if switch.mpls_lsr is true. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mpls_ldp</samp>](## "l3_edge.p2p_links_profiles.[].mpls_ldp") | Boolean |  |  |  | MPLS parameters. Default value is true for ldp underlay variants, otherwise false. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mtu</samp>](## "l3_edge.p2p_links_profiles.[].mtu") | Integer |  |  |  | MTU for this P2P link. Default value same as p2p_uplinks_mtu. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bfd</samp>](## "l3_edge.p2p_links_profiles.[].bfd") | Boolean |  | False |  | Enable BFD (only considered for BGP). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ptp</samp>](## "l3_edge.p2p_links_profiles.[].ptp") | Dictionary |  |  |  | PTP parameters. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "l3_edge.p2p_links_profiles.[].ptp.enabled") | Boolean |  | False |  | Enable PTP |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;qos_profile</samp>](## "l3_edge.p2p_links_profiles.[].qos_profile") | String |  |  |  | QOS service profile. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;macsec_profile</samp>](## "l3_edge.p2p_links_profiles.[].macsec_profile") | String |  |  |  | MAC security profile. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;port_channel</samp>](## "l3_edge.p2p_links_profiles.[].port_channel") | Dictionary |  |  |  | Port-channel parameters. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "l3_edge.p2p_links_profiles.[].port_channel.mode") | String |  | active |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes_child_interfaces</samp>](## "l3_edge.p2p_links_profiles.[].port_channel.nodes_child_interfaces") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- node</samp>](## "l3_edge.p2p_links_profiles.[].port_channel.nodes_child_interfaces.[].node") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interfaces</samp>](## "l3_edge.p2p_links_profiles.[].port_channel.nodes_child_interfaces.[].interfaces") | List, items: String |  |  |  | List of node interfaces. Ex.- [ 'node1 interface1', 'node1 interface2' ]. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "l3_edge.p2p_links_profiles.[].port_channel.nodes_child_interfaces.[].interfaces.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "l3_edge.p2p_links_profiles.[].raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the point-to-point interface in the final EOS configuration. |
    | [<samp>&nbsp;&nbsp;p2p_links</samp>](## "l3_edge.p2p_links") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- nodes</samp>](## "l3_edge.p2p_links.[].nodes") | List, items: String | Required |  |  | Nodes where this link should be configured. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "l3_edge.p2p_links.[].nodes.[].&lt;str&gt;") | String |  |  |  | The values can be < node_a >, < node_b >.<br>ex.- [ core-1-isis-sr-ldp, core-2-ospf-ldp ].<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;profile</samp>](## "l3_edge.p2p_links.[].profile") | String |  |  |  | P2P profile name. Profile defined under p2p_profiles. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;id</samp>](## "l3_edge.p2p_links.[].id") | Integer |  |  |  | Unique id per subnet_summary. Used to calculate ip addresses.<br>Required with ip_pool. ID starting from 1.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;speed</samp>](## "l3_edge.p2p_links.[].speed") | String |  |  |  | The values can be speed or auto speed or forced speed. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_pool</samp>](## "l3_edge.p2p_links.[].ip_pool") | String |  |  |  | P2P pool name. IP Pool defined under p2p_links_ip_pools. A /31 will be taken from the pool per P2P link |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;subnet</samp>](## "l3_edge.p2p_links.[].subnet") | String |  |  |  | IPv4 address/Mask. Subnet used on this P2P link. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip</samp>](## "l3_edge.p2p_links.[].ip") | List, items: String |  |  |  | Specific IP addresses used on this P2P link. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "l3_edge.p2p_links.[].ip.[].&lt;str&gt;") | String |  |  |  | Node IPv4 address/Mask. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_enable</samp>](## "l3_edge.p2p_links.[].ipv6_enable") | Boolean |  | False |  | Allows turning on ipv6 for the link or profile (also autodetected based on underlay_rfc5549 and include_in_underlay_protocol). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interfaces</samp>](## "l3_edge.p2p_links.[].interfaces") | List, items: String |  |  |  | Interfaces where this link should be configured and Required unless using port-channels. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "l3_edge.p2p_links.[].interfaces.[].&lt;str&gt;") | String |  |  |  | The value can be like < node_a_interface >, < node_b_interface >.<br>ex. - [ Ethernet2, Ethernet2 ].<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;as</samp>](## "l3_edge.p2p_links.[].as") | List, items: String |  |  |  | AS numbers for BGP.<br>Required with bgp peering.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "l3_edge.p2p_links.[].as.[].&lt;str&gt;") | String |  |  |  | The values can be like ["node_a_as", "node_b_as"]. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;descriptions</samp>](## "l3_edge.p2p_links.[].descriptions") | List, items: String |  |  |  | Interface description. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "l3_edge.p2p_links.[].descriptions.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_in_underlay_protocol</samp>](## "l3_edge.p2p_links.[].include_in_underlay_protocol") | Boolean |  | True |  | Add this interface to underlay routing protocol. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_hello_padding</samp>](## "l3_edge.p2p_links.[].isis_hello_padding") | Boolean |  | False |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_metric</samp>](## "l3_edge.p2p_links.[].isis_metric") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_circuit_type</samp>](## "l3_edge.p2p_links.[].isis_circuit_type") | String |  |  | Valid Values:<br>- level-1<br>- level-2<br>- level-1-2 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_authentication_mode</samp>](## "l3_edge.p2p_links.[].isis_authentication_mode") | String |  |  | Valid Values:<br>- md5<br>- text |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_authentication_key</samp>](## "l3_edge.p2p_links.[].isis_authentication_key") | String |  |  |  | Type-7 encrypted password. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mpls_ip</samp>](## "l3_edge.p2p_links.[].mpls_ip") | Boolean |  |  |  | MPLS parameters. Default value is true if switch.mpls_lsr is true. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mpls_ldp</samp>](## "l3_edge.p2p_links.[].mpls_ldp") | Boolean |  |  |  | MPLS parameters. Default value is true for ldp underlay variants, otherwise false. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mtu</samp>](## "l3_edge.p2p_links.[].mtu") | Integer |  |  |  | MTU for this P2P link. Default value same as p2p_uplinks_mtu. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bfd</samp>](## "l3_edge.p2p_links.[].bfd") | Boolean |  | False |  | Enable BFD (only considered for BGP). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ptp</samp>](## "l3_edge.p2p_links.[].ptp") | Dictionary |  |  |  | PTP parameters. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "l3_edge.p2p_links.[].ptp.enabled") | Boolean |  | False |  | Enable PTP |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;qos_profile</samp>](## "l3_edge.p2p_links.[].qos_profile") | String |  |  |  | QOS service profile. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;macsec_profile</samp>](## "l3_edge.p2p_links.[].macsec_profile") | String |  |  |  | MAC security profile. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;port_channel</samp>](## "l3_edge.p2p_links.[].port_channel") | Dictionary |  |  |  | Port-channel parameters. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "l3_edge.p2p_links.[].port_channel.mode") | String |  | active |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes_child_interfaces</samp>](## "l3_edge.p2p_links.[].port_channel.nodes_child_interfaces") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- node</samp>](## "l3_edge.p2p_links.[].port_channel.nodes_child_interfaces.[].node") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interfaces</samp>](## "l3_edge.p2p_links.[].port_channel.nodes_child_interfaces.[].interfaces") | List, items: String |  |  |  | List of node interfaces. Ex.- [ 'node1 interface1', 'node1 interface2' ]. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "l3_edge.p2p_links.[].port_channel.nodes_child_interfaces.[].interfaces.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "l3_edge.p2p_links.[].raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the point-to-point interface in the final EOS configuration. |

=== "YAML"

    ```yaml
    l3_edge:
      p2p_links_ip_pools:
        - name: <str>
          ipv4_pool: <str>
          prefix_size: <int>
      p2p_links_profiles:
        - name: <str>
          id: <int>
          speed: <str>
          ip_pool: <str>
          subnet: <str>
          ip:
            - <str>
          ipv6_enable: <bool>
          nodes:
            - <str>
          interfaces:
            - <str>
          as:
            - <str>
          descriptions:
            - <str>
          include_in_underlay_protocol: <bool>
          isis_hello_padding: <bool>
          isis_metric: <int>
          isis_circuit_type: <str>
          isis_authentication_mode: <str>
          isis_authentication_key: <str>
          mpls_ip: <bool>
          mpls_ldp: <bool>
          mtu: <int>
          bfd: <bool>
          ptp:
            enabled: <bool>
          qos_profile: <str>
          macsec_profile: <str>
          port_channel:
            mode: <str>
            nodes_child_interfaces:
              - node: <str>
                interfaces:
                  - <str>
          raw_eos_cli: <str>
      p2p_links:
        - nodes:
            - <str>
          profile: <str>
          id: <int>
          speed: <str>
          ip_pool: <str>
          subnet: <str>
          ip:
            - <str>
          ipv6_enable: <bool>
          interfaces:
            - <str>
          as:
            - <str>
          descriptions:
            - <str>
          include_in_underlay_protocol: <bool>
          isis_hello_padding: <bool>
          isis_metric: <int>
          isis_circuit_type: <str>
          isis_authentication_mode: <str>
          isis_authentication_key: <str>
          mpls_ip: <bool>
          mpls_ldp: <bool>
          mtu: <int>
          bfd: <bool>
          ptp:
            enabled: <bool>
          qos_profile: <str>
          macsec_profile: <str>
          port_channel:
            mode: <str>
            nodes_child_interfaces:
              - node: <str>
                interfaces:
                  - <str>
          raw_eos_cli: <str>
    ```

## Local Users

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>local_users</samp>](## "local_users") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;- name</samp>](## "local_users.[].name") | String | Required, Unique |  |  | Username |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;disabled</samp>](## "local_users.[].disabled") | Boolean |  |  |  | If true, the user will be removed and all other settings are ignored.<br>Useful for removing the default "admin" user.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;privilege</samp>](## "local_users.[].privilege") | Integer |  |  | Min: 0<br>Max: 15 | Initial privilege level with local EXEC authorization.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;role</samp>](## "local_users.[].role") | String |  |  |  | EOS RBAC Role to be assigned to the user such as "network-admin" or "network-operator"<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;sha512_password</samp>](## "local_users.[].sha512_password") | String |  |  |  | SHA512 Hash of Password<br>Must be the hash of the password. By default EOS salts the password with the username, so the simplest is to generate the hash on an EOS device using the same username.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;no_password</samp>](## "local_users.[].no_password") | Boolean |  |  |  | If set a password will not be configured for this user. "sha512_password" MUST not be defined for this user.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ssh_key</samp>](## "local_users.[].ssh_key") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;shell</samp>](## "local_users.[].shell") | String |  |  | Valid Values:<br>- /bin/bash<br>- /bin/sh<br>- /sbin/nologin | Specify shell for the user<br> |

=== "YAML"

    ```yaml
    local_users:
      - name: <str>
        disabled: <bool>
        privilege: <int>
        role: <str>
        sha512_password: <str>
        no_password: <bool>
        ssh_key: <str>
        shell: <str>
    ```

## MAC Address Table

MAC address-table aging time
Use to change the EOS default of 300.

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>mac_address_table</samp>](## "mac_address_table") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;aging_time</samp>](## "mac_address_table.aging_time") | Integer |  |  | Min: 0<br>Max: 1000000 | Aging time in seconds 10-1000000.<br>Enter 0 to disable aging.<br> |

=== "YAML"

    ```yaml
    mac_address_table:
      aging_time: <int>
    ```

## Management Destination Networks

List of IPv4 prefixes to configure as static routes towards the OOB Management interface gateway.
Replaces the default route.

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>mgmt_destination_networks</samp>](## "mgmt_destination_networks") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;- &lt;str&gt;</samp>](## "mgmt_destination_networks.[].&lt;str&gt;") | String |  |  |  | IPv4_address/Mask |

=== "YAML"

    ```yaml
    mgmt_destination_networks:
      - <str>
    ```

## Management Eapi

Default is HTTPS management eAPI enabled.
The VRF is set to < mgmt_interface_vrf >.

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>management_eapi</samp>](## "management_eapi") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;enable_http</samp>](## "management_eapi.enable_http") | Boolean |  | False |  |  |
    | [<samp>&nbsp;&nbsp;enable_https</samp>](## "management_eapi.enable_https") | Boolean |  | True |  |  |
    | [<samp>&nbsp;&nbsp;default_services</samp>](## "management_eapi.default_services") | Boolean |  |  |  |  |

=== "YAML"

    ```yaml
    management_eapi:
      enable_http: <bool>
      enable_https: <bool>
      default_services: <bool>
    ```

## Management Gateway

OOB Management interface gateway in IPv4 format.
Used as next-hop for default gateway or static routes defined under 'mgmt_destination_networks'

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>mgmt_gateway</samp>](## "mgmt_gateway") | String |  |  |  |  |

=== "YAML"

    ```yaml
    mgmt_gateway: <str>
    ```

## Management Interface Description

Management interface description

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>mgmt_interface_description</samp>](## "mgmt_interface_description") | String |  | oob_management |  |  |

=== "YAML"

    ```yaml
    mgmt_interface_description: <str>
    ```

## Management Interface VRF

OOB Management VRF.

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>mgmt_interface_vrf</samp>](## "mgmt_interface_vrf") | String |  | MGMT |  |  |

=== "YAML"

    ```yaml
    mgmt_interface_vrf: <str>
    ```

## Management Interface

OOB Management interface.

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>mgmt_interface</samp>](## "mgmt_interface") | String |  | Management1 |  |  |

=== "YAML"

    ```yaml
    mgmt_interface: <str>
    ```

## Management VRF Routing

Configure IP routing for the OOB Management VRF.

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>mgmt_vrf_routing</samp>](## "mgmt_vrf_routing") | Boolean |  | False |  |  |

=== "YAML"

    ```yaml
    mgmt_vrf_routing: <bool>
    ```

## MLAG Ibgp Peering VRFs

On mlag leafs, an SVI interface is defined per vrf, to establish iBGP peering (required when there are MLAG leafs in topology)
The SVI id will be derived from the base vlan defined: mlag_ibgp_peering_vrfs.base_vlan + (vrf_id or vrf_vni) - 1
Depending on the values of vrf_id / vrf_vni it may be required to adjust the base_vlan to avoid overlaps or invalid vlan ids.
The SVI ip address derived from mlag_l3_peer_ipv4_pool is re-used across all iBGP peerings.

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>mlag_ibgp_peering_vrfs</samp>](## "mlag_ibgp_peering_vrfs") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;base_vlan</samp>](## "mlag_ibgp_peering_vrfs.base_vlan") | Integer |  | 3000 | Min: 1<br>Max: 4093 |  |

=== "YAML"

    ```yaml
    mlag_ibgp_peering_vrfs:
      base_vlan: <int>
    ```

## Name Servers

List of DNS servers. The VRF is set to < mgmt_interface_vrf >.

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>name_servers</samp>](## "name_servers") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;- &lt;str&gt;</samp>](## "name_servers.[].&lt;str&gt;") | String |  |  |  | IPv4 address |

=== "YAML"

    ```yaml
    name_servers:
      - <str>
    ```

## Network Ports

All switch_ports ranges are expanded into individual port configurations.

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>network_ports</samp>](## "network_ports") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;- switches</samp>](## "network_ports.[].switches") | List, items: String |  |  |  | Regex matching the full hostname of one or more switches.<br>The regular expression must match the full hostname.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "network_ports.[].switches.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;switch_ports</samp>](## "network_ports.[].switch_ports") | List, items: String |  |  |  | List of ranges using AVD range_expand syntax.<br>For example:<br><br>switch_ports:<br>  - Ethernet1<br>  - Ethernet2-48<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "network_ports.[].switch_ports.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "network_ports.[].description") | String |  |  |  | Description to be used on all ports. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;endpoint_ports</samp>](## "network_ports.[].endpoint_ports") | List, items: String |  |  |  | Endpoint ports is used for description, required unless description is set.<br>The lists `endpoint_ports`, `switch_ports`, and `switches` must have the same length.<br>Each list item is one switchport.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "network_ports.[].endpoint_ports.[].&lt;str&gt;") | String |  |  |  | Interface name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;speed</samp>](## "network_ports.[].speed") | String |  |  |  | Set adapter speed: `< interface_speed >`, `forced < interface_speed >`, `auto < interface_speed >`.<br>If not specified will be auto.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;profile</samp>](## "network_ports.[].profile") | String |  |  |  | Port-profile name to inherit configuration. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "network_ports.[].enabled") | Boolean |  | True |  | Administrative state, setting to false will set the port to 'shutdown' in the intended configuration.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "network_ports.[].mode") | String |  |  | Valid Values:<br>- access<br>- dot1q-tunnel<br>- trunk<br>- trunk phone | Interface mode. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mtu</samp>](## "network_ports.[].mtu") | Integer |  |  | Min: 68<br>Max: 65535 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;l2_mtu</samp>](## "network_ports.[].l2_mtu") | Integer |  |  | Min: 68<br>Max: 9416 | This should only be defined for platforms supporting the "l2 mtu" CLI command. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;native_vlan</samp>](## "network_ports.[].native_vlan") | Integer |  |  | Min: 1<br>Max: 4094 | Native VLAN for a trunk port.<br>If both `native_vlan` and `native_vlan_tag`, `native_vlan_tag` takes precedence.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;native_vlan_tag</samp>](## "network_ports.[].native_vlan_tag") | Boolean |  | False |  | If both `native_vlan` and `native_vlan_tag`, `native_vlan_tag` takes precedence. |
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
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "network_ports.[].ptp.enabled") | Boolean |  | False |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;endpoint_role</samp>](## "network_ports.[].ptp.endpoint_role") | String |  | follower | Valid Values:<br>- bmca<br>- default<br>- follower |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;profile</samp>](## "network_ports.[].ptp.profile") | String |  | aes67-r16-2016 | Valid Values:<br>- aes67<br>- aes67-r16-2016<br>- smpte2059-2 |  |
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
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;storm_control</samp>](## "network_ports.[].storm_control") | Dictionary |  |  |  | Storm control settings applied on port toward the endpoint. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;all</samp>](## "network_ports.[].storm_control.all") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;level</samp>](## "network_ports.[].storm_control.all.level") | Integer |  |  |  | Configure maximum storm-control level. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unit</samp>](## "network_ports.[].storm_control.all.unit") | String |  | percent | Valid Values:<br>- percent<br>- pps | Optional variable and is hardware dependent. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;broadcast</samp>](## "network_ports.[].storm_control.broadcast") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;level</samp>](## "network_ports.[].storm_control.broadcast.level") | Integer |  |  |  | Configure maximum storm-control level. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unit</samp>](## "network_ports.[].storm_control.broadcast.unit") | String |  | percent | Valid Values:<br>- percent<br>- pps | Optional variable and is hardware dependent. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;multicast</samp>](## "network_ports.[].storm_control.multicast") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;level</samp>](## "network_ports.[].storm_control.multicast.level") | Integer |  |  |  | Configure maximum storm-control level. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unit</samp>](## "network_ports.[].storm_control.multicast.unit") | String |  | percent | Valid Values:<br>- percent<br>- pps | Optional variable and is hardware dependent. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unknown_unicast</samp>](## "network_ports.[].storm_control.unknown_unicast") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;level</samp>](## "network_ports.[].storm_control.unknown_unicast.level") | Integer |  |  |  | Configure maximum storm-control level. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unit</samp>](## "network_ports.[].storm_control.unknown_unicast.unit") | String |  | percent | Valid Values:<br>- percent<br>- pps | Optional variable and is hardware dependent. |
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
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "network_ports.[].port_channel.enabled") | Boolean |  | True |  | Port-Channel administrative state.<br>Setting to false will set port to 'shutdown' in intended configuration.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;esi</samp>](## "network_ports.[].port_channel.esi") <span style="color:red">removed</span> | String |  |  |  | Format xxxx:xxxx:xxxx.<span style="color:red">This key was removed. Support was removed in AVD version 4.0.0. Use <samp>short_esi</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;short_esi</samp>](## "network_ports.[].port_channel.short_esi") | String |  |  |  | In format xxxx:xxxx:xxxx or "auto". |
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
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "network_ports.[].port_channel.structured_config") | Dictionary |  |  |  | Custom structured config added under port_channel_interfaces.<interface> for eos_cli_config_gen. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "network_ports.[].raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the ethernet interface in the final EOS configuration. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "network_ports.[].structured_config") | Dictionary |  |  |  | Custom structured config added under ethernet_interfaces.<interface> for eos_cli_config_gen. |

=== "YAML"

    ```yaml
    network_ports:
      - switches:
          - <str>
        switch_ports:
          - <str>
        description: <str>
        endpoint_ports:
          - <str>
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

## Network Services Keys

Define network services keys, to define grouping of network services.
This provides the ability to define various keys of your choice to better organize/group your data.
This should be defined in top level group_var for the fabric.

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>network_services_keys</samp>](## "network_services_keys") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;- name</samp>](## "network_services_keys.[].name") | String | Required, Unique |  |  |  |

=== "YAML"

    ```yaml
    network_services_keys:
      - name: <str>
    ```

## Node Type Keys

Define Node Type Keys, to specify the properties of each node type in the fabric.
This allows for complete customization of the fabric layout.
This should be defined in top level group_var for the fabric.

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>node_type_keys</samp>](## "node_type_keys") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;- key</samp>](## "node_type_keys.[].key") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "node_type_keys.[].type") | String |  |  |  | Type value matching this node_type_key. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;connected_endpoints</samp>](## "node_type_keys.[].connected_endpoints") | Boolean |  | False |  | Are endpoints connected to this node type. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;default_evpn_role</samp>](## "node_type_keys.[].default_evpn_role") | String |  | none | Valid Values:<br>- none<br>- client<br>- server | Default evpn_role. Can be overridden in topology vars. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;default_ptp_priority1</samp>](## "node_type_keys.[].default_ptp_priority1") | Integer |  | 127 | Min: 0<br>Max: 255 | Default PTP priority 1 |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;default_underlay_routing_protocol</samp>](## "node_type_keys.[].default_underlay_routing_protocol") | String |  | ebgp | Value is converted to lower case<br>Valid Values:<br>- ebgp<br>- ibgp<br>- ospf<br>- ospf-ldp<br>- isis<br>- isis-sr<br>- isis-ldp<br>- isis-sr-ldp<br>- none | Set the default underlay routing_protocol.<br>Can be overridden by setting "underlay_routing_protocol" host/group_vars.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;default_overlay_routing_protocol</samp>](## "node_type_keys.[].default_overlay_routing_protocol") | String |  | ebgp | Value is converted to lower case<br>Valid Values:<br>- ebgp<br>- ibgp<br>- her<br>- cvx<br>- none | Set the default overlay routing_protocol.<br>Can be overridden by setting "overlay_routing_protocol" host/group_vars.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;default_mpls_overlay_role</samp>](## "node_type_keys.[].default_mpls_overlay_role") | String |  |  | Valid Values:<br>- client<br>- server<br>- none | Set the default mpls overlay role.<br>Acting role in overlay control plane.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;default_overlay_address_families</samp>](## "node_type_keys.[].default_overlay_address_families") | List, items: String |  |  |  | Set the default overlay address families.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "node_type_keys.[].default_overlay_address_families.[].&lt;str&gt;") | String |  |  | Value is converted to lower case<br>Valid Values:<br>- evpn<br>- vpn-ipv4<br>- vpn-ipv6 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;default_evpn_encapsulation</samp>](## "node_type_keys.[].default_evpn_encapsulation") | String |  |  | Value is converted to lower case<br>Valid Values:<br>- mpls<br>- vxlan | Set the default evpn encapsulation.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mlag_support</samp>](## "node_type_keys.[].mlag_support") | Boolean |  | False |  | Can this node type support mlag. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;network_services</samp>](## "node_type_keys.[].network_services") | Dictionary |  |  |  | Will network services be deployed on this node type. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;l1</samp>](## "node_type_keys.[].network_services.l1") | Boolean |  | False |  | ?? |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;l2</samp>](## "node_type_keys.[].network_services.l2") | Boolean |  | False |  | Vlans |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;l3</samp>](## "node_type_keys.[].network_services.l3") | Boolean |  | False |  | VRFs, SVIs (if l2 is true).<br>Only supported with underlay_router.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;underlay_router</samp>](## "node_type_keys.[].underlay_router") | Boolean |  | True |  | Is this node type a L3 device. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;uplink_type</samp>](## "node_type_keys.[].uplink_type") | String |  | p2p | Valid Values:<br>- p2p<br>- port-channel | Uplinks must be p2p if "vtep" or "underlay_router" is true. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vtep</samp>](## "node_type_keys.[].vtep") | Boolean |  | False |  | Is this switch an EVPN VTEP. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mpls_lsr</samp>](## "node_type_keys.[].mpls_lsr") | Boolean |  | False |  | Is this switch an MPLS LSR. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_addressing</samp>](## "node_type_keys.[].ip_addressing") | Dictionary |  |  |  | Override ip_addressing templates. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;python_module</samp>](## "node_type_keys.[].ip_addressing.python_module") | String |  |  |  | Python Module to import for IP addressing - default inherited from templates.ip_addressing.python_module |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;python_class_name</samp>](## "node_type_keys.[].ip_addressing.python_class_name") | String |  |  |  | Name of Python Class to import for IP addressing  - default inherited from templates.ip_addressing.python_class_name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;router_id</samp>](## "node_type_keys.[].ip_addressing.router_id") | String |  |  |  | Path to J2 template - default inherited from templates.ip_addressing.router_id. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;router_id_ipv6</samp>](## "node_type_keys.[].ip_addressing.router_id_ipv6") | String |  |  |  | Path to J2 template - default inherited from templates.ip_addressing.router_id_ipv6. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_ip_primary</samp>](## "node_type_keys.[].ip_addressing.mlag_ip_primary") | String |  |  |  | Path to J2 template - default inherited from templates.ip_addressing.mlag_ip_primary. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_ip_secondary</samp>](## "node_type_keys.[].ip_addressing.mlag_ip_secondary") | String |  |  |  | Path to J2 template - default inherited from templates.ip_addressing.mlag_ip_secondary. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_l3_ip_primary</samp>](## "node_type_keys.[].ip_addressing.mlag_l3_ip_primary") | String |  |  |  | Path to J2 template - default inherited from templates.ip_addressing.mlag_l3_ip_primary. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_l3_ip_secondary</samp>](## "node_type_keys.[].ip_addressing.mlag_l3_ip_secondary") | String |  |  |  | Path to J2 template - default inherited from templates.ip_addressing.mlag_l3_ip_secondary. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_ibgp_peering_ip_primary</samp>](## "node_type_keys.[].ip_addressing.mlag_ibgp_peering_ip_primary") | String |  |  |  | Path to J2 template - default inherited from templates.ip_addressing.mlag_ibgp_peering_ip_primary. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_ibgp_peering_ip_secondary</samp>](## "node_type_keys.[].ip_addressing.mlag_ibgp_peering_ip_secondary") | String |  |  |  | Path to J2 template - default inherited from templates.ip_addressing.mlag_ibgp_peering_ip_secondary. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;p2p_uplinks_ip</samp>](## "node_type_keys.[].ip_addressing.p2p_uplinks_ip") | String |  |  |  | Path to J2 template - default inherited from templates.ip_addressing.p2p_uplinks_ip. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;p2p_uplinks_peer_ip</samp>](## "node_type_keys.[].ip_addressing.p2p_uplinks_peer_ip") | String |  |  |  | Path to J2 template - default inherited from templates.ip_addressing.p2p_uplinks_peer_ip. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vtep_ip_mlag</samp>](## "node_type_keys.[].ip_addressing.vtep_ip_mlag") | String |  |  |  | Path to J2 template - default inherited from templates.ip_addressing.vtep_ip_mlag. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vtep_ip</samp>](## "node_type_keys.[].ip_addressing.vtep_ip") | String |  |  |  | Path to J2 template - default inherited from templates.ip_addressing.vtep_ip. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;interface_descriptions</samp>](## "node_type_keys.[].interface_descriptions") | Dictionary |  |  |  | Override interface_descriptions templates<br>If description templates use Jinja2, they have to strip whitespaces using {%- -%} on any code blocks.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;python_module</samp>](## "node_type_keys.[].interface_descriptions.python_module") | String |  |  |  | Python Module to import for interface descriptions - default inherited from templates.interface_descriptions.python_module |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;python_class_name</samp>](## "node_type_keys.[].interface_descriptions.python_class_name") | String |  |  |  | Name of Python Class to import for interface descriptions - default inherited from templates.interface_descriptions.python_class_name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;underlay_ethernet_interfaces</samp>](## "node_type_keys.[].interface_descriptions.underlay_ethernet_interfaces") | String |  |  |  | Path to J2 template - default inherited from templates.interface_descriptions.underlay_ethernet_interfaces. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;underlay_port_channel_interfaces</samp>](## "node_type_keys.[].interface_descriptions.underlay_port_channel_interfaces") | String |  |  |  | Path to J2 template - default inherited from templates.interface_descriptions.underlay_port_channel_interfaces. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_ethernet_interfaces</samp>](## "node_type_keys.[].interface_descriptions.mlag_ethernet_interfaces") | String |  |  |  | Path to J2 template - default inherited from templates.interface_descriptions.mlag_ethernet_interfaces. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_port_channel_interfaces</samp>](## "node_type_keys.[].interface_descriptions.mlag_port_channel_interfaces") | String |  |  |  | Path to J2 template - default inherited from templates.interface_descriptions.mlag_port_channel_interfaces. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;connected_endpoints_ethernet_interfaces</samp>](## "node_type_keys.[].interface_descriptions.connected_endpoints_ethernet_interfaces") | String |  |  |  | Path to J2 template - default inherited from templates.interface_descriptions.connected_endpoints_ethernet_interfaces. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;connected_endpoints_port_channel_interfaces</samp>](## "node_type_keys.[].interface_descriptions.connected_endpoints_port_channel_interfaces") | String |  |  |  | Path to J2 template - default inherited from templates.interface_descriptions.connected_endpoints_port_channel_interfaces. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;overlay_loopback_interface</samp>](## "node_type_keys.[].interface_descriptions.overlay_loopback_interface") | String |  |  |  | Path to J2 template - default inherited from templates.interface_descriptions.overlay_loopback_interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vtep_loopback_interface</samp>](## "node_type_keys.[].interface_descriptions.vtep_loopback_interface") | String |  |  |  | Path to J2 template - default inherited from templates.interface_descriptions.vtep_loopback_interface. |

=== "YAML"

    ```yaml
    node_type_keys:
      - key: <str>
        type: <str>
        connected_endpoints: <bool>
        default_evpn_role: <str>
        default_ptp_priority1: <int>
        default_underlay_routing_protocol: <str>
        default_overlay_routing_protocol: <str>
        default_mpls_overlay_role: <str>
        default_overlay_address_families:
          - <str>
        default_evpn_encapsulation: <str>
        mlag_support: <bool>
        network_services:
          l1: <bool>
          l2: <bool>
          l3: <bool>
        underlay_router: <bool>
        uplink_type: <str>
        vtep: <bool>
        mpls_lsr: <bool>
        ip_addressing:
          python_module: <str>
          python_class_name: <str>
          router_id: <str>
          router_id_ipv6: <str>
          mlag_ip_primary: <str>
          mlag_ip_secondary: <str>
          mlag_l3_ip_primary: <str>
          mlag_l3_ip_secondary: <str>
          mlag_ibgp_peering_ip_primary: <str>
          mlag_ibgp_peering_ip_secondary: <str>
          p2p_uplinks_ip: <str>
          p2p_uplinks_peer_ip: <str>
          vtep_ip_mlag: <str>
          vtep_ip: <str>
        interface_descriptions:
          python_module: <str>
          python_class_name: <str>
          underlay_ethernet_interfaces: <str>
          underlay_port_channel_interfaces: <str>
          mlag_ethernet_interfaces: <str>
          mlag_port_channel_interfaces: <str>
          connected_endpoints_ethernet_interfaces: <str>
          connected_endpoints_port_channel_interfaces: <str>
          overlay_loopback_interface: <str>
          vtep_loopback_interface: <str>
    ```

## Only Local VLAN Trunk Groups

A vlan can have many trunk_groups assigned. To avoid unneeded configuration changes on all leaf
switches when a new trunk group is added, this feature will only configure the vlan trunk groups
matched with local connected_endpoints.
See "Details on only_local_vlan_trunk_groups" below.
Requires "enable_trunk_groups: true"

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>only_local_vlan_trunk_groups</samp>](## "only_local_vlan_trunk_groups") | Boolean |  | False |  |  |

=== "YAML"

    ```yaml
    only_local_vlan_trunk_groups: <bool>
    ```

## Overlay CVX Servers

List of CVX vxlan overlay controllers.
Required if overlay_routing_protocol == CVX.
CVX servers (VMs) are peering using their management interface, so mgmt_ip must be set for all CVX servers.

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>overlay_cvx_servers</samp>](## "overlay_cvx_servers") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;- &lt;str&gt;</samp>](## "overlay_cvx_servers.[].&lt;str&gt;") | String |  |  |  | 'inventory_hostname' of CVX server |

=== "YAML"

    ```yaml
    overlay_cvx_servers:
      - <str>
    ```

## Overlay Her Flood List Per Vni

When using Head-End Replication, configure flood-lists per VNI.
By default HER will be configured with a common flood-list containing all VTEPs.
This behavior can be changed to per-VNI flood-lists by setting `overlay_her_flood_list_per_vni: true`.
This will make `eos_designs` consider configured VLANs per VTEP, and only include the relevant VTEPs to each VNI's flood-list.

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>overlay_her_flood_list_per_vni</samp>](## "overlay_her_flood_list_per_vni") | Boolean |  | False |  |  |

=== "YAML"

    ```yaml
    overlay_her_flood_list_per_vni: <bool>
    ```

## Overlay Her Flood List Scope

When using Head-End Replication, set the scope of flood-lists to Fabric or DC.
By default all VTEPs in the Fabric (part of the inventory group referenced by "fabric_name") are added to the flood-lists.
This can be changed to all VTEPs in the DC (part of the inventory group referenced by "dc_name").
This is useful if Border Leaf switches are dividing the VXLAN overlay into separate domains.

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>overlay_her_flood_list_scope</samp>](## "overlay_her_flood_list_scope") | String |  | fabric | Valid Values:<br>- fabric<br>- dc |  |

=== "YAML"

    ```yaml
    overlay_her_flood_list_scope: <str>
    ```

## Overlay Loopback Description

Customize the description on overlay interface Loopback0.

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>overlay_loopback_description</samp>](## "overlay_loopback_description") | String |  |  |  |  |

=== "YAML"

    ```yaml
    overlay_loopback_description: <str>
    ```

## Overlay MLAG Rfc5549

IPv6 Unnumbered for MLAG iBGP connections.
Requires "underlay_rfc5549: true".

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>overlay_mlag_rfc5549</samp>](## "overlay_mlag_rfc5549") | Boolean |  | False |  |  |

=== "YAML"

    ```yaml
    overlay_mlag_rfc5549: <bool>
    ```

## Overlay Rd Type

Specify RD type.
Route Distinguisher (RD) for L2 / L3 services is set to <overlay_loopback>:<vni> per default.
By configuring overlay_rd_type the Administrator subfield (first part of RD) can be set to other values.
Note:
RD is a 48-bit value which is split into <16-bit>:<32-bit> or <32-bit>:<16-bit>.
For loopback or 32-bit ASN/number the VNI can only be a 16-bit number.
For 16-bit ASN/number the VNI can be a 32-bit number.

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>overlay_rd_type</samp>](## "overlay_rd_type") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;admin_subfield</samp>](## "overlay_rd_type.admin_subfield") | String |  | overlay_loopback_ip |  | "vtep_loopback" or "bgp_as" or <IPv4 Address> or interger between <0-65535> or integer between <0-4294967295> or "overlay_loopback_ip".<br> |
    | [<samp>&nbsp;&nbsp;admin_subfield_offset</samp>](## "overlay_rd_type.admin_subfield_offset") | String |  |  |  | Offset can only be used if admin_subfield is an interger between <0-4294967295> or "switch_id".<br>Total value of admin_subfield + admin_subfield_offset must be <= 4294967295. |

=== "YAML"

    ```yaml
    overlay_rd_type:
      admin_subfield: <str>
      admin_subfield_offset: <str>
    ```

## Overlay Routing Protocol Address Family

When set to `ipv6`, enable overlay EVPN peering with IPv6 addresses.
This feature depends on underlay_ipv6 variable. As of today, only RFC5549 is capable to transport IPv6 in the underlay.

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>overlay_routing_protocol_address_family</samp>](## "overlay_routing_protocol_address_family") | String |  | ipv4 | Valid Values:<br>- ipv4<br>- ipv6 |  |

=== "YAML"

    ```yaml
    overlay_routing_protocol_address_family: <str>
    ```

## Overlay Routing Protocol

- The following overlay routing protocols are supported:
  - eBGP: Configures fabric with eBGP, default for l3ls-evpn design.
  - iBGP: Configured fabric with iBGP, only supported with OSPF or ISIS variants in underlay, default for mpls design.
  - CVX: Configures fabric to leverage CloudVision eXchange as the overlay controller.
  - HER: Configures fabric with Head-End Replication, configures static VXLAN flood-lists instead of using a dynamic overlay protocol.
  - none: No overlay configuration will be generated, default for l2ls design.

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>overlay_routing_protocol</samp>](## "overlay_routing_protocol") | String |  | ebgp | Value is converted to lower case<br>Valid Values:<br>- ebgp<br>- ibgp<br>- cvx<br>- her<br>- none |  |

=== "YAML"

    ```yaml
    overlay_routing_protocol: <str>
    ```

## Overlay Rt Type

Specify RT type.
Route Target (RT) for L2 / L3 services is set to <vni>:<vni> per default.
By configuring overlay_rt_type the Administrator subfield (first part of RT) can be set to other values.
Notes:
RT is a 48-bit value which is split into <16-bit>:<32-bit> or <32-bit>:<16-bit>.
For 32-bit ASN/number the VNI can only be a 16-bit number.
For 16-bit ASN/number the VNI can be a 32-bit number.

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>overlay_rt_type</samp>](## "overlay_rt_type") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;admin_subfield</samp>](## "overlay_rt_type.admin_subfield") | String |  | mac_vrf_id |  | "bgp_as" or interger between <0-65535> or integer between <0-4294967295>.<br> |

=== "YAML"

    ```yaml
    overlay_rt_type:
      admin_subfield: <str>
    ```

## P2P Uplinks MTU

Point to Point Links MTU

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>p2p_uplinks_mtu</samp>](## "p2p_uplinks_mtu") | Integer |  | 9214 | Min: 68<br>Max: 65535 |  |

=== "YAML"

    ```yaml
    p2p_uplinks_mtu: <int>
    ```

## P2P Uplinks QOS Profile

QOS Profile assigned on all infrastructure links

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>p2p_uplinks_qos_profile</samp>](## "p2p_uplinks_qos_profile") | String |  |  |  |  |

=== "YAML"

    ```yaml
    p2p_uplinks_qos_profile: <str>
    ```

## Platform Settings

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>platform_settings</samp>](## "platform_settings") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;- platforms</samp>](## "platform_settings.[].platforms") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "platform_settings.[].platforms.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;trident_forwarding_table_partition</samp>](## "platform_settings.[].trident_forwarding_table_partition") | String |  |  |  | Only applied when evpn_multicast is true |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;reload_delay</samp>](## "platform_settings.[].reload_delay") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag</samp>](## "platform_settings.[].reload_delay.mlag") | Integer |  |  | Min: 0<br>Max: 86400 | In seconds |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;non_mlag</samp>](## "platform_settings.[].reload_delay.non_mlag") | Integer |  |  | Min: 0<br>Max: 86400 | In seconds |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;tcam_profile</samp>](## "platform_settings.[].tcam_profile") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;lag_hardware_only</samp>](## "platform_settings.[].lag_hardware_only") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;feature_support</samp>](## "platform_settings.[].feature_support") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;queue_monitor_length_notify</samp>](## "platform_settings.[].feature_support.queue_monitor_length_notify") | Boolean |  | True |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interface_storm_control</samp>](## "platform_settings.[].feature_support.interface_storm_control") | Boolean |  | True |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp_update_wait_install</samp>](## "platform_settings.[].feature_support.bgp_update_wait_install") | Boolean |  | True |  | Disables FIB updates and route advertisement when the BGP instance is initiated until the BGP convergence state is reached.<br>Can be overridden by setting "bgp_update_wait_install" host/group_vars<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp_update_wait_for_convergence</samp>](## "platform_settings.[].feature_support.bgp_update_wait_for_convergence") | Boolean |  | True |  | Do not advertise reachability to a prefix until that prefix has been installed in hardware.<br>This will eliminate any temporary black holes due to a BGP speaker advertising reachability to a prefix that may not yet be installed into the forwarding plane.<br>Can be overridden by setting "bgp_update_wait_for_convergence" host/group_vars<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;management_interface</samp>](## "platform_settings.[].management_interface") | String |  | Management1 |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "platform_settings.[].raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the root level of the final EOS configuration |

=== "YAML"

    ```yaml
    platform_settings:
      - platforms:
          - <str>
        trident_forwarding_table_partition: <str>
        reload_delay:
          mlag: <int>
          non_mlag: <int>
        tcam_profile: <str>
        lag_hardware_only: <bool>
        feature_support:
          queue_monitor_length_notify: <bool>
          interface_storm_control: <bool>
          bgp_update_wait_install: <bool>
          bgp_update_wait_for_convergence: <bool>
        management_interface: <str>
        raw_eos_cli: <str>
    ```

## Platform Speed Groups

Set Hardware Speed Groups per Platform

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>platform_speed_groups</samp>](## "platform_speed_groups") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;- platform</samp>](## "platform_speed_groups.[].platform") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;speeds</samp>](## "platform_speed_groups.[].speeds") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- speed</samp>](## "platform_speed_groups.[].speeds.[].speed") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;speed_groups</samp>](## "platform_speed_groups.[].speeds.[].speed_groups") | List, items: Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;int&gt;</samp>](## "platform_speed_groups.[].speeds.[].speed_groups.[].&lt;int&gt;") | Integer |  |  |  |  |

=== "YAML"

    ```yaml
    platform_speed_groups:
      - platform: <str>
        speeds:
          - speed: <str>
            speed_groups:
              - <int>
    ```

## Pod Name

POD Name, only used in Fabric Documentation (Optional), fallback to dc_name and then to fabric_name.
Recommended to be common between Spines and Leafs within a POD (One l3ls topology).

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>pod_name</samp>](## "pod_name") | String |  |  |  |  |

=== "YAML"

    ```yaml
    pod_name: <str>
    ```

## Port Profiles

Optional profiles to share common settings for connected_endpoints and/or network_ports.
Keys are the same used under endpoints adapters. Keys defined under endpoints adapters take precedence.

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>port_profiles</samp>](## "port_profiles") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;- profile</samp>](## "port_profiles.[].profile") | String | Required, Unique |  |  | Port profile name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;parent_profile</samp>](## "port_profiles.[].parent_profile") | String |  |  |  | Parent profile is optional.<br>Port_profiles can refer to another port_profile to inherit settings in up to two levels (adapter->profile->parent_profile). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;endpoint_ports</samp>](## "port_profiles.[].endpoint_ports") | List, items: String |  |  |  | Endpoint ports is used for description, required unless description is set.<br>The lists `endpoint_ports`, `switch_ports`, and `switches` must have the same length.<br>Each list item is one switchport.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "port_profiles.[].endpoint_ports.[].&lt;str&gt;") | String |  |  |  | Interface name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;speed</samp>](## "port_profiles.[].speed") | String |  |  |  | Set adapter speed: `< interface_speed >`, `forced < interface_speed >`, `auto < interface_speed >`.<br>If not specified will be auto.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "port_profiles.[].description") | String |  |  |  | By default the description is built leveraging `<peer>_<peer_interface>`.<br>When set this key will overide the default value on the physical ports.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "port_profiles.[].enabled") | Boolean |  | True |  | Administrative state, setting to false will set the port to 'shutdown' in the intended configuration.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "port_profiles.[].mode") | String |  |  | Valid Values:<br>- access<br>- dot1q-tunnel<br>- trunk<br>- trunk phone | Interface mode. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mtu</samp>](## "port_profiles.[].mtu") | Integer |  |  | Min: 68<br>Max: 65535 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;l2_mtu</samp>](## "port_profiles.[].l2_mtu") | Integer |  |  | Min: 68<br>Max: 9416 | This should only be defined for platforms supporting the "l2 mtu" CLI command. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;native_vlan</samp>](## "port_profiles.[].native_vlan") | Integer |  |  | Min: 1<br>Max: 4094 | Native VLAN for a trunk port.<br>If both `native_vlan` and `native_vlan_tag`, `native_vlan_tag` takes precedence.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;native_vlan_tag</samp>](## "port_profiles.[].native_vlan_tag") | Boolean |  | False |  | If both `native_vlan` and `native_vlan_tag`, `native_vlan_tag` takes precedence. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;trunk_groups</samp>](## "port_profiles.[].trunk_groups") | List, items: String |  |  |  | Required with `enable_trunk_groups: true`.<br>Trunk Groups are used for limiting VLANs on trunk ports to VLANs with the same Trunk Group.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "port_profiles.[].trunk_groups.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vlans</samp>](## "port_profiles.[].vlans") | String |  |  |  | Interface VLANs - if not set, the EOS default is that all VLANs are allowed for trunk ports, and VLAN 1 will be used for access ports. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_portfast</samp>](## "port_profiles.[].spanning_tree_portfast") | String |  |  | Valid Values:<br>- edge<br>- network |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_bpdufilter</samp>](## "port_profiles.[].spanning_tree_bpdufilter") | String |  |  | Valid Values:<br>- enabled<br>- disabled<br>- True<br>- False<br>- true<br>- false |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_bpduguard</samp>](## "port_profiles.[].spanning_tree_bpduguard") | String |  |  | Valid Values:<br>- enabled<br>- disabled<br>- True<br>- False<br>- true<br>- false |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;flowcontrol</samp>](## "port_profiles.[].flowcontrol") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;received</samp>](## "port_profiles.[].flowcontrol.received") | String |  |  | Valid Values:<br>- received<br>- send<br>- on |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;qos_profile</samp>](## "port_profiles.[].qos_profile") | String |  |  |  | QOS profile name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ptp</samp>](## "port_profiles.[].ptp") | Dictionary |  |  |  | The global PTP profile parameters will be applied to all connected endpoints where `ptp` is manually enabled.<br>`ptp role master` is set to ensure control over the PTP topology.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "port_profiles.[].ptp.enabled") | Boolean |  | False |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;endpoint_role</samp>](## "port_profiles.[].ptp.endpoint_role") | String |  | follower | Valid Values:<br>- bmca<br>- default<br>- follower |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;profile</samp>](## "port_profiles.[].ptp.profile") | String |  | aes67-r16-2016 | Valid Values:<br>- aes67<br>- aes67-r16-2016<br>- smpte2059-2 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;link_tracking</samp>](## "port_profiles.[].link_tracking") | Dictionary |  |  |  | Configure the downstream interfaces of a respective Link Tracking Group.<br>If `port_channel` is defined in an adapter, then the port-channel interface is configured to be the downstream.<br>Else all the ethernet interfaces will be configured as downstream -> to configure single-active EVPN multihomed networks.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "port_profiles.[].link_tracking.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "port_profiles.[].link_tracking.name") | String |  |  |  | Tracking group name.<br>The default group name is taken from fabric variable of the switch, `link_tracking.groups[0].name` with default value being "LT_GROUP1".<br>Optional if default link_tracking settings are configured on the node.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;dot1x</samp>](## "port_profiles.[].dot1x") | Dictionary |  |  |  | 802.1x |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;port_control</samp>](## "port_profiles.[].dot1x.port_control") | String |  |  | Valid Values:<br>- auto<br>- force-authorized<br>- force-unauthorized |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;port_control_force_authorized_phone</samp>](## "port_profiles.[].dot1x.port_control_force_authorized_phone") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;reauthentication</samp>](## "port_profiles.[].dot1x.reauthentication") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pae</samp>](## "port_profiles.[].dot1x.pae") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "port_profiles.[].dot1x.pae.mode") | String |  |  | Valid Values:<br>- authenticator |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;authentication_failure</samp>](## "port_profiles.[].dot1x.authentication_failure") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "port_profiles.[].dot1x.authentication_failure.action") | String |  |  | Valid Values:<br>- allow<br>- drop |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;allow_vlan</samp>](## "port_profiles.[].dot1x.authentication_failure.allow_vlan") | Integer |  |  | Min: 1<br>Max: 4094 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;host_mode</samp>](## "port_profiles.[].dot1x.host_mode") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "port_profiles.[].dot1x.host_mode.mode") | String |  |  | Valid Values:<br>- multi-host<br>- single-host |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;multi_host_authenticated</samp>](## "port_profiles.[].dot1x.host_mode.multi_host_authenticated") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mac_based_authentication</samp>](## "port_profiles.[].dot1x.mac_based_authentication") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "port_profiles.[].dot1x.mac_based_authentication.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;always</samp>](## "port_profiles.[].dot1x.mac_based_authentication.always") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;host_mode_common</samp>](## "port_profiles.[].dot1x.mac_based_authentication.host_mode_common") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;timeout</samp>](## "port_profiles.[].dot1x.timeout") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;idle_host</samp>](## "port_profiles.[].dot1x.timeout.idle_host") | Integer |  |  | Min: 10<br>Max: 65535 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;quiet_period</samp>](## "port_profiles.[].dot1x.timeout.quiet_period") | Integer |  |  | Min: 1<br>Max: 65535 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;reauth_period</samp>](## "port_profiles.[].dot1x.timeout.reauth_period") | String |  |  |  | Range 60-4294967295 or "server". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;reauth_timeout_ignore</samp>](## "port_profiles.[].dot1x.timeout.reauth_timeout_ignore") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tx_period</samp>](## "port_profiles.[].dot1x.timeout.tx_period") | Integer |  |  | Min: 1<br>Max: 65535 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;reauthorization_request_limit</samp>](## "port_profiles.[].dot1x.reauthorization_request_limit") | Integer |  |  | Min: 1<br>Max: 10 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;storm_control</samp>](## "port_profiles.[].storm_control") | Dictionary |  |  |  | Storm control settings applied on port toward the endpoint. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;all</samp>](## "port_profiles.[].storm_control.all") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;level</samp>](## "port_profiles.[].storm_control.all.level") | Integer |  |  |  | Configure maximum storm-control level. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unit</samp>](## "port_profiles.[].storm_control.all.unit") | String |  | percent | Valid Values:<br>- percent<br>- pps | Optional variable and is hardware dependent. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;broadcast</samp>](## "port_profiles.[].storm_control.broadcast") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;level</samp>](## "port_profiles.[].storm_control.broadcast.level") | Integer |  |  |  | Configure maximum storm-control level. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unit</samp>](## "port_profiles.[].storm_control.broadcast.unit") | String |  | percent | Valid Values:<br>- percent<br>- pps | Optional variable and is hardware dependent. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;multicast</samp>](## "port_profiles.[].storm_control.multicast") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;level</samp>](## "port_profiles.[].storm_control.multicast.level") | Integer |  |  |  | Configure maximum storm-control level. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unit</samp>](## "port_profiles.[].storm_control.multicast.unit") | String |  | percent | Valid Values:<br>- percent<br>- pps | Optional variable and is hardware dependent. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unknown_unicast</samp>](## "port_profiles.[].storm_control.unknown_unicast") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;level</samp>](## "port_profiles.[].storm_control.unknown_unicast.level") | Integer |  |  |  | Configure maximum storm-control level. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unit</samp>](## "port_profiles.[].storm_control.unknown_unicast.unit") | String |  | percent | Valid Values:<br>- percent<br>- pps | Optional variable and is hardware dependent. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;monitor_sessions</samp>](## "port_profiles.[].monitor_sessions") | List, items: Dictionary |  |  |  | Used to define switchports as source or destination for monitoring sessions. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "port_profiles.[].monitor_sessions.[].name") | String | Required |  |  | Session name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;role</samp>](## "port_profiles.[].monitor_sessions.[].role") | String |  |  | Valid Values:<br>- source<br>- destination |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_settings</samp>](## "port_profiles.[].monitor_sessions.[].source_settings") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction</samp>](## "port_profiles.[].monitor_sessions.[].source_settings.direction") | String |  |  | Valid Values:<br>- rx<br>- tx<br>- both |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_group</samp>](## "port_profiles.[].monitor_sessions.[].source_settings.access_group") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "port_profiles.[].monitor_sessions.[].source_settings.access_group.type") | String |  |  | Valid Values:<br>- ip<br>- ipv6<br>- mac |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "port_profiles.[].monitor_sessions.[].source_settings.access_group.name") | String |  |  |  | ACL name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority</samp>](## "port_profiles.[].monitor_sessions.[].source_settings.access_group.priority") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;session_settings</samp>](## "port_profiles.[].monitor_sessions.[].session_settings") | Dictionary |  |  |  | Session settings are defined per session name.<br>Different session_settings for the same session name will be combined/merged.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;encapsulation_gre_metadata_tx</samp>](## "port_profiles.[].monitor_sessions.[].session_settings.encapsulation_gre_metadata_tx") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;header_remove_size</samp>](## "port_profiles.[].monitor_sessions.[].session_settings.header_remove_size") | Integer |  |  |  | Number of bytes to remove from header. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_group</samp>](## "port_profiles.[].monitor_sessions.[].session_settings.access_group") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "port_profiles.[].monitor_sessions.[].session_settings.access_group.type") | String |  |  | Valid Values:<br>- ip<br>- ipv6<br>- mac |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "port_profiles.[].monitor_sessions.[].session_settings.access_group.name") | String |  |  |  | ACL name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rate_limit_per_ingress_chip</samp>](## "port_profiles.[].monitor_sessions.[].session_settings.rate_limit_per_ingress_chip") | String |  |  |  | Ratelimit and unit as string.<br>Examples:<br>  "100000 bps"<br>  "100 kbps"<br>  "10 mbps"<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rate_limit_per_egress_chip</samp>](## "port_profiles.[].monitor_sessions.[].session_settings.rate_limit_per_egress_chip") | String |  |  |  | Ratelimit and unit as string.<br>Examples:<br>  "100000 bps"<br>  "100 kbps"<br>  "10 mbps"<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sample</samp>](## "port_profiles.[].monitor_sessions.[].session_settings.sample") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;truncate</samp>](## "port_profiles.[].monitor_sessions.[].session_settings.truncate") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "port_profiles.[].monitor_sessions.[].session_settings.truncate.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;size</samp>](## "port_profiles.[].monitor_sessions.[].session_settings.truncate.size") | Integer |  |  |  | Size in bytes |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ethernet_segment</samp>](## "port_profiles.[].ethernet_segment") | Dictionary |  |  |  | Settings for all or single-active EVPN multihoming. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;short_esi</samp>](## "port_profiles.[].ethernet_segment.short_esi") | String | Required |  |  | In format xxxx:xxxx:xxxx or "auto".<br>Define a manual short-esi (be careful using this on profiles) or set the value to "auto" to automatically generate the value.<br>Please see the notes under "EVPN A/A ESI dual and single-attached endpoint scenarios" before setting `short_esi: auto`.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;redundancy</samp>](## "port_profiles.[].ethernet_segment.redundancy") | String |  |  | Valid Values:<br>- all-active<br>- single-active | If omitted, Port-Channels use the EOS default of all-active.<br>If omitted, Ethernet interfaces are configured as single-active.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;designated_forwarder_algorithm</samp>](## "port_profiles.[].ethernet_segment.designated_forwarder_algorithm") | String |  |  | Valid Values:<br>- auto<br>- modulus<br>- preference | Configure DF algorithm and preferences.<br>- auto: Use preference-based algorithm and assign preference based on position of device in the 'switches' list,<br>  e.g., assuming a list of three switches, this would assign a preference of 200 to the first switch, 100 to the 2nd, and 0 to the third.<br>- preference: Set preference for each switch manually using designated_forwarder_preferences key.<br>- modulus: Use the default modulus-based algorithm.<br>If omitted, Port-Channels use the EOS default of modulus.<br>If omitted, Ethernet interfaces default to the 'auto' mechanism detailed above.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;designated_forwarder_preferences</samp>](## "port_profiles.[].ethernet_segment.designated_forwarder_preferences") | List, items: String |  |  |  | Manual preference as described above, required only for preference algorithm. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "port_profiles.[].ethernet_segment.designated_forwarder_preferences.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dont_preempt</samp>](## "port_profiles.[].ethernet_segment.dont_preempt") | Boolean |  |  |  | Disable preemption for single-active forwarding when auto/manual DF preference is configured. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;port_channel</samp>](## "port_profiles.[].port_channel") | Dictionary |  |  |  | Used for port-channel adapter. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "port_profiles.[].port_channel.mode") | String |  |  | Valid Values:<br>- active<br>- passive<br>- on | Port-Channel Mode. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;channel_id</samp>](## "port_profiles.[].port_channel.channel_id") | Integer |  |  |  | Port-Channel ID.<br>If no channel_id is specified, an id is generated from the first switch port in the port channel.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "port_profiles.[].port_channel.description") | String |  |  |  | By default the description is built leveraging `<peer>` name or `adapter.description` when defined.<br>When this key is defined, it will append its content to the physical port description.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "port_profiles.[].port_channel.enabled") | Boolean |  | True |  | Port-Channel administrative state.<br>Setting to false will set port to 'shutdown' in intended configuration.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;esi</samp>](## "port_profiles.[].port_channel.esi") <span style="color:red">removed</span> | String |  |  |  | Format xxxx:xxxx:xxxx.<span style="color:red">This key was removed. Support was removed in AVD version 4.0.0. Use <samp>short_esi</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;short_esi</samp>](## "port_profiles.[].port_channel.short_esi") | String |  |  |  | In format xxxx:xxxx:xxxx or "auto". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;lacp_fallback</samp>](## "port_profiles.[].port_channel.lacp_fallback") | Dictionary |  |  |  | LACP fallback configuration. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "port_profiles.[].port_channel.lacp_fallback.mode") | String |  |  | Valid Values:<br>- static | Currently only static mode is supported. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;timeout</samp>](## "port_profiles.[].port_channel.lacp_fallback.timeout") | Integer |  |  |  | Timeout in seconds. EOS default is 90 seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;lacp_timer</samp>](## "port_profiles.[].port_channel.lacp_timer") | Dictionary |  |  |  | LACP timer configuration. Applies only when Port-channel mode is not "on". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "port_profiles.[].port_channel.lacp_timer.mode") | String |  |  | Valid Values:<br>- normal<br>- fast | LACP mode for interface members. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;multiplier</samp>](## "port_profiles.[].port_channel.lacp_timer.multiplier") | Integer |  |  |  | Number of LACP BPDUs lost before deeming the peer down. EOS default is 3. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;subinterfaces</samp>](## "port_profiles.[].port_channel.subinterfaces") | List, items: Dictionary |  |  |  | Port-Channel L2 Subinterfaces<br>Subinterfaces are only supported on routed port-channels, which means they cannot be configured on MLAG port-channels.<br>Setting short_esi: auto generates the short_esi automatically using a hash of configuration elements.<br>Please see the notes under "EVPN A/A ESI dual-attached endpoint scenario" before setting short_esi: auto.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- number</samp>](## "port_profiles.[].port_channel.subinterfaces.[].number") | Integer |  |  |  | Subinterface number |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;short_esi</samp>](## "port_profiles.[].port_channel.subinterfaces.[].short_esi") | String |  |  |  | In format xxxx:xxxx:xxxx or "auto"<br>Required for multihomed port-channels with subinterfaces<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vlan_id</samp>](## "port_profiles.[].port_channel.subinterfaces.[].vlan_id") | Integer |  |  | Min: 1<br>Max: 4094 | VLAN ID to bridge.<br>Default is subinterface number.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;encapsulation_vlan</samp>](## "port_profiles.[].port_channel.subinterfaces.[].encapsulation_vlan") | Dictionary |  |  |  | Client VLAN ID encapsulation.<br>Default is subinterface number.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;client_dot1q</samp>](## "port_profiles.[].port_channel.subinterfaces.[].encapsulation_vlan.client_dot1q") | Integer |  |  | Min: 1<br>Max: 4094 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "port_profiles.[].port_channel.raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the port-channel interface in the final EOS configuration. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "port_profiles.[].port_channel.structured_config") | Dictionary |  |  |  | Custom structured config added under port_channel_interfaces.<interface> for eos_cli_config_gen. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "port_profiles.[].raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the ethernet interface in the final EOS configuration. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "port_profiles.[].structured_config") | Dictionary |  |  |  | Custom structured config added under ethernet_interfaces.<interface> for eos_cli_config_gen. |

=== "YAML"

    ```yaml
    port_profiles:
      - profile: <str>
        parent_profile: <str>
        endpoint_ports:
          - <str>
        speed: <str>
        description: <str>
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

## PTP Profiles

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>ptp_profiles</samp>](## "ptp_profiles") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;- profile</samp>](## "ptp_profiles.[].profile") | String |  |  |  | PTP profile. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;announce</samp>](## "ptp_profiles.[].announce") | Dictionary |  |  |  | PTP announce interval. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interval</samp>](## "ptp_profiles.[].announce.interval") | Integer |  |  | Min: -7<br>Max: 4 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;timeout</samp>](## "ptp_profiles.[].announce.timeout") | Integer |  |  | Min: 2<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;delay_req</samp>](## "ptp_profiles.[].delay_req") | Integer |  |  | Min: -7<br>Max: 8 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;sync_message</samp>](## "ptp_profiles.[].sync_message") | Dictionary |  |  |  | PTP sync message interval. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interval</samp>](## "ptp_profiles.[].sync_message.interval") | Integer |  |  | Min: -7<br>Max: 3 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;transport</samp>](## "ptp_profiles.[].transport") | String |  |  | Valid Values:<br>- ipv4 |  |

=== "YAML"

    ```yaml
    ptp_profiles:
      - profile: <str>
        announce:
          interval: <int>
          timeout: <int>
        delay_req: <int>
        sync_message:
          interval: <int>
        transport: <str>
    ```

## Redundancy

Redundancy for chassis platforms with dual supervisors | Optional

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>redundancy</samp>](## "redundancy") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;protocol</samp>](## "redundancy.protocol") | String |  |  | Valid Values:<br>- sso<br>- rpr |  |

=== "YAML"

    ```yaml
    redundancy:
      protocol: <str>
    ```

## Serial Number

Serial Number of the device.
Used for documentation purpose in the fabric documentation as can also be used by the 'eos_config_deploy_cvp' role.
"serial_number" can also be set directly under "Fabric Topology".
If both are set, the setting under "Fabric Topology" takes precedence.

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>serial_number</samp>](## "serial_number") | String |  |  |  |  |

=== "YAML"

    ```yaml
    serial_number: <str>
    ```

## Shutdown Interfaces Towards Undeployed Peers

- It is possible to provision configurations for a complete topology but flag devices as undeployed using the host level variable `is_deployed: false`.

```yaml
# Use at the host level
is_deployed: < true or false or default -> true >
```

- By default, this will have no impact within the `eos_designs` role. Configs will still be generated by the `eos_cli_config_gen` role and will still be pushed by the `eos_config_deploy_eapi` directly to devices if used.
- However, if the `eos_config_deploy_cvp` role is used to push configurations, CloudVision will ignore the devices flagged  as `is_deployed: false` and not attempt to configure them.
- If the device is not present in the network due to CloudVision not configuring the device, `eos_validate_state` role will fail tests on peers of the undeployed device trying to verify that interfaces are up.
- To overcome this and shutdown interfaces towards undeployed peers, the variable `shutdown_interfaces_towards_undeployed_peers` can be used, satisfying the `eos_validate_state` role interface tests.
- Again, this is only an issue if `eos_config_deploy_cvp` is used and the devices are not present in the network.

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>shutdown_interfaces_towards_undeployed_peers</samp>](## "shutdown_interfaces_towards_undeployed_peers") | Boolean |  | False |  |  |

=== "YAML"

    ```yaml
    shutdown_interfaces_towards_undeployed_peers: <bool>
    ```

## Snmp Settings

Set SNMP settings (optional).

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>snmp_settings</samp>](## "snmp_settings") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;contact</samp>](## "snmp_settings.contact") | String |  |  |  | SNMP contact. |
    | [<samp>&nbsp;&nbsp;location</samp>](## "snmp_settings.location") | Boolean |  | False |  | Set SNMP location. Formatted as {{ fabric_name }} {{ dc_name }} {{ pod_name }} {{ switch_rack }} {{ inventory_hostname }}. |
    | [<samp>&nbsp;&nbsp;compute_local_engineid</samp>](## "snmp_settings.compute_local_engineid") | Boolean |  | False |  | Generate a local engineId for SNMP using the 'compute_local_engineid_source' method.<br> |
    | [<samp>&nbsp;&nbsp;compute_local_engineid_source</samp>](## "snmp_settings.compute_local_engineid_source") | String |  | hostname_and_ip | Valid Values:<br>- hostname_and_ip<br>- system_mac | `compute_local_engineid_source` supports:<br>- `hostname_and_ip` generate a local engineId for SNMP by hashing via SHA1<br>  the string generated via the concatenation of the hostname plus the management IP.<br>  {{ inventory_hostname }} + {{ switch.mgmt_ip }}<br>- `system_mac` generate the switch default engine id for AVD usage<br>  To use this, `system_mac_address` MUST be set for the device<br>  The formula is f5717f + system_mac_address + 00<br> |
    | [<samp>&nbsp;&nbsp;compute_v3_user_localized_key</samp>](## "snmp_settings.compute_v3_user_localized_key") | Boolean |  | False |  | Requires compute_local_engineid to be `true`.<br>If enabled, the SNMPv3 passphrases for auth and priv are transformed using RFC 2574, matching the value they would take in EOS CLI.<br>The algorithm requires a local engineId, which is unknown to AVD, hence the necessity to generate one beforehand.<br> |
    | [<samp>&nbsp;&nbsp;users</samp>](## "snmp_settings.users") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "snmp_settings.users.[].name") | String |  |  |  | Username |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;group</samp>](## "snmp_settings.users.[].group") | String |  |  |  | Configuration of the SNMP User Groups are currently only possible using `structured_config`.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;version</samp>](## "snmp_settings.users.[].version") | String |  |  | Valid Values:<br>- v1<br>- v2c<br>- v3 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;auth</samp>](## "snmp_settings.users.[].auth") | String |  |  | Valid Values:<br>- md5<br>- sha<br>- sha256<br>- sha384<br>- sha512 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;auth_passphrase</samp>](## "snmp_settings.users.[].auth_passphrase") | String |  |  |  | Cleartext passphrase so the recommendation is to use vault. Requires 'auth' to be set. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priv</samp>](## "snmp_settings.users.[].priv") | String |  |  | Valid Values:<br>- des<br>- aes<br>- aes192<br>- aes256 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priv_passphrase</samp>](## "snmp_settings.users.[].priv_passphrase") | String |  |  |  | Cleartext passphrase so the recommendation is to use vault. Requires 'priv' to be set. |

=== "YAML"

    ```yaml
    snmp_settings:
      contact: <str>
      location: <bool>
      compute_local_engineid: <bool>
      compute_local_engineid_source: <str>
      compute_v3_user_localized_key: <bool>
      users:
        - name: <str>
          group: <str>
          version: <str>
          auth: <str>
          auth_passphrase: <str>
          priv: <str>
          priv_passphrase: <str>
    ```

## Svi Profiles

Profiles to share common settings for SVIs under `<network_services_key>.[].vrfs.svis`.
Keys are the same used under SVIs. Keys defined under SVIs take precedence.
Note: structured configuration is not merged recursively and will be taken directly from the most specific level in the following order:
1. svi.nodes[inventory_hostname].structured_config
2. svi_profile.nodes[inventory_hostname].structured_config
3. svi_parent_profile.nodes[inventory_hostname].structured_config
4. svi.structured_config
5. svi_profile.structured_config
6. svi_parent_profile.structured_config

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>svi_profiles</samp>](## "svi_profiles") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;- profile</samp>](## "svi_profiles.[].profile") | String | Required, Unique |  |  | Profile name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;parent_profile</samp>](## "svi_profiles.[].parent_profile") | String |  |  |  | Parent SVI profile name to apply.<br>svi_profiles can refer to another svi_profile to inherit settings in up to two levels (svi -> svi_profile -> svi_parent_profile). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "svi_profiles.[].nodes") | List, items: Dictionary |  |  |  | Define node specific configuration, such as unique IP addresses. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- node</samp>](## "svi_profiles.[].nodes.[].node") | String | Required, Unique |  |  | l3_leaf inventory hostname |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "svi_profiles.[].nodes.[].name") | String |  |  |  | VLAN name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "svi_profiles.[].nodes.[].enabled") | Boolean |  |  |  | Enable or disable interface |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "svi_profiles.[].nodes.[].description") | String |  |  |  | SVI description. By default set to VLAN name.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "svi_profiles.[].nodes.[].ip_address") | String |  |  |  | IPv4_address/Mask. Usually set under "nodes" to have unique IPv4 addresses per node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_address</samp>](## "svi_profiles.[].nodes.[].ipv6_address") | String |  |  |  | IPv6_address/Mask. Usually set under "nodes" to have unique IPv6 addresses per node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_enable</samp>](## "svi_profiles.[].nodes.[].ipv6_enable") | Boolean |  |  |  | Explicitly enable/disable link-local IPv6 addressing. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_address_virtual</samp>](## "svi_profiles.[].nodes.[].ip_address_virtual") | String |  |  |  | IPv4_address/Mask<br>IPv4 VXLAN Anycast IP address<br>Conserves IP addresses in VXLAN deployments as it doesn't require unique IP addresses on each node.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_address_virtual</samp>](## "svi_profiles.[].nodes.[].ipv6_address_virtual") | String |  |  |  | IPv6_address/Mask<br>ipv6 address virtuals to configure VXLAN Anycast IP address (Optional)<br>The below "ipv6_address_virtual" key will be deprecated in AVD v4.0 in favor of the new "ipv6_address_virtuals"<br>If both "ipv6_address_virtual" and "ipv6_address_virtuals" are set, all addresses will be configured<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_address_virtuals</samp>](## "svi_profiles.[].nodes.[].ipv6_address_virtuals") | List, items: String |  |  |  | IPv6 VXLAN Anycast IP addresses<br>Conserves IPv6 addresses in VXLAN deployments as it doesn't require unique IPv6 addresses on each node.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "svi_profiles.[].nodes.[].ipv6_address_virtuals.[].&lt;str&gt;") | String |  |  |  | IPv6_address/Mask |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_address_virtual_secondaries</samp>](## "svi_profiles.[].nodes.[].ip_address_virtual_secondaries") | List, items: String |  |  |  | Secondary IPv4 VXLAN Anycast IP addresses |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "svi_profiles.[].nodes.[].ip_address_virtual_secondaries.[].&lt;str&gt;") | String |  |  |  | IPv4_address/Mask |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_virtual_router_addresses</samp>](## "svi_profiles.[].nodes.[].ip_virtual_router_addresses") | List, items: String |  |  |  | IPv4 VARP addresses.<br>Requires an IP address to be configured on the SVI.<br>If ip_address_virtual is also set, ip_virtual_router_addresses will take precedence<br>_if_ there is an ip_address configured for the node.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "svi_profiles.[].nodes.[].ip_virtual_router_addresses.[].&lt;str&gt;") | String |  |  |  | IPv4_address/Mask or IPv4_address<br>IPv4_address/Mask will also configure a static route to the SVI per best practice.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_virtual_router_addresses</samp>](## "svi_profiles.[].nodes.[].ipv6_virtual_router_addresses") | List, items: String |  |  |  | IPv6 VARP addresses.<br>Requires an IPv6 address to be configured on the SVI.<br>If ipv6_address_virtuals is also set, ipv6_virtual_router_addresses will take precedence<br>_if_ there is an ipv6_address configured for the node.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "svi_profiles.[].nodes.[].ipv6_virtual_router_addresses.[].&lt;str&gt;") | String |  |  |  | IPv6_address |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_helpers</samp>](## "svi_profiles.[].nodes.[].ip_helpers") | List, items: Dictionary |  |  |  | IP helper for DHCP relay |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- ip_helper</samp>](## "svi_profiles.[].nodes.[].ip_helpers.[].ip_helper") | String | Required, Unique |  |  | IPv4 DHCP server IP |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_interface</samp>](## "svi_profiles.[].nodes.[].ip_helpers.[].source_interface") | String |  |  |  | Interface name to originate DHCP relay packets to DHCP server. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_vrf</samp>](## "svi_profiles.[].nodes.[].ip_helpers.[].source_vrf") | String |  |  |  | VRF to originate DHCP relay packets to DHCP server. If not set, EOS uses the VRF on the SVI. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vni_override</samp>](## "svi_profiles.[].nodes.[].vni_override") | Integer |  |  | Min: 1<br>Max: 16777215 | By default the VNI will be derived from "mac_vrf_vni_base"<br>The vni_override allows us to override this value and statically define it (optional)<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rt_override</samp>](## "svi_profiles.[].nodes.[].rt_override") | Integer |  |  | Min: 1<br>Max: 16777215 | By default the MAC VRF RD/RT ID will be derived from "mac_vrf_id_base"<br>The rt_override allows us to override this value and statically define it (optional)<br>If not set, vni_override will be used.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tags</samp>](## "svi_profiles.[].nodes.[].tags") | List, items: String |  | ['all'] |  | Tags leveraged for networks services filtering<br>Tags are matched against "filter.tags" defined under Fabric Topology variables<br>Tags are also matched against the "node_group" name under Fabric Topology variables<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "svi_profiles.[].nodes.[].tags.[].&lt;str&gt;") | String |  |  |  | Tag value |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;trunk_groups</samp>](## "svi_profiles.[].nodes.[].trunk_groups") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "svi_profiles.[].nodes.[].trunk_groups.[].&lt;str&gt;") | String |  |  |  | Trunk groups are used for limiting vlans to trunk ports assigned to the same trunk group<br>Requires "enable_trunk_groups: true"<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_l2_multicast</samp>](## "svi_profiles.[].nodes.[].evpn_l2_multicast") | Dictionary |  |  |  | Explicitly enable or disable evpn_l2_multicast to override setting of `<network_services_key>.[].evpn_l2_multicast.enabled`.<br>When evpn_l2_multicast.enabled is set to true for a vlan or a tenant, "igmp snooping" and "igmp snooping querier" will always be enabled, overriding those individual settings.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "svi_profiles.[].nodes.[].evpn_l2_multicast.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_l3_multicast</samp>](## "svi_profiles.[].nodes.[].evpn_l3_multicast") | Dictionary |  |  |  | Explicitly enable or disable evpn_l3_multicast to override setting of `<network_services_key>.[].evpn_l3_multicast.enabled` and `<network_services_key>.[].vrfs.[].evpn_l3_multicast.enabled`.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "svi_profiles.[].nodes.[].evpn_l3_multicast.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;igmp_snooping_enabled</samp>](## "svi_profiles.[].nodes.[].igmp_snooping_enabled") | Boolean |  |  |  | Enable IGMP Snooping (Enabled by default on EOS) |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;igmp_snooping_querier</samp>](## "svi_profiles.[].nodes.[].igmp_snooping_querier") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "svi_profiles.[].nodes.[].igmp_snooping_querier.enabled") | Boolean |  |  |  | Will be enabled automatically if evpn_l2_multicast is enabled. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_address</samp>](## "svi_profiles.[].nodes.[].igmp_snooping_querier.source_address") | String |  |  |  | IPv4_address<br>If not set, IP address of "Loopback0" will be used.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;version</samp>](## "svi_profiles.[].nodes.[].igmp_snooping_querier.version") | Integer |  |  | Valid Values:<br>- 1<br>- 2<br>- 3 | IGMP Version (By default EOS uses IGMP version 2 for IGMP querier) |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vxlan</samp>](## "svi_profiles.[].nodes.[].vxlan") | Boolean |  | True |  | Extend this SVI over VXLAN |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mtu</samp>](## "svi_profiles.[].nodes.[].mtu") | Integer |  |  |  | Interface MTU |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ospf</samp>](## "svi_profiles.[].nodes.[].ospf") | Dictionary |  |  |  | OSPF interface configuration |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "svi_profiles.[].nodes.[].ospf.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;point_to_point</samp>](## "svi_profiles.[].nodes.[].ospf.point_to_point") | Boolean |  | True |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;area</samp>](## "svi_profiles.[].nodes.[].ospf.area") | String |  | 0 |  | OSPF area ID |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cost</samp>](## "svi_profiles.[].nodes.[].ospf.cost") | Integer |  |  |  | OSPF link cost |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;authentication</samp>](## "svi_profiles.[].nodes.[].ospf.authentication") | String |  |  | Valid Values:<br>- simple<br>- message-digest |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;simple_auth_key</samp>](## "svi_profiles.[].nodes.[].ospf.simple_auth_key") | String |  |  |  | Password used with simple authentication |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;message_digest_keys</samp>](## "svi_profiles.[].nodes.[].ospf.message_digest_keys") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- id</samp>](## "svi_profiles.[].nodes.[].ospf.message_digest_keys.[].id") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hash_algorithm</samp>](## "svi_profiles.[].nodes.[].ospf.message_digest_keys.[].hash_algorithm") | String |  | sha512 | Valid Values:<br>- md5<br>- sha1<br>- sha256<br>- sha384<br>- sha512 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key</samp>](## "svi_profiles.[].nodes.[].ospf.message_digest_keys.[].key") | String |  |  |  | Type 7 encrypted key |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp</samp>](## "svi_profiles.[].nodes.[].bgp") | Dictionary |  |  |  | Structured configuration and EOS CLI commands rendered on router_bgp.vlans<br>This configuration will not be applied to vlan aware bundles<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "svi_profiles.[].nodes.[].bgp.structured_config") | Dictionary |  |  |  | Custom structured config added under vlan_interfaces.<interface> for eos_cli_config_gen.<br>Overrides the setting on SVI level.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "svi_profiles.[].nodes.[].bgp.raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the VLAN interface in the final EOS configuration<br>Overrides the setting on SVI level.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "svi_profiles.[].nodes.[].raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the VLAN interface in the final EOS configuration<br>Overrides the setting on SVI level<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "svi_profiles.[].nodes.[].structured_config") | Dictionary |  |  |  | Custom structured config added under vlan_interfaces.<interface> for eos_cli_config_gen.<br>Overrides the setting on SVI level. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "svi_profiles.[].name") | String |  |  |  | VLAN name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "svi_profiles.[].enabled") | Boolean |  |  |  | Enable or disable interface |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "svi_profiles.[].description") | String |  |  |  | SVI description. By default set to VLAN name.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "svi_profiles.[].ip_address") | String |  |  |  | IPv4_address/Mask. Usually set under "nodes" to have unique IPv4 addresses per node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_address</samp>](## "svi_profiles.[].ipv6_address") | String |  |  |  | IPv6_address/Mask. Usually set under "nodes" to have unique IPv6 addresses per node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_enable</samp>](## "svi_profiles.[].ipv6_enable") | Boolean |  |  |  | Explicitly enable/disable link-local IPv6 addressing. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_address_virtual</samp>](## "svi_profiles.[].ip_address_virtual") | String |  |  |  | IPv4_address/Mask<br>IPv4 VXLAN Anycast IP address<br>Conserves IP addresses in VXLAN deployments as it doesn't require unique IP addresses on each node.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_address_virtual</samp>](## "svi_profiles.[].ipv6_address_virtual") | String |  |  |  | IPv6_address/Mask<br>ipv6 address virtuals to configure VXLAN Anycast IP address (Optional)<br>The below "ipv6_address_virtual" key will be deprecated in AVD v4.0 in favor of the new "ipv6_address_virtuals"<br>If both "ipv6_address_virtual" and "ipv6_address_virtuals" are set, all addresses will be configured<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_address_virtuals</samp>](## "svi_profiles.[].ipv6_address_virtuals") | List, items: String |  |  |  | IPv6 VXLAN Anycast IP addresses<br>Conserves IPv6 addresses in VXLAN deployments as it doesn't require unique IPv6 addresses on each node.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "svi_profiles.[].ipv6_address_virtuals.[].&lt;str&gt;") | String |  |  |  | IPv6_address/Mask |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_address_virtual_secondaries</samp>](## "svi_profiles.[].ip_address_virtual_secondaries") | List, items: String |  |  |  | Secondary IPv4 VXLAN Anycast IP addresses |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "svi_profiles.[].ip_address_virtual_secondaries.[].&lt;str&gt;") | String |  |  |  | IPv4_address/Mask |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_virtual_router_addresses</samp>](## "svi_profiles.[].ip_virtual_router_addresses") | List, items: String |  |  |  | IPv4 VARP addresses.<br>Requires an IP address to be configured on the SVI.<br>If ip_address_virtual is also set, ip_virtual_router_addresses will take precedence<br>_if_ there is an ip_address configured for the node.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "svi_profiles.[].ip_virtual_router_addresses.[].&lt;str&gt;") | String |  |  |  | IPv4_address/Mask or IPv4_address<br>IPv4_address/Mask will also configure a static route to the SVI per best practice.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_virtual_router_addresses</samp>](## "svi_profiles.[].ipv6_virtual_router_addresses") | List, items: String |  |  |  | IPv6 VARP addresses.<br>Requires an IPv6 address to be configured on the SVI.<br>If ipv6_address_virtuals is also set, ipv6_virtual_router_addresses will take precedence<br>_if_ there is an ipv6_address configured for the node.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "svi_profiles.[].ipv6_virtual_router_addresses.[].&lt;str&gt;") | String |  |  |  | IPv6_address |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_helpers</samp>](## "svi_profiles.[].ip_helpers") | List, items: Dictionary |  |  |  | IP helper for DHCP relay |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- ip_helper</samp>](## "svi_profiles.[].ip_helpers.[].ip_helper") | String | Required, Unique |  |  | IPv4 DHCP server IP |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_interface</samp>](## "svi_profiles.[].ip_helpers.[].source_interface") | String |  |  |  | Interface name to originate DHCP relay packets to DHCP server. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_vrf</samp>](## "svi_profiles.[].ip_helpers.[].source_vrf") | String |  |  |  | VRF to originate DHCP relay packets to DHCP server. If not set, EOS uses the VRF on the SVI. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vni_override</samp>](## "svi_profiles.[].vni_override") | Integer |  |  | Min: 1<br>Max: 16777215 | By default the VNI will be derived from "mac_vrf_vni_base"<br>The vni_override allows us to override this value and statically define it (optional)<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;rt_override</samp>](## "svi_profiles.[].rt_override") | Integer |  |  | Min: 1<br>Max: 16777215 | By default the MAC VRF RD/RT ID will be derived from "mac_vrf_id_base"<br>The rt_override allows us to override this value and statically define it (optional)<br>If not set, vni_override will be used.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;tags</samp>](## "svi_profiles.[].tags") | List, items: String |  | ['all'] |  | Tags leveraged for networks services filtering<br>Tags are matched against "filter.tags" defined under Fabric Topology variables<br>Tags are also matched against the "node_group" name under Fabric Topology variables<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "svi_profiles.[].tags.[].&lt;str&gt;") | String |  |  |  | Tag value |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;trunk_groups</samp>](## "svi_profiles.[].trunk_groups") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "svi_profiles.[].trunk_groups.[].&lt;str&gt;") | String |  |  |  | Trunk groups are used for limiting vlans to trunk ports assigned to the same trunk group<br>Requires "enable_trunk_groups: true"<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;evpn_l2_multicast</samp>](## "svi_profiles.[].evpn_l2_multicast") | Dictionary |  |  |  | Explicitly enable or disable evpn_l2_multicast to override setting of `<network_services_key>.[].evpn_l2_multicast.enabled`.<br>When evpn_l2_multicast.enabled is set to true for a vlan or a tenant, "igmp snooping" and "igmp snooping querier" will always be enabled, overriding those individual settings.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "svi_profiles.[].evpn_l2_multicast.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;evpn_l3_multicast</samp>](## "svi_profiles.[].evpn_l3_multicast") | Dictionary |  |  |  | Explicitly enable or disable evpn_l3_multicast to override setting of `<network_services_key>.[].evpn_l3_multicast.enabled` and `<network_services_key>.[].vrfs.[].evpn_l3_multicast.enabled`.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "svi_profiles.[].evpn_l3_multicast.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;igmp_snooping_enabled</samp>](## "svi_profiles.[].igmp_snooping_enabled") | Boolean |  |  |  | Enable IGMP Snooping (Enabled by default on EOS) |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;igmp_snooping_querier</samp>](## "svi_profiles.[].igmp_snooping_querier") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "svi_profiles.[].igmp_snooping_querier.enabled") | Boolean |  |  |  | Will be enabled automatically if evpn_l2_multicast is enabled. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_address</samp>](## "svi_profiles.[].igmp_snooping_querier.source_address") | String |  |  |  | IPv4_address<br>If not set, IP address of "Loopback0" will be used.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;version</samp>](## "svi_profiles.[].igmp_snooping_querier.version") | Integer |  |  | Valid Values:<br>- 1<br>- 2<br>- 3 | IGMP Version (By default EOS uses IGMP version 2 for IGMP querier) |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vxlan</samp>](## "svi_profiles.[].vxlan") | Boolean |  | True |  | Extend this SVI over VXLAN |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mtu</samp>](## "svi_profiles.[].mtu") | Integer |  |  |  | Interface MTU |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ospf</samp>](## "svi_profiles.[].ospf") | Dictionary |  |  |  | OSPF interface configuration |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "svi_profiles.[].ospf.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;point_to_point</samp>](## "svi_profiles.[].ospf.point_to_point") | Boolean |  | True |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;area</samp>](## "svi_profiles.[].ospf.area") | String |  | 0 |  | OSPF area ID |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cost</samp>](## "svi_profiles.[].ospf.cost") | Integer |  |  |  | OSPF link cost |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;authentication</samp>](## "svi_profiles.[].ospf.authentication") | String |  |  | Valid Values:<br>- simple<br>- message-digest |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;simple_auth_key</samp>](## "svi_profiles.[].ospf.simple_auth_key") | String |  |  |  | Password used with simple authentication |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;message_digest_keys</samp>](## "svi_profiles.[].ospf.message_digest_keys") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- id</samp>](## "svi_profiles.[].ospf.message_digest_keys.[].id") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hash_algorithm</samp>](## "svi_profiles.[].ospf.message_digest_keys.[].hash_algorithm") | String |  | sha512 | Valid Values:<br>- md5<br>- sha1<br>- sha256<br>- sha384<br>- sha512 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key</samp>](## "svi_profiles.[].ospf.message_digest_keys.[].key") | String |  |  |  | Type 7 encrypted key |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;bgp</samp>](## "svi_profiles.[].bgp") | Dictionary |  |  |  | Structured configuration and EOS CLI commands rendered on router_bgp.vlans<br>This configuration will not be applied to vlan aware bundles<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "svi_profiles.[].bgp.structured_config") | Dictionary |  |  |  | Custom structured config added under vlan_interfaces.<interface> for eos_cli_config_gen.<br>Overrides the setting on SVI level.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "svi_profiles.[].bgp.raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the VLAN interface in the final EOS configuration<br>Overrides the setting on SVI level.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "svi_profiles.[].raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the VLAN interface in the final EOS configuration<br>Overrides the setting on SVI level<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "svi_profiles.[].structured_config") | Dictionary |  |  |  | Custom structured config added under vlan_interfaces.<interface> for eos_cli_config_gen.<br>Overrides the setting on SVI level. |

=== "YAML"

    ```yaml
    svi_profiles:
      - profile: <str>
        parent_profile: <str>
        nodes:
          - node: <str>
            name: <str>
            enabled: <bool>
            description: <str>
            ip_address: <str>
            ipv6_address: <str>
            ipv6_enable: <bool>
            ip_address_virtual: <str>
            ipv6_address_virtual: <str>
            ipv6_address_virtuals:
              - <str>
            ip_address_virtual_secondaries:
              - <str>
            ip_virtual_router_addresses:
              - <str>
            ipv6_virtual_router_addresses:
              - <str>
            ip_helpers:
              - ip_helper: <str>
                source_interface: <str>
                source_vrf: <str>
            vni_override: <int>
            rt_override: <int>
            tags:
              - <str>
            trunk_groups:
              - <str>
            evpn_l2_multicast:
              enabled: <bool>
            evpn_l3_multicast:
              enabled: <bool>
            igmp_snooping_enabled: <bool>
            igmp_snooping_querier:
              enabled: <bool>
              source_address: <str>
              version: <int>
            vxlan: <bool>
            mtu: <int>
            ospf:
              enabled: <bool>
              point_to_point: <bool>
              area: <str>
              cost: <int>
              authentication: <str>
              simple_auth_key: <str>
              message_digest_keys:
                - id: <int>
                  hash_algorithm: <str>
                  key: <str>
            bgp:
              structured_config: <dict>
              raw_eos_cli: <str>
            raw_eos_cli: <str>
            structured_config: <dict>
        name: <str>
        enabled: <bool>
        description: <str>
        ip_address: <str>
        ipv6_address: <str>
        ipv6_enable: <bool>
        ip_address_virtual: <str>
        ipv6_address_virtual: <str>
        ipv6_address_virtuals:
          - <str>
        ip_address_virtual_secondaries:
          - <str>
        ip_virtual_router_addresses:
          - <str>
        ipv6_virtual_router_addresses:
          - <str>
        ip_helpers:
          - ip_helper: <str>
            source_interface: <str>
            source_vrf: <str>
        vni_override: <int>
        rt_override: <int>
        tags:
          - <str>
        trunk_groups:
          - <str>
        evpn_l2_multicast:
          enabled: <bool>
        evpn_l3_multicast:
          enabled: <bool>
        igmp_snooping_enabled: <bool>
        igmp_snooping_querier:
          enabled: <bool>
          source_address: <str>
          version: <int>
        vxlan: <bool>
        mtu: <int>
        ospf:
          enabled: <bool>
          point_to_point: <bool>
          area: <str>
          cost: <int>
          authentication: <str>
          simple_auth_key: <str>
          message_digest_keys:
            - id: <int>
              hash_algorithm: <str>
              key: <str>
        bgp:
          structured_config: <dict>
          raw_eos_cli: <str>
        raw_eos_cli: <str>
        structured_config: <dict>
    ```

## System MAC Address

Set to the same MAC address as available in "show version" on the device.
"system_mac_address" can also be set under "Fabric Topology".
If both are set, the setting under "Fabric Topology" takes precedence.

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>system_mac_address</samp>](## "system_mac_address") | String |  |  |  |  |

=== "YAML"

    ```yaml
    system_mac_address: <str>
    ```

## TerminAttr Disable AAA

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>terminattr_disable_aaa</samp>](## "terminattr_disable_aaa") | Boolean |  | False |  |  |

=== "YAML"

    ```yaml
    terminattr_disable_aaa: <bool>
    ```

## TerminAttr Ingestexclude

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>terminattr_ingestexclude</samp>](## "terminattr_ingestexclude") | String |  | /Sysdb/cell/1/agent,/Sysdb/cell/2/agent |  |  |

=== "YAML"

    ```yaml
    terminattr_ingestexclude: <str>
    ```

## TerminAttr Ingestgrpcurl Port

Port number used for Terminattr connection to an on-premise CloudVision cluster.
The port number is always 443 when using CloudVision as a Service, so this value is ignored.

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>terminattr_ingestgrpcurl_port</samp>](## "terminattr_ingestgrpcurl_port") | Integer |  | 9910 |  |  |

=== "YAML"

    ```yaml
    terminattr_ingestgrpcurl_port: <int>
    ```

## TerminAttr Smashexcludes

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>terminattr_smashexcludes</samp>](## "terminattr_smashexcludes") | String |  | ale,flexCounter,hardware,kni,pulse,strata |  |  |

=== "YAML"

    ```yaml
    terminattr_smashexcludes: <str>
    ```

## Timezone

Clock timezone like "CET" or "US/Pacific".

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>timezone</samp>](## "timezone") | String |  |  |  |  |

=== "YAML"

    ```yaml
    timezone: <str>
    ```

## Trunk Groups

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>trunk_groups</samp>](## "trunk_groups") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;mlag</samp>](## "trunk_groups.mlag") | Dictionary |  |  |  | Trunk Group used for MLAG VLAN (Typically VLAN 4094)<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "trunk_groups.mlag.name") | String |  | MLAG |  |  |
    | [<samp>&nbsp;&nbsp;mlag_l3</samp>](## "trunk_groups.mlag_l3") | Dictionary |  |  |  | Trunk Group used for MLAG L3 peering VLAN and for VRF L3 peering VLANs (Typically VLAN 4093)<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "trunk_groups.mlag_l3.name") | String |  | LEAF_PEER_L3 |  |  |
    | [<samp>&nbsp;&nbsp;uplink</samp>](## "trunk_groups.uplink") | Dictionary |  |  |  | Trunk Group used on L2 Leaf switches when "enable_trunk_groups" is set<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "trunk_groups.uplink.name") | String |  | UPLINK |  |  |

=== "YAML"

    ```yaml
    trunk_groups:
      mlag:
        name: <str>
      mlag_l3:
        name: <str>
      uplink:
        name: <str>
    ```

## Type

The `type:` variable needs to be defined for each device in the fabric.
This is leveraged to load the appropriate template to generate the configuration.

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>type</samp>](## "type") | String |  |  | Valid Values:<br>- <value(s) of node_type_keys.type> |  |

=== "YAML"

    ```yaml
    type: <str>
    ```

## Underlay Filter Peer As

Configure route-map on eBGP sessions towards underlay peers, where prefixes with the peer's ASN in the AS Path are filtered away.
This is very useful in very large scale networks not using EVPN overlays, where convergence will be quicker by not having to return
all updates received from Spine-1 to Spine-2 just for Spine-2 to throw them away because of AS Path loop detection.
Note this key is ignored when EVPN is configured.

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>underlay_filter_peer_as</samp>](## "underlay_filter_peer_as") | Boolean |  | False |  |  |

=== "YAML"

    ```yaml
    underlay_filter_peer_as: <bool>
    ```

## Underlay Filter Redistribute Connected

Filter redistribution of connected into the underlay routing protocol.
Only applicable when overlay_routing_protocol != 'none' and underlay_routing_protocol == BGP.
Creates a route-map and prefix-list assigned to redistribute connected permitting only loopbacks and inband management subnets.

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>underlay_filter_redistribute_connected</samp>](## "underlay_filter_redistribute_connected") | Boolean |  | True |  |  |

=== "YAML"

    ```yaml
    underlay_filter_redistribute_connected: <bool>
    ```

## Underlay IPv6

This feature allows IPv6 underlay routing protocol with RFC5549 addresses to be used along with IPv4 advertisements as VXLAN tunnel endpoints.
Requires "underlay_rfc5549: true" and "loopback_ipv6_pool" under the "Fabric Topology"

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>underlay_ipv6</samp>](## "underlay_ipv6") | Boolean |  | False |  |  |

=== "YAML"

    ```yaml
    underlay_ipv6: <bool>
    ```

## Underlay ISIS Instance Name

Default -> "EVPN_UNDERLAY" for l3ls, "CORE" for mpls

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>underlay_isis_instance_name</samp>](## "underlay_isis_instance_name") | String |  |  |  |  |

=== "YAML"

    ```yaml
    underlay_isis_instance_name: <str>
    ```

## Underlay Multicast

Enable Multicast in the underlay on all p2p uplink interfaces and mlag l3 peer interface.
Specifically PIM Sparse-Mode will be configured on all routed underlay interfaces.
No other configuration is added, so the underlay will only support Source-Specific Multicast (SSM)
The configuration is intended to be used as multicast underlay for EVPN OISM overlay

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>underlay_multicast</samp>](## "underlay_multicast") | Boolean |  | False |  |  |

=== "YAML"

    ```yaml
    underlay_multicast: <bool>
    ```

## Underlay OSPF Area

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>underlay_ospf_area</samp>](## "underlay_ospf_area") | String |  | 0.0.0.0 | Format: ipv4 |  |

=== "YAML"

    ```yaml
    underlay_ospf_area: <str>
    ```

## Underlay OSPF BFD Enable

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>underlay_ospf_bfd_enable</samp>](## "underlay_ospf_bfd_enable") | Boolean |  | False |  |  |

=== "YAML"

    ```yaml
    underlay_ospf_bfd_enable: <bool>
    ```

## Underlay OSPF Max LSA

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>underlay_ospf_max_lsa</samp>](## "underlay_ospf_max_lsa") | Integer |  | 12000 |  |  |

=== "YAML"

    ```yaml
    underlay_ospf_max_lsa: <int>
    ```

## Underlay OSPF Process ID

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>underlay_ospf_process_id</samp>](## "underlay_ospf_process_id") | Integer |  | 100 |  |  |

=== "YAML"

    ```yaml
    underlay_ospf_process_id: <int>
    ```

## Underlay Rfc5549

Point to Point Underlay with RFC 5549(eBGP), i.e. IPv6 Unnumbered
Requires "underlay_routing_protocol: ebgp"

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>underlay_rfc5549</samp>](## "underlay_rfc5549") | Boolean |  | False |  |  |

=== "YAML"

    ```yaml
    underlay_rfc5549: <bool>
    ```

## Underlay Routing Protocol

- The following underlay routing protocols are supported:
  - EBGP (default for l3ls-evpn)
  - OSPF.
  - ISIS.
  - ISIS-SR*.
  - ISIS-LDP*.
  - ISIS-SR-LDP*.
  - OSPF-LDP*.
- The variables should be applied to all devices in the fabric.
*Only supported with core_interfaces data model.

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>underlay_routing_protocol</samp>](## "underlay_routing_protocol") | String |  |  | Value is converted to lower case<br>Valid Values:<br>- ebgp<br>- ospf<br>- isis<br>- isis-sr<br>- isis-ldp<br>- isis-sr-ldp<br>- ospf-ldp |  |

=== "YAML"

    ```yaml
    underlay_routing_protocol: <str>
    ```

## Uplink PTP

Enable PTP on all infrastructure links

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>uplink_ptp</samp>](## "uplink_ptp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;enable</samp>](## "uplink_ptp.enable") | Boolean |  | False |  |  |

=== "YAML"

    ```yaml
    uplink_ptp:
      enable: <bool>
    ```

## Vtep Vvtep IP

IP Address used as Virtual VTEP. Will be configured as secondary IP on Loopback1.
This is only needed for centralized routing designs.

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>vtep_vvtep_ip</samp>](## "vtep_vvtep_ip") | String |  |  |  |  |

=== "YAML"

    ```yaml
    vtep_vvtep_ip: <str>
    ```

## VxLAN VLAN Aware Bundles

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>vxlan_vlan_aware_bundles</samp>](## "vxlan_vlan_aware_bundles") <span style="color:red">removed</span> | Boolean |  | False |  | <span style="color:red">This key was removed. Support was removed in AVD version 4.0.0. Use <samp>evpn_vlan_aware_bundles</samp> instead.</span> |

=== "YAML"

    ```yaml
    ```
