// Copyright (c) 2025 Arista Networks, Inc.
// Use of this source code is governed by the Apache License 2.0
// that can be found in the LICENSE file.

use avdschema::{any::AnySchema, boolean::Bool, resolve_ref};
use serde_json::Value;

use crate::{
    context::Context,
    feedback::{Type, Violation},
};

use super::Validation;

impl Validation<bool> for Bool {
    fn validate(&self, value: &bool, ctx: &mut Context) {
        self.validate_ref(value, ctx);
    }

    fn validate_value(&self, value: &Value, ctx: &mut Context) {
        if let Some(v) = value.as_bool() {
            self.validate(&v, ctx)
        } else if value.is_null() && !ctx.configuration.restrict_null_values {
        } else {
            ctx.add_error(Violation::InvalidType {
                expected: Type::Bool,
                found: value.into(),
            })
        }
    }

    fn validate_ref(&self, value: &bool, ctx: &mut Context) {
        if let Some(ref_) = self.base.schema_ref.as_ref() {
            // Ignoring not being able to resolve the schema.
            // Ignoring a wrong schema type at the ref. Since Validation is infallible.
            // TODO: What to do?
            if let Ok(AnySchema::Bool(ref_schema)) = resolve_ref(ref_, ctx.store) {
                ref_schema.validate(value, ctx);
            }
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    use crate::{
        feedback::{Feedback, Type, Violation},
        validation::test_utils::get_test_store,
    };

    #[test]
    fn validate_type_ok() {
        let schema = Bool::default();
        let input = true.into();
        let store = get_test_store();
        let mut ctx = Context::new(&store, None);
        schema.validate_value(&input, &mut ctx);
        assert!(ctx.result.errors.is_empty() && ctx.result.infos.is_empty());
    }

    #[test]
    fn validate_type_err() {
        let schema = Bool::default();
        let input = serde_json::json!([]);
        let store = get_test_store();
        let mut ctx = Context::new(&store, None);
        schema.validate_value(&input, &mut ctx);
        assert!(ctx.result.infos.is_empty());
        assert_eq!(
            ctx.result.errors,
            vec![Feedback {
                path: vec![].into(),
                issue: Violation::InvalidType {
                    expected: Type::Bool,
                    found: Type::List,
                }
                .into(),
            }],
        );
    }
}
