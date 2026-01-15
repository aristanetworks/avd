// Copyright (c) 2025-2026 Arista Networks, Inc.
// Use of this source code is governed by the Apache License 2.0
// that can be found in the LICENSE file.

use serde::{Deserialize, Serialize};
use serde_with::skip_serializing_none;

// Valid values allowed by schema. Used for Int and Str schemas.
#[skip_serializing_none]
#[derive(Debug, Default, Clone, PartialEq, Serialize, Deserialize)]
#[serde(deny_unknown_fields)]
pub struct ValidValues<T> {
    /// List of valid values
    pub valid_values: Option<Vec<T>>,
    /// Path to variable under the parent dictionary containing valid values.
    pub dynamic_valid_values: Option<Vec<String>>,
}
