// Copyright (c) 2025 Arista Networks, Inc.
// Use of this source code is governed by the Apache License 2.0
// that can be found in the LICENSE file.

use avdschema::{Schema, Store};
use serde::Serialize;
use serde_json::Value;

use crate::{
    Item, coercion::Coercion, context::Context, feedback::ValidationIssue,
    validation_result::ValidationResult,
};

use super::Validation;

#[derive(Debug, PartialEq, Eq, Serialize)]
pub enum Violation {
    InvalidSchema { schema: String }, // InvalidPath { component: String },
                                      // MissingKey { key: String },
}

impl From<Violation> for Item {
    fn from(val: Violation) -> Self {
        ValidationIssue::Store(val).into()
    }
}

pub trait ValidateJson<T> {
    fn validate_json(
        &self,
        json: &str,
        schema_name: T,
    ) -> Result<ValidationResult, Box<dyn std::error::Error>>;
}

impl ValidateJson<Schema> for Store {
    fn validate_json(
        &self,
        json: &str,
        schema_type: Schema,
    ) -> Result<ValidationResult, Box<dyn std::error::Error>> {
        // todo: remove `serde_yaml` once `saphyr` adds `serde` support
        // https://github.com/saphyr-rs/saphyr/issues/1
        let mut value = serde_yaml::from_str::<Value>(json)?;
        let mut ctx = Context::new();

        let schema = self.get(schema_type);
        schema.coerce(&mut value, &mut ctx);
        schema.validate_value(&value, &mut ctx);

        Ok(ctx.into())
    }
}

impl ValidateJson<&str> for Store {
    fn validate_json(
        &self,
        json: &str,
        schema_name: &str,
    ) -> Result<ValidationResult, Box<dyn std::error::Error>> {
        if let Ok(schema_type) = Schema::try_from(schema_name) {
            self.validate_json(json, schema_type)
        } else {
            let mut ctx = Context::new();
            ctx.add_violation(Violation::InvalidSchema {
                schema: schema_name.into(),
            });

            Ok(ctx.into())
        }
    }
}
