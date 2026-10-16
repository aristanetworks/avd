---
# This title is used for search results
title: AVD Design data models for endpoint connectivity
---
<!--
  ~ Copyright (c) 2023-2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# Endpoint connectivity

Model how servers and other endpoints attach to the fabric using connected endpoints, network ports, shared port profiles, and related access control features such as 802.1X and address locking.

## Endpoint connectivity

AVD supports two different data models for defining connectivity to endpoints:

- ["Connected Endpoints"](#connected-endpoints-settings) is an endpoint-centric model intended for servers or other use cases where most ports have unique configurations.
- ["Network Ports"](#network-ports-settings) is a compact and port-centric model intended for configuration of generic port configurations on large ranges of ports.

Both data models share the same underlying implementation and can coexist without conflicts.
If a switch port is defined in both "Connected Endpoints" and "Network Ports", the "Connected Endpoints" configuration will take precedence.

Both data models support variable inheritance from profiles defined under [`port_profiles`](#port-profiles-settings). The profiles can be shared between the models. Any setting defined under the `port_profiles` will be inherited from `parent_profile` to `profile` to `adapter`.

### Connected endpoints settings

- The connected endpoints variables define connectivity from the perspective of the endpoints that connect to the fabric.
- Each endpoint can have one or more `adapters` defined, under which the connected `switches`, `switch_ports` and `endpoint_ports`
  must be set.
- If port_channel mode is enabled under one "adapter", all switch_ports connected to that "adapter" will become part of this port-channel.
- The keys used to define connected endpoints are configurable using [`connected_endpoints_keys`](#connected-endpoints-keys-settings).
  The default available keys are:
  - `servers`
  - `firewalls`
  - `routers`
  - `load_balancers`
  - `storage_arrays`
  - `cpes`
  - `workstations`
  - `access_points`
  - `phones`
  - `printers`
  - `cameras`
  - `generic_devices`

??? example "Example with profiles"

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
              endpoint_port_channel: Bond0
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

??? example "Example with single attached endpoint"

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

??? example "Example with MLAG dual-attached endpoint"

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
              endpoint_port_channel: Bond0
              mode: active
    ```

??? example "Example with EVPN A/A ESI dual-attached endpoint"

    To help provide consistency when configuring EVPN A/A ESI values, arista.avd provides an abstraction in the form of a `short_esi` key.
    `short_esi` is an abbreviated 3 octets value to encode [Ethernet Segment ID](https://tools.ietf.org/html/rfc7432#section-8.3.1) and LACP ID.

    The abstracted `short_esi: "0303:0202:0101"` is transformed into the following network values:

    - *EVPN ESI*: 0000:0000:0303:0202:0101
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
              endpoint_port_channel: Bond0
              mode: active
            ethernet_segment:
              short_esi: 0303:0202:0101
    ```

--8<--
schemas/avd_design/docs/tables/connected-endpoints.md
--8<--

### Connected endpoints default description or description template settings

Connected endpoints support the customization of generated descriptions with a static value or template.

--8<--
schemas/avd_design/docs/tables/default-connected-endpoints-description.md
--8<--

### Network ports settings

The `network_ports` data model is intended to be used with `port_profiles` and `parent_profiles` to keep the configuration generic and compact,
but all features and keys supported under `connected_endpoints.adapters` are also supported directly under `network_ports`.

To filter what switches to configure, match on a switch full hostname or platform type using regex patterns. When both criteria are used together, the switch must match both in order to generate the assigned port configuration.

All ranges defined under `switch_ports` will be expanded to individual port configuration which leads to a some behavioral differences to `connected_endpoints`:

- By default each port will be configured in a port-channel with one member when leveraging automatic channel-id generation.
  To configure multiple ports as member of the same port-channel set the channel-id key (see the example below).
- Inconsistent configurations when used with `short_esi: auto` or `designated_forwarder_algorithm: auto`, since those rely on information from multiple switches and interfaces.

??? example "Example using match criteria"

    ```yaml
    # Port Profiles
    # Common settings inherited to network_ports
    port_profiles:
      - profile: common
        mode: access
        vlans: "999"
        spanning_tree_portfast: edge
        spanning_tree_bpdufilter: enabled

    # Network Ports
    # Switches are matched with regex matching the full hostname and platform type.
    network_ports:
      - switches:
          - network-ports-[est]{5}-.*
        platforms:
          - 720XPM-48Y6
        switch_ports:
          - Ethernet1-48
        profile: common

    # Switches are matched on platform type, regardless of hostname.
      - platforms:
          - 720XPM-24Y6
        switch_ports:
          - Ethernet1-24
        profile: common

    # Custom Platform Settings
    # Copied default 720XP platform settings, adding more specific platform names for match.
    # These platform types can be assigned to devices as part of nodes/node_group settings.
    custom_platform_settings:
      - platforms:
          - 720XPM-48Y6
          - 720XPM-24Y6
        feature_support:
          poe: true
          queue_monitor_length_notify: false
        reload_delay:
          mlag: 300
          non_mlag: 330
        trident_forwarding_table_partition: flexible exact-match 16000 l2-shared 18000 l3-shared
          22000

    ```

??? example "Example using network ports and profiles"

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
        endpoint: PCs

      - switches:
          - network-ports-tests-2$
        switch_ports:
          - Ethernet1-2
        profile: ap_with_port_channel
        endpoint: AP1 with port_channel

      - switches:
          - network-ports-[est]{5}-.*
        switch_ports:
          - Ethernet3-4
          - Ethernet2/1-48
        profile: pc
        endpoint: PCs
    ```

??? example "Example using network ports to configure multiple ports in the same port-channel"

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

    !!! tip
        To leverage automatic channel-id computation and configure port-channel with multiple members, `connected_endpoints` should be used.

--8<--
schemas/avd_design/docs/tables/network-ports.md
--8<--

### Network ports default description or description template settings

Network ports support the customization of generated descriptions with a static value or template.

--8<--
schemas/avd_design/docs/tables/default-network-ports-description.md
--8<--

### Port profiles settings

Optional profiles to share common settings for connected_endpoints and/or network_ports.
Keys are the same as used under endpoint adapters. Keys defined under endpoints adapters take precedence.

A port profile can refer to another port profile using `parent_profile` to inherit settings in up to two levels (adapter->profile->parent_profile).

--8<--
schemas/avd_design/docs/tables/port-profiles.md
--8<--

### Connected endpoints keys settings

The keys used to define Connected Endpoints are configurable using `connected_endpoints_keys`.

Endpoints connecting to the fabric can be grouped by using separate keys.
The keys can be customized to provide a better better organization or grouping of your data.

`connected_endpoints_keys` should be defined in the top level group_vars for the fabric.

!!! note
    The default values will be overridden if defining this key, so it is recommended to copy the defaults and modify them.

--8<--
schemas/avd_design/docs/tables/connected-endpoints-keys.md
--8<--

## 802.1X Settings

--8<--
schemas/avd_design/docs/tables/dot1x-settings.md
--8<--

## Address locking settings

--8<--
schemas/avd_design/docs/tables/address-locking-settings.md
--8<--
