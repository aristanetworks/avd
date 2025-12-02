// Copyright (c) 2025 Arista Networks, Inc.
// Use of this source code is governed by the Apache License 2.0
// that can be found in the LICENSE file.

use ordermap::OrderMap;
use serde_json::Value;

use crate::feedback::{Feedback, Type, Violation};

use crate::{context::Context, validation::Validation};
use avdschema::{Walker, any::AnySchema, list::List, resolve_ref};

impl Validation<Vec<Value>> for List {
    fn validate(&self, input: &Vec<Value>, ctx: &mut Context) {
        validate_min_length(self, input, ctx);
        validate_max_length(self, input, ctx);
        validate_items(self, input, ctx);
        validate_unique_keys(self, input, ctx);
    }

    fn validate_value(&self, value: &Value, ctx: &mut Context) {
        if let Some(v) = value.as_array() {
            self.validate(v, ctx)
        } else {
            ctx.add_violation(Violation::InvalidType {
                expected: Type::List,
                found: value.into(),
            })
        }
    }

    fn is_required(&self) -> bool {
        self.base.required.unwrap_or_default()
    }

    fn validate_ref(&self, value: &Vec<Value>, ctx: &mut Context) {
        if let Some(ref_) = self.base.schema_ref.as_ref() {
            // Ignoring not being able to resolve the schema.
            // Ignoring a wrong schema type at the ref. Since Validation is infallible.
            // TODO: What to do?
            if let Ok(AnySchema::List(ref_schema)) = resolve_ref(ref_, ctx.store) {
                ref_schema.validate(value, ctx);
            }
        }
    }

    fn default_value(&self) -> Option<Vec<Value>> {
        self.base.default.to_owned()
    }
}

fn validate_min_length(schema: &List, input: &[Value], ctx: &mut Context) {
    if let Some(min_length) = schema.min_length {
        let length = input.len() as u64;
        if min_length > length {
            ctx.add_violation(Violation::LengthBelowMinimum {
                minimum: min_length,
                found: length,
            });
        }
    }
}

fn validate_max_length(schema: &List, input: &[Value], ctx: &mut Context) {
    if let Some(max_length) = schema.max_length {
        let length = input.len() as u64;
        if max_length < length {
            ctx.add_violation(Violation::LengthAboveMaximum {
                maximum: max_length,
                found: length,
            });
        }
    }
}

fn validate_unique_keys(schema: &List, items: &[Value], ctx: &mut Context) {
    let unique_keys = schema.unique_keys.iter().flatten().chain(
        // the primary key is considered unique unless told otherwise
        schema
            .primary_key
            .as_ref()
            .filter(|_| !schema.allow_duplicate_primary_key.unwrap_or_default()),
    );

    for unique_key in unique_keys {
        let path = unique_key.split('.');
        let items = items
            .iter()
            .enumerate()
            .flat_map(|(i, item)| {
                let mut trail = vec![i.to_string()];
                item.walk(path.clone(), Some(&mut trail))
            })
            .collect::<OrderMap<_, _>>();

        for (current_trail, current_item) in &items {
            for (trail, item) in &items {
                if current_trail != trail && current_item == item {
                    ctx.violations.push(Feedback {
                        path: {
                            let mut path = ctx.path.clone();
                            path.extend_from_slice(current_trail);
                            path
                        },
                        issue: Violation::ValueNotUnique {
                            other_path: {
                                let mut path = ctx.path.clone();
                                path.extend_from_slice(trail);
                                path
                            },
                        }
                        .into(),
                    });
                }
            }
        }
    }
}

fn validate_items(schema: &List, items: &[Value], ctx: &mut Context) {
    for (i, item) in items.iter().enumerate() {
        ctx.path.push(i.to_string());
        validate_item_schema(schema, item, ctx);
        validate_item_primary_key(schema, item, ctx);
        ctx.path.pop();
    }
}

fn validate_item_schema(schema: &List, item: &Value, ctx: &mut Context) {
    if let Some(schema) = &schema.items {
        schema.validate_value(item, ctx);
    }
}

fn validate_item_primary_key(schema: &List, item: &Value, ctx: &mut Context) {
    if let Some(primary_key) = &schema.primary_key
        && item.get(primary_key).is_none_or(|value| value.is_null()) {
            ctx.add_violation(Violation::MissingRequiredKey {
                key: primary_key.to_owned(),
            });
        }
}

#[cfg(test)]
mod tests {
    use avdschema::{any::AnySchema, dict::Dict, str::Str};
    use ordermap::OrderMap;

    use super::*;
    use crate::{
        coercion::Coercion as _,
        feedback::{CoercionNote, Feedback},
        validation::test_utils::get_test_store,
    };

    #[test]
    fn validate_type_ok() {
        let schema = List::default();
        let input = serde_json::json!(["foo", "bar"]);
        let store = get_test_store();
        let mut ctx = Context::new(&store, None);
        schema.validate_value(&input, &mut ctx);
        assert!(ctx.violations.is_empty() && ctx.coercions.is_empty());
    }

    #[test]
    fn validate_type_err() {
        let schema = List::default();
        let input = true.into();
        let store = get_test_store();
        let mut ctx = Context::new(&store, None);
        schema.validate_value(&input, &mut ctx);
        assert!(ctx.coercions.is_empty());
        assert_eq!(
            ctx.violations,
            vec![Feedback {
                path: vec![],
                issue: Violation::InvalidType {
                    expected: Type::List,
                    found: Type::Bool
                }
                .into()
            }]
        );
    }

    #[test]
    fn validate_item_type_ok() {
        let schema = List {
            items: Some(AnySchema::Str(Str::default()).into()),
            ..Default::default()
        };
        let input = serde_json::json!(["foo", "bar"]);
        let store = get_test_store();
        let mut ctx = Context::new(&store, None);
        schema.validate_value(&input, &mut ctx);
        assert!(ctx.violations.is_empty() && ctx.coercions.is_empty());
    }

    #[test]
    fn validate_item_type_err() {
        let schema = List {
            items: Some(Box::new(Str::default().into())),
            ..Default::default()
        };
        let input = serde_json::json!([{}, {}]);
        let store = get_test_store();
        let mut ctx = Context::new(&store, None);
        schema.validate_value(&input, &mut ctx);
        assert!(ctx.coercions.is_empty());
        assert_eq!(
            ctx.violations,
            vec![
                Feedback {
                    path: vec!["0".into()],
                    issue: Violation::InvalidType {
                        expected: Type::Str,
                        found: Type::Dict
                    }
                    .into()
                },
                Feedback {
                    path: vec!["1".into()],
                    issue: Violation::InvalidType {
                        expected: Type::Str,
                        found: Type::Dict
                    }
                    .into()
                }
            ]
        );
    }

    #[test]
    fn validate_item_type_coercion_ok_err() {
        let schema = List {
            items: Some(Box::new(Str::default().into())),
            ..Default::default()
        };
        let mut input = serde_json::json!([1, []]);
        let store = get_test_store();
        let mut ctx = Context::new(&store, None);
        schema.coerce(&mut input, &mut ctx);
        schema.validate_value(&input, &mut ctx);
        assert_eq!(
            ctx.coercions,
            vec![Feedback {
                path: vec!["0".into()],
                issue: CoercionNote {
                    found: 1.into(),
                    made: "1".into()
                }
                .into()
            }]
        );
        assert_eq!(
            ctx.violations,
            vec![Feedback {
                path: vec!["1".into()],
                issue: Violation::InvalidType {
                    expected: Type::Str,
                    found: Type::List
                }
                .into()
            },]
        );
    }

    #[test]
    fn validate_min_length_ok() {
        let schema = List {
            min_length: Some(1),
            ..Default::default()
        };
        let input = serde_json::json!(["foo", "bar"]);
        let store = get_test_store();
        let mut ctx = Context::new(&store, None);
        schema.validate_value(&input, &mut ctx);
        assert!(ctx.violations.is_empty() && ctx.coercions.is_empty());
    }

    #[test]
    fn validate_min_length_err() {
        let schema = List {
            min_length: Some(3),
            ..Default::default()
        };
        let input = serde_json::json!(["foo", "bar"]);
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
        let schema = List {
            max_length: Some(2),
            ..Default::default()
        };
        let input = serde_json::json!(["foo", "bar"]);
        let store = get_test_store();
        let mut ctx = Context::new(&store, None);
        schema.validate_value(&input, &mut ctx);
        assert!(ctx.violations.is_empty() && ctx.coercions.is_empty());
    }

    #[test]
    fn validate_max_length_err() {
        let schema = List {
            max_length: Some(2),
            ..Default::default()
        };
        let input = serde_json::json!(["foo", "bar", "baz"]);
        let store = get_test_store();
        let mut ctx = Context::new(&store, None);
        schema.validate_value(&input, &mut ctx);
        assert!(ctx.coercions.is_empty());
        assert_eq!(
            ctx.violations,
            vec![Feedback {
                path: vec![],
                issue: Violation::LengthAboveMaximum {
                    maximum: 2,
                    found: 3
                }
                .into()
            }]
        );
    }

    #[test]
    fn validate_primary_key_ok() {
        let schema = List {
            items: Some(Box::new(
                Dict {
                    keys: Some(OrderMap::from_iter([("foo".into(), Str::default().into())])),
                    ..Default::default()
                }
                .into(),
            )),
            primary_key: Some("foo".into()),
            ..Default::default()
        };
        let input = serde_json::json!([{ "foo": "v1" }, { "foo": "v2" }]);
        let store = get_test_store();
        let mut ctx = Context::new(&store, None);
        schema.validate_value(&input, &mut ctx);
        assert!(ctx.violations.is_empty() && ctx.coercions.is_empty());
    }

    #[test]
    fn validate_primary_key_required_err() {
        let schema = List {
            items: Some(Box::new(
                Dict {
                    keys: Some(OrderMap::from_iter([("foo".into(), Str::default().into())])),
                    ..Default::default()
                }
                .into(),
            )),
            primary_key: Some("foo".into()),
            ..Default::default()
        };
        let input = serde_json::json!([{ "foo": null }, { "foo": "v1" }]);
        let store = get_test_store();
        let mut ctx = Context::new(&store, None);
        schema.validate_value(&input, &mut ctx);
        assert!(ctx.coercions.is_empty());
        assert_eq!(
            ctx.violations,
            vec![Feedback {
                path: vec!["0".into()],
                issue: Violation::MissingRequiredKey { key: "foo".into() }.into()
            }]
        );
    }

    #[test]
    fn validate_primary_key_not_unique_err() {
        let schema = List {
            items: Some(Box::new(
                Dict {
                    keys: Some(OrderMap::from_iter([("foo".into(), Str::default().into())])),
                    ..Default::default()
                }
                .into(),
            )),
            primary_key: Some("foo".into()),
            ..Default::default()
        };
        let input = serde_json::json!([{ "foo": "111" }, { "foo": "222" }, { "foo": "111" }]);
        let store = get_test_store();
        let mut ctx = Context::new(&store, None);
        schema.validate_value(&input, &mut ctx);
        assert!(ctx.coercions.is_empty());
        assert_eq!(
            ctx.violations,
            vec![
                Feedback {
                    path: vec!["0".into(), "foo".into()],
                    issue: Violation::ValueNotUnique {
                        other_path: vec!["2".into(), "foo".into()]
                    }
                    .into()
                },
                Feedback {
                    path: vec!["2".into(), "foo".into()],
                    issue: Violation::ValueNotUnique {
                        other_path: vec!["0".into(), "foo".into()]
                    }
                    .into()
                }
            ]
        );
    }

    #[test]
    fn validate_allow_duplicate_primary_key_ok() {
        let schema = List {
            items: Some(Box::new(
                Dict {
                    keys: Some(OrderMap::from_iter([("foo".into(), Str::default().into())])),
                    ..Default::default()
                }
                .into(),
            )),
            primary_key: Some("foo".into()),
            allow_duplicate_primary_key: Some(true),
            ..Default::default()
        };
        let input = serde_json::json!([{ "foo": "111" }, { "foo": "222" }, { "foo": "111" }]);
        let store = get_test_store();
        let mut ctx = Context::new(&store, None);
        schema.validate_value(&input, &mut ctx);
        assert!(ctx.coercions.is_empty());
        assert!(ctx.violations.is_empty());
    }
}
