# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING

from pyavd._anta.lib import AntaTest

if TYPE_CHECKING:
    from pyavd._anta.input_factories._base_classes import AntaTestInputFactory


@dataclass(frozen=True)
class AvdTestSpec:
    """
    Model used to define an ANTA test specification in PyAVD.

    Primarily used internally to build a default list of ANTA tests to be run
    but can also be provided in the `get_device_test_catalog` PyAVD function to add custom tests.
    """

    test_class: type[AntaTest]
    """The ANTA test class to be used for the test."""
    input_factory: type[AntaTestInputFactory] | None = field(default=None)
    """
    Optional input factory class that generates the `AntaTest.Input` models (inputs) for the test.

    Required field if the ANTA test needs inputs.
    """

    def __post_init__(self) -> None:
        """Check if `input_factory` is provided when the ANTA test requires inputs."""
        input_class = self.test_class.__dict__.get("Input", None)
        if not (isinstance(input_class, type) and issubclass(input_class, AntaTest.Input)):
            return

        # No need to check the base class fields
        excluded_fields = {"result_overwrite", "filters"}

        requires_input = any(f_info.is_required() for f_name, f_info in input_class.model_fields.items() if f_name not in excluded_fields)

        if requires_input and self.input_factory is None:
            msg = f"AvdTestSpec for {self.test_class.name} must have `input_factory`."
            raise ValueError(msg)
