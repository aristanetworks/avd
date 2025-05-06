// Copyright (c) 2025 Arista Networks, Inc.
// Use of this source code is governed by the Apache License 2.0
// that can be found in the LICENSE file.

use avdschema::{Schema, Store};
use serde_json::Value;

use crate::{
    coercion::Coercion, context::Context, feedback::Violation, validation_result::ValidationResult,
};

use super::Validation;

pub trait StoreValidate<T> {
    /// Entrypoint for validating a JSON document against the given schema name.
    fn validate_json(
        &self,
        json: &str,
        schema_name: T,
    ) -> Result<ValidationResult, StoreValidateError>;

    /// Entrypoint for validating a YAML document against the given schema name.
    fn validate_yaml(
        &self,
        yaml: &str,
        schema_name: T,
    ) -> Result<ValidationResult, StoreValidateError>;

    /// Coerce the given value recursively to match the types of the schema.
    /// Returns a ValidationResult where only coercions have been populated.
    ///
    /// Used by external tools to coerce the data and inserting default values
    /// before trying to resolve refs based on data paths.
    fn coerce_value(&self, value: &mut Value, schema_name: T) -> ValidationResult;
}

impl StoreValidate<Schema> for Store {
    fn validate_json(
        &self,
        json: &str,
        schema_type: Schema,
    ) -> Result<ValidationResult, StoreValidateError> {
        let mut value = serde_json::from_str(json)?;
        let mut ctx = Context::new(self);

        let schema = self.get(schema_type);
        schema.coerce(&mut value, &mut ctx);
        schema.validate_value(&value, &mut ctx);

        Ok(ctx.into())
    }
    fn validate_yaml(
        &self,
        yaml: &str,
        schema_type: Schema,
    ) -> Result<ValidationResult, StoreValidateError> {
        // todo: remove `serde_yaml` once `saphyr` adds `serde` support
        // https://github.com/saphyr-rs/saphyr/issues/1
        let mut value = serde_yaml::from_str::<Value>(yaml)?;
        let mut ctx = Context::new(self);

        let schema = self.get(schema_type);
        schema.coerce(&mut value, &mut ctx);
        schema.validate_value(&value, &mut ctx);

        Ok(ctx.into())
    }
    fn coerce_value(&self, value: &mut Value, schema_name: Schema) -> ValidationResult {
        let mut ctx = Context::new(self);
        let schema = self.get(schema_name);
        schema.coerce(value, &mut ctx);
        ctx.into()
    }
}

impl StoreValidate<&str> for Store {
    fn validate_json(
        &self,
        json: &str,
        schema_name: &str,
    ) -> Result<ValidationResult, StoreValidateError> {
        if let Ok(schema_type) = Schema::try_from(schema_name) {
            self.validate_json(json, schema_type)
        } else {
            let mut ctx = Context::new(self);
            ctx.add_violation(Violation::InvalidSchema {
                schema: schema_name.into(),
            });

            Ok(ctx.into())
        }
    }
    fn validate_yaml(
        &self,
        yaml: &str,
        schema_name: &str,
    ) -> Result<ValidationResult, StoreValidateError> {
        if let Ok(schema_type) = Schema::try_from(schema_name) {
            self.validate_yaml(yaml, schema_type)
        } else {
            let mut ctx = Context::new(self);
            ctx.add_violation(Violation::InvalidSchema {
                schema: schema_name.into(),
            });

            Ok(ctx.into())
        }
    }
    fn coerce_value(&self, value: &mut Value, schema_name: &str) -> ValidationResult {
        if let Ok(schema_type) = Schema::try_from(schema_name) {
            self.coerce_value(value, schema_type)
        } else {
            let mut ctx = Context::new(self);
            ctx.add_violation(Violation::InvalidSchema {
                schema: schema_name.into(),
            });
            ctx.into()
        }
    }
}

#[derive(Debug, derive_more::Display, derive_more::From)]
pub enum StoreValidateError {
    JsonError(serde_json::Error),
    YamlError(serde_yaml::Error),
}

#[cfg(test)]
mod tests {
    use super::*;

    use crate::{
        feedback::{Feedback, Type},
        validation::test_utils::get_test_store,
    };

    #[test]
    fn validate_yaml_err() {
        let input = "key3:\n  some_key: some_value\n";
        let store = get_test_store();
        let result = store.validate_yaml(input, "eos_designs");
        assert!(result.is_ok());
        let validation_result = result.unwrap();
        assert!(validation_result.coercions.is_empty());
        assert_eq!(
            validation_result.violations,
            vec![Feedback {
                path: vec!["key3".into()],
                issue: Violation::InvalidType {
                    expected: Type::Str,
                    found: Type::Dict
                }
                .into()
            },]
        )
    }
}
