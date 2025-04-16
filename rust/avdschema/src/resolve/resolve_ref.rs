// Copyright (c) 2025 Arista Networks, Inc.
// Use of this source code is governed by the Apache License 2.0
// that can be found in the LICENSE file.

use std::sync::LazyLock;

use crate::resolve::errors::{RefSyntax, SchemaResolverError};
use crate::{Store, any::AnySchema};
use regex::Regex;

use super::walker::Walker as _;

/// Regex matching $ref syntax according the AVD metaschema.
static REF_REGEX: LazyLock<Regex> =
    LazyLock::new(|| Regex::new("^([a-z][a-z_]*)#((/[a-z$][\\.a-z0-9_]*)*)$").unwrap());

/// Resolve the given ref by first finding the relevant schema in in the store
/// and afterwards walk that schema according to the path.
/// Returns the schema pointed to by the ref, or an error for invalid ref.
pub fn resolve_ref<'a>(ref_: &str, store: &'a Store) -> Result<&'a AnySchema, SchemaResolverError> {
    let captures = REF_REGEX.captures(ref_).ok_or(RefSyntax {
        schema_ref: ref_.to_owned(),
    })?;
    let schema_name = captures
        .get(1)
        .ok_or(RefSyntax {
            schema_ref: ref_.to_owned(),
        })?
        .as_str();
    let schema_path = captures
        .get(2)
        .ok_or(RefSyntax {
            schema_ref: ref_.to_owned(),
        })?
        .as_str();

    let path_iter = schema_path.split('/').skip(1).peekable();
    let schema = store.get(schema_name.try_into()?);
    Ok(schema.walk(path_iter)?)
}

#[cfg(test)]
mod tests {
    use crate::resolve::errors::SchemaResolverError;
    use crate::store::SchemaStoreError;
    use crate::str::Str;

    use crate::utils::test_utils::get_test_store;

    use super::resolve_ref;

    #[test]
    fn resolve_ref_ok() {
        let test_store = get_test_store();
        let result = resolve_ref("eos_cli_config_gen#/keys/key2", &test_store);
        assert!(result.is_ok());
        let result_schema = result.unwrap();
        let str_schema_result: Result<&Str, _> = result_schema.try_into();
        assert!(str_schema_result.is_ok());
        let str_schema = str_schema_result.unwrap();
        assert!(str_schema.base.description.is_some());
        assert_eq!(
            str_schema.base.description.as_ref().unwrap(),
            "this is from key2"
        );
    }

    #[test]
    fn resolve_ref_err_1() {
        let test_store = get_test_store();
        let ref_ = "#/keys/key2";
        let result = resolve_ref(ref_, &test_store);
        assert!(result.is_err());
        assert!(matches!(
            result.unwrap_err(),
            SchemaResolverError::RefSyntax(_)
        ))
    }

    #[test]
    fn resolve_ref_err_2() {
        let test_store = get_test_store();
        let ref_ = "eos_cli_config_gen";
        let result = resolve_ref(ref_, &test_store);
        assert!(result.is_err());
        assert!(matches!(
            result.unwrap_err(),
            SchemaResolverError::RefSyntax(_)
        ))
    }

    #[test]
    fn resolve_ref_err_3() {
        let test_store = get_test_store();
        let ref_ = "wrong_schema#/keys/key2";
        let result = resolve_ref(ref_, &test_store);
        assert!(result.is_err());
        assert!(matches!(
            result.unwrap_err(),
            SchemaResolverError::SchemaStoreError(SchemaStoreError::SchemaName(_))
        ))
    }
}
