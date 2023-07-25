# arista.avd.eos_designs_structured_config

Generate AVD EOS Designs structured configuration

## Synopsis

Validates input variables according to eos\_designs schema

Generates structured configuration

Optionally run any custom jinja2 YAML templates and merge result onto structured configuration

Optionally run jinja2 templating the generated structured configuration

Optionally write structured configuration to a JSON or YAML file

Return structured configuration as \"ansible\_facts\"

## Parameters

  eos_designs_custom_templates (False, list, None)
    List of dicts for Jinja2 templates to be run after generating the structured configuration

    template (True, str, None)
      Template file\.


    options (False, dict, None)
      Template options

      list_merge (False, str, append)
        Merge strategy for lists

      strip_empty_keys (False, bool, True)
        Filter out keys from the generated output if value is null/none/undefined
        Only applies to templates\.

  dest (False, str, None)
    Destination path\. If set\, the output facts will also be written to this path\.
    Autodetects data format based on file suffix\. \'\.yml\'\, \'\.yaml\' \-\> YAML\, default \-\> JSON

  mode (False, str, None)
    File mode \(ex\. 0664\) for dest file\. See \'ansible\.builtin\.copy\' module for details\.

  template_output (False, bool, None)
    If true the output data will be run through another jinja2 rendering before returning\.
    This is to resolve any input values with inline jinja using variables/facts set by the input templates\.

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
- name: Generate device configuration in structured format
  arista.avd.eos_designs_structured_config:
    templates:
      - template: "custom_templates/custom_feature1.j2"
      - template: "custom_templates/custom_feature2.j2"
        options:
          list_merge: replace
          strip_empty_keys: false
  check_mode: no
  changed_when: False
```

## Status

## Authors

- Arista Ansible Team (@aristanetworks)
