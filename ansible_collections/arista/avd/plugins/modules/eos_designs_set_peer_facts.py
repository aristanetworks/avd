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
module: eos_designs_set_peer_facts
version_added: "3.4.0"
author: Arista Ansible Team (@aristanetworks)
short_description: Set eos_designs peer facts
description:
  - Parse all hostvars and set a common avd_topology_peers and avd_overlay_peers dicts with list per host
options:
  avd_topology_peers:
    description: |
      Set avd_topology_peers fact with a list per device of downstream devices,
      meaning devices pointing to this device as uplink switch
    required: False
    type: bool
  avd_overlay_peers:
    description: |
      Set avd_overlay_peers fact with a list per device of EVPN Route Server Clients,
      meaning devices pointing to this device as EVPN Route Server
    required: False
    type: bool
'''

EXAMPLES = r'''
# tasks file for configlet_build_config
- name: Set AVD peer facts
  eos_designs_set_peer_facts:
    avd_topology_peers: True
    avd_overlay_peers: True
  run_once: True
'''
