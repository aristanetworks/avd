eos-config-deploy-cvp
=========

__eos-config-deploy-cvp__ is a module in charge of publishing AVD configuration to a CloudVision instance.

Requirements
------------

To use this role, you must follow next requirements:

- arista.cvp collection

```
$ ansible-galaxy collection install arista.cvp
```

- Python libraies:

```
$ pip install ansible>=2.9.0rc4,<2.10
$ pip install requests==2.22.0
$ pip install treelib==1.5.5
```

Role Variables
--------------

Some variables are used to capture customer's inputs:

- Filter to apply on cv_device to target only devices involved in Fabric

```yaml
device_filter: 'all'
```

- Define inventory group to consider root of container topology
```yaml
container_root: '{{ fabric_name }}'
```

- Configure prefix to append to configlets on CloudVision
```yaml
configlets_prefix: 'AVD-{{ fabric_name }}-'
```

- Define whether Ansible must create/update or delete CloudVision topology
```yaml
state: present
```

Dependencies
------------

- arista.cvp collection

```
$ ansible-galaxy collection install arista.cvp
```

Inventory file must use `YAML` syntax and have at least one group named __CVP__


Example Playbook
----------------

Below is an example of how to use this role to create topology on CloudVision:

```yaml
- name: Configuration deployment with CVP
  hosts: CVP
  connection: local
  gather_facts: no
  tasks:
    - name: run CVP provisioning
      import_role:
         name: eos-config-deploy-cvp
      vars:
        container_root: DC1
        configlets_prefix: 'DC1-AVD'
        device_filter: 'A-'
        state: present
```

Below is an example of how to use this role to delete topology on CloudVision:

```yaml
- name: Configuration deployment with CVP
  hosts: CVP
  connection: local
  gather_facts: no
  tasks:
    - name: run CVP provisioning
      import_role:
         name: eos-config-deploy-cvp
      vars:
        container_root: DC1
        configlets_prefix: 'DC1-AVD'
        device_filter: 'A-'
        state: absent
```


License
-------

BSD

Author Information
------------------

An optional section for the role authors to include contact information, or a website (HTML is not allowed).
