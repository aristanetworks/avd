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

    def get_filtered_test_specs(self) -> list[AvdTestSpec]:
        """Return a filtered list of AvdTestSpec based on run_tests, skip_tests, and custom_test_specs."""
        from pyavd._anta.index import AVD_TEST_INDEX  # noqa: PLC0415

        run_tests_set = set(self.run_tests)
        skip_tests_set = set(self.skip_tests)

        # Check for invalid test names across all filters
        test_names = {test.test_class.name for test in AVD_TEST_INDEX}
        invalid_test_names = (run_tests_set | skip_tests_set) - test_names
        if invalid_test_names:
            msg = f"Invalid test name(s) in 'run_tests' or 'skip_tests' filters: {', '.join(sorted(invalid_test_names))}"
            raise ValueError(msg)

        # Remove any tests from run_tests that are in skip_tests
        remaining_run_tests = run_tests_set - skip_tests_set

        final_test_specs: list[AvdTestSpec] = []

        for test in AVD_TEST_INDEX:
            name = test.test_class.name

            # Skip tests explicitly mentioned in skip_tests
            if name in self.skip_tests:
                continue

            # If run_tests is specified, only include tests in remaining_run_tests
            if self.run_tests and name not in remaining_run_tests:
                continue

            final_test_specs.append(test)

        # Add custom test specs
        final_test_specs.extend(self.custom_test_specs)

        return final_test_specs
