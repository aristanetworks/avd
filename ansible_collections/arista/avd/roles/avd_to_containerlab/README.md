AVD to containerlab
=========

Role to build a [containerlab](https://containerlab.srlinux.dev/) topology from [Arista AVD](https://www.avd.sh) project

Requirements
------------

- Arista AVD set of variables

Role Variables
--------------

- `containerlabs_configuration`: Location and name of the containerlabs configuration generated. (default: `{{ inventory_dir }}/containerlabs.yml`)
- `ceos_version`: Version of cEOS to use for the topology (default: 4.25.2F)
- `mgmt_network_v4`: Subnet for management IPs use for OOB

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

```yaml
---
- name: Build containerlab topology
  hosts: DC1_FABRIC
  connection: local
  gather_facts: false
  collections:
    - inetsix.avd_tools
  tasks:
    - name: 'Build a containerlab topolgy'
      import_role:
        name: inetsix.avd_tools.avd_to_containerlab
      vars:
        mgmt_network_v4: 10.73.0.0/16
        ceos_version: arista/ceos:4.25.2F
```

License
-------

Apache 2
