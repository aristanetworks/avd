---
search:
  boost: 2
---

# Input Variables

## BFD Multihop

BFD Multihop tuning

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>bfd_multihop</samp>](## "bfd_multihop") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;interval</samp>](## "bfd_multihop.interval") | Integer |  | 300 |  |  |
    | [<samp>&nbsp;&nbsp;min_rx</samp>](## "bfd_multihop.min_rx") | Integer |  | 300 |  |  |
    | [<samp>&nbsp;&nbsp;multiplier</samp>](## "bfd_multihop.multiplier") | Integer |  | 3 |  |  |

=== "YAML"

    ```yaml
    bfd_multihop:
      interval: <int>
      min_rx: <int>
      multiplier: <int>
    ```

## BGP As

AS number to use to configure overlay when "overlay_routing_protocol" == IBGP

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>bgp_as</samp>](## "bgp_as") | String |  |  |  |  |

=== "YAML"

    ```yaml
    bgp_as: <str>
    ```

## BGP Ecmp

Maximum ECMP for BGP multi-path

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>bgp_ecmp</samp>](## "bgp_ecmp") | Integer |  | 4 |  |  |

=== "YAML"

    ```yaml
    bgp_ecmp: <int>
    ```

## BGP Maximum Paths

Maximum Paths for BGP multi-path

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>bgp_maximum_paths</samp>](## "bgp_maximum_paths") | Integer |  | 4 |  |  |

=== "YAML"

    ```yaml
    bgp_maximum_paths: <int>
    ```

## BGP Mesh Pes

Whether to configure an iBGP full mesh between PEs, either because there is no RR used or other reasons.

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>bgp_mesh_pes</samp>](## "bgp_mesh_pes") | Boolean |  | False |  |  |

=== "YAML"

    ```yaml
    bgp_mesh_pes: <bool>
    ```

## BGP Peer Groups

Leverage an Arista EOS switch to generate the encrypted password using the correct peer group name.
Note that the name of the peer groups use '-' instead of '_' in EOS configuration.

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>bgp_peer_groups</samp>](## "bgp_peer_groups") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;ipv4_underlay_peers</samp>](## "bgp_peer_groups.ipv4_underlay_peers") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "bgp_peer_groups.ipv4_underlay_peers.name") | String |  | IPv4-UNDERLAY-PEERS |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;password</samp>](## "bgp_peer_groups.ipv4_underlay_peers.password") | String |  |  |  | Encrypted Password |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "bgp_peer_groups.ipv4_underlay_peers.structured_config") | Dictionary |  |  |  | Custom structured config added under router_bgp.peer_groups.<name> for eos_cli_config_gen |
    | [<samp>&nbsp;&nbsp;mlag_ipv4_underlay_peer</samp>](## "bgp_peer_groups.mlag_ipv4_underlay_peer") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "bgp_peer_groups.mlag_ipv4_underlay_peer.name") | String |  | MLAG-IPv4-UNDERLAY-PEER |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;password</samp>](## "bgp_peer_groups.mlag_ipv4_underlay_peer.password") | String |  |  |  | Encrypted Password |
    | [<samp>&nbsp;&nbsp;evpn_overlay_peers</samp>](## "bgp_peer_groups.evpn_overlay_peers") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "bgp_peer_groups.evpn_overlay_peers.name") | String |  | EVPN-OVERLAY-PEERS |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;password</samp>](## "bgp_peer_groups.evpn_overlay_peers.password") | String |  |  |  | Encrypted Password |
    | [<samp>&nbsp;&nbsp;evpn_overlay_core</samp>](## "bgp_peer_groups.evpn_overlay_core") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "bgp_peer_groups.evpn_overlay_core.name") | String |  | EVPN-OVERLAY-CORE |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;password</samp>](## "bgp_peer_groups.evpn_overlay_core.password") | String |  |  |  | Encrypted Password |
    | [<samp>&nbsp;&nbsp;IPv4_UNDERLAY_PEERS</samp>](## "bgp_peer_groups.IPv4_UNDERLAY_PEERS") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "bgp_peer_groups.IPv4_UNDERLAY_PEERS.name") | String |  | IPv4-UNDERLAY-PEERS |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;password</samp>](## "bgp_peer_groups.IPv4_UNDERLAY_PEERS.password") | String |  |  |  | Encrypted Password |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "bgp_peer_groups.IPv4_UNDERLAY_PEERS.structured_config") | Dictionary |  |  |  | Custom structured config added under router_bgp.peer_groups.<name> for eos_cli_config_gen |
    | [<samp>&nbsp;&nbsp;MLAG_IPv4_UNDERLAY_PEER</samp>](## "bgp_peer_groups.MLAG_IPv4_UNDERLAY_PEER") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "bgp_peer_groups.MLAG_IPv4_UNDERLAY_PEER.name") | String |  | MLAG-IPv4-UNDERLAY-PEER |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;password</samp>](## "bgp_peer_groups.MLAG_IPv4_UNDERLAY_PEER.password") | String |  |  |  | Encrypted Password |
    | [<samp>&nbsp;&nbsp;EVPN_OVERLAY_PEERS</samp>](## "bgp_peer_groups.EVPN_OVERLAY_PEERS") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "bgp_peer_groups.EVPN_OVERLAY_PEERS.name") | String |  | EVPN-OVERLAY-PEERS |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;password</samp>](## "bgp_peer_groups.EVPN_OVERLAY_PEERS.password") | String |  |  |  | Encrypted Password |

=== "YAML"

    ```yaml
    bgp_peer_groups:
      ipv4_underlay_peers:
        name: <str>
        password: <str>
        structured_config:
      mlag_ipv4_underlay_peer:
        name: <str>
        password: <str>
      evpn_overlay_peers:
        name: <str>
        password: <str>
      evpn_overlay_core:
        name: <str>
        password: <str>
      IPv4_UNDERLAY_PEERS:
        name: <str>
        password: <str>
        structured_config:
      MLAG_IPv4_UNDERLAY_PEER:
        name: <str>
        password: <str>
      EVPN_OVERLAY_PEERS:
        name: <str>
        password: <str>
    ```
