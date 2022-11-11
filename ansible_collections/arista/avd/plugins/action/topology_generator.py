from __future__ import absolute_import, division, print_function

__metaclass__ = type


import glob

from ansible.errors import AnsibleActionFail
from ansible.plugins.action import ActionBase

import ansible_collections.arista.avd.plugins.plugin_utils.topology_generator_utils as gt


class ActionModule(ActionBase):
    def run(self, tmp=None, task_vars=None):
        if task_vars is None:
            task_vars = {}
        result = super().run(tmp, task_vars)
        del tmp  # tmp no longer has any effect
        if self._task.args and "structured_config" not in self._task.args:
            raise AnsibleActionFail("Missing 'structured_config' variable.")
        path = self._task.args["structured_config"]
        self.driver_func(path)
        return result

    def driver_func(self, directory_path):
        files = glob.glob(directory_path + "/*.yml")

        output_list = []
        for file in files:
            data = gt.read_yaml_file(file)
            node_dict = gt.create_node_dict(data, file)
            output_list = gt.structured_config_to_topology_input(output_list, node_dict, data["diagram_groups"], current_dict={})
        root_dict = gt.find_root_nodes(output_list[0])
        output_list[0]["nodes"].append(root_dict)
        global_node_list, graph_dict = gt.create_graph_dict(output_list)
        nodes_rank_dict = gt.find_node_levels(graph_dict, "0", global_node_list)
        rank_nodes_list = []
        for v in nodes_rank_dict.values():
            rank_nodes_list += v
        undefined_rank_nodes = list(set(rank_nodes_list) ^ set(global_node_list))
        gt.generate_topology(nodes_rank_dict, graph_dict, output_list, undefined_rank_nodes)
