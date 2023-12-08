---
# This title is used for search results
title: arista.avd.add_md_toc
---
<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# add_md_toc

!!! note
    Always use the FQCN (Fully Qualified Collection Name) `arista.avd.add_md_toc` when using this plugin.

Parse the input Markdown and add a Table of Contents between the toc\_markers.

## Synopsis

The filter is used in arista.avd.eos\_designs to create a table of contents for Fabric Documentation.

The filter is also used in arista.avd.eos\_cli\_config\_gen to create a table of contents for Device Documentation.

## Requirements

The below requirements are needed on the host that executes this module.

- md\_toc

## Parameters

| Argument | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| _input | string | True | None |  | Markdown to process. |
| skip_lines | integer | optional | 0 |  | Skip the first x lines when parsing the input Markdown. |
| toc_levels | integer | optional | 3 |  | How many levels of headings will be included in the TOC. |
| toc_marker | string | optional | <!-- toc --> |  | TOC will be inserted or updated between two of markers in the input Markdown. |

## Examples

```yaml
---
tasks:
- name: Generate fabric documentation
  tags: [build, provision, documentation]
  run_once: true
  delegate_to: localhost
  check_mode: no
  copy:
    content: "{{ lookup('template','documentation/fabric-documentation.j2') | arista.avd.add_md_toc(skip_lines=3) }}"
    dest: "{{ fabric_dir }}/{{ fabric_name }}-documentation.md"
    mode: 0664
```

## Return Values

| Name | Type | Description |
| ---- | ---- | ----------- |
| _value | string | Markdown with TOC inserted between the toc\_markers. |

## Authors

- Arista Ansible Team (@aristanetworks)
