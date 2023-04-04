from __future__ import absolute_import, division, print_function

__metaclass__ = type


import glob
import os

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
        if self._task.args and "destination" not in self._task.args:
            raise AnsibleActionFail("Missing 'destination' variable.")
        destination = self._task.args["destination"]

        inventory_group = [i.split(".")[0] for i in os.listdir(path)]
        self.driver_func(path, inventory_group, destination)
        return result

    # def driver_func(self, directory_path):
    def driver_func(self, directory_path, inventory_group, destination):  
        files = glob.glob(directory_path + "/*.yml")

        output_list = []
        for file in files:
            data = gt.read_yaml_file(file)
            node_dict = gt.create_node_dict(data, file)
            output_list = gt.structured_config_to_topology_input(output_list, node_dict, data["diagram_groups"], current_dict={})

        root_dict = gt.find_root_nodes(output_list[0])
        output_list[0]["nodes"].append(root_dict)

        global_node_list, graph_dict = gt.create_graph_dict(output_list, inventory_group)

        level_dict, node_level_dict = gt.find_node_levels(graph_dict, "0", global_node_list)

        rank_nodes_list = []
        for v in level_dict.values():
            rank_nodes_list += v

        undefined_rank_nodes = list(set(rank_nodes_list) ^ set(global_node_list))

        node_port_val, temp_graph_dict = gt.get_node_port_temp_graph_dict(graph_dict, node_level_dict, level_dict, undefined_rank_nodes)
 
        graph_dict = temp_graph_dict

        gt.generate_topology_hampton(destination, level_dict, graph_dict, output_list, undefined_rank_nodes, node_port_val)
