<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>&lt;connected_endpoints_keys.key&gt;</samp>](## "&lt;connected_endpoints_keys.key&gt;") | List, items: Dictionary |  |  |  | This should be applied to group_vars or host_vars where endpoints are connecting.<br>`connected_endpoints_keys.key` is one of the keys under "connected_endpoints_keys".<br>The default keys are `servers`, `firewalls`, `routers`, `load_balancers`, and `storage_arrays`.<br> |
    | [<samp>&nbsp;&nbsp;- name</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].name") | String | Required, Unique |  |  | Endpoint name will be used in the switchport description. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;rack</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].rack") | String |  |  |  | Rack is used for documentation purposes only. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;adapters</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters") | List, items: Dictionary |  |  |  | A list of adapters, group by adapters leveraging the same port-profile. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- switch_ports</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].switch_ports") | List, items: String | Required |  |  | List of switch interfaces.<br>The lists `endpoint_ports`, `switch_ports`, and `switches` must have the same length.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].switch_ports.[].&lt;str&gt;") | String |  |  |  | Switchport interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;switches</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].switches") | List, items: String | Required |  |  | List of switches.<br>The lists `endpoint_ports`, `switch_ports`, and `switches` must have the same length.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].switches.[].&lt;str&gt;") | String |  |  |  | Device |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;endpoint_ports</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].endpoint_ports") | List, items: String |  |  |  | Endpoint ports is used for description, required unless description is set.<br>The lists `endpoint_ports`, `switch_ports`, and `switches` must have the same length.<br>Each list item is one switchport.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].endpoint_ports.[].&lt;str&gt;") | String |  |  |  | Interface name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;server_ports</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].server_ports") <span style="color:red">removed</span> | List, items: String |  |  |  | <span style="color:red">This key was removed. Support was removed in AVD version 4.0.0. Use <samp>endpoint_ports</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].server_ports.[].&lt;str&gt;") | String |  |  |  | Used for documentation purposes. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;speed</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].speed") | String |  |  |  | Set adapter speed: `< interface_speed >`, `forced < interface_speed >`, `auto < interface_speed >`.<br>If not specified will be auto.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].description") | String |  |  |  | By default the description is built leveraging `<peer>_<peer_interface>`.<br>When set this key will overide the default value on the physical ports.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;profile</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].profile") | String |  |  |  | Port-profile name to inherit configuration. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].enabled") | Boolean |  | `True` |  | Administrative state, setting to false will set the port to 'shutdown' in the intended configuration.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].mode") | String |  |  | Valid Values:<br>- access<br>- dot1q-tunnel<br>- trunk<br>- trunk phone | Interface mode. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mtu</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].mtu") | Integer |  |  | Min: 68<br>Max: 65535 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;l2_mtu</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].l2_mtu") | Integer |  |  | Min: 68<br>Max: 9416 | This should only be defined for platforms supporting the "l2 mtu" CLI command. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;native_vlan</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].native_vlan") | Integer |  |  | Min: 1<br>Max: 4094 | Native VLAN for a trunk port.<br>If both `native_vlan` and `native_vlan_tag`, `native_vlan_tag` takes precedence.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;native_vlan_tag</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].native_vlan_tag") | Boolean |  | `False` |  | If both `native_vlan` and `native_vlan_tag`, `native_vlan_tag` takes precedence. |
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
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].ptp.enabled") | Boolean |  | `False` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;endpoint_role</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].ptp.endpoint_role") | String |  | `follower` | Valid Values:<br>- bmca<br>- default<br>- follower |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;profile</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].ptp.profile") | String |  | `aes67-r16-2016` | Valid Values:<br>- aes67<br>- aes67-r16-2016<br>- smpte2059-2 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sflow</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].sflow") | Boolean |  |  |  | Configures sFlow on the interface. Overrides `fabric_sflow` setting.<br> |
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
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;poe</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].poe") | Dictionary |  |  |  | Power Over Ethernet settings applied on port. Only configured if platform supports PoE. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;disabled</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].poe.disabled") | Boolean |  | `False` |  | Disable PoE on a POE capable port. PoE is enabled on all ports that support it by default in EOS. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].poe.priority") | String |  |  | Valid Values:<br>- critical<br>- high<br>- medium<br>- low | Prioritize a port's power in the event that one of the switch's power supplies loses power |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;reboot</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].poe.reboot") | Dictionary |  |  |  | Set the PoE power behavior for a PoE port when the system is rebooted |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].poe.reboot.action") | String |  |  | Valid Values:<br>- maintain<br>- power-off | PoE action for interface |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;link_down</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].poe.link_down") | Dictionary |  |  |  | Set the PoE power behavior for a PoE port when the port goes down |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].poe.link_down.action") | String |  |  | Valid Values:<br>- maintain<br>- power-off | PoE action for interface |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;power_off_delay</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].poe.link_down.power_off_delay") | Integer |  |  | Min: 1<br>Max: 86400 | Number of seconds to delay shutting the power off after a link down event occurs. Default value is 5 seconds in EOS. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;shutdown</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].poe.shutdown") | Dictionary |  |  |  | Set the PoE power behavior for a PoE port when the port is admin down |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].poe.shutdown.action") | String |  |  | Valid Values:<br>- maintain<br>- power-off | PoE action for interface |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;limit</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].poe.limit") | Dictionary |  |  |  | Override the hardware-negotiated power limit using either wattage or a power class. Note that if using a power class, AVD will automatically convert the class value to the wattage value corresponding to that power class. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;class</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].poe.limit.class") | Integer |  |  | Min: 0<br>Max: 8 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;watts</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].poe.limit.watts") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;fixed</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].poe.limit.fixed") | Boolean |  |  |  | Set to ignore hardware classification |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;negotiation_lldp</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].poe.negotiation_lldp") | Boolean |  |  |  | Disable to prevent port from negotiating power with powered devices over LLDP. Enabled by default in EOS. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;legacy_detect</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].poe.legacy_detect") | Boolean |  |  |  | Allow a subset of legacy devices to work with the PoE switch. Disabled by default in EOS because it can cause false positive detections. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;storm_control</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].storm_control") | Dictionary |  |  |  | Storm control settings applied on port toward the endpoint. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;all</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].storm_control.all") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;level</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].storm_control.all.level") | String |  |  |  | Configure maximum storm-control level. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unit</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].storm_control.all.unit") | String |  | `percent` | Valid Values:<br>- percent<br>- pps | Optional variable and is hardware dependent. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;broadcast</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].storm_control.broadcast") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;level</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].storm_control.broadcast.level") | String |  |  |  | Configure maximum storm-control level. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unit</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].storm_control.broadcast.unit") | String |  | `percent` | Valid Values:<br>- percent<br>- pps | Optional variable and is hardware dependent. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;multicast</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].storm_control.multicast") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;level</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].storm_control.multicast.level") | String |  |  |  | Configure maximum storm-control level. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unit</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].storm_control.multicast.unit") | String |  | `percent` | Valid Values:<br>- percent<br>- pps | Optional variable and is hardware dependent. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unknown_unicast</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].storm_control.unknown_unicast") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;level</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].storm_control.unknown_unicast.level") | String |  |  |  | Configure maximum storm-control level. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unit</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].storm_control.unknown_unicast.unit") | String |  | `percent` | Valid Values:<br>- percent<br>- pps | Optional variable and is hardware dependent. |
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
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].port_channel.enabled") | Boolean |  | `True` |  | Port-Channel administrative state.<br>Setting to false will set port to 'shutdown' in intended configuration.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;esi</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].port_channel.esi") <span style="color:red">removed</span> | String |  |  |  | Format xxxx:xxxx:xxxx.<span style="color:red">This key was removed. Support was removed in AVD version 4.0.0. Use <samp>short_esi</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;short_esi</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].port_channel.short_esi") <span style="color:red">deprecated</span> | String |  |  |  | In format xxxx:xxxx:xxxx or "auto".<span style="color:red">This key is deprecated. Support will be removed in AVD version 5.0.0. Use <samp>ethernet_segment.short_esi</samp> instead.</span> |
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
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].port_channel.structured_config") | Dictionary |  |  |  | Custom structured config added under port_channel_interfaces.[name=<interface>] for eos_cli_config_gen. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the ethernet interface in the final EOS configuration. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].structured_config") | Dictionary |  |  |  | Custom structured config added under ethernet_interfaces.[name=<interface>] for eos_cli_config_gen. |

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
