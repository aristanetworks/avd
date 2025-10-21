<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>&lt;node_type_keys.key&gt;</samp>](## "<node_type_keys.key>") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;defaults</samp>](## "<node_type_keys.key>.defaults") | Dictionary |  |  |  | Define variables for all nodes of this type. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;underlay_multicast</samp>](## "<node_type_keys.key>.defaults.underlay_multicast") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pim_sm</samp>](## "<node_type_keys.key>.defaults.underlay_multicast.pim_sm") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<node_type_keys.key>.defaults.underlay_multicast.pim_sm.enabled") | Boolean |  |  |  | When enabled, configures multicast routing and by default configures PIM sparse-mode in the underlay on all:<br>  - P2P uplink interfaces if enabled on uplink peer<br>  - MLAG L3 peer interface if also enabled on MLAG peer<br>  - l3_edge and core interfaces<br>Overrides the global `underlay_multicast_pim_sm`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplinks</samp>](## "<node_type_keys.key>.defaults.underlay_multicast.pim_sm.uplinks") | Boolean |  | `True` |  | Enable/Disable PIM sparse-mode on uplinks.<br>Requires node setting `underlay_multicast.pim_sm.enabled: true` or, if unset, global `underlay_multicast_pim_sm: true` |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_interfaces</samp>](## "<node_type_keys.key>.defaults.underlay_multicast.pim_sm.uplink_interfaces") | List, items: String |  |  |  | Limit PIM SM to the uplink_interfaces in this list. All interfaces if unset.<br>Effective only when node settings `underlay_multicast.pim_sm.uplinks: true`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "<node_type_keys.key>.defaults.underlay_multicast.pim_sm.uplink_interfaces.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag</samp>](## "<node_type_keys.key>.defaults.underlay_multicast.pim_sm.mlag") | Boolean |  | `True` |  | Configure PIM sparse-mode in the underlay on the MLAG L3 peer VLAN interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;static</samp>](## "<node_type_keys.key>.defaults.underlay_multicast.static") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<node_type_keys.key>.defaults.underlay_multicast.static.enabled") | Boolean |  |  |  | When enabled, configures multicast routing and by default configures static multicast in the underlay on all:<br>  - P2P uplink interfaces if enabled on uplink peer<br>  - MLAG L3 peer interface if also enabled on MLAG peer<br>  - l3_edge and core interfaces<br>Overrides the global `underlay_multicast_static`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplinks</samp>](## "<node_type_keys.key>.defaults.underlay_multicast.static.uplinks") | Boolean |  | `True` |  | Enable/Disable static multicast on uplinks.<br>Requires node setting `underlay_multicast.static.enabled: true` or, if unset, global `underlay_multicast_static: true` |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_interfaces</samp>](## "<node_type_keys.key>.defaults.underlay_multicast.static.uplink_interfaces") | List, items: String |  |  |  | Limit static multicast to the uplink_interfaces in this list. All interfaces if unset.<br>Effective only when node settings `underlay_multicast.static.uplinks: true`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "<node_type_keys.key>.defaults.underlay_multicast.static.uplink_interfaces.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag</samp>](## "<node_type_keys.key>.defaults.underlay_multicast.static.mlag") | Boolean |  | `True` |  | Configure static multicast in the underlay on MLAG L3 peer interfacee. |
    | [<samp>&nbsp;&nbsp;node_groups</samp>](## "<node_type_keys.key>.node_groups") | List, items: Dictionary |  |  |  | Define variables related to all nodes part of this group. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;group</samp>](## "<node_type_keys.key>.node_groups.[].group") | String | Required, Unique |  |  | The Node Group Name is used for MLAG domain unless set with 'mlag_domain_id'.<br>The Node Group Name is also used for peer description on downstream switches' uplinks.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "<node_type_keys.key>.node_groups.[].nodes") | List, items: Dictionary |  |  |  | Define variables per node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].name") | String | Required, Unique |  |  | The Node Name is used as "hostname". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;underlay_multicast</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].underlay_multicast") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pim_sm</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].underlay_multicast.pim_sm") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].underlay_multicast.pim_sm.enabled") | Boolean |  |  |  | When enabled, configures multicast routing and by default configures PIM sparse-mode in the underlay on all:<br>  - P2P uplink interfaces if enabled on uplink peer<br>  - MLAG L3 peer interface if also enabled on MLAG peer<br>  - l3_edge and core interfaces<br>Overrides the global `underlay_multicast_pim_sm`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplinks</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].underlay_multicast.pim_sm.uplinks") | Boolean |  | `True` |  | Enable/Disable PIM sparse-mode on uplinks.<br>Requires node setting `underlay_multicast.pim_sm.enabled: true` or, if unset, global `underlay_multicast_pim_sm: true` |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_interfaces</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].underlay_multicast.pim_sm.uplink_interfaces") | List, items: String |  |  |  | Limit PIM SM to the uplink_interfaces in this list. All interfaces if unset.<br>Effective only when node settings `underlay_multicast.pim_sm.uplinks: true`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].underlay_multicast.pim_sm.uplink_interfaces.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].underlay_multicast.pim_sm.mlag") | Boolean |  | `True` |  | Configure PIM sparse-mode in the underlay on the MLAG L3 peer VLAN interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;static</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].underlay_multicast.static") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].underlay_multicast.static.enabled") | Boolean |  |  |  | When enabled, configures multicast routing and by default configures static multicast in the underlay on all:<br>  - P2P uplink interfaces if enabled on uplink peer<br>  - MLAG L3 peer interface if also enabled on MLAG peer<br>  - l3_edge and core interfaces<br>Overrides the global `underlay_multicast_static`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplinks</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].underlay_multicast.static.uplinks") | Boolean |  | `True` |  | Enable/Disable static multicast on uplinks.<br>Requires node setting `underlay_multicast.static.enabled: true` or, if unset, global `underlay_multicast_static: true` |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_interfaces</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].underlay_multicast.static.uplink_interfaces") | List, items: String |  |  |  | Limit static multicast to the uplink_interfaces in this list. All interfaces if unset.<br>Effective only when node settings `underlay_multicast.static.uplinks: true`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].underlay_multicast.static.uplink_interfaces.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].underlay_multicast.static.mlag") | Boolean |  | `True` |  | Configure static multicast in the underlay on MLAG L3 peer interfacee. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;underlay_multicast</samp>](## "<node_type_keys.key>.node_groups.[].underlay_multicast") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pim_sm</samp>](## "<node_type_keys.key>.node_groups.[].underlay_multicast.pim_sm") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<node_type_keys.key>.node_groups.[].underlay_multicast.pim_sm.enabled") | Boolean |  |  |  | When enabled, configures multicast routing and by default configures PIM sparse-mode in the underlay on all:<br>  - P2P uplink interfaces if enabled on uplink peer<br>  - MLAG L3 peer interface if also enabled on MLAG peer<br>  - l3_edge and core interfaces<br>Overrides the global `underlay_multicast_pim_sm`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplinks</samp>](## "<node_type_keys.key>.node_groups.[].underlay_multicast.pim_sm.uplinks") | Boolean |  | `True` |  | Enable/Disable PIM sparse-mode on uplinks.<br>Requires node setting `underlay_multicast.pim_sm.enabled: true` or, if unset, global `underlay_multicast_pim_sm: true` |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_interfaces</samp>](## "<node_type_keys.key>.node_groups.[].underlay_multicast.pim_sm.uplink_interfaces") | List, items: String |  |  |  | Limit PIM SM to the uplink_interfaces in this list. All interfaces if unset.<br>Effective only when node settings `underlay_multicast.pim_sm.uplinks: true`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "<node_type_keys.key>.node_groups.[].underlay_multicast.pim_sm.uplink_interfaces.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag</samp>](## "<node_type_keys.key>.node_groups.[].underlay_multicast.pim_sm.mlag") | Boolean |  | `True` |  | Configure PIM sparse-mode in the underlay on the MLAG L3 peer VLAN interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;static</samp>](## "<node_type_keys.key>.node_groups.[].underlay_multicast.static") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<node_type_keys.key>.node_groups.[].underlay_multicast.static.enabled") | Boolean |  |  |  | When enabled, configures multicast routing and by default configures static multicast in the underlay on all:<br>  - P2P uplink interfaces if enabled on uplink peer<br>  - MLAG L3 peer interface if also enabled on MLAG peer<br>  - l3_edge and core interfaces<br>Overrides the global `underlay_multicast_static`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplinks</samp>](## "<node_type_keys.key>.node_groups.[].underlay_multicast.static.uplinks") | Boolean |  | `True` |  | Enable/Disable static multicast on uplinks.<br>Requires node setting `underlay_multicast.static.enabled: true` or, if unset, global `underlay_multicast_static: true` |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_interfaces</samp>](## "<node_type_keys.key>.node_groups.[].underlay_multicast.static.uplink_interfaces") | List, items: String |  |  |  | Limit static multicast to the uplink_interfaces in this list. All interfaces if unset.<br>Effective only when node settings `underlay_multicast.static.uplinks: true`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "<node_type_keys.key>.node_groups.[].underlay_multicast.static.uplink_interfaces.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag</samp>](## "<node_type_keys.key>.node_groups.[].underlay_multicast.static.mlag") | Boolean |  | `True` |  | Configure static multicast in the underlay on MLAG L3 peer interfacee. |
    | [<samp>&nbsp;&nbsp;nodes</samp>](## "<node_type_keys.key>.nodes") | List, items: Dictionary |  |  |  | Define variables per node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "<node_type_keys.key>.nodes.[].name") | String | Required, Unique |  |  | The Node Name is used as "hostname". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;underlay_multicast</samp>](## "<node_type_keys.key>.nodes.[].underlay_multicast") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pim_sm</samp>](## "<node_type_keys.key>.nodes.[].underlay_multicast.pim_sm") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<node_type_keys.key>.nodes.[].underlay_multicast.pim_sm.enabled") | Boolean |  |  |  | When enabled, configures multicast routing and by default configures PIM sparse-mode in the underlay on all:<br>  - P2P uplink interfaces if enabled on uplink peer<br>  - MLAG L3 peer interface if also enabled on MLAG peer<br>  - l3_edge and core interfaces<br>Overrides the global `underlay_multicast_pim_sm`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplinks</samp>](## "<node_type_keys.key>.nodes.[].underlay_multicast.pim_sm.uplinks") | Boolean |  | `True` |  | Enable/Disable PIM sparse-mode on uplinks.<br>Requires node setting `underlay_multicast.pim_sm.enabled: true` or, if unset, global `underlay_multicast_pim_sm: true` |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_interfaces</samp>](## "<node_type_keys.key>.nodes.[].underlay_multicast.pim_sm.uplink_interfaces") | List, items: String |  |  |  | Limit PIM SM to the uplink_interfaces in this list. All interfaces if unset.<br>Effective only when node settings `underlay_multicast.pim_sm.uplinks: true`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "<node_type_keys.key>.nodes.[].underlay_multicast.pim_sm.uplink_interfaces.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag</samp>](## "<node_type_keys.key>.nodes.[].underlay_multicast.pim_sm.mlag") | Boolean |  | `True` |  | Configure PIM sparse-mode in the underlay on the MLAG L3 peer VLAN interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;static</samp>](## "<node_type_keys.key>.nodes.[].underlay_multicast.static") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<node_type_keys.key>.nodes.[].underlay_multicast.static.enabled") | Boolean |  |  |  | When enabled, configures multicast routing and by default configures static multicast in the underlay on all:<br>  - P2P uplink interfaces if enabled on uplink peer<br>  - MLAG L3 peer interface if also enabled on MLAG peer<br>  - l3_edge and core interfaces<br>Overrides the global `underlay_multicast_static`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplinks</samp>](## "<node_type_keys.key>.nodes.[].underlay_multicast.static.uplinks") | Boolean |  | `True` |  | Enable/Disable static multicast on uplinks.<br>Requires node setting `underlay_multicast.static.enabled: true` or, if unset, global `underlay_multicast_static: true` |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_interfaces</samp>](## "<node_type_keys.key>.nodes.[].underlay_multicast.static.uplink_interfaces") | List, items: String |  |  |  | Limit static multicast to the uplink_interfaces in this list. All interfaces if unset.<br>Effective only when node settings `underlay_multicast.static.uplinks: true`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "<node_type_keys.key>.nodes.[].underlay_multicast.static.uplink_interfaces.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag</samp>](## "<node_type_keys.key>.nodes.[].underlay_multicast.static.mlag") | Boolean |  | `True` |  | Configure static multicast in the underlay on MLAG L3 peer interfacee. |
    | [<samp>device_profiles</samp>](## "device_profiles") | List, items: Dictionary |  |  |  | PREVIEW - This datamodel is still under development and may change or get removed at any time. |
    | [<samp>&nbsp;&nbsp;-&nbsp;name</samp>](## "device_profiles.[].name") | String | Required, Unique |  |  | Profile Name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;underlay_multicast</samp>](## "device_profiles.[].underlay_multicast") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pim_sm</samp>](## "device_profiles.[].underlay_multicast.pim_sm") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "device_profiles.[].underlay_multicast.pim_sm.enabled") | Boolean |  |  |  | When enabled, configures multicast routing and by default configures PIM sparse-mode in the underlay on all:<br>  - P2P uplink interfaces if enabled on uplink peer<br>  - MLAG L3 peer interface if also enabled on MLAG peer<br>  - l3_edge and core interfaces<br>Overrides the global `underlay_multicast_pim_sm`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplinks</samp>](## "device_profiles.[].underlay_multicast.pim_sm.uplinks") | Boolean |  | `True` |  | Enable/Disable PIM sparse-mode on uplinks.<br>Requires node setting `underlay_multicast.pim_sm.enabled: true` or, if unset, global `underlay_multicast_pim_sm: true` |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_interfaces</samp>](## "device_profiles.[].underlay_multicast.pim_sm.uplink_interfaces") | List, items: String |  |  |  | Limit PIM SM to the uplink_interfaces in this list. All interfaces if unset.<br>Effective only when node settings `underlay_multicast.pim_sm.uplinks: true`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "device_profiles.[].underlay_multicast.pim_sm.uplink_interfaces.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag</samp>](## "device_profiles.[].underlay_multicast.pim_sm.mlag") | Boolean |  | `True` |  | Configure PIM sparse-mode in the underlay on the MLAG L3 peer VLAN interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;static</samp>](## "device_profiles.[].underlay_multicast.static") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "device_profiles.[].underlay_multicast.static.enabled") | Boolean |  |  |  | When enabled, configures multicast routing and by default configures static multicast in the underlay on all:<br>  - P2P uplink interfaces if enabled on uplink peer<br>  - MLAG L3 peer interface if also enabled on MLAG peer<br>  - l3_edge and core interfaces<br>Overrides the global `underlay_multicast_static`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplinks</samp>](## "device_profiles.[].underlay_multicast.static.uplinks") | Boolean |  | `True` |  | Enable/Disable static multicast on uplinks.<br>Requires node setting `underlay_multicast.static.enabled: true` or, if unset, global `underlay_multicast_static: true` |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_interfaces</samp>](## "device_profiles.[].underlay_multicast.static.uplink_interfaces") | List, items: String |  |  |  | Limit static multicast to the uplink_interfaces in this list. All interfaces if unset.<br>Effective only when node settings `underlay_multicast.static.uplinks: true`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "device_profiles.[].underlay_multicast.static.uplink_interfaces.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag</samp>](## "device_profiles.[].underlay_multicast.static.mlag") | Boolean |  | `True` |  | Configure static multicast in the underlay on MLAG L3 peer interfacee. |
    | [<samp>device_roles</samp>](## "device_roles") | List, items: Dictionary |  | See (+) on YAML tab |  | PREVIEW - This datamodel is still under development and may change or get removed at any time. |
    | [<samp>&nbsp;&nbsp;-&nbsp;name</samp>](## "device_roles.[].name") | String | Required, Unique |  |  | Role Name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;underlay_multicast</samp>](## "device_roles.[].underlay_multicast") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pim_sm</samp>](## "device_roles.[].underlay_multicast.pim_sm") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "device_roles.[].underlay_multicast.pim_sm.enabled") | Boolean |  |  |  | When enabled, configures multicast routing and by default configures PIM sparse-mode in the underlay on all:<br>  - P2P uplink interfaces if enabled on uplink peer<br>  - MLAG L3 peer interface if also enabled on MLAG peer<br>  - l3_edge and core interfaces<br>Overrides the global `underlay_multicast_pim_sm`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplinks</samp>](## "device_roles.[].underlay_multicast.pim_sm.uplinks") | Boolean |  | `True` |  | Enable/Disable PIM sparse-mode on uplinks.<br>Requires node setting `underlay_multicast.pim_sm.enabled: true` or, if unset, global `underlay_multicast_pim_sm: true` |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_interfaces</samp>](## "device_roles.[].underlay_multicast.pim_sm.uplink_interfaces") | List, items: String |  |  |  | Limit PIM SM to the uplink_interfaces in this list. All interfaces if unset.<br>Effective only when node settings `underlay_multicast.pim_sm.uplinks: true`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "device_roles.[].underlay_multicast.pim_sm.uplink_interfaces.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag</samp>](## "device_roles.[].underlay_multicast.pim_sm.mlag") | Boolean |  | `True` |  | Configure PIM sparse-mode in the underlay on the MLAG L3 peer VLAN interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;static</samp>](## "device_roles.[].underlay_multicast.static") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "device_roles.[].underlay_multicast.static.enabled") | Boolean |  |  |  | When enabled, configures multicast routing and by default configures static multicast in the underlay on all:<br>  - P2P uplink interfaces if enabled on uplink peer<br>  - MLAG L3 peer interface if also enabled on MLAG peer<br>  - l3_edge and core interfaces<br>Overrides the global `underlay_multicast_static`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplinks</samp>](## "device_roles.[].underlay_multicast.static.uplinks") | Boolean |  | `True` |  | Enable/Disable static multicast on uplinks.<br>Requires node setting `underlay_multicast.static.enabled: true` or, if unset, global `underlay_multicast_static: true` |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_interfaces</samp>](## "device_roles.[].underlay_multicast.static.uplink_interfaces") | List, items: String |  |  |  | Limit static multicast to the uplink_interfaces in this list. All interfaces if unset.<br>Effective only when node settings `underlay_multicast.static.uplinks: true`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "device_roles.[].underlay_multicast.static.uplink_interfaces.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag</samp>](## "device_roles.[].underlay_multicast.static.mlag") | Boolean |  | `True` |  | Configure static multicast in the underlay on MLAG L3 peer interfacee. |
    | [<samp>devices</samp>](## "devices") | List, items: Dictionary |  |  |  | PREVIEW - This datamodel is still under development and may change or get removed at any time. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "devices.[].name") | String | Required, Unique |  |  | The Node Name is used as "hostname". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;underlay_multicast</samp>](## "devices.[].underlay_multicast") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pim_sm</samp>](## "devices.[].underlay_multicast.pim_sm") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "devices.[].underlay_multicast.pim_sm.enabled") | Boolean |  |  |  | When enabled, configures multicast routing and by default configures PIM sparse-mode in the underlay on all:<br>  - P2P uplink interfaces if enabled on uplink peer<br>  - MLAG L3 peer interface if also enabled on MLAG peer<br>  - l3_edge and core interfaces<br>Overrides the global `underlay_multicast_pim_sm`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplinks</samp>](## "devices.[].underlay_multicast.pim_sm.uplinks") | Boolean |  | `True` |  | Enable/Disable PIM sparse-mode on uplinks.<br>Requires node setting `underlay_multicast.pim_sm.enabled: true` or, if unset, global `underlay_multicast_pim_sm: true` |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_interfaces</samp>](## "devices.[].underlay_multicast.pim_sm.uplink_interfaces") | List, items: String |  |  |  | Limit PIM SM to the uplink_interfaces in this list. All interfaces if unset.<br>Effective only when node settings `underlay_multicast.pim_sm.uplinks: true`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "devices.[].underlay_multicast.pim_sm.uplink_interfaces.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag</samp>](## "devices.[].underlay_multicast.pim_sm.mlag") | Boolean |  | `True` |  | Configure PIM sparse-mode in the underlay on the MLAG L3 peer VLAN interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;static</samp>](## "devices.[].underlay_multicast.static") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "devices.[].underlay_multicast.static.enabled") | Boolean |  |  |  | When enabled, configures multicast routing and by default configures static multicast in the underlay on all:<br>  - P2P uplink interfaces if enabled on uplink peer<br>  - MLAG L3 peer interface if also enabled on MLAG peer<br>  - l3_edge and core interfaces<br>Overrides the global `underlay_multicast_static`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplinks</samp>](## "devices.[].underlay_multicast.static.uplinks") | Boolean |  | `True` |  | Enable/Disable static multicast on uplinks.<br>Requires node setting `underlay_multicast.static.enabled: true` or, if unset, global `underlay_multicast_static: true` |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_interfaces</samp>](## "devices.[].underlay_multicast.static.uplink_interfaces") | List, items: String |  |  |  | Limit static multicast to the uplink_interfaces in this list. All interfaces if unset.<br>Effective only when node settings `underlay_multicast.static.uplinks: true`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "devices.[].underlay_multicast.static.uplink_interfaces.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag</samp>](## "devices.[].underlay_multicast.static.mlag") | Boolean |  | `True` |  | Configure static multicast in the underlay on MLAG L3 peer interfacee. |
    | [<samp>match_devices</samp>](## "match_devices") | List, items: Dictionary |  |  |  | PREVIEW - This datamodel is still under development and may change or get removed at any time.<br>If a device is not defined under `devices`, AVD will check for a matching entry here, and apply the device settings for the first match. |
    | [<samp>&nbsp;&nbsp;-&nbsp;hostname_pattern</samp>](## "match_devices.[].hostname_pattern") | String | Required, Unique |  |  | Regex pattern matching the full inventory hostname of one or more devices. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;underlay_multicast</samp>](## "match_devices.[].underlay_multicast") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pim_sm</samp>](## "match_devices.[].underlay_multicast.pim_sm") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "match_devices.[].underlay_multicast.pim_sm.enabled") | Boolean |  |  |  | When enabled, configures multicast routing and by default configures PIM sparse-mode in the underlay on all:<br>  - P2P uplink interfaces if enabled on uplink peer<br>  - MLAG L3 peer interface if also enabled on MLAG peer<br>  - l3_edge and core interfaces<br>Overrides the global `underlay_multicast_pim_sm`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplinks</samp>](## "match_devices.[].underlay_multicast.pim_sm.uplinks") | Boolean |  | `True` |  | Enable/Disable PIM sparse-mode on uplinks.<br>Requires node setting `underlay_multicast.pim_sm.enabled: true` or, if unset, global `underlay_multicast_pim_sm: true` |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_interfaces</samp>](## "match_devices.[].underlay_multicast.pim_sm.uplink_interfaces") | List, items: String |  |  |  | Limit PIM SM to the uplink_interfaces in this list. All interfaces if unset.<br>Effective only when node settings `underlay_multicast.pim_sm.uplinks: true`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "match_devices.[].underlay_multicast.pim_sm.uplink_interfaces.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag</samp>](## "match_devices.[].underlay_multicast.pim_sm.mlag") | Boolean |  | `True` |  | Configure PIM sparse-mode in the underlay on the MLAG L3 peer VLAN interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;static</samp>](## "match_devices.[].underlay_multicast.static") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "match_devices.[].underlay_multicast.static.enabled") | Boolean |  |  |  | When enabled, configures multicast routing and by default configures static multicast in the underlay on all:<br>  - P2P uplink interfaces if enabled on uplink peer<br>  - MLAG L3 peer interface if also enabled on MLAG peer<br>  - l3_edge and core interfaces<br>Overrides the global `underlay_multicast_static`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplinks</samp>](## "match_devices.[].underlay_multicast.static.uplinks") | Boolean |  | `True` |  | Enable/Disable static multicast on uplinks.<br>Requires node setting `underlay_multicast.static.enabled: true` or, if unset, global `underlay_multicast_static: true` |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_interfaces</samp>](## "match_devices.[].underlay_multicast.static.uplink_interfaces") | List, items: String |  |  |  | Limit static multicast to the uplink_interfaces in this list. All interfaces if unset.<br>Effective only when node settings `underlay_multicast.static.uplinks: true`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "match_devices.[].underlay_multicast.static.uplink_interfaces.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag</samp>](## "match_devices.[].underlay_multicast.static.mlag") | Boolean |  | `True` |  | Configure static multicast in the underlay on MLAG L3 peer interfacee. |

=== "YAML"

    ```yaml
    <node_type_keys.key>:

      # Define variables for all nodes of this type.
      defaults:
        underlay_multicast:
          pim_sm:

            # When enabled, configures multicast routing and by default configures PIM sparse-mode in the underlay on all:
            #   - P2P uplink interfaces if enabled on uplink peer
            #   - MLAG L3 peer interface if also enabled on MLAG peer
            #   - l3_edge and core interfaces
            # Overrides the global `underlay_multicast_pim_sm`.
            enabled: <bool>

            # Enable/Disable PIM sparse-mode on uplinks.
            # Requires node setting `underlay_multicast.pim_sm.enabled: true` or, if unset, global `underlay_multicast_pim_sm: true`
            uplinks: <bool; default=True>

            # Limit PIM SM to the uplink_interfaces in this list. All interfaces if unset.
            # Effective only when node settings `underlay_multicast.pim_sm.uplinks: true`.
            uplink_interfaces:
              - <str>

            # Configure PIM sparse-mode in the underlay on the MLAG L3 peer VLAN interface.
            mlag: <bool; default=True>
          static:

            # When enabled, configures multicast routing and by default configures static multicast in the underlay on all:
            #   - P2P uplink interfaces if enabled on uplink peer
            #   - MLAG L3 peer interface if also enabled on MLAG peer
            #   - l3_edge and core interfaces
            # Overrides the global `underlay_multicast_static`.
            enabled: <bool>

            # Enable/Disable static multicast on uplinks.
            # Requires node setting `underlay_multicast.static.enabled: true` or, if unset, global `underlay_multicast_static: true`
            uplinks: <bool; default=True>

            # Limit static multicast to the uplink_interfaces in this list. All interfaces if unset.
            # Effective only when node settings `underlay_multicast.static.uplinks: true`.
            uplink_interfaces:
              - <str>

            # Configure static multicast in the underlay on MLAG L3 peer interfacee.
            mlag: <bool; default=True>

      # Define variables related to all nodes part of this group.
      node_groups:

          # The Node Group Name is used for MLAG domain unless set with 'mlag_domain_id'.
          # The Node Group Name is also used for peer description on downstream switches' uplinks.
        - group: <str; required; unique>

          # Define variables per node.
          nodes:

              # The Node Name is used as "hostname".
            - name: <str; required; unique>
              underlay_multicast:
                pim_sm:

                  # When enabled, configures multicast routing and by default configures PIM sparse-mode in the underlay on all:
                  #   - P2P uplink interfaces if enabled on uplink peer
                  #   - MLAG L3 peer interface if also enabled on MLAG peer
                  #   - l3_edge and core interfaces
                  # Overrides the global `underlay_multicast_pim_sm`.
                  enabled: <bool>

                  # Enable/Disable PIM sparse-mode on uplinks.
                  # Requires node setting `underlay_multicast.pim_sm.enabled: true` or, if unset, global `underlay_multicast_pim_sm: true`
                  uplinks: <bool; default=True>

                  # Limit PIM SM to the uplink_interfaces in this list. All interfaces if unset.
                  # Effective only when node settings `underlay_multicast.pim_sm.uplinks: true`.
                  uplink_interfaces:
                    - <str>

                  # Configure PIM sparse-mode in the underlay on the MLAG L3 peer VLAN interface.
                  mlag: <bool; default=True>
                static:

                  # When enabled, configures multicast routing and by default configures static multicast in the underlay on all:
                  #   - P2P uplink interfaces if enabled on uplink peer
                  #   - MLAG L3 peer interface if also enabled on MLAG peer
                  #   - l3_edge and core interfaces
                  # Overrides the global `underlay_multicast_static`.
                  enabled: <bool>

                  # Enable/Disable static multicast on uplinks.
                  # Requires node setting `underlay_multicast.static.enabled: true` or, if unset, global `underlay_multicast_static: true`
                  uplinks: <bool; default=True>

                  # Limit static multicast to the uplink_interfaces in this list. All interfaces if unset.
                  # Effective only when node settings `underlay_multicast.static.uplinks: true`.
                  uplink_interfaces:
                    - <str>

                  # Configure static multicast in the underlay on MLAG L3 peer interfacee.
                  mlag: <bool; default=True>
          underlay_multicast:
            pim_sm:

              # When enabled, configures multicast routing and by default configures PIM sparse-mode in the underlay on all:
              #   - P2P uplink interfaces if enabled on uplink peer
              #   - MLAG L3 peer interface if also enabled on MLAG peer
              #   - l3_edge and core interfaces
              # Overrides the global `underlay_multicast_pim_sm`.
              enabled: <bool>

              # Enable/Disable PIM sparse-mode on uplinks.
              # Requires node setting `underlay_multicast.pim_sm.enabled: true` or, if unset, global `underlay_multicast_pim_sm: true`
              uplinks: <bool; default=True>

              # Limit PIM SM to the uplink_interfaces in this list. All interfaces if unset.
              # Effective only when node settings `underlay_multicast.pim_sm.uplinks: true`.
              uplink_interfaces:
                - <str>

              # Configure PIM sparse-mode in the underlay on the MLAG L3 peer VLAN interface.
              mlag: <bool; default=True>
            static:

              # When enabled, configures multicast routing and by default configures static multicast in the underlay on all:
              #   - P2P uplink interfaces if enabled on uplink peer
              #   - MLAG L3 peer interface if also enabled on MLAG peer
              #   - l3_edge and core interfaces
              # Overrides the global `underlay_multicast_static`.
              enabled: <bool>

              # Enable/Disable static multicast on uplinks.
              # Requires node setting `underlay_multicast.static.enabled: true` or, if unset, global `underlay_multicast_static: true`
              uplinks: <bool; default=True>

              # Limit static multicast to the uplink_interfaces in this list. All interfaces if unset.
              # Effective only when node settings `underlay_multicast.static.uplinks: true`.
              uplink_interfaces:
                - <str>

              # Configure static multicast in the underlay on MLAG L3 peer interfacee.
              mlag: <bool; default=True>

      # Define variables per node.
      nodes:

          # The Node Name is used as "hostname".
        - name: <str; required; unique>
          underlay_multicast:
            pim_sm:

              # When enabled, configures multicast routing and by default configures PIM sparse-mode in the underlay on all:
              #   - P2P uplink interfaces if enabled on uplink peer
              #   - MLAG L3 peer interface if also enabled on MLAG peer
              #   - l3_edge and core interfaces
              # Overrides the global `underlay_multicast_pim_sm`.
              enabled: <bool>

              # Enable/Disable PIM sparse-mode on uplinks.
              # Requires node setting `underlay_multicast.pim_sm.enabled: true` or, if unset, global `underlay_multicast_pim_sm: true`
              uplinks: <bool; default=True>

              # Limit PIM SM to the uplink_interfaces in this list. All interfaces if unset.
              # Effective only when node settings `underlay_multicast.pim_sm.uplinks: true`.
              uplink_interfaces:
                - <str>

              # Configure PIM sparse-mode in the underlay on the MLAG L3 peer VLAN interface.
              mlag: <bool; default=True>
            static:

              # When enabled, configures multicast routing and by default configures static multicast in the underlay on all:
              #   - P2P uplink interfaces if enabled on uplink peer
              #   - MLAG L3 peer interface if also enabled on MLAG peer
              #   - l3_edge and core interfaces
              # Overrides the global `underlay_multicast_static`.
              enabled: <bool>

              # Enable/Disable static multicast on uplinks.
              # Requires node setting `underlay_multicast.static.enabled: true` or, if unset, global `underlay_multicast_static: true`
              uplinks: <bool; default=True>

              # Limit static multicast to the uplink_interfaces in this list. All interfaces if unset.
              # Effective only when node settings `underlay_multicast.static.uplinks: true`.
              uplink_interfaces:
                - <str>

              # Configure static multicast in the underlay on MLAG L3 peer interfacee.
              mlag: <bool; default=True>

    # PREVIEW - This datamodel is still under development and may change or get removed at any time.
    device_profiles:

        # Profile Name
      - name: <str; required; unique>
        underlay_multicast:
          pim_sm:

            # When enabled, configures multicast routing and by default configures PIM sparse-mode in the underlay on all:
            #   - P2P uplink interfaces if enabled on uplink peer
            #   - MLAG L3 peer interface if also enabled on MLAG peer
            #   - l3_edge and core interfaces
            # Overrides the global `underlay_multicast_pim_sm`.
            enabled: <bool>

            # Enable/Disable PIM sparse-mode on uplinks.
            # Requires node setting `underlay_multicast.pim_sm.enabled: true` or, if unset, global `underlay_multicast_pim_sm: true`
            uplinks: <bool; default=True>

            # Limit PIM SM to the uplink_interfaces in this list. All interfaces if unset.
            # Effective only when node settings `underlay_multicast.pim_sm.uplinks: true`.
            uplink_interfaces:
              - <str>

            # Configure PIM sparse-mode in the underlay on the MLAG L3 peer VLAN interface.
            mlag: <bool; default=True>
          static:

            # When enabled, configures multicast routing and by default configures static multicast in the underlay on all:
            #   - P2P uplink interfaces if enabled on uplink peer
            #   - MLAG L3 peer interface if also enabled on MLAG peer
            #   - l3_edge and core interfaces
            # Overrides the global `underlay_multicast_static`.
            enabled: <bool>

            # Enable/Disable static multicast on uplinks.
            # Requires node setting `underlay_multicast.static.enabled: true` or, if unset, global `underlay_multicast_static: true`
            uplinks: <bool; default=True>

            # Limit static multicast to the uplink_interfaces in this list. All interfaces if unset.
            # Effective only when node settings `underlay_multicast.static.uplinks: true`.
            uplink_interfaces:
              - <str>

            # Configure static multicast in the underlay on MLAG L3 peer interfacee.
            mlag: <bool; default=True>

    # PREVIEW - This datamodel is still under development and may change or get removed at any time.
    device_roles: # (1)!

        # Role Name
      - name: <str; required; unique>
        underlay_multicast:
          pim_sm:

            # When enabled, configures multicast routing and by default configures PIM sparse-mode in the underlay on all:
            #   - P2P uplink interfaces if enabled on uplink peer
            #   - MLAG L3 peer interface if also enabled on MLAG peer
            #   - l3_edge and core interfaces
            # Overrides the global `underlay_multicast_pim_sm`.
            enabled: <bool>

            # Enable/Disable PIM sparse-mode on uplinks.
            # Requires node setting `underlay_multicast.pim_sm.enabled: true` or, if unset, global `underlay_multicast_pim_sm: true`
            uplinks: <bool; default=True>

            # Limit PIM SM to the uplink_interfaces in this list. All interfaces if unset.
            # Effective only when node settings `underlay_multicast.pim_sm.uplinks: true`.
            uplink_interfaces:
              - <str>

            # Configure PIM sparse-mode in the underlay on the MLAG L3 peer VLAN interface.
            mlag: <bool; default=True>
          static:

            # When enabled, configures multicast routing and by default configures static multicast in the underlay on all:
            #   - P2P uplink interfaces if enabled on uplink peer
            #   - MLAG L3 peer interface if also enabled on MLAG peer
            #   - l3_edge and core interfaces
            # Overrides the global `underlay_multicast_static`.
            enabled: <bool>

            # Enable/Disable static multicast on uplinks.
            # Requires node setting `underlay_multicast.static.enabled: true` or, if unset, global `underlay_multicast_static: true`
            uplinks: <bool; default=True>

            # Limit static multicast to the uplink_interfaces in this list. All interfaces if unset.
            # Effective only when node settings `underlay_multicast.static.uplinks: true`.
            uplink_interfaces:
              - <str>

            # Configure static multicast in the underlay on MLAG L3 peer interfacee.
            mlag: <bool; default=True>

    # PREVIEW - This datamodel is still under development and may change or get removed at any time.
    devices:

        # The Node Name is used as "hostname".
        name: <str; required; unique>
        underlay_multicast:
          pim_sm:

            # When enabled, configures multicast routing and by default configures PIM sparse-mode in the underlay on all:
            #   - P2P uplink interfaces if enabled on uplink peer
            #   - MLAG L3 peer interface if also enabled on MLAG peer
            #   - l3_edge and core interfaces
            # Overrides the global `underlay_multicast_pim_sm`.
            enabled: <bool>

            # Enable/Disable PIM sparse-mode on uplinks.
            # Requires node setting `underlay_multicast.pim_sm.enabled: true` or, if unset, global `underlay_multicast_pim_sm: true`
            uplinks: <bool; default=True>

            # Limit PIM SM to the uplink_interfaces in this list. All interfaces if unset.
            # Effective only when node settings `underlay_multicast.pim_sm.uplinks: true`.
            uplink_interfaces:
              - <str>

            # Configure PIM sparse-mode in the underlay on the MLAG L3 peer VLAN interface.
            mlag: <bool; default=True>
          static:

            # When enabled, configures multicast routing and by default configures static multicast in the underlay on all:
            #   - P2P uplink interfaces if enabled on uplink peer
            #   - MLAG L3 peer interface if also enabled on MLAG peer
            #   - l3_edge and core interfaces
            # Overrides the global `underlay_multicast_static`.
            enabled: <bool>

            # Enable/Disable static multicast on uplinks.
            # Requires node setting `underlay_multicast.static.enabled: true` or, if unset, global `underlay_multicast_static: true`
            uplinks: <bool; default=True>

            # Limit static multicast to the uplink_interfaces in this list. All interfaces if unset.
            # Effective only when node settings `underlay_multicast.static.uplinks: true`.
            uplink_interfaces:
              - <str>

            # Configure static multicast in the underlay on MLAG L3 peer interfacee.
            mlag: <bool; default=True>

    # PREVIEW - This datamodel is still under development and may change or get removed at any time.
    # If a device is not defined under `devices`, AVD will check for a matching entry here, and apply the device settings for the first match.
    match_devices:

        # Regex pattern matching the full inventory hostname of one or more devices.
      - hostname_pattern: <str; required; unique>
        underlay_multicast:
          pim_sm:

            # When enabled, configures multicast routing and by default configures PIM sparse-mode in the underlay on all:
            #   - P2P uplink interfaces if enabled on uplink peer
            #   - MLAG L3 peer interface if also enabled on MLAG peer
            #   - l3_edge and core interfaces
            # Overrides the global `underlay_multicast_pim_sm`.
            enabled: <bool>

            # Enable/Disable PIM sparse-mode on uplinks.
            # Requires node setting `underlay_multicast.pim_sm.enabled: true` or, if unset, global `underlay_multicast_pim_sm: true`
            uplinks: <bool; default=True>

            # Limit PIM SM to the uplink_interfaces in this list. All interfaces if unset.
            # Effective only when node settings `underlay_multicast.pim_sm.uplinks: true`.
            uplink_interfaces:
              - <str>

            # Configure PIM sparse-mode in the underlay on the MLAG L3 peer VLAN interface.
            mlag: <bool; default=True>
          static:

            # When enabled, configures multicast routing and by default configures static multicast in the underlay on all:
            #   - P2P uplink interfaces if enabled on uplink peer
            #   - MLAG L3 peer interface if also enabled on MLAG peer
            #   - l3_edge and core interfaces
            # Overrides the global `underlay_multicast_static`.
            enabled: <bool>

            # Enable/Disable static multicast on uplinks.
            # Requires node setting `underlay_multicast.static.enabled: true` or, if unset, global `underlay_multicast_static: true`
            uplinks: <bool; default=True>

            # Limit static multicast to the uplink_interfaces in this list. All interfaces if unset.
            # Effective only when node settings `underlay_multicast.static.uplinks: true`.
            uplink_interfaces:
              - <str>

            # Configure static multicast in the underlay on MLAG L3 peer interfacee.
            mlag: <bool; default=True>
    ```

    1. Default Value

        ```yaml
        device_roles:
        - name: spine
          evpn_role: server
          ptp:
            priority1: 20
          cv_tags_topology_type: spine
        - name: l3leaf
          connected_endpoints: true
          evpn_role: client
          mlag_support: true
          network_services:
            l2: true
            l3: true
          vtep: true
          ptp:
            priority1: 30
          cv_tags_topology_type: leaf
        - name: l2leaf
          connected_endpoints: true
          mlag_support: true
          network_services:
            l2: true
          underlay_router: false
          uplink_type: port-channel
          cv_tags_topology_type: leaf
        ```
