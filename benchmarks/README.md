<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# AVD Benchmarks

This directory contains performance benchmarks for Arista AVD using [pytest-codspeed](https://github.com/CodSpeedHQ/pytest-codspeed).

## Overview

The benchmark suite tests the performance of critical AVD operations:

1. **PyAVD API Functions** (`test_pyavd_api.py`)

   Tests core API functions using the `eos_designs_unit_tests` molecule scenario.
   **Important:** Most tests process **ALL devices** in the scenario (not just one) to:
   - Get comprehensive coverage across different device types (spines, leafs, MLAG pairs, etc.)
   - Detect regressions that only affect specific device configurations
   - Avoid false regressions when a single test device changes

   **All benchmarks process ALL devices in the scenario:**
   - `test_validate_inputs_benchmark` - Input validation for all devices
   - `test_get_avd_facts_benchmark` - AVD facts generation for entire fabric
   - `test_get_device_structured_config_benchmark` - Structured config generation for all devices
   - `test_validate_structured_config_benchmark` - Structured config validation for all devices
   - `test_get_device_config_benchmark` - EOS CLI rendering (Jinja2) for all devices
   - `test_get_device_doc_benchmark` - Documentation generation for all devices
   - `test_get_fabric_documentation_benchmark` - Fabric-wide documentation
   - `test_get_device_test_catalog_benchmark` - ANTA test catalog for all devices

2. **Molecule Scenarios** (`test_molecule_scenarios.py`)
   - `test_molecule_scenario_full_workflow_benchmark` - Complete end-to-end workflow for real molecule scenarios
   - Tests the full workflow: validate → facts → structured_config → eos_config
   - Covers 16 different molecule scenarios:
     - **EOS Designs**: `eos_designs_unit_tests`, `eos_designs-l2ls`, `eos_designs-mpls-isis-sr-ldp`, `eos_designs-twodc-5stage-clos`
     - **EVPN**: `evpn_underlay_ebgp_overlay_ebgp`, `evpn_underlay_isis_overlay_ibgp`, `evpn_underlay_ospf_overlay_ebgp`, `evpn_underlay_rfc5549_overlay_ebgp`
     - **Examples**: `example-campus-fabric`, `example-cv-pathfinder`, `example-dual-dc-l3ls`, `example-isis-ldp-ipvpn`, `example-l2ls-fabric`, `example-single-dc-l3ls`, `example-single-dc-l3ls-ipv6`
   - Excludes: `eos_designs_negative_unit_tests` (expected to fail), `eos_designs_deprecated_vars` (legacy)

3. **Large Fabric Scaling** (`test_large_fabric_scaling.py`)

   Tests at **3 scales** (15, 150, 1500 devices) to understand how performance scales:
   - **15 devices**: Small fabric baseline
   - **150 devices**: 10x scale (should be ~10x slower if linear)
   - **1500 devices**: 100x scale (detects O(n²) issues if much slower than 100x)

   The 150 and 1500-device tests use a realistic topology: 20% spines, 50% l3leaf, 30% l2leaf.

   **Why these scales?** Comparing performance across 10x and 100x scales helps detect:
   - Linear scaling (O(n)) - Good! 10x devices = 10x time
   - Quadratic scaling (O(n²)) - Bad! 10x devices = 100x time
   - Algorithmic regressions that only appear at scale

   **Individual workflow step benchmarks:**
   - `test_large_fabric_validation_benchmark` - Input validation only
   - `test_large_fabric_facts_generation_benchmark` - AVD facts generation only
   - `test_large_fabric_structured_config_benchmark` - Structured config generation only (typically the slowest step)

   **End-to-end workflow benchmark:**
   - `test_large_fabric_full_workflow_benchmark` - Complete workflow:
     1. Validate inputs
     2. Generate AVD facts
     3. Generate structured configs
     4. Render EOS configs

## Viewing Results (from a CI run)

Benchmark results are available on [CodSpeed](https://codspeed.io/aristanetworks/avd).

CodSpeed provides:

- **Performance trends** over time
- **Regression detection** with automatic alerts
- **Flame graphs** for detailed profiling
- **PR comparisons** showing performance impact
- **Historical data** across all commits and branches

## CI vs Local Benchmarks

### CI Benchmarks (GitHub Actions)

**PR Benchmarks (with `benchmark` label):**

- Scale benchmarks: 15 and 150 devices (8 tests)
- 4 shards for parallel execution
- **Approval required:** Users with `admin` or `maintain` permissions auto-approved; others require manual approval from maintainers

**Weekly Scheduled Benchmarks:**

- Scale benchmarks: 15, 150, and 1500 devices (12 tests)
- Multiple Python/Ansible version combinations
- 4 shards per version
- Runs automatically without approval

**Manual Workflow Trigger:**

- Same as scheduled benchmarks
- **Approval required:** Users with `admin` or `maintain` permissions auto-approved; others require manual approval from maintainers

**Why limited scope in CI:**

- API benchmarks (443 devices) are too resource-intensive for simulation mode
- Molecule scenarios would fail in CI
- Scale benchmarks provide good performance tracking

### Local Benchmarks (Full Suite)

**All benchmarks available locally:**

- **API benchmarks** (8 tests, 443 devices) - `make benchmark-api` - Not in CI
- **Scale benchmarks** (all scales) - `make benchmark-scaling` - Partial in CI
- **Molecule scenarios** (16 tests) - `pytest --codspeed benchmarks/test_molecule_scenarios.py` - Not in CI
- **All benchmarks** - `make benchmark`

### Approval Process

**Environment Setup (one-time):**

1. Go to repository Settings → Environments
2. Create environment: `benchmark-approval`
3. Enable "Required reviewers"
4. Add `avd-maintainers` team as reviewers

**How it works:**

- **Admin/Maintain permissions:** Benchmarks run immediately
- **Write/Read permissions:** Requires approval from `avd-maintainers` team
- **Scheduled runs:** Always run automatically

## Running Benchmarks Locally

### Prerequisites

Install the benchmark dependencies:

```bash
pip install --group dev --group benchmark --upgrade
```

Build schemas and templates:

```bash
cd python-avd
make compile-schemas
make compile-templates
```

### Using Makefile (Recommended)

```bash
# From python-avd directory
cd python-avd
make benchmark

# Or from repo root
cd benchmarks
pytest --codspeed .
```

**Makefile targets:**

- `make benchmark` - Run all benchmarks
- `make benchmark-api` - Run only PyAVD API benchmarks (faster)
- `make benchmark-scaling` - Run only large fabric scaling benchmarks

### Using pytest Directly

```bash
# From repo root
pytest --codspeed benchmarks

# Run specific benchmark file
pytest --codspeed benchmarks/test_pyavd_api.py

# Run specific benchmark test
pytest --codspeed benchmarks/test_pyavd_api.py::test_validate_inputs_benchmark

# Run with pytest -k filter
pytest --codspeed benchmarks -k "test_get_avd_facts"
```

## Adding New Benchmarks

1. Create a new test function in an existing file or new file
2. Use the `@benchmark` decorator from `pytest_codspeed`
3. Follow the pattern:

```python
from pytest_codspeed import BenchmarkFixture

def test_my_benchmark(benchmark: BenchmarkFixture) -> None:
    # Setup code (not timed)
    data = prepare_data()

    # Benchmark code (timed)
    @benchmark
    def _() -> None:
        result = my_function(data)
        assert result is not None
```

## Best Practices

1. **Disable logging** during benchmarks to avoid timing overhead

   ```python
   logging.disable(logging.CRITICAL)
   # ... benchmark code ...
   logging.disable(logging.NOTSET)
   ```

2. **Prepare data outside the benchmark** - Setup should not be timed

   ```python
   # Good: Setup outside @benchmark
   all_inputs = prepare_inputs()
   avd_facts = get_avd_facts(all_inputs)

   @benchmark
   def _():
       result = get_device_structured_config(...)
   ```

3. **Use assertions** to verify correctness

   ```python
   @benchmark
   def _():
       result = my_function()
       assert result is not None  # Ensures function actually runs
   ```

4. **Keep benchmarks focused** on a single operation
   - Benchmark one API function at a time
   - Avoid mixing multiple operations in one benchmark

## Known Limitations

Several API functions currently require dict inputs instead of accepting EOSConfig models directly. These are marked with TODO comments in the code:

1. `validate_structured_config` - Should accept EOSConfig models
2. `AVDFabricData.from_structured_configs` - Should accept EOSConfig models
3. `get_device_test_catalog` - Should accept EOSConfig models

These conversions add overhead and should be addressed in future improvements.
