# AVD Upgrade Tools 2.x.x to 3.x.x

This role can be used to upgrade AVD data model structures to facilitate the upgrade path for **major** releases of ansible avd.
The role focuses on updating data structure for abstracted data model roles only, i.e. eos_designs.

The output will be saved in `{{ inventory_dir }}/upgrade_2.x_to_3.0` directory.
You then need to replace the old data structures manually in `group_vars/host_vars`.

### Example Playbook

```yaml
---

- hosts: DC1_FABRIC
  tasks:
    - name: convert data model from 2.x to 3.0
      import_role:
        name: arista.avd.upgrade_tools
```

## Requirements

Requirements are located here: [avd-requirements](../../README.md#Requirements)

## License

Project is published under [Apache 2.0 License](../../LICENSE)
