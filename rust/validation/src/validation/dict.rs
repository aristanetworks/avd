// Copyright (c) 2025 Arista Networks, Inc.
// Use of this source code is governed by the Apache License 2.0
// that can be found in the LICENSE file.

use avdschema::{any::AnySchema, dict::Dict, get_dynamic_keys, resolve_ref};
use serde_json::{Map, Value};

use crate::{
    context::Context,
    feedback::{Type, Violation},
};

use super::Validation;

impl Validation<Map<String, Value>> for Dict {
    fn validate(&self, value: &Map<String, Value>, ctx: &mut Context) {
        validate_keys(self, value, ctx);
        validate_allowed_keys(self, value, ctx);
        validate_dynamic_keys(self, value, ctx);
        self.validate_ref(value, ctx);
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

    fn validate_ref(&self, value: &Map<String, Value>, ctx: &mut Context) {
        if let Some(ref_) = self.base.schema_ref.as_ref() {
            // Ignoring not being able to resolve the schema.
            // Ignoring a wrong schema type at the ref. Since Validation is infallible.
            // TODO: What to do?
            if let Ok(AnySchema::Dict(ref_schema)) = resolve_ref(ref_, ctx.store) {
                ref_schema.validate(value, ctx);
            }
        }
    }

    fn default_value(&self) -> Option<Map<String, Value>> {
        if let Some(value) = &self.base.default {
            let value = value.to_owned();
            let map = Map::from_iter(value);
            Some(map)
        } else {
            None
        }
    }
}

fn validate_allowed_keys(schema: &Dict, input: &Map<String, Value>, ctx: &mut Context) {
    if !schema.allow_other_keys.unwrap_or_default()
        && let Some(keys) = &schema.keys {
            input
                .keys()
                // keys starting with "_" are passed over to allow for custom usage
                .filter(|key| !key.starts_with('_'))
                .filter(|key| !keys.contains_key(key.as_str()))
                .for_each(|key| {
                    ctx.path.push(key.to_owned());
                    ctx.add_violation(Violation::UnexpectedKey());
                    ctx.path.pop();
                });
        }
}

fn validate_keys(schema: &Dict, input: &Map<String, Value>, ctx: &mut Context) {
    if let Some(keys) = &schema.keys {
        for (key, key_schema) in keys {
            match input.get(key) {
                Some(Value::Null) | None => {
                    // nullish values don't need to be validated beyond a requiredness check

                    // Don't validate required keys if we are at the root level.
                    if ctx.configuration.ignore_required_keys_on_root_dict && ctx.path.is_empty() {
                        continue;
                    }
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
    use crate::context::{Configuration, Context};
    use crate::feedback::{CoercionNote, Feedback, Issue};
    use crate::validation::test_utils::get_test_store;

    #[test]
    fn validate_type_ok() {
        let schema = Dict::default();
        let input = serde_json::json!({ "foo": true });
        let store = get_test_store();
        let mut ctx = Context::new(&store, None);
        schema.validate_value(&input, &mut ctx);
        assert!(ctx.violations.is_empty() && ctx.coercions.is_empty());
    }

    #[test]
    fn validate_type_err() {
        let schema = Dict::default();
        let input = serde_json::json!(true);
        let store = get_test_store();
        let mut ctx = Context::new(&store, None);
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
        let store = get_test_store();
        let mut ctx = Context::new(&store, None);
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
        let store = get_test_store();
        let mut ctx = Context::new(&store, None);
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
        let store = get_test_store();
        let mut ctx = Context::new(&store, None);
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
                    items: Some(Box::new(
                        Dict {
                            keys: Some(OrderMap::from_iter([(
                                "key".into(),
                                Str::default().into(),
                            )])),
                            ..Default::default()
                        }
                        .into(),
                    )),
                    ..Default::default()
                }
                .into(),
            )])),
            dynamic_keys: Some(OrderMap::from_iter([(
                "my_dynamic_keys.key".into(),
                Int {
                    max: Some(10),
                    ..Default::default()
                }
                .into(),
            )])),
            allow_other_keys: Some(true),
            ..Default::default()
        };
        let input = serde_json::json!(
            { "my_dynamic_keys": [{"key": "dynkey1"}, {"key": "dynkey2"}], "dynkey1": 5, "dynkey2": 9 });
        let store = get_test_store();
        let mut ctx = Context::new(&store, None);
        schema.validate_value(&input, &mut ctx);
        assert_eq!(ctx.violations, vec![]);
        assert_eq!(ctx.coercions, vec![]);
    }

    #[test]
    fn validate_dynamic_keys_err() {
        let schema = Dict {
            keys: Some(OrderMap::from_iter([(
                "my_dynamic_keys".into(),
                List {
                    items: Some(Box::new(
                        Dict {
                            keys: Some(OrderMap::from_iter([(
                                "key".into(),
                                Str::default().into(),
                            )])),
                            ..Default::default()
                        }
                        .into(),
                    )),
                    ..Default::default()
                }
                .into(),
            )])),
            dynamic_keys: Some(OrderMap::from_iter([(
                "my_dynamic_keys.key".into(),
                Int {
                    max: Some(10),
                    ..Default::default()
                }
                .into(),
            )])),
            allow_other_keys: Some(true),
            ..Default::default()
        };
        let input = serde_json::json!(
            { "my_dynamic_keys": [{"key": "dynkey1"}, {"key": "dynkey2"}], "dynkey1": 11, "dynkey2": "wrong" });
        let store = get_test_store();
        let mut ctx = Context::new(&store, None);
        schema.validate_value(&input, &mut ctx);
        assert_eq!(ctx.coercions, vec![]);
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
    fn validate_dynamic_keys_from_defaults_ok() {
        let schema = Dict {
            keys: Some(OrderMap::from_iter([(
                "my_dynamic_keys".into(),
                List {
                    items: Some(Box::new(Str::default().into())),
                    base: Base {
                        default: Some(vec!["dynkey1".into(), "dynkey2".into()]),
                        ..Default::default()
                    },
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
        let mut input = serde_json::json!({ "dynkey1": 5, "dynkey2": 9 });
        let store = get_test_store();
        let mut ctx = Context::new(&store, None);
        schema.coerce(&mut input, &mut ctx);
        schema.validate_value(&input, &mut ctx);
        assert!(ctx.violations.is_empty());
        assert_eq!(
            ctx.coercions,
            vec![Feedback {
                path: vec!["my_dynamic_keys".into()],
                issue: Issue::DefaultValueInserted()
            }]
        );
    }

    #[test]
    fn validate_dynamic_keys_from_defaults_err() {
        let schema = Dict {
            keys: Some(OrderMap::from_iter([(
                "my_dynamic_keys".into(),
                List {
                    items: Some(Box::new(Str::default().into())),
                    base: Base {
                        default: Some(vec!["dynkey1".into(), "dynkey2".into()]),
                        ..Default::default()
                    },
                    ..Default::default()
                }
                .into(),
            )])),
            dynamic_keys: Some(OrderMap::from_iter([(
                "my_dynamic_keys".into(),
                Dict {
                    keys: Some(OrderMap::from_iter([(
                        "sub_key".into(),
                        Int {
                            max: Some(10),
                            ..Default::default()
                        }
                        .into(),
                    )])),
                    ..Default::default()
                }
                .into(),
            )])),
            allow_other_keys: Some(true),
            ..Default::default()
        };
        let mut input =
            serde_json::json!({ "dynkey1": {"sub_key": 11, "bad_key": true}, "dynkey2": "wrong" });
        let store = get_test_store();
        let mut ctx = Context::new(&store, None);
        schema.coerce(&mut input, &mut ctx);
        schema.validate_value(&input, &mut ctx);
        assert_eq!(
            ctx.coercions,
            vec![Feedback {
                path: vec!["my_dynamic_keys".into()],
                issue: Issue::DefaultValueInserted()
            }]
        );
        assert_eq!(
            ctx.violations,
            vec![
                Feedback {
                    path: vec!["dynkey1".into(), "sub_key".into()],
                    issue: Violation::ValueAboveMaximum {
                        maximum: 10,
                        found: 11
                    }
                    .into()
                },
                Feedback {
                    path: vec!["dynkey1".into(), "bad_key".into()],
                    issue: Violation::UnexpectedKey {}.into()
                },
                Feedback {
                    path: vec!["dynkey2".into()],
                    issue: Violation::InvalidType {
                        expected: Type::Dict,
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
        let store = get_test_store();
        let mut ctx = Context::new(&store, None);
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
        let store = get_test_store();
        let mut ctx = Context::new(&store, None);
        schema.validate_value(&input, &mut ctx);
        assert!(ctx.coercions.is_empty());
        assert_eq!(
            ctx.violations,
            vec![Feedback {
                path: vec!["foo1".into()],
                issue: Violation::UnexpectedKey().into()
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
        let store = get_test_store();
        let mut ctx = Context::new(&store, None);
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
        let store = get_test_store();
        let mut ctx = Context::new(&store, None);
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

    #[test]
    fn validate_key_required_relaxed_root_dict_ok() {
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
        let mut input = serde_json::json!({});
        let store = get_test_store();
        let mut ctx = Context::new(
            &store,
            Some(&Configuration {
                ignore_required_keys_on_root_dict: true,
            }),
        );
        schema.coerce(&mut input, &mut ctx);
        schema.validate_value(&input, &mut ctx);
        assert!(ctx.violations.is_empty());
        assert!(ctx.coercions.is_empty());
    }

    #[test]
    fn validate_key_required_relaxed_root_dict_err() {
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
        let store = get_test_store();
        let mut ctx = Context::new(
            &store,
            Some(&Configuration {
                ignore_required_keys_on_root_dict: true,
            }),
        );
        // Using a deeper path and see that we still get the error even though we relax for the root dict.
        ctx.path.push("deeper".into());
        schema.validate_value(&input, &mut ctx);
        assert!(ctx.coercions.is_empty());
        assert_eq!(
            ctx.violations,
            vec![Feedback {
                path: vec!["deeper".into()],
                issue: Violation::MissingRequiredKey { key: "foo".into() }.into()
            }]
        )
    }
}
