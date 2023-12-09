# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import inspect
import re
from typing import TYPE_CHECKING, Callable, Generator

if TYPE_CHECKING:
    from io import TextIOWrapper

    from .results_manager import ResultsManager


class MDReportUtils:
    """Provide utility methods for generating and formatting sections of a Markdown report."""

    @staticmethod
    def generate_heading_name(function_name: str) -> str:
        """Generate a formatted heading name based on a given function name.

        The function removes the '_generate_' prefix if it exists, replaces underscores with spaces and convert to title case.

        Args:
        ----
            function_name (str): The function name to be formatted.

        Returns:
        -------
            str: The formatted heading name.
        """
        readable_name = re.sub(r"^_generate_", "", function_name)
        return readable_name.replace("_", " ").title()

    def write_table(self, table_heading: list[str], rows_generator: Callable[[], Generator[str, None, None]]) -> None:
        """Write a markdown table with a table heading and multiple rows to the markdown file.

        Args:
        ----
            table_heading (list[str]): List of strings to join for the table heading.
            rows_generator (Callable): The rows generator function.
        """
        self.mdfile.write("\n".join(table_heading) + "\n")
        for row in rows_generator(self):
            self.mdfile.write(row)
        self.mdfile.write("\n")

    def write_heading(self, heading_level: int) -> None:
        """Write a markdown heading to the markdown file.

        The heading name used is the caller function name.

        Args:
        ----
            heading_level (int): The level of the heading (1-6).

        Example:
        -------
            ## Test Results Summary
        """
        # Ensure the heading level is within the valid range of 1 to 6
        heading_level = max(1, min(heading_level, 6))
        heading_name = self.generate_heading_name(inspect.stack()[1].function)
        heading = "#" * heading_level + " " + heading_name
        self.mdfile.write(f"{heading}\n\n")


class MDReport(MDReportUtils):
    """Generate and write the validation markdown report based on test results managed by ResultsManager.

    The class uses the `generate_report` method as the main method to call the private methods,
    each representing a section of the report, to generate and write the final report.
    """

    def __init__(self, mdfile: TextIOWrapper, results: ResultsManager) -> None:
        """Initialize the MDReport with an open markdown file object to write to and a ResultsManager instance.

        Args:
        ----
            mdfile (TextIOWrapper): An open file object to write the markdown data into.
            results (ResultsManager): The ResultsManager instance containing all test results.
        """
        self.mdfile = mdfile
        self.results = results

    def generate_report(self) -> None:
        """Generate and write the various sections of the markdown report.

        The order in which the private methods are called represents the order of the sections in the final report.
        """
        self._generate_validate_state_report()
        self._generate_test_results_summary()
        self._generate_failed_test_results_summary()
        if not self.results.only_failed_tests:
            self._generate_all_test_results()

    def _generate_validate_state_report(self) -> None:
        """Generate the `# Validate State Report` section of the markdown report."""
        self.write_heading(heading_level=1)
        self.mdfile.write(
            """**Table of Contents:**

- [Validate State Report](validate-state-report)
  - [Test Results Summary](#test-results-summary)
  - [Failed Test Results Summary](#failed-test-results-summary)
  - [All Test Results](#all-test-results)

""",
        )

    def _generate_test_results_summary(self) -> None:
        """Generate the `## Test Results Summary` section of the markdown report."""
        self.write_heading(heading_level=2)
        self._generate_summary_totals()
        self._generate_summary_totals_devices_under_tests()
        self._generate_summary_totals_per_category()

    def _generate_summary_totals(self) -> None:
        """Generate the `### Summary Totals` section of the markdown report."""
        table_heading = [
            "| Total Tests | Total Tests Passed | Total Tests Failed | Total Tests Skipped |",
            "| ----------- | ------------------ | ------------------ | ------------------- |",
        ]

        def generate_rows(self: MDReport) -> Generator[str, None, None]:
            """Generate the rows of the summary totals table."""
            yield (
                f"| {self.results.total_tests} | {self.results.total_tests_passed} | {self.results.total_tests_failed} | {self.results.total_tests_skipped} |\n"
            )

        self.write_heading(heading_level=3)
        self.write_table(table_heading=table_heading, rows_generator=generate_rows)

    def _generate_summary_totals_devices_under_tests(self) -> None:
        """Generate the `### Summary Totals Devices Under Tests` section of the markdown report."""
        table_heading = [
            "| DUT | Total Tests | Tests Passed | Tests Failed | Tests Skipped | Categories Failed | Categories Skipped |",
            "| --- | ----------- | ------------ | ------------ | ------------- | ----------------- | ------------------ |",
        ]

        def generate_rows(self: MDReport) -> Generator[str, None, None]:
            """Generate the rows of the summary totals dut table."""
            for dut, stat in self.results.dut_stats.items():
                total_tests = stat["tests_passed"] + stat["tests_failed"] + stat["tests_skipped"] + stat["tests_not_run"]
                categories_failed = ", ".join(sorted(stat["categories_failed"]))
                categories_skipped = ", ".join(sorted(stat["categories_skipped"]))
                yield (
                    f"| {dut} | {total_tests} | {stat['tests_passed']} | {stat['tests_failed']} | {stat['tests_skipped']} | {categories_failed or '-'} |"
                    f" {categories_skipped or '-'} |\n"
                )

        self.write_heading(heading_level=3)
        self.write_table(table_heading=table_heading, rows_generator=generate_rows)

    def _generate_summary_totals_per_category(self) -> None:
        """Generate the `### Summary Totals Per Category` section of the markdown report."""
        table_heading = [
            "| Test Category | Total Tests | Tests Passed | Tests Failed | Tests Skipped |",
            "| ------------- | ----------- | ------------ | ------------ | ------------- |",
        ]

        def generate_rows(self: MDReport) -> Generator[str, None, None]:
            """Generate the rows of the summary totals per category table."""
            for category, stat in self.results.category_stats.items():
                total_tests = stat["tests_passed"] + stat["tests_failed"] + stat["tests_skipped"] + stat["tests_not_run"]
                yield f"| {category} | {total_tests} | {stat['tests_passed']} | {stat['tests_failed']} | {stat['tests_skipped']} |\n"

        self.write_heading(heading_level=3)
        self.write_table(table_heading=table_heading, rows_generator=generate_rows)

    def _generate_failed_test_results_summary(self) -> None:
        """Generate the `## Failed Test Results Summary` section of the markdown report."""
        table_heading = [
            "| Test ID | Node | Test Categories | Test Description | Test | Test Result | Failure Reasons |",
            "| ------- | ---- | --------------- | ---------------- | ---- | ----------- | --------------- |",
        ]

        def generate_rows(self: MDReport) -> Generator[str, None, None]:
            """Generate the rows of the failed test results table."""
            for result in self.results.failed_tests:
                failure_reasons = ", ".join(result["failure_reasons"])
                categories = ", ".join(result["test_categories"])
                yield (
                    f"| {result['test_id'] or '-'} | {result['node'] or '-'} | {categories or '-'} | {result['test_description'] or '-'} |"
                    f" {result['test'] or '-'} | {result['result'] or '-'} | {failure_reasons or '-'} |\n"
                )

        self.write_heading(heading_level=2)
        self.write_table(table_heading=table_heading, rows_generator=generate_rows)

    def _generate_all_test_results(self) -> None:
        """Generate the `## All Test Results` section of the markdown report.

        This section is generated only if the report includes all results.
        """
        table_heading = [
            "| Test ID | Node | Test Categories | Test Description | Test | Test Result | Failure Reasons |",
            "| ------- | ---- | --------------- | ---------------- | ---- | ----------- | --------------- |",
        ]

        def generate_rows(self: MDReport) -> Generator[str, None, None]:
            """Generate the rows of the all test results table."""
            for result in self.results.all_tests:
                failure_reasons = ", ".join(result["failure_reasons"])
                categories = ", ".join(result["test_categories"])
                yield (
                    f"| {result['test_id'] or '-'} | {result['node'] or '-'} | {categories or '-'} | {result['test_description'] or '-'} |"
                    f" {result['test'] or '-'} | {result['result'] or '-'} | {failure_reasons or '-'} |\n"
                )

        self.write_heading(heading_level=2)
        self.write_table(table_heading=table_heading, rows_generator=generate_rows)
