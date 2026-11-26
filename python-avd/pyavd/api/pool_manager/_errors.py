# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.


class InvalidPoolValueError(ValueError):
    """An explicit assignment requests a value outside the pool's supported range or type."""

    def __init__(self, key: str, value: int | str, pool_key: str) -> None:
        self.key = key
        self.value = value
        super().__init__(f"Invalid value '{value}' requested for '{key}' in pool '{pool_key}'.")


class PoolAssignmentConflictError(ValueError):
    """An explicit assignment requests a value already assigned to another key."""

    def __init__(self, key: str, value: int | str, pool_key: str, assigned_key: str) -> None:
        self.key = key
        self.value = value
        self.assigned_key = assigned_key
        super().__init__(f"Value '{value}' requested for '{key}' in pool '{pool_key}' is already assigned to '{assigned_key}'.")
