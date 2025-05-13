// Copyright (c) 2025 Arista Networks, Inc.
// Use of this source code is governed by the Apache License 2.0
// that can be found in the LICENSE file.

pub mod errors;
pub mod resolve_ref;
mod walker;

use crate::{any::AnySchema, inherit::Inherit, store::Store};

use errors::{SchemaResolverError, SchemaType};
use resolve_ref::resolve_ref;

/// Inplace resolve all $ref in the provided AnySchema.
/// All $ref are are looked up in the provided Store.
pub fn resolve_schema<'a>(
    schema: &'a mut AnySchema,
    store: &'a Store,
) -> Result<(), SchemaResolverError> {
    schema.resolve(store)
}

/// Inplace resolve all $ref in Self.
/// All $ref are are looked up in the provided Store.
trait Resolve {
    fn resolve(&mut self, store: &Store) -> Result<(), SchemaResolverError>
    where
        Self: Inherit;
    fn ref_(&self) -> Option<String>;
    fn unset_ref(&mut self);
}
impl Resolve for AnySchema {
    fn resolve(&mut self, store: &Store) -> Result<(), SchemaResolverError>
    where
        Self: Inherit,
    {
        // First resolve any child schemas to avoid anything inherited from overriding the main schema.
        // Only relevant for lists and dicts.
        if let Self::List(schema) = self {
            // resolve items
            if let Some(items) = schema.items.as_mut() {
                items.resolve(store)?;
            }
        } else if let Self::Dict(schema) = self {
            // resolve keys, dynamic_keys and defs
            if let Some(keys) = schema.keys.as_mut() {
                for (_, value) in keys {
                    value.resolve(store)?;
                }
            }
            if let Some(dynamic_keys) = schema.dynamic_keys.as_mut() {
                for (_, value) in dynamic_keys {
                    value.resolve(store)?;
                }
            }
            if let Some(schema_defs) = schema.schema_defs.as_mut() {
                for (_, value) in schema_defs {
                    value.resolve(store)?;
                }
            }
        }
        // Skip resolving references to a full schema. These will be handled during validation.
        if self.ref_().is_some_and(|ref_| ref_.ends_with("#")) {
            return Ok(());
        }

        // Next resolve the main schema itself
        while let Some(ref ref_) = self.ref_() {
            // The clone here is required since we might be inheriting parts of this schema in other places, and thereby modify the schemas.
            let mut ref_schema = resolve_ref(ref_, store)?.clone();
            ref_schema.resolve(store)?;
            if !is_same_schema(self, &ref_schema) {
                return Err(SchemaType {
                    schema_ref: ref_.to_owned(),
                    expected: self.into(),
                    found: (&ref_schema).into(),
                }
                .into());
            }
            self.unset_ref();
            self.inherit(&ref_schema);
            // After inheriting the ref schema we might have inherited another ref, so going back to the while loop.
        }
        Ok(())
    }
    fn ref_(&self) -> Option<String> {
        match self {
            Self::Bool(schema) => schema.base.schema_ref.to_owned(),
            Self::Dict(schema) => schema.base.schema_ref.to_owned(),
            Self::Int(schema) => schema.base.schema_ref.to_owned(),
            Self::List(schema) => schema.base.schema_ref.to_owned(),
            Self::Str(schema) => schema.base.schema_ref.to_owned(),
        }
    }
    fn unset_ref(&mut self) {
        match self {
            Self::Bool(schema) => schema.base.schema_ref = None,
            Self::Dict(schema) => schema.base.schema_ref = None,
            Self::Int(schema) => schema.base.schema_ref = None,
            Self::List(schema) => schema.base.schema_ref = None,
            Self::Str(schema) => schema.base.schema_ref = None,
        }
    }
}

/// Returns bool indicating if the two given schemas are of the same type.
fn is_same_schema(a: &AnySchema, b: &AnySchema) -> bool {
    matches!(
        (a, b),
        (AnySchema::Bool(_), AnySchema::Bool(_))
            | (AnySchema::Dict(_), AnySchema::Dict(_))
            | (AnySchema::Int(_), AnySchema::Int(_))
            | (AnySchema::List(_), AnySchema::List(_))
            | (AnySchema::Str(_), AnySchema::Str(_))
    )
}

#[cfg(test)]
mod tests {
    use crate::utils::test_utils::{get_test_dict_schema_with_refs, get_test_store};
    use crate::{dict::Dict, str::Str};

    use super::Resolve;

    #[test]
    fn resolve_ok() {
        let mut schema = get_test_dict_schema_with_refs();
        let store = get_test_store();
        let result = schema.resolve(&store);
        assert!(result.is_ok());
        let dict_schema: &Dict = (&schema).try_into().unwrap();
        let keys = dict_schema.keys.as_ref().unwrap();
        let single_ref: &Str = keys.get("single_ref").unwrap().try_into().unwrap();
        assert_eq!(
            single_ref.base.description,
            Some("this is from key2".into())
        );
        let nested_ref: &Str = keys.get("nested_ref").unwrap().try_into().unwrap();
        assert_eq!(
            nested_ref.base.description,
            Some("this is from key2".into())
        );
        let cross_schema_ref: &Str = keys.get("cross_schema_ref").unwrap().try_into().unwrap();
        assert_eq!(
            cross_schema_ref.base.description,
            Some("this is from key2".into())
        );
    }
}
