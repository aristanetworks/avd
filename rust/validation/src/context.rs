// Copyright (c) 2025 Arista Networks, Inc.
// Use of this source code is governed by the Apache License 2.0
// that can be found in the LICENSE file.

use avdschema::Store;

use crate::feedback::{Feedback, Issue};

/// The Context object is passed along during coercion and validation.
/// All coercions and violations will be registered in the context with the path carried in the context.
/// The store is used for looking up schema references.
#[derive(Debug)]
pub(crate) struct Context<'a> {
    pub(crate) store: &'a Store,
    pub(crate) path: Vec<String>,
    pub(crate) violations: Vec<Feedback>,
    pub(crate) coercions: Vec<Feedback>,
}

impl<'a> Context<'a> {
    pub(crate) fn new(store: &'a Store) -> Self {
        Self {
            store,
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

    pub(crate) fn add_coercion(&mut self, coercion: impl Into<Issue>) {
        self.coercions.push(Feedback {
            path: self.path.clone(),
            issue: coercion.into(),
        });
    }
}
