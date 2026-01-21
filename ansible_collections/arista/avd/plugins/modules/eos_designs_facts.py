# Copyright (c) 2022-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.

DOCUMENTATION = r"""
---
module: eos_designs_facts
version_added: "3.5.0"
author: Arista Ansible Team (@aristanetworks)
short_description: Set eos_designs facts
description:
  - |-
    The `arista.avd.eos_designs_facts` module is an Ansible Action Plugin providing the following capabilities:

    - Set `avd_switch_facts` fact containing internal AVD facts per host.

  - The plugin is designed to `run_once`. With this, Ansible will set the same facts on all devices,
    so all devices can lookup values of any other device without using the slower `hostvars`.
  - The module is used in `arista.avd.eos_designs` to set facts for devices, which are then used by jinja templates
    and python module in `arista.avd.eos_designs` to generate the `structured_configuration`.
options:
  template_output:
    description:
      - If true, the output data will be run through another jinja2 rendering before returning.
        This is to resolve any input values with inline jinja using variables/facts set by the input templates.
      - Ignored for ansible-core versions >= 2.19, since it is no longer needed.
    required: false
    type: bool
  cprofile_file:
    description:
      - Filename for storing cprofile data used to debug performance issues.
      - Running cprofile will slow down performance in it self, so only set this while troubleshooting.
    required: false
    type: str
  digital_twin:
    description: |-
      PREVIEW: This option is marked as "preview", meaning the data models or generated configuration can change at any time.
      Generate Digital Twin topology information.
    default: false
    type: bool
  avd_eos_designs_warn_eos_cli_config_gen_keys:
    description: |-
      Enable warnings for eos_cli_config_gen keys used in eos_designs input data.
      When enabled, warnings will be emitted during validation if any top-level keys
      from the eos_cli_config_gen schema are found at the top level of eos_designs input data.
      Note: These keys will be ignored during eos_cli_config_gen processing when used with eos_designs.
    default: true
    type: bool
"""

EXAMPLES = r"""
---
- name: Set eos_designs facts
  arista.avd.eos_designs_facts:
    schema_id: eos_designs
  check_mode: false
  run_once: true
"""
