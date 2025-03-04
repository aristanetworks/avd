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
}
