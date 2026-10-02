# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.

DOCUMENTATION = r"""
---
module: legacy_role_vars
version_added: "6.5.0"
author: Arista Ansible Team (@aristanetworks)
short_description: Validate legacy role variable aliases
description: |-
  The C(arista.avd.legacy_role_vars) action plugin detects legacy unprefixed role variables.
  It can emit one aggregated warning, reject the variables, or accept them silently.
  Variable values are never returned or displayed.
options:
  role_name:
    description: Name of the role owning the variables.
    required: true
    type: str
  aliases:
    description: Mapping of legacy variable names to canonical role-prefixed names.
    required: true
    type: dict
  mode:
    description: Behavior when a consumed legacy alias is detected.
    required: false
    default: warning
    choices: [warning, error, silent]
    type: str
"""

EXAMPLES = r"""
- name: Validate legacy eos_designs variables
  arista.avd.legacy_role_vars:
    role_name: eos_designs
    aliases:
      root_dir: eos_designs_root_dir
    mode: "{{ avd_legacy_role_vars_mode | default('warning') }}"
  run_once: true
"""

RETURN = r"""
legacy_aliases:
  description: Names of consumed legacy aliases. Values are never returned.
  returned: always
  type: list
  elements: str
  sample: [root_dir]
"""
