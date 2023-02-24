from urllib.request import urlopen

from yaml import safe_load

from ansible_collections.arista.avd.plugins.plugin_utils.errors import AristaAvdError

try:
    import jsonschema
    import jsonschema.validators
except ImportError as imp_exc:
    JSONSCHEMA_IMPORT_ERROR = imp_exc
else:
    JSONSCHEMA_IMPORT_ERROR = None


def yaml_file_loader(uri):
    """
    Load YAML file from URI
    Used to resolve $ref with file:// style
    """
    with urlopen(uri) as data:
        return safe_load(data.read().encode("UTF-8"))


def create_refresolver(schema: dict, store: dict):
    if JSONSCHEMA_IMPORT_ERROR:
        raise AristaAvdError('Python library "jsonschema" must be installed to use this plugin') from JSONSCHEMA_IMPORT_ERROR

    return jsonschema.validators.RefResolver(
        base_uri=schema.get("$id", ""),
        referrer=schema,
        handlers={
            "file": yaml_file_loader,
        },
        store=store,
    )
