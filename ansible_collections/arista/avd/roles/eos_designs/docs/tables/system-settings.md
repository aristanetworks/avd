<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>default_igmp_snooping_enabled</samp>](## "default_igmp_snooping_enabled") | Boolean |  | `True` |  | When set to false, disables IGMP snooping at fabric level and overrides per vlan settings.<br> |
    | [<samp>hardware_counters</samp>](## "hardware_counters") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;features</samp>](## "hardware_counters.features") | List, items: Dictionary |  |  |  | This data model allows to configure the list of hardware counters feature<br>available on Arista platforms.<br><br>The `name` key accepts a list of valid_values which MUST be updated to support<br>new feature as they are released in EOS.<br><br>The available values of the different keys like 'direction' or 'address_type'<br>are feature and hardware dependent and this model DOES NOT validate that the<br>combinations are valid. It is the responsability of the user of this data model<br>to make sure that the rendered CLI is accepted by the targeted device.<br><br>Examples:<br><br>  * Use:<br>    ```yaml<br>    hardware_counters:<br>      features:<br>        - name: ip<br>          direction: out<br>          layer3: true<br>          units_packets: true<br>    ```<br><br>    to render:<br>    ```eos<br>    hardware counter feature ip out layer3 units packets<br>    ```<br>  * Use:<br>    ```yaml<br>    hardware_counters:<br>      features:<br>        - name: route<br>          address_type: ipv4<br>          vrf: test<br>          prefix: 192.168.0.0/24<br>    ```<br><br>    to render:<br>    ```eos<br>    hardware counter feature route ipv4 vrf test 192.168.0.0/24<br>    ```<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "hardware_counters.features.[].name") | String |  |  | Valid Values:<br>- acl<br>- decap-group<br>- directflow<br>- ecn<br>- flow-spec<br>- gre tunnel interface<br>- ip<br>- mpls interface<br>- mpls lfib<br>- mpls tunnel<br>- multicast<br>- nexthop<br>- pbr<br>- pdp<br>- policing interface<br>- qos<br>- qos dual-rate-policer<br>- route<br>- routed-port<br>- subinterface<br>- tapagg<br>- traffic-class<br>- traffic-policy<br>- vlan<br>- vlan-interface<br>- vni decap<br>- vni encap<br>- vtep decap<br>- vtep encap |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction</samp>](## "hardware_counters.features.[].direction") | String |  |  | Valid Values:<br>- in<br>- out<br>- cpu | Most features support only 'in' and 'out'. Some like traffic-policy support 'cpu'.<br>Some features DO NOT have any direction.<br>This validation IS NOT made by the schemas.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;address_type</samp>](## "hardware_counters.features.[].address_type") | String |  |  | Valid Values:<br>- ipv4<br>- ipv6<br>- mac | Supported only for the following features:<br>- acl: [ipv4, ipv6, mac] if direction is 'out'<br>- multicast: [ipv4, ipv6]<br>- route: [ipv4, ipv6]<br>This validation IS NOT made by the schemas.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;layer3</samp>](## "hardware_counters.features.[].layer3") | Boolean |  |  |  | Supported only for the 'ip' feature<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "hardware_counters.features.[].vrf") | String |  |  |  | Supported only for the 'route' feature.<br>This validation IS NOT made by the schemas.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefix</samp>](## "hardware_counters.features.[].prefix") | String |  |  |  | Supported only for the 'route' feature.<br>Mandatory for the 'route' feature.<br>This validation IS NOT made by the schemas.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;units_packets</samp>](## "hardware_counters.features.[].units_packets") | Boolean |  |  |  |  |
    | [<samp>internal_vlan_order</samp>](## "internal_vlan_order") | Dictionary |  | See (+) on YAML tab |  | Internal vlan allocation order and range. |
    | [<samp>&nbsp;&nbsp;allocation</samp>](## "internal_vlan_order.allocation") | String | Required |  | Valid Values:<br>- ascending<br>- descending |  |
    | [<samp>&nbsp;&nbsp;range</samp>](## "internal_vlan_order.range") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;beginning</samp>](## "internal_vlan_order.range.beginning") | Integer | Required |  | Min: 2<br>Max: 4094 | First VLAN ID. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ending</samp>](## "internal_vlan_order.range.ending") | Integer | Required |  | Min: 2<br>Max: 4094 | Last VLAN ID. |
    | [<samp>mac_address_table</samp>](## "mac_address_table") | Dictionary |  |  |  | MAC address-table aging time.<br>Use to change the EOS default of 300.<br> |
    | [<samp>&nbsp;&nbsp;aging_time</samp>](## "mac_address_table.aging_time") | Integer |  |  | Min: 0<br>Max: 1000000 | Aging time in seconds 10-1000000.<br>Enter 0 to disable aging.<br> |
    | [<samp>queue_monitor_length</samp>](## "queue_monitor_length") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;enabled</samp>](## "queue_monitor_length.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;notifying</samp>](## "queue_monitor_length.notifying") | Boolean |  |  |  | If True, `eos_designs` will configure `queue-monitor length notifying` according to the<br>`platform_settings.[].feature_support.queue_monitor_length_notify` setting. |
    | [<samp>&nbsp;&nbsp;default_thresholds</samp>](## "queue_monitor_length.default_thresholds") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;high</samp>](## "queue_monitor_length.default_thresholds.high") | Integer | Required |  |  | Default high threshold for Ethernet Interfaces.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;low</samp>](## "queue_monitor_length.default_thresholds.low") | Integer |  |  |  | Default low threshold for Ethernet Interfaces.<br>Low threshold support is platform dependent.<br> |
    | [<samp>&nbsp;&nbsp;log</samp>](## "queue_monitor_length.log") | Integer |  |  |  | Logging interval in seconds |
    | [<samp>&nbsp;&nbsp;cpu</samp>](## "queue_monitor_length.cpu") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;thresholds</samp>](## "queue_monitor_length.cpu.thresholds") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;high</samp>](## "queue_monitor_length.cpu.thresholds.high") | Integer | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;low</samp>](## "queue_monitor_length.cpu.thresholds.low") | Integer |  |  |  |  |
    | [<samp>redundancy</samp>](## "redundancy") | Dictionary |  |  |  | Redundancy for chassis platforms with dual supervisors | Optional. |
    | [<samp>&nbsp;&nbsp;protocol</samp>](## "redundancy.protocol") | String |  |  | Valid Values:<br>- sso<br>- rpr |  |
    | [<samp>serial_number</samp>](## "serial_number") | String |  |  |  | Serial Number of the device.<br>Used for documentation purpose in the fabric documentation as can also be used by the 'eos_config_deploy_cvp' role.<br>"serial_number" can also be set directly under node type settings.<br>If both are set, the value under node type settings takes precedence.<br> |
    | [<samp>system_mac_address</samp>](## "system_mac_address") | String |  |  |  | Set to the same MAC address as available in "show version" on the device.<br>"system_mac_address" can also be set under node type settings.<br>If both are set, the value under node type settings takes precedence. |

=== "YAML"

    ```yaml
    default_igmp_snooping_enabled: <bool>
    hardware_counters:
      features:
        - name: <str>
          direction: <str>
          address_type: <str>
          layer3: <bool>
          vrf: <str>
          prefix: <str>
          units_packets: <bool>
    internal_vlan_order: # (1)!
      allocation: <str>
      range:
        beginning: <int>
        ending: <int>
    mac_address_table:
      aging_time: <int>
    queue_monitor_length:
      enabled: <bool>
      notifying: <bool>
      default_thresholds:
        high: <int>
        low: <int>
      log: <int>
      cpu:
        thresholds:
          high: <int>
          low: <int>
    redundancy:
      protocol: <str>
    serial_number: <str>
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
