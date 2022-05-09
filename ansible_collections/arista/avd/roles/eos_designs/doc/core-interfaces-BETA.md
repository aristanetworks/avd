# BETA Feature

The Core Interfaces feature is in BETA until the release of AVD 4.0.0. Changes to data models and default behavior for the Core Interfaces should be expected.

# Core Interfaces

The `core_interfaces` data model can be used to configure L3 P2P links anywhere in the fabric. It can be between two switches that are already part of the fabric inventory, or it can be towards another device, where only one end of the link is on a switch in the fabric.

The data model supports using IP pools, Subnet per link or specifying the IP addresses manually.
For BGP peerings the AS number must be specified. If the AS number is different than the AS number configured for the node, the local-as will be replaced on this BGP peering (`neighbor <ip> local-as <as> no-prepend replace-as`).

Make sure to configure the variables in a group_vars file covering all devices mentioned in the data model.

```yaml
core_interfaces:
  p2p_links_ip_pools:
    - name: < p2p_pool_name_1 >
      ipv4_pool: < IPv4_address/Mask >
  p2p_links_profiles:
    - name: < p2p_profile_name >
      < any variable supported under p2p_links can be inherited from a profile >
  p2p_links:
      # Unique id per subnet_summary. Used to calculate ip addresses | Required with ip_pool
    - id: < integer - starting from 1 >

      # Speed | Optional
      speed: < speed | auto speed | forced speed >

      # IP Pool defined under p2p_links_ip_pools. A /31 will be taken from the pool per P2P link | Optional
      ip_pool: < p2p_pool_name >

      # Subnet used on this P2P link | Optional
      subnet: < IPv4_address/Mask >

      # Specific IP addresses used on this P2P link | Optional
      ip: [ < node_a IPv4_address/Mask >, < node_b IPv4_address/Mask > ]

      # Allows turning on ipv6 for the link or profile (also autodetected based on underlay_rfc5549 and include_in_underlay_protocol) | Optional
      ipv6_enable: < true | false | default -> false >

      # Nodes where this link should be configured | Required
      nodes: [ < node_a >, < node_b > ]

      # Interfaces where this link should be configured | Required unless using port-channels
      interfaces: [ < node_a_interface >, < node_b_interface > ]

      # AS Numbers for BGP | Required with bgp peering
      as: [ < node_a_as >, < node_b_as > ]

      # Add this interface to underlay routing protocol | Optional
      include_in_underlay_protocol: < true | false | default -> true >

      # IS-IS parameters
      isis_hello_padding: false
      isis_metric: 60
      isis_circuit_type: level-2
      isis_authentication_mode: md5
      isis_authentication_key: $1c$sTNAlR6rKSw=

      # MPLS Parameters
      mpls_ip: < true | false | default -> true if switch.mpls_lsr is true >
      mpls_ldp: < true | false | default -> true for ldp underlay variants, otherwise false >

      # MTU for this P2P link | Optional
      mtu: < number | default -> same as p2p_uplinks_mtu >

      # Enable BFD (only considered for BGP) | Optional
      bfd: < true | false | default -> false >

      # Enable PTP | Optional
      ptp_enable: < true | false | default -> false >

      # QOS Service Profile | Optional
      qos_profile: < qos_profile_name >

      # MAC Security Profile | Optional
      macsec_profile: < macsec_profile_name >

      # Profile defined under p2p_profiles | Optional
      profile: < p2p_profile_name >

      # Port-channel parameters
      port_channel:
        mode: active
        nodes_child_interfaces:
          < node1 >: [ '< node1 interface1 >', '< node1 interface2 >' ]
          < node2 >: [ '< node2 interface1 >', '< node2 interface2 >' ]
```

# Fabric Level Variables

These fabric level parameters can be used with core_interfaces running ISIS, and may be overridden on link profile or link level:

```yaml
isis_default_circuit_type: < level-1-2, | level-1 | level-2 | default -> level-2 >
isis_default_metric: < metric | default -> 50 >
````
