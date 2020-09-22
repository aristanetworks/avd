# Ansible Role: eos_config_deploy_eapi

**Table of Contents:**

- [Ansible Role: eos_config_deploy_eapi](#ansible-role-eos_config_deploy_eapi)
  - [Overview](#overview)
  - [Role Inputs and Outputs](#role-inputs-and-outputs)
  - [Default Variables](#default-variables)
  - [Requirements](#requirements)
  - [License](#license)

## Overview

**eos_config_deploy_eapi**, is a role that deploys the configuration to Arista EOS devices.

The **eos_config_deploy_eapi** role:

- Designed to replace device running-configuration with intended configuration.
- Backup configuration after successfully change.

## Role Inputs and Outputs

Figure 1 below provides a visualization of the roles inputs, and outputs and tasks in order executed by the role.

![Figure 1: Ansible Role eos_config_deploy_eapi](media/role_eos_config_deploy_eapi.gif)

**Inputs:**

- Device configuration file in EOS CLI syntax.

**Outputs:**

- Device running-configuration before configuration is replaced (snapshot).
- Device running-configuration after configuration is replaced (backup).

**Tasks:**

1. Take a snapshop of the running configuration before configuration is replaced - (optional, default false).
2. Replace configuration on device with intended EOS configuration. If changed, saves to startup-config, and notifies handler to backup configuration.
3. Backup Configuration: `./config_backup/{{ inventory_hostname }}.cfg` (handler).

## Default Variables

```yaml
# Peform config snapshop before config replace

eos_config_deploy_eapi_snapshot: false

# Root directory where to build output structure
root_dir: '{{ inventory_dir }}'


# Directory Path and filename
running_config_backup_filename: "{{ inventory_hostname }}_running-config.conf"
running_config_backup_dir_name: 'config_backup'
running_config_backup_dir: '{{ root_dir }}/{{ running_config_backup_dir_name }}'

running_config_snapshot_filename: "{{ inventory_hostname }}_pre_running-config.conf"
running_config_snapshot_dir_name: 'config_backup'
running_config_snapshot_dir: '{{ root_dir }}/{{ running_config_snapshot_dir_name }}'
```

## Requirements

Requirements are located here: [avd-requirements](../../README.md#Requirements)

## License

Project is published under [Apache 2.0 License](../../LICENSE)
