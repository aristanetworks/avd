// Copyright (c) 2025 Arista Networks, Inc.
// Use of this source code is governed by the Apache License 2.0
// that can be found in the LICENSE file.

use std::env;

fn main() {
    println!("cargo:rerun-if-changed=build.rs");
    println!("cargo:rerun-if-env-changed=CARGO_CFG_TARGET_OS");

    if let Ok(current_target_os) = env::var("CARGO_CFG_TARGET_OS")
        && current_target_os == "macos" {
            println!("cargo:warning=Compiling on 'macos'");
            // Needed for MacOS when using pyo3 extension-module
            pyo3_build_config::add_extension_module_link_args();
        }
}
