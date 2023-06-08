AVD supports two different data models for defining connectivity to endpoints:

- ["Connected Endpoints"](#1---connected-endpoints) is an endpoint-centric model intended for servers or other use cases where most ports have unique configurations.
- ["Network Ports"](#2---network-ports) is a compact and port-centric model intended for configuration of generic port configurations on large ranges of ports.

Both data models share the same underlying implementation and can coexist without conflicts.
If a switch port is defined in both "Connected Endpoints" and "Network Ports", the "Connected Endpoints" configuration will take precedence.

Both data models support variable inheritance from profiles defined under [`port_profiles`](#3---port-profiles). The profiles can be shared between the models. Any setting defined under the `port_profiles` will be inherited from `parent_profile` to `profile` to `adapter`.
