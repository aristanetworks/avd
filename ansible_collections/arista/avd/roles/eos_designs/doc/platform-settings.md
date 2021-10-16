# Platform Specific settings

- Set platform specific settings, TCAM profile and reload delay.
- The reload delay values should be reviewed and tuned to the specific environment.
- If the platform is not defined, it will load parameters from the platform tagged `default`.

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
  - platforms: [ default ]
    reload_delay:
      mlag: 300
      non_mlag: 330
    feature_support:
      # "queue-monitor length notify" is only valid for R-Series so should be disabled on default platform.
      queue_monitor_length_notify: false
      interface_storm_control: false
  - platforms: [ 7280R, 7280R2, 7500R, 7500R2 ]
    tcam_profile: vxlan-routing
    lag_hardware_only: true
    reload_delay:
      mlag: 900
      non_mlag: 1020
  - platforms: [ 7280R3, 7500R3, 7800R3 ]
    reload_delay:
      mlag: 900
      non_mlag: 1020
  - platforms: ["VEOS", "VEOS-LAB"]
    reload_delay:
      mlag: 300
      non_mlag: 330
    feature_support:
      queue_monitor_length_notify: false
      interface_storm_control: false
```
