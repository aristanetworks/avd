---
# This title is used for search results
title: arista.avd._emit_warning
---
<!--
  ~ Copyright (c) 2023-2024 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# _emit_warning

!!! note
    Always use the FQCN (Fully Qualified Collection Name) `arista.avd._emit_warning` when using this plugin.

Internal module - DO NOT USE - Emit a warning in a task.

## Synopsis

Emit a warning in a task.

## Parameters

| Argument | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| <samp>message</samp> | str | optional | None |  | The warning message to emit. |

## Examples

```yaml
---
- name: Emit a warning
  arista.avd._emit_warning:
    message |-
      The warning message.
  delegate_to: localhost
  check_mode: false
  run_once: true
  changed_when: false
```

## Authors

- EMEA AS Team (@aristanetworks)
