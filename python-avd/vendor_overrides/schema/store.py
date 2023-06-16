from functools import lru_cache
from pickle import load

from pyavd.vendor.schema.default_schemas import DEFAULT_PICKLED_SCHEMAS


@lru_cache
def create_store():
    store = {}
    for id, schema_file in DEFAULT_PICKLED_SCHEMAS.items():
        with open(schema_file, "rb") as file:
            store[id] = load(file)

    return store
