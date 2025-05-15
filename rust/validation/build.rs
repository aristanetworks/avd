// Copyright (c) 2025 Arista Networks, Inc.
// Use of this source code is governed by the Apache License 2.0
// that can be found in the LICENSE file.

use pyo3_build_config;
use std::env;

fn main() {
    println!("cargo:rerun-if-changed=build.rs");
    println!("cargo:rerun-if-env-changed=CARGO_CFG_FEATURE");
    println!("cargo:rerun-if-env-changed=CARGO_CFG_TARGET_OS");
    let features = env::var_os("CARGO_CFG_FEATURE");

    if let Some(features_string_ref) = features.as_ref().and_then(|os_str| os_str.to_str()) {
        let enabled_features: Vec<&str> = features_string_ref.split(',').collect();

        if enabled_features.contains(&"python_bindings") {
            if env::var("CARGO_CFG_TARGET_OS") == Ok("macos".to_string()) {
                println!("cargo:warning=Compiling using feature 'python_bindings' on 'macos'");
                // Needed for MacOS when using pyo3 extension-module
                pyo3_build_config::add_extension_module_link_args();
            }
        } else {
            println!("cargo:warning=INACTIVE");
        }
    }
}
