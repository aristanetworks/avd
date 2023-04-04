# Copyright 2022 Arista Networks
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

DOCUMENTATION = r"""
---
module: eos_designs_facts
version_added: "3.5.0"
author: Arista Ansible Team (@aristanetworks)
short_description: Set eos_designs facts
description:
  - The `arista.avd.eos_designs_facts` module is an Ansible Action Plugin providing the following capabilities
  - Set `avd_switch_facts` fact containing both `switch` facts per host.
  - Set `avd_topology_peers` fact containing list of downlink switches per host.
    This list is built based on the `uplink_switches` from all other hosts.
  - Set `avd_overlay_peers` fact containing list of EVPN or MPLS overlay peers per host.
    This list is built based on the `evpn_route_servers` and `mpls_route_reflectors` from all other hosts.
  - The plugin is designed to `run_once`. With this, Ansible will set the same facts on all devices,
    so all devices can lookup values of any other device without using the slower `hostvars`.
  - The facts can also be copied to the "root" `switch` in a task run per-device (see example below)
  - The module is used in `arista.avd.eos_designs` to set facts for devices, which are then used by jinja templates
    and python module in `arista.avd.eos_designs` to generate the `structured_configuration`.
options:
  schema:
    description: Schema conforming to "AVD Meta Schema". Either schema or schema_id must be set.
    required: false
    type: dict
  schema_id:
    description: ID of Schema conforming to "AVD Meta Schema".  Either schema or schema_id must be set.
    required: false
    type: str
    choices: [ "eos_cli_config_gen", "eos_designs" ]
  template_output:
    description: |
      If true the output data will be run through another jinja2 rendering before returning.
      This is to resolve any input values with inline jinja using variables/facts set by the input templates.
    required: false
    type: bool
  conversion_mode:
    description:
      - Run data conversion in either "warning", "info", "debug", "quiet" or "disabled" mode.
      - Conversion will perform type conversion of input variables as defined in the schema.
      - Conversion is intended to help the user to identify minor issues with the input data, while still allowing the data to be validated.
      - During conversion, messages will be generated with information about the host(s) and key(s) which required conversion.
      - conversion_mode:disabled means that conversion will not run.
      - conversion_mode:error will produce error messages and fail the task.
      - conversion_mode:warning will produce warning messages.
      - conversion_mode:info will produce regular log messages.
      - conversion_mode:debug will produce hidden messages viewable with -v.
      - conversion_mode:quiet will not produce any messages.
    required: false
    default: "debug"
    type: str
    choices: [ "warning", "info", "debug", "quiet", "disabled" ]
  validation_mode:
    description:
      - Run validation in either "error", "warning", "info", "debug" or "disabled" mode.
      - Validation will validate the input variables according to the schema.
      - During validation, messages will be generated with information about the host(s) and key(s) which failed validation.
      - validation_mode:disabled means that validation will not run.
      - validation_mode:error will produce error messages and fail the task.
      - validation_mode:warning will produce warning messages.
      - validation_mode:info will produce regular log messages.
      - validation_mode:debug will produce hidden messages viewable with -v.
    required: false
    default: "warning"
    type: str
    choices: [ "error", "warning", "info", "debug", "disabled" ]
"""

EXAMPLES = r"""
- name: Set eos_designs facts
  tags: [build, provision, facts]
  arista.avd.eos_designs_facts:
    avd_switch_facts: True
  check_mode: False
  run_once: True

- name: Set eos_designs facts per device
  tags: [build, provision, facts]
  ansible.builtin.set_fact:
    switch: "{{ avd_switch_facts[inventory_hostname].switch }}"
  delegate_to: localhost
  changed_when: false
"""
