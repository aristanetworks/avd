// Copyright (c) 2025 Arista Networks, Inc.
// Use of this source code is governed by the Apache License 2.0
// that can be found in the LICENSE file.
#![deny(unused_crate_dependencies)]

use std::path::PathBuf;

use avdschema::{Dump, LoadFromFragments as _, Store, any::AnySchema, resolve_schema};
use proc_macro::TokenStream;

const EOS_CLI_CONFIG_GEN_FRAGMENTS: &str = concat!(
    env!("CARGO_MANIFEST_DIR"),
    "/../../python-avd/pyavd/_eos_cli_config_gen/schema/schema_fragments/"
);

const EOS_DESIGNS_FRAGMENTS: &str = concat!(
    env!("CARGO_MANIFEST_DIR"),
    "/../../python-avd/pyavd/_eos_designs/schema/schema_fragments/"
);

const TMP_FILE_PATH_ELEMENTS: [&str; 3] = [env!("CARGO_MANIFEST_DIR"), "tmp", "store.gz"];

/// Returns a bytestream (&'static [u8; N]) of AVD schemas built from fragments during compilation.
///
/// Operations:
/// - Loads schemas from fragments
/// - Resolve all $ref
/// - Save in a temporary file
/// - Run include_bytes on the temporary file and return the output.
#[proc_macro]
pub fn include_avd_schemas(_input: TokenStream) -> TokenStream {
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

    let tmp_file = PathBuf::from_iter(TMP_FILE_PATH_ELEMENTS);
    store.to_file(Some(tmp_file.clone())).unwrap();
    format!("r\"{}\"", tmp_file.to_str().unwrap())
        .parse()
        .unwrap()
}
