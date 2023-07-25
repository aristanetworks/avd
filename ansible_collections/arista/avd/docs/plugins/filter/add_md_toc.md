# arista.avd.add_md_toc

Parse the input MarkDown and add a Table of Contents between the toc\_markers\.

## Synopsis

The filter is used in arista\.avd\.eos\_designs to create a table of contents for Fabric Documentation\.

The filter is also used in arista\.avd\.eos\_cli\_config\_gen to create a table of contents for Device Documentation\.

## Parameters

  _input (True, string, None)
    MarkDown which will be processed\.

  skip_lines (optional, integer, 0)
    Skip first x lines when parsing the input MarkDown\.

  toc_levels (optional, integer, 3)
    How many levels of headings will be included in the TOC\.

  toc_marker (optional, string, <!-- toc -->)
    TOC will be inserted or updated between two of these markers in the input MarkDown\.

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

  _value (, string, )
    MarkDown with TOC inserted between the toc\_markers\.

## Status

## Authors

- Arista Ansible Team (@aristanetworks)
