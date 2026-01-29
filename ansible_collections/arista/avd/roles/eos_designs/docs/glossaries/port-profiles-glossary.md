# Glossary

## Table of Contents

- [A](#a)
- [D](#d)
- [E](#e)
- [M](#m)
- [P](#p)
- [R](#r)
- [S](#s)
- [T](#t)
- [U](#u)

## A

### action

**Type**: String  
**Path**: `port_profiles.[].dot1x.authentication_failure.action`  
**Valid Values**: `allow`, `drop`  
---

### action

**Type**: String  
**Path**: `port_profiles.[].poe.reboot.action`  
**Valid Values**: `maintain`, `power-off`  

PoE action for interface.

---

### action

**Type**: String  
**Path**: `port_profiles.[].poe.link_down.action`  
**Valid Values**: `maintain`, `power-off`  

PoE action for interface.

---

### action

**Type**: String  
**Path**: `port_profiles.[].poe.shutdown.action`  
**Valid Values**: `maintain`, `power-off`  

PoE action for interface.

---

## D

### designated_forwarder_algorithm

**Type**: String  
**Path**: `port_profiles.[].ethernet_segment.designated_forwarder_algorithm`  
**Valid Values**: `auto`, `modulus`, `preference`  

Configure DF algorithm and preferences.
- auto: Use preference-based algorithm and assign preference based on position of device in the 'switches' list,
  e.g., assuming a list of three switches, this would assign a preference of 200 to the first switch, 100 to the 2nd, and 0 to the third.
- preference: Set preference for each switch manually using designated_forwarder_preferences key.
- modulus: Use the default modulus-based algorithm.
If omitted, Port-Channels use the EOS default of modulus.
If omitted, Ethernet interfaces default to the 'auto' mechanism detailed above.


---

### direction

**Type**: String  
**Path**: `port_profiles.[].monitor_sessions.[].source_settings.direction`  
**Valid Values**: `rx`, `tx`, `both`  
---

## E

### eap_response

**Type**: String  
**Path**: `port_profiles.[].dot1x.aaa.unresponsive.eap_response`  
**Valid Values**: `success`, `disabled`  

EAP response to send. EOS default is `success`.

---

### endpoint_role

**Type**: String  
**Path**: `port_profiles.[].ptp.endpoint_role`  
**Default**: `follower`  
**Valid Values**: `follower`, `dynamic`, `bmca`, `default`  

PTP role of the endpoint.
`follower` will configure the switch port as `ptp role master`.
`dynamic` will use BMCA.
`default` is deprecated in favor of `follower`.
`bmca` is deprecated in favor of `dynamic`.

---

## M

### mode

**Type**: String  
**Path**: `port_profiles.[].mode`  
**Valid Values**: `access`, `dot1q-tunnel`, `trunk`, `trunk phone`  

Interface mode.

---

### mode

**Type**: String  
**Path**: `port_profiles.[].dot1x.pae.mode`  
**Valid Values**: `authenticator`, `supplicant`  
---

### mode

**Type**: String  
**Path**: `port_profiles.[].dot1x.host_mode.mode`  
**Valid Values**: `multi-host`, `single-host`  
---

### mode

**Type**: String  
**Path**: `port_profiles.[].port_channel.mode`  
**Valid Values**: `active`, `passive`, `on`  

Port-Channel Mode.

---

### mode

**Type**: String  
**Path**: `port_profiles.[].port_channel.lacp_fallback.mode`  
**Valid Values**: `static`, `individual`  

Either static or individual mode is supported.
If the mode is set to "individual" either 'profile' or ('mode' and 'vlans')  must be set under 'port_channel.lacp_fallback.individual'.


---

### mode

**Type**: String  
**Path**: `port_profiles.[].port_channel.lacp_fallback.individual.mode`  
**Valid Values**: `access`, `dot1q-tunnel`, `trunk`, `trunk phone`  

Interface mode on the port-channel member interfaces when in fallback individual.

---

### mode

**Type**: String  
**Path**: `port_profiles.[].port_channel.lacp_timer.mode`  
**Valid Values**: `normal`, `fast`  

LACP mode for interface members.

---

## P

### phone_trunk_mode

**Type**: String  
**Path**: `port_profiles.[].phone_trunk_mode`  
**Valid Values**: `tagged`, `untagged`, `tagged phone`, `untagged phone`  

Specify if the phone traffic is tagged or untagged.
If both data and phone traffic are untagged, MAC-Based VLAN Assignment (MBVA) is used, if supported by the model of switch.

---

### port_control

**Type**: String  
**Path**: `port_profiles.[].dot1x.port_control`  
**Valid Values**: `auto`, `force-authorized`, `force-unauthorized`  
---

### port_profiles

**Type**: List, items: Dictionary  
**Path**: `port_profiles`  

Optional profiles to share common settings for connected_endpoints and/or network_ports.
Keys are the same used under endpoints adapters. Keys defined under endpoints adapters take precedence.


---

### priority

**Type**: String  
**Path**: `port_profiles.[].poe.priority`  
**Valid Values**: `critical`, `high`, `medium`, `low`  

Prioritize a port's power in the event that one of the switch's power supplies loses power.

---

## R

### received

**Type**: String  
**Path**: `port_profiles.[].flowcontrol.received`  
**Valid Values**: `desired`, `on`, `off`  
---

### redundancy

**Type**: String  
**Path**: `port_profiles.[].ethernet_segment.redundancy`  
**Valid Values**: `all-active`, `single-active`  

If omitted, Port-Channels use the EOS default of all-active.
If omitted, Ethernet interfaces are configured as single-active.


---

### role

**Type**: String  
**Path**: `port_profiles.[].monitor_sessions.[].role`  
**Valid Values**: `source`, `destination`  
---

## S

### spanning_tree_bpdufilter

**Type**: String  
**Path**: `port_profiles.[].spanning_tree_bpdufilter`  
**Valid Values**: `enabled`, `disabled`, `True`, `False`, `true`, `false`  
---

### spanning_tree_bpduguard

**Type**: String  
**Path**: `port_profiles.[].spanning_tree_bpduguard`  
**Valid Values**: `enabled`, `disabled`, `True`, `False`, `true`, `false`  
---

### spanning_tree_portfast

**Type**: String  
**Path**: `port_profiles.[].spanning_tree_portfast`  
**Valid Values**: `edge`, `network`  
---

### speed

**Type**: String  
**Path**: `port_profiles.[].speed`  
**Valid Values**: `100full`, `100g`, `100g-1`, `100g-2`, `100g-4`, `100half`, `10full`, `10g`, `10half`, `1g`, `200g`, `200g-2`, `200g-4`, `25g`, `400g`, `400g-4`, `400g-8`, `40g`, `50g`, `50g-1`, `50g-2`, `800g-8`, `sfp-1000baset auto 100full`, `1.6t-8`, `100mfull`, `100mhalf`, `10mfull`, `10mhalf`, `200g-1`, `400g-2`, `40g-4`, `800g-4`, `auto`, `auto 10000full`, `auto 1000full`, `auto 100full`, `auto 100g-1`, `auto 100g-2`, `auto 100g-4`, `auto 100gfull`, `auto 100half`, `auto 10full`, `auto 10gfull`, `auto 10half`, `auto 1gfull`, `auto 2.5gfull`, `auto 200g-2`, `auto 200g-4`, `auto 25gfull`, `auto 400g-4`, `auto 400g-8`, `auto 40gfull`, `auto 50g-1`, `auto 50g-2`, `auto 50gfull`, `auto 5gfull`, `auto 800g-8`, `auto 1.6t-8`, `auto 100mfull`, `auto 100mhalf`, `auto 10g`, `auto 10mfull`, `auto 10mhalf`, `auto 1g`, `auto 2.5g`, `auto 200g-1`, `auto 25g`, `auto 400g-2`, `auto 40g-4`, `auto 5g`, `auto 800g-4`, `forced 10000full`, `forced 1000full`, `forced 1000half`, `forced 100full`, `forced 100gfull`, `forced 100half`, `forced 10full`, `forced 10half`, `forced 25gfull`, `forced 40gfull`, `forced 50gfull`  

Set adapter speed.
If not specified speed will be auto.


---

## T

### time_duration_unit

**Type**: String  
**Path**: `port_profiles.[].dot1x.aaa.unresponsive.action.cached_results_timeout.time_duration_unit`  
**Valid Values**: `days`, `hours`, `minutes`, `seconds`  
---

### time_duration_unit

**Type**: String  
**Path**: `port_profiles.[].dot1x.aaa.unresponsive.phone_action.cached_results_timeout.time_duration_unit`  
**Valid Values**: `days`, `hours`, `minutes`, `seconds`  
---

### type

**Type**: String  
**Path**: `port_profiles.[].monitor_sessions.[].source_settings.access_group.type`  
**Valid Values**: `ip`, `ipv6`, `mac`  
---

### type

**Type**: String  
**Path**: `port_profiles.[].monitor_sessions.[].session_settings.access_group.type`  
**Valid Values**: `ip`, `ipv6`, `mac`  
---

## U

### unit

**Type**: String  
**Path**: `port_profiles.[].storm_control.all.unit`  
**Default**: `percent`  
**Valid Values**: `percent`, `pps`  

Optional variable and is hardware dependent.

---

### unit

**Type**: String  
**Path**: `port_profiles.[].storm_control.broadcast.unit`  
**Default**: `percent`  
**Valid Values**: `percent`, `pps`  

Optional variable and is hardware dependent.

---

### unit

**Type**: String  
**Path**: `port_profiles.[].storm_control.multicast.unit`  
**Default**: `percent`  
**Valid Values**: `percent`, `pps`  

Optional variable and is hardware dependent.

---

### unit

**Type**: String  
**Path**: `port_profiles.[].storm_control.unknown_unicast.unit`  
**Default**: `percent`  
**Valid Values**: `percent`, `pps`  

Optional variable and is hardware dependent.

---
