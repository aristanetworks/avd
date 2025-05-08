// Copyright (c) 2025 Arista Networks, Inc.
// Use of this source code is governed by the Apache License 2.0
// that can be found in the LICENSE file.

use avdschema::{Store, any::AnySchema};
use serde::Deserialize as _;
use serde_json::json;

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
                    }
                }
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
