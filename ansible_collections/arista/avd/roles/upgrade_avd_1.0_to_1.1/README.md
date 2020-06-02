Role Name
=========

This role can be used to upgrade AVD data structures from 1.0 to 1.1 data model.
Following data structures will be upgraded:

- `./group_vars/{{ DC-name }}_TENANTS_NETWORKS.yml`

The output will be saved in ./upgrade_1.0_to_1.1 directory. You can then replace old data structures manually or add that into the playbook.

Requirements
------------

Requirements are located here: [avd-requirements](../../README.md#Requirements)

Example Playbook
----------------

To translate the data, provide the list of `{{ DC-name }}_TENANTS_NETWORKS.yml` files in group_vars directory:

```yaml
---
- name: upgrade
  hosts: localhost
  connection: local
  gather_facts: false
  collections:
    - arista.avd
  tasks:
    - name: upgrade
      include_role:
        name: upgrade_avd_1.0_to_1.1
      loop:
        - DC1_TENANTS_NETWORKS.yml
        - DC2_TENANTS_NETWORKS.yml
```

License
-------

BSD
