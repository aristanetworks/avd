# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING

from anta.tests.vxlan import VerifyVxlanConfigSanity

from pyavd._anta.constants import StructuredConfigKey

from ._base_classes import AntaTestInputFactory
from ._decorators import skip_if_missing_config

if TYPE_CHECKING:
    from collections.abc import Iterator


class VerifyVxlanConfigSanityInputFactory(AntaTestInputFactory[VerifyVxlanConfigSanity.Input]):
    """
    Input factory class for the `VerifyVxlanConfigSanity` test.

    Generate the test inputs only if `vxlan_interface.vxlan1.vxlan` is configured.
    """

    @skip_if_missing_config(StructuredConfigKey.VXLAN1_INTERFACE)
    def create(self) -> Iterator[VerifyVxlanConfigSanity.Input]:
        yield VerifyVxlanConfigSanity.Input()
