// Copyright (c) 2025 Arista Networks, Inc.
// Use of this source code is governed by the Apache License 2.0
// that can be found in the LICENSE file.

use std::{path::PathBuf, sync::OnceLock};

use crate::{LoadFromFragments as _, Store, any::AnySchema, resolve_schema};
use serde::Deserialize as _;
use serde_json::json;

// Using a tmp path in the crate allows us to inspect the generated artifacts.
// The files in the path are exempted from git.
const TMP_PATH: &str = concat!(env!("CARGO_MANIFEST_DIR"), "/tmp");

pub(crate) const EOS_CLI_CONFIG_GEN_FRAGMENTS: &str = concat!(
    env!("CARGO_MANIFEST_DIR"),
    "/../../python-avd/pyavd/_eos_cli_config_gen/schema/schema_fragments/"
);

pub(crate) const EOS_DESIGNS_FRAGMENTS: &str = concat!(
    env!("CARGO_MANIFEST_DIR"),
    "/../../python-avd/pyavd/_eos_designs/schema/schema_fragments/"
);

pub(crate) fn get_tmp_path() -> PathBuf {
    PathBuf::from(TMP_PATH)
}
pub(crate) fn get_tmp_file(filename: &str) -> PathBuf {
    get_tmp_path().join(filename)
}

pub(crate) fn get_test_store() -> Store {
    Store {
        eos_cli_config_gen: AnySchema::deserialize(json!(
            {
                "type": "dict",
                "keys": {
                    "key1": {
                        "type": "str",
                        "$ref": "eos_cli_config_gen#/keys/key2",
                    },
                    "key2": {
                        "type": "str",
                        "description": "this is from key2",
                    },
                },
                "dynamic_keys": {
                    "dynamic.key": {
                        "type": "int",
                        "max": 10,
                    },
                },
            }
        ))
        .unwrap(),
        eos_designs: AnySchema::deserialize(json!(
            {
                "type": "dict",
                "keys": {
                    "key3": {
                        "type": "str",
                        "$ref": "eos_cli_config_gen#/keys/key2",
                    }
                }
            }
        ))
        .unwrap(),
    }
}

pub(crate) fn get_test_dict_schema_with_refs() -> AnySchema {
    AnySchema::deserialize(json!(
        {
            "type": "dict",
            "keys": {
                "single_ref": {
                    "type": "str",
                    "$ref": "eos_cli_config_gen#/keys/key2"
                },
                "nested_ref": {
                    "type": "str",
                    "$ref": "eos_cli_config_gen#/keys/key1"
                },
                "cross_schema_ref": {
                    "type": "str",
                    "$ref": "eos_designs#/keys/key3"
                },
            }
        }
    ))
    .unwrap()
}

pub(crate) fn get_test_bool_schema() -> AnySchema {
    AnySchema::deserialize(json!(
        {
            "type": "bool",
            "display_name": "bool",
            "description": "test_bool_schema",
            "required": true,
            "default": false,
            "deprecation": {
                "warning": true,
                "new_key": "new_bool",
                "remove_in_version": "10.0.0",
                "remove_after_date": "soon",
                "url": "somewhere",
                "removed": false,
            },
            "documentation_options": {"table": "test"},
            "$ref": "eos_cli_config_gen#/keys/somewhere",
        }
    ))
    .unwrap()
}

pub(crate) fn get_test_int_schema() -> AnySchema {
    AnySchema::deserialize(json!(
        {
            "type": "int",
            "display_name": "int",
            "description": "test_bool_schema",
            "required": true,
            "valid_values": [1,2],
            "default": 2,
            "min": 1,
            "max": 2,
            "convert_types": ["str"],
            "deprecation": {
                "warning": true,
                "new_key": "new_bool",
                "remove_in_version": "10.0.0",
                "remove_after_date": "soon",
                "url": "somewhere",
                "removed": false,
            },
            "documentation_options": {"table": "test"},
            "$ref": "eos_cli_config_gen#/keys/somewhere",
        }
    ))
    .unwrap()
}

pub(crate) fn get_test_str_schema() -> AnySchema {
    AnySchema::deserialize(json!(
        {
            "type": "str",
            "display_name": "str",
            "description": "test_bool_schema",
            "required": true,
            "valid_values": ["foo", "bar"],
            "default": "bar",
            "min_length": 3,
            "max_length": 3,
            "convert_types": ["int"],
            "convert_to_lower_case": true,
            "format": "mac",
            "pattern": "(foo|bar)",
            "deprecation": {
                "warning": true,
                "new_key": "new_bool",
                "remove_in_version": "10.0.0",
                "remove_after_date": "soon",
                "url": "somewhere",
                "removed": false,
            },
            "documentation_options": {"table": "test"},
            "$ref": "eos_cli_config_gen#/keys/somewhere",
        }
    ))
    .unwrap()
}

pub(crate) fn get_test_list_schema() -> AnySchema {
    AnySchema::deserialize(json!(
        {
            "type": "list",
            "display_name": "list",
            "description": "test_bool_schema",
            "required": true,
            "default": [{"primary": 1}],
            "min_length": 3,
            "max_length": 10,
            "primary_key": "primary",
            "allow_duplicate_primary_key": true,
            "unique_keys": ["secondary"],
            "items": {
                "type": "dict",
                "keys": {
                    "primary": {"type": "int"},
                    "secondary": {"type": "str"}
                }
            },
            "deprecation": {
                "warning": true,
                "new_key": "new_bool",
                "remove_in_version": "10.0.0",
                "remove_after_date": "soon",
                "url": "somewhere",
                "removed": false
            },
            "documentation_options": {"table": "test"},
            "$ref": "eos_cli_config_gen#/keys/somewhere",
        }
    ))
    .unwrap()
}

pub(crate) fn get_test_dict_schema() -> AnySchema {
    AnySchema::deserialize(json!(
        {
            "type": "dict",
            "display_name": "list",
            "description": "test_bool_schema",
            "required": true,
            "default": {"bool_key": false},
            "allow_other_keys": false,
            "relaxed_validation": true,
            "$id": "foo",
            "$schema": "myschema",
            "keys": {
                "bool_key": {"type": "bool"},
                "int_key": {"type": "int"},
                "str_key": {"type": "str"},
                "list_key": {"type": "list", "items": {"type": "int"}},
                "dict_key": {"type": "dict", "keys": {"nested_key": {"type": "str"}}}
            },
            "dynamic_keys": {"some_path": {"type": "int"}},
            "$defs": {"def_schema": {"type": "str"}},
            "deprecation": {
                "warning": true,
                "new_key": "new_bool",
                "remove_in_version": "10.0.0",
                "remove_after_date": "soon",
                "url": "somewhere",
                "removed": false
            },
            "documentation_options": {"table": "test"},
            "$ref": "eos_cli_config_gen#/keys/somewhere",
        }
    ))
    .unwrap()
}

static AVD_STORE: OnceLock<Store> = OnceLock::new();

fn init_avd_store() -> Store {
    // Load schemas from fragments, resolve all $ref and save in a store we can compare the loaded store with.
    let mut eos_cli_config_gen_schema =
        AnySchema::from_fragments(EOS_CLI_CONFIG_GEN_FRAGMENTS.into()).unwrap();
    let mut eos_designs_schema = AnySchema::from_fragments(EOS_DESIGNS_FRAGMENTS.into()).unwrap();
    let mut store = Store {
        eos_cli_config_gen: eos_cli_config_gen_schema.to_owned(),
        eos_designs: eos_designs_schema.to_owned(),
    };
    resolve_schema(&mut eos_cli_config_gen_schema, &store).unwrap();
    store.eos_cli_config_gen = eos_cli_config_gen_schema;
    resolve_schema(&mut eos_designs_schema, &store).unwrap();
    store.eos_designs = eos_designs_schema;
    store
}

pub(crate) fn get_avd_store() -> &'static Store {
    AVD_STORE.get_or_init(init_avd_store)
}
