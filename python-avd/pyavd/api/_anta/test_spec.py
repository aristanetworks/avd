# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import BaseModel, ConfigDict, model_validator

from pyavd._anta.constants import StructuredConfigKey
from pyavd._anta.input_factories._base_classes import AntaTestInputFactory
from pyavd._anta.lib import AntaTest

if TYPE_CHECKING:
    from typing_extensions import Self


class TestSpec(BaseModel):
    """
    TestSpec model used to define an ANTA test specification in PyAVD.

    Primarily used in the `AVD_TEST_INDEX` list to define the ANTA tests to be run
    but can also be provided in the `get_device_test_catalog` PyAVD function to add custom tests.

    Attributes:
    ----------
    test_class : type[AntaTest]
        The ANTA test class to be used for the test.
    conditional_keys : list[StructuredConfigKey] | None
        Optional structured config keys that are required to run the test.
    input_factory : type[AntaTestInputFactory] | None
        Optional input factory class that generates the `AntaTest.Input` models (inputs) for the test.
        Required field if the ANTA test needs inputs.
    """

    model_config = ConfigDict(extra="forbid")
    test_class: type[AntaTest]
    conditional_keys: list[StructuredConfigKey] | None = None
    input_factory: type[AntaTestInputFactory] | None = None

    @model_validator(mode="after")
    def check_inputs(self) -> Self:
        """Check if `input_factory` is provided when the ANTA test requires inputs."""
        # Check if the test class has an `Input` model and if it has required fields
        if "Input" in self.test_class.__dict__ and isinstance((input_class := self.test_class.__dict__["Input"]), AntaTest.Input):
            for f_name, f_info in input_class.model_fields.items():
                # No need to check the base class fields
                if f_name in {"result_overwrite", "filters"}:
                    continue
                # If a required field is present, an input factory must be provided
                if f_info.is_required() and self.input_factory is None:
                    msg = f"TestSpec for {self.test_class.name} must have `input_factory`"
                    raise ValueError(msg)

        return self
