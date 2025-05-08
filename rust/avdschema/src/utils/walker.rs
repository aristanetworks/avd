// Copyright (c) 2025 Arista Networks, Inc.
// Use of this source code is governed by the Apache License 2.0
// that can be found in the LICENSE file.

use ordermap::OrderMap;
use serde_json::Value;

pub trait Walker<'a> {
    fn walk<'s>(
        &'a self,
        path: impl Iterator<Item = &'s str> + Clone,
        trail: Option<&mut Vec<String>>,
    ) -> OrderMap<Vec<String>, &'a Self>;
}

impl<'a> Walker<'a> for Value {
    fn walk<'s>(
        &'a self,
        mut path: impl Iterator<Item = &'s str> + Clone,
        mut trail: Option<&mut Vec<String>>,
    ) -> OrderMap<Vec<String>, &'a Self> {
        if let Some(component) = path.next() {
            if let Some(trail) = &mut trail {
                trail.push(component.to_string());
            }
            match self {
                Value::Object(object) => object
                    .get(component)
                    .map(|value| value.walk(path, trail))
                    .unwrap_or_default(),
                Value::Array(array) => array
                    .iter()
                    .enumerate()
                    .filter_map(|(i, element)| element.get(component).map(|el| (i, el)))
                    .flat_map(|(i, value)| {
                        let mut forked_trail = trail.as_ref().map(|trail| {
                            let mut forked_trail = trail.to_vec();
                            forked_trail.push(i.to_string());
                            forked_trail
                        });
                        value.walk(path.clone(), forked_trail.as_mut())
                    })
                    .collect(),
                _ => Default::default(),
            }
        } else {
            OrderMap::from_iter([(trail.map(|t| t.to_owned()).unwrap_or_default(), self)])
        }
    }
}
