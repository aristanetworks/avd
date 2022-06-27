# Platform Specific settings

- Set platform specific settings, TCAM profile and reload delay.
- The reload delay values should be reviewed and tuned to the specific environment.
- If the platform is not defined, it will load parameters from the platform tagged `default`.
- Management interface is modified for specific platforms: Modular platforms with dual supervisor support and container EOS.
- Set default uplink, downlink and mlag interfaces which will be used if these interfaces are not defined on a device (either directly or through inheritance).
  - This is specified as a list of interfaces
  - Each list item supports range syntax. Interface range examples:
    - Ethernet49-52/1: Expands to [ Ethernet49/1, Ethernet50/1, Ethernet51/1, Ethernet52/1 ]
    - Ethernet1/31-34/1: Expands to [ Ethernet1/31/1, Ethernet1/32/1, Ethernet1/33/1, Ethernet1/34/1 ]
    - Ethernet49-50,53-54: Expands to [ Ethernet49, Ethernet50, Ethernet53, Ethernet54 ]
    - Ethernet1-2/1-4: Expands to [ Ethernet1/1, Ethernet1/2, Ethernet1/3, Ethernet1/4, Ethernet2/1, Ethernet2/2, Ethernet2/3, Ethernet2/4 ]
  - Range syntaxes are expanded into a list of interfaces.
  - `default_uplink_interfaces` and `default_mlag_interfaces` are directly inherited to `uplink_interfaces` and `mlag_interfaces`.
  - `default_downlink_interfaces` are referenced by the child switch (e.g. the leaf in a leaf/spine network). Essentially the child switch indexes into an upstream switch's `default_downlink interfaces` using the child switch ID.  This is then used to build `uplink_switch_interfaces` for that child.
    - In the case of `max_parallel_uplinks` > 1 the `default_downlink_interfaces` are mapped with consecutive downlinks per child ID.
    - Example for `max_parallel_uplinks: 2`, downlink interfaces will be mapped as `[ <downlink1 to leaf-id1>, <downlink2 to leaf-id1>, <downlink1 to leaf-id2>, <downlink2 to leaf-id2> ...]`
  - Please note that no default interfaces are defined in the default `platform_settings`. You will need to override the defaults and create your own.

## Variables and Options

```yaml
platform_settings:
  - platforms: [ default ]
    reload_delay:
      mlag: < seconds >
      non_mlag: < seconds >
  - platforms: [ < Arista Platform Family >, < Arista Platform Family > ]
    tcam_profile: < tcam_profile >
    lag_hardware_only: < true | false >
    feature_support:
      queue_monitor_length_notify: < true | false | default -> true >
      interface_storm_control: < true | false | default -> true >
    # Optional - Set default uplink, downlink and mlag interfaces.  If these interfaces are not defined on a device (either directly or through inheritance)
    default_uplink_interfaces: [ < interface_range | interface > ]
    default_downlink_interfaces: [ < interface_range | interface > ]
    default_mlag_interfaces: [ < interface_range | interface > ]
    management_interface: < management interface name | default -> Management1 >
    reload_delay:
      mlag: < seconds >
      non_mlag: < seconds >
    # EOS CLI rendered directly on the root level of the final EOS configuration
    raw_eos_cli: |
      < multiline eos cli >

# Set Hardware Speed Groups per Platform
platform_speed_groups:
  < platform >:
    < speed >: [ < speed_group >, < speed_group > ]

# Redundancy for chassis platforms with dual supervisors | Optional
redundancy:
  protocol: < sso | rpr >
```

note:
Recommended default values for Jericho based platform, VEOS and all other platforms `default` tag.
The reload delay values should be reviewed and tuned to the specific environment.

## Default Values

```yaml
platform_settings:
  - platforms: [ 'default' ]
    reload_delay:
      mlag: 300
      non_mlag: 330
    feature_support:
      # "queue-monitor length notify" is only valid for R-Series so should be disabled on default platform.
      queue_monitor_length_notify: false
  - platforms: [ '7280R', '7280R2' ]
    tcam_profile: vxlan-routing
    lag_hardware_only: true
    reload_delay:
      mlag: 900
      non_mlag: 1020
  - platforms: [ '7280R3' ]
    reload_delay:
      mlag: 900
      non_mlag: 1020
  - platforms: [ '7500R', '7500R2' ]
    tcam_profile: vxlan-routing
    lag_hardware_only: true
    management_interface: Management0
    reload_delay:
      mlag: 900
      non_mlag: 1020
  - platforms: [ '7500R3', '7800R3' ]
    management_interface: Management0
    reload_delay:
      mlag: 900
      non_mlag: 1020
  - platforms: [ '7368X4' ]
    management_interface: Management0
    reload_delay:
      mlag: 300
      non_mlag: 330
  - platforms: [ 'VEOS', 'VEOS-LAB', 'vEOS', 'vEOS-lab' ]
    reload_delay:
      mlag: 300
      non_mlag: 330
    feature_support:
      queue_monitor_length_notify: false
      interface_storm_control: false
  - platforms: [ 'CEOS', 'cEOS', 'ceos', 'cEOSLab' ]
    management_interface: Management0
    reload_delay:
      mlag: 300
      non_mlag: 330
    feature_support:
      queue_monitor_length_notify: false
      interface_storm_control: false
```
