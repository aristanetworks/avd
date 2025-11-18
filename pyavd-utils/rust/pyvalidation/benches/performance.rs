// Copyright (c) 2025 Arista Networks, Inc.
// Use of this source code is governed by the Apache License 2.0
// that can be found in the LICENSE file.

use criterion::{Criterion, criterion_group, criterion_main};
use pyvalidation::validation::{get_validated_data, init_store_from_fragments};

const EOS_CLI_CONFIG_GEN_FRAGMENTS: &str = concat!(
    env!("CARGO_MANIFEST_DIR"),
    "/../../../python-avd/pyavd/_eos_cli_config_gen/schema/schema_fragments/"
);

const EOS_DESIGNS_FRAGMENTS: &str = concat!(
    env!("CARGO_MANIFEST_DIR"),
    "/../../../python-avd/pyavd/_eos_designs/schema/schema_fragments/"
);

const TEST_DATA: &str = "{'fabric_name': 'foo', 'type': 123}";


pub fn benchmark_init_store_from_fragments(c: &mut Criterion) {
    let mut group = c.benchmark_group("sample-size-10");
    group.sample_size(10);
    group.bench_function("init_store_from_fragments", |b| {
        b.iter(|| {
            init_store_from_fragments(
                EOS_CLI_CONFIG_GEN_FRAGMENTS.into(),
                EOS_DESIGNS_FRAGMENTS.into(),
            )
        })
    });
    group.finish();
}

pub fn benchmark_get_validated_data(c: &mut Criterion) {
    c.bench_function("get_validated_data", |b| {
        b.iter(|| get_validated_data(TEST_DATA, "eos_designs"));
    });
}

criterion_group!(
    benches,
    benchmark_init_store_from_fragments,
    benchmark_get_validated_data
);
criterion_main!(benches);
