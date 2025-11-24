// Copyright (c) 2025 Arista Networks, Inc.
// Use of this source code is governed by the Apache License 2.0
// that can be found in the LICENSE file.

use serde_json::Value;

use crate::{
    context::Context,
    feedback::{Type, Violation},
};

use avdschema::{any::AnySchema, int::Int, resolve_ref};

use super::{Validation, valid_values::ValidateValidValues};

impl Validation<i64> for Int {
    fn validate(&self, value: &i64, ctx: &mut Context) {
        self.valid_values.validate(value, ctx);
        validate_min(self, value, ctx);
        validate_max(self, value, ctx);
        self.validate_ref(value, ctx);
    }

    fn validate_value(&self, value: &Value, ctx: &mut Context) {
        if let Some(v) = value.as_i64() {
            self.validate(&v, ctx)
        } else if value.is_null() && !ctx.configuration.restrict_null_values {
        } else {
            ctx.add_error(Violation::InvalidType {
                expected: Type::Int,
                found: value.into(),
            })
        }
    }

    fn validate_ref(&self, value: &i64, ctx: &mut Context) {
        if let Some(ref_) = self.base.schema_ref.as_ref() {
            // Ignoring not being able to resolve the schema.
            // Ignoring a wrong schema type at the ref. Since Validation is infallible.
            // TODO: What to do?
            if let Ok(AnySchema::Int(ref_schema)) = resolve_ref(ref_, ctx.store) {
                ref_schema.validate(value, ctx);
            }
        }
    }
}

fn validate_min(schema: &Int, input: &i64, ctx: &mut Context) {
    if let Some(min) = schema.min
        && min > *input
    {
        ctx.add_error(Violation::ValueBelowMinimum {
            minimum: min,
            found: *input,
        });
    }
}

fn validate_max(schema: &Int, input: &i64, ctx: &mut Context) {
    if let Some(max) = schema.max
        && max < *input
    {
        ctx.add_error(Violation::ValueAboveMaximum {
            maximum: max,
            found: *input,
        });
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    use crate::Configuration;
    use crate::coercion::Coercion as _;
    use crate::context::Context;
    use crate::feedback::{CoercionNote, Feedback, Violation};
    use crate::validation::test_utils::get_test_store;

    #[test]
    fn validate_type_ok() {
        let schema = Int::default();
        let input = 123.into();
        let store = get_test_store();
        let mut ctx = Context::new(&store, None);
        schema.validate_value(&input, &mut ctx);
        assert!(ctx.result.errors.is_empty() && ctx.result.infos.is_empty());
    }

    #[test]
    fn validate_type_err() {
        let schema = Int::default();
        let input = serde_json::json!({});
        let store = get_test_store();
        let mut ctx = Context::new(&store, None);
        schema.validate_value(&input, &mut ctx);
        assert!(ctx.result.infos.is_empty());
        assert_eq!(
            ctx.result.errors,
            vec![Feedback {
                path: vec![].into(),
                issue: Violation::InvalidType {
                    expected: Type::Int,
                    found: Type::Dict,
                }
                .into()
            }]
        );
    }

    #[test]
    fn validate_type_coerced_from_str_ok() {
        let schema = Int::default();
        let mut input = "123".into();
        let store = get_test_store();
        let configuration = Configuration {
            return_coercion_infos: true,
            ..Default::default()
        };
        let mut ctx = Context::new(&store, Some(&configuration));
        schema.coerce(&mut input, &mut ctx);
        schema.validate_value(&input, &mut ctx);
        assert!(ctx.result.errors.is_empty());
        assert_eq!(
            ctx.result.infos,
            vec![Feedback {
                path: vec![].into(),
                issue: CoercionNote {
                    found: "123".into(),
                    made: 123.into()
                }
                .into()
            }]
        );
    }

    #[test]
    fn validate_type_coerced_from_str_err() {
        let schema = Int::default();
        let input = "one23".into();
        let store = get_test_store();
        let mut ctx = Context::new(&store, None);
        schema.validate_value(&input, &mut ctx);
        assert!(ctx.result.infos.is_empty());
        assert_eq!(
            ctx.result.errors,
            vec![Feedback {
                path: vec![].into(),
                issue: Violation::InvalidType {
                    expected: Type::Int,
                    found: Type::Str
                }
                .into()
            }]
        );
    }

    #[test]
    fn validate_valid_values_ok() {
        let schema = {
            let mut int = Int::default();
            int.valid_values.valid_values = Some(vec![123]);
            int
        };
        let input = 123.into();
        let store = get_test_store();
        let mut ctx = Context::new(&store, None);
        schema.validate_value(&input, &mut ctx);
        assert!(ctx.result.errors.is_empty() && ctx.result.infos.is_empty());
    }

    #[test]
    fn validate_valid_values_err() {
        let schema = {
            let mut int = Int::default();
            int.valid_values.valid_values = Some(vec![123]);
            int
        };
        let input = 321.into();
        let store = get_test_store();
        let mut ctx = Context::new(&store, None);
        schema.validate_value(&input, &mut ctx);
        assert!(ctx.result.infos.is_empty());
        assert_eq!(
            ctx.result.errors,
            vec![Feedback {
                path: vec![].into(),
                issue: Violation::InvalidValue {
                    expected: vec![123].into(),
                    found: input.into()
                }
                .into()
            }]
        );
    }

    #[test]
    fn validate_min_ok() {
        let schema = Int {
            min: Some(122),
            ..Default::default()
        };
        let input = 123.into();
        let store = get_test_store();
        let mut ctx = Context::new(&store, None);
        schema.validate_value(&input, &mut ctx);
        assert!(ctx.result.errors.is_empty() && ctx.result.infos.is_empty());
    }

    #[test]
    fn validate_min_err() {
        let schema = Int {
            min: Some(122),
            ..Default::default()
        };
        let input = 121.into();
        let store = get_test_store();
        let mut ctx = Context::new(&store, None);
        schema.validate_value(&input, &mut ctx);
        assert!(ctx.result.infos.is_empty());
        assert_eq!(
            ctx.result.errors,
            vec![Feedback {
                path: vec![].into(),
                issue: Violation::ValueBelowMinimum {
                    minimum: 122,
                    found: 121
                }
                .into()
            }]
        );
    }

    #[test]
    fn validate_max_ok() {
        let schema = Int {
            max: Some(124),
            ..Default::default()
        };
        let input = 123.into();
        let store = get_test_store();
        let mut ctx = Context::new(&store, None);
        schema.validate_value(&input, &mut ctx);
        assert!(ctx.result.errors.is_empty() && ctx.result.infos.is_empty());
    }

    #[test]
    fn validate_max_err() {
        let schema = Int {
            max: Some(124),
            ..Default::default()
        };
        let input = 125.into();
        let store = get_test_store();
        let mut ctx = Context::new(&store, None);
        schema.validate_value(&input, &mut ctx);
        assert!(ctx.result.infos.is_empty());
        assert_eq!(
            ctx.result.errors,
            vec![Feedback {
                path: vec![].into(),
                issue: Violation::ValueAboveMaximum {
                    maximum: 124,
                    found: 125
                }
                .into()
            }]
        );
    }
}
