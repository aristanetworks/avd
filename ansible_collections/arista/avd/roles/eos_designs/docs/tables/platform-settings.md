<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>platform_settings</samp>](## "platform_settings") | List, items: Dictionary |  | See (+) on YAML tab |  |  |
    | [<samp>&nbsp;&nbsp;-&nbsp;platforms</samp>](## "platform_settings.[].platforms") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "platform_settings.[].platforms.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;trident_forwarding_table_partition</samp>](## "platform_settings.[].trident_forwarding_table_partition") | String |  |  |  | Only applied when evpn_multicast is true. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;reload_delay</samp>](## "platform_settings.[].reload_delay") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag</samp>](## "platform_settings.[].reload_delay.mlag") | Integer |  |  | Min: 0<br>Max: 86400 | In seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;non_mlag</samp>](## "platform_settings.[].reload_delay.non_mlag") | Integer |  |  | Min: 0<br>Max: 86400 | In seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;tcam_profile</samp>](## "platform_settings.[].tcam_profile") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;lag_hardware_only</samp>](## "platform_settings.[].lag_hardware_only") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;default_interface_mtu</samp>](## "platform_settings.[].default_interface_mtu") | Integer |  |  | Min: 68<br>Max: 65535 | Default interface MTU configured on EOS under "interface defaults".<br>Takes precedence over the root key "default_interface_mtu".<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;feature_support</samp>](## "platform_settings.[].feature_support") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;queue_monitor_length_notify</samp>](## "platform_settings.[].feature_support.queue_monitor_length_notify") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interface_storm_control</samp>](## "platform_settings.[].feature_support.interface_storm_control") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;poe</samp>](## "platform_settings.[].feature_support.poe") | Boolean |  | `False` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;per_interface_mtu</samp>](## "platform_settings.[].feature_support.per_interface_mtu") | Boolean |  | `True` |  | Support for configuration of per interface MTU for p2p links, MLAG SVIs and Network Services.<br>Effectively this means that all settings regarding interface MTU will be ignored if this is false.<br>Platforms without support for per interface MTU can use a single default interface MTU setting. Set this via "default_interface_mtu"<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp_update_wait_install</samp>](## "platform_settings.[].feature_support.bgp_update_wait_install") | Boolean |  | `True` |  | Disables FIB updates and route advertisement when the BGP instance is initiated until the BGP convergence state is reached.<br>Can be overridden by setting "bgp_update_wait_install" host/group_vars.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp_update_wait_for_convergence</samp>](## "platform_settings.[].feature_support.bgp_update_wait_for_convergence") | Boolean |  | `True` |  | Do not advertise reachability to a prefix until that prefix has been installed in hardware.<br>This will eliminate any temporary black holes due to a BGP speaker advertising reachability to a prefix that may not yet be installed into the forwarding plane.<br>Can be overridden by setting "bgp_update_wait_for_convergence" host/group_vars.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;management_interface</samp>](## "platform_settings.[].management_interface") | String |  | `Management1` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "platform_settings.[].raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the root level of the final EOS configuration. |
    | [<samp>platform_speed_groups</samp>](## "platform_speed_groups") | List, items: Dictionary |  |  |  | Set Hardware Speed Groups per Platform. |
    | [<samp>&nbsp;&nbsp;-&nbsp;platform</samp>](## "platform_speed_groups.[].platform") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;speeds</samp>](## "platform_speed_groups.[].speeds") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;speed</samp>](## "platform_speed_groups.[].speeds.[].speed") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;speed_groups</samp>](## "platform_speed_groups.[].speeds.[].speed_groups") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "platform_speed_groups.[].speeds.[].speed_groups.[]") | String |  |  |  |  |

=== "YAML"

    ```yaml
    platform_settings: # (1)!
      - platforms:
          - <str>

        # Only applied when evpn_multicast is true.
        trident_forwarding_table_partition: <str>
        reload_delay:

          # In seconds.
          mlag: <int; 0-86400>

          # In seconds.
          non_mlag: <int; 0-86400>
        tcam_profile: <str>
        lag_hardware_only: <bool>

        # Default interface MTU configured on EOS under "interface defaults".
        # Takes precedence over the root key "default_interface_mtu".
        default_interface_mtu: <int; 68-65535>
        feature_support:
          queue_monitor_length_notify: <bool; default=True>
          interface_storm_control: <bool; default=True>
          poe: <bool; default=False>

          # Support for configuration of per interface MTU for p2p links, MLAG SVIs and Network Services.
          # Effectively this means that all settings regarding interface MTU will be ignored if this is false.
          # Platforms without support for per interface MTU can use a single default interface MTU setting. Set this via "default_interface_mtu"
          per_interface_mtu: <bool; default=True>

          # Disables FIB updates and route advertisement when the BGP instance is initiated until the BGP convergence state is reached.
          # Can be overridden by setting "bgp_update_wait_install" host/group_vars.
          bgp_update_wait_install: <bool; default=True>

          # Do not advertise reachability to a prefix until that prefix has been installed in hardware.
          # This will eliminate any temporary black holes due to a BGP speaker advertising reachability to a prefix that may not yet be installed into the forwarding plane.
          # Can be overridden by setting "bgp_update_wait_for_convergence" host/group_vars.
          bgp_update_wait_for_convergence: <bool; default=True>
        management_interface: <str; default="Management1">

        # EOS CLI rendered directly on the root level of the final EOS configuration.
        raw_eos_cli: <str>

    # Set Hardware Speed Groups per Platform.
    platform_speed_groups:
      - platform: <str; required; unique>
        speeds:
          - speed: <str; required; unique>
            speed_groups:
              - <str>
    ```

    1. Default Value

        ```yaml
        platform_settings:
        - feature_support:
            queue_monitor_length_notify: false
          platforms:
          - default
          reload_delay:
            mlag: 300
            non_mlag: 330
        - feature_support:
            queue_monitor_length_notify: false
          platforms:
          - 7050X3
          - 720XP
          - 722XP
          reload_delay:
            mlag: 300
            non_mlag: 330
          trident_forwarding_table_partition: flexible exact-match 16384 l2-shared 98304 l3-shared
            131072
        - lag_hardware_only: true
          platforms:
          - 7280R
          - 7280R2
          - 7020R
          reload_delay:
            mlag: 900
            non_mlag: 1020
          tcam_profile: vxlan-routing
        - platforms:
          - 7280R3
          reload_delay:
            mlag: 900
            non_mlag: 1020
        - lag_hardware_only: true
          management_interface: Management0
          platforms:
          - 7500R
          - 7500R2
          reload_delay:
            mlag: 900
            non_mlag: 1020
          tcam_profile: vxlan-routing
        - management_interface: Management0
          platforms:
          - 7500R3
          - 7800R3
          reload_delay:
            mlag: 900
            non_mlag: 1020
        - management_interface: Management0
          platforms:
          - 7368X4
          reload_delay:
            mlag: 300
            non_mlag: 330
        - management_interface: Management0
          platforms:
          - 7300X3
          reload_delay:
            mlag: 1200
            non_mlag: 1320
          trident_forwarding_table_partition: flexible exact-match 16384 l2-shared 98304 l3-shared
            131072
        - feature_support:
            bgp_update_wait_for_convergence: false
            bgp_update_wait_install: false
            interface_storm_control: false
            queue_monitor_length_notify: false
          platforms:
          - VEOS
          - VEOS-LAB
          - vEOS
          - vEOS-lab
          reload_delay:
            mlag: 300
            non_mlag: 330
        - feature_support:
            bgp_update_wait_for_convergence: false
            bgp_update_wait_install: false
            interface_storm_control: false
            queue_monitor_length_notify: false
          management_interface: Management0
          platforms:
          - CEOS
          - cEOS
          - ceos
          - cEOSLab
          reload_delay:
            mlag: 300
            non_mlag: 330
        ```
