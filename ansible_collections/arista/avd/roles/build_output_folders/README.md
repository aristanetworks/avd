# Build Output Folders

Role to cleanup and create local folder structure to save roles' outputs

## Requirements

None

## Role Variables

Role support following variables:

```yaml
# Root directory where to build output structure
root_dir: '{{playbook_dir}}'
# Main output directory
output_dir_name: 'intended'
# Output for structured YAML files:
structured_dir_name: 'structured_configs'
# EOS Configuration Directory name
eos_config_dir_name: 'configs'
# Main documentation folder
documentation_dir_name: 'documentation'
# Fabric Documentation
fabric_dir_name: 'DC1_FABRIC'
# Device documentation
devices_dir_name: 'devices'
```

Role will create following structure:

```
intended
├── configs
└── structured_configs
|
documentation
├── DC1_FABRIC
└── devices
```

If folders already exists, role will delete them and recreate structure.

## Dependencies

None

## Example Playbook

Below is an example to use in your playbook to build output folders using default values.

```yaml
- name: Build Switch configuration
  hosts: DC1_FABRIC
  connection: local
  gather_facts: no
  tasks:
    - name: 'Reset local folders for output'
      tags: [build]
      import_role:
        name: arista.avd.build_output_folders
```

## License

Project is published under [Apache 2.0 License](../../../../../LICENSE)

