// Copyright (c) 2025 Arista Networks, Inc.
// Use of this source code is governed by the Apache License 2.0
// that can be found in the LICENSE file.

use avdschema::str::Str;
use regex::Regex;
use serde::Serialize;
use serde_json::Value;

use crate::{
    context::Context,
    feedback::{Item, MiscViolation, Type, ValidationIssue},
};

use super::{Validation, valid_values::ValidateValidValues as _};

#[derive(Debug, PartialEq, Eq, Serialize)]
pub enum Violation {
    MinimumLength { minimum: u64, found: u64 },
    MaximumLength { maximum: u64, found: u64 },
    Pattern { pattern: String },
}

impl From<Violation> for Item {
    fn from(val: Violation) -> Self {
        ValidationIssue::String(val).into()
    }
}

impl Validation<String> for Str {
    fn validate(&self, value: &String, ctx: &mut Context) {
        self.valid_values.validate(value, ctx);
        validate_min_length(self, value, ctx);
        validate_max_length(self, value, ctx);
        validate_pattern(self, value, ctx);
    }

    fn validate_value(&self, value: &Value, ctx: &mut Context) {
        if let Some(v) = value.as_str() {
            self.validate(&v.into(), ctx)
        } else {
            ctx.add_violation(MiscViolation::InvalidType {
                expected: Type::Str,
                found: value.into(),
            })
        }
    }

    fn is_required(&self) -> bool {
        self.base.required.unwrap_or_default()
    }
}

fn validate_min_length(schema: &Str, input: &str, ctx: &mut Context) {
    if let Some(min_length) = schema.min_length {
        let length = input.chars().count() as u64;
        if min_length > length {
            ctx.add_violation(Violation::MinimumLength {
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
            ctx.add_violation(Violation::MaximumLength {
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
                    ctx.add_violation(Violation::Pattern {
                        pattern: pattern.to_string(),
                    });
                }
            }
            Err(e) => ctx.add_violation(MiscViolation::InvalidRegex {
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
    };

    #[test]
    fn validate_type_ok() {
        let schema = Str::default();
        let input = "foo".into();
        let mut ctx = Context::new();
        schema.validate_value(&input, &mut ctx);
        assert!(ctx.violations.is_empty() && ctx.coercions.is_empty());
    }

    #[test]
    fn validate_type_err() {
        let schema = Str::default();
        let input = serde_json::json!([]);
        let mut ctx = Context::new();
        schema.validate_value(&input, &mut ctx);
        assert!(ctx.coercions.is_empty());
        assert_eq!(
            ctx.violations,
            vec![Feedback {
                path: vec![],
                item: MiscViolation::InvalidType {
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
        let mut ctx = Context::new();
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
        let mut ctx = Context::new();
        schema.coerce(&mut input, &mut ctx);
        schema.validate_value(&input, &mut ctx);
        assert!(ctx.violations.is_empty());
        assert_eq!(
            ctx.coercions,
            vec![Feedback {
                path: vec![],
                item: CoercionNote {
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
        let mut ctx = Context::new();
        schema.coerce(&mut input, &mut ctx);
        schema.validate_value(&input, &mut ctx);
        assert!(ctx.violations.is_empty());
        assert_eq!(
            ctx.coercions,
            vec![
                Feedback {
                    path: vec![],
                    item: CoercionNote {
                        found: true.into(),
                        made: "True".into()
                    }
                    .into()
                },
                Feedback {
                    path: vec![],
                    item: CoercionNote {
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
        let mut ctx = Context::new();
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
        let mut ctx = Context::new();
        schema.validate_value(&input, &mut ctx);
        assert!(ctx.coercions.is_empty());
        assert_eq!(
            ctx.violations,
            vec![Feedback {
                path: vec![],
                item: Violation::MinimumLength {
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
        let mut ctx = Context::new();
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
        let mut ctx = Context::new();
        schema.validate_value(&input, &mut ctx);
        assert!(ctx.coercions.is_empty());
        assert_eq!(
            ctx.violations,
            vec![Feedback {
                path: vec![],
                item: Violation::MaximumLength {
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
        let mut ctx = Context::new();
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
        let mut ctx = Context::new();
        schema.validate_value(&input, &mut ctx);
        assert!(ctx.coercions.is_empty());
        assert_eq!(
            ctx.violations,
            vec![Feedback {
                path: vec![],
                item: Violation::Pattern {
                    pattern: "[a-z][A-Z][a-z]".into()
                }
                .into()
            }]
        );
    }
}
