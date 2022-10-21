"""
conftest.py file for schema testing
"""

import pytest

from ansible_collections.arista.avd.plugins.plugin_utils.schema.avdschema import AvdSchema
from ansible_collections.arista.avd.plugins.plugin_utils.schema.avdschemaresolver import AvdSchemaResolver
from ansible_collections.arista.avd.plugins.plugin_utils.schema.avdvalidator import AvdValidator


@pytest.fixture
def avdvalidator_factory():
    def factory(schema):
        return AvdValidator(schema)

    return factory


@pytest.fixture
def avdschema_factory():
    def factory(schema):
        return AvdSchema(schema)

    return factory


@pytest.fixture
def avdschemaresolver_factory():
    def factory(schema):
        return AvdSchemaResolver(schema)

    return factory
