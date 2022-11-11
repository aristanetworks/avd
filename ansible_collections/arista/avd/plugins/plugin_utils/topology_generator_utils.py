from __future__ import absolute_import, division, print_function

__metaclass__ = type
import os
import queue

import graphviz
import yaml


def read_yaml_file(filename):
    """
    Open a structure config file and load a data from the file

    Args:
        filename: Name of the file

    Returns:
        Data from the file
    """
    with open(filename, "r", encoding="utf-8") as stream:
        data = None
        try:
            data = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
        return data


def create_node_dict(file_data, filename):
    """
    Create a dictionary of nodes with its corresponding neighbours

    Args:
        file_data: Data of structure config file
        filename: Name of the file

    Returns:
        Dictionary with node and its corresponding neighbours
    """
    node_dict = {}
    node_dict["name"] = os.path.splitext(filename)[0].split("/")[2]
    node_dict["neighbours"] = []
    if file_data and file_data.get("ethernet_interfaces"):
        for key, value in file_data["ethernet_interfaces"].items():
            neighbour_dict = {}
            neighbour_dict["neighborDevice"] = value["peer"]
            neighbour_dict["neighborPort"] = value["peer_interface"]
            neighbour_dict["port"] = key
            if "channel_group" in value and "id" in value["channel_group"]:
                neighbour_dict["portChannel"] = value["channel_group"]["id"]
            node_dict["neighbours"].append(neighbour_dict)
    return node_dict


def structured_config_to_topology_input(output_list, node_dict, diagram_groups, current_dict=None):
    """
    Convert structure config file data to topology input data by creating a nested dictionary
    of "nodes" and "groups"

    Args:
        output_list: Original input dictionary with nested "name", "nodes" and "groups" keys
        nodes: List of nodes
        node_neighbour_dict: Dictionary with nodes and neighbours list
                       ex- {'0': ['super-spine1', 'super-spine2']}
    Returns:
       output_list: List of dictionary with nested "name", "nodes" and "groups" keys
    """
    if diagram_groups:
        diagram_group_var = diagram_groups.pop(0)["name"]
        if not output_list:
            new_dict = {"name": diagram_group_var, "groups": [], "nodes": []}
            output_list.append(new_dict)
            structured_config_to_topology_input(new_dict["groups"], node_dict, diagram_groups, new_dict)
        else:
            found = False
            for entry in output_list:
                if diagram_group_var == entry["name"]:
                    structured_config_to_topology_input(entry["groups"], node_dict, diagram_groups, entry)
                    found = True

            if not found:
                new_dict = {"name": diagram_group_var, "groups": [], "nodes": []}
                output_list.append(new_dict)
                structured_config_to_topology_input(new_dict["groups"], node_dict, diagram_groups, new_dict)
    else:
        current_dict["nodes"].append(node_dict)

    return output_list


def find_root_nodes(data, root=None):
    """
    Find a root node

    Args:
        data: Dictinary with nested keys "nodes" and "groups"

    Returns:
        Return a dictinary with root node as "0" with it's neighbours
    """

    if not root:
        root = {"name": "0", "neighbours": []}
    if "nodes" in data and data["nodes"]:
        for node in data["nodes"]:
            neighbour_dict = {"neighborDevice": node["name"], "neighborPort": "", "port": ""}
            root["neighbours"].append(neighbour_dict)
        return root

    if "groups" in data and data["groups"]:
        for group in data["groups"]:
            root = find_root_nodes(group, root)
        return root


def create_graph_dict(output_list, nodes=None, node_neighbour_dict=None):
    """
    Create a dictionary of rank/levels and it's corresponding node list

    Args:
      output_list: List of dictionaries with nested "name", "nodes" and "groups" keys
      nodes: List of nodes
      node_neighbour_dict: Dictionary with nodes and neighbours list
                        ex- {'0': ['super-spine1', 'super-spine2']}
    Returns:
       nodes: List of nodes which are present in the graph
       node_neighbour_dict: Dictionary of node and its corresponding neighbours
    """
    if nodes is None:
        nodes = []
    if node_neighbour_dict is None:
        node_neighbour_dict = {}
    for group in output_list:
        if "nodes" in group and group["nodes"]:
            for node in group["nodes"]:
                nodes.append(node["name"])
                neighbours = []
                for neighbour in node["neighbours"]:
                    neighbours.append(neighbour["neighborDevice"])
                node_neighbour_dict[node["name"]] = neighbours
        if "groups" in group and group["groups"]:
            create_graph_dict(group["groups"], nodes, node_neighbour_dict)
    return nodes, node_neighbour_dict


def find_node_levels(graph, start_node, node_list):
    """
    Function to determine level of each node starting from start_node using BFS algorithm
    Args:
        graph: dictionary with node and its neighbours list
        start_node: Starting point/root node of the graph
        node_list: List of nodes
    Returns:
         dict: Return a dictionary with level as key and node list as value
    """
    # array to store level of each node
    level_dict = {}
    marked = {node: False for node in node_list}
    # create a queue
    que = queue.Queue()
    # enqueue element x
    que.put(start_node)
    # initialize level of start_node
    # node to 0
    level_dict[start_node] = 0
    # marked it as visited
    marked[start_node] = True

    # do until queue is empty
    while not que.empty():
        # get the first element of queue
        start_node = que.get()
        # traverse neighbors of node start_node
        if start_node in graph:
            for i in graph[start_node]:
                # neighbor is neighbor of node start_node
                neighbor = i
                # if neighbor is not marked already
                if neighbor in marked and not marked[neighbor]:
                    # enqueue neighbor in queue
                    que.put(neighbor)
                    # level of neighbor is level of start_node + 1
                    level_dict[neighbor] = level_dict[start_node] + 1
                    # mark neighbor
                    marked[neighbor] = True

    rank_dict = {}
    for node, level in level_dict.items():
        if level not in rank_dict:
            rank_dict[level] = [node]
        else:
            rank_dict[level].append(node)
    return rank_dict


def draw_nested_subgraphs(input_data, rank_dict, graph_obj, undefined_rank_nodes):
    """
    Create a nested subgraphs recursively based on input_data

    Args:
        input_data: Original input dictionary with nested "name", "nodes" and "groups" keys
        rank_dict: Node level dictionary
        graph_obj: Object of graphviz.Graph class
        undefined_rank_nodes: Nodes without parent/root nodes
    Returns:
         None
    """
    for data in input_data:
        graph_obj.attr(ranksep="0.7")
        with graph_obj.subgraph(name="cluster_child_" + str(data["name"])) as subgraph:
            subgraph.attr(label=data["name"])
            subgraph.attr(labelloc="t")
            if "nodes" in data and data["nodes"]:
                pod_node_list = [node["name"] for node in data["nodes"] if node["name"] != "0"]
                new_rank_dict = {"undefined": {}}
                new_node_list = [undefined_rank_node for undefined_rank_node in undefined_rank_nodes if undefined_rank_node in pod_node_list]
                new_rank_dict["undefined"] = new_node_list
                for rank, nodes in rank_dict.items():
                    new_rank_dict[rank] = []
                    for node in nodes:
                        if node in pod_node_list and node not in undefined_rank_nodes:
                            new_rank_dict[rank].append(node)

                for rank, nodes in new_rank_dict.items():
                    with subgraph.subgraph() as inner_subgraph:
                        inner_subgraph.attr(rank="same")
                        for node in nodes:
                            inner_subgraph.node(node)

            if "groups" in data and data["groups"]:
                draw_nested_subgraphs(data["groups"], rank_dict, subgraph, undefined_rank_nodes)


def create_graph_and_set_properties():
    """
    Create a graphviz graph object and set node and edge properties

    Returns: Graph object
    """
    graph_obj = graphviz.Graph(
        name="parent",
        format="svg",
        filename="topology.gv",
        graph_attr={"splines": "line"},
        node_attr={
            "color": "lightblue",
            "style": "filled",
            "fontname": "arial",
            "shape": "box",
            "center": "true",
            "image": "switch.jpg",
            "pin": "True",
            "height": "1",
            "width": "1",
            "fixedsize": "true",
            "labelloc": "t",
            "fontsize": " 10pt",
            "fontcolor": "yellow",
        },
        edge_attr={"fontname": "arial", "fontsize": "8", "minlen": "2", "center": "true", "concentrate": "true", "weight": "0", "labelfloat": "false"},
    )
    graph_obj.attr(rank="same")
    return graph_obj


def generate_topology(rank_dict, node_neighbour_dict, output_list, undefined_rank_nodes):
    """
    Generate topology diagram using graphviz.Graph

    Args:
       rank_dict: Dictionary of nodes with respective levels
                  ex- {0: ['0'], 1: ['super-spine1', 'super-spine2']}
       node_neighbour_dict: Dictionary with nodes and neighbours list
                            ex- {'0': ['super-spine1', 'super-spine2']}
       output_list: List of dictionaries with nested "name", "nodes" and "groups" keys
       undefined_rank_nodes: Nodes without parent
    Returns:
        None
    """

    graph_obj = create_graph_and_set_properties()

    draw_nested_subgraphs(output_list, rank_dict, graph_obj, undefined_rank_nodes)

    for node, neighbours in node_neighbour_dict.items():
        if node != "0":
            for neighbour in neighbours:
                graph_obj.edge(node, neighbour)

    graph_obj.view()
