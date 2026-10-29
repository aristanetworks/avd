# Copyright (c) 2024-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from re import compile as re_compile
from re import fullmatch

from .constants import CVAAS_VERSION_STRING

# The double braces are escaping braces for the f-string. The regex pattern will get a single brace.
VERSION_PATTERN = re_compile(rf"(\d{{4}}\.\d{{1,2}}\.\d{{1,2}}(?:\.\d{{1,2}})?|{CVAAS_VERSION_STRING})")


class CvVersion:
    version: str
    version_value: int

    def __init__(self, version: str) -> None:
        if not fullmatch(VERSION_PATTERN, version):
            msg = f"Invalid CV Version '{version}'. The version must conform to the pattern '{VERSION_PATTERN.pattern}'"
            raise ValueError(msg)

        self.version = version
        self.version_value = self._version_as_value()

    def __str__(self) -> str:
        return self.version

    def __repr__(self) -> str:
        return f"<CvVersion {self.version}>"

    def __hash__(self) -> int:
        return self.version_value

    def _version_as_value(self) -> int:
        """
        Return the CloudVision version as an integer.

        Used for API selection.
        CloudVision releases may use a fourth component, which is ignored for API compatibility comparisons.
        """
        if self.version == CVAAS_VERSION_STRING:
            return 99999999

        elements = self.version.split(".", maxsplit=3)
        return int(f"{elements[0]:0>4}{elements[1]:0>2}{elements[2]:0>2}")

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, CvVersion):
            return False
        return self.version_value == other.version_value

    def __neq__(self, other: object) -> bool:
        if not isinstance(other, CvVersion):
            return False
        return self.version_value != other.version_value

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, CvVersion):
            return False
        return self.version_value < other.version_value

    def __le__(self, other: object) -> bool:
        if not isinstance(other, CvVersion):
            return False
        return self.version_value <= other.version_value

    def __gt__(self, other: object) -> bool:
        if not isinstance(other, CvVersion):
            return False
        return self.version_value > other.version_value

    def __ge__(self, other: object) -> bool:
        if not isinstance(other, CvVersion):
            return False
        return self.version_value >= other.version_value
