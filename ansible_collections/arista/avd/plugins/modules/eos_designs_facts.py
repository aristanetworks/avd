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
  - Parse all hostvars and set common facts
options:
  avd_switch_facts:
    description: |
      Set avd_switch_facts fact with a dict per device of switch.* facts
      Set avd_overlay_peers fact with a list per device of EVPN Route Server Clients,
      meaning devices pointing to this device as EVPN Route Server
    required: False
    type: bool
  avd_topology_facts:
    description: |
      Set avd_switch_facts fact with a dict per device of topology.* facts
      Set avd_topology_peers fact with a list per device of downstream devices,
      meaning devices pointing to this device as uplink switch
      Most topology_facts are based on switch.* facts, so those must be set in the same
      or a previous task.
    required: False
    type: bool
'''

EXAMPLES = r'''
- name: Set eos_designs facts
  eos_designs_facts:
    avd_switch_facts: True
    avd_topology_facts: True
  run_once: True
'''
