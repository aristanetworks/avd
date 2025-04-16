// Copyright (c) 2025 Arista Networks, Inc.
// Use of this source code is governed by the Apache License 2.0
// that can be found in the LICENSE file.

use serde::{Deserialize, Serialize};
use serde_with::skip_serializing_none;

use crate::schema::base::Base;

use super::{
    any::AnySchema,
    base::{
        convert_types::ConvertTypes, documentation_options::DocumentationOptions,
        valid_values::ValidValues,
    },
};

/// AVD Schema for integer data.
#[skip_serializing_none]
#[derive(Debug, Clone, Default, PartialEq, Serialize, Deserialize)]
#[serde(deny_unknown_fields)]
pub struct Int {
    pub min: Option<i64>,
    pub max: Option<i64>,
    #[serde(flatten)]
    pub base: Base<i64>,
    #[serde(flatten)]
    pub convert_types: ConvertTypes,
    #[serde(flatten)]
    pub valid_values: ValidValues<i64>,
    pub documentation_options: Option<DocumentationOptions>,
}

impl<'x> TryFrom<&'x AnySchema> for &'x Int {
    type Error = &'static str;

    fn try_from(value: &'x AnySchema) -> Result<Self, Self::Error> {
        match value {
            AnySchema::Int(int) => Ok(int),
            _ => Err("Unable to convert from AnySchema to Int. Invalid Schema type."),
        }
    }
}

#[cfg(test)]
mod tests {
    use crate::{any::AnySchema, str::Str};

    use super::Int;

    #[test]
    fn try_from_anyschema_ok() {
        let anyschema = &AnySchema::Int(Int::default());
        let result: Result<&Int, _> = anyschema.try_into();
        assert!(result.is_ok());
    }
    #[test]
    fn try_from_anyschema_err() {
        let anyschema = &AnySchema::Str(Str::default());
        let result: Result<&Int, _> = anyschema.try_into();
        assert!(result.is_err());
    }
}
