try:
    import jsonschema
except ImportError as imp_exc:
    JSONSCHEMA_IMPORT_ERROR = imp_exc
else:
    JSONSCHEMA_IMPORT_ERROR = None


class AristaAvdError(Exception):
    def __init__(self, message="An Error has occured in an arista.avd plugin"):
        self.message = message
        super().__init__(self.message)

    def _json_path_to_string(self, json_path):
        path = ""
        for index, elem in enumerate(json_path):
            if isinstance(elem, int):
                path += "[" + str(elem) + "]"
            else:
                if index == 0:
                    path += elem
                    continue
                path += "." + elem
        return path


class AristaAvdMissingVariableError(AristaAvdError):
    pass


class AvdSchemaError(AristaAvdError):
    def __init__(self, message="Schema Error", error=None):
        if JSONSCHEMA_IMPORT_ERROR:
            raise AristaAvdError('Python library "jsonschema" must be installed to use this plugin') from JSONSCHEMA_IMPORT_ERROR

        if isinstance(error, jsonschema.SchemaError):
            self.message = f"'Schema Error: {self._json_path_to_string(error.absolute_path)}': {error.message}"
        else:
            self.message = message
        super().__init__(self.message)


class AvdValidationError(AristaAvdError):
    def __init__(self, message: str = "Schema Error", error=None):
        if JSONSCHEMA_IMPORT_ERROR:
            raise AristaAvdError('Python library "jsonschema" must be installed to use this plugin') from JSONSCHEMA_IMPORT_ERROR

        if isinstance(error, (jsonschema.ValidationError)):
            self.message = f"'Validation Error: {self._json_path_to_string(error.absolute_path)}': {error.message}"
        else:
            self.message = message
        super().__init__(self.message)


class AvdConversionWarning(AristaAvdError):
    def __init__(self, message: str = "Data was converted to conform to schema", key=None, oldtype="unknown", newtype="unknown"):
        if key is not None:
            self.message = f"'Data Type Converted: {key} from '{oldtype}' to '{newtype}'"
        else:
            self.message = message
        super().__init__(self.message)
