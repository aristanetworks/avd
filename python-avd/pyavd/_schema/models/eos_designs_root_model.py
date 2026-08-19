# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from collections import ChainMap
from collections.abc import Iterator, Mapping
from typing import TYPE_CHECKING, TypeVar

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen

from .avd_list import AvdList
from .avd_model import AvdModel

if TYPE_CHECKING:
    from typing_extensions import Self

    from pyavd._eos_designs.schema import EosDesigns

    T = TypeVar("T", bound="EosDesignsRootModel")


SKIP_KEYS = ["custom_structured_configuration_list_merge", "custom_structured_configuration_prefix"]


class EosDesignsRootModel(AvdModel):
    @classmethod
    def _from_dict(cls, data: Mapping, load_custom_structured_config: bool = True) -> Self:
        """
        Returns a new instance loaded with the data from the given dict.

        The EosDesignsRootModel is special because it will load `custom_structured_configuration_prefix` and search for any keys prefixed with those.
        Found keys will be loaded into the `_custom_structured_configurations` model.

        Dynamic keys are normalized under `_dynamic_keys` by input validation before loading this model.

        Args:
            data: A mapping containing the EosDesigns input data to be loaded.
            load_custom_structured_config: Some custom structured config contains inline Jinja templates relying on variables produced by EosDesignsFacts.
                To avoid such templates breaking the type checks, we can skip loading custom_structured_configuration during the facts phase by setting this
                to False.

        """
        if not isinstance(data, Mapping):
            msg = f"Expecting 'data' as a 'Mapping' when loading data into '{cls.__name__}'. Got '{type(data)}"
            raise TypeError(msg)

        if not load_custom_structured_config:
            return super()._from_dict(data)

        custom_structured_configurations = cls._CustomStructuredConfigurations(cls._get_csc_items(data))
        return super()._from_dict(ChainMap({"_custom_structured_configurations": custom_structured_configurations}, data))

    @classmethod
    def _get_csc_items(cls, data: Mapping) -> Iterator[EosDesigns._CustomStructuredConfigurationsItem]:
        """
        Returns a list of _CustomStructuredConfigurationsItem objects containing each custom structured configuration extracted from the inputs.

        Find any keys starting with any prefix defined under "custom_structured_configuration_prefix".
        """
        prefixes = data.get("custom_structured_configuration_prefix", cls._get_field_default_value("custom_structured_configuration_prefix"))
        if not isinstance(prefixes, (list, AvdList)):
            # Invalid prefix format.
            return

        for prefix in prefixes:
            if not isinstance(prefix, str):
                # Invalid prefix format.
                continue

            if not (matching_keys := [key for key in data if str(key).startswith(prefix) and key not in SKIP_KEYS]):
                continue

            prefix_length = len(prefix)
            for key in matching_keys:
                yield cls._CustomStructuredConfigurationsItem(key=key, value=EosCliConfigGen._from_dict({key[prefix_length:]: data[key]}))
