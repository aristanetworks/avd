// Copyright (c) 2025 Arista Networks, Inc.
// Use of this source code is governed by the Apache License 2.0
// that can be found in the LICENSE file.

// When running from Python we wish to cache Store inside Rust,
// to avoid sending the huge object back and forth.
// The store will be initialized automatically on the first validation.
//
// If the feature "include-schemas" is not enabled, the store must be initialized
// from YAML fragments at run-time with the `init_store_from_fragments(eos_cli_config_gen: str, eos_designs: str)` function.
//
// If the feature "include-schemas" is enabled, the store will be built from YAML fragments
// during compilation and included as a json string in the source code.

use std::{
    path::PathBuf,
    sync::{LazyLock, Mutex},
};

use avdschema::{Dump as _, LoadFromFragments, Store, any::AnySchema, dict::Dict, resolve_schema};
use pyo3::{
    Bound, PyResult,
    exceptions::PyRuntimeError,
    pyfunction, pymodule,
    types::{PyModule, PyModuleMethods as _},
    wrap_pyfunction,
};
use serde_json::Value;

use crate::{
    ValidateJson as _, coercion::Coercion, context::Context, validation::Validation,
    validation_result::ValidationResult,
};

static STORE: LazyLock<Mutex<Option<Store>>> =
    LazyLock::new(|| Mutex::new(Some(initialize_store())));

fn initialize_store() -> Store {
    // TODO: Add the macro to include the schema during compilation
    Store {
        eos_cli_config_gen: AnySchema::Dict(Dict::default()),
        eos_designs: AnySchema::Dict(Dict::default()),
    }
}

#[pymodule]
#[pyo3(name = "_validation")]
fn validation(module: &Bound<'_, PyModule>) -> PyResult<()> {
    module.add_function(wrap_pyfunction!(init_store_from_fragments, module)?)?;
    module.add_function(wrap_pyfunction!(validate_json, module)?)?;
    module.add_function(wrap_pyfunction!(validate_json_with_adhoc_schema, module)?)
}

#[pyfunction]
pub fn init_store_from_fragments(
    eos_cli_config_gen: PathBuf,
    eos_designs: PathBuf,
) -> PyResult<()> {
    let mut eos_cli_config_gen_schema =
        AnySchema::from_fragments(eos_cli_config_gen).map_err(|err| {
            pyo3::exceptions::PyRuntimeError::new_err(format!(
                "Error while reading the EosCliConfigGen schema fragments: {err}",
            ))
        })?;
    let mut eos_designs_schema = AnySchema::from_fragments(eos_designs).map_err(|err| {
        pyo3::exceptions::PyRuntimeError::new_err(format!(
            "Error while reading the EosDesigns schema fragments: {err}",
        ))
    })?;

    // First create the store without resolving schemas.
    let mut store = Store {
        eos_cli_config_gen: eos_cli_config_gen_schema.clone(),
        eos_designs: eos_designs_schema.clone(),
    };

    // Next resolve all $ref in each schema, updating the store as we go, to avoid re-resolving nested refs many times.
    let _ = resolve_schema(&mut eos_cli_config_gen_schema, &store);
    store.eos_cli_config_gen = eos_cli_config_gen_schema;
    let _ = resolve_schema(&mut eos_designs_schema, &store);
    store.eos_designs = eos_designs_schema;

    // Finally insert the resolved store into the Mutex.
    let mut store_option = STORE.lock().map_err(|err| {
        PyRuntimeError::new_err(format!(
            "Unable to lock the schema store for updating: {err}"
        ))
    })?;
    _ = store_option.replace(store);
    Ok(())
}

#[pyfunction]
pub fn validate_json(data_as_json: &str, schema_name: &str) -> PyResult<String> {
    let store_option = STORE.lock().map_err(|err| {
        PyRuntimeError::new_err(format!(
            "Unable to lock the schema store for updating: {err}"
        ))
    })?;
    let store = store_option.as_ref().ok_or_else(|| {
        PyRuntimeError::new_err("Schema store must be initialized before calling validation")
    })?;
    store
        .validate_json(data_as_json, schema_name)
        .map_err(|err| PyRuntimeError::new_err(format!("Invalid JSON in data: {err}")))?
        .to_json()
        .map_err(|err| {
            PyRuntimeError::new_err(format!(
                "Error occurred during dumping of validation results to JSON: {err}"
            ))
        })
}

#[pyfunction]
pub fn validate_json_with_adhoc_schema(
    data_as_json: &str,
    schema_as_json: &str,
) -> PyResult<String> {
    // Parse schema JSON
    let schema: AnySchema = serde_json::from_str(schema_as_json)
        .map_err(|err| PyRuntimeError::new_err(format!("Invalid JSON in adhoc schema: {err}")))?;
    // Parse data JSON
    let mut data: Value = serde_json::from_str(data_as_json)
        .map_err(|err| PyRuntimeError::new_err(format!("Invalid JSON in data: {err}")))?;

    let mut ctx = Context::new();
    schema.coerce(&mut data, &mut ctx);
    schema.validate_value(&data, &mut ctx);

    ValidationResult {
        violations: ctx.violations,
        coercions: ctx.coercions,
    }
    .to_json()
    .map_err(|err| {
        PyRuntimeError::new_err(format!(
            "Error occurred during dumping of validation results to JSON: {err}"
        ))
    })
}
