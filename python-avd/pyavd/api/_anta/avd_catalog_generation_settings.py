# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .avd_test_spec import AvdTestSpec


@dataclass(frozen=True)
class AvdCatalogGenerationSettings:
    """
    Model defining settings for the AVD-generated ANTA catalog.

    Used in `pyavd.get_device_test_catalog` to customize the AVD test catalog generation.
    """

    run_tests: tuple[str, ...] = field(default_factory=tuple)
    """List of ANTA test names to run. If provided, only these tests (minus skipped ones) will run."""
    skip_tests: tuple[str, ...] = field(default_factory=tuple)
    """List of ANTA test names to skip. Takes precedence over `run_tests`."""
    custom_test_specs: tuple[AvdTestSpec, ...] = field(default_factory=tuple)
    """List of custom AvdTestSpec instances to generate additional tests in the catalog."""
    output_dir: str | Path | None = field(default=None)
    """Directory to output the test catalog. Must exist if provided."""
    extra_fabric_validation: bool = field(default=False)
    """Whether to include extra fabric-wide validation tests in the catalog."""

    def __post_init__(self) -> None:
        """Validate the `output_dir` attribute if provided."""
        if self.output_dir is None:
            return
        path = Path(self.output_dir)
        if not (path.exists() and path.is_dir()):
            msg = f"Provided output_dir {self.output_dir} does not exist or is not a directory."
            raise ValueError(msg)
