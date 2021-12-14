from ansible_collections.arista.avd.plugins.modules.inventory_to_container import is_in_filter, isIterable, get_device_option_value
import os
import logging
import pytest
import yaml

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

INVENTORY_FILE = os.path.dirname(
    os.path.realpath(__file__)) + "../inventory/inventory.yml"


@pytest.fixture
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
        assert output == True

    def test_is_in_filter_valid_hostname(self):
        output = is_in_filter(hostname_filter=[
                              "arista", "aristanetworks"], hostname="test1.aristanetworks.com")
        assert output == True

    def test_is_in_filter_invalid_hostname(self):
        output = is_in_filter(
            hostname_filter=["arista", "aristanetworks"], hostname="test1.bsn.com")
        assert output == False

    # TODO: Check if this is a valid testcase. Add a type check?
    def test_is_in_filter_invalid_filter(self):
        output = is_in_filter(hostname_filter="aristanetworks",
                              hostname="test1.aristanetworks.com")
        assert output == True

    def test_isIterable_default_iterable(self):
        output = isIterable()
        assert output == False

    @pytest.mark.parametrize("DATA", IS_ITERABLE_VALID)
    def test_isIterable_valid_iterable(self, DATA):
        output = isIterable(DATA)
        assert output == True

    @pytest.mark.parametrize("DATA", IS_ITERABLE_INVALID)
    def test_isIterable_invalid_iterable(self, DATA):
        output = isIterable(DATA)
        assert output == False

    def test_isLeaf_valid_leaf(self, inventory):
        logging.info(inventory)
        pass

    def test_isLeaf_invalid_leaf(self):
        pass

    def test_isLeaf_none_leaf(self):
        pass

    def test_get_device_option_value(self):
        pass
