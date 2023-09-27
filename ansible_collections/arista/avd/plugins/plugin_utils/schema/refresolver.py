# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from ansible_collections.arista.avd.plugins.plugin_utils.errors import AristaAvdError

try:
    import jsonschema
    import jsonschema.validators
except ImportError as imp_exc:
    JSONSCHEMA_IMPORT_ERROR = imp_exc
else:
    JSONSCHEMA_IMPORT_ERROR = None


def create_refresolver(schema: dict, store: dict):
    if JSONSCHEMA_IMPORT_ERROR:
        raise AristaAvdError('Python library "jsonschema" must be installed to use this plugin') from JSONSCHEMA_IMPORT_ERROR

    return jsonschema.validators.RefResolver(
        base_uri=schema.get("$id", ""),
        referrer=schema,
        store=store,
    )
