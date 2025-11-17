// Copyright (c) 2025 Arista Networks, Inc.
// Use of this source code is governed by the Apache License 2.0
// that can be found in the LICENSE file.

use avdschema::{
    any::AnySchema, boolean::Bool, dict::Dict, get_dynamic_keys, int::Int, list::List, str::Str,
};
use serde_json::Value;

use crate::{
    context::Context,
    feedback::{CoercionNote, Issue},
    validation::Validation,
};

pub trait Coercion
where
    for<'x> &'x Self: TryFrom<&'x AnySchema>,
{
    /// Recursively coerce the given value into the type specified by the schema.
    /// Also insert default values since dynamic keys and dynamic values may rely on these.
    ///
    /// Coercion is called before validation, to allow a more "loose" validation of types.
    /// This is especially useful when the input is coming from YAML where all types are inferred from strings.
    ///
    ///  TODO: Decide whether we should limit this to only coerce according to `convert_types`.
    fn coerce(&self, input: &mut Value, ctx: &mut Context);
}
impl Coercion for Bool {
    fn coerce(&self, _input: &mut Value, _ctx: &mut Context) {}
}
impl Coercion for Dict {
    fn coerce(&self, input: &mut Value, ctx: &mut Context) {
        if let Value::Object(dict) = input {
            if let Some(keys) = &self.keys {
                for (key, key_schema) in keys {
                    match dict.get_mut(key) {
                        Some(value) => {
                            ctx.path.push(key.to_owned());
                            key_schema.coerce(value, ctx);
                            ctx.path.pop();
                        }
                        // Insert default value since dynamic keys and dynamic values may rely on these.
                        None => {
                            if let Some(default_value) = key_schema.default_value() {
                                dict.insert(key.to_owned(), default_value);
                                ctx.path.push(key.to_owned());
                                ctx.add_coercion(Issue::DefaultValueInserted());
                                ctx.path.pop();
                            }
                        }
                    }
                }
            }
            if let Some(dynamic_keys) = &self.dynamic_keys {
                for (key_path, key_schema) in dynamic_keys {
                    let keys = get_dynamic_keys(key_path, dict);
                    // validate the computed dynamic keys' corresponding values
                    for key in keys {
                        if let Some(value) = dict.get_mut(&key) {
                            ctx.path.push(key);
                            key_schema.coerce(value, ctx);
                            ctx.path.pop();
                        }
                    }
                }
            }
        }
    }
}

impl Coercion for Int {
    fn coerce(&self, input: &mut Value, ctx: &mut Context) {
        let value = match input {
            Value::Number(number) => match number.as_i64() {
                Some(integer) => Some(integer),
                None => match number.as_f64() {
                    Some(float) if float.fract() == 0.0 => {
                        ctx.add_coercion(CoercionNote {
                            found: float.into(),
                            made: (float as i64).into(),
                        });
                        Some(float as i64)
                    }
                    _ => None,
                },
            },
            Value::Bool(boolean) => {
                let value: i64 = (*boolean).into();
                ctx.add_coercion(CoercionNote {
                    found: (*boolean).into(),
                    made: value.into(),
                });
                Some(value)
            }
            Value::String(string) => string
                .parse()
                .inspect(|value: &i64| {
                    ctx.add_coercion(CoercionNote {
                        found: string.clone().into(),
                        made: (*value).into(),
                    });
                })
                .ok(),
            _ => None,
        };

        if let Some(value) = value {
            _ = core::mem::replace(input, value.into());
        }
    }
}
impl Coercion for List {
    fn coerce(&self, input: &mut Value, ctx: &mut Context) {
        if let Some(item_schema) = &self.items
            && let Value::Array(list) = input {
                for (i, item) in list.iter_mut().enumerate() {
                    ctx.path.push(i.to_string());
                    item_schema.coerce(item, ctx);
                    ctx.path.pop();
                }
            }
    }
}
impl Coercion for Str {
    fn coerce(&self, input: &mut Value, ctx: &mut Context) {
        let value = match input {
            Value::String(string) => Some(string.to_string()),
            Value::Number(number) => {
                ctx.add_coercion(CoercionNote {
                    found: Value::Number(number.clone()).into(),
                    made: number.to_string().into(),
                });
                Some(number.to_string())
            }
            Value::Bool(boolean) => {
                // Using Title case to match Python behavior.
                let string: String = match boolean {
                    true => "True".into(),
                    false => "False".into(),
                };
                ctx.add_coercion(CoercionNote {
                    found: boolean.to_owned().into(),
                    made: string.to_owned().into(),
                });
                Some(string)
            }
            _ => None,
        }
        .map(|string| {
            if self.convert_to_lower_case.unwrap_or_default() {
                let lower_case_string = string.to_lowercase();
                if lower_case_string != string {
                    ctx.add_coercion(CoercionNote {
                        found: string.into(),
                        made: lower_case_string.to_owned().into(),
                    });
                    lower_case_string
                } else {
                    string
                }
            } else {
                string
            }
        });

        if let Some(value) = value.as_deref() {
            _ = core::mem::replace(input, value.into());
        }
    }
}
impl Coercion for AnySchema {
    fn coerce(&self, input: &mut Value, ctx: &mut Context) {
        match self {
            Self::Bool(schema) => schema.coerce(input, ctx),
            Self::Int(schema) => schema.coerce(input, ctx),
            Self::Str(schema) => schema.coerce(input, ctx),
            Self::List(schema) => schema.coerce(input, ctx),
            Self::Dict(schema) => schema.coerce(input, ctx),
        }
    }
}

#[cfg(test)]
mod tests {
    use serde_json::json;

    use avdschema::base::Base;
    use avdschema::list::List;
    use avdschema::str::Str;
    use ordermap::OrderMap;

    use super::*;

    use crate::context::Context;
    use crate::feedback::Feedback;
    use crate::validation::test_utils::get_test_store;

    #[test]
    fn validate_insertion_of_default_value() {
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
            ..Default::default()
        };
        let mut input = json!({});
        let store = get_test_store();
        let mut ctx = Context::new(&store, None);
        schema.coerce(&mut input, &mut ctx);
        assert!(ctx.violations.is_empty());
        assert_eq!(
            ctx.coercions,
            vec![Feedback {
                path: vec!["my_dynamic_keys".into()],
                issue: Issue::DefaultValueInserted()
            }]
        );
        assert_eq!(input, json!({"my_dynamic_keys": ["dynkey1", "dynkey2"]}));
    }
}
