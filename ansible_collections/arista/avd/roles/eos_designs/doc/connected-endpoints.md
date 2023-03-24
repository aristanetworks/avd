# Connected Endpoints

AVD supports two different data models for defining connectivity to endpoints:

- "Connected Endpoints" is an endpoint-centric model intended for servers or other use cases where most ports have unique configurations.
- "Network Ports" is a compact and port-centric model intended for configuration of generic port configurations on large ranges of ports.

Both data models share the same underlying implementation and can coexist without conflicts, as long as the same switchports are not
defined in both models.

Both data models support variable inheritance from profiles defined under [`port_profiles`](#port-profiles). The profiles can be shared between the models. Any setting defined under the `port_profiles` will be inherited from `parent_profile` to `profile` to `adapter`.

## Connected Endpoints

- The connected endpoints variables define connectivity from the perspective of the endpoints that connect to the fabric.
- Each endpoint can have one or more `adapters` defined, under which the connected `switches`, `switch_ports` and `endpoint_ports`
  must be set.
- If port_channel mode is enabled under one "adapter", all switch_ports connected to that "adapter" will become part of this port-channel.
- The keys used to define `connected_endpoints` are configurable using [`connected_endpoints_keys`](#connected-endpoints-keys).
  The default keys are: `servers`, `firewalls`, `routers`, `load_balancers` and `storage_arrays`.

## Network Ports

- `network_ports` is intended to be used with `port_profiles` and `parent_profiles` to keep the configuration generic and compact, but all
  features and keys supported under `connected_endpoints.adapters` is also supported directly under `network_ports`.
- Since all ranges defined under `network_ports` will be expanded to individual port configurations, by default each port will be configured
  in a port-channel with one member when leveraging automatic channel-id generation. To configure multiple ports as member of the same port-channel,
  set the channel-id key (cf examples below).

## Variables and Options

### Connected Endpoints

```yaml
# Dictionary of connected endpoint | Optional
# This should be applied to group_vars or host_vars where endpoints are connecting.
# <connected_endpoints_keys.key> is one of the keys under "connected_endpoints_keys"
# Default keys are "servers", "firewalls", "routers", "load_balancers" and "storage_arrays".
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

        # The lists "endpoint_ports", "switch_ports" and "switches" must have the same length.
        # Each list item is one switchport.

        # Endpoint port(s). Used for description. | Required unless description is set
        endpoint_ports: [ < interface_name > ]

        # List of switch interfac(es) | Required
        switch_ports: [ < switchport_interface > ]

        # List of switch(es) | Required
        switches: [ < device > ]

        # Interface descriptions Description | Optional
        description: <description>

        # Port-profile name, to inherit configuration.
        profile: < port_profile_name >

        # Administrative state | Optional - default is true
        # setting to false will set port to 'shutdown' in intended configuration
        enabled: < true | false >

        # Interface mode | Optional
        mode: < access | dot1q-tunnel | trunk >

        # MTU | Optional
        mtu: < mtu >

        # L2 MTU - This should only be defined for platforms supporting the "l2 mtu" CLI
        l2_mtu: < l2_mtu >

        # Native VLAN for a trunk port | Optional
        # If setting both native_vlan and native_vlan_tag, native_vlan_tag takes precedence
        native_vlan: < native_vlan_number >
        native_vlan_tag: < boolean | default -> false >

        # Trunk Groups | Required with "enable_trunk_groups: true"
        # Trunk Groups are used for limiting vlans on trunk ports to vlans with the same Trunk Group
        trunk_groups: [ < trunk_group_1 >, < trunk_group_2 > ]

        # Interface vlans | Optional
        # If not set, the EOS default is that all vlans are allowed for trunk ports and vlan 1 will be used for access ports
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
          enable: < true | false | default -> false | Required >
          # These are the default settings:
          # - The global PTP profile parameters will be applied to all connected endpoints where ptp is manually enabled.
          # - `ptp role master` is set to ensure control over the PTP topology.
          endpoint_role: < follower | bmca | default -> follower >
          profile: < aes67 | smpte2059-2 | aes67-r16-2016 | default -> aes67-r16-2016 >

        # Configure the downstream interfaces of a respective Link Tracking Group | Optional
        # If port_channel is defined in an adapter then port-channel interface is configured to be the downstream
        # else all the ethernet-interfaces will be configured as downstream -> to configure single-active EVPN multihomed networks
        link_tracking:
          enabled: < true | false >
          # The default group name is taken from fabric variable of the switch, link_tracking.groups[0].name with default value being "LT_GROUP1".
          # Optional if default link_tracking settings are configured on the node.
          name: < tracking_group_name >

        # 802.1x | Optional
        dot1x:
          port_control: < "auto" | "force-authorized" | "force-unauthorized" >
          port_control_force_authorized_phone: < true | false >
          reauthentication: < true | false >
          pae:
            mode: < "authenticator" >
          authentication_failure:
            action: < "allow" | "drop" >
            allow_vlan: < 1-4094 >
          host_mode:
            mode: < "multi-host" | "single-host" >
            multi_host_authenticated: < true | false >
          mac_based_authentication:
            enabled: < true | false >
            always: < true | false >
            host_mode_common: < true | false >
          timeout:
            idle_host: < 10-65535 >
            quiet_period: < 1-65535 >
            reauth_period: < 60-4294967295 | server >
            reauth_timeout_ignore: < true | false >
            tx_period: < 1-65535 >
          reauthorization_request_limit: < 1-10 >

        # EOS CLI rendered directly on the ethernet interface in the final EOS configuration
        raw_eos_cli: |
          < multiline eos cli >

        # Custom structured config added under ethernet_interfaces.<interface> for eos_cli_config_gen
        structured_config: < dictionary >

        # Storm control settings applied on port toward the endpoint | Optional
        storm_control:
          all:
            level: < Configure maximum storm-control level >
            unit: < percent | pps > | Optional var and is hardware dependent - default is percent)
          broadcast:
            level: < Configure maximum storm-control level >
            unit: < percent | pps > | Optional var and is hardware dependent - default is percent)
          multicast:
            level: < Configure maximum storm-control level >
            unit: < percent | pps > | Optional var and is hardware dependent - default is percent)
          unknown_unicast:
            level: < Configure maximum storm-control level >
            unit: < percent | pps > | Optional var and is hardware dependent - default is percent)

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

        # Settings for all- or single-active EVPN multihoming
        ethernet_segment:

          # Define a manual short-esi (be careful using this on profiles) or auto-generate an ESI | Required
          # Please see the notes under "EVPN A/A ESI dual- and single-attached endpoint scenarios" before setting short_esi: auto
          short_esi: < xxxx:xxxx:xxxx | auto >

          # Configure this Ethernet Segment for all-active or single-active forwarding | Optional
          # If omitted, Port-Channels use the EOS default of all-active
          # If omitted, Ethernet interfaces are configured as single-active
          redundancy: < all-active | single-active >

          # Configure DF algorithm and preferences | Optional
          #  - auto: Use preference-based algorithm and assign preference based on position of device in the 'switches' list
          #          e.g. assuming a list of three switches, this would assign a preference of 200 to the first switch, 100 to the 2nd and 0 to the third
          #  - preference: Set preference for each switch manually using designated_forwarder_preferences key
          #  - modulus: Use the default modulus-based algorithm
          # If omitted, Port-Channels use the EOS default of modulus
          # If omitted, Ethernet interfaces default to the 'auto' mechanism detailed above
          designated_forwarder_algorithm: < "auto" | "modulus" | "preference" >
          # manual preference as described above | Required only for preference algorithm
          designated_forwarder_preferences: [ < df_preference_for_each_switch > ]
          # Disable preemption for single-active forwarding when auto/manual DF preference is configured | Optional
          dont_preempt: < true | false >

      # Example of port-channel adapter
      - endpoint_ports: [ < interface_name_1 > , < interface_name_2 > ]
        switch_ports: [ < switchport_interface_1 >, < switchport_interface_2 > ]
        switches: [ < device_1 >, < device_2 > ]
        profile: < port_profile_name >

        # Port- Channel
        port_channel:

          # Port-Channel Mode | Required
          mode: < "active" | "passive" | "on" >

          # Port-Channel ID | Optional
          # If no channel_id is specified, an id is generated from the first switch port in the port channel
          channel_id : < port_channel_id >

          # Port-Channel Description - added after endpoint name in the description | Optional
          description: < port_channel_description >

          # Port-Channel administrative state | Optional - default is true
          # setting to false will set port to 'shutdown' in intended configuration
          enabled: < true | false >

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
            short_esi: < xxxx:xxxx:xxxx | auto > Required for multihomed port-channels with subinterfaces
            vlan_id: < VLAN ID to bridge > | Optional - default is subinterface number
            # Flexible encapsulation parameters
            encapsulation_vlan:
              client_dot1q: < client vlan id encapsulation > | Optional - default is subinterface number

          # Allocates an automatic short_esi to all ports using this profile
          # Please see the notes under "EVPN A/A ESI dual-attached endpoint examples" in this document before setting short_esi: auto.
          short_esi: auto

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
          # Note that short_esi defined here is overridden by short_esi defined under the ethernet_segment section.
          # This key will be deprecated in the next major version of AVD.
          short_esi: < xxxx:xxxx:xxxx | auto >
        ethernet_segment:
          short_esi: < xxxx:xxxx:xxxx | auto >
```

### Network Ports

The `network_ports` data model is intended to be used with `port_profiles` and `parent_profiles` to keep the configuration generic and compact,
but all features and keys supported under `connected_endpoints.adapters` is also supported directly under `network_ports`.

Since all ranges defined under `network_ports` will be expanded to individual port configurations, by default each port will be configured
in a port-channel with one member when leveraging automatic channel-id generation. To configure multiple ports as member of the same port-channel,
set the channel-id key (cf examples below).
To leverage automatic channel-id computation and configure port-channel with multiple members, `connected_endpoints` should be used.

The expansiont to individual port configurations also lead to inconsistent configurations when used with `short_esi: auto` or
`designated_forwarder_algorithm: auto`, since those rely on information from multiple switches and interfaces.

```yaml
# Network Ports | Optional
# All switch_ports ranges are expanded into individual port configurations.
# Switches are matched with regular expressions, which must match the full hostname.
network_ports:
  - switches:
      - < regex matching the full hostname of one or more switches >
    # Switch_ports is a list of ranges using AVD range_expand syntax (see link below).
    # Ex Ethernet1-48 or Ethernet2-3/1-48
    switch_ports:
      - < interface | interface_range >
    description: < description to be used on all ports >

    # Port-profile name, to inherit configuration.
    profile: < port_profile_name >

    < any keys supported under connected_endpoints adapters >
```

For more details and examples of the `range_expand` syntax, see the [arista.avd.range_expand documentation](../../../plugins/README.md#range_expand-filter)

### Port Profiles

```yaml
# Optional profiles to share common settings for connected_endpoints and/or network_ports
# Keys are the same used under endpoints adapters. Keys defined under endpoints adapters take precedence.
port_profiles:
  < port_profile_name >:
    # Parent Profile | Optional
    # Port_profiles can refer to another port_profile to inherit settings in up to two levels (adapter->profile->parent_profile).
    parent_profile: < port_profile_name >

    < any keys supported under connected_endpoints adapters >
```

### Connected Endpoints Keys

```yaml
# Define connected endpoints keys, to define grouping of endpoints connecting to the fabric.
# This provides the ability to define various keys of your choice to better organize/group your data.
# This should be defined in top level group_var for the fabric.
# The default values will be overridden if defining this key, so it is recommended to copy the defaults and modify them.
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

## Examples

### Example with profiles

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

### Single attached endpoint example

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

### MLAG dual-attached endpoint example

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

### EVPN A/A ESI dual-attached endpoint examples

To help provide consistency when configuring EVPN A/A ESI values, arista.avd provides an abstraction in the form of a `short_esi` key.
`short_esi` is an abbreviated 3 octets value to encode [Ethernet Segment ID](https://tools.ietf.org/html/rfc7432#section-8.3.1) and LACP ID.
Transformation from abstraction to network values is managed by a [filter_plugin](../../../plugins/README.md) and provides following result:

- *EVPN ESI*: 000:000:0303:0202:0101
- *LACP ID*: 0303.0202.0101
- *Route Target*: 03:03:02:02:01:01

In addition, setting the `short_esi` key to `auto` generates the short_esi automatically using a hash of the following data elements:

- Port-Channel Interfaces: first two uplink switch hostnames, the ports on those switches, the corresponding endpoint ports and the channel-group ID.
- Port-Channel Subinterface: first two uplink switch hostname, the ports on those switches, the corresponding endpoint ports, the channel-group ID and the subinterface number.
- Ethernet Interfaces: first two uplink switch hostnames, the ports on those switches, the corresponding endpoint ports and the interface number.

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

### Example using network ports and profiles

```yaml
# Port Profiles
# Common settings inherited to network_ports
port_profiles:
  - profile: common
    mode: access
    vlans: "999"
    spanning_tree_portfast: edge
    spanning_tree_bpdufilter: enabled

  - profile: ap_with_port_channel
    parent_profile: common
    vlans: "101"
    port_channel:
      mode: active

  - profile: pc
    parent_profile: common
    vlans: "100"

# Network Ports
# All switch_ports ranges are expanded into individual port configurations
# Switches are matched with regex matching the full hostname.
network_ports:
  - switches:
      - network-ports-tests-1
    switch_ports:
      - Ethernet1-2
    profile: pc
    description: PCs

  - switches:
      - network-ports-tests-2$
    switch_ports:
      - Ethernet1-2
    profile: ap_with_port_channel
    description: AP1 with port_channel

  - switches:
      - network-ports-[est]{5}-.*
    switch_ports:
      - Ethernet3-4
      - Ethernet2/1-48
    profile: pc
    description: PCs
```

### Example using network ports to configure multiple ports in the same port-channel

```yaml
# Network Ports
# By setting the channel_id key under port-channel, interfaces Ethernet3-4 will
# be configured under the same port-channel.
network_ports:
  - switches:
      - network-ports-tests-1
    switch_ports:
      - Ethernet3-4
    description: Multiple interfaces in the same port-channel
    port_channel:
      mode: active
      channel_id: 42
```

This will generate the following config:

```shell
interface Port-Channel42
   description Multiple interfaces in the same port-channel
   no shutdown
   switchport
!
!
interface Ethernet3
   description Multiple interfaces in the same port-channel
   no shutdown
   channel-group 42 mode active
!
interface Ethernet4
   description Multiple interfaces in the same port-channel
   no shutdown
   channel-group 42 mode active
!
```
