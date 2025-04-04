# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from pathlib import Path

from pydantic import BaseModel, ConfigDict, Field, field_validator

from .test_spec import TestSpec


class InputFactorySettings(BaseModel):
    """
    Model defining settings for test input generation.

    Attributes:
    ----------
        allow_bgp_vrfs : bool
            Whether to include BGP neighbors in VRFs.
    """

    allow_bgp_vrfs: bool = Field(default=False)


class AvdCatalogGenerationSettings(BaseModel):
    """
    Model defining settings for the AVD-generated ANTA catalog.

    Used in `pyavd.get_device_anta_catalog` to customize the AVD test catalog generation.

    Attributes:
    ----------
        input_factory_settings : InputFactorySettings
            Settings for test input generation.
        run_tests : list[str]
            List of ANTA test names to run.
        skip_tests : list[str]
            List of ANTA test names to skip. Takes precedence over `run_tests`.
        custom_test_specs : list[TestSpec]
            List of custom test specs.
        output_dir : str | Path | None, optional
            Directory to output test catalog.
        ignore_is_deployed : bool
            Whether to ignore the `is_deployed` key in the structured config.
            When set to `True`, the catalog will still be generated even if the `is_deployed` key is `False`.
    """

    model_config = ConfigDict(extra="forbid", arbitrary_types_allowed=True)

    input_factory_settings: InputFactorySettings = Field(default_factory=InputFactorySettings)
    run_tests: list[str] = Field(default_factory=list)
    skip_tests: list[str] = Field(default_factory=list)
    custom_test_specs: list[TestSpec] = Field(default_factory=list)
    output_dir: str | Path | None = Field(default=None)
    ignore_is_deployed: bool = Field(default=False)

    @field_validator("output_dir")
    @classmethod
    def validate_output_dir(cls, value: str | Path | None) -> Path | None:
        if value is None:
            return None
        path = Path(value)
        if not (path.exists() and path.is_dir()):
            msg = f"Provided output_dir {value} does not exist or is not a directory"
            raise ValueError(msg)
        return path
