---
search:
  boost: 2
---

# Input Variables

## EVPN Ebgp Gateway Multihop

Default of 15, considering a large value to avoid BGP reachability issues in very complex DCI networks.
Adapt the value for your specific topology.

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>evpn_ebgp_gateway_multihop</samp>](## "evpn_ebgp_gateway_multihop") | Integer |  | 15 |  |  |

=== "YAML"

    ```yaml
    evpn_ebgp_gateway_multihop: <int>
    ```

## EVPN Ebgp Multihop

Default of 3, the recommended value for a 3 stage spine and leaf topology.
Set to a higher value to allow for very large and complex topologies.

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>evpn_ebgp_multihop</samp>](## "evpn_ebgp_multihop") | Integer |  | 3 |  |  |

=== "YAML"

    ```yaml
    evpn_ebgp_multihop: <int>
    ```

## EVPN Hostflap Detection

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>evpn_hostflap_detection</samp>](## "evpn_hostflap_detection") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;enabled</samp>](## "evpn_hostflap_detection.enabled") | Boolean |  | True |  | If set to false it will disable EVPN host-flap detection |
    | [<samp>&nbsp;&nbsp;threshold</samp>](## "evpn_hostflap_detection.threshold") | Integer |  | 5 |  | Minimum number of MAC moves that indicate a MAC duplication issue |
    | [<samp>&nbsp;&nbsp;window</samp>](## "evpn_hostflap_detection.window") | Integer |  | 180 |  | Time (in seconds) to detect a MAC duplication issue |
    | [<samp>&nbsp;&nbsp;expiry_timeout</samp>](## "evpn_hostflap_detection.expiry_timeout") | Integer |  |  |  | Time (in seconds) to purge a MAC duplication issue |

=== "YAML"

    ```yaml
    evpn_hostflap_detection:
      enabled: <bool>
      threshold: <int>
      window: <int>
      expiry_timeout: <int>
    ```

## EVPN Import Pruning

Enable VPN import pruning (Min. EOS 4.24.2F)
The Route Target extended communities carried by incoming VPN paths will
be examined. If none of those Route Targets have been configured for import,
the path will be immediately discarded

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>evpn_import_pruning</samp>](## "evpn_import_pruning") | Boolean |  | False |  |  |

=== "YAML"

    ```yaml
    evpn_import_pruning: <bool>
    ```

## EVPN Multicast

General Configuration required for EVPN Multicast. "evpn_l2_multicast" must also be configured under the Network Services (tenants).
Requires "underlay_multicast: true" and IGMP snooping enabled globally (default).
For MLAG devices Route Distinguisher must be unique since this feature will create multi-vtep configuration.
Warning !!! For Trident3 based platforms i.e 7050X3, 7300X3, 720XP and 722XP
  The Following default platform setting will be configured: "platform trident forwarding-table partition flexible exact-match 16384 l2-shared 98304 l3-shared 131072"
  All forwarding agents will be restarted when this configuration is applied.
  You can tune the settings by overridding the default variable: "platform_settings[platforms].trident_forwarding_table_partition:"
  Please contact an Arista representative for help with determining the appropriate values for your environment.

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>evpn_multicast</samp>](## "evpn_multicast") | Boolean |  | False |  |  |

=== "YAML"

    ```yaml
    evpn_multicast: <bool>
    ```

## EVPN Overlay BGP Rtc

Enable Route Target Membership Constraint Address Family on EVPN overlay BGP peerings (Min. EOS 4.25.1F)
Requires use eBGP as overlay protocol.

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>evpn_overlay_bgp_rtc</samp>](## "evpn_overlay_bgp_rtc") | Boolean |  | False |  |  |

=== "YAML"

    ```yaml
    evpn_overlay_bgp_rtc: <bool>
    ```

## EVPN Prevent Readvertise To Server

Configure route-map on eBGP sessions towards route-servers, where prefixes with the peer's ASN in the AS Path are filtered away.
This is very useful in very large scale networks, where convergence will be quicker by not having to return all updates received
from Route-server-1 to Router-server-2 just for Route-server-2 to throw them away because of AS Path loop detection.

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>evpn_prevent_readvertise_to_server</samp>](## "evpn_prevent_readvertise_to_server") | Boolean |  | False |  |  |

=== "YAML"

    ```yaml
    evpn_prevent_readvertise_to_server: <bool>
    ```

## EVPN Short Esi Prefix

Configure prefix for "short_esi" values

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>evpn_short_esi_prefix</samp>](## "evpn_short_esi_prefix") | String |  | 0000:0000: |  |  |

=== "YAML"

    ```yaml
    evpn_short_esi_prefix: <str>
    ```

## EVPN VLAN Aware Bundles

Enable vlan aware bundles for EVPN MAC-VRF
Old variable name vxlan_vlan_aware_bundles, supported for backward-compatibility.

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>evpn_vlan_aware_bundles</samp>](## "evpn_vlan_aware_bundles") | Boolean |  | False |  |  |

=== "YAML"

    ```yaml
    evpn_vlan_aware_bundles: <bool>
    ```
