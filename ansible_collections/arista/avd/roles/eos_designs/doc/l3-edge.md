# DCI & L3 Edge

The `l3_edge` data model can be used to configure extra L3 P2P links anywhere in the fabric. It can be between two switches that are already part of the fabric inventory, or it can be towards another device, where only one end of the link is on a switch in the fabric. Fabric switches can be types `l3leaf`, `spine` or `super-spine`.

The data model supports using IP pools, Subnet per link or specifying the IP addresses manually.
For BGP peerings the AS number must be specified. If the AS number is different than the AS number configured for the node, the local-as will be replaced on this BGP peering (`neighbor <ip> local-as <as> no-prepend replace-as`).

Make sure to configure the variables in a group_vars file covering all devices mentioned in the data model.

```yaml
l3_edge:
  p2p_links_ip_pools:
    < p2p_pool_name_1 >: < IPv4_address/Mask >
  p2p_links_profiles:
    < p2p_profile_name >:
      < any variable supported under p2p_links can be inherited from a profile >
  p2p_links:
      # Unique id per subnet_summary. Used to calculate ip addresses | Required with ip_pool
    - id: < integer - starting from 1 >

      # Speed | Optional
      speed: < speed | auto speed | forced speed >

      # IP Pool defined under p2p_links_ip_pools. A /31 will be taken from the pool per P2P link | Optional (Requires ip_pool or subnet or ip)
      ip_pool: < p2p_pool_name >

      # Subnet used on this P2P link | Optional (Requires ip_pool or subnet or ip)
      subnet: < IPv4_address/Mask >

      # Specific IP addresses used on this P2P link | Optional (Requires ip_pool or subnet or ip)
      ip: [ < node_a IPv4_address/Mask >, < node_b IPv4_address/Mask > ]

      # Nodes where this link should be configured | Required
      nodes: [ < node_a >, < node_b > ]

      # Interfaces where this link should be configured | Required
      interfaces: [ < node_a_interface >, < node_b_interface > ]

      # AS Numbers for BGP | Required with bgp peering
      as: [ < node_a_as >, < node_b_as > ]

      # Add this interface to underlay routing protocol | Optional
      include_in_underlay_protocol: < true | false | default -> false >

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
```
