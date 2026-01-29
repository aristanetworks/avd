# Glossary

## Table of Contents

- [A](#a)
- [C](#c)
- [D](#d)
- [E](#e)
- [F](#f)
- [G](#g)
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

### access

**Type**: String  
**Path**: `snmp_server.communities.[].access`  
**Valid Values**: `ro`, `rw`  
---

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

### action

**Type**: String  
**Path**: `event_handlers.[].trigger_on_maintenance.action`  
**Valid Values**: `after`, `before`, `all`, `begin`, `end`  

Action for maintenance operation.

---

### action

**Type**: String  
**Path**: `ip_access_lists.[].entries.[].action`  
**Valid Values**: `permit`, `deny`  

ACL action.
Required except for remarks.

---

### action

**Type**: String  
**Path**: `ip_community_lists.[].entries.[].action`  
**Valid Values**: `permit`, `deny`  
---

### action

**Type**: String  
**Path**: `ip_large_community_lists.[].entries.[].action`  
**Valid Values**: `permit`, `deny`  
---

### action

**Type**: String  
**Path**: `ip_security.profiles.[].dpd.action`  
**Valid Values**: `clear`, `hold`, `restart`  

Action to apply.

* 'clear': Delete all connections
* 'hold': Re-negotiate connection on demand
* 'restart': Restart connection immediately


---

### action

**Type**: String  
**Path**: `logging.policy.match.match_lists.[].action`  
**Valid Values**: `discard`  
---

### action

**Type**: String  
**Path**: `mac_security.profiles.[].traffic_unprotected.action`  
**Valid Values**: `allow`, `drop`  

Allow/drop the transmit/receive of unprotected traffic.

---

### action

**Type**: String  
**Path**: `poe.reboot.action`  
**Valid Values**: `power-off`, `maintain`  

PoE action for interface. By default in EOS, reboot action is set to power-off.

---

### action

**Type**: String  
**Path**: `poe.interface_shutdown.action`  
**Valid Values**: `power-off`, `maintain`  

PoE action for interface. By default in EOS, interface shutdown action is set to maintain.

---

### action

**Type**: String  
**Path**: `priority_flow_control.watchdog.action`  
**Valid Values**: `drop`, `errdisable`, `notify-only`  

Action on stuck queue.


---

### action

**Type**: String  
**Path**: `qos_profiles.[].priority_flow_control.watchdog.action`  
**Valid Values**: `drop`, `notify-only`  

Override the default error-disable action to either drop
traffic on the stuck queue or notify-only
without making any actions on the stuck queue.


---

### action

**Type**: String  
**Path**: `roles.[].sequence_numbers.[].action`  
**Valid Values**: `permit`, `deny`  
---

### action

**Type**: String  
**Path**: `router_bgp.peer_groups.[].missing_policy.direction_in.action`  
**Valid Values**: `deny`, `permit`, `deny-in-out`  

Missing policy action.

---

### action

**Type**: String  
**Path**: `router_bgp.peer_groups.[].missing_policy.direction_out.action`  
**Valid Values**: `deny`, `permit`, `deny-in-out`  

Missing policy action.

---

### action

**Type**: String  
**Path**: `router_bgp.neighbors.[].missing_policy.direction_in.action`  
**Valid Values**: `deny`, `permit`, `deny-in-out`  

Missing policy action.

---

### action

**Type**: String  
**Path**: `router_bgp.neighbors.[].missing_policy.direction_out.action`  
**Valid Values**: `deny`, `permit`, `deny-in-out`  

Missing policy action.

---

### action

**Type**: String  
**Path**: `router_bgp.address_family_ipv4_labeled_unicast.bgp.missing_policy.direction_in.action`  
**Valid Values**: `deny`, `permit`, `deny-in-out`  

Missing policy action.

---

### action

**Type**: String  
**Path**: `router_bgp.address_family_ipv4_labeled_unicast.bgp.missing_policy.direction_out.action`  
**Valid Values**: `deny`, `permit`, `deny-in-out`  

Missing policy action.

---

### action

**Type**: String  
**Path**: `router_bgp.address_family_ipv4_labeled_unicast.peer_groups.[].missing_policy.direction_in.action`  
**Valid Values**: `deny`, `permit`, `deny-in-out`  

Missing policy action.

---

### action

**Type**: String  
**Path**: `router_bgp.address_family_ipv4_labeled_unicast.peer_groups.[].missing_policy.direction_out.action`  
**Valid Values**: `deny`, `permit`, `deny-in-out`  

Missing policy action.

---

### action

**Type**: String  
**Path**: `router_bgp.address_family_ipv4_labeled_unicast.neighbors.[].missing_policy.direction_in.action`  
**Valid Values**: `deny`, `permit`, `deny-in-out`  

Missing policy action.

---

### action

**Type**: String  
**Path**: `router_bgp.address_family_ipv4_labeled_unicast.neighbors.[].missing_policy.direction_out.action`  
**Valid Values**: `deny`, `permit`, `deny-in-out`  

Missing policy action.

---

### action

**Type**: String  
**Path**: `router_segment_security.policies.[].sequence_numbers.[].action`  
**Valid Values**: `forward`, `drop`, `redirect`  

The action to take - note that platform support for the redirect action is limited. The "redirect" action also requires the 'next_hop' to be configured.

---

### address_family

**Type**: String  
**Path**: `router_bgp.vrfs.[].default_route_exports.[].address_family`  
**Valid Values**: `evpn`, `vpn-ipv4`, `vpn-ipv6`  
---

### address_family

**Type**: String  
**Path**: `router_segment_security.vrfs.[].segments.[].definition.match_lists.[].address_family`  
**Valid Values**: `ipv4`, `ipv6`  

Indicate which address-family the match list belongs to e.g. ipv4 or ipv6.

---

### address_type

**Type**: String  
**Path**: `hardware_counters.features.[].address_type`  
**Valid Values**: `ipv4`, `ipv6`, `mac`  

Supported only for the following features:
- acl: [ipv4, ipv6, mac] if direction is 'out'
- multicast: [ipv4, ipv6]
- route: [ipv4, ipv6]
This validation IS NOT made by the schemas.


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

### algorithm

**Type**: String  
**Path**: `router_bgp.vrfs.[].evpn_multicast_gateway_dr_election.algorithm`  
**Valid Values**: `hrw`, `modulus`, `preference`  

DR election algorithms:
  hrw: Default selection based on highest random weight.
  modulus: Selection based on VLAN ID modulo number of candidates.
  preference: Selection based on a configured preference value.

---

### algorithm

**Type**: String  
**Path**: `router_isis.authentication.both.key_ids.[].algorithm`  
**Valid Values**: `sha-1`, `sha-224`, `sha-256`, `sha-384`, `sha-512`  
---

### algorithm

**Type**: String  
**Path**: `router_isis.authentication.both.shared_secret.algorithm`  
**Valid Values**: `md5`, `sha-1`, `sha-224`, `sha-256`, `sha-384`, `sha-512`  
---

### algorithm

**Type**: String  
**Path**: `router_isis.authentication.level_1.key_ids.[].algorithm`  
**Valid Values**: `sha-1`, `sha-224`, `sha-256`, `sha-384`, `sha-512`  
---

### algorithm

**Type**: String  
**Path**: `router_isis.authentication.level_1.shared_secret.algorithm`  
**Valid Values**: `md5`, `sha-1`, `sha-224`, `sha-256`, `sha-384`, `sha-512`  
---

### algorithm

**Type**: String  
**Path**: `router_isis.authentication.level_2.key_ids.[].algorithm`  
**Valid Values**: `sha-1`, `sha-224`, `sha-256`, `sha-384`, `sha-512`  
---

### algorithm

**Type**: String  
**Path**: `router_isis.authentication.level_2.shared_secret.algorithm`  
**Valid Values**: `md5`, `sha-1`, `sha-224`, `sha-256`, `sha-384`, `sha-512`  
---

### algorithm

**Type**: String  
**Path**: `vlan_interfaces.[].isis_authentication.both.key_ids.[].algorithm`  
**Valid Values**: `sha-1`, `sha-224`, `sha-256`, `sha-384`, `sha-512`  
---

### algorithm

**Type**: String  
**Path**: `vlan_interfaces.[].isis_authentication.both.shared_secret.algorithm`  
**Valid Values**: `md5`, `sha-1`, `sha-224`, `sha-256`, `sha-384`, `sha-512`  
---

### algorithm

**Type**: String  
**Path**: `vlan_interfaces.[].isis_authentication.level_1.key_ids.[].algorithm`  
**Valid Values**: `sha-1`, `sha-224`, `sha-256`, `sha-384`, `sha-512`  
---

### algorithm

**Type**: String  
**Path**: `vlan_interfaces.[].isis_authentication.level_1.shared_secret.algorithm`  
**Valid Values**: `md5`, `sha-1`, `sha-224`, `sha-256`, `sha-384`, `sha-512`  
---

### algorithm

**Type**: String  
**Path**: `vlan_interfaces.[].isis_authentication.level_2.key_ids.[].algorithm`  
**Valid Values**: `sha-1`, `sha-224`, `sha-256`, `sha-384`, `sha-512`  
---

### algorithm

**Type**: String  
**Path**: `vlan_interfaces.[].isis_authentication.level_2.shared_secret.algorithm`  
**Valid Values**: `md5`, `sha-1`, `sha-224`, `sha-256`, `sha-384`, `sha-512`  
---

### aliases

**Type**: String  
**Path**: `aliases`  

Multi-line string with one or more alias commands.

Example:

```yaml
aliases: |
  alias wr copy running-config startup-config
  alias siib show ip interface brief
```


---

### allocation

**Type**: String  
**Path**: `vlan_internal_order.allocation`  
**Valid Values**: `ascending`, `descending`  
---

### application_override

**Type**: String  
**Path**: `ethernet_interfaces.[].transceiver.application_override`  
**Valid Values**: `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `13`, `14`, `15`, `100gbase-srbd`  

Set CMIS transceiver application.
'100gbase-srbd' should not be used in conjunction with `application_override_lanes`.

---

### application_traffic_recognition

**Type**: Dictionary  
**Path**: `application_traffic_recognition`  

Application traffic recognition configuration.

---

### ASN Notation

**Type**: String  
**Path**: `router_bgp.as_notation`  
**Valid Values**: `asdot`, `asplain`  

BGP AS can be deplayed in the asplain <1-4294967295> or asdot notation "<1-65535>.<0-65535>". This flag indicates which mode is preferred - asplain is the default.

---

### authentication

**Type**: String  
**Path**: `snmp_server.groups.[].authentication`  
**Valid Values**: `auth`, `noauth`, `priv`  
---

### authentication_level

**Type**: String  
**Path**: `snmp_server.hosts.[].users.[].authentication_level`  
**Valid Values**: `auth`, `noauth`, `priv`  
---

### avd_data_validation_mode

**Type**: String  
**Path**: `avd_data_validation_mode`  
**Default**: `error`  
**Valid Values**: `error`, `warning`  

Validation Mode for AVD input data validation.
Input data validation will validate the input variables according to the schema.
During validation, messages will be generated with information about the host(s) and key(s) which failed validation.
"error" will produce error messages and fail the task.
"warning" will produce warning messages.


---

### avd_eos_cli_config_gen_validate_inputs_batch_size

**Type**: Integer  
**Path**: `avd_eos_cli_config_gen_validate_inputs_batch_size`  
**Default**: `10`  

The number of hosts to process in each batch when validating inputs.
Depending on your inventory size and the available resources, you may want to adjust this number.

---

### avd_structured_config_file_format

**Type**: String  
**Path**: `avd_structured_config_file_format`  
**Default**: `yml`  
**Valid Values**: `yml`, `yaml`, `json`  

The file format to use when loading structured configuration files.


---

## C

### cfm

**Type**: Dictionary  
**Path**: `cfm`  

Configure connectivity fault management (CFM).
CFM is a network protocol for monitoring and troubleshooting Ethernet networks.

---

### cipher

**Type**: String  
**Path**: `mac_security.profiles.[].cipher`  
**Valid Values**: `aes128-gcm`, `aes128-gcm-xpn`, `aes256-gcm`, `aes256-gcm-xpn`  
---

### circuit_id_format

**Type**: String  
**Path**: `ip_dhcp_snooping.information_option.circuit_id_format`  
**Valid Values**: `%h:%p`, `%p:%v`  

Required if `circuit_id_type` is set.
- "%h:%p" Hostname and interface name
- "%p:%v" Interface name and VLAN ID

---

### Community Lists (legacy model)

**Type**: List  
**Path**: `community_lists`  
---

### config_comment

**Type**: String  
**Path**: `config_comment`  

Add a comment to provide information about the configuration.
This comment will be rendered at the top of the generated configuration.

---

### config_end

**Type**: Boolean  
**Path**: `config_end`  
**Default**: `False`  

Render `end` at the end of the configuration.

---

### connection

**Type**: String  
**Path**: `ip_security.profiles.[].connection`  
**Valid Values**: `add`, `start`, `route`  

IPsec connection (Initiator/Responder/Dynamic).

---

### console

**Type**: String  
**Path**: `logging.console`  
**Valid Values**: `debugging`, `informational`, `notifications`, `warnings`, `errors`, `critical`, `alerts`, `emergencies`, `disabled`  

Console logging severity level.

---

### Custom Daemons

**Type**: List, items: Dictionary  
**Path**: `daemons`  

This will add a daemon to the eos configuration that is most useful when trying to run OpenConfig clients like ocprometheus.

---

### cvx

**Type**: Dictionary  
**Path**: `cvx`  

CVX server features are not supported on physical switches. See `management_cvx` for client configurations.

---

## D

### daemon_terminattr

**Type**: Dictionary  
**Path**: `daemon_terminattr`  

You can either provide a list of IPs/FQDNs to target on-premise Cloudvision cluster or use DNS name for your Cloudvision as a Service instance.
Streaming to multiple clusters both on-prem and cloud service is supported.

!!! note
    For TerminAttr version recommendation and EOS compatibility matrix, please refer to the latest TerminAttr Release Notes
    which always contain the latest recommended versions and minimum required versions per EOS release.


---

### default

**Type**: String  
**Path**: `platform.sand.multicast_replication.default`  
**Valid Values**: `ingress`, `egress`  
---

### delay_mechanism

**Type**: String  
**Path**: `ethernet_interfaces.[].ptp.delay_mechanism`  
**Valid Values**: `e2e`, `p2p`  
---

### delay_mechanism

**Type**: String  
**Path**: `port_channel_interfaces.[].ptp.delay_mechanism`  
**Valid Values**: `e2e`, `p2p`  
---

### delimiter

**Type**: String  
**Path**: `dot1x.radius_av_pair_username_format.delimiter`  
**Valid Values**: `colon`, `hyphen`, `none`, `period`  

Delimiter to use in MAC address string.

---

### destination_grouping

**Type**: String  
**Path**: `load_balance.cluster.destination_grouping`  
**Valid Values**: `bgp field-set`, `prefix length`, `vtep`  

Perform destination grouping using given setting.

---

### destination_mac_address

**Type**: String  
**Path**: `ethernet_interfaces.[].ptp.profile.g8275_1.destination_mac_address`  
**Valid Values**: `forwardable`, `non-forwardable`  
---

### destination_mac_address

**Type**: String  
**Path**: `port_channel_interfaces.[].ptp.profile.g8275_1.destination_mac_address`  
**Valid Values**: `forwardable`, `non-forwardable`  
---

### destination_ports_match

**Type**: String  
**Path**: `ip_access_lists.[].entries.[].destination_ports_match`  
**Default**: `eq`  
**Valid Values**: `eq`, `gt`, `lt`, `neq`, `range`  
---

### dh_group

**Type**: Integer  
**Path**: `ip_security.ike_policies.[].dh_group`  
**Valid Values**: `1`, `2`, `5`, `14`, `15`, `16`, `17`, `19`, `20`, `21`, `24`  

Diffie-Hellman group for the key exchange.

---

### direction

**Type**: String  
**Path**: `cfm.domains.[].associations.[].direction`  
**Valid Values**: `up`, `down`  

Local maintenance endpoint direction.

---

### direction

**Type**: String  
**Path**: `dps_interfaces.[].tcp_mss_ceiling.direction`  
**Valid Values**: `ingress`, `egress`  

Optional direction ('ingress', 'egress')  for tcp mss ceiling.

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

### direction

**Type**: String  
**Path**: `hardware_counters.features.[].direction`  
**Valid Values**: `in`, `out`, `cpu`  

Most features support only 'in' and 'out'. Some like traffic-policy support 'cpu'.
Some features DO NOT have any direction.
This validation IS NOT made by the schemas.


---

### direction

**Type**: String  
**Path**: `ip_nat.profiles.[].destination.static.[].direction`  
**Valid Values**: `egress`, `ingress`  

Egress or ingress can be the default. This depends on source/destination, EOS version, and hardware platform.
EOS might remove this keyword in the configuration. So, check the configuration on targeted HW/SW.


---

### direction

**Type**: String  
**Path**: `ip_nat.profiles.[].source.static.[].direction`  
**Valid Values**: `egress`, `ingress`  

Egress or ingress can be the default. This depends on source/destination, EOS version, and hardware platform.
EOS might remove this keyword in the configuration. So, check the configuration on targeted HW/SW.


---

### direction

**Type**: String  
**Path**: `monitor_sessions.[].sources.[].direction`  
**Valid Values**: `rx`, `tx`, `both`  
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

### direction

**Type**: String  
**Path**: `router_path_selection.tcp_mss_ceiling.direction`  
**Default**: `ingress`  
**Valid Values**: `ingress`  

Enforce on packets through DPS tunnel for a specific direction.
Only 'ingress' direction is supported.

---

### direction

**Type**: String  
**Path**: `tunnel_interfaces.[].tcp_mss_ceiling.direction`  
**Valid Values**: `ingress`, `egress`  

Optional direction ('ingress', 'egress')  for tcp mss ceiling.


---

### direction

**Type**: String  
**Path**: `vlan_interfaces.[].ip_nat.destination.static.[].direction`  
**Valid Values**: `egress`, `ingress`  

Egress or ingress can be the default. This depends on source/destination, EOS version, and hardware platform.
EOS might remove this keyword in the configuration. So, check the configuration on targeted HW/SW.


---

### direction

**Type**: String  
**Path**: `vlan_interfaces.[].ip_nat.source.static.[].direction`  
**Valid Values**: `egress`, `ingress`  

Egress or ingress can be the default. This depends on source/destination, EOS version, and hardware platform.
EOS might remove this keyword in the configuration. So, check the configuration on targeted HW/SW.


---

### direction_in_action

**Type**: String  
**Path**: `router_bgp.address_family_ipv6_multicast.bgp.missing_policy.direction_in_action`  
**Valid Values**: `deny`, `deny-in-out`, `permit`  
---

### direction_in_action

**Type**: String  
**Path**: `router_bgp.address_family_link_state.bgp.missing_policy.direction_in_action`  
**Valid Values**: `deny`, `deny-in-out`, `permit`  
---

### direction_in_action

**Type**: String  
**Path**: `router_bgp.address_family_link_state.peer_groups.[].missing_policy.direction_in_action`  
**Valid Values**: `deny`, `deny-in-out`, `permit`  
---

### direction_in_action

**Type**: String  
**Path**: `router_bgp.address_family_link_state.neighbors.[].missing_policy.direction_in_action`  
**Valid Values**: `deny`, `deny-in-out`, `permit`  
---

### direction_in_action

**Type**: String  
**Path**: `router_bgp.address_family_flow_spec_ipv4.bgp.missing_policy.direction_in_action`  
**Valid Values**: `deny`, `deny-in-out`, `permit`  
---

### direction_in_action

**Type**: String  
**Path**: `router_bgp.address_family_flow_spec_ipv6.bgp.missing_policy.direction_in_action`  
**Valid Values**: `deny`, `deny-in-out`, `permit`  
---

### direction_in_action

**Type**: String  
**Path**: `router_bgp.vrfs.[].address_family_ipv4.bgp.missing_policy.direction_in_action`  
**Valid Values**: `deny`, `deny-in-out`, `permit`  
---

### direction_in_action

**Type**: String  
**Path**: `router_bgp.vrfs.[].address_family_ipv6.bgp.missing_policy.direction_in_action`  
**Valid Values**: `deny`, `deny-in-out`, `permit`  
---

### direction_in_action

**Type**: String  
**Path**: `router_bgp.vrfs.[].address_family_ipv4_multicast.bgp.missing_policy.direction_in_action`  
**Valid Values**: `deny`, `deny-in-out`, `permit`  
---

### direction_in_action

**Type**: String  
**Path**: `router_bgp.vrfs.[].address_family_ipv6_multicast.bgp.missing_policy.direction_in_action`  
**Valid Values**: `deny`, `deny-in-out`, `permit`  
---

### direction_in_action

**Type**: String  
**Path**: `router_bgp.vrfs.[].address_family_flow_spec_ipv4.bgp.missing_policy.direction_in_action`  
**Valid Values**: `deny`, `deny-in-out`, `permit`  
---

### direction_in_action

**Type**: String  
**Path**: `router_bgp.vrfs.[].address_family_flow_spec_ipv6.bgp.missing_policy.direction_in_action`  
**Valid Values**: `deny`, `deny-in-out`, `permit`  
---

### direction_out_action

**Type**: String  
**Path**: `router_bgp.address_family_ipv6_multicast.bgp.missing_policy.direction_out_action`  
**Valid Values**: `deny`, `deny-in-out`, `permit`  
---

### direction_out_action

**Type**: String  
**Path**: `router_bgp.address_family_link_state.bgp.missing_policy.direction_out_action`  
**Valid Values**: `deny`, `deny-in-out`, `permit`  
---

### direction_out_action

**Type**: String  
**Path**: `router_bgp.address_family_link_state.peer_groups.[].missing_policy.direction_out_action`  
**Valid Values**: `deny`, `deny-in-out`, `permit`  
---

### direction_out_action

**Type**: String  
**Path**: `router_bgp.address_family_link_state.neighbors.[].missing_policy.direction_out_action`  
**Valid Values**: `deny`, `deny-in-out`, `permit`  
---

### direction_out_action

**Type**: String  
**Path**: `router_bgp.address_family_flow_spec_ipv4.bgp.missing_policy.direction_out_action`  
**Valid Values**: `deny`, `deny-in-out`, `permit`  
---

### direction_out_action

**Type**: String  
**Path**: `router_bgp.address_family_flow_spec_ipv6.bgp.missing_policy.direction_out_action`  
**Valid Values**: `deny`, `deny-in-out`, `permit`  
---

### direction_out_action

**Type**: String  
**Path**: `router_bgp.vrfs.[].address_family_ipv4.bgp.missing_policy.direction_out_action`  
**Valid Values**: `deny`, `deny-in-out`, `permit`  
---

### direction_out_action

**Type**: String  
**Path**: `router_bgp.vrfs.[].address_family_ipv6.bgp.missing_policy.direction_out_action`  
**Valid Values**: `deny`, `deny-in-out`, `permit`  
---

### direction_out_action

**Type**: String  
**Path**: `router_bgp.vrfs.[].address_family_ipv4_multicast.bgp.missing_policy.direction_out_action`  
**Valid Values**: `deny`, `deny-in-out`, `permit`  
---

### direction_out_action

**Type**: String  
**Path**: `router_bgp.vrfs.[].address_family_ipv6_multicast.bgp.missing_policy.direction_out_action`  
**Valid Values**: `deny`, `deny-in-out`, `permit`  
---

### direction_out_action

**Type**: String  
**Path**: `router_bgp.vrfs.[].address_family_flow_spec_ipv4.bgp.missing_policy.direction_out_action`  
**Valid Values**: `deny`, `deny-in-out`, `permit`  
---

### direction_out_action

**Type**: String  
**Path**: `router_bgp.vrfs.[].address_family_flow_spec_ipv6.bgp.missing_policy.direction_out_action`  
**Valid Values**: `deny`, `deny-in-out`, `permit`  
---

### dns_domain

**Type**: String  
**Path**: `dns_domain`  

Domain Name.

---

### domain

**Type**: String  
**Path**: `router_bgp.vlan_aware_bundles.[].rd_evpn_domain.domain`  
**Valid Values**: `remote`, `all`  
---

### domain

**Type**: String  
**Path**: `router_bgp.vlan_aware_bundles.[].route_targets.import_evpn_domains.[].domain`  
**Valid Values**: `remote`, `all`  
---

### domain

**Type**: String  
**Path**: `router_bgp.vlan_aware_bundles.[].route_targets.export_evpn_domains.[].domain`  
**Valid Values**: `remote`, `all`  
---

### domain

**Type**: String  
**Path**: `router_bgp.vlan_aware_bundles.[].route_targets.import_export_evpn_domains.[].domain`  
**Valid Values**: `remote`, `all`  
---

### domain

**Type**: String  
**Path**: `router_bgp.vlans.[].rd_evpn_domain.domain`  
**Valid Values**: `remote`, `all`  
---

### domain

**Type**: String  
**Path**: `router_bgp.vlans.[].route_targets.import_evpn_domains.[].domain`  
**Valid Values**: `remote`, `all`  
---

### domain

**Type**: String  
**Path**: `router_bgp.vlans.[].route_targets.export_evpn_domains.[].domain`  
**Valid Values**: `remote`, `all`  
---

### domain

**Type**: String  
**Path**: `router_bgp.vlans.[].route_targets.import_export_evpn_domains.[].domain`  
**Valid Values**: `remote`, `all`  
---

### domain

**Type**: String  
**Path**: `router_bgp.address_family_evpn.evpn_ethernet_segment.[].domain`  
**Valid Values**: `all`, `local`, `remote`  
---

### domain_list

**Type**: List, items: String  
**Path**: `domain_list`  

Search list of DNS domains.

---

### dot1q_dzgre_source

**Type**: String  
**Path**: `ethernet_interfaces.[].switchport.tool.identity.dot1q_dzgre_source`  
**Valid Values**: `policy`, `port`  
---

### dot1q_dzgre_source

**Type**: String  
**Path**: `port_channel_interfaces.[].switchport.tool.identity.dot1q_dzgre_source`  
**Valid Values**: `policy`, `port`  
---

### dscp

**Type**: String  
**Path**: `mpls.tunnel.termination.model.dscp`  
**Valid Values**: `pipe`, `uniform`  

The DSCP model `uniform` is supported only on specific hardware platforms.

---

### dscp

**Type**: String  
**Path**: `mpls.tunnel.termination.php_model.dscp`  
**Valid Values**: `pipe`, `uniform`  

The DSCP model `uniform` is supported only on specific hardware platforms.

---

## E

### eap_method

**Type**: String  
**Path**: `dot1x.supplicant.profiles.[].eap_method`  
**Valid Values**: `fast`, `tls`  

Extensible Authentication Protocol method:
  - EAP Flexible Authentication via Secure Tunneling.
  - EAP with Transport Layer Security.

---

### eap_response

**Type**: String  
**Path**: `dot1x.aaa.unresponsive.eap_response`  
**Valid Values**: `success`, `disabled`  

EAP response to send.

---

### eap_response

**Type**: String  
**Path**: `ethernet_interfaces.[].dot1x.aaa.unresponsive.eap_response`  
**Valid Values**: `success`, `disabled`  

EAP response to send. EOS default is `success`.

---

### ecn

**Type**: String  
**Path**: `class_maps.qos.[].ecn`  
**Valid Values**: `ce`, `ect`, `ect-ce`, `non-ect`  

Match packets based on the ECN value.
Accepted values:
  - non-ect (matches 00).
  - ect (matches 01 an 10).
  - ce (matches 11).
  - ect-ce (matches 01, 10 and 11).

---

### empty_passwords

**Type**: String  
**Path**: `management_ssh.authentication.empty_passwords`  
**Valid Values**: `auto`, `deny`, `permit`  

Permit or deny empty passwords for SSH authentication.

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

### encapsulation

**Type**: String  
**Path**: `router_bgp.address_family_evpn.neighbor_default.encapsulation`  
**Valid Values**: `vxlan`, `mpls`, `path-selection`  

Transport encapsulation for neighbor.

---

### encapsulation

**Type**: String  
**Path**: `router_bgp.address_family_evpn.neighbors.[].encapsulation`  
**Valid Values**: `vxlan`, `mpls`, `path-selection`  

Transport encapsulation for the neighbor.

---

### encapsulation

**Type**: String  
**Path**: `router_bgp.address_family_evpn.peer_groups.[].encapsulation`  
**Valid Values**: `vxlan`, `mpls`, `path-selection`  

Transport encapsulation for the peer-group.

---

### encryption

**Type**: String  
**Path**: `ip_security.ike_policies.[].encryption`  
**Valid Values**: `3des`, `aes128`, `aes256`  

IKE encryption algorithm.

---

### encryption

**Type**: String  
**Path**: `ip_security.sa_policies.[].esp.encryption`  
**Valid Values**: `disabled`, `aes128`, `aes128gcm128`, `aes128gcm64`, `aes256`, `aes256gcm128`, `3des`  
---

### environment

**Type**: String  
**Path**: `metadata.digital_twin.environment`  
**Valid Values**: `act`  

Targeted Digital Twin environment.

---

### eos_cli

**Type**: String  
**Path**: `eos_cli`  

Multiline string with EOS CLI rendered directly on the root level of the final EOS configuration.

---

### eth_type

**Type**: String  
**Path**: `port_channel.load_balance_trident_udf.[].eth_type`  
**Valid Values**: `ipv4`, `ipv6`  

Ethernet type in the port channel hash.

---

### event_handlers

**Type**: List, items: Dictionary  
**Path**: `event_handlers`  

Gives the ability to monitor and react to Syslog messages.
Event Handlers provide a powerful and flexible tool that can be used to apply self-healing actions,
customize the system behavior, and implement workarounds to problems discovered in the field.


---

### explicit_null

**Type**: String  
**Path**: `router_traffic_engineering.segment_routing.policy_endpoints.[].colors.[].path_group.[].explicit_null`  
**Valid Values**: `ipv4`, `ipv6`, `ipv4 ipv6`, `none`  
---

### Extensibility with Custom Templates

**Type**: List, items: String  
**Path**: `custom_templates`  

- Custom templates can be added below the playbook directory.
- If a location above the directory is desired, a symbolic link can be used.
- Example under the `playbooks` directory create symbolic link with the following command:

  ```bash
  ln -s ../../shared_repo/custom_avd_templates/ ./custom_avd_templates
  ```

- The output will be rendered at the end of the configuration.
- The order of custom templates in the list can be important if they overlap.
- It is recommended to use a `!` delimiter at the top of each custom template.

Add `custom_templates` to group/host variables:


---

## F

### facility

**Type**: String  
**Path**: `logging.facility`  
**Valid Values**: `auth`, `cron`, `daemon`, `kern`, `local0`, `local1`, `local2`, `local3`, `local4`, `local5`, `local6`, `local7`, `lpr`, `mail`, `news`, `sys9`, `sys10`, `sys11`, `sys12`, `sys13`, `sys14`, `syslog`, `user`, `uucp`  
---

### fcs_error

**Type**: String  
**Path**: `tap_aggregation.mac.fcs_error`  
**Valid Values**: `correct`, `discard`, `pass-through`  
---

### flow_assignment

**Type**: String  
**Path**: `router_path_selection.path_groups.[].flow_assignment`  
**Valid Values**: `lan`  

Flow assignment `lan` can not be configured in a path group with dynamic peers.

---

### format

**Type**: String  
**Path**: `flow_tracking.mirror_on_drop.trackers.[].exporters.[].format`  
**Valid Values**: `sflow`, `drop-report`  

Configure flow export format. Valid values are platform dependent.

---

### format

**Type**: String  
**Path**: `tap_aggregation.mac.timestamp.header.format`  
**Valid Values**: `48-bit`, `64-bit`  
---

### forwarding_type

**Type**: String  
**Path**: `load_balance.cluster.forwarding_type`  
**Valid Values**: `bridged encapsulation vxlan ipv4`, `routed ipv4`  
---

### frequency_unit

**Type**: String  
**Path**: `ethernet_interfaces.[].transceiver.frequency_unit`  
**Valid Values**: `ghz`  

Unit of Transceiver Laser Frequency.

---

## G

### Global 802.1x Authentication

**Type**: Dictionary  
**Path**: `dot1x`  
---

## H

### Hardware TCAM Profiles

**Type**: Dictionary  
**Path**: `tcam_profile`  
---

### hash

**Type**: String  
**Path**: `management_defaults.secret.hash`  
**Valid Values**: `md5`, `sha512`  
---

### hash_algorithm

**Type**: String  
**Path**: `boot.secret.hash_algorithm`  
**Default**: `sha512`  
**Valid Values**: `md5`, `sha512`  
---

### hash_algorithm

**Type**: String  
**Path**: `enable_password.hash_algorithm`  
**Valid Values**: `md5`, `sha512`  
---

### hash_algorithm

**Type**: String  
**Path**: `ethernet_interfaces.[].ospf_message_digest_keys.[].hash_algorithm`  
**Valid Values**: `md5`, `sha1`, `sha256`, `sha384`, `sha512`  
---

### hash_algorithm

**Type**: String  
**Path**: `ntp.authentication_keys.[].hash_algorithm`  
**Valid Values**: `md5`, `sha1`  
---

### hash_algorithm

**Type**: String  
**Path**: `port_channel_interfaces.[].ospf_message_digest_keys.[].hash_algorithm`  
**Valid Values**: `md5`, `sha1`, `sha256`, `sha384`, `sha512`  
---

### hash_algorithm

**Type**: String  
**Path**: `router_bgp.peer_groups.[].shared_secret.hash_algorithm`  
**Valid Values**: `aes-128-cmac-96`, `hmac-sha-256`, `hmac-sha1-96`  

Note: Algorithm hmac-sha-256 requires EOS version 4.31.1F and above.

---

### hash_algorithm

**Type**: String  
**Path**: `router_bgp.neighbors.[].shared_secret.hash_algorithm`  
**Valid Values**: `aes-128-cmac-96`, `hmac-sha-256`, `hmac-sha1-96`  

Note: Algorithm hmac-sha-256 requires EOS version 4.31.1F and above.

---

### hash_algorithm

**Type**: String  
**Path**: `vlan_interfaces.[].ospf_message_digest_keys.[].hash_algorithm`  
**Valid Values**: `md5`, `sha1`, `sha256`, `sha384`, `sha512`  
---

### header

**Type**: String  
**Path**: `port_channel.load_balance_trident_udf.[].header`  
**Valid Values**: `inner_l3`, `inner_l4`, `outer_l2`, `outer_l3`, `outer_l4`  
---

### higher_rate_burst_size_unit

**Type**: String  
**Path**: `policy_maps.qos.[].classes.[].police.higher_rate_burst_size_unit`  
**Default**: `bytes`  
**Valid Values**: `bytes`, `kbytes`, `mbytes`, `packets`  
---

### higher_rate_unit

**Type**: String  
**Path**: `policy_maps.qos.[].classes.[].police.higher_rate_unit`  
**Default**: `bps`  
**Valid Values**: `bps`, `kbps`, `mbps`, `pps`  
---

### host_proxy_match_mroute

**Type**: String  
**Path**: `router_igmp.host_proxy_match_mroute`  
**Valid Values**: `all`, `iif`  

Specify conditions for sending IGMP joins for host-proxy.
'iif' will enable igmp host-proxy to work in iif aware.
'all' will enable igmp host-proxy to work in iif unaware mode (EOS default).


---

### host_proxy_match_mroute

**Type**: String  
**Path**: `router_igmp.vrfs.[].host_proxy_match_mroute`  
**Valid Values**: `all`, `iif`  

Specify conditions for sending IGMP joins for host-proxy.
'iif' will enable igmp host-proxy to work in iif aware.
'all' will enable igmp host-proxy to work in iif unaware mode (EOS default).


---

### hostname

**Type**: String  
**Path**: `logging.format.hostname`  
**Valid Values**: `fqdn`, `ipv4`  

Hostname format in syslogs. For hostname _only_, remove the line. (default EOS CLI behaviour).

---

## I

### import_match_failure_action

**Type**: String  
**Path**: `router_bgp.address_family_evpn.route.import_match_failure_action`  
**Valid Values**: `discard`  
---

### import_match_failure_action

**Type**: String  
**Path**: `router_bgp.address_family_vpn_ipv4.route.import_match_failure_action`  
**Valid Values**: `discard`  
---

### import_match_failure_action

**Type**: String  
**Path**: `router_bgp.address_family_vpn_ipv6.route.import_match_failure_action`  
**Valid Values**: `discard`  
---

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

### integrity

**Type**: String  
**Path**: `ip_security.ike_policies.[].integrity`  
**Valid Values**: `md5`, `sha1`, `sha256`, `sha384`, `sha512`  

Integrity algorithm.

---

### integrity

**Type**: String  
**Path**: `ip_security.sa_policies.[].esp.integrity`  
**Valid Values**: `disabled`, `sha1`, `sha256`, `sha384`, `sha512`, `md5`  
---

### interval_unit

**Type**: String  
**Path**: `router_isis.spf_interval.interval_unit`  
**Valid Values**: `seconds`, `milliseconds`  

If interval unit is not defined EOS takes `seconds` by default.

---

### IP Community Lists

**Type**: List, items: Dictionary  
**Path**: `ip_community_lists`  
---

### IP Extended Access-Lists (improved model)

**Type**: List, items: Dictionary  
**Path**: `ip_access_lists`  
---

### IP Extended Access-Lists (legacy model)

**Type**: List, items: Dictionary  
**Path**: `access_lists`  
---

### IP Extended Community Lists

**Type**: List, items: Dictionary  
**Path**: `ip_extcommunity_lists`  
---

### IP Extended Community Lists RegExp

**Type**: List, items: Dictionary  
**Path**: `ip_extcommunity_lists_regexp`  
---

### IP Large Community Lists

**Type**: List, items: Dictionary  
**Path**: `ip_large_community_lists`  

A BGP large-community access list filters prefixes based on their BGP large community values. Multiple large-community lists with the same name may be specified.


---

### IP Tacacs Source Interfaces

**Type**: List, items: Dictionary  
**Path**: `ip_tacacs_source_interfaces`  
---

### ip_access_lists_max_entries

**Type**: Integer  
**Path**: `ip_access_lists_max_entries`  

Limit ACL entries defined under the `ip_access_lists`.

---

### ip_ospf_router_id_output_format_hostnames

**Type**: Boolean  
**Path**: `ip_ospf_router_id_output_format_hostnames`  

Display DNS-resolved router names for OSPF router IDs.

---

### ip_verify_unicast_source_reachable_via

**Type**: String  
**Path**: `ethernet_interfaces.[].ip_verify_unicast_source_reachable_via`  
**Valid Values**: `any`, `rx`  
---

### ip_verify_unicast_source_reachable_via

**Type**: String  
**Path**: `port_channel_interfaces.[].ip_verify_unicast_source_reachable_via`  
**Valid Values**: `any`, `rx`  
---

### ip_verify_unicast_source_reachable_via

**Type**: String  
**Path**: `vlan_interfaces.[].ip_verify_unicast_source_reachable_via`  
**Valid Values**: `any`, `rx`  
---

### ip_virtual_router_mac_address

**Type**: String  
**Path**: `ip_virtual_router_mac_address`  

MAC address (hh:hh:hh:hh:hh:hh).

---

### ip_virtual_router_mac_address_advertisement_interval

**Type**: Integer  
**Path**: `ip_virtual_router_mac_address_advertisement_interval`  

Advertisement interval in seconds.

---

### ip_virtual_router_mac_address_mlag_peer

**Type**: Boolean  
**Path**: `ip_virtual_router_mac_address_mlag_peer`  

Enable MLAG peer gateway.

---

### IPv6 Extended Access-Lists

**Type**: List, items: Dictionary  
**Path**: `ipv6_access_lists`  
---

### IPv6 router OSPF Configuration

**Type**: Dictionary  
**Path**: `ipv6_router_ospf`  
---

### IS Type

**Type**: String  
**Path**: `router_isis.is_type`  
**Valid Values**: `level-1`, `level-1-2`, `level-2`  
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

### isis_circuit_type

**Type**: String  
**Path**: `port_channel_interfaces.[].isis_circuit_type`  
**Valid Values**: `level-1-2`, `level-1`, `level-2`  
---

### isis_level

**Type**: String  
**Path**: `ipv6_router_ospf.process_ids.[].redistribute.isis.isis_level`  
**Valid Values**: `level-1`, `level-2`, `level-1-2`  

Redistribute IS-IS route level.

---

### isis_level

**Type**: String  
**Path**: `router_bgp.redistribute.isis.isis_level`  
**Valid Values**: `level-1`, `level-2`, `level-1-2`  

Redistribute IS-IS route level.

---

### isis_level

**Type**: String  
**Path**: `router_bgp.address_family_ipv4.redistribute.isis.isis_level`  
**Valid Values**: `level-1`, `level-2`, `level-1-2`  

Redistribute IS-IS route level.

---

### isis_level

**Type**: String  
**Path**: `router_bgp.address_family_ipv4_multicast.redistribute.isis.isis_level`  
**Valid Values**: `level-1`, `level-2`, `level-1-2`  

Redistribute IS-IS route level.

---

### isis_level

**Type**: String  
**Path**: `router_bgp.address_family_ipv6.redistribute.isis.isis_level`  
**Valid Values**: `level-1`, `level-2`, `level-1-2`  

Redistribute IS-IS route level.

---

### isis_level

**Type**: String  
**Path**: `router_bgp.address_family_ipv6_multicast.redistribute.isis.isis_level`  
**Valid Values**: `level-1`, `level-2`, `level-1-2`  

Redistribute IS-IS route level.

---

### isis_level

**Type**: String  
**Path**: `router_bgp.vrfs.[].redistribute.isis.isis_level`  
**Valid Values**: `level-1`, `level-2`, `level-1-2`  

Redistribute IS-IS route level.

---

### isis_level

**Type**: String  
**Path**: `router_bgp.vrfs.[].address_family_ipv4.redistribute.isis.isis_level`  
**Valid Values**: `level-1`, `level-2`, `level-1-2`  

Redistribute IS-IS route level.

---

### isis_level

**Type**: String  
**Path**: `router_bgp.vrfs.[].address_family_ipv6.redistribute.isis.isis_level`  
**Valid Values**: `level-1`, `level-2`, `level-1-2`  

Redistribute IS-IS route level.

---

### isis_level

**Type**: String  
**Path**: `router_bgp.vrfs.[].address_family_ipv4_multicast.redistribute.isis.isis_level`  
**Valid Values**: `level-1`, `level-2`, `level-1-2`  

Redistribute IS-IS route level.

---

### isis_level

**Type**: String  
**Path**: `router_bgp.vrfs.[].address_family_ipv6_multicast.redistribute.isis.isis_level`  
**Valid Values**: `level-1`, `level-2`, `level-1-2`  

Redistribute IS-IS route level.

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

### key_type

**Type**: String  
**Path**: `ntp.authentication_keys.[].key_type`  
**Valid Values**: `0`, `7`, `8a`  
---

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

### key_type

**Type**: String  
**Path**: `router_isis.authentication.both.key_type`  
**Valid Values**: `0`, `7`, `8a`  

Configure authentication key type.

---

### key_type

**Type**: String  
**Path**: `router_isis.authentication.both.key_ids.[].key_type`  
**Valid Values**: `0`, `7`, `8a`  

Configure authentication key type.

---

### key_type

**Type**: String  
**Path**: `router_isis.authentication.level_1.key_type`  
**Valid Values**: `0`, `7`, `8a`  

Configure authentication key type.

---

### key_type

**Type**: String  
**Path**: `router_isis.authentication.level_1.key_ids.[].key_type`  
**Valid Values**: `0`, `7`, `8a`  

Configure authentication key type.

---

### key_type

**Type**: String  
**Path**: `router_isis.authentication.level_2.key_type`  
**Valid Values**: `0`, `7`, `8a`  

Configure authentication key type.

---

### key_type

**Type**: String  
**Path**: `router_isis.authentication.level_2.key_ids.[].key_type`  
**Valid Values**: `0`, `7`, `8a`  

Configure authentication key type.

---

### key_type

**Type**: String  
**Path**: `tacacs_servers.hosts.[].key_type`  
**Default**: `7`  
**Valid Values**: `0`, `7`, `8a`  
---

### key_type

**Type**: String  
**Path**: `vlan_interfaces.[].ospf_message_digest_keys.[].key_type`  
**Default**: `7`  
**Valid Values**: `7`, `8a`  

Authentication key type.

---

### key_type

**Type**: String  
**Path**: `vlan_interfaces.[].isis_authentication.both.key_type`  
**Valid Values**: `0`, `7`, `8a`  

Configure authentication key type.

---

### key_type

**Type**: String  
**Path**: `vlan_interfaces.[].isis_authentication.both.key_ids.[].key_type`  
**Valid Values**: `0`, `7`, `8a`  

Configure authentication key type.

---

### key_type

**Type**: String  
**Path**: `vlan_interfaces.[].isis_authentication.level_1.key_type`  
**Valid Values**: `0`, `7`, `8a`  

Configure authentication key type.

---

### key_type

**Type**: String  
**Path**: `vlan_interfaces.[].isis_authentication.level_1.key_ids.[].key_type`  
**Valid Values**: `0`, `7`, `8a`  

Configure authentication key type.

---

### key_type

**Type**: String  
**Path**: `vlan_interfaces.[].isis_authentication.level_2.key_type`  
**Valid Values**: `0`, `7`, `8a`  

Configure authentication key type.

---

### key_type

**Type**: String  
**Path**: `vlan_interfaces.[].isis_authentication.level_2.key_ids.[].key_type`  
**Valid Values**: `0`, `7`, `8a`  

Configure authentication key type.

---

### key_type

**Type**: String  
**Path**: `vlan_interfaces.[].vrrp_ids.[].peer_authentication.key_type`  
**Valid Values**: `0`, `7`, `8a`  

Authentication key type.

---

## L

### label_local_termination

**Type**: String  
**Path**: `mpls.rsvp.label_local_termination`  
**Valid Values**: `implicit-null`, `explicit-null`  

Local termination label to be advertised.

---

### label_local_termination

**Type**: String  
**Path**: `router_bgp.address_family_ipv4_labeled_unicast.label_local_termination`  
**Valid Values**: `explicit-null`, `implicit-null`  
---

### lacp

**Type**: Dictionary  
**Path**: `lacp`  

Set Link Aggregation Control Protocol (LACP) parameters.

---

### lacp_fallback_mode

**Type**: String  
**Path**: `port_channel_interfaces.[].lacp_fallback_mode`  
**Valid Values**: `individual`, `static`  
---

### level

**Type**: String  
**Path**: `logging.buffered.level`  
**Valid Values**: `alerts`, `critical`, `debugging`, `emergencies`, `errors`, `informational`, `notifications`, `warnings`, `disabled`  

Buffer logging severity level.

---

### level

**Type**: String  
**Path**: `logging.synchronous.level`  
**Default**: `critical`  
**Valid Values**: `alerts`, `all`, `critical`, `debugging`, `emergencies`, `errors`, `informational`, `notifications`, `warnings`, `disabled`  

Synchronous logging severity level.

---

### level

**Type**: String  
**Path**: `router_isis.address_family_ipv4.fast_reroute_ti_lfa.level`  
**Valid Values**: `level-1`, `level-2`  
---

### level

**Type**: String  
**Path**: `router_isis.address_family_ipv6.fast_reroute_ti_lfa.level`  
**Valid Values**: `level-1`, `level-2`  

Optional, default is to protect all levels.

---

### load_balance

**Type**: Dictionary  
**Path**: `load_balance`  

Configuration for load balancing behavior across port-channels and ECMP paths.

---

## M

### MAC Security (MACsec)

**Type**: Dictionary  
**Path**: `mac_security`  
---

### mac_string_case

**Type**: String  
**Path**: `dot1x.radius_av_pair_username_format.mac_string_case`  
**Valid Values**: `lowercase`, `uppercase`  

MAC address string in lowercase/uppercase.

---

### mac_timestamp

**Type**: String  
**Path**: `ethernet_interfaces.[].mac_timestamp`  
**Valid Values**: `before-fcs`, `replace-fcs`, `header`  

header: Insert timestamp in ethernet header. Supported on platforms like 7500E/R and 7280E/R.
before-fcs: Insert timestamp before fcs field. Supported on platforms like 7150.
replace-fcs: Replace fcs field with timestamp.

---

### Maintenance Interface Groups

**Type**: List, items: Dictionary  
**Path**: `interface_groups`  
---

### Maintenance Mode

**Type**: Dictionary  
**Path**: `maintenance`  
---

### Match Lists

**Type**: Dictionary  
**Path**: `match_list_input`  
---

### mdb_profile

**Type**: String  
**Path**: `platform.sand.mdb_profile`  
**Valid Values**: `balanced`, `balanced-xl`, `l3`, `l3-xl`, `l3-xxl`, `l3-xxxl`  

Sand platforms MDB Profile configuration. Note: l3-xxxl does not support MLAG.

---

### mechanism

**Type**: String  
**Path**: `hardware.access_list.mechanism`  
**Valid Values**: `algomatch`, `none`, `tcam`  
---

### metadata

**Type**: Dictionary  
**Path**: `metadata`  

The data under `metadata` is used for documentation, validation or integration purposes.
It will not affect the generated EOS configuration.

---

### method

**Type**: String  
**Path**: `aaa_accounting.exec.console.methods.[].method`  
**Valid Values**: `logging`, `group`  
---

### method

**Type**: String  
**Path**: `aaa_accounting.exec.default.methods.[].method`  
**Valid Values**: `logging`, `group`  
---

### method

**Type**: String  
**Path**: `aaa_accounting.system.default.methods.[].method`  
**Valid Values**: `logging`, `group`  
---

### method

**Type**: String  
**Path**: `aaa_accounting.dot1x.default.methods.[].method`  
**Valid Values**: `logging`, `group`  
---

### method

**Type**: String  
**Path**: `aaa_accounting.commands.console.[].methods.[].method`  
**Valid Values**: `logging`, `group`  
---

### method

**Type**: String  
**Path**: `aaa_accounting.commands.default.[].methods.[].method`  
**Valid Values**: `logging`, `group`  
---

### method

**Type**: String  
**Path**: `daemon_terminattr.clusters.[].cvauth.method`  
**Valid Values**: `token`, `token-secure`, `key`, `certs`  
---

### method

**Type**: String  
**Path**: `daemon_terminattr.cvauth.method`  
**Valid Values**: `token`, `token-secure`, `key`, `certs`  
---

### method

**Type**: String  
**Path**: `monitor_server_radius.probe.method`  
**Valid Values**: `status-server`, `access-request`  

Method used to probe the server. `status-server` is the EOS default method.

---

### method

**Type**: String  
**Path**: `mpls.rsvp.refresh.method`  
**Valid Values**: `bundled`, `explicit`  

Neighbor refresh mechanism.
bundled: Refresh states using message identifier lists.
explicit: Send each message individually.

---

### metric

**Type**: String  
**Path**: `router_traffic_engineering.flex_algos.[].metric`  
**Valid Values**: `0`, `1`, `2`, `igp-metric`, `min-delay`, `te-metric`  

Metric can be specified as an integer or named type, 0 = igp-metric, 1 = min-delay, 2 = te-metric. Device CLI will show the name regardless.

---

### metric_type

**Type**: Integer  
**Path**: `router_ospf.process_ids.[].default_information_originate.metric_type`  
**Valid Values**: `1`, `2`  

OSPF metric type for default route.

---

### metric_type

**Type**: Integer  
**Path**: `router_ospf.process_ids.[].areas.[].default_information_originate.metric_type`  
**Valid Values**: `1`, `2`  

OSPF metric type for default route.

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

### mode

**Type**: String  
**Path**: `ip_security.profiles.[].mode`  
**Valid Values**: `transport`, `tunnel`  

Ipsec mode type.

---

### mode

**Type**: String  
**Path**: `mac_security.profiles.[].l2_protocols.ethernet_flow_control.mode`  
**Valid Values**: `encrypt`, `bypass`  
---

### mode

**Type**: String  
**Path**: `mac_security.profiles.[].l2_protocols.lldp.mode`  
**Valid Values**: `bypass`, `bypass unauthorized`  
---

### mode

**Type**: String  
**Path**: `mpls.rsvp.fast_reroute.mode`  
**Valid Values**: `link-protection`, `node-protection`, `none`  

Fast reroute mode.
link-protection: Protect against failure of the next link.
node-protection: Protect against failure of the next node.
none: Disable fast reroute.

---

### mode

**Type**: String  
**Path**: `platform.sfe.interface.profiles.[].interfaces.[].rx_queue.mode`  
**Valid Values**: `shared`, `exclusive`  

Mode applicable to the workers. Default mode is 'shared'.

---

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

### mode

**Type**: String  
**Path**: `ptp.mode`  
**Valid Values**: `boundary`, `disabled`, `e2etransparent`, `gptp`, `ordinarymaster`, `p2ptransparent`  
---

### mode

**Type**: String  
**Path**: `router_isis.authentication.both.mode`  
**Valid Values**: `md5`, `sha`, `text`, `shared-secret`  

Authentication mode.

---

### mode

**Type**: String  
**Path**: `router_isis.authentication.level_1.mode`  
**Valid Values**: `md5`, `sha`, `text`, `shared-secret`  

Authentication mode.

---

### mode

**Type**: String  
**Path**: `router_isis.authentication.level_2.mode`  
**Valid Values**: `md5`, `sha`, `text`, `shared-secret`  

Authentication mode.

---

### mode

**Type**: String  
**Path**: `router_isis.address_family_ipv4.fast_reroute_ti_lfa.mode`  
**Valid Values**: `link-protection`, `node-protection`  
---

### mode

**Type**: String  
**Path**: `router_isis.address_family_ipv6.fast_reroute_ti_lfa.mode`  
**Valid Values**: `link-protection`, `node-protection`  
---

### mode

**Type**: String  
**Path**: `spanning_tree.mode`  
**Valid Values**: `mstp`, `rstp`, `rapid-pvst`, `none`  
---

### mode

**Type**: String  
**Path**: `switchport_default.mode`  
**Valid Values**: `routed`, `access`  
---

### mode

**Type**: String  
**Path**: `vlan_interfaces.[].isis_authentication.both.mode`  
**Valid Values**: `md5`, `sha`, `text`, `shared-secret`  

Authentication mode.

---

### mode

**Type**: String  
**Path**: `vlan_interfaces.[].isis_authentication.level_1.mode`  
**Valid Values**: `md5`, `sha`, `text`, `shared-secret`  

Authentication mode.

---

### mode

**Type**: String  
**Path**: `vlan_interfaces.[].isis_authentication.level_2.mode`  
**Valid Values**: `md5`, `sha`, `text`, `shared-secret`  

Authentication mode.

---

### mode

**Type**: String  
**Path**: `vlan_interfaces.[].vrrp_ids.[].peer_authentication.mode`  
**Valid Values**: `text`, `ietf-md5`  

Authentication mode.

---

### monitor

**Type**: String  
**Path**: `logging.monitor`  
**Valid Values**: `debugging`, `informational`, `notifications`, `warnings`, `errors`, `critical`, `alerts`, `emergencies`, `disabled`  

Monitor logging severity level.

---

### monitor_layer1

**Type**: Dictionary  
**Path**: `monitor_layer1`  

Enable SYSLOG messages on transceiver SMBus communication failures.

---

### monitor_server_radius

**Type**: Dictionary  
**Path**: `monitor_server_radius`  

Settings to monitor radius servers.

---

### Multi-Chassis Link Aggregation (MLAG) Configuration

**Type**: Dictionary  
**Path**: `mlag_configuration`  
---

### multipath

**Type**: String  
**Path**: `router_multicast.ipv4.multipath`  
**Valid Values**: `none`, `deterministic`, `deterministic color`, `deterministic router-id`  
---

## N

### name

**Type**: String  
**Path**: `dps_interfaces.[].name`  
**Valid Values**: `Dps1`  

"Dps1" is currently the only supported interface.

---

### name

**Type**: String  
**Path**: `errdisable.recovery.causes.[].name`  
**Valid Values**: `acl`, `arp-inspection`, `bpduguard`, `dot1x`, `dot1x-coa`, `dot1x-phone-classification`, `dot1x-session-replace`, `error-correction-encoding`, `hardware-speed-group`, `hitless-reload-down`, `interface-speed`, `internal-error`, `lacp-rate-limit`, `link-flap`, `no-internal-vlan`, `port-breakout`, `portchannelguard`, `portsec`, `speed-misconfigured`, `storm-control`, `stuck-queue`, `switchcard-unreachable`, `tap-port-init`, `tapagg`, `transceiver-adapter`, `uplink-failure-detection`, `xcvr-misconfigured`, `xcvr-overheat`, `xcvr-power-unsupported`, `xcvr-unsupported`  

Specifies the type of event that can trigger recovery actions.
The list of supported causes depends on both the EOS version and the hardware platform.

---

### name

**Type**: String  
**Path**: `hardware_counters.features.[].name`  
**Valid Values**: `acl`, `decap-group`, `directflow`, `ecn`, `flow-spec`, `gre tunnel interface`, `ip`, `mpls interface`, `mpls lfib`, `mpls tunnel`, `multicast`, `nexthop`, `pbr`, `pdp`, `policing interface`, `qos`, `qos dual-rate-policer`, `route`, `routed-port`, `segment-security`, `subinterface`, `tapagg`, `traffic-class`, `traffic-policy`, `traffic-policy vlan-interface`, `vlan`, `vlan-interface`, `vni decap`, `vni encap`, `vtep decap`, `vtep encap`  
---

### name

**Type**: String  
**Path**: `l2_protocol.forwarding_profiles.[].protocols.[].name`  
**Valid Values**: `bfd per-link rfc-7130`, `e-lmi`, `isis`, `lacp`, `lldp`, `macsec`, `pause`, `stp`  
---

### name

**Type**: String  
**Path**: `lldp.tlvs.[].name`  
**Valid Values**: `link-aggregation`, `management-address`, `max-frame-size`, `med`, `port-description`, `port-vlan`, `power-via-mdi`, `system-capabilities`, `system-description`, `system-name`, `vlan-name`  
---

### nat_type

**Type**: String  
**Path**: `ethernet_interfaces.[].ip_nat.source.dynamic.[].nat_type`  
**Valid Values**: `overload`, `pool`, `pool-address-only`, `pool-full-cone`  
---

### nat_type

**Type**: String  
**Path**: `ip_nat.profiles.[].source.dynamic.[].nat_type`  
**Valid Values**: `overload`, `pool`, `pool-address-only`, `pool-full-cone`  
---

### nat_type

**Type**: String  
**Path**: `port_channel_interfaces.[].ip_nat.source.dynamic.[].nat_type`  
**Valid Values**: `overload`, `pool`, `pool-address-only`, `pool-full-cone`  
---

### nat_type

**Type**: String  
**Path**: `vlan_interfaces.[].ip_nat.source.dynamic.[].nat_type`  
**Valid Values**: `overload`, `pool`, `pool-address-only`, `pool-full-cone`  
---

### notification_timestamp

**Type**: String  
**Path**: `management_api_gnmi.transport.grpc.[].notification_timestamp`  
**Valid Values**: `send-time`, `last-change-time`  

Per the gNMI specification, the default timestamp field of a notification message is set to be
the time at which the value of the underlying data source changes or when the reported event takes place.
In order to facilitate integration in legacy environments oriented around polling style operations,
an option to support overriding the timestamp field to the send-time is available from EOS 4.27.0F.


---

### nssa_type

**Type**: Integer  
**Path**: `router_bgp.redistribute.ospf.match_nssa_external.nssa_type`  
**Valid Values**: `1`, `2`  

NSSA External Type Number.

---

### nssa_type

**Type**: Integer  
**Path**: `router_bgp.redistribute.ospfv3.match_nssa_external.nssa_type`  
**Valid Values**: `1`, `2`  

NSSA External Type Number.

---

### nssa_type

**Type**: Integer  
**Path**: `router_bgp.address_family_ipv4.redistribute.ospf.match_nssa_external.nssa_type`  
**Valid Values**: `1`, `2`  

NSSA External Type Number.

---

### nssa_type

**Type**: Integer  
**Path**: `router_bgp.address_family_ipv4.redistribute.ospfv3.match_nssa_external.nssa_type`  
**Valid Values**: `1`, `2`  

NSSA External Type Number.

---

### nssa_type

**Type**: Integer  
**Path**: `router_bgp.address_family_ipv4_multicast.redistribute.ospf.match_nssa_external.nssa_type`  
**Valid Values**: `1`, `2`  

NSSA External Type Number.

---

### nssa_type

**Type**: Integer  
**Path**: `router_bgp.address_family_ipv4_multicast.redistribute.ospfv3.match_nssa_external.nssa_type`  
**Valid Values**: `1`, `2`  

NSSA External Type Number.

---

### nssa_type

**Type**: Integer  
**Path**: `router_bgp.address_family_ipv6.redistribute.ospfv3.match_nssa_external.nssa_type`  
**Valid Values**: `1`, `2`  

NSSA External Type Number.

---

### nssa_type

**Type**: Integer  
**Path**: `router_bgp.address_family_ipv6_multicast.redistribute.ospf.match_nssa_external.nssa_type`  
**Valid Values**: `1`, `2`  

NSSA External Type Number.

---

### nssa_type

**Type**: Integer  
**Path**: `router_bgp.address_family_ipv6_multicast.redistribute.ospfv3.match_nssa_external.nssa_type`  
**Valid Values**: `1`, `2`  

NSSA External Type Number.

---

### nssa_type

**Type**: Integer  
**Path**: `router_bgp.vrfs.[].redistribute.ospf.match_nssa_external.nssa_type`  
**Valid Values**: `1`, `2`  

NSSA External Type Number.

---

### nssa_type

**Type**: Integer  
**Path**: `router_bgp.vrfs.[].redistribute.ospfv3.match_nssa_external.nssa_type`  
**Valid Values**: `1`, `2`  

NSSA External Type Number.

---

### nssa_type

**Type**: Integer  
**Path**: `router_bgp.vrfs.[].address_family_ipv4.redistribute.ospf.match_nssa_external.nssa_type`  
**Valid Values**: `1`, `2`  

NSSA External Type Number.

---

### nssa_type

**Type**: Integer  
**Path**: `router_bgp.vrfs.[].address_family_ipv4.redistribute.ospfv3.match_nssa_external.nssa_type`  
**Valid Values**: `1`, `2`  

NSSA External Type Number.

---

### nssa_type

**Type**: Integer  
**Path**: `router_bgp.vrfs.[].address_family_ipv6.redistribute.ospfv3.match_nssa_external.nssa_type`  
**Valid Values**: `1`, `2`  

NSSA External Type Number.

---

### nssa_type

**Type**: Integer  
**Path**: `router_bgp.vrfs.[].address_family_ipv4_multicast.redistribute.ospf.match_nssa_external.nssa_type`  
**Valid Values**: `1`, `2`  

NSSA External Type Number.

---

### nssa_type

**Type**: Integer  
**Path**: `router_bgp.vrfs.[].address_family_ipv4_multicast.redistribute.ospfv3.match_nssa_external.nssa_type`  
**Valid Values**: `1`, `2`  

NSSA External Type Number.

---

### nssa_type

**Type**: Integer  
**Path**: `router_bgp.vrfs.[].address_family_ipv6_multicast.redistribute.ospf.match_nssa_external.nssa_type`  
**Valid Values**: `1`, `2`  

NSSA External Type Number.

---

### nssa_type

**Type**: Integer  
**Path**: `router_bgp.vrfs.[].address_family_ipv6_multicast.redistribute.ospfv3.match_nssa_external.nssa_type`  
**Valid Values**: `1`, `2`  

NSSA External Type Number.

---

## O

### operation

**Type**: String  
**Path**: `event_handlers.[].trigger_on_maintenance.operation`  
**Valid Values**: `enter`, `exit`  
---

### origin

**Type**: String  
**Path**: `as_path.access_lists.[].entries.[].origin`  
**Default**: `any`  
**Valid Values**: `any`, `egp`, `igp`, `incomplete`  
---

### ospf_authentication

**Type**: String  
**Path**: `ethernet_interfaces.[].ospf_authentication`  
**Valid Values**: `none`, `simple`, `message-digest`  
---

### ospf_authentication

**Type**: String  
**Path**: `port_channel_interfaces.[].ospf_authentication`  
**Valid Values**: `none`, `simple`, `message-digest`  
---

### ospf_authentication

**Type**: String  
**Path**: `vlan_interfaces.[].ospf_authentication`  
**Valid Values**: `none`, `simple`, `message-digest`  
---

### ospf_authentication_key_type

**Type**: String  
**Path**: `ethernet_interfaces.[].ospf_authentication_key_type`  
**Default**: `7`  
**Valid Values**: `7`, `8a`  

Authentication key type.

---

### ospf_authentication_key_type

**Type**: String  
**Path**: `port_channel_interfaces.[].ospf_authentication_key_type`  
**Default**: `7`  
**Valid Values**: `7`, `8a`  

Authentication key type.

---

### ospf_authentication_key_type

**Type**: String  
**Path**: `vlan_interfaces.[].ospf_authentication_key_type`  
**Default**: `7`  
**Valid Values**: `7`, `8a`  

Authentication key type.

---

### ospf_route_type

**Type**: String  
**Path**: `router_isis.redistribute_routes.[].ospf_route_type`  
**Valid Values**: `external`, `internal`, `nssa-external`  

ospf_route_type is required with source_protocols 'ospf' and 'ospfv3'.

---

## P

### passphrase_type

**Type**: String  
**Path**: `dot1x.supplicant.profiles.[].passphrase_type`  
**Default**: `7`  
**Valid Values**: `0`, `7`, `8a`  
---

### password_type

**Type**: String  
**Path**: `cvx.services.mcs.redis.password_type`  
**Default**: `7`  
**Valid Values**: `0`, `7`, `8a`  
---

### password_type

**Type**: String  
**Path**: `monitor_server_radius.probe.access_request.password_type`  
**Default**: `7`  
**Valid Values**: `0`, `7`, `8a`  
---

### password_type

**Type**: String  
**Path**: `monitor_telemetry_influx.destinations.[].password_type`  
**Default**: `7`  
**Valid Values**: `0`, `7`, `8a`  
---

### password_type

**Type**: String  
**Path**: `mpls.rsvp.authentication.password_indexes.[].password_type`  
**Default**: `7`  
**Valid Values**: `0`, `7`, `8a`  

Authentication password type.

---

### password_type

**Type**: String  
**Path**: `router_bgp.peer_groups.[].password_type`  
**Default**: `7`  
**Valid Values**: `7`, `8a`  
---

### password_type

**Type**: String  
**Path**: `router_bgp.neighbors.[].password_type`  
**Default**: `7`  
**Valid Values**: `7`, `8a`  
---

### password_type

**Type**: String  
**Path**: `router_bgp.vrfs.[].neighbors.[].password_type`  
**Default**: `7`  
**Valid Values**: `7`, `8a`  
---

### payload

**Type**: String  
**Path**: `monitor_session_default_encapsulation_gre.payload`  
**Valid Values**: `full-packet`, `inner-packet`  

Mirroring GRE payload type configuration commands.

---

### peer_dynamic_source

**Type**: String  
**Path**: `router_path_selection.peer_dynamic_source`  
**Valid Values**: `stun`  

Source of dynamic peer discovery.

---

### permit_response_traffic

**Type**: String  
**Path**: `access_lists.[].permit_response_traffic`  
**Valid Values**: `nat`  

Permit response traffic automatically based on NAT translations.
Minimum EOS version requirement 4.32.2F.

---

### permit_response_traffic

**Type**: String  
**Path**: `ip_access_lists.[].permit_response_traffic`  
**Valid Values**: `nat`  

Permit response traffic automatically based on NAT translations.
Minimum EOS version requirement 4.32.2F.

---

### pfs_dh_group

**Type**: Integer  
**Path**: `ip_security.sa_policies.[].pfs_dh_group`  
**Valid Values**: `1`, `2`, `5`, `14`, `15`, `16`, `17`, `19`, `20`, `21`, `24`  
---

### platform

**Type**: Dictionary  
**Path**: `platform`  

Every key below this point is platform dependent.

---

### port_control

**Type**: String  
**Path**: `ethernet_interfaces.[].dot1x.port_control`  
**Valid Values**: `auto`, `force-authorized`, `force-unauthorized`  
---

### precedence

**Type**: Integer  
**Path**: `platform.trident.mmu.queue_profiles.[].multicast_queues.[].drop.precedence`  
**Valid Values**: `1`, `2`  
---

### precedence

**Type**: Integer  
**Path**: `platform.trident.mmu.queue_profiles.[].unicast_queues.[].drop.precedence`  
**Valid Values**: `1`, `2`  
---

### preemption

**Type**: String  
**Path**: `mpls.rsvp.preemption_method.preemption`  
**Valid Values**: `hard`, `soft`  
---

### preferred_metric

**Type**: String  
**Path**: `router_adaptive_virtual_topology.profiles.[].metric_order.preferred_metric`  
**Valid Values**: `jitter`, `latency`, `load`, `loss-rate`  
---

### priority

**Type**: String  
**Path**: `ethernet_interfaces.[].poe.priority`  
**Valid Values**: `critical`, `high`, `medium`, `low`  

Prioritize a port's power in the event that one of the switch's power supplies loses power.

---

### priority

**Type**: String  
**Path**: `qos_profiles.[].tx_queues.[].priority`  
**Valid Values**: `priority strict`, `no priority`  
---

### priority

**Type**: String  
**Path**: `qos_profiles.[].uc_tx_queues.[].priority`  
**Valid Values**: `priority strict`, `no priority`  
---

### priority

**Type**: String  
**Path**: `qos_profiles.[].mc_tx_queues.[].priority`  
**Valid Values**: `priority strict`, `no priority`  
---

### priority_flow_control

**Type**: Dictionary  
**Path**: `priority_flow_control`  

Global Priority Flow Control settings.


---

### profile

**Type**: String  
**Path**: `ip_hardware.fib.optimize.prefixes.profile`  
**Valid Values**: `internet`, `urpf-internet`  
---

### profile

**Type**: String  
**Path**: `platform.fap.buffering_egress.profile`  
**Valid Values**: `unicast`, `balanced`  

Preferred traffic profile for egress fap buffering.

---

### profile

**Type**: String  
**Path**: `ptp.profile`  
**Valid Values**: `g8275.1`, `g8275.2`  
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

### protocol

**Type**: String  
**Path**: `ip_nat.profiles.[].destination.static.[].protocol`  
**Valid Values**: `udp`, `tcp`  
---

### protocol

**Type**: String  
**Path**: `ip_nat.profiles.[].source.static.[].protocol`  
**Valid Values**: `udp`, `tcp`  
---

### protocol

**Type**: String  
**Path**: `ip_nat.translation.timeouts.[].protocol`  
**Valid Values**: `tcp`, `udp`  
---

### protocol

**Type**: String  
**Path**: `logging.vrfs.[].hosts.[].protocol`  
**Default**: `udp`  
**Valid Values**: `tcp`, `udp`, `tls`  
---

### protocol

**Type**: String  
**Path**: `monitor_telemetry_postcard_policy.sample_policies.[].match_rules.[].protocols.[].protocol`  
**Valid Values**: `tcp`, `udp`  
---

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

### protocol

**Type**: String  
**Path**: `router_bgp.address_family_ipv4_labeled_unicast.tunnel_source_protocols.[].protocol`  
**Valid Values**: `isis segment-routing`, `ldp`  
---

### protocol

**Type**: String  
**Path**: `vlan_interfaces.[].ip_nat.destination.static.[].protocol`  
**Valid Values**: `udp`, `tcp`  
---

### protocol

**Type**: String  
**Path**: `vlan_interfaces.[].ip_nat.source.static.[].protocol`  
**Valid Values**: `udp`, `tcp`  
---

## Q

### qinq_dzgre_source

**Type**: String  
**Path**: `ethernet_interfaces.[].switchport.tool.identity.qinq_dzgre_source`  
**Valid Values**: `policy inner port`, `port inner policy`  
---

### qinq_dzgre_source

**Type**: String  
**Path**: `port_channel_interfaces.[].switchport.tool.identity.qinq_dzgre_source`  
**Valid Values**: `policy inner port`, `port inner policy`  
---

### QOS Class-maps

**Type**: Dictionary  
**Path**: `class_maps`  
---

### qos_trust

**Type**: String  
**Path**: `switchport_default.phone.qos_trust`  
**Valid Values**: `cos`, `dscp`  

Quality of Service (QoS) trust mode. Outgoing traffic class being derived from the ingress COS/DSCP value.

---

## R

### radius_proxy

**Type**: Dictionary  
**Path**: `radius_proxy`  

Configure RADIUS proxy parameters.

---

### rate

**Type**: Integer  
**Path**: `monitor_telemetry_postcard_policy.ingress.sample.rate`  
**Valid Values**: `16384`, `32768`, `65536`  

Sampling rate. `rate` is preferred when both `rate` and `tcp_udp_checksum` are defined.

---

### rate_burst_size_unit

**Type**: String  
**Path**: `policy_maps.qos.[].classes.[].police.rate_burst_size_unit`  
**Default**: `bytes`  
**Valid Values**: `bytes`, `kbytes`, `mbytes`, `packets`  
---

### rate_unit

**Type**: String  
**Path**: `policy_maps.qos.[].classes.[].police.rate_unit`  
**Default**: `bps`  
**Valid Values**: `bps`, `kbps`, `mbps`, `pps`  
---

### rate_unit

**Type**: String  
**Path**: `policy_maps.copp_system_policy.classes.[].rate_unit`  
**Valid Values**: `pps`, `kbps`  

The `rate_unit` must be defined for `shape` and `bandwidth`.

---

### read_structured_config_from_file

**Type**: Boolean  
**Path**: `read_structured_config_from_file`  
**Default**: `True`  

Read structured configuration from files in `structured_dir` (default directory also used by the `eos_designs` role).
If set to false, `eos_cli_config_gen` will read structured configuration from hostvars.


---

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

### redundancy

**Type**: String  
**Path**: `port_channel_interfaces.[].evpn_ethernet_segment.redundancy`  
**Valid Values**: `all-active`, `single-active`  
---

### regex_mode

**Type**: String  
**Path**: `as_path.regex_mode`  
**Valid Values**: `asn`, `string`  
---

### remote_id_format

**Type**: String  
**Path**: `ipv6_dhcp_relay.option.remote_id_format`  
**Valid Values**: `%m:%h:%p`, `%m:%i`, `%m:%p`  

Add RemoteID option 37 in format
- MAC address, hostname and interface name (`%m:%h:%p`)
- MAC address and interface ID (`%m:%i`)
- MAC address and interface name (`%m:%p`)

---

### reversion

**Type**: String  
**Path**: `mpls.rsvp.fast_reroute.reversion`  
**Valid Values**: `global`, `local`  

Reversion behavior.
Global revertive repair.
Local revertive repair.

---

### rib_type

**Type**: String  
**Path**: `router_bgp.address_family_evpn.next_hop_mpls_resolution_ribs.[].rib_type`  
**Valid Values**: `system-connected`, `tunnel-rib-colored`, `tunnel-rib`  

Type of RIB. For 'tunnel-rib', use 'rib_name' to specify the name of the Tunnel-RIB to use.

---

### rib_type

**Type**: String  
**Path**: `router_bgp.address_family_ipv4_labeled_unicast.next_hop_resolution_ribs.[].rib_type`  
**Valid Values**: `system-connected`, `tunnel-rib-colored`, `tunnel-rib`  

Type of RIB. For 'tunnel-rib', use 'rib_name' to specify the name of the Tunnel-RIB to use.

---

### role

**Type**: String  
**Path**: `ethernet_interfaces.[].ptp.role`  
**Valid Values**: `master`, `dynamic`  
---

### role

**Type**: String  
**Path**: `port_channel_interfaces.[].ptp.role`  
**Valid Values**: `master`, `dynamic`  
---

### Router General configuration

**Type**: Dictionary  
**Path**: `router_general`  
---

### Router IGMP Configuration

**Type**: Dictionary  
**Path**: `router_igmp`  
---

### Router OSPF Configuration

**Type**: Dictionary  
**Path**: `router_ospf`  
---

### router_internet_exit

**Type**: Dictionary  
**Path**: `router_internet_exit`  

Internet-exit feature to configure internet bound service for virtual topologies.

---

### router_path_selection

**Type**: Dictionary  
**Path**: `router_path_selection`  

Dynamic path selection configuration.

---

### router_rip

**Type**: Dictionary  
**Path**: `router_rip`  

Routing Information Protocol settings.

---

### router_service_insertion

**Type**: Dictionary  
**Path**: `router_service_insertion`  

Configure network services inserted to data forwarding.

---

## S

### secret_type

**Type**: String  
**Path**: `management_security.shared_secret_profiles.[].secrets.[].secret_type`  
**Default**: `7`  
**Valid Values**: `0`, `7`, `8a`  
---

### send

**Type**: String  
**Path**: `router_bgp.bgp.additional_paths.send`  
**Valid Values**: `any`, `backup`, `ecmp`, `limit`, `disabled`  

Select an option to send multiple paths for same prefix through bgp updates.
any: Send any eligible path.
backup: Best path and installed backup path.
ecmp: All paths in best path ECMP group.
limit: Limit to n eligible paths.
disabled: Disable sending any paths.

---

### send

**Type**: String  
**Path**: `router_bgp.address_family_evpn.neighbors.[].additional_paths.send`  
**Valid Values**: `any`, `backup`, `ecmp`, `limit`, `disabled`  

Select an option to send multiple paths for same prefix through bgp updates.
any: Send any eligible path.
backup: Best path and installed backup path.
ecmp: All paths in best path ECMP group.
limit: Limit to n eligible paths.
disabled: Disable sending any paths.

---

### send

**Type**: String  
**Path**: `router_bgp.address_family_evpn.peer_groups.[].additional_paths.send`  
**Valid Values**: `any`, `backup`, `ecmp`, `limit`, `disabled`  

Select an option to send multiple paths for same prefix through bgp updates.
any: Send any eligible path.
backup: Best path and installed backup path.
ecmp: All paths in best path ECMP group.
limit: Limit to n eligible paths.
disabled: Disable sending any paths.

---

### send

**Type**: String  
**Path**: `router_bgp.address_family_evpn.bgp.additional_paths.send`  
**Valid Values**: `any`, `backup`, `ecmp`, `limit`, `disabled`  

Select an option to send multiple paths for same prefix through bgp updates.
any: Send any eligible path.
backup: Best path and installed backup path.
ecmp: All paths in best path ECMP group.
limit: Limit to n eligible paths.
disabled: Disable sending any paths.

---

### send

**Type**: String  
**Path**: `router_bgp.address_family_ipv4.bgp.additional_paths.send`  
**Valid Values**: `any`, `backup`, `ecmp`, `limit`, `disabled`  

Select an option to send multiple paths for same prefix through bgp updates.
any: Send any eligible path.
backup: Best path and installed backup path.
ecmp: All paths in best path ECMP group.
limit: Limit to n eligible paths.
disabled: Disable sending any paths.

---

### send

**Type**: String  
**Path**: `router_bgp.address_family_ipv4.peer_groups.[].additional_paths.send`  
**Valid Values**: `any`, `backup`, `ecmp`, `limit`, `disabled`  

Select an option to send multiple paths for same prefix through bgp updates.
any: Send any eligible path.
backup: Best path and installed backup path.
ecmp: All paths in best path ECMP group.
limit: Limit to n eligible paths.
disabled: Disable sending any paths.

---

### send

**Type**: String  
**Path**: `router_bgp.address_family_ipv4.neighbors.[].additional_paths.send`  
**Valid Values**: `any`, `backup`, `ecmp`, `limit`, `disabled`  

Select an option to send multiple paths for same prefix through bgp updates.
any: Send any eligible path.
backup: Best path and installed backup path.
ecmp: All paths in best path ECMP group.
limit: Limit to n eligible paths.
disabled: Disable sending any paths.

---

### send

**Type**: String  
**Path**: `router_bgp.address_family_ipv4_labeled_unicast.bgp.additional_paths.send`  
**Valid Values**: `any`, `backup`, `ecmp`, `limit`, `disabled`  

Select an option to send multiple paths for same prefix through bgp updates.
any: Send any eligible path.
backup: Best path and installed backup path.
ecmp: All paths in best path ECMP group.
limit: Limit to n eligible paths.
disabled: Disable sending any paths.

---

### send

**Type**: String  
**Path**: `router_bgp.address_family_ipv4_labeled_unicast.peer_groups.[].additional_paths.send`  
**Valid Values**: `any`, `backup`, `ecmp`, `limit`, `disabled`  

Select an option to send multiple paths for same prefix through bgp updates.
any: Send any eligible path.
backup: Best path and installed backup path.
ecmp: All paths in best path ECMP group.
limit: Limit to n eligible paths.
disabled: Disable sending any paths.

---

### send

**Type**: String  
**Path**: `router_bgp.address_family_ipv4_labeled_unicast.neighbors.[].additional_paths.send`  
**Valid Values**: `any`, `backup`, `ecmp`, `limit`, `disabled`  

Select an option to send multiple paths for same prefix through bgp updates.
any: Send any eligible path.
backup: Best path and installed backup path.
ecmp: All paths in best path ECMP group.
limit: Limit to n eligible paths.
disabled: Disable sending any paths.

---

### send

**Type**: String  
**Path**: `router_bgp.address_family_ipv6.bgp.additional_paths.send`  
**Valid Values**: `any`, `backup`, `ecmp`, `limit`, `disabled`  

Select an option to send multiple paths for same prefix through bgp updates.
any: Send any eligible path.
backup: Best path and installed backup path.
ecmp: All paths in best path ECMP group.
limit: Limit to n eligible paths.
disabled: Disable sending any paths.

---

### send

**Type**: String  
**Path**: `router_bgp.address_family_ipv6.peer_groups.[].additional_paths.send`  
**Valid Values**: `any`, `backup`, `ecmp`, `limit`, `disabled`  

Select an option to send multiple paths for same prefix through bgp updates.
any: Send any eligible path.
backup: Best path and installed backup path.
ecmp: All paths in best path ECMP group.
limit: Limit to n eligible paths.
disabled: Disable sending any paths.

---

### send

**Type**: String  
**Path**: `router_bgp.address_family_ipv6.neighbors.[].additional_paths.send`  
**Valid Values**: `any`, `backup`, `ecmp`, `limit`, `disabled`  

Select an option to send multiple paths for same prefix through bgp updates.
any: Send any eligible path.
backup: Best path and installed backup path.
ecmp: All paths in best path ECMP group.
limit: Limit to n eligible paths.
disabled: Disable sending any paths.

---

### send

**Type**: String  
**Path**: `router_bgp.address_family_path_selection.bgp.additional_paths.send`  
**Valid Values**: `any`, `backup`, `ecmp`, `limit`, `disabled`  

Select an option to send multiple paths for same prefix through bgp updates.
any: Send any eligible path.
backup: Best path and installed backup path.
ecmp: All paths in best path ECMP group.
limit: Limit to n eligible paths.
disabled: Disable sending any paths.

---

### send

**Type**: String  
**Path**: `router_bgp.address_family_path_selection.neighbors.[].additional_paths.send`  
**Valid Values**: `any`, `backup`, `ecmp`, `limit`, `disabled`  

Select an option to send multiple paths for same prefix through bgp updates.
any: Send any eligible path.
backup: Best path and installed backup path.
ecmp: All paths in best path ECMP group.
limit: Limit to n eligible paths.
disabled: Disable sending any paths.

---

### send

**Type**: String  
**Path**: `router_bgp.address_family_path_selection.peer_groups.[].additional_paths.send`  
**Valid Values**: `any`, `backup`, `ecmp`, `limit`, `disabled`  

Select an option to send multiple paths for same prefix through bgp updates.
any: Send any eligible path.
backup: Best path and installed backup path.
ecmp: All paths in best path ECMP group.
limit: Limit to n eligible paths.
disabled: Disable sending any paths.

---

### send

**Type**: String  
**Path**: `router_bgp.vrfs.[].bgp.additional_paths.send`  
**Valid Values**: `any`, `backup`, `ecmp`, `limit`, `disabled`  

Select an option to send multiple paths for same prefix through bgp updates.
any: Send any eligible path.
backup: Best path and installed backup path.
ecmp: All paths in best path ECMP group.
limit: Limit to n eligible paths.
disabled: Disable sending any paths.

---

### send

**Type**: String  
**Path**: `router_bgp.vrfs.[].neighbors.[].additional_paths.send`  
**Valid Values**: `any`, `backup`, `ecmp`, `limit`, `disabled`  

Select an option to send multiple paths for same prefix through bgp updates.
any: Send any eligible path.
backup: Best path and installed backup path.
ecmp: All paths in best path ECMP group.
limit: Limit to n eligible paths.
disabled: Disable sending any paths.

---

### send

**Type**: String  
**Path**: `router_bgp.vrfs.[].address_family_ipv4.bgp.additional_paths.send`  
**Valid Values**: `any`, `backup`, `ecmp`, `limit`, `disabled`  

Select an option to send multiple paths for same prefix through bgp updates.
any: Send any eligible path.
backup: Best path and installed backup path.
ecmp: All paths in best path ECMP group.
limit: Limit to n eligible paths.
disabled: Disable sending any paths.

---

### send

**Type**: String  
**Path**: `router_bgp.vrfs.[].address_family_ipv4.neighbors.[].additional_paths.send`  
**Valid Values**: `any`, `backup`, `ecmp`, `limit`, `disabled`  

Select an option to send multiple paths for same prefix through bgp updates.
any: Send any eligible path.
backup: Best path and installed backup path.
ecmp: All paths in best path ECMP group.
limit: Limit to n eligible paths.
disabled: Disable sending any paths.

---

### send

**Type**: String  
**Path**: `router_bgp.vrfs.[].address_family_ipv6.bgp.additional_paths.send`  
**Valid Values**: `any`, `backup`, `ecmp`, `limit`, `disabled`  

Select an option to send multiple paths for same prefix through bgp updates.
any: Send any eligible path.
backup: Best path and installed backup path.
ecmp: All paths in best path ECMP group.
limit: Limit to n eligible paths.
disabled: Disable sending any paths.

---

### send

**Type**: String  
**Path**: `router_bgp.vrfs.[].address_family_ipv6.neighbors.[].additional_paths.send`  
**Valid Values**: `any`, `backup`, `ecmp`, `limit`, `disabled`  

Select an option to send multiple paths for same prefix through bgp updates.
any: Send any eligible path.
backup: Best path and installed backup path.
ecmp: All paths in best path ECMP group.
limit: Limit to n eligible paths.
disabled: Disable sending any paths.

---

### send_community

**Type**: String  
**Path**: `router_bgp.neighbor_default.send_community`  
**Valid Values**: `all`, `large`, `extended`, `standard`, `extended large`, `standard large`, `standard extended`, `standard extended large`  
---

### service

**Type**: String  
**Path**: `application_traffic_recognition.categories.[].applications.[].service`  
**Valid Values**: `audio-video`, `chat`, `default`, `file-transfer`, `networking-protocols`, `peer-to-peer`, `software-update`  

Service Name.
Specific service to target for this application.
If no service is specified, all supported services of the application are matched.
Not all valid values are valid for all applications, check on EOS CLI.

---

### service

**Type**: String  
**Path**: `application_traffic_recognition.application_profiles.[].applications.[].service`  
**Valid Values**: `audio-video`, `chat`, `default`, `file-transfer`, `networking-protocols`, `peer-to-peer`, `software-update`  

Service Name.
Specific service to target for this application.
If no service is specified, all supported services of the application are matched.
Not all valid values are valid for all applications, check on EOS CLI.

---

### service

**Type**: String  
**Path**: `application_traffic_recognition.application_profiles.[].categories.[].service`  
**Valid Values**: `audio-video`, `chat`, `default`, `file-transfer`, `networking-protocols`, `peer-to-peer`, `software-update`  

Service Name.
Specific service to target for this application.
If no service is specified, all supported services of the application are matched.
Not all valid values are valid for all applications, check on EOS CLI.

---

### service_routing_protocols_model

**Type**: String  
**Path**: `service_routing_protocols_model`  
**Valid Values**: `multi-agent`, `ribd`  
---

### severity

**Type**: String  
**Path**: `logging.level.[].severity`  
**Valid Values**: `alerts`, `critical`, `debugging`, `emergencies`, `errors`, `informational`, `notifications`, `warnings`, `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`  

Severity of facility. Below are the supported severities.
emergencies    System is unusable                (severity=0)
alerts         Immediate action needed           (severity=1)
critical       Critical conditions               (severity=2)
errors         Error conditions                  (severity=3)
warnings       Warning conditions                (severity=4)
notifications  Normal but significant conditions (severity=5)
informational  Informational messages            (severity=6)
debugging      Debugging messages                (severity=7)
<0-7>          Severity level value

---

### shell

**Type**: String  
**Path**: `local_users.[].shell`  
**Valid Values**: `/bin/bash`, `/bin/sh`, `/sbin/nologin`  

Specify shell for the user.


---

### snmp_server

**Type**: Dictionary  
**Path**: `snmp_server`  

SNMP settings.

---

### software_forwarding

**Type**: String  
**Path**: `router_multicast.ipv4.software_forwarding`  
**Valid Values**: `kernel`, `sfe`  
---

### source_interface

**Type**: String  
**Path**: `ethernet_interfaces.[].switchport.source_interface`  
**Valid Values**: `tx`, `tx multicast`  

tx: Allow bridged traffic to go out of the source interface.
tx multicast: Allow multicast traffic only to go out of the source interface.

---

### source_interface

**Type**: String  
**Path**: `port_channel_interfaces.[].switchport.source_interface`  
**Valid Values**: `tx`, `tx multicast`  

tx: Allow bridged traffic to go out of the source interface.
tx multicast: Allow multicast traffic only to go out of the source interface.

---

### source_ports_match

**Type**: String  
**Path**: `ip_access_lists.[].entries.[].source_ports_match`  
**Default**: `eq`  
**Valid Values**: `eq`, `gt`, `lt`, `neq`, `range`  
---

### source_protocol

**Type**: String  
**Path**: `router_isis.redistribute_routes.[].source_protocol`  
**Valid Values**: `bgp`, `connected`, `isis`, `ospf`, `ospfv3`, `static`  
---

### spanning_tree_bpdufilter

**Type**: String  
**Path**: `ethernet_interfaces.[].spanning_tree_bpdufilter`  
**Valid Values**: `enabled`, `disabled`, `True`, `False`, `true`, `false`  
---

### spanning_tree_bpdufilter

**Type**: String  
**Path**: `port_channel_interfaces.[].spanning_tree_bpdufilter`  
**Valid Values**: `enabled`, `disabled`, `True`, `False`, `true`, `false`  
---

### spanning_tree_bpduguard

**Type**: String  
**Path**: `ethernet_interfaces.[].spanning_tree_bpduguard`  
**Valid Values**: `enabled`, `disabled`, `True`, `False`, `true`, `false`  
---

### spanning_tree_bpduguard

**Type**: String  
**Path**: `port_channel_interfaces.[].spanning_tree_bpduguard`  
**Valid Values**: `enabled`, `disabled`, `True`, `False`, `true`, `false`  
---

### spanning_tree_guard

**Type**: String  
**Path**: `ethernet_interfaces.[].spanning_tree_guard`  
**Valid Values**: `loop`, `root`, `disabled`  
---

### spanning_tree_guard

**Type**: String  
**Path**: `port_channel_interfaces.[].spanning_tree_guard`  
**Valid Values**: `loop`, `root`, `disabled`  
---

### spanning_tree_portfast

**Type**: String  
**Path**: `ethernet_interfaces.[].spanning_tree_portfast`  
**Valid Values**: `edge`, `network`  
---

### spanning_tree_portfast

**Type**: String  
**Path**: `port_channel_interfaces.[].spanning_tree_portfast`  
**Valid Values**: `edge`, `network`  
---

### speed

**Type**: String  
**Path**: `ethernet_interfaces.[].speed`  
**Valid Values**: `100full`, `100g`, `100g-1`, `100g-2`, `100g-4`, `100half`, `10full`, `10g`, `10half`, `1g`, `200g`, `200g-2`, `200g-4`, `25g`, `400g`, `400g-4`, `400g-8`, `40g`, `50g`, `50g-1`, `50g-2`, `800g-8`, `sfp-1000baset auto 100full`, `1.6t-8`, `100mfull`, `100mhalf`, `10mfull`, `10mhalf`, `200g-1`, `400g-2`, `40g-4`, `800g-4`, `auto`, `auto 10000full`, `auto 1000full`, `auto 100full`, `auto 100g-1`, `auto 100g-2`, `auto 100g-4`, `auto 100gfull`, `auto 100half`, `auto 10full`, `auto 10gfull`, `auto 10half`, `auto 1gfull`, `auto 2.5gfull`, `auto 200g-2`, `auto 200g-4`, `auto 25gfull`, `auto 400g-4`, `auto 400g-8`, `auto 40gfull`, `auto 50g-1`, `auto 50g-2`, `auto 50gfull`, `auto 5gfull`, `auto 800g-8`, `auto 1.6t-8`, `auto 100mfull`, `auto 100mhalf`, `auto 10g`, `auto 10mfull`, `auto 10mhalf`, `auto 1g`, `auto 2.5g`, `auto 200g-1`, `auto 25g`, `auto 400g-2`, `auto 40g-4`, `auto 5g`, `auto 800g-4`, `forced 10000full`, `forced 1000full`, `forced 1000half`, `forced 100full`, `forced 100gfull`, `forced 100half`, `forced 10full`, `forced 10half`, `forced 25gfull`, `forced 40gfull`, `forced 50gfull`  

Interface Speed.

---

### speed

**Type**: String  
**Path**: `management_interfaces.[].speed`  
**Valid Values**: `100full`, `100g`, `100g-1`, `100g-2`, `100g-4`, `100half`, `10full`, `10g`, `10half`, `1g`, `200g`, `200g-2`, `200g-4`, `25g`, `400g`, `400g-4`, `400g-8`, `40g`, `50g`, `50g-1`, `50g-2`, `800g-8`, `sfp-1000baset auto 100full`, `1.6t-8`, `100mfull`, `100mhalf`, `10mfull`, `10mhalf`, `200g-1`, `400g-2`, `40g-4`, `800g-4`, `auto`, `auto 10000full`, `auto 1000full`, `auto 100full`, `auto 100g-1`, `auto 100g-2`, `auto 100g-4`, `auto 100gfull`, `auto 100half`, `auto 10full`, `auto 10gfull`, `auto 10half`, `auto 1gfull`, `auto 2.5gfull`, `auto 200g-2`, `auto 200g-4`, `auto 25gfull`, `auto 400g-4`, `auto 400g-8`, `auto 40gfull`, `auto 50g-1`, `auto 50g-2`, `auto 50gfull`, `auto 5gfull`, `auto 800g-8`, `auto 1.6t-8`, `auto 100mfull`, `auto 100mhalf`, `auto 10g`, `auto 10mfull`, `auto 10mhalf`, `auto 1g`, `auto 2.5g`, `auto 200g-1`, `auto 25g`, `auto 400g-2`, `auto 40g-4`, `auto 5g`, `auto 800g-4`, `forced 10000full`, `forced 1000full`, `forced 1000half`, `forced 100full`, `forced 100gfull`, `forced 100half`, `forced 10full`, `forced 10half`, `forced 25gfull`, `forced 40gfull`, `forced 50gfull`  

Interface Speed.

---

### stage

**Type**: String  
**Path**: `event_handlers.[].trigger_on_maintenance.stage`  
**Valid Values**: `bgp`, `linkdown`, `mlag`, `ratemon`  

Action is triggered after/before specified stage.

---

### state

**Type**: String  
**Path**: `vlans.[].state`  
**Valid Values**: `active`, `suspend`  
---

### stun

**Type**: Dictionary  
**Path**: `stun`  

STUN configuration.

---

### System Boot Settings

**Type**: Dictionary  
**Path**: `boot`  

Set the Aboot password.


---

## T

### tag

**Type**: String  
**Path**: `ethernet_interfaces.[].switchport.tool.identity.tag`  
**Valid Values**: `dot1q`, `qinq`  
---

### tag

**Type**: String  
**Path**: `port_channel_interfaces.[].switchport.tool.identity.tag`  
**Valid Values**: `dot1q`, `qinq`  
---

### Terminal Settings

**Type**: Dictionary  
**Path**: `terminal`  
---

### threshold

**Type**: String  
**Path**: `platform.trident.mmu.queue_profiles.[].ingress.priority_groups.[].threshold`  
**Valid Values**: `1`, `1/128`, `1/16`, `1/2`, `1/32`, `1/4`, `1/64`, `1/8`, `2`, `4`, `8`  
---

### threshold

**Type**: String  
**Path**: `platform.trident.mmu.queue_profiles.[].ingress.threshold`  
**Valid Values**: `1`, `1/128`, `1/16`, `1/2`, `1/32`, `1/4`, `1/64`, `1/8`, `2`, `4`, `8`  

Specify the dynamic shared memory threshold.

---

### threshold

**Type**: String  
**Path**: `platform.trident.mmu.queue_profiles.[].multicast_queues.[].threshold`  
**Valid Values**: `1`, `1/128`, `1/16`, `1/2`, `1/32`, `1/4`, `1/64`, `1/8`, `2`, `4`, `8`  

Dynamic Shared Memory threshold.


---

### threshold

**Type**: String  
**Path**: `platform.trident.mmu.queue_profiles.[].unicast_queues.[].threshold`  
**Valid Values**: `1`, `1/128`, `1/16`, `1/2`, `1/32`, `1/4`, `1/64`, `1/8`, `2`, `4`, `8`  

Dynamic Shared Memory threshold.


---

### time_duration_unit

**Type**: String  
**Path**: `dot1x.aaa.unresponsive.action.cached_results_timeout.time_duration_unit`  
**Valid Values**: `days`, `hours`, `minutes`, `seconds`  
---

### time_duration_unit

**Type**: String  
**Path**: `dot1x.aaa.unresponsive.phone_action.cached_results_timeout.time_duration_unit`  
**Valid Values**: `days`, `hours`, `minutes`, `seconds`  
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

### timestamp

**Type**: String  
**Path**: `logging.format.timestamp`  
**Valid Values**: `high-resolution`, `traditional`, `traditional timezone`, `traditional year`, `traditional timezone year`, `traditional year timezone`  

Timestamp format.

---

### topology_role

**Type**: String  
**Path**: `router_adaptive_virtual_topology.topology_role`  
**Valid Values**: `edge`, `pathfinder`, `transit region`, `transit zone`  

Role name.

---

### transceiver_qsfp_default_mode_4x10

**Type**: Boolean  
**Path**: `transceiver_qsfp_default_mode_4x10`  
**Default**: `True`  

On all front panel ports which support this feature, the following global configuration command changes the QSFP mode from 40G to 4x10G (default). When set to false the command reverts the default QSFP mode back to 40G.


---

### transport

**Type**: String  
**Path**: `ethernet_interfaces.[].ptp.transport`  
**Valid Values**: `ipv4`, `ipv6`, `layer2`  
---

### transport

**Type**: String  
**Path**: `port_channel_interfaces.[].ptp.transport`  
**Valid Values**: `ipv4`, `ipv6`, `layer2`  
---

### trap

**Type**: String  
**Path**: `logging.trap`  
**Valid Values**: `alerts`, `critical`, `debugging`, `emergencies`, `errors`, `informational`, `notifications`, `system`, `warnings`, `disabled`  

Trap logging severity level.

---

### trigger

**Type**: String  
**Path**: `event_handlers.[].trigger`  
**Valid Values**: `on-boot`, `on-counters`, `on-intf`, `on-logging`, `on-maintenance`, `on-startup-config`, `vm-tracer vm`  

Configure event trigger condition.


---

### trunk

**Type**: String  
**Path**: `ethernet_interfaces.[].switchport.phone.trunk`  
**Valid Values**: `tagged`, `tagged phone`, `untagged`, `untagged phone`  
---

### trunk

**Type**: String  
**Path**: `port_channel_interfaces.[].switchport.phone.trunk`  
**Valid Values**: `tagged`, `tagged phone`, `untagged`, `untagged phone`  
---

### trunk

**Type**: String  
**Path**: `switchport_default.phone.trunk`  
**Valid Values**: `tagged`, `untagged`, `tagged phone`, `untagged phone`  
---

### trust

**Type**: String  
**Path**: `ethernet_interfaces.[].qos.trust`  
**Valid Values**: `dscp`, `cos`, `disabled`  
---

### trust

**Type**: String  
**Path**: `port_channel_interfaces.[].qos.trust`  
**Valid Values**: `dscp`, `cos`, `disabled`  
---

### trust

**Type**: String  
**Path**: `qos_profiles.[].trust`  
**Valid Values**: `cos`, `dscp`, `disabled`  
---

### ttl

**Type**: String  
**Path**: `mpls.tunnel.termination.model.ttl`  
**Valid Values**: `pipe`, `uniform`  
---

### ttl

**Type**: String  
**Path**: `mpls.tunnel.termination.php_model.ttl`  
**Valid Values**: `pipe`, `uniform`  
---

### ttl_match

**Type**: String  
**Path**: `ip_access_lists.[].entries.[].ttl_match`  
**Default**: `eq`  
**Valid Values**: `eq`, `gt`, `lt`, `neq`  
---

### tunnel_mode

**Type**: String  
**Path**: `tunnel_interfaces.[].tunnel_mode`  
**Valid Values**: `gre`, `ipsec`  

Tunnel encapsulation method.
`gre`: Generic route encapsulation protocol,
`ipsec`: IPsec-over-IP encapsulation.

---

### tx_interval

**Type**: String  
**Path**: `cfm.profiles.[].alarm_indication.tx_interval`  
**Valid Values**: `1 seconds`, `1 minutes`  

Transmission interval for AIS packets.

---

### tx_interval

**Type**: String  
**Path**: `cfm.profiles.[].continuity_check.tx_interval`  
**Valid Values**: `3.33 milliseconds`, `10 milliseconds`, `100 milliseconds`, `1 seconds`, `10 seconds`, `1 minutes`, `10 minutes`  

Set the transmission interval for continuity check messages (CCMs).

---

### type

**Type**: String  
**Path**: `aaa_accounting.exec.console.type`  
**Valid Values**: `none`, `start-stop`, `stop-only`  
---

### type

**Type**: String  
**Path**: `aaa_accounting.exec.default.type`  
**Valid Values**: `none`, `start-stop`, `stop-only`  
---

### type

**Type**: String  
**Path**: `aaa_accounting.system.default.type`  
**Valid Values**: `none`, `start-stop`, `stop-only`  
---

### type

**Type**: String  
**Path**: `aaa_accounting.dot1x.default.type`  
**Valid Values**: `start-stop`, `stop-only`  
---

### type

**Type**: String  
**Path**: `aaa_accounting.commands.console.[].type`  
**Valid Values**: `none`, `start-stop`, `stop-only`  
---

### type

**Type**: String  
**Path**: `aaa_accounting.commands.default.[].type`  
**Valid Values**: `none`, `start-stop`, `stop-only`  
---

### type

**Type**: String  
**Path**: `aaa_server_groups.[].type`  
**Valid Values**: `tacacs+`, `radius`, `ldap`  
---

### type

**Type**: String  
**Path**: `as_path.access_lists.[].entries.[].type`  
**Valid Values**: `permit`, `deny`  
---

### type

**Type**: String  
**Path**: `ethernet_interfaces.[].type`  
**Valid Values**: `routed`, `switched`, `l3dot1q`, `l2dot1q`, `port-channel-member`  

l3dot1q and l2dot1q are used for sub-interfaces. The parent interface should be defined as routed.
The `type = switched/routed` should not be combined with `switchport`.


---

### type

**Type**: String  
**Path**: `ip_extcommunity_lists.[].entries.[].type`  
**Valid Values**: `permit`, `deny`  
---

### type

**Type**: String  
**Path**: `ip_extcommunity_lists_regexp.[].entries.[].type`  
**Valid Values**: `permit`, `deny`  
---

### type

**Type**: String  
**Path**: `ip_nat.pools.[].type`  
**Default**: `ip-port`  
**Valid Values**: `ip-port`, `port-only`  
---

### type

**Type**: String  
**Path**: `management_interfaces.[].type`  
**Default**: `oob`  
**Valid Values**: `oob`, `inband`  

For documentation purposes only.

---

### type

**Type**: String  
**Path**: `management_tech_support.policy_show_tech_support.exclude_commands.[].type`  
**Default**: `text`  
**Valid Values**: `text`, `json`  

The supported values for type are platform dependent.

---

### type

**Type**: String  
**Path**: `monitor_sessions.[].sources.[].access_group.type`  
**Valid Values**: `ip`, `ipv6`, `mac`  
---

### type

**Type**: String  
**Path**: `monitor_sessions.[].access_group.type`  
**Valid Values**: `ip`, `ipv6`, `mac`  
---

### type

**Type**: String  
**Path**: `monitor_telemetry_postcard_policy.sample_policies.[].match_rules.[].type`  
**Valid Values**: `ipv4`, `ipv6`  

IP address version.

---

### type

**Type**: String  
**Path**: `mpls.rsvp.authentication.type`  
**Valid Values**: `md5`, `none`  

Authentication mechanism.

---

### type

**Type**: String  
**Path**: `mpls.rsvp.neighbors.[].authentication.type`  
**Valid Values**: `md5`, `none`  

Authentication mechanism.

---

### type

**Type**: String  
**Path**: `patch_panel.patches.[].connectors.[].type`  
**Valid Values**: `interface`, `pseudowire`  
---

### type

**Type**: String  
**Path**: `policy_maps.qos.[].classes.[].police.action.type`  
**Valid Values**: `dscp`, `drop-precedence`  

Set action for policed traffic.

---

### type

**Type**: String  
**Path**: `route_maps.[].sequence_numbers.[].type`  
**Valid Values**: `permit`, `deny`  
---

### type

**Type**: String  
**Path**: `router_ospf.process_ids.[].areas.[].type`  
**Default**: `normal`  
**Valid Values**: `normal`, `stub`, `nssa`  
---

### type

**Type**: String  
**Path**: `traffic_policies.policies.[].matches.[].type`  
**Valid Values**: `ipv4`, `ipv6`  
---

### type

**Type**: String  
**Path**: `vlans.[].private_vlan.type`  
**Valid Values**: `community`, `isolated`  
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

### unit

**Type**: String  
**Path**: `ip_security.sa_policies.[].sa_lifetime.unit`  
**Default**: `hours`  
**Valid Values**: `gigabytes`, `hours`, `megabytes`, `thousand-packets`  
---

### unit

**Type**: String  
**Path**: `platform.trident.mmu.headroom_pool.unit`  
**Valid Values**: `bytes`, `cells`  

Unit to be used for the `headroom_pool` value.
If not specified, default is bytes.

---

### unit

**Type**: String  
**Path**: `platform.trident.mmu.queue_profiles.[].ingress.priority_groups.[].reserved.unit`  
**Valid Values**: `bytes`, `cells`  

Unit to be used for the `priority_groups` `reserved` value.
If not specified, default is bytes.

---

### unit

**Type**: String  
**Path**: `platform.trident.mmu.queue_profiles.[].ingress.reserved.unit`  
**Valid Values**: `bytes`, `cells`  

Unit to be used for the `reserved` value.
If not specified, default is bytes.

---

### unit

**Type**: String  
**Path**: `platform.trident.mmu.queue_profiles.[].ingress.headroom.unit`  
**Valid Values**: `bytes`, `cells`  

Unit to be used for the headroom value.
If not specified, default is bytes.

---

### unit

**Type**: String  
**Path**: `platform.trident.mmu.queue_profiles.[].multicast_queues.[].unit`  
**Valid Values**: `bytes`, `cells`  

Unit to be used for the reservation value. If not specified, default is bytes.


---

### unit

**Type**: String  
**Path**: `platform.trident.mmu.queue_profiles.[].unicast_queues.[].unit`  
**Valid Values**: `bytes`, `cells`  

Unit to be used for the reservation value. If not specified, default is bytes.


---

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

### units

**Type**: String  
**Path**: `monitor_link_flap_policy.damping_profiles.[].penalty_decay.units`  
**Valid Values**: `minutes`, `seconds`  
---

### units

**Type**: String  
**Path**: `qos_profiles.[].tx_queues.[].random_detect.ecn.threshold.units`  
**Valid Values**: `segments`, `bytes`, `kbytes`, `mbytes`, `milliseconds`, `microseconds`  

Units to be used for the threshold values.

---

### units

**Type**: String  
**Path**: `qos_profiles.[].tx_queues.[].random_detect.drop.threshold.units`  
**Valid Values**: `segments`, `bytes`, `kbytes`, `mbytes`, `microseconds`, `milliseconds`  

Units to be used for the threshold values.

---

### units

**Type**: String  
**Path**: `qos_profiles.[].uc_tx_queues.[].random_detect.ecn.threshold.units`  
**Valid Values**: `segments`, `bytes`, `kbytes`, `mbytes`, `milliseconds`  

Unit to be used for the threshold values.

---

### units

**Type**: String  
**Path**: `qos_profiles.[].uc_tx_queues.[].random_detect.drop.threshold.units`  
**Valid Values**: `segments`, `bytes`, `kbytes`, `mbytes`, `microseconds`, `milliseconds`  

Units to be used for the threshold values.

---

### unsupported_error_correction_action

**Type**: String  
**Path**: `system.l1.unsupported_error_correction_action`  
**Valid Values**: `error`, `warn`  
---

### unsupported_speed_action

**Type**: String  
**Path**: `system.l1.unsupported_speed_action`  
**Valid Values**: `error`, `warn`  
---

## V

### version

**Type**: Integer  
**Path**: `ethernet_interfaces.[].vrrp_ids.[].ipv4.version`  
**Valid Values**: `2`, `3`  
---

### version

**Type**: Integer  
**Path**: `monitor_telemetry_postcard_policy.ingress.collection.version`  
**Valid Values**: `1`, `2`  

Postcard version.

---

### version

**Type**: Integer  
**Path**: `port_channel_interfaces.[].vrrp_ids.[].ipv4.version`  
**Valid Values**: `2`, `3`  
---

### version

**Type**: String  
**Path**: `snmp_server.groups.[].version`  
**Valid Values**: `v1`, `v2c`, `v3`  
---

### version

**Type**: String  
**Path**: `snmp_server.users.[].version`  
**Valid Values**: `v1`, `v2c`, `v3`  
---

### version

**Type**: String  
**Path**: `snmp_server.hosts.[].version`  
**Valid Values**: `1`, `2c`, `3`  
---

### version

**Type**: Integer  
**Path**: `vlan_interfaces.[].vrrp_ids.[].ipv4.version`  
**Valid Values**: `2`, `3`  
---

### vlan_tag

**Type**: String  
**Path**: `ethernet_interfaces.[].switchport.dot1q.vlan_tag`  
**Valid Values**: `disallowed`, `required`  

Allow/disallow VLAN tagged frames.

---

### vlan_tag

**Type**: String  
**Path**: `port_channel_interfaces.[].switchport.dot1q.vlan_tag`  
**Valid Values**: `disallowed`, `required`  
---

### VRF

**Type**: String  
**Path**: `ip_tacacs_source_interfaces.[].vrf`  
---

### vrfs

**Type**: List, items: Dictionary  
**Path**: `vrfs`  

These keys are ignored if the name of the vrf is 'default'.


---

### vtep_mac_learning

**Type**: String  
**Path**: `cvx.services.vxlan.vtep_mac_learning`  
**Valid Values**: `control-plane`, `data-plane`  
---

### vxlan

**Type**: String  
**Path**: `traffic_policies.policies.[].matches.[].packet_type.vxlan`  
**Valid Values**: `decap`, `decap exclude`  

Configure VXLAN decapsulation match.

---
