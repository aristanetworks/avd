# arista.avd.eos_designs_facts

Set eos\_designs facts

## Synopsis

The \`arista\.avd\.eos\_designs\_facts\` module is an Ansible Action Plugin providing the following capabilities

Set \`avd\_switch\_facts\` fact containing both \`switch\` facts per host\.

Set \`avd\_topology\_peers\` fact containing list of downlink switches per host\. This list is built based on the \`uplink\_switches\` from all other hosts\.

Set \`avd\_overlay\_peers\` fact containing list of EVPN or MPLS overlay peers per host\. This list is built based on the \`evpn\_route\_servers\` and \`mpls\_route\_reflectors\` from all other hosts\.

The plugin is designed to \`run\_once\`\. With this\, Ansible will set the same facts on all devices\, so all devices can lookup values of any other device without using the slower \`hostvars\`\.

The facts can also be copied to the \"root\" \`switch\` in a task run per\-device \(see example below\)

The module is used in \`arista\.avd\.eos\_designs\` to set facts for devices\, which are then used by jinja templates and python module in \`arista\.avd\.eos\_designs\` to generate the \`structured\_configuration\`\.

## Parameters

  template_output (False, bool, None)
    If true the output data will be run through another jinja2 rendering before returning\. This is to resolve any input values with inline jinja using variables/facts set by the input templates\.

  conversion_mode (False, str, debug)
    Run data conversion in either \"error\"\, \"warning\"\, \"info\"\, \"debug\"\, \"quiet\" or \"disabled\" mode\.
    Conversion will perform type conversion of input variables as defined in the schema\.
    Conversion is intended to help the user to identify minor issues with the input data\, while still allowing the data to be validated\.
    During conversion\, messages will be generated with information about the host\(s\) and key\(s\) which required conversion\.
    conversion\_mode\:disabled means that conversion will not run\.
    conversion\_mode\:error will produce error messages and fail the task\.
    conversion\_mode\:warning will produce warning messages\.
    conversion\_mode\:info will produce regular log messages\.
    conversion\_mode\:debug will produce hidden messages viewable with \-v\.
    conversion\_mode\:quiet will not produce any messages\.

  validation_mode (False, str, warning)
    Run validation in either \"error\"\, \"warning\"\, \"info\"\, \"debug\" or \"disabled\" mode\.
    Validation will validate the input variables according to the schema\.
    During validation\, messages will be generated with information about the host\(s\) and key\(s\) which failed validation\.
    validation\_mode\:disabled means that validation will not run\.
    validation\_mode\:error will produce error messages and fail the task\.
    validation\_mode\:warning will produce warning messages\.
    validation\_mode\:info will produce regular log messages\.
    validation\_mode\:debug will produce hidden messages viewable with \-v\.

  cprofile_file (False, str, None)
    Filename for storing cprofile data used to debug performance issues\.
    Running cprofile will slow down performance in it self\, so only set this while troubleshooting\.

## Examples

```yaml
---
- name: Set eos_designs facts
  tags: [build, provision, facts]
  arista.avd.eos_designs_facts:
    schema_id: eos_designs
  check_mode: False
  run_once: True

- name: Set eos_designs facts per device
  tags: [build, provision, facts]
  ansible.builtin.set_fact:
    switch: "{{ avd_switch_facts[inventory_hostname].switch }}"
  delegate_to: localhost
  changed_when: false
```

## Status

## Authors

- Arista Ansible Team (@aristanetworks)
