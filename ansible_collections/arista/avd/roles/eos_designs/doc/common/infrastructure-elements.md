# Infrastructure Elements Port Connectivity

- The infrastructure elements port connectivity variables, define infrastructure elements that connect to the fabric on leaf interface(s).
- The infrastructure elements is leverage to define any device that connect to a leaf switch ports, i.e.: servers, firewalls, routers, load balancers and storage arrays.
- Infrastructure elements key/pair value are design to be extend for your onw needs, and leveraged to configure the infrastructure element itself.


## Variables and Options:

### Infrastructure Elements Keys

```yaml
# Define infrastructure elements keys and type for documentation
# This provides the ability to define various key of your choice to better organize your data.
# The below key/pair values are default provided by the role.
infrastructure_elements_keys:
  servers:
    type: server
  firewalls:
    type: firewall
  routers:
    type: router
  load_balancers:
    type: load_balancer
  storage_arrays:
    type: storage
```

### Port Profiles

```yaml
# Optional profiles to apply on Server facing interfaces
# Each profile can support all or some of the following keys according your own needs.
# Keys are the same used under Server Adapters.
# Keys defined under Server Adapters take precedence.
port_profiles:
  < port_profile_1 >:
    speed: < interface_speed | forced interface_speed | auto interface_speed >
    mode: < access | dot1q-tunnel | trunk >
    l2_mtu: < l2_mtu - if defined this profile should only be used for platforms supporting the "l2 mtu" CLI >
    native_vlan: <native vlan number>
    vlans: < vlans as string >
    spanning_tree_portfast: < edge | network >
    spanning_tree_bpdufilter: < true | false >
    spanning_tree_bpduguard: < true | false >
    flowcontrol:
      received: < received | send | on >
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
      mode: < active | passive | on >
      lacp_fallback:
        mode: < static > | Currently only static mode is supported
        timeout: < timeout in seconds > | Optional - default is 90 seconds

# Dictionary of servers, a device attaching to a L2 switched port(s)
<infrastructure_elements_keys.key>:

  # Server name, this will be used in the switchport description
  < server_1 >:

    # rack is used for documentation purposes only
    rack: < rack_id >

    # A list of adapter(s), group by adapters leveraging the same port-profile.
    adapters:

      # Example of stand-alone adapter

        # Adapter speed - if not specified will be auto.
      - speed: < interface_speed | forced interface_speed | auto interface_speed >

        # Local server port(s)
        server_ports: [ < interface_name > ]

        # List of port(s) connected to switches
        switch_ports: [ < switchport_interface > ]

        # List of switche(s)
        switches: [ < device > ]

        # Port-profile name, to inherit configuration.
        profile: < port_profile_name >

        # Interface mode | required
        mode: < access | dot1q-tunnel | trunk >

        # Native VLAN for a trunk port | optional
        native_vlan: <native vlan number>

        # Interface vlans | required
        vlans: < vlans as string >

        # Spanning Tree
        spanning_tree_portfast: < edge | network >
        spanning_tree_bpdufilter: < true | false >
        spanning_tree_bpduguard: < true | false >

        # Flow control | Optional
        flowcontrol:
          received: < received | send | on >

        # QOS Profile | Optional
        qos_profile: < qos_profile_name >

        # PTP Enable | Optional
        ptp:
          enable: < true | false >

      < port_profile_2 >:
        mode: < access | dot1q-tunnel | trunk >
        vlans: < vlans as string >

        # Storm control settings applied on port toward server | Optional
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


      # Example of port-channel adpater
      - server_ports: [ < interface_name_1 > , < interface_name_2 > ]
        switch_ports: [ < switchport_interface_1 >, < switchport_interface_2 > ]
        switches: [ < device_1 >, < device_2 > ]
        profile: < port_profile_name >

        # Port- Channel
        port_channel:

          # Port-Channel Description.
          description: < port_channel_description >

          # Port-Channel Mode.
          mode: < active | passive | on >

          # LACP Fallback configuration | Optional
          lacp_fallback:
            mode: < static > Currently only static mode is supported
            timeout: < timeout in seconds > | Optional - default is 90 seconds

  < server_2 >:
    rack: RackC
    adapters:
      - speed: < interface_speed | forced interface_speed | auto interface_speed >
        server_ports: [ < interface_name > ]
        switch_ports: [ < switchport_interface > ]
        switches: [ < device > ]
        profile: < port_profile_name >
      - server_ports: [ < interface_name_1 > , < interface_name_2 > ]
        switch_ports: [ < switchport_interface_1 >, < switchport_interface_2 > ]
        switches: [ < device_1 >, < device_2 > ]
        profile: < port_profile_name >
        port_channel:
          description: < port_channel_description >
          mode: '< active | passive | on >'
          short_esi: < 0000:0000:0000 >
```
## Examples

```yaml
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


servers:

  server01:
    rack: RackB
    adapters:

      # Single homed interface from E0 toward DC1-LEAF1A_Eth5
      - server_ports: [ E0 ]
        switch_ports: [ Ethernet5 ]
        switches: [ DC1-LEAF1A ]
        profile: MGMT

      # MLAG dual-homed connection from E1 to DC1-LEAF2A_Eth10
      #                            from E2 to DC1-LEAF2B_Eth10
      - server_ports: [ E1, E2 ]
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
      - server_ports: [ E0, E1 ]
        switch_ports: [ Ethernet10, Ethernet10 ]
        switches: [ DC1-SVC3A, DC1-SVC3B ]
        profile: VM_Servers
        port_channel:
          description: PortChanne1
          mode: active
```

## Single attached server scenario

Single attached interface from `E0` toward `DC1-LEAF1A` interface `Eth5`

```yaml
servers:
  server01:
    rack: RackB
    adapters:
      - server_ports: [ E0 ]
        switch_ports: [ Ethernet5 ]
        switches: [ DC1-LEAF1A ]
        profile: MGMT
```

## MLAG dual-attached server scenario

MLAG dual-homed connection:

- From `E0` to `DC1-SVC3A` interface `Eth10`
- From `E1` to `DC1-SVC3B` interface `Eth10`

```yaml
servers:
  server01:
    rack: RackB
    adapters:
      - server_ports: [ E0, E1 ]
        switch_ports: [ Ethernet10, Ethernet10 ]
        switches: [ DC1-SVC3A, DC1-SVC3B ]
        profile: VM_Servers
        port_channel:
          description: PortChanne1
          mode: active
```

## EVPN A/A ESI dual-attached server scenario

To help provide consistency when configuring EVPN A/A ESI values, arista.avd provides an abstraction in the form of a `short_esi` key.
`short_esi` is an abbreviated 3 octets value to encode [Ethernet Segment ID](https://tools.ietf.org/html/rfc7432#section-8.3.1) and LACP ID.
Transformation from abstraction to network values is managed by a [filter_plugin](../../../../plugins/README.md) and provides following result:

- _EVPN ESI_: 000:000:0303:0202:0101
- _LACP ID_: 0303.0202.0101
- _Route Target_: 03:03:02:02:01:01

Active/Active multihoming connections:

- From `E0` to `DC1-SVC3A` interface `Eth10`
- From `E1` to `DC1-SVC4A` interface `Eth10`

```yaml
servers:
  server01:
    rack: RackB
    adapters:
      - server_ports: [ E0, E1 ]
        switch_ports: [ Ethernet10, Ethernet10 ]
        switches: [ DC1-SVC3A, DC1-SVC4A ]
        profile: VM_Servers
        port_channel:
          description: PortChanne1
          mode: active
          short_esi: 0303:0202:0101
```
