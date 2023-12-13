---
# This title is used for search results
title: arista.avd.convert_dicts
---
<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# convert_dicts

!!! note
    Always use the FQCN (Fully Qualified Collection Name) `arista.avd.convert_dicts` when using this plugin.

Convert a dictionary containing nested dictionaries to a list of dictionaries.

## Synopsis

The filter inserts the outer dictionary keys into each list item using the primary\_key \`name\` \(the key name is configurable\), and if there is a non\-dictionary value, it inserts this value to secondary key \(the key name is configurable\), if <em>secondary\_key</em> is provided.

This filter is intended for seamless data model migration from dictionaries to lists.

The filter can improve Ansible\'s processing performance when dealing with large dictionaries by converting them to lists of dictionaries.

Note \- if there is a non\-dictionary value with no secondary key provided, it will pass through untouched.

## Parameters

| Argument | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| _input | any | True | None |  | Dictionary to convert \- returned untouched if not a nested dictionary/list. |
| primary_key | string | optional | name |  | Name of the primary key used when inserting outer dictionary keys into items. |
| secondary_key | string | optional | None |  | Name of the secondary key used when inserting dictionary values which are list into items. |

## Examples

```yaml
---
- hosts: localhost
  gather_facts: false
  tasks:
  - name: Show convert_dicts with default primary_key "name"
    vars:
      my_dict:
        item1:
          value: value1
        item2:
          value: value2
    ansible.builtin.debug:
      msg: "{{ item.name }}: {{ item.value }}"
    loop:
      items: "{{ my_dict | arista.avd.convert_dicts }}"

  - name: Show convert_dicts with custom primary_key "myname"
    vars:
      my_dict:
        item1:
          value: value1
        item2:
          value: value2
    ansible.builtin.debug:
      msg: "{{ item.myname }}: {{ item.value }}"
    loop: "{{ my_dict | arista.avd.convert_dicts('myname') }}"

  - name: Show convert_dicts with secondary_key "myvalue"
    vars:
      my_dict:
        item1: value1
        item2: value2
    ansible.builtin.debug:
      msg: "{{ item.name }}: {{ item.myvalue }}"
    loop: "{{ my_dict | arista.avd.convert_dicts(secondary_key='myvalue') }}"
```

## Return Values

| Name | Type | Description |
| ---- | ---- | ----------- |
| _value | any | Returns list of dictionaries or input variable untouched if not a nested dictionary/list. |

## Authors

- Arista Ansible Team (@aristanetworks)
