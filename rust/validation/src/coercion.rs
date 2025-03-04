// Copyright (c) 2025 Arista Networks, Inc.
// Use of this source code is governed by the Apache License 2.0
// that can be found in the LICENSE file.

use avdschema::{any::AnySchema, boolean::Bool, dict::Dict, int::Int, list::List, str::Str};
use serde_json::{Map, Value};

use crate::{context::Context, feedback::CoercionNote, utils::dynamic_keys::get_dynamic_keys};

pub(crate) trait Coercion<T>
where
    for<'x> &'x Self: TryFrom<&'x AnySchema>,
{
    fn coerce(&self, input: &mut Value, ctx: &mut Context);
}
impl Coercion<bool> for Bool {
    fn coerce(&self, _input: &mut Value, _ctx: &mut Context) {}
}
impl Coercion<Map<String, Value>> for Dict {
    fn coerce(&self, input: &mut Value, ctx: &mut Context) {
        if let Value::Object(dict) = input {
            if let Some(keys) = &self.keys {
                for (key, key_schema) in keys {
                    if let Some(value) = dict.get_mut(key) {
                        ctx.path.push(key.to_owned());
                        key_schema.coerce(value, ctx);
                        ctx.path.pop();
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

impl Coercion<i64> for Int {
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
impl Coercion<Vec<Value>> for List {
    fn coerce(&self, input: &mut Value, ctx: &mut Context) {
        if let Some(item_schema) = &self.items {
            if let Value::Array(list) = input {
                for (i, item) in list.iter_mut().enumerate() {
                    ctx.path.push(i.to_string());
                    item_schema.coerce(item, ctx);
                    ctx.path.pop();
                }
            }
        }
    }
}
impl Coercion<String> for Str {
    fn coerce(&self, input: &mut Value, ctx: &mut Context) {
        let value = match input {
            Value::String(string) => Some(string.to_string()),
            Value::Number(number) => {
                ctx.add_coercion(CoercionNote {
                    found: number.clone().into(),
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
impl Coercion<Value> for AnySchema {
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
