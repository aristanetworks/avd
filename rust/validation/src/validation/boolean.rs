// Copyright (c) 2025 Arista Networks, Inc.
// Use of this source code is governed by the Apache License 2.0
// that can be found in the LICENSE file.

use avdschema::{any::AnySchema, boolean::Bool, resolve_ref};
use serde_json::Value;

use crate::{
    context::Context,
    feedback::{Type, Violation},
};

use super::{Validation, valid_values::ValidateValidValues as _};

impl Validation<bool> for Bool {
    fn validate(&self, value: &bool, ctx: &mut Context) {
        self.valid_values.validate(value, ctx);
        self.validate_ref(value, ctx);
    }

    fn validate_value(&self, value: &Value, ctx: &mut Context) {
        if let Some(v) = value.as_bool() {
            self.validate(&v, ctx)
        } else {
            ctx.add_violation(Violation::InvalidType {
                expected: Type::Bool,
                found: value.into(),
            })
        }
    }

    fn is_required(&self) -> bool {
        self.base.required.unwrap_or_default()
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
    use avdschema::base::valid_values::ValidValues;

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
        let mut ctx = Context::new(&store);
        schema.validate_value(&input, &mut ctx);
        assert!(ctx.violations.is_empty() && ctx.coercions.is_empty());
    }

    #[test]
    fn validate_type_err() {
        let schema = Bool::default();
        let input = serde_json::json!([]);
        let store = get_test_store();
        let mut ctx = Context::new(&store);
        schema.validate_value(&input, &mut ctx);
        assert!(ctx.coercions.is_empty());
        assert_eq!(
            ctx.violations,
            vec![Feedback {
                path: vec![],
                issue: Violation::InvalidType {
                    expected: Type::Bool,
                    found: Type::List,
                }
                .into(),
            }],
        );
    }

    #[test]
    fn validate_valid_values_ok() {
        let schema = Bool {
            valid_values: ValidValues {
                valid_values: Some(vec![false]),
                ..Default::default()
            },
            ..Default::default()
        };
        let input = false.into();
        let store = get_test_store();
        let mut ctx = Context::new(&store);
        schema.validate_value(&input, &mut ctx);
        assert!(ctx.violations.is_empty() && ctx.coercions.is_empty());
    }

    #[test]
    fn validate_valid_values_err() {
        let schema = Bool {
            valid_values: ValidValues {
                valid_values: Some(vec![false]),
                ..Default::default()
            },
            ..Default::default()
        };
        let input = true.into();
        let store = get_test_store();
        let mut ctx = Context::new(&store);
        schema.validate_value(&input, &mut ctx);
        assert!(ctx.coercions.is_empty());
        assert_eq!(
            ctx.violations,
            vec![Feedback {
                path: vec![],
                issue: Violation::InvalidValue {
                    expected: vec![false].into(),
                    found: input
                }
                .into()
            }]
        );
    }
}
