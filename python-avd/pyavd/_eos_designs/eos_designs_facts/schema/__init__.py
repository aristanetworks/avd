# Copyright (c) 2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from pyavd._schema.models.avd_model import AvdModel

from .protocol import EosDesignsFactsProtocol


class EosDesignsFacts(AvdModel, EosDesignsFactsProtocol):
    """EosDesignsFacts` is a schema class derived from the EosDesignsFactsProtocol."""
