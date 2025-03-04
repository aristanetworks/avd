// Copyright (c) 2025 Arista Networks, Inc.
// Use of this source code is governed by the Apache License 2.0
// that can be found in the LICENSE file.

use serde::Serialize;
use serde_json::Value;

use crate::{
    context::Context,
    feedback::{Item, MiscViolation, Type, ValidationIssue},
};

use avdschema::int::Int;

use super::{Validation, valid_values::ValidateValidValues};

#[derive(Debug, PartialEq, Eq, Serialize)]
pub enum Violation {
    Minimum { minimum: i64, found: i64 },
    Maximum { maximum: i64, found: i64 },
}

impl From<Violation> for Item {
    fn from(val: Violation) -> Self {
        ValidationIssue::Int(val).into()
    }
}

impl Validation<i64> for Int {
    fn validate(&self, value: &i64, ctx: &mut Context) {
        self.valid_values.validate(value, ctx);
        validate_min(self, value, ctx);
        validate_max(self, value, ctx);
    }

    fn validate_value(&self, value: &Value, ctx: &mut Context) {
        if let Some(v) = value.as_i64() {
            self.validate(&v, ctx)
        } else {
            ctx.add_violation(MiscViolation::InvalidType {
                expected: Type::Int,
                found: value.into(),
            })
        }
    }

    fn is_required(&self) -> bool {
        self.base.required.unwrap_or_default()
    }
}

fn validate_min(schema: &Int, input: &i64, ctx: &mut Context) {
    if let Some(min) = schema.min {
        if min > *input {
            ctx.add_violation(Violation::Minimum {
                minimum: min,
                found: *input,
            });
        }
    }
}

fn validate_max(schema: &Int, input: &i64, ctx: &mut Context) {
    if let Some(max) = schema.max {
        if max < *input {
            ctx.add_violation(Violation::Maximum {
                maximum: max,
                found: *input,
            });
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    use crate::coercion::Coercion as _;
    use crate::context::Context;
    use crate::feedback::{CoercionNote, Feedback, MiscViolation};

    #[test]
    fn validate_type_ok() {
        let schema = Int::default();
        let input = 123.into();
        let mut ctx = Context::new();
        schema.validate_value(&input, &mut ctx);
        assert!(ctx.violations.is_empty() && ctx.coercions.is_empty());
    }

    #[test]
    fn validate_type_err() {
        let schema = Int::default();
        let input = serde_json::json!({});
        let mut ctx = Context::new();
        schema.validate_value(&input, &mut ctx);
        assert!(ctx.coercions.is_empty());
        assert_eq!(
            ctx.violations,
            vec![Feedback {
                path: vec![],
                item: MiscViolation::InvalidType {
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
        let mut ctx = Context::new();
        schema.coerce(&mut input, &mut ctx);
        schema.validate_value(&input, &mut ctx);
        assert!(ctx.violations.is_empty());
        assert_eq!(
            ctx.coercions,
            vec![Feedback {
                path: vec![],
                item: CoercionNote {
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
        let mut ctx = Context::new();
        schema.validate_value(&input, &mut ctx);
        assert!(ctx.coercions.is_empty());
        assert_eq!(
            ctx.violations,
            vec![Feedback {
                path: vec![],
                item: MiscViolation::InvalidType {
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
        let mut ctx = Context::new();
        schema.validate_value(&input, &mut ctx);
        assert!(ctx.violations.is_empty() && ctx.coercions.is_empty());
    }

    #[test]
    fn validate_valid_values_err() {
        let schema = {
            let mut int = Int::default();
            int.valid_values.valid_values = Some(vec![123]);
            int
        };
        let input = 321.into();
        let mut ctx = Context::new();
        schema.validate_value(&input, &mut ctx);
        assert!(ctx.coercions.is_empty());
        assert_eq!(
            ctx.violations,
            vec![Feedback {
                path: vec![],
                item: MiscViolation::DisallowedValue.into()
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
        let mut ctx = Context::new();
        schema.validate_value(&input, &mut ctx);
        assert!(ctx.violations.is_empty() && ctx.coercions.is_empty());
    }

    #[test]
    fn validate_min_err() {
        let schema = Int {
            min: Some(122),
            ..Default::default()
        };
        let input = 121.into();
        let mut ctx = Context::new();
        schema.validate_value(&input, &mut ctx);
        assert!(ctx.coercions.is_empty());
        assert_eq!(
            ctx.violations,
            vec![Feedback {
                path: vec![],
                item: Violation::Minimum {
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
        let mut ctx = Context::new();
        schema.validate_value(&input, &mut ctx);
        assert!(ctx.violations.is_empty() && ctx.coercions.is_empty());
    }

    #[test]
    fn validate_max_err() {
        let schema = Int {
            max: Some(124),
            ..Default::default()
        };
        let input = 125.into();
        let mut ctx = Context::new();
        schema.validate_value(&input, &mut ctx);
        assert!(ctx.coercions.is_empty());
        assert_eq!(
            ctx.violations,
            vec![Feedback {
                path: vec![],
                item: Violation::Maximum {
                    maximum: 124,
                    found: 125
                }
                .into()
            }]
        );
    }
}
