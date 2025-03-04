// Copyright (c) 2025 Arista Networks, Inc.
// Use of this source code is governed by the Apache License 2.0
// that can be found in the LICENSE file.

use serde::Serialize;
use serde_json::Value;

use crate::validation::{dict, int, list, store, str};

#[derive(Debug, PartialEq, Eq, Serialize)]
pub struct Feedback {
    pub path: Vec<String>,
    pub item: Item,
}

#[derive(Debug, PartialEq, Eq, Serialize)]
pub enum Item {
    Validation(ValidationIssue),
    Coercion(CoercionNote),
}

impl From<ValidationIssue> for Item {
    fn from(value: ValidationIssue) -> Self {
        Self::Validation(value)
    }
}

impl From<CoercionNote> for Item {
    fn from(value: CoercionNote) -> Self {
        Self::Coercion(value)
    }
}

#[derive(Debug, PartialEq, Eq, Serialize)]
pub enum ValidationIssue {
    Int(int::Violation),
    String(str::Violation),
    List(list::Violation),
    Dict(dict::Violation),
    Store(store::Violation),
    Misc(MiscViolation),
}

#[derive(Debug, PartialEq, Eq, Serialize)]
pub enum MiscViolation {
    InvalidType { expected: Type, found: Type },
    DisallowedValue,
    InvalidRegex { message: String },
}

impl From<MiscViolation> for Item {
    fn from(val: MiscViolation) -> Self {
        ValidationIssue::Misc(val).into()
    }
}

#[derive(Debug, PartialEq, Eq, Serialize)]
pub struct CoercionNote {
    pub found: Value,
    pub made: Value,
}

#[derive(Debug, PartialEq, Eq, Serialize)]
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
