# Testing Playbooks

Current folder centralizes a set of playbooks and inventories to validate Arista Validated Design along the development path.

Each time a new feature is added to the collection, a test playbook and inventory should be created. Thus, it will allow to validate any other change won't break feature with come additional development.

```yaml
testing
├── README.md
└── avd-eos-only-generic
    ├── ansible.cfg
    ├── documentation
    ├── group_vars
    ├── intended
    ├── inventory.yml
    └── playbook-validation.yml

4 directories, 4 files
```

During each CI run, script [`run-test-playbooks`](../.github/run-test-playbooks) is launched and detects every scenario to run playbook accordingly.

```shell
sh .github/run-test-playbooks
Run Test playbooks for AVD validation
  * found test avd-eos-only-generic
    * running test playbook: playbook-validation.yml

PLAY [DC1_FABRIC] ************
[...]
```

A specific command is available in [`Makefile`](../Makefile) to run command from any local environment and validate this CI step locally.

```shell
$ make playbook-validation
sh .github/run-test-playbooks
Run Test playbooks for AVD validation
  * found test avd-eos-only-generic
    * running test playbook: playbook-validation.yml
```
