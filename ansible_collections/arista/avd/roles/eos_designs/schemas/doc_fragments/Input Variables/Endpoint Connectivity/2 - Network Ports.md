The `network_ports` data model is intended to be used with `port_profiles` and `parent_profiles` to keep the configuration generic and compact,
but all features and keys supported under `connected_endpoints.adapters` are also supported directly under `network_ports`.

All ranges defined under `switch_ports` will be expanded to individual port configuration which leads to a some behavioral differences to `connected_endpoints`:

- By default each port will be configured in a port-channel with one member when leveraging automatic channel-id generation.
  To configure multiple ports as member of the same port-channel set the channel-id key (see the example below).
- Inconsistent configurations when used with `short_esi: auto` or `designated_forwarder_algorithm: auto`, since those rely on information from multiple switches and interfaces.

#### Example using network ports and profiles

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

#### Example using network ports to configure multiple ports in the same port-channel

When defining port-channels, all ranges defined under `switch_ports` will be expanded to individual port configurations
in a port-channel with one member. To configure multiple ports as members of the same port-channel, set the channel-id key manually
like in this example:

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

To leverage automatic channel-id computation and configure port-channel with multiple members, `connected_endpoints` should be used.
