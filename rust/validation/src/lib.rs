// Copyright (c) 2025 Arista Networks, Inc.
// Use of this source code is governed by the Apache License 2.0
// that can be found in the LICENSE file.
#![deny(unused_crate_dependencies)]

mod coercion;
mod context;
pub mod feedback;
mod validation;

pub use self::coercion::Coercion;
pub use self::context::{Configuration, Context, ValidationResult};
pub use self::validation::Validation;
pub use self::validation::store::StoreValidate;
