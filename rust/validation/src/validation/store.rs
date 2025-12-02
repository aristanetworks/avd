// Copyright (c) 2025 Arista Networks, Inc.
// Use of this source code is governed by the Apache License 2.0
// that can be found in the LICENSE file.

use avdschema::{Schema, Store};
use serde_json::Value;

use crate::{
    coercion::Coercion,
    context::{Configuration, Context},
    feedback::Violation,
    validation_result::ValidationResult,
};

use super::Validation;

pub trait StoreValidate<T> {
    /// Entrypoint for validating a JSON document against the given schema name.
    fn validate_json(
        &self,
        json: &str,
        schema_name: T,
        configuration: Option<&Configuration>,
    ) -> Result<ValidationResult, StoreValidateError>;

    /// Entrypoint for validating a YAML document against the given schema name.
    fn validate_yaml(
        &self,
        yaml: &str,
        schema_name: T,
        configuration: Option<&Configuration>,
    ) -> Result<ValidationResult, StoreValidateError>;

    /// Entrypoint for validating a serde_json::Value against the given schema name.
    fn validate_value(
        &self,
        value: &mut Value,
        schema_name: T,
        configuration: Option<&Configuration>,
    ) -> ValidationResult;

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
        schema_name: Schema,
        configuration: Option<&Configuration>,
    ) -> Result<ValidationResult, StoreValidateError> {
        let mut value = serde_json::from_str(json)?;
        Ok(self.validate_value(&mut value, schema_name, configuration))
    }
    fn validate_yaml(
        &self,
        yaml: &str,
        schema_name: Schema,
        configuration: Option<&Configuration>,
    ) -> Result<ValidationResult, StoreValidateError> {
        // todo: remove `serde_yaml` once `saphyr` adds `serde` support
        // https://github.com/saphyr-rs/saphyr/issues/1
        let mut value = serde_yaml::from_str::<Value>(yaml)?;
        Ok(self.validate_value(&mut value, schema_name, configuration))
    }
    fn validate_value(
        &self,
        value: &mut Value,
        schema_name: Schema,
        configuration: Option<&Configuration>,
    ) -> ValidationResult {
        let mut ctx = Context::new(self, configuration);
        let schema = self.get(schema_name);
        schema.coerce(value, &mut ctx);
        schema.validate_value(value, &mut ctx);
        ctx.into()
    }
    fn coerce_value(&self, value: &mut Value, schema_name: Schema) -> ValidationResult {
        let mut ctx = Context::new(self, None);
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
        configuration: Option<&Configuration>,
    ) -> Result<ValidationResult, StoreValidateError> {
        with_resolved_schema(schema_name, self, |schema_type| {
            self.validate_json(json, schema_type, configuration)
        })
    }

    fn validate_yaml(
        &self,
        yaml: &str,
        schema_name: &str,
        configuration: Option<&Configuration>,
    ) -> Result<ValidationResult, StoreValidateError> {
        with_resolved_schema(schema_name, self, |schema_type| {
            self.validate_yaml(yaml, schema_type, configuration)
        })
    }

    fn validate_value(
        &self,
        value: &mut Value,
        schema_name: &str,
        configuration: Option<&Configuration>,
    ) -> ValidationResult {
        with_resolved_schema(schema_name, self, |schema_type| {
            self.validate_value(value, schema_type, configuration)
        })
    }

    fn coerce_value(&self, value: &mut Value, schema_name: &str) -> ValidationResult {
        with_resolved_schema(schema_name, self, |schema_type| {
            self.coerce_value(value, schema_type)
        })
    }
}

#[derive(Debug, derive_more::Display, derive_more::From)]
pub enum StoreValidateError {
    JsonError(serde_json::Error),
    YamlError(serde_yaml::Error),
}

#[derive(Debug, derive_more::Display, derive_more::From)]
pub enum SchemaConversionError {
    InvalidSchemaName(String),
}

impl SchemaConversionError {
    pub fn get_invalid_schema_name(&self) -> String {
        match self {
            SchemaConversionError::InvalidSchemaName(s) => s.clone(),
        }
    }

    pub fn to_validation_result(&self, store: &Store) -> ValidationResult {
        let mut ctx = Context::new(store, None);
        ctx.add_violation(Violation::InvalidSchema {
            schema: self.get_invalid_schema_name(),
        });
        ctx.into()
    }
}

impl From<ValidationResult> for Result<ValidationResult, StoreValidateError> {
    fn from(result: ValidationResult) -> Self {
        Ok(result)
    }
}

fn with_resolved_schema<T: std::convert::From<ValidationResult>, F: FnOnce(Schema) -> T>(
    schema_name: &str,
    store: &Store,
    func: F,
) -> T {
    match Schema::try_from(schema_name) {
        Ok(schema_type) => func(schema_type),
        Err(_) => SchemaConversionError::InvalidSchemaName(schema_name.to_string())
            .to_validation_result(store)
            .into(),
    }
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
        let result = store.validate_yaml(input, "eos_designs", None);
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
    #[test]
    fn validate_yaml_invalid_schema() {
        let input = "";
        let store = get_test_store();
        let result = store.validate_yaml(input, "invalid_schema", None);
        assert!(result.is_ok());
        let validation_result = result.unwrap();
        assert!(validation_result.coercions.is_empty());
        assert_eq!(
            validation_result.violations,
            vec![Feedback {
                path: vec![],
                issue: Violation::InvalidSchema {
                    schema: "invalid_schema".to_string()
                }
                .into()
            },]
        )
    }
    #[test]
    fn validate_value_invalid_schema() {
        let mut input = serde_json::json!({});
        let store = get_test_store();
        let validation_result = store.validate_value(&mut input, "invalid_schema", None);
        assert!(validation_result.coercions.is_empty());
        assert_eq!(
            validation_result.violations,
            vec![Feedback {
                path: vec![],
                issue: Violation::InvalidSchema {
                    schema: "invalid_schema".to_string()
                }
                .into()
            },]
        )
    }
}
