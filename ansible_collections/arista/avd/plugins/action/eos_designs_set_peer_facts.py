from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.plugins.action import ActionBase


class ActionModule(ActionBase):
    def run(self, tmp=None, task_vars=None):
        if task_vars is None:
            task_vars = {}

        result = super().run(tmp, task_vars)
        del tmp  # tmp no longer has any effect

        hostvars = task_vars['hostvars']

        fabric_name = task_vars.get('fabric_name', 'all')

        hosts = task_vars.get('groups', {}).get(fabric_name, [])

        avd_topology_peers = {}
        avd_overlay_peers = {}
        for host in hosts:
            host_hostvars = hostvars.raw_get(host)

            host_topology_peers = host_hostvars.get('topology', {}).get('peers', [])

            for peer in host_topology_peers:
                if peer not in avd_topology_peers:
                    avd_topology_peers[peer] = []
                avd_topology_peers[peer].append(host)

            host_evpn_route_servers = host_hostvars.get('switch', {}).get('evpn_route_servers', [])

            for peer in host_evpn_route_servers:
                if peer not in avd_overlay_peers:
                    avd_overlay_peers[peer] = []
                avd_overlay_peers[peer].append(host)

        result['ansible_facts'] = {
            'avd_topology_peers': avd_topology_peers,
            'avd_overlay_peers': avd_overlay_peers
        }
        return result
