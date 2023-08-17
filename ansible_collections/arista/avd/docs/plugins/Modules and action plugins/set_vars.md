# set_vars

!!! note
    Always use the FQCN (Fully Qualified Collection Name) `arista.avd.set_vars` when using this plugin.

Set vars as ansible\_facts.

## Synopsis

Set vars as ansible\_facts.

Ansible will copy these into vars in the global namespace as well.

Arguments are treated as one dict so all arguments will be set as vars.

## Examples

```yaml
- name: Remove avd_switch_facts
  tags: [build, provision, facts, remove_avd_switch_facts]
  arista.avd.set_vars:
    avd_switch_facts: null
  run_once: true
  check_mode: false
```

## Status

## Authors

- Arista Ansible Team (@aristanetworks)
