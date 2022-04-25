# Management Settings

## Common Settings

- Common Settings should be applied to all devices within the fabric and can be shared with other infrastructure elements.

### Variables and Options

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
    ssh_key: "< ssh_key_string >"

  < username_2 >:
    privilege: < (1-15) Initial privilege level with local EXEC authorization >
    role: < Specify a role for the user >
    sha512_password: "< SHA512 ENCRYPTED password >"

# Management eAPI | Optional
# Default is https management eAPI enabled
# The vrf is set to < mgmt_interface_vrf >
management_eapi:
  enable_http: < boolean | default -> false >
  enable_https: < boolean | default -> true >
  default_services: < boolean >

# CloudVision - Telemetry Agent (TerminAttr) configuration | Optional
# You can either provide a list of IPs to target on-premise CloudVision cluster or
# use DNS name for your CloudVision as a Service instance. If you have both on-prem and
# CVaaS defined, only on-prem is going to be configured.

cvp_instance_ip: < IPv4 address >
# or
cvp_instance_ips:
  - < IPv4 address >
  - < IPv4 address >
  - < IPv4 address >
  - < CV as a Service hostname >
# cvp_ingestauth_key is required for on-prem CVP
cvp_ingestauth_key: < CloudVision Ingest Authentication key >
# cvp_token_file is only applicable to CV as a Service
cvp_token_file: < 'path_to_token_file_on_switch' | default -> '/tmp/cv-onboarding-token' >
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

# Set SNMP settings | Optional
snmp_settings:
  contact: < contact_info >
  location: < boolean | default -> false > # Formatted as: {{ fabric_name }} {{ dc_name }} {{ pod_name }} {{ switch_rack }} {{ inventory_hostname }}
```

## Event Handlers

Gives ability to monitor and react to Syslog messages provides a powerful and flexible tool that can be used to apply self-healing actions, customize the system behavior, and implement workarounds to problems discovered in the field.

### Variables and Options

```yaml
event_handlers:
  < event_handler_name >:
    action_type: < bash, increment >
    action: < Command to run when handler is triggered >
    delay: < int / delay in sec between 2 triggers >
    trigger: < on-logging >
    regex:  < string to trigger handler >
    asynchronous: < true, false >
```

### Example for EVPN blacklist recovery

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
