---
# This title is used for search results
title: arista.avd.eos_designs_structured_config
---
<!--
  ~ Copyright (c) 2023-2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# eos_designs_structured_config

!!! note
    Always use the FQCN (Fully Qualified Collection Name) `arista.avd.eos_designs_structured_config` when using this plugin.

Generate AVD EOS Designs structured configuration

## Synopsis

The `arista.avd.eos_designs_structured_config` module is an Ansible Action Plugin providing the following capabilities:

- Generates structured configuration
- Optionally run any custom jinja2 YAML templates and merge result onto structured configuration
- Optionally run jinja2 templating the generated structured configuration
- Optionally write structured configuration to a JSON or YAML file
- Return structured configuration as &#34;ansible_facts&#34;

Note: Input validation is performed by the `arista.avd.validate_inputs` plugin, which must be run before this plugin.

## Parameters

| Argument | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| <samp>tmp_dir</samp> | str | True | None | - | Path to use as the AVD temporary directory for storing templated and validated data used internally by plugins.<br>Must be the same across all plugins. |
| <samp>eos_designs_custom_templates</samp> | list | False | None | - | List of dicts for Jinja2 templates to be run after generating the structured configuration |
| <samp>&nbsp;&nbsp;&nbsp;&nbsp;template</samp> | str | True | None | - | Template file. |
| <samp>&nbsp;&nbsp;&nbsp;&nbsp;options</samp> | dict | False | None | - | Template options |
| <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;list_merge</samp> | str | False | append | - | Merge strategy for lists |
| <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;strip_empty_keys</samp> | bool | False | True | - | Filter out keys from the generated output if value is null/none/undefined<br>Only applies to templates. |
| <samp>dest</samp> | str | False | None | - | Destination path. If set, the output facts will also be written to this path.<br>Autodetects data format based on file suffix. &#39;.yml&#39;, &#39;.yaml&#39; -&gt; YAML, default -&gt; JSON |
| <samp>mode</samp> | str | False | None | - | File mode (ex. &#34;0o664&#34;) for dest file. See &#39;ansible.builtin.copy&#39; module for details. |
| <samp>template_output</samp> | bool | False | None | - | If true, the output data will be run through another jinja2 rendering before returning.<br>This is to resolve any input values with inline jinja using variables/facts set by the input templates.<br>Ignored for ansible-core versions &gt;= 2.19, since it is no longer needed. |
| <samp>cprofile_file</samp> | str | False | None | - | Filename for storing cprofile data used to debug performance issues.<br>Running cprofile will slow down performance in it self, so only set this while troubleshooting. |
| <samp>digital_twin</samp> | bool | optional | False | - | PREVIEW: This option is marked as &#34;preview&#34;, meaning the data models or generated configuration can change at any time.<br>Generate Digital Twin topology information. |
| <samp>return_structured_config</samp> | bool | optional | False | - | Return the structured configuration as &#34;ansible_facts&#34;. |

## Examples

```yaml
---
- name: Generate device configuration in structured format
  arista.avd.eos_designs_structured_config:
    tmp_dir: "intended/tmp/eos_designs"
    templates:
      - template: "custom_templates/custom_feature1.j2"
      - template: "custom_templates/custom_feature2.j2"
        options:
          list_merge: replace
          strip_empty_keys: false
  check_mode: false
  changed_when: false
```

## Authors

- Arista Ansible Team (@aristanetworks)
