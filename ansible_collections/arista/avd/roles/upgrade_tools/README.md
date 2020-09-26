# AVD Upgrade Tools

This role can be used to upgrade AVD data model structures to facilate the upgrade path for **major** or **minor** releases of ansible avd.
The role focuses on updating data structure for abstrated data model roles only, i.e. eos_l3ls_evpn.

## AVD 1.0.x to 1.1.x

- `subset: v1.0_to_v1.1`

Leveraged to update data model for tenants networks services definition from 1.0 to 1.1.
Following data structures will be upgraded:

- `./group_vars/{{ ??_TENANTS_NETWORKS }}.yml`

The output will be saved in ./upgrade_1.0_to_1.1 directory. You can then replace old data structures manually or add that into the playbook.

### Example Playbook

To translate the data, provide the list of `{{ ??_TENANTS_NETWORKS }}.yml` files in group_vars directory:

```yaml
---

- hosts: DC1_FABRIC
  tasks:
    - name: upgrade data model
      include_role:
        name: arista.avd.upgrade_tools
      vars:
        subset: 'v1.0_to_v1.1'
      loop:
        - DC1_TENANTS_NETWORKS.yml
```

## Requirements

Requirements are located here: [avd-requirements](../../README.md#Requirements)

## License

Project is published under [Apache 2.0 License](../../LICENSE)
