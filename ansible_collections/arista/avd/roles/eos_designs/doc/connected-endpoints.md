# Connected Endpoints

- The connected endpoints variables, define endpoints that connect to the fabric on leaf interface(s).
- The connected endpoints are leveraged to define any device that connects to a leaf switch ports, i.e.: servers, firewalls, routers, load balancers, and storage arrays.
- Connected endpoints key/value pairs are designed to be extended for your own needs and leveraged to configure the endpoint itself.

## Variables and Options

### Connected Endpoints Keys

```yaml
# Define connected endpoints keys, to define grouping of endpoints connecting to the fabric.
# This provides the ability to define various keys of your choice to better organize/group your data.
# This should be defined in top level group_var for the fabric.
connected_endpoints_keys:
  < key_1 >:
    type: < type used for documentation >
  < key_2 >:
    type: < type used for documentation >
```

```yaml
# Example
# The below key/pair values are the role defaults.
connected_endpoints_keys:
  servers:
    type: server
  firewalls:
    type: firewall
  routers:
    type: router
  load_balancers:
    type: load_balancer
  storage_arrays:
    type: storage_array
```

### Port Profiles

```yaml
# Optional profiles to apply on endpoints facing interfaces
# Each profile can support all or some of the following keys according to your own needs.
# Keys are the same used under endpoints adapters. Keys defined under endpoints adapters take precedence.
# Port_profiles can refer to another port_profile to inherit settings in up to two levels (adapter->profile->parent_profile).
port_profiles:
  < port_profile_1 >:
    parent_profile: < port_profile_name >
    speed: < interface_speed | forced interface_speed | auto interface_speed >
    enabled: < true | false >
    mode: < access | dot1q-tunnel | trunk >
    mtu: < mtu >
    l2_mtu: < l2_mtu - if defined this profile should only be used for platforms supporting the "l2 mtu" CLI >
    native_vlan: <native vlan number>
    vlans: < vlans as string >
    spanning_tree_portfast: < edge | network >
    spanning_tree_bpdufilter: < "enabled" | true | "disabled" >
    spanning_tree_bpduguard: < "enabled" | true | "disabled" >
    flowcontrol:
      received: < "received" | "send" | "on" >
    qos_profile: < qos_profile_name >
    ptp:
      enable: < true | false >
    storm_control:
      all:
        level: < Configure maximum storm-control level >
        unit: < percent | pps > | Optional var and is hardware dependant - default is percent)
      broadcast:
        level: < Configure maximum storm-control level >
        unit: < percent | pps > | Optional var and is hardware dependant - default is percent)
      multicast:
        level: < Configure maximum storm-control level >
        unit: < percent | pps > | Optional var and is hardware dependant - default is percent)
      unknown_unicast:
        level: < Configure maximum storm-control level >
        unit: < percent | pps > | Optional var and is hardware dependant - default is percent)
    port_channel:
      description: < port_channel_description >
      mode: < "active" | "passive" | "on" >
      lacp_fallback:
        mode: < static > | Currently only static mode is supported
        timeout: < timeout in seconds > | Optional - default is 90 seconds

# Dictionary key of connected endpoint as defined in connected_endpoints_keys
# This should be applied to group_vars or host_vars where endpoints are connecting.
< connected_endpoints_keys.key >:

  # Endpoint name, this will be used in the switchport description
  < endpoint_1 >:

    # rack is used for documentation purposes only
    rack: < rack_id >

    # A list of adapter(s), group by adapters leveraging the same port-profile.
    adapters:

      # Example of stand-alone adapter

        # Adapter speed - if not specified will be auto.
      - speed: < interface_speed | forced interface_speed | auto interface_speed >

        # Local endpoint port(s) | required
        endpoint_ports: [ < interface_name > ]

        # List of port(s) connected to switches | required
        switch_ports: [ < switchport_interface > ]

        # List of switch(es) | required
        switches: [ < device > ]

        # Port-profile name, to inherit configuration.
        profile: < port_profile_name >

        # Administrative state | optional - default is true
        # setting to false will set port to 'shutdown' in intended configuration
        enabled: < true | false >

        # Interface mode | required
        mode: < access | dot1q-tunnel | trunk >

        # Native VLAN for a trunk port | optional
        native_vlan: <native vlan number>

        # Interface vlans | required
        vlans: < vlans as string >

        # Spanning Tree
        spanning_tree_portfast: < edge | network >
        spanning_tree_bpdufilter: < "enabled" | true | "disabled" >
        spanning_tree_bpduguard: < "enabled" | true | "disabled" >

        # Flow control | Optional
        flowcontrol:
          received: < "received" | "send" | "on" >

        # QOS Profile | Optional
        qos_profile: < qos_profile_name >

        # PTP Enable | Optional
        ptp:
          enable: < true | false >

        # Configure the downstream interfaces of a respective Link Tracking Group | Optional
        # If port_channel is defined in an adapter then port-channel interface is configured to be the downstream
        # else all the ethernet-interfaces will be configured as downstream -> to configure single-active EVPN multihomed networks
        link_tracking:
          enabled: < true | false >
          # The default group name is taken from fabric variable of the switch, link_tracking.groups[0].name with default value being "LT_GROUP1".
          # Optional if default link_tracking settings are configured on the node.
          name: < tracking_group_name >

        # EOS CLI rendered directly on the ethernet interface in the final EOS configuration
        raw_eos_cli: |
          < multiline eos cli >

        # Custom structured config added under ethernet_interfaces.<interface> for eos_cli_config_gen
        structured_config: < dictionary >

        # Storm control settings applied on port toward the endpoint | Optional
        storm_control:
          all:
            level: < Configure maximum storm-control level >
            unit: < percent | pps > | Optional var and is hardware dependant - default is percent)
          broadcast:
            level: < Configure maximum storm-control level >
            unit: < percent | pps > | Optional var and is hardware dependant - default is percent)
          multicast:
            level: < Configure maximum storm-control level >
            unit: < percent | pps > | Optional var and is hardware dependant - default is percent)
          unknown_unicast:
            level: < Configure maximum storm-control level >
            unit: < percent | pps > | Optional var and is hardware dependant - default is percent)

        # Monitor Session configuration: use defined switchports as source or destination for monitoring sessions | Optional
        monitor_sessions:
          - name: < session_name >
            role: < source | destination >
            source_settings:
              direction: < rx | tx | both >
              access_group:
                type: < ip | ipv6 | mac >
                name: < acl_name >
                priority: < priority >
            # Session settings are defined per session name. Different session_settings with for same session name will be combined/merged
            session_settings:
              encapsulation_gre_metadata_tx: < true | false >
              header_remove_size: < bytes >
              access_group:
                type: < ip | ipv6 | mac >
                name: < acl_name >
              rate_limit_per_ingress_chip: < "<int> bps" | "<int> kbps" | "<int> mbps" >
              rate_limit_per_egress_chip: < "<int> bps" | "<int> kbps" | "<int> mbps" >
              sample: < int >
              truncate:
                enabled: < true | false >
                size: < bytes >

      # Example of port-channel adapter
      - endpoint_ports: [ < interface_name_1 > , < interface_name_2 > ]
        switch_ports: [ < switchport_interface_1 >, < switchport_interface_2 > ]
        switches: [ < device_1 >, < device_2 > ]
        profile: < port_profile_name >

        # Port- Channel
        port_channel:

          # Port-Channel Description.
          description: < port_channel_description >

          # Port-Channel administrative state | optional - default is true
          # setting to false will set port to 'shutdown' in intended configuration
          enabled: < true | false >

          # Port-Channel Mode.
          mode: < "active" | "passive" | "on" >

          # LACP Fallback configuration | Optional
          lacp_fallback:
            mode: < static > Currently only static mode is supported
            timeout: < timeout in seconds > | Optional - default is 90 seconds

          # Port-Channel L2 Subinterfaces
          # Subinterfaces are only supported on routed port-channels, which means they cannot be configured on MLAG port-channels.
          # Setting short_esi: auto generates the short_esi automatically using a hash of configuration elements.
          # Please see the notes under "EVPN A/A ESI dual-attached endpoint scenario" before setting short_esi: auto.
          subinterfaces:
          - number: < subinterface number >
            short_esi: < 0000:0000:0000 | auto > Required for multihomed port-channels with subinterfaces
            vlan_id: < VLAN ID to bridge > | Optional - default is subinterface number
            # Flexible encapsulation parameters
            encapsulation_vlan:
              client_dot1q: < client vlan id encapsulation > | Optional - default is subinterface number

          # EOS CLI rendered directly on the port-channel interface in the final EOS configuration
          raw_eos_cli: |
            < multiline eos cli >

          # Custom structured config added under port_channel_interfaces.<interface> for eos_cli_config_gen
          structured_config: < dictionary >

  # Setting short_esi: auto generates the short_esi automatically using a hash of configuration elements.
  # Please see the notes under "EVPN A/A ESI dual-attached endpoint scenario" before setting short_esi: auto.
  < endpoint_2 >:
    rack: RackC
    adapters:
      - speed: < interface_speed | forced interface_speed | auto interface_speed >
        endpoint_ports: [ < interface_name > ]
        switch_ports: [ < switchport_interface > ]
        switches: [ < device > ]
        profile: < port_profile_name >
      - endpoint_ports: [ < interface_name_1 > , < interface_name_2 > ]
        switch_ports: [ < switchport_interface_1 >, < switchport_interface_2 > ]
        switches: [ < device_1 >, < device_2 > ]
        profile: < port_profile_name >
        port_channel:
          description: < port_channel_description >
          mode: '< active | passive | on >'
          short_esi: < 0000:0000:0000 | auto >
```

## Examples

```yaml
# Example

connected_endpoints_keys:
  servers:
    type: server
  firewalls:
    type: firewall
  routers:
    type: router


port_profiles:

  VM_Servers:
    mode: trunk
    vlans: "110-111,120-121,130-131"
    spanning_tree_portfast: edge

  MGMT:
    mode: access
    vlans: "110"

  DB_Clusters:
    mode: trunk
    vlans: "140-141"

# servers
servers:

  server01:
    rack: RackB
    adapters:

      # Single homed interface from E0 toward DC1-LEAF1A_Eth5
      - endpoint_ports: [ E0 ]
        switch_ports: [ Ethernet5 ]
        switches: [ DC1-LEAF1A ]
        profile: MGMT

      # MLAG dual-homed connection from E1 to DC1-LEAF2A_Eth10
      #                            from E2 to DC1-LEAF2B_Eth10
      - endpoint_ports: [ E1, E2 ]
        switch_ports: [ Ethernet10, Ethernet10 ]
        switches: [ DC1-LEAF2A, DC1-LEAF2B ]
        profile: DB_Clusters
        port_channel:
          description: PortChanne1
          mode: active

  server03:
    rack: RackC
    adapters:

      # MLAG dual-homed connection from E0 to DC1-SVC3A_Eth10
      #                            from E1 to DC1-SVC3B_Eth10
      - endpoint_ports: [ E0, E1 ]
        switch_ports: [ Ethernet10, Ethernet10 ]
        switches: [ DC1-SVC3A, DC1-SVC3B ]
        profile: VM_Servers
        port_channel:
          description: PortChanne1
          mode: active
# Firewall
firewalls:
  FIREWALL01:
    rack: RackB
    adapters:
      - endpoint_ports: [ E0, E1 ]
        switch_ports: [ Ethernet20, Ethernet20 ]
        switches: [ DC1-LEAF2A, DC1-LEAF2B ]
        profile: TENANT_A_B
        port_channel:
          description: PortChanne1
          mode: active

# Routers
routers:
  ROUTER01:
    rack: RackB
    adapters:
      - endpoint_ports: [ Eth0, Eth1 ]
        switch_ports: [ Ethernet21, Ethernet21 ]
        switches: [ DC1-LEAF2A, DC1-LEAF2B ]
        profile: TENANT_A
```

## Single attached endpoint scenario

Single attached interface from `E0` toward `DC1-LEAF1A` interface `Eth5`

```yaml
servers:
  server01:
    rack: RackB
    adapters:
      - endpoint_ports: [ E0 ]
        switch_ports: [ Ethernet5 ]
        switches: [ DC1-LEAF1A ]
        profile: MGMT
```

## MLAG dual-attached endpoint scenario

MLAG dual-homed connection:

- From `E0` to `DC1-SVC3A` interface `Eth10`
- From `E1` to `DC1-SVC3B` interface `Eth10`

```yaml
servers:
  server01:
    rack: RackB
    adapters:
      - endpoint_ports: [ E0, E1 ]
        switch_ports: [ Ethernet10, Ethernet10 ]
        switches: [ DC1-SVC3A, DC1-SVC3B ]
        profile: VM_Servers
        port_channel:
          description: PortChanne1
          mode: active
```

## EVPN A/A ESI dual-attached endpoint scenario

To help provide consistency when configuring EVPN A/A ESI values, arista.avd provides an abstraction in the form of a `short_esi` key.
`short_esi` is an abbreviated 3 octets value to encode [Ethernet Segment ID](https://tools.ietf.org/html/rfc7432#section-8.3.1) and LACP ID.
Transformation from abstraction to network values is managed by a [filter_plugin](../../../plugins/README.md) and provides following result:

- _EVPN ESI_: 000:000:0303:0202:0101
- _LACP ID_: 0303.0202.0101
- _Route Target_: 03:03:02:02:01:01

In addition, setting the `short_esi` key to `auto` generates the short_esi automatically using a hash of the following data elements:

- Port-Channel Interfaces: first two uplink switch hostnames, the ports on those switches, the corresponding endpoint ports and the channel-group ID.
- Port-Channel Subinterface: first two uplink switch hostname, the ports on those switches, the corresponding endpoint ports, the channel-group ID and the subinterface number.

It should be noted that arista.avd does not currently check for hash collisions when using `short_esi: auto` and while the risk of this happening is non-zero, it is small.

Active/Active multihoming connections:

- From `E0` to `DC1-SVC3A` interface `Eth10`
- From `E1` to `DC1-SVC4A` interface `Eth10`

```yaml
servers:
  server01:
    rack: RackB
    adapters:
      - endpoint_ports: [ E0, E1 ]
        switch_ports: [ Ethernet10, Ethernet10 ]
        switches: [ DC1-SVC3A, DC1-SVC4A ]
        profile: VM_Servers
        port_channel:
          description: PortChanne1
          mode: active
          short_esi: 0303:0202:0101
```
