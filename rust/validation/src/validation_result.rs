// Copyright (c) 2025 Arista Networks, Inc.
// Use of this source code is governed by the Apache License 2.0
// that can be found in the LICENSE file.

use avdschema::Dump;
use serde::Serialize;

use crate::{context::Context, feedback::Feedback};

/// Result of coercion and/or validation.
/// Holds multiple Feedback objects pointing to each Issue.
#[derive(Clone, Debug, Serialize)]
pub struct ValidationResult {
    pub violations: Vec<Feedback>,
    pub coercions: Vec<Feedback>,
}
impl From<Context<'_>> for ValidationResult {
    fn from(value: Context) -> Self {
        Self {
            coercions: value.coercions,
            violations: value.violations,
        }
    }
}
impl Dump for ValidationResult {}
