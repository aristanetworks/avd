# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import csv
from json import loads
from typing import TYPE_CHECKING, Generator

if TYPE_CHECKING:
    from io import TextIOWrapper

    from .results_manager import ResultsManager


class CSVReport:
    """
    Generates and writes the validation CSV report based on test results managed by ResultsManager.
    """

    def __init__(self, csvfile: TextIOWrapper, results: ResultsManager):
        """
        Initializes the CSVReport with an open CSV file object to write to and a ResultsManager instance.

        Args:
            csvfile (TextIOWrapper): An open file object to write the CSV data into.
            results (ResultsManager): The ResultsManager instance containing all test results.
        """
        self.csvfile: TextIOWrapper = csvfile
        self.results: ResultsManager = results

    def generate_rows(self) -> Generator[dict, None, None]:
        """
        Generates rows of test result data for the CSV report.

        Results are sourced from `failed_tests` or from a temporary file managed by ResultsManager,
        based on whether the report includes only failed tests or all results.

        Yields:
            Generator[dict, None, None]: A generator of test result dictionaries representing CSV rows.
        """
        if self.results.only_failed_tests:
            for result in self.results.failed_tests:
                yield {**result, "failure_reasons": ";".join(result["failure_reasons"])}
        else:
            self.results.tmp_test_results_file.seek(0)
            for result in self.results.tmp_test_results_file:
                result_dict = loads(result.strip())
                yield {**result_dict, "failure_reasons": ";".join(result_dict["failure_reasons"])}

    def generate_report(self) -> None:
        """
        Generates and writes the CSV report using the collected test results.
        """
        fieldnames = ["test_id", "node", "test_category", "test_description", "test", "result", "failure_reasons"]
        writer = csv.DictWriter(self.csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for row in self.generate_rows():
            writer.writerow(row)
