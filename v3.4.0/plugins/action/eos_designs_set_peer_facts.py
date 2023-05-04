from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.plugins.action import ActionBase


class ActionModule(ActionBase):
    def run(self, tmp=None, task_vars=None):
        if task_vars is None:
            task_vars = {}

        result = super().run(tmp, task_vars)
        del tmp  # tmp no longer has any effect

        set_avd_topology_peers = self._task.args.get('avd_topology_peers', False)
        set_avd_overlay_peers = self._task.args.get('avd_overlay_peers', False)

        hostvars = task_vars['hostvars']

        fabric_name = task_vars.get('fabric_name', 'all')

        hosts = task_vars.get('groups', {}).get(fabric_name, [])

        if set_avd_topology_peers or set_avd_overlay_peers:
            avd_topology_peers = {}
            avd_overlay_peers = {}
            for host in hosts:
                host_hostvars = hostvars.raw_get(host)

                if set_avd_topology_peers:
                    host_topology_peers = host_hostvars.get('topology', {}).get('peers', [])

                    for peer in host_topology_peers:
                        if peer not in avd_topology_peers:
                            avd_topology_peers[peer] = []
                        avd_topology_peers[peer].append(host)

                if set_avd_overlay_peers:
                    host_evpn_route_servers = host_hostvars.get('switch', {}).get('evpn_route_servers', [])

                    for peer in host_evpn_route_servers:
                        if peer not in avd_overlay_peers:
                            avd_overlay_peers[peer] = []
                        avd_overlay_peers[peer].append(host)

            result['ansible_facts'] = {}
            if set_avd_topology_peers:
                result['ansible_facts']['avd_topology_peers'] = avd_topology_peers
            if set_avd_overlay_peers:
                result['ansible_facts']['avd_overlay_peers'] = avd_overlay_peers

        return result
