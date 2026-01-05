# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING

from anta.tests.mlag import VerifyMlagConfigSanity, VerifyMlagInterfaces, VerifyMlagStatus

from pyavd._anta.constants import StructuredConfigKey

from ._base_classes import AntaTestInputFactory
from ._decorators import skip_if_missing_config

if TYPE_CHECKING:
    from collections.abc import Iterator


class VerifyMlagConfigSanityInputFactory(AntaTestInputFactory[VerifyMlagConfigSanity.Input]):
    """
    Input factory class for the `VerifyMlagConfigSanity` test.

    Generate the test inputs only if `mlag_configuration` is configured.
    """

    @skip_if_missing_config(StructuredConfigKey.MLAG_CONFIGURATION)
    def create(self) -> Iterator[VerifyMlagConfigSanity.Input]:
        yield VerifyMlagConfigSanity.Input()


class VerifyMlagInterfacesInputFactory(AntaTestInputFactory[VerifyMlagInterfaces.Input]):
    """
    Input factory class for the `VerifyMlagInterfaces` test.

    Generate the test inputs only if `mlag_configuration` is configured.
    """

    @skip_if_missing_config(StructuredConfigKey.MLAG_CONFIGURATION)
    def create(self) -> Iterator[VerifyMlagInterfaces.Input]:
        yield VerifyMlagInterfaces.Input()


class VerifyMlagStatusInputFactory(AntaTestInputFactory[VerifyMlagStatus.Input]):
    """
    Input factory class for the `VerifyMlagStatus` test.

    Generate the test inputs only if `mlag_configuration` is configured.
    """

    @skip_if_missing_config(StructuredConfigKey.MLAG_CONFIGURATION)
    def create(self) -> Iterator[VerifyMlagStatus.Input]:
        yield VerifyMlagStatus.Input()
