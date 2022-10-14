---
search:
  boost: 2
---

# Input Variables

## P2P Uplinks MTU

Point to Point Links MTU

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>p2p_uplinks_mtu</samp>](## "p2p_uplinks_mtu") | Integer |  | 9000 | Min: 0<br>Max: 9216 |  |

=== "YAML"

    ```yaml
    p2p_uplinks_mtu: <int>
    ```

## P2P Uplinks QOS Profile

QOS Profile assigned on all infrastructure links

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>p2p_uplinks_qos_profile</samp>](## "p2p_uplinks_qos_profile") | String |  |  |  |  |

=== "YAML"

    ```yaml
    p2p_uplinks_qos_profile: <str>
    ```

## Underlay Filter Peer As

Configure route-map on eBGP sessions towards underlay peers, where prefixes with the peer's ASN in the AS Path are filtered away.
This is very useful in very large scale networks not using EVPN overlays, where convergence will be quicker by not having to return
all updates received from Spine-1 to Spine-2 just for Spine-2 to throw them away because of AS Path loop detection.
Note this key is ignored when EVPN is configured.

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>underlay_filter_peer_as</samp>](## "underlay_filter_peer_as") | Boolean |  | False |  |  |

=== "YAML"

    ```yaml
    underlay_filter_peer_as: <bool>
    ```

## Underlay IPv6

This feature allows IPv6 underlay routing protocol with RFC5549 addresses to be used along with IPv4 advertisements as VXLAN tunnel endpoints.
Requires "underlay_rfc5549: true" and "loopback_ipv6_pool" under the "Fabric Topology"

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>underlay_ipv6</samp>](## "underlay_ipv6") | Boolean |  | False |  |  |

=== "YAML"

    ```yaml
    underlay_ipv6: <bool>
    ```

## Underlay ISIS Instance Name

Additional underlay ISIS parameters

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>underlay_isis_instance_name</samp>](## "underlay_isis_instance_name") | String |  | EVPN_UNDERLAY |  |  |

=== "YAML"

    ```yaml
    underlay_isis_instance_name: <str>
    ```

## Underlay Multicast

Enable Multicast in the underlay on all p2p uplink interfaces and mlag l3 peer interface.
Specifically PIM Sparse-Mode will be configured on all routed underlay interfaces.
No other configuration is added, so the underlay will only support Source-Specific Multicast (SSM)
The configuration is intended to be used as multicast underlay for EVPN OISM overlay

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>underlay_multicast</samp>](## "underlay_multicast") | Boolean |  | False |  |  |

=== "YAML"

    ```yaml
    underlay_multicast: <bool>
    ```

## Underlay OSPF Area

Underlay OSFP Required when < underlay_routing_protocol > == OSPF variants

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>underlay_ospf_area</samp>](## "underlay_ospf_area") | String |  | 0.0.0.0 | Format: ipv4 |  |

=== "YAML"

    ```yaml
    underlay_ospf_area: <str>
    ```

## Underlay OSPF BFD Enable

Underlay OSFP Required when < underlay_routing_protocol > == OSPF variants

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>underlay_ospf_bfd_enable</samp>](## "underlay_ospf_bfd_enable") | Boolean |  | False |  |  |

=== "YAML"

    ```yaml
    underlay_ospf_bfd_enable: <bool>
    ```

## Underlay OSPF Max LSA

Underlay OSFP Required when < underlay_routing_protocol > == OSPF variants

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>underlay_ospf_max_lsa</samp>](## "underlay_ospf_max_lsa") | Integer |  | 12000 |  |  |

=== "YAML"

    ```yaml
    underlay_ospf_max_lsa: <int>
    ```

## Underlay OSPF Process ID

Underlay OSFP Required when < underlay_routing_protocol > == OSPF variants

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>underlay_ospf_process_id</samp>](## "underlay_ospf_process_id") | Integer |  | 100 |  |  |

=== "YAML"

    ```yaml
    underlay_ospf_process_id: <int>
    ```

## Underlay Rfc5549

Point to Point Underlay with RFC 5549(eBGP), i.e. IPv6 Unnumbered
Requires "underlay_routing_protocol: ebgp"

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>underlay_rfc5549</samp>](## "underlay_rfc5549") | Boolean |  | False |  |  |

=== "YAML"

    ```yaml
    underlay_rfc5549: <bool>
    ```

## Underlay Routing Protocol

- The following underlay routing protocols are supported:
  - EBGP (default for l3ls-evpn)
  - OSPF.
  - ISIS.
  - ISIS-SR*.
  - ISIS-LDP*.
  - ISIS-SR-LDP*.
  - OSPF-LDP*.
- The variables should be applied to all devices in the fabric.

*Only supported with core_interfaces data model.

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>underlay_routing_protocol</samp>](## "underlay_routing_protocol") | String |  | ebgp | Valid Values:<br>- ebgp<br>- ospf<br>- isis<br>- isis-sr<br>- isis-ldp<br>- isis-sr-ldp<br>- ospf-ldp<br>- BGP |  |

=== "YAML"

    ```yaml
    underlay_routing_protocol: <str>
    ```

## Uplink PTP

Enable PTP on all infrastructure links

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>uplink_ptp</samp>](## "uplink_ptp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;enable</samp>](## "uplink_ptp.enable") | Boolean |  | False |  |  |

=== "YAML"

    ```yaml
    uplink_ptp:
      enable: <bool>
    ```
