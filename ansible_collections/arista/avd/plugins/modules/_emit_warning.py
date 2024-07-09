# Copyright (c) 2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
DOCUMENTATION = r"""
---
module: _emit_warning
version_added: "4.9.0"
author: Arista Networks (@aristanetworks)
short_description: Internal module - DO NOT USE - Emit a warning in a task.
description:
  - Emit a warning in a task.
options:
  message:
    description: The warning message to emit.
    type: str
"""

EXAMPLES = r"""
---
- name: Emit a warning
  arista.avd._emit_warning:
    message |-
      The warning message.
  delegate_to: localhost
  check_mode: false
  run_once: true
  changed_when: false
"""
