---
# This title is used for search results
title: arista.avd.eos_designs_structured_config
---
<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# eos_designs_structured_config

!!! note
    Always use the FQCN (Fully Qualified Collection Name) `arista.avd.eos_designs_structured_config` when using this plugin.

Generate AVD EOS Designs structured configuration

## Synopsis

The \`arista.avd.eos\_designs\_facts\` module is an Ansible Action Plugin providing the following capabilities\:

\- Validates input variables according to eos\_designs schema
\- Generates structured configuration
\- Optionally run any custom jinja2 YAML templates and merge result onto structured configuration
\- Optionally run jinja2 templating the generated structured configuration
\- Optionally write structured configuration to a JSON or YAML file
\- Return structured configuration as \"ansible\_facts\"

## Parameters

| Argument | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| eos_designs_custom_templates | list | False | None |  | List of dicts for Jinja2 templates to be run after generating the structured configuration |
|     template | str | True | None |  | Template file.
 |
|     options | dict | False | None |  | Template options |
|         list_merge | str | False | append |  | Merge strategy for lists |
|         strip_empty_keys | bool | False | True |  | Filter out keys from the generated output if value is null/none/undefined<br>Only applies to templates. |
| dest | str | False | None |  | Destination path. If set, the output facts will also be written to this path.<br>Autodetects data format based on file suffix. \'.yml\', \'.yaml\' \-\> YAML, default \-\> JSON |
| mode | str | False | None |  | File mode \(ex. 0664\) for dest file. See \'ansible.builtin.copy\' module for details. |
| template_output | bool | False | None |  | If true, the output data will be run through another jinja2 rendering before returning.<br>This is to resolve any input values with inline jinja using variables/facts set by the input templates. |
| conversion_mode | str | False | debug | Valid values:<br>- <code>error</code><br>- <code>warning</code><br>- <code>info</code><br>- <code>debug</code><br>- <code>quiet</code><br>- <code>disabled</code> | Run data conversion in either \"error\", \"warning\", \"info\", \"debug\", \"quiet\" or \"disabled\" mode.<br>Conversion will perform type conversion of input variables as defined in the schema.<br>Conversion is intended to help the user to identify minor issues with the input data, while still allowing the data to be validated.<br>During conversion, messages will be generated with information about the host\(s\) and key\(s\) which required conversion.<br>conversion\_mode\:disabled means that conversion will not run.<br>conversion\_mode\:error will produce error messages and fail the task.<br>conversion\_mode\:warning will produce warning messages.<br>conversion\_mode\:info will produce regular log messages.<br>conversion\_mode\:debug will produce hidden messages viewable with \-v.<br>conversion\_mode\:quiet will not produce any messages. |
| validation_mode | str | False | warning | Valid values:<br>- <code>error</code><br>- <code>warning</code><br>- <code>info</code><br>- <code>debug</code><br>- <code>disabled</code> | Run validation in either \"error\", \"warning\", \"info\", \"debug\" or \"disabled\" mode.<br>Validation will validate the input variables according to the schema.<br>During validation, messages will be generated with information about the host\(s\) and key\(s\) which failed validation.<br>validation\_mode\:disabled means that validation will not run.<br>validation\_mode\:error will produce error messages and fail the task.<br>validation\_mode\:warning will produce warning messages.<br>validation\_mode\:info will produce regular log messages.<br>validation\_mode\:debug will produce hidden messages viewable with \-v. |
| cprofile_file | str | False | None |  | Filename for storing cprofile data used to debug performance issues.<br>Running cprofile will slow down performance in it self, so only set this while troubleshooting. |

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

## Authors

- Arista Ansible Team (@aristanetworks)
