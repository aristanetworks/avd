// Copyright (c) 2025 Arista Networks, Inc.
// Use of this source code is governed by the Apache License 2.0
// that can be found in the LICENSE file.

use crate::feedback::{CoercionNote, Feedback, Issue};

#[derive(Debug)]
pub(crate) struct Context {
    pub(crate) path: Vec<String>,
    pub(crate) violations: Vec<Feedback>,
    pub(crate) coercions: Vec<Feedback>,
}

impl Context {
    pub(crate) fn new() -> Self {
        Self {
            path: vec![],
            violations: vec![],
            coercions: vec![],
        }
    }

    pub(crate) fn add_violation(&mut self, violation: impl Into<Issue>) {
        self.violations.push(Feedback {
            path: self.path.clone(),
            issue: violation.into(),
        });
    }

    pub(crate) fn add_coercion(&mut self, coercion: impl Into<CoercionNote>) {
        self.coercions.push(Feedback {
            path: self.path.clone(),
            issue: coercion.into().into(),
        });
    }
}
