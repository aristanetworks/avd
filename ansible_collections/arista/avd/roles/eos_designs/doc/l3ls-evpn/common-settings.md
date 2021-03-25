# Common Settings

## Common Device Configuration Variables

- Common device configuration variables are for elements not related specifically to the fabric configuration.
- The variables should be applied to all devices within the fabric and can be shared with other infrastructure elements.

**Variables and Options:**

```yaml
# Clock timezone | Optional
timezone: < timezone >

# Dictionary of local users | Required
local_users:
  < username_1 >:
    privilege: < (1-15) Initial privilege level with local EXEC authorization >
    role: < Specify a role for the user >
    no_password: < true | do not configure a password for given username. sha512_password MUST not be defined for this user. >
    sha512_password: "< SHA512 ENCRYPTED password >"

  < username_2 >:
    privilege: < (1-15) Initial privilege level with local EXEC authorization >
    role: < Specify a role for the user >
    sha512_password: "< SHA512 ENCRYPTED password >"

# Management eAPI | Required
# Default is https management eAPI enabled
management_eapi:
  enable_http: < boolean | default -> false >
  enable_https: < boolean | default -> true >

# CloudVision - Telemetry Agent (TerminAttr) configuration | Optional
cvp_instance_ip: < IPv4 address >
or
cvp_instance_ips:
  - < IPv4 address >
  - < IPv4 address >
  - < IPv4 address >
  - < CV as a Service hostname >
cvp_ingestauth_key: < CloudVision Ingest Authentication key >
terminattr_ingestgrpcurl_port: < port_number | default -> 9910 >
terminattr_smashexcludes: "< smash excludes | default -> ale,flexCounter,hardware,kni,pulse,strata >"
terminattr_ingestexclude: "< ingest excludes | default -> /Sysdb/cell/1/agent,/Sysdb/cell/2/agent >"
terminattr_disable_aaa: "< boolean | default -> false >"


# Management interface configuration | Required
mgmt_vrf_routing: < boolean | default -> false >
mgmt_interface: < mgmt_interface | default -> Management1 >
mgmt_interface_vrf: < vrf_name | default -> MGMT >
mgmt_gateway: < IPv4 address >
# OOB mgmt interface destination networks - override default route
mgmt_destination_networks:
  - < IPv4_network/Mask >
  - < IPv4_network/Mask >

# list of DNS servers | Optional
name_servers:
 - < IPv4_address_1 >
 - < IPv4_address_2 >

# List of NTP Servers IP or DNS name | Optional
# The first NTP server in the list will be preferred
# NTP request will be sourced from < management_interface_vrf >
ntp_servers:
 - < ntp_server_1 >
 - < ntp_server_1 >

# Internal vlan allocation order and range | Required
internal_vlan_order:
  allocation: < ascending or descending | default -> ascending >
  range:
    beginning: < vlan_id | default -> 1006 >
    ending: < vlan_id | default -> 1199 >

# Redundancy for chassis platforms with dual supervisors | Optional
redundancy:
  protocol: < sso | rpr >

# MAC address-table aging time | Optional
# Use to change the EOS default of 300
mac_address_table:
  aging_time: < time_in_seconds >

# Set Hardware Speed Groups per Platform
platform_speed_groups:
  < platform >:
    < speed >: [ < speed_group >, < speed_group > ]

# Set SNMP settings | Optional
snmp_settings:
  contact: < contact_info >
  location: < boolean | default -> false > # Formatted as: {{ fabric_name }} {{ dc_name }} {{ pod_name }} {{ switch_rack }} {{ inventory_hostname }}
```

> In `cvp_instance_ips` you can either provide a list of IPs to target on-premise CloudVision cluster or either use DNS name for your CloudVision as a Service instance. If you have both on-prem and CVaaS defined, only on-prem is going to be configured.

**Example:**

note: Default values are commented

```yaml
# Timezone
timezone: "US/Eastern"

# local users
local_users:
  admin:
    privilege: 15
    role: network-admin
    sha512_password: "$6$Df86J4/SFMDE3/1K$Hef4KstdoxNDaami37cBquTWOTplC.miMPjXVgQxMe92.e5wxlnXOLlebgPj8Fz1KO0za/RCO7ZIs4Q6Eiq1g1"

  cvpadmin:
    privilege: 15
    role: network-admin
    sha512_password: "$6$rZKcbIZ7iWGAWTUM$TCgDn1KcavS0s.OV8lacMTUkxTByfzcGlFlYUWroxYuU7M/9bIodhRO7nXGzMweUxvbk8mJmQl8Bh44cRktUj."

# Management eAPI
# management_eapi:
#   enable_https: true

# Cloud Vision server information
cvp_instance_ips:
 - 192.168.2.201
 - 192.168.2.202
 - 192.168.2.203
cvp_ingestauth_key: telarista
# terminattr_ingestgrpcurl_port: 9910
# terminattr_smashexcludes: "ale,flexCounter,hardware,kni,pulse,strata"
# terminattr_ingestexclude: "/Sysdb/cell/1/agent,/Sysdb/cell/2/agent

# Management interface configuration
mgmt_gateway: 192.168.2.1
# mgmt_vrf_routing: false
# mgmt_interface: Management1
# mgmt_interface_vrf: MGMT
# OOB mgmt interface destination networks
# mgmt_destination_networks:
#   - 0.0.0.0/0

# DNS servers.
name_servers:
 - 192.168.2.1
 - 8.8.8.8

# NTP Servers
ntp_servers:
 - 0.north-america.pool.ntp.org
 - 1.north-america.pool.ntp.org

# Internal vlan allocation order and range
# internal_vlan_order:
#   allocation: ascending
#   range:
#     beginning: 1006
#     ending: 1199

# Redundancy for chassis platforms with dual supervisors
redundancy:
  protocol: sso

# MAC address-table aging time
mac_address_table:
  aging_time: 1500

# Set Hardware Speed Groups per Platform
platform_speed_groups:
  7280R2:
    25G: [ 1, 2, 12 ]
    10G: [ 3, 4, 5, 6, 7, 8, 9, 10, 11 ]
```

## Event Handlers

Gives ability to monitor and react to Syslog messages provides a powerful and flexible tool that can be used to apply self-healing actions, customize the system behavior, and implement workarounds to problems discovered in the field.

**Variables and Options:**

```yaml
event_handlers:
  evpn-blacklist-recovery:    # Name of the event-handler
    action_type: < bash, increment >
    action: < Command to run when handler is triggered >
    delay: < int / delay in sec between 2 triggers >
    trigger: < on-logging >
    regex:  < string to trigger handler >
    asynchronous: < true, false >

```

**Example:**

```yaml
event_handlers:
  evpn-blacklist-recovery:
    action_type: bash
    action: FastCli -p 15 -c "clear bgp evpn host-flap"
    delay: 300
    trigger: on-logging
    regex:  EVPN-3-BLACKLISTED_DUPLICATE_MAC
    asynchronous: true
```

## Platform Specific settings

- Set platform specific settings, TCAM profile and reload delay.
- The reload delay values should be reviewed and tuned to the specific environment.
- If the platform is not defined, it will load parameters from the platform tagged `default`.

**Variables and Options:**

```yaml
platform_settings:
  - platforms: [ default ]
    reload_delay:
      mlag: < seconds >
      non_mlag: < seconds >
  - platforms: [ < Arista Platform Family >, < Arista Platform Family > ]
    tcam_profile: < tcam_profile >
    lag_hardware_only: < true | false >
    reload_delay:
      mlag: < seconds >
      non_mlag: < seconds >

```

note: Recommended default values for Jericho based platform, and all other platforms `default` tag.

**Example:**

```yaml
platform_settings:
  - platforms: [ default ]
    reload_delay:
      mlag: 300
      non_mlag: 330
  - platforms: [ 7800R3, 7500R3, 7500R, 7280R3, 7280R2, 7280R ]
    tcam_profile: vxlan-routing
    lag_hardware_only: true
    reload_delay:
      mlag: 780
      non_mlag: 1020
```

## Custom EOS Structured Configuration

Custom EOS Structured Configuration keys can be set on any level using the name
of the corresponding `eos_cli_config_gen` key prefixed with content of `custom_structured_configuration_prefix`.
The content of Custom Structured Configuration variables will be combined with the structured config generated by the eos_designs role.
Lists are replaced. Dictionaries are updated. The combine is done recursively, so it is possible to update a sub-key of a variable set by
`eos_designs` role already.

 Example:

```yaml
custom_structured_configuration_name_server:
  nodes:
    - 10.2.3.4
custom_structured_configuration_ethernet_interfaces:
  Ethernet4000:
    description: My test
    ip_address: 10.1.2.3/12
    shutdown: false
    type: routed
    mtu: 1500
    peer: MY-own-peer
    peer_interface: Ethernet123
    peer_type: my_precious
```

In this example the contents of the `name_server.nodes` variable in the Structured Configuration will be replaced by the list `[ 10.2.3.4 ]`
and `Ethernet4000` will be added to the `ethernet_interfaces` dictionary in the Structured Configuration.

`custom_structured_configuration_prefix` allows the user to customize the prefix for Custom Structured Configuration variables.
Default value is `custom_structured_configuration_`. Remember to include any delimiter like the last `_` in this case.
It is possible to specify a list of prefixes, which will all be merged one by one. The order of merge will start from beginning of the list, which means that keys defined in the later prefixes will be able to override keys defined in previous ones.

```yaml
custom_structured_configuration_prefix: < variable_prefix, default -> "custom_structured_configuration_" >
#or
custom_structured_configuration_prefix: [ < variable_prefix_1 > , < variable_prefix_2 > , < variable_prefix_3 > ]
```

Example using multiple prefixes:

```yaml
custom_structured_configuration_prefix: [ my_dci_ , my_special_dci_ ]

my_dci_ethernet_interfaces:
  Ethernet4000:
    description: My test
    ip_address: 10.1.2.3/12
    shutdown: false
    type: routed
    mtu: 1500
    peer: MY-own-peer
    peer_interface: Ethernet123
    peer_type: my_precious

my_special_dci_ethernet_interfaces:
  Ethernet4000:
    ip_address: 10.3.2.1/21
```

In this example  `Ethernet4000` will be added to the `ethernet_interfaces` dictionary in the Structured Configuration and the ip_address will be `10.3.2.1/21` since ip_adddress was overridden on the later `custom_scructured_configuration_prefix`


## Variable to attach additional configlets

Role [`eos_config_deploy_cvp`](../../../eos_config_deploy_cvp/README.md#add-additional-configlets) provides an option to attach additional configlets to both devices or containers.

This function allows users to quickly deployed a new feature with no JINJA2 implementation. These configlets **must** be managed on CloudVision as current role does not upload additional containers.

To attach configlets to containers or devices, please refer to [**`eos_config_deploy_cvp` documentation**](../../../eos_config_deploy_cvp/README.md#add-additional-configlets)

Below is an example provided as-is:

```yaml
# group_vars/DC1_FABRIC.yml

# List of additional CVP configlets to bind to devices and containers
# Configlets MUST be configured on CVP before running AVD playbooks.
cv_configlets:
  containers:
    DC1_L3LEAFS:
      - GLOBAL-ALIASES
  devices:
    DC1-L2LEAF2A:
      - GLOBAL-ALIASES
    DC1-L2LEAF2B:
      - GLOBAL-ALIASES
```
