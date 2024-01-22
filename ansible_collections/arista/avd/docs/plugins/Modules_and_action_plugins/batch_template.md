---
# This title is used for search results
title: arista.avd.batch_template
---
<!--
  ~ Copyright (c) 2023-2024 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# batch_template

!!! note
    Always use the FQCN (Fully Qualified Collection Name) `arista.avd.batch_template` when using this plugin.

Render Jinja2 template on multiple items and write result to individual files.

## Synopsis

Render Jinja2 template on multiple items and write result to individual files.

Destination file mode is hardcoded to 0o664.

## Parameters

| Argument | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| <samp>template</samp> | str | True | None |  | Path to Jinja2 Template file |
| <samp>dest_format_string</samp> | str | True | None |  | Format string used to specify target file for each item. \'item\' is the current item from \'items\'. Like \"mypath/\{item\}.md\" |
| <samp>items</samp> | list | True | None |  | List of strings. Each list item is passed to \'dest\_format\_string\' as \'item\' and passed to templater as \'item\' |

## Examples

```yaml
- name: Output eos_cli_config_gen Documentation
  tags: [eos_cli_config_gen]
  delegate_to: localhost
  run_once: true
  arista.avd.batch_template:
    template: avd_schema_documentation.j2
    dest_format_str: "{{ role_documentation_dir }}/{item}.md"
    items: "{{ data_in_list_form }}"
```

## Authors

- Arista Ansible Team (@aristanetworks)
