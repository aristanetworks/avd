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
| <samp>dest_format_string</samp> | str | True | None |  | Format string used to specify target file for each item. &#39;item&#39; is the current item from &#39;items&#39;. Like &#34;mypath/{item}.md&#34; |
| <samp>items</samp> | list | True | None |  | List of strings. Each list item is passed to &#39;dest_format_string&#39; as &#39;item&#39; and passed to templater as &#39;item&#39; |

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
