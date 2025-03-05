// Copyright (c) 2025 Arista Networks, Inc.
// Use of this source code is governed by the Apache License 2.0
// that can be found in the LICENSE file.

use avdschema::dict::Dict;
use serde_json::{Map, Value};

use crate::{
    context::Context,
    feedback::{Type, Violation},
    utils::dynamic_keys::get_dynamic_keys,
};

use super::Validation;

impl Validation<Map<String, Value>> for Dict {
    fn validate(&self, value: &Map<String, Value>, ctx: &mut Context) {
        validate_keys(self, value, ctx);
        validate_allowed_keys(self, value, ctx);
        validate_dynamic_keys(self, value, ctx);
    }

    fn validate_value(&self, value: &Value, ctx: &mut Context) {
        if let Some(v) = value.as_object() {
            self.validate(v, ctx)
        } else {
            ctx.add_violation(Violation::InvalidType {
                expected: Type::Dict,
                found: value.into(),
            })
        }
    }

    fn is_required(&self) -> bool {
        self.base.required.unwrap_or_default()
    }
}

fn validate_allowed_keys(schema: &Dict, input: &Map<String, Value>, ctx: &mut Context) {
    if !schema.allow_other_keys.unwrap_or_default() {
        if let Some(keys) = &schema.keys {
            if let Some(key) = input
                .keys()
                // keys starting with "_" are passed over to allow for custom usage
                .filter(|key| !key.starts_with('_'))
                .find(|key| !keys.contains_key(key.as_str()))
            {
                ctx.add_violation(Violation::UnexpectedKey {
                    key: key.to_string(),
                });
            }
        }
    }
}

fn validate_keys(schema: &Dict, input: &Map<String, Value>, ctx: &mut Context) {
    if let Some(keys) = &schema.keys {
        for (key, key_schema) in keys {
            match input.get(key) {
                Some(Value::Null) | None => {
                    // nullish values don't need to be validated beyond a requiredness check
                    if key_schema.is_required() {
                        ctx.add_violation(Violation::MissingRequiredKey {
                            key: key.to_string(),
                        });
                    }
                }
                Some(value) => {
                    ctx.path.push(key.to_owned());
                    key_schema.validate(value, ctx);
                    ctx.path.pop();
                }
            }
        }
    }
}

fn validate_dynamic_keys(schema: &Dict, input: &Map<String, Value>, ctx: &mut Context) {
    if let Some(dynamic_keys) = &schema.dynamic_keys {
        for (key_path, key_schema) in dynamic_keys {
            let keys = get_dynamic_keys(key_path, input);
            // validate the computed dynamic keys' corresponding values
            for key in keys {
                if let Some(value) = input.get(&key) {
                    ctx.path.push(key);
                    key_schema.validate(value, ctx);
                    ctx.path.pop();
                }
            }
        }
    }
}

#[cfg(test)]
mod tests {
    use avdschema::base::Base;
    use avdschema::int::Int;
    use avdschema::list::List;
    use avdschema::str::Str;
    use ordermap::OrderMap;

    use super::*;
    use crate::coercion::Coercion as _;
    use crate::context::Context;
    use crate::feedback::{CoercionNote, Feedback};

    #[test]
    fn validate_type_ok() {
        let schema = Dict::default();
        let input = serde_json::json!({ "foo": true });
        let mut ctx = Context::new();
        schema.validate_value(&input, &mut ctx);
        assert!(ctx.violations.is_empty() && ctx.coercions.is_empty());
    }

    #[test]
    fn validate_type_err() {
        let schema = Dict::default();
        let input = serde_json::json!(true);
        let mut ctx = Context::new();
        schema.validate_value(&input, &mut ctx);
        assert!(ctx.coercions.is_empty());
        assert_eq!(
            ctx.violations,
            vec![Feedback {
                path: vec![],
                issue: Violation::InvalidType {
                    expected: Type::Dict,
                    found: Type::Bool
                }
                .into()
            }]
        );
    }

    #[test]
    fn validate_key_type_ok() {
        let schema = Dict {
            keys: Some(OrderMap::from_iter([
                ("foo".into(), Str::default().into()),
                ("bar".into(), Int::default().into()),
            ])),
            ..Default::default()
        };
        let input = serde_json::json!({ "foo": "bar", "bar": 123 });
        let mut ctx = Context::new();
        schema.validate_value(&input, &mut ctx);
        assert!(ctx.violations.is_empty() && ctx.coercions.is_empty());
    }

    #[test]
    fn validate_key_type_err() {
        let schema = Dict {
            keys: Some(OrderMap::from_iter([
                ("foo".into(), Str::default().into()),
                ("bar".into(), Int::default().into()),
            ])),
            ..Default::default()
        };
        let input = serde_json::json!({ "foo": [], "bar": "boo" });
        let mut ctx = Context::new();
        schema.validate_value(&input, &mut ctx);
        assert!(ctx.coercions.is_empty());
        assert_eq!(
            ctx.violations,
            vec![
                Feedback {
                    path: vec!["foo".into()],
                    issue: Violation::InvalidType {
                        expected: Type::Str,
                        found: Type::List
                    }
                    .into()
                },
                Feedback {
                    path: vec!["bar".into()],
                    issue: Violation::InvalidType {
                        expected: Type::Int,
                        found: Type::Str
                    }
                    .into()
                }
            ]
        )
    }

    #[test]
    fn validate_key_type_coerced_ok() {
        let schema = Dict {
            keys: Some(OrderMap::from_iter([
                ("foo".into(), Str::default().into()),
                ("bar".into(), Int::default().into()),
            ])),
            ..Default::default()
        };
        let mut input = serde_json::json!({ "foo": 321, "bar": "123" });
        let mut ctx = Context::new();
        schema.coerce(&mut input, &mut ctx);
        schema.validate_value(&input, &mut ctx);
        assert!(ctx.violations.is_empty());
        assert_eq!(
            ctx.coercions,
            vec![
                Feedback {
                    path: vec!["foo".into()],
                    issue: CoercionNote {
                        found: 321.into(),
                        made: "321".into()
                    }
                    .into()
                },
                Feedback {
                    path: vec!["bar".into()],
                    issue: CoercionNote {
                        found: "123".into(),
                        made: 123.into()
                    }
                    .into()
                }
            ]
        )
    }

    #[test]
    fn validate_dynamic_keys_ok() {
        let schema = Dict {
            keys: Some(OrderMap::from_iter([(
                "my_dynamic_keys".into(),
                List {
                    items: Some(Box::new(Str::default().into())),
                    ..Default::default()
                }
                .into(),
            )])),
            dynamic_keys: Some(OrderMap::from_iter([(
                "my_dynamic_keys".into(),
                Int {
                    max: Some(10),
                    ..Default::default()
                }
                .into(),
            )])),
            allow_other_keys: Some(true),
            ..Default::default()
        };
        let input = serde_json::json!({ "my_dynamic_keys": ["dynkey1", "dynkey2"], "dynkey1": 5, "dynkey2": 9 });
        let mut ctx = Context::new();
        schema.validate_value(&input, &mut ctx);
        assert!(ctx.violations.is_empty() && ctx.coercions.is_empty());
    }

    #[test]
    fn validate_dynamic_keys_err() {
        let schema = Dict {
            keys: Some(OrderMap::from_iter([(
                "my_dynamic_keys".into(),
                List {
                    items: Some(Box::new(Str::default().into())),
                    ..Default::default()
                }
                .into(),
            )])),
            dynamic_keys: Some(OrderMap::from_iter([(
                "my_dynamic_keys".into(),
                Int {
                    max: Some(10),
                    ..Default::default()
                }
                .into(),
            )])),
            allow_other_keys: Some(true),
            ..Default::default()
        };
        let input = serde_json::json!({ "my_dynamic_keys": ["dynkey1", "dynkey2"], "dynkey1": 11, "dynkey2": "wrong" });
        let mut ctx = Context::new();
        schema.validate_value(&input, &mut ctx);
        assert!(ctx.coercions.is_empty());
        assert_eq!(
            ctx.violations,
            vec![
                Feedback {
                    path: vec!["dynkey1".into()],
                    issue: Violation::ValueAboveMaximum {
                        maximum: 10,
                        found: 11
                    }
                    .into()
                },
                Feedback {
                    path: vec!["dynkey2".into()],
                    issue: Violation::InvalidType {
                        expected: Type::Int,
                        found: Type::Str
                    }
                    .into()
                }
            ]
        )
    }

    #[test]
    fn validate_key_allowed_ok() {
        let schema = Dict {
            keys: Some(OrderMap::from_iter([("foo".into(), Str::default().into())])),
            allow_other_keys: Some(true),
            ..Default::default()
        };
        let input = serde_json::json!({ "foo": "ok", "foo1": "wrong" });
        let mut ctx = Context::new();
        schema.validate_value(&input, &mut ctx);
        assert!(ctx.violations.is_empty() && ctx.coercions.is_empty());
    }

    #[test]
    fn validate_key_allowed_err() {
        let schema = Dict {
            keys: Some(OrderMap::from_iter([("foo".into(), Str::default().into())])),
            ..Default::default()
        };
        let input = serde_json::json!({ "foo": "ok", "foo1": "wrong", "_internal": "ignored" });
        let mut ctx = Context::new();
        schema.validate_value(&input, &mut ctx);
        assert!(ctx.coercions.is_empty());
        assert_eq!(
            ctx.violations,
            vec![Feedback {
                path: vec![],
                issue: Violation::UnexpectedKey { key: "foo1".into() }.into()
            }]
        )
    }

    #[test]
    fn validate_key_required_ok() {
        let schema = Dict {
            keys: Some(OrderMap::from_iter([(
                "foo".into(),
                Str {
                    base: Base {
                        required: Some(true),
                        ..Default::default()
                    },
                    ..Default::default()
                }
                .into(),
            )])),
            ..Default::default()
        };
        let mut input = serde_json::json!({ "foo": true });
        let mut ctx = Context::new();
        schema.coerce(&mut input, &mut ctx);
        schema.validate_value(&input, &mut ctx);
        assert!(ctx.violations.is_empty());
        assert_eq!(
            ctx.coercions,
            vec![Feedback {
                path: vec!["foo".into()],
                issue: CoercionNote {
                    found: true.into(),
                    made: "True".into()
                }
                .into()
            }]
        )
    }

    #[test]
    fn validate_key_required_err() {
        let schema = Dict {
            keys: Some(OrderMap::from_iter([(
                "foo".into(),
                Str {
                    base: Base {
                        required: Some(true),
                        ..Default::default()
                    },
                    ..Default::default()
                }
                .into(),
            )])),
            ..Default::default()
        };
        let input = serde_json::json!({});
        let mut ctx = Context::new();
        schema.validate_value(&input, &mut ctx);
        assert!(ctx.coercions.is_empty());
        assert_eq!(
            ctx.violations,
            vec![Feedback {
                path: vec![],
                issue: Violation::MissingRequiredKey { key: "foo".into() }.into()
            }]
        )
    }
}
