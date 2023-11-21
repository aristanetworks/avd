# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import re
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Callable, ClassVar, Generator

if TYPE_CHECKING:
    from io import TextIOWrapper

    from .results_manager import ResultsManager


class MDReportBase(ABC):
    """Base class for generating the validation markdown report based on test results managed by ResultsManager."""

    def __init__(self, mdfile: TextIOWrapper, results: ResultsManager) -> None:
        """Initialize the MDReportBase with an open markdown file object to write to and a ResultsManager instance.

        Args:
        ----
            mdfile (TextIOWrapper): An open file object to write the markdown data into.
            results (ResultsManager): The ResultsManager instance containing all test results.
        """
        self.mdfile = mdfile
        self.results = results

    @abstractmethod
    def generate_section(self) -> None:
        """Abstract method to generate a specific section of the markdown report.

        Must be implemented by subclasses.
        """

    def generate_header_name(self) -> str:
        """Generate a formatted header name based on the class name.

        Returns:
        -------
            str: Formatted header name.

        Example:
        -------
            `ValidateStateReport` will become Validate State Report.
        """
        class_name = self.__class__.__name__
        return re.sub(r"(?<!^)(?=[A-Z])", " ", class_name).title()

    def generate_table(self, table_header: list[str], row_generator: Callable[[], Generator[str, None, None]]) -> None:
        """Generate a table with a header and multiple rows.

        Args:
        ----
            table_header (list[str]): The table header.
            row_generator (Callable): The rows generator function.
        """
        self.write_table_header(table_header)
        for row in row_generator():
            self.mdfile.write(row)
        self.mdfile.write("\n")

    def write_header(self, heading_level: int) -> None:
        """Write a markdown header to the markdown file.

        Args:
        ----
            heading_level (int): The level of the heading (1-6).

        Example:
        -------
            ## Test Results Summary
        """
        # Ensure the heading level is within the valid range of 1 to 6
        heading_level = max(1, min(heading_level, 6))
        header_name = self.generate_header_name()
        heading = "#" * heading_level + " " + header_name
        self.mdfile.write(f"{heading}\n\n")

    def write_table_header(self, headers: list[str]) -> None:
        """Write a table header to the markdown file.

        Args:
        ----
            headers (list[str]): List of header strings for the table.
        """
        self.mdfile.write("\n".join(headers) + "\n")


class ValidateStateReport(MDReportBase):
    """Generate the `# Validate State Report` section of the markdown report."""

    def generate_report(self, cls: type | None = None, *, is_root: bool = True) -> None:
        """Recursively generates report sections for each inner classes.

        Args:
        ----
            cls: Internal use for recursive calls.
            is_root (bool): Flag indicating if this is the root call.
        """
        # Determine the class to process; default to the current class on the first call.
        if cls is None:
            cls = self.__class__

        if is_root:
            self.generate_section()

        # Iterate through inner classes and generate their respective sections
        for element in cls.__dict__.values():
            if isinstance(element, type) and issubclass(element, MDReportBase):
                inner_cls_instance = element(self.mdfile, self.results)
                inner_cls_instance.generate_section()
                self.generate_report(cls=element, is_root=False)

    def generate_section(self) -> None:
        """Generate the `# Validate State Report` section of the markdown report."""
        self.write_header(heading_level=1)
        self.mdfile.write(
            """**Table of Contents:**

- [Validate State Report](validate-state-report)
  - [Test Results Summary](#test-results-summary)
  - [Failed Test Results Summary](#failed-test-results-summary)
  - [All Test Results](#all-test-results)

""",
        )

    class TestResultsSummary(MDReportBase):
        """Generate the `## Test Results Summary` section of the markdown report."""

        def generate_section(self) -> None:
            """Generate the `## Test Results Summary` section of the markdown report."""
            self.write_header(heading_level=2)

        class SummaryTotals(MDReportBase):
            """Generate the `### Summary Totals` section of the markdown report."""

            TABLE_HEADER: ClassVar[list[str]] = [
                "| Total Tests | Total Tests Passed | Total Tests Failed | Total Tests Skipped |",
                "| ----------- | ------------------ | ------------------ | ------------------- |",
            ]

            def generate_rows(self) -> Generator[str, None, None]:
                """Generate the rows of the results table."""
                yield (
                    f"| {self.results.total_tests} | {self.results.total_tests_passed} | {self.results.total_tests_failed} |"
                    f" {self.results.total_tests_skipped} |\n"
                )

            def generate_section(self) -> None:
                """Generate the `### Summary Totals` section of the markdown report."""
                self.write_header(heading_level=3)
                self.generate_table(table_header=self.TABLE_HEADER, row_generator=self.generate_rows)

        class SummaryTotalsDevicesUnderTests(MDReportBase):
            """Generate the `### Summary Totals Devices Under Tests` section of the markdown report."""

            TABLE_HEADER: ClassVar[list[str]] = [
                "| DUT | Total Tests | Tests Passed | Tests Failed | Tests Skipped | Categories Failed | Categories Skipped |",
                "| --- | ----------- | ------------ | ------------ | ------------- | ----------------- | ------------------ |",
            ]

            def generate_rows(self) -> Generator[str, None, None]:
                """Generate the rows of the results table."""
                for dut, stat in self.results.dut_stats.items():
                    total_tests = stat["tests_passed"] + stat["tests_failed"] + stat["tests_skipped"]
                    categories_failed = ", ".join(sorted(stat["categories_failed"]))
                    categories_skipped = ", ".join(sorted(stat["categories_skipped"]))
                    yield (
                        f"| {dut} | {total_tests} | {stat['tests_passed']} | {stat['tests_failed']} | {stat['tests_skipped']} | {categories_failed} |"
                        f" {categories_skipped} |\n"
                    )

            def generate_section(self) -> None:
                """Generate the `### Summary Totals Devices Under Tests` section of the markdown report."""
                self.write_header(heading_level=3)
                self.generate_table(table_header=self.TABLE_HEADER, row_generator=self.generate_rows)

        class SummaryTotalsPerCategory(MDReportBase):
            """Generate the `### Summary Totals Per Category` section of the markdown report."""

            TABLE_HEADER: ClassVar[list[str]] = [
                "| Test Category | Total Tests | Tests Passed | Tests Failed | Tests Skipped |",
                "| ------------- | ----------- | ------------ | ------------ | ------------- |",
            ]

            def generate_rows(self) -> Generator[str, None, None]:
                """Generate the rows of the results table."""
                for category, stat in self.results.category_stats.items():
                    total_tests = stat["tests_passed"] + stat["tests_failed"] + stat["tests_skipped"]
                    yield f"| {category} | {total_tests} | {stat['tests_passed']} | {stat['tests_failed']} | {stat['tests_skipped']} |\n"

            def generate_section(self) -> None:
                """Generate the `### Summary Totals Per Category` section of the markdown report."""
                self.write_header(heading_level=3)
                self.generate_table(table_header=self.TABLE_HEADER, row_generator=self.generate_rows)

    class FailedTestResultsSummary(MDReportBase):
        """Generate the `## Failed Test Results Summary` section of the markdown report."""

        TABLE_HEADER: ClassVar[list[str]] = [
            "| Test ID | Node | Test Categories | Test Description | Test | Test Result | Failure Reasons |",
            "| ------- | ---- | --------------- | ---------------- | ---- | ----------- | --------------- |",
        ]

        def generate_rows(self) -> Generator[str, None, None]:
            """Generate the rows of the results table."""
            for result in self.results.failed_tests:
                failure_reasons = ", ".join(result["failure_reasons"])
                categories = ", ".join(result["test_categories"])
                yield (
                    f"| {result['test_id'] or '-'} | {result['node'] or '-'} | {categories or '-'} | {result['test_description'] or '-'} |"
                    f" {result['test'] or '-'} | {result['result'] or '-'} | {failure_reasons or '-'} |\n"
                )

        def generate_section(self) -> None:
            """Generate the `## Failed Test Results Summary` section of the markdown report."""
            self.write_header(heading_level=2)
            self.generate_table(table_header=self.TABLE_HEADER, row_generator=self.generate_rows)

    class AllTestResults(MDReportBase):
        """Generates the `## All Test Results` section of the markdown report.

        This section is generated only if the report includes all results.
        """

        TABLE_HEADER: ClassVar[list[str]] = [
            "| Test ID | Node | Test Categories | Test Description | Test | Test Result | Failure Reasons |",
            "| ------- | ---- | --------------- | ---------------- | ---- | ----------- | --------------- |",
        ]

        def generate_rows(self) -> Generator[str, None, None]:
            """Generate the rows of the results table."""
            for result in self.results.all_tests:
                failure_reasons = ", ".join(result["failure_reasons"])
                categories = ", ".join(result["test_categories"])
                yield (
                    f"| {result['test_id'] or '-'} | {result['node'] or '-'} | {categories or '-'} | {result['test_description'] or '-'} |"
                    f" {result['test'] or '-'} | {result['result'] or '-'} | {failure_reasons or '-'} |\n"
                )

        def generate_section(self) -> None:
            """Generate the `## All Test Results` section of the markdown report.

            This section is generated only if the report includes all results.
            """
            if not self.results.only_failed_tests:
                self.write_header(heading_level=2)
                self.generate_table(table_header=self.TABLE_HEADER, row_generator=self.generate_rows)
