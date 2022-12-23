!!! warning
    This document describes the data model for AVD 4.x. It may or may not work in previous versions.

## BFD Multihop

### Description

BFD Multihop tuning
### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>bfd_multihop</samp>](## "bfd_multihop") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;interval</samp>](## "bfd_multihop.interval") | Integer |  | 300 |  |  |
| [<samp>&nbsp;&nbsp;min_rx</samp>](## "bfd_multihop.min_rx") | Integer |  | 300 |  |  |
| [<samp>&nbsp;&nbsp;multiplier</samp>](## "bfd_multihop.multiplier") | Integer |  | 3 |  |  |

### YAML

```yaml
bfd_multihop:
  interval: <int>
  min_rx: <int>
  multiplier: <int>
```

## BGP As

### Description

AS number to use to configure overlay when "overlay_routing_protocol" == IBGP
### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>bgp_as</samp>](## "bgp_as") | String |  |  |  |  |

### YAML

```yaml
bgp_as: <str>
```

## BGP Ecmp

### Description

Maximum ECMP for BGP multi-path
### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>bgp_ecmp</samp>](## "bgp_ecmp") | Integer |  | 4 |  |  |

### YAML

```yaml
bgp_ecmp: <int>
```

## BGP Maximum Paths

### Description

Maximum Paths for BGP multi-path
### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>bgp_maximum_paths</samp>](## "bgp_maximum_paths") | Integer |  | 4 |  |  |

### YAML

```yaml
bgp_maximum_paths: <int>
```

## BGP Mesh Pes

### Description

Whether to configure an iBGP full mesh between PEs, either because there is no RR used or other reasons.
### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>bgp_mesh_pes</samp>](## "bgp_mesh_pes") | Boolean |  | False |  |  |

### YAML

```yaml
bgp_mesh_pes: <bool>
```

## BGP Peer Groups

### Description

Leverage an Arista EOS switch to generate the encrypted password using the correct peer group name.
Note that the name of the peer groups use '-' instead of '_' in EOS configuration.

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>bgp_peer_groups</samp>](## "bgp_peer_groups") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;EVPN_OVERLAY_PEERS</samp>](## "bgp_peer_groups.EVPN_OVERLAY_PEERS") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "bgp_peer_groups.EVPN_OVERLAY_PEERS.name") | String |  | EVPN-OVERLAY-PEERS |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;password</samp>](## "bgp_peer_groups.EVPN_OVERLAY_PEERS.password") | String |  |  |  | Encrypted Password |
| [<samp>&nbsp;&nbsp;IPv4_UNDERLAY_PEERS</samp>](## "bgp_peer_groups.IPv4_UNDERLAY_PEERS") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "bgp_peer_groups.IPv4_UNDERLAY_PEERS.name") | String |  | IPv4-UNDERLAY-PEERS |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;password</samp>](## "bgp_peer_groups.IPv4_UNDERLAY_PEERS.password") | String |  |  |  | Encrypted Password |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "bgp_peer_groups.IPv4_UNDERLAY_PEERS.structured_config") | Dictionary |  |  |  | Custom structured config added under router_bgp.peer_groups.<name> for eos_cli_config_gen |
| [<samp>&nbsp;&nbsp;MLAG_IPv4_UNDERLAY_PEER</samp>](## "bgp_peer_groups.MLAG_IPv4_UNDERLAY_PEER") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "bgp_peer_groups.MLAG_IPv4_UNDERLAY_PEER.name") | String |  | MLAG-IPv4-UNDERLAY-PEER |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;password</samp>](## "bgp_peer_groups.MLAG_IPv4_UNDERLAY_PEER.password") | String |  |  |  | Encrypted Password |
| [<samp>&nbsp;&nbsp;evpn_overlay_core</samp>](## "bgp_peer_groups.evpn_overlay_core") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "bgp_peer_groups.evpn_overlay_core.name") | String |  | EVPN-OVERLAY-CORE |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;password</samp>](## "bgp_peer_groups.evpn_overlay_core.password") | String |  |  |  | Encrypted Password |
| [<samp>&nbsp;&nbsp;evpn_overlay_peers</samp>](## "bgp_peer_groups.evpn_overlay_peers") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "bgp_peer_groups.evpn_overlay_peers.name") | String |  | EVPN-OVERLAY-PEERS |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;password</samp>](## "bgp_peer_groups.evpn_overlay_peers.password") | String |  |  |  | Encrypted Password |
| [<samp>&nbsp;&nbsp;ipv4_underlay_peers</samp>](## "bgp_peer_groups.ipv4_underlay_peers") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "bgp_peer_groups.ipv4_underlay_peers.name") | String |  | IPv4-UNDERLAY-PEERS |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;password</samp>](## "bgp_peer_groups.ipv4_underlay_peers.password") | String |  |  |  | Encrypted Password |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "bgp_peer_groups.ipv4_underlay_peers.structured_config") | Dictionary |  |  |  | Custom structured config added under router_bgp.peer_groups.<name> for eos_cli_config_gen |
| [<samp>&nbsp;&nbsp;mlag_ipv4_underlay_peer</samp>](## "bgp_peer_groups.mlag_ipv4_underlay_peer") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "bgp_peer_groups.mlag_ipv4_underlay_peer.name") | String |  | MLAG-IPv4-UNDERLAY-PEER |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;password</samp>](## "bgp_peer_groups.mlag_ipv4_underlay_peer.password") | String |  |  |  | Encrypted Password |

### YAML

```yaml
bgp_peer_groups:
  EVPN_OVERLAY_PEERS:
    name: <str>
    password: <str>
  IPv4_UNDERLAY_PEERS:
    name: <str>
    password: <str>
    structured_config:
  MLAG_IPv4_UNDERLAY_PEER:
    name: <str>
    password: <str>
  evpn_overlay_core:
    name: <str>
    password: <str>
  evpn_overlay_peers:
    name: <str>
    password: <str>
  ipv4_underlay_peers:
    name: <str>
    password: <str>
    structured_config:
  mlag_ipv4_underlay_peer:
    name: <str>
    password: <str>
```

## Connected Endpoints

### Description

This should be applied to group_vars or host_vars where endpoints are connecting.
<connected_endpoints_keys.key> is one of the keys under "connected_endpoints_keys"
Default keys are "servers", "firewalls", "routers", "load_balancers" and "storage_arrays".

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>connected_endpoints</samp>](## "connected_endpoints") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;- adapters</samp>](## "connected_endpoints.[].adapters") | List, items: Dictionary |  |  |  | A list of adapter(s), group by adapters leveraging the same port-profile. |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- description</samp>](## "connected_endpoints.[].adapters.[].description") | String |  |  |  | Interface descriptions Description. |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dot1x</samp>](## "connected_endpoints.[].adapters.[].dot1x") | Dictionary |  |  |  | 802.1x |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;authentication_failure</samp>](## "connected_endpoints.[].adapters.[].dot1x.authentication_failure") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "connected_endpoints.[].adapters.[].dot1x.authentication_failure.action") | String |  |  | Valid Values:<br>- allow<br>- drop |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;allow_vlan</samp>](## "connected_endpoints.[].adapters.[].dot1x.authentication_failure.allow_vlan") | Integer |  |  | Min: 1<br>Max: 4094 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;host_mode</samp>](## "connected_endpoints.[].adapters.[].dot1x.host_mode") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "connected_endpoints.[].adapters.[].dot1x.host_mode.mode") | String |  |  | Valid Values:<br>- multi-host<br>- single-host |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;multi_host_authenticated</samp>](## "connected_endpoints.[].adapters.[].dot1x.host_mode.multi_host_authenticated") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mac_based_authentication</samp>](## "connected_endpoints.[].adapters.[].dot1x.mac_based_authentication") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;always</samp>](## "connected_endpoints.[].adapters.[].dot1x.mac_based_authentication.always") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "connected_endpoints.[].adapters.[].dot1x.mac_based_authentication.enabled") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;host_mode_common</samp>](## "connected_endpoints.[].adapters.[].dot1x.mac_based_authentication.host_mode_common") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pae</samp>](## "connected_endpoints.[].adapters.[].dot1x.pae") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "connected_endpoints.[].adapters.[].dot1x.pae.mode") | String |  |  | Valid Values:<br>- authenticator |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;port_control</samp>](## "connected_endpoints.[].adapters.[].dot1x.port_control") | String |  |  | Valid Values:<br>- auto<br>- force-authorized<br>- force-unauthorized |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;port_control_force_authorized_phone</samp>](## "connected_endpoints.[].adapters.[].dot1x.port_control_force_authorized_phone") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;reauthentication</samp>](## "connected_endpoints.[].adapters.[].dot1x.reauthentication") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;reauthorization_request_limit</samp>](## "connected_endpoints.[].adapters.[].dot1x.reauthorization_request_limit") | Integer |  |  | Min: 1<br>Max: 10 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;timeout</samp>](## "connected_endpoints.[].adapters.[].dot1x.timeout") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;idle_host</samp>](## "connected_endpoints.[].adapters.[].dot1x.timeout.idle_host") | Integer |  |  | Min: 10<br>Max: 65535 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;quiet_period</samp>](## "connected_endpoints.[].adapters.[].dot1x.timeout.quiet_period") | Integer |  |  | Min: 1<br>Max: 65535 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;reauth_period</samp>](## "connected_endpoints.[].adapters.[].dot1x.timeout.reauth_period") | String |  |  |  | Range 60-4294967295 or "server" |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;reauth_timeout_ignore</samp>](## "connected_endpoints.[].adapters.[].dot1x.timeout.reauth_timeout_ignore") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tx_period</samp>](## "connected_endpoints.[].adapters.[].dot1x.timeout.tx_period") | Integer |  |  | Min: 1<br>Max: 65535 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "connected_endpoints.[].adapters.[].enabled") | Boolean |  | True |  | Administrative state, setting to false will set port to 'shutdown' in intended configuration<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;endpoint_ports</samp>](## "connected_endpoints.[].adapters.[].endpoint_ports") | List, items: String |  |  |  | The lists "endpoint_ports", "switch_ports" and "switches" must have the same length.<br>Each list item is one switchport.<br>Endpoint port(s) is used for description, required unless description is set.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "connected_endpoints.[].adapters.[].endpoint_ports.[].&lt;str&gt;") | String |  |  |  | Interface name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ethernet_segment</samp>](## "connected_endpoints.[].adapters.[].ethernet_segment") | Dictionary |  |  |  | Settings for all- or single-active EVPN multihoming |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;designated_forwarder_algorithm</samp>](## "connected_endpoints.[].adapters.[].ethernet_segment.designated_forwarder_algorithm") | String |  |  | Valid Values:<br>- auto<br>- modulus<br>- preference | Configure DF algorithm and preferences<br>- auto: Use preference-based algorithm and assign preference based on position of device in the 'switches' list<br>   e.g. assuming a list of three switches, this would assign a preference of 200 to the first switch, 100 to the 2nd and 0 to the third<br>- preference: Set preference for each switch manually using designated_forwarder_preferences key<br>- modulus: Use the default modulus-based algorithm<br>If omitted, Port-Channels use the EOS default of modulus<br>If omitted, Ethernet interfaces default to the 'auto' mechanism detailed above<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;designated_forwarder_preferences</samp>](## "connected_endpoints.[].adapters.[].ethernet_segment.designated_forwarder_preferences") | List, items: String |  |  |  | Manual preference as described above, required only for preference algorithm |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "connected_endpoints.[].adapters.[].ethernet_segment.designated_forwarder_preferences.[].&lt;str&gt;") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dont_preempt</samp>](## "connected_endpoints.[].adapters.[].ethernet_segment.dont_preempt") | Boolean |  |  |  | Disable preemption for single-active forwarding when auto/manual DF preference is configured. |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;redundancy</samp>](## "connected_endpoints.[].adapters.[].ethernet_segment.redundancy") | String |  |  | Valid Values:<br>- all-active<br>- single-active | If omitted, Port-Channels use the EOS default of all-active<br>If omitted, Ethernet interfaces are configured as single-active<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;short_esi</samp>](## "connected_endpoints.[].adapters.[].ethernet_segment.short_esi") | String | Required |  |  | In format xxxx:xxxx:xxxx or "auto"<br>Define a manual short-esi (be careful using this on profiles) or auto-generate an ESI<br>Please see the notes under "EVPN A/A ESI dual- and single-attached endpoint scenarios" before setting short_esi: auto<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;flowcontrol</samp>](## "connected_endpoints.[].adapters.[].flowcontrol") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;received</samp>](## "connected_endpoints.[].adapters.[].flowcontrol.received") | String |  |  | Valid Values:<br>- received<br>- send<br>- on |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;l2_mtu</samp>](## "connected_endpoints.[].adapters.[].l2_mtu") | Integer |  |  |  | This should only be defined for platforms supporting the "l2 mtu" CLI |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;link_tracking</samp>](## "connected_endpoints.[].adapters.[].link_tracking") | Dictionary |  |  |  | Configure the downstream interfaces of a respective Link Tracking Group<br>If port_channel is defined in an adapter then port-channel interface is configured to be the downstream<br>else all the ethernet-interfaces will be configured as downstream -> to configure single-active EVPN multihomed networks<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "connected_endpoints.[].adapters.[].link_tracking.enabled") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "connected_endpoints.[].adapters.[].link_tracking.name") | String |  |  |  | Tracking group name<br>The default group name is taken from fabric variable of the switch, link_tracking.groups[0].name with default value being "LT_GROUP1".<br>Optional if default link_tracking settings are configured on the node.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "connected_endpoints.[].adapters.[].mode") | String |  |  | Valid Values:<br>- access<br>- dot1q-tunnel<br>- trunk | Interface mode |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;monitor_sessions</samp>](## "connected_endpoints.[].adapters.[].monitor_sessions") | List, items: Dictionary |  |  |  | Monitor Session configuration - Use defined switchports as source or destination for monitoring sessions |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "connected_endpoints.[].adapters.[].monitor_sessions.[].name") | String | Required |  |  | Session name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;role</samp>](## "connected_endpoints.[].adapters.[].monitor_sessions.[].role") | String |  |  | Valid Values:<br>- source<br>- destination |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;session_settings</samp>](## "connected_endpoints.[].adapters.[].monitor_sessions.[].session_settings") | Dictionary |  |  |  | Session settings are defined per session name. Different session_settings with for same session name will be combined/merged |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_group</samp>](## "connected_endpoints.[].adapters.[].monitor_sessions.[].session_settings.access_group") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "connected_endpoints.[].adapters.[].monitor_sessions.[].session_settings.access_group.name") | String |  |  |  | ACL Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "connected_endpoints.[].adapters.[].monitor_sessions.[].session_settings.access_group.type") | String |  |  | Valid Values:<br>- ip<br>- ipv6<br>- mac |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;encapsulation_gre_metadata_tx</samp>](## "connected_endpoints.[].adapters.[].monitor_sessions.[].session_settings.encapsulation_gre_metadata_tx") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;header_remove_size</samp>](## "connected_endpoints.[].adapters.[].monitor_sessions.[].session_settings.header_remove_size") | Integer |  |  |  | Number of bytes to remove from header |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rate_limit_per_egress_chip</samp>](## "connected_endpoints.[].adapters.[].monitor_sessions.[].session_settings.rate_limit_per_egress_chip") | String |  |  |  | Ratelimit and unit as string.<br>Examples:<br>  "100000 bps"<br>  "100 kbps"<br>  "10 mbps"<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rate_limit_per_ingress_chip</samp>](## "connected_endpoints.[].adapters.[].monitor_sessions.[].session_settings.rate_limit_per_ingress_chip") | String |  |  |  | Ratelimit and unit as string.<br>Examples:<br>  "100000 bps"<br>  "100 kbps"<br>  "10 mbps"<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sample</samp>](## "connected_endpoints.[].adapters.[].monitor_sessions.[].session_settings.sample") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;truncate</samp>](## "connected_endpoints.[].adapters.[].monitor_sessions.[].session_settings.truncate") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "connected_endpoints.[].adapters.[].monitor_sessions.[].session_settings.truncate.enabled") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;size</samp>](## "connected_endpoints.[].adapters.[].monitor_sessions.[].session_settings.truncate.size") | Integer |  |  |  | Size in bytes |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_settings</samp>](## "connected_endpoints.[].adapters.[].monitor_sessions.[].source_settings") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_group</samp>](## "connected_endpoints.[].adapters.[].monitor_sessions.[].source_settings.access_group") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "connected_endpoints.[].adapters.[].monitor_sessions.[].source_settings.access_group.name") | String |  |  |  | ACL Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority</samp>](## "connected_endpoints.[].adapters.[].monitor_sessions.[].source_settings.access_group.priority") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "connected_endpoints.[].adapters.[].monitor_sessions.[].source_settings.access_group.type") | String |  |  | Valid Values:<br>- ip<br>- ipv6<br>- mac |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction</samp>](## "connected_endpoints.[].adapters.[].monitor_sessions.[].source_settings.direction") | String |  |  | Valid Values:<br>- rx<br>- tx<br>- both |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mtu</samp>](## "connected_endpoints.[].adapters.[].mtu") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;native_vlan</samp>](## "connected_endpoints.[].adapters.[].native_vlan") | Integer |  |  |  | Native VLAN for a trunk port<br>If setting both native_vlan and native_vlan_tag, native_vlan_tag takes precedence<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;native_vlan_tag</samp>](## "connected_endpoints.[].adapters.[].native_vlan_tag") | Boolean |  | False |  | If setting both native_vlan and native_vlan_tag, native_vlan_tag takes precedence |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;port_channel</samp>](## "connected_endpoints.[].adapters.[].port_channel") | Dictionary |  |  |  | Used for port-channel adapter |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;channel_id</samp>](## "connected_endpoints.[].adapters.[].port_channel.channel_id") | Integer |  |  |  | Port-Channel ID, Optional<br>If no channel_id is specified, an id is generated from the first switch port in the port channel<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "connected_endpoints.[].adapters.[].port_channel.description") | String |  |  |  | Port-Channel Description - added after endpoint name in the description, Optional |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "connected_endpoints.[].adapters.[].port_channel.enabled") | Boolean |  | True |  | Port-Channel administrative state, Optional<br>setting to false will set port to 'shutdown' in intended configuration<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;esi</samp>](## "connected_endpoints.[].adapters.[].port_channel.esi") | String |  |  |  | Format xxxx:xxxx:xxxx |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;lacp_fallback</samp>](## "connected_endpoints.[].adapters.[].port_channel.lacp_fallback") | Dictionary |  |  |  | LACP Fallback configuration |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "connected_endpoints.[].adapters.[].port_channel.lacp_fallback.mode") | String |  |  | Valid Values:<br>- static | Currently only static mode is supported |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;timeout</samp>](## "connected_endpoints.[].adapters.[].port_channel.lacp_fallback.timeout") | Integer |  |  |  | Timeout in seconds, Optional - default is 90 seconds |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "connected_endpoints.[].adapters.[].port_channel.mode") | String | Required |  | Valid Values:<br>- active<br>- passive<br>- on | Port-Channel Mode |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;short_esi</samp>](## "connected_endpoints.[].adapters.[].port_channel.short_esi") | String |  |  |  | In format xxxx:xxxx:xxxx or "auto" |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;subinterfaces</samp>](## "connected_endpoints.[].adapters.[].port_channel.subinterfaces") | List, items: Dictionary |  |  |  | Port-Channel L2 Subinterfaces<br>Subinterfaces are only supported on routed port-channels, which means they cannot be configured on MLAG port-channels.<br>Setting short_esi: auto generates the short_esi automatically using a hash of configuration elements.<br>Please see the notes under "EVPN A/A ESI dual-attached endpoint scenario" before setting short_esi: auto.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- encapsulation_vlan</samp>](## "connected_endpoints.[].adapters.[].port_channel.subinterfaces.[].encapsulation_vlan") | Dictionary |  |  |  | Client vlan id encapsulation<br>Default is subinterface number<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;client_dot1q</samp>](## "connected_endpoints.[].adapters.[].port_channel.subinterfaces.[].encapsulation_vlan.client_dot1q") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;number</samp>](## "connected_endpoints.[].adapters.[].port_channel.subinterfaces.[].number") | Integer |  |  |  | Subinterface number |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;short_esi</samp>](## "connected_endpoints.[].adapters.[].port_channel.subinterfaces.[].short_esi") | String |  |  |  | In format xxxx:xxxx:xxxx or "auto"<br>Required for multihomed port-channels with subinterfaces<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vlan_id</samp>](## "connected_endpoints.[].adapters.[].port_channel.subinterfaces.[].vlan_id") | Integer |  |  |  | VLAN ID to bridge<br>Default is subinterface number<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;profile</samp>](## "connected_endpoints.[].adapters.[].profile") | String |  |  |  | Port-profile name, to inherit configuration. |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ptp</samp>](## "connected_endpoints.[].adapters.[].ptp") | Dictionary |  |  |  | PTP Enable |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enable</samp>](## "connected_endpoints.[].adapters.[].ptp.enable") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;qos_profile</samp>](## "connected_endpoints.[].adapters.[].qos_profile") | String |  |  |  | QOS profile name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "connected_endpoints.[].adapters.[].raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the ethernet interface in the final EOS configuration |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;server_ports</samp>](## "connected_endpoints.[].adapters.[].server_ports") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "connected_endpoints.[].adapters.[].server_ports.[].&lt;str&gt;") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;short_esi</samp>](## "connected_endpoints.[].adapters.[].short_esi") | String |  |  | Valid Values:<br>- auto | Allocates an automatic short_esi to all ports using this profile<br>Please see the notes under "EVPN A/A ESI dual-attached endpoint examples" in this document before setting short_esi: auto.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_bpdufilter</samp>](## "connected_endpoints.[].adapters.[].spanning_tree_bpdufilter") | String |  |  | Valid Values:<br>- enabled<br>- disabled<br>- True<br>- False |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_bpduguard</samp>](## "connected_endpoints.[].adapters.[].spanning_tree_bpduguard") | String |  |  | Valid Values:<br>- enabled<br>- disabled<br>- True<br>- False |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_portfast</samp>](## "connected_endpoints.[].adapters.[].spanning_tree_portfast") | String |  |  | Valid Values:<br>- edge<br>- network |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;speed</samp>](## "connected_endpoints.[].adapters.[].speed") | String |  |  |  | < interface_speed or forced interface_speed or auto interface_speed ><br>Adapter speed - if not specified will be auto.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;storm_control</samp>](## "connected_endpoints.[].adapters.[].storm_control") | Dictionary |  |  |  | Storm control settings applied on port toward the endpoint |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;all</samp>](## "connected_endpoints.[].adapters.[].storm_control.all") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;level</samp>](## "connected_endpoints.[].adapters.[].storm_control.all.level") | Integer |  |  |  | Configure maximum storm-control level |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unit</samp>](## "connected_endpoints.[].adapters.[].storm_control.all.unit") | String |  | percent | Valid Values:<br>- percent<br>- pps | Optional var and is hardware dependent |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;broadcast</samp>](## "connected_endpoints.[].adapters.[].storm_control.broadcast") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;level</samp>](## "connected_endpoints.[].adapters.[].storm_control.broadcast.level") | Integer |  |  |  | Configure maximum storm-control level |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unit</samp>](## "connected_endpoints.[].adapters.[].storm_control.broadcast.unit") | String |  | percent | Valid Values:<br>- percent<br>- pps | Optional var and is hardware dependent |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;multicast</samp>](## "connected_endpoints.[].adapters.[].storm_control.multicast") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;level</samp>](## "connected_endpoints.[].adapters.[].storm_control.multicast.level") | Integer |  |  |  | Configure maximum storm-control level |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unit</samp>](## "connected_endpoints.[].adapters.[].storm_control.multicast.unit") | String |  | percent | Valid Values:<br>- percent<br>- pps | Optional var and is hardware dependent |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unknown_unicast</samp>](## "connected_endpoints.[].adapters.[].storm_control.unknown_unicast") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;level</samp>](## "connected_endpoints.[].adapters.[].storm_control.unknown_unicast.level") | Integer |  |  |  | Configure maximum storm-control level |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unit</samp>](## "connected_endpoints.[].adapters.[].storm_control.unknown_unicast.unit") | String |  | percent | Valid Values:<br>- percent<br>- pps | Optional var and is hardware dependent |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;switch_ports</samp>](## "connected_endpoints.[].adapters.[].switch_ports") | List, items: String |  |  |  | List of switch interfac(es) |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "connected_endpoints.[].adapters.[].switch_ports.[].&lt;str&gt;") | String |  |  |  | Switchport interface |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;switches</samp>](## "connected_endpoints.[].adapters.[].switches") | List, items: String |  |  |  | List of switch(es) |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "connected_endpoints.[].adapters.[].switches.[].&lt;str&gt;") | String |  |  |  | Device |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;trunk_groups</samp>](## "connected_endpoints.[].adapters.[].trunk_groups") | List, items: String |  |  |  | Required with "enable_trunk_groups: true"<br>Trunk Groups are used for limiting vlans on trunk ports to vlans with the same Trunk Group<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "connected_endpoints.[].adapters.[].trunk_groups.[].&lt;str&gt;") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vlans</samp>](## "connected_endpoints.[].adapters.[].vlans") | String |  |  |  | Interface vlans - if not set, the EOS default is that all vlans are allowed for trunk ports and vlan 1 will be used for access ports. |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "connected_endpoints.[].name") | String | Required, Unique |  |  | Endpoint name, this will be used in the switchport description. |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;rack</samp>](## "connected_endpoints.[].rack") | String |  |  |  | Rack is used for documentation purposes only |

### YAML

```yaml
connected_endpoints:
  - adapters:
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
    name: <str>
    rack: <str>
```

## Connected Endpoints Keys

### Description

Define connected endpoints keys, to define grouping of endpoints connecting to the fabric.
This provides the ability to define various keys of your choice to better organize/group your data.
This should be defined in top level group_var for the fabric.

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>connected_endpoints_keys</samp>](## "connected_endpoints_keys") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;- key</samp>](## "connected_endpoints_keys.[].key") | String | Required, Unique |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "connected_endpoints_keys.[].type") | String |  |  |  | Type used for documentation |

### YAML

```yaml
connected_endpoints_keys:
  - key: <str>
    type: <str>
```

## Core Interfaces

### Description

The `core_interfaces` data model can be used to configure L3 P2P links anywhere in the fabric.
It can be between two switches that are already part of the fabric inventory, or it can be towards another device,
where only one end of the link is on a switch in the fabric.

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>core_interfaces</samp>](## "core_interfaces") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;p2p_links</samp>](## "core_interfaces.p2p_links") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- as</samp>](## "core_interfaces.p2p_links.[].as") | List, items: String |  |  |  | AS Numbers for BGP or Required with bgp peering |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "core_interfaces.p2p_links.[].as.[].&lt;str&gt;") | String |  |  |  | The values can be like ["node_a_as", "node_b_as"] |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bfd</samp>](## "core_interfaces.p2p_links.[].bfd") | Boolean |  | False |  | Enable BFD (only considered for BGP). |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;id</samp>](## "core_interfaces.p2p_links.[].id") | Integer |  |  |  | Unique id per subnet_summary. Used to calculate ip addresses or Required with ip_pool.<br>ID starting from 1<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_in_underlay_protocol</samp>](## "core_interfaces.p2p_links.[].include_in_underlay_protocol") | Boolean |  | True |  | Add this interface to underlay routing protocol. |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interfaces</samp>](## "core_interfaces.p2p_links.[].interfaces") | List, items: String |  |  |  | Interfaces where this link should be configured and Required unless using port-channels |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "core_interfaces.p2p_links.[].interfaces.[].&lt;str&gt;") | String |  |  |  | The value can be like < node_a_interface >, < node_b_interface ><br>ex. - [ Ethernet2, Ethernet2 ]<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip</samp>](## "core_interfaces.p2p_links.[].ip") | List, items: String |  |  |  | Specific IP addresses used on this P2P link |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "core_interfaces.p2p_links.[].ip.[].&lt;str&gt;") | String |  |  |  | Node IPv4 address/Mask |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_pool</samp>](## "core_interfaces.p2p_links.[].ip_pool") | String |  |  |  | P2P pool name. IP Pool defined under p2p_links_ip_pools. A /31 will be taken from the pool per P2P link |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_enable</samp>](## "core_interfaces.p2p_links.[].ipv6_enable") | Boolean |  | False |  | Allows turning on ipv6 for the link or profile (also autodetected based on underlay_rfc5549 and include_in_underlay_protocol) |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_authentication_key</samp>](## "core_interfaces.p2p_links.[].isis_authentication_key") | String |  |  |  | type-7 encrypted password |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_authentication_mode</samp>](## "core_interfaces.p2p_links.[].isis_authentication_mode") | String |  |  | Valid Values:<br>- md5<br>- text |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_circuit_type</samp>](## "core_interfaces.p2p_links.[].isis_circuit_type") | String |  |  | Valid Values:<br>- level-1<br>- level-2<br>- level-1-2 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_hello_padding</samp>](## "core_interfaces.p2p_links.[].isis_hello_padding") | Boolean |  | False |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_metric</samp>](## "core_interfaces.p2p_links.[].isis_metric") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;macsec_profile</samp>](## "core_interfaces.p2p_links.[].macsec_profile") | String |  |  |  | MAC security profile |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mpls_ip</samp>](## "core_interfaces.p2p_links.[].mpls_ip") | Boolean |  |  |  | MPLS parameters. Default value is true if switch.mpls_lsr is true |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mpls_ldp</samp>](## "core_interfaces.p2p_links.[].mpls_ldp") | Boolean |  |  |  | MPLS parameters. Default value is true for ldp underlay variants, otherwise false |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mtu</samp>](## "core_interfaces.p2p_links.[].mtu") | Integer |  |  |  | MTU for this P2P link. Default value same as p2p_uplinks_mtu. |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "core_interfaces.p2p_links.[].nodes") | List, items: String | Required |  |  | Nodes where this link should be configured |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "core_interfaces.p2p_links.[].nodes.[].&lt;str&gt;") | String |  |  |  | The values can be < node_a >, < node_b ><br>ex.- [ core-1-isis-sr-ldp, core-2-ospf-ldp ]<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;port_channel</samp>](## "core_interfaces.p2p_links.[].port_channel") | Dictionary |  |  |  | Port-channel parameters |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "core_interfaces.p2p_links.[].port_channel.mode") | String |  | active |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes_child_interfaces</samp>](## "core_interfaces.p2p_links.[].port_channel.nodes_child_interfaces") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- interfaces</samp>](## "core_interfaces.p2p_links.[].port_channel.nodes_child_interfaces.[].interfaces") | List, items: String |  |  |  | List of node interfaces. Ex.- [ 'node1 interface1', 'node1 interface2' ] |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "core_interfaces.p2p_links.[].port_channel.nodes_child_interfaces.[].interfaces.[].&lt;str&gt;") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;node</samp>](## "core_interfaces.p2p_links.[].port_channel.nodes_child_interfaces.[].node") | String | Required, Unique |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;profile</samp>](## "core_interfaces.p2p_links.[].profile") | String |  |  |  | P2P profile name. Profile defined under p2p_profiles |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ptp_enable</samp>](## "core_interfaces.p2p_links.[].ptp_enable") | Boolean |  | False |  | Enable PTP |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;qos_profile</samp>](## "core_interfaces.p2p_links.[].qos_profile") | String |  |  |  | QOS service profile |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "core_interfaces.p2p_links.[].raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the point-to-point interface in the final EOS configuration. |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;speed</samp>](## "core_interfaces.p2p_links.[].speed") | String |  |  |  | The values can be speed or auto speed or forced speed |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;subnet</samp>](## "core_interfaces.p2p_links.[].subnet") | String |  |  |  | IPv4 address/Mask. Subnet used on this P2P link (Optional) |
| [<samp>&nbsp;&nbsp;p2p_links_ip_pools</samp>](## "core_interfaces.p2p_links_ip_pools") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- ipv4_pool</samp>](## "core_interfaces.p2p_links_ip_pools.[].ipv4_pool") | String |  |  |  | IPv4 address/Mask |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "core_interfaces.p2p_links_ip_pools.[].name") | String |  |  |  | P2P pool name |
| [<samp>&nbsp;&nbsp;p2p_links_profiles</samp>](## "core_interfaces.p2p_links_profiles") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- ip_pool</samp>](## "core_interfaces.p2p_links_profiles.[].ip_pool") | String |  |  |  | P2P pool name. IP Pool defined under p2p_links_ip_pools. A /31 will be taken from the pool per P2P link |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_enable</samp>](## "core_interfaces.p2p_links_profiles.[].ipv6_enable") | Boolean |  | False |  | Allows turning on ipv6 for the link or profile (also autodetected based on underlay_rfc5549 and include_in_underlay_protocol) |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_authentication_key</samp>](## "core_interfaces.p2p_links_profiles.[].isis_authentication_key") | String |  | $1c$sTNAlR6rKSw= |  | IS-IS parameters |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_authentication_mode</samp>](## "core_interfaces.p2p_links_profiles.[].isis_authentication_mode") | String |  | md5 |  | IS-IS parameters |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_circuit_type</samp>](## "core_interfaces.p2p_links_profiles.[].isis_circuit_type") | String |  | level-2 |  | IS-IS parameters |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_hello_padding</samp>](## "core_interfaces.p2p_links_profiles.[].isis_hello_padding") | Boolean |  | False |  | IS-IS parameters |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_metric</samp>](## "core_interfaces.p2p_links_profiles.[].isis_metric") | Integer |  | 60 |  | IS-IS parameters |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mtu</samp>](## "core_interfaces.p2p_links_profiles.[].mtu") | Integer |  |  |  | MTU for this P2P link. Default value same as p2p_uplinks_mtu. |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "core_interfaces.p2p_links_profiles.[].name") | String |  |  |  | P2P profile name. Any variable supported under p2p_links can be inherited from a profile. |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;speed</samp>](## "core_interfaces.p2p_links_profiles.[].speed") | String |  |  |  | The values can be speed or auto speed or forced speed |

### YAML

```yaml
core_interfaces:
  p2p_links:
    - as:
        - <str>
      bfd: <bool>
      id: <int>
      include_in_underlay_protocol: <bool>
      interfaces:
        - <str>
      ip:
        - <str>
      ip_pool: <str>
      ipv6_enable: <bool>
      isis_authentication_key: <str>
      isis_authentication_mode: <str>
      isis_circuit_type: <str>
      isis_hello_padding: <bool>
      isis_metric: <int>
      macsec_profile: <str>
      mpls_ip: <bool>
      mpls_ldp: <bool>
      mtu: <int>
      nodes:
        - <str>
      port_channel:
        mode: <str>
        nodes_child_interfaces:
          - interfaces:
              - <str>
            node: <str>
      profile: <str>
      ptp_enable: <bool>
      qos_profile: <str>
      raw_eos_cli: <str>
      speed: <str>
      subnet: <str>
  p2p_links_ip_pools:
    - ipv4_pool: <str>
      name: <str>
  p2p_links_profiles:
    - ip_pool: <str>
      ipv6_enable: <bool>
      isis_authentication_key: <str>
      isis_authentication_mode: <str>
      isis_circuit_type: <str>
      isis_hello_padding: <bool>
      isis_metric: <int>
      mtu: <int>
      name: <str>
      speed: <str>
```

## Custom Structured Configuration List Merge

### Description

The List-merge strategy can be changed using `custom_structured_configuration_list_merge` variable using any value accepted by `list_merge` on the Ansible Combine filter.

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>custom_structured_configuration_list_merge</samp>](## "custom_structured_configuration_list_merge") | String |  | replace | Valid Values:<br>- replace<br>- append<br>- keep<br>- prepend<br>- append_rp<br>- prepend_rp |  |

### YAML

```yaml
custom_structured_configuration_list_merge: <str>
```

## Custom Structured Configuration Prefix

### Description

Custom EOS Structured Configuration keys can be set on any group or host_var level using the name
of the corresponding `eos_cli_config_gen` key prefixed with content of `custom_structured_configuration_prefix`.
The content of Custom Structured Configuration variables will be combined with the structured config generated by the eos_designs role.
By default Lists are replaced and Dictionaries are updated. The combine is done recursively, so it is possible to update a sub-key of a variable set by
`eos_designs` role already.

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>custom_structured_configuration_prefix</samp>](## "custom_structured_configuration_prefix") | List, items: String |  | ['custom_structured_configuration_'] |  |  |
| [<samp>&nbsp;&nbsp;- &lt;str&gt;</samp>](## "custom_structured_configuration_prefix.[].&lt;str&gt;") | String |  |  |  |  |

### YAML

```yaml
custom_structured_configuration_prefix:
  - <str>
```

## CVP Ingestauth Key

### Description

CloudVision ingest authentication key is required for on-prem CVP
### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>cvp_ingestauth_key</samp>](## "cvp_ingestauth_key") | String |  |  |  |  |

### YAML

```yaml
cvp_ingestauth_key: <str>
```

## CVP Instance IP

### Description

IPv4 address.
CloudVision - Telemetry Agent (TerminAttr) configuration is optional
You can either provide a list of IPs to target on-premise CloudVision cluster or
use DNS name for your CloudVision as a Service instance. If you have both on-prem and
CVaaS defined, only on-prem is going to be configured.
### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>cvp_instance_ip</samp>](## "cvp_instance_ip") | String |  |  |  |  |

### YAML

```yaml
cvp_instance_ip: <str>
```

## CVP Instance Ips

### Description

You can either provide a list of IPs to target on-premise CloudVision cluster or
use DNS name for your CloudVision as a Service instance. If you have both on-prem and
CVaaS defined, only on-prem is going to be configured.

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>cvp_instance_ips</samp>](## "cvp_instance_ips") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;- &lt;str&gt;</samp>](## "cvp_instance_ips.[].&lt;str&gt;") | String |  |  |  | IPv4 address or CV as a Service hostname |

### YAML

```yaml
cvp_instance_ips:
  - <str>
```

## CVP Token File

### Description

CVP token file is path to token file on switch and is only applicable to CV as a Service
### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>cvp_token_file</samp>](## "cvp_token_file") | String |  | /tmp/cv-onboarding-token |  |  |

### YAML

```yaml
cvp_token_file: <str>
```

## DC Name

### Description

Optional DC Name, only used in SNMP location and Fabric Documentation.
Recommended to be common between all devices within a Site

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>dc_name</samp>](## "dc_name") | String |  |  |  |  |

### YAML

```yaml
dc_name: <str>
```

## Default IGMP Snooping Enabled

### Description

Disable IGMP snooping at fabric level.
If set, it overrides per vlan settings

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>default_igmp_snooping_enabled</samp>](## "default_igmp_snooping_enabled") | Boolean |  | True |  |  |

### YAML

```yaml
default_igmp_snooping_enabled: <bool>
```

## Default Interfaces

### Description

- Set default uplink, downlink and mlag interfaces which will be used if these interfaces are not defined on a device (either directly or through inheritance).
- These are defined based on the combination of node_type (e.g. l3leaf or spine) and a regex for matching the platform.
- A list of interfaces or interface ranges can be specified.
- Each list item supports range syntax that can be expanded into a list of interfaces. Interface range examples:
  - Ethernet49-52/1: Expands to [ Ethernet49/1, Ethernet50/1, Ethernet51/1, Ethernet52/1 ]
  - Ethernet1/31-34/1: Expands to [ Ethernet1/31/1, Ethernet1/32/1, Ethernet1/33/1, Ethernet1/34/1 ]
  - Ethernet49-50,53-54: Expands to [ Ethernet49, Ethernet50, Ethernet53, Ethernet54 ]
  - Ethernet1-2/1-4: Expands to [ Ethernet1/1, Ethernet1/2, Ethernet1/3, Ethernet1/4, Ethernet2/1, Ethernet2/2, Ethernet2/3, Ethernet2/4 ]
- `uplink_interfaces` and `mlag_interfaces` under `default_interfaces` are directly inherited by `uplink_interfaces` and `mlag_interfaces`.
- `downlink_interfaces` are referenced by the child switch (e.g. the leaf in a leaf/spine network). Essentially the child switch indexes into an upstream switch's `default_downlink_interfaces` using the child switch ID.  This is then used to build `uplink_switch_interfaces` for that child.
  - In the case of `max_parallel_uplinks` > 1 the `default_downlink_interfaces` are mapped with consecutive downlinks per child ID.
  - Example for `max_parallel_uplinks: 2`, downlink interfaces will be mapped as `[ <downlink1 to leaf-id1>, <downlink2 to leaf-id1>, <downlink1 to leaf-id2>, <downlink2 to leaf-id2> ...]`
- Please note that no default interfaces are defined in AVD itself. You will need to create your own based on the example below.

Example:

```yaml
- types: [ spine, l3leaf ]
  platforms: [ "7050[SC]X3", vEOS.*, default ]
  uplink_interfaces: [ Ethernet49-54/1 ]
  mlag_interfaces: [ Ethernet55-56/1 ]
  downlink_interfaces: [ Ethernet1-32/1 ]
```

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>default_interfaces</samp>](## "default_interfaces") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;- downlink_interfaces</samp>](## "default_interfaces.[].downlink_interfaces") | List, items: String | Required |  |  | List of downlink interfaces or downlink interface ranges |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "default_interfaces.[].downlink_interfaces.[].&lt;str&gt;") | String |  |  |  | Interface range or interface |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mlag_interfaces</samp>](## "default_interfaces.[].mlag_interfaces") | List, items: String | Required |  |  | List of MLAG interfaces or MLAG interface ranges |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "default_interfaces.[].mlag_interfaces.[].&lt;str&gt;") | String |  |  |  | Interface range or interface |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;platforms</samp>](## "default_interfaces.[].platforms") | List, items: String | Required |  |  | List of platform families<br>This is defined as a Python regular expression that matches the full platform type<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "default_interfaces.[].platforms.[].&lt;str&gt;") | String |  |  |  | Arista platform family regular expression |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;types</samp>](## "default_interfaces.[].types") | List, items: String | Required |  |  | List of node type keys |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "default_interfaces.[].types.[].&lt;str&gt;") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;uplink_interfaces</samp>](## "default_interfaces.[].uplink_interfaces") | List, items: String | Required |  |  | List of uplink interfaces or uplink interface ranges |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "default_interfaces.[].uplink_interfaces.[].&lt;str&gt;") | String |  |  |  | Interface range or interface |

### YAML

```yaml
default_interfaces:
  - downlink_interfaces:
      - <str>
    mlag_interfaces:
      - <str>
    platforms:
      - <str>
    types:
      - <str>
    uplink_interfaces:
      - <str>
```

## Default Node Types

### Description

Uses hostname matches against a regular expression to determine the node type.
### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>default_node_types</samp>](## "default_node_types") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;- match_hostnames</samp>](## "default_node_types.[].match_hostnames") | List, items: String | Required |  |  | Regular expressions to match against hostnames |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "default_node_types.[].match_hostnames.[].&lt;str&gt;") | String | Required |  |  | Regex needs to match full hostname (i.e. is bounded by ^ and $ elements) |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;node_type</samp>](## "default_node_types.[].node_type") | String | Required, Unique |  |  | Resulting node type when regex matches |

### YAML

```yaml
default_node_types:
  - match_hostnames:
      - <str>
    node_type: <str>
```

## Design

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>design</samp>](## "design") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;type</samp>](## "design.type") | String |  | l3ls-evpn | Valid Values:<br>- l3ls-evpn<br>- mpls | By setting the `design.type` to `mpls`,<br>the default node-types and templates described in these documents will be used.<br> |

### YAML

```yaml
design:
  type: <str>
```

## Enable Trunk Groups

### Description

Enable Trunk Group support across eos_designs
Warning: Because of the nature of the EOS Trunk Group feature, enabling this is "all or nothing".
*All* vlans and *all* trunks towards connected endpoints must be using trunk groups as well.
If trunk groups are not assigned to a trunk, no vlans will be enabled on that trunk.
See "Details on enable_trunk_groups" below before enabling this feature

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>enable_trunk_groups</samp>](## "enable_trunk_groups") | Boolean |  | False |  |  |

### YAML

```yaml
enable_trunk_groups: <bool>
```

## Event Handlers

### Description

Gives ability to monitor and react to Syslog messages provides a powerful and flexible tool that can be used to apply self-healing actions,
customize the system behavior, and implement workarounds to problems discovered in the field.

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>event_handlers</samp>](## "event_handlers") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;- action</samp>](## "event_handlers.[].action") | String |  |  |  | Command to run when handler is triggered |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;action_type</samp>](## "event_handlers.[].action_type") | String |  |  | Valid Values:<br>- bash<br>- increment |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;asynchronous</samp>](## "event_handlers.[].asynchronous") | Boolean |  | False |  | Set the action to be non-blocking. |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;delay</samp>](## "event_handlers.[].delay") | Integer |  |  |  | Event-handler delay in seconds |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "event_handlers.[].name") | String | Required, Unique |  |  | Event handler name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;regex</samp>](## "event_handlers.[].regex") | String |  |  |  | Regular expression to use for searching log messages. Required for on-logging trigger |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;trigger</samp>](## "event_handlers.[].trigger") | String |  |  | Valid Values:<br>- on-logging | Configure event trigger condition. |

### YAML

```yaml
event_handlers:
  - action: <str>
    action_type: <str>
    asynchronous: <bool>
    delay: <int>
    name: <str>
    regex: <str>
    trigger: <str>
```

## EVPN Ebgp Gateway Multihop

### Description

Default of 15, considering a large value to avoid BGP reachability issues in very complex DCI networks.
Adapt the value for your specific topology.

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>evpn_ebgp_gateway_multihop</samp>](## "evpn_ebgp_gateway_multihop") | Integer |  | 15 |  |  |

### YAML

```yaml
evpn_ebgp_gateway_multihop: <int>
```

## EVPN Ebgp Multihop

### Description

Default of 3, the recommended value for a 3 stage spine and leaf topology.
Set to a higher value to allow for very large and complex topologies.

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>evpn_ebgp_multihop</samp>](## "evpn_ebgp_multihop") | Integer |  | 3 |  |  |

### YAML

```yaml
evpn_ebgp_multihop: <int>
```

## EVPN Hostflap Detection

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>evpn_hostflap_detection</samp>](## "evpn_hostflap_detection") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;enabled</samp>](## "evpn_hostflap_detection.enabled") | Boolean |  | True |  | If set to false it will disable EVPN host-flap detection |
| [<samp>&nbsp;&nbsp;expiry_timeout</samp>](## "evpn_hostflap_detection.expiry_timeout") | Integer |  |  |  | Time (in seconds) to purge a MAC duplication issue |
| [<samp>&nbsp;&nbsp;threshold</samp>](## "evpn_hostflap_detection.threshold") | Integer |  | 5 |  | Minimum number of MAC moves that indicate a MAC duplication issue |
| [<samp>&nbsp;&nbsp;window</samp>](## "evpn_hostflap_detection.window") | Integer |  | 180 |  | Time (in seconds) to detect a MAC duplication issue |

### YAML

```yaml
evpn_hostflap_detection:
  enabled: <bool>
  expiry_timeout: <int>
  threshold: <int>
  window: <int>
```

## EVPN Import Pruning

### Description

Enable VPN import pruning (Min. EOS 4.24.2F)
The Route Target extended communities carried by incoming VPN paths will
be examined. If none of those Route Targets have been configured for import,
the path will be immediately discarded

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>evpn_import_pruning</samp>](## "evpn_import_pruning") | Boolean |  | False |  |  |

### YAML

```yaml
evpn_import_pruning: <bool>
```

## EVPN Multicast

### Description

General Configuration required for EVPN Multicast. "evpn_l2_multicast" must also be configured under the Network Services (tenants).
Requires "underlay_multicast: true" and IGMP snooping enabled globally (default).
For MLAG devices Route Distinguisher must be unique since this feature will create multi-vtep configuration.
Warning !!! For Trident3 based platforms i.e 7050X3, 7300X3, 720XP and 722XP
  The Following default platform setting will be configured: "platform trident forwarding-table partition flexible exact-match 16384 l2-shared 98304 l3-shared 131072"
  All forwarding agents will be restarted when this configuration is applied.
  You can tune the settings by overridding the default variable: "platform_settings[platforms].trident_forwarding_table_partition:"
  Please contact an Arista representative for help with determining the appropriate values for your environment.

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>evpn_multicast</samp>](## "evpn_multicast") | Boolean |  | False |  |  |

### YAML

```yaml
evpn_multicast: <bool>
```

## EVPN Overlay BGP Rtc

### Description

Enable Route Target Membership Constraint Address Family on EVPN overlay BGP peerings (Min. EOS 4.25.1F)
Requires use eBGP as overlay protocol.

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>evpn_overlay_bgp_rtc</samp>](## "evpn_overlay_bgp_rtc") | Boolean |  | False |  |  |

### YAML

```yaml
evpn_overlay_bgp_rtc: <bool>
```

## EVPN Prevent Readvertise To Server

### Description

Configure route-map on eBGP sessions towards route-servers, where prefixes with the peer's ASN in the AS Path are filtered away.
This is very useful in very large scale networks, where convergence will be quicker by not having to return all updates received
from Route-server-1 to Router-server-2 just for Route-server-2 to throw them away because of AS Path loop detection.

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>evpn_prevent_readvertise_to_server</samp>](## "evpn_prevent_readvertise_to_server") | Boolean |  | False |  |  |

### YAML

```yaml
evpn_prevent_readvertise_to_server: <bool>
```

## EVPN Short Esi Prefix

### Description

Configure prefix for "short_esi" values
### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>evpn_short_esi_prefix</samp>](## "evpn_short_esi_prefix") | String |  | 0000:0000: |  |  |

### YAML

```yaml
evpn_short_esi_prefix: <str>
```

## EVPN VLAN Aware Bundles

### Description

Enable vlan aware bundles for EVPN MAC-VRF
Old variable name vxlan_vlan_aware_bundles, supported for backward-compatibility.

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>evpn_vlan_aware_bundles</samp>](## "evpn_vlan_aware_bundles") | Boolean |  | False |  |  |

### YAML

```yaml
evpn_vlan_aware_bundles: <bool>
```

## Fabric Name

### Description

Fabric Name, required to match Ansible Group name covering all devices in the Fabric, **must** be an inventory group name.
### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>fabric_name</samp>](## "fabric_name") | String | Required |  |  |  |

### YAML

```yaml
fabric_name: <str>
```

## Inband Management Subnet

### Description

Optional IP subnet assigned to Inband Management SVI on l2leafs in default VRF.
Parent l3leafs will have SVI with "ip virtual-router" and host-route injection based on ARP. This allows all l3leafs to reuse the same subnet
SVI IP address will be assigned as follows:
virtual-router: <subnet> + 1
l3leaf A      : <subnet> + 2 (same IP on all l3leaf A)
l3leaf B      : <subnet> + 3 (same IP on all l3leaf B)
l2leafs       : <subnet> + 3 + <l2leaf id>
GW on l2leafs : <subnet> + 1
Assign range larger than total l2leafs + 5
### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>inband_management_subnet</samp>](## "inband_management_subnet") | String |  |  |  |  |

### YAML

```yaml
inband_management_subnet: <str>
```

## Inband Management VLAN

### Description

VLAN number assigned to Inband Management SVI on l2leafs in default VRF.

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>inband_management_vlan</samp>](## "inband_management_vlan") | Integer |  | 4092 |  |  |

### YAML

```yaml
inband_management_vlan: <int>
```

## Internal VLAN Order

### Description

Internal vlan allocation order and range
### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>internal_vlan_order</samp>](## "internal_vlan_order") | Dictionary | Required |  |  |  |
| [<samp>&nbsp;&nbsp;allocation</samp>](## "internal_vlan_order.allocation") | String |  | ascending | Valid Values:<br>- ascending<br>- descending |  |
| [<samp>&nbsp;&nbsp;range</samp>](## "internal_vlan_order.range") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;beginning</samp>](## "internal_vlan_order.range.beginning") | Integer |  | 1006 |  | VLAN ID |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ending</samp>](## "internal_vlan_order.range.ending") | Integer |  | 1199 |  | VLAN ID |

### YAML

```yaml
internal_vlan_order:
  allocation: <str>
  range:
    beginning: <int>
    ending: <int>
```

## ISIS Advertise Passive Only

### Description

Additional underlay ISIS parameters
### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>isis_advertise_passive_only</samp>](## "isis_advertise_passive_only") | Boolean |  | False |  |  |

### YAML

```yaml
isis_advertise_passive_only: <bool>
```

## ISIS Area ID

### Description

Required when "underlay_routing_protocol" == ISIS variants
### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>isis_area_id</samp>](## "isis_area_id") | String |  | 49.0001 |  |  |

### YAML

```yaml
isis_area_id: <str>
```

## ISIS Default Circuit Type

### Description

Fabric vevel variables. These fabric level parameters can be used with core_interfaces running ISIS,
and may be overridden on link profile or link level.
### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>isis_default_circuit_type</samp>](## "isis_default_circuit_type") | String |  | level-2 | Valid Values:<br>- level-1-2<br>- level-1<br>- level-2 |  |

### YAML

```yaml
isis_default_circuit_type: <str>
```

## ISIS Default IS Type

### Description

Additional underlay ISIS parameters
### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>isis_default_is_type</samp>](## "isis_default_is_type") | String |  | level-2 | Valid Values:<br>- level-1-2<br>- level-1<br>- level-2 |  |

### YAML

```yaml
isis_default_is_type: <str>
```

## ISIS Default Metric

### Description

Fabric level variables. These fabric level parameters can be used with core_interfaces running ISIS,
and may be overridden on link profile or link level.
### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>isis_default_metric</samp>](## "isis_default_metric") | Integer |  | 50 |  |  |

### YAML

```yaml
isis_default_metric: <int>
```

## ISIS TI LFA

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>isis_ti_lfa</samp>](## "isis_ti_lfa") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;enabled</samp>](## "isis_ti_lfa.enabled") | Boolean |  | False |  |  |
| [<samp>&nbsp;&nbsp;local_convergence_delay</samp>](## "isis_ti_lfa.local_convergence_delay") | Integer |  | 10000 |  | Local convergence delay in mpls |
| [<samp>&nbsp;&nbsp;protection</samp>](## "isis_ti_lfa.protection") | String |  |  | Valid Values:<br>- link<br>- node |  |

### YAML

```yaml
isis_ti_lfa:
  enabled: <bool>
  local_convergence_delay: <int>
  protection: <str>
```

## L3 Edge

### Description

The `l3_edge` data model can be used to configure extra L3 P2P links anywhere in the fabric. It can be between two switches that are already part of the fabric inventory, or it can be towards another device, where only one end of the link is on a switch in the fabric. Fabric switches can be types `l3leaf`, `spine` or `super-spine`.

The data model supports using IP pools, Subnet per link or specifying the IP addresses manually.
For BGP peerings the AS number must be specified. If the AS number is different than the AS number configured for the node, the local-as will be replaced on this BGP peering (`neighbor <ip> local-as <as> no-prepend replace-as`).

Make sure to configure the variables in a group_vars file covering all devices mentioned in the data model.

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>l3_edge</samp>](## "l3_edge") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;p2p_links</samp>](## "l3_edge.p2p_links") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- as</samp>](## "l3_edge.p2p_links.[].as") | List, items: String |  |  |  | AS Numbers for BGP or Required with bgp peering |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "l3_edge.p2p_links.[].as.[].&lt;str&gt;") | String |  |  |  | The values can be like ["node_a_as", "node_b_as"] |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bfd</samp>](## "l3_edge.p2p_links.[].bfd") | Boolean |  | False |  | Enable BFD (only considered for BGP). |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;id</samp>](## "l3_edge.p2p_links.[].id") | Integer |  |  |  | Unique id per subnet_summary. Used to calculate ip addresses or Required with ip_pool.<br>ID starting from 1<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_in_underlay_protocol</samp>](## "l3_edge.p2p_links.[].include_in_underlay_protocol") | Boolean |  | True |  | Add this interface to underlay routing protocol. |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interfaces</samp>](## "l3_edge.p2p_links.[].interfaces") | List, items: String |  |  |  | Interfaces where this link should be configured and Required unless using port-channels |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "l3_edge.p2p_links.[].interfaces.[].&lt;str&gt;") | String |  |  |  | The value can be like < node_a_interface >, < node_b_interface ><br>ex. - [ Ethernet2, Ethernet2 ]<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip</samp>](## "l3_edge.p2p_links.[].ip") | List, items: String |  |  |  | Specific IP addresses used on this P2P link |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "l3_edge.p2p_links.[].ip.[].&lt;str&gt;") | String |  |  |  | Node IPv4 address/Mask |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_pool</samp>](## "l3_edge.p2p_links.[].ip_pool") | String |  |  |  | P2P pool name. IP Pool defined under p2p_links_ip_pools. A /31 will be taken from the pool per P2P link |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_enable</samp>](## "l3_edge.p2p_links.[].ipv6_enable") | Boolean |  | False |  | Allows turning on ipv6 for the link or profile (also autodetected based on underlay_rfc5549 and include_in_underlay_protocol) |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_authentication_key</samp>](## "l3_edge.p2p_links.[].isis_authentication_key") | String |  |  |  | type-7 encrypted password |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_authentication_mode</samp>](## "l3_edge.p2p_links.[].isis_authentication_mode") | String |  |  | Valid Values:<br>- md5<br>- text |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_circuit_type</samp>](## "l3_edge.p2p_links.[].isis_circuit_type") | String |  |  | Valid Values:<br>- level-1<br>- level-2<br>- level-1-2 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_hello_padding</samp>](## "l3_edge.p2p_links.[].isis_hello_padding") | Boolean |  | False |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_metric</samp>](## "l3_edge.p2p_links.[].isis_metric") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;macsec_profile</samp>](## "l3_edge.p2p_links.[].macsec_profile") | String |  |  |  | MAC security profile |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mpls_ip</samp>](## "l3_edge.p2p_links.[].mpls_ip") | Boolean |  |  |  | MPLS parameters. Default value is true if switch.mpls_lsr is true |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mpls_ldp</samp>](## "l3_edge.p2p_links.[].mpls_ldp") | Boolean |  |  |  | MPLS parameters. Default value is true for ldp underlay variants, otherwise false |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mtu</samp>](## "l3_edge.p2p_links.[].mtu") | Integer |  |  |  | MTU for this P2P link. Default value same as p2p_uplinks_mtu. |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "l3_edge.p2p_links.[].nodes") | List, items: String | Required |  |  | Nodes where this link should be configured |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "l3_edge.p2p_links.[].nodes.[].&lt;str&gt;") | String |  |  |  | The values can be < node_a >, < node_b ><br>ex.- [ core-1-isis-sr-ldp, core-2-ospf-ldp ]<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;port_channel</samp>](## "l3_edge.p2p_links.[].port_channel") | Dictionary |  |  |  | Port-channel parameters |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "l3_edge.p2p_links.[].port_channel.mode") | String |  | active |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes_child_interfaces</samp>](## "l3_edge.p2p_links.[].port_channel.nodes_child_interfaces") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- interfaces</samp>](## "l3_edge.p2p_links.[].port_channel.nodes_child_interfaces.[].interfaces") | List, items: String |  |  |  | List of node interfaces. Ex.- [ 'node1 interface1', 'node1 interface2' ] |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "l3_edge.p2p_links.[].port_channel.nodes_child_interfaces.[].interfaces.[].&lt;str&gt;") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;node</samp>](## "l3_edge.p2p_links.[].port_channel.nodes_child_interfaces.[].node") | String | Required, Unique |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;profile</samp>](## "l3_edge.p2p_links.[].profile") | String |  |  |  | P2P profile name. Profile defined under p2p_profiles |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ptp_enable</samp>](## "l3_edge.p2p_links.[].ptp_enable") | Boolean |  | False |  | Enable PTP |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;qos_profile</samp>](## "l3_edge.p2p_links.[].qos_profile") | String |  |  |  | QOS service profile |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "l3_edge.p2p_links.[].raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the point-to-point interface in the final EOS configuration. |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;speed</samp>](## "l3_edge.p2p_links.[].speed") | String |  |  |  | The values can be speed or auto speed or forced speed |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;subnet</samp>](## "l3_edge.p2p_links.[].subnet") | String |  |  |  | IPv4 address/Mask. Subnet used on this P2P link (Optional) |
| [<samp>&nbsp;&nbsp;p2p_links_ip_pools</samp>](## "l3_edge.p2p_links_ip_pools") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- ipv4_pool</samp>](## "l3_edge.p2p_links_ip_pools.[].ipv4_pool") | String |  |  |  | IPv4 address/Mask |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "l3_edge.p2p_links_ip_pools.[].name") | String |  |  |  | P2P pool name |
| [<samp>&nbsp;&nbsp;p2p_links_profiles</samp>](## "l3_edge.p2p_links_profiles") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- ip_pool</samp>](## "l3_edge.p2p_links_profiles.[].ip_pool") | String |  |  |  | P2P pool name. IP Pool defined under p2p_links_ip_pools. A /31 will be taken from the pool per P2P link |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_enable</samp>](## "l3_edge.p2p_links_profiles.[].ipv6_enable") | Boolean |  | False |  | Allows turning on ipv6 for the link or profile (also autodetected based on underlay_rfc5549 and include_in_underlay_protocol) |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_authentication_key</samp>](## "l3_edge.p2p_links_profiles.[].isis_authentication_key") | String |  | $1c$sTNAlR6rKSw= |  | IS-IS parameters |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_authentication_mode</samp>](## "l3_edge.p2p_links_profiles.[].isis_authentication_mode") | String |  | md5 |  | IS-IS parameters |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_circuit_type</samp>](## "l3_edge.p2p_links_profiles.[].isis_circuit_type") | String |  | level-2 |  | IS-IS parameters |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_hello_padding</samp>](## "l3_edge.p2p_links_profiles.[].isis_hello_padding") | Boolean |  | False |  | IS-IS parameters |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_metric</samp>](## "l3_edge.p2p_links_profiles.[].isis_metric") | Integer |  | 60 |  | IS-IS parameters |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mtu</samp>](## "l3_edge.p2p_links_profiles.[].mtu") | Integer |  |  |  | MTU for this P2P link. Default value same as p2p_uplinks_mtu. |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "l3_edge.p2p_links_profiles.[].name") | String |  |  |  | P2P profile name. Any variable supported under p2p_links can be inherited from a profile. |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;speed</samp>](## "l3_edge.p2p_links_profiles.[].speed") | String |  |  |  | The values can be speed or auto speed or forced speed |

### YAML

```yaml
l3_edge:
  p2p_links:
    - as:
        - <str>
      bfd: <bool>
      id: <int>
      include_in_underlay_protocol: <bool>
      interfaces:
        - <str>
      ip:
        - <str>
      ip_pool: <str>
      ipv6_enable: <bool>
      isis_authentication_key: <str>
      isis_authentication_mode: <str>
      isis_circuit_type: <str>
      isis_hello_padding: <bool>
      isis_metric: <int>
      macsec_profile: <str>
      mpls_ip: <bool>
      mpls_ldp: <bool>
      mtu: <int>
      nodes:
        - <str>
      port_channel:
        mode: <str>
        nodes_child_interfaces:
          - interfaces:
              - <str>
            node: <str>
      profile: <str>
      ptp_enable: <bool>
      qos_profile: <str>
      raw_eos_cli: <str>
      speed: <str>
      subnet: <str>
  p2p_links_ip_pools:
    - ipv4_pool: <str>
      name: <str>
  p2p_links_profiles:
    - ip_pool: <str>
      ipv6_enable: <bool>
      isis_authentication_key: <str>
      isis_authentication_mode: <str>
      isis_circuit_type: <str>
      isis_hello_padding: <bool>
      isis_metric: <int>
      mtu: <int>
      name: <str>
      speed: <str>
```

## Local Users

### Description

Dictionary of local users
### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>local_users</samp>](## "local_users") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;- disabled</samp>](## "local_users.[].disabled") | Boolean |  |  |  | If "disabled" is true, the user will be removed and all other settings are ignored.<br>Useful for removing the default "admin" user. |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "local_users.[].name") | String | Required, Unique |  |  | Username |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;no_password</samp>](## "local_users.[].no_password") | Boolean |  | True |  | If set a password will not be configured for this user. "sha512_password" MUST not be defined for this user. |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;privilege</samp>](## "local_users.[].privilege") | Integer |  |  | Min: 1<br>Max: 15 | Initial privilege level with local EXEC authorization. |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;role</samp>](## "local_users.[].role") | String |  |  |  | EOS RBAC Role to be assigned to the user such as "network-admin" or "network-operator" |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;sha512_password</samp>](## "local_users.[].sha512_password") | String |  |  |  | Must be the hash of the password. By default EOS salts the password with the username, so the simplest is to generate the hash on an EOS device using the same username. |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ssh_key</samp>](## "local_users.[].ssh_key") | String |  |  |  | SSH key string |

### YAML

```yaml
local_users:
  - disabled: <bool>
    name: <str>
    no_password: <bool>
    privilege: <int>
    role: <str>
    sha512_password: <str>
    ssh_key: <str>
```

## MAC Address Table

### Description

MAC address-table aging time
Use to change the EOS default of 300.

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>mac_address_table</samp>](## "mac_address_table") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;aging_time</samp>](## "mac_address_table.aging_time") | Integer |  |  |  | Time in seconds |

### YAML

```yaml
mac_address_table:
  aging_time: <int>
```

## Management Eapi

### Description

Default is https management eAPI enabled.
The vrf is set to < mgmt_interface_vrf >

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>management_eapi</samp>](## "management_eapi") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;default_services</samp>](## "management_eapi.default_services") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;enable_http</samp>](## "management_eapi.enable_http") | Boolean |  | False |  |  |
| [<samp>&nbsp;&nbsp;enable_https</samp>](## "management_eapi.enable_https") | Boolean |  | True |  |  |

### YAML

```yaml
management_eapi:
  default_services: <bool>
  enable_http: <bool>
  enable_https: <bool>
```

## Mgmt Destination Networks

### Description

OOB mgmt interface destination networks - override default route
### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>mgmt_destination_networks</samp>](## "mgmt_destination_networks") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;- &lt;str&gt;</samp>](## "mgmt_destination_networks.[].&lt;str&gt;") | String |  |  |  | IPv4_network/Mask |

### YAML

```yaml
mgmt_destination_networks:
  - <str>
```

## Mgmt Gateway

### Description

Management interface configuration and it is IPv4 address
### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>mgmt_gateway</samp>](## "mgmt_gateway") | String |  |  |  |  |

### YAML

```yaml
mgmt_gateway: <str>
```

## Mgmt Interface

### Description

Management interface configuration
### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>mgmt_interface</samp>](## "mgmt_interface") | String |  | Management1 |  |  |

### YAML

```yaml
mgmt_interface: <str>
```

## Mgmt Interface VRF

### Description

Management interface configuration
### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>mgmt_interface_vrf</samp>](## "mgmt_interface_vrf") | String |  | MGMT |  |  |

### YAML

```yaml
mgmt_interface_vrf: <str>
```

## Mgmt VRF Routing

### Description

Management interface configuration
### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>mgmt_vrf_routing</samp>](## "mgmt_vrf_routing") | Boolean |  | False |  |  |

### YAML

```yaml
mgmt_vrf_routing: <bool>
```

## MLAG Ibgp Peering VRFs

### Description

On mlag leafs, an SVI interface is defined per vrf, to establish iBGP peering (required when mlag leafs in topology)
The SVI id will be derived from the base vlan defined: mlag_ibgp_peering_vrfs.base_vlan + (vrf_id or vrf_vni) - 1
Depending on the values of vrf_id / vrf_id it may be required to adjust the base_vlan to avoid overlaps or invalid vlan ids.
The SVI ip address derived from mlag_l3_peer_ipv4_pool is re-used across all iBGP peerings.

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>mlag_ibgp_peering_vrfs</samp>](## "mlag_ibgp_peering_vrfs") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;base_vlan</samp>](## "mlag_ibgp_peering_vrfs.base_vlan") | Integer |  | 3000 | Min: 1<br>Max: 4000 |  |

### YAML

```yaml
mlag_ibgp_peering_vrfs:
  base_vlan: <int>
```

## Name Server

### Description

Only name_server from eos_ci_config_gen.
The variables will make it to the intended config.

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>name_server</samp>](## "name_server") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;nodes</samp>](## "name_server.nodes") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "name_server.nodes.[].&lt;str&gt;") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;source</samp>](## "name_server.source") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "name_server.source.vrf") | String |  |  |  |  |

### YAML

```yaml
name_server:
  nodes:
    - <str>
  source:
    vrf: <str>
```

## Name Servers

### Description

Only eos_designs name_servers variables
### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>name_servers</samp>](## "name_servers") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;- &lt;str&gt;</samp>](## "name_servers.[].&lt;str&gt;") | String |  |  |  | IPv4 address |

### YAML

```yaml
name_servers:
  - <str>
```

## Network Services

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>network_services</samp>](## "network_services") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;- bgp_peer_groups</samp>](## "network_services.[].bgp_peer_groups") | List, items: Dictionary |  |  |  | Dictionary of BGP peer groups definitions (Optional).<br>This will configure BGP peer groups to be used inside the tenant VRF for peering with external devices.<br>Since BGP peer groups are configured at higher BGP level, shared between VRFs,<br>peer_group names should not overlap between VRFs.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- bfd</samp>](## "network_services.[].bgp_peer_groups.[].bfd") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default_originate</samp>](## "network_services.[].bgp_peer_groups.[].default_originate") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;always</samp>](## "network_services.[].bgp_peer_groups.[].default_originate.always") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "network_services.[].bgp_peer_groups.[].default_originate.enabled") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "network_services.[].bgp_peer_groups.[].description") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ebgp_multihop</samp>](## "network_services.[].bgp_peer_groups.[].ebgp_multihop") | Integer |  |  | Min: 1<br>Max: 255 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;local_as</samp>](## "network_services.[].bgp_peer_groups.[].local_as") | String |  |  |  | Local BGP ASN<br>eg. "65001.1200"<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maximum_routes</samp>](## "network_services.[].bgp_peer_groups.[].maximum_routes") | Integer |  |  | Min: 0<br>Max: 4294967294 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "network_services.[].bgp_peer_groups.[].name") | String |  |  |  | BGP peer group name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;next_hop_self</samp>](## "network_services.[].bgp_peer_groups.[].next_hop_self") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "network_services.[].bgp_peer_groups.[].nodes") | List, items: String |  |  |  | Nodes is required to restrict configuration of BGP neighbors to certain nodes in the network.<br>If not set the peer-group is created on the device which has a bgp_peer mapped to corresponding peer_group.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "network_services.[].bgp_peer_groups.[].nodes.[].&lt;str&gt;") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remote_as</samp>](## "network_services.[].bgp_peer_groups.[].remote_as") | Integer |  |  |  | Remote ASN |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_in</samp>](## "network_services.[].bgp_peer_groups.[].route_map_in") | String |  |  |  | Route-map name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_out</samp>](## "network_services.[].bgp_peer_groups.[].route_map_out") | String |  |  |  | Route-map name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;send_community</samp>](## "network_services.[].bgp_peer_groups.[].send_community") | String |  |  |  | 'all' or a combination of 'standard', 'extended', 'large' and 'link-bandwidth (w/options)'<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;set_ipv4_next_hop</samp>](## "network_services.[].bgp_peer_groups.[].set_ipv4_next_hop") | String |  |  |  | IPv4_address<br>Next hop settings can be either ipv4 or ipv6 for one neighbor, this will be applied by a uniquely generated route-map per neighbor.<br>Next hop takes precedence over route_map_out.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;set_ipv6_next_hop</samp>](## "network_services.[].bgp_peer_groups.[].set_ipv6_next_hop") | String |  |  |  | IPv6_address<br>Next hop settings can be either ipv4 or ipv6 for one neighbor, this will be applied by a uniquely generated route-map per neighbor.<br>Next hop takes precedence over route_map_out.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;update_source</samp>](## "network_services.[].bgp_peer_groups.[].update_source") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;weight</samp>](## "network_services.[].bgp_peer_groups.[].weight") | Integer |  |  | Min: 0<br>Max: 65535 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;enable_mlag_ibgp_peering_vrfs</samp>](## "network_services.[].enable_mlag_ibgp_peering_vrfs") | Boolean |  |  |  | MLAG IBGP peering per VRF.<br>By default an IBGP peering is configured per VRF between MLAG peers on separate VLANs.<br>Setting enable_mlag_ibgp_peering_vrfs: false under tenant will change this default to prevent configuration of these peerings and VLANs for all VRFs in the tenant.<br>This setting can be overridden per VRF.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;evpn_l2_multicast</samp>](## "network_services.[].evpn_l2_multicast") | Dictionary |  |  |  | Enable EVPN L2 Multicast for all SVIs and l2vlans within Tenant | Optional<br>- Multicast group binding is created only for Multicast traffic. BULL traffic will use ingress-replication<br>- Configures binding between VXLAN, VLAN, and multicast group IPv4 address using the following formula:<br>  < evpn_l2_multicast.underlay_l2_multicast_group_ipv4_pool > + < vlan_id - 1 > + < evpn_l2_multicast.underlay_l2_multicast_group_ipv4_pool_offset >.<br>- The recommendation is to assign a /20 block within the 232.0.0.0/8 Source-Specific Multicast range.<br>- Enables `redistribute igmp` on the router bgp MAC VRF.<br>- When evpn_l2_multicast.enabled is true for a VLAN or a tenant, "igmp snooping" and "igmp snooping querier" will always be enabled - overriding those individual settings.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "network_services.[].evpn_l2_multicast.enabled") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;underlay_l2_multicast_group_ipv4_pool</samp>](## "network_services.[].evpn_l2_multicast.underlay_l2_multicast_group_ipv4_pool") | String |  |  |  | IPv4_address/Mask |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;underlay_l2_multicast_group_ipv4_pool_offset</samp>](## "network_services.[].evpn_l2_multicast.underlay_l2_multicast_group_ipv4_pool_offset") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;evpn_l3_multicast</samp>](## "network_services.[].evpn_l3_multicast") | Dictionary |  |  |  | Enable L3 Multicast for all SVIs and l3vlans within Tenant | Optional<br>- In the evpn-l3ls design type, this enables L3 EVPN Multicast (aka OISM)<br>- Multicast group binding for VRF is created only for Multicast traffic. BULL traffic will use ingress-replication<br>- Configures binding between VXLAN, VLAN, and multicast group IPv4 address using the following formula:<br>  < l3_multicast.evpn_underlay_l3_multicast_group_ipv4_pool > + < vrf_vni - 1 > + < l3_multicast.evpn_underlay_l3_multicast_group_ipv4_pool_offset >.<br>- The recommendation is to assign a /20 block within the 232.0.0.0/8 Source-Specific Multicast range.<br>- If enabled on an SVI using the anycast default gateway feature, a diagnostic loopback (see below) MUST be configured to source IGMP traffic.<br>- Enables `evpn multicast` on the router bgp VRF.<br>- When enabled on an SVI:<br>     - If switch is part of an MLAG pair, enables "pim ipv4 sparse-mode" on the SVI.<br>     - If switch is standalone or A-A MH, enables "ip igmp" on the SVI.<br>     - If "ip address virtual" is configured, enables "pim ipv4 local-interface" and uses the diagnostic Loopback defined in the VRF<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "network_services.[].evpn_l3_multicast.enabled") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_peg</samp>](## "network_services.[].evpn_l3_multicast.evpn_peg") | List, items: Dictionary |  |  |  | For each group of nodes, allow configuration of EVPN PEG options (Optional)<br>The first group of settings where the device's hostname is present in the 'nodes' list will be used.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- nodes</samp>](## "network_services.[].evpn_l3_multicast.evpn_peg.[].nodes") | List, items: String |  |  |  | (Optional) will apply to all nodes with RP addresses configured if not set. |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "network_services.[].evpn_l3_multicast.evpn_peg.[].nodes.[].&lt;str&gt;") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;transit</samp>](## "network_services.[].evpn_l3_multicast.evpn_peg.[].transit") | Boolean |  |  |  | Enable EVPN PEG transit mode |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_underlay_l3_multicast_group_ipv4_pool</samp>](## "network_services.[].evpn_l3_multicast.evpn_underlay_l3_multicast_group_ipv4_pool") | String | Required |  |  | IPv4_address/Mask |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_underlay_l3_multicast_group_ipv4_pool_offset</samp>](## "network_services.[].evpn_l3_multicast.evpn_underlay_l3_multicast_group_ipv4_pool_offset") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;igmp_snooping_querier</samp>](## "network_services.[].igmp_snooping_querier") | Dictionary |  |  |  | Enable IGMP snooping querier for each SVI/l2vlan within tenant, by default using IP address of Loopback 0.<br>When enabled, IGMP snooping querier will only be configured on L3 devices, i.e., uplink_type: p2p.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "network_services.[].igmp_snooping_querier.enabled") | Boolean |  |  |  | Will be enabled automatically if "evpn_l2_multicast" is enabled. |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_address</samp>](## "network_services.[].igmp_snooping_querier.source_address") | String |  |  | Format: ipv4 | Default IP address of Loopback0 |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;version</samp>](## "network_services.[].igmp_snooping_querier.version") | Integer |  | 2 | Valid Values:<br>- 1<br>- 2<br>- 3 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;l2vlans</samp>](## "network_services.[].l2vlans") | List, items: Dictionary |  |  |  | Define L2 network services organized by vlan id. |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- bgp</samp>](## "network_services.[].l2vlans.[].bgp") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "network_services.[].l2vlans.[].bgp.raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the VLAN interface in the final EOS configuration<br>Overrides the setting on SVI level |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_l2_multicast</samp>](## "network_services.[].l2vlans.[].evpn_l2_multicast") | Boolean |  |  |  | Explicitly enable or disable evpn_l2_multicast to override setting of tenants.<tenant>.evpn_l2_multicast.enabled.<br>When evpn_l2_multicast.enabled is set to true for a vlan or a tenant, igmp snooping and igmp snooping querier will always be enabled - overriding those individual settings.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;id</samp>](## "network_services.[].l2vlans.[].id") | Integer | Required, Unique |  | Min: 1<br>Max: 4096 | VLAN id |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;igmp_snooping_enabled</samp>](## "network_services.[].l2vlans.[].igmp_snooping_enabled") | Boolean |  | True |  | Activate or deactivate IGMP snooping |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;igmp_snooping_querier</samp>](## "network_services.[].l2vlans.[].igmp_snooping_querier") | Dictionary |  |  |  | Enable igmp snooping querier, by default using IP address of Loopback 0.<br>When enabled, igmp snooping querier will only be configured on l3 devices, i.e., uplink_type: p2p.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "network_services.[].l2vlans.[].igmp_snooping_querier.enabled") | Boolean |  |  |  | Will be enabled automatically if evpn_l2_multicast is enabled. |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_address</samp>](## "network_services.[].l2vlans.[].igmp_snooping_querier.source_address") | String |  |  |  | IPv4_address<br>If not set, IP address of "Loopback0" will be used.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;version</samp>](## "network_services.[].l2vlans.[].igmp_snooping_querier.version") | Integer |  | 2 | Valid Values:<br>- 1<br>- 2<br>- 3 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "network_services.[].l2vlans.[].name") | String | Required |  |  | VLAN name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rt_override</samp>](## "network_services.[].l2vlans.[].rt_override") | Integer |  |  | Min: 1<br>Max: 16777215 | By default the MAC VRF RD/RT ID will be derived from mac_vrf_id_base<br>The rt_override allows us to override this value and statically define it (Optional)<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tags</samp>](## "network_services.[].l2vlans.[].tags") | List, items: String |  |  |  | Tags leveraged for networks services filtering<br>Tags are matched against filter.tags defined under Fabric Topology variables<br>Tags are also matched against the node_group name under Fabric Topology variables<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "network_services.[].l2vlans.[].tags.[].&lt;str&gt;") | String |  | all |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;trunk_groups</samp>](## "network_services.[].l2vlans.[].trunk_groups") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "network_services.[].l2vlans.[].trunk_groups.[].&lt;str&gt;") | String |  |  |  | Trunk groups are used for limiting vlans to trunk ports assigned to the same trunk group<br>Requires enable_trunk_groups: true<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vni_override</samp>](## "network_services.[].l2vlans.[].vni_override") | Integer |  |  | Min: 1<br>Max: 16777215 | By default the vni will be derived from mac_vrf_vni_base<br>The vni_override, allows to override this value and statically define it.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vxlan</samp>](## "network_services.[].l2vlans.[].vxlan") | Boolean |  | True |  | Extend this L2VLAN over VXLAN |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mac_vrf_id_base</samp>](## "network_services.[].mac_vrf_id_base") | Integer |  |  | Min: 0<br>Max: 16770000 | If not set, "mac_vrf_vni_base" will be used.<br>Base number for MAC VRF RD/RT ID (Required unless mac_vrf_vni_base is set)<br>ID is derived from the base number with simple addition.<br>e.g. mac_vrf_id_base = 10000, svi 100 = RD/RT 10100, svi 300 = RD/RT 10300.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mac_vrf_vni_base</samp>](## "network_services.[].mac_vrf_vni_base") | Integer |  |  | Min: 0<br>Max: 16770000 | Base number for MAC VRF VXLAN Network Identifier (Required with VXLAN)<br>VXLAN VNI is derived from the base number with simple addition.<br>e.g. mac_vrf_vni_base = 10000, svi 100 = VNI 10100, svi 300 = VNI 10300.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "network_services.[].name") | String | Required, Unique |  |  | Specify a tenant name.<br>Tenant provide a construct to group L3 VRFs and L2 VLANs.<br>Networks services can be filtered by tenant name.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;pim_rp_addresses</samp>](## "network_services.[].pim_rp_addresses") | List, items: Dictionary |  |  |  | For each group of nodes, allow configuration of RP Addresses & associated groups<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- groups</samp>](## "network_services.[].pim_rp_addresses.[].groups") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "network_services.[].pim_rp_addresses.[].groups.[].&lt;str&gt;") | String |  |  |  | Group_prefix/mask |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "network_services.[].pim_rp_addresses.[].nodes") | List, items: String |  |  |  | (Optional) will apply to all nodes with RP addresses configured if not set. |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "network_services.[].pim_rp_addresses.[].nodes.[].&lt;str&gt;") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rps</samp>](## "network_services.[].pim_rp_addresses.[].rps") | List, items: String |  |  |  | A minimum of one RP must be specified |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "network_services.[].pim_rp_addresses.[].rps.[].&lt;str&gt;") | String |  |  |  | RP address |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vlan_aware_bundle_number_base</samp>](## "network_services.[].vlan_aware_bundle_number_base") | Integer |  | 0 |  | Base number for vlan_aware_bundle.<br>The "Assigned Number" part of RD/RT is derived from vrf_vni + vlan_aware_bundle_number_base.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vrfs</samp>](## "network_services.[].vrfs") | List, items: Dictionary |  |  |  | vrf "default" is supported under network-services. Currently the supported options for "default" vrf are route-target,<br>route-distinguisher settings, structured_config, raw_eos_cli in bgp and SVIs are the only supported interface type.<br>Vlan-aware-bundles are supported as well inside default vrf. OSPF is not supported currently.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- additional_route_targets</samp>](## "network_services.[].vrfs.[].additional_route_targets") | List, items: Dictionary |  |  |  | Optional configuration of extra route-targets for this VRF. Useful for route-leaking or gateway between address families. |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- address_family</samp>](## "network_services.[].vrfs.[].additional_route_targets.[].address_family") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "network_services.[].vrfs.[].additional_route_targets.[].nodes") | List, items: String |  |  |  | Nodes is required to restrict configuration of BGP neighbors to certain nodes in the network.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "network_services.[].vrfs.[].additional_route_targets.[].nodes.[].&lt;str&gt;") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_target</samp>](## "network_services.[].vrfs.[].additional_route_targets.[].route_target") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "network_services.[].vrfs.[].additional_route_targets.[].type") | String |  |  | Valid Values:<br>- import<br>- export |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp</samp>](## "network_services.[].vrfs.[].bgp") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "network_services.[].vrfs.[].bgp.raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the VLAN interface in the final EOS configuration<br>Overrides the setting on SVI level.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "network_services.[].vrfs.[].bgp.structured_config") | Dictionary |  |  |  | Custom structured config added under vlan_interfaces.<interface> for eos_cli_config_gen.<br>Overrides the setting on SVI level.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp_peer_groups</samp>](## "network_services.[].vrfs.[].bgp_peer_groups") | List, items: Dictionary |  |  |  | Dictionary of BGP peer groups definitions (Optional).<br>This will configure BGP peer groups to be used inside the tenant VRF for peering with external devices.<br>Since BGP peer groups are configured at higher BGP level, shared between VRFs,<br>peer_group names should not overlap between VRFs.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- bfd</samp>](## "network_services.[].vrfs.[].bgp_peer_groups.[].bfd") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default_originate</samp>](## "network_services.[].vrfs.[].bgp_peer_groups.[].default_originate") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;always</samp>](## "network_services.[].vrfs.[].bgp_peer_groups.[].default_originate.always") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "network_services.[].vrfs.[].bgp_peer_groups.[].default_originate.enabled") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "network_services.[].vrfs.[].bgp_peer_groups.[].description") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ebgp_multihop</samp>](## "network_services.[].vrfs.[].bgp_peer_groups.[].ebgp_multihop") | Integer |  |  | Min: 1<br>Max: 255 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;local_as</samp>](## "network_services.[].vrfs.[].bgp_peer_groups.[].local_as") | String |  |  |  | Local BGP ASN<br>eg. "65001.1200"<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maximum_routes</samp>](## "network_services.[].vrfs.[].bgp_peer_groups.[].maximum_routes") | Integer |  |  | Min: 0<br>Max: 4294967294 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "network_services.[].vrfs.[].bgp_peer_groups.[].name") | String |  |  |  | BGP peer group name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;next_hop_self</samp>](## "network_services.[].vrfs.[].bgp_peer_groups.[].next_hop_self") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "network_services.[].vrfs.[].bgp_peer_groups.[].nodes") | List, items: String |  |  |  | Nodes is required to restrict configuration of BGP neighbors to certain nodes in the network.<br>If not set the peer-group is created on the device which has a bgp_peer mapped to corresponding peer_group.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "network_services.[].vrfs.[].bgp_peer_groups.[].nodes.[].&lt;str&gt;") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remote_as</samp>](## "network_services.[].vrfs.[].bgp_peer_groups.[].remote_as") | Integer |  |  |  | Remote ASN |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_in</samp>](## "network_services.[].vrfs.[].bgp_peer_groups.[].route_map_in") | String |  |  |  | Route-map name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_out</samp>](## "network_services.[].vrfs.[].bgp_peer_groups.[].route_map_out") | String |  |  |  | Route-map name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;send_community</samp>](## "network_services.[].vrfs.[].bgp_peer_groups.[].send_community") | String |  |  |  | 'all' or a combination of 'standard', 'extended', 'large' and 'link-bandwidth (w/options)'<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;set_ipv4_next_hop</samp>](## "network_services.[].vrfs.[].bgp_peer_groups.[].set_ipv4_next_hop") | String |  |  |  | IPv4_address<br>Next hop settings can be either ipv4 or ipv6 for one neighbor, this will be applied by a uniquely generated route-map per neighbor.<br>Next hop takes precedence over route_map_out.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;set_ipv6_next_hop</samp>](## "network_services.[].vrfs.[].bgp_peer_groups.[].set_ipv6_next_hop") | String |  |  |  | IPv6_address<br>Next hop settings can be either ipv4 or ipv6 for one neighbor, this will be applied by a uniquely generated route-map per neighbor.<br>Next hop takes precedence over route_map_out.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;update_source</samp>](## "network_services.[].vrfs.[].bgp_peer_groups.[].update_source") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;weight</samp>](## "network_services.[].vrfs.[].bgp_peer_groups.[].weight") | Integer |  |  | Min: 0<br>Max: 65535 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp_peers</samp>](## "network_services.[].vrfs.[].bgp_peers") | List, items: Dictionary |  |  |  | Dictionary of BGP peer definitions (Optional).<br>This will configure BGP neighbors inside the tenant VRF for peering with external devices.<br>The configured peer will automatically be activated for ipv4 or ipv6 address family based on the ip address.<br>Note, only ipv4 and ipv6 address families are currently supported in eos_designs.<br>For other address families, use custom_structured configuration with eos_cli_config_gen.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- bfd</samp>](## "network_services.[].vrfs.[].bgp_peers.[].bfd") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default_originate</samp>](## "network_services.[].vrfs.[].bgp_peers.[].default_originate") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;always</samp>](## "network_services.[].vrfs.[].bgp_peers.[].default_originate.always") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "network_services.[].vrfs.[].bgp_peers.[].description") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ebgp_multihop</samp>](## "network_services.[].vrfs.[].bgp_peers.[].ebgp_multihop") | Integer |  |  | Min: 1<br>Max: 255 | Time-to-live in range of hops |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "network_services.[].vrfs.[].bgp_peers.[].ip_address") | String | Required, Unique |  |  | IPv4_address or IPv6_address |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;local_as</samp>](## "network_services.[].vrfs.[].bgp_peers.[].local_as") | String |  |  |  | Local BGP ASN<br>eg. "65001.1200"<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maximum_routes</samp>](## "network_services.[].vrfs.[].bgp_peers.[].maximum_routes") | Integer |  |  | Min: 0<br>Max: 4294967294 | Maximum number of routes (0 means unlimited) |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;next_hop_self</samp>](## "network_services.[].vrfs.[].bgp_peers.[].next_hop_self") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "network_services.[].vrfs.[].bgp_peers.[].nodes") | List, items: String |  |  |  | Nodes is required to restrict configuration of BGP neighbors to certain nodes in the network. |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "network_services.[].vrfs.[].bgp_peers.[].nodes.[].&lt;str&gt;") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;password</samp>](## "network_services.[].vrfs.[].bgp_peers.[].password") | String |  |  |  | Encrypted password |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefix_list_in</samp>](## "network_services.[].vrfs.[].bgp_peers.[].prefix_list_in") | String |  |  |  | Prefix list name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefix_list_out</samp>](## "network_services.[].vrfs.[].bgp_peers.[].prefix_list_out") | String |  |  |  | Prefix list name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remote_as</samp>](## "network_services.[].vrfs.[].bgp_peers.[].remote_as") | Integer |  |  |  | Remote ASN |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_in</samp>](## "network_services.[].vrfs.[].bgp_peers.[].route_map_in") | String |  |  |  | Route-map name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_out</samp>](## "network_services.[].vrfs.[].bgp_peers.[].route_map_out") | String |  |  |  | Route-map name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;send_community</samp>](## "network_services.[].vrfs.[].bgp_peers.[].send_community") | String |  |  |  | 'all' or a combination of 'standard', 'extended', 'large' and 'link-bandwidth (w/options)'<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;set_ipv4_next_hop</samp>](## "network_services.[].vrfs.[].bgp_peers.[].set_ipv4_next_hop") | String |  |  |  | IPv4_address<br>Next hop settings can be either ipv4 or ipv6 for one neighbor, this will be applied by a uniquely generated route-map per neighbor.<br>Next hop takes precedence over route_map_out.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;set_ipv6_next_hop</samp>](## "network_services.[].vrfs.[].bgp_peers.[].set_ipv6_next_hop") | String |  |  |  | IPv6_address<br>Next hop settings can be either ipv4 or ipv6 for one neighbor, this will be applied by a uniquely generated route-map per neighbor.<br>Next hop takes precedence over route_map_out.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;timers</samp>](## "network_services.[].vrfs.[].bgp_peers.[].timers") | String |  |  |  | BGP Keepalive and Hold Timer values in seconds as string <0-3600> <0-3600> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;update_source</samp>](## "network_services.[].vrfs.[].bgp_peers.[].update_source") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;weight</samp>](## "network_services.[].vrfs.[].bgp_peers.[].weight") | Integer |  |  | Min: 0<br>Max: 65535 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "network_services.[].vrfs.[].description") | String |  |  |  | VRF description |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enable_mlag_ibgp_peering_vrfs</samp>](## "network_services.[].vrfs.[].enable_mlag_ibgp_peering_vrfs") | Boolean |  |  |  | MLAG IBGP peering per VRF (optional)<br>By default an IBGP peering is configured per VRF between MLAG peers on separate VLANs.<br>Setting enable_mlag_ibgp_peering_vrfs: false under vrf will change this default and/or override the tenant-wide setting<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_helpers</samp>](## "network_services.[].vrfs.[].ip_helpers") | List, items: Dictionary |  |  |  | IP helper for DHCP relay |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- ip_helper</samp>](## "network_services.[].vrfs.[].ip_helpers.[].ip_helper") | String | Required, Unique |  |  | IPv4 DHCP server IP |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_interface</samp>](## "network_services.[].vrfs.[].ip_helpers.[].source_interface") | String |  |  |  | Interface name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_vrf</samp>](## "network_services.[].vrfs.[].ip_helpers.[].source_vrf") | String |  |  |  | VRF to originate DHCP relay packets to DHCP server. If not set, uses current VRF |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_static_routes</samp>](## "network_services.[].vrfs.[].ipv6_static_routes") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- destination_address_prefix</samp>](## "network_services.[].vrfs.[].ipv6_static_routes.[].destination_address_prefix") | String |  |  |  | IPv4_address/Mask |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;distance</samp>](## "network_services.[].vrfs.[].ipv6_static_routes.[].distance") | Integer |  |  | Min: 1<br>Max: 255 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;gateway</samp>](## "network_services.[].vrfs.[].ipv6_static_routes.[].gateway") | String |  |  | Format: ipv6 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interface</samp>](## "network_services.[].vrfs.[].ipv6_static_routes.[].interface") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;metric</samp>](## "network_services.[].vrfs.[].ipv6_static_routes.[].metric") | Integer |  |  | Min: 0<br>Max: 4294967295 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "network_services.[].vrfs.[].ipv6_static_routes.[].name") | String |  |  |  | description |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "network_services.[].vrfs.[].ipv6_static_routes.[].nodes") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "network_services.[].vrfs.[].ipv6_static_routes.[].nodes.[].&lt;str&gt;") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tag</samp>](## "network_services.[].vrfs.[].ipv6_static_routes.[].tag") | Integer |  |  | Min: 0<br>Max: 4294967295 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;l3_interfaces</samp>](## "network_services.[].vrfs.[].l3_interfaces") | List, items: Dictionary |  |  |  | List of L3 interfaces (Optional)<br>This will create IP routed interface inside VRF. Length of interfaces, nodes and ip_addresses must match<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- description</samp>](## "network_services.[].vrfs.[].l3_interfaces.[].description") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;descriptions</samp>](## "network_services.[].vrfs.[].l3_interfaces.[].descriptions") | List, items: String |  |  |  | "descriptions" has precedence over "description"<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "network_services.[].vrfs.[].l3_interfaces.[].descriptions.[].&lt;str&gt;") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "network_services.[].vrfs.[].l3_interfaces.[].enabled") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interfaces</samp>](## "network_services.[].vrfs.[].l3_interfaces.[].interfaces") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "network_services.[].vrfs.[].l3_interfaces.[].interfaces.[].&lt;str&gt;") | String |  |  |  | Interface name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_addresses</samp>](## "network_services.[].vrfs.[].l3_interfaces.[].ip_addresses") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "network_services.[].vrfs.[].l3_interfaces.[].ip_addresses.[].&lt;str&gt;") | String |  |  |  | IPv4_address/Mask |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mtu</samp>](## "network_services.[].vrfs.[].l3_interfaces.[].mtu") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "network_services.[].vrfs.[].l3_interfaces.[].nodes") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "network_services.[].vrfs.[].l3_interfaces.[].nodes.[].&lt;str&gt;") | String |  |  |  | Node |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ospf</samp>](## "network_services.[].vrfs.[].l3_interfaces.[].ospf") | Dictionary |  |  |  | OSPF interface configuration |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;area</samp>](## "network_services.[].vrfs.[].l3_interfaces.[].ospf.area") | Integer |  | 0 |  | OSPF area id |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;authentication</samp>](## "network_services.[].vrfs.[].l3_interfaces.[].ospf.authentication") | String |  |  | Valid Values:<br>- simple<br>- message-digest |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cost</samp>](## "network_services.[].vrfs.[].l3_interfaces.[].ospf.cost") | Integer |  |  |  | OSPF link cost |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "network_services.[].vrfs.[].l3_interfaces.[].ospf.enabled") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;message_digest_keys</samp>](## "network_services.[].vrfs.[].l3_interfaces.[].ospf.message_digest_keys") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- hash_algorithm</samp>](## "network_services.[].vrfs.[].l3_interfaces.[].ospf.message_digest_keys.[].hash_algorithm") | String |  | sha512 | Valid Values:<br>- md5<br>- sha1<br>- sha256<br>- sha384<br>- sha512 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;id</samp>](## "network_services.[].vrfs.[].l3_interfaces.[].ospf.message_digest_keys.[].id") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key</samp>](## "network_services.[].vrfs.[].l3_interfaces.[].ospf.message_digest_keys.[].key") | String |  |  |  | Key password |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;point_to_point</samp>](## "network_services.[].vrfs.[].l3_interfaces.[].ospf.point_to_point") | Boolean |  | False |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;simple_auth_key</samp>](## "network_services.[].vrfs.[].l3_interfaces.[].ospf.simple_auth_key") | String |  |  |  | Password used with simple authentication |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "network_services.[].vrfs.[].l3_interfaces.[].raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the VLAN interface in the final EOS configuration<br>Overrides the setting on SVI level.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "network_services.[].vrfs.[].l3_interfaces.[].structured_config") | Dictionary |  |  |  | Custom structured config added under vlan_interfaces.<interface> for eos_cli_config_gen.<br>Overrides the setting on SVI level.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_ibgp_peering_ipv4_pool</samp>](## "network_services.[].vrfs.[].mlag_ibgp_peering_ipv4_pool") | String |  |  |  | IPv4_address/Mask<br>The subnet used for iBGP peering in the VRF.<br>Each MLAG pair will be assigned a subnet based on the ID of the primary MLAG switch<br>If not set, "mlag_peer_l3_ipv4_pool" or "mlag_peer_ipv4_pool" will be used<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_ibgp_peering_vlan</samp>](## "network_services.[].vrfs.[].mlag_ibgp_peering_vlan") | Integer |  |  | Min: 1<br>Max: 4096 | Manually define the VLAN used on the MLAG pair for the iBGP session (optional)<br>By default this parameter is calculated using the following formula: <mlag_ibgp_peering_vrfs.base_vlan> + <vrf_id> - 1<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "network_services.[].vrfs.[].name") | String | Required, Unique |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ospf</samp>](## "network_services.[].vrfs.[].ospf") | Dictionary |  |  |  | Dictionary for router OSPF configuration (optional)<br>This will create an ospf routing instance in the tenant VRF. If there is no nodes definition, the ospf instance will be<br>created on all leafs where the vrf is deployed. This will also cause automatic ospf redistribution into bgp unless<br>explicitly turned off with "redistribute_ospf: false".<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bfd</samp>](## "network_services.[].vrfs.[].ospf.bfd") | Boolean |  | False |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "network_services.[].vrfs.[].ospf.enabled") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;max_lsa</samp>](## "network_services.[].vrfs.[].ospf.max_lsa") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "network_services.[].vrfs.[].ospf.nodes") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "network_services.[].vrfs.[].ospf.nodes.[].&lt;str&gt;") | String |  |  |  | Hostname |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;process_id</samp>](## "network_services.[].vrfs.[].ospf.process_id") | Integer |  |  |  | If not set, "vrf_id" will be used. |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;redistribute_bgp</samp>](## "network_services.[].vrfs.[].ospf.redistribute_bgp") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "network_services.[].vrfs.[].ospf.redistribute_bgp.enabled") | Boolean |  | True |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "network_services.[].vrfs.[].ospf.redistribute_bgp.route_map") | String |  |  |  | Route-map name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;router_id</samp>](## "network_services.[].vrfs.[].ospf.router_id") | String |  |  |  | If not set, switch router_id will be used. |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "network_services.[].vrfs.[].raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the VLAN interface in the final EOS configuration<br>Overrides the setting on SVI level.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;redistribute_ospf</samp>](## "network_services.[].vrfs.[].redistribute_ospf") | Boolean |  | True |  | Non-selectively enabling or disabling redistribute ospf inside the VRF (optional) |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;redistribute_static</samp>](## "network_services.[].vrfs.[].redistribute_static") | Boolean |  |  |  | Non-selectively enabling or disabling redistribute static inside the VRF (Optional). |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;static_routes</samp>](## "network_services.[].vrfs.[].static_routes") | List, items: Dictionary |  |  |  | Dictionary of static routes for v4 and/or v6 (Optional).<br>This will create static routes inside the tenant VRF.<br>If nodes are not specified, all l3leafs that carry the VRF will also be applied the static routes.<br>If a node has a static route in the VRF, redistribute static will be automatically enabled in that VRF.<br>This automatic behavior can be overridden non-selectively with the redistribute_static knob for the VRF.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- destination_address_prefix</samp>](## "network_services.[].vrfs.[].static_routes.[].destination_address_prefix") | String |  |  |  | IPv4_address/Mask |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;distance</samp>](## "network_services.[].vrfs.[].static_routes.[].distance") | Integer |  |  | Min: 1<br>Max: 255 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;gateway</samp>](## "network_services.[].vrfs.[].static_routes.[].gateway") | String |  |  |  | IPv4_address |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interface</samp>](## "network_services.[].vrfs.[].static_routes.[].interface") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;metric</samp>](## "network_services.[].vrfs.[].static_routes.[].metric") | Integer |  |  | Min: 0<br>Max: 4294967295 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "network_services.[].vrfs.[].static_routes.[].name") | String |  |  |  | description |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "network_services.[].vrfs.[].static_routes.[].nodes") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "network_services.[].vrfs.[].static_routes.[].nodes.[].&lt;str&gt;") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tag</samp>](## "network_services.[].vrfs.[].static_routes.[].tag") | Integer |  |  | Min: 0<br>Max: 4294967295 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "network_services.[].vrfs.[].structured_config") | Dictionary |  |  |  | Custom structured config added under vlan_interfaces.<interface> for eos_cli_config_gen.<br>Overrides the setting on SVI level.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;svis</samp>](## "network_services.[].vrfs.[].svis") | List, items: Dictionary |  |  |  | Dictionary of SVIs<br>This will create both the L3 SVI and L2 VLAN based on filters applied to l3leaf and l2leaf.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- bgp</samp>](## "network_services.[].vrfs.[].svis.[].bgp") | Dictionary |  |  |  | Structured configuration and eos cli commands rendered on router_bgp.vlans<br>This configuration will not be applied to vlan aware bundles<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "network_services.[].vrfs.[].svis.[].bgp.raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the VLAN interface in the final EOS configuration<br>Overrides the setting on SVI level.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "network_services.[].vrfs.[].svis.[].bgp.structured_config") | Dictionary |  |  |  | Custom structured config added under vlan_interfaces.<interface> for eos_cli_config_gen.<br>Overrides the setting on SVI level.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "network_services.[].vrfs.[].svis.[].description") | String |  | VLAN name |  | SVI description<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "network_services.[].vrfs.[].svis.[].enabled") | Boolean |  |  |  | Enable or disable interface |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_l2_multicast</samp>](## "network_services.[].vrfs.[].svis.[].evpn_l2_multicast") | Boolean |  |  |  | Explicitly enable or disable evpn_l2_multicast to override setting of tenants.<tenant>.evpn_l2_multicast.enabled.<br>When evpn_l2_multicast.enabled is set to true for a vlan or a tenant, "igmp snooping" and "igmp snooping querier" will always be enabled - overriding those individual settings.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;id</samp>](## "network_services.[].vrfs.[].svis.[].id") | Integer | Required, Unique |  | Min: 1<br>Max: 4096 | SVI interface id and VLAN id. |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;igmp_snooping_enabled</samp>](## "network_services.[].vrfs.[].svis.[].igmp_snooping_enabled") | Boolean |  | True |  | Enable IGMP Snooping |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;igmp_snooping_querier</samp>](## "network_services.[].vrfs.[].svis.[].igmp_snooping_querier") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "network_services.[].vrfs.[].svis.[].igmp_snooping_querier.enabled") | Boolean |  |  |  | Will be enabled automatically if evpn_l2_multicast is enabled. |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_address</samp>](## "network_services.[].vrfs.[].svis.[].igmp_snooping_querier.source_address") | String |  |  |  | IPv4_address<br>If not set, IP address of "Loopback0" will be used.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;version</samp>](## "network_services.[].vrfs.[].svis.[].igmp_snooping_querier.version") | Integer |  | 2 | Valid Values:<br>- 1<br>- 2<br>- 3 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_address_virtual</samp>](## "network_services.[].vrfs.[].svis.[].ip_address_virtual") | String |  |  |  | IPv4_address/Mask<br>ip address virtual to configure VXLAN Anycast IP address<br>Conserves IP addresses in VXLAN deployments as it doesn't require unique IP addresses on each node.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_address_virtual_secondaries</samp>](## "network_services.[].vrfs.[].svis.[].ip_address_virtual_secondaries") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "network_services.[].vrfs.[].svis.[].ip_address_virtual_secondaries.[].&lt;str&gt;") | String |  |  |  | IPv4_address/Mask |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_helpers</samp>](## "network_services.[].vrfs.[].svis.[].ip_helpers") | List, items: Dictionary |  |  |  | IP helper for DHCP relay |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- ip_helper</samp>](## "network_services.[].vrfs.[].svis.[].ip_helpers.[].ip_helper") | String | Required, Unique |  |  | IPv4 DHCP server IP |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_interface</samp>](## "network_services.[].vrfs.[].svis.[].ip_helpers.[].source_interface") | String |  |  |  | Interface name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_vrf</samp>](## "network_services.[].vrfs.[].svis.[].ip_helpers.[].source_vrf") | String |  |  |  | VRF to originate DHCP relay packets to DHCP server. If not set, uses current VRF |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_virtual_router_addresses</samp>](## "network_services.[].vrfs.[].svis.[].ip_virtual_router_addresses") | List, items: String |  |  |  | IPv4_address/Mask or IPv4_address<br>note, also requires an IP address to be configured on the SVI where it is applied.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "network_services.[].vrfs.[].svis.[].ip_virtual_router_addresses.[].&lt;str&gt;") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_address_virtual</samp>](## "network_services.[].vrfs.[].svis.[].ipv6_address_virtual") | String |  |  |  | IPv6_address/Mask<br>ipv6 address virtuals to configure VXLAN Anycast IP address (Optional)<br>The below "ipv6_address_virtual" key will be deprecated in AVD v4.0 in favor of the new "ipv6_address_virtuals"<br>If both "ipv6_address_virtual" and "ipv6_address_virtuals" are set, all addresses will be configured<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_address_virtuals</samp>](## "network_services.[].vrfs.[].svis.[].ipv6_address_virtuals") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "network_services.[].vrfs.[].svis.[].ipv6_address_virtuals.[].&lt;str&gt;") | String |  |  |  | IPv6_address/Mask |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_virtual_router_addresses</samp>](## "network_services.[].vrfs.[].svis.[].ipv6_virtual_router_addresses") | String |  |  |  | IPv6_address |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mtu</samp>](## "network_services.[].vrfs.[].svis.[].mtu") | Integer |  |  |  | Defined interface MTU |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "network_services.[].vrfs.[].svis.[].name") | String |  |  |  | VLAN name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "network_services.[].vrfs.[].svis.[].nodes") | List, items: Dictionary |  |  |  | Define node specific configuration, such as unique IP addresses. |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- ip_address</samp>](## "network_services.[].vrfs.[].svis.[].nodes.[].ip_address") | String |  |  |  | IPv4_address/Mask<br>Device unique IP address for node.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_address_virtual_secondaries</samp>](## "network_services.[].vrfs.[].svis.[].nodes.[].ip_address_virtual_secondaries") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "network_services.[].vrfs.[].svis.[].nodes.[].ip_address_virtual_secondaries.[].&lt;str&gt;") | String |  |  |  | IPv4_address/Mask |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_helpers</samp>](## "network_services.[].vrfs.[].svis.[].nodes.[].ip_helpers") | List, items: Dictionary |  |  |  | IP helper for DHCP relay |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- ip_helper</samp>](## "network_services.[].vrfs.[].svis.[].nodes.[].ip_helpers.[].ip_helper") | String | Required, Unique |  |  | IPv4 DHCP server IP |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_interface</samp>](## "network_services.[].vrfs.[].svis.[].nodes.[].ip_helpers.[].source_interface") | String |  |  |  | Interface name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_vrf</samp>](## "network_services.[].vrfs.[].svis.[].nodes.[].ip_helpers.[].source_vrf") | String |  |  |  | VRF to originate DHCP relay packets to DHCP server. If not set, uses current VRF |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_virtual_router_addresses</samp>](## "network_services.[].vrfs.[].svis.[].nodes.[].ip_virtual_router_addresses") | List, items: String |  |  |  | IPv4_address/Mask or IPv4_address<br>note, also requires an IP address to be configured on the SVI where it is applied.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "network_services.[].vrfs.[].svis.[].nodes.[].ip_virtual_router_addresses.[].&lt;str&gt;") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_address</samp>](## "network_services.[].vrfs.[].svis.[].nodes.[].ipv6_address") | String |  |  |  | IPv6_address/Mask<br>Device unique IPv6 address for node.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;node</samp>](## "network_services.[].vrfs.[].svis.[].nodes.[].node") | String | Required, Unique |  |  | l3_leaf inventory hostname |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "network_services.[].vrfs.[].svis.[].nodes.[].raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the VLAN interface in the final EOS configuration<br>Overrides the setting on SVI level.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "network_services.[].vrfs.[].svis.[].nodes.[].structured_config") | Dictionary |  |  |  | Custom structured config added under vlan_interfaces.<interface> for eos_cli_config_gen.<br>Overrides the setting on SVI level.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ospf</samp>](## "network_services.[].vrfs.[].svis.[].ospf") | Dictionary |  |  |  | OSPF interface configuration |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;area</samp>](## "network_services.[].vrfs.[].svis.[].ospf.area") | Integer |  | 0 |  | OSPF area id |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;authentication</samp>](## "network_services.[].vrfs.[].svis.[].ospf.authentication") | String |  |  | Valid Values:<br>- simple<br>- message-digest |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cost</samp>](## "network_services.[].vrfs.[].svis.[].ospf.cost") | Integer |  |  |  | OSPF link cost |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "network_services.[].vrfs.[].svis.[].ospf.enabled") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;message_digest_keys</samp>](## "network_services.[].vrfs.[].svis.[].ospf.message_digest_keys") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- hash_algorithm</samp>](## "network_services.[].vrfs.[].svis.[].ospf.message_digest_keys.[].hash_algorithm") | String |  | sha512 | Valid Values:<br>- md5<br>- sha1<br>- sha256<br>- sha384<br>- sha512 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;id</samp>](## "network_services.[].vrfs.[].svis.[].ospf.message_digest_keys.[].id") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key</samp>](## "network_services.[].vrfs.[].svis.[].ospf.message_digest_keys.[].key") | String |  |  |  | Key password |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;point_to_point</samp>](## "network_services.[].vrfs.[].svis.[].ospf.point_to_point") | Boolean |  | True |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;simple_auth_key</samp>](## "network_services.[].vrfs.[].svis.[].ospf.simple_auth_key") | String |  |  |  | Password used with simple authentication |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;profile</samp>](## "network_services.[].vrfs.[].svis.[].profile") | String |  |  |  | SVI profile name to apply<br>If variables are configured in profile AND SVI, SVI information will overwrite profile<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "network_services.[].vrfs.[].svis.[].raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the VLAN interface in the final EOS configuration<br>Overrides the setting on SVI level<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rt_override</samp>](## "network_services.[].vrfs.[].svis.[].rt_override") | Integer |  |  | Min: 1<br>Max: 16777215 | By default the MAC VRF RD/RT ID will be derived from "mac_vrf_id_base"<br>The rt_override allows us to override this value and statically define it (optional)<br>If not set, vni_override will be used.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "network_services.[].vrfs.[].svis.[].structured_config") | Dictionary |  |  |  | Custom structured config added under vlan_interfaces.<interface> for eos_cli_config_gen.<br>Overrides the setting on SVI level.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tags</samp>](## "network_services.[].vrfs.[].svis.[].tags") | List, items: String |  |  |  | Tags leveraged for networks services filtering<br>Tags are matched against "filter.tags" defined under Fabric Topology variables<br>Tags are also matched against the "node_group" name under Fabric Topology variables<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "network_services.[].vrfs.[].svis.[].tags.[].&lt;str&gt;") | String |  | all |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;trunk_groups</samp>](## "network_services.[].vrfs.[].svis.[].trunk_groups") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "network_services.[].vrfs.[].svis.[].trunk_groups.[].&lt;str&gt;") | String |  |  |  | Trunk groups are used for limiting vlans to trunk ports assigned to the same trunk group<br>Requires "enable_trunk_groups: true"<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vni_override</samp>](## "network_services.[].vrfs.[].svis.[].vni_override") | Integer |  |  | Min: 1<br>Max: 16777215 | By default the vni will be derived from "mac_vrf_vni_base"<br>The vni_override allows us to override this value and statically define it (optional)<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vxlan</samp>](## "network_services.[].vrfs.[].svis.[].vxlan") | Boolean |  | True |  | Extend this SVI over VXLAN |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf_id</samp>](## "network_services.[].vrfs.[].vrf_id") | Integer |  |  | Min: 1<br>Max: 1024 | Required if "vrf_vni" is not set.<br>"vrf_id" is used as default value for "vrf_vni" and "ospf.process_id" unless those are set.<br>"vrf_id" is preferred over "vrf_vni" for VRF RD/RT ID before vrf_vni<br>"vrf_id" is preferred over "vrf_vni" for MLAG IBGP peering vlan, see "mlag_ibgp_peering_vrfs.base_vlan" for details<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf_vni</samp>](## "network_services.[].vrfs.[].vrf_vni") | Integer |  |  | Min: 1<br>Max: 1024 | Required if "vrf_id" is not set.<br>The VRF VNI range is not limited, but if vrf_id is not set, "vrf_vni" is used for calculating MLAG IBGP peering vlan id.<br>See "mlag_ibgp_peering_vrfs.base_vlan" for details.<br>If vrf_vni > 10000 make sure to adjust "mac_vrf_vni_base" accordingly to avoid overlap.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vtep_diagnostic</samp>](## "network_services.[].vrfs.[].vtep_diagnostic") | Dictionary |  |  |  | Enable VTEP Network diagnostics (Optional)<br>This will create a loopback with virtual source-nat enable to perform diagnostics from the switch<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loopback</samp>](## "network_services.[].vrfs.[].vtep_diagnostic.loopback") | Integer |  |  | Min: 2<br>Max: 2100 | Loopback interface number, required (when vtep_diagnotics defined)<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loopback_ip_pools</samp>](## "network_services.[].vrfs.[].vtep_diagnostic.loopback_ip_pools") | List, items: Dictionary |  |  |  | For inventories with multiple PODs a loopback range can be set per POD to avoid overlaps.<br>This only takes effect when loopback_ip_range is not defined, ptional (loopback is not created unless loopback_ip_range or loopback_ip_pools are set)<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- ipv4_pool</samp>](## "network_services.[].vrfs.[].vtep_diagnostic.loopback_ip_pools.[].ipv4_pool") | String |  |  |  | IPv4_address/Mask |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pod</samp>](## "network_services.[].vrfs.[].vtep_diagnostic.loopback_ip_pools.[].pod") | String |  |  |  | POD name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loopback_ip_range</samp>](## "network_services.[].vrfs.[].vtep_diagnostic.loopback_ip_range") | String |  |  |  | IPv4_address/Mask<br>Loopback ip range, a unique ip is derived from this ranged and assigned<br>to each l3 leaf based on it's unique id, ptional (loopback is not created unless loopback_ip_range or loopback_ip_pools are set)<br> |

### YAML

```yaml
network_services:
  - bgp_peer_groups:
      - bfd: <bool>
        default_originate:
          always: <bool>
          enabled: <bool>
        description: <str>
        ebgp_multihop: <int>
        local_as: <str>
        maximum_routes: <int>
        name: <str>
        next_hop_self: <bool>
        nodes:
          - <str>
        remote_as: <int>
        route_map_in: <str>
        route_map_out: <str>
        send_community: <str>
        set_ipv4_next_hop: <str>
        set_ipv6_next_hop: <str>
        update_source: <str>
        weight: <int>
    enable_mlag_ibgp_peering_vrfs: <bool>
    evpn_l2_multicast:
      enabled: <bool>
      underlay_l2_multicast_group_ipv4_pool: <str>
      underlay_l2_multicast_group_ipv4_pool_offset: <int>
    evpn_l3_multicast:
      enabled: <bool>
      evpn_peg:
        - nodes:
            - <str>
          transit: <bool>
      evpn_underlay_l3_multicast_group_ipv4_pool: <str>
      evpn_underlay_l3_multicast_group_ipv4_pool_offset: <int>
    igmp_snooping_querier:
      enabled: <bool>
      source_address: <str>
      version: <int>
    l2vlans:
      - bgp:
          raw_eos_cli: <str>
        evpn_l2_multicast: <bool>
        id: <int>
        igmp_snooping_enabled: <bool>
        igmp_snooping_querier:
          enabled: <bool>
          source_address: <str>
          version: <int>
        name: <str>
        rt_override: <int>
        tags:
          - <str>
        trunk_groups:
          - <str>
        vni_override: <int>
        vxlan: <bool>
    mac_vrf_id_base: <int>
    mac_vrf_vni_base: <int>
    name: <str>
    pim_rp_addresses:
      - groups:
          - <str>
        nodes:
          - <str>
        rps:
          - <str>
    vlan_aware_bundle_number_base: <int>
    vrfs:
      - additional_route_targets:
          - address_family: <str>
            nodes:
              - <str>
            route_target: <str>
            type: <str>
        bgp:
          raw_eos_cli: <str>
          structured_config:
        bgp_peer_groups:
          - bfd: <bool>
            default_originate:
              always: <bool>
              enabled: <bool>
            description: <str>
            ebgp_multihop: <int>
            local_as: <str>
            maximum_routes: <int>
            name: <str>
            next_hop_self: <bool>
            nodes:
              - <str>
            remote_as: <int>
            route_map_in: <str>
            route_map_out: <str>
            send_community: <str>
            set_ipv4_next_hop: <str>
            set_ipv6_next_hop: <str>
            update_source: <str>
            weight: <int>
        bgp_peers:
          - bfd: <bool>
            default_originate:
              always: <bool>
            description: <str>
            ebgp_multihop: <int>
            ip_address: <str>
            local_as: <str>
            maximum_routes: <int>
            next_hop_self: <bool>
            nodes:
              - <str>
            password: <str>
            prefix_list_in: <str>
            prefix_list_out: <str>
            remote_as: <int>
            route_map_in: <str>
            route_map_out: <str>
            send_community: <str>
            set_ipv4_next_hop: <str>
            set_ipv6_next_hop: <str>
            timers: <str>
            update_source: <str>
            weight: <int>
        description: <str>
        enable_mlag_ibgp_peering_vrfs: <bool>
        ip_helpers:
          - ip_helper: <str>
            source_interface: <str>
            source_vrf: <str>
        ipv6_static_routes:
          - destination_address_prefix: <str>
            distance: <int>
            gateway: <str>
            interface: <str>
            metric: <int>
            name: <str>
            nodes:
              - <str>
            tag: <int>
        l3_interfaces:
          - description: <str>
            descriptions:
              - <str>
            enabled: <bool>
            interfaces:
              - <str>
            ip_addresses:
              - <str>
            mtu: <int>
            nodes:
              - <str>
            ospf:
              area: <int>
              authentication: <str>
              cost: <int>
              enabled: <bool>
              message_digest_keys:
                - hash_algorithm: <str>
                  id: <int>
                  key: <str>
              point_to_point: <bool>
              simple_auth_key: <str>
            raw_eos_cli: <str>
            structured_config:
        mlag_ibgp_peering_ipv4_pool: <str>
        mlag_ibgp_peering_vlan: <int>
        name: <str>
        ospf:
          bfd: <bool>
          enabled: <bool>
          max_lsa: <int>
          nodes:
            - <str>
          process_id: <int>
          redistribute_bgp:
            enabled: <bool>
            route_map: <str>
          router_id: <str>
        raw_eos_cli: <str>
        redistribute_ospf: <bool>
        redistribute_static: <bool>
        static_routes:
          - destination_address_prefix: <str>
            distance: <int>
            gateway: <str>
            interface: <str>
            metric: <int>
            name: <str>
            nodes:
              - <str>
            tag: <int>
        structured_config:
        svis:
          - bgp:
              raw_eos_cli: <str>
              structured_config:
            description: <str>
            enabled: <bool>
            evpn_l2_multicast: <bool>
            id: <int>
            igmp_snooping_enabled: <bool>
            igmp_snooping_querier:
              enabled: <bool>
              source_address: <str>
              version: <int>
            ip_address_virtual: <str>
            ip_address_virtual_secondaries:
              - <str>
            ip_helpers:
              - ip_helper: <str>
                source_interface: <str>
                source_vrf: <str>
            ip_virtual_router_addresses:
              - <str>
            ipv6_address_virtual: <str>
            ipv6_address_virtuals:
              - <str>
            ipv6_virtual_router_addresses: <str>
            mtu: <int>
            name: <str>
            nodes:
              - ip_address: <str>
                ip_address_virtual_secondaries:
                  - <str>
                ip_helpers:
                  - ip_helper: <str>
                    source_interface: <str>
                    source_vrf: <str>
                ip_virtual_router_addresses:
                  - <str>
                ipv6_address: <str>
                node: <str>
                raw_eos_cli: <str>
                structured_config:
            ospf:
              area: <int>
              authentication: <str>
              cost: <int>
              enabled: <bool>
              message_digest_keys:
                - hash_algorithm: <str>
                  id: <int>
                  key: <str>
              point_to_point: <bool>
              simple_auth_key: <str>
            profile: <str>
            raw_eos_cli: <str>
            rt_override: <int>
            structured_config:
            tags:
              - <str>
            trunk_groups:
              - <str>
            vni_override: <int>
            vxlan: <bool>
        vrf_id: <int>
        vrf_vni: <int>
        vtep_diagnostic:
          loopback: <int>
          loopback_ip_pools:
            - ipv4_pool: <str>
              pod: <str>
          loopback_ip_range: <str>
```

## Network Services Keys

### Description

Define network services keys, to define grouping of network services.
This provides the ability to define various keys of your choice to better organize/group your data.
This should be defined in top level group_var for the fabric.

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>network_services_keys</samp>](## "network_services_keys") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;- name</samp>](## "network_services_keys.[].name") | String | Required, Unique |  |  |  |

### YAML

```yaml
network_services_keys:
  - name: <str>
```

## Node Type Keys

### Description

Define Node Type Keys, to specify the properties of each node type in the fabric
This allows for complete customization of the fabric layout.
This should be defined in top level group_var for the fabric.

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>node_type_keys</samp>](## "node_type_keys") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;- connected_endpoints</samp>](## "node_type_keys.[].connected_endpoints") | Boolean |  | False |  | Are endpoints connected to this node type |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;default_evpn_role</samp>](## "node_type_keys.[].default_evpn_role") | String |  | none | Valid Values:<br>- none<br>- client<br>- server | Default evpn_role. Can be overridden in topology vars. |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;default_underlay_routing_protocol</samp>](## "node_type_keys.[].default_underlay_routing_protocol") | String |  | ebgp |  | Set the default underlay routing_protocol.<br>Can be overridden by setting "underlay_routing_protocol" host/group_vars<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;interface_descriptions</samp>](## "node_type_keys.[].interface_descriptions") | Dictionary |  |  |  | Override interface_descriptions templates<br>If description templates use Jinja2, they have to strip whitespaces using {%- -%} on any code blocks<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;connected_endpoints_ethernet_interfaces</samp>](## "node_type_keys.[].interface_descriptions.connected_endpoints_ethernet_interfaces") | String |  |  |  | Path to J2 template - default inherited from templates.interface_descriptions.connected_endpoints_ethernet_interfaces |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;connected_endpoints_port_channel_interfaces</samp>](## "node_type_keys.[].interface_descriptions.connected_endpoints_port_channel_interfaces") | String |  |  |  | Path to J2 template - default inherited from templates.interface_descriptions.connected_endpoints_port_channel_interfaces |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;overlay_loopback_interface</samp>](## "node_type_keys.[].interface_descriptions.overlay_loopback_interface") | String |  |  |  | Path to J2 template - default inherited from templates.interface_descriptions.overlay_loopback_interface |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;underlay_ethernet_interfaces</samp>](## "node_type_keys.[].interface_descriptions.underlay_ethernet_interfaces") | String |  |  |  | Path to J2 template - default inherited from templates.interface_descriptions.underlay_ethernet_interfaces |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;underlay_ethernet_mlag_interfaces</samp>](## "node_type_keys.[].interface_descriptions.underlay_ethernet_mlag_interfaces") | String |  |  |  | Path to J2 template - default inherited from templates.interface_descriptions.underlay_ethernet_mlag_interfaces |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;underlay_port_channel_interfaces</samp>](## "node_type_keys.[].interface_descriptions.underlay_port_channel_interfaces") | String |  |  |  | Path to J2 template - default inherited from templates.interface_descriptions.underlay_port_channel_interfaces |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;underlay_port_channel_mlag_interfaces</samp>](## "node_type_keys.[].interface_descriptions.underlay_port_channel_mlag_interfaces") | String |  |  |  | Path to J2 template - default inherited from templates.interface_descriptions.underlay_port_channel_mlag_interfaces |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vtep_loopback_interface</samp>](## "node_type_keys.[].interface_descriptions.vtep_loopback_interface") | String |  |  |  | Path to J2 template - default inherited from templates.interface_descriptions.vtep_loopback_interface |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_addressing</samp>](## "node_type_keys.[].ip_addressing") | Dictionary |  |  |  | Override ip_addressing templates |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_ip_primary</samp>](## "node_type_keys.[].ip_addressing.mlag_ip_primary") | String |  |  |  | Path to J2 template - default inherited from templates.ip_addressing.mlag_ip_primary |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_ip_secondary</samp>](## "node_type_keys.[].ip_addressing.mlag_ip_secondary") | String |  |  |  | Path to J2 template - default inherited from templates.ip_addressing.mlag_ip_secondary |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_l3_ip_primary</samp>](## "node_type_keys.[].ip_addressing.mlag_l3_ip_primary") | String |  |  |  | Path to J2 template - default inherited from templates.ip_addressing.mlag_l3_ip_primary |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_l3_ip_secondary</samp>](## "node_type_keys.[].ip_addressing.mlag_l3_ip_secondary") | String |  |  |  | Path to J2 template - default inherited from templates.ip_addressing.mlag_l3_ip_secondary |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;p2p_uplinks_ip</samp>](## "node_type_keys.[].ip_addressing.p2p_uplinks_ip") | String |  |  |  | Path to J2 template - default inherited from templates.ip_addressing.p2p_uplinks_ip |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;p2p_uplinks_peer_ip</samp>](## "node_type_keys.[].ip_addressing.p2p_uplinks_peer_ip") | String |  |  |  | Path to J2 template - default inherited from templates.ip_addressing.p2p_uplinks_peer_ip |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;router_id</samp>](## "node_type_keys.[].ip_addressing.router_id") | String |  |  |  | Path to J2 template - default inherited from templates.ip_addressing.router_id |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vtep_ip</samp>](## "node_type_keys.[].ip_addressing.vtep_ip") | String |  |  |  | Path to J2 template - default inherited from templates.ip_addressing.vtep_ip |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vtep_ip_mlag</samp>](## "node_type_keys.[].ip_addressing.vtep_ip_mlag") | String |  |  |  | Path to J2 template - default inherited from templates.ip_addressing.vtep_ip_mlag |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;key</samp>](## "node_type_keys.[].key") | String | Required, Unique |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mlag_support</samp>](## "node_type_keys.[].mlag_support") | Boolean |  | False |  | Can this node type support mlag |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mpls_lsr</samp>](## "node_type_keys.[].mpls_lsr") | Boolean |  | False |  | Is this switch an MPLS LSR |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;network_services</samp>](## "node_type_keys.[].network_services") | Dictionary |  |  |  | Will network services be deployed on this node type |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;l2</samp>](## "node_type_keys.[].network_services.l2") | Boolean |  | False |  | Vlans |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;l3</samp>](## "node_type_keys.[].network_services.l3") | Boolean |  | False |  | VRFs, SVIs (if l2 is true)<br>Only supported with underlay_router<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "node_type_keys.[].type") | String |  |  |  | Type value matching this node_type_key |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;underlay_router</samp>](## "node_type_keys.[].underlay_router") | Boolean |  | True |  | Is this node type a L3 device |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;uplink_type</samp>](## "node_type_keys.[].uplink_type") | String |  | p2p | Valid Values:<br>- p2p<br>- port-channel | Uplinks must be p2p if "vtep" or "underlay_router" is true. |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vtep</samp>](## "node_type_keys.[].vtep") | Boolean |  | False |  | Is this switch an EVPN VTEP |

### YAML

```yaml
node_type_keys:
  - connected_endpoints: <bool>
    default_evpn_role: <str>
    default_underlay_routing_protocol: <str>
    interface_descriptions:
      connected_endpoints_ethernet_interfaces: <str>
      connected_endpoints_port_channel_interfaces: <str>
      overlay_loopback_interface: <str>
      underlay_ethernet_interfaces: <str>
      underlay_ethernet_mlag_interfaces: <str>
      underlay_port_channel_interfaces: <str>
      underlay_port_channel_mlag_interfaces: <str>
      vtep_loopback_interface: <str>
    ip_addressing:
      mlag_ip_primary: <str>
      mlag_ip_secondary: <str>
      mlag_l3_ip_primary: <str>
      mlag_l3_ip_secondary: <str>
      p2p_uplinks_ip: <str>
      p2p_uplinks_peer_ip: <str>
      router_id: <str>
      vtep_ip: <str>
      vtep_ip_mlag: <str>
    key: <str>
    mlag_support: <bool>
    mpls_lsr: <bool>
    network_services:
      l2: <bool>
      l3: <bool>
    type: <str>
    underlay_router: <bool>
    uplink_type: <str>
    vtep: <bool>
```

## Only Local VLAN Trunk Groups

### Description

A vlan can have many trunk_groups assigned. To avoid unneeded configuration changes on all leaf
switches when a new trunk group is added, this feature will only configure the vlan trunk groups
matched with local connected_endpoints.
See "Details on only_local_vlan_trunk_groups" below.
Requires "enable_trunk_groups: true"

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>only_local_vlan_trunk_groups</samp>](## "only_local_vlan_trunk_groups") | Boolean |  | False |  |  |

### YAML

```yaml
only_local_vlan_trunk_groups: <bool>
```

## Overlay Her Flood List Per Vni

### Description

When using Head-End Replication, configure flood-lists per VNI. | Optional
By default HER will be configured with a common flood-list containing all VTEPs. This behavior can be changed
to per-VNI flood-lists by setting `overlay_her_flood_list_per_vni: true`. This will make `eos_designs` consider
configured VLANs per VTEP, and only include the relevant VTEPs to each VNI's flood-list.

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>overlay_her_flood_list_per_vni</samp>](## "overlay_her_flood_list_per_vni") | Boolean |  | False |  |  |

### YAML

```yaml
overlay_her_flood_list_per_vni: <bool>
```

## Overlay Her Flood List Scope

### Description

When using Head-End Replication, set the scope of flood-lists to Fabric or DC
By default all VTEPs in the Fabric (part of the inventory group referenced by "fabric_name") are added
to the flood-lists. This can be changed to all VTEPs in the DC (part of the inventory group referenced
by "dc_name")
This is useful if Border Leaf switches are dividing the VXLAN overlay into separate domains.

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>overlay_her_flood_list_scope</samp>](## "overlay_her_flood_list_scope") | String |  | fabric | Valid Values:<br>- fabric<br>- dc |  |

### YAML

```yaml
overlay_her_flood_list_scope: <str>
```

## Overlay Loopback Description

### Description

Customizable overlay loopback description
### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>overlay_loopback_description</samp>](## "overlay_loopback_description") | String |  |  |  |  |

### YAML

```yaml
overlay_loopback_description: <str>
```

## Overlay MLAG Rfc5549

### Description

IPv6 Unnumbered for MLAG iBGP connections.
Requires "underlay_rfc5549: true"

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>overlay_mlag_rfc5549</samp>](## "overlay_mlag_rfc5549") | Boolean |  | False |  |  |

### YAML

```yaml
overlay_mlag_rfc5549: <bool>
```

## Overlay Rd Type

### Description

Specify RD type
Route Distinguisher (RD) for L2 / L3 services is set to <overlay_loopback>:<vni> per default.
By configuring overlay_rd_type the Administrator subfield (first part of RD) can be set to other values.

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>overlay_rd_type</samp>](## "overlay_rd_type") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;admin_subfield</samp>](## "overlay_rd_type.admin_subfield") | String |  |  |  | < "vtep_loopback" or "bgp_as" or < IPv4 Address > or <0-65535> or <0-4294967295>, default -> <overlay_loopback_ip> > |

### YAML

```yaml
overlay_rd_type:
  admin_subfield: <str>
```

## Overlay Routing Protocol

### Description

- The following overlay routing protocols are supported:
  - EBGP (default for l3ls-evpn)
  - IBGP (only with OSPF or ISIS variants in underlay)

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>overlay_routing_protocol</samp>](## "overlay_routing_protocol") | String |  | ebgp | Valid Values:<br>- ebgp<br>- ibgp<br>- BGP |  |

### YAML

```yaml
overlay_routing_protocol: <str>
```

## Overlay Routing Protocol Address Family

### Description

Enable overlay EVPN peering with IPv6 addresses | Optional
This feature depends on underlay_ipv6 variable. As of today, only RFC5549 is capable to transport IPv6 in the underlay.

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>overlay_routing_protocol_address_family</samp>](## "overlay_routing_protocol_address_family") | String |  | ipv4 | Valid Values:<br>- ipv4<br>- ipv6 |  |

### YAML

```yaml
overlay_routing_protocol_address_family: <str>
```

## Overlay Rt Type

### Description

Specify RT type
Route Target (RT) for L2 / L3 services is set to <vni>:<vni> per default
By configuring overlay_rt_type the Administrator subfield (first part of RT) can be set to other values.
Note: structured configuration is not merged recursively and will be taken directly from the most specific level in the following order:
1. svi.nodes[inventory_hostname].structured_config
2. svi_profile.nodes[inventory_hostname].structured_config
3. svi_parent_profile.nodes[inventory_hostname].structured_config
4. svi.structured_config
5. svi_profile.structured_config
6. svi_parent_profile.structured_config

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>overlay_rt_type</samp>](## "overlay_rt_type") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;admin_subfield</samp>](## "overlay_rt_type.admin_subfield") | String |  |  |  | < "bgp_as" or <0-65535> or <0-4294967295>, default -> <mac_vrf_id> > |

### YAML

```yaml
overlay_rt_type:
  admin_subfield: <str>
```

## P2P Uplinks MTU

### Description

Point to Point Links MTU
### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>p2p_uplinks_mtu</samp>](## "p2p_uplinks_mtu") | Integer |  | 9000 | Min: 0<br>Max: 9216 |  |

### YAML

```yaml
p2p_uplinks_mtu: <int>
```

## P2P Uplinks QOS Profile

### Description

QOS Profile assigned on all infrastructure links
### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>p2p_uplinks_qos_profile</samp>](## "p2p_uplinks_qos_profile") | String |  |  |  |  |

### YAML

```yaml
p2p_uplinks_qos_profile: <str>
```

## Platform Settings

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>platform_settings</samp>](## "platform_settings") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;- feature_support</samp>](## "platform_settings.[].feature_support") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interface_storm_control</samp>](## "platform_settings.[].feature_support.interface_storm_control") | Boolean |  | True |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;queue_monitor_length_notify</samp>](## "platform_settings.[].feature_support.queue_monitor_length_notify") | Boolean |  | True |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;lag_hardware_only</samp>](## "platform_settings.[].lag_hardware_only") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;management_interface</samp>](## "platform_settings.[].management_interface") | String |  | Management1 |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;platforms</samp>](## "platform_settings.[].platforms") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "platform_settings.[].platforms.[].&lt;str&gt;") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "platform_settings.[].raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the root level of the final EOS configuration |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;reload_delay</samp>](## "platform_settings.[].reload_delay") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag</samp>](## "platform_settings.[].reload_delay.mlag") | Integer |  |  |  | In seconds |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;non_mlag</samp>](## "platform_settings.[].reload_delay.non_mlag") | Integer |  |  |  | In seconds |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;tcam_profile</samp>](## "platform_settings.[].tcam_profile") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;trident_forwarding_table_partition</samp>](## "platform_settings.[].trident_forwarding_table_partition") | String |  |  |  | Only applied when evpn_multicast is true |

### YAML

```yaml
platform_settings:
  - feature_support:
      interface_storm_control: <bool>
      queue_monitor_length_notify: <bool>
    lag_hardware_only: <bool>
    management_interface: <str>
    platforms:
      - <str>
    raw_eos_cli: <str>
    reload_delay:
      mlag: <int>
      non_mlag: <int>
    tcam_profile: <str>
    trident_forwarding_table_partition: <str>
```

## Platform Speed Groups

### Description

Set Hardware Speed Groups per Platform
### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>platform_speed_groups</samp>](## "platform_speed_groups") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;- platform</samp>](## "platform_speed_groups.[].platform") | String | Required, Unique |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;speeds</samp>](## "platform_speed_groups.[].speeds") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- speed</samp>](## "platform_speed_groups.[].speeds.[].speed") | String | Required, Unique |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;speed_groups</samp>](## "platform_speed_groups.[].speeds.[].speed_groups") | List, items: Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;int&gt;</samp>](## "platform_speed_groups.[].speeds.[].speed_groups.[].&lt;int&gt;") | Integer |  |  |  |  |

### YAML

```yaml
platform_speed_groups:
  - platform: <str>
    speeds:
      - speed: <str>
        speed_groups:
          - <int>
```

## Pod Name

### Description

POD Name, only used in Fabric Documentation (Optional), fallback to dc_name and then to fabric_name.
Recommended to be common between Spines, Leafs within a POD (One l3ls topology)

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>pod_name</samp>](## "pod_name") | String |  |  |  |  |

### YAML

```yaml
pod_name: <str>
```

## Redundancy

### Description

Redundancy for chassis platforms with dual supervisors | Optional
### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>redundancy</samp>](## "redundancy") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;protocol</samp>](## "redundancy.protocol") | String |  |  | Valid Values:<br>- sso<br>- rpr |  |

### YAML

```yaml
redundancy:
  protocol: <str>
```

## Shutdown Interfaces Towards Undeployed Peers

### Description

- It is possible to provision configurations for a complete topology but flag devices as undeployed using the host level variable `is_deployed: false`.

```yaml
# Use at the host level
is_deployed: < true or false or default -> true >
```

- By default, this will have no impact within the `eos_designs` role. Configs will still be generated by the `eos_cli_config_gen` role and will still be pushed by the `eos_config_deploy_eapi` directly to devices if used.
- However, if the `eos_config_deploy_cvp` role is used to push configurations, CloudVision will ignore the devices flagged  as `is_deployed: false` and not attempt to configure them.
- If the device is not present in the network due to CloudVision not configuring the device, `eos_validate_state` role will fail tests on peers of the undeployed device trying to verify that interfaces are up.
- To overcome this and shutdown interfaces towards undeployed peers, the variable `shutdown_interfaces_towards_undeployed_peers` can be used, satisfying the `eos_validate_state` role interface tests. Again, this is only an issue if `eos_config_deploy_cvp` is used and the devices are not present in the network.
### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>shutdown_interfaces_towards_undeployed_peers</samp>](## "shutdown_interfaces_towards_undeployed_peers") | Boolean |  | False |  |  |

### YAML

```yaml
shutdown_interfaces_towards_undeployed_peers: <bool>
```

## Snmp Settings

### Description

Set SNMP settings. It is optional.
### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>snmp_settings</samp>](## "snmp_settings") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;compute_local_engineid</samp>](## "snmp_settings.compute_local_engineid") | Boolean |  | False |  | Generate a local engineId for SNMP by hashing via SHA1 the string<br>generated via the concatenation of the hostname plus the management IP.<br>{{ inventory_hostname }} + {{ switch.mgmt_ip }}<br> |
| [<samp>&nbsp;&nbsp;compute_v3_user_localized_key</samp>](## "snmp_settings.compute_v3_user_localized_key") | Boolean |  | False |  | Requires compute_local_engineid to be `true` if enabled, the SNMPv3<br>passphrases for auth and priv are transfromed using RFC 2574,<br>matching the value they would take in EOS cli the algorithm requires<br>a local engineId which is unknown to AVD hence the necessity to generate<br>one beforehand.<br> |
| [<samp>&nbsp;&nbsp;contact</samp>](## "snmp_settings.contact") | String |  |  |  | SNMP contact |
| [<samp>&nbsp;&nbsp;location</samp>](## "snmp_settings.location") | Boolean |  | False |  | SNMP location. Formatted as {{ fabric_name }} {{ dc_name }} {{ pod_name }} {{ switch_rack }} {{ inventory_hostname }} |
| [<samp>&nbsp;&nbsp;users</samp>](## "snmp_settings.users") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- auth</samp>](## "snmp_settings.users.[].auth") | String |  |  | Valid Values:<br>- md5<br>- sha<br>- sha256<br>- sha384<br>- sha512 | It is optional |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;auth_passphrase</samp>](## "snmp_settings.users.[].auth_passphrase") | String |  |  |  | Clear passphrase, requires auth, recommended to use vault |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;group</samp>](## "snmp_settings.users.[].group") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "snmp_settings.users.[].name") | String |  |  |  | Username |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priv</samp>](## "snmp_settings.users.[].priv") | String |  |  | Valid Values:<br>- des<br>- aes<br>- aes192<br>- aes256 | It is optional |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priv_passphrase</samp>](## "snmp_settings.users.[].priv_passphrase") | String |  |  |  | Clear pasphrase, requires priv, recommended to use vault |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;version</samp>](## "snmp_settings.users.[].version") | String |  |  | Valid Values:<br>- v1<br>- v2c<br>- v3 |  |

### YAML

```yaml
snmp_settings:
  compute_local_engineid: <bool>
  compute_v3_user_localized_key: <bool>
  contact: <str>
  location: <bool>
  users:
    - auth: <str>
      auth_passphrase: <str>
      group: <str>
      name: <str>
      priv: <str>
      priv_passphrase: <str>
      version: <str>
```

## Svi Profiles

### Description

Optional profiles to apply on SVI interfaces
Each profile can support all or some of the following keys according to your own needs.
Keys are the same used under SVI.
Svi_profiles can refer to another svi_profiles to inherit settings in up to two levels (svi->profile->parent_profile).

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>svi_profiles</samp>](## "svi_profiles") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;- enabled</samp>](## "svi_profiles.[].enabled") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;igmp_snooping_enabled</samp>](## "svi_profiles.[].igmp_snooping_enabled") | Boolean |  | True |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_address_virtual</samp>](## "svi_profiles.[].ip_address_virtual") | String |  |  |  | IPv4_address/Mask |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_address_virtual_secondaries</samp>](## "svi_profiles.[].ip_address_virtual_secondaries") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "svi_profiles.[].ip_address_virtual_secondaries.[].&lt;str&gt;") | String |  |  |  | IPv4_address/Mask |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_helpers</samp>](## "svi_profiles.[].ip_helpers") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- ip_helper</samp>](## "svi_profiles.[].ip_helpers.[].ip_helper") | String |  |  |  | IPv4 DHCP server IP |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_interface</samp>](## "svi_profiles.[].ip_helpers.[].source_interface") | String |  |  |  | Interface name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_vrf</samp>](## "svi_profiles.[].ip_helpers.[].source_vrf") | String |  |  |  | VRF to originate DHCP relay packets to DHCP server |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_virtual_router_addresses</samp>](## "svi_profiles.[].ip_virtual_router_addresses") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "svi_profiles.[].ip_virtual_router_addresses.[].&lt;str&gt;") | String |  |  |  | IPv4_address/Mask or IPv4_address |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mtu</samp>](## "svi_profiles.[].mtu") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "svi_profiles.[].name") | String |  |  |  | VLAN name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "svi_profiles.[].nodes") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- ip_address</samp>](## "svi_profiles.[].nodes.[].ip_address") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_address_virtual_secondaries</samp>](## "svi_profiles.[].nodes.[].ip_address_virtual_secondaries") | List, items: String |  |  |  | Should take config from svis[svi].nodes[node] |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "svi_profiles.[].nodes.[].ip_address_virtual_secondaries.[].&lt;str&gt;") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_helpers</samp>](## "svi_profiles.[].nodes.[].ip_helpers") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- ip_helper</samp>](## "svi_profiles.[].nodes.[].ip_helpers.[].ip_helper") | String |  |  |  | IPv4 DHCP server IP |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_interface</samp>](## "svi_profiles.[].nodes.[].ip_helpers.[].source_interface") | String |  |  |  | Interface name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_vrf</samp>](## "svi_profiles.[].nodes.[].ip_helpers.[].source_vrf") | String |  |  |  | VRF to originate DHCP relay packets to DHCP server |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_virtual_router_addresses</samp>](## "svi_profiles.[].nodes.[].ip_virtual_router_addresses") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "svi_profiles.[].nodes.[].ip_virtual_router_addresses.[].&lt;str&gt;") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_address</samp>](## "svi_profiles.[].nodes.[].ipv6_address") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_virtual_router_addresses</samp>](## "svi_profiles.[].nodes.[].ipv6_virtual_router_addresses") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "svi_profiles.[].nodes.[].ipv6_virtual_router_addresses.[].&lt;str&gt;") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "svi_profiles.[].nodes.[].name") | String | Required, Unique |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;parent_profile</samp>](## "svi_profiles.[].parent_profile") | String |  |  |  | SVI profile name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;profile</samp>](## "svi_profiles.[].profile") | String | Required, Unique |  |  | Profile name |

### YAML

```yaml
svi_profiles:
  - enabled: <bool>
    igmp_snooping_enabled: <bool>
    ip_address_virtual: <str>
    ip_address_virtual_secondaries:
      - <str>
    ip_helpers:
      - ip_helper: <str>
        source_interface: <str>
        source_vrf: <str>
    ip_virtual_router_addresses:
      - <str>
    mtu: <int>
    name: <str>
    nodes:
      - ip_address: <str>
        ip_address_virtual_secondaries:
          - <str>
        ip_helpers:
          - ip_helper: <str>
            source_interface: <str>
            source_vrf: <str>
        ip_virtual_router_addresses:
          - <str>
        ipv6_address: <str>
        ipv6_virtual_router_addresses:
          - <str>
        name: <str>
    parent_profile: <str>
    profile: <str>
```

## TerminAttr Disable AAA

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>terminattr_disable_aaa</samp>](## "terminattr_disable_aaa") | Boolean |  | False |  |  |

### YAML

```yaml
terminattr_disable_aaa: <bool>
```

## TerminAttr Ingestexclude

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>terminattr_ingestexclude</samp>](## "terminattr_ingestexclude") | String |  | /Sysdb/cell/1/agent,/Sysdb/cell/2/agent |  |  |

### YAML

```yaml
terminattr_ingestexclude: <str>
```

## TerminAttr Ingestgrpcurl Port

### Description

Port number
### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>terminattr_ingestgrpcurl_port</samp>](## "terminattr_ingestgrpcurl_port") | Integer |  | 9910 |  |  |

### YAML

```yaml
terminattr_ingestgrpcurl_port: <int>
```

## TerminAttr Smashexcludes

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>terminattr_smashexcludes</samp>](## "terminattr_smashexcludes") | String |  | ale,flexCounter,hardware,kni,pulse,strata |  |  |

### YAML

```yaml
terminattr_smashexcludes: <str>
```

## Timezone

### Description

Clock timezone is optional
### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>timezone</samp>](## "timezone") | String |  |  |  |  |

### YAML

```yaml
timezone: <str>
```

## Trunk Groups

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>trunk_groups</samp>](## "trunk_groups") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;mlag</samp>](## "trunk_groups.mlag") | Dictionary |  |  |  | "mlag" is the Trunk Group used for MLAG VLAN (Typically VLAN 4094)<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "trunk_groups.mlag.name") | String |  | MLAG |  |  |
| [<samp>&nbsp;&nbsp;mlag_l3</samp>](## "trunk_groups.mlag_l3") | Dictionary |  |  |  | "mlag_l3" is the Trunk Group used for MLAG L3 peering VLAN (Typically VLAN 4093)<br>"mlag_l3" is also the Trunk Group used for VRF L3 peering VLANs<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "trunk_groups.mlag_l3.name") | String |  | LEAF_PEER_L3 |  |  |
| [<samp>&nbsp;&nbsp;uplink</samp>](## "trunk_groups.uplink") | Dictionary |  |  |  | "uplink" is the Trunk Group used on L2 Leaf switches when "enable_trunk_groups" is set<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "trunk_groups.uplink.name") | String |  | UPLINK |  |  |

### YAML

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

### Description

The `type:` variable needs to be defined for each device in the fabric.
This is leveraged to load the appropriate template to generate the configuration.

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>type</samp>](## "type") | String | Required |  | Valid Values:<br>- <value(s) of node_type_keys.type> |  |

### YAML

```yaml
type: <str>
```

## Underlay Filter Peer As

### Description

Configure route-map on eBGP sessions towards underlay peers, where prefixes with the peer's ASN in the AS Path are filtered away.
This is very useful in very large scale networks not using EVPN overlays, where convergence will be quicker by not having to return
all updates received from Spine-1 to Spine-2 just for Spine-2 to throw them away because of AS Path loop detection.
Note this key is ignored when EVPN is configured.

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>underlay_filter_peer_as</samp>](## "underlay_filter_peer_as") | Boolean |  | False |  |  |

### YAML

```yaml
underlay_filter_peer_as: <bool>
```

## Underlay IPv6

### Description

This feature allows IPv6 underlay routing protocol with RFC5549 addresses to be used along with IPv4 advertisements as VXLAN tunnel endpoints.
Requires "underlay_rfc5549: true" and "loopback_ipv6_pool" under the "Fabric Topology"

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>underlay_ipv6</samp>](## "underlay_ipv6") | Boolean |  | False |  |  |

### YAML

```yaml
underlay_ipv6: <bool>
```

## Underlay ISIS Instance Name

### Description

Additional underlay ISIS parameters
### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>underlay_isis_instance_name</samp>](## "underlay_isis_instance_name") | String |  | EVPN_UNDERLAY |  |  |

### YAML

```yaml
underlay_isis_instance_name: <str>
```

## Underlay Multicast

### Description

Enable Multicast in the underlay on all p2p uplink interfaces and mlag l3 peer interface.
Specifically PIM Sparse-Mode will be configured on all routed underlay interfaces.
No other configuration is added, so the underlay will only support Source-Specific Multicast (SSM)
The configuration is intended to be used as multicast underlay for EVPN OISM overlay

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>underlay_multicast</samp>](## "underlay_multicast") | Boolean |  | False |  |  |

### YAML

```yaml
underlay_multicast: <bool>
```

## Underlay OSPF Area

### Description

Underlay OSFP Required when < underlay_routing_protocol > == OSPF variants
### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>underlay_ospf_area</samp>](## "underlay_ospf_area") | String |  | 0.0.0.0 | Format: ipv4 |  |

### YAML

```yaml
underlay_ospf_area: <str>
```

## Underlay OSPF BFD Enable

### Description

Underlay OSFP Required when < underlay_routing_protocol > == OSPF variants
### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>underlay_ospf_bfd_enable</samp>](## "underlay_ospf_bfd_enable") | Boolean |  | False |  |  |

### YAML

```yaml
underlay_ospf_bfd_enable: <bool>
```

## Underlay OSPF Max LSA

### Description

Underlay OSFP Required when < underlay_routing_protocol > == OSPF variants
### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>underlay_ospf_max_lsa</samp>](## "underlay_ospf_max_lsa") | Integer |  | 12000 |  |  |

### YAML

```yaml
underlay_ospf_max_lsa: <int>
```

## Underlay OSPF Process ID

### Description

Underlay OSFP Required when < underlay_routing_protocol > == OSPF variants
### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>underlay_ospf_process_id</samp>](## "underlay_ospf_process_id") | Integer |  | 100 |  |  |

### YAML

```yaml
underlay_ospf_process_id: <int>
```

## Underlay Rfc5549

### Description

Point to Point Underlay with RFC 5549(eBGP), i.e. IPv6 Unnumbered
Requires "underlay_routing_protocol: ebgp"

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>underlay_rfc5549</samp>](## "underlay_rfc5549") | Boolean |  | False |  |  |

### YAML

```yaml
underlay_rfc5549: <bool>
```

## Underlay Routing Protocol

### Description

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

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>underlay_routing_protocol</samp>](## "underlay_routing_protocol") | String |  | ebgp | Valid Values:<br>- ebgp<br>- ospf<br>- isis<br>- isis-sr<br>- isis-ldp<br>- isis-sr-ldp<br>- ospf-ldp<br>- BGP |  |

### YAML

```yaml
underlay_routing_protocol: <str>
```

## Uplink PTP

### Description

Enable PTP on all infrastructure links
### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>uplink_ptp</samp>](## "uplink_ptp") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;enable</samp>](## "uplink_ptp.enable") | Boolean |  | False |  |  |

### YAML

```yaml
uplink_ptp:
  enable: <bool>
```

## Vtep Vvtep IP

### Description

IP Address used as Virtual VTEP. Will be configured as secondary IP on loopback1
This is only needed for centralized routing designs

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>vtep_vvtep_ip</samp>](## "vtep_vvtep_ip") | String |  |  | Format: ipv4_cidr |  |

### YAML

```yaml
vtep_vvtep_ip: <str>
```

## <Connected Endpoints Keys.Key>

### Description

This should be applied to group_vars or host_vars where endpoints are connecting.
<connected_endpoints_keys.key> is one of the keys under "connected_endpoints_keys"
Default keys are "servers", "firewalls", "routers", "load_balancers" and "storage_arrays".

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>&lt;connected_endpoints_keys.key&gt;</samp>](## "&lt;connected_endpoints_keys.key&gt;") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;- adapters</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters") | List, items: Dictionary |  |  |  | A list of adapter(s), group by adapters leveraging the same port-profile. |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- description</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].description") | String |  |  |  | Interface descriptions Description. |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dot1x</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].dot1x") | Dictionary |  |  |  | 802.1x |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;authentication_failure</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].dot1x.authentication_failure") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].dot1x.authentication_failure.action") | String |  |  | Valid Values:<br>- allow<br>- drop |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;allow_vlan</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].dot1x.authentication_failure.allow_vlan") | Integer |  |  | Min: 1<br>Max: 4094 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;host_mode</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].dot1x.host_mode") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].dot1x.host_mode.mode") | String |  |  | Valid Values:<br>- multi-host<br>- single-host |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;multi_host_authenticated</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].dot1x.host_mode.multi_host_authenticated") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mac_based_authentication</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].dot1x.mac_based_authentication") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;always</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].dot1x.mac_based_authentication.always") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].dot1x.mac_based_authentication.enabled") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;host_mode_common</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].dot1x.mac_based_authentication.host_mode_common") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pae</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].dot1x.pae") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].dot1x.pae.mode") | String |  |  | Valid Values:<br>- authenticator |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;port_control</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].dot1x.port_control") | String |  |  | Valid Values:<br>- auto<br>- force-authorized<br>- force-unauthorized |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;port_control_force_authorized_phone</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].dot1x.port_control_force_authorized_phone") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;reauthentication</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].dot1x.reauthentication") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;reauthorization_request_limit</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].dot1x.reauthorization_request_limit") | Integer |  |  | Min: 1<br>Max: 10 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;timeout</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].dot1x.timeout") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;idle_host</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].dot1x.timeout.idle_host") | Integer |  |  | Min: 10<br>Max: 65535 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;quiet_period</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].dot1x.timeout.quiet_period") | Integer |  |  | Min: 1<br>Max: 65535 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;reauth_period</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].dot1x.timeout.reauth_period") | String |  |  |  | Range 60-4294967295 or "server" |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;reauth_timeout_ignore</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].dot1x.timeout.reauth_timeout_ignore") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tx_period</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].dot1x.timeout.tx_period") | Integer |  |  | Min: 1<br>Max: 65535 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].enabled") | Boolean |  | True |  | Administrative state, setting to false will set port to 'shutdown' in intended configuration<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;endpoint_ports</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].endpoint_ports") | List, items: String |  |  |  | The lists "endpoint_ports", "switch_ports" and "switches" must have the same length.<br>Each list item is one switchport.<br>Endpoint port(s) is used for description, required unless description is set.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].endpoint_ports.[].&lt;str&gt;") | String |  |  |  | Interface name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ethernet_segment</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].ethernet_segment") | Dictionary |  |  |  | Settings for all- or single-active EVPN multihoming |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;designated_forwarder_algorithm</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].ethernet_segment.designated_forwarder_algorithm") | String |  |  | Valid Values:<br>- auto<br>- modulus<br>- preference | Configure DF algorithm and preferences<br>- auto: Use preference-based algorithm and assign preference based on position of device in the 'switches' list<br>   e.g. assuming a list of three switches, this would assign a preference of 200 to the first switch, 100 to the 2nd and 0 to the third<br>- preference: Set preference for each switch manually using designated_forwarder_preferences key<br>- modulus: Use the default modulus-based algorithm<br>If omitted, Port-Channels use the EOS default of modulus<br>If omitted, Ethernet interfaces default to the 'auto' mechanism detailed above<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;designated_forwarder_preferences</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].ethernet_segment.designated_forwarder_preferences") | List, items: String |  |  |  | Manual preference as described above, required only for preference algorithm |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].ethernet_segment.designated_forwarder_preferences.[].&lt;str&gt;") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dont_preempt</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].ethernet_segment.dont_preempt") | Boolean |  |  |  | Disable preemption for single-active forwarding when auto/manual DF preference is configured. |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;redundancy</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].ethernet_segment.redundancy") | String |  |  | Valid Values:<br>- all-active<br>- single-active | If omitted, Port-Channels use the EOS default of all-active<br>If omitted, Ethernet interfaces are configured as single-active<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;short_esi</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].ethernet_segment.short_esi") | String | Required |  |  | In format xxxx:xxxx:xxxx or "auto"<br>Define a manual short-esi (be careful using this on profiles) or auto-generate an ESI<br>Please see the notes under "EVPN A/A ESI dual- and single-attached endpoint scenarios" before setting short_esi: auto<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;flowcontrol</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].flowcontrol") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;received</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].flowcontrol.received") | String |  |  | Valid Values:<br>- received<br>- send<br>- on |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;l2_mtu</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].l2_mtu") | Integer |  |  |  | This should only be defined for platforms supporting the "l2 mtu" CLI |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;link_tracking</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].link_tracking") | Dictionary |  |  |  | Configure the downstream interfaces of a respective Link Tracking Group<br>If port_channel is defined in an adapter then port-channel interface is configured to be the downstream<br>else all the ethernet-interfaces will be configured as downstream -> to configure single-active EVPN multihomed networks<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].link_tracking.enabled") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].link_tracking.name") | String |  |  |  | Tracking group name<br>The default group name is taken from fabric variable of the switch, link_tracking.groups[0].name with default value being "LT_GROUP1".<br>Optional if default link_tracking settings are configured on the node.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].mode") | String |  |  | Valid Values:<br>- access<br>- dot1q-tunnel<br>- trunk | Interface mode |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;monitor_sessions</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].monitor_sessions") | List, items: Dictionary |  |  |  | Monitor Session configuration - Use defined switchports as source or destination for monitoring sessions |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].monitor_sessions.[].name") | String | Required |  |  | Session name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;role</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].monitor_sessions.[].role") | String |  |  | Valid Values:<br>- source<br>- destination |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;session_settings</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].monitor_sessions.[].session_settings") | Dictionary |  |  |  | Session settings are defined per session name. Different session_settings with for same session name will be combined/merged |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_group</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].monitor_sessions.[].session_settings.access_group") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].monitor_sessions.[].session_settings.access_group.name") | String |  |  |  | ACL Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].monitor_sessions.[].session_settings.access_group.type") | String |  |  | Valid Values:<br>- ip<br>- ipv6<br>- mac |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;encapsulation_gre_metadata_tx</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].monitor_sessions.[].session_settings.encapsulation_gre_metadata_tx") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;header_remove_size</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].monitor_sessions.[].session_settings.header_remove_size") | Integer |  |  |  | Number of bytes to remove from header |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rate_limit_per_egress_chip</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].monitor_sessions.[].session_settings.rate_limit_per_egress_chip") | String |  |  |  | Ratelimit and unit as string.<br>Examples:<br>  "100000 bps"<br>  "100 kbps"<br>  "10 mbps"<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rate_limit_per_ingress_chip</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].monitor_sessions.[].session_settings.rate_limit_per_ingress_chip") | String |  |  |  | Ratelimit and unit as string.<br>Examples:<br>  "100000 bps"<br>  "100 kbps"<br>  "10 mbps"<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sample</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].monitor_sessions.[].session_settings.sample") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;truncate</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].monitor_sessions.[].session_settings.truncate") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].monitor_sessions.[].session_settings.truncate.enabled") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;size</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].monitor_sessions.[].session_settings.truncate.size") | Integer |  |  |  | Size in bytes |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_settings</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].monitor_sessions.[].source_settings") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_group</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].monitor_sessions.[].source_settings.access_group") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].monitor_sessions.[].source_settings.access_group.name") | String |  |  |  | ACL Name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].monitor_sessions.[].source_settings.access_group.priority") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].monitor_sessions.[].source_settings.access_group.type") | String |  |  | Valid Values:<br>- ip<br>- ipv6<br>- mac |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].monitor_sessions.[].source_settings.direction") | String |  |  | Valid Values:<br>- rx<br>- tx<br>- both |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mtu</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].mtu") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;native_vlan</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].native_vlan") | Integer |  |  |  | Native VLAN for a trunk port<br>If setting both native_vlan and native_vlan_tag, native_vlan_tag takes precedence<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;native_vlan_tag</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].native_vlan_tag") | Boolean |  | False |  | If setting both native_vlan and native_vlan_tag, native_vlan_tag takes precedence |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;port_channel</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].port_channel") | Dictionary |  |  |  | Used for port-channel adapter |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;channel_id</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].port_channel.channel_id") | Integer |  |  |  | Port-Channel ID, Optional<br>If no channel_id is specified, an id is generated from the first switch port in the port channel<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].port_channel.description") | String |  |  |  | Port-Channel Description - added after endpoint name in the description, Optional |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].port_channel.enabled") | Boolean |  | True |  | Port-Channel administrative state, Optional<br>setting to false will set port to 'shutdown' in intended configuration<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;esi</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].port_channel.esi") | String |  |  |  | Format xxxx:xxxx:xxxx |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;lacp_fallback</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].port_channel.lacp_fallback") | Dictionary |  |  |  | LACP Fallback configuration |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].port_channel.lacp_fallback.mode") | String |  |  | Valid Values:<br>- static | Currently only static mode is supported |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;timeout</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].port_channel.lacp_fallback.timeout") | Integer |  |  |  | Timeout in seconds, Optional - default is 90 seconds |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].port_channel.mode") | String | Required |  | Valid Values:<br>- active<br>- passive<br>- on | Port-Channel Mode |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;short_esi</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].port_channel.short_esi") | String |  |  |  | In format xxxx:xxxx:xxxx or "auto" |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;subinterfaces</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].port_channel.subinterfaces") | List, items: Dictionary |  |  |  | Port-Channel L2 Subinterfaces<br>Subinterfaces are only supported on routed port-channels, which means they cannot be configured on MLAG port-channels.<br>Setting short_esi: auto generates the short_esi automatically using a hash of configuration elements.<br>Please see the notes under "EVPN A/A ESI dual-attached endpoint scenario" before setting short_esi: auto.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- encapsulation_vlan</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].port_channel.subinterfaces.[].encapsulation_vlan") | Dictionary |  |  |  | Client vlan id encapsulation<br>Default is subinterface number<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;client_dot1q</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].port_channel.subinterfaces.[].encapsulation_vlan.client_dot1q") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;number</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].port_channel.subinterfaces.[].number") | Integer |  |  |  | Subinterface number |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;short_esi</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].port_channel.subinterfaces.[].short_esi") | String |  |  |  | In format xxxx:xxxx:xxxx or "auto"<br>Required for multihomed port-channels with subinterfaces<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vlan_id</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].port_channel.subinterfaces.[].vlan_id") | Integer |  |  |  | VLAN ID to bridge<br>Default is subinterface number<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;profile</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].profile") | String |  |  |  | Port-profile name, to inherit configuration. |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ptp</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].ptp") | Dictionary |  |  |  | PTP Enable |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enable</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].ptp.enable") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;qos_profile</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].qos_profile") | String |  |  |  | QOS profile name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the ethernet interface in the final EOS configuration |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;server_ports</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].server_ports") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].server_ports.[].&lt;str&gt;") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;short_esi</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].short_esi") | String |  |  | Valid Values:<br>- auto | Allocates an automatic short_esi to all ports using this profile<br>Please see the notes under "EVPN A/A ESI dual-attached endpoint examples" in this document before setting short_esi: auto.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_bpdufilter</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].spanning_tree_bpdufilter") | String |  |  | Valid Values:<br>- enabled<br>- disabled<br>- True<br>- False |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_bpduguard</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].spanning_tree_bpduguard") | String |  |  | Valid Values:<br>- enabled<br>- disabled<br>- True<br>- False |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_portfast</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].spanning_tree_portfast") | String |  |  | Valid Values:<br>- edge<br>- network |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;speed</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].speed") | String |  |  |  | < interface_speed or forced interface_speed or auto interface_speed ><br>Adapter speed - if not specified will be auto.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;storm_control</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].storm_control") | Dictionary |  |  |  | Storm control settings applied on port toward the endpoint |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;all</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].storm_control.all") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;level</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].storm_control.all.level") | Integer |  |  |  | Configure maximum storm-control level |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unit</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].storm_control.all.unit") | String |  | percent | Valid Values:<br>- percent<br>- pps | Optional var and is hardware dependent |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;broadcast</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].storm_control.broadcast") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;level</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].storm_control.broadcast.level") | Integer |  |  |  | Configure maximum storm-control level |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unit</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].storm_control.broadcast.unit") | String |  | percent | Valid Values:<br>- percent<br>- pps | Optional var and is hardware dependent |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;multicast</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].storm_control.multicast") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;level</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].storm_control.multicast.level") | Integer |  |  |  | Configure maximum storm-control level |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unit</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].storm_control.multicast.unit") | String |  | percent | Valid Values:<br>- percent<br>- pps | Optional var and is hardware dependent |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unknown_unicast</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].storm_control.unknown_unicast") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;level</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].storm_control.unknown_unicast.level") | Integer |  |  |  | Configure maximum storm-control level |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unit</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].storm_control.unknown_unicast.unit") | String |  | percent | Valid Values:<br>- percent<br>- pps | Optional var and is hardware dependent |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;switch_ports</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].switch_ports") | List, items: String |  |  |  | List of switch interfac(es) |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].switch_ports.[].&lt;str&gt;") | String |  |  |  | Switchport interface |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;switches</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].switches") | List, items: String |  |  |  | List of switch(es) |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].switches.[].&lt;str&gt;") | String |  |  |  | Device |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;trunk_groups</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].trunk_groups") | List, items: String |  |  |  | Required with "enable_trunk_groups: true"<br>Trunk Groups are used for limiting vlans on trunk ports to vlans with the same Trunk Group<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].trunk_groups.[].&lt;str&gt;") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vlans</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].adapters.[].vlans") | String |  |  |  | Interface vlans - if not set, the EOS default is that all vlans are allowed for trunk ports and vlan 1 will be used for access ports. |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].name") | String | Required, Unique |  |  | Endpoint name, this will be used in the switchport description. |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;rack</samp>](## "&lt;connected_endpoints_keys.key&gt;.[].rack") | String |  |  |  | Rack is used for documentation purposes only |

### YAML

```yaml
<connected_endpoints_keys.key>:
  - adapters:
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
    name: <str>
    rack: <str>
```

## <Network Services Keys.Name>

### Variables

| Variable | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| [<samp>&lt;network_services_keys.name&gt;</samp>](## "&lt;network_services_keys.name&gt;") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;- bgp_peer_groups</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups") | List, items: Dictionary |  |  |  | Dictionary of BGP peer groups definitions (Optional).<br>This will configure BGP peer groups to be used inside the tenant VRF for peering with external devices.<br>Since BGP peer groups are configured at higher BGP level, shared between VRFs,<br>peer_group names should not overlap between VRFs.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- bfd</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups.[].bfd") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default_originate</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups.[].default_originate") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;always</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups.[].default_originate.always") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups.[].default_originate.enabled") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups.[].description") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ebgp_multihop</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups.[].ebgp_multihop") | Integer |  |  | Min: 1<br>Max: 255 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;local_as</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups.[].local_as") | String |  |  |  | Local BGP ASN<br>eg. "65001.1200"<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maximum_routes</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups.[].maximum_routes") | Integer |  |  | Min: 0<br>Max: 4294967294 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups.[].name") | String |  |  |  | BGP peer group name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;next_hop_self</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups.[].next_hop_self") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups.[].nodes") | List, items: String |  |  |  | Nodes is required to restrict configuration of BGP neighbors to certain nodes in the network.<br>If not set the peer-group is created on the device which has a bgp_peer mapped to corresponding peer_group.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups.[].nodes.[].&lt;str&gt;") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remote_as</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups.[].remote_as") | Integer |  |  |  | Remote ASN |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_in</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups.[].route_map_in") | String |  |  |  | Route-map name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_out</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups.[].route_map_out") | String |  |  |  | Route-map name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;send_community</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups.[].send_community") | String |  |  |  | 'all' or a combination of 'standard', 'extended', 'large' and 'link-bandwidth (w/options)'<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;set_ipv4_next_hop</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups.[].set_ipv4_next_hop") | String |  |  |  | IPv4_address<br>Next hop settings can be either ipv4 or ipv6 for one neighbor, this will be applied by a uniquely generated route-map per neighbor.<br>Next hop takes precedence over route_map_out.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;set_ipv6_next_hop</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups.[].set_ipv6_next_hop") | String |  |  |  | IPv6_address<br>Next hop settings can be either ipv4 or ipv6 for one neighbor, this will be applied by a uniquely generated route-map per neighbor.<br>Next hop takes precedence over route_map_out.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;update_source</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups.[].update_source") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;weight</samp>](## "&lt;network_services_keys.name&gt;.[].bgp_peer_groups.[].weight") | Integer |  |  | Min: 0<br>Max: 65535 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;enable_mlag_ibgp_peering_vrfs</samp>](## "&lt;network_services_keys.name&gt;.[].enable_mlag_ibgp_peering_vrfs") | Boolean |  |  |  | MLAG IBGP peering per VRF.<br>By default an IBGP peering is configured per VRF between MLAG peers on separate VLANs.<br>Setting enable_mlag_ibgp_peering_vrfs: false under tenant will change this default to prevent configuration of these peerings and VLANs for all VRFs in the tenant.<br>This setting can be overridden per VRF.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;evpn_l2_multicast</samp>](## "&lt;network_services_keys.name&gt;.[].evpn_l2_multicast") | Dictionary |  |  |  | Enable EVPN L2 Multicast for all SVIs and l2vlans within Tenant | Optional<br>- Multicast group binding is created only for Multicast traffic. BULL traffic will use ingress-replication<br>- Configures binding between VXLAN, VLAN, and multicast group IPv4 address using the following formula:<br>  < evpn_l2_multicast.underlay_l2_multicast_group_ipv4_pool > + < vlan_id - 1 > + < evpn_l2_multicast.underlay_l2_multicast_group_ipv4_pool_offset >.<br>- The recommendation is to assign a /20 block within the 232.0.0.0/8 Source-Specific Multicast range.<br>- Enables `redistribute igmp` on the router bgp MAC VRF.<br>- When evpn_l2_multicast.enabled is true for a VLAN or a tenant, "igmp snooping" and "igmp snooping querier" will always be enabled - overriding those individual settings.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;network_services_keys.name&gt;.[].evpn_l2_multicast.enabled") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;underlay_l2_multicast_group_ipv4_pool</samp>](## "&lt;network_services_keys.name&gt;.[].evpn_l2_multicast.underlay_l2_multicast_group_ipv4_pool") | String |  |  |  | IPv4_address/Mask |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;underlay_l2_multicast_group_ipv4_pool_offset</samp>](## "&lt;network_services_keys.name&gt;.[].evpn_l2_multicast.underlay_l2_multicast_group_ipv4_pool_offset") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;evpn_l3_multicast</samp>](## "&lt;network_services_keys.name&gt;.[].evpn_l3_multicast") | Dictionary |  |  |  | Enable L3 Multicast for all SVIs and l3vlans within Tenant | Optional<br>- In the evpn-l3ls design type, this enables L3 EVPN Multicast (aka OISM)<br>- Multicast group binding for VRF is created only for Multicast traffic. BULL traffic will use ingress-replication<br>- Configures binding between VXLAN, VLAN, and multicast group IPv4 address using the following formula:<br>  < l3_multicast.evpn_underlay_l3_multicast_group_ipv4_pool > + < vrf_vni - 1 > + < l3_multicast.evpn_underlay_l3_multicast_group_ipv4_pool_offset >.<br>- The recommendation is to assign a /20 block within the 232.0.0.0/8 Source-Specific Multicast range.<br>- If enabled on an SVI using the anycast default gateway feature, a diagnostic loopback (see below) MUST be configured to source IGMP traffic.<br>- Enables `evpn multicast` on the router bgp VRF.<br>- When enabled on an SVI:<br>     - If switch is part of an MLAG pair, enables "pim ipv4 sparse-mode" on the SVI.<br>     - If switch is standalone or A-A MH, enables "ip igmp" on the SVI.<br>     - If "ip address virtual" is configured, enables "pim ipv4 local-interface" and uses the diagnostic Loopback defined in the VRF<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;network_services_keys.name&gt;.[].evpn_l3_multicast.enabled") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_peg</samp>](## "&lt;network_services_keys.name&gt;.[].evpn_l3_multicast.evpn_peg") | List, items: Dictionary |  |  |  | For each group of nodes, allow configuration of EVPN PEG options (Optional)<br>The first group of settings where the device's hostname is present in the 'nodes' list will be used.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- nodes</samp>](## "&lt;network_services_keys.name&gt;.[].evpn_l3_multicast.evpn_peg.[].nodes") | List, items: String |  |  |  | (Optional) will apply to all nodes with RP addresses configured if not set. |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;network_services_keys.name&gt;.[].evpn_l3_multicast.evpn_peg.[].nodes.[].&lt;str&gt;") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;transit</samp>](## "&lt;network_services_keys.name&gt;.[].evpn_l3_multicast.evpn_peg.[].transit") | Boolean |  |  |  | Enable EVPN PEG transit mode |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_underlay_l3_multicast_group_ipv4_pool</samp>](## "&lt;network_services_keys.name&gt;.[].evpn_l3_multicast.evpn_underlay_l3_multicast_group_ipv4_pool") | String | Required |  |  | IPv4_address/Mask |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_underlay_l3_multicast_group_ipv4_pool_offset</samp>](## "&lt;network_services_keys.name&gt;.[].evpn_l3_multicast.evpn_underlay_l3_multicast_group_ipv4_pool_offset") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;igmp_snooping_querier</samp>](## "&lt;network_services_keys.name&gt;.[].igmp_snooping_querier") | Dictionary |  |  |  | Enable IGMP snooping querier for each SVI/l2vlan within tenant, by default using IP address of Loopback 0.<br>When enabled, IGMP snooping querier will only be configured on L3 devices, i.e., uplink_type: p2p.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;network_services_keys.name&gt;.[].igmp_snooping_querier.enabled") | Boolean |  |  |  | Will be enabled automatically if "evpn_l2_multicast" is enabled. |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_address</samp>](## "&lt;network_services_keys.name&gt;.[].igmp_snooping_querier.source_address") | String |  |  | Format: ipv4 | Default IP address of Loopback0 |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;version</samp>](## "&lt;network_services_keys.name&gt;.[].igmp_snooping_querier.version") | Integer |  | 2 | Valid Values:<br>- 1<br>- 2<br>- 3 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;l2vlans</samp>](## "&lt;network_services_keys.name&gt;.[].l2vlans") | List, items: Dictionary |  |  |  | Define L2 network services organized by vlan id. |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- bgp</samp>](## "&lt;network_services_keys.name&gt;.[].l2vlans.[].bgp") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "&lt;network_services_keys.name&gt;.[].l2vlans.[].bgp.raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the VLAN interface in the final EOS configuration<br>Overrides the setting on SVI level |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_l2_multicast</samp>](## "&lt;network_services_keys.name&gt;.[].l2vlans.[].evpn_l2_multicast") | Boolean |  |  |  | Explicitly enable or disable evpn_l2_multicast to override setting of tenants.<tenant>.evpn_l2_multicast.enabled.<br>When evpn_l2_multicast.enabled is set to true for a vlan or a tenant, igmp snooping and igmp snooping querier will always be enabled - overriding those individual settings.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;id</samp>](## "&lt;network_services_keys.name&gt;.[].l2vlans.[].id") | Integer | Required, Unique |  | Min: 1<br>Max: 4096 | VLAN id |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;igmp_snooping_enabled</samp>](## "&lt;network_services_keys.name&gt;.[].l2vlans.[].igmp_snooping_enabled") | Boolean |  | True |  | Activate or deactivate IGMP snooping |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;igmp_snooping_querier</samp>](## "&lt;network_services_keys.name&gt;.[].l2vlans.[].igmp_snooping_querier") | Dictionary |  |  |  | Enable igmp snooping querier, by default using IP address of Loopback 0.<br>When enabled, igmp snooping querier will only be configured on l3 devices, i.e., uplink_type: p2p.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;network_services_keys.name&gt;.[].l2vlans.[].igmp_snooping_querier.enabled") | Boolean |  |  |  | Will be enabled automatically if evpn_l2_multicast is enabled. |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_address</samp>](## "&lt;network_services_keys.name&gt;.[].l2vlans.[].igmp_snooping_querier.source_address") | String |  |  |  | IPv4_address<br>If not set, IP address of "Loopback0" will be used.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;version</samp>](## "&lt;network_services_keys.name&gt;.[].l2vlans.[].igmp_snooping_querier.version") | Integer |  | 2 | Valid Values:<br>- 1<br>- 2<br>- 3 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "&lt;network_services_keys.name&gt;.[].l2vlans.[].name") | String | Required |  |  | VLAN name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rt_override</samp>](## "&lt;network_services_keys.name&gt;.[].l2vlans.[].rt_override") | Integer |  |  | Min: 1<br>Max: 16777215 | By default the MAC VRF RD/RT ID will be derived from mac_vrf_id_base<br>The rt_override allows us to override this value and statically define it (Optional)<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tags</samp>](## "&lt;network_services_keys.name&gt;.[].l2vlans.[].tags") | List, items: String |  |  |  | Tags leveraged for networks services filtering<br>Tags are matched against filter.tags defined under Fabric Topology variables<br>Tags are also matched against the node_group name under Fabric Topology variables<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;network_services_keys.name&gt;.[].l2vlans.[].tags.[].&lt;str&gt;") | String |  | all |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;trunk_groups</samp>](## "&lt;network_services_keys.name&gt;.[].l2vlans.[].trunk_groups") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;network_services_keys.name&gt;.[].l2vlans.[].trunk_groups.[].&lt;str&gt;") | String |  |  |  | Trunk groups are used for limiting vlans to trunk ports assigned to the same trunk group<br>Requires enable_trunk_groups: true<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vni_override</samp>](## "&lt;network_services_keys.name&gt;.[].l2vlans.[].vni_override") | Integer |  |  | Min: 1<br>Max: 16777215 | By default the vni will be derived from mac_vrf_vni_base<br>The vni_override, allows to override this value and statically define it.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vxlan</samp>](## "&lt;network_services_keys.name&gt;.[].l2vlans.[].vxlan") | Boolean |  | True |  | Extend this L2VLAN over VXLAN |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mac_vrf_id_base</samp>](## "&lt;network_services_keys.name&gt;.[].mac_vrf_id_base") | Integer |  |  | Min: 0<br>Max: 16770000 | If not set, "mac_vrf_vni_base" will be used.<br>Base number for MAC VRF RD/RT ID (Required unless mac_vrf_vni_base is set)<br>ID is derived from the base number with simple addition.<br>e.g. mac_vrf_id_base = 10000, svi 100 = RD/RT 10100, svi 300 = RD/RT 10300.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mac_vrf_vni_base</samp>](## "&lt;network_services_keys.name&gt;.[].mac_vrf_vni_base") | Integer |  |  | Min: 0<br>Max: 16770000 | Base number for MAC VRF VXLAN Network Identifier (Required with VXLAN)<br>VXLAN VNI is derived from the base number with simple addition.<br>e.g. mac_vrf_vni_base = 10000, svi 100 = VNI 10100, svi 300 = VNI 10300.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "&lt;network_services_keys.name&gt;.[].name") | String | Required, Unique |  |  | Specify a tenant name.<br>Tenant provide a construct to group L3 VRFs and L2 VLANs.<br>Networks services can be filtered by tenant name.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;pim_rp_addresses</samp>](## "&lt;network_services_keys.name&gt;.[].pim_rp_addresses") | List, items: Dictionary |  |  |  | For each group of nodes, allow configuration of RP Addresses & associated groups<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- groups</samp>](## "&lt;network_services_keys.name&gt;.[].pim_rp_addresses.[].groups") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;network_services_keys.name&gt;.[].pim_rp_addresses.[].groups.[].&lt;str&gt;") | String |  |  |  | Group_prefix/mask |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "&lt;network_services_keys.name&gt;.[].pim_rp_addresses.[].nodes") | List, items: String |  |  |  | (Optional) will apply to all nodes with RP addresses configured if not set. |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;network_services_keys.name&gt;.[].pim_rp_addresses.[].nodes.[].&lt;str&gt;") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rps</samp>](## "&lt;network_services_keys.name&gt;.[].pim_rp_addresses.[].rps") | List, items: String |  |  |  | A minimum of one RP must be specified |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;network_services_keys.name&gt;.[].pim_rp_addresses.[].rps.[].&lt;str&gt;") | String |  |  |  | RP address |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vlan_aware_bundle_number_base</samp>](## "&lt;network_services_keys.name&gt;.[].vlan_aware_bundle_number_base") | Integer |  | 0 |  | Base number for vlan_aware_bundle.<br>The "Assigned Number" part of RD/RT is derived from vrf_vni + vlan_aware_bundle_number_base.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vrfs</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs") | List, items: Dictionary |  |  |  | vrf "default" is supported under network-services. Currently the supported options for "default" vrf are route-target,<br>route-distinguisher settings, structured_config, raw_eos_cli in bgp and SVIs are the only supported interface type.<br>Vlan-aware-bundles are supported as well inside default vrf. OSPF is not supported currently.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- additional_route_targets</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].additional_route_targets") | List, items: Dictionary |  |  |  | Optional configuration of extra route-targets for this VRF. Useful for route-leaking or gateway between address families. |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- address_family</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].additional_route_targets.[].address_family") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].additional_route_targets.[].nodes") | List, items: String |  |  |  | Nodes is required to restrict configuration of BGP neighbors to certain nodes in the network.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].additional_route_targets.[].nodes.[].&lt;str&gt;") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_target</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].additional_route_targets.[].route_target") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].additional_route_targets.[].type") | String |  |  | Valid Values:<br>- import<br>- export |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp.raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the VLAN interface in the final EOS configuration<br>Overrides the setting on SVI level.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp.structured_config") | Dictionary |  |  |  | Custom structured config added under vlan_interfaces.<interface> for eos_cli_config_gen.<br>Overrides the setting on SVI level.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp_peer_groups</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups") | List, items: Dictionary |  |  |  | Dictionary of BGP peer groups definitions (Optional).<br>This will configure BGP peer groups to be used inside the tenant VRF for peering with external devices.<br>Since BGP peer groups are configured at higher BGP level, shared between VRFs,<br>peer_group names should not overlap between VRFs.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- bfd</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups.[].bfd") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default_originate</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups.[].default_originate") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;always</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups.[].default_originate.always") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups.[].default_originate.enabled") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups.[].description") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ebgp_multihop</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups.[].ebgp_multihop") | Integer |  |  | Min: 1<br>Max: 255 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;local_as</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups.[].local_as") | String |  |  |  | Local BGP ASN<br>eg. "65001.1200"<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maximum_routes</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups.[].maximum_routes") | Integer |  |  | Min: 0<br>Max: 4294967294 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups.[].name") | String |  |  |  | BGP peer group name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;next_hop_self</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups.[].next_hop_self") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups.[].nodes") | List, items: String |  |  |  | Nodes is required to restrict configuration of BGP neighbors to certain nodes in the network.<br>If not set the peer-group is created on the device which has a bgp_peer mapped to corresponding peer_group.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups.[].nodes.[].&lt;str&gt;") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remote_as</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups.[].remote_as") | Integer |  |  |  | Remote ASN |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_in</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups.[].route_map_in") | String |  |  |  | Route-map name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_out</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups.[].route_map_out") | String |  |  |  | Route-map name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;send_community</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups.[].send_community") | String |  |  |  | 'all' or a combination of 'standard', 'extended', 'large' and 'link-bandwidth (w/options)'<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;set_ipv4_next_hop</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups.[].set_ipv4_next_hop") | String |  |  |  | IPv4_address<br>Next hop settings can be either ipv4 or ipv6 for one neighbor, this will be applied by a uniquely generated route-map per neighbor.<br>Next hop takes precedence over route_map_out.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;set_ipv6_next_hop</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups.[].set_ipv6_next_hop") | String |  |  |  | IPv6_address<br>Next hop settings can be either ipv4 or ipv6 for one neighbor, this will be applied by a uniquely generated route-map per neighbor.<br>Next hop takes precedence over route_map_out.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;update_source</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups.[].update_source") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;weight</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peer_groups.[].weight") | Integer |  |  | Min: 0<br>Max: 65535 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp_peers</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peers") | List, items: Dictionary |  |  |  | Dictionary of BGP peer definitions (Optional).<br>This will configure BGP neighbors inside the tenant VRF for peering with external devices.<br>The configured peer will automatically be activated for ipv4 or ipv6 address family based on the ip address.<br>Note, only ipv4 and ipv6 address families are currently supported in eos_designs.<br>For other address families, use custom_structured configuration with eos_cli_config_gen.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- bfd</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peers.[].bfd") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default_originate</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peers.[].default_originate") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;always</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peers.[].default_originate.always") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peers.[].description") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ebgp_multihop</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peers.[].ebgp_multihop") | Integer |  |  | Min: 1<br>Max: 255 | Time-to-live in range of hops |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peers.[].ip_address") | String | Required, Unique |  |  | IPv4_address or IPv6_address |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;local_as</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peers.[].local_as") | String |  |  |  | Local BGP ASN<br>eg. "65001.1200"<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maximum_routes</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peers.[].maximum_routes") | Integer |  |  | Min: 0<br>Max: 4294967294 | Maximum number of routes (0 means unlimited) |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;next_hop_self</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peers.[].next_hop_self") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peers.[].nodes") | List, items: String |  |  |  | Nodes is required to restrict configuration of BGP neighbors to certain nodes in the network. |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peers.[].nodes.[].&lt;str&gt;") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;password</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peers.[].password") | String |  |  |  | Encrypted password |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefix_list_in</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peers.[].prefix_list_in") | String |  |  |  | Prefix list name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefix_list_out</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peers.[].prefix_list_out") | String |  |  |  | Prefix list name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remote_as</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peers.[].remote_as") | Integer |  |  |  | Remote ASN |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_in</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peers.[].route_map_in") | String |  |  |  | Route-map name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_out</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peers.[].route_map_out") | String |  |  |  | Route-map name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;send_community</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peers.[].send_community") | String |  |  |  | 'all' or a combination of 'standard', 'extended', 'large' and 'link-bandwidth (w/options)'<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;set_ipv4_next_hop</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peers.[].set_ipv4_next_hop") | String |  |  |  | IPv4_address<br>Next hop settings can be either ipv4 or ipv6 for one neighbor, this will be applied by a uniquely generated route-map per neighbor.<br>Next hop takes precedence over route_map_out.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;set_ipv6_next_hop</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peers.[].set_ipv6_next_hop") | String |  |  |  | IPv6_address<br>Next hop settings can be either ipv4 or ipv6 for one neighbor, this will be applied by a uniquely generated route-map per neighbor.<br>Next hop takes precedence over route_map_out.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;timers</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peers.[].timers") | String |  |  |  | BGP Keepalive and Hold Timer values in seconds as string <0-3600> <0-3600> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;update_source</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peers.[].update_source") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;weight</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].bgp_peers.[].weight") | Integer |  |  | Min: 0<br>Max: 65535 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].description") | String |  |  |  | VRF description |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enable_mlag_ibgp_peering_vrfs</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].enable_mlag_ibgp_peering_vrfs") | Boolean |  |  |  | MLAG IBGP peering per VRF (optional)<br>By default an IBGP peering is configured per VRF between MLAG peers on separate VLANs.<br>Setting enable_mlag_ibgp_peering_vrfs: false under vrf will change this default and/or override the tenant-wide setting<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_helpers</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].ip_helpers") | List, items: Dictionary |  |  |  | IP helper for DHCP relay |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- ip_helper</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].ip_helpers.[].ip_helper") | String | Required, Unique |  |  | IPv4 DHCP server IP |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_interface</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].ip_helpers.[].source_interface") | String |  |  |  | Interface name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_vrf</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].ip_helpers.[].source_vrf") | String |  |  |  | VRF to originate DHCP relay packets to DHCP server. If not set, uses current VRF |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_static_routes</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].ipv6_static_routes") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- destination_address_prefix</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].ipv6_static_routes.[].destination_address_prefix") | String |  |  |  | IPv4_address/Mask |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;distance</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].ipv6_static_routes.[].distance") | Integer |  |  | Min: 1<br>Max: 255 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;gateway</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].ipv6_static_routes.[].gateway") | String |  |  | Format: ipv6 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interface</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].ipv6_static_routes.[].interface") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;metric</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].ipv6_static_routes.[].metric") | Integer |  |  | Min: 0<br>Max: 4294967295 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].ipv6_static_routes.[].name") | String |  |  |  | description |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].ipv6_static_routes.[].nodes") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].ipv6_static_routes.[].nodes.[].&lt;str&gt;") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tag</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].ipv6_static_routes.[].tag") | Integer |  |  | Min: 0<br>Max: 4294967295 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;l3_interfaces</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].l3_interfaces") | List, items: Dictionary |  |  |  | List of L3 interfaces (Optional)<br>This will create IP routed interface inside VRF. Length of interfaces, nodes and ip_addresses must match<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- description</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].l3_interfaces.[].description") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;descriptions</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].l3_interfaces.[].descriptions") | List, items: String |  |  |  | "descriptions" has precedence over "description"<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].l3_interfaces.[].descriptions.[].&lt;str&gt;") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].l3_interfaces.[].enabled") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interfaces</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].l3_interfaces.[].interfaces") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].l3_interfaces.[].interfaces.[].&lt;str&gt;") | String |  |  |  | Interface name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_addresses</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].l3_interfaces.[].ip_addresses") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].l3_interfaces.[].ip_addresses.[].&lt;str&gt;") | String |  |  |  | IPv4_address/Mask |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mtu</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].l3_interfaces.[].mtu") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].l3_interfaces.[].nodes") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].l3_interfaces.[].nodes.[].&lt;str&gt;") | String |  |  |  | Node |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ospf</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].l3_interfaces.[].ospf") | Dictionary |  |  |  | OSPF interface configuration |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;area</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].l3_interfaces.[].ospf.area") | Integer |  | 0 |  | OSPF area id |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;authentication</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].l3_interfaces.[].ospf.authentication") | String |  |  | Valid Values:<br>- simple<br>- message-digest |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cost</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].l3_interfaces.[].ospf.cost") | Integer |  |  |  | OSPF link cost |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].l3_interfaces.[].ospf.enabled") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;message_digest_keys</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].l3_interfaces.[].ospf.message_digest_keys") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- hash_algorithm</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].l3_interfaces.[].ospf.message_digest_keys.[].hash_algorithm") | String |  | sha512 | Valid Values:<br>- md5<br>- sha1<br>- sha256<br>- sha384<br>- sha512 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;id</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].l3_interfaces.[].ospf.message_digest_keys.[].id") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].l3_interfaces.[].ospf.message_digest_keys.[].key") | String |  |  |  | Key password |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;point_to_point</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].l3_interfaces.[].ospf.point_to_point") | Boolean |  | False |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;simple_auth_key</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].l3_interfaces.[].ospf.simple_auth_key") | String |  |  |  | Password used with simple authentication |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].l3_interfaces.[].raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the VLAN interface in the final EOS configuration<br>Overrides the setting on SVI level.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].l3_interfaces.[].structured_config") | Dictionary |  |  |  | Custom structured config added under vlan_interfaces.<interface> for eos_cli_config_gen.<br>Overrides the setting on SVI level.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_ibgp_peering_ipv4_pool</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].mlag_ibgp_peering_ipv4_pool") | String |  |  |  | IPv4_address/Mask<br>The subnet used for iBGP peering in the VRF.<br>Each MLAG pair will be assigned a subnet based on the ID of the primary MLAG switch<br>If not set, "mlag_peer_l3_ipv4_pool" or "mlag_peer_ipv4_pool" will be used<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_ibgp_peering_vlan</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].mlag_ibgp_peering_vlan") | Integer |  |  | Min: 1<br>Max: 4096 | Manually define the VLAN used on the MLAG pair for the iBGP session (optional)<br>By default this parameter is calculated using the following formula: <mlag_ibgp_peering_vrfs.base_vlan> + <vrf_id> - 1<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].name") | String | Required, Unique |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ospf</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].ospf") | Dictionary |  |  |  | Dictionary for router OSPF configuration (optional)<br>This will create an ospf routing instance in the tenant VRF. If there is no nodes definition, the ospf instance will be<br>created on all leafs where the vrf is deployed. This will also cause automatic ospf redistribution into bgp unless<br>explicitly turned off with "redistribute_ospf: false".<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bfd</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].ospf.bfd") | Boolean |  | False |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].ospf.enabled") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;max_lsa</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].ospf.max_lsa") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].ospf.nodes") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].ospf.nodes.[].&lt;str&gt;") | String |  |  |  | Hostname |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;process_id</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].ospf.process_id") | Integer |  |  |  | If not set, "vrf_id" will be used. |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;redistribute_bgp</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].ospf.redistribute_bgp") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].ospf.redistribute_bgp.enabled") | Boolean |  | True |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].ospf.redistribute_bgp.route_map") | String |  |  |  | Route-map name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;router_id</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].ospf.router_id") | String |  |  |  | If not set, switch router_id will be used. |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the VLAN interface in the final EOS configuration<br>Overrides the setting on SVI level.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;redistribute_ospf</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].redistribute_ospf") | Boolean |  | True |  | Non-selectively enabling or disabling redistribute ospf inside the VRF (optional) |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;redistribute_static</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].redistribute_static") | Boolean |  |  |  | Non-selectively enabling or disabling redistribute static inside the VRF (Optional). |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;static_routes</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].static_routes") | List, items: Dictionary |  |  |  | Dictionary of static routes for v4 and/or v6 (Optional).<br>This will create static routes inside the tenant VRF.<br>If nodes are not specified, all l3leafs that carry the VRF will also be applied the static routes.<br>If a node has a static route in the VRF, redistribute static will be automatically enabled in that VRF.<br>This automatic behavior can be overridden non-selectively with the redistribute_static knob for the VRF.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- destination_address_prefix</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].static_routes.[].destination_address_prefix") | String |  |  |  | IPv4_address/Mask |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;distance</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].static_routes.[].distance") | Integer |  |  | Min: 1<br>Max: 255 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;gateway</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].static_routes.[].gateway") | String |  |  |  | IPv4_address |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interface</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].static_routes.[].interface") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;metric</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].static_routes.[].metric") | Integer |  |  | Min: 0<br>Max: 4294967295 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].static_routes.[].name") | String |  |  |  | description |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].static_routes.[].nodes") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].static_routes.[].nodes.[].&lt;str&gt;") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tag</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].static_routes.[].tag") | Integer |  |  | Min: 0<br>Max: 4294967295 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].structured_config") | Dictionary |  |  |  | Custom structured config added under vlan_interfaces.<interface> for eos_cli_config_gen.<br>Overrides the setting on SVI level.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;svis</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis") | List, items: Dictionary |  |  |  | Dictionary of SVIs<br>This will create both the L3 SVI and L2 VLAN based on filters applied to l3leaf and l2leaf.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- bgp</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].bgp") | Dictionary |  |  |  | Structured configuration and eos cli commands rendered on router_bgp.vlans<br>This configuration will not be applied to vlan aware bundles<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].bgp.raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the VLAN interface in the final EOS configuration<br>Overrides the setting on SVI level.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].bgp.structured_config") | Dictionary |  |  |  | Custom structured config added under vlan_interfaces.<interface> for eos_cli_config_gen.<br>Overrides the setting on SVI level.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].description") | String |  | VLAN name |  | SVI description<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].enabled") | Boolean |  |  |  | Enable or disable interface |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_l2_multicast</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].evpn_l2_multicast") | Boolean |  |  |  | Explicitly enable or disable evpn_l2_multicast to override setting of tenants.<tenant>.evpn_l2_multicast.enabled.<br>When evpn_l2_multicast.enabled is set to true for a vlan or a tenant, "igmp snooping" and "igmp snooping querier" will always be enabled - overriding those individual settings.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;id</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].id") | Integer | Required, Unique |  | Min: 1<br>Max: 4096 | SVI interface id and VLAN id. |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;igmp_snooping_enabled</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].igmp_snooping_enabled") | Boolean |  | True |  | Enable IGMP Snooping |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;igmp_snooping_querier</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].igmp_snooping_querier") | Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].igmp_snooping_querier.enabled") | Boolean |  |  |  | Will be enabled automatically if evpn_l2_multicast is enabled. |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_address</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].igmp_snooping_querier.source_address") | String |  |  |  | IPv4_address<br>If not set, IP address of "Loopback0" will be used.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;version</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].igmp_snooping_querier.version") | Integer |  | 2 | Valid Values:<br>- 1<br>- 2<br>- 3 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_address_virtual</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].ip_address_virtual") | String |  |  |  | IPv4_address/Mask<br>ip address virtual to configure VXLAN Anycast IP address<br>Conserves IP addresses in VXLAN deployments as it doesn't require unique IP addresses on each node.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_address_virtual_secondaries</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].ip_address_virtual_secondaries") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].ip_address_virtual_secondaries.[].&lt;str&gt;") | String |  |  |  | IPv4_address/Mask |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_helpers</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].ip_helpers") | List, items: Dictionary |  |  |  | IP helper for DHCP relay |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- ip_helper</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].ip_helpers.[].ip_helper") | String | Required, Unique |  |  | IPv4 DHCP server IP |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_interface</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].ip_helpers.[].source_interface") | String |  |  |  | Interface name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_vrf</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].ip_helpers.[].source_vrf") | String |  |  |  | VRF to originate DHCP relay packets to DHCP server. If not set, uses current VRF |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_virtual_router_addresses</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].ip_virtual_router_addresses") | List, items: String |  |  |  | IPv4_address/Mask or IPv4_address<br>note, also requires an IP address to be configured on the SVI where it is applied.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].ip_virtual_router_addresses.[].&lt;str&gt;") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_address_virtual</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].ipv6_address_virtual") | String |  |  |  | IPv6_address/Mask<br>ipv6 address virtuals to configure VXLAN Anycast IP address (Optional)<br>The below "ipv6_address_virtual" key will be deprecated in AVD v4.0 in favor of the new "ipv6_address_virtuals"<br>If both "ipv6_address_virtual" and "ipv6_address_virtuals" are set, all addresses will be configured<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_address_virtuals</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].ipv6_address_virtuals") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].ipv6_address_virtuals.[].&lt;str&gt;") | String |  |  |  | IPv6_address/Mask |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_virtual_router_addresses</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].ipv6_virtual_router_addresses") | String |  |  |  | IPv6_address |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mtu</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].mtu") | Integer |  |  |  | Defined interface MTU |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].name") | String |  |  |  | VLAN name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes") | List, items: Dictionary |  |  |  | Define node specific configuration, such as unique IP addresses. |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- ip_address</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].ip_address") | String |  |  |  | IPv4_address/Mask<br>Device unique IP address for node.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_address_virtual_secondaries</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].ip_address_virtual_secondaries") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].ip_address_virtual_secondaries.[].&lt;str&gt;") | String |  |  |  | IPv4_address/Mask |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_helpers</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].ip_helpers") | List, items: Dictionary |  |  |  | IP helper for DHCP relay |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- ip_helper</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].ip_helpers.[].ip_helper") | String | Required, Unique |  |  | IPv4 DHCP server IP |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_interface</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].ip_helpers.[].source_interface") | String |  |  |  | Interface name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_vrf</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].ip_helpers.[].source_vrf") | String |  |  |  | VRF to originate DHCP relay packets to DHCP server. If not set, uses current VRF |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_virtual_router_addresses</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].ip_virtual_router_addresses") | List, items: String |  |  |  | IPv4_address/Mask or IPv4_address<br>note, also requires an IP address to be configured on the SVI where it is applied.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].ip_virtual_router_addresses.[].&lt;str&gt;") | String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_address</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].ipv6_address") | String |  |  |  | IPv6_address/Mask<br>Device unique IPv6 address for node.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;node</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].node") | String | Required, Unique |  |  | l3_leaf inventory hostname |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the VLAN interface in the final EOS configuration<br>Overrides the setting on SVI level.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].nodes.[].structured_config") | Dictionary |  |  |  | Custom structured config added under vlan_interfaces.<interface> for eos_cli_config_gen.<br>Overrides the setting on SVI level.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ospf</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].ospf") | Dictionary |  |  |  | OSPF interface configuration |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;area</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].ospf.area") | Integer |  | 0 |  | OSPF area id |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;authentication</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].ospf.authentication") | String |  |  | Valid Values:<br>- simple<br>- message-digest |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cost</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].ospf.cost") | Integer |  |  |  | OSPF link cost |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].ospf.enabled") | Boolean |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;message_digest_keys</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].ospf.message_digest_keys") | List, items: Dictionary |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- hash_algorithm</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].ospf.message_digest_keys.[].hash_algorithm") | String |  | sha512 | Valid Values:<br>- md5<br>- sha1<br>- sha256<br>- sha384<br>- sha512 |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;id</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].ospf.message_digest_keys.[].id") | Integer |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].ospf.message_digest_keys.[].key") | String |  |  |  | Key password |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;point_to_point</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].ospf.point_to_point") | Boolean |  | True |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;simple_auth_key</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].ospf.simple_auth_key") | String |  |  |  | Password used with simple authentication |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;profile</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].profile") | String |  |  |  | SVI profile name to apply<br>If variables are configured in profile AND SVI, SVI information will overwrite profile<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the VLAN interface in the final EOS configuration<br>Overrides the setting on SVI level<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rt_override</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].rt_override") | Integer |  |  | Min: 1<br>Max: 16777215 | By default the MAC VRF RD/RT ID will be derived from "mac_vrf_id_base"<br>The rt_override allows us to override this value and statically define it (optional)<br>If not set, vni_override will be used.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].structured_config") | Dictionary |  |  |  | Custom structured config added under vlan_interfaces.<interface> for eos_cli_config_gen.<br>Overrides the setting on SVI level.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tags</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].tags") | List, items: String |  |  |  | Tags leveraged for networks services filtering<br>Tags are matched against "filter.tags" defined under Fabric Topology variables<br>Tags are also matched against the "node_group" name under Fabric Topology variables<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].tags.[].&lt;str&gt;") | String |  | all |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;trunk_groups</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].trunk_groups") | List, items: String |  |  |  |  |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].trunk_groups.[].&lt;str&gt;") | String |  |  |  | Trunk groups are used for limiting vlans to trunk ports assigned to the same trunk group<br>Requires "enable_trunk_groups: true"<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vni_override</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].vni_override") | Integer |  |  | Min: 1<br>Max: 16777215 | By default the vni will be derived from "mac_vrf_vni_base"<br>The vni_override allows us to override this value and statically define it (optional)<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vxlan</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].svis.[].vxlan") | Boolean |  | True |  | Extend this SVI over VXLAN |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf_id</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].vrf_id") | Integer |  |  | Min: 1<br>Max: 1024 | Required if "vrf_vni" is not set.<br>"vrf_id" is used as default value for "vrf_vni" and "ospf.process_id" unless those are set.<br>"vrf_id" is preferred over "vrf_vni" for VRF RD/RT ID before vrf_vni<br>"vrf_id" is preferred over "vrf_vni" for MLAG IBGP peering vlan, see "mlag_ibgp_peering_vrfs.base_vlan" for details<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf_vni</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].vrf_vni") | Integer |  |  | Min: 1<br>Max: 1024 | Required if "vrf_id" is not set.<br>The VRF VNI range is not limited, but if vrf_id is not set, "vrf_vni" is used for calculating MLAG IBGP peering vlan id.<br>See "mlag_ibgp_peering_vrfs.base_vlan" for details.<br>If vrf_vni > 10000 make sure to adjust "mac_vrf_vni_base" accordingly to avoid overlap.<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vtep_diagnostic</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].vtep_diagnostic") | Dictionary |  |  |  | Enable VTEP Network diagnostics (Optional)<br>This will create a loopback with virtual source-nat enable to perform diagnostics from the switch<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loopback</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].vtep_diagnostic.loopback") | Integer |  |  | Min: 2<br>Max: 2100 | Loopback interface number, required (when vtep_diagnotics defined)<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loopback_ip_pools</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].vtep_diagnostic.loopback_ip_pools") | List, items: Dictionary |  |  |  | For inventories with multiple PODs a loopback range can be set per POD to avoid overlaps.<br>This only takes effect when loopback_ip_range is not defined, ptional (loopback is not created unless loopback_ip_range or loopback_ip_pools are set)<br> |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- ipv4_pool</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].vtep_diagnostic.loopback_ip_pools.[].ipv4_pool") | String |  |  |  | IPv4_address/Mask |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pod</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].vtep_diagnostic.loopback_ip_pools.[].pod") | String |  |  |  | POD name |
| [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loopback_ip_range</samp>](## "&lt;network_services_keys.name&gt;.[].vrfs.[].vtep_diagnostic.loopback_ip_range") | String |  |  |  | IPv4_address/Mask<br>Loopback ip range, a unique ip is derived from this ranged and assigned<br>to each l3 leaf based on it's unique id, ptional (loopback is not created unless loopback_ip_range or loopback_ip_pools are set)<br> |

### YAML

```yaml
<network_services_keys.name>:
  - bgp_peer_groups:
      - bfd: <bool>
        default_originate:
          always: <bool>
          enabled: <bool>
        description: <str>
        ebgp_multihop: <int>
        local_as: <str>
        maximum_routes: <int>
        name: <str>
        next_hop_self: <bool>
        nodes:
          - <str>
        remote_as: <int>
        route_map_in: <str>
        route_map_out: <str>
        send_community: <str>
        set_ipv4_next_hop: <str>
        set_ipv6_next_hop: <str>
        update_source: <str>
        weight: <int>
    enable_mlag_ibgp_peering_vrfs: <bool>
    evpn_l2_multicast:
      enabled: <bool>
      underlay_l2_multicast_group_ipv4_pool: <str>
      underlay_l2_multicast_group_ipv4_pool_offset: <int>
    evpn_l3_multicast:
      enabled: <bool>
      evpn_peg:
        - nodes:
            - <str>
          transit: <bool>
      evpn_underlay_l3_multicast_group_ipv4_pool: <str>
      evpn_underlay_l3_multicast_group_ipv4_pool_offset: <int>
    igmp_snooping_querier:
      enabled: <bool>
      source_address: <str>
      version: <int>
    l2vlans:
      - bgp:
          raw_eos_cli: <str>
        evpn_l2_multicast: <bool>
        id: <int>
        igmp_snooping_enabled: <bool>
        igmp_snooping_querier:
          enabled: <bool>
          source_address: <str>
          version: <int>
        name: <str>
        rt_override: <int>
        tags:
          - <str>
        trunk_groups:
          - <str>
        vni_override: <int>
        vxlan: <bool>
    mac_vrf_id_base: <int>
    mac_vrf_vni_base: <int>
    name: <str>
    pim_rp_addresses:
      - groups:
          - <str>
        nodes:
          - <str>
        rps:
          - <str>
    vlan_aware_bundle_number_base: <int>
    vrfs:
      - additional_route_targets:
          - address_family: <str>
            nodes:
              - <str>
            route_target: <str>
            type: <str>
        bgp:
          raw_eos_cli: <str>
          structured_config:
        bgp_peer_groups:
          - bfd: <bool>
            default_originate:
              always: <bool>
              enabled: <bool>
            description: <str>
            ebgp_multihop: <int>
            local_as: <str>
            maximum_routes: <int>
            name: <str>
            next_hop_self: <bool>
            nodes:
              - <str>
            remote_as: <int>
            route_map_in: <str>
            route_map_out: <str>
            send_community: <str>
            set_ipv4_next_hop: <str>
            set_ipv6_next_hop: <str>
            update_source: <str>
            weight: <int>
        bgp_peers:
          - bfd: <bool>
            default_originate:
              always: <bool>
            description: <str>
            ebgp_multihop: <int>
            ip_address: <str>
            local_as: <str>
            maximum_routes: <int>
            next_hop_self: <bool>
            nodes:
              - <str>
            password: <str>
            prefix_list_in: <str>
            prefix_list_out: <str>
            remote_as: <int>
            route_map_in: <str>
            route_map_out: <str>
            send_community: <str>
            set_ipv4_next_hop: <str>
            set_ipv6_next_hop: <str>
            timers: <str>
            update_source: <str>
            weight: <int>
        description: <str>
        enable_mlag_ibgp_peering_vrfs: <bool>
        ip_helpers:
          - ip_helper: <str>
            source_interface: <str>
            source_vrf: <str>
        ipv6_static_routes:
          - destination_address_prefix: <str>
            distance: <int>
            gateway: <str>
            interface: <str>
            metric: <int>
            name: <str>
            nodes:
              - <str>
            tag: <int>
        l3_interfaces:
          - description: <str>
            descriptions:
              - <str>
            enabled: <bool>
            interfaces:
              - <str>
            ip_addresses:
              - <str>
            mtu: <int>
            nodes:
              - <str>
            ospf:
              area: <int>
              authentication: <str>
              cost: <int>
              enabled: <bool>
              message_digest_keys:
                - hash_algorithm: <str>
                  id: <int>
                  key: <str>
              point_to_point: <bool>
              simple_auth_key: <str>
            raw_eos_cli: <str>
            structured_config:
        mlag_ibgp_peering_ipv4_pool: <str>
        mlag_ibgp_peering_vlan: <int>
        name: <str>
        ospf:
          bfd: <bool>
          enabled: <bool>
          max_lsa: <int>
          nodes:
            - <str>
          process_id: <int>
          redistribute_bgp:
            enabled: <bool>
            route_map: <str>
          router_id: <str>
        raw_eos_cli: <str>
        redistribute_ospf: <bool>
        redistribute_static: <bool>
        static_routes:
          - destination_address_prefix: <str>
            distance: <int>
            gateway: <str>
            interface: <str>
            metric: <int>
            name: <str>
            nodes:
              - <str>
            tag: <int>
        structured_config:
        svis:
          - bgp:
              raw_eos_cli: <str>
              structured_config:
            description: <str>
            enabled: <bool>
            evpn_l2_multicast: <bool>
            id: <int>
            igmp_snooping_enabled: <bool>
            igmp_snooping_querier:
              enabled: <bool>
              source_address: <str>
              version: <int>
            ip_address_virtual: <str>
            ip_address_virtual_secondaries:
              - <str>
            ip_helpers:
              - ip_helper: <str>
                source_interface: <str>
                source_vrf: <str>
            ip_virtual_router_addresses:
              - <str>
            ipv6_address_virtual: <str>
            ipv6_address_virtuals:
              - <str>
            ipv6_virtual_router_addresses: <str>
            mtu: <int>
            name: <str>
            nodes:
              - ip_address: <str>
                ip_address_virtual_secondaries:
                  - <str>
                ip_helpers:
                  - ip_helper: <str>
                    source_interface: <str>
                    source_vrf: <str>
                ip_virtual_router_addresses:
                  - <str>
                ipv6_address: <str>
                node: <str>
                raw_eos_cli: <str>
                structured_config:
            ospf:
              area: <int>
              authentication: <str>
              cost: <int>
              enabled: <bool>
              message_digest_keys:
                - hash_algorithm: <str>
                  id: <int>
                  key: <str>
              point_to_point: <bool>
              simple_auth_key: <str>
            profile: <str>
            raw_eos_cli: <str>
            rt_override: <int>
            structured_config:
            tags:
              - <str>
            trunk_groups:
              - <str>
            vni_override: <int>
            vxlan: <bool>
        vrf_id: <int>
        vrf_vni: <int>
        vtep_diagnostic:
          loopback: <int>
          loopback_ip_pools:
            - ipv4_pool: <str>
              pod: <str>
          loopback_ip_range: <str>
```
