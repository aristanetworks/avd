// Copyright (c) 2025 Arista Networks, Inc.
// Use of this source code is governed by the Apache License 2.0
// that can be found in the LICENSE file.

use serde_json::Value;

use crate::context::Context;
use avdschema::any::AnySchema;
use avdschema::delegate_anyshcema_method;

use super::Validation;

impl Validation<Value> for AnySchema {
    fn validate(&self, value: &Value, ctx: &mut Context) {
        self.validate_value(value, ctx)
    }

    fn validate_value(&self, value: &Value, ctx: &mut Context) {
        delegate_anyshcema_method!(self, validate_value, value, ctx)
    }

    fn validate_ref(&self, _value: &Value, _ctx: &mut Context) {}
}
