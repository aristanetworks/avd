# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import logging
from typing import TYPE_CHECKING

import pytest

if TYPE_CHECKING:
    from collections.abc import Generator


@pytest.fixture(autouse=True)
def reset_avd_logger() -> Generator[None, None, None]:
    logger = logging.getLogger("ansible_collections.arista.avd")
    original_propagate = logger.propagate
    original_handlers = logger.handlers[:]
    yield
    logger.propagate = original_propagate
    logger.handlers = original_handlers
