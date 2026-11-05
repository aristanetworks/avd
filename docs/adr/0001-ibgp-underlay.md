<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# ADR 0001 - iBGP underlay with derived route reflection

- Status: Accepted
- Date: 2026-11-02

## Context

AI fabrics ask for a single-AS iBGP underlay over RFC 5549 ([#7272](https://github.com/aristanetworks/avd/issues/7272), [#7264](https://github.com/aristanetworks/avd/issues/7264)).
The uplinks already describe the hierarchy, so the route reflection can be derived instead of modeled. Implemented in [#7661](https://github.com/aristanetworks/avd/pull/7661).

## Decisions

1. **Narrow scope.** `underlay_routing_protocol: ibgp` only supports RFC 5549 with no overlay. Everything else raises an error instead of being ignored, so relaxing a guard is a deliberate change with tests.
2. **Derived route reflection.** A node with downlink switches is a route reflector (RR) for them. Every session uses `next-hop-self`. There is no RR role input.
3. **One cluster ID per RR group.** The RRs serving the same clients form a group. `bgp_cluster_id` is mandatory on every RR, the same in a group and unique across groups.
    - A distinct ID per RR, like the router ID default, creates hairpin ECMP paths through the upper tier.
    - The same ID in two groups drops routes between them, through cluster list loop detection.
    - A shared ID is only safe with a full mesh between adjacent tiers, so partial meshes and tier skips are rejected.
4. **Two peer groups, one set of session settings.** Uplinks use `ipv4_underlay_peers`. Downlinks use `rr_clients_underlay_peers`, which only has `name` and `structured_config` and inherits the password, `bfd` and `maximum_routes`.
    - RFC 5549 `neighbor interface` only takes a peer group, so `route-reflector-client` must live on a peer group, and a spine needs one per direction.
    - Both ends of a session read the same inputs, so they can't mismatch. A use case for different values can add keys later.
    - EOS encrypts a type 7 BGP password with the peer group name, so AVD decrypts it with the `ipv4_underlay_peers` name and encrypts it again with the `rr_clients_underlay_peers` name. Passwords never go into facts.
5. **Topology checks in facts, per device.** Clients check that their RRs share one cluster ID. RRs check that all their clients have the same RRs, and use a shared cluster ID registry, filled during `cross_pollinate()` like `mlag_groups`, for uniqueness.
    - Per device, so the checks fit a future facts stage processed in parallel per device. The registry is the only cross-device state.
    - The registry covers all the devices of the run, so two unconnected fabrics built together can't reuse a cluster ID.
    - Facts only check what needs several devices. Neighbors that aren't iBGP routers with p2p uplinks are skipped there, and rejected in structured config with a more specific error.

## Guards

The guards and their reasons are maintained in the [Restrictions](../howto/ibgp_underlay/README.md#restrictions) of the how-to guide.
"Not supported yet" means there is no known technical blocker, so relaxing the guard mostly needs tests. The other reasons need a design change first.
