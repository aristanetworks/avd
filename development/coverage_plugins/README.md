<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# Coverage Plugins

This package contains coverage.py plugins used by the AVD test suite.

## Jinja Template Coverage

`coverage_plugins.jinja` maps execution of Jinja compiled Python modules back to the checked-in `.j2` template files.

The plugin is intended for this workflow:

1. `coverage run` executes tests while the compiled template `.py` files exist.
2. The file tracer maps compiled-template execution to source `.j2` filenames.
3. `coverage report` and `coverage xml` operate on the checked-in `.j2` files only.

The report step must not require compiled template artifacts. This keeps downstream tools such as Codecov focused on checked-in source files instead of generated, gitignored files.

## Configuration

Enable the plugin in `pyproject.toml`:

```toml
[tool.coverage.run]
plugins = [
  "coverage_plugins.jinja",
]
source_dirs = [
  "python-avd/pyavd/_eos_cli_config_gen/j2templates",
  "python-avd/pyavd/_eos_designs/j2templates",
]

[tool.coverage.coverage_plugins.jinja]
compiled_template_roots = [
  "python-avd/pyavd/_eos_cli_config_gen/j2templates/compiled_templates",
  "python-avd/pyavd/_eos_designs/j2templates/compiled_templates",
]
```

`compiled_template_roots` is required and is used during `coverage run` only. It tells the tracer where generated Jinja Python modules can be found. Reporting should work without those directories being present.

Do not omit compiled template paths in `[tool.coverage.run]`; coverage must be allowed to see those files so the tracer can claim them and remap execution to `.j2` files.

## Line Coverage

Line coverage is based on generated Python execution, Jinja `debug_info`, and explicit runtime evidence from generated `yield` statements.

The plugin reports these template lines as executable:

- Static output lines, including intentional blank lines rendered as Markdown structure.
- Output expression lines, including mixed text and expressions.
- Jinja control statement lines such as `if`, `elif`, `for`, and `set`.
- Static output inside conditionals and loops.

Jinja `debug_info` does not map every rendered static line back to source. The plugin supplements `debug_info` by parsing generated `yield` statements and matching rendered static output back to static source-template tokens. This includes blank-only rendered output when the source line is intentionally blank.

Blank-only static output is credited only when the generated Python gives enough runtime evidence. For example, if Jinja compiles a conditional body as a generated `yield "\n"` before a `for` loop, the plugin maps that generated yield to the blank source line inside the `if` body. Jinja may insert generated `pass` statements before the yield; those are ignored while looking for the first real generated body statement.

Generated Python lines are credited to template lines only when the mapping is explicit enough to be useful. Runtime scaffolding that cannot be tied confidently to a source line is ignored instead of being assigned to the nearest previous template line.

Examples of ignored generated scaffolding include:

- Loop variable cleanup.
- Jinja runtime bookkeeping.
- Generated `pass` statements.
- Missing filter or test lookup fallback code.
- Other generated assignments that do not directly correspond to template behavior.

This means output lines should only be marked covered when the template actually rendered that output or evaluated that expression.

## Branch Coverage

The plugin also reports source-level branch arcs for common Jinja control flow:

- `if`
- `elif`
- `else`
- `for` loop body execution
- `for ... else` when the template has an explicit `{% else %}` block

Normal `for` loops without an explicit `{% else %}` do not report the empty-iteration path as a missing branch. In AVD templates, an empty loop without an `else` usually means there was no optional input to render, not that an important source branch was untested.

Top-level optional guards without `elif` or `else` are marked as no-branch lines. These are commonly used to wrap optional EOS feature sections and would otherwise add noisy `line->exit` misses across many templates.

Some Jinja body statements, especially `set`, `do`, and static output, execute through generated Python scaffolding instead of clean source-to-source arcs. When coverage records generated code entering a reportable body line, the plugin credits the corresponding source branch arc. This prevents false partial branches for conditionals whose body was executed but whose body statement did not produce a normal Python frame mapped directly from the source `if` line.

## Expected Noise

The plugin prefers reporting meaningful source coverage over hiding possible template behavior, so some branch misses can still be noisy. Treat Jinja branch coverage as a useful signal, not as a perfect equivalent of Python branch coverage.

Findings are most likely to need review when they involve these patterns.

### Optional Nested Input Guards

```jinja
1  {% if feature.enabled %}
2  feature
3  {% if feature.optional %}
4  optional
5  {% endif %}
6  after
7  {% endif %}
```

If `feature.enabled` is rendered but `feature.optional` is absent, the `optional` line is reported missing. This is useful when the optional output should be tested, but it can also be noisy when the nested guard only reflects an optional input shape.

Typical finding:

```text
Missing: 4
```

This means line 4 did not render. The inner guard on line 3 was evaluated, but the plugin does not currently report line 3 as a partial branch in this shape because line 3 only has one modeled source-level exit.

### Long `elif` Chains

```jinja
1  {% if mode == 'a' %}
2  alpha
3  {% elif mode == 'b' %}
4  bravo
5  {% elif mode == 'c' %}
6  charlie
7  {% else %}
8  delta
9  {% endif %}
```

Rendering only `mode == 'a'` reports the unvisited `elif` and `else` alternatives as missing branches. This is usually correct, but long selector-style chains can produce several branch misses from one template line group.

Typical finding:

```text
Missing: 3, 4, 5, 6, 8, 1->3, 3->4, 3->5, 5->6, 5->8
```

This means line 1 took the `alpha` branch, so the false path to line 3 was not executed. Lines 3 and 5 are unvisited `elif` checks, and lines 4, 6, and 8 are their unrendered output bodies.

### Conditions That Build Later Output

```jinja
1  {% if dangerous %}
2  {% set prefix = 'dangerous ' %}
3  {% else %}
4  {% set prefix = '' %}
5  {% endif %}
6  value {{ prefix }}done
```

The output line can be covered while one assignment branch is still reported missing. This is useful when both rendered variants matter, but it can feel noisy because the visible output is concentrated on a later line.

Typical finding when `dangerous` is false:

```text
Missing: 2, 1->2, 1->4
```

Line 6 rendered, but line 2 was not executed. The branch arcs show that only one assignment path was taken before the shared output line.

### Nested Loops With Conditional Output

```jinja
1  {% for parent in parents %}
2  parent {{ parent.name }}
3  {% for child in parent.children %}
4  {% if child.enabled %}
5  child {{ child.name }}
6  {% endif %}
7  {% endfor %}
8  {% endfor %}
```

If a child exists but `child.enabled` is false, the child output branch is reported missing. This catches untested nested output, but it can be noisy when the nested condition represents sparse optional data.

Typical finding:

```text
Missing: 5, 4->5
```

Line 4 was evaluated for a child, but the output on line 5 did not render. The modeled false path leaving the inner condition (`4->exit`) was covered.

### Complex Jinja Expressions

```jinja
1  {% if wrapper %}
2  {% if item.enabled and item.name is defined %}
3  item {{ item.name }}
4  {% endif %}
5  after
6  {% endif %}
```

Rendering `wrapper` with `item.enabled` false reports the true output branch as missing. The plugin reports the source-level branch, not every generated Python sub-expression, so the finding should be read as “the full condition never rendered its body.”

Typical finding:

```text
Missing: 3, 2->3
```

Line 2 was evaluated, but the full condition was false and the output on line 3 did not render. The report does not distinguish which part of the compound expression made it false.

These misses can still reveal real gaps in template test data, so they are intentionally reported unless they are known to be generated scaffolding or broad optional-section guards.

## Report Artifacts

Coverage XML should reference `.j2` files, not files under `compiled_templates`.

The compiled template files are runtime inputs for test execution. They are not report artifacts and should not be uploaded to coverage consumers.
