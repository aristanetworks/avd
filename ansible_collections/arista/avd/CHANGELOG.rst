========================
Arista.Avd Release Notes
========================

.. contents:: Topics


v3.5.0
======

Release Summary
---------------

Release 3.5.0 - See documentation on avd.sh for details.


Minor Changes
-------------

- Bump(requirements) - Relax ansible.netcommon requirements to ">=2.4.0,!=2.6.0" (https://github.com/aristanetworks/ansible-avd/pull/6)
- Doc - Fix typo in release-notes for v3.4.0 (https://github.com/aristanetworks/ansible-avd/pull/8)
- Doc - Improve documentation, fix typo (https://github.com/aristanetworks/ansible-avd/pull/9)
- Doc - Minor Corrections on Documentation (https://github.com/aristanetworks/ansible-avd/pull/1)
- Doc - Network services data model in v4.0 mpls docs (https://github.com/aristanetworks/ansible-avd/pull/4)
- Doc - Remove CI badge (https://github.com/aristanetworks/ansible-avd/pull/6)
- Doc - Update links to github documentation (https://github.com/aristanetworks/ansible-avd/pull/3)
- Doc(eos_cli_config_gen) - Improve documentation for router_general (https://github.com/aristanetworks/ansible-avd/pull/9)
- Doc(eos_designs) - add precisions regarding eos_designs and eos_cli_config_gen variables (https://github.com/aristanetworks/ansible-avd/pull/3)
- Feat(eos_cli_config_gen) - Add BGP listen-range to VRF (https://github.com/aristanetworks/ansible-avd/pull/9)
- Feat(eos_cli_config_gen) - Add BGP neighbor interfaces in VRF (https://github.com/aristanetworks/ansible-avd/pull/7)
- Feat(eos_cli_config_gen) - Add Tap Aggregation support (https://github.com/aristanetworks/ansible-avd/pull/7)
- Feat(eos_cli_config_gen) - Add eos_cli for loopback_interfaces (https://github.com/aristanetworks/ansible-avd/pull/7)
- Feat(eos_cli_config_gen) - Add eos_cli for loopback_interfaces (https://github.com/aristanetworks/ansible-avd/pull/7)
- Feat(eos_cli_config_gen) - Add management_api_models (https://github.com/aristanetworks/ansible-avd/pull/4)
- Feat(eos_cli_config_gen) - Add sflow interface disable default command (https://github.com/aristanetworks/ansible-avd/pull/3)
- Feat(eos_cli_config_gen) - Add support for authenticating only ntp servers (https://github.com/aristanetworks/ansible-avd/pull/0)
- Feat(eos_cli_config_gen) - Add support for multiple dot1x interface features (https://github.com/aristanetworks/ansible-avd/pull/9)
- Feat(eos_cli_config_gen) - Added support for CVX client (https://github.com/aristanetworks/ansible-avd/pull/2)
- Feat(eos_cli_config_gen) - Adding support for ssl profile for gnmi (https://github.com/aristanetworks/ansible-avd/pull/7)
- Feat(eos_cli_config_gen) - Aegis Traffic Policies on Interfaces (https://github.com/aristanetworks/ansible-avd/pull/8)
- Feat(eos_cli_config_gen) - BGP VRF IPv4 RM support (https://github.com/aristanetworks/ansible-avd/pull/3)
- Feat(eos_cli_config_gen) - Extend listen_range support for BGP (https://github.com/aristanetworks/ansible-avd/pull/5)
- Feat(eos_cli_config_gen) - Extend logging format timestamp options (https://github.com/aristanetworks/ansible-avd/pull/9)
- Feat(eos_cli_config_gen) - Support Aboot password (https://github.com/aristanetworks/ansible-avd/pull/1)
- Feat(eos_cli_config_gen) - Support for multiple VARPv6 addresses (https://github.com/aristanetworks/ansible-avd/pull/1)
- Feat(eos_cli_config_gen) - Support interfaces snmp trap link-change (https://github.com/aristanetworks/ansible-avd/pull/3)
- Feat(eos_cli_config_gen) - Support platfom sand qos-mapping (https://github.com/aristanetworks/ansible-avd/pull/6)
- Feat(eos_cli_config_gen) - Support remove-private-as in router_bgp (https://github.com/aristanetworks/ansible-avd/pull/6)
- Feat(eos_cli_config_gen) - VRRP timer delay and IPv4 version options (https://github.com/aristanetworks/ansible-avd/pull/6)
- Feat(eos_cli_config_gen) - add SNMPv3 hashed user passphrases support (https://github.com/aristanetworks/ansible-avd/pull/1)
- Feat(eos_cli_config_gen) - add VRRP support for object tracking (https://github.com/aristanetworks/ansible-avd/pull/7)
- Feat(eos_cli_config_gen) - dot1x-pae-mode (https://github.com/aristanetworks/ansible-avd/pull/2)
- Feat(eos_cli_config_gen) - dot1x-reauthentication (https://github.com/aristanetworks/ansible-avd/pull/0)
- Feat(eos_config_deploy_cvp) - support for !vault value in inventory file (https://github.com/aristanetworks/ansible-avd/pull/9)
- Feat(eos_designs) - Add ability to set mlag port-channel id (https://github.com/aristanetworks/ansible-avd/pull/9)
- Feat(eos_designs) - Add platform settings for 7368X4 (https://github.com/aristanetworks/ansible-avd/pull/0)
- Feat(eos_designs) - Auto short_esi support for connected_endpoints and l2leaf uplinks (#1609) (https://github.com/aristanetworks/ansible-avd/pull/8)
- Feat(eos_designs) - Custom name for underlay isis process (https://github.com/aristanetworks/ansible-avd/pull/1)
- Feat(eos_designs) - EVPN VXLAN gateway feature (https://github.com/aristanetworks/ansible-avd/pull/1)
- Feat(eos_designs) - Enable RTC for EVPN-OVERLAY-CORE peer group (https://github.com/aristanetworks/ansible-avd/pull/5)
- Feat(eos_designs) - RFC5549 for MLAG iBGP in VRF (https://github.com/aristanetworks/ansible-avd/pull/8)
- Feat(eos_designs) - RFC5549 support for core_interfaces (https://github.com/aristanetworks/ansible-avd/pull/1)
- Feat(eos_designs) - Shutdown underlay links if the peer device is not deployed (https://github.com/aristanetworks/ansible-avd/pull/5)
- Feat(eos_designs) - Support evpn hostflap detection expiry (https://github.com/aristanetworks/ansible-avd/pull/3)
- Feat(eos_designs) - Support for IPv6 in underlay with RFC5549 (https://github.com/aristanetworks/ansible-avd/pull/3)
- Feat(eos_designs) - Support for IPv6 overlay peerings with RFC5549 underlay (https://github.com/aristanetworks/ansible-avd/pull/9)
- Feat(eos_designs) - Support for Ipv6 network services (https://github.com/aristanetworks/ansible-avd/pull/0)
- Feat(eos_designs, eos_cli_config_gen) - Support default-services in management-api-http (https://github.com/aristanetworks/ansible-avd/pull/4)
- Feat(eos_designs, eos_cli_config_gen) - Support default-services in management-api-http (https://github.com/aristanetworks/ansible-avd/pull/4)
- Feat(plugins) - Updated convert_dicts filter for list values in dictionary (https://github.com/aristanetworks/ansible-avd/pull/4)
- Feat(plugins) - Updated convert_dicts filter for list/string values in dictionary (https://github.com/aristanetworks/ansible-avd/pull/0)

Bugfixes
--------

- Fix(eos_cli_config_gen) - Adjust the address-family evpn host-flap detection (https://github.com/aristanetworks/ansible-avd/pull/8)
- Fix(eos_cli_config_gen) - Documentation template for IPv6 on port-channels (https://github.com/aristanetworks/ansible-avd/pull/5)
- Fix(eos_cli_config_gen) - Render error-correction encoding on port-channel members (https://github.com/aristanetworks/ansible-avd/pull/0)
- Fix(eos_designs) - Error in eos_designs_facts when dot in hostname (https://github.com/aristanetworks/ansible-avd/pull/6)
- Fix(eos_designs) - Fix IPv6 static routes tenants (https://github.com/aristanetworks/ansible-avd/pull/8)
- Fix(eos_designs) - ipv6_underlay should not apply for l2 switches (https://github.com/aristanetworks/ansible-avd/pull/2)
- Fix(plugins) - convert_dicts resolve corner case with dictionary with invalid value (https://github.com/aristanetworks/ansible-avd/pull/7)

New Modules
-----------

- arista.avd.eos_designs_facts - Set eos_designs facts
