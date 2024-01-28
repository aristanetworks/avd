# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import Any

from pydantic import BaseModel, model_validator

from ..vendor.utils import get, get_all


class AvdDictBaseModel(BaseModel):
    """
    Special base model for dicts, where keys with leading _ are stored in custom_data with no further validation (Using Any).
    The keys are popped from the input model to still enforce the model config "extra" for allow or forbid extra keys.

    This class does not apply to the root dict, since we do not want to parse all given data for _.
    """

    custom_data: dict[str, Any] | None = None

    @model_validator(mode="before")
    @classmethod
    def _extract_custom_data(cls, data: Any) -> dict:
        """
        Find any keys starting with _ and *move* them under custom_data
        """
        if not isinstance(data, dict):
            return data

        custom_keys = [key for key in data.keys() if str(key).startswith("_")]
        if custom_keys:
            data: dict = data.copy()
            data["custom_data"] = {key: data.pop(key) for key in custom_keys}

        return data


class AvdEosDesignsRootDictBaseModel(BaseModel):
    """
    Special base model for the root dict, where dynamic keys are mapped into relevant data models under dynamic_keys.
    The keys are popped from the input model to still enforce the model config "extra" for allow or forbid extra keys.
    """

    @model_validator(mode="before")
    @classmethod
    def _extract_custom_structured_configuration(cls, data: Any) -> dict:
        """
        Find any keys starting with any prefix defined under "custom_structured_configuration_prefix" and *move* them under "custom_structured_configurations"
        ```yaml
        custom_structured_configurations:
          - key: <full key ex. "custom_structured_configuration_router_bgp">
            value: <structured config including the suffix part of the key>
        ```
        """
        if not isinstance(data, dict):
            return data

        if not (prefixes := get(data, "custom_structured_configuration_prefix", default=["custom_structured_configuration_"])):
            return data

        excluded_keys = ["custom_structured_configuration_prefix", "custom_structured_configuration_list_merge"]
        custom_structured_configurations = []
        for prefix in prefixes:
            keys = [key for key in data.keys() if str(key).startswith(prefix) if key not in excluded_keys]
            if not keys:
                continue

            prefix_length = len(prefix)
            for key in keys:
                custom_structured_configurations.append(
                    {
                        "key": key,
                        "value": {
                            key[prefix_length:]: data[key],
                        },
                    }
                )

        if custom_structured_configurations:
            data: dict = data.copy()
            data["custom_structured_configurations"] = custom_structured_configurations

        return data

    @model_validator(mode="before")
    @classmethod
    def _extract_dynamic_keys(cls, data: Any) -> dict:
        """
        Extract content of dynamic keys and insert into data under this model:
        ```yaml
        dynamic_keys:
          <model_key ex. "node_type_keys">:
            - key: <dynamic_key ex. "l3leaf">
              value: <value of dynamic key>
        ```

        The corresponding data models are auto created by the conversion from schemas, which also sets "_dynamic_key_maps" on the class:
        ```python
        _dynamic_key_maps: list[dict] = [{'dynamic_keys_path': 'connected_endpoints_keys.key', 'model_key': 'connected_endpoints_keys'}, ...]
        ```

        Here we parse "_dynamic_key_maps" and for entry  find all values for the dynamic_keys_path (ex "node_type_keys.key") in the input data
        to identify all dynamic keys (ex "l3leaf", "spine" ...)

        Then *move* each dynamic key to dynamic_keys.<model_key>.[key=<key>, value=<value>]. This is still within the input data, so after moving,
        the data will be subject to the correct validation according to the schema.
        """
        if not isinstance(data, dict):
            return data

        if getattr(cls, "dynamic_keys", None) is None:
            return data

        data: dict = data.copy()
        for dynamic_key_map in cls.dynamic_keys._dynamic_key_maps:
            dynamic_keys_path: str = dynamic_key_map["dynamic_keys_path"]
            model_key: str = dynamic_key_map["model_key"]
            model_key_list = []

            dynamic_keys = get_all(data, dynamic_keys_path, required=True)
            # TODO: Catch the issue with the same dynamic keys
            for dynamic_key in dynamic_keys:
                # dynamic_key is one key like "l3leaf".
                if data.get(dynamic_key) is None:
                    # Do not add missing key or None.
                    continue

                model_key_list.append({"key": dynamic_key, "value": data[dynamic_key]})

            data.setdefault("dynamic_keys", {})[model_key] = model_key_list

        return data
