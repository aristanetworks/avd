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
    # If "disabled" is true, the user will be removed and all other settings are ignored.
    # Useful for removing the default "admin" user.
    disabled: < true | false >

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

# On-premise CVP ingest auth key | Optional
# If set, terminattr will be configured with key-based authentication for on-premise CVP.
# If not set, terminattr will be configured with certificate based authentication using token-secure onboarding.
# Token must be copied to the device first.
cvp_ingestauth_key: < CloudVision Ingest Authentication key >
cvp_token_file: < 'path_to_token_file_on_switch' | default -> '/tmp/cv-onboarding-token' >
terminattr_ingestgrpcurl_port: < port_number | default -> 9910 >
terminattr_smashexcludes: "< smash excludes | default -> ale,flexCounter,hardware,kni,pulse,strata >"
terminattr_ingestexclude: "< ingest excludes | default -> /Sysdb/cell/1/agent,/Sysdb/cell/2/agent >"
terminattr_disable_aaa: "< boolean | default -> false >"

# Management interface configuration | Optional
mgmt_vrf_routing: < boolean | default -> false >
mgmt_interface: < mgmt_interface | default -> Management1 >
mgmt_interface_vrf: < vrf_name | default -> MGMT >
mgmt_interface_description: < description | default -> "oob_management" >
mgmt_gateway: < IPv4 address >
ipv6_mgmt_gateway: < IPv6 address >
# OOB mgmt interface destination networks - override default route
mgmt_destination_networks:
  - < IPv4_network/Mask >
  - < IPv4_network/Mask >
# OOB mgmt interface destination ipv6 networks - override default route
ipv6_mgmt_destination_networks:
  - < IPv6_network/Mask >
  - < IPv6_network/Mask >

# list of DNS servers | Optional
name_servers:
  - < IPv4_address_1 >
  - < IPv4_address_2 >

# System Mac Address | Optional
# Set to the same MAC address as available in "show version" on the device.
# "system_mac_address" can also be set under "Fabric Topology".
# If both are set, the setting under "Fabric Topology" takes precedence.
system_mac_address: < "xx:xx:xx:xx:xx:xx" >

# Serial Number | Optional
# Set to the Serial Number of the device
# For  now only used for documentation purpose in the fabric
# documentation.
# "serial_number" can also be set under "Fabric Topology".
# If both are set, the setting under "Fabric Topology" takes precedence.
serial_number: < string >

# Set SNMP settings | Optional
snmp_settings:
  contact: < contact_info >
  location: < boolean | default -> false > # Formatted as: {{ fabric_name }} {{ dc_name }} {{ pod_name }} {{ switch_rack }} {{ inventory_hostname }}
  # Generate a local engineId for SNMP using the compute_local_engineid_source method
  compute_local_engineid: < boolean | default -> false >
  # `compute_local_engineid_source` supports:
  # * 'hostname_and_ip': Generate a local engineId for SNMP by hashing via SHA1
  #                      the string generated via the concatenation of the hostname plus the management IP.
  #                      {{ inventory_hostname }} + {{ switch.mgmt_ip }}
  # * `system_mac`:  Generate the switch default engine id for AVD usage
  #                  To use this, `system_mac_address` MUST be set for the device
  #                  The formula is f5717f + system_mac_address + 00
  # default is `hostname_and_ip`
  compute_local_engineid_source: < hostname_and_ip | system_mac | default -> hostanme_and_ip >
  # Requires compute_local_engineid to be `true` if enabled, the SNMPv3
  # passphrases for auth and priv are transfromed using RFC 2574,
  # matching the value they would take in EOS cli the algorithm requires
  # a local engineId which is unknown to AVD hence the necessity to generate
  # one beforehand.
  compute_v3_user_localized_key: < boolean | default -> false >
  users:
    - name: < username >
      group: < group >
      version: < v1 | v2c | v3 >
      auth: < md5 | sha | sha256 | sha384 | sha512 > # optional
      auth_passphrase: < clear_passphrase >          # requires auth, recommended to use vault
      priv: < des | aes | aes192 | aes256 >          # optional
      priv_passphrase: < clear_pasphrase >           # requires priv, recommended to use vault
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
