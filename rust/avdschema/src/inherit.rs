// Copyright (c) 2025 Arista Networks, Inc.
// Use of this source code is governed by the Apache License 2.0
// that can be found in the LICENSE file.

use crate::base::DataValue;
use crate::base::{
    Base, Deprecation, convert_types::ConvertTypes, documentation_options::DocumentationOptions,
    documentation_options::DocumentationOptionsDict, valid_values::ValidValues,
};
use crate::str::Format;
use crate::{any::AnySchema, boolean::Bool, dict::Dict, int::Int, list::List, str::Str};
use ordermap::OrderMap;
use serde_json::Value;

trait InheritableWithClone {}
impl InheritableWithClone for String {}
impl InheritableWithClone for bool {}
impl InheritableWithClone for i64 {}
impl InheritableWithClone for u64 {}
impl<T> InheritableWithClone for Vec<T> where T: Clone {}
impl InheritableWithClone for Deprecation {}
impl InheritableWithClone for DocumentationOptions {}
impl InheritableWithClone for DocumentationOptionsDict {}
impl InheritableWithClone for OrderMap<String, AnySchema> {}
impl InheritableWithClone for OrderMap<String, Value> {}
impl InheritableWithClone for Format {}
impl InheritableWithClone for Box<AnySchema> {}

pub trait Inherit {
    /// Inherit schema data from another schema.
    /// Used when resolving $ref by deep-inheriting the schema pointed to by the $ref.
    fn inherit(&mut self, other: &Self);
}
impl<T> Inherit for Option<T>
where
    T: InheritableWithClone + Clone,
{
    fn inherit(&mut self, other: &Self) {
        if self.is_none()
            && let Some(other_value) = other {
                self.replace(other_value.to_owned());
            }
    }
}
impl Inherit for OrderMap<String, AnySchema> {
    fn inherit(&mut self, other: &Self) {
        other.iter().for_each(|(key, other_value)| {
            self.entry(key.clone())
                .and_modify(|self_value| self_value.inherit(other_value))
                .or_insert(other_value.to_owned());
        });
    }
}
impl<T> Inherit for Base<T>
where
    T: InheritableWithClone + DataValue + Clone,
{
    fn inherit(&mut self, other: &Self) {
        self.default.inherit(&other.default);
        self.display_name.inherit(&other.display_name);
        self.description.inherit(&other.description);
        self.required.inherit(&other.required);
        self.deprecation.inherit(&other.deprecation);
        self.schema_ref.inherit(&other.schema_ref);
    }
}
impl Inherit for ConvertTypes {
    fn inherit(&mut self, other: &Self) {
        self.convert_types.inherit(&other.convert_types);
    }
}
impl<T> Inherit for ValidValues<T>
where
    T: InheritableWithClone + Clone,
{
    fn inherit(&mut self, other: &Self) {
        self.valid_values.inherit(&other.valid_values);
        self.dynamic_valid_values
            .inherit(&other.dynamic_valid_values);
    }
}
impl Inherit for Bool {
    fn inherit(&mut self, other: &Self) {
        self.base.inherit(&other.base);
        self.documentation_options
            .inherit(&other.documentation_options);
    }
}
impl Inherit for Dict {
    fn inherit(&mut self, other: &Self) {
        // Deep inherit each key in the maps (keys, dynamic_keys, defs) if it is set in both. Otherwise use regular option inheritance.
        if let (Some(keys), Some(other_keys)) = (self.keys.as_mut(), other.keys.as_ref()) {
            keys.inherit(other_keys);
        } else {
            self.keys.inherit(&other.keys);
        }
        if let (Some(dynamic_keys), Some(other_dynamic_keys)) =
            (self.dynamic_keys.as_mut(), other.dynamic_keys.as_ref())
        {
            dynamic_keys.inherit(other_dynamic_keys);
        } else {
            self.dynamic_keys.inherit(&other.dynamic_keys);
        }
        if let (Some(schema_defs), Some(other_schema_defs)) =
            (self.schema_defs.as_mut(), other.schema_defs.as_ref())
        {
            schema_defs.inherit(other_schema_defs);
        } else {
            self.schema_defs.inherit(&other.schema_defs);
        }
        self.allow_other_keys.inherit(&other.allow_other_keys);
        self.relaxed_validation.inherit(&other.relaxed_validation);
        self.schema_id.inherit(&other.schema_id);
        self.schema_schema.inherit(&other.schema_schema);
        self.base.inherit(&other.base);
        self.documentation_options
            .inherit(&other.documentation_options);
    }
}
impl Inherit for Int {
    fn inherit(&mut self, other: &Self) {
        self.min.inherit(&other.min);
        self.max.inherit(&other.max);
        self.base.inherit(&other.base);
        self.convert_types.inherit(&other.convert_types);
        self.valid_values.inherit(&other.valid_values);
        self.documentation_options
            .inherit(&other.documentation_options);
    }
}
impl Inherit for List {
    fn inherit(&mut self, other: &Self) {
        // Deep inherit "items" if it is set in both. Otherwise use regular option inheritance.
        if let (Some(items), Some(other_items)) = (self.items.as_deref_mut(), other.items.as_ref())
        {
            items.inherit(other_items);
        } else {
            self.items.inherit(&other.items);
        }
        self.min_length.inherit(&other.min_length);
        self.max_length.inherit(&other.max_length);
        self.primary_key.inherit(&other.primary_key);
        self.unique_keys.inherit(&other.unique_keys);
        self.allow_duplicate_primary_key
            .inherit(&other.allow_duplicate_primary_key);
        self.base.inherit(&other.base);
        self.documentation_options
            .inherit(&other.documentation_options);
    }
}
impl Inherit for Str {
    fn inherit(&mut self, other: &Self) {
        self.convert_to_lower_case
            .inherit(&other.convert_to_lower_case);
        self.format.inherit(&other.format);
        self.min_length.inherit(&other.min_length);
        self.max_length.inherit(&other.max_length);
        self.pattern.inherit(&other.pattern);
        self.base.inherit(&other.base);
        self.convert_types.inherit(&other.convert_types);
        self.valid_values.inherit(&other.valid_values);
        self.documentation_options
            .inherit(&other.documentation_options);
    }
}
impl Inherit for AnySchema {
    fn inherit(&mut self, other: &Self) {
        match (self, other) {
            (Self::Bool(schema), Self::Bool(other_schema)) => {
                schema.inherit(other_schema);
            }
            (Self::Dict(schema), Self::Dict(other_schema)) => {
                schema.inherit(other_schema);
            }
            (Self::Int(schema), Self::Int(other_schema)) => {
                schema.inherit(other_schema);
            }
            (Self::List(schema), Self::List(other_schema)) => {
                schema.inherit(other_schema);
            }
            (Self::Str(schema), Self::Str(other_schema)) => {
                schema.inherit(other_schema);
            }
            #[allow(
                clippy::panic,
                reason = "TODO: Refactor all inheritance to return Result."
            )]
            (_, _) => panic!("Unable to inherit from a different types of schemas."),
        }
    }
}

#[cfg(test)]
mod tests {
    use crate::{any::AnySchema, boolean::Bool, dict::Dict, int::Int, list::List, str::Str};

    use crate::utils::test_utils::{
        get_test_bool_schema, get_test_dict_schema, get_test_int_schema, get_test_list_schema,
        get_test_str_schema,
    };

    use super::Inherit;

    #[test]
    fn inherit_bool() {
        let mut schema_a = AnySchema::Bool(Bool::default());
        let schema_b = get_test_bool_schema();
        // Verify that the schemas are different
        assert_ne!(
            serde_json::to_string(&schema_a).unwrap(),
            serde_json::to_string(&schema_b).unwrap()
        );
        // Perform the inheritance
        schema_a.inherit(&schema_b);
        // Since we have no conflicts we can just check the the serialized versions of both schemas are the same
        assert_eq!(
            serde_json::to_string(&schema_a).unwrap(),
            serde_json::to_string(&schema_b).unwrap()
        );
    }

    #[test]
    fn inherit_int() {
        let mut schema_a = AnySchema::Int(Int::default());
        let schema_b = get_test_int_schema();
        // Verify that the schemas are different
        assert_ne!(
            serde_json::to_string(&schema_a).unwrap(),
            serde_json::to_string(&schema_b).unwrap()
        );
        // Perform the inheritance
        schema_a.inherit(&schema_b);
        // Since we have no conflicts we can just check the the serialized versions of both schemas are the same
        assert_eq!(
            serde_json::to_string(&schema_a).unwrap(),
            serde_json::to_string(&schema_b).unwrap()
        );
    }

    #[test]
    fn inherit_str() {
        let mut schema_a = AnySchema::Str(Str::default());
        let schema_b = get_test_str_schema();
        // Verify that the schemas are different
        assert_ne!(
            serde_json::to_string(&schema_a).unwrap(),
            serde_json::to_string(&schema_b).unwrap()
        );
        // Perform the inheritance
        schema_a.inherit(&schema_b);
        // Since we have no conflicts we can just check the the serialized versions of both schemas are the same
        assert_eq!(
            serde_json::to_string(&schema_a).unwrap(),
            serde_json::to_string(&schema_b).unwrap()
        );
    }

    #[test]
    fn inherit_list() {
        let mut schema_a = AnySchema::List(List::default());
        let schema_b = get_test_list_schema();
        // Verify that the schemas are different
        assert_ne!(
            serde_json::to_string(&schema_a).unwrap(),
            serde_json::to_string(&schema_b).unwrap()
        );
        // Perform the inheritance
        schema_a.inherit(&schema_b);
        // Since we have no conflicts we can just check the the serialized versions of both schemas are the same
        assert_eq!(
            serde_json::to_string(&schema_a).unwrap(),
            serde_json::to_string(&schema_b).unwrap()
        );
    }

    #[test]
    fn inherit_dict() {
        let mut schema_a = AnySchema::Dict(Dict::default());
        let schema_b = get_test_dict_schema();
        // Verify that the schemas are different
        assert_ne!(
            serde_json::to_string(&schema_a).unwrap(),
            serde_json::to_string(&schema_b).unwrap()
        );
        // Perform the inheritance
        schema_a.inherit(&schema_b);
        // Since we have no conflicts we can just check the the serialized versions of both schemas are the same
        assert_eq!(
            serde_json::to_string(&schema_a).unwrap(),
            serde_json::to_string(&schema_b).unwrap()
        );
    }
}
