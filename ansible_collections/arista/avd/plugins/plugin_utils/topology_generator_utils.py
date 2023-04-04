from __future__ import absolute_import, division, print_function

__metaclass__ = type
import os
import queue
import math

import yaml
import textwrap

import drawSvg as draw

import re

_nsre = re.compile('([0-9]+)')
def natural_sort_key(s):
    return [int(text) if text.isdigit() else text.lower()
            for text in re.split(_nsre, s)] 

# MARGINS between real groups
BOXMARGIN = 25

# Sizings
ROUTERMAXFONTSIZE = 25
ROUTERWRAPFONTSIZE = 18
ROUTERSIZE = 120
ROWSPACING = ROUTERSIZE * 2
LVLSPACING = ROUTERSIZE * 2
PORTHEIGHT = 30
PORTWIDTH = 20
PORTOFFSET = 3
PORTFONTSIZE = 16
TITLEFONTSIZE = 24
TITLEOFFSET = 0
FONTWIDTHHEIGHTRATIO = 0.62

# Used for horizontal connection overlaps
WIREDEFAULTDISTANCE = 10
WIRESPREAD = 6

EDGETYPES = ["server"]

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
    Create a dictionary of nodes with its corresponding neighbors

    Args:
        file_data: Data of structure config file
        filename: Name of the file

    Returns:
        Dictionary with node and its corresponding neighbors
    """
    node_dict = {}
    node_dict["edge"] = False
    node_dict["name"] = os.path.splitext(filename)[0].split("/")[-1]
    node_dict["neighbors"] = []
    if file_data and file_data.get("ethernet_interfaces"):
        if type(file_data["ethernet_interfaces"]) == dict:
            for key, value in file_data["ethernet_interfaces"].items():
                if "peer_interface" not in value:
                    continue
                neighbor_dict = {}
                neighbor_dict["neighborDevice"] = value["peer"]
                neighbor_dict["neighborPort"] = value["peer_interface"]
                neighbor_dict["port"] = key
                if "channel_group" in value and "id" in value["channel_group"]:
                    neighbor_dict["portChannel"] = value["channel_group"]["id"]
                node_dict["neighbors"].append(neighbor_dict)
                if value["peer_type"] in EDGETYPES:
                    node_dict["edge"] = True
        else:
            for value in file_data["ethernet_interfaces"]:
                if "peer_interface" not in value:
                    continue
                neighbor_dict = {}
                neighbor_dict["neighborDevice"] = value["peer"]
                neighbor_dict["neighborPort"] = value["peer_interface"]
                neighbor_dict["port"] = value["name"]
                if "channel_group" in value and "id" in value["channel_group"]:
                    neighbor_dict["portChannel"] = value["channel_group"]["id"]
                node_dict["neighbors"].append(neighbor_dict)
                if value["peer_type"] in EDGETYPES:
                    node_dict["edge"] = True                

    return node_dict


def structured_config_to_topology_input(ol, node_dict, diagram_groups, current_dict=None):
    """
    Convert structure config file data to topology input data by creating a nested dictionary
    of "nodes" and "groups"

    Args:
        ol: Original input dictionary with nested "name", "nodes" and "groups" keys
        node_dict: List of nodes
        node_neighbor_dict: Dictionary with nodes and neighbors list
                       ex- {'0': ['super-spine1', 'super-spine2']}
    Returns:
       ol: List of dictionary with nested "name", "nodes" and "groups" keys
    """

    if diagram_groups:
        diagram_group_var = diagram_groups.pop(0)
        for temp_check in diagram_group_var.keys():
            if temp_check in ['fabric_name','dc_name','pod_name','name']:
                diagram_group_var = diagram_group_var[temp_check] 

        if not ol:
            new_dict = {"name": diagram_group_var, "groups": [], "nodes": []}
            ol.append(new_dict)
            structured_config_to_topology_input(new_dict["groups"], node_dict, diagram_groups, new_dict)
        else:
            found = False
            for entry in ol:
                if diagram_group_var == entry["name"]:
                    structured_config_to_topology_input(entry["groups"], node_dict, diagram_groups, entry)
                    found = True     

            if not found:
                new_dict = {"name": diagram_group_var, "groups": [], "nodes": []}
                ol.append(new_dict)
                structured_config_to_topology_input(new_dict["groups"], node_dict, diagram_groups, new_dict)
    else:
        current_dict["nodes"].append(node_dict)

    return ol

def find_edge_distance(currentNode, nodes, seen):
    """
    Create a dictionary of rank/levels and it's corresponding node list

    Args:
      ol: List of dictionaries with nested "name", "nodes" and "groups" keys
      nodes: List of nodes
      node_neighbor_dict: Dictionary with nodes and neighbors list
                        ex- {'0': ['super-spine1', 'super-spine2']}
    Returns:
       nodes: List of nodes which are present in the graph
       node_neighbor_dict: Dictionary of node and its corresponding neighbors
    """    
    seen.append(currentNode["name"])
    if currentNode["edge"]:
        return 1

    links = []
    for link in currentNode["neighbors"]:
        if link["neighborDevice"] in nodes and link["neighborDevice"] not in seen:
            links.append(find_edge_distance(nodes[link["neighborDevice"]], nodes, seen))
    if len(links) == 0:
        return 1
    return 1 + min(links)

def find_root_nodes(data, root=None):
    """
    Find a root node

    Args:
        data: Dictinary with nested keys "nodes" and "groups"

    Returns:
        Return a dictinary with root node as "0" with it's neighbors
    """
    psuedo = False
    if not root:
        root = {"name": "0", "neighbors": []}
        psuedo = True

    # Calculate distance to edges if we just have nodes
    if psuedo and "groups" in data and len(data["groups"]) == 0:
        nodeLookup = {}
        maxDistance = -1
        for node in data["nodes"]:
            nodeLookup[node["name"]] = node

        for node in data["nodes"]:    
            node["distanceToEdge"] = find_edge_distance(node, nodeLookup, [])
            maxDistance = max(maxDistance, node["distanceToEdge"])

        for node in data["nodes"]:
            if node["distanceToEdge"] == maxDistance:
                neighbor_dict = {"neighborDevice": node["name"], "neighborPort": "", "port": ""}
                root["neighbors"].append(neighbor_dict)
        return root

    if "nodes" in data and data["nodes"]:
        for node in data["nodes"]:            
            neighbor_dict = {"neighborDevice": node["name"], "neighborPort": "", "port": ""}
            root["neighbors"].append(neighbor_dict)
        return root

    if "groups" in data and data["groups"]:
        for group in data["groups"]:
            root = find_root_nodes(group, root)
        return root


def create_graph_dict(ol, inventory_group, nodes=None, node_neighbor_dict=None):
    """
    Create a dictionary of rank/levels and it's corresponding node list

    Args:
      ol: List of dictionaries with nested "name", "nodes" and "groups" keys
      nodes: List of nodes
      node_neighbor_dict: Dictionary with nodes and neighbors list
                        ex- {'0': ['super-spine1', 'super-spine2']}
    Returns:
       nodes: List of nodes which are present in the graph
       node_neighbor_dict: Dictionary of node and its corresponding neighbors
    """
    if nodes is None:
        nodes = []
    if node_neighbor_dict is None:
        node_neighbor_dict = {}
    for group in ol:
        if "nodes" in list(group.keys()) and group["nodes"]:
            for node in group["nodes"]:
                if  (node["name"] in inventory_group) or (node["name"] == "0"):
                    nodes.append(node["name"])
                    neighbors = []
                    for neighbor in node["neighbors"]:
                        if  neighbor["neighborDevice"] in inventory_group:  
                            node_detail_dict = {}

                            node_detail_dict["nodePort"] = neighbor["port"].replace("Ethernet", "")

                            node_detail_dict["neighborDevice"] = neighbor["neighborDevice"]

                            node_detail_dict["neighborPort"] = neighbor["neighborPort"].replace("Ethernet", "")

                            neighbors.append(node_detail_dict)   
                    node_neighbor_dict[node["name"]] = neighbors
        if "groups" in group and group["groups"]:
            create_graph_dict(group["groups"], inventory_group, nodes, node_neighbor_dict)
     
    return nodes, node_neighbor_dict


def find_node_levels(graph, start_node, node_list):

    """
    Function to determine level of each node starting from start_node using BFS algorithm
    Args:
        graph: dictionary with node and its neighbors list
        start_node: Starting point/root node of the graph
        node_list: List of nodes
    Returns:
         dict: Return a dictionary with level as key and node list as value
    """

    # array to store level of each node
    node_level_dict = {}
    marked = {node: False for node in node_list}

    # create a queue
    que = queue.Queue()
    # enqueue element x
    que.put(start_node)
    # initialize level of start_node
    # node to 0
    node_level_dict[start_node] = 0
    # marked it as visited
    marked[start_node] = True
    # do until queue is empty
    while not que.empty():
        # get the first element of queue
        start_node = que.get()      
        # traverse neighbors of node start_node
        if start_node in graph:  #key checking
            for i in graph[start_node]:
                # neighbor is neighbor of node start_node
                neighbor = i["neighborDevice"] 
                  
                # if neighbor is not marked already
                if neighbor in marked.keys() and not marked[neighbor]:
                    # enqueue neighbor in queue       
                    que.put(neighbor)

                    # level of neighbor is level of start_node + 1
                    node_level_dict[neighbor] = node_level_dict[start_node] + 1

                    # mark neighbor
                    marked[neighbor] = True
 
    level_dict = {}
    for node, level in node_level_dict.items():
        if level not in level_dict:
            level_dict[level] = [node]
        else:
            level_dict[level].append(node)

    return level_dict, node_level_dict

def generate_topology_hampton(destination, old_level_dict, node_neighbor_dict, ol, undefined_rank_nodes, node_port_val):
    """
    Generate topology diagram using node neighbour dictionary

    Args:
      destination: file name in which topology diagram get saved
      old_level_dict: List of nodes and its corrensponding level
                        ex- {0: ['0'], 1: ['dc1-ss1', 'dc1-ss2']}
      node_neighbor_dict: Dictionary with nodes and neighbors list and their ports
                        ex- {'0': [{'nodePort': '', 'neighborDevice': 'dc2-ss3', 'neighborPort': ''}]
      ol: output_list contain dictionary having cluster name and having their corresponding nodes 
      undefined_rank_nodes: nodes which dont have parent
      node_port_val: port values for each node
    """ 
    # Remove psuedo 0'th element
    del old_level_dict[0]

    # Make a level loopup dict
    level_dict = {}
    for idx, nodes in old_level_dict.items():
        for node in nodes:
            level_dict[node] = idx


    ol = subgroup_inventor_recursive(level_dict, ol[0])

    ol = calculate_box_size_recursive(level_dict, ol)


    GROUPOFFSET = LVLSPACING
    if len(ol["nodes"]) == 0:
        GROUPOFFSET = 0
    HEIGHTMARGIN = ol["height"] * (BOXMARGIN*2.75)
    height = (((ol["height"]-1) * LVLSPACING))+ GROUPOFFSET + HEIGHTMARGIN + (BOXMARGIN*2)
    width = ol["width"] + BOXMARGIN * 2
    d = draw.Drawing(width, height, origin=(0,0), font_family="monospace")
    d.append(draw.Rectangle(0,0, width, height, fill='#00285A'))

    nodes, render_orderings, titles = draw_groups_recursive(d, level_dict, ol, 20, height-50, 90)

    del node_port_val['0']
    draw_ports(d, nodes, node_port_val)

    del node_neighbor_dict['0']
    draw_links(d, nodes, node_neighbor_dict, level_dict, render_orderings)
    
    for title in titles:
        d.append(title)

    # Display
    d.setRenderSize(width, height)
    d.saveSvg(destination)

def subgroup_inventor_recursive(ld, ol):
    """
    Create a dictionary of clusters and it's corresponding node

    Args:
      ld: level_dict dictionary of nodes and its corresponding level
      ol: List of dictionaries with nested "name", "nodes" and "groups" keys
    Returns:
      ol: Dictionary of clusters and its corresponding nodes and its neighbors list
    """    
    groupLookup = {}
    if len(ol["groups"]) == 0:
        for idx, child in enumerate(ol["nodes"]):
            if ("." in child["name"] or "0" == child["name"]):
                continue
            lvl = ld[child["name"]]
            if lvl not in groupLookup:
                groupLookup[lvl] = {
                    "nodes": [],
                    "groups": [],
                    "name": child["name"],
                    "psuedo": True,
                }
            groupLookup[lvl]["nodes"].append(child)

        ol["nodes"] = []
        if len(groupLookup.keys()) == 1:
            ol["nodes"] = list(groupLookup.values())[0]["nodes"]
        else:
            keys = list(groupLookup.keys())
            lowest = min(keys)
            keys.remove(lowest)
            secondLowest = min(keys)
            sLI = 0
            other = []
            for i, group in groupLookup.items():
                if i == lowest:
                    ol["nodes"] = group["nodes"]
                elif i == secondLowest:
                    sLI = len(ol["groups"])
                    ol["groups"].append(group)
                else:
                    other.append(group)
            for group in other:
                ol["groups"][sLI]["groups"].append(group)

    for idx, child in enumerate(ol["groups"]):
        child = subgroup_inventor_recursive(ld, child)
        ol["groups"][idx] = child

    return ol


def calculate_box_size_recursive(level_dict, ol):
    """
    Create a outter box for clusters

    Args:
      ld: level_dict dictionary of nodes and its corresponding level
      ol: List of dictionaries with nested "name", "nodes" and "groups" keys
    Returns:
      ol: Dictionary of clusters and adds width and height to it
    """       
    if "neighbors" in ol:
        ol["width"] = ROWSPACING
        return ol

    groupWidths = 0
    
    height = 0
    for idx, child in enumerate(ol["groups"]):
        child = calculate_box_size_recursive(level_dict, child)
        ol["groups"][idx] = child
        groupWidths += child["width"] + (BOXMARGIN *2)
        height = max(child["height"]+1, height)

    if height == 0:
        height = 1

    ol["height"] = height

    if len(ol["groups"]) > 1:
        groupWidths -= BOXMARGIN

    childrenWidth = 0
    for idx, child in enumerate(ol["nodes"]):
        if child["name"] == "0":
            del ol["nodes"][idx]
            continue
        child = calculate_box_size_recursive(level_dict, child)
        ol["nodes"][idx] = child
        childrenWidth += child["width"]

    ol["nodes"] = sorted(ol["nodes"], key=lambda d: d['name']) 

    # Add padding
    # childrenWidth += ROUTERSIZE/2

    ol["width"] = max(groupWidths, childrenWidth)

    return ol

def calculate_text_length(text, size):
    """
    Create a dictionary of rank/levels and it's corresponding node list

    Args:
      ol: List of dictionaries with nested "name", "nodes" and "groups" keys
      nodes: List of nodes
      node_neighbor_dict: Dictionary with nodes and neighbors list
                        ex- {'0': ['super-spine1', 'super-spine2']}
    Returns:
       nodes: List of nodes which are present in the graph
       node_neighbor_dict: Dictionary of node and its corresponding neighbors
    """    
    return (len(text)) * size * FONTWIDTHHEIGHTRATIO

def calculate_max_letter_count(size, fontsize):
    """
    Create a dictionary of rank/levels and it's corresponding node list

    Args:
      ol: List of dictionaries with nested "name", "nodes" and "groups" keys
      nodes: List of nodes
      node_neighbor_dict: Dictionary with nodes and neighbors list
                        ex- {'0': ['super-spine1', 'super-spine2']}
    Returns:
       nodes: List of nodes which are present in the graph
       node_neighbor_dict: Dictionary of node and its corresponding neighbors
    """    
    return math.floor(size / (fontsize * FONTWIDTHHEIGHTRATIO))

def draw_groups_recursive(d, ld, ol, x, y, lum):
    """
    Draw groups, cluster and nodes corresponding to it

    Args:
      d: object of drawSVG 
      ld: dictionary of level  
      ol: output list containing groups cluster and nodes  
      x: width default count
      y: padding on outter box 
      lum: List 
    Returns:
       nodes: List of nodes which are present in the graph
       orderings: level of nodes
       titles: Titles of node
    """

    titles = []
    orderings = {}
    nodes = {}
    GROUPOFFSET = LVLSPACING
    if len(ol["nodes"]) == 0:
        GROUPOFFSET = 0
    HEIGHTMARGIN = ol["height"] * (BOXMARGIN*2.75)

    if "psuedo" not in ol:
        fill = f'hsl(0, 0%, {lum}%)'
        lum -= 10
        d.append(draw.Rectangle(
            x, y-(((ol["height"]-1) * LVLSPACING))-GROUPOFFSET - HEIGHTMARGIN + BOXMARGIN, 
            ol["width"], 
            (((ol["height"]-1) * LVLSPACING))+GROUPOFFSET + HEIGHTMARGIN, 
            fill=fill, rx="25", stroke=f'hsl(0, 0%, {lum * .75}%)', stroke_width=4,
            )
        )
        textlength = calculate_text_length(ol["name"], TITLEFONTSIZE)
        titles.append(draw.Rectangle(x + ol["width"]/2 - textlength/2, y-TITLEFONTSIZE + TITLEOFFSET + BOXMARGIN - 3, textlength, TITLEFONTSIZE - 1, fill=fill))
        titles.append(draw.Text(ol["name"], TITLEFONTSIZE, x + ol["width"]/2, y-TITLEFONTSIZE + BOXMARGIN + TITLEOFFSET, fill="black",  text_anchor="middle"))

    cx = 0
    for child in ol["groups"]:
        cx += child["width"] + BOXMARGIN
    cx = ol["width"]/2 - (cx/2) + BOXMARGIN/2 + 0.5
    for idx, child in enumerate(ol["groups"]):
        newNodes, newOrderings, newTitles = draw_groups_recursive(d, ld, child, x + cx, y - GROUPOFFSET - (BOXMARGIN * 1.50), lum)
        for k, node in newNodes.items():
            nodes[k] = node
        cx += child["width"] + BOXMARGIN
        titles = [*titles, *newTitles]
        for level, onodes in newOrderings.items():
            if level not in orderings:
                orderings[level] = []
            for node in onodes:
                orderings[level].append(node)
    
    cx = (ol["width"]/2) - ((len(ol["nodes"])/2)*ROWSPACING) + (ROUTERSIZE/2)
    for idx, child in enumerate(ol["nodes"]):
        child["x"] = x + cx + (ROUTERSIZE/2)
        child["y"] = y-(LVLSPACING/2)
        nodes[child["name"]] = child
        d.append(draw.Rectangle(
            child["x"] - (ROUTERSIZE/2), child["y"]-(ROUTERSIZE/2), 
            ROUTERSIZE, 
            ROUTERSIZE, 
            fill="#5167B7", text=child["name"]
        ))

        fontsize = ROUTERMAXFONTSIZE
        while calculate_text_length(child["name"], fontsize) > ROUTERSIZE and fontsize > ROUTERWRAPFONTSIZE:
            fontsize-=1

        if not fontsize > ROUTERWRAPFONTSIZE:
            fontsize = ROUTERWRAPFONTSIZE
            wrapper = textwrap.TextWrapper(width=calculate_max_letter_count(ROUTERSIZE, fontsize))
            lines = wrapper.wrap(text=child["name"])
            
            offset = (fontsize * len(lines)) / 4
            for element in lines:
                if element.endswith("-"):
                    element = element[:-1]
                d.append(draw.Text(element, fontsize, child["x"], child["y"]-6 + offset, fill="white", text_anchor="middle"))
                offset -= fontsize
        else:
            d.append(draw.Text(child["name"], fontsize, child["x"], child["y"]-6, fill="white", text_anchor="middle"))
        cx += ROWSPACING
        level = ld[child["name"]]
        if level not in orderings:
            orderings[level] = []
        orderings[level].append(child["name"])
    return nodes, orderings, titles

def draw_ports(d, nodes, node_port_val):
    """
    Draw ports around nodes

    Args:
      d: object of drawSVG
      nodes: List of nodes
      node_port_val: ports value at top bottom left and right
    """    
    for name, parts in node_port_val.items():
        if name not in nodes:
            continue 
        node = nodes[name]
        node["ports"] = {}

        if len(parts["top"]) > 0:
            ox = node["x"] - (((PORTWIDTH + PORTOFFSET) * len(parts["top"]))/2) + PORTWIDTH/2 + PORTOFFSET/2
            for portID in parts["top"]:
                port = {"x": ox, "y": node["y"] + (ROUTERSIZE/2) + PORTHEIGHT, "dir": "up"}
                node["ports"][portID] = port
                d.append(draw.Rectangle(port["x"] - (PORTWIDTH/2), port["y"] - PORTHEIGHT, PORTWIDTH, PORTHEIGHT, fill="white", stroke="black"))
                fontsize = PORTFONTSIZE
                while calculate_text_length(portID, fontsize) > PORTWIDTH:
                    fontsize-=1
                d.append(draw.Text(portID, fontsize, port["x"], port["y"] - PORTHEIGHT/2 - PORTFONTSIZE/3, fill="black", text_anchor="middle"))
                ox = ox + PORTWIDTH + PORTOFFSET
        
        if len(parts["bottom"]) > 0:
            ox = node["x"] - (((PORTWIDTH + PORTOFFSET) * len(parts["bottom"]))/2) + PORTWIDTH/2 + PORTOFFSET/2
            for portID in parts["bottom"]:
                port = {"x": ox, "y": node["y"] - (ROUTERSIZE/2) - PORTHEIGHT, "dir": "down"}
                node["ports"][portID] = port
                d.append(draw.Rectangle(port["x"] - (PORTWIDTH/2), port["y"], PORTWIDTH, PORTHEIGHT, fill="white", stroke="black"))
                fontsize = PORTFONTSIZE
                while calculate_text_length(portID, fontsize) > PORTWIDTH:
                    fontsize-=1
                d.append(draw.Text(portID, fontsize, port["x"], port["y"] + PORTHEIGHT/2 - PORTFONTSIZE/3, fill="black", text_anchor="middle"))
                ox = ox + PORTWIDTH + PORTOFFSET
        
        if len(parts["right"]) > 0:
            oy = node["y"] + (((PORTWIDTH + PORTOFFSET) * len(parts["right"]))/2) - PORTWIDTH/2 - PORTOFFSET/2
            for portID in parts["right"]:
                port = {"x": node["x"] + (ROUTERSIZE/2) + PORTHEIGHT, "y": oy, "dir": "right"}
                node["ports"][portID] = port
                d.append(draw.Rectangle(port["x"] - PORTHEIGHT, port["y"] - PORTWIDTH/2, PORTHEIGHT, PORTWIDTH, fill="white", stroke="black"))
                fontsize = PORTFONTSIZE
                while calculate_text_length(portID, fontsize) > PORTWIDTH:
                    fontsize-=1
                d.append(draw.Text(portID, fontsize, port["x"] - PORTHEIGHT/2, port["y"] - PORTFONTSIZE/3, fill="black", text_anchor="middle"))
                oy = oy - PORTWIDTH - PORTOFFSET

        if len(parts["left"]) > 0:
            oy = node["y"] + (((PORTWIDTH + PORTOFFSET) * len(parts["left"]))/2) - PORTWIDTH/2 - PORTOFFSET/2
            for portID in parts["left"]:
                port = {"x": node["x"] - (ROUTERSIZE/2) - PORTHEIGHT , "y": oy, "dir": "left"}
                node["ports"][portID] = port
                d.append(draw.Rectangle(port["x"], port["y"] - (PORTWIDTH/2), PORTHEIGHT, PORTWIDTH, fill="white", stroke="black"))
                fontsize = PORTFONTSIZE
                while calculate_text_length(portID, fontsize) > PORTHEIGHT:
                    fontsize-=1
                d.append(draw.Text(portID, fontsize, port["x"] + PORTHEIGHT/2, port["y"] - PORTFONTSIZE/3, fill="black", text_anchor="middle"))
                oy = oy - PORTWIDTH - PORTOFFSET

def draw_links(d, nodes, node_neighbor_dict, level_dict, render_orderings):
    """
    Draw links/connections between nodes

    Args:
      d: object of drawSVG
      nodes: List of nodes
      node_neighbor_dict: Dictionary with nodes and neighbors list
      level_dict: dictionary of nodes and it corresponding level
      render_orderings:
    """    
    used_heights = {}
    for name, links in node_neighbor_dict.items():
        if name not in nodes:
                continue 
        node = nodes[name]
        for id, link in enumerate(links):
            if link["neighborDevice"] not in nodes:
                continue
            neigh = nodes[link["neighborDevice"]]
            if link["neighborPort"] not in neigh["ports"] or link["nodePort"] not in node["ports"]:
                print("MISSING LINK BETWEEN", id, neigh)
                continue

            nol = node["ports"][link["nodePort"]]
            nel = neigh["ports"][link["neighborPort"]]
            stroke = "black"
            
            # Check if same level, if so we need to route specially
            if level_dict.get(node["name"]) == level_dict.get(neigh["name"]):
                level = level_dict.get(node["name"])
                # Check collision, if their index is more than 1 apart then the lines would collide
                if abs(render_orderings[level].index(node["name"]) - render_orderings[level].index(neigh["name"])) > 1:
                    if level not in used_heights:
                        used_heights[level] = WIREDEFAULTDISTANCE
                    used_heights[level] = used_heights[level] + WIRESPREAD
                    draw_same_level_links(d, node, neigh, nol, nel, stroke, used_heights[level])
                    continue

            d.append(draw.Line(nol["x"], nol["y"], nel["x"], nel["y"], stroke=stroke, stroke_width=2))

def draw_same_level_links(d, node, neigh, nol, nel, stroke, used_height):
    """
    Draw link on same level

    Args:
      d: 
      node: 
      neigh: 
      ol: 
      ol: 
      ol: 
      ol: 

    """    
    if nel["dir"] == "right":
        temp = nol
        nol = nel
        nel = temp
    routey = node["y"] + ROUTERSIZE/2 + PORTHEIGHT + used_height
    routex = (nel["x"] + nol["x"])/2

    XOffset = 10
    d.append(draw.Line(nol["x"], nol["y"], nol["x"] + XOffset, nol["y"], stroke=stroke, stroke_width=2))
    d.append(draw.Line(nol["x"] + XOffset, nol["y"], nol["x"] + XOffset, routey, stroke=stroke, stroke_width=2))
    d.append(draw.Line(nol["x"] + XOffset, routey, routex, routey, stroke=stroke, stroke_width=2))


    d.append(draw.Line(nel["x"], nel["y"], nel["x"] - XOffset, nel["y"], stroke=stroke, stroke_width=2))
    d.append(draw.Line(nel["x"] - XOffset, nel["y"], nel["x"] - XOffset, routey, stroke=stroke, stroke_width=2))
    d.append(draw.Line(nel["x"] - XOffset, routey, routex, routey, stroke=stroke, stroke_width=2))


def get_node_port_temp_graph_dict(graph_dict, node_level_dict, level_dict, undefined_rank_nodes):
    node_port_val = {}

    for i in node_level_dict.keys():
        if i not in undefined_rank_nodes:
            node_port_val[i] = {}
            node_port_val[i]["checked"] = []
            node_port_val[i]["top"] = []
            node_port_val[i]["bottom"] = []
            node_port_val[i]["left"] = []
            node_port_val[i]["right"] = []

    # avoid same node neighbor pair
    check_same_node = []
    temp_graph_dict = {}

    for node_val, node_details in graph_dict.items():
        if node_val not in undefined_rank_nodes:

            for i in node_details:
                node_neighbor_str = None

                node_neighbor_str = [node_val] + [i["nodePort"]] + [i["neighborDevice"]] + [i["neighborPort"]]

                node_neighbor_str.sort()
                node_neighbor_str = "_".join(node_neighbor_str)

                if node_neighbor_str not in check_same_node:
                    check_same_node.append(node_neighbor_str)
                    if node_val not in temp_graph_dict.keys():
                        temp_graph_dict[node_val] = [i]
                    else:
                        temp_graph_dict[node_val] = temp_graph_dict[node_val] + [i]

                #node_level_dict
                # set top and bottom port values
                if node_level_dict[node_val] < node_level_dict[i["neighborDevice"]]:
                    if i["nodePort"] not in node_port_val[node_val]["bottom"] and i["nodePort"] and i["nodePort"] not in node_port_val[node_val]["checked"]:
                        node_port_val[node_val]["bottom"] = node_port_val[node_val]["bottom"] + [i["nodePort"]]
                        node_port_val[node_val]["checked"] = node_port_val[node_val]["checked"] + [i["nodePort"]]

                    if i["neighborPort"] not in node_port_val[i["neighborDevice"]]["top"] and i["neighborPort"] and i["neighborPort"] not in node_port_val[i["neighborDevice"]]["checked"]:
                        node_port_val[i["neighborDevice"]]["top"] = node_port_val[i["neighborDevice"]]["top"] + [i["neighborPort"]]
                        node_port_val[i["neighborDevice"]]["checked"] = node_port_val[i["neighborDevice"]]["checked"] + [i["neighborPort"]]

                if node_level_dict[node_val] > node_level_dict[i["neighborDevice"]]:
                    if i["nodePort"] not in node_port_val[node_val]["top"] and i["nodePort"] and i["nodePort"] not in node_port_val[node_val]["checked"]:
                        node_port_val[node_val]["top"] = node_port_val[node_val]["top"] + [i["nodePort"]]
                        node_port_val[node_val]["checked"] = node_port_val[node_val]["checked"] + [i["nodePort"]]

                    if i["neighborPort"] not in node_port_val[i["neighborDevice"]]["bottom"] and i["neighborPort"] and i["neighborPort"] not in node_port_val[i["neighborDevice"]]["checked"]:
                        node_port_val[i["neighborDevice"]]["bottom"] = node_port_val[i["neighborDevice"]]["bottom"] + [i["neighborPort"]]
                        node_port_val[i["neighborDevice"]]["checked"] = node_port_val[i["neighborDevice"]]["checked"] + [i["neighborPort"]]

    for _,level_list in level_dict.items():
        level_list.sort(key=natural_sort_key)

        for i in range(len(level_list) - 1):
            for j in range(i+1,len(level_list)): 
                for node_detail in graph_dict[level_list[i]]:
                    if node_detail["neighborDevice"] == level_list[j]:
                        #left node => right port    
                        if (node_detail["nodePort"] not in node_port_val[level_list[i]]["right"]) and (node_detail["nodePort"] not in node_port_val[level_list[i]]["checked"]):
                            node_port_val[level_list[i]]["right"] = node_port_val[level_list[i]]["right"] + [node_detail["nodePort"]]
                            node_port_val[level_list[i]]["checked"] = node_port_val[level_list[i]]["checked"] + [node_detail["nodePort"]]
                        
                        #right node => left port 
                        if (node_detail["neighborPort"] not in node_port_val[level_list[j]]["left"]) and (node_detail["neighborPort"] not in node_port_val[level_list[j]]["checked"]):
                            node_port_val[level_list[j]]["left"] = node_port_val[level_list[j]]["left"] + [node_detail["neighborPort"]]
                            node_port_val[level_list[j]]["checked"] = node_port_val[level_list[j]]["checked"] + [node_detail["neighborPort"]]

    return node_port_val, temp_graph_dict                        
