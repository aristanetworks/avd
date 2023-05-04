# GNU General Public License v3.0+
#
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

DOCUMENTATION = r'''
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
    in `arista.avd.eos_designs` to generate the `structured_configuration`.
options:
  avd_switch_facts:
    description: |
      - Calculate and set 'avd_switch_facts.<devices>.switch', 'avd_overlay_peers' and 'avd_topology_peers' facts
    required: False
    type: bool
'''

EXAMPLES = r'''
- name: Set eos_designs facts
  tags: [build, provision, facts]
  arista.avd.eos_designs_facts:
    avd_switch_facts: True
  check_mode: False
  run_once: True
'''
