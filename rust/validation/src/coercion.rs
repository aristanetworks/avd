// Copyright (c) 2025 Arista Networks, Inc.
// Use of this source code is governed by the Apache License 2.0
// that can be found in the LICENSE file.

use avdschema::{
    any::{AnySchema, Shortcuts as _}, boolean::Bool, dict::{Dict}, int::Int, list::List, str::Str,
};
use serde_json::Value;

use crate::{
    context::Context,
    feedback::{CoercionNote},
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
                    // Skip removed keys
                    if let Some(deprecation) = key_schema.deprecation()
                        && deprecation.removed.unwrap_or_default()
                    {
                        continue;
                    }
                    if let Some(value) = dict.get_mut(key) {
                        ctx.state.path.push(key.to_owned());
                        key_schema.coerce(value, ctx);
                        ctx.state.path.pop();
                    }
                }
            }
            if let Some(dynamic_keys) = self.get_dynamic_keys(dict) {
                for (key, dynamic_key_info) in dynamic_keys.iter() {
                    if let Some(value) = dict.get_mut(key) {
                        ctx.state.path.push(key.to_owned());
                        dynamic_key_info.schema.coerce(value, ctx);
                        ctx.state.path.pop();
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
                        if ctx.configuration.return_coercion_infos {
                            ctx.add_info(CoercionNote {
                                found: float.into(),
                                made: (float as i64).into(),
                            });
                        }
                        Some(float as i64)
                    }
                    _ => None,
                },
            },
            Value::Bool(boolean) => {
                let value: i64 = (*boolean).into();
                if ctx.configuration.return_coercion_infos {
                    ctx.add_info(CoercionNote {
                        found: (*boolean).into(),
                        made: value.into(),
                    });
                }
                Some(value)
            }
            Value::String(string) => string
                .parse()
                .inspect(|value: &i64| {
                    if ctx.configuration.return_coercion_infos {
                        ctx.add_info(CoercionNote {
                            found: string.clone().into(),
                            made: (*value).into(),
                        });
                    }
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
            && let Value::Array(list) = input
        {
            for (i, item) in list.iter_mut().enumerate() {
                ctx.state.path.push(i.to_string());
                item_schema.coerce(item, ctx);
                ctx.state.path.pop();
            }
        }
    }
}
impl Coercion for Str {
    fn coerce(&self, input: &mut Value, ctx: &mut Context) {
        let value = match input {
            Value::String(string) => Some(string.to_string()),
            Value::Number(number) => {
                if ctx.configuration.return_coercion_infos {
                    ctx.add_info(CoercionNote {
                        found: Value::Number(number.clone()).into(),
                        made: number.to_string().into(),
                    });
                }
                Some(number.to_string())
            }
            Value::Bool(boolean) => {
                // Using Title case to match Python behavior.
                let string: String = match boolean {
                    true => "True".into(),
                    false => "False".into(),
                };
                if ctx.configuration.return_coercion_infos {
                    ctx.add_info(CoercionNote {
                        found: boolean.to_owned().into(),
                        made: string.to_owned().into(),
                    });
                }
                Some(string)
            }
            _ => None,
        }
        .map(|string| {
            if self.convert_to_lower_case.unwrap_or_default() {
                let lower_case_string = string.to_lowercase();
                if lower_case_string != string {
                    if ctx.configuration.return_coercion_infos {
                        ctx.add_info(CoercionNote {
                            found: string.into(),
                            made: lower_case_string.to_owned().into(),
                        });
                    }
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
