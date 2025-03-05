// Copyright (c) 2025 Arista Networks, Inc.
// Use of this source code is governed by the Apache License 2.0
// that can be found in the LICENSE file.

use avdschema::boolean::Bool;
use serde_json::Value;

use crate::{
    context::Context,
    feedback::{Type, Violation},
};

use super::{Validation, valid_values::ValidateValidValues as _};

impl Validation<bool> for Bool {
    fn validate(&self, value: &bool, ctx: &mut Context) {
        self.valid_values.validate(value, ctx);
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
}

#[cfg(test)]
mod tests {
    use avdschema::base::valid_values::ValidValues;

    use super::*;
    use crate::feedback::{Feedback, Type, Violation};

    #[test]
    fn validate_type_ok() {
        let schema = Bool::default();
        let input = true.into();
        let mut ctx = Context::new();
        schema.validate_value(&input, &mut ctx);
        assert!(ctx.violations.is_empty() && ctx.coercions.is_empty());
    }

    #[test]
    fn validate_type_err() {
        let schema = Bool::default();
        let input = serde_json::json!([]);
        let mut ctx = Context::new();
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
        let mut ctx = Context::new();
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
        let mut ctx = Context::new();
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
