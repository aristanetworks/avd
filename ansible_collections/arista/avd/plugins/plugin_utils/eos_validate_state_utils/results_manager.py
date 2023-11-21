# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from collections import defaultdict

from ansible_collections.arista.avd.roles.eos_validate_state.python_modules.constants import ACRONYM_CATEGORIES


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
        self.test_id = 0
        self.total_tests_passed = 0
        self.total_tests_failed = 0
        self.total_tests_skipped = 0
        self.total_tests_not_run = 0
        self.dut_stats = defaultdict(
            lambda: {
                "tests_passed": 0,
                "tests_failed": 0,
                "tests_skipped": 0,
                "categories_failed": set(),
                "categories_skipped": set(),
            },
        )
        self.category_stats = defaultdict(
            lambda: {
                "tests_passed": 0,
                "tests_failed": 0,
                "tests_skipped": 0,
            },
        )
        self.failed_tests = []
        self.all_tests = []
        self.only_failed_tests = only_failed_tests

    def _parse_result(self, result: dict) -> dict:
        """Parse a single test result and converts it into a standardized format for the reports.

        Args:
        ----
            result (dict): The test result data to parse.

        Returns:
        -------
            dict: The parsed and standardized test result.
        """
        test_categories = [
            " ".join(word.upper() if word.lower() in ACRONYM_CATEGORIES else word.title() for word in category.split())
            for category in result.get("categories", [])
        ]

        # Mapping the ANTA results
        result_mapping = {"success": "PASS", "failure": "FAIL", "error": "FAIL", "skipped": "SKIPPED", "unset": "NOT RUN"}
        anta_result = result.get("result", "")
        new_result = result_mapping.get(anta_result, "")

        # Create the parsed result dictionary
        return {
            "test_id": self.test_id,
            "node": result.get("name", ""),
            "test_categories": test_categories,
            "test_description": result.get("description", ""),
            # Since AVD tests can have the same description and category, ANTA's custom_field is used to differentiate tests
            "test": result.get("custom_field", "") if result.get("custom_field") != "None" else result.get("test", ""),
            "result": new_result,
            "failure_reasons": result.get("messages", []),
        }

    def _increment_stats(self, test_result: str, dut: str, categories: list[str]) -> None:
        """Increment test statistics based on the test result.

        Args:
        ----
            test_result (str): The test result.
            dut (str): The name of the device under test.
            categories (list[str]): The categories of the test.
        """
        stats_mapping = {
            "PASS": ("total_tests_passed", "tests_passed"),
            "FAIL": ("total_tests_failed", "tests_failed", "categories_failed"),
            "SKIPPED": ("total_tests_skipped", "tests_skipped", "categories_skipped"),
        }
        stats_to_increment = stats_mapping.get(test_result, ())

        for stat in stats_to_increment:
            if stat.startswith("total_"):
                setattr(self, stat, getattr(self, stat) + 1)
                continue
            if stat.startswith("tests_"):
                self.dut_stats[dut][stat] += 1
            for category in categories:
                if stat.startswith("tests_"):
                    self.category_stats[category][stat] += 1
                else:
                    self.dut_stats[dut][stat].add(category)

    def update_results(self, result: dict) -> None:
        """Update the internal statistics and test results based on the given test result.

        Args:
        ----
            result (dict): The test result data to be added and processed.
        """
        self.test_id += 1
        parsed_result = self._parse_result(result)
        test_result = parsed_result["result"]
        categories = parsed_result["test_categories"]
        dut = parsed_result["node"]

        self._increment_stats(test_result, dut, categories)

        if test_result == "FAIL":
            self.failed_tests.append(parsed_result)
        elif test_result == "NOT RUN":
            self.total_tests_not_run += 1
        if not self.only_failed_tests:
            self.all_tests.append(parsed_result)

    @property
    def total_tests(self) -> int:
        """Calculates the total number of tests processed.

        Returns
        -------
            int: The total number of tests.
        """
        return self.total_tests_passed + self.total_tests_failed + self.total_tests_skipped + self.total_tests_not_run
