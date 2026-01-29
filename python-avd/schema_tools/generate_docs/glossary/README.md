# Glossary Documentation

This directory contains the custom glossary definitions for the AVD documentation.

## Files in This Directory

- **`custom_glossary.yml`** - Custom glossary entries that you can add manually (source file)
- **`README.md`** - This documentation file

## Related Files

- **`../glossarygen.py`** - Glossary generation code
- **`../glossaryentrygen.py`** - Glossary entry generation code

## Generated Output

The generated glossary is located at:
- **`docs/glossary/glossary.md`** - The consolidated glossary (auto-generated, do not edit manually)

## How the Glossary Works

The glossary is automatically generated from two sources:

### 1. Schema-Based Entries

Fields in the AVD schemas can be marked for inclusion in the glossary by adding `glossary: true` to their `documentation_options`:

```yaml
# In a schema fragment file (e.g., hardware.schema.yml)
update_default_result_permit:
  type: bool
  description: Accept the packets when access-list is being updated.
  documentation_options:
    glossary: true
```

**Important Notes:**
- Only leaf fields (str, int, bool) are included in the glossary
- Container types (dict, list) are automatically excluded
- Terms are automatically formatted in Title Case with spaces (e.g., `update_default_result_permit` → "Update Default Result Permit")

### 2. Custom Glossary Entries

You can add custom terms and definitions that are not part of the schema by editing `python-avd/schema_tools/generate_docs/glossary/custom_glossary.yml`.

#### Format

```yaml
- term: "Your Term Here"
  description: |
    Your description here.
    Can be multiline.
```

#### Example

```yaml
- term: "BGP"
  description: |
    Border Gateway Protocol - A standardized exterior gateway protocol designed to exchange
    routing and reachability information among autonomous systems on the Internet.

- term: "VXLAN"
  description: |
    Virtual Extensible LAN - A network virtualization technology that uses a VLAN-like
    encapsulation technique to encapsulate OSI layer 2 Ethernet frames within layer 4 UDP datagrams.
```

## Generating the Glossary

After adding schema fields with `glossary: true` or adding custom entries to `custom_glossary.yml`, rebuild the schemas:

```bash
cd python-avd
python scripts/build_schemas.py
```

This will regenerate `glossary.md` with all entries (both schema-based and custom) sorted alphabetically.

## Glossary Entry Format

Each glossary entry appears in the following format:

```markdown
### Term Name

Description of the term.
```

The glossary is clean and minimal, showing only the term heading and description.

## Best Practices

1. **Use schema-based entries** for AVD configuration fields that users need to understand
2. **Use custom entries** for:
   - Networking concepts and protocols (BGP, VXLAN, EVPN, etc.)
   - Arista-specific terminology
   - General terms that help users understand AVD
3. **Keep descriptions concise** but informative
4. **Use proper capitalization** for terms (they will appear exactly as you type them in custom_glossary.yml)
5. **Avoid duplicates** - check existing entries before adding new ones

## Location in Documentation

The glossary is accessible in the MkDocs navigation under:
- **Glossary** → `docs/glossary/glossary.md`

