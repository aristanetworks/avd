# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from json import dumps
from tempfile import TemporaryFile
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from io import TextIOWrapper


class ResultsManager:
    """
    Manages and stores test results from eos_validate_state running ANTA.

    This class processes individual test results, categorizes them based on their outcomes,
    and maintains statistics on various aspects like total tests passed, failed, and skipped.

    It also handles temporary storage of all test results if needed.

    An instance of this class holding all results can then be passed to the report classes to
    generate the validation reports.
    """

    def __init__(self, only_failed_tests: bool = True):
        """
        Initializes the ResultsManager with default values and optional temporary file
        creation to hold all test results.

        Args:
            only_failed_tests (bool): Flag to determine if only failed tests are considered.
                                      Defaults to True. If set to False, a temporary file will
                                      be created to hold all test results.
        """
        self.test_id: int = 0
        self.total_tests_passed: int = 0
        self.total_tests_failed: int = 0
        self.total_tests_skipped: int = 0
        self.dut_stats: dict[str, dict] = {}
        self.category_stats: dict[str, dict] = {}
        self.failed_tests: list[dict] = []
        self.only_failed_tests: bool = only_failed_tests

        # Initialize a temp file to hold all test results
        self.tmp_test_results_file: TextIOWrapper | None = TemporaryFile(mode="w+", encoding="UTF-8") if not only_failed_tests else None

    def parse_result(self, result: dict) -> dict:
        """
        Parses a single test result and converts it into a standardized format for the reports.

        Args:
            result (dict): The test result data to parse.

        Returns:
            dict: The parsed and standardized test result.
        """

        # All AVD tests have a single category and overwrite the native ANTA tests categories
        categories = result.get("categories", [])
        new_test_category = categories[0] if categories else ""

        # Convert the ANTA test result
        if (anta_result := result.get("result", "")) == "success":
            new_result = "PASS"
        elif anta_result == "failure" or anta_result == "error":
            new_result = "FAIL"
        elif anta_result == "skipped" or anta_result == "unset":
            new_result = "SKIPPED"
        else:
            new_result = ""

        # Since AVD tests can have the same description and category, ANTA's custom_field is used to differentiate tests
        custom_field = result.get("custom_field", "")
        new_test = result.get("test", "") if custom_field == "None" else custom_field

        # Create the parsed result dictionary
        parsed_result = {
            "test_id": self.test_id,
            "node": result.get("name", ""),
            "test_category": new_test_category,
            "test_description": result.get("description", ""),
            "test": new_test,
            "result": new_result,
            "failure_reasons": result.get("messages", []),
        }

        return parsed_result

    def update_results(self, result: dict) -> None:
        """
        Updates the internal statistics and test results based on the given test result.

        Args:
            result (dict): The test result data to be added and processed.
        """

        # Update the test_id counter when we add a result
        self.test_id += 1

        # Parse and convert the result data
        parsed_result = self.parse_result(result)

        # Update the statistics
        category = parsed_result["test_category"]
        dut = parsed_result["node"]
        if category not in self.category_stats:
            self.category_stats[category] = {"tests_passed": 0, "tests_failed": 0, "tests_skipped": 0}
        if dut not in self.dut_stats:
            self.dut_stats[dut] = {"tests_passed": 0, "tests_failed": 0, "tests_skipped": 0, "categories_failed": set(), "categories_skipped": set()}

        test_result = parsed_result["result"]
        if test_result == "PASS":
            self.total_tests_passed += 1
            self.dut_stats[dut]["tests_passed"] += 1
            self.category_stats[category]["tests_passed"] += 1
        elif test_result == "FAIL":
            self.total_tests_failed += 1
            self.dut_stats[dut]["tests_failed"] += 1
            self.category_stats[category]["tests_failed"] += 1
            self.dut_stats[dut]["categories_failed"].add(category)
            self.failed_tests.append(parsed_result)
        elif test_result == "SKIPPED":
            self.total_tests_skipped += 1
            self.dut_stats[dut]["tests_skipped"] += 1
            self.category_stats[category]["tests_skipped"] += 1
            self.dut_stats[dut]["categories_skipped"].add(category)

        # Update the temp results if we want all tests and not only the failed tests
        if self.tmp_test_results_file and not self.only_failed_tests:
            self.tmp_test_results_file.write(dumps(parsed_result) + "\n")

    @property
    def total_tests(self) -> int:
        """
        Calculates the total number of tests processed.

        Returns:
            int: The total number of tests.
        """
        return self.total_tests_passed + self.total_tests_failed + self.total_tests_skipped
