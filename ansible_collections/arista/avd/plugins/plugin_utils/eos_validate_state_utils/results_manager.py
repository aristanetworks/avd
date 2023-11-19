# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from collections import defaultdict


class ResultsManager:
    """Manages and stores test results from eos_validate_state running ANTA.

    This class processes individual test result and maintains statistics like total tests passed, failed, and skipped.

    An instance of this class holding all results and statistics can be used to generate the validation reports.
    """

    def __init__(self, *, only_failed_tests: bool = True) -> None:
        """Initialize the ResultsManager with default values and stats counters set to 0.

        Args:
        ----
            only_failed_tests (bool): Flag to determine if only failed tests are saved.
                                      Defaults to True. If set to False, all tests will be saved.
        """
        self.test_id: int = 0
        self.total_tests_passed: int = 0
        self.total_tests_failed: int = 0
        self.total_tests_skipped: int = 0
        self.dut_stats: defaultdict = defaultdict(
            lambda: {
                "tests_passed": 0,
                "tests_failed": 0,
                "tests_skipped": 0,
                "categories_failed": set(),
                "categories_skipped": set(),
            },
        )
        self.category_stats: defaultdict = defaultdict(
            lambda: {
                "tests_passed": 0,
                "tests_failed": 0,
                "tests_skipped": 0,
            },
        )
        self.failed_tests: list[dict] = []
        self.all_tests: list[dict] = []
        self.only_failed_tests: bool = only_failed_tests

    def parse_result(self, result: dict) -> dict:
        """Parse a single test result and converts it into a standardized format for the reports.

        Args:
        ----
            result (dict): The test result data to parse.

        Returns:
        -------
            dict: The parsed and standardized test result.
        """
        # All AVD tests have a single category and overwrite the native ANTA tests categories
        new_test_category = result.get("categories", [""])[0]

        # Mapping the ANTA results
        result_mapping = {"success": "PASS", "failure": "FAIL", "error": "FAIL", "skipped": "SKIPPED", "unset": "SKIPPED"}
        anta_result = result.get("result", "")
        new_result = result_mapping.get(anta_result, "")

        # Create the parsed result dictionary
        return {
            "test_id": self.test_id,
            "node": result.get("name", ""),
            "test_category": new_test_category,
            "test_description": result.get("description", ""),
            # Since AVD tests can have the same description and category, ANTA's custom_field is used to differentiate tests
            "test": result.get("custom_field", "") if result.get("custom_field") != "None" else result.get("test", ""),
            "result": new_result,
            "failure_reasons": result.get("messages", []),
        }

    def update_results(self, result: dict) -> None:
        """Update the internal statistics and test results based on the given test result.

        Args:
        ----
            result (dict): The test result data to be added and processed.
        """
        self.test_id += 1
        parsed_result = self.parse_result(result)
        test_result = parsed_result["result"]
        category = parsed_result["test_category"]
        dut = parsed_result["node"]

        # Process the test result
        # TODO: Simplify this
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

        if not self.only_failed_tests:
            self.all_tests.append(parsed_result)

    @property
    def total_tests(self) -> int:
        """Calculates the total number of tests processed.

        Returns
        -------
            int: The total number of tests.
        """
        return self.total_tests_passed + self.total_tests_failed + self.total_tests_skipped
