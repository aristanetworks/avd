# Glossary

## Table of Contents

- [A](#a)
- [D](#d)
- [E](#e)
- [F](#f)
- [H](#h)
- [I](#i)
- [K](#k)
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

### action

**Type**: String  
**Path**: `ethernet_interfaces.[].poe.reboot.action`  
**Valid Values**: `maintain`, `power-off`  

PoE action for interface.

---

### action

**Type**: String  
**Path**: `ethernet_interfaces.[].poe.link_down.action`  
**Valid Values**: `maintain`, `power-off`  

PoE action for interface.

---

### action

**Type**: String  
**Path**: `ethernet_interfaces.[].poe.shutdown.action`  
**Valid Values**: `maintain`, `power-off`  

PoE action for interface.

---

### action

**Type**: String  
**Path**: `ethernet_interfaces.[].dot1x.authentication_failure.action`  
**Valid Values**: `allow`, `drop`  
---

### algorithm

**Type**: String  
**Path**: `ethernet_interfaces.[].evpn_ethernet_segment.designated_forwarder_election.algorithm`  
**Valid Values**: `modulus`, `preference`  
---

### algorithm

**Type**: String  
**Path**: `ethernet_interfaces.[].isis_authentication.both.key_ids.[].algorithm`  
**Valid Values**: `sha-1`, `sha-224`, `sha-256`, `sha-384`, `sha-512`  
---

### algorithm

**Type**: String  
**Path**: `ethernet_interfaces.[].isis_authentication.both.shared_secret.algorithm`  
**Valid Values**: `md5`, `sha-1`, `sha-224`, `sha-256`, `sha-384`, `sha-512`  
---

### algorithm

**Type**: String  
**Path**: `ethernet_interfaces.[].isis_authentication.level_1.key_ids.[].algorithm`  
**Valid Values**: `sha-1`, `sha-224`, `sha-256`, `sha-384`, `sha-512`  
---

### algorithm

**Type**: String  
**Path**: `ethernet_interfaces.[].isis_authentication.level_1.shared_secret.algorithm`  
**Valid Values**: `md5`, `sha-1`, `sha-224`, `sha-256`, `sha-384`, `sha-512`  
---

### algorithm

**Type**: String  
**Path**: `ethernet_interfaces.[].isis_authentication.level_2.key_ids.[].algorithm`  
**Valid Values**: `sha-1`, `sha-224`, `sha-256`, `sha-384`, `sha-512`  
---

### algorithm

**Type**: String  
**Path**: `ethernet_interfaces.[].isis_authentication.level_2.shared_secret.algorithm`  
**Valid Values**: `md5`, `sha-1`, `sha-224`, `sha-256`, `sha-384`, `sha-512`  
---

### application_override

**Type**: String  
**Path**: `ethernet_interfaces.[].transceiver.application_override`  
**Valid Values**: `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `13`, `14`, `15`, `100gbase-srbd`  

Set CMIS transceiver application.
'100gbase-srbd' should not be used in conjunction with `application_override_lanes`.

---

## D

### delay_mechanism

**Type**: String  
**Path**: `ethernet_interfaces.[].ptp.delay_mechanism`  
**Valid Values**: `e2e`, `p2p`  
---

### destination_mac_address

**Type**: String  
**Path**: `ethernet_interfaces.[].ptp.profile.g8275_1.destination_mac_address`  
**Valid Values**: `forwardable`, `non-forwardable`  
---

### direction

**Type**: String  
**Path**: `ethernet_interfaces.[].link_tracking_groups.[].direction`  
**Valid Values**: `upstream`, `downstream`  
---

### direction

**Type**: String  
**Path**: `ethernet_interfaces.[].link_tracking.direction`  
**Valid Values**: `upstream`, `downstream`  
---

### direction

**Type**: String  
**Path**: `ethernet_interfaces.[].ip_nat.destination.static.[].direction`  
**Valid Values**: `egress`, `ingress`  

Egress or ingress can be the default. This depends on source/destination, EOS version, and hardware platform.
EOS might remove this keyword in the configuration. So, check the configuration on targeted HW/SW.


---

### direction

**Type**: String  
**Path**: `ethernet_interfaces.[].ip_nat.source.static.[].direction`  
**Valid Values**: `egress`, `ingress`  

Egress or ingress can be the default. This depends on source/destination, EOS version, and hardware platform.
EOS might remove this keyword in the configuration. So, check the configuration on targeted HW/SW.


---

### direction

**Type**: String  
**Path**: `ethernet_interfaces.[].tcp_mss_ceiling.direction`  
**Valid Values**: `egress`, `ingress`  
---

### dot1q_dzgre_source

**Type**: String  
**Path**: `ethernet_interfaces.[].switchport.tool.identity.dot1q_dzgre_source`  
**Valid Values**: `policy`, `port`  
---

## E

### eap_response

**Type**: String  
**Path**: `ethernet_interfaces.[].dot1x.aaa.unresponsive.eap_response`  
**Valid Values**: `success`, `disabled`  

EAP response to send. EOS default is `success`.

---

### encapsulation

**Type**: String  
**Path**: `ethernet_interfaces.[].encapsulation_vlan.client.encapsulation`  
**Valid Values**: `dot1q`, `dot1ad`, `unmatched`, `untagged`  
---

### encapsulation

**Type**: String  
**Path**: `ethernet_interfaces.[].encapsulation_vlan.network.encapsulation`  
**Valid Values**: `dot1q`, `dot1ad`, `client`, `client inner`, `untagged`  

`untagged` (no encapsulation) is applicable for `untagged` client only.
`client` and `client inner` (retain client encapsulation) is not applicable for `untagged` client.

---

## F

### frequency_unit

**Type**: String  
**Path**: `ethernet_interfaces.[].transceiver.frequency_unit`  
**Valid Values**: `ghz`  

Unit of Transceiver Laser Frequency.

---

## H

### hash_algorithm

**Type**: String  
**Path**: `ethernet_interfaces.[].ospf_message_digest_keys.[].hash_algorithm`  
**Valid Values**: `md5`, `sha1`, `sha256`, `sha384`, `sha512`  
---

## I

### inner_encapsulation

**Type**: String  
**Path**: `ethernet_interfaces.[].encapsulation_vlan.client.inner_encapsulation`  
**Valid Values**: `dot1q`, `dot1ad`  
---

### inner_encapsulation

**Type**: String  
**Path**: `ethernet_interfaces.[].encapsulation_vlan.network.inner_encapsulation`  
**Valid Values**: `dot1q`, `dot1ad`  
---

### ip_verify_unicast_source_reachable_via

**Type**: String  
**Path**: `ethernet_interfaces.[].ip_verify_unicast_source_reachable_via`  
**Valid Values**: `any`, `rx`  
---

### isis_authentication_mode

**Type**: String  
**Path**: `ethernet_interfaces.[].isis_authentication_mode`  
**Valid Values**: `text`, `md5`  
---

### isis_circuit_type

**Type**: String  
**Path**: `ethernet_interfaces.[].isis_circuit_type`  
**Valid Values**: `level-1-2`, `level-1`, `level-2`  
---

## K

### key_type

**Type**: String  
**Path**: `ethernet_interfaces.[].ospf_message_digest_keys.[].key_type`  
**Default**: `7`  
**Valid Values**: `7`, `8a`  

Authentication key type.

---

### key_type

**Type**: String  
**Path**: `ethernet_interfaces.[].isis_authentication.both.key_type`  
**Valid Values**: `0`, `7`, `8a`  

Configure authentication key type.

---

### key_type

**Type**: String  
**Path**: `ethernet_interfaces.[].isis_authentication.both.key_ids.[].key_type`  
**Valid Values**: `0`, `7`, `8a`  

Configure authentication key type.

---

### key_type

**Type**: String  
**Path**: `ethernet_interfaces.[].isis_authentication.level_1.key_type`  
**Valid Values**: `0`, `7`, `8a`  

Configure authentication key type.

---

### key_type

**Type**: String  
**Path**: `ethernet_interfaces.[].isis_authentication.level_1.key_ids.[].key_type`  
**Valid Values**: `0`, `7`, `8a`  

Configure authentication key type.

---

### key_type

**Type**: String  
**Path**: `ethernet_interfaces.[].isis_authentication.level_2.key_type`  
**Valid Values**: `0`, `7`, `8a`  

Configure authentication key type.

---

### key_type

**Type**: String  
**Path**: `ethernet_interfaces.[].isis_authentication.level_2.key_ids.[].key_type`  
**Valid Values**: `0`, `7`, `8a`  

Configure authentication key type.

---

### key_type

**Type**: String  
**Path**: `ethernet_interfaces.[].vrrp_ids.[].peer_authentication.key_type`  
**Valid Values**: `0`, `7`, `8a`  

Authentication key type.

---

## M

### mac_timestamp

**Type**: String  
**Path**: `ethernet_interfaces.[].mac_timestamp`  
**Valid Values**: `before-fcs`, `replace-fcs`, `header`  

header: Insert timestamp in ethernet header. Supported on platforms like 7500E/R and 7280E/R.
before-fcs: Insert timestamp before fcs field. Supported on platforms like 7150.
replace-fcs: Replace fcs field with timestamp.

---

### mode

**Type**: String  
**Path**: `ethernet_interfaces.[].channel_group.mode`  
**Valid Values**: `on`, `active`, `passive`  
---

### mode

**Type**: String  
**Path**: `ethernet_interfaces.[].isis_authentication.both.mode`  
**Valid Values**: `md5`, `sha`, `text`, `shared-secret`  

Authentication mode.

---

### mode

**Type**: String  
**Path**: `ethernet_interfaces.[].isis_authentication.level_1.mode`  
**Valid Values**: `md5`, `sha`, `text`, `shared-secret`  

Authentication mode.

---

### mode

**Type**: String  
**Path**: `ethernet_interfaces.[].isis_authentication.level_2.mode`  
**Valid Values**: `md5`, `sha`, `text`, `shared-secret`  

Authentication mode.

---

### mode

**Type**: String  
**Path**: `ethernet_interfaces.[].dot1x.pae.mode`  
**Valid Values**: `authenticator`, `supplicant`  
---

### mode

**Type**: String  
**Path**: `ethernet_interfaces.[].dot1x.host_mode.mode`  
**Valid Values**: `multi-host`, `single-host`  
---

### mode

**Type**: String  
**Path**: `ethernet_interfaces.[].lacp_timer.mode`  
**Valid Values**: `fast`, `normal`  
---

### mode

**Type**: String  
**Path**: `ethernet_interfaces.[].vrrp_ids.[].peer_authentication.mode`  
**Valid Values**: `text`, `ietf-md5`  

Authentication mode.

---

### mode

**Type**: String  
**Path**: `ethernet_interfaces.[].switchport.mode`  
**Valid Values**: `access`, `dot1q-tunnel`, `trunk`, `trunk phone`, `tap`, `tool`, `tap-tool`  
---

### mode

**Type**: String  
**Path**: `ethernet_interfaces.[].switchport.port_security.violation.mode`  
**Valid Values**: `shutdown`, `protect`  

Configure port security mode.

---

### mode

**Type**: String  
**Path**: `ethernet_interfaces.[].mode`  
**Valid Values**: `access`, `dot1q-tunnel`, `trunk`, `trunk phone`  
---

## N

### nat_type

**Type**: String  
**Path**: `ethernet_interfaces.[].ip_nat.source.dynamic.[].nat_type`  
**Valid Values**: `overload`, `pool`, `pool-address-only`, `pool-full-cone`  
---

## O

### ospf_authentication

**Type**: String  
**Path**: `ethernet_interfaces.[].ospf_authentication`  
**Valid Values**: `none`, `simple`, `message-digest`  
---

### ospf_authentication_key_type

**Type**: String  
**Path**: `ethernet_interfaces.[].ospf_authentication_key_type`  
**Default**: `7`  
**Valid Values**: `7`, `8a`  

Authentication key type.

---

## P

### port_control

**Type**: String  
**Path**: `ethernet_interfaces.[].dot1x.port_control`  
**Valid Values**: `auto`, `force-authorized`, `force-unauthorized`  
---

### priority

**Type**: String  
**Path**: `ethernet_interfaces.[].poe.priority`  
**Valid Values**: `critical`, `high`, `medium`, `low`  

Prioritize a port's power in the event that one of the switch's power supplies loses power.

---

### protocol

**Type**: String  
**Path**: `ethernet_interfaces.[].ip_nat.destination.static.[].protocol`  
**Valid Values**: `udp`, `tcp`  
---

### protocol

**Type**: String  
**Path**: `ethernet_interfaces.[].ip_nat.source.static.[].protocol`  
**Valid Values**: `udp`, `tcp`  
---

## Q

### qinq_dzgre_source

**Type**: String  
**Path**: `ethernet_interfaces.[].switchport.tool.identity.qinq_dzgre_source`  
**Valid Values**: `policy inner port`, `port inner policy`  
---

## R

### received

**Type**: String  
**Path**: `ethernet_interfaces.[].flowcontrol.received`  
**Valid Values**: `desired`, `on`, `off`  
---

### redundancy

**Type**: String  
**Path**: `ethernet_interfaces.[].evpn_ethernet_segment.redundancy`  
**Valid Values**: `all-active`, `single-active`  
---

### role

**Type**: String  
**Path**: `ethernet_interfaces.[].ptp.role`  
**Valid Values**: `master`, `dynamic`  
---

## S

### source_interface

**Type**: String  
**Path**: `ethernet_interfaces.[].switchport.source_interface`  
**Valid Values**: `tx`, `tx multicast`  

tx: Allow bridged traffic to go out of the source interface.
tx multicast: Allow multicast traffic only to go out of the source interface.

---

### spanning_tree_bpdufilter

**Type**: String  
**Path**: `ethernet_interfaces.[].spanning_tree_bpdufilter`  
**Valid Values**: `enabled`, `disabled`, `True`, `False`, `true`, `false`  
---

### spanning_tree_bpduguard

**Type**: String  
**Path**: `ethernet_interfaces.[].spanning_tree_bpduguard`  
**Valid Values**: `enabled`, `disabled`, `True`, `False`, `true`, `false`  
---

### spanning_tree_guard

**Type**: String  
**Path**: `ethernet_interfaces.[].spanning_tree_guard`  
**Valid Values**: `loop`, `root`, `disabled`  
---

### spanning_tree_portfast

**Type**: String  
**Path**: `ethernet_interfaces.[].spanning_tree_portfast`  
**Valid Values**: `edge`, `network`  
---

### speed

**Type**: String  
**Path**: `ethernet_interfaces.[].speed`  
**Valid Values**: `100full`, `100g`, `100g-1`, `100g-2`, `100g-4`, `100half`, `10full`, `10g`, `10half`, `1g`, `200g`, `200g-2`, `200g-4`, `25g`, `400g`, `400g-4`, `400g-8`, `40g`, `50g`, `50g-1`, `50g-2`, `800g-8`, `sfp-1000baset auto 100full`, `1.6t-8`, `100mfull`, `100mhalf`, `10mfull`, `10mhalf`, `200g-1`, `400g-2`, `40g-4`, `800g-4`, `auto`, `auto 10000full`, `auto 1000full`, `auto 100full`, `auto 100g-1`, `auto 100g-2`, `auto 100g-4`, `auto 100gfull`, `auto 100half`, `auto 10full`, `auto 10gfull`, `auto 10half`, `auto 1gfull`, `auto 2.5gfull`, `auto 200g-2`, `auto 200g-4`, `auto 25gfull`, `auto 400g-4`, `auto 400g-8`, `auto 40gfull`, `auto 50g-1`, `auto 50g-2`, `auto 50gfull`, `auto 5gfull`, `auto 800g-8`, `auto 1.6t-8`, `auto 100mfull`, `auto 100mhalf`, `auto 10g`, `auto 10mfull`, `auto 10mhalf`, `auto 1g`, `auto 2.5g`, `auto 200g-1`, `auto 25g`, `auto 400g-2`, `auto 40g-4`, `auto 5g`, `auto 800g-4`, `forced 10000full`, `forced 1000full`, `forced 1000half`, `forced 100full`, `forced 100gfull`, `forced 100half`, `forced 10full`, `forced 10half`, `forced 25gfull`, `forced 40gfull`, `forced 50gfull`  

Interface Speed.

---

## T

### tag

**Type**: String  
**Path**: `ethernet_interfaces.[].switchport.tool.identity.tag`  
**Valid Values**: `dot1q`, `qinq`  
---

### time_duration_unit

**Type**: String  
**Path**: `ethernet_interfaces.[].dot1x.aaa.unresponsive.action.cached_results_timeout.time_duration_unit`  
**Valid Values**: `days`, `hours`, `minutes`, `seconds`  
---

### time_duration_unit

**Type**: String  
**Path**: `ethernet_interfaces.[].dot1x.aaa.unresponsive.phone_action.cached_results_timeout.time_duration_unit`  
**Valid Values**: `days`, `hours`, `minutes`, `seconds`  
---

### transport

**Type**: String  
**Path**: `ethernet_interfaces.[].ptp.transport`  
**Valid Values**: `ipv4`, `ipv6`, `layer2`  
---

### trunk

**Type**: String  
**Path**: `ethernet_interfaces.[].switchport.phone.trunk`  
**Valid Values**: `tagged`, `tagged phone`, `untagged`, `untagged phone`  
---

### trust

**Type**: String  
**Path**: `ethernet_interfaces.[].qos.trust`  
**Valid Values**: `dscp`, `cos`, `disabled`  
---

### type

**Type**: String  
**Path**: `ethernet_interfaces.[].type`  
**Valid Values**: `routed`, `switched`, `l3dot1q`, `l2dot1q`, `port-channel-member`  

l3dot1q and l2dot1q are used for sub-interfaces. The parent interface should be defined as routed.
The `type = switched/routed` should not be combined with `switchport`.


---

## U

### unit

**Type**: String  
**Path**: `ethernet_interfaces.[].storm_control.all.unit`  
**Default**: `percent`  
**Valid Values**: `percent`, `pps`  

Optional field and is hardware dependent.

---

### unit

**Type**: String  
**Path**: `ethernet_interfaces.[].storm_control.broadcast.unit`  
**Default**: `percent`  
**Valid Values**: `percent`, `pps`  

Optional field and is hardware dependent.

---

### unit

**Type**: String  
**Path**: `ethernet_interfaces.[].storm_control.multicast.unit`  
**Default**: `percent`  
**Valid Values**: `percent`, `pps`  

Optional field and is hardware dependent.

---

### unit

**Type**: String  
**Path**: `ethernet_interfaces.[].storm_control.unknown_unicast.unit`  
**Default**: `percent`  
**Valid Values**: `percent`, `pps`  

Optional field and is hardware dependent.

---

### unit

**Type**: String  
**Path**: `ethernet_interfaces.[].traffic_engineering.bandwidth.unit`  
**Valid Values**: `gbps`, `mbps`, `percent`  
---

### unit

**Type**: String  
**Path**: `ethernet_interfaces.[].traffic_engineering.min_delay_static.unit`  
**Valid Values**: `microseconds`, `milliseconds`  
---

### unit

**Type**: String  
**Path**: `ethernet_interfaces.[].traffic_engineering.min_delay_dynamic.twamp_light_fallback.unit`  
**Valid Values**: `microseconds`, `milliseconds`  
---

### units

**Type**: String  
**Path**: `ethernet_interfaces.[].uc_tx_queues.[].random_detect.ecn.threshold.units`  
**Valid Values**: `segments`, `bytes`, `kbytes`, `mbytes`, `milliseconds`  

Indicate the units to be used for the threshold values.

---

### units

**Type**: String  
**Path**: `ethernet_interfaces.[].tx_queues.[].random_detect.ecn.threshold.units`  
**Valid Values**: `segments`, `bytes`, `kbytes`, `mbytes`, `milliseconds`  

Indicate the units to be used for the threshold values.

---

## V

### version

**Type**: Integer  
**Path**: `ethernet_interfaces.[].vrrp_ids.[].ipv4.version`  
**Valid Values**: `2`, `3`  
---

### vlan_tag

**Type**: String  
**Path**: `ethernet_interfaces.[].switchport.dot1q.vlan_tag`  
**Valid Values**: `disallowed`, `required`  

Allow/disallow VLAN tagged frames.

---
