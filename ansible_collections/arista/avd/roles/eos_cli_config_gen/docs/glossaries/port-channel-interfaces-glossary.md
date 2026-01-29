# Glossary

## Table of Contents

- [A](#a)
- [D](#d)
- [E](#e)
- [H](#h)
- [I](#i)
- [K](#k)
- [L](#l)
- [M](#m)
- [N](#n)
- [O](#o)
- [P](#p)
- [Q](#q)
- [R](#r)
- [S](#s)
- [T](#t)
- [U](#u)
- [V](#v)

## A

### algorithm

**Type**: String  
**Path**: `port_channel_interfaces.[].isis_authentication.both.key_ids.[].algorithm`  
**Valid Values**: `sha-1`, `sha-224`, `sha-256`, `sha-384`, `sha-512`  
---

### algorithm

**Type**: String  
**Path**: `port_channel_interfaces.[].isis_authentication.both.shared_secret.algorithm`  
**Valid Values**: `md5`, `sha-1`, `sha-224`, `sha-256`, `sha-384`, `sha-512`  
---

### algorithm

**Type**: String  
**Path**: `port_channel_interfaces.[].isis_authentication.level_1.key_ids.[].algorithm`  
**Valid Values**: `sha-1`, `sha-224`, `sha-256`, `sha-384`, `sha-512`  
---

### algorithm

**Type**: String  
**Path**: `port_channel_interfaces.[].isis_authentication.level_1.shared_secret.algorithm`  
**Valid Values**: `md5`, `sha-1`, `sha-224`, `sha-256`, `sha-384`, `sha-512`  
---

### algorithm

**Type**: String  
**Path**: `port_channel_interfaces.[].isis_authentication.level_2.key_ids.[].algorithm`  
**Valid Values**: `sha-1`, `sha-224`, `sha-256`, `sha-384`, `sha-512`  
---

### algorithm

**Type**: String  
**Path**: `port_channel_interfaces.[].isis_authentication.level_2.shared_secret.algorithm`  
**Valid Values**: `md5`, `sha-1`, `sha-224`, `sha-256`, `sha-384`, `sha-512`  
---

### algorithm

**Type**: String  
**Path**: `port_channel_interfaces.[].evpn_ethernet_segment.designated_forwarder_election.algorithm`  
**Valid Values**: `modulus`, `preference`  
---

## D

### delay_mechanism

**Type**: String  
**Path**: `port_channel_interfaces.[].ptp.delay_mechanism`  
**Valid Values**: `e2e`, `p2p`  
---

### destination_mac_address

**Type**: String  
**Path**: `port_channel_interfaces.[].ptp.profile.g8275_1.destination_mac_address`  
**Valid Values**: `forwardable`, `non-forwardable`  
---

### direction

**Type**: String  
**Path**: `port_channel_interfaces.[].link_tracking_groups.[].direction`  
**Valid Values**: `upstream`, `downstream`  
---

### direction

**Type**: String  
**Path**: `port_channel_interfaces.[].link_tracking.direction`  
**Valid Values**: `upstream`, `downstream`  
---

### direction

**Type**: String  
**Path**: `port_channel_interfaces.[].ip_nat.destination.static.[].direction`  
**Valid Values**: `egress`, `ingress`  

Egress or ingress can be the default. This depends on source/destination, EOS version, and hardware platform.
EOS might remove this keyword in the configuration. So, check the configuration on targeted HW/SW.


---

### direction

**Type**: String  
**Path**: `port_channel_interfaces.[].ip_nat.source.static.[].direction`  
**Valid Values**: `egress`, `ingress`  

Egress or ingress can be the default. This depends on source/destination, EOS version, and hardware platform.
EOS might remove this keyword in the configuration. So, check the configuration on targeted HW/SW.


---

### dot1q_dzgre_source

**Type**: String  
**Path**: `port_channel_interfaces.[].switchport.tool.identity.dot1q_dzgre_source`  
**Valid Values**: `policy`, `port`  
---

## E

### encapsulation

**Type**: String  
**Path**: `port_channel_interfaces.[].encapsulation_vlan.client.encapsulation`  
**Valid Values**: `dot1q`, `dot1ad`, `unmatched`, `untagged`  
---

### encapsulation

**Type**: String  
**Path**: `port_channel_interfaces.[].encapsulation_vlan.network.encapsulation`  
**Valid Values**: `dot1q`, `dot1ad`, `client`, `client inner`, `untagged`  

`untagged` (no encapsulation) is applicable for `untagged` client only.
`client` and `client inner` (retain client encapsulation) is not applicable for `untagged` client.

---

## H

### hash_algorithm

**Type**: String  
**Path**: `port_channel_interfaces.[].ospf_message_digest_keys.[].hash_algorithm`  
**Valid Values**: `md5`, `sha1`, `sha256`, `sha384`, `sha512`  
---

## I

### inner_encapsulation

**Type**: String  
**Path**: `port_channel_interfaces.[].encapsulation_vlan.client.inner_encapsulation`  
**Valid Values**: `dot1q`, `dot1ad`  
---

### inner_encapsulation

**Type**: String  
**Path**: `port_channel_interfaces.[].encapsulation_vlan.network.inner_encapsulation`  
**Valid Values**: `dot1q`, `dot1ad`  
---

### ip_verify_unicast_source_reachable_via

**Type**: String  
**Path**: `port_channel_interfaces.[].ip_verify_unicast_source_reachable_via`  
**Valid Values**: `any`, `rx`  
---

### isis_circuit_type

**Type**: String  
**Path**: `port_channel_interfaces.[].isis_circuit_type`  
**Valid Values**: `level-1-2`, `level-1`, `level-2`  
---

## K

### key_type

**Type**: String  
**Path**: `port_channel_interfaces.[].isis_authentication.both.key_type`  
**Valid Values**: `0`, `7`, `8a`  

Configure authentication key type.

---

### key_type

**Type**: String  
**Path**: `port_channel_interfaces.[].isis_authentication.both.key_ids.[].key_type`  
**Valid Values**: `0`, `7`, `8a`  

Configure authentication key type.

---

### key_type

**Type**: String  
**Path**: `port_channel_interfaces.[].isis_authentication.level_1.key_type`  
**Valid Values**: `0`, `7`, `8a`  

Configure authentication key type.

---

### key_type

**Type**: String  
**Path**: `port_channel_interfaces.[].isis_authentication.level_1.key_ids.[].key_type`  
**Valid Values**: `0`, `7`, `8a`  

Configure authentication key type.

---

### key_type

**Type**: String  
**Path**: `port_channel_interfaces.[].isis_authentication.level_2.key_type`  
**Valid Values**: `0`, `7`, `8a`  

Configure authentication key type.

---

### key_type

**Type**: String  
**Path**: `port_channel_interfaces.[].isis_authentication.level_2.key_ids.[].key_type`  
**Valid Values**: `0`, `7`, `8a`  

Configure authentication key type.

---

### key_type

**Type**: String  
**Path**: `port_channel_interfaces.[].ospf_message_digest_keys.[].key_type`  
**Default**: `7`  
**Valid Values**: `7`, `8a`  

Authentication key type.

---

### key_type

**Type**: String  
**Path**: `port_channel_interfaces.[].vrrp_ids.[].peer_authentication.key_type`  
**Valid Values**: `0`, `7`, `8a`  

Authentication key type.

---

## L

### lacp_fallback_mode

**Type**: String  
**Path**: `port_channel_interfaces.[].lacp_fallback_mode`  
**Valid Values**: `individual`, `static`  
---

## M

### mode

**Type**: String  
**Path**: `port_channel_interfaces.[].isis_authentication.both.mode`  
**Valid Values**: `md5`, `sha`, `text`, `shared-secret`  

Authentication mode.

---

### mode

**Type**: String  
**Path**: `port_channel_interfaces.[].isis_authentication.level_1.mode`  
**Valid Values**: `md5`, `sha`, `text`, `shared-secret`  

Authentication mode.

---

### mode

**Type**: String  
**Path**: `port_channel_interfaces.[].isis_authentication.level_2.mode`  
**Valid Values**: `md5`, `sha`, `text`, `shared-secret`  

Authentication mode.

---

### mode

**Type**: String  
**Path**: `port_channel_interfaces.[].vrrp_ids.[].peer_authentication.mode`  
**Valid Values**: `text`, `ietf-md5`  

Authentication mode.

---

### mode

**Type**: String  
**Path**: `port_channel_interfaces.[].switchport.mode`  
**Valid Values**: `access`, `dot1q-tunnel`, `trunk`, `trunk phone`  
---

### mode

**Type**: String  
**Path**: `port_channel_interfaces.[].switchport.port_security.violation.mode`  
**Valid Values**: `shutdown`, `protect`  

Configure port security mode.

---

## N

### nat_type

**Type**: String  
**Path**: `port_channel_interfaces.[].ip_nat.source.dynamic.[].nat_type`  
**Valid Values**: `overload`, `pool`, `pool-address-only`, `pool-full-cone`  
---

## O

### ospf_authentication

**Type**: String  
**Path**: `port_channel_interfaces.[].ospf_authentication`  
**Valid Values**: `none`, `simple`, `message-digest`  
---

### ospf_authentication_key_type

**Type**: String  
**Path**: `port_channel_interfaces.[].ospf_authentication_key_type`  
**Default**: `7`  
**Valid Values**: `7`, `8a`  

Authentication key type.

---

## P

### protocol

**Type**: String  
**Path**: `port_channel_interfaces.[].ip_nat.destination.static.[].protocol`  
**Valid Values**: `udp`, `tcp`  
---

### protocol

**Type**: String  
**Path**: `port_channel_interfaces.[].ip_nat.source.static.[].protocol`  
**Valid Values**: `udp`, `tcp`  
---

## Q

### qinq_dzgre_source

**Type**: String  
**Path**: `port_channel_interfaces.[].switchport.tool.identity.qinq_dzgre_source`  
**Valid Values**: `policy inner port`, `port inner policy`  
---

## R

### redundancy

**Type**: String  
**Path**: `port_channel_interfaces.[].evpn_ethernet_segment.redundancy`  
**Valid Values**: `all-active`, `single-active`  
---

### role

**Type**: String  
**Path**: `port_channel_interfaces.[].ptp.role`  
**Valid Values**: `master`, `dynamic`  
---

## S

### source_interface

**Type**: String  
**Path**: `port_channel_interfaces.[].switchport.source_interface`  
**Valid Values**: `tx`, `tx multicast`  

tx: Allow bridged traffic to go out of the source interface.
tx multicast: Allow multicast traffic only to go out of the source interface.

---

### spanning_tree_bpdufilter

**Type**: String  
**Path**: `port_channel_interfaces.[].spanning_tree_bpdufilter`  
**Valid Values**: `enabled`, `disabled`, `True`, `False`, `true`, `false`  
---

### spanning_tree_bpduguard

**Type**: String  
**Path**: `port_channel_interfaces.[].spanning_tree_bpduguard`  
**Valid Values**: `enabled`, `disabled`, `True`, `False`, `true`, `false`  
---

### spanning_tree_guard

**Type**: String  
**Path**: `port_channel_interfaces.[].spanning_tree_guard`  
**Valid Values**: `loop`, `root`, `disabled`  
---

### spanning_tree_portfast

**Type**: String  
**Path**: `port_channel_interfaces.[].spanning_tree_portfast`  
**Valid Values**: `edge`, `network`  
---

## T

### tag

**Type**: String  
**Path**: `port_channel_interfaces.[].switchport.tool.identity.tag`  
**Valid Values**: `dot1q`, `qinq`  
---

### transport

**Type**: String  
**Path**: `port_channel_interfaces.[].ptp.transport`  
**Valid Values**: `ipv4`, `ipv6`, `layer2`  
---

### trunk

**Type**: String  
**Path**: `port_channel_interfaces.[].switchport.phone.trunk`  
**Valid Values**: `tagged`, `tagged phone`, `untagged`, `untagged phone`  
---

### trust

**Type**: String  
**Path**: `port_channel_interfaces.[].qos.trust`  
**Valid Values**: `dscp`, `cos`, `disabled`  
---

## U

### unit

**Type**: String  
**Path**: `port_channel_interfaces.[].storm_control.all.unit`  
**Default**: `percent`  
**Valid Values**: `percent`, `pps`  

Optional field and is hardware dependent.

---

### unit

**Type**: String  
**Path**: `port_channel_interfaces.[].storm_control.broadcast.unit`  
**Default**: `percent`  
**Valid Values**: `percent`, `pps`  

Optional field and is hardware dependent.

---

### unit

**Type**: String  
**Path**: `port_channel_interfaces.[].storm_control.multicast.unit`  
**Default**: `percent`  
**Valid Values**: `percent`, `pps`  

Optional field and is hardware dependent.

---

### unit

**Type**: String  
**Path**: `port_channel_interfaces.[].storm_control.unknown_unicast.unit`  
**Default**: `percent`  
**Valid Values**: `percent`, `pps`  

Optional field and is hardware dependent.

---

### unit

**Type**: String  
**Path**: `port_channel_interfaces.[].traffic_engineering.bandwidth.unit`  
**Valid Values**: `gbps`, `mbps`, `percent`  
---

### unit

**Type**: String  
**Path**: `port_channel_interfaces.[].traffic_engineering.min_delay_static.unit`  
**Valid Values**: `microseconds`, `milliseconds`  
---

### unit

**Type**: String  
**Path**: `port_channel_interfaces.[].traffic_engineering.min_delay_dynamic.twamp_light_fallback.unit`  
**Valid Values**: `microseconds`, `milliseconds`  
---

## V

### version

**Type**: Integer  
**Path**: `port_channel_interfaces.[].vrrp_ids.[].ipv4.version`  
**Valid Values**: `2`, `3`  
---

### vlan_tag

**Type**: String  
**Path**: `port_channel_interfaces.[].switchport.dot1q.vlan_tag`  
**Valid Values**: `disallowed`, `required`  
---
