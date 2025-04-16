// Copyright (c) 2025 Arista Networks, Inc.
// Use of this source code is governed by the Apache License 2.0
// that can be found in the LICENSE file.
use serde::Serialize;
use serde_json::Value;

/// Feedback item carried in the Context under either `coercions` or `violations`
#[derive(Debug, PartialEq, Serialize)]
pub struct Feedback {
    /// Data path which the feedback concerns.
    pub path: Vec<String>,
    pub issue: Issue,
}

/// Issue is wrapped in Feedback and added to the Context during coercion and validation.
#[derive(Debug, PartialEq, Serialize, derive_more::From)]
pub enum Issue {
    /// Violation found during validation.
    Validation(Violation),
    /// Coercion performed during coercion.
    Coercion(CoercionNote),
    /// Default value as specified in the schema was inserted into the data.
    DefaultValueInserted,
    /// Some internal error occurred.
    InternalError { message: String },
}

/// One coercion performed during recursive coercion.
#[derive(Debug, PartialEq, Eq, Serialize)]
pub struct CoercionNote {
    pub found: Value,
    pub made: Value,
}

/// One violation found during recursive validation.
#[derive(Debug, PartialEq, Serialize)]
pub enum Violation {
    /// The length is above the maximum allowed.
    LengthAboveMaximum { maximum: u64, found: u64 },
    /// The length is below the minimum allowed.
    LengthBelowMinimum { minimum: u64, found: u64 },
    /// The dictionary key is required, but was not set.
    MissingRequiredKey { key: String },
    /// The given schema name was not found in the schema store.
    InvalidSchema { schema: String },
    /// The value is not of the expected type.
    InvalidType { expected: Type, found: Type },
    /// The value is not among the valid values.
    InvalidValue {
        expected: ViolationValidValues,
        found: Value,
    },
    /// The value is not matching the allowed pattern.
    NotMatchingPattern { pattern: String, found: String },
    /// The dictionary key is not allowed by the schema.
    UnexpectedKey,
    /// The value is above the maximum allowed.
    ValueAboveMaximum { maximum: i64, found: i64 },
    /// The value is below the minimum allowed.
    ValueBelowMinimum { minimum: i64, found: i64 },
    /// The value is not unique as required.
    ValueNotUnique { other_path: Vec<String> },
}

/// Data Type used in Violation.
#[derive(Debug, PartialEq, Serialize)]
pub enum Type {
    Null,
    Bool,
    Int,
    Str,
    List,
    Dict,
}
impl From<&Value> for Type {
    fn from(value: &Value) -> Self {
        match value {
            Value::Null => Self::Null,
            Value::Bool(_) => Self::Bool,
            Value::Number(_) => Self::Int,
            Value::String(_) => Self::Str,
            Value::Array(_) => Self::List,
            Value::Object(_) => Self::Dict,
        }
    }
}

/// List of valid values used in Violation
#[derive(Debug, PartialEq, Serialize, derive_more::From)]
pub enum ViolationValidValues {
    Bool(Vec<bool>),
    Int(Vec<i64>),
    Str(Vec<String>),
}
