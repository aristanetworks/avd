// Copyright (c) 2025 Arista Networks, Inc.
// Use of this source code is governed by the Apache License 2.0
// that can be found in the LICENSE file.

use serde_json::Value;

use crate::context::Context;
use avdschema::any::AnySchema;

use super::Validation;

impl Validation<Value> for AnySchema {
    fn validate(&self, value: &Value, ctx: &mut Context) {
        self.validate_value(value, ctx)
    }

    fn validate_value(&self, value: &Value, ctx: &mut Context) {
        match self {
            Self::Bool(schema) => schema.validate_value(value, ctx),
            Self::Int(schema) => schema.validate_value(value, ctx),
            Self::Str(schema) => schema.validate_value(value, ctx),
            Self::List(schema) => schema.validate_value(value, ctx),
            Self::Dict(schema) => schema.validate_value(value, ctx),
        }
    }

    fn is_required(&self) -> bool {
        match self {
            Self::Bool(schema) => schema.is_required(),
            Self::Int(schema) => schema.is_required(),
            Self::Str(schema) => schema.is_required(),
            Self::List(schema) => schema.is_required(),
            Self::Dict(schema) => schema.is_required(),
        }
    }
}
