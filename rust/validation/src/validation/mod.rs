// Copyright (c) 2025 Arista Networks, Inc.
// Use of this source code is governed by the Apache License 2.0
// that can be found in the LICENSE file.

pub(crate) mod any;
pub(crate) mod boolean;
pub(crate) mod dict;
pub(crate) mod int;
pub(crate) mod list;
pub(crate) mod store;
pub(crate) mod str;
pub(crate) mod valid_values;

use serde_json::Value;

use crate::context::Context;

pub(crate) trait Validation<T> {
    fn validate(&self, value: &T, ctx: &mut Context);
    fn validate_value(&self, value: &Value, ctx: &mut Context);
    fn is_required(&self) -> bool;

    /// This validation of ref will not merge in the schema, so it only works as expected when there are no local variables set as well.
    /// In practice this is only used for structured_config, where we $ref in the full eos_cli_config_gen schema. All other schemas
    /// will be resolved up-front and stored in the schema store.
    fn validate_ref(&self, value: &T, ctx: &mut Context);
}

#[cfg(test)]
pub(crate) mod test_utils;
