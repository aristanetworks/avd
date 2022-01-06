from ansible_collections.arista.avd.plugins.modules.inventory_to_container import is_in_filter, isIterable, get_device_option_value, serialize, get_devices, isLeaf, get_containers
import os
import logging
import pytest
import yaml
import treelib
import json

IS_ITERABLE_VALID = [
    ("string1", "string2", "string3", "string4"),
    {"key1": "value1", "key2": "value2", "key3": "value3"},
    ["string1", "string2", "string3", "string4"],
    "string1"
]

IS_ITERABLE_INVALID = [
    None,
    0
]

PARENT_CONTAINER = {
    "default_parent": {"parent": "Tenant",
                       "expected_output": {'all': {}, 'CVP': {'devices': ['cv_ztp', 'cv_server'], 'parent_container': 'all'}, 'DC1': {'parent_container': 'all'}, 'DC1_FABRIC': {'parent_container': 'DC1'}, 'DC1_L2LEAFS': {'parent_container': 'DC1_FABRIC'}, 'DC1_L2LEAF1': {'devices': ['DC1-L2LEAF1A'], 'parent_container': 'DC1_L2LEAFS'}, 'DC1_L2LEAF2': {'devices': ['DC1-L2LEAF2A'], 'parent_container': 'DC1_L2LEAFS'}, 'DC1_L3LEAFS': {'parent_container': 'DC1_FABRIC'}, 'DC1_LEAF1': {'devices': ['DC1-LEAF1A', 'DC1-LEAF1B'], 'parent_container': 'DC1_L3LEAFS'}, 'DC1_LEAF2': {'devices': ['DC1-LEAF2A', 'DC1-LEAF2B'], 'parent_container': 'DC1_L3LEAFS'}, 'DC1_SPINES': {'devices': ['DC1-SPINE1', 'DC1-SPINE2'], 'parent_container': 'DC1_FABRIC'}, 'DC1_SERVERS': {'devices': [], 'parent_container': 'DC1'}, 'DC1_TENANTS_NETWORKS': {'devices': [], 'parent_container': 'DC1'}}
                       },
    "non_default_parent": {"parent": "CVP",
                           "expected_output":  {'CVP': {'parent_container': 'Tenant'}}
                           }
}

INVENTORY_FILE = os.path.dirname(
    os.path.realpath(__file__)) + "/../../inventory/inventory.yml"

ROOT_CONTAINER = 'Tenant'

TREELIB = treelib.tree.Tree()
TREELIB.create_node("Tenant", "Tenant")
TREELIB.create_node("CVP", "CVP", parent="Tenant")
TREELIB.create_node("DC1", "DC1", parent="Tenant")
TREELIB.create_node("Leaf1", "Leaf1", parent="DC1")
TREELIB.create_node("Leaf2", "Leaf2", parent="DC1")


@pytest.fixture(scope="session")
def inventory():
    with open(INVENTORY_FILE, 'r', encoding='utf8') as stream:
        try:
            inventory_content = yaml.safe_load(stream)
        except yaml.YAMLError as e:
            logging.error(e)
            return None
        return inventory_content


class TestInventoryToContainer:
    def test_is_in_filter_default_filter(self):
        output = is_in_filter(hostname="aristanetworks.com")
        assert output

    def test_is_in_filter_valid_hostname(self):
        output = is_in_filter(hostname_filter=[
                              "arista", "aristanetworks"], hostname="test1.aristanetworks.com")
        assert output

    def test_is_in_filter_invalid_hostname(self):
        output = is_in_filter(
            hostname_filter=["arista", "aristanetworks"], hostname="test1.bsn.com")
        assert output is False

    # TODO: Check if this is a valid testcase. Add a type check?
    def test_is_in_filter_invalid_filter(self):
        output = is_in_filter(hostname_filter="aristanetworks",
                              hostname="test1.aristanetworks.com")
        assert output

    def test_isIterable_default_iterable(self):
        output = isIterable()
        assert output is False

    @pytest.mark.parametrize("DATA", IS_ITERABLE_VALID)
    def test_isIterable_valid_iterable(self, DATA):
        output = isIterable(DATA)
        assert output

    @pytest.mark.parametrize("DATA", IS_ITERABLE_INVALID)
    def test_isIterable_invalid_iterable(self, DATA):
        output = isIterable(DATA)
        assert output is False

    def test_isLeaf_valid_leaf(self):
        output = isLeaf(TREELIB, "Leaf1")
        assert output

    def test_isLeaf_invalid_leaf(self):
        output = isLeaf(TREELIB, "DC1")
        assert output is False

    def test_isLeaf_none_leaf(self):
        output = isLeaf(TREELIB, None)
        assert output is False

    def test_get_device_option_value_valid(self, inventory):
        data = inventory['all']['children']['CVP']['hosts']
        output = get_device_option_value(
            device_data_dict=data,
            option_name='cv_server')
        assert output
        assert isinstance(output, dict)

    def test_get_device_option_value_invalid(self, inventory):
        data = inventory['all']['children']['CVP']['hosts']
        output = get_device_option_value(
            device_data_dict=data,
            option_name='is_deployed')
        assert output == None

    def test_get_device_option_value_none(self, inventory):
        data = inventory['all']['children']['CVP']['hosts']
        output = get_device_option_value(
            device_data_dict=data,
            option_name=None)
        assert output == None

    def test_get_device_option_value_empty_data(self, inventory):
        data = inventory['all']['children']['CVP']['hosts']
        output = get_device_option_value(
            device_data_dict=None,
            option_name='cv_server')
        assert output == None

    def test_get_devices_empty_inventory(self):
        output = get_devices(None)
        assert output == None

    def test_get_devices_default_search_container(self, inventory):
        output = get_devices(inventory)
        assert output == None

    def test_get_devices_non_default_search_container(self, inventory):
        expected_output = ['DC1-SPINE1', 'DC1-SPINE2']
        output = get_devices(
            inventory, search_container="DC1_SPINES", devices=[])
        assert output == expected_output

    def test_get_devices_preexisting_devices(self, inventory):
        devices = ["TEST_DEVICE"]
        expected_output = ['DC1-SPINE1', 'DC1-SPINE2']
        output = get_devices(
            inventory, search_container="DC1_SPINES", devices=devices)
        assert output == ["TEST_DEVICE"] + expected_output

    def test_get_devices_preexisting_devices(self, inventory):
        expected_output = ['DC1-SPINE2']
        output = get_devices(
            inventory, search_container="DC1_SPINES", devices=[], device_filter=["SPINE2"])
        assert output == expected_output

    @pytest.mark.parametrize("DATA", [None])
    def test_serialize_empty_inventory(self, DATA):
        output = serialize(DATA)
        assert output == None

    def test_serialize_valid_inventory(self, inventory):
        output = serialize(inventory)
        assert isinstance(output, treelib.tree.Tree)
        tree_dict = json.loads(output.to_json())
        assert (list(tree_dict.keys()))[0] == ROOT_CONTAINER

    @pytest.mark.parametrize("DATA", PARENT_CONTAINER.values(), ids=PARENT_CONTAINER.keys())
    def test_serialize_parent_container(self, DATA, inventory):
        output = serialize(inventory, parent_container=DATA["parent"])
        assert isinstance(output, treelib.tree.Tree)
        tree_dict = json.loads(output.to_json())
        assert (list(tree_dict.keys()))[0] == ROOT_CONTAINER

    def test_serialize_none_parent_container_with_tree_topology(self, inventory):
        tree = treelib.tree.Tree()
        output = serialize(inventory, tree_topology=tree)
        assert isinstance(output, treelib.tree.Tree)
        tree_dict = json.loads(output.to_json())
        assert (list(tree_dict.keys()))[0] == "all"

    def test_serialize_non_default_parent_container_with_tree_topology(self, inventory):
        tree = treelib.tree.Tree()
        tree.create_node("DC2", "DC2")
        output = serialize(
            inventory, parent_container="DC2", tree_topology=tree)
        tree_dict = json.loads(output.to_json())
        assert (list(tree_dict.keys()))[0] == "DC2"

    @pytest.mark.parametrize("DATA", PARENT_CONTAINER.values(), ids=PARENT_CONTAINER.keys())
    def test_get_containers(self, DATA, inventory):
        output = get_containers(
            inventory, parent_container=DATA["parent"], device_filter=["all"])
        assert output == DATA["expected_output"]
