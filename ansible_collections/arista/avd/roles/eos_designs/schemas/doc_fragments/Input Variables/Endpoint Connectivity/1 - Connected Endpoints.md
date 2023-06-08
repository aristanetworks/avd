- The connected endpoints variables define connectivity from the perspective of the endpoints that connect to the fabric.
- Each endpoint can have one or more `adapters` defined, under which the connected `switches`, `switch_ports` and `endpoint_ports`
  must be set.
- If port_channel mode is enabled under one "adapter", all switch_ports connected to that "adapter" will become part of this port-channel.
- The keys used to define `connected_endpoints` are configurable using [`connected_endpoints_keys`](#4---connected-endpoints-keys).
  The default keys are: `servers`, `firewalls`, `routers`, `load_balancers` and `storage_arrays`.

#### Example with profiles

```yaml
port_profiles:

  - profile: VM_Servers
    mode: trunk
    vlans: "110-111,120-121,130-131"
    spanning_tree_portfast: edge

  - profile: MGMT
    mode: access
    vlans: "110"

  - profile: DB_Clusters
    mode: trunk
    vlans: "140-141"

servers:
  - name: server01
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

  - name: server03
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
  - name: FIREWALL01
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
  - name: ROUTER01
    rack: RackB
    adapters:
      - endpoint_ports: [ Eth0, Eth1 ]
        switch_ports: [ Ethernet21, Ethernet21 ]
        switches: [ DC1-LEAF2A, DC1-LEAF2B ]
        profile: TENANT_A
```

#### Example with single attached endpoint

Single attached interface from `E0` toward `DC1-LEAF1A` interface `Eth5`

```yaml
servers:
  - name: server01
    rack: RackB
    adapters:
      - endpoint_ports: [ E0 ]
        switch_ports: [ Ethernet5 ]
        switches: [ DC1-LEAF1A ]
        profile: MGMT
```

#### Example with MLAG dual-attached endpoint

MLAG dual-homed connection:

- From `E0` to `DC1-SVC3A` interface `Eth10`
- From `E1` to `DC1-SVC3B` interface `Eth10`

```yaml
servers:
  - name: server01
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

#### Example with EVPN A/A ESI dual-attached endpoint

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
  - name: server01
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
