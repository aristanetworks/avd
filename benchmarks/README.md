<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# AVD Benchmarks

This directory contains performance benchmarks for Arista AVD using
`pytest-codspeed`.

## Benchmark Suite

The default CodSpeed suite is intentionally small and stable:

- `test_molecule_scenarios.py` benchmarks per-host validation, structured config
  generation, and EOS config rendering for representative hosts from the
  `eos_designs_unit_tests` molecule scenario. Fabric facts are prepared outside
  the timed path. It also benchmarks fabric-wide facts generation for the full
  scenario.
- `test_large_fabric_scaling.py` benchmarks a deterministic synthetic full
  workflow. The 15-device case runs in the default suite; the 150-device case is
  marked `benchmark_scale` and is only intended for full/manual runs.

The benchmark suite does not invoke Molecule CLI, Docker, CloudVision, ANTA
runner, or network services.

## GitHub Actions

The standalone `Benchmarks` workflow runs on `ubuntu-latest` with tokenless
CodSpeed upload and no write-capable checkout token. It runs on:

- Pushes to `devel` affecting PyAVD, benchmark, molecule fixture, dependency, or
  benchmark workflow files.
- Pull requests with the `benchmark` label.

Default CI runs:

```bash
python -m pytest --codspeed \
  benchmarks/test_molecule_scenarios.py \
  benchmarks/test_large_fabric_scaling.py \
  -m "not benchmark_scale" \
  -q
```

Local full-suite runs include the 150-device scale benchmark. They do not add an
all-host render benchmark for the full molecule scenario; that kind of load test
is intentionally outside the CodSpeed suite.

```bash
python -m pytest --codspeed benchmarks -q
```

## Local Usage

Install the benchmark dependencies from the repository root:

```bash
pip install --group dev --group benchmark --upgrade
make -C python-avd dep
```

Run benchmarks from the repository root:

```bash
python -m pytest --codspeed benchmarks -q
python -m pytest --codspeed benchmarks/test_molecule_scenarios.py -q
python -m pytest --codspeed benchmarks/test_large_fabric_scaling.py -m "not benchmark_scale" -q
```

Or use the `python-avd` Makefile targets:

```bash
cd python-avd
make benchmark
make benchmark-molecule
make benchmark-scaling
```

## Adding Benchmarks

- Keep benchmark IDs stable across runs.
- Prepare expensive fixture data outside the timed function.
- Use assertions inside the timed path so the benchmark cannot silently skip the
  work.
- Batch very small operations instead of adding noisy micro-benchmarks.
- Keep default CI benchmark count and runtime low; reserve larger scale tests for
  manual full-suite runs.
