// Copyright (c) 2025-2026 Arista Networks, Inc.
// Use of this source code is governed by the Apache License 2.0
// that can be found in the LICENSE file.

use serde::{Deserialize, Serialize};
use serde_with::skip_serializing_none;

/// Settings used for generating documentation for all other types than dict.
#[skip_serializing_none]
#[derive(Debug, Default, Clone, PartialEq, Serialize, Deserialize)]
#[serde(deny_unknown_fields)]
pub struct DocumentationOptions {
    /// Setting `table` will allow for custom grouping of schema fields in the documentation.
    /// By default each root key has its own table. By setting the same table-value on multiple keys, they will be merged to a single table.
    /// If `table` is set on a 'child' key, all 'ancestor' keys are automatically included in the table so the full path is visible.
    /// The `table` option is inherited to all child keys, unless specifically set on the child.
    pub table: Option<String>,
}

/// Settings options used for generating documentation for a dict.
#[skip_serializing_none]
#[derive(Debug, Default, Clone, PartialEq, Serialize, Deserialize)]
#[serde(deny_unknown_fields)]
pub struct DocumentationOptionsDict {
    /// Setting `table` will allow for custom grouping of schema fields in the documentation.
    /// By default each root key has its own table. By setting the same table-value on multiple keys, they will be merged to a single table.
    /// If `table` is set on a 'child' key, all 'ancestor' keys are automatically included in the table so the full path is visible.
    /// The `table` option is inherited to all child keys, unless specifically set on the child.
    pub table: Option<String>,
    /// Prevent keys of the dict from being displayed in the generated documentation.
    /// This is used for structured_config where we wish to avoid displaying the full eos_cli_config_gen schema everywhere.
    pub hide_keys: Option<bool>,
}
