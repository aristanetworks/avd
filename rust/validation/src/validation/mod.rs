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

pub trait Validation<T> {
    /// Validate the given value T according to the schema where the trait is implemented.
    /// Validation updates the given Context with any found violations.
    fn validate(&self, value: &T, ctx: &mut Context);

    /// Validate the given JSON Value according to the schema where the trait is implemented.
    /// Validation updates the given Context with any found violations including if the type of Value is wrong.
    fn validate_value(&self, value: &Value, ctx: &mut Context);

    /// Validation of ref which will not merge in the schema, so it only works as expected when there are no local variables set.
    /// In practice this is only used for structured_config, where we $ref in the full eos_cli_config_gen schema. All other schemas
    /// will be resolved up-front and stored in the schema store.
    fn validate_ref(&self, value: &T, ctx: &mut Context);
}

#[cfg(test)]
pub(crate) mod test_utils;
