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

    Primarily used in the `AVD_TEST_INDEX` list to define the ANTA tests to be run
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
        # Check if the test class has an `Input` model and if it has required fields
        if "Input" in self.test_class.__dict__ and issubclass((input_class := self.test_class.__dict__["Input"]), AntaTest.Input):
            for f_name, f_info in input_class.model_fields.items():
                # No need to check the base class fields
                if f_name in {"result_overwrite", "filters"}:
                    continue
                # If a required field is present, an input factory must be provided
                if f_info.is_required() and self.input_factory is None:
                    msg = f"AvdTestSpec for {self.test_class.name} must have `input_factory`"
                    raise ValueError(msg)
