// Copyright (c) 2025 Arista Networks, Inc.
// Use of this source code is governed by the Apache License 2.0
// that can be found in the LICENSE file.

use avdschema::{any::AnySchema, resolve_ref, str::Str};
use regex::Regex;
use serde_json::Value;

use crate::{
    context::Context,
    feedback::{Issue, Type, Violation},
};

use super::{Validation, valid_values::ValidateValidValues as _};

impl Validation<String> for Str {
    fn validate(&self, value: &String, ctx: &mut Context) {
        self.valid_values.validate(value, ctx);
        validate_min_length(self, value, ctx);
        validate_max_length(self, value, ctx);
        validate_pattern(self, value, ctx);
        self.validate_ref(value, ctx);
    }

    fn validate_value(&self, value: &Value, ctx: &mut Context) {
        if let Some(v) = value.as_str() {
            self.validate(&v.into(), ctx)
        } else {
            ctx.add_violation(Violation::InvalidType {
                expected: Type::Str,
                found: value.into(),
            })
        }
    }

    fn is_required(&self) -> bool {
        self.base.required.unwrap_or_default()
    }

    fn validate_ref(&self, value: &String, ctx: &mut Context) {
        if let Some(ref_) = self.base.schema_ref.as_ref() {
            // Ignoring not being able to resolve the schema.
            // Ignoring a wrong schema type at the ref. Since Validation is infallible.
            // TODO: What to do?
            if let Ok(AnySchema::Str(ref_schema)) = resolve_ref(ref_, ctx.store) {
                ref_schema.validate(value, ctx);
            }
        }
    }

    fn default_value(&self) -> Option<String> {
        self.base.default.to_owned()
    }
}

fn validate_min_length(schema: &Str, input: &str, ctx: &mut Context) {
    if let Some(min_length) = schema.min_length {
        let length = input.chars().count() as u64;
        if min_length > length {
            ctx.add_violation(Violation::LengthBelowMinimum {
                minimum: min_length,
                found: length,
            });
        }
    }
}

fn validate_max_length(schema: &Str, input: &str, ctx: &mut Context) {
    if let Some(max_length) = schema.max_length {
        let length = input.chars().count() as u64;
        if max_length < length {
            ctx.add_violation(Violation::LengthAboveMaximum {
                maximum: max_length,
                found: length,
            });
        }
    }
}

fn validate_pattern(schema: &Str, input: &str, ctx: &mut Context) {
    if let Some(pattern) = schema.pattern.as_deref() {
        match Regex::new(&format!("^{pattern}$")) {
            Ok(regex) => {
                if !regex.is_match(input) {
                    ctx.add_violation(Violation::NotMatchingPattern {
                        pattern: pattern.to_string(),
                        found: input.into(),
                    });
                }
            }
            Err(e) => ctx.add_violation(Issue::InternalError {
                message: e.to_string(),
            }),
        }
    }
}

#[cfg(test)]
mod tests {
    use avdschema::base::valid_values::ValidValues;

    use super::*;
    use crate::{
        coercion::Coercion,
        feedback::{CoercionNote, Feedback},
        validation::test_utils::get_test_store,
    };

    #[test]
    fn validate_type_ok() {
        let schema = Str::default();
        let input = "foo".into();
        let store = get_test_store();
        let mut ctx = Context::new(&store, None);
        schema.validate_value(&input, &mut ctx);
        assert!(ctx.violations.is_empty() && ctx.coercions.is_empty());
    }

    #[test]
    fn validate_type_err() {
        let schema = Str::default();
        let input = serde_json::json!([]);
        let store = get_test_store();
        let mut ctx = Context::new(&store, None);
        schema.validate_value(&input, &mut ctx);
        assert!(ctx.coercions.is_empty());
        assert_eq!(
            ctx.violations,
            vec![Feedback {
                path: vec![],
                issue: Violation::InvalidType {
                    expected: Type::Str,
                    found: Type::List
                }
                .into()
            }]
        );
    }

    #[test]
    fn validate_valid_values_ok() {
        let schema = Str {
            valid_values: ValidValues {
                valid_values: Some(vec!["foo".into()]),
                ..Default::default()
            },
            ..Default::default()
        };
        let input = "foo".into();
        let store = get_test_store();
        let mut ctx = Context::new(&store, None);
        schema.validate_value(&input, &mut ctx);
        assert!(ctx.violations.is_empty() && ctx.coercions.is_empty());
    }

    #[test]
    fn validate_valid_values_err() {
        let schema = Str {
            valid_values: ValidValues {
                valid_values: Some(vec!["foo".into()]),
                ..Default::default()
            },
            ..Default::default()
        };
        let input = "FOO".into();
        let store = get_test_store();
        let mut ctx = Context::new(&store, None);
        schema.validate_value(&input, &mut ctx);
        assert!(ctx.coercions.is_empty());
        assert_eq!(
            ctx.violations,
            vec![Feedback {
                path: vec![],
                issue: Violation::InvalidValue {
                    expected: vec!["foo".to_string()].into(),
                    found: "FOO".into()
                }
                .into()
            }]
        );
    }

    #[test]
    fn validate_valid_values_to_lower_case_ok() {
        let schema = Str {
            valid_values: ValidValues {
                valid_values: Some(vec!["foo".into()]),
                ..Default::default()
            },
            convert_to_lower_case: Some(true),
            ..Default::default()
        };
        let mut input = "FOO".into();
        let store = get_test_store();
        let mut ctx = Context::new(&store, None);
        schema.coerce(&mut input, &mut ctx);
        schema.validate_value(&input, &mut ctx);
        assert!(ctx.violations.is_empty());
        assert_eq!(
            ctx.coercions,
            vec![Feedback {
                path: vec![],
                issue: CoercionNote {
                    found: "FOO".into(),
                    made: "foo".into()
                }
                .into()
            }]
        );
    }

    #[test]
    fn validate_valid_values_from_bool_to_lower_case_ok() {
        let schema = Str {
            valid_values: ValidValues {
                valid_values: Some(vec!["true".into()]),
                ..Default::default()
            },
            convert_to_lower_case: Some(true),
            ..Default::default()
        };
        let mut input = true.into();
        let store = get_test_store();
        let mut ctx = Context::new(&store, None);
        schema.coerce(&mut input, &mut ctx);
        schema.validate_value(&input, &mut ctx);
        assert!(ctx.violations.is_empty());
        assert_eq!(
            ctx.coercions,
            vec![
                Feedback {
                    path: vec![],
                    issue: CoercionNote {
                        found: true.into(),
                        made: "True".into()
                    }
                    .into()
                },
                Feedback {
                    path: vec![],
                    issue: CoercionNote {
                        found: "True".into(),
                        made: "true".into()
                    }
                    .into()
                }
            ]
        );
    }

    #[test]
    fn validate_min_length_ok() {
        let schema = Str {
            min_length: Some(3),
            ..Default::default()
        };
        let input = "foo".into();
        let store = get_test_store();
        let mut ctx = Context::new(&store, None);
        schema.validate_value(&input, &mut ctx);
        assert!(ctx.violations.is_empty() && ctx.coercions.is_empty());
    }

    #[test]
    fn validate_min_length_err() {
        let schema = Str {
            min_length: Some(3),
            ..Default::default()
        };
        let input = "go".into();
        let store = get_test_store();
        let mut ctx = Context::new(&store, None);
        schema.validate_value(&input, &mut ctx);
        assert!(ctx.coercions.is_empty());
        assert_eq!(
            ctx.violations,
            vec![Feedback {
                path: vec![],
                issue: Violation::LengthBelowMinimum {
                    minimum: 3,
                    found: 2
                }
                .into()
            }]
        );
    }

    #[test]
    fn validate_max_length_ok() {
        let schema = Str {
            max_length: Some(3),
            ..Default::default()
        };
        let input = "foo".into();
        let store = get_test_store();
        let mut ctx = Context::new(&store, None);
        schema.validate_value(&input, &mut ctx);
        assert!(ctx.violations.is_empty() && ctx.coercions.is_empty());
    }

    #[test]
    fn validate_max_length_err() {
        let schema = Str {
            max_length: Some(3),
            ..Default::default()
        };
        let input = "fooo".into();
        let store = get_test_store();
        let mut ctx = Context::new(&store, None);
        schema.validate_value(&input, &mut ctx);
        assert!(ctx.coercions.is_empty());
        assert_eq!(
            ctx.violations,
            vec![Feedback {
                path: vec![],
                issue: Violation::LengthAboveMaximum {
                    maximum: 3,
                    found: 4
                }
                .into()
            }]
        );
    }

    #[test]
    fn validate_pattern_ok() {
        let schema = Str {
            pattern: Some("[a-z][A-Z][a-z]".into()),
            ..Default::default()
        };
        let input = "fOo".into();
        let store = get_test_store();
        let mut ctx = Context::new(&store, None);
        schema.validate_value(&input, &mut ctx);
        assert!(ctx.violations.is_empty() && ctx.coercions.is_empty());
    }

    #[test]
    fn validate_pattern_err() {
        let schema = Str {
            pattern: Some("[a-z][A-Z][a-z]".into()),
            ..Default::default()
        };
        let input = "foo".into();
        let store = get_test_store();
        let mut ctx = Context::new(&store, None);
        schema.validate_value(&input, &mut ctx);
        assert!(ctx.coercions.is_empty());
        assert_eq!(
            ctx.violations,
            vec![Feedback {
                path: vec![],
                issue: Violation::NotMatchingPattern {
                    pattern: "[a-z][A-Z][a-z]".into(),
                    found: "foo".into(),
                }
                .into()
            }]
        );
    }
}
